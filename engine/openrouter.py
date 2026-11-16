"""Minimal OpenRouter client for the engine's workers. Free models only (IDs ending in ':free').

The API key is a network secret: the session's proxy injects it into requests to openrouter.ai, so the code sends a
placeholder. Free accounts get a small daily request allowance (50/day at the time of writing); `remaining()` reads it.
"""
import time

import requests

API = "https://openrouter.ai/api/v1"
HEAD = {"Authorization": "Bearer proxy-injected", "HTTP-Referer": "https://thechimeraai.com", "X-Title": "Chimera engine"}


def remaining():
    d = requests.get(f"{API}/key", headers=HEAD, timeout=30).json().get("data", {})
    return (d.get("free_model_daily_requests") or {}).get("remaining", 0)


def chat(model, prompt, system=None, max_tokens=900, retries=2):
    if not model.endswith(":free"):
        raise ValueError("Only free models are allowed: " + model)
    msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
    for i in range(retries + 1):
        r = requests.post(f"{API}/chat/completions", headers=HEAD, timeout=120,
                          json={"model": model, "messages": msgs, "max_tokens": max_tokens, "temperature": 0.2})
        if r.status_code == 429 and i < retries:
            time.sleep(15 * (i + 1))
            continue
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"] or ""
    return ""
