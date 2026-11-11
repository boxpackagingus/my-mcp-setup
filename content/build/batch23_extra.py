"""Extra sections for batch 23 guides: a checklist, a worked example and how the task fits a local plan.
Examples are clearly framed as illustrations, not as real businesses; facts come from the same Google sources."""

PLAN_V = [
    ("<p>This task is one piece of a wider local plan. Google says local results are mainly based on relevance, distance and popularity, "
     "so the profile, your website and your reputation all have to agree. A practical order for most Orange County businesses is: get the "
     "Business Profile verified and accurate, make the name, address and phone identical everywhere, publish one clear page per service, "
     "then build a steady habit of genuine reviews and replies. Each step makes the next one work better, and the same signals help AI "
     "assistants such as ChatGPT, Gemini and Google's AI features describe your business correctly when someone in Anaheim asks for a recommendation.</p>"),
    ("<p>Treat this as part of a routine rather than a one-off fix. Local visibility in Anaheim and the rest of Orange County comes from many "
     "small, accurate signals adding up: a verified profile, consistent listings, useful service pages, real photos and a flow of honest "
     "reviews. Google is open that relevance, distance and popularity drive local results. You cannot change distance, but you can make sure "
     "Google and AI assistants understand exactly what you do and see evidence that customers value it. Put a monthly reminder in the calendar "
     "to check the profile, read new reviews and update anything that has changed.</p>"),
    ("<p>It helps to see where this sits in the bigger picture. Google ranks local results mainly on relevance, distance and popularity, and "
     "AI assistants lean on the same public information: your Business Profile, your website, other listings and what customers write. "
     "For a business in Anaheim or anywhere in Orange County, the most reliable plan is simple and repeated: keep every listing accurate, "
     "explain each service clearly on its own page, show real proof of your work and reply to customers. Small improvements here compound, "
     "and they are far harder for competitors to copy than an ad budget.</p>"),
]

HELP_V = [
    ("When to get help", "<p>Most of this can be done in-house with an hour or two and careful reading of Google's own help pages. It is worth bringing in help when the "
     "stakes are high or the problem keeps coming back: a profile that has been suspended more than once, many locations to manage, a site that "
     "keeps failing the same checks, or no time to keep up the routine. A good local SEO partner should explain what they will change and why, "
     "point to Google's guidelines rather than promise rankings, and leave you with access to every account. Chimera works this way with "
     "businesses across Anaheim and Orange County.</p>"),
    ("When to get help", "<p>You do not need an agency for every step here; Google documents most of it clearly. Consider outside help when the work is urgent "
     "and unfamiliar, when you manage several locations, or when the same issue returns after you fix it. Ask any provider to show you the "
     "specific guideline or documentation behind each recommendation, to keep you as the owner of your accounts and to report results in "
     "calls, bookings and leads rather than vanity numbers. That is how Chimera works with Orange County businesses from our base in Anaheim.</p>"),
    ("When to get help", "<p>Plenty of owners handle this themselves. Outside help pays off when time is short, when the business has many locations or when a "
     "problem is costing calls every day it stays unresolved. Be wary of anyone who promises guaranteed positions or asks for your verification "
     "codes or passwords; Google says nobody can pay for a better local ranking. Look for clear explanations, honest timelines and reporting tied "
     "to real enquiries. Chimera offers exactly that to businesses in Anaheim and across Orange County.</p>"),
]

