"""Turns a section's plain HTML into designed blocks.

Each section is split into its top-level blocks (paragraphs, lists, tables, sub-headings,
quotes). Lists become card grids, numbered lists become step cards, sub-headings become a
grid of topic cards, tables become comparison cards. The words never change, only the layout.
"""
import re

BLOCK = re.compile(r"<(p|ul|ol|table|h3|h4|blockquote)\b([^>]*)>(.*?)</\1>", re.S)
LI = re.compile(r"<li[^>]*>(.*?)</li>", re.S)
LEAD_TITLE = re.compile(r"^\s*<strong>(.*?)</strong>\s*[:.—-]?\s*(.*)$", re.S)


def blocks(body):
    """[(tag, attrs, inner_html)] in order, ignoring whitespace between them."""
    return [(m.group(1), m.group(2), m.group(3)) for m in BLOCK.finditer(body)]


def _items(inner):
    out = []
    for raw in LI.findall(inner):
        m = LEAD_TITLE.match(raw)
        if m and m.group(2).strip():
            out.append((m.group(1).rstrip(".:"), m.group(2).strip()))
        elif m:
            out.append((m.group(1).rstrip(".:"), ""))
        else:
            out.append(("", raw.strip()))
    return out


def _feature_grid(inner):
    cards = []
    for title, text in _items(inner):
        head = f"<h4>{title}</h4>" if title else ""
        body = f"<p>{text}</p>" if text else ""
        cards.append(f'<li class="cp-fcard">{head}{body}</li>')
    return f'<ul class="cp-fgrid">{"".join(cards)}</ul>'


def _steps(inner, attrs):
    start = re.search(r'start="(\d+)"', attrs)
    first = int(start.group(1)) if start else 1
    cards = []
    for i, (title, text) in enumerate(_items(inner)):
        n = first + i
        head = f"<h4>{title}</h4>" if title else ""
        body = f"<p>{text}</p>" if text else ""
        cards.append(f'<li class="cp-step"><span class="cp-step-n">{n:02d}</span><div>{head}{body}</div></li>')
    return f'<ol class="cp-stepgrid">{"".join(cards)}</ol>'


def _render(tag, attrs, inner):
    if tag == "p":
        return f"<p>{inner}</p>"
    if tag == "ul":
        return _feature_grid(inner)
    if tag == "ol":
        return _steps(inner, attrs)
    if tag == "table":
        return f'<div class="cp-tablecard"><table>{inner}</table></div>'
    if tag == "blockquote":
        return f'<div class="cp-callout">{inner}</div>'
    if tag in ("h3", "h4"):
        return f"<h3>{inner}</h3>"
    return f"<{tag}{attrs}>{inner}</{tag}>"


def kind(body):
    tags = [b[0] for b in blocks(body)]
    if "table" in tags:
        return "compare", "Compare"
    if "h3" in tags:
        return "topics", "In detail"
    if "ol" in tags:
        return "steps", "Step by step"
    if "ul" in tags:
        return "cards", "Checklist"
    return "prose", "Explained"


def section(heading_html, anchor, body, tone, label):
    """One designed section. tone: light | paper | dark."""
    parts = blocks(body)
    variant, default_label = kind(body)
    label = label or default_label

    # Lead paragraph sits beside the heading; the rest goes below.
    lead = ""
    if parts and parts[0][0] == "p":
        lead = parts[0][2]
        parts = parts[1:]

    if variant == "topics":
        intro, groups, cur = [], [], None
        for b in parts:
            if b[0] in ("h3", "h4"):
                cur = [b[2], []]
                groups.append(cur)
            elif cur is None:
                intro.append(b)
            else:
                cur[1].append(b)
        inner = "".join(_render(*b) for b in intro)
        cards = "".join(
            f'<article class="cp-topic"><h3>{title}</h3>{"".join(_render(*b) for b in items)}</article>'
            for title, items in groups
        )
        content = f'{inner}<div class="cp-topicgrid">{cards}</div>'
    else:
        content = "".join(_render(*b) for b in parts)

    lead_html = f'<p class="cp-sec-lead">{lead}</p>' if lead else ""
    return (
        f'<section class="cp-sec cp-sec--{variant} cp-tone--{tone}" id="{anchor}">'
        f'<div class="cp-sec-head"><div><p class="cp-eyebrow">{label}</p><h2>{heading_html}</h2></div>{lead_html}</div>'
        f'<div class="cp-sec-body">{content}</div></section>'
    )
