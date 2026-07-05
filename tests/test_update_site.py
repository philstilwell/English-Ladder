import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup

import update_site


def build_valid_lesson_data(title="Market Visit"):
    return {
        "title": title,
        "overview": "This lesson explains a short news-style report about a local market visit.",
        "topic": "A Local Market Visit",
        "news_brief_sentences": [
            "Maria saw a market near the station.",
            "The market opened early on Friday.",
            "A local guide greeted the visitors.",
            "The guide showed them fresh bread.",
            "Maria wrote notes about the prices.",
            "The prices were lower than last week.",
            "A friendly vendor explained each fruit.",
            "The visitors compared apples and oranges.",
            "Maria thanked the vendor before lunch.",
            "Everyone left with a clearer picture of the market.",
        ],
        "vocabulary": [
            {"term": "market", "part_of_speech": "noun", "definition": "a place where people buy and sell goods"},
            {"term": "station", "part_of_speech": "noun", "definition": "a place where trains or buses stop"},
            {"term": "guide", "part_of_speech": "noun", "definition": "a person who shows others around a place"},
            {"term": "prices", "part_of_speech": "noun", "definition": "the amounts of money needed to buy things"},
            {"term": "vendor", "part_of_speech": "noun", "definition": "a person who sells something"},
        ],
        "grammar": {
            "concept": "Comparatives",
            "explanation": "Comparatives help us compare two things, such as the prices this week and last week.",
            "example_quote": "The prices were lower than last week.",
        },
        "quiz": [
            {
                "question": f"What detail does question {index} test about the market visit?",
                "options": [
                    f"The correct fact for item {index}",
                    f"The wrong fact for item {index}",
                    f"Another wrong fact for item {index}",
                ],
                "correct_option_index": 0,
                "option_feedback": [
                    f"This option matches the market lesson for item {index}.",
                    f"This option does not match the market lesson for item {index}.",
                    f"This option also does not match the market lesson for item {index}.",
                ],
            }
            for index in range(1, 11)
        ],
    }


