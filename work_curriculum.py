"""Canonical, offline curriculum shared by all English for Work pages and PDFs.

Cases are authored per lesson, not produced by substituting industry nouns into
one response. Repeated language workshops are deliberate retrieval practice.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content" / "work"
REVISION = "2026-09-06"


def workshop(title, goal, explanation, frames, before, after, reason, questions, role_b, challenge):
    return dict(title=title, goal=goal, explanation=explanation, frames=frames,
                before=before, after=after, reason=reason, questions=questions,
                role_b=role_b, challenge=challenge)


def question(prompt, correct, alternatives, why, feedback):
    return dict(prompt=prompt, options=[correct, *alternatives], correct_index=0,
                feedback=[why, *feedback])


WORKSHOPS = {
    "clarify": workshop("Ask a precise question", "Clarify missing information before responding.",
        "Name the exact word, fact, or requirement you need clarified. Ask one focused question at a time. Repeat your understanding and give the other person a chance to correct it.",
        ["When you say ..., do you mean ...?", "Could you clarify which ...?", "So, my understanding is ... . Is that right?"],
        "Could you explain what does this mean?", "Could you explain what this means?",
        "After an introductory phrase such as 'Could you explain', the embedded question uses statement word order: what this means.",
        [question("Which indirect question has the usual word order?", "Could you confirm when the review starts?",
                  ["Could you confirm when does the review start?", "Could you confirm when starts the review?"],
                  "The embedded question uses subject then verb: the review starts.",
                  ["Remove 'does' and use statement word order after 'confirm'.", "Place the subject 'the review' before 'starts'."]),
         question("Someone says the report is 'ready.' Which question best clarifies its approval status?", "Has the report been approved, or is it ready for review?",
                  ["Can you send the report to me this afternoon?", "Who will present the report at the meeting?"],
                  "This question distinguishes two meanings of 'ready' that affect the next action.",
                  ["This asks about delivery timing, not whether approval has happened.", "This asks about the presenter, not the report's approval status."])],
        "You need to know exactly what information is missing. Give one answer only after your partner asks a focused question; then ask them to confirm their understanding.",
        "The other person uses an ambiguous word such as 'ready', 'approved', or 'urgent'. Clarify it before continuing."),
    "explain": workshop("Make a complex point clear", "Explain a useful distinction in plain English.",
        "Start with the reader's question. Explain one unfamiliar term with familiar words, then give a relevant example or contrast. Check understanding without asking only 'Do you understand?'.",
        ["In this context, ... means ... .", "The difference is that ... .", "How would you explain that distinction to a colleague?"],
        "We need to operationalize the implementation.", "We need to put the plan into practice.",
        "The revised sentence names the action in familiar words. Specialist vocabulary is useful when it adds precision, but repeating abstract nouns can hide the meaning.",
        [question("Which sentence explains 'backlog' rather than repeating it?", "The backlog is the work still waiting to be completed.",
                  ["The backlog is the work completed during the last period.", "The backlog is the maximum work the team can finish in a period."],
                  "This gives the meaning in familiar words.",
                  ["Completed work is different from work still waiting.", "This describes capacity, not the work waiting to be completed."]),
         question("Which follow-up best checks whether your explanation was clear?", "How would you describe the next step in your own words?",
                  ["Would you like me to repeat the explanation?", "Was the explanation detailed enough for you?"],
                  "An open request lets the listener show their understanding.",
                  ["Offering repetition may help, but it does not show how the listener understood the next step.", "This invites an opinion on detail, not a demonstration of understanding."])],
        "You are unfamiliar with one technical term in the case. Ask for a plain-English explanation and then paraphrase it. Do not pretend to understand a term you cannot explain.",
        "Your listener is new to this field. Replace two specialist expressions with clear explanations without changing the meaning."),
    "qualify": workshop("Match certainty to evidence", "Separate observations, assumptions, and conclusions.",
        "Say what the evidence shows, identify what is still unknown, and limit the conclusion to that evidence. Words such as 'may', 'suggests', and 'in this sample' are useful when the uncertainty is real. Do not soften an urgent, verified safety concern.",
        ["The available evidence shows ... .", "This may indicate ..., but ... .", "We have not yet established whether ... ."],
        "The pilot proves this will work everywhere.", "The pilot worked in the tested setting; performance elsewhere remains untested.",
        "The revision states the finding and its scope. It avoids turning limited evidence into a universal claim.",
        [question("Which sentence preserves uncertainty about an unconfirmed cause?", "The change may have contributed to the delay.",
                  ["The change must have caused the delay.", "The change definitely caused the delay."],
                  "'May have contributed' presents a possibility without claiming the cause is established.",
                  ["'Must have' expresses a strong inference that the evidence may not support.", "'Definitely' presents the cause as certain."]),
         question("A result comes from a small pilot in one location. Which phrase accurately limits the claim?", "In this pilot, the observed result was ...",
                  ["In similar locations, we can now expect the same result ...", "Across the service, the observed result was ..."],
                  "This locates the finding in the setting actually studied.",
                  ["Similarity alone does not establish that the result will transfer.", "A pilot in one location does not establish a service-wide observation."])],
        "You need to tell a colleague what is known. Ask which part is confirmed and which part is an assumption. Challenge one statement that sounds more certain than the case supports.",
        "Someone asks for a yes-or-no answer when the evidence supports only a qualified answer. Be concise while preserving the uncertainty."),
    "compare": workshop("Explain a fair comparison", "Compare options using the same criteria and state the tradeoff.",
        "Use the same time period, scope, and measurement basis for both options. Explain a difference with 'whereas' or 'while'. State what improves and what is given up; do not hide the weaker side of a recommendation.",
        ["Both options ..., but ... .", "Option A ..., whereas option B ... .", "The comparison depends on ... ."],
        "This option is more better.", "This option is better on cost, but slower to deliver.",
        "'Better' already has comparative meaning, so it does not need 'more'. Naming the criterion and tradeoff makes the comparison useful.",
        [question("Which sentence expresses a clear contrast?", "Option A is faster, whereas option B costs less.",
                  ["Option A is faster because option B costs less.", "Option A is faster, so option B costs less."],
                  "'Whereas' marks a contrast between two options.",
                  ["'Because' claims a causal connection that is not given.", "'So' implies one fact causes the other."]),
         question("A rate increases from 6% to 7%. What is the absolute difference?", "An increase of one percentage point.",
                  ["An increase of one percent relative to the original rate.", "An increase of seven percentage points."],
                  "Subtracting 6% from 7% gives one percentage point. The relative increase is about 16.7%.",
                  ["A one-percent relative increase on 6% would be 6.06%, not 7%.", "The new rate is 7%; the difference between the rates is one percentage point."])],
        "You favor one option but have not checked whether the scope is comparable. Ask about one difference, then explain the tradeoff you are willing to accept.",
        "Your listener focuses only on the lowest price or fastest date. Explain one other relevant comparison criterion."),
    "update": workshop("Give a useful status update", "Distinguish completed work from pending work and explain its impact.",
        "Lead with the current state, then the important change or open item. Use completed-action language only for completed work. Add a next update point when it is known; do not invent a date to make the message sound complete.",
        ["We have completed ...; ... remains open.", "As of ..., the status is ... .", "The next update will cover ... ."],
        "Everything is progressing well.", "Three checks are complete; two remain open and are being reviewed.",
        "The revision gives observable progress. A positive label alone does not tell the reader what is complete or still needed.",
        [question("Which sentence says a review is finished?", "The team has completed the review.",
                  ["The team is completing the review.", "The team plans to complete the review."],
                  "'Has completed' states that the action is finished.",
                  ["'Is completing' presents the work as in progress.", "'Plans to complete' describes an intention, not completion."]),
         question("Which update distinguishes a plan from a confirmed fact?", "Delivery is planned for Friday; the carrier has not confirmed it.",
                  ["Delivery is confirmed for Friday because we planned it.", "The delivery plan proves that arrival will be Friday."],
                  "This explicitly labels the date as planned and identifies the missing confirmation.",
                  ["A plan does not establish carrier confirmation.", "A plan cannot prove a future arrival time."])],
        "You need to brief someone who has only one minute. Ask what is complete, what is open, and which open item affects the next action.",
        "The listener asks you to reduce the update to two sentences. Preserve the most important completed and pending items."),
    "request": workshop("Ask for an actionable next step", "Make a request with a clear action, purpose, and realistic timing.",
        "State the action and the information needed. Explain why it matters and specify a deadline only when one is given or agreed. 'Could you' is polite; repeated apologies can obscure a legitimate request. Urgent situations may require a direct request.",
        ["Could you provide ... so that ...?", "Please confirm ... by [agreed time].", "If that timing is not possible, please let me know ... ."],
        "Please revert soonest with the necessary.", "Could you send the missing document and confirm when it will be available?",
        "The revision names the document and requested response. It avoids expressions that may be unfamiliar or ambiguous for an international audience.",
        [question("What does 'Please send it by Thursday' normally mean?", "Send it no later than Thursday.",
                  ["Send it on Thursday, but not earlier.", "Keep sending it regularly until Thursday."],
                  "'By' sets the latest point, while 'after' refers to a later time.",
                  ["By Thursday permits earlier delivery; it is not restricted to that day.", "This interprets a deadline as a continuing activity, which would use until."]),
         question("Which request gives the recipient enough detail to act?", "Could you confirm the document version needed for the review?",
                  ["Could you confirm that the review is important?", "Could you confirm that you received my earlier message?"],
                  "The requested action and information are explicit.",
                  ["This checks importance rather than identifying the needed document version.", "This checks receipt, not which version is required for the review."])],
        "You can help but need a clear request and its purpose. Ask what is required and whether the timing is fixed or negotiable.",
        "The other person cannot meet the requested timing. Clarify an alternative without inventing authority to change a formal deadline."),
    "negotiate": workshop("Offer a workable tradeoff", "Negotiate scope or timing while making conditions explicit.",
        "Acknowledge the goal and explain the available choices. Connect an offer to its actual conditions. A useful response makes room for discussion without promising approval or resources you do not control.",
        ["We can ..., provided that ... .", "Would you prefer ... or ...?", "I can take that proposal for review; I cannot yet confirm ... ."],
        "If you will approve the scope, we can assess the schedule.", "If you approve the scope, we can assess the schedule.",
        "For an ordinary future condition, the if-clause uses present tense. The other clause can express the future consequence or possibility.",
        [question("Which sentence presents a normal future condition clearly?", "If the scope changes, we will review the schedule.",
                  ["If the scope will change, we will review the schedule.", "If the scope changes, we reviewed the schedule."],
                  "The if-clause uses present tense; the main clause states the future response.",
                  ["For this ordinary future condition, use present simple in the if-clause.", "Reviewed places the response in the past instead of expressing the future response."]),
         question("Which response negotiates a new request without silently promising extra work?", "We can assess the addition and explain its effect on the agreed scope.",
                  ["We have included it, although its scope has not been reviewed.", "We guarantee the original date without assessing the addition."],
                  "This offers a useful next step while keeping the approval and scope question open.",
                  ["It treats unreviewed work as already included.", "It promises an outcome without examining the consequences."])],
        "You want the preferred outcome but can accept one tradeoff. Ask for two options, then state which condition you can accept and which still needs approval.",
        "The preferred option is unavailable. Offer an alternative and clearly state any approval still needed."),
    "handoff": workshop("Transfer information and responsibility", "Give a handoff that the receiving person can confirm.",
        "State the current situation, relevant background, open task, and receiving role. Ask for acknowledgment or repeat-back of the critical item. Sending a message and transferring responsibility are not always the same thing.",
        ["The current status is ...; the outstanding item is ... .", "The record shows ... .", "Please confirm who has accepted ... ."],
        "Someone should follow up on this.", "Please confirm which team has accepted the follow-up task.",
        "The revised sentence asks for an identifiable receiving team instead of leaving responsibility with an unspecified 'someone'.",
        [question("Which sentence checks that responsibility has been accepted?", "Please confirm who will complete the outstanding check.",
                  ["I mentioned the check in my earlier email.", "The check appears somewhere in the notes."],
                  "It asks for an identifiable person or team responsible for the task.",
                  ["Mentioning a task does not show that anyone accepted it.", "A written record alone does not identify who will act."]),
         question("Which response best checks a critical handoff detail?", "So the result is pending and your team will follow up; is that correct?",
                  ["I assume all results are final, so we can finish.", "I saw the message, so no clarification is needed."],
                  "This repeats the status and responsibility and invites correction.",
                  ["It changes pending information into a final result.", "Receiving a message is not the same as confirming its meaning."])],
        "You are taking over the work. Ask what remains open and repeat back the critical status or responsibility. Point out one detail that would be unsafe or misleading to assume.",
        "The intended recipient cannot take ownership. Keep the status clear and identify the need for an authorized reassignment."),
    "repair": workshop("Repair a misunderstanding", "Acknowledge a communication problem and give a corrected message.",
        "Name what was unclear or wrong, acknowledge its effect, and correct it. A brief apology can help, followed by a practical next step. Avoid explaining away the other person's reaction or promising an outcome you cannot control.",
        ["My earlier message did not make ... clear.", "I'm sorry for ... . The correct information is ... .", "Let me check that the revised explanation addresses ... ."],
        "I'm sorry if you failed to understand.", "I'm sorry my message did not explain the timing clearly.",
        "The revision takes responsibility for the message without blaming the listener. It identifies what needs to be corrected.",
        [question("Which apology takes responsibility for unclear wording?", "I'm sorry my earlier wording was unclear.",
                  ["I'm sorry the process took longer than expected.", "I'm sorry we could not meet the original date."],
                  "This acknowledges the speaker's contribution to the problem.",
                  ["This acknowledges duration, but does not take responsibility for the unclear wording.", "This acknowledges a missed date, not the communication problem in the question."]),
         question("What should follow an apology for an incorrect date?", "The corrected date and the current confirmation status.",
                  ["A longer explanation that never states the correct date.", "A new guaranteed date even if it is unverified."],
                  "A repair needs usable corrected information, including any uncertainty.",
                  ["The reader still lacks the information they need.", "An unsupported new promise can create a second misunderstanding."])],
        "You are frustrated because an earlier message created an expectation. Explain that expectation. Ask your partner to distinguish the correction from anything still uncertain.",
        "The listener remains disappointed after the correction. Acknowledge the impact and restate the available next step calmly."),
    "facilitate": workshop("Help a group reach a clear next step", "Include relevant voices and clarify the decision process.",
        "Summarize the issue neutrally, invite missing perspectives, and distinguish discussion from decision. State who can decide and record any unresolved question. Do not assume silence means agreement.",
        ["Let's hear ... before we decide.", "The point we still need to resolve is ... .", "Who will make this decision, and what do they need?"],
        "Nobody objected, so everyone agrees.", "Before I record agreement, does anyone have a concern or need more time?",
        "The revised question gives people a way to raise a concern. Silence can have several meanings, especially in unfamiliar or unequal-power situations.",
        [question("Which phrase invites a missing perspective?", "We haven't heard from the remote team yet; what is your view?",
                  ["The remote team has been quiet, so they must agree.", "We can record their agreement without asking them."],
                  "It invites participation without interpreting silence as consent.",
                  ["Silence does not establish agreement.", "Recording agreement without checking may misrepresent the team's view."]),
         question("Which closing statement records an unresolved decision accurately?", "Approval is pending; the sponsor will review the two options.",
                  ["We discussed the options, so approval is complete.", "Everyone spoke, so the decision must be final."],
                  "This distinguishes discussion from approval and identifies the next reviewer.",
                  ["Discussion does not itself constitute approval.", "Participation alone does not establish a decision."])],
        "You hold a relevant concern that has not been discussed. Raise it when invited and ask who will decide. Help the facilitator state one unresolved question accurately.",
        "A participant interrupts or the meeting is running out of time. Protect a turn to speak and close with an accurate decision record."),
    "feedback": workshop("Give feedback people can use", "Describe observed behavior, its effect, and a useful next step.",
        "Use a specific example instead of a personality label. Explain its effect, invite the person's perspective, and agree on a practical improvement. Focus on communication that can be changed, not accent or national identity.",
        ["In [specific situation], I noticed ... .", "The effect was ... . What was happening from your perspective?", "Could we agree to ... and review it ...?"],
        "You are always careless.", "The last two reports omitted the agreed summary section.",
        "The revision identifies observable work. 'Always' and a personality judgment make the feedback harder to verify or act on.",
        [question("Which feedback begins with observable behavior?", "The last two updates omitted the agreed completion date.",
                  ["The last two updates seemed less professional than usual.", "I think the team needs to be more committed to the updates."],
                  "The recipient can check the specific examples and discuss how to improve them.",
                  ["Less professional is an evaluation; it does not identify a specific observable omission.", "Commitment is an interpretation, not a description of what the updates contained."]),
         question("Which follow-up invites useful information before agreeing on support?", "What is making this part of the task difficult?",
                  ["Can you promise this will never happen again?", "Would another reminder solve this problem?"],
                  "An open question may reveal a barrier the speaker has not considered.",
                  ["A promise does not reveal the obstacle or what support would help.", "This proposes a solution before finding out what is making the task difficult."])],
        "You can explain a practical obstacle affecting the work. Share it after your partner asks for your perspective, then agree on one observable change.",
        "The recipient disagrees with your interpretation. Return to the observed example, listen, and revise an unsupported assumption."),
    "pushback": workshop("Disagree with a useful reason", "State a concern respectfully and propose a practical route forward.",
        "Acknowledge the goal without pretending agreement. Name the specific problem and its implication, then ask a focused question or propose a next step. Be direct when a safety or ethical boundary requires it.",
        ["I understand the goal. My concern is ... .", "That statement goes beyond ... .", "Could we ... before confirming ...?"],
        "That idea is ridiculous.", "My concern is that the proposal assumes capacity we have not confirmed.",
        "The revised sentence identifies a testable concern about the proposal. It leaves room for a constructive response.",
        [question("Which response identifies a specific assumption and evidence against it?", "The proposal assumes the review is complete; the record shows it is still open.",
                  ["The proposal appears optimistic, and I would prefer a slower approach.", "I would like another discussion before we proceed with the proposal."],
                  "It connects the concern to a specific assumption and record.",
                  ["This expresses a preference, but does not identify the assumption or the record that contradicts it.", "This requests discussion without stating the specific assumption or evidence."]),
         question("Which follow-up makes disagreement actionable?", "Could we resolve the missing approval before confirming the plan?",
                  ["Could we confirm the plan and discuss the missing approval later?", "Could we ask for general feedback before sending the next update?"],
                  "It names the unresolved condition and a practical next step.",
                  ["This confirms the plan before resolving the stated approval condition.", "General feedback does not directly address the missing approval."])],
        "You want to move quickly and initially overlook a relevant condition. Ask why it matters, then consider a practical route forward that respects the real constraint.",
        "The other person repeats the request more firmly. Restate the specific concern calmly and explain the appropriate next route."),
}

RUBRIC = [
    ("Meaning and accuracy", "Keeps the case facts accurate; clearly separates confirmed and unknown information."),
    ("Clarity and language", "Uses understandable sentences and explains specialist terms when the listener needs it."),
    ("Interaction and tone", "Responds to the other person's question, checks understanding, and uses an appropriate tone."),
    ("Task completion", "Makes the requested action or unresolved question clear without inventing authority or facts."),
]
SCORE_DESCRIPTORS = [(0, "Not yet", "The reader or listener cannot yet recover the intended meaning or action."),
                     (1, "With support", "The message works after a prompt, clarification, or revision."),
                     (2, "Independently", "The message is clear and accurate without a prompt.")]

SOURCES = {
    "plain": ("Digital.gov: plain-language guidance", "https://digital.gov/guides/plain-language"),
    "cefr": ("Council of Europe: CEFR descriptors", "https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors"),
    "sbar": ("AHRQ: SBAR communication tool", "https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/sbar.html"),
    "hipaa": ("HHS: HIPAA business associates", "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html"),
    "device": ("FDA: De Novo classification", "https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request"),
    "mdr": ("FDA: Medical Device Reporting", "https://www.fda.gov/medical-devices/medical-device-safety/medical-device-reporting-mdr-how-report-medical-device-problems"),
    "law": ("US Courts: glossary of legal terms", "https://www.uscourts.gov/glossary"),
    "invest": ("Investor.gov: investing glossary", "https://www.investor.gov/introduction-investing/investing-basics/glossary"),
    "cip": ("FinCEN: customer identification guidance", "https://www.fincen.gov/resources/statutes-regulations/guidance/interagency-interpretive-guidance-customer-identification"),
    "ferpa": ("US Department of Education: FERPA", "https://studentprivacy.ed.gov/ferpa"),
    "ghg": ("GHG Protocol: corporate standard", "https://ghgprotocol.org/corporate-standard"),
    "aviation": ("FAA: aviation English standard", "https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1031388"),
}


def read_cases():
    result = {}
    slug = None
    for line in (CONTENT / "cases.txt").read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            slug = line[1:-1]
            if slug in result:
                raise ValueError(f"Duplicate case group: {slug}")
            result[slug] = []
        else:
            if slug is None:
                raise ValueError("Case outside a course")
            function, brief, model = line.split("|", 2)
            result[slug].append(dict(function=function, brief=brief, model=model))
    return result


def scope_note(track):
    slug = track["slug"]
    if slug == "aviation":
        return "Workplace coordination English. This course does not teach radiotelephony phraseology or certify aviation language proficiency; operational communication follows approved aviation procedures."
    if track["category"] == "Health & life sciences":
        return "Fictional language practice for professional communication. Clinical, safety, regulatory, and patient-care decisions follow qualified supervision and current local procedures."
    if slug in {"law", "finance", "financial-advice", "real-estate", "insurance", "banking-operations", "legal-operations-compliance"}:
        return "Fictional language practice. Legal, financial, and regulatory meanings depend on jurisdiction and context; use current documents and qualified review for actual decisions."
    if slug in {"manufacturing", "engineering", "construction-architecture", "energy-utilities", "semiconductor"}:
        return "These cases practice communication. Actual equipment, construction, and safety work follows approved procedures and authorized specialist decisions."
    if slug == "cultural-leadership-us-branches":
        return "Ask about individual preferences and team norms. Nationality, accent, silence, or directness does not tell you what a person believes or how they will behave."
    return "All cases and figures are fictional. Adapt the language to your role and organization's current procedures, using invented details for practice."


def load_tracks():
    tracks = json.loads((CONTENT / "courses.json").read_text())
    glossary = dict(line.split('|', 1) for line in (CONTENT / 'glossary.txt').read_text().splitlines()
                    if line and not line.startswith('#'))
    glossary = {key.casefold(): value for key, value in glossary.items()}
    cases = read_cases()
    if set(cases) != {t["slug"] for t in tracks}:
        raise ValueError("Case groups and course inventory differ")
    for track_index, t in enumerate(tracks):
        slug = t["slug"]
        for term in t['jargon']:
            if term.get('definition_key'):
                term['definition'] = glossary[term['definition_key']]
        if len(cases[slug]) != len(t["modules"]) or len(t["modules"]) != 8:
            raise ValueError(f"Expected eight authored cases for {slug}")
        t["revision"] = REVISION
        t["scope_note"] = scope_note(t)
        source_keys = ["plain", "cefr"]
        source_keys += {
            "nursing-allied-health": ["sbar"], "healthcare-administration": ["hipaa", "sbar"],
            "medical-devices": ["device", "mdr"], "law": ["law"],
            "legal-operations-compliance": ["law"], "finance": ["invest"],
            "financial-advice": ["invest"], "banking-operations": ["cip"],
            "education-administration": ["ferpa"], "higher-education-research": ["ferpa"],
            "environmental-consulting": ["ghg"], "energy-utilities": ["ghg"], "aviation": ["aviation"],
        }.get(slug, [])
        t["sources"] = [dict(title=SOURCES[k][0], url=SOURCES[k][1]) for k in source_keys]
        vocab = {j["term"].casefold(): j for j in t["jargon"]}
        for i, (m, case) in enumerate(zip(t["modules"], cases[slug])):
            m.update(case)
            w = copy.deepcopy(WORKSHOPS[case["function"]])
            m["workshop"] = w
            m["number"] = i + 1
            m["id"] = f"module-{i + 1}"
            m["vocabulary"] = [vocab[term.casefold()] for term in m["terms"]]
            m["goals"] = [w["goal"], "Use two relevant field terms accurately and explain one in plain English.",
                          "Respond to a follow-up question and revise a short workplace message."]
            for qi, q in enumerate(w["questions"]):
                shift = (track_index + i + qi) % len(q["options"])
                q["options"] = q["options"][shift:] + q["options"][:shift]
                q["feedback"] = q["feedback"][shift:] + q["feedback"][:shift]
                q["correct_index"] = (-shift) % len(q["options"])
                q["answer"] = q["options"][q["correct_index"]]
            m["writing_task"] = ("Write a 70-110 word message for the person who needs to act on this case. "
                "State the purpose, preserve the relevant facts, and make the next action or unresolved question clear. "
                "Use a subject line and an appropriate opening. Do not invent a deadline, finding, or approval.")
            m["speaking_task"] = ("Prepare for two minutes. Speak for 45-60 seconds using the case facts, then respond to your partner's question. "
                "Switch roles and repeat without reading the model response.")
        t["outcomes"] = list(dict.fromkeys(m["workshop"]["goal"] for m in t["modules"]))
    return tracks


def content_hash():
    files = [CONTENT / "courses.json", CONTENT / "cases.txt", CONTENT / "glossary.txt", Path(__file__)]
    return hashlib.sha256(b"".join(p.read_bytes() for p in files)).hexdigest()


def related_tracks(track, tracks):
    return [t for t in tracks if t["slug"] != track["slug"] and t["category"] == track["category"]][:4]


def validate_tracks(tracks):
    """Fail publication when authored cases, definitions, or answer explanations are incomplete."""
    seen = set()
    for t in tracks:
        assert len(t["pdfs"]) == 4
        for j in t["jargon"]:
            assert len(j["definition"].split()) >= 4, (t["slug"], j["term"])
            assert "field-specific concept" not in j["definition"]
            assert "decision variable. Use it" not in j["definition"]
        for m in t["modules"]:
            assert m["brief"] not in seen, (t["slug"], m["id"])
            seen.add(m["brief"])
            assert len(m["model"].split()) >= 20
            assert len(m["vocabulary"]) >= 3
            for q in m["workshop"]["questions"]:
                assert len(set(q["options"])) == len(q["options"]) == len(q["feedback"])
                assert q["answer"] == q["options"][q["correct_index"]]
    return {"courses": len(tracks), "lessons": len(seen),
            "pdfs": sum(len(t["pdfs"]) for t in tracks),
            "vocabulary_entries": sum(len(t["jargon"]) for t in tracks)}
