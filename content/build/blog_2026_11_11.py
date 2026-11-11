"""Blog posts for 2026-11-11 (5 posts). Every fact is checked at the linked Google source on 2026-11-11."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_10b  # noqa: F401  (SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SC = "https://developers.google.com/search/blog/2026/"
SRC.update({
    "g_aipref": {"title": "Google Search Central blog: Supporting a shared AI training control for websites (Oct 30, 2026)",
                 "url": SC + "10/ai-training-control"},
    "g_extended": {"title": "Google crawler documentation: Google's common crawlers (Google-Extended)",
                   "url": "https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers"},
    "g_carbon": {"title": "Google: Gemini 4 Carbon is now available (Nov 10, 2026)",
                 "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/"},
    "g_genai_sc": {"title": "Google Search Central blog: Introducing Search Generative AI performance reports in Search Console (Jun 3, 2026)",
                   "url": SC + "06/gen-ai-performance-reports"},
    "g_multimodal_sc": {"title": "Google Search Central blog: Announcing web multimodal Search performance reporting in Search Console (Sep 24, 2026)",
                        "url": SC + "09/web-multimodal-in-sc"},
    "g_paths": {"title": "Google Search Central blog: New learning paths for Search fundamentals and Technical SEO (Oct 6, 2026)",
                "url": SC + "10/seo-learning-paths"},
    "g_photos": {"title": "Google Business Profile Help: Manage your Business Profile photos and videos",
                 "url": "https://support.google.com/business/answer/6103862?hl=en"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")
ROBOTS = L("robots.txt for AI crawlers", "robots-txt-for-ai-crawlers")
CRAWLERS = L("AI crawler user agents", "ai-crawler-user-agents")
MODE = L("how to optimize for Google AI Mode", "how-to-optimize-for-google-ai-mode")
AIO = L("how to show up in Google AI Overviews", "how-to-show-up-in-google-ai-overviews")
TRACK = L("how to track AI visibility", "how-to-track-ai-visibility")
MEASURE = L("how to measure GEO results", "how-to-measure-geo-results")
GBP_PHOTOS = L("Google Business Profile photos", "google-business-profile-photos")
CWV = L("Core Web Vitals for local businesses", "core-web-vitals-for-local-businesses")
SMB = L("AI SEO for small business", "ai-seo-for-small-business")
CHECK = L("local SEO checklist", "local-seo-checklist")

PAGES = [
# 1 ------------------------------------------------------------------
blog(1, "Google Search",
     slug="google-ai-training-control-robots-txt", query="ai training control robots.txt", kw="AI training control in robots.txt",
     eyebrow="Google Search", short_title="Google's shared AI training control in robots.txt",
     title="AI Training Control in robots.txt: Google's Plan",
     meta="Google plans to support a shared AI training control in robots.txt. What it means for Anaheim and Orange County websites, Google-Extended and AI answers.",
     h1="Google's Shared AI Training Control in robots.txt: What Website Owners Should Know",
     answer="Google plans to support a shared AI training control in robots.txt, based on IETF work, so one setting can tell participating AI providers whether your content may be used for training. Google aims to support it with other providers in 2027. For Anaheim and Orange County businesses, the key point is that opting out of training does not affect Google Search, but it can affect grounding in Gemini Apps.",
     takeaways=["Google announced the plan on October 30, 2026.", "A shared policy token in robots.txt would cover participating AI providers.",
                "Opting out with the token is treated like disallowing Google-Extended.", "Google-Extended does not affect Google Search inclusion or ranking.",
                "Google aims to support the control in 2027."],
     sections=[
      ("What Google announced", "<p>On October 30, 2026, Google's Search Central blog announced plans to support a shared AI training control in robots.txt. The idea is to let websites express their AI training preferences across multiple AI providers in one step. Google says the work is based on the AIPREF working group at the Internet Engineering Task Force, the body that develops many internet standards, and builds on Google-Extended, the AI training control Google has offered since 2023.</p>"),
      ("How the shared control would work", "<p>Instead of writing separate instructions for every AI developer, site owners would add a shared policy token to robots.txt to set broad preferences across participating AI providers. Google says that when a site uses this token to opt out of training, and Google-Extended is not explicitly specified, Google plans to treat it as if the publisher had disallowed Google-Extended. Other providers can handle it the same way, so owners could opt out across all providers at once, or pick and choose.</p>"),
      ("Company-specific controls still work", "<p>Google says existing company-specific controls will keep working alongside the new joint signal. A site could set a broad preference with the industry token and still tailor instructions for individual AI developers, such as Google through Google-Extended. More specific rules continue to matter.</p>"),
      ("What Google-Extended actually controls", "<p>Google's crawler documentation describes Google-Extended as a standalone product token that controls whether content Google crawls may be used to train future Gemini models that power Gemini Apps and the Vertex AI API, and for grounding in Gemini Apps and Grounding with Google Search on Vertex AI. Grounding means providing content from the Google Search index to the model when it answers, to improve accuracy and relevance.</p>"),
      ("It does not affect Google Search", "<p>This is the point most owners worry about. Google's documentation says Google-Extended does not impact a site's inclusion in Google Search and is not used as a ranking signal in Google Search. Opting out of AI training through Google-Extended, or through the planned shared token, is not the same as blocking Googlebot.</p>"),
      ("But it can affect Gemini answers", "<p>Google's announcement adds an important detail: websites that specifically allow Google-Extended are eligible to appear in responses and receive clicks via grounding in Gemini Apps. A local business that opts out may therefore give up a route to being cited and linked in Gemini's answers, even though its Search rankings are unaffected.</p>"),
      ("The decision for local businesses", "<table><tr><th>Choice</th><th>Google Search</th><th>Gemini Apps grounding</th></tr><tr><td>Allow (default)</td><td>No effect</td><td>Eligible to appear and receive clicks</td></tr><tr><td>Opt out of training</td><td>No effect</td><td>Treated as disallowing Google-Extended</td></tr></table><p>For most Anaheim and Orange County service businesses, whose goal is to be found and recommended, staying open to AI use is usually the better trade. Publishers who sell their content may weigh it differently.</p>"),
      ("When this arrives", "<p>Google describes the proposal as a draft that reflects feedback from publishers, civil society groups and regulators, and says it aims to support the new control along with other AI providers in 2027, with updates on progress. Nothing needs to change in your robots.txt today because of this announcement.</p>"),
      ("Why it matters beyond Google", "<p>Today, each AI company uses its own crawler name, so a site that wants to opt out of training has to list many user agents and keep the list current. A shared token would make one clear choice possible. Google notes the approach is consistent with the EU Code of Practice for general-purpose AI model providers, which recognizes robots.txt as a primary way for publishers to express machine-readable preferences.</p>"),
      ("Check your robots.txt now", "<ol><li>Open yoursite.com/robots.txt and read every rule.</li><li>Confirm Googlebot is not blocked from pages you want in Search.</li><li>Look for Google-Extended and other AI user agents, and check each rule is intentional.</li><li>Remove leftovers from old plugins or developers that block crawlers you want.</li><li>Write down your policy so future changes are deliberate.</li></ol>"),
      ("A worked example", "<p>Imagine an Orange County law firm whose developer added a block on every AI user agent years ago, including Google-Extended. The firm's Search rankings were never affected, but it was not eligible to be grounded and linked in Gemini Apps answers. After reviewing its goals, the firm decides it wants to be cited, removes the Google-Extended block and keeps rules for crawlers it does not want. It notes to revisit the decision when the shared token is supported.</p>"),
      ("What this means for AI search visibility", "<p>Being cited by AI assistants depends on them being able to read and use your content. Blocking AI uses can reduce your chances of appearing in AI answers, while allowing them keeps the door open. Pair the decision with the basics that make you worth citing: clear service pages, accurate facts and consistent business details.</p>"),
      ("Questions to ask your web team", "<ul><li>Which AI user agents does our robots.txt mention, and why?</li><li>Did a plugin or security tool add rules we did not choose?</li><li>Do we want to appear in Gemini answers with a link?</li><li>Who will update the file when the shared token is supported?</li></ul>"),
      ("The short version", "<p>Google plans a shared robots.txt token for AI training preferences, aiming for 2027. It will not change Google Search, but opting out can remove eligibility for grounding in Gemini Apps. For most Anaheim and Orange County businesses that want to be recommended, allowing AI use and keeping content accurate is the sensible default.</p>")],
     faqs=[("What is the shared AI training control?", "A planned policy token in robots.txt that lets websites state AI training preferences across participating AI providers at once."),
           ("When will Google support it?", "Google says it aims to support the control along with other AI providers in 2027."),
           ("Does blocking Google-Extended hurt my Google rankings?", "No. Google says Google-Extended does not affect inclusion in Google Search or ranking."),
           ("Does opting out affect Gemini?", "Yes. Google says sites that allow Google-Extended are eligible to appear and receive clicks via grounding in Gemini Apps."),
           ("Will my existing robots.txt rules still work?", "Yes. Google says company-specific controls will continue alongside the shared signal."),
           ("Who developed the standard?", "It is based on work by the AIPREF working group at the Internet Engineering Task Force."),
           ("Should a local business opt out of AI training?", "Most businesses that want to be recommended benefit from staying open; publishers may decide differently."),
           ("Do I need to change anything now?", "No, but it is a good moment to check your robots.txt for rules you did not intend."),
           LOCAL_FAQ],
     links=[ROBOTS, CRAWLERS, L("Gemini SEO", "gemini-seo"), LOCAL, AUD],
     sources=["g_aipref", "g_extended"],
     visuals=[V.flow(1, "How the shared control would work", "Based on Google's October 30, 2026 announcement.",
               [("Token", "Add the shared policy token to robots.txt."), ("Providers", "Participating AI providers read it."),
                ("Google", "Treated as disallowing Google-Extended, unless Google-Extended is set explicitly."), ("Search", "No effect on Google Search.")])],
     secondary=["Google-Extended", "AIPREF robots.txt", "block AI training robots.txt", "opt out of AI training"],
     hero_query="If I block AI training in robots.txt, will my site drop out of Google?"),

# 2 ------------------------------------------------------------------
blog(2, "AI news",
     slug="gemini-4-carbon-ai-mode-local-business", query="gemini 4 carbon", kw="Gemini 4 Carbon",
     eyebrow="AI news", short_title="Gemini 4 Carbon arrives in AI Mode",
     title="Gemini 4 Carbon: What It Means for Local Business",
     meta="Gemini 4 Carbon launched on November 10, 2026 and is rolling out in AI Mode for AI Ultra subscribers. What Anaheim and Orange County businesses should know.",
     h1="Gemini 4 Carbon Is Here: What Google's Newest Model Means for Local Businesses",
     answer="Gemini 4 Carbon, released on November 10, 2026, is Google's strongest model, built for long, multi-step reasoning. It is available to developers and enterprises and rolling out to Google AI Ultra subscribers in the Gemini app and AI Mode in Search. For Anaheim and Orange County businesses, it means deeper AI research for some customers, which rewards accurate, detailed information.",
     takeaways=["Google released Gemini 4 Carbon on November 10, 2026.", "Carbon is built for complex, long-running reasoning tasks.",
                "Gemini 4 Argon remains the choice for most everyday work.", "Carbon is rolling out to AI Ultra subscribers in AI Mode in Search.",
                "Developer pricing starts at $2 per million input tokens."],
     sections=[
      ("What Google announced", "<p>On November 10, 2026, Google made Gemini 4 Carbon available to developers, enterprises, scientists and consumers. Google calls Carbon its strongest model, with frontier performance in cybersecurity and in long-horizon agentic work across complex knowledge work, software engineering and scientific reasoning. Two weeks earlier, Google had released it to a group of cybersecurity defenders through its Fairwind Program.</p>"),
      ("Carbon versus Argon", "<p>Google positions Carbon alongside Gemini 4 Argon, which it launched recently. Google says Argon remains the ideal choice for the majority of software engineering and knowledge work, while Carbon is for tasks that test the limits of a model's intelligence, such as complex, multi-step coding and debugging or open-ended research. Carbon uses more tokens than Argon to explore thoroughly, reason deeply and run extended verification loops.</p>"),
      ("Where people can use it", "<table><tr><th>Who</th><th>Where</th></tr><tr><td>Paying developers and enterprises</td><td>The API in Google AI Studio and Gemini for business</td></tr><tr><td>Google AI Ultra subscribers</td><td>Google Antigravity, the Gemini app and AI Mode in Search</td></tr></table><p>Google says Carbon is rolling out to all AI Ultra subscribers, so most people using free Google Search will not see Carbon-powered AI Mode answers yet.</p>"),
      ("Benchmarks Google reported", "<p>Google says Carbon ranks first on CursorBench 4.0, Perplexity's WANDR and Zapier's AutomationBench at more than 2 times lower cost per task than the next best external model. On a new Multimodal Knowledge Agent benchmark built with Artificial Analysis, Google says Carbon ranks second at more than 6 times lower average cost per task than the top model. These are Google's reported results.</p>"),
      ("Pricing for developers", "<p>Google lists an introductory price matching Gemini 4 Argon: $2 per million input tokens and $10 per million output tokens through the API. For small businesses building their own tools, such as a quoting assistant or an internal knowledge search, that sets the cost of trying the most capable model.</p>"),
      ("What changes in AI Mode", "<p>Google has not said how Carbon changes which businesses appear in AI Mode answers, and we will not guess. What is clear is that some AI Mode users now have a model built to research longer and verify more. A customer asking for the best roofer in Orange County for a specific tile roof may get a more thorough comparison, drawn from more sources.</p>"),
      ("Why detail wins with deeper research", "<p>A model that reads more and checks more is more likely to notice gaps and contradictions. If your website says you serve Irvine but your Business Profile does not, or your prices differ between pages, a careful model may skip you or hedge. Detailed, consistent information is the practical response to more capable models.</p>"),
      ("What to update this month", "<ol><li>Make sure each service has its own page with scope, timing, price guidance and service area.</li><li>Check that your name, address, phone and hours match on your site, Business Profile and main directories.</li><li>Add the answers customers actually ask before buying.</li><li>Keep reviews coming and reply to them.</li><li>Fix anything outdated, such as old offers or staff who have left.</li></ol>"),
      ("Agents and swarms", "<p>Google also previewed a /swarm feature in Google Antigravity that turns one prompt into a coordinated team of agents, with Carbon in the roles needing the deepest reasoning. This is mainly for developers today, but it points to a future where AI agents research and compare suppliers on someone's behalf. Businesses that are easy for machines to understand will be easier to choose.</p>"),
      ("A worked example", "<p>Imagine an AI Ultra subscriber in Anaheim asking AI Mode to compare three kitchen remodelers for a budget and timeline. A remodeler whose site publishes a cost guide, a typical timeline, its license number and real project pages gives the model concrete facts to compare. One whose site only says call for a quote gives it nothing, and is more likely to be left out of a careful comparison.</p>"),
      ("Should your business use Carbon?", "<p>For everyday writing, customer emails and summaries, Google itself says Argon suits most work. Carbon makes sense for complex jobs such as analyzing many documents or building software. Start with the simpler model and move up only when a task needs it.</p>"),
      ("Keeping up without chasing releases", "<p>New models arrive every few months. Rather than reacting to each one, keep improving the basics that every model relies on: accurate listings, clear pages, genuine reviews and a site that is fast and easy to read.</p>"),
      ("The short version", "<p>Gemini 4 Carbon is Google's most capable model, now reaching AI Mode for AI Ultra subscribers. It raises the bar for detail and consistency. Anaheim and Orange County businesses that publish clear, accurate, specific information are best placed as AI research gets deeper.</p>")],
     faqs=[("What is Gemini 4 Carbon?", "Google's strongest model, released on November 10, 2026, built for complex, long-running reasoning tasks."),
           ("Is Gemini 4 Carbon in Google Search?", "Google says it is rolling out to all Google AI Ultra subscribers in AI Mode in Search."),
           ("How is Carbon different from Argon?", "Google says Argon suits most work, while Carbon is for the hardest multi-step tasks and uses more tokens to reason."),
           ("How much does Carbon cost for developers?", "Google lists $2 per million input tokens and $10 per million output tokens as an introductory price."),
           ("Will Carbon change my local rankings?", "Google has not said; accurate, detailed and consistent information is the safest preparation."),
           ("Can I use Carbon in the Gemini app?", "Google says it is rolling out to AI Ultra subscribers in the Gemini app."),
           ("What is /swarm?", "A preview feature in Google Antigravity that turns one prompt into a coordinated team of AI agents."),
           ("Should small businesses build tools on Carbon?", "Start with simpler models and use Carbon only for tasks that need deep reasoning."),
           LOCAL_FAQ],
     links=[MODE, AIO, L("Gemini SEO", "gemini-seo"), LOCAL, AUD],
     sources=["g_carbon", "g_ai_oct"],
     visuals=[V.timeline(0, "Gemini 4 Carbon rollout", "Dates and availability from Google's announcement.",
               [("Late Oct 2026", "Fairwind", "Released to cybersecurity defenders."), ("Nov 10, 2026", "Developers", "API in AI Studio and Gemini for business."),
                ("Nov 10, 2026", "AI Ultra", "Rolling out in the Gemini app and AI Mode."), ("Ongoing", "Argon", "Remains the choice for most work.")])],
     secondary=["Gemini 4 Carbon AI Mode", "Gemini Carbon vs Argon", "Google newest AI model", "Gemini 4 Carbon pricing"],
     hero_query="What is Gemini 4 Carbon and does it change Google AI Mode results?"),

# 3 ------------------------------------------------------------------
blog(3, "Search Console",
     slug="search-console-generative-ai-performance-report", query="search console generative ai performance report", kw="generative AI performance report",
     eyebrow="Search Console", short_title="Search Console's generative AI performance report",
     title="Search Console Generative AI Performance Report",
     meta="Search Console's generative AI performance report shows impressions in AI Overviews and AI Mode. How Anaheim and Orange County businesses can use it.",
     h1="Search Console's Generative AI Performance Report: How to See Your AI Overviews and AI Mode Visibility",
     answer="The Search Console generative AI performance report shows how often your pages appear in Google's generative AI features, such as AI Overviews and AI Mode, with views for Search and Discover. Google rolled it out to all websites worldwide by August 31, 2026. Anaheim and Orange County businesses can use it to see which pages AI features show, by country, device and date.",
     takeaways=["Google announced the reports on June 3, 2026.", "They reached all websites worldwide as of August 31, 2026.",
                "They cover AI Overviews, AI Mode and AI features in Discover.", "You can filter by page, country, device and date.",
                "The same data still counts in the overall performance report."],
     sections=[
      ("What the report is", "<p>On June 3, 2026, Google announced Search Generative AI performance reports in Search Console, with dedicated reports for Search and Discover. Google says they give dedicated views of your impressions within generative AI features on Search, such as AI Overviews and AI Mode, and within generative AI features in Discover. A note on Google's post says that as of August 31, 2026, the insights had rolled out to all websites worldwide.</p>"),
      ("What it shows", "<table><tr><th>Data</th><th>What it tells you</th></tr><tr><td>Impressions</td><td>How often your URLs appeared in generative AI features in Search and Discover</td></tr><tr><td>Pages</td><td>Which URLs appeared within AI features</td></tr><tr><td>Countries</td><td>Your visibility by country</td></tr><tr><td>Devices</td><td>The devices people used (for Search results)</td></tr><tr><td>Dates</td><td>Trends with hourly, daily, weekly and monthly views</td></tr></table>"),
      ("How it relates to the main report", "<p>Google says this data is also included in the overall performance report, where it continues to be tracked. The new report is a separate view dedicated to visibility from generative AI features, not extra traffic on top of what you already saw.</p>"),
      ("Why it matters for local businesses", "<p>Until this report, most businesses could only guess whether Google's AI features were showing their pages. For an Anaheim dentist or an Orange County HVAC company, seeing which pages appear in AI Overviews and AI Mode shows which content Google's AI finds useful, and which pages are missing.</p>"),
      ("How to open it", "<ol><li>Sign in to Search Console and choose your property.</li><li>Open the performance reports and select the generative AI report for Search, or for Discover.</li><li>Set the date range and look at impressions over time.</li><li>Open the Pages view to see which URLs appeared.</li><li>Compare with your overall performance report for the same dates.</li></ol>"),
      ("Questions to answer with it", "<ul><li>Which of our pages appear in AI features at all?</li><li>Are our main service pages among them, or only blog posts?</li><li>Did impressions change after we updated a page?</li><li>Are AI impressions mostly on mobile or desktop?</li><li>Is our visibility growing month over month?</li></ul>"),
      ("Reading the numbers carefully", "<p>Google's post describes impressions, pages, countries, devices and dates. Treat impressions as visibility, not visits. Combine the report with Google Analytics to see visits that follow, and with your own lead tracking to see whether AI visibility turns into calls and bookings.</p>"),
      ("Turning insights into action", "<p>If a service page never appears while a blog post does, look at what the blog post does better: a direct answer near the top, clear headings, specific facts. Apply the same to the service page. If AI impressions drop after an edit, compare the old and new versions. Change one thing at a time so you can see what worked.</p>"),
      ("Pair it with manual checks", "<p>Search Console tells you that your page appeared, not what the AI said. Each month, ask Google, ChatGPT, Gemini and Perplexity the questions your customers ask, from a phone in Orange County, and record whether you are named and described correctly. Together, the report and manual checks give a fuller picture.</p>"),
      ("A worked example", "<p>Imagine a pest control company in Garden Grove. The report shows its termite guide appearing in AI features while its main termite treatment page does not. The company adds a short, direct answer at the top of the service page, a clear section on cost factors and its service area. Over the following weeks it watches the Pages view to see whether the service page starts appearing too.</p>"),
      ("Feedback and what is next", "<p>Google asks for feedback through the Submit feedback link in Search Console, a dedicated form and the Search Central Community, and says it is working with site owners to understand which data would be most useful, such as adding more metrics over time.</p>"),
      ("The short version", "<p>Search Console's generative AI performance report finally shows how often your pages appear in AI Overviews, AI Mode and AI features in Discover. Anaheim and Orange County businesses should check it monthly, compare it with leads and use it to improve the pages AI features skip.</p>")],
     faqs=[("What is the Search Console generative AI performance report?", "A dedicated view of how often your pages appear in Google's generative AI features in Search and Discover."),
           ("Does it include AI Overviews and AI Mode?", "Yes. Google names AI Overviews and AI Mode as examples."),
           ("Is it available for every site?", "Google says it rolled out to all websites worldwide as of August 31, 2026."),
           ("What can I filter by?", "Pages, countries, devices (for Search) and dates, with hourly, daily, weekly and monthly views."),
           ("Is this data separate from my normal performance report?", "No. Google says it is also included in the overall performance report."),
           ("Does it show what the AI said about me?", "No. It shows impressions; check AI answers manually for wording."),
           ("How often should I check it?", "Monthly is enough for most local businesses, and after major page changes."),
           ("How do I give feedback?", "Through the Submit feedback link in Search Console, Google's dedicated form or the Search Central Community."),
           LOCAL_FAQ],
     links=[TRACK, MEASURE, AIO, LOCAL, AUD],
     sources=["g_genai_sc"],
     visuals=[V.timeline(0, "From launch to every site", "Dates from Google's Search Central blog.",
               [("Jun 3, 2026", "Announced", "Reports launched to a subset of sites."), ("Summer 2026", "Testing", "Google gathers feedback."),
                ("Aug 31, 2026", "Everyone", "Rolled out to all websites worldwide."), ("Now", "Your turn", "Check it monthly.")])],
     secondary=["AI Overviews report Search Console", "AI Mode Search Console", "generative AI performance Search Console", "track AI Overviews impressions"],
     hero_query="How can I see if my website shows up in Google AI Overviews?"),

# 4 ------------------------------------------------------------------
blog(4, "Search Console",
     slug="search-console-multimodal-search-report", query="search console multimodal search", kw="multimodal search in Search Console",
     eyebrow="Search Console", short_title="Multimodal search data in Search Console",
     title="Multimodal Search in Search Console: Lens Data",
     meta="Search Console now reports multimodal search from Google Lens and Circle to Search. What it shows and how Anaheim and Orange County businesses can use it.",
     h1="Multimodal Search in Search Console: See When People Find You with Lens and Circle to Search",
     answer="Multimodal search in Search Console is a new search type filter, added on September 24, 2026, that shows how your site performs when people search with images, through Google Lens, Circle to Search on Android, image uploads to Google Search and Chrome's Search this image. For Anaheim and Orange County businesses that sell visible products, it shows whether pictures lead customers to you.",
     takeaways=["Google announced the reporting on September 24, 2026.", "It covers Lens, Circle to Search, image uploads and Chrome's Search this image.",
                "Use the multimodal search type filter in the performance reports.", "It also appears in the generative AI features report.",
                "Data shows only if your site gets traffic from these searches."],
     sections=[
      ("What Google announced", "<p>On September 24, 2026, Google introduced Search Console reporting for web multimodal search, in the performance report for Search results and in the report for generative AI features. Google says the update gives site owners insight into how content is surfaced when people search using images, such as with a smartphone camera.</p>"),
      ("Which searches count", "<table><tr><th>Source</th><th>How people use it</th></tr><tr><td>Google Lens</td><td>Point the camera at something to search for it</td></tr><tr><td>Circle to Search on Android</td><td>Circle something on screen to search it</td></tr><tr><td>Image uploads to Google Search</td><td>Search with a saved photo</td></tr><tr><td>Chrome right-click Search this image</td><td>Search an image found on a web page</td></tr></table>"),
      ("How to find the data", "<p>Google says to use the new multimodal search type filter in the performance reports. You can also click Export to download the data and analyze it in other tools. The rollout began globally on September 24, 2026, and Google notes the metrics appear in your Performance report only if your site is receiving traffic from these queries.</p>"),
      ("Why it matters locally", "<p>People increasingly search with their camera: a shopper photographs a lamp in a friend's house, a homeowner snaps a broken part, a visitor in Anaheim points a phone at a dish or a storefront. If your products and services are well represented in images, these searches can lead to your site. Until now, that traffic was hard to separate.</p>"),
      ("Businesses that benefit most", "<ul><li>Retailers selling distinctive products, such as furniture, clothing or gifts.</li><li>Restaurants and bakeries whose dishes people photograph.</li><li>Home services where customers photograph a part or problem.</li><li>Auto shops and parts suppliers.</li><li>Venues and attractions people photograph and share.</li></ul>"),
      ("Make your images findable", "<ol><li>Use real, high-quality photos of your products and work.</li><li>Place each image near text that describes it.</li><li>Write descriptive file names and alt text.</li><li>Give important products their own pages with clear names, prices and availability.</li><li>Keep images fast to load.</li></ol>"),
      ("Your Business Profile photos matter too", "<p>Google's Business Profile help recommends photos that are in focus, well lit and represent reality, at around 720 by 720 pixels. Real photos of your storefront, products and work help customers recognize you on Maps and keep your visual presence consistent across Google.</p>"),
      ("Reading the report", "<p>Compare multimodal clicks and impressions with your total. If they are a meaningful share, image quality and product pages deserve more attention. Look at which pages attract multimodal traffic and whether they lead to calls, orders or visits. Exported data can be combined with analytics for a fuller view.</p>"),
      ("A worked example", "<p>Imagine a furniture store in Costa Mesa. After filtering for multimodal search, it sees that several product pages get visits from image searches, mostly on mobile. It adds clear photos from more angles, names and dimensions near each image, and in-store availability. It then watches whether those pages bring more visits and store inquiries.</p>"),
      ("Multimodal search and AI features", "<p>Because the filter also appears in the generative AI features report, you can see when image searches lead to your pages appearing in AI features. As AI answers grow more visual, clear product images and descriptive text work together.</p>"),
      ("Common mistakes", "<ul><li>Stock photos that do not show your real products.</li><li>Products shown only in image carousels without text.</li><li>Missing alt text and generic file names.</li><li>Heavy images that slow pages on phones.</li></ul>"),
      ("The short version", "<p>Search Console now separates searches made with images, from Lens, Circle to Search, uploads and Chrome. Anaheim and Orange County businesses with visual products should check the multimodal filter, improve real product photos and descriptive text, and track whether image searches turn into customers.</p>")],
     faqs=[("What is multimodal search in Search Console?", "A search type filter showing performance when people search with images, such as through Google Lens."),
           ("Which tools are included?", "Lens, Circle to Search on Android, image uploads to Google Search and Chrome's right-click Search this image."),
           ("When was it added?", "Google announced it on September 24, 2026, rolling out globally from that date."),
           ("Why don't I see any multimodal data?", "Google says metrics appear only if your site receives traffic from these queries."),
           ("Can I export the data?", "Yes. Google says you can click Export to analyze it in other tools."),
           ("Is it in the generative AI report too?", "Yes. Google added it to the report for generative AI features as well."),
           ("How can I get more image search traffic?", "Use real, well-described product photos on fast pages with clear text near each image."),
           ("Do Business Profile photos help?", "They help customers recognize you on Maps; use real, well-lit photos that represent reality."),
           LOCAL_FAQ],
     links=[GBP_PHOTOS, L("product pages for AI shopping", "product-pages-for-ai-shopping"), TRACK, LOCAL, AUD],
     sources=["g_multimodal_sc", "g_photos", "g_genai_sc"],
     visuals=[V.flow(2, "Where multimodal searches come from", "The four sources Google includes in the new filter.",
               [("Lens", "Camera search."), ("Circle to Search", "On Android screens."),
                ("Image upload", "Search with a saved photo."), ("Chrome", "Right-click Search this image.")])],
     secondary=["Google Lens Search Console", "Circle to Search traffic", "image search performance report", "visual search SEO"],
     hero_query="Can I see how many people find my store through Google Lens?"),

# 5 ------------------------------------------------------------------
blog(5, "SEO learning",
     slug="google-seo-learning-paths-small-business", query="google seo learning paths", kw="SEO learning paths",
     eyebrow="SEO learning", short_title="Google's free SEO learning paths",
     title="Google's Free SEO Learning Paths: A Guide",
     meta="Google's Search Central team released two free SEO learning paths on YouTube. How Anaheim and Orange County business owners can use them, step by step.",
     h1="Google's Free SEO Learning Paths: A Practical Plan for Business Owners",
     answer="Google's SEO learning paths are two free YouTube playlists from the Search Central team, released on October 6, 2026: Search fundamentals for beginners and Technical SEO fundamentals. For Anaheim and Orange County business owners, the beginner path is the useful starting point, covering how Search works, Search Console and Google Trends, straight from Google.",
     takeaways=["Google released the playlists on October 6, 2026.", "Search fundamentals is for owners, marketers and beginners.",
                "Technical SEO fundamentals is for developers and specialists.", "Both are free on the Search Central YouTube channel.",
                "Pair learning with action on your own site."],
     sections=[
      ("What Google released", "<p>On October 6, 2026, Google's Search Central team organized its YouTube content into two learning paths. Google notes that its channel has published hundreds of videos across series such as Search for Beginners, Ask Googlebot, Search Console Training and Search Off the Record, and that finding a clear, sequential path could be hard. The two playlists put the right videos in order.</p>"),
      ("Search fundamentals for beginners", "<p>Google says this playlist is for website owners, marketers, content creators and anyone new to SEO, taking them from core concepts to practical measurement. It covers how Google crawls, indexes and serves content, how to improve your presence in search results and how to measure performance with Search Console and Google Trends.</p><ul><li>How Search works: crawling, indexing, serving and the anatomy of search results.</li><li>Getting started with Search Console: setup, performance reports and Search Console Insights.</li><li>Market and content insights: using Google Trends for SEO and spotting trending topics.</li></ul>"),
      ("Technical SEO fundamentals", "<p>The second playlist is for developers and technical specialists. Google says it skips the basics to focus on site health, crawl budget, rendering and large-scale debugging.</p><ul><li>Crawl directives and architecture: robots.txt, crawl stats and crawl budget.</li><li>Indexing and debugging at scale: indexing issues, the URL Inspection tool and duplicate content.</li><li>Serving, rendering and APIs: how browsers parse HTML, page weight and Search Console bulk data exports and APIs.</li></ul>"),
      ("Which path is for you", "<table><tr><th>If you are</th><th>Start with</th></tr><tr><td>A business owner or office manager</td><td>Search fundamentals for beginners</td></tr><tr><td>A marketer or content writer</td><td>Search fundamentals for beginners</td></tr><tr><td>A web developer</td><td>Technical SEO fundamentals</td></tr><tr><td>The person who runs your website</td><td>Both, in order</td></tr></table>"),
      ("Why learn from Google directly", "<p>SEO advice online varies widely in quality. Videos from Google's own Search Central team explain how Google Search works in Google's words, which is a reliable base for judging other advice, including what agencies and consultants tell you.</p>"),
      ("A four-week plan for owners", "<ol><li>Week 1: watch the How Search works videos and search for your own business to see what Google shows.</li><li>Week 2: watch the Search Console videos, then verify your site and open the performance report.</li><li>Week 3: watch the Google Trends videos and compare interest in your services across seasons.</li><li>Week 4: pick three pages to improve based on what you learned, and note the date you changed them.</li></ol>"),
      ("Apply it to local search", "<p>The playlists cover Google Search generally. Local businesses also need their Google Business Profile, consistent listings and reviews, which Google explains in its Business Profile help. Combine the two: the playlists for your website, the help center for your profile.</p>"),
      ("Put Search Console to work", "<p>Once you have watched the Search Console videos, use the newer reports too, such as the generative AI performance report for AI Overviews and AI Mode, and the multimodal search filter for image searches. Learning the basics makes these reports much easier to read.</p>"),
      ("Bring your team along", "<p>Google suggests saving the playlists and sharing them with your team. A shared understanding helps: whoever writes your service pages, updates your profile or answers reviews will make better decisions if they know how Search works.</p>"),
      ("A worked example", "<p>Imagine the owner of a small landscaping company in Fullerton who has never opened Search Console. After the beginner path, they verify the site, see which searches bring impressions and notice that drought-tolerant landscaping gets attention in Google Trends each spring. They write a clear page on that service before the season and check its impressions the following months.</p>"),
      ("When to bring in help", "<p>Learning the fundamentals does not mean doing everything yourself. It means you can judge advice, ask better questions and spot promises that do not match how Google works. Bring in help when time is short or problems are technical.</p>"),
      ("The short version", "<p>Google's free learning paths are the best starting point for owners who want to understand SEO in Google's own words. Anaheim and Orange County business owners can work through the beginner path in a month and apply each lesson to their own site and Business Profile.</p>")],
     faqs=[("What are Google's SEO learning paths?", "Two free YouTube playlists from Google's Search Central team: Search fundamentals for beginners and Technical SEO fundamentals."),
           ("When were they released?", "Google announced them on October 6, 2026."),
           ("Are they free?", "Yes. They are on the Search Central YouTube channel."),
           ("Which one should a business owner watch?", "Search fundamentals for beginners."),
           ("What does the technical path cover?", "robots.txt, crawl stats and crawl budget, indexing and URL Inspection, duplicate content, rendering, page weight and Search Console APIs."),
           ("Do they cover Google Business Profile?", "They focus on Google Search; use Google's Business Profile help for your listing."),
           ("How long does the beginner path take?", "A few hours of video; spreading it over a month leaves time to apply each lesson."),
           ("Can I learn SEO without an agency?", "You can learn the fundamentals; help is useful when time is short or problems are technical."),
           LOCAL_FAQ],
     links=[SMB, CHECK, CWV, LOCAL, AUD],
     sources=["g_paths", "g_genai_sc", "g_multimodal_sc"],
     visuals=[V.flow(5, "A month with the beginner path", "One theme a week, with an action each time.",
               [("Week 1", "How Search works; search for your business."), ("Week 2", "Search Console; verify and open reports."),
                ("Week 3", "Google Trends; check seasonality."), ("Week 4", "Improve three pages and note the date.")])],
     secondary=["Search Central YouTube playlists", "learn SEO from Google", "free SEO course Google", "technical SEO fundamentals"],
     hero_query="Where can I learn SEO for free from Google?"),
]

EXTRA = {
"gemini-4-carbon-ai-mode-local-business": [
 ("Safety and security", "<p>Google's announcement also covers progress in model safety and security, and Carbon was first released to cybersecurity defenders. For small businesses, the practical lesson is the same as with every stronger model: protect your Business Profile, website and email with multi-factor authentication, because capable AI helps defenders and attackers alike.</p>")],
"search-console-generative-ai-performance-report": [
 ("Set a baseline now", "<p>Export a few months of data from the report and save it. When you publish new pages, update old ones or change your site, you will be able to compare against a clear baseline instead of relying on memory. Note the dates of major changes in a simple log so you can match them to movements in the report later.</p>"),
 ("Discover is part of it", "<p>The Discover view shows AI features in Google's Discover feed, which people browse on their phones without searching. Local businesses that publish timely, useful articles, such as seasonal guides or event coverage in Anaheim, may see impressions there as well as in Search.</p>"),
 ("Share it with your team", "<p>Give the people who write and update your pages access to Search Console, or share a monthly summary. When writers can see which pages AI features show, they learn what clear, useful content looks like on your own site rather than in general advice.</p>")],
"search-console-multimodal-search-report": [
 ("Set up a simple monthly check", "<p>Once a month, open the performance report, apply the multimodal search type filter and note total clicks and impressions, the top pages and the device split. Export the data and keep it in one spreadsheet. A few months of history will show whether image searches matter for your business and which product pages benefit most.</p>"),
 ("Photograph products the way customers see them", "<p>People often search with a photo taken in real life, not in a studio. Alongside clean product shots, include photos of items in use or in a room, from the angles customers would see them. For a boutique in Anaheim or a home decor shop in Orange, that can make the difference between matching a shopper's photo and being missed.</p>"),
 ("Keep product details complete", "<p>When a shopper lands on your page from an image search, they want the essentials immediately: name, price, sizes or dimensions, availability and how to buy or visit. Put these near the main image so the visit turns into a sale or a trip to the store.</p>")],
"google-seo-learning-paths-small-business": [
 ("Make notes as you watch", "<p>Keep a short document of what you learn and one action for each video, such as checking which pages are indexed or comparing two seasonal searches in Google Trends. Notes turn passive viewing into changes on your site, and they make it easy to brief a colleague or agency later.</p>"),
 ("Questions to ask after the beginner path", "<ul><li>Is our site verified in Search Console, and who has access?</li><li>Which searches bring impressions but few clicks?</li><li>Which pages are not indexed, and why?</li><li>Which of our services have seasonal peaks in Google Trends?</li><li>What is one page we can improve this month?</li></ul>"),
 ("Keep learning after the playlists", "<p>Search changes constantly. Follow the Search Central blog for announcements, such as new Search Console reports, and review your own reports monthly. Short, regular learning keeps an owner in Anaheim or anywhere in Orange County informed without needing to become a full-time SEO specialist.</p>")],
}
for p in PAGES:
    for h, b in EXTRA.get(p["slug"], []):
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

MORE = {
"gemini-4-carbon-ai-mode-local-business": ("Questions customers may now ask AI", "<p>With deeper research models, customers can ask longer, more specific questions, such as which licensed electricians in Anaheim install EV chargers on weekends, or which Orange County caterers handle gluten-free menus for 200 guests. Look at the questions your customers ask on the phone and in emails, and make sure your website answers them in plain text. Those answers are what a careful model will look for when it builds a comparison, and they help human visitors too.</p>"),
"search-console-generative-ai-performance-report": ("What good looks like", "<p>There is no universal benchmark for AI impressions, so compare your site with itself over time. A healthy pattern for a local business is steady or rising impressions, a growing number of pages appearing and main service pages among them, not only blog posts. If impressions rise but calls and bookings do not, look at what those pages ask visitors to do next, and make sure contact details, booking links and service areas are easy to find on every page that appears in AI features.</p>"),
"search-console-multimodal-search-report": ("Local storefronts and landmarks", "<p>Image searches are not only about products. Visitors in Anaheim photograph storefronts, menus, signs and buildings to find out more. Make sure your storefront photos on your website and Business Profile match how the place looks today, with signage visible, and that your website names the business exactly as it appears on the sign. When someone searches with a photo of your shopfront, a clear match between image, name and website helps them land on the right place.</p>"),
"google-seo-learning-paths-small-business": ("How this connects to AI search", "<p>The fundamentals in the beginner path, how Google crawls, indexes and serves pages, also underpin Google's AI features such as AI Overviews and AI Mode, which draw on content Google can find and understand. Other AI assistants work from pages they can read too. Understanding crawling and indexing therefore helps with both regular search and AI answers. For an Orange County business, that means one set of skills supports visibility in Google, in AI features and in assistants that recommend local businesses.</p>"),
}
for p in PAGES:
    if p["slug"] in MORE:
        h, b = MORE[p["slug"]]
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

LAST = {
"search-console-multimodal-search-report": ("A quick checklist", "<ol><li>Open the performance report and apply the multimodal search type filter.</li><li>Note clicks, impressions and top pages.</li><li>Replace stock images with real photos of your products and work.</li><li>Add descriptive text, file names and alt text near each image.</li><li>Check pages load quickly on phones.</li><li>Update storefront photos on your Business Profile.</li></ol><p>Repeat the check each month and compare with the previous export.</p>"),
"google-seo-learning-paths-small-business": ("Where to find them", "<p>Both playlists are live on the Search Central YouTube channel's playlists page. Google suggests saving them to your library, sharing them with your team and subscribing for upcoming tutorials and deep dives. Start with the first video of the beginner path and keep a notebook open.</p>"),
}
for p in PAGES:
    if p["slug"] in LAST:
        h, b = LAST[p["slug"]]
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

if __name__ == "__main__":
    save_all(PAGES)
