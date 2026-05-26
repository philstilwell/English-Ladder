from __future__ import annotations

import html
import re
import ssl
import textwrap
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


ROOT = Path(__file__).resolve().parent
DETAIL_DIR = ROOT / "grammar-concepts"
ASSET_DIR = ROOT / "assets" / "grammar-concepts"
INDEX_URL = "https://stilwellfiles.wordpress.com/english-grammar-concepts/"


CLOUDFLARE_SNIPPET = (
    "<!-- Cloudflare Web Analytics --><script defer "
    "src='https://static.cloudflareinsights.com/beacon.min.js' "
    "data-cf-beacon='{\"token\": \"c9c5fc6fc0f947efb5b32e0139ad4459\"}'></script>"
    "<!-- End Cloudflare Web Analytics -->"
)

LABEL_LINES = {
    "Answer:",
    "Explanation:",
    "Feedback:",
    "Alternative:",
    "Correct:",
    "Incorrect:",
}


@dataclass
class PracticeItem:
    number: int
    prompt_lines: list[str]
    answer_lines: list[str]
    note_sections: list[tuple[str, list[str]]]


@dataclass
class ShowcaseBlock:
    title: str
    lines: list[str]


@dataclass
class Section:
    title: str
    blocks: list[dict[str, object]]


@dataclass
class ConceptEntry:
    number: int
    label: str
    source_url: str
    slug: str
    image_url: str
    image_name: str
    title: str
    intro: list[str]
    sections: list[Section]
    practice_intro: str | None
    practice_items: list[PracticeItem]
    showcase_title: str | None
    showcase_blocks: list[ShowcaseBlock]
    preview: str


def build_ssl_context() -> ssl.SSLContext:
    try:
        import certifi
    except ImportError:
        return ssl._create_unverified_context()
    return ssl.create_default_context(cafile=certifi.where())


SSL_CONTEXT = build_ssl_context()


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, context=SSL_CONTEXT, timeout=30) as response:
        return response.read()


def fetch_soup(url: str) -> BeautifulSoup:
    return BeautifulSoup(fetch_url(url), "html.parser")


def clean_text(value: str) -> str:
    value = value.replace("\xa0", " ")
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"\s+([,.;:!?])", r"\1", value)
    value = re.sub(r"([(\[{])\s+", r"\1", value)
    value = re.sub(r"\s+([)\]}])", r"\1", value)
    value = re.sub(r"([“‘])\s+", r"\1", value)
    value = re.sub(r"\s+([”’])", r"\1", value)
    return value.strip()


def clean_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def find_first_columns(content: Tag) -> Tag:
    for child in content.find_all(recursive=False):
        if isinstance(child, Tag) and child.name == "div" and "wp-block-columns" in (child.get("class") or []):
            return child
    raise ValueError("Could not find concept columns.")


def iter_content_blocks(node: Tag):
    for child in node.children:
        if isinstance(child, NavigableString):
            continue
        if child.name in {"h2", "h3", "h4", "p", "ul", "ol"}:
            yield child
            continue
        if child.name == "div":
            yield from iter_content_blocks(child)


def parse_sections(column: Tag) -> tuple[str, list[str], list[Section]]:
    title = ""
    intro: list[str] = []
    sections: list[Section] = []
    current_section: Section | None = None
    seen_section = False

    for block in iter_content_blocks(column):
        text = clean_text(block.get_text(" ", strip=True))
        if not text:
            continue

        if block.name == "h2":
            title = text
            continue

        if block.name == "h3":
            current_section = Section(title=text, blocks=[])
            sections.append(current_section)
            seen_section = True
            continue

        if block.name == "h4":
            if current_section is None:
                current_section = Section(title="Key Points", blocks=[])
                sections.append(current_section)
                seen_section = True
            current_section.blocks.append({"type": "subheading", "text": text})
            continue

        if block.name == "p":
            if not seen_section:
                intro.append(text)
            else:
                if current_section is None:
                    current_section = Section(title="Key Points", blocks=[])
                    sections.append(current_section)
                    seen_section = True
                current_section.blocks.append({"type": "paragraph", "text": text})
            continue

        if block.name in {"ul", "ol"}:
            items = [
                clean_text(item.get_text(" ", strip=True))
                for item in block.find_all("li", recursive=False)
            ]
            items = [item for item in items if item]
            if not items:
                continue
            if current_section is None:
                current_section = Section(title="Key Points", blocks=[])
                sections.append(current_section)
                seen_section = True
            current_section.blocks.append({"type": "list", "items": items})

    return title, intro, sections


def extract_number(label: str) -> int:
    match = re.search(r"#(\d+)", label)
    if not match:
        raise ValueError(f"Could not parse concept number from {label!r}")
    return int(match.group(1))