WEEK = {
    "google-business-profile-suspended": ["Read the decision and policy link in the appeals tool.", "Fix the name, address or categories.", "Collect documents that match exactly.", "Submit one complete appeal."],
    "google-business-profile-verification": ["Search for and claim any existing profile.", "Correct name, address or service area and phone.", "Prepare what you will show on video.", "Start verification and do not edit while it runs."],
    "google-business-profile-categories": ["Note the categories nearby competitors use.", "Pick the most specific true primary category.", "Remove categories that do not fit.", "Add matching services and pages."],
    "google-business-profile-service-area": ["Decide: service-area or hybrid.", "Remove the address if customers do not visit.", "Replace any radius with cities or postal codes.", "Update the service area page on your site."],
    "google-business-profile-photos": ["Upload a logo and cover photo.", "Take exterior and interior photos in daylight.", "Add photos of recent work or products.", "Record one 30-second video."],
    "google-business-profile-posts": ["Write one update linking to a service page.", "Schedule an offer or event with dates.", "Set one repeating monthly post.", "Check older updates before they archive."],
    "google-business-profile-holiday-hours": ["List every holiday for the next 12 months.", "Set special hours for each change.", "Confirm unchanged holidays.", "Update other listings to match."],
    "how-to-remove-fake-google-reviews": ["List suspicious reviews and why.", "Report each with the right reason.", "Reply briefly to each one.", "Send review links to recent real customers."],
    "google-local-services-ads-vs-seo": ["Check whether your category is eligible.", "Work out what a customer is worth.", "Complete your Business Profile and service pages.", "Set up separate tracking for each source."],
    "core-web-vitals-for-local-businesses": ["Open the Core Web Vitals report in Search Console.", "Test your homepage on mobile.", "Compress the largest image.", "Remove one unused script."],
}


def sec(h, items=None, p=None):
    body = ""
    if p:
        body += f"<p>{p}</p>"
    if items:
        body += "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    return (h, body)


