"""Blog posts for 2026-11-16 (5 posts). Every fact is checked at the linked source on 2026-11-16."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_15  # noqa: F401  (SRC entries)
import batch35  # noqa: F401  (Merchant Center SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SRC.update({
    "g_backbutton": {"title": "Google Search Central blog: Introducing a new spam policy for \"back button hijacking\" (Apr 13, 2026)",
                     "url": "https://developers.google.com/search/blog/2026/04/back-button-hijacking"},
    "g_maps_tips": {"title": "Google: 3 ways Google Maps can help you navigate your next culinary adventure (Oct 8, 2026)",
                    "url": "https://blog.google/products-and-platforms/products/maps/google-maps-restaurant-tips-tricks/"},
    "g_thrift": {"title": "Google: 5 ways Google Search can level up your thrift and vintage shopping (Jun 3, 2026)",
                 "url": "https://blog.google/products-and-platforms/products/search/thrifting-tips/"},
    "g_yt_assets": {"title": "Google Ads & Commerce blog: Turn your existing social assets into high-impact YouTube ads (Oct 1, 2026)",
                    "url": "https://blog.google/products/ads-commerce/creating-assets-youtube-ads/"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")
TECH = L("Search Console security issues", "google-search-console-security-issues")
ROBOTS = L("robots.txt for AI crawlers", "robots-txt-for-ai-crawlers")
SC = L("Search Console manual actions", "google-search-console-manual-actions")
REST = L("SEO for restaurants in Orange County", "seo-for-restaurants-orange-county")
ASKMAPS = L("Ask Maps food ordering", "ask-maps-food-ordering-restaurants")
DINING = L("Google Maps dining trends", "google-maps-dining-trends-restaurants")
GBP = L("Google Business Profile optimization", "google-business-profile-optimization-orange-county")
THRIFT = L("SEO for thrift stores", "seo-for-thrift-stores")
BOUT = L("SEO for clothing boutiques", "seo-for-clothing-boutiques")
FREE = L("Google free product listings", "google-free-product-listings")
LIA = L("local inventory ads and free local listings", "google-local-inventory-ads")
DG = L("Demand Gen data strength", "google-ads-data-strength-demand-gen")
YTAI = L("YouTube for AI search", "youtube-for-ai-search")
START = L("how to set up Google Merchant Center", "how-to-set-up-google-merchant-center")
SPEC = L("Merchant Center product data", "merchant-center-product-data")
ISSUES = L("Merchant Center product disapprovals", "merchant-center-disapprovals")
RETURNS = L("Merchant Center return policies", "merchant-center-return-policies")
PROMO = L("Merchant Center promotions", "google-merchant-center-promotions")
FEED = L("local inventory feed", "local-inventory-feed")
MCAI = L("Merchant Center AI performance insights", "merchant-center-ai-performance-insights")


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


PAGES = [
# 1 ------------------------------------------------------------------
blog(1, "Google news",
     slug="back-button-hijacking-spam-policy", query="back button hijacking", kw="back button hijacking",
     eyebrow="Google Search", short_title="Google's back button hijacking spam policy",
     title="Back Button Hijacking: Google's Spam Policy",
     meta="Back button hijacking is now an explicit Google spam violation, enforced since June 15, 2026. How Orange County businesses can check their sites and ad scripts.",
     h1="Back Button Hijacking: Check Your Website Before Google Does",
     answer="Back button hijacking is when a website stops visitors from using the browser's back button to return to the page they came from, for example by sending them to pages they never visited or to ads. Google made it an explicit violation of its malicious practices spam policy, with enforcement from June 15, 2026. Anaheim and Orange County businesses should check their site's scripts, plugins and ad code.",
     takeaways=["Announced April 13, 2026.", "Enforcement began June 15, 2026.", "It's part of the malicious practices policy.",
                "Ad platforms and libraries can cause it.", "Fixed sites can request reconsideration."],
     sections=[
      ("What Google announced", "<p>On April 13, 2026, Google's Search Quality team announced that back button hijacking would become an explicit violation of the malicious practices section of its spam policies, which can lead to spam actions. Google published the policy two months ahead of enforcement, which began on June 15, 2026.</p>"),
      ("What back button hijacking is", "<p>Google explains that when people click the back button, they expect to return to the previous page. Back button hijacking happens when a site interferes with browser navigation and stops them from going straight back. Instead, they may land on pages they never visited, see unsolicited recommendations or ads, or simply be unable to browse normally.</p>"),
      ("Why Google is acting", "<p>Google says the practice breaks the expected user journey, frustrates people and makes them feel manipulated and less willing to visit unfamiliar sites. It notes that inserting deceptive or manipulative pages into browser history has always been against Google Search Essentials, but that it has seen a rise in this behavior.</p>"),
      ("The possible consequences", "<p>Google says pages engaging in back button hijacking may be subject to manual spam actions or automated demotions, which can affect a site's performance in Google Search.</p>"),
      ("It may not be your own code", "<p>Google specifically notes that some back button hijacking may come from a site's included libraries or advertising platform. A small business might never have added such code deliberately but could still be running it through a plugin, theme, pop-up tool or ad network.</p>"),
      ("How to check your site", ol(["Open your site on a phone from a Google search result.", "Visit two or three pages, then press back repeatedly.",
                                     "Check that each press returns to the page you came from, ending at Google.", "Repeat on pages with ads, pop-ups or chat widgets.",
                                     "Ask your developer to review scripts that change browser history."])),
      ("Common sources on small business sites", ul(["Aggressive pop-up or exit-intent plugins.", "Ad networks with recommendation widgets.", "Old landing page tools.",
                                                     "Third-party chat or booking scripts.", "Plugins from unknown developers."])),
      ("What to do if you find it", "<p>Google expects site owners to remove or disable any code, imports or configurations responsible for back button hijacking. Contact the plugin or ad provider, switch off the feature, or replace the tool. Test again afterwards on desktop and mobile browsers.</p>"),
      ("If you received a manual action", "<p>Google says that if your site has had a manual action and you've fixed the issue, you can submit a reconsideration request in Search Console. Explain what you found, what you removed and how you tested it.</p>"),
      ("Why this matters beyond Google", "<p>Even without a penalty, trapping visitors damages trust. A customer in Anaheim who can't get back to search results after visiting your site is unlikely to call you. A clean, predictable experience supports both rankings and conversions.</p>"),
      ("A worked example", "<p>Imagine a dental office in Irvine using a free pop-up plugin to promote a new-patient offer. When the office manager tests the site from Google, pressing back opens the offer page again instead of returning to search results. The developer removes the plugin's exit-intent feature, tests on several phones and adds a monthly check to the maintenance list.</p>"),
      ("Questions owners ask us", "<p>Owners often ask whether exit pop-ups are banned. Google's policy is about interfering with the back button and inserting deceptive pages into browser history, not about showing a polite pop-up. Another common question is whether a small site will really be noticed. Google says affected pages may face manual actions or automated demotions, so it isn't worth the risk. Owners also ask how often to check. After any new plugin, theme or ad setup, and as part of a regular technical review.</p>"),
      ("The short version", "<p>Back button hijacking is an explicit Google spam violation, enforced since June 15, 2026. Test your site's back button, review plugins and ad code, remove anything that traps visitors, and request reconsideration if you received a manual action. Anaheim and Orange County businesses keep both rankings and trust this way.</p>")],
     faqs=[("What is back button hijacking?", "When a site stops visitors from using the back button to return to the page they came from."),
           ("When did Google start enforcing the policy?", "June 15, 2026."),
           ("Which Google policy covers it?", "The malicious practices section of Google's spam policies."),
           ("Can ad code cause back button hijacking?", "Yes. Google says it may come from included libraries or advertising platforms."),
           ("What happens to sites that do it?", "Manual spam actions or automated demotions are possible."),
           ("How do I recover from a manual action?", "Fix the issue, then submit a reconsideration request in Search Console."),
           LOCAL_FAQ],
     links=[TECH, SC, ROBOTS, LOCAL, AUD],
     sources=["g_backbutton"],
     visuals=[V.flow(5, "Checking your back button", "Based on Google's April 13, 2026 post.",
               [("Search", "Open your site from Google."), ("Browse", "Visit a few pages."),
                ("Back", "Press back to Google."), ("Fix", "Remove scripts that interfere.")])],
     secondary=["Google spam policy back button", "malicious practices policy", "back button redirect SEO", "Google manual action back button"],
     hero_query="Will Google penalize my site for back button redirects?"),

# 2 ------------------------------------------------------------------
blog(2, "Playbooks",
     slug="google-maps-know-before-you-go-restaurants", query="google maps know before you go", kw="Google Maps know before you go tips",
     eyebrow="Google Maps", short_title="Google Maps know before you go tips for restaurants",
     title="Google Maps Know Before You Go Tips: Guide",
     meta="Google Maps know before you go tips, trending dining lists and Ask Maps help diners pick restaurants. What Anaheim and Orange County restaurants should do.",
     h1="Google Maps Know Before You Go Tips: What Restaurants Should Know",
     answer="Google Maps know before you go tips are insider notes from the Maps community, shown when people search for restaurants, cafes and diners, covering things like how to get a reservation, where to park and what to order. Google highlighted them in October 2026 with Ask Maps and weekly dining lists. Anaheim and Orange County restaurants can shape these tips through clear information and good guest experiences.",
     takeaways=["Tips come from the Maps community.", "They cover reservations, parking and dishes.", "Explore tab lists update weekly.",
                "Ask Maps analyzes photos, reviews and menus.", "Clear information helps guests leave useful tips."],
     sections=[
      ("What Google highlighted", "<p>On October 8, 2026, Google shared three Google Maps features for finding a meal: Ask Maps for finding and ordering what people crave, trending dining lists in the Explore tab and know before you go tips from the Maps community.</p>"),
      ("Know before you go tips", "<p>Google says that when people search for restaurants, cafes and diners, they can scroll down to find insider tips from the Maps community, including how to get a hard-to-get reservation, where to park and which dishes to order.</p>"),
      ("Ask Maps", "<p>Google says people can say or type what they want, such as fall dessert spots with outdoor seating, and Ask Maps analyzes billions of photos, reviews and menus to find a match. It can also let people order delivery through partners like Uber Eats, Toast and Square.</p>"),
      ("Trending dining lists", "<p>The Explore tab shows dining lists updated weekly, according to Google: Trending for places that recently spiked in popularity, Gems for new neighborhood favorites and Top for tried-and-true classics. People can save them with a tap.</p>"),
      ("Why these features matter", "<p>Each feature draws on information about your restaurant that comes from guests and from you: photos, reviews, menus and community tips. Restaurants that make the basics easy to understand, from parking to signature dishes, give diners and Maps more useful details to share.</p>"),
      ("Make parking and arrival easy", "<p>Parking is one of the tip topics Google mentions. Put clear parking and arrival details on your website and Business Profile, such as validated parking, the nearest lot or the best entrance. Near the Anaheim Resort and busy Orange County centers, this makes a real difference.</p>"),
      ("Be clear about reservations", "<p>If you take reservations, explain how far ahead they open, whether you hold tables for walk-ins and how to join a waitlist. Clear rules mean guests share accurate tips rather than guesses.</p>"),
      ("Make your signature dishes obvious", "<p>Diners often tell others what to order. Name your signature dishes on the menu, in photos and on your website, and keep your menu as text, so the dishes guests mention match what Maps can find.</p>"),
      ("What restaurants can do this week", ol(["Check your Business Profile menu, hours and photos.", "Add parking and arrival details.", "Explain reservations and waitlists.",
                                                "Upload photos of signature dishes.", "Reply to recent reviews.", "Check ordering links work."])),
      ("Don't try to game tips", "<p>Tips and reviews should come from real guests. Asking staff or friends to post fake tips or reviews breaks Google's policies and erodes trust. Focus on giving real guests a great experience and clear information.</p>"),
      ("A worked example", "<p>Imagine a ramen shop in Tustin where guests often struggle to find parking. The owner adds clear parking directions to the website and Business Profile, posts photos of the three most popular bowls and explains the walk-in waitlist. Over the following weeks, guest tips mention the parking lot behind the building and the spicy miso ramen.</p>"),
      ("Questions owners ask us", "<p>Owners often ask whether they can edit know before you go tips. They come from the Maps community, so the best influence is clear information and good experiences. Another common question is how to get into trending lists. Google describes them as based on popularity and favorites, so there's no shortcut; steady visits, reviews and photos help. Owners also ask whether Ask Maps ordering needs a specific partner. Google names partners like Uber Eats, Toast and Square for delivery orders.</p>"),
      ("The short version", "<p>Google Maps know before you go tips, trending lists and Ask Maps all draw on real information about your restaurant. Anaheim and Orange County restaurants that make parking, reservations and signature dishes clear, and keep menus and photos current, give diners and Maps better material to recommend them.</p>")],
     faqs=[("What are Google Maps know before you go tips?", "Insider tips from the Maps community shown when people search for restaurants."),
           ("What do the tips cover?", "Google mentions reservations, parking and what to order."),
           ("How often do Explore dining lists update?", "Google says weekly."),
           ("What lists are in the Explore tab?", "Trending, Gems and Top."),
           ("Can Ask Maps order food?", "Google says it can order delivery through partners like Uber Eats, Toast and Square."),
           ("Can restaurants write their own tips?", "Tips come from the Maps community; restaurants should provide clear information instead."),
           LOCAL_FAQ],
     links=[ASKMAPS, DINING, REST, GBP, LOCAL],
     sources=["g_maps_tips"],
     visuals=[V.flow(4, "Getting ready for Maps tips", "Based on Google's October 8, 2026 post.",
               [("Parking", "Clear arrival details."), ("Reservations", "Explain how they work."),
                ("Dishes", "Name and photograph them."), ("Menus", "Current and as text.")])],
     secondary=["Google Maps restaurant tips", "Google Maps Explore dining lists", "Ask Maps restaurants", "Google Maps trending restaurants"],
     hero_query="How do diners find restaurant tips on Google Maps?"),

# 3 ------------------------------------------------------------------
blog(3, "AI Shopping",
     slug="thrift-shopping-google-lens-ai-mode", query="thrift shopping google lens", kw="thrift shopping with Google Lens",
     eyebrow="Google Search", short_title="Thrift shopping with Google Lens and AI Mode",
     title="Thrift Shopping With Google Lens and AI Mode",
     meta="Thrift shopping with Google Lens, AI Mode and Circle to Search is changing how vintage shoppers find stores. What Orange County resale shops should do now.",
     h1="Thrift Shopping With Google Lens and AI Mode: What Resale Shops Should Know",
     answer="Thrift shopping with Google Lens lets shoppers snap a photo of an item to find visual matches, its designer or era, and what similar pieces sell for. Google says search interest in vintage and how to thrift reached all-time highs in 2026, and AI Mode helps people plan thrift trips. Anaheim and Orange County thrift, vintage and consignment shops should make their stores easy to find and understand.",
     takeaways=["Google says vintage search interest hit all-time highs.", "AI Mode helps plan thrift trips.", "Lens identifies items and shows resale prices.",
                "Circle to Search finds similar items.", "Lens also helps people decide what to sell."],
     sections=[
      ("What Google shared", "<p>In June 2026, Google published five ways its tools can help with thrift and vintage shopping. It said search interest in vintage and how to thrift hit all-time highs this year.</p>"),
      ("Planning trips with AI Mode", "<p>Google says people can ask AI Mode detailed questions to plan a thrifting outing, such as where to find vintage jerseys in a city with a gluten-free brunch spot nearby. AI Mode highlights a few options with key details and links.</p>"),
      ("Google Lens in the store", "<p>Google describes Lens as a way to learn about an item while shopping at a thrift store or vintage market. Shoppers can snap a photo to see visual matches and ask about its designer or era, and check what similar items sell for online and how many offers exist.</p>"),
      ("Circle to Search and Virtual Try-On", "<p>Google says Circle to Search on Android can find similar items, prices and places to buy them. It also mentions Virtual Try-On, where people find a similar item with Lens, tap try it on and upload a full-body photo to see the style on themselves.</p>"),
      ("Selling with Lens", "<p>Google also suggests using Lens to see what items from your own closet might be worth and asking questions like what kind of stores buy items like this. That's a direct opportunity for consignment and resale shops.</p>"),
      ("What this means for resale shops", "<p>Shoppers who check items with Lens in your store are better informed about prices, so fair, consistent pricing matters. People planning trips with AI Mode need clear information about what you sell, your hours and your neighborhood. People looking to sell need to know what you buy.</p>"),
      ("Describe what you carry", "<p>Say plainly what kinds of items you specialize in, such as vintage denim, band T-shirts, mid-century furniture or designer bags. AI Mode answers specific questions, so specific descriptions on your website and Business Profile help it match your store.</p>"),
      ("Explain buying and consignment", "<p>If you buy or consign items, publish what you accept, when to bring items and how offers or splits work. Sellers who've just checked an item with Lens are ready to act.</p>"),
      ("Steps for Orange County resale shops", ol(["List your specialties on your website and Business Profile.", "Post photos of new arrivals regularly.",
                                                    "Publish buying or consignment terms.", "Keep hours and location accurate.", "Mention nearby spots for a day out."])),
      ("Price with confidence", "<p>Because shoppers can compare prices on the spot, explain what makes your pricing fair: condition checks, authenticity checks or curation. Staff who can talk about an item's era or maker add value a search can't.</p>"),
      ("A worked example", "<p>Imagine a vintage shop in Fullerton's downtown. The owner updates the Business Profile description to mention 70s and 80s denim, band shirts and vintage sportswear, posts weekly new-arrival photos and adds a page explaining how the shop buys clothing. Shoppers planning a day in Fullerton with AI Mode find a clear match, and sellers who checked items with Lens know where to bring them.</p>"),
      ("Questions owners ask us", "<p>Owners often ask whether Lens hurts resale shops by revealing online prices. It makes shoppers better informed, which rewards fair pricing and good curation. Another common question is whether small shops need a website. A simple site with specialties, hours, photos and buying terms helps AI Mode and shoppers understand your store. Owners also ask about listing items online. Selling online isn't required, but regular photos of new arrivals give people a reason to visit.</p>"),
      ("The short version", "<p>Thrift shopping with Google Lens, AI Mode and Circle to Search makes vintage shoppers better informed. Anaheim and Orange County resale shops win by describing their specialties clearly, posting new arrivals, explaining buying terms and pricing fairly.</p>")],
     faqs=[("How does Google Lens help thrift shoppers?", "It identifies items, shows visual matches and what similar pieces sell for."),
           ("Is vintage search interest growing?", "Google says searches for vintage and how to thrift hit all-time highs in 2026."),
           ("Can AI Mode help plan thrift trips?", "Yes. Google gives examples of detailed trip-planning questions."),
           ("What is Circle to Search?", "An Android feature for finding similar items, prices and where to buy."),
           ("Can Lens help people sell items?", "Google suggests using it to see what items are worth and which stores buy them."),
           ("What should resale shops do?", "Describe specialties, post new arrivals, explain buying terms and price fairly."),
           LOCAL_FAQ],
     links=[THRIFT, BOUT, FREE, GBP, LOCAL],
     sources=["g_thrift"],
     visuals=[V.flow(3, "How thrift shoppers use Google", "From Google's June 3, 2026 post.",
               [("Plan", "AI Mode."), ("Identify", "Google Lens."),
                ("Compare", "Circle to Search."), ("Sell", "Lens for value.")])],
     secondary=["Google Lens thrift", "vintage shopping AI Mode", "Circle to Search shopping", "resale shop marketing"],
     hero_query="How do thrift shoppers use Google Lens to find vintage stores?"),

# 4 ------------------------------------------------------------------
blog(4, "Google news",
     slug="youtube-ads-from-social-assets", query="youtube ads from social assets", kw="YouTube ads from social assets",
     eyebrow="Google Ads", short_title="Turning social assets into YouTube ads",
     title="YouTube Ads From Social Assets: Google's Tips",
     meta="YouTube ads from social assets: Google says existing creative is a solid base, with Asset Studio video creation. What Orange County businesses should know.",
     h1="YouTube Ads From Social Assets: Start With What You Already Have",
     answer="YouTube ads from social assets are a practical starting point, according to Google: existing creative such as social posts is probably a solid base for Demand Gen campaigns, as long as it follows Google's asset specs. Google also points to Asset Studio's multimodal video creation, powered by Gemini Omni, which turns website URLs and photos into videos. Anaheim and Orange County businesses can test YouTube without new shoots.",
     takeaways=["Published October 1, 2026.", "Existing social creative is a solid base.", "Assets must follow Google's specs.",
                "Asset Studio turns URLs and photos into videos.", "Test gradually and focus on quality."],
     sections=[
      ("What Google shared", "<p>On October 1, 2026, Google's Ads Decoded podcast covered Demand Gen campaigns and the role of creative, with Ads Product Liaison Ginny Marvin and a Demand Gen and YouTube performance ads product manager. Google summarized three takeaways.</p>"),
      ("Start with what you have", "<p>Google says your existing creative, such as social assets, is probably a solid base, as long as it follows Google's asset specs and guidelines. Small businesses with Reels, TikToks or short clips already have material to test.</p>"),
      ("Asset Studio video creation", "<p>Google suggests trying Asset Studio's multimodal video creation. It says the tool is powered by Gemini Omni and turns website URLs and photos into high-quality videos that stakeholders can preview before publishing.</p>"),
      ("Let data drive testing", "<p>Google advises making changes gradually and focusing on the quality of new assets rather than quantity, which gives the system enough time for measurement.</p>"),
      ("What this means for local businesses", "<p>Many small businesses avoid YouTube because they think they need professional video. Google's advice is that existing social clips can be a starting point. A restaurant's dish videos, a contractor's before-and-after clips or a salon's transformation reels may already work.</p>"),
      ("Check specs before uploading", "<p>Social videos are often vertical and short. Before using them, check Google's current asset specs for Demand Gen and YouTube, and prepare the formats required. Make sure text isn't cut off and the first seconds show your business clearly.</p>"),
      ("What makes a good local video ad", ul(["Shows the product, service or result quickly.", "Mentions the area you serve.", "Has a clear next step, such as call or book.",
                                                "Uses real footage of your business.", "Works without sound, with captions."])),
      ("Testing without wasting budget", ol(["Pick two or three of your best social clips.", "Check they meet Google's asset specs.", "Run a small Demand Gen test.",
                                             "Change one thing at a time.", "Compare leads, not just views."])),
      ("Connect measurement first", "<p>Before testing, make sure conversions such as calls, bookings and form submissions are tracked, so you can judge YouTube on real results. Without measurement, a cheap view tells you very little.</p>"),
      ("A worked example", "<p>Imagine a landscaping company in Yorba Linda with dozens of before-and-after Instagram reels. The owner picks three of the best, checks them against Google's specs, adds captions and runs a small Demand Gen test aimed at nearby homeowners. After a month, the company compares quote requests from the test with other channels.</p>"),
      ("Questions owners ask us", "<p>Owners often ask whether AI-made videos look fake. Google says Asset Studio lets people preview videos before publishing, so review each one and only use what represents your business honestly. Another common question is how many assets to test. Google advises focusing on quality over quantity and making changes gradually. Owners also ask whether YouTube works for local businesses. It can, when targeting and measurement are set up properly and the creative clearly shows what you do.</p>"),
      ("Keep your brand honest", "<p>Whatever tool creates the video, make sure it shows your real business, real work and accurate offers. Customers in Orange County who see one thing in an ad and another in person won't come back.</p>"),
      ("The short version", "<p>Google says existing social assets are a solid base for YouTube ads, Asset Studio can create videos from URLs and photos, and testing should be gradual and quality-focused. Anaheim and Orange County businesses can try YouTube without a big production budget.</p>")],
     faqs=[("Can I use social media videos as YouTube ads?", "Google says existing social assets are probably a solid base if they follow its asset specs."),
           ("What is Asset Studio's video creation?", "A tool Google says turns website URLs and photos into videos, powered by Gemini Omni."),
           ("Can I preview AI-created videos?", "Yes. Google says stakeholders can preview them before publishing."),
           ("How should I test creative?", "Google advises gradual changes and quality over quantity."),
           ("Which campaign type was discussed?", "Demand Gen campaigns."),
           ("Do I need professional video?", "Not to start; existing clips may work if they meet the specs."),
           LOCAL_FAQ],
     links=[DG, YTAI, LOCAL, AUD],
     sources=["g_yt_assets"],
     visuals=[V.flow(3, "Google's three takeaways", "From Google's October 1, 2026 post.",
               [("Reuse", "Start with social assets."), ("Create", "Asset Studio video."),
                ("Test", "Gradual, quality-first."), ("Measure", "Leads, not views.")])],
     secondary=["Demand Gen creative", "Asset Studio video", "YouTube ads small business", "reuse social videos for ads"],
     hero_query="Can I use my Instagram videos as YouTube ads?"),

# 5 ------------------------------------------------------------------
blog(5, "Playbooks",
     slug="holiday-merchant-center-checklist", query="holiday merchant center checklist", kw="holiday Merchant Center checklist",
     eyebrow="Google Shopping", short_title="A holiday Merchant Center checklist for retailers",
     title="Holiday Merchant Center Checklist for Retailers",
     meta="A holiday Merchant Center checklist for Orange County retailers: product data, shipping, returns, promotions, local inventory and issues, from Google's help.",
     h1="A Holiday Merchant Center Checklist for Orange County Retailers",
     answer="A holiday Merchant Center checklist covers the steps that keep products showing on Google during the busiest season: fix issues, keep prices and availability matching your site, add shipping and return policies, submit promotions early enough for Google's review and keep local inventory current. Anaheim and Orange County retailers who work through it before December avoid disapprovals when shoppers are searching most.",
     takeaways=["Fix issues before traffic peaks.", "Prices and availability must match your site.", "Shipping is required in the U.S.",
                "Google reviews every promotion.", "Local inventory must stay current."],
     sections=[
      ("Why a checklist now", "<p>Shoppers search for gifts across Google in November and December. Merchant Center decides whether your products can appear in free listings, Shopping ads and local listings, so problems found in mid-December cost sales. A checklist done now prevents that.</p>"),
      ("1. Clear your issues", "<p>Open Merchant Center's issues view. Google says disapproved products stop showing, while products with warnings may perform worse and can become disapproved. Fix account-level issues first, then the product issues affecting the most products.</p>"),
      ("2. Match prices and availability", "<p>Google says that when price or availability don't match between your product data and product pages, products can be pre-emptively disapproved and need a review. Holiday sales change prices often, so update product data automatically and frequently.</p>"),
      ("3. Check the required product data", "<p>Google's product data specification requires a title, description, image link, price and availability, with brand, GTIN and condition where they apply. Titles can be up to 150 characters. Rewrite titles for your best sellers so they say what the product is, with brand, size or color.</p>"),
      ("4. Shipping and returns", "<p>Google says shipping settings or costs are required in countries including the United States for free listings. It also recommends adding return policies, which can show next to products on ads, listings and Gmail. Set holiday return windows in Merchant Center as well as on your site.</p>"),
      ("5. Submit promotions early", "<p>Google reviews every promotion before it shows. Submit holiday promotions with a clean promotion ID, up to 50 characters with no spaces or symbols, and map them to the right products well before the sale starts.</p>"),
      ("6. Keep local inventory current", "<p>If you use free local listings or local inventory ads, Google says store codes must match your Business Profile, and syncing locations can take up to 24 hours. Update stock at least daily during the holidays.</p>"),
      ("7. Plan for image requirements", "<p>Google has announced that product images must be at least 500 x 500 pixels, enforced from January 31, 2027. Replace small images now, while you're already reviewing products.</p>"),
      ("The checklist", ol(["Clear account and product issues.", "Automate price and availability updates.", "Rewrite titles for top sellers.", "Confirm shipping settings.",
                            "Upload return policies, including holiday terms.", "Submit promotions a week ahead.", "Update local inventory daily.", "Replace images under 500 x 500."])),
      ("After the holidays", "<p>Returns and new stock change what's accurate in January. Switch return policies back to normal terms, remove ended promotions and check issues again after the rush.</p>"),
      ("A worked example", "<p>Imagine a gift shop in Orange with 300 products. In mid-November the owner clears 40 disapprovals caused by out-of-date prices, sets the product feed to update several times a day, adds a holiday return window, submits a December promotion a week early and updates the in-store inventory feed daily. Products keep showing through the busiest weeks.</p>"),
      ("Questions retailers ask us", "<p>Retailers often ask what to do first if time is short. Clear issues on your best-selling products, then make sure prices and availability match your site. Another common question is whether promotions are worth the effort for small stores. For strong offers like holiday discounts or free shipping, yes, as long as they're submitted early enough for review. Retailers also ask about local inventory. If you have a store, showing in-stock items nearby can win last-minute shoppers who want a gift today.</p>"),
      ("The short version", "<p>Work through a holiday Merchant Center checklist before December: issues, prices, product data, shipping, returns, promotions, local inventory and images. Anaheim and Orange County retailers who do keep their products in front of holiday shoppers when it matters most.</p>")],
     faqs=[("What should a holiday Merchant Center checklist include?", "Issues, prices and availability, product data, shipping, returns, promotions, local inventory and images."),
           ("Why do products get disapproved during sales?", "Often because prices or availability don't match the product page."),
           ("Is shipping information required?", "Google says yes, in countries including the United States, for free listings."),
           ("When should I submit holiday promotions?", "Early enough for Google's review; we suggest a week ahead."),
           ("How long do store locations take to sync?", "Google says up to 24 hours."),
           ("What image size will Google require?", "At least 500 x 500 pixels, enforced from January 31, 2027."),
           LOCAL_FAQ],
     links=[START, SPEC, ISSUES, RETURNS, PROMO, FEED, LIA, MCAI],
     sources=["mc_issues", "mc_spec", "mc_free", "mc_returns", "mc_promo", "mc_localspec"],
     visuals=[V.flow(2, "Holiday Merchant Center checklist", "From Google's Merchant Center help pages.",
               [("Issues", "Clear them first."), ("Data", "Prices, stock, titles."),
                ("Policies", "Shipping and returns."), ("Extras", "Promotions and local stock.")])],
     secondary=["Merchant Center holiday", "Google Shopping holiday checklist", "holiday product feed", "Merchant Center Black Friday"],
     hero_query="How do I get my products ready for Google Shopping before the holidays?"),
]

if __name__ == "__main__":
    from blog_2026_11_16_extra import add_x
    add_x(PAGES)
    save_all(PAGES)
