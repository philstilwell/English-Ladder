from __future__ import annotations

import argparse
import json
import math
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from generate_grammar_concepts import (
    EXPERIMENTAL_ITEM_BANK_DIR,
    INDEX_URL,
    clean_text,
    extract_number,
    fetch_soup,
    load_entries,
    parse_entry,
)


API_URL = "https://api.openai.com/v1/responses"
MODEL = os.environ.get("ENGLISH_LADDER_ITEM_MODEL", "gpt-4.1")
ITEM_BANK_DIR = EXPERIMENTAL_ITEM_BANK_DIR
PUBLIC_LESSON_ITEM_TARGET = 24
TOTAL_TARGET = 44 * PUBLIC_LESSON_ITEM_TARGET
SPECIAL_GUIDANCE = {
    1: (
        "This concept should assess the core contrast among 'in', 'on', and 'at'. "
        "Keep the correct answer inside that three-way choice and avoid introducing outside fixes such as 'during' or 'into'. "
        "Use clean textbook categories: cities, countries, rooms, buildings, months, years, dates, days, clock times, surfaces, events, and public transport. "
        "Avoid borderline location nouns or nested place phrases where more than one preposition can sound acceptable depending on viewpoint, such as campus, corner, street-level landmarks, or large venues with both point and area interpretations. "
        "Also avoid weekend, holiday-period, and festival expressions whose preferred preposition can vary by dialect or by whether the meaning is a day or a period."
    ),
    2: (
        "This concept teaches a three-pattern system: 'go', 'go to', and 'go to the/a/an'. "
        "Use 'go' for destination adverbs or bare travel expressions such as home, abroad, inside, outside, upstairs, downstairs, and there. "
        "Use 'go to' for destination nouns that naturally appear without an article in the source pattern family, such as school, class, work, church, and bed. "
        "Use 'go to the/a/an' for specific countable destinations, buildings, events, stores, and places that require an article. "
        "Do not use distractors like 'go in', 'go at', or 'go into' unless the item is explicitly correcting that exact learner error, and avoid contexts where two patterns could both sound acceptable. "
        "Avoid nouns with regional article variation or context-dependent article use, such as hospital, bank, library, prison, university, or market. "
        "Also avoid adverbial destinations whose surrounding prepositions vary regionally, such as downtown. "
        "Prefer clearer source-aligned categories such as home, abroad, inside, Paris, school, class, work, church, bed, the mountains, the store, and the concert. "
        "Within the article-required pattern, prefer destinations that naturally take the definite article in these teaching contexts; do not force learners to choose between 'the' and 'a/an' unless only one article is unmistakably correct. "
        "For meaning-and-contrast items, prefer fuller sentence choices or rewrites when that makes the distractors more plausible than bare fragments."
    ),
    7: (
        "This concept teaches standard verb and adjective patterns with 'about'. "
        "Use clear, mainstream collocations such as talk about, speak about, think about, worry about, complain about, argue about, ask about, learn about, know about, hear about, read about, write about, be concerned about, and be excited about. "
        "Avoid treating grammatical alternatives as errors; for example, 'wrote her experiences' and 'wrote about her experiences' can both be acceptable depending on meaning. "
        "Do not use awkward or nonstandard near-collocations such as 'read up about'; use 'read about' or 'read up on' only when the contrast is explicitly taught. "
        "Avoid laugh/laughed items unless the answer is 'laugh at' for the target of laughter or the item explicitly teaches 'laugh about' as discussing a humorous past event. "
        "Avoid dream/dreamed items because 'dream about' and 'dream of' are both standard in many contexts. "
        "Avoid excited items because 'excited about' and 'excited for' can both be standard depending on context. "
        "Make every item test whether 'about' is required, optional with a meaning change, or wrong after a specific verb/adjective."
    ),
}
CONCEPT_BANNED_TERMS = {
    1: ["weekend", "festival", "campus"],
    2: ["cinema", "hospital", "bank", "library", "downtown", "market", "university", "prison"],
    7: ["read up about", "laughed about the joke", "laugh about the joke", "dreamed", "dream about", "dream of", "excited about", "excited for"],
}
CONCEPT_ITEM_TYPE_OVERRIDES = {
    2: ["gap_fill", "sentence_choice", "best_rewrite"],
    7: ["gap_fill", "sentence_choice", "best_rewrite", "collocation_choice", "meaning_in_context"],
}
CONCEPT_MIN_ITEM_TYPES = {
    2: 1,
}
SKIP_EDITORIAL_REVIEW_CONCEPTS = {2}
SET_BLUEPRINTS = [
    (
        "core-grammar",
        "Core Grammar Forms",
        "Target the core form, structure, and sentence-building errors learners make with this concept.",
    ),
    (
        "meaning-and-contrast",
        "Meaning and Contrast",
        "Target close contrasts, meaning shifts, and high-confusion choices that strong distractors can expose.",
    ),
    (
        "vocabulary-and-usage",
        "Vocabulary and Usage",
        "Target collocation, lexical choice, word class, register, and other vocabulary-linked weaknesses tied to this concept.",
    ),
    (
        "mixed-diagnostic",
        "Mixed Diagnostic Set",
        "Mix grammar and vocabulary weaknesses in assessment-style items that feel like placement or progress-test questions.",
    ),
]
ITEM_TYPES = [
    "gap_fill",
    "sentence_choice",
    "error_detection",
    "best_rewrite",
    "collocation_choice",
    "word_form_choice",
    "meaning_in_context",
    "register_choice",
]
FOCUS_AREAS = ["grammar", "vocabulary", "mixed"]
CEFR_LEVELS = ["A1", "A2", "B1", "B2", "C1", "unrated"]
DIFFICULTY_LEVELS = ["easy", "medium", "hard", "unrated"]
SOURCE_STATUSES = ["original", "revised", "new", "retired", "experimental"]
SET_ATTEMPTS = 6
CONCEPT_ATTEMPTS = 2
REVIEW_ATTEMPTS = 2
SET_CHUNK_SIZE = 6
CONCEPT_CHUNK_SIZE_OVERRIDES = {
    2: 5,
}


