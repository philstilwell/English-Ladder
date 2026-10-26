"""New York production-cycle dates for the English Ladder daily edition."""
from __future__ import annotations

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

TIME_ZONE_NAME = "America/New_York"
TIME_ZONE = ZoneInfo(TIME_ZONE_NAME)
START_TIME = time(22, 30)
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


def monitoring_ready(now=None):
    """Wait until 01:00 after the final 00:30 New York recovery opportunity."""
    clock = local_time(now).time().replace(tzinfo=None)
    return MONITOR_TIME <= clock < START_TIME
