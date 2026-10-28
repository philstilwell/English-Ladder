"""Pin all nightly producer opportunities to one New York edition date."""
from datetime import date, datetime, timedelta, timezone
from contextlib import redirect_stderr, redirect_stdout
import io
import unittest
from unittest.mock import patch
from zoneinfo import ZoneInfo

import daily_schedule as schedule


NEW_YORK = ZoneInfo("America/New_York")


class DailyScheduleTests(unittest.TestCase):
    def wait_with_fake_clock(self, start):
        current = start
        pauses = []
        messages = []

        def pause(seconds):
            nonlocal current
            pauses.append(seconds)
            current += timedelta(seconds=seconds)

        ready = schedule.wait_for_scheduled_start(
            clock=lambda: current, pause=pause, report=messages.append
        )
        self.assertTrue(all(0 < seconds <= 30 for seconds in pauses))
        return ready, pauses, messages

    def test_observed_early_dispatch_waits_before_resolving_next_edition(self):
        start = datetime(2026, 10, 27, 22, 26, 39, tzinfo=NEW_YORK)
        self.assertEqual(date(2026, 10, 27), schedule.scheduled_release_date(start))
        ready, pauses, messages = self.wait_with_fake_clock(start)
        self.assertEqual(datetime(2026, 10, 27, 22, 30, tzinfo=NEW_YORK), ready)
        self.assertEqual(201, sum(pauses))
        self.assertIn("America/New_York", messages[0])
        self.assertEqual(date(2026, 10, 28), schedule.scheduled_release_date(ready))

    def test_all_early_opportunities_wait_for_same_edition(self):
        for start in (
            datetime(2026, 10, 27, 22, 25, tzinfo=NEW_YORK),
            datetime(2026, 10, 27, 23, 25, tzinfo=NEW_YORK),
            datetime(2026, 10, 28, 0, 25, tzinfo=NEW_YORK),
        ):
            with self.subTest(start=start):
                ready, pauses, _ = self.wait_with_fake_clock(start)
                self.assertEqual(start + timedelta(minutes=5), ready)
                self.assertEqual(300, sum(pauses))
                self.assertEqual(date(2026, 10, 28), schedule.scheduled_release_date(ready))

    def test_late_nominal_and_daytime_invocations_do_not_wait(self):
        for start in (
            datetime(2026, 10, 27, 12, 0, tzinfo=NEW_YORK),
            datetime(2026, 10, 27, 22, 24, 59, tzinfo=NEW_YORK),
            datetime(2026, 10, 27, 22, 30, tzinfo=NEW_YORK),
            datetime(2026, 10, 27, 22, 34, tzinfo=NEW_YORK),
            datetime(2026, 10, 27, 23, 34, tzinfo=NEW_YORK),
            datetime(2026, 10, 28, 0, 33, tzinfo=NEW_YORK),
        ):
            with self.subTest(start=start):
                ready, pauses, messages = self.wait_with_fake_clock(start)
                self.assertEqual(start, ready)
                self.assertEqual([], pauses)
                self.assertEqual([], messages)

    def test_early_wait_uses_new_york_clock_across_dst_and_year_end(self):
        for day in (date(2026, 3, 7), date(2026, 3, 8),
                    date(2026, 10, 31), date(2026, 11, 1), date(2026, 12, 31)):
            for hour in (0, 22, 23):
                local = datetime(day.year, day.month, day.day, hour, 26, tzinfo=NEW_YORK)
                with self.subTest(local=local):
                    ready, pauses, _ = self.wait_with_fake_clock(local.astimezone(timezone.utc))
                    self.assertEqual(local.replace(minute=30), ready)
                    self.assertEqual(local.utcoffset(), ready.utcoffset())
                    self.assertEqual(240, sum(pauses))
                    expected = day + timedelta(days=hour >= 22)
                    self.assertEqual(expected, schedule.scheduled_release_date(ready))

    def test_cli_prints_only_ready_edition_on_stdout(self):
        ready = datetime(2026, 10, 27, 22, 30, tzinfo=NEW_YORK)

        def wait(**kwargs):
            kwargs["report"]("Early scheduled dispatch: waiting until 22:30.")
            return ready

        out, err = io.StringIO(), io.StringIO()
        with patch.object(schedule, "wait_for_scheduled_start", side_effect=wait), \
                redirect_stdout(out), redirect_stderr(err):
            self.assertEqual(0, schedule.main(["--wait-for-start"]))
        self.assertEqual("2026-10-28\n", out.getvalue())
        self.assertIn("waiting until 22:30", err.getvalue())

    def test_evening_and_after_midnight_attempts_share_one_release_date(self):
        cases = (
            (datetime(2026, 7, 10, 22, 29, tzinfo=NEW_YORK), date(2026, 7, 10)),
            (datetime(2026, 7, 10, 22, 30, tzinfo=NEW_YORK), date(2026, 7, 11)),
            (datetime(2026, 7, 10, 23, 30, tzinfo=NEW_YORK), date(2026, 7, 11)),
            (datetime(2026, 7, 11, 0, 30, tzinfo=NEW_YORK), date(2026, 7, 11)),
            (datetime(2026, 7, 11, 4, 0, tzinfo=NEW_YORK), date(2026, 7, 11)),
        )
        for now, expected in cases:
            with self.subTest(now=now):
                self.assertEqual(expected, schedule.scheduled_release_date(now))

    def test_monitor_waits_through_final_recovery_then_checks_until_next_cycle(self):
        for now in (datetime(2026, 7, 10, 22, 30, tzinfo=NEW_YORK),
                    datetime(2026, 7, 10, 23, 30, tzinfo=NEW_YORK),
                    datetime(2026, 7, 11, 0, 59, tzinfo=NEW_YORK)):
            self.assertFalse(schedule.monitoring_ready(now))
        for now in (datetime(2026, 7, 11, 1, 0, tzinfo=NEW_YORK),
                    datetime(2026, 7, 11, 22, 29, tzinfo=NEW_YORK)):
            self.assertTrue(schedule.monitoring_ready(now))

    def test_spring_and_fall_dst_transitions_keep_the_cycle_date(self):
        cases = (
            (datetime(2026, 3, 7, 22, 30, tzinfo=NEW_YORK), date(2026, 3, 8)),
            (datetime(2026, 3, 8, 0, 30, tzinfo=NEW_YORK), date(2026, 3, 8)),
            (datetime(2026, 3, 8, 3, 30, tzinfo=NEW_YORK), date(2026, 3, 8)),
            (datetime(2026, 10, 31, 22, 30, tzinfo=NEW_YORK), date(2026, 11, 1)),
            (datetime(2026, 11, 1, 0, 30, tzinfo=NEW_YORK), date(2026, 11, 1)),
            (datetime(2026, 11, 1, 1, 30, tzinfo=NEW_YORK, fold=0), date(2026, 11, 1)),
            (datetime(2026, 11, 1, 1, 30, tzinfo=NEW_YORK, fold=1), date(2026, 11, 1)),
        )
        for now, expected in cases:
            with self.subTest(now=now, fold=now.fold):
                self.assertEqual(expected, schedule.scheduled_release_date(now))

    def test_nominal_start_tracks_new_york_across_both_dst_transitions(self):
        cases = (
            (datetime(2026, 3, 7, 22, 30, tzinfo=NEW_YORK),
             datetime(2026, 3, 8, 3, 30, tzinfo=timezone.utc), timedelta(hours=-5)),
            (datetime(2026, 3, 8, 22, 30, tzinfo=NEW_YORK),
             datetime(2026, 3, 9, 2, 30, tzinfo=timezone.utc), timedelta(hours=-4)),
            (datetime(2026, 10, 31, 22, 30, tzinfo=NEW_YORK),
             datetime(2026, 11, 1, 2, 30, tzinfo=timezone.utc), timedelta(hours=-4)),
            (datetime(2026, 11, 1, 22, 30, tzinfo=NEW_YORK),
             datetime(2026, 11, 2, 3, 30, tzinfo=timezone.utc), timedelta(hours=-5)),
        )
        for local, expected_utc, expected_offset in cases:
            with self.subTest(local=local):
                self.assertEqual(expected_offset, local.utcoffset())
                self.assertEqual(expected_utc, local.astimezone(timezone.utc))

    def test_naive_clocks_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "time zone"):
            schedule.scheduled_release_date(datetime(2026, 7, 10, 22, 30))


if __name__ == "__main__":
    unittest.main()
