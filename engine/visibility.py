"""AI visibility tracker (free tier).

Asks free OpenRouter models the questions Orange County buyers ask, and records which agencies each answer names.
Free models have no live web access, so this measures what the models already know (their training data). The live-web
side is checked in the daily run with web search and saved by `record_web()`.
Config: config/visibility.json. Output: data/ai_visibility/YYYY-MM-DD.json and data/ai_visibility/summary.json.
"""
import re
from datetime import date

from . import config, openrouter

SYSTEM = ("You are a helpful assistant. Answer the user's question directly with specific business names where you can. "
          "If you are not sure, say so instead of inventing names.")


def _names(cfg):
    v = config.read_json(config.ROOT / "config" / "visibility.json", {})
    comps = config.read_json(config.ROOT / "config" / "competitors.json", {}).get("domains", [])
    brands = {"Chimera": [r"\bchimera\b", r"thechimeraai"]}
    for name, pats in v.get("extra_brands", {}).items():
        brands[name] = pats
    for d in comps:
        base = d.split(".")[0]
        if not any(re.search(p, d) or re.search(p, base) for ps in brands.values() for p in ps):
            brands[base] = [rf"\b{re.escape(base)}\b", re.escape(d)]
    return v, brands


def mentions(text, brands):
    t = text.lower()
    return [b for b, pats in brands.items() if any(re.search(p, t) for p in pats)]


GENERIC = {"specialization signals", "focus", "why", "note", "pros", "cons", "best for", "what to look for", "location",
           "services", "top-tier", "how to choose", "summary", "pricing", "red flags", "next steps", "website"}


def named_entities(text):
    """Every bolded or numbered name in an answer, e.g. '**PaperStreet**' or '1. Thrive Internet Marketing'."""
    found = re.findall(r"\*\*([^*\n]{3,60})\*\*", text) + re.findall(r"(?m)^\s*\d+\.\s+([A-Z][^\n:(*]{2,50})", text)
    out = []
    for f in found:
        f = re.sub(r"^\d+\.\s*", "", re.sub(r"\s*\(.*$", "", f)).strip(" :-")
        if f and f.lower() not in GENERIC and not f.lower().startswith(("focus", "why", "best", "what", "how")) and len(f.split()) <= 6:
            out.append(f)
    return list(dict.fromkeys(out))


def run(cfg, budget=24, models=None):
    v, brands = _names(cfg)
    prompts, models = v.get("prompts", []), models or v.get("models", [])
    left = openrouter.remaining()
    budget = min(budget, max(left - 10, 0))  # keep 10 free requests for the link prospector
    rows, used = [], 0
    for p in prompts:
        for m in models:
            if used >= budget:
                break
            try:
                ans = openrouter.chat(m, p, system=SYSTEM)
            except Exception as e:
                rows.append({"prompt": p, "model": m, "error": str(e)[:160]})
                used += 1
                continue
            used += 1
            rows.append({"prompt": p, "model": m, "named": mentions(ans, brands), "entities": named_entities(ans), "answer": ans[:8000]})
    ok = [r for r in rows if "named" in r]
    share = {b: sum(b in r["named"] for r in ok) for b in brands}
    from collections import Counter
    top = Counter(e for r in ok for e in r.get("entities", []))
    out = {"top_entities": top.most_common(40), "date": date.today().isoformat(), "kind": "model memory (free models, no live web)", "answers": len(ok),
           "errors": len(rows) - len(ok), "share_of_answers": share, "rows": rows}
    d = config.ROOT / "data" / "ai_visibility"
    d.mkdir(exist_ok=True)
    config.write_json(d / f"{out['date']}.json", out)
    summ = config.read_json(d / "summary.json", {"days": []})
    summ["days"] = [x for x in summ["days"] if x["date"] != out["date"]] + [
        {"date": out["date"], "answers": len(ok), "chimera": share.get("Chimera", 0), "share": share}]
    config.write_json(d / "summary.json", summ)
    return {"top_named": top.most_common(15), "answers": len(ok), "errors": out["errors"], "chimera_named": share.get("Chimera", 0), "share": share,
            "free_requests_left": openrouter.remaining()}


def record_web(results):
    """Save live-web results gathered in the daily run: [{'query':..., 'top':[domains...]}]."""
    d = config.ROOT / "data" / "ai_visibility"
    d.mkdir(exist_ok=True)
    config.write_json(d / f"web-{date.today().isoformat()}.json", results)
