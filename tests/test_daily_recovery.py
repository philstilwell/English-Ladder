"""Exercise recovery decisions without network, generation, or real dispatches."""
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
    def __init__(self, body=None, runs=None, failure=None):
        self.body = body
        self.running = runs or []
        self.failure = failure
        self.requests = []

    def archive(self, release):
        if release != RELEASE:
            raise AssertionError(release)
        return self.body

    def runs(self, now):
        return self.running

    def dispatch(self, release, kind):
        self.requests.append((release, kind))
        if self.failure:
            raise self.failure


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / "state.json"

    def check(self, github, now=NOW, apply=True, fetch=None):
        return recovery.check(now, github, self.path, apply, fetch or Mock(return_value=None))

    def test_missing_edition_starts_normal_workflow(self):
        github = FakeGitHub()
        result = self.check(github)
        self.assertEqual("recovery_requested", result["status"])
        self.assertEqual([(RELEASE, "generation")], github.requests)
        self.assertEqual("requested", json.loads(self.path.read_text())["attempts"][0]["status"])

    def test_read_only_never_dispatches_or_writes_state(self):
        github = FakeGitHub()
        self.assertEqual("would_start_recovery", self.check(github, apply=False)["status"])
        self.assertEqual([], github.requests)
        self.assertFalse(self.path.exists())

    def test_every_active_queue_state_prevents_another_run(self):
        for status in ("queued", "in_progress", "waiting", "pending", "requested"):
            with self.subTest(status=status):
                github = FakeGitHub(runs=[{"status": status}])
                self.assertEqual("waiting_for_active_job", self.check(github)["status"])
                self.assertEqual([], github.requests)

    def test_repeated_checks_observe_one_hour_spacing_and_daily_cap(self):
        github = FakeGitHub()
        for minutes, status in ((0, "recovery_requested"), (15, "waiting_for_retry_interval"),
                                (60, "recovery_requested"), (120, "recovery_requested"),
                                (180, "needs_attention")):
            self.assertEqual(status, self.check(github, NOW + timedelta(minutes=minutes))["status"])
        self.assertEqual(3, len(github.requests))

    def test_ambiguous_dispatch_failure_is_reserved_before_transmission(self):
        github = FakeGitHub(failure=recovery.ServiceUnavailable("Timeout after transmission"))
        with self.assertRaises(recovery.ServiceUnavailable):
            self.check(github)
        self.assertEqual("reserved", json.loads(self.path.read_text())["attempts"][0]["status"])
        github.failure = None
        self.assertEqual("waiting_for_retry_interval", self.check(github, NOW + timedelta(minutes=15))["status"])
        self.assertEqual(1, len(github.requests))

    def test_partial_saved_edition_never_starts_paid_generation(self):
        for body in (b"unreadable", edition("2026-10-05"), b'{"release_date":"2026-10-06","levels":{}}'):
            github = FakeGitHub(body)
            self.assertEqual("needs_attention", self.check(github)["status"])
            self.assertEqual([], github.requests)

    def test_stale_saved_edition_gets_grace_then_free_publication_retry(self):
        github = FakeGitHub(edition())
        self.assertEqual("waiting_for_publishing", self.check(github)["status"])
        self.assertEqual("waiting_for_publishing", self.check(github, NOW + timedelta(minutes=15))["status"])
        result = self.check(github, NOW + timedelta(minutes=30))
        self.assertEqual("publication", result["kind"])
        self.assertEqual([(RELEASE, "publication")], github.requests)

    def test_public_connection_failure_never_starts_paid_generation(self):
        github = FakeGitHub(edition())
        with self.assertRaises(recovery.ServiceUnavailable):
            self.check(github, fetch=Mock(side_effect=recovery.ServiceUnavailable("Unavailable")))
        self.assertEqual([], github.requests)

    def test_healthy_edition_requires_all_three_live_levels_and_indexes(self):
        body = edition()
        feed = json.dumps({level: {"url": f"news/{RELEASE}/{level}.html"} for level in recovery.LEVELS}).encode()
        def fetch(path, now):
            if path.startswith("archive/lessons/"):
                return body
            if path == "lesson-data.json":
                return feed
            if path == "":
                return f'data-completion-story="news/{RELEASE}"'.encode()
            return f"news/{RELEASE}/beginner.html".encode()
        github = FakeGitHub(body)
        self.assertEqual("healthy", self.check(github, fetch=fetch)["status"])
        self.assertEqual([], github.requests)
        def missing_advanced(path, now):
            return None if path == f"news/{RELEASE}/advanced.html" else fetch(path, now)
        self.assertEqual("waiting_for_publishing", self.check(github, fetch=missing_advanced)["status"])

    def test_corrupt_or_naive_state_stops_before_dispatch(self):
        for state in ({"version": 1, "release_date": RELEASE, "attempts": [{"kind": "generation", "at": "2026-10-06T12:00:00"}]},
                      {"version": 1, "release_date": RELEASE, "attempts": "broken"}):
            self.path.write_text(json.dumps(state))
            github = FakeGitHub()
            with self.assertRaises(recovery.ServiceUnavailable):
                self.check(github)
            self.assertEqual([], github.requests)

    def test_previous_date_attempts_do_not_exhaust_todays_allowance(self):
        recovery.save_state(self.path, {"version": 1, "release_date": "2026-10-05", "attempts": [
            {"kind": "generation", "at": "2026-10-05T12:00:00+00:00"} for _ in range(3)]})
        self.assertEqual("recovery_requested", self.check(FakeGitHub())["status"])
        self.assertEqual(1, len(json.loads(self.path.read_text())["attempts"]))

    def test_eastern_time_window_tracks_daylight_saving(self):
        for utc in (datetime(2026, 10, 6, 6, 44, tzinfo=timezone.utc),
                    datetime(2026, 12, 6, 7, 44, tzinfo=timezone.utc)):
            github = Mock()
            self.assertEqual("before_recovery_window", self.check(github, utc)["status"])
            github.archive.assert_not_called()

    def test_lock_prevents_overlapping_checks(self):
        with recovery.locked(self.path.with_suffix(".lock")) as acquired:
            self.assertTrue(acquired)
            with recovery.locked(self.path.with_suffix(".lock")) as second:
                self.assertFalse(second)


