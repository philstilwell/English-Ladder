import argparse
import html
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import feedparser
from bs4 import BeautifulSoup


MODEL_NAME = "gemini-2.5-flash"
LESSON_LIMIT = 7
NEWS_FEED_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"
MAX_GENERATION_ATTEMPTS = 3
DEFAULT_RELEASE_HOUR_UTC = 10
FORBIDDEN_TAGS = {"script", "style", "iframe", "object", "embed", "link", "meta"}
SAFE_BUTTON_HANDLER = "checkAnswer(this)"

LEVELS = [
    {
        "name": "Beginner",
        "file_path": "beginner.html",
        "cefr": "A1-A2",
        "header_label": "Beginner ESL",
        "sentence_count": 10,
        "vocabulary_count": 5,
        "quiz_count": 10,
        "overview_instruction": "Write the overview in one short and simple sentence.",
        "difficulty_instruction": (
            "Aim for strong A1-A2 level English, especially A2 rather than pre-A1. "
            "Use clear but meaningful news language, basic connectors such as because, "
            "but, after, while, or so, and slightly richer verbs than childlike phrases."
        ),
        "reading_instruction": (
            "Write exactly 10 short sentences in clear, simple English. Use very easy "
            "vocabulary, short clauses, and direct meaning for CEFR A1-A2 learners."
        ),
        "vocabulary_instruction": (
            "Choose exactly 5 useful words or short phrases that already appear in the "
            "News Brief exactly as written, define them in very simple English, and "
            "make sure those same 5 terms appear naturally in the News Brief."
        ),
        "grammar_label": "Grammar Focus",
        "grammar_instruction": (
            "Choose one basic grammar point such as simple past, simple present, "
            "because, can, there is/there are, or basic comparatives. Explain it in "
            "simple English only if that grammar point appears clearly in the News "
            "Brief. Include one exact quote from the News Brief."
        ),
        "quiz_instruction": (
            "Make exactly 10 quiz questions that are short, direct, and easy to "
            "understand. Every question must test the News Brief, the vocabulary box, "
            "or the grammar point from this same lesson. Keep each answer choice brief "
            "and beginner-friendly."
        ),
    },
    {
        "name": "Intermediate",
        "file_path": "intermediate.html",
        "cefr": "B1-B2",
        "header_label": "Intermediate ESL",
        "sentence_count": 10,
        "vocabulary_count": 5,
        "quiz_count": 10,
        "overview_instruction": "Write the overview in one clear sentence.",
        "difficulty_instruction": (
            "Aim for true B1-B2 classroom English with natural detail, more precise "
            "verbs, and clear sentence links, but keep the meaning easy to follow."
        ),
        "reading_instruction": (
            "Write exactly 10 sentences using natural CEFR B1-B2 English. Add moderate "
            "detail, but keep the meaning easy to follow."
        ),
        "vocabulary_instruction": (
            "Choose exactly 5 helpful words or phrases that already appear in the News "
            "Brief exactly as written, and define them in clear everyday English for "
            "intermediate learners. Make sure those same 5 terms appear naturally in "
            "the News Brief."
        ),
        "grammar_label": "Grammar Focus",
        "grammar_instruction": (
            "Choose one useful mid-level grammar point such as passive voice, relative "
            "clauses, present perfect, conditionals, or reporting verbs. Explain it "
            "clearly only if that grammar point appears clearly in the News Brief. "
            "Include one exact quote from the News Brief."
        ),
        "quiz_instruction": (
            "Make exactly 10 quiz questions that are thoughtful but readable for CEFR "
            "B1-B2 learners. Every question must test the News Brief, the vocabulary "
            "box, or the grammar point from this same lesson. Use short explanations "
            "in the feedback."
        ),
    },
    {
        "name": "Advanced",
        "file_path": "advanced.html",
        "cefr": "C1-Higher",
        "header_label": "Advanced ESL",
        "sentence_count": 10,
        "vocabulary_count": 5,
        "quiz_count": 10,
        "overview_instruction": "Write the overview in one polished sentence.",
        "difficulty_instruction": (
            "Aim for precise C1+ English with nuanced vocabulary, cohesive argument, "
            "and polished news-analysis style."
        ),
        "reading_instruction": (
            "Write exactly 10 sentences in a formal summary using advanced vocabulary."
        ),
        "vocabulary_instruction": (
            "Choose exactly 5 advanced terms or phrases that already appear in the News "
            "Brief exactly as written, define them precisely, and make sure those same "
            "5 terms appear naturally in the News Brief."
        ),
        "grammar_label": "Advanced Grammar",
        "grammar_instruction": (
            "Choose one advanced grammar or style feature only if it appears clearly in "
            "the News Brief. Explain it briefly and include one exact quote from the "
            "News Brief."
        ),
        "quiz_instruction": (
            "Make exactly 10 quiz questions that are appropriately challenging for "
            "advanced learners. Every question must test the News Brief, the vocabulary "
            "box, or the grammar point from this same lesson, with concise but "
            "specific feedback."
        ),
    },
]


