"""Visual blocks for engine pages: platform logos, diagrams and charts.

A page spec can carry "visuals": [{"after": <section index>, "type": ..., ...}].
Types:
  engines   - grid of AI platforms with their logos and a note each
  flow      - a left-to-right process diagram
  timeline  - dated or phased milestones
  stats     - headline figures with logo, date and source (real, sourced numbers only)
  bars      - a horizontal bar chart (real, sourced numbers only)
  scorecard - qualitative 1-5 ratings, always labelled as an assessment
  matrix    - a comparison table with platform logos as column headers
Logos are drawn by the plugin's CSS from its icons folder (no <svg> in content).
"""
import html

ENGINES = {
    "chatgpt": ("ChatGPT", "OpenAI"),
    "claude": ("Claude", "Anthropic"),
    "perplexity": ("Perplexity", "Perplexity AI"),
    "gemini": ("Gemini", "Google"),
    "google": ("Google AI Overviews", "Google Search"),
    "copilot": ("Microsoft Copilot", "Microsoft"),
    "meta": ("Meta AI", "Meta"),
    "grok": ("Grok", "xAI"),
    "mistral": ("Le Chat", "Mistral AI"),
    "deepseek": ("DeepSeek", "DeepSeek"),
}
LETTERS = {"copilot": "Co", "deepseek": "DS"}  # no free official mark available
ASSESSMENT = "Chimera's assessment, based on our audit work. Not a measured statistic."


def _e(t):
    return html.escape(str(t), quote=True)


def logo(engine, size="md"):
    name = ENGINES.get(engine, (engine.title(), ""))[0]
    if engine in LETTERS:
        return f'<span class="cp-logo cp-logo--{size} cp-logo--text cp-logo--{engine}" role="img" aria-label="{_e(name)}">{LETTERS[engine]}</span>'
    return f'<span class="cp-logo cp-logo--{size} cp-logo--{engine}" role="img" aria-label="{_e(name)}"></span>'


def _head(v, default_eyebrow):
    lead = f'<p class="cp-sec-lead">{_e(v["lead"])}</p>' if v.get("lead") else ""
    return (f'<div class="cp-sec-head"><div><p class="cp-eyebrow">{_e(v.get("eyebrow", default_eyebrow))}</p>'
            f'<h3 class="cp-vis-title">{_e(v["title"])}</h3></div>{lead}</div>')


def _source(v):
    s = v.get("source")
    if not s:
        return ""
    return (f'<p class="cp-figsource">Source: <a href="{_e(s["url"])}" rel="nofollow noopener" target="_blank">{_e(s["title"])}</a>'
            f'{(" · " + _e(s["note"])) if s.get("note") else ""}</p>')


def engines(v, tone):
    cards = "".join(
        f'<li class="cp-engine">{logo(i["engine"])}<div><strong>{_e(ENGINES.get(i["engine"], (i["engine"], ""))[0])}</strong>'
        f'<span class="cp-engine-by">{_e(ENGINES.get(i["engine"], ("", ""))[1])}</span></div>'
        f'<p>{_e(i["note"])}</p></li>' for i in v["items"])
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--engines">{_head(v, "AI platforms")}'
            f'<ul class="cp-enginegrid">{cards}</ul><p class="cp-figsource">Logos are trademarks of their owners and are shown only to identify each platform.</p></section>')


def flow(v, tone):
    steps = []
    for k, s in enumerate(v["steps"]):
        icon = logo(s["engine"], "sm") if s.get("engine") else f'<span class="cp-flow-n">{k + 1}</span>'
        steps.append(f'<li class="cp-flow-step">{icon}<strong>{_e(s["title"])}</strong><p>{_e(s["text"])}</p></li>')
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--flow">{_head(v, "How it works")}'
            f'<ol class="cp-flow">{"".join(steps)}</ol></section>')


def timeline(v, tone):
    items = "".join(
        f'<li class="cp-tl-item"><span class="cp-tl-when">{_e(i["when"])}</span><div class="cp-tl-card">'
        f'<strong>{_e(i["title"])}</strong><p>{_e(i["text"])}</p></div></li>' for i in v["items"])
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--timeline">{_head(v, "Timeline")}'
            f'<ol class="cp-timeline">{items}</ol></section>')


