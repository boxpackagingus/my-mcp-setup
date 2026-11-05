"""Drafts for pages 8-10. Run: python content/build/batch3.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch1 import CORE, SRC, L, save  # noqa: E402

PAGES = []

# ---------------------------------------------------------------- 8
PAGES.append({
    "query": "answer engine optimization vs generative engine optimization",
    "slug": "answer-engine-optimization-vs-generative-engine-optimization",
    "eyebrow": "AEO vs GEO",
    "primary_keyword": "AEO vs GEO",
    "secondary_keywords": ["answer engine optimization", "generative engine optimization", "AEO meaning", "AI search optimization"],
    "search_intent": "informational",
    "seo": {
        "title": "AEO vs GEO: What's the Difference and Which Matters?",
        "meta_description": "AEO vs GEO compared: answer engine optimization targets snippets and voice answers, GEO targets AI-written answers. See where they overlap and what to do.",
    },
    "h1": "AEO vs GEO: Answer Engine Optimization vs Generative Engine Optimization",
    "answer": "In AEO vs GEO, answer engine optimization (AEO) aims to make your content the direct answer in featured snippets, People Also Ask boxes and voice assistants, while generative engine optimization (GEO) aims to get your brand named and cited inside AI-written answers from ChatGPT, Perplexity, Gemini and Google AI Overviews. The tactics overlap heavily, so most businesses should do both.",
    "key_takeaways": [
        "AEO grew up around featured snippets, People Also Ask and voice search.",
        "GEO focuses on generative AI assistants that write answers and cite several sources.",
        "Both reward direct answers, question headings, FAQs and structured data.",
        "GEO adds brand-level work: mentions across the web and access for AI crawlers.",
        "Treat AEO as part of GEO rather than a separate program.",
    ],
    "sections": [
        {"heading": "What answer engine optimization means",
         "body_html": "<p>Answer engine optimization (AEO) is the practice of structuring content so a search engine or assistant can lift it as the single, direct answer to a question. The term became popular as Google added featured snippets and People Also Ask boxes, and as voice assistants started reading answers aloud.</p><p>Classic AEO tactics include answering a question in one clear paragraph, using the question as a heading, adding numbered steps or tables Google can show as a snippet, and marking up content with FAQ or HowTo structured data where appropriate.</p>"},
        {"heading": "What generative engine optimization means",
         "body_html": "<p>Generative engine optimization (GEO) targets AI systems that write an answer rather than quote one. ChatGPT, Perplexity, Gemini, Claude, Copilot and Google's AI Overviews read multiple sources, combine them and present a new response, usually naming brands and linking to a few pages.</p><p>The term comes from a 2023 research paper that measured how content changes affect a source's visibility in generated answers. Its best methods, such as adding citations, quotations and statistics, improved visibility by up to 40% in the authors' tests.</p>"},
        {"heading": "AEO vs GEO side by side",
         "body_html": "<table><tr><th></th><th>AEO</th><th>GEO</th></tr><tr><td>Target surface</td><td>Featured snippets, People Also Ask, voice answers</td><td>AI-written answers in ChatGPT, Perplexity, Gemini, Claude, Copilot, AI Overviews</td></tr><tr><td>What wins</td><td>One page quoted as the answer</td><td>Several sources summarized; brands named in the answer</td></tr><tr><td>Unit of optimization</td><td>A concise answer block</td><td>Passages across many pages, plus the brand as an entity</td></tr><tr><td>Key tactics</td><td>Question headings, short answers, lists, tables, FAQ markup</td><td>All AEO tactics, plus sourced facts, brand mentions off-site and AI crawler access</td></tr><tr><td>Measurement</td><td>Snippet ownership, impressions and clicks</td><td>Mentions and citations per engine, AI referral visits, leads</td></tr></table>"},
        {"heading": "Where AEO and GEO overlap",
         "body_html": "<p>Most of the page-level work is identical. Both approaches reward:</p><ul><li>A direct answer to the exact question in the first lines.</li><li>Headings phrased as the questions people ask.</li><li>Short paragraphs, numbered steps, lists and comparison tables.</li><li>FAQs that cover the natural follow-up questions.</li><li>Structured data that matches what is visible on the page.</li><li>Helpful, accurate content from a source that shows real expertise.</li></ul><p>If you have done good AEO work, you already have a head start on GEO.</p>"},
        {"heading": "What GEO adds beyond AEO",
         "body_html": "<h3>Brand mentions, not just page answers</h3><p>Generative engines often answer \"which provider should I choose?\" by naming companies. Whether you are named depends on what the wider web says about you: reviews, directories, industry articles, community discussions and partner pages. AEO rarely looked beyond your own page.</p><h3>Access for AI crawlers</h3><p>AI assistants use their own crawlers alongside search indexes. OpenAI documents OAI-SearchBot for ChatGPT search and Perplexity documents PerplexityBot. If they are blocked, those products cannot cite you, no matter how good your answer is.</p><h3>Evidence density</h3><p>Because generative engines combine sources, they favor pages that add something specific: a statistic, a quote, a real example, a clear trade-off. A page that only restates the common answer has less reason to be chosen.</p><h3>Machine-readable maps</h3><p>Files such as <code>llms.txt</code> give AI tools a clean list of your most useful pages. It is a young proposal and support varies, but it costs little to add.</p>"},
        {"heading": "Which should you prioritize?",
         "body_html": "<p>You do not have to choose. A practical order of work:</p><ol><li><strong>Fix the foundations</strong> so pages are crawlable and indexed by search engines and AI crawlers.</li><li><strong>Apply AEO formatting</strong> to your most important pages: direct answers, question headings, FAQs and schema.</li><li><strong>Add GEO depth:</strong> sourced facts, examples, comparisons and a clear statement of who you serve.</li><li><strong>Build off-site signals</strong> so AI engines can confidently name your brand.</li><li><strong>Measure both:</strong> snippet and search performance in Search Console, plus citations and AI referrals.</li></ol><p>For a local service business, AEO often wins quick results in voice and snippet answers. For B2B and considered purchases, GEO usually matters more, because buyers ask AI assistants to compare providers.</p>"},
        {"heading": "An example of the same page done for AEO and for GEO",
         "body_html": "<p>Take the question <em>\"How much does a GEO audit cost?\"</em></p><p><strong>AEO version:</strong> a heading with the question, a two-sentence answer explaining what affects the price, and a short list of factors. Good for a featured snippet.</p><p><strong>GEO version:</strong> everything above, plus a table of what different audit levels include, an explanation of when a cheap audit is enough and when it is not, a real example of findings from an audit, a note on how long it takes, and FAQs on follow-up questions. Good for a snippet, and far more likely to be cited and summarized by an AI assistant that is comparing options for the buyer.</p>"},
        {"heading": "Common misconceptions",
         "body_html": "<ul><li><strong>\"AEO is dead.\"</strong> Snippets and voice answers still exist, and their formatting habits are exactly what generative engines like.</li><li><strong>\"GEO is just SEO with a new name.\"</strong> It shares foundations but adds brand-level signals, AI crawler access and citation-based measurement.</li><li><strong>\"Schema alone will get me into AI answers.\"</strong> Structured data helps engines understand pages, but the content itself still has to be the best answer.</li><li><strong>\"You need different content for each engine.\"</strong> One well-structured, specific page usually serves search, snippets and AI answers at once.</li></ul>"},
    ],
    "faqs": [
        {"q": "What is the difference between AEO and GEO?", "a": "AEO focuses on making your content the direct answer in featured snippets, People Also Ask and voice assistants. GEO focuses on getting your brand named and your pages cited inside AI-written answers from tools such as ChatGPT, Perplexity, Gemini and Google AI Overviews."},
        {"q": "Is AEO part of GEO?", "a": "In practice, yes. The page-level tactics of AEO, such as direct answers, question headings, FAQs and schema, are the foundation of GEO. GEO then adds brand mentions across the web, AI crawler access and deeper evidence."},
        {"q": "Which is better for a small business, AEO or GEO?", "a": "Local service businesses often see quick AEO wins in snippets and voice answers. Businesses whose buyers compare providers before buying usually gain more from GEO. Most small businesses benefit from doing the shared basics first."},
        {"q": "Does structured data help with AEO and GEO?", "a": "It helps engines understand what a page is about and can make it eligible for rich results, as long as it matches the visible content. It supports both approaches but does not replace a genuinely useful answer."},
        {"q": "How do I measure AEO vs GEO results?", "a": "Measure AEO with snippet ownership, impressions and clicks in Google Search Console. Measure GEO by testing a fixed list of questions in each AI engine monthly, tracking mentions and citations, and counting visits and leads from AI referrers."},
        {"q": "Will AEO and GEO replace SEO?", "a": "No. Both build on SEO foundations such as crawlable, indexed, trustworthy pages. They change how you write and measure, not whether search engines need to find and trust you."},
    ],
    "internal_links": [L("GEO vs SEO compared", "geo-vs-seo"), L("what generative engine optimization is", "what-is-generative-engine-optimization-and-how-does-it-work"), L("how to show up in Google AI Overviews", "how-to-show-up-in-google-ai-overviews"), CORE["services"], CORE["audit"]],
    "sources": [SRC["geo"], SRC["aif"], SRC["sd"], SRC["oai"], SRC["pplx"]],
})

# ---------------------------------------------------------------- 9
PAGES.append({
    "query": "best practices for llms txt",
    "slug": "best-practices-for-llms-txt",
    "eyebrow": "llms.txt guide",
    "primary_keyword": "llms.txt best practices",
    "secondary_keywords": ["how to create llms.txt", "llms.txt example", "llms.txt vs robots.txt", "llms-full.txt"],
    "search_intent": "informational",
    "seo": {
        "title": "llms.txt Best Practices: How to Create One That Helps",
        "meta_description": "llms.txt best practices: what the file is, the exact format, what to include, how it differs from robots.txt and sitemaps, and mistakes to avoid.",
    },
    "h1": "llms.txt Best Practices: How to Create a File AI Tools Can Use",
    "answer": "The main llms.txt best practices are to place a Markdown file at your site root, start with your brand name and a one-line summary, then list your most useful pages in clear sections with short descriptions. Link to clean, readable versions of those pages, keep it current, and treat it as a helpful map for AI tools, not a ranking switch.",
    "key_takeaways": [
        "llms.txt is a proposed Markdown file at /llms.txt that guides AI tools to your best content.",
        "The format is simple: an H1 name, a short summary, then sections of links with descriptions.",
        "It complements robots.txt and your sitemap; it does not replace either.",
        "Support from AI companies is still uneven, so treat it as low-cost groundwork.",
        "Keep it short, accurate and updated whenever important pages change.",
    ],
    "sections": [
        {"heading": "What llms.txt is",
         "body_html": "<p><code>llms.txt</code> is a proposal, published in 2024 by Jeremy Howard of Answer.AI, for a standard file that helps large language models use a website. It lives at the root of your domain, for example <code>https://example.com/llms.txt</code>, and is written in Markdown so both people and models can read it easily.</p><p>The idea is simple. Websites are full of navigation, scripts, pop-ups and layout that make them hard for an AI tool to read within a limited context window. A short, curated file pointing to your most useful content, ideally in clean text, saves the tool from guessing.</p>"},
        {"heading": "The llms.txt format",
         "body_html": "<p>The proposal defines a small, predictable structure:</p><ol><li><strong>An H1 with the name</strong> of the site or project. This is the only required part.</li><li><strong>A blockquote</strong> with a short summary of what the site is and who it is for.</li><li><strong>Optional paragraphs</strong> with any other context a model should know.</li><li><strong>H2 sections</strong> containing lists of links, each in the form <code>- [Title](URL): short description</code>.</li><li><strong>An optional section named \"Optional\"</strong> for links a tool can skip when it needs to save space.</li></ol><p>A minimal example for a service business:</p><blockquote><code># Chimera<br>&gt; Generative Engine Optimization agency in Orange County, CA.<br><br>## Services<br>- [AI Visibility Audit](https://example.com/audit.md): what the audit covers and how to book it<br><br>## Guides<br>- [GEO vs SEO](https://example.com/geo-vs-seo.md): the differences and how they work together</code></blockquote>"},
        {"heading": "llms.txt best practices for content",
         "body_html": "<ul><li><strong>Lead with a precise summary.</strong> One or two sentences that say exactly what you do, for whom and where. This is often the first thing a tool reads about you.</li><li><strong>Curate, do not dump.</strong> List the pages that best explain your business and answer buyers' questions. A file with every URL on the site is a sitemap, not a guide.</li><li><strong>Describe every link.</strong> A short description after each link helps a model decide which page to read.</li><li><strong>Group logically.</strong> Typical sections: Services, Pricing, Guides, Case studies, About, Contact.</li><li><strong>Link to clean versions.</strong> The proposal suggests offering Markdown copies of pages, for example by adding <code>.md</code> to the URL, so tools get text without layout.</li><li><strong>Use the Optional section</strong> for secondary material such as older posts or deep documentation.</li><li><strong>Keep facts consistent</strong> with your homepage, schema and profiles. Contradictions reduce trust.</li></ul>"},
        {"heading": "llms.txt vs robots.txt vs sitemap.xml",
         "body_html": "<table><tr><th>File</th><th>Purpose</th><th>Audience</th></tr><tr><td><code>robots.txt</code></td><td>Tells crawlers what they may and may not fetch</td><td>Search and AI crawlers</td></tr><tr><td><code>sitemap.xml</code></td><td>Lists every URL you want indexed, with update dates</td><td>Search engines</td></tr><tr><td><code>llms.txt</code></td><td>Curated, described map of your most useful content</td><td>AI tools and language models</td></tr><tr><td><code>llms-full.txt</code></td><td>A common extension: the full text of key pages in one file</td><td>AI tools that want everything at once</td></tr></table><p>They work together. <code>robots.txt</code> must allow the crawlers you want; the sitemap makes sure pages are discovered and indexed; <code>llms.txt</code> points AI tools to the best of them. A page blocked in robots.txt gains nothing from being listed in llms.txt.</p>"},
        {"heading": "How much does llms.txt help today?",
         "body_html": "<p>Be realistic. llms.txt is a community proposal, not an official web standard, and AI companies have not all said they use it. Some developer tools and documentation platforms read it, and adoption is growing, but there is no public evidence that it alone moves your visibility in ChatGPT, Gemini or Google AI Overviews.</p><p>Google, for example, says there are no special requirements for its AI features beyond normal Search eligibility. So think of llms.txt as cheap groundwork: quick to create, harmless when accurate, and potentially useful as more tools adopt it. The work that clearly moves AI visibility is still crawl access, strong pages and brand authority.</p>"},
        {"heading": "Step-by-step: create your llms.txt",
         "body_html": "<ol><li><strong>List your 10–30 most important pages:</strong> core services, pricing, key guides, case studies and contact.</li><li><strong>Write a one-sentence description</strong> for each, focused on what question it answers.</li><li><strong>Write the header:</strong> an H1 with your brand name and a blockquote summary.</li><li><strong>Group the links</strong> into H2 sections and add an Optional section for extras.</li><li><strong>Publish it at the root</strong> as <code>/llms.txt</code>, served as plain text.</li><li><strong>Offer clean copies</strong> of key pages as Markdown where your platform allows it.</li><li><strong>Check robots.txt</strong> so the pages you list are not blocked.</li><li><strong>Automate updates</strong> so new pages are added when they go live. On WordPress, a small plugin can generate the file from your pages.</li></ol>"},
        {"heading": "Mistakes to avoid",
         "body_html": "<ul><li><strong>Listing blocked or broken pages.</strong> Every link should return a working page.</li><li><strong>Marketing fluff in the summary.</strong> Plain, specific language is more useful than slogans.</li><li><strong>Letting it go stale.</strong> Out-of-date prices, services or locations mislead AI tools and customers.</li><li><strong>Stuffing keywords.</strong> It does not help and makes the file less readable.</li><li><strong>Expecting it to fix weak content.</strong> llms.txt points to your pages; it cannot make them better answers.</li><li><strong>Putting private information in it.</strong> The file is public, like robots.txt.</li></ul>"},
        {"heading": "Checklist",
         "body_html": "<table><tr><th>Check</th><th>Done when</th></tr><tr><td>Location</td><td>File loads at /llms.txt as plain text</td></tr><tr><td>Header</td><td>H1 brand name and a precise one-line summary</td></tr><tr><td>Links</td><td>10–30 curated pages, each with a description</td></tr><tr><td>Clean copies</td><td>Key pages available as Markdown, where possible</td></tr><tr><td>Access</td><td>Listed pages allowed in robots.txt and indexed</td></tr><tr><td>Freshness</td><td>Updated automatically or reviewed monthly</td></tr></table>"},
    ],
    "faqs": [
        {"q": "What is llms.txt?", "a": "It is a proposed Markdown file placed at a website's root, such as example.com/llms.txt, that gives AI tools a short summary of the site and a curated list of its most useful pages. It was proposed in 2024 by Jeremy Howard of Answer.AI."},
        {"q": "What are the most important llms.txt best practices?", "a": "Use the standard format with an H1 name and a short summary, list a curated set of important pages with a description for each, link to clean text versions where possible, keep it consistent with the rest of your site, and update it when pages change."},
        {"q": "Is llms.txt the same as robots.txt?", "a": "No. Robots.txt tells crawlers what they may fetch. Llms.txt is a guide that points AI tools to your best content. You need robots.txt to allow access for llms.txt to be useful."},
        {"q": "Does Google use llms.txt for AI Overviews?", "a": "Google has not said it uses llms.txt, and its guidance states there are no special requirements for AI features beyond normal Search eligibility. Treat llms.txt as low-cost groundwork, not a ranking factor."},
        {"q": "What is llms-full.txt?", "a": "A common extension of the proposal: a single file containing the full text of your key pages, so an AI tool can read everything at once without visiting each URL."},
        {"q": "How often should I update llms.txt?", "a": "Whenever important pages are added, removed or changed. The easiest approach is to generate it automatically from your site, so it stays current without manual edits."},
    ],
    "internal_links": [L("Perplexity SEO guide", "perplexity-seo"), L("GEO SEO best practices", "geo-seo-best-practices"), L("how to rank in ChatGPT", "how-to-rank-in-chatgpt"), CORE["process"], CORE["audit"]],
    "sources": [SRC["llms"], SRC["robots"], SRC["aif"], SRC["oai"]],
})

# ---------------------------------------------------------------- 10
PAGES.append({
    "query": "geo seo best practices",
    "slug": "geo-seo-best-practices",
    "eyebrow": "Best practices",
    "primary_keyword": "GEO SEO best practices",
    "secondary_keywords": ["generative engine optimization checklist", "AI search best practices", "GEO checklist", "optimize for AI search"],
    "search_intent": "informational",
    "seo": {
        "title": "GEO SEO Best Practices: 15-Point Checklist for 2026",
        "meta_description": "GEO SEO best practices in one checklist: crawl access, page structure, quotable content, schema, llms.txt, brand authority and how to measure AI citations.",
    },
    "h1": "GEO SEO Best Practices: A 15-Point Checklist",
    "answer": "The core GEO SEO best practices are to let search and AI crawlers reach your pages, answer each buyer question directly in the first lines, support claims with specific facts and sources, structure pages with question headings, tables and FAQs, add accurate schema and llms.txt, keep your brand described consistently across the web, and measure citations and AI-referred leads.",
    "key_takeaways": [
        "Access first: a page AI crawlers cannot reach cannot be cited.",
        "Write for passages: each section should answer one question on its own.",
        "Specific, sourced facts beat general claims and keyword repetition.",
        "Brand consistency across the web helps engines name you with confidence.",
        "Measure citations, AI referrals and leads, not just rankings.",
    ],
    "sections": [
        {"heading": "Access and indexing (1–4)",
         "body_html": "<ol><li><strong>Allow the crawlers you want to be cited by.</strong> Check robots.txt for Googlebot and Bingbot, OpenAI's OAI-SearchBot, PerplexityBot and others. Also check firewall, CDN and security-plugin rules, which often block bots silently.</li><li><strong>Get every important page indexed.</strong> Use URL Inspection in Google Search Console and Bing Webmaster Tools. A page that is not indexed by search engines is rarely used by AI engines that depend on them.</li><li><strong>Keep content in the HTML.</strong> Text that only appears after heavy JavaScript, inside images, or behind tabs and logins is harder for crawlers to read.</li><li><strong>Announce new pages fast.</strong> Keep an accurate XML sitemap, link new pages from existing ones, and use IndexNow to notify participating engines such as Bing as soon as a page is published.</li></ol>"},
        {"heading": "Page structure (5–8)",
         "body_html": "<ol start=\"5\"><li><strong>Answer first.</strong> Open with a 40–60 word answer to the exact question, using the buyer's words.</li><li><strong>Use question headings.</strong> Phrase H2s and H3s as the follow-up questions people ask, so each section can be matched to a query.</li><li><strong>Make sections self-contained.</strong> Each section should make sense if quoted alone. Avoid \"as mentioned above\".</li><li><strong>Use tables, steps and lists</strong> for comparisons, processes and criteria. They are easier to summarize accurately.</li></ol>"},
        {"heading": "Content quality (9–11)",
         "body_html": "<ol start=\"9\"><li><strong>Add specific, sourced facts.</strong> In the original GEO research, adding citations, quotations and statistics improved visibility in generated answers by up to 40% in tests, while keyword stuffing did not. Replace vague claims with numbers, named methods and references.</li><li><strong>Show first-hand experience.</strong> Real examples, processes you use, results you have seen and honest trade-offs. Say who the advice is not for.</li><li><strong>Write for people, not for volume.</strong> Google's spam policies target scaled content that adds little value. Fewer, genuinely useful pages beat many thin ones in both search and AI answers.</li></ol>"},
        {"heading": "Structured data and machine-readable files (12–13)",
         "body_html": "<ol start=\"12\"><li><strong>Add accurate schema.</strong> Organization and LocalBusiness or Service on core pages; Article and FAQPage on guides; BreadcrumbList site-wide. Make sure markup matches what is visible on the page.</li><li><strong>Publish llms.txt.</strong> A short Markdown file at your root that summarizes your business and lists your most useful pages, ideally with clean text copies. It is a young proposal, so treat it as low-cost groundwork rather than a ranking factor.</li></ol>"},
        {"heading": "Authority and measurement (14–15)",
         "body_html": "<ol start=\"14\"><li><strong>Build consistent brand signals.</strong> Describe what you do the same way on your site, profiles, directories and partner pages. Earn mentions in publications, reviews and community discussions your buyers read. AI engines recommend brands they can confidently describe.</li><li><strong>Measure what matters.</strong> Test a fixed list of buyer questions in ChatGPT, Perplexity, Gemini and Google AI Overviews every month, recording mentions and citations. Group visits from AI referrers into one analytics channel. Tie leads to landing pages and sources.</li></ol>"},
        {"heading": "The checklist at a glance",
         "body_html": "<table><tr><th>#</th><th>Practice</th><th>Quick test</th></tr><tr><td>1</td><td>Allow search and AI crawlers</td><td>robots.txt and firewall allow OAI-SearchBot, PerplexityBot, Googlebot, Bingbot</td></tr><tr><td>2</td><td>Index key pages</td><td>URL Inspection shows \"URL is on Google\"</td></tr><tr><td>3</td><td>Content in HTML</td><td>Main text visible with JavaScript disabled</td></tr><tr><td>4</td><td>Fast discovery</td><td>Sitemap current; IndexNow enabled</td></tr><tr><td>5</td><td>Answer first</td><td>Answer appears in the first two sentences</td></tr><tr><td>6</td><td>Question headings</td><td>Headings match real follow-up questions</td></tr><tr><td>7</td><td>Self-contained sections</td><td>Each section reads well alone</td></tr><tr><td>8</td><td>Tables and lists</td><td>Comparisons and steps are structured</td></tr><tr><td>9</td><td>Sourced facts</td><td>Every statistic links to a source</td></tr><tr><td>10</td><td>Experience</td><td>Real examples and trade-offs included</td></tr><tr><td>11</td><td>Quality over volume</td><td>No near-duplicate or thin pages</td></tr><tr><td>12</td><td>Accurate schema</td><td>Rich Results Test passes; markup matches the page</td></tr><tr><td>13</td><td>llms.txt</td><td>/llms.txt loads and lists key pages</td></tr><tr><td>14</td><td>Brand consistency</td><td>Same description across site and profiles</td></tr><tr><td>15</td><td>Measurement</td><td>AI channel in analytics; monthly question test</td></tr></table>"},
        {"heading": "How to prioritize if you have limited time",
         "body_html": "<p>Start where the effort is smallest and the impact is largest:</p><ol><li><strong>Today:</strong> check robots.txt and security settings for blocked AI crawlers (practice 1).</li><li><strong>This week:</strong> rewrite the opening of your top five pages so they answer directly (practice 5), and add FAQs (practice 6).</li><li><strong>This month:</strong> add schema and llms.txt (12–13), set up AI referral tracking (15), and publish pages for the highest-intent questions you are missing.</li><li><strong>This quarter:</strong> build brand mentions and reviews (14) and keep improving pages based on what gets cited.</li></ol><p>Re-run your question test after each round. GEO is a loop: measure, improve the pages that matter, and measure again.</p>"},
        {"heading": "Applying the checklist to a service business",
         "body_html": "<p>Here is how the checklist plays out for a typical service company, such as a marketing agency, law firm or home-services business:</p><ul><li><strong>Homepage:</strong> the first paragraph says exactly what you do, for whom and where, in one or two sentences. Organization schema repeats the same facts.</li><li><strong>Service pages:</strong> each opens with a direct answer to \"what is this service and who is it for\", then explains process, timelines, how pricing works and what results to expect, with FAQs at the end.</li><li><strong>Comparison pages:</strong> honest \"X vs Y\" pages for the choices buyers weigh, including when the other option is better.</li><li><strong>Guides:</strong> one page per high-intent question, each linked from the relevant service page.</li><li><strong>Proof:</strong> case studies with numbers, named clients where permitted, and reviews on the platforms your buyers check.</li><li><strong>Next step:</strong> a short form or booking link on every page, so visitors sent by an AI answer can act immediately.</li></ul><p>Most service sites already have some of this. The gaps are usually the direct answers, the comparison pages and consistent proof.</p>"},
        {"heading": "Common mistakes",
         "body_html": "<ul><li>Blocking AI crawlers through a security tool and never noticing.</li><li>Rewriting pages for AI but breaking what already ranked in search.</li><li>Publishing large volumes of thin pages instead of fewer, better ones.</li><li>Adding schema that does not match the visible content.</li><li>Judging progress from a single AI answer instead of trends across many questions.</li><li>Sending AI-referred visitors to pages with no clear next step.</li></ul>"},
    ],
    "faqs": [
        {"q": "What are GEO SEO best practices?", "a": "Let search and AI crawlers reach your pages, answer each question directly at the top, back claims with specific sourced facts, structure pages with question headings, tables and FAQs, add accurate schema and llms.txt, keep your brand consistent across the web, and measure citations and AI-referred leads."},
        {"q": "What is the most important GEO best practice?", "a": "Access. If AI crawlers such as OAI-SearchBot or PerplexityBot are blocked, or your pages are not indexed, nothing else matters. After that, opening each page with a direct answer usually has the biggest effect."},
        {"q": "Do GEO best practices hurt traditional SEO?", "a": "No, when done properly. Direct answers, clear structure, sourced facts and schema support search rankings too. The risk is rewriting pages carelessly and losing content that already ranked, so change key pages with care and monitor Search Console."},
        {"q": "How many pages should I publish for GEO?", "a": "Publish as many genuinely useful pages as you can keep high quality. One strong page per important buyer question beats many thin or overlapping pages, which can hurt both search and AI visibility."},
        {"q": "How do I check if GEO best practices are working?", "a": "Test the same buyer questions in each AI engine monthly and track mentions and citations, watch AI referral sessions in analytics, check indexed pages and impressions in Search Console, and compare leads by source."},
        {"q": "Is llms.txt required for GEO?", "a": "No. It is a helpful, low-cost addition, but crawl access, strong pages and brand authority matter far more. Add it once the basics are in place."},
    ],
    "internal_links": [L("llms.txt best practices", "best-practices-for-llms-txt"), L("how to show up in Google AI Overviews", "how-to-show-up-in-google-ai-overviews"), L("how to choose a GEO agency", "how-to-choose-a-geo-agency"), CORE["process"], CORE["audit"]],
    "sources": [SRC["geo"], SRC["spam"], SRC["sd"], SRC["indexnow"], SRC["llms"], SRC["oai"]],
})

if __name__ == "__main__":
    for p in PAGES:
        save(p)
