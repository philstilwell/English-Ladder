from __future__ import annotations

import argparse
import html
from pathlib import Path

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, Spacer

from generate_efsp_guarded_activities import (
    add_answer_key,
    add_cloze_exercise,
    make_dialogue_cloze,
    make_module_cloze,
    term_learning_fields,
)
from generate_efsp_culture_pdfs import (
    CONTENT_WIDTH,
    S,
    box,
    build_pdf,
    bullets,
    h1,
    h2,
    h3,
    p,
    table,
)


ROOT = Path(__file__).resolve().parent


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def m(
    title: str,
    skill: str,
    scenario: str,
    pressure: str,
    constraint: str,
    output: str,
    terms: list[str],
    speakers: tuple[str, str],
) -> dict:
    return {
        "title": title,
        "skill": skill,
        "scenario": scenario,
        "pressure": pressure,
        "constraint": constraint,
        "output": output,
        "terms": terms,
        "speakers": speakers,
    }


def profile(
    title: str,
    slug: str,
    roles: str,
    summary: str,
    modules: list[dict],
    sources: list[str],
    term_definitions: dict[str, str] | None = None,
    collocations: list[tuple[str, str]] | None = None,
    dialogues: list[dict] | None = None,
    nomenclature: list[tuple[str, str, str]] | None = None,
) -> dict:
    return {
        "title": title,
        "slug": slug,
        "roles": roles,
        "summary": summary,
        "modules": modules,
        "sources": sources,
        "term_definitions": term_definitions or {},
        "collocations": collocations or [],
        "dialogues": dialogues or [],
        "nomenclature": nomenclature or [],
    }


TERM_DEFINITIONS = {
    "accreditation": "External recognition that an organization meets defined quality, safety, or professional standards.",
    "adverse event": "An unfavorable event or outcome that must be documented, reviewed, and escalated according to policy.",
    "API": "Application programming interface; a defined way for software systems to exchange data or trigger actions.",
    "ARR": "Annual recurring revenue; subscription revenue normalized to a yearly amount.",
    "audit trail": "A record showing who changed what, when, and often why.",
    "backlog": "Ordered body of work waiting to be refined, prioritized, assigned, or completed.",
    "benchmark": "A comparison point used to judge performance, cost, quality, risk, or maturity.",
    "budget variance": "Difference between planned and actual financial performance.",
    "business case": "Structured argument for action, usually including problem, options, cost, benefit, risk, and recommendation.",
    "CAPA": "Corrective and preventive action used to address root cause and reduce recurrence.",
    "capacity": "Available people, assets, time, space, or system throughput for a given workload.",
    "change control": "Formal process for reviewing, approving, implementing, and documenting changes.",
    "churn": "Loss of customers, revenue, employees, donors, users, or accounts over a period of time.",
    "claim": "A statement that may need evidence, approval, qualification, or disclosure before it is used externally.",
    "client intake": "Structured process for gathering facts, goals, constraints, risks, and scope at the start of work.",
    "compliance": "Conformance with laws, regulations, standards, policies, contracts, or approved procedures.",
    "control": "A process, approval, check, or technical safeguard designed to reduce risk.",
    "corrective action": "Action taken to fix a current problem and prevent recurrence.",
    "credentialing": "Verification that a professional has the required license, training, background, or authority for a role.",
    "critical path": "Sequence of dependent work that determines the shortest feasible timeline.",
    "dashboard": "Visual summary of selected measures used to monitor status, performance, or risk.",
    "data lineage": "Traceable path of data from source through transformation to final use.",
    "defect": "Failure, flaw, nonconformance, or error that prevents an output from meeting requirements.",
    "dependency": "Work, approval, input, vendor, system, or decision that another activity relies on.",
    "disclosure": "Required communication of facts, risks, conflicts, limitations, or terms.",
    "documentation": "Written evidence of what was done, why, by whom, when, and under which authority.",
    "due diligence": "Structured review of facts, risks, financials, operations, obligations, or claims before a decision.",
    "escalation": "Raising an issue to a higher authority or different function because risk, urgency, or decision rights require it.",
    "evidence standard": "Level and type of support required before a decision, claim, approval, or recommendation is appropriate.",
    "forecast": "Forward-looking estimate based on assumptions, trends, constraints, and known risks.",
    "governance": "Decision structure defining roles, rights, approvals, controls, and accountability.",
    "handoff": "Transfer of work, responsibility, information, or risk from one person or team to another.",
    "HIPAA": "US health privacy framework governing protected health information in covered health contexts.",
    "incident": "Unplanned event that disrupts service, safety, quality, security, operations, or expected performance.",
    "KPI": "Key performance indicator used to monitor progress against an important objective.",
    "materiality": "Importance threshold at which a fact, risk, error, or change could affect a decision.",
    "mitigation": "Action taken to reduce likelihood, impact, or exposure of a risk.",
    "nonconformance": "Failure to meet a requirement, specification, contract, standard, or approved procedure.",
    "operating model": "How work is organized across people, process, technology, governance, and metrics.",
    "owner": "Named person or role accountable for a decision, action, deliverable, or risk.",
    "policy": "Formal rule or standard that guides decisions and behavior.",
    "postmortem": "Structured review after an incident or project to identify causes, impacts, lessons, and actions.",
    "prioritization": "Deliberate ordering of work based on value, urgency, risk, capacity, and dependencies.",
    "quality assurance": "Process discipline used to confirm work meets requirements and standards.",
    "quality control": "Inspection, testing, or review used to detect whether an output meets requirements.",
    "root cause": "Underlying reason a problem occurred, not merely the visible symptom.",
    "runbook": "Documented operational procedure for repeatable tasks or incident response.",
    "scope": "Defined boundary of work, responsibility, deliverables, assumptions, and exclusions.",
    "SLA": "Service-level agreement defining expected service performance or response commitments.",
    "SOP": "Standard operating procedure describing approved steps for recurring work.",
    "stakeholder": "Person or group with an interest, risk, authority, or dependency in the work.",
    "throughput": "Amount of work, patients, goods, cases, or transactions completed in a period of time.",
    "triage": "Sorting issues by urgency, severity, risk, owner, and next action.",
    "variance": "Difference between actual and expected performance, cost, timing, quality, or volume.",
    "workflow": "Sequence of steps, roles, handoffs, systems, and decisions used to complete work.",
}

TERM_DEFINITIONS.update(
    {
        "5 Whys": "Root-cause method that repeatedly asks why a problem occurred until the team reaches a controllable underlying cause.",
        "510(k)": "US FDA premarket submission that typically demonstrates substantial equivalence to a legally marketed predicate device.",
        "8D": "Eight-discipline problem-solving report used to contain a problem, identify root cause, implement corrective action, and prevent recurrence.",
        "A/B test": "Controlled comparison of two variants to estimate the effect of a change on a defined outcome.",
        "ACH": "US electronic bank-transfer network used for direct deposits, bill payments, and account-to-account transfers.",
        "AML": "Anti-money laundering controls used to detect, investigate, and report suspicious financial activity.",
        "airworthiness": "Condition in which an aircraft conforms to approved design and is safe for operation under applicable rules.",
        "assay": "Laboratory procedure used to measure the presence, amount, activity, or quality of a biological target.",
        "attack surface": "Set of systems, interfaces, identities, and entry points an attacker could attempt to exploit.",
        "authorization": "Required approval from a payer, regulator, manager, or system before a service, transaction, or action can proceed.",
        "beneficial owner": "Natural person who ultimately owns or controls an entity or receives its economic benefit.",
        "biomarker": "Measurable biological characteristic used to indicate a condition, response, exposure, or disease-related process.",
        "clean claim": "Insurance claim submitted with the required data and documentation so it can be processed without avoidable delay or rejection.",
        "clinical deterioration": "Worsening patient condition that requires prompt reassessment, communication, and possible escalation of care.",
        "CMC": "Chemistry, manufacturing, and controls information that shows how a drug substance or product is made and consistently controlled.",
        "coding": "Assignment of standardized diagnostic, procedure, or service codes used for records, billing, reporting, or reimbursement.",
        "constructability": "Extent to which a design can be built safely, efficiently, and reliably using available methods, materials, and sequencing.",
        "critical dimension": "Measured feature size that must remain within specification for a product, component, or semiconductor device to perform as intended.",
        "CVE": "Common Vulnerabilities and Exposures identifier used to reference a publicly known cybersecurity vulnerability.",
        "CVSS": "Common Vulnerability Scoring System, a standardized method for expressing the severity and characteristics of a vulnerability.",
        "data subject request": "Request from an individual to access, correct, delete, restrict, or otherwise exercise rights over personal data.",
        "denial": "Decision by an insurer, payer, regulator, or authority not to approve, pay, or grant a requested item or claim.",
        "design intent": "Functional, aesthetic, performance, and user objectives the design must preserve as details are developed.",
        "due diligence": "Structured review of facts, risks, obligations, and evidence before a transaction, onboarding, investment, or decision.",
        "eligibility": "Rules that determine whether a person, account, provider, service, or request qualifies for a program, benefit, or action.",
        "FMEA": "Failure mode and effects analysis, a structured method for identifying how a process or product can fail and prioritizing controls.",
        "freedom to operate": "Assessment of whether a product or activity can proceed without infringing another party's enforceable intellectual-property rights.",
        "HCAHPS": "US standardized patient-experience survey used by hospitals for public reporting and quality improvement.",
        "identity verification": "Process of confirming that a requester is the person or authorized representative entitled to act or receive information.",
        "in vitro": "Performed outside a living organism, typically in a laboratory vessel, cell system, or controlled assay.",
        "in vivo": "Performed in a living organism, such as an animal or human study participant.",
        "KYC": "Know-your-customer process used to verify a customer's identity, ownership, and risk profile.",
        "lot traceability": "Ability to follow a production lot through materials, process steps, tools, inspections, and downstream customers or products.",
        "MEL": "Minimum equipment list identifying aircraft equipment that may be inoperative under specified conditions while the aircraft remains dispatchable.",
        "minimum necessary": "HIPAA principle requiring use or disclosure of only the minimum protected health information needed for the purpose.",
        "no-show": "Scheduled patient, customer, or guest who does not arrive or cancel in time for the appointment or reservation to be reused.",
        "non-retaliation": "Requirement that people are not punished or disadvantaged for making a good-faith report, complaint, or participation in an investigation.",
        "patient stratification": "Grouping patients by characteristics that may affect disease course, treatment response, safety, or trial analysis.",
        "process window": "Range of operating conditions within which a process produces acceptable results with adequate performance margin.",
        "protected health information": "Individually identifiable health information protected by HIPAA when held or transmitted by covered entities or business associates.",
        "rapid response": "Clinical team activated to assess and stabilize a patient showing signs of acute deterioration before a full emergency event.",
        "readmission": "Return of a patient to a hospital or facility within a defined period after discharge, often tracked as an outcome measure.",
        "referral": "Order, recommendation, or routing process that directs a patient or case to another clinician, service, or specialist.",
        "RFI": "Request for information used to resolve an ambiguity, conflict, or missing detail in contract documents or a project scope.",
        "SBAR": "Situation, background, assessment, recommendation; a structured format for concise clinical communication and escalation.",
        "sensitivity": "Ability of a test, model, or process to correctly identify true positives or detect a change in an input.",
        "specificity": "Ability of a test, model, or process to correctly identify true negatives and avoid false positives.",
        "surrogate endpoint": "Measure expected to predict clinical benefit but not itself a direct measure of how a patient feels, functions, or survives.",
        "tech transfer": "Controlled transfer of product, process, method, or manufacturing knowledge between teams, sites, or organizations.",
        "translatability": "Likelihood that a finding in one model, setting, or population will predict results in the intended real-world or clinical setting.",
        "underwriting": "Evaluation of risk and terms used to decide whether and on what conditions to issue insurance, extend credit, or accept an investment exposure.",
        "vital signs": "Core clinical measurements such as temperature, pulse, respiratory rate, blood pressure, and oxygen saturation used to assess patient status.",
        "wire transfer": "Electronic movement of funds between financial institutions, usually with irreversible settlement characteristics once released.",
    }
)


SEMICONDUCTOR_TERM_DEFINITIONS = {
    "binning": "Sorting tested semiconductor units into performance, power, speed, or quality categories.",
    "burn-in": "Stress testing used to screen for early-life failures before product release or shipment.",
    "capacity allocation": "Decision process for assigning limited foundry, tool, test, or assembly capacity across products or customers.",
    "cleanroom": "Controlled manufacturing environment designed to limit particles, humidity, electrostatic risk, and contamination.",
    "CMP": "Chemical mechanical planarization; a process that smooths wafer surfaces for later manufacturing steps.",
    "contamination control": "Practices used to prevent particles, residues, metals, organics, moisture, or handling errors from affecting wafers or devices.",
    "critical dimension": "A measured feature size on a wafer that must stay within specification for device performance and yield.",
    "defect density": "Number or rate of defects on a wafer, die, layer, lot, or process area.",
    "deposition": "Process of adding material layers to a wafer by physical, chemical, epitaxial, or atomic-layer methods.",
    "die": "Individual semiconductor device cut from a processed wafer.",
    "ESD": "Electrostatic discharge; sudden electrical discharge that can damage sensitive semiconductor devices.",
    "etch": "Process that removes selected material from a wafer using wet chemistry or plasma-based methods.",
    "excursion": "Manufacturing event or trend outside expected control limits, specifications, or normal process behavior.",
    "fab": "Semiconductor fabrication facility where wafers are processed through manufacturing steps.",
    "foundry": "Semiconductor manufacturer that fabricates chips for external customers or design companies.",
    "lithography": "Patterning process that transfers circuit features to a wafer using light, masks, and photoresist.",
    "metrology": "Measurement discipline used to verify process, dimension, film, defect, and device characteristics.",
    "node": "Technology generation or process family, often associated with feature size, performance, density, and design rules.",
    "package": "Protective and electrical interface that connects a semiconductor die to a board or system.",
    "particle": "Small contaminant that can create defects, yield loss, reliability risk, or process instability.",
    "PDK": "Process design kit; foundry-provided design rules, models, and files used to design chips for a process.",
    "photoresist": "Light-sensitive material used in lithography to define patterns on a wafer.",
    "preventive maintenance": "Planned equipment service performed to reduce unplanned downtime, drift, contamination, safety risk, or tool instability.",
    "process flow": "Ordered sequence of semiconductor manufacturing steps, layers, inspections, holds, and decision points.",
    "process window": "Range of process conditions under which results meet specification with acceptable margin.",
    "qualification": "Evidence-based approval that a process, product, tool, package, supplier, or change meets defined requirements.",
    "recipe": "Controlled equipment parameters used to run a process step on a wafer, lot, or tool.",
    "reticle": "Photomask used in lithography to project circuit patterns onto a wafer.",
    "SPC": "Statistical process control; use of control charts and limits to monitor process stability.",
    "tape-out": "Final release of a chip design to the foundry for mask generation and fabrication.",
    "tool matching": "Effort to make similar manufacturing tools produce equivalent results within defined limits.",
    "tool uptime": "Percentage of time equipment is available and qualified for production use.",
    "wafer": "Thin semiconductor substrate, usually silicon, on which integrated circuits are fabricated.",
    "yield": "Share of wafers, die, units, or lots that meet requirements after manufacturing, test, or qualification.",
}


SEMICONDUCTOR_COLLOCATIONS = [
    ("put a lot on hold", "Stop a wafer lot from moving until the hold reason, owner, risk, and release condition are clear."),
    ("release a lot", "Allow a held lot to continue only after route, disposition, and risk acceptance have been documented."),
    ("open an excursion", "Start a formal investigation when SPC, defect, yield, or tool behavior moves outside expected limits."),
    ("contain affected lots", "Identify, quarantine, or restrict lots that may share the same exposure, tool path, material, or time window."),
    ("verify lot genealogy", "Trace where a lot has been, which tools touched it, and which lots share possible exposure."),
    ("quarantine suspect material", "Physically or systemically prevent wafers, chemicals, parts, or finished units from being used or shipped."),
    ("review SPC charts", "Look at control charts, rules, limits, and trends before deciding whether a signal is real."),
    ("separate signal from noise", "Avoid reacting to a single data point until sampling, repeatability, and tool history are checked."),
    ("tighten the process window", "Reduce allowed process variation when yield, reliability, or margin is at risk."),
    ("run split lots", "Process comparable lots or wafers under different conditions to isolate a variable or compare paths."),
    ("qualify a recipe", "Generate evidence that a controlled tool recipe meets process, quality, and reliability requirements."),
    ("match a tool", "Show that two tools produce equivalent results within approved limits for a given process step."),
    ("move lots to the matched tool", "Transfer work to an alternate tool only within the approved matching, recipe, and product constraints."),
    ("pull in preventive maintenance", "Move planned maintenance earlier to reduce drift, contamination, safety, or downtime risk."),
    ("recover tool uptime", "Restore qualified equipment availability without bypassing restart, monitor, or qualification requirements."),
    ("check chamber history", "Review recent maintenance, cleans, alarms, consumables, recipes, and abnormal events for a process chamber."),
    ("confirm metrology repeatability", "Repeat or cross-check measurements before treating a trend as a process problem."),
    ("hold shipment", "Prevent finished units from leaving until quality, reliability, customer, or compliance questions are resolved."),
    ("screen for early-life failure", "Use burn-in, stress, or test screening to identify infant mortality risk before release."),
    ("bin devices by speed and power", "Sort parts into usable categories after test, often tied to customer specifications or price."),
    ("perform failure analysis", "Investigate failed die, packages, or returned units to identify physical, electrical, process, or use-related causes."),
    ("close the 8D", "Complete the structured customer problem-solving report with verified root cause and effective corrective action."),
    ("freeze the mask set", "Stop design changes so masks, reticles, wafer starts, and downstream schedules can proceed."),
    ("release the PDK", "Publish foundry design rules, models, and files for a process after readiness checks are complete."),
    ("lock the tape-out package", "Finalize the files, checks, signoffs, and assumptions needed for mask generation."),
    ("allocate wafer starts", "Assign constrained foundry capacity or fab starts across products, customers, or priorities."),
    ("approve a deviation", "Permit a controlled exception only after impact, owner, duration, and risk acceptance are documented."),
    ("issue a customer quality notice", "Give customers a factual update about risk, containment, impact, and next action without speculation."),
]


