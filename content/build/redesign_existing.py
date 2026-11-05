"""Adds hero art settings and visuals to the 11 published pages, then copies them to drafts."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import visuals_lib as V  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PUB, DRAFTS = ROOT / "content" / "published", ROOT / "content" / "drafts"

ALL6 = ["chatgpt", "perplexity", "gemini", "claude", "google", "copilot"]

EXTRAS = {
    "is-geo-bring-sales": dict(
        short_title="Does GEO Bring Sales? How AI Search Turns Into Revenue", hero_query="Is GEO worth it for my sales?",
        visuals=[V.stats(0), V.flow(1, "How a GEO sale happens", "From the buyer's question to a booked call.",
                 [("Ask", "A buyer asks an AI assistant a specific question."), ("Shortlist", "The engine names a few providers and links sources."),
                  ("Verify", "The buyer clicks through to check proof, process and fit."), ("Convert", "A clear offer and short form turn the visit into a lead.")]),
                 V.timeline(5, "A realistic GEO sales timeline", "What to expect, and when.",
                 [("Wk 1–4", "Indexed", "New pages crawled and indexed; first impressions in Search Console."),
                  ("Mo 1–3", "First citations", "Long-tail questions start citing you; first AI-referred visits."),
                  ("Mo 3–6", "Lead patterns", "Enough data to see which topics produce leads, so you double down.")])]),
    "generative-engine-optimization-agency": dict(
        short_title="Generative Engine Optimization Agency: What They Do", hero_query="Which GEO agency should I hire?",
        visuals=[V.engines(0, "The engines a GEO agency works on"), V.timeline(4, "A good first 90 days", "What a credible agency should deliver, week by week.",
                 [("Wk 1–2", "Diagnose", "Baseline of AI answers for 30–50 buyer questions plus a technical audit."),
                  ("Wk 2–4", "Fix", "Unblock AI crawlers, fix indexing, add schema and llms.txt, set up tracking."),
                  ("Wk 4–8", "Structure + content", "Rebuild key pages and publish answers to high-intent questions."),
                  ("Wk 8–12", "Authority + measure", "Earn mentions, re-test the baseline and report what moved.")]),
                 V.stats(5, "Why brands hire a GEO agency now")]),
    "how-to-choose-a-geo-agency": dict(
        short_title="How to Choose a GEO Agency: 10-Point Checklist", hero_query="How do I choose the right GEO agency?",
        visuals=[V.scorecard(1, "What matters most when you choose", "How much weight to give each factor when comparing agencies.",
                 [("Shows your live AI baseline", 5, "The fastest way to tell real expertise from a sales deck."),
                  ("Page-level plan", 5, "Names the pages and fixes, not just tactics."),
                  ("Verifiable measurement", 5, "Citations per engine, AI referrals and leads."),
                  ("Keeps SEO healthy", 4, "Protects rankings AI answers already rely on."),
                  ("Price", 3, "Compare only after you know what each agency will actually do.")]),
                 V.engines(4, "Engines your agency should cover")]),
    "geo-vs-seo": dict(
        short_title="GEO vs SEO: Key Differences and How They Work Together", hero_query="What's the difference between GEO and SEO?",
        hero_engines=["google", "chatgpt", "perplexity", "gemini", "claude", "copilot"],
        visuals=[V.flow(2, *V.ANSWER_FLOW), V.stats(4, "The audience AI answers now reach"), V.citations_matrix(5)]),
    "what-is-generative-engine-optimization-and-how-does-it-work": dict(
        short_title="What Is Generative Engine Optimization (GEO)?", hero_query="What is generative engine optimization?",
        visuals=[V.engines(0, "Generative engines GEO targets"), V.flow(1, *V.ANSWER_FLOW), V.chatgpt_growth(3), V.crawler_matrix(4)]),
    "how-to-rank-in-chatgpt": dict(
        short_title="How to Rank in ChatGPT: 9 Steps to Get Recommended", hero_query="How do I get my brand recommended by ChatGPT?",
        hero_engines=["chatgpt", "google", "perplexity", "gemini", "claude", "copilot"],
        visuals=[V.chatgpt_growth(0), V.crawler_matrix(1), V.flow(3, "From question to recommendation in ChatGPT", "What happens between a buyer's prompt and your brand being named.",
                 [("Prompt", "A buyer asks ChatGPT for options or advice."), ("Search", "OAI-SearchBot's index and search partners supply candidate pages."),
                  ("Weigh", "ChatGPT favors clear answers, specifics and brands mentioned across the web."), ("Recommend", "It names a few brands and links the pages it used.")])]),
    "how-to-show-up-in-google-ai-overviews": dict(
        short_title="How to Show Up in Google AI Overviews", hero_query="How do I get my site into Google AI Overviews?",
        hero_engines=["google", "gemini", "chatgpt", "perplexity", "claude", "copilot"],
        visuals=[V.stats(0, "How big Google's AI answers are"), V.flow(2, "How AI Overviews build an answer", "Google describes a 'query fan-out' that searches several sub-topics at once.",
                 [("Query", "A searcher asks a question in Google."), ("Fan-out", "Google issues related searches across subtopics."),
                  ("Select", "Indexed pages eligible for snippets are used as sources."), ("Summarize", "An overview appears above results with links to sources.")]),
                 V.gemini_growth(5)]),
    "perplexity-seo": dict(
        short_title="Perplexity SEO: How to Get Cited by Perplexity", hero_query="How do I get cited by Perplexity?",
        hero_engines=["perplexity", "chatgpt", "google", "gemini", "claude", "copilot"],
        visuals=[V.stats(0, "Perplexity's scale, and its peers"), V.crawler_matrix(1), V.citations_matrix(5)]),
    "answer-engine-optimization-vs-generative-engine-optimization": dict(
        short_title="AEO vs GEO: What's the Difference?", hero_query="Should I focus on AEO or GEO?",
        visuals=[V.scorecard(2, "Where AEO and GEO focus", "How strongly each tactic matters for each approach (5 = central).",
                 [("Direct answers and question headings", 5, "Central to both AEO and GEO."),
                  ("FAQ and structured data", 4, "Core AEO; supportive for GEO."),
                  ("Brand mentions across the web", 5, "Central to GEO; rarely part of classic AEO."),
                  ("AI crawler access", 5, "A GEO essential; not part of classic AEO."),
                  ("Sourced statistics and quotes", 4, "Shown to raise visibility in generative answers.")]),
                 V.engines(4, "Answer engines vs generative engines")]),
    "best-practices-for-llms-txt": dict(
        short_title="llms.txt Best Practices: Create One That Helps", hero_query="How do I create a good llms.txt file?",
        visuals=[V.flow(1, "How llms.txt fits with your other files", "Three files, three jobs.",
                 [("robots.txt", "Decides which crawlers may fetch which pages."), ("sitemap.xml", "Lists every URL you want indexed."),
                  ("llms.txt", "A short, described map of your best pages for AI tools."), ("llms-full.txt", "Full text of key pages in one file.")]),
                 V.crawler_matrix(3)]),
    "geo-seo-best-practices": dict(
        short_title="GEO SEO Best Practices: 15-Point Checklist", hero_query="What are the best practices for GEO SEO?",
        visuals=[V.crawler_matrix(0), V.scorecard(5, "Effort vs impact of each practice", "Our view of where to start if time is short (5 = highest impact for the effort).",
                 [("Unblock AI crawlers", 5, "Minutes of work; nothing else matters if bots are blocked."),
                  ("Answer-first openings", 5, "A rewrite of the first lines on your top pages."),
                  ("FAQs and schema", 4, "Moderate effort, broad benefit."),
                  ("Brand mentions off-site", 4, "Slow, but compounds over months."),
                  ("llms.txt", 2, "Cheap groundwork; impact still unproven.")]),
                 V.stats(7, "Why it pays to get this right")]),
}

if __name__ == "__main__":
    DRAFTS.mkdir(exist_ok=True)
    for slug, extra in EXTRAS.items():
        spec = json.loads((PUB / f"{slug}.json").read_text())
        spec.pop("visuals", None)
        spec.update({k: v for k, v in extra.items()})
        spec.setdefault("hero_engines", ALL6)
        n = len(spec["sections"])
        for v in spec["visuals"]:
            assert 0 <= v["after"] < n, (slug, v["after"], n)
        (DRAFTS / f"{slug}.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
        print("ready", slug, len(spec["visuals"]), "visuals")
