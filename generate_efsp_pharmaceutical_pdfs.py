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
                "Focus: high-level professional English for pharmaceutical workplaces, including drug development, target product profile, IND, NDA, BLA, clinical trial design, GCP, endpoints, estimands, safety, pharmacovigilance, CMC, CGMP, quality events, regulatory strategy, labeling, medical affairs, promotion review, market access, RWE, lifecycle management, and realistic cross-functional dialogue.",
                "Designed for advanced ESL learners who work in clinical development, clinical operations, regulatory affairs, pharmacovigilance, medical affairs, quality, CMC, manufacturing, biostatistics, data management, market access, commercial compliance, or pharma-adjacent roles.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: pharmaceutical English is evidence, safety, compliance, and cross-functional judgment under pressure. Learners need to be scientifically precise, operationally clear, patient-centered, and careful with claims. This curriculum teaches professional communication and judgment, not medical, regulatory, or legal advice.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use pharmaceutical terminology accurately in development-team meetings, protocol reviews, clinical operations calls, regulatory interactions, safety reviews, CMC meetings, quality investigations, medical affairs discussions, launch readiness reviews, and market-access conversations.",
    "Translate vague scientific, clinical, regulatory, or commercial goals into target population, mechanism, endpoint, evidence standard, risk, timeline, owner, and decision criteria.",
    "Discuss drug development, clinical trial design, GCP, statistical interpretation, pharmacovigilance, manufacturing quality, regulatory strategy, labeling, promotion review, medical affairs, RWE, and lifecycle management in precise professional English.",
    "Push back on weak or risky proposals: endpoint drift, protocol overload, underpowered studies, premature efficacy claims, incomplete safety narratives, CMC shortcuts, undocumented deviations, off-label promotion risk, and launch plans without supply or reimbursement realism.",
    "Participate in realistic pharma dialogues: IND readiness, endpoint debate, enrollment rescue, data readout, safety signal triage, quality deviation, labeling negotiation, promotional claim review, MSL boundary-setting, payer evidence, biosimilar discussion, and launch governance.",
    "Write clear pharma outputs: protocol clarification notes, risk-based monitoring summaries, safety narratives, query-resolution messages, CMC risk updates, CAPA summaries, labeling comments, MLR review notes, payer value messages, and launch readiness updates.",
]


