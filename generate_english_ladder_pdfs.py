from __future__ import annotations

import math
import re
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    HRFlowable,
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
DETAIL_DIR = ROOT / "grammar-concepts"
OUTPUT_DIR = ROOT / "pdf"
STUDENT_DIR = OUTPUT_DIR / "students"
TEACHER_DIR = OUTPUT_DIR / "teachers"
LADDER_IMAGE = ROOT / "English-Ladder.png"

PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN_X = 0.72 * inch
MARGIN_TOP = 0.72 * inch
MARGIN_BOTTOM = 0.58 * inch
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN_X)

PALETTE = {
    "paper": colors.HexColor("#FBF7EF"),
    "cream": colors.HexColor("#FFF4DE"),
    "cream_alt": colors.HexColor("#F7EAD0"),
    "white": colors.HexColor("#FFFFFF"),
    "ink": colors.HexColor("#2E2519"),
    "muted": colors.HexColor("#6A573D"),
    "accent": colors.HexColor("#B96A12"),
    "accent_dark": colors.HexColor("#8A4B08"),
    "sage": colors.HexColor("#3A7B62"),
    "line": colors.HexColor("#D9C4A0"),
}


@dataclass
class SectionBlock:
    kind: str
    text: str | None = None
    items: list[str] | None = None


@dataclass
class Section:
    title: str
    blocks: list[SectionBlock]


@dataclass
class ShowcaseCard:
    title: str
    paragraphs: list[str]


@dataclass
class SupportSection:
    title: str
    blocks: list[SectionBlock]
    cards: list[ShowcaseCard]


@dataclass
class PracticeItem:
    number: int
    label: str
    prompt: str
    options: list[str]
    answer: str
    notes: list[str]


@dataclass
class ConceptData:
    slug: str
    label: str
    title: str
    subtitle: str
    core_idea: list[str]
    focus_items: list[str]
    sections: list[Section]
    support_sections: list[SupportSection]
    practice_intro: str
    practice_items: list[PracticeItem]
    concept_image: Path


def normalize_text(text: str) -> str:
    replacements = {
        "\xa0": " ",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "–": "-",
        "—": "-",
        "…": "...",
    }
    for original, updated in replacements.items():
        text = text.replace(original, updated)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    return text.strip()


def keep_text(text: str) -> bool:
    cleaned = normalize_text(text)
    if not cleaned:
        return False
    if cleaned == "4o":
        return False
    if "ChatGPT" in cleaned:
        return False
    return True


def concise_example(text: str, max_chars: int = 150) -> str:
    candidate = normalize_text(text)
    for marker in ("Sentence:", "Example:"):
        if marker in candidate:
            candidate = candidate.split(marker, 1)[1].strip()
    for marker in (
        "Analysis:",
        "Extended Example Sentences:",
        "Grammar Focus:",
        "Function:",
        "Commentary:",
    ):
        if marker in candidate:
            candidate = candidate.split(marker, 1)[0].strip()
    if len(candidate) <= max_chars:
        return candidate
    sentences = re.split(r"(?<=[.!?])\s+", candidate)
    clipped = sentences[0].strip() if sentences else candidate[:max_chars].rsplit(" ", 1)[0]
    return clipped.rstrip(" ,;:") + ("..." if len(clipped) < len(candidate) else "")


def slugify(text: str) -> str:
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def title_case_label(section_title: str) -> str:
    return normalize_text(section_title).rstrip(":")


def parse_blocks(node: Tag, title_selector: str = "h2") -> tuple[str, list[SectionBlock]]:
    title_node = node.find(title_selector, recursive=False)
    title = normalize_text(title_node.get_text(" ", strip=True)) if title_node else ""
    blocks: list[SectionBlock] = []
    for child in node.children:
        if isinstance(child, NavigableString) or not isinstance(child, Tag):
            continue
        if child.name == title_selector:
            continue
        if child.name == "h3":
            blocks.append(SectionBlock(kind="subheading", text=normalize_text(child.get_text(" ", strip=True))))
        elif child.name == "p":
            text = normalize_text(child.get_text(" ", strip=True))
            if keep_text(text):
                blocks.append(SectionBlock(kind="paragraph", text=text))
        elif child.name in {"ul", "ol"}:
            items = [
                normalize_text(item.get_text(" ", strip=True))
                for item in child.find_all("li", recursive=False)
            ]
            items = [item for item in items if item]
            if items:
                blocks.append(SectionBlock(kind="list", items=items))
    return title, blocks


