"""Opportunity finder: turns real Search Console query data into the day's highest-value work.

Methods adapted from MIT-licensed open-source work, rewritten for this engine:
  - striking distance / content opportunities and cannibalization checks: github.com/AminForou/mcp-gsc (skills/)
  - local intent categories (core service, geo-modified, near-me, qualifier, question): github.com/garrettjsmith/localseoskills
Writes data/opportunities.json and returns a summary.
"""
import re
from collections import defaultdict
from datetime import date, timedelta

from . import config, google_api, sitekit

CITIES = ["anaheim", "orange county", "oc", "irvine", "santa ana", "huntington beach", "newport beach", "fullerton",
          "costa mesa", "garden grove", "orange", "tustin", "yorba linda", "mission viejo", "lake forest", "buena park",
          "laguna", "brea", "placentia", "cypress", "westminster", "fountain valley", "seal beach", "san clemente",
          "dana point", "aliso viejo", "rancho santa margarita", "la habra", "los alamitos", "stanton", "villa park"]
SERVICE = r"\b(seo|geo|aeo|search engine optimi[sz]ation|local seo|ai search|llm seo|generative engine|marketing|google business profile|gbp|website|web design)\b"
BUYER = r"\b(agency|agencies|company|companies|consultant|consulting|services?|expert|firm|specialist|hire|cost|price|pricing|best|top|near me|audit)\b"
QUESTION = r"^(how|what|why|when|which|who|can|does|do|is|are|should)\b"
NON_EN = re.compile(r"[^\x00-\x7f]|\b(tracciare|traffico|como|para|wie|pour|seo para|posicionamiento)\b")


def classify(q):
    ql = q.lower()
    local = any(re.search(rf"\b{re.escape(c)}\b", ql) for c in CITIES) or "near me" in ql
    service = bool(re.search(SERVICE, ql))
    buyer = bool(re.search(BUYER, ql))
    if NON_EN.search(ql):
        return "non-us"
    if service and local:
        return "money-local"          # e.g. "anaheim seo", "seo company orange county"
    if service and buyer:
        return "money-national"       # e.g. "geo agency", "carpet cleaning seo services"
    if re.search(QUESTION, ql):
        return "question"
    if service:
        return "service-research"     # e.g. "carpet cleaning seo": other agencies' turf, low conversion odds
    return "other"


VALUE = {"money-local": 10, "money-national": 3, "question": 2, "service-research": 1, "other": 1, "non-us": 0}


def ctr_gap(pos, ctr):
    # Rough expected CTR by position for a young local site; used only to rank work.
    exp = 0.25 if pos <= 1.5 else 0.12 if pos <= 3 else 0.06 if pos <= 5 else 0.03 if pos <= 10 else 0.01 if pos <= 20 else 0.002
    return max(exp - ctr, 0)


def run(cfg):
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=27)
    import os
    if os.environ.get("GSC_SERVICE_ACCOUNT_KEY_JSON"):
        prop = google_api.gsc_property(cfg["site"]["domain"])
        rows = google_api.gsc_query(prop, start.isoformat(), end.isoformat(), ["query", "page"])
    else:
        rows = sitekit.gsc_query(start.isoformat(), end.isoformat(), ["query", "page"])
    base = cfg["site"]["base_url"].rstrip("/")
    for r in rows:
        r["slug"] = r["page"].replace(base, "").strip("/").split("/")[-1] or "home"
        r["intent"] = classify(r["query"])
        r["ctr"] = r.get("ctr", (r.get("clicks", 0) / r["impressions"]) if r.get("impressions") else 0)

    # 1. Money queries: local buyer intent, ranked by how close they are to page 1.
    money = sorted([r for r in rows if r["intent"] == "money-local"], key=lambda r: (r["position"], -r["impressions"]))

    # 2. Striking distance: positions 4-30 (wider than the usual 11-20 while the site is young), weighted by intent.
    striking = [r for r in rows if 4 <= r["position"] <= 30 and r["intent"] != "non-us"]
    for r in striking:
        r["score"] = round(r["impressions"] * VALUE[r["intent"]] / r["position"], 2)
    striking.sort(key=lambda r: -r["score"])

    # 3. CTR fixes: pages on page 1-2 earning fewer clicks than their position should.
    ctr = [dict(r, gap=round(ctr_gap(r["position"], r["ctr"]) * r["impressions"], 2)) for r in rows if r["position"] <= 20]
    ctr = sorted([r for r in ctr if r["gap"] > 0], key=lambda r: -r["gap"])

    # 4. Cannibalization: one query, several of our pages.
    byq = defaultdict(list)
    for r in rows:
        byq[r["query"]].append(r)
    cannibal = []
    for q, rs in byq.items():
        if len({r["slug"] for r in rs}) > 1:
            rs = sorted(rs, key=lambda r: r["position"])
            cannibal.append({"query": q, "intent": rs[0]["intent"], "impressions": sum(r["impressions"] for r in rs),
                             "keep": rs[0]["slug"], "pages": [(r["slug"], round(r["position"], 1), r["impressions"]) for r in rs]})
    cannibal.sort(key=lambda c: -c["impressions"] * VALUE[c["intent"]])

    # 5. Intent mix: where impressions come from today.
    mix = defaultdict(lambda: {"queries": 0, "impressions": 0, "clicks": 0})
    for r in rows:
        m = mix[r["intent"]]
        m["queries"] += 1
        m["impressions"] += r["impressions"]
        m["clicks"] += r.get("clicks", 0)

    keep = ("query", "slug", "intent", "impressions", "clicks", "position", "ctr")
    slim = lambda rs, extra=(): [{k: (round(r[k], 3) if isinstance(r.get(k), float) else r.get(k)) for k in keep + extra} for r in rs]
    out = {"date": date.today().isoformat(), "window": [start.isoformat(), end.isoformat()], "rows": len(rows),
           "intent_mix": dict(mix), "money_queries": slim(money[:40]), "striking_distance": slim(striking[:40], ("score",)),
           "ctr_fixes": slim(ctr[:30], ("gap",)), "cannibalization": cannibal[:30]}
    config.write_json(config.ROOT / "data" / "opportunities.json", out)
    return {"rows": len(rows), "intent_mix": dict(mix), "money_queries": len(money), "striking": len(striking),
            "ctr_fixes": len(ctr), "cannibalization": len(cannibal), "file": "data/opportunities.json"}
