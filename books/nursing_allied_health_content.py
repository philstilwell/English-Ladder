"""Original nursing and allied-health language simulations."""
from books.authoring import unit

BOOK = dict(
    slug='nursing-allied-health', title='Nursing and Allied Health English',
    cover_label='Handoffs / patient education / teamwork / safety',
    cover_title='Nursing &\nAllied Health', cover_size=33,
    tagline='Speak clearly. Check understanding. Confirm the next action.',
    audience='For nurses, therapists, and allied-health professionals communicating with patients, families, and clinical teams.',
    map_intro='Eight clinical communication simulations, from shift handoffs to patient explanations and safety reviews.',
    notes_title='Clear language is part of the care.',
    notes_intro='Clinical conversations move between technical detail and everyday language. A colleague needs a precise observation and an actionable request; a patient needs a usable explanation without unexplained shorthand. These fictional cases practice that change of register while keeping uncertainty, professional boundaries, and the patient\'s own account visible.',
    field_notes=[
        ('Lead with the important change', 'Identify yourself, the person concerned, the change, and the response you need. A well-organized report supports prompt attention; it must never delay urgent action while you perfect the wording.', '"This is a change from the earlier assessment. I need a review now."'),
        ('Name the source of information', 'Separate what you observed, what the patient reported, and what another record states. Preserve a discrepancy for appropriate review instead of silently choosing the version that looks most convenient.', '"The record says none known; the patient reports a previous reaction."'),
        ('Check the explanation, not the patient', 'Use ordinary language and small steps. A patient\'s own account of the agreed plan can reveal a misunderstanding that a polite nod leaves hidden. Clarify and check again without blame.', '"I may not have explained that clearly. Let us go through that step again."'),
        ('Close the loop with the receiving person', 'State who owns the next action and confirm that the other person has understood it. Sending a message, accepting a task, and completing that task are different events.', '"You will follow the pending result and contact the responsible clinician. Is that correct?"')],
    scope_note='Original fictional language practice, not clinical training, medical advice, or a treatment protocol. No real patient information is used. Follow current local procedures, professional scope, applicable privacy rules, and qualified clinical judgment. UK sources are identified as such; their legal duties are not presented as universal rules.',
    sources=[
        dict(title='Agency for Healthcare Research and Quality. TeamSTEPPS: Communication.', url='https://www.ahrq.gov/teamstepps-program/curriculum/communication/index.html', note='Background on structured handoffs, SBAR, and checking back. The original simulations do not prescribe clinical response thresholds.', checked='30 September 2026'),
        dict(title='Agency for Healthcare Research and Quality. Use the Teach-Back Method: Tool 5.', url='https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html', note='Background on checking the clarity of an explanation through a patient\'s own words and clarifying misunderstandings.', checked='30 September 2026'),
        dict(title='National Institute for Health and Care Excellence. Drug Allergy: Recommendations, section 1.2.', url='https://www.nice.org.uk/guidance/CG183/chapter/recommendations', note='UK guidance supporting the distinction between reported reactions, documented allergy status, and information requiring clarification.', checked='30 September 2026'),
        dict(title='Nursing and Midwifery Council. The Code, sections 10 and 16.', url='https://www.nmc.org.uk/standards/code/read-the-code-online/', note='UK professional standards used as background for accurate records and raising safety concerns, not as a universal legal checklist.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Shift Handoffs and Clinical Prioritization',
    scene='The shift ends; the result is still pending',
    skill='Transfer an unfinished clinical follow-up with its current status, named owner, and confirmed next action.',
    brief='In a simulation, outgoing nurse Maya hands over to incoming nurse Jonas at 7 p.m. A requested laboratory result is still pending; Maya has not seen a value. The responsible clinician has asked to be contacted when it becomes available. Jonas will take over checking the result and contacting that clinician through the agreed route. The team must also continue the existing care plan. The handoff does not establish a new diagnosis or replace local escalation procedures.',
    cast='Maya | Outgoing nurse\nJonas | Incoming nurse',
    culture=('Transfer the task, not just the information', 'An experienced colleague may sound brief without intending to be dismissive. Ask for the missing owner or action directly. A concise handoff is useful only when the receiving person knows which facts are current and which responsibilities they are accepting.'),
    a='''What is known about the requested result? | It is pending, with no value available to Maya. | It is within the expected range. | It has been reviewed by the responsible clinician. | It was cancelled at the shift change. | The briefing states that the result is pending and no value has been seen.
Which responsibility is transferring? | Checking for the result and contacting the responsible clinician when available | Choosing treatment from the expected result | Replacing the existing care plan | Declaring the patient ready for discharge | Jonas is taking over the specified follow-up, not a new clinical decision.
What completes the verbal transfer? | Jonas confirms the task and next action, and Maya checks that confirmation. | Maya names the test without discussing follow-up. | The shift clock reaches seven. | The result remains in the electronic record. | Mutual confirmation establishes what the receiving nurse understood and accepted.''',
    vocabulary='''handoff | Transfer of relevant information and responsibility between care professionals. | give a structured handoff
shift overlap | A period when outgoing and incoming staff are both present. | use the shift overlap
patient identifier | An approved detail used to establish the correct person's identity. | verify patient identifiers
current status | The person's or task's condition at the stated present time. | summarize current status
baseline | A reference condition used when describing a change. | compare with the baseline
relevant history | Background information that bears on the present care situation. | provide relevant history
pending result | A requested result not yet available or finalized. | follow a pending result
outstanding task | An action that remains to be completed. | identify outstanding tasks
follow-up owner | The named person accountable for the next agreed action. | name the follow-up owner
receiving clinician | The professional taking over information or care responsibility. | confirm the receiving clinician
contingency | An agreed response if a specified situation occurs. | clarify the contingency
check-back | Repetition and confirmation used to verify a received message. | use a check-back
SBAR | Situation, background, assessment, and recommendation or request. | structure the report with SBAR
I-PASS | A structured handoff framework expanded in the precision note below. | use an I-PASS handoff
care plan | The documented, agreed approach to a person's care. | continue the care plan
action list | A stated set of tasks with relevant responsibility and timing. | review the action list
clinical priority | The relative urgency established through appropriate clinical assessment. | communicate clinical priority
escalation route | The designated path for obtaining further clinical attention. | confirm the escalation route
read-back | Repeating supplied information to check its accuracy. | complete a read-back
acknowledgment | Confirmation that a message has been received. | obtain an acknowledgment
responsibility transfer | Explicit movement of a defined duty to another professional. | document responsibility transfer
continuity of care | Coordination that connects care across people, shifts, or settings. | support continuity of care
source record | The original record from which information is taken. | check the source record
time stamp | A recorded time attached to an observation or action. | include the time stamp''',
    precision='Pending is not normal, negative, reviewed, or unimportant. State what has actually been received and who will follow it. A handoff framework organizes communication; it does not supply missing observations or authorize a clinical decision.',
    precision_extra='I-PASS: illness severity; patient summary; action list; situation awareness and contingency plans; synthesis by receiver. Use the locally adopted format. Acknowledgment confirms receipt; a check-back also verifies meaning. Urgent changes still require the appropriate immediate response.',
    phrases='''Open the transfer | I am handing over one result that is still pending.
Confirm identity | Let us verify the patient identifiers before discussing the record.
Time the report | This is the status at the seven o'clock handoff.
Separate known from unknown | I have not seen a result value yet.
Name the request | The responsible clinician asked to be contacted when it is available.
Give the owner | You are taking over that follow-up from this handoff.
Accept the task | I will check for the result and contact the responsible clinician.
Check understanding | Please repeat the outstanding action so we can confirm it.
Correct a mismatch | Not reviewed; it is still pending.
Preserve the plan | The existing care plan remains in place unless appropriately changed.
Use the source | Let us check the current record rather than rely on an old summary.
Keep urgency visible | A change in condition follows the clinical escalation process.
Avoid a guess | We cannot describe a value that has not been received.
Name the contingency | Which agreed route applies if the expected follow-up cannot be completed?
Document the transfer | Record the task, receiving professional, and agreed next action.
Close the loop | That is correct; you have the pending-result follow-up.''',
    notes='''Pending versus reviewed | These describe different stages; neither should be substituted for the other.
I will versus someone will | A named commitment is easier to act on than an unspecified expectation.
Stable | Use only when supported by an actual clinical assessment, not as a filler word.
Handoff or handover | Both terms are common; local usage varies.
Read-back versus completion | Repeating an action does not mean the action has already occurred.
At seven | A time reference limits the status claim to the information then available.''',
    d='''Which opening preserves the known facts? | At seven, the result is still pending; Jonas will follow it and contact the responsible clinician. | At seven, the result was reviewed and no action was needed. | The laboratory will probably call, so no owner is necessary. | The shift has changed, so the original request no longer applies. | The first statement preserves pending status and names the agreed follow-up responsibility.
Jonas says, "I will review the normal result." What needs correction? | No value is available, so normal is unsupported. | The result is definitely abnormal. | The follow-up task has been cancelled. | The clinician has already changed treatment. | No result value has been received, so neither normal nor abnormal is established.
Which response is a useful check-back? | I will check for the result and contact the responsible clinician when it is available. | I heard a test mentioned. | The computer probably knows what to do. | I will wait for the next handoff to discuss ownership. | The response repeats both the task and the action requested when the result arrives.
What should happen if an urgent change occurs before the result? | Use the appropriate clinical escalation process without waiting for that result. | Wait because result follow-up was assigned first. | Call the result normal to simplify the handoff. | Treat the communication framework as a replacement for local procedures. | Pending information does not justify delaying the appropriate response to an urgent clinical change.''',
    dialogue='''Maya | Before I leave, we need to hand over one unfinished follow-up. We have checked the patient identifiers, and this report reflects the position at seven.
Jonas | Go ahead with the [[current status::Current status identifies what is actually known at the stated handoff time.]]. I have the correct record open, but I do not want to mistake an earlier note for the latest information.
Maya | The requested laboratory result has not arrived. I have not seen a value, and the responsible clinician asked to be contacted when it becomes available.
Jonas | So it remains a [[pending result::Pending result means no available result has yet supplied the value being discussed.]], not a reviewed result. I will not describe it as normal just because there is no new value on this screen.
Maya | Correct. The request to contact the clinician still stands. The shift change should not leave the task sitting between two people who each assume the other will act.
Jonas | I will be the [[follow-up owner::The follow-up owner is the named person accepting responsibility for the outstanding action.]] from this handoff. I will check for the result and contact the responsible clinician through our agreed route when it is available.
Maya | That is the action I am transferring. The existing care plan continues; this conversation does not introduce a different treatment or a new assessment.
Jonas | I will retain the [[care plan::The care plan remains the documented approach unless an appropriately authorized change is made.]] and follow any properly communicated changes. I also want to keep this result task separate from other observations and responsibilities on the shift.
Maya | The current record contains the request and the relevant background. If a copied summary conflicts with it, we need to clarify that difference rather than choose the shorter version.
Jonas | I will use the [[source record::The source record provides the original information against which summaries should be checked.]] to verify the request. A familiar phrase in yesterday's summary is not enough to establish what is required now.
Maya | Exactly. If the patient's condition changes before the result arrives, that change needs its own assessment and response. We cannot wait merely because this test is outstanding.
Jonas | The [[escalation route::The escalation route provides the appropriate path for further clinical attention when needed.]] remains available for that concern. The pending-result task is not a reason to postpone attention to a new clinical change.
Maya | Please repeat the follow-up in one sentence. I want to check that I have given you a clear action rather than just another piece of information.
Jonas | Here is my [[check-back::A check-back repeats the received task so the sender can verify accurate understanding.]]: I will check for the outstanding result and contact the responsible clinician when it becomes available, using the agreed route.
Maya | That matches my request. If the follow-up cannot be completed through that route, use the applicable local process rather than leave an unacknowledged message indefinitely.
Jonas | I will keep the [[outstanding task::An outstanding task remains open until the required follow-up has actually occurred.]] visible until the required follow-up is complete. An acknowledgment that I heard you is not evidence that the clinician has reviewed the result.
Maya | Good. We should record who accepted the task and when. That will help the next person distinguish this transfer from an assumption made after I left.
Jonas | I will document the [[responsibility transfer::Responsibility transfer records the accepted movement of a defined duty between professionals.]] with the relevant time. The record will state the actual arrangement, not imply that the result was already available.
Maya | We agree, then: no value yet, your follow-up from seven, and contact with the responsible clinician when the result arrives. The other care responsibilities remain in place.
Jonas | Agreed. That supports [[continuity of care::Continuity of care connects the unfinished work across the shift boundary with an explicit owner.]] across the shift change. I have the request, the source, and the next action, rather than simply a test name.''',
    transfer_title='Seen by whom?',
    transfer_setup='A scan report is available, but the responsible clinician has not yet reviewed it. The incoming therapist agrees to contact that clinician. No clinical interpretation is supplied.',
    transfer='''Therapist: "The report is available, but clinical review is ___." | pending | Availability of a report does not mean the responsible clinician has reviewed it.
Nurse: "Who owns the next ___?" | action | The exchange needs an explicit owner for the remaining contact task.
Therapist: "I will ___ the responsible clinician." | contact | The supplied agreement assigns that contact to the incoming therapist.
Nurse: "Do not add an unsupported ___." | interpretation | No clinical interpretation appears in the supplied facts for this exercise.'''))

BOOK['units'].append(unit(
    title='Patient Assessment and Escalation',
    scene='A change needs a clear request',
    skill='Report a new concern with its time, source, and comparison, then confirm an appropriate clinical response.',
    brief='In a simulation at 10:20 a.m., patient Alex tells nurse Priya, "I feel worse than earlier." Priya observes that Alex is now stopping mid-sentence to catch a breath, unlike at 10 a.m. The cause is not established. Priya uses the local urgent-response process immediately and communicates with responding clinician Dan. The exercise practices that exchange during the response, not a reason to delay it. No treatment, diagnosis, or numerical threshold is supplied.',
    cast='Priya | Nurse\nDan | Responding clinician',
    culture=('Directness can be a safety skill', 'A clear request for urgent review is not an accusation. State the change and what you need without softening the message into a casual suggestion. Professional politeness should not obscure urgency, and a senior colleague should acknowledge the concern explicitly.'),
    a='''What changed between the supplied observations? | Alex now stops mid-sentence to catch a breath. | A diagnosis was confirmed. | A new numerical result became available. | The patient withdrew the concern. | The brief contrasts the earlier observation with the new interruption of speech.
What is the source of "I feel worse than earlier"? | Alex's own report | A laboratory result | Dan's completed assessment | A copied discharge note | The statement is attributed directly to the patient, rather than to a clinician or test.
What is Priya already doing? | Using the local urgent-response process | Waiting to complete a perfect script | Assigning a diagnosis from the dialogue | Deferring the concern until the next shift | The briefing explicitly places the communication within an immediate local response.''',
    vocabulary='''patient-reported symptom | A change or experience described by the patient. | record a patient-reported symptom
clinical observation | A finding noticed or measured during clinical care. | communicate a clinical observation
change from baseline | A difference from the person's relevant reference condition. | report a change from baseline
onset | The beginning of a symptom or change. | clarify symptom onset
time course | The pattern of a condition or change over time. | describe the time course
deterioration | Worsening of a person's clinical condition. | recognize possible deterioration
assessment finding | Information obtained through an appropriate clinical assessment. | report assessment findings
clinical concern | A reason for professional attention to possible patient risk. | state the clinical concern
urgent review | Prompt assessment requested because of a clinical concern. | request an urgent review
response activation | Initiating the applicable process for clinical assistance. | confirm response activation
clinical uncertainty | A stated limit on what is known about a clinical situation. | communicate clinical uncertainty
differential diagnosis | Possible explanations considered through qualified clinical assessment. | discuss a differential diagnosis
situational awareness | Shared understanding of the current conditions and relevant risks. | maintain situational awareness
call-out | A clear announcement of important information to the team. | make a focused call-out
closed-loop communication | An exchange in which receipt and meaning are confirmed. | use closed-loop communication
assertive statement | A direct, respectful expression of a concern or need. | make an assertive statement
safety concern | A condition that may expose someone to harm. | raise a safety concern
chain of command | The designated sequence for escalating unresolved concerns. | use the chain of command
reassessment | A further assessment after time, intervention, or a change. | communicate reassessment findings
response time | The interval between a request and the relevant response. | record the response time
bedside review | Clinical assessment with the patient present. | arrange a bedside review
monitoring plan | The agreed approach to observing and responding to clinical status. | clarify the monitoring plan
clinical rationale | The professional reasoning supporting a clinical decision. | explain the clinical rationale
escalation record | Documentation of the concern, contacts, response, and relevant times. | complete the escalation record''',
    precision='Describe the actual change and its time before adding an interpretation. A patient-reported symptom and your own observation can both matter, but they are different sources. Do not turn a concern into a confirmed diagnosis merely to sound confident.',
    precision_extra='Urgent language should accompany the appropriate response, not replace it. Follow local procedures and professional judgment. This fictional exchange supplies no treatment, monitoring interval, diagnostic conclusion, or universal trigger for activating a clinical team.',
    phrases='''State the change | This is different from the observation at ten o'clock.
Attribute the report | Alex says, "I feel worse than earlier."
Describe what you see | Alex is now stopping mid-sentence to catch a breath.
Request review | I need an urgent review now.
Confirm action | I have activated the local response process.
Avoid an unsupported diagnosis | The cause has not been established.
Give the time | I observed this change at 10:20.
Keep the concern clear | I am concerned about the change, not just the wording in the earlier note.
Ask for acknowledgment | Please confirm that you have received the urgent request.
Correct minimization | The earlier assessment does not describe what I am seeing now.
Summarize the comparison | Earlier speech was uninterrupted; now Alex pauses to catch a breath.
Clarify responsibility | Who is taking the clinical review, and what response is underway?
Escalate an unresolved concern | The concern remains unresolved; I am using the next appropriate route.
Stay within evidence | I can report the observation without claiming a cause.
Record the response | Document the concern, contact time, and actual response.
Maintain continuity | Any further change needs to reach the responding team promptly.''',
    notes='''Worse | Attribute the patient's word and add relevant observations rather than replacing it with a diagnosis.
Now versus earlier | These time markers make the comparison actionable.
Could you perhaps | Excessive softening can hide an urgent request.
No diagnosis yet | Uncertainty about cause does not mean there is no need for attention.
Response activated | This is an action status, not proof that an assessment has finished.
Escalation | Escalating an unresolved concern is not the same as blaming a colleague.''',
    d='''Which opening is most useful during the response? | At 10:20 Alex is stopping mid-sentence to catch a breath, unlike at ten; I need urgent review. | Alex was assessed earlier, so this is probably unchanged. | I have a possible administrative issue whenever you are free. | The cause is confirmed because the patient said worse. | The message gives the observed change, comparison, time, and requested response without diagnosing.
Which statement properly separates sources? | Alex reports feeling worse; I observe pauses to catch a breath. | The laboratory reports that Alex feels worse. | Dan observed the change at ten before it occurred. | The patient's words are my confirmed diagnosis. | The first statement distinguishes the patient's account from the nurse's observation.
Dan has not acknowledged the request. Which response fits the brief? | Continue the appropriate urgent escalation process rather than assume silence means acceptance. | Treat the request as accepted because it was sent. | Wait until the next shift to check receipt. | Replace the concern with a less urgent message. | A sent request is not confirmed receipt, and the urgent concern remains actionable.
What should the later record describe? | Actual observations, attributed reports, relevant times, and the response taken | A diagnosis added to make the narrative decisive | An earlier status copied as though current | An assessment marked complete before it happened | A factual escalation record preserves both the clinical information and what actually occurred.''',
    dialogue='''Priya | Dan, I have activated our urgent-response process for Alex. At ten twenty, Alex is stopping mid-sentence to catch a breath. This differs from the observation at ten.
Dan | I have received the request for [[urgent review::Urgent review is the prompt clinical assessment Priya is requesting in response to the change.]]. I am responding now. Tell me what Alex reported and what you observed, without waiting to establish a cause.
Priya | Alex said, "I feel worse than earlier." I observed the pauses while Alex was speaking to me. I have not established what is causing the change.
Dan | That separates the [[patient-reported symptom::The patient's description is a reported experience, distinct from the nurse's direct observation.]] from your own finding. Keep the patient's words attributed rather than rewriting them as a diagnosis that has already been confirmed.
Priya | At ten, Alex spoke without those pauses during my conversation. I am concerned that the earlier note could make this sound like an unchanged situation.
Dan | Your comparison identifies a [[change from baseline::The comparison shows a difference from the earlier reference observation, not an unchanged status.]]. The earlier entry provides context, but it cannot substitute for assessment of what is happening now.
Priya | I need the team to understand the urgency. I do not want my request to sound like a routine update that can wait until the next round.
Dan | Your [[clinical concern::The clinical concern is the stated reason for prompt professional attention to the observed change.]] is clear. Keep the request for review now at the front of the message; the receiving team should not have to infer urgency from the older note.
Priya | Thank you. I will communicate any further change through the response already underway. I will not delay that process while trying to produce a perfectly worded summary.
Dan | Maintain [[situational awareness::Situational awareness keeps the team aligned on the current condition, relevant change, and response.]] across the team. Everyone involved needs the present concern and response status, not just the reassuring language of an older entry.
Priya | If a request is not acknowledged, I should not assume that pressing send means the receiving person has accepted responsibility for responding.
Dan | Correct. Use [[closed-loop communication::Closed-loop communication includes confirmation of receipt and meaning rather than reliance on sending alone.]] and the appropriate escalation process. The route must remain responsive to the concern; an unanswered message is not a completed clinical review.
Priya | For the handover to the responding team, I can give the patient identifiers, the two observation times, the patient's words, and the action already taken.
Dan | Include the [[time course::The time course describes how the concern developed across the supplied observations.]] clearly. In this case, the earlier observation and the change at ten twenty are more useful than an unspecific statement that things changed sometime.
Priya | I also want to avoid writing a possible cause as if it were established. We have a concern requiring assessment, not a diagnosis from this conversation.
Dan | State that [[clinical uncertainty::Clinical uncertainty identifies what remains unknown without reducing the need for an appropriate response.]] explicitly. Not knowing the cause does not reduce the importance of reporting the change or obtaining the appropriate assessment.
Priya | I will record the observation and the response activation with their times. Later actions should be added as they actually occur, not as though they already happened.
Dan | The [[escalation record::The escalation record documents the concern, communication, timing, and actual response for continuity.]] should reflect that sequence. Documenting a request for assessment and documenting the completed assessment are different entries about different events.
Priya | We have the urgent request acknowledged and the response underway. The next team should receive the same factual comparison without an invented result or treatment instruction.
Dan | Agreed. Any [[reassessment::Reassessment is a further clinical assessment whose findings must reflect what is actually established.]] findings will be communicated through the clinical process. Keep the current concern visible as the responding team takes over; the earlier note must not obscure the change.''',
    transfer_title='An earlier note is not a current finding',
    transfer_setup='At 2 p.m., a therapist identifies a new change during a simulation and uses the appropriate response route. A colleague refers to an unchanged status recorded at noon.',
    transfer='''Therapist: "The noon entry is an ___ observation." | earlier | Noon precedes the new finding at two and cannot establish the current status.
Colleague: "The two o'clock finding describes a ___." | change | The supplied facts explicitly identify something new rather than an unchanged condition.
Therapist: "The appropriate response is already ___." | underway | The briefing says the therapist has used the appropriate response route.
Colleague: "We must not substitute the old note for a current ___." | assessment | An earlier record does not replace assessment of the newly identified change.'''))

BOOK['units'].append(unit(
    title='Medication Safety and Allergy Clarification',
    scene='The allergy field and the patient disagree',
    skill='Communicate conflicting allergy information without deleting a report, diagnosing a reaction, or guessing a medication decision.',
    brief='In a simulation, the medication record says "no known drug allergies." Patient Rosa reports a rash after an antibiotic several years ago, but cannot recall the name or exact date. No current reaction is reported. Nurse Mei contacts pharmacist Sam through the local medication-safety process before the unresolved discrepancy is treated as settled. The available facts do not establish the cause of the historical rash or authorize a drug choice, dose, or administration decision.',
    cast='Mei | Nurse\nSam | Pharmacist',
    culture=('Make uncertainty specific', 'A patient may use allergy for several kinds of past experience. Listen without dismissing the account or confirming a diagnosis beyond the evidence. Explain what needs clarification and preserve the source of each detail so the next professional can assess it appropriately.'),
    a='''Which conflict needs review? | The record says no known drug allergies, while Rosa reports a previous rash after an antibiotic. | Two clinicians have confirmed opposite diagnoses. | Rosa reports a current reaction to a named drug. | The record supplies a verified date that Rosa disputes. | The discrepancy is between the documented status and an incompletely identified historical patient report.
Which details remain unknown? | The antibiotic name and exact date | Whether Rosa described a rash | Whether the record contains an allergy entry | Whether Mei contacted the medication-safety process | The briefing explicitly identifies the missing drug name and date.
What can this language exercise establish? | How to communicate the discrepancy accurately for appropriate review | Which drug should be administered | That the historical rash was definitely allergic | That the patient has no relevant history | The supplied facts support accurate communication, not a clinical conclusion or medication decision.''',
    vocabulary='''allergy status | The documented position on a person's known or suspected allergies. | verify allergy status
drug allergy | A harmful immune-mediated response to a medicine. | assess a suspected drug allergy
adverse drug reaction | A harmful, unintended response to a medicine. | document an adverse drug reaction
intolerance | An unwanted response that is not necessarily an immune-mediated allergy. | clarify a reported intolerance
hypersensitivity | A reproducible adverse response associated with exposure to a substance. | describe suspected hypersensitivity
reaction history | The account of a previous response to a medicine or substance. | obtain a reaction history
suspected culprit | The medicine or substance thought possibly responsible. | identify the suspected culprit
generic name | The nonproprietary name of a medicine's active substance. | verify the generic name
brand name | A product name assigned by a manufacturer. | record the brand name
formulation | The prepared form of a medicine, such as a tablet or liquid. | confirm the formulation
route of administration | The way a medicine enters the body. | verify the route of administration
temporal association | A relationship in timing that does not alone prove causation. | describe a temporal association
medication reconciliation | Comparing medication information to identify and resolve differences. | complete medication reconciliation
medication administration record | The record used to document medicines administered. | check the medication administration record
discrepancy | A difference between two accounts or records. | escalate a discrepancy
patient account | Information reported by the person receiving care. | preserve the patient account
corroborating record | Another reliable record that may support or clarify an account. | seek a corroborating record
unable to ascertain | Not possible to establish from the available information. | document information as unable to ascertain
no known drug allergies | A stated absence of known drug allergies, not a synonym for unknown. | verify a no-known-drug-allergies entry
allergy alert | A visible notification drawing attention to relevant allergy information. | review an allergy alert
contraindication | A circumstance making a treatment inappropriate under applicable clinical criteria. | check a contraindication
prescriber clarification | Information sought from the authorized prescribing professional. | request prescriber clarification
pharmacist review | Professional assessment of a medication-related question by a pharmacist. | obtain pharmacist review
record reconciliation | Resolving documented differences through an authorized process. | track record reconciliation''',
    precision='A report of a rash after a medicine establishes a reported sequence, not a confirmed immune mechanism. Preserve the report and seek appropriate review. No known allergies and information not established are different statuses; do not substitute one for the other.',
    precision_extra='Medication administration record is often shortened to MAR. Use approved terminology and documentation procedures locally. An alert, an order, and a pharmacist review serve different purposes; none should be treated as permission to guess away conflicting information.',
    phrases='''State the discrepancy | The allergy field and the patient's account do not match.
Attribute the history | Rosa reports a rash after an antibiotic several years ago.
Identify the unknown | She cannot recall the drug name or exact date.
Avoid diagnosis | The cause of that historical reaction is not established.
Separate the timing | No current reaction has been reported in this scenario.
Seek review | Please review this discrepancy through the medication-safety process.
Preserve the report | Do not erase the patient's account to make the fields agree.
Avoid false certainty | Unknown is not the same as no known allergies.
Ask specifically | What happened, when did it happen, and which medicine was involved?
Check other records | Is there an appropriate prior record that could clarify the medicine?
Distinguish names | We need to verify the active substance, not assume from a remembered brand.
Route the decision | The medication decision needs the appropriately authorized clinical review.
Explain the purpose | I am checking the difference so the team has accurate information.
Confirm receipt | Please confirm who is reviewing the unresolved history.
Update appropriately | Record clarified information through the authorized documentation process.
Close the discrepancy | Keep the difference visible until the review actually resolves it.''',
    notes='''After versus because of | The first states a time relationship; the second claims causation.
Allergy versus intolerance | Do not assign either label solely to simplify the conversation.
None known versus unknown | One is a stated status; the other describes missing information.
Historical versus current | A past report and a current reaction require distinct descriptions.
Reported | This word attributes information without dismissing it.
Reconciled | Use only when the relevant difference has actually been addressed.''',
    d='''Which message best supports review? | The record says no known drug allergies; Rosa reports a past rash after an unnamed antibiotic. | Rosa has a confirmed allergy to every antibiotic. | The record is complete because the patient cannot remember a date. | Rosa is currently having the same reaction. | The accurate message preserves both sources and the limits of the reported history.
Which inference is unsupported? | The rash was definitely caused by an immune-mediated drug allergy. | A historical rash was reported. | The exact drug is not recalled. | The record and patient account differ. | Timing and a patient report alone do not establish the reaction's mechanism or cause.
What should happen to the unresolved information? | Keep it visible and route it for appropriate clinical clarification. | Delete it because it is incomplete. | Convert it to no known allergies without review. | Mark it resolved because a message was sent. | Incomplete information still matters and must not be silently removed or prematurely closed.
Which question seeks a useful missing detail without suggesting the answer? | Do you remember the medicine's name or have a prior record we can appropriately check? | It was definitely the same medicine as today's order, wasn't it? | Can I assume the rash was unrelated? | You meant stomach upset rather than a rash, correct? | The neutral question seeks identifying evidence without supplying an unsupported answer.''',
    dialogue='''Mei | Sam, I need a medication-safety review. Rosa's record says no known drug allergies, but she reports a rash after an antibiotic several years ago.
Sam | I have the [[discrepancy::The discrepancy is the difference between the recorded status and the patient's historical report.]]. Before we treat that field as settled, tell me exactly what Rosa said and which details you have not been able to establish.
Mei | She remembers a rash, but not the antibiotic name or the exact date. She is describing a past event; she has not reported a current reaction.
Sam | Keep that as the [[patient account::The patient account attributes the historical information to Rosa without making it a confirmed diagnosis.]]. We should not replace her words with a confirmed allergy diagnosis, but the missing details are not a reason to discard the report.
Mei | The old entry might have been copied forward. I cannot tell from this screen when somebody last checked it with her, so I should not call it verified.
Sam | Correct. We need to review the [[allergy status::Allergy status is the documented position that requires clarification when new information conflicts with it.]] and the relevant history. An existing field is useful information, not proof that every later report has already been assessed.
Mei | Should I say that the antibiotic caused the rash? Rosa remembers taking it before the rash, but she does not have a diagnosis or written explanation.
Sam | Describe the [[temporal association::Temporal association preserves the reported timing without claiming that causation has been established.]] without asserting the cause. We can say the rash followed an antibiotic in her account while leaving clinical interpretation to the appropriate review.
Mei | I can ask whether she remembers a product name or has a previous clinic record. I will not suggest a medicine and ask her to agree.
Sam | A [[corroborating record::A corroborating record may help identify the medicine or clarify the previous reaction history.]] could help. Use the appropriate access process and distinguish what the record actually says from what we still need to verify.
Mei | If she recalls only a brand, we need to confirm the actual medicine rather than assume that every similarly named product contains the same substance.
Sam | Verify the [[generic name::The generic name identifies the medicine's active substance rather than relying only on a remembered product brand.]] and any relevant product details. That clarification belongs with the clinical review, not a guess made to complete an empty field.
Mei | For now, the drug name and date remain unknown. I should not select no known allergies just because the software encourages a completed status.
Sam | Exactly. [[Unable to ascertain::Unable to ascertain describes information that cannot currently be established, not an absence of allergy history.]] and none known have different meanings. Follow our authorized documentation process while keeping the reported history and the unresolved details visible.
Mei | I will make clear that this is a historical report with no current reaction reported. That distinction should travel with the request, not disappear in the subject line.
Sam | I will take the [[pharmacist review::Pharmacist review is the professional assessment of the medication-related discrepancy, not a clerical status change.]] and coordinate any necessary clarification with the appropriate clinician. This exchange itself does not authorize a medicine choice or administration decision.
Mei | If the prescriber needs to clarify the order in light of the history, we should receive the actual response rather than infer it from silence.
Sam | We will request [[prescriber clarification::Prescriber clarification obtains the authorized prescribing professional's response to the medication question.]] through the correct route where needed. Record what was asked and what was answered, including any issue that remains open.
Mei | I will keep the discrepancy open until the relevant review is complete and the information is appropriately updated. Sending the request is not the final step.
Sam | Agreed. [[Record reconciliation::Record reconciliation addresses the documented difference through an authorized process rather than deleting one source.]] should reflect what the review establishes. Rosa's report, the old entry, and the eventual clarification each need an accurate place in that process.''',
    transfer_title='Unknown does not mean absent',
    transfer_setup='A patient remembers a previous reaction but cannot name the medicine. A new staff member proposes recording no known allergies solely because the name is unavailable.',
    transfer='''Nurse: "The medicine name is ___." | unknown | The patient's inability to name the medicine leaves that detail unestablished.
Colleague: "That does not prove the history is ___." | absent | Missing identification does not establish that no reaction history exists.
Nurse: "Preserve the patient's ___." | report | The supplied history should remain attributed and visible for appropriate review.
Colleague: "Route the discrepancy for qualified ___." | clarification | The unresolved difference requires appropriate review, not an unsupported negative entry.'''))

BOOK['units'].append(unit(
    title='Patient Education and Teach-Back',
    scene='A nod hides the wrong day',
    skill='Check understanding of supplied instructions, correct a misunderstanding without blame, and verify the corrected plan.',
    brief='In a role-play, nurse Leila reviews an approved discharge sheet with patient Victor. Its appointment section says Thursday at 10:30 a.m., reception B, and bring the current medication list. The printed clinic number is for appointment questions, not an emergency route. Victor nods, then says he will return Friday. Leila must check and clarify the supplied appointment details without adding medical instructions. Victor may use the sheet while explaining the plan in his own words.',
    cast='Leila | Nurse\nVictor | Patient',
    culture=('A nod is not a completed check', 'Nodding may show attention, politeness, or a wish not to interrupt. Invite the patient to describe the plan without making the exchange sound like an examination. Take responsibility for an unclear explanation and check the corrected detail again.'),
    a='''Which appointment details are supplied? | Thursday, 10:30 a.m., reception B | Friday, 10:30 a.m., reception B | Thursday, 3:30 p.m., reception A | Friday, 3:30 p.m., reception A | The approved sheet gives Thursday at ten thirty in the morning at reception B.
What does Victor's Friday answer reveal? | A misunderstanding that needs clarification | Deliberate refusal to attend | A confirmed change to the appointment | Proof that the written sheet is obsolete | The supplied facts show a mismatch in understanding, not refusal or a changed booking.
What is the printed clinic number for in this case? | Appointment questions | Any emergency instead of the applicable emergency route | Direct permission to change medication | Confirmation that no clinical follow-up is needed | The brief explicitly limits this number's stated purpose to appointment questions.''',
    vocabulary='''teach-back | Asking a person to explain information in their own words to check the explanation. | use teach-back
plain language | Familiar wording that communicates the intended meaning clearly. | explain in plain language
health literacy | The ability to find, understand, and use health information and services. | support health literacy
chunk and check | Giving small amounts of information and checking each part. | use chunk and check
discharge instructions | The approved information about the plan after leaving a care setting. | review discharge instructions
follow-up appointment | A planned later visit to continue review or care. | confirm the follow-up appointment
appointment window | A stated period for attending or arranging a visit. | clarify the appointment window
medication list | A record of medicines the person is using. | bring a current medication list
self-management | The person's role in carrying out an agreed care plan. | support self-management
caregiver involvement | Participation of a supporting person with appropriate permission. | confirm caregiver involvement
language access | Arrangements enabling meaningful communication across language differences. | arrange language access
qualified interpreter | A person with appropriate interpreting competence for the setting. | request a qualified interpreter
comprehension check | A focused check of what information has been understood. | make a comprehension check
misunderstanding | A difference between the intended meaning and the received meaning. | clarify a misunderstanding
rephrasing | Expressing the same meaning in different words. | try a clearer rephrasing
demonstration | Showing how a specified task is performed. | provide a demonstration
return demonstration | The learner showing a taught task back to the professional. | observe a return demonstration
action step | A specific part of the agreed plan to carry out. | identify the next action step
contact pathway | The appropriate route for a particular question or concern. | clarify the contact pathway
access barrier | A practical difficulty affecting use of information or services. | identify an access barrier
written reinforcement | Printed or digital information supporting the spoken explanation. | provide written reinforcement
nonjudgmental wording | Language that avoids blame or disparagement. | use nonjudgmental wording
understanding verified | A status supported by an actual check of the relevant information. | document understanding verified
education record | Documentation of information given and the person's demonstrated understanding. | update the education record''',
    precision='Teach-back checks how clearly information was explained. It is not a memory test or a request to repeat every word exactly. A person may consult the approved sheet while describing the plan. A yes answer alone does not verify understanding.',
    precision_extra='A return demonstration checks a practical task, while this case checks appointment information. Do not invent clinical instructions to make the exercise more detailed. Keep routine appointment contacts distinct from the appropriate route for urgent clinical concerns.',
    phrases='''Invite the plan | In your own words, when and where will you return?
Take responsibility | I may not have made the day clear.
Correct one detail | The appointment is Thursday, not Friday.
Point to the source | Let us look at the appointment line together.
Allow the reference | You can keep the sheet in front of you.
Clarify the time | Ten thirty here means 10:30 in the morning.
Check location | Which reception will you go to?
Confirm what to bring | Please bring the current medication list shown on the sheet.
Check again | Let us go over that part once more.
Avoid a memory test | I am checking my explanation, not testing your memory.
Invite questions | What would you like me to explain more clearly?
Separate contact purposes | This clinic number is for appointment questions.
Check practical access | Is there any difficulty reaching that reception at the agreed time?
Arrange language support | We can arrange appropriate language assistance.
Acknowledge the correction | Yes, that matches the appointment details on the sheet.
Record accurately | Document the corrected plan you actually checked with the patient.''',
    notes='''Do you understand? | A yes answer can conceal a misunderstanding; ask for the supplied plan in the patient's own words.
You got it wrong | Replace blame with a clear correction and responsibility for the explanation.
Repeat versus explain | Verbatim repetition may not show that the meaning is understood.
Current list | Current means the up-to-date list, not automatically any old printed version.
One number, one purpose | Do not broaden an appointment number into an emergency contact.
Check again | A correction is incomplete until the relevant point has been checked after rephrasing.''',
    d='''Which question checks the supplied information most effectively? | In your own words, when and where will you return, and what will you bring? | Do you understand everything? | You can read the sheet, can't you? | You will remember all of that, right? | The focused question requires the patient to explain the actual plan rather than simply agree.
Victor says Friday. Which response is best? | I may not have made the day clear; the sheet says Thursday. Let us check that part again. | You were nodding, so you must already know. | Friday is close enough to Thursday. | I will record understanding verified without asking again. | The response corrects the supplied detail without blame and includes another check.
Which entry is supported after Victor accurately restates the corrected details? | Appointment day, time, reception, and medication-list instruction checked through teach-back | All discharge information understood permanently | Patient will certainly attend regardless of barriers | No further questions can arise | The completed check supports the specific details verified, not unlimited claims about future behavior.
Victor asks whether the clinic number replaces urgent care routes. What preserves the brief? | No; its stated purpose here is appointment questions, and urgent concerns use the appropriate clinical route. | Yes, every number on a discharge sheet serves every purpose. | It proves no urgent concern can occur. | It authorizes changing treatment without review. | The supplied number has a limited appointment purpose and does not replace appropriate urgent attention.''',
    dialogue='''Leila | We have reached the appointment section on your discharge sheet. Before we finish, I would like to check that I have explained those details clearly.
Victor | I nodded because I was following most of it, but there were several details together. Could you go through the [[appointment::Appointment identifies the specific later visit being discussed, not the entire discharge plan.]] part once more?
Leila | Of course. The sheet says Thursday at ten thirty in the morning, at reception B. It also says to bring your current medication list.
Victor | I think I have it. I will return Friday at ten thirty and go to reception B with my [[medication list::The medication list is the supplied document Victor should bring to the visit.]].
Leila | I may not have made the day clear. It is Thursday, not Friday. Let us look at that line together so the spoken and written information match.
Victor | Yes, I see Thursday now. I connected it with a different appointment on Friday. Having the sheet in front of me helps with that [[detail::Detail refers to the particular day that Victor confused with another appointment.]].
Leila | Keep it there. I am not testing your memory. In your own words, when will you come back, and which reception will you use?
Victor | I will come on Thursday at ten thirty in the morning. I will go to [[reception B::Reception B is the location explicitly stated in the approved appointment instructions.]], rather than the desk where I first arrived today.
Leila | Yes, that matches the sheet. What will you bring with you for the appointment? You can look at the same line while you explain it.
Victor | I will bring my [[current::Current distinguishes the up-to-date medication list from an older version that may no longer be accurate.]] medication list. I have an older printed list at home, so I should not assume that old copy describes everything accurately now.
Leila | The instruction is to bring the current list. If you need help clarifying what you have, use the appropriate team contact rather than guess about medication changes.
Victor | Understood. I also see a clinic number. Is that the [[contact::Contact refers to the printed route for appointment questions, whose purpose must remain clear.]] for questions about this appointment, such as finding reception B?
Leila | Yes, that is the purpose identified in this section. It is not a replacement for the appropriate urgent clinical route if an urgent concern arises.
Victor | So I should not use the appointment number as a substitute for urgent help. Its stated purpose is [[appointment questions::Appointment questions is the limited purpose assigned to the printed clinic number in this scenario.]], not every possible concern after leaving.
Leila | Correct. Returning to this visit, is there any practical difficulty reaching reception B at the time shown? I can help clarify the location information available here.
Victor | I was not sure whether B meant the building or the desk. Could you explain the [[location::Location identifies Victor's remaining practical question about where to attend.]] on the clinic map rather than assume I know this site?
Leila | Certainly. We can check the clinic map together before you leave. I will not direct you from memory if the map or local arrangements need clarification.
Victor | Thank you. That would remove an [[access barrier::An access barrier is a practical difficulty, here uncertainty about finding the right reception.]] for me. The day is now clear, and the next thing I need is the exact way to that reception.
Leila | We will clarify that together. Then I will record the appointment details we checked, rather than write a broad statement that every discharge instruction is understood.
Victor | Let me give the [[plan::Plan summarizes the corrected appointment facts that Victor has now checked with Leila.]] once more: Thursday, ten thirty in the morning, reception B, with my current medication list. We will check the map before I leave.''',
    transfer_title='Correct the location, then check it',
    transfer_setup='An approved appointment note says Tuesday at 2 p.m., reception C. A patient correctly repeats the day and time but says reception A. The nurse clarifies only the location.',
    transfer='''Nurse: "The day and time match; let us clarify the ___." | location | The only mismatch in the supplied response concerns the reception.
Patient: "The note says reception ___." | C | The approved appointment note explicitly names reception C.
Nurse: "Please explain that corrected detail in your own ___." | words | Teach-back checks the person's understanding rather than asking only for agreement.
Patient: "I will use reception C on Tuesday at two in the ___." | afternoon | Two p.m. means two in the afternoon, preserving the supplied appointment time.'''))

BOOK['units'].append(unit(
    title='Interprofessional Rounds',
    scene='Walking the corridor is not testing the stairs',
    skill='Present a functional finding, challenge an overbroad discharge summary, and agree on the next professional review.',
    brief='During simulated rounds, nurse Omar sees a proposed noon discharge and a note saying "mobilizing well." Physiotherapist Eva reports a 40-meter corridor walk with a wheeled walker and supervision. Stairs were not assessed. The stated home access includes 12 steps and no elevator. Eva has not cleared stair use or independent mobility. The team needs the specific finding and unresolved access question; the language exercise does not decide fitness for discharge or prescribe a mobility technique.',
    cast='Omar | Nurse\nEva | Physiotherapist',
    culture=('Disagree with the inference, not the profession', 'Different disciplines bring different observations to rounds. A functional concern is not automatically an objection to efficient discharge planning. Name the assessed task, the conditions, and the unassessed task so the team can decide from a shared picture rather than a vague label.'),
    a='''What was actually assessed? | A 40-meter corridor walk with a wheeled walker and supervision | Independent stair climbing | Twelve steps without equipment | All activities required at home | The supplied assessment concerns a corridor walk under stated equipment and supervision conditions.
What remains unresolved? | Stair access to the stated home setting | Whether the home has any steps | Whether a corridor walk occurred | Whether the proposed time is noon | The home has twelve steps, but the relevant stair task has not been assessed.
What is the team's immediate communication need? | A precise finding and a clear unresolved question for the appropriate review | A guarantee that noon discharge is safe | A mobility technique invented from the dialogue | Removal of the supervision condition to shorten the note | The case calls for accurate shared information before the qualified discharge decision.''',
    vocabulary='''interprofessional rounds | A care discussion involving professionals from different disciplines. | contribute to interprofessional rounds
functional assessment | Evaluation of how a person performs relevant practical tasks. | report a functional assessment
ambulation | Walking or moving about on foot. | describe observed ambulation
gait | The pattern of walking. | assess gait
mobility aid | Equipment used to support movement. | specify the mobility aid
wheeled walker | A walking support with wheels. | use a wheeled walker
supervision | Oversight without assuming the same meaning as physical assistance. | document required supervision
physical assistance | Hands-on help provided during a task. | specify physical assistance
independent mobility | Movement without another person's assistance or supervision for the stated task. | verify independent mobility
transfer ability | Capacity to move between positions or surfaces. | assess transfer ability
stair negotiation | Managing ascent or descent of steps. | assess stair negotiation
activity tolerance | Capacity to sustain a specified activity. | describe activity tolerance
home environment | The physical and practical conditions in the person's home setting. | assess the home environment
access requirement | A condition that must be met to enter or use a setting. | clarify access requirements
discharge readiness | Whether relevant conditions for leaving the care setting have been met. | review discharge readiness
discharge destination | The setting to which a person is expected to leave. | confirm the discharge destination
equipment provision | Arranging necessary equipment through the appropriate process. | verify equipment provision
functional limitation | A restriction in performing a specified task. | describe a functional limitation
unassessed task | A relevant activity not yet evaluated. | identify an unassessed task
discipline-specific finding | An observation within a professional field's assessment. | share discipline-specific findings
shared goal | An agreed outcome supported by the care team and patient. | establish a shared goal
discharge barrier | An unresolved issue relevant to a proposed departure. | communicate a discharge barrier
therapy recommendation | Advice from the relevant therapy assessment. | clarify the therapy recommendation
team decision | A conclusion reached through the appropriate care-team process. | record the team decision''',
    precision='A distance alone does not describe functional performance. Include the aid, assistance or supervision, setting, and assessed task. A corridor walk does not establish stair ability. Not assessed is different from assessed and unable; preserve that distinction.',
    precision_extra='Physiotherapist and physical therapist are common regional titles. Assistance labels vary across settings, so use the local definitions. A proposed departure time does not override unresolved clinical or functional questions, and a language exercise cannot supply a discharge clearance.',
    phrases='''State the finding | Eva observed a 40-meter corridor walk.
Include the conditions | The walk used a wheeled walker and required supervision.
Name the gap | Stairs have not been assessed.
Clarify the home | The stated home access has twelve steps and no elevator.
Challenge the summary | Mobilizing well is too broad for the finding we have.
Avoid a false negative | Not assessed does not mean unable.
Avoid a false positive | Corridor performance does not establish stair safety.
Preserve professional scope | The relevant qualified team must review the discharge implications.
Separate timing from readiness | Noon is a proposed time, not evidence that the conditions are met.
Invite the next review | What assessment is needed to address the stair-access question?
State a shared goal | We want a workable plan that reflects the actual home setting.
Check equipment | Confirm the equipment arrangements rather than assume they are complete.
Make the concern specific | My concern is the unassessed task required at the destination.
Prevent overstatement | Please retain the supervision condition in the summary.
Clarify the record | Record the observed task separately from the outstanding assessment.
Close rounds accurately | The discharge decision remains with the appropriate clinical process.''',
    notes='''Mobilizing well | Too vague without the task, conditions, and relevant limits.
Independent | Do not use this term when supervision was required in the supplied assessment.
Not assessed | A statement about evidence, not a prediction of success or failure.
Cleared | Specify who made which decision and on what basis.
Home today | A proposed destination and date are not a completed readiness assessment.
Common goal | Shared discharge planning can include respectful disagreement about missing evidence.''',
    d='''Which summary is most accurate? | Walked 40 meters with a wheeled walker and supervision; stairs not assessed. | Independently mobile in all home activities. | Unable to climb stairs, as demonstrated today. | Cleared for twelve steps because the corridor distance was longer. | The accurate statement preserves the assessed task and its conditions without inventing stair findings.
Why does the home information matter? | The destination requires a task that the corridor assessment did not establish. | Twelve steps are always equivalent to forty meters of walking. | An elevator was confirmed available. | Home access never affects discharge planning. | The home requires stair access, which remains distinct from the assessed corridor walk.
How should Omar respond to pressure for a noon summary? | Report the specific assessment and unresolved stair question for the qualified team. | Remove supervision to make the note more decisive. | Convert not assessed to safe. | Treat the proposed time as the assessment result. | Accurate reporting allows the appropriate team to address the actual gap despite scheduling pressure.
Which statement incorrectly treats missing evidence as a negative finding? | Eva established that the patient cannot use stairs. | Eva has not assessed stairs. | The corridor walk required supervision. | The home access includes twelve steps. | The supplied facts state no stair assessment, not a demonstrated inability to use stairs.''',
    dialogue='''Omar | The proposed departure time is noon, and the rounds note says mobilizing well. Before I repeat that to the team, can you tell me exactly what you assessed?
Eva | My [[functional assessment::Functional assessment concerns the specific task and conditions actually evaluated, not a general clearance.]] included a forty-meter corridor walk. The patient used a wheeled walker and required supervision. Stairs were not part of that assessment.
Omar | The home information says twelve steps and no elevator. I was about to describe the patient as independently mobile, but that would leave out your conditions.
Eva | Please retain [[supervision::Supervision was required during the observed walk, so independent mobility would overstate the finding.]]. The distance alone does not establish independence. The equipment, setting, and level of support are part of the finding, not optional details.
Omar | Some colleagues may hear that as a general objection to discharge. I need to make the unresolved point specific, so rounds can address it efficiently.
Eva | The unresolved question is [[stair negotiation::Stair negotiation is the unassessed task required by the stated access to the home.]] in relation to the stated home access. I am not saying the patient failed a stair assessment; I am saying it has not occurred.
Omar | That distinction matters. If I write unable to manage steps, I would be turning an absence of assessment into a result that you never reported.
Eva | Correct. It is an [[unassessed task::An unassessed task lacks an evaluation; that is different from a demonstrated inability.]]. Neither safe on stairs nor unable on stairs follows from the corridor walk. We need the relevant professional review.
Omar | I will tell the team that the home access requires twelve steps. The proposed noon time should be discussed alongside that fact rather than erase it.
Eva | The [[home environment::The home environment supplies practical conditions that the discharge plan must address.]] gives the assessment its practical context. A finding can be accurate for this corridor and still leave a question about the destination unanswered.
Omar | We also need to avoid assuming the walker arrangements are complete. The assessment tells us what was used here, not what has been arranged elsewhere.
Eva | Yes, [[equipment provision::Equipment provision concerns actual arrangements for equipment, not merely its use during an assessment.]] is a separate status to verify through the appropriate team. We should not turn observed use into confirmation that every arrangement is finished.
Omar | How should I summarize this at rounds without asking everyone to read a long therapy note? I want one concise statement and the unresolved question.
Eva | State the observed walk and support, then the stair question affecting [[discharge readiness::Discharge readiness concerns the relevant conditions for leaving, not the proposed departure time alone.]]. Keep the decision with the appropriate clinical process rather than presenting my observation as complete clearance.
Omar | I can say: forty meters with a wheeled walker and supervision; stairs not assessed; home access includes twelve steps without an elevator. The stair question needs review.
Eva | That is accurate. Our [[shared goal::A shared goal allows the team to coordinate a workable plan without concealing unresolved evidence.]] is a workable plan for the actual destination, not simply a shorter note or an argument about which discipline controls the schedule.
Omar | If the team changes the destination or obtains another assessment, we should update the summary from those actual facts rather than predict the result now.
Eva | Exactly. Confirm the [[discharge destination::The discharge destination identifies the actual setting whose access and support requirements need consideration.]] and relevant findings as they are established. A different setting may raise different questions, but we cannot invent that change in advance.
Omar | I will replace mobilizing well with the specific finding and bring the outstanding question to rounds. Noon remains proposed, not clinically confirmed by this exchange.
Eva | Thank you. Record the eventual [[team decision::The team decision must reflect the appropriate review rather than an inference from a vague mobility summary.]] through the appropriate process, including any conditions. My contribution is the assessment actually performed and the limit of what it establishes.''',
    transfer_title='Measured distance, untested task',
    transfer_setup='A therapist observes a 25-meter indoor walk with assistance. Outdoor uneven ground has not been assessed. A summary incorrectly calls the person independent outdoors.',
    transfer='''Therapist: "The observed walk was ___." | indoors | The supplied assessment took place indoors, not on outdoor ground.
Nurse: "It required ___." | assistance | The briefing explicitly includes assistance as a condition of the observed walk.
Therapist: "Uneven outdoor ground is ___." | unassessed | No assessment of that separate task is supplied in this case.
Nurse: "The summary must not claim outdoor ___." | independence | An assisted indoor walk does not establish independent outdoor performance.'''))

BOOK['units'].append(unit(
    title='Documentation and Charting',
    scene='Replace the label with the observable facts',
    skill='Select an objective, attributed clinical note and distinguish event time, entry time, and a later correction.',
    brief='In a documentation simulation, nurse Elena drafts "Patient difficult and refusing all care." At 2:20 p.m., the patient said, "I want to rest before washing." Elena offered to return at 3 p.m.; the patient agreed. No other care was discussed. Elena enters the note at 2:45 p.m. Supervisor Chris reviews its wording. No capacity assessment, diagnosis, or explanation beyond the quoted request is supplied.',
    cast='Elena | Nurse\nChris | Supervisor',
    culture=('A useful note can be both precise and respectful', 'Labels may feel efficient, but they can hide the event that the next clinician needs to understand. Record observable behavior, attributed words, relevant actions, and timing. Neutral wording does not require deleting a difficult interaction; it requires describing it accurately.'),
    a='''What did the patient actually request? | Rest before washing | Refusal of every type of care | Permanent cancellation of all support | A confirmed change in diagnosis | The supplied quotation concerns the timing of washing, not every aspect of care.
Which times need to be distinguished? | Event at 2:20 p.m. and entry at 2:45 p.m. | Event and entry both at 3 p.m. | Event at 2:45 p.m. and entry at 2:20 p.m. | Only the computer's current date | The briefing gives separate times for the interaction and documentation.
What was agreed? | Elena would return at 3 p.m. | The patient had already washed at 3 p.m. | No further contact would occur | Every future care offer would be declined | The agreement is a future return time, not a completed care event.''',
    vocabulary='''objective documentation | Recording observable or verifiable information without unsupported judgment. | use objective documentation
subjective report | Information about an experience described by the person. | attribute a subjective report
direct quotation | The person's exact words identified as a quote. | include a relevant direct quotation
behavioral description | A factual account of what a person said or did. | provide a behavioral description
clinical inference | A professional interpretation distinguished from the underlying facts. | separate clinical inference from observation
event time | The time the described action or observation occurred. | record the event time
entry time | The time the documentation is entered. | preserve the entry time
late entry | A later record of an earlier event, identified according to local procedure. | identify a late entry
addendum | Additional information appended to an existing record. | make an authorized addendum
amendment | A documented correction or change made through the approved process. | request an amendment
audit trail | A record showing relevant entries, changes, authors, and times. | preserve the audit trail
record integrity | The reliability and traceability of documented information. | protect record integrity
copy-forward | Reusing earlier text in a later record. | verify copy-forward content
template text | Preset wording inserted into a record. | review template text
autopopulated field | A field filled automatically from another source. | verify autopopulated fields
author attribution | Identification of the person responsible for an entry. | maintain author attribution
contemporaneous note | Documentation made at or close to the relevant event. | make a contemporaneous note
factual correction | A change that corrects an inaccurate statement. | document a factual correction
care declined | A specific offered action that the person did not accept. | specify the care declined
agreed follow-up | The next contact or action actually agreed with the person. | record agreed follow-up
capacity assessment | A qualified assessment of decision-making ability under applicable criteria. | document a capacity assessment accurately
informed refusal | Declining an intervention after the relevant information and process. | distinguish an informed refusal
approved abbreviation | A shortened form permitted and understood in the local documentation system. | use approved abbreviations
documentation scope | The limits of what an entry can support from the available evidence. | keep within documentation scope''',
    precision='The quoted request supports a preference about timing, not refusal of all care or a capacity finding. Record the offered return and the agreement. Do not document a planned action as completed before it occurs.',
    precision_extra='Event time and entry time answer different questions. Follow local rules for delayed entries and corrections; never disguise when a note was entered. A preserved audit trail is compatible with correcting an inaccurate statement through the authorized process.',
    phrases='''Replace the label | Describe what was said and what you observed.
Attribute the words | The patient said, "I want to rest before washing."
Limit the claim | No other care was discussed in this interaction.
Record the offer | I offered to return at 3 p.m.
Record agreement | The patient agreed to that return time.
Separate the times | The event occurred at 2:20; this entry is being made at 2:45.
Avoid an inferred motive | The record does not establish why the patient wanted to rest beyond the stated request.
Keep plans prospective | A planned return is not a completed visit.
Check copied wording | That phrase came from an earlier note and needs verification.
Preserve the author | Attribute the entry to the person making it.
Correct transparently | Use the approved amendment process rather than conceal the earlier entry.
Avoid overreach | This interaction does not establish a capacity assessment.
Use relevant detail | Include the facts needed for the next person's follow-up.
Clarify an abbreviation | Use the approved term where a shortened form could be misunderstood.
Check the final note | Does every statement have a source in the supplied facts?
Close accurately | Record the later return only after its actual outcome is known.''',
    notes='''Difficult | A label that does not identify an observable action.
Refusing all care | Far broader than a request to postpone one task.
Patient stated | Attributes the account rather than presenting it as your independent finding.
Agreed versus completed | An agreement concerns a plan; completion concerns an event that occurred.
Backdating | Do not disguise the actual time of entry.
Correction versus concealment | Correct errors through the approved process while preserving appropriate traceability.''',
    d='''Which replacement note best matches the event? | At 2:20, patient said, "I want to rest before washing." Return at 3 offered and agreed. | Patient refused all clinical care throughout the day. | Patient lacked capacity because washing was postponed. | Patient was uncooperative for reasons not recorded. | The replacement preserves the quotation, timing, offer, and agreement without adding unsupported judgments.
Which claim is not supported? | The patient refused every type of care. | The patient requested rest before washing. | Elena offered to return at three. | The entry was made after the event. | The brief explicitly says no other care was discussed, so the universal refusal claim is unjustified.
How should the two times be handled? | Identify the event time and preserve the actual entry time under local procedure. | Change the entry time to make it appear contemporaneous. | Omit the event time and assume readers will infer it. | Record the event at three because that was the planned return. | The two times describe different events and should not be conflated or concealed.
At 2:45, which follow-up statement is accurate? | Return at 3 p.m. agreed; outcome not yet recorded. | Returned at 3 and completed washing. | Patient later refused the visit. | All subsequent care was accepted. | The future return has been agreed but its actual outcome is not yet known.''',
    dialogue='''Elena | My draft says the patient was difficult and refusing all care. Reading it back, I can see that it does not explain what happened during the interaction.
Chris | Start with a [[behavioral description::A behavioral description identifies what was said or done instead of relying on a judgmental label.]]. What did the patient actually say, what did you offer, and which part of care was discussed?
Elena | At two twenty, the patient said, "I want to rest before washing." I offered to return at three, and the patient agreed to that time.
Chris | That [[direct quotation::The direct quotation preserves the patient's actual words and the limited request they express.]] is useful because it states the request precisely. It does not support a claim that every kind of care was refused.
Elena | No other care was discussed. I should not make the note broader just because the original template gave me a short phrase about noncompliance.
Chris | Correct. Review the [[template text::Template text is preset wording that must still match the facts of the individual interaction.]] rather than let it determine the event. A convenient field does not justify recording something that the interaction did not establish.
Elena | I am entering the note at two forty-five. The conversation happened at two twenty, so those times describe different things even though they are close together.
Chris | Preserve the [[event time::Event time identifies when the patient interaction occurred, distinct from when the note was entered.]] and the actual entry time according to our documentation procedure. Do not make the entry appear to have been written earlier than it was.
Elena | I also wrote that I returned at three, but that is still in the future. I meant that I had arranged to return then.
Chris | Record it as [[agreed follow-up::Agreed follow-up is the accepted future plan, not evidence that the later visit has occurred.]]. The patient agreed to your offer, but the outcome of that future visit cannot be documented as complete now.
Elena | Should I include a reason such as the patient being anxious? I thought that might explain why the patient wanted to delay washing.
Chris | Only add a supported [[clinical inference::A clinical inference must be distinguished from observed facts and cannot be invented to explain the event.]] within your role, clearly distinguished from the facts. The account supports a request for rest, not an established finding of anxiety or another explanation.
Elena | The phrase refusing all care may already have been saved in the draft record. I should check its status rather than silently assume nobody could have seen it.
Chris | Follow the authorized [[amendment::An amendment corrects a record through the approved process without concealing the original history.]] process if a saved entry needs correction. Keep the change traceable and do not obscure the original entry or its author.
Elena | So I should not delete the history merely to make the final record look as though the inaccurate wording never existed.
Chris | Preserve the [[audit trail::The audit trail provides traceability of entries and changes, supporting reliable correction rather than concealment.]] in the appropriate system. Transparent correction helps a later reader understand what was changed and why the current wording is more accurate.
Elena | The final note can state the quotation, the offer to return, and the agreement. It should not imply a formal decision about capacity or informed refusal.
Chris | That respects the [[documentation scope::Documentation scope limits the entry to what the supplied evidence and relevant professional process actually support.]]. Those are distinct clinical and procedural matters, and the facts here do not establish that either assessment occurred.
Elena | I will check each sentence against the actual interaction. At three, the next entry will describe what really happens, including any further agreement or change.
Chris | Good. [[Objective documentation::Objective documentation records supported facts and attributed information without the unsupported label in the original draft.]] can remain respectful without losing detail. The next clinician should understand the specific request and follow-up, rather than inherit a label about the patient.''',
    transfer_title='A plan entered as an event',
    transfer_setup='At 11 a.m., a note says "Education completed at noon." The only supplied fact is an agreement to return at noon for education. The noon visit has not occurred.',
    transfer='''Reviewer: "Noon is still in the ___." | future | At eleven, the agreed noon visit has not yet occurred.
Author: "The visit is ___, not completed." | planned | The supplied fact is an agreement to return, not a completed education session.
Reviewer: "Correct the statement through the approved ___." | process | An inaccurate entry should be corrected transparently under the applicable documentation procedure.
Author: "The later entry must reflect the actual ___." | outcome | The result of the visit can be documented only after it is known.'''))

BOOK['units'].append(unit(
    title='Difficult Families and Boundaries',
    scene='Acknowledge the frustration; keep the boundary',
    skill='Respond to a family member with empathy, accurate limits, and a concrete next contact without promising another clinician.',
    brief='In a simulation, family member Anika says, "Nobody tells us anything," and asks nurse Luis to explain a test result. The patient has agreed to include Anika in relevant updates; that permission does not authorize Luis to invent an interpretation. Luis can contact the responsible clinician and return with a status update by 4 p.m. No clinician meeting time is confirmed. Anika is frustrated but is not making threats. Urgent clinical concerns would follow the appropriate separate route.',
    cast='Anika | Family member\nLuis | Nurse',
    culture=('Boundaries should still offer a way forward', 'A boundary can sound dismissive when it ends the conversation without an alternative. Acknowledge the specific concern, explain what you can do, and state the next contact. Do not describe every frustrated family member as aggressive or confuse a firm request with a threat.'),
    a='''What permission is supplied? | The patient has agreed to include Anika in relevant updates. | Anika can make every decision for the patient. | Luis can interpret any result without the appropriate role. | Every relative may receive all records. | The permission concerns relevant updates to Anika, not unlimited authority or disclosure.
What can Luis promise? | His own status update by 4 p.m. | A clinician meeting at exactly 4 p.m. | A reassuring interpretation of the result | Completion of every unresolved issue by four | The brief gives Luis control of his update, not the clinician's schedule or clinical conclusion.
How is Anika's behavior described? | Frustrated, without threats | Physically threatening | Calm and satisfied | A confirmed reason to end all communication | The supplied facts identify frustration but explicitly state that no threats are being made.''',
    vocabulary='''family liaison | Communication connecting family members with the care team. | coordinate family liaison
patient preference | The person's expressed choice relevant to their care or communication. | respect patient preferences
permission to share | An appropriate basis allowing specified information to be communicated. | verify permission to share
confidentiality | Protection of information from inappropriate access or disclosure. | maintain confidentiality
authorized recipient | A person appropriately entitled to receive the relevant information. | confirm the authorized recipient
professional boundary | A limit that keeps actions and communication within an appropriate role. | maintain a professional boundary
scope of practice | The professional activities permitted by role, competence, and applicable rules. | work within scope of practice
empathic acknowledgment | Recognition of a person's concern or experience without unsupported agreement. | offer empathic acknowledgment
validation | Recognition that an expressed feeling or concern has been heard. | provide appropriate validation
de-escalation | Communication or action intended to reduce tension and support safety. | use de-escalation skills
active listening | Attentive listening that checks the speaker's meaning. | demonstrate active listening
clarifying question | A question used to establish the specific concern or missing detail. | ask a clarifying question
family meeting | An arranged discussion involving appropriate relatives and care professionals. | request a family meeting
clinical explanation | Interpretation of clinical information by an appropriately qualified professional. | arrange a clinical explanation
status update | Information about what has happened and what remains pending. | provide a status update
update commitment | A specific promise to communicate again at an agreed point. | honor the update commitment
named contact | The identified person responsible for the next communication. | provide a named contact
expectation management | Clear communication about what can and cannot currently be promised. | improve expectation management
complaint pathway | The designated route for raising and reviewing service concerns. | explain the complaint pathway
shared decision-making | A process combining relevant evidence with the patient's values and preferences. | support shared decision-making
substitute decision-maker | A person with applicable authority to decide in specified circumstances. | verify substitute decision-maker authority
consent discussion | A relevant exchange supporting an appropriately informed decision. | arrange a consent discussion
communication preference | A stated choice about how or with whom information is shared. | record communication preferences
safety boundary | A limit or action needed to protect people from actual risk. | apply an appropriate safety boundary''',
    precision='Permission to include a relative in updates is not automatically authority to decide for the patient. A nurse can acknowledge frustration without confirming an unsupported allegation. A status update promises communication; a clinical explanation requires the appropriate professional involvement.',
    precision_extra='Frustration, assertiveness, threats, and violence are not interchangeable labels. Respond to the actual behavior and local safety procedures. This scenario supplies no threat; it calls for listening, accurate boundaries, and reliable follow-through rather than punitive language.',
    phrases='''Acknowledge the experience | You have been waiting for a clear explanation, and that is frustrating.
Clarify the concern | Which question has not yet been answered?
Confirm participation | The patient has agreed that you can be included in these updates.
Keep the role clear | I can explain the next step, but I cannot invent an interpretation of the result.
Arrange the right discussion | I will contact the responsible clinician about that question.
Promise what you control | I will return with a status update by 4 p.m.
Separate the appointment | Four is my update time, not a confirmed meeting with the clinician.
Avoid unsupported reassurance | I cannot tell you the result is normal from the information we have here.
Keep listening | Let me check that I have understood your main concern.
Avoid defensiveness | I want to address the missing explanation rather than argue about your frustration.
Clarify authority | Being included in updates does not by itself determine decision-making authority.
Name the next contact | I will be your contact for this promised update.
Explain delay honestly | The meeting time is still unconfirmed, and I will tell you what I have established.
Offer the formal route | I can explain how to raise the communication concern through the appropriate pathway.
Protect urgent response | A new urgent clinical concern needs the appropriate clinical route immediately.
Close with the commitment | I will update you by four even if the meeting time remains pending.''',
    notes='''I understand | Name what you understand rather than use the phrase as a substitute for listening.
Nobody | A frustrated absolute can be acknowledged without debating every previous contact.
I promise | Restrict the promise to an action you can actually control.
Normal | Do not use this as reassurance without an established clinical basis.
Included versus authorized to decide | These are different permissions and responsibilities.
Difficult family | Describe the actual communication issue rather than treating the label as an assessment.''',
    d='''Which opening best acknowledges the concern? | You have been waiting for a clear explanation; let me check the unanswered question and arrange the right contact. | You are wrong because staff have spoken today. | Calm down before anyone tells you anything. | Every test result is probably fine. | The opening recognizes the missing explanation and moves toward an appropriate response without unsupported reassurance.
Anika asks, "Will the clinician be here at four?" What is accurate? | Four is my promised status update; a clinician meeting time is not yet confirmed. | Yes, my update promise guarantees the clinician's attendance. | No clinician will ever attend because no time is booked now. | Four means the result will definitely be normal. | The brief distinguishes Luis's own update from an unconfirmed clinician meeting.
What should Luis avoid inferring from permission to share updates? | That Anika automatically has full decision-making authority | That relevant updates may include Anika | That patient preferences matter | That the result question needs the right clinical professional | Being included in communication does not itself confer authority to make every decision.
At four, no meeting time is confirmed. What honors the commitment? | Give Anika the current status and a clear next communication step. | Say nothing until a meeting can be guaranteed. | Invent a meeting time to reduce frustration. | Mark the concern resolved because a message was sent. | Luis promised an update, so honest communication remains due even while the meeting is pending.''',
    dialogue='''Anika | Nobody tells us anything. We keep hearing that someone will explain the result, but we still do not know who that person is or when we will hear.
Luis | You have been waiting for a [[clear explanation::Clear explanation identifies the unmet communication need Luis is acknowledging rather than dismissing.]], and I can hear how frustrating that is. Let me check which question you most need answered.
Anika | I want to know what the test result means for my father. I do not want another message saying that somebody has passed the request to somebody else.
Luis | The patient has agreed to include you in these [[updates::Updates are the relevant communications the patient has permitted Anika to receive in this case.]]. I can contact the responsible clinician with that question, but I should not invent a clinical interpretation.
Anika | Does that mean you cannot tell me anything? I am not asking for a lecture about whose job it is. I need a practical next step.
Luis | The next step is for me to contact the [[responsible clinician::The responsible clinician is the appropriate contact for the clinical explanation sought in this scenario.]] and confirm the response arrangements. I will stay responsible for the update I promise you.
Anika | All right, but what exactly are you promising? Earlier I heard soon, and soon turned into several hours without a clear answer.
Luis | I will give you a [[status update::A status update reports what has been established and what remains pending, not necessarily a completed clinical explanation.]] by four this afternoon. That will include what I have confirmed and anything still awaiting a response.
Anika | So the clinician will meet us at four? I can ask my sister to come then if that is a firm time.
Luis | Four is my [[update time::Update time identifies Luis's own communication commitment, not a clinician meeting that has not been arranged.]], not a confirmed clinician meeting. I do not want you to rearrange the family around an appointment that has not been agreed.
Anika | Thank you for making that distinction. I am still worried. Can you at least say the result is probably normal because nobody has come urgently?
Luis | I cannot give that [[reassurance::Reassurance about a normal result would lack a clinical basis in the facts supplied here.]] from silence or timing. The result needs the appropriate clinical explanation, and I will carry that specific question to the responsible team.
Anika | I also want them to know that the lack of communication has made this harder. I should not have to become upset before somebody gives a clear answer.
Luis | I will include that [[concern::Concern refers to Anika's complaint about the communication experience, which can be passed on accurately.]] accurately. If you want it reviewed through the formal communication-complaint route, I can explain that process as well.
Anika | I would like the explanation arranged first. Since my father agreed to include me, does that also mean I can make all the decisions for him?
Luis | Inclusion in updates does not by itself establish [[decision-making authority::Decision-making authority is distinct from permission to receive relevant information and requires the applicable basis.]]. His preferences and the applicable decision process still matter. We should clarify any specific decision with the appropriate team.
Anika | That is fair. My immediate request is the result discussion and a reliable contact. I do not want to start the whole explanation again with every shift.
Luis | I will be the [[named contact::The named contact is the identified person accountable for this promised follow-up communication.]] for this promised update and document the concern and next step appropriately. The team should receive the question you have already explained.
Anika | If the meeting time is still unknown at four, please tell me that directly. Waiting without knowing whether the request was received is the hardest part.
Luis | I will keep that [[commitment::Commitment refers to the promised update Luis can control even if the meeting remains unconfirmed.]]. You will hear the current status from me by four, with the next communication step, rather than an invented answer or an unconfirmed appointment.''',
    transfer_title='An update is not a meeting',
    transfer_setup='A therapist promises a family a 5 p.m. update about arranging a care conference. The conference time remains unconfirmed. The patient has agreed to the relevant family involvement.',
    transfer='''Family member: "Is five the conference ___?" | time | The question asks whether the update time also establishes a conference appointment.
Therapist: "Five is my ___; the conference is not yet booked." | update | The only confirmed promise concerns the therapist's communication.
Family member: "Please explain the current ___ even if it is pending." | status | The family requests accurate information about arrangements, not an invented booking.
Therapist: "I will keep my communication ___." | commitment | The update can still be delivered even when another person's meeting is unconfirmed.'''))

BOOK['units'].append(unit(
    title='Safety Events and Just Culture',
    scene='Report the fall without inventing its cause',
    skill='Separate an event chronology from causal assumptions and select a follow-up measure tied to the identified risk.',
    brief='In a simulated safety review, a patient fall is recorded at 11:05 a.m. Immediate clinical response has followed local procedure; the review does not replace it. Nurse Beth did not witness the fall. The patient later reported standing to reach water. A draft says a colleague was careless and the call bell was out of reach, but neither claim is established. Safety lead Arun asks for the sources, sequence, and unresolved environmental details before conclusions or corrective actions are assigned.',
    cast='Beth | Nurse\nArun | Safety lead',
    culture=('Fair review is not automatic blame or automatic absolution', 'An event deserves a careful account of actions, context, and system conditions. A fair learning culture makes it possible to report concerns while retaining appropriate accountability. It does not establish a cause from an outcome or promise that every action is beyond review.'),
    a='''Which event is supplied as recorded? | A fall at 11:05 a.m. | A proven act of carelessness | A verified unreachable call bell | A completed causal investigation | The briefing establishes the recorded fall and time, not the draft's causal claims.
What is the source of the water detail? | The patient's later report | Beth's eyewitness account | A confirmed equipment log | A completed staff investigation | The patient reported standing to reach water; Beth did not witness the event.
What is the purpose of this review? | Reconstruct supported facts and unresolved details before conclusions | Replace the immediate clinical response | Assign blame from the outcome alone | Mark every suggested cause as verified | The review follows the clinical response and seeks evidence before causal conclusions.''',
    vocabulary='''patient safety event | An occurrence relevant to possible or actual harm during care. | report a patient safety event
event chronology | The ordered sequence of known events and times. | reconstruct the event chronology
firsthand observation | Information directly witnessed by the person reporting it. | distinguish firsthand observation
secondhand account | Information received from another person rather than directly witnessed. | attribute a secondhand account
contributing factor | A condition or action that helped an event occur. | investigate contributing factors
causal assumption | An explanation treated as true before sufficient support is established. | challenge a causal assumption
hindsight bias | Judging earlier actions as obviously wrong because the outcome is now known. | avoid hindsight bias
outcome bias | Judging a decision mainly by its result rather than the information available then. | recognize outcome bias
just culture | A fair approach combining learning from systems with appropriate individual accountability. | support a just culture
psychological safety | A climate in which people can raise concerns without interpersonal intimidation. | strengthen psychological safety
human factors | Study of interactions between people, tasks, equipment, and working conditions. | apply human-factors analysis
systems approach | Review of how connected processes and conditions affect performance. | use a systems approach
environmental condition | A relevant physical feature of the setting. | verify environmental conditions
call-bell access | Whether the patient can reach and use the assistance-call device. | check call-bell access
immediate response | Actions taken promptly to address the situation and possible harm. | document the immediate response
incident report | The formal record submitted through a safety-reporting process. | complete an incident report
clinical record | The care documentation concerning the individual patient. | maintain the clinical record
evidence preservation | Protecting relevant records or information for accurate review. | support evidence preservation
root cause analysis | A structured investigation of underlying and contributing causes. | contribute to root cause analysis
corrective action | A change intended to address an identified problem or cause. | assign a corrective action
action owner | The named person responsible for carrying out an agreed action. | name the action owner
effectiveness measure | A way to check whether an action achieved its intended result. | define an effectiveness measure
balancing measure | A check for unintended effects of a change. | include a balancing measure
learning feedback | Information returned to staff about findings and improvements. | provide learning feedback''',
    precision='A fall is an event; carelessness is an interpretation that requires evidence. Attribute the patient\'s account and distinguish it from firsthand observation. Absence of a witness does not make the report irrelevant, but it limits what the reporter can personally verify.',
    precision_extra='An incident report and a clinical record serve different purposes; follow local requirements for both. A completed training session shows delivery, not necessarily reduced risk. Match follow-up measures to the actual finding and monitor unintended effects.',
    phrases='''State the event | A fall was recorded at 11:05 a.m.
Attribute the account | The patient later reported standing to reach water.
Limit firsthand knowledge | I did not witness the fall.
Challenge the inference | The draft does not establish that the colleague was careless.
Name the unknown | The call-bell position at the time has not been verified.
Preserve the sequence | Separate what happened before, during, and after the event.
Respect the clinical response | The safety review does not replace immediate patient assessment and care.
Seek relevant evidence | Which records or accounts can clarify the conditions at that time?
Avoid hindsight | Evaluate what was known then, not only what became clear afterward.
Keep accountability fair | Review actions and system conditions without prejudging the outcome.
Match the action | Which identified factor would this proposed change address?
Name an owner | Assign the agreed action to a specific responsible person.
Distinguish delivery | Attendance confirms the briefing occurred, not that risk decreased.
Check effectiveness | Measure whether the intended condition actually improved.
Watch for trade-offs | Include a check for unintended delays or workarounds.
Return the learning | Share the supported findings and next steps through the appropriate process.''',
    notes='''Caused by | Requires more support than a sequence or an assumption.
Patient reported | Attributes information without claiming you witnessed it.
No blame | A fair review is not a promise that conduct will never be examined.
Root cause | Avoid using the phrase as a shortcut for the first explanation suggested.
Completed training | Describes an activity, not automatically its practical effect.
Resolved | Use only when the defined problem and follow-up criteria have actually been addressed.''',
    d='''Which opening gives the strongest factual foundation? | A fall was recorded at 11:05; I did not witness it; the patient later reported standing to reach water. | A careless colleague caused the fall. | The call bell was definitely unreachable because a fall occurred. | Every system failed at exactly the same time. | The factual opening identifies the event, the limit of firsthand knowledge, and the source of the account.
Which statement needs verification before being presented as fact? | The call bell was out of reach at the time. | Beth did not witness the fall. | The patient later reported standing for water. | A fall is recorded at eleven oh five. | The briefing explicitly says the call-bell position has not been established.
A later review identifies inconsistent call-bell positioning. Which measure tests a related improvement? | A defined audit of whether call bells are appropriately accessible in the relevant setting | The number of slides in a staff presentation | Whether a training invitation was sent | The number of times a reminder email was opened | A relevant accessibility audit measures the intended condition, whereas delivery counts do not.
What does a just-culture approach require here? | Examine supported actions and system conditions with fair accountability. | Assume everyone is careless after an adverse outcome. | Promise that no conduct will ever be reviewed. | Remove patient accounts because staff did not witness the event. | Fair learning combines evidence about systems and behavior without automatic blame or automatic absolution.''',
    dialogue='''Beth | I am reviewing the safety report for the fall at eleven oh five. The immediate clinical response followed our process, but the draft explanation goes beyond what I know.
Arun | Let us start with the [[event chronology::Event chronology reconstructs the supported sequence and times before assigning a cause.]]. What is recorded, what did you observe yourself, and what was reported afterward by somebody else?
Beth | I did not witness the fall. The patient later said they had stood to reach water. I can attribute that account, but I cannot describe the fall as an eyewitness.
Arun | Make the limit on [[firsthand observation::Firsthand observation concerns what the reporter directly witnessed, which Beth explicitly did not do here.]] explicit. The patient's account remains relevant; it should not be erased simply because you did not see the event yourself.
Beth | The draft says a colleague was careless. I cannot identify evidence supporting that description, and it might steer the next reviewer before the circumstances are reconstructed.
Arun | That is a [[causal assumption::A causal assumption presents an explanation as established before the supporting evidence is available.]], not an established finding. Remove the unsupported conclusion through the appropriate correction process while retaining the actual event and relevant accounts.
Beth | It also says the call bell was out of reach. We need to establish its position at the time rather than infer it from the fact that the patient stood.
Arun | Yes. [[Call-bell access::Call-bell access is a specific environmental condition requiring verification, not an inference from the fall alone.]] is a relevant question, but not yet a verified explanation. Identify which information could clarify that condition and preserve the distinction in the report.
Beth | We may also need the surrounding care record and staff accounts. They could help reconstruct the sequence, although no single source should be treated as complete automatically.
Arun | Follow the appropriate [[evidence preservation::Evidence preservation protects relevant information so the review can reconstruct events accurately.]] process. Keep records and accounts accurate and traceable rather than rewriting them to fit the first theory suggested at the meeting.
Beth | Some staff fear that questioning the draft removes accountability. Others think reviewing individual actions means automatically blaming someone.
Arun | A [[just culture::Just culture combines fair examination of individual accountability with learning about system conditions.]] avoids both shortcuts. We examine actions and system conditions fairly; we do not decide guilt from the outcome or promise that conduct can never be reviewed.
Beth | Knowing the outcome makes it tempting to say the next step should have been obvious. But we need to understand what information people actually had at the time.
Arun | That helps avoid [[hindsight bias::Hindsight bias makes an earlier decision seem obvious after the outcome is already known.]]. Reconstruct the working situation before judging decisions. The review should explain what is supported, what remains uncertain, and what further evidence is needed.
Beth | Suppose a later review finds inconsistent positioning of the call bell. A reminder session alone would not tell us whether the intended bedside condition actually improved.
Arun | We would need an [[effectiveness measure::An effectiveness measure checks whether the intended practical condition improved rather than merely counting an activity.]] matched to that finding, such as a defined accessibility audit in the relevant setting. Attendance would show delivery, not the practical result.
Beth | We should assign the change to someone and state when follow-up will be checked. Otherwise we have only a general promise.
Arun | Name the [[action owner::The action owner is accountable for carrying out the agreed improvement and its follow-up.]] and the review point. Include an appropriate check for unintended effects rather than assume every change is beneficial in every respect.
Beth | I will revise the report to separate the recorded fall, the patient's account, and the unanswered questions. Any later conclusion should identify the evidence supporting it.
Arun | Then provide [[learning feedback::Learning feedback returns supported findings and practical next steps to the people involved in improving care.]] through the appropriate route. Staff need the supported findings and next actions, not a repeated accusation or a claim that the event is explained before review.''',
    transfer_title='Delivery is not effectiveness',
    transfer_setup='After an identified equipment-location problem, a team gives a briefing to 20 staff. No check of equipment accessibility has yet occurred. A review asks whether the practical condition improved.',
    transfer='''Lead: "The briefing was ___ to twenty staff." | delivered | Attendance supports that the briefing took place for the stated group.
Reviewer: "That is evidence of the ___, not the practical result." | activity | Delivery describes what the team did, not whether the intended condition changed.
Lead: "Equipment accessibility remains ___." | unchecked | The supplied facts say no accessibility check has yet occurred.
Reviewer: "Use a relevant measure of ___." | effectiveness | The review needs evidence that the action improved the intended practical condition.'''))
