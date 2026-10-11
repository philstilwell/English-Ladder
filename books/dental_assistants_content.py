"""Original Dental Assisting learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='dental-assistants',
    title='Dental Assisting English',
    cover_label='ENGLISH FOR THE DENTAL TEAM',
    cover_title='Dental\nAssisting',
    cover_size=40,
    tagline='Clarify the request. Support the patient.',
    audience='For dental assistants, dental nurses, chairside support staff, and dental practice teams.',
    map_intro='Clarify appointments and chairside requests, support patient questions, check records, track laboratory work, and communicate aftercare concerns. Three further cases cover tooth notation, medical history, and dental-material stock.',
    notes_title='Clear language supports careful teamwork.',
    notes_intro='Dental assisting combines technical vocabulary, short chairside exchanges, and patient conversations that need time and empathy. A clear question can prevent a wrong assumption. A helpful explanation can acknowledge uncertainty without sounding dismissive.',
    field_notes=[
        ('Separate the appointment from the treatment', 'A schedule entry, a patient expectation, and a clinical treatment decision are different pieces of information. Explain the recorded visit and arrange clarification before assuming agreement to a procedure.', '"The schedule shows a consultation; the dentist needs to clarify the plan with you."'),
        ('Make a concern specific', 'Name the item, missing check, and action needed. Keep an unverified status distinct from a confirmed failure, but do not let schedule pressure turn missing evidence into permission to proceed.', '"I cannot confirm the readiness record for this pack; we need the required check."'),
        ('Check the word you missed', 'Chairside speech can be brief and interrupted. Ask for the distinguishing word and repeat the full request. Knowing two possible instruments does not tell you which one was requested.', '"Did you mean the instrument tray or the impression tray?"'),
        ('Route clinical questions without abandoning them', 'An assistant can recognize and communicate a question while staying within the actual role. Preserve the patient concern and identify the clinician or approved process that can answer it.', '"I cannot interpret the image, but I will ask the dentist to explain what it shows."'),
    ],
    scope_note='All patients, staff, records, schedules, and cases are fictional. This book teaches workplace English, not dental treatment, radiographic interpretation, infection-control certification, or a universal scope of practice. Follow current local law, authorized duties, training, manufacturer instructions, and practice procedures. Use the appropriate urgent or emergency route for urgent concerns; routine callback examples do not replace it. United States and UK sources provide context, not interchangeable legal rules.',
    sources=[
        dict(title='American Dental Association. Dental Assistant.',
             url='https://www.ada.org/resources/careers/career-pathways/dental-assistant',
             note='United States career and role terminology. Permitted duties vary by jurisdiction, qualifications, and actual authorization; examples do not grant clinical authority.', checked='10 October 2026'),
        dict(title='CDC. Sterilization and Disinfection in Dental Settings.',
             url='https://www.cdc.gov/dental-infection-control/hcp/summary/sterilization-disinfection.html',
             note='Background on processing terminology and the importance of verification records. The fictional readiness dialogue is not an instrument-reprocessing procedure.', checked='10 October 2026'),
        dict(title='General Dental Council. Principle Three: Obtain Valid Consent.',
             url='https://standards.gdc-uk.org/pages/principle3/principle3',
             note='UK professional context for ongoing patient communication and consent. Original language scenarios do not substitute for the applicable consent process.', checked='10 October 2026'),
        dict(title='General Dental Council. Principle Four: Maintain and Protect Patients Information.',
             url='https://standards.gdc-uk.org/pages/principle4/principle4',
             note='UK professional context for clear, accurate, confidential records and traceable amendments. Follow actual local requirements for records and disclosure.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Clarifying the appointment purpose',
    scene='A consultation is not a confirmed filling',
    skill='Reconcile a patient expectation with the schedule and arrange an explanation before assuming a treatment decision.',
    brief='Patient Lena arrives expecting a filling today. Assistant Amir sees a thirty-minute consultation on the schedule; no procedure is confirmed. The dentist is available to clarify the purpose before Lena decides whether to continue. Amir should acknowledge the time she has set aside, explain what the record actually shows, and preserve her questions about options, costs, and timing. He cannot promise a filling today, diagnose the tooth, or imply that attending a consultation means agreeing to whatever treatment might later be recommended.',
    cast='Lena | Patient\nAmir | Dental assistant',
    culture=('Correct the expectation without blaming the patient', 'A mismatch may result from several conversations or records. Explain what you can verify and invite clarification without declaring that the patient heard incorrectly. A neutral correction protects trust while leaving clinical decisions with the appropriate person.'),
    a='''What does the schedule show? | A thirty-minute consultation | A completed filling | A guaranteed procedure today | An emergency extraction | The schedule confirms a consultation and its duration, not a particular procedure.
What does Lena expect? | A filling today | A laboratory delivery next week | Only a telephone call | No discussion with a dentist | Lena's expectation is a filling, which differs from the recorded appointment type.
Who can clarify the clinical plan? | The dentist before Lena decides whether to continue | Amir by guessing from the booking length | Another patient in the waiting room | The schedule automatically | The dentist is available to explain the plan; a booking entry does not supply a clinical decision.''',
    vocabulary='''consultation | An appointment for discussion and assessment, not automatic agreement to treatment. | attend a consultation
restoration | Repair or replacement of damaged tooth structure using an appropriate dental method. | discuss a restoration
filling | Material placed to restore a prepared tooth area as clinically indicated. | schedule a filling
appointment type | The category of visit recorded in the schedule. | verify the appointment type
chief concern | The main issue the patient wants addressed. | clarify the chief concern
presenting complaint | The problem or symptom reported at the visit. | record the presenting complaint
clinical examination | Assessment performed by the appropriate clinician. | arrange a clinical examination
treatment plan | The proposed sequence of dental care discussed with the patient. | explain the treatment plan
treatment option | A possible approach requiring appropriate explanation and assessment. | compare treatment options
informed consent | Agreement through the applicable process after relevant understandable information. | support informed consent
provisional recommendation | A recommendation not yet finalized or confirmed. | qualify a provisional recommendation
definitive treatment | Treatment intended to address the identified condition rather than an interim measure. | discuss definitive treatment
caries | Tooth decay; identification and management require clinical assessment. | discuss diagnosed caries
restorative dentistry | Dental care concerned with repairing or restoring teeth and function. | explain restorative dentistry
procedure code | A coded description of a dental service within a particular system. | verify the procedure code
treatment estimate | An estimated cost for specified proposed care. | request a treatment estimate
coverage estimate | An estimate of relevant payment coverage, not a guarantee. | qualify a coverage estimate
referral | A request for assessment or care by another appropriate provider. | confirm the referral
review appointment | A follow-up visit to reassess an issue or treatment. | arrange a review appointment
booking discrepancy | A difference between the recorded booking and the expected visit. | resolve a booking discrepancy
clinical decision | A decision requiring the appropriate clinical assessment and authority. | refer a clinical decision
appointment duration | The allocated length of the visit. | confirm appointment duration
patient expectation | What the patient believes will happen. | acknowledge a patient expectation
decision time | Time for the person to receive information and make the relevant choice. | allow decision time''',
    precision='A thirty-minute booking describes allocated time, not clinical suitability or consent for a filling. Explain the visit type and arrange the clinical discussion. Do not convert a hoped-for treatment into a confirmed procedure because the patient has arrived.',
    precision_extra='The treatment estimate, coverage estimate, and final charge may describe different things. Keep their scope and confirmation status clear. The assistant can help route cost questions without promising insurance payment or diagnosing what treatment will be required.',
    phrases='''Acknowledge the expectation | I understand you expected a filling today.
State the record | The schedule shows a thirty-minute consultation.
Name the difference | That differs from the treatment you were expecting.
Avoid blame | Let us clarify the appointment before making assumptions.
Invite the concern | What would you like the dentist to address first?
Explain the next step | The dentist can discuss the purpose and options with you.
Keep the procedure unconfirmed | No filling is confirmed in the booking I can see.
Respect the decision | You can ask questions before deciding whether to continue.
Avoid a diagnosis | I cannot determine the treatment from the schedule.
Separate attendance and consent | Coming to this visit is not agreement to every possible procedure.
Route cost questions | I will include your question about the treatment estimate.
Qualify coverage | Any coverage estimate needs confirmation through the appropriate process.
Clarify timing | The allocated thirty minutes does not guarantee a procedure today.
Check understanding | Are we clear that the current booking is for consultation?
Preserve the concern | I will tell the dentist that you expected treatment today.
Close the handoff | We will clarify the plan and your questions before treating a procedure as agreed.''',
    notes='''The schedule shows | Identifies the source and limit of the information.
No filling is confirmed | States current booking status without saying a filling is never possible.
Before deciding | Preserves the patient's opportunity to understand and choose.
Cannot determine | Keeps an administrative record separate from diagnosis.
Include your question | Routes the concern without abandoning it.
Allocated thirty minutes | Describes time reserved, not treatment readiness or outcome.''',
    d='''Which response is accurate? | The record shows a consultation; the dentist can clarify the plan before you decide. | A thirty-minute slot guarantees a filling. | You arrived, so you consented to treatment. | The booking proves which tooth needs repair. | The response separates scheduling, clinical explanation, and the patient's decision.
Which statement overpromises? | Your insurance will definitely pay because the visit is booked. | The estimate needs checking. | No procedure is confirmed yet. | The dentist can address your question. | A booking does not establish coverage, payment, or the final treatment charge.
What should be handed to the dentist? | The mismatch between the expected filling and recorded consultation, plus the patient's questions | An invented diagnosis | A statement that all treatment is already accepted | A changed record hiding the original booking | The dentist needs the actual expectation and questions to clarify the visit without fabricated consent or diagnosis.
What does attendance establish by itself? | The patient came to the appointment, not agreement to every procedure | Consent to every possible treatment | Confirmation of clinical suitability | Acceptance of every future cost | Attendance is an event and does not replace the required explanation and consent process.''',
    dialogue='''Lena | I am here for the filling. I took the afternoon off, so I hope we can finish it today rather than arrange another visit.
Amir | I can see why that is frustrating. I will flag the [[patient expectation::The patient expectation is a filling today, which must be acknowledged without treating it as a confirmed booking.]] to the dentist: you came for a filling, but our schedule shows a thirty-minute consultation. No procedure is confirmed yet.
Lena | When I spoke to reception, I mentioned the tooth that was bothering me. I assumed booking an appointment meant booking the treatment as well.
Amir | The [[appointment type::The appointment type identifies the scheduled consultation and does not automatically authorize or confirm treatment.]] matters here. A consultation lets the dentist discuss the concern and appropriate next steps, but I should not tell you that it guarantees a filling today.
Lena | Does the shorter appointment mean the dentist has already decided there is nothing wrong? I do not want my concern dismissed before anyone looks.
Amir | No. The [[appointment duration::Appointment duration is the time allocated in the schedule, not a clinical judgment about the tooth.]] does not establish a diagnosis or the seriousness of your concern. I will tell the dentist what you expected and ask them to clarify the purpose with you.
Lena | My main question is whether this tooth needs a filling at all. I also want to know what the alternatives would involve.
Amir | I can pass on that [[chief concern::The chief concern is the patient's central question about the tooth and treatment options, not an assistant's diagnosis.]]. The dentist needs to assess and explain the options; I cannot determine the treatment from a booking entry or from where you point.
Lena | I would also like to understand the cost before agreeing. I received a number over the phone, but I do not know exactly what it covered.
Amir | We should clarify the [[treatment estimate::The treatment estimate must specify the proposed care and cost basis rather than remain an unexplained number.]] and which service it described. A consultation estimate and an estimate for a particular restoration may not cover the same work.
Lena | The receptionist also mentioned my insurer. Should I assume that the amount above that estimate will be paid by insurance?
Amir | No. A [[coverage estimate::A coverage estimate is provisional payment information and is not a guarantee of insurer payment or final patient cost.]] is not a payment guarantee. I can route the question to the appropriate person so the limits are clear before you rely on it.
Lena | If I stay to talk to the dentist, am I agreeing to go ahead with whatever they recommend during that conversation?
Amir | No. [[Informed consent::Informed consent requires the applicable explanation and agreement process; staying for a consultation is not blanket treatment permission.]] concerns the actual care being proposed and discussed. Attending this visit does not mean you have already accepted every possible procedure or cost.
Lena | Thank you. I want the dentist to know I expected treatment, but I do not want anyone to think I am demanding a procedure that might not be right.
Amir | I will describe the [[booking discrepancy::The booking discrepancy is the difference between the expected filling and recorded consultation, without assigning blame or demanding treatment.]] neutrally. Your expectation and your request to understand the options can both be included, without presenting either as a clinical decision.
Lena | Then I would like to ask the dentist to explain what can be decided today and whether another appointment might be needed.
Amir | That is a useful question about the [[treatment plan::The treatment plan concerns the proposed care and sequence; the dentist must explain it rather than the assistant promise same-day treatment.]]. I will make sure it reaches the dentist rather than promise that today's allocated time can accommodate any treatment that may be recommended.
Lena | All right, I will speak to the dentist first. Please mention the time off work too. Another appointment would take some arranging.
Amir | I will. We will allow [[decision time::Decision time gives the patient an opportunity to understand the explanation and ask questions before agreeing to the proposed next step.]] for that discussion and keep the current status clear: consultation booked, procedure unconfirmed, and your questions still to be answered.''',
    rehearsal=('Read Lena and Amir aloud; stress consultation and no procedure confirmed.', 'Repeat the exchange with the crown-fitting facts below. Keep the twenty-minute duration separate from readiness.', 'Check that neither speaker promises treatment or insurance payment; use the numbered answers to correct the four blanks.'),
    transfer_title='Clarify a review rather than a procedure booking',
    transfer_setup='A patient expects a crown fitting. The schedule shows a twenty-minute review, and the dentist has not confirmed fitting readiness. The patient asks about timing and the estimate.',
    transfer='''Assistant: "The recorded appointment type is a ___." | review | The schedule states a review rather than a confirmed fitting procedure.
Patient: "I expected a ___." | crown fitting | Crown fitting is the patient's stated expectation, not the confirmed booking.
Assistant: "The allocated time is ___ minutes." | twenty | The supplied schedule allocates twenty minutes and does not guarantee a procedure.
Assistant: "Fitting readiness remains ___." | unconfirmed | The dentist has not confirmed readiness, so the assistant must preserve that status.''',
))

BOOK['units'].append(unit(
    title='Room readiness and safe clarification',
    scene='The pack is present; readiness is not verified',
    skill='Raise an unresolved instrument-readiness check clearly and seek a verified replacement without waiving the practice process.',
    brief='Assistant Tessa sees instrument pack P18 in the treatment room. The required readiness documentation cannot be confirmed, and the dentist is about to begin. Tessa has not released the pack for use and is not authorized to waive the practice checks. Lead assistant Bruno can investigate and may have a verified replacement. No contamination or sterilization failure has been established in the supplied facts. The immediate communication task is to make the unresolved check visible, keep the pack from being used until properly resolved, and follow the actual practice procedure.',
    cast='Tessa | Dental assistant\nBruno | Lead assistant',
    culture=('A clear interruption can protect the workflow', 'A junior worker may hesitate when the team is ready to begin. Name the specific unresolved check and the needed action. A factual concern is not a personal accusation, and politeness should not make a request to pause sound optional.'),
    a='''What is known about P18? | It is present, but required readiness documentation cannot be confirmed. | It has been proved contaminated. | Every required check has passed. | It was already used on the patient. | The brief establishes an unresolved verification gap, not a confirmed failure or completed readiness.
What may Bruno provide? | A replacement whose readiness has been verified | An automatic waiver for every pack | Permission inferred from the busy schedule | A guaranteed replacement before checking | A verified replacement may be available, but availability itself has not yet been confirmed.
What must not happen? | Treating pack presence as permission to skip the required checks | Reporting the gap | Asking for clarification | Identifying P18 in the record | The assistant lacks authority to waive checks, and physical presence does not establish readiness.''',
    vocabulary='''instrument pack | A packaged set of dental instruments with a defined processing and use status. | identify the instrument pack
reprocessing | The required sequence for preparing a reusable device for further use. | follow reprocessing instructions
decontamination | Removal or reduction of contamination through the applicable process. | follow decontamination procedures
cleaning | Removal of soil and material, distinct from sterilization. | verify the cleaning step
disinfection | A process reducing or inactivating specified microorganisms under defined conditions. | distinguish disinfection from sterilization
sterilization | A validated process intended to eliminate viable microorganisms, including spores. | verify sterilization records
sterilizer | Equipment used for an appropriate sterilization process. | identify the sterilizer
cycle record | Documentation of a particular processing cycle. | trace the cycle record
load number | The identifier linking items to a particular processing load. | verify the load number
mechanical monitoring | Checking process parameters such as time, temperature, and pressure as applicable. | review mechanical monitoring
chemical indicator | A material showing exposure to specified process conditions. | inspect the chemical indicator
biological indicator | A test system using resistant microorganisms to assess the sterilization process. | review biological indicator results
pack integrity | The condition of the packaging and its protective barrier. | check pack integrity
compromised packaging | Packaging whose protective condition has been damaged or otherwise impaired. | report compromised packaging
IFU | Instructions for use; the relevant manufacturer's directions. | consult the IFU
single-use device | A device intended for one use under its labeling. | identify a single-use device
reusable device | A device intended for further use after the specified reprocessing. | identify a reusable device
readiness documentation | Records needed to establish the relevant item is ready under the procedure. | confirm readiness documentation
traceability | Ability to connect an item with relevant identity and processing history. | maintain traceability
release status | Whether an item is authorized for use under the required checks. | confirm release status
hold | A status preventing use pending the appropriate resolution. | maintain the hold
verified replacement | An alternative item whose required readiness has been confirmed. | obtain a verified replacement
processing deviation | A departure from the specified processing requirement. | report a processing deviation
infection prevention | Measures intended to reduce the risk of infection transmission. | follow infection prevention procedures''',
    precision='Present, packaged, clean, disinfected, and sterile are not interchangeable statuses. Recognition of an indicator or a sealed pack does not replace the required combined checks, records, and manufacturer directions. This unit practices clarification, not a processing protocol.',
    precision_extra='Cannot confirm readiness is more accurate than confirmed contaminated when no failure has been established. The distinction does not justify use. Keep the unresolved status visible and follow the actual hold, review, replacement, and release process.',
    phrases='''Interrupt clearly | Please pause; I cannot confirm the required readiness check for P18.
Identify the item | The concern is about pack P18 in this room.
State the gap | The required documentation is not available for verification.
Avoid an unsupported finding | I am not reporting a confirmed contamination event.
Prevent an assumption | The pack being present does not establish its release status.
Name the limit | I am not authorized to waive this check.
Request the lead | Can you review the status through the practice procedure?
Ask about an alternative | Is a verified replacement available?
Keep a hold visible | This pack should not be used while the required check remains unresolved.
Preserve traceability | Keep the pack identifier linked to the review record.
Clarify the evidence | Which record confirms the relevant processing and release checks?
Reject schedule pressure | The appointment timing does not complete the missing check.
Confirm the replacement | Please confirm the replacement identifier and verified status.
Separate two outcomes | Replacing the pack does not by itself resolve the original documentation issue.
Record the action | I will record the concern and the action actually taken.
Close the loop | We need an explicit readiness confirmation before describing the setup as ready.''',
    notes='''Please pause | Makes the immediate action clear without blaming a colleague.
Cannot confirm | Identifies missing verification rather than inventing a result.
Not authorized to waive | Names the actual authority boundary.
Verified replacement | Requires readiness as well as physical availability.
By itself | Prevents a workaround from being mistaken for resolution of the original issue.
Explicit confirmation | Avoids assuming that silence or activity means release approval.''',
    d='''Which message is best? | Please pause; P18's required readiness record is unconfirmed, and I need the approved review or a verified replacement. | The pack looks clean, so it must be ready. | Every instrument is contaminated, without evidence. | We can waive the check because the dentist is waiting. | The message identifies the item, gap, and appropriate response without guessing a result or waiving the process.
What does a color change alone establish here? | Not completion of every required readiness check | That the pack's release record is complete | That the biological monitoring result has passed | That pack integrity no longer needs checking | A single observation does not replace the complete applicable verification process.
What should happen to the original issue if a replacement is found? | It remains subject to the required review and record process. | It automatically disappears from all records. | It proves P18 was contaminated. | It permits changing the old record to show prior verification. | A replacement supports the immediate workflow but does not establish or erase the original pack's history.
Which statement is precise? | Readiness is unverified; no confirmed failure is established in the supplied facts. | Readiness and contamination are identical words. | Missing records prove every cycle failed. | No documented failure means automatic permission to use the pack. | The statement preserves uncertainty while avoiding both a fabricated failure and an unsupported release.''',
    dialogue='''Tessa | Bruno, please pause the setup. Pack P18 is present, but I cannot confirm its required readiness documentation, and the dentist is about to begin.
Bruno | P18, understood. Has that [[instrument pack::The instrument pack identifier makes the concern specific and prevents confusion with another item or replacement.]] been opened or used? Tell me where it is now so nobody picks it up while I check the record.
Tessa | It has not been used. I have not released it, and I do not have authority to waive the missing check just because the room is busy.
Bruno | Then keep the [[release status::Release status remains unconfirmed because the required checks have not been established; a busy schedule does not authorize use.]] unresolved under our procedure. I will help review the record rather than treat the presence of the pack as proof that it is ready.
Tessa | The package is here, but I do not want to say it is contaminated. The issue I can establish is that the required documentation cannot be confirmed.
Bruno | That is the right distinction. We need the [[readiness documentation::Readiness documentation supports the required verification; its absence is a gap, not by itself a confirmed contamination finding.]], not an invented finding of failure or a reassuring assumption. The uncertainty still means we must not bypass the check.
Tessa | Would a replacement solve the immediate setup problem? I heard there might be another pack, but I have not checked its identity or status.
Bruno | A [[verified replacement::A verified replacement must have its own readiness established; merely finding another package is insufficient.]] may be available. I will check the actual alternative and its required status, not simply swap one unverified package for another because it is nearby.
Tessa | If we locate the original record, we also need to know that it belongs to P18 rather than a similar pack from another processing load.
Bruno | Correct. [[Traceability::Traceability connects the particular pack to its relevant processing history rather than accepting an unrelated record.]] connects the item to the relevant history. A complete-looking record for a different load would not answer the question about this pack.
Tessa | I can give you the identifiers shown without altering anything. I do not want to copy a number from another pack into the missing record.
Bruno | Preserve the actual [[load number::The load number identifies the relevant processing load; substituting another number would break the factual link.]] and follow the documentation process. A guessed identifier would hide the problem rather than establish that the required processing and checks occurred.
Tessa | Someone asked whether the visible indicator was enough. I was unsure how to explain why one visible feature did not settle every readiness question.
Bruno | A [[chemical indicator::A chemical indicator relates to specified process exposure and does not independently establish every readiness requirement.]] has a defined purpose, but it is not a substitute for all applicable checks. We need the practice process and manufacturer instructions followed, not an isolated shortcut.
Tessa | I will tell the dentist that I have raised the specific gap and that you are checking the record and a possible verified alternative.
Bruno | Keep the [[hold::The hold prevents premature use while the identified verification issue is being resolved through the required process.]] visible. I am checking the replacement now; please tell the dentist that setup is still waiting for verification, not ready yet.
Tessa | If another pack is confirmed, should I describe the entire issue as closed, or distinguish the replacement from the original record question?
Bruno | Distinguish them. The [[cycle record::The cycle record concerns the original processing history, which still needs the appropriate review even if a replacement is available.]] issue may require further review even after the immediate setup has an acceptable alternative. Do not erase the first concern from the history.
Tessa | Understood. I will record the actual pack status, whom I contacted, and any verified replacement details, without claiming a failure that has not been found.
Bruno | And follow the relevant [[IFU::The instructions for use are the manufacturer's applicable directions and remain part of the required process, not an optional reference.]] and practice procedures for the item. Our handoff should end with explicit confirmed facts, not with the assumption that someone else must have completed the check.''',
    rehearsal=('Read the pause request aloud with P18 and the missing readiness record clearly audible.', 'Repeat the four-line transfer using its different pack and check; do not call an unresolved check a confirmed contamination event.', 'Check the answers, then repeat the difference between a verified replacement and resolution of the original record issue.'),
    transfer_title='Identify a different unresolved readiness check',
    transfer_setup='Pack Q7 has not been used. Its required readiness check is unconfirmed. Lead assistant Eva can review it; a replacement has been requested but not yet verified.',
    transfer='''Assistant: "The affected pack is ___." | Q7 | Q7 is the specific item whose readiness remains unresolved.
Lead: "Its use status is ___." | not used | The brief explicitly states that the pack has not been used.
Assistant: "The review contact is ___." | Eva | Eva is the lead assistant identified for the review.
Lead: "The replacement is requested but not yet ___." | verified | A replacement request does not establish the alternative item's readiness.''',
))

BOOK['units'].append(unit(
    title='Chairside requests and read-backs',
    scene='Which tray did you mean?',
    skill='Identify the word you missed, request the distinguishing detail, and confirm the full chairside instruction before acting.',
    brief='During a setup briefing, assistant Noor hears Dr. Shaw say "tray" but misses the rest because another conversation interrupts. The setup list contains both an instrument tray and an impression tray. Noor has not selected either. She needs to ask which item is intended and read back the complete request before continuing under practice procedures. The dentist then clarifies that the instrument tray is wanted for the current setup. Knowing the general treatment context does not justify guessing the missing instruction, and this language exercise does not authorize a clinical procedure.',
    cast='Noor | Dental assistant\nDr. Shaw | Dentist',
    culture=('A brief clarification is professional', 'Fast speech and local shorthand can make an unfamiliar term seem obvious to everyone else. State exactly what you heard and what you missed. A precise question is more useful than a vague yes, an apology repeated several times, or a silent guess.'),
    a='''Which word did Noor hear? | Tray | Instrument | Impression | A confirmed size | The brief says tray was audible while the distinguishing part was missed.
What are the two listed possibilities? | Instrument tray and impression tray | Two confirmed identical instruments | A radiograph and a consent form | Two appointment times | Both tray types appear on the setup list, making the incomplete request ambiguous.
What does the dentist clarify? | The instrument tray is wanted for the current setup. | Noor should guess each future request. | The impression tray was already selected. | Every clinical check is waived. | The clarification resolves the current item while leaving ordinary practice procedures in place.''',
    vocabulary='''chairside | Relating to assistance beside the dental chair during care. | provide chairside support
setup briefing | A discussion confirming the planned equipment and arrangements. | conduct a setup briefing
instrument tray | A tray used to organize the relevant dental instruments. | confirm the instrument tray
impression tray | A device used to hold impression material under the appropriate procedure. | identify the impression tray
impression | A negative reproduction used in making a model of oral structures. | distinguish an impression from a scan
intraoral scan | A digital capture of structures inside the mouth. | identify the intraoral scan
mirror | A dental instrument used for viewing or related clinical purposes. | identify the requested mirror
explorer | A dental examination instrument used by appropriately trained personnel. | identify the explorer
periodontal probe | An instrument for periodontal measurements under the relevant clinical procedure. | distinguish the periodontal probe
cotton pliers | An instrument for handling suitable small materials. | identify the cotton pliers
HVE | High-volume evacuation; a dental suction system or device. | clarify the HVE request
saliva ejector | A suction device intended for removing saliva under its specified use. | distinguish the saliva ejector
air-water syringe | A dental device delivering air, water, or a combination under its design. | identify the air-water syringe
handpiece | A powered dental instrument used with specified attachments. | clarify the handpiece type
bur | A rotary cutting or finishing attachment with a particular design and purpose. | verify the bur identifier
matrix band | A device used to provide a temporary wall during certain restorations. | identify the matrix band
wedge | A small device used for specified separation or adaptation tasks in dentistry. | clarify the requested wedge
curing light | A device used to initiate setting of compatible dental materials. | identify the curing light
retractor | An instrument or device used to hold tissue away as appropriate. | identify the retractor
distinguishing detail | The feature that separates one possible request from another. | request the distinguishing detail
read-back | Repeating an instruction to check it was heard correctly. | give a complete read-back
closed-loop request | A request followed by acknowledgment and confirmation of the intended information. | complete a closed-loop request
ambiguous instruction | Wording that supports more than one interpretation. | clarify an ambiguous instruction
interruption | Something that breaks attention or prevents hearing the full message. | acknowledge an interruption''',
    precision='Instrument tray and impression tray share a word but identify different items. Repeat the distinguishing term, not only tray. The same principle applies to size, identifier, side, and timing when those details are part of the actual request.',
    precision_extra='Recognizing a term does not demonstrate competence to use the equipment. These definitions support listening and clarification. Follow the actual procedure, training, and authorization; a successful read-back confirms communication, not every separate readiness or safety requirement.',
    phrases='''Signal the gap | I heard tray, but I missed the word before it.
Name the interruption | Another conversation covered the rest of the request.
Offer the alternatives | Did you mean the instrument tray or the impression tray?
Avoid guessing | I have not selected either yet.
Ask for the whole request | Could you repeat the full item name?
Read back | The instrument tray for the current setup, correct?
Check a modifier | Which size or identifier did you specify?
Clarify sequence | Do you need that now or at the next stage?
Confirm a correction | Thank you; I will use the corrected request.
Avoid vague agreement | I need to confirm the item before saying it is ready.
Keep checks separate | Hearing the request correctly does not replace the readiness checks.
Name unfamiliar shorthand | I do not know that abbreviation in this practice.
Request ordinary wording | Could you say the full name once?
State what is confirmed | We have confirmed the instrument tray, not the impression tray.
Protect the handoff | I will pass on the complete request rather than the shortened version.
Close the loop | I have repeated the item, and you have confirmed it.''',
    notes='''I heard, but I missed | Separates the reliable part of the message from the missing part.
Did you mean X or Y | Narrows a genuine ambiguity to the stated alternatives.
Not selected either | Confirms that no guess has already become an action.
Correct? | Invites explicit confirmation of the repeated instruction.
Full name once | Requests efficient clarification without a lengthy apology.
Does not replace | Keeps communication confirmation distinct from other required checks.''',
    d='''Which question best resolves the actual ambiguity? | Did you mean the instrument tray or the impression tray? | You said tray, so either must be acceptable. | Shall I choose the one nearest me? | Can I ignore the rest because I heard one word? | The question identifies the two relevant alternatives and requests the missing distinction.
Which read-back is complete for the clarified request? | The instrument tray for the current setup, correct? | The tray from yesterday, correct? | The impression tray for the current setup, correct? | The instrument tray for the next appointment, correct? | The complete read-back preserves the distinguishing item and current context.
What should Noor do with unfamiliar local shorthand? | Ask for the full name and confirm the intended meaning. | Pretend every abbreviation is universal. | Choose an item based only on its color. | Change the request without telling anyone. | Local shorthand can vary, so explicit clarification is more reliable than assumed meaning.
What does confirmation of the request establish? | Shared understanding of the requested item, not completion of all readiness checks | Universal competence to use all devices | A waiver of the practice procedure | Consent for an unrelated treatment | A communication check resolves the instruction while separate procedural requirements remain applicable.''',
    dialogue='''Noor | Dr. Shaw, I heard tray, but the conversation by the door covered the first word. Instrument tray or impression tray? I have not selected either.
Dr. Shaw | Sorry about the [[interruption::The interruption masked part of the request; it does not justify choosing an item by guesswork.]]. The instrument tray for this setup, please. The impression tray is not part of this request.
Noor | Instrument tray for the current setup, correct? I will check its readiness status before bringing it over. The other tray will stay where it is.
Dr. Shaw | Correct; that [[read-back::The read-back repeats the item and timing so the dentist can confirm the intended request.]] matches. Also, have the high-volume evacuator ready under our normal checks. We will confirm the remaining equipment during the briefing.
Noor | I heard suction from the doorway earlier. Do you mean the HVE rather than the saliva ejector? Both are on the equipment list.
Dr. Shaw | Yes, HVE. That is the [[distinguishing detail::Naming HVE distinguishes the requested high-volume evacuator from the listed saliva ejector.]] I left out earlier. Please keep those names separate when you pass the request to Marta.
Noor | HVE confirmed. Marta has asked which tray to bring. I will give her the full item name and tell her this is for the current setup.
Dr. Shaw | Ask her for the [[instrument tray::Instrument tray is the requested item, rather than the separate impression tray on the list.]], with the required readiness checks completed. If she cannot confirm its status, have her tell us before it reaches the setup.
Noor | One more point: someone put small suction on the handwritten list. Is that your request, or a note carried over from the previous appointment?
Dr. Shaw | I cannot tell from that note. Treat it as an [[ambiguous instruction::Small suction does not reliably identify the device or whether this handwritten request is current.]], not a substitute for the HVE request we have just confirmed. I will check its source.
Noor | I will mark that question as unresolved. I will not remove an equipment requirement merely because the handwriting is unclear. We still need to establish what it refers to.
Dr. Shaw | During the [[setup briefing::The setup briefing is the appropriate point to reconcile the equipment list before relying on it.]], we will reconcile that note with the actual list. Please bring the original wording so I can see what needs clarification.
Noor | For any size-specific request, please include the size in the full name. I missed a modifier in yesterday's briefing and had to ask again.
Dr. Shaw | Of course. In a [[chairside::Chairside exchanges take place beside the dental chair, where short requests still need precise identifying details.]] exchange, say which part you missed. I would rather repeat one size than discover that we understood different items.
Noor | Marta is here now. She has repeated instrument tray and HVE. She also wants to confirm that you did not request impression equipment at this stage.
Dr. Shaw | Correct: no [[impression tray::The impression tray is specifically excluded from this current request, not declared unnecessary for every appointment.]] in this request. That is about our current setup, not a change to another patient's appointment or planned equipment.
Noor | I have repeated that to Marta, and she has confirmed it back. She is checking the tray's readiness and will report before bringing it across.
Dr. Shaw | That completes the [[closed-loop request::The receiver repeats the specific request and the requester confirms it, closing the communication loop.]]. Let me know if the check is unresolved; an accurate equipment name does not settle its processing status.
Noor | My note reads: instrument tray and HVE for this setup, checks required; small suction note awaiting clarification. Marta has those same details.
Dr. Shaw | That is the [[handoff::The handoff transfers the confirmed items and the still-unresolved note without concealing either status.]] I need. Bring the handwritten list to the briefing, and we will settle the remaining point before relying on it.''',
    rehearsal=('Read the chairside briefing in pairs; pause after each read-back for the confirming reply.', 'Repeat the suction-device transfer, clearly distinguishing HVE from saliva ejector.', 'Use the key to correct the four blanks, then repeat the final line without implying that identification completes readiness checks.'),
    transfer_title='Clarify a suction-device request',
    transfer_setup='During a briefing, an assistant hears suction but misses the device name. The list includes an HVE device and a saliva ejector. The dentist clarifies HVE for the current setup; normal checks remain required.',
    transfer='''Assistant: "I heard suction but missed the ___." | device name | The missing information is the distinguishing device name, not the general word suction.
Dentist: "The requested device is ___." | HVE | The dentist specifically clarifies HVE rather than the saliva ejector.
Assistant: "I will confirm it with a complete ___." | read-back | Repeating the complete request lets the dentist confirm or correct the understanding.
Dentist: "The ordinary readiness checks remain ___." | required | Clarifying the device does not waive separate readiness requirements.''',
))

BOOK['units'].append(unit(
    title='Imaging questions and authorization',
    scene='Explain the route to an answer, not the image',
    skill='Acknowledge a question about dental imaging and arrange clinical explanation without interpreting findings or promising treatment.',
    brief='Patient Marco looks at a dental image and asks assistant Suki whether it proves that a tooth needs treatment. The dentist has not yet discussed the image with him. Suki is assisting with the visit and is not authorized to interpret the image or recommend treatment. She can identify the question, explain her role, and ask the dentist to discuss the findings and their significance. No finding, diagnosis, or treatment decision is supplied in this case. Technical vocabulary supports communication; it does not qualify a learner to read an image.',
    cast='Marco | Patient\nSuki | Dental assistant',
    culture=('Technical confidence should not become a diagnosis', 'A patient may expect any team member near an image to explain it. Acknowledge the specific question and make the route to an answer clear. Avoid casual reassurance or an alarming guess based on an apparent shadow, color, or shape.'),
    a='''What does Marco ask? | Whether the image proves that a tooth needs treatment | Whether the laboratory confirmed delivery | Which pack was processed | Whether his appointment was cancelled | The question concerns interpretation and treatment significance of the image.
What is Suki not authorized to do here? | Interpret the image or recommend treatment | Acknowledge the question | Ask the dentist to explain | Preserve the patient's concern | The fictional role expressly excludes image interpretation and treatment recommendation.
What clinical finding is established in the brief? | None | A confirmed cavity | A confirmed fracture | A definite need for extraction | The brief supplies a patient question but no interpreted finding or diagnosis.''',
    vocabulary='''radiograph | An image produced using X-rays. | identify the radiograph
radiography | The process of producing radiographic images under the applicable rules. | distinguish radiography from interpretation
intraoral image | In dental radiography, an image obtained with the receptor inside the mouth. | identify an intraoral image
extraoral image | In dental radiography, an image obtained with the receptor outside the mouth. | identify an extraoral image
bitewing | A dental radiographic view commonly showing crowns of upper and lower teeth and nearby structures. | identify the bitewing view
periapical image | A dental image showing a tooth and the area around its root tip. | identify a periapical image
panoramic image | A broad dental image of the jaws and surrounding structures. | identify a panoramic image
CBCT | Cone-beam computed tomography; three-dimensional X-ray imaging used for appropriate indications. | identify the CBCT study
image receptor | The film or digital sensor receiving the image information. | identify the image receptor
field of view | The area or volume included in an imaging examination. | clarify the field of view
exposure | The use of radiation to obtain an image under an authorized process. | document the exposure
image quality | Whether an image meets the relevant technical requirements for its intended use. | assess image quality within role
artifact | An image feature introduced by a technical or other non-anatomical factor. | report a possible artifact
radiolucent | Appearing relatively darker on a radiograph because more X-rays reach the receptor. | recognize the term radiolucent
radiopaque | Appearing relatively lighter on a radiograph because fewer X-rays reach the receptor. | recognize the term radiopaque
anatomical structure | A part of the body represented or examined. | identify the named anatomical structure
image interpretation | Professional assessment of what an image shows and means. | refer image interpretation
clinical finding | Information established through the appropriate clinical assessment. | explain a clinical finding
diagnostic significance | The relevance of information to identifying a condition. | ask about diagnostic significance
correlation | Considering information together with other relevant findings. | correlate clinical information
comparison image | An earlier or other image used for a defined comparison. | identify the comparison image
image annotation | A label or mark added to an image with its meaning and source identified. | clarify an image annotation
treatment indication | The clinical reason for considering a particular treatment. | explain the treatment indication
authorized interpreter | A professional permitted and qualified to interpret the relevant image. | refer to the authorized interpreter''',
    precision='Acquiring, labeling, displaying, and interpreting an image are different activities. The actual role and local rules determine who may do each. A visible feature or a technical term does not establish a diagnosis or make an assistant authorized to provide one.',
    precision_extra='An image may contribute to a clinical assessment, but the learner is not given a finding to interpret here. Preserve the question about treatment need and ask the dentist to explain the evidence, relevant uncertainty, and options in understandable terms.',
    phrases='''Acknowledge the question | You want to know whether the image means this tooth needs treatment.
State the role | I am not authorized to interpret the image.
Offer the next step | I will ask the dentist to explain the findings with you.
Avoid a visual guess | I cannot identify a diagnosis from that feature for you.
Avoid false reassurance | I should not tell you everything is normal without the clinical explanation.
Separate process and meaning | Helping with an image is different from interpreting it.
Preserve the exact concern | I will include your question about whether treatment is necessary.
Ask for ordinary language | Could the dentist explain that term in everyday language?
Clarify an annotation | Please ask the clinician what that marked area refers to.
Keep decisions open | No treatment decision has been explained in this conversation yet.
Invite evidence questions | You can ask how the image relates to the rest of the examination.
Distinguish alternatives | You can ask which options are being considered and why.
Avoid overstating proof | I cannot say the image alone proves a particular treatment is needed.
Route a technical question | The clinician can explain the significance of that imaging term.
Check the handoff | I will make sure the question reaches the dentist before you decide.
Close without abandonment | I cannot give the interpretation, but I can help you get a clear answer.''',
    notes='''You want to know whether | Restates the substance instead of answering a different question.
Not authorized to interpret | Identifies the specific boundary without denying the patient's right to an explanation.
How it relates | Invites an explanation of the whole clinical assessment.
No decision explained yet | Describes the current conversation without claiming no clinical assessment exists elsewhere.
In everyday language | Requests accessible explanation rather than less accurate information.
Before you decide | Connects understanding with the patient's actual choice.''',
    d='''Which response is appropriate? | I cannot interpret it, but I will ask the dentist to explain whether it supports treatment and why. | The dark area definitely proves decay. | Everything is normal because you are not in pain. | Any image means treatment is compulsory. | The response preserves the treatment question and routes interpretation to the appropriate clinician.
What is wrong with labeling an unexplained feature a cavity? | No interpreted finding is supplied, and Suki lacks authorization to diagnose it. | Every dark feature always means the same thing. | The patient has already received an explanation. | The schedule supplies diagnostic proof. | The proposed label invents a clinical conclusion that neither the facts nor the assistant's role supports.
Which distinction is necessary? | Producing an image and interpreting it are different activities. | Displaying the image confirms the diagnosis recorded elsewhere. | Correctly positioning a receptor establishes authority to recommend treatment. | Knowing the term radiolucent establishes what this feature represents. | Tasks connected with imaging have different competencies and permissions, so they cannot be treated as interchangeable.
Which question should reach the dentist? | Does the image support treatment, and how does it relate to the examination and options? | Can the assistant invent a reassuring result? | Can all uncertainty be deleted from the record? | Can an annotation replace the explanation? | The question seeks the actual clinical significance and options rather than an unsupported shortcut.''',
    dialogue='''Marco | Suki, I can see a darker area on this picture. Does that prove the tooth needs treatment, or am I misunderstanding what I am looking at?
Suki | You are asking about [[diagnostic significance::Diagnostic significance concerns what the image means for identifying a condition, which requires the appropriate clinical explanation.]]. I am not authorized to interpret the image, but I will ask the dentist to explain the finding, if any, and how it relates to treatment.
Marco | I thought you could explain it because you displayed it. Who should I ask about that darker patch?
Suki | Displaying a [[radiograph::A radiograph is the X-ray image; displaying it does not establish authority to diagnose or explain every feature.]] and interpreting it are different tasks. I can help communicate the question without giving you a diagnosis from something I see on the display.
Marco | Is darker always worse? I have heard words used for dark and light areas, but I do not know whether they describe a disease.
Suki | Terms such as [[radiolucent::Radiolucent describes relative image appearance and is not, by itself, the name of a disease or treatment decision.]] describe image appearance, not a diagnosis by themselves. The dentist can explain the relevant terminology in context rather than have us attach a condition to an isolated word.
Marco | Then I should ask what the feature actually represents. I would also like to know whether anything else in the examination supports the same conclusion.
Suki | That is a question about [[correlation::Correlation here means considering the image alongside other relevant clinical information, not treating one feature as sufficient proof.]] with other clinical information. I will pass it on along with your question about whether a treatment recommendation is supported and what alternatives exist.
Marco | There is also a mark on the screen. I cannot tell whether it is part of the original image or something someone added to point out an area.
Suki | The clinician can clarify that [[image annotation::An image annotation is an added label or mark whose purpose and source need explanation rather than assumed diagnostic meaning.]] and what it refers to. I should not guess the purpose of a mark or present it as proof of a particular condition.
Marco | Could it be a technical issue instead? I am not asking you to decide that, but I would like the dentist to address the possibility.
Suki | I will include your question about a possible [[artifact::An artifact is a feature introduced by a technical or other non-anatomical factor; its presence here has not been established.]]. We should keep that as a question, not replace one unsupported conclusion with another.
Marco | I appreciate that. I do not want reassurance if it is not justified, but I also do not want a frightening answer based on a guess.
Suki | The [[authorized interpreter::The authorized interpreter is the appropriately qualified professional who can assess the image within the actual clinical and legal framework.]] can explain what is established and what remains uncertain. I can make sure your concern is heard without telling you that everything is normal or definitely abnormal.
Marco | If a treatment is recommended, I want to understand why that treatment follows from the evidence rather than think the picture makes the decision automatically.
Suki | I will ask the dentist to explain the [[treatment indication::The treatment indication is the clinical reason for considering treatment, which must be explained rather than inferred from merely having an image.]] in ordinary language. An image on a screen is not a substitute for the discussion you need before deciding.
Marco | Would an earlier image matter? Has the dentist compared this with my previous image?
Suki | You can ask whether a [[comparison image::A comparison image is another image used for a defined clinical comparison; the scenario does not establish that one was reviewed.]] was relevant and reviewed. I will not say that comparison has happened unless it is confirmed in the actual explanation.
Marco | Please ask what the patch means and whether it matches the examination. That is what I need to understand first.
Suki | I will preserve them for the [[image interpretation::Image interpretation is the professional assessment the patient is requesting; the assistant's handoff supports but does not supply it.]] discussion. We have identified the questions, not a diagnosis or an agreed procedure, and I will help you obtain the clinical explanation.''',
    rehearsal=('Read Marco and Suki aloud; keep radiolucent distinct from a diagnosis.', 'Repeat the transfer with radiopaque and crown. Preserve the question rather than confirming a need for treatment.', 'Check all four answers, then read the corrected handoff to the dentist aloud.'),
    transfer_title='Route a question about an imaging term',
    transfer_setup='A patient asks whether a note saying radiopaque proves that a tooth needs a crown. The assistant is not authorized to interpret the image. The dentist has not yet explained the note.',
    transfer='''Assistant: "The term in your question is ___." | radiopaque | Radiopaque is the supplied image-appearance term, not a confirmed treatment indication.
Patient: "I want to know whether I need a ___." | crown | The patient asks about a crown, but the question does not establish that it is needed.
Assistant: "The explanation needs the ___." | dentist | The dentist is the identified clinician who can explain the note and its significance.
Assistant: "No treatment conclusion has been ___ here." | established | The brief supplies no interpreted finding or confirmed treatment decision.''',
))

BOOK['units'].append(unit(
    title='Patient comfort, questions, and pauses',
    scene='Reassure without promising a painless procedure',
    skill='Acknowledge dental anxiety, communicate a comfort concern, and request an agreed pause signal without guaranteeing sensations.',
    brief='Patient Ava tells assistant Ben she is anxious and asks him to promise that the planned procedure will not hurt. The dentist has not yet discussed comfort measures or her concerns. Ben can listen, relay the concern, and ask the dentist to explain the plan and an appropriate pause signal before proceeding. He cannot guarantee a painless experience, select medication, or invent a sedation arrangement. No specific treatment or anesthetic plan is supplied. The conversation should help Ava ask questions and understand how concerns will be addressed within the actual care process.',
    cast='Ava | Patient\nBen | Dental assistant',
    culture=('Reassurance should be honest and specific', 'Phrases such as you will not feel a thing can sound kind but promise more than the speaker knows. Acknowledge the concern without minimizing it. Explain the next conversation and let the clinician discuss likely sensations, options, and the way to request a pause.'),
    a='''What does Ava ask Ben to promise? | That the procedure will not hurt | That the laboratory will deliver early | That the visit will be free | That a particular sedative is prescribed | The stated request is a guarantee about pain, not a confirmed comfort plan.
What has not happened yet? | The dentist's discussion of comfort measures and Ava's concerns | Any expression of anxiety | Ava's arrival | Ben hearing the request | The brief says the clinical comfort discussion has not yet taken place.
What can Ben appropriately arrange? | Communication of the concern and a dentist explanation of the plan and pause signal | His own sedation prescription | A guarantee of no sensation | An instruction to remain silent during discomfort | Ben can support the clinical conversation without inventing medication, sensations, or a treatment plan.''',
    vocabulary='''dental anxiety | Apprehension or fear related to dental care. | acknowledge dental anxiety
distress | Significant discomfort or emotional upset. | notice reported distress
comfort measure | An appropriate action intended to support comfort during care. | discuss comfort measures
pain concern | A question or fear about pain that needs to be heard and addressed. | relay a pain concern
sensation | Something physically felt, such as pressure or discomfort. | describe a reported sensation
pressure | A physical sensation whose expected meaning requires the relevant clinical explanation. | clarify expected pressure
numbness | Reduced or absent sensation in a particular area. | report numbness accurately
local anesthesia | A clinical method of reducing sensation in a defined area. | discuss local anesthesia
topical anesthetic | An anesthetic applied to a surface for an appropriate clinical purpose. | clarify a topical anesthetic question
sedation | Medication-related reduction of awareness or anxiety at a defined level under clinical supervision. | discuss sedation options
analgesia | Relief of pain through the appropriate method or treatment. | clarify an analgesia question
contraindication | A reason a treatment may be inappropriate in a particular situation. | refer a contraindication question
medical history | Relevant past and current health information. | update the medical history
previous experience | An earlier event affecting expectations or concerns. | acknowledge a previous experience
trigger | Something associated with an anxiety or distress response. | ask about a reported trigger
pause signal | An agreed way to request a pause during care. | agree a pause signal
ongoing consent | Consent addressed throughout the care process, not only at its beginning. | check ongoing consent
stop request | A request that the activity be stopped through the appropriate safe response. | acknowledge a stop request
explanation before action | Information given before the relevant step occurs. | request explanation before action
communication preference | The person's preferred way of receiving or giving information. | clarify a communication preference
reassurance | Information or support intended to reduce concern without misleading. | give honest reassurance
absolute guarantee | A promise with no stated uncertainty or exceptions. | avoid an unsupported absolute guarantee
clinician review | Assessment or explanation by the responsible qualified clinician. | request clinician review
shared understanding | Agreement about what has been explained and understood. | establish shared understanding''',
    precision='Pain, pressure, numbness, and anxiety are different words, but the assistant must not use that distinction to dismiss a patient report. The clinician should explain the actual comfort plan and expected sensations; the patient should not be promised an unqualified outcome.',
    precision_extra='Agreeing a pause signal is a communication step, not a universal gesture prescribed by this book. The clinician should confirm how to signal, how the team will respond safely, and how ongoing questions and consent will be addressed in the actual procedure.',
    phrases='''Acknowledge anxiety | Thank you for telling me that you are worried.
Invite the specific concern | What would you like the dentist to know before starting?
Avoid a guarantee | I cannot promise that you will feel nothing.
Offer a useful next step | I will ask the dentist to discuss the comfort plan with you.
Preserve the wording | I will tell the dentist you are worried about pain.
Request explanation | Please explain the likely sensations and available comfort measures.
Ask about a signal | Can we agree an appropriate way to request a pause?
Confirm the response | How will the team respond if you use that signal?
Respect a concern | Please tell us if something does not feel as explained.
Avoid minimization | I will not dismiss your concern as just nerves.
Clarify preference | Would you prefer an explanation before each stage?
Keep clinical choices with the clinician | The dentist needs to discuss any medication or sedation question.
Separate reassurance and certainty | I can help communicate your concern without promising an outcome.
Support questions | You can ask for clarification before deciding whether to continue.
Record accurately | I will record your concern and the explanation actually provided.
Close the loop | We need to confirm the plan and signal with you, not assume they are understood.''',
    notes='''Thank you for telling me | Makes reporting discomfort or anxiety welcome.
Cannot promise | Avoids certainty that the assistant cannot support.
Before starting | Places the discussion before the relevant action.
How will the team respond | Checks that a signal has an understood practical response.
As explained | Encourages reporting a difference without diagnosing it.
Actually provided | Keeps a pending explanation separate from a completed conversation.''',
    d='''Which reassurance is appropriate? | I will help you discuss pain concerns and the comfort plan with the dentist before starting. | You will definitely feel nothing. | Anxiety means your concern is not real. | I will choose a sedative for you. | The response offers concrete support without a false sensation guarantee or unauthorized clinical decision.
Which statement wrongly treats consent as permanent? | You agreed once, so you cannot ask to stop. | The clinician should discuss ongoing questions. | The pause signal needs explanation. | A changed concern should be communicated. | An earlier agreement does not remove the need to address ongoing consent and a stop request.
What should be confirmed about a pause signal? | The actual signal and how the team will respond safely | A universal gesture invented by the assistant | That the patient must never use it | That it replaces all clinical discussion | A useful signal requires shared understanding of both the request and the team's response.
What should the record distinguish? | Reported concern, explanation given, and any agreement actually reached | A hoped-for painless outcome as a guaranteed fact | A requested sedative as an administered drug | Silence as proof that every question was answered | Accurate recording separates concerns, communication, and actual decisions rather than assuming an outcome.''',
    dialogue='''Ava | Ben, I barely slept. Last time I felt something sharp and could not get anyone's attention. Can you promise this will not hurt?
Ben | Thank you for telling me about your [[dental anxiety::Dental anxiety identifies the patient's apprehension and should be acknowledged rather than dismissed or treated as a diagnosis of the tooth.]]. I cannot promise a painless experience, but I can make sure the dentist discusses your concern and the comfort plan before starting.
Ava | People say not to worry, but that makes me feel I should stay quiet if something bothers me.
Ben | I do not want [[reassurance::Reassurance should provide honest support and information, not pressure the patient to suppress a concern.]] to silence you. Your concern needs a clear response, not a phrase that makes you feel responsible for hiding discomfort.
Ava | Last time I did not know whether I was supposed to feel pressure or pain. I could not tell what the person expected me to report.
Ben | We can ask about the expected [[sensation::Sensation refers to what the patient may feel; the actual clinician must explain it in relation to the planned procedure.]] in this procedure. I should not tell you which feeling is acceptable without the clinician's explanation or use the word pressure to dismiss what you report.
Ava | I would like to know what can be done to help me feel comfortable. I do not know which choices are appropriate for me.
Ben | That needs discussion of the actual [[comfort measure::A comfort measure must be appropriate to the patient's circumstances and explained by the responsible clinical team.]] or measures with the dentist. I will not invent a medication plan, but I will make sure the question is included.
Ava | Someone mentioned sedation to me, although I do not know whether they meant the same thing as having part of the mouth numb.
Ben | [[Sedation::Sedation and local anesthesia are different clinical concepts; neither is confirmed or selected in this scenario.]] and local anesthesia are different terms. The dentist can explain their meanings and relevance to you; neither should be assumed simply because a patient has heard the word.
Ava | Please tell them about my previous experience too. I was not sure how to ask for a break once the person had started working.
Ben | We should ask the dentist to agree an appropriate [[pause signal::A pause signal is an agreed communication method whose meaning and safe response must be confirmed for the actual care.]] with you before proceeding. The signal and the team's response need to be understood, rather than left for you to guess.
Ava | I would also like an explanation before each stage. Surprises make me tense, even when the action itself might not be difficult.
Ben | I can pass on that [[communication preference::The communication preference is the patient's request for explanation before each stage, not a demand for a particular clinical treatment.]]. The team can discuss how to explain the sequence clearly and check what information helps you feel prepared.
Ava | If I agree to continue after the explanation and then change my mind, I want to know that I can still say something.
Ben | The clinician should address [[ongoing consent::Ongoing consent requires attention throughout care; an earlier yes does not erase later questions or a request to stop.]] and respond to questions or a request to stop through the appropriate safe process. An earlier yes does not mean your later concern should be ignored.
Ava | That is more useful than a promise that nothing will hurt. I want an honest explanation and a way to communicate, not certainty nobody can give.
Ben | An unsupported [[absolute guarantee::An absolute guarantee about pain would claim certainty the assistant does not have and could undermine honest communication.]] would not help you make an informed choice. I can support a specific conversation about your concern, the plan, and how to ask for attention during care.
Ava | Could we discuss this before anything starts? I would feel less trapped with an agreed pause signal.
Ben | I will request that [[clinician review::Clinician review supplies the qualified discussion of the actual plan; the assistant's acknowledgment alone does not complete it.]] before we treat those questions as resolved. I will record what you asked and what is actually explained and agreed, not an assumed painless outcome.''',
    rehearsal=('Read Ava and Ben aloud; make the request for a pause signal easy to hear.', 'Complete and read the transfer using its supplied concern, without dismissing pain as expected pressure.', 'Check the key, then repeat the request for the actual clinician explanation before treating the concern as resolved.'),
    transfer_title='Communicate a concern about unexpected sensations',
    transfer_setup='A patient requests explanation before each stage and asks how to request a pause. The clinician has not yet confirmed a signal. The assistant cannot guarantee particular sensations.',
    transfer='''Assistant: "The requested communication preference is explanation before ___." | each stage | The patient specifically asks for explanations before each stage of care.
Patient: "I would like to agree a ___." | pause signal | The request concerns how to communicate a need for a pause.
Assistant: "The signal is not yet ___." | confirmed | The clinician has not yet agreed the signal or its response.
Assistant: "I cannot provide an absolute ___ about sensations." | guarantee | The supplied role does not support an unqualified promise about what the patient will feel.''',
))

BOOK['units'].append(unit(
    title='Records, identifiers, and factual handoffs',
    scene='A shared surname is not a verified match',
    skill='Report an identifier mismatch before using a record and hand off the facts without guessing which source is correct.',
    brief='Assistant Diego is preparing a folder for a patient named Morgan. Two patients share that surname. The appointment list shows identifier ending 462, while the folder label shows 426. Diego has not used the folder or disclosed its contents. Lead assistant Priya can check the records through the approved identification process. Neither number is established as correct by this teaching brief. Diego must report the mismatch, preserve confidentiality, and avoid silently changing a label, merging records, or deciding that two similar numbers are merely a harmless typing error.',
    cast='Diego | Dental assistant\nPriya | Lead assistant',
    culture=('Speak up before a near match becomes a match', 'A familiar surname and nearly identical digits can feel convincing during a busy clinic. State the exact mismatch without blaming the patient or a colleague. A neutral verification request is more useful than choosing whichever record looks most familiar.'),
    a='''Which mismatch is supplied? | The list ends 462 and the folder label ends 426. | Both verified identifiers are identical. | The surname is absent from both records. | The appointment is confirmed for a different day. | The two supplied identifier endings differ despite the shared surname.
Which record is established as correct? | Neither | The folder automatically | The list automatically | Whichever was printed most recently without verification | The brief does not establish the correct source, so the approved process must resolve the mismatch.
What has Diego not done? | Used the folder or disclosed its contents | Noticed the discrepancy | Identified the shared surname | Contacted a route for clarification in the scenario | The brief says the folder has not been used and its contents have not been disclosed.''',
    vocabulary='''patient identifier | Information used to distinguish a particular patient under the approved process. | verify patient identifiers
demographic detail | Recorded information such as name or date of birth. | verify demographic details
record number | An identifier assigned to a particular record. | confirm the record number
identifier mismatch | A disagreement between relevant identifying information. | report an identifier mismatch
name collision | Different people sharing the same or similar name in a system. | recognize a name collision
duplicate record | More than one record for the same person, requiring proper verification before consolidation. | investigate a possible duplicate record
wrong-patient risk | The possibility of using information or providing care for the wrong person. | address wrong-patient risk
chart | A patient's clinical record. | verify the chart
folder label | The identifying information shown on a physical folder. | check the folder label
appointment list | The schedule of booked patients and visits. | reconcile the appointment list
medical-history form | A record of relevant health information supplied and reviewed under the care process. | verify the medical-history form
odontogram | A diagrammatic dental chart of teeth and relevant recorded findings or treatment. | identify the odontogram
tooth notation | A system for identifying teeth in records. | confirm the tooth notation system
laterality | The specified side of the body or structure. | verify laterality
dentition | The arrangement or set of teeth present. | distinguish dentition references
chart entry | An item recorded in the patient chart. | make an accurate chart entry
source record | The original record used for verification or reference. | preserve the source record
reconciliation | Comparing records and resolving relevant differences through an approved process. | complete record reconciliation
traceable correction | An amendment that preserves who changed what and when. | make a traceable correction
audit trail | A history of recorded actions or changes. | preserve the audit trail
access control | Restriction of information access to authorized users and purposes. | follow access controls
confidential handoff | Transfer of relevant information through an appropriately protected route. | give a confidential handoff
unverified match | A possible link between person and record not yet confirmed. | flag an unverified match
record merge | Combining records after the required verification and authorization. | authorize a record merge''',
    precision='A shared surname does not establish that two records concern the same patient. Similar digits do not prove a typing error, either. Preserve both values and use the full approved identification process; these three-digit endings are teaching references, not sufficient real-world identifiers.',
    precision_extra='Do not silently relabel or merge records to make the screen look consistent. Corrections require the appropriate verified basis and traceable process. A factual handoff can describe the mismatch and nonuse without claiming the investigation is already complete.',
    phrases='''State the discrepancy | The list and folder show different identifier endings.
Read the values clearly | The list ends four-six-two; the label ends four-two-six.
Name the shared name | Two patients in the records share this surname.
Avoid choosing a winner | I cannot yet establish which record is correct.
State the current action | I have not used this folder.
Protect information | I have not disclosed its contents.
Request verification | Please check the match through the approved identification process.
Avoid a casual correction | I will not change the label just to make it match.
Keep sources separate | Let us preserve what each source currently shows.
Do not assume duplication | A shared surname does not prove duplicate records.
Clarify a record change | Any correction needs the proper verified basis and audit trail.
Protect the handoff | I will discuss the details through the approved confidential route.
Separate identification and treatment | A record match does not itself confirm the treatment plan.
Check notation | Which tooth notation system is used in this record?
Report the outcome accurately | I will record the actual verification result, not the expected result.
Close only when resolved | The match remains unverified until the required checks are complete.''',
    notes='''Different endings | Describes the observed mismatch without disclosing more information than necessary.
Four-six-two | Reading digits individually can make a transposition easier to detect.
Cannot yet establish | Avoids choosing a source without evidence.
Have not used | Identifies the stage at which the issue was caught.
Verified basis | Requires evidence before altering records.
Actual result | Keeps investigation status separate from a hoped-for correction.''',
    d='''Which report is precise? | The list ends 462, the folder ends 426, and I have not used the folder. | The folder is definitely wrong because the list is on screen. | Both records must belong to one person. | I corrected the label without checking so it looks consistent. | The precise report preserves the values and action status without assigning unsupported correctness.
Why not merge the records immediately? | A shared surname does not establish that they concern the same person. | Every name collision is a duplicate record. | Similar digits are proof of identity. | Record merges never require verification. | Different people can share a surname, so consolidation without verification could combine their information incorrectly.
What should a legitimate correction preserve? | The verified basis and appropriate traceable history | Only the new value with no history | An invented earlier verification | Another patient's details as a shortcut | A traceable correction records the supported change rather than concealing how the discrepancy was resolved.
What are the three-digit endings in this exercise? | Teaching references, not a complete real-world identification method | A universal minimum identification standard | Proof of clinical consent | Authorization to disclose the folder | The exercise uses shortened references for language practice and does not replace an approved full identification process.''',
    dialogue='''Diego | Priya, I have an identifier mismatch before using this folder. The appointment list ends four-six-two, but the folder label ends four-two-six.
Priya | Keep the [[source record::The source record preserves the original information needed to investigate the mismatch rather than replacing it with a guess.]] unchanged while we check. Does the surname identify only one patient in our records, or is there another person with the same name?
Diego | There are two patients named Morgan. I have not used the folder or disclosed its contents, and I cannot establish which identifier belongs with this visit.
Priya | That is a [[name collision::A name collision means more than one person shares a name; it does not prove the records should be combined.]], not proof that the records are duplicates. We need the approved identification process before choosing a chart or changing information.
Diego | Four-six-two and four-two-six look like swapped digits. I nearly trusted the screen over the folder, but I have no evidence that the screen is right.
Priya | An [[identifier mismatch::An identifier mismatch establishes disagreement between sources, not which source is correct or why the difference occurred.]] does not tell us which source is right. A plausible explanation still needs verification; the screen does not become authoritative merely because it is easier to read.
Diego | I will preserve the two values and the fact that the folder has not been used. That seems more helpful than deciding the cause in advance.
Priya | Yes. We should address the [[wrong-patient risk::Wrong-patient risk arises when an unverified record could be used for the wrong person; raising the mismatch before use supports prevention.]] through the actual process, while keeping the description factual. We have identified a discrepancy before use, not established that treatment was given to the wrong person.
Diego | Should I ask the person a leading question with one of the numbers, or follow the usual identification questions without suggesting the answer?
Priya | Follow our approved [[patient identifier::Patient identifiers must be verified through the actual approved process, not by treating a prompted guess as reliable confirmation.]] checks. These partial numbers alone are not enough, and we should not improvise a shortcut that makes an uncertain match appear confirmed.
Diego | The folder also contains a dental chart, but I have not used its contents to guess whether it looks like the patient I remember.
Priya | Correct. An [[odontogram::An odontogram records dental information and must not become an informal substitute for the required patient-identification checks.]] or a remembered treatment history should not replace the required identity checks. The relevant clinical record must first be linked to the correct person through the process.
Diego | If the review shows that one label is wrong, I should not remove the old information without recording how and why it was changed.
Priya | A [[traceable correction::A traceable correction preserves the verified basis and history of a change rather than silently overwriting the discrepancy.]] is needed under the record procedure. The result must show the supported amendment, not pretend that the original discrepancy never existed.
Diego | And if the review reveals two records for one person, that would still be a separate authorized process rather than something I do because the surname matches.
Priya | Exactly. A [[record merge::A record merge combines information and therefore requires verified identity and the appropriate authority, not a shared surname alone.]] needs the proper verification and authority. Joining records prematurely could mix information from different patients and make the problem harder to correct.
Diego | Can we check the details in the staff area? Both patients' names are visible here, and I do not want this conversation carrying into the waiting room.
Priya | That keeps this a [[confidential handoff::A confidential handoff shares the relevant information through an appropriately protected route instead of exposing it to unrelated people.]]. We need enough information to resolve the issue, without exposing either patient's details to people who do not need them.
Diego | Until the check is complete, my update will say that the match is unverified, the folder has not been used, and you are coordinating the review.
Priya | Good. The [[audit trail::The audit trail records relevant actions and changes so the actual review and correction history can be understood later.]] should preserve the discrepancy, review, and actual resolution. We will close the issue on verified information rather than a near match that feels convincing.''',
    rehearsal=('Read the two endings four-six-two and four-two-six distinctly, then read the confidential handoff.', 'Complete the transfer with its different identifiers; do not choose a record simply because one value looks familiar.', 'Check the four answers, then repeat the distinction between a mismatch, an authorized correction, and a record merge.'),
    transfer_title='Report a second identifier mismatch',
    transfer_setup='A schedule reference ends 815 and a folder reference ends 851. Two patients share a surname. The folder has not been used, and neither value is established as correct.',
    transfer='''Assistant: "The schedule reference ends ___." | 815 | The supplied schedule value is 815, distinct from the folder value.
Lead: "The folder reference ends ___." | 851 | The supplied folder value is 851 and must not be silently changed.
Assistant: "The folder has ___." | not been used | The brief places the discrepancy before any use of the folder.
Lead: "The match remains ___." | unverified | Neither source is established as correct, so the identification process remains necessary.''',
))

BOOK['units'].append(unit(
    title='Laboratory cases and delivery expectations',
    scene='Expected by noon is not ready for two',
    skill='Distinguish estimated delivery from clinical readiness and agree a useful laboratory update before confirming the patient plan.',
    brief='Laboratory coordinator Felix estimates that case C62 will reach the practice on Tuesday by noon. The patient appointment is at 14:00 that day. Delivery is not guaranteed, and the dentist must confirm readiness before the appointment proceeds. Assistant Rina can obtain a laboratory status update on Monday at 16:00. She needs to separate production status, dispatch, receipt, and clinical readiness. The two-hour interval between estimated delivery and the appointment is not a guarantee of sufficient review time. No final decision to proceed or reschedule has been supplied.',
    cast='Rina | Dental assistant\nFelix | Laboratory coordinator',
    culture=('An estimate is useful when its limits travel with it', 'Teams may shorten an expected delivery into it will be ready. Preserve the source, time, and conditions when passing information to the practice. A precise update request helps the patient plan without turning laboratory progress into a clinical promise.'),
    a='''What is the laboratory estimate? | Tuesday by noon, not guaranteed | Monday at 16:00 delivery guaranteed | Tuesday at 14:00 treatment confirmed | A completed clinical fit review | The lab estimates arrival by Tuesday noon and explicitly does not guarantee it.
When can the lab provide the next status update? | Monday at 16:00 | Tuesday at 14:00 only | After the procedure is complete | A guaranteed arrival time of 16:00 | Monday 16:00 is the update time, not the estimated delivery time.
What else is required before proceeding? | Dentist confirmation of readiness | Only the existence of tracking | Automatic consent from the courier | A two-hour gap alone | The scenario separately requires the dentist to confirm readiness after the relevant checks.''',
    vocabulary='''laboratory case | A defined item of work handled by a dental laboratory. | track the laboratory case
case reference | The identifier used to distinguish a particular lab case. | verify the case reference
laboratory prescription | Authorized clinical instructions for the laboratory work. | verify the laboratory prescription
work authorization | Approval for the specified laboratory task. | confirm work authorization
impression | A negative reproduction used for making a model of oral structures. | identify the submitted impression
digital scan | A digital representation used within the relevant laboratory workflow. | verify the submitted digital scan
working model | A model used in producing the specified dental work. | identify the working model
shade | The specified color characteristics of a restoration or appliance. | confirm the shade reference
crown | A restoration covering the relevant tooth structure as clinically prescribed. | track a crown case
bridge | A restoration replacing missing teeth and supported as clinically designed. | identify the bridge case
denture | A prosthesis replacing missing teeth and related structures as prescribed. | identify the denture case
appliance | A device prescribed for a particular dental or orthodontic purpose. | verify the appliance type
try-in | A clinical stage for assessing specified work before final completion or placement. | arrange a try-in appointment
fit assessment | Clinical assessment of whether the item fits as required. | obtain a fit assessment
occlusal check | Clinical assessment relating to how opposing teeth or restorations meet. | refer the occlusal check
remake | Production of replacement work after an appropriate reviewed request. | authorize a remake
production status | The current stage of laboratory manufacture. | request production status
dispatch status | Whether the item has actually been sent. | confirm dispatch status
tracking event | A recorded carrier event, not necessarily final receipt. | interpret a tracking event
estimated delivery | A forecast of when the item may arrive. | qualify estimated delivery
receipt confirmation | Verification that the specified item has arrived at the destination. | obtain receipt confirmation
clinical readiness | Confirmation that the relevant clinical requirements for proceeding are met. | verify clinical readiness
contingency booking | An alternative appointment arrangement considered under the practice process. | discuss a contingency booking
status checkpoint | An agreed time for reviewing and communicating progress. | set a status checkpoint''',
    precision='Produced, dispatched, delivered, checked, and ready for the appointment are different statuses. A tracking event does not necessarily confirm receipt of the correct case, and receipt does not replace the clinical readiness decision by the dentist.',
    precision_extra='Tuesday noon to 14:00 is a two-hour interval, but no sufficient review duration is established here. Keep the appointment decision with the practice and clinician. Use the Monday update to improve the information, not to guarantee a result before it exists.',
    phrases='''Identify the case | I am checking case C62 for Tuesday's appointment.
Request the stage | What is the current production and dispatch status?
Repeat the estimate | You estimate arrival Tuesday by noon, without a guarantee.
Separate the checkpoint | Monday at sixteen hundred is the status update, not delivery.
Name the dependency | The dentist must confirm readiness before the appointment proceeds.
Avoid a timing assumption | The two-hour gap does not itself establish enough review time.
Verify the shipment | Please confirm the case reference associated with the tracking.
Distinguish dispatch and receipt | A dispatch message does not confirm arrival at the practice.
Ask about a change | Please tell us if the estimate or production status changes.
Avoid treatment promises | I cannot tell the patient the appointment is ready based only on the estimate.
Clarify a lab question | Any change to the clinical specification needs the proper authorization.
Keep the patient plan separate | The practice will decide the appointment response using the confirmed information.
Request a useful update | At the checkpoint, please distinguish finished, dispatched, and expected arrival.
Preserve uncertainty | We have an estimate, not receipt confirmation.
Confirm the handoff | I will pass the source and limits of the estimate to the dentist.
Close the status | C62 remains subject to delivery and the required readiness confirmation.''',
    notes='''Without a guarantee | Keeps the limitation attached to the forecast.
Before the appointment proceeds | States the separate clinical dependency.
Does not itself establish | Prevents a time calculation from becoming readiness evidence.
Associated with the tracking | Checks that a real carrier event concerns the intended case.
Proper authorization | Keeps clinical specifications out of an improvised administrative change.
Source and limits | Helps the estimate survive a handoff without becoming a promise.''',
    d='''Which patient update is accurate? | The lab estimates Tuesday noon delivery; the practice still needs receipt and dentist readiness confirmation. | Tuesday treatment is guaranteed because a shipment is expected. | Monday 16:00 is the confirmed delivery. | The courier will decide clinical suitability. | The accurate message separates estimated arrival from the practice's required readiness decision.
What is the interval from noon to 14:00? | Two hours, with no proof that this is sufficient review time | Four hours and automatic readiness | Two days | A guaranteed clinical clearance period | The arithmetic gives two hours, but the brief supplies no rule making that sufficient.
Which request is most useful at Monday's checkpoint? | Current production, actual dispatch, revised estimate, and any change affecting delivery | A repeat of an old promise regardless of current facts | A clinical diagnosis from the courier | A silent change to the laboratory prescription | The requested status gives the practice actionable facts without replacing clinical authority or current evidence.
What does a delivered status not establish by itself? | Clinical readiness to proceed | That a carrier recorded a delivery event | A need to verify receipt details | A reason to check the case reference | A delivery event concerns logistics and does not supply the dentist's separate readiness confirmation.''',
    dialogue='''Rina | Felix, I am checking case C62. The patient is booked for Tuesday at two, and I need to know exactly what your delivery estimate means.
Felix | The current [[estimated delivery::Estimated delivery is a forecast of Tuesday noon arrival, not a guaranteed appointment or confirmed receipt.]] is Tuesday by noon, but it is not guaranteed. Please keep that qualification attached when you pass the timing to the practice.
Rina | That leaves two hours on paper. I am worried reception will hear Tuesday noon and tell the patient the two-o'clock fitting is definitely going ahead.
Felix | Correct. The [[clinical readiness::Clinical readiness requires the dentist's relevant checks and decision; a forecast delivery time does not establish it.]] decision belongs with the dentist after the relevant checks. The laboratory estimate concerns arrival, not whether the appointment can definitely proceed.
Rina | What can you tell us at Monday's four-o'clock update? It would help to separate what is finished from what has actually left the laboratory.
Felix | We can report the [[production status::Production status identifies the manufacturing stage and must remain distinct from actual dispatch or delivery.]] and whether dispatch has occurred, along with the current delivery estimate. I will not call an item shipped simply because production is expected to finish.
Rina | If it has been sent, we also need the correct reference and tracking details. We sometimes receive more than one case in the same delivery.
Felix | We should verify the [[case reference::The case reference links the status and tracking to C62 rather than another case in the same delivery.]] against the shipment. Tracking information for another item would not answer your question about C62, even if the destination is the same.
Rina | If the carrier website shows movement, I should describe that movement rather than say we have received the case in the practice.
Felix | Yes. A [[tracking event::A tracking event records a carrier action and is not necessarily confirmation that the intended case was received by the practice.]] can show collection or transit without establishing receipt. Use the actual event and time instead of translating every update into arrived.
Rina | And when a package reaches us, the practice needs to confirm the right case was received and follow the relevant checks before calling it ready.
Felix | Exactly. [[Receipt confirmation::Receipt confirmation verifies arrival of the specified item; it remains separate from the clinical assessment needed before proceeding.]] and clinical readiness are separate. We should keep the sequence clear so a logistics message does not accidentally become a treatment promise.
Rina | If something changes in the clinical specification, I cannot simply amend it over this call to make the production schedule easier.
Felix | Any change to the [[laboratory prescription::The laboratory prescription contains authorized clinical instructions and cannot be altered casually to accommodate a schedule.]] needs the appropriate authorization and documentation. We can communicate a question, but the convenience of a delivery date does not decide clinical specifications.
Rina | The patient may need time to plan travel. I will ask the practice how to communicate the uncertainty and any alternative appointment arrangements.
Felix | A [[contingency booking::A contingency booking is an alternative appointment arrangement for the practice to consider, not an automatic cancellation or confirmed replacement.]] may be a practice decision, but I cannot make it from the laboratory. I can provide the clearest available facts and flag changes promptly.
Rina | Let me read those back: update Monday at four; estimated arrival Tuesday by noon. I will put them in separate fields so nobody confuses the dates.
Felix | That is the [[status checkpoint::The status checkpoint is the agreed Monday update time and must not be confused with the Tuesday delivery estimate.]]. At that time we will distinguish production, dispatch, and expected arrival. If information changes earlier, we will communicate the change through the agreed route.
Rina | I will tell the dentist that no final decision to proceed or reschedule is established by this conversation. The appointment still depends on actual receipt and readiness.
Felix | Agreed. Our [[dispatch status::Dispatch status records whether the case has actually been sent; it is one logistical fact, not final appointment approval.]] update will be factual and case-specific. C62 is expected Tuesday by noon, not guaranteed, and the dentist must make the relevant readiness decision.''',
    rehearsal=('Read the C62 call with Monday at four and Tuesday by noon clearly separated.', 'Use the Wednesday transfer facts below to practice a different checkpoint and delivery estimate.', 'Check each blank, then repeat the final status without turning estimated delivery into clinical readiness.'),
    transfer_title='Separate a Wednesday delivery estimate from an update',
    transfer_setup='Case D14 is estimated for Wednesday at 10:00, without a guarantee. The appointment is at 13:00. The lab will update Tuesday at 15:00, and the dentist must still confirm readiness.',
    transfer='''Assistant: "The case reference is ___." | D14 | D14 identifies the particular laboratory case in this exchange.
Lab: "Estimated arrival is ___." | Wednesday at 10:00 | The supplied estimate concerns Wednesday arrival and is explicitly not guaranteed.
Assistant: "The status update is due ___." | Tuesday at 15:00 | Tuesday 15:00 is the information checkpoint, not the delivery time.
Lab: "The dentist must confirm ___." | clinical readiness | Delivery timing alone does not establish readiness for the appointment.''',
))

BOOK['units'].append(unit(
    title='Aftercare questions and follow-up calls',
    scene='An unclear instruction needs an exact clinical answer',
    skill='Capture a postoperative question accurately, route it to the clinician, and distinguish routine clarification from urgent concerns.',
    brief='Patient Owen calls assistant Farah because a phrase in his written postoperative instructions is unclear. He quotes "resume your usual routine as directed" and asks what that means for him. Farah is not authorized to reinterpret or change the instructions. The clinician can answer through the practice callback process, but no callback time or clinical answer is yet confirmed. Farah should preserve the exact wording and question, verify the contact through the approved process, and route it appropriately. An urgent or emergency concern must use the designated route rather than an ordinary queue.',
    cast='Owen | Patient\nFarah | Dental assistant',
    culture=('Clarification is not a nuisance', 'Patients may feel embarrassed to call about a phrase that seems simple to staff. Thank the caller for checking. Use exact wording and an accurate handoff so the clinician answers the real question rather than a summary that silently changes the instruction.'),
    a='''What does Owen need? | Clarification of a phrase in his actual postoperative instructions | A new prescription invented by Farah | Confirmation that every symptom is normal | A laboratory dispatch update | The caller asks what a particular written phrase means in his circumstances.
What is outside Farah's supplied role? | Reinterpreting or changing the instructions | Recording the exact question | Using the approved callback process | Explaining that timing is not confirmed | The brief explicitly excludes independent reinterpretation and alteration of clinical instructions.
What overrides an ordinary callback queue? | The appropriate route for an urgent or emergency concern | A wish to keep every call short | The existence of a printed sheet alone | An unconfirmed assumption that all callers are stable | Urgent concerns require their designated response rather than delay for routine clarification.''',
    vocabulary='''postoperative | Relating to the period after an operation or procedure. | clarify postoperative instructions
aftercare | Care and instructions relevant after treatment. | discuss an aftercare question
discharge instructions | The information given for care and follow-up after leaving the service. | verify discharge instructions
written direction | An instruction recorded in text whose actual wording matters. | quote the written direction
clinical clarification | An explanation from the appropriate clinician about the intended instruction. | request clinical clarification
verbatim | Using the actual words rather than a changed summary. | record the question verbatim
patient-reported concern | An issue described by the patient and attributed to them. | document a patient-reported concern
callback request | A request for a return call, not confirmation that the call occurred. | log a callback request
contact verification | Checking relevant contact details through the approved process. | complete contact verification
telephone note | A factual record of the call and actions taken. | complete a telephone note
triage route | The designated process for assessing and directing the concern. | use the triage route
urgent concern | A concern requiring timely action under the applicable clinical process. | escalate an urgent concern
emergency response | The immediate appropriate response to an emergency under local arrangements. | use the emergency response
safety-net advice | Clinician-approved information on what to do if symptoms change or concerns arise. | clarify safety-net advice
review interval | The specified period before reassessment or follow-up. | confirm the review interval
follow-up appointment | A later visit arranged for a stated clinical purpose. | verify the follow-up appointment
extraction site | The area where a tooth has been removed. | identify an extraction-site question
suture | Material used to hold tissues together as part of a clinical procedure. | clarify a suture question
swelling | Enlargement of tissue whose meaning depends on clinical context. | report swelling accurately
bleeding | Loss of blood whose severity and context require appropriate assessment. | report bleeding without minimizing it
infection concern | A reported worry about possible infection, not itself a diagnosis. | route an infection concern
dry socket | A painful post-extraction complication requiring dental assessment; not a label for any discomfort. | refer a dry-socket question
instruction amendment | An authorized change to the actual clinical directions. | document an instruction amendment
unresolved question | A question for which an appropriate answer has not yet been provided. | track an unresolved question''',
    precision='A familiar phrase can still have a patient-specific meaning. Do not silently replace as directed with an invented timetable or permission. Preserve the wording and have the clinician explain the intended direction and any relevant conditions.',
    precision_extra='A callback request is not a completed answer. Record actual contact, instructions, and follow-up accurately. If the caller describes an urgent or emergency concern, use the appropriate local route promptly; the absence of such details in a language exercise is not a clinical clearance.',
    phrases='''Welcome the question | Thank you for calling to check the instruction.
Ask for exact wording | Could you read the phrase exactly as it appears?
Preserve the source | I will record that as wording from your instruction sheet.
Clarify the question | What part would you like the clinician to explain?
State the limit | I am not authorized to reinterpret or change that direction.
Offer the route | I can pass the exact question to the clinician through our callback process.
Avoid invented timing | I do not yet have a confirmed callback time.
Verify contact properly | Let us confirm the contact details through our usual process.
Keep urgency separate | An urgent concern needs the designated route, not the ordinary queue.
Avoid a diagnosis | I cannot identify the cause of a symptom from an unassessed description.
Record an attributed report | I will record what you tell me as your report.
Do not replace the instruction | I will not substitute my own timetable for the clinician's direction.
Check the response | Please ask for clarification if the clinician's answer remains unclear.
Confirm any amendment | A changed instruction needs the authorized clinical response.
Track the open question | The question remains unresolved until the appropriate answer is provided.
Close accurately | I have logged the request; I have not given a new clinical instruction.''',
    notes='''Exactly as it appears | Preserves the wording that needs explanation.
What part | Identifies the actual uncertainty without guessing the intended question.
Not authorized to reinterpret | Separates communication support from clinical alteration.
Do not yet have | Avoids an unsupported promise of a specific response time.
Your report | Attributes symptoms or events to the caller rather than claiming direct observation.
Logged versus answered | Keeps the administrative action distinct from clinical resolution.''',
    d='''Which response is appropriate? | Please quote the phrase; I will route the exact question for clinical clarification without changing it. | As directed always means immediately. | Any written instruction can be replaced by my personal advice. | Calling proves no urgent concern exists. | The response preserves the question and routes it within the assistant's role.
What should Farah say about callback timing? | No time is confirmed yet. | The clinician will call in five minutes without confirmation. | The answer has already been given because the request was logged. | Every callback may safely wait indefinitely. | The brief supplies no confirmed callback time, so neither a specific promise nor an indefinite safety claim is justified.
What should happen if the caller reports an urgent concern? | Use the designated urgent or emergency route as appropriate. | Leave it in the ordinary queue regardless. | Diagnose it from a single word. | Tell the caller that all postoperative symptoms are normal. | The appropriate urgent route takes precedence over routine clarification and avoids unsupported reassurance.
Which note preserves the distinction? | Exact phrase and question logged; clinician response pending | New clinical advice supplied by Farah when none was authorized | Concern resolved because a form was completed | Original instruction silently replaced | A factual note separates the request, action, and pending response without inventing clinical resolution.''',
    dialogue='''Owen | Farah, I am home with the instruction sheet, but one sentence has me stuck. Could someone explain it before I guess what I am supposed to do?
Farah | Thank you for checking the [[written direction::The written direction is the actual text needing explanation, so its wording should be preserved rather than guessed.]]. Could you read the phrase exactly as it appears, then tell me which part you want the clinician to explain?
Owen | It says, resume your usual routine as directed. I do not know what as directed refers to or whether another part of the sheet explains it.
Farah | I will record that [[verbatim::Verbatim recording preserves the actual phrase so the clinician can answer the real wording instead of a changed summary.]], along with your question. I am not authorized to reinterpret or change the instruction, so I should not supply a timetable that the clinician has not confirmed.
Owen | I am glad you said that. I do not need a general answer copied from someone else's visit; I need to know what the direction means for mine.
Farah | That requires [[clinical clarification::Clinical clarification provides the appropriate patient-specific explanation of the instruction rather than an assistant's improvised interpretation.]]. I can pass the exact wording and your question through the practice callback process, using the relevant verified record and contact details.
Owen | Will the dentist actually see that wording? Last time I was told a message had been logged, but I still did not know what to do.
Farah | A [[callback request::A callback request records the need for contact but does not establish that the clinician has called or answered.]] is not an answer. I will keep the response pending until the actual clinical communication is recorded, rather than treat the administrative entry as resolution.
Owen | When should I expect the call? Please tell me if the time is not confirmed.
Farah | I do not have a confirmed time. We should complete [[contact verification::Contact verification checks the appropriate details through the approved process so the response is routed correctly without assumptions.]] through our process and use the designated route for an update on timing, rather than promise five minutes without confirmation.
Owen | If I report a new problem as well as the wording question, should that go into the same ordinary queue automatically?
Farah | No. An [[urgent concern::An urgent concern requires its appropriate timely response and must not be downgraded merely because the call began as a wording question.]] must use the designated route, including emergency response when appropriate. A call that begins with a routine question can still need a different response.
Owen | I understand. I do not want anyone to assume that every symptom after treatment is normal, or to guess a diagnosis from one word.
Farah | I will preserve any [[patient-reported concern::A patient-reported concern is attributed to the caller and routed for assessment rather than labeled normal or diagnosed without support.]] accurately and follow the practice process. I should not reassure you that a described symptom is harmless without the appropriate clinical assessment.
Owen | When the clinician responds, I want to be able to repeat what I understood and ask again if the explanation is still unclear.
Farah | That can help clarify the [[aftercare::Aftercare concerns the actual post-treatment directions and follow-up, which should be understood rather than merely delivered.]] discussion. Ask about anything unclear in the actual response rather than rely on a guess simply because the original phrase sounded familiar.
Owen | And if the clinician changes the direction, I would like the new wording clear. I do not want two different instructions without knowing which applies.
Farah | Any [[instruction amendment::An instruction amendment is an authorized change to the directions and must be communicated and recorded clearly through the required process.]] needs to be communicated and recorded through the proper process. I will not create a competing instruction myself or silently replace the original text.
Owen | Please record the phrase and my question about its meaning. You have not given me a new clinical direction.
Farah | Correct. My [[telephone note::The telephone note records the actual phrase, question, contact action, and pending response without claiming a clinical answer has been given.]] will preserve the question, the action taken, and the pending response. We will use the appropriate route for any urgent concern rather than let the callback process delay it.''',
    rehearsal=('Read the exact aftercare wording before reading the request for clarification.', 'Complete the transfer using review as arranged and the missing appointment date, not an invented interval.', 'Check the key, then repeat the pending-response status and the distinction between a routine callback and an urgent concern.'),
    transfer_title='Route an unclear follow-up interval',
    transfer_setup='A patient asks what review as arranged means on the instruction sheet. No appointment date is confirmed in the available record. The assistant cannot invent an interval; the clinician and scheduling team must clarify through the approved process.',
    transfer='''Assistant: "The quoted phrase is ___." | review as arranged | The exact phrase identifies the instruction that needs clarification.
Patient: "The missing information is the confirmed ___." | appointment date | No appointment date is confirmed in the available record.
Assistant: "I cannot invent a review ___." | interval | The assistant lacks authority to create a clinical follow-up timetable.
Assistant: "The question is still ___." | unresolved | Routing the question does not establish that an appropriate answer has already been provided.''',
))