MODULES = [
    {
        "title": "Module 1. Drug Development Strategy, Unmet Need, TPP, and Evidence Logic",
        "time": "90 minutes",
        "big_idea": "Pharma conversations often fail when teams discuss activities before aligning on the patient population, unmet need, target product profile, evidence standard, regulatory path, and commercial reality.",
        "objectives": [
            "Distinguish indication, mechanism of action, target population, standard of care, unmet need, TPP, product profile, and value proposition.",
            "Explain how preclinical, clinical, regulatory, safety, CMC, and market-access evidence connect across development.",
            "Ask strategic questions when a program goal is scientifically interesting but not yet clinically or commercially meaningful.",
        ],
        "concepts": [
            "Target product profile: a planning tool describing intended indication, population, dosing, efficacy, safety, differentiation, labeling goals, and evidence needs.",
            "Unmet need: clinically meaningful gap in current care, not simply a market opportunity.",
            "Evidence logic: how each study, assay, endpoint, and analysis supports a future decision or label claim.",
        ],
        "activities": [
            "TPP alignment: learners revise a vague product goal into a decision-ready TPP excerpt.",
            "Evidence chain drill: learners map nonclinical, clinical, CMC, safety, and market-access evidence to a development decision.",
            "Unmet-need debate: learners distinguish patient burden, treatment gap, competitive differentiation, and payer relevance.",
        ],
        "outputs": [
            "TPP clarification memo.",
            "Evidence logic map.",
            "Unmet-need statement.",
        ],
    },
    {
        "title": "Module 2. Regulatory Pathways, IND Readiness, NDA/BLA Strategy, and Agency Interaction",
        "time": "90 minutes",
        "big_idea": "Regulatory language must be specific about what is known, what is proposed, what the agency is being asked to agree with, and what remains a sponsor risk.",
        "objectives": [
            "Use regulatory terms such as IND, NDA, BLA, accelerated approval, breakthrough therapy, orphan designation, complete response letter, information request, and meeting package accurately.",
            "Explain an agency interaction plan without overstating what regulators have agreed to.",
            "Identify readiness gaps before a submission or formal meeting.",
        ],
        "concepts": [
            "IND: regulatory submission that allows clinical investigation of an investigational drug in humans in the United States.",
            "NDA/BLA: marketing application asking FDA to approve a drug or biologic based on evidence of safety, effectiveness, and quality.",
            "Agency alignment: a documented understanding of regulatory feedback, not a guarantee of approval.",
        ],
        "activities": [
            "IND readiness review: learners identify missing nonclinical, CMC, protocol, investigator brochure, and safety elements.",
            "Meeting objective rewrite: learners turn broad agency questions into answerable regulatory questions.",
            "Regulatory feedback debrief: learners summarize feedback without exaggerating certainty.",
        ],
        "outputs": [
            "Regulatory readiness checklist.",
            "Agency question bank.",
            "Regulatory feedback summary.",
        ],
    },
    {
        "title": "Module 3. Clinical Trial Design, Protocols, GCP, and Operations",
        "time": "90 minutes",
        "big_idea": "Clinical trial English requires protocol precision, ethical discipline, operational realism, and the ability to explain tradeoffs among scientific rigor, patient protection, site burden, enrollment, and data integrity.",
        "objectives": [
            "Use trial-design terms such as randomization, blinding, control arm, endpoint, inclusion criteria, exclusion criteria, stratification, protocol deviation, informed consent, monitoring, and site feasibility accurately.",
            "Explain GCP concepts in plain English: participant protection, data integrity, risk proportionate quality, documentation, oversight, and responsibilities.",
            "Push back on protocol complexity that may harm feasibility or data quality.",
        ],
        "concepts": [
            "Protocol: the document specifying study objectives, design, population, treatments, assessments, endpoints, safety monitoring, and statistical plan.",
            "GCP: international ethical and scientific quality standard for designing, conducting, recording, and reporting clinical trials.",
            "Risk-based quality: focus on factors critical to participant safety, rights, and data reliability.",
        ],
        "activities": [
            "Protocol burden audit: learners identify visits, assessments, and eligibility rules that may impair enrollment or retention.",
            "Site feasibility role-play: learners negotiate realistic enrollment assumptions with clinical operations.",
            "Deviation discussion: learners explain whether a deviation affects safety, rights, or data integrity.",
        ],
        "outputs": [
            "Protocol feasibility note.",
            "GCP explanation script.",
            "Risk-based monitoring summary.",
        ],
    },
    {
        "title": "Module 4. Endpoints, Estimands, Statistics, Data Readouts, and Clinical Meaning",
        "time": "90 minutes",
        "big_idea": "Data readouts can be technically correct but strategically misleading. Learners need language for statistical significance, clinical relevance, estimands, missing data, intercurrent events, multiplicity, subgroup findings, and uncertainty.",
        "objectives": [
            "Use statistical and clinical terms such as primary endpoint, secondary endpoint, exploratory endpoint, estimand, intercurrent event, p-value, confidence interval, hazard ratio, noninferiority margin, sensitivity analysis, and missing data.",
            "Explain the difference between statistical significance and clinical meaningfulness.",
            "Challenge overinterpretation of subgroup, post hoc, interim, or exploratory findings.",
        ],
        "concepts": [
            "Estimand: precise description of the treatment effect being estimated, including population, treatment condition, endpoint, intercurrent events, and summary measure.",
            "Clinical relevance: whether the magnitude, durability, and safety tradeoff of an effect matters for patients and decision-makers.",
            "Multiplicity: increased risk of false-positive conclusions when many comparisons are tested.",
        ],
        "activities": [
            "Readout rehearsal: learners explain a positive primary endpoint with mixed secondary endpoints.",
            "Estimand clarification: learners define what treatment effect the trial is actually estimating.",
            "Subgroup caution drill: learners rephrase overconfident claims from a small subgroup.",
        ],
        "outputs": [
            "Data readout talking points.",
            "Estimand plain-English explanation.",
            "Clinical relevance caveat set.",
        ],
    },
    {
        "title": "Module 5. Pharmacovigilance, Safety Signals, Risk-Benefit, and Label Updates",
        "time": "90 minutes",
        "big_idea": "Safety language must be calm, disciplined, and precise. Learners need to distinguish adverse event, adverse reaction, serious, severe, expected, unexpected, related, signal, and confirmed risk.",
        "objectives": [
            "Use pharmacovigilance terms accurately: AE, SAE, SUSAR, MedDRA, case narrative, causality, signal detection, aggregate report, risk-benefit, label change, REMS, and postmarketing commitment.",
            "Explain what can and cannot be concluded from spontaneous adverse event reports.",
            "Participate in safety triage without minimizing patient risk or overstating causality.",
        ],
        "concepts": [
            "Adverse event: any unfavorable medical occurrence after product use, whether or not considered related.",
            "Signal: information suggesting a possible causal association that requires further evaluation.",
            "Risk-benefit: integrated judgment about therapeutic benefit, known and potential risks, uncertainty, severity of disease, alternatives, and risk mitigation.",
        ],
        "activities": [
            "Safety case triage: learners classify seriousness, expectedness, relatedness, and reporting urgency.",
            "Signal meeting role-play: learners discuss a possible liver-safety signal with incomplete evidence.",
            "Label update language: learners draft cautious language for an emerging risk.",
        ],
        "outputs": [
            "Safety triage summary.",
            "Signal assessment questions.",
            "Risk-benefit update paragraph.",
        ],
    },
    {
        "title": "Module 6. CMC, CGMP, Quality Events, Manufacturing, and Supply",
        "time": "90 minutes",
        "big_idea": "Quality and manufacturing conversations require exact language because patient supply and product quality depend on documented control, not informal confidence.",
        "objectives": [
            "Use CMC and quality terms such as API, excipient, formulation, process validation, analytical method, specification, batch record, deviation, OOS, CAPA, change control, comparability, stability, tech transfer, and cold chain.",
            "Explain why CGMP compliance, documentation, and quality systems matter for product safety and supply continuity.",
            "Push back on release, supply, or process-change shortcuts that lack data or quality approval.",
        ],
        "concepts": [
            "CMC: chemistry, manufacturing, and controls information describing product quality, manufacturing process, testing, stability, and control strategy.",
            "Deviation: departure from an approved instruction, process, specification, or expectation that must be investigated and documented.",
            "CAPA: corrective and preventive action designed to address root cause and prevent recurrence.",
        ],
        "activities": [
            "Deviation review: learners explain impact, root cause, containment, and CAPA.",
            "Supply-risk call: learners communicate a batch delay without blaming quality or manufacturing.",
            "Comparability discussion: learners explain what evidence is needed after a manufacturing change.",
        ],
        "outputs": [
            "CMC risk update.",
            "Deviation and CAPA summary.",
            "Supply continuity communication.",
        ],
    },
    {
        "title": "Module 7. Labeling, Medical Affairs, Promotion Review, and Compliance Boundaries",
        "time": "90 minutes",
        "big_idea": "Pharma communication is constrained by approved labeling, evidence quality, audience, intent, and compliance rules. Learners need language for scientific exchange and for saying no to risky claims.",
        "objectives": [
            "Use terms such as prescribing information, indication, contraindication, warning, precaution, adverse reactions, fair balance, substantial evidence, off-label, promotional claim, medical review, MLR, and scientific exchange.",
            "Distinguish medical information, medical affairs, scientific exchange, promotional communication, and commercial messaging.",
            "Push back on claims that are accurate in a narrow sense but misleading, incomplete, off-label, or unsupported.",
        ],
        "concepts": [
            "Labeling: FDA-approved prescribing information and related materials that define approved use, dosing, safety, and evidence boundaries.",
            "Fair balance: presentation of benefits and risks in a way that is not misleading.",
            "MLR review: medical, legal, and regulatory review process for externally facing materials.",
        ],
        "activities": [
            "Claim review: learners revise a promotional claim that overstates subgroup data.",
            "MSL boundary role-play: learners respond to an unsolicited off-label question.",
            "Labeling negotiation: learners propose wording that is accurate, useful, and supportable.",
        ],
        "outputs": [
            "MLR comment set.",
            "Off-label boundary script.",
            "Labeling comment memo.",
        ],
    },
    {
        "title": "Module 8. Market Access, RWE, Launch Readiness, Biosimilars, and Lifecycle Management",
        "time": "90 minutes",
        "big_idea": "Approval is not the end of pharmaceutical strategy. Learners need language for evidence generation, payer value, access barriers, launch governance, real-world evidence, lifecycle plans, generics, biosimilars, and loss of exclusivity.",
        "objectives": [
            "Use terms such as HEOR, value proposition, payer, formulary, prior authorization, step therapy, budget impact, RWE, RWD, registry, label expansion, lifecycle management, patent cliff, generic, biosimilar, interchangeable, and reference product.",
            "Explain payer evidence needs without promising reimbursement.",
            "Discuss lifecycle options and launch risks across medical, regulatory, supply, access, commercial, and safety functions.",
        ],
        "concepts": [
            "RWD: data relating to patient health status or health care delivery routinely collected from sources such as EHRs, claims, registries, or digital tools.",
            "RWE: clinical evidence about usage, benefits, or risks derived from analysis of RWD.",
            "Biosimilar: a biologic highly similar to a reference product with no clinically meaningful differences in safety, purity, and potency.",
        ],
        "activities": [
            "Payer objection role-play: learners explain value without overclaiming outcomes.",
            "Launch readiness review: learners identify gaps across supply, access, medical training, safety, and promotional approval.",
            "Lifecycle scenario: learners compare label expansion, formulation improvement, RWE study, partnership, and biosimilar defense options.",
        ],
        "outputs": [
            "Payer value message.",
            "Launch readiness update.",
            "Lifecycle recommendation.",
        ],
    },
]