def parse_support_section(node: Tag) -> SupportSection:
    title = normalize_text(node.find("h2", recursive=False).get_text(" ", strip=True))
    blocks: list[SectionBlock] = []
    cards: list[ShowcaseCard] = []
    for child in node.children:
        if isinstance(child, NavigableString) or not isinstance(child, Tag):
            continue
        if child.name == "h2":
            continue
        if child.name == "p":
            text = normalize_text(child.get_text(" ", strip=True))
            if keep_text(text):
                blocks.append(SectionBlock(kind="paragraph", text=text))
        elif child.name in {"ul", "ol"}:
            items = [
                normalize_text(item.get_text(" ", strip=True))
                for item in child.find_all("li", recursive=False)
            ]
            items = [item for item in items if item]
            if items:
                blocks.append(SectionBlock(kind="list", items=items))
        elif child.name == "div" and "showcase-grid" in (child.get("class") or []):
            for article in child.select(".showcase-card"):
                card_title_node = article.find("h3")
                card_title = normalize_text(card_title_node.get_text(" ", strip=True)) if card_title_node else "Showcase"
                paragraphs = [
                    normalize_text(paragraph.get_text(" ", strip=True))
                    for paragraph in article.find_all("p")
                ]
                paragraphs = [paragraph for paragraph in paragraphs if keep_text(paragraph)]
                cards.append(ShowcaseCard(title=card_title, paragraphs=paragraphs))
    return SupportSection(title=title, blocks=blocks, cards=cards)


