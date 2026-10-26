"""Stage and validate ChatGPT-plan artifacts for one English Ladder edition.

This module contains no model client and never reads an API key. Model calls are
made by ``plan_daily_runner.py`` through the signed-in Codex CLI, in separate
ephemeral sessions. Every artifact enters the site through the same local
evidence, teaching, translation, image, and publication validators used by the
existing application.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

from daily_images import image_for_lesson, image_prompt, import_daily_image
from daily_publication import saved_edition_status
from lesson_evidence import resolve_evidence_references
from lesson_levels import LANGUAGE_POLICY_VERSION
from lesson_run import saved_source_is_complete
from news_quality import review_lesson, validate_editorial_review, validate_evidence
from vocabulary_translations import (
    INSTRUCTIONS as TRANSLATION_INSTRUCTIONS,
    LANGUAGES,
    language_instruction,
    read_record,
    response_schema as translation_schema,
    source_data as translation_source,
    source_key as translation_key,
    validate_entries,
)
import update_site


ROOT = Path(__file__).resolve().parent
STATE_ROOT = ROOT / ".daily-agent"
MODEL = "gpt-6.1-sol"
IMAGE_MODEL = "ChatGPT built-in image generation (exact model not exposed)"
SURFACE = "Codex with ChatGPT sign-in"
LEVEL_NAMES = ("beginner", "intermediate", "advanced")


def atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def state_dir(release_date: str, directory: str | None = None) -> Path:
    datetime.strptime(release_date, "%Y-%m-%d")
    return Path(directory) if directory else STATE_ROOT / release_date


def level_config(name: str, state: Path | None = None):
    try:
        base = next(item for item in update_site.LEVELS if item["name"].lower() == name)
    except StopIteration as error:
        raise ValueError(f"Unknown level: {name}") from error
    level = dict(base)
    reserved = []
    if state is not None:
        for previous in LEVEL_NAMES:
            if previous == name:
                break
            path = state / f"approved-{previous}.json"
            if path.exists():
                reserved.extend({"term": item["term"], "level": previous.title()}
                                for item in load_json(path)["vocabulary"])
    level["reserved_vocabulary"] = reserved
    return level


def source_path(state: Path) -> Path:
    return state / "source.json"


def prepare_source(release_date: str, state: Path) -> Path:
    path = source_path(state)
    if path.exists():
        source = load_json(path)
        if saved_source_is_complete(source):
            return path
        raise ValueError("Saved source state is incomplete; remove it only after reviewing the file.")
    release_dt = update_site.release_datetime_from_date(release_date)
    source = update_site.get_daily_news(release_dt)
    if not saved_source_is_complete(source):
        raise ValueError("The selected source is incomplete.")
    atomic_json(path, source)
    return path


def prepare_level(release_date: str, state: Path, name: str) -> dict:
    source = load_json(source_path(state))
    level = level_config(name, state)
    previous_path = state / f"lesson-{name}.json"
    issues_path = state / f"issues-{name}.json"
    revision = None
    if previous_path.exists() and issues_path.exists():
        issues = load_json(issues_path)
        if not isinstance(issues, list) or any(not isinstance(issue, str) for issue in issues):
            raise ValueError("Saved revision issues are invalid.")
        revision = update_site.revision_instructions(load_json(previous_path), level, issues)
    schema = update_site.build_response_schema(level, source)
    prompt = update_site.build_prompt(source, level, revision)
    schema_path = state / f"draft-{name}.schema.json"
    prompt_path = state / f"draft-{name}.prompt.txt"
    atomic_json(schema_path, schema)
    prompt_path.write_text(prompt, encoding="utf-8")
    return {"schema": str(schema_path), "prompt": str(prompt_path)}


def accept_draft(release_date: str, state: Path, name: str, draft_path: Path) -> Path:
    source = load_json(source_path(state))
    level = level_config(name, state)
    try:
        lesson = resolve_evidence_references(load_json(draft_path), source)
        issues = list(dict.fromkeys(
            update_site.validate_lesson_data(lesson, level) + validate_evidence(lesson, source)
        ))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        lesson = None
        issues = [f"The generated lesson could not be applied: {error}"]
    if issues:
        atomic_json(state / f"issues-{name}.json", issues)
        if lesson is not None:
            atomic_json(state / f"lesson-{name}.json", lesson)
        raise ValueError("; ".join(issues))
    lesson_path = state / f"lesson-{name}.json"
    atomic_json(lesson_path, lesson)
    prepare_review(release_date, state, name)
    return lesson_path


def prepare_review(release_date: str, state: Path, name: str) -> dict:
    """Resume at review without asking the model to recreate a valid lesson draft."""
    source = load_json(source_path(state))
    lesson = load_json(state / f"lesson-{name}.json")
    level = level_config(name, state)
    issues = list(dict.fromkeys(
        update_site.validate_lesson_data(lesson, level) + validate_evidence(lesson, source)
    ))
    if issues:
        atomic_json(state / f"issues-{name}.json", issues)
        raise ValueError("; ".join(issues))
    prompt, schema = review_lesson(None, source, lesson, level, MODEL, return_request=True)
    prompt_path = state / f"review-{name}.prompt.txt"
    schema_path = state / f"review-{name}.schema.json"
    prompt_path.write_text(prompt, encoding="utf-8")
    atomic_json(schema_path, schema)
    (state / f"issues-{name}.json").unlink(missing_ok=True)
    return {"schema": str(schema_path), "prompt": str(prompt_path)}


def accept_review(release_date: str, state: Path, name: str, review_path: Path,
                  attempt: int) -> Path:
    source = load_json(source_path(state))
    lesson = load_json(state / f"lesson-{name}.json")
    level = level_config(name, state)
    raw = load_json(review_path)
    issues = list(dict.fromkeys(
        update_site.validate_lesson_data(lesson, level)
        + validate_evidence(lesson, source)
        + validate_editorial_review(raw)
    ))
    if issues:
        atomic_json(state / f"issues-{name}.json", issues)
        raise ValueError("; ".join(issues))
    lesson["editorial_check"] = {
        "date": datetime.now(timezone.utc).isoformat(),
        "model": MODEL,
        "status": "passed",
        "method": "separate ChatGPT-plan evidence, teaching and level suitability review",
        "generation_attempts": attempt,
        "repaired_sections": [],
        "provider": "OpenAI",
        "surface": SURFACE,
        "reviewer": {"model": MODEL, "surface": SURFACE, "separate_session": True},
        "language_policy_version": LANGUAGE_POLICY_VERSION,
        "target_level": level["cefr"],
        "level_checks": raw["level_checks"],
    }
    lesson["editorial_check"]["content_digest"] = update_site.lesson_approval_digest(
        lesson, source, level)
    destination = state / f"approved-{name}.json"
    atomic_json(destination, lesson)
    (state / f"issues-{name}.json").unlink(missing_ok=True)
    return destination


def stage_archive(release_date: str, state: Path) -> Path:
    source = load_json(source_path(state))
    lessons = {name: load_json(state / f"approved-{name}.json") for name in LEVEL_NAMES}
    archive = update_site.archive_daily_lessons(
        source, lessons, update_site.release_datetime_from_date(release_date)
    )
    record = load_json(archive)
    record["model"] = MODEL
    record["generation"] = {
        "provider": "OpenAI",
        "surface": SURFACE,
        "model": MODEL,
        "review_model": MODEL,
        "separate_review_sessions": True,
    }
    atomic_json(archive, record)
    return archive


def archive_path(release_date: str) -> Path:
    return ROOT / "archive/lessons" / f"{release_date}.json"


def prepare_translation(release_date: str, state: Path, name: str, review: bool) -> dict:
    edition = load_json(archive_path(release_date))
    source = translation_source(edition["levels"][name]["lesson"], name)
    schema = translation_schema(source)
    schema_path = state / f"translation-{name}.schema.json"
    prompt_path = state / f"translation-{'review' if review else 'draft'}-{name}.prompt.txt"
    atomic_json(schema_path, schema)
    instructions = TRANSLATION_INSTRUCTIONS + language_instruction(LANGUAGES)
    if review:
        draft = load_json(state / f"translation-draft-{name}.json")
        prompt = (instructions + "\nINDEPENDENT REVIEW: Check every supplied translation against its "
                  "English definition and story context. Correct any mistranslation, omitted "
                  "qualification, wrong sense, unnatural phrasing, wrong script or regional "
                  "variant. Retain correct wording. Return the complete final corrected entries, "
                  "not a review report.\nLESSON AND DRAFT:\n"
                  + json.dumps({"lesson": source, "draft": draft["entries"]}, ensure_ascii=False))
    else:
        prompt = instructions + "\nLESSON:\n" + json.dumps(source, ensure_ascii=False)
    prompt_path.write_text(prompt, encoding="utf-8")
    return {"schema": str(schema_path), "prompt": str(prompt_path)}


def accept_translation_draft(release_date: str, state: Path, name: str,
                             result_path: Path) -> Path:
    edition = load_json(archive_path(release_date))
    source = translation_source(edition["levels"][name]["lesson"], name)
    entries = validate_entries(load_json(result_path)["entries"], source)
    destination = state / f"translation-draft-{name}.json"
    atomic_json(destination, {"source": source, "entries": entries})
    return destination


def accept_translation_review(release_date: str, state: Path, name: str,
                              result_path: Path) -> Path:
    edition = load_json(archive_path(release_date))
    source = translation_source(edition["levels"][name]["lesson"], name)
    draft = load_json(state / f"translation-draft-{name}.json")
    validate_entries(draft["entries"], source)
    entries = validate_entries(load_json(result_path)["entries"], source)
    destination = ROOT / "data/vocabulary-translations" / f"{translation_key(source)}.json"
    record = {
        "source": source,
        "entries": entries,
        "review": {
            "status": "reviewed",
            "method": "separate ChatGPT plan translation and independent editing sessions",
            "model": MODEL,
            "date": datetime.now(timezone.utc).isoformat(),
            "added_languages": list(LANGUAGES),
            "generator": {"provider": "OpenAI", "surface": SURFACE, "model": MODEL,
                          "phase": "translation"},
            "reviewer": {"provider": "OpenAI", "surface": SURFACE, "model": MODEL,
                         "phase": "independent multilingual editing", "separate_session": True},
        },
    }
    atomic_json(destination, record)
    if read_record(source) is None:
        raise ValueError("The imported translation record did not pass the canonical reader.")
    return destination


def prepare_image(release_date: str, state: Path) -> Path:
    edition = load_json(archive_path(release_date))
    path = state / "image.prompt.txt"
    path.write_text(image_prompt(edition), encoding="utf-8")
    return path


def import_image(release_date: str, image_path: Path):
    return import_daily_image(archive_path(release_date), image_path, ROOT,
                              model=IMAGE_MODEL, surface=SURFACE)


def build_and_check(release_date: str) -> None:
    edition = load_json(archive_path(release_date))
    for name in LEVEL_NAMES:
        source = translation_source(edition["levels"][name]["lesson"], name)
        if read_record(source) is None:
            raise ValueError(f"Reviewed translations are missing for {release_date}/{name}.")
    if image_for_lesson(edition, ROOT) is None:
        raise ValueError(f"The validated illustration is missing for {release_date}.")
    subprocess.run([sys.executable, "update_site.py", "--refresh-pages", "--release-date", release_date],
                   cwd=ROOT, check=True)
    subprocess.run([sys.executable, "audit_site.py"], cwd=ROOT, check=True)
    for pattern in ("test_quality.py", "test_daily_publication.py",
                    "test_vocabulary_translations.py", "test_daily_images.py"):
        subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", pattern],
                       cwd=ROOT, check=True)
    complete, reason = saved_edition_status(ROOT, release_date)
    if not complete:
        raise ValueError(reason)


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument("--date", required=True)
    command.add_argument("--state-dir")
    sub = command.add_subparsers(dest="command", required=True)
    sub.add_parser("prepare-source")
    for name in ("prepare-level", "prepare-review", "accept-draft", "accept-review",
                 "prepare-translation", "accept-translation-draft",
                 "accept-translation-review"):
        item = sub.add_parser(name)
        item.add_argument("--level", choices=LEVEL_NAMES, required=True)
        if name.startswith("accept-"):
            item.add_argument("--input", type=Path, required=True)
        if name == "accept-review":
            item.add_argument("--attempt", type=int, required=True)
        if name == "prepare-translation":
            item.add_argument("--review", action="store_true")
    sub.add_parser("stage-archive")
    sub.add_parser("prepare-image")
    image = sub.add_parser("import-image")
    image.add_argument("--input", type=Path, required=True)
    sub.add_parser("build")
    sub.add_parser("status")
    return command


def main(argv=None) -> int:
    args = parser().parse_args(argv)
    state = state_dir(args.date, args.state_dir)
    state.mkdir(parents=True, exist_ok=True)
    if args.command == "prepare-source":
        result = prepare_source(args.date, state)
    elif args.command == "prepare-level":
        result = prepare_level(args.date, state, args.level)
    elif args.command == "prepare-review":
        result = prepare_review(args.date, state, args.level)
    elif args.command == "accept-draft":
        result = accept_draft(args.date, state, args.level, args.input)
    elif args.command == "accept-review":
        result = accept_review(args.date, state, args.level, args.input, args.attempt)
    elif args.command == "stage-archive":
        result = stage_archive(args.date, state)
    elif args.command == "prepare-translation":
        result = prepare_translation(args.date, state, args.level, args.review)
    elif args.command == "accept-translation-draft":
        result = accept_translation_draft(args.date, state, args.level, args.input)
    elif args.command == "accept-translation-review":
        result = accept_translation_review(args.date, state, args.level, args.input)
    elif args.command == "prepare-image":
        result = prepare_image(args.date, state)
    elif args.command == "import-image":
        result = import_image(args.date, args.input)
    elif args.command == "build":
        build_and_check(args.date)
        result = "complete"
    else:
        complete, reason = saved_edition_status(ROOT, args.date)
        result = {"complete": complete, "reason": reason}
    print(json.dumps(result if isinstance(result, dict) else {"result": str(result)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
