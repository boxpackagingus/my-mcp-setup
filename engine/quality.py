"""Quality gate: a page that fails stays a draft instead of going live."""
import re

from . import page


def _words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def _shingles(text, n=5):
    w = _words(text)
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def similarity(a, b):
    sa, sb = _shingles(a), _shingles(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def check(spec, cfg, existing_texts=()):
    """Returns (passed, problems, stats). existing_texts: plain text of pages already live."""
    q = cfg["quality"]
    problems = []
    try:
        page.validate(spec)
    except ValueError as e:
        return False, [str(e)], {}

    text = page.plain_text(spec)
    words = len(_words(text))
    kw = spec["primary_keyword"].lower()
    seo = spec["seo"]

    if words < q["min_words"]:
        problems.append(f"Too short: {words} words (minimum {q['min_words']})")
    if len(spec["sections"]) < q["min_sections"]:
        problems.append(f"Only {len(spec['sections'])} sections (minimum {q['min_sections']})")
    if len(spec["faqs"]) < q["min_faqs"]:
        problems.append(f"Only {len(spec['faqs'])} FAQs (minimum {q['min_faqs']})")
    if len(spec.get("internal_links", [])) < q["min_internal_links"]:
        problems.append(f"Only {len(spec.get('internal_links', []))} internal links (minimum {q['min_internal_links']})")

    if not (30 <= len(seo["title"]) <= 60):
        problems.append(f"SEO title is {len(seo['title'])} characters (aim for 30–60)")
    if not (120 <= len(seo["meta_description"]) <= 160):
        problems.append(f"Meta description is {len(seo['meta_description'])} characters (aim for 120–160)")
    answer_words = len(_words(spec["answer"]))
    if not (25 <= answer_words <= 80):
        problems.append(f"Short answer is {answer_words} words (aim for 40–60, so AI engines can quote it)")

    kw_words = set(_words(kw))
    for where, value in (("SEO title", seo["title"]), ("H1", spec["h1"]), ("short answer", spec["answer"])):
        if not kw_words <= set(_words(value)):
            problems.append(f"Primary keyword '{kw}' is not in the {where}")

    for phrase in cfg["site"].get("never_say", []):
        if phrase.lower() in text.lower():
            problems.append(f"Uses a banned phrase: '{phrase}'")
    if re.search(r"lorem ipsum|TODO|\[insert", text, re.I):
        problems.append("Contains placeholder text")
    if "<script" in " ".join(s["body_html"] for s in spec["sections"]).lower():
        problems.append("Sections must not contain <script> tags")

    worst = max((similarity(text, t) for t in existing_texts), default=0.0)
    if worst > q["max_similarity_to_existing"]:
        problems.append(f"Too similar to an existing page ({worst:.0%} overlap)")

    stats = {"words": words, "sections": len(spec["sections"]), "faqs": len(spec["faqs"]),
             "max_similarity": round(worst, 3)}
    return not problems, problems, stats
