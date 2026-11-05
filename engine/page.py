"""Turns a page spec (JSON) into WordPress HTML, JSON-LD schema and a Markdown copy."""
import html
import json
import re
from datetime import date

REQUIRED = ["query", "slug", "primary_keyword", "h1", "answer", "seo", "sections", "faqs"]


def slugify(text):
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return re.sub(r"[\s-]+", "-", text).strip("-")[:80].rstrip("-")


def validate(spec):
    missing = [k for k in REQUIRED if not spec.get(k)]
    if missing:
        raise ValueError(f"Spec is missing: {', '.join(missing)}")
    for k in ("title", "meta_description"):
        if not spec["seo"].get(k):
            raise ValueError(f"Spec is missing seo.{k}")
    if spec["slug"] != slugify(spec["slug"]):
        raise ValueError(f"Slug '{spec['slug']}' is not clean; use '{slugify(spec['slug'])}'")


def _e(text):
    return html.escape(str(text), quote=True)


def _anchor(text):
    return slugify(text)[:60]


def _lead_block(cfg, variant, anchor):
    lead = cfg["lead"]
    btn = lead.get("fallback_button") or {"text": "Book your AI visibility audit", "url": cfg["site"]["base_url"] + "/"}
    points = "".join(f"<li>{_e(p)}</li>" for p in lead.get("points", []))
    return (
        f'<section class="cp-lead" id="{anchor}">'
        f'<div class="cp-lead-copy"><p class="cp-eyebrow">{_e(lead["offer"])}</p>'
        f'<h2>{_e(lead["cta_heading"])}</h2><p>{_e(lead["cta_text"])}</p>'
        f'<ul class="cp-lead-points">{points}</ul></div>'
        # The plugin swaps this block for the live form; the button is the fallback.
        f'<div class="chimera-lead" data-chimera-form="{variant}"><p>'
        f'<a class="cp-btn cp-btn--primary" href="{_e(btn["url"])}">{_e(btn["text"])}</a></p></div>'
        f'</section>'
    )


def _process_band(cfg):
    steps = cfg["site"].get("process") or []
    if not steps or not isinstance(steps[0], dict):
        return ""
    items = "".join(f"<li><strong>{_e(s['name'])}</strong><span>{_e(s['text'])}</span></li>" for s in steps)
    return (f'<section class="cp-process"><p class="cp-eyebrow">How {_e(cfg["site"]["brand"])} works</p>'
            f'<h2>A six-phase GEO build that compounds over time</h2><ol class="cp-steps">{items}</ol></section>')


def render_html(spec, cfg):
    """Page body for WordPress. No <script> or <style>: the plugin supplies the design and the form."""
    site = cfg["site"]
    parts = ['<div class="cp">']

    clients = site.get("proof_clients") or []
    trust = ""
    if clients:
        trust = ('<p class="cp-trust"><span>Brands working with ' + _e(site["brand"]) + ':</span> '
                 + " ".join(f"<b>{_e(c)}</b>" for c in clients) + "</p>")
    parts.append(
        '<section class="cp-hero">'
        f'<p class="cp-eyebrow">{_e(spec.get("eyebrow") or "GEO guide")}</p>'
        f'<p class="cp-answer"><strong>Short answer:</strong> {_e(spec["answer"])}</p>'
        '<div class="cp-actions"><a class="cp-btn cp-btn--primary" href="#get-started">Get your free AI visibility audit</a>'
        '<a class="cp-btn cp-btn--ghost" href="#faq">Read the FAQs</a></div>'
        f'{trust}</section>'
    )

    if spec.get("key_takeaways"):
        items = "".join(f'<li class="cp-card">{_e(t)}</li>' for t in spec["key_takeaways"])
        parts.append(f'<section class="cp-band cp-takeaways"><h2>Key takeaways</h2><ul class="cp-cards">{items}</ul></section>')

    toc = "".join(f'<li><a href="#{_anchor(s["heading"])}">{_e(s["heading"])}</a></li>' for s in spec["sections"])
    parts.append(f'<nav class="cp-toc" aria-label="Contents"><p class="cp-eyebrow">On this page</p><ol>{toc}'
                 f'<li><a href="#faq">Frequently asked questions</a></li></ol></nav>')

    n = len(spec["sections"])
    for i, s in enumerate(spec["sections"]):
        parts.append(f'<section class="cp-section" id="{_anchor(s["heading"])}"><h2>{_e(s["heading"])}</h2>{s["body_html"]}</section>')
        if i == 1:
            parts.append(_lead_block(cfg, "inline", "get-started"))
        if i == min(4, n - 2):
            parts.append(_process_band(cfg))

    faq = "".join(
        f'<details class="cp-faq"><summary><h3>{_e(f["q"])}</h3></summary><p>{_e(f["a"])}</p></details>'
        for f in spec["faqs"]
    )
    parts.append(f'<section class="cp-band" id="faq"><p class="cp-eyebrow">FAQ</p><h2>Frequently asked questions</h2>'
                 f'<div class="cp-faq-list">{faq}</div></section>')

    if spec.get("internal_links"):
        links = "".join(f'<li class="cp-card"><a href="{_e(l["url"])}">{_e(l["anchor"])}</a></li>'
                        for l in spec["internal_links"])
        parts.append(f'<section class="cp-related"><h2>Related guides</h2><ul class="cp-cards">{links}</ul></section>')

    parts.append(_lead_block(cfg, "full", "get-started-bottom"))

    if spec.get("sources"):
        src = "".join(
            f'<li><a href="{_e(s["url"])}" rel="nofollow noopener" target="_blank">{_e(s["title"])}</a></li>'
            for s in spec["sources"]
        )
        parts.append(f'<section class="cp-sources"><h2>Sources</h2><ul>{src}</ul></section>')

    updated = spec.get("updated") or date.today().isoformat()
    parts.append(f'<p class="cp-updated">Last updated: {_e(updated)}</p></div>')
    return "\n".join(parts)


