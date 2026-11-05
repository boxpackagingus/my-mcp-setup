"""Publishes today's drafts: quality gate → WordPress → records → sitemap ping."""
import shutil
from datetime import date

from . import config, page, quality

PAGES = config.DATA / "pages.json"


def pages_allowed_today(cfg):
    """3 a day at first; 10 a day once enough pages are indexed (the ramp)."""
    pub = cfg["publishing"]
    ramp = pub["ramp"]
    pages = config.read_json(PAGES, [])
    today = date.today().isoformat()
    done_today = sum(1 for p in pages if p.get("published") == today)
    limit = pub["pages_per_day"]
    if pages:
        first = min(p["published"] for p in pages)
        days = (date.today() - date.fromisoformat(first)).days
        checked = [p for p in pages if p.get("index_verdict")]
        rate = sum(p["index_verdict"] == "PASS" for p in checked) / len(checked) if checked else 0
        if days >= ramp["after_days"] and rate >= ramp["min_index_rate"]:
            limit = ramp["target_pages_per_day"]
    return max(0, limit - done_today), limit


def existing_texts():
    texts = []
    for f in config.PUBLISHED.glob("*.json"):
        texts.append(page.plain_text(config.read_json(f, {})))
    return texts


def run(cfg, dry_run=False):
    remaining, limit = pages_allowed_today(cfg)
    drafts = sorted(config.DRAFTS.glob("*.json"))
    report = {"limit": limit, "remaining_before": remaining, "published": [], "failed": [], "skipped": []}
    if not drafts:
        return report

    wp = None if dry_run else _wp()
    pages = config.read_json(PAGES, [])
    texts = existing_texts()

    for f in drafts:
        spec = config.read_json(f, {})
        ok, problems, stats = quality.check(spec, cfg, texts)
        if not ok:
            report["failed"].append({"file": f.name, "problems": problems})
            continue
        if remaining <= 0:
            report["skipped"].append(f.name)
            continue

        spec.setdefault("published", date.today().isoformat())
        spec["updated"] = date.today().isoformat()
        html = page.render_html(spec, cfg)
        md = page.render_markdown(spec, cfg)
        schema = page.render_schema(spec, cfg)
        url = f'{cfg["site"]["base_url"]}/{spec["slug"]}/'

        if dry_run:
            out = config.ROOT / "content" / "preview"
            out.mkdir(parents=True, exist_ok=True)
            (out / f'{spec["slug"]}.html').write_text(html)
            (out / f'{spec["slug"]}.md').write_text(md)
            (out / f'{spec["slug"]}.schema.json').write_text(schema)
            report["published"].append({"slug": spec["slug"], "url": url, "dry_run": True, **stats})
            remaining -= 1
            continue

        result, action = wp.upsert_page(spec, html, md, schema, status=cfg["publishing"]["status"])
        url = result.get("link", url)
        pages = [p for p in pages if p["slug"] != spec["slug"]]
        pages.append({
            "slug": spec["slug"], "query": spec["query"], "url": url, "wp_id": result["id"],
            "published": spec["published"], "primary_keyword": spec["primary_keyword"],
            "volume": spec.get("volume"), "words": stats["words"],
        })
        config.write_json(f, spec)
        shutil.move(str(f), config.PUBLISHED / f.name)
        texts.append(page.plain_text(spec))
        report["published"].append({"slug": spec["slug"], "url": url, "action": action, **stats})
        remaining -= 1

    if not dry_run:
        config.write_json(PAGES, pages)
        if report["published"]:
            _ping_sitemap(cfg)
    return report


def _wp():
    from .wp import WordPress
    return WordPress()


def _ping_sitemap(cfg):
    try:
        from . import google_api
        prop = google_api.gsc_property(cfg["site"]["domain"])
        for path in ("/sitemap_index.xml", "/wp-sitemap.xml"):
            if google_api.gsc_submit_sitemap(prop, cfg["site"]["base_url"] + path):
                break
    except (Exception, SystemExit) as e:  # sitemap ping is nice-to-have
        print(f"Sitemap ping skipped: {e}")
