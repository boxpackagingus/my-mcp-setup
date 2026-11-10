"""Shared pieces for the local SEO + AI search pages (batches 13-17).
Every fact here was checked at its source on 2026-11-10 (Google help/docs, schema.org, Wikipedia 2020 census)."""
from common import CORE, L, SRC, V, page
import batch8  # noqa: F401  (Pew, SparkToro and schema sources)
import batch9  # noqa: F401
import batch10  # noqa: F401
import batch11  # noqa: F401
import batch12  # noqa: F401
from batch8 import pew_clicks, pew_trigger, spark_bars  # noqa: F401

W = "https://en.wikipedia.org/wiki/"
SRC.update({
    "g_rank": {"title": "Google Business Profile Help: Tips to improve your local ranking on Google",
               "url": "https://support.google.com/business/answer/7091?hl=en"},
    "g_gbp": {"title": "Google Business Profile Help: Guidelines for representing your business on Google",
              "url": "https://support.google.com/business/answer/3038177?hl=en"},
    "g_fake": {"title": "Google Maps user contributed content policy: Fake engagement",
               "url": "https://support.google.com/contributionpolicy/answer/7400114?hl=en"},
    "w_irvine": {"title": "Wikipedia: Irvine, California", "url": W + "Irvine,_California"},
    "w_santaana": {"title": "Wikipedia: Santa Ana, California", "url": W + "Santa_Ana,_California"},
    "w_newport": {"title": "Wikipedia: Newport Beach, California", "url": W + "Newport_Beach,_California"},
    "w_hb": {"title": "Wikipedia: Huntington Beach, California", "url": W + "Huntington_Beach,_California"},
    "w_costamesa": {"title": "Wikipedia: Costa Mesa, California", "url": W + "Costa_Mesa,_California"},
    "w_fullerton": {"title": "Wikipedia: Fullerton, California", "url": W + "Fullerton,_California"},
    "w_orange": {"title": "Wikipedia: Orange, California", "url": W + "Orange,_California"},
    "w_gg": {"title": "Wikipedia: Garden Grove, California", "url": W + "Garden_Grove,_California"},
    "w_anaheim": {"title": "Wikipedia: Anaheim, California (2020 census figures)", "url": W + "Anaheim,_California"},
    "w_oc": {"title": "Wikipedia: Orange County, California (2020 census figures)", "url": W + "Orange_County,_California"},
})
for t in ["Plumber", "HVACBusiness", "RoofingContractor", "Electrician", "GeneralContractor", "HousePainter",
          "Locksmith", "MovingCompany", "AutoRepair", "AutoDealer", "InsuranceAgency", "AccountingService",
          "VeterinaryCare", "HealthClub", "BeautySalon", "ChildCare", "TravelAgency", "Physiotherapy",
          "MedicalBusiness", "Attorney", "RealEstateAgent", "FinancialService", "ProfessionalService",
          "LodgingBusiness", "Dentist", "DaySpa", "LocalBusiness", "HomeAndConstructionBusiness", "AutoBodyShop", "AutoWash", "AutomotiveBusiness", "EducationalOrganization", "SportsActivityLocation", "Optician", "MedicalClinic", "Store", "NGO", "School", "Physician", "Restaurant", "Hotel", "Dentist", "RealEstateAgent", "Attorney", "TravelAgency"]:
    SRC["s_" + t.lower()] = {"title": f"Schema.org: {t}", "url": f"https://schema.org/{t}"}

SVC, AUD, PROC = CORE["services"], CORE["audit"], CORE["process"]
LOCALGEO = L("local GEO", "local-geo")
OCAGENCY = L("GEO agency in Orange County", "geo-agency-orange-county")
SCHEMA_LOCAL = L("local business schema for AI search", "local-business-schema-for-ai-search")
CHATGPT_LOCAL = L("how ChatGPT recommends local businesses", "how-chatgpt-recommends-local-businesses")
HOME_SVC = L("GEO for home services", "geo-for-home-services")