def target_count_for_concept(number: int) -> int:
    return PUBLIC_LESSON_ITEM_TARGET


def split_target(total: int, buckets: int) -> list[int]:
    base = total // buckets
    remainder = total % buckets
    return [base + (1 if index < remainder else 0) for index in range(buckets)]


def split_generation_chunks(total: int, max_chunk_size: int = SET_CHUNK_SIZE) -> list[int]:
    chunk_count = max(1, math.ceil(total / max_chunk_size))
    return split_target(total, chunk_count)


def chunk_size_for_entry(entry) -> int:
    return CONCEPT_CHUNK_SIZE_OVERRIDES.get(entry.number, SET_CHUNK_SIZE)


def option_label(index: int) -> str:
    return chr(ord("A") + index)


def normalize_key(text: str) -> str:
    text = clean_text(text).lower()
    text = re.sub(r"\s+", " ", text)
    return text


def extract_focus_terms(entry) -> list[str]:
    title = clean_text(entry.title)
    terms: list[str] = []

    quoted = re.findall(r"[\"“”']([^\"“”']{1,40})[\"“”']", title)
    terms.extend(quoted)

    for pattern in [r"\b([A-Za-z][A-Za-z -]{1,20})\s+vs\.?\s+([A-Za-z][A-Za-z -]{1,20})\b"]:
        for left, right in re.findall(pattern, title, flags=re.I):
            terms.extend([left, right])

    if ":" in title:
        trailing = title.split(":", 1)[1]
        if any(separator in trailing for separator in ["/", "|"]):
            for part in re.split(r"[/|]", trailing):
                candidate = clean_text(part)
                if candidate and len(candidate.split()) <= 4:
                    terms.append(candidate)

    deduped: list[str] = []
    seen: set[str] = set()
    for term in terms:
        normalized = normalize_key(term)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(clean_text(term))
    return deduped[:8]


def concept_brief(entry) -> str:
    intro = " ".join(entry.intro[:3])
    section_titles = ", ".join(section.title for section in entry.sections[:8])
    sample_lines: list[str] = []
    for section in entry.sections[:4]:
        for block in section.blocks[:4]:
            if block["type"] == "paragraph":
                sample_lines.append(clean_text(str(block["text"])))
            elif block["type"] == "list":
                for item in block["items"][:2]:
                    sample_lines.append(clean_text(str(item["text"])))
            if len(sample_lines) >= 10:
                break
        if len(sample_lines) >= 10:
            break
    sample_items = []
    for item in entry.practice_items[:6]:
        stem = next((line for line in item.prompt_lines if not re.match(r"^[a-d]\)", line, re.I)), "")
        if stem:
            answer = " / ".join(clean_text(line) for line in item.answer_lines if clean_text(line))
            sample_items.append((clean_text(stem), answer))

    lines = [
        f"Concept number: {entry.number}",
        f"Concept title: {entry.title}",
        f"Intro summary: {intro}",
        f"Key section titles: {section_titles}",
        "Representative explanation lines:",
    ]
    lines.extend(f"- {line}" for line in sample_lines[:10])
    if sample_items:
        lines.append("Existing or source-inspired sample item patterns:")
        for stem, answer in sample_items:
            if answer:
                lines.append(f"- Stem: {stem} | Correct answer pattern: {answer}")
            else:
                lines.append(f"- Stem: {stem}")
    return "\n".join(lines)


def build_system_prompt() -> str:
    return textwrap_dedent(
        """
        You are an expert ESL assessment writer creating high-quality grammar and vocabulary items.
        Write assessment-style items that resemble placement tests, progress tests, or diagnostic checks.

        Non-negotiable requirements:
        - Every item must test a distinct learner weakness within the concept.
        - Focus on both grammar and vocabulary.
        - Use natural, idiomatic English.
        - Distractors must be plausible and diagnostically useful, not random.
        - Avoid near-duplicate stems, recycled wording, and pattern drilling.
        - Make each explanation short, accurate, and directly tied to the learner weakness.
        - Do not include trivia, culture-specific specialist knowledge, or vague opinion questions.
        - Use standard, internationally understandable English unless the concept explicitly teaches a regional contrast.
        - Avoid ambiguous items with more than one defensibly correct answer.
        - Keep the correct answer inside the concept's core contrast whenever that is the point being tested.
        - Do not introduce outside grammar fixes that bypass the concept being assessed.
        - Make options parallel in grammar, length, and style whenever possible.
        - For pattern or phrase-choice concepts, make every option a realistic learner choice, not an obviously impossible fragment.
        - Stay close to the source concept's own categories and fixed expressions; avoid borderline cases that vary by dialect or register.
        - Return only JSON that matches the schema.
        """
    )


def concept_specific_guidance(entry) -> str:
    return SPECIAL_GUIDANCE.get(entry.number, "")


def allowed_item_types(entry) -> list[str]:
    return CONCEPT_ITEM_TYPE_OVERRIDES.get(entry.number, ITEM_TYPES)


def banned_terms(entry) -> list[str]:
    return CONCEPT_BANNED_TERMS.get(entry.number, [])


def min_required_item_types(entry, expected_count: int) -> int:
    return CONCEPT_MIN_ITEM_TYPES.get(entry.number, min(2, max(1, expected_count)))


def should_run_editorial_review(entry) -> bool:
    return entry.number not in SKIP_EDITORIAL_REVIEW_CONCEPTS


def textwrap_dedent(text: str) -> str:
    lines = [line.rstrip() for line in text.strip().splitlines()]
    margin = min((len(line) - len(line.lstrip())) for line in lines if line)
    return "\n".join(line[margin:] for line in lines)


def build_ssl_context() -> ssl.SSLContext:
    try:
        import certifi
    except ImportError:
        return ssl._create_unverified_context()
    return ssl.create_default_context(cafile=certifi.where())


SSL_CONTEXT = build_ssl_context()