class ServiceBoundaryTests(unittest.TestCase):
    def test_only_a_confirmed_404_means_archive_absent(self):
        for error, missing in (("gh: Not Found (HTTP 404)", True), ("gh: Bad credentials (HTTP 401)", False),
                               ("gh: unavailable (HTTP 500)", False)):
            github = recovery.GitHub(runner=Mock(return_value=SimpleNamespace(returncode=1, stderr=error, stdout="")))
            if missing:
                self.assertIsNone(github.archive(RELEASE))
            else:
                with self.assertRaises(recovery.ServiceUnavailable):
                    github.archive(RELEASE)

    def test_dispatch_inputs_keep_publication_free(self):
        runner = Mock(return_value=SimpleNamespace(returncode=0, stdout="", stderr=""))
        github = recovery.GitHub("/opt/homebrew/bin/gh", runner)
        github.dispatch(RELEASE, "publication")
        payload = json.loads(runner.call_args.kwargs["input"])
        self.assertEqual({"ref": "main", "inputs": {"release_date": RELEASE, "deploy_only": True,
                                                     "retry_publishing": True}}, payload)
        github.dispatch(RELEASE, "generation")
        self.assertEqual({"release_date": RELEASE}, json.loads(runner.call_args.kwargs["input"])["inputs"])

    def test_unrecognized_or_truncated_job_queue_stops_recovery(self):
        for data in ({"total_count": 101, "workflow_runs": []},
                     {"total_count": 1, "workflow_runs": [{"head_branch": "main", "status": "unknown"}]}):
            github = recovery.GitHub(runner=Mock(return_value=SimpleNamespace(returncode=0, stdout=json.dumps(data))))
            with self.assertRaises(recovery.ServiceUnavailable):
                github.runs(NOW)

    def test_archive_decoding_and_size_boundary(self):
        record = {"type": "file", "encoding": "base64", "content": base64.b64encode(edition()).decode()}
        github = recovery.GitHub(runner=Mock(return_value=SimpleNamespace(returncode=0, stdout=json.dumps(record))))
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