def trim_preview(text: str, limit: int = 220) -> str:
    text = clean_text(text)
    if len(text) <= limit:
        return text
    clipped = text[: limit + 1].rsplit(" ", 1)[0]
    return clipped.rstrip(",;:") + "..."


def build_preview(intro: list[str]) -> str:
    if not intro:
        return "Study a clearer, locally hosted version of this illustrated grammar concept."
    return trim_preview(" ".join(intro))


def pull_intro_from_sections(sections: list[Section]) -> list[str]:
    for section in sections:
        for index, block in enumerate(section.blocks):
            if block["type"] == "paragraph":
                text = block["text"]
                del section.blocks[index]
                return [text]
    return []


def parse_practice(column: Tag) -> tuple[str | None, list[PracticeItem], str | None, list[ShowcaseBlock]]:
    raw_lines = [clean_text(line) for line in column.get_text("\n", strip=True).splitlines()]
    lines = [line for line in raw_lines if line and line != ":"]
    if not lines:
        return None, [], None, []

    marker_re = re.compile(r"^#?(\d+)[:.]$")
    markers = [index for index, line in enumerate(lines) if marker_re.match(line)]

    if markers:
        intro_lines: list[str] = []
        practice_items: list[PracticeItem] = []

        if markers[0] > 0:
            intro_lines = lines[: markers[0]]
            if intro_lines and intro_lines[0] == "Quiz":
                intro_lines = intro_lines[1:]

        for offset, marker_index in enumerate(markers):
            end_index = markers[offset + 1] if offset + 1 < len(markers) else len(lines)
            number = int(marker_re.match(lines[marker_index]).group(1))
            chunk = lines[marker_index + 1 : end_index]
            prompt_lines: list[str] = []
            answer_lines: list[str] = []
            note_sections: list[tuple[str, list[str]]] = []
            mode = "prompt"

            for line in chunk:
                if line in LABEL_LINES:
                    label = line[:-1]
                    if line == "Answer:":
                        mode = "answer"
                    else:
                        note_sections.append((label, []))
                        mode = "notes"
                    continue

                if mode == "prompt":
                    prompt_lines.append(line)
                elif mode == "answer":
                    answer_lines.append(line)
                else:
                    if not note_sections:
                        note_sections.append(("Note", []))
                    note_sections[-1][1].append(line)

            practice_items.append(
                PracticeItem(
                    number=number,
                    prompt_lines=prompt_lines,
                    answer_lines=answer_lines,
                    note_sections=note_sections,
                )
            )

        practice_intro = " ".join(intro_lines) if intro_lines else None
        return practice_intro, practice_items, None, []

    showcase_title = lines[0]
    showcase_blocks: list[ShowcaseBlock] = []
    current_block: ShowcaseBlock | None = None

    for line in lines[1:]:
        is_title = (
            re.match(r"^Dialogue \d+", line)
            or (len(line.split()) <= 5 and not line.endswith(".") and not re.match(r"^[AB]:", line))
        )
        if is_title:
            current_block = ShowcaseBlock(title=line.rstrip(":"), lines=[])
            showcase_blocks.append(current_block)
            continue

        if current_block is None:
            current_block = ShowcaseBlock(title="Example", lines=[])
            showcase_blocks.append(current_block)
        current_block.lines.append(line)

    return None, [], showcase_title, showcase_blocks


def render_paragraph(text: str) -> str:
    return f"<p>{html.escape(text)}</p>"


def render_list(items: list[str]) -> str:
    inner = "".join(f"<li>{html.escape(item)}</li>" for item in items)
    return f"<ul>{inner}</ul>"


def render_section(section: Section) -> str:
    parts = [f"<section class=\"grammar-section\"><h2>{html.escape(section.title)}</h2>"]
    for block in section.blocks:
        if block["type"] == "subheading":
            parts.append(f"<h3>{html.escape(block['text'])}</h3>")
        elif block["type"] == "paragraph":
            parts.append(render_paragraph(block["text"]))
        elif block["type"] == "list":
            parts.append(render_list(block["items"]))
    parts.append("</section>")
    return "".join(parts)


def line_is_option(line: str) -> bool:
    return bool(re.match(r"^(?:[A-Da-d][).]|[ivxIVX]+[).])\s", line))


def render_prompt(lines: list[str]) -> str:
    if not lines:
        return "<p>Review the concept and then reveal the answer.</p>"

    option_lines = [line for line in lines if line_is_option(line)]
    stem_lines = [line for line in lines if line not in option_lines]
    rendered: list[str] = []

    if stem_lines:
        rendered.extend(f"<p>{html.escape(line)}</p>" for line in stem_lines)

    if option_lines:
        rendered.append("<ul class=\"practice-options\">")
        rendered.extend(f"<li>{html.escape(line)}</li>" for line in option_lines)
        rendered.append("</ul>")

    return "".join(rendered)