# 2020 census populations, from each city's Wikipedia article.
CITY_POP = [("Anaheim", 346824), ("Santa Ana", 310227), ("Irvine", 307670), ("Huntington Beach", 198711),
            ("Garden Grove", 171949), ("Fullerton", 143617), ("Orange", 139911), ("Costa Mesa", 111918),
            ("Newport Beach", 85239)]


def oc_cities(after, title="Orange County's largest cities", lead=None, highlight=None):
    return {"after": after, "type": "bars", "eyebrow": "2020 census", "title": title,
            "lead": lead or "Residents by city, from the 2020 U.S. census. Orange County as a whole had 3,186,989.",
            "unit": "", "items": [{"label": c + (" (you are here)" if c == highlight else ""), "value": n, "display": f"{n:,}"}
                                  for c, n in CITY_POP],
            "source": {"title": "U.S. 2020 census, via each city's Wikipedia article", "url": SRC["w_oc"]["url"]}}


def local_rank_flow(after):
    return V.flow(after, "How Google ranks local results", "The factors Google names for local results.",
                  [("Relevance", "How well your profile matches the search."), ("Distance", "How far you are from the searcher."),
                   ("Popularity", "How well known you are: links and reviews count."), ("Result", "The local pack and Maps listing.")])


GOOGLE_RANK = ("<p>Google is unusually direct about local rankings. Its Business Profile help says local results are "
               "mainly based on relevance, distance and popularity. It describes prominence as how well-known a business is, "
               "based partly on how many websites link to it and how many reviews it has, and says more reviews and positive "
               "ratings can help. The same page adds that there is no way to request or pay for a better local ranking.</p>")

SAB_RULES = ("<p>Google's guidelines say service-area businesses, which serve customers at their locations, should have one "
             "profile for the central office or location with a designated service area. A rented mailing address you do not "
             "operate from, a virtual office, is not eligible, and P.O. boxes are not acceptable. Your business name should be "
             "your real-world name as used on your storefront, website and stationery, without extra keywords.</p>")

REVIEW_RULES = ("<p>Google's Maps content policy prohibits fake engagement: reviews must reflect a genuine experience, and "
                "businesses may not offer incentives, such as payment, discounts or free services, in exchange for a review or "
                "for removing a negative one. Ask every real customer, make it easy with a direct link, and reply to reviews.</p>")


# Three wordings of each shared explanation, rotated by page, so industry pages don't repeat each other.
RANK_V = [GOOGLE_RANK,
    ("<p>Google publishes the basics of how local results work. According to its Business Profile help, results are mainly "
     "based on relevance, distance and popularity. Prominence, in Google's words, is how well-known a business is, which "
     "draws on links from other websites and on reviews, and more reviews and positive ratings can help. Google also states "
     "plainly that nobody can request or pay for a better local ranking.</p>"),
    ("<p>Three things decide most local rankings, according to Google's own help pages: relevance, distance and popularity. "
     "Google explains prominence as how well-known a business is, reflected in things like how many websites link to it and "
     "how many reviews it has; more reviews and positive ratings can help. It is also clear that a better local ranking "
     "cannot be bought or requested.</p>")]
SAB_V = [SAB_RULES,
    ("<p>If you work at customers' homes, Google's guidelines treat you as a service-area business: one profile for your central "
     "office or location, with a service area set. Virtual offices, meaning rented addresses you do not work from, are not eligible, "
     "and neither are P.O. boxes. Use your real-world business name, the one on your signage and invoices, with no added keywords.</p>"),
    ("<p>Google's representation guidelines matter here. Businesses that travel to customers should keep a single profile for their "
     "central location and define a service area. An address you rent but do not operate from counts as a virtual office and is not "
     "eligible; P.O. boxes are not accepted either. Keep the business name exactly as customers know it, without stuffing in keywords.</p>")]
