from __future__ import annotations

import re
from typing import Any

from reportlab.lib.units import inch

from generate_efsp_culture_pdfs import CONTENT_WIDTH, box, h1, h2, h3, p, table


NOUN_DISTRACTORS = [
    "evidence threshold",
    "approval path",
    "operating constraint",
    "decision owner",
]
ADVERB_DISTRACTORS = ["separately", "prematurely", "informally", "conditionally"]
VERB_DISTRACTORS = ["verify", "qualify", "escalate", "document"]
KNOWN_TERMS = [
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
]

TERM_CARD_OVERRIDES = {
    "jurisdiction": (["establish jurisdiction", "challenge jurisdiction"], "Jurisdiction concerns a court's authority, not simply the location where a dispute is inconvenient.", "Before we assess the merits, counsel needs to establish which court has jurisdiction."),
    "referral": (["submit a referral", "schedule from a referral"], "A referral routes a patient or case; it is not the same as completed access to the next service.", "The team should track each referral from order to scheduled first appointment."),
    "eligibility": (["verify eligibility", "document eligibility"], "Eligibility determines whether a person or request qualifies; it does not guarantee capacity or authorization.", "Please verify eligibility before the patient is offered a limited appointment slot."),
    "authorization": (["obtain authorization", "confirm authorization status"], "Authorization is a required approval; it is not the same as eligibility or clinical appropriateness.", "We cannot assume payment until authorization status is confirmed with the payer."),
    "no-show": (["reduce no-shows", "track no-show rate"], "A no-show is a missed use of reserved capacity, not proof that a patient no longer needs care.", "The clinic is testing reminders and transport screening to reduce no-shows."),
    "clean claim": (["submit a clean claim", "improve clean-claim rate"], "A clean claim is ready for processing, not a guarantee that the payer will ultimately pay it.", "The coding lead checks that the claim is clean before it enters the payer workflow."),
    "denial": (["appeal a denial", "analyze denial trends"], "A denial is a payer or authority decision, not necessarily the final resolution of the claim.", "The revenue-cycle team is analyzing denial trends after the policy change."),
    "coding": (["validate coding", "correct coding"], "Coding translates services and conditions into standardized classifications; it is not a substitute for complete documentation.", "The analyst will validate coding against the clinical note and payer rule."),
    "sbar": (["use SBAR", "give an SBAR handoff"], "SBAR structures urgent clinical communication; it does not replace bedside assessment or escalation criteria.", "Use SBAR to give the resident the current situation, trend, assessment, and recommendation."),
    "vital signs": (["trend vital signs", "recheck vital signs"], "Vital signs are time-sensitive clinical measurements, not a complete explanation of a patient's condition.", "The nurse will recheck vital signs and call the rapid-response team if the trend worsens."),
    "wafer": (["inspect the wafer", "hold the wafer lot"], "A wafer is the substrate being processed; it is not interchangeable with a finished die or packaged device.", "Do not release the wafer lot until the metrology result and process route are confirmed."),
    "process window": (["tighten the process window", "operate within the process window"], "A process window is the safe operating range, not a single target setting.", "The team will not widen the process window until split-lot evidence supports the change."),
    "yield": (["improve yield", "analyze yield loss"], "Yield measures conforming output, not the root cause of a process change.", "The fab is analyzing yield loss by tool, layer, and time window."),
    "design intent": (["preserve design intent", "clarify design intent"], "Design intent describes the objective a solution must preserve; it is not identical to one drawing detail or material selection.", "Before revising the drawing, confirm whether the change preserves the approved design intent."),
    "rfi": (["issue an RFI", "answer an RFI"], "An RFI resolves ambiguity in project information; it does not itself authorize a scope or price change.", "The contractor should issue an RFI before proceeding with the conflicting detail."),
    "airworthiness": (["confirm airworthiness", "restore airworthiness"], "Airworthiness is an aircraft's approved and safe operating condition, not simply whether the aircraft can physically depart.", "Maintenance must confirm airworthiness before dispatch releases the aircraft."),
    "aml": (["perform AML screening", "escalate an AML alert"], "AML is a financial-crime control framework, not a conclusion that a customer has committed wrongdoing.", "The analyst will escalate the AML alert after reviewing the transaction pattern."),
    "kyc": (["complete KYC", "refresh KYC records"], "KYC verifies identity and risk information; it is not satisfied by a customer name alone.", "The onboarding team cannot activate the account until KYC checks are complete."),
    "attack surface": (["reduce attack surface", "map the attack surface"], "Attack surface is the set of possible entry points for compromise, not evidence that an attack has occurred.", "The security team is mapping the attack surface before exposing the new API."),
    "cve": (["triage the CVE", "patch the CVE"], "A CVE identifies a known vulnerability; its identifier alone does not show whether a particular system is exposed.", "First confirm whether the CVE affects the deployed version before scheduling the patch."),
    "cvss": (["review the CVSS score", "contextualize CVSS"], "CVSS expresses vulnerability severity, but it does not replace local exploitability and business-impact analysis.", "The team will contextualize the CVSS score with internet exposure and compensating controls."),
    "assay": (["validate the assay", "run the assay"], "An assay is a defined laboratory measurement method, not proof that a result will translate to clinical benefit.", "The team will validate the assay's precision before using it for a development decision."),
    "biomarker": (["validate the biomarker", "stratify by biomarker"], "A biomarker can indicate a biological state or response; it is not automatically a clinically useful endpoint.", "The protocol will stratify patients by biomarker status only after the assay is validated."),
    "510(k)": (["prepare a 510(k)", "identify a predicate device"], "A 510(k) is a regulatory submission pathway, not a general approval for any future device use.", "Regulatory will prepare the 510(k) around the intended use and predicate comparison."),
    "due diligence": (["conduct due diligence", "complete due diligence"], "Due diligence tests facts and risks before commitment; it is not a ceremonial step after the decision is made.", "The team will complete due diligence on data practices before onboarding the vendor."),
    "underwriting": (["complete underwriting", "price the underwriting risk"], "Underwriting evaluates risk and terms; it is not a promise that coverage, credit, or funding has been approved.", "The underwriter needs loss history and controls before pricing the account."),
}


