"""Extra practical sections for the 2026-11-18 blogs (general advice; facts stay on the main pages)."""
X = {
"gemini-tasks-calls-local-businesses": [
 ("Handling busy times", "The calls that matter most often arrive when you are busiest, such as Monday mornings for auto shops or Friday afternoons for salons. If you can't answer every call live, set up a call-back routine: a short voicemail that says when you'll return calls, a person responsible for returning them within the hour, and a simple log so no booking request is lost. Some businesses use a call-answering service during peak hours, given a clear list of services, availability and booking rules. Whatever you choose, test it by calling your own number at a busy time and seeing what a customer, or an assistant, would experience."),
 ("What to put on your Business Profile", "Use the profile fields Google provides as fully as possible: the most specific primary category, additional categories that genuinely apply, every service you offer with a short description, accurate hours including holidays, and an appointment or booking link if you have one. In the description, say plainly whether you take appointments, walk-ins or both, and for which services. An assistant choosing between nearby businesses can only use what it can read, so complete, accurate fields make it easier to choose you."),
],
"google-wallet-ios-local-businesses": [
 ("Choosing a digital loyalty approach", "Small businesses have several options. Some point-of-sale systems include digital loyalty with cards customers can save to their phone wallet. Others use a simple card with a barcode or QR code linked to a customer account. A few still use paper punch cards. If you're choosing now, favor an option customers can carry on their phone and that staff can scan quickly, and make joining take less than a minute. Ask your point-of-sale provider what it supports before buying anything new."),
 ("Making rewards worth carrying", "A digital card only helps if customers want to use it. Keep rewards simple and achievable, such as a free item after a set number of visits or a small discount on a birthday, and tell customers how close they are to the next reward. Clear, generous rewards encourage people to keep your card in their wallet, whether on an iPhone or an Android phone, and to choose you over a nearby competitor when they're deciding where to go."),
 ("Online sellers and Google Pay", "If you sell online, check that your checkout accepts Google Pay, since Google describes Wallet as a way to check out faster online across Google and wherever Google Pay is used. A faster checkout reduces abandoned carts, especially on phones. Test your checkout on both an iPhone and an Android phone to make sure the payment options display correctly."),
],
"holiday-search-features-local-businesses": [
 ("Getting store inventory onto Google", "For retailers, the practical route to appearing in local in-stock results is Google Merchant Center. Set up a Merchant Center account, add your products, connect your Google Business Profile, and turn on free local listings with an inventory feed showing which products are in each store. Many point-of-sale systems can export inventory automatically. Start with your best-selling and most giftable products, keep stock levels updated daily during the holidays, and check Merchant Center for any issues that stop products from showing."),
 ("Restaurants: make holiday bookings easy", "Holiday diners often book for larger groups and special occasions. Make it clear online how far ahead reservations open, the largest party size you take online, whether you offer private dining or set menus, and any deposits or cancellation rules. Keep your reservation system's availability current, and add holiday hours to your Business Profile early. When AI Mode looks for tables that match a party size and time, accurate availability is what puts your restaurant in front of the guest."),
 ("Hotels and venues near Anaheim", "Hotels near the Anaheim Resort District and venues across Orange County see some of their busiest weeks around the holidays. Keep amenity lists specific, such as parking, shuttles, family rooms or fireplaces, and make sure rates and room types match across your website and booking partners. Venues should publish event dates, ticket prices and on-sale times clearly, so search features can pick up changes as soon as they happen."),
],
"google-vids-avatars-small-business-video": [
 ("Video ideas by industry", "Different businesses can use short avatar videos in different ways. A dentist might explain what happens at a first visit; a contractor might explain how quotes and scheduling work; a restaurant might introduce its holiday menu; a salon might explain how to book color services; an accountant might cover what documents to bring at tax time. Keep each video focused on one question, and pair it with real photos of your premises or work on the same page, so customers see both the explanation and the real thing."),
 ("Getting the most from a short video", "Short videos work best when the first few seconds say exactly what the viewer will learn. Start with the question, answer it simply, and end with one action. Keep videos under two minutes, and test them on a phone, since most local customers will watch there. If you publish on YouTube as well as your website, use a clear title that says what the video answers and mentions your city where relevant, for example how quoting works for kitchen remodels in Anaheim."),
 ("Protecting your likeness and brand", "Because the avatar uses your own face and voice, treat it like any other brand asset. Keep your Google account secure with a strong password and two-step verification, review every video before publishing, and don't let anyone else create videos with your avatar without your approval. If you stop using a video, remove it from your site and channels so outdated information doesn't circulate."),
],
"ai-mode-temporary-threads-businesses": [
 ("Writing pages a stranger understands", "Imagine a customer who has never heard of you, asking an AI assistant for a recommendation with no history to draw on. What would it need to know to suggest you? Start each important page with one or two sentences that say what you do, for whom and where, such as family dentistry in Tustin with Saturday hours. Follow with the details people compare: services, price ranges or how pricing works, availability and what makes you different. Avoid vague slogans, which give an AI system nothing concrete to use."),
 ("Structured data helps machines read you", "Structured data, such as LocalBusiness or Product markup, states key facts in a format search systems can read reliably: your name, address, phone, hours, products and prices. It doesn't guarantee anything, but it reduces ambiguity, which matters more when answers rely only on public information. Make sure the details in your markup match what's visible on the page and on your Business Profile."),
 ("Reviews that help strangers decide", "When someone has no history with your business, reviews describing real experiences carry extra weight. Encourage customers to mention what they bought or what you did for them, and how it went. Reply to reviews in a helpful, specific way. Over time, these reviews give AI systems and people alike a clear, trustworthy picture of your business, even in a temporary thread."),
],
}
ADD = {
"google-vids-avatars-small-business-video": [
[
"Planning a small video library",
"Rather than making one video and stopping, plan a small library over a month or two. List the ten questions customers ask most, group them by service, and create one short avatar video for each. Add each to the most relevant page on your website, with a written summary, and share it on your Business Profile and social channels. Review the list every quarter and add videos for new questions as they come up."
]
],
"ai-mode-temporary-threads-businesses": [
[
"Local details make a difference",
"For a local business, the details a stranger needs usually include where you are, which areas you serve, when you're open and how to get in touch or book. Put these on every important page, not only the contact page, and keep them identical to your Business Profile. For businesses in Anaheim and across Orange County, naming the city and neighborhood naturally in your page text helps search systems connect you to local questions, whether or not the person asking has any history with you."
]
]
}
for k, v in ADD.items():
    X[k] += [tuple(x) for x in v]


def add_x(pages):
    for p in pages:
        for h, b in X.get(p["slug"], []):
            p["sections"].insert(len(p["sections"]) - 1, {"heading": h, "body_html": f"<p>{b}</p>"})
