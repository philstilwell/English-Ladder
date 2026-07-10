from __future__ import annotations

import re
from typing import Any

from reportlab.lib.units import inch

from generate_efsp_culture_pdfs import CONTENT_WIDTH, box, h1, h2, h3, p, table


FALLBACK_CHOICES = [
    "evidence",
    "risk",
    "owner",
    "scope",
    "timeline",
    "assumption",
    "mitigation",
    "approval",
    "control",
    "disclosure",
]


def _unique(items: list[str]) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for item in items:
        clean = item.strip()
        key = clean.casefold()
        if clean and key not in seen:
            output.append(clean)
            seen.add(key)
    return output


def _note_terms(notes: list[str]) -> list[str]:
    terms: list[str] = []
    for note in notes:
        match = re.match(r"^([A-Za-z0-9][A-Za-z0-9 /-]{1,42}?)\s+(?:means|is|are)\b", note)
        if match:
            terms.append(match.group(1).strip())
    return _unique(terms)


def _target_from_line(line: str, preferred_terms: list[str]) -> str:
    for term in preferred_terms:
        if re.search(re.escape(term), line, flags=re.IGNORECASE):
            return term
    for phrase in [
        "evidence",
        "risk",
        "owner",
        "scope",
        "timeline",
        "assumption",
        "mitigation",
        "approval",
        "control",
        "release",
        "recommend",
        "confirm",
        "qualify",
        "containment",
        "retrieval",
        "latency",
        "evaluation",
    ]:
        if re.search(rf"\b{re.escape(phrase)}\b", line, flags=re.IGNORECASE):
            return phrase
    words = re.findall(r"[A-Za-z][A-Za-z-]{5,}", line)
    return words[-1] if words else "evidence"


def _four_choices(answer: str, candidates: list[str], seed_text: str) -> tuple[list[str], int]:
    options = _unique([answer] + candidates + FALLBACK_CHOICES)
    selected = options[:]
    rotation = sum(ord(char) for char in seed_text) % len(selected)
    selected = selected[rotation:] + selected[:rotation]
    chosen = _unique([answer] + [item for item in selected if item.casefold() != answer.casefold()])[:4]
    while len(chosen) < 4:
        chosen.append(FALLBACK_CHOICES[len(chosen)])
    rotation = sum(ord(char) for char in answer + seed_text) % 4
    chosen = chosen[rotation:] + chosen[:rotation]
    return chosen, chosen.index(answer)


def make_dialogue_cloze(dialogue: dict[str, Any], preferred_terms: list[str] | None = None) -> dict[str, Any]:
    turns = list(dialogue.get("dialogue", dialogue.get("turns", [])))
    learner_turns = [turn for turn in turns if str(turn[0]).casefold() == "esl learner"]
    speaker, line = learner_turns[-1] if learner_turns else turns[-1]
    terms = _unique((preferred_terms or []) + _note_terms(dialogue.get("notes", dialogue.get("coach_notes", []))))
    answer = _target_from_line(line, terms)
    options, correct_index = _four_choices(answer, terms, str(dialogue.get("title", "dialogue")))
    blank_line = re.sub(re.escape(answer), "________", line, count=1, flags=re.IGNORECASE)
    blanked_turns = [
        (turn_speaker, blank_line if turn_speaker == speaker and turn_line == line else turn_line)
        for turn_speaker, turn_line in turns
    ]
    return {
        "title": dialogue.get("title", "Guided dialogue completion"),
        "setting": dialogue.get("setting", ""),
        "turns": blanked_turns,
        "prompt": blank_line,
        "options": options,
        "correct_index": correct_index,
        "answer": answer,
        "explanation": f"'{answer}' is the precise phrase used in this professional response. The other choices do not fit the dialogue's meaning or grammar.",
    }


def make_module_cloze(module: dict[str, Any], all_outputs: list[str]) -> dict[str, Any]:
    terms = module.get("terms", [])
    first_term = terms[0] if terms else "the relevant evidence"
    second_term = terms[1] if len(terms) > 1 else "the operating constraint"
    answer = module.get("output", (module.get("outputs") or ["decision record"])[0])
    options, correct_index = _four_choices(answer, all_outputs, module.get("title", "module"))
    pressure = module.get("pressure", "We need to move faster.")
    turns = [
        ("Stakeholder", pressure),
        ("ESL learner", f"I understand the urgency. Before we commit, I need to confirm {first_term}, {second_term}, the owner, and the evidence standard."),
        ("Stakeholder", "What would let us move forward responsibly?"),
        ("ESL learner", "Let's document the risk and prepare a ________ with facts, caveats, owner, and next step."),
    ]
    return {
        "title": module.get("title", "Guided dialogue completion"),
        "setting": module.get("scenario", module.get("focus", "")),
        "turns": turns,
        "prompt": turns[-1][1],
        "options": options,
        "correct_index": correct_index,
        "answer": answer,
        "explanation": f"A {answer} is the bounded workplace output that captures the evidence, owner, and next action for this situation.",
    }


def add_cloze_exercise(story: list, cloze: dict[str, Any], answer_key: list[dict[str, str]], show_context: bool = True) -> None:
    story.append(h3("Guided dialogue completion"))
    if show_context and cloze.get("setting"):
        story.append(box("Situation", [cloze["setting"]], "blue"))
    if show_context and cloze.get("turns"):
        rows = [["Speaker", "Line"]]
        rows.extend([[speaker, line] for speaker, line in cloze["turns"]])
        story.append(table(rows, [1.45 * inch, CONTENT_WIDTH - 1.45 * inch]))
    else:
        story.append(p(cloze["prompt"]))
    story.append(h3("Choose the missing language"))
    rows = [["Option", "Phrase"]]
    rows.extend([[chr(65 + index), option] for index, option in enumerate(cloze["options"])])
    story.append(table(rows, [0.75 * inch, CONTENT_WIDTH - 0.75 * inch]))
    answer_key.append(
        {
            "title": cloze["title"],
            "answer": f"{chr(65 + cloze['correct_index'])}. {cloze['answer']}",
            "explanation": cloze["explanation"],
        }
    )


def add_answer_key(story: list, answer_key: list[dict[str, str]]) -> None:
    if not answer_key:
        return
    story += h1("Answer Key and Rationale")
    story.append(p("Check each answer after completing the dialogue. The rationale shows why the correct phrase is the strongest fit for the real workplace situation."))
    for entry in answer_key:
        story.append(h2(entry["title"]))
        story.append(table([["Correct answer", "Why it fits"], [entry["answer"], entry["explanation"]]], [2.25 * inch, CONTENT_WIDTH - 2.25 * inch]))
