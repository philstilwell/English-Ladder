"""Original dental-team cases for notation, history, and materials."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Which tooth does twelve mean?",
        skill="Read back the notation system, anatomical tooth, surfaces, and record status without inventing a treatment decision.",
        setup="An imported note says 12 MOD without a notation-system label. The local chart uses Universal numbering. Dentist Imani confirms the intended tooth is the permanent upper-left first premolar, surfaces mesial, occlusal, distal, and the entry is planned, not completed. Assistant Jo verifies the charting instruction.",
        cast="Jo|Dental assistant\nDr. Imani|Dentist",
        dialogue="""Jo|Before I enter this, the imported note says twelve MOD. It does not name the numbering system. Which tooth did you intend?
Dr. Imani|The permanent upper-left first premolar. In our [[Universal::Universal number twelve identifies the permanent upper-left first premolar; the identical digits in FDI notation identify a different tooth.]] chart that is number twelve. Please read back the tooth name as well as the number.
Jo|Permanent upper-left first premolar, Universal twelve. I nearly read the imported twelve as FDI one-two, which would be the upper-right lateral incisor.
Dr. Imani|Exactly. For the intended first premolar, the [[FDI::FDI two-four corresponds to the intended permanent upper-left first premolar; FDI one-two is not the same tooth as Universal twelve.]] equivalent is two-four. The conversion helps us check the language; it does not establish what an unlabeled source intended.
Jo|So I should preserve the imported wording and record your clarification, not silently replace every twelve in the source with twenty-four.
Dr. Imani|Correct. Keep the [[notation system::The notation system must accompany the tooth designation so a reader knows how to interpret the digits.]] visible in the appropriate field. A correct conversion attached to the wrong source assumption would still be wrong.
Jo|Now the surfaces: I read MOD as mesial, occlusal, and distal. Is that the full entry, rather than MO?
Dr. Imani|Yes. Include [[distal::The confirmed MOD entry includes distal as well as mesial and occlusal; recording MO would omit one of the specified surfaces.]] as well as mesial and occlusal. Do not drop the final letter because the imported print is faint.
Jo|The screen offers existing, planned, and completed. Which status belongs with this entry? I do not want a treatment plan recorded as work already performed.
Dr. Imani|Use [[planned::The dentist explicitly confirms planned status; the dialogue supplies no completed procedure to document or bill as completed.]]. This instruction does not say that today's treatment has been carried out. Keep any existing restoration information separate from this proposed work.
Jo|I have the three parts: Universal twelve, MOD, planned. Does the charting clarification itself confirm consent to proceed today?
Dr. Imani|No. Confirming a record entry is not the whole clinical and consent process. We still follow those processes for the actual patient and proposed care.
Jo|I will not create a completed procedure entry or a charge from this clarification. I will enter only what you have actually confirmed within my authorized role.
Dr. Imani|Good. If the imported record needs an amendment, preserve the [[audit trail::An audit trail preserves the source wording and the dated, attributable clarification instead of concealing the original ambiguity.]]. Do not make it look as though the original system label was present all along.
Jo|There is another twelve on the next page, but it has no tooth name. Should I apply today's clarification to that one too?
Dr. Imani|Not automatically. It may refer to another entry or a different context. Flag it separately so its source and intended tooth can be checked.
Jo|Understood. Today's confirmation covers this entry only. I will leave the second ambiguity visible rather than make the whole record appear reconciled.
Dr. Imani|That is right. Also keep left and right from the patient's perspective. A display facing us does not reverse the anatomical tooth name.
Jo|Final read-back: permanent upper-left first premolar, Universal twelve, equivalent FDI two-four; mesial, occlusal, distal; planned. Separate unlabeled entry still needs clarification.
Dr. Imani|Confirmed. Record this clarification with its source and date through our process. The other entry remains unresolved, and no completed treatment is established by this exchange.""",
        transfer_title="Separate the number from the status",
        transfer_setup="The dentist confirms the permanent upper-right lateral incisor: FDI 12, Universal 7. The entry describes an existing restoration, not a newly completed procedure. The imported notation must remain traceable; the assistant is authorized to record this clarification.",
        transfer="""Assistant: In FDI notation, the confirmed tooth is ___ .|12|FDI twelve identifies the permanent upper-right lateral incisor specified by the dentist.