class UpdateSiteTests(unittest.TestCase):
    def test_validate_lesson_data_accepts_valid_fixture(self):
        issues = update_site.validate_lesson_data(build_valid_lesson_data(), update_site.LEVELS[0])
        self.assertEqual([], issues)

    def test_parse_summary_parts_supports_structured_markup(self):
        summary = BeautifulSoup(
            '<summary class="lesson-date" data-release-iso="2026-05-09T19:00:00Z">'
            '<span class="lesson-date-prefix">📅</span> '
            '<span class="lesson-date-text">May 09, 2026</span> '
            '<span class="lesson-age">[0 days, 9 hours old]</span> '
            '<span class="lesson-separator">-</span> '
            '<span class="lesson-title-text">Structured Title</span>'
            "</summary>",
            "html.parser",
        ).find("summary")

        date_text, title_text = update_site.parse_summary_parts(summary)
        self.assertEqual("May 09, 2026", date_text)
        self.assertEqual("Structured Title", title_text)

    def test_update_level_page_replaces_same_day_lesson(self):
        page_html = """<!DOCTYPE html><html><body><div id="lesson-container"></div></body></html>"""
        release_dt = datetime(2026, 5, 9, 19, 0, tzinfo=timezone.utc)

        first_html = update_site.render_lesson_html(
            build_valid_lesson_data("First Title"),
            update_site.LEVELS[0],
            release_dt,
        )
        second_html = update_site.render_lesson_html(
            build_valid_lesson_data("Second Title"),
            update_site.LEVELS[0],
            release_dt.replace(hour=20),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            page_path = Path(temp_dir) / "beginner.html"
            page_path.write_text(page_html, encoding="utf-8")

            update_site.update_level_page(page_path, first_html, default_release_dt=release_dt)
            update_site.update_level_page(page_path, second_html, default_release_dt=release_dt)

            soup = BeautifulSoup(page_path.read_text(encoding="utf-8"), "html.parser")
            lessons = soup.select("details.daily-lesson")
            self.assertEqual(1, len(lessons))
            self.assertEqual("2026-05-09", lessons[0]["data-lesson-key"])
            self.assertIn("Second Title", lessons[0].get_text(" ", strip=True))

    def test_render_lesson_html_randomizes_quiz_option_positions(self):
        release_dt = datetime(2026, 5, 9, 19, 0, tzinfo=timezone.utc)
        lesson_html = update_site.render_lesson_html(
            build_valid_lesson_data(),
            update_site.LEVELS[0],
            release_dt,
        )
        soup = BeautifulSoup(lesson_html, "html.parser")

        correct_positions = []
        for quiz_question in soup.select(".quiz-question"):
            buttons = quiz_question.find_all("button")
            for index, button in enumerate(buttons):
                if button["data-bg"] == "#e6ffe6":
                    correct_positions.append(index)
                    self.assertIn("The correct fact", button.get_text(" ", strip=True))
                    self.assertIn("This option matches", button["data-feedback"])

        self.assertEqual(10, len(correct_positions))
        self.assertGreater(len(set(correct_positions)), 1)
        self.assertNotIn("margin-bottom: 25px", lesson_html)
        self.assertNotIn("padding: 10px", lesson_html)
        self.assertIn("padding: 7px 10px", lesson_html)

    def test_render_lesson_html_strips_markdown_bold_markers(self):
        release_dt = datetime(2026, 5, 9, 19, 0, tzinfo=timezone.utc)
        lesson_data = build_valid_lesson_data()
        lesson_data["news_brief_sentences"][0] = "Maria saw a **market** near the station."

        lesson_html = update_site.render_lesson_html(
            lesson_data,
            update_site.LEVELS[0],
            release_dt,
        )
        soup = BeautifulSoup(lesson_html, "html.parser")
        news_brief = soup.select_one(".section p")

        self.assertIsNotNone(news_brief)
        self.assertNotIn("**", str(news_brief))
        self.assertIn("<strong>market</strong>", str(news_brief))

    def test_archive_daily_lessons_writes_all_levels_json(self):
        release_dt = datetime(2026, 5, 9, 19, 0, tzinfo=timezone.utc)
        news_item = {
            "title": "Source News Title",
            "summary": "A short source summary for the generated ESL lessons.",
            "link": "https://example.com/source-news",
        }
        level_lessons = {
            level["name"].lower(): build_valid_lesson_data(f"{level['name']} Title")
            for level in update_site.LEVELS
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            archive_dir = Path(temp_dir) / "archive" / "lessons"

            archive_path = update_site.archive_daily_lessons(
                news_item,
                level_lessons,
                release_dt,
                archive_dir=archive_dir,
            )

            self.assertEqual(archive_dir / "2026-05-09.json", archive_path)
            archive_data = json.loads(archive_path.read_text(encoding="utf-8"))

        self.assertEqual(update_site.ARCHIVE_SCHEMA_VERSION, archive_data["schema_version"])
        self.assertEqual("2026-05-09", archive_data["release_date"])
        self.assertEqual("2026-05-09T19:00:00Z", archive_data["release_iso"])
        self.assertEqual(update_site.MODEL_NAME, archive_data["model"])
        self.assertEqual(update_site.NEWS_SOURCE_NAME, archive_data["source"]["name"])
        self.assertEqual(update_site.NEWS_FEED_URL, archive_data["source"]["feed_url"])
        self.assertEqual("Source News Title", archive_data["source"]["title"])
        self.assertEqual(
            {"beginner", "intermediate", "advanced"},
            set(archive_data["levels"]),
        )
        self.assertEqual("Beginner Title", archive_data["levels"]["beginner"]["lesson"]["title"])
        self.assertEqual("Intermediate", archive_data["levels"]["intermediate"]["name"])
        self.assertEqual("C1-Higher", archive_data["levels"]["advanced"]["cefr"])

    def test_refresh_page_markup_dedupes_and_sanitizes_legacy_markup(self):
        page_html = """
        <!DOCTYPE html>
        <html><body>
        <div id="lesson-container">
          <details class="daily-lesson">
            <summary class="lesson-date">📅 May 09, 2026 - Legacy Title A</summary>
            <div class="quiz-question">
              <button onclick="checkAnswer(this)" data-feedback="✅ <strong>Correct:</strong> Nice work." data-color="#2e8b57"></button>
              <div class="feedback"></div>
            </div>
          </details>
          <details class="daily-lesson">
            <summary class="lesson-date">📅 May 09, 2026 - Legacy Title B</summary>
            <div class="quiz-question">
              <button onclick="checkAnswer(this)" data-feedback="❌ <strong>Incorrect:</strong> Try again." data-color="#b22222"></button>
              <div class="feedback"></div>
            </div>
          </details>
        </div>
        </body></html>
        """
        soup = BeautifulSoup(page_html, "html.parser")

        update_site.refresh_page_markup(soup)

        lessons = soup.select("details.daily-lesson")
        self.assertEqual(1, len(lessons))
        lesson = lessons[0]
        self.assertEqual("2026-05-09", lesson["data-lesson-key"])

        summary = lesson.find("summary", class_="lesson-date")
        self.assertIsNotNone(summary.get("data-release-iso"))
        self.assertIsNotNone(summary.find(class_="lesson-age"))

        button = lesson.find("button")
        self.assertEqual("button", button["type"])
        self.assertNotIn("<", button["data-feedback"])
        self.assertNotIn(">", button["data-feedback"])
        self.assertIn("padding: 7px 10px", button["style"])

        quiz_question = lesson.find("div", class_="quiz-question")
        self.assertEqual(update_site.QUIZ_QUESTION_STYLE, quiz_question["style"])

        feedback = lesson.find("div", class_="feedback")
        self.assertEqual("status", feedback["role"])
        self.assertEqual("polite", feedback["aria-live"])
        self.assertEqual(update_site.QUIZ_FEEDBACK_STYLE, feedback["style"])

    def test_refresh_page_markup_strips_markdown_around_existing_strong_terms(self):
        page_html = """
        <!DOCTYPE html>
        <html><body>
        <div id="lesson-container">
          <details class="daily-lesson">
            <summary class="lesson-date">📅 May 09, 2026 - Legacy Title</summary>
            <div class="section">
              <p>Maria saw a **<strong>market</strong>** near the station.</p>
            </div>
          </details>
        </div>
        </body></html>
        """
        soup = BeautifulSoup(page_html, "html.parser")

        update_site.refresh_page_markup(soup)

        news_brief = soup.select_one(".section p")
        self.assertIsNotNone(news_brief)
        self.assertNotIn("**", str(news_brief))
        self.assertIn("<strong>market</strong>", str(news_brief))


if __name__ == "__main__":
    unittest.main()
