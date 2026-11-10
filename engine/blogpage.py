"""Blog post layout (editorial style): dark title band, large banner, one reading column,
grey FAQ accordions, previous-post link, related articles with images and a dark form band.
Guides keep the layout in page.py; only specs with "kind": "blog" use this one."""
import html as _html
from datetime import date

from . import config

_e = _html.escape

STYLE = """<style>
body:has(.cpb) .entry-title,body:has(.cpb) .page-header{display:none}
body:has(.cpb){overflow-x:clip}
.cpb{--b-night:#0D0D12;--b-red:#CA272C;--b-gold:#FFC727;--b-ink:#16171c;--b-text:#3d3f48;--b-pill:#dcdcdc;color:var(--b-text);font-size:17px;line-height:1.7}
.cpb *{box-sizing:border-box}
.cpb-bleed{width:100vw;margin-left:calc(50% - 50vw)}
.cpb-band{background:radial-gradient(70% 140% at 0% 100%,rgba(202,39,44,.85),transparent 55%),var(--b-night);color:#fff;padding:clamp(56px,8vw,96px) 20px clamp(64px,9vw,110px);text-align:center}
.cpb-band .cpb-crumbs{font-size:13px;opacity:.75;margin:0 0 18px}
.cpb-band .cpb-crumbs a{color:#fff;text-decoration:none}
.cpb-band .cpb-crumbs a:hover{color:var(--b-gold)}
.cpb-band .cpb-kicker{display:inline-block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--b-gold);font-weight:700;margin:0 0 14px}
.cpb-band h1{color:#fff!important;font-size:clamp(30px,4.6vw,56px);line-height:1.15;font-weight:700;margin:0 auto;max-width:1150px;letter-spacing:-.01em}
.cpb-band .cpb-meta{margin:22px 0 0;font-size:14px;opacity:.8}
.cpb-wrap{max-width:980px;margin:0 auto;padding:0 20px}
.cpb-banner{margin:clamp(40px,6vw,90px) auto 0;max-width:980px}
.cpb-banner img{width:100%;height:auto;display:block;border-radius:0}
.cpb-body{max-width:960px;margin:0 auto;padding:clamp(32px,4vw,56px) 10px 0}
.cpb-body p{margin:0 0 18px}
.cpb-body a{color:#d9a400;text-decoration:none}
.cpb-body a:hover{text-decoration:underline}
.cpb-body strong{color:var(--b-ink)}
.cpb-body h2{color:var(--b-ink);font-size:clamp(26px,3vw,36px);line-height:1.2;font-weight:700;margin:44px 0 18px;letter-spacing:-.01em}
.cpb-body h3{color:var(--b-ink);font-size:21px;margin:28px 0 12px}
.cpb-body ul,.cpb-body ol{margin:0 0 22px;padding-left:24px}
.cpb-body li{margin:0 0 12px}
.cpb-answer{font-size:17px}
.cpb-take{background:#f6f4f3;border-left:4px solid var(--b-gold);padding:22px 26px;margin:28px 0 8px;border-radius:0 12px 12px 0}
.cpb-take p{margin:0 0 8px;font-weight:700;color:var(--b-ink)}
.cpb-take ul{margin:0}
.cpb-body table{width:100%;border-collapse:collapse;margin:8px 0 26px;font-size:15px;line-height:1.5}
.cpb-body th{background:var(--b-night);color:#fff;text-align:left;padding:12px 14px;font-weight:600}
.cpb-body td{padding:12px 14px;border-bottom:1px solid #e4e4e4;vertical-align:top}
.cpb-body tr:nth-child(even) td{background:#f8f8f8}
.cpb-tablewrap{overflow-x:auto}
.cpb-figure{margin:30px 0}
.cpb-figure img{width:100%;height:auto;display:block;border-radius:14px}
.cpb-figure figcaption{font-size:13px;color:#7a7c85;margin-top:8px}
.cpb .cp-vis{margin:30px 0;padding:clamp(22px,3vw,34px)!important;border-radius:18px;background:#f6f4f3!important;color:var(--b-ink)}
.cpb .cp-vis h3.cp-vis-title{font-size:24px;margin:0 0 6px;color:var(--b-ink);font-weight:700}
.cpb-faq summary h3{margin:0;font-size:16px;font-weight:500;color:var(--b-ink);line-height:1.4}
.cpb h3.cp-h4{font-size:1rem;margin:0 0 .35em}
.cpb-faqhead{margin-top:52px}
.cpb-faqsub{margin:0 0 26px}
.cpb-faqsub span{color:#d9a400}
.cpb-faq{background:var(--b-pill);border-radius:30px;margin:0 0 14px;overflow:hidden}
.cpb-faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:17px 26px;font-weight:500;color:var(--b-ink);font-size:16px}
.cpb-faq summary::-webkit-details-marker{display:none}
.cpb-faq summary::after{content:"";width:9px;height:9px;border-right:2px solid var(--b-ink);border-bottom:2px solid var(--b-ink);transform:rotate(45deg);margin-top:-4px;flex:none;transition:transform .2s}
.cpb-faq[open] summary::after{transform:rotate(-135deg);margin-top:4px}
.cpb-faq div{padding:0 26px 20px;font-size:15.5px}
.cpb-faq div p{margin:0}
.cpb-sources{font-size:14px;margin-top:36px}
.cpb-sources p{font-weight:700;color:var(--b-ink);margin-bottom:8px}
.cpb-sources ul{padding-left:20px}
.cpb-sources li{margin:0 0 6px}
.cpb-nav{max-width:980px;margin:48px auto 0;border-top:1px solid #222;border-bottom:1px solid #222;display:flex;justify-content:space-between;gap:20px;padding:18px 0;font-size:15px}
.cpb-nav a{color:var(--b-ink);text-decoration:none;font-weight:600}
.cpb-nav a:hover{color:#d9a400}
.cpb-nav small{display:block;font-weight:400;color:#7a7c85;font-size:12px;text-transform:uppercase;letter-spacing:.1em}
.cpb-related{max-width:1200px;margin:0 auto;padding:clamp(56px,7vw,90px) 20px}
.cpb-related h2{color:var(--b-ink);font-size:clamp(28px,3vw,38px);margin:0 0 36px;font-weight:700}
.cpb-relgrid{list-style:none;margin:0;padding:0;display:grid;gap:26px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}
.cpb-relgrid a{display:block;text-decoration:none;color:var(--b-ink)}
.cpb-relgrid img{width:100%;aspect-ratio:2.1/1;object-fit:cover;display:block}
.cpb-relgrid h3{display:block;margin-top:18px;font-size:19px;line-height:1.4;font-weight:500}
.cpb-relgrid a:hover h3{color:#d9a400}
.cpb-cta{background:radial-gradient(80% 120% at 100% 100%,rgba(230,90,40,.85),transparent 60%),radial-gradient(70% 120% at 0% 100%,rgba(202,39,44,.9),transparent 60%),var(--b-night);padding:clamp(56px,7vw,90px) 20px}
.cpb-cta h2{color:#fff;text-align:center;font-size:clamp(28px,3.4vw,40px);line-height:1.2;margin:0 auto 34px;max-width:560px;font-weight:700}
.cpb-cta .cpb-local{color:#e9e9ee;text-align:center;max-width:760px;margin:-14px auto 30px;font-size:15.5px}
.cpb-card{background:#fff;border-radius:36px;max-width:1195px;margin:0 auto;padding:clamp(28px,4vw,50px)}
@media(max-width:640px){.cpb-nav{flex-direction:column}.cpb-faq summary{padding:15px 20px}}
</style>"""


