"""Site-wide internal linking.

For every published page and blog post:
  1. Links the first natural mention of key topics in the body text to the page that covers them (max 5 per page,
     one per target, never the page itself, never inside headings or existing links).
  2. Links the first mention of "Chimera" in the body text to the homepage.
  3. Tops up the related-links list with the most closely related pages (service pages and blog posts), and adds a
     homepage link.
Writes changed specs to content/drafts/ (ready to publish) and a report to data/interlink_report.json.
Run with --dry-run to write the report only.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB, DRAFTS = ROOT / "content" / "published", ROOT / "content" / "drafts"
BASE = "https://thechimeraai.com"

# Phrase (regex, case-insensitive) -> slug of the page that covers it. Longer, more specific phrases first.
PHRASES = [
    (r"Google Business Profile(?:s)? (?:suspension|suspended)", "google-business-profile-suspended"),
    (r"verify (?:your|the) (?:business|Business Profile)|Business Profile verification|verification code|postcard verification", "google-business-profile-verification"),
    (r"special hours|holiday hours", "google-business-profile-holiday-hours"),
    (r"service[- ]area business(?:es)?", "service-area-business-seo"),
    (r"service areas?", "google-business-profile-service-area"),
    (r"primary category|business categor(?:y|ies)", "google-business-profile-categories"),
    (r"Local Services Ads", "google-local-services-ads-vs-seo"),
    (r"Core Web Vitals|page speed", "core-web-vitals-for-local-businesses"),
    (r"fake reviews?|fake engagement", "how-to-remove-fake-google-reviews"),
    (r"repl(?:y|ies|ying) to (?:every |all )?reviews|respond(?:ing)? to reviews", "how-to-respond-to-google-reviews"),
    (r"genuine reviews|more reviews|review link", "how-to-get-more-google-reviews"),
    (r"Google Business Profile", "google-business-profile-optimization-orange-county"),
    (r"local business (?:schema|structured data)", "local-business-schema-for-ai-search"),
    (r"structured data|schema markup", "schema-markup-for-ai-search"),
    (r"llms\.txt", "best-practices-for-llms-txt"),
    (r"robots\.txt", "robots-txt-for-ai-crawlers"),
    (r"AI crawlers?", "ai-crawler-user-agents"),
    (r"AI Overviews", "how-to-show-up-in-google-ai-overviews"),
    (r"AI Mode", "how-to-optimize-for-google-ai-mode"),
    (r"Perplexity", "perplexity-seo"),
    (r"Microsoft Copilot|Copilot", "microsoft-copilot-seo"),
    (r"Meta AI", "how-to-optimize-for-meta-ai"),
    (r"ChatGPT recommends?|recommend(?:ed|s)? by ChatGPT", "how-chatgpt-recommends-local-businesses"),
    (r"ChatGPT", "how-to-rank-in-chatgpt"),
    (r"Gemini", "gemini-seo"),
    (r"E-E-A-T", "eeat-for-ai-search"),
    (r"near me", "near-me-searches"),
    (r"(?:consistent|inconsistent) listings|name, address and phone|NAP", "nap-consistency-local-citations"),
    (r"city pages?|doorway (?:pages|abuse)", "local-landing-pages"),
    (r"knowledge panel", "how-to-get-a-google-knowledge-panel"),
    (r"best-of lists?", "how-to-get-on-best-of-lists"),
    (r"Wikipedia|Wikidata", "wikipedia-and-wikidata-for-ai-search"),
    (r"Reddit", "reddit-for-ai-search"),
    (r"YouTube", "youtube-for-ai-search"),
    (r"zero-click", "zero-click-searches"),
    (r"query fan-out", "what-is-query-fan-out"),
    (r"brand mentions", "how-to-get-brand-mentions-for-ai-search"),
    (r"digital PR", "digital-pr-for-ai-search"),
    (r"comparison pages?", "how-to-write-comparison-pages"),
    (r"FAQ pages?", "faq-pages-for-ai-search"),
    (r"author (?:pages|bios)", "author-pages-for-eeat"),
    (r"internal links?", "internal-linking-for-ai-search"),
    (r"Search Console", "search-console-generative-ai-performance-report"),
    (r"Google Analytics", "how-to-track-ai-traffic-in-google-analytics"),
    (r"generative engine optimization|GEO\b", "what-is-generative-engine-optimization-and-how-does-it-work"),
    (r"local SEO", "local-seo-orange-county"),
    (r"Irvine", "seo-irvine"), (r"Santa Ana", "seo-santa-ana"), (r"Huntington Beach", "seo-huntington-beach"),
    (r"Newport Beach", "seo-newport-beach"), (r"Fullerton", "seo-fullerton"), (r"Costa Mesa", "seo-costa-mesa"),
]
MAX_CONTEXT = 5
MAX_RELATED_ADD = 4
MAX_LINKS = 13  # related-list size before the homepage card
STOP = set("the a an and or of for to in on with your you how what is are does do by from at as it its this that be can get"
           " guide orange county anaheim california 2026 seo local marketing agency business businesses near me google"
           " search ai should know means".split())

CLUSTERS = [
    ("hospitality", r"restaurant|bakeries|coffee|hotel|travel|wedding|event-planner|holiday-travel|eat-here|hotel-booking"),
    ("home", r"plumb|hvac|roof|electric|contractor|painter|landscap|pest|pool|tree|cleaning|carpet|window|junk|moving|garage|handyman|concrete|flooring|bathroom|kitchen|fence|pressure|water-damage|solar|locksmith|home-builder|interior|architect|home-services|property-management|self-storage"),
    ("legal", r"law|lawyer|attorney|personal-injury|estate-planning|criminal|immigration"),
    ("health", r"dentist|orthodont|doctor|chiropract|physical-therap|dermatolog|plastic-surg|optometr|veterinar|therapist|med-spa|healthcare|senior-living|massage"),
    ("lifestyle", r"salon|tattoo|gym|yoga|martial|dog-|photograph"),
    ("auto", r"auto-|car-"),
    ("professional", r"accountant|insurance|mortgage|financial|real-estate|it-companies|staffing|b2b|saas|manufactur|nonprofit|startup"),
    ("education", r"tutoring|private-school|daycare"),
    ("retail", r"shopify|ecommerce|product-pages|holiday-100|universal-cart|shopping"),
    ("gbp", r"google-business-profile|review|nap-|service-area|near-me|local-landing|local-seo|local-geo|local-business-schema|seo-company|seo-irvine|seo-santa|seo-hunt|seo-newport|seo-full|seo-costa|geo-agency|local-services-ads|core-web-vitals|30-day"),
    ("ai", r"chatgpt|gemini|perplexity|copilot|claude|meta-ai|ai-mode|ai-overviews|llm|query-fan|crawler|robots|llms-txt|training-control|carbon|october-2026|search-profiles|inline-links|businesses-in-chatgpt"),
]


def cluster(slug):
    return next((c for c, rx in CLUSTERS if re.search(rx, slug)), "geo")


def url_for(spec):
    return f'{BASE}/{"blog/" if spec.get("kind") == "blog" else ""}{spec["slug"]}/'


def tokens(spec):
    text = " ".join([spec.get("primary_keyword", ""), spec.get("h1", ""), " ".join(spec.get("secondary_keywords", [])),
                     spec.get("category", ""), spec.get("eyebrow", "")])
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) > 2}


TAG = re.compile(r"(<[^>]+>)")


def link_text(html, pattern, href, budget):
    """Wraps the first match of pattern in text nodes outside <a>, headings and table headers. Returns (html, done)."""
    parts = TAG.split(html)
    depth = {"a": 0, "h": 0, "th": 0}
    rx = re.compile(r"(?<![\w-])(" + pattern + r")(?![\w-])", re.I)
    for i, p in enumerate(parts):
        if p.startswith("<"):
            m = re.match(r"</?\s*(a|h[1-6]|th)\b", p, re.I)
            if m:
                key = "h" if m.group(1).lower().startswith("h") else m.group(1).lower()
                depth[key] += -1 if p.startswith("</") else 1
            continue
        if any(depth.values()) or not p.strip():
            continue
        m = rx.search(p)
        if m:
            parts[i] = p[:m.start()] + f'<a href="{href}">{m.group(1)}</a>' + p[m.end():]
            return "".join(parts), True
    return html, False


def main(dry=False):
    specs = {f.stem: json.loads(f.read_text()) for f in PUB.glob("*.json")}
    # Drafts (today's new pages, or pages already staged) take precedence over their published copies.
    specs.update({f.stem: json.loads(f.read_text()) for f in DRAFTS.glob("*.json")})
    before = {s: json.dumps(d, sort_keys=True) for s, d in specs.items()}
    toks = {s: tokens(d) for s, d in specs.items()}
    report, changed = {}, []
    for slug, spec in specs.items():
        me = url_for(spec)
        added_ctx, used = [], {slug}
        # Links already in the text count toward the per-page limit, so re-runs don't keep adding more.
        body = " ".join(sec["body_html"] for sec in spec["sections"])
        existing = {u.rstrip("/").split("/")[-1] for u in re.findall(r'<a href="' + re.escape(BASE) + r'/([a-z0-9/-]+)/"', body)}
        used |= existing
        budget = MAX_CONTEXT - len(existing)
        # 1. Contextual links in body text.
        for pattern, target in PHRASES:
            if len(added_ctx) >= budget:
                break
            if target in used or target not in specs:
                continue
            href = url_for(specs[target])
            for sec in spec["sections"]:
                if href in sec["body_html"]:
                    break
                # Google Business Profile topics only link from sections that are about the Business Profile.
                if target.startswith("google-business-profile-") and "Business Profile" not in sec["body_html"] + sec["heading"]:
                    continue
                new, ok = link_text(sec["body_html"], pattern, href, 1)
                if ok:
                    sec["body_html"] = new
                    added_ctx.append(target)
                    used.add(target)
                    break
        # 2. First "Chimera" mention -> homepage.
        home_ctx = False
        for sec in spec["sections"]:
            if f'href="{BASE}/"' in sec["body_html"]:
                home_ctx = True
                break
            new, ok = link_text(sec["body_html"], r"Chimera", f"{BASE}/", 1)
            if ok:
                sec["body_html"] = new
                home_ctx = True
                break
        # 3. Related list: top similar pages not yet linked, plus homepage.
        have = {l["url"].rstrip("/") for l in spec.get("internal_links", [])}
        linked = have | {url_for(specs[t]).rstrip("/") for t in added_ctx}
        mine = cluster(slug)

        def score(o):
            j = len(toks[slug] & toks[o]) / (len(toks[slug] | toks[o]) or 1)
            return j + (0.5 if cluster(o) == mine else 0)
        ranked = sorted((o for o in specs if o != slug), key=score, reverse=True)
        rel_added = []
        want_other_kind = "guide" if spec.get("kind") == "blog" else "blog"
        # Best page of the other kind first (a blog post for service pages, a guide for posts), then the closest pages.
        done_before = BASE in have  # already processed: keep its related list as it is
        for o in ([] if done_before else [next((o for o in ranked if (specs[o].get("kind") or "guide") == want_other_kind and score(o) > 0.05), None)] + ranked):
            if o is None or len(rel_added) >= MAX_RELATED_ADD or len(spec.get("internal_links", [])) >= MAX_LINKS:
                continue
            u = url_for(specs[o]).rstrip("/")
            if u in linked or score(o) < 0.08:
                continue
            if cluster(o) != mine and score(o) < 0.2 and rel_added:
                continue
            spec.setdefault("internal_links", []).append({"anchor": specs[o].get("short_title") or specs[o]["h1"], "url": u + "/"})
            linked.add(u)
            rel_added.append(o)
        if BASE not in have:
            spec["internal_links"].append({"anchor": "Chimera: GEO agency in Anaheim, Orange County", "url": f"{BASE}/"})
        report[slug] = {"context": added_ctx, "home_in_text": home_ctx, "related_added": rel_added}
        if not dry and json.dumps(spec, sort_keys=True) != before[slug]:
            (DRAFTS / f"{slug}.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
            changed.append(slug)
    (ROOT / "data" / "interlink_report.json").write_text(json.dumps(report, indent=1) + "\n")
    ctx = sum(len(r["context"]) for r in report.values())
    rel = sum(len(r["related_added"]) for r in report.values())
    print(f"{len(report)} pages · {ctx} in-text links · {rel} related links · homepage in text on "
          f"{sum(r['home_in_text'] for r in report.values())} · homepage card on all · {len(changed)} pages changed")


if __name__ == "__main__":
    main(dry="--dry-run" in sys.argv)
