"""Blog posts for 2026-11-15 (5 posts). Every fact is checked at the linked source on 2026-11-15."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_14  # noqa: F401  (SRC entries)
import batch33  # noqa: F401  (Apple Business SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SRC.update({
    "g_channel_priority": {"title": "Google Ads & Commerce blog: New Google Ads channel prioritization and budget controls (Oct 14, 2026)",
                           "url": "https://blog.google/products/ads-commerce/channel-prioritization-budget-allocation/"},
    "g_demandgen_oct": {"title": "Google Ads & Commerce blog: Build your data strength with October's Demand Gen drop (Oct 13, 2026)",
                        "url": "https://blog.google/products/ads-commerce/demand-gen-drop-october-2026/"},
    "g_holiday_agentic": {"title": "Google: Retailers, get ready for AI-driven holiday shopping (Sep 16, 2026)",
                          "url": "https://blog.google/products-and-platforms/products/shopping/google-shopping-updates-holiday-shopping/"},
    "g_studio_credits": {"title": "Google: Claim your Google Cloud Credits in Google AI Studio (Nov 13, 2026)",
                         "url": "https://blog.google/innovation-and-ai/technology/developers-tools/google-cloud-credits-gdp-ai-studio/"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")
AB_SETUP = L("how to set up Apple Business", "how-to-set-up-apple-business")
AB_ADDLOC = L("add your business to Apple Maps", "add-business-to-apple-maps")
AB_ADS = L("ads on Apple Maps", "apple-maps-ads")
AB_CARD = L("Apple Maps place card", "apple-maps-place-card")
NAP = L("NAP consistency and local citations", "nap-consistency-local-citations")
IVT = L("Google Ads' Invalid Traffic card", "google-ads-invalid-traffic-card")
AIMODE_ADS = L("ads in AI Mode", "ads-in-ai-mode-local-business")
LINKADS = L("link Google Ads to Google Analytics", "link-google-ads-to-google-analytics")
KEYEV = L("GA4 key events", "google-analytics-4-key-events")
LSA = L("Google Local Services Ads vs SEO", "google-local-services-ads-vs-seo")
PRODUCT = L("product pages for AI shopping", "product-pages-for-ai-shopping")
CART = L("Google's universal cart for retailers", "google-universal-cart-orange-county-retailers")
WHEN = L("Google's When to Buy Guide for retailers", "google-when-to-buy-holiday-retailers")
HYDRO = L("Gemini 4 Hydrogen for small businesses", "gemini-4-hydrogen-small-business")
SMB = L("AI SEO for small business", "ai-seo-for-small-business")
GEMSEO = L("Gemini SEO", "gemini-seo")


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


PAGES = [
# 1 ------------------------------------------------------------------
blog(1, "Playbooks",
     slug="apple-business-connect-now-apple-business", query="apple business connect apple business", kw="Apple Business Connect is now Apple Business",
     eyebrow="Apple Maps", short_title="Apple Business Connect is now Apple Business",
     title="Apple Business Connect Is Now Apple Business",
     meta="Apple Business Connect is now Apple Business. What changed, how to sign in and what Orange County businesses should do about their Apple Maps listings.",
     h1="Apple Business Connect Is Now Apple Business: What Local Businesses Should Do",
     answer="Apple Business Connect is now Apple Business, according to Apple's own guide. Apple Business combines Apple Business Manager, Apple Business Essentials and Apple Business Connect in one place, including the tools for managing how your business appears on Apple Maps. Existing users can sign in with the same Apple Account. Anaheim and Orange County businesses should check their listings and verification.",
     takeaways=["Apple Business Connect is now Apple Business.", "It combines three former Apple business products.", "You can sign in with your existing Apple Account.",
                "Organizations must verify within 60 days.", "Ads on Maps are available in the U.S. and Canada."],
     sections=[
      ("What changed", "<p>Apple's Apple Business Connect guide now states that Apple Business Connect is now Apple Business. Apple says Apple Business combines the capabilities of Apple Business Manager, Apple Business Essentials and Apple Business Connect into a single offering, covering both internal operations and customer-facing tools such as your Apple Maps listing.</p>"),
      ("Signing in", "<p>Apple says you can sign in to Apple Business at business.apple.com with the personal Apple Account you used for Apple Business Connect. You can create an Apple Account for Work, a Managed Apple Account with the full feature set, or keep your personal account and use only brand and location management.</p>"),
      ("Organizations become units", "<p>If you managed more than one organization in Apple Business Connect, Apple says they now appear as organizational units, and you can switch between them after agreeing to the terms.</p>"),
      ("Verification", "<p>Apple's guide says organizations have 60 days to verify, using two methods, such as a D-U-N-S Number or EIN plus an official business document, and that verification can take up to five business days.</p>"),
      ("What you can still do for Apple Maps", ul(["Add and verify locations and fix pins.", "Complete the place card with logo, cover photo and about section.",
                                                   "Upload photos and create showcases.", "Add Actions such as Order or Reserve.", "Read insights on searches, views and actions."])),
      ("Ads on Apple Maps", "<p>Apple Business also includes ads on Maps. Apple says they're available in the United States and Canada for advertisers with locations and an organization address there, with a monthly budget you control.</p>"),
      ("Why this matters for local businesses", "<p>The place card appears across Apple's apps, from Maps to Siri, Calendar and Messages, according to Apple's guide. Many iPhone users in Anaheim and across Orange County never open another map app, so an accurate Apple listing matters as much as your Google Business Profile.</p>"),
      ("What to do this week", ol(["Sign in at business.apple.com with your existing Apple Account.", "Accept the new terms and choose how you want to sign in.",
                                   "Check your organization's verification status.", "Review each location's name, pin, hours and phone.", "Make sure Apple's emails reach your inbox."])),
      ("Keep listings consistent", "<p>Apple Maps and Google Maps are separate. Whatever you change on one, change on the other, and on your website and main directories. Consistent details help customers and the apps and AI assistants that read business data.</p>"),
      ("A worked example", "<p>Imagine a flower shop in Fullerton that set up Apple Business Connect two years ago. The owner signs in to Apple Business with the same Apple Account, keeps the personal account for brand and location management, confirms the shop is verified, updates holiday hours and adds a Valentine's Day showcase. Nothing about the listing was lost in the change.</p>"),
      ("Our Apple Business guides", "<p>We've published step-by-step guides to setting up Apple Business, adding locations, completing the place card, photos, showcases, Actions, insights, Branded Mail, Tap to Pay on iPhone and ads on Apple Maps, each checked against Apple's own guide.</p>"),
      ("The short version", "<p>Apple Business Connect is now Apple Business. Sign in with your existing Apple Account, check verification and keep your Apple Maps listing as accurate as your Google one. Anaheim and Orange County businesses that do this reach iPhone users across Apple's apps.</p>")],
     faqs=[("Is Apple Business Connect gone?", "Apple says Apple Business Connect is now Apple Business."),
           ("What does Apple Business include?", "Capabilities from Apple Business Manager, Apple Business Essentials and Apple Business Connect."),
           ("Can I use my old Apple Business Connect login?", "Yes. Apple says you can sign in with the same personal Apple Account."),
           ("Do I need a Managed Apple Account?", "Only for the full feature set; a personal account still covers brand and location management."),
           ("Where do I sign in?", "At business.apple.com."),
           ("Can I still advertise on Apple Maps?", "Yes, in the U.S. and Canada, through Apple Business."),
           ("Does this change my Apple Maps listing?", "Your listing tools remain; check verification and details after signing in."),
           LOCAL_FAQ],
     links=[AB_SETUP, AB_ADDLOC, AB_CARD, AB_ADS, LOCAL, AUD],
     sources=["ab_renamed", "ab_signup", "ab_ads"],
     visuals=[V.flow(3, "Moving to Apple Business", "From Apple's guide.",
               [("Sign in", "business.apple.com."), ("Choose", "Work account or personal."),
                ("Verify", "Two methods within 60 days."), ("Review", "Locations and details.")])],
     secondary=["Apple Business", "Apple Business Connect change", "Apple Maps business listing", "business.apple.com"],
     hero_query="What happened to Apple Business Connect?"),

# 2 ------------------------------------------------------------------
blog(2, "Google news",
     slug="google-ads-channel-prioritization-budget-controls", query="google ads channel prioritization", kw="Google Ads channel prioritization",
     eyebrow="Google Ads", short_title="Google Ads channel prioritization and budget controls",
     title="Google Ads Channel Prioritization: New Controls",
     meta="Google Ads channel prioritization lets advertisers fund chosen channels first and cap spend on others. What Anaheim and Orange County advertisers should know.",
     h1="Google Ads Channel Prioritization and Budget Allocation: More Control Over Where Ads Run",
     answer="Google Ads channel prioritization lets advertisers mark channels such as Google Search, Search partners or the Display Network as high or low priority, so campaigns fund high-priority channels first. Budget allocation lets you cap low-priority channels at a percentage of the daily budget. Google is rolling them out across Search, Shopping, Performance Max and Demand Gen. Anaheim and Orange County advertisers can test networks without all-or-nothing choices.",
     takeaways=["Announced October 14, 2026.", "Mark channels as high or low priority.", "Cap low-priority channels at a share of daily budget.",
                "Rolling out to Search, Shopping, Performance Max and Demand Gen.", "Search campaigns with the Display Network change in February 2027."],
     sections=[
      ("What Google announced", "<p>On October 14, 2026, Google introduced two optional controls in Google Ads: channel prioritization and budget allocation. Google says they build on earlier controls such as Smart Bidding Exploration and campaign total budgets, and are rolling out globally across Search, Shopping, Performance Max and Demand Gen.</p>"),
      ("Channel prioritization", "<p>Google says channel prioritization lets advertisers categorize inventory as High priority or Low priority. Campaigns fully fund high-priority channels, within the target when using Target CPA or Target ROAS, before spending the rest on lower-priority channels.</p>"),
      ("How channels are grouped", "<p>For Search campaigns, Google Search, Search partners and the Google Display Network can be set to different priorities. In Performance Max and Demand Gen, Google surfaces like Search, YouTube, Maps, Gmail and Discover are prioritized together as Google channels.</p>"),
      ("Budget allocation", "<p>For channels set to Low priority, Google says advertisers can set a maximum percentage of the daily budget, which its tools aim to keep within on a best-effort basis. Google notes this matters for Target CPA or Target ROAS campaigns not limited by budget, where prioritization alone generally won't change much.</p>"),
      ("Where controls apply", "<p>Google says the controls roll out at the account and campaign levels and also apply to shared budgets, with distinct priority tiers across Search, Shopping, Performance Max and Demand Gen.</p>"),
      ("Test instead of opting out", "<p>Google describes these controls as giving more control than all-or-nothing opt-outs. Advertisers who switched off Search partners or the Display Network can now test them with clear limits instead.</p>"),
      ("A change coming in February 2027", "<p>Google says that starting in February 2027, for Search campaigns with the Google Display Network turned on, the current spend allocation setup will go away and advertisers may see a shift in channel spending. To keep their current setup, they can set the Display Network to Low priority with a 50% budget allocation.</p>"),
      ("What this means for local advertisers", "<p>Many small advertisers in Orange County want their money spent on Google Search, where people are actively looking for a plumber, dentist or restaurant. Setting Google Search as high priority and capping partner networks gives that control without switching other channels off entirely.</p>"),
      ("A simple setup for service businesses", ol(["Set Google Search to High priority.", "Set Search partners and the Display Network to Low priority.",
                                                     "Cap low-priority channels at a small share of the daily budget.", "Track leads by channel for a month.", "Adjust priorities based on cost per real lead."])),
      ("Measure leads, not clicks", "<p>Compare channels by key events such as form submissions and calls, ideally with Google Ads linked to Analytics. A channel with cheap clicks but few leads isn't cheap.</p>"),
      ("A worked example", "<p>Imagine a roofing company in Mission Viejo that turned off the Display Network years ago. With the new controls, it keeps Google Search as high priority and sets the Display Network to low priority with a 10% cap. After a month, it compares leads per dollar on each channel and decides whether to keep the test running.</p>"),
      ("The short version", "<p>Google Ads channel prioritization lets you fund chosen channels first and cap others. Anaheim and Orange County advertisers can protect Search budgets, test other networks safely and prepare for the February 2027 change to Search campaigns with the Display Network.</p>")],
     faqs=[("What is Google Ads channel prioritization?", "A control to mark channels as high or low priority so high-priority channels are funded first."),
           ("What is budget allocation?", "A cap on low-priority channels as a maximum percentage of the daily budget."),
           ("Which campaign types get these controls?", "Search, Shopping, Performance Max and Demand Gen."),
           ("Are the controls required?", "No. Google says they're optional."),
           ("What changes in February 2027?", "For Search campaigns with the Display Network on, the current spend allocation setup goes away."),
           ("How do I keep my current setup?", "Google suggests setting the Display Network to Low priority with a 50% allocation."),
           ("Is the budget cap exact?", "Google says it works on a best-effort basis."),
           LOCAL_FAQ],
     links=[AIMODE_ADS, IVT, LINKADS, LSA, LOCAL, AUD],
     sources=["g_channel_priority"],
     visuals=[V.flow(3, "How prioritization works", "From Google's October 14, 2026 post.",
               [("High priority", "Funded first."), ("Low priority", "Gets the rest."),
                ("Cap", "Maximum share of daily budget."), ("Review", "Compare leads by channel.")])],
     secondary=["Google Ads budget allocation", "Search partners control", "Display Network Search campaigns", "Google Ads channel controls"],
     hero_query="Can I control which Google channels my ad budget goes to?"),

# 3 ------------------------------------------------------------------
blog(3, "AI Shopping",
     slug="merchant-center-ai-performance-insights", query="merchant center ai performance insights", kw="Merchant Center AI performance insights",
     eyebrow="Google Shopping", short_title="Merchant Center AI performance insights for retailers",
     title="Merchant Center AI Performance Insights Explained",
     meta="Merchant Center AI performance insights show retailers their share of voice in AI Mode and AI Overviews. What Anaheim and Orange County retailers should do now.",
     h1="Merchant Center AI Performance Insights: See How Shoppers Find You in AI Search",
     answer="Merchant Center AI performance insights, now available in the U.S., Australia, Canada, India and New Zealand, show retailers how their brand and products are discovered in AI Mode and AI Overviews, comparing share of voice with other brands. Google paired them with feed tips such as conversational attributes. Anaheim and Orange County retailers can use them to improve how AI shopping features present their products.",
     takeaways=["Announced September 16, 2026.", "Available in the U.S., Australia, Canada, India and New Zealand.", "Compares your share of voice in AI Mode and AI Overviews.",
                "Feed best practices linked to 5% more conversions on average.", "Conversational attributes add context for AI recommendations."],
     sections=[
      ("What Google announced", "<p>On September 16, 2026, Google shared agentic commerce updates for the holiday season. Among them, AI performance insights in Merchant Center became available to businesses in Australia, Canada, India, New Zealand and the U.S.</p>"),
      ("What AI performance insights show", "<p>Google says the feature gives retailers a view of how their brand and products are discovered by comparing share of voice with other brands across surfaces like AI Mode and AI Overviews, and helps them take action to improve discoverability.</p>"),
      ("Why it matters", "<p>Google notes that shoppers increasingly turn to AI to discover products, compare options and decide what to buy. Knowing whether your products appear in those conversations, and how you compare, is new information for most retailers.</p>"),
      ("Feed best practices", "<p>Google says that, on average, merchants adopting core Merchant Center feed best practices see a 5% increase in conversions the following month. An accurate product feed is the foundation for showing up in AI shopping experiences.</p>"),
      ("Conversational attributes", "<p>Google suggests submitting conversational attributes to add richer context to listings. In testing with lululemon, Google says conversational attributes from the brand were used 50% of the time in relevant product recommendations in AI Mode.</p>"),
      ("Video and loyalty", "<p>Google also suggests adding the video link attribute to power shoppable ad formats, and connecting loyalty data in Merchant Center to show member pricing and perks across Google.</p>"),
      ("Business Agent in YouTube ads", "<p>Google invited U.S. retailers into a Business Agent for YouTube ads beta, which lets viewers ask product questions and get guidance inside YouTube ads.</p>"),
      ("Universal Commerce Protocol updates", "<p>Google says the Universal Commerce Protocol already enables direct checkout for hundreds of thousands of brands, and that merchants using the Merchant Center hub can now enable cart transfer to their site and enhanced checkout testing, rolling out in the U.S. first.</p>"),
      ("What local retailers should do", ol(["Set up or review your Merchant Center account and product feed.", "Fix feed errors and fill in key attributes.",
                                              "Add conversational attributes that describe who each product is for.", "Check AI performance insights for your categories.",
                                              "Keep product pages on your website detailed and current."])),
      ("Local stock too", "<p>Shoppers using AI to research gifts still often buy locally. Keep store hours, stock and pickup options clear on your website and Business Profile so AI research turns into a visit.</p>"),
      ("A worked example", "<p>Imagine a home goods boutique in Newport Beach with a small online store. After reviewing its Merchant Center feed, it fixes missing attributes and adds conversational details such as gift for new homeowners and pairs with our linen line. It then checks AI performance insights monthly to see whether its share of voice in its categories improves.</p>"),
      ("The short version", "<p>Merchant Center AI performance insights show retailers how they're discovered in AI Mode and AI Overviews. Anaheim and Orange County retailers should clean up their feeds, add conversational attributes and check insights regularly.</p>")],
     faqs=[("What are Merchant Center AI performance insights?", "Reports showing how your brand and products are discovered in AI Mode and AI Overviews, with share of voice."),
           ("Where are they available?", "Google says the U.S., Australia, Canada, India and New Zealand."),
           ("What are conversational attributes?", "Extra product details that add context for AI recommendations."),
           ("Do feed best practices help?", "Google says merchants adopting them see 5% more conversions on average the following month."),
           ("What is Business Agent for YouTube ads?", "A beta letting viewers ask product questions inside YouTube ads."),
           ("Is Universal Commerce Protocol checkout available?", "Google says it already powers direct checkout for hundreds of thousands of brands."),
           ("Do small retailers need Merchant Center?", "If they sell products online, it's how products reach Google's shopping features."),
           LOCAL_FAQ],
     links=[PRODUCT, CART, WHEN, LOCAL, AUD],
     sources=["g_holiday_agentic"],
     visuals=[V.flow(3, "Improving AI shopping visibility", "From Google's September 16, 2026 post.",
               [("Feed", "Accurate product data."), ("Attributes", "Conversational context."),
                ("Insights", "Share of voice in AI surfaces."), ("Act", "Improve weak categories.")])],
     secondary=["AI Mode shopping", "Merchant Center share of voice", "conversational attributes", "Google Shopping AI"],
     hero_query="How can I see if my products show up in Google AI Mode?"),

# 4 ------------------------------------------------------------------
blog(4, "Google news",
     slug="google-ads-data-strength-demand-gen", query="google ads data strength", kw="Google Ads data strength",
     eyebrow="Google Ads", short_title="Google Ads data strength and Demand Gen",
     title="Google Ads Data Strength: Why Tracking Matters",
     meta="Google's October Demand Gen drop focuses on Google Ads data strength, enhanced conversions and Data Manager. What Orange County advertisers should do.",
     h1="Google Ads Data Strength: Why Better Tracking Means Better Ad Results",
     answer="Google Ads data strength is about how well your measurement setup feeds campaigns with conversion data. In its October 2026 Demand Gen drop, Google said advertisers who build data strength with Google Tag Gateway see over 20% conversion uplift in Demand Gen on average, and announced a Data Strength Uplift metric. For Anaheim and Orange County advertisers, accurate tracking is the first step to better results.",
     takeaways=["Announced October 13, 2026.", "Google cites over 20% average conversion uplift with Google Tag Gateway in Demand Gen.",
                "A Data Strength Uplift metric is launching in Google Ads.", "Data Manager is expanding to Display & Video 360 and Google Analytics.",
                "Enhanced conversions are coming to Display & Video 360 and Google Analytics."],
     sections=[
      ("What Google announced", "<p>On October 13, 2026, Google's October Demand Gen drop focused on data strength, saying Demand Gen is only as powerful as the quality of the data fueling it. Demand Gen campaigns run across Google's visual surfaces, so better measurement helps them find customers.</p>"),
      ("The headline number", "<p>Google says that, based on internal analysis, advertisers who build their data strength with Google Tag Gateway see, on average, over 20% conversion uplift in Demand Gen campaigns. Google cites its own global performance data from June 2026.</p>"),
      ("The updates", ul(["A Data Strength Uplift metric in Google Ads, showing conversion gains driven by your data setup.",
                          "Data Manager expanding to Display & Video 360 and Google Analytics, to connect and manage first-party data.",
                          "Enhanced conversions coming soon to Display & Video 360 and Google Analytics, for more accurate measurement and bidding."])),
      ("A customer example", "<p>Google says insurance platform The Zebra implemented data strength and achieved a 16% increase in conversion volume and a 19% increase in overall conversion value.</p>"),
      ("What data strength means for small advertisers", "<p>For a local business, data strength starts with basics: the Google tag installed correctly, the right actions tracked as conversions, and Google Ads linked to Analytics. Without these, smart bidding has little to learn from.</p>"),
      ("Track the actions that matter", "<p>Mark real lead actions, such as quote requests, bookings and calls, as key events in Google Analytics, and use them as conversions in Google Ads. Page views and clicks alone don't tell campaigns which visitors became customers.</p>"),
      ("First-party data", "<p>Google points to connecting first-party data, such as customer lists, through Data Manager. Small businesses should only do this in line with their privacy policy and applicable law, and with customers' information handled carefully.</p>"),
      ("Your setup checklist", ol(["Confirm the Google tag fires on every page.", "Define three to five conversion actions that mean real business.",
                                   "Link Google Ads and Google Analytics.", "Ask your developer or agency about enhanced conversions.", "Review conversion counts against real leads monthly."])),
      ("Check the new metric", "<p>When the Data Strength Uplift metric appears in your account, use it to see how much your setup is helping, and fix gaps it highlights.</p>"),
      ("A worked example", "<p>Imagine a solar installer in Irvine running Demand Gen and Search campaigns that only track page views. It marks consultation requests and qualified calls as conversions, links Ads to Analytics and sets up enhanced conversions with its developer. Bidding starts optimizing toward consultations rather than visits, and the company tracks cost per consultation month over month.</p>"),
      ("The short version", "<p>Google Ads data strength means giving campaigns accurate conversion data. Anaheim and Orange County advertisers should fix their tag, track real lead actions, link Ads and Analytics and consider enhanced conversions.</p>")],
     faqs=[("What is Google Ads data strength?", "How well your measurement setup feeds campaigns with conversion data."),
           ("What uplift does Google report?", "Over 20% average conversion uplift in Demand Gen with Google Tag Gateway, based on Google's analysis."),
           ("What is the Data Strength Uplift metric?", "A Google Ads metric showing conversion gains driven by your data setup."),
           ("What is Data Manager?", "A tool for connecting and managing first-party data, expanding to DV360 and Google Analytics."),
           ("Are enhanced conversions coming to Google Analytics?", "Google says they'll soon be available in DV360 and Google Analytics."),
           ("Where should a small business start?", "Correct tagging, real conversion actions and linking Ads with Analytics."),
           ("Does more data mean sharing customer details?", "Only within your privacy policy and the law; handle customer data carefully."),
           LOCAL_FAQ],
     links=[KEYEV, LINKADS, IVT, LOCAL, AUD],
     sources=["g_demandgen_oct"],
     visuals=[V.flow(4, "Building data strength", "Based on Google's October 13, 2026 post.",
               [("Tag", "Google tag on every page."), ("Conversions", "Real lead actions."),
                ("Link", "Ads and Analytics."), ("Enhance", "Enhanced conversions.")])],
     secondary=["Demand Gen data strength", "Google Tag Gateway", "enhanced conversions Google Analytics", "Google Ads conversion tracking"],
     hero_query="Why do my Google Ads need better conversion tracking?"),

# 5 ------------------------------------------------------------------
blog(5, "AI news",
     slug="google-ai-studio-cloud-credits", query="google ai studio cloud credits", kw="Google AI Studio cloud credits",
     eyebrow="AI news", short_title="Claim Google Cloud credits in Google AI Studio",
     title="Google AI Studio Cloud Credits: How to Claim Them",
     meta="Google AI Pro and Ultra subscribers can now claim monthly Google Cloud credits in Google AI Studio. What it means for Orange County businesses building with AI.",
     h1="Google AI Studio Cloud Credits: What Small Businesses Building With AI Should Know",
     answer="Since November 13, 2026, Google AI Pro and Ultra subscribers can claim their monthly Google Cloud credits directly in Google AI Studio and use them for Gemini API usage. Each monthly credit is valid for 12 months and grants stack. For Anaheim and Orange County businesses experimenting with AI tools, it lowers the cost of trying ideas.",
     takeaways=["Announced November 13, 2026.", "Claim credits without leaving Google AI Studio.", "For Google AI Pro and Ultra subscribers.",
                "Each monthly credit is valid for 12 months.", "Credits stack and scale with your plan tier."],
     sections=[
      ("What Google announced", "<p>On November 13, 2026, Google said Google Developer Program Cloud credits are now built into Google AI Studio. Google AI Pro and Ultra subscribers can set up billing, claim monthly credits and build with the Gemini API without leaving the workspace.</p>"),
      ("Who gets credits", "<p>Google says Google AI Pro and Ultra memberships include recurring monthly Google Cloud credits through the Google Developer Program, a no-cost membership across AI Studio, Google Cloud, Firebase, Android and more. An active Developer Program profile is required; AI Studio creates one when you redeem credits.</p>"),
      ("How credits work", ul(["Each monthly credit is valid for 12 months from issue.", "Grants stack month to month.",
                               "Credits can be used for paid-tier models and overages when your subscription quota runs out in AI Studio.", "Upgrading your plan increases your monthly grant."])),
      ("You may already have credits", "<p>Google notes that if you've been a Pro or Ultra subscriber for a few months and have a Developer Program profile, you likely have credits waiting to be claimed.</p>"),
      ("What you can use them for", "<p>Google says credits can go toward Gemini API usage for prompting, building and deploying AI-powered apps from AI Studio, including models like Gemini 4 Carbon when your subscription quota runs out.</p>"),
      ("Why it matters for small businesses", "<p>Many small businesses want to try AI tools, such as a quote estimator, an internal knowledge search or a customer FAQ assistant, but hesitate over API costs. Credits that come with an existing subscription make early experiments cheaper.</p>"),
      ("Ideas worth testing", ol(["A tool that drafts quotes from job details for staff to review.", "An internal search over your policies, price lists and manuals.",
                                  "A system that summarizes customer reviews into themes.", "A draft generator for service page outlines, edited by people.", "Automated summaries of long supplier documents."])),
      ("Keep it safe", "<p>Don't send sensitive customer data to experimental tools without checking terms and privacy settings, and keep a person reviewing anything that reaches customers.</p>"),
      ("Choosing a model", "<p>For most everyday tasks, a fast, lower-cost model such as Gemini 4 Hydrogen is enough. Save frontier models like Carbon for complex tasks, so credits last longer.</p>"),
      ("A worked example", "<p>Imagine a landscaping company in Yorba Linda whose owner already subscribes to Google AI Pro. In AI Studio, the owner claims the waiting credits and builds a simple tool that turns site notes into a draft quote with line items, which the office manager reviews before sending. The credits cover the testing period at no extra cost.</p>"),
      ("The short version", "<p>Google AI Pro and Ultra subscribers can now claim monthly Cloud credits inside Google AI Studio, valid for 12 months and stackable. Anaheim and Orange County businesses can use them to test AI tools cheaply, with people checking the results.</p>")],
     faqs=[("What are Google AI Studio cloud credits?", "Monthly Google Cloud credits for Gemini API usage, now claimable inside AI Studio."),
           ("Who can claim them?", "Google AI Pro and Ultra subscribers with a Google Developer Program profile."),
           ("How long do credits last?", "Each monthly credit is valid for 12 months."),
           ("Do unused credits roll over?", "Yes. Google says grants stack month to month."),
           ("Do I need a Developer Program profile?", "Yes; AI Studio creates one when you redeem credits."),
           ("Can I use credits for Gemini 4 Carbon?", "Google says credits can cover paid-tier models when subscription quota runs out."),
           ("Does upgrading increase credits?", "Yes. Google says upgrading increases the monthly grant."),
           LOCAL_FAQ],
     links=[HYDRO, GEMSEO, SMB, LOCAL, AUD],
     sources=["g_studio_credits"],
     visuals=[V.flow(3, "Claiming credits", "From Google's November 13, 2026 post.",
               [("Subscribe", "Google AI Pro or Ultra."), ("Profile", "Developer Program profile."),
                ("Claim", "Inside AI Studio."), ("Build", "Gemini API usage.")])],
     secondary=["Google Developer Program credits", "Gemini API credits", "Google AI Pro credits", "AI Studio billing"],
     hero_query="Can I get free credits to build with the Gemini API?"),
]

EXTRA = {
"apple-business-connect-now-apple-business": [
 ("Questions owners ask us", "<p>Owners often ask whether they need to set up their Apple Maps listing again. Apple's guide says existing Apple Business Connect users can sign in with the same personal Apple Account, so the starting point is to sign in and review what's there. Another common question is whether Apple Business costs money. Apple's pages describe ads on Maps as a paid option with its own budget; check Apple's current terms for anything else. Owners also ask whether a personal Apple Account is enough. For brand and location management, Apple says yes; a Managed Apple Account unlocks the full feature set, which matters more for businesses that also manage Apple devices.</p>"),
 ("A checklist for multi-location businesses", "<p>If you have several locations in Orange County, sign in and confirm every location appears under the right brand and organizational unit. Check each pin, hours and phone number, and make sure each location has its own cover photo where the locations look different. Assign access to the right people, and confirm Apple's change emails reach someone who will act on them. Then plan monthly showcases and review insights by location to see which ones need attention.</p>")],
"google-ads-channel-prioritization-budget-controls": [
 ("Questions advertisers ask us", "<p>Advertisers often ask whether to turn partner networks back on. For many local service businesses, Search is still the main source of leads, but a capped test of partner networks can show whether they add affordable leads. Another common question is how much to cap. Start small, such as 10% of the daily budget, and adjust once you have a month of lead data. Advertisers also ask whether the February 2027 change affects them. If your Search campaigns include the Display Network, review the settings before then and decide whether to set a priority and allocation that matches what you want.</p>"),
 ("How this fits with Local Services Ads", "<p>Many Orange County service businesses run Local Services Ads alongside Search campaigns. Local Services Ads have their own lead-based model, so these new controls don't apply to them. Compare cost per real lead across both, and use the new controls to keep Search campaign spending focused on the channels that bring the best leads.</p>")],
"merchant-center-ai-performance-insights": [
 ("Questions retailers ask us", "<p>Retailers often ask whether a small store can compete for share of voice with big brands. In niche categories, specific products with detailed, accurate data can stand out, especially when conversational attributes describe exactly who a product suits. Another common question is where to start with feed best practices. Fix errors and warnings in Merchant Center first, then complete titles, descriptions, images, prices and availability. Retailers also ask how often to check insights. Monthly is enough for most small stores, with a closer look before and during the holiday season.</p>"),
 ("Writing conversational attributes", "<p>Think about how a shopper would describe what they need to an AI assistant: a gift for a dad who likes grilling, a waterproof jacket for a rainy trip, a non-toxic toy for a toddler. Describe your products in those terms, accurately and without exaggeration, so AI shopping features can match them to real requests.</p>")],
"google-ads-data-strength-demand-gen": [
 ("Questions advertisers ask us", "<p>Advertisers often ask what Google Tag Gateway is. It's a Google option for serving the Google tag through your own infrastructure; ask your developer or hosting provider whether it suits your site before changing anything. Another common question is whether small accounts benefit from data strength. Yes: smart bidding works best with accurate conversion data, whatever the budget. Advertisers also ask how to check whether tracking works. Submit a test form, watch it appear in Analytics Realtime and in Google Ads conversions, and compare monthly conversion counts with real leads in your records.</p>"),
 ("Common tracking problems", "<p>The problems we see most often in Orange County accounts are simple: the Google tag missing from landing pages built in a separate tool, conversions counted twice because both a thank-you page and a form event are tracked, calls not tracked at all, and old conversion actions left active after a website change. Fixing these usually improves data strength more than any new feature.</p>")],
"google-ai-studio-cloud-credits": [
 ("Questions owners ask us", "<p>Owners often ask whether they need to be developers to use AI Studio. AI Studio is designed for building with Gemini, so basic experiments are approachable, but production tools usually need a developer. Another common question is whether credits are free money. They come with an existing paid Google AI Pro or Ultra subscription, so they're valuable if you already pay for one. Owners also ask what happens when credits run out. Usage is then billed to the linked billing account, so set budgets and alerts in Google Cloud before building anything that runs continuously.</p>"),
 ("Start small and measure", "<p>Pick one task that takes your team time every week, build a simple prototype, and measure the time saved over a month. If it helps, improve it; if not, move on. For small businesses across Anaheim and Orange County, a few small, useful tools are worth more than an ambitious project that never launches.</p>")],
}
for p in PAGES:
    for h, b in EXTRA.get(p["slug"], []):
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

MORE = {
"apple-business-connect-now-apple-business": [
 ("Why Apple Maps deserves attention", "<p>It's easy to focus only on Google, but many customers never leave Apple's apps. When someone taps an address in a text message, accepts a calendar invite with a location or asks Siri for the nearest pharmacy, Apple's place card is what they see. For businesses near Anaheim's resort area, visitors from out of town often rely on whatever map their phone opens by default. An accurate Apple listing with photos, hours and Actions makes sure those customers find the right door at the right time, without extra advertising spend.</p>"),
 ("What to watch for next", "<p>Apple's guide now lives under the Apple Business name, and Apple publishes the date each page was updated. Check the guide when you notice a new option in your account, because features such as showcases, Actions and insights may gain new capabilities. Keep a short record of what you change in Apple Business each month, alongside your Google Business Profile changes, so you can match changes to results in Apple's insights.</p>")],
"google-ads-channel-prioritization-budget-controls": [
 ("Understanding the channels", "<p>Google Search is the main search results page. Search partners are other sites that show Google search ads, and the Google Display Network shows ads on websites and apps. In Performance Max and Demand Gen, Google groups its own surfaces, including Search, YouTube, Maps, Gmail and Discover, as Google channels. Knowing which channel brings which kind of lead is what lets you set priorities sensibly instead of guessing.</p>"),
 ("Reporting to watch", "<p>After setting priorities, review spend, conversions and cost per conversion by channel each week for the first month, then monthly. Look for low-priority channels that bring leads at a similar or better cost; those may deserve more budget. Watch for channels that spend up to their cap without producing leads; those may need a lower cap or a different approach. Keep notes of each change so you can connect it to results later, and remember that lead quality, not just volume, decides what's worth paying for.</p>")],
"merchant-center-ai-performance-insights": [
 ("Why AI shopping changes product data", "<p>When shoppers ask an AI assistant for a gift idea or a product that fits a specific need, the assistant relies on product data to decide what to recommend. Titles, descriptions, images, prices, availability and extra attributes all help it understand what a product is and who it's for. Retailers with thin or inconsistent product data are harder to recommend. That's why Google pairs AI performance insights with feed best practices: the insights show where you stand, and the feed is how you improve it.</p>"),
 ("A holiday feed checklist", "<ul><li>Fix all errors and warnings in Merchant Center.</li><li>Make titles specific: brand, product type, key feature, size or color.</li><li>Use clear, real product images.</li><li>Keep prices and availability accurate daily during the holidays.</li><li>Add conversational attributes for gift-relevant products.</li><li>Add video links where you have product videos.</li><li>Connect loyalty perks if you run a program.</li></ul><p>For Orange County retailers, these steps also help shoppers who search for local stock and pickup.</p>")],
"google-ads-data-strength-demand-gen": [
 ("What Demand Gen campaigns are", "<p>Demand Gen campaigns show ads across Google's visual surfaces to reach people who are browsing and discovering, rather than actively searching. For local businesses, they're often used to build awareness for a new location, a seasonal offer or a service people don't search for until they see it. Because these campaigns rely on Google's systems to find likely customers, the conversion data you provide matters even more than in a simple keyword campaign.</p>"),
 ("How enhanced conversions help", "<p>Enhanced conversions improve measurement by securely using first-party information that customers provide, such as an email address on a form, to match conversions more accurately. Google says they're coming to Display & Video 360 and Google Analytics. For small advertisers already using Google Ads, ask your developer or agency whether enhanced conversions are set up, and make sure your privacy policy explains how you use customer information. Better matching gives bidding a clearer picture of which ads lead to real customers.</p>")],
"google-ai-studio-cloud-credits": [
 ("What Google AI Studio is", "<p>Google AI Studio is Google's workspace for trying Gemini models, testing prompts and building AI-powered apps with the Gemini API. Google's post mentions testing prompts with models like Gemini 4 Carbon, generating videos and building apps. For a small business, it's a place to prototype an idea quickly before deciding whether it's worth building properly.</p>"),
 ("Budgets and billing", "<p>Because AI Studio now links billing and credits in one place, it's easier to see what you're spending. Set a budget alert in Google Cloud so you know when credits are running low, and keep experimental tools limited until you're confident in their usefulness. For businesses in Anaheim and across Orange County trying AI for the first time, a clear budget and a single owner for each experiment prevent surprises and make it easier to decide what to keep.</p>"),
 ("Questions to ask before building", "<ul><li>What task will this tool save time on, and how much?</li><li>Who will check its output before it reaches customers?</li><li>What data will it use, and is any of it sensitive?</li><li>Which model is good enough for the job?</li><li>How will we know after a month whether it's worth keeping?</li></ul>")],
}
for p in PAGES:
    for h, b in MORE.get(p["slug"], []):
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

LAST = {
"apple-business-connect-now-apple-business": ("How Apple and Google listings work together", "<p>Think of Apple Business and Google Business Profile as two front doors to the same business. Each has its own tools, review processes and insights, but customers expect the same name, address, phone number, hours and website on both. Make changes in both on the same day, such as holiday hours, a new phone number or a move, and keep your website as the source both can match. Review both sets of insights each month side by side. For most Orange County businesses, Google will bring more traffic, but Apple Maps users are often ready to visit, call or book, so the effort pays off.</p>"),
"google-ads-channel-prioritization-budget-controls": ("Where to find the settings", "<p>Google says the controls are rolling out at the account and campaign levels and also apply to shared budgets, over the next months, so they may not appear in every account yet. When they do, review each campaign's network settings, decide which channels matter most for your goals and set priorities accordingly. If you work with an agency, ask how they plan to use the controls and how they'll report results by channel. For small budgets, simple settings reviewed regularly beat complicated setups that nobody checks. Google points to its Help Center for details as the features roll out.</p>"),
"merchant-center-ai-performance-insights": ("Questions to ask about your product data", "<p>Before the holiday rush, ask a few simple questions. Would a shopper understand each product from its title alone? Do descriptions say who the product is for and what problem it solves? Are images clear and current? Do prices and stock match your store? Do your best-selling products have the richest data? If the answer to any is no, fix your top products first, since they matter most to sales. For Orange County retailers with both a shop and an online store, accurate product data serves shoppers whether they buy online or visit in person, and it gives AI shopping features something solid to recommend. Revisit the same questions after the holidays, when returns and new stock change what's accurate, and keep improving the products that sell best year-round. Small, regular improvements to product data compound over time, just as they do for your website and listings.</p>"),
"google-ads-data-strength-demand-gen": ("A month-by-month plan", "<p>In the first month, audit tracking: confirm the tag fires everywhere, list your conversion actions, remove duplicates and link Ads with Analytics. In the second month, add missing lead actions such as calls or bookings and ask about enhanced conversions. In the third month, compare conversion counts with real leads and adjust bidding goals to the actions that matter most. Watch the new Data Strength Uplift metric when it appears in your account. This steady approach suits small advertisers in Anaheim and across Orange County better than trying to change everything at once, and it gives each change time to show its effect before the next one. Keep a simple log of every tracking change with the date, so if conversion numbers jump or drop suddenly you can tell whether it's real performance or a measurement change. Share the log with anyone who manages your ads, and review it whenever results change unexpectedly. Good data is never finished; it needs checking every time your website or forms change.</p>"),
"google-ai-studio-cloud-credits": ("Who should own AI experiments", "<p>Give each experiment a single owner who understands the task it's meant to help with, not just the technology. That person decides what good output looks like, checks results, tracks time saved and decides after a month whether to keep it. Small businesses often start AI projects with enthusiasm and then abandon them because nobody owns them. With credits making experiments cheaper, clear ownership is what turns them into tools your team actually uses. Write down the goal, the owner and the review date before you start, and treat the first month as a test rather than a commitment. If an experiment works, document how it's used, who maintains it and what it costs each month, so it keeps running smoothly when the person who built it is busy or away. If it doesn't, write down why, so the next idea starts from what you learned rather than from scratch. Over a year, a handful of small, well-chosen tools can save a team many hours each month and free people for work customers notice.</p>"),
}
for p in PAGES:
    if p["slug"] in LAST:
        h, b = LAST[p["slug"]]
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

if __name__ == "__main__":
    save_all(PAGES)