def configure_gemini():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set.")

    from google import genai

    return genai.Client(api_key=api_key)


def get_daily_news():
    feed = feedparser.parse(NEWS_FEED_URL)
    if not feed.entries:
        raise RuntimeError("No news found today.")

    top_entry = feed.entries[0]
    summary_html = getattr(top_entry, "summary", "") or getattr(top_entry, "description", "")
    clean_summary = BeautifulSoup(summary_html, "html.parser").get_text(" ", strip=True)
    return {
        "title": normalize_text(getattr(top_entry, "title", "")),
        "summary": clean_summary,
        "link": normalize_text(getattr(top_entry, "link", "")),
    }


def build_response_schema(level):
    return {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "title",
            "overview",
            "topic",
            "news_brief_sentences",
            "vocabulary",
            "grammar",
            "quiz",
        ],
        "properties": {
            "title": {"type": "string", "minLength": 4, "maxLength": 140},
            "overview": {"type": "string", "minLength": 12, "maxLength": 220},
            "topic": {"type": "string", "minLength": 4, "maxLength": 140},
            "news_brief_sentences": {
                "type": "array",
                "minItems": level["sentence_count"],
                "maxItems": level["sentence_count"],
                "items": {"type": "string", "minLength": 6, "maxLength": 320},
            },
            "vocabulary": {
                "type": "array",
                "minItems": level["vocabulary_count"],
                "maxItems": level["vocabulary_count"],
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["term", "part_of_speech", "definition"],
                    "properties": {
                        "term": {"type": "string", "minLength": 2, "maxLength": 80},
                        "part_of_speech": {"type": "string", "minLength": 2, "maxLength": 40},
                        "definition": {"type": "string", "minLength": 6, "maxLength": 220},
                    },
                },
            },
            "grammar": {
                "type": "object",
                "additionalProperties": False,
                "required": ["concept", "explanation", "example_quote"],
                "properties": {
                    "concept": {"type": "string", "minLength": 3, "maxLength": 80},
                    "explanation": {"type": "string", "minLength": 12, "maxLength": 420},
                    "example_quote": {"type": "string", "minLength": 6, "maxLength": 220},
                },
            },
            "quiz": {
                "type": "array",
                "minItems": level["quiz_count"],
                "maxItems": level["quiz_count"],
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": [
                        "question",
                        "options",
                        "correct_option_index",
                        "option_feedback",
                    ],
                    "properties": {
                        "question": {"type": "string", "minLength": 6, "maxLength": 220},
                        "options": {
                            "type": "array",
                            "minItems": 3,
                            "maxItems": 3,
                            "items": {"type": "string", "minLength": 1, "maxLength": 160},
                        },
                        "correct_option_index": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 2,
                        },
                        "option_feedback": {
                            "type": "array",
                            "minItems": 3,
                            "maxItems": 3,
                            "items": {"type": "string", "minLength": 8, "maxLength": 220},
                        },
                    },
                },
            },
        },
    }


