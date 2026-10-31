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
    def repair_fixture(self, state):
        edition = json.loads((ROOT / "tests/fixtures/reviewed-edition.json").read_text())
        lesson = edition["levels"]["beginner"]["lesson"]
        plan_daily.atomic_json(state / "source.json", edition["source"])
        plan_daily.atomic_json(state / "lesson-beginner.json", lesson)
        issues = ["The explanation stops before its thought is complete.",
                  "Level suitability failed (teaching_language): The grammar explanation is unfinished."]
        plan_daily.atomic_json(state / "issues-beginner.json", issues)
        plan_daily.atomic_json(state / "repair-scope-beginner.json", {
            "base_sha256": plan_daily.draft_digest(lesson),
            "issues_sha256": plan_daily.draft_digest(issues),
            "affected_sections": ["grammar"], "failed_checks": ["teaching_language"],
        })
        return lesson

    def test_isolated_grammar_repair_locks_every_other_section_and_requires_review(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            original = self.repair_fixture(state)
            plan_daily.prepare_level("2026-10-26", state, "beginner")
            schema = plan_daily.load_json(state / "draft-beginner.schema.json")
            self.assertEqual(["grammar"], schema["required"])
            self.assertEqual({"grammar"}, set(schema["properties"]))
            result = state / "repair.json"
            plan_daily.atomic_json(result, {"grammar": {
                "concept": "Simple present", "explanation": "Use the simple present to describe facts.",
                "example_sentence_index": 0}})
            with patch.object(plan_daily, "prepare_review") as review:
                plan_daily.accept_draft("2026-10-26", state, "beginner", result)
            saved = plan_daily.load_json(state / "lesson-beginner.json")
            for key in original:
                if key not in ("grammar", "editorial_check"):
                    self.assertEqual(original[key], saved[key], key)
            self.assertNotIn("editorial_check", saved)
            self.assertFalse((state / "approved-beginner.json").exists())
            review.assert_called_once()

    def test_repair_rejects_extra_sections_and_changed_base(self):
        for changed_base in (False, True):
            with self.subTest(changed_base=changed_base), tempfile.TemporaryDirectory() as directory:
                state = Path(directory)
                original = self.repair_fixture(state)
                plan_daily.prepare_level("2026-10-26", state, "beginner")
                result = state / "repair.json"
                plan_daily.atomic_json(result, {"grammar": original["grammar"], "quiz": []})
                if changed_base:
                    original["title"] = "Changed after repair preparation"
                    plan_daily.atomic_json(state / "lesson-beginner.json", original)
                with self.assertRaises(ValueError):
                    plan_daily.accept_draft("2026-10-26", state, "beginner", result)
                self.assertEqual(original, plan_daily.load_json(state / "lesson-beginner.json"))

    def test_editorial_routing_uses_explicit_scope_instead_of_feedback_wording(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            self.repair_fixture(state)
            plan_daily.prepare_level("2026-10-26", state, "beginner")
            self.assertEqual(["grammar"], plan_daily.load_json(
                state / "draft-beginner.schema.json")["required"])
            from teaching_typography import GUIDANCE
            self.assertIn(GUIDANCE, (state / "draft-beginner.prompt.txt").read_text())

    def test_mixed_editorial_issues_fall_back_to_complete_revision(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            self.repair_fixture(state)
            plan_daily.atomic_json(state / "issues-beginner.json", [
                "lesson.grammar.explanation is unfinished.", "Reading sentence 1 adds an unsupported name."])
            plan_daily.prepare_level("2026-10-26", state, "beginner")
            self.assertIn("reading", plan_daily.load_json(state / "draft-beginner.schema.json")["properties"])

    def test_truncated_explanation_is_rejected_locally_without_changing_it(self):
        with patch.object(plan_daily.update_site, "validate_lesson_data", return_value=[]):
            for text in ("Use the form to describe a possible result", "x" * 420, "x" * 421 + "."):
                lesson = {"grammar": {"explanation": text}}
                self.assertTrue(plan_daily.validate_plan_lesson(lesson, {}))
                self.assertEqual(text, lesson["grammar"]["explanation"])
            self.assertFalse(plan_daily.validate_plan_lesson(
                {"grammar": {"explanation": "Use this form for an unrealised possibility."}}, {}))

    def test_stale_unknown_or_mixed_scope_never_authorizes_grammar_only_repair(self):
        for change in ({"base_sha256": "stale"}, {"issues_sha256": "stale"},
                       {"affected_sections": ["grammar", "quiz"]},
                       {"affected_sections": ["unknown"]},
                       {"failed_checks": ["register"]}):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as directory:
                state = Path(directory)
                self.repair_fixture(state)
                path = state / "repair-scope-beginner.json"
                scope = plan_daily.load_json(path)
                scope.update(change)
                plan_daily.atomic_json(path, scope)
                plan_daily.prepare_level("2026-10-26", state, "beginner")
                self.assertIn("reading", plan_daily.load_json(
                    state / "draft-beginner.schema.json")["properties"])

    def test_review_scope_is_emitted_saved_and_cannot_override_failed_review(self):
        from review_fixtures import approved_review
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            self.repair_fixture(state)
            plan_daily.prepare_review("2026-10-26", state, "beginner")
            schema = plan_daily.load_json(state / "review-beginner.schema.json")
            self.assertIn("affected_sections", schema["required"])
            review = approved_review()
            review.update(approved=False, issues=["Finish the explanation."], affected_sections=["grammar"])
            review["level_checks"]["teaching_language"] = {
                "passed": False, "reason": "The explanation is incomplete."}
            path = state / "review.json"
            plan_daily.atomic_json(path, review)
            with self.assertRaises(ValueError):
                plan_daily.accept_review("2026-10-26", state, "beginner", path, 1)
            self.assertFalse((state / "approved-beginner.json").exists())
            plan_daily.prepare_level("2026-10-26", state, "beginner")
            self.assertEqual(["grammar"], plan_daily.load_json(
                state / "draft-beginner.schema.json")["required"])

    def test_invalid_or_conflicting_review_scope_is_rejected(self):
        for raw in ([], {"approved": True, "affected_sections": ["grammar"]},
                    {"approved": False, "affected_sections": []},
                    {"approved": False, "affected_sections": ["made_up"]},
                    {"approved": False, "affected_sections": ["grammar", "grammar"]}):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                plan_daily.validate_review_scope(raw)
        self.assertIsNone(plan_daily.validate_review_scope({"approved": False}))

    def test_local_fragment_check_routes_to_grammar_repair_without_editorial_prose(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            lesson = self.repair_fixture(state)
            lesson["grammar"]["explanation"] = "The result would be"
            level = plan_daily.level_config("beginner", state)
            issues = plan_daily.validate_plan_lesson(lesson, level)
            self.assertEqual(("grammar",), plan_daily.repair_fields(
                lesson, plan_daily.load_json(state / "source.json"), level, issues))

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

    def publication_fixture(self, root):
        state = root / 'state'
        state.mkdir()
        archive = root / 'archive/lessons/2026-10-26.json'
        archive.parent.mkdir(parents=True)
        archive.write_text('{"approved":true}')
        with patch.dict(os.environ, {"CODEX_THREAD_ID": "failed-chat"}):
            marker = plan_daily_runner.mark_publication_pending('2026-10-26', state, archive)
        return state, archive, marker

    def test_handoff_records_owner_and_pending_reports_it_without_generation(self):
        with tempfile.TemporaryDirectory() as directory:
            state, archive, marker = self.publication_fixture(Path(directory))
            self.assertEqual('failed-chat', json.loads(marker.read_text())['owner_thread_id'])
            with contextlib.redirect_stdout(io.StringIO()) as output, \
                    patch.object(plan_daily_runner, 'verify_free_space') as preflight:
                plan_daily_runner.main(['--date', '2026-10-26', '--state-dir', str(state)])
            self.assertEqual('failed-chat', json.loads(output.getvalue())['owner_thread_id'])
            preflight.assert_not_called()

    def test_failed_owner_recovery_preserves_content_and_cannot_call_models_or_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state, archive, marker = self.publication_fixture(root)
            original = archive.read_bytes()
            with patch.object(plan_daily_runner, 'ROOT', root), \
                    patch.dict(os.environ, {'CODEX_THREAD_ID': 'recovery-chat'}), \
                    patch.object(plan_daily_runner, 'saved_edition_status', return_value=(True, 'complete')), \
                    patch.object(plan_daily_runner, 'verify_free_space') as preflight, \
                    patch.object(plan_daily_runner, 'run_python') as build, \
                    patch.object(plan_daily_runner, 'model_json') as model, \
                    contextlib.redirect_stdout(io.StringIO()) as output:
                result = plan_daily_runner.main(['--date', '2026-10-26', '--state-dir', str(state),
                                                '--resume-publication-from', 'failed-chat'])
            self.assertEqual(0, result)
            self.assertEqual('ready_to_publish', json.loads(output.getvalue())['status'])
            self.assertEqual('recovery-chat', json.loads(marker.read_text())['owner_thread_id'])
            self.assertEqual(original, archive.read_bytes())
            for operation in (preflight, build, model):
                operation.assert_not_called()

    def test_concurrent_takeover_loser_cannot_replace_new_owner(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state, archive, marker = self.publication_fixture(root)
            with patch.object(plan_daily_runner, 'ROOT', root), \
                    patch.object(plan_daily_runner, 'saved_edition_status', return_value=(True, 'complete')):
                for owner in ('first-recovery', 'second-recovery'):
                    with patch.dict(os.environ, {'CODEX_THREAD_ID': owner}), \
                            plan_daily_runner.producer_lock(state / 'producer.lock'):
                        if owner == 'first-recovery':
                            plan_daily_runner.resume_publication('2026-10-26', state, 'failed-chat')
                        else:
                            with self.assertRaisesRegex(RuntimeError, 'owner changed'):
                                plan_daily_runner.resume_publication('2026-10-26', state, 'failed-chat')
            record = json.loads(marker.read_text())
            self.assertEqual('first-recovery', record['owner_thread_id'])
            self.assertEqual(1, len(record['ownership_transfers']))

    def test_recovery_rejects_changed_archive_incomplete_content_and_unknown_owner(self):
        for failure in ('changed archive', 'incomplete content', 'unknown owner'):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                state, archive, marker = self.publication_fixture(root)
                if failure == 'changed archive':
                    archive.write_text('{"changed":true}')
                if failure == 'unknown owner':
                    record = json.loads(marker.read_text()); record.pop('owner_thread_id')
                    plan_daily.atomic_json(marker, record)
                before = marker.read_bytes()
                with patch.object(plan_daily_runner, 'ROOT', root), \
                        patch.dict(os.environ, {'CODEX_THREAD_ID': 'recovery-chat'}), \
                        patch.object(plan_daily_runner, 'saved_edition_status',
                                     return_value=(failure != 'incomplete content', 'missing translations')):
                    with self.assertRaises(RuntimeError):
                        plan_daily_runner.resume_publication('2026-10-26', state, 'failed-chat')
                self.assertEqual(before, marker.read_bytes())

    def test_recovery_cannot_bypass_active_process_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            state, archive, marker = self.publication_fixture(Path(directory))
            with plan_daily_runner.producer_lock(state / 'producer.lock'), \
                    contextlib.redirect_stdout(io.StringIO()) as output, \
                    patch.object(plan_daily_runner, 'resume_publication') as resume:
                plan_daily_runner.main(['--date', '2026-10-26', '--state-dir', str(state),
                                        '--resume-publication-from', 'failed-chat'])
            self.assertEqual('already_running', json.loads(output.getvalue())['status'])
            resume.assert_not_called()

    def test_image_provenance_does_not_claim_an_unexposed_model(self):
        self.assertIn("model not exposed", plan_daily.IMAGE_MODEL)


if __name__ == "__main__":
    unittest.main()
