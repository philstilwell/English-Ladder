from __future__ import annotations

import html
from pathlib import Path

from reportlab.platypus import PageBreak, Paragraph, Spacer

from generate_efsp_guarded_activities import add_answer_key, add_cloze_exercise, bounded_activity_instruction, make_dialogue_cloze
from generate_efsp_culture_pdfs import (
    S,
    box,
    build_pdf,
    bullets,
    h1,
    h2,
    h3,
    lines,
    p,
    rule,
    table,
)


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "pdf" / "efsp"


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def cover(title: str, subtitle: str, audience: str) -> list:
    return [
        Spacer(1, 0.95 * 72),
        p("EFSP Auxiliary ESL Curriculum", "CoverKicker"),
        Paragraph(esc(title), S["CoverTitle"]),
        Paragraph(esc(subtitle), S["CoverSub"]),
        Spacer(1, 0.25 * 72),
        box(
            audience,
            [
                "Focus: high-level professional English for legal workplaces, including client intake, confidentiality, privilege, litigation, discovery, legal writing, contracts, compliance, negotiation, advocacy, and realistic law-office dialogue.",
                "Designed for advanced ESL learners who already work in law, compliance, contracts, legal operations, paralegal support, or law-adjacent business roles and need field-specific fluency.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: this is legal English training, not legal advice. Laws, procedures, professional rules, and court practices vary by jurisdiction and role. Learners should practice language, judgment, and documentation habits while relying on qualified counsel and local rules for legal conclusions.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use legal terminology accurately in client calls, internal strategy meetings, research assignments, contract markups, discovery disputes, compliance reviews, and settlement discussions.",
    "Ask precise fact-development questions without promising outcomes, creating accidental advice, or losing client trust.",
    "Explain legal risk with appropriate caveats: facts known, facts missing, authority level, jurisdiction, procedural posture, and business consequence.",
    "Participate in litigation and transactional dialogues using realistic legal verbs: allege, assert, preserve, object, compel, waive, stipulate, reserve, amend, dismiss, and settle.",
    "Distinguish legal information, legal advice, privileged communications, confidential information, work product, and business advice.",
    "Write clear legal-workplace outputs: intake summaries, research questions, issue statements, contract comments, privilege notes, discovery updates, risk memos, and client-safe status emails.",
]


MODULES = [
    {
        "title": "Module 1. Legal English Mindset: Facts, Issues, Rules, Risk",
        "time": "90 minutes",
        "big_idea": "Legal English is precise because legal work turns on small distinctions: fact vs allegation, argument vs holding, risk vs conclusion, and client goal vs legal theory.",
        "objectives": [
            "Separate facts, assumptions, allegations, issues, rules, analysis, and conclusions.",
            "Use careful caveat language without sounding weak.",
            "Convert vague business questions into legally answerable questions.",
        ],
        "concepts": [
            "Issue spotting: identifying the legal question raised by a fact pattern.",
            "Procedural posture: where the matter stands in the legal process, which affects what arguments and evidence matter.",
            "Decision-grade risk: a legal assessment that states confidence, missing facts, authority, alternatives, and consequences.",
        ],
        "activities": [
            "Fact vs conclusion sort: learners classify 30 statements from a mock client email.",
            "Caveat ladder: learners rewrite overconfident answers into legally careful but useful advice-language.",
            "Issue-framing drill: learners turn broad business concerns into focused legal research questions.",
        ],
        "outputs": [
            "Legal caveat phrase bank.",
            "Issue statement template.",
            "Fact/assumption/risk distinction worksheet.",
        ],
    },
    {
        "title": "Module 2. Client Intake, Scope, Conflicts, and Confidentiality",
        "time": "90 minutes",
        "big_idea": "The first conversation can create legal, ethical, and business risk. Legal professionals must gather facts, preserve confidentiality, check conflicts, define scope, and avoid premature promises.",
        "objectives": [
            "Conduct an intake conversation with empathy and control.",
            "Use role-appropriate language around confidentiality, conflicts, privilege, and engagement.",
            "Summarize facts and next steps without creating an unintended commitment.",
        ],
        "concepts": [
            "Engagement scope: what the lawyer or legal team is and is not responsible for.",
            "Conflict check: screening whether existing duties to another client or party may limit representation.",
            "Privilege and confidentiality: related but not identical concepts; learners must avoid casual disclosures and overclaims.",
        ],
        "activities": [
            "Intake role-play: learners interview a potential client and pause before legal conclusions.",
            "Conflict-sensitive phrasing: learners ask for names, affiliates, adverse parties, and matter background without revealing protected details.",
            "Scope rewrite: learners convert a casual promise into a careful next-step statement.",
        ],
        "outputs": [
            "Intake question bank.",
            "Client-safe next-step script.",
            "Conflict-check information checklist.",
        ],
    },
    {
        "title": "Module 3. Litigation Lifecycle: Pleadings, Motions, Deadlines, Strategy",
        "time": "90 minutes",
        "big_idea": "Litigation conversations are shaped by procedure. Learners need language for complaints, answers, affirmative defenses, motions, orders, discovery, settlement, trial, judgment, and appeal.",
        "objectives": [
            "Explain the basic lifecycle of a civil litigation matter.",
            "Discuss pleadings, motions, jurisdiction, venue, deadlines, and remedies.",
            "Ask strategy questions that connect legal theory to evidence and client goals.",
        ],
        "concepts": [
            "Claim and defense: what one side must prove and how the other side responds.",
            "Motion practice: asking the court to order, dismiss, compel, exclude, or decide something.",
            "Remedy: what the client seeks, such as damages, injunction, declaratory relief, or settlement terms.",
        ],
        "activities": [
            "Lifecycle map: learners place litigation documents and events in order.",
            "Motion triage: learners decide whether a fact pattern suggests motion to dismiss, motion to compel, or summary judgment research.",
            "Deadline status update: learners brief a partner on filings, service, response dates, and risks.",
        ],
        "outputs": [
            "Civil litigation process map.",
            "Deadline update template.",
            "Motion strategy question list.",
        ],
    },
    {
        "title": "Module 4. Discovery, ESI, Privilege Review, and Depositions",
        "time": "90 minutes",
        "big_idea": "Discovery is language-heavy and risk-heavy. Teams must negotiate scope, preserve evidence, collect ESI, review privilege, prepare witnesses, and object without becoming unprofessional.",
        "objectives": [
            "Use discovery terminology in meet-and-confer calls and internal updates.",
            "Explain proportionality, burden, relevance, privilege, work product, and preservation.",
            "Prepare and debrief a deposition using clear, ethical language.",
        ],
        "concepts": [
            "ESI: electronically stored information such as email, chat, files, databases, logs, and metadata.",
            "Proportionality: discovery should fit the needs of the case, considering importance, access, resources, and burden.",
            "Privilege log: a record identifying withheld materials and the claimed basis for withholding them.",
        ],
        "activities": [
            "Meet-and-confer simulation: learners negotiate overbroad document requests.",
            "Privilege review drill: learners flag documents for attorney-client privilege, work product, business advice, or escalation.",
            "Deposition prep role-play: learners coach a witness on listening, answering only the question, and not speculating.",
        ],
        "outputs": [
            "Discovery objection phrase bank.",
            "Privilege escalation checklist.",
            "Deposition prep script.",
        ],
    },
    {
        "title": "Module 5. Legal Research, Authority, and Memo Writing",
        "time": "90 minutes",
        "big_idea": "Legal writing requires a hierarchy of authority and disciplined reasoning. A persuasive answer shows the issue, rule, relevant facts, contrary authority, and practical recommendation.",
        "objectives": [
            "Distinguish statute, regulation, case law, binding authority, persuasive authority, holding, dicta, and standard of review.",
            "Write a focused research question and a useful short answer.",
            "Present legal uncertainty without burying the conclusion.",
        ],
        "concepts": [
            "Binding vs persuasive authority: whether a court must follow the authority or may consider it.",
            "Holding vs dicta: the rule necessary to the decision vs language that is not essential to the outcome.",
            "IRAC/CRAC/CREAC: common structures for legal analysis; the best structure depends on audience and assignment.",
        ],
        "activities": [
            "Authority ranking: learners order sources by strength for a given jurisdiction.",
            "Short-answer rewrite: learners turn a long research note into a concise partner-ready answer.",
            "Contrary authority drill: learners explain bad law for the client without panic or concealment.",
        ],
        "outputs": [
            "Research assignment clarification checklist.",
            "Short-answer memo template.",
            "Authority and caveat language bank.",
        ],
    },
    {
        "title": "Module 6. Contracts, Redlines, and Negotiation",
        "time": "90 minutes",
        "big_idea": "Contract English is technical and strategic. Learners need to discuss obligations, risk allocation, remedies, negotiation posture, and business fallback positions.",
        "objectives": [
            "Use contract terms such as representation, warranty, covenant, condition, indemnity, limitation of liability, termination, governing law, and dispute resolution.",
            "Explain why a clause matters without over-legalizing the business conversation.",
            "Negotiate redlines with firm but professional language.",
        ],
        "concepts": [
            "Risk allocation: which party bears a particular legal, financial, operational, or compliance risk.",
            "Indemnity: one party may be required to cover certain losses, claims, or liabilities of another party.",
            "Fallback position: a less preferred but acceptable clause position if the counterparty rejects the first proposal.",
        ],
        "activities": [
            "Redline comment workshop: learners write business-friendly comments on five contract clauses.",
            "Negotiation ladder: learners practice ask, rationale, fallback, trade, and reserve language.",
            "Clause-risk briefing: learners explain limitation of liability and indemnity to a sales leader.",
        ],
        "outputs": [
            "Contract comment phrase bank.",
            "Redline negotiation script.",
            "Clause-risk summary template.",
        ],
    },
    {
        "title": "Module 7. Corporate, Compliance, Regulatory, and Investigation Language",
        "time": "90 minutes",
        "big_idea": "In-house and regulatory legal work often requires risk judgment under imperfect facts. Learners need language for materiality, disclosure, due diligence, governance, investigation, remediation, and enforcement.",
        "objectives": [
            "Discuss compliance issues using evidence, policy, exposure, materiality, and remediation language.",
            "Ask investigation questions that preserve documents and avoid contaminating witness accounts.",
            "Brief business leaders without turning uncertainty into either alarm or reassurance.",
        ],
        "concepts": [
            "Materiality: whether information could matter to a legal, regulatory, investor, or decision-making analysis.",
            "Due diligence: structured review of facts, documents, risks, obligations, and representations before a transaction or decision.",
            "Remediation: steps taken to correct a problem, reduce recurrence, and document control improvements.",
        ],
        "activities": [
            "Compliance triage: learners classify a marketing claim, privacy complaint, and vendor issue by risk and evidence.",
            "Investigation interview planning: learners draft neutral questions and preservation reminders.",
            "Executive risk update: learners present known facts, unknowns, exposure, options, and recommendation.",
        ],
        "outputs": [
            "Compliance triage memo.",
            "Investigation interview question set.",
            "Executive legal-risk update.",
        ],
    },
    {
        "title": "Module 8. Advocacy, Settlement, Ethics, and Professional Judgment",
        "time": "90 minutes",
        "big_idea": "Legal professionals need persuasive language that stays accurate, ethical, and client-centered. Strong advocacy does not mean overclaiming; strong settlement posture does not mean hiding risk from the client.",
        "objectives": [
            "Use advocacy language in oral argument, mediation, settlement, and client counseling.",
            "Respond to difficult questions from judges, partners, clients, opposing counsel, and regulators.",
            "Recognize when professional responsibility concerns require escalation.",
        ],
        "concepts": [
            "Candor, confidentiality, loyalty, competence, diligence, and communication are recurring professional-responsibility themes.",
            "Settlement authority: who can approve settlement terms and what information they need to decide.",
            "Ethical escalation: when a language problem is also a professional judgment problem.",
        ],
        "activities": [
            "Hot bench practice: learners answer a judge's skeptical question in 30 seconds.",
            "Settlement caucus: learners explain risk, cost, uncertainty, and recommended range to the client.",
            "Ethics scenario sorting: learners identify confidentiality, conflict, candor, unauthorized-practice, and supervision issues.",
        ],
        "outputs": [
            "Advocacy answer template.",
            "Settlement recommendation script.",
            "Ethics escalation checklist.",
        ],
    },
]


COURSE_OBJECTIVES = [bounded_activity_instruction(item) for item in COURSE_OBJECTIVES]
for _module in MODULES:
    _module["objectives"] = [bounded_activity_instruction(item) for item in _module["objectives"]]
    _module["activities"] = [bounded_activity_instruction(item) for item in _module["activities"]]


JARGON_GROUPS = [
    (
        "Court and litigation process",
        [
            ("Jurisdiction", "A court's legal authority to hear a matter or exercise power over a party or subject."),
            ("Venue", "The proper geographic or court location for a case."),
            ("Complaint", "A pleading that starts a civil lawsuit by stating claims against the defendant."),
            ("Answer", "A defendant's pleading responding to the complaint and often asserting defenses."),
            ("Motion", "A request asking the court to issue an order or take action."),
            ("Order", "A court's direction or decision on a matter before it."),
            ("Judgment", "A final court decision resolving the dispute or a claim."),
            ("Appeal", "A request for a higher court to review a lower court's decision."),
        ],
    ),
    (
        "Discovery, evidence, and proof",
        [
            ("Discovery", "The formal process for obtaining information and evidence from other parties or nonparties."),
            ("Deposition", "Out-of-court sworn testimony recorded for use in litigation."),
            ("Interrogatory", "A written question served in discovery that must be answered under oath."),
            ("Request for production", "A discovery request seeking documents, ESI, or tangible things."),
            ("Privilege", "A legal protection that may permit withholding certain communications or materials."),
            ("Work product", "Materials prepared in anticipation of litigation that may receive protection from disclosure."),
            ("Admissible", "Allowed to be considered by a judge or jury under the rules of evidence."),
            ("Burden of proof", "The obligation to prove a fact, claim, defense, or element to the required standard."),
        ],
    ),
    (
        "Research and legal writing",
        [
            ("Authority", "A legal source used to support analysis, such as a statute, regulation, case, or rule."),
            ("Binding authority", "Authority a court must follow in the relevant jurisdiction and procedural context."),
            ("Persuasive authority", "Authority a court may consider but does not have to follow."),
            ("Precedent", "A prior decision used as legal authority for later cases."),
            ("Holding", "The rule or principle necessary to the court's decision."),
            ("Dicta", "Language in an opinion that is not necessary to the holding."),
            ("Standard of review", "The level of deference an appellate court gives to a lower court's decision."),
            ("Distinguish", "Explain why a case or authority does not control because facts or law differ materially."),
        ],
    ),
    (
        "Client, ethics, and professional responsibility",
        [
            ("Confidentiality", "The professional duty to protect information relating to a client or matter, subject to applicable rules."),
            ("Attorney-client privilege", "A legal doctrine protecting certain confidential communications for legal advice."),
            ("Conflict of interest", "A situation where duties to one client, former client, third person, or personal interest may limit representation."),
            ("Informed consent", "Agreement after adequate information about material risks and alternatives."),
            ("Engagement letter", "A document defining the representation, scope, fees, responsibilities, and sometimes limitations."),
            ("Retainer", "An arrangement or payment connected to securing legal services, depending on local rules and agreement terms."),
            ("Waiver", "Intentional relinquishment of a known right, claim, protection, or objection."),
            ("Scope of representation", "The agreed boundaries of legal work to be performed.",
            ),
        ],
    ),
    (
        "Contracts and transactions",
        [
            ("Representation", "A statement of fact made by a party, often used to allocate risk."),
            ("Warranty", "A promise or assurance about a fact, condition, product, service, or performance."),
            ("Covenant", "A promise to do or not do something."),
            ("Condition precedent", "An event that must occur before an obligation becomes due."),
            ("Material breach", "A serious breach that may justify stronger remedies or termination."),
            ("Indemnity", "A clause requiring one party to cover certain losses, claims, or liabilities."),
            ("Limitation of liability", "A clause limiting the amount or type of damages recoverable."),
            ("Governing law", "The jurisdiction's law selected to interpret and enforce the agreement."),
        ],
    ),
    (
        "Corporate, compliance, and regulatory",
        [
            ("Due diligence", "Structured review of facts, documents, obligations, and risks before a transaction or decision."),
            ("Materiality", "Importance of information to a legal, regulatory, investor, or business decision."),
            ("Disclosure", "Providing required or relevant information to a party, regulator, investor, court, or public filing."),
            ("Fiduciary duty", "A duty of loyalty, care, or good faith owed by someone in a position of trust."),
            ("Board resolution", "A formal record of a board decision or authorization."),
            ("Enforcement action", "A regulator's action to investigate, stop, penalize, or remedy alleged violations."),
            ("Remediation", "Corrective action taken to fix a problem and prevent recurrence."),
            ("Audit trail", "Records that show who did what, when, and why."),
        ],
    ),
    (
        "Intellectual property and business law",
        [
            ("Trademark", "A source identifier such as a word, phrase, symbol, or design for goods or services."),
            ("Patent", "A government-granted right related to an invention, subject to statutory requirements."),
            ("Copyright", "Protection for original works fixed in a tangible medium, subject to limits and exceptions."),
            ("Trade secret", "Information with economic value from not being generally known and subject to reasonable secrecy efforts."),
            ("License", "Permission to use rights or property under specified conditions."),
            ("Assignment", "Transfer of rights, interests, or obligations, depending on context and agreement."),
            ("Claim substantiation", "Evidence supporting advertising or marketing claims before they are made."),
            ("Reasonable accommodation", "A workplace adjustment considered under disability laws, subject to legal standards and facts."),
        ],
    ),
    (
        "Legal verbs and meeting language",
        [
            ("Allege", "State a claim or fact as asserted but not yet proven."),
            ("Assert", "State a position, claim, right, defense, or privilege."),
            ("Stipulate", "Agree formally to a fact, issue, procedure, or condition."),
            ("Object", "State a legal objection to a question, evidence, request, or procedure."),
            ("Compel", "Ask or order someone to do something, often through a motion or court order."),
            ("Preserve", "Keep evidence, rights, arguments, or objections from being lost."),
            ("Reserve rights", "State that a party is not waiving rights or remedies by acting now."),
            ("Settle", "Resolve a dispute by agreement rather than final adjudication."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. Client Intake: Strong Emotions, Missing Facts",
        "setting": "A potential client calls after receiving a demand letter from a former business partner.",
        "dialogue": [
            ("Client", "They are lying. Can you tell them we will sue immediately?"),
            ("Legal team", "I understand this feels urgent. Before we discuss strategy, I need to gather facts and run a conflict check."),
            ("ESL learner", "Can you send the demand letter, the contract, and any recent emails with the former partner? Also, please list the company names and individuals involved so we can check conflicts."),
            ("Client", "So do we have a case?"),
            ("ESL learner", "I cannot assess that responsibly from one call. After we review the documents and confirm scope, we can identify claims, defenses, deadlines, and practical options."),
        ],
        "notes": [
            "Good intake language protects trust without promising an outcome.",
            "Conflict checks and engagement scope should come before substantive commitments.",
        ],
    },
    {
        "title": "2. Partner Assignment: Research Memo Under Pressure",
        "setting": "A partner asks for a quick memo on whether a forum-selection clause is enforceable.",
        "dialogue": [
            ("Partner", "I need an answer by noon. Is the forum-selection clause enforceable?"),
            ("ESL learner", "I can give you a short answer by noon. To focus the research, which jurisdiction controls, and are we challenging enforcement or defending it?"),
            ("Partner", "Defending it in federal court. The contract chooses Delaware law but the case was filed in California."),
            ("ESL learner", "Understood. I will check binding Ninth Circuit authority, Delaware choice-of-law relevance, any public-policy exceptions, and procedural posture. I will flag contrary authority separately."),
        ],
        "notes": [
            "Clarify jurisdiction, posture, desired use, and deadline before researching.",
            "A legal memo should say how strong the answer is and why.",
        ],
    },
    {
        "title": "3. Contract Redline: Indemnity and Liability Cap",
        "setting": "A SaaS vendor and enterprise customer negotiate risk allocation.",
        "dialogue": [
            ("Sales lead", "The customer rejected our limitation of liability. Can we just accept?"),
            ("Lawyer", "Not without understanding the exposure."),
            ("ESL learner", "The issue is not only the cap amount. Their redline excludes confidentiality, data security, IP infringement, and indemnity claims from the cap. That could create uncapped exposure."),
            ("Sales lead", "What is a reasonable fallback?"),
            ("ESL learner", "We can offer a super-cap for data security and IP claims, tied to a multiple of fees, while keeping consequential damages excluded. I would not accept unlimited liability without executive approval."),
        ],
        "notes": [
            "Contract comments should connect clause language to business risk.",
            "Fallback language helps business teams negotiate without giving away the legal position too early.",
        ],
    },
    {
        "title": "4. Discovery Meet-and-Confer: Overbroad Requests",
        "setting": "Opposing counsel requests all communications from five years across every product line.",
        "dialogue": [
            ("Opposing counsel", "Your objections are boilerplate. We need all communications to understand the pattern."),
            ("ESL learner", "We disagree that the request is proportional as drafted. It covers unrelated products, custodians, and time periods. We can propose targeted custodians, search terms, and a three-year window tied to the claims."),
            ("Opposing counsel", "You are withholding relevant evidence."),
            ("ESL learner", "We are not refusing discovery. We are asking to tailor the scope to nonprivileged, relevant, and proportional material. If you identify specific gaps, we can discuss them."),
        ],
        "notes": [
            "Meet-and-confer language should be firm, record-conscious, and professional.",
            "Avoid personal accusations; keep the discussion on scope, burden, relevance, and proportionality.",
        ],
    },
    {
        "title": "5. Deposition Prep: Nervous Witness",
        "setting": "A product manager will be deposed about an internal defect report.",
        "dialogue": [
            ("Witness", "What if I do not remember? I do not want to look unprepared."),
            ("ESL learner", "If you do not remember, say that. Do not guess. Listen to the full question, answer only that question, and ask for clarification if a term is unclear."),
            ("Witness", "Can I explain the whole background?"),
            ("ESL learner", "Only if the question asks for it. Your job is to testify truthfully, not to volunteer every fact. If privileged legal advice comes up, pause so counsel can address it."),
        ],
        "notes": [
            "Deposition prep language must be ethical: truthful, clear, and non-coaching as to substance.",
            "Learners should avoid scripts that tell a witness what facts to say.",
        ],
    },
    {
        "title": "6. Privilege Review: Copying a Lawyer Is Not Magic",
        "setting": "A review team is deciding whether internal emails are privileged.",
        "dialogue": [
            ("Reviewer", "Legal is copied, so this is privileged."),
            ("ESL learner", "Maybe, but not automatically. We need to ask whether the email seeks or gives legal advice, who received it, and whether confidentiality was maintained."),
            ("Reviewer", "This one discusses pricing strategy with counsel copied."),
            ("ESL learner", "That may be business advice rather than legal advice. Let's tag it for senior review instead of making the privilege call ourselves."),
        ],
        "notes": [
            "Privilege calls are jurisdiction- and fact-sensitive.",
            "Escalation language is better than overconfident privilege conclusions.",
        ],
    },
    {
        "title": "7. Motion Strategy: Dismiss or Summary Judgment?",
        "setting": "The team discusses whether to challenge a weak claim early.",
        "dialogue": [
            ("Client", "The claim is false. Can we file a motion to dismiss?"),
            ("Lawyer", "A motion to dismiss usually tests legal sufficiency, not whether the facts are true."),
            ("ESL learner", "If the complaint fails to state a required element, dismissal may be worth researching. If our argument depends on evidence outside the pleadings, summary judgment may be the better later vehicle."),
            ("Client", "So we wait?"),
            ("ESL learner", "We should evaluate cost, timing, likelihood of success, and whether an early motion educates the court or only delays discovery."),
        ],
        "notes": [
            "Procedural posture changes the available argument.",
            "A client-friendly explanation should distinguish legal sufficiency from factual proof.",
        ],
    },
    {
        "title": "8. Settlement Caucus: Risk, Cost, and Authority",
        "setting": "During mediation, the client wants to reject a settlement offer on principle.",
        "dialogue": [
            ("Client", "I would rather go to trial than pay them anything."),
            ("ESL learner", "That is a valid business position, but let's separate principle from decision risk. Trial could vindicate the company, but it also means legal fees, management distraction, uncertainty, and potential adverse precedent."),
            ("Client", "What range do you recommend?"),
            ("ESL learner", "Based on current evidence, litigation cost, and downside exposure, I recommend authority up to this range, but only with confidentiality, no admission of liability, and a mutual release."),
        ],
        "notes": [
            "Settlement language should respect client values while surfacing decision consequences.",
            "Authority, release, confidentiality, and non-admission terms often matter as much as amount.",
        ],
    },
    {
        "title": "9. Compliance Review: Advertising Claim Substantiation",
        "setting": "Marketing wants to launch an ad saying a product is 'clinically proven' to improve focus.",
        "dialogue": [
            ("Marketing", "Competitors make stronger claims than this. Can we approve it?"),
            ("ESL learner", "We need substantiation for the express and implied claims before launch. 'Clinically proven' suggests reliable evidence, not just user testimonials."),
            ("Marketing", "We have a small internal survey."),
            ("ESL learner", "That may support customer satisfaction, but probably not a clinical efficacy claim. A safer path is to revise the claim to match the evidence or obtain stronger support before release."),
        ],
        "notes": [
            "Compliance review often turns on what a reasonable consumer may take from the claim.",
            "The legal team should propose a compliant alternative, not only block the campaign.",
        ],
    },
    {
        "title": "10. Board Briefing: Material Risk and Disclosure",
        "setting": "An in-house legal team briefs executives on a regulatory inquiry.",
        "dialogue": [
            ("CFO", "Do we have to disclose this inquiry?"),
            ("General counsel", "We need a materiality analysis before answering."),
            ("ESL learner", "Current facts: the regulator requested documents, no allegations have been filed, potential exposure is uncertain, and the issue relates to a growing product line. The disclosure question depends on likelihood, magnitude, existing public statements, and investor significance."),
            ("CFO", "Can we say it is not material?"),
            ("ESL learner", "I would not say that yet. We can say legal is assessing materiality and will update the disclosure committee after reviewing the request and business impact."),
        ],
        "notes": [
            "Materiality language should not be rushed.",
            "Board and executive updates need known facts, unknowns, timing, owner, and decision path.",
        ],
    },
    {
        "title": "11. Internal Investigation: Neutral Interviewing",
        "setting": "Legal interviews an employee about a possible policy violation.",
        "dialogue": [
            ("Employee", "Am I being accused of something?"),
            ("ESL learner", "We are gathering facts about a concern that was reported. I am not here to argue with you or make a final decision today."),
            ("Employee", "Should I delete my personal notes?"),
            ("ESL learner", "No. Please preserve documents and messages that may relate to this topic. If you are unsure whether something is relevant, ask before deleting or changing it."),
            ("Employee", "Can you tell me what other people said?"),
            ("ESL learner", "I cannot share interview details. I can ask you about your own recollection and any documents that may help us understand the timeline."),
        ],
        "notes": [
            "Investigation questions should avoid suggesting the desired answer.",
            "Preservation language should be simple, direct, and documented.",
        ],
    },
    {
        "title": "12. Oral Argument: Answering the Hard Question",
        "setting": "A judge asks about the weakest point in counsel's statutory interpretation.",
        "dialogue": [
            ("Judge", "Counsel, does your reading make subsection (c) unnecessary?"),
            ("ESL learner", "No, Your Honor. Subsection (c) still does work in two situations. First, it covers post-termination conduct. Second, it supplies the remedy when the notice period has expired."),
            ("Judge", "But the other side says that is not in the text."),
            ("ESL learner", "Respectfully, the text supports it when subsections (b) and (c) are read together. If the Court disagrees, our narrower fallback is that dismissal should be without prejudice because the defect is curable."),
        ],
        "notes": [
            "Advocacy language should answer directly, then explain.",
            "Fallback arguments preserve credibility when the main argument faces pressure.",
        ],
    },
]


PHRASE_BANK = {
    "Careful legal conclusions": [
        "Based on the facts we have now, the stronger argument appears to be...",
        "That conclusion depends on jurisdiction, procedural posture, and several facts we still need to confirm.",
        "I would not characterize this as settled law without checking controlling authority.",
        "The business risk is clear, but the legal exposure needs more factual development.",
    ],
    "Client intake and scope": [
        "Before we discuss strategy, I need to gather facts and confirm there is no conflict.",
        "I can explain the process, but I cannot give a legal conclusion until we review the documents.",
        "That issue may be outside the current scope, so we should confirm whether you want us to evaluate it.",
        "Please do not send privileged or sensitive materials until we confirm the proper channel and scope.",
    ],
    "Research and writing": [
        "What jurisdiction, deadline, procedural posture, and intended audience should guide the research?",
        "The short answer is yes, but with two important limitations.",
        "The best authority is binding, but the facts are distinguishable.",
        "There is contrary persuasive authority, so I would frame the conclusion as moderate rather than strong.",
    ],
    "Discovery and privilege": [
        "We object to the request as overbroad and disproportionate as drafted.",
        "We are willing to discuss targeted custodians, search terms, date ranges, and document categories.",
        "This may involve legal advice, but we should escalate the privilege call rather than assume.",
        "Please preserve potentially relevant documents and do not alter or delete related communications.",
    ],
    "Contracts and negotiation": [
        "Our concern is not the wording alone; it is the risk allocation behind the wording.",
        "We can accept the concept if the clause includes a cap, a defined scope, and an exclusion for indirect damages.",
        "That is not our preferred position, but a possible fallback is...",
        "I need business approval before accepting uncapped liability or an open-ended indemnity.",
    ],
    "Advocacy and settlement": [
        "Respectfully, Your Honor, the record supports a narrower point.",
        "The strongest point for the other side is..., but our response is...",
        "Settlement avoids litigation cost and uncertainty, but it also requires acceptable non-monetary terms.",
        "We can recommend a range, but the client must approve settlement authority.",
    ],
}


WORKBOOK_TASKS = [
    "A business leader asks, 'Can we sue them?' Rewrite the question into facts needed, legal issues, possible remedies, and a responsible next-step response.",
    "A potential client calls with an urgent dispute. Draft your first five intake questions and a careful sentence about conflicts, scope, and document review.",
    "A partner asks for a litigation status update. Write a concise update covering pleadings, deadlines, pending motions, discovery, and next risk.",
    "Opposing counsel sends overbroad discovery requests. Draft a meet-and-confer response that is firm, professional, and record-conscious.",
    "You find a case that hurts the client's position. Write a short memo paragraph explaining the contrary authority and how it might be distinguished.",
    "A sales leader wants to accept a broad indemnity. Write a business-friendly explanation of the risk and propose two fallback positions.",
    "A marketing claim may be unsupported. Write a compliance review note identifying express claim, implied claim, evidence gap, and safer alternative.",
    "A judge asks the hardest question about your argument. Draft a direct answer, supporting reason, and fallback position.",
]


SOURCES = [
    "U.S. Courts Glossary of Legal Terms for federal court and litigation vocabulary.",
    "Federal Rules of Civil Procedure, especially discovery concepts and Rule 26 proportionality language.",
    "Federal Rules of Evidence for evidence vocabulary such as admissibility, hearsay, and privilege context.",
    "American Bar Association Model Rules of Professional Conduct for confidentiality, conflicts, communication, competence, and related professional-responsibility vocabulary.",
    "U.S. Patent and Trademark Office resources for trademark, patent, copyright, and IP terminology.",
    "Federal Trade Commission business guidance for advertising claim substantiation and compliance-review vocabulary.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in legal environments: lawyers, law students, paralegals, legal assistants, compliance analysts, contracts specialists, legal operations staff, in-house legal team members, and business professionals who work closely with counsel."
        )
    )
    story.append(
        p(
            "The course is not a law course and does not train learners to give legal advice. It trains professional English for legal work: careful questions, precise terminology, client-safe caveats, ethical awareness, document discipline, persuasive but accurate advocacy, and clear written updates."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "Legal teams compress complex judgments into short phrases: conflict check, privileged and confidential, work product, motion to compel, proportionality objection, binding authority, distinguishable facts, indemnity carveout, materiality analysis, settlement authority, and no admission of liability. Learners need both the vocabulary and the conversational habits that protect the client, the record, and the professional relationship."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_legal_communication_principles(story: list) -> None:
    story += h1("Legal Communication Principles")
    story.append(h2("Separate legal facts from legal conclusions"))
    story.append(
        p(
            "Clients and business partners often ask for a conclusion before the legal team has enough facts. Strong legal English acknowledges urgency, gathers the facts needed for analysis, and avoids premature certainty. A learner should be able to say what is known, what is assumed, what is alleged, what remains unknown, and what legal question follows."
        )
    )
    story.append(h2("Use caveats as professional precision"))
    story.append(
        bullets(
            [
                "Use 'based on the facts we have now' when facts may change.",
                "Use 'in this jurisdiction' when local law controls the answer.",
                "Use 'the stronger argument is' when the law is unsettled or fact-sensitive.",
                "Use 'we should not characterize this as privileged until review' when a protection is possible but not confirmed.",
                "Use 'this is a business decision with legal risk' when counsel can advise but not decide.",
            ]
        )
    )
    story.append(h2("Turn vague legal requests into answerable assignments"))
    story.append(
        table(
            [
                ["Vague request", "Stronger legal-workplace question"],
                ["Can we sue them?", "What claims, remedies, evidence, deadlines, cost, and business objectives should we evaluate?"],
                ["Is this clause okay?", "Which risk does the clause allocate, what fallback is acceptable, and who owns the business risk?"],
                ["Is this privileged?", "Who communicated, for what purpose, was legal advice sought or given, and was confidentiality preserved?"],
                ["Can we use this ad claim?", "What express and implied claims will consumers take away, and what substantiation exists before launch?"],
            ],
            [2.3 * 72, 4.7 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in context, ask a clarification question, and explain why the distinction matters. Because legal meaning varies by jurisdiction and context, instructors should treat these as workplace-English definitions, not legal advice."
        )
    )
    for title, items in JARGON_GROUPS:
        story.append(h2(title))
        rows = [["Term", "Working meaning"]]
        rows.extend([[term, definition] for term, definition in items])
        story.append(table(rows, [1.55 * 72, 5.45 * 72]))


def add_module_details(story: list) -> None:
    story += h1("Instructor Module Plans")
    for module in MODULES:
        story.append(h2(f"{module['title']} ({module['time']})"))
        story.append(p(module["big_idea"]))
        story.append(h3("Learning objectives"))
        story.append(bullets(module["objectives"]))
        story.append(h3("Core concepts"))
        story.append(bullets(module["concepts"]))
        story.append(h3("Activities"))
        story.append(bullets([bounded_activity_instruction(activity) for activity in module["activities"]], numbered=True))
        story.append(h3("Learner outputs"))
        story.append(bullets(module["outputs"]))
        story.append(
            box(
                "Facilitator note",
                [
                    "When learners answer too quickly, ask: what jurisdiction, what procedural posture, what facts are assumed, what authority supports the point, what facts are missing, and what role is the learner allowed to play?"
                ],
                "blue",
            )
        )


def add_assessment(story: list) -> None:
    story += h1("Assessment and Coaching")
    story.append(h2("Pre-course diagnostic"))
    story.append(
        bullets(
            [
                "Learner explains their legal role in 90 seconds, including matter types, documents handled, audiences, and highest-risk conversations.",
                "Learner defines twelve legal terms and uses six in realistic legal-workplace sentences.",
                "Learner handles a short role-play: a client asks for an immediate legal conclusion before the team has documents or conflict clearance.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but overgeneralizes.", "Uses common terms accurately in context.", "Defines terms, notices misuse, and adapts to audience and role."],
                ["Fact development", "Accepts client wording too quickly.", "Separates facts, assumptions, allegations, and missing evidence.", "Builds a legally useful fact record while preserving trust."],
                ["Caveat control", "Sounds either too certain or too vague.", "Uses clear caveats tied to jurisdiction, posture, facts, and authority.", "Makes uncertainty useful for decision-making."],
                ["Legal writing", "Summarizes information without prioritizing.", "States issue, short answer, rule, analysis, and recommendation.", "Handles contrary authority and practical consequence concisely."],
                ["Professional judgment", "Misses confidentiality, conflict, or role boundaries.", "Recognizes when to pause and escalate.", "Protects client, record, ethics, and business relationship under pressure."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a legal-team response to a fast-moving dispute. A customer sends a demand letter, sales wants to continue negotiating a contract, marketing wants to launch related claims, and leadership asks whether disclosure is required. The learner must conduct intake, identify missing facts, preserve documents, frame research questions, explain contract and litigation risk, and write a client-safe status update."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "Law English",
        "Instructor guide for high-level ESL learners working in law, compliance, contracts, litigation support, legal operations, and legal-adjacent roles",
        "Audience: instructors, legal English coaches, law-firm trainers, legal operations teams, and advanced professional English programs",
    )
    add_course_opening(story)
    add_legal_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-law-english-instructor-guide.pdf",
        "EFSP Law English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Law English",
        "Participant workbook: client-safe language, legal terminology, research discussion, contracts, discovery, compliance, and advocacy practice",
        "Audience: advanced ESL learners working in law, compliance, contracts, litigation support, legal operations, and related business roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you speak and write more precisely in legal workplaces. The goal is not to sound dramatic or overly formal. The goal is to protect meaning: facts, legal issues, authority, uncertainty, confidentiality, risk, and next steps."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which legal conversations are hardest for you: client intake, partner updates, contract markups, discovery calls, research memos, compliance reviews, settlement, or hearings?",
                "Which legal terms do you understand when reading but avoid when speaking?",
                "When someone pressures you for a quick answer, do you become too vague, too certain, too indirect, or too technical?",
                "What is one recent legal-workplace sentence you wish you had phrased more carefully?",
            ]
        )
    )
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("Legal Matter Language")
    story.append(
        table(
            [
                ["Layer", "Useful verbs", "Example sentence"],
                ["Facts", "gather, confirm, preserve, document, verify", "We need to confirm the timeline before assessing exposure."],
                ["Issues", "identify, frame, narrow, separate, prioritize", "The immediate issue is whether the deadline has been triggered."],
                ["Authority", "research, cite, distinguish, reconcile, update", "The case is persuasive, but not binding in this jurisdiction."],
                ["Procedure", "file, serve, move, oppose, object, compel", "We may need to move to compel if the production remains incomplete."],
                ["Contracts", "draft, redline, negotiate, accept, reserve", "We can accept the concept if the indemnity is capped."],
                ["Risk", "assess, quantify, mitigate, escalate, disclose", "The legal risk is moderate, but the reputational risk may be higher."],
            ],
            [1.15 * 72, 2.15 * 72, 3.7 * 72],
        )
    )
    story += h1("Practice Pages")
    answer_key: list[dict[str, str]] = []
    for index, module in enumerate(MODULES):
        dialogue = DIALOGUES[index % len(DIALOGUES)]
        story.append(PageBreak())
        story.append(h2(module["title"]))
        story.append(p(module["big_idea"]))
        story.append(h3("What you should be able to do"))
        story.append(bullets(module["objectives"]))
        add_cloze_exercise(story, make_dialogue_cloze(dialogue), answer_key)
    story.append(PageBreak())
    story += h1("Phrase Bank")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-law-english-participant-workbook.pdf",
        "EFSP Law English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "Law Dialogue Lab",
        "Realistic legal-workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners",
        "Audience: instructors, legal English coaches, peer practice groups, law-firm training teams, and legal operations teams",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: legal speaker, counterpart, observer.",
                "Read the model dialogue once. Then replay it with new facts, different risk level, or a different audience.",
                "The observer listens for terminology accuracy, careful caveats, fact development, role boundaries, confidentiality awareness, and decision clarity.",
                "After each role-play, replay the hardest 30 seconds with a more precise legal-workplace sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners turn role-play into legal advice. Keep the focus on language, reasoning structure, ethical awareness, and escalation habits. When a scenario depends on actual law, ask learners to identify the question and source, not to invent the rule."
            ],
            "amber",
        )
    )
    answer_key: list[dict[str, str]] = []
    for item in DIALOGUES:
        story.append(PageBreak())
        story.append(Paragraph(esc(item["title"]), S["CardTitle"]))
        story.append(rule())
        story.append(box("Setting", [item["setting"]], "blue"))
        rows = [["Speaker", "Line"]]
        rows.extend([[speaker, line] for speaker, line in item["dialogue"]])
        story.append(table(rows, [1.25 * 72, 5.75 * 72]))
        story.append(h3("Language notes"))
        story.append(bullets(item["notes"]))
        add_cloze_exercise(story, make_dialogue_cloze(item), answer_key, show_context=False)
        story.append(h3("Observer checklist"))
        story.append(
            bullets(
                [
                    "Did the learner separate facts, assumptions, legal issues, and conclusions?",
                    "Did the learner use legal terminology accurately and define it when useful?",
                    "Did the learner preserve confidentiality, privilege, conflict, and role boundaries?",
                    "Did the learner make a clear next step, recommendation, or escalation path?",
                ]
            )
        )
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-law-dialogue-lab.pdf",
        "EFSP Law Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "Law Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise legal vocabulary and workplace meeting language",
        "Audience: advanced ESL learners in law firms, in-house legal teams, compliance, contracts, legal operations, and legal-adjacent roles",
    )
    story += h1("How to Use Legal Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it locates the legal issue more precisely.",
                "Pair legal terms with facts, authority, jurisdiction, procedural posture, and audience.",
                "Define terms for clients and business teams without sounding patronizing.",
                "Avoid legal conclusions before conflict checks, engagement scope, document review, and local-law confirmation.",
            ]
        )
    )
    add_jargon_sections(story)
    story += h1("Common Meeting Moves")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story += h1("Fast Contrast Pairs")
    story.append(
        table(
            [
                ["Do not confuse", "Working contrast"],
                ["Fact vs allegation", "A fact is established or supported; an allegation is asserted but not yet proven."],
                ["Confidentiality vs privilege", "Confidentiality is a professional duty; privilege is a legal protection from disclosure in certain contexts."],
                ["Legal information vs legal advice", "Information explains general concepts; advice applies law to specific facts for a person or entity."],
                ["Binding vs persuasive authority", "Binding authority must be followed; persuasive authority may influence but does not control."],
                ["Holding vs dicta", "A holding is necessary to the decision; dicta is commentary not essential to the result."],
                ["Representation vs warranty", "Both allocate factual risk, but usage and remedies depend on contract language and law."],
                ["Indemnity vs limitation of liability", "Indemnity shifts specified losses; limitation clauses cap or exclude damages."],
                ["Dismissal with vs without prejudice", "With prejudice usually bars refiling; without prejudice may allow refiling or correction."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-law-jargon-quick-reference.pdf",
        "EFSP Law Jargon Field Guide",
        story,
    )


def main() -> None:
    paths = [
        instructor_guide(),
        participant_workbook(),
        dialogue_lab(),
        quick_reference(),
    ]
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