SEMICONDUCTOR_DIALOGUES = [
    {
        "title": "Lot Hold vs Customer Expedite",
        "setting": "A strategic customer is waiting for units, but a wafer lot is on hold after an inline monitor showed abnormal film thickness.",
        "turns": [
            ("Customer program manager", "Can we release the lot today? The customer is escalating and the ship date is already tight."),
            ("Process integration engineer", "I understand the schedule pressure, but the hold code is tied to a film-thickness excursion after deposition."),
            ("Customer program manager", "Is it a real excursion or just a metrology artifact?"),
            ("Process integration engineer", "That is exactly what we need to confirm. I want repeat metrology, chamber history, and lot genealogy before release."),
            ("Customer program manager", "What is the fastest responsible option?"),
            ("Process integration engineer", "We can contain the affected lots, run a split on one lower-risk lot, and prepare a deviation request if quality agrees."),
            ("Customer program manager", "So I should not promise shipment today."),
            ("Process integration engineer", "Right. Say the lot is under controlled disposition, with an update after repeat measurement and quality review."),
        ],
        "coach_notes": [
            "The learner does not say no; the learner names hold code, excursion, metrology, genealogy, containment, and disposition.",
            "The response gives the commercial team usable customer language without pretending the risk is solved.",
        ],
        "collocations": ["put a lot on hold", "confirm metrology repeatability", "verify lot genealogy", "approve a deviation"],
    },
    {
        "title": "Critical Dimension Drift on a Customer Call",
        "setting": "A customer quality lead challenges whether a CD trend is real before a corrective action report is due.",
        "turns": [
            ("Customer quality lead", "Your report shows CD drift, but we think the trend could be measurement noise."),
            ("Lithography engineer", "That is a fair question. We are checking metrology repeatability before we call it a process shift."),
            ("Customer quality lead", "What are you comparing?"),
            ("Lithography engineer", "The same layer across the last three lots, the reference wafer, reticle history, exposure dose, focus data, and CD-SEM repeat runs."),
            ("Customer quality lead", "Can you state whether product performance is affected?"),
            ("Lithography engineer", "Not yet. We can say the drift is within electrical guardband so far, but we are not closing the excursion until SPC and yield correlation are complete."),
            ("Customer quality lead", "When will we have a decision?"),
            ("Lithography engineer", "By 5 p.m. tomorrow, we will provide either a release recommendation or a containment plan with affected-lot IDs."),
        ],
        "coach_notes": [
            "The learner distinguishes measurement repeatability, process shift, electrical impact, and customer disposition.",
            "The dialogue trains a precise but cautious answer: what is known, what is being checked, and when the decision comes.",
        ],
        "collocations": ["review SPC charts", "confirm metrology repeatability", "separate signal from noise", "contain affected lots"],
    },
    {
        "title": "Particle Excursion After Maintenance",
        "setting": "Production wants to restart a tool after maintenance, but defect maps show a new particle signature.",
        "turns": [
            ("Production planner", "The tool is back up. Can we load the backlog now?"),
            ("Manufacturing quality engineer", "Not until we close the restart checks. The monitor wafer shows a particle signature that was not present before maintenance."),
            ("Production planner", "If we wait, the area will miss the shift target."),
            ("Manufacturing quality engineer", "I understand. The tradeoff is that restarting too early could contaminate multiple high-value lots."),
            ("Production planner", "What do you need before release?"),
            ("Manufacturing quality engineer", "A clean monitor run, chamber history, maintenance notes, and a lot list for any material exposed during the suspect window."),
            ("Production planner", "Can we at least run engineering material?"),
            ("Manufacturing quality engineer", "Possibly, if the module owner approves the route and quality agrees that the risk is contained."),
        ],
        "coach_notes": [
            "The learner uses contamination-control language without blaming the maintenance team.",
            "The practical move is to define the restart condition, not simply defend quality in general terms.",
        ],
        "collocations": ["quarantine suspect material", "check chamber history", "contain affected lots", "recover tool uptime"],
    },
    {
        "title": "Tool Matching Under Capacity Pressure",
        "setting": "A bottleneck tool is down, and operations wants to move production to an alternate tool that is almost matched.",
        "turns": [
            ("Operations director", "We need to move all lots to Tool B. The matched-tool report looked close enough."),
            ("Module process owner", "Tool B is close for monitor wafers, but product-lot data are still limited for this layer."),
            ("Operations director", "How much risk are we really talking about?"),
            ("Module process owner", "The main risks are uniformity, selectivity, and downstream CMP margin. If those shift, yield loss may appear several steps later."),
            ("Operations director", "What is your recommendation?"),
            ("Module process owner", "Move low-risk lots first, run enhanced metrology, and keep critical customer lots on hold until the first product split clears."),
            ("Operations director", "Give me language for the morning standup."),
            ("Module process owner", "Say Tool B is under controlled qualification, not fully released for unrestricted product movement."),
        ],
        "coach_notes": [
            "The learner explains why almost matched is not the same as unrestricted production release.",
            "The line 'under controlled qualification' gives leaders a concise phrase for operations updates.",
        ],
        "collocations": ["match a tool", "move lots to the matched tool", "run split lots", "qualify a recipe"],
    },
    {
        "title": "Reliability Qualification vs Early Shipment",
        "setting": "A business unit wants to ship early units after electrical test, before reliability stress is complete.",
        "turns": [
            ("Business unit manager", "Electrical test passed. Can we ship early samples while reliability finishes?"),
            ("Product engineer", "We can discuss sample release, but electrical pass is not the same as reliability qualification."),
            ("Business unit manager", "The customer only needs a few units for bring-up."),
            ("Product engineer", "Then we should label them clearly as engineering samples, define use limits, and avoid treating them as qualified product."),
            ("Business unit manager", "What is the unresolved risk?"),
            ("Product engineer", "Package interaction, burn-in results, early-life failure rate, and bin stability are still open."),
            ("Business unit manager", "What can I tell sales?"),
            ("Product engineer", "Tell them sample release may be possible with restrictions, but production shipment waits for qualification review."),
        ],
        "coach_notes": [
            "The learner separates sample release, production shipment, electrical test, and reliability qualification.",
            "This is useful for sales and business conversations where 'passed test' is often overextended.",
        ],
        "collocations": ["screen for early-life failure", "bin devices by speed and power", "hold shipment", "perform failure analysis"],
    },
    {
        "title": "Foundry Capacity and Tape-Out Commitment",
        "setting": "A customer asks for a guaranteed tape-out and wafer-start date while PDK updates and foundry capacity are still moving.",
        "turns": [
            ("Customer program manager", "We need a firm wafer-start date before our executive review. Can you guarantee the slot?"),
            ("Foundry coordinator", "I can confirm the current allocation request, but I cannot guarantee the slot until the tape-out package and change freeze are complete."),
            ("Customer program manager", "What is blocking the commitment?"),
            ("Foundry coordinator", "PDK version signoff, mask data checks, final DRC closure, and capacity allocation approval."),
            ("Customer program manager", "That sounds like too many caveats."),
            ("Foundry coordinator", "The caveats are the conditions for a reliable commitment. If any of them move, the wafer-start date can move with them."),
            ("Customer program manager", "What should our executive slide say?"),
            ("Foundry coordinator", "Say the target slot is requested, with commitment pending PDK signoff, mask package lock, and foundry allocation confirmation."),
        ],
        "coach_notes": [
            "The learner protects the relationship by giving a usable target while refusing a false guarantee.",
            "The dialogue models conditional commitment language common in foundry and customer-program work.",
        ],
        "collocations": ["freeze the mask set", "release the PDK", "lock the tape-out package", "allocate wafer starts"],
    },
]


SEMICONDUCTOR_NOMENCLATURE = [
    ("Fab logistics", "FOUP", "Front opening unified pod used to transport and protect wafers in automated fab environments."),
    ("Fab logistics", "lot traveler", "Record or system route showing where the lot goes, what has been done, and what instructions apply."),
    ("Fab logistics", "hold code", "System code that explains why material is blocked from movement or shipment."),
    ("Fab logistics", "WIP", "Work in process; material currently moving through manufacturing, test, assembly, or disposition."),
    ("Fab logistics", "queue time", "Time a lot waits between process steps; excessive queue time can affect quality or cycle time."),
    ("Fab logistics", "lot genealogy", "Traceable history of tools, materials, routes, rework, holds, and related lots."),
    ("Process control", "control wafer", "Wafer used to monitor process or tool behavior without risking production material."),
    ("Process control", "split lot", "Lot divided or compared across conditions to test a process variable or disposition path."),
    ("Process control", "golden tool", "Reference tool whose performance is treated as the comparison point for matching."),
    ("Process control", "chamber matching", "Effort to align performance across chambers in the same or similar equipment."),
    ("Process control", "inline monitor", "Measurement taken during manufacturing to catch drift before final test or yield loss."),
    ("Process control", "PCM", "Process control monitor structures or measurements used to evaluate process health."),
    ("Lithography", "overlay", "Alignment accuracy between patterned layers on the wafer."),
    ("Lithography", "dose", "Exposure energy applied during lithography."),
    ("Lithography", "focus", "Exposure focus condition that affects printed feature quality."),
    ("Lithography", "OPC", "Optical proximity correction used to adjust mask patterns for printing behavior."),
    ("Lithography", "CD-SEM", "Critical-dimension scanning electron microscope used to measure small patterned features."),
    ("Lithography", "scatterometry", "Optical metrology method used to infer feature profiles, dimensions, or film characteristics."),
    ("Films and etch", "film thickness", "Measured thickness of a deposited or grown layer."),
    ("Films and etch", "sheet resistance", "Electrical resistance measurement used to monitor thin films or implants."),
    ("Films and etch", "selectivity", "How much faster one material is removed than another during etch or CMP."),
    ("Films and etch", "uniformity", "Degree to which a process result is consistent across wafer, lot, tool, or chamber."),
    ("Films and etch", "end-point detection", "Method for determining when an etch or process step has reached the target condition."),
    ("Films and etch", "slurry", "Abrasive chemical mixture used in CMP."),
    ("Films and etch", "post-CMP clean", "Cleaning step used to remove residue, particles, or contamination after CMP."),
    ("Test and sort", "wafer sort", "Electrical testing of die while still on the wafer."),
    ("Test and sort", "die sort", "Classification of die after wafer-level testing."),
    ("Test and sort", "probe card", "Test interface that contacts wafer pads during wafer sort."),
    ("Test and sort", "parametric test", "Electrical measurement of device or process parameters, often used to monitor margins."),
    ("Test and sort", "guardband", "Extra margin used to reduce risk when specification, process, or use conditions vary."),
    ("Reliability", "infant mortality", "Early-life failures that appear soon after device use or stress."),
    ("Reliability", "FIT rate", "Failures in time; reliability measure often expressed as failures per billion device hours."),
    ("Reliability", "electromigration", "Reliability failure mechanism caused by metal movement under current stress."),
    ("Reliability", "TDDB", "Time-dependent dielectric breakdown; reliability mechanism affecting insulating layers."),
    ("Reliability", "HCI", "Hot carrier injection; reliability mechanism that can degrade transistor performance."),
    ("Reliability", "NBTI", "Negative-bias temperature instability; reliability mechanism affecting transistor threshold behavior."),
    ("Packaging", "wire bond", "Electrical connection made by bonding fine wires between die and package leads or substrate."),
    ("Packaging", "flip chip", "Package approach where die are connected face-down through bumps."),
    ("Packaging", "underfill", "Material placed under flip-chip die to improve mechanical reliability."),
    ("Packaging", "bump", "Conductive connection point used in advanced packages or wafer-level packaging."),
    ("Packaging", "TSV", "Through-silicon via used to connect vertically through silicon in advanced packages."),
    ("Packaging", "substrate", "Package platform that supports the die and routes signals to the board."),
    ("Quality and customer", "MRB", "Material review board that decides disposition for nonconforming or suspect material."),
    ("Quality and customer", "deviation", "Approved exception from a normal requirement, route, specification, or process condition."),
    ("Quality and customer", "rework", "Additional approved processing intended to bring material back into requirement."),
    ("Quality and customer", "scrap", "Disposition for material that cannot be used or recovered acceptably."),
    ("Quality and customer", "FA", "Failure analysis; structured investigation of why a device, die, package, or system failed."),
    ("Quality and customer", "decapsulation", "Removal of package material to inspect die, bonds, or physical evidence during FA."),
]


