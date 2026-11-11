"""The /blog/ page: the parent of every blog post, and the index that lists them (newest first)."""
import html as _html
import json
from datetime import date

from . import config, page

_e = _html.escape

STYLE = """<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Inter+Tight:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
body:has(.cph){background:#FBFAF7!important;overflow-x:clip}
body:has(.cph) .entry-title,body:has(.cph) .page-header,body:has(.cph) .elementor-location-header,body:has(.cph) .elementor-location-footer,
body:has(.cph) header.site-header,body:has(.cph) footer.site-footer{display:none!important}
body:has(.cph) .site-main,body:has(.cph) .page-content,body:has(.cph) main{max-width:none!important;padding:0!important;margin:0!important}
.cph{--bg:#FBFAF7;--bg-2:#F5F1E8;--white:#fff;--ink:#15140F;--ink-2:#2E2C26;--muted:#6A675F;--line:#E8E2D5;--gold:#FFC827;--gold-2:#F5B800;--gold-soft:#FFF5D6;
--display:"Archivo","Helvetica Neue",Arial,sans-serif;--body:"Inter Tight","Helvetica Neue",Arial,sans-serif;--mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
--shadow-sm:0 1px 2px rgba(40,30,0,.05),0 4px 14px -6px rgba(40,30,0,.08);--shadow:0 2px 4px rgba(40,30,0,.04),0 24px 60px -24px rgba(60,44,0,.22);
--ease:cubic-bezier(.16,1,.3,1);font-family:var(--body);color:var(--ink-2);background:var(--bg);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.cph *{box-sizing:border-box}.cph a{text-decoration:none!important;color:inherit}
.cph-bleed{width:100vw;margin-left:calc(50% - 50vw)}
.cph-wrap{max-width:1240px;margin:0 auto;padding:0 clamp(16px,3.2vw,40px)}
.cph-hdr{position:sticky;top:14px;z-index:50;padding:0 16px}
.cph-bar{max-width:1240px;margin:0 auto;height:66px;padding:0 8px 0 24px;border-radius:999px;display:flex;align-items:center;justify-content:space-between;gap:20px;
background:#ffffffe0;backdrop-filter:blur(18px) saturate(1.6);-webkit-backdrop-filter:blur(18px) saturate(1.6);border:1px solid rgba(232,226,213,.9);box-shadow:0 10px 30px -18px #3c2c0040}
.cph-bar img{height:28px;width:auto;display:block}
.cph-nav{display:flex;gap:6px;font-size:14.5px;font-weight:500;color:var(--ink-2)}
.cph-nav a{padding:8px 14px;border-radius:999px;transition:background .25s}
.cph-nav a:hover{background:var(--bg-2)}.cph-nav a[aria-current=page]{background:var(--gold-soft);color:var(--ink)}
.cph-cta{height:46px;padding:0 8px 0 20px;display:inline-flex;align-items:center;gap:12px;background:var(--ink);color:#fff!important;border-radius:999px;font-size:14px;font-weight:600}
.cph-cta i,.cph-go i{width:32px;height:32px;border-radius:50%;background:var(--gold);color:var(--ink);display:grid;place-items:center;font-style:normal}
.cph-hero{position:relative;padding:clamp(70px,9vw,120px) 0 clamp(40px,5vw,64px);background:radial-gradient(55% 80% at 88% 0%,#FFF5D6 0%,transparent 62%),var(--bg)}
.cph-hero:before{content:"";position:absolute;inset:0;background:linear-gradient(#F0EBE1 1px,transparent 1px) 0 0/72px 72px,linear-gradient(90deg,#F0EBE1 1px,transparent 1px) 0 0/72px 72px;-webkit-mask-image:radial-gradient(80% 90% at 50% 0%,#000 30%,transparent 85%);mask-image:radial-gradient(80% 90% at 50% 0%,#000 30%,transparent 85%);pointer-events:none}
.cph-hero .cph-wrap{position:relative}
.cph-eyebrow{display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border-radius:999px;background:#fff;border:1px solid var(--line);font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.cph-eyebrow b{width:7px;height:7px;border-radius:50%;background:var(--gold-2)}
.cph h1.cph-title{font-family:var(--display)!important;font-weight:700;color:var(--ink)!important;font-size:clamp(44px,6.4vw,92px);line-height:.98;letter-spacing:-.035em;margin:22px 0 22px;max-width:14ch}
.cph-title em{font-style:normal;background:linear-gradient(transparent 62%,var(--gold) 62%,var(--gold) 92%,transparent 92%)}
.cph-lead{max-width:620px;font-size:clamp(17px,1.4vw,19px);color:var(--muted);margin:0}
.cph-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:34px}
.cph-chips button{font:500 14px var(--body);padding:9px 16px;border-radius:999px;border:1px solid var(--line);background:#fff;color:var(--ink-2);cursor:pointer;transition:all .25s}
.cph-chips button:hover{border-color:var(--ink)}.cph-chips button[aria-pressed=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
.cph-list{padding:clamp(20px,3vw,40px) 0 clamp(70px,8vw,110px)}
.cph-feat{display:grid;grid-template-columns:1.35fr 1fr;align-items:stretch;background:#fff;border:1px solid var(--line);border-radius:28px;overflow:hidden;box-shadow:var(--shadow);margin-bottom:28px;transition:transform .5s var(--ease)}
.cph-feat:hover{transform:translateY(-4px)}
.cph-feat img{width:100%;height:100%;min-height:100%;object-fit:cover;object-position:left center;display:block}
.cph-feat .cph-body{padding:clamp(26px,3.4vw,48px);gap:16px;justify-content:center}
.cph-feat h2.cph-h{font-size:clamp(26px,2.6vw,36px)}
.cph-grid{list-style:none;margin:0;padding:0;display:grid;gap:24px;grid-template-columns:repeat(auto-fill,minmax(310px,1fr))}
.cph-grid li{margin:0}
.cph-card{display:flex;flex-direction:column;height:100%;background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow-sm);transition:transform .5s var(--ease),box-shadow .5s var(--ease)}
.cph-card:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.cph-card img{width:100%;aspect-ratio:1600/760;object-fit:cover;display:block}
.cph-body{display:flex;flex-direction:column;gap:12px;padding:22px 22px 24px;flex:1}
.cph-meta{display:flex;align-items:center;gap:10px;font-family:var(--mono);font-size:12px;color:var(--muted)}
.cph-tag{padding:4px 10px;border-radius:999px;background:var(--gold-soft);color:#7a5600;font-family:var(--body);font-weight:600;font-size:12px}
.cph h2.cph-h{font-family:var(--display)!important;font-weight:700;color:var(--ink)!important;font-size:21px;line-height:1.2;letter-spacing:-.015em;margin:0}
.cph-ex{font-size:15px;color:var(--muted);line-height:1.55}
.cph-go{margin-top:auto;padding-top:8px;display:inline-flex;align-items:center;gap:10px;font-weight:600;font-size:14px;color:var(--ink)}
.cph-go i{width:28px;height:28px;font-size:13px;transition:transform .4s var(--ease)}
.cph-card:hover .cph-go i,.cph-feat:hover .cph-go i{transform:translateX(4px)}
.cph-pager{display:flex;justify-content:center;gap:8px;margin:44px 0 0}
.cph-pager button{min-width:42px;height:42px;padding:0 14px;border-radius:999px;border:1px solid var(--line);background:#fff;font:600 14px var(--body);color:var(--ink);cursor:pointer}
.cph-pager button[aria-current=true]{background:var(--ink);color:#fff;border-color:var(--ink)}.cph-pager button:disabled{opacity:.35;cursor:default}
.cph-cta-band{padding:0 0 clamp(60px,7vw,100px)}
.cph-gold{background:var(--gold);border-radius:36px;padding:clamp(34px,5vw,64px);display:grid;grid-template-columns:1fr 1.1fr;gap:clamp(24px,4vw,56px);align-items:center;box-shadow:0 18px 40px -16px rgba(245,184,0,.65)}
.cph-gold h2{font-family:var(--display)!important;color:var(--ink)!important;font-size:clamp(32px,3.8vw,52px);line-height:1;letter-spacing:-.03em;margin:0 0 16px;font-weight:700}
.cph-gold p{margin:0;color:var(--ink-2);font-size:17px}
.cph-gold ul{list-style:none;padding:0;margin:20px 0 0;display:flex;flex-wrap:wrap;gap:8px 20px;font-size:14px;font-weight:600;color:var(--ink)}
.cph-form{background:#fff;border-radius:24px;padding:clamp(20px,3vw,32px);box-shadow:var(--shadow)}
.cph-ftr{border-top:1px solid var(--line);padding:clamp(56px,7vw,90px) 0 28px;background:var(--bg)}
.cph-fgrid{display:grid;grid-template-columns:minmax(0,1.6fr) repeat(3,minmax(0,1fr));gap:40px}
.cph-fgrid img{height:30px;width:auto}.cph-fgrid p{color:var(--muted);max-width:340px;margin:16px 0 0;font-size:15px}
.cph-fgrid .cph-fh{font-family:var(--body);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 16px;font-weight:600}
.cph-fgrid ul{list-style:none;padding:0;margin:0;display:grid;gap:12px;font-size:15px;color:var(--ink-2)}
.cph-fgrid a:hover{color:var(--ink);text-decoration:underline!important}
.cph-base{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-top:56px;padding-top:20px;border-top:1px solid var(--line);font-size:13px;color:var(--muted)}
.cph .cp-form{background:none!important;box-shadow:none!important;padding:0!important;border-radius:0!important;font-family:var(--body)}
.cph .cp-hp{position:absolute!important;left:-9999px!important}
.cph .cp-form-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
.cph .cp-field{display:flex;flex-direction:column;gap:6px;margin:0}.cph .cp-field--wide{grid-column:1/-1}
.cph .cp-field span{font-size:13px;font-weight:600;color:var(--ink-2)}
.cph .cp-form input,.cph .cp-form select,.cph .cp-form textarea{width:100%;font:400 15px var(--body);color:var(--ink)!important;background:var(--bg)!important;border:1px solid var(--line)!important;border-radius:12px!important;padding:12px 14px!important;box-shadow:none!important;outline:none}
.cph .cp-form input:focus,.cph .cp-form select:focus,.cph .cp-form textarea:focus{border-color:var(--ink)!important;background:#fff!important}
.cph .cp-form textarea{min-height:92px;resize:vertical}
.cph .cp-form button[type=submit]{width:100%;height:52px;display:inline-flex;align-items:center;justify-content:center;gap:12px;background:var(--ink)!important;color:#fff!important;border:0!important;border-radius:999px!important;font:600 15px var(--body)!important;cursor:pointer;box-shadow:none!important;padding:0 24px!important}
.cph .cp-form button[type=submit]:after{content:"→";width:30px;height:30px;border-radius:50%;background:var(--gold);color:var(--ink);display:grid;place-items:center}
.cph .cp-form button[type=submit]:hover{background:#000!important}
.cph .cp-form-note{margin:10px 0 0;font-size:13px;color:var(--muted);text-align:center}
.cph .cp-form-status{margin:12px 0 0;padding:12px 14px;border-radius:12px;background:#E6F4EC;color:#14532d}
.cph-menu{display:none;position:relative}.cph-menu summary{list-style:none;width:46px;height:46px;border-radius:50%;background:var(--bg-2);display:grid;place-items:center;cursor:pointer;font-size:18px}
.cph-menu summary::-webkit-details-marker{display:none}
.cph-menu nav{position:absolute;right:0;top:56px;background:#fff;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow);padding:10px;display:grid;min-width:200px}
.cph-menu nav a{padding:10px 14px;border-radius:12px;font-weight:500}.cph-menu nav a:hover{background:var(--bg-2)}
@media(max-width:960px){.cph-menu{display:block}.cph-nav{display:none}.cph-feat,.cph-gold{grid-template-columns:1fr}.cph-feat img{height:auto;aspect-ratio:1600/760}.cph-fgrid{grid-template-columns:1fr 1fr}.cph-fgrid>div:first-child{grid-column:1/-1}}
@media(max-width:560px){.cph .cp-form-grid{grid-template-columns:1fr}.cph-eyebrow{font-size:11px}.cph-bar{height:58px;padding-left:18px}.cph-cta span{display:none}.cph-cta{padding:0 7px}.cph-grid{grid-template-columns:1fr}}
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


LOGO = "https://thechimeraai.com/wp-content/plugins/chimera-geo-home/assets/chimera-logo.webp"
GROUPS = {"Google Search": ["Google Search", "Google news", "Google AI Mode", "Google AI Search", "Search Trends"],
          "Search Console": ["Search Console"], "AI assistants": ["AI assistants", "AI news"],
          "Shopping": ["Shopping trends", "AI Shopping"], "Playbooks": ["Playbooks", "SEO learning"]}


def _group(cat):
    return next((g for g, cats in GROUPS.items() if cat in cats), "Playbooks")


PAGER = """<script>(function(){var g=document.querySelector('.cph-grid'),n=document.querySelector('.cph-pager'),f=document.querySelector('.cph-feat');if(!g||!n)return;
var all=[].slice.call(g.children),per=12,cur=1,filter='All';
function items(){return all.filter(function(li){return filter==='All'||li.dataset.group===filter;});}
function show(p){var list=items(),pages=Math.max(1,Math.ceil(list.length/per));cur=Math.min(Math.max(1,p),pages);
all.forEach(function(li){li.hidden=true;});list.forEach(function(li,i){li.hidden=Math.floor(i/per)!==cur-1;});
if(f)f.hidden=!(filter==='All'||f.dataset.group===filter);draw(pages);}
function btn(t,p,dis,curr){var b=document.createElement('button');b.type='button';b.textContent=t;b.disabled=!!dis;if(curr)b.setAttribute('aria-current','true');
b.onclick=function(){show(p);g.scrollIntoView({behavior:'smooth',block:'start'});};return b;}
function draw(pages){n.innerHTML='';if(pages<2)return;n.append(btn('←',cur-1,cur===1));for(var i=1;i<=pages;i++)n.append(btn(String(i),i,false,i===cur));n.append(btn('→',cur+1,cur===pages));}
document.querySelectorAll('.cph-chips button').forEach(function(c){c.onclick=function(){document.querySelectorAll('.cph-chips button').forEach(function(x){x.setAttribute('aria-pressed','false');});
c.setAttribute('aria-pressed','true');filter=c.dataset.f;show(1);};});show(1);})();</script>"""


def _date(s):
    try:
        return date.fromisoformat(s.get("published", "")).strftime("%b %d, %Y")
    except ValueError:
        return ""


def _card(s, cfg, i, cls="cph-card", words=24):
    img = (s.get("hero_image") or {}).get("url", "")
    alt = (s.get("hero_image") or {}).get("alt", s["h1"])
    return (f'<a class="{cls}" data-group="{_e(_group(s.get("category", "")))}" href="{_e(page.page_url(s, cfg))}">'
            + (f'<img src="{_e(img)}" alt="{_e(alt)}" loading="{"eager" if i < 4 else "lazy"}" width="1600" height="760">' if img else "")
            + f'<div class="cph-body"><div class="cph-meta"><span class="cph-tag">{_e(s.get("category") or "Blog")}</span><span>{_date(s)}</span></div>'
            f'<h2 class="cph-h">{_e(s["h1"])}</h2><span class="cph-ex">{_e(_excerpt(s, words))}</span>'
            '<span class="cph-go">Read article <i aria-hidden="true">→</i></span></div></a>')


def _header(base):
    nav = [("Why GEO", "/#shift"), ("Services", "/#services"), ("Process", "/#process"), ("Results", "/#results"), ("FAQ", "/#faq")]
    links = "".join(f'<a href="{base}{h}">{t}</a>' for t, h in nav) + f'<a href="{base}/blog/" aria-current="page">Blog</a>'
    return (f'<div class="cph-hdr cph-bleed"><div class="cph-bar"><a href="{base}/" aria-label="Chimera home"><img src="{LOGO}" alt="Chimera Marketing &amp; Advertisement" height="28"></a>'
            f'<nav class="cph-nav" aria-label="Primary">{links}</nav>'
            f'<div style="display:flex;gap:8px;align-items:center"><a class="cph-cta" href="{base}/#scan"><span>Free AI scan</span><i aria-hidden="true">→</i></a>'
            f'<details class="cph-menu"><summary aria-label="Menu">☰</summary><nav>{links}</nav></details></div></div></div>')


def _footer(base, city, region):
    col = lambda title, rows: f'<div><p class="cph-fh">{title}</p><ul>' + "".join(f'<li><a href="{base}{h}">{t}</a></li>' for t, h in rows) + "</ul></div>"
    return ('<footer class="cph-ftr cph-bleed"><div class="cph-wrap"><div class="cph-fgrid">'
            f'<div><img src="{LOGO}" alt="Chimera Marketing &amp; Advertisement" height="30"><p>GEO and AI SEO agency in Anaheim, serving businesses across Orange County, California.</p></div>'
            + col("Page", [("Why GEO", "/#shift"), ("Services", "/#services"), ("Process", "/#process"), ("Results", "/#results"), ("FAQ", "/#faq"), ("Blog", "/blog/"), ("Free AI scan", "/#scan")])
            + col("GEO", [("AI Visibility Audit", "/ai-visibility-audit/"), ("Content Structuring", "/how-to-write-content-for-ai-search/"),
                          ("Schema and llms.txt", "/schema-markup-for-ai-search/"), ("Citation Optimization", "/how-ai-search-engines-choose-sources/")])
            + col("Also from Chimera", [("SEO and Local SEO", "/seo-company-orange-county/"), ("Paid Marketing", "/geo-vs-ppc/"),
                                        ("Web Development", "/core-web-vitals-for-local-businesses/"), ("Branding and Design", "/how-to-get-brand-mentions-for-ai-search/")])
            + f'</div><div class="cph-base"><span>© {date.today().year} Chimera Marketing</span><span>Anaheim · Orange County, California</span>'
            '<a href="#top">Back to top ↑</a></div></div></footer>')


def render(cfg):
    base = cfg["site"]["base_url"].rstrip("/")
    city, region = page.place(cfg)
    items = posts()
    feat, rest = (items[0], items[1:]) if items else (None, [])
    cards = "".join(f'<li data-group="{_e(_group(s.get("category", "")))}">{_card(s, cfg, i + 1)}</li>' for i, s in enumerate(rest))
    chips = '<button type="button" data-f="All" aria-pressed="true">All posts</button>' + "".join(
        f'<button type="button" data-f="{_e(g)}" aria-pressed="false">{_e(g)}</button>'
        for g in GROUPS if any(_group(s.get("category", "")) == g for s in items))
    btn = cfg["lead"].get("fallback_button") or {"text": "Book your AI visibility audit", "url": base + "/"}
    html = (
        STYLE + '<div class="cph" id="top">' + _header(base)
        + '<section class="cph-hero cph-bleed cpbi-band"><div class="cph-wrap">'
        '<span class="cph-eyebrow"><b></b>Chimera blog · Anaheim, CA</span>'
        '<h1 class="cph-title">Get your business <em>named</em> by AI.</h1>'
        f'<p class="cph-lead">Practical, source-checked guides on ChatGPT, Gemini, Google AI Overviews and local search, written by the Chimera team in Anaheim for businesses across Orange County, California.</p>'
        f'<div class="cph-chips" role="group" aria-label="Filter posts">{chips}</div></div></section>'
        '<section class="cph-list cph-bleed"><div class="cph-wrap">'
        + (_card(feat, cfg, 0, "cph-feat", 40) if feat else "")
        + f'<ul class="cph-grid">{cards}</ul><nav class="cph-pager" aria-label="Blog pages"></nav></div></section>'
        '<section class="cph-cta-band cph-bleed" id="get-started"><div class="cph-wrap"><div class="cph-gold">'
        '<div><h2>See what AI says about your business.</h2><p>Get a free AI visibility scan: we check how ChatGPT, Gemini, Perplexity and Google AI Overviews describe you, and what to fix first.</p>'
        '<ul><li>✓ Free 48-hour readiness report</li><li>✓ No obligation</li><li>✓ Works alongside your SEO</li></ul></div>'
        f'<div class="cph-form"><div class="chimera-lead" data-chimera-form="full"><p><a class="cp-btn cp-btn--primary" href="{_e(btn["url"])}">{_e(btn["text"])}</a></p></div></div>'
        '</div></div></section>' + _footer(base, city, region) + '</div>' + PAGER
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
