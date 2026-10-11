"""Additional radiography cases for access, downtime, and patient control."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Positioning instructions through an interpreter',
    skill='Coordinate interpreted movement instructions without relying on a companion to guess the meaning.',
    setup='Radiographer Ari and qualified interpreter Sol prepare an examination for patient Hana. The script shows coordination before speaking with Hana. The actual examination and patient ability determine the instructions. No positioning technique or permission to proceed is supplied by this language case.',
    cast='Ari | Radiographer\nSol | Qualified interpreter',
    dialogue='''Ari | I want Hana to understand each instruction before moving. Let us agree on short segments and a clear pause.
Sol | Please speak directly to Hana and let me interpret the complete instruction before adding another movement.
Ari | I will use a [[single-step instruction::A single-step instruction asks for one action at a time and allows the patient to understand and respond before another action is added.]] rather than combine turning, lifting, and breathing into one long sentence.
Sol | That will help. If a term is unclear, I will request clarification rather than choose a movement by guesswork.
Ari | I also need to check what Hana can comfortably do before describing any position as agreed.
Sol | I can interpret the question and response without replacing the patient's account with my own assessment.
Ari | We should preserve the [[patient response::The patient response communicates the person's understanding, ability, or concern and must be interpreted rather than supplied by the interpreter.]] exactly, especially if an instruction causes pain or confusion.
Sol | Yes. An interpreter's fluent answer must not be mistaken for the patient's agreement or ability to move.
Ari | Hana's companion has offered to show the movement, but the actual ability and safe approach still need assessment.
Sol | Qualified interpretation supports communication; it does not authorize a companion to move the patient or make clinical decisions.
Ari | I will ask Hana to explain the instruction back before any actual acquisition, when appropriate.
Sol | That [[understanding check::An understanding check asks the patient to demonstrate or restate the meaning and verifies the explanation rather than the interpreter's knowledge.]] should be directed to Hana, not to me as though I were the patient.
Ari | If the instruction needs revision, I will say so clearly rather than change it halfway through your interpretation.
Sol | Please do. A transparent correction prevents the patient from receiving two incompatible instructions without knowing which is current.
Ari | We also need an agreed way for Hana to request a pause during the preparation.
Sol | A [[pause signal::A pause signal provides a clear way for the patient to communicate a need to stop or clarify within the actual examination process.]] can be explained and checked before the procedure begins.
Ari | I will not assume that a nod means every safety question has been answered.
Sol | Nor should silence be treated as [[informed agreement::Informed agreement requires the relevant understanding and authorization rather than being inferred solely from silence or a nod during interpretation.]] without the actual required process.
Ari | Once the explanation is clear, we will proceed only under the real examination checks and authorized plan.
Sol | That preserves [[role boundaries::Role boundaries keep clinical assessment and authorization with the appropriate professionals while the interpreter supports accurate communication.]] while making the instructions accessible to Hana.''',
    transfer_title='Two movements were combined',
    transfer_setup='The radiographer gives two movement instructions together. The interpreter requests separate instructions before the patient moves. The patient has not yet agreed to the movement.',
    transfer='''Interpreter: "Please separate the two ___." | instructions | The interpreter asks for the combined movement directions to be given separately.
Radiographer: "I will give one ___ at a time." | movement | Each instruction will now address one movement rather than two together.
Interpreter: "The patient has not yet ___." | agreed | The scenario states that agreement to the movement is not yet established.
Radiographer: "We will check understanding before ___." | proceeding | The preparation requires a clear explanation and understanding before proceeding.'''),
scenario(title='The imaging worklist is unavailable',
    skill='Use the approved downtime process without creating duplicate or guessed patient records.',
    setup='The imaging worklist is unavailable. Radiographer Ren contacts lead technologist Dev. They use the approved downtime process for identity, request verification, acquisition records, and later reconciliation. No substitute identifiers, device operation instructions, or authorization to bypass checks are supplied.',
    cast='Ren | Radiographer\nDev | Lead technologist',
    dialogue='''Ren | The worklist is unavailable. I can see an appointment message, but I do not want to treat it as a verified order.
Dev | Use the approved downtime process. The outage does not remove identity or examination-verification requirements.
Ren | We need to confirm whether this is a [[system outage::A system outage is loss of access or function in the relevant system and requires the approved continuity process rather than informal workarounds.]] affecting the worklist rather than assume every system is unavailable.
Dev | Correct. State what is affected and what remains accessible without guessing about the technical cause.
Ren | I will not create a new record from a remembered name or use another patient's examination as a placeholder.
Dev | That protects [[patient matching::Patient matching links the correct person with the correct request and record and must remain reliable during downtime.]] and avoids introducing a second identity problem while addressing the first.
Ren | What should we use for recording the examination if the normal electronic workflow cannot be completed?
Dev | Follow the actual [[downtime procedure::The downtime procedure is the approved process for continuing appropriate work during a system interruption and must not be invented in a language exercise.]], including the authorized documentation and verification steps for this service.
Ren | We also need a clear record of what was acquired and when, so the information can be reconciled later.
Dev | Yes. Preserve the required [[acquisition record::An acquisition record documents the actual examination data and timing and is needed for accurate later reconciliation.]] under the approved process rather than relying on memory after the system returns.
Ren | Could entering the same request again create a duplicate if the original reappears?
Dev | It could create a discrepancy. Do not improvise another order or identifier outside the authorized process.
Ren | I will tell the team which examinations remain incomplete in the electronic workflow.
Dev | A clear status prevents an unfinished electronic step from being mistaken for an examination that never occurred.
Ren | When the system is restored, someone needs to check that the records match rather than assume the outage fixed itself.
Dev | Assign [[reconciliation ownership::Reconciliation ownership identifies who will verify and align the downtime records with the restored systems instead of leaving the task unassigned.]] and follow the actual review process.
Ren | That review should also check for duplicate entries and any information still missing.
Dev | Exactly. [[Duplicate prevention::Duplicate prevention avoids creating multiple conflicting records for the same examination and remains important both during downtime and after restoration.]] is part of maintaining a trustworthy record.
Ren | I will report the affected workflow, use the approved process, and keep unresolved items visible.
Dev | Good. Restoration of system access is not proof that every examination record has been correctly reconciled.''',
    transfer_title='Access is restored, reconciliation is not complete',
    transfer_setup='The worklist becomes available again. Two downtime records still need verification against the restored system. No duplicates have been ruled out yet.',
    transfer='''Technologist: "System access is ___." | restored | The worklist is available again in the supplied update.
Lead: "Two records still need ___." | verification | Two downtime records have not yet been checked against the restored system.
Technologist: "Reconciliation is not ___." | complete | Restored access does not establish that all records have been reconciled.
Lead: "Possible duplicates remain ___." | unchecked | The scenario states that duplicate records have not yet been ruled out.'''),
scenario(title='A patient asks to stop the examination',
    skill='Respond to a request to stop without interpreting distress as permission to continue.',
    setup='During preparation, patient Jo asks radiographer Kim to stop because the position is painful and a previous experience was distressing. Kim stops the preparation and seeks the appropriate clinical review. No emergency exception, restraint authorization, or alternative examination decision is supplied.',
    cast='Jo | Patient\nKim | Radiographer',
    dialogue='''Jo | Please stop. That position hurts, and I am remembering a previous examination that was very distressing.
Kim | I am stopping the preparation. Thank you for telling me; we need to understand what is difficult before proceeding.
Jo | I was afraid that once I entered the room I would have no say about what happened next.
Kim | Entering the room is not unlimited permission. Your [[request to stop::A request to stop communicates that the person wants the current activity paused and must not be ignored as automatic consent to continue.]] needs to be heard and handled through the actual clinical process.
Jo | I still want help with the problem that brought me here, but I cannot tolerate this position now.
Kim | That distinction matters. A [[positioning intolerance::Positioning intolerance describes difficulty tolerating a particular position and is not necessarily refusal of every possible examination or care option.]] is not automatically refusal of all care.
Jo | Could you explain what you are going to do before touching my arm again?
Kim | Yes. I will explain and seek the appropriate agreement before any proposed [[physical contact::Physical contact includes hands-on assistance and requires appropriate explanation, agreement, and professional judgment rather than being assumed.]] rather than surprise you with another movement.
Jo | I do not want to describe every detail of the previous experience in order to be believed.
Kim | You do not need to disclose unnecessary personal detail to have the current pain and request acknowledged.
Jo | What happens if the original position is not possible for me today?
Kim | We need the appropriate [[clinical review::Clinical review assesses the actual situation and suitable next step rather than authorizing an improvised alternative from this conversation.]] and authorized approach, not an improvised alternative that I assume will be suitable.
Jo | Will the record say I was difficult, or will it explain what I actually said?
Kim | I will document the pain, the position, and your request factually, avoiding a judgment about your character.
Jo | I would like a support person involved if that can be arranged appropriately.
Kim | We can discuss the actual [[support arrangement::A support arrangement identifies appropriate practical or interpersonal help within the examination's real safety and privacy requirements.]] and the relevant safety and privacy requirements.
Jo | I appreciate knowing that stopping does not mean I will be abandoned without an explanation.
Kim | We should provide a clear next step and contact, while keeping the decision about the examination with the appropriate clinical process.
Jo | Then we can pause, review the options, and avoid pretending that I already agreed to another attempt.
Kim | Correct. A [[revised agreement::A revised agreement concerns the next proposed step after explanation and review and must not be inferred from the earlier preparation alone.]] would need the actual discussion; it has not been assumed here.''',
    transfer_title='The patient agrees to discussion, not movement',
    transfer_setup='A patient agrees to discuss an alternative approach after a pause. The patient has not agreed to another positioning attempt. The clinical review is pending.',
    transfer='''Patient: "I agree to a ___." | discussion | The patient agrees to discussing an alternative, not to performing it.
Radiographer: "Another movement is not yet ___." | agreed | Agreement to conversation does not authorize a positioning attempt.
Patient: "The review remains ___." | pending | The appropriate clinical review has not yet concluded.
Radiographer: "We will explain the proposed next ___." | step | The next proposed action requires explanation after the relevant review.'''),
]
