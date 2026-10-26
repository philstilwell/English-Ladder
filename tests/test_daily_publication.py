"""Prove that the daily shortcut preserves incomplete-content recovery."""
import contextlib
from datetime import date
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

import daily_publication as publication
from daily_images import image_paths, story_digest
from vocabulary_translations import LANGUAGES, source_data, source_key

DATE = "2026-10-20"


class DailyPublicationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for day in ("2026-10-18", "2026-10-19", DATE):
            levels = {}
            for level in publication.LEVELS:
                lesson = {"title": f"{day} {level}", "overview": "A complete story.",
                          "news_brief_sentences": [f"A story for {day} and {level}."],
                          "vocabulary": [{"term": "story", "part_of_speech": "noun", "definition": "An account."}]}
                levels[level] = {"lesson": lesson, "file_path": f"news/{day}/{level}.html"}
                source = source_data(lesson, level)
                definitions = {code: "翻訳" if code in ("ja", "zh-Hans") else "번역" if code == "ko"
                               else "Définition traduite" for code in LANGUAGES}
                self.write(f"data/vocabulary-translations/{source_key(source)}.json",
                           {"source": source, "review": {"status": "reviewed"},
                            "entries": [{"id": 0, **definitions}]})
                self.write(f"news/{day}/{level}.html", f"Lesson {day}")
            edition = {"release_date": day, "levels": levels}
            self.write(f"archive/lessons/{day}.json", edition)
            if day == DATE:
                self.edition = edition
        meta_path, image_path = image_paths(self.edition, self.root)
        image_path.parent.mkdir(parents=True, exist_ok=True)
        image_path.write_bytes(b"saved test illustration")
        self.image = image_path
        self.write(str(meta_path.relative_to(self.root)), {
            "status": "ready", "story_digest": story_digest(self.edition),
            "path": str(image_path.relative_to(self.root)), "width": 1024, "height": 768,
            "alt": "A conceptual illustration.",
            "sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
        })

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) if isinstance(value, dict) else value)

    def test_complete_live_edition_skips_rebuilding(self):
        run = Mock(return_value=subprocess.CompletedProcess([], 0))
        with patch.object(publication, "node_executable", return_value="/supported/node"):
            ready, reason = publication.check_publication(self.root, DATE, run)
        self.assertTrue(ready, reason)
        run.assert_called_once()
        self.assertEqual(run.call_args.args[0],
                         ["/supported/node", "cloudflare/check-daily-publication.cjs", DATE])
        self.assertEqual(run.call_args.kwargs["timeout"], 120)

    def test_node_resolution_supports_minimal_scheduled_path(self):
        with patch.dict(os.environ, {"PATH": ""}, clear=False), \
                patch.object(publication, "CHATGPT_NODE", Path("/scheduled/node")), \
                patch.object(publication.Path, "is_file", autospec=True,
                             side_effect=lambda path: str(path) == "/scheduled/node"):
            self.assertEqual("/scheduled/node", publication.node_executable())

    def test_missing_edition_does_not_probe_network_or_claim_success(self):
        (self.root / f"archive/lessons/{DATE}.json").unlink()
        run = Mock()
        self.assertFalse(publication.check_publication(self.root, DATE, run)[0])
        run.assert_not_called()

    def test_missing_level_keeps_recovery_enabled(self):
        del self.edition["levels"]["advanced"]
        self.write(f"archive/lessons/{DATE}.json", self.edition)
        self.assertFalse(publication.saved_edition_status(self.root, DATE)[0])

    def test_missing_rendered_page_keeps_recovery_enabled(self):
        (self.root / f"news/{DATE}/advanced.html").unlink()
        self.assertFalse(publication.saved_edition_status(self.root, DATE)[0])

    def test_wrong_archive_date_is_not_accepted(self):
        self.edition["release_date"] = "2026-10-19"
        self.write(f"archive/lessons/{DATE}.json", self.edition)
        self.assertFalse(publication.saved_edition_status(self.root, DATE)[0])

    def test_corrupt_illustration_keeps_recovery_enabled(self):
        self.image.write_bytes(b"broken")
        ready, reason = publication.saved_edition_status(self.root, DATE)
        self.assertFalse(ready)
        self.assertIn("illustration", reason)

    def test_incomplete_recent_translations_keep_recovery_enabled(self):
        edition = json.loads((self.root / "archive/lessons/2026-10-18.json").read_text())
        source = source_data(edition["levels"]["advanced"]["lesson"], "advanced")
        (self.root / f"data/vocabulary-translations/{source_key(source)}.json").unlink()
        ready, reason = publication.saved_edition_status(self.root, DATE)
        self.assertFalse(ready)
        self.assertIn("2026-10-18/advanced", reason)

    def test_unsuccessful_or_timed_out_probe_never_skips_recovery(self):
        for run in (Mock(return_value=subprocess.CompletedProcess([], 1)),
                    Mock(side_effect=subprocess.TimeoutExpired("node", 120)),
                    Mock(side_effect=OSError("missing executable"))):
            with self.subTest(run=run):
                with patch.object(publication, "node_executable", return_value="/supported/node"):
                    self.assertFalse(publication.check_publication(self.root, DATE, run)[0])

    def test_verification_only_fails_without_generating_or_sending(self):
        output = self.root / "outputs"
        with patch.object(publication, "ROOT", self.root), \
                patch.object(publication, "check_publication", return_value=(False, "Missing edition")) as probe, \
                patch.object(publication.subprocess, "check_output", return_value="test-revision\n"), \
                patch.dict(os.environ, {"GITHUB_OUTPUT": str(output), "GITHUB_STEP_SUMMARY": ""}), \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(1, publication.main(["--date", DATE, "--require-published"]))
        probe.assert_called_once_with(self.root, DATE)
        self.assertIn(f"release_date={DATE}", output.read_text())
        self.assertIn("already_published=false", output.read_text())

    def test_default_date_uses_the_new_york_cycle_resolver(self):
        with patch.object(publication, "ROOT", self.root), \
                patch.object(publication, "scheduled_release_date", return_value=date.fromisoformat(DATE)), \
                patch.object(publication, "check_publication", return_value=(True, "Verified")) as probe, \
                patch.object(publication.subprocess, "check_output", return_value="test-revision\n"), \
                contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(0, publication.main([]))
        probe.assert_called_once_with(self.root, DATE)
        self.assertEqual(DATE, json.loads(output.getvalue())["release_date"])


if __name__ == "__main__":
    unittest.main()
