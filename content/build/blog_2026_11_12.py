"""Blog posts for 2026-11-12 (5 posts). Every fact is checked at the linked Google source on 2026-11-12."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_11  # noqa: F401  (SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SRC.update({
    "g_hydrogen_search": {"title": "Google: Google Search gets a major upgrade with Gemini 4 Hydrogen (Nov 12, 2026)",
                          "url": "https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/"},
    "g_ivt_card": {"title": "Google Ads & Commerce blog: We're introducing a new transparency tool for invalid traffic in Google Ads (Nov 12, 2026)",
                   "url": "https://blog.google/products/ads-commerce/invalid-traffic-overview-google-ads/"},
    "g_ivt_help": {"title": "Google Ads Help: About invalid traffic", "url": "https://support.google.com/google-ads/answer/2549113?hl=en"},
    "g_cdn": {"title": "Google Search Central blog: Moving to a CDN without overwhelming your origin (or blocking Googlebot) (Nov 11, 2026)",
              "url": "https://developers.google.com/search/blog/2026/11/crawling-cdn"},
    "g_carplay": {"title": "Google: Talk it through with Gemini, now on Apple CarPlay (Nov 11, 2026)",
                  "url": "https://blog.google/innovation-and-ai/products/gemini-app/gemini-on-apple-carplay/"},
    "g_gbp_gemini": {"title": "Google Business Profile Help: Manage your Business Profile on Google with the Gemini web app",
                     "url": "https://support.google.com/business/answer/17142585?hl=en"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")
MODE = L("how to optimize for Google AI Mode", "how-to-optimize-for-google-ai-mode")
AIO = L("how to show up in Google AI Overviews", "how-to-show-up-in-google-ai-overviews")
TRACK = L("how to track AI visibility", "how-to-track-ai-visibility")
GEMSEO = L("Gemini SEO", "gemini-seo")
CRAWLERS = L("AI crawler user agents", "ai-crawler-user-agents")
ROBOTS = L("robots.txt for AI crawlers", "robots-txt-for-ai-crawlers")
CWV = L("Core Web Vitals for local businesses", "core-web-vitals-for-local-businesses")
LSA = L("Google Local Services Ads vs SEO", "google-local-services-ads-vs-seo")
CHECK = L("local SEO checklist", "local-seo-checklist")
GBP = L("Google Business Profile optimization", "google-business-profile-optimization-orange-county")
GBP_PERF = L("Google Business Profile performance insights", "google-business-profile-performance")
GBP_LINKS = L("Google Business Profile booking and order links", "google-business-profile-links")
GBP_USERS = L("Google Business Profile owners and managers", "google-business-profile-owners-and-managers")
REPLY = L("how to respond to Google reviews", "how-to-respond-to-google-reviews")


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


PAGES = [
# 1 ------------------------------------------------------------------
blog(1, "Google AI Search",
     slug="gemini-4-hydrogen-google-search-upgrade", query="gemini 4 hydrogen google search", kw="Gemini 4 Hydrogen",
     eyebrow="Google Search", short_title="Gemini 4 Hydrogen comes to Google Search",
     title="Gemini 4 Hydrogen in Google Search: What Changes",
     meta="Google brought Gemini 4 Hydrogen to Search for all users on November 12, 2026. What it changes and what Anaheim and Orange County businesses should do.",
     h1="Gemini 4 Hydrogen Comes to Google Search: What It Means for Local Businesses",
     answer="On November 12, 2026, Google brought Gemini 4 Hydrogen to Google Search globally for all users, calling it the biggest model upgrade to Search yet. Google says it better understands complex questions, runs a stronger query fan-out that links to a broader range of sites, and gives more visual answers. For Anaheim and Orange County businesses, clear, specific pages are more likely to be found and linked.",
     takeaways=["Announced November 12, 2026 by Google Search.", "Available globally in Google Search for all users.",
                "Google calls it the biggest model upgrade to Search yet.", "Improved query fan-out connects people to a broader range of links.",
                "Answers include more images, tables and custom tools."],
     sections=[
      ("What Google announced", "<p>On November 12, 2026, Robby Stein, Vice President of Product for Google Search, announced that Gemini 4 Hydrogen is now available globally in Google Search for all users. Google describes it as the biggest model upgrade to Search yet, delivering more helpful, visual and intuitive responses. Unlike some earlier model launches that started with paid subscribers, this one reaches everyone who uses Search.</p>"),
      ("Better understanding of intent", "<p>Google says Search can now handle more nuanced and complicated questions. People can ask in their natural flow of thought, including questions with multiple parts, hard-to-understand typos or highly specific requests. With deeper instruction following and tool calling, Google says Search more precisely follows what someone wants and addresses each part of the question.</p>"),
      ("Improved query fan-out and linking", "<p>Query fan-out is the technique Google uses to break a question into related subtopics and search them at the same time. Google says Hydrogen's reasoning supercharges this, conducting simultaneous queries across all the relevant subtopics and connecting people to a broader range of helpful links than before. In Google's words, it helps people find sites they previously might not have discovered.</p>"),
      ("More visual responses", "<p>Google says answers are now more adaptive, visual and easy to scan, with more images, structured responses, comparison tables and custom tools built for the person asking, at the speed of Search. That means a question about options or prices is more likely to be answered with a table or a visual summary than a block of text.</p>"),
      ("Richer language understanding", "<p>Google says people will get more nuanced and helpful responses in every supported AI Mode language. In a region as diverse as Orange County, where many customers search in Spanish, Vietnamese, Korean and other languages, that matters for businesses serving those communities.</p>"),
      ("Why fan-out matters for small businesses", "<p>When Search runs many related queries for one question, each subtopic is a chance for a different page to be cited. A customer in Anaheim asking which plumbers handle tankless water heaters, offer weekend service and give upfront pricing is asking three questions at once. A business with a clear page on each of those points has more ways to be found than one with a single general services page.</p>"),
      ("What we don't know", "<p>Google has not said how Hydrogen changes which businesses are shown, or how links are chosen, and we will not guess. What Google has said is that it connects people to a broader range of links and better understands specific requests. The sensible response is to make your information easy to understand and easy to link to.</p>"),
      ("How to prepare your website", ol(["Give each main service its own page that answers what, where, how long and roughly how much.",
                                          "Answer the multi-part questions customers actually ask, in plain language.",
                                          "Use simple tables for prices, options or comparisons where they help.",
                                          "Add real photos of your work, premises and team with descriptive text.",
                                          "Keep your business name, address, phone and hours identical everywhere."])),
      ("Visual answers reward real visuals", "<p>As answers include more images and tables, original photos and clearly structured information become more useful. Stock photos tell Search nothing about your business. A photo of a finished kitchen in Irvine or a menu board in Fullerton does.</p>"),
      ("Your Business Profile still matters", "<p>Local questions draw heavily on business listings. Make sure your Google Business Profile has the right categories, services, attributes and hours, and that it matches your website. When an answer compares local options, accurate profile details help you appear correctly.</p>"),
      ("A worked example", "<p>Imagine someone in Garden Grove searching for a dentist open Saturdays who takes their insurance, speaks Vietnamese and offers payment plans. With improved fan-out, Search can look for each part. A practice whose site states Saturday hours, lists accepted insurance, mentions Vietnamese-speaking staff and explains payment plans gives Search a specific answer for every part. A practice that only lists general dentistry gives it far less to work with.</p>"),
      ("Measuring the effect", "<p>Search Console's performance reports, including the Generative AI performance report for AI features, are the place to watch. Compare impressions and clicks before and after November 12, and look at which pages gain visibility. Give it a few weeks before drawing conclusions.</p>"),
      ("Don't chase every model release", "<p>Model upgrades will keep coming. The pages that do well tend to be the same each time: specific, accurate, well organized and trustworthy. Improving those basics is more reliable than reacting to each announcement.</p>"),
      ("The short version", "<p>Gemini 4 Hydrogen is now in Google Search for everyone, with better understanding of complex questions, broader linking through query fan-out and more visual answers. For Anaheim and Orange County businesses, the best preparation is clear, specific pages, real visuals and consistent business details.</p>")],
     faqs=[("What is Gemini 4 Hydrogen in Google Search?", "Google's model upgrade to Search, announced November 12, 2026, which Google calls the biggest model upgrade to Search yet."),
           ("Who can use it?", "Google says it is available globally in Google Search for all users."),
           ("What is query fan-out?", "A technique where Search runs simultaneous queries across the relevant subtopics of a question; Google says Hydrogen improves it."),
           ("Will it send traffic to more websites?", "Google says it connects people to a broader range of helpful links, including sites they might not have discovered."),
           ("What do answers look like now?", "Google says more images, structured responses, comparison tables and custom tools."),
           ("Does it work in other languages?", "Google says responses are more nuanced across all supported AI Mode languages."),
           ("What should a local business change?", "Make service pages specific, answer multi-part questions, use real photos and keep details consistent."),
           LOCAL_FAQ],
     links=[MODE, AIO, GEMSEO, TRACK, LOCAL, AUD],
     sources=["g_hydrogen_search"],
     visuals=[V.flow(5, "How a multi-part question is handled", "Based on Google's November 12, 2026 announcement.",
               [("Question", "A nuanced, multi-part request."), ("Intent", "Search works out each part."),
                ("Fan-out", "Simultaneous queries across subtopics."), ("Answer", "Visual response with a broader range of links.")])],
     secondary=["Gemini 4 Hydrogen Search", "Google Search model upgrade", "query fan-out", "AI Mode Gemini 4 Hydrogen"],
     hero_query="What does the Gemini 4 Hydrogen upgrade to Google Search mean for my business?"),

# 2 ------------------------------------------------------------------
blog(2, "Google news",
     slug="google-ads-invalid-traffic-card", query="google ads invalid traffic card", kw="Google Ads invalid traffic",
     eyebrow="Google Ads", short_title="Google Ads' new Invalid Traffic card",
     title="Google Ads Invalid Traffic Card: What It Shows",
     meta="Google Ads now shows invalid traffic savings and credits in a new Overview card. What it means for Anaheim and Orange County advertisers and lead quality.",
     h1="Google Ads Invalid Traffic Card: See What Google Filters and Credits",
     answer="On November 12, 2026, Google began rolling out the Invalid Traffic Overview Card in Google Ads, which shows advertisers the amount saved by filtering invalid traffic and the credits issued for invalid activity found later. Google says it doesn't charge for invalid traffic. For Anaheim and Orange County advertisers, the card adds transparency, but lead quality still needs your own safeguards.",
     takeaways=["Announced November 12, 2026.", "Shows estimated savings and credited cost for invalid traffic.",
                "Google says it doesn't charge for invalid traffic.", "Google says it reduced exposure to invalid leads by an average of 30% so far in 2026.",
                "Lead form protection is still the advertiser's job."],
     sections=[
      ("What Google announced", "<p>On November 12, 2026, Keerat Sharma, Vice President and General Manager of Ads Privacy and Safety at Google, announced the Invalid Traffic Overview Card in Google Ads. Google says it gives advertisers front-end transparency into how it protects their campaigns. For the first time, businesses can see both the amount saved and the credits Google automatically provides for invalid activity.</p>"),
      ("What invalid traffic is", "<p>Google's help page defines invalid traffic as traffic that doesn't represent genuine interest in your business. Its examples include non-human traffic from bots and automated software, accidental clicks caused by poor ad placement, fraudulent placements such as clickjacking and ad stacking, and intentional clicks from people with no genuine interest, such as competitors trying to raise your spend. Google notes the list isn't exhaustive.</p>"),
      ("You don't pay for it", "<p>Google says it doesn't charge for invalid traffic. Invalid activity detected before the end of the billing cycle is removed from billing and campaign reports automatically. If it is detected after you were billed, Google issues a credit where appropriate and possible, shown as an Invalid activity adjustment on your invoice.</p>"),
      ("What the card shows", "<p>Google's help page says the card, on the Overview page in the Campaigns menu, highlights two metrics for your selected date range: Estimated savings, the cost saved by automated protections, and Credited cost, the amount credited back for past invalid activity found after the billing period ended. Select View details for daily graphs, a breakdown by campaign and links to invoices with credits.</p>"),
      ("It's rolling out gradually", "<p>Google notes the Invalid traffic card is rolling out gradually and may not be in your account yet. If you don't see it, check again over the coming weeks.</p>"),
      ("Other places to check", ul(["Add the Invalid clicks column to your campaigns table to see clicks Google filtered out.",
                                    "Check Billing, Summary, Adjustments for Invalid activity credits.",
                                    "Use the Invalid Activity Credit Report in Report Editor to see metrics adjusted for credits."])),
      ("Why filtered clicks and credits differ", "<p>Google explains that you may see many filtered invalid clicks but small credit amounts, and that this is normal. The invalid clicks column shows traffic filtered before you were billed; credits cover invalid activity found after the billing cycle closed. The two numbers measure different things.</p>"),
      ("Invalid leads: a shared job", "<p>Google says that so far in 2026 it has reduced advertiser exposure to invalid leads by an average of 30% through system upgrades. But its help page is clear that its filters can't block traffic from your site, and that some real people submit fake details. Lead quality is a shared effort: Google filters invalid traffic, and you protect your forms.</p>"),
      ("Protect your lead forms", ol(["Choose Leads as the campaign objective and optimize for goals such as qualified lead or booked appointment.",
                                     "Secure forms with tools like reCAPTCHA and server-side validation.",
                                     "Consider a double opt-in that confirms a real email address.",
                                     "Set up the Google tag and enhanced conversions to measure real customer actions."])),
      ("If you suspect problems", "<p>Google says you can request an investigation into invalid traffic within the last 60 days. Prepare your 10-digit customer ID, the exact dates, the campaign and ad group names, any suspicious keywords and your web server logs before you submit.</p>"),
      ("What this means for local advertisers", "<p>For a roofer in Anaheim or a law firm in Santa Ana spending on Search ads, the card makes it easier to see that Google is filtering junk clicks. It doesn't tell you whether your leads turn into customers. Compare ad leads against your own records of booked jobs and signed clients.</p>"),
      ("A worked example", "<p>Imagine an HVAC company in Orange that notices a run of form fills with fake phone numbers. The Invalid traffic card shows savings and a small credit, so Google is filtering some activity, but the fake forms keep arriving. The company adds reCAPTCHA and server-side checks to the form, switches its conversion goal to booked appointments and imports which leads became jobs. Fake submissions fall and the campaign optimizes toward real customers.</p>"),
      ("Ads and organic work together", "<p>Paid search works best alongside a strong organic presence. A complete Business Profile, clear service pages and genuine reviews improve the experience for people who click your ads and give you visibility that doesn't stop when the budget does.</p>"),
      ("The short version", "<p>Google Ads now shows invalid traffic savings and credits in an Overview card. You aren't charged for invalid traffic, but you still need to protect your lead forms and measure real outcomes. Anaheim and Orange County advertisers should check the card, secure their forms and track leads to sales.</p>")],
     faqs=[("What is the Google Ads invalid traffic card?", "An Overview page card showing estimated savings from invalid traffic protection and credits for past invalid activity."),
           ("Do I pay for invalid clicks?", "No. Google says it doesn't charge for invalid traffic; later detections are credited where appropriate and possible."),
           ("Why can't I see the card?", "Google says it is rolling out gradually and may not be available in your account yet."),
           ("Why are credits smaller than filtered clicks?", "Filtered clicks are removed before billing; credits only cover activity found after billing."),
           ("Does Google stop fake leads?", "Its filters can't block traffic from your site, so protect forms with tools like reCAPTCHA and validation."),
           ("How far back can I request an investigation?", "Google says investigations cover activity within the last 60 days."),
           ("How much did Google reduce invalid leads?", "Google says by an average of 30% so far in 2026."),
           LOCAL_FAQ],
     links=[LSA, TRACK, CHECK, LOCAL, AUD],
     sources=["g_ivt_card", "g_ivt_help"],
     visuals=[V.flow(3, "Where invalid traffic is handled", "From Google's announcement and help page.",
               [("Before billing", "Filtered from metrics and billing."), ("After billing", "Credited as Invalid activity."),
                ("Card", "Estimated savings and credited cost."), ("Your site", "Protect forms and measure real leads.")])],
     secondary=["invalid clicks Google Ads", "Google Ads click fraud", "invalid activity credit", "Google Ads fake leads"],
     hero_query="Am I paying for fake clicks on my Google Ads?"),

# 3 ------------------------------------------------------------------
blog(3, "Google Search",
     slug="moving-to-a-cdn-googlebot-crawling", query="moving to a cdn googlebot", kw="moving to a CDN",
     eyebrow="Technical SEO", short_title="Moving to a CDN without blocking Googlebot",
     title="Moving to a CDN: Google's Advice on Crawling",
     meta="Google explains why crawling can spike after moving to a CDN and how blanket bot protection can block Googlebot. What Orange County site owners should do.",
     h1="Moving to a CDN Without Overwhelming Your Server or Blocking Googlebot",
     answer="Google's Search Central blog explains that after moving to a CDN, faster responses can make Google crawl more, while the CDN's empty cache sends those requests to your origin server. Turning on blanket bot protection can then block Googlebot and drop pages from Search. Anaheim and Orange County site owners moving to a CDN should allow verified bots, pre-warm caches and use 429 or 503 briefly if needed.",
     takeaways=["Published on Search Central on November 11, 2026.", "Fast CDN responses can raise Google's crawl rate.",
                "A cold cache sends first requests to your origin server.", "Blanket bot protection and CAPTCHAs can block Googlebot.",
                "Allow verified bots and pre-warm caches."],
     sections=[
      ("What Google published", "<p>On November 11, 2026, Google's Search Central blog published a post on moving to a CDN, a content delivery network that serves your site from servers closer to visitors. Google says a CDN can be a major upgrade, lowering latency and shielding your origin server from heavy traffic, but that the transition phase can be a bit weird.</p>"),
      ("Why crawling can spike", "<p>Google explains that its crawlers set a crawl capacity limit, also called hostload, based on how your server responds. Slower responses decrease the crawl rate; fast, stable responses let it rise when there is crawl demand. When your DNS points to a fast CDN, response times drop, and to Google it looks like your server got a major hardware upgrade, so crawlers gradually ramp up.</p>"),
      ("The cold cache problem", "<p>A new CDN starts with an empty, or cold, cache. The first request for each URL at an edge location is a cache miss, so the CDN fetches it from your origin server. Only later requests are served from the edge. Google points out that people cluster around popular pages that warm up quickly, while crawlers explore your whole URL inventory, so many crawler requests pass straight through to your origin at first.</p>"),
      ("Blanket bot protection goes too far", "<p>Seeing a surge of automated requests, admins are tempted to turn on blanket bot protection. Google warns that without exemptions these rules treat all automated traffic the same. When a CDN or web application firewall challenges requests with a CAPTCHA, Google's crawlers fail. Google says crawlers then back off, and pages and shopping listings begin to drop out of Search.</p>"),
      ("Google's three recommendations", ol(["If you need to block bots, allow verified bots in your CDN and firewall settings, or target specific unwanted bots with robots.txt or rules rather than blocking all automated clients.",
                                             "Pre-warm caches by fetching your highest-traffic pages, upcoming peak pages and most frequently crawled URLs through the CDN at a controlled pace before switching all traffic.",
                                             "If crawling still overloads your origin, return 429 or 503 status codes for a short window, a few hours or 1 to 2 days at most."])),
      ("Identifying Google's crawlers", "<p>Google notes you can identify its crawlers using Google's published IP ranges, and that most major CDNs and firewalls have a built-in toggle or managed rule to allow known or verified bots. Use that instead of trusting any request that simply claims to be Googlebot.</p>"),
      ("Don't forget AI crawlers", "<p>The same firewall rules decide whether other crawlers can read your site, including those used by AI assistants. Decide which you want to allow, using robots.txt and verified-bot settings, rather than letting a blanket rule decide for you. Blocking everything can remove you from places customers now look for recommendations.</p>"),
      ("Who this affects locally", "<p>Many small business sites in Orange County sit behind a CDN or security service without the owner realizing it, often set up by a host or developer. If your host turns on bot protection during an attack or a site move, check that Google can still crawl your site.</p>"),
      ("How to check Googlebot can reach you", ul(["Use URL Inspection in Search Console to test a live URL.", "Check the Crawl Stats report for rising errors or falling requests.",
                                                  "Look for 403 responses or challenge pages served to crawlers in your CDN logs.", "Confirm verified bots are allowed in your firewall settings."])),
      ("A worked example", "<p>Imagine an online store in Irvine that moves to a CDN before the holiday season. Server load jumps, so the developer switches on the CDN's strictest bot mode. Within days, product pages start disappearing from Search. The fix is to allow verified bots, pre-warm the cache with the top product and category pages, and use a temporary 503 only if the origin truly struggles. Pages return as Google crawls them again.</p>"),
      ("Plan the move", "<p>Before moving to a CDN, list your most important and most crawled URLs, check your firewall's verified-bot option, and schedule the switch for a quieter period. Monitor server load and Search Console for the first few weeks.</p>"),
      ("Speed still helps", "<p>Once caches are warm, a CDN can make your site faster for visitors, which helps user experience and Core Web Vitals. The aim is to get those benefits without a rough transition.</p>"),
      ("The short version", "<p>After moving to a CDN, Google may crawl faster while the cache is still cold, so your origin carries the load. Don't block all bots: allow verified ones, pre-warm caches and use 429 or 503 only briefly. Anaheim and Orange County site owners should check Googlebot can still reach their pages after any security change.</p>")],
     faqs=[("Why does crawling increase after moving to a CDN?", "Google says faster responses signal healthy infrastructure, so its crawl rate can rise."),
           ("Why is my origin server still busy?", "A new CDN's cache is cold, so first requests for each URL go to the origin."),
           ("Can bot protection block Googlebot?", "Yes. Google says crawlers fail CAPTCHA challenges and pages can drop out of Search."),
           ("How do I allow Google's crawlers?", "Use your CDN or firewall's verified-bot setting; Google publishes its IP ranges."),
           ("What does pre-warming a cache mean?", "Fetching important URLs through the CDN at a controlled pace before switching all traffic."),
           ("When should I use 429 or 503?", "Google says briefly, a few hours or 1 to 2 days at most, if crawling overloads your origin."),
           ("Should I block all bots?", "No. Target specific unwanted bots instead of blocking all automated clients."),
           LOCAL_FAQ],
     links=[CWV, CRAWLERS, ROBOTS, CHECK, LOCAL, AUD],
     sources=["g_cdn"],
     visuals=[V.flow(2, "Why crawling spikes after a CDN move", "From Google's November 11, 2026 post.",
               [("Faster", "CDN responses look like a healthy server."), ("More crawling", "Crawl rate ramps up."),
                ("Cache miss", "First requests go to the origin."), ("Fix", "Allow verified bots, pre-warm caches.")])],
     secondary=["CDN Googlebot", "CDN crawl rate", "bot protection blocking Googlebot", "CDN migration SEO"],
     hero_query="Will moving my website to a CDN affect Google crawling?"),

# 4 ------------------------------------------------------------------
blog(4, "AI assistants",
     slug="gemini-apple-carplay-local-business", query="gemini apple carplay", kw="Gemini on Apple CarPlay",
     eyebrow="AI news", short_title="Gemini arrives on Apple CarPlay",
     title="Gemini on Apple CarPlay: What Local Businesses Gain",
     meta="Gemini Live is rolling out on Apple CarPlay for iPhone users. What hands-free AI in the car means for Anaheim and Orange County businesses customers drive to.",
     h1="Gemini on Apple CarPlay: Why Hands-Free AI in the Car Matters for Local Businesses",
     answer="On November 11, 2026, Google began rolling out Gemini on Apple CarPlay globally to all Gemini users on iOS, bringing hands-free Gemini Live conversations to the car's display. Google's examples include asking for local recommendations such as a quick lunch spot. For Anaheim and Orange County businesses, more people will ask an AI assistant where to go while driving, so accurate listings matter.",
     takeaways=["Announced November 11, 2026.", "Rolling out globally to all Gemini users on iOS.", "Follows Android Auto and cars with Google built-in.",
                "Google's examples include asking for local spots and landmarks.", "Conversations sync to the Gemini app on iPhone."],
     sections=[
      ("What Google announced", "<p>On November 11, 2026, Google announced that the Gemini app is now on Apple CarPlay. Following its rollout on Android Auto and cars with Google built-in, iPhone users can now have natural, free-flowing conversations with Gemini Live from their car's display, hands-free. Google says it is rolling out globally to all Gemini users on iOS in every supported Gemini Live language.</p>"),
      ("How it works", "<p>Drivers tap the Gemini icon on the CarPlay screen or side rail, then pick up a recent chat or start a new one. Google says people can talk back and forth at their own pace, interrupting to add a detail, changing the subject, or pausing to focus on an exit. Google designed it as a conversational driving companion that minimizes distraction.</p>"),
      ("What people can ask", ul(["What's on the calendar and when to leave for the next appointment.", "A daily brief and summaries of unread emails, through Gmail and Google Calendar.",
                                  "Recommendations near where they are heading, from a quick lunch spot to the story behind a landmark.", "Practice for a presentation or a talk through a complex topic."])),
      ("Local recommendations in the car", "<p>Google's own example is a driver asking for a quick lunch spot in a downtown area that is easy to get in and out of. That is a local search, spoken, with specific conditions. For restaurants, cafes and shops in Anaheim and across Orange County, this is the kind of question that turns into a visit within minutes.</p>"),
      ("Why commutes matter", "<p>Google notes that for millions of people the daily commute averages about an hour behind the wheel. Southern California drivers know this well. That is a lot of time when people can now ask an AI assistant for suggestions without picking up their phone.</p>"),
      ("What helps you get recommended", "<p>Google hasn't said how Gemini picks local suggestions, and we won't guess. But spoken questions often include conditions such as open now, easy parking, quick service or family friendly. Businesses whose public information covers those details clearly give an assistant something concrete to match.</p>"),
      ("Get your details right", ol(["Keep hours, including special and holiday hours, accurate on your Business Profile.",
                                      "Fill in attributes such as parking, accessibility, outdoor seating and payment options.",
                                      "Describe what makes your location convenient: parking, drive-through, quick service.",
                                      "Make sure your website states the same details in plain language.",
                                      "Keep reviews coming and reply to them."])),
      ("Getting started", "<p>Google says to update to the latest Gemini app on iPhone, enable microphone permissions and use Gemini Live on the phone at least once. The next time the phone connects to the car, tap the Gemini icon on the CarPlay display.</p>"),
      ("Conversations follow you", "<p>Google says CarPlay conversations sync automatically with the Gemini app on iPhone, so summaries, notes and brainstorms are waiting in the chat history when you park. A recommendation heard in the car can be looked up again later.</p>"),
      ("Some features have limits", "<p>Google notes that the Daily Brief feature must be enabled first, and that certain personalization features, including Daily Brief, aren't available to users under 18 or in the European Economic Area and Nigeria.</p>"),
      ("A worked example", "<p>Imagine a family driving to Anaheim for the day who ask Gemini for a quick, kid-friendly lunch spot near the Convention Center with easy parking. A cafe whose profile lists its hours, family-friendly attributes and parking, and whose website mentions quick service and a parking lot, gives the assistant clear details to match. One with missing hours and no attributes leaves it guessing.</p>"),
      ("Using it in your own business", "<p>Owners who drive between jobs, such as contractors and mobile services, can use Gemini on CarPlay to hear a daily brief, catch up on emails and prepare for meetings hands-free, as Google describes. Keep safety first and use it the way Google intends: hands on the wheel, eyes on the road.</p>"),
      ("The short version", "<p>Gemini on Apple CarPlay brings hands-free AI conversations to iPhone users' cars, including local recommendations. For Anaheim and Orange County businesses, accurate hours, attributes and clear details are what help an assistant suggest you to drivers nearby.</p>")],
     faqs=[("Is Gemini available on Apple CarPlay?", "Yes. Google says it is rolling out globally to all Gemini users on iOS from November 11, 2026."),
           ("What can Gemini do in the car?", "Hands-free conversations with Gemini Live, including calendar, email summaries, local recommendations and brainstorming."),
           ("How do I start using it?", "Update the Gemini app, enable microphone permissions, use Gemini Live once on your phone, then tap the icon on CarPlay."),
           ("Do car conversations save?", "Google says they sync automatically to the Gemini app on your iPhone."),
           ("Was Gemini already in other cars?", "Yes. Google says it followed the rollout on Android Auto and cars with Google built-in."),
           ("How can a business get recommended by Gemini?", "Google hasn't said how suggestions are chosen; accurate hours, attributes and clear details help."),
           ("Is Daily Brief available everywhere?", "No. Google says it isn't available to users under 18 or in the EEA and Nigeria."),
           LOCAL_FAQ],
     links=[GEMSEO, GBP, L("Google Business Profile attributes", "google-business-profile-attributes"), TRACK, LOCAL, AUD],
     sources=["g_carplay"],
     visuals=[V.flow(3, "From a spoken question to a visit", "Using Google's example of a lunch recommendation.",
               [("Ask", "Driver asks Gemini Live hands-free."), ("Match", "Conditions like quick and easy parking."),
                ("Suggest", "Gemini recommends places."), ("Visit", "Accurate details turn into a stop.")])],
     secondary=["Gemini CarPlay", "Gemini Live CarPlay", "AI assistant in the car", "Gemini app iPhone car"],
     hero_query="Can drivers ask Gemini for local restaurant recommendations on CarPlay?"),

# 5 ------------------------------------------------------------------
blog(5, "AI assistants",
     slug="google-business-profile-gemini-web-app", query="google business profile gemini", kw="Google Business Profile in Gemini",
     eyebrow="Google Business Profile", short_title="Manage your Business Profile in Gemini",
     title="Google Business Profile in Gemini: How to Use It",
     meta="You can now manage your Google Business Profile in the Gemini web app: hours, reviews, posts and insights. Requirements and tips for Orange County owners.",
     h1="How to Manage Your Google Business Profile in Gemini",
     answer="Google now lets owners and managers manage their Google Business Profile in Gemini by connecting it to the Gemini web app. You can update hours and links, draft review replies, create posts, summarize reviews and check performance by asking in plain language. You must manage only one verified profile, be 18 or over and use a personal Google Account. It suits many single-location Anaheim and Orange County businesses.",
     takeaways=["Connect Google Business Profile to the Gemini web app.", "Update details, draft review replies and create posts by asking.",
                "Check performance metrics and search keywords.", "Only for people managing one verified profile.", "A business notebook adds proactive suggestions."],
     sections=[
      ("What Google offers", "<p>Google's Business Profile help center says you can now manage your Business Profile conversationally and access your business insights in the Gemini web app. Once connected, Gemini can help you update your profile, engage with customers, analyze reviews and access performance data.</p>"),
      ("Who can use it", ul(["Owners or managers of only one verified Business Profile.", "People 18 or over.",
                             "People signed in to the Gemini web app with a personal Google Account associated with the profile; work or school accounts aren't supported for now.",
                             "Accounts with Keep Activity turned on."])),
      ("Where it works", "<p>Google says the feature is only in the Gemini web app at gemini.google.com, is available wherever the Gemini web app is supported, and isn't available to owners or managers with access to more than one verified Business Profile. Agencies and multi-location businesses will need to keep using the usual tools for now.</p>"),
      ("How to connect", ol(["Go to gemini.google.com, signed in to the account you use for your Business Profile.",
                             "Ask Gemini about your Business Profile; if it doesn't use the app, add @Google Business Profile to your prompt.",
                             "If it isn't connected, follow the on-screen option to connect it.",
                             "You can connect or disconnect it at any time in Connected Apps settings."])),
      ("What you can update", "<p>Google lists business hours, including special hours for holidays and events; food menus for food businesses; photos, uploaded from a public URL; attributes such as outdoor seating or Wi-Fi, which vary by category; your website and social links; action links for ordering, reservations or appointments; and location details and profile status.</p>"),
      ("Engaging with customers", "<p>Gemini can show star ratings and reviews, draft or delete replies to reviews, and create, schedule, publish or delete Update, Offer and Event posts. Google's example prompts include asking Gemini to summarize recent reviews or help draft a reply to the latest one.</p>"),
      ("Business insights", "<p>Gemini can analyze impressions, website clicks, direction requests and bookings, and show the search keywords customers use to find your business. Google's examples include asking for performance metrics for the past month or the top search keywords driving traffic.</p>"),
      ("The business notebook", "<p>Eligible owners can create a business notebook in Gemini, which requires Business Profile to be connected. Google says it adds proactive insights and suggested actions, such as adding missing hours or a description, adding an exterior photo or reviewing performance, plus suggested prompts and recent chats. It appears in the sidebar under Notebooks with your business name.</p>"),
      ("Review what Gemini drafts", "<p>Gemini can draft review replies and posts, but you are responsible for what's published. Read every reply before it goes live, make it personal, and never share private customer details. A short, genuine reply written with Gemini's help beats a generic one.</p>"),
      ("Keep access tidy", "<p>Because the feature requires a personal Google Account linked to the profile, check who owns and manages your profile and that access sits with the right people. If several staff help, give each their own manager access rather than sharing one login.</p>"),
      ("A worked example", "<p>Imagine a single-location bakery in Fullerton. On Monday morning, the owner asks Gemini to summarize last week's reviews, then drafts and edits replies to two of them. Next, they ask for last month's top search keywords, notice many searches for custom birthday cakes and create an Offer post about them. Finally, they set special hours for an upcoming holiday. The whole routine takes about fifteen minutes.</p>"),
      ("What it means for local search", "<p>Tools like this make it easier to keep a profile current, and a current, complete profile is the foundation of local visibility on Google and in AI assistants. The convenience only pays off if you use it regularly.</p>"),
      ("The short version", "<p>If you manage one verified profile with a personal account, you can manage your Google Business Profile in Gemini: update details, reply to reviews, post and check insights by asking. Anaheim and Orange County owners should connect it, review every draft and build a weekly routine.</p>")],
     faqs=[("Can I manage my Google Business Profile in Gemini?", "Yes, in the Gemini web app at gemini.google.com, once you connect Google Business Profile."),
           ("Who is eligible?", "Owners or managers of only one verified profile, 18 or over, using a personal Google Account with Keep Activity on."),
           ("Can I use a work Google Account?", "Not for now. Google says work and school accounts aren't supported."),
           ("What can Gemini change on my profile?", "Hours, menus, photos, attributes, contact links, action links and more."),
           ("Can Gemini reply to reviews?", "It can draft or delete replies; review each one before publishing."),
           ("What is a business notebook?", "A Gemini notebook with proactive insights, suggested actions and prompts for your business."),
           ("Does it work for agencies with many profiles?", "No. Google says it isn't available to people with access to more than one verified profile."),
           LOCAL_FAQ],
     links=[GBP, GBP_PERF, GBP_USERS, REPLY, GBP_LINKS, LOCAL, AUD],
     sources=["g_gbp_gemini"],
     visuals=[V.flow(3, "Managing your profile with Gemini", "From Google's Business Profile help center.",
               [("Connect", "Link Business Profile in the Gemini web app."), ("Update", "Hours, links, attributes, photos."),
                ("Engage", "Draft replies and create posts."), ("Insights", "Metrics and search keywords.")])],
     secondary=["Gemini Google Business Profile", "manage Business Profile with AI", "Gemini business notebook", "Google Business Profile AI assistant"],
     hero_query="Can I update my Google Business Profile by chatting with Gemini?"),
]

EXTRA = {
"gemini-4-hydrogen-google-search-upgrade": [
 ("Questions to ask about your own pages", ul(["If someone asked a three-part question about our service, would one page answer every part?",
   "Do our pages state prices, timelines, service areas and availability, or only say call us?",
   "Would a comparison table help customers choose between our options?",
   "Are our photos original, and do they show the work, the place and the people?",
   "Is anything on our site out of date or contradicted by our Business Profile?"])),
 ("Typos and natural language", "<p>Google says Search can now cope with hard-to-understand typos and questions asked in a natural flow of thought. People rarely search in neat keywords when they speak or type quickly on a phone. Rather than writing pages around awkward keyword phrases, write them the way you would explain the service to a customer at the counter. Clear, natural language is easier for both people and Search to understand, and it reads far better than text stuffed with city names and repeated phrases.</p>")],
"google-ads-invalid-traffic-card": [
 ("What the card can't tell you", "<p>The card shows what Google filtered and credited. It doesn't show whether the remaining clicks became customers, whether your landing page converts, or whether your keywords match the jobs you want. Those answers come from your own conversion tracking and records. Treat the card as reassurance about billing, and your lead and sales data as the real measure of whether your ads work.</p>"),
 ("A monthly ads check for local businesses", ol(["Open the Invalid traffic card and note estimated savings and credited cost.",
   "Check the Invalid clicks column for unusual spikes by campaign.",
   "Compare ad leads with booked jobs or signed clients from your own records.",
   "Review your search terms and add negatives for irrelevant queries.",
   "Test your lead form on a phone to make sure it works and is protected."]))],
"moving-to-a-cdn-googlebot-crawling": [
 ("Questions to ask your host or developer", ul(["Is our site behind a CDN or web application firewall, and who manages it?",
   "Is the option to allow verified bots turned on?", "Do any rules show CAPTCHA or challenge pages to automated traffic?",
   "How would we spot a sudden drop in Google's crawling?", "What is our plan if the origin server is overloaded during a move?"])),
 ("Why this matters for small sites", "<p>It is easy to assume crawling problems only affect huge sites. But a small business site with a few hundred pages can still be knocked out of Search by a single firewall rule that challenges every bot. The fix is usually a settings change, but only if someone notices. Add a check of Search Console's crawl stats and indexing reports to your monthly routine, and look again any time your host, CDN or security settings change.</p>")],
"gemini-apple-carplay-local-business": [
 ("Questions drivers might ask", ul(["Where can I get a quick lunch near the stadium that has easy parking?",
   "Is there a tire shop open now on my way to Irvine?", "Which coffee shop near the freeway exit has a drive-through?",
   "What's a family-friendly restaurant near the Convention Center that takes walk-ins?",
   "Is there a florist on the way that can make an arrangement in under an hour?"])),
 ("Voice changes how people ask", "<p>When people speak to an assistant, they tend to ask complete questions with conditions attached rather than typing two or three words. They mention timing, location, convenience and who they are with. Businesses that state these details plainly, such as walk-ins welcome, free parking behind the building or orders ready in ten minutes, give an assistant concrete facts to match against a spoken request. Look at your Business Profile and website through that lens: would a driver's question be answered by what you have published?</p>"),
 ("Hours are the first test", "<p>A recommendation is only useful if the place is open. Wrong hours are one of the fastest ways to lose a customer who drove to you. Keep regular and special hours accurate on your Business Profile, especially around holidays and events in Anaheim, when traffic and visitor numbers change.</p>")],
"google-business-profile-gemini-web-app": [
 ("Prompts to try", ul(["Show all the contact information on my profile.", "Review all my business attributes.",
   "Summarize my recent reviews and the main themes.", "Help me draft a reply to my latest review.",
   "Help me brainstorm and create a new post.", "Show me my performance metrics for the past month.",
   "What are the top search keywords driving traffic to my business?"])),
 ("A weekly routine", "<p>Pick a regular time each week and work through the same steps: summarize new reviews and reply to each one, check performance and top search keywords, create one post about a service, offer or event, and confirm hours for the coming week, including any holidays. Once a month, ask Gemini to review your attributes and contact links, and check the business notebook's suggested actions for missing details such as photos or a description. A routine that takes fifteen minutes a week keeps a profile current far better than an occasional overhaul.</p>"),
 ("Privacy and data", "<p>Google points to its Gemini Apps Privacy Hub and its help on Connected Apps for how your data is handled when Gemini works with your Business Profile. Read those pages before connecting, and decide who in the business should hold the connected account.</p>")],
}
for p in PAGES:
    for h, b in EXTRA.get(p["slug"], []):
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

MORE = {
"google-ads-invalid-traffic-card": ("Third-party click fraud tools", "<p>Google's help page notes that third-party tools might flag traffic as invalid, such as duplicate IP addresses or bot activity, that Google has already filtered and excluded from your bill. Before paying for a separate tool or filing an investigation, compare its reports with the Invalid clicks column and the new card. If the suspicious clicks are already filtered, you were not charged for them.</p>"),
"gemini-apple-carplay-local-business": ("Landmarks and local stories", "<p>Google also mentions asking Gemini for the backstory on a local landmark. Anaheim and Orange County attract millions of visitors, and businesses near well-known places can benefit from clearly describing where they are in relation to them.</p>"),
"google-business-profile-gemini-web-app": ("If the option doesn't appear", "<p>If Gemini doesn't offer to connect your profile or create a business notebook, check the requirements first: one verified profile only, a personal Google Account linked to it, age 18 or over and Keep Activity turned on. Google suggests adding @Google Business Profile to a prompt to prompt the connection or the notebook offer. Also make sure you are using the web app at gemini.google.com rather than the mobile app.</p>"),
}
for p in PAGES:
    if p["slug"] in MORE:
        h, b = MORE[p["slug"]]
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

if __name__ == "__main__":
    save_all(PAGES)
