"""Additional patient-access and administrative safety conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='Language assistance belongs in the appointment plan',
        skill='Offer language support respectfully and confirm the practical arrangements.',
        setup='A patient booking a nonurgent visit says medical discussions in English are difficult. This fictional clinic offers qualified interpreters without charging the patient. The registrar can arrange support but cannot explain clinical consent or substitute for the clinician.',
        cast='Huy|Patient\nAmira|Patient-access registrar',
        dialogue='''Huy|I can arrange the appointment in English, but I find medical explanations difficult. My daughter usually helps me understand.
Amira|Thank you for telling me. What is your [[preferred language::Preferred language identifies the language the patient wants to use for communication; basic English conversation does not establish comfort with medical discussions.]] for the visit, including any dialect we should specify?
Huy|Vietnamese. I understand some English, but I worry I will agree to something because I cannot find the right question.
Amira|We can arrange a [[qualified interpreter::A qualified interpreter provides accurate, impartial spoken communication with appropriate language and specialist skills.]] through our service. You will not be charged for that support at this clinic.
Huy|Would my daughter still be allowed to come? I would like her there for support, not to make every decision for me.
Amira|I will record your preference and confirm the visit arrangements. Her supporting role is separate from providing the interpretation.
Huy|Can the interpreter join remotely? It may be hard to find someone who can come at the same time.
Amira|We can request [[remote interpreting::Remote interpreting connects an interpreter by an approved telephone or video service rather than requiring physical attendance.]]. I will confirm availability and the clinic's setup before describing it as booked.
Huy|I would prefer not to explain private matters where everyone in the waiting room can hear.
Amira|I will note that concern and arrange the appropriate setting. Your [[confidentiality::Confidentiality concerns protecting the patient's information; interpretation should not require discussing private matters in an exposed setting.]] matters during the connection as well as during the consultation.
Huy|There is a form in the appointment message. Can you explain what the treatment permission section means?
Amira|I can help you obtain language support for the form. The clinical team needs to explain the treatment and answer your questions; I cannot give that explanation for them.
Huy|I sometimes nod when I have heard a sentence, even if I have not understood everything.
Amira|Then please say when you need something repeated. I will note the [[communication need::Communication need records the support required for effective understanding, rather than treating a nod as proof of comprehension.]] so the team can allow for questions.
Huy|Do I need to call the interpreting company myself?
Amira|No, I will send the request through our process and track the response. You should not have to coordinate the service between several offices.
Huy|Will the appointment confirmation say whether the interpreter is arranged, or only show the doctor's time?
Amira|It will distinguish the visit booking from the interpreter [[confirmation::Confirmation means the requested support has actually been arranged; a request alone is not that completed status.]]. If support is still pending, I will explain the next step.
Huy|Thank you. Please use the contact method already recorded for me, and include the language arrangement in the update.
Amira|I will check that contact detail through our usual process and update you with both the appointment and support status.''',
        transfer_title='A requested interpreter is reported as booked',
        transfer_setup='A clinic has sent an interpreter request but received no acceptance. The appointment itself is booked.',
        transfer='''Registrar: The appointment is booked, but interpreting remains ___.|pending|The request has no acceptance, so the interpreting arrangement is not yet confirmed.
Colleague: Keep that separate from the visit booking ___.|status|The confirmed visit and unconfirmed support have different administrative states.
Registrar: I will follow up with the interpreting ___.|service|The service needs to respond before the requested support can be treated as arranged.
Colleague: Tell the patient the actual position in the next ___.|update|An accurate update distinguishes the completed booking from support still being coordinated.'''),
    scenario(
        title='Two similar names, two different patient records',
        skill='Escalate a possible identity mismatch without guessing, merging, or exposing records.',
        setup='A registrar sees two similar names during check-in. Their dates of birth differ, and an incoming referral may be attached to the wrong record. No clinical information has been disclosed to the waiting patient. The patient-identification team must resolve the mismatch through the approved process.',
        cast='Mara|Registration specialist\nFelix|Health-information colleague',
        dialogue='''Mara|I have two similar names on screen, and the referral may be attached to the wrong person. I have paused the check-in step.
Felix|Good. Verify the required [[patient identifiers::Patient identifiers are person-specific details used together to match the individual to the correct record, not merely a similar name.]] through our process, without reading another person's details aloud.
Mara|The dates of birth differ. I have not shown either record to the patient or asked them to choose between the two.
Felix|Keep that boundary. A similar name does not establish a [[duplicate record::A duplicate record is more than one record for the same person; these records have not been shown to belong to one person.]], and a mismatch does not tell us which record is correct.
Mara|Could I create a third record to get the patient into the queue while we investigate?
Felix|Do not improvise a workaround. Use the identification escalation process so the care team can manage the delay safely without compounding the record problem.
Mara|I will notify the receiving team that check-in is delayed for identification review, not say the patient failed to provide information.
Felix|Exactly. Also preserve the [[referral provenance::Referral provenance identifies where the referral came from and how it entered the record, supporting investigation of the attachment error.]] so we can trace how the document was attached.
Mara|I have the source reference and arrival time. Should I move the document to the record with the closer spelling?
Felix|No. Spelling similarity is not enough. The authorized team must establish the right match and apply the correction with traceability.
Mara|We should check whether anyone has already used the referral information for scheduling or clinical work.
Felix|Yes. That is part of the [[impact assessment::Impact assessment examines what actions or disclosures may already have been affected by the mismatch, beyond correcting one attachment.]]. Do not assume there was no effect because you caught it at check-in.
Mara|The patient is asking why this is taking longer. I can explain that we are checking the record without discussing the other person.
Felix|That protects [[privacy::Privacy requires avoiding unnecessary disclosure of another patient's information while explaining the delay.]]. Offer a clear update and route any urgent clinical concern promptly to the clinical team.
Mara|If the team confirms that the referral was misfiled, will the original attachment history stay visible?
Felix|The correction must preserve the required history under the authorized process. Do not delete evidence just to make the screen look tidy.
Mara|I will send the discrepancy through the designated channel and keep the check-in status accurate.
Felix|I will confirm the review owner and the next contact. Any [[record merge::A record merge combines records and must follow authorized identity review; it is not a routine fix for similar names.]] requires the separate authorized process, not our assumption during this call.
Mara|Please confirm when the match and any affected workflow are resolved. I do not want to restart simply because my message was received.
Felix|Agreed. We will distinguish acknowledgment, identity confirmation, correction, and permission to resume the relevant administrative step.''',
        transfer_title='Similar names are mistaken for a duplicate',
        transfer_setup='Two records have similar names but different verified dates of birth. A colleague proposes merging them without identity review.',
        transfer='''Registrar: Similar names do not prove these records belong to the same ___.|person|The differing identifiers require review and do not establish one shared identity.
Reviewer: Do not perform a record ___ on that basis.|merge|Merging combines records and is not justified by name similarity alone.
Registrar: I will preserve the discrepancy and route it for authorized ___.|resolution|The designated process must establish and correct the identity issue with traceability.
Reviewer: Do not disclose the other record while explaining the ___.|delay|The patient can receive a useful explanation without learning another person's information.'''),
    scenario(
        title='A clinic closure needs more than a cancellation message',
        skill='Coordinate administrative disruption while keeping clinical prioritization with the clinical team.',
        setup='A facilities fault closes one outpatient clinic for the afternoon. Twenty patients are scheduled; none has yet been contacted. Alternative capacity is unconfirmed. Clinical staff must assess any time-sensitive care needs. Administrators are coordinating communication, not independently deciding which care can wait.',
        cast='Soren|Clinic operations manager\nPriya|Scheduling lead',
        dialogue='''Soren|Facilities has closed the clinic for this afternoon. We have twenty scheduled patients. How quickly can your team contact them?
Priya|We can begin through the approved routes, but first I need the [[service-continuity plan::The service-continuity plan sets out how essential services and communication are maintained during a disruption.]] and the clinical contact for cases that cannot simply be deferred.
Soren|The clinical lead is reviewing that now. Do not assign urgency from appointment labels or move everyone to next week automatically.
Priya|Understood. I will prepare the [[contact worklist::The contact worklist tracks each affected patient's communication status and next action, not just the number of calls attempted.]] with the booked visit, approved contact route, and assigned caller.
Soren|Another site may have space, but they have not confirmed staff or suitable appointment types.
Priya|Then we must not advertise that as [[alternative capacity::Alternative capacity means suitable usable service capacity elsewhere; a possible room alone is not confirmation.]]. I will keep it pending until the receiving team confirms what they can accept.
Soren|Some patients may already be traveling. The message needs to say clearly that this site is closed, without implying their care need has disappeared.
Priya|Yes. We will give the verified closure information and the appropriate contact for next steps, with clinical questions passed to the clinical team.
Soren|What will you record when a call goes to voicemail?
Priya|An attempted contact, not a [[successful notification::Successful notification means the message has been communicated through the defined process; an unanswered call alone does not establish it.]]. We will follow the approved message and privacy rules.
Soren|We also need language assistance for some calls. Use the recorded needs rather than assume an English voicemail is enough.
Priya|I will include those arrangements and track which messages still need an accessible follow-up.
Soren|Can you promise everyone a replacement visit tomorrow? That would make the first call easier.
Priya|Not without confirmed slots and clinical review. We can promise a specific [[status update::A status update is a communication commitment, distinct from guaranteeing a replacement appointment.]] from our team and keep it even if rebooking is unfinished.
Soren|Agreed. I will give you a confirmed update time and the route for unresolved cases before calls begin.
Priya|Please also confirm who handles people arriving at the closed site so the phone team and onsite staff give the same information.
Soren|The duty coordinator will handle that under the closure plan. What will your end-of-shift report show?
Priya|Reached, not reached, rebooked, awaiting clinical review, and pending alternatives, with a [[handover owner::A handover owner is the named person responsible for unfinished actions after responsibility transfers.]] for every unfinished action.
Soren|That lets us see the remaining work without treating twenty attempted calls as twenty resolved appointments.
Priya|Exactly. We will close each item only when its communication and next-step status meet the actual plan, not when someone has dialed the number.''',
        transfer_title='A voicemail is counted as a completed rebooking',
        transfer_setup='A scheduler leaves a permitted voicemail about a closure. No replacement slot has been offered or accepted.',
        transfer='''Scheduler: The call was attempted; the appointment is not yet ___.|rebooked|No replacement slot has been offered or accepted, so rebooking is incomplete.
Lead: Record the voicemail and the required next contact ___.|action|The record should identify what must happen next rather than imply the case is finished.
Scheduler: Any question about delaying care goes to the clinical ___.|team|Clinical staff, not the scheduler's guess, must assess time-sensitive care questions.
Lead: Carry the unfinished item into the shift ___.|handover|The unresolved task needs a clear transfer of responsibility at shift change.'''),
]
