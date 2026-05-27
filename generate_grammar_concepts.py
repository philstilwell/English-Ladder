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
PDF_DIR = ROOT / "pdf"
STUDENT_PDF_DIR = PDF_DIR / "students"
TEACHER_PDF_DIR = PDF_DIR / "teachers"
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

LABEL_PATTERN = re.compile(
    r"(Answer:|Explanation:|Feedback:|Alternative:|Correct:|Incorrect:)"
)

INLINE_CHILD_MARKER_PATTERN = re.compile(
    r"(?=\b(?:Examples?|Example Sentences?|Similar Sentences?|Similar Sentence|"
    r"Ways to say it|Formal Alternative|Formal|Informal|Alternative|"
    r"Important|Rule|Explanation|Context)\s*:)",
    flags=re.IGNORECASE,
)


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


def slugify(text: str) -> str:
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def split_embedded_labels(line: str) -> list[tuple[str, str]]:
    parts = LABEL_PATTERN.split(line)
    segments: list[tuple[str, str]] = []
    for part in parts:
        if not part:
            continue
        if part in LABEL_LINES:
            segments.append(("label", part[:-1]))
            continue
        cleaned = clean_text(part)
        if cleaned:
            segments.append(("text", cleaned))
    return segments


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
            items = parse_list_items(block)
            if not items:
                continue
            if current_section is None:
                current_section = Section(title="Key Points", blocks=[])
                sections.append(current_section)
                seen_section = True
            list_block = {
                "type": "list",
                "items": group_list_items(items),
            }
            if (
                current_section.blocks
                and current_section.blocks[-1]["type"] == "list"
                and should_merge_list_blocks(current_section.blocks[-1], list_block)
            ):
                current_section.blocks[-1]["items"][-1]["children"].extend(list_block["items"])
                current_section.blocks[-1]["items"] = group_list_items(current_section.blocks[-1]["items"])
                if (
                    len(current_section.blocks) >= 2
                    and current_section.blocks[-2]["type"] == "list"
                    and should_concatenate_list_blocks(current_section.blocks[-2], current_section.blocks[-1])
                ):
                    current_section.blocks[-2]["items"].extend(current_section.blocks[-1]["items"])
                    current_section.blocks.pop()
            elif (
                current_section.blocks
                and current_section.blocks[-1]["type"] == "list"
                and should_concatenate_list_blocks(current_section.blocks[-1], list_block)
            ):
                current_section.blocks[-1]["items"].extend(list_block["items"])
            else:
                current_section.blocks.append(list_block)

    return title, intro, sections


def direct_list_text(item: Tag) -> tuple[str, bool]:
    parts: list[str] = []
    saw_strong = False
    for child in item.contents:
        if isinstance(child, Tag) and child.name in {"ul", "ol"}:
            continue
        if isinstance(child, NavigableString):
            parts.append(str(child))
            continue
        if isinstance(child, Tag):
            if child.name in {"strong", "b"}:
                saw_strong = True
            parts.append(child.get_text(" ", strip=False))
    return clean_text("".join(parts)), saw_strong


def split_inline_children(text: str) -> tuple[str, list[dict[str, object]]]:
    parts = [clean_text(part) for part in INLINE_CHILD_MARKER_PATTERN.split(text) if clean_text(part)]
    if len(parts) <= 1:
        return text, []
    return parts[0], [{"text": part, "children": [], "strong": False} for part in parts[1:]]


def parse_list_items(block: Tag) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    for item in block.find_all("li", recursive=False):
        text, saw_strong = direct_list_text(item)
        if not text:
            continue
        text, inline_children = split_inline_children(text)
        children: list[dict[str, object]] = inline_children
        for nested in item.find_all(["ul", "ol"], recursive=False):
            children.extend(parse_list_items(nested))
        items.append(
            {
                "text": text,
                "children": group_list_items(children) if children else [],
                "strong": saw_strong,
            }
        )
    return items


def is_focus_label(item: dict[str, object]) -> bool:
    text = clean_text(str(item["text"]))
    if not text:
        return False
    if text.endswith(":"):
        return True
    if "/" in text and len(re.findall(r"[A-Za-z0-9]+", text)) <= 6:
        return True
    if item.get("strong") and len(text.split()) <= 5 and not re.search(r"[.!?]", text):
        return True
    return False


