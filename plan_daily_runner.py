"""Run the complete daily producer through a ChatGPT-authenticated Codex CLI.

No API key is accepted or forwarded. Drafting, independent review, translation,
independent multilingual editing, and image generation each use a fresh
ephemeral Codex session. Local Python code validates and imports every result.
Git synchronization, commits, pushes, and live verification deliberately remain
the responsibility of the scheduled repository skill.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import date, datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import plan_daily
from daily_schedule import scheduled_release_date
from daily_publication import check_publication, saved_edition_status
from vocabulary_translations import read_record, source_data


ROOT = Path(__file__).resolve().parent
MODEL = plan_daily.MODEL
LEVELS = plan_daily.LEVEL_NAMES
FORBIDDEN_ENV = {
    "OPENAI_API_KEY", "GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENAI_API_KEY",
    "ANTHROPIC_API_KEY", "AZURE_OPENAI_API_KEY",
}
MINIMUM_FREE_BYTES = 512 * 1024 * 1024


def publication_marker(state: Path) -> Path:
    return state / "publication-pending.json"


def mark_publication_pending(release: str, state: Path, archive: Path) -> Path:
    marker = publication_marker(state)
    plan_daily.atomic_json(marker, {
        "release_date": release,
        "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "owner_thread_id": os.environ.get("CODEX_THREAD_ID"),
    })
    return marker


def resume_publication(release: str, state: Path, previous_owner: str) -> None:
    """Transfer a handoff after the caller verifies the old chat has stopped.

    Called only under producer_lock. The expected owner makes concurrent
    takeovers fail closed; a marker's age alone never authorizes takeover.
    This path cannot invoke a model or rebuild the saved edition.
    """
    owner = os.environ.get("CODEX_THREAD_ID")
    marker = publication_marker(state)
    record = json.loads(marker.read_text())
    if not owner or not previous_owner or owner == previous_owner:
        raise RuntimeError("Publication recovery requires a different, identified owning chat.")
    if record.get("owner_thread_id") != previous_owner:
        raise RuntimeError("Publication owner changed or is unknown; recheck ownership before recovery.")
    archive = ROOT / f"archive/lessons/{release}.json"
    if (record.get("release_date") != release or
            record.get("archive_sha256") != hashlib.sha256(archive.read_bytes()).hexdigest()):
        raise RuntimeError("The saved edition no longer matches its publication handoff.")
    complete, reason = saved_edition_status(ROOT, release)
    if not complete:
        raise RuntimeError(reason)
    record.setdefault("ownership_transfers", []).append({
        "from": previous_owner, "to": owner,
        "at": datetime.now(timezone.utc).isoformat(),
    })
    record["owner_thread_id"] = owner
    plan_daily.atomic_json(marker, record)


def finish_publication(release: str, state: Path) -> None:
    published, reason = check_publication(ROOT, release)
    if not published:
        raise RuntimeError(reason)
    publication_marker(state).unlink(missing_ok=True)


def codex_executable() -> str:
    configured = os.environ.get("CODEX_PLAN_EXECUTABLE")
    candidates = [
        configured,
        shutil.which("codex"),
        "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise RuntimeError("The signed-in Codex CLI is not installed.")


def clean_environment() -> dict[str, str]:
    return {key: value for key, value in os.environ.items() if key not in FORBIDDEN_ENV}


def verify_chatgpt_login(executable: str) -> None:
    result = subprocess.run([executable, "login", "status"], cwd=ROOT,
                            env=clean_environment(), capture_output=True, text=True, timeout=30)
    if result.returncode or "ChatGPT" not in result.stdout + result.stderr:
        raise RuntimeError("Codex is not signed in through ChatGPT; no generation was attempted.")


def verify_free_space(minimum: int = MINIMUM_FREE_BYTES) -> None:
    free = shutil.disk_usage(ROOT).free
    if free < minimum:
        raise RuntimeError(
            f"Daily generation needs at least {minimum // (1024 * 1024)} MiB free; "
            f"only {free // (1024 * 1024)} MiB is available. No generation was attempted."
        )


def run_python(release: str, command: str, *arguments: str,
               state: Path | None = None) -> None:
    invocation = [sys.executable, "plan_daily.py", "--date", release]
    if state is not None:
        invocation += ["--state-dir", str(state)]
    invocation += [command, *arguments]
    subprocess.run(invocation, cwd=ROOT, check=True)


def model_json(executable: str, prompt_path: Path, schema_path: Path,
               output_path: Path) -> None:
    prompt = prompt_path.read_text(encoding="utf-8")
    instruction = (
        "Return only the JSON object required by the supplied output schema. "
        "Do not call tools, browse, modify files, or include Markdown.\n\n" + prompt
    )
    output_path.unlink(missing_ok=True)
    command = [
        executable,
        "--ask-for-approval", "never",
        "--sandbox", "read-only",
        "-C", str(ROOT),
        "-m", MODEL,
        "-c", 'model_reasoning_effort="high"',
        "exec", "--ephemeral",
        "--output-schema", str(schema_path),
        "--output-last-message", str(output_path),
        "-",
    ]
    subprocess.run(command, input=instruction, text=True, cwd=ROOT,
                   env=clean_environment(), check=True, timeout=1800)
    if not output_path.is_file():
        raise RuntimeError("Codex completed without saving its structured result.")
    json.loads(output_path.read_text(encoding="utf-8"))


def model_image(executable: str, release: str, state: Path) -> Path:
    prompt_path = plan_daily.prepare_image(release, state)
    output_path = state / "image.png"
    # A model session may have completed before import or publication failed.
    # Preserve that staged image and let the deterministic importer validate it.
    if output_path.is_file():
        return output_path
    instruction = f"""Use the $imagegen skill and only ChatGPT's built-in image-generation tool.
