"""Reusable visual blocks. Every number here is company-reported and linked to its source."""

SRC_CHATGPT = {"title": "TechCrunch: Sam Altman says ChatGPT has hit 800M weekly active users (Oct 6, 2025)",
               "url": "https://techcrunch.com/2025/10/06/sam-altman-says-chatgpt-has-hit-800m-weekly-active-users/"}
SRC_GEMINI = {"title": "9to5Google: Gemini app passes 650 million monthly users (Oct 29, 2025)",
              "url": "https://9to5google.com/2025/10/29/gemini-app-650-million-users/"}
SRC_PPLX = {"title": "MediaPost: Perplexity CEO on 780M queries in May 2025",
            "url": "https://www.mediapost.com/publications/article/406449/perplexity-ceo-estimates-firm-will-serve-1b-querie.html"}
SRC_AIO = {"title": "Dataconomy: Google's AI Overviews now serve 2 billion monthly users (Jul 24, 2025)",
           "url": "https://dataconomy.com/2025/07/24/googles-ai-overviews-now-serve-2-billion-monthly-users/"}


def stats(after, title="AI search by the numbers", lead=None):
    return {"after": after, "type": "stats", "eyebrow": "By the numbers", "title": title,
            "lead": lead or "Company-reported audience figures for the biggest AI answer engines. Each is the latest official number we could verify, with its date.",
            "items": [
                {"engine": "chatgpt", "value": "800M", "label": "ChatGPT weekly active users", "date": "Oct 2025, OpenAI", "source": "TechCrunch", "source_url": SRC_CHATGPT["url"]},
                {"engine": "google", "value": "2B", "label": "AI Overviews monthly users", "date": "Jul 2025, Google", "source": "Dataconomy", "source_url": SRC_AIO["url"]},
                {"engine": "gemini", "value": "650M", "label": "Gemini app monthly active users", "date": "Oct 2025, Google", "source": "9to5Google", "source_url": SRC_GEMINI["url"]},
                {"engine": "perplexity", "value": "780M", "label": "Perplexity queries in one month", "date": "May 2025, Perplexity CEO", "source": "MediaPost", "source_url": SRC_PPLX["url"]},
            ],
            "note": "Weekly users, monthly users and monthly queries measure different things, so compare each figure with its own history rather than with the others."}


def chatgpt_growth(after):
    return {"after": after, "type": "bars", "eyebrow": "Chart", "title": "ChatGPT's weekly users, as reported by OpenAI",
            "lead": "Weekly active users grew eightfold in under two years. That is the audience now asking ChatGPT which provider to choose.",
            "engine": "chatgpt", "chart_label": "ChatGPT weekly active users (millions)", "unit": "M",
            "items": [{"label": "Nov 2023", "value": 100}, {"label": "Mar 2025", "value": 500},
                      {"label": "Aug 2025", "value": 700}, {"label": "Oct 2025", "value": 800}],
            "source": {**SRC_CHATGPT, "note": "Figures announced by OpenAI"}}


def gemini_growth(after):
    return {"after": after, "type": "bars", "eyebrow": "Chart", "title": "Gemini app monthly users, as reported by Google",
            "lead": "Google's assistant is growing fast too, so visibility in Gemini matters alongside Google Search.",
            "engine": "gemini", "chart_label": "Gemini app monthly active users (millions)", "unit": "M",
            "items": [{"label": "Oct 2024", "value": 90}, {"label": "Mar 2025", "value": 350}, {"label": "Oct 2025", "value": 650}],
            "source": {**SRC_GEMINI, "note": "Oct 2024 and Mar 2025 from court documents; Oct 2025 from Alphabet's Q3 earnings call"}}