def parse_concept(path: Path) -> ConceptData:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    hero = soup.select_one(".grammar-hero-copy")
    if hero is None:
        raise ValueError(f"Could not find grammar hero in {path}")

    label = normalize_text(hero.select_one(".eyebrow").get_text(" ", strip=True))
    title = normalize_text(hero.select_one("h1").get_text(" ", strip=True))

    hero_paragraphs = [
        normalize_text(node.get_text(" ", strip=True))
        for node in hero.find_all("p", recursive=False)
        if "eyebrow" not in (node.get("class") or [])
    ]
    subtitle = hero_paragraphs[0] if hero_paragraphs else ""

    focus_items = [
        normalize_text(item.get_text(" ", strip=True))
        for item in soup.select(".grammar-focus-list li")
    ]

    overview = soup.select_one(".grammar-overview-card")
    core_idea = []
    if overview:
        core_idea = [
            normalize_text(node.get_text(" ", strip=True))
            for node in overview.find_all("p", recursive=False)
        ]
        core_idea = [paragraph for paragraph in core_idea if keep_text(paragraph)]

    sections: list[Section] = []
    for section_node in soup.select("section.grammar-section"):
        title_text, blocks = parse_blocks(section_node)
        sections.append(Section(title=title_text, blocks=blocks))

    support_sections: list[SupportSection] = []
    for support_node in soup.select("section.grammar-support"):
        if "grammar-footer-nav" in (support_node.get("class") or []):
            continue
        support_sections.append(parse_support_section(support_node))

    practice = soup.select_one(".grammar-practice")
    practice_intro = ""
    practice_items: list[PracticeItem] = []
    if practice:
        intro_node = practice.find("p", recursive=False)
        practice_intro = normalize_text(intro_node.get_text(" ", strip=True)) if intro_node else ""
        for card in practice.select(".practice-card"):
            label_node = card.select_one(".practice-item-label")
            prompt_lines = [
                normalize_text(node.get_text(" ", strip=True))
                for node in card.find_all("p", recursive=False)
            ]
            correct_nodes = [
                normalize_text(node.get_text(" ", strip=True))
                for node in card.select(".practice-feedback-item-correct")
            ]
            if not label_node or not prompt_lines or not correct_nodes:
                continue
            label_text = normalize_text(label_node.get_text(" ", strip=True))
            match = re.search(r"(\d+)", label_text)
            number = int(match.group(1)) if match else len(practice_items) + 1
            options = [
                normalize_text(option.get_text(" ", strip=True))
                for option in card.select(".practice-options li")
            ]
            notes = [
                normalize_text(note.get_text(" ", strip=True))
                for note in card.select(".practice-notes p")
            ]
            practice_items.append(
                PracticeItem(
                    number=number,
                    label=label_text,
                    prompt=normalize_text(" ".join(prompt_lines)),
                    options=[option for option in options if option],
                    answer=normalize_text(" ".join(correct_nodes)),
                    notes=[note for note in notes if note],
                )
            )

    concept_image_node = soup.select_one(".grammar-hero-image")
    if concept_image_node is None or not concept_image_node.get("src"):
        raise ValueError(f"Could not locate concept image in {path}")
    concept_image = (path.parent / concept_image_node["src"]).resolve()

    return ConceptData(
        slug=path.stem,
        label=label,
        title=title,
        subtitle=subtitle,
        core_idea=core_idea,
        focus_items=focus_items,
        sections=sections,
        support_sections=support_sections,
        practice_intro=practice_intro,
        practice_items=practice_items,
        concept_image=concept_image,
    )


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=28,
            textColor=PALETTE["ink"],
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubhead",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=PALETTE["accent_dark"],
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCopy",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.1,
            leading=15.2,
            textColor=PALETTE["ink"],
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyMuted",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=13,
            textColor=PALETTE["muted"],
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=18,
            textColor=PALETTE["accent_dark"],
            spaceBefore=14,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Subheading",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.6,
            leading=13.2,
            textColor=PALETTE["ink"],
            spaceBefore=6,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CardHeading",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11.2,
            leading=14,
            textColor=PALETTE["accent_dark"],
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TinyCaps",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.2,
            leading=10,
            textColor=PALETTE["accent_dark"],
            spaceAfter=4,
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="PracticePrompt",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=14.2,
            textColor=PALETTE["ink"],
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="OptionLine",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.1,
            leading=12.3,
            textColor=PALETTE["ink"],
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideList",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.6,
            leading=14,
            textColor=PALETTE["ink"],
            leftIndent=10,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="AnswerKey",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=12,
            textColor=PALETTE["ink"],
        )
    )
    styles.add(
        ParagraphStyle(
            name="DialogueLine",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13.5,
            textColor=PALETTE["ink"],
            spaceAfter=4,
        )
    )
    return styles


def image_size(path: Path) -> tuple[float, float]:
    reader = ImageReader(str(path))
    width, height = reader.getSize()
    return float(width), float(height)


def fitted_image(path: Path, max_width: float, max_height: float) -> Image:
    width, height = image_size(path)
    scale = min(max_width / width, max_height / height)
    return Image(str(path), width=width * scale, height=height * scale)


def pill_table(text: str, width_hint: float = 2.0 * inch) -> Table:
    pill_style = ParagraphStyle(
        name=f"PillText-{slugify(text)[:20]}",
        fontName="Helvetica-Bold",
        fontSize=8.1,
        leading=10,
        textColor=PALETTE["accent_dark"],
        alignment=TA_CENTER,
    )
    pill = Table(
        [[Paragraph(text, pill_style)]],
        colWidths=[max(width_hint, stringWidth(text, "Helvetica-Bold", 8.1) + 18)],
    )
    pill.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["cream_alt"]),
                ("BOX", (0, 0), (-1, -1), 0.8, PALETTE["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return pill


def card(flowables: list, width: float, background=PALETTE["white"], border=PALETTE["line"], padding: int = 12) -> Table:
    table = Table([[flowables]], colWidths=[width])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("BOX", (0, 0), (-1, -1), 1.0, border),
                ("INNERGRID", (0, 0), (-1, -1), 0, colors.white),
                ("LEFTPADDING", (0, 0), (-1, -1), padding),
                ("RIGHTPADDING", (0, 0), (-1, -1), padding),
                ("TOPPADDING", (0, 0), (-1, -1), padding),
                ("BOTTOMPADDING", (0, 0), (-1, -1), padding),
            ]
        )
    )
    return table


