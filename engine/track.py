"""Daily tracking: Search Console + GA4 per page, AI-search traffic and leads."""
from datetime import date, timedelta
from urllib.parse import urlparse

import os

import requests

from . import config, google_api, sitekit

PAGES = config.DATA / "pages.json"
SUMMARY = config.DATA / "summary.json"
INSPECT_PER_DAY = 40  # Google allows 2,000/day; keep it light


def classify_ai(source, cfg):
    s = (source or "").lower()
    for engine, domains in cfg["ai_referrers"].items():
        if any(d in s for d in domains):
            return engine
    return None


def run(cfg):
    pages = config.read_json(PAGES, [])
    by_path = {urlparse(p["url"]).path.rstrip("/") + "/": p for p in pages}
    # Site Kit returns the freshest data Google has; the service-account path keeps the 3-day lag.
    end = date.today() - timedelta(days=1 if not os.environ.get("GSC_SERVICE_ACCOUNT_KEY_JSON") else 3)
    start = end - timedelta(days=27)
    yday = (date.today() - timedelta(days=1)).isoformat()
    month_ago = (date.today() - timedelta(days=28)).isoformat()

    use_sitekit = not os.environ.get("GSC_SERVICE_ACCOUNT_KEY_JSON")
    lead_event = cfg["lead"]["ga4_lead_event"]

    if use_sitekit:
        # Site Kit by Google on the WordPress site supplies Search Console and GA4 data.
        site_daily = sitekit.gsc_query(start.isoformat(), end.isoformat(), ["date"])
        page_rows = sitekit.gsc_query(start.isoformat(), end.isoformat(), ["page"])
        # Site Kit allows landingPage (not landingPagePlusQueryString); rename for the shared code below.
        traffic = [dict(r, landingPagePlusQueryString=r.get("landingPage", "")) for r in
                   sitekit.ga4_report(month_ago, yday, ["landingPage", "sessionSource"],
                                      ["sessions", "engagedSessions", "keyEvents"])]
        leads = [dict(r, landingPagePlusQueryString=r.get("landingPage", "")) for r in
                 sitekit.ga4_report(month_ago, yday, ["landingPage", "sessionSource"],
                                    ["eventCount"], event_name=lead_event)]
        ga_daily = sitekit.ga4_report(month_ago, yday, ["date"], ["sessions", "keyEvents"])
    else:
        prop = google_api.gsc_property(cfg["site"]["domain"])
        site_daily = google_api.gsc_query(prop, start.isoformat(), end.isoformat(), ["date"])
        page_rows = google_api.gsc_query(prop, start.isoformat(), end.isoformat(), ["page"])
        # URL inspection: oldest-checked pages first (service-account mode only).
        pages.sort(key=lambda p: p.get("index_checked", ""))
        for p in pages[:INSPECT_PER_DAY]:
            try:
                res = google_api.gsc_inspect(prop, p["url"])
                p["index_verdict"], p["index_coverage"] = res["verdict"], res["coverage"]
                p["index_last_crawl"] = res["last_crawl"]
                p["index_checked"] = date.today().isoformat()
            except RuntimeError as e:
                print(f"Inspect failed for {p['url']}: {e}")
        traffic = google_api.ga4_report(month_ago, yday, ["landingPagePlusQueryString", "sessionSource"],
                                        ["sessions", "engagedSessions", "keyEvents"])
        leads = google_api.ga4_report(month_ago, yday, ["landingPagePlusQueryString", "sessionSource"], ["eventCount"],
                                      dimension_filter={"filter": {"fieldName": "eventName",
                                                                   "stringFilter": {"value": lead_event}}})
        ga_daily = google_api.ga4_report(month_ago, yday, ["date"], ["sessions", "keyEvents"])
    gsc_by_path = {urlparse(r["page"]).path.rstrip("/") + "/": r for r in page_rows}

    ai_totals, site_leads = {}, 0
    for p in pages:
        p.update(sessions_28d=0, ai_sessions_28d=0, leads_28d=0, ai_sources={})
    for r in traffic:
        path = urlparse(r["landingPagePlusQueryString"]).path.rstrip("/") + "/"
        engine = classify_ai(r["sessionSource"], cfg)
        if engine:
            ai_totals[engine] = ai_totals.get(engine, 0) + r["sessions"]
        p = by_path.get(path)
        if p:
            p["sessions_28d"] += r["sessions"]
            if engine:
                p["ai_sessions_28d"] += r["sessions"]
                p["ai_sources"][engine] = p["ai_sources"].get(engine, 0) + r["sessions"]
    for r in leads:
        site_leads += r["eventCount"]
        p = by_path.get(urlparse(r["landingPagePlusQueryString"]).path.rstrip("/") + "/")
        if p:
            p["leads_28d"] += r["eventCount"]

    for p in pages:
        g = gsc_by_path.get(urlparse(p["url"]).path.rstrip("/") + "/", {})
        p.update(clicks_28d=g.get("clicks", 0), impressions_28d=g.get("impressions", 0),
                 position_28d=round(g["position"], 1) if g else None)

    if use_sitekit:
        # Without URL Inspection, a page that earns search impressions is known to be indexed.
        for p in pages:
            if p["impressions_28d"]:
                p["index_verdict"], p["index_coverage"] = "PASS", "Appearing in Google Search"
                p["index_checked"] = date.today().isoformat()
            elif p.get("index_verdict") != "PASS":
                p["index_verdict"], p["index_coverage"] = "NEUTRAL", "No search impressions yet"

    # Form leads recorded by the Chimera Engine plugin (independent of GA4).
    try:
        base = config.env("WP_URL").rstrip("/")
        ls = requests.get(f"{base}/?rest_route=/chimera/v1/leads-summary", timeout=30,
                          auth=(config.env("WP_USER"), config.env("WP_APP_PASSWORD"))).json()
        form_leads, form_by_page = int(ls.get("total", 0)), ls.get("by_page", {})
        for p in pages:
            p["form_leads_28d"] = int(form_by_page.get(urlparse(p["url"]).path, 0))
    except Exception as e:
        print(f"Form lead summary skipped: {e}")
        form_leads = None

    indexed = sum(p.get("index_verdict") == "PASS" for p in pages)
    summary = config.read_json(SUMMARY, {"history": []})
    today = {
        "date": date.today().isoformat(),
        "pages_total": len(pages),
        "pages_indexed": indexed,
        "clicks_28d": sum(r["clicks"] for r in site_daily),
        "impressions_28d": sum(r["impressions"] for r in site_daily),
        "engine_clicks_28d": sum(p["clicks_28d"] for p in pages),
        "sessions_28d": sum(r["sessions"] for r in ga_daily),
        "ai_sessions_28d": sum(ai_totals.values()),
        "ai_by_engine": ai_totals,
        "leads_28d": max(site_leads, form_leads or 0),
        "form_leads_28d": form_leads,
        "source": "Site Kit" if use_sitekit else "Google API",
        "engine_leads_28d": sum(p["leads_28d"] for p in pages),
    }
    summary["history"] = [h for h in summary["history"] if h["date"] != today["date"]] + [today]
    summary["latest"] = today
    summary["gsc_daily"] = site_daily
    summary["ga_daily"] = ga_daily
    config.write_json(SUMMARY, summary)
    config.write_json(PAGES, pages)
    config.write_json(config.DATA / "metrics" / f"{today['date']}.json", {"summary": today, "pages": pages})
    return today