INDUSTRIES = [
    profile(
        "Healthcare Administration English",
        "healthcare-administration",
        "hospital administrators, clinic managers, practice administrators, care coordinators, patient-experience leaders, revenue-cycle staff, operations managers, and healthcare-adjacent professionals",
        "A challenging professional English curriculum for healthcare administration teams who need precise language for access, patient flow, revenue cycle, quality, compliance, staffing, service recovery, care coordination, and executive reporting.",
        [
            m("Patient Access, Scheduling, and Referrals", "Turn access problems into measurable workflow and patient-impact questions.", "A clinic is losing referrals because patients wait too long for first appointments.", "Open more appointment slots immediately.", "Provider capacity, eligibility checks, referral completeness, and no-show risk are unclear.", "access improvement memo", ["referral", "eligibility", "authorization", "no-show"], ("Practice director", "Scheduling lead")),
            m("Revenue Cycle, Coding, and Denials", "Discuss payment operations without blaming front-desk, clinical, or billing teams.", "Denials have increased after a payer policy change.", "Tell billing to fix the claims faster.", "The root cause may involve documentation, coding, authorization, or payer rules.", "denial root-cause brief", ["claim", "coding", "denial", "clean claim"], ("Revenue-cycle manager", "Clinic manager")),
            m("Patient Flow, Capacity, and Staffing", "Explain bottlenecks using census, throughput, acuity, and staffing language.", "Emergency department boarding is delaying inpatient admissions.", "Move patients upstairs faster.", "Bed availability, discharge timing, acuity, transport, and nursing coverage all interact.", "capacity escalation update", ["census", "bed management", "throughput", "staffing ratio"], ("Hospital operations lead", "Nurse manager")),
            m("Quality, Safety, and Accreditation", "Use safety language that is factual, nonpunitive, and escalation-ready.", "A wrong-patient near miss occurred during registration.", "Treat it as a training issue and move on.", "Patient safety, process reliability, and documentation require a structured review.", "quality event summary", ["near miss", "accreditation", "audit trail", "corrective action"], ("Quality director", "Registration supervisor")),
            m("HIPAA, Privacy, and Information Governance", "Set privacy boundaries without sounding obstructive.", "A manager wants patient lists emailed to a vendor for outreach.", "Send the spreadsheet today.", "Minimum necessary use, vendor agreements, and secure transmission must be confirmed.", "privacy-safe vendor response", ["HIPAA", "protected health information", "minimum necessary", "business associate"], ("Operations manager", "Privacy officer")),
            m("Patient Experience and Service Recovery", "Handle complaints with empathy, facts, and process accountability.", "A family complains about poor communication during discharge.", "Apologize and promise it will never happen again.", "The organization needs empathy, review, realistic commitment, and documented follow-up.", "service recovery script", ["grievance", "service recovery", "HCAHPS", "patient experience"], ("Patient-experience lead", "Unit manager")),
            m("Population Health and Care Coordination", "Explain care gaps, readmission risk, and coordination without overpromising outcomes.", "A payer flags high readmissions for heart-failure patients.", "Call every patient and tell them to comply.", "Social needs, discharge instructions, medication access, and follow-up timing affect outcomes.", "care coordination plan", ["care gap", "readmission", "discharge planning", "social determinants"], ("Population health lead", "Care coordinator")),
            m("Executive Dashboards and Board Updates", "Translate operational data into concise executive risk and decision language.", "The board asks why wait times improved but patient satisfaction fell.", "Show more charts.", "Metrics need interpretation, tradeoffs, assumptions, and action owners.", "board-ready operations update", ["dashboard", "KPI", "variance", "owner"], ("Chief operating officer", "Service-line manager")),
        ],
        ["Current CMS and payer guidance for reimbursement language.", "HIPAA and organizational privacy policies.", "Accreditation standards and local quality-safety procedures."],
    ),
    profile(
        "Nursing and Allied Health English",
        "nursing-allied-health",
        "nurses, charge nurses, physical therapists, occupational therapists, respiratory therapists, imaging staff, laboratory staff, care-team coordinators, and allied-health supervisors",
        "A clinical workplace English curriculum for nursing and allied health learners who need handoff, escalation, patient education, documentation, interprofessional communication, safety-event, discharge, and conflict language.",
        [
            m("Shift Handoffs and Clinical Prioritization", "Use structured handoff language under time pressure.", "A night nurse hands off a patient with changing vitals and incomplete labs.", "Keep the report short and skip details.", "The receiving clinician needs severity, trend, pending actions, and contingency triggers.", "SBAR handoff script", ["SBAR", "acuity", "pending lab", "watcher"], ("Charge nurse", "Incoming nurse")),
            m("Patient Assessment and Escalation", "Escalate deterioration clearly without sounding panicked or vague.", "A patient is becoming short of breath after surgery.", "Wait for the next scheduled assessment.", "Respiratory status, vital-sign trends, and escalation criteria require immediate communication.", "clinical escalation call", ["vital signs", "rapid response", "clinical deterioration", "escalation"], ("Bedside nurse", "Resident physician")),
            m("Medication Safety and Allergy Clarification", "Ask precise medication questions and challenge unsafe orders.", "A medication order conflicts with a documented allergy.", "Administer it because the physician ordered it.", "Patient safety requires clarification, documentation, and closed-loop communication.", "medication clarification note", ["allergy", "contraindication", "MAR", "closed-loop communication"], ("Staff nurse", "Pharmacist")),
            m("Patient Education and Teach-Back", "Explain care instructions in plain English and verify understanding.", "A patient nods during discharge teaching but cannot describe the plan.", "Just print the instructions.", "Teach-back is needed to confirm understanding and reduce avoidable return visits.", "teach-back dialogue", ["teach-back", "discharge instructions", "health literacy", "adherence"], ("Discharge nurse", "Patient")),
            m("Interprofessional Rounds", "Participate assertively when physicians, therapists, and case managers disagree.", "The team is debating whether the patient is safe to go home.", "Let the physician decide without allied-health input.", "Mobility, oxygen needs, home support, and follow-up resources affect safety.", "rounds contribution", ["plan of care", "functional status", "case management", "safe discharge"], ("Physical therapist", "Hospitalist")),
            m("Documentation and Charting", "Write objective notes that support continuity and risk management.", "A supervisor says a note sounds emotional and unclear.", "Write exactly what you felt happened.", "Clinical documentation should describe observations, interventions, response, and notification.", "objective charting rewrite", ["charting", "objective finding", "intervention", "patient response"], ("Clinical supervisor", "Staff clinician")),
            m("Difficult Families and Boundaries", "Respond to upset families with empathy and role clarity.", "A family demands test results before the provider has reviewed them.", "Give them whatever information is available.", "Scope, privacy, clinical authority, and emotional support all matter.", "family communication script", ["scope of practice", "privacy", "family meeting", "boundary"], ("Charge nurse", "Family member")),
            m("Safety Events and Just Culture", "Discuss mistakes without hiding facts or assigning premature blame.", "A fall occurred after a missed bed alarm.", "Name the person responsible immediately.", "A just-culture review should separate human error, system weakness, and reckless behavior.", "safety-event debrief", ["fall risk", "incident report", "just culture", "root cause"], ("Unit manager", "Risk manager")),
        ],
        ["Facility clinical policies and scope-of-practice rules.", "Patient safety and incident reporting procedures.", "Professional standards for nursing and allied-health documentation."],
    ),
    profile(
        "Biotechnology English",
        "biotechnology",
        "biotech scientists, translational researchers, assay-development teams, platform teams, program managers, alliance managers, business-development staff, and biotech executives",
        "A high-level biotechnology English curriculum for platform science, assay design, translational evidence, biomarkers, IP, partnerships, investor updates, regulatory-adjacent planning, and scientific-business dialogue.",
        [
            m("Platform Technology and Scientific Thesis", "Explain platform promise without overstating translation to products.", "A founder wants to describe the platform as broadly validated.", "Use the strongest possible investor language.", "The evidence supports specific models and indications, not every future use case.", "platform evidence statement", ["platform", "modality", "proof of concept", "translatability"], ("Founder", "Scientific lead")),
            m("Assay Development and Reproducibility", "Discuss assay performance, variability, and limitations.", "A partner asks whether a biomarker assay is ready for decision-making.", "Say the assay works because the pilot was positive.", "Precision, sensitivity, specificity, controls, and reproducibility need review.", "assay readiness note", ["assay", "sensitivity", "specificity", "reproducibility"], ("Alliance manager", "Assay scientist")),
            m("Biomarkers and Translational Strategy", "Connect preclinical signals to patient selection and clinical hypotheses.", "A team wants to use a biomarker as the main development rationale.", "Make the biomarker the centerpiece of the clinical story.", "Biological plausibility, patient relevance, and validation status are different.", "biomarker caveat memo", ["biomarker", "patient stratification", "surrogate endpoint", "validation"], ("Translational lead", "Clinical advisor")),
            m("Preclinical Data Packages", "Describe animal, in vitro, and tox findings with appropriate caution.", "A board member asks whether animal data prove human efficacy.", "Say the model predicts human response.", "Model relevance, dose, exposure, safety margin, and limitations must be named.", "preclinical evidence summary", ["in vitro", "in vivo", "toxicity", "safety margin"], ("Board member", "Preclinical scientist")),
            m("CMC and Scale-Up in Biotech", "Explain manufacturing feasibility before process maturity is complete.", "A program lead wants to promise rapid scale-up after financing.", "Assure investors that scale-up will be simple.", "Yield, process control, comparability, and supply-chain risk are unresolved.", "scale-up risk update", ["CMC", "yield", "comparability", "tech transfer"], ("Program lead", "Process development lead")),
            m("IP, Freedom to Operate, and Collaboration", "Use careful language around patents and partner boundaries.", "A collaborator requests broad access to unpublished methods.", "Share the materials to keep the relationship warm.", "Confidentiality, background IP, publication rights, and freedom to operate matter.", "collaboration boundary response", ["IP", "freedom to operate", "material transfer agreement", "publication rights"], ("Alliance manager", "External scientist")),
            m("Investor and Board Updates", "Translate science into milestone, runway, risk, and decision language.", "The board wants a clean milestone story before a financing round.", "Remove uncertainties from the update.", "Credibility requires clear milestones, risks, assumptions, and mitigation.", "investor-ready milestone update", ["milestone", "runway", "inflection point", "risk mitigation"], ("CEO", "Program manager")),
            m("Partnering and Business Development", "Discuss deal value without losing scientific caveats.", "A potential partner wants exclusive rights after limited data review.", "Agree quickly before they lose interest.", "Diligence, territory, field, economics, governance, and data rights need definition.", "partnering negotiation brief", ["term sheet", "option", "exclusivity", "due diligence"], ("Business-development lead", "Scientific founder")),
        ],
        ["Company scientific records and approved investor materials.", "Patent counsel and confidentiality agreements.", "Current regulatory and quality guidance relevant to the product type."],
    ),
    profile(
        "Medical Devices English",
        "medical-devices",
        "medical device engineers, product managers, quality and regulatory staff, clinical specialists, manufacturing teams, field-service teams, and device-company leaders",
        "A device-focused professional English curriculum for design controls, risk management, usability, verification and validation, regulatory pathways, complaint handling, quality systems, manufacturing, and clinical-user dialogue.",
        [
            m("User Needs and Design Inputs", "Translate user pain points into controlled requirements.", "A surgeon requests a feature after a product demo.", "Add it to the roadmap as requested.", "User need, design input, intended use, and risk must be separated.", "design-input clarification", ["user need", "design input", "intended use", "traceability"], ("Product manager", "Design engineer")),
            m("Risk Management and Hazard Analysis", "Discuss hazards, harms, mitigations, and residual risk.", "A team calls a rare use error acceptable.", "Document that the risk is low and move on.", "Severity, probability, detectability, and mitigation evidence need review.", "risk-control rationale", ["hazard", "harm", "FMEA", "residual risk"], ("Quality engineer", "R&D lead")),
            m("Verification, Validation, and Design Review", "Distinguish building the product right from building the right product.", "Leadership asks whether testing is finished.", "Say yes because verification passed.", "Validation, usability, clinical workflow, and traceability may still be open.", "V&V readiness update", ["verification", "validation", "design review", "acceptance criteria"], ("Regulatory lead", "Engineering manager")),
            m("Usability and Human Factors", "Explain use errors without blaming users.", "A nurse repeatedly selects the wrong mode during formative testing.", "Call it a training problem.", "Interface design, labeling, workflow, and risk controls need assessment.", "human-factors finding", ["human factors", "use error", "formative study", "summative study"], ("Human-factors lead", "Clinical specialist")),
            m("Regulatory Pathways and Submissions", "Use pathway language without promising clearance or approval.", "Sales wants to say clearance is guaranteed because predicates exist.", "Tell customers clearance is straightforward.", "Predicate comparison, indications, performance data, and agency review remain uncertain.", "regulatory pathway caveat", ["510(k)", "De Novo", "PMA", "predicate device"], ("Regulatory affairs", "Sales director")),
            m("Complaints, MDRs, and Postmarket Signals", "Triage field reports with safety and regulatory discipline.", "A field rep hears about a device malfunction during a case.", "Handle it informally with the hospital.", "Complaint intake, adverse-event assessment, and reporting timelines may apply.", "complaint intake summary", ["complaint", "MDR", "malfunction", "postmarket surveillance"], ("Field clinical specialist", "Complaint handler")),
            m("Manufacturing, Suppliers, and Nonconformance", "Communicate product-quality problems without hiding supply risk.", "A supplier change caused dimensional variation.", "Use the parts to avoid backorder.", "Nonconformance, disposition, supplier CAPA, and process validation must be resolved.", "supplier quality update", ["nonconformance", "supplier CAPA", "process validation", "lot traceability"], ("Supply-chain lead", "Quality manager")),
            m("Clinical Training and Labeling Boundaries", "Train users while staying inside cleared indications and instructions.", "A key opinion leader asks about an off-label technique.", "Demonstrate the technique to build enthusiasm.", "Labeling, intended use, clinical evidence, and compliance boundaries control the response.", "label-safe training response", ["labeling", "instructions for use", "off-label", "clinical evidence"], ("Clinical trainer", "Surgeon")),
        ],
        ["Current FDA medical device and quality-system resources.", "Company design-control, complaint, and regulatory procedures.", "Approved labeling and instructions for use."],
    ),
    profile(
        "Manufacturing English",
        "manufacturing",
        "plant managers, production supervisors, quality engineers, maintenance teams, industrial engineers, safety leads, supply planners, and manufacturing-adjacent professionals",
        "A manufacturing English curriculum for production meetings, line problems, lean improvement, defects, maintenance, safety, supplier quality, shift handoffs, and root-cause communication.",
        [
            m("Production Flow and Daily Management", "Report line status with throughput, downtime, and constraint language.", "A line misses target for the third shift in a row.", "Ask operators to work faster.", "The constraint may be material availability, changeover time, staffing, or equipment reliability.", "daily production update", ["throughput", "cycle time", "constraint", "downtime"], ("Plant manager", "Production supervisor")),
            m("Lean, Waste, and Continuous Improvement", "Discuss waste reduction without blaming people.", "A kaizen event identifies excess movement and waiting.", "Tell employees to be more efficient.", "Process design, layout, standard work, and visual management need review.", "lean improvement proposal", ["kaizen", "standard work", "waste", "value stream"], ("Continuous-improvement lead", "Cell supervisor")),
            m("Defects, Scrap, and Rework", "Explain defect trends and containment actions clearly.", "Scrap has increased after a tooling change.", "Ship the acceptable units and watch the trend.", "Containment, defect mode, inspection plan, and customer impact must be defined.", "defect containment brief", ["defect", "scrap", "rework", "containment"], ("Quality engineer", "Production lead")),
            m("Root Cause and Corrective Action", "Move from symptom language to evidence-based cause analysis.", "A customer returns parts for fit issues.", "Say the operator missed a step.", "Root cause must be supported by data, not assumed from the visible failure.", "8D problem statement", ["root cause", "5 Whys", "fishbone", "8D"], ("Customer quality manager", "Manufacturing engineer")),
            m("Maintenance, Reliability, and Changeover", "Discuss equipment risk and maintenance tradeoffs.", "A critical machine keeps failing during peak demand.", "Delay maintenance until the order is complete.", "Unplanned downtime, safety risk, spare parts, and preventive maintenance need balancing.", "maintenance risk escalation", ["preventive maintenance", "MTBF", "changeover", "spare parts"], ("Maintenance manager", "Production planner")),
            m("EHS and Safety Communication", "Stop unsafe work with direct but professional language.", "A supervisor sees bypassed guarding during a rush order.", "Finish the run and fix the guard later.", "Safety controls, lockout/tagout, and incident risk override schedule pressure.", "safety stop-work script", ["EHS", "lockout/tagout", "near miss", "stop work"], ("EHS lead", "Shift supervisor")),
            m("Supplier Quality and Incoming Materials", "Communicate supplier problems with evidence and business impact.", "Incoming material fails inspection before a major build.", "Use it because the supplier says it is fine.", "Specification, deviation approval, alternate supply, and customer risk must be assessed.", "supplier deviation request", ["supplier quality", "incoming inspection", "specification", "deviation"], ("Supply planner", "Supplier quality engineer")),
            m("Shift Handoffs and Escalation", "Create clean shift-to-shift continuity.", "The night shift leaves an unresolved process alarm.", "Let day shift figure it out.", "Handoff needs status, actions taken, risk, owner, and escalation path.", "shift handoff note", ["handoff", "andon", "escalation", "owner"], ("Shift lead", "Incoming supervisor")),
        ],
        ["Company quality manuals and SOPs.", "OSHA or local safety requirements.", "Customer specifications and supplier quality agreements."],
    ),
    profile(
        "Supply Chain and Logistics English",
        "supply-chain-logistics",
        "supply-chain managers, planners, buyers, logistics coordinators, warehouse leaders, procurement teams, customs staff, and operations managers",
        "A supply-chain English curriculum for forecasting, shortages, purchasing, inventory, warehouse operations, logistics delays, supplier performance, customs, risk, and crisis communication.",
        [
            m("Demand Planning and Forecast Bias", "Discuss forecast changes without treating estimates as promises.", "Sales raises the forecast after a promotion begins.", "Increase production commitments immediately.", "Forecast bias, lead time, capacity, and inventory exposure need review.", "demand-planning exception note", ["forecast", "forecast bias", "demand signal", "S&OP"], ("Demand planner", "Sales manager")),
            m("Procurement and Supplier Performance", "Challenge supplier promises using evidence and contract language.", "A supplier misses delivery but promises recovery next week.", "Accept the promise and update the plan.", "Capacity, allocation, purchase order terms, and recovery evidence are unclear.", "supplier recovery plan", ["purchase order", "lead time", "OTIF", "allocation"], ("Buyer", "Supplier account manager")),
            m("Inventory, Safety Stock, and Service Levels", "Explain inventory tradeoffs between service and cash.", "Finance wants to reduce inventory across all SKUs.", "Cut safety stock by the same percentage.", "Demand variability, lead time, margin, service level, and stockout risk differ by item.", "inventory segmentation memo", ["safety stock", "stockout", "service level", "SKU"], ("Supply-chain analyst", "Finance partner")),
            m("Warehousing and Fulfillment", "Report warehouse constraints and fulfillment risk.", "Orders are late because pick accuracy is falling.", "Add overtime until backlog clears.", "Slotting, labor, scanner data, training, and error types need diagnosis.", "fulfillment recovery update", ["pick rate", "slotting", "cycle count", "backlog"], ("Warehouse manager", "Operations director")),
            m("Freight, Routing, and Carrier Delays", "Communicate transportation risk precisely.", "A carrier misses pickup before a major customer shipment.", "Blame the carrier and wait.", "Mode, route, cutoff time, expedite cost, and customer promise need a decision.", "freight escalation notice", ["incoterms", "carrier", "expedite", "ETA"], ("Logistics coordinator", "Customer service manager")),
            m("Customs, Trade Compliance, and Documentation", "Prevent shipment delays caused by incomplete documents.", "A shipment is held because the commercial invoice has inconsistent data.", "Ask customs to release it anyway.", "Classification, country of origin, valuation, and document consistency matter.", "customs hold response", ["HS code", "country of origin", "commercial invoice", "broker"], ("Trade compliance lead", "Freight forwarder")),
            m("Supply Risk and Business Continuity", "Discuss disruptions with contingency and prioritization language.", "A port strike threatens inbound components.", "Promise no customer impact.", "Allocation, alternate sources, inventory position, and customer priority need governance.", "supply risk brief", ["business continuity", "dual sourcing", "allocation", "constraint"], ("Supply-chain director", "Sales operations")),
            m("Executive S&OP Decisions", "Turn cross-functional disagreement into decisions and assumptions.", "Sales, finance, and operations disagree on next quarter's plan.", "Use the most optimistic demand view.", "The executive team must agree on assumptions, risk, upside, and owners.", "S&OP decision summary", ["S&OP", "consensus plan", "scenario", "owner"], ("Operations VP", "Demand planning lead")),
        ],
        ["Supplier contracts and purchase terms.", "Trade compliance procedures and customs documentation rules.", "Company S&OP, inventory, and logistics policies."],
    ),
    profile(
        "Human Resources English",
        "human-resources",
        "HR business partners, recruiters, talent managers, people managers, employee-relations staff, learning teams, compensation analysts, and HR-adjacent leaders",
        "A human-resources English curriculum for hiring, onboarding, performance feedback, employee relations, investigations, benefits, compensation, policy explanation, workplace conflict, and dignity-preserving directness.",
        [
            m("Recruiting, Screening, and Candidate Experience", "Discuss hiring criteria and fairness without vague culture-fit language.", "A hiring manager rejects candidates for not feeling like a fit.", "Use the manager's intuition.", "Selection criteria, interview evidence, bias risk, and documentation need clarity.", "candidate-debrief guide", ["job requirement", "structured interview", "bias", "candidate experience"], ("Recruiter", "Hiring manager")),
            m("Onboarding and Role Clarity", "Explain expectations, support, and early performance signals.", "A new employee is confused about ownership after two weeks.", "Tell them to be more proactive.", "Role scope, manager check-ins, training, and success measures may be unclear.", "onboarding reset plan", ["role clarity", "onboarding", "manager check-in", "success measure"], ("HR business partner", "Team manager")),
            m("Performance Feedback and Documentation", "Give direct feedback that is specific, fair, and useful.", "A manager wants to put an employee on a warning after months of vague concerns.", "Issue the warning immediately.", "The employee may not have received clear expectations, examples, or support.", "performance feedback script", ["performance gap", "documentation", "expectation", "support plan"], ("HRBP", "Department manager")),
            m("Employee Relations and Investigations", "Handle complaints with neutrality, confidentiality, and procedural care.", "An employee reports harassment by a high performer.", "Resolve it quietly because the accused is important.", "Investigation process, anti-retaliation, evidence, and confidentiality are critical.", "investigation intake summary", ["employee relations", "harassment", "retaliation", "confidentiality"], ("Employee-relations specialist", "Senior manager")),
            m("Compensation, Benefits, and Equity", "Explain pay and benefits decisions without making unauthorized promises.", "An employee says a peer is paid more for the same job.", "Promise an immediate adjustment.", "Pay bands, job leveling, equity review, budget, and communication process matter.", "compensation response", ["pay band", "job level", "equity review", "benefits"], ("Compensation analyst", "Employee")),
            m("Policy Communication and Compliance", "Explain policies in plain English while preserving flexibility where allowed.", "A manager wants to make an exception to leave policy.", "Approve it because the employee is valued.", "Consistency, accommodation, legal risk, and manager precedent need review.", "policy exception review", ["policy", "accommodation", "precedent", "compliance"], ("HR operations lead", "Line manager")),
            m("Conflict Mediation and Manager Coaching", "Coach managers to address conflict early and respectfully.", "Two team leads accuse each other of blocking work.", "Move one of them to another team.", "Shared expectations, facts, behavior, and operating agreements should be tested first.", "mediation opening script", ["mediation", "behavioral example", "operating agreement", "accountability"], ("HRBP", "Functional leader")),
            m("Restructuring and Sensitive Communication", "Use careful language for layoffs, reorganizations, and role changes.", "Leadership plans a reorg but wants managers to hint at it early.", "Give employees informal warnings.", "Timing, confidentiality, legal review, messaging, and dignity are essential.", "reorg communication checklist", ["restructuring", "position elimination", "severance", "talking points"], ("People leader", "Executive")),
        ],
        ["Company employee handbook and HR policies.", "Current employment-law guidance from counsel.", "EEOC and local workplace-rights resources where applicable."],
    ),
    profile(
        "Project Management English",
        "project-management",
        "project managers, program managers, PMO staff, scrum masters, delivery leads, operations managers, and cross-functional coordinators",
        "A project-management English curriculum for scope, schedule, risks, dependencies, stakeholder alignment, status reporting, change control, delivery governance, and difficult timeline conversations.",
        [
            m("Project Charter and Scope Definition", "Create shared boundaries before work accelerates.", "A sponsor asks the team to start before scope is agreed.", "Begin execution and define scope later.", "Objectives, deliverables, assumptions, exclusions, and decision rights need alignment.", "project charter excerpt", ["charter", "scope", "assumption", "exclusion"], ("Project sponsor", "Project manager")),
            m("Schedule, Critical Path, and Dependencies", "Explain timeline pressure without hiding dependency risk.", "A launch date is announced before vendor dates are confirmed.", "Tell teams to compress their tasks.", "Critical path, dependency owners, buffers, and decision dates are unresolved.", "schedule risk update", ["critical path", "dependency", "milestone", "buffer"], ("Program manager", "Vendor lead")),
            m("Risk Register and Issue Escalation", "Separate possible risks from current issues and decisions.", "A risk has become an active blocker.", "Keep it green until the next steering meeting.", "Severity, probability, impact, mitigation, and owner must be updated.", "risk-to-issue escalation", ["risk register", "issue log", "mitigation", "owner"], ("PMO lead", "Workstream owner")),
            m("Stakeholder Alignment and Governance", "Use governance language to prevent hidden disagreement.", "Two executives give conflicting direction to the team.", "Try to satisfy both quietly.", "Decision rights, tradeoffs, and escalation path need clarification.", "governance decision note", ["governance", "RACI", "decision rights", "steering committee"], ("Project manager", "Executive sponsor")),
            m("Change Requests and Scope Creep", "Push back on extra work without sounding unhelpful.", "A business lead asks for additional reporting in the same timeline.", "Add it because the request is small.", "Impact on scope, timeline, cost, quality, and dependencies must be assessed.", "change request response", ["change request", "scope creep", "impact analysis", "baseline"], ("Business lead", "Delivery manager")),
            m("Status Reporting and Executive Updates", "Turn project noise into crisp status and asks.", "The project has many small problems and leaders want a simple color status.", "Mark it yellow without details.", "Executives need trend, risks, decisions, and owner accountability.", "executive status update", ["status report", "RAG status", "trend", "decision ask"], ("PMO director", "Project manager")),
            m("Vendor and Cross-Functional Delivery", "Hold partners accountable while preserving working relationships.", "A vendor misses a deliverable and proposes a vague recovery plan.", "Accept the revised date.", "Deliverables, acceptance criteria, resourcing, and escalation terms need definition.", "vendor recovery plan", ["deliverable", "acceptance criteria", "SLA", "escalation"], ("Vendor manager", "Implementation partner")),
            m("Post-Implementation Review", "Discuss lessons learned without blame or theater.", "A project launches late and the sponsor wants a quick lessons-learned meeting.", "Focus only on what went well.", "Root causes, decisions, handoffs, and preventive actions need honest review.", "post-implementation review", ["postmortem", "lesson learned", "root cause", "action item"], ("Project sponsor", "Delivery lead")),
        ],
        ["PMO methodology and project governance standards.", "Contract and vendor delivery terms.", "Current organizational risk and change-control procedures."],
    ),
    profile(
        "Engineering English",
        "engineering",
        "mechanical, electrical, civil, systems, industrial, test, quality, manufacturing, and field engineers, plus engineering managers and technical project leads",
        "An engineering English curriculum for requirements, design reviews, tradeoffs, testing, failure analysis, quality, safety factors, manufacturability, field issues, and technical disagreement.",
        [
            m("Requirements and Constraints", "Clarify requirements before proposing technical solutions.", "A customer asks for a lighter design with no cost increase.", "Say engineering can make it work.", "Load, tolerance, material, manufacturability, regulatory, and cost constraints conflict.", "requirements clarification matrix", ["requirement", "constraint", "tolerance", "tradeoff"], ("Customer engineer", "Design engineer")),
            m("Design Reviews and Technical Pushback", "Challenge assumptions using evidence rather than status.", "A senior engineer prefers a design with limited test data.", "Accept the senior view.", "Design rationale, risk, analysis, and verification evidence should be reviewed.", "design-review comment set", ["design review", "design rationale", "risk", "verification"], ("Senior engineer", "Systems engineer")),
            m("Failure Modes and Reliability", "Explain failure risk, severity, and detection.", "A component failure appears only under certain vibration conditions.", "Treat it as an edge case.", "Operating envelope, duty cycle, failure mode, and reliability target matter.", "failure mode summary", ["failure mode", "FMEA", "reliability", "duty cycle"], ("Reliability engineer", "Product lead")),
            m("Testing, Validation, and Data Interpretation", "Discuss test results without overgeneralizing.", "A prototype passes one test but fails under thermal cycling.", "Claim the design is mostly validated.", "Test conditions, sample size, acceptance criteria, and failure analysis are incomplete.", "test-readiness update", ["prototype", "acceptance criteria", "validation", "sample size"], ("Test engineer", "Program manager")),
            m("Manufacturability and Cost Engineering", "Connect design decisions to production and cost reality.", "A design change improves performance but complicates assembly.", "Approve it because performance is better.", "Yield, tooling, cycle time, supplier capability, and cost must be balanced.", "DFM tradeoff note", ["DFM", "tooling", "yield", "cycle time"], ("Manufacturing engineer", "Design lead")),
            m("Safety Factors and Compliance", "Explain safety margin and regulatory implications clearly.", "Leadership wants to reduce material thickness to save cost.", "Reduce it if simulations pass.", "Safety factor, code requirements, test evidence, and liability exposure need review.", "safety margin escalation", ["safety factor", "code compliance", "margin", "liability"], ("Engineering manager", "Structural engineer")),
            m("Field Issues and Customer Communication", "Communicate technical problems to customers without speculation.", "A field failure affects a strategic account.", "Tell the customer the part was misused.", "Evidence, installation conditions, warranty terms, and corrective action are not complete.", "customer technical update", ["field failure", "warranty", "corrective action", "installation condition"], ("Field engineer", "Account manager")),
            m("Systems Integration and Interface Control", "Manage cross-disciplinary dependencies.", "A software change affects hardware timing.", "Ask teams to coordinate informally.", "Interfaces, timing assumptions, version control, and regression testing need governance.", "interface-control update", ["interface control", "integration", "regression test", "configuration management"], ("Systems engineer", "Software lead")),
        ],
        ["Engineering standards and applicable codes.", "Company design-control, test, and quality procedures.", "Customer specifications and contractual requirements."],
    ),
    profile(
        "Semiconductor English",
        "semiconductor",
        "semiconductor process engineers, yield engineers, product engineers, equipment engineers, fab supervisors, quality teams, test and packaging teams, foundry coordinators, supply planners, applications engineers, and technical program managers",
        "A semiconductor English curriculum for wafer fabrication, lithography, process integration, deposition and etch, metrology, yield learning, cleanroom discipline, equipment uptime, packaging, reliability qualification, foundry communication, and customer pressure.",
        [
            m("Wafer Fabrication Flow and Process Integration", "Explain the fab process as a controlled sequence of dependencies, not a simple production line.", "A program manager asks why one wafer lot cannot skip a hold and move directly to the next module.", "Release the lot to protect the customer schedule.", "Process flow, route control, layer dependency, and integration risk must be confirmed before movement.", "lot-disposition recommendation", ["wafer", "fab", "process flow", "node"], ("Program manager", "Process integration engineer")),
            m("Lithography, Reticles, and Critical Dimensions", "Discuss patterning risk with enough precision for engineers and enough clarity for non-specialists.", "A customer asks whether a critical-dimension trend is only a measurement artifact.", "Tell them the lithography module is under control.", "Reticle status, photoresist behavior, exposure conditions, metrology repeatability, and control limits need review.", "lithography risk update", ["lithography", "photoresist", "reticle", "critical dimension"], ("Customer quality lead", "Lithography engineer")),
            m("Deposition, Etch, CMP, and Process Windows", "Connect process module changes to downstream device performance.", "A team wants to widen an etch recipe to improve throughput.", "Approve the recipe because cycle time improves.", "Deposition uniformity, etch selectivity, CMP margin, and the qualified process window must be protected.", "process-window tradeoff memo", ["deposition", "etch", "CMP", "process window"], ("Operations director", "Module process owner")),
            m("Metrology, SPC, and Yield Learning", "Use data language that separates signal, noise, and urgent excursion.", "A dashboard shows yield loss after a new metrology sampling plan.", "Call it a bad lot and move on.", "SPC trends, sampling change, tool history, defect signatures, and product mix must be separated.", "yield-learning brief", ["metrology", "SPC", "yield", "excursion"], ("Yield engineer", "Fab area manager")),
            m("Defect Density and Cleanroom Contamination", "Escalate contamination risk without creating blame or panic.", "A particle excursion appears after maintenance in a critical bay.", "Restart production and watch the next few lots.", "Defect density, cleanroom protocol, contamination source, containment, and affected-lot traceability require action.", "contamination containment note", ["defect density", "particle", "cleanroom", "contamination control"], ("Cleanroom supervisor", "Manufacturing quality engineer")),
            m("Equipment Uptime, Recipes, and Tool Matching", "Discuss equipment pressure without sacrificing process control.", "A high-demand tool is repeatedly down and a second tool is almost matched.", "Move all lots to the second tool immediately.", "Tool uptime, preventive maintenance status, recipe qualification, tool matching evidence, and bottleneck risk must be balanced.", "tool-qualification escalation", ["tool uptime", "preventive maintenance", "recipe", "tool matching"], ("Equipment engineer", "Production planner")),
            m("Packaging, Test, and Reliability Qualification", "Explain post-fab risk using test and reliability language.", "A product team wants to ship early units before reliability stress testing is complete.", "Ship the units because electrical test passed.", "Package interaction, binning criteria, burn-in results, qualification status, and customer-use conditions are not interchangeable.", "qualification readiness update", ["package", "binning", "burn-in", "qualification"], ("Product engineer", "Business unit manager")),
            m("Foundry, Tape-Out, PDK, and Capacity Communication", "Handle customer and executive pressure around constrained foundry schedules.", "A customer asks for a guaranteed tape-out and wafer-start date despite capacity constraints.", "Promise the date to protect the relationship.", "Foundry allocation, PDK readiness, mask schedule, change freeze, and capacity allocation need documented assumptions.", "foundry customer update", ["foundry", "tape-out", "PDK", "capacity allocation"], ("Foundry coordinator", "Customer program manager")),
        ],
        ["Company process-control plans, fab SOPs, and manufacturing quality procedures.", "SEMI, JEDEC, AEC-Q, and customer qualification expectations where applicable.", "Foundry documentation, PDK release notes, customer quality agreements, and approved communication procedures."],
        SEMICONDUCTOR_TERM_DEFINITIONS,
        SEMICONDUCTOR_COLLOCATIONS,
        SEMICONDUCTOR_DIALOGUES,
        SEMICONDUCTOR_NOMENCLATURE,
    ),
    profile(
        "Software Product Management English",
        "software-product-management",
        "software product managers, product owners, UX leads, engineering managers, growth product teams, platform PMs, and product-operations staff",
        "A software product-management English curriculum for discovery, roadmaps, user stories, prioritization, metrics, launches, stakeholder negotiation, experimentation, and product strategy.",
        [
            m("Product Discovery and Problem Framing", "Separate customer requests from underlying problems.", "A large customer asks for a custom feature.", "Put it on the roadmap immediately.", "User need, segment fit, evidence, opportunity cost, and strategy need review.", "discovery brief", ["user need", "persona", "use case", "opportunity cost"], ("Sales leader", "Product manager")),
            m("Roadmaps and Prioritization", "Explain roadmap tradeoffs under executive pressure.", "Executives want three major features in one quarter.", "Commit to all three.", "Capacity, dependencies, risk, strategic fit, and sequencing must be clear.", "roadmap tradeoff memo", ["roadmap", "prioritization", "dependency", "capacity"], ("VP Product", "Engineering manager")),
            m("User Stories and Acceptance Criteria", "Turn vague ideas into buildable requirements.", "Design and engineering disagree about what done means.", "Let engineering interpret the request.", "Acceptance criteria, edge cases, analytics, and UX intent need definition.", "user-story rewrite", ["user story", "acceptance criteria", "edge case", "definition of done"], ("Product owner", "UX designer")),
            m("Metrics, Funnels, and Product Analytics", "Discuss metrics without confusing movement with causation.", "Activation improved after a release.", "Declare the feature successful.", "Cohorts, instrumentation, seasonality, and counter-metrics need review.", "metric interpretation note", ["activation", "retention", "funnel", "cohort"], ("Product analyst", "Growth PM")),
            m("Experimentation and A/B Testing", "Frame experiments with hypotheses and guardrails.", "Marketing wants to launch a variant because early clicks are higher.", "Roll it out to everyone.", "Sample size, significance, novelty effect, and guardrail metrics matter.", "experiment readout", ["A/B test", "hypothesis", "guardrail metric", "statistical significance"], ("Growth PM", "Marketing lead")),
            m("Release Readiness and Go-to-Market", "Coordinate launch dependencies across product, engineering, sales, and support.", "A feature is code-complete but docs and support training are not ready.", "Launch because engineering is done.", "Documentation, enablement, migration, monitoring, and rollback need readiness.", "launch readiness checklist", ["release", "rollback", "enablement", "migration"], ("Product manager", "Support lead")),
            m("Platform, APIs, and Technical Debt", "Discuss invisible work in business terms.", "Engineering asks for a sprint to address technical debt.", "Reject it because customers cannot see it.", "Reliability, developer velocity, support burden, and future roadmap risk need translation.", "technical debt business case", ["technical debt", "API", "platform", "reliability"], ("Engineering manager", "Product leader")),
            m("Stakeholder Pushback and Executive Narrative", "Say no or not now while preserving trust.", "A senior stakeholder wants a feature that conflicts with strategy.", "Agree to keep the relationship positive.", "Strategic fit, customer segment, cost, and alternatives need a clear recommendation.", "stakeholder pushback script", ["stakeholder", "strategic fit", "tradeoff", "decision memo"], ("Executive sponsor", "Product manager")),
        ],
        ["Company product strategy and roadmap governance.", "Analytics definitions and data-quality standards.", "Privacy, security, and customer-commitment review procedures."],
    ),
    profile(
        "Cybersecurity English",
        "cybersecurity",
        "security analysts, SOC staff, incident responders, security engineers, GRC specialists, identity teams, vulnerability managers, and security leaders",
        "A cybersecurity English curriculum for incident response, vulnerability triage, identity, threat modeling, risk communication, compliance, executive briefings, and security pushback.",
        [
            m("Security Triage and Alert Investigation", "Move from noisy alerts to risk-based investigation.", "The SOC receives repeated alerts from a privileged account.", "Close them as false positives because the user is senior.", "Privilege, behavior, context, and evidence need review.", "alert triage note", ["SIEM", "alert", "false positive", "privileged account"], ("SOC analyst", "Security manager")),
            m("Incident Response and Containment", "Communicate urgency without speculation.", "A ransomware note appears on a shared server.", "Tell everyone the company is breached.", "Scope, containment, evidence preservation, communications, and legal review matter.", "incident bridge update", ["incident", "containment", "ransomware", "forensics"], ("Incident commander", "IT operations lead")),
            m("Vulnerability Management", "Prioritize vulnerabilities beyond CVSS alone.", "A critical CVE affects an internet-facing system.", "Patch every system immediately.", "Exploitability, exposure, asset criticality, compensating controls, and downtime must be balanced.", "vulnerability prioritization memo", ["CVE", "CVSS", "exploitability", "compensating control"], ("Vulnerability manager", "Application owner")),
            m("Identity, Access, and Least Privilege", "Push back on excessive access requests.", "A contractor asks for admin rights to troubleshoot faster.", "Grant temporary admin access.", "Least privilege, approval, logging, and time-bound access are required.", "access request response", ["IAM", "least privilege", "MFA", "RBAC"], ("Identity engineer", "Contractor manager")),
            m("Threat Modeling and Secure Design", "Discuss security risk early in design.", "A product team wants to skip threat modeling to meet a launch date.", "Do a quick review after launch.", "Abuse cases, data flows, trust boundaries, and mitigations need design-time attention.", "threat model findings", ["threat model", "attack surface", "trust boundary", "abuse case"], ("Security architect", "Product manager")),
            m("Governance, Risk, and Compliance", "Translate control gaps into business risk.", "Audit finds incomplete access reviews.", "Say the control is mostly working.", "Control design, evidence, ownership, remediation, and risk acceptance need clarity.", "GRC remediation plan", ["control", "audit evidence", "risk acceptance", "remediation"], ("GRC lead", "System owner")),
            m("Security Awareness and Phishing", "Coach users without shaming them.", "An executive clicks a phishing simulation link.", "Send a public warning.", "Behavior, training, reporting culture, and technical controls all matter.", "awareness coaching script", ["phishing", "social engineering", "reporting culture", "security awareness"], ("Security awareness lead", "Executive assistant")),
            m("Executive Risk Briefings", "Explain cyber risk in decision language.", "The board asks whether the organization is safe from attacks.", "Give a yes-or-no answer.", "Residual risk, threat landscape, controls, investment, and response readiness require nuance.", "board cyber-risk update", ["residual risk", "threat actor", "maturity", "investment ask"], ("CISO", "Board member")),
        ],
        ["NIST, CISA, and relevant security frameworks.", "Company incident-response and access-control policies.", "Legal, privacy, and communications guidance for incidents."],
    ),
    profile(
        "Data Analytics and Business Intelligence English",
        "data-analytics-business-intelligence",
        "data analysts, BI developers, analytics engineers, data scientists, reporting teams, business analysts, and data-driven managers",
        "A data analytics and BI English curriculum for metric definitions, dashboards, data quality, stakeholder requests, causation, experimentation, governance, and insight presentation.",
        [
            m("Metric Definitions and Business Questions", "Clarify what a number means before reporting it.", "Two teams use different definitions of active customer.", "Pick one quickly for the dashboard.", "Business definition, source table, filter logic, and owner need agreement.", "metric definition note", ["metric", "business definition", "source of truth", "owner"], ("Analytics lead", "Revenue leader")),
            m("Data Quality and Trust", "Discuss data problems without undermining the whole analysis.", "A dashboard shows a sudden drop after a pipeline change.", "Tell users the data are wrong.", "Freshness, completeness, transformation logic, and upstream changes must be checked.", "data-quality incident update", ["data quality", "freshness", "completeness", "pipeline"], ("BI developer", "Business stakeholder")),
            m("Dashboards and Executive Reporting", "Design dashboards around decisions, not decoration.", "Executives ask for a dashboard with every possible metric.", "Add all requested charts.", "Audience, decision, refresh cadence, and alert thresholds need focus.", "dashboard requirements brief", ["dashboard", "KPI", "threshold", "drill-down"], ("Executive", "BI analyst")),
            m("Causation, Correlation, and Caveats", "Prevent overinterpretation of patterns.", "Sales increased after a campaign and marketing claims causality.", "Say the campaign caused the increase.", "Seasonality, selection bias, control groups, and other factors need analysis.", "causality caveat paragraph", ["correlation", "causation", "confounder", "selection bias"], ("Marketing manager", "Data analyst")),
            m("SQL, Models, and Transformation Logic", "Explain technical logic to nontechnical partners.", "A finance report differs from the warehouse model.", "Fix the number silently.", "Join logic, grain, filters, and reconciliation need transparent review.", "reconciliation explanation", ["SQL", "data model", "grain", "join logic"], ("Analytics engineer", "Finance analyst")),
            m("Experiment Readouts and Statistical Thinking", "Present test results with practical and statistical context.", "A test shows a small lift with uncertain confidence.", "Recommend full rollout.", "Sample size, effect size, confidence, guardrails, and cost should guide decisions.", "experiment readout slide", ["sample size", "effect size", "confidence interval", "guardrail"], ("Data scientist", "Product manager")),
            m("Data Governance and Privacy", "Set data-use boundaries professionally.", "A team requests customer-level data for broad exploration.", "Send the extract.", "Purpose limitation, access control, retention, and privacy rules need confirmation.", "data access response", ["data governance", "privacy", "access control", "retention"], ("Data governance lead", "Business analyst")),
            m("Insight Storytelling and Recommendations", "Move from analysis to action without overstating certainty.", "A stakeholder wants a simple recommendation from messy data.", "Hide limitations to make the story clear.", "Uncertainty, tradeoffs, assumptions, and next tests need visible framing.", "insight recommendation memo", ["insight", "recommendation", "assumption", "next best action"], ("Analytics manager", "Operations leader")),
        ],
        ["Company data governance and privacy policies.", "Analytics definitions and semantic-layer documentation.", "Experimentation and dashboard standards."],
    ),
    profile(
        "Education Administration English",
        "education-administration",
        "school administrators, curriculum coordinators, student-services staff, program directors, admissions teams, registrars, and education operations leaders",
        "An education administration English curriculum for enrollment, student support, curriculum planning, parent communication, faculty coordination, compliance, accreditation, and institutional decision-making.",
        [
            m("Enrollment, Admissions, and Placement", "Discuss student fit and capacity with fairness and clarity.", "A program has more qualified applicants than seats.", "Accept the loudest families first.", "Admission criteria, placement evidence, capacity, and equity need transparent handling.", "admissions decision rationale", ["admissions criteria", "placement", "capacity", "equity"], ("Admissions director", "Program coordinator")),
            m("Curriculum Planning and Learning Outcomes", "Connect course design to measurable learning outcomes.", "A department wants to add content without changing assessments.", "Insert the new unit.", "Standards, outcomes, sequence, assessment, and workload must align.", "curriculum alignment memo", ["learning outcome", "curriculum map", "assessment", "standard"], ("Curriculum lead", "Department chair")),
            m("Student Support and Intervention", "Discuss struggling students using evidence and support language.", "A student is failing multiple classes.", "Tell the family the student is not trying.", "Attendance, assessment data, accommodations, behavior, and support plans need review.", "student intervention plan", ["intervention", "accommodation", "attendance", "student support"], ("Student-services coordinator", "Teacher")),
            m("Parent and Guardian Communication", "Handle emotionally charged conversations with clarity.", "A parent disputes a disciplinary decision.", "Defend the school policy firmly.", "Facts, policy, student privacy, appeal options, and empathy must be balanced.", "parent meeting script", ["guardian communication", "discipline", "appeal", "confidentiality"], ("Assistant principal", "Parent")),
            m("Faculty Coordination and Evaluation", "Give faculty feedback without vague judgment.", "A teacher receives complaints about inconsistent grading.", "Say students are unhappy.", "Rubrics, grading policy, classroom evidence, and professional support are needed.", "faculty feedback note", ["rubric", "grading policy", "observation", "professional development"], ("Academic dean", "Teacher")),
            m("Compliance, Records, and Privacy", "Explain record rules and student privacy.", "A staff member wants to share student records by email.", "Send the files because the request is internal.", "Need-to-know access, secure handling, and privacy policy must be confirmed.", "records-access response", ["FERPA", "student record", "need to know", "secure handling"], ("Registrar", "Program staff")),
            m("Accreditation and Program Review", "Use evidence language for institutional quality.", "A program review finds weak outcome data.", "Write that improvements are in progress.", "Evidence, assessment cycle, action plan, and ownership must be documented.", "program review action plan", ["accreditation", "program review", "evidence", "action plan"], ("Accreditation lead", "Program director")),
            m("Budget, Staffing, and Institutional Priorities", "Discuss resource tradeoffs without mission drift.", "A school wants to launch a new program with no additional staff.", "Ask existing staff to absorb it.", "Workload, student impact, compliance, and sustainability need evaluation.", "resource tradeoff brief", ["budget", "staffing model", "workload", "sustainability"], ("School director", "Operations manager")),
        ],
        ["Institutional policies and student-record privacy rules.", "Accreditation and curriculum standards.", "Local education regulations and student-support procedures."],
    ),
    profile(
        "Higher Education and Research English",
        "higher-education-research",
        "faculty, postdoctoral researchers, graduate students, lab managers, research administrators, grant staff, ethics-board coordinators, and academic program leaders",
        "A higher education and research English curriculum for grant proposals, lab meetings, peer review, research ethics, authorship, data management, academic presentations, and institutional collaboration.",
        [
            m("Research Questions and Study Design", "Frame research claims with scope and methodological discipline.", "A lab wants to describe an exploratory study as definitive.", "Use stronger language to attract attention.", "Hypothesis, design, sample, limitations, and inference must be aligned.", "study-design caveat", ["research question", "hypothesis", "methodology", "limitation"], ("Principal investigator", "Postdoc")),
            m("Grant Proposals and Specific Aims", "Write aims that are ambitious but testable.", "A proposal includes too many objectives for the budget.", "Keep every aim to look comprehensive.", "Feasibility, significance, innovation, approach, and milestones need balance.", "specific-aims revision", ["specific aims", "significance", "innovation", "feasibility"], ("Grant writer", "Principal investigator")),
            m("Lab Meetings and Data Challenges", "Question data respectfully but rigorously.", "A student presents inconsistent results.", "Say the data are bad.", "Controls, replication, protocol drift, and analysis assumptions need review.", "lab-meeting question set", ["control", "replication", "protocol drift", "analysis assumption"], ("Lab manager", "Graduate student")),
            m("Research Ethics and Human Subjects", "Set boundaries around consent, risk, and protocol adherence.", "A researcher wants to use data for a new question outside the approved protocol.", "Analyze it because the data already exist.", "Consent, IRB approval, privacy, and secondary-use rules may apply.", "ethics consultation note", ["IRB", "informed consent", "secondary use", "human subjects"], ("Research administrator", "Faculty member")),
            m("Authorship, Collaboration, and Credit", "Discuss contribution and authorship early.", "A collaborator expects authorship after a small advisory role.", "Agree to avoid conflict.", "Contribution, criteria, order, acknowledgments, and publication norms must be explicit.", "authorship agreement draft", ["authorship", "contribution", "corresponding author", "acknowledgment"], ("Postdoc", "External collaborator")),
            m("Peer Review and Revision Responses", "Respond to criticism without defensiveness.", "Reviewers ask for additional analyses outside the original scope.", "Reject the comment sharply.", "Tone, evidence, scope, feasibility, and transparent limitations matter.", "reviewer-response paragraph", ["peer review", "major revision", "response letter", "scope"], ("Journal editor", "Author")),
            m("Data Management and Reproducibility", "Explain data stewardship and reproducible workflows.", "A dataset lacks clear metadata before publication.", "Upload it anyway.", "Metadata, code, provenance, privacy, and repository requirements need attention.", "data-management checklist", ["metadata", "repository", "provenance", "reproducibility"], ("Data steward", "Research team")),
            m("Academic Presentations and Conferences", "Present claims with confidence and caveats.", "A conference audience challenges the study's generalizability.", "Defend every conclusion.", "Population, context, method, and future work should be addressed calmly.", "conference Q&A response", ["generalizability", "limitation", "future work", "conference Q&A"], ("Conference attendee", "Presenter")),
        ],
        ["Institutional research policies and IRB guidance.", "Grant-funder instructions and journal requirements.", "Field norms for authorship, data, and reproducibility."],
    ),
    profile(
        "Hospitality and Tourism English",
        "hospitality-tourism",
        "hotel managers, front-desk teams, guest-relations staff, event coordinators, restaurant managers, tour operators, revenue managers, and destination-service professionals",
        "A hospitality and tourism English curriculum for guest complaints, service recovery, reservations, revenue management, events, vendor coordination, cultural expectations, reviews, and operational briefings.",
        [
            m("Guest Arrival and Front-Desk Escalation", "Resolve arrival problems while protecting policy and guest dignity.", "A guest arrives early and their room is not ready.", "Upgrade them immediately.", "Inventory, loyalty status, housekeeping, policy, and guest emotion need balance.", "arrival recovery script", ["check-in", "room inventory", "upgrade", "service recovery"], ("Front-office manager", "Guest")),
            m("Complaint Handling and Online Reviews", "Respond to complaints without admitting unsupported facts.", "A guest posts that staff were rude and the room was dirty.", "Offer a full refund publicly.", "Investigation, privacy, brand tone, and recovery options must be considered.", "review response draft", ["guest complaint", "online review", "brand voice", "compensation"], ("Guest-relations lead", "General manager")),
            m("Reservations, Overbooking, and Walks", "Communicate inventory constraints transparently.", "The hotel is oversold during a citywide event.", "Tell late arrivals there is nothing available.", "Walk policy, partner hotel, transportation, compensation, and empathy are needed.", "overbooking response", ["overbooking", "walk", "occupancy", "rate parity"], ("Revenue manager", "Front-desk supervisor")),
            m("Revenue Management and Pricing", "Explain pricing changes without sounding arbitrary.", "A corporate client questions a rate increase.", "Say demand is high.", "Demand, compression nights, contract terms, and value need careful explanation.", "rate-change explanation", ["ADR", "RevPAR", "yield management", "compression night"], ("Sales manager", "Corporate client")),
            m("Housekeeping, Maintenance, and Turnover", "Coordinate operational recovery across departments.", "Rooms are not turning over fast enough for check-in.", "Pressure housekeeping to move faster.", "Room status, staffing, maintenance defects, and guest promises need coordination.", "turnover recovery plan", ["room status", "out of order", "turnover", "preventive maintenance"], ("Housekeeping manager", "Front-office manager")),
            m("Events, Banquets, and Run of Show", "Manage event details and last-minute changes.", "A client changes seating and AV needs on event day.", "Say yes to every change.", "Contract, staffing, setup time, safety, and vendor capacity need review.", "event change response", ["BEO", "run of show", "attrition", "AV requirement"], ("Event coordinator", "Client")),
            m("Tour Operations and Traveler Safety", "Communicate itinerary changes and safety constraints.", "Weather disrupts a tour itinerary.", "Keep the original plan to avoid complaints.", "Safety, local rules, refunds, timing, and guest expectations must be managed.", "itinerary-change announcement", ["itinerary", "force majeure", "waiver", "local operator"], ("Tour manager", "Guest group")),
            m("Cultural Expectations and Service Style", "Interpret guest behavior across cultures without stereotyping.", "International guests complain that service feels cold.", "Tell staff to be friendlier.", "Expectations, language, nonverbal cues, and service standards need coaching.", "cross-cultural service briefing", ["service standard", "cultural expectation", "guest profile", "recovery gesture"], ("Training manager", "Front-line staff")),
        ],
        ["Property policies and brand standards.", "Local tourism, safety, and consumer-protection rules.", "Contracts, event orders, and reservation terms."],
    ),
    profile(
        "Aviation English",
        "aviation",
        "aviation operations managers, airline staff, maintenance coordinators, safety teams, dispatchers, airport operations staff, ground handlers, and aviation-adjacent professionals",
        "An aviation English curriculum for safety culture, operations control, maintenance coordination, irregular operations, ground handling, compliance, passenger escalation, and incident reporting.",
        [
            m("Safety Culture and Stop-Work Authority", "Use safety language that is direct and nonpunitive.", "Ground staff notice a possible fuel leak during a turnaround.", "Continue boarding to avoid delay.", "Safety, inspection, documentation, and operational control override schedule pressure.", "safety stop-work call", ["safety management system", "hazard", "stop work", "reporting culture"], ("Ramp supervisor", "Operations control")),
            m("Operations Control and Dispatch Coordination", "Communicate operational constraints quickly and accurately.", "A crew legality issue appears before departure.", "Ask the crew to continue anyway.", "Duty limits, passenger impact, aircraft routing, and recovery options need review.", "dispatch coordination update", ["dispatch", "crew legality", "aircraft routing", "delay code"], ("Dispatcher", "Station manager")),
            m("Maintenance Deferrals and MEL Language", "Discuss maintenance status without casual reassurance.", "A component issue may be deferrable.", "Tell the gate it is fine.", "MEL conditions, logbook entry, placarding, and operational limitations must be confirmed.", "maintenance status brief", ["MEL", "logbook", "deferred maintenance", "airworthiness"], ("Maintenance controller", "Gate manager")),
            m("Irregular Operations and Passenger Communication", "Explain disruptions with empathy and operational accuracy.", "Weather causes cancellations across the network.", "Say flights are canceled due to weather and stop there.", "Rebooking, hotel policy, crew, aircraft, and safety rationale need clear messaging.", "IROP passenger announcement", ["IROP", "reaccommodation", "misconnect", "weather delay"], ("Customer service lead", "Passenger")),
            m("Ground Handling and Turnaround Performance", "Coordinate fast turnarounds without unsafe shortcuts.", "A late inbound aircraft has a short connection window.", "Cut corners to make the departure slot.", "Fueling, catering, bags, security checks, and safety zones all have minimum requirements.", "turnaround risk update", ["turnaround", "ground handling", "load sheet", "ramp safety"], ("Ground operations lead", "Load planner")),
            m("Security and Access Control", "Set boundaries around secure areas and credentials.", "A vendor arrives without proper badge access.", "Escort them informally because the work is urgent.", "Access rules, escort requirements, identity checks, and audit risk apply.", "access-control response", ["secure area", "badge", "escort", "audit"], ("Airport operations supervisor", "Vendor")),
            m("Incident Reporting and Investigation", "Report events factually before conclusions are known.", "A baggage vehicle clips aircraft equipment.", "Describe it as minor and continue.", "Damage assessment, reporting, evidence preservation, and accountability are required.", "incident report summary", ["incident report", "damage assessment", "root cause", "corrective action"], ("Safety manager", "Ramp agent")),
            m("Regulatory Audits and Readiness", "Answer audit questions with evidence, not confidence.", "An auditor asks for training records for ground staff.", "Say everyone is trained.", "Records, currency, scope, and corrective action must be documented.", "audit response plan", ["audit", "training record", "compliance", "corrective action"], ("Compliance manager", "Station director")),
        ],
        ["Current FAA, airport, carrier, and local aviation procedures.", "Company safety management system and reporting processes.", "Maintenance, ground-handling, and security manuals."],
    ),
    profile(
        "Construction and Architecture English",
        "construction-architecture",
        "architects, construction managers, project engineers, site supervisors, estimators, owners' representatives, subcontractor coordinators, and design-build teams",
        "A construction and architecture English curriculum for design intent, RFIs, change orders, site coordination, safety, schedule pressure, permitting, punch lists, claims, and client communication.",
        [
            m("Design Intent and Client Requirements", "Clarify aesthetic, functional, code, and budget constraints.", "A client requests a major design change late in design development.", "Update the drawings immediately.", "Scope, fee, schedule, code, and constructability implications need review.", "design-change response", ["design intent", "program", "constructability", "scope"], ("Architect", "Client representative")),
            m("Drawings, Specifications, and RFIs", "Resolve ambiguity without assigning blame.", "A subcontractor says drawings conflict with specifications.", "Tell them to follow the drawings.", "Contract documents, RFI process, schedule impact, and design response are needed.", "RFI response summary", ["RFI", "specification", "drawing set", "submittal"], ("Project engineer", "Subcontractor")),
            m("Change Orders and Cost Control", "Discuss changes using entitlement, impact, and documentation language.", "A subcontractor submits a change order for hidden conditions.", "Reject it because the budget is tight.", "Contract terms, notice, evidence, schedule, and pricing must be reviewed.", "change-order evaluation", ["change order", "allowance", "contingency", "notice"], ("Construction manager", "Owner")),
            m("Schedule, Sequencing, and Critical Path", "Explain delay risk with dependency language.", "Steel delivery delay threatens enclosure work.", "Ask all trades to recover the time.", "Critical path, float, resequencing, crew availability, and weather risk matter.", "schedule impact update", ["critical path", "float", "lookahead schedule", "resequencing"], ("Scheduler", "Site superintendent")),
            m("Site Safety and Toolbox Talks", "Stop unsafe work and explain why.", "A crew works at height without proper fall protection.", "Remind them quickly and continue.", "Safety requirements, stop-work authority, training, and documentation apply.", "toolbox safety talk", ["PPE", "fall protection", "toolbox talk", "stop work"], ("Safety manager", "Foreman")),
            m("Permitting, Inspections, and Code Issues", "Communicate authority and compliance constraints.", "An inspector rejects an installation detail.", "Ask the inspector to be flexible.", "Code interpretation, approved drawings, corrective work, and reinspection are required.", "inspection correction plan", ["permit", "inspection", "code compliance", "reinspection"], ("Owner's rep", "Inspector")),
            m("Quality, Punch List, and Closeout", "Define completion and acceptance clearly.", "The client wants occupancy while punch items remain.", "Hand over the space anyway.", "Life safety, substantial completion, warranties, and closeout documents need clarity.", "punch-list closeout plan", ["punch list", "substantial completion", "warranty", "closeout"], ("Project manager", "Client")),
            m("Claims, Disputes, and Documentation", "Preserve facts during conflict.", "A delay dispute emerges after months of informal changes.", "Argue from memory.", "Daily reports, notices, photos, meeting minutes, and contract language matter.", "claim chronology", ["claim", "daily report", "meeting minutes", "entitlement"], ("Claims consultant", "Project executive")),
        ],
        ["Project contracts, drawings, specifications, and local codes.", "OSHA or local construction safety requirements.", "Permitting, inspection, and closeout procedures."],
    ),
    profile(
        "Energy and Utilities English",
        "energy-utilities",
        "utility operations staff, energy project managers, grid planners, field supervisors, regulatory affairs teams, renewable-energy developers, customer operations teams, and infrastructure leaders",
        "An energy and utilities English curriculum for reliability, outages, grid operations, safety, regulatory filings, renewables integration, infrastructure projects, customer communication, and risk reporting.",
        [
            m("Grid Reliability and Outage Response", "Explain reliability events with operational precision.", "A feeder outage affects critical customers during peak load.", "Promise restoration within an hour.", "Crew safety, fault location, switching, weather, and restoration uncertainty matter.", "outage response update", ["reliability", "feeder", "restoration", "critical customer"], ("Control-room operator", "Customer operations lead")),
            m("Safety, Field Work, and Switching", "Use field-safety language under pressure.", "A crew is asked to energize equipment before all checks are complete.", "Proceed to meet the schedule.", "Lockout, clearance, switching order, and crew confirmation must be complete.", "field safety stop", ["switching order", "lockout", "clearance", "energize"], ("Field supervisor", "Operations control")),
            m("Regulatory Affairs and Rate Cases", "Translate regulatory requirements into business and customer impact.", "Leadership wants to simplify a rate-case explanation.", "Say rates must rise because costs rose.", "Cost drivers, prudence, customer impact, and regulatory process need careful framing.", "rate-case narrative", ["rate case", "tariff", "prudence", "customer impact"], ("Regulatory affairs manager", "Finance lead")),
            m("Renewables Integration and Interconnection", "Discuss clean-energy goals with grid constraints.", "A developer wants fast interconnection for a solar project.", "Promise the date to secure the deal.", "Queue position, study results, upgrades, and system reliability affect timing.", "interconnection status note", ["interconnection", "capacity", "curtailment", "queue"], ("Renewables developer", "Grid planner")),
            m("Asset Management and Maintenance", "Explain infrastructure risk and investment needs.", "Aging equipment shows rising failure rates.", "Delay replacement for budget reasons.", "Asset condition, reliability impact, safety, and lifecycle cost need evaluation.", "asset-risk business case", ["asset management", "condition assessment", "lifecycle cost", "failure rate"], ("Asset manager", "Operations director")),
            m("Emergency Preparedness and Storm Response", "Coordinate crisis communication and resource allocation.", "A storm forecast may affect multiple service territories.", "Wait until damage is confirmed.", "Mutual aid, crew staging, materials, public communication, and safety messaging need preparation.", "storm readiness brief", ["mutual aid", "crew staging", "restoration priority", "emergency response"], ("Emergency response lead", "Communications manager")),
            m("Customer Programs and Energy Efficiency", "Explain incentives without overpromising savings.", "A customer expects guaranteed savings from an efficiency program.", "Promise the average result.", "Eligibility, baseline use, behavior, equipment, and measurement rules affect outcomes.", "program expectation script", ["incentive", "baseline", "demand response", "measurement and verification"], ("Program manager", "Customer")),
            m("Executive Reliability and Investment Updates", "Present technical risk to leaders and regulators.", "The executive team asks why reliability metrics worsened.", "Blame weather.", "SAIDI, SAIFI, asset condition, vegetation, investment, and mitigation all matter.", "reliability executive update", ["SAIDI", "SAIFI", "vegetation management", "capital plan"], ("Utility executive", "Reliability engineer")),
        ],
        ["Utility operating procedures and safety manuals.", "Public utility commission requirements and tariffs.", "Emergency response and customer communication protocols."],
    ),
    profile(
        "Environmental Consulting English",
        "environmental-consulting",
        "environmental consultants, remediation managers, sustainability analysts, field scientists, permitting specialists, ESG teams, and environmental project managers",
        "An environmental consulting English curriculum for site assessments, permitting, remediation, sampling, stakeholder meetings, sustainability reporting, compliance, and client-risk communication.",
        [
            m("Phase I and Phase II Site Assessments", "Explain environmental risk before conclusions are final.", "A buyer wants assurance that a site is clean.", "Say no issues were found.", "Recognized environmental conditions, sampling scope, limitations, and due diligence matter.", "site-assessment caveat", ["Phase I ESA", "REC", "Phase II", "due diligence"], ("Consultant", "Real estate client")),
            m("Sampling Plans and Data Quality", "Discuss field data with chain-of-custody and QA language.", "A client questions why more samples are needed.", "Reduce sampling to save budget.", "Decision units, detection limits, QA/QC, and regulatory standards must support conclusions.", "sampling-plan explanation", ["sampling plan", "chain of custody", "detection limit", "QA/QC"], ("Field scientist", "Client project manager")),
            m("Permitting and Agency Coordination", "Manage agency questions without promising outcomes.", "A permit reviewer requests additional modeling.", "Tell the client approval is still certain.", "Agency discretion, technical support, timelines, and public comments may affect approval.", "permit-response update", ["permit", "agency comment", "public notice", "modeling"], ("Permitting specialist", "Client executive")),
            m("Remediation Options and Risk", "Compare cleanup options in plain language.", "A site has contaminated soil under an active facility.", "Excavate immediately.", "Exposure pathway, remedy effectiveness, operations disruption, cost, and long-term monitoring matter.", "remediation options memo", ["remediation", "exposure pathway", "cap", "long-term monitoring"], ("Remediation manager", "Operations client")),
            m("Regulatory Compliance and Audits", "Explain findings without exaggeration or minimization.", "An audit finds storage and labeling issues.", "Call them minor housekeeping items.", "Compliance obligations, corrective action, documentation, and recurrence risk need review.", "compliance finding summary", ["compliance audit", "corrective action", "recordkeeping", "inspection"], ("Environmental auditor", "Plant manager")),
            m("Sustainability and ESG Reporting", "Use sustainability claims carefully.", "Marketing wants to claim the company is carbon neutral.", "Use the claim because offsets were purchased.", "Scope, boundary, methodology, assurance, and claim substantiation are required.", "sustainability claim review", ["ESG", "Scope 1", "Scope 2", "Scope 3", "carbon neutral"], ("Sustainability analyst", "Marketing lead")),
            m("Community and Stakeholder Meetings", "Communicate technical risk to nontechnical audiences.", "Residents ask whether a plume affects drinking water.", "Give a quick yes-or-no answer.", "Data, uncertainty, exposure, agency role, and next steps need accessible explanation.", "community-meeting response", ["stakeholder", "plume", "exposure", "risk communication"], ("Project manager", "Community member")),
            m("Proposal, Scope, and Client Expectations", "Define consulting scope and assumptions clearly.", "A client expects unlimited regulatory support under a small budget.", "Absorb the extra work.", "Scope, assumptions, exclusions, change orders, and deliverables need explicit language.", "consulting scope clarification", ["scope", "assumption", "deliverable", "change order"], ("Consulting principal", "Client sponsor")),
        ],
        ["EPA and state environmental guidance as applicable.", "Client contracts and project scopes.", "Field sampling, QA/QC, and health-safety plans."],
    ),
    profile(
        "Insurance English",
        "insurance",
        "underwriters, claims adjusters, brokers, risk managers, actuarial analysts, policy-service teams, compliance staff, and insurance operations leaders",
        "An insurance English curriculum for underwriting, claims, policy language, coverage disputes, actuarial assumptions, broker communication, fraud concerns, compliance, and customer escalation.",
        [
            m("Underwriting and Risk Selection", "Explain underwriting decisions without sounding arbitrary.", "A broker asks why a profitable account received a restrictive quote.", "Say the risk appetite changed.", "Exposure, loss history, controls, appetite, and pricing adequacy need explanation.", "underwriting rationale", ["underwriting", "risk appetite", "exposure", "loss history"], ("Underwriter", "Broker")),
            m("Policy Language and Coverage Interpretation", "Discuss coverage without giving casual assurances.", "A client asks whether a new activity is covered.", "Say it should be covered.", "Policy terms, exclusions, endorsements, facts, and claims review may control.", "coverage caveat response", ["policy", "endorsement", "exclusion", "coverage"], ("Account manager", "Insured client")),
            m("Claims Intake and Reserving", "Gather facts and set expectations after a loss.", "A policyholder wants immediate payment after submitting photos.", "Promise payment this week.", "Coverage, documentation, liability, damages, and reserve review are needed.", "claims intake summary", ["claim", "reserve", "proof of loss", "adjuster"], ("Claims adjuster", "Policyholder")),
            m("Coverage Disputes and Denials", "Communicate adverse decisions with clarity and empathy.", "A claim appears excluded under the policy.", "Send a short denial letter.", "Facts, policy language, legal review, appeal rights, and tone matter.", "denial explanation draft", ["denial", "reservation of rights", "appeal", "coverage position"], ("Claims manager", "Policyholder")),
            m("Broker and Client Renewal Meetings", "Discuss rate increases and terms under market pressure.", "Premiums increase despite no recent losses.", "Blame the market.", "Loss trends, exposure growth, reinsurance, capacity, and terms need explanation.", "renewal meeting brief", ["renewal", "premium", "deductible", "reinsurance"], ("Broker", "Risk manager")),
            m("Fraud Indicators and SIU Referral", "Raise suspicious patterns without accusation.", "A claim has inconsistent timing and documents.", "Accuse the claimant of fraud.", "Evidence, investigation process, documentation, and legal boundaries matter.", "SIU referral note", ["fraud indicator", "SIU", "material misrepresentation", "investigation"], ("Claims examiner", "SIU analyst")),
            m("Actuarial Assumptions and Pricing", "Explain model outputs and uncertainty.", "Leadership wants a simple reason for reserve strengthening.", "Say the model says so.", "Loss development, frequency, severity, assumptions, and confidence ranges need translation.", "actuarial assumption memo", ["loss development", "frequency", "severity", "reserve adequacy"], ("Actuary", "Finance executive")),
            m("Compliance, Market Conduct, and Complaints", "Handle regulator and customer complaints precisely.", "A regulator asks about delayed claim communications.", "Say delays were isolated.", "Market-conduct rules, timelines, evidence, corrective action, and monitoring are needed.", "market-conduct response", ["market conduct", "complaint", "timely communication", "corrective action"], ("Compliance officer", "Claims director")),
        ],
        ["Policy forms, endorsements, and state insurance rules.", "Company underwriting and claims procedures.", "Compliance and legal review for coverage positions."],
    ),
    profile(
        "Banking Operations English",
        "banking-operations",
        "bank operations staff, branch managers, loan operations teams, KYC/AML analysts, fraud operations staff, payment operations teams, compliance staff, and banking leaders",
        "A banking operations English curriculum for KYC, AML, loan operations, payment exceptions, fraud, customer complaints, audits, operational risk, and regulatory communication.",
        [
            m("Account Opening and KYC", "Ask for required information without sounding suspicious or intrusive.", "A customer resists providing beneficial ownership information.", "Open the account to preserve the relationship.", "KYC, customer identification, beneficial ownership, and risk rating must be complete.", "KYC explanation script", ["KYC", "CIP", "beneficial owner", "risk rating"], ("Branch manager", "Business customer")),
            m("AML Monitoring and Suspicious Activity", "Escalate unusual activity carefully.", "A series of cash deposits appears structured.", "Tell the customer the bank is investigating them.", "Tipping-off risk, investigation, documentation, and SAR process apply.", "AML escalation note", ["AML", "structuring", "SAR", "tipping off"], ("AML analyst", "Relationship manager")),
            m("Loan Operations and Documentation", "Coordinate closing conditions and exceptions.", "A commercial loan is scheduled to close but documents are incomplete.", "Close now and collect documents later.", "Conditions precedent, collateral, authority, and exception approval must be reviewed.", "loan closing exception memo", ["loan boarding", "collateral", "condition precedent", "exception"], ("Loan operations lead", "Relationship manager")),
            m("Payment Operations and Exceptions", "Communicate payment delays with precise status language.", "A wire transfer is held for sanctions screening.", "Tell the customer it is delayed for compliance.", "Screening, investigation status, release authority, and customer messaging must be controlled.", "payment hold update", ["wire transfer", "ACH", "sanctions screening", "exception queue"], ("Payments analyst", "Branch staff")),
            m("Fraud Operations and Customer Escalation", "Balance customer empathy with fraud controls.", "A customer insists a disputed debit should be refunded immediately.", "Refund it to calm the customer.", "Provisional credit, investigation timelines, evidence, and regulatory rights matter.", "fraud dispute script", ["fraud claim", "provisional credit", "chargeback", "dispute"], ("Fraud operations specialist", "Customer")),
            m("Operational Risk and Controls", "Discuss control failures without hiding exposure.", "A reconciliation control was missed for two months.", "Mark it remediated after one correction.", "Impact assessment, root cause, control redesign, and evidence are required.", "control-gap remediation", ["operational risk", "control", "reconciliation", "remediation"], ("Risk manager", "Operations owner")),
            m("Audit and Regulatory Exams", "Answer exam questions with evidence and ownership.", "An examiner requests proof of complaint handling.", "Say the process exists.", "Documentation, sample evidence, timing, owner, and corrective action must be ready.", "exam response tracker", ["examiner", "audit evidence", "finding", "management response"], ("Compliance manager", "Operations director")),
            m("Customer Complaints and Fair Treatment", "Resolve complaints without unauthorized promises.", "A customer alleges unfair fees.", "Waive all fees immediately.", "Fee schedule, disclosures, error resolution, fairness, and escalation path need review.", "complaint resolution summary", ["complaint", "fee disclosure", "error resolution", "fair treatment"], ("Complaint manager", "Branch manager")),
        ],
        ["Bank policies, KYC/AML procedures, and regulator guidance.", "Payment rules and sanctions-screening procedures.", "Audit, complaint, and operational-risk frameworks."],
    ),
    profile(
        "Retail and E-Commerce English",
        "retail-ecommerce",
        "retail managers, e-commerce teams, merchandising staff, store operations leaders, fulfillment teams, customer service managers, marketplace sellers, and growth operators",
        "A retail and e-commerce English curriculum for merchandising, pricing, inventory, fulfillment, marketplaces, customer complaints, returns, conversion metrics, promotions, and vendor coordination.",
        [
            m("Merchandising and Assortment Planning", "Discuss assortment choices using customer, margin, and inventory language.", "A buyer wants to add many new SKUs before holiday season.", "Approve the assortment expansion.", "Shelf space, demand signal, margin, inventory risk, and vendor capacity need review.", "assortment decision memo", ["assortment", "SKU", "sell-through", "gross margin"], ("Merchant", "Category manager")),
            m("Pricing, Promotions, and Margin", "Explain discount strategy beyond top-line sales.", "A promotion drives revenue but margin falls sharply.", "Repeat the promotion because sales increased.", "Gross margin, cannibalization, inventory, customer acquisition, and brand impact matter.", "promotion readout", ["markdown", "promotion", "gross margin", "cannibalization"], ("Pricing analyst", "Marketing manager")),
            m("Inventory, Allocation, and Replenishment", "Balance stock availability with working capital.", "A hot item is stocked out in stores but overstocked online.", "Transfer everything immediately.", "Allocation, demand, lead time, logistics cost, and service level require planning.", "replenishment action plan", ["allocation", "replenishment", "stockout", "inventory turn"], ("Planner", "Store operations lead")),
            m("Fulfillment, Shipping, and Returns", "Communicate order problems with clear recovery options.", "A warehouse backlog delays guaranteed delivery dates.", "Send a general apology.", "Order status, carrier capacity, customer promise, refund policy, and service recovery matter.", "fulfillment delay script", ["fulfillment", "SLA", "return rate", "carrier"], ("E-commerce operations lead", "Customer service manager")),
            m("Conversion, UX, and Digital Analytics", "Discuss website performance using funnel language.", "Checkout conversion drops after a redesign.", "Assume customers dislike the new look.", "Instrumentation, device mix, payment errors, and funnel step drop-off need analysis.", "conversion diagnosis", ["conversion rate", "funnel", "cart abandonment", "A/B test"], ("E-commerce analyst", "UX lead")),
            m("Marketplace and Vendor Management", "Hold marketplace or vendor partners accountable.", "A vendor ships late and product ratings fall.", "Threaten to delist them immediately.", "Scorecards, SLA, customer impact, inventory, and remediation plan need review.", "vendor scorecard update", ["marketplace", "vendor scorecard", "SLA", "defect rate"], ("Marketplace manager", "Vendor")),
            m("Customer Service and Escalations", "Respond to angry customers without policy chaos.", "A customer demands a refund outside the return window.", "Make an exception for anyone who complains loudly.", "Policy, goodwill, fraud risk, and customer lifetime value need balanced judgment.", "escalation response", ["return policy", "goodwill credit", "chargeback", "customer lifetime value"], ("Customer service lead", "Customer")),
            m("Store Operations and Omnichannel Execution", "Coordinate store, online, and fulfillment workflows.", "Buy-online-pickup-in-store orders are not ready on time.", "Tell stores to prioritize online orders over walk-ins.", "Labor, inventory accuracy, queue management, and customer expectations all matter.", "omnichannel operations brief", ["BOPIS", "inventory accuracy", "queue", "labor model"], ("Store manager", "Omnichannel lead")),
        ],
        ["Company pricing, returns, and marketplace policies.", "Consumer-protection and privacy requirements.", "Vendor contracts and fulfillment SLAs."],
    ),
    profile(
        "Media and Entertainment English",
        "media-entertainment",
        "producers, production managers, creative executives, rights coordinators, distribution teams, talent managers, marketing staff, and media operations professionals",
        "A media and entertainment English curriculum for creative development, production planning, rights, talent, distribution, audience metrics, sponsorship, brand safety, and high-pressure creative disagreement.",
        [
            m("Creative Briefs and Development Notes", "Give creative feedback that is specific and usable.", "A client says a concept does not feel premium.", "Tell the creative team to make it better.", "Audience, tone, brand fit, budget, and deliverables need concrete direction.", "creative feedback note", ["creative brief", "tone", "brand fit", "deliverable"], ("Creative director", "Producer")),
            m("Production Planning and Budget", "Discuss creative ambition against schedule and cost.", "A director adds a complex scene late in pre-production.", "Approve it to protect the creative vision.", "Budget, crew, location, safety, permits, and post-production impact need review.", "production impact memo", ["production budget", "call sheet", "location", "permit"], ("Line producer", "Director")),
            m("Rights, Clearances, and Licensing", "Set boundaries around music, footage, images, and likeness.", "An editor uses a popular song in a rough cut.", "Keep it because it improves the scene.", "Clearance, territory, duration, platform, and budget must be confirmed.", "clearance risk response", ["rights", "clearance", "license", "territory"], ("Rights coordinator", "Editor")),
            m("Talent, Contracts, and Approvals", "Communicate approval rights and contractual limits.", "A talent representative objects to a promotional edit.", "Ignore the objection because the spot is finished.", "Contract terms, approval rights, likeness use, and release timing matter.", "talent approval update", ["talent agreement", "approval right", "likeness", "release"], ("Talent manager", "Marketing producer")),
            m("Distribution and Windowing", "Explain release strategy and platform constraints.", "A partner wants simultaneous release across all channels.", "Agree if it increases reach.", "Windowing, exclusivity, rights, platform economics, and audience strategy need review.", "distribution strategy note", ["windowing", "exclusivity", "platform", "rights window"], ("Distribution lead", "Platform partner")),
            m("Audience Metrics and Performance", "Interpret viewership without overclaiming success.", "A pilot has strong social buzz but weak completion.", "Call it a hit.", "Reach, completion, retention, demographic fit, and benchmark matter.", "audience performance readout", ["reach", "completion rate", "retention", "audience segment"], ("Audience insights lead", "Creative executive")),
            m("Sponsorship, Brand Safety, and Integration", "Balance sponsor needs with audience trust.", "A sponsor wants more visible product placement.", "Add more shots in the final cut.", "Editorial integrity, brand safety, contractual deliverables, and audience reaction matter.", "sponsorship integration response", ["brand safety", "product placement", "deliverable", "makegood"], ("Partnerships manager", "Showrunner")),
            m("Crisis Response and Public Statements", "Respond to controversy without premature admissions.", "A clip is criticized online before the full context is known.", "Post an apology immediately.", "Facts, legal review, stakeholder impact, tone, and timing need coordination.", "crisis holding statement", ["public statement", "backlash", "legal review", "holding statement"], ("Communications lead", "Executive producer")),
        ],
        ["Contracts, rights documents, and clearance records.", "Platform and distribution agreements.", "Brand safety, communications, and legal review procedures."],
    ),
    profile(
        "Telecommunications English",
        "telecommunications",
        "network operations staff, telecom engineers, field technicians, customer operations teams, product managers, regulatory staff, and telecom project leaders",
        "A telecommunications English curriculum for network reliability, outages, fiber and wireless deployment, service provisioning, field operations, regulatory issues, customer escalations, and technical coordination.",
        [
            m("Network Operations and Outage Bridges", "Communicate service impact and restoration estimates.", "A regional outage affects enterprise customers.", "Give a restoration time before diagnosis is complete.", "Fault isolation, affected services, redundancy, field dispatch, and ETA confidence matter.", "outage bridge update", ["NOC", "outage", "fault isolation", "ETA"], ("NOC manager", "Enterprise support lead")),
            m("Fiber Deployment and Construction Coordination", "Explain deployment constraints across permits, crews, and make-ready work.", "A sales team promises service before fiber construction is complete.", "Keep the promise and push construction.", "Permits, pole access, make-ready, splicing, and testing affect timeline.", "fiber deployment status", ["fiber", "make-ready", "splicing", "permit"], ("Deployment manager", "Sales director")),
            m("Wireless Capacity and Coverage", "Discuss network performance without oversimplifying bars or speed.", "A customer complains that 5G coverage is unreliable indoors.", "Say coverage maps show service.", "Spectrum, building penetration, congestion, device type, and site density matter.", "coverage explanation", ["spectrum", "coverage", "capacity", "congestion"], ("RF engineer", "Account manager")),
            m("Provisioning and Service Activation", "Coordinate order flow and activation dates.", "A circuit is sold but not provisioned by the target date.", "Tell the customer activation is pending.", "Order status, dependencies, testing, CPE, and carrier coordination need clarity.", "activation delay update", ["provisioning", "CPE", "circuit", "service activation"], ("Provisioning coordinator", "Customer success manager")),
            m("Field Service and Dispatch", "Handle repeat truck rolls and customer frustration.", "A technician returns for a third visit to the same site.", "Send another tech without deeper review.", "Root cause, equipment, signal levels, inside wiring, and dispatch notes need analysis.", "repeat-dispatch review", ["truck roll", "signal level", "dispatch", "inside wiring"], ("Field supervisor", "Support agent")),
            m("Regulatory and Emergency Services", "Explain obligations around emergency calling and lawful requirements.", "A product change may affect emergency call routing.", "Launch and monitor issues.", "Testing, regulatory obligations, customer notice, and risk review are required.", "regulatory readiness note", ["E911", "lawful intercept", "regulatory filing", "customer notice"], ("Regulatory manager", "Product manager")),
            m("Customer Churn and Service Recovery", "Discuss retention offers without hiding root causes.", "A major account threatens to leave after repeated outages.", "Offer a discount immediately.", "SLA credits, root cause, reliability plan, account trust, and executive ownership matter.", "retention recovery plan", ["churn", "SLA credit", "root cause", "service assurance"], ("Account director", "Network operations")),
            m("Vendor and Equipment Lifecycle", "Manage network vendor risk and end-of-life planning.", "A vendor announces end of support for core equipment.", "Delay replacement until failure.", "Lifecycle risk, spares, maintenance, interoperability, and capital planning need review.", "equipment lifecycle brief", ["end of support", "interoperability", "spares", "capital plan"], ("Network architect", "Procurement lead")),
        ],
        ["Network operations procedures and service-level commitments.", "FCC or local telecom regulatory obligations.", "Vendor lifecycle and field-service documentation."],
    ),
    profile(
        "Government and Public Administration English",
        "government-public-administration",
        "public administrators, agency program managers, policy analysts, procurement staff, constituent-service teams, grants managers, and interagency coordinators",
        "A public-administration English curriculum for policy implementation, public meetings, procurement, grants, interagency coordination, constituent communication, transparency, and bureaucratic nuance.",
        [
            m("Policy Implementation and Program Rules", "Explain policy choices within legal and operational constraints.", "A new rule must be implemented before systems are ready.", "Announce full implementation immediately.", "Eligibility, process, staffing, technology, and public guidance need alignment.", "implementation readiness brief", ["policy", "eligibility", "implementation", "public guidance"], ("Program manager", "Policy analyst")),
            m("Public Meetings and Stakeholder Input", "Respond to public criticism with clarity and neutrality.", "Residents challenge an agency plan at a public meeting.", "Defend the agency strongly.", "Public record, process, evidence, respect, and next steps matter.", "public meeting response", ["public comment", "stakeholder", "public record", "facilitation"], ("Agency director", "Resident")),
            m("Procurement and Vendor Selection", "Use procurement language that protects fairness.", "A preferred vendor asks for early feedback before an RFP closes.", "Give informal guidance.", "Fair competition, procurement rules, evaluation criteria, and communication limits apply.", "procurement boundary response", ["RFP", "evaluation criteria", "bidder", "procurement rule"], ("Procurement officer", "Vendor")),
            m("Grants, Compliance, and Reporting", "Discuss grant performance and allowable use of funds.", "A subrecipient wants to reallocate funds quickly.", "Approve by email.", "Allowability, budget category, reporting, and amendment procedures must be checked.", "grant modification response", ["grant", "subrecipient", "allowable cost", "reporting"], ("Grants manager", "Nonprofit partner")),
            m("Interagency Coordination", "Clarify authority and ownership across agencies.", "Two agencies assume the other owns a public complaint.", "Wait for the other agency to act.", "Jurisdiction, authority, data sharing, and communication plan need definition.", "interagency action note", ["jurisdiction", "memorandum of understanding", "data sharing", "owner"], ("Agency liaison", "Program lead")),
            m("Constituent Services and Escalation", "Give helpful responses without promising outcomes outside authority.", "A constituent demands immediate action on a permit decision.", "Promise to fix it.", "Process status, appeal rights, agency authority, and respectful tone must be clear.", "constituent response", ["constituent", "casework", "appeal", "authority"], ("Constituent-services manager", "Resident")),
            m("Transparency, Records, and Ethics", "Handle requests for information and conflicts of interest.", "A staff member receives a records request involving sensitive emails.", "Forward everything quickly.", "Public-records rules, exemptions, review, and privacy need attention.", "records request triage", ["public records", "exemption", "conflict of interest", "ethics"], ("Records officer", "Program staff")),
            m("Performance Metrics and Budget Justification", "Connect public value to funding requests.", "A program wants budget growth despite mixed performance metrics.", "Highlight only success stories.", "Outcomes, equity, cost, statutory mandate, and improvement plan need balanced framing.", "budget justification memo", ["appropriation", "outcome measure", "equity", "public value"], ("Budget analyst", "Program director")),
        ],
        ["Agency policies, ethics rules, and public-records requirements.", "Procurement and grant-management regulations.", "Current statutes and implementing guidance."],
    ),
    profile(
        "Nonprofit and NGO English",
        "nonprofit-ngo",
        "nonprofit program managers, NGO staff, grant writers, development officers, monitoring and evaluation teams, field coordinators, volunteer managers, and nonprofit executives",
        "A nonprofit and NGO English curriculum for donor communication, grants, program evaluation, field operations, safeguarding, community partnerships, volunteer management, and mission-versus-budget tradeoffs.",
        [
            m("Mission, Theory of Change, and Program Design", "Connect mission language to measurable program logic.", "A donor asks how activities create outcomes.", "Use inspirational stories only.", "Inputs, activities, outputs, outcomes, assumptions, and evidence need alignment.", "theory-of-change explanation", ["mission", "theory of change", "output", "outcome"], ("Program director", "Donor")),
            m("Grant Proposals and Donor Restrictions", "Write compelling proposals while respecting restrictions.", "A funder offers money for work outside the mission.", "Accept it because funding is scarce.", "Mission fit, restricted funds, capacity, and reporting obligations need review.", "grant-fit recommendation", ["restricted funding", "deliverable", "grant proposal", "mission fit"], ("Development director", "Executive director")),
            m("Monitoring, Evaluation, and Learning", "Discuss impact evidence without overclaiming.", "A report shows improved participation but unclear outcomes.", "Call the program successful.", "Indicators, baseline, attribution, qualitative evidence, and limitations matter.", "evaluation caveat paragraph", ["indicator", "baseline", "attribution", "learning agenda"], ("M&E specialist", "Program manager")),
            m("Field Operations and Partner Coordination", "Communicate operational risk in community settings.", "A local partner cannot deliver services on the agreed timeline.", "Pressure the partner publicly.", "Local constraints, safety, community trust, budget, and contingency planning matter.", "partner recovery plan", ["implementing partner", "field visit", "contingency", "community trust"], ("Field coordinator", "Partner organization")),
            m("Safeguarding and Incident Reporting", "Escalate sensitive concerns with care.", "A volunteer reports possible misconduct by a staff member.", "Ask the staff member informally.", "Safeguarding policy, confidentiality, survivor-centered response, and investigation process apply.", "safeguarding intake note", ["safeguarding", "confidentiality", "survivor-centered", "incident report"], ("Safeguarding lead", "Volunteer manager")),
            m("Volunteer Management and Training", "Set expectations for volunteers without discouraging them.", "Volunteers want to perform tasks beyond their training.", "Let them help wherever needed.", "Role scope, training, supervision, risk, and client dignity matter.", "volunteer boundary script", ["volunteer role", "training", "supervision", "duty of care"], ("Volunteer coordinator", "Volunteer")),
            m("Advocacy, Public Messaging, and Neutrality", "Communicate advocacy positions responsibly.", "A campaign team wants to use a dramatic statistic.", "Use it because it gets attention.", "Source, context, dignity, legal status, and organizational position need review.", "advocacy message review", ["advocacy", "campaign", "dignity", "source"], ("Communications manager", "Campaign lead")),
            m("Board Reporting and Sustainability", "Present program and financial reality without panic.", "Cash runway is tightening while demand rises.", "Ask the board for emergency funds without options.", "Scenario planning, reserves, restricted funds, staffing, and mission impact need clarity.", "board sustainability update", ["board governance", "cash runway", "reserve", "scenario"], ("Executive director", "Board treasurer")),
        ],
        ["Donor agreements and grant restrictions.", "Safeguarding and incident-reporting policies.", "Monitoring, evaluation, and learning standards."],
    ),
    profile(
        "Consulting English",
        "consulting",
        "management consultants, strategy consultants, implementation consultants, analysts, engagement managers, client partners, internal consultants, and advisory teams",
        "A consulting English curriculum for discovery, hypotheses, stakeholder management, scope, executive recommendations, slide narratives, implementation risk, and client pushback.",
        [
            m("Client Discovery and Problem Definition", "Clarify the real problem before proposing work.", "A client asks for a benchmark study but describes a decision problem.", "Sell the requested benchmark.", "Decision question, stakeholders, constraints, and expected use of analysis need clarification.", "discovery question guide", ["discovery", "problem statement", "decision question", "stakeholder"], ("Client partner", "Client executive")),
            m("Hypotheses and Issue Trees", "Structure analysis without pretending certainty.", "The team has limited data but needs a workplan.", "Analyze everything.", "Hypotheses, issue tree, prioritization, and evidence plan should focus effort.", "issue-tree workplan", ["hypothesis", "issue tree", "workstream", "evidence plan"], ("Engagement manager", "Analyst")),
            m("Data Requests and Client Burden", "Ask for information efficiently and respectfully.", "The consulting team sends a long data request to a busy client.", "Ask for everything just in case.", "Data relevance, owner, confidentiality, deadline, and burden need management.", "data request prioritization", ["data request", "confidentiality", "owner", "deadline"], ("Consultant", "Client data owner")),
            m("Slide Storylines and Executive Synthesis", "Turn analysis into a clear recommendation.", "A deck has many charts but no decision narrative.", "Add more detail.", "So-what, implication, recommendation, and decision ask must be explicit.", "executive storyline", ["storyline", "so what", "recommendation", "decision ask"], ("Principal", "Consultant")),
            m("Scope Management and Change Requests", "Protect scope while staying client-service oriented.", "A client asks for an additional market study mid-project.", "Do it to keep the client happy.", "Scope, timeline, budget, value, and tradeoff need a formal conversation.", "scope-change response", ["scope", "change request", "tradeoff", "statement of work"], ("Engagement manager", "Client sponsor")),
            m("Difficult Client Feedback", "Receive criticism without losing authority.", "A client says the recommendation is not practical.", "Defend the model.", "Implementation constraints, assumptions, and client knowledge should be integrated.", "feedback recovery plan", ["assumption", "implementation constraint", "stakeholder buy-in", "iteration"], ("Client executive", "Consultant")),
            m("Implementation and Change Management", "Move from recommendation to adoption risk.", "Leadership approves a new operating model but managers resist.", "Tell managers the decision is final.", "Change story, incentives, decision rights, training, and adoption metrics matter.", "implementation risk brief", ["operating model", "change management", "adoption", "decision rights"], ("Implementation lead", "Business unit manager")),
            m("Steering Committees and Final Readouts", "Manage executive decisions and unresolved disagreement.", "Executives disagree during the final readout.", "Keep presenting the slides.", "Decision rights, options, risks, and next-step ownership need facilitation.", "steering committee close", ["steering committee", "option set", "risk", "next step"], ("Partner", "Executive sponsor")),
        ],
        ["Statement of work and client confidentiality terms.", "Firm quality standards and slide-review practices.", "Client data-governance and decision-making protocols."],
    ),
    profile(
        "Sales and Business Development English",
        "sales-business-development",
        "account executives, business-development representatives, sales managers, partnership teams, solutions consultants, channel managers, and revenue leaders",
        "A sales and business development English curriculum for discovery, qualification, objection handling, pricing, procurement, enterprise buying committees, negotiation, partnership language, and CRM discipline.",
        [
            m("Discovery and Qualification", "Ask business questions before pitching features.", "A prospect asks for a demo before explaining their problem.", "Show the full demo immediately.", "Pain, priority, authority, timeline, and business impact need qualification.", "discovery call plan", ["discovery", "qualification", "pain point", "buying process"], ("Account executive", "Prospect")),
            m("Value Proposition and Use-Case Fit", "Connect product value to the buyer's actual workflow.", "A prospect likes the product but cannot name a use case.", "Push for next steps anyway.", "Use case, stakeholder value, success metric, and urgency need definition.", "value mapping note", ["value proposition", "use case", "success metric", "stakeholder"], ("Solutions consultant", "Account executive")),
            m("Objection Handling and Competitive Pressure", "Respond to objections without sounding defensive.", "A prospect says a competitor is cheaper.", "Discount immediately.", "Total value, risk, scope, implementation, and commercial terms need comparison.", "competitive objection response", ["objection", "competitor", "differentiator", "total cost"], ("Sales manager", "Prospect")),
            m("Pricing, Discounting, and Approval", "Negotiate price without eroding value.", "Procurement demands a last-minute discount.", "Approve it to close the quarter.", "Pricing policy, margin, term length, volume, and approval path must be reviewed.", "discount approval request", ["discount", "procurement", "margin", "approval path"], ("Account executive", "Revenue operations")),
            m("Enterprise Buying Committees", "Navigate multiple stakeholders and hidden blockers.", "A champion says the deal is done but legal has not reviewed it.", "Forecast the deal as committed.", "Decision criteria, legal, security, finance, and executive sponsor status matter.", "deal-risk update", ["champion", "economic buyer", "buying committee", "forecast category"], ("Sales director", "Account executive")),
            m("Negotiation and Contract Redlines", "Keep commercial momentum while respecting legal boundaries.", "A customer requests unlimited liability in the contract.", "Agree because it is a strategic deal.", "Risk allocation, legal approval, insurance, and business value need decision.", "redline escalation", ["redline", "liability", "indemnity", "commercial term"], ("Account executive", "Legal counsel")),
            m("Partnerships and Channel Development", "Define partnership value and responsibilities.", "A potential partner wants exclusivity before proving pipeline.", "Grant exclusivity to secure the relationship.", "Territory, targets, enablement, economics, and performance gates need clarity.", "partner term outline", ["channel partner", "exclusivity", "pipeline", "enablement"], ("Business-development lead", "Partner")),
            m("CRM Hygiene and Pipeline Reviews", "Discuss pipeline honestly under target pressure.", "A rep keeps stale opportunities in late stages.", "Leave them because the pipeline looks stronger.", "Next step, close date, buyer evidence, and risk should drive forecast accuracy.", "pipeline inspection notes", ["CRM", "pipeline", "close date", "commit", "slippage"], ("Sales manager", "Account executive")),
        ],
        ["Company sales process, approval matrix, and pricing policy.", "Contract review and procurement procedures.", "CRM definitions and forecast governance."],
    ),
    profile(
        "Customer Success English",
        "customer-success",
        "customer success managers, account managers, onboarding specialists, support escalation leads, renewals managers, implementation teams, and post-sale revenue leaders",
        "A customer success English curriculum for onboarding, adoption, health scoring, escalations, QBRs, renewals, churn risk, difficult customers, product feedback, and expansion conversations.",
        [
            m("Onboarding and Implementation Expectations", "Set realistic timelines and responsibilities after the sale.", "A customer expects go-live in two weeks despite incomplete data.", "Promise the date to maintain excitement.", "Scope, data readiness, customer owner, training, and risk need alignment.", "onboarding expectation reset", ["onboarding", "go-live", "implementation", "customer owner"], ("Onboarding manager", "Customer sponsor")),
            m("Adoption Metrics and Health Scores", "Discuss account health without reducing it to one number.", "Usage is high but key stakeholders are disengaged.", "Mark the account healthy.", "Depth of adoption, business outcomes, sponsor engagement, and support trends matter.", "account health analysis", ["adoption", "health score", "stakeholder engagement", "usage"], ("CSM", "Renewals manager")),
            m("Support Escalations and Incident Communication", "Coordinate urgent customer issues across support and product.", "A strategic customer has a recurring defect.", "Promise engineering will fix it this week.", "Severity, workaround, reproduction, priority, and communication cadence need agreement.", "escalation update", ["escalation", "severity", "workaround", "SLA"], ("Support lead", "Customer success manager")),
            m("QBRs and Business Outcomes", "Run business reviews that connect product use to value.", "A QBR deck lists activity but no outcomes.", "Add more usage charts.", "Customer goals, outcomes, risks, recommendations, and executive asks should guide the story.", "QBR narrative", ["QBR", "business outcome", "ROI", "executive sponsor"], ("CSM", "Customer executive")),
            m("Renewals and Churn Risk", "Talk about renewal risk early and specifically.", "A customer delays renewal conversations and complains about value.", "Offer a discount.", "Adoption gaps, unresolved issues, executive alignment, and commercial terms need a recovery plan.", "renewal risk plan", ["renewal", "churn risk", "commercial term", "value gap"], ("Renewals manager", "Customer sponsor")),
            m("Expansion and Upsell Ethics", "Recommend expansion only when value is credible.", "Sales wants to upsell before the customer is live.", "Pitch the expansion anyway.", "Readiness, value proof, use case, and customer trust must be considered.", "expansion readiness note", ["upsell", "expansion", "use case", "readiness"], ("Account manager", "CSM")),
            m("Product Feedback and Feature Requests", "Translate customer requests into product evidence.", "A customer says a missing feature is a deal breaker.", "Demand that product build it.", "Segment fit, revenue impact, workaround, frequency, and roadmap tradeoff need assessment.", "feature request brief", ["feature request", "roadmap", "workaround", "product feedback"], ("CSM", "Product manager")),
            m("Difficult Customers and Boundary Setting", "Stay calm when customers are angry or unrealistic.", "A customer threatens escalation unless all issues are fixed by tomorrow.", "Accept the demand.", "Priority, feasibility, contractual commitments, and respectful boundaries need clear communication.", "customer boundary script", ["boundary", "executive escalation", "commitment", "expectation setting"], ("Customer success director", "Customer")),
        ],
        ["Customer contracts, SLAs, and support policies.", "Company renewal, escalation, and product-feedback procedures.", "CRM and health-score definitions."],
    ),
    profile(
        "Legal Operations and Compliance English",
        "legal-operations-compliance",
        "legal operations staff, compliance managers, contract managers, policy owners, audit teams, investigation coordinators, privacy operations staff, and risk professionals",
        "A legal operations and compliance English curriculum for contract workflow, policy implementation, audits, controls, investigations, privacy requests, training, third-party risk, and governance communication.",
        [
            m("Contract Intake and Workflow", "Clarify legal requests before they become bottlenecks.", "A business team marks every contract urgent.", "Prioritize by who is loudest.", "Risk, value, deadline, template deviation, and approval path should drive triage.", "contract intake triage", ["contract intake", "template", "approval path", "triage"], ("Legal operations manager", "Sales operations")),
            m("Policy Implementation and Controls", "Turn policy language into operational behavior.", "A new policy is published but teams do not follow it.", "Send a reminder email.", "Process ownership, controls, training, monitoring, and escalation need design.", "policy rollout plan", ["policy", "control", "monitoring", "process owner"], ("Compliance manager", "Business owner")),
            m("Compliance Audits and Evidence", "Respond to audits with evidence, not informal assurance.", "An auditor asks for proof of approval reviews.", "Say approvals happen in email.", "Evidence location, retention, sample quality, and control design must be shown.", "audit evidence tracker", ["audit", "evidence", "retention", "sample"], ("Audit lead", "Process owner")),
            m("Internal Investigations", "Coordinate investigations with neutrality and confidentiality.", "A manager wants to know who made a hotline complaint.", "Share the name privately.", "Confidentiality, non-retaliation, evidence, and investigative independence matter.", "investigation boundary response", ["hotline", "non-retaliation", "confidentiality", "evidence"], ("Investigation coordinator", "Manager")),
            m("Privacy Operations and Data Requests", "Handle data requests with process discipline.", "A customer asks for deletion of personal data across systems.", "Delete the visible profile only.", "Identity verification, system inventory, exceptions, and response timelines matter.", "privacy request plan", ["data subject request", "personal data", "verification", "exception"], ("Privacy operations lead", "Support manager")),
            m("Third-Party Risk and Due Diligence", "Explain vendor risk without blocking business unnecessarily.", "A team wants to onboard a vendor that processes sensitive data.", "Approve after a quick demo.", "Security, privacy, contract terms, data location, and monitoring need review.", "vendor risk assessment", ["third-party risk", "due diligence", "data processing", "vendor questionnaire"], ("Compliance analyst", "Procurement manager")),
            m("Training, Attestations, and Culture", "Make compliance training practical, not ceremonial.", "Employees complete training but keep asking basic policy questions.", "Require another training module.", "Role-based examples, manager reinforcement, attestations, and controls should be aligned.", "training improvement memo", ["attestation", "role-based training", "culture", "reinforcement"], ("Compliance training lead", "HR partner")),
            m("Governance, Reporting, and Risk Committees", "Present compliance risk with decisions and owners.", "A committee receives a long list of issues with no prioritization.", "Review every item in order.", "Severity, trend, root cause, owner, deadline, and risk acceptance should drive governance.", "risk committee update", ["governance", "risk committee", "risk acceptance", "remediation"], ("Chief compliance officer", "Legal operations lead")),
        ],
        ["Company legal, compliance, privacy, and contract procedures.", "Current legal counsel guidance for regulated activities.", "Audit, investigation, and third-party-risk frameworks."],
    ),
]