REVIEW_V = [REVIEW_RULES,
    ("<p>Stay inside Google's rules. Its Maps content policy bans fake engagement and says reviews must come from genuine experiences. "
     "Offering payment, discounts or free services for a review, or for removing a bad one, is not allowed. The safe method is simple: "
     "ask every real customer, send a direct review link and reply to what people write.</p>"),
    ("<p>Google removes reviews that break its fake engagement policy, including paid reviews and reviews given in exchange for discounts, "
     "free services or other incentives. Ask all of your real customers rather than a hand-picked few, make leaving a review take seconds, "
     "and respond to both praise and criticism.</p>")]
SCHEMA_V = [
    "Schema.org has a specific type for this business: <strong>{t}</strong>. Google's local business structured data documentation explains that markup can help it show details such as hours, address and price range. Add it to your homepage and location pages with your real name, address, phone, hours, service area and a sameAs list of your official profiles, and keep it identical to your Business Profile.",
    "Mark up your site with Schema.org's <strong>{t}</strong> type. Google's documentation on local business structured data notes it can help Google understand details like opening hours, address and price range. Include name, address, phone, hours, area served and links to your official profiles, and make every value match your Business Profile.",
    "Use structured data so machines read your facts correctly. The closest Schema.org type here is <strong>{t}</strong>. Google's local business documentation describes how this markup can surface details such as hours and price range. Keep name, address, phone and hours identical to your Business Profile, and list your official profiles with sameAs."]
DOORWAY_V = [
    "<p>Google's spam policies list pages targeted at specific cities that funnel visitors to one page, and substantially similar pages, as doorway abuse. Create a city page only when you have something specific to say about work there, such as local projects, permits or response times, and link it clearly from your main service pages.</p>",
    "<p>Be careful with city pages. Google's spam policies call pages aimed at specific regions or cities that funnel users to one page, and substantially similar pages, doorway abuse. A city page earns its place only with genuinely local detail, such as real projects, local rules or response times there.</p>",
    "<p>Resist the urge to clone a page for every city. Google's spam policies treat near-identical city pages that funnel visitors to one destination as doorway abuse. Show real local work instead, and only build a city page when there is something specific and useful to say.</p>"]


