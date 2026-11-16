"""Competitor topic gap from public XML sitemaps, using advertools (MIT, github.com/eliasdabbas/advertools).

Reads config/competitors.json: {"domains": ["example-agency.com", ...]}. For each domain it reads the sitemap listed in
robots.txt (or /sitemap.xml), turns page URLs into topics, keeps the ones with local buyer intent or a service we sell,
and lists the topics none of our pages cover. Writes data/competitor_gaps.json. Only public sitemaps are read; no pages
are crawled and no search results are scraped.
"""
import re
from collections import Counter

from . import config
from .opportunities import classify

STOP = {"www", "com", "html", "php", "blog", "page", "category", "tag", "author", "wp", "content", "uploads", "index"}


def topic(url):
    path = re.sub(r"https?://[^/]+", "", url).strip("/")
    last = [p for p in path.split("/") if p and not p.isdigit()]
    if not last:
        return ""
    words = [w for w in re.split(r"[-_]+", re.sub(r"\.\w+$", "", last[-1]).lower()) if w and w not in STOP]
    return " ".join(words)


def ours():
    words = set()
    for f in list(config.PUBLISHED.glob("*.json")):
        spec = config.read_json(f, {})
        words.add(" ".join(spec.get("slug", "").split("-")))
        words.add((spec.get("primary_keyword") or "").lower())
    return words


def covered(t, mine):
    tw = set(t.split())
    return any(len(tw & set(m.split())) >= max(2, int(len(tw) * 0.7)) for m in mine if m)


def run(cfg):
    import advertools as adv
    import requests

    domains = config.read_json(config.ROOT / "config" / "competitors.json", {}).get("domains", [])
    if not domains:
        return {"error": "Add competitor domains to config/competitors.json first."}
    mine = ours()
    result = {}
    for d in domains:
        try:
            robots = requests.get(f"https://{d}/robots.txt", timeout=15).text
            maps = re.findall(r"(?im)^sitemap:\s*(\S+)", robots) or [f"https://{d}/sitemap.xml"]
            urls = []
            for m in maps[:3]:
                df = adv.sitemap_to_df(m, max_workers=4)
                urls += df["loc"].dropna().tolist() if "loc" in df else []
        except Exception as e:  # one bad site should not stop the rest
            result[d] = {"error": str(e)[:200]}
            continue
        topics = Counter(t for t in (topic(u) for u in urls) if len(t.split()) >= 2)
        gaps = []
        for t, n in topics.items():
            intent = classify(t)
            if intent in ("money-local", "money-national", "question") and not covered(t, mine):
                gaps.append({"topic": t, "intent": intent})
        gaps.sort(key=lambda g: (g["intent"] != "money-local", g["topic"]))
        result[d] = {"urls": len(urls), "topics": len(topics), "gaps": gaps[:80]}
    config.write_json(config.ROOT / "data" / "competitor_gaps.json", result)
    return {d: {k: (len(v) if isinstance(v, list) else v) for k, v in r.items()} for d, r in result.items()}