Do not use Gemini, an API key, curl, a browser, or another external image service.
Create exactly one image from the following production prompt. Save the final PNG directly at:
{output_path}
Do not modify any other file. When the PNG is present, reply briefly with its dimensions and path.

{prompt_path.read_text(encoding='utf-8')}
"""
    command = [
        executable,
        "--ask-for-approval", "never",
        "--sandbox", "workspace-write",
        "-C", str(state),
        "--add-dir", str(ROOT),
        "-m", MODEL,
        "-c", 'model_reasoning_effort="high"',
        "exec", "--ephemeral", "-",
    ]
    subprocess.run(command, input=instruction, text=True, cwd=state,
                   env=clean_environment(), check=True, timeout=1800)
    if not output_path.is_file():
        raise RuntimeError("The plan image session completed without the requested PNG.")
    return output_path


def create_lessons(executable: str, release: str, state: Path) -> None:
    run_python(release, "prepare-source", state=state)
    for level in LEVELS:
        if (state / f"approved-{level}.json").exists():
            continue
        last_error = None
        for attempt in range(1, 4):
            try:
                lesson = state / f"lesson-{level}.json"
                issues = state / f"issues-{level}.json"
                if lesson.exists() and not issues.exists():
                    run_python(release, "prepare-review", "--level", level, state=state)
                else:
                    run_python(release, "prepare-level", "--level", level, state=state)
                    draft_result = state / f"draft-result-{level}-{attempt}.json"
                    model_json(executable, state / f"draft-{level}.prompt.txt",
                               state / f"draft-{level}.schema.json", draft_result)
                    run_python(release, "accept-draft", "--level", level,
                               "--input", str(draft_result), state=state)
                review_result = state / f"review-result-{level}-{attempt}.json"
                model_json(executable, state / f"review-{level}.prompt.txt",
                           state / f"review-{level}.schema.json", review_result)
                run_python(release, "accept-review", "--level", level,
                           "--input", str(review_result), "--attempt", str(attempt), state=state)
                break
            except (subprocess.CalledProcessError, RuntimeError, ValueError,
                    json.JSONDecodeError) as error:
                last_error = error
                print(f"{level} attempt {attempt}/3 did not pass; retaining state for repair.",
                      file=sys.stderr, flush=True)
        else:
            raise RuntimeError(f"{level} did not pass after three bounded attempts: "
                               f"{type(last_error).__name__}")
    run_python(release, "stage-archive", state=state)


def create_translation(executable: str, release: str, state: Path, level: str) -> None:
    edition = json.loads((ROOT / f"archive/lessons/{release}.json").read_text())
    source = source_data(edition["levels"][level]["lesson"], level)
    if read_record(source):
        return
    saved_draft = state / f"translation-draft-{level}.json"
    draft = state / f"translation-result-draft-{level}.json"
    if not saved_draft.exists():
        if not draft.exists():
            run_python(release, "prepare-translation", "--level", level, state=state)
            model_json(executable, state / f"translation-draft-{level}.prompt.txt",
                       state / f"translation-{level}.schema.json", draft)
        run_python(release, "accept-translation-draft", "--level", level,
                   "--input", str(draft), state=state)
    run_python(release, "prepare-translation", "--level", level, "--review", state=state)
    review = state / f"translation-result-review-{level}.json"
    if not review.exists():
        model_json(executable, state / f"translation-review-{level}.prompt.txt",
                   state / f"translation-{level}.schema.json", review)
    run_python(release, "accept-translation-review", "--level", level,
               "--input", str(review), state=state)


def recent_releases() -> list[str]:
    return [path.stem for path in sorted((ROOT / "archive/lessons").glob("*.json"), reverse=True)[:3]]


@contextmanager
def producer_lock(path: Path):
    """Serialize the three scheduled opportunities without hiding a failed process."""
    path.parent.mkdir(parents=True, exist_ok=True)
    activity = path.with_name("producer-active.json")
    with path.open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            yield False
            return
        try:
            plan_daily.atomic_json(activity, {
                "started_at": datetime.now(timezone.utc).isoformat(),
                "pid": os.getpid(),
            })
            yield True
        finally:
            activity.unlink(missing_ok=True)
            fcntl.flock(stream, fcntl.LOCK_UN)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date")
    parser.add_argument("--state-dir")
    parser.add_argument("--finish-publication", action="store_true",
                        help="Verify the live edition and release its publication handoff.")
    parser.add_argument("--resume-publication-from", metavar="STOPPED_THREAD_ID",
                        help="Claim saved publication after verifying that its owning chat stopped.")
    args = parser.parse_args(argv)
    if args.finish_publication and args.resume_publication_from:
        parser.error("Choose either finishing or resuming publication.")
    release = date.fromisoformat(args.date).isoformat() if args.date else scheduled_release_date().isoformat()
    state = plan_daily.state_dir(release, args.state_dir)
    state.mkdir(parents=True, exist_ok=True)
    with producer_lock(state / "producer.lock") as acquired:
        if not acquired:
            print(json.dumps({"release_date": release, "status": "already_running",
                              "model": MODEL, "authentication": "ChatGPT",
                              "api_fallback": False}))
            return 0
        if args.finish_publication:
            finish_publication(release, state)
            print(json.dumps({"release_date": release, "status": "published"}))
            return 0
        if args.resume_publication_from:
            resume_publication(release, state, args.resume_publication_from)
            print(json.dumps({"release_date": release, "status": "ready_to_publish",
                              "resumed": True, "owner_thread_id": os.environ["CODEX_THREAD_ID"],
                              "model": MODEL, "authentication": "ChatGPT", "api_fallback": False}))
            return 0
        if publication_marker(state).exists():
            record = json.loads(publication_marker(state).read_text())
            print(json.dumps({"release_date": release, "status": "publication_pending",
                              "owner_thread_id": record.get("owner_thread_id"),
                              "model": MODEL, "authentication": "ChatGPT",
                              "api_fallback": False}))
            return 0
        verify_free_space()
        executable = codex_executable()
        verify_chatgpt_login(executable)

        archive = ROOT / f"archive/lessons/{release}.json"
        if not archive.exists():
            create_lessons(executable, release, state)
        for recent in recent_releases():
            recent_state = plan_daily.state_dir(recent)
            recent_state.mkdir(parents=True, exist_ok=True)
            for level in LEVELS:
                create_translation(executable, recent, recent_state, level)

        edition = json.loads(archive.read_text(encoding="utf-8"))
        if plan_daily.image_for_lesson(edition, ROOT) is None:
            image = model_image(executable, release, state)
            run_python(release, "import-image", "--input", str(image), state=state)

        run_python(release, "build", state=state)
        mark_publication_pending(release, state, archive)
        print(json.dumps({"release_date": release, "status": "ready_to_publish", "model": MODEL,
                          "authentication": "ChatGPT", "api_fallback": False}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
