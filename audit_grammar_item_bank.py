from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from build_grammar_item_bank import (
    CEFR_LEVELS,
    DIFFICULTY_LEVELS,
    FOCUS_AREAS,
    ITEM_BANK_DIR,
    ITEM_TYPES,
    MODEL,
    SOURCE_STATUSES,
    api_request,
    build_review_prompt,
    build_review_schema,
    clean_text,
    extract_response_json,
    load_selected_entries,
    normalize_key,
    should_run_editorial_review,
    validate_banned_terms,
)


AUDIT_MODEL = os.environ.get("ENGLISH_LADDER_AUDIT_MODEL", MODEL)
DEFAULT_REPORT_PATH = Path("tmp/grammar-item-audit.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit local English Ladder grammar assessment items.")
    parser.add_argument("--concept", type=int, nargs="*", help="Optional concept numbers to audit.")
    parser.add_argument("--data-dir", default=str(ITEM_BANK_DIR), help="Directory containing concept-XX.json banks.")
    parser.add_argument("--report", default=str(DEFAULT_REPORT_PATH), help="JSON report path.")
    parser.add_argument("--model", default=AUDIT_MODEL, help="OpenAI model for editorial review.")
    parser.add_argument("--batch-size", type=int, default=8, help="Items per model review batch.")
    parser.add_argument("--deterministic-only", action="store_true", help="Skip model-based editorial review.")
    return parser.parse_args()


def load_bank(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def bank_paths(data_dir: Path, concepts: list[int] | None) -> list[Path]:
    if concepts:
        return [data_dir / f"concept-{number:02d}.json" for number in concepts]
    return sorted(data_dir.glob("concept-*.json"))


def flatten_items(bank: dict[str, Any], path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    concept_number = int(bank["concept_number"])
    concept_title = str(bank["concept_title"])
    for practice_set in bank.get("assessment_sets", []):
        for item in practice_set.get("items", []):
            rows.append(
                {
                    "bank_path": str(path),
                    "concept_number": concept_number,
                    "concept_title": concept_title,
                    "set_id": practice_set.get("id", ""),
                    "set_title": practice_set.get("title", ""),
                    "item": item,
                }
            )
    return rows


def issue(item_id: str, severity: str, message: str, source: str) -> dict[str, str]:
    return {
        "item_id": item_id,
        "severity": severity,
        "message": message,
        "source": source,
    }


def deterministic_audit(rows: list[dict[str, Any]], entries_by_number: dict[int, Any]) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    stems_by_concept: dict[int, dict[str, str]] = defaultdict(dict)
    weakness_by_concept: dict[int, dict[str, str]] = defaultdict(dict)
    ids_seen: set[str] = set()

    for row in rows:
        item = row["item"]
        concept_number = int(row["concept_number"])
        entry = entries_by_number.get(concept_number)
        item_id = clean_text(str(item.get("id", ""))) or "[blank id]"

        if item_id in ids_seen:
            issues.append(issue(item_id, "high", "Duplicate item id across audited banks.", "deterministic"))
        ids_seen.add(item_id)

        question = clean_text(str(item.get("question", "")))
        if not question:
            issues.append(issue(item_id, "high", "Question is blank.", "deterministic"))
        elif len(question) > 260:
            issues.append(issue(item_id, "medium", "Question is unusually long for phone-first assessment use.", "deterministic"))
        if re.search(r"(^|\n)\s*[A-D][.)]\s+", question):
            issues.append(issue(item_id, "medium", "Question embeds A/B/C/D choices instead of using the options list.", "deterministic"))

        normalized_question = normalize_key(question)
        existing_stem_id = stems_by_concept[concept_number].get(normalized_question)
        if existing_stem_id:
            issues.append(
                issue(item_id, "high", f"Question duplicates {existing_stem_id} in the same concept.", "deterministic")
            )
        elif normalized_question:
            stems_by_concept[concept_number][normalized_question] = item_id

        weakness = clean_text(str(item.get("weakness_tag", "")))
        normalized_weakness = normalize_key(weakness)
        existing_weakness_id = weakness_by_concept[concept_number].get(normalized_weakness)
        if existing_weakness_id:
            issues.append(
                issue(item_id, "medium", f"Weakness tag repeats {existing_weakness_id} in the same concept.", "deterministic")
            )
        elif normalized_weakness:
            weakness_by_concept[concept_number][normalized_weakness] = item_id
        else:
            issues.append(issue(item_id, "medium", "Weakness tag is blank.", "deterministic"))

        options = [clean_text(str(option)) for option in item.get("options", [])]
        if len(options) != 4:
            issues.append(issue(item_id, "high", "Item does not contain exactly four options.", "deterministic"))
        elif len({normalize_key(option) for option in options}) != 4:
            issues.append(issue(item_id, "high", "Item contains duplicate or near-duplicate options.", "deterministic"))
        elif {normalize_key(option) for option in options} <= {"a", "b", "c", "d"}:
            issues.append(issue(item_id, "medium", "Options are letter-only instead of full answer choices.", "deterministic"))
        elif any(re.match(r"^[A-D][.)]\s+", option) for option in options):
            issues.append(issue(item_id, "medium", "Options include visible A/B/C/D prefixes.", "deterministic"))

        correct_index = item.get("correct_index")
        if not isinstance(correct_index, int) or not 0 <= correct_index < len(options):
            issues.append(issue(item_id, "high", "Correct index is invalid.", "deterministic"))

        explanation = clean_text(str(item.get("explanation", "")))
        explanation_words = explanation.split()
        if len(explanation_words) < 5:
            issues.append(issue(item_id, "medium", "Explanation is too short to be useful.", "deterministic"))
        if len(explanation_words) > 32:
            issues.append(issue(item_id, "low", "Explanation is longer than the preferred concise feedback range.", "deterministic"))

        if item.get("focus_area") not in FOCUS_AREAS:
            issues.append(issue(item_id, "high", "Unsupported focus_area value.", "deterministic"))
        if item.get("item_type") not in ITEM_TYPES:
            issues.append(issue(item_id, "high", "Unsupported item_type value.", "deterministic"))
        if item.get("cefr_level") not in CEFR_LEVELS:
            issues.append(issue(item_id, "medium", "Missing or unsupported cefr_level metadata.", "deterministic"))
        if item.get("difficulty") not in DIFFICULTY_LEVELS:
            issues.append(issue(item_id, "medium", "Missing or unsupported difficulty metadata.", "deterministic"))
        if item.get("source_status") not in SOURCE_STATUSES:
            issues.append(issue(item_id, "medium", "Missing or unsupported source_status metadata.", "deterministic"))

        if entry is not None:
            for banned_issue in validate_banned_terms(entry, item, item_id):
                issues.append(issue(item_id, "high", banned_issue, "deterministic"))

    return issues


def review_batch(entry: Any, rows: list[dict[str, Any]], model: str) -> list[dict[str, str]]:
    practice_set = {
        "id": rows[0]["set_id"],
        "title": rows[0]["set_title"],
        "description": "Item-level quality audit batch.",
        "items": [row["item"] for row in rows],
    }
    payload = {
        "model": model,
        "temperature": 0.15,
        "max_output_tokens": 5000,
        "input": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "You are a careful ESL assessment quality auditor. "
                            "Review each item independently using mainstream ESL test standards."
                        ),
                    }
                ],
            },
            {"role": "user", "content": [{"type": "input_text", "text": build_review_prompt(entry, practice_set)}]},
        ],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "grammar_item_audit",
                "strict": True,
                "schema": build_review_schema(),
            }
        },
    }
    result = extract_response_json(api_request(payload))
    issues: list[dict[str, str]] = []
    for review_issue in result.get("issues", []):
        item_id = clean_text(str(review_issue.get("item_id", "")))
        reason = clean_text(str(review_issue.get("reason", "")))
        if item_id and reason:
            issues.append(issue(item_id, "medium", reason, "editorial"))
    for item_id in result.get("rejected_item_ids", []):
        clean_id = clean_text(str(item_id))
        if clean_id and not any(existing["item_id"] == clean_id for existing in issues):
            issues.append(issue(clean_id, "medium", "Editorial review rejected this item.", "editorial"))
    return issues