def engines(after, title="Where your buyers ask", lead=None, notes=None):
    default = {
        "chatgpt": "The largest assistant. Searches the web for current questions and links sources in its answers.",
        "google": "AI summaries above Google results, built from pages Google has indexed.",
        "gemini": "Google's assistant app, increasingly used for research and comparisons.",
        "perplexity": "Answer engine built around numbered, clickable citations.",
        "claude": "Anthropic's assistant, used heavily for research and work tasks; can search the web.",
        "copilot": "Microsoft's assistant in Windows, Edge and Office, grounded in Bing results.",
    }
    notes = {**default, **(notes or {})}
    return {"after": after, "type": "engines", "eyebrow": "AI platforms", "title": title,
            "lead": lead or "The answer engines that matter most for buyer research, and how each one finds sources.",
            "items": [{"engine": e, "note": notes[e]} for e in ["chatgpt", "google", "gemini", "perplexity", "claude", "copilot"]]}


def crawler_matrix(after):
    return {"after": after, "type": "matrix", "eyebrow": "Crawler access", "title": "Which crawler each AI platform uses",
            "lead": "Allow these in robots.txt and your firewall, or that platform cannot read your pages for its answers.",
            "columns": ["chatgpt", "perplexity", "google", "claude", "copilot"],
            "rows": [
                {"label": "Crawler for search answers", "cells": ["OAI-SearchBot", "PerplexityBot", "Googlebot", "Claude-SearchBot", "Bingbot"]},
                {"label": "Fetches pages on a user's request", "cells": ["ChatGPT-User", "Perplexity-User", "Googlebot", "Claude-User", "Bingbot"]},
                {"label": "Separate training crawler you can block", "cells": ["Yes: GPTBot", "Not used for training", "Yes: Google-Extended", "Yes: ClaudeBot", "No separate bot"]},
            ],
            "source": {"title": "OpenAI, Perplexity, Google and Anthropic crawler documentation", "url": "https://platform.openai.com/docs/bots",
                       "note": "Check each platform's docs for changes"}}


def citations_matrix(after):
    return {"after": after, "type": "matrix", "eyebrow": "Compare platforms", "title": "How each platform shows its sources",
            "lead": "Platforms that show clickable sources send measurable visits. The rest shape decisions you see later as branded searches.",
            "columns": ["chatgpt", "perplexity", "google", "gemini", "claude", "copilot"],
            "rows": [
                {"label": "Links to sources in answers", "cells": ["Yes, when searching", "Yes, numbered", "Yes", "Sometimes", "Yes, with web search", "Yes"]},
                {"label": "Searches the live web", "cells": ["Yes", "Yes", "Yes", "Yes", "Yes, when enabled", "Yes"]},
                {"label": "Referral shows in analytics", "cells": ["Yes: chatgpt.com", "Yes: perplexity.ai", "Counted as Google", "Yes: gemini.google.com", "Yes: claude.ai", "Yes: copilot.microsoft.com"]},
            ]}


def flow(after, title, lead, steps):
    return {"after": after, "type": "flow", "eyebrow": "How it works", "title": title, "lead": lead,
            "steps": [{"title": a, "text": b} for a, b in steps]}


def timeline(after, title, lead, items):
    return {"after": after, "type": "timeline", "eyebrow": "Timeline", "title": title, "lead": lead,
            "items": [{"when": w, "title": t, "text": x} for w, t, x in items]}


def scorecard(after, title, lead, rows):
    return {"after": after, "type": "scorecard", "eyebrow": "Scorecard", "title": title, "lead": lead,
            "rows": [{"label": a, "score": s, "note": n} for a, s, n in rows]}


ANSWER_FLOW = ("How an AI engine picks its sources",
               "Every engine that searches the web follows roughly the same four steps. GEO improves your odds at each one.",
               [("Understand", "The engine works out what the buyer is really asking, often splitting it into sub-questions."),
                ("Retrieve", "It searches its index or a partner's for pages likely to answer each part."),
                ("Select", "It keeps the clearest, most trustworthy passages and drops the rest."),
                ("Answer", "It writes a summary, names brands and links the sources it used.")])
