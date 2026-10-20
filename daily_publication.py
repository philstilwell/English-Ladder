"""Read-only shortcut for a complete daily edition that is already live.

No generation, page rendering, paid requests, or email delivery occurs here.
An incomplete edition or an inconclusive network check leaves recovery enabled.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
import os
from pathlib import Path
import subprocess

from daily_images import image_for_lesson
from lesson_retention import retention_date
from vocabulary_translations import read_record, source_data

ROOT = Path(__file__).resolve().parent
LEVELS = ("beginner", "intermediate", "advanced")


def saved_edition_status(root, release_date):
    """Reuse the image and translation validators without loading an API client."""
    root = Path(root)
    try:
        path = root / "archive/lessons" / f"{release_date}.json"
        edition = json.loads(path.read_text())
        if edition["release_date"] != release_date:
            return False, "The saved edition has a different release date."
        for level in LEVELS:
            lesson = edition["levels"][level]["lesson"]
            if not all(isinstance(lesson.get(key), str) and lesson[key].strip()
                       for key in ("title", "overview")):
                return False, f"The saved {level} lesson is incomplete."
            if not lesson.get("news_brief_sentences") or not lesson.get("vocabulary"):
                return False, f"The saved {level} lesson is incomplete."
            if not (root / "news" / release_date / f"{level}.html").is_file():
                return False, f"The saved {level} page is missing."
        if not image_for_lesson(edition, root=root):
            return False, "The daily illustration needs recovery."
        # Match the scheduled translation pass: the newest three editions.
        paths = sorted((root / "archive/lessons").glob("*.json"), reverse=True)[:3]
        for path in paths:
            recent = json.loads(path.read_text())
            for level in LEVELS:
                source = source_data(recent["levels"][level]["lesson"], level)
                if not read_record(source, root / "data/vocabulary-translations"):
                    return False, f"Reviewed translations need recovery for {path.stem}/{level}."
    except (OSError, ValueError, KeyError, TypeError, IndexError):
        return False, "A saved lesson or supporting file is missing or invalid."
    return True, "Saved lessons, illustration, and recent translations are complete."


def check_publication(root, release_date, run=subprocess.run):
    complete, reason = saved_edition_status(root, release_date)
    if not complete:
        return False, reason
    try:
        result = run(
            ["node", "cloudflare/check-daily-publication.cjs", release_date],
            cwd=root, capture_output=True, text=True, timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False, "The live publication check did not complete; recovery remains enabled."
    if result.returncode:
        return False, "The complete saved edition could not be verified live; recovery remains enabled."
    return True, "Today's complete edition is verified live; skip generation, tests, and page rebuilding."


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default="")
    parser.add_argument("--require-published", action="store_true",
                        help="Fail without doing recovery if the edition is not verified live.")
    args = parser.parse_args(argv)
    release_date = date.fromisoformat(args.date).isoformat() if args.date else retention_date().isoformat()
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    # Save the target date before the network check, including on a failed probe.
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a") as stream:
            stream.write(f"release_date={release_date}\npublishing_revision={revision}\n")
    published, reason = check_publication(ROOT, release_date)
    if output:
        with open(output, "a") as stream:
            stream.write(f"already_published={str(published).lower()}\n")
    print(json.dumps({"release_date": release_date, "already_published": published, "reason": reason}))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as stream:
            stream.write(f"### Daily publication check: {release_date}\n\n{reason}\n")
    return int(args.require_published and not published)


if __name__ == "__main__":
    raise SystemExit(main())