TERM_MEANING_RULES = [
    (("rate", "ratio", "margin", "yield", "score", "index", "turnover", "variance", "runway"), "a measurable indicator used to quantify performance, exposure, capacity, quality, or change over time"),
    (("plan", "roadmap", "strategy", "program", "agenda", "playbook"), "a structured course of action that assigns priorities, sequencing, assumptions, and responsible roles"),
    (("policy", "standard", "protocol", "procedure", "guideline", "requirement", "criteria"), "an approved rule or decision framework that sets what is permitted, required, or acceptable"),
    (("audit", "review", "assessment", "analysis", "inspection", "evaluation", "study"), "a structured examination of evidence, process, or results used to reach a defensible conclusion"),
    (("report", "memo", "brief", "notice", "statement", "update", "readout", "letter"), "a workplace communication artifact that records facts, interpretation, and the decision or action requested"),
    (("request", "intake", "referral", "ticket", "order", "submission", "filing"), "a formal intake or routing mechanism that starts work, seeks a decision, or transfers responsibility"),
    (("evidence", "record", "log", "trail", "documentation", "provenance", "traceability"), "information that can be checked to support a claim, decision, investigation, or compliance conclusion"),
    (("risk", "hazard", "threat", "exposure", "failure", "defect", "incident", "exception", "deviation"), "a condition or event that can create harm, loss, noncompliance, delay, or unacceptable performance"),
    (("control", "monitoring", "validation", "verification", "assurance", "safeguard", "check"), "a repeatable control mechanism used to prevent, detect, or confirm conditions before work proceeds"),
    (("contract", "agreement", "term sheet", "license", "endorsement", "waiver", "indemnity"), "a negotiated legal or commercial arrangement that allocates rights, obligations, remedies, or risk"),
    (("data", "metric", "dashboard", "model", "cohort", "sample", "signal", "attribution"), "a defined information asset or analytical construct used to measure, explain, or predict an outcome"),
    (("capacity", "staffing", "inventory", "allocation", "schedule", "queue", "throughput", "lead time"), "an operational constraint that affects how much work can be completed, by whom, and by when"),
    (("customer", "client", "patient", "guest", "student", "employee", "vendor", "supplier", "partner"), "a stakeholder category whose needs, eligibility, experience, or obligations affect the decision"),
    (("quality", "safety", "security", "privacy", "compliance", "ethics", "reliability"), "a performance or governance dimension that must be protected through defined evidence, thresholds, and accountability"),
    (("training", "onboarding", "enablement", "attestation", "credential", "competency"), "a capability or authorization process used to prepare, verify, or document that a person can perform a role"),
    (("governance", "committee", "approval", "authority", "decision rights", "RACI", "owner"), "a decision-accountability mechanism that clarifies who recommends, approves, performs, and accepts risk"),
    (("design", "specification", "drawing", "blueprint", "architecture", "interface", "configuration"), "a controlled description of how a product, service, system, or built asset is intended to work"),
    (("claim", "message", "voice", "campaign", "creative", "positioning", "audience"), "a communication or market-facing element that must match evidence, audience, channel, and approval boundaries"),
]


