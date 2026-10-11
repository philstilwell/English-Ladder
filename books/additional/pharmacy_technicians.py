"""Original pharmacy calculations, storage-log, and pack-change conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Check what the number measures",
        skill="Explain a days-supply calculation using verified units and distinguish a maximum-use calculation from actual consumption.",
        setup="Fictional calculation check, not patient advice: order A supplies 60 tablets, strength 5 mg each, verified direction one tablet twice daily. A copied days-supply field says 60. Separate order B supplies 30 tablets, as needed, with an explicit maximum of 6 tablets daily. Pharmacist review is required before processing.",
        cast="Tara|Pharmacy technician\nOmar|Pharmacist",
        dialogue="""Tara|Omar, order A has sixty tablets, but the days-supply field also says sixty. That looks copied from the old once-daily order. The current direction is twice daily.
Omar|Start with the current [[directions for use::The verified current directions specify one tablet twice daily; the previous once-daily pattern cannot determine this order's days supply.]]. Read the amount per administration and the frequency separately before you divide anything.
Tara|One tablet each time, twice daily: two tablets per day. Quantity sixty divided by two gives thirty days at that stated schedule.
Omar|Correct: the calculated [[days supply::Sixty tablets divided by two tablets per day equals thirty days; the copied sixty-day field does not match the current directions.]] is thirty. What does the five-milligram figure describe, and why is it not your divisor here?
Tara|That is the strength per tablet. Dividing sixty tablets by five milligrams would mix unlike units and would not produce the number of days.
Omar|Exactly. Keep [[strength::Strength is five milligrams per tablet; it is not the number of tablets used each day and cannot replace the daily tablet quantity in this calculation.]], tablet quantity, and daily tablet use in separate fields. The arithmetic should carry the units, not just a row of numbers.
Tara|I will correct the draft calculation through our process and retain the reason: current twice-daily directions, not the earlier once-daily entry.
Omar|Bring it back for the required check. Correct arithmetic is not [[clinical approval::Clinical approval and the required pharmacy checks are separate from arithmetic; a correct quotient does not establish that a prescription is appropriate or ready to supply.]] or evidence that all other dispensing checks are complete.
Tara|Order B is different. It says as needed, maximum six tablets in a day, quantity thirty. Should I describe that as certain to last five days?
Omar|No. Five days is the calculation at [[maximum daily use::Thirty tablets divided by the explicit maximum of six daily equals five days at maximum use, not a prediction that the patient will consume that amount every day.]]. As-needed use does not tell us the amount the person will actually take each day.
Tara|So thirty divided by six gives five at the maximum, but lower use would leave some tablets after five days. I cannot infer the actual use pattern from that division.
Omar|Right. Nor should you tell the patient to take six daily because that makes the calculation easy. A maximum is a limit in the supplied instruction, not a new scheduled dose.
Tara|For the claim entry, I still need to apply the relevant plan and pharmacy rules, with your check. The language exercise does not establish a universal billing rule.
Omar|Yes. Keep the arithmetic and its assumptions visible. If the directions or maximum were unclear, we would resolve that rather than choose a convenient number to pass the claim.
Tara|Does a thirty-day calculation on order A establish that the patient took every dose in an earlier supply?
Omar|No. [[Adherence::Adherence concerns following the agreed medicine directions; a quantity-based calculation or refill interval alone does not prove how the patient actually used the medicine.]] needs an appropriate discussion and assessment. A calculated supply period is not an observation of what somebody swallowed.
Tara|And if a patient reports taking it differently, I should record their account and bring it to you, not alter the directions just to make the stock balance.
Omar|Correct. Keep prescribed use, reported use, and the supplied quantity distinguishable. A discrepancy may need clarification; hiding it inside a new days-supply figure would lose important information.
Tara|My read-back: order A, sixty tablets at two daily, thirty days. Order B, thirty tablets at six maximum daily, five days at maximum use, actual duration unknown.
Omar|Agreed. Mark both calculations for the required review. No supply authorization, treatment change, or confirmed pattern of patient use follows solely from these numbers.""",
        transfer_title="Use tablets per day, not milligrams",
        transfer_setup="Fictional arithmetic only: 84 tablets, strength 10 mg per tablet, verified direction one tablet three times daily. Separately, 24 tablets have as-needed directions with an explicit maximum of 4 daily. No actual consumption or billing outcome is supplied.",
        transfer="""Technician: The scheduled order uses ___ tablets daily.|3|One tablet on each of three daily occasions equals three tablets per day, not ten.
Pharmacist: Eighty-four tablets at that rate represents ___ days.|28|Eighty-four divided by three tablets per day equals twenty-eight days under the supplied schedule.
Technician: The separate as-needed quantity represents ___ days at maximum use.|6|Twenty-four tablets divided by the maximum of four daily equals six days at that maximum.
Pharmacist: Actual as-needed consumption remains ___ .|unknown|The maximum-use calculation supplies a conditional rate, not evidence of the amount actually taken.""",
        reference=("PTCB: 2026 knowledge reference, calculations and pharmacist intervention", "https://ptcb.org/wp-content/uploads/2025/05/cpht-knowledge-reference.pdf"),
    ),
    scenario(
        title="Read the whole temperature log",
        skill="Report the recorded excursion interval, measurement source, stock details, and unresolved disposition without inferring product stability.",
        setup="Fictional Product R requires 2 to 8 degrees Celsius. The validated fridge air log establishes 10:05 to 10:40 above 8, peak 11.4. Current reading at 11:00 is 5. Three cartons contain 12 vials each, lot Q28. Technician Lina has activated the hold and alerts pharmacist Daniel; no release decision exists.",
        cast="Lina|Pharmacy technician\nDaniel|Pharmacist",
        dialogue="""Lina|Daniel, Product R is on hold. The fridge is showing five degrees now, but its validated log records an earlier out-of-range interval. I have not released the stock.
Daniel|Give me the [[temperature excursion::The excursion is the recorded interval outside this fictional product's two-to-eight-degree range; the current in-range reading does not erase that history.]] details, including the measurement source. Do not describe the medicine itself as reaching a temperature unless we have that evidence.
Lina|The sensor measures fridge air. The established interval above eight is ten oh five to ten forty, with a peak of eleven point four degrees Celsius.
Daniel|That is [[thirty-five minutes::The established interval from 10:05 to 10:40 lasts thirty-five minutes; it is not the fifty-five minutes from the interval's start to the current 11:00 reading.]] outside the specified upper limit. The present reading at eleven does not tell us when that interval began or how high it went.
Lina|I have preserved the data export, sensor identity, and timestamps. I will not reset the record before the evidence is retained under our procedure.
Daniel|Good. The [[air temperature::The sensor records fridge air, not a directly measured vial-content temperature; the assessment must preserve that measurement distinction.]] tells us about the storage environment. The responsible assessment needs the product details as well as the log, not a guess about a vial's internal temperature.
Lina|Three cartons, twelve vials each, thirty-six vials in total. Product R, lot Q28. I am checking expiry and whether any earlier excursion is recorded.
Daniel|Retain that [[traceability::Traceability connects the affected quantity, product and lot with the specific storage event and subsequent authorized decision.]]. Unknown earlier exposure should stay unknown until checked; do not mark none merely because you have not found the record yet.
Lina|The hold is marked in the system and on the segregated stock. Should it stay under the product's required storage arrangements while the decision is pending?
Daniel|Follow our established hold and storage procedure. [[Quarantine::Quarantine prevents use pending assessment; it is not permission to abandon required storage conditions or a final decision to destroy the medicine.]] controls availability; it does not mean leaving temperature-sensitive stock unattended on a counter.
Lina|A colleague said another brand tolerated a warmer delivery last month. Can that earlier decision clear this lot too?
Daniel|No. I need information for the actual product, conditions, and history. Another brand's previous assessment is not a release decision for Product R after this event.
Lina|I will gather the current manufacturer information and record the source. I will also check whether any stock movement occurred during the interval, rather than assume everything stayed untouched.
Daniel|Bring the findings to me for the assessment. Do not tell patients to change treatment on the basis of this inventory conversation; any affected supply or clinical concern needs the appropriate separate response.
Lina|For the incident note, I will describe the reading and times without stating that the product is spoiled. The excursion is established, but suitability has not been determined.
Daniel|Correct. The [[disposition::Disposition is the authorized decision about use, return, or disposal after assessment; neither an excursion nor a normal current reading establishes that decision by itself.]] remains pending. We need the evidence and the authorized decision, not a premature release or destruction entry.
Lina|The current five-degree reading also does not prove the equipment fault has been investigated. I will keep the fridge-status issue separate from the stock assessment.
Daniel|Exactly. Check the equipment through the relevant procedure and retain its findings. A repaired or stable fridge and an assessed medicine lot answer different questions.
Lina|Summary: thirty-six vials Q28 held; fridge-air peak eleven point four, thirty-five-minute interval; current five; earlier exposure being checked; product and equipment reviews pending.
Daniel|That is the report I need. I own the product assessment. Keep the hold and storage controls in place under our procedure until the authorized outcome is documented.""",
        transfer_title="Do not substitute the current reading",
        transfer_setup="Fictional required range: 2 to 8 degrees Celsius. An established logger interval above 8 runs 14:20 to 14:50; peak 10.2. Current reading at 15:00 is 4.8. Two cartons contain 15 vials each. Stock is held; no disposition is confirmed.",
        transfer="""Technician: The established excursion lasted ___ minutes.|30|The interval from 14:20 to 14:50 is thirty minutes, not forty minutes to the current reading.
Pharmacist: The recorded peak was ___ degrees Celsius.|10.2|The historical peak is 10.2; the current 4.8 reading must not replace it in the event report.
Technician: Two cartons of fifteen means thirty ___ on hold.|vials|The quantity unit is vials: two cartons multiplied by fifteen vials per carton equals thirty vials.
Pharmacist: The authorized disposition is still ___ .|pending|The supplied facts establish a hold and current reading, not a completed decision about release or disposal.""",
        reference=("NHS SPS: managing temperature excursions and product-specific assessment", "https://sps.nhs.uk/articles/managing-temperature-excursions/"),
    ),
    scenario(
        title="A change before the next pack",
        skill="Communicate a verified regimen change across current and future medicine packs without treating a printing update as completed patient communication.",
        setup="Fictional case on Friday 9 October: pharmacist Ren verifies an authorized order discontinuing Medicine P from this evening. The patient's current multi-compartment pack covers 5 to 11 October; a prepared, undelivered pack covers 12 to 18 October. Both contain P. Ren owns immediate patient coordination; technician Jade controls the pending pack.",
        cast="Jade|Pharmacy technician\nRen|Pharmacist",
        dialogue="""Jade|Ren, the new instruction discontinues Medicine P from this evening, but next week's pack is already prepared. It has not gone out. Does your verification cover the effective date too?
Ren|Yes: Friday the ninth, this evening. Put the prepared [[multi-compartment pack::The multi-compartment pack for 12 to 18 October still contains the discontinued medicine and must enter the agreed hold and correction process before release.]] on hold under our process. We must address the pack already at home as well.
Jade|The current pack runs from October fifth through the eleventh. It also contains P. Changing only the pack starting Monday would miss this evening and the weekend.
Ren|Exactly. The [[effective date::The effective date is Friday 9 October, not the Monday start of the next packaging cycle; the change affects the current pack as well as future preparation.]] and the next packaging cycle are different. I will coordinate the immediate patient instructions and support, not defer the issue to Monday's delivery.
Jade|I have applied the hold to the October twelfth pack and removed it from the dispatch queue. I have not opened, altered, or released it.
Ren|Keep the [[pack identifier::The pack identifier and covered dates distinguish the held future pack from the current pack at the patient's home.]] and covered dates in the record. A note saying pack changed would be too vague when there are two different packs to account for.
Jade|Should I phone and tell the patient to remove whichever tablet looks like P? There may be several similar-looking tablets in a compartment.
Ren|No. Do not improvise identification or removal instructions from appearance. I will arrange the appropriate patient-specific response with the relevant people under our process.
Jade|The amended order is verified, but patient contact has not happened yet. I will record those as separate stages instead of marking the whole change complete.
Ren|Correct. [[Medicines reconciliation::Medicines reconciliation compares the actual medicine information and resolves discrepancies; receiving a changed order does not prove that all packs, records, and patient instructions already match.]] needs the actual current information, not an assumption that every record and pack updated automatically.
Jade|The care team also has a medicines administration record. I will flag the need to coordinate that record through the proper route, not edit their administration history myself.
Ren|Yes. Preserve the source, verified instruction, timing, and contacts. A new regimen should not erase the record of support or administration that actually occurred before the change.
Jade|For our preparation record, I will retain the earlier version and the dated correction. The revised pack still needs the applicable preparation and final checks.
Ren|And we must distinguish [[prepared::Prepared describes work on a pack; it is not equivalent to final checking, release, dispatch, delivery, or the patient receiving instructions.]], checked, released, and delivered. A revised printout alone is not a corrected pack in the patient's hands.
Jade|If the patient has other medicines outside the pack, the same change should not become a message to stop everything. The order concerns P only.
Ren|Right. I will explain the specific authorized change and check understanding in the actual conversation. You should not invent instructions for other medicines or assume that every product belongs inside the pack.
Jade|For the handoff, I have two open actions: your immediate coordination of the current pack and our held future pack's correction and checking.
Ren|I accept the current-pack action now. Record the actual [[contact outcome::Contact outcome distinguishes an attempted call from successful communication and an agreed arrangement; accepting responsibility does not itself prove that the patient has been reached.]] when it occurs, including anything still unresolved. If contact fails, we must continue the appropriate escalation, not silently wait for delivery day.
Jade|Then the status is: current-pack response with you now; future pack held and undelivered; authorized stop effective this evening; no completed patient communication yet.
Ren|Confirmed. I am starting that coordination immediately. Keep the future pack blocked from dispatch until its required correction and checks are completed and the release is authorized.""",
        transfer_title="A delivery date is not an effective date",
        transfer_setup="An authorized change is verified to take effect Wednesday 14 October. The patient has a current pack for 12 to 18 October; the next pack starts 19 October and is undelivered. Pharmacist Leena owns immediate patient coordination. No contact outcome is recorded yet.",
        transfer="""Technician: The change takes effect on ___ October.|14|The verified effective date is the fourteenth, not the next pack's nineteenth-of-October start date.
Pharmacist: The current pack ends on ___ October.|18|The current pack covers the twelfth through the eighteenth and therefore spans the change date.
Technician: The next pack begins on ___ October.|19|The undelivered next pack starts on the nineteenth; that does not postpone the earlier effective change.
Pharmacist: Patient communication is not yet confirmed as ___ .|completed|A named pharmacist and a verified order do not establish that the patient has received the updated instructions.""",
        reference=("NHS SPS: complex regimens and avoiding confusion between old and new medicine packs", "https://sps.nhs.uk/articles/complex-medication-regimens-supporting-adherence/"),
    ),
]