def build_prompt(news_item, level, revision_feedback=None):
    return f"""
You are an ESL curriculum writer creating a lesson for CEFR {level["cefr"]} learners.

Source news:
Headline: {news_item["title"]}
Summary: {news_item["summary"]}
Link: {news_item["link"] or "Not provided"}

Return only JSON that matches the supplied schema.
Use plain text only in every JSON string. Do not include HTML, Markdown, code fences, numbered lists, or angle brackets.

Important requirements:
1. {level["overview_instruction"]}
2. {level["difficulty_instruction"]}
3. {level["reading_instruction"]}
4. {level["vocabulary_instruction"]}
5. {level["grammar_instruction"]}
6. Section III must be an interactive {level["quiz_count"]}-item multiple-choice quiz.
7. The News Brief, vocabulary list, grammar point, and quiz must all match one another closely.
8. Every vocabulary term must appear naturally in the News Brief exactly as written in the vocabulary list.
9. The grammar example quote must be copied exactly from the News Brief.
10. Every quiz question must be highly relevant to the News Brief, the vocabulary list, or the grammar explanation in this same lesson.
11. Do not use generic questions that could fit a different lesson.
12. The news_brief_sentences array must contain exactly {level["sentence_count"]} complete sentences.
13. The vocabulary array must contain exactly {level["vocabulary_count"]} terms.
14. Each quiz item must have exactly 3 options, 1 correct_option_index, and 3 aligned option_feedback strings.
15. Keep the lesson factually grounded in the supplied headline and summary.
16. {level["quiz_instruction"]}

Revision feedback:
{revision_feedback or "None. This is the first draft."}
"""


def extract_json_text(raw_text):
    raw_text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", raw_text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return raw_text


def normalize_text(text):
    return re.sub(r"\s+", " ", text.strip())


def normalize_for_match(text):
    cleaned = re.sub(r"[^a-z0-9\s-]", " ", text.lower())
    return re.sub(r"\s+", " ", cleaned).strip()


def sentence_has_terminal_punctuation(text):
    return bool(re.search(r"[.!?]['\")\]]*$", text.strip()))


def strip_markup(text):
    return normalize_text(BeautifulSoup(text, "html.parser").get_text(" ", strip=True))


def flatten_strings(value):
    if isinstance(value, str):
        yield value
        return
    if isinstance(value, list):
        for item in value:
            yield from flatten_strings(item)
        return
    if isinstance(value, dict):
        for item in value.values():
            yield from flatten_strings(item)


def contains_markup(text):
    return "<" in text or ">" in text


def parse_summary_parts(summary_tag):
    date_node = summary_tag.find(class_="lesson-date-text")
    title_node = summary_tag.find(class_="lesson-title-text")
    if date_node and title_node:
        return (
            normalize_text(date_node.get_text(" ", strip=True)),
            normalize_text(title_node.get_text(" ", strip=True)),
        )

    summary_text = normalize_text(summary_tag.get_text(" ", strip=True))
    if summary_text.startswith("📅"):
        summary_text = normalize_text(summary_text[1:])

    if " - " not in summary_text:
        raise ValueError(f"Could not split lesson summary into date and title: {summary_text}")

    date_text, title_text = summary_text.split(" - ", 1)
    return normalize_text(date_text), normalize_text(title_text)


def fallback_release_datetime(date_text):
    release_date = datetime.strptime(date_text, "%B %d, %Y")
    return release_date.replace(
        hour=DEFAULT_RELEASE_HOUR_UTC,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=timezone.utc,
    )