def bullet_list(items: list[str], style: ParagraphStyle) -> ListFlowable:
    entries = [ListItem(Paragraph(item, style), leftIndent=0) for item in items]
    return ListFlowable(
        entries,
        bulletType="bullet",
        bulletFontName="Helvetica-Bold",
        bulletFontSize=6,
        bulletOffsetY=2,
        leftIndent=12,
        spaceBefore=2,
        spaceAfter=6,
    )


def rule_summary(section: Section) -> list[tuple[str, str]]:
    summary: list[tuple[str, str]] = []
    current = ""
    for block in section.blocks:
        if block.kind == "subheading" and block.text:
            current = block.text
        elif block.kind == "list" and block.items:
            first_items = [item for item in block.items if not item.endswith(":")]
            if current and first_items:
                summary.append((current, first_items[0]))
    return summary[:6]


def section_story(section: Section, styles) -> list:
    story = [
        Paragraph(section.title, styles["SectionTitle"]),
        HRFlowable(width="100%", color=PALETTE["line"], thickness=0.7, spaceBefore=0, spaceAfter=10),
    ]
    for block in section.blocks:
        if block.kind == "subheading" and block.text:
            story.append(Paragraph(block.text, styles["Subheading"]))
        elif block.kind == "paragraph" and block.text:
            story.append(Paragraph(block.text, styles["BodyCopy"]))
        elif block.kind == "list" and block.items:
            story.append(bullet_list(block.items, styles["BodyCopy"]))
    story.append(Spacer(1, 0.08 * inch))
    return story


def support_story(section: SupportSection, styles) -> list:
    story = [
        Paragraph(section.title, styles["SectionTitle"]),
        HRFlowable(width="100%", color=PALETTE["line"], thickness=0.7, spaceBefore=0, spaceAfter=10),
    ]
    for block in section.blocks:
        if block.kind == "paragraph" and block.text:
            story.append(Paragraph(block.text, styles["BodyCopy"]))
        elif block.kind == "list" and block.items:
            story.append(bullet_list(block.items, styles["BodyCopy"]))
    for showcase in section.cards:
        card_items = [Paragraph(showcase.title, styles["CardHeading"])]
        for paragraph in showcase.paragraphs:
            card_items.append(Paragraph(paragraph, styles["DialogueLine"]))
        story.append(card(card_items, CONTENT_WIDTH, background=colors.HexColor("#FFFDF8"), border=PALETTE["line"], padding=12))
        story.append(Spacer(1, 0.1 * inch))
    return story


def extract_examples(data: ConceptData, limit: int = 6) -> list[str]:
    examples: list[str] = []
    for section in data.sections:
        for block in section.blocks:
            if block.kind != "list" or not block.items:
                continue
            for item in block.items:
                candidate = concise_example(item)
                if candidate and candidate not in examples:
                    examples.append(candidate)
                if len(examples) >= limit:
                    return examples
    for support in data.support_sections:
        for showcase in support.cards:
            for paragraph in showcase.paragraphs:
                if paragraph.startswith(("A:", "B:", "Role A", "Role B")):
                    continue
                if paragraph not in examples:
                    examples.append(paragraph)
                if len(examples) >= limit:
                    return examples
    return examples[:limit]


def practice_columns(items: list[PracticeItem]) -> int:
    if not items:
        return 1
    if any(item.options or len(item.prompt) > 90 for item in items):
        return 1
    return 2


