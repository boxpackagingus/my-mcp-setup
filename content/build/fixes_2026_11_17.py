"""Fixes for 2026-11-17, chosen from data/opportunities.json (money queries, cannibalization, CTR).
Anaheim facts are from Wikipedia's Anaheim, California article (read 2026-11-17)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB, DRAFTS = ROOT / "content" / "published", ROOT / "content" / "drafts"
B = "https://thechimeraai.com"


def load(slug):
    return json.loads((PUB / f"{slug}.json").read_text())


def save(d):
    (DRAFTS / f"{d['slug']}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False))


def add_sec(d, heading, html, before_last=True):
    d["sections"].insert(len(d["sections"]) - 1 if before_last else len(d["sections"]), {"heading": heading, "body_html": html})


def add_kw(d, kws):
    d["secondary_keywords"] = list(dict.fromkeys(d.get("secondary_keywords", []) + kws))


def add_faq(d, q, a):
    d["faqs"] = d.get("faqs", []) + [{"question": q, "answer": a}] if d.get("faqs") and isinstance(d["faqs"][0], dict) else d.get("faqs", []) + [[q, a]]


def link_first(d, html):
    d["sections"][0]["body_html"] += html


FIXES = []

# 1. Anaheim page: more Anaheim-only substance so Google prefers it over the county page for "anaheim seo".
d = load("seo-company-anaheim")
add_sec(d, "Anaheim's business districts, and what each searches for",
        "<p>Anaheim is not one market. Wikipedia describes several distinct areas, and each produces different searches:</p><ul>"
        "<li><strong>The Anaheim Resort District:</strong> the Disneyland Resort, the Anaheim Convention Center, the Honda Center and Angel Stadium. "
        "Searches here are visitor searches: hotels, restaurants, parking and things to do, made on phones close to the visit.</li>"
        "<li><strong>The Platinum Triangle:</strong> the redevelopment district around Angel Stadium, planned for mixed-use streets and high-rises. "
        "New residents there search for everyday services as the area fills in.</li>"
        "<li><strong>Downtown and the Anaheim Colony:</strong> downtown has three mixed-use historic districts, the largest being the Anaheim Colony, "
        "plus attractions such as the Anaheim Packing House. Searches mix dining, events and local shops.</li>"
        "<li><strong>Anaheim Canyon:</strong> an industrial district north of the Riverside Freeway and east of the Orange Freeway, where buyers "
        "search for suppliers, manufacturers and B2B services.</li>"
        "<li><strong>Anaheim Hills:</strong> the city's eastern third, a master-planned community, where residents search for home, family and health services.</li></ul>"
        "<p>An Anaheim SEO plan should say which of these areas a business serves. Chimera is based in Anaheim and plans each client's pages, "
        "profile and reviews around the districts its customers actually come from.</p>")
add_kw(d, ["anaheim seo company", "anaheim seo agency", "seo anaheim ca", "anaheim search engine optimization"])
FIXES.append(d)

# 2. Huntington Beach: rising (40.7 -> 32.1); answer the new queries directly.
d = load("seo-huntington-beach")
add_sec(d, "Local SEO tips for Huntington Beach businesses",
        "<ol><li>Set your Business Profile category to exactly what you do, and add every service you offer.</li>"
        "<li>Keep seasonal hours current, especially around summer and major beach events.</li>"
        "<li>Name the areas you serve, such as downtown and Main Street or the neighborhoods inland, only where you genuinely work.</li>"
        "<li>Ask every customer for a review that mentions the job and Huntington Beach.</li>"
        "<li>Publish one clear page per service with prices or price ranges where possible.</li>"
        "<li>Check monthly what ChatGPT and Google's AI say when asked for your service in Huntington Beach.</li></ol>")
add_sec(d, "How AI search optimization works in Huntington Beach",
        "<p>AI search optimization means making sure AI assistants such as ChatGPT, Gemini, Perplexity and Google's AI Overviews can find, "
        "understand and trust information about your business. For a Huntington Beach business that means accurate, consistent details "
        "everywhere your business appears, a website with clear service pages and answers to common questions, structured data that "
        "states your name, address, services and hours, and genuine reviews that describe real jobs. Assistants then have something specific "
        "to cite when someone asks for a recommendation in Huntington Beach.</p>")
add_kw(d, ["local seo tips huntington beach", "ai search optimization huntington beach", "huntington beach seo company"])
FIXES.append(d)

# 3. GEO agency page owns "AI search optimization Orange County" (currently split across a blog post and other pages).
d = load("geo-agency-orange-county")
d["seo"]["title"] = "GEO Agency in Orange County | AI Search Optimization"
add_sec(d, "AI search optimization in Orange County",
        "<p>AI search optimization and generative engine optimization (GEO) describe the same work: helping a business get found, understood "
        "and recommended by ChatGPT, Gemini, Perplexity, Claude and Google's AI Overviews and AI Mode. For Orange County businesses that starts with "
        "the basics AI assistants rely on, a complete Google Business Profile, consistent listings, clear service pages and genuine reviews, then adds "
        "structured data, answer-style content and regular checks of what assistants say. Chimera does this from Anaheim for businesses across the county.</p>")
add_kw(d, ["ai search optimization orange county", "ai search orange county", "ai seo orange county", "geo agency newport beach"])
FIXES.append(d)

d = load("30-day-ai-search-plan-orange-county")
link_first(d, f'<p>Want this done for you? See our <a href="{B}/geo-agency-orange-county/">AI search optimization in Orange County</a> service.</p>')
d["secondary_keywords"] = [k for k in d.get("secondary_keywords", []) if "optimization orange county" not in k.lower()]
FIXES.append(d)

# 4. Fullerton: "local seo fullerton" at 43 with 13 impressions.
d = load("seo-fullerton")
add_sec(d, "Local SEO in Fullerton: where to start",
        "<p>For most Fullerton businesses, local SEO starts with three things. First, a complete Google Business Profile with the right category, "
        "services, hours and photos. Second, a website page for each service that names Fullerton and the nearby areas you serve, such as the "
        "neighborhoods around Cal State Fullerton or downtown. Third, a steady flow of genuine reviews. Businesses near the Anaheim border should "
        "describe their service area clearly so Google knows they serve both cities.</p>")
add_kw(d, ["local seo fullerton", "fullerton local seo", "seo company fullerton"])
FIXES.append(d)

# 5. Gyms: the personal trainers page ranks 6 for "seo for gyms orange county"; give the gyms page that query and link to it.
d = load("seo-for-gyms")
add_kw(d, ["seo for gyms orange county", "gym seo orange county", "fitness studio seo orange county"])
FIXES.append(d)
d = load("seo-for-personal-trainers")
link_first(d, f'<p>Running a full gym or studio rather than training independently? See <a href="{B}/seo-for-gyms/">SEO for gyms in Orange County</a>.</p>')
d["secondary_keywords"] = [k for k in d.get("secondary_keywords", []) if "gym" not in k.lower()]
FIXES.append(d)

# 6. Medical practices: doctors page is the stronger one for "medical practice seo orange county".
d = load("seo-for-doctors")
add_kw(d, ["medical practice seo orange county", "healthcare seo orange county"])
FIXES.append(d)
d = load("seo-for-dentists-orange-county")
link_first(d, f'<p>For physicians and multi-specialty clinics, see <a href="{B}/seo-for-doctors/">medical practice SEO in Orange County</a>.</p>')
FIXES.append(d)

# 7. Local SEO checklist ranks 53 for "local seo anaheim": point that query at the Anaheim page.
d = load("local-seo-checklist")
link_first(d, f'<p>Based in Anaheim and want help with these steps? See our <a href="{B}/seo-company-anaheim/">Anaheim SEO company</a> page.</p>')
FIXES.append(d)

# 8. Estate planning page: ranks 15.8 for "estate planning attorney seo company near me"; make that intent explicit.
d = load("seo-for-estate-planning-attorneys")
d["seo"]["meta_description"] = "SEO for estate planning attorneys in Anaheim and Orange County: an SEO company for trust and probate firms, with practice pages, reviews and AI search."
add_kw(d, ["estate planning attorney seo company", "estate planning law firm seo", "trust and probate attorney seo"])
FIXES.append(d)

# 9. Travel GEO page: position 7.7 with 15 impressions and no clicks; a title that states the benefit.
d = load("geo-for-travel-websites")
d["seo"]["title"] = "GEO for Travel Websites: Get Booked via AI Search"
FIXES.append(d)

if __name__ == "__main__":
    for d in FIXES:
        save(d)
    print(len(FIXES), "pages staged:", ", ".join(d["slug"] for d in FIXES))
