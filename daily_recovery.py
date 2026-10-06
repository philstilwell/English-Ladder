"""Independent daily recovery, using the signed-in GitHub CLI and no AI APIs.

The macOS timer lives outside GitHub Actions. Read-only is the default; --apply
permits bounded recovery through the existing checked daily workflow.
"""
from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import fcntl
import hashlib
import json
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlencode
from zoneinfo import ZoneInfo

REPOSITORY = "philstilwell/English-Ladder"
WORKFLOW = "cron.yml"
LEVELS = {"beginner": 6, "intermediate": 8, "advanced": 10}
TIME_ZONE = ZoneInfo("America/New_York")
MAX_ATTEMPTS = 3
RETRY_INTERVAL = timedelta(hours=1)
PUBLISHING_GRACE = timedelta(minutes=30)
DEFAULT_STATE_DIR = Path.home() / "Documents/Codex/English-Ladder-daily-recovery/state"


class ServiceUnavailable(RuntimeError):
    """Unknown remote state must never be interpreted as a missing edition."""


class GitHub:
    def __init__(self, executable="gh", runner=subprocess.run):
        self.executable, self.runner = executable, runner

    def api(self, path, payload=None, missing_ok=False):
        command = [self.executable, "api", f"repos/{REPOSITORY}/{path}"]
        options = {"capture_output": True, "text": True, "timeout": 45}
        if payload is not None:
            command += ["--method", "POST", "--input", "-"]
            options["input"] = json.dumps(payload)
        try:
            response = self.runner(command, **options)
        except (OSError, subprocess.TimeoutExpired) as error:
            raise ServiceUnavailable("GitHub could not be reached; no recovery was started.") from error
        if response.returncode:
            if missing_ok and "(HTTP 404)" in response.stderr:
                return None
            # Never print command diagnostics, credentials, or untrusted response bodies.
            raise ServiceUnavailable("GitHub rejected the check; verify its connection and account access.")
        if not response.stdout.strip():
            return None
        try:
            return json.loads(response.stdout)
        except ValueError as error:
            raise ServiceUnavailable("GitHub returned unreadable data; no recovery was started.") from error

    def archive(self, release):
        record = self.api(f"contents/archive/lessons/{release}.json?ref=main", missing_ok=True)
        if record is None:
            return None
        try:
            if record.get("type") != "file" or record.get("encoding") != "base64":
                raise ValueError()
            body = base64.b64decode("".join(record["content"].split()), validate=True)
            if not body or len(body) > 2_000_000:
                raise ValueError()
            return body
        except (ValueError, KeyError, TypeError, AttributeError) as error:
            raise ServiceUnavailable("GitHub's saved edition could not be read safely.") from error

    def runs(self, now):
        since = (now.astimezone(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        query = urlencode({"branch": "main", "per_page": 100, "created": ">=" + since})
        result = self.api(f"actions/workflows/{WORKFLOW}/runs?{query}")
        if (not isinstance(result, dict) or not isinstance(result.get("workflow_runs"), list)
                or type(result.get("total_count")) is not int or result["total_count"] > 100):
            raise ServiceUnavailable("The daily job queue could not be checked completely.")
        runs = result["workflow_runs"]
        for run in runs:
            if (not isinstance(run, dict) or run.get("head_branch") != "main"
                    or run.get("status") not in {"queued", "in_progress", "waiting", "pending", "requested", "completed"}):
                raise ServiceUnavailable("The daily job queue returned an unknown state.")
        return runs

    def dispatch(self, release, kind):
        inputs = {"release_date": release}
        if kind == "publication":
            inputs.update(deploy_only=True, retry_publishing=True)
        self.api(f"actions/workflows/{WORKFLOW}/dispatches", {"ref": "main", "inputs": inputs})


def public_file(path, now, runner=subprocess.run):
    url = f"https://englishladder.com/{path}?daily-recovery={int(now.timestamp())}"
    try:
        result = runner(["/usr/bin/curl", "--silent", "--show-error", "--location",
                         "--max-time", "15", "--max-filesize", "3000000",
                         "--header", "Cache-Control: no-cache", "--write-out", "\n%{http_code}", url],
                        capture_output=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ServiceUnavailable("English Ladder could not be reached.") from error
    if result.returncode:
        raise ServiceUnavailable("English Ladder could not be reached.")
    body, separator, status = result.stdout.rpartition(b"\n")
    if not separator or status not in {b"200", b"404"}:
        raise ServiceUnavailable("English Ladder returned an unexpected response; no automatic action was taken.")
    return body if status == b"200" else None


def complete_archive(body, release):
    """A corrupt/partial saved file needs attention, not fresh paid generation."""
    try:
        edition = json.loads(body)
        if edition["release_date"] != release:
            return False
        for level, minimum in LEVELS.items():
            lesson = edition["levels"][level]["lesson"]
            if lesson["editorial_check"]["status"] != "passed":
                return False
            if any(len(lesson[field]) < minimum for field in ("news_brief_sentences", "vocabulary", "quiz")):
                return False
        return True
    except (ValueError, KeyError, TypeError):
        return False


def published(body, release, now, fetch=public_file):
    remote = fetch(f"archive/lessons/{release}.json", now)
    if remote is None or hashlib.sha256(remote).digest() != hashlib.sha256(body).digest():
        return False
    feed_body = fetch("lesson-data.json", now)
    if feed_body is None:
        return False
    try:
        feed = json.loads(feed_body)
        if any(feed[level]["url"] != f"news/{release}/{level}.html" for level in LEVELS):
            return False
    except (ValueError, KeyError, TypeError):
        return False
    homepage = fetch("", now)
    if homepage is None or f'data-completion-story="news/{release}"'.encode() not in homepage:
        return False
    for path in ("archive.html", *[f"{level}.html" for level in LEVELS]):
        page = fetch(path, now)
        if page is None or f"news/{release}/".encode() not in page:
            return False
    for level in LEVELS:
        page = fetch(f"news/{release}/{level}.html", now)
        if page is None or release.encode() not in page:
            return False
    return True


def read_state(path, release):
    if not path.exists():
        return {"version": 1, "release_date": release, "attempts": []}
    try:
        state = json.loads(path.read_text())
        if state.get("version") != 1 or not isinstance(state.get("attempts"), list):
            raise ValueError()
        # Validate before permitting any action, including a date rollover.
        datetime.fromisoformat(state["release_date"])
        for attempt in state["attempts"]:
            if attempt["kind"] not in {"generation", "publication"}:
                raise ValueError()
            if datetime.fromisoformat(attempt["at"]).tzinfo is None:
                raise ValueError()
        if state["release_date"] != release:
            return {"version": 1, "release_date": release, "attempts": []}
        return state
    except (ValueError, KeyError, TypeError, AttributeError) as error:
        raise ServiceUnavailable("Recovery state is unreadable; automatic retries are stopped.") from error


def save_state(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, prefix=".recovery-", delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(state, stream, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def check(now, github, state_path, apply=False, fetch=public_file):
    if now.tzinfo is None:
        raise ValueError("The recovery clock must have a time zone.")
    local = now.astimezone(TIME_ZONE)
    release = local.date().isoformat()
    result = {"release_date": release, "checked_at": now.isoformat(), "apply": apply}
    # Respect the overnight production window; after waking later in the day,
    # check the current date only, never pay to backfill yesterday automatically.
    if (local.hour, local.minute) < (2, 45):
        return {**result, "status": "before_recovery_window"}
    state = read_state(state_path, release)
    body = github.archive(release)
    if body is not None and not complete_archive(body, release):
        return {**result, "status": "needs_attention", "reason": "The saved edition is incomplete or unreviewed."}
    if body is not None and published(body, release, now, fetch):
        state.pop("stale_since", None)
        state["last_result"] = {**result, "status": "healthy"}
        if apply:
            save_state(state_path, state)
        return state["last_result"]
    if any(run["status"] != "completed" for run in github.runs(now)):
        return {**result, "status": "waiting_for_active_job"}
    kind = "generation" if body is None else "publication"
    if kind == "publication":
        fingerprint = hashlib.sha256(body).hexdigest()
        if state.get("expected_archive") != fingerprint:
            state.update(expected_archive=fingerprint, stale_since=now.isoformat())
        try:
            since = datetime.fromisoformat(state["stale_since"])
            if since.tzinfo is None:
                raise ValueError()
        except (KeyError, ValueError, TypeError) as error:
            raise ServiceUnavailable("The publishing recovery clock is unreadable.") from error
        if now - since < PUBLISHING_GRACE:
            if apply:
                save_state(state_path, state)
            return {**result, "status": "waiting_for_publishing", "kind": kind}
    attempts = [attempt for attempt in state["attempts"] if attempt["kind"] == kind]
    if len(attempts) >= MAX_ATTEMPTS:
        return {**result, "status": "needs_attention", "reason": f"The {MAX_ATTEMPTS} daily {kind} recovery attempts are exhausted."}
    if state["attempts"] and now - datetime.fromisoformat(state["attempts"][-1]["at"]) < RETRY_INTERVAL:
        return {**result, "status": "waiting_for_retry_interval", "kind": kind}
    if not apply:
        return {**result, "status": "would_start_recovery", "kind": kind}
    # Reserve BEFORE sending. A timeout after GitHub accepts the request consumes
    # an attempt and cannot cause another immediate request after a crash.
    state["attempts"].append({"at": now.isoformat(), "kind": kind, "status": "reserved"})
    save_state(state_path, state)
    github.dispatch(release, kind)
    state["attempts"][-1]["status"] = "requested"
    result.update(status="recovery_requested", kind=kind, attempt=len(attempts) + 1)
    state["last_result"] = result
    save_state(state_path, state)
    return result


@contextmanager
def locked(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            yield False
            return
        try:
            yield True
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Permit bounded automatic recovery; default is read-only.")
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE_DIR)
    parser.add_argument("--gh", default="gh", help="Absolute GitHub CLI path for the macOS timer.")
    parser.add_argument("--json", action="store_true", help="Print the result for a manual check.")
    args = parser.parse_args(argv)
    logger = logging.getLogger("daily-recovery")
    if args.apply:
        args.state_dir.mkdir(parents=True, exist_ok=True)
        handler = RotatingFileHandler(args.state_dir / "recovery.log", maxBytes=100_000, backupCount=2)
        handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    try:
        with locked(args.state_dir / "recovery.lock") as acquired:
            if not acquired:
                result = {"status": "another_check_is_running"}
            else:
                result = check(datetime.now(timezone.utc), GitHub(args.gh), args.state_dir / "state.json", args.apply)
    except (ServiceUnavailable, OSError) as error:
        result = {"status": "needs_attention", "reason": str(error), "checked_at": datetime.now(timezone.utc).isoformat()}
    if args.apply:
        logger.info(json.dumps(result))
        save_state(args.state_dir / "last-check.json", result)
    if args.json or not args.apply:
        print(json.dumps(result, indent=2))
    return 1 if result["status"] == "needs_attention" else 0


if __name__ == "__main__":
    raise SystemExit(main())
