"""A receipt must use current scheduler evidence and never create a producer."""
from datetime import datetime, timezone
from pathlib import Path
import sqlite3
import tempfile
import unittest

import daily_registration as registration


class DailyRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.config_path = self.root / "automations" / registration.AUTOMATION_ID / "automation.toml"
        self.config_path.parent.mkdir(parents=True)
        self.config_path.write_text(
            f'id = "{registration.AUTOMATION_ID}"\n'
            'name = "English Ladder Daily Plan"\nkind = "cron"\nstatus = "ACTIVE"\n'
            f'rrule = "{registration.RECURRENCE}"\n'
            'execution_environment = "local"\nmodel = "gpt-6.1-sol"\nreasoning_effort = "high"\n'
            f'cwds = ["{registration.CHECKOUT}"]\n'
            f'prompt = "Read {registration.SKILL}; run {registration.GUARD}."\n'
            'target = { type = "project", project_id = "test-project" }\n'
        )
        self.database = self.root / "sqlite" / "codex-dev.db"
        self.database.parent.mkdir()
        self.connection = sqlite3.connect(self.database)
        self.addCleanup(self.connection.close)
        self.connection.execute(
            "CREATE TABLE automations (id TEXT, name TEXT, kind TEXT, prompt TEXT, status TEXT, "
            "rrule TEXT, execution_environment TEXT, project_id TEXT, model TEXT, "
            "reasoning_effort TEXT, next_run_at INTEGER, next_run_nominal_at INTEGER)"
        )
        self.connection.execute("INSERT INTO automations VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
            registration.AUTOMATION_ID, "English Ladder Daily Plan", "cron",
            f"Read {registration.SKILL}; run {registration.GUARD}.", "ACTIVE",
            registration.RECURRENCE, "local", "test-project", "gpt-6.1-sol", "high",
            1793240760000, 1793241000000))
        self.connection.commit()
        self.now = datetime(2026, 10, 28, 23, tzinfo=timezone.utc)

    def inspect(self, **kwargs):
        return registration.inspect_registration(self.root, now=self.now,
                                                 host_timezone=kwargs.get("zone", registration.TIME_ZONE))

    def test_actual_early_dispatch_receipt_and_no_database_changes(self):
        before = self.database.read_bytes()
        result = self.inspect()
        self.assertEqual("registered", result["status"])
        self.assertEqual("2026-10-28T22:26:00-04:00", result["next_dispatch"]["new_york"])
        self.assertEqual("2026-10-28T22:30:00-04:00", result["next_nominal_start"]["new_york"])
        self.assertEqual(-240, result["dispatch_offset_seconds"])
        self.assertEqual(before, self.database.read_bytes())
        self.assertNotIn("prompt", result["registration"])

    def test_wrong_mac_timezone_never_reports_registered(self):
        result = self.inspect(zone="America/Los_Angeles")
        self.assertEqual("needs_attention", result["status"])
        self.assertIn("Mac time zone", " ".join(result["problems"]))

    def test_duplicate_active_producer_is_reported(self):
        self.connection.execute("INSERT INTO automations SELECT 'duplicate', name, kind, prompt, "
                                "status, rrule, execution_environment, project_id, model, "
                                "reasoning_effort, next_run_at, next_run_nominal_at FROM automations")
        self.connection.commit()
        result = self.inspect()
        self.assertEqual("needs_attention", result["status"])
        self.assertEqual(2, len(result["active_producer_ids_in_scheduler"]))

    def test_missing_database_is_not_created(self):
        self.connection.close()
        self.database.unlink()
        result = self.inspect()
        self.assertEqual("needs_attention", result["status"])
        self.assertFalse(self.database.exists())

    def test_wrong_nominal_time_is_detected_even_when_registration_is_active(self):
        self.connection.execute("UPDATE automations SET next_run_at=?, next_run_nominal_at=?",
                                (1793230467000, 1793230200000))
        self.connection.commit()
        result = self.inspect()
        self.assertEqual("needs_attention", result["status"])
        self.assertIn("three New York opportunities", " ".join(result["problems"]))

    def test_stale_receipt_and_missing_nominal_time_are_not_success(self):
        self.now = datetime(2026, 10, 29, 4, tzinfo=timezone.utc)
        self.assertEqual("needs_attention", self.inspect()["status"])
        self.connection.execute("UPDATE automations SET next_run_nominal_at=NULL")
        self.connection.commit()
        self.assertEqual("needs_attention", self.inspect()["status"])

    def test_changed_scheduler_schema_is_unavailable_not_registered(self):
        self.connection.execute("DROP TABLE automations")
        self.connection.commit()
        result = self.inspect()
        self.assertEqual("needs_attention", result["status"])
        self.assertIn("evidence unavailable", " ".join(result["problems"]))

    def test_saved_configuration_and_scheduler_must_agree(self):
        self.connection.execute("UPDATE automations SET status='PAUSED'")
        self.connection.commit()
        self.assertEqual("needs_attention", self.inspect()["status"])

    def test_winter_nominal_start_retains_new_york_wall_clock(self):
        # After the November 1 clock change, 22:30 New York is 03:30 UTC.
        self.now = datetime(2026, 11, 1, 23, tzinfo=timezone.utc)
        nominal = int(datetime(2026, 11, 2, 3, 30, tzinfo=timezone.utc).timestamp() * 1000)
        self.connection.execute("UPDATE automations SET next_run_at=?, next_run_nominal_at=?",
                                (nominal, nominal))
        self.connection.commit()
        result = self.inspect()
        self.assertEqual("registered", result["status"])
        self.assertEqual("2026-11-01T22:30:00-05:00", result["next_nominal_start"]["new_york"])

    def test_scheduler_cannot_silently_skip_to_a_later_day(self):
        self.connection.execute("UPDATE automations SET next_run_at=next_run_at+172800000, "
                                "next_run_nominal_at=next_run_nominal_at+172800000")
        self.connection.commit()
        self.assertEqual("needs_attention", self.inspect()["status"])


if __name__ == "__main__":
    unittest.main()