def _contextual_term_definition(term: str, prof: dict, module: dict) -> str:
    lower = term.casefold()
    purpose = next(
        (meaning for triggers, meaning in TERM_MEANING_RULES if any(trigger in lower for trigger in triggers)),
        "a field-specific concept used to locate the relevant fact, boundary, or decision variable",
    )
    skill = module["skill"].rstrip(".")
    industry = prof["title"].replace(" English", "").lower()
    return (
        f"In {industry}, {term} is {purpose}. "
        f"Use it when teams need to {skill[:1].lower() + skill[1:]}."
    )


def term_definition(term: str, prof: dict, module: dict) -> str:
    if term in prof.get("term_definitions", {}):
        return prof["term_definitions"][term]
    if term in TERM_DEFINITIONS:
        return TERM_DEFINITIONS[term]
    return _contextual_term_definition(term, prof, module)


def pdf_name(prof: dict, kind: str) -> str:
    return f"efsp-{prof['slug']}-{kind}.pdf"


def cover(prof: dict, doc_title: str, subtitle: str) -> list:
    return [
        Spacer(1, 0.9 * inch),
        p("EFSP Auxiliary ESL Curriculum", "CoverKicker"),
        Paragraph(esc(doc_title), S["CoverTitle"]),
        Paragraph(esc(subtitle), S["CoverSub"]),
        Spacer(1, 0.25 * inch),
        box(
            f"Audience: {prof['roles']}",
            [
                f"Focus: {prof['summary']}",
                "Designed for advanced ESL learners who already use professional English and need industry-specific terminology, realistic meetings, role-play pressure, careful pushback, and polished workplace outputs.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * inch),
        p(
            "Teaching stance: this is language and workplace-communication training, not legal, medical, financial, safety, or regulatory advice. Instructors should connect every scenario to the learner's current company policies, local rules, and approved procedures.",
            "Small",
        ),
        PageBreak(),
    ]


def add_course_opening(story: list, prof: dict) -> None:
    story += h1("Purpose and Course Logic")
    story.append(p(prof["summary"]))
    story.append(
        box(
            "Core language challenge",
            [
                "Advanced learners do not only need vocabulary. They need the ability to ask which standard applies, who owns the decision, what evidence is sufficient, what risk is being accepted, and how to disagree without sounding vague, defensive, or reckless.",
                "Each module trains a realistic workplace pressure point with role-specific terms, decision language, pushback practice, and bounded decision activities learners can apply to their own work.",
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(
        bullets(
            [
                f"Use {prof['title'].replace(' English', '').lower()} terminology accurately in meetings, written updates, handoffs, escalations, reviews, and client or stakeholder conversations.",
                "Turn vague requests into specific questions about evidence, owner, deadline, constraint, risk, and decision rights.",
                "Push back on unsafe, unsupported, noncompliant, unrealistic, or poorly scoped proposals while preserving professional trust.",
                "Handle realistic dialogues from the field, including conflict, uncertainty, documentation gaps, customer or stakeholder pressure, and cross-functional disagreement.",
                "Select language that produces concise workplace outputs: briefing notes, escalation updates, meeting scripts, risk memos, decision records, and follow-up messages.",
            ]
        )
    )


def add_module_plans(story: list, prof: dict) -> None:
    story += h1("Instructor Module Plans")
    for index, module in enumerate(prof["modules"], start=1):
        story.append(h2(f"Module {index}. {module['title']} (90 minutes)"))
        story.append(p(module["skill"]))
        story.append(h3("Learners should be able to"))
        story.append(
            bullets(
                [
                    f"Use these terms accurately: {', '.join(module['terms'])}.",
                    f"Explain the workplace tension: {module['constraint']}",
                    f"Respond professionally when a stakeholder says: {module['pressure']}",
                    f"Select the evidence, tradeoff, owner, and decision required for a {module['output']}.",
                ]
            )
        )
        story.append(h3("Customized scenario"))
        story.append(box("Workplace pressure", [module["scenario"], module["pressure"], module["constraint"]], "green"))
        story.append(h3("Classroom sequence"))
        story.append(
            bullets(
                [
                    "Terminology selection: distinguish the term that names the decision variable from three plausible alternatives.",
                    "Risk triage: select the stakeholder, decision, evidence gap, operating constraint, and cost of being wrong from a bounded scenario set.",
                    "Pushback ladder: choose the strongest sequence from clarification to evidence-based objection to consequence to decision request.",
                    f"Decision artifact check: select the facts, caveat, owner, and next action that belong in a {module['output']}.",
                ],
                numbered=True,
            )
        )


def add_jargon(story: list, prof: dict) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "These are classroom working definitions. Learners should adapt wording to their organization's policies, systems, and local regulatory environment."
        )
    )
    for module in prof["modules"]:
        story.append(h2(module["title"]))
        rows = [["Term", "Working meaning", "Collocations", "Contrast and workplace line"]]
        for term in module["terms"]:
            card = term_learning_fields(term, term_definition(term, prof, module), module["scenario"])
            rows.append(
                [
                    term,
                    card["definition"],
                    "; ".join(card["collocations"]),
                    f"Contrast: {card['contrast']}\nExample: {card['example']}",
                ]
            )
        story.append(table(rows, [1.15 * inch, 2.25 * inch, 1.35 * inch, CONTENT_WIDTH - 4.75 * inch]))


def add_phrase_bank(story: list, prof: dict) -> None:
    story += h1("Industry-Specific Meeting Moves")
    rows = [["Situation", "Useful language"]]
    for module in prof["modules"]:
        rows.append(
            [
                module["title"],
                f"Before we commit, I want to confirm {module['terms'][0]}, {module['terms'][1]}, the owner, and the evidence behind the decision. If {module['constraint'].lower()}, I recommend we document the risk and agree on the next step.",
            ]
        )
    story.append(table(rows, [2.1 * inch, CONTENT_WIDTH - 2.1 * inch]))
    story.append(h2("High-pressure pushback frames"))
    story.append(
        bullets(
            [
                "I understand the urgency. The risk is that we move faster than the evidence or process supports.",
                "I am not blocking the goal. I am naming the condition we need before the decision is safe and credible.",
                "If we accept this risk, we should name the owner, document the assumption, and define the trigger for escalation.",
                "That may be possible, but not under the current scope, timeline, or approval path.",
                "Let's separate what we know, what we assume, and what still needs confirmation.",
            ]
        )
    )


def chunks(items: list, size: int) -> list[list]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def add_practical_collocations(story: list, prof: dict) -> None:
    collocations = prof.get("collocations", [])
    if not collocations:
        return
    story += h1("Practical Collocations and Field Moves")
    story.append(
        p(
            "These phrases are intentionally practical. Learners should rehearse them as complete workplace moves: what they mean, when to use them, what evidence they require, and what decision they support."
        )
    )
    for index, group in enumerate(chunks(collocations, 10), start=1):
        story.append(h2(f"Collocation set {index}"))
        rows = [["Collocation", "How it works in the field"]]
        rows.extend([[phrase, use] for phrase, use in group])
        story.append(table(rows, [1.85 * inch, CONTENT_WIDTH - 1.85 * inch]))


def add_specialized_nomenclature(story: list, prof: dict) -> None:
    nomenclature = prof.get("nomenclature", [])
    if not nomenclature:
        return
    story += h1("Specialized Nomenclature Expansion")
    story.append(
        p(
            "Use this expansion set for learners who already know the general module terms and need the more specific nouns, acronyms, and measurement language that appear in fab, test, packaging, reliability, and customer-quality conversations."
        )
    )
    by_category: dict[str, list[tuple[str, str]]] = {}
    for category, term, meaning in nomenclature:
        by_category.setdefault(category, []).append((term, meaning))
    for category, items in by_category.items():
        story.append(h2(category))
        rows = [["Term", "Working meaning"]]
        rows.extend([[term, meaning] for term, meaning in items])
        story.append(table(rows, [1.45 * inch, CONTENT_WIDTH - 1.45 * inch]))


def add_expanded_dialogues(story: list, prof: dict) -> None:
    dialogues = prof.get("dialogues", [])
    if not dialogues:
        return
    story += h1("Additional Practical Dialogues")
    story.append(
        p(
            "These dialogues are written for advanced role-play. Learners should practice the first version as written, then replace the technical facts with a similar problem from their own role."
        )
    )
    for index, dialogue in enumerate(dialogues, start=1):
        story.append(h2(f"{index}. {dialogue['title']}"))
        story.append(box("Setting", [dialogue["setting"]], "blue"))
        rows = [["Speaker", "Line"]]
        rows.extend([[speaker, line] for speaker, line in dialogue["turns"]])
        story.append(table(rows, [1.55 * inch, CONTENT_WIDTH - 1.55 * inch]))
        story.append(h3("Coach notes"))
        story.append(bullets(dialogue.get("coach_notes", [])))
        if dialogue.get("collocations"):
            story.append(h3("Target collocations"))
            story.append(bullets(dialogue["collocations"]))


def add_participant_practical_drills(story: list, prof: dict, answer_key: list[dict[str, str]]) -> None:
    collocations = prof.get("collocations", [])
    dialogues = prof.get("dialogues", [])
    nomenclature = prof.get("nomenclature", [])
    if not (collocations or dialogues or nomenclature):
        return
    story += h1("Practical Semiconductor Language Lab")
    story.append(
        p(
            "Use these guided selections to practice the exact language used in fab, yield, qualification, and foundry conversations. Each answer is bounded by the situation and includes a rationale in the answer key."
        )
    )
    if collocations:
        story.append(h2("Collocation completion"))
        add_cloze_exercise(
            story,
            make_dialogue_cloze(
                {
                    "title": "Lot release language",
                    "setting": "A customer is asking for an urgent shipment update while the lot remains under review.",
                    "dialogue": [
                        ("Customer program manager", "Can we promise shipment today?"),
                        ("ESL learner", "Before we release the lot, we need to confirm the evidence, owner, and decision condition."),
                    ],
                    "notes": ["release is the controlled act of allowing held material to continue through the approved route."],
                },
                [phrase for phrase, _use in collocations],
            ),
            answer_key,
        )
    if dialogues:
        story.append(h2("Additional dialogue completions"))
        for dialogue in dialogues[:3]:
            add_cloze_exercise(story, make_dialogue_cloze(dialogue), answer_key)
    if nomenclature:
        story.append(h2("Nomenclature completion"))
        target_term = nomenclature[0][1]
        add_cloze_exercise(
            story,
            make_dialogue_cloze(
                {
                    "title": "Fab logistics terminology",
                    "setting": "An operator is preparing material for the next approved process step.",
                    "dialogue": [
                        ("Manufacturing lead", "How will the wafers move through the automated bay?"),
                        ("ESL learner", f"The wafers will remain in the {target_term} until the approved route and tool are confirmed."),
                    ],
                    "notes": [f"{target_term} is the logistics term used for this controlled wafer-handling context."],
                },
                [term for _category, term, _meaning in nomenclature],
            ),
            answer_key,
        )


def add_assessment(story: list, prof: dict) -> None:
    story += h1("Assessment and Coaching")
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but uses them loosely.", "Uses field terms accurately in context.", "Defines terms, connects them to evidence, and explains decision impact."],
                ["Pushback", "Disagrees vaguely or avoids disagreement.", "Names concern with evidence and next step.", "Balances urgency, relationship, risk, owner, and decision rights."],
                ["Scenario judgment", "Focuses on one stakeholder's preference.", "Identifies constraint, risk, and process.", "Guides the group toward a documented, realistic decision."],
                ["Decision communication", "Selects language without linking it to the decision.", "Chooses language that names facts, owner, and next step.", "Distinguishes evidence, tradeoff, authority, and escalation in a decision-ready response."],
            ],
            [1.2 * inch, 1.85 * inch, 1.95 * inch, 2.0 * inch],
        )
    )
    story.append(h2("Source orientation"))
    story.append(bullets(prof["sources"] + ["The learner's own company policies, SOPs, contracts, systems, templates, and approved communication standards."]))


