"""New York production-cycle dates for the English Ladder daily edition."""
from __future__ import annotations

import argparse
from datetime import datetime, time, timedelta
import sys
from time import sleep
from zoneinfo import ZoneInfo

TIME_ZONE_NAME = "America/New_York"
TIME_ZONE = ZoneInfo(TIME_ZONE_NAME)
START_TIME = time(22, 30)
PRODUCER_TIMES = (time(0, 30), START_TIME, time(23, 30))
EARLY_DISPATCH_SECONDS = 5 * 60
FINAL_RECOVERY_TIME = time(0, 30)
MONITOR_TIME = time(1, 0)


def local_time(now=None):
    if now is None:
        return datetime.now(TIME_ZONE)
    if now.tzinfo is None:
        raise ValueError("The production clock must include a time zone.")
    return now.astimezone(TIME_ZONE)


def scheduled_release_date(now=None):
    """Pin 22:30/23:30 and the following 00:30 to one edition date."""
    local = local_time(now)
    released = local.date()
    if local.time().replace(tzinfo=None) >= START_TIME:
        released += timedelta(days=1)
    return released


def early_dispatch_target(now=None):
    """Recognize Codex's five-minute early-dispatch window in local wall time."""
    local = local_time(now)
    for clock in PRODUCER_TIMES:
        target = datetime.combine(local.date(), clock, tzinfo=TIME_ZONE)
        if 0 < (target - local).total_seconds() <= EARLY_DISPATCH_SECONDS:
            return target
    return None


def wait_for_scheduled_start(*, clock=local_time, pause=sleep, report=None):
    """Keep an early scheduled attempt alive until its nominal production time.

    Do this before resolving the edition or probing publication: at 22:26 an
    ordinary date lookup still correctly refers to the previous edition.
    Short waits leave the calling agent able to report progress. Manual daytime
    calls and late dispatches return immediately. No producer is started here.
    """
    now = local_time(clock())
    target = early_dispatch_target(now)
    if target is not None:
        while now < target:
            remaining = (target - now).total_seconds()
            if report is not None:
                report(f"Early scheduled dispatch: waiting {remaining:.0f}s until "
                       f"{target.isoformat()} ({TIME_ZONE_NAME}).")
            pause(min(30, remaining))
            now = local_time(clock())
    return now


def monitoring_ready(now=None):
    """Wait until 01:00 after the final 00:30 New York recovery opportunity."""
    clock = local_time(now).time().replace(tzinfo=None)
    return MONITOR_TIME <= clock < START_TIME


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wait-for-start", action="store_true",
                        help="Wait out an early scheduled dispatch before resolving the edition.")
    args = parser.parse_args(argv)
    now = (wait_for_scheduled_start(
        report=lambda message: print(message, file=sys.stderr, flush=True)
    ) if args.wait_for_start else local_time())
    print(scheduled_release_date(now).isoformat())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
