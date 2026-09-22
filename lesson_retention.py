"""Remove expired daily news files offline; keep today and the preceding 49 EST dates."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RETENTION_DAYS = 50
FIXED_EST = timezone(timedelta(hours=-5), name="EST")
DATE_NAME = re.compile(r"\d{4}-\d{2}-\d{2}")
IMAGE_NAME = re.compile(r"(\d{4}-\d{2}-\d{2})(?:-[a-f0-9]{12})?\.(?:json|webp)(?:\.tmp)?")


def retention_date(now=None):
    """Use fixed UTC-5 throughout the year, including summer and near UTC midnight."""
    if now is not None and now.tzinfo is None:
        raise ValueError("The retention clock must include a time zone.")
    return (now or datetime.now(FIXED_EST)).astimezone(FIXED_EST).date()


def parse_date(value):
    if not isinstance(value, str) or not DATE_NAME.fullmatch(value):
        raise ValueError("Use an actual calendar date in YYYY-MM-DD format.")
    return date.fromisoformat(value)


def _lesson_keys(edition):
    from vocabulary_translations import source_data, source_key
    return {source_key(source_data(value["lesson"], level))
            for level, value in edition["levels"].items()}


def _evergreen_keys():
    from story_lessons import STORIES
    return set().union(*(_lesson_keys({"levels": {level: {"lesson": lesson}
                              for level, lesson in story["levels"].items()}})
                         for story in STORIES))


def plan_retention(root=ROOT, today=None):
    """Build and validate the whole deletion list before touching any files.

    Only recognized daily-news paths are eligible. Future or unrecognized dates
    are preserved. A malformed or mismatched dated archive stops deletion rather
    than trusting its filename or guessing which translations belong to it.
    """
    root = Path(root).resolve()
    today = today or retention_date()
    if type(today) is not date:
        raise ValueError("The retention date must be a calendar date.")
    cutoff = today - timedelta(days=RETENTION_DAYS - 1)
    files = set()
    expired_dates = set()
    warnings = []
    expired_keys = set()
    protected_keys = _evergreen_keys()
    translations_safe = True

    def include(path, released):
        if released < cutoff:
            # Do not follow an unexpected link into another directory.
            relative = path.relative_to(root)
            if any(parent.is_symlink() for parent in [path, *path.parents] if parent != root):
                raise ValueError(f"Refusing to remove a linked daily-news path: {relative}")
            if path.is_file():
                files.add(relative.as_posix())
                expired_dates.add(released.isoformat())

    for path in sorted((root / "archive/lessons").glob("*.json")):
        try:
            released = parse_date(path.stem)
        except ValueError:
            warnings.append(f"Preserved unrecognized archive name: {path.name}")
            translations_safe = False
            continue
        try:
            edition = json.loads(path.read_text(encoding="utf-8"))
            if parse_date(edition["release_date"]) != released:
                raise ValueError("Release date does not match filename")
        except (ValueError, KeyError, TypeError) as error:
            raise ValueError(f"Refusing cleanup because archive date data is invalid: {path.name}") from error
        try:
            keys = _lesson_keys(edition)
            (expired_keys if released < cutoff else protected_keys).update(keys)
        except (ValueError, KeyError, TypeError):
            # Old incomplete lesson data can still expire, but its cache ownership
            # cannot be proved, so preserve translations on this cleanup pass.
            translations_safe = False
            warnings.append(f"Preserved translation caches because source data is incomplete: {path.name}")
        include(path, released)

    for directory in sorted((root / "news").glob("*")):
        try:
            released = parse_date(directory.name)
        except ValueError:
            continue
        for level in ("beginner", "intermediate", "advanced"):
            include(directory / f"{level}.html", released)

    for path in sorted((root / "assets/news").glob("*")):
        match = IMAGE_NAME.fullmatch(path.name)
        if match:
            try:
                released = parse_date(match[1])
            except ValueError:
                continue
            include(path, released)

    if translations_safe:
        for key in expired_keys - protected_keys:
            for name in (f"{key}.json", f".draft-{key}.json"):
                path = root / "data/vocabulary-translations" / name
                if path.exists():
                    if path.is_symlink() or path.parent.is_symlink() or path.parent.parent.is_symlink():
                        raise ValueError(f"Refusing to remove linked translation cache: {name}")
                    files.add(path.relative_to(root).as_posix())

    counts = Counter("archives" if name.startswith("archive/") else
                     "lesson_pages" if name.startswith("news/") else
                     "images_and_metadata" if name.startswith("assets/") else
                     "translation_caches" for name in files)
    return {"as_of": today.isoformat(), "time_zone": "EST (UTC-5, fixed)",
            "retention_days": RETENTION_DAYS, "oldest_allowed": cutoff.isoformat(),
            "expired_dates": sorted(expired_dates), "files": sorted(files),
            "counts": dict(sorted(counts.items())),
            "bytes": sum((root / name).stat().st_size for name in files), "warnings": warnings}


def prune_expired_lessons(root=ROOT, today=None, dry_run=False):
    """Prune source/assets only; the caller must rebuild and check the public pages."""
    root = Path(root).resolve()
    plan = plan_retention(root, today)
    if not dry_run:
        for name in plan["files"]:
            (root / name).unlink()
        for released in plan["expired_dates"]:
            directory = root / "news" / released
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()
    return plan


def summary(plan, dry_run=False):
    action = "Would remove" if dry_run else "Removed"
    return (f"{action} {len(plan['files'])} expired daily-news files across "
            f"{len(plan['expired_dates'])} dates; keeping {plan['oldest_allowed']} "
            f"through {plan['as_of']} ({plan['time_zone']}).")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--today", type=parse_date, help="Override the fixed EST calendar date for an offline check.")
    parser.add_argument("--apply", action="store_true", help="Delete the listed expired source/assets; default is dry run.")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable report, including the file list.")
    args = parser.parse_args()
    plan = prune_expired_lessons(args.root, args.today, dry_run=not args.apply)
    if args.json:
        print(json.dumps(plan, indent=2))
    else:
        print(summary(plan, dry_run=not args.apply))
        for warning in plan["warnings"]:
            print(f"Warning: {warning}")
        if args.apply:
            print("Rebuild with update_site.py --refresh-pages before publishing.")


if __name__ == "__main__":
    main()