def instructor_guide(prof: dict) -> Path:
    story = cover(
        prof,
        prof["title"],
        f"Instructor guide for advanced ESL learners working in {prof['title'].replace(' English', '').lower()}",
    )
    add_course_opening(story, prof)
    add_module_plans(story, prof)
    add_jargon(story, prof)
    add_phrase_bank(story, prof)
    add_practical_collocations(story, prof)
    add_expanded_dialogues(story, prof)
    add_specialized_nomenclature(story, prof)
    add_assessment(story, prof)
    return build_pdf(pdf_name(prof, "english-instructor-guide"), f"EFSP {prof['title']} - Instructor Guide", story)


def participant_workbook(prof: dict) -> Path:
    story = cover(
        prof,
        f"{prof['title']} Participant Workbook",
        "Practice pages for realistic field-specific meetings, pushback, documentation, and role-play preparation",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "For each module, read a workplace scenario and complete a bounded dialogue. Choose one of four options, then use the answer key to see why the selected phrase fits the evidence, risk, owner, and next step."
        )
    )
    answer_key: list[dict[str, str]] = []
    all_outputs = [item["output"] for item in prof["modules"]]
    for index, module in enumerate(prof["modules"], start=1):
        story.append(h2(f"Module {index}. {module['title']}"))
        story.append(box("Situation", [module["scenario"], f"Stakeholder pressure: {module['pressure']}", f"Constraint: {module['constraint']}"], "blue"))
        story.append(h3("Terms to use"))
        story.append(bullets(module["terms"]))
        add_cloze_exercise(story, make_module_cloze(module, all_outputs), answer_key)
    add_participant_practical_drills(story, prof, answer_key)
    add_answer_key(story, answer_key)
    return build_pdf(pdf_name(prof, "english-participant-workbook"), f"EFSP {prof['title']} - Participant Workbook", story)


