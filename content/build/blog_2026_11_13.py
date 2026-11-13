"""Blog posts for 2026-11-13 (5 posts). Every fact is checked at the linked Google source on 2026-11-13."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_12  # noqa: F401  (SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SRC.update({
    "g_aimode_ads": {"title": "Google Ads & Commerce blog: Ads in AI Mode expand to new markets (Oct 28, 2026)",
                     "url": "https://blog.google/products/ads-commerce/ads-in-ai-mode-global/"},
    "g_ai_ads_help": {"title": "Google Ads Help: About ads in AI-powered experiences in Google Search",
                      "url": "https://support.google.com/google-ads/answer/16297775?hl=en"},
    "g_fsv": {"title": "Google Ads & Commerce blog: Expanding our defenses against financial scam ads (Oct 20, 2026)",
              "url": "https://blog.google/products/ads-commerce/financial-services-verification-united-states-canada/"},
    "g_askmaps": {"title": "Google: Ask Maps gets more helpful with food ordering and more (Aug 6, 2026)",
                  "url": "https://blog.google/products-and-platforms/products/maps/order-food-in-ask-maps/"},
    "g_eyewear": {"title": "Google: See our intelligent eyewear lineup and pre-order your pair (Nov 12, 2026)",
                  "url": "https://blog.google/innovation-and-ai/technology/xr-ar/google-intelligent-eyewear-collections-pre-order/"},
    "g_chrome_gemini": {"title": "Google: Get quick answers from Gemini on any website (Nov 12, 2026)",
                        "url": "https://blog.google/innovation-and-ai/products/gemini-app/research-with-gemini-in-chrome/"},
    "g_chrome_help": {"title": "Google Chrome Help: Use Gemini in Chrome", "url": "https://support.google.com/chrome/answer/16283624?hl=en"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")
MODE = L("how to optimize for Google AI Mode", "how-to-optimize-for-google-ai-mode")
AIO = L("how to show up in Google AI Overviews", "how-to-show-up-in-google-ai-overviews")
GEMSEO = L("Gemini SEO", "gemini-seo")
TRACK = L("how to track AI visibility", "how-to-track-ai-visibility")
GEOPPC = L("GEO vs PPC", "geo-vs-ppc")
IVT = L("Google Ads' Invalid Traffic card", "google-ads-invalid-traffic-card")
GBP = L("Google Business Profile optimization", "google-business-profile-optimization-orange-county")
GBP_LINKS = L("Google Business Profile booking and order links", "google-business-profile-links")
GBP_EDIT = L("how to edit your Google Business Profile", "how-to-edit-google-business-profile")
REST = L("SEO for restaurants in Orange County", "seo-for-restaurants-orange-county")
FIN = L("GEO for financial advisors", "geo-for-financial-advisors")
MORT = L("SEO for mortgage brokers", "seo-for-mortgage-brokers")
INS = L("SEO for insurance agents", "seo-for-insurance-agents")
COMPARE = L("how to write comparison pages", "how-to-write-comparison-pages")
PRODUCT = L("product pages for AI shopping", "product-pages-for-ai-shopping")
FAQ = L("FAQ pages for AI search", "faq-pages-for-ai-search")


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


PAGES = [
# 1 ------------------------------------------------------------------
blog(1, "Google AI Search",
     slug="ads-in-ai-mode-local-business", query="ads in ai mode", kw="ads in AI Mode",
     eyebrow="Google Ads", short_title="Ads in AI Mode: what local advertisers should know",
     title="Ads in AI Mode: What Local Businesses Should Know",
     meta="Google is expanding ads in AI Mode and launching multiturn ads in the U.S. How they work and what Anaheim and Orange County advertisers should do now.",
     h1="Ads in AI Mode: How Google's Sponsored Results Work for Local Businesses",
     answer="Google is expanding ads in AI Mode to more countries and launching multiturn ads in the U.S., so ads can appear in follow-up questions, always labeled Sponsored. Existing Search, Shopping and Performance Max campaigns are eligible automatically, and Google says paid ads don't influence the organic AI responses. Anaheim and Orange County advertisers should check targeting, assets and landing pages.",
     takeaways=["Announced October 28, 2026.", "Multiturn ads launching in the U.S. for follow-up questions.",
                "Ads are labeled Sponsored and don't influence organic AI answers.", "Existing Search, Shopping and Performance Max campaigns are eligible.",
                "AI Mode queries are on average three times longer than traditional searches."],
     sections=[
      ("What Google announced", "<p>On October 28, 2026, Shashi Thakur, Vice President and General Manager of Google Search Ads, announced that ads in AI Mode are expanding to new countries. Google is scaling them in Australia, Canada, India, Kenya, Malaysia, New Zealand, Nigeria, Pakistan, the Philippines and Singapore, with plans for more locales including Brazil, Mexico and the United Kingdom in the fourth quarter of 2026. In the U.S., Google is launching multiturn ads, which can appear in follow-up questions in AI Mode.</p>"),
      ("Why Google says this matters", "<p>Google says that in AI Mode, queries are on average three times longer than traditional searches, citing its US AI Mode report from May 2026. Longer, conversational questions give Google more context about what someone needs. Google also says click-through rates are already similar between sponsored and organic product list items within AI Mode, based on its US internal data from late August to early September 2026.</p>"),
      ("Always labeled Sponsored", "<p>Google's Ads help page says all ads in AI Overviews and AI Mode are clearly labeled Sponsored and visually distinguished from organic content. It also states that paid advertising does not influence the organic responses generated by Google AI. Paying for ads doesn't buy a mention in the AI answer itself.</p>"),
      ("No new campaigns needed", "<p>Advertisers don't need new campaigns or separate budgets. Google says existing Search, Shopping and Performance Max campaigns are automatically eligible through the Google Ads auction. Text ads and Shopping ads can appear, and Google is experimenting with other formats such as local inventory ads and vehicle ads. Availability is in English in the U.S. and select English-speaking markets, expanding over time.</p>"),
      ("How ads are matched", "<p>Google matches ads either directly to the query, when the search already shows commercial intent, or contextually to both the query and the AI response, when someone asks a longer, exploratory question. Google's example: someone asking why their pool is green may see ads for pool vacuums or algae treatment, because the AI answer mentions cleaning steps.</p>"),
      ("Which targeting is eligible", "<table><tr><th>Targeting</th><th>Direct query matching</th><th>Contextual matching</th></tr><tr><td>AI Max for Search, broad match, Shopping, Performance Max</td><td>Yes</td><td>Yes</td></tr><tr><td>Exact and phrase match keywords</td><td>Yes, for clear commercial intent</td><td>No</td></tr></table><p>Source: Google Ads Help. Advertisers who rely only on exact and phrase match won't appear in contextual placements on broader questions.</p>"),
      ("AI explainers", "<p>Google says some placements may show AI explainers: short text generated by Gemini that explains how an ad relates to what the person is looking for. They can draw on the query, the AI response and publicly available sources, including your website. They aren't part of your headlines or descriptions, which makes accurate website content even more important.</p>"),
      ("What this means for local advertisers", "<p>For a pool service in Anaheim, a dentist in Irvine or a contractor in Santa Ana, AI Mode questions are often detailed: costs, timing, comparisons. Ads can now follow the conversation. Your assets, landing pages and website content all shape how you're presented.</p>"),
      ("Checklist for this month", ol(["Review whether your campaigns use broad match, AI Max or Performance Max if you want contextual placements.",
                                       "Update headlines, descriptions, images and prices in your assets.",
                                       "Make landing pages answer the detailed questions customers ask.",
                                       "Check your website facts, since AI explainers may draw on it.",
                                       "Watch performance and lead quality, not just clicks."])),
      ("Organic visibility still matters", "<p>Because ads don't influence the organic AI response, being mentioned in the answer itself depends on the same things as before: clear, accurate pages, consistent listings and genuine reviews. Most businesses benefit from both: organic visibility for trust and ads for reach when budgets allow.</p>"),
      ("A worked example", "<p>Imagine a homeowner in Orange asking AI Mode how to fix a leaking water heater and whether to repair or replace it. A plumber running broad match or Performance Max could appear in a Sponsored section as the conversation turns to replacement costs. Meanwhile, a plumber whose website clearly explains repair versus replacement and lists prices has a better chance of being cited in the organic answer.</p>"),
      ("Measure carefully", "<p>Track leads and booked jobs by campaign, not only clicks. Google's Invalid Traffic card can show what was filtered, but your own records show whether AI Mode traffic turns into customers.</p>"),
      ("The short version", "<p>Ads in AI Mode are expanding, and in the U.S. they can now appear in follow-up questions. They're labeled Sponsored and don't influence organic answers. Anaheim and Orange County advertisers should review targeting, refresh assets and make sure their websites answer detailed questions.</p>")],
     faqs=[("What are ads in AI Mode?", "Sponsored ads that can appear within or alongside AI Mode responses when a conversation has commercial relevance."),
           ("Do I need a new campaign for AI Mode ads?", "No. Google says existing Search, Shopping and Performance Max campaigns are automatically eligible."),
           ("Do ads influence the AI answer?", "No. Google says paid advertising doesn't influence organic responses generated by Google AI."),
           ("What are multiturn ads?", "Ads that can appear in follow-up questions in AI Mode; Google is launching them in the U.S."),
           ("Do exact match keywords show in AI Mode?", "For clear commercial queries, yes; they aren't eligible for contextual matching on broader questions."),
           ("What is an AI explainer?", "Short Gemini-generated text explaining how an ad relates to the search, which can draw on your website."),
           ("How much longer are AI Mode searches?", "Google says on average three times longer than traditional searches."),
           LOCAL_FAQ],
     links=[MODE, GEOPPC, IVT, AIO, LOCAL, AUD],
     sources=["g_aimode_ads", "g_ai_ads_help"],
     visuals=[V.flow(4, "How ads reach AI Mode", "From Google's announcement and Ads Help.",
               [("Question", "A detailed, conversational search."), ("Match", "Direct or contextual matching."),
                ("Sponsored", "Ads labeled and separate from the answer."), ("Follow-up", "Multiturn ads in the U.S.")])],
     secondary=["AI Mode advertising", "Google AI Mode ads", "multiturn ads", "ads in AI Overviews"],
     hero_query="Can my business advertise inside Google AI Mode answers?"),

# 2 ------------------------------------------------------------------
blog(2, "Google news",
     slug="google-financial-services-verification-us", query="google financial services verification", kw="Financial Services Verification",
     eyebrow="Google Ads", short_title="Google's Financial Services Verification comes to the U.S.",
     title="Google Financial Services Verification Comes to U.S.",
     meta="Google plans Financial Services Verification for ads in the U.S. and Canada in early 2027. What Orange County advisors, lenders and agents should prepare.",
     h1="Financial Services Verification Is Coming to the U.S.: What Financial Advertisers Should Know",
     answer="Google plans to bring its Financial Services Verification program to the U.S. and Canada in early 2027. Advertisers will need to show they're authorized by relevant regulators or recognized registries before running certain financial ads. Google will share country-specific requirements and notify advertisers who must verify. Anaheim and Orange County financial businesses should prepare credentials now.",
     takeaways=["Announced October 20, 2026.", "Rollout planned for early 2027 in the U.S. and Canada.", "Advertisers must show regulator or registry authorization.",
                "More than 97% of ads seen in both countries already come from identity-verified advertisers.", "Google will notify advertisers who need to verify."],
     sections=[
      ("What Google announced", "<p>On October 20, 2026, Keerat Sharma, Vice President and General Manager of Ads Privacy and Safety at Google, announced that Google is bringing its Financial Services Verification program to the U.S. and Canada, with a planned rollout in early 2027. Google says the program already protects approximately 2 billion internet users across 42 countries from financial scams.</p>"),
      ("What verification requires", "<p>Under the policy, advertisers must demonstrate that they are authorized by relevant regulators or recognized registries before running certain financial ads. Google says this helps prevent brand impersonation and stops bad actors from reaching people. It sits on top of identity verification, which Google calls its longstanding first line of defense.</p>"),
      ("Identity verification already covers most ads", "<p>Google says that in both the U.S. and Canada, more than 97% of the ads people see on Google already come from identity-verified advertisers. Financial Services Verification adds a specialized check of an advertiser's credentials for financial ads.</p>"),
      ("Where it started", "<p>Google says it was the first major platform to require this kind of verification, starting in the United Kingdom in 2021 and most recently expanding across the European Union. The U.S. and Canada rollout builds on that experience.</p>"),
      ("Working with banking associations", "<p>In the U.S., Google says it is working with the American Bankers Association to use its registry to verify authorized banks before ads run. In Canada, it is engaging with the Canadian Bankers Association. Because regulations differ by country, Google says it will use a phased approach adapted to each market.</p>"),
      ("AI-powered ad safety", "<p>Google says verification works alongside its safety systems, and that in 2025 Gemini helped those systems catch over 99% of policy-violating ads before they ever served. It also mentions the Global Signal Exchange, which shares information across tech, finance and law enforcement to stop fraud.</p>"),
      ("What advertisers can expect", ul(["Country-specific information before rollout, including accepted registries.", "Details of required credentials.",
                                          "Onboarding instructions.", "A notification if and when your business needs to complete verification, before enforcement begins."])),
      ("Who should pay attention", "<p>Google refers to certain financial ads without listing every category in this announcement, so watch for its country-specific guidance. Banks, credit unions, lenders, mortgage brokers, investment advisers, insurance providers and other financial businesses advertising in Orange County should all keep an eye on their Google Ads accounts.</p>"),
      ("How to prepare now", ol(["Confirm your Google Ads identity verification is complete.", "Gather your licenses and registration numbers, such as those on regulator or registry lookups.",
                                 "Make sure your business name in Google Ads matches your registered name.", "Check that your website shows license details and disclosures clearly.",
                                 "Watch for notifications in Google Ads and act quickly."])),
      ("Why this helps legitimate businesses", "<p>Scam ads that impersonate trusted brands damage trust in every financial advertiser. Stronger verification makes it harder for impostors to target your customers, and makes a verified business easier to trust.</p>"),
      ("Trust signals beyond ads", "<p>The same credentials matter in organic search and AI answers. Show license numbers, regulatory disclosures, professional credentials and real team pages on your website. AI assistants and searchers both look for evidence that a financial business is legitimate.</p>"),
      ("A worked example", "<p>Imagine a mortgage broker in Irvine who runs Search ads for refinancing. Before verification opens, the broker confirms identity verification is complete, notes the company and individual license numbers from the relevant registry, checks that the Google Ads business name matches the license, and adds license details to the website footer. When Google's notification arrives, the broker can complete verification quickly and avoid paused ads.</p>"),
      ("The short version", "<p>Google's Financial Services Verification is coming to the U.S. and Canada in early 2027. Financial advertisers will need to prove authorization by regulators or registries. Anaheim and Orange County financial businesses should prepare credentials, align business names and watch for Google's notifications.</p>")],
     faqs=[("What is Google's Financial Services Verification?", "A program requiring advertisers to show authorization by regulators or registries before running certain financial ads."),
           ("When does it come to the U.S.?", "Google plans to roll it out in the U.S. and Canada in early 2027."),
           ("Which ads does it cover?", "Certain financial ads; Google will publish country-specific details before rollout."),
           ("Will Google tell me if I need to verify?", "Yes. Google says advertisers will be notified if and when they need to complete it."),
           ("Is this the same as identity verification?", "No. It adds a check of financial credentials on top of identity verification."),
           ("How many countries already have it?", "Google says 42 countries, protecting about 2 billion users."),
           ("What should I do now?", "Complete identity verification, gather license details and align your business name."),
           LOCAL_FAQ],
     links=[FIN, MORT, INS, IVT, LOCAL, AUD],
     sources=["g_fsv"],
     visuals=[V.flow(4, "Getting verified", "From Google's October 20, 2026 announcement.",
               [("Identity", "Advertiser identity verification."), ("Credentials", "Regulator or registry authorization."),
                ("Notice", "Google notifies who must verify."), ("Ads run", "Verified financial ads serve.")])],
     secondary=["Google Ads financial services verification", "financial ads policy Google", "financial scam ads", "verify financial advertiser Google"],
     hero_query="Will my financial services ads on Google need extra verification?"),

# 3 ------------------------------------------------------------------
blog(3, "Google Search",
     slug="ask-maps-food-ordering-restaurants", query="ask maps food ordering", kw="Ask Maps food ordering",
     eyebrow="Google Maps", short_title="Ask Maps food ordering and what restaurants should do",
     title="Ask Maps Food Ordering: What Restaurants Should Do",
     meta="Google's Ask Maps can now help people order food, find hotels and events, and suggest edits. What Anaheim and Orange County restaurants should check.",
     h1="Ask Maps Food Ordering: How Google Maps' AI Helps Diners Order, and What Restaurants Should Do",
     answer="Ask Maps food ordering lets people ask Google Maps to find open restaurants along their route that serve what they want and add the dish to their cart. Google says it's rolling out in the U.S. with partners like Square and Toast, with Uber Eats coming soon. Anaheim and Orange County restaurants should keep menus, hours and ordering links accurate.",
     takeaways=["Announced August 6, 2026.", "Ask Maps can find open restaurants on your route and add a dish to your cart.",
                "Food ordering partners include Square and Toast, with Uber Eats coming soon.", "People can suggest edits by photographing a storefront sign.",
                "Food ordering is rolling out in the U.S. first."],
     sections=[
      ("What Google announced", "<p>On August 6, 2026, Google added new agentic capabilities to Ask Maps, which it describes as Google Maps' biggest transformation in over a decade. Ask Maps brings Gemini model capabilities to Maps to answer real-world questions, and can now handle complex, multi-step tasks such as ordering food.</p>"),
      ("How food ordering works", "<p>Google's example: ask Maps to order a specific dish to pick up on the way home. Ask Maps finds open restaurants along the route that serve it, and can consider saved places or dietary needs. Once the person chooses a restaurant, Ask Maps can add the dish directly to the cart so they can review and complete the order.</p>"),
      ("The ordering partners", "<p>Google says food ordering is rolling out with partners like Square and Toast, with Uber Eats coming soon. It is co-developing a Universal Commerce Protocol for Food with partners. For restaurants, the point-of-sale and ordering systems you already use may determine whether you can take orders this way.</p>"),
      ("Hotels and events too", "<p>Ask Maps can also compare real-time hotel prices and availability, and show local events, from concerts to comedy shows, with links for tickets. In a visitor-heavy city like Anaheim, that puts restaurants, hotels and venues side by side in one conversation.</p>"),
      ("Personal Intelligence and memory", "<p>People can choose to connect Ask Maps to Gmail, with Calendar coming later, so it can factor in plans such as flights or dinner reservations. Google says this connection is off by default. If history settings are on, Ask Maps also remembers past conversations.</p>"),
      ("Conversational edits and tips", "<p>Google says people can suggest edits conversationally, including uploading a photo of a storefront sign so Maps can detect new hours and ask them to confirm before submitting. They can also share insider tips, such as more parking behind the building. Google says its protection systems review suggested edits for accuracy.</p>"),
      ("Why this matters for restaurants", "<p>If customers can update your hours from a photo of your sign, your sign, your website and your Business Profile all need to agree. And if diners order through Maps, your menu, availability and ordering setup decide whether you're an option at all.</p>"),
      ("Where it's available", "<p>Google says food ordering, hotel and event discovery and conversational contributions are rolling out in the U.S., with more countries to come. Ask Maps itself is also expanding to Australia, Brazil, Canada, Indonesia, Japan and Mexico, along with over 150 countries and territories in English.</p>"),
      ("What to check this week", ol(["Confirm your hours and special hours on your Business Profile and signage match.",
                                       "Keep your menu current, with dish names customers actually use.",
                                       "Check whether your ordering or POS provider supports ordering through Google.",
                                       "Add your own ordering link and set it as preferred where possible.",
                                       "Fill in attributes such as dietary options, parking and takeout."])),
      ("Dietary needs and dish names", "<p>Ask Maps can consider dietary needs and look for a specific dish. Restaurants that list dishes clearly, with vegetarian, vegan or gluten-free options marked, are easier to match than those with a menu only in a photo or PDF.</p>"),
      ("A worked example", "<p>Imagine someone leaving work in Irvine who asks Maps for vegetarian pho to pick up on the way home to Anaheim. A Vietnamese restaurant on that route with an accurate menu, correct hours and ordering through a supported provider can be suggested and have the dish added to the cart. One with an outdated menu photo and wrong hours may not appear at all.</p>"),
      ("Keep an eye on suggested edits", "<p>Because people can now suggest edits easily, check your Business Profile regularly for changes you didn't make, and correct anything inaccurate quickly.</p>"),
      ("The short version", "<p>Ask Maps can now help diners order food along their route, with partners like Square and Toast. Anaheim and Orange County restaurants should keep hours, menus, attributes and ordering links accurate everywhere.</p>")],
     faqs=[("What is Ask Maps food ordering?", "A feature that finds open restaurants serving what you want and adds the dish to your cart for review."),
           ("Which ordering partners work with Ask Maps?", "Google says Square and Toast, with Uber Eats coming soon."),
           ("Where is food ordering available?", "Google says it's rolling out in the U.S., with more countries to come."),
           ("Can customers change my hours on Maps?", "They can suggest edits, including from a photo of your sign; Google reviews them."),
           ("Is Gmail connected to Ask Maps automatically?", "No. Google says Personal Intelligence is off by default."),
           ("What should restaurants do now?", "Keep hours, menus, attributes and ordering links accurate."),
           ("Does Ask Maps consider dietary needs?", "Google says it can consider dietary needs and saved places."),
           LOCAL_FAQ],
     links=[REST, GBP_LINKS, GBP_EDIT, GBP, LOCAL, AUD],
     sources=["g_askmaps"],
     visuals=[V.flow(3, "From a request to an order", "Based on Google's August 6, 2026 announcement.",
               [("Ask", "A dish to pick up on the way home."), ("Find", "Open restaurants along the route."),
                ("Cart", "Dish added for review."), ("Order", "Completed through a partner.")])],
     secondary=["Ask Maps", "Google Maps AI ordering", "Google Maps Square Toast ordering", "restaurant Google Maps AI"],
     hero_query="Can customers order from my restaurant through Google Maps AI?"),

# 4 ------------------------------------------------------------------
blog(4, "AI assistants",
     slug="google-intelligent-eyewear-local-business", query="google intelligent eyewear", kw="Google intelligent eyewear",
     eyebrow="AI news", short_title="Google intelligent eyewear and local businesses",
     title="Google Intelligent Eyewear: What It Means Locally",
     meta="Google intelligent eyewear with Gemini goes on sale December 10. What hands-free AI glasses mean for Anaheim and Orange County shops, venues and restaurants.",
     h1="Google Intelligent Eyewear With Gemini: What Hands-Free AI Glasses Mean for Local Businesses",
     answer="Google intelligent eyewear, made with Gentle Monster, Warby Parker and Samsung, brings Gemini to glasses: people can ask about what they see, get Maps directions in their ear and translate speech. Pre-orders opened November 12, 2026, with sales from December 10. For Anaheim and Orange County businesses, storefronts, signs and posters become things customers can ask AI about.",
     takeaways=["Pre-orders opened November 12, 2026.", "Available in stores and online from December 10.", "Made with Gentle Monster, Warby Parker and Samsung.",
                "Gemini can answer questions about what you're looking at.", "Works with Pixel, Samsung phones and iPhones."],
     sections=[
      ("What Google announced", "<p>On November 12, 2026, Google opened pre-orders for its Intelligent Eyewear collections, made with Gentle Monster, Warby Parker and Samsung. Google says the glasses bring real-time help from Gemini throughout the day and work with Pixel and Samsung phones as well as iPhones. They go on sale in stores and online on December 10.</p>"),
      ("The collections", "<table><tr><th>Collection</th><th>Starting price</th><th>Notes</th></tr><tr><td>Gentle Monster</td><td>$449</td><td>Six designs; U.S. and South Korea</td></tr><tr><td>Warby Parker</td><td>$395</td><td>Three styles; guided demos at more than 360 retail locations</td></tr></table><p>Source: Google, November 12, 2026. Prescription options are available for most frames.</p>"),
      ("Built for all-day wear", "<p>Google says the frames weigh around 41 grams, the battery lasts up to nine hours, and the charging case can recharge the glasses up to seven times. Google notes these figures come with conditions in its footnotes.</p>"),
      ("Asking about what you see", "<p>Google's examples include asking Gemini about the story behind a street mural, getting a recommendation from a New Arrivals bookshelf, or looking at an event poster to check calendar availability. People say Hey Gemini or tap their frames to ask.</p>"),
      ("Directions and translation", "<p>Google Maps can give turn-by-turn directions in the wearer's ear, and Google Translate can deliver real-time speech translation with automatic language detection across more than 70 languages. In an area with as many visitors and languages as Anaheim and Orange County, that changes how people find and talk to businesses.</p>"),
      ("Accessibility features", "<p>Google highlights Guided Vision, which gives conversational audio descriptions for people who are blind, have low vision or want help reading small print. Through a collaboration with Aira, wearers can connect to a trained human visual interpreter.</p>"),
      ("Privacy protections", ul(["Camera visuals from Gemini on glasses aren't saved in Gemini History or used to train AI models or target ads.",
                                  "The glasses are designed to redact bystanders' faces before Gemini processes visuals.", "An indicator light shows when a photo or video is being taken.",
                                  "Recording is designed to stop if the light is covered or disabled."])),
      ("Why this matters for local businesses", "<p>When customers can look at your storefront, menu board or event poster and ask Gemini about it, the information Google has about your business matters even more. Hours, reviews, menus and events need to be accurate across your Business Profile and website, because that's what an AI assistant can draw on.</p>"),
      ("What to get right", ol(["Keep signage, hours and Business Profile details consistent.", "Publish events with dates and ticket links on your website and profile.",
                                "Make menus and product details readable as text, not only images.", "Add photos of your storefront so it's easy to recognize.",
                                "Respond to reviews; they shape how assistants describe you."])),
      ("Retail and demos", "<p>Warby Parker is offering guided demos at more than 360 retail locations, and Google Store and select Gentle Monster stores have hands-on demos too. Optical shops and electronics retailers may see questions from customers curious about the glasses.</p>"),
      ("A worked example", "<p>Imagine a visitor walking near Anaheim's Center Street who sees a poster for a weekend jazz night at a local bar. Wearing the glasses, they ask Gemini whether they're free and how to get there. A venue whose event is listed with a date and ticket link on its website and Business Profile is easy for the assistant to describe; one that only posted the event on a flyer gives it far less to work with.</p>"),
      ("Should you change anything now?", "<p>The glasses go on sale December 10, so adoption will take time. But every step above also helps with Google Search, Maps and AI assistants on phones, so there's no wasted effort.</p>"),
      ("The short version", "<p>Google's intelligent eyewear brings Gemini to everyday glasses from December 10. Anaheim and Orange County businesses should make sure signs, hours, menus and events are accurate and consistent online, so AI can describe them correctly.</p>")],
     faqs=[("What is Google intelligent eyewear?", "Glasses made with Gentle Monster, Warby Parker and Samsung that bring Gemini help hands-free."),
           ("When can people buy them?", "Google says in stores and online from December 10, with pre-orders from November 12, 2026."),
           ("How much do they cost?", "Google lists Warby Parker from $395 and Gentle Monster from $449."),
           ("Do they work with iPhone?", "Google says they work with Pixel and Samsung phones as well as iPhones."),
           ("Can the glasses translate speech?", "Google says real-time speech translation across more than 70 languages."),
           ("Do they record people without notice?", "An indicator light shows when recording, and recording is designed to stop if it's covered."),
           ("What should local businesses do?", "Keep signage, hours, menus and events accurate on your website and Business Profile."),
           LOCAL_FAQ],
     links=[GEMSEO, GBP, GBP_EDIT, TRACK, LOCAL, AUD],
     sources=["g_eyewear"],
     visuals=[V.flow(3, "From a glance to a visit", "Using Google's examples.",
               [("Look", "A storefront, poster or menu."), ("Ask", "Hey Gemini, or tap the frames."),
                ("Answer", "Gemini uses Google apps and info."), ("Go", "Maps directions in your ear.")])],
     secondary=["Gemini glasses", "Warby Parker Google glasses", "Gentle Monster Google eyewear", "AI glasses local business"],
     hero_query="What do Google's new Gemini glasses mean for my store?"),

# 5 ------------------------------------------------------------------
blog(5, "AI assistants",
     slug="gemini-in-chrome-website-answers", query="gemini in chrome", kw="Gemini in Chrome",
     eyebrow="AI news", short_title="Gemini in Chrome reads your website for visitors",
     title="Gemini in Chrome: How Visitors Read Your Site Now",
     meta="Gemini in Chrome can summarize and compare web pages in a side panel. What it means for Anaheim and Orange County business websites and how to prepare.",
     h1="Gemini in Chrome: How Visitors Use AI to Read and Compare Your Website",
     answer="Gemini in Chrome lets people open a side panel and ask Gemini to summarize a page, compare product details across tabs or explain complicated topics, using the content of the tabs they share. Google highlighted it on November 12, 2026. For Anaheim and Orange County businesses, it means visitors may read your website through an AI summary, so clear facts matter.",
     takeaways=["Google highlighted Gemini in Chrome on November 12, 2026.", "It works in a side panel using the current tab's content.",
                "People can share up to 10 open tabs on a computer.", "It can compare information across pages.", "It's rolling out gradually and isn't available to everyone."],
     sections=[
      ("What Google shared", "<p>On November 12, 2026, Google published a short tip on using Gemini in Chrome to get answers without opening another tab: click the Gemini icon in the Chrome toolbar to open the side panel, then ask Gemini to summarize a dense report, compare product details or explain complicated topics in plain language, all while keeping your place on the page.</p>"),
      ("How it uses your page", "<p>Chrome's help page says Gemini in Chrome uses content from the current browser tab to give relevant responses, and on a computer people can share up to 10 open tabs. Tabs opened from a chat are also shared. Users can stop sharing a tab at any time.</p>"),
      ("What people can ask", ul(["Summarize key takeaways from an article.", "Explain a complex topic in a different way.", "Compare or consolidate information across pages.",
                                  "Make recommendations based on preferences.", "Modify a recipe to meet dietary needs.", "Complete multi-step actions on their behalf."])),
      ("Who can use it", "<p>Google says Gemini in Chrome isn't available to everyone yet and is rolling out gradually. On a computer, people need to be 13 or older and in a supported region, use a Chromebook Plus, Mac or Windows computer, use the latest Chrome, be signed in and use a supported language. It isn't available in Incognito mode, and work or school accounts need administrator approval.</p>"),
      ("Why this matters for businesses", "<p>When a potential customer compares three contractors' websites in three tabs and asks Gemini which offers a warranty, which serves their city and what each costs, the AI reads your page for them. If those facts aren't on the page in plain text, they can't be compared.</p>"),
      ("Comparison is the key use", "<p>Comparing product details across pages is one of Google's headline examples. For local businesses, this is the shortlist moment: a customer has narrowed the choice and is weighing options side by side.</p>"),
      ("Make your facts easy to extract", ol(["State prices or price ranges, service areas, hours and warranties in text, not only images.",
                                             "Use clear headings for each service and key detail.", "Put the most important facts near the top of each page.",
                                             "Use tables for options and pricing tiers.", "Keep details consistent with your Business Profile."])),
      ("Avoid vague pages", "<p>Pages that say call for a quote and little else give Gemini nothing to summarize or compare. Even rough ranges, what's included and how long jobs take give a customer something concrete, and give the AI accurate facts to repeat.</p>"),
      ("Test it yourself", "<p>If Gemini in Chrome is available to you, open your own service page and ask it to summarize the page, then open a competitor's page and ask Gemini to compare the two. Note what it gets wrong or can't find, and fix the page.</p>"),
      ("Media and multi-step actions", "<p>Chrome's help page says Gemini in Chrome can answer questions about audio and video already played on media websites, and can complete multi-step actions on a user's behalf. Clear page structure helps both people and AI move through your site.</p>"),
      ("A worked example", "<p>Imagine a homeowner in Garden Grove comparing three roofing companies in separate tabs and asking Gemini in Chrome which ones offer a written warranty and serve Garden Grove. A roofer whose page states its warranty terms and service area in plain text is named; one that only shows them in a badge image may be described as not mentioning a warranty.</p>"),
      ("Privacy for your visitors", "<p>Visitors control what they share: Google says the current tab is shared by default and can be removed, and people can turn off sharing the current tab by default in Chrome settings. You don't need to change anything on your site for it to work.</p>"),
      ("The short version", "<p>Gemini in Chrome lets visitors summarize and compare your pages with AI in a side panel. Anaheim and Orange County businesses should put key facts, prices, areas, hours and warranties, in clear text so Gemini represents them accurately.</p>")],
     faqs=[("What is Gemini in Chrome?", "AI assistance in a Chrome side panel that uses the content of your current tab to answer questions."),
           ("Can Gemini compare websites?", "Yes. Google says it can compare or consolidate information across pages, with up to 10 shared tabs on a computer."),
           ("Is Gemini in Chrome available to everyone?", "No. Google says it's rolling out gradually."),
           ("Does it work in Incognito mode?", "No. Google says it isn't available in Incognito mode."),
           ("Do I need to change my website?", "Nothing technical is required, but clear text facts help Gemini summarize you accurately."),
           ("What should my pages include?", "Prices or ranges, service areas, hours and warranties in plain text."),
           ("Can visitors stop sharing my page with Gemini?", "Yes. Users can remove tabs and change the default in settings."),
           LOCAL_FAQ],
     links=[GEMSEO, COMPARE, FAQ, PRODUCT, LOCAL, AUD],
     sources=["g_chrome_gemini", "g_chrome_help"],
     visuals=[V.flow(4, "How a visitor uses Gemini in Chrome", "From Google's tip and Chrome Help.",
               [("Open", "Gemini icon opens the side panel."), ("Share", "Current tab, up to 10 tabs."),
                ("Ask", "Summarize or compare."), ("Decide", "Customer shortlists a business.")])],
     secondary=["Gemini Chrome side panel", "Chrome AI summary", "Gemini compare websites", "AI browser assistant"],
     hero_query="Can customers use Gemini in Chrome to compare my business with competitors?"),
]

EXTRA = {
"ads-in-ai-mode-local-business": [
 ("Questions to ask your ads manager", ul(["Which of our campaigns use broad match, AI Max or Performance Max, and which rely only on exact and phrase match?",
   "Are our headlines, descriptions, images and prices current in every asset group?", "Which landing page does each campaign send people to, and does it answer detailed questions?",
   "How are we measuring leads and booked jobs, not just clicks?", "What negative keywords keep us out of irrelevant conversations?"])),
 ("Budgets and expectations", "<p>Because AI Mode placements come through existing campaigns, there is no separate budget to set. That also means spend can shift toward these placements without anyone noticing. Look at your search terms and placement reports regularly, compare cost per lead before and after you change targeting, and make one change at a time so you know what caused any difference. For a small business in Orange County with a limited budget, it is often better to keep tight targeting on your best services and expand only when the numbers justify it.</p>")],
"google-financial-services-verification-us": [
 ("Common mistakes to avoid", ul(["Waiting until ads are paused to gather credentials.", "Using a trade name in Google Ads that doesn't match the registered business name.",
   "Letting an agency's account details stand in for your own verification.", "Hiding license numbers and disclosures on the website.", "Ignoring Google Ads notifications and emails."])),
 ("Agencies and multiple accounts", "<p>Many financial businesses in Orange County work with an agency or manage several Google Ads accounts for different branches or products. Decide now who will receive Google's notifications and who will complete verification for each account. Make sure the business, not only the agency, has owner-level access to its Google Ads accounts, so verification isn't delayed by a change of provider. Keep a single folder with your licenses, registration numbers and business documents ready to share.</p>"),
 ("What this says about trust online", "<p>Verification programs are part of a broader shift toward proving who is behind ads, listings and content. Search engines and AI assistants increasingly favor businesses with clear, verifiable credentials. For financial firms, publishing the same licenses and disclosures you'll use for ad verification on your website and Business Profile strengthens trust in organic results too, where people often research before they ever click an ad.</p>")],
"ask-maps-food-ordering-restaurants": [
 ("Menus that work for AI", "<p>A menu that only exists as a photo or PDF is harder for any system to read. Publish your menu as text on your website, with dish names, short descriptions, prices and clear labels for dietary options. Keep your Business Profile menu in sync, and update both when dishes, prices or hours change. If you use an online ordering system, make sure its menu matches too, so a dish suggested by Ask Maps is actually available to order.</p>"),
 ("Common mistakes", ul(["Hours on the sign that don't match the Business Profile.", "Menu photos from years ago.", "No dietary labels on dishes.",
   "Ordering links that go to an old provider.", "Ignoring suggested edits from customers."])),
 ("Questions to ask your POS or ordering provider", ul(["Do you support ordering through Google Maps, and in which regions?", "How do menu updates sync to Google?",
   "What fees apply to orders placed through Google?", "How are order issues and refunds handled?"]))],
"google-intelligent-eyewear-local-business": [
 ("Translation and visitors", "<p>Anaheim welcomes visitors from around the world, and Orange County is home to large Spanish, Vietnamese, Korean and Chinese-speaking communities. Real-time translation in glasses could make it easier for visitors and residents to ask questions in shops and restaurants in their own language. That doesn't replace multilingual signage or staff, but it is another reason to keep your public information clear and simple, so it translates well.</p>"),
 ("Questions owners ask us", "<p>Owners often ask whether they should allow customers wearing camera glasses. That's a business decision, but Google says an indicator light shows when the glasses record, and recording is designed to stop if the light is covered. Another question is whether to create content specifically for glasses. There's no need: the same accurate listings, menus and pages that serve phones serve glasses. Owners also ask how quickly this will matter. Adoption will be gradual, but the groundwork is the same as for AI search today.</p>"),
 ("Checklist for retailers and venues", ol(["Photograph your storefront so it matches what people see on the street.", "List upcoming events with dates, times and ticket links.",
   "Keep holiday hours current from December onward.", "Make product and menu details available as text.", "Review your Business Profile monthly."]))],
"gemini-in-chrome-website-answers": [
 ("What to put on every service page", ul(["What the service is and who it's for.", "The cities or neighborhoods you serve.", "Typical price ranges or how pricing works.",
   "How long the job takes and how soon you can start.", "Warranties, licenses and insurance.", "How to book or request a quote."])),
 ("Questions owners ask us", "<p>Owners often ask whether Gemini in Chrome will replace their website. It won't: it reads your website for the visitor, which makes your site's content more important, not less. Another question is whether AI summaries can be wrong. They can, especially when pages are vague or contradict each other, so clear, consistent facts reduce the risk. Owners also ask whether they can block Gemini in Chrome. It works with content the visitor has open in their browser, so the practical approach is to make your pages easy to summarize accurately.</p>"),
 ("A quick page audit", "<p>Pick your three most important pages. For each, write down the five facts a customer most needs: price, area, timing, guarantee and how to book. Then check whether each fact is on the page in plain text, near the top and stated the same way as on your Business Profile. Fix any gaps, and repeat with your next three pages.</p>")],
}
for p in PAGES:
    for h, b in EXTRA.get(p["slug"], []):
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

MORE = {
"google-financial-services-verification-us": ("How this fits with your local visibility", "<p>Ads are only one way customers find a financial business. Many people in Anaheim and across Orange County search for an advisor, lender or insurance agent, read reviews, compare websites and ask AI assistants for recommendations before contacting anyone. The verification work you do for ads, gathering licenses, matching your registered name and publishing disclosures, also supports those organic channels. Keep your Google Business Profile name identical to your registered business name, list your credentials on your About and team pages, and make sure directory listings use the same details. When everything matches, customers, search engines and AI assistants see one consistent, trustworthy business, whether they arrive from an ad or an organic result. That consistency also makes the eventual verification step faster, because the details Google checks will already agree everywhere.</p>"),
"ask-maps-food-ordering-restaurants": ("Why this matters in Anaheim and Orange County", "<p>Anaheim's resorts, convention center and stadiums bring a constant flow of visitors who don't know the local restaurants and rely on their phones to decide where to eat. Orange County's commuters spend a lot of time on the road, and ordering a pickup on the way home is exactly the use case Google describes. For a family restaurant near the Convention Center or a taqueria along a busy commute route, being suggested by Ask Maps could mean orders from people who would never have found the business otherwise. The work to get there is not new or complicated: accurate hours, a readable menu, a supported ordering setup and an up-to-date Business Profile. What changes is how directly those details turn into orders, because the assistant can now go from question to cart in one conversation.</p>"),
"google-intelligent-eyewear-local-business": ("How this connects to AI search today", "<p>Glasses are a new way to ask the same AI that already answers questions in Google Search, Maps and the Gemini app. The information Gemini uses to answer a question about your storefront is largely the same information it uses when someone types a question on a phone: your Business Profile, your website, reviews and other public sources. That's why the preparation is the same. Businesses that already keep their listings accurate, publish clear pages about their services and respond to reviews are ready for glasses without doing anything extra. Businesses that haven't done that work have one more reason to start. Over the coming year, watch how customers describe finding you, and ask new customers how they heard about you, so you can spot when these new devices start making a difference.</p>"),
"gemini-in-chrome-website-answers": ("Why this matters for local service businesses", "<p>For many service businesses in Orange County, such as roofers, plumbers, dentists and lawyers, the website visit happens at the shortlist stage, after a customer has already found a few options on Google or Maps. That's when people compare details side by side, which is exactly what Gemini in Chrome makes easier. If your page clearly states your service area, pricing approach, guarantee and availability, the comparison works in your favor. If a competitor's page is clearer, the AI summary will reflect that. Treat each key page as an answer sheet for the questions customers ask before they call, and review it whenever your prices, services or hours change.</p>"),
}
for p in PAGES:
    if p["slug"] in MORE:
        h, b = MORE[p["slug"]]
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

if __name__ == "__main__":
    save_all(PAGES)
