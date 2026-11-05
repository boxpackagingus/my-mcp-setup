"""Checks the live site: llms.txt, llms-full.txt, robots.txt, sitemap and every engine page.

Writes data/sitecheck.json. Only reads public URLs; needs no login.
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests

from . import config

UA = {"User-Agent": "ChimeraEngine-SiteCheck/1.0"}
AI_BOTS = ["GPTBot", "OAI-SearchBot", "PerplexityBot", "ClaudeBot", "Google-Extended"]


def _get(url):
    try:
        r = requests.get(url, headers=UA, timeout=30, params={"nocache": datetime.now().timestamp()})
        return r.status_code, r.text, r.headers.get("content-type", "")
    except requests.RequestException as e:
        return 0, str(e), ""


def _sitemap_urls(start):
    """Follows a sitemap index and returns every page URL listed."""
    seen, urls, todo = set(), set(), [start]
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    while todo and len(seen) < 50:
        u = todo.pop()
        if u in seen:
            continue
        seen.add(u)
        code, body, _ = _get(u)
        if code != 200:
            continue
        try:
            root = ET.fromstring(body.encode())
        except ET.ParseError:
            continue
        for loc in root.iter(f"{ns}loc"):
            text = (loc.text or "").strip()
            if root.tag.endswith("sitemapindex"):
                todo.append(text)
            else:
                urls.add(text)
    return urls


def _norm(url):
    p = urlparse(url)
    return p.path.rstrip("/") + "/"


def run(cfg):
    base = cfg["site"]["base_url"].rstrip("/")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    files = []

    # robots.txt
    code, robots, _ = _get(base + "/robots.txt")
    sitemap_line = re.search(r"^Sitemap:\s*(\S+)", robots, re.M | re.I) if code == 200 else None
    bots_ok = [b for b in AI_BOTS if code == 200 and re.search(rf"User-agent:\s*{b}\s*\nAllow:\s*/", robots, re.I)]
    blocked_all = code == 200 and re.search(r"User-agent:\s*\*\s*\n(?:[^\n]*\n)*?Disallow:\s*/\s*$", robots, re.M)
    files.append({
        "file": "robots.txt", "url": base + "/robots.txt", "http": code,
        "status": "OK" if code == 200 and not blocked_all else "Problem",
        "items": len(bots_ok), "items_label": "AI crawlers allowed",
        "note": ("Lists the sitemap" if sitemap_line else "No sitemap line") +
                ("; blocks all crawlers!" if blocked_all else ""),
        "checked": now,
    })

    # sitemap
    sitemap_url = sitemap_line.group(1) if sitemap_line else base + "/wp-sitemap.xml"
    smap = _sitemap_urls(sitemap_url)
    files.append({
        "file": "Sitemap", "url": sitemap_url, "http": 200 if smap else _get(sitemap_url)[0],
        "status": "OK" if smap else "Problem",
        "items": len(smap), "items_label": "pages listed",
        "note": "Google reads this to find new pages", "checked": now,
    })

    # llms.txt and llms-full.txt
    code, llms, _ = _get(base + "/llms.txt")
    guides = re.findall(r"^- \[[^\]]+\]\(([^)]+)\)", llms.split("## Guides and answers")[-1], re.M) \
        if code == 200 and "## Guides and answers" in llms else []
    files.append({
        "file": "llms.txt", "url": base + "/llms.txt", "http": code,
        "status": "OK" if code == 200 and llms.startswith("#") else "Problem",
        "items": len(guides), "items_label": "guides listed",
        "note": "Map of your site for AI assistants", "checked": now,
    })
    code_f, full, _ = _get(base + "/llms-full.txt")
    files.append({
        "file": "llms-full.txt", "url": base + "/llms-full.txt", "http": code_f,
        "status": "OK" if code_f == 200 and full.startswith("#") else "Problem",
        "items": full.count("\n---\n\n# ") if code_f == 200 else 0, "items_label": "full guides included",
        "note": f"{len(full.encode()) // 1024} KB of plain text for AI assistants" if code_f == 200 else "Not reachable",
        "checked": now,
    })

    smap_paths = {_norm(u) for u in smap}
    llms_slugs = {_norm(u).replace(".md/", "/") for u in guides}

    # Each engine page
    pages = []
    for p in config.read_json(config.DATA / "pages.json", []):
        code, html, _ = _get(p["url"])
        md_code, md, _ = _get(f'{base}/{p["slug"]}.md')
        path = _norm(p["url"])
        pages.append({
            "slug": p["slug"], "url": p["url"], "published": p.get("published"),
            "live": "Yes" if code == 200 else f"No ({code})",
            "in_sitemap": "Yes" if path in smap_paths else "No",
            "in_llms": "Yes" if path in llms_slugs else "No",
            "markdown": "Yes" if md_code == 200 and md.startswith("# ") else "No",
            "schema": "Yes" if code == 200 and "application/ld+json" in html and '"FAQPage"' in html else "No",
            "meta_tags": len(re.findall(r'<meta name="description"', html)) if code == 200 else 0,
            "checked": now,
        })

    out = {"checked": now, "files": files, "pages": pages}
    config.write_json(config.DATA / "sitecheck.json", out)
    return out
