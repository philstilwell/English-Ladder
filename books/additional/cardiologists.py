"""Additional cardiology encounters about monitoring, shared plans, and care goals."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='An alert from a cardiac device',
    skill='Distinguish a device transmission, an alert, and a reviewed clinical finding.',
    setup='Patient Ellis sees a message that a device transmission was received and asks whether it proves a new problem. Dr Kim explains the actual review process. No alert type, device setting, symptom assessment, or diagnosis is supplied. Device messaging is not a substitute for the actual urgent-care route if concerning symptoms occur.',
    cast='Ellis | Patient\nDr Kim | Cardiologist',
    dialogue='''Ellis | My device account says a transmission was received. Does that mean the team has found a new heart problem?
Dr Kim | Receipt confirms that information arrived. It does not, by itself, tell us the clinical interpretation.
Ellis | I thought every notification meant a clinician had already reviewed the recording and reached a conclusion.
Dr Kim | A [[device transmission::A device transmission is information sent from the monitoring system and is not automatically a reviewed clinical finding.]] and a reviewed finding are separate stages.
Ellis | What about the word alert? Is that always a diagnosis rather than a signal for someone to check?
Dr Kim | An [[alert::An alert flags information for attention under the actual system and requires context rather than automatically establishing a diagnosis.]] needs the actual system context and review; the word alone does not establish a diagnosis.
Ellis | I do not want to ignore something important, but I also do not want to invent a conclusion.
Dr Kim | We should clarify the real [[review workflow::The review workflow describes how the service receives, assesses, and communicates device information rather than assuming every notification has already been interpreted.]] and who communicates the outcome, without promising a finding before review.
Ellis | Does this kind of system always mean someone is watching every heartbeat in real time?
Dr Kim | Do not assume that. The service must explain the actual monitoring arrangements and their limitations for your device.
Ellis | If I have a concerning new symptom, should I just send data and wait for the next message?
Dr Kim | Follow the actual [[urgent-care instructions::Urgent-care instructions identify the appropriate clinical response to concerning symptoms and are not replaced by sending a routine device transmission.]] rather than treating a routine transmission as a substitute for assessment.
Ellis | I also want to know how to report a problem with the connection itself.
Dr Kim | The team can explain the appropriate technical contact and distinguish a connection problem from a clinical finding.
Ellis | So a missing signal would not automatically prove that my heart rhythm is normal or abnormal?
Dr Kim | Correct. [[Data availability::Data availability concerns whether usable information reached the service and cannot itself establish the underlying clinical state when data are missing.]] is a separate question from what the information means clinically.
Ellis | Could we confirm who explains the reviewed result and how I can check the status?
Dr Kim | Yes. We will identify the actual contact route and distinguish a pending review from a completed discussion.
Ellis | That helps me understand the message without mistaking an administrative confirmation for a diagnosis.
Dr Kim | A clear [[review status::Review status identifies whether information is awaiting assessment or has been reviewed and should not be inferred solely from a receipt notification.]] prevents exactly that confusion while keeping the appropriate clinical contact route visible.''',
    transfer_title='The data arrived but review is pending',
    transfer_setup='The service confirms receipt of a transmission. Clinical review is pending. The patient has not reported a symptom in this update.',
    transfer='''Patient: "The transmission was ___." | received | The service confirms that the device information arrived.
Clinician: "Clinical review remains ___." | pending | Receipt does not mean the clinical interpretation is complete.
Patient: "That is not a confirmed ___." | diagnosis | A received transmission alone does not establish a clinical diagnosis.
Clinician: "We should clarify the review ___." | status | The relevant question is the actual stage of review and communication.'''),
scenario(title='Reconciling a cross-specialty medicine plan',
    skill='Resolve conflicting instructions through the responsible clinicians without independently changing treatment.',
    setup='Dr Reed, a cardiologist, and Dr Hall, a procedural clinician, find conflicting medicine instructions in two appointment documents. The actual medicines, procedure, and doses are not supplied. They agree to verify the current plan, responsible prescriber, and patient communication before presenting an instruction as settled.',
    cast='Dr Reed | Cardiologist\nDr Hall | Procedural clinician',
    dialogue='''Dr Hall | Our appointment document contains a medicine instruction that conflicts with the cardiology letter. The patient has noticed the difference.
Dr Reed | We need to resolve that through the responsible clinicians, not ask the patient to guess which document to follow.
Dr Hall | I will identify the exact instruction and date rather than summarize it as a general disagreement.
Dr Reed | The [[document version::The document version identifies which dated instruction is being discussed and helps distinguish a superseded copy from a current plan.]] matters. We should establish which copies are current and what authority each instruction has.
Dr Hall | The procedure team needs the actual clinical context, not an assumption that all procedures use identical instructions.
Dr Reed | Agreed. The [[procedural context::Procedural context includes the actual planned intervention and relevant circumstances, which must be known before medicine instructions are reconciled.]] must be verified before a medicine plan is treated as appropriate.
Dr Hall | We should also identify the clinician responsible for the prescription rather than assume the appointment office owns the decision.
Dr Reed | Let us confirm the [[responsible prescriber::The responsible prescriber is the clinician accountable for the relevant medicine decision and should be identified explicitly when instructions conflict.]] and the necessary cross-specialty discussion.
Dr Hall | Until then, I will not describe a stop or restart instruction as agreed merely because it appears in one letter.
Dr Reed | Correct. We are reconciling conflicting information, not issuing a new medicine instruction in this conversation.
Dr Hall | The patient needs a single clear explanation once the actual decision has been verified.
Dr Reed | A [[reconciled instruction::A reconciled instruction is the verified direction after conflicting information has been resolved by the appropriate clinicians.]] should identify the relevant medicine details, timing, and contact route in the real clinical plan.
Dr Hall | If one document is superseded, should we retain the correction history rather than silently erase the old wording?
Dr Reed | Yes. Follow the actual record-correction process so the change and its authority remain traceable.
Dr Hall | I will confirm who contacts the patient and how we verify that the conflicting message has been corrected.
Dr Reed | That is [[communication ownership::Communication ownership assigns responsibility for explaining the verified plan and correcting the earlier conflicting message to the patient.]], which must not disappear after the clinicians agree among themselves.
Dr Hall | We should also update the relevant teams so the old instruction is not repeated at the next appointment.
Dr Reed | Exactly. A resolved discussion is incomplete if the outdated message remains the one everyone keeps using.
Dr Hall | I will record the verified plan, the responsible clinicians, and the communication outcome under our actual process.
Dr Reed | Then [[closed-loop reconciliation::Closed-loop reconciliation resolves the conflicting instructions and verifies that the appropriate recipients have the updated plan rather than merely documenting internal agreement.]] includes both a clinical decision and accurate communication to the people who need it.''',
    transfer_title='The old letter is still being used',
    transfer_setup='The clinicians have verified the current plan, but an appointment office is still sending the older letter. The team requests an authorized correction and patient communication.',
    transfer='''Clinician: "The current plan is ___." | verified | The clinical plan has been checked and agreed by the relevant clinicians.
Office: "We are still sending the ___ letter." | older | The remaining problem is distribution of the superseded document.
Clinician: "We need an authorized ___." | correction | The outdated communication must be corrected through the proper record and document process.
Office: "The patient also needs clear ___." | communication | An internal correction alone does not ensure the patient receives the accurate plan.'''),
scenario(title='Discussing priorities in advanced heart disease',
    skill='Elicit care goals without equating supportive care with abandonment or a predetermined resuscitation decision.',
    setup='Patient Avery, living with advanced heart disease, wants less breathlessness and more time at home. Dr Shah explores those priorities and explains that supportive or palliative care can be discussed alongside disease-directed care. No prognosis estimate, treatment withdrawal, or resuscitation decision is supplied.',
    cast='Avery | Patient\nDr Shah | Cardiologist',
    dialogue='''Avery | I want less breathlessness and more time at home. I am worried that saying that sounds like giving up.
Dr Shah | Those priorities deserve a direct discussion. Telling us what matters does not automatically mean stopping disease-directed care.
Avery | I would like the team to hear the practical things I am finding hardest, not only the test results.
Dr Shah | We can discuss your [[symptom burden::Symptom burden describes the impact of symptoms on daily life and helps connect clinical information with what matters to the patient.]] and how it affects the activities and time that matter to you.
Avery | Someone mentioned palliative care, and I thought that meant all other treatment would end immediately.
Dr Shah | [[Palliative care::Palliative care addresses symptoms, support, and quality of life and can be discussed alongside disease-directed care rather than automatically replacing it.]] can be discussed alongside other treatment. It does not automatically mean that every treatment stops.
Avery | I also worry that a conversation about priorities will be recorded as a decision about resuscitation.
Dr Shah | A discussion of [[care goals::Care goals describe the outcomes and experiences important to the patient and are not automatically a specific resuscitation or treatment-withdrawal decision.]] is not itself a resuscitation decision. Any specific decision needs its own appropriate discussion.
Avery | I would like my daughter involved, but I still want to speak for myself while I can.
Dr Shah | We can include her with your permission while keeping you central to the conversation and clarifying the relevant roles.
Avery | If there are options with different burdens, I want those explained in terms I can compare.
Dr Shah | We should discuss [[treatment burden::Treatment burden includes the practical and personal demands of care and should be considered with expected benefits and the patient's priorities.]] alongside expected benefits, using the actual clinical options rather than an invented choice.
Avery | Can you guarantee that choosing a particular plan will keep me out of hospital?
Dr Shah | No. We can explain the aims and uncertainties, but we should not promise an outcome that cannot be guaranteed.
Avery | Then I would like a plan that records my priorities without pretending the future is settled.
Dr Shah | An [[advance care discussion::An advance care discussion explores preferences for future care and requires accurate documentation without claiming that every later circumstance or decision is already settled.]] can help, with the actual documentation and legal arrangements explained where relevant.
Avery | What happens if my priorities change as my symptoms or circumstances change?
Dr Shah | We should revisit them. A record should support your care, not freeze a preference that no longer represents you.
Avery | I would appreciate a clear contact who can help coordinate the clinical and practical support.
Dr Shah | We can identify the appropriate [[care coordinator::A care coordinator helps connect services and responsibilities, but the actual role and contact route must be confirmed rather than assumed.]] and confirm the next discussion without converting today's priorities into an unmade treatment decision.''',
    transfer_title='A preference has changed',
    transfer_setup='A patient previously prioritized clinic-based treatment but now asks to discuss more care at home. No treatment change has yet been agreed.',
    transfer='''Patient: "I want to revisit my ___." | priorities | The patient asks to discuss a changed preference about the setting of care.
Clinician: "A treatment change is not yet ___." | agreed | The scenario contains a request for discussion, not a completed decision.
Patient: "My current wishes should be ___." | heard | The patient's updated preferences need to inform the next discussion.
Clinician: "We will explain the actual ___." | options | Available options require an appropriate clinical discussion rather than an assumed change.'''),
]
