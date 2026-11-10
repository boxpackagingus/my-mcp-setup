"""The /blog/ page: the parent of every blog post, and the index that lists them (newest first)."""
import html as _html
import json
from datetime import date

from . import config, page

_e = _html.escape

STYLE = """<style>
body:has(.cpbi) .entry-title,body:has(.cpbi) .page-header{display:none}
body:has(.cpbi){overflow-x:clip}
.cpbi{--b-night:#0D0D12;--b-red:#CA272C;--b-gold:#FFC727;--b-ink:#16171c;font-size:16px;line-height:1.6;color:#3d3f48}
.cpbi *{box-sizing:border-box}
.cpbi-bleed{width:100vw;margin-left:calc(50% - 50vw)}
.cpbi-band{background:radial-gradient(70% 140% at 0% 100%,rgba(202,39,44,.85),transparent 55%),var(--b-night);color:#fff;text-align:center;padding:clamp(60px,8vw,100px) 20px clamp(70px,9vw,110px)}
.cpbi-band h1{color:#fff!important;font-size:clamp(40px,5vw,58px);font-weight:700;margin:0 0 18px}
.cpbi-band p{margin:0 auto;max-width:720px;font-size:17px;opacity:.9}
.cpbi-list{background:#f3f3f3;padding:clamp(56px,7vw,100px) 20px}
.cpbi-grid{list-style:none;margin:0 auto;padding:0;max-width:1200px;display:grid;gap:26px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}
.cpbi-grid li{margin:0}
.cpbi-card{display:flex;flex-direction:column;height:100%;background:#fff;border-radius:22px;overflow:hidden;text-decoration:none!important;color:inherit;transition:transform .2s,box-shadow .2s}
.cpbi-card:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(0,0,0,.08)}
.cpbi-card img{width:100%;aspect-ratio:2.13/1;object-fit:cover;display:block}
.cpbi-body{display:flex;flex-direction:column;gap:14px;padding:26px 20px 26px;flex:1}
.cpbi-body strong{color:var(--b-ink);font-size:20px;line-height:1.4;font-weight:500}
.cpbi-body span.cpbi-ex{font-size:14px;color:#2a2b30;line-height:1.55}
.cpbi-body span.cpbi-more{margin-top:auto;padding-top:14px;color:var(--b-gold);font-weight:700;font-size:13px;letter-spacing:.03em;text-transform:uppercase}
.cpbi-pager{display:flex;justify-content:center;gap:22px;margin:44px 0 0;font-size:17px}
.cpbi-pager button{background:none;border:0;font:inherit;color:var(--b-ink);cursor:pointer;padding:2px 4px}
.cpbi-pager button[aria-current=true]{color:var(--b-gold);font-weight:700}
.cpbi-pager button:disabled{opacity:.35;cursor:default}
.cpbi-cta{background:radial-gradient(80% 120% at 100% 100%,rgba(230,90,40,.85),transparent 60%),radial-gradient(70% 120% at 0% 100%,rgba(202,39,44,.9),transparent 60%),var(--b-night);padding:clamp(56px,7vw,90px) 20px}
.cpbi-cta h2{color:#fff;text-align:center;font-size:clamp(28px,3.4vw,40px);line-height:1.2;margin:0 auto 34px;max-width:560px;font-weight:700}
.cpbi-card2{background:#fff;border-radius:36px;max-width:1195px;margin:0 auto;padding:clamp(28px,4vw,50px)}
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


def _excerpt(spec, words=24):
    w = ("Short answer: " + spec["answer"]).split()
    return " ".join(w[:words]) + ("…" if len(w) > words else "")


PAGER = """<script>(function(){var g=document.querySelector('.cpbi-grid'),n=document.querySelector('.cpbi-pager');if(!g||!n)return;
var items=[].slice.call(g.children),per=12,pages=Math.ceil(items.length/per),cur=1;if(pages<2){n.remove();return;}
function show(p){cur=p;items.forEach(function(li,i){li.hidden=Math.floor(i/per)!==p-1;});draw();
if(p>1||window.scrollY>400)g.scrollIntoView({behavior:'smooth',block:'start'});}
function btn(t,p,dis,curr){var b=document.createElement('button');b.type='button';b.textContent=t;b.disabled=!!dis;if(curr)b.setAttribute('aria-current','true');b.onclick=function(){show(p);};return b;}
function draw(){n.innerHTML='';n.append(btn('« Prev',cur-1,cur===1));for(var i=1;i<=pages;i++)n.append(btn(String(i),i,false,i===cur));n.append(btn('Next »',cur+1,cur===pages));}
items.forEach(function(li,i){li.hidden=i>=per;});draw();})();</script>"""


def render(cfg):
    base = cfg["site"]["base_url"].rstrip("/")
    city, region = page.place(cfg)
    items = posts()
    cards = []
    for i, s in enumerate(items):
        img = (s.get("hero_image") or {}).get("url", "")
        cards.append(
            f'<li><a class="cpbi-card" href="{_e(page.page_url(s, cfg))}">'
            + (f'<img src="{_e(img)}" alt="{_e((s.get("hero_image") or {}).get("alt", s["h1"]))}" loading="{"eager" if i < 3 else "lazy"}" width="1600" height="760">' if img else "")
            + f'<span class="cpbi-body"><strong>{_e(s["h1"])}</strong><span class="cpbi-ex">{_e(_excerpt(s))}</span>'
            f'<span class="cpbi-more">Read more »</span></span></a></li>'
        )
    btn = cfg["lead"].get("fallback_button") or {"text": "Book your AI visibility audit", "url": base + "/"}
    html = (
        STYLE + '<div class="cpbi">'
        '<header class="cpbi-band cpbi-bleed"><h1>Blog</h1>'
        f'<p>Thoughts, ideas and practical playbooks on AI search, from the Chimera team in {_e(city)}, for businesses across {_e(region)}.</p></header>'
        f'<section class="cpbi-list cpbi-bleed"><ul class="cpbi-grid">{"".join(cards) or "<li>New posts are on the way.</li>"}</ul>'
        '<nav class="cpbi-pager" aria-label="Blog pages"></nav></section>'
        '<section class="cpbi-cta cpbi-bleed" id="get-started"><h2>To Get Started, Simply Fill Out The Form Below!</h2>'
        f'<div class="cpbi-card2"><div class="chimera-lead" data-chimera-form="full"><p>'
        f'<a class="cp-btn cp-btn--primary" href="{_e(btn["url"])}">{_e(btn["text"])}</a></p></div></div></section>'
        '</div>' + PAGER
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
