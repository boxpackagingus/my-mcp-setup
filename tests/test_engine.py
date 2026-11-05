import copy
import json
from pathlib import Path

from engine import config, page, quality, research

ROOT = Path(__file__).resolve().parent.parent
EXAMPLE = json.loads((ROOT / "content/examples/is-geo-bring-sales.json").read_text())
CFG = config.load()


def test_example_passes_quality_gate():
    ok, problems, stats = quality.check(EXAMPLE, CFG)
    assert ok, problems
    assert stats["words"] >= CFG["quality"]["min_words"]


def test_thin_page_fails():
    spec = copy.deepcopy(EXAMPLE)
    spec["sections"] = spec["sections"][:2]
    spec["faqs"] = spec["faqs"][:1]
    ok, problems, _ = quality.check(spec, CFG)
    assert not ok
    assert any("sections" in p for p in problems)
    assert any("FAQs" in p for p in problems)


def test_duplicate_page_fails():
    ok, problems, _ = quality.check(EXAMPLE, CFG, [page.plain_text(EXAMPLE)])
    assert not ok
    assert any("similar" in p for p in problems)


def test_banned_phrase_fails():
    spec = copy.deepcopy(EXAMPLE)
    spec["sections"][0]["body_html"] += "<p>We offer guaranteed rankings.</p>"
    ok, problems, _ = quality.check(spec, CFG)
    assert not ok and any("banned" in p for p in problems)


def test_script_tags_rejected():
    spec = copy.deepcopy(EXAMPLE)
    spec["sections"][0]["body_html"] += "<script>alert(1)</script>"
    ok, problems, _ = quality.check(spec, CFG)
    assert not ok


def test_slugify():
    assert page.slugify("Is GEO bring sales?") == "is-geo-bring-sales"
    assert page.slugify("  SEO & GEO: what's   new ") == "seo-and-geo-whats-new"


def test_html_has_answer_cta_and_faq_but_no_script():
    html = page.render_html(EXAMPLE, CFG)
    assert "chimera-answer" in html
    assert html.count('class="chimera-cta"') == 2
    assert 'id="faq"' in html
    assert "<script" not in html


def test_schema_is_valid_json_with_faq():
    schema = json.loads(page.render_schema(EXAMPLE, CFG))
    types = [g["@type"] for g in schema["@graph"]]
    assert types == ["Article", "FAQPage", "BreadcrumbList"]
    assert len(schema["@graph"][1]["mainEntity"]) == len(EXAMPLE["faqs"])


def test_markdown_copy():
    md = page.render_markdown(EXAMPLE, CFG)
    assert md.startswith("# " + EXAMPLE["h1"])
    assert "<" not in md.replace("<code>", "")  # tags stripped


def test_same_question_detection():
    assert research.same_question("does geo bring sales", "geo bring sales")
    assert not research.same_question("geo cost for small business", "what is llms.txt")


def test_scoring_prefers_commercial_intent():
    a = research.score({"query": "geo agency cost", "source": "autocomplete", "volume": 100})
    b = research.score({"query": "what is geo", "source": "autocomplete", "volume": 100})
    assert a > b


def test_relevance_filter():
    assert research.relevant("generative engine optimization agency", CFG)
    assert research.relevant("how to rank in chatgpt", CFG)
    assert not research.relevant("cost of geothermal system", CFG)
    assert not research.relevant("cost of george mason university", CFG)
    assert not research.relevant("best geo agency in india", CFG)


def test_local_queries_rank_higher():
    a = research.score({"query": "geo agency orange county", "source": "autocomplete"}, CFG)
    b = research.score({"query": "geo agency", "source": "autocomplete"}, CFG)
    assert a > b
