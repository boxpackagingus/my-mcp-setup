"""Search Console and Google Analytics 4 access through a service account."""
import base64
import json
from urllib.parse import quote

import requests

from . import config

SCOPES = [
    "https://www.googleapis.com/auth/webmasters",
    "https://www.googleapis.com/auth/analytics.readonly",
]

_token = None


def _credentials_info():
    raw = config.env("GSC_SERVICE_ACCOUNT_KEY_JSON")
    if not raw.lstrip().startswith("{"):
        raw = base64.b64decode(raw).decode()
    return json.loads(raw)


def token():
    global _token
    if _token is None:
        from google.auth.transport.requests import Request
        from google.oauth2 import service_account

        creds = service_account.Credentials.from_service_account_info(
            _credentials_info(), scopes=SCOPES
        )
        creds.refresh(Request())
        _token = creds.token
    return _token


def _post(url, body):
    r = requests.post(url, json=body, headers={"Authorization": f"Bearer {token()}"}, timeout=60)
    if r.status_code >= 400:
        raise RuntimeError(f"Google API error {r.status_code}: {r.text[:500]}")
    return r.json()


def _get(url):
    r = requests.get(url, headers={"Authorization": f"Bearer {token()}"}, timeout=60)
    if r.status_code >= 400:
        raise RuntimeError(f"Google API error {r.status_code}: {r.text[:500]}")
    return r.json()


# ---------- Search Console ----------

def gsc_sites():
    return _get("https://www.googleapis.com/webmasters/v3/sites").get("siteEntry", [])


def gsc_property(domain):
    """Find the Search Console property for the domain (domain or URL-prefix)."""
    sites = [s["siteUrl"] for s in gsc_sites()]
    for candidate in (f"sc-domain:{domain}", f"https://{domain}/", f"https://www.{domain}/"):
        if candidate in sites:
            return candidate
    raise SystemExit(
        f"No Search Console property for {domain} is shared with the service account. "
        f"Properties it can see: {sites or 'none'}"
    )


def gsc_query(prop, start, end, dimensions, row_limit=25000, filters=None):
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "dataState": "final",
    }
    if filters:
        body["dimensionFilterGroups"] = [{"filters": filters}]
    url = f"https://www.googleapis.com/webmasters/v3/sites/{quote(prop, safe='')}/searchAnalytics/query"
    rows = _post(url, body).get("rows", [])
    out = []
    for row in rows:
        item = dict(zip(dimensions, row["keys"]))
        item.update(
            clicks=row["clicks"],
            impressions=row["impressions"],
            ctr=row["ctr"],
            position=row["position"],
        )
        out.append(item)
    return out


def gsc_inspect(prop, url):
    body = {"inspectionUrl": url, "siteUrl": prop}
    res = _post("https://searchconsole.googleapis.com/v1/urlInspection/index:inspect", body)
    r = res.get("inspectionResult", {}).get("indexStatusResult", {})
    return {
        "verdict": r.get("verdict"),
        "coverage": r.get("coverageState"),
        "last_crawl": r.get("lastCrawlTime"),
    }


def gsc_submit_sitemap(prop, sitemap_url):
    url = (
        f"https://www.googleapis.com/webmasters/v3/sites/{quote(prop, safe='')}"
        f"/sitemaps/{quote(sitemap_url, safe='')}"
    )
    r = requests.put(url, headers={"Authorization": f"Bearer {token()}"}, timeout=60)
    return r.status_code < 300


# ---------- Google Analytics 4 ----------

def ga4_report(start, end, dimensions, metrics, dimension_filter=None, limit=10000):
    prop = config.env("GA4_PROPERTY_ID")
    body = {
        "dateRanges": [{"startDate": start, "endDate": end}],
        "dimensions": [{"name": d} for d in dimensions],
        "metrics": [{"name": m} for m in metrics],
        "limit": limit,
    }
    if dimension_filter:
        body["dimensionFilter"] = dimension_filter
    res = _post(f"https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport", body)
    out = []
    for row in res.get("rows", []):
        item = {d: v["value"] for d, v in zip(dimensions, row["dimensionValues"])}
        for m, v in zip(metrics, row["metricValues"]):
            item[m] = float(v["value"])
        out.append(item)
    return out