def stats(v, tone):
    cards = []
    for i in v["items"]:
        src = f'<a href="{_e(i["source_url"])}" rel="nofollow noopener" target="_blank">{_e(i.get("source", "Source"))}</a>' if i.get("source_url") else ""
        cards.append(
            f'<li class="cp-stat">{logo(i["engine"]) if i.get("engine") else ""}'
            f'<span class="cp-stat-value">{_e(i["value"])}</span><span class="cp-stat-label">{_e(i["label"])}</span>'
            f'<span class="cp-stat-meta">{_e(i.get("date", ""))}{" · " if src else ""}{src}</span></li>')
    note = f'<p class="cp-figsource">{_e(v["note"])}</p>' if v.get("note") else ""
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--stats">{_head(v, "By the numbers")}'
            f'<ul class="cp-statgrid">{"".join(cards)}</ul>{note}</section>')


def bars(v, tone):
    top = max(float(i["value"]) for i in v["items"]) or 1
    unit = v.get("unit", "")
    rows = "".join(
        f'<li class="cp-bar"><span class="cp-bar-label">{_e(i["label"])}</span>'
        f'<span class="cp-bar-track"><span class="cp-bar-fill" style="width:{max(4, round(float(i["value"]) / top * 100))}%"></span></span>'
        f'<span class="cp-bar-value">{_e(i.get("display", i["value"]))}{_e(unit) if not i.get("display") else ""}</span></li>'
        for i in v["items"])
    who = f'<div class="cp-chart-who">{logo(v["engine"], "sm")}<span>{_e(v.get("chart_label", ""))}</span></div>' if v.get("engine") else ""
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--bars">{_head(v, "Chart")}'
            f'<figure class="cp-chart">{who}<ul class="cp-bars">{rows}</ul>{_source(v)}</figure></section>')


def scorecard(v, tone):
    rows = []
    for r in v["rows"]:
        dots = "".join(f'<span class="cp-dot{" is-on" if k < int(r["score"]) else ""}"></span>' for k in range(5))
        rows.append(f'<li class="cp-score"><div><strong>{_e(r["label"])}</strong><p>{_e(r.get("note", ""))}</p></div>'
                    f'<span class="cp-dots" role="img" aria-label="{int(r["score"])} out of 5">{dots}</span></li>')
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--score">{_head(v, "Scorecard")}'
            f'<ul class="cp-scorelist">{"".join(rows)}</ul>'
            f'<p class="cp-figsource">{_e(v.get("label", ASSESSMENT))}</p></section>')


def matrix(v, tone):
    head = "".join(f'<th>{logo(c, "sm")}<span>{_e(ENGINES.get(c, (c, ""))[0])}</span></th>' for c in v["columns"])
    body = ""
    for r in v["rows"]:
        cells = ""
        for c in r["cells"]:
            low = str(c).lower()
            cls = "yes" if low.startswith("yes") else ("no" if low == "no" or low.startswith(("no:", "no,")) else "mid")
            cells += f'<td><span class="cp-pill cp-pill--{cls}">{_e(c)}</span></td>'
        body += f'<tr><td>{_e(r["label"])}</td>{cells}</tr>'
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--matrix">{_head(v, "Compare platforms")}'
            f'<div class="cp-tablecard cp-matrix"><table><tr><th></th>{head}</tr>{body}</table></div>{_source(v)}'
            f'<p class="cp-figsource">Logos are trademarks of their owners and are shown only to identify each platform.</p></section>')


def line(v, tone):
    """Animated, hoverable line chart drawn by the plugin's script from data-points.
    The same numbers are always visible in a data table, so they work without script too."""
    import json as _json
    pts = [{"l": i["label"], "v": float(i["value"])} for i in v["items"]]
    unit = v.get("unit", "")
    rows = "".join(f"<tr><td>{_e(i['label'])}</td><td>{_e(i.get('display', str(i['value']) + unit))}</td></tr>" for i in v["items"])
    who = f'<div class="cp-chart-who">{logo(v["engine"], "sm")}<span>{_e(v.get("chart_label", ""))}</span></div>' if v.get("engine") else ""
    first, last = v["items"][0], v["items"][-1]
    label = f'{v.get("chart_label", v["title"])}: from {first["value"]}{unit} in {first["label"]} to {last["value"]}{unit} in {last["label"]}'
    return (f'<section class="cp-sec cp-tone--{tone} cp-vis cp-vis--line">{_head(v, "Chart")}'
            f'<figure class="cp-chart">{who}'
            f'<div class="cp-line" role="img" aria-label="{_e(label)}" data-unit="{_e(unit)}" data-points="{_e(_json.dumps(pts))}"></div>'
            f'<details class="cp-chartdata"><summary>View the data</summary><table><tr><th>Date</th><th>Value</th></tr>{rows}</table></details>'
            f'{_source(v)}</figure></section>')


RENDER = {"engines": engines, "line": line, "flow": flow, "timeline": timeline, "stats": stats,
          "bars": bars, "scorecard": scorecard, "matrix": matrix}


def render(v, tone="light"):
    return RENDER[v["type"]](v, tone)
