"""Drafts for the first engine batch (pages 1-3). Run: python content/build/batch1.py"""
import json
from pathlib import Path

DRAFTS = Path(__file__).resolve().parents[1] / "drafts"
B = "https://thechimeraai.com"

SRC = {
    "geo": {"title": "GEO: Generative Engine Optimization (Aggarwal et al., KDD 2024)", "url": "https://arxiv.org/abs/2311.09735"},
    "aif": {"title": "Google Search Central: AI features and your website", "url": "https://developers.google.com/search/docs/appearance/ai-features"},
    "helpful": {"title": "Google Search Central: Creating helpful, reliable, people-first content", "url": "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"},
    "spam": {"title": "Google Search Central: Spam policies", "url": "https://developers.google.com/search/docs/essentials/spam-policies"},
    "sd": {"title": "Google Search Central: Introduction to structured data", "url": "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"},
    "oai": {"title": "OpenAI: Overview of OpenAI crawlers", "url": "https://platform.openai.com/docs/bots"},
    "pplx": {"title": "Perplexity: Perplexity crawlers", "url": "https://docs.perplexity.ai/guides/bots"},
    "gcrawl": {"title": "Google Search Central: Google's common crawlers (including Google-Extended)", "url": "https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers"},
    "llms": {"title": "The llms.txt proposal", "url": "https://llmstxt.org"},
    "indexnow": {"title": "IndexNow: how it works", "url": "https://www.indexnow.org/"},
    "robots": {"title": "Google Search Central: Introduction to robots.txt", "url": "https://developers.google.com/search/docs/crawling-indexing/robots/intro"},
}


def L(anchor, slug):
    return {"anchor": anchor, "url": f"{B}/{slug}/" if slug else f"{B}/"}


CORE = {
    "services": {"anchor": "Chimera's GEO services", "url": f"{B}/#services"},
    "process": {"anchor": "how Chimera's six-phase GEO build works", "url": f"{B}/#process"},
    "results": {"anchor": "GEO results for real brands", "url": f"{B}/#results"},
    "audit": {"anchor": "book a free AI visibility audit", "url": f"{B}/#audit"},
    "hub": {"anchor": "all GEO guides and answers", "url": f"{B}/insights/"},
}


