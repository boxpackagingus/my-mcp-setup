"""Local link prospector (free tier).

Input: data/link_prospects_raw.json, a list of candidates found with web search during the daily run:
  {"name", "url", "type", "evidence", "cost", "found": "YYYY-MM-DD", "query"}
The worker merges them into data/link_prospects.json, keeps each prospect's status (new / contacted / listed / skip) so
nothing is pitched twice, checks whether each URL answers (where this environment's network allows), and asks one free
OpenRouter model to write a one-line next step and a priority for the new ones in a single request.
Facts come only from the search results recorded in "evidence"; the model never adds facts.
"""
import json
import re
from datetime import date

import requests

from . import config, openrouter

MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"
TYPES = {"chamber": 5, "podcast": 4, "news": 4, "directory": 3, "association": 4, "event": 3, "listicle": 2, "other": 1}


def _reach(url):
    try:
        r = requests.head(url, timeout=15, allow_redirects=True)
        return r.status_code
    except requests.exceptions.ProxyError:
        return "blocked by network allowlist"
    except Exception as e:
        return str(e)[:60]


def run(cfg):
    raw = config.read_json(config.ROOT / "data" / "link_prospects_raw.json", [])
    path = config.ROOT / "data" / "link_prospects.json"
    have = {p["url"]: p for p in config.read_json(path, [])}
    new = []
    for c in raw:
        url = c["url"].rstrip("/") + "/"
        if url in have:
            continue
        p = dict(c, url=url, status="new", http=_reach(url), priority=TYPES.get(c.get("type"), 1), next_step="")
        have[url] = p
        new.append(p)
    if new and openrouter.remaining() > 0:
        brief = [{"i": i, "name": p["name"], "type": p.get("type"), "cost": p.get("cost"), "evidence": p.get("evidence")} for i, p in enumerate(new)]
        prompt = ("You help an Anaheim, California SEO/GEO agency (Chimera) earn local links and mentions. For each item, using ONLY the "
                  "evidence given, write a one-sentence next step and a priority 1-5 (5 = best: local, relevant, free or low cost, "
                  "likely to give a link or mention). Reply with JSON only: [{\"i\":0,\"priority\":4,\"next_step\":\"...\"}].\n"
                  + json.dumps(brief))
        try:
            txt = openrouter.chat(MODEL, prompt, max_tokens=2500)
            m = re.search(r"\[.*\]", txt, re.S)
            for row in json.loads(m.group(0)) if m else []:
                p = new[int(row["i"])]
                p["priority"] = max(1, min(5, int(row.get("priority", p["priority"]))))
                p["next_step"] = str(row.get("next_step", ""))[:240]
        except Exception as e:
            for p in new:
                p["next_step"] = p["next_step"] or f"(model unavailable: {str(e)[:60]})"
    out = sorted(have.values(), key=lambda p: (p["status"] != "new", -p["priority"], p["name"]))
    config.write_json(path, out)
    return {"new": len(new), "total": len(out), "open": sum(p["status"] == "new" for p in out),
            "top": [(p["priority"], p["name"], p["next_step"][:90]) for p in out[:8]],
            "free_requests_left": openrouter.remaining(), "date": date.today().isoformat()}