def build_user_prompt(entry, target_count: int, prior_issues: list[str] | None) -> str:
    set_counts = split_target(target_count, len(SET_BLUEPRINTS))
    set_lines = []
    for (set_id, title, description), count in zip(SET_BLUEPRINTS, set_counts):
        set_lines.append(f"- {title} ({set_id}): {count} items. {description}")

    issue_block = ""
    if prior_issues:
        bullets = "\n".join(f"- {issue}" for issue in prior_issues[:20])
        issue_block = f"\nFix these problems from the previous attempt:\n{bullets}\n"

    return (
        f"Create a local assessment bank for this English Ladder grammar concept.\n\n"
        f"{concept_brief(entry)}\n\n"
        f"Target total: {target_count} items.\n"
        f"Assessment sets and counts:\n" + "\n".join(set_lines) + "\n\n"
        "Item-writing rules:\n"
        "- Use exactly 4 options for every item.\n"
        "- Use exactly one correct option for every item.\n"
        "- Make weakness_tag distinct for every item within this concept.\n"
        "- Balance focus_area across grammar, vocabulary, and mixed items.\n"
        "- Use the item_type field to vary what is being tested.\n"
        "- Add cefr_level, difficulty, and source_status metadata to every item.\n"
        "- Use source_status 'new' for generated items that have not yet been hand-approved.\n"
        "- Keep explanations under 28 words.\n"
        "- Include a meaningful mix of sentence-level and short-context items.\n"
        "- Ensure vocabulary items still connect naturally to the concept focus.\n"
        "- Avoid repeating the same sentence frame more than once.\n"
        "- Keep questions self-contained and mobile-friendly.\n"
        "- In every set, use at least three different item_type values.\n"
        "- Make the Vocabulary and Usage set mostly vocabulary or mixed items.\n"
        "- Make the Mixed Diagnostic Set mostly mixed-focus items.\n"
        "- Across the whole concept, include at least 15 vocabulary items and at least 15 mixed items when the target is 86 or 87.\n"
        f"{issue_block}"
    )


def build_set_prompt(
    entry,
    target_count: int,
    set_index: int,
    set_id: str,
    title: str,
    description: str,
    item_count: int,
    existing_items: list[dict[str, object]],
    prior_issues: list[str] | None,
) -> str:
    existing_block = ""
    if existing_items:
        weaknesses = [clean_text(str(item["weakness_tag"])) for item in existing_items[-24:]]
        stems = [clean_text(str(item["question"])) for item in existing_items[-24:]]
        existing_block = (
            "\nAlready generated material that you must not duplicate or closely paraphrase:\n"
            "Used weakness tags:\n"
            + "\n".join(f"- {weakness}" for weakness in weaknesses)
            + "\nUsed question stems:\n"
            + "\n".join(f"- {stem}" for stem in stems)
            + "\nDo not reuse these weaknesses, stem openings, or near-paraphrases of them.\n"
        )

    issue_block = ""
    if prior_issues:
        issue_block = "\nFix these problems from the previous attempt:\n" + "\n".join(
            f"- {issue}" for issue in prior_issues[:20]
        ) + "\n"

    set_focus_rules = {
        "core-grammar": [
            "Make most items grammar-focused.",
            "Prioritize form, sentence building, and structural control.",
        ],
        "meaning-and-contrast": [
            "Mix grammar and mixed-focus items.",
            "Target close contrasts, nuance, and choice under pressure.",
        ],
        "vocabulary-and-usage": [
            "Make this set mostly vocabulary or mixed items.",
            "Target collocation, lexical choice, word class, register, and meaning in context.",
        ],
        "mixed-diagnostic": [
            "Make this set predominantly mixed-focus items.",
            "In small pilot sets, make at least 4 of 5 items mixed-focus; in larger sets, keep roughly 70% or more mixed-focus.",
            "Blend grammar and vocabulary weaknesses in test-like diagnostics.",
        ],
    }
    focus_rules = "\n".join(f"- {rule}" for rule in set_focus_rules[set_id])
    allowed_types = allowed_item_types(entry)
    focus_terms = extract_focus_terms(entry)
    focus_term_block = ""
    if focus_terms:
        focus_term_block = (
            "- Central focus terms for this concept include: "
            + ", ".join(f"'{term}'" for term in focus_terms)
            + ".\n"
            "- Keep the correct answer inside that contrast set whenever natural, unless the source concept clearly expands beyond it.\n"
        )
    special_guidance = concept_specific_guidance(entry)
    special_guidance_block = ""
    if special_guidance:
        special_guidance_block = f"- Special concept guidance: {special_guidance}\n"
    allowed_type_block = ""
    if allowed_types != ITEM_TYPES:
        allowed_type_block = "- Only use these item_type values for this concept: " + ", ".join(allowed_types) + ".\n"

    return (
        f"Create one assessment set for this English Ladder grammar concept.\n\n"
        f"{concept_brief(entry)}\n\n"
        f"Overall concept target: {target_count} items.\n"
        f"Current set: {title} ({set_id}).\n"
        f"Set description: {description}\n"
        f"Set target: {item_count} items.\n\n"
        "Rules:\n"
        "- Use exactly 4 options for every item.\n"
        "- Use exactly one correct option for every item.\n"
        "- Make every weakness_tag distinct within this concept.\n"
        "- Use at least three different item_type values in this set.\n"
        "- Add cefr_level, difficulty, and source_status metadata to every item.\n"
        "- Use source_status 'new' for generated items that have not yet been hand-approved.\n"
        "- Keep explanations between 5 and 28 words.\n"
        "- Make distractors plausible and diagnostically meaningful.\n"
        "- Make sure exactly one option is clearly defensible in standard English.\n"
        "- Avoid regional-variation ambiguity unless the item explicitly names the variety.\n"
        "- Avoid noun or context choices that make multiple answers plausible in the real world.\n"
        "- Avoid repeated sentence frames.\n"
        "- Do not reuse the same question opening or stem pattern from earlier sets.\n"
        "- Keep the questions self-contained and assessment-style.\n"
        "- When a concept tests phrase patterns or formula choices, keep all four options as realistic learner completions from that pattern family.\n"
        "- Do not use obviously impossible fillers such as random preposition swaps unless they are real learner confusions within this concept.\n"
        "- Stay close to the source concept's own categories and avoid borderline nouns or contexts that could make two patterns acceptable.\n"
        f"{focus_term_block}"
        f"{special_guidance_block}"
        f"{allowed_type_block}"
        f"{focus_rules}\n"
        f"{existing_block}"
        f"{issue_block}"
    )