def dialogue_lab(prof: dict) -> Path:
    story = cover(
        prof,
        f"{prof['title']} Dialogue Lab",
        "Realistic field-specific dialogues, role-play variations, and observer checklists",
    )
    story += h1("Dialogue Practice Method")
    story.append(
        p(
            "Read each exchange once for meaning, once for tone, and once for decision structure. Then complete the missing language by selecting one of four options and check the rationale at the end."
        )
    )
    answer_key: list[dict[str, str]] = []
    all_outputs = [item["output"] for item in prof["modules"]]
    for index, module in enumerate(prof["modules"], start=1):
        speaker_a, speaker_b = module["speakers"]
        story.append(h2(f"{index}. {module['title']}"))
        story.append(box("Setting", [module["scenario"]], "blue"))
        rows = [
            ["Speaker", "Line"],
            [speaker_a, module["pressure"]],
            [speaker_b, module["constraint"]],
            [
                "ESL learner",
                f"I understand the goal, but we need to separate urgency from control. For this decision, I need to confirm {module['terms'][0]}, {module['terms'][1]}, the owner, and the evidence standard before we commit.",
            ],
            [speaker_a, "What would let us move forward without slowing everything down?"],
            [
                "ESL learner",
                f"Let's document the assumption, define the risk trigger, and create a short {module['output']}. Then we can decide whether to proceed, escalate, or revise the plan.",
            ],
        ]
        story.append(table(rows, [1.55 * inch, CONTENT_WIDTH - 1.55 * inch]))
        story.append(h3("Language notes"))
        story.append(
            bullets(
                [
                    f"The learner names the field-specific control point instead of giving a vague no: {', '.join(module['terms'][:2])}.",
                    "The response preserves the business goal while adding evidence, owner, and next-step discipline.",
                ]
            )
        )
        add_cloze_exercise(story, make_module_cloze(module, all_outputs), answer_key, show_context=False)
        story.append(h3("Observer checklist"))
        story.append(
            bullets(
                [
                    "Did the learner name the decision and the risk?",
                    "Did the learner use at least two industry terms accurately?",
                    "Did the learner give a concrete next step without overpromising?",
                ]
            )
        )
    add_expanded_dialogues(story, prof)
    add_answer_key(story, answer_key)
    return build_pdf(pdf_name(prof, "dialogue-lab"), f"EFSP {prof['title']} - Dialogue Lab", story)


