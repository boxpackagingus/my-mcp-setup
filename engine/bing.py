"""Bing Webmaster Tools (free): what Bing records about thechimeraai.com.

Bing's index feeds Microsoft Copilot and ChatGPT search, so its numbers matter for AI visibility.
Needs BING_WEBMASTER_API_KEY in the environment (free key: Bing Webmaster Tools > Settings > API access).
Pulls search queries, daily traffic, inbound link counts and crawl stats into data/bing/YYYY-MM-DD.json
and data/bing/summary.json. Read-only: it never changes anything in the Bing account.
IndexNow submissions are separate (engine/indexnow.py, run by publish).
"""
import os
import re
from datetime import date, datetime, timezone

import requests

from . import config

API = "https://ssl.bing.com/webmaster/api.svc/json"
SITE = "https://thechimeraai.com/"


def _get(endpoint, key, **params):
    r = requests.get(f"{API}/{endpoint}", params={"apikey": key, **params}, timeout=30,
                     headers={"User-Agent": "ChimeraEngine/1.0 (+https://thechimeraai.com)"})
    r.raise_for_status()
    return r.json().get("d")


def _day(v):
    """Bing dates look like /Date(1700000000000)/ or /Date(1700000000000-0800)/."""
    m = re.search(r"\d{10,}", str(v or ""))
    return datetime.fromtimestamp(int(m.group()) / 1000, timezone.utc).date().isoformat() if m else v


def run(cfg):
    key = os.environ.get("BING_WEBMASTER_API_KEY", "").strip()
    if not key:
        return {"ok": False, "error": "BING_WEBMASTER_API_KEY is not set. Add the free key in the environment settings "
                                      "(see HANDBOOK.md, Bing Webmaster Tools)."}
    out = {"date": date.today().isoformat(), "site": SITE, "errors": {}}
    try:
        sites = _get("GetUserSites", key) or []
        out["verified"] = any(s.get("Url", "").rstrip("/") == SITE.rstrip("/") and s.get("IsVerified") for s in sites)
    except Exception as e:
        return {"ok": False, "error": f"GetUserSites failed: {str(e)[:200]}"}

    def grab(name, endpoint, **p):
        try:
            return _get(endpoint, key, siteUrl=SITE, **p)
        except Exception as e:
            out["errors"][name] = str(e)[:200]
            return None

    q = grab("queries", "GetQueryStats") or []
    out["queries"] = sorted(({"query": x.get("Query"), "impressions": x.get("Impressions", 0), "clicks": x.get("Clicks", 0),
                              "position": x.get("AvgImpressionPosition"), "date": _day(x.get("Date"))} for x in q),
                            key=lambda x: -x["impressions"])[:200]
    t = grab("traffic", "GetRankAndTrafficStats") or []
    out["traffic"] = [{"date": _day(x.get("Date")), "impressions": x.get("Impressions", 0), "clicks": x.get("Clicks", 0)}
                      for x in t]
    links, page = [], 0
    while page < 5:
        d = grab("links", "GetLinkCounts", page=page)
        if not d or not d.get("Links"):
            break
        links += [{"url": x.get("Url"), "count": x.get("Count", 0)} for x in d["Links"]]
        page += 1
        if page >= (d.get("TotalPages") or 1):
            break
    out["links"] = sorted(links, key=lambda x: -x["count"])
    c = grab("crawl", "GetCrawlStats") or []
    out["crawl"] = [{"date": _day(x.get("Date")), "crawled": x.get("CrawledPages", 0), "in_index": x.get("InIndex", 0),
                     "errors": x.get("CrawlErrors", 0)} for x in c][-30:]

    summary = {
        "date": out["date"], "verified": out.get("verified"),
        "impressions": sum(x["impressions"] for x in out["traffic"]), "clicks": sum(x["clicks"] for x in out["traffic"]),
        "queries": len(out["queries"]), "linked_pages": len(out["links"]),
        "inbound_links": sum(x["count"] for x in out["links"]),
        "in_index": out["crawl"][-1]["in_index"] if out["crawl"] else None,
        "top_queries": out["queries"][:10], "errors": out["errors"],
    }
    d = config.ROOT / "data" / "bing"
    d.mkdir(parents=True, exist_ok=True)
    config.write_json(d / f"{out['date']}.json", out)
    config.write_json(d / "summary.json", summary)
    return {"ok": True, **{k: v for k, v in summary.items() if k != "top_queries"}}
