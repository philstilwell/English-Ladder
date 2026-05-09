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

LEVELS = [
    {
        "name": "Beginner",
        "file_path": "beginner.html",
        "cefr": "A1-A2",
        "header_label": "Beginner ESL",
        "overview_instruction": "Write the overview in one short and simple sentence.",
        "reading_instruction": (
            "Write 5 or 6 short sentences in clear, simple English. Use very easy "
            "vocabulary, short clauses, and direct meaning for CEFR A1-A2 learners."
        ),
        "vocabulary_instruction": (
            "Choose 4 useful words or short phrases from the news and define them in "
            "very simple English."
        ),
        "grammar_label": "Grammar Focus",
        "grammar_instruction": (
            "Choose one basic grammar point such as simple past, simple present, "
            "because, can, there is/there are, or basic comparatives. Explain it in "
            "simple English and give one example from the passage."
        ),
        "quiz_instruction": (
            "Make all 7 quiz questions short, direct, and easy to understand. Keep "
            "each answer choice brief and beginner-friendly."
        ),
    },
    {
        "name": "Intermediate",
        "file_path": "intermediate.html",
        "cefr": "B1-B2",
        "header_label": "Intermediate ESL",
        "overview_instruction": "Write the overview in one clear sentence.",
        "reading_instruction": (
            "Write 6 or 7 sentences using natural CEFR B1-B2 English. Add moderate "
            "detail, but keep the meaning easy to follow."
        ),
        "vocabulary_instruction": (
            "Choose 4 helpful words or phrases from the news and define them in clear "
            "everyday English for intermediate learners."
        ),
        "grammar_label": "Grammar Focus",
        "grammar_instruction": (
            "Choose one useful mid-level grammar point such as passive voice, relative "
            "clauses, present perfect, conditionals, or reporting verbs. Explain it "
            "clearly and give one example from the passage."
        ),
        "quiz_instruction": (
            "Make all 7 quiz questions thoughtful but readable for CEFR B1-B2 learners. "
            "Use short explanations in the feedback."
        ),
    },
    {
        "name": "Advanced",
        "file_path": "advanced.html",
        "cefr": "C1-Higher",
        "header_label": "Advanced ESL",
        "overview_instruction": "Write the overview in one polished sentence.",
        "reading_instruction": (
            "Write a formal summary using advanced vocabulary. The reading passage must "
            "be at least 7 sentences long."
        ),
        "vocabulary_instruction": (
            "Choose 4 advanced terms or phrases from the news and define them precisely."
        ),
        "grammar_label": "Advanced Grammar",
        "grammar_instruction": (
            "Choose one advanced grammar or style feature and explain it briefly with an "
            "example from the passage."
        ),
        "quiz_instruction": (
            "Make all 7 quiz questions appropriately challenging for advanced learners, "
            "with concise but specific feedback."
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


def build_prompt(news_text, level):
    today_str = datetime.now(timezone.utc).strftime("%B %d, %Y")

    return f"""
You are an ESL curriculum writer creating a lesson for CEFR {level["cefr"]} learners.

Use the following news:
{news_text}

Write a 3-part {level["name"].lower()} ESL lesson.
Return ONLY raw HTML. Do not add markdown fences. Do not add explanations before or after the HTML.
Wrap the entire lesson in a single <details class="daily-lesson"> tag.

Important requirements:
1. {level["overview_instruction"]}
2. {level["reading_instruction"]}
3. {level["vocabulary_instruction"]}
4. {level["grammar_instruction"]}
5. Section III must be an interactive 7-item multiple-choice quiz.
6. Use the exact inline structure shown below and do not alter onclick="checkAnswer(this)".
7. In each quiz-question div, randomize the position of the correct answer.
8. When writing data-feedback explanations, do not use double quotes inside the explanation text.
9. Do not provide a separate answer key section.
10. {level["quiz_instruction"]}

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
                <span class="vocab-term">1. [Term] (part of speech):</span> [Definition]<br>
                <span class="vocab-term">2. [Term] (part of speech):</span> [Definition]<br>
                <span class="vocab-term">3. [Term] (part of speech):</span> [Definition]<br>
                <span class="vocab-term">4. [Term] (part of speech):</span> [Definition]
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


def generate_lesson_html(model, news_text, level):
    response = model.generate_content(build_prompt(news_text, level))
    return extract_lesson_html(response.text)


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
