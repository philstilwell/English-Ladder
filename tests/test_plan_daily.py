"""Boundaries for the ChatGPT-plan producer."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch
import contextlib
from datetime import date
import io

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

    def test_build_pins_cleanup_to_the_edition_date(self):
        edition = {"levels": {level: {"lesson": {}} for level in plan_daily.LEVEL_NAMES}}
        with patch.object(plan_daily, "load_json", return_value=edition), \
                patch.object(plan_daily, "translation_source", return_value={}), \
                patch.object(plan_daily, "read_record", return_value={"reviewed": True}), \
                patch.object(plan_daily, "image_for_lesson", return_value=Path("image.webp")), \
                patch.object(plan_daily.subprocess, "run") as run, \
                patch.object(plan_daily, "saved_edition_status", return_value=(True, "complete")):
            plan_daily.build_and_check("2026-10-26")
        self.assertEqual(
            [plan_daily.sys.executable, "update_site.py", "--refresh-pages", "--release-date", "2026-10-26"],
            run.call_args_list[0].args[0],
        )

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

    def test_existing_staged_image_is_reused_without_another_model_call(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            image = state / "image.png"
            image.write_bytes(b"already generated")
            with patch.object(plan_daily, "prepare_image", return_value=state / "image.prompt.txt"), \
                    patch.object(plan_daily_runner.subprocess, "run") as run:
                self.assertEqual(image, plan_daily_runner.model_image("codex", "2026-10-26", state))
            run.assert_not_called()

    def test_saved_translation_draft_and_review_are_imported_without_model_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "state"
            state.mkdir()
            lesson = {"news_brief_sentences": ["A complete sentence."],
                      "vocabulary": [{"term": "complete", "part_of_speech": "adjective",
                                      "definition": "Having every needed part."}]}
            archive = root / "archive/lessons/2026-10-26.json"
            archive.parent.mkdir(parents=True)
            archive.write_text('{"levels":{"beginner":{"lesson":' +
                               json.dumps(lesson) + '}}}')
            (state / "translation-draft-beginner.json").write_text("{}")
            (state / "translation-result-review-beginner.json").write_text("{}")
            with patch.object(plan_daily_runner, "ROOT", root), \
                    patch.object(plan_daily_runner, "read_record", return_value=None), \
                    patch.object(plan_daily_runner, "run_python") as run_python, \
                    patch.object(plan_daily_runner, "model_json") as model_json:
                plan_daily_runner.create_translation(
                    "codex", "2026-10-26", state, "beginner")
            model_json.assert_not_called()
            commands = [call.args[1] for call in run_python.call_args_list]
            self.assertEqual(["prepare-translation", "accept-translation-review"], commands)

    def test_transient_review_failure_reuses_structurally_valid_lesson(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            (state / "lesson-beginner.json").write_text("{}")
            calls = []

            def record_run(release, command, *args, **kwargs):
                calls.append(command)

            failure = subprocess.CalledProcessError(1, ["codex"])
            with patch.object(plan_daily_runner, "LEVELS", ("beginner",)), \
                    patch.object(plan_daily_runner, "run_python", side_effect=record_run), \
                    patch.object(plan_daily_runner, "model_json", side_effect=[failure, None]):
                plan_daily_runner.create_lessons("codex", "2026-10-26", state)
            self.assertNotIn("prepare-level", calls)
            self.assertNotIn("accept-draft", calls)
            self.assertEqual(2, calls.count("prepare-review"))
            self.assertIn("accept-review", calls)

    def test_producer_lock_serializes_overlapping_attempts(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "producer.lock"
            with plan_daily_runner.producer_lock(path) as acquired:
                self.assertTrue(acquired)
                self.assertTrue(path.with_name("producer-active.json").is_file())
                with plan_daily_runner.producer_lock(path) as second:
                    self.assertFalse(second)
            self.assertFalse(path.with_name("producer-active.json").exists())

    def test_already_running_exits_before_preflight_or_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            with plan_daily_runner.producer_lock(state / "producer.lock"):
                with patch.object(plan_daily_runner, "verify_free_space") as preflight, \
                        contextlib.redirect_stdout(io.StringIO()) as output:
                    result = plan_daily_runner.main([
                        "--date", "2026-10-26", "--state-dir", str(state)])
            self.assertEqual(0, result)
            self.assertEqual("already_running", json.loads(output.getvalue())["status"])
            preflight.assert_not_called()

    def test_publication_handoff_blocks_later_attempts_before_preflight(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            plan_daily.atomic_json(plan_daily_runner.publication_marker(state), {"release_date": "2026-10-26"})
            with patch.object(plan_daily_runner, "verify_free_space") as preflight, \
                    contextlib.redirect_stdout(io.StringIO()) as output:
                result = plan_daily_runner.main([
                    "--date", "2026-10-26", "--state-dir", str(state)])
            self.assertEqual(0, result)
            self.assertEqual("publication_pending", json.loads(output.getvalue())["status"])
            preflight.assert_not_called()

    def test_default_date_uses_the_new_york_cycle_resolver(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            plan_daily.atomic_json(plan_daily_runner.publication_marker(state), {"release_date": "2026-10-26"})
            with patch.object(plan_daily_runner, "scheduled_release_date", return_value=date(2026, 10, 26)), \
                    patch.object(plan_daily_runner, "verify_free_space") as preflight, \
                    contextlib.redirect_stdout(io.StringIO()) as output:
                result = plan_daily_runner.main(["--state-dir", str(state)])
            self.assertEqual(0, result)
            self.assertEqual("2026-10-26", json.loads(output.getvalue())["release_date"])
            preflight.assert_not_called()

    def test_publication_handoff_clears_only_after_live_verification(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            marker = plan_daily_runner.publication_marker(state)
            plan_daily.atomic_json(marker, {"release_date": "2026-10-26"})
            with patch.object(plan_daily_runner, "check_publication",
                              return_value=(False, "not live")):
                with self.assertRaisesRegex(RuntimeError, "not live"):
                    plan_daily_runner.finish_publication("2026-10-26", state)
            self.assertTrue(marker.exists())
            with patch.object(plan_daily_runner, "check_publication",
                              return_value=(True, "verified")):
                plan_daily_runner.finish_publication("2026-10-26", state)
            self.assertFalse(marker.exists())

    def test_image_provenance_does_not_claim_an_unexposed_model(self):
        self.assertIn("model not exposed", plan_daily.IMAGE_MODEL)


if __name__ == "__main__":
    unittest.main()