def practice_grid(items: list[PracticeItem], styles, width: float, show_answers: bool = False) -> Table:
    columns = practice_columns(items)
    gap = 12 if columns == 2 else 0
    card_width = width if columns == 1 else (width - gap) / 2
    rows = []
    current_row = []

    label_style = ParagraphStyle(
        name=f"PracticeLabel-{columns}",
        fontName="Helvetica-Bold",
        fontSize=8.6,
        leading=10,
        textColor=PALETTE["accent_dark"],
    )

    for item in items:
        label = Table([[Paragraph(item.label.upper(), label_style)]], colWidths=[card_width - 22])
        label.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), PALETTE["cream_alt"]),
                    ("BOX", (0, 0), (-1, -1), 0.8, PALETTE["line"]),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        card_items = [label, Spacer(1, 8), Paragraph(item.prompt, styles["PracticePrompt"])]
        for option in item.options:
            card_items.append(Paragraph(option, styles["OptionLine"]))
        card_items.append(HRFlowable(width="100%", color=PALETTE["line"], thickness=0.8, spaceBefore=4, spaceAfter=7))

        if show_answers:
            card_items.append(Paragraph(f"<b>Answer:</b> {item.answer}", styles["BodyCopy"]))
            for note in item.notes[:1]:
                card_items.append(Paragraph(note, styles["BodyMuted"]))
        else:
            answer_prompt = "Correct choice: ____________________" if item.options else "Answer: ____________________"
            card_items.append(Paragraph(answer_prompt, styles["BodyCopy"]))

        current_row.append(
            card(
                card_items,
                card_width,
                background=colors.HexColor("#FFFDF8"),
                border=PALETTE["line"],
                padding=11,
            )
        )
        if len(current_row) == columns:
            rows.append(current_row)
            current_row = []

    if current_row:
        while len(current_row) < columns:
            current_row.append("")
        rows.append(current_row)

    table = Table(rows, colWidths=[card_width] * columns, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("INNERGRID", (0, 0), (-1, -1), gap, colors.white),
            ]
        )
    )
    return table


def answer_key_table(items: list[PracticeItem], styles, width: float) -> Table:
    if not items:
        return card([Paragraph("No practice items were available on this page.", styles["BodyCopy"])], width, background=colors.HexColor("#FFFDF8"), border=PALETTE["line"], padding=12)

    columns = 4 if len(items) >= 8 else 2
    rows = math.ceil(len(items) / columns)
    matrix = [["" for _ in range(columns)] for _ in range(rows)]
    for index, item in enumerate(items):
        row = index % rows
        col = index // rows
        matrix[row][col] = Paragraph(f"<b>{item.number:02d}</b> - {item.answer}", styles["AnswerKey"])

    table = Table(matrix, colWidths=[width / columns] * columns)
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEBELOW", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
            ]
        )
    )
    return table


def answer_review_story(items: list[PracticeItem], styles, include_notes: bool = False) -> list:
    if not items:
        return [Paragraph("No practice items were available on this page.", styles["BodyCopy"])]

    story: list = []
    for item in items:
        story.append(Paragraph(f"<b>{item.label}</b> {item.answer}", styles["BodyCopy"]))
        if include_notes and item.notes:
            story.append(Paragraph(item.notes[0], styles["BodyMuted"]))
        story.append(HRFlowable(width="100%", color=PALETTE["line"], thickness=0.55, spaceBefore=2, spaceAfter=8))
    return story


def draw_page(canvas, doc, footer_label: str, cover: bool = False):
    canvas.saveState()
    canvas.setFillColor(PALETTE["paper"])
    canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    if cover:
        canvas.setFillColor(PALETTE["cream"])
        canvas.rect(0, PAGE_HEIGHT - 180, PAGE_WIDTH, 180, fill=1, stroke=0)
        canvas.setFillColor(PALETTE["cream_alt"])
        canvas.rect(0, 0, PAGE_WIDTH, 44, fill=1, stroke=0)
    else:
        canvas.setFillColor(PALETTE["cream"])
        canvas.rect(0, PAGE_HEIGHT - 34, PAGE_WIDTH, 34, fill=1, stroke=0)
        canvas.setStrokeColor(PALETTE["line"])
        canvas.setLineWidth(0.8)
        canvas.line(MARGIN_X, PAGE_HEIGHT - 40, PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 40)
        canvas.setFillColor(PALETTE["muted"])
        canvas.setFont("Helvetica-Bold", 8.2)
        canvas.drawString(MARGIN_X, PAGE_HEIGHT - 24, "ENGLISH LADDER")
        canvas.setFont("Helvetica", 8.2)
        canvas.drawRightString(PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 24, footer_label)
        canvas.drawRightString(PAGE_WIDTH - MARGIN_X, 22, f"Page {doc.page}")
        canvas.setStrokeColor(PALETTE["line"])
        canvas.line(MARGIN_X, 30, PAGE_WIDTH - MARGIN_X, 30)

        ladder_width = 0.22 * inch
        ladder_height = ladder_width * (582 / 167)
        canvas.drawImage(
            str(LADDER_IMAGE),
            PAGE_WIDTH - MARGIN_X - ladder_width,
            PAGE_HEIGHT - 34 - ladder_height + 2,
            width=ladder_width,
            height=ladder_height,
            mask="auto",
            preserveAspectRatio=True,
        )
    canvas.restoreState()