def get_release_datetime(summary_tag, date_text, default_release_dt=None):
    release_iso = summary_tag.get("data-release-iso")
    if release_iso:
        try:
            return datetime.fromisoformat(release_iso.replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError:
            pass

    if default_release_dt is not None:
        return default_release_dt.astimezone(timezone.utc)

    return fallback_release_datetime(date_text)


def format_elapsed_text(release_dt, now_dt=None):
    now_dt = (now_dt or datetime.now(timezone.utc)).astimezone(timezone.utc)
    elapsed_seconds = max(0, int((now_dt - release_dt).total_seconds()))
    days = elapsed_seconds // 86400
    hours = (elapsed_seconds % 86400) // 3600
    day_label = "day" if days == 1 else "days"
    hour_label = "hour" if hours == 1 else "hours"
    return f"[{days} {day_label}, {hours} {hour_label} old]"


def lesson_key_from_release_dt(release_dt):
    return release_dt.astimezone(timezone.utc).date().isoformat()


def rebuild_summary_markup(summary_tag, release_dt, date_text, title_text):
    release_iso = (
        release_dt.astimezone(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    elapsed_text = format_elapsed_text(release_dt)
    markup = BeautifulSoup(
        (
            f'<span class="lesson-date-prefix">📅</span> '
            f'<span class="lesson-date-text">{html.escape(date_text)}</span> '
            f'<span class="lesson-age">{html.escape(elapsed_text)}</span> '
            f'<span class="lesson-separator">-</span> '
            f'<span class="lesson-title-text">{html.escape(title_text)}</span>'
        ),
        "html.parser",
    )
    summary_tag.clear()
    for node in list(markup.contents):
        summary_tag.append(node)
    summary_tag["data-release-iso"] = release_iso


def normalize_lesson_summary(summary_tag, default_release_dt=None):
    date_text, title_text = parse_summary_parts(summary_tag)
    release_dt = get_release_datetime(summary_tag, date_text, default_release_dt=default_release_dt)
    rebuild_summary_markup(summary_tag, release_dt, date_text, title_text)
    return release_dt


def sanitize_existing_lesson_markup(lesson_tag):
    for forbidden in list(lesson_tag.find_all(FORBIDDEN_TAGS)):
        forbidden.decompose()

    for tag in lesson_tag.find_all(True):
        attrs_to_remove = []
        for attr_name, attr_value in list(tag.attrs.items()):
            if attr_name.lower().startswith("on"):
                if tag.name == "button" and attr_name == "onclick" and attr_value == SAFE_BUTTON_HANDLER:
                    continue
                attrs_to_remove.append(attr_name)
        for attr_name in attrs_to_remove:
            del tag[attr_name]

    for button in lesson_tag.find_all("button"):
        button["type"] = "button"
        if button.get("data-feedback"):
            button["data-feedback"] = strip_markup(button["data-feedback"])

    for feedback_div in lesson_tag.find_all("div", class_="feedback"):
        feedback_div["role"] = "status"
        feedback_div["aria-live"] = "polite"


def upgrade_lesson_markup(lesson_tag, default_release_dt=None):
    sanitize_existing_lesson_markup(lesson_tag)
    summary_tag = lesson_tag.find("summary", class_="lesson-date")
    if not summary_tag:
        return None

    release_dt = normalize_lesson_summary(summary_tag, default_release_dt=default_release_dt)
    lesson_tag["data-lesson-key"] = lesson_key_from_release_dt(release_dt)
    return release_dt


def refresh_page_markup(soup, default_release_dt=None):
    container = soup.find(id="lesson-container")
    if not container:
        return

    seen_keys = set()
    for lesson_tag in list(container.find_all("details", class_="daily-lesson")):
        release_dt = upgrade_lesson_markup(lesson_tag, default_release_dt=default_release_dt)
        lesson_key = lesson_tag.get("data-lesson-key")
        if lesson_key and lesson_key in seen_keys:
            lesson_tag.decompose()
            continue
        if lesson_key:
            seen_keys.add(lesson_key)

    lessons = container.find_all("details", class_="daily-lesson")
    for old_lesson in lessons[LESSON_LIMIT:]:
        old_lesson.decompose()


def parse_lesson_response(response):
    parsed = getattr(response, "parsed", None)
    if isinstance(parsed, dict):
        return parsed

    raw_text = extract_json_text(getattr(response, "text", "") or "")
    if not raw_text:
        raise ValueError("The model response was empty.")
    return json.loads(raw_text)


def validate_lesson_data(lesson_data, level):
    issues = []
    if not isinstance(lesson_data, dict):
        return ["The model response must be a JSON object."]

    all_strings = list(flatten_strings(lesson_data))
    for text in all_strings:
        if contains_markup(text):
            issues.append("All lesson fields must be plain text without HTML or angle brackets.")
            break

    title = normalize_text(str(lesson_data.get("title", "")))
    overview = normalize_text(str(lesson_data.get("overview", "")))
    topic = normalize_text(str(lesson_data.get("topic", "")))
    if not title:
        issues.append("The lesson title is missing.")
    if not overview:
        issues.append("The lesson overview is missing.")
    if not topic:
        issues.append("The lesson topic is missing.")

    sentences = lesson_data.get("news_brief_sentences")
    if not isinstance(sentences, list) or len(sentences) != level["sentence_count"]:
        issues.append(
            f"The News Brief must contain exactly {level['sentence_count']} sentences."
        )
        sentences = []

    normalized_sentences = []
    for sentence in sentences:
        if not isinstance(sentence, str) or not normalize_text(sentence):
            issues.append("Every News Brief sentence must be a non-empty string.")
            continue
        cleaned_sentence = normalize_text(sentence)
        normalized_sentences.append(cleaned_sentence)
        if not sentence_has_terminal_punctuation(cleaned_sentence):
            issues.append("Every News Brief sentence must end with normal sentence punctuation.")

    brief_text = " ".join(normalized_sentences)
    normalized_brief = normalize_for_match(brief_text)

    vocabulary = lesson_data.get("vocabulary")
    if not isinstance(vocabulary, list) or len(vocabulary) != level["vocabulary_count"]:
        issues.append(
            f"The vocabulary section must contain exactly {level['vocabulary_count']} terms."
        )
        vocabulary = []

    vocab_terms = []
    seen_terms = set()
    for item in vocabulary:
        if not isinstance(item, dict):
            issues.append("Each vocabulary entry must be an object.")
            continue
        term = normalize_text(str(item.get("term", "")))
        part_of_speech = normalize_text(str(item.get("part_of_speech", "")))
        definition = normalize_text(str(item.get("definition", "")))
        if not term or not part_of_speech or not definition:
            issues.append("Each vocabulary entry must include a term, part_of_speech, and definition.")
            continue
        normalized_term = normalize_for_match(term)
        if normalized_term in seen_terms:
            issues.append("Vocabulary terms must be unique.")
        seen_terms.add(normalized_term)
        vocab_terms.append(term)
        if normalized_term and normalized_term not in normalized_brief:
            issues.append(
                f"The vocabulary term '{term}' must appear in the News Brief exactly as written."
            )

    grammar = lesson_data.get("grammar")
    if not isinstance(grammar, dict):
        issues.append("The grammar section must be an object.")
        grammar = {}

    grammar_concept = normalize_text(str(grammar.get("concept", "")))
    grammar_explanation = normalize_text(str(grammar.get("explanation", "")))
    example_quote = normalize_text(str(grammar.get("example_quote", "")))
    if not grammar_concept or not grammar_explanation or not example_quote:
        issues.append("The grammar section must include concept, explanation, and example_quote.")
    elif brief_text and normalize_text(example_quote) not in brief_text:
        issues.append("The grammar example quote must come directly from the News Brief.")

    quiz = lesson_data.get("quiz")
    if not isinstance(quiz, list) or len(quiz) != level["quiz_count"]:
        issues.append(
            f"The quiz must contain exactly {level['quiz_count']} questions."
        )
        quiz = []

    for question in quiz:
        if not isinstance(question, dict):
            issues.append("Each quiz item must be an object.")
            continue

        prompt = normalize_text(str(question.get("question", "")))
        options = question.get("options")
        correct_index = question.get("correct_option_index")
        feedback = question.get("option_feedback")

        if not prompt:
            issues.append("Each quiz item must include a question.")
        if not isinstance(options, list) or len(options) != 3:
            issues.append("Each quiz question must have exactly three answer options.")
            continue
        if not isinstance(feedback, list) or len(feedback) != 3:
            issues.append("Each quiz question must include three aligned feedback strings.")
        if not isinstance(correct_index, int) or correct_index not in (0, 1, 2):
            issues.append("Each quiz question must have a correct_option_index between 0 and 2.")

        normalized_options = [normalize_text(str(option)) for option in options]
        if len(set(normalize_for_match(option) for option in normalized_options if option)) != 3:
            issues.append("Each quiz question must have three distinct answer options.")

        for option in normalized_options:
            if not option:
                issues.append("Quiz answer options cannot be empty.")

        if isinstance(feedback, list):
            for explanation in feedback:
                if not isinstance(explanation, str) or not normalize_text(explanation):
                    issues.append("Quiz feedback explanations cannot be empty.")
                    break

    return list(dict.fromkeys(issues))


def highlight_terms_in_text(text, terms):
    placeholder_map = {}
    result = text

    for term in sorted({normalize_text(term) for term in terms if normalize_text(term)}, key=len, reverse=True):
        pattern = re.compile(rf"(?<!\w){re.escape(term)}(?!\w)", re.IGNORECASE)

        def replacer(match):
            placeholder = f"__TERM_PLACEHOLDER_{len(placeholder_map)}__"
            placeholder_map[placeholder] = f"<strong>{html.escape(match.group(0))}</strong>"
            return placeholder

        result = pattern.sub(replacer, result)

    escaped = html.escape(result)
    for placeholder, rendered in placeholder_map.items():
        escaped = escaped.replace(placeholder, rendered)
    return escaped


def render_summary_html(title, release_dt):
    date_text = release_dt.strftime("%B %d, %Y")
    release_iso = (
        release_dt.astimezone(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    return (
        f'<summary class="lesson-date" data-release-iso="{release_iso}">'
        f'<span class="lesson-date-prefix">📅</span> '
        f'<span class="lesson-date-text">{html.escape(date_text)}</span> '
        f'<span class="lesson-age">{html.escape(format_elapsed_text(release_dt))}</span> '
        f'<span class="lesson-separator">-</span> '
        f'<span class="lesson-title-text">{html.escape(title)}</span>'
        f"</summary>"
    )


def render_quiz_question_html(question_number, item):
    option_labels = ["a", "b", "c"]
    buttons = []
    options = item["options"]
    feedback = item["option_feedback"]
    correct_index = item["correct_option_index"]

    for index, option_text in enumerate(options):
        is_correct = index == correct_index
        data_bg = "#e6ffe6" if is_correct else "#ffe6e6"
        data_color = "#2e8b57" if is_correct else "#b22222"
        feedback_prefix = "Correct: " if is_correct else "Incorrect: "
        feedback_text = feedback_prefix + normalize_text(feedback[index])
        buttons.append(
            (
                '<button type="button" '
                'style="text-align: left; padding: 10px; border: 1px solid var(--button-border); '
                'border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;" '
                f'data-bg="{data_bg}" data-color="{data_color}" '
                f'data-feedback="{html.escape(feedback_text, quote=True)}" '
                f'onclick="{SAFE_BUTTON_HANDLER}">'
                f"{option_labels[index]}) {html.escape(normalize_text(option_text))}"
                "</button>"
            )
        )

    return (
        '<div class="quiz-card">'
        '<div class="quiz-question" style="margin-bottom: 25px;">'
        f'<p style="font-weight: bold; color: var(--quiz-question); margin-bottom: 10px;">'
        f"{question_number}. {html.escape(normalize_text(item['question']))}</p>"
        '<div style="display: flex; flex-direction: column; gap: 8px;">'
        + "".join(buttons)
        + '</div>'
        '<div class="feedback" role="status" aria-live="polite" '
        'style="margin-top: 12px; font-size: 0.95em; min-height: 1.5em;"></div>'
        "</div>"
        "</div>"
    )


def render_lesson_html(lesson_data, level, release_dt):
    lesson_key = lesson_key_from_release_dt(release_dt)
    brief_sentences = [normalize_text(sentence) for sentence in lesson_data["news_brief_sentences"]]
    vocab_terms = [normalize_text(item["term"]) for item in lesson_data["vocabulary"]]
    brief_text = " ".join(brief_sentences)
    highlighted_brief = highlight_terms_in_text(brief_text, vocab_terms)

    vocab_lines = []
    for index, item in enumerate(lesson_data["vocabulary"], start=1):
        suffix = "<br/>" if index < len(lesson_data["vocabulary"]) else ""
        vocab_lines.append(
            f'<span class="vocab-term">{index}. {html.escape(normalize_text(item["term"]))} '
            f'({html.escape(normalize_text(item["part_of_speech"]))}):</span> '
            f'{html.escape(normalize_text(item["definition"]))}{suffix}'
        )

    grammar = lesson_data["grammar"]
    grammar_html = (
        f'<p><strong>{html.escape(level["grammar_label"])}: '
        f'{html.escape(normalize_text(grammar["concept"]))}</strong><br/>'
        f'{html.escape(normalize_text(grammar["explanation"]))}<br/>'
        f'Example from the text: "{html.escape(normalize_text(grammar["example_quote"]))}"</p>'
    )

    quiz_html = "".join(
        render_quiz_question_html(index, item)
        for index, item in enumerate(lesson_data["quiz"], start=1)
    )

    return (
        f'<details class="daily-lesson" data-lesson-key="{lesson_key}">'
        f"{render_summary_html(normalize_text(lesson_data['title']), release_dt)}"
        f'<div class="lesson-description">{html.escape(normalize_text(lesson_data["overview"]))}</div>'
        '<div class="lesson-content">'
        f'<div class="header"><h2>{html.escape(level["header_label"])}: '
        f'{html.escape(normalize_text(lesson_data["topic"]))}</h2></div>'
        '<div class="section">'
        '<h2>I. The News Brief</h2>'
        f"<p>{highlighted_brief}</p>"
        "</div>"
        '<div class="section">'
        '<h2>II. Vocabulary &amp; Grammar Focus</h2>'
        '<div class="vocab-box">'
        + "".join(vocab_lines)
        + "</div>"
        + grammar_html
        + "</div>"
        '<div class="section">'
        '<h2>III. Comprehension &amp; Mastery Quiz</h2>'
        '<p><em>Click on an option to check your answer.</em></p>'
        + quiz_html
        + "</div>"
        "</div>"
        "</details>"
    )


def generate_lesson_html(client, news_item, level, release_dt):
    revision_feedback = None
    issues = []

    for attempt in range(MAX_GENERATION_ATTEMPTS):
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=build_prompt(news_item, level, revision_feedback),
            config={
                "response_mime_type": "application/json",
                "response_json_schema": build_response_schema(level),
            },
        )

        try:
            lesson_data = parse_lesson_response(response)
        except (json.JSONDecodeError, ValueError) as exc:
            issues = [f"The model response was not valid JSON: {exc}"]
        else:
            issues = validate_lesson_data(lesson_data, level)
            if not issues:
                return render_lesson_html(lesson_data, level, release_dt)

        issue_lines = "\n".join(f"- {issue}" for issue in issues)
        revision_feedback = (
            "The previous draft failed validation. Rewrite the entire lesson from scratch and "
            f"fix every issue below:\n{issue_lines}"
        )
        print(
            f"Validation issues for {level['name'].lower()} lesson on attempt "
            f"{attempt + 1}: {'; '.join(issues)}"
        )

    raise RuntimeError(
        f"Could not generate a valid {level['name'].lower()} lesson after "
        f"{MAX_GENERATION_ATTEMPTS} attempts: {'; '.join(issues)}"
    )


def update_level_page(file_path, new_lesson_html, default_release_dt=None):
    page_path = Path(file_path)
    if not page_path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    with page_path.open("r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    container = soup.find(id="lesson-container")
    if not container:
        raise RuntimeError(f"Could not find <div id='lesson-container'> in {file_path}.")

    new_lesson_soup = BeautifulSoup(new_lesson_html, "html.parser")
    new_lesson_tag = new_lesson_soup.find("details", class_="daily-lesson")
    if not new_lesson_tag:
        snippet = new_lesson_html[:200].replace("\n", " ")
        raise RuntimeError(
            "Could not extract <details class='daily-lesson'> "
            f"from the rendered lesson for {file_path}. Snippet: {snippet}..."
        )

    empty_state = soup.find(id="empty-state")
    if empty_state:
        empty_state.decompose()

    container.insert(0, new_lesson_tag)
    refresh_page_markup(soup, default_release_dt=default_release_dt)

    with page_path.open("w", encoding="utf-8") as file:
        file.write(str(soup))

    print(f"Updated {file_path}.")


def refresh_existing_pages():
    for level in LEVELS:
        page_path = Path(level["file_path"])
        if not page_path.exists():
            raise FileNotFoundError(f"{level['file_path']} not found.")

        with page_path.open("r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        refresh_page_markup(soup)

        with page_path.open("w", encoding="utf-8") as file:
            file.write(str(soup))

        print(f"Refreshed lesson markup in {level['file_path']}.")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--refresh-pages",
        "--refresh-summaries",
        dest="refresh_pages",
        action="store_true",
        help="Normalize lesson markup, accessibility metadata, and dedupe archive entries without generating new lessons.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.refresh_pages:
        refresh_existing_pages()
        return

    print("Fetching news...")
    news_item = get_daily_news()
    client = configure_gemini()
    release_dt = datetime.now(timezone.utc)

    try:
        for level in LEVELS:
            print(f"Generating {level['name'].lower()} lesson...")
            lesson_html = generate_lesson_html(client, news_item, level, release_dt)
            print(f"Updating {level['file_path']}...")
            update_level_page(level["file_path"], lesson_html, default_release_dt=release_dt)
    finally:
        if hasattr(client, "close"):
            client.close()

    print("Finished updating all lesson pages.")


if __name__ == "__main__":
    main()