def _date(iso):
    d = date.fromisoformat(iso[:10])
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def _published_specs():
    return {f.stem: config.read_json(f, {}) for f in config.PUBLISHED.glob("*.json")}


def _wrap_tables(body):
    return body.replace("<table>", '<div class="cpb-tablewrap"><table>').replace("</table>", "</table></div>")


def _shown(v):
    """Blog posts leave out scorecards and local-data charts (guides still show them)."""
    return v.get("type") != "scorecard" and (v.get("eyebrow") or "").lower() != "local data"


def render(spec, cfg):
    from . import page, visuals

    site = cfg["site"]
    base = site["base_url"].rstrip("/")
    blog_slug = cfg["publishing"].get("blog_page_slug", "blog")
    city, region = page.place(cfg)
    town = city.split(",")[0]
    pub = spec.get("published") or date.today().isoformat()
    minutes = max(3, round(len(page.plain_text(spec).split()) / 230))
    specs = _published_specs()

    out = [STYLE, '<div class="cpb">']

    # Title band
    out.append(
        '<header class="cpb-band cpb-bleed">'
        f'<p class="cpb-crumbs"><a href="{base}/">Home</a> &nbsp;/&nbsp; <a href="{base}/{blog_slug}/">Blog</a></p>'
        f'<p class="cpb-kicker">{_e(spec.get("category") or spec.get("eyebrow") or "Blog")} · {_e(town)}, {_e(region)}</p>'
        f'<h1>{_e(spec["h1"])}</h1>'
        f'<p class="cpb-meta">{_e(_date(pub))} · {minutes} min read · {_e(site["brand"])} team, {_e(town)}, CA</p>'
        '</header>'
    )

    hero = spec.get("hero_image")
    if hero:
        out.append(f'<div class="cpb-wrap"><figure class="cpb-banner"><img src="{_e(hero["url"])}" alt="{_e(hero["alt"])}" '
                   f'width="{int(hero.get("width", 1600))}" height="{int(hero.get("height", 840))}" loading="eager" decoding="async"></figure></div>')

    body = ['<article class="cpb-body">',
            f'<p class="cpb-answer"><strong>Short answer:</strong> {_e(spec["answer"])}</p>']
    if spec.get("key_takeaways"):
        body.append('<div class="cpb-take"><p>Key takeaways</p><ul>'
                    + "".join(f"<li>{_e(t)}</li>" for t in spec["key_takeaways"]) + "</ul></div>")
    for i, s in enumerate(spec["sections"]):
        body.append(f'<h2 id="{page._anchor(s["heading"])}">{_e(s["heading"])}</h2>{_wrap_tables(s["body_html"])}')
        for v in [v for v in spec.get("visuals", []) if v.get("after") == i and _shown(v)]:
            body.append(f'<div class="cp">{visuals.render(v, "light")}</div>')

    body.append(f'<h2 id="local">Local help in {_e(town)} and {_e(region)}</h2>'
                f'<p>{_e(page.local_paragraph(spec, cfg))} <a href="#get-started">Book a free AI visibility audit</a>.</p>')

    body.append('<h2 class="cpb-faqhead" id="faq">Frequently Asked Questions</h2>'
                '<p class="cpb-faqsub">Have questions about AI search? We have <span>answers!</span></p>')
    body.append("".join(f'<details class="cpb-faq"><summary><h3>{_e(f["q"])}</h3></summary><div><p>{_e(f["a"])}</p></div></details>'
                        for f in spec["faqs"]))

    body.append("</article>")
    out.append('<div class="cpb-wrap">' + "".join(body) + "</div>")

    # Previous post (the newest older post; stays correct as new posts are added) and the blog index.
    blogs = sorted((s for s in specs.values() if s.get("kind") == "blog" and s.get("slug") != spec["slug"]),
                   key=lambda s: (s.get("published", ""), -s.get("slot", 0)), reverse=True)
    key = (pub, -spec.get("slot", 0))
    older = next((s for s in blogs if (s.get("published", ""), -s.get("slot", 0)) < key), None)
    prev = (f'<a href="{_e(page.page_url(older, cfg))}"><small>« Previous post</small>{_e(older["h1"])}</a>'
            if older else f'<a href="{base}/{blog_slug}/"><small>Blog</small>All posts</a>')
    out.append(f'<div class="cpb-wrap"><nav class="cpb-nav" aria-label="Post navigation">{prev}'
               f'<a href="{base}/{blog_slug}/" style="text-align:right"><small>More from Chimera</small>All blog posts »</a></nav></div>')

    # Related articles: the newest other posts first, then the page's related guides. Each has a banner.
    rel = [s for s in blogs if s.get("hero_image")][:3]
    for l in spec.get("internal_links", []):
        slug = l["url"].rstrip("/").split("/")[-1]
        s = specs.get(slug)
        if s and s.get("hero_image") and s["slug"] != spec["slug"] and s not in rel:
            rel.append(s)
    cards = "".join(
        f'<li><a href="{_e(page.page_url(s, cfg))}"><img src="{_e(s["hero_image"]["url"])}" alt="{_e(s["hero_image"].get("alt", s["h1"]))}" '
        f'loading="lazy" width="1200" height="571"><h3>{_e(s["h1"])}</h3></a></li>' for s in rel[:3])
    if cards:
        out.append(f'<section class="cpb-related"><h2>Related Articles</h2><ul class="cpb-relgrid">{cards}</ul></section>')

    # Form band (the plugin swaps .chimera-lead for the live form).
    btn = cfg["lead"].get("fallback_button") or {"text": "Book your AI visibility audit", "url": base + "/"}
    out.append(
        '<section class="cpb-cta cpb-bleed" id="get-started"><h2>To Get Started, Simply Fill Out The Form Below!</h2>'
        f'<p class="cpb-local">{_e(site["brand"])} is based in {_e(city)} and works with businesses across {_e(region)}.</p>'
        f'<div class="cpb-card"><div class="chimera-lead" data-chimera-form="full"><p>'
        f'<a class="cp-btn cp-btn--primary" href="{_e(btn["url"])}">{_e(btn["text"])}</a></p></div></div></section>'
    )
    out.append("</div>")
    return "\n".join(out)