COURSE_OBJECTIVES = [bounded_activity_instruction(item) for item in COURSE_OBJECTIVES]
for _module in MODULES:
    _module["objectives"] = [bounded_activity_instruction(item) for item in _module["objectives"]]
    _module["activities"] = [bounded_activity_instruction(item) for item in _module["activities"]]


JARGON_GROUPS = [
    (
        "Development strategy and regulatory path",
        [
            ("Indication", "Disease, condition, or patient population for which a product is intended or approved."),
            ("MOA", "Mechanism of action; how the product is understood to produce a biological effect."),
            ("TPP", "Target product profile describing desired product attributes and evidence needs."),
            ("IND", "Investigational new drug application allowing clinical investigation in humans in the United States."),
            ("NDA", "New drug application requesting approval to market a drug."),
            ("BLA", "Biologics license application requesting approval to market a biologic."),
            ("Accelerated approval", "Approval pathway using a surrogate or intermediate clinical endpoint reasonably likely to predict clinical benefit."),
            ("Complete response letter", "FDA communication that an application is not ready for approval in its current form."),
        ],
    ),
    (
        "Clinical trials and GCP",
        [
            ("Protocol", "Document describing study objectives, design, population, assessments, endpoints, safety, and analysis."),
            ("Randomization", "Assignment to treatment groups by chance to reduce bias."),
            ("Blinding", "Keeping treatment assignment unknown to reduce bias."),
            ("Control arm", "Comparator group used to interpret the effect of the investigational treatment."),
            ("Informed consent", "Process and documentation showing that participants understand key trial information before participation."),
            ("Protocol deviation", "Departure from the approved protocol or study procedures."),
            ("Risk-based monitoring", "Monitoring approach focused on critical risks to participant safety and data reliability."),
            ("Data integrity", "Completeness, consistency, accuracy, and reliability of data throughout the lifecycle."),
        ],
    ),
    (
        "Endpoints, statistics, and data interpretation",
        [
            ("Primary endpoint", "Main outcome measure used to evaluate the primary objective."),
            ("Secondary endpoint", "Additional outcome measure supporting other objectives."),
            ("Exploratory endpoint", "Outcome assessed to generate hypotheses or additional insight, usually not definitive."),
            ("Estimand", "Precise description of the treatment effect being estimated."),
            ("Intercurrent event", "Event after treatment initiation that affects interpretation or existence of measurements."),
            ("P-value", "Measure of compatibility between observed data and a null hypothesis under model assumptions."),
            ("Confidence interval", "Range reflecting uncertainty around an estimate."),
            ("Sensitivity analysis", "Analysis testing how robust results are to assumptions or data handling choices."),
        ],
    ),
    (
        "Safety and pharmacovigilance",
        [
            ("AE", "Adverse event; unfavorable medical occurrence after product use, regardless of causality."),
            ("SAE", "Serious adverse event meeting criteria such as death, life-threatening event, hospitalization, disability, or birth defect."),
            ("SUSAR", "Suspected unexpected serious adverse reaction."),
            ("MedDRA", "Medical Dictionary for Regulatory Activities used to code medical terms."),
            ("Case narrative", "Written summary of an individual safety case."),
            ("Signal detection", "Process for identifying information that may suggest a new or changed risk."),
            ("Risk-benefit", "Integrated assessment of benefits, risks, uncertainty, disease severity, and alternatives."),
            ("REMS", "Risk Evaluation and Mitigation Strategy used to manage serious known or potential risks when required."),
        ],
    ),
    (
        "CMC, CGMP, quality, and supply",
        [
            ("CMC", "Chemistry, manufacturing, and controls information supporting product quality."),
            ("API", "Active pharmaceutical ingredient."),
            ("Specification", "Quality standard a material or product must meet."),
            ("Batch record", "Documented record of manufacturing steps, controls, and results for a batch."),
            ("OOS", "Out of specification result requiring investigation."),
            ("Deviation", "Departure from approved procedure, process, specification, or expected result."),
            ("CAPA", "Corrective and preventive action addressing root cause and recurrence prevention."),
            ("Process validation", "Evidence that a manufacturing process consistently produces product meeting quality requirements."),
        ],
    ),
    (
        "Labeling, medical affairs, and promotion",
        [
            ("Prescribing information", "Approved product information describing indication, dosing, warnings, adverse reactions, and other use information."),
            ("Indication statement", "Approved language describing what the drug is approved to treat and in whom."),
            ("Fair balance", "Balanced communication of benefits and risks so the message is not misleading."),
            ("Off-label", "Use or discussion outside approved labeling."),
            ("MLR", "Medical, legal, and regulatory review of materials."),
            ("Promotional claim", "Product-related statement intended to promote use and requiring support and compliance review."),
            ("Scientific exchange", "Non-promotional scientific communication, usually handled within medical affairs boundaries."),
            ("Medical information", "Function that responds to medical inquiries with approved, balanced, evidence-based information."),
        ],
    ),
    (
        "Market access, RWE, and lifecycle",
        [
            ("HEOR", "Health economics and outcomes research."),
            ("Formulary", "List of medicines covered or preferred by a payer or health system."),
            ("Prior authorization", "Payer requirement for approval before coverage."),
            ("Step therapy", "Payer rule requiring use of one therapy before another."),
            ("RWD", "Real-world data routinely collected from health care or patient sources."),
            ("RWE", "Clinical evidence about usage, benefits, or risks derived from RWD analysis."),
            ("Biosimilar", "Biologic highly similar to a reference product with no clinically meaningful differences."),
            ("Lifecycle management", "Post-approval strategy for evidence, indications, formulations, access, safety, and competition."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. TPP Debate: Scientifically Interesting vs Clinically Meaningful",
        "setting": "A discovery team wants to advance a compound, but the development team is uncertain about the patient and evidence logic.",
        "dialogue": [
            ("Discovery lead", "The biomarker response is strong. We should move quickly."),
            ("Clinical development", "The biology is promising, but the clinical target is not clear yet."),
            ("ESL learner", "Before we commit to the next study, we need a sharper TPP: target population, expected clinical benefit, dose rationale, safety assumptions, comparator, endpoint, and differentiation from standard of care."),
            ("Discovery lead", "The mechanism is novel."),
            ("ESL learner", "Novel mechanism helps, but it does not replace evidence that patients, regulators, physicians, and payers will consider meaningful."),
        ],
        "notes": [
            "Scientific excitement should be connected to patient and development logic.",
            "TPP language keeps the team from confusing mechanism with product value.",
        ],
    },
    {
        "title": "2. IND Readiness: CMC Is Not Just a Detail",
        "setting": "A team wants to file an IND quickly, but CMC documentation is incomplete.",
        "dialogue": [
            ("Program lead", "Clinical is ready. Let's file the IND next month."),
            ("CMC lead", "The stability package and analytical validation are not complete."),
            ("ESL learner", "An IND is not only a protocol. We need enough nonclinical, clinical, and CMC information to support safe human dosing and product quality. If CMC is incomplete, the clinical timeline may not be credible."),
            ("Program lead", "Can we explain that the data are coming?"),
            ("ESL learner", "We can propose a plan, but we should not present future work as current readiness. Let's identify the minimum data needed and the regulatory risk of filing early."),
        ],
        "notes": [
            "Regulatory readiness must include quality and manufacturing evidence.",
            "Use 'minimum data needed' and 'regulatory risk' instead of blame.",
        ],
    },
    {
        "title": "3. Endpoint Debate: Convenient vs Clinically Relevant",
        "setting": "The team is choosing a primary endpoint for a Phase 2 trial.",
        "dialogue": [
            ("Clinical operations", "The biomarker endpoint is easier to measure and faster."),
            ("Medical lead", "But it may not persuade physicians."),
            ("ESL learner", "We should separate operational convenience from clinical relevance. If the biomarker is the primary endpoint, we need a strong rationale that it predicts patient benefit or supports the development decision."),
            ("Statistician", "The study is not powered for the clinical endpoint."),
            ("ESL learner", "Then we should be explicit: the study may be decision-enabling for dose and signal, but not definitive for clinical benefit."),
        ],
        "notes": [
            "Endpoint language should name what the study can and cannot prove.",
            "Operationally convenient endpoints may still need clinical justification.",
        ],
    },
    {
        "title": "4. Enrollment Rescue: Protocol Burden and Site Reality",
        "setting": "Enrollment is behind plan and the team is considering more sites.",
        "dialogue": [
            ("Clinical operations", "We are 40 percent behind enrollment. We should activate more sites."),
            ("Site manager", "The current sites say the visit schedule is too burdensome."),
            ("ESL learner", "More sites may help, but only if the protocol is feasible. We should examine screen failure reasons, visit burden, competing trials, eligibility criteria, and patient travel before adding cost."),
            ("Program lead", "We need speed."),
            ("ESL learner", "Agreed, but speed without feasibility will only create more underperforming sites. Let's propose a rescue plan with root cause, amendment options, and site-support actions."),
        ],
        "notes": [
            "Enrollment rescue should start with root cause, not only site count.",
            "Protocol burden language helps connect operations to data quality.",
        ],
    },
    {
        "title": "5. Safety Signal: Possible Liver Risk",
        "setting": "Several liver enzyme elevations have appeared across studies.",
        "dialogue": [
            ("Safety physician", "We have a cluster of ALT elevations."),
            ("Clinical lead", "Are they related to the drug?"),
            ("ESL learner", "We should not jump to causality, but we also should not minimize it. Let's review timing, dose relationship, dechallenge, rechallenge, baseline risk factors, concomitant medications, seriousness, and whether the pattern changes the risk-benefit assessment."),
            ("Regulatory affairs", "Do we need to notify FDA?"),
            ("ESL learner", "Let's assess seriousness, expectedness, reasonable possibility, and reporting timelines against the protocol, regulations, and safety SOPs."),
        ],
        "notes": [
            "Safety language should be calm, structured, and urgent where needed.",
            "Avoid both premature causality and premature reassurance.",
        ],
    },
    {
        "title": "6. Data Readout: Statistically Significant but Modest Effect",
        "setting": "A Phase 3 trial met the primary endpoint, but the effect size is small and safety events increased.",
        "dialogue": [
            ("Executive", "The p-value is positive. Can we call this a major breakthrough?"),
            ("Biostatistician", "The effect is statistically significant, but the confidence interval is narrow around a modest benefit."),
            ("ESL learner", "We can say the primary endpoint was met, but we should not overstate clinical impact. The communication needs effect size, clinical relevance, safety profile, population, and comparison to current options."),
            ("Commercial", "But we need a strong launch message."),
            ("ESL learner", "A strong message must still be supportable. Overclaiming now may create regulatory, credibility, and MLR risk later."),
        ],
        "notes": [
            "Positive data still need clinical and safety context.",
            "Commercial excitement must stay inside evidence boundaries.",
        ],
    },
    {
        "title": "7. Quality Deviation: Batch Release Pressure",
        "setting": "A batch is needed for launch supply, but an OOS result is under investigation.",
        "dialogue": [
            ("Supply lead", "If we do not release this batch, launch inventory is at risk."),
            ("Quality", "The OOS investigation is not closed."),
            ("ESL learner", "Supply pressure does not remove the need for quality disposition. We need documented root cause, impact assessment, and QA approval before release. If the batch cannot be released, we should communicate supply risk and mitigation options."),
            ("Supply lead", "Can we release with a memo?"),
            ("ESL learner", "Only if the quality system supports that conclusion. The decision must be evidence-based, documented, and approved through the proper process."),
        ],
        "notes": [
            "Quality decisions must not be framed as paperwork obstacles.",
            "Use documentation and process language rather than personal disagreement.",
        ],
    },
    {
        "title": "8. Promotional Claim Review: Subgroup Data",
        "setting": "Marketing wants to use a subgroup result in launch materials.",
        "dialogue": [
            ("Marketing", "The subgroup response looks impressive. Can we make it the headline?"),
            ("Medical reviewer", "It was exploratory and not powered."),
            ("ESL learner", "The subgroup may be scientifically interesting, but as a promotional headline it could be misleading. We need to check whether the claim is consistent with approved labeling, adequately supported, and presented with appropriate context and risk information."),
            ("Marketing", "Can we say 'especially effective' in that subgroup?"),
            ("ESL learner", "Not unless that claim is supported and approved. We can discuss a balanced, label-consistent statement or keep the subgroup in scientific exchange if appropriate."),
        ],
        "notes": [
            "MLR language should distinguish evidence interest from promotional support.",
            "A true statement can still be misleading without context.",
        ],
    },
    {
        "title": "9. MSL Boundary: Unsolicited Off-Label Question",
        "setting": "A physician asks an MSL about an off-label use during a scientific exchange.",
        "dialogue": [
            ("Physician", "Have you seen data for use in younger patients?"),
            ("MSL", "That is outside the approved indication."),
            ("ESL learner", "I can respond to your unsolicited scientific question with available data, but I need to be clear that this use is not approved. I cannot recommend off-label use, and I can provide medical information resources if you would like a formal response."),
            ("Physician", "So you have data?"),
            ("ESL learner", "I can discuss the study design and limitations in a balanced way, including what is known, what is not known, and how it differs from the approved population."),
        ],
        "notes": [
            "Boundary language should be clear without shutting down legitimate scientific exchange.",
            "Balance and context matter in medical affairs conversations.",
        ],
    },
    {
        "title": "10. Payer Evidence: Value Story Is Not the Same as Label",
        "setting": "Market access is preparing for payer discussions after approval.",
        "dialogue": [
            ("Market access", "Payers will ask why this deserves preferred formulary status."),
            ("HEOR", "We have clinical data but limited real-world outcomes."),
            ("ESL learner", "The payer value story should connect eligible population, clinical benefit, safety, budget impact, comparator, adherence, and unmet need. We should not imply outcomes we have not measured."),
            ("Commercial", "Can we say it reduces hospitalizations?"),
            ("ESL learner", "Only if the evidence supports that claim for the relevant population and context. Otherwise, we can frame it as a hypothesis or evidence-generation need."),
        ],
        "notes": [
            "Market access language must separate approved label, evidence, and economic hypothesis.",
            "Payer communication should avoid unsupported outcomes claims.",
        ],
    },
    {
        "title": "11. Biosimilar Discussion: Similar Is Not Identical",
        "setting": "A cross-functional team is preparing educational material on a biosimilar.",
        "dialogue": [
            ("Commercial", "Can we say it is the same as the reference product?"),
            ("Regulatory affairs", "Biosimilar language is more specific than that."),
            ("ESL learner", "We should say highly similar with no clinically meaningful differences in safety, purity, and potency, consistent with the approved biosimilar framework. 'Same' may oversimplify and create confusion."),
            ("Medical affairs", "What about interchangeability?"),
            ("ESL learner", "Interchangeability has a specific regulatory meaning. We should use it only if the product has that designation and the material explains it accurately."),
        ],
        "notes": [
            "Biosimilar language needs regulatory precision.",
            "Avoid simplifying technical terms into misleading equivalence.",
        ],
    },
    {
        "title": "12. Launch Readiness: Approval Is Not Enough",
        "setting": "The team is two months from expected approval and launch readiness is uneven.",
        "dialogue": [
            ("General manager", "If approval comes on time, we launch immediately."),
            ("Launch lead", "Supply, MLR materials, medical training, payer coverage, and PV intake process still have open risks."),
            ("ESL learner", "Approval is necessary but not sufficient for launch. We need a readiness view across label, supply, quality release, safety reporting, medical information, field training, access, and promotional materials."),
            ("General manager", "What is the critical path?"),
            ("ESL learner", "Supply release, final label-dependent MLR approval, safety intake readiness, and payer communication are the main dependencies. I recommend a weekly risk review until launch decision."),
        ],
        "notes": [
            "Launch readiness requires cross-functional dependency language.",
            "Approval timing should not hide supply, safety, or compliance readiness risk.",
        ],
    },
]


PHRASE_BANK = {
    "Development strategy and evidence": [
        "What decision does this evidence support?",
        "The mechanism is promising, but the clinical value proposition is not yet clear.",
        "We should connect the endpoint to patient benefit, regulatory acceptability, and payer relevance.",
        "The TPP needs to specify population, comparator, dosing, safety assumptions, and differentiation.",
    ],
    "Regulatory and clinical operations": [
        "I would not describe this as agency agreement; it is regulatory feedback with remaining sponsor risk.",
        "The protocol may be scientifically rich but operationally burdensome.",
        "Before adding sites, we should understand screen failures, visit burden, and competing trials.",
        "This deviation needs impact assessment for participant safety, rights, and data integrity.",
    ],
    "Data interpretation": [
        "Statistical significance does not automatically mean clinical relevance.",
        "The subgroup is hypothesis-generating unless the analysis was pre-specified and adequately powered.",
        "The estimand clarifies what treatment effect we are actually estimating.",
        "We should present effect size, confidence interval, population, safety, and limitations together.",
    ],
    "Safety and pharmacovigilance": [
        "We should not jump to causality, but we also should not minimize the pattern.",
        "Let's assess seriousness, expectedness, relatedness, and reporting timeline.",
        "A signal means further evaluation is needed; it is not automatically a confirmed risk.",
        "The risk-benefit update should include severity, alternatives, reversibility, and mitigation.",
    ],
    "Quality and manufacturing": [
        "Supply pressure does not remove quality disposition requirements.",
        "The batch decision must be evidence-based, documented, and approved through the quality system.",
        "We need root cause, containment, CAPA, and recurrence prevention.",
        "The manufacturing change requires comparability evidence before we treat it as low risk.",
    ],
    "Medical, promotional, and access boundaries": [
        "The claim may be scientifically interesting but not promotional-ready.",
        "We need to confirm consistency with approved labeling and fair balance.",
        "I can answer an unsolicited scientific question, but I cannot recommend off-label use.",
        "The payer message should separate demonstrated outcomes from economic hypotheses.",
    ],
}


WORKBOOK_TASKS = [
    "A discovery team wants to advance a compound based on biomarker response. Write five TPP clarification questions and a short evidence-logic memo.",
    "A program lead wants to file an IND before CMC documentation is complete. Write a readiness-risk explanation that is firm but collaborative.",
    "A protocol has many exploratory assessments and restrictive eligibility criteria. Write a feasibility critique with patient, site, and data-quality implications.",
    "A Phase 3 readout is statistically significant but clinically modest. Write a data-readout summary that avoids overclaiming.",
    "Several liver enzyme elevations appear across studies. Write a safety triage note that avoids premature causality and premature reassurance.",
    "A batch needed for launch has an unresolved OOS investigation. Write a quality and supply update with next steps.",
    "Marketing wants to headline an exploratory subgroup result. Write MLR review comments and a safer alternative message.",
    "A launch team assumes approval means immediate launch. Write a launch readiness update identifying cross-functional dependencies and decision criteria.",
]


SOURCES = [
    "FDA drug development and approval resources, including IND, NDA, and BLA pathway language.",
    "ICH E8(R1) and ICH E6(R3) guidance for clinical-study quality, GCP, participant protection, data reliability, and risk-proportionate trial conduct.",
    "ICH E9(R1) estimands and sensitivity-analysis guidance for endpoint, intercurrent-event, and treatment-effect language.",
    "FDA current good manufacturing practice resources for pharmaceutical quality, manufacturing controls, documentation, and quality-system language.",
    "FDA FAERS, MedWatch, IND safety reporting, and postmarketing adverse-event reporting resources for pharmacovigilance language.",
    "FDA OPDP and promotional labeling and advertising resources for claims, fair balance, promotional material submissions, and review language.",
    "FDA real-world evidence and biosimilar resources for RWD, RWE, reference product, biosimilar, and interchangeability language.",
    "The learner's own company SOPs, approved labeling, safety management plans, quality systems, regulatory correspondence, MLR process, and legal or compliance guidance.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in pharmaceutical environments: clinical development, clinical operations, regulatory affairs, pharmacovigilance, medical affairs, quality, CMC, manufacturing, biostatistics, data management, market access, commercial compliance, and pharma-adjacent leadership roles."
        )
    )
    story.append(
        p(
            "The course is not a drug-development certification and does not replace company SOPs, regulatory counsel, medical review, quality systems, or approved labeling. It trains professional English for pharma work: clarifying evidence standards, discussing risk, protecting patient safety, challenging overclaims, and coordinating cross-functional decisions."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "Pharma teams compress high-stakes judgment into short phrases: TPP, IND, NDA, BLA, endpoint, estimand, GCP, protocol deviation, SAE, SUSAR, MedDRA, signal, risk-benefit, CMC, CGMP, OOS, CAPA, stability, labeling, fair balance, off-label, MLR, HEOR, RWE, biosimilar, and launch readiness. Learners need the terms and the dialogue habits around them: define the evidence, name the uncertainty, protect patient safety, document the decision, and stay inside approved claims."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_pharma_communication_principles(story: list) -> None:
    story += h1("Pharmaceutical Communication Principles")
    story.append(h2("Separate evidence, interpretation, and claim"))
    story.append(
        p(
            "Pharma conversations become risky when teams blur what the data show, what the team believes, what regulators may accept, what the label allows, and what commercial teams want to say. Strong pharma English keeps those layers separate."
        )
    )
    story.append(h2("Use caution without paralysis"))
    story.append(
        bullets(
            [
                "Use 'supports' rather than 'proves' when evidence is directional or limited.",
                "Use 'consistent with the approved label' when reviewing external claims.",
                "Use 'further evaluation is needed' when discussing a possible safety signal.",
                "Use 'quality disposition' when supply pressure meets batch-release uncertainty.",
                "Use 'decision-enabling, not definitive' when a study can guide development but not establish final benefit.",
            ]
        )
    )
    story.append(h2("Turn vague pharma requests into evidence questions"))
    story.append(
        table(
            [
                ["Vague request", "Stronger pharmaceutical question"],
                ["Can we move faster?", "Which evidence package is incomplete, what risk does it create, and who owns the decision?"],
                ["The data are positive.", "Positive for which endpoint, population, estimand, effect size, safety profile, and clinical context?"],
                ["Can marketing use this result?", "Is the claim label-consistent, supported, balanced, and approved through MLR?"],
                ["Can we release the batch?", "What does the quality investigation show, and has QA approved disposition?"],
            ],
            [2.1 * 72, 4.9 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a realistic sentence, ask which regulation, protocol, SOP, label, quality record, or evidence standard applies, and explain the consequence for patients, data, product quality, or compliance."
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
                    "When learners give an overconfident answer, ask: what is the evidence source, what is the patient or quality risk, what document controls the decision, what uncertainty remains, who owns approval, and whether the language stays inside the label, protocol, SOP, or regulatory boundary?"
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
                "Learner explains their pharma role in 90 seconds, including therapeutic area, functional partners, regulatory or quality boundaries, common documents, and highest-risk conversations.",
                "Learner defines twelve pharma terms and uses six in realistic workplace sentences.",
                "Learner handles a short role-play: a senior leader wants to move faster despite incomplete evidence and compliance risk.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but uses them loosely.", "Uses pharma terms accurately in context.", "Defines terms, cites controlling document, and explains patient, data, quality, or compliance implication."],
                ["Evidence discipline", "Treats positive data as a broad claim.", "Separates result, interpretation, limitation, and claim.", "Prevents overclaiming while preserving useful scientific meaning."],
                ["Risk communication", "Sounds either alarmist or dismissive.", "Names safety, quality, regulatory, or operational risk clearly.", "Gives calm, documented next steps under pressure."],
                ["Cross-functional judgment", "Accepts one function's timeline or preference.", "Balances clinical, regulatory, safety, quality, access, and commercial constraints.", "Guides the team toward a decision-ready tradeoff."],
                ["Compliance boundaries", "Misses label, GCP, CGMP, PV, or promotional limits.", "Flags boundaries and refers to SOPs or review processes.", "Uses precise, credible language that protects patients, product quality, and company trust."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a cross-functional program review. The product has promising biomarker data, CMC readiness gaps, a burdensome Phase 2 protocol, a possible liver-safety signal, an exploratory subgroup result commercial wants to use, launch-supply risk, payer evidence gaps, and a leadership demand for speed. The learner must clarify evidence, define risk, protect compliance, and write a decision-ready program update."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "Pharmaceutical English",
        "Instructor guide for high-level ESL learners working in clinical development, regulatory affairs, pharmacovigilance, quality, CMC, medical affairs, market access, and pharma-adjacent roles",
        "Audience: instructors, pharmaceutical English coaches, corporate learning teams, medical affairs trainers, clinical operations trainers, and advanced professional English programs",
    )
    add_course_opening(story)
    add_pharma_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-pharmaceutical-english-instructor-guide.pdf",
        "EFSP Pharmaceutical English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Pharmaceutical English",
        "Participant workbook: drug development, clinical trials, GCP, safety, CMC, CGMP, labeling, medical affairs, promotion, access, RWE, and launch dialogue practice",
        "Audience: advanced ESL learners working in pharmaceutical development, regulatory, clinical operations, pharmacovigilance, quality, CMC, medical affairs, market access, and related roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you sound precise, careful, and useful in pharmaceutical conversations. The goal is not to memorize acronyms. The goal is to connect evidence, patient safety, product quality, regulatory expectations, and business decisions without overclaiming."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which pharma conversations are hardest for you: protocol review, regulatory meetings, safety triage, CMC updates, MLR review, launch readiness, payer evidence, or cross-functional escalation?",
                "Which acronyms do you understand when reading but avoid when speaking?",
                "When a senior leader asks for speed or a stronger claim, do you become too agreeable, too technical, too indirect, or too blunt?",
                "What is one recent pharma meeting you wish you had handled more clearly?",
            ]
        )
    )
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("Pharmaceutical Workstream Language")
    story.append(
        table(
            [
                ["Area", "Useful verbs", "Example sentence"],
                ["Development", "define, differentiate, justify, sequence, de-risk", "The TPP should clarify the population, endpoint, comparator, and evidence standard."],
                ["Regulatory", "submit, align, respond, justify, document", "The agency feedback reduces uncertainty, but it does not guarantee approval."],
                ["Clinical", "randomize, monitor, enroll, amend, analyze", "The protocol may need amendment if eligibility criteria are driving screen failures."],
                ["Safety", "triage, assess, code, report, mitigate", "The pattern requires evaluation, but we should not assume causality yet."],
                ["Quality", "investigate, validate, release, contain, prevent", "The batch cannot be released until quality disposition is approved."],
                ["Medical and access", "review, substantiate, contextualize, respond, educate", "The claim must be label-consistent, balanced, and supported by evidence."],
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
        "efsp-pharmaceutical-english-participant-workbook.pdf",
        "EFSP Pharmaceutical English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "Pharmaceutical Dialogue Lab",
        "Realistic pharmaceutical-workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners",
        "Audience: instructors, pharmaceutical English coaches, clinical teams, regulatory teams, medical affairs teams, quality teams, market access teams, and peer practice cohorts",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: pharma professional, cross-functional stakeholder, observer.",
                "Read the model dialogue once. Then replay it with a different therapeutic area, evidence package, timeline pressure, regulatory region, safety pattern, or launch constraint.",
                "The observer listens for evidence discipline, patient-safety language, quality or compliance boundaries, document control, uncertainty clarity, and decision-ready next steps.",
                "After each role-play, replay the hardest 30 seconds with a more precise pharma sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners hide behind acronyms. Ask them to define the evidence, controlling document, patient or product-quality risk, compliance boundary, owner, and decision needed."
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
                    "Did the learner separate data, interpretation, claim, and decision?",
                    "Did the learner name patient safety, data integrity, product quality, or compliance risk?",
                    "Did the learner use the relevant document boundary: protocol, label, SOP, quality record, or regulatory feedback?",
                    "Did the learner give a concrete next step without overpromising?",
                ]
            )
        )
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-pharmaceutical-dialogue-lab.pdf",
        "EFSP Pharmaceutical Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "Pharmaceutical Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise pharmaceutical vocabulary and cross-functional meeting language",
        "Audience: advanced ESL learners in clinical development, clinical operations, regulatory affairs, pharmacovigilance, quality, CMC, manufacturing, medical affairs, market access, commercial compliance, and related roles",
    )
    story += h1("How to Use Pharmaceutical Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it clarifies evidence, patient safety, product quality, compliance, timeline, or decision ownership.",
                "Pair acronyms with plain English when speaking to cross-functional partners.",
                "Ask which document controls the answer: protocol, SAP, label, SOP, regulatory correspondence, quality record, or approved material.",
                "Avoid overclaiming efficacy, minimizing safety, bypassing quality disposition, or turning scientific exchange into promotion.",
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
                ["Adverse event vs adverse reaction", "AE occurs after product use; adverse reaction implies reasonable possibility of causal relationship."],
                ["Serious vs severe", "Serious is regulatory outcome-based; severe describes intensity."],
                ["Endpoint vs estimand", "Endpoint is what is measured; estimand defines the treatment effect being estimated."],
                ["Statistical significance vs clinical relevance", "Statistical result may be reliable but still modest or not meaningful for patients."],
                ["Signal vs confirmed risk", "Signal suggests further evaluation; confirmed risk is supported by stronger evidence."],
                ["Deviation vs CAPA", "Deviation is what went wrong; CAPA addresses root cause and recurrence prevention."],
                ["Scientific exchange vs promotion", "Scientific exchange is balanced and non-promotional; promotion encourages product use within approved boundaries."],
                ["RWD vs RWE", "RWD is the data source; RWE is clinical evidence derived from analysis of that data."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-pharmaceutical-jargon-quick-reference.pdf",
        "EFSP Pharmaceutical Jargon Field Guide",
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
