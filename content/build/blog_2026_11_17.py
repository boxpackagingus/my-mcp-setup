"""Blog posts for 2026-11-17 (5 posts). Every fact is checked at the linked source on 2026-11-17."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_16  # noqa: F401  (SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SRC.update({
    "g_askmaps_holiday": {"title": "Google: New Ask Maps features to help with holiday travel and prep (Nov 16, 2026)",
                          "url": "https://blog.google/products-and-platforms/products/maps/ask-maps-holiday-travel-features-2026/"},
    "g_maps_holiday_trends": {"title": "Google: Navigate holiday traffic and crowds with Google Maps trends (Nov 16, 2026)",
                              "url": "https://blog.google/products-and-platforms/products/maps/holiday-thanksgiving-travel-trends-2026/"},
    "g_bfcm_2026": {"title": "Google: How to find the best Black Friday deals and shop smarter (Nov 16, 2026)",
                    "url": "https://blog.google/products-and-platforms/products/shopping/black-friday-cyber-monday-shopping-tips-2026/"},
    "g_sa_api": {"title": "Google Search Central blog: Search Analytics API update (Nov 16, 2026)",
                 "url": "https://developers.google.com/search/blog/2026/11/search-analytics-api-update"},
    "g_gtig_q4": {"title": "Google: The era of autonomous attacks has arrived (GTIG, Nov 16, 2026)",
                  "url": "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gtig-ai-threat-tracker-q4-2026/"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")
GBP = L("Google Business Profile optimization", "google-business-profile-optimization-orange-county")
ASKMAPS = L("Ask Maps food ordering", "ask-maps-food-ordering-restaurants")
KBYG = L("Google Maps know before you go tips", "google-maps-know-before-you-go-restaurants")
FREE = L("Google free product listings", "google-free-product-listings")
LIA = L("local inventory ads and free local listings", "google-local-inventory-ads")
HOLIDAY_MC = L("holiday Merchant Center checklist", "holiday-merchant-center-checklist")
CART = L("Google's universal cart for retailers", "google-universal-cart-orange-county-retailers")
GSC_PERF = L("Search Console Performance report", "google-search-console-performance-report")
MULTI = L("Search Console multimodal report", "search-console-multimodal-search-report")
SECISSUES = L("Search Console security issues", "google-search-console-security-issues")
BACK = L("back button hijacking", "back-button-hijacking-spam-policy")
SALONS = L("SEO for salons", "seo-for-salons")
AUTO = L("SEO for auto repair shops", "seo-for-auto-repair-shops")


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def p(*xs):
    return "".join(f"<p>{x}</p>" for x in xs)


PAGES = [
# 1 ------------------------------------------------------------------
blog(1, "Google news",
     slug="ask-maps-books-local-appointments", query="ask maps appointments", kw="Ask Maps appointments",
     eyebrow="Google Maps", short_title="Ask Maps can now find and book local appointments",
     title="Ask Maps Appointments: What Local Businesses Need",
     meta="Ask Maps appointments let people find open beauty, pet care, auto and home repair slots, and Maps can call businesses. What Orange County owners should do.",
     h1="Ask Maps Appointments: Google Maps Can Now Find Open Slots and Call Local Businesses",
     answer="Ask Maps appointments are a new Google Maps feature, launched November 16, 2026, that finds open beauty, pet care, auto and home repair appointments online and can call local businesses for the customer. It is launching first in the U.S. Anaheim and Orange County businesses in those categories should make sure their booking links, hours and phone details are accurate.",
     takeaways=["Announced November 16, 2026.", "Covers beauty, pet care, auto and home repair appointments.", "Ask Maps can call local businesses for customers.",
                "Finding appointments launches first in the U.S.", "Accurate booking links, hours and phones decide who gets the booking."],
     sections=[
      ("What Google announced", p("On November 16, 2026, Google launched new Ask Maps features for the holidays. Among them, Google says Ask Maps can now find beauty, pet care, auto and home repair appointments online and call local businesses for you, using what it calls new agentic capabilities.")),
      ("How it works for customers", p("Google's example is simple: a person asks for a 4 p.m. nail appointment nearby, and Ask Maps shows open slots across nearby businesses so it is easy to decide what to book.")),
      ("Where it is available", p("Google says finding appointments, along with route tips, is launching first in the U.S., with more regions coming. Ask Maps itself is expanding to 30 countries in Europe, reaching more than 200 countries and territories.")),
      ("Why this matters for local businesses", p("Until now, a customer usually searched, compared a few profiles and then called or booked. Ask Maps now does part of that work for them, so the businesses it can check, because their availability and contact details are clear, are the ones that get considered.")),
      ("Which Orange County businesses it affects first", ul(["Nail, hair, lash and beauty salons.", "Groomers, pet sitters and other pet care.", "Auto repair, tires and detailing.", "Home repair trades such as plumbing, electrical and handyman services."])),
      ("Check your booking link", p("If you take appointments online, make sure your Google Business Profile links to the booking page you actually use, and that it shows real availability. A dead link or a page that only says call us gives Maps nothing to show.")),
      ("Check your phone and hours", p("Because Ask Maps can call local businesses for customers, a phone number that goes to a full voicemail, or hours that are wrong, can lose the booking. Update holiday hours early and make sure calls are answered or returned quickly.")),
      ("Make services clear", p("List each service you offer on your profile and website in plain words, such as gel manicure, dog grooming for large breeds or brake inspection. A customer asks for a specific service, and Maps can only match it if you name it.")),
      ("Reviews still matter", p("When several businesses have open slots, customers still choose by rating and reviews. Steady, genuine reviews that mention the service help you win the choice.")),
      ("What to do this week", ol(["Check the booking link on your Business Profile.", "Confirm hours, including Thanksgiving and December.", "List every service by name.", "Answer calls or set up quick callbacks.", "Ask recent customers for reviews."])),
      ("A worked example", p("Imagine a nail salon in Fullerton whose profile links to an old booking app. The owner switches the link to the current booking page, lists each service with prices, adds holiday hours and asks for reviews after each visit. When someone nearby asks Ask Maps for a 4 p.m. appointment, the salon's open slots can now be shown.")),
      ("Questions owners ask us", p("Owners often ask whether they need a special integration. Google's post doesn't describe one for businesses, so start with what you control: an accurate profile, a working booking link and answered phones. Another common question is whether this replaces their booking software. It doesn't; it sends customers to the systems and phones you already use. Owners also ask whether small, one-chair businesses benefit. They can, because Ask Maps compares nearby availability, not just size.")),
      ("Keep Apple Maps and your website consistent", p("Customers also use Apple Maps and your website. Keep hours, phone and booking links the same everywhere, so any assistant or app that checks your details finds the same answer. Inconsistent details make it harder for any of them to recommend you with confidence.")),
      ("Prepare staff for AI-assisted calls", p("If Ask Maps calls on a customer's behalf, the call may be short and specific: a service, a time and a name. Brief whoever answers the phone to confirm availability clearly and take the booking the same way they would for any caller, so the appointment is not lost to confusion.")),
      ("Track where bookings come from", p("Add a question at booking, such as how did you find us, or use your booking software's source reports, and watch for growth from Google Maps over the holiday season. This tells you whether the effort on your profile is paying off.")),
      ("The short version", p("Ask Maps can now find appointments and call local businesses in the U.S. Anaheim and Orange County salons, pet care, auto and home repair businesses should check booking links, hours, phones, service names and reviews now, before the holiday rush."))],
     faqs=[("What are Ask Maps appointments?", "A Google Maps feature that finds open beauty, pet care, auto and home repair appointments and can call businesses for customers."),
           ("When did Google announce it?", "November 16, 2026."),
           ("Is it available in the U.S.?", "Yes. Google says finding appointments launches first in the U.S."),
           ("Which businesses are covered?", "Google names beauty, pet care, auto and home repair."),
           ("What should businesses do first?", "Check booking links, hours, phone and service names on their Google Business Profile."),
           ("Does it replace booking software?", "No. It sends customers to the booking pages and phones businesses already use."),
           LOCAL_FAQ],
     links=[GBP, ASKMAPS, KBYG, SALONS, AUTO, LOCAL],
     sources=["g_askmaps_holiday"],
     visuals=[V.flow(4, "How Ask Maps finds an appointment", "From Google's November 16, 2026 post.",
               [("Ask", "\"Find me a 4 p.m. nail appointment near me.\""), ("Check", "Open slots at nearby businesses."),
                ("Call", "Maps can call businesses for you."), ("Book", "The customer picks a slot.")])],
     secondary=["Ask Maps booking", "Google Maps book appointment", "Ask Maps agentic", "Google Maps call business for me"],
     hero_query="Can Google Maps book an appointment for me?"),

# 2 ------------------------------------------------------------------
blog(2, "Playbooks",
     slug="holiday-crowd-times-google-maps", query="holiday crowd times google maps", kw="holiday crowd times",
     eyebrow="Google Maps", short_title="Holiday crowd times from Google Maps trends",
     title="Holiday Crowd Times From Google Maps Trends",
     meta="Holiday crowd times from Google Maps trends show when grocery stores, bakeries and roads peak around Thanksgiving. How Orange County businesses can plan.",
     h1="Holiday Crowd Times: What Google Maps Trends Mean for Local Businesses",
     answer="Holiday crowd times from Google Maps trends show when roads, grocery stores, bakeries and movie theaters are busiest around Thanksgiving. Google says grocery crowds peak around 2 p.m. the Saturday and Sunday before Thanksgiving and bakeries around 11 a.m. that Saturday. Anaheim and Orange County businesses can use these patterns to plan staffing, hours and promotions.",
     takeaways=["Published by Google on November 16, 2026.", "Grocery crowds peak around 2 p.m. the weekend before Thanksgiving.", "Bakeries peak around 11 a.m. the Saturday before.",
                "Black Friday driving is heaviest 11 a.m. to 3 p.m.", "Use quieter times to promote and staff smarter."],
     sections=[
      ("What Google shared", p("On November 16, 2026, Google published holiday traffic and crowd trends from Google Maps: when to drive, when to run errands and which destinations see spikes in interest. These are national patterns, but they are a useful starting point for local planning.")),
      ("When stores and venues are busiest",
       "<table><tr><th>Place</th><th>Busiest</th><th>Quieter</th></tr>"
       "<tr><td>Grocery stores</td><td>About 2 p.m. Saturday and Sunday before Thanksgiving</td><td>Before 4 p.m. Monday to Wednesday</td></tr>"
       "<tr><td>Bakeries</td><td>11 a.m. Saturday before Thanksgiving</td><td>Before noon Monday to Wednesday</td></tr>"
       "<tr><td>Movie theaters</td><td>Around 7 p.m. on the Saturdays before and after Thanksgiving</td><td>Before 5 p.m. on Black Friday</td></tr></table>"
       "<p>Source: Google Maps trends, as published by Google on November 16, 2026.</p>"),
      ("When roads are busiest",
       "<table><tr><th>Trip</th><th>Avoid</th><th>Better</th></tr>"
       "<tr><td>Long-distance, Wednesday</td><td>Noon to 3 p.m.</td><td>Before 9 a.m. or after 6 p.m.</td></tr>"
       "<tr><td>Long-distance, Tuesday</td><td>3 p.m. to 5 p.m.</td><td>Before 1 p.m. or after 6 p.m.</td></tr>"
       "<tr><td>Thanksgiving Day</td><td>Before dinner rush</td><td>Roads generally quiet, especially after noon</td></tr>"
       "<tr><td>Black Friday</td><td>11 a.m. to 3 p.m.</td><td>Outside those hours</td></tr>"
       "<tr><td>Return, Sunday</td><td>Noon to 3 p.m.</td><td>Before noon or after 3 p.m.</td></tr></table>"
       "<p>Google also flags the Friday before Thanksgiving, with traffic peaking between 3 p.m. and 5 p.m.</p>"),
      ("What this means for local businesses", p("Customers who read the same advice will try to shop at quieter times. A bakery in Orange County can expect pre-orders and early-week visits, while a grocery store can expect weekend peaks. Planning around these patterns helps you staff well and keep wait times down.")),
      ("Staffing", p("Put more people on at the times Google says are busiest for your kind of business, and use the quieter windows for prep, restocking and pickups. Customers notice short waits during the busiest week of the year.")),
      ("Hours and Business Profile updates", p("If you open early, close late or close for Thanksgiving, update your Google Business Profile's special hours now. Customers who plan around crowd times will check your hours first, and Ask Maps can now show whether a place is open on a route.")),
      ("Promotions for quieter times", p("Encourage customers into your quieter windows with a reason to come: early-week pickup for pies, a weekday holiday menu or a Black Friday morning event before the driving peak. A Business Profile post is a simple way to announce it.")),
      ("Pre-orders and pickup", p("Bakeries, caterers and specialty food shops can take pressure off the peak by pushing pre-orders with set pickup windows. Put the order deadline and pickup times on your website and profile, in plain words.")),
      ("Orange County timing", p("For Anaheim and Orange County, holiday traffic also gathers around the major shopping and entertainment areas. If customers have to drive to you, mention parking and the easiest arrival times on your website, and keep those details current.")),
      ("A simple holiday plan", ol(["Update special hours on Google and Apple Maps.", "Staff up for your busiest times.", "Promote quieter times with a clear offer.", "Set pre-order deadlines and pickup windows.", "Reply quickly to messages and reviews."])),
      ("A worked example", p("Imagine a bakery in Tustin that usually gets swamped on the Saturday before Thanksgiving. It opens pie pre-orders with Monday to Wednesday morning pickup, posts the deadline on its Business Profile, and adds extra staff on Saturday at 11 a.m. The line is shorter, and more orders are ready on time.")),
      ("Questions owners ask us", p("Owners often ask whether national trends apply locally. They are a guide; your own sales and foot traffic are the best evidence, so compare them with Google's patterns. Another common question is whether to close on Thanksgiving. That's a business decision; what matters is that your profile shows it correctly. Owners also ask how far ahead to update hours. Do it now, since customers start planning a week or more ahead.")),
      ("Use your own data too", p("Your Google Business Profile insights show when people search for you and request directions, and your sales system shows when people buy. Put last year's holiday numbers next to Google's patterns to decide where to add staff or offers.")),
      ("After the holidays", p("Write down what worked: which hours were busiest, which offers moved people to quieter times and how wait times felt. Next year, start your plan from those notes rather than from scratch.")),
      ("The short version", p("Google Maps trends show when holiday crowds and traffic peak. Anaheim and Orange County businesses can staff for the peaks, update hours, promote quieter times and push pre-orders to keep the busiest week running smoothly."))],
     faqs=[("When are grocery stores busiest before Thanksgiving?", "Google says around 2 p.m. on the Saturday and Sunday before."),
           ("When are bakeries busiest?", "Around 11 a.m. on the Saturday before Thanksgiving, according to Google."),
           ("When is Black Friday driving heaviest?", "Between 11 a.m. and 3 p.m., Google says."),
           ("Should I update holiday hours on Google?", "Yes, as early as possible, using special hours on your Business Profile."),
           ("Do national trends apply to Orange County?", "They are a guide; compare them with your own sales and foot traffic."),
           ("How can I move customers to quieter times?", "Offer a reason, such as early-week pickup or a weekday offer, and post it on your profile."),
           LOCAL_FAQ],
     links=[GBP, KBYG, ASKMAPS, HOLIDAY_MC, LOCAL],
     sources=["g_maps_holiday_trends"],
     visuals=[V.flow(3, "Planning around holiday crowds", "Based on Google Maps trends.",
               [("Peaks", "Know your busiest times."), ("Staff", "Add people at peaks."),
                ("Shift", "Promote quieter windows."), ("Update", "Special hours everywhere.")])],
     secondary=["Thanksgiving busy times", "Google Maps popular times holidays", "holiday staffing small business", "Black Friday traffic times"],
     hero_query="When are stores busiest before Thanksgiving?"),

# 3 ------------------------------------------------------------------
blog(3, "AI Shopping",
     slug="black-friday-google-shopping-tools-retailers", query="black friday google shopping tools", kw="Black Friday Google shopping tools",
     eyebrow="Google Shopping", short_title="Black Friday shopping tools and what retailers should do",
     title="Black Friday Google Shopping Tools for Retailers",
     meta="Black Friday Google shopping tools: Universal Cart alerts, Price Insights, AI Mode gift ideas and Lens in stores. What Orange County retailers should do.",
     h1="Black Friday Google Shopping Tools: How Shoppers Will Find and Compare Your Products",
     answer="Black Friday Google shopping tools include Universal Cart price-drop and restock alerts, Price Insights that show whether a price is low, typical or high, gift ideas in AI Mode and the Gemini app, and Google Lens for products seen in stores. Anaheim and Orange County retailers should make sure their prices, availability and product details on Google are accurate and competitive.",
     takeaways=["Google shared four shopping tools on November 16, 2026.", "Universal Cart alerts shoppers to price drops and restocks.", "Price Insights shows if a price is low, typical or high.",
                "AI Mode suggests gifts with store availability.", "Lens connects in-store products to reviews and details."],
     sections=[
      ("What Google shared", p("On November 16, 2026, Google published four ways shoppers can use its tools for Black Friday and Cyber Monday: Universal Cart, gift ideas in Search and the Gemini app, Price Insights, and Google Lens in stores.")),
      ("Universal Cart", p("Google says shoppers can add items from different retailers to Universal Cart, which notifies them of price drops or when out-of-stock items return, shows merchant promo codes and offers, and lets them check out with Google Pay or move items to the retailer's site.")),
      ("Gift ideas in AI Mode and Gemini", p("Shoppers can describe a person in everyday language, such as useful gifts under $40 for an uncle training for his first half marathon, and get tailored ideas with customer reviews, photos and store availability, according to Google.")),
      ("Price Insights", p("Google says tapping a product listing lets shoppers compare prices across merchants and see price history showing whether a price is low, typical or high, and track the price for a drop.")),
      ("Google Lens in stores", p("Shoppers can photograph an item on a store shelf with Lens to see reviews, product details and similar styles, and ask follow-up questions such as whether it comes in another color.")),
      ("What it means for retailers", p("Shoppers can now compare your price against others in one tap and get alerted when you discount. That rewards accurate prices, honest promotions and clear availability, and it makes product data on Google a direct sales channel.")),
      ("Keep prices accurate", p("If your Black Friday price on your website differs from your product data on Google, shoppers see the wrong number, and Google may disapprove the product. Update product data whenever prices change during the sale.")),
      ("Show store availability", p("Because AI Mode gift ideas include store availability, retailers with in-store stock on Google through free local listings can appear for shoppers who want to buy nearby today.")),
      ("Make products easy to recognize", p("Lens matches what shoppers photograph. Clear product titles with brand and model, real product images and accurate GTINs help Google connect a shelf item to your listing.")),
      ("Use real promotions", p("Promotions submitted in Merchant Center can show with your products, and Universal Cart surfaces promo codes. Make sure every code works at checkout before the sale starts.")),
      ("A Black Friday checklist", ol(["Check prices and availability match your site.", "Turn on free listings and local inventory.", "Fix product titles, images and GTINs.", "Submit real promotions early.", "Update holiday hours for the store."])),
      ("A worked example", p("Imagine a running shop in Irvine. Before Black Friday, it updates sale prices in its product feed, adds in-store stock to Google, rewrites titles with brand, model and size, and submits a promotion for its shoe sale. Shoppers searching for running gifts in AI Mode see the shop's shoes in stock nearby, at a price Price Insights marks as low.")),
      ("Questions retailers ask us", p("Retailers often ask whether they must be in Universal Cart. Shoppers add products themselves; what retailers control is accurate product data on Google. Another common question is whether Price Insights hurts small shops. It rewards fair prices, and small shops can still win on availability today and service. Retailers also ask what to fix first. Prices and availability, since mismatches can get products disapproved during the busiest week.")),
      ("Small shops can still win", p("Big retailers have more products, but small shops often win on availability today, advice and local pickup. Make those clear in your product data, store details and Business Profile, so AI-assisted shoppers see them.")),
      ("After Black Friday", p("Keep product data accurate through Cyber Monday and December, switch prices back when the sale ends, and remove expired promotions so shoppers are not disappointed.")),
      ("The short version", p("Google's Black Friday tools let shoppers track prices, compare deals, get gift ideas and look up products in stores. Anaheim and Orange County retailers win by keeping prices, stock and product details on Google accurate and their promotions genuine."))],
     faqs=[("What Black Friday tools did Google highlight?", "Universal Cart, gift ideas in AI Mode and Gemini, Price Insights and Google Lens."),
           ("What does Price Insights show?", "Price comparisons across merchants and whether a price is low, typical or high."),
           ("Does Universal Cart alert shoppers to discounts?", "Yes. Google says it notifies them about price drops and restocks."),
           ("Do AI Mode gift ideas show store availability?", "Yes, according to Google."),
           ("What should retailers fix first?", "Prices and availability that match their website."),
           ("Can small shops compete?", "Yes, with accurate data, in-store availability and service."),
           LOCAL_FAQ],
     links=[HOLIDAY_MC, CART, FREE, LIA, LOCAL],
     sources=["g_bfcm_2026", "mc_issues", "mc_promo"],
     visuals=[V.flow(3, "How shoppers find Black Friday deals", "From Google's November 16, 2026 post.",
               [("Ideas", "Gift ideas in AI Mode."), ("Compare", "Price Insights."),
                ("Track", "Universal Cart alerts."), ("In store", "Lens on the shelf.")])],
     secondary=["Google Price Insights", "Universal Cart Black Friday", "Google Lens shopping", "Black Friday retailer checklist"],
     hero_query="How will shoppers compare my Black Friday prices on Google?"),

# 4 ------------------------------------------------------------------
blog(4, "Google news",
     slug="search-analytics-api-branded-queries", query="search analytics api branded queries", kw="Search Analytics API branded queries",
     eyebrow="Search Console", short_title="Search Analytics API adds branded queries and multimodal data",
     title="Search Analytics API: Branded Queries and More",
     meta="The Search Analytics API now supports branded queries, web multimodal data and multi-country filters. What Orange County businesses and agencies can do with it.",
     h1="Search Analytics API Update: Branded Queries, Multimodal Data and Multi-Country Filters",
     answer="The Search Analytics API, which feeds Search Console data to dashboards and tools, added three options on November 16, 2026: a branded queries classification to separate branded from non-branded searches, a web multimodal type for Lens and Circle to Search traffic, and filter lists for several countries or devices in one request. Anaheim and Orange County businesses can track non-brand growth more easily.",
     takeaways=["Announced November 16, 2026.", "Branded vs non-branded queries are now in the API.", "Web multimodal covers Google Lens, Circle to Search and image uploads.",
                "Filter several countries or devices in one request.", "Branded data is only for eligible properties."],
     sections=[
      ("What Google announced", p("On November 16, 2026, Google's Search Console team brought three features from the Performance report to the Search Analytics API: the branded queries filter, web multimodal reporting, and multi-country and multi-device filtering.")),
      ("Branded queries", p("Google says you can group or filter data by brandedClassification to compare branded and non-branded performance. As in Search Console, the data is only available for eligible properties; for others, the response returns no rows.")),
      ("Web multimodal", p("Setting the type to webMultimodal returns performance data from Google Lens, Circle to Search on Android and image uploads in Google Search, according to Google. It is also available in BigQuery for properties with an active bulk data export.")),
      ("Multi-country and multi-device filters", p("A new filterLists field lets you filter by several countries or devices in a single request, instead of making separate requests and combining them.")),
      ("Why branded vs non-branded matters", p("Branded searches, people typing your business name, show reputation. Non-branded searches, such as plumber in Anaheim, show whether SEO is bringing new customers who didn't know you. Separating them is the clearest way to see if SEO is working.")),
      ("What this means for small businesses", p("You don't need the API to see branded queries; eligible properties have the filter in Search Console's Performance report. The API matters if you use a dashboard or agency report, which can now separate brand from non-brand automatically.")),
      ("What this means for agencies and dashboards", p("Agencies can now report non-brand growth for clients without maintaining long lists of brand-name variations, and can include Lens and Circle to Search performance alongside regular search results.")),
      ("Multimodal search for local businesses", p("Lens and Circle to Search let people search with a photo. For retailers, restaurants and anyone whose products or storefront are photographed, multimodal data shows how often those searches lead to your pages.")),
      ("How to start", ol(["Open Search Console's Performance report.", "Check whether the branded queries filter is available for your property.", "Compare branded and non-branded clicks month to month.",
                           "Look at the multimodal search report if you sell products.", "Ask your agency or dashboard provider to add the new API fields."])),
      ("A worked example", p("Imagine an Orange County law firm whose monthly report shows clicks rising. Splitting branded from non-branded shows most of the growth came from people searching the firm's name after a radio ad, while non-branded searches like attorney Santa Ana stayed flat. The firm shifts effort to practice area pages to grow non-brand searches.")),
      ("Questions owners ask us", p("Owners often ask which number to watch. Non-branded clicks, because they show new customers finding you through SEO. Another common question is why branded data is missing. Google says it's only available for eligible properties. Owners also ask whether multimodal matters for service businesses. Less than for retailers, but photos of storefronts, vehicles and equipment can still lead to searches.")),
      ("Keep reporting simple", p("For most small businesses, three numbers a month are enough: non-branded clicks, branded clicks and calls or bookings from search. The API update makes the first two easier to separate automatically.")),
      ("Data limits to remember", p("Search Console data is sampled and filtered for privacy, and recent days can change as data is finalized. Compare full months rather than single days, and treat small numbers as directional.")),
      ("Connect it to leads", p("Clicks are only part of the story. Link Search Console with Google Analytics and track form submissions and calls, so you can see whether non-brand visitors become customers.")),
      ("The short version", p("The Search Analytics API now separates branded and non-branded queries, includes Lens and Circle to Search data, and filters several countries or devices at once. Anaheim and Orange County businesses should watch non-branded growth, and ask their agency to use the new fields."))],
     faqs=[("What changed in the Search Analytics API?", "It added branded queries, web multimodal data and multi-country and multi-device filters."),
           ("When was it announced?", "November 16, 2026."),
           ("What is web multimodal?", "Performance from Google Lens, Circle to Search on Android and image uploads in Google Search."),
           ("Is branded data available for every site?", "No. Google says it's only for eligible properties."),
           ("Do I need the API?", "Not to see the data in Search Console; the API helps dashboards and agencies automate reports."),
           ("Which number should I watch?", "Non-branded clicks, which show new customers finding you."),
           LOCAL_FAQ],
     links=[GSC_PERF, MULTI, LOCAL, AUD],
     sources=["g_sa_api"],
     visuals=[V.flow(3, "What the API adds", "From Google's November 16, 2026 post.",
               [("Branded", "Brand vs non-brand."), ("Multimodal", "Lens and Circle to Search."),
                ("Filters", "Many countries or devices."), ("Report", "Automated dashboards.")])],
     secondary=["Search Console branded queries", "brandedClassification", "webMultimodal Search Console", "Search Console API filterLists"],
     hero_query="How do I see non-branded searches in Search Console?"),

# 5 ------------------------------------------------------------------
blog(5, "Playbooks",
     slug="ai-autonomous-attacks-small-business-websites", query="autonomous ai attacks small business", kw="autonomous AI attacks",
     eyebrow="Website security", short_title="Autonomous AI attacks and small business websites",
     title="Autonomous AI Attacks: Protect Your Website",
     meta="Google says autonomous AI attacks now scan software updates and build exploits without humans. How Orange County small businesses can keep websites safe.",
     h1="Autonomous AI Attacks: Why Small Business Websites Must Update Faster",
     answer="Autonomous AI attacks, as described by Google's Threat Intelligence Group on November 16, 2026, use AI frameworks to continuously scan software updates, work out what flaw was patched and build an attack for it without human involvement. For Anaheim and Orange County small businesses, the practical lesson is to apply website, plugin and theme updates quickly and remove software you don't use.",
     takeaways=["Google's threat group published this on November 16, 2026.", "Attackers use AI to study software patches automatically.", "The gap between a patch and an attack is shrinking.",
                "Updating promptly is the most important defense.", "Remove unused plugins and themes."],
     sections=[
      ("What Google reported", p("On November 16, 2026, the Google Threat Intelligence Group (GTIG) said, citing its latest AI Threat Tracker report, that bad actors now use autonomous large language model frameworks to continuously scan software updates, figure out what flaw was patched and build an attack for it, all without human involvement.")),
      ("What that means in plain words", p("When a software maker releases a security fix, the fix itself reveals where the weakness was. Attackers have always studied patches; Google's report says AI now lets them do it continuously and automatically. A website that delays updates stays exposed while attacks are being built.")),
      ("Google's own conclusion", p("Google says defending against machine-speed threats at human speed isn't feasible, and describes its own response for organizations, Google AI Threat Defense. Small businesses don't need enterprise tools to act on the same lesson: shorten the time between an update and installing it.")),
      ("Why small business websites are exposed", p("Many small business sites run on WordPress or similar systems with plugins and themes from many developers, often updated only when someone remembers. Each outdated component is a known weakness once its fix is public.")),
      ("Turn on automatic updates where safe", p("Most website platforms can apply security and minor updates automatically. Turn this on for the core software and for well-maintained plugins, and check after updates that key pages and forms still work.")),
      ("Remove what you don't use", p("Every inactive plugin, unused theme and old test page is something to keep updated. Deleting them, not just deactivating them, reduces what attackers can target.")),
      ("Keep backups you can restore", p("Make sure your host or a backup tool keeps regular copies of your site and database, stored away from the site itself, and test a restore at least once. A working backup turns a disaster into an inconvenience.")),
      ("Protect logins", p("Use strong, unique passwords and two-factor authentication for every admin account, remove old staff accounts and give each person only the access they need.")),
      ("Watch for warning signs", ul(["Unfamiliar admin users.", "Pages or links you didn't add.", "Redirects to other sites.", "Security warnings in Google Search Console.", "Sudden drops in search traffic."])),
      ("Search Console helps", p("Google Search Console has a Security issues report that warns site owners when Google detects problems such as hacked content or malware. Check it monthly and make sure alerts reach an inbox someone reads.")),
      ("A monthly website security routine", ol(["Apply pending updates.", "Delete unused plugins, themes and accounts.", "Check backups ran.", "Review Search Console's Security issues report.", "Click through key pages and forms."])),
      ("A worked example", p("Imagine a dental office in Irvine whose website has 30 plugins, half of them inactive and several out of date. Its web developer deletes the unused ones, turns on automatic security updates, adds two-factor login and sets up off-site backups. The site now has fewer weak points and recovers quickly if anything goes wrong.")),
      ("Questions owners ask us", p("Owners often ask whether small sites are really targeted. Automated attacks don't choose by size; they look for known weaknesses anywhere. Another common question is whether automatic updates break sites. Occasionally, which is why backups and a quick check after updates matter. Owners also ask who should be responsible. Name one person or provider who applies updates and checks the site every month.")),
      ("Security protects search visibility too", p("A hacked site can show spam to visitors, get flagged by Google and lose rankings. Keeping your site secure is part of keeping the search visibility you have built for your Anaheim or Orange County business.")),
      ("The short version", p("Google says attackers now use AI to turn security patches into attacks automatically. Anaheim and Orange County small businesses should update their websites promptly, remove unused software, protect logins, keep tested backups and watch Search Console's security report."))],
     faqs=[("What are autonomous AI attacks?", "Attacks where AI frameworks scan software updates, find the patched flaw and build an exploit without humans, as Google's threat group described."),
           ("When did Google report this?", "November 16, 2026, in the Google Threat Intelligence Group's post."),
           ("What should small businesses do first?", "Apply website, plugin and theme updates promptly."),
           ("Should I delete unused plugins?", "Yes. Delete them rather than only deactivating them."),
           ("How do I know if my site is hacked?", "Watch for unfamiliar users or pages, redirects and alerts in Search Console's Security issues report."),
           ("Are small sites targeted?", "Automated attacks look for known weaknesses regardless of a site's size."),
           LOCAL_FAQ],
     links=[SECISSUES, BACK, LOCAL, AUD],
     sources=["g_gtig_q4"],
     visuals=[V.flow(5, "Why update speed matters", "Based on Google's November 16, 2026 post.",
               [("Patch", "A fix is released."), ("Scan", "AI studies the patch."),
                ("Exploit", "An attack is built."), ("Defend", "Update before it arrives.")])],
     secondary=["AI cyberattacks small business", "website security updates", "WordPress plugin updates", "GTIG AI Threat Tracker"],
     hero_query="How can my small business website stay safe from AI attacks?"),
]

if __name__ == "__main__":
    from blog_2026_11_17_extra import add_x
    add_x(PAGES)
    save_all(PAGES)