def build_cover_story(data: ConceptData, styles, edition_label: str, intro_text: str) -> list:
    story = [Spacer(1, 0.35 * inch)]
    title_style = ParagraphStyle(
        name=f"ConceptTitle-{data.slug}-{edition_label}",
        parent=styles["CoverTitle"],
        fontSize=18.5,
        leading=22,
        textColor=PALETTE["accent_dark"],
        spaceAfter=12,
    )

    title_block = [
        Paragraph("English Ladder", styles["CoverTitle"]),
        Paragraph(edition_label, styles["CoverSubhead"]),
        Paragraph(data.title, title_style),
        Paragraph(intro_text, styles["BodyCopy"]),
    ]

    ladder = fitted_image(LADDER_IMAGE, 1.15 * inch, 4.8 * inch)
    hero = Table([[title_block, ladder]], colWidths=[5.55 * inch, 1.05 * inch])
    hero.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(hero)
    story.append(Spacer(1, 0.18 * inch))

    focus_row = [pill_table(data.label, width_hint=1.6 * inch)]
    for item in data.focus_items[:4]:
        focus_row.append(pill_table(item, width_hint=1.4 * inch))
    focus = Table([focus_row], hAlign="LEFT")
    focus.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(focus)
    story.append(Spacer(1, 0.28 * inch))

    concept_caption = [
        Paragraph("Visual anchor", styles["TinyCaps"]),
        Paragraph(
            f"Use the concept poster to spotlight the main language pattern in <b>{data.title}</b> and keep the explanation visible during practice and discussion.",
            styles["BodyCopy"],
        ),
        Spacer(1, 0.07 * inch),
        fitted_image(data.concept_image, 5.15 * inch, 3.2 * inch),
    ]
    story.append(card(concept_caption, CONTENT_WIDTH, background=PALETTE["white"], border=PALETTE["line"], padding=14))
    return story


