"""Pin all nightly producer opportunities to one New York edition date."""
from datetime import date, datetime, timedelta, timezone
import unittest
from zoneinfo import ZoneInfo

import daily_schedule as schedule


NEW_YORK = ZoneInfo("America/New_York")


class DailyScheduleTests(unittest.TestCase):
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
