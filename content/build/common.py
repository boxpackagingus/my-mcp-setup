"""Shared helpers for writing page specs."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch1 import CORE, SRC, L  # noqa: E402,F401
import visuals_lib as V  # noqa: E402,F401

DRAFTS = Path(__file__).resolve().parents[1] / "drafts"

SRC.update({
    "anthropic": {"title": "Anthropic: Does Anthropic crawl data from the web, and how can site owners block the crawler?",
                  "url": "https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler"},
    "bing": {"title": "Bing Webmaster Tools", "url": "https://www.bing.com/webmasters"},
    "faq": {"title": "Google Search Central: FAQ (FAQPage) structured data", "url": "https://developers.google.com/search/docs/appearance/structured-data/faqpage"},
    "faqchange": {"title": "Google Search Central blog: Changes to HowTo and FAQ rich results (Aug 2023)", "url": "https://developers.google.com/search/blog/2023/08/howto-faq-changes"},
    "org": {"title": "Schema.org: Organization", "url": "https://schema.org/Organization"},
    "local": {"title": "Schema.org: LocalBusiness", "url": "https://schema.org/LocalBusiness"},
    "gbp": {"title": "Google Business Profile", "url": "https://www.google.com/business/"},
    "ga": {"title": "Google Analytics Help Center", "url": "https://support.google.com/analytics"},
    "chatgpt": V.SRC_CHATGPT, "gemini": V.SRC_GEMINI, "pplx_q": V.SRC_PPLX, "aio": V.SRC_AIO,
})


def page(slug, query, kw, eyebrow, title, meta, h1, answer, takeaways, sections, faqs, links, sources,
         visuals, secondary=(), intent="informational", hero_query=None, hero_engines=None, short_title=None):
    return {
        "query": query, "slug": slug, "eyebrow": eyebrow, "primary_keyword": kw,
        "secondary_keywords": list(secondary), "search_intent": intent,
        "seo": {"title": title, "meta_description": meta}, "h1": h1, "answer": answer,
        "key_takeaways": takeaways,
        "sections": [{"heading": h, "body_html": b} for h, b in sections],
        "faqs": [{"q": q, "a": a} for q, a in faqs],
        "internal_links": links, "sources": [SRC[s] for s in sources], "visuals": visuals,
        "hero_query": hero_query, "short_title": short_title or title,
        "hero_engines": hero_engines or ["chatgpt", "perplexity", "gemini", "claude", "google", "copilot"],
    }


def save_all(pages):
    DRAFTS.mkdir(parents=True, exist_ok=True)
    for p in pages:
        n = len(p["sections"])
        for v in p["visuals"]:
            assert 0 <= v["after"] < n, (p["slug"], v["after"], n)
        f = DRAFTS / f"{p['slug']}.json"
        if f.exists():  # keep images already uploaded for this draft
            old = json.loads(f.read_text())
            for k in ("hero_image", "photo"):
                if old.get(k) and not p.get(k):
                    p[k] = old[k]
        f.write_text(json.dumps(p, indent=2, ensure_ascii=False) + "\n")
        print("wrote", p["slug"])
