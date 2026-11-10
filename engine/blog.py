"""The /blog/ page: the parent of every blog post, and the index that lists them (newest first)."""
import html as _html
import json
from datetime import date

from . import config, page

_e = _html.escape

STYLE = """<style>
.cp-bloggrid{list-style:none;margin:0;padding:0;display:grid;gap:24px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}
.cp-bloggrid li{margin:0}
.cp-blogcard{display:flex;flex-direction:column;height:100%;border-radius:18px;overflow:hidden;text-decoration:none;
 background:var(--cp-card,#fff);border:1px solid var(--cp-line,rgba(15,23,42,.1));color:inherit;transition:transform .2s,box-shadow .2s}
.cp-blogcard,.cp-blogcard *{text-decoration:none!important}
.cp-blogmore{font-weight:600;margin-top:4px;color:var(--cp-accent,#b8860b)}
.cp-blogcard:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(15,23,42,.12)}
.cp-blogcard img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.cp-blogcard-body{padding:18px 20px 22px;display:flex;flex-direction:column;gap:8px}
.cp-blogcard strong{font-size:1.12rem;line-height:1.3}
.cp-blogcard .cp-guide-desc{opacity:.8;font-size:.95rem}
.cp-blogfeature{grid-column:1/-1}
@media(min-width:900px){.cp-blogfeature .cp-blogcard{flex-direction:row}.cp-blogfeature img{width:58%;aspect-ratio:auto}
 .cp-blogfeature .cp-blogcard-body{justify-content:center;padding:32px}.cp-blogfeature strong{font-size:1.6rem}}
</style>"""


def _slug(cfg):
    return cfg["publishing"].get("blog_page_slug", "blog")


def url(cfg):
    return f'{cfg["site"]["base_url"].rstrip("/")}/{_slug(cfg)}/'


def posts():
    """Published blog specs, newest first."""
    out = []
    for f in config.PUBLISHED.glob("*.json"):
        s = config.read_json(f, {})
        if page.is_blog(s):
            out.append(s)
    return sorted(out, key=lambda s: (s.get("published", ""), -s.get("slot", 0)), reverse=True)


def _meta(cfg, html, markdown, schema):
    return {
        "_chimera_engine": True,
        "_chimera_query": "geo blog",
        "_chimera_markdown": markdown,
        "_chimera_schema": schema,
        "_chimera_meta_description": DESC,
        "_chimera_eyebrow": "Blog",
        "_yoast_wpseo_title": TITLE,
        "_yoast_wpseo_metadesc": DESC,
        "rank_math_title": TITLE,
        "rank_math_description": DESC,
    }


TITLE = "AI Search Blog for Anaheim & Orange County Businesses"
DESC = ("Daily posts from Chimera AI in Anaheim, California on AI search, ChatGPT, Google AI Overviews and "
        "how Orange County businesses get recommended by AI.")


def ensure_page(wp, cfg):
    """Returns the /blog/ page ID, creating a placeholder the first time."""
    found = wp.find_page(_slug(cfg))
    if found:
        return found["id"]
    body = {"title": "Blog", "slug": _slug(cfg), "status": "publish",
            "content": '<div class="cp"><p>New posts are on the way.</p></div>', "excerpt": DESC}
    return wp._req("POST", "/pages", json=body)["id"]


def render(cfg):
    base = cfg["site"]["base_url"].rstrip("/")
    city, region = page.place(cfg)
    items = posts()
    cards = []
    for i, s in enumerate(items):
        img = (s.get("hero_image") or {}).get("url", "")
        when = date.fromisoformat(s["published"]).strftime("%B %-d, %Y") if s.get("published") else ""
        cards.append(
            f'<li class="{"cp-blogfeature" if i == 0 else ""}"><a class="cp-blogcard" href="{_e(page.page_url(s, cfg))}">'
            + (f'<img src="{_e(img)}" alt="{_e((s.get("hero_image") or {}).get("alt", s["h1"]))}" loading="{"eager" if i == 0 else "lazy"}" width="1200" height="675">' if img else "")
            + f'<span class="cp-blogcard-body"><span class="cp-eyebrow">{_e(when)} · {_e(s.get("category", "AI search"))}</span>'
            f'<strong>{_e(s["h1"])}</strong><span class="cp-guide-desc">{_e(s["seo"]["meta_description"])}</span>'
            f'<span class="cp-blogmore" aria-hidden="true">Read the post →</span></span></a></li>'
        )
    html = (
        STYLE + '<div class="cp">'
        f'<nav class="cp-crumbs" aria-label="Breadcrumb"><a href="{base}/">Home</a><span aria-hidden="true">/</span>'
        '<span aria-current="page">Blog</span></nav>'
        f'<section class="cp-hub-hero cp-hero"><p class="cp-eyebrow">Chimera AI Blog · {_e(city)} · {_e(region)} · {len(items)} posts</p>'
        '<h1>AI search news and playbooks for Anaheim and Orange County businesses</h1>'
        f'<p>New posts every day on how ChatGPT, Google AI Overviews, Gemini and Perplexity find, describe and recommend '
        f'businesses, written by the Chimera AI team in {_e(city)} for companies across {_e(region)}.</p>'
        f'<div class="cp-actions"><a class="cp-btn cp-btn--primary" href="{base}/#audit">Get your free AI visibility audit</a>'
        f'<a class="cp-btn cp-btn--ghost" href="{base}/{cfg["publishing"].get("hub_page_slug", "insights")}/">Browse the GEO guides</a></div></section>'
        f'<section class="cp-sec"><ul class="cp-bloggrid">{"".join(cards) or "<li>New posts are on the way.</li>"}</ul></section>'
        '</div>'
    )
    md = [f"# {TITLE}", "", DESC, ""]
    md += [f"- [{s['h1']}]({page.page_url(s, cfg)}) ({s.get('published', '')}): {s['seo']['meta_description']}" for s in items]
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": url(cfg) + "#blog", "url": url(cfg), "name": "Chimera AI Blog", "description": DESC,
         "inLanguage": "en-US",
         "publisher": {"@type": "Organization", "name": cfg["site"]["brand"], "url": base,
                       "address": {"@type": "PostalAddress", "addressLocality": "Anaheim", "addressRegion": "CA", "addressCountry": "US"},
                       "areaServed": [{"@type": "City", "name": city}, {"@type": "AdministrativeArea", "name": region}]},
         "blogPost": [{"@type": "BlogPosting", "headline": s["h1"], "url": page.page_url(s, cfg),
                       "datePublished": s.get("published")} for s in items[:50]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": url(cfg)}]},
    ]}
    return html, "\n".join(md) + "\n", json.dumps(schema, ensure_ascii=False)


def build_index(cfg, wp):
    """Rewrites the /blog/ page with every post. Returns its URL."""
    pid = ensure_page(wp, cfg)
    html, md, schema = render(cfg)
    wp._req("POST", f"/pages/{pid}", json={"title": "Blog", "content": html, "excerpt": DESC,
                                           "status": "publish", "meta": _meta(cfg, html, md, schema)})
    return url(cfg)
