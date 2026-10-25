"""Exercise the monitor without network, generation, or remote mutations."""
import base64
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

import daily_recovery as recovery

NOW = datetime(2026, 10, 6, 12, 0, tzinfo=timezone.utc)
RELEASE = "2026-10-06"


def edition(release=RELEASE):
    return json.dumps({"release_date": release, "levels": {
        level: {"lesson": {"editorial_check": {"status": "passed"},
                         "news_brief_sentences": ["A complete sentence."] * minimum,
                         "vocabulary": [{}] * minimum, "quiz": [{}] * minimum}}
        for level, minimum in recovery.LEVELS.items()}}).encode()


class FakeGitHub:
    def __init__(self, body=None, runs=None):
        self.body = body
        self.running = runs or []

    def archive(self, release):
        if release != RELEASE:
            raise AssertionError(release)
        return self.body

    def runs(self, now):
        return self.running


class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / "state.json"

    def check(self, github, now=NOW, apply=True, fetch=None):
        return recovery.check(now, github, self.path, apply, fetch or Mock(return_value=None))

    def test_missing_edition_requires_attention_without_dispatch(self):
        github = FakeGitHub()
        self.assertEqual("needs_attention", self.check(github)["status"])
        self.assertFalse(hasattr(github, "dispatch"))

    def test_read_only_check_never_writes_state(self):
        self.assertEqual("needs_attention", self.check(FakeGitHub(), apply=False)["status"])
        self.assertFalse(self.path.exists())

    def test_partial_saved_edition_requires_attention(self):
        for body in (b"unreadable", edition("2026-10-05"), b'{"release_date":"2026-10-06","levels":{}}'):
            self.assertEqual("needs_attention", self.check(FakeGitHub(body))["status"])

    def test_stale_saved_edition_gets_grace_then_requires_attention(self):
        github = FakeGitHub(edition())
        self.assertEqual("waiting_for_publishing", self.check(github)["status"])
        self.assertEqual("waiting_for_publishing",
                         self.check(github, NOW + timedelta(minutes=15))["status"])
        self.assertEqual("needs_attention",
                         self.check(github, NOW + timedelta(minutes=30))["status"])

    def test_active_offline_check_extends_publication_wait(self):
        github = FakeGitHub(edition(), [{"status": "in_progress"}])
        self.check(github)
        self.assertEqual("waiting_for_publishing",
                         self.check(github, NOW + timedelta(hours=1))["status"])

    def test_public_connection_failure_never_causes_mutation(self):
        github = FakeGitHub(edition())
        with self.assertRaises(recovery.ServiceUnavailable):
            self.check(github, fetch=Mock(side_effect=recovery.ServiceUnavailable("Unavailable")))

    def test_healthy_edition_requires_all_three_live_levels_and_indexes(self):
        body = edition()
        feed = json.dumps({level: {"url": f"news/{RELEASE}/{level}.html"}
                           for level in recovery.LEVELS}).encode()
        def fetch(path, now):
            if path.startswith("archive/lessons/"):
                return body
            if path == "lesson-data.json":
                return feed
            if path == "":
                return f'data-completion-story="news/{RELEASE}"'.encode()
            return f"news/{RELEASE}/beginner.html".encode()
        self.assertEqual("healthy", self.check(FakeGitHub(body), fetch=fetch)["status"])

    def test_monitor_waits_until_after_final_utc_attempt(self):
        for utc in (datetime(2026, 10, 6, 6, 44, tzinfo=timezone.utc),
                    datetime(2026, 12, 6, 8, 44, tzinfo=timezone.utc)):
            github = Mock()
            self.assertEqual("before_monitor_window", self.check(github, utc)["status"])
            github.archive.assert_not_called()

    def test_lock_prevents_overlapping_checks(self):
        with recovery.locked(self.path.with_suffix(".lock")) as acquired:
            self.assertTrue(acquired)
            with recovery.locked(self.path.with_suffix(".lock")) as second:
                self.assertFalse(second)


class ServiceBoundaryTests(unittest.TestCase):
    def test_only_a_confirmed_404_means_archive_absent(self):
        for error, missing in (("gh: Not Found (HTTP 404)", True),
                               ("gh: Bad credentials (HTTP 401)", False),
                               ("gh: unavailable (HTTP 500)", False)):
            github = recovery.GitHub(runner=Mock(return_value=SimpleNamespace(
                returncode=1, stderr=error, stdout="")))
            if missing:
                self.assertIsNone(github.archive(RELEASE))
            else:
                with self.assertRaises(recovery.ServiceUnavailable):
                    github.archive(RELEASE)

    def test_unrecognized_or_truncated_job_queue_stops_monitor(self):
        for data in ({"total_count": 101, "workflow_runs": []},
                     {"total_count": 1, "workflow_runs": [
                         {"head_branch": "main", "status": "unknown"}]}):
            github = recovery.GitHub(runner=Mock(return_value=SimpleNamespace(
                returncode=0, stdout=json.dumps(data))))
            with self.assertRaises(recovery.ServiceUnavailable):
                github.runs(NOW)

    def test_archive_decoding_and_size_boundary(self):
        record = {"type": "file", "encoding": "base64",
                  "content": base64.b64encode(edition()).decode()}
        github = recovery.GitHub(runner=Mock(return_value=SimpleNamespace(
            returncode=0, stdout=json.dumps(record))))
        self.assertEqual(edition(), github.archive(RELEASE))
        record["content"] = "invalid!?"
        github.runner.return_value.stdout = json.dumps(record)
        with self.assertRaises(recovery.ServiceUnavailable):
            github.archive(RELEASE)

    def test_timeout_never_exposes_diagnostics(self):
        github = recovery.GitHub(runner=Mock(side_effect=subprocess.TimeoutExpired("gh", 45)))
        with self.assertRaisesRegex(recovery.ServiceUnavailable, "could not be reached"):
            github.archive(RELEASE)


if __name__ == "__main__":
    unittest.main()
