"""Command line for the Chimera engine.

  python -m engine check              Test Google, WordPress and site access
  python -m engine research           Build today's query queue (data/queue.json)
  python -m engine quality FILE...    Run the quality gate on draft specs
  python -m engine publish [--dry-run] Publish drafts that pass (respects the daily limit)
  python -m engine track              Pull Search Console + GA4 numbers
  python -m engine dashboard          Rebuild dashboard/index.html
  python -m engine sitecheck          Check llms.txt, robots.txt, sitemap and every page
  python -m engine export             Write the dashboard data files (dashboard/export/)
  python -m engine status             Show today's limit and queue size
"""
import json
import sys

from . import config


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, args = argv[0], argv[1:]
    cfg = config.load()

    if cmd == "check":
        return check(cfg)
    if cmd == "research":
        from . import research
        queue = research.run(cfg, use_gsc="--no-gsc" not in args)
        print(f"{len(queue)} candidate queries. Top 15:")
        for c in queue[:15]:
            extra = c.get("volume", c.get("impressions", "?"))
            print(f"  {c['score']:>8}  {c['query']}  ({c['source']}, demand {extra})")
        return 0
    if cmd == "quality":
        from . import publish, quality
        failed = 0
        for f in args:
            spec = config.read_json(f, {})
            ok, problems, stats = quality.check(spec, cfg, publish.existing_texts(exclude=spec.get("slug")))
            print(f"{'PASS' if ok else 'FAIL'}  {f}  {stats}")
            for p in problems:
                print(f"   - {p}")
            failed += not ok
        return 1 if failed else 0
    if cmd == "publish":
        from . import publish
        max_pages = int(args[args.index("--max") + 1]) if "--max" in args else None
        print(json.dumps(publish.run(cfg, dry_run="--dry-run" in args, max_pages=max_pages), indent=2))
        return 0
    if cmd == "track":
        from . import track
        print(json.dumps(track.run(cfg), indent=2))
        return 0
    if cmd == "dashboard":
        from . import dashboard
        print(dashboard.build(cfg))
        return 0
    if cmd == "sitecheck":
        from . import sitecheck
        out = sitecheck.run(cfg)
        for f in out["files"]:
            print(f"{f['status']:8} {f['file']:14} {f['items']} {f['items_label']} · {f['note']}")
        for p in out["pages"]:
            print(f"page /{p['slug']}/ live={p['live']} sitemap={p['in_sitemap']} llms={p['in_llms']} md={p['markdown']} schema={p['schema']}")
        return 0
    if cmd == "export":
        from . import export
        print(json.dumps(export.run(cfg), indent=2))
        return 0
    if cmd == "status":
        from . import publish
        remaining, limit = publish.pages_allowed_today(cfg)
        queue = config.read_json(config.DATA / "queue.json", {"candidates": []})["candidates"]
        drafts = list(config.DRAFTS.glob("*.json"))
        print(f"Daily limit {limit}, {remaining} left today. Queue: {len(queue)}. Drafts waiting: {len(drafts)}.")
        return 0
    print(f"Unknown command: {cmd}\n{__doc__}")
    return 2


def check(cfg):
    import requests
    ok = True
    site = cfg["site"]["base_url"]
    try:
        r = requests.get(site, timeout=20)
        print(f"[ok]   Website reachable ({r.status_code})")
    except requests.RequestException as e:
        ok = False
        print(f"[fail] Website not reachable: {e}. Add {cfg['site']['domain']} to Allowed domains.")
    try:
        from . import google_api
        prop = google_api.gsc_property(cfg["site"]["domain"])
        print(f"[ok]   Search Console property: {prop}")
    except (SystemExit, Exception) as e:
        ok = False
        print(f"[fail] Search Console: {e}")
    try:
        from . import google_api
        google_api.ga4_report("7daysAgo", "yesterday", ["date"], ["sessions"])
        print("[ok]   Google Analytics 4")
    except (SystemExit, Exception) as e:
        ok = False
        print(f"[fail] Google Analytics 4: {e}")
    try:
        from .wp import WordPress
        info = WordPress().check()
        print(f"[ok]   WordPress login as {info['user']} {info['roles']}")
        if not info["plugin_active"]:
            ok = False
            print("[fail] Chimera Engine plugin is not active in WordPress")
    except (SystemExit, Exception) as e:
        ok = False
        print(f"[fail] WordPress: {e}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