def build_student_story(data: ConceptData, styles) -> list:
    story = build_cover_story(
        data,
        styles,
        "Student Workbook",
        "A polished self-study handout designed for print or tablet use. Read the concept, notice the pattern, and then complete the matching practice set on your own.",
    )
    story.append(PageBreak())

    story.append(Paragraph("Core Idea", styles["SectionTitle"]))
    core_card_items = [Paragraph(paragraph, styles["BodyCopy"]) for paragraph in data.core_idea]
    story.append(card(core_card_items, CONTENT_WIDTH, background=colors.HexColor("#FFFCF4"), border=PALETTE["line"], padding=14))
    story.append(Spacer(1, 0.18 * inch))

    rules = rule_summary(data.sections[0]) if data.sections else []
    if rules:
        summary_rows = [[Paragraph("<b>Quick reference</b>", styles["CardHeading"]), ""]]
        for left, right in rules:
            summary_rows.append(
                [
                    Paragraph(left, styles["BodyCopy"]),
                    Paragraph(right, styles["BodyMuted"]),
                ]
            )
        summary_table = Table(summary_rows, colWidths=[2.25 * inch, 4.0 * inch])
        summary_table.setStyle(
            TableStyle(
                [
                    ("SPAN", (0, 0), (1, 0)),
                    ("BACKGROUND", (0, 0), (-1, 0), PALETTE["cream_alt"]),
                    ("BOX", (0, 0), (-1, -1), 1.0, PALETTE["line"]),
                    ("LINEBELOW", (0, 0), (-1, 0), 0.8, PALETTE["line"]),
                    ("LEFTPADDING", (0, 0), (-1, -1), 10),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        story.append(summary_table)
        story.append(Spacer(1, 0.16 * inch))

    for section in data.sections:
        story.extend(section_story(section, styles))

    for support in data.support_sections:
        story.extend(support_story(support, styles))

    if data.practice_items:
        story.append(PageBreak())
        story.append(Paragraph("Practice Check", styles["SectionTitle"]))
        if data.practice_intro:
            story.append(Paragraph(data.practice_intro, styles["BodyCopy"]))
        story.append(Spacer(1, 0.08 * inch))
        story.append(practice_grid(data.practice_items, styles, CONTENT_WIDTH, show_answers=False))
        story.append(PageBreak())
        story.append(Paragraph("Self-check Answer Key", styles["SectionTitle"]))
        story.append(Paragraph("Use the key after you have completed every item on your own.", styles["BodyCopy"]))
        story.extend(answer_review_story(data.practice_items, styles, include_notes=False))
    return story


def build_lesson_arc(data: ConceptData) -> list[tuple[str, str]]:
    section_names = ", ".join(title_case_label(section.title) for section in data.sections[:3])
    showcase_hint = ""
    if data.support_sections:
        showcase_hint = " If time allows, finish with one of the built-in dialogue or showcase cards."
    return [
        ("Warm-up", f"Display the concept image and ask learners to predict the rule behind <b>{data.title}</b> before reading the explanation."),
        ("Model", f"Walk through the Core Idea and the sections on {section_names or 'the main focus areas'}. Pause after each part so students can restate the pattern in plain English."),
        ("Guided practice", "Project two or three examples from the concept sheet and ask pairs to explain why each choice works, not just what the answer is."),
        ("Independent work", f"Assign the {len(data.practice_items)} practice items for quiet work, partner checking, and final feedback." if data.practice_items else "Use the examples on the concept sheet for quick written or oral checks."),
        ("Closure", "Ask students to create one new sentence or mini-example of their own that follows the same pattern." + showcase_hint),
    ]


def build_error_items(data: ConceptData) -> list[str]:
    focus = ", ".join(data.focus_items[:3]) if data.focus_items else "the key contrast points"
    return [
        f"Learners may overgeneralize the first pattern they notice. Keep returning to <b>{focus}</b> and ask students to explain what changes from one example to the next.",
        "Long explanations can hide the signal word or structure. Have students underline the exact phrase that tells them which form, pattern, or response is needed.",
        "If students can choose an answer but cannot explain it, ask them to justify their choice using words taken directly from the concept sheet.",
    ]


def build_support_items(data: ConceptData) -> list[str]:
    first_support = data.support_sections[0].title if data.support_sections else "the examples"
    return [
        f"Support: teach one section at a time, then send students back to <b>{first_support}</b> or the practice set so they can apply the same rule immediately.",
        "Pair work: let students compare answers aloud before you reveal the key. The explanation step is as important as the final answer.",
        "Extension: ask stronger students to write two fresh examples or a short dialogue that uses the same target language accurately.",
    ]


def build_feedback_cues(data: ConceptData) -> list[str]:
    cues = []
    for item in data.practice_items:
        if item.notes:
            cues.append(f"{item.label}: {item.notes[0]}")
        if len(cues) >= 6:
            break
    return cues


def build_teacher_story(data: ConceptData, styles) -> list:
    story = build_cover_story(
        data,
        styles,
        "Teaching Guide",
        "A concise classroom guide with lesson flow, teaching cues, and a ready-to-use answer key built around the same English Ladder concept sheet.",
    )
    story.append(PageBreak())

    overview_rows = [
        [
            Paragraph(f"<b>Lesson focus</b><br/>{data.title}", styles["BodyCopy"]),
            Paragraph("<b>Suggested timing</b><br/>45-60 minutes", styles["BodyCopy"]),
        ],
        [
            Paragraph("<b>Core objective</b><br/>Students explain the target pattern clearly and apply it accurately in controlled practice and discussion.", styles["BodyCopy"]),
            Paragraph("<b>Materials</b><br/>Student PDF, the concept image, board space, and time for partner checking.", styles["BodyCopy"]),
        ],
    ]
    overview = Table(overview_rows, colWidths=[3.25 * inch, 3.25 * inch])
    overview.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["white"]),
                ("BOX", (0, 0), (-1, -1), 1.0, PALETTE["line"]),
                ("INNERGRID", (0, 0), (-1, -1), 0.8, PALETTE["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(Paragraph("At a Glance", styles["SectionTitle"]))
    story.append(overview)
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Suggested Lesson Flow", styles["SectionTitle"]))
    for stage, text in build_lesson_arc(data):
        story.append(Paragraph(stage, styles["Subheading"]))
        story.append(Paragraph(text, styles["BodyCopy"]))

    story.append(Paragraph("Likely Learner Errors", styles["SectionTitle"]))
    story.append(card([bullet_list(build_error_items(data), styles["GuideList"])], CONTENT_WIDTH, background=colors.HexColor("#FFFDF8"), border=PALETTE["line"], padding=12))
    story.append(Spacer(1, 0.18 * inch))

    story.append(Paragraph("Differentiation and Delivery Notes", styles["SectionTitle"]))
    story.append(card([bullet_list(build_support_items(data), styles["GuideList"])], CONTENT_WIDTH, background=colors.HexColor("#FFFDF8"), border=PALETTE["line"], padding=12))
    story.append(Spacer(1, 0.18 * inch))

    story.append(Paragraph("Model Language from the Concept Sheet", styles["SectionTitle"]))
    model_examples = extract_examples(data)
    if model_examples:
        story.append(card([bullet_list(model_examples, styles["GuideList"])], CONTENT_WIDTH, background=PALETTE["white"], border=PALETTE["line"], padding=12))

    if data.support_sections:
        story.append(Spacer(1, 0.18 * inch))
        story.append(Paragraph("Dialogue or Showcase Ideas", styles["SectionTitle"]))
        showcase_points = []
        for support in data.support_sections:
            if support.cards:
                showcase_points.extend(card.title for card in support.cards[:4])
        showcase_points = [point for point in showcase_points if point]
        if showcase_points:
            story.append(card([bullet_list(showcase_points[:6], styles["GuideList"])], CONTENT_WIDTH, background=colors.HexColor("#FFFDF8"), border=PALETTE["line"], padding=12))

    story.append(PageBreak())
    story.append(Paragraph("Answer Key", styles["SectionTitle"]))
    story.append(Paragraph("Use this key for whole-class feedback or fast marking.", styles["BodyCopy"]))
    story.extend(answer_review_story(data.practice_items, styles, include_notes=False))

    feedback_cues = build_feedback_cues(data)
    if feedback_cues:
        story.append(Spacer(1, 0.18 * inch))
        story.append(Paragraph("Feedback Cues", styles["SectionTitle"]))
        story.append(card([bullet_list(feedback_cues, styles["GuideList"])], CONTENT_WIDTH, background=colors.HexColor("#FFFDF8"), border=PALETTE["line"], padding=12))
    return story


def build_pdf(output_path: Path, story: list, footer_label: str):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title=footer_label,
        author="OpenAI Codex",
    )
    doc.build(
        story,
        onFirstPage=lambda canvas, pdf_doc: draw_page(canvas, pdf_doc, footer_label, cover=True),
        onLaterPages=lambda canvas, pdf_doc: draw_page(canvas, pdf_doc, footer_label, cover=False),
    )


def output_paths(data: ConceptData) -> tuple[Path, Path]:
    title_slug = slugify(data.title)
    student_pdf = STUDENT_DIR / f"{data.slug}-{title_slug}-student-workbook.pdf"
    teacher_pdf = TEACHER_DIR / f"{data.slug}-{title_slug}-teaching-guide.pdf"
    return student_pdf, teacher_pdf


def main():
    styles = build_styles()
    concepts = [parse_concept(path) for path in sorted(DETAIL_DIR.glob("concept-*.html"))]

    STUDENT_DIR.mkdir(parents=True, exist_ok=True)
    TEACHER_DIR.mkdir(parents=True, exist_ok=True)

    for concept in concepts:
        student_pdf, teacher_pdf = output_paths(concept)
        build_pdf(student_pdf, build_student_story(concept, styles), f"{concept.title} - Student Workbook")
        build_pdf(teacher_pdf, build_teacher_story(concept, styles), f"{concept.title} - Teaching Guide")
        print(student_pdf)
        print(teacher_pdf)


if __name__ == "__main__":
    main()
