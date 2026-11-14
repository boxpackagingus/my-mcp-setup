"""Blog posts for 2026-11-14 (5 posts). Every fact is checked at the linked Google source on 2026-11-14."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_13  # noqa: F401  (SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SRC.update({
    "g_hydrogen_model": {"title": "Google: Introducing Gemini 4 Hydrogen (Nov 12, 2026)",
                         "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/"},
    "g_platform_props": {"title": "Google Search Central blog: Platform properties roll out globally, plus a new social and video performance guide (Jul 29, 2026)",
                         "url": "https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide"},
    "sc_add": {"title": "Search Console Help: Add a website or platform property to Search Console",
               "url": "https://support.google.com/webmasters/answer/34592?hl=en"},
    "g_dining": {"title": "Google: Google Maps' first Fan-Favorite Dining list (Oct 8, 2026)",
                 "url": "https://blog.google/products-and-platforms/products/maps/google-maps-fan-favorite-dining-list/"},
    "g_whentobuy": {"title": "Google: When to Buy Guide, holiday shopping tips for 2026 (Oct 15, 2026)",
                    "url": "https://blog.google/products-and-platforms/products/shopping/holiday-shopping-when-to-buy-guide/"},
    "g_wallet_gemini": {"title": "Google: Connect Google Wallet to Gemini for personal finance insights (Nov 13, 2026)",
                        "url": "https://blog.google/innovation-and-ai/products/gemini-app/google-wallet-gemini-app/"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")
GEMSEO = L("Gemini SEO", "gemini-seo")
SMB = L("AI SEO for small business", "ai-seo-for-small-business")
HYDRO_SEARCH = L("Gemini 4 Hydrogen in Google Search", "gemini-4-hydrogen-google-search-upgrade")
SC_SETUP = L("how to set up Google Search Console", "how-to-set-up-google-search-console")
SC_PERF = L("Search Console Performance report", "google-search-console-performance-report")
YT = L("YouTube for AI search", "youtube-for-ai-search")
REST = L("SEO for restaurants in Orange County", "seo-for-restaurants-orange-county")
COFFEE = L("SEO for coffee shops", "seo-for-coffee-shops")
BOBA = L("SEO for bubble tea shops", "seo-for-bubble-tea-shops")
H100 = L("Google's Holiday 100 for Orange County retailers", "google-holiday-100-orange-county-retailers")
CART = L("Google's universal cart for retailers", "google-universal-cart-orange-county-retailers")
PRODUCT = L("product pages for AI shopping", "product-pages-for-ai-shopping")
GYMS = L("SEO for gyms", "seo-for-gyms")
GBP = L("Google Business Profile optimization", "google-business-profile-optimization-orange-county")
REVIEWS = L("how to get more Google reviews", "how-to-get-more-google-reviews")


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def dining_chart(after):
    items = [("Froyo, New York", 320), ("Mochi, Tokyo", 168), ("Dosas, Seattle", 136), ("Hojicha, London", 114),
             ("Cinnamon buns, Montréal", 84), ("Matcha, Santiago", 84), ("Matcha, Chicago", 82), ("Beef tallow, Chicago", 82),
             ("Beignets, Atlanta", 77), ("Ube, Melbourne", 75)]
    return {"after": after, "type": "bars", "eyebrow": "Google Maps data", "title": "Year-over-year growth in review mentions",
            "lead": "From Google Maps' first Fan-Favorite Dining List, based on reviews, ratings and direction searches in 10 cities.",
            "unit": "%", "chart_label": "Increase in review mentions",
            "items": [{"label": a, "value": v, "display": f"+{v}%"} for a, v in items],
            "source": {"title": "Google, Oct 8, 2026", "url": SRC["g_dining"]["url"]}}


PAGES = [
# 1 ------------------------------------------------------------------
blog(1, "AI news",
     slug="gemini-4-hydrogen-small-business", query="gemini 4 hydrogen", kw="Gemini 4 Hydrogen",
     eyebrow="AI news", short_title="What Gemini 4 Hydrogen means for small businesses",
     title="Gemini 4 Hydrogen: What Small Businesses Can Use",
     meta="Gemini 4 Hydrogen is now available across the Gemini app, Gemini for business, Sheets and the API. What Anaheim and Orange County businesses can do with it.",
     h1="Gemini 4 Hydrogen: What Google's New Everyday Model Means for Small Businesses",
     answer="Gemini 4 Hydrogen, released November 12, 2026, is Google's fast, efficient model for everyday work. Google says it's available to everyone in the Gemini app, Google Search, Gemini for business, Google AI Studio and the Gemini API, priced at $1.50 per million input tokens for developers. For Anaheim and Orange County businesses, it means faster help with documents, spreadsheets and research.",
     takeaways=["Released November 12, 2026.", "Available in the Gemini app, Search, Gemini for business and the API.",
                "Developer price: $1.50 per million input tokens, $7.50 per million output.", "Built for speed in everyday tasks.",
                "Google says it cuts fabricated claims by more than 5x versus Gemini 3.8 Flash."],
     sections=[
      ("What Google announced", "<p>On November 12, 2026, Koray Kavukcuoglu, Senior Vice President at Google DeepMind and Google's Chief AI Architect, introduced Gemini 4 Hydrogen. Google describes it as bringing cutting-edge intelligence to everyone, with speed and efficiency for everyday coding and agentic workflows. It sits alongside Gemini 4 Carbon and Argon, which Google positions for deep, long reasoning on the hardest problems.</p>"),
      ("Where it's available", ul(["The Gemini app and Google Search.", "Gemini for business.", "All tiers of Google AI Studio and the Gemini API.",
                                    "Google Antigravity for paid Google AI Pro and Ultra subscribers."])),
      ("How it compares", "<p>Google says Hydrogen surpasses Argon on the Artificial Analysis Intelligence Index at its default high thinking level, scoring 51 versus 50, and reaching 54 at its highest setting, while often completing tasks faster than models in its class.</p>"),
      ("Improvements over the previous fast model", "<table><tr><th>Measure Google reports</th><th>Hydrogen vs Gemini 3.8 Flash</th></tr><tr><td>Task speed at default setting</td><td>2.5 times faster</td></tr><tr><td>Terminal-Bench 4.1</td><td>57% vs 18.2%</td></tr><tr><td>Fabricated claims</td><td>Cut by more than 5x</td></tr></table><p>Source: Google, November 12, 2026.</p>"),
      ("Pricing for developers", "<p>Google says Hydrogen is priced flat across its 1 million-token context window at $1.50 per million input tokens and $7.50 per million output tokens. That's lower than the introductory Carbon price Google announced on November 10, which makes Hydrogen the practical choice for most small-business tools.</p>"),
      ("Working with documents and data", "<p>Google says Hydrogen accepts up to 1 million input tokens and can produce up to 1 million output tokens, synthesizing dense PDFs, spreadsheets, charts, audio and recorded video into cited reports. For a small business, that means summarizing long contracts, supplier catalogs or months of customer feedback faster.</p>"),
      ("In Google Sheets and Slides", "<p>Google gives examples of Hydrogen turning financial data into interactive models in Google Sheets, generating outputs over 30% faster than previous models in Sheets canvas, and building a multi-slide presentation in Google Slides from a video and a template. Business owners who live in spreadsheets may notice the difference first.</p>"),
      ("Why fewer fabricated claims matter", "<p>Google reports Hydrogen cuts fabricated claims by more than 5x compared with Gemini 3.8 Flash. For businesses using AI to draft customer-facing content, fewer invented facts means less risk, though every draft still needs a human check.</p>"),
      ("What it means for search visibility", "<p>Hydrogen also powers Google Search, which Google upgraded the same day. As AI in Search gets faster and better at following detailed questions, clear and accurate business information matters even more.</p>"),
      ("Practical uses for a local business", ol(["Summarize long documents, such as leases or vendor contracts, before review with your adviser.",
                                                 "Analyze sales or booking data in Sheets to spot seasonal patterns.",
                                                 "Draft service page outlines, then edit them with your own expertise and facts.",
                                                 "Turn customer reviews into themes to improve your service.",
                                                 "Prepare quick presentations for staff or partners."])),
      ("Keep a human in the loop", "<p>Faster AI is still AI. Check facts, prices and claims before anything goes to customers, and don't paste sensitive customer data into tools without understanding how it's handled under your plan.</p>"),
      ("A worked example", "<p>Imagine a catering company in Orange that exports a year of orders to Google Sheets and asks Gemini to find which menus and months bring the most revenue. Within minutes, it sees that corporate holiday events in December and graduation parties in June are its most profitable work, and plans its marketing calendar around them.</p>"),
      ("The short version", "<p>Gemini 4 Hydrogen is Google's fast, affordable model, now available almost everywhere Google offers Gemini. Anaheim and Orange County businesses can use it for documents, data and drafts, with a human checking the results.</p>")],
     faqs=[("What is Gemini 4 Hydrogen?", "Google's fast, efficient Gemini 4 model for everyday work, released November 12, 2026."),
           ("Where can I use Gemini 4 Hydrogen?", "The Gemini app, Google Search, Gemini for business, Google AI Studio and the Gemini API."),
           ("How much does Gemini 4 Hydrogen cost for developers?", "Google lists $1.50 per million input tokens and $7.50 per million output tokens."),
           ("Is Hydrogen better than Gemini 4 Argon?", "Google says it scores 51 vs 50 on the Artificial Analysis Intelligence Index at default settings."),
           ("Does it make fewer mistakes?", "Google says it cuts fabricated claims by more than 5x versus Gemini 3.8 Flash."),
           ("Can it work with spreadsheets?", "Yes. Google gives examples in Google Sheets and Slides."),
           ("Should small businesses use it for customer content?", "For drafts, with a human checking every fact."),
           LOCAL_FAQ],
     links=[HYDRO_SEARCH, GEMSEO, SMB, LOCAL, AUD],
     sources=["g_hydrogen_model"],
     visuals=[V.flow(5, "Where Hydrogen shows up", "From Google's November 12, 2026 announcement.",
               [("Gemini app", "Everyday help."), ("Search", "Faster AI answers."),
                ("Workspace", "Sheets and Slides examples."), ("API", "$1.50 per million input tokens.")])],
     secondary=["Gemini 4 Hydrogen pricing", "Gemini for business", "Gemini in Google Sheets", "Gemini 4 Hydrogen vs Argon"],
     hero_query="Can my small business use Gemini 4 Hydrogen?"),

# 2 ------------------------------------------------------------------
blog(2, "Search Console",
     slug="search-console-platform-properties-social", query="search console platform properties", kw="Search Console platform properties",
     eyebrow="Search Console", short_title="Search Console platform properties for your social accounts",
     title="Search Console Platform Properties: Social in Search",
     meta="Search Console platform properties show how your Instagram, TikTok, X and YouTube posts perform in Google Search. How Orange County businesses can use them.",
     h1="Search Console Platform Properties: See How Your Social Posts Perform in Google Search",
     answer="Search Console platform properties let you track how your posts on Instagram, TikTok, X and YouTube perform in Google Search, Discover and Google News. Google made them available globally on July 29, 2026. For Anaheim and Orange County businesses that post on social media, they show which posts people find through Google and what they searched.",
     takeaways=["Platform properties cover Instagram, TikTok, X and YouTube.", "They show performance in Search, Discover and News.",
                "Available globally since July 29, 2026.", "Verification by website property or platform login.", "Google published a guide to analyzing social and video performance."],
     sections=[
      ("What Google launched", "<p>Google's Search Central blog announced platform properties for Search Console in July 2026, and on July 29, 2026 made them globally available. They let you track how social and video posts on Instagram, TikTok, X and YouTube perform on Google Search, Discover and Google News.</p>"),
      ("What a platform property is", "<p>Search Console's help page explains that platform properties represent your presence on supported platforms, such as instagram.com/username. You verify them either through an automated connection with an existing website property or by logging in to the platform directly.</p>"),
      ("Why local businesses should care", "<p>Many Orange County businesses post more often on Instagram or TikTok than on their websites. When those posts appear in Google Search, they bring attention that's hard to measure inside the social apps. Platform properties show which posts Google sends people to and what they searched for.</p>"),
      ("Understand your Search audience", "<p>Google suggests using the Insights report to find top, trending up and trending down query groups sending people from Google Search to your social and video content. Those themes show what your audience cares about and can inspire your next post, caption or video.</p>"),
      ("Spot trending posts", "<p>Google recommends the 24-hour filter to spot sudden traffic spikes from Search to recent posts, so you can cross-promote them on other platforms while interest is high.</p>"),
      ("Compare across platforms", "<p>Google suggests exporting performance data from several platform properties into one spreadsheet to compare YouTube, Instagram, X and TikTok side by side.</p>"),
      ("Refresh older content", "<p>Google points out that Search Console can show older videos regaining search traction, which might be worth pinning or following up with a part two. Search Console annotations can track whether changes, such as a new YouTube title or TikTok caption, affect performance.</p>"),
      ("How to add one", ol(["Open the property selector in Search Console and select Add property.", "Choose a platform property and the platform.",
                             "Connect through your verified website property, or log in to the platform.", "Open the Performance and Insights reports for that account."])),
      ("Already have a Search profile?", "<p>Google says that if you've already set up your Search profile, you should have access to data for the same platform in Search Console.</p>"),
      ("Captions and titles as search text", "<p>Because people find posts through Google Search, captions, titles and descriptions work like page titles. Mention the service, place and question your post answers, such as a before-and-after kitchen remodel in Irvine, rather than only emojis and hashtags.</p>"),
      ("A worked example", "<p>Imagine a nail salon in Anaheim with a busy Instagram account. After adding a platform property, it sees that posts about gel extensions get impressions from Google searches for gel nails near Disneyland. The salon writes clearer captions mentioning gel extensions and Anaheim, and creates a matching service page on its website.</p>"),
      ("Measure alongside your website", "<p>Keep your website property and platform properties in the same account, check both monthly and compare which topics perform on each. Topics that do well on social are good candidates for full website pages.</p>"),
      ("The short version", "<p>Search Console platform properties show how your Instagram, TikTok, X and YouTube posts perform in Google. Anaheim and Orange County businesses can use them to write better captions, spot trends and decide what to post next.</p>")],
     faqs=[("What are Search Console platform properties?", "Properties that track how your Instagram, TikTok, X and YouTube posts perform on Google."),
           ("Which platforms are supported?", "Google lists Instagram, TikTok, X and YouTube."),
           ("When did they become available to everyone?", "July 29, 2026."),
           ("How do I verify a platform property?", "Through your existing website property or by logging in to the platform."),
           ("What can I learn from them?", "Which queries and posts bring Google traffic, and trending posts."),
           ("Do I need a website property too?", "It's recommended, and it can be used to connect platform properties."),
           ("Do captions matter for Google Search?", "Yes. Clear captions and titles help people find posts through Search."),
           LOCAL_FAQ],
     links=[SC_SETUP, SC_PERF, YT, LOCAL, AUD],
     sources=["g_platform_props", "sc_add"],
     visuals=[V.flow(4, "Using platform properties", "From Google's July 29, 2026 post.",
               [("Add", "Platform property in Search Console."), ("Insights", "Query groups by topic."),
                ("Trending", "24-hour filter for spikes."), ("Act", "Better captions and new pages.")])],
     secondary=["Search Console Instagram", "Search Console TikTok", "Search Console YouTube", "social media in Google Search"],
     hero_query="Can I see how my Instagram posts perform in Google Search?"),

# 3 ------------------------------------------------------------------
blog(3, "Search Trends",
     slug="google-maps-dining-trends-restaurants", query="google maps fan favorite dining", kw="Google Maps dining trends",
     eyebrow="Google Maps", short_title="Google Maps dining trends for Orange County restaurants",
     title="Google Maps Dining Trends: Lessons for Restaurants",
     meta="Google Maps' Fan-Favorite Dining List shows matcha, froyo and ube trending. What these Google Maps dining trends mean for Anaheim and Orange County restaurants.",
     h1="Google Maps Dining Trends: What the Fan-Favorite Dining List Teaches Orange County Restaurants",
     answer="Google Maps' first Fan-Favorite Dining List, from October 8, 2026, used reviews, ratings and direction searches to find Google Maps dining trends in 10 cities: matcha grew in nearly all of them, froyo mentions in New York rose 320% and ube rose 75% in Melbourne. For Anaheim and Orange County restaurants, it shows how reviews and menus shape discovery.",
     takeaways=["Google analyzed reviews, ratings and direction searches.", "The list covers 10 cities, none in Orange County.",
                "Matcha grew double digits in nearly all 10 cities.", "Review mentions of froyo in New York rose 320%.", "Specific dishes in reviews and menus drive discovery."],
     sections=[
      ("What Google published", "<p>On October 8, 2026, Google Maps released its first Fan-Favorite Dining List. Google says it used Maps reviews, ratings and aggregated searches for directions to find dining trends across 10 cities: Atlanta, Chicago, London, Melbourne, Montréal, New York, San Francisco, Santiago, Seattle and Tokyo.</p>"),
      ("Not Orange County data", "<p>None of the 10 cities is in Orange County, so these numbers don't describe local diners. What they do show is how Google Maps reads reviews and searches to spot trends, which applies to every restaurant on Maps.</p>"),
      ("Trend 1: classic treats came back", "<p>Google says reviews mentioning froyo in New York rose 320% year over year, cinnamon buns in Montréal rose 84% and mochi in Tokyo rose 168%, which Google links to record tourism.</p>"),
      ("Trend 2: matcha and earthy flavors", "<p>Google says matcha grew by double digits year over year in nearly all 10 cities, including 82% in Chicago and 84% in Santiago, and by over 50% in Seattle, San Francisco, New York and Atlanta. Hojicha mentions rose 114% in London and ube 75% in Melbourne.</p>"),
      ("Trend 3: crispy and golden comfort food", "<p>Google reports review mentions of beef tallow up 82% in Chicago, dosas up 136% in Seattle and beignets up 77% in Atlanta.</p>"),
      ("Beyond trends", "<p>The list also names the most-navigated-to dining spot in each city, such as La Taqueria in San Francisco and Katz's Delicatessen in New York, and top-reviewed spots for big portions and small checks.</p>"),
      ("What this shows about Maps", "<p>Google built the list from what people write in reviews and where they ask for directions. Specific dish names in reviews are visible signals. When diners mention your matcha latte, ube dessert or birria tacos by name, that detail is part of how Maps understands what you're known for.</p>"),
      ("What Orange County restaurants can do", ol(["Publish your menu as text on your website and Business Profile, with dish names people search for.",
                                                    "Ask happy customers to mention the dish they loved in their review.",
                                                    "Add photos of signature dishes to your profile.",
                                                    "Reply to reviews and mention the dish when it fits naturally.",
                                                    "Highlight seasonal or trending items you genuinely serve."])),
      ("Don't chase every trend", "<p>Adding matcha or ube to a menu only makes sense if it fits your kitchen and customers. The lesson is to make what you already do well visible, not to copy another city's trend.</p>"),
      ("A worked example", "<p>Imagine a cafe in Garden Grove known for its pandan and ube pastries. Its menu exists only as a photo, and reviews just say great place. The owner publishes the menu as text, adds photos of the ube croissant to the Business Profile and asks regulars who love it to mention it by name. Over time, reviews and the menu tell Maps exactly what the cafe is known for.</p>"),
      ("The short version", "<p>Google's Fan-Favorite Dining List shows Maps finds trends in what diners write and where they go. Anaheim and Orange County restaurants should publish menus as text, show signature dishes and encourage specific reviews.</p>")],
     faqs=[("What is Google Maps' Fan-Favorite Dining List?", "A list of dining trends and popular spots in 10 cities, based on Maps reviews, ratings and direction searches."),
           ("Which cities are included?", "Atlanta, Chicago, London, Melbourne, Montréal, New York, San Francisco, Santiago, Seattle and Tokyo."),
           ("Is Orange County included?", "No. None of the 10 cities is in Orange County."),
           ("What was the biggest trend?", "Matcha grew double digits in nearly all 10 cities; froyo mentions in New York rose 320%."),
           ("How did Google find the trends?", "From Maps reviews, ratings and aggregated searches for directions."),
           ("What should restaurants do?", "Publish text menus, show signature dishes and encourage specific reviews."),
           ("Should I add trending items to my menu?", "Only if they fit your kitchen and customers."),
           LOCAL_FAQ],
     links=[REST, COFFEE, BOBA, REVIEWS, LOCAL, AUD],
     sources=["g_dining"],
     visuals=[dining_chart(4)],
     secondary=["Google Maps food trends", "matcha trend", "restaurant reviews Google Maps", "Fan-Favorite Dining List"],
     hero_query="What food trends is Google Maps seeing this year?"),

# 4 ------------------------------------------------------------------
blog(4, "Shopping trends",
     slug="google-when-to-buy-holiday-retailers", query="google when to buy guide", kw="Google's When to Buy Guide",
     eyebrow="Holiday shopping", short_title="Google's When to Buy Guide for Orange County retailers",
     title="Google's When to Buy Guide: Tips for Retailers",
     meta="Google's When to Buy Guide shows when holiday discounts peak by category. What it means for Anaheim and Orange County retailers planning promotions and stock.",
     h1="Google's When to Buy Guide: How Orange County Retailers Can Time Holiday Promotions",
     answer="Google's When to Buy Guide, published October 15, 2026, uses last year's promotional patterns, Search trends and discount data from U.S. merchants to show when holiday deals peak by category. Fragrance deals thin out after early December, while large luggage and motorized tech toys see their deepest markdowns in late December. Anaheim and Orange County retailers can use it to plan promotions and stock.",
     takeaways=["Published October 15, 2026.", "Based on last year's U.S. merchant discount data and Search trends.",
                "Fragrance: best in the two weeks after Black Friday weekend.", "Large luggage and tech toys: deepest markdowns in late December.",
                "Google calls it general guidance, not a guarantee."],
     sections=[
      ("What Google published", "<p>On October 15, 2026, Google shared its When to Buy Guide, which it describes as a research-backed roadmap showing when holiday discounts may hit their peak. Google says it analyzed historical promotional patterns, Search trends and discount data across U.S. merchants on Google, based on last year's data.</p>"),
      ("The category findings", "<table><tr><th>Category</th><th>When Google says deals are best</th></tr><tr><td>Fragrance</td><td>Within the first two weeks after Black Friday weekend</td></tr><tr><td>Handbags</td><td>Mid-December for balance; late December for lowest prices</td></tr><tr><td>Travel accessories</td><td>November</td></tr><tr><td>Large luggage and suitcases</td><td>Late December clearance</td></tr><tr><td>Motorized tech toys</td><td>Final weeks of December</td></tr></table><p>Source: Google, October 15, 2026.</p>"),
      ("Fragrance: early is better", "<p>Google says fragrance discounts don't typically increase as Christmas approaches, and the volume of fragrance deals drops off sharply, so waiting until late December may not bring lower prices and could mean fewer options.</p>"),
      ("Handbags: not on Black Friday", "<p>Google suggests holding off on handbags during Black Friday weekend, targeting mid-December for a balance of discount and selection, or late December for the lowest prices on remaining stock.</p>"),
      ("Travel: accessories early, luggage late", "<p>Google says travel accessories see their best deals in November, while large luggage and suitcases usually hit their deepest markdowns in late December clearance sales.</p>"),
      ("Tech toys: wait", "<p>Unlike traditional electronics, Google says motorized tech toys show some of their steepest markdowns in the final weeks of December.</p>"),
      ("Guidance, not guarantees", "<p>Google notes pricing and inventory vary from year to year and calls the findings general guidance rather than absolute guarantees. Use them alongside your own sales history.</p>"),
      ("What it means for local retailers", "<p>Shoppers who read this guide will time their purchases. A boutique in Fullerton selling fragrance can expect demand right after Black Friday, while a luggage shop near Anaheim's resorts may see bargain hunters wait for late December. Planning promotions around those expectations helps you compete.</p>"),
      ("Plan your promotions", ol(["Match promotion timing to when shoppers expect deals in your category.", "Make sure product pages show current prices and stock.",
                                   "Update your Google Business Profile with holiday hours and posts about offers.", "Promote in-store pickup for last-minute shoppers who miss shipping deadlines.",
                                   "Track which promotions bring visits and sales."])),
      ("Shipping deadlines favor local stores", "<p>Google reminds shoppers who wait to keep an eye on shipping deadlines unless they plan to shop in-store. That's an opportunity for Orange County stores: late shoppers who can't wait for delivery look for local stock and pickup.</p>"),
      ("A worked example", "<p>Imagine a toy store in Tustin. Knowing shoppers may wait for late-December deals on tech toys, it holds back its biggest toy discounts until the final weeks, promotes in-store availability and pickup, and posts updates on its Business Profile. Earlier in the season, it focuses on gift guides and items that don't follow the late-discount pattern.</p>"),
      ("The short version", "<p>Google's When to Buy Guide shows when shoppers expect the best deals by category. Anaheim and Orange County retailers can time promotions, keep product pages accurate and win last-minute shoppers with local stock.</p>")],
     faqs=[("What is Google's When to Buy Guide?", "Google's 2026 research on when holiday discounts tend to peak by category."),
           ("What data is it based on?", "Last year's promotional patterns, Search trends and U.S. merchant discount data on Google."),
           ("When are fragrance deals best?", "Google says within the first two weeks after Black Friday weekend."),
           ("When are luggage deals best?", "Google says late December clearance for large luggage."),
           ("When are tech toy deals best?", "Google says the final weeks of December."),
           ("Is the guide guaranteed?", "No. Google calls it general guidance."),
           ("How can local stores benefit?", "Promote in-store stock and pickup for late shoppers who miss shipping deadlines."),
           LOCAL_FAQ],
     links=[H100, CART, PRODUCT, GBP, LOCAL, AUD],
     sources=["g_whentobuy"],
     visuals=[V.flow(2, "Holiday timing by category", "From Google's October 15, 2026 guide.",
               [("November", "Travel accessories."), ("After Black Friday", "Fragrance."),
                ("Mid-December", "Handbags."), ("Late December", "Luggage and tech toys.")])],
     secondary=["holiday discount timing", "when to buy holiday gifts", "holiday retail promotions", "Black Friday deals timing"],
     hero_query="When should my store run holiday promotions?"),

# 5 ------------------------------------------------------------------
blog(5, "AI assistants",
     slug="google-wallet-gemini-subscriptions-local-business", query="google wallet gemini", kw="Google Wallet in Gemini",
     eyebrow="AI news", short_title="Google Wallet in Gemini and your customers' subscriptions",
     title="Google Wallet in Gemini: What Local Businesses Learn",
     meta="Gemini can now review spending and subscriptions through Google Wallet. What it means for Anaheim and Orange County businesses with memberships and plans.",
     h1="Google Wallet in Gemini: Why Membership Businesses Should Pay Attention",
     answer="Since November 13, 2026, Gemini app users in the U.S. can connect Google Wallet so Gemini can review their spending, find recurring subscriptions, flag price increases and suggest holiday budgets. Gemini can only read the data, not move money. For Anaheim and Orange County businesses with memberships or plans, customers may now review your charges with AI.",
     takeaways=["Announced November 13, 2026.", "Available to all Gemini app users in the U.S.", "Gemini can find recurring charges and price increases.",
                "Gemini can only read Wallet data, not move money.", "The connection is optional and can be turned off."],
     sections=[
      ("What Google announced", "<p>On November 13, 2026, Google added Google Wallet to the apps Gemini can connect to through Personal Intelligence. Google says it's rolling out to all Gemini app users in the U.S., on web, Android and iOS, so they can get responses informed by their spending habits.</p>"),
      ("What people can ask", ul(["Review spending from last quarter and plan savings, with charts generated in the chat.",
                                  "Find subscriptions they're still paying for and whether any went up in price this year.",
                                  "Look at last year's spending on gifts and travel to set a holiday budget."])),
      ("Linking bank accounts", "<p>Google says users can also link credit card and bank accounts to Wallet through Plaid for deeper insights, and tag @Google Wallet in Gemini to ask finance questions.</p>"),
      ("Privacy and control", "<p>Google says Gemini can only read information from connected accounts; it can't move, manage or invest money. Users choose whether to connect Wallet under Connected Apps in Personal Intelligence settings and can turn it off at any time.</p>"),
      ("Why membership businesses should care", "<p>When a customer asks Gemini what subscriptions they're still paying for and whether any went up, every gym membership, salon plan, meal kit, car wash club and maintenance plan they pay for can show up in the answer, including recent price increases. That makes value and clarity more important.</p>"),
      ("Price increases get noticed", "<p>Google's example specifically mentions flagging subscriptions that went up in price this year. If you raise prices, tell members clearly and explain what they get, before an AI summary points it out for them.</p>"),
      ("Make the charge recognizable", "<p>Customers often cancel charges they don't recognize. Make sure your business name on card statements is clear and matches your brand, so a list of recurring charges doesn't show a confusing name.</p>"),
      ("Show value every month", ol(["Remind members what they've used: classes attended, services received or savings earned.",
                                     "Explain any price change in advance, with the reason.", "Make it easy to pause or change plans instead of cancelling.",
                                     "Ask happy members for reviews.", "Keep your website's membership page clear and current."])),
      ("Holiday budgets", "<p>Google's example of setting a holiday budget from last year's spending shows that customers may plan gift and travel spending more carefully. Local retailers and gift-card sellers should make offers easy to understand and compare.</p>"),
      ("A worked example", "<p>Imagine a fitness studio in Yorba Linda that raised its monthly fee in the spring. A member asks Gemini which subscriptions increased this year, and the studio appears on the list. Because the studio sent a clear email explaining new classes and equipment, and the member attends three times a week, they keep the membership. A gym that raised prices quietly might not be so lucky.</p>"),
      ("The short version", "<p>Google Wallet in Gemini lets U.S. users ask AI to review their subscriptions and spending. Anaheim and Orange County businesses with memberships should communicate value and price changes clearly and make their charges easy to recognize.</p>")],
     faqs=[("What is Google Wallet in Gemini?", "A connection that lets Gemini give answers informed by your spending in Google Wallet."),
           ("Who can use it?", "Google says all Gemini app users in the U.S."),
           ("Can Gemini move money?", "No. Google says it can only read information, not move, manage or invest money."),
           ("Can Gemini find subscriptions?", "Yes. Google says it can find recurring charges and flag price increases."),
           ("Is the connection automatic?", "No. Users choose to connect it and can turn it off."),
           ("What should membership businesses do?", "Communicate value and price changes clearly and use a recognizable statement name."),
           ("Can people link bank accounts?", "Yes, through Plaid in Wallet, according to Google."),
           LOCAL_FAQ],
     links=[GYMS, GEMSEO, REVIEWS, GBP, LOCAL, AUD],
     sources=["g_wallet_gemini"],
     visuals=[V.flow(4, "How a customer reviews subscriptions", "From Google's November 13, 2026 announcement.",
               [("Connect", "Google Wallet in Gemini."), ("Ask", "Which subscriptions am I paying for?"),
                ("Review", "Recurring charges and price increases."), ("Decide", "Keep, pause or cancel.")])],
     secondary=["Gemini personal finance", "Google Wallet Gemini subscriptions", "membership retention", "Gemini Personal Intelligence"],
     hero_query="Can customers use Gemini to find and cancel my subscription?"),
]

EXTRA = {
"gemini-4-hydrogen-small-business": [
 ("Four thinking levels", "<p>Google says Hydrogen offers four thinking levels, from low to an extra-high setting, so developers can trade speed for depth. For small businesses using tools built on the API, that can mean quick answers for simple tasks and more careful reasoning for complex ones, without switching models.</p>"),
 ("Questions owners ask us", "<p>Owners often ask whether they need a developer to use Hydrogen. No: it's available in the Gemini app and Gemini for business, so anyone can use it for drafts, summaries and analysis. Developers use the API to build custom tools such as quoting assistants or internal search. Another question is which model to choose. For most everyday tasks, a fast model like Hydrogen is enough; the more expensive frontier models are for the hardest, longest tasks. Owners also ask about data privacy. Check the terms of your plan, especially before pasting customer information, and prefer business plans for work data.</p>")],
"search-console-platform-properties-social": [
 ("What to post when you know what people search", "<p>Once you can see the queries that lead to your posts, plan content around them. If people find your bakery's TikTok through searches for custom birthday cakes in Anaheim, post more cake decorating videos with clear captions and link to an order page. If a roofer's YouTube walkthrough of a tile roof repair keeps getting impressions, make more of those and add a written version on the website. Social platforms reward engagement, while Google rewards relevance; clear titles and captions serve both.</p>"),
 ("Questions owners ask us", "<p>Owners often ask whether platform properties replace the analytics inside Instagram or TikTok. They don't: those show activity within the app, while Search Console shows how Google Search, Discover and News send people to your posts. Another question is whether this helps local SEO directly. It shows demand and topics that you can also cover on your website and Business Profile. Owners also ask if it's worth it for small accounts. Setup takes minutes, and even a small account can learn which posts Google surfaces.</p>")],
"google-maps-dining-trends-restaurants": [
 ("Questions owners ask us", "<p>Owners often ask whether they can ask customers to mention specific dishes in reviews. You can ask for honest reviews and suggest they mention what they ordered, but never offer rewards for reviews or write them yourself; Google's policies prohibit fake engagement. Another question is whether Google will publish a list for Orange County. Google hasn't said, so focus on the signals you control. Owners also ask how menus help on Maps. Text menus and dish photos make it easier for Maps and AI assistants to match your restaurant to searches for specific dishes.</p>"),
 ("Your own trend check", "<p>You don't need Google's list to see your own trends. Read your last 50 reviews and note which dishes come up most, check which menu items sell best by month and look at the search terms in your Business Profile performance report. Together, these show what you're becoming known for. Feature those items in photos, posts and your website, and train staff to mention them to first-time guests.</p>")],
"google-when-to-buy-holiday-retailers": [
 ("Check your own data too", "<p>Google's guide is based on national patterns across U.S. merchants. Your store's customers may behave differently, especially in a visitor-heavy area like Anaheim or a gift-focused shopping district. Compare last year's sales by week for your main categories with Google's findings, and adjust where your own data disagrees. The best plan uses both.</p>"),
 ("Questions owners ask us", "<p>Owners often ask whether to discount early or wait. It depends on the category and on your stock: if shoppers in your category expect late discounts, early full-price sales to eager buyers and later clearance can both work. Another question is how to compete with large retailers. Local stock, pickup, personal service and gift wrapping matter more to last-minute shoppers than a few extra dollars off. Owners also ask about online visibility. Keep product pages and your Business Profile accurate so shoppers searching nearby find what you actually have in stock.</p>")],
"google-wallet-gemini-subscriptions-local-business": [
 ("Questions owners ask us", "<p>Owners often ask whether Gemini can cancel subscriptions automatically. Google says it can't move or manage money; it only reads information, so customers still decide and act themselves. Another question is whether this affects businesses outside the U.S. Google says the rollout is for Gemini app users in the U.S. Owners also ask what to change first. Start with the statement name on card charges and a clear membership page that lists what's included and what it costs.</p>"),
 ("A retention checklist", "<p>Review your membership or plan from a customer's point of view. Is the price easy to find? Are benefits clear? Do members get a regular reminder of what they've used? Is there a pause option? Are price changes announced in advance with reasons? Each yes makes it more likely that a member who sees your charge in an AI summary decides it's worth keeping. For Orange County businesses that rely on recurring revenue, such as gyms, studios, salons and car washes, this is worth an afternoon.</p>")],
}
for p in PAGES:
    for h, b in EXTRA.get(p["slug"], []):
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

MORE = {
"gemini-4-hydrogen-small-business": [
 ("Where it fits in a small business", "<p>Think of Hydrogen as a fast assistant for repetitive knowledge work. Office managers can summarize long email threads and documents, owners can turn exported sales data into clear charts, and marketing staff can draft outlines and first versions of posts that they then edit with real details. Front-desk teams can prepare answers to common customer questions, checked against your policies. The common thread is speed on tasks where a person still makes the final call. For a business in Anaheim or anywhere in Orange County with a small team, that time saved is the main benefit.</p>")],
"search-console-platform-properties-social": [
 ("Writing captions that work in Search", "<p>Write the first line of a caption as if it were a headline someone could search for: what the post shows, for whom and where. A restaurant might write Birria tacos and consommé in Anaheim, made fresh every weekend rather than only using emojis. A contractor might write Before and after: tile roof repair in Mission Viejo. Keep hashtags, but don't rely on them alone. Use the same words customers use in reviews and search terms, which you can see in Search Console and your Business Profile performance report.</p>"),
 ("A monthly social and search review", "<p>Once a month, open each platform property's Performance and Insights reports alongside your website property. Note the top queries and posts on each platform, any topics trending up and posts that are regaining traction. Pick one topic that performs well on social but has no page on your website, and create that page. Pick one older post worth refreshing or pinning. Over a few months, your social accounts and website start supporting each other, and you can see which content earns attention in Google, not just in the app.</p>")],
"google-maps-dining-trends-restaurants": [
 ("Why reviews are discovery signals", "<p>Google built the list partly from what people write in Maps reviews. When reviewers mention specific dishes, those words describe your restaurant in a way your own marketing can't. They help Google, and AI assistants that draw on reviews, connect your business to searches for that dish. A restaurant with hundreds of reviews that only say good food is harder to match to a specific craving than one whose reviews mention the house-made tortillas, the matcha tiramisu or the late-night menu.</p>"),
 ("Orange County's own food scene", "<p>Orange County has its own strong food traditions, from Vietnamese restaurants in Little Saigon to Korean barbecue, taquerias, boba shops and cafes near Anaheim's attractions. Whatever your cuisine, the same approach works: make your signature dishes easy to find in your menu, photos and reviews. When a visitor in Anaheim asks Google Maps or an AI assistant for the best pho or the best boba nearby, those details decide who appears.</p>")],
"google-when-to-buy-holiday-retailers": [
 ("Make online stock match the shelf", "<p>Shoppers who wait for late-December deals often search for what's available nearby right now. If your website or product listings show items you've sold out of, or miss items you have, you lose those visits. Keep stock levels and prices current online during the holidays, and use your Google Business Profile posts to highlight what's in stock, holiday hours and pickup options. For stores in busy Orange County shopping areas, accurate local stock information can turn a last-minute search into a visit within the hour.</p>"),
 ("A holiday calendar for local retailers", "<p>Use Google's findings to sketch a simple calendar. In early November, publish gift guides and highlight travel accessories. Over Black Friday weekend and the two weeks after, feature categories where shoppers expect early deals, such as fragrance. In mid-December, promote categories where shoppers balance price and selection, such as handbags. In the final weeks, emphasize in-store pickup, gift cards and clearance for categories that shoppers expect to drop late, such as large luggage and tech toys. Adjust each step with your own sales history.</p>")],
"google-wallet-gemini-subscriptions-local-business": [
 ("Why clarity beats discounts", "<p>When a customer reviews subscriptions with AI, the question is simple: is this worth it? A discount might keep a member for a month, but clear value keeps them for years. Members who understand what they get, use it regularly and feel well treated rarely cancel because a charge appears on a list. That's why communication, usage reminders and a fair price-change policy matter more than ever for gyms, studios, salons, car washes and other membership businesses across Anaheim and Orange County.</p>"),
 ("Gift cards and holiday budgets", "<p>Google's example of building a holiday budget from last year's spending suggests some shoppers will plan gift spending more carefully this year. Gift cards and gift memberships are easy to fit into a budget when the price and value are clear. Make them easy to buy online, explain what they include and promote them in Business Profile posts and on your website through December.</p>")],
}
for p in PAGES:
    for h, b in MORE.get(p["slug"], []):
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

LAST = {
"gemini-4-hydrogen-small-business": ("Getting started this week", "<p>Pick one repetitive task that takes your team at least an hour a week, such as summarizing customer emails, preparing a weekly sales summary or drafting social posts from your service pages. Try it in the Gemini app or Gemini for business with Hydrogen, compare the result with how you do it now and note the time saved. Keep a short list of prompts that work, share them with staff, and set a simple rule that anything going to customers is checked by a person first. Small, repeatable wins add up faster than trying to automate everything at once.</p>"),
"search-console-platform-properties-social": ("Questions to ask your social media manager", "<ul><li>Have we added our Instagram, TikTok, X and YouTube accounts as platform properties?</li><li>Which posts get the most impressions from Google Search?</li><li>What search topics lead people to our posts?</li><li>Which of those topics don't have a page on our website yet?</li><li>Are our captions written so people can find them in Search?</li><li>Do we track changes with Search Console annotations?</li></ul><p>Answering these takes an hour and usually reveals one or two quick wins, such as a post topic that deserves a website page or captions that could be clearer.</p>"),
"google-maps-dining-trends-restaurants": ("Questions to ask your team", "<ul><li>Which three dishes do customers mention most in reviews?</li><li>Is our menu published as text on our website and Business Profile?</li><li>Do we have recent photos of our signature dishes on Maps?</li><li>Do we reply to reviews and thank people for mentioning specific dishes?</li><li>Are seasonal items listed while they're available and removed when they're not?</li><li>Do our hours, including late nights, match on every listing?</li></ul><p>Fixing even two or three of these makes it easier for diners, Google Maps and AI assistants to understand what your restaurant is known for, which is the real lesson behind Google's list.</p>"),
"google-when-to-buy-holiday-retailers": ("Questions retailers ask us", "<p>Retailers often ask whether to follow national timing if their customers are different. Use the guide as a starting point and let your own sales history decide. Another common question is whether to advertise during quiet weeks. Small, targeted promotions for categories that sell early, combined with clear holiday hours and stock information, often work better than broad discounts. Retailers also ask how to reach last-minute shoppers. Keep your Business Profile, product pages and pickup options current, because those shoppers search for what's available nearby today. Finally, after the season, compare your results with Google's guide and your plan, and note what to change next year while the details are fresh. A short written review, covering which categories sold when, which promotions worked and where stock ran out, becomes next year's starting plan.</p>"),
"google-wallet-gemini-subscriptions-local-business": ("Questions to ask about your memberships", "<ul><li>Is our business name on card statements easy to recognize?</li><li>Does our website clearly explain what each plan includes and costs?</li><li>Did we announce our last price change in advance, with reasons?</li><li>Do members get a regular summary of what they've used?</li><li>Can members pause or switch plans easily?</li><li>Do we ask happy members for reviews?</li></ul><p>If any answer is no, that's the first thing to fix before members review their subscriptions with AI. None of these changes require new technology: they're about clear communication, fair pricing and making value visible. Businesses that already do this well have little to worry about from AI-powered spending reviews, and may even benefit as competitors with unclear plans lose members. Start with the statement name and the membership page this week, then build monthly usage reminders into your routine over the next month.</p>"),
}
for p in PAGES:
    if p["slug"] in LAST:
        h, b = LAST[p["slug"]]
        p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": b})

if __name__ == "__main__":
    save_all(PAGES)