def build_item_schema(allowed_types: list[str] | None = None) -> dict[str, object]:
    type_enum = allowed_types or ITEM_TYPES
    return {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "focus_area": {"type": "string", "enum": FOCUS_AREAS},
            "item_type": {"type": "string", "enum": type_enum},
            "cefr_level": {"type": "string", "enum": CEFR_LEVELS},
            "difficulty": {"type": "string", "enum": DIFFICULTY_LEVELS},
            "source_status": {"type": "string", "enum": SOURCE_STATUSES},
            "subskill": {"type": "string"},
            "weakness_tag": {"type": "string"},
            "question": {"type": "string"},
            "options": {
                "type": "array",
                "minItems": 4,
                "maxItems": 4,
                "items": {"type": "string"},
            },
            "correct_index": {
                "type": "integer",
                "minimum": 0,
                "maximum": 3,
            },
            "explanation": {"type": "string"},
        },
        "required": [
            "id",
            "focus_area",
            "item_type",
            "cefr_level",
            "difficulty",
            "source_status",
            "subskill",
            "weakness_tag",
            "question",
            "options",
            "correct_index",
            "explanation",
        ],
        "additionalProperties": False,
    }


def build_set_schema(set_id: str, title: str, item_count: int, allowed_types: list[str] | None = None) -> dict[str, object]:
    return {
        "type": "object",
        "properties": {
            "id": {"type": "string", "const": set_id},
            "title": {"type": "string", "const": title},
            "description": {"type": "string"},
            "items": {
                "type": "array",
                "minItems": item_count,
                "maxItems": item_count,
                "items": build_item_schema(allowed_types),
            },
        },
        "required": ["id", "title", "description", "items"],
        "additionalProperties": False,
    }


def build_replacement_schema(item_count: int, allowed_types: list[str] | None = None) -> dict[str, object]:
    return {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "minItems": item_count,
                "maxItems": item_count,
                "items": build_item_schema(allowed_types),
            }
        },
        "required": ["items"],
        "additionalProperties": False,
    }


def build_review_schema() -> dict[str, object]:
    return {
        "type": "object",
        "properties": {
            "approved": {"type": "boolean"},
            "summary": {"type": "string"},
            "rejected_item_ids": {
                "type": "array",
                "items": {"type": "string"},
            },
            "issues": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["item_id", "reason"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["approved", "summary", "rejected_item_ids", "issues"],
        "additionalProperties": False,
    }


def build_schema(target_count: int) -> dict[str, object]:
    set_counts = split_target(target_count, len(SET_BLUEPRINTS))
    set_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "title": {"type": "string"},
            "description": {"type": "string"},
            "items": {
                "type": "array",
                "minItems": min(set_counts),
                "maxItems": max(set_counts),
                "items": build_item_schema(),
            },
        },
        "required": ["id", "title", "description", "items"],
        "additionalProperties": False,
    }

    return {
        "type": "object",
        "properties": {
            "concept_number": {"type": "integer"},
            "concept_title": {"type": "string"},
            "schema_version": {"type": "integer", "const": 2},
            "publication_status": {"type": "string", "enum": ["experimental", "public_candidate", "public", "retired"]},
            "target_public_item_count": {"type": "integer"},
            "assessment_intro": {"type": "string"},
            "assessment_sets": {
                "type": "array",
                "minItems": len(SET_BLUEPRINTS),
                "maxItems": len(SET_BLUEPRINTS),
                "items": set_schema,
            },
        },
        "required": [
            "concept_number",
            "concept_title",
            "schema_version",
            "publication_status",
            "target_public_item_count",
            "assessment_intro",
            "assessment_sets",
        ],
        "additionalProperties": False,
    }


def build_review_prompt(entry, practice_set: dict[str, object]) -> str:
    items_json = json.dumps(practice_set["items"], ensure_ascii=True, indent=2)
    focus_terms = extract_focus_terms(entry)
    focus_block = ""
    if focus_terms:
        focus_block = (
            "Central focus terms for this concept: "
            + ", ".join(f"'{term}'" for term in focus_terms)
            + ".\n"
        )
    return (
        "Review this ESL assessment set as a strict editorial quality checker.\n\n"
        f"{concept_brief(entry)}\n\n"
        f"Set id: {practice_set['id']}\n"
        f"Set title: {practice_set['title']}\n"
        f"{focus_block}\n"
        "Reject any item that has one or more of these problems:\n"
        "- more than one defensibly correct answer\n"
        "- an answer that depends on regional variation without saying so\n"
        "- an out-of-scope fix that bypasses the concept\n"
        "- unnatural, awkward, or misleading English\n"
        "- a distractor set that is random, trivial, or unrelated rather than a genuine learner choice\n"
        "- an explanation that does not match the answer\n"
        "- too much overlap with another item in this set\n\n"
        "Use mainstream ESL classroom and assessment standards.\n"
        "For gap-fill items, judge the completed sentence with the selected option inserted, not the raw stem fragment by itself.\n"
        "Do not reject an item because of a remote, highly marked, elliptical, or niche dialect reading that ordinary learners would not reasonably be expected to consider.\n"
        "Do not reject an item merely because it is easier than others if it still tests a real learner pattern with coherent distractors.\n"
        "Be selective but strict. Reject only the items that should be rewritten, not the whole set by default.\n\n"
        "Set items:\n"
        f"{items_json}\n"
    )


def api_request(payload: dict[str, object]) -> dict[str, object]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required to build the grammar item bank.")

    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=240, context=SSL_CONTEXT) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API request failed with HTTP {exc.code}: {body}") from exc