def looks_like_example_item(item: dict[str, object]) -> bool:
    text = clean_text(str(item["text"]))
    if not text:
        return False
    if text.startswith(("“", "\"")):
        return True
    if re.match(
        r"^(?:Examples?|Example Sentences?|Similar Sentences?|Similar Sentence|"
        r"Ways to say it|Formal Alternative|Formal|Informal|Alternative|"
        r"Important|Rule|Explanation|Context)\s*:",
        text,
        flags=re.IGNORECASE,
    ):
        return True
    return bool(re.search(r"[.!?)]", text) and len(text.split()) >= 5)


def is_explicit_example_item(item: dict[str, object]) -> bool:
    text = clean_text(str(item["text"]))
    return bool(re.match(r"^(?:Examples?|Example Sentences?)\s*:", text, flags=re.IGNORECASE))


def group_list_items(items: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: list[dict[str, object]] = []
    current_parent: dict[str, object] | None = None

    for item in items:
        if item["children"]:
            item["children"] = group_list_items(item["children"])

        if is_focus_label(item):
            grouped.append(item)
            current_parent = item
            continue

        if current_parent and is_explicit_example_item(item):
            current_parent["children"].append(item)
            continue

        if current_parent and looks_like_example_item(item):
            current_parent["children"].append(item)
            continue

        grouped.append(item)
        current_parent = None

    return grouped


def should_merge_list_blocks(previous_block: dict[str, object], new_block: dict[str, object]) -> bool:
    previous_items = previous_block["items"]
    new_items = new_block["items"]
    if len(previous_items) != 1 or not new_items:
        return False
    anchor = previous_items[-1]
    if anchor["children"] or not is_focus_label(anchor):
        return False
    return all(looks_like_example_item(item) or item["children"] for item in new_items)


def should_concatenate_list_blocks(previous_block: dict[str, object], new_block: dict[str, object]) -> bool:
    previous_items = previous_block["items"]
    new_items = new_block["items"]
    if not previous_items or not new_items:
        return False
    return all(item["children"] for item in previous_items + new_items)


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
                for kind, value in split_embedded_labels(line):
                    if kind == "label":
                        if value == "Answer":
                            mode = "answer"
                        else:
                            note_sections.append((value, []))
                            mode = "notes"
                        continue

                    if mode == "prompt":
                        prompt_lines.append(value)
                    elif mode == "answer":
                        answer_lines.append(value)
                    else:
                        if not note_sections:
                            note_sections.append(("Note", []))
                        note_sections[-1][1].append(value)

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


def render_list(items: list[dict[str, object]], depth: int = 0) -> str:
    tag_name = "ul"
    rendered_items: list[str] = []

    for item in items:
        text = html.escape(str(item["text"]))
        item_classes = []
        if item["children"]:
            item_classes.append("grammar-list-parent")
        label_classes = []
        if depth == 0 and (item["children"] or item.get("strong") or is_focus_label(item)):
            label_classes.append("grammar-list-label")
        class_attr = f' class="{" ".join(item_classes)}"' if item_classes else ""
        if label_classes:
            label_html = f'<span class="{" ".join(label_classes)}">{text}</span>'
        else:
            label_html = text

        child_html = render_list(item["children"], depth=depth + 1) if item["children"] else ""
        rendered_items.append(f"<li{class_attr}>{label_html}{child_html}</li>")

    return f"<{tag_name}>{''.join(rendered_items)}</{tag_name}>"


def section_anchor_id(section: Section, index: int) -> str:
    base = slugify(section.title) or "section"
    return f"section-{index + 1:02d}-{base}"


def render_section(section: Section, section_id: str) -> str:
    parts = [f"<section class=\"grammar-section\" id=\"{html.escape(section_id)}\"><h2>{html.escape(section.title)}</h2>"]
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


def split_prompt_lines(lines: list[str]) -> tuple[list[str], list[str]]:
    option_lines = [line for line in lines if line_is_option(line)]
    stem_lines = [line for line in lines if line not in option_lines]
    return stem_lines, option_lines


def option_prefix(line: str) -> str | None:
    match = re.match(r"^\s*([A-Za-z0-9ivxIVX]+[).])\s+", line)
    return match.group(1).lower() if match else None


def strip_option_prefix(line: str) -> str:
    return re.sub(r"^\s*[A-Za-z0-9ivxIVX]+[).]\s+", "", line).strip()


def normalize_feedback_text(line: str) -> str:
    lowered = line.lower().strip()
    lowered = lowered.replace('"', "").replace("'", "")
    lowered = re.sub(r"^[^a-z0-9]+|[^a-z0-9]+$", "", lowered)
    lowered = re.sub(r"\s+", " ", lowered)
    return lowered


def parse_answer_text(answer_lines: list[str]) -> tuple[str, list[tuple[str, list[str]]]]:
    answer_text = clean_text(" ".join(answer_lines))
    if not answer_text:
        return "", []

    match = re.match(
        r"^The correct (?:answer|sentence|choice|response) is\s+(.+?)(?:\s*\.\s+|(?=\s*[\"“])|$)(.*)$",
        answer_text,
        flags=re.IGNORECASE,
    )
    if match:
        correct_text = clean_text(match.group(1).strip(" ."))
        remainder = clean_text(match.group(2))
        extra_notes = [("Explanation", [remainder])] if remainder else []
        return correct_text, extra_notes

    return answer_text, []


def split_answer_fragments(answer_text: str, slot_count: int) -> list[str]:
    base_text = strip_option_prefix(answer_text)
    if slot_count <= 1:
        return [base_text] if base_text else []

    fragments = [
        fragment.strip(" .")
        for fragment in re.split(r"\s*[,;/]\s*", base_text)
        if fragment.strip(" .")
    ]
    if len(fragments) == slot_count:
        return fragments

    return [base_text] if base_text else []


def build_completed_answers(stem_lines: list[str], answer_text: str) -> list[str]:
    if not stem_lines or not answer_text:
        return []

    blank_pattern = re.compile(r"_{2,}")
    prepared_lines = [
        re.sub(r"(_{2,})\s*\([^)]+\)", r"\1", line)
        for line in stem_lines
    ]
    blank_count = sum(len(blank_pattern.findall(line)) for line in prepared_lines)
    choice_pattern = re.compile(r"(?:\([^)]*\)\s*)+")
    choice_count = 0 if blank_count else sum(len(choice_pattern.findall(line)) for line in prepared_lines)
    slot_count = blank_count or choice_count
    if not slot_count:
        return []

    fragments = split_answer_fragments(answer_text, slot_count)
    if len(fragments) != slot_count:
        return []

    fragment_index = 0
    completed_lines: list[str] = []

    for line in prepared_lines:
        if blank_count:
            def replace_blank(match: re.Match[str]) -> str:
                nonlocal fragment_index
                replacement = fragments[fragment_index]
                fragment_index += 1
                return replacement

            completed = blank_pattern.sub(replace_blank, line)
        else:
            def replace_choice(match: re.Match[str]) -> str:
                nonlocal fragment_index
                replacement = fragments[fragment_index]
                fragment_index += 1
                next_char = match.string[match.end():match.end() + 1]
                if next_char and not next_char.isspace() and next_char not in ",.;:!?)]}":
                    return f"{replacement} "
                return replacement

            completed = choice_pattern.sub(replace_choice, line, count=1)

        completed_lines.append(clean_text(completed))

    if fragment_index != slot_count:
        return []

    combined = clean_text(" ".join(line for line in completed_lines if line))
    return [combined] if combined else []


def find_matching_option(answer_text: str, option_lines: list[str]) -> str | None:
    if not answer_text or not option_lines:
        return None

    answer_label = option_prefix(answer_text)
    answer_body = normalize_feedback_text(strip_option_prefix(answer_text))

    for option in option_lines:
        if answer_label and option_prefix(option) == answer_label:
            return option

    for option in option_lines:
        option_body = normalize_feedback_text(strip_option_prefix(option))
        if answer_body and option_body == answer_body:
            return option

    for option in option_lines:
        option_body = normalize_feedback_text(strip_option_prefix(option))
        if answer_body and (answer_body in option_body or option_body in answer_body):
            return option

    return None


def derive_correct_answers(item: PracticeItem) -> list[str]:
    stem_lines, option_lines = split_prompt_lines(item.prompt_lines)
    answer_text, _ = parse_answer_text(item.answer_lines)
    matched_option = find_matching_option(answer_text, option_lines)
    if matched_option:
        return [matched_option]

    completed = build_completed_answers(stem_lines, answer_text)
    if completed:
        return completed

    return [strip_option_prefix(answer_text)] if answer_text else []


def extract_quoted_terms(text: str) -> list[str]:
    terms = re.findall(r"[\"“]([^\"”]+)[\"”]", text)
    return [clean_text(term) for term in terms if clean_text(term)]


def derive_incorrect_answers(item: PracticeItem, correct_answers: list[str]) -> list[str]:
    _, option_lines = split_prompt_lines(item.prompt_lines)
    answer_text, extra_notes = parse_answer_text(item.answer_lines)
    note_sections = item.note_sections + extra_notes
    incorrect: list[str] = []
    matched_option = find_matching_option(answer_text, option_lines)

    if option_lines:
        incorrect.extend(option for option in option_lines if option != matched_option)

    correct_context = " ".join(correct_answers + [answer_text]).lower()

    for label, lines in note_sections:
        if label.lower() == "incorrect":
            incorrect.extend(lines)
        for line in lines:
            for term in extract_quoted_terms(line):
                normalized_term = normalize_feedback_text(term)
                if not normalized_term:
                    continue
                if normalized_term in normalize_feedback_text(correct_context):
                    continue
                incorrect.append(term)

    seen: set[str] = set()
    deduped: list[str] = []
    for line in incorrect:
        cleaned = clean_text(line)
        normalized = normalize_feedback_text(strip_option_prefix(cleaned))
        if not cleaned or not normalized or normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(cleaned)

    return deduped


def render_prompt(lines: list[str]) -> str:
    if not lines:
        return "<p>Review the concept and then reveal the answer.</p>"

    stem_lines, option_lines = split_prompt_lines(lines)
    rendered: list[str] = []

    if stem_lines:
        rendered.extend(f"<p>{html.escape(line)}</p>" for line in stem_lines)

    if option_lines:
        rendered.append("<ul class=\"practice-options\">")
        rendered.extend(f"<li>{html.escape(line)}</li>" for line in option_lines)
        rendered.append("</ul>")

    return "".join(rendered)


def render_notes(note_sections: list[tuple[str, list[str]]], extra_notes: list[tuple[str, list[str]]] | None = None) -> str:
    combined_sections = list(note_sections)
    if extra_notes:
        combined_sections.extend(extra_notes)

    filtered_sections = [
        (label, lines)
        for label, lines in combined_sections
        if lines and label.lower() not in {"correct", "incorrect"}
    ]

    if not filtered_sections:
        return ""

    parts = ["<div class=\"practice-notes\">"]
    for label, lines in filtered_sections:
        parts.append(f"<p><strong>{html.escape(label)}:</strong> {html.escape(' '.join(lines))}</p>")
    parts.append("</div>")
    return "".join(parts)


def render_feedback_block(item: PracticeItem) -> str:
    answer_text, extra_notes = parse_answer_text(item.answer_lines)
    correct_answers = derive_correct_answers(item)
    incorrect_answers = derive_incorrect_answers(item, correct_answers)

    if not correct_answers and not incorrect_answers:
        answer_html = html.escape(answer_text) if answer_text else "See explanation below."
        return f"<p>{answer_html}</p>{render_notes(item.note_sections, extra_notes)}"

    parts = ["<div class=\"practice-feedback\">"]

    if correct_answers:
        parts.append("<p class=\"practice-feedback-label practice-feedback-label-correct\">Correct answer</p>")
        parts.append("<ul class=\"practice-feedback-list practice-feedback-list-correct\">")
        for line in correct_answers:
            parts.append(f"<li class=\"practice-feedback-item practice-feedback-item-correct\">{html.escape(line)}</li>")
        parts.append("</ul>")

    if incorrect_answers:
        parts.append("<p class=\"practice-feedback-label practice-feedback-label-incorrect\">Incorrect answer")
        parts.append("s</p>" if len(incorrect_answers) != 1 else "</p>")
        parts.append("<ul class=\"practice-feedback-list practice-feedback-list-incorrect\">")
        for line in incorrect_answers:
            parts.append(f"<li class=\"practice-feedback-item practice-feedback-item-incorrect\">{html.escape(line)}</li>")
        parts.append("</ul>")

    parts.append(render_notes(item.note_sections, extra_notes))
    parts.append("</div>")
    return "".join(parts)


def render_practice_items(items: list[PracticeItem]) -> str:
    cards = []
    for item in items:
        cards.append(
            textwrap.dedent(
                f"""
                <article class="practice-card">
                <h3 class="practice-item-label">Item {item.number:02d}</h3>
                {render_prompt(item.prompt_lines)}
                <details class="practice-answer">
                <summary>Reveal answer</summary>
                {render_feedback_block(item)}
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
    pills = list(enumerate(sections[:6]))
    if not pills:
        return ""
    inner = "".join(
        (
            "<li>"
            f"<a href=\"#{html.escape(section_anchor_id(section, index))}\">{html.escape(section.title)}</a>"
            "</li>"
        )
        for index, section in pills
    )
    return f"<ul class=\"grammar-focus-list\">{inner}</ul>"


def pdf_filenames(entry: ConceptEntry) -> tuple[str, str]:
    title_slug = slugify(entry.title)
    student_name = f"{Path(entry.slug).stem}-{title_slug}-student-workbook.pdf"
    teacher_name = f"{Path(entry.slug).stem}-{title_slug}-teaching-guide.pdf"
    return student_name, teacher_name


def render_detail_page(entry: ConceptEntry, previous_entry: ConceptEntry | None, next_entry: ConceptEntry | None) -> str:
    intro_html = "".join(render_paragraph(paragraph) for paragraph in entry.intro)
    rendered_sections = "".join(
        render_section(section, section_anchor_id(section, index))
        for index, section in enumerate(entry.sections)
    )
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
    student_pdf_name, teacher_pdf_name = pdf_filenames(entry)

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
        <script defer src="../app.js"></script>
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
        <div class="grammar-download-links">
        <a class="grammar-download-link" href="../pdf/students/{html.escape(student_pdf_name)}">Student PDF</a>
        <a class="grammar-download-link grammar-download-link-secondary" href="../pdf/teachers/{html.escape(teacher_pdf_name)}">Teaching Guide PDF</a>
        </div>
        {render_focus_pills(entry.sections)}
        </div>
        <div class="grammar-hero-art">
        <button
        aria-label="Open larger version of the concept image"
        class="grammar-image-trigger"
        data-lightbox-alt="{html.escape(entry.title)} concept image"
        data-lightbox-src="../assets/grammar-concepts/{html.escape(entry.image_name)}"
        type="button">
        <img alt="{html.escape(entry.title)} concept image" class="grammar-hero-image" src="../assets/grammar-concepts/{html.escape(entry.image_name)}">
        <span class="grammar-image-hint">Click to enlarge</span>
        </button>
        </div>
        </section>
        <div class="grammar-layout">
        <section class="grammar-overview-card">
        <h2>Core Idea</h2>
        {intro_html}
        </section>
        {rendered_sections}
        {practice_html}
        {showcase_html}
        <section class="grammar-support grammar-footer-nav">
        <div class="grammar-page-links">
        {previous_link}
        {next_link}
        </div>
        </section>
        </div>
        <div class="image-lightbox" hidden>
        <button aria-label="Close enlarged image" class="image-lightbox-backdrop" data-lightbox-close type="button"></button>
        <div aria-label="Enlarged concept image" aria-modal="true" class="image-lightbox-dialog" role="dialog">
        <button aria-label="Close enlarged image" class="image-lightbox-close" data-lightbox-close type="button">Close</button>
        <img alt="" class="image-lightbox-image" src="">
        </div>
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