def render_notes(note_sections: list[tuple[str, list[str]]]) -> str:
    if not note_sections:
        return ""

    parts = ["<div class=\"practice-notes\">"]
    for label, lines in note_sections:
        if not lines:
            continue
        parts.append(f"<p><strong>{html.escape(label)}:</strong> {html.escape(' '.join(lines))}</p>")
    parts.append("</div>")
    return "".join(parts)


def render_practice_items(items: list[PracticeItem]) -> str:
    cards = []
    for item in items:
        answer_html = " ".join(html.escape(line) for line in item.answer_lines) or "See note."
        cards.append(
            textwrap.dedent(
                f"""
                <article class="practice-card">
                <h3>Item {item.number:02d}</h3>
                {render_prompt(item.prompt_lines)}
                <details class="practice-answer">
                <summary>Reveal answer</summary>
                <p>{answer_html}</p>
                {render_notes(item.note_sections)}
                </details>
                </article>
                """
            ).strip()
        )
    return "".join(cards)


def render_showcase(showcase_title: str | None, blocks: list[ShowcaseBlock]) -> str:
    if not blocks:
        return ""

    parts = [
        "<section class=\"grammar-support\">",
        f"<h2>{html.escape(showcase_title or 'Applied Examples')}</h2>",
        "<div class=\"showcase-grid\">",
    ]

    for block in blocks:
        parts.append("<article class=\"showcase-card\">")
        parts.append(f"<h3>{html.escape(block.title)}</h3>")
        for line in block.lines:
            if re.match(r"^[AB]:", line):
                speaker, speech = line.split(":", 1)
                parts.append(
                    f"<p><strong>{html.escape(speaker)}:</strong> {html.escape(speech.strip())}</p>"
                )
            else:
                parts.append(f"<p>{html.escape(line)}</p>")
        parts.append("</article>")

    parts.append("</div></section>")
    return "".join(parts)


def render_focus_pills(sections: list[Section]) -> str:
    pills = sections[:6]
    if not pills:
        return ""
    inner = "".join(
        f"<li>{html.escape(section.title)}</li>"
        for section in pills
    )
    return f"<ul class=\"grammar-focus-list\">{inner}</ul>"


def render_detail_page(entry: ConceptEntry, previous_entry: ConceptEntry | None, next_entry: ConceptEntry | None) -> str:
    intro_html = "".join(render_paragraph(paragraph) for paragraph in entry.intro)
    practice_html = ""
    if entry.practice_items:
        practice_intro = (
            render_paragraph(entry.practice_intro)
            if entry.practice_intro
            else "<p>Use these prompts to check the concept before moving on.</p>"
        )
        practice_html = (
            "<section class=\"grammar-practice\">"
            "<h2>Practice Check</h2>"
            f"{practice_intro}"
            "<div class=\"practice-grid\">"
            f"{render_practice_items(entry.practice_items)}"
            "</div></section>"
        )

    showcase_html = render_showcase(entry.showcase_title, entry.showcase_blocks)

    previous_link = (
        f"<a href=\"{html.escape(previous_entry.slug)}\">&larr; {html.escape(previous_entry.label)}</a>"
        if previous_entry
        else "<span></span>"
    )
    next_link = (
        f"<a href=\"{html.escape(next_entry.slug)}\">{html.escape(next_entry.label)} &rarr;</a>"
        if next_entry
        else "<span></span>"
    )

    body = textwrap.dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta content="width=device-width, initial-scale=1.0" name="viewport">
        <title>English Ladder | {html.escape(entry.title)}</title>
        <link href="../favicon.png" rel="icon" type="image/png">
        <link href="../styles.css" rel="stylesheet">
        {CLOUDFLARE_SNIPPET}
        </head>
        <body class="theme-grammar-detail">
        <main class="page-shell">
        <nav class="top-nav">
        <a href="../index.html">Back to Level Hub</a>
        <a href="../grammar-concepts.html">All Grammar Concepts</a>
        </nav>
        <section class="grammar-hero grammar-detail-hero">
        <div class="grammar-hero-copy">
        <p class="eyebrow">{html.escape(entry.label)}</p>
        <h1>{html.escape(entry.title)}</h1>
        <p>This rebuilt lesson keeps the original concept image, tightens the structure, and turns the explanation into a clearer self-study guide.</p>
        {render_focus_pills(entry.sections)}
        </div>
        <div class="grammar-hero-art">
        <img alt="{html.escape(entry.title)} concept image" class="grammar-hero-image" src="../assets/grammar-concepts/{html.escape(entry.image_name)}">
        </div>
        </section>
        <div class="grammar-layout">
        <section class="grammar-overview-card">
        <h2>Core Idea</h2>
        {intro_html}
        </section>
        {''.join(render_section(section) for section in entry.sections)}
        {practice_html}
        {showcase_html}
        <section class="grammar-support grammar-footer-nav">
        <div class="grammar-page-links">
        {previous_link}
        {next_link}
        </div>
        </section>
        </div>
        </main>
        </body>
        </html>
        """
    )
    return body


def render_index_page(entries: list[ConceptEntry]) -> str:
    cards = []
    for entry in entries:
        cards.append(
            textwrap.dedent(
                f"""
                <article class="grammar-overview-item">
                <a class="grammar-thumb" href="grammar-concepts/{html.escape(entry.slug)}">
                <img alt="{html.escape(entry.label)} image" src="assets/grammar-concepts/{html.escape(entry.image_name)}">
                </a>
                <div class="grammar-overview-copy">
                <p class="grammar-overview-label">{html.escape(entry.label)}</p>
                <h2><a href="grammar-concepts/{html.escape(entry.slug)}">{html.escape(entry.title)}</a></h2>
                <p>{html.escape(entry.preview)}</p>
                <a class="grammar-cta" href="grammar-concepts/{html.escape(entry.slug)}">Open concept</a>
                </div>
                </article>
                """
            ).strip()
        )

    return textwrap.dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta content="width=device-width, initial-scale=1.0" name="viewport">
        <title>English Ladder | Grammar Concepts</title>
        <link href="favicon.png" rel="icon" type="image/png">
        <link href="styles.css" rel="stylesheet">
        {CLOUDFLARE_SNIPPET}
        </head>
        <body class="theme-grammar-index">
        <main class="page-shell">
        <nav class="top-nav">
        <a href="index.html">Back to Level Hub</a>
        <span>44 illustrated grammar concepts</span>
        </nav>
        <section class="grammar-hero">
        <div class="grammar-hero-copy">
        <p class="eyebrow">English Ladder</p>
        <h1>English Grammar<br>Concepts</h1>
        <p>These 44 grammar concept pages rebuild the original Stilwell Files set into a fully local English Ladder study section. Each page keeps the original image while using a cleaner structure, clearer navigation, and practice or example panels that are easier to review on phones.</p>
        <ul class="grammar-stat-list">
        <li>44 concept pages</li>
        <li>Local image assets</li>
        <li>Improved mobile reading</li>
        </ul>
        </div>
        </section>
        <section class="grammar-overview-list">
        {''.join(cards)}
        </section>
        </main>
        </body>
        </html>
        """
    )


