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


def render_html(spec, cfg):
    """Page body for WordPress. No <script>: schema is output by the plugin from post meta."""
    lead = cfg["lead"]
    parts = []
    parts.append(f'<div class="chimera-answer"><p><strong>Short answer:</strong> {_e(spec["answer"])}</p></div>')

    if spec.get("key_takeaways"):
        items = "".join(f"<li>{_e(t)}</li>" for t in spec["key_takeaways"])
        parts.append(f'<div class="chimera-takeaways"><h2>Key takeaways</h2><ul>{items}</ul></div>')

    toc = "".join(
        f'<li><a href="#{_anchor(s["heading"])}">{_e(s["heading"])}</a></li>' for s in spec["sections"]
    )
    parts.append(f'<nav class="chimera-toc" aria-label="Contents"><h2>On this page</h2><ol>{toc}'
                 f'<li><a href="#faq">FAQs</a></li></ol></nav>')

    cta = (
        f'<div class="chimera-cta" id="get-started"><h2>{_e(lead["cta_heading"])}</h2>'
        f'<p>{_e(lead["cta_text"])}</p>{lead.get("form_shortcode", "")}</div>'
    )

    for i, s in enumerate(spec["sections"]):
        parts.append(f'<h2 id="{_anchor(s["heading"])}">{_e(s["heading"])}</h2>{s["body_html"]}')
        if i == 1:  # first CTA after two sections, while interest is high
            parts.append(cta)

    faq = "".join(
        f'<details class="chimera-faq"><summary><h3>{_e(f["q"])}</h3></summary><p>{_e(f["a"])}</p></details>'
        for f in spec["faqs"]
    )
    parts.append(f'<h2 id="faq">Frequently asked questions</h2>{faq}')

    if spec.get("internal_links"):
        links = "".join(f'<li><a href="{_e(l["url"])}">{_e(l["anchor"])}</a></li>' for l in spec["internal_links"])
        parts.append(f'<div class="chimera-related"><h2>Related guides</h2><ul>{links}</ul></div>')

    parts.append(cta.replace('id="get-started"', 'id="get-started-bottom"'))

    if spec.get("sources"):
        src = "".join(
            f'<li><a href="{_e(s["url"])}" rel="nofollow noopener" target="_blank">{_e(s["title"])}</a></li>'
            for s in spec["sources"]
        )
        parts.append(f'<div class="chimera-sources"><h2>Sources</h2><ul>{src}</ul></div>')

    updated = spec.get("updated") or date.today().isoformat()
    parts.append(f'<p class="chimera-updated">Last updated: {_e(updated)}</p>')
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
