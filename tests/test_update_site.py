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

        feedback = lesson.find("div", class_="feedback")
        self.assertEqual("status", feedback["role"])
        self.assertEqual("polite", feedback["aria-live"])


if __name__ == "__main__":
    unittest.main()
