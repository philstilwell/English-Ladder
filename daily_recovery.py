"""Independent read-only monitor for the plan-authenticated daily producer.

The macOS timer lives outside GitHub Actions. It checks repository and public
state, records a local health result, and never dispatches generation or changes
remote state. The scheduled Codex task is the only daily producer.
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
from html.parser import HTMLParser
import os
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlencode

REPOSITORY = "philstilwell/English-Ladder"
WORKFLOW = "cron.yml"
LEVELS = {"beginner": 6, "intermediate": 8, "advanced": 10}
LANGUAGES = ("ja", "ko", "zh-Hans", "es", "pt-BR", "fr", "de")
PUBLISHING_GRACE = timedelta(minutes=30)
PUBLICATION_HANDOFF_GRACE = timedelta(hours=2)
MONITOR_HOUR_UTC = 8
MONITOR_MINUTE_UTC = 45
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


class TranslationParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.entries = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = set(attributes.get("class", "").split())
        if tag == "span" and "vocab-definition" in classes:
            self.entries.append(attributes.get("data-translations"))


def valid_page_translations(body, expected_count):
    """Validate the seven-language objects users receive inside the live HTML."""
    try:
        parser = TranslationParser()
        parser.feed(body.decode("utf-8"))
        parser.close()
        if len(parser.entries) != expected_count:
            return False
        for raw in parser.entries:
            translations = json.loads(raw)
            if (set(translations) != set(LANGUAGES)
                    or any(not isinstance(translations[code], str) or not translations[code].strip()
                           for code in LANGUAGES)):
                return False
        return True
    except (UnicodeDecodeError, ValueError, TypeError, AttributeError):
        return False


def story_digest(edition):
    lesson = edition["levels"]["beginner"]["lesson"]
    context = {"source": edition.get("source", {}), "title": lesson["title"],
               "overview": lesson["overview"], "reading": lesson.get("news_brief_sentences", [])}
    return hashlib.sha256(json.dumps(context, sort_keys=True).encode()).hexdigest()


def valid_image(edition, release, now, fetch):
    metadata_body = fetch(f"assets/news/{release}.json", now)
    if metadata_body is None:
        return False
    try:
        metadata = json.loads(metadata_body)
        digest = story_digest(edition)
        expected_path = f"assets/news/{release}-{digest[:12]}.webp"
        if (metadata.get("status") != "ready" or metadata.get("story_digest") != digest
                or metadata.get("path") != expected_path
                or any(type(metadata.get(key)) is not int or not 512 <= metadata[key] <= 1600
                       for key in ("width", "height"))):
            return False
        image = fetch(expected_path, now)
        return image is not None and hashlib.sha256(image).hexdigest() == metadata.get("sha256")
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


def published(body, release, now, fetch=public_file):
    remote = fetch(f"archive/lessons/{release}.json", now)
    if remote is None or hashlib.sha256(remote).digest() != hashlib.sha256(body).digest():
        return False
    try:
        edition = json.loads(body)
        if not valid_image(edition, release, now, fetch):
            return False
    except (ValueError, KeyError, TypeError, AttributeError):
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
        expected = len(edition["levels"][level]["lesson"]["vocabulary"])
        if (page is None or release.encode() not in page
                or not valid_page_translations(page, expected)):
            return False
    return True


def producer_running(root, release, now=None):
    """Read the producer lock/handoff without creating state or signalling work."""
    if root is None:
        return False
    state = Path(root) / ".daily-agent" / release
    marker = state / "publication-pending.json"
    if marker.is_file():
        try:
            record = json.loads(marker.read_text())
            created = datetime.fromisoformat(record["created_at"])
            current = now or datetime.now(timezone.utc)
            age = current.astimezone(timezone.utc) - created.astimezone(timezone.utc)
            if record["release_date"] != release or age < -timedelta(minutes=5):
                raise ValueError()
            if age <= PUBLICATION_HANDOFF_GRACE:
                return True
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
            raise ServiceUnavailable("The local publication handoff is unreadable.") from error
    path = state / "producer.lock"
    if not path.is_file():
        return False
    try:
        with path.open("r") as stream:
            try:
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                return True
            else:
                fcntl.flock(stream, fcntl.LOCK_UN)
                return False
    except OSError as error:
        raise ServiceUnavailable("The local producer state could not be checked safely.") from error


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


def check(now, github, state_path, apply=False, fetch=public_file, producer_is_active=None):
    if now.tzinfo is None:
        raise ValueError("The recovery clock must have a time zone.")
    utc = now.astimezone(timezone.utc)
    release = utc.date().isoformat()
    result = {"release_date": release, "checked_at": now.isoformat(), "apply": apply}
    # The three producer attempts are 06:15, 07:15 and 08:15 UTC. Wait thirty
    # minutes after the final requested start before declaring attention needed.
    if (utc.hour, utc.minute) < (MONITOR_HOUR_UTC, MONITOR_MINUTE_UTC):
        return {**result, "status": "before_monitor_window"}
    state = read_state(state_path, release)
    body = github.archive(release)
    local_active = bool(producer_is_active and producer_is_active(release))
    if body is not None and not complete_archive(body, release):
        if local_active:
            return {**result, "status": "producer_running"}
        return {**result, "status": "needs_attention", "reason": "The saved edition is incomplete or unreviewed."}
    if body is not None and published(body, release, now, fetch):
        state.pop("stale_since", None)
        state["last_result"] = {**result, "status": "healthy"}
        if apply:
            save_state(state_path, state)
        return state["last_result"]
    if body is None:
        if local_active:
            return {**result, "status": "producer_running"}
        return {**result, "status": "needs_attention",
                "reason": "The scheduled ChatGPT producer has not saved today's edition."}
    active = any(run["status"] != "completed" for run in github.runs(now))
    fingerprint = hashlib.sha256(body).hexdigest()
    if state.get("expected_archive") != fingerprint:
        state.update(expected_archive=fingerprint, stale_since=now.isoformat())
    try:
        since = datetime.fromisoformat(state["stale_since"])
        if since.tzinfo is None:
            raise ValueError()
    except (KeyError, ValueError, TypeError) as error:
        raise ServiceUnavailable("The publishing monitor clock is unreadable.") from error
    if local_active:
        if apply:
            save_state(state_path, state)
        return {**result, "status": "producer_running"}
    if active or now - since < PUBLISHING_GRACE:
        if apply:
            save_state(state_path, state)
        return {**result, "status": "waiting_for_publishing"}
    return {**result, "status": "needs_attention",
            "reason": "The saved edition has not reached the public site after the publishing grace period."}


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
    parser.add_argument("--apply", action="store_true",
                        help="Persist the read-only health result and logs; never dispatch work.")
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE_DIR)
    parser.add_argument("--gh", default="gh", help="Absolute GitHub CLI path for the macOS timer.")
    parser.add_argument("--producer-root", type=Path,
                        help="Repository root used only to inspect the read-only producer lock.")
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
                result = check(
                    datetime.now(timezone.utc), GitHub(args.gh), args.state_dir / "state.json",
                    args.apply,
                    producer_is_active=lambda release: producer_running(
                        args.producer_root, release, datetime.now(timezone.utc)),
                )
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
