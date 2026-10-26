"""Exercise the monitor without network, generation, or remote mutations."""
import base64
from datetime import datetime, timedelta, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock
from zoneinfo import ZoneInfo

import daily_recovery as recovery

NOW = datetime(2026, 10, 6, 12, 0, tzinfo=timezone.utc)
RELEASE = "2026-10-06"


def edition(release=RELEASE):
    levels = {}
    for level, minimum in recovery.LEVELS.items():
        levels[level] = {"lesson": {
            "title": f"A complete {level} lesson", "overview": "A complete overview.",
            "editorial_check": {"status": "passed"},
            "news_brief_sentences": [f"Complete sentence {index}." for index in range(minimum)],
            "vocabulary": [{"term": f"term {index}", "part_of_speech": "noun",
                            "definition": f"Definition number {index}."}
                           for index in range(minimum)],
            "quiz": [{}] * minimum,
        }}
    return json.dumps({"release_date": release, "levels": levels}).encode()


def public_files(body):
    record = json.loads(body)
    files = {f"archive/lessons/{RELEASE}.json": body}
    digest = recovery.story_digest(record)
    image_path = f"assets/news/{RELEASE}-{digest[:12]}.webp"
    image = b"verified image bytes"
    files[f"assets/news/{RELEASE}.json"] = json.dumps({
        "status": "ready", "story_digest": digest, "path": image_path,
        "width": 1024, "height": 768, "sha256": hashlib.sha256(image).hexdigest(),
    }).encode()
    files[image_path] = image
    files["lesson-data.json"] = json.dumps({
        level: {"url": f"news/{RELEASE}/{level}.html"} for level in recovery.LEVELS
    }).encode()
    files[""] = f'data-completion-story="news/{RELEASE}"'.encode()
    for path in ("archive.html", *[f"{level}.html" for level in recovery.LEVELS]):
        files[path] = f"news/{RELEASE}/beginner.html".encode()
    for level in recovery.LEVELS:
        count = len(record["levels"][level]["lesson"]["vocabulary"])
        spans = []
        for index in range(count):
            translations = json.dumps({
                code: f"Translated {code} {index}" for code in recovery.LANGUAGES
            }, ensure_ascii=False)
            spans.append('<span class="vocab-definition" data-translations="' +
                         html.escape(translations, quote=True) + '">Definition</span>')
        files[f"news/{RELEASE}/{level}.html"] = (
            f"Lesson {RELEASE}" + "".join(spans)).encode()
    return files


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

    def check(self, github, now=NOW, apply=True, fetch=None, producer_is_active=None):
        return recovery.check(now, github, self.path, apply, fetch or Mock(return_value=None),
                              producer_is_active=producer_is_active)

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
        files = public_files(body)
        def fetch(path, now):
            return files.get(path)
        self.assertEqual("healthy", self.check(FakeGitHub(body), fetch=fetch)["status"])

    def test_healthy_requires_every_translation_and_matching_image(self):
        body = edition()
        complete = public_files(body)
        missing_translation = dict(complete)
        missing_translation[f"news/{RELEASE}/beginner.html"] = f"Lesson {RELEASE}".encode()
        self.assertEqual("waiting_for_publishing", self.check(
            FakeGitHub(body), fetch=lambda path, now: missing_translation.get(path))["status"])
        missing_image = dict(complete)
        missing_image.pop(f"assets/news/{RELEASE}.json")
        self.assertEqual("waiting_for_publishing", self.check(
            FakeGitHub(body), fetch=lambda path, now: missing_image.get(path))["status"])

    def test_active_local_producer_is_not_reported_as_failure(self):
        self.assertEqual("producer_running", self.check(
            FakeGitHub(), producer_is_active=lambda release: release == RELEASE)["status"])

    def test_timestamped_activity_marker_is_observed_without_opening_lock(self):
        root = Path(self.temporary.name) / "repository"
        marker = root / ".daily-agent" / RELEASE / "producer-active.json"
        marker.parent.mkdir(parents=True)
        marker.write_text("metadata content is deliberately not opened")
        os.utime(marker, (NOW.timestamp(), NOW.timestamp()))
        self.assertTrue(recovery.producer_running(root, RELEASE, NOW + timedelta(hours=5)))
        self.assertFalse(recovery.producer_running(root, RELEASE, NOW + timedelta(hours=7)))
        marker.unlink()
        self.assertFalse(recovery.producer_running(root, RELEASE, NOW))

    def test_recent_publication_handoff_is_active_but_stale_handoff_is_not(self):
        root = Path(self.temporary.name) / "repository"
        marker = root / ".daily-agent" / RELEASE / "publication-pending.json"
        marker.parent.mkdir(parents=True)
        marker.write_text("metadata content is deliberately not opened")
        os.utime(marker, (NOW.timestamp(), NOW.timestamp()))
        self.assertTrue(recovery.producer_running(root, RELEASE, NOW + timedelta(minutes=90)))
        self.assertFalse(recovery.producer_running(root, RELEASE, NOW + timedelta(hours=3)))

    def test_monitor_waits_until_one_am_new_york_after_final_attempt(self):
        new_york = ZoneInfo("America/New_York")
        for local in (datetime(2026, 7, 10, 22, 30, tzinfo=new_york),
                      datetime(2026, 7, 10, 23, 30, tzinfo=new_york),
                      datetime(2026, 7, 11, 0, 59, tzinfo=new_york)):
            github = Mock()
            self.assertEqual("before_monitor_window", self.check(github, local)["status"])
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
