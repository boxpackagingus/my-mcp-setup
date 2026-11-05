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


EXPLORE = [
    ("What we do", "Six GEO services, from the AI visibility audit to citation tracking.", "/#services"),
    ("How it works", "The six-phase build: diagnose, fix, structure, content, authority, AI signal.", "/#process"),
    ("Results", "Brands that AI engines now cite and recommend.", "/#results"),
    ("GEO questions", "Straight answers to what clients ask us most.", "/#faq"),
]


def _tone(i):
    """Background rhythm for content sections: light and paper, with a dark band now and then."""
    if i == 3 or (i >= 6 and i % 3 == 0):
        return "dark"
    return "paper" if i % 2 else "light"


def render_html(spec, cfg):
    """Page body for WordPress. No <script> or <style>: the plugin supplies the design and the form."""
    from . import design, visuals

    site = cfg["site"]
    base = site["base_url"].rstrip("/")
    hub = cfg["publishing"].get("hub_page_slug", "insights")
    parts = ['<div class="cp">']

    # Breadcrumb: links every page back to the homepage and the guides hub.
    parts.append(
        f'<nav class="cp-crumbs" aria-label="Breadcrumb"><a href="{base}/">Home</a><span aria-hidden="true">/</span>'
        f'<a href="{base}/{hub}/">GEO Insights</a><span aria-hidden="true">/</span>'
        f'<span aria-current="page">{_e(spec.get("eyebrow") or spec["h1"])}</span></nav>'
    )

    clients = site.get("proof_clients") or []
    trust = ""
    if clients:
        trust = ('<div class="cp-trust"><span>Brands working with ' + _e(site["brand"]) + '</span>'
                 + "".join(f"<b>{_e(c)}</b>" for c in clients) + "</div>")
    words = len(plain_text(spec).split())
    minutes = max(3, round(words / 230))
    updated_iso = spec.get("updated") or date.today().isoformat()
    d = date.fromisoformat(updated_iso[:10])
    updated = f"{d.strftime('%b')} {d.day}, {d.year}"
    parts.append(
        '<section class="cp-hero"><div class="cp-hero-grid"><div>'
        f'<p class="cp-eyebrow">{_e(spec.get("eyebrow") or "GEO guide")}</p>'
        f'<p class="cp-answer"><strong>Short answer:</strong> {_e(spec["answer"])}</p>'
        '<div class="cp-actions"><a class="cp-btn cp-btn--primary" href="#get-started">Get your free AI visibility audit</a>'
        '<a class="cp-btn cp-btn--ghost" href="#faq">Read the FAQs</a></div></div>'
        '<dl class="cp-glance">'
        f'<div><dt>Reading time</dt><dd>{minutes} min</dd></div>'
        f'<div><dt>Sections</dt><dd>{len(spec["sections"])}</dd></div>'
        f'<div><dt>FAQs answered</dt><dd>{len(spec["faqs"])}</dd></div>'
        f'<div><dt>Updated</dt><dd>{_e(updated)}</dd></div>'
        f'</dl></div>{trust}</section>'
    )
    hero = spec.get("hero_image")
    if hero:
        parts.append(
            f'<figure class="cp-hero-art"><img src="{_e(hero["url"])}" alt="{_e(hero["alt"])}" '
            f'width="{int(hero.get("width", 1600))}" height="{int(hero.get("height", 840))}" loading="eager" decoding="async"></figure>'
        )

    if spec.get("key_takeaways"):
        items = "".join(f'<li class="cp-take"><span class="cp-take-n">{i + 1:02d}</span><p>{_e(t)}</p></li>'
                        for i, t in enumerate(spec["key_takeaways"]))
        parts.append(
            '<section class="cp-sec cp-tone--paper cp-takeaways"><div class="cp-sec-head"><div>'
            '<p class="cp-eyebrow">Summary</p><h2>Key takeaways</h2></div>'
            '<p class="cp-sec-lead">The five things to know before you read the rest.</p></div>'
            f'<ol class="cp-takegrid">{items}</ol></section>'
        )

    toc = "".join(f'<li><a href="#{_anchor(s["heading"])}">{_e(s["heading"])}</a></li>' for s in spec["sections"])
    parts.append(f'<nav class="cp-toc" aria-label="Contents"><p class="cp-eyebrow">On this page</p><ol>{toc}'
                 f'<li><a href="#faq">Frequently asked questions</a></li></ol></nav>')

    n = len(spec["sections"])
    for i, s in enumerate(spec["sections"]):
        parts.append(design.section(_e(s["heading"]), _anchor(s["heading"]), s["body_html"], _tone(i), s.get("label")))
        photo = spec.get("photo")
        if photo and i == 0:
            parts.append(
                f'<figure class="cp-photo"><img src="{_e(photo["url"])}" alt="{_e(photo["alt"])}" '
                f'width="{int(photo.get("width", 1360))}" height="{int(photo.get("height", 768))}" loading="lazy" decoding="async">'
                f'<figcaption>{_e(photo.get("caption", ""))}</figcaption></figure>'
            )
        prev = _tone(i)
        for v in [v for v in spec.get("visuals", []) if v.get("after") == i]:
            nxt = _tone(i + 1) if i + 1 < n else "paper"
            tone = next((c for c in ("paper", "light") if c not in (prev, nxt)), "light" if prev != "light" else "paper")
            parts.append(visuals.render(v, tone))
            prev = tone
        if i == 1:
            parts.append(_lead_block(cfg, "inline", "get-started"))
        if i == min(4, n - 2):
            parts.append(_process_band(cfg))

    faq = "".join(
        f'<details class="cp-faq"{" open" if k == 0 else ""}><summary><h3>{_e(f["q"])}</h3></summary><p>{_e(f["a"])}</p></details>'
        for k, f in enumerate(spec["faqs"])
    )
    parts.append(
        '<section class="cp-sec cp-tone--paper cp-faqsec" id="faq"><div class="cp-faq-side">'
        '<p class="cp-eyebrow">FAQ</p><h2>Frequently asked questions</h2>'
        '<p class="cp-sec-lead">Quick answers to what people ask next. Still unsure? Our team will look at your brand for free.</p>'
        f'<a class="cp-btn cp-btn--dark" href="#get-started-bottom">Ask about your brand</a></div>'
        f'<div class="cp-faq-list">{faq}</div></section>'
    )

    if spec.get("internal_links"):
        cards = []
        for l in spec["internal_links"]:
            home = "#" in l["url"] or l["url"].rstrip("/") == base
            tag = site["brand"] if home else "Guide"
            cards.append(f'<li><a class="cp-link-card" href="{_e(l["url"])}"><span class="cp-eyebrow">{_e(tag)}</span>'
                         f'<strong>{_e(l["anchor"][:1].upper() + l["anchor"][1:])}</strong><span class="cp-arrow" aria-hidden="true">→</span></a></li>')
        parts.append('<section class="cp-sec cp-tone--light cp-related"><div class="cp-sec-head"><div>'
                     '<p class="cp-eyebrow">Keep reading</p><h2>Related guides</h2></div></div>'
                     f'<ul class="cp-linkgrid">{"".join(cards)}</ul></section>')

    # Explore band: links to the main website's homepage sections.
    explore = "".join(
        f'<li><a class="cp-explore-card" href="{base}{url}"><strong>{_e(title)}</strong><span>{_e(text)}</span>'
        f'<span class="cp-arrow" aria-hidden="true">→</span></a></li>' for title, text, url in EXPLORE)
    parts.append(
        f'<section class="cp-explore"><div class="cp-sec-head"><div><p class="cp-eyebrow">{_e(site["brand"])} · {_e(site.get("location", ""))}</p>'
        f'<h2>Get recommended by AI, not just ranked</h2></div>'
        f'<p class="cp-sec-lead">{_e(site["one_liner"])} <a href="{base}/">Visit the {_e(site["brand"])} homepage</a>.</p></div>'
        f'<ul class="cp-exploregrid">{explore}</ul></section>'
    )

    parts.append(_lead_block(cfg, "full", "get-started-bottom"))

    if spec.get("sources"):
        src = "".join(
            f'<li><a href="{_e(s["url"])}" rel="nofollow noopener" target="_blank">{_e(s["title"])}</a></li>'
            for s in spec["sources"]
        )
        parts.append(f'<section class="cp-sources"><p class="cp-eyebrow">Sources</p><ul>{src}</ul>'
                     f'<p class="cp-updated">Last updated: {_e(updated)}</p></section>')
    else:
        parts.append(f'<p class="cp-updated">Last updated: {_e(updated)}</p>')
    parts.append("</div>")
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
                {"@type": "ListItem", "position": 2, "name": "GEO Insights",
                 "item": f'{site["base_url"]}/{cfg["publishing"].get("hub_page_slug", "insights")}/'},
                {"@type": "ListItem", "position": 3, "name": spec["h1"], "item": url},
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
    for v in spec.get("visuals", []):
        out += [f"## {v['title']}", ""]
        for key in ("items", "steps", "rows"):
            for it in v.get(key, []):
                label = it.get("title") or it.get("label") or it.get("engine", "")
                text = it.get("note") or it.get("text") or it.get("value") or ""
                if it.get("display") or ("value" in it and key == "items" and v["type"] == "bars"):
                    text = f'{it.get("display", it.get("value"))}{v.get("unit", "")}'
                out.append(f"- {label}: {text}".rstrip(": "))
        if v.get("source"):
            out.append(f"Source: {v['source']['title']} ({v['source']['url']})")
        out.append("")
    out += ["## Frequently asked questions", ""]
    for f in spec["faqs"]:
        out += [f"### {f['q']}", "", f["a"], ""]
    out += [f"---", f"{site['brand']} — {cfg['lead']['offer']}: {site['base_url']}/"]
    return "\n".join(out)


def plain_text(spec):
    body = " ".join(html_to_markdown(s["body_html"]) for s in spec["sections"])
    faqs = " ".join(f["q"] + " " + f["a"] for f in spec["faqs"])
    vis = []
    for v in spec.get("visuals", []):
        vis.append(v.get("title", "") + " " + v.get("lead", ""))
        for key in ("items", "steps", "rows"):
            for it in v.get(key, []):
                vis.append(" ".join(str(it.get(k, "")) for k in ("title", "label", "note", "text", "value", "when")))
    return f'{spec["h1"]} {spec["answer"]} {" ".join(spec.get("key_takeaways", []))} {body} {" ".join(vis)} {faqs}'
