"""Read-only, point-in-time receipt for the existing local daily producer.

This is a diagnostic command, never a scheduler or a generation entry point.
The desktop database is read through SQLite's read-only mode. Its internal
schema may change; unavailable evidence is an error, never proof of success.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import socket
import sqlite3
import tomllib
from zoneinfo import ZoneInfo

from daily_schedule import scheduled_release_date

AUTOMATION_ID = "english-ladder-daily-plan"
TIME_ZONE = "America/New_York"
RECURRENCE = "FREQ=DAILY;BYHOUR=0,22,23;BYMINUTE=30;BYSECOND=0"
CHECKOUT = "/Users/philstilwell/.local/share/EnglishLadder/English-Ladder"
GUARD = "daily_schedule.py --wait-for-start"
SKILL = "english-ladder-daily-producer/SKILL.md"


def system_timezone():
    resolved = str(Path("/etc/localtime").resolve())
    return resolved.split("/zoneinfo/", 1)[1] if "/zoneinfo/" in resolved else None


def stamp(milliseconds):
    if milliseconds is None:
        return None
    instant = datetime.fromtimestamp(milliseconds / 1000, timezone.utc)
    return {"epoch_ms": milliseconds, "utc": instant.isoformat(),
            "new_york": instant.astimezone(ZoneInfo(TIME_ZONE)).isoformat()}


def is_producer(record):
    return (record.get("id") == AUTOMATION_ID or
            (record.get("kind") == "cron" and
             (SKILL in record.get("prompt", "") or
              "plan_daily_runner.py" in record.get("prompt", ""))))


def inspect_registration(codex_dir, *, now=None, host_timezone=None):
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("The receipt clock must include a time zone.")
    codex_dir = Path(codex_dir)
    host_timezone = system_timezone() if host_timezone is None else host_timezone
    result = {"schema_version": 1, "observed_at": now.isoformat(),
              "scope": "Point-in-time local registration; not proof of a future run or publication.",
              "host": socket.gethostname(), "system_timezone": host_timezone,
              "required_timezone": TIME_ZONE, "automation_id": AUTOMATION_ID,
              "status": "needs_attention", "problems": []}
    problems = result["problems"]
    if host_timezone != TIME_ZONE:
        problems.append("The desktop local-time schedule requires the Mac time zone to be America/New_York.")
    try:
        saved = []
        for path in sorted((codex_dir / "automations").glob("*/automation.toml")):
            with path.open("rb") as stream:
                record = tomllib.load(stream)
            if is_producer(record):
                saved.append(record)
        active = [record for record in saved if record.get("status") == "ACTIVE"]
        result["active_producer_ids_in_configuration"] = [record["id"] for record in active]
        if len(active) != 1 or active[0]["id"] != AUTOMATION_ID:
            problems.append("Expected exactly one active saved daily producer with the existing ID.")
        config = next((record for record in saved if record["id"] == AUTOMATION_ID), None)
        if config is None:
            raise ValueError("Existing producer configuration is missing.")
        result["registration"] = {key: config.get(key) for key in (
            "id", "name", "kind", "status", "rrule", "execution_environment",
            "model", "reasoning_effort", "target", "cwds", "updated_at")}
        result["registration"]["prompt_sha256"] = hashlib.sha256(config["prompt"].encode()).hexdigest()
        result["registration"]["early_dispatch_guard_present"] = GUARD in config["prompt"]
        if config.get("rrule") != RECURRENCE:
            problems.append("Saved recurrence differs from the verified desktop local-time format.")
        if config.get("execution_environment") != "local" or CHECKOUT not in config.get("cwds", []):
            problems.append("Producer must use the existing stable local checkout.")
        if GUARD not in config["prompt"]:
            problems.append("Saved producer prompt is missing the early-dispatch wait.")

        db_path = codex_dir / "sqlite" / "codex-dev.db"
        connection = sqlite3.connect(db_path.resolve().as_uri() + "?mode=ro", uri=True)
        try:
            connection.row_factory = sqlite3.Row
            rows = [dict(row) for row in connection.execute(
                "SELECT id, name, kind, prompt, status, rrule, execution_environment, "
                "project_id, model, reasoning_effort, next_run_at, next_run_nominal_at "
                "FROM automations WHERE status != 'DELETED'")]
        finally:
            connection.close()
        active_rows = [row for row in rows if is_producer(row) and row["status"] == "ACTIVE"]
        result["active_producer_ids_in_scheduler"] = [row["id"] for row in active_rows]
        if len(active_rows) != 1 or active_rows[0]["id"] != AUTOMATION_ID:
            problems.append("Expected exactly one active daily producer in the desktop scheduler.")
        row = next((row for row in rows if row["id"] == AUTOMATION_ID), None)
        if row is None:
            raise ValueError("Existing producer has no scheduler record.")
        for key in ("status", "rrule", "execution_environment", "prompt", "model", "reasoning_effort"):
            if row[key] != config.get(key):
                problems.append(f"Saved configuration and scheduler disagree on {key}.")
        if row["project_id"] != config.get("target", {}).get("project_id"):
            problems.append("Saved configuration and scheduler disagree on the project.")
        result["next_dispatch"] = stamp(row["next_run_at"])
        result["next_nominal_start"] = stamp(row["next_run_nominal_at"])
        if row["next_run_at"] is None or row["next_run_nominal_at"] is None:
            problems.append("Scheduler has no complete next-run receipt.")
        else:
            nominal = datetime.fromtimestamp(row["next_run_nominal_at"] / 1000, ZoneInfo(TIME_ZONE))
            result["next_edition_date"] = scheduled_release_date(nominal).isoformat()
            if (nominal.hour not in (0, 22, 23) or nominal.minute != 30 or nominal.second != 0):
                problems.append("Next nominal start is not one of the three New York opportunities.")
            if nominal.timestamp() - now.timestamp() > 24 * 60 * 60:
                problems.append("Next nominal start is more than a day away despite the daily schedule.")
            if row["next_run_at"] <= now.timestamp() * 1000:
                problems.append("Recorded next dispatch is due or stale; refresh live scheduler evidence.")
            offset = (row["next_run_at"] - row["next_run_nominal_at"]) / 1000
            result["dispatch_offset_seconds"] = offset
            if abs(offset) > 300:
                problems.append("Next dispatch lies outside the verified five-minute scheduler window.")
    except (OSError, sqlite3.Error, ValueError, KeyError, TypeError) as error:
        problems.append(f"Registration evidence unavailable: {error}")
    if not problems:
        result["status"] = "registered"
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-dir", type=Path, default=Path.home() / ".codex")
    args = parser.parse_args(argv)
    result = inspect_registration(args.codex_dir)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "registered" else 1


if __name__ == "__main__":
    raise SystemExit(main())