def term_learning_fields(term: str, definition: str, context: str = "") -> dict[str, Any]:
    """Return compact, closed-study supports for a terminology card."""
    lower = term.casefold()
    override = TERM_CARD_OVERRIDES.get(lower)
    if override:
        collocations, contrast, example = override
    elif any(word in lower for word in ["rate", "ratio", "margin", "yield", "score", "variance", "runway", "kpi"]):
        collocations = [f"track {term}", f"explain a change in {term}"]
        contrast = f"{term} measures a result or condition; it does not, by itself, prove the cause."
        example = f"Before we act, let us track {term} by segment and explain what changed."
    elif any(word in lower for word in ["risk", "hazard", "threat", "exposure", "incident", "defect", "deviation"]):
        collocations = [f"assess {term}", f"mitigate {term}"]
        contrast = f"{term} identifies a possible or current exposure; it is not the same as accepting that exposure."
        example = f"We need to assess {term}, name the owner, and agree on the trigger for escalation."
    elif any(word in lower for word in ["policy", "standard", "protocol", "procedure", "requirement", "criteria"]):
        collocations = [f"apply the {term}", f"comply with the {term}"]
        contrast = f"{term} is an approved rule or threshold, not an informal preference."
        example = f"Please confirm which {term} applies before we commit the team."
    elif any(word in lower for word in ["report", "memo", "brief", "notice", "statement", "letter", "update"]):
        collocations = [f"prepare a {term}", f"circulate the {term}"]
        contrast = f"{term} is a reviewable communication artifact, not an undocumented verbal assurance."
        example = f"The {term} should state the evidence, caveat, decision owner, and next action."
    elif any(word in lower for word in ["plan", "strategy", "roadmap", "program", "playbook"]):
        collocations = [f"align on the {term}", f"revise the {term}"]
        contrast = f"{term} sets an intended course of action; it is not proof that the work is feasible or approved."
        example = f"Before we revise the {term}, we need to test the dependency and resource assumptions."
    elif any(word in lower for word in ["audit", "review", "assessment", "analysis", "inspection", "evaluation"]):
        collocations = [f"conduct a {term}", f"document the {term}"]
        contrast = f"{term} is a structured examination of evidence; it is not a conclusion reached before the evidence is checked."
        example = f"The team will conduct a {term} before it recommends a corrective action."
    else:
        collocations = [f"clarify {term}", f"document {term}"]
        contrast = f"{term} should be defined against the relevant evidence and decision boundary, rather than used as a vague label."
        example = f"Before we proceed, please clarify {term} and the evidence that supports it."
    return {
        "term": term,
        "definition": definition,
        "contrast": contrast,
        "collocations": collocations,
        "example": example,
        "context": context,
    }


