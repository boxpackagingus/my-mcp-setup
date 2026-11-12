"""Extra sections for batch 26 guides: common mistakes and practical advice. General advice only; Google facts stay on the main pages."""


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


EXTRA = {
"how-to-create-google-business-profile": [
 ("Common mistakes when creating a profile", ul([
  "Creating a new profile when one already exists, which splits reviews and confuses customers.",
  "Adding city names or service keywords to the business name to try to rank higher.",
  "Listing a home address that customers never visit instead of setting a service area.",
  "Using a personal Gmail tied to one employee, so the business loses access when they leave.",
  "Choosing a broad primary category such as Contractor when a specific one such as Roofing contractor fits.",
  "Leaving the profile half-finished after verification, with no hours, services or photos."])),
 ("What to prepare before you start", "<p>Gather everything in one place before you sign in: the exact business name from your signage or paperwork, "
  "the address or the list of cities you serve, a phone number answered during business hours, your website address, opening hours, "
  "a short description of what you do, and a handful of real photos of your premises, team or work. Decide who will own the profile "
  "and who will help manage it. Having this ready turns a frustrating afternoon into a fifteen-minute task, and it means the details "
  "Google shows from day one are complete and consistent with your website. For a new business in Anaheim, Fullerton, Irvine or anywhere "
  "else in Orange County, that first impression on Maps often decides whether a nearby customer calls you or the business next to you.</p>")],
"how-to-claim-google-business-profile": [
 ("Common problems when claiming", ul([
  "The claim button is missing because the profile is already verified by someone else; request ownership instead.",
  "A former agency or employee owns the profile and has stopped responding; keep records and use Google's ownership request route.",
  "There are two listings for the same business; claim the right one and deal with the duplicate rather than adding another.",
  "The address on the listing is an old location; correct it after claiming, before you start verification if possible.",
  "Someone calls offering to claim or verify the listing for a fee; claiming is free, so decline."])),
 ("Questions to answer before you claim", "<p>Before you start, confirm three things. First, that the listing really is your business and not a "
  "similarly named one in another Orange County city. Second, which Google Account should own it: ideally one the business controls, "
  "not a personal account belonging to one person. Third, whether customers visit you or you visit them, because that decides whether "
  "the profile shows an address or a service area. Answering these up front avoids the most common clean-up jobs later. Once the profile "
  "is yours, keep a short note of who owns it, who manages it and when access was last reviewed, so the business never has to recover "
  "its own listing again.</p>")],
"how-to-edit-google-business-profile": [
 ("Common editing mistakes", ul([
  "Editing from the wrong Google Account and wondering why the options are missing.",
  "Changing the same detail several times in a row while an earlier edit is still being reviewed.",
  "Adding keywords or a location to the business name, which can trigger re-verification or a policy problem.",
  "Updating the profile but forgetting the website, other directories and printed materials.",
  "Ignoring information collected from customers or automated calls that has changed the profile."])),
 ("A monthly profile check", "<p>Most profiles drift out of date slowly rather than all at once. A ten-minute check once a month keeps "
  "yours accurate: confirm the hours, including any upcoming holidays; call the listed phone number to make sure it rings through; open "
  "the website link on a phone; scan the services and attributes for anything that has changed; and read recent reviews and questions. "
  "Note anything you change and the date, so you can tell later whether a change in calls or direction requests lined up with an edit. "
  "For businesses in Anaheim and across Orange County with seasonal patterns, such as pool services in summer or HVAC in heat waves, "
  "this routine catches the changes that matter most before customers notice them.</p>")],
"google-business-profile-owners-and-managers": [
 ("Common access mistakes", ul([
  "Sharing one login between several staff members instead of giving each person their own access.",
  "Letting an agency or web designer hold primary ownership of the business's own profile.",
  "Forgetting to remove access when an employee or contractor leaves.",
  "Making everyone an owner when manager access would do the job.",
  "Using a personal email for the primary owner, so ownership is tied to one individual."])),
 ("A simple access policy", "<p>Write down a short access policy and keep it with your other business records. It only needs a few lines: "
  "the business account that holds primary ownership, the people who are owners and why, the people and agencies who are managers, and "
  "a date to review the list, such as every quarter. Add a line to your staff leaving checklist to remove profile access on their last "
  "day. When you hire an agency, put in writing that they will be managers and that the business keeps ownership. These small habits "
  "prevent the most painful situation we see with Orange County businesses: a profile that nobody at the business can control because "
  "the only owner has moved on.</p>")],
"google-business-profile-attributes": [
 ("Common attribute mistakes", ul([
  "Leaving most attributes blank, so the profile says nothing about payments, accessibility or amenities.",
  "Selecting attributes that are only partly true, such as accessible parking that is often unavailable.",
  "Forgetting to update attributes after a renovation, a new payment system or the end of patio season.",
  "Not checking details that customers have contributed to the profile.",
  "Describing amenities on the profile that the website contradicts."])),
 ("Attributes customers in Orange County ask about", "<p>The attributes that matter depend on who your customers are. Families visiting "
  "Anaheim often look for accessible entrances, restrooms and seating; diners compare outdoor seating, reservations and dietary options; "
  "shoppers want to know which payment methods are accepted; and people booking services want to know whether appointments are needed. "
  "Think about the questions your staff answer on the phone every week, then check that each answer is reflected in your attributes "
  "where Google offers one. Every question answered on the profile is one less reason for a customer to choose a competitor whose "
  "profile answers it first.</p>")],
"google-business-profile-services": [
 ("Common services mistakes", ul([
  "Relying only on the primary category and leaving the services list empty.",
  "Putting prices, phone numbers or city names into custom service names.",
  "Listing services the business no longer offers, which leads to wasted calls.",
  "Using different names for the same service on the profile and the website.",
  "Writing no descriptions, so customers cannot tell what each service includes."])),
 ("How to decide what to list", "<p>Start from what customers actually ask for, not from internal job codes. Look at the last few months "
  "of calls, emails and invoices and note the words customers use: they may say water heater replacement where your team says tank "
  "install. Use the customer's words for service names and descriptions. Then rank services by how much they matter to the business and "
  "make sure the most valuable ones have clear descriptions and, where it helps, a price or price range. Review the list whenever you "
  "add or drop a service. For trades and service businesses across Anaheim and Orange County, a complete, plain-language services list "
  "is one of the simplest ways to show up for the specific jobs you want more of.</p>")],
"google-business-profile-links": [
 ("Common link mistakes", ul([
  "Linking every action to the homepage instead of the booking, menu or order page.",
  "Leaving old third-party links in place after switching to a new provider.",
  "Not setting a preferred link, so a third-party option appears first.",
  "Using links that break on phones or require customers to log in first.",
  "Forgetting to check links after a website redesign changes page addresses."])),
 ("Choosing your own links or third parties", "<p>Third-party platforms can bring convenience and sometimes new customers, but they "
  "usually take a fee and own the customer relationship. Your own booking or ordering system typically costs less per transaction and "
  "lets you keep customer details for repeat business. Many businesses use both: their own link as the preferred option and a third "
  "party as a backup. Whatever you choose, make the path short: a customer in Anaheim who taps Book or Order on your profile should reach "
  "a page where they can finish the task in a minute or two on a phone. Review the numbers every few months and adjust the preferred "
  "link if one route clearly converts better.</p>")],
"google-business-profile-booking-button": [
 ("Common booking setup mistakes", ul([
  "Turning on a provider without checking its fees for bookings made through Google.",
  "Letting the provider's calendar fall out of step with real staff schedules.",
  "Offering services online that need a consultation first, which leads to cancellations.",
  "Forgetting to update availability before holidays and closures.",
  "Expecting performance data for a custom link, which Google says is not available."])),
 ("Is a booking button right for you?", "<p>A booking button suits businesses where customers book a set service for a set time: "
  "haircuts, nails, massages, fitness classes, restaurant tables and many health appointments. It suits jobs that need a quote or site "
  "visit less well; those businesses are usually better served by a clear quote request link. Before you turn bookings on, check how "
  "you take bookings today, how much each one costs you through each route, and whether your team can keep the online calendar accurate. "
  "For salons, studios and restaurants in Anaheim and across Orange County, a working booking button can capture customers who decide "
  "late in the evening, long after the phones are off.</p>")],
"google-business-profile-performance": [
 ("Common mistakes when reading performance", ul([
  "Comparing a busy month with a quiet one and drawing conclusions about the profile.",
  "Forgetting that Google Ads activity is included in the numbers.",
  "Treating views as customers when calls, directions and bookings are the real signals.",
  "Checking the report once and never again, so trends go unnoticed.",
  "Not connecting profile actions to real leads and sales in your own records."])),
 ("A simple monthly report", "<p>Keep a one-page record each month with five numbers: views, calls, direction requests, website clicks "
  "and bookings or messages where they apply. Add a short note of anything you changed on the profile that month, such as new photos, "
  "services or a run of new reviews, and anything outside the profile, such as an ad campaign or a seasonal rush. After six months you "
  "will see which changes lined up with more calls and directions. Add the top search terms to the record as well; when a service keeps "
  "appearing in searches, give it a clear place on your profile and its own page on your website. This is the same routine Chimera uses "
  "for businesses in Anaheim and Orange County.</p>")],
"google-automated-calls-to-your-business": [
 ("Common mistakes with automated calls", ul([
  "Hanging up on every automated call and missing customer booking requests.",
  "Trusting any caller who says they are from Google, even when they ask for money.",
  "Clicking links in unexpected texts claiming to be about your listing.",
  "Giving staff no guidance, so answers to Google's questions are guessed.",
  "Never checking what information has been added to the profile from these calls."])),
 ("A short script for your front desk", "<p>Give whoever answers the phone a few lines to follow. If an automated call asks to confirm "
  "hours or services, answer accurately and briefly, and tell the manager afterwards so the profile can be checked. If it is a booking "
  "or availability request on behalf of a customer, treat it like any other customer enquiry. If any caller claiming to be Google asks "
  "for a payment, card details, passwords or verification codes, end the call, do not click any links sent afterwards and report it to "
  "the manager. Post these points near the phone. For busy businesses in Anaheim and across Orange County, this small step protects the "
  "profile and makes sure genuine requests become customers.</p>")],
}


