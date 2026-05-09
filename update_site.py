import os
import re
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import google.generativeai as genai
from bs4 import BeautifulSoup


MODEL_NAME = "gemini-2.5-flash"
LESSON_LIMIT = 7
NEWS_FEED_URL = "http://feeds.bbci.co.uk/news/world/rss.xml"
MAX_GENERATION_ATTEMPTS = 3

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
            "make sure those same 5 terms appear in bold font inside the News Brief."
        ),
        "grammar_label": "Grammar Focus",
        "grammar_instruction": (
            "Choose one basic grammar point such as simple past, simple present, "
            "because, can, there is/there are, or basic comparatives. Explain it in "
            "simple English only if that grammar point appears clearly in the News "
            "Brief at least twice. Include 'Example from the text:' followed by an "
            "exact quotation from the News Brief."
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
            "intermediate learners. Make sure those same 5 terms appear in bold font "
            "inside the News Brief."
        ),
        "grammar_label": "Grammar Focus",
        "grammar_instruction": (
            "Choose one useful mid-level grammar point such as passive voice, relative "
            "clauses, present perfect, conditionals, or reporting verbs. Explain it "
            "clearly only if that grammar point appears clearly in the News Brief at "
            "least twice. Include 'Example from the text:' followed by an exact "
            "quotation from the News Brief."
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
            "5 terms appear in bold font inside the News Brief."
        ),
        "grammar_label": "Advanced Grammar",
        "grammar_instruction": (
            "Choose one advanced grammar or style feature only if it appears clearly in "
            "the News Brief at least twice. Explain it briefly and include 'Example "
            "from the text:' followed by an exact quotation from the News Brief."
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
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def get_daily_news():
    feed = feedparser.parse(NEWS_FEED_URL)
    if not feed.entries:
        raise RuntimeError("No news found today.")

    top_entry = feed.entries[0]
    summary_html = getattr(top_entry, "description", "")
    clean_summary = BeautifulSoup(summary_html, "html.parser").get_text(" ", strip=True)
    return f"Title: {top_entry.title}\nSummary: {clean_summary}"


def build_prompt(news_text, level, revision_feedback=None):
    today_str = datetime.now(timezone.utc).strftime("%B %d, %Y")
    vocab_lines = []
    for index in range(1, level["vocabulary_count"] + 1):
        suffix = "<br>" if index < level["vocabulary_count"] else ""
        vocab_lines.append(
            f'                <span class="vocab-term">{index}. [Term] (part of speech):</span> [Definition]{suffix}'
        )
    vocab_html = "\n".join(vocab_lines)

    return f"""
You are an ESL curriculum writer creating a lesson for CEFR {level["cefr"]} learners.

Use the following news:
{news_text}

Write a 3-part {level["name"].lower()} ESL lesson.
Return ONLY raw HTML. Do not add markdown fences. Do not add explanations before or after the HTML.
Wrap the entire lesson in a single <details class="daily-lesson"> tag.

Important requirements:
1. {level["overview_instruction"]}
2. {level["difficulty_instruction"]}
3. {level["reading_instruction"]}
4. {level["vocabulary_instruction"]}
5. {level["grammar_instruction"]}
6. Section III must be an interactive {level["quiz_count"]}-item multiple-choice quiz.
7. The News Brief, vocabulary list, grammar point, and quiz must all match one another closely.
8. Every vocabulary term must appear naturally in the News Brief exactly as written in the vocabulary list.
9. Wrap every vocabulary term in <strong>...</strong> in the News Brief.
9. The grammar point must be clearly present in the News Brief, and the grammar explanation must quote exact words from the News Brief.
10. Every quiz question must be highly relevant to the News Brief, the vocabulary list, or the grammar explanation in this same lesson.
11. Do not use generic questions that could fit a different lesson.
12. Use the exact inline structure shown below and do not alter onclick="checkAnswer(this)".
13. In each quiz-question div, randomize the position of the correct answer.
14. When writing data-feedback explanations, do not use double quotes inside the explanation text.
15. Do not provide a separate answer key section.
16. {level["quiz_instruction"]}
17. The News Brief must contain exactly {level["sentence_count"]} sentences.
18. The vocabulary section must contain exactly {level["vocabulary_count"]} terms.
19. Before finalizing, silently check that every vocabulary term appears in bold in the News Brief, the grammar example is quoted from the News Brief, and the quiz count is correct.

Revision feedback:
{revision_feedback or "None. This is the first draft."}

Structure:
<details class="daily-lesson">
    <summary class="lesson-date">📅 {today_str} - [Catchy Title]</summary>
    <div class="lesson-description">[1-sentence overview]</div>
    <div class="lesson-content">
        <div class="header"><h2>{level["header_label"]}: [Topic]</h2></div>
        <div class="section">
            <h2>I. The News Brief</h2>
            <p>[News summary]</p>
        </div>
        <div class="section">
            <h2>II. Vocabulary & Grammar Focus</h2>
            <div class="vocab-box">
{vocab_html}
            </div>
            <p><strong>{level["grammar_label"]}: [Concept]</strong><br>[Brief explanation and example from the text]</p>
        </div>
        <div class="section">
            <h2>III. Comprehension & Mastery Quiz</h2>
            <p><em>Click on an option to check your answer.</em></p>
            <div class="quiz-card">
                <div class="quiz-question" style="margin-bottom: 25px;">
                    <p style="font-weight: bold; color: var(--quiz-question); margin-bottom: 10px;">[Question Number]. [Question Text]</p>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <button style="text-align: left; padding: 10px; border: 1px solid var(--button-border); border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;"
                                data-bg="#ffe6e6" data-color="#b22222" data-feedback="❌ <strong>Incorrect:</strong> [Explain why this option is wrong]"
                                onclick="checkAnswer(this)">
                            a) [Option A]
                        </button>
                        <button style="text-align: left; padding: 10px; border: 1px solid var(--button-border); border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;"
                                data-bg="#e6ffe6" data-color="#2e8b57" data-feedback="✅ <strong>Correct:</strong> [Explain why this option is right]"
                                onclick="checkAnswer(this)">
                            b) [Option B]
                        </button>
                        <button style="text-align: left; padding: 10px; border: 1px solid var(--button-border); border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;"
                                data-bg="#ffe6e6" data-color="#b22222" data-feedback="❌ <strong>Incorrect:</strong> [Explain why this option is wrong]"
                                onclick="checkAnswer(this)">
                            c) [Option C]
                        </button>
                    </div>
                    <div class="feedback" style="margin-top: 12px; font-size: 0.95em; min-height: 1.5em;"></div>
                </div>
            </div>
        </div>
    </div>
</details>
"""


def extract_lesson_html(raw_text):
    raw_html = raw_text.strip()
    backticks = "`" * 3
    match = re.search(
        fr"{backticks}(?:html)?\s*(.*?)\s*{backticks}",
        raw_html,
        re.DOTALL | re.IGNORECASE,
    )
    if match:
        return match.group(1).strip()
    return raw_html


def normalize_text(text):
    return re.sub(r"\s+", " ", text.strip())


def normalize_for_match(text):
    cleaned = re.sub(r"[^a-z0-9\s-]", " ", text.lower())
    return re.sub(r"\s+", " ", cleaned).strip()


def extract_vocab_terms(soup):
    terms = []
    for span in soup.find_all("span", class_="vocab-term"):
        label = span.get_text(" ", strip=True).split(":", 1)[0]
        label = re.sub(r"^\s*\d+\.\s*", "", label)
        label = re.sub(r"\s*\([^)]*\)\s*$", "", label)
        label = normalize_text(label)
        if label:
            terms.append(label)
    return terms


def extract_bold_terms(tag):
    if not tag:
        return []
    return [
        normalize_text(node.get_text(" ", strip=True))
        for node in tag.find_all(["strong", "b"])
        if normalize_text(node.get_text(" ", strip=True))
    ]


def extract_exact_quotes(text):
    return [
        normalize_text(match)
        for match in re.findall(r"[\"'“”‘’]([^\"'“”‘’]{6,220})[\"'“”‘’]", text)
    ]


def validate_generated_lesson(new_lesson_html, level):
    issues = []
    soup = BeautifulSoup(new_lesson_html, "html.parser")
    lesson_tag = soup.find("details", class_="daily-lesson")
    if not lesson_tag:
        return ["The lesson is missing the outer details.daily-lesson wrapper."]

    sections = lesson_tag.find_all("div", class_="section")
    if len(sections) < 3:
        issues.append("The lesson must contain all three main sections.")
        return issues

    brief_paragraph = sections[0].find("p")
    brief_text = normalize_text(brief_paragraph.get_text(" ", strip=True)) if brief_paragraph else ""
    if not brief_text:
        issues.append("The News Brief paragraph is missing.")
    else:
        sentence_count = len(
            [part for part in re.split(r"(?<=[.!?])\s+", brief_text) if part.strip()]
        )
        if sentence_count != level["sentence_count"]:
            issues.append(
                f"The News Brief must contain exactly {level['sentence_count']} sentences."
            )

    vocab_terms = extract_vocab_terms(sections[1])
    if len(vocab_terms) != level["vocabulary_count"]:
        issues.append(
            f"The vocabulary section must contain exactly {level['vocabulary_count']} terms."
        )

    normalized_brief = normalize_for_match(brief_text)
    bold_terms = {
        normalize_for_match(term)
        for term in extract_bold_terms(brief_paragraph)
        if normalize_for_match(term)
    }
    for term in vocab_terms:
        normalized_term = normalize_for_match(term)
        if normalized_term and normalized_term not in normalized_brief:
            issues.append(
                f"The vocabulary term '{term}' must appear in the News Brief exactly as written."
            )
        if normalized_term and normalized_term not in bold_terms:
            issues.append(
                f"The vocabulary term '{term}' must appear in bold in the News Brief."
            )

    grammar_paragraph = sections[1].find_all("p")
    grammar_text = normalize_text(grammar_paragraph[-1].get_text(" ", strip=True)) if grammar_paragraph else ""
    if "Example from the text:" not in grammar_text:
        issues.append("The grammar explanation must include 'Example from the text:'.")
    else:
        quotes = extract_exact_quotes(grammar_text)
        if not quotes:
            issues.append("The grammar explanation must include an exact quoted example from the News Brief.")
        elif brief_text and not any(normalize_text(quote) in brief_text for quote in quotes):
            issues.append("The quoted grammar example must come from the News Brief.")

    quiz_questions = lesson_tag.find_all("div", class_="quiz-question")
    if len(quiz_questions) != level["quiz_count"]:
        issues.append(
            f"The quiz must contain exactly {level['quiz_count']} questions."
        )
    for quiz_question in quiz_questions:
        buttons = quiz_question.find_all("button")
        if len(buttons) != 3:
            issues.append("Each quiz question must have exactly three answer options.")
            break

    return issues


def generate_lesson_html(model, news_text, level):
    revision_feedback = None
    issues = []

    for attempt in range(MAX_GENERATION_ATTEMPTS):
        response = model.generate_content(build_prompt(news_text, level, revision_feedback))
        lesson_html = extract_lesson_html(response.text)
        issues = validate_generated_lesson(lesson_html, level)
        if not issues:
            return lesson_html

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


def update_level_page(file_path, new_lesson_html):
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
            f"from the AI response for {file_path}. Snippet: {snippet}..."
        )

    empty_state = soup.find(id="empty-state")
    if empty_state:
        empty_state.decompose()

    new_summary = new_lesson_tag.find("summary", class_="lesson-date")
    new_summary_text = new_summary.get_text(" ", strip=True) if new_summary else None

    for existing in list(container.find_all("details", class_="daily-lesson")):
        existing_summary = existing.find("summary", class_="lesson-date")
        if (
            new_summary_text
            and existing_summary
            and existing_summary.get_text(" ", strip=True) == new_summary_text
        ):
            existing.decompose()

    container.insert(0, new_lesson_tag)

    lessons = container.find_all("details", class_="daily-lesson")
    for old_lesson in lessons[LESSON_LIMIT:]:
        old_lesson.decompose()

    with page_path.open("w", encoding="utf-8") as file:
        file.write(str(soup))

    print(f"Updated {file_path}.")


def main():
    print("Fetching news...")
    news = get_daily_news()
    model = configure_gemini()

    for level in LEVELS:
        print(f"Generating {level['name'].lower()} lesson...")
        lesson_html = generate_lesson_html(model, news, level)
        print(f"Updating {level['file_path']}...")
        update_level_page(level["file_path"], lesson_html)

    print("Finished updating all lesson pages.")


if __name__ == "__main__":
    main()
