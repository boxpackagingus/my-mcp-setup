"""Drafts for pages 4-7. Run: python content/build/batch2.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch1 import CORE, SRC, L, save  # noqa: E402

PAGES = []

# ---------------------------------------------------------------- 4
PAGES.append({
    "query": "what is generative engine optimization and how does it work",
    "slug": "what-is-generative-engine-optimization-and-how-does-it-work",
    "eyebrow": "GEO explained",
    "primary_keyword": "generative engine optimization",
    "secondary_keywords": ["what is GEO", "how GEO works", "GEO meaning", "AI search optimization"],
    "search_intent": "informational",
    "seo": {
        "title": "What Is Generative Engine Optimization (GEO)?",
        "meta_description": "What generative engine optimization is, how AI engines choose which brands and pages to cite, and the steps that make your business easier to recommend.",
    },
    "h1": "What Is Generative Engine Optimization, and How Does It Work?",
    "answer": "Generative engine optimization (GEO) is the practice of shaping your website and brand so AI systems such as ChatGPT, Gemini, Perplexity, Claude and Google AI Overviews can find your content, trust it and quote it in their answers. It works by improving crawl access, structure, quotable facts and the outside signals that tell AI who you are.",
    "key_takeaways": [
        "GEO aims for mentions and citations inside AI answers, not just a ranked link.",
        "AI engines that search the web pick sources much like search engines, then summarize them.",
        "Direct answers, sourced facts, clear structure and brand consistency make content quotable.",
        "The term comes from a 2023 research paper that tested which content changes raise AI visibility.",
        "GEO depends on SEO foundations: if a page is not crawlable and indexed, it is rarely cited.",
    ],
    "sections": [
        {"heading": "Generative engine optimization in plain terms",
         "body_html": "<p>A generative engine is any AI system that writes an answer instead of returning a list of links. ChatGPT with search, Perplexity, Google's AI Overviews and AI Mode, Gemini, Claude and Microsoft Copilot all do this. They read sources, combine what they find, and present a single response, often with a few links.</p><p>Generative engine optimization is the work of making your content one of those sources, and your brand one of the names in the answer. It is to AI answers what SEO is to search results.</p><p>The phrase was introduced in a 2023 research paper by researchers from Princeton, Georgia Tech, the Allen Institute for AI and IIT Delhi, later published at the KDD 2024 conference. They built a benchmark of real queries and measured how different content changes affected a source's visibility inside generated answers.</p>"},
        {"heading": "How generative engines choose what to cite",
         "body_html": "<p>Each product works differently, but engines that answer with live web results generally follow the same pattern:</p><ol><li><strong>Understand the question.</strong> The engine works out what the person is really asking, often splitting it into several sub-questions.</li><li><strong>Retrieve sources.</strong> It searches an index of the web, such as its own crawl or a search partner, for pages likely to answer each part.</li><li><strong>Select passages.</strong> It picks the passages that answer most clearly and seem most trustworthy.</li><li><strong>Write the answer.</strong> It summarizes those passages, names relevant brands and often links to the sources it used.</li></ol><p>Two consequences follow. First, a page must be reachable and indexed before it can be selected at all. Second, the page competes passage by passage: a clear paragraph that answers the exact question beats a long page that answers it somewhere in the middle.</p><p>Models without live search behave differently. They answer from what they learned in training, which changes slowly. GEO helps there too, through the brand mentions and descriptions that end up in future training data, but progress is slower.</p>"},
        {"heading": "What the research found",
         "body_html": "<p>The GEO paper tested several ways of rewriting content and measured the effect on visibility in generated answers. Its headline result was that the best methods improved a source's visibility by up to 40% in their benchmark. The methods that helped most added substance:</p><ul><li><strong>Citing sources</strong> for claims.</li><li><strong>Adding quotations</strong> from relevant authorities.</li><li><strong>Adding statistics</strong> in place of vague statements.</li><li>Writing more fluently and clearly.</li></ul><p>Keyword stuffing, the old SEO habit of repeating phrases, did not help. The lesson for businesses is simple: AI engines prefer content that is specific, checkable and easy to lift into an answer.</p>"},
        {"heading": "The building blocks of a GEO strategy",
         "body_html": "<h3>1. Access</h3><p>Allow the crawlers that power AI search. OpenAI documents OAI-SearchBot for ChatGPT search results and Perplexity documents PerplexityBot for its index. Check robots.txt and any firewall or bot-protection settings.</p><h3>2. Structure</h3><p>Use descriptive headings that match real questions, short paragraphs, lists and tables. Add structured data such as Organization, Service, Article and FAQPage, and publish an <code>llms.txt</code> file that points AI tools to your most useful pages.</p><h3>3. Answers</h3><p>Open each page with a direct answer of about 40–60 words. Then give the detail: steps, comparisons, examples and trade-offs.</p><h3>4. Evidence</h3><p>Back claims with sources, data and named examples. Say who the advice is for and who it is not for.</p><h3>5. Entity signals</h3><p>Describe your business the same way everywhere: your site, social profiles, directories, partner pages and press. Engines recommend brands they can confidently describe.</p><h3>6. Measurement</h3><p>Track a fixed set of buyer questions in each engine every month, plus AI-referred visits and the leads they produce.</p>"},
        {"heading": "GEO in practice: an example",
         "body_html": "<p>Imagine a luxury tent rental company in California. A buyer asks an AI assistant: <em>\"Who rents luxury tents for weddings in Southern California, and what do they cost?\"</em></p><p>A GEO-ready site would have a page that opens with a direct answer about what the company offers, where it operates and how pricing works; a table comparing tent sizes and typical uses; FAQs about permits, setup time and weather; and consistent listings on wedding directories and review sites. Each piece gives the engine something concrete to quote and a reason to trust it.</p><p>A site with a single gallery page and a contact form gives the engine almost nothing to work with, so it cites someone else.</p>"},
        {"heading": "How long generative engine optimization takes",
         "body_html": "<p>Plan in months, not days:</p><ul><li><strong>First weeks:</strong> technical fixes, structured data, tracking, and a baseline of today's AI answers.</li><li><strong>Months 1–3:</strong> new and rebuilt pages get indexed; first citations usually appear for specific, long-tail questions.</li><li><strong>Months 3–6:</strong> clear patterns emerge in which topics bring citations and leads, so you can double down.</li></ul><p>Engines that search the web live can pick up a strong page soon after it is indexed. Answers that rely on training data move more slowly. Nobody can control exactly what an AI model says on a given day, so judge progress on trends across many questions, not a single answer.</p>"},
        {"heading": "Where to start this week",
         "body_html": "<ol><li>Write down ten questions your best customers asked before they bought from you.</li><li>Ask each one in ChatGPT, Perplexity and Google, and note who is mentioned.</li><li>Check that your robots.txt does not block AI crawlers you want to be cited by.</li><li>Pick the question you most want to own and make sure one page answers it in the first two sentences.</li><li>Set up a channel in Google Analytics for AI referrers so you can see the results.</li></ol>"},
    ],
    "faqs": [
        {"q": "What is generative engine optimization in simple words?", "a": "It is the work of making your website and brand easy for AI assistants to find, trust and quote. When someone asks ChatGPT, Perplexity or Google's AI a question about your field, GEO aims to have your business named in the answer."},
        {"q": "How does generative engine optimization work?", "a": "Engines that answer from the web retrieve pages, select the clearest and most trustworthy passages, and summarize them. GEO improves each step: crawl access so pages can be retrieved, structure and direct answers so passages are easy to select, and evidence and brand signals so they are trusted."},
        {"q": "Who coined the term GEO?", "a": "The term comes from a 2023 research paper, 'GEO: Generative Engine Optimization', by researchers from Princeton, Georgia Tech, the Allen Institute for AI and IIT Delhi, published at KDD 2024."},
        {"q": "Is GEO just SEO with a new name?", "a": "No, but it builds on SEO. Both need crawlable, indexed, helpful pages. GEO adds a focus on quotable passages, sourced facts, brand consistency across the web and access for AI crawlers, and it is measured by citations rather than rankings."},
        {"q": "Which AI engines does GEO target?", "a": "The main ones are ChatGPT, Google AI Overviews and AI Mode, Gemini, Perplexity, Claude and Microsoft Copilot. Which matter most depends on where your buyers do their research."},
        {"q": "Can I do generative engine optimization myself?", "a": "Yes, the basics are approachable: allow AI crawlers, answer questions directly, add FAQs and schema, cite sources and keep your brand description consistent. An agency helps when you need scale, technical depth or ongoing measurement."},
    ],
    "internal_links": [L("GEO vs SEO compared", "geo-vs-seo"), L("how to rank in ChatGPT", "how-to-rank-in-chatgpt"), L("llms.txt best practices", "best-practices-for-llms-txt"), CORE["process"], CORE["audit"]],
    "sources": [SRC["geo"], SRC["aif"], SRC["oai"], SRC["pplx"], SRC["llms"]],
})

# ---------------------------------------------------------------- 5
PAGES.append({
    "query": "how to rank in chatgpt",
    "slug": "how-to-rank-in-chatgpt",
    "eyebrow": "ChatGPT visibility",
    "primary_keyword": "rank in ChatGPT",
    "secondary_keywords": ["ChatGPT SEO", "get recommended by ChatGPT", "ChatGPT search", "OAI-SearchBot"],
    "search_intent": "informational",
    "seo": {
        "title": "How to Rank in ChatGPT: 9 Steps to Get Recommended",
        "meta_description": "How to rank in ChatGPT answers: let OAI-SearchBot crawl you, answer questions directly, earn brand mentions, and track ChatGPT referrals and leads.",
    },
    "h1": "How to Rank in ChatGPT: 9 Steps to Get Your Brand Recommended",
    "answer": "To rank in ChatGPT, make sure OpenAI's OAI-SearchBot can crawl your site, publish pages that answer buyers' exact questions in the first lines, back claims with specific facts and sources, and earn consistent brand mentions on sites ChatGPT trusts. Then track ChatGPT referrals and leads to see which pages it actually recommends.",
    "key_takeaways": [
        "ChatGPT has no ranked list; it names a few brands and cites sources when it searches the web.",
        "OAI-SearchBot must be allowed to crawl your pages for them to appear in ChatGPT search results.",
        "Pages that answer the exact question early, with specifics, are the easiest to cite.",
        "Mentions of your brand on other trusted sites strongly shape what ChatGPT says about you.",
        "Visits from chatgpt.com show up in analytics, so you can measure what works.",
    ],
    "sections": [
        {"heading": "What it means to rank in ChatGPT",
         "body_html": "<p>ChatGPT does not show ten blue links. When it answers a question that needs current information, it can search the web, read sources and write a response, often with links to the pages it used. For questions it answers from training alone, it draws on what it learned about brands and topics.</p><p>So \"ranking\" in ChatGPT really means three things:</p><ul><li><strong>Being mentioned</strong> by name when someone asks for options or recommendations.</li><li><strong>Being described correctly:</strong> your specialty, location and strengths.</li><li><strong>Being cited</strong> with a link when ChatGPT searches the web.</li></ul><p>You influence all three with the same steps.</p>"},
        {"heading": "Step 1–3: Let ChatGPT find and read your site",
         "body_html": "<h3>1. Allow OAI-SearchBot</h3><p>OpenAI documents several crawlers. OAI-SearchBot is used to surface websites in ChatGPT's search features; GPTBot is used for training; ChatGPT-User fetches pages when a user asks. If your robots.txt or firewall blocks OAI-SearchBot, your pages cannot appear in ChatGPT search results. You can allow search while still blocking training if you prefer.</p><h3>2. Make sure pages are indexable and fast</h3><p>Pages that load slowly, depend entirely on JavaScript, or sit behind logins are hard for any crawler to read. Keep key content in the HTML, use clean URLs, and include every important page in your sitemap.</p><h3>3. Tell crawlers about new pages quickly</h3><p>Submit your sitemap in search tools and use IndexNow, which notifies participating search engines such as Bing the moment a page is published or updated.</p>"},
        {"heading": "Step 4–6: Write pages ChatGPT wants to quote",
         "body_html": "<h3>4. Answer the exact question first</h3><p>Start each page with a 40–60 word answer that uses the words buyers use. If someone asks \"what does a GEO agency cost\", your page should say it plainly in the first lines, then explain.</p><h3>5. Be specific and cite sources</h3><p>Research on generative engines found that adding citations, quotations and statistics made sources noticeably more visible in AI answers, while keyword stuffing did not help. Replace general claims with numbers, named methods, examples and references.</p><h3>6. Structure for passages</h3><p>Use question-style headings, short paragraphs, comparison tables and FAQs. Each section should make sense if quoted on its own, because that is how it will be used.</p>"},
        {"heading": "Step 7–8: Build the reputation ChatGPT relies on",
         "body_html": "<h3>7. Earn mentions on trusted sites</h3><p>When ChatGPT recommends providers, it leans on what the wider web says: reviews, \"best of\" lists, directories, industry publications, Reddit and community discussions, and partner pages. A brand that appears consistently in those places is far easier to recommend than one that only describes itself.</p><p>Practical ways to earn mentions: contribute expert quotes to industry articles, get listed in the directories your buyers use, collect detailed reviews, publish original data others want to reference, and keep partner and supplier pages up to date.</p><h3>8. Describe your brand the same way everywhere</h3><p>Use one clear description of what you do, who you serve and where, on your homepage, About page, social profiles, directory listings and Organization schema. Inconsistency makes an AI engine less confident about what you are best at.</p>"},
        {"heading": "Step 9: Measure what ChatGPT sends you",
         "body_html": "<p>Visitors who click links in ChatGPT usually arrive with <code>chatgpt.com</code> as the referrer, and ChatGPT often adds <code>utm_source=chatgpt.com</code> to links. In Google Analytics, group these visits into an \"AI search\" channel alongside perplexity.ai, gemini.google.com, copilot.microsoft.com and claude.ai.</p><p>Then track:</p><ul><li>Which landing pages ChatGPT sends visitors to.</li><li>How those visitors convert compared with search visitors.</li><li>A fixed list of 20–50 buyer questions you test in ChatGPT each month, recording whether you are mentioned and cited.</li></ul><p>People who read a recommendation and later search your brand name show up as branded search instead, so watch branded search growth too.</p>"},
        {"heading": "What a page ChatGPT recommends looks like",
         "body_html": "<p>When ChatGPT recommends a provider, the pages it cites tend to share the same building blocks. Use this as a template for your most important service or comparison pages:</p><ul><li><strong>A one-line description</strong> of who you are, what you do and who you serve, in the first paragraph.</li><li><strong>A direct answer</strong> to the question the page targets, in plain language.</li><li><strong>Specifics:</strong> service areas, price ranges or how pricing works, timelines, and what is included.</li><li><strong>Proof:</strong> named clients where you have permission, case results with numbers, reviews and certifications.</li><li><strong>Comparisons:</strong> how your approach differs from alternatives, including when you are not the right fit.</li><li><strong>FAQs</strong> that mirror real follow-up questions.</li><li><strong>A clear next step,</strong> such as a short form, so the visitor ChatGPT sends you can act right away.</li></ul><p>Pages built this way serve people and AI engines equally well, which is exactly the point.</p>"},
        {"heading": "Mistakes that keep brands out of ChatGPT answers",
         "body_html": "<ul><li><strong>Blocking AI crawlers by accident</strong> through a security plugin or CDN setting.</li><li><strong>Hiding the answer</strong> under long introductions, sliders or tabs that need clicks.</li><li><strong>Thin, repetitive pages</strong> produced in bulk. They rarely get cited and can hurt search visibility.</li><li><strong>No proof:</strong> claims without examples, data or reviews give ChatGPT little reason to trust you.</li><li><strong>Inconsistent business details</strong> across the web.</li><li><strong>Checking once and giving up.</strong> AI answers vary between sessions; track trends over many questions.</li></ul>"},
        {"heading": "A 30-day plan to rank in ChatGPT",
         "body_html": "<table><tr><th>Week</th><th>Focus</th><th>Output</th></tr><tr><td>1</td><td>Baseline and access</td><td>List of 30 buyer questions tested in ChatGPT; robots.txt and firewall allow OAI-SearchBot</td></tr><tr><td>2</td><td>Fix key pages</td><td>Homepage and top service pages open with direct answers, FAQs and schema</td></tr><tr><td>3</td><td>New answer pages</td><td>Pages for the five highest-intent questions you are not mentioned for</td></tr><tr><td>4</td><td>Reputation and tracking</td><td>Directory and review profiles updated; AI search channel live in analytics</td></tr></table><p>Repeat the question test at the end of the month and keep going on whatever moved.</p>"},
    ],
    "faqs": [
        {"q": "How do I rank in ChatGPT?", "a": "Allow OpenAI's OAI-SearchBot to crawl your site, publish pages that answer buyers' exact questions in the first lines with specific, sourced facts, keep your brand description consistent, and earn mentions on trusted sites. Then track ChatGPT referrals to see what works."},
        {"q": "Can I pay to rank in ChatGPT?", "a": "ChatGPT's organic answers are not something you can buy a position in. You improve your chances by being the clearest, best-supported source and the most consistently described brand for the questions your buyers ask."},
        {"q": "What is OAI-SearchBot?", "a": "It is OpenAI's crawler for ChatGPT's search features. Allowing it in robots.txt lets your pages be shown and linked in ChatGPT search results. It is separate from GPTBot, which OpenAI uses for training."},
        {"q": "How long does it take to appear in ChatGPT answers?", "a": "When ChatGPT searches the web, a well-structured page can be cited soon after it is crawled. Mentions that rely on what the model learned in training change more slowly, often over months as your brand appears on more trusted sites."},
        {"q": "How can I see if ChatGPT sends me traffic?", "a": "Look for visits with chatgpt.com as the source or referrer in Google Analytics, often tagged utm_source=chatgpt.com. Group them with other AI referrers into one channel and compare their conversion rate with search traffic."},
        {"q": "Does ChatGPT use Google rankings?", "a": "Not directly. ChatGPT search uses its own crawler and third-party search providers. In practice, pages that are well structured, trustworthy and widely referenced tend to do well in both."},
    ],
    "internal_links": [L("what generative engine optimization is", "what-is-generative-engine-optimization-and-how-does-it-work"), L("Perplexity SEO guide", "perplexity-seo"), L("how to show up in Google AI Overviews", "how-to-show-up-in-google-ai-overviews"), CORE["services"], CORE["audit"]],
    "sources": [SRC["oai"], SRC["geo"], SRC["indexnow"], SRC["robots"]],
})

# ---------------------------------------------------------------- 6
PAGES.append({
    "query": "how to show up in google ai overviews",
    "slug": "how-to-show-up-in-google-ai-overviews",
    "eyebrow": "Google AI Overviews",
    "primary_keyword": "Google AI Overviews",
    "secondary_keywords": ["AI Overviews SEO", "get cited in AI Overviews", "AI Mode", "Google AI search"],
    "search_intent": "informational",
    "seo": {
        "title": "How to Show Up in Google AI Overviews (2026 Guide)",
        "meta_description": "How to show up in Google AI Overviews: what Google says it needs, how sources are chosen, and the page changes that make your content easier to cite.",
    },
    "h1": "How to Show Up in Google AI Overviews",
    "answer": "To show up in Google AI Overviews, your page must first be indexed and eligible to appear in Google Search with a snippet. Google says no special markup is required. After that, pages that answer the question directly, cover related follow-up questions, show clear expertise and use clean structure are the ones most often linked as sources.",
    "key_takeaways": [
        "Google states there are no extra technical requirements for AI Overviews beyond normal Search eligibility.",
        "A page must be indexed and allowed to show a snippet to be used as a source.",
        "AI Overviews often answer several sub-questions, so pages that cover follow-ups get more chances.",
        "Helpful, people-first content and visible expertise matter as much as in regular Search.",
        "Clicks from AI Overviews are counted in Search Console's web search totals.",
    ],
    "sections": [
        {"heading": "What Google AI Overviews are",
         "body_html": "<p>AI Overviews are AI-generated summaries that appear at the top of some Google results. They answer the query in a few sentences or bullet points and show links to the web pages they drew on. AI Mode goes further, letting people ask follow-up questions in a conversational view.</p><p>For businesses, being one of the linked sources is valuable: the link sits above the traditional results, and the summary often describes your offer before the searcher reaches any blue link.</p>"},
        {"heading": "What Google says you need",
         "body_html": "<p>Google's documentation for site owners is clear on the basics:</p><ul><li>There are <strong>no additional requirements</strong> to appear in AI Overviews or AI Mode, and no special schema or markup to add.</li><li>A page must be <strong>indexed and eligible to be shown in Google Search with a snippet</strong>.</li><li>The same <strong>SEO best practices</strong> apply: crawlable pages, internal links, good page experience, text content, and structured data that matches visible content.</li></ul><p>Google also notes that AI features may use a technique it calls \"query fan-out\", issuing several related searches across subtopics to build a response. That means a single overview can draw on pages answering different parts of the question.</p><p>Controls work through normal snippet settings. If you set <code>nosnippet</code> or a very short <code>max-snippet</code>, your content is less likely to be used.</p>"},
        {"heading": "How to make your pages easier to cite",
         "body_html": "<h3>Answer the main question in the first lines</h3><p>Put a direct, complete answer near the top. AI Overviews summarize, so the clearest statement of the answer is the most useful passage on the page.</p><h3>Cover the follow-up questions</h3><p>Because of query fan-out, the overview for \"how much does a GEO agency cost\" might also look for what affects price, what is included and how long it takes. A page with sections for each of those has more chances to be linked.</p><h3>Use descriptive headings</h3><p>Headings that read like the questions people ask help both readers and systems find the right passage.</p><h3>Add tables and lists where they fit</h3><p>Comparisons, steps and criteria are easier to summarize when they are already organized.</p><h3>Show who is behind the content</h3><p>Google's guidance on helpful content asks whether the content shows first-hand expertise and whether it is clear who created it. Author details, real examples and an accurate About page support that.</p>"},
        {"heading": "Technical checklist for AI Overviews",
         "body_html": "<table><tr><th>Check</th><th>Why it matters</th></tr><tr><td>Page is indexed (URL Inspection in Search Console)</td><td>Unindexed pages cannot be sources</td></tr><tr><td>No <code>nosnippet</code> or restrictive <code>max-snippet</code></td><td>Snippet controls also limit AI features</td></tr><tr><td>Important content is in the HTML text</td><td>Content hidden in images or late-loading scripts is harder to use</td></tr><tr><td>Internal links point to the page</td><td>Helps Google discover and understand it</td></tr><tr><td>Structured data matches the visible page</td><td>Mismatched markup can be ignored or penalized</td></tr><tr><td>Page loads fast on mobile</td><td>Page experience is part of overall quality</td></tr></table><p>Note that <code>Google-Extended</code> in robots.txt controls whether content is used for Gemini training and grounding; Google says it does not affect inclusion in Search, including AI Overviews.</p>"},
        {"heading": "Which queries trigger AI Overviews",
         "body_html": "<p>Google shows AI Overviews when it judges they add value beyond regular results. In practice they appear most for informational and comparison questions: \"how does\", \"what is the difference between\", \"is it worth\", \"best way to\". Pure navigational searches, such as a brand name, rarely show them.</p><p>That is good news for service businesses. The research-stage questions buyers ask before choosing a provider are exactly where AI Overviews appear, and where a well-structured guide can put your brand in front of them early.</p>"},
        {"heading": "How to track AI Overviews traffic",
         "body_html": "<p>Google includes clicks and impressions from AI features in the regular web search totals in Search Console, rather than reporting them separately. So:</p><ul><li>Watch impressions and clicks for the pages you have optimized, and for question-style queries.</li><li>Look for pages whose impressions rise while average position looks unusual, which can signal appearances in AI features.</li><li>Search your target questions yourself regularly and record whether your site is linked.</li><li>Track leads by landing page, so you see whether these visitors convert.</li></ul><p>Google has said that clicks from AI Overviews tend to be higher quality, with visitors spending more time on the site. Treat that as a hypothesis to test with your own data.</p>"},
        {"heading": "Writing for AI Mode and follow-up questions",
         "body_html": "<p>AI Mode lets people keep asking questions in a conversation, and AI Overviews already break a query into related searches. Both reward pages that anticipate the next question. A practical way to plan this:</p><ol><li>Write the main question at the top of a document.</li><li>List the five questions a buyer would ask next, such as cost, timing, alternatives, risks and how to get started.</li><li>Give each follow-up its own heading and a two-to-four sentence answer, then the detail.</li><li>Close with FAQs for the smaller questions that do not need a full section.</li></ol><p>This turns one page into several useful passages. Each one can be selected for a different part of an AI answer, and readers who arrive from any of them find the rest of their questions answered on the same page, next to your offer.</p>"},
        {"heading": "Common reasons a page is not cited",
         "body_html": "<ul><li>It is not indexed, or it is a near-duplicate of another page.</li><li>The answer is buried below long introductions.</li><li>It covers the topic broadly but never answers the specific question.</li><li>Other pages offer clearer facts, examples or first-hand experience.</li><li>Snippet controls or rendering problems hide the text.</li></ul><p>Fix the first two before anything else; they are the most common and the easiest to solve.</p>"},
    ],
    "faqs": [
        {"q": "How do I get my website into Google AI Overviews?", "a": "Make sure the page is indexed and can show a snippet in Google Search, then make it the clearest answer to the question: a direct answer near the top, sections for follow-up questions, descriptive headings and visible expertise. Google says no special markup is required."},
        {"q": "Do I need schema markup for AI Overviews?", "a": "Google says no special schema is required for AI Overviews. Structured data is still useful for understanding your content and for rich results, as long as it matches what is visible on the page."},
        {"q": "Does blocking Google-Extended remove me from AI Overviews?", "a": "No. Google says Google-Extended controls use of content for Gemini training and grounding and does not affect inclusion in Google Search, which includes AI Overviews. Snippet controls such as nosnippet do limit AI features."},
        {"q": "Can I see AI Overviews traffic in Search Console?", "a": "Clicks and impressions from AI features are included in the web search totals in Search Console rather than shown separately. Track the pages and question queries you have optimized to see the effect."},
        {"q": "Why does my competitor appear in AI Overviews and not me?", "a": "Usually their page answers the specific question more directly, covers the follow-up questions, or shows clearer expertise. Compare the two pages section by section and close the gaps, starting with the opening answer."},
        {"q": "Are AI Overviews the same as featured snippets?", "a": "No. A featured snippet quotes one page. An AI Overview writes a new summary, often drawing on several pages found through related searches, and links to multiple sources."},
    ],
    "internal_links": [L("how to rank in ChatGPT", "how-to-rank-in-chatgpt"), L("GEO SEO best practices", "geo-seo-best-practices"), L("GEO vs SEO", "geo-vs-seo"), CORE["services"], CORE["audit"]],
    "sources": [SRC["aif"], SRC["helpful"], SRC["gcrawl"], SRC["sd"]],
})

# ---------------------------------------------------------------- 7
PAGES.append({
    "query": "perplexity seo",
    "slug": "perplexity-seo",
    "eyebrow": "Perplexity visibility",
    "primary_keyword": "Perplexity SEO",
    "secondary_keywords": ["get cited by Perplexity", "PerplexityBot", "Perplexity AI search", "answer engine visibility"],
    "search_intent": "informational",
    "seo": {
        "title": "Perplexity SEO: How to Get Cited by Perplexity AI",
        "meta_description": "Perplexity SEO explained: how Perplexity picks and numbers its sources, how to let PerplexityBot crawl you, and how to write pages it cites again and again.",
    },
    "h1": "Perplexity SEO: How to Get Your Site Cited by Perplexity",
    "answer": "Perplexity SEO is the work of getting your pages chosen as numbered sources in Perplexity's answers. Start by allowing PerplexityBot to crawl your site. Then publish fresh, specific pages that answer one question clearly, with facts and sources, so Perplexity's search can find them and its answer can quote them.",
    "key_takeaways": [
        "Perplexity searches the web for almost every answer and shows its sources as numbered citations.",
        "PerplexityBot must be allowed in robots.txt for your pages to be surfaced in Perplexity search.",
        "Clear, specific, recently updated pages are cited most often.",
        "Each citation is a visible, clickable link, which makes Perplexity traffic easy to measure.",
        "The same work also helps ChatGPT, Google AI Overviews and Copilot.",
    ],
    "sections": [
        {"heading": "How Perplexity builds an answer",
         "body_html": "<p>Perplexity is built around citations. For most questions it runs a web search, reads the best-matching pages and writes an answer with numbered references that link to each source. Users can open the sources panel to see every page used.</p><p>That design makes Perplexity unusually transparent. You can see exactly who is cited for a question, which means you can study the winners and do better, and you can measure the visits Perplexity sends you.</p>"},
        {"heading": "Step 1: Let PerplexityBot crawl your site",
         "body_html": "<p>Perplexity documents two user agents. <strong>PerplexityBot</strong> is designed to surface and link websites in Perplexity's search results, and Perplexity says it is not used to crawl content for training AI models. <strong>Perplexity-User</strong> fetches pages when a user's question needs them.</p><p>To be cited, allow PerplexityBot in robots.txt and make sure your firewall, CDN or security plugin does not block it. A simple rule looks like this:</p><blockquote><code>User-agent: PerplexityBot<br>Allow: /</code></blockquote><p>Then check that your important pages are in your sitemap and load quickly with their main content in the HTML.</p>"},
        {"heading": "Step 2: Write pages Perplexity wants to cite",
         "body_html": "<h3>One question, answered early</h3><p>Perplexity tends to cite pages that address the exact question rather than broad overviews. Give each important question its own page or section, and answer it in the first lines.</p><h3>Specific facts with sources</h3><p>Research on generative engines found that adding statistics, quotations and citations made sources more visible in AI-written answers. Name numbers, dates, methods and examples, and link to where they come from.</p><h3>Freshness</h3><p>Perplexity is often used for current questions. Keep key pages updated, show a clear \"last updated\" date, and refresh facts when they change.</p><h3>Clean structure</h3><p>Use headings that match follow-up questions, short paragraphs, lists and comparison tables. Each section should stand on its own if quoted.</p>"},
        {"heading": "Step 3: Build signals beyond your own site",
         "body_html": "<p>Perplexity's search draws on the wider web, so where else your brand appears matters. Useful places to earn mentions include industry publications, directories, review platforms, community discussions such as Reddit, partner pages and podcasts with show notes. Consistent descriptions of what you do help Perplexity connect your brand to the right topics when it summarizes options.</p><p>Original data is especially powerful. A short survey, benchmark or price index that others reference gives Perplexity a unique fact that only your page can supply.</p>"},
        {"heading": "Study who Perplexity cites today",
         "body_html": "<p>Because sources are visible, Perplexity SEO can start with research:</p><ol><li>List 20 questions your buyers ask.</li><li>Ask each in Perplexity and record the cited domains.</li><li>Open the top sources and note what they do well: length, structure, freshness, data, author details.</li><li>Find questions where weak or outdated pages are cited. Those are your easiest wins.</li><li>Publish or improve a page for each, then re-test after it is crawled.</li></ol><p>Repeat monthly. Patterns usually appear quickly, such as Perplexity favoring certain publications or formats in your field.</p><p>Keep a simple spreadsheet with one row per question and columns for the date, the cited domains, whether you were cited, and the position of your citation. After two or three months it shows clearly which pages earn citations and which topics still need work.</p>"},
        {"heading": "Formats that get cited most on Perplexity",
         "body_html": "<p>Some page formats are cited again and again because they match the way people use Perplexity:</p><ul><li><strong>Comparison pages</strong> such as \"X vs Y\", with a table of differences and a clear recommendation for each type of buyer.</li><li><strong>How-to guides</strong> with numbered steps, prerequisites and common mistakes.</li><li><strong>Definitions</strong> that explain a term in the first sentence and then give examples.</li><li><strong>Buying guides</strong> listing selection criteria, price factors and questions to ask.</li><li><strong>Original data</strong> such as surveys, benchmarks or price trackers that no other page can supply.</li></ul><p>Pick the format that best matches each buyer question, rather than forcing every topic into a blog post.</p>"},
        {"heading": "How Perplexity SEO differs from Google SEO",
         "body_html": "<p>Google ranks a list of pages and lets the searcher choose. Perplexity reads several pages and writes one answer, so it rewards different strengths:</p><table><tr><th></th><th>Google SEO</th><th>Perplexity SEO</th></tr><tr><td>Win condition</td><td>A high position in the results</td><td>Being one of the numbered sources</td></tr><tr><td>Best content</td><td>Comprehensive pages that satisfy a keyword</td><td>Clear passages that answer one question precisely</td></tr><tr><td>Freshness</td><td>Matters for some topics</td><td>Matters for many, since users ask current questions</td></tr><tr><td>Measurement</td><td>Rankings and clicks</td><td>Citations per question and perplexity.ai referrals</td></tr></table><p>The foundations still overlap: a crawlable, fast, trustworthy site with helpful content does well in both.</p>"},
        {"heading": "Measure Perplexity traffic",
         "body_html": "<p>Perplexity citations are clickable links, so visits usually arrive with <code>perplexity.ai</code> as the referrer. In Google Analytics, include it in an \"AI search\" channel with chatgpt.com, gemini.google.com, copilot.microsoft.com and claude.ai. Track which landing pages it sends visitors to and whether they submit your forms.</p><p>Visitors from Perplexity are often in research mode and have already read a summary, so a clear next step, such as an audit offer or a short form, matters on every page they land on.</p>"},
        {"heading": "Perplexity SEO checklist",
         "body_html": "<table><tr><th>Area</th><th>Check</th></tr><tr><td>Access</td><td>PerplexityBot allowed in robots.txt and not blocked by firewall or CDN</td></tr><tr><td>Discovery</td><td>Page in sitemap, linked internally, submitted through IndexNow where supported</td></tr><tr><td>Answer</td><td>Direct answer to one question in the opening lines</td></tr><tr><td>Evidence</td><td>Specific facts, data and linked sources</td></tr><tr><td>Freshness</td><td>Visible last-updated date; facts reviewed regularly</td></tr><tr><td>Structure</td><td>Question headings, lists, tables, FAQs</td></tr><tr><td>Reputation</td><td>Brand mentioned consistently on trusted third-party sites</td></tr><tr><td>Measurement</td><td>perplexity.ai referrals and leads tracked by page</td></tr></table>"},
    ],
    "faqs": [
        {"q": "What is Perplexity SEO?", "a": "It is the practice of getting your pages cited as sources in Perplexity's answers. It combines letting PerplexityBot crawl your site, writing specific and up-to-date pages that answer one question clearly, and earning mentions on sites Perplexity's search trusts."},
        {"q": "How do I allow PerplexityBot?", "a": "Add a rule to robots.txt such as 'User-agent: PerplexityBot' followed by 'Allow: /', and check that your firewall, CDN or security plugin does not block it. Perplexity says PerplexityBot is used to surface sites in search results, not to train models."},
        {"q": "Why does Perplexity cite my competitors and not me?", "a": "Their pages usually answer the exact question more directly, include more specific facts or are more recently updated. Open the cited sources, compare them with your page and close the gaps."},
        {"q": "How fast can Perplexity cite a new page?", "a": "Because Perplexity searches the web for most answers, a well-structured page can be cited soon after it is discovered and crawled. Sitemaps, internal links and IndexNow help it get found faster."},
        {"q": "Does Perplexity SEO help with ChatGPT and Google too?", "a": "Yes. Crawl access, direct answers, sourced facts, clean structure and brand mentions help every engine that builds answers from the web, including ChatGPT search, Google AI Overviews and Copilot."},
        {"q": "Can I measure traffic from Perplexity?", "a": "Yes. Visits from Perplexity citations usually show perplexity.ai as the referrer in Google Analytics. Track them as part of an AI search channel and compare their lead rate with other sources."},
    ],
    "internal_links": [L("how to rank in ChatGPT", "how-to-rank-in-chatgpt"), L("llms.txt best practices", "best-practices-for-llms-txt"), L("what generative engine optimization is", "what-is-generative-engine-optimization-and-how-does-it-work"), CORE["results"], CORE["audit"]],
    "sources": [SRC["pplx"], SRC["geo"], SRC["robots"], SRC["indexnow"]],
})

if __name__ == "__main__":
    for p in PAGES:
        save(p)
