"""Blog post 6 for 2026-11-11: OpenAI's Businesses in ChatGPT.
Facts come only from OpenAI's announcement (Nov 10, 2026). openai.com refuses automated requests, so the text was
supplied by the site owner from the live page; the title and date match OpenAI's own RSS feed."""
from common import CORE, L, SRC, V, save_all
import blog_2026_11_11  # noqa: F401  (SRC entries)
from blog_2026_11_10 import LOCAL_FAQ, blog

SRC.update({
    "oai_biz": {"title": "OpenAI: Introducing Businesses in ChatGPT (Nov 10, 2026)",
                "url": "https://openai.com/index/introducing-businesses-chatgpt/"},
    "oai_biz_policy": {"title": "OpenAI: Business Agents policy (eligible categories)",
                       "url": "https://openai.com/policies/business-agents-policy/"},
})
AUD = CORE["audit"]
LOCAL = L("GEO agency in Orange County", "geo-agency-orange-county")

PAGES = [
blog(6, "AI assistants",
     slug="businesses-in-chatgpt-claim-your-business", query="businesses in chatgpt", kw="Businesses in ChatGPT",
     eyebrow="AI assistants", short_title="Businesses in ChatGPT: claim your business",
     title="Businesses in ChatGPT: How to Claim Your Business",
     meta="OpenAI launched Businesses in ChatGPT: claim your business, manage details and see insights. What Anaheim and Orange County businesses should do now.",
     h1="Businesses in ChatGPT: What It Is and Why Orange County Businesses Should Claim Theirs",
     answer="Businesses in ChatGPT is a new OpenAI beta, launched on November 10, 2026, that lets businesses claim their business in ChatGPT through Business Hub, keep their details current, add product feeds and see aggregated insights such as mentions and website clicks. For Anaheim and Orange County businesses, it is the ChatGPT equivalent of claiming a Google Business Profile, and worth doing early.",
     takeaways=["OpenAI launched Businesses in ChatGPT in beta on November 10, 2026.", "Business Hub lets you claim your business and update key details once verified.",
                "Insights show mentions, website clicks and discovery topics.", "Business Agents start with eligible U.S. ecommerce and online service businesses.",
                "OpenAI says it does not share users' conversations with businesses."],
     sections=[
      ("What OpenAI announced", "<p>On November 10, 2026, OpenAI introduced Businesses in ChatGPT in beta, describing it as a new way for businesses to connect with the 1.2 billion people who use ChatGPT each week, a figure OpenAI gives in the announcement. The launch has two parts: Business Hub, where businesses claim their business, manage their information and see insights, and Business Agents, a way for businesses to talk with customers inside ChatGPT, starting with eligible ecommerce and online service businesses in the U.S.</p>"),
      ("Claiming your business", "<p>In Business Hub, companies can claim their organization in ChatGPT. Once verified, they can update key details and add self-service product feeds with pricing and availability. OpenAI says this gives businesses a new way to provide information to ChatGPT, so people exploring products and services see the most accurate and up-to-date details.</p>"),
      ("Who can claim", "<p>OpenAI says any eligible business located where ChatGPT is available can claim its business through Business Hub. Existing OpenAI Enterprise customers and advertisers can work with their OpenAI representative instead. Shopify merchants can connect their store from Business Hub or the Shopify admin to streamline verification, and OpenAI notes that eligible products from Shopify merchants are already integrated into ChatGPT through Shopify Catalog.</p>"),
      ("The insights you get", "<table><tr><th>Insight</th><th>What it tells you</th></tr><tr><td>Mentions</td><td>How often your business is mentioned in ChatGPT</td></tr><tr><td>Website clicks</td><td>How many clicks your website receives from ChatGPT</td></tr><tr><td>Discovery topics</td><td>Common themes across conversations where your website is cited</td></tr></table><p>OpenAI says these insights can help businesses understand how they are represented and find opportunities to improve the information they share.</p>"),
      ("Privacy built in", "<p>OpenAI states that it does not share users' conversations or Business Agent chats with businesses. Insights are aggregated and only appear when there are enough conversations or interactions to meet certain thresholds. A small business with little ChatGPT visibility may therefore see limited data at first.</p>"),
      ("What Business Agents are", "<p>After claiming their business, eligible organizations can build, test and launch a Business Agent, which OpenAI describes as a new way to answer questions and help people explore their offerings. When a business appears in a ChatGPT response, people can click through to its ChatGPT profile and, if an agent is available, start a conversation with the business. OpenAI says that conversation is clearly labeled, separate from the person's original ChatGPT conversation and distinct from ChatGPT's independent answers.</p>"),
      ("Who can use Business Agents today", "<p>OpenAI says Business Agents are available to eligible ecommerce and online service businesses in the United States, with eligible categories listed in its Business Agents policy. Most local service businesses in Anaheim and Orange County, such as plumbers, dentists or restaurants, can claim their business and use insights now, but should not expect an agent yet. OpenAI says it plans to expand Businesses in ChatGPT and Business Agents to more markets and business categories over time.</p>"),
      ("Ads and sponsored agents", "<p>Businesses can also sponsor their Business Agent and use it as the destination for ChatGPT Ads. OpenAI says sponsored placements are clearly labeled and separate from ChatGPT responses. That separation matters: paying for an ad is not described as changing ChatGPT's own answers.</p>"),
      ("Does claiming help you get recommended?", "<p>OpenAI's announcement does not say that claiming a business improves how often ChatGPT recommends it, and we will not claim otherwise. What it does say is that claiming lets you supply accurate, up-to-date details. Wrong hours, an old address or outdated prices are exactly the kind of errors that make an AI answer less useful, so correcting them at the source is worthwhile on its own.</p>"),
      ("Why this matters in Orange County", "<p>Orange County had 3,186,989 residents in the 2020 census, and Anaheim alone had 346,824. Many of them, and the visitors who come for Anaheim's attractions and conventions, now ask AI assistants where to eat, who to call and what to buy. A verified ChatGPT presence with accurate details sits alongside your Google Business Profile as part of being findable in 2026.</p>"),
      ("How to get ready", "<ol><li>Make sure your business name, address, phone, hours and services are identical on your website, Google Business Profile and main directories.</li><li>Claim your business through Business Hub if you are eligible.</li><li>Once verified, check and update every key detail.</li><li>If you sell products, set up a product feed with accurate pricing and availability, or connect Shopify.</li><li>Review insights monthly once they appear.</li></ol>"),
      ("Use discovery topics to improve your website", "<p>Discovery topics show the themes of conversations where your website is cited. If ChatGPT cites you mostly for one service while you want to be known for another, that is a signal to strengthen the page for the second service: a direct answer at the top, specific details, prices or price ranges, service area and real proof. The same improvements help Google and other AI assistants.</p>"),
      ("Keep ChatGPT and Google consistent", "<p>Treat your ChatGPT business details like another listing. Any time you change hours, move, add a service or rename something, update your website, Google Business Profile and ChatGPT together. Consistency across sources makes it easier for every AI assistant to describe you correctly.</p>"),
      ("A worked example", "<p>Imagine a family-owned gift shop in downtown Fullerton that also sells online through Shopify. The owner connects the store from the Shopify admin to streamline verification, checks that the shop's hours and address match its Google Business Profile, and confirms product pricing and availability are current. A month later, the insights show which discovery topics bring mentions, and the owner expands the website's pages on the gift categories people ask about. As an online store in the U.S., the shop could also check whether it is eligible for a Business Agent.</p>"),
      ("What to watch next", "<p>OpenAI calls this an early step and says it will expand to more markets and business categories and build tools for organizations with more complex needs. Local service businesses should watch for Business Agents reaching their category, and for richer insights as data builds up.</p>"),
      ("The short version", "<p>Businesses in ChatGPT lets you claim your business, keep your details accurate and see how people find you in ChatGPT. Anaheim and Orange County businesses should claim theirs where eligible, keep every listing consistent and use the insights to improve their website. Chimera, based in Anaheim, helps local businesses get this right across ChatGPT, Google and other AI assistants.</p>")],
     faqs=[("What is Businesses in ChatGPT?", "An OpenAI beta, launched November 10, 2026, that lets businesses claim their business in ChatGPT, manage information and see insights through Business Hub."),
           ("How do I claim my business in ChatGPT?", "Through Business Hub, if your business is eligible and located where ChatGPT is available; Enterprise customers and advertisers can work with their OpenAI representative."),
           ("What insights does Business Hub show?", "Aggregated mentions, website clicks and discovery topics, the themes of conversations where your website is cited."),
           ("Does OpenAI share customer chats with businesses?", "No. OpenAI says it does not share users' conversations or Business Agent chats with businesses."),
           ("Who can use Business Agents?", "Eligible ecommerce and online service businesses in the United States, for now."),
           ("Does claiming my business improve ChatGPT recommendations?", "OpenAI does not say so; it says claiming lets you keep your information accurate and up to date."),
           ("Can Shopify stores join?", "Yes. Shopify merchants can connect their store from Business Hub or the Shopify admin to streamline verification."),
           ("Are sponsored Business Agents labeled?", "Yes. OpenAI says sponsored placements are clearly labeled and separate from ChatGPT responses."),
           LOCAL_FAQ],
     links=[L("how ChatGPT recommends local businesses", "how-chatgpt-recommends-local-businesses"), L("how to rank in ChatGPT", "how-to-rank-in-chatgpt"),
            L("how to check if ChatGPT mentions your brand", "how-to-check-if-chatgpt-mentions-your-brand"), LOCAL, AUD],
     sources=["oai_biz", "oai_biz_policy", "w_oc", "w_anaheim"],
     visuals=[V.flow(0, "How Businesses in ChatGPT works", "The steps OpenAI describes, from claim to conversation.",
               [("Claim", "Claim your business in Business Hub."), ("Update", "Once verified, edit details and add product feeds."),
                ("Learn", "See mentions, website clicks and discovery topics."), ("Engage", "Eligible U.S. businesses can launch a Business Agent.")]),
              V.timeline(6, "Who gets what today", "Availability as described in OpenAI's announcement.",
               [("Eligible businesses", "Claim and insights", "Where ChatGPT is available."), ("Shopify merchants", "Faster verification", "Connect from Business Hub or Shopify admin."),
                ("U.S. ecommerce and online services", "Business Agents", "Eligible categories per OpenAI's policy."), ("Later", "Expansion", "More markets and business categories planned.")])],
     secondary=["ChatGPT Business Hub", "claim business on ChatGPT", "ChatGPT Business Agents", "ChatGPT business profile"],
     hero_query="How do I claim my business on ChatGPT?"),
]

if __name__ == "__main__":
    save_all(PAGES)