def extract_response_json(response: dict[str, object]) -> dict[str, object]:
    last_error: Exception | None = None
    for output in response.get("output", []):
        for content in output.get("content", []):
            if content.get("type") == "output_text":
                text = content.get("text", "")
                if not text or not text.strip():
                    continue
                try:
                    return json.loads(text)
                except json.JSONDecodeError as exc:
                    last_error = exc
                    continue
    if last_error is not None:
        raise RuntimeError(f"The OpenAI response contained output_text, but it was not valid JSON: {last_error}") from last_error
    raise RuntimeError("The OpenAI response did not contain output_text JSON.")


def count_focus_areas(items: list[dict[str, object]]) -> dict[str, int]:
    counts = {key: 0 for key in FOCUS_AREAS}
    for item in items:
        counts[item["focus_area"]] += 1
    return counts


def validate_banned_terms(entry, item: dict[str, object], item_id: str) -> list[str]:
    terms = banned_terms(entry)
    if not terms:
        return []
    haystacks = [
        clean_text(str(item.get("question", ""))).lower(),
        *[clean_text(str(option)).lower() for option in item.get("options", [])],
    ]
    issues = []
    for term in terms:
        token = term.lower()
        if any(token in haystack for haystack in haystacks):
            issues.append(f"{item_id} uses banned concept term '{term}'.")
    return issues


def review_practice_set(entry, practice_set: dict[str, object], model: str) -> list[str]:
    issues: list[str] = []
    for _ in range(REVIEW_ATTEMPTS):
        payload = {
            "model": model,
            "temperature": 0.2,
            "max_output_tokens": 5000,
            "input": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": (
                                "You are a strict ESL assessment editor. Return JSON only. "
                                "Reject items only when there is a real quality problem under mainstream ESL testing standards."
                            ),
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": build_review_prompt(entry, practice_set)}],
                },
            ],
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "grammar_set_review",
                    "strict": True,
                    "schema": build_review_schema(),
                }
            },
        }
        response = api_request(payload)
        result = extract_response_json(response)
        rejected_item_ids = [clean_text(str(item_id)) for item_id in result.get("rejected_item_ids", []) if clean_text(str(item_id))]
        review_issues = result.get("issues", [])
        issues = []
        for review_issue in review_issues:
            item_id = clean_text(str(review_issue.get("item_id", "")))
            reason = clean_text(str(review_issue.get("reason", "")))
            if item_id and reason:
                issues.append(f"{item_id} {reason}")
        if result.get("approved") and not rejected_item_ids and not issues:
            return []
        if rejected_item_ids and not issues:
            issues = [f"{item_id} editorial review rejected this item." for item_id in rejected_item_ids]
        if issues:
            return issues
    return issues


def apply_stable_item_ids(concept_number: int, practice_sets: list[dict[str, object]]) -> None:
    for set_index, practice_set in enumerate(practice_sets, start=1):
        for item_index, item in enumerate(practice_set.get("items", []), start=1):
            item["id"] = f"c{concept_number:02d}-s{set_index:02d}-i{item_index:03d}"


def assign_temporary_set_item_ids(practice_set: dict[str, object], prefix: str) -> None:
    for item_index, item in enumerate(practice_set.get("items", []), start=1):
        item["id"] = f"{prefix}-i{item_index:03d}"