def bounded_activity_instruction(activity: str) -> str:
    """Convert legacy free-response directions into a closed instructional objective."""
    clean = activity.strip()
    leading = re.match(r"^(?:write|draft|rewrite)(?:\s+and\s+discuss)?\s+(.+?)(?:\.)?$", clean, flags=re.IGNORECASE)
    if leading:
        outcome = leading.group(1).rstrip(".")
        return (
            "Guided communication selection: choose the evidence, caveat, audience, and next action "
            f"needed for {outcome[:1].lower() + outcome[1:]}"
        )
    clean = re.sub(r"\blearners\s+(?:write|draft|rewrite)\b", "learners select language for", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bwriting\b", "decision communication", clean, flags=re.IGNORECASE)
    return clean


def _unique(items: list[str]) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for item in items:
        clean = str(item).strip()
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


def _word_form(answer: str) -> str:
    clean = answer.casefold().strip()
    if clean.endswith("ly"):
        return "adverb"
    if clean in {"verify", "qualify", "escalate", "document", "confirm", "contain", "release", "defer"}:
        return "verb"
    return "noun"


def _fallbacks_for(answer: str) -> list[str]:
    form = _word_form(answer)
    if form == "adverb":
        return ADVERB_DISTRACTORS
    if form == "verb":
        return VERB_DISTRACTORS
    return NOUN_DISTRACTORS


def _target_from_line(line: str, preferred_terms: list[str]) -> str:
    for term in preferred_terms:
        if re.search(re.escape(term), line, flags=re.IGNORECASE):
            return term
    for phrase in KNOWN_TERMS:
        if re.search(rf"\b{re.escape(phrase)}\b", line, flags=re.IGNORECASE):
            return phrase
    words = re.findall(r"[A-Za-z][A-Za-z-]{5,}", line)
    return words[-1] if words else "evidence"


def _four_choices(answer: str, candidates: list[str], seed_text: str) -> tuple[list[str], int]:
    form = _word_form(answer)
    compatible = [item for item in candidates if _word_form(item) == form]
    options = _unique([answer] + compatible + _fallbacks_for(answer))
    selected = options[:]
    rotation = sum(ord(char) for char in seed_text) % len(selected)
    selected = selected[rotation:] + selected[:rotation]
    chosen = _unique([answer] + [item for item in selected if item.casefold() != answer.casefold()])[:4]
    for fallback in _fallbacks_for(answer):
        if len(chosen) == 4:
            break
        if fallback.casefold() != answer.casefold() and fallback.casefold() not in {item.casefold() for item in chosen}:
            chosen.append(fallback)
    rotation = sum(ord(char) for char in answer + seed_text) % 4
    chosen = chosen[rotation:] + chosen[:rotation]
    return chosen, chosen.index(answer)


def _activity(
    title: str,
    instruction: str,
    prompt: str,
    options: list[str],
    correct_index: int,
    explanation: str,
    option_feedback: list[str],
) -> dict[str, Any]:
    return {
        "title": title,
        "instruction": instruction,
        "prompt": prompt,
        "options": options,
        "correct_index": correct_index,
        "answer": options[correct_index],
        "explanation": explanation,
        "option_feedback": option_feedback,
    }


def _response_activity(answer: str, correct_line: str, setting: str) -> dict[str, Any]:
    options = [
        correct_line,
        f"I can approve the result now and look at {answer} after the decision.",
        f"Let's avoid naming {answer} until the discussion is over.",
        "I disagree, but I cannot identify the evidence or condition that would change the decision.",
    ]
    correct_index = 0
    options, correct_index = _four_choices(options[0], options[1:], setting + correct_line)
    feedback = []
    for option in options:
        if option == correct_line:
            feedback.append("This response protects the decision while still moving the conversation forward.")
        elif "approve" in option:
            feedback.append("This overpromises before the relevant evidence has been checked.")
        elif "avoid" in option:
            feedback.append("Avoiding the key term makes the risk harder for the team to evaluate.")
        else:
            feedback.append("This names disagreement without giving the group a usable evidence standard or next step.")
    return _activity(
        "2. Choose the strongest professional response",
        "Choose the response that acknowledges pressure, names the real boundary, and keeps the decision moving.",
        f"In this situation ({setting}), a stakeholder asks for an immediate answer. Which response is the strongest?",
        options,
        correct_index,
        "The strongest response is specific about what must be checked and avoids either false certainty or vague resistance.",
        feedback,
    )


def _decision_activity(answer: str, setting: str) -> dict[str, Any]:
    correct = f"Verify {answer}, name the decision owner, and state the evidence that would change the recommendation."
    options = [
        correct,
        "Treat urgency as sufficient evidence and commit before the review is complete.",
        "Escalate the issue without first naming the decision, evidence gap, or accountable owner.",
        "Use broader jargon instead of making the risk and next action clear.",
    ]
    correct_index = 0
    options, correct_index = _four_choices(correct, options[1:], setting + answer)
    feedback = []
    for option in options:
        if option == correct:
            feedback.append("This creates a bounded decision: a fact to verify, an accountable person, and a clear condition for action.")
        elif option.startswith("Treat urgency"):
            feedback.append("Urgency can set timing, but it does not replace the evidence needed for a responsible decision.")
        elif option.startswith("Escalate"):
            feedback.append("Escalation is more useful when the receiving leader can see the decision, evidence gap, and owner immediately.")
        else:
            feedback.append("Extra jargon does not substitute for an explicit risk, evidence source, and next action.")
    return _activity(
        "3. Select the next decision move",
        "Choose the next move that keeps the work controlled without creating unnecessary delay.",
        f"After this situation ({setting}), what should the learner do next?",
        options,
        correct_index,
        "A practical next move connects a named fact to an owner and a condition for proceeding, revising, or escalating.",
        feedback,
    )


def _with_activities(base: dict[str, Any], activities: list[dict[str, Any]]) -> dict[str, Any]:
    first = activities[0]
    return {
        **base,
        "activities": activities,
        "prompt": first["prompt"],
        "options": first["options"],
        "correct_index": first["correct_index"],
        "answer": first["answer"],
        "explanation": first["explanation"],
        "option_feedback": first["option_feedback"],
    }


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
    term_feedback = [
        "This is the precise term already used in the professional response. It fits both the grammar and the technical meaning."
        if option == answer
        else "This choice may be relevant to the broader discussion, but it does not fit this exact grammatical and technical slot."
        for option in options
    ]
    activities = [
        _activity(
            "1. Complete the field language",
            "Use the dialogue and the surrounding evidence to choose the precise term.",
            blank_line,
            options,
            correct_index,
            f"'{answer}' is the precise language in this response. The other options are plausible workplace terms, but they do not fit this sentence's meaning and form.",
            term_feedback,
        ),
        _response_activity(answer, line, str(dialogue.get("setting", ""))),
        _decision_activity(answer, str(dialogue.get("setting", ""))),
    ]
    return _with_activities(
        {
            "title": dialogue.get("title", "Guided dialogue completion"),
            "setting": dialogue.get("setting", ""),
            "turns": blanked_turns,
        },
        activities,
    )


def make_module_cloze(module: dict[str, Any], all_outputs: list[str]) -> dict[str, Any]:
    terms = _unique(module.get("terms", []))
    first_term = terms[0] if terms else "evidence standard"
    second_term = terms[1] if len(terms) > 1 else "operating constraint"
    output = module.get("output", (module.get("outputs") or ["decision brief"])[0])
    pressure = module.get("pressure", "We need to move faster.")
    constraint = module.get("constraint", "The evidence and operating conditions need review.")
    first_options, first_index = _four_choices(first_term, terms[1:], module.get("title", "module"))
    prompt = f"Before we act, I need to confirm the ________ and how it affects {second_term}."
    turns = [
        ("Stakeholder", pressure),
        ("ESL learner", prompt),
        ("Stakeholder", "What would let us move forward responsibly?"),
        ("ESL learner", f"I will test the constraint with the decision owner and return with a {output}."),
    ]
    term_feedback = [
        "This is the decision variable the learner must confirm before the team acts."
        if option == first_term
        else f"'{option}' is relevant vocabulary, but it is not the primary decision variable in this exchange."
        for option in first_options
    ]
    correct_response = (
        f"I understand the urgency. I need to verify {first_term} and {second_term} against the stated constraint before I recommend the next step."
    )
    response_options, response_index = _four_choices(
        correct_response,
        [
            f"We should act now and resolve {first_term} after the result is visible.",
            f"A {output} is unnecessary; verbal assurance should be enough.",
            "I disagree, but I cannot name the boundary or the decision the group needs to make.",
        ],
        module.get("scenario", ""),
    )
    response_feedback = []
    for option in response_options:
        if option == correct_response:
            response_feedback.append("This response is specific, respectful, and appropriately conditional. It converts pressure into a controlled decision.")
        elif option.startswith("We should act"):
            response_feedback.append("This postpones the key decision variable until after action, when the cost of correction may be higher.")
        elif "verbal assurance" in option:
            response_feedback.append("A high-stakes decision needs a shared, reviewable record rather than unsupported reassurance.")
        else:
            response_feedback.append("Professional pushback should identify the missing evidence and the exact decision, not merely express disagreement.")
    correct_decision = (
        f"Review the stated constraint with the accountable owner, then prepare the {output} with the evidence, tradeoff, and requested decision."
    )
    decision_options, decision_index = _four_choices(
        correct_decision,
        [
            "Accept the request immediately because the stakeholder has already expressed urgency.",
            "Send every available detail to senior leaders without identifying the decision they need to make.",
            "Wait for the problem to become visible before assigning an owner or evidence source.",
        ],
        output + module.get("title", ""),
    )
    decision_feedback = []
    for option in decision_options:
        if option == correct_decision:
            decision_feedback.append("This sequence creates a concise, decision-ready artifact with a clear owner and evidence boundary.")
        elif option.startswith("Accept"):
            decision_feedback.append("Stakeholder urgency is important, but it does not remove the need to check the stated constraint.")
        elif option.startswith("Send every"):
            decision_feedback.append("More information is not automatically more useful. Leaders need a clear decision, tradeoff, and recommendation.")
        else:
            decision_feedback.append("Waiting for visible harm is reactive. Good professional language names the owner and evidence condition early.")
    activities = [
        _activity(
            "1. Complete the field language",
            "Choose the term that belongs in this decision point.",
            prompt,
            first_options,
            first_index,
            f"'{first_term}' is the field-specific variable that must be checked before the team can proceed responsibly.",
            term_feedback,
        ),
        _activity(
            "2. Choose the strongest professional response",
            "Select the response that preserves the relationship while setting an evidence-based boundary.",
            f"A stakeholder says, '{pressure}' Which response gives a useful, professional form of pushback?",
            response_options,
            response_index,
            "The strongest response names the field terms, the constraint, and the condition for a recommendation without sounding defensive or passive.",
            response_feedback,
        ),
        _activity(
            "3. Select the next decision move",
            "Choose the action that turns the discussion into a controlled workplace decision.",
            f"Given this situation - {module.get('scenario', '')} - what should happen next?",
            decision_options,
            decision_index,
            "The best next move makes the evidence, tradeoff, owner, and requested decision visible in a concise workplace artifact.",
            decision_feedback,
        ),
    ]
    return _with_activities(
        {
            "title": module.get("title", "Guided dialogue completion"),
            "setting": module.get("scenario", module.get("focus", "")),
            "turns": turns,
        },
        activities,
    )


def add_cloze_exercise(story: list, cloze: dict[str, Any], answer_key: list[dict[str, str]], show_context: bool = True) -> None:
    story.append(h3("Three-step decision practice"))
    if show_context and cloze.get("setting"):
        story.append(box("Situation", [cloze["setting"]], "blue"))
    if show_context and cloze.get("turns"):
        rows = [["Speaker", "Line"]]
        rows.extend([[speaker, line] for speaker, line in cloze["turns"]])
        story.append(table(rows, [1.45 * inch, CONTENT_WIDTH - 1.45 * inch]))
    activities = cloze.get("activities") or [
        {
            "title": "Complete the field language",
            "instruction": "Choose the strongest answer.",
            "prompt": cloze["prompt"],
            "options": cloze["options"],
            "correct_index": cloze["correct_index"],
            "answer": cloze["answer"],
            "explanation": cloze["explanation"],
            "option_feedback": [],
        }
    ]
    for activity in activities:
        story.append(h3(activity["title"]))
        story.append(p(activity["instruction"]))
        story.append(p(activity["prompt"]))
        rows = [["Option", "Phrase"]]
        rows.extend([[chr(65 + index), option] for index, option in enumerate(activity["options"])])
        story.append(table(rows, [0.75 * inch, CONTENT_WIDTH - 0.75 * inch]))
        feedback = activity.get("option_feedback", [])
        correct_feedback = feedback[activity["correct_index"]] if len(feedback) > activity["correct_index"] else ""
        answer_key.append(
            {
                "title": f"{cloze['title']} - {activity['title']}",
                "answer": f"{chr(65 + activity['correct_index'])}. {activity['answer']}",
                "explanation": f"{activity['explanation']} {correct_feedback}".strip(),
            }
        )


def add_answer_key(story: list, answer_key: list[dict[str, str]]) -> None:
    if not answer_key:
        return
    story += h1("Answer Key and Rationale")
    story.append(p("Check each stage after completing the practice sequence. The rationale explains the decision skill the strongest response demonstrates."))
    for entry in answer_key:
        story.append(h2(entry["title"]))
        story.append(table([["Correct answer", "Why it fits"], [entry["answer"], entry["explanation"]]], [2.25 * inch, CONTENT_WIDTH - 2.25 * inch]))
