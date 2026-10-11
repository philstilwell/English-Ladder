"""Original metrology, replenishment, and first-piece conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='The gauge passes today, but what about yesterday?',
        skill='Report a measurement concern and define the scope of a product-impact review.',
        setup='A micrometer fails its incoming calibration check and passes after adjustment. It was used to accept three production lots yesterday. The quality engineer and supervisor must organize a retrospective review. The fictional site has removed the instrument from production use pending the required decisions.',
        cast='Marta|Quality engineer\nCal|Production supervisor',
        dialogue='''Cal|The lab adjusted the micrometer and it passes now. Can I close the issue and put yesterday\'s three lots back on schedule?
Marta|Not yet. I need the [[as-found results::As-found results describe the instrument before adjustment, which is the relevant starting point for assessing earlier measurements.]], not just the passing report after adjustment. What did it read before anyone changed it?
Cal|I have the final certificate here. The earlier readings are on a separate sheet; I will request that too.
Marta|Thank you. The [[as-left results::As-left results describe the instrument after the calibration work or adjustment and do not establish its earlier condition.]] tell us its condition afterward. They do not resolve the earlier acceptance decisions.
Cal|We know it was used yesterday, but two operators shared it. Their inspection sheets should give us the part numbers.
Marta|Match those sheets to the instrument\'s [[asset identifier::The asset identifier connects the specific instrument to its inspection records, avoiding assumptions based on a tool description alone.]]. We must not include every micrometer just because they look alike.
Cal|Should I tell the warehouse that all three lots are defective? They are asking what to put in their update.
Marta|Say acceptance is under review. A suspect measurement does not automatically prove that every part is defective.
Cal|What else will you need once we have the readings and the lot list?
Marta|The measured features, limits, method, and relevant [[measurement uncertainty::Measurement uncertainty describes the dispersion associated with a measured value; it contributes to evaluating whether the measurement is fit for its intended decision.]]. Then we can assess which decisions may be affected.
Cal|Some results were near a limit. I will flag those, but I will not quietly replace them with fresh measurements.
Marta|Correct. Preserve the original records. Any [[reinspection::Reinspection is a new examination under an established plan; its results must remain distinguishable from the original inspection.]] needs an agreed plan, suitable equipment, and separate results.
Cal|One of the lots has already left the site. I will identify its destination rather than leave it out of the review.
Marta|Please do. Include shipped material in the impact assessment and route any required customer action to the responsible team.
Cal|Can we borrow another calibrated micrometer for the next job while you review these lots?
Marta|Check its range, resolution, condition, and suitability for the feature. A calibration label alone does not establish [[fitness for purpose::Fitness for purpose means the measurement capability is adequate for the intended task, not merely that a calibration label exists.]].
Cal|Understood. I will send the three lot records and identify which instrument handled each inspection before the planning meeting.
Marta|I will bring the initial assessment and list anything still missing. Keep the affected material status visible until the required disposition is recorded.
Cal|The update will separate today\'s instrument condition from yesterday\'s product decisions. That should prevent the passing certificate from closing both questions.
Marta|Exactly. We need a defensible conclusion about the earlier measurements, not just a tool that reads correctly now.''',
        transfer_title='A replacement gauge is not automatically suitable',
        transfer_setup='A replacement instrument has a current calibration label, but its range and measurement capability have not been checked against the required feature.',
        transfer='''Supervisor: The label does not establish fitness for this ___.|measurement|A calibration label alone does not show suitability for the particular measurement task.
Engineer: Compare the instrument capability with the feature and its ___.|limits|The relevant feature limits help determine the measurement capability required for the decision.
Supervisor: Keep earlier results separate from any new ___.|inspection|New inspection results must not silently overwrite the original evidence.
Engineer: Record the basis for selecting the replacement ___.|instrument|The selection should identify the actual instrument and why it is suitable.''',
        reference=('NIST: Metrological Traceability Policy', 'https://www.nist.gov/calibrations/traceability')),
    scenario(
        title='The right total, the wrong replenishment mix',
        skill='Resolve a line-side material shortage without confusing quantities, variants, and replenishment signals.',
        setup='An assembly cell needs 40 left-hand and 40 right-hand brackets. Its delivery contains 60 left-hand and 20 right-hand brackets. The total of 80 is correct, but only 20 complete pairs are available. A material handler and cell leader reconcile the delivery and the replenishment signal.',
        cast='Inez|Cell leader\nDev|Material handler',
        dialogue='''Inez|Dev, the trolley has eighty brackets, but we cannot build forty assemblies from it. Can you check the two variant labels with me?
Dev|I see the problem. The [[part-number mix::The part-number mix describes the quantities of different variants; the correct combined total does not establish the required mix.]] is sixty left-hand and twenty right-hand, rather than forty of each.
Inez|Each assembly uses one of each. That gives us twenty complete pairs, with forty left-hand brackets left over.
Dev|So the immediate [[shortage::The shortage is twenty right-hand brackets relative to the forty required; excess left-hand brackets do not substitute for them.]] is twenty right-hand brackets. I will locate those before asking stores for another eighty parts.
Inez|Thank you. The last delivery note only showed the family total. We need the two part numbers on the correction.
Dev|I will check the [[pick list::The pick list records the items and quantities requested for retrieval, helping locate where the variant mismatch entered the process.]] against what was actually loaded. We should not assume the error started in stores.
Inez|The line-side bins look similar, and one replenishment card was tucked behind the other. That may be relevant, but let us preserve the actual record.
Dev|Agreed. I will match each [[kanban::A kanban is a signal authorizing production or movement within a defined pull system; it must identify the relevant item and quantity.]] to its part number and standard quantity before changing anything.
Inez|Please do not increase both quantities as a quick fix. We have limited space, and extra left-hand stock will not solve the missing pairs.
Dev|No. I will return the excess through the normal process and correct the [[inventory balance::The inventory balance must reflect the actual quantity and location after the physical movement, rather than retaining an incorrect delivery total.]] after the movement is recorded.
Inez|Can you give me a reliable arrival time for the twenty missing pieces? I need to coordinate the remaining work at the cell.
Dev|I will confirm stock and transport first. At the moment, I can promise a status update in ten minutes, not delivery in ten minutes.
Inez|That works. There is also a right-hand container on the next trolley, but it carries a hold label.
Dev|Leave it alone. [[Held stock::Held stock is restricted pending the applicable decision; physical availability does not mean it is available for production.]] is not a source we can use just to clear the shortage.
Inez|Once the correct parts arrive, we will verify the identifiers and quantities at the cell, not only the total on the trolley.
Dev|I will include those details on the delivery record. Will you confirm receipt so stores knows the correction reached the right location?
Inez|Yes. Then we can review whether the card position or the family-only list contributed to the mismatch.
Dev|I will bring both records. Let us fix the immediate shortage first and investigate the signal without guessing who made the mistake.
Inez|Good. I will tell planning we have twenty pairs now and twenty more pending, rather than eighty usable components for forty assemblies.
Dev|That describes the actual constraint. I will come back with the stock position and the confirmed delivery arrangement.''',
        transfer_title='A family total hides a variant shortage',
        transfer_setup='A cell needs 12 large and 12 small housings. A delivery contains 18 large and six small housings. Each assembly requires one of each.',
        transfer='''Leader: We can build only six complete ___.|assemblies|Six small housings limit production to six assemblies despite the correct overall count.
Handler: We are short of six small ___.|housings|The requirement is twelve small housings but only six have arrived.
Leader: Reconcile the two variants separately on the delivery ___.|record|A combined total hides the incorrect mix and must not replace variant-level quantities.
Handler: Verify the corrected quantities when the cell confirms ___.|receipt|Receipt confirmation establishes that the corrected delivery reached the intended cell.''',
        reference=('Lean Enterprise Institute: Kanban', 'https://www.lean.org/lexicon-terms/kanban/')),
    scenario(
        title='The first-piece report points to the wrong feature',
        skill='Resolve a drawing-to-inspection mismatch before treating a setup as approved.',
        setup='A machine setup produces a first piece for review. The report calls a 6 mm hole feature 12, but feature 12 on the current ballooned drawing is a 10 mm slot. The setup technician and inspector need to reconcile the report, drawing, and physical part. No production approval has been recorded.',
        cast='Nico|Setup technician\nRae|Inspector',
        dialogue='''Nico|The first piece is ready, but your report marks feature twelve as failed. I measured the six-millimeter hole before bringing it over.
Rae|On this [[ballooned drawing::A ballooned drawing numbers the features to connect them with inspection results; the number must refer to the correct feature and revision.]], feature twelve is the ten-millimeter slot. Let us check whether we are discussing the same feature.
Nico|That explains the mismatch. My setup sheet calls the hole twelve. Which drawing revision does your report identify?
Rae|Revision D. The [[inspection characteristic::The inspection characteristic is the specific feature or requirement being evaluated, not merely a number copied between documents.]] needs to match the actual slot, including its applicable requirements.
Nico|My sheet also says D, but the feature numbering may have been copied from an earlier report. I will bring the source file.
Rae|Please keep the original entry. We need a [[controlled correction::A controlled correction preserves the original record and documents the authorized change, rather than silently replacing an inconsistent result.]], not a number changed to make the failure disappear.
Nico|Agreed. I also want to know whether the part itself meets the requirement. Fixing the label will not answer that.
Rae|Exactly. We will reconcile the references and inspect the correct feature using the approved method. The [[datum::A datum is the theoretically exact reference used for applicable dimensional or geometric requirements; the reference must match the drawing and method.]] reference matters where the requirement calls for it.
Nico|Would a passing result for the hole still be useful, provided it is connected to the right characteristic?
Rae|Yes, if the evidence supports it. We should not discard a valid observation, but we cannot relabel it as a measurement of the slot.
Nico|Planning is asking whether the machine can start the full run. They see first piece complete on the schedule.
Rae|That should say first piece submitted. [[First-piece acceptance::First-piece acceptance is the recorded determination that the required setup checks meet their criteria; making or submitting the piece does not establish acceptance.]] has not been recorded, and the unresolved inspection cannot be hidden by the schedule label.
Nico|I will correct that status now. Is this also the same as approving every part that follows?
Rae|No. The [[in-process checks::In-process checks monitor the subsequent production according to the established plan; first-piece acceptance does not remove those requirements.]] remain part of the production plan. A satisfactory first piece does not prove the whole run will remain satisfactory.
Nico|We should check the other copied feature numbers too. Otherwise this may be only the first mismatch we have noticed.
Rae|I agree. Let us compare the full mapping before closing the report. I will identify which results are affected and which remain correctly linked.
Nico|I can provide the setup sheet and the earlier template. You can show the actual inspection records beside the current drawing.
Rae|Good. Then the reviewer can follow the correction instead of reconstructing it from a verbal explanation later.
Nico|I will tell planning the setup is awaiting inspection resolution, with no production approval yet. We will give them the next status after review.
Rae|And we will separate the documentation mismatch from the part result. Either may need action, but they are not the same finding.''',
        transfer_title='A submitted first piece is shown as accepted',
        transfer_setup='The setup team submits a first piece, but a required dimensional result is missing and the acceptance decision is still open.',
        transfer='''Technician: The piece is submitted, but it is not yet ___.|accepted|Submission is a handover milestone and does not establish the inspection decision.
Inspector: Obtain the missing result for the specified ___.|feature|The required feature result is still needed before the inspection can be resolved.
Technician: Keep the schedule status separate from production ___.|approval|A schedule label cannot substitute for the authorized production decision.
Inspector: Retain the required checks throughout the subsequent ___.|run|Acceptance of a first piece does not remove the established in-process inspection requirements.'''),
]
