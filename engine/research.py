"""Finds the best queries to write pages for today.

Sources, combined and scored:
  1. Search Console: queries you already get impressions for but rank poorly on.
  2. Google Autocomplete: real questions people type, built from your seed topics.
  3. DataForSEO (optional): search volume and difficulty for every candidate.
"""
import os
from datetime import date, timedelta

import requests

from . import config, page

QUEUE = config.DATA / "queue.json"
PAGES = config.DATA / "pages.json"


def published_slugs():
    pages = config.read_json(PAGES, [])
    drafts = [p.stem for p in config.DRAFTS.glob("*.json")]
    return {p["slug"] for p in pages} | set(drafts)


def from_search_console(cfg):
    from . import google_api

    prop = google_api.gsc_property(cfg["site"]["domain"])
    end = date.today() - timedelta(days=3)
    start = end - timedelta(days=28)
    rows = google_api.gsc_query(prop, start.isoformat(), end.isoformat(), ["query", "page"])
    best = {}
    for r in rows:
        q = r["query"].strip().lower()
        if r["impressions"] < cfg["research"]["min_gsc_impressions"] or len(q.split()) < 3:
            continue
        cur = best.get(q)
        if cur is None or r["impressions"] > cur["impressions"]:
            best[q] = r
    out = []
    for q, r in best.items():
        if r["position"] <= 5:  # already doing well
            continue
        out.append({"query": q, "source": "search_console", "impressions": r["impressions"],
                    "position": round(r["position"], 1), "current_page": r["page"]})
    return out


def from_autocomplete(cfg):
    seen, out = set(), []
    lang = cfg["site"].get("language", "en")
    country = (cfg["site"].get("target_countries") or ["US"])[0].lower()
    for topic in cfg["research"]["seed_topics"]:
        for prefix in [""] + cfg["research"]["question_prefixes"]:
            q = f"{prefix} {topic}".strip()
            try:
                r = requests.get(
                    "https://suggestqueries.google.com/complete/search",
                    params={"client": "firefox", "q": q, "hl": lang, "gl": country},
                    timeout=15,
                )
                suggestions = r.json()[1] if r.ok else []
            except (requests.RequestException, ValueError, IndexError):
                suggestions = []
            for s in suggestions:
                s = s.strip().lower()
                if s not in seen and len(s.split()) >= 3:
                    seen.add(s)
                    out.append({"query": s, "source": "autocomplete", "seed": topic})
    return out


def add_volumes(cfg, candidates):
    """Adds search volume and difficulty from DataForSEO when its login is set."""
    login, pw = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not (login and pw) or not candidates:
        return candidates
    by_q = {c["query"]: c for c in candidates}
    queries = list(by_q)[:700]
    r = requests.post(
        "https://api.dataforseo.com/v3/dataforseo_labs/google/bulk_keyword_difficulty/live",
        auth=(login, pw),
        json=[{"keywords": queries, "language_code": cfg["site"].get("language", "en"),
               "location_code": 2840}],
        timeout=120,
    )
    if r.ok:
        for item in (r.json().get("tasks") or [{}])[0].get("result") or []:
            for k in item.get("items") or []:
                if k["keyword"] in by_q:
                    by_q[k["keyword"]]["difficulty"] = k.get("keyword_difficulty")
    r = requests.post(
        "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
        auth=(login, pw),
        json=[{"keywords": queries, "language_code": cfg["site"].get("language", "en"),
               "location_code": 2840}],
        timeout=120,
    )
    if r.ok:
        for k in (r.json().get("tasks") or [{}])[0].get("result") or []:
            if k.get("keyword") in by_q:
                by_q[k["keyword"]]["volume"] = k.get("search_volume") or 0
    return candidates


INTENT_WORDS = {"cost": 1.6, "price": 1.6, "agency": 1.8, "service": 1.6, "hire": 1.8, "best": 1.4,
                "vs": 1.3, "tool": 1.3, "how": 1.1, "does": 1.1, "is": 1.0, "what": 0.9}


STOP = {"a", "an", "the", "to", "of", "for", "in", "on", "and", "or", "is", "are", "do", "does", "my", "your"}


def same_question(a, b):
    wa = set(a.lower().split()) - STOP
    wb = set(b.lower().split()) - STOP
    if not wa or not wb:
        return False
    return len(wa & wb) / len(wa | wb) >= 0.8


def relevant(query, cfg):
    """Keeps queries about AI search / SEO; drops 'geothermal', 'george' and similar noise."""
    r = cfg["research"]
    q = f" {query.lower()} "
    tokens = set(query.lower().replace("?", "").split())
    if any(f" {x} " in q or (" " not in x and x in tokens) for x in r.get("exclude_terms", [])):
        return False
    terms = r.get("relevant_terms", [])
    return any((" " in t and t in q) or t in tokens for t in terms)


def score(c, cfg=None):
    words = c["query"].split()
    intent = max([INTENT_WORDS.get(w, 1.0) for w in words] or [1.0])
    demand = c.get("volume") or c.get("impressions") or 10
    difficulty = c.get("difficulty") or 30
    bonus = 1.5 if c["source"] == "search_console" else 1.0  # Google already links you to it
    q = f' {c["query"]} '
    if cfg and any(f" {t} " in q for t in cfg["research"].get("local_terms", [])):
        bonus *= 1.5  # your own market
    return round(demand * intent * bonus / (1 + difficulty / 25), 2)


def run(cfg, use_gsc=True):
    candidates = []
    if use_gsc:
        try:
            candidates += from_search_console(cfg)
        except SystemExit as e:
            print(f"Search Console skipped: {e}")
    candidates += from_autocomplete(cfg)
    candidates = add_volumes(cfg, candidates)

    taken = published_slugs()
    existing_queries = [p["query"] for p in config.read_json(PAGES, [])]
    queue, kept = [], []
    for c in candidates:
        c["slug"] = page.slugify(c["query"])
        if not relevant(c["query"], cfg) or c["slug"] in taken:
            continue
        if c.get("volume") is not None and c["volume"] < cfg["research"]["min_volume"]:
            continue
        if any(same_question(c["query"], q) for q in existing_queries + kept):
            continue  # same question as a page we already have
        c["score"] = score(c, cfg)
        queue.append(c)
        kept.append(c["query"])
    queue.sort(key=lambda c: c["score"], reverse=True)
    config.write_json(QUEUE, {"generated": date.today().isoformat(), "candidates": queue[:200]})
    return queue