EXTRA = {
"google-business-profile-suspended": [
    sec("Appeal checklist", ["Business name matches signage and documents exactly.", "Address is one you operate from, or the profile is set as a service-area business.",
        "No virtual office or P.O. box.", "Categories describe services you really offer.", "No duplicate profiles for the same location.",
        "Evidence ready: registration, license, tax certificate or utility bill.", "Every document shows the same name and address as the profile.",
        "You are signed in to the Google Account that manages the profile."]),
],
"google-business-profile-verification": [
    sec("Verification checklist", ["Search for the business first and claim it if it already exists.", "Name matches your signage and paperwork.",
        "Address is real, or the profile is set up with a service area.", "The phone number reaches a person or a phone that receives texts.",
        "For video: signage, equipment, tools and proof of management ready to show.", "For postcard: no edits to name, address or category while waiting.",
        "The code stays private.", "Calendar reminder at 14 days if the postcard has not arrived."]),
    sec("An example", p="Imagine a new mobile auto detailer based in Anaheim with no storefront. When setting up the profile, the owner hides the home address, adds a service area for nearby cities and is offered video verification. The video shows the branded van, the detailing equipment, business paperwork and the street outside the base location, recorded in one continuous take. Because the details match what the owner can show, verification is straightforward. Had the owner listed the home address as a storefront, it would not have matched what Google's guidelines expect for a business that visits customers."),
],
"google-business-profile-categories": [
    sec("Category checklist", ["Primary category is the most specific one that is true.", "Additional categories cover real departments or services only.",
        "No category for every product.", "Separately owned businesses at your location have their own profiles.",
        "Services list and website pages match your categories.", "Category changes are made one at a time.", "Performance reports checked after each change."]),
    sec("An example", p="Imagine a family-run bakery in Orange that also sells coffee and runs cake decorating classes. Its main business is baking, so Bakery is the primary category. Coffee is a real part of what customers come for, so Coffee shop could be an additional category, and the classes are described as a service and on a page of the website rather than as another category. If an independently owned juice bar rents a counter inside the shop, it keeps its own profile with its own category. This mirrors Google's own grocery store and health club examples."),
    PLAN_V[0],
],
"google-business-profile-service-area": [
    sec("Service area checklist", ["Business type is set correctly: service-area or hybrid.", "Address removed if customers do not visit it.",
        "No more than 20 service areas.", "Areas are cities, postal codes or regions, not a radius.", "The whole area is within about 2 hours of driving.",
        "Every listed area is somewhere you genuinely work.", "Website service area page lists the same places.", "Real projects or reviews from those places are shown."]),
    sec("An example", p="Imagine a plumber who works from home in Anaheim and drives to customers. The profile hides the home address and lists cities the business genuinely covers, such as Anaheim, Fullerton, Orange, Placentia, Yorba Linda, Garden Grove and Santa Ana, rather than every city in the county. The website has one service area page naming those cities, with a few real jobs from each. If the plumber later rents a showroom where customers can visit during set hours with permanent signage, the profile can become a hybrid business showing that address alongside the service area."),
    PLAN_V[1],
],
"google-business-profile-photos": [
    sec("Photo checklist", ["Profile verified.", "Logo uploaded.", "Cover photo chosen.", "Exterior photo from the street.",
        "Interior or workspace photos.", "Team photos with permission.", "Photos of products, dishes or finished jobs.",
        "JPG or PNG, 10 KB to 5 MB, around 720 by 720 pixels.", "No heavy filters or misleading edits.", "A short video of 30 seconds or less."]),
    sec("A simple monthly photo routine", p="Set a recurring reminder to add a handful of new photos each month. Take them on a phone in good daylight: the storefront as customers approach it, the space on a typical day, the team at work and a few recent products or projects. Check each image is sharp and honest before uploading. Over a year, a routine like this builds a large, current gallery that reflects how the business really looks, which helps people arriving from Google Maps recognize you and reduces surprises when they visit."),
    sec("An example", p="Imagine a nail salon near the Anaheim Packing District. Its profile starts with only a logo. The owner adds an exterior shot showing the entrance and nearby parking, interior photos of the stations, photos of finished nail designs taken under natural light and a 20-second video walking through the salon. A month later, new photos of seasonal designs are added. Customers searching on Maps now see what the salon looks like and the style of work it does before they book."),
    PLAN_V[2],
],
"google-business-profile-posts": [
    sec("Post checklist", ["Choose the right type: update, offer or event.", "Offers have a title, dates and time.", "Events have start and end dates and times.",
        "A real photo or short video.", "A button linking to the matching page on your site.", "No unverified phone numbers in the description.",
        "Scheduled ahead where possible.", "Evergreen updates refreshed before 6 months."]),
    sec("A monthly post calendar", ["Week 1: an update about a service, linking to its page.", "Week 2: a recent project or product with a photo.",
        "Week 3: an offer with clear dates and terms, if you run one.", "Week 4: an event, a seasonal tip or an answer to a common question."],
        p="A simple rhythm keeps the profile current without much effort:"),
    sec("An example", p="Imagine an HVAC company in Fullerton heading into summer. In May it schedules an update about AC tune-ups linking to its tune-up page, an offer for a seasonal inspection with clear start and end dates, and an update with a photo of a recent installation. It sets a monthly repeating post reminding customers to change filters. Customers who find the company on Maps see current, relevant information, and each post leads to the right page on the website."),
    PLAN_V[0],
],
"google-business-profile-holiday-hours": [
    sec("Holiday hours checklist", ["Regular hours set and the profile is Open with main hours.", "Special hours added for each holiday that changes.",
        "Unchanged holidays confirmed.", "Closures of 7 days or more marked temporarily closed.", "More hours set for delivery, takeout or senior hours.",
        "Website, Apple Maps, Yelp and other listings updated to match.", "A post announcing holiday hours."]),
    sec("Holidays to plan for", p="Work through the calendar once a year and set special hours early. Common dates include New Year's Day, Memorial Day, Independence Day, Labor Day, Thanksgiving and the day after, Christmas Eve, Christmas Day and New Year's Eve. Add local factors too: in Anaheim, conventions and events can change when customers come, and some businesses extend hours rather than close. Setting all dates in one sitting means none are forgotten."),
    sec("An example", p="Imagine a restaurant near the Anaheim Convention Center. It closes on Thanksgiving Day, opens late on the Friday after, closes early on Christmas Eve and closes for a five-day refurbishment in January. Thanksgiving, the Friday and Christmas Eve are special hours. The five-day refurbishment also uses special hours, because it is under 7 days. If the refurbishment had run for two weeks, Google's guidance would point to marking the restaurant temporarily closed instead. The restaurant also posts an update with the holiday schedule."),
    PLAN_V[1],
],
"how-to-remove-fake-google-reviews": [
    sec("Fake review checklist", ["Check your records for the reviewer.", "Note what is false or off-topic.", "Report with the most accurate reason.",
        "Track the status in the Reviews Management Tool.", "Reply calmly and briefly in public.", "Appeal once if you disagree with the decision.",
        "Report extortion attempts and never pay.", "Keep asking real customers for reviews."]),
    sec("How to word a reply", p="Keep replies short and factual. For example: \"We can't find any record of a visit matching this description. We'd like to understand what happened, so please contact us directly.\" Do not accuse the reviewer, do not mention competitors and never share details about real customers. A measured reply reassures other readers, who often judge the business more by its response than by a single review."),
    sec("An example", p="Imagine a dental office in Garden Grove that receives three one-star reviews in a day from accounts with no visit history, all describing a procedure the office does not offer. The office reports each one as spam through the Reviews Management Tool, replies to each briefly saying it has no record of the patient, and notes the dates. If the reports are rejected, it files one appeal covering the reviews. Meanwhile, it continues asking every patient for a review, so genuine feedback keeps outweighing the fake ones."),
    PLAN_V[2],
],
"google-local-services-ads-vs-seo": [
    sec("Questions to decide between them", ["Is your category eligible in your area?", "Can you answer calls and messages quickly, every day?",
        "Do you have the licenses and reviews needed to pass screening?", "How quickly do you need new calls?",
        "What is your budget per lead, and what is a customer worth?", "Do you want visibility that continues without ongoing spend?"]),
    sec("Tracking both properly", p="Measure each source separately. Local Services Ads have their own lead reports. For organic, use Business Profile performance for calls and direction requests, Search Console for search impressions and clicks, and Google Analytics for website visits, including referrals from AI assistants. Record where each booked job came from. After a few months you will know the real cost per customer from ads and how much organic is contributing, which tells you where the next dollar should go."),
    sec("An example", p="Imagine a new electrician in Orange. With few reviews and no rankings yet, the owner signs up for Local Services Ads to get calls in the first months, while also completing the Business Profile, publishing a page for each service and asking every customer for a review. As reviews and pages build, organic calls grow. The owner then lowers the ad budget during busy seasons when organic leads are enough, and keeps the ads for slower months."),
    PLAN_V[0],
],
"core-web-vitals-for-local-businesses": [
    sec("Core Web Vitals checklist", ["Hero image resized and compressed.", "Main image not lazy-loaded.", "Width and height set on images and embeds.",
        "Unused plugins and tracking tags removed.", "Chat widgets and pop-ups delayed.", "Fonts limited to what you use.",
        "Caching enabled.", "Mobile results checked in Search Console after changes."]),
    sec("Questions to ask your web developer", ["Which pages fail Core Web Vitals in Search Console, and on which metric?",
        "What is the largest element on our key pages, and how big is it?", "Which third-party scripts load on every page, and are they all needed?",
        "Do our images have set dimensions?", "How will we confirm the fix worked?"], p="If someone else maintains your site, these questions keep the conversation specific:"),
    sec("Where to start on a small site", p="Begin with the pages that bring customers: the homepage, the main service pages and the contact page. Fix the largest images first, because they usually account for most of the loading time, then remove scripts no one uses. Re-test those pages, then move to the rest of the site. Search Console's report groups pages with similar problems, so one fix to a shared template often improves many pages at once."),
    sec("An example", p="Imagine a landscaping company in Irvine whose homepage hero is a large, uncompressed photo, with a chat widget and three old tracking tags loading on every page. Resizing and compressing the hero image speeds up the main content, removing the unused tags and delaying the chat widget makes buttons respond faster, and setting dimensions on the gallery images stops the page jumping. The company then checks Search Console over the following weeks to confirm the field data improves."),
    PLAN_V[1],
],
}


def add_extras(pages):
    for p in pages:
        extra = EXTRA.get(p["slug"], [])
        secs = p["sections"]
        last = secs.pop()  # keep "The short version" last
        for e in extra:
            if isinstance(e, str):
                secs.append({"heading": "How this fits your local plan", "body_html": e})
            else:
                secs.append({"heading": e[0], "body_html": e[1]})
        secs.append({"heading": "What to do this week", "body_html": "<ol>" + "".join(f"<li>{w}</li>" for w in WEEK[p["slug"]]) + "</ol>"})
        h, b = HELP_V[pages.index(p) % 3]
        secs.append({"heading": h, "body_html": b})
        secs.append(last)