def render_schema(spec, cfg):
    site = cfg["site"]
    url = f'{site["base_url"]}/{spec["slug"]}/'
    today = spec.get("updated") or date.today().isoformat()
    org = {"@type": "Organization", "name": site["brand"], "url": site["base_url"]}
    graph = [
        {
            "@type": "Article",
            "@id": f"{url}#article",
            "headline": spec["h1"][:110],
            "description": spec["seo"]["meta_description"],
            "mainEntityOfPage": url,
            "datePublished": spec.get("published", today),
            "dateModified": today,
            "author": org,
            "publisher": org,
            "inLanguage": site.get("language", "en"),
            "keywords": ", ".join([spec["primary_keyword"]] + spec.get("secondary_keywords", [])),
        },
        {
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
                for f in spec["faqs"]
            ],
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": site["base_url"] + "/"},
                {"@type": "ListItem", "position": 2, "name": spec["h1"], "item": url},
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def html_to_markdown(fragment):
    t = fragment
    t = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", t, flags=re.S)
    t = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n#### \1\n", t, flags=re.S)
    t = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", t, flags=re.S)
    t = re.sub(r"</t[hd]>\s*", " | ", t)
    t = re.sub(r"<tr[^>]*>", "\n| ", t)
    t = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r"[\2](\1)", t, flags=re.S)
    t = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", t, flags=re.S)
    t = re.sub(r"<(em|i)>(.*?)</\1>", r"*\2*", t, flags=re.S)
    t = re.sub(r"</p>|<br\s*/?>", "\n\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def render_markdown(spec, cfg):
    site = cfg["site"]
    url = f'{site["base_url"]}/{spec["slug"]}/'
    out = [f"# {spec['h1']}", "", f"> {spec['answer']}", "", f"Source: {url}", ""]
    if spec.get("key_takeaways"):
        out += ["## Key takeaways", ""] + [f"- {t}" for t in spec["key_takeaways"]] + [""]
    for s in spec["sections"]:
        out += [f"## {s['heading']}", "", html_to_markdown(s["body_html"]), ""]
    out += ["## Frequently asked questions", ""]
    for f in spec["faqs"]:
        out += [f"### {f['q']}", "", f["a"], ""]
    out += [f"---", f"{site['brand']} — {cfg['lead']['offer']}: {site['base_url']}/"]
    return "\n".join(out)


def plain_text(spec):
    body = " ".join(html_to_markdown(s["body_html"]) for s in spec["sections"])
    faqs = " ".join(f["q"] + " " + f["a"] for f in spec["faqs"])
    return f'{spec["h1"]} {spec["answer"]} {" ".join(spec.get("key_takeaways", []))} {body} {faqs}'
