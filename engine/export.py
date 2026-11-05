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

    totals = [{
        "pages_live": len(pages),
        "keywords_used": len(keyword_rows),
        "queries_found": len(queue),
        "impressions": latest.get("impressions_28d") if google else None,
        "clicks": latest.get("clicks_28d") if google else None,
        "visits": latest.get("sessions_28d") if google else None,
        "ai_visits": latest.get("ai_sessions_28d") if google else None,
        "leads": latest.get("leads_28d") if google else None,
        "pages_indexed": latest.get("pages_indexed") if google else None,
        "pages_per_day": cfg["publishing"]["pages_per_day"],
        "google_connected": google,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }]

    ga = {r["date"]: r for r in summary.get("ga_daily", [])}
    daily = []
    for r in summary.get("gsc_daily", []):
        d = r["date"]
        g = ga.get(d.replace("-", ""), ga.get(d, {}))
        daily.append({"day": d, "impressions": r["impressions"], "clicks": r["clicks"],
                      "visits": g.get("sessions")})

    upcoming = [{"query": c["query"], "source": {"autocomplete": "Google suggestions",
                 "search_console": "Your Search Console"}.get(c["source"], c["source"]),
                 "volume": c.get("volume"), "score": c.get("score")} for c in queue[:15]]

    files = {"totals": totals, "pages": page_rows, "keywords": keyword_rows,
             "daily": daily, "upcoming": upcoming}
    for name, rows in files.items():
        config.write_json(OUT / f"{name}.json", rows)
    return {k: len(v) for k, v in files.items()}