def editorial_audit(rows: list[dict[str, Any]], entries_by_number: dict[int, Any], batch_size: int, model: str) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    grouped: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(int(row["concept_number"]), str(row["set_id"]))].append(row)

    for (concept_number, _set_id), group_rows in sorted(grouped.items()):
        entry = entries_by_number[concept_number]
        if not should_run_editorial_review(entry):
            continue
        for start in range(0, len(group_rows), batch_size):
            batch = group_rows[start : start + batch_size]
            issues.extend(review_batch(entry, batch, model))
    return issues


def main() -> int:
    args = parse_args()
    data_dir = Path(args.data_dir)
    paths = bank_paths(data_dir, args.concept)
    missing = [path for path in paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing bank file: {path}", file=sys.stderr)
        return 2

    banks = [load_bank(path) for path in paths]
    rows = [row for bank, path in zip(banks, paths) for row in flatten_items(bank, path)]
    concepts = sorted({int(row["concept_number"]) for row in rows})
    entries = load_selected_entries(concepts)
    entries_by_number = {entry.number: entry for entry in entries}

    deterministic_issues = deterministic_audit(rows, entries_by_number)
    editorial_issues: list[dict[str, str]] = []
    if not args.deterministic_only:
        editorial_issues = editorial_audit(rows, entries_by_number, args.batch_size, args.model)

    all_issues = deterministic_issues + editorial_issues
    report = {
        "audited_files": [str(path) for path in paths],
        "audited_concepts": concepts,
        "audited_item_count": len(rows),
        "deterministic_issue_count": len(deterministic_issues),
        "editorial_issue_count": len(editorial_issues),
        "issue_count": len(all_issues),
        "issues": sorted(all_issues, key=lambda item: (item["severity"], item["item_id"], item["source"])),
    }

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    print(f"Audited items: {len(rows)}")
    print(f"Audited concepts: {', '.join(f'{number:02d}' for number in concepts)}")
    print(f"Deterministic issues: {len(deterministic_issues)}")
    print(f"Editorial issues: {len(editorial_issues)}")
    print(f"Report: {report_path}")
    return 1 if all_issues else 0


if __name__ == "__main__":
    sys.exit(main())