Dentist: Its Universal designation is ___ .|7|Universal seven identifies that same permanent upper-right lateral incisor, not Universal twelve.
Assistant: The confirmed record status is ___ .|existing|The supplied instruction describes an existing restoration rather than work newly completed at this visit.
Dentist: Preserve the source and clarification in the ___ .|audit trail|The correction must remain attributable and traceable rather than silently erasing the imported notation.""",
        reference=("ADA: Universal Tooth Designation System and ISO equivalents", "https://www.ada.org/-/media/project/ada-organization/ada/ada-org/files/publications/cdt/universal_tooth_designation_system_valueset_2.pdf"),
    ),
    scenario(
        title="Update the medical history",
        skill="Elicit and attribute a reported past reaction, distinguish unknown from none known, and obtain clinical review without diagnosing an allergy.",
        setup="The chart says no known drug allergies. Patient Ravi now reports a past rash after an antibiotic but cannot recall the drug, year, or number of doses. There is no current reaction. Assistant Mei may collect history, but the dentist must assess the report before the visit proceeds.",
        cast="Mei|Dental assistant\nRavi|Patient",
        dialogue="""Mei|Before we continue, has anything changed in your medical history or medicines since the last visit? That includes anything you forgot to mention before.
Ravi|I remembered a rash after an antibiotic years ago. The form says [[no known drug allergies::The existing no-known-allergies entry conflicts with a newly reported possible drug reaction and needs review; it should not be carried forward unquestioned.]], but I am not sure that still describes what I have told you.
Mei|Thank you for raising it. Are you describing a past event, or is anything happening now?
Ravi|A past event. I have no rash or other symptoms now. I cannot remember the [[drug name::The drug name is unknown in the supplied account; choosing a familiar antibiotic would invent information rather than clarify the history.]], though my old pharmacy might have a record.
Mei|I will record what you recall and what you do not. What did you notice at the time, and did anyone assess it?
Ravi|Red, itchy patches on my arms. I spoke to a doctor, but I cannot remember what they called it. That is my [[reported reaction::The reported reaction is Ravi's account of red, itchy patches, not a confirmed allergy diagnosis or a clinician's documented conclusion.]], not a diagnosis I can confirm.
Mei|Do you remember the year, how long you had taken the medicine, or how soon the patches appeared after a dose?
Ravi|No. Please mark the timing as [[unknown::Unknown timing is a missing fact; it must not be converted into an immediate reaction or a statement that no reaction occurred.]]. I do not want to guess a date just to finish the form.
Mei|That is helpful. Do you have a letter, medication list, or other record we could ask about through the proper process?
Ravi|Not with me. I can give the old pharmacy's details. My recollection is the current [[information source::The information source is the patient's recollection until another record is actually obtained and checked; a possible pharmacy record is not yet corroborating evidence.]], not something you have already verified with them.
Mei|Exactly. I will identify you as the source and keep the gaps visible. I will also tell the dentist that the old entry needs review before we proceed.
Ravi|Does that mean you are adding penicillin allergy? That is the antibiotic name people usually mention to me.
Mei|I cannot substitute that name for an unknown medicine or diagnose the cause. The dentist needs to assess your account and decide the appropriate next step.
Ravi|All right. I also started a supplement last month. Do you only need prescribed medicines for this history update?
Mei|Please include the medicines and supplements requested by our history process, including nonprescription products. Bring the names or packaging details rather than relying on a description such as a small white tablet.
Ravi|Should I stop taking my usual tablets until somebody has checked the list?
Mei|I cannot advise you to stop or change them. I will relay that question for [[clinical review::Clinical review is needed for assessment and advice; collecting the history does not authorize the assistant to change medicines or clear the patient for treatment.]], together with the information you have given me.
Ravi|Please make sure the dentist knows I am asking about a past event, not saying I have a reaction here today.
Mei|I will. My handoff will separate the past rash, unknown antibiotic and timing, no current reaction reported, old chart entry, and your question about regular medicines.
Ravi|That is accurate. I can supply the pharmacy details now, but please do not say the history has been confirmed until the proper review has actually happened.""",
        transfer_title="Do not turn uncertainty into an allergy label",
        transfer_setup="A patient reports nausea after a pain medicine two years ago; its name is unknown. No current symptoms are reported. The old chart says no known allergies. The assistant records the account and routes it to the clinician; no allergy diagnosis or advice to change medicines has been given.",
        transfer="""Assistant: The symptom the patient recalls is ___ .|nausea|Nausea is the supplied symptom; replacing it with rash would change the reported history.