def save(spec):
    DRAFTS.mkdir(parents=True, exist_ok=True)
    (DRAFTS / f"{spec['slug']}.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
    print("wrote", spec["slug"])


PAGES = []

# ---------------------------------------------------------------- 1
PAGES.append({
    "query": "generative engine optimization agency",
    "slug": "generative-engine-optimization-agency",
    "eyebrow": "GEO agency guide",
    "primary_keyword": "generative engine optimization agency",
    "secondary_keywords": ["GEO agency", "AI search agency", "ChatGPT visibility", "AI Overviews optimization"],
    "search_intent": "commercial",
    "seo": {
        "title": "Generative Engine Optimization Agency: What They Do",
        "meta_description": "What a generative engine optimization agency actually does, what a good engagement includes, and how to tell if your brand needs one yet.",
    },
    "h1": "Generative Engine Optimization Agency: What It Does and When You Need One",
    "answer": "A generative engine optimization agency gets your brand found, trusted and cited by AI assistants such as ChatGPT, Gemini, Perplexity, Claude and Google AI Overviews. It audits how those engines describe you today, fixes what blocks them, restructures key pages into quotable answers, and builds the outside signals that make AI recommend you.",
    "key_takeaways": [
        "A GEO agency works on being cited inside AI answers, not only on ranking a link.",
        "Good engagements start with an audit of what each AI engine says about you today.",
        "Most of the work is technical access, page structure, quotable content and brand authority.",
        "GEO builds on SEO: AI answers lean heavily on pages search engines can already crawl and trust.",
        "Judge an agency on measurement and transparency, not on promises about placement.",
    ],
    "sections": [
        {"heading": "What a generative engine optimization agency actually does",
         "body_html": "<p>Generative engine optimization (GEO) is the practice of making a brand easy for AI systems to find, understand, trust and quote. A generative engine optimization agency does that work for you across the engines your buyers use: ChatGPT, Google Gemini and AI Overviews, Perplexity, Claude and Microsoft Copilot.</p><p>The goal is different from classic SEO. A search result page shows ten links and lets the buyer choose. An AI answer usually names a handful of brands, explains why, and links to a few sources. If you are not one of those names, you are invisible for that question, even if you rank on page one.</p><p>So a GEO agency asks a specific question for every topic that matters to your business: <em>when a buyer asks an AI assistant about this, does it mention us, describe us correctly, and link to us?</em> Then it works on the gaps.</p>"},
        {"heading": "The core services in a GEO engagement",
         "body_html": "<p>Engagements vary, but a complete generative engine optimization agency covers six areas:</p><ol><li><strong>AI visibility audit.</strong> Running your buyers' real questions through each engine and recording who gets mentioned, how you are described, and which sources are cited.</li><li><strong>Technical access.</strong> Making sure AI crawlers such as OpenAI's OAI-SearchBot and PerplexityBot can reach your pages, that pages are indexed, and that nothing important is hidden behind scripts or logins.</li><li><strong>Machine-readable structure.</strong> Organization, Service, Article and FAQ schema, a clean sitemap and an <code>llms.txt</code> file that maps your most useful pages.</li><li><strong>GEO content structuring.</strong> Rewriting key pages at passage level: direct answers at the top, question-style headings, comparison tables and specific, sourced facts.</li><li><strong>Entity and authority building.</strong> Consistent brand descriptions across your site, profiles, directories and earned mentions, so engines can confidently connect your name to your specialty.</li><li><strong>Citation tracking.</strong> Re-testing the same questions over time and reporting mentions, citations and AI-referred visits and leads.</li></ol>"},
        {"heading": "How a GEO agency differs from an SEO agency",
         "body_html": "<p>There is real overlap. Google states that the same fundamentals apply to its AI features as to Search: helpful, reliable content that can be crawled and indexed. Many AI answers cite pages that already rank well. That is why a serious GEO agency keeps SEO running in parallel rather than replacing it.</p><table><tr><th></th><th>Traditional SEO agency</th><th>Generative engine optimization agency</th></tr><tr><td>Main goal</td><td>Rank pages in search results</td><td>Be named and cited inside AI answers</td></tr><tr><td>Unit of work</td><td>Pages and keywords</td><td>Passages, entities and questions</td></tr><tr><td>Key signals</td><td>Links, relevance, technical health</td><td>Clear answers, sourced facts, brand mentions, crawl access for AI bots</td></tr><tr><td>Reporting</td><td>Rankings, clicks, impressions</td><td>Mentions and citations per engine, AI referral traffic, leads</td></tr></table><p>The difference is emphasis. An SEO agency asks how to rank a page. A GEO agency asks whether an AI system would choose your page, or your brand, as the answer.</p>"},
        {"heading": "Signs your business is ready for a GEO agency",
         "body_html": "<p>GEO pays off fastest when buyers research before they contact anyone. You are a good fit if:</p><ul><li>Your buyers compare providers, read reviews and ask for recommendations before they buy.</li><li>You sell a service, software or a considered purchase rather than an impulse product.</li><li>Competitors are already being named when you test questions in ChatGPT or Perplexity.</li><li>You have a clear specialty an AI engine could describe in one sentence.</li><li>Your website already works: it loads, it is indexed, and it has a way to contact you.</li></ul><h3>When to wait</h3><p>If your site has almost no indexed pages, no clear offer, or no contact path, fix those basics first. GEO amplifies what is already there. It does not replace a working website or a product people want.</p>"},
        {"heading": "What a good first 90 days looks like",
         "body_html": "<p>A credible generative engine optimization agency should be able to show you a plan like this before you sign:</p><ul><li><strong>Weeks 1–2: diagnose.</strong> A baseline of how each engine answers your top 30–50 buyer questions, plus a technical audit of crawl access, indexing and structured data.</li><li><strong>Weeks 2–4: fix.</strong> Unblock AI crawlers, repair indexing problems, add schema and <code>llms.txt</code>, and set up tracking for AI referrers and form submissions.</li><li><strong>Weeks 4–8: structure and content.</strong> Rebuild the pages that matter most and publish new pages that answer high-intent questions directly.</li><li><strong>Weeks 8–12: authority and measurement.</strong> Start earning mentions in places engines trust, re-run the baseline questions, and report what moved.</li></ul><p>Expect early citations on specific, long-tail questions first. Broad, competitive questions take longer, and nobody controls what an AI model says on a given day.</p>"},
        {"heading": "How to measure what a GEO agency delivers",
         "body_html": "<p>Vague reports are the biggest risk with any new discipline. Ask for numbers you can check yourself:</p><ul><li><strong>Mentions and citations:</strong> for a fixed list of buyer questions, how often each engine names you or links to you, month over month.</li><li><strong>AI referral traffic:</strong> visits from chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com and claude.ai, grouped as their own channel in Google Analytics.</li><li><strong>Leads by source:</strong> form submissions tied to the page and the engine that sent the visitor.</li><li><strong>Search health:</strong> indexed pages, impressions and clicks from Google Search Console.</li></ul><p>If an agency cannot explain how it will measure progress, or promises a fixed position inside ChatGPT, treat that as a warning sign.</p>"},
        {"heading": "Questions to ask before you hire",
         "body_html": "<ol><li>Can you show me what ChatGPT, Gemini and Perplexity say about my brand today?</li><li>Which of my pages would you change first, and why?</li><li>How do you handle crawl access for AI bots, and which ones do you allow?</li><li>What does your monthly report contain, and can I see an example?</li><li>How do you keep traditional SEO healthy while doing GEO?</li><li>What will you need from my team each month?</li></ol><p>A strong agency answers these with specifics about <em>your</em> site, not with a generic deck.</p>"},
    ],
    "faqs": [
        {"q": "What does a generative engine optimization agency do?", "a": "It improves how AI assistants such as ChatGPT, Gemini, Perplexity, Claude and Google AI Overviews find, describe and cite your brand. The work covers an AI visibility audit, technical crawl access, schema and llms.txt, rewriting key pages into quotable answers, building brand authority, and tracking citations and AI-referred leads."},
        {"q": "Is a GEO agency different from an SEO agency?", "a": "Yes, in emphasis. SEO focuses on ranking pages in search results, while GEO focuses on being named and cited inside AI answers. The two overlap heavily, so a good GEO agency keeps SEO running in parallel."},
        {"q": "How long does it take to see results from a GEO agency?", "a": "Most brands see technical fixes and first citations on specific questions within the first two to three months. Competitive, broad questions take longer, and results depend on how quickly pages are indexed and how strong your existing authority is."},
        {"q": "Can a GEO agency guarantee my brand appears in ChatGPT?", "a": "No. Nobody controls what an AI model says, and answers change over time. A good agency improves the odds by making your brand the clearest, best-supported option to cite, and shows the change with measurement."},
        {"q": "What should a GEO agency report every month?", "a": "Mentions and citations for a fixed set of buyer questions in each engine, visits from AI referrers, leads by source page, and search health from Google Search Console. You should be able to verify each number yourself."},
        {"q": "Do small businesses need a generative engine optimization agency?", "a": "Small specialists often benefit most, because AI engines can describe a clear niche more easily than a broad generalist. Start with the questions your best customers ask before they buy and check whether AI assistants mention you for them."},
    ],
    "internal_links": [CORE["services"], CORE["process"], L("how to choose a GEO agency", "how-to-choose-a-geo-agency"), L("GEO vs SEO: the real differences", "geo-vs-seo"), CORE["audit"]],
    "sources": [SRC["geo"], SRC["aif"], SRC["oai"], SRC["pplx"]],
})

# ---------------------------------------------------------------- 2
PAGES.append({
    "query": "how to choose a geo agency",
    "slug": "how-to-choose-a-geo-agency",
    "eyebrow": "Buyer's checklist",
    "primary_keyword": "choose a GEO agency",
    "secondary_keywords": ["GEO agency checklist", "best GEO agency", "generative engine optimization services", "AI search agency"],
    "search_intent": "commercial",
    "seo": {
        "title": "How to Choose a GEO Agency: A 10-Point Checklist",
        "meta_description": "A practical checklist to choose a GEO agency: what to ask, what proof to expect, red flags to avoid, and how to compare proposals side by side.",
    },
    "h1": "How to Choose a GEO Agency: A 10-Point Checklist",
    "answer": "To choose a GEO agency, ask each one to show what AI engines say about your brand today, explain exactly which pages and signals they would change first, and describe how they measure citations, AI-referred traffic and leads. Prefer agencies that run SEO in parallel, explain their crawl and schema approach, and never promise a fixed spot inside ChatGPT.",
    "key_takeaways": [
        "Start every conversation by asking for a live look at what AI engines say about you.",
        "A real plan names specific pages, technical fixes and questions, not just tactics.",
        "Measurement should be verifiable: citations per engine, AI referral visits and leads.",
        "Promises of guaranteed placement in AI answers are a red flag.",
        "Compare proposals on the same scorecard so price is not the only thing you see.",
    ],
    "sections": [
        {"heading": "Why choosing a GEO agency is harder than choosing an SEO agency",
         "body_html": "<p>Generative engine optimization is young. Many agencies have added \"AI\" to an existing SEO menu without changing how they work, and the results of GEO are harder to see than a ranking report. That makes it easy to buy the wrong thing.</p><p>The good news is that you can test most of what matters before you sign anything. A capable agency can show you, in a single call, how ChatGPT, Perplexity, Gemini and Google AI Overviews currently answer your buyers' questions, and explain why you are or are not in those answers.</p>"},
        {"heading": "The 10-point checklist to choose a GEO agency",
         "body_html": "<ol><li><strong>They show your baseline first.</strong> Before pitching, they run real buyer questions through several AI engines and show who gets cited.</li><li><strong>They name specific pages.</strong> Their plan says which of your pages they would rebuild and which new pages they would create, and why.</li><li><strong>They explain crawl access.</strong> They can tell you which AI crawlers, such as OAI-SearchBot, PerplexityBot and Google-Extended, your robots.txt allows today, and what they recommend.</li><li><strong>They treat structure seriously.</strong> Schema, a clean sitemap, internal links and an <code>llms.txt</code> file are part of the plan, not an afterthought.</li><li><strong>They write for passages.</strong> They talk about direct answers, question headings, comparison tables and sourced facts, because that is what AI engines quote.</li><li><strong>They build authority off your site.</strong> They have a plan for consistent brand descriptions and earned mentions, not just on-page edits.</li><li><strong>They keep SEO healthy.</strong> They protect existing rankings, because many AI answers draw on pages that already rank.</li><li><strong>They measure what you care about.</strong> Citations per engine, AI referral sessions and leads by page, each one something you can verify.</li><li><strong>They are honest about time.</strong> They expect early wins on specific questions within months and slower progress on broad ones.</li><li><strong>They make no placement promises.</strong> Nobody controls AI answers. An agency that says otherwise is selling certainty it does not have.</li></ol>"},
        {"heading": "Red flags that should end the conversation",
         "body_html": "<ul><li><strong>Promised positions:</strong> \"We'll get you to #1 in ChatGPT\" is not something anyone can deliver.</li><li><strong>Volume over quality:</strong> plans to publish hundreds of thin, near-identical pages. Google's spam policies specifically target scaled content that adds little value, and AI engines rarely quote it.</li><li><strong>Secret methods:</strong> if they cannot explain what they will change on your site, you cannot judge it.</li><li><strong>No baseline:</strong> without a before-and-after test of the same questions, improvement is impossible to prove.</li><li><strong>Blocking AI crawlers by default:</strong> some security setups block the very bots that power AI search. An agency should check this in week one.</li></ul>"},
        {"heading": "How to compare GEO proposals side by side",
         "body_html": "<p>Put every proposal on the same scorecard so the comparison is fair:</p><table><tr><th>Question</th><th>What a strong answer looks like</th></tr><tr><td>What does AI say about us now?</td><td>Screenshots or a table of answers for your real buyer questions</td></tr><tr><td>What changes first?</td><td>A named list of pages, fixes and new topics, with reasons</td></tr><tr><td>How is progress measured?</td><td>Citations per engine, AI referral visits, leads by page, Search Console data</td></tr><tr><td>What does month one deliver?</td><td>Audit, crawl and schema fixes, tracking set up</td></tr><tr><td>Who does the work?</td><td>Named people, with how often you meet them</td></tr><tr><td>What do you need from us?</td><td>A clear, small list: access, approvals, subject-matter input</td></tr></table><p>Price matters, but compare it only after you know what each agency will actually do.</p>"},
        {"heading": "Questions to ask on the first call",
         "body_html": "<ul><li>Which three questions would you most want us to be cited for, and why?</li><li>What would you change on our homepage and our best service page?</li><li>How do you decide which AI engines to prioritize for our buyers?</li><li>Can you show a past report, with client details removed?</li><li>How do you handle content approvals and our brand voice?</li><li>What happens if a change hurts our existing rankings?</li></ul><p>Listen for specifics about your site. Generic answers usually mean a generic service.</p>"},
        {"heading": "What a good GEO agency will ask you",
         "body_html": "<p>Choosing well works both ways. The agencies worth hiring will want to understand your business before they promise anything, so expect questions like these on the first call:</p><ul><li><strong>Who are your best customers,</strong> and what do they ask before they buy? The questions buyers ask AI assistants are the raw material of a GEO plan.</li><li><strong>Which competitors do you lose to,</strong> and where do they show up that you do not? Competitors already cited by AI engines show what the engines currently trust.</li><li><strong>What proof do you have?</strong> Case studies, reviews, certifications and real numbers are what make a page worth quoting.</li><li><strong>Who can approve changes,</strong> and how fast? GEO depends on editing real pages, so slow approvals slow results.</li><li><strong>How do leads reach you today?</strong> If the site has no clear next step, extra visibility will not turn into revenue.</li></ul><p>If an agency skips these and goes straight to a price, it is probably selling a package rather than a plan built for you. The best proposals read like they could only have been written for your business.</p>"},
        {"heading": "Local versus remote GEO agencies",
         "body_html": "<p>GEO is mostly remote work, so you can hire anywhere. A local agency still helps when your buyers search locally, for example \"best accountant in Orange County\", because it will understand the local competitors, directories and review sites that AI engines lean on for those answers. For national or online businesses, choose on expertise and measurement rather than location.</p>"},
    ],
    "faqs": [
        {"q": "How do I choose a GEO agency?", "a": "Ask each agency to show what AI engines say about your brand today, name the specific pages and fixes they would start with, and explain how they measure citations, AI-referred visits and leads. Compare proposals on the same scorecard and avoid anyone promising fixed placement."},
        {"q": "What is a red flag when hiring a GEO agency?", "a": "Promises of guaranteed positions in ChatGPT or other engines, plans to mass-produce thin pages, and methods they will not explain. Each of these suggests the agency is selling certainty rather than real improvements you can verify."},
        {"q": "Should a GEO agency also do SEO?", "a": "Yes. Many AI answers draw on pages that already rank in search, so keeping technical SEO, content quality and links healthy supports GEO. An agency that ignores SEO can undo existing results."},
        {"q": "How much proof should I expect before signing?", "a": "At minimum, a live baseline of how AI engines answer your buyers' questions, a page-level plan, and an example report. A capable agency can produce the baseline quickly because it is the first thing they would do anyway."},
        {"q": "Is a local GEO agency better?", "a": "Only if your buyers search locally. Local knowledge helps with regional competitors, directories and reviews that feed local AI answers. Otherwise, choose on expertise, transparency and measurement."},
        {"q": "How long should a first GEO contract be?", "a": "Three months is a sensible first term: long enough to audit, fix, publish and re-test, and short enough to judge whether the agency is delivering before you commit further."},
    ],
    "internal_links": [L("what a generative engine optimization agency does", "generative-engine-optimization-agency"), L("GEO SEO best practices", "geo-seo-best-practices"), CORE["process"], CORE["results"], CORE["audit"]],
    "sources": [SRC["spam"], SRC["aif"], SRC["oai"], SRC["gcrawl"]],
})

# ---------------------------------------------------------------- 3
PAGES.append({
    "query": "geo vs seo",
    "slug": "geo-vs-seo",
    "eyebrow": "GEO vs SEO",
    "primary_keyword": "GEO vs SEO",
    "secondary_keywords": ["generative engine optimization vs SEO", "difference between GEO and SEO", "does GEO replace SEO", "AI search optimization"],
    "search_intent": "informational",
    "seo": {
        "title": "GEO vs SEO: Key Differences and How They Work Together",
        "meta_description": "GEO vs SEO explained: how ranking differs from being cited by AI, what changes in content and measurement, and why you need both in 2026.",
    },
    "h1": "GEO vs SEO: What's the Difference, and Do You Need Both?",
    "answer": "In GEO vs SEO, the difference is the goal. SEO (search engine optimization) helps your pages rank in search results. GEO (generative engine optimization) helps AI assistants like ChatGPT, Perplexity and Google AI Overviews choose your brand and quote your pages inside their answers. They share foundations, so most businesses need both working together.",
    "key_takeaways": [
        "SEO earns a ranked link; GEO earns a mention or citation inside an AI answer.",
        "Both depend on crawlable, indexed, helpful pages, so GEO builds on SEO.",
        "GEO puts more weight on direct answers, sourced facts and brand mentions across the web.",
        "Measurement differs: rankings and clicks for SEO, citations and AI referrals for GEO.",
        "GEO does not replace SEO; dropping SEO usually weakens GEO too.",
    ],
    "sections": [
        {"heading": "GEO vs SEO in one sentence each",
         "body_html": "<p><strong>SEO</strong> is the work of helping search engines crawl, understand and rank your pages so people click through from the results page.</p><p><strong>GEO</strong> is the work of helping generative AI systems find, trust and quote your content, so your brand is named inside the answer itself.</p><p>The shift matters because the answer is increasingly the destination. When an AI assistant summarizes the options and recommends two or three, the brands it names get the attention, and the rest of page one gets much less.</p>"},
        {"heading": "Side-by-side comparison",
         "body_html": "<table><tr><th></th><th>SEO</th><th>GEO</th></tr><tr><td>Where you appear</td><td>A ranked list of links</td><td>Inside an AI-written answer, as a mention or a cited source</td></tr><tr><td>What gets optimized</td><td>Pages for keywords</td><td>Passages for questions, and your brand as an entity</td></tr><tr><td>Strongest signals</td><td>Relevance, links, technical health, user satisfaction</td><td>Clear answers, specific and sourced facts, structure, consistent brand mentions, AI crawler access</td></tr><tr><td>Typical query</td><td>Short keywords, \"near me\" searches</td><td>Longer questions, comparisons and \"which should I choose\" prompts</td></tr><tr><td>How you measure it</td><td>Rankings, impressions, clicks</td><td>Mentions and citations per engine, AI referral visits, leads</td></tr><tr><td>Main tools</td><td>Google Search Console, rank trackers</td><td>Prompt testing across engines, analytics grouped by AI referrer, Search Console</td></tr></table>"},
        {"heading": "What GEO and SEO have in common",
         "body_html": "<p>Google says plainly that the same best practices apply to its AI features as to Search, and that there are no special requirements beyond being indexed and eligible to show in Search. In practice, the foundations overlap almost completely:</p><ul><li>Pages must be crawlable and indexed.</li><li>Content must be genuinely helpful and written for people.</li><li>Your site needs a clear structure and good internal links.</li><li>Trust signals, such as who is behind the content and why they know, matter in both.</li></ul><p>That is why a GEO program starts by checking SEO health. If search engines cannot see a page, AI systems that rely on search indexes usually cannot cite it either.</p>"},
        {"heading": "Where GEO goes further than SEO",
         "body_html": "<h3>Answers first</h3><p>AI engines pull short passages. Pages that open with a direct, 40–60 word answer to the exact question, then expand, are easier to quote than pages that build up slowly.</p><h3>Facts that can be checked</h3><p>The original GEO research from Princeton and partners found that adding citations, quotations and statistics raised a source's visibility in generative answers by up to 40% in their tests, while keyword stuffing did not help. Specific, sourced facts are more quotable than general claims.</p><h3>Your brand as an entity</h3><p>AI answers recommend brands, not just pages. Consistent descriptions of who you are and what you specialize in, across your site, profiles, directories and earned mentions, make it easier for engines to connect your name with a topic.</p><h3>Access for AI crawlers</h3><p>Search crawlers are not the only bots that matter now. OpenAI's OAI-SearchBot and PerplexityBot, for example, need to reach your pages for those products to cite them. Some security settings block them by accident.</p>"},
        {"heading": "Does GEO replace SEO?",
         "body_html": "<p>No. Search still sends most website traffic, and AI answers often draw on pages that already rank. Dropping SEO to focus on GEO usually weakens both, because the pages AI engines would cite lose the authority and visibility that got them noticed.</p><p>The better question is how to split effort. A sensible starting point:</p><ul><li>Keep technical SEO and indexing healthy across the whole site.</li><li>Rebuild your most important service and comparison pages so they answer questions directly.</li><li>Publish new pages for the specific, high-intent questions buyers ask AI assistants.</li><li>Track AI referrals and leads alongside search clicks, so you can see which effort is paying off.</li></ul>"},
        {"heading": "A simple plan to run GEO and SEO together",
         "body_html": "<p>You do not need two separate teams or two separate strategies. One plan, run in this order, covers both:</p><ol><li><strong>Fix the foundations.</strong> Make sure every important page is crawlable, indexed, fast and linked from other pages. Check that robots.txt allows both search crawlers and AI crawlers you want to be cited by.</li><li><strong>Pick the questions that matter.</strong> List the 30–50 questions buyers ask before choosing a provider like you, from early research to final comparison.</li><li><strong>Match each question to a page.</strong> Improve an existing page where one fits, or publish a new one where none does. Each page should answer its question in the opening lines.</li><li><strong>Add structure.</strong> Use FAQ, Article, Organization and Service schema, a clear sitemap and an <code>llms.txt</code> file that lists your best pages.</li><li><strong>Earn outside signals.</strong> Reviews, directory listings, partner pages and press mentions help search rankings and give AI engines more reasons to name you.</li><li><strong>Measure both.</strong> Review Search Console and AI citations together every month, and move effort toward whatever produces leads.</li></ol><p>Run this loop for a quarter and you will know which questions and pages bring in buyers, whether they arrive from a search result or an AI answer.</p>"},
        {"heading": "How to measure GEO vs SEO",
         "body_html": "<p>Use one dashboard with both views:</p><ul><li><strong>SEO:</strong> impressions, clicks, average position and indexed pages from Google Search Console.</li><li><strong>GEO:</strong> a fixed list of buyer questions tested monthly in each AI engine, recording mentions and citations; plus sessions from AI referrers in Google Analytics.</li><li><strong>Business results:</strong> leads by landing page and by source, so you can see whether AI-referred visitors convert differently from search visitors.</li></ul><p>Many businesses find AI-referred visits are fewer but further along in their decision. Your own data is the only way to know.</p>"},
    ],
    "faqs": [
        {"q": "What is the main difference in GEO vs SEO?", "a": "SEO aims to rank your pages in search results, while GEO aims to get your brand named and your pages cited inside AI-generated answers. The foundations are shared, but GEO puts more weight on direct answers, sourced facts and brand mentions."},
        {"q": "Does GEO replace SEO?", "a": "No. Search still drives most traffic, and AI answers often rely on pages that already rank. The strongest approach runs both, with GEO building on a healthy SEO base."},
        {"q": "Is GEO the same as AEO?", "a": "They overlap. Answer engine optimization (AEO) usually refers to winning direct answers such as featured snippets and voice results, while GEO focuses on generative AI assistants that write answers and cite sources. Most tactics serve both."},
        {"q": "Which should a new website focus on first, GEO or SEO?", "a": "Start with SEO foundations: crawlable, indexed, helpful pages. Then structure your key pages for GEO from the beginning, with direct answers, FAQs and schema, so they are ready to be cited as they gain visibility."},
        {"q": "How do I know if GEO is working?", "a": "Test the same buyer questions in ChatGPT, Perplexity, Gemini and Google AI Overviews every month and record mentions and citations. Also track visits from AI referrers and the leads they produce in your analytics."},
        {"q": "Do GEO and SEO use different content?", "a": "Mostly the same content, written with more care. GEO-friendly pages answer the question in the first lines, use question headings, include specific facts with sources, and make the brand's specialty unmistakable."},
    ],
    "internal_links": [L("what is generative engine optimization", "what-is-generative-engine-optimization-and-how-does-it-work"), L("AEO vs GEO explained", "answer-engine-optimization-vs-generative-engine-optimization"), L("GEO SEO best practices", "geo-seo-best-practices"), CORE["services"], CORE["audit"]],
    "sources": [SRC["aif"], SRC["geo"], SRC["helpful"], SRC["oai"]],
})

if __name__ == "__main__":
    for p in PAGES:
        save(p)
