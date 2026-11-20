"""Fixes for 2026-11-18, chosen from data/opportunities.json (rising city pages, cannibalization, CTR).
City facts are from Wikipedia's Newport Beach, Santa Ana and Costa Mesa articles (read 2026-11-18)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB, DRAFTS = ROOT / "content" / "published", ROOT / "content" / "drafts"
B = "https://thechimeraai.com"


def load(slug):
    return json.loads((PUB / f"{slug}.json").read_text())


def save(d):
    (DRAFTS / f"{d['slug']}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False))


def add_sec(d, heading, html):
    d["sections"].insert(len(d["sections"]) - 1, {"heading": heading, "body_html": html})


def add_kw(d, kws):
    d["secondary_keywords"] = list(dict.fromkeys(d.get("secondary_keywords", []) + kws))


def link_first(d, html):
    d["sections"][0]["body_html"] += html


FIXES = []

# 1-3. Rising city pages: more city-only substance.
d = load("seo-newport-beach")
add_sec(d, "Newport Beach's business mix and what it means for search",
        "<p>Newport Beach had 85,239 residents in 2020 and is best known for its beaches, its recreational harbor and Balboa Island, where a "
        "waterfront path and the ferry bring visitors to shops and restaurants. It is also a business center: Wikipedia lists insurer Pacific Life, "
        "its one Fortune 500 company, along with PIMCO, Chipotle Mexican Grill and the Irvine Company among firms based here.</p>"
        "<p>That mix creates three kinds of search: visitors looking for dining, boating and things to do around the harbor and Balboa Island; "
        "residents looking for high-end home, health and professional services; and businesses looking for B2B partners. A Newport Beach SEO plan "
        "should say clearly which of these a business serves, with pages and reviews to match.</p>")
add_kw(d, ["seo newport beach", "newport beach seo services", "local seo services newport beach", "newport beach seo company"])
FIXES.append(d)

d = load("seo-santa-ana")
add_sec(d, "Santa Ana as the county seat and a business hub",
        "<p>Santa Ana is the county seat of Orange County and, with 310,227 residents in 2020, its third most populous city after Anaheim and Irvine. "
        "Wikipedia describes it as a major regional economic and cultural hub, and lists companies headquartered here including Behr Paint, "
        "First American Corporation, Ingram Micro and SchoolsFirst Federal Credit Union.</p>"
        "<p>As the county seat, Santa Ana draws people for government and legal business, which makes it important for law firms, accountants and "
        "other professional services. Pages that name Santa Ana and describe the specific services offered there, in English and Spanish where "
        "customers need it, help both Google and AI assistants match a business to local searches.</p>")
add_kw(d, ["seo santa ana", "santa ana seo company", "local seo santa ana", "attorney seo santa ana"])
FIXES.append(d)

d = load("seo-costa-mesa")
add_sec(d, "South Coast Plaza and the Costa Mesa retail market",
        "<p>Costa Mesa grew from a farming community of 16,840 at incorporation in 1953 to 111,918 residents in 2020, and includes part of the "
        "South Coast Plaza and John Wayne Airport edge city. Wikipedia notes that South Coast Plaza, with more than 270 stores, generates more than "
        "$1 billion a year in sales, placing it among the highest-volume regional shopping centers in the nation.</p>"
        "<p>For retailers and restaurants nearby, that means intense competition for shoppers who decide on their phones. Accurate product data on "
        "Google, current hours, menus and photos, and steady reviews are what separate businesses in local results and in AI shopping answers.</p>")
add_kw(d, ["seo costa mesa ca", "costa mesa seo", "costa mesa seo company"])
FIXES.append(d)

# 4. Brake searches land on the auto repair page; point them at the brake page.
d = load("seo-for-auto-repair-shops")
link_first(d, f'<p>Specializing in brakes? See <a href="{B}/seo-for-brake-shops/">brake repair shop SEO</a>.</p>')
d["secondary_keywords"] = [k for k in d.get("secondary_keywords", []) if "brake" not in k.lower()]
FIXES.append(d)
d = load("seo-for-brake-shops")
add_kw(d, ["brake repair shop seo", "brake shop marketing", "brake repair seo orange county"])
FIXES.append(d)

# 5. Security page ranks 2 for alarm monitoring: make it explicit.
d = load("seo-for-security-companies")
add_sec(d, "SEO for alarm and monitoring companies",
        "<p>Alarm installation and monitoring companies face different searches from guard services. Homeowners and businesses search for alarm "
        "installation, monitoring plans, cameras and smart locks, often comparing monthly costs and contract terms. Give each service its own page: "
        "installation, monitoring, cameras, access control and commercial systems, with clear explanations of what monitoring includes, response "
        "procedures, contract length and any licensing you hold. Reviews that mention installation quality and response help customers choose, "
        "and specific pages give AI assistants something concrete to cite.</p>")
add_kw(d, ["seo for alarm and monitoring companies", "alarm company seo", "security system installer seo"])
FIXES.append(d)

# 6. Checklist ranks 14 for Huntington Beach tips: send that query to the Huntington Beach page.
d = load("local-seo-checklist")
link_first(d, f'<p>In Huntington Beach? See our <a href="{B}/seo-huntington-beach/">local SEO tips for Huntington Beach businesses</a>.</p>')
FIXES.append(d)

# 7. Travel GEO page: still no clicks at 7.1; sharper meta description.
d = load("geo-for-travel-websites")
d["seo"]["meta_description"] = "GEO for travel websites: how hotels, tour operators and agencies get recommended when travelers plan trips with ChatGPT, Gemini and Google AI Mode."
FIXES.append(d)

# 8. Law firm page: Santa Ana is the county seat, and Santa Ana law-firm searches land here.
d = load("seo-for-law-firms-orange-county")
add_sec(d, "Law firm SEO in Santa Ana",
        "<p>Santa Ana is Orange County's county seat, so many residents search for attorneys there. Firms with Santa Ana offices should say so "
        f"clearly on their practice pages and Business Profile, and can see our <a href=\"{B}/seo-santa-ana/\">Santa Ana SEO</a> page for city-specific "
        "advice. Firms serving the whole county should describe the cities they cover rather than creating near-identical pages for each.</p>")
add_kw(d, ["law firm seo company santa ana", "attorney seo santa ana"])
FIXES.append(d)

# 9. City pages that are new get a link from the county page.
d = load("seo-company-orange-county")
link_first(d, f'<p>Looking for your city? See our pages for <a href="{B}/seo-garden-grove/">Garden Grove</a>, <a href="{B}/seo-tustin/">Tustin</a>, '
              f'<a href="{B}/seo-mission-viejo/">Mission Viejo</a>, <a href="{B}/seo-laguna-beach/">Laguna Beach</a> and other Orange County cities.</p>')
FIXES.append(d)

if __name__ == "__main__":
    for d in FIXES:
        save(d)
    print(len(FIXES), "pages staged:", ", ".join(d["slug"] for d in FIXES))