def add_extras(pages):
    for p in pages:
        secs = p["sections"]
        last = secs.pop()
        for h, b in EXTRA[p["slug"]]:
            secs.insert(len(secs) - 4, {"heading": h, "body_html": b})
        secs.append(last)

MORE = {
"how-to-create-google-business-profile": "Owners often ask how long it takes before a new profile appears in searches. Once it is verified and complete, it can start showing for searches near you, but visibility grows with time, reviews and accurate details rather than overnight. Another common question is whether a business with no storefront can still have a profile; it can, as long as it meets customers in person at their location, using a service area. Finally, owners ask whether they should create profiles for nearby cities they serve. They should not: one real business location gets one profile, and the service area tells Google which cities you cover.",
"how-to-claim-google-business-profile": "Owners often ask whether claiming will erase the reviews already on the listing. It does not: reviews stay with the profile, which is one reason to claim the existing listing rather than start again. Another common question is whether a claimed listing will rank immediately. Claiming gives you control; rankings improve as you complete the profile, earn reviews and keep details accurate. Owners also ask what happens if verification fails. Check that the name, address and category follow Google's guidelines, fix anything that does not, and try again with the methods Google offers.",
"how-to-edit-google-business-profile": "Owners often ask why a detail they changed went back to the old value. Usually an edit was not approved, or information from another source was applied; check the edit status and Collected info. Another common question is how quickly an edit goes live. Google reviews changes first, so give important updates, such as new hours or a new phone number, some lead time. Owners also ask whether editing often harms the profile. Regular, accurate updates are fine; repeated changes to the same core details, especially the name, are what to avoid.",
"google-business-profile-owners-and-managers": "Owners often ask what to do when the only owner has left and cannot be reached. Google offers an ownership request route for people authorized to manage the business; keep documents that show your role. Another common question is whether managers can see the performance data. They can view and download insights, so agencies and staff can report without owner access. Owners also ask how many managers is too many. There is no need for everyone to have access; give it to the people who actively manage reviews, posts and details, and review the list regularly.",
"google-business-profile-attributes": "Owners often ask why an attribute they set is not showing. Some attributes only appear for certain categories or regions, and edits can take time to review, so check again after a few days. Another common question is whether attributes replace a good description. They do not: attributes answer specific yes-or-no questions, while the description and services explain what you do. Owners also ask whether to select attributes that apply only part of the time. Choose the answer that is true for a typical visit, and use special hours or updates to explain temporary changes.",
"google-business-profile-services": "Owners often ask how many services to list. List every service you genuinely want enquiries for, grouped so the list stays easy to scan; there is no prize for padding it with services you rarely do. Another common question is whether prices must be shown. Prices are optional, but a price or range can filter out poor-fit enquiries and build trust. Owners also ask whether services replace service pages on the website. They do not: the profile list helps people on Google, while a dedicated page for each important service gives Google and AI assistants the detail they need. A good rule of thumb is that every service worth listing on the profile is worth a short page of its own, with the same name, a plain description of what is included, the areas you cover and how to get a quote. Link that page from your services list where Google allows, and from your homepage, so customers and search engines can find it easily.",
"google-business-profile-links": "Owners often ask why a third-party link appeared on their profile without their permission. Partners can supply links to Google, which is why Google provides ways to hide food ordering providers and routes to request removal of booking links. Another common question is whether links affect rankings. Their main job is to help customers act; a profile that leads more people to book or order is doing its work. Owners also ask what to link when they have no online booking. A clear contact or quote page with a short form is a sensible choice for a services link.",
"google-business-profile-booking-button": "Owners often ask whether a booking button replaces phone bookings. It does not need to: many customers still call, and a button simply adds another route for people who prefer to book online. Another common question is how to change providers. Set up the new provider, then follow the old provider's process to stop bookings through Google, and check the profile afterwards. Owners also ask whether restaurants need both reservations and a waitlist. It depends on how you seat guests; walk-in-heavy restaurants may benefit most from a waitlist, while bookable dining rooms suit reservations. Owners also ask what to do when a customer books a slot that is no longer free. That is a sign the provider calendar and the real schedule are out of step; fix the sync first, then contact the customer quickly with an alternative time. A good habit is to check the online calendar each morning and block out staff holidays, training days and closures well in advance, so that customers who book through Google only ever see times you can actually honor.",
"google-business-profile-performance": "Owners often ask why calls in the report do not match their phone bill. The report counts taps on the call button from the profile, not every call the business receives, so the two will differ. Another common question is why views dropped while calls stayed steady. Views can move with seasonality and search behavior; actions such as calls and directions are usually the better measure. Owners also ask how long it takes to see the effect of changes. Give changes a few months and compare like-for-like periods before deciding what worked.",
"google-automated-calls-to-your-business": "Owners often ask whether they can stop automated calls entirely. Google describes these calls as a standard way to keep details accurate and to pass on customer requests, so the better approach is to prepare staff to handle them. Another common question is how to tell a real call from a scam. Real calls ask about business details or a customer's request; scams ask for money, card details, passwords or codes. Owners also ask what to do if wrong details were added after a call. Edit the profile and review Collected info to correct or delete them.",
}

_orig_add = add_extras


def add_extras(pages):  # noqa: F811
    _orig_add(pages)
    for p in pages:
        secs = p["sections"]
        secs.insert(len(secs) - 3, {"heading": "Questions owners ask us", "body_html": f"<p>{MORE[p['slug']]}</p>"})
