"""Writes the dashboard's data files (dashboard/export/*.json) from the engine's records.

The dashboard artifact reads these files. Numbers Google hasn't supplied yet are null,
so the dashboard shows a dash instead of a misleading zero.
"""
from datetime import datetime, timezone

from . import config

OUT = config.ROOT / "dashboard" / "export"


def _spec(slug):
    return config.read_json(config.PUBLISHED / f"{slug}.json", {})


def run(cfg):
    pages = config.read_json(config.DATA / "pages.json", [])
    summary = config.read_json(config.DATA / "summary.json", {"history": []})
    latest = summary.get("latest") or {}
    queue = config.read_json(config.DATA / "queue.json", {"candidates": []}).get("candidates", [])
    google = bool(latest)

    page_rows, keyword_rows, seen = [], [], set()
    for p in sorted(pages, key=lambda p: p.get("published", ""), reverse=True):
        spec = _spec(p["slug"])
        page_rows.append({
            "slug": p["slug"],
            "kind": "Blog" if spec.get("kind") == "blog" else "Guide",
            "title": spec.get("h1") or p["query"],
            "url": p["url"],
            "keyword": p["primary_keyword"],
            "published": p.get("published"),
            "words": p.get("words"),
            "indexed": {"PASS": "Indexed", "NEUTRAL": "Not yet", "FAIL": "Problem"}.get(
                p.get("index_verdict"), "Not checked"),
            "impressions": p.get("impressions_28d") if google else None,
            "clicks": p.get("clicks_28d") if google else None,
            "visits": p.get("sessions_28d") if google else None,
            "ai_visits": p.get("ai_sessions_28d") if google else None,
            "leads": p.get("leads_28d") if google else None,
        })
        for kind, words in (("Main", [spec.get("primary_keyword") or p["primary_keyword"]]),
                            ("Supporting", spec.get("secondary_keywords", []))):
            for kw in words:
                key = kw.lower()
                if key in seen:
                    continue
                seen.add(key)
                keyword_rows.append({"keyword": kw, "kind": kind, "page": p["slug"]})

    from datetime import date as _date
    today = _date.today().isoformat()
    blog_rows = [{
        "slug": r["slug"], "title": r["title"], "url": r["url"], "published": r["published"],
        "category": _spec(r["slug"]).get("category", ""), "banner": (_spec(r["slug"]).get("hero_image") or {}).get("url"),
        "words": r["words"], "indexed": r["indexed"], "impressions": r["impressions"], "clicks": r["clicks"],
        "visits": r["visits"], "leads": r["leads"],
        "indexnow": next((p.get("indexnow") for p in pages if p["slug"] == r["slug"]), None) or "Not sent",
    } for r in page_rows if r["kind"] == "Blog"]

    totals = [{
        "pages_live": len(pages),
        "guides_live": sum(r["kind"] == "Guide" for r in page_rows),
        "blogs_live": len(blog_rows),
        "blogs_today": sum(b["published"] == today for b in blog_rows),
        "blogs_per_day": cfg["publishing"].get("blogs_per_day", 5),
        "blogs_indexed": sum(b["indexed"] == "Indexed" for b in blog_rows),
        "location": f'{cfg["site"].get("location", "")} · {cfg["site"].get("region", "")}',
        "keywords_used": len(keyword_rows),
        "queries_found": len(queue),
        "impressions": latest.get("impressions_28d") if google else None,
        "clicks": latest.get("clicks_28d") if google else None,
        "visits": latest.get("sessions_28d") if google else None,
        "ai_visits": latest.get("ai_sessions_28d") if google else None,
        "leads": latest.get("leads_28d") if google else None,
        "pages_indexed": latest.get("pages_indexed") if google else None,
        "site_files_ok": sum(f["status"] == "OK" for f in config.read_json(config.DATA / "sitecheck.json", {"files": []})["files"]),
        "site_files_total": len(config.read_json(config.DATA / "sitecheck.json", {"files": []})["files"]),
        "pages_per_day": cfg["publishing"]["pages_per_day"],
        "google_connected": google,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }]

    ga = {r["date"]: r for r in summary.get("ga_daily", [])}
    # One row per day for the last 28 days, with zeros where Google has nothing yet.
    gsc = {r["date"]: r for r in summary.get("gsc_daily", [])}
    daily = []
    if google:
        from datetime import date, timedelta
        end = date.today() - timedelta(days=1)
        for i in range(27, -1, -1):
            d = (end - timedelta(days=i)).isoformat()
            r, g = gsc.get(d, {}), ga.get(d.replace("-", ""), ga.get(d, {}))
            daily.append({"day": d, "impressions": int(r.get("impressions", 0)), "clicks": int(r.get("clicks", 0)),
                          "visits": int(g.get("sessions", 0) or 0)})

    done = {p["slug"] for p in pages} | {p["query"].lower() for p in pages}
    queue = [c for c in queue if c.get("slug") not in done and c["query"].lower() not in done]
    upcoming = [{"query": c["query"], "source": {"autocomplete": "Google suggestions",
                 "search_console": "Your Search Console"}.get(c["source"], c["source"]),
                 "volume": c.get("volume"), "score": c.get("score")} for c in queue[:15]]

    check = config.read_json(config.DATA / "sitecheck.json", {"files": [], "pages": []})
    site_files = [{k: f.get(k) for k in ("file", "url", "status", "http", "items", "items_label", "note", "checked")}
                  for f in check["files"]]
    page_checks = [{k: c.get(k) for k in ("slug", "url", "published", "live", "in_sitemap", "in_llms",
                                         "markdown", "schema", "checked")} for c in check["pages"]]

    indexing = []
    for p in sorted(pages, key=lambda p: p.get("published", ""), reverse=True):
        verdict = p.get("index_verdict")
        indexing.append({
            "slug": p["slug"], "url": p["url"], "published": p.get("published"),
            "google": {"PASS": "Indexed", "NEUTRAL": "No search data yet", "FAIL": "Problem"}.get(
                verdict, "Waiting for Google" if not google else "Not checked yet"),
            "coverage": p.get("index_coverage") or "",
            "last_crawl": (p.get("index_last_crawl") or "")[:10] or None,
            "bing": p.get("indexnow") or "Not sent",
        })

    runs = [dict(r) for r in reversed(config.read_json(config.DATA / "runs.json", []))][:60]

    opp_money, opp_fixes, ai_vis, links = _opportunities()
    if totals:
        totals[0]["money_queries"] = len(opp_money)
        totals[0]["money_top20"] = sum(1 for r in opp_money if r["position"] <= 20)
        totals[0]["fixes_open"] = len(opp_fixes)
        totals[0]["ai_chimera_named"] = next((r["answers_named"] for r in ai_vis if r["brand"] == "Chimera"), None)
        totals[0]["ai_answers"] = ai_vis[0]["answers"] if ai_vis else None
        totals[0]["links_open"] = sum(1 for r in links if r["status"] == "new")

    files = {"totals": totals, "pages": page_rows, "opp_money": opp_money, "opp_fixes": opp_fixes,
             "ai_visibility": ai_vis, "link_prospects": links, "blogs": blog_rows, "keywords": keyword_rows,
             "daily": daily, "upcoming": upcoming, "site_files": site_files,
             "page_checks": page_checks, "indexing": indexing, "runs": runs}
    for name, rows in files.items():
        config.write_json(OUT / f"{name}.json", rows)
    return {k: len(v) for k, v in files.items()}


