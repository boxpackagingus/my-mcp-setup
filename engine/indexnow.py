"""IndexNow: tells Bing (which feeds ChatGPT search and Copilot), Yandex and others about new pages at once.

The Chimera Engine plugin (1.1+) serves the key file at /<key>.txt and gives the key to the
engine through the API. Without it, submission is skipped.
"""
from datetime import date
from urllib.parse import urlparse

import requests

from . import config


def key(cfg):
    import os
    if not (os.environ.get("WP_USER") and os.environ.get("WP_APP_PASSWORD")):
        return None
    base = cfg["site"]["base_url"].rstrip("/")
    try:
        r = requests.get(f"{base}/?rest_route=/chimera/v1/indexnow",
                         auth=(config.env("WP_USER"), config.env("WP_APP_PASSWORD")), timeout=30)
        return r.json().get("key") if r.ok else None
    except (requests.RequestException, ValueError):
        return None


def submit(cfg, urls):
    """Returns a short status string for the dashboard."""
    if not urls:
        return ""
    k = key(cfg)
    if not k:
        return "Skipped (plugin 1.1 needed)"
    host = urlparse(cfg["site"]["base_url"]).netloc
    try:
        r = requests.post("https://api.indexnow.org/indexnow", timeout=30, json={
            "host": host, "key": k, "keyLocation": f"https://{host}/{k}.txt", "urlList": urls})
    except requests.RequestException as e:
        return f"Failed ({e.__class__.__name__})"
    if r.status_code in (200, 202):
        return f"Sent {date.today().isoformat()}"
    return f"Failed ({r.status_code})"