def parse_entry(label: str, source_url: str) -> ConceptEntry:
    number = extract_number(label)
    slug = f"concept-{number:02d}.html"
    soup = fetch_soup(source_url)
    content = soup.select_one(".entry-content")
    if content is None:
        raise ValueError(f"Could not find .entry-content for {source_url}")

    image = content.find("img")
    if image is None:
        raise ValueError(f"Could not find concept image for {source_url}")

    image_url = clean_url(image.get("data-orig-file") or image.get("src"))
    image_name = f"concept-{number:02d}{Path(urllib.parse.urlsplit(image_url).path).suffix}"

    columns = find_first_columns(content)
    left_column, right_column = columns.select(":scope > .wp-block-column")[:2]

    title, intro, sections = parse_sections(left_column)
    if not intro:
        intro = pull_intro_from_sections(sections)
    practice_intro, practice_items, showcase_title, showcase_blocks = parse_practice(right_column)

    return ConceptEntry(
        number=number,
        label=label,
        source_url=source_url,
        slug=slug,
        image_url=image_url,
        image_name=image_name,
        title=title or label,
        intro=intro,
        sections=sections,
        practice_intro=practice_intro,
        practice_items=practice_items,
        showcase_title=showcase_title,
        showcase_blocks=showcase_blocks,
        preview=build_preview(intro),
    )


def download_image(source_url: str, target_path: Path) -> None:
    target_path.write_bytes(fetch_url(source_url))


def load_entries() -> list[ConceptEntry]:
    soup = fetch_soup(INDEX_URL)
    entries: list[ConceptEntry] = []
    for anchor in soup.select("h4 a"):
        label = clean_text(anchor.get_text(" ", strip=True))
        if not label.startswith("Grammar Concepts #"):
            continue
        entries.append(parse_entry(label, anchor["href"]))
    entries.sort(key=lambda entry: entry.number)
    return entries


def main() -> None:
    entries = load_entries()
    DETAIL_DIR.mkdir(exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        download_image(entry.image_url, ASSET_DIR / entry.image_name)

    for index, entry in enumerate(entries):
        previous_entry = entries[index - 1] if index > 0 else None
        next_entry = entries[index + 1] if index + 1 < len(entries) else None
        (DETAIL_DIR / entry.slug).write_text(
            render_detail_page(entry, previous_entry, next_entry),
            encoding="utf-8",
        )

    (ROOT / "grammar-concepts.html").write_text(
        render_index_page(entries),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