def validate_payload(entry, payload: dict[str, object], target_count: int) -> list[str]:
    problems: list[str] = []
    if payload.get("concept_number") != entry.number:
        problems.append("concept_number does not match the requested concept.")
    if clean_text(str(payload.get("concept_title", ""))) != clean_text(entry.title):
        problems.append("concept_title does not match the requested concept title.")

    practice_sets = payload.get("assessment_sets", [])
    if len(practice_sets) != len(SET_BLUEPRINTS):
        problems.append("assessment_sets does not contain exactly four sets.")
        return problems

    all_items: list[dict[str, object]] = []
    seen_ids: set[str] = set()
    seen_questions: set[str] = set()
    seen_weaknesses: set[str] = set()
    expected_counts = split_target(target_count, len(SET_BLUEPRINTS))

    for index, (practice_set, blueprint, expected_count) in enumerate(zip(practice_sets, SET_BLUEPRINTS, expected_counts), start=1):
        set_id, set_title, _ = blueprint
        if practice_set.get("id") != set_id:
            problems.append(f"set {index} id should be {set_id}.")
        if clean_text(str(practice_set.get("title", ""))) != clean_text(set_title):
            problems.append(f"set {index} title should be {set_title}.")
        items = practice_set.get("items", [])
        if len(items) != expected_count:
            problems.append(f"set {index} should contain {expected_count} items.")

        set_item_types: set[str] = set()
        for item in items:
            all_items.append(item)
            item_id = clean_text(str(item.get("id", "")))
            if not item_id:
                problems.append("item id is blank.")
            elif item_id in seen_ids:
                problems.append(f"duplicate item id: {item_id}.")
            seen_ids.add(item_id)

            question = clean_text(str(item.get("question", "")))
            if not question:
                problems.append(f"{item_id} has a blank question.")
            normalized_question = normalize_key(question)
            if normalized_question in seen_questions:
                problems.append(f"{item_id} duplicates an existing question stem.")
            seen_questions.add(normalized_question)

            weakness = clean_text(str(item.get("weakness_tag", "")))
            if not weakness:
                problems.append(f"{item_id} has a blank weakness_tag.")
            normalized_weakness = normalize_key(weakness)
            if normalized_weakness in seen_weaknesses:
                problems.append(f"{item_id} repeats an existing weakness_tag.")
            seen_weaknesses.add(normalized_weakness)

            options = [clean_text(str(option)) for option in item.get("options", [])]
            if len(options) != 4:
                problems.append(f"{item_id} does not contain exactly four options.")
            if len({normalize_key(option) for option in options}) != len(options):
                problems.append(f"{item_id} contains duplicate options.")

            correct_index = item.get("correct_index")
            if not isinstance(correct_index, int) or not 0 <= correct_index < len(options):
                problems.append(f"{item_id} has an invalid correct_index.")

            explanation = clean_text(str(item.get("explanation", "")))
            if len(explanation.split()) < 5:
                problems.append(f"{item_id} explanation is too short.")
            if len(explanation.split()) > 28:
                problems.append(f"{item_id} explanation is too long.")

            problems.extend(validate_banned_terms(entry, item, item_id))

            if item.get("item_type") not in ITEM_TYPES:
                problems.append(f"{item_id} uses an unsupported item_type.")
            else:
                set_item_types.add(str(item["item_type"]))

            if item.get("focus_area") not in FOCUS_AREAS:
                problems.append(f"{item_id} uses an unsupported focus_area.")

            if item.get("cefr_level") not in CEFR_LEVELS:
                problems.append(f"{item_id} uses an unsupported cefr_level.")
            if item.get("difficulty") not in DIFFICULTY_LEVELS:
                problems.append(f"{item_id} uses an unsupported difficulty.")
            if item.get("source_status") not in SOURCE_STATUSES:
                problems.append(f"{item_id} uses an unsupported source_status.")

        required_set_types = min_required_item_types(entry, expected_count)
        if len(set_item_types) < required_set_types:
            problems.append(f"set {index} should use at least {required_set_types} different item types.")

    if len(all_items) != target_count:
        problems.append(f"total item count should be {target_count}, got {len(all_items)}.")

    focus_counts = count_focus_areas(all_items)
    if focus_counts["vocabulary"] < max(2 if target_count < 40 else 4, target_count // 6):
        problems.append("not enough vocabulary-focused items.")
    if focus_counts["mixed"] < max(2 if target_count < 40 else 4, target_count // 6):
        problems.append("not enough mixed-focus items.")

    return problems


def validate_practice_set(
    entry,
    practice_set: dict[str, object],
    set_id: str,
    set_title: str,
    expected_count: int,
    existing_items: list[dict[str, object]],
    *,
    enforce_set_mix: bool = True,
) -> list[str]:
    problems: list[str] = []
    if practice_set.get("id") != set_id:
        problems.append(f"set id should be {set_id}.")
    if clean_text(str(practice_set.get("title", ""))) != clean_text(set_title):
        problems.append(f"set title should be {set_title}.")

    items = practice_set.get("items", [])
    if len(items) != expected_count:
        problems.append(f"set should contain {expected_count} items.")

    seen_questions = {normalize_key(clean_text(str(item["question"]))) for item in existing_items}
    seen_weaknesses = {normalize_key(clean_text(str(item["weakness_tag"]))) for item in existing_items}
    local_questions: set[str] = set()
    local_weaknesses: set[str] = set()
    local_ids: set[str] = set()
    set_item_types: set[str] = set()
    focus_counts = {key: 0 for key in FOCUS_AREAS}

    for item in items:
        item_id = clean_text(str(item.get("id", "")))
        if not item_id:
            problems.append("item id is blank.")
        elif item_id in local_ids:
            problems.append(f"{item_id} duplicates an existing item id in this set.")
        local_ids.add(item_id)

        question = clean_text(str(item.get("question", "")))
        normalized_question = normalize_key(question)
        if normalized_question in seen_questions or normalized_question in local_questions:
            problems.append(f"{item_id or '[blank id]'} duplicates an existing question stem.")
        local_questions.add(normalized_question)

        weakness = clean_text(str(item.get("weakness_tag", "")))
        normalized_weakness = normalize_key(weakness)
        if normalized_weakness in seen_weaknesses or normalized_weakness in local_weaknesses:
            problems.append(f"{item_id or '[blank id]'} repeats an existing weakness_tag.")
        local_weaknesses.add(normalized_weakness)

        options = [clean_text(str(option)) for option in item.get("options", [])]
        if len(options) != 4:
            problems.append(f"{item_id} does not contain exactly four options.")
        if len({normalize_key(option) for option in options}) != len(options):
            problems.append(f"{item_id} contains duplicate options.")

        explanation = clean_text(str(item.get("explanation", "")))
        if len(explanation.split()) < 5:
            problems.append(f"{item_id} explanation is too short.")
        if len(explanation.split()) > 28:
            problems.append(f"{item_id} explanation is too long.")

        problems.extend(validate_banned_terms(entry, item, item_id))

        item_type = str(item.get("item_type", ""))
        if item_type in ITEM_TYPES:
            set_item_types.add(item_type)
        else:
            problems.append(f"{item_id} uses an unsupported item_type.")

        focus_area = str(item.get("focus_area", ""))
        if focus_area in FOCUS_AREAS:
            focus_counts[focus_area] += 1
        else:
            problems.append(f"{item_id} uses an unsupported focus_area.")

        if item.get("cefr_level") not in CEFR_LEVELS:
            problems.append(f"{item_id} uses an unsupported cefr_level.")
        if item.get("difficulty") not in DIFFICULTY_LEVELS:
            problems.append(f"{item_id} uses an unsupported difficulty.")
        if item.get("source_status") not in SOURCE_STATUSES:
            problems.append(f"{item_id} uses an unsupported source_status.")

    if enforce_set_mix:
        required_set_types = min_required_item_types(entry, expected_count)
        if len(set_item_types) < required_set_types:
            problems.append(f"set should use at least {required_set_types} different item types.")

        if set_id == "vocabulary-and-usage" and focus_counts["vocabulary"] + focus_counts["mixed"] < max(2, expected_count // 3):
            problems.append("vocabulary-and-usage set needs more vocabulary or mixed items.")
        if set_id == "mixed-diagnostic" and focus_counts["mixed"] < max(2, expected_count // 3):
            problems.append("mixed-diagnostic set needs more mixed items.")

    return problems


def extract_problem_item_ids(problems: list[str]) -> list[str]:
    item_ids: list[str] = []
    for issue in problems:
        match = re.match(r"([A-Za-z0-9_-]+)\b", issue)
        if not match:
            continue
        item_id = match.group(1)
        if item_id.lower() == "set":
            continue
        item_ids.append(item_id)
    deduped: list[str] = []
    seen: set[str] = set()
    for item_id in item_ids:
        if item_id in seen:
            continue
        seen.add(item_id)
        deduped.append(item_id)
    return deduped


def build_replacement_prompt(
    entry,
    target_count: int,
    set_id: str,
    title: str,
    description: str,
    replacement_count: int,
    existing_items: list[dict[str, object]],
    issues: list[str],
) -> str:
    weaknesses = [clean_text(str(item["weakness_tag"])) for item in existing_items]
    stems = [clean_text(str(item["question"])) for item in existing_items]
    special_guidance = concept_specific_guidance(entry)
    special_guidance_block = f"- Special concept guidance: {special_guidance}\n" if special_guidance else ""
    return (
        f"Create {replacement_count} replacement ESL assessment items for the {title} set.\n\n"
        f"{concept_brief(entry)}\n\n"
        f"Overall concept target: {target_count} items.\n"
        f"Set id: {set_id}\n"
        f"Set description: {description}\n\n"
        "These replacements must fix the following issues:\n"
        + "\n".join(f"- {issue}" for issue in issues[:20])
        + "\n\nAlready used weakness tags to avoid:\n"
        + "\n".join(f"- {weakness}" for weakness in weaknesses)
        + "\nAlready used question stems to avoid:\n"
        + "\n".join(f"- {stem}" for stem in stems)
        + "\nRules:\n"
        "- Use exactly 4 options.\n"
        "- Use exactly one correct option.\n"
        "- Include cefr_level, difficulty, and source_status metadata.\n"
        "- Use source_status 'new' for replacement items until a human editor approves them.\n"
        "- Keep explanations between 5 and 28 words.\n"
        "- Do not duplicate or closely paraphrase any used stem or weakness.\n"
        "- Ensure exactly one answer is defensibly correct in standard English.\n"
        "- Avoid regional-variation ambiguity unless explicitly labeled.\n"
        "- Keep the replacement inside the concept's own contrast, not an outside fix.\n"
        "- If the concept is about phrase patterns, all options must be realistic completions from that pattern family.\n"
        "- Stay close to the source concept's own categories and avoid borderline nouns or contexts.\n"
        f"{special_guidance_block}"
        "- Keep the items assessment-style and mobile-friendly.\n"
    )


def request_replacement_items(
    entry,
    target_count: int,
    set_id: str,
    set_title: str,
    set_description: str,
    replacement_count: int,
    existing_items: list[dict[str, object]],
    issues: list[str],
    model: str,
    id_prefix: str,
) -> list[dict[str, object]]:
    schema = build_replacement_schema(replacement_count, allowed_item_types(entry))
    last_issues = issues

    for _ in range(5):
        payload = {
            "model": model,
            "temperature": 0.15,
            "max_output_tokens": 5000,
            "input": [
                {
                    "role": "system",
                    "content": [{"type": "input_text", "text": build_system_prompt()}],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": build_replacement_prompt(
                                entry,
                                target_count,
                                set_id,
                                set_title,
                                set_description,
                                replacement_count,
                                existing_items,
                                last_issues,
                            ),
                        }
                    ],
                },
            ],
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": f"grammar_{set_id.replace('-', '_')}_replacements",
                    "strict": True,
                    "schema": schema,
                }
            },
        }
        response = api_request(payload)
        result = extract_response_json(response)
        replacements = result["items"]
        for index, item in enumerate(replacements, start=1):
            item["id"] = f"{id_prefix}-i{index:03d}"
        temp_set = {
            "id": set_id,
            "title": set_title,
            "description": set_description,
            "items": replacements,
        }
        validation_issues = validate_practice_set(
            entry,
            temp_set,
            set_id,
            set_title,
            replacement_count,
            existing_items,
            enforce_set_mix=False,
        )
        if not validation_issues:
            return replacements
        last_issues = validation_issues

    raise RuntimeError(
        f"Unable to generate replacement items for concept {entry.number:02d} {set_id}:\n"
        + "\n".join(f"- {issue}" for issue in last_issues)
    )