def jargon_guide(prof: dict) -> Path:
    story = cover(
        prof,
        f"{prof['title']} Jargon Quick Reference",
        "Field-specific terms, contrast pairs, and high-pressure sentence frames",
    )
    add_jargon(story, prof)
    add_phrase_bank(story, prof)
    add_practical_collocations(story, prof)
    add_specialized_nomenclature(story, prof)
    story += h1("Contrast Pairs")
    rows = [["Do not confuse", "Useful distinction"]]
    for module in prof["modules"]:
        rows.append(
            [
                f"{module['terms'][0]} vs {module['terms'][-1]}",
                f"In {module['title'].lower()}, define whether the discussion is about the current fact pattern, the controlling process, the stakeholder pressure, or the final decision.",
            ]
        )
    story.append(table(rows, [2.25 * inch, CONTENT_WIDTH - 2.25 * inch]))
    return build_pdf(pdf_name(prof, "jargon-quick-reference"), f"EFSP {prof['title']} - Jargon Quick Reference", story)


def generate_all() -> list[Path]:
    paths: list[Path] = []
    for prof in INDUSTRIES:
        paths.extend([instructor_guide(prof), participant_workbook(prof), dialogue_lab(prof), jargon_guide(prof)])
    return paths


def feature_html(prof: dict) -> str:
    title = html.escape(prof["title"])
    summary = html.escape(prof["summary"])
    slug = prof["slug"]
    return f"""<section class="efsp-feature">
<div class="efsp-feature-copy">
<p class="eyebrow">Available Now</p>
<h2>{title}</h2>
<p>{summary}</p>
</div>
<div class="efsp-download-grid" aria-label="{title} PDF downloads">
<a class="efsp-download-link" href="pdf/efsp/{pdf_name(prof, "english-instructor-guide")}">Instructor Guide</a>
<a class="efsp-download-link" href="pdf/efsp/{pdf_name(prof, "english-participant-workbook")}">Participant Workbook</a>
<a class="efsp-download-link" href="pdf/efsp/{pdf_name(prof, "dialogue-lab")}">Dialogue Lab</a>
<a class="efsp-download-link" href="pdf/efsp/{pdf_name(prof, "jargon-quick-reference")}">Jargon Guide</a>
</div>
</section>"""


def card_html(prof: dict) -> str:
    title = html.escape(prof["title"])
    card_title = title.replace(" English", "")
    summary = html.escape(prof["summary"])
    return f"""<article class="efsp-curriculum-card efsp-curriculum-card-ready">
<span class="efsp-card-label">Ready</span>
<h3>{card_title}</h3>
<p>{summary}</p>
<a class="efsp-card-link" href="#{prof['slug']}-detail">View details</a>
</article>"""


def detail_html(prof: dict) -> str:
    title = html.escape(prof["title"])
    summary = html.escape(prof["summary"])
    module_items = "\n".join(
        f"<li>{html.escape(module['title'])}: {html.escape(module['skill'])}</li>" for module in prof["modules"]
    )
    material_items = "\n".join(
        [
            "<li>Instructor guide with eight 90-minute module plans</li>",
            "<li>Participant workbook with customized field-specific practice pages</li>",
            "<li>Dialogue lab with realistic workplace conversations and observer checklists</li>",
            "<li>Jargon quick reference with terminology, contrast pairs, and pressure-tested sentence frames</li>",
        ]
    )
    return f"""<section class="efsp-detail" id="{prof['slug']}-detail">
<p class="eyebrow">Curriculum Detail</p>
<h2>{title}</h2>
<p>{summary}</p>
<div class="efsp-detail-grid">
<article>
<h3>Core topics</h3>
<ul>
{module_items}
</ul>
</article>
<article>
<h3>Materials included</h3>
<ul>
{material_items}
</ul>
</article>
</div>
</section>"""


def replace_or_insert(text: str, start: str, end: str, block: str, insert_before: str) -> str:
    wrapped = f"{start}\n{block}\n{end}"
    if start in text and end in text:
        before, rest = text.split(start, 1)
        _, after = rest.split(end, 1)
        return before + wrapped + after
    if insert_before not in text:
        raise ValueError(f"Insert marker not found: {insert_before[:80]}")
    return text.replace(insert_before, wrapped + "\n\n" + insert_before, 1)


def update_html() -> Path:
    path = ROOT / "efsp.html"
    text = path.read_text()
    features = "\n\n".join(feature_html(prof) for prof in INDUSTRIES)
    cards = "\n".join(card_html(prof) for prof in INDUSTRIES)
    details = "\n\n".join(detail_html(prof) for prof in INDUSTRIES)
    text = replace_or_insert(
        text,
        "<!-- EFSP INDUSTRY BATCH FEATURES START -->",
        "<!-- EFSP INDUSTRY BATCH FEATURES END -->",
        features,
        '<section class="efsp-section">\n<p class="eyebrow">Curriculum Library</p>',
    )
    text = replace_or_insert(
        text,
        "<!-- EFSP INDUSTRY BATCH CARDS START -->",
        "<!-- EFSP INDUSTRY BATCH CARDS END -->",
        cards,
        '<article class="efsp-curriculum-card">\n<span class="efsp-card-label">Planned</span>',
    )
    text = replace_or_insert(
        text,
        "<!-- EFSP INDUSTRY BATCH DETAILS START -->",
        "<!-- EFSP INDUSTRY BATCH DETAILS END -->",
        details,
        '<section class="efsp-detail" id="pharmaceutical-detail">',
    )
    text = text.replace(
        "Managers, engineers, legal professionals, finance teams, financial advisors, marketers, real estate professionals, strategy teams, pharmaceutical teams, HR partners, sales teams, customer support, researchers, and executives.",
        "Managers, engineers, legal professionals, finance teams, healthcare administrators, educators, manufacturing teams, supply-chain teams, HR partners, sales teams, customer-success teams, public-sector teams, researchers, and executives.",
    )
    path.write_text(text)
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-html", action="store_true", help="Generate PDFs without updating efsp.html.")
    args = parser.parse_args()
    paths = generate_all()
    if not args.skip_html:
        from generate_efsp_web_pages import main as generate_web_pages

        generate_web_pages()
    for path in paths:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
