"""Original Medical Assisting learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='medical-assistants',
    title='Medical Assisting English',
    cover_label='ENGLISH FOR PATIENT-FACING CLINIC TEAMS',
    cover_title='Medical\nAssisting',
    cover_size=40,
    tagline='Listen carefully. Clarify the details.',
    audience='For medical assistants and outpatient clinic staff supporting patients, clinicians, and care coordination.',
    map_intro='Eight clinic cases: visit expectations, patient reports, medication lists, specimen records, referrals, instruction questions, clinical calls, and appointment corrections.',
    notes_title='Accurate details. Respectful conversations.',
    notes_intro='Medical assistants move between patient language, clinical terminology, and administrative systems. Clear communication preserves what the patient said, distinguishes a recorded event from a judgment, and makes the next responsible person visible.',
    field_notes=[
        ('Attribute a report', 'Keep the source attached to information. A patient report, an observation, a measurement, and a clinician assessment have different meanings. Do not turn one into another to make a note sound more authoritative.', '"Pat reports tiredness since Monday; I have not assessed its cause."'),
        ('Name the unresolved detail', 'A useful clarification states exactly what differs. Read the appointment type, medicine-list entry, event time, or message back before proposing a correction. A discrepancy does not prove which source is wrong.', '"The local list still includes it; the patient reports an outside instruction."'),
        ('Give a concrete route', 'A role boundary should lead to the right person or process. Preserve the question and explain the immediate next step. Do not leave a clinical concern waiting for a routine administrative update.', '"Nurse Dana is available through our clinical-call route now."'),
        ('Separate progress from completion', 'Received does not mean booked, and an attempted call does not mean the patient received the correction. Name the actual stage, unfinished work, and owner so a colleague can continue accurately.', '"The referral is under review; Friday is a status check, not an appointment."'),
    ],
    scope_note='All patients, records, times, and cases are fictional. This book teaches workplace English, not clinical assessment, triage, prescribing, specimen procedures, legal advice, or professional certification. Duties depend on local law, training, delegation, supervision, and clinic policy. Follow actual clinical and emergency procedures; these dialogues do not establish that any symptom can safely wait. US sources provide context, not universal rules. Use actual dates and required identifiers in real records.',
    sources=[
        dict(title='American Association of Medical Assistants. State Scope of Practice Laws.',
             url='https://www.aama-ntl.org/publications/state-scope-of-practice-laws',
             note='US context for jurisdiction-dependent duties and delegation. The fictional roles in this book do not authorize clinical work.', checked='10 October 2026'),
        dict(title='AHRQ. Use the Teach-Back Method: Tool 5.',
             url='https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html',
             note='Communication context for checking an explanation without shaming the patient. Clinical instruction questions remain with the appropriately authorized professional.', checked='10 October 2026'),
        dict(title='AHRQ. Make Referrals Easy: Tool 21.',
             url='https://www.ahrq.gov/health-literacy/improve/precautions/tool21.html',
             note='Background on referral coordination, clear instructions, and follow-up. Original referral cases separate receipt, review, booking, and completed attendance.', checked='10 October 2026'),
        dict(title='CDC. Collect Adult Blood Culture Sets.',
             url='https://www.cdc.gov/lab-quality/php/preventing-adult-blood-culture-contamination/collect.html',
             note='A specific laboratory example distinguishing collection documentation and specimen receipt. The book does not teach blood collection or universal specimen handling.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Clarifying the visit at check-in',
    scene='The schedule and the expectation',
    skill='Clarify a mismatch between a scheduled visit and a patient concern while respecting the preferred name.',
    brief='The schedule lists an annual review for patient Alexandra, whose verified record has already been matched through the clinic process. The patient prefers Alex and expected to discuss a recent concern. Assistant Sam cannot decide whether the appointment type is suitable. Nurse Dana is available to clarify the visit plan. No decision about the concern, billing, urgency, or an additional appointment has been supplied. Sam must acknowledge the expectation, preserve accurate identification, use Alex in conversation, and ask Dana to clarify the clinical plan.',
    cast='Alex | Patient\nSam | Medical assistant',
    culture=('Respect the person and verify the record', 'A preferred name and a verified record name can coexist. Use the requested form of address while following the actual identification process. A mismatch in visit expectations deserves clarification rather than blame for booking or an automatic refusal to discuss the concern.'),
    a='''What does the schedule show? | An annual review | A confirmed procedure for the recent concern | An emergency assessment already completed | A canceled visit | The schedule lists an annual review, while the patient's expectation differs.
What should Sam do with the name preference? | Use Alex while preserving the verified record match. | Open another record under Alex to avoid the mismatch. | Replace verified identifiers without following the correction process. | Use Alexandra in conversation until the appointment type changes. | Alex is the preferred spoken name; that does not justify a duplicate record or an unverified identifier change.
Who can clarify the visit plan? | Nurse Dana | Sam making an independent clinical decision | Another waiting patient | A billing code alone | Dana is the available clinical route, and Sam cannot determine suitability independently.''',
    vocabulary='''check-in | Arrival process confirming a patient and the scheduled visit. | complete check-in
appointment type | Category describing the scheduled purpose or format of a visit. | verify the appointment type
annual review | Periodic review visit recorded as occurring yearly. | attend an annual review
presenting concern | Issue the patient brings to the current visit. | record the presenting concern
chief complaint | Clinical-record term for the main reason for seeking care. | clarify the chief complaint
visit agenda | Topics planned for discussion during the encounter. | clarify the visit agenda
preferred name | Name a person asks others to use when addressing them. | use the preferred name
recorded name | Name shown in the relevant patient record. | verify the recorded name
patient identifier | Information used to match a person with the correct record. | confirm patient identifiers
demographic details | Administrative identity and contact information in a record. | verify demographic details
registration | Creation or updating of required administrative patient information. | complete registration
encounter | A particular interaction or visit involving healthcare services. | document the encounter
appointment slot | Reserved time in a schedule. | confirm the appointment slot
scheduled purpose | Reason for a visit as recorded in the booking. | state the scheduled purpose
patient expectation | What a patient believes will happen during a service or visit. | acknowledge the patient expectation
clinical suitability | Whether a plan or appointment is appropriate for the clinical need. | refer a suitability question
scope of practice | Activities permitted within a role under applicable requirements. | work within scope of practice
delegation | Assignment of an activity under the applicable professional rules. | clarify the delegation
supervision | Required oversight of work by an appropriate professional. | confirm supervision arrangements
clinical handoff | Transfer of relevant information to a receiving clinical professional. | complete a clinical handoff
visit plan | Intended approach to the current appointment. | clarify the visit plan
billing category | Classification used for charging or reimbursement purposes. | verify the billing category
identity match | Confirmation that a person corresponds to the correct record. | establish the identity match
name pronunciation | The way a person's name is spoken. | check name pronunciation''',
    precision='An appointment label describes a scheduled category, not a clinical judgment about every concern raised that day. Do not promise that the concern will be resolved, reject it automatically, or invent a billing outcome from the schedule alone.',
    precision_extra='Using Alex does not mean silently replacing verified identifiers or creating another record. Follow the clinic process for recorded preferences and corrections. Respectful address supports accurate identification; it does not remove the need for it.',
    phrases='''Use the preferred name | Thank you, Alex; I will use that name.
State the schedule | The schedule lists an annual review.
Acknowledge the expectation | You expected to discuss a recent concern.
Name the difference | The recorded visit type and your expectation are not the same.
Avoid a clinical decision | I cannot decide whether this appointment type meets that need.
Offer a named route | Nurse Dana can clarify the visit plan.
Preserve identification | We will keep the verified record linked correctly.
Avoid blame | Let us clarify the plan before assuming how the mismatch happened.
Separate billing | I cannot determine charges from this appointment label alone.
Keep the concern visible | I will include your stated concern in the handoff.
Protect privacy | We can use the appropriate setting for personal details.
Do not promise treatment | I cannot promise a particular clinical outcome.
Ask for clarification | Dana, can you clarify the visit plan with Alex?
Confirm the preference | The verified record says Alexandra; the preferred spoken name is Alex.
Avoid duplicate records | We should use the correctly matched existing record.
Close the loop | I will explain the mismatch to Dana so you do not have to start from nothing.''',
    notes='''Lists | Attributes the category to the schedule rather than presenting it as a clinical decision.
You expected | Acknowledges the patient's understanding without assigning fault.
Can clarify | Offers a next step without promising a clinical outcome.
Before assuming | Stops blame from replacing a factual check.
Linked correctly | Keeps respectful address and accurate identification together.
From the label alone | Limits conclusions about billing or suitability.''',
    d='''Which handoff preserves both facts? | The schedule says annual review; Alex expected to discuss a recent concern. | Alex booked incorrectly and must leave. | Annual review guarantees treatment of every concern. | The record is definitely for another person. | The statement preserves the scheduled category and reported expectation without inventing fault or a clinical decision.
What does using Alex change here? | The respectful form of spoken address, not the verified identity match | The need for all patient identifiers | The clinical urgency of the concern | The billing category automatically | The preferred name affects address while record matching and other decisions remain separate.
Which reassurance is unsupported? | This visit will definitely resolve the concern at no additional cost. | Dana can clarify the plan. | The schedule says annual review. | Sam cannot decide clinical suitability. | Neither the clinical outcome nor any billing decision is established by the facts.
Which action is appropriate? | Pass the mismatch to Dana while keeping the correctly matched record. | Create another record because the patient prefers Alex. | Dismiss the concern because it is not in the schedule label. | Change the clinical plan independently. | The available route is clinical clarification with accurate identification, not an unauthorized record or treatment change.''',
    dialogue='''Alex | I am here for my appointment, but I noticed the reminder says annual review. I thought this was the visit for the concern I called about.
Sam | The [[scheduled purpose::The scheduled purpose is the annual review recorded in the booking, which differs from Alex's stated expectation.]] is an annual review. Thank you for explaining what you expected; I will ask nurse Dana to clarify the plan.
Alex | Before we go further, please call me Alex. Alexandra is the name in my records, but I use Alex in conversation and at work.
Sam | Of course, Alex. Your [[preferred name::The preferred name is Alex, while the verified record name remains Alexandra and must stay correctly linked.]] is clear, and we will keep the verified record correctly linked. I am not creating another record because you use a shorter name.
Alex | Good. I worry that the appointment category means nobody will hear the reason I actually came. Do I need to book something else?
Sam | I cannot decide [[clinical suitability::Clinical suitability requires the appropriate clinical judgment; Sam cannot decide it from the appointment label alone.]] from the schedule label. Dana can clarify how the visit should address your concern before we assume that another booking is required.
Alex | I do not want to explain personal details here in front of everyone. Can the question reach Dana without a discussion across reception?
Sam | Yes. I can identify the mismatch and use the appropriate private route for the [[presenting concern::The presenting concern is what Alex wants addressed, and it should reach the clinical team without unnecessary public disclosure.]]. We do not need to announce personal details to the waiting room.
Alex | Will you tell Dana that I expected this to be the concern visit, rather than just saying that I am unhappy about the reminder?
Sam | I will preserve that [[patient expectation::Patient expectation describes what Alex believed the visit would address, not merely dissatisfaction with an administrative reminder.]]. The handoff will say the schedule lists an annual review and you expected a discussion of a recent concern.
Alex | Is this a billing problem too? I have heard different visit categories can mean different charges, and I do not want a surprise.
Sam | A [[billing category::A billing category may affect charging, but the scenario supplies no verified charge or coverage decision from the visit label.]] is another question to clarify through the proper process. I cannot promise a charge or coverage outcome from the label alone.
Alex | Please check before anyone promises it is covered. I took time off for this visit, and I need to understand what will actually happen today.
Sam | I can confirm the schedule and your expectation, then request a [[clinical handoff::The clinical handoff passes the mismatch to Dana, the identified clinical route, without Sam inventing a treatment decision.]] to Dana. I cannot promise how the clinician will resolve the concern.
Alex | Please also make sure the team uses Alex. Sometimes one person agrees, but the preference disappears as soon as I move to another room.
Sam | I will handle that preference through our record process while preserving the [[identity match::The identity match links Alex to the verified existing record and must remain intact while the preferred address is communicated.]]. The name used in conversation and the correctly matched record need not conflict.
Alex | Thank you. I do not need you to change the appointment yourself; I need someone qualified to clarify what today's visit can include.
Sam | That is the [[visit plan::The visit plan concerns what this encounter will address and is the question Dana can clarify with Alex.]] question for Dana. I will not turn the appointment label into a refusal or a guarantee before that discussion.
Alex | All right. Can you let Dana know I am here? I would like to settle the visit plan before I explain everything again.
Sam | Correct. I will record the [[appointment type::The appointment type remains the recorded annual review, distinct from the clinical clarification now requested.]] accurately and pass on your expectation. We will keep the two facts clear while Dana clarifies the next step.''',
    rehearsal=["Read Alex and Sam's corrected exchange. Stress annual review, recent concern, and Dana; keep the patient concern separate from the booking label.","Switch roles. Repeat the privacy request and preferred-name exchange without changing the verified identity facts.","Complete Morgan's four-line exchange, check the key, then read it aloud with follow-up and initial consultation clearly contrasted."],
    transfer_title='Clarify a different appointment expectation',
    transfer_setup='The schedule says follow-up. Patient Morgan expected an initial consultation. Assistant Lee cannot decide suitability. Nurse Inez is available to clarify the plan.',
    transfer='''Lee: "The recorded visit is a ___." | follow-up | Follow-up is the scheduled category stated in this scenario.
Morgan: "I expected an ___." | initial consultation | The patient's expectation differs from the recorded follow-up category.
Lee: "Nurse ___ can clarify the plan." | Inez | Inez is the available clinical professional named in the facts.
Lee: "Clinical suitability is not yet ___." | established | No clinical suitability decision has been supplied for this mismatch.''',
))

BOOK['units'].append(unit(
    title='Rooming and factual patient reports',
    scene='Report, observation, assessment',
    skill='Give a concise patient report that separates the patient words, observed behavior, and unassessed clinical questions.',
    brief='During rooming, patient Pat says, "I have felt tired since Monday." Assistant Rosa observed Pat answering questions while seated. Rosa has not assessed the cause or severity, and no measurement values are supplied. Nurse Dana is receiving the report. The conversation must preserve the onset as reported by Pat, state the limited observation, and avoid filling missing fields with normal values. Sitting and answering questions do not establish that the concern is mild or safe to defer. Actual urgency must follow the clinic clinical process.',
    cast='Rosa | Medical assistant\nDana | Receiving nurse',
    culture=('Neutral is not dismissive', 'A factual report can be both concise and attentive. Use the patient words and name the limits of the observation. Avoid vague labels such as fine or difficult, which replace useful information with an impression and can distort the clinical handoff.'),
    a='''What onset did Pat report? | Monday | A date measured by Rosa | This morning confirmed by testing | No symptoms ever | Monday is the onset reported by Pat, not an independently measured event.
What did Rosa observe? | Pat answering questions while seated | Normal blood pressure | A diagnosed cause of tiredness | A completed severity assessment | Only the seated question-answering observation is supplied; measurements and conclusions are absent.
What should remain unassessed in the report? | Cause and severity | Whether Pat spoke | Whether Dana is receiving the report | Whether Monday was mentioned | Rosa has not assessed cause or severity and must not manufacture those findings.''',
    vocabulary='''rooming | Preparing a patient for the clinical encounter under the clinic process. | complete the rooming process
patient-reported symptom | Experience described by the patient rather than independently observed. | attribute a patient-reported symptom
onset | When a symptom or condition began. | clarify the reported onset
duration | Length of time an experience or condition has continued. | document symptom duration
severity | Degree or intensity of a condition or symptom. | assess severity
observation | Something directly noticed and described without inventing its cause. | record an observation
subjective information | Information based on a person's reported experience. | attribute subjective information
objective finding | Observed or measured finding, with its source and context. | document an objective finding
baseline | Usual or earlier state used for comparison. | establish the baseline
change from baseline | Difference from a known usual or previous state. | report a change from baseline
associated symptom | Additional symptom occurring with the main concern. | ask about associated symptoms
functional impact | Effect on a person's ability to perform ordinary activities. | describe functional impact
vital signs | Physiological measurements such as pulse and temperature. | record measured vital signs
blood pressure | Pressure exerted by blood within the circulation, measured with relevant units. | document blood pressure
pulse rate | Number of palpable arterial pulses per unit of time. | measure pulse rate
respiratory rate | Number of breaths per unit of time. | record respiratory rate
oxygen saturation | Percentage of hemoglobin oxygen-binding sites occupied by oxygen, estimated or measured by an appropriate method. | report oxygen saturation
temperature | Measure of how hot or cold the body or another object is. | record the measured temperature
unit of measurement | Standard used to express a measured quantity. | include the unit of measurement
measurement time | Time at which a measurement was actually taken. | preserve the measurement time
clinical assessment | Qualified evaluation of health information and the patient's condition. | request clinical assessment
unassessed | Not evaluated through the relevant assessment. | mark severity as unassessed
pertinent negative | Relevant absence established by asking or assessing, not by silence. | document a pertinent negative
source attribution | Identification of where a statement or finding came from. | preserve source attribution''',
    precision='Not reported does not mean absent, and not measured does not mean normal. A pertinent negative requires a relevant question or assessment. Do not populate a record from expectation or convert an empty field into reassurance.',
    precision_extra='Pat answering questions while seated is a limited observation. It does not establish alertness on a formal scale, normal vital signs, a cause of tiredness, or a severity rating. Preserve what was actually observed and leave interpretation with the appropriate clinician.',
    phrases='''Attribute the words | Pat reports feeling tired since Monday.
Quote accurately | Pat said, "I have felt tired since Monday."
Describe the observation | I observed Pat answering questions while seated.
Name the limit | I have not assessed the cause or severity.
Do not invent values | No measurement values are available in this report.
Separate sources | That is the patient report, not a measured finding.
Keep onset attributed | Monday is the onset Pat reported.
Avoid a vague reassurance | I cannot describe the concern as mild from that observation.
State what is missing | The relevant clinical assessment is still needed.
Do not imply absence | An unreported symptom is not automatically absent.
Keep the handoff concise | I will give the report, observation, and outstanding assessment separately.
Use units accurately | Any actual measurement needs its correct value, unit, and context.
Refer the judgment | Dana, please assess the clinical concern through our process.
Preserve uncertainty | I do not have a verified explanation for the tiredness.
Confirm receipt | Have you received Pat's report and the limits of my observation?
Close factually | The cause and severity remain unassessed in my report.''',
    notes='''Pat reports | Keeps the patient's experience distinct from an assistant's clinical conclusion.
I observed | Identifies a firsthand observation and its source.
Since Monday | Gives the reported starting point without inventing a date or duration.
Have not assessed | Describes the actual evidence limit, not a negative result.
Not automatically absent | Prevents a blank field from becoming a clinical finding.
Separately | Helps a receiving professional distinguish evidence types quickly.''',
    d='''Which report is supported? | Pat reports tiredness since Monday; I observed Pat answering questions while seated. | Pat has a mild condition caused by poor sleep. | All vital signs are normal. | Pat is safe to wait because Pat can speak. | The supported report preserves both supplied sources without adding a cause, severity, or safety judgment.
What belongs in the temperature field when no measurement is available? | No invented numeric value | A previous visit's value entered as today's reading | A normal category inferred from Pat answering questions | A numeric value inferred from the reported tiredness | No measurement is supplied; neither a previous value nor an impression can establish today's temperature.
Why is "Pat is fine" inadequate? | It substitutes a broad conclusion for the limited observation. | It gives the exact onset. | It preserves the patient quotation. | It identifies a measured oxygen level. | Fine does not describe the actual observation and implies a clinical reassurance that Rosa has not established.
Which statement about other symptoms is accurate? | No other symptoms are supplied; that does not prove their absence. | Every unmentioned symptom was denied. | Pat has no associated symptoms. | Every blank field can be completed as normal. | Silence in the case does not constitute a negative clinical history or assessment.''',
    dialogue='''Rosa | Dana, I have Pat's rooming report. Pat said, "I have felt tired since Monday." I want to keep that separate from what I observed.
Dana | Please give the [[source attribution::Source attribution identifies Pat as the source of the symptom report and Rosa as the source of the observation.]] clearly. What came from Pat, what did you directly observe, and what has not been assessed?
Rosa | The tiredness and Monday starting point came from Pat. I observed Pat answering questions while seated. I have not assessed the cause or severity.
Dana | Good. The reported [[onset::Onset is the stated beginning of the symptom; Monday is attributed to Pat rather than independently established.]] is Monday. Do not replace it with a guessed date or calculate a duration from an assumed calendar.
Rosa | The handoff draft says looks fine. I will replace that with what I saw: Pat was seated and answering my questions.
Dana | Exactly. Keep the [[observation::The observation is Pat answering questions while seated; it does not establish a diagnosis, severity, or normal measurements.]] specific. Answering questions while seated does not establish the severity of tiredness or whether a concern can safely wait.
Rosa | I also need to flag the blank measurement fields. I have no values to report; those fields should not be read as normal findings.
Dana | Correct. [[Vital signs::Vital signs require actual measurements and context; expected or typical values cannot fill missing clinical data.]] need actual values and appropriate context. A missing measurement cannot be converted into normal by choosing a familiar number.
Rosa | Should I write that Pat denied other symptoms? None are included in the information I am handing over, but I have not established their absence.
Dana | No. A [[pertinent negative::A pertinent negative is an established relevant absence, not a conclusion drawn from an unmentioned symptom.]] must come from the relevant question or assessment. Lack of a statement in this report is not a denial.
Rosa | I will keep the original wording in quotation marks when I use it exactly. If I summarize, I will still identify Pat as the source.
Dana | That preserves the [[patient-reported symptom::The patient-reported symptom is the experienced tiredness described by Pat; attribution remains necessary even when it is paraphrased.]]. Do not translate tired into a specific diagnosis or imply that Pat used a technical term they did not actually say.
Rosa | I also cannot say this is a change from Pat's normal condition unless I have an established usual state to compare it with.
Dana | Right. A [[baseline::A baseline supplies the known usual or earlier state needed for a meaningful comparison; it is not supplied here.]] is not something we should invent. Your report can remain useful without adding a comparison that has not been obtained.
Rosa | The handoff can be short: Pat reports tiredness since Monday; observed answering questions while seated; cause and severity not assessed by me.
Dana | That clearly identifies what is [[unassessed::Unassessed means not evaluated through the relevant process, not evaluated and found normal or harmless.]]. It does not minimize the concern, and it leaves the clinical questions visible for the proper assessment.
Rosa | Have you received those points? I do not want the phrase answering questions to be passed on as a formal severity rating later.
Dana | I have received the report and its limits. [[Clinical assessment::Clinical assessment is the qualified evaluation still needed; it must not be inferred from Rosa's limited rooming observation.]] is separate, and the concern will follow our clinical process rather than an administrative assumption.
Rosa | I will record the report accordingly and preserve what I actually observed. I will not add a measurement, diagnosis, or assurance about waiting.
Dana | Thank you. Keep the [[severity::Severity remains unassessed in Rosa's report and cannot be inferred merely from Pat speaking while seated.]] question open in that record. Clear limits help the receiving team know what still requires attention.''',
    rehearsal=["Read Rosa and Dana's corrected report. Contrast Pat reports with I observed; keep the reported onset attached to Pat.","Switch roles. Repeat the unmeasured-vitals and pertinent-negative exchanges without adding a normal finding.","Complete the second patient report, check the key, and read the patient's words separately from the observation."],
    transfer_title='Attribute a different symptom report',
    transfer_setup='Patient Lee reports dizziness since breakfast. Assistant Noor observed Lee speaking while seated. No measurements or cause assessment are supplied. Nurse Inez receives the report.',
    transfer='''Noor: "Lee reports ___ since breakfast." | dizziness | Dizziness is the symptom attributed to Lee in the facts.
Inez: "The reported onset is ___." | breakfast | Breakfast is the reported starting point, not a measured cause.
Noor: "I observed Lee speaking while ___." | seated | The supplied observation concerns speaking in a seated position.
Inez: "The cause remains ___." | unassessed | No assessment of the cause has been supplied here.''',
))

BOOK['units'].append(unit(
    title='Medication histories with clear sources',
    scene='Two sources, one unresolved entry',
    skill='Document a reported medication change without treating an unverified history as a new clinical instruction.',
    brief='Patient Ren reports that another clinic stopped one medicine. The local medication list still includes it. Ren does not have the outside instruction available. Assistant Talia cannot verify discontinuation, change the list as a clinical decision, or tell Ren to start, stop, or restart treatment. Nurse Dana can review the discrepancy with the clinician. The immediate communication task is to record the patient report and the conflicting local entry with clear sources, then connect the question with Dana. No medicine name, dose, or timing decision is supplied.',
    cast='Ren | Patient\nTalia | Medical assistant',
    culture=('A discrepancy is not a credibility contest', 'Do not make the patient defend their memory against the computer. Acknowledge the report and preserve both sources for review. Respect does not require treating an unverified instruction as confirmed, and careful verification does not require dismissing the patient.'),
    a='''What does Ren report? | Another clinic stopped one medicine. | A new verified prescription has arrived here. | The local clinician has confirmed a restart. | The medication list is already reconciled. | Ren reports an outside change, but the instruction is not available for verification.
What conflicts with that report? | The medicine remains on the local list. | A supplied laboratory result | An established allergy reaction | A confirmed replacement dose | The local list still includes the medicine, creating the stated discrepancy.
What can Dana do? | Review the discrepancy with the clinician | Guarantee that Ren should restart treatment | Prove the outside clinic was wrong without evidence | Treat the local list as a new prescription automatically | Dana is the identified route for appropriate review, not a supplied treatment decision.''',
    vocabulary='''medication history | Account of medicines used or reported, with relevant sources and timing. | obtain a medication history
medication reconciliation | Process of comparing medication information and resolving discrepancies appropriately. | support medication reconciliation
local medication list | Medicine record held by the current organization. | review the local medication list
outside instruction | Direction originating from another healthcare source. | verify the outside instruction
discontinuation | Ending a medicine or order through the relevant clinical process. | confirm discontinuation
patient report | Information supplied by the patient about their experience or history. | document the patient report
active entry | Record item currently marked active in a system. | verify an active entry
historical entry | Record of earlier information rather than necessarily current treatment. | distinguish a historical entry
duplicate entry | Repeated record item that may need clarification. | investigate a duplicate entry
omission | Information missing from a list or account. | identify a possible omission
discrepancy | Difference between sources requiring clarification. | flag a medication discrepancy
prescribing clinician | Professional authorized to prescribe the relevant medicine. | contact the prescribing clinician
dose | Amount intended to be taken or administered at one time. | verify the prescribed dose
strength | Amount of active ingredient in a specified unit of product. | distinguish strength from dose
dosage form | Physical form of a medicine, such as tablet or solution. | confirm the dosage form
route | Way a medicine is taken or administered. | verify the route
frequency | How often a medicine is taken or administered. | clarify the frequency
as-needed instruction | Direction allowing use under specified conditions rather than a fixed schedule alone. | verify the as-needed instruction
over-the-counter medicine | Medicine available without a prescription under applicable rules. | record over-the-counter medicines
dietary supplement | Product used to supplement dietary intake, subject to relevant regulation. | ask about dietary supplements
allergy history | Account of suspected or confirmed allergic reactions with relevant details. | document allergy history
adverse reaction | Harmful or unwanted response associated with a medicine or other exposure. | report an adverse reaction
adherence | Extent to which medicine use corresponds with the agreed plan. | discuss adherence without blame
verification source | Person, document, or system used to confirm information. | identify the verification source''',
    precision='An active entry can reflect the state of a record rather than a verified current instruction. Conversely, a patient report deserves documentation but does not automatically complete reconciliation. Preserve both until the authorized review resolves the discrepancy.',
    precision_extra='A history question is not permission to advise starting, stopping, or restarting a medicine. Dose, strength, route, and frequency describe different aspects of an instruction. Do not fill any of them from memory or from a similar product.',
    phrases='''Acknowledge the report | You report that another clinic stopped this medicine.
State the local source | The local medication list still includes it.
Name the discrepancy | Those two sources need to be reconciled.
Avoid judging memory | I will record what you remember and ask the clinical team to check the difference.
Keep attribution | I will record that this information came from you.
Identify the missing evidence | The outside instruction is not available here.
Give the review route | Dana can review the discrepancy with the clinician.
Avoid treatment advice | I cannot tell you to start, stop, or restart it.
Do not silently delete | We need the appropriate review before treating the entry as resolved.
Preserve the details | I will keep the original source and the reported change clear.
Separate strength and dose | The product strength and prescribed amount are different details.
Include nonprescription use | Relevant nonprescription medicines and supplements also belong in an accurate history.
Do not invent a reaction | No allergy or adverse reaction is established by this discrepancy.
Keep urgency separate | A current medicine concern needs the appropriate clinical route.
Confirm the handoff | Dana will receive both the patient report and the local-list difference.
Close without a new instruction | This conversation records the question; it does not change your treatment.''',
    notes='''You report | Attributes the change without dismissing it or confirming it prematurely.
Still includes | Describes the local record rather than asserting that treatment must continue.
Those two sources | Treats the problem as reconciliation instead of a contest over credibility.
Not available here | Names the evidence gap without claiming the outside instruction never existed.
Start, stop, or restart | Makes the clinical boundary explicit in ordinary language.
Does not change | Prevents a history discussion from being mistaken for prescribing advice.''',
    d='''Which note is accurate? | Patient reports outside discontinuation; local list still includes medicine; instruction unavailable; referred to Dana. | Discontinuation verified from the patient's memory alone. | Patient is nonadherent and the outside clinic is wrong. | Restart approved because the computer says active. | The note preserves the two sources, missing instruction, and review route without inventing a treatment decision.
What does the active local entry establish by itself? | The medicine remains listed locally, not that a new instruction has been verified. | The patient must take it now. | The outside report is false. | Reconciliation is complete. | A record status does not automatically resolve a conflicting report or create a new prescription.
Which reply crosses Talia's stated role? | Restart it until we hear otherwise. | Dana can review the discrepancy. | I will record the source of your report. | I cannot verify the outside instruction here. | Restarting is a treatment instruction that Talia is not authorized to supply in this case.
Which additional conclusion is unsupported? | The discrepancy proves an allergy. | The sources conflict. | The outside instruction is unavailable. | The clinician review is still needed. | No reaction or allergy details are supplied; a record discrepancy cannot establish either.''',
    dialogue='''Ren | Your list still shows a medicine that another clinic told me to stop. I do not have their instruction with me, but I remember the conversation.
Talia | Thank you for telling me. I will record your [[patient report::The patient report attributes the claimed outside change to Ren without pretending the original instruction has been verified.]] and the difference in our list. I am not going to dismiss it because the computer still shows an entry.
Ren | Does the computer mean I should be taking it after all? I do not want two clinics giving me opposite directions without explaining why.
Talia | The [[local medication list::The local medication list is the current organization's record, not automatic proof of a verified present treatment instruction.]] is a record we need to review. It does not let me give you a new instruction to take, stop, or restart a medicine.
Ren | Then please do not remove it and say everything is sorted either. I want the right person to check what the other clinic actually intended.
Talia | Exactly. We need the [[outside instruction::The outside instruction is the missing source needed for appropriate verification; its absence does not prove Ren's report is false.]] and appropriate review. Nurse Dana can take the discrepancy to the clinician; I cannot verify the change myself from this conversation.
Ren | I appreciate that. Sometimes questions about medicines sound as though I am being accused of not following instructions, even when I am trying to explain a change.
Talia | I will not label this an [[adherence::Adherence concerns use in relation to an agreed plan; a conflict between records does not establish deliberate nonadherence.]] problem without evidence. The immediate issue is that your report and our entry differ, and we need to clarify the plan.
Ren | I do not have the other clinic's instructions with me. Can you help get them checked? I am worried about being given conflicting advice again.
Talia | Yes. The [[verification source::A verification source is the document or professional used to confirm information; Ren's attributed report is not a substitute for that review.]] is still to be established through the review. I will distinguish your report from a verified clinical decision.
Ren | The medicine being marked active is what confused me. Is that label always current, or can the record need updating after another clinic makes a change?
Talia | An [[active entry::An active entry describes the system status and may require reconciliation; it cannot independently settle the reported outside change.]] tells us how the item is marked. It does not settle this conflicting information, so we must not treat that label as the answer.
Ren | I also do not have the exact strength or dose in front of me. I would rather say that than give you a number from memory.
Talia | That is helpful. [[Strength::Strength describes active ingredient per product unit and is different from the amount prescribed for a dose.]] and dose are different details, and neither should be guessed. We will preserve what is known and identify what requires verification.
Ren | Can Dana speak with me about it? The list worries me because I still need to know which instruction I should follow.
Talia | It is a [[discrepancy::A discrepancy is the unresolved difference between Ren's report and the local record, not a confirmed treatment error or new instruction.]] needing the appropriate review. I will pass on both sources and the missing instruction rather than silently choose one over the other.
Ren | Please make sure any current question about what I should do reaches the clinical team. I do not want the record discussion mistaken for actual advice.
Talia | I will route that clinical question appropriately. [[Medication reconciliation::Medication reconciliation compares and resolves medication information through the authorized process; merely documenting a conflict does not complete it.]] and clinical guidance need the proper owner, and recording a history does not authorize me to change treatment.
Ren | Then I understand the position: I reported an outside change, your list still includes the medicine, and Dana will review the difference with the clinician.
Talia | Correct. The reported [[discontinuation::Discontinuation is the claimed stopping of the medicine; it remains a reported change rather than a verified decision in this conversation.]] is not yet verified here. I will keep the source clear, preserve the question, and connect the review with Dana.''',
    rehearsal=["Read Ren's question and Talia's responses using the checked answers. Stress reports, active, unavailable, and review.","Switch roles. Repeat the exchange about the outside instruction without adding a dose or restart recommendation.","Complete the Ellis transfer, check the key, then read it aloud with Priya clearly named as the receiving owner."],
    transfer_title='Report a different medication-list change',
    transfer_setup='Patient Ellis reports an outside dose change. The local record is unchanged, and the outside instruction is unavailable. Nurse Priya accepts the query. No new dose is supplied.',
    transfer='''Assistant: "Ellis reports an outside ___ change." | dose | The patient reports a dose change, not an established allergy.
Nurse: "The local record remains ___." | unchanged | The local record has not changed in the supplied facts.
Assistant: "The outside instruction is ___." | unavailable | The outside instruction is not available for verification here.
Nurse: "The receiving owner is ___." | Priya | Priya has explicitly accepted the query for appropriate review.''',
))

BOOK['units'].append(unit(
    title='Laboratory paperwork and specimen queries',
    scene='Two times, two events',
    skill='Preserve collection and arrival times accurately when a colleague proposes an unnecessary record change.',
    brief='A requisition records specimen collection at 09:20. The courier sheet records arrival at 10:05. Colleague Ben proposes replacing 09:20 with 10:05 so the paperwork looks consistent. Assistant Imani notices that the fields describe different events. No patient-identity mismatch, specimen-quality problem, or test result is stated. The pair must retain the event labels and source records, clarify any genuinely ambiguous field through the laboratory process, and avoid creating a false collection time. The 45-minute interval alone does not establish specimen acceptability.',
    cast='Ben | Clinic colleague\nImani | Medical assistant',
    culture=('Question the field, not the colleague', 'A correction request can be challenged without making the exchange personal. Name the field and event that would change, then propose a read-back. Two different values can both be correct when they refer to different events.'),
    a='''Which event occurred at 09:20 according to the requisition? | Collection | Courier arrival | Result authorization | Patient discharge | The requisition explicitly labels 09:20 as the collection time.
What does 10:05 describe? | Arrival on the courier sheet | A revised collection time | A confirmed rejection | A reported test result | The courier sheet records arrival, which is a different event from collection.
What does the interval establish by itself? | A 45-minute difference between the recorded events | Specimen acceptability for every test | A proven transport failure | A diagnostic conclusion | The time difference can be calculated, but no test-specific acceptability criteria or result is supplied.''',
    vocabulary='''requisition | Request document specifying laboratory testing and relevant information. | check the requisition
specimen | Material collected for examination or testing. | identify the specimen
collection time | Time the specimen was obtained from its source. | record the collection time
arrival time | Time an item reached the stated destination. | verify the arrival time
receipt time | Time the receiving service recorded receiving the specimen. | document the receipt time
courier sheet | Transport record containing delivery or movement information. | reconcile the courier sheet
accession number | Identifier assigned by a laboratory to track a case or specimen. | confirm the accession number
specimen label | Information attached to the specimen container for identification. | verify the specimen label
specimen source | Body site or material origin relevant to the test. | record the specimen source
collection method | Technique by which a specimen was obtained. | document the collection method
transport interval | Time between specified transport-related events. | calculate the transport interval
preanalytical phase | Steps before analysis that can affect laboratory testing. | review the preanalytical phase
analytical phase | Stage in which the laboratory examination or measurement is performed. | distinguish the analytical phase
postanalytical phase | Steps after analysis, including review and reporting. | describe the postanalytical phase
acceptance criteria | Requirements for accepting a specimen or process. | check acceptance criteria
rejection criteria | Conditions under which a specimen cannot be accepted for the intended test. | apply rejection criteria
specimen integrity | Condition of the specimen relevant to reliable testing. | assess specimen integrity
hemolysis | Breakdown of red blood cells that can affect some tests. | report hemolysis
insufficient quantity | Amount below what is required for the intended test. | report insufficient quantity
transport medium | Material used to preserve or support a specimen during movement. | verify the transport medium
temperature condition | Required or recorded temperature circumstances. | document temperature conditions
event label | Description of the event to which a time or value belongs. | preserve the event label
record amendment | Traceable correction or addition through the approved record process. | make a record amendment
turnaround time | Interval between defined start and completion events for a service. | define the turnaround time''',
    precision='Collection, courier arrival, laboratory receipt, analysis, and result release are distinct events. Do not assume that arrival on a transport sheet means formal laboratory receipt unless the record defines it that way. Always preserve the stated event label.',
    precision_extra='A 45-minute interval is not itself a specimen-quality verdict. Requirements depend on the specimen, test, container, handling, and actual laboratory procedure. This lesson practices document language, not collection, transport, acceptance, or rejection procedures.',
    phrases='''Identify the first field | The requisition says collection at 09:20.
Identify the second field | The courier sheet says arrival at 10:05.
Name the distinction | Those times describe different events.
Question the proposed change | Why would an arrival time replace a collection time?
Keep both facts | We should preserve each time with its event label.
Avoid cosmetic correction | Matching numbers would make the record less accurate here.
Read back the sequence | Collected at 09:20; arrival recorded at 10:05.
Clarify an ambiguous field | Let us ask the laboratory which event this field requires.
Do not invent a receipt event | The sheet says arrival; it does not establish every later laboratory step.
Separate calculation and judgment | The interval is 45 minutes, not an acceptability decision.
Name missing criteria | We do not have the test-specific acceptance criteria here.
Keep identifiers separate | No identity discrepancy is established by these different times.
Preserve the source | Retain the original requisition and courier references.
Use a traceable process | Any genuine correction needs the approved amendment process.
Do not infer a result | The timing records do not tell us the test result.
Close accurately | Both entries can remain accurate when their event labels are preserved.''',
    notes='''Says collection | Anchors the value to the source and event.
Different events | Explains why numerical disagreement is not necessarily an error.
Would replace | Makes the consequence of the proposed edit explicit.
Here | Limits the conclusion to the supplied records, not every future discrepancy.
Not an acceptability decision | Separates a calculation from a laboratory judgment.
Any genuine correction | Leaves room for real errors without manufacturing one.''',
    d='''Which combined entry preserves the facts? | Collection 09:20; arrival 10:05 | Collection 10:05; arrival 10:05 | Collection and arrival both unknown | Test authorized at 09:20 | The two original times remain attached to their stated events.
Why should 09:20 not be replaced merely for consistency? | The replacement would change a collection event into an arrival time. | All timestamps must always be identical. | Arrival is a more important word than collection. | The test is known to have failed. | Matching the numbers would falsify the supplied event meaning rather than resolve a real discrepancy.
Which conclusion is unsupported? | The specimen is acceptable because only 45 minutes elapsed. | The records describe two events. | The interval is 45 minutes. | No result is supplied. | No test-specific acceptance criteria or relevant handling facts support an acceptability decision.
If a destination field is unclear, what is the next step? | Clarify the required event with the laboratory through the approved process. | Copy whichever time is later. | Replace all original values. | Invent an accession number. | The field meaning must be established before transferring a time into it.''',
    dialogue='''Ben | I have two different times on this paperwork. The requisition says 09:20, but the courier sheet says 10:05. Should I make them match?
Imani | First check the [[event label::The event label identifies what happened at each time; different events need not have matching timestamps.]]. The requisition records collection, while the courier sheet records arrival. Those are not two competing values for the same event.
Ben | So replacing the earlier time would not simply clean up the paperwork. It would say the specimen was collected later than the requisition records.
Imani | Exactly. The [[collection time::The collection time is 09:20 on the requisition and must not be replaced with the separate arrival time.]] is 09:20 in that source. Keeping the record accurate matters more than making two boxes look identical.
Ben | Let me read it back: collected at nine twenty; arrival at ten oh five. The difference is forty-five minutes, but each time has its own meaning.
Imani | That preserves the [[arrival time::The arrival time is 10:05 on the courier sheet; its meaning remains separate from collection and other laboratory events.]] correctly. We also should not rename arrival as a later laboratory event unless the record actually defines it that way.
Ben | I was about to enter ten oh five in a field labeled received. I should check what that field means before assuming the courier entry is enough.
Imani | Yes. [[Receipt time::Receipt time refers to the receiving service's documented event and must not be inferred from an undefined arrival field.]] depends on the receiving record and process. Ask the laboratory which event the destination field requires rather than copying a nearby value.
Ben | The patient details match in these records. I was only looking at the two times; I do not have evidence of a labeling problem.
Imani | That would be a separate [[specimen label::The specimen label supports identification; the two different event times do not themselves establish an identity mismatch.]] or identification question. No identity discrepancy is established here, so we should not turn an event-time difference into a patient mismatch.
Ben | A colleague called that a quick delivery and marked the specimen acceptable. We have the journey time, but have we checked the requirements for this test?
Imani | It gives the [[transport interval::The transport interval is a calculated difference between defined events, not an independent judgment of specimen acceptability.]] between these entries. It does not establish acceptability without the relevant specimen, test, handling conditions, and actual laboratory requirements.
Ben | Then I will avoid writing acceptable or rejected. Neither result follows just from the times we have read on these two documents.
Imani | Correct. [[Acceptance criteria::Acceptance criteria are the applicable requirements for the specimen and test; they are not supplied by the time difference alone.]] belong to the real laboratory process. A language clarification about timestamps is not a quality decision.
Ben | If the laboratory later confirms that a field genuinely was entered incorrectly, we can correct it through the proper process while keeping the history clear.
Imani | That would be a [[record amendment::A record amendment is a traceable correction through the approved process, not an unexplained overwrite to make fields look consistent.]]. It should preserve what was changed and why under our requirements, rather than silently overwrite the original source.
Ben | I also should not tell the patient that these times predict when a result will be ready. Collection-to-arrival is not the entire testing process.
Imani | Exactly. [[Turnaround time::Turnaround time needs defined start and end events; the collection-to-arrival interval does not establish result availability.]] must have defined start and end points. These entries do not supply an analysis completion or result-release time.
Ben | I will keep both source references, preserve 09:20 as collection and 10:05 as arrival, and clarify the receiving field before entering anything there.
Imani | Good. The [[requisition::The requisition remains the source of the collection entry, while the courier sheet supplies the distinct arrival entry.]] and courier sheet can both be accurate. Our task is to carry their meanings forward without creating a false match.''',
    rehearsal=["Read Ben and Imani's corrected dialogue. Say nine twenty and ten oh five clearly, with collection and arrival attached.","Switch roles. Repeat the received-field clarification and the distinction between elapsed time and acceptability.","Complete the 08:40 and 09:15 transfer, check the key, and read it aloud without merging the two events."],
    transfer_title='Keep a second pair of events distinct',
    transfer_setup='The collection record says 08:40. The courier sheet says arrival 09:15. The destination field meaning is unclear. No acceptability decision is supplied.',
    transfer='''Assistant: "Collection was recorded at ___." | 08:40 | The collection record supplies 08:40 as its event time.
Colleague: "Arrival was recorded at ___." | 09:15 | The courier sheet supplies 09:15 as the arrival time.
Assistant: "The event labels must remain ___." | distinct | The times refer to separate events and should not be merged.
Colleague: "The destination field needs ___." | clarification | Its meaning is unclear and must be established before entry.''',
))

BOOK['units'].append(unit(
    title='Referrals and appointment dependencies',
    scene='Friday is a status check',
    skill='Explain referral stages and a named follow-up date without accidentally confirming an appointment.',
    brief='Referral F8 was sent Monday and received by the specialist office Tuesday. The office reports that it is under review; no appointment is booked. Coordinator Lia has agreed to check its status Friday. Patient Morgan believes receipt means an appointment on Friday. Assistant Omar must clarify the actual sequence, distinguish a status check from a booking, and identify Lia as the follow-up owner. No review deadline, appointment date, coverage decision, or reason for the review duration is supplied. Clinical concerns require the clinical route, not a wait for this administrative check.',
    cast='Morgan | Patient\nOmar | Medical assistant',
    culture=('Explain the stage in ordinary language', 'A word such as received may sound final to someone outside the clinic. Give the plain-language meaning and the next known action. Repeating under review without explanation can sound evasive; inventing a likely appointment can be misleading.'),
    a='''What happened Tuesday? | The specialist office received referral F8. | The patient attended a specialist appointment. | Lia completed the Friday check. | A coverage decision was issued. | Tuesday is the recorded receipt event, not attendance or booking.
What is Friday for? | Lia's status check | A confirmed patient appointment | A guaranteed review deadline | A promised test result | The only Friday commitment is Lia checking the referral status.
What remains unconfirmed? | An appointment date | That the referral was sent Monday | That receipt occurred Tuesday | Lia's ownership of the status check | No appointment has been booked in the supplied facts.''',
    vocabulary='''referral | Request for another service or professional to assess or provide care. | send a referral
referring clinician | Professional initiating a referral. | identify the referring clinician
receiving service | Organization or team to which a referral is sent. | contact the receiving service
specialist office | Practice or department providing care in a particular specialty. | check with the specialist office
referral identifier | Reference used to track a particular referral. | quote the referral identifier
sent status | Record that a referral or message was transmitted. | verify the sent status
receipt acknowledgment | Confirmation that the receiving organization obtained the referral. | obtain a receipt acknowledgment
under review | Being assessed through a process before a further decision or action. | explain under review
booking confirmation | Verified notice that an appointment has been scheduled. | obtain booking confirmation
appointment availability | Times or capacity potentially available for booking. | check appointment availability
referral coordinator | Person organizing referral tracking and related communication. | name the referral coordinator
follow-up checkpoint | Agreed point for checking progress or reporting status. | set a follow-up checkpoint
dependency | Event or requirement that another step relies on. | identify a booking dependency
supporting documentation | Information accompanying a request to support its assessment. | supply supporting documentation
referral criteria | Requirements used by a service to assess an appropriate referral. | clarify referral criteria
clinical priority | Urgency or relative need determined through clinical assessment. | refer clinical-priority questions
waiting list | Record of people awaiting an available service. | verify waiting-list status
cancellation slot | Appointment time made available when an existing booking is canceled. | check a cancellation slot
appointment offer | Proposed date or time not necessarily accepted or finalized. | confirm an appointment offer
attendance | Actual presence at an appointment or service. | confirm attendance
referral completion | Completion of the intended referral process, with its definition made clear. | document referral completion
consultation report | Account returned after a specialist or other consultation. | obtain the consultation report
care coordination | Organization of care activities and information across people or services. | support care coordination
access barrier | Practical obstacle to obtaining an intended service. | identify an access barrier''',
    precision='Sent, received, reviewed, offered, booked, attended, and reported are different stages. Even referral complete can have different system meanings. State the actual event instead of assuming a status label proves that the patient has been seen.',
    precision_extra='A Friday status check is not a Friday appointment or a clinical recommendation to wait until Friday. Keep administrative tracking separate from urgent clinical needs. A named coordinator improves follow-up without controlling the specialist decision or appointment availability.',
    phrases='''Identify the referral | We are discussing referral F8.
State transmission | It was sent Monday.
State receipt | The specialist office received it Tuesday.
Explain the stage | They report that it is under review.
Correct the appointment inference | No appointment has been booked.
Define Friday | Friday is Lia's status check, not your appointment.
Name the owner | Lia has agreed to check the status.
Avoid a review guarantee | We do not have a confirmed review-completion date.
Keep an offer distinct | An offered time still needs the relevant booking confirmation.
Do not invent a cause | I do not have a verified reason for the review duration.
Preserve the next step | Lia will check what stage the referral has reached.
Route clinical concern | A new or urgent concern needs our clinical route.
Clarify access needs | We can communicate relevant access needs through the proper process.
Avoid a coverage claim | Referral receipt does not itself confirm insurance coverage.
Check understanding | The referral is received and under review, with no booked appointment.
Close precisely | The confirmed next action is Lia's Friday status check.''',
    notes='''They report | Attributes the status to the receiving office.
No appointment | Explicitly corrects the patient's central misunderstanding.
Not your appointment | Prevents a follow-up day from becoming an arrival instruction.
Has agreed | Identifies a real owner rather than a vague someone.
Confirmed next action | Offers certainty about the known task without controlling external decisions.
New or urgent concern | Keeps clinical needs separate from administrative timing.''',
    d='''Which update accurately uses all three days? | Sent Monday, received Tuesday, and Lia checks status Friday; no appointment is booked. | Booked Monday, attended Tuesday, and results Friday. | Received Tuesday, so Friday attendance is confirmed. | Review must finish Friday because Lia will call. | Each day is attached to its actual event, and the absence of a booking remains explicit.
Which sentence creates a false expectation? | We will see you at the specialist on Friday. | Lia will check the status Friday. | The referral is under review. | No appointment is booked. | Friday is only a coordinator checkpoint, not a supplied appointment.
What does receipt establish? | The referral reached the receiving office, not that a slot is booked. | The specialist completed an assessment. | Insurance coverage is guaranteed. | The patient attended. | Receipt is an earlier administrative stage and does not prove later decisions or attendance.
How should a new clinical concern be handled? | Through the clinic's appropriate clinical route rather than waiting for Lia's routine check | By assuming Friday is always safe | By inventing a specialist assessment over reception | By treating the referral identifier as an urgency score | Administrative follow-up timing does not establish clinical safety or replace assessment.''',
    dialogue='''Morgan | I heard the specialist received my referral on Tuesday, and someone mentioned Friday. What time should I arrive for the appointment?
Omar | Let me clarify the [[follow-up checkpoint::The follow-up checkpoint is Lia's Friday status check, not a booked time for Morgan to attend the specialist.]]. Friday is when Lia will check its status. No specialist appointment has been booked.
Morgan | I thought received meant they had accepted me into a slot. Is there still another step before I can arrange time away from work?
Omar | The [[receipt acknowledgment::Receipt acknowledgment confirms the referral reached the specialist office; it does not establish an appointment or completed clinical review.]] means the office received the referral. They say it is under review, and we do not yet have a date for you to attend.
Morgan | Let me get this straight. It went out Monday and reached them Tuesday. What exactly is Lia doing on Friday if I am not booked in?
Omar | The [[referral identifier::The referral identifier F8 links the conversation to the specific request, preserving which case the three dates describe.]] is F8. It was sent Monday, received Tuesday, and Lia has agreed to check the status Friday.
Morgan | Does under review mean the referral has been rejected, or that the office is still deciding what happens next?
Omar | [[Under review::Under review describes the current assessment stage; it is not a supplied rejection or confirmed booking.]] is the status they gave us. We should not turn it into either a rejection or an appointment confirmation without further information.
Morgan | Who is Lia in this process? I need to know whether she is the person checking the status or the clinician deciding about my care.
Omar | Lia is the [[referral coordinator::The referral coordinator owns the administrative status check here, not the specialist's clinical decision or appointment availability.]] handling this follow-up. Her Friday check does not control the specialist's decision or guarantee that their review will finish that day.
Morgan | I nearly asked for Friday off work. Please make the next message clear about whether it is an update or an actual appointment offer.
Omar | Correct. A [[booking confirmation::Booking confirmation would establish a scheduled appointment, which is specifically absent from the supplied referral status.]] is different from the status check. At present, no appointment date or time is confirmed.
Morgan | If they offer a time later, I may need to explain my work schedule and transport arrangements. I cannot assume every offered slot is possible.
Omar | An [[appointment offer::An appointment offer is a proposed time that still needs the relevant agreement and confirmation, not automatic attendance.]] should be handled through the booking process. Relevant access needs can be communicated appropriately rather than assuming an offered time has already been accepted.
Morgan | I also wondered whether the referral being received means my plan has approved the visit. I do not want to confuse the two processes.
Omar | The [[receiving service::The receiving service's acknowledgment concerns referral receipt and does not by itself verify the patient's insurance coverage.]] receiving a referral does not itself confirm coverage. Any coverage question needs the appropriate verification, separate from the current referral status.
Morgan | What if the concern I was referred for changes before Friday? Should I simply wait because that is when Lia has promised to check?
Omar | No administrative checkpoint establishes that waiting is safe. A change or urgent concern needs our clinical route for [[clinical priority::Clinical priority requires the appropriate clinical assessment and cannot be inferred from a routine coordinator follow-up date.]], not an assumption based on Lia's diary.
Morgan | Understood. The referral reached them Tuesday and remains under review. Lia will check Friday, but I do not have an appointment yet.
Omar | Exactly. That is the current [[care coordination::Care coordination keeps the referral status, owner, and next action connected without falsely reporting that the specialist visit is booked.]] position. I will keep the status and ownership clear, and any actual booking information must be confirmed separately.''',
    rehearsal=["Read Morgan and Omar's checked dialogue. Stress sent Monday, received Tuesday, and status check Friday.","Switch roles. Repeat the work-schedule question and explain the actual referral stage without inventing a booking.","Complete the transfer using the printed referral facts, check the key, and read the checkpoint as an update, not an appointment."],
    transfer_title='Separate another checkpoint from booking',
    transfer_setup='Referral G3 was received Wednesday and remains under review. No appointment is booked. Coordinator Noor will check Monday.',
    transfer='''Assistant: "The referral identifier is ___." | G3 | G3 identifies the specific referral in this second scenario.
Patient: "Receipt was confirmed ___." | Wednesday | Wednesday is the receipt day, not an appointment date.
Assistant: "The status remains ___." | under review | The receiving service has not supplied a booked appointment.
Patient: "Noor will check on ___." | Monday | Monday is the coordinator checkpoint rather than a confirmed visit.''',
))

BOOK['units'].append(unit(
    title='Supporting questions during a clinical visit',
    scene='Clarify before leaving',
    skill='Support a patient request for a private explanation while preserving the original clinical instruction.',
    brief='Patient Jules has not yet left the clinic and does not understand a phrase in the after-visit summary. Jules wants an explanation away from reception before leaving. Dr Chen is available. Assistant Mina cannot reinterpret or change the clinical instruction. No exact instruction, treatment detail, or revised plan is supplied. Mina must identify the document and unclear phrase, pass the question to Dr Chen, and arrange the appropriate private conversation. A patient saying yes or receiving the document does not by itself establish understanding.',
    cast='Jules | Patient\nMina | Medical assistant',
    culture=('Make a question welcome', 'Patients may hesitate to ask again when staff appear busy. Thank the person for identifying the unclear wording, and avoid treating clarification as failure. A request for privacy can be handled without announcing the personal question across reception.'),
    a='''Which document contains the unclear phrase? | The after-visit summary | A supplied insurance appeal | A courier manifest | A new prescription invented by Mina | The brief identifies the after-visit summary as the source.
Who is available to explain the clinical instruction? | Dr Chen | Mina acting outside the stated role | Another patient in reception | An automated guess | Dr Chen is available while Mina cannot reinterpret the instruction.
What does Jules request? | An explanation before leaving, away from reception | A silent change to the instruction | A public discussion across the waiting area | A claim that understanding is already confirmed | The patient requests timely clarification in an appropriate private setting.''',
    vocabulary='''after-visit summary | Document summarizing relevant information and instructions after a clinical encounter. | review the after-visit summary
clinical instruction | Direction concerning care or treatment from an authorized professional. | clarify a clinical instruction
plain language | Clear wording suited to the intended audience. | explain in plain language
technical term | Specialized word used within a professional field. | explain a technical term
jargon | Specialized expressions that may be unfamiliar outside a group. | clarify unfamiliar jargon
abbreviation | Shortened form of a word or phrase. | expand an abbreviation
ambiguity | Wording that permits more than one interpretation. | resolve an ambiguity
clarification | Explanation that makes meaning more definite or understandable. | request clarification
reinterpretation | Assigning a meaning that changes or newly determines the original instruction. | avoid unauthorized reinterpretation
teach-back | Checking an explanation by inviting the person to express their understanding. | use teach-back appropriately
show-me method | Checking understanding by asking the person to demonstrate an instructed action. | use the show-me method
chunk and check | Giving information in short portions and checking understanding between them. | use chunk and check
health literacy | Ability to find, understand, and use health information and services. | support health literacy
language access | Appropriate support enabling communication across language differences. | arrange language access
qualified interpreter | Person with the relevant skills and qualifications to interpret accurately in context. | request a qualified interpreter
translation | Rendering written information into another language. | obtain an appropriate translation
interpretation | Rendering spoken or signed communication into another language, or explaining meaning in another context. | clarify the required interpretation
accessible format | Presentation adapted to a person's communication or access needs. | provide an accessible format
private discussion | Conversation conducted with appropriate protection from unnecessary hearing. | arrange a private discussion
patient question | Specific issue the person wants clarified. | preserve the patient question
understanding check | Method used to establish whether an explanation was understood. | conduct an understanding check
instruction source | Document or professional from which a direction came. | identify the instruction source
revised plan | Updated clinical plan established by the appropriate professional. | confirm a revised plan
question handoff | Transfer of a specific question to the person who can address it. | complete a question handoff''',
    precision='Clarifying where a phrase appears is different from deciding what the clinical instruction means. Mina can preserve the question and connect Jules with Dr Chen. This does not authorize a paraphrase that changes treatment, timing, or conditions.',
    precision_extra='Teach-back checks the explanation, not the intelligence of the patient. A yes answer or a handed-over summary does not establish comprehension. In this scene, Dr Chen must explain the clinical wording; no new medical direction should be invented during practice.',
    phrases='''Welcome the question | Thank you for telling me which part is unclear.
Identify the document | The phrase is in your after-visit summary.
Preserve the wording | I will keep the original wording with your question.
State the boundary | I cannot reinterpret this clinical instruction.
Name the available clinician | Dr Chen is available to explain it.
Respect the timing | You would like clarification before you leave.
Respect privacy | We can arrange the appropriate conversation away from reception.
Avoid a guessed meaning | I do not want to give you an explanation that changes the instruction.
Make the handoff specific | Dr Chen, Jules has a question about this phrase in the summary.
Do not imply understanding | Receiving the summary does not mean every instruction is clear.
Invite a clearer explanation | Please ask Dr Chen to explain the phrase in language that works for you.
Keep the question intact | I will not reduce your concern to a generic request for information.
Distinguish support needs | An interpreter request and a clinical meaning question may require different support.
Avoid shaming | Asking again is a reasonable part of understanding the plan.
Keep changes attributed | Any revised clinical plan must come from the authorized clinician.
Close the route | I will connect the question with Dr Chen before you leave.''',
    notes='''Which part | Makes the request specific without requiring a public account of personal details.
Keep the original | Protects the instruction from accidental alteration during a handoff.
Available to explain | Names a real route instead of leaving the patient with a refusal.
Before you leave | Preserves the patient's timing request.
Language that works for you | Invites understandable communication without blaming the listener.
Any revised plan | Distinguishes explaining an existing direction from changing it.''',
    d='''Which response best preserves Jules's request? | Dr Chen is available; I will pass on this phrase and arrange the appropriate private explanation before you leave. | I will guess what the instruction probably means. | You received the paper, so clarification is complete. | Ask another patient what they did. | The response preserves the specific question, clinician route, timing, and privacy request.
What does handing over the summary establish? | The document was provided, not that the patient understands every instruction. | Teach-back was completed. | A revised plan was approved. | Every abbreviation was explained. | Document delivery and understanding are distinct events requiring different evidence.
Which statement misuses teach-back? | It is a test to prove the patient is intelligent enough. | It helps check whether an explanation was clear. | It can reveal a misunderstanding. | It may require another explanation. | Teach-back evaluates communication and understanding rather than judging the patient's intelligence.
What must remain unchanged in Mina's handoff? | The original instruction and the substance of the patient's question | A guessed clinical meaning supplied by Mina | A new dose invented for simplicity | An unsupported promise of treatment success | Preserving the source and question allows the clinician to clarify without distortion.''',
    dialogue='''Jules | Mina, I have not left yet because one phrase on this paper is unclear. I can read the words, but I do not know what I am meant to do.
Mina | Thank you for raising it. This is your [[after-visit summary::The after-visit summary is the document containing the unclear phrase, so the handoff should preserve that source.]]. Please indicate the phrase, and I will pass the actual wording and your question to Dr Chen.
Jules | Could you just explain what it means? I know everyone is busy, but I do not want to go home and make the wrong assumption.
Mina | I cannot reinterpret the [[clinical instruction::A clinical instruction concerns care and requires the appropriate professional explanation; Mina cannot invent its meaning in this role.]]. Dr Chen is available, so I can connect you with the clinician who can explain it properly.
Jules | I would prefer not to discuss the personal details across reception. There are several people waiting, and this is not something I want them to hear.
Mina | We can arrange an appropriate [[private discussion::A private discussion addresses Jules's request to ask away from reception without announcing the personal details publicly.]]. I will tell Dr Chen that you want clarification before leaving and that the setting matters to you.
Jules | Thank you. I sometimes nod because I recognize a term, then realize I do not understand how it applies to the instruction.
Mina | Recognizing a [[technical term::A technical term may be familiar in appearance without being understood in its clinical context, which is why clarification remains necessary.]] does not always make the instruction clear. Asking again is reasonable; receiving the paper does not mean every question has been answered.
Jules | Could you show Dr Chen this line on the summary? It is this phrase, not the whole page, that I cannot make sense of.
Mina | I will preserve the [[patient question::The patient question concerns a specific phrase and its practical meaning, not merely a nonspecific request for more information.]] with the wording. That gives Dr Chen the actual issue rather than a vague message that could miss it.
Jules | I would like a plain explanation, not just the same phrase repeated more loudly. I heard it; the meaning is what I need.
Mina | You can request [[plain language::Plain language addresses understandable wording; louder repetition of the same unclear phrase does not resolve its meaning.]] from Dr Chen. I will not substitute my own clinical interpretation while arranging that explanation.
Jules | After Dr Chen explains it, can I say back what I would actually do? I sometimes say yes too quickly when someone asks whether I understand.
Mina | Yes. That kind of [[teach-back::Teach-back helps the professional check the explanation by hearing the patient's understanding, rather than accepting a yes answer as sufficient.]] can help the clinician identify what still needs clarification. It is not a test of your intelligence or a reason to feel embarrassed.
Jules | I also want the original wording available during the conversation. Otherwise someone might explain a shortened version and miss the part that confused me.
Mina | Keeping the [[instruction source::The instruction source preserves the actual wording and context for Dr Chen instead of an altered summary created during the handoff.]] with the question will help. We should not edit the direction simply to make the handoff shorter.
Jules | So there is no new instruction from this conversation yet. The next step is for Dr Chen to clarify the existing phrase privately before I leave.
Mina | Correct. No [[revised plan::A revised plan would require an authorized clinical change, which has not occurred merely because Jules asked for clarification.]] has been established here. I am arranging the explanation, not changing the clinical direction.
Jules | Please tell Dr Chen that I am still here and that I want to understand the instruction before going. I appreciate having a clear next step.
Mina | I will make that [[question handoff::The question handoff includes the document, specific phrase, privacy request, and need for clarification while Jules remains at the clinic.]] now: the phrase in your summary, your request for privacy, and clarification before leaving. Dr Chen is the available clinician for that conversation.''',
    rehearsal=["Read Jules and Mina's corrected exchange. Keep the unclear phrase, original summary, and private explanation connected.","Switch roles. Repeat the request to explain understanding in the patient's own words without inventing the clinical instruction.","Complete Ari's abbreviation exchange, check the key, then read it aloud with Dr Malik and before leaving clearly stated."],
    transfer_title='Route an unclear abbreviation',
    transfer_setup='Patient Ari asks about an abbreviation in the visit summary before leaving. Assistant Lee cannot interpret the clinical instruction. Dr Malik is available for a private explanation.',
    transfer='''Lee: "The unclear item is an ___." | abbreviation | The supplied question concerns an abbreviation in the visit summary.
Ari: "I want clarification before ___." | leaving | Ari is requesting explanation before leaving the clinic.
Lee: "Dr ___ is available." | Malik | Dr Malik is the available clinician identified in this scenario.
Ari: "I would like the explanation to be ___." | private | The facts specify an appropriate private explanation with the clinician.''',
))

BOOK['units'].append(unit(
    title='Telephone concerns and clinical escalation',
    scene='After the clinical connection',
    skill='Confirm a received clinical handoff and record its actual outcome without inventing an assessment or delaying care.',
    brief='Caller Ellis asked assistant Noor whether a new concern could wait until next week\'s routine appointment. Noor could not assess urgency and immediately connected Ellis with nurse Dana through the clinic process. Dana received the call. This later conversation reviews the handoff record; it does not delay the live clinical call. No symptom details, clinical assessment, or waiting advice are supplied. Noor must record the actual recipient and outcome without inventing a clinical conclusion. Applicable emergency procedures take priority over routine call handling or documentation.',
    cast='Noor | Medical assistant\nDana | Receiving nurse',
    culture=('A calm caller can still need assessment', 'Tone of voice is not a reliable substitute for clinical information. Be respectful and direct when someone asks for reassurance you cannot provide. Name the available clinical route immediately, rather than giving a long explanation of your limitations.'),
    a='''What is Ellis asking Noor to decide? | Whether a new concern can safely wait until next week's visit | The spelling of a street name | A confirmed test result | A completed medication review | The caller seeks a clinical timing decision rather than an administrative fact.
Who is available now? | Nurse Dana through the clinical-call route | An unspecified clinician next month | A specialist appointment already booked | No one in the clinic | Dana is specifically available now for the proper clinical route.
What does the lack of supplied symptom details establish? | The exercise has not established urgency or safety to wait. | The concern is harmless. | The caller has no symptoms. | A routine visit is definitely enough. | Missing clinical information cannot be turned into a reassuring assessment or a negative finding.''',
    vocabulary='''clinical-call route | Established pathway for calls requiring clinical review. | use the clinical-call route
triage | Clinical assessment that determines urgency and appropriate next care. | refer for triage
urgency assessment | Evaluation of how promptly a concern requires attention. | obtain an urgency assessment
routine appointment | Scheduled visit not itself proof that a new concern can wait. | distinguish a routine appointment
new concern | Newly raised issue requiring appropriate handling. | report a new concern
clinical escalation | Moving an issue to the appropriate level of clinical attention. | initiate clinical escalation
warm transfer | Call transfer with an introduction or relevant handoff to the receiving person. | arrange a warm transfer
blind transfer | Transfer without a direct introduction or confirmed contextual handoff. | avoid an unsupported blind transfer
receiving clinician | Clinical professional accepting the concern or handoff. | identify the receiving clinician
callback queue | List of requests awaiting a return call. | check the callback queue
callback commitment | Agreed promise about a return contact, with scope made clear. | confirm a callback commitment
call disposition | Recorded outcome or next handling status of a call. | document the call disposition
dropped call | Telephone connection that ends unexpectedly. | follow the dropped-call process
verified callback number | Return-contact number checked through the appropriate procedure. | obtain a verified callback number
identity check | Process of confirming who is communicating. | complete the identity check
emergency pathway | Established route for immediate emergency response. | follow the emergency pathway
red flag | Finding or feature that may signal a serious concern requiring appropriate action. | escalate a reported red flag
safety-net advice | Professional guidance about changes or circumstances requiring further help. | provide authorized safety-net advice
symptom onset | Time a reported symptom began. | relay symptom onset
symptom progression | How a symptom has changed over time. | describe symptom progression
reassurance | Statement intended to reduce concern, which must not exceed evidence or authority. | avoid unsupported reassurance
closed-loop communication | Exchange that confirms receipt and intended action. | use closed-loop communication
SBAR | Situation, background, assessment, recommendation: a structured communication framework. | use SBAR within the actual role
escalation outcome | Result of routing a concern, including whether it was received. | record the escalation outcome''',
    precision='A routine appointment is an administrative booking, not a clinical assessment of a new concern. Calm speech, a familiar patient, or an empty symptom field cannot establish that waiting is safe. Follow the actual clinical and emergency pathways.',
    precision_extra='A queued message is not a connected clinical call. Preserve the actual outcome and follow the clinic process if transfer fails or the connection drops. A structured handoff must not contain an assessment or recommendation invented by someone outside the authorized role.',
    phrases='''Acknowledge the question | You want to know whether this can wait until next week.
State the limit briefly | I cannot assess urgency or tell you it is safe to wait.
Offer the immediate route | Nurse Dana is available through our clinical-call route now.
Avoid unsupported reassurance | I do not have a clinical assessment that would support that reassurance.
Separate the booking | The routine appointment does not answer the new clinical question.
Preserve the request | I will pass on your question about how soon you need care.
Use the actual pathway | We need to follow the clinic's clinical-call process.
Confirm the recipient | I will identify the person receiving the concern.
Protect continuity | We should use the verified contact process if the connection fails.
Do not claim connection early | A message in a queue is not the same as a completed transfer.
Keep facts attributed | I will relay what you report without adding a diagnosis.
Avoid guessed advice | I will not invent treatment or safety-net instructions.
Keep emergency priority | Applicable emergency procedures take precedence over routine call handling.
Check receipt | Please confirm that the receiving clinician has the concern.
Record the outcome | The note must show whether the clinical transfer succeeded.
Close the handoff | The timing question belongs with the available clinical team now.''',
    notes='''You want to know | Shows understanding of the actual question before routing it.
Cannot assess urgency | Names the specific boundary instead of a vague refusal to help.
Available now | Makes the next step concrete and timely.
Does not answer | Separates the scheduled visit from the new concern.
Whether it succeeded | Keeps the record focused on outcome rather than effort.
Without adding | Preserves the caller's information and avoids invented clinical content.''',
    d='''Which response addresses the caller's need appropriately? | I cannot assess whether waiting is safe; Dana is available now through our clinical-call route. | If you sound calm, next week is fine. | A routine appointment always means the concern can wait. | No details were supplied, so nothing is wrong. | The response avoids an unsupported assessment and identifies the immediate clinical route.
What does an unanswered transfer establish? | The clinical connection has not been completed. | Dana received and assessed the concern. | The caller was reassured by a clinician. | The issue is resolved. | An attempted transfer is not evidence of a received or completed clinical assessment.
Which information must not be invented for a structured handoff? | A diagnosis or urgency decision outside Noor's role | The caller's actual question | The receiving person's name when confirmed | The actual transfer outcome | A framework organizes real information; it does not authorize fabricated clinical judgments.
What takes precedence when applicable? | The actual emergency pathway | Waiting for next week's booking regardless of circumstances | Completing an English practice dialogue | Obtaining a routine administrative update first | Emergency procedures must not be delayed by a routine booking or language exercise.''',
    dialogue='''Noor | Dana, thanks for taking Ellis's call immediately. I am checking my handoff note now, after the connection. Ellis asked whether a new concern could wait until next week.
Dana | I received that question. Your note should not contain an [[urgency assessment::Urgency assessment is a clinical judgment, not a decision Noor made when connecting the call.]] from you. Receiving the call and assessing the concern are different events.
Noor | I told Ellis I could not decide that and connected the call through our process. I did not ask Ellis to finish a long administrative discussion first.
Dana | Good. The request needed [[triage::Triage addresses urgency and care needs; asking whether a concern can wait requires more than a booking check.]], not a yes-or-no answer from reception. Keep the actual clinical response in the appropriate clinical record.
Noor | Ellis already had a booking next week. I included that as background, but I did not say the booking established a safe waiting period.
Dana | Correct. A [[routine appointment::An existing routine booking does not assess a new concern or establish a safe waiting period.]] does not assess a new concern. Do not let the appointment date become the only information the next person receives.
Noor | My note currently says passed to nursing. That leaves out who received the call. I should name you and record the actual connection.
Dana | Yes. The [[clinical-call route::This is the established pathway used to connect Ellis with Dana; its actual outcome must be recorded.]] worked in this case. Record that factual outcome, not simply an attempt to put somebody through.
Noor | I gave you Ellis's question without describing Ellis as anxious or suggesting the concern was mild. Neither would have been a finding I had established.
Dana | As the [[receiving clinician::Dana confirmed receipt. Naming her does not authorize Noor to invent a clinical conclusion on her behalf.]], I need the actual report. Your introduction helped me understand why Ellis was calling rather than making Ellis start with the appointment history again.
Noor | I stayed for the introduction and confirmed the connection before leaving the call. I will describe what happened rather than just checking a transfer box.
Dana | That is the relevant [[warm transfer::Noor introduced the concern and confirmed Dana received the call, rather than merely attempting an unconfirmed transfer.]] detail. Keep the actual handoff time in the record; do not substitute the later time at which you finish writing.
Noor | For a future call, if the line disconnects before anyone confirms receipt, I cannot use today's completed status as the default.
Dana | Exactly. Follow the clinic's [[dropped call::A dropped call needs the actual continuity process; interruption does not establish successful clinical contact.]] process. Verified contact details and the actual unresolved concern matter; do not silently leave a failed connection marked complete.
Noor | And if I only put a request into a message queue, the note should still show pending contact, not that the patient spoke to a nurse.
Dana | Right. A [[callback queue::A callback queue holds requests awaiting contact, not evidence that a clinical conversation or assessment occurred.]] is not a clinical conversation. Use the appropriate follow-up and escalation process for the real situation, rather than assume the queue resolves urgency.
Noor | This record review happened after the immediate connection. We should never make an active caller wait while we discuss all these documentation examples.
Dana | Agreed. The actual [[emergency pathway::Applicable emergency procedures take priority over administrative work or this later language-practice review.]] takes precedence when needed. Do not use this case to decide that another caller is nonurgent.
Noor | I will record your confirmed receipt and my factual introduction. I will not add a diagnosis, waiting advice, or clinical outcome that you have not provided.
Dana | That keeps the [[escalation outcome::Dana's receipt is confirmed; no diagnosis, completed assessment, or waiting advice is supplied here.]] accurate. The call reached me; your note should say that clearly while leaving the clinical findings to the clinical record.''',
    rehearsal=["Read Noor and Dana's corrected review. Stress received, not independently assessed, and the actual call outcome.","Switch roles. Repeat the distinction between a connected call and a queued message without adding a clinical result.","Complete Ari's interrupted-transfer exchange, check the key, then read it aloud without claiming receipt or assessment."],
    transfer_title='Preserve an interrupted clinical transfer',
    transfer_setup='A clinical transfer for caller Ari disconnects before receipt is confirmed. Assistant Lee must use the clinic dropped-call process. Nurse Priya is the intended clinical recipient. No assessment has occurred.',
    transfer='''Lee: "Receipt has not been ___." | confirmed | The connection ended before anyone confirmed clinical receipt of the concern.
Colleague: "Use the clinic's ___ process." | dropped-call | The scenario specifies the established process for interrupted contact.
Lee: "The intended recipient is nurse ___." | Priya | Priya is the named clinical recipient for this transfer.
Colleague: "No clinical ___ has occurred." | assessment | The facts explicitly state that clinical assessment has not occurred.''',
))

BOOK['units'].append(unit(
    title='Records, corrections, and follow-up ownership',
    scene='Thursday, not Tuesday',
    skill='Correct an appointment message with a clear apology, verified booking details, and an accurate contact record.',
    brief='Assistant Elena sent patient Robin a message incorrectly saying that a results discussion was booked Tuesday. The verified schedule shows Thursday at 14:00 with Dr Chen. Robin rearranged work after the incorrect message. Elena can correct the communication and confirm the actual booking, but no test results or clinical interpretation are supplied. The appointment itself has not been changed from Tuesday to Thursday; the earlier message was wrong. Elena must preserve that distinction, acknowledge the disruption, and document whether the correction actually reached Robin.',
    cast='Robin | Patient\nElena | Medical assistant',
    culture=('Correct the message without rewriting the history', 'An apology is more useful when it names what went wrong and supplies the verified replacement information. Avoid describing an inaccurate message as a rescheduled visit if the booking never changed. Acknowledge the practical effect without making an unsupported compensation promise.'),
    a='''What does the verified schedule show? | Thursday at 14:00 with Dr Chen | Tuesday at 14:00 with a different clinician | An appointment already attended | A canceled results discussion | The schedule confirms Thursday at 14:00 with Dr Chen.
What caused Robin to rearrange work? | Elena's inaccurate Tuesday message | A confirmed clinical emergency | An actual schedule change from Tuesday | A supplied abnormal result | The case identifies the incorrect message as the reason for the work disruption.
Which topic is not supplied for discussion? | The actual test results | The verified appointment details | The correction ownership | The effect of the wrong message | No result values or clinical interpretations are part of this exercise.''',
    vocabulary='''appointment confirmation | Verified communication of a scheduled visit and its details. | send an appointment confirmation
incorrect notification | Message containing inaccurate information. | correct an incorrect notification
schedule of record | Authoritative schedule used to verify the actual booking. | check the schedule of record
message correction | Communication replacing an inaccurate earlier message. | issue a message correction
rescheduling | Changing an actual appointment from one slot to another. | distinguish rescheduling from correction
results discussion | Appointment or conversation in which a clinician explains test findings. | confirm a results discussion
result interpretation | Clinical explanation of what findings mean in context. | refer result interpretation
date verification | Checking the actual calendar date associated with a booking. | complete date verification
twenty-four-hour time | Time notation running from 00:00 through 23:59. | use twenty-four-hour time
time-zone reference | Identification of the time zone when relevant to communication. | clarify the time-zone reference
read-back | Repeating important information to confirm accurate receipt. | request a read-back
correction timestamp | Recorded time at which an amendment or correction occurred. | preserve the correction timestamp
original entry | Earlier record item retained under the applicable process. | preserve the original entry
addendum | Additional note linked to an existing record. | enter an addendum
audit trail | Record showing the sequence and authorship of events or changes. | maintain an audit trail
communication log | Record of relevant contacts and their outcomes. | update the communication log
contact attempt | Effort to reach someone without assuming successful contact. | document a contact attempt
successful contact | Confirmed communication with the intended recipient. | verify successful contact
acknowledgment | Confirmation of receipt or recognition of information. | record acknowledgment
follow-up owner | Person responsible for a specified unfinished next action. | name the follow-up owner
outstanding action | Task that remains to be completed. | track the outstanding action
service disruption | Practical interference caused by a service problem. | acknowledge the service disruption
escalation route | Defined path for a concern requiring additional attention or authority. | explain the escalation route
closure evidence | Information establishing that the intended task was actually completed. | retain closure evidence''',
    precision='Correcting Tuesday to Thursday in a message is not necessarily rescheduling. The verified booking was Thursday; the communication was wrong. Keep that history accurate so a later colleague does not infer a clinical or scheduling decision that never occurred.',
    precision_extra='A results discussion appointment does not reveal whether results are normal, abnormal, urgent, or already reviewed. Confirm the booking within the role and route clinical questions appropriately. In real communication, verify the full date and relevant location or time-zone details.',
    phrases='''Open the correction | I need to correct the appointment message I sent you.
Name the error | I wrote Tuesday, but that was incorrect.
Give the verified booking | The schedule confirms Thursday at 14:00 with Dr Chen.
Translate the time | Fourteen hundred is two in the afternoon.
Distinguish the event | This corrects my message; it is not a change from a Tuesday booking.
Apologize directly | I am sorry that my incorrect message disrupted your work arrangements.
Avoid a result inference | The appointment details do not tell us what the results mean.
Keep the role clear | Dr Chen will handle the clinical discussion.
Check accurate receipt | Please read back the verified day and time.
Preserve the original | The record should retain the earlier message and its correction appropriately.
Document contact honestly | An attempted call is not the same as speaking with you.
Name the owner | I am responsible for communicating this correction.
Track unfinished work | Any unsuccessful contact must remain an open action.
Offer the actual route | We can use the clinic's process for any unresolved service concern.
Avoid an unsupported promise | I cannot promise a remedy that has not been authorized.
Close with the verified facts | Thursday at 14:00 with Dr Chen is the confirmed booking.''',
    notes='''I wrote | Names the source of the error without vague blame.
But that was incorrect | Explicitly withdraws the earlier information.
Not a change | Distinguishes a message repair from a real booking change.
Disrupted your work | Acknowledges the specific effect instead of a generic inconvenience.
Read back | Checks factual receipt of appointment details.
Remain an open action | Prevents an unsuccessful attempt from being marked complete.''',
    d='''Which correction preserves the history? | My Tuesday message was wrong; the verified booking is Thursday at 14:00 with Dr Chen. | Your appointment has been moved from Tuesday even though the schedule never changed. | Tuesday and Thursday mean the same thing here. | The booking is unverified because a message was wrong. | The original error was in the message, while the schedule supplies the verified Thursday booking.
Which conclusion about results is unsupported? | Thursday means the results are definitely normal. | Dr Chen is the named clinician. | No results are supplied in the exercise. | The booking is for a results discussion. | Scheduling details do not establish the content or clinical significance of test results.
What should be recorded if Robin is not reached? | The contact attempt and the still-outstanding correction | Confirmed patient receipt | Completed results counseling | Robin's agreement to the booking | An unsuccessful attempt does not prove that the patient received or acknowledged the corrected details.
Which apology is strongest? | I am sorry my incorrect Tuesday message disrupted your work arrangements. | I am sorry you understood the Tuesday message differently. | I am sorry the schedule changed, although the verified booking never changed. | I am sorry for the inconvenience; the original date does not matter now. | The strongest apology identifies the actual message error and work disruption without shifting blame or inventing a schedule change.''',
    dialogue='''Robin | Elena, I arranged time off for the Tuesday results discussion, but the latest information says Thursday. Has the appointment been moved again?
Elena | I need to make a [[message correction::The message correction replaces Elena's inaccurate Tuesday notification; the actual booking was not changed from Tuesday to Thursday.]]. My Tuesday message was incorrect. The verified schedule shows Thursday at 14:00 with Dr Chen.
Robin | That matters because I changed my work shift after reading what you sent. I need to know whether Thursday is confirmed or just another possible date.
Elena | I have checked the [[schedule of record::The schedule of record is the verified source showing Thursday at 14:00 with Dr Chen, rather than another tentative message.]]. Thursday at 14:00 with Dr Chen is confirmed. I am sorry my incorrect message disrupted your work arrangements.
Robin | I have the Tuesday message right here. Was that date wrong from the start, or did someone move my appointment without telling me?
Elena | You are right. This is not [[rescheduling::Rescheduling changes an actual appointment; here the booking remained Thursday and only the Tuesday message was wrong.]]. The earlier message was wrong; I should not describe that as moving an appointment that was booked for Tuesday.
Robin | Fourteen hundred means two in the afternoon, correct? I want to check the time as well as the day before I speak to my manager.
Elena | Correct. That is [[twenty-four-hour time::Twenty-four-hour time expresses two in the afternoon as 14:00, which is the verified booking time in this case.]] for two in the afternoon. Please keep Thursday, 14:00, and Dr Chen together when you read back the details.
Robin | Thursday at two in the afternoon with Dr Chen. Does the later day tell me anything about whether the results are normal or serious?
Elena | No. A [[results discussion::A results discussion identifies the purpose of the appointment and does not reveal the findings or their clinical significance.]] booking does not tell us what the results mean. I can confirm the appointment, but the clinical explanation belongs with Dr Chen.
Robin | I understand. Please do not let my question about the date become a note saying that someone already explained the results to me.
Elena | I will keep [[result interpretation::Result interpretation is a clinical explanation that has not occurred in this conversation, which concerns only the booking correction.]] separate from this correction. The record should describe the appointment information communicated, not a clinical conversation that did not happen.
Robin | Will the earlier message remain visible appropriately? Otherwise a later colleague may think I simply chose the wrong day when I arranged work.
Elena | We need the appropriate [[audit trail::The audit trail preserves the inaccurate original message and its correction, so the sequence is not rewritten as patient error.]]. I will preserve the earlier event and the correction through our process rather than erase the reason for your confusion.
Robin | And will you record that you actually reached me today? I would like the team to know I received and repeated back the Thursday information.
Elena | Yes. This is [[successful contact::Successful contact means Robin actually received the corrected details; it is different from a call attempt or unsent message.]], not merely an attempted call. I will document the actual communication and acknowledgment through the required process.
Robin | Please send the corrected details through the clinic's usual channel too. I need something accurate to refer to when I rearrange my shift.
Elena | Exactly. A named [[follow-up owner::A follow-up owner remains responsible for unfinished communication; an unsuccessful contact attempt must not automatically close the task.]] would need to keep that action visible. I own this correction and will record what has actually been communicated.
Robin | Thank you for acknowledging the work disruption. I may still raise that concern through the clinic process, but I now have the confirmed appointment details.
Elena | We can use the appropriate [[escalation route::The escalation route provides a real process for the unresolved service concern without inventing an unauthorized remedy or compensation promise.]] for that concern. The verified booking remains Thursday at 14:00 with Dr Chen, and I am sorry for the inaccurate Tuesday message.''',
    rehearsal=["Read Robin and Elena's corrected dialogue. Contrast the wrong Tuesday message with the verified Thursday booking.","Switch roles. Repeat the apology and read-back, saying 14:00 and two in the afternoon as the same time.","Complete the second correction, check the key, and read the verified time without describing the message error as rescheduling."],
    transfer_title='Correct a different time error',
    transfer_setup='Assistant Noor sent 09:00 in error. The verified booking is Friday at 11:30 with Dr Shah. The appointment itself has not changed. Patient Ari has now received the correction.',
    transfer='''Noor: "My message incorrectly said ___." | 09:00 | The error was the 09:00 time in the message.
Ari: "The verified time is ___." | 11:30 | The schedule confirms 11:30 rather than the earlier message time.
Noor: "The clinician is Dr ___." | Shah | Dr Shah is the clinician named in the verified booking.
Ari: "This is a message correction, not ___." | rescheduling | The appointment itself did not change; only the communication was corrected.''',
))