def _opportunities():
    """Rows for the dashboard's Opportunities section, from the opportunity finder and the two free workers."""
    opp = config.read_json(config.DATA / "opportunities.json", {})
    hist = sorted((config.DATA / "money_positions").glob("*.json")) if (config.DATA / "money_positions").exists() else []
    prev = {}
    for f in hist:
        if f.stem < opp.get("date", ""):
            prev = config.read_json(f, {})
    money = []
    for r in opp.get("money_queries", []):
        before = prev.get(r["query"] + " | " + r["slug"])
        pos = round(r["position"], 1)
        money.append({"query": r["query"], "page": r["slug"], "position": pos, "previous": before,
                      "change": round(before - pos, 1) if before is not None else None,
                      "impressions": r["impressions"], "clicks": r.get("clicks", 0)})
    fixes = [{"query": c["query"], "keep": c["keep"], "others": ", ".join(p[0] for p in c["pages"] if p[0] != c["keep"]),
              "pages": len(c["pages"]), "impressions": c["impressions"], "intent": c["intent"]}
             for c in opp.get("cannibalization", []) if c["intent"] in ("money-local", "money-national")]
    vis_days = sorted((config.DATA / "ai_visibility").glob("2*.json")) if (config.DATA / "ai_visibility").exists() else []
    ai = []
    if vis_days:
        v = config.read_json(vis_days[-1], {})
        counts = dict(v.get("share_of_answers", {}))
        import re
        ents = {}
        for name, n in v.get("top_entities", []):
            name = re.sub(r"^\d+\.\s*", "", name).rstrip(".")
            ents[name] = ents.get(name, 0) + n
        for name, n in sorted(ents.items(), key=lambda kv: -kv[1])[:15]:
            if name not in counts and n > 1:
                counts[name] = n
        counts = {b: n for b, n in counts.items() if n > 0 or b == "Chimera"}
        for brand, n in sorted(counts.items(), key=lambda kv: (kv[0] != "Chimera", -kv[1], kv[0])):
            ai.append({"brand": brand, "answers_named": n, "answers": v.get("answers", 0), "date": v.get("date"),
                       "share": round(n / v["answers"], 3) if v.get("answers") else None})
    links = [{"name": p["name"], "url": p["url"], "type": p.get("type"), "priority": p.get("priority"),
              "status": p.get("status"), "cost": p.get("cost"), "next_step": p.get("next_step"), "found": p.get("found")}
             for p in config.read_json(config.DATA / "link_prospects.json", [])]
    return money, fixes, ai, links
