"""Boundaries for the ChatGPT-plan producer."""
import os
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import plan_daily
import plan_daily_runner


ROOT = Path(__file__).resolve().parents[1]


class PlanDailyTests(unittest.TestCase):
    def test_runner_strips_every_supported_model_api_key(self):
        values = {name: "must-not-leak" for name in plan_daily_runner.FORBIDDEN_ENV}
        with patch.dict(os.environ, values, clear=False):
            cleaned = plan_daily_runner.clean_environment()
        self.assertFalse(plan_daily_runner.FORBIDDEN_ENV & set(cleaned))

    def test_login_check_requires_chatgpt_authentication(self):
        with patch.object(plan_daily_runner.subprocess, "run", return_value=SimpleNamespace(
                returncode=0, stdout="Logged in using ChatGPT", stderr="")):
            plan_daily_runner.verify_chatgpt_login("codex")
        with patch.object(plan_daily_runner.subprocess, "run", return_value=SimpleNamespace(
                returncode=0, stdout="Logged in using an API key", stderr="")):
            with self.assertRaisesRegex(RuntimeError, "ChatGPT"):
                plan_daily_runner.verify_chatgpt_login("codex")

    def test_runner_stops_before_generation_when_disk_is_low(self):
        usage = SimpleNamespace(total=1_000, used=950, free=50)
        with patch.object(plan_daily_runner.shutil, "disk_usage", return_value=usage):
            with self.assertRaisesRegex(RuntimeError, "at least 512 MiB"):
                plan_daily_runner.verify_free_space()

    def test_model_modules_contain_no_api_client_or_fallback(self):
        for path in (ROOT / "plan_daily.py", ROOT / "plan_daily_runner.py"):
            source = path.read_text()
            for forbidden in ("google.genai", "from google import genai",
                              "api.openai.com", "generativelanguage.googleapis.com"):
                with self.subTest(path=path.name, forbidden=forbidden):
                    self.assertNotIn(forbidden, source)

    def test_review_request_can_be_built_without_a_client(self):
        lesson = {
            "title": "A clear title", "overview": "A clear overview for learners.",
            "topic": "A useful topic", "news_brief_sentences": ["Trees grow in cities."],
            "sentence_evidence": ["Trees grow in cities."], "vocabulary": [],
            "grammar": {"concept": "Simple present", "explanation": "Use it for facts.",
                        "example_quote": "Trees grow in cities."},
            "quiz": [], "discussion": ["Why do cities need trees?", "How can trees help?"]}
        news = {"title": "Trees", "summary": "Trees grow in cities.",
                "evidence_text": "Trees grow in cities."}
        level = dict(plan_daily.level_config("beginner"), min_sentence_count=1,
                     min_vocabulary_count=0, min_quiz_count=0)
        prompt, schema = plan_daily.review_lesson(
            None, news, lesson, level, plan_daily.MODEL, return_request=True)
        self.assertIn("Review an English lesson", prompt)
        self.assertEqual({"approved", "issues", "level_checks"},
                         set(schema["properties"]))


if __name__ == "__main__":
    unittest.main()