def request_set_chunk(
    entry,
    target_count: int,
    set_index: int,
    chunk_index: int,
    blueprint: tuple[str, str, str],
    item_count: int,
    existing_items: list[dict[str, object]],
    model: str,
    concept_issues: list[str] | None,
) -> dict[str, object]:
    set_id, set_title, set_description = blueprint
    issues = concept_issues
    schema = build_set_schema(set_id, set_title, item_count, allowed_item_types(entry))
    last_result: dict[str, object] | None = None

    for _ in range(SET_ATTEMPTS):
        payload = {
            "model": model,
            "temperature": 0.55,
            "max_output_tokens": 12000,
            "input": [
                {
                    "role": "system",
                    "content": [{"type": "input_text", "text": build_system_prompt()}],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": build_set_prompt(
                                entry,
                                target_count,
                                set_index,
                                set_id,
                                set_title,
                                set_description,
                                item_count,
                                existing_items,
                                issues,
                            ),
                        }
                    ],
                },
            ],
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": f"grammar_{set_id.replace('-', '_')}",
                    "strict": True,
                    "schema": schema,
                }
            },
        }
        response = api_request(payload)
        result = extract_response_json(response)
        assign_temporary_set_item_ids(result, f"draft-s{set_index:02d}-c{chunk_index:02d}")
        last_result = result
        issues = validate_practice_set(entry, result, set_id, set_title, item_count, existing_items)
        if not issues and should_run_editorial_review(entry):
            issues = review_practice_set(entry, result, model)
        if not issues:
            return result
        time.sleep(1.0)

    if last_result is not None and issues:
        current_ids = {clean_text(str(item.get("id", ""))) for item in last_result["items"]}
        bad_ids = [item_id for item_id in extract_problem_item_ids(issues) if item_id in current_ids]
        if bad_ids and len(bad_ids) < item_count:
            keep_items = [
                item for item in last_result["items"]
                if clean_text(str(item.get("id", ""))) not in set(bad_ids)
            ]
            replacements = request_replacement_items(
                entry,
                target_count,
                set_id,
                set_title,
                set_description,
                len(bad_ids),
                [*existing_items, *keep_items],
                issues,
                model,
                f"repair-s{set_index:02d}-c{chunk_index:02d}",
            )
            if len(keep_items) + len(replacements) != item_count:
                raise RuntimeError(
                    f"Replacement merge failed for concept {entry.number:02d} {set_id}: "
                    f"expected {item_count} items, got {len(keep_items) + len(replacements)}."
                )
            repaired = {
                "id": set_id,
                "title": set_title,
                "description": last_result.get("description", set_description),
                "items": [*keep_items, *replacements],
            }
            issues = validate_practice_set(entry, repaired, set_id, set_title, item_count, existing_items)
            if not issues and should_run_editorial_review(entry):
                issues = review_practice_set(entry, repaired, model)
            if not issues:
                return repaired

    raise RuntimeError(
        f"Unable to generate a valid practice set for concept {entry.number:02d} {set_id}:\n"
        + "\n".join(f"- {issue}" for issue in issues or ["unknown error"])
    )


