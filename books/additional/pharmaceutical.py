"""Original pharmaceutical quality and supply conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='The shipment is cold again, but its history still matters',
        skill='Report a temperature excursion without making an unsupported product-quality decision.',
        setup='A logger for a fictional refrigerated medicine shipment shows a period above its specified transport range. The shipment is now within range. Duration, peak temperature, affected lots, and product-specific stability support need qualified review. Distribution has not been authorized.',
        cast='Ravi|Distribution coordinator\nElena|Quality specialist',
        dialogue='''Ravi|The logger alarmed during transit, but the delivery is back within range. Can the warehouse receive it into available stock?
Elena|Keep it in the appropriate [[quarantine status::Quarantine status prevents use or distribution pending the authorized quality decision; current temperature alone does not settle suitability.]] under our procedure. What does the original logger record show?
Ravi|A period above the upper limit. I have the graph but have not checked the time zone or downloaded the complete file.
Elena|Preserve the [[raw data::Raw data are the original recorded measurements and associated information needed to assess the excursion reliably.]] and the logger details. A screenshot alone may omit information needed for the assessment.
Ravi|The carrier says the alarm lasted only briefly. Should I use their estimate in the incident summary?
Elena|Attribute it as the carrier's statement, not the verified duration. We need the recorded interval, peak, and time basis checked.
Ravi|I will also confirm the lot numbers and which shipping containers the logger accompanied.
Elena|Good. That establishes the [[affected scope::Affected scope identifies which product and quantities may be involved, rather than assuming every shipment or no shipment was exposed.]] for review. Do not infer that one logger necessarily represents every container.
Ravi|The products look normal. There is no visible damage to the cartons.
Elena|Record that observation, but appearance does not establish product quality after a [[temperature excursion::A temperature excursion is exposure outside the specified range; visual appearance does not determine its effect on the product.]].
Ravi|Could we use the allowance applied to another medicine last month? That shipment was eventually released.
Elena|No. The assessment needs the relevant [[stability data::Stability data support assessment of this product under relevant conditions; another product's decision cannot be transferred automatically.]], history, and approved process for this product.
Ravi|The receiving site is asking whether the delivery can be used today. I need a sentence that is clear without sounding evasive.
Elena|Say: "The shipment is held for quality assessment; use is not authorized. We will provide the next status update at the agreed time."
Ravi|Should I arrange replacement stock now, or wait for the assessment?
Elena|Ask supply to assess the options in parallel. Do not make the quality decision depend on whether a replacement is convenient.
Ravi|I will send the complete record and container mapping, and keep the current storage conditions controlled under the procedure.
Elena|I will assign the review and document the [[disposition::Disposition is the authorized decision about how the product may be handled after the evidence has been reviewed.]] once the evidence supports it.
Ravi|The summary will distinguish the verified readings from the carrier's account. I will not describe the shipment as released.
Elena|Exactly. Returning to the specified range ends the current temperature event; it does not erase the exposure history.''',
        transfer_title='A missing logger file is treated as a normal result',
        transfer_setup='A logger file cannot yet be opened. Cartons are intact and the receiving temperature is within range. Transport history has not been verified.',
        transfer='''Coordinator: The receiving reading is within range, but the journey history is ___.|unverified|The current reading cannot establish the temperatures experienced earlier in transit.
Quality: Preserve the device and pursue recovery of the original ___.|record|The original logger record is the evidence needed to assess the transport history.
Coordinator: I will not translate missing data into a passing ___.|result|No passing assessment can be inferred merely because the data cannot be read.
Quality: Keep the product in its required controlled status pending authorized ___.|review|The unresolved history requires the appropriate quality review before a use decision.'''),
    scenario(
        title='A passing retest does not make the first result disappear',
        skill='Discuss an out-of-specification result while protecting the complete investigation record.',
        setup='A fictional assay result falls outside its approved acceptance criterion. A later test passes. No assignable laboratory error has been established, and the investigation is still open. The laboratory manager and quality reviewer must decide what to document and investigate, not release the batch.',
        cast='Noemi|Laboratory manager\nAlex|Quality reviewer',
        dialogue='''Noemi|The later assay passes. Production wants the summary updated to show the passing result instead of the original failure.
Alex|We must retain both. The original [[out-of-specification result::An out-of-specification result falls outside the established acceptance criterion and requires documented investigation, not silent replacement.]] still requires a supported investigation conclusion.
Noemi|The analyst suspects a preparation error, but has not found evidence of one.
Alex|Then record it as a hypothesis. We cannot designate an [[assignable cause::An assignable cause is a cause established by evidence; an analyst's suspicion alone does not establish one.]] because it would explain away an inconvenient result.
Noemi|I will review the preparation records, instrument information, calculations, and the original sample sequence with the analyst.
Alex|And preserve the [[audit trail::The audit trail records relevant actions and changes so the investigation can reconstruct what actually occurred.]]. The original files and their history need to remain available.
Noemi|Would averaging the passing and failing values give us a representative number for the batch?
Alex|Not as a way to cancel the failing result. Follow the approved method and investigation procedure; do not invent an averaging rule after seeing the outcomes.
Noemi|The next question is whether more testing would clarify the suspected preparation issue.
Alex|Any further [[retesting::Retesting repeats analysis under a justified investigation plan; it must not become repeated testing until a favorable result appears.]] needs a documented rationale and authorized plan, not an open-ended search for a pass.
Noemi|We should also establish whether the retained sample can answer the question or whether someone is proposing a new sample.
Alex|Yes. [[Resampling::Resampling takes another sample; it is different from retesting and needs its own justified basis in the investigation.]] is a separate action with its own justification. Changing the sample can change what evidence we have.
Noemi|If the laboratory review finds no supported error, the investigation cannot simply stop with "retest passed."
Alex|Correct. The review must address the potential manufacturing issue and the full body of evidence through the applicable process.
Noemi|I will notify production of the open investigation and request the relevant batch records without declaring a manufacturing defect.
Alex|That keeps the scope open appropriately. We need evidence, not an early conclusion about which department is responsible.
Noemi|For today's report, I will show both results, the hypothesis, completed checks, and the questions still unanswered.
Alex|Include the [[investigation conclusion::The investigation conclusion must explain the supported findings and treatment of all relevant results; it remains pending here.]] as pending, with the owner and next review step.
Noemi|And no batch-release statement, even if the shipment date is close.
Alex|Exactly. A passing later test is evidence to evaluate, not permission to delete the first result or bypass disposition.''',
        transfer_title='Testing continues until the desired number appears',
        transfer_setup='After a failing result, a colleague proposes repeated testing without a defined plan and retaining only the first passing result.',
        transfer='''Reviewer: We need an authorized investigation ___ before further testing.|plan|The proposed repeated testing lacks a defined, justified investigation approach.
Analyst: I will preserve every original result, not just the favorable ___.|one|Selecting only a favorable result would conceal relevant evidence from the investigation.
Reviewer: A possible preparation error is still a hypothesis, not an established ___.|cause|No evidence establishing the suspected preparation error has been supplied.
Analyst: The batch status remains subject to the authorized quality ___.|decision|Testing alone does not transfer batch-disposition authority to the analyst.'''),
    scenario(
        title='The packaging artwork is current, but the line has an older version',
        skill='Coordinate a labeling discrepancy with precise version, scope, and release language.',
        setup='Before packaging starts, an operator finds that the issued carton artwork revision differs from the revision required by the approved batch instruction. No units have been packaged in this run. The discrepancy must be controlled through the site quality process; no one may silently substitute files.',
        cast='Dina|Packaging supervisor\nHassan|Quality coordinator',
        dialogue='''Dina|The batch instruction calls for revision C, but the issued cartons show revision B. We caught it before starting the run.
Hassan|Keep the start on hold and secure the suspect materials under the procedure. First confirm the [[artwork revision::Artwork revision identifies the specific approved labeling version; similar appearance does not establish that two revisions are equivalent.]] against the controlled records.
Dina|The visible difference is small. Someone suggested crossing out the instruction's revision letter and using what is already at the line.
Hassan|Do not change the instruction informally. We need to establish whether the issue is the instruction, material issuance, or something else.
Dina|I will record both identifiers and the quantities issued. No units from this run have been packaged.
Hassan|That is an important boundary. Preserve the [[material traceability::Material traceability links the issued packaging components to their identity, quantities, and handling records.]] so we can identify exactly what may be affected.
Dina|Should we check whether the same carton revision was issued to another line?
Hassan|Yes, through the investigation. Expand the scope using records rather than assume this is the only occurrence or that all other runs are affected.
Dina|The planner can deliver revision C this afternoon. Is that enough to restart?
Hassan|Not by itself. The correct materials, required review, and [[line clearance::Line clearance verifies that the line is ready for the intended operation and free of relevant materials from an incompatible or previous operation.]] must be confirmed before authorized restart.
Dina|I want to make sure the older cartons cannot be picked up again while we wait.
Hassan|Use the required [[segregation::Segregation keeps materials with different or restricted status from being mixed or used inadvertently.]] and status controls. Record their location rather than leave a loose note beside an unmarked stack.
Dina|Could the supplier tell us whether the revisions are interchangeable?
Hassan|They can provide relevant information. Equivalence and permitted use still require our authorized review; the supplier's reassurance is not our release decision.
Dina|If the instruction itself needs correcting, we should not overwrite the original file.
Hassan|Correct. Route it through [[change control::Change control evaluates, approves, and documents a proposed change rather than allowing an undocumented substitution.]] and retain the reason, approvals, and applicable version history.
Dina|For the shift handover, I will state that the run has not started and the material mismatch is under review.
Hassan|Add the hold location, open actions, and responsible contacts. The incoming shift should not interpret a replacement delivery as permission to begin.
Dina|Once the issue is resolved, I will reconcile the issued, returned, and used quantities through the batch record.
Hassan|And document the [[restart authorization::Restart authorization is the formal permission to resume after the required conditions are met, not merely the arrival of replacement cartons.]] so the final decision is traceable to the actual completed checks.''',
        transfer_title='Correct cartons arrive during a shift change',
        transfer_setup='Replacement cartons arrive while the line remains on hold. Required review and clearance checks are incomplete.',
        transfer='''Supervisor: Delivery of the cartons does not cancel the current ___.|hold|The hold remains because the required review and clearance checks are incomplete.
Quality: The handover must identify the remaining checks and their ___.|owners|Named owners make responsibility for the unfinished checks explicit across the shift change.
Supervisor: I will keep the two material versions physically controlled and clearly ___.|identified|Clear identification and control help prevent unintended use of the wrong packaging version.
Quality: Resume only after the required conditions and authorization are ___.|confirmed|Replacement delivery alone does not establish that the required restart conditions are satisfied.'''),
]