Patient: The medicine's name is ___ .|unknown|The patient cannot identify the medicine, so the assistant must not invent a drug name.
Assistant: This is a reported reaction, not a confirmed ___ .|allergy|The facts provide an account requiring assessment, not a clinical conclusion that the reaction was allergic.
Patient: The advice and history update still need clinician ___ .|review|The report has been routed but not clinically assessed or resolved in the supplied exchange.""",
        reference=("NICE CG183: documenting and sharing suspected drug-allergy information", "https://www.nice.org.uk/guidance/cg183/chapter/Recommendations"),
    ),
    scenario(
        title="Check the material, not the box",
        skill="Separate product identity, shade, lot, expiry, and availability when reconciling restorative-material stock.",
        setup="Fictional stock check on 10 October 2026: composite A2 lot C18 has 4 syringes, expiry 30 September; lot C27 has 6, expiry 31 December. Same product and shade. C27's storage and other required checks are verified. The reorder point is 8 usable syringes; target stock is 12, with none on order.",
        cast="Ella|Dental assistant\nSam|Stock lead",
        dialogue="""Ella|The inventory screen shows ten A2 composite syringes, but four belong to a lot that expired on September thirtieth. Today is October tenth.
Sam|Separate physical count from [[usable stock::Only the six verified, in-date syringes count as usable stock; the four expired syringes remain physically present but unavailable for use.]]. Put the expired four on the required hold and check the other lot's identity and status before counting it as available.
Ella|The six are the same product and shade A2, lot C27, expiry December thirty-first. Its storage and other required checks are verified in our record.
Sam|Then usable quantity is six. The [[lot number::The lot number distinguishes C27 from expired C18 even though their product and shade are the same.]] matters because two visually similar boxes can have different histories and expiry dates.
Ella|The reorder point is eight usable syringes. Six is below it, even though the shelf contains ten. Nothing is already on order.
Sam|Raise the order under our process to the target of twelve: [[six::Twelve target syringes minus six usable syringes leaves a six-syringe replenishment requirement, with no outstanding order to subtract.]] additional syringes. Do not order only two; two would reach the trigger, not our stated target.
Ella|I will check the exact product, shade, pack size, and unit of purchase. Six syringes is not automatically six boxes.
Sam|Correct. Also use [[first-expiry-first-out::First-expiry-first-out prioritizes the earliest expiry among eligible stock; it does not authorize using already expired material.]] for eligible stock under our procedure. That means comparing expiry dates, not assuming the oldest delivery is always the first to expire.
Ella|The expired lot arrived later than C27. If I had followed delivery order alone, I would not have caught that difference.
Sam|That is why the [[expiry date::The expiry date is a separate label field from receipt date and lot number; opening or moving a pack does not extend it.]] needs its own check. We do not extend it by opening the box or moving the material to a different drawer.
Ella|There is also an A3 syringe on the shelf. Can I include it in the A2 available count because it is the same product range?
Sam|No. A different shade is not the requested item. Any clinical substitution needs the appropriate decision, not an inventory assumption made to avoid a shortage.
Ella|And the bonding agent is a separate stock item, even though it is used in the same restorative workflow. Its count cannot fill the composite shortage.
Sam|Exactly. Check each product's current [[instructions for use::The instructions for use are product-specific; another material's storage, handling, or curing directions cannot be applied merely because the products are used together.]]. Do not carry over another manufacturer's storage or handling directions because the packaging looks familiar.
Ella|For the expired four, I will record C18, quantity four, the printed expiry, and the hold location. The stock lead will arrange the authorized disposition.
Sam|Keep those units out of available inventory while preserving their traceability. A hold is not the same as a completed supplier return or documented disposal.
Ella|The order request will specify six additional A2 syringes, subject to approval. I will confirm the supplier's pack quantity before sending it.
Sam|And do not add that request to received stock. Approved, ordered, dispatched, and received quantities are different stages, even when we expect delivery soon.
Ella|Summary: ten physical, four expired on hold, six usable, six to replenish to twelve. A3 and bonding agent remain separate items.
Sam|Agreed. Update the counts and the hold record, then route the replenishment request. We have identified the requirement; we have not claimed that new stock has arrived.""",
        transfer_title="Count syringes rather than cartons",
        transfer_setup="Fictional target: 15 usable syringes. There are 5 verified usable syringes and 3 expired units on hold; nothing is on order. The supplier sells cartons of 5 syringes. A purchase request is prepared but neither approved nor received.",
        transfer="""Assistant: Physical quantity is ___ syringes.|8|Five usable plus three expired units equals eight physically present, but not eight usable.
Lead: The replenishment requirement is ___ syringes.|10|The target of fifteen less five usable syringes requires ten additional syringes.
Assistant: That quantity equals ___ supplier cartons.|2|Ten required syringes divided by five per carton equals two cartons.
Lead: New stock has not yet been ___ .|received|Preparing a purchase request does not establish approval, shipment, or physical receipt of supplies.""",
        reference=("GC: composite product identification, shades, and manufacturer instructions", "https://www.gc.dental/india/products/operatory/composite-restoratives/gc-solare-sculpt"),
    ),
]