def request_practice_set(
    entry,
    target_count: int,
    set_index: int,
    blueprint: tuple[str, str, str],
    item_count: int,
    existing_items: list[dict[str, object]],
    model: str,
    concept_issues: list[str] | None,
) -> dict[str, object]:
    set_id, set_title, set_description = blueprint
    chunk_sizes = split_generation_chunks(item_count, chunk_size_for_entry(entry))
    chunked_items: list[dict[str, object]] = []

    for chunk_index, chunk_size in enumerate(chunk_sizes, start=1):
        chunk_result = request_set_chunk(
            entry,
            target_count,
            set_index,
            chunk_index,
            blueprint,
            chunk_size,
            [*existing_items, *chunked_items],
            model,
            concept_issues,
        )
        chunked_items.extend(chunk_result["items"])

    combined = {
        "id": set_id,
        "title": set_title,
        "description": set_description,
        "items": chunked_items,
    }
    final_issues = validate_practice_set(entry, combined, set_id, set_title, item_count, existing_items)
    if final_issues:
        raise RuntimeError(
            f"Unable to combine chunked set for concept {entry.number:02d} {set_id}:\n"
            + "\n".join(f"- {issue}" for issue in final_issues)
        )
    return combined


def request_concept_bank(entry, target_count: int, model: str) -> dict[str, object]:
    for attempt in range(1, CONCEPT_ATTEMPTS + 1):
        set_counts = split_target(target_count, len(SET_BLUEPRINTS))
        generated_sets = []
        generated_items: list[dict[str, object]] = []
        concept_issues: list[str] | None = None

        for set_index, (blueprint, item_count) in enumerate(zip(SET_BLUEPRINTS, set_counts), start=1):
            practice_set = request_practice_set(
                entry,
                target_count,
                set_index,
                blueprint,
                item_count,
                generated_items,
                model,
                concept_issues,
            )
            generated_sets.append(practice_set)
            generated_items.extend(practice_set["items"])

        result = {
            "concept_number": entry.number,
            "concept_title": entry.title,
            "schema_version": 2,
            "publication_status": "experimental",
            "target_public_item_count": PUBLIC_LESSON_ITEM_TARGET,
            "assessment_intro": (
                "These assessment sets check grammar, vocabulary, meaning, and test-style decision-making across this concept."
            ),
            "assessment_sets": generated_sets,
        }
        apply_stable_item_ids(entry.number, generated_sets)
        issues = validate_payload(entry, result, target_count)
        if not issues:
            return result
        concept_issues = issues
        time.sleep(1.0)

    raise RuntimeError(
        f"Unable to generate a valid item bank for concept {entry.number:02d} after {CONCEPT_ATTEMPTS} attempts:\n"
        + "\n".join(f"- {issue}" for issue in issues or ["unknown error"])
    )


def load_selected_entries(concepts: list[int] | None):
    if not concepts:
        return load_entries()

    wanted = set(concepts)
    soup = fetch_soup(INDEX_URL)
    entries = []
    for anchor in soup.select("h4 a"):
        label = clean_text(anchor.get_text(" ", strip=True))
        if not label.startswith("Grammar Concepts #"):
            continue
        number = extract_number(label)
        if number in wanted:
            entries.append(parse_entry(label, anchor["href"]))
    entries.sort(key=lambda entry: entry.number)
    return entries


def write_bank_file(payload: dict[str, object], output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    number = int(payload["concept_number"])
    path = output_dir / f"concept-{number:02d}.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the local English Ladder grammar item bank.")
    parser.add_argument("--concept", type=int, nargs="*", help="Optional concept numbers to generate.")
    parser.add_argument("--model", default=MODEL, help="OpenAI model name to use.")
    parser.add_argument("--force", action="store_true", help="Regenerate bank files even if they already exist.")
    parser.add_argument("--target-override", type=int, help="Optional per-concept target for pilot generation.")
    parser.add_argument("--output-dir", help="Optional directory for generated bank files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entries = load_selected_entries(args.concept)
    output_dir = Path(args.output_dir).resolve() if args.output_dir else ITEM_BANK_DIR
    generated = []
    skipped = []
    failures: list[tuple[int, str]] = []

    for entry in entries:
        target_count = args.target_override or target_count_for_concept(entry.number)
        path = output_dir / f"concept-{entry.number:02d}.json"
        if path.exists() and not args.force:
            skipped.append(path)
            continue
        try:
            payload = request_concept_bank(entry, target_count, args.model)
        except Exception as exc:
            failures.append((entry.number, str(exc)))
            print(f"FAILED concept-{entry.number:02d}: {exc}", file=sys.stderr)
            continue
        generated.append(write_bank_file(payload, output_dir))
        print(f"Generated {generated[-1].name} ({target_count} items).")

    total = sum(target_count_for_concept(entry.number) for entry in entries)
    print(f"Selected concepts: {len(entries)}")
    print(f"Target total items for selection: {total}")
    print(f"Generated files: {len(generated)}")
    print(f"Skipped existing files: {len(skipped)}")
    print(f"Failed concepts: {len(failures)}")
    for number, message in failures:
        first_line = message.splitlines()[0]
        print(f"- concept-{number:02d}: {first_line}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