def industry(slot, d):
    """Industry page: SEO + AI search for one trade or profession in Anaheim and Orange County.
    d holds the industry-specific content; the shared text is kept short on purpose."""
    n, one = d["plural"], d["singular"]
    kw = d["kw"]
    secs = [
        (f"Why {n} in Orange County need both SEO and AI search",
         f"<p>{d['why']}</p><p>Orange County had 3,186,989 residents in the 2020 census, and Anaheim, the largest city, had 346,824. "
         f"For a {one} serving that market, the work now has two halves: ranking in Google's local results and being the name AI "
         f"assistants such as ChatGPT, Gemini and Google AI Overviews give when someone asks for a recommendation.</p>"),
        (f"What people search for before they call a {one}",
         "<p>These are the kinds of searches and AI questions that lead to a booked job. Write pages that answer them directly.</p><ul>"
         + "".join(f"<li><strong>{q}</strong> {a}</li>" for q, a in d["searches"]) + "</ul>"),
        (f"How Google ranks {n} in local results", RANK_V[slot % 3] + f"<p>{d['rank_note']}</p>"),
        (f"How AI assistants choose a {one}", f"<p>{d['ai_note']}</p>"),
        ("Test what AI says about you every month",
         "<p>Ask ChatGPT, Gemini, Perplexity and Google these questions from a phone in Orange County, then record which businesses "
         "are named, whether you appear, and whether the details about you are correct:</p><ol>"
         + "".join(f"<li>{q[:1].upper() + q[1:]}{'' if 'Orange County' in q or 'Anaheim' in q else ' in Anaheim'}?</li>" for q, _ in d["searches"][:5])
         + "</ol><p>Repeat the same questions each month. When you are missing or described wrongly, fix the page, listing or review gap "
           "behind it, then check again the following month.</p>"),
        ("Set up your Google Business Profile properly",
         f"<p>{d['gbp']}</p>" + SAB_V[slot % 3]),
        ("Build one page per service",
         "<p>Each main service deserves its own page that states what it is, who it is for, typical timing, what affects price and how to book.</p>"
         "<table><tr><th>Service page</th><th>What to include</th></tr>"
         + "".join(f"<tr><td>{s}</td><td>{w}</td></tr>" for s, w in d["services"]) + "</table>"),
        ("Cover your service area without doorway pages",
         f"<p>{d['area']}</p>" + DOORWAY_V[slot % 3]),
        ("Earn reviews that mention the details",
         "<p>Reviews that mention the job, the neighborhood and the outcome help both Google and AI assistants describe you. "
         "Topics worth asking customers to mention:</p><ul>" + "".join(f"<li>{t}</li>" for t in d["review_topics"]) + "</ul>" + REVIEW_V[slot % 3]),
        ("Show trust signals on every page", f"<p>{d['trust']}</p>"),
        ("Add structured data", "<p>" + SCHEMA_V[slot % 3].format(t=d["schema"]) + "</p>"),
        ("Content that brings in customers",
         "<ul>" + "".join(f"<li>{c}</li>" for c in d["content"]) + "</ul>"),
        ("Seasons and timing in Orange County", f"<p>{d['season']}</p>"),
        ("Mistakes that cost calls", "<ul>" + "".join(f"<li>{m}</li>" for m in d["mistakes"]) + "</ul>"),
        ("How to measure results",
         "<table><tr><th>What to track</th><th>Where</th></tr>"
         "<tr><td>Calls, direction requests and website clicks</td><td>Google Business Profile performance</td></tr>"
         f"<tr><td>Impressions and clicks for {d['short']} searches</td><td>Google Search Console</td></tr>"
         "<tr><td>Visits from ChatGPT, Perplexity, Gemini and Copilot</td><td>Google Analytics referrals</td></tr>"
         "<tr><td>Being named in AI answers</td><td>Ask the same 10 questions monthly and record the results</td></tr>"
         f"<tr><td>{d['kpi']}</td><td>Your CRM, booking or call-tracking system</td></tr></table>"),
        ("The short version",
         f"<p>{d['short_version']} Chimera, based in Anaheim, helps {n} across Orange County do this work.</p>"),
    ]
    faqs = d["faqs"] + [
        (f"How long does SEO take for {n}?", "Profile and on-page fixes can show up within weeks; new pages and reviews usually take a few months to move rankings and AI answers."),
        (f"Can a {one} show up in ChatGPT answers?", "Yes. AI assistants draw on websites, listings, reviews and other web sources, so clear service pages, consistent listings and genuine reviews make you easier to recommend."),
        (f"Do you work with {n} in Anaheim and Orange County?", f"Yes. Chimera is based in Anaheim, California and works with {n} across Orange County, California."),
    ]
    return page(d["slug"], d["query"], kw, d.get("eyebrow", "Local SEO"), d["title"], d["meta"], d["h1"], d["answer"],
                d["takeaways"], secs, faqs,
                d.get("links", []) + [LOCALGEO, CHATGPT_LOCAL, SCHEMA_LOCAL, OCAGENCY, AUD],
                ["g_rank", "g_gbp", "g_fake", "spam", "g_local", "s_" + d["schema"].lower(), "w_oc"],
                [local_rank_flow(2), oc_cities(6, lead=f"Where {n} in Orange County find their customers. County total: 3,186,989 (2020 census)."),
                 V.scorecard(9, f"What moves the needle for {n}", "Impact on calls from Google and AI (5 = most).", d["score"])],
                secondary=d["secondary"], hero_query=d["hero_query"], short_title=d["short_title"])
