"""Search Console and GA4 data through the Site Kit by Google plugin on the WordPress site.

Used when no Google service-account key is configured. The engine's WordPress user must be
allowed to view Site Kit's shared Search Console and Analytics data (Site Kit → Dashboard
sharing). URL Inspection and sitemap submission are not available through Site Kit.
"""
import requests

from . import config


def _get(route, params):
    base = config.env("WP_URL").rstrip("/")
    auth = (config.env("WP_USER"), config.env("WP_APP_PASSWORD"))
    r = requests.get(f"{base}/?rest_route=/google-site-kit/v1/{route}", auth=auth, params=params, timeout=90)
    if r.status_code >= 400:
        raise RuntimeError(f"Site Kit error {r.status_code}: {r.text[:300]}")
    return r.json()


def available():
    try:
        p = _get("core/user/data/permissions", {})
    except Exception:
        return False
    return bool(p.get('googlesitekit_read_shared_module_data::["search-console"]')) and \
        bool(p.get('googlesitekit_read_shared_module_data::["analytics-4"]'))


def gsc_query(start, end, dimensions, row_limit=25000):
    rows = _get("modules/search-console/data/searchanalytics",
                {"startDate": start, "endDate": end, "dimensions": ",".join(dimensions), "rowLimit": row_limit})
    out = []
    for row in rows or []:
        item = dict(zip(dimensions, row.get("keys", [])))
        item.update(clicks=row.get("clicks", 0), impressions=row.get("impressions", 0),
                    ctr=row.get("ctr", 0), position=row.get("position", 0))
        out.append(item)
    return out


def ga4_report(start, end, dimensions, metrics, event_name=None, limit=10000):
    params = {"startDate": start, "endDate": end, "limit": limit}
    for i, d in enumerate(dimensions):
        params[f"dimensions[{i}][name]"] = d
    for i, m in enumerate(metrics):
        params[f"metrics[{i}][name]"] = m
    if event_name:
        params["dimensionFilters[eventName]"] = event_name
    res = _get("modules/analytics-4/data/report", params)
    out = []
    for row in res.get("rows", []) or []:
        item = {d: v.get("value") for d, v in zip(dimensions, row.get("dimensionValues", []))}
        for m, v in zip(metrics, row.get("metricValues", [])):
            item[m] = float(v.get("value") or 0)
        out.append(item)
    return out
