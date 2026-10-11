"""Additional general-practice encounters, authored independently of the eight lessons."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='A consultation through a qualified interpreter',
    skill='Speak directly to the patient, use manageable segments, and verify the interpreted message.',
    setup='Dr Patel meets Noor with qualified interpreter Lin. The script shows the clinician and interpreter coordinating the interpreted consultation; Noor remains the patient and decision-maker. A relative has offered to summarize, but the service provides qualified interpretation. No clinical diagnosis or treatment choice is supplied.',
    cast='Dr Patel | General practitioner\nLin | Qualified interpreter',
    dialogue='''Dr Patel | Before we begin, I will introduce your role to Noor and confirm the language and communication preferences.
Lin | Thank you. Please speak directly to Noor rather than asking me what the patient thinks in the third person.
Dr Patel | I will use [[direct address::Direct address keeps the patient as the person being consulted rather than turning the interpreter into the recipient of clinical questions.]] and keep my attention on the patient, even while you interpret the words.
Lin | That helps preserve the relationship. Please also give me manageable segments rather than a long uninterrupted explanation.
Dr Patel | I can pause after one idea. I do not want a long speech to become an abbreviated summary.
Lin | I will interpret the content rather than replace it with my own advice or a shortened conclusion.
Dr Patel | If a term is ambiguous, please identify the need for [[clarification::Clarification resolves an unclear term or message before it is interpreted as though its meaning were already certain.]] before we continue to a new point.
Lin | I will make that transparent to both of you rather than silently choose a meaning that may be wrong.
Dr Patel | Noor's relative offered to summarize. How should I explain why we are using the service today?
Lin | Explain the value of accurate, confidential language support without suggesting that the relative has done something wrong.
Dr Patel | I will describe [[qualified interpretation::Qualified interpretation provides trained language support and does not transfer clinical decision-making or consent from the patient to the interpreter.]] as support for Noor's participation, not as a substitute decision-maker.
Lin | Exactly. I do not provide consent on the patient's behalf or decide which clinical option the patient should choose.
Dr Patel | When I check understanding, I will ask Noor to explain the message in their own words.
Lin | I can interpret that response fully. Please do not treat a brief yes as proof that the explanation was clear.
Dr Patel | That makes [[teach-back::Teach-back checks how the explanation was understood and should be directed to the patient through the interpreter rather than answered by the interpreter.]] a check on my explanation, not a test for you to answer instead of Noor.
Lin | Yes. If the response shows a misunderstanding, explain the point differently and let me interpret the revised explanation.
Dr Patel | I will also record that language support was used and distinguish the patient account from anyone else's report.
Lin | That preserves [[source attribution::Source attribution identifies who supplied the information and prevents an interpreted patient account from being confused with the interpreter's own opinion.]] while keeping the interpreter's role clear.
Dr Patel | Before closing, I will confirm the actual next step and the appropriate language support for follow-up.
Lin | A clear [[closing summary::A closing summary gathers the agreed information and next step so the patient can confirm the meaning through the same language support.]] gives Noor a chance to correct the meaning before the consultation ends.''',
    transfer_title='The interpreter requests a shorter segment',
    transfer_setup='The clinician gives a long explanation. The interpreter asks for one idea at a time so the full meaning can be interpreted. No summary is substituted.',
    transfer='''Interpreter: "Please give one ___ at a time." | idea | The request is for manageable segments rather than a long uninterrupted explanation.
Clinician: "I will ___ between them." | pause | Pausing allows each segment to be interpreted before more information is added.
Interpreter: "I will preserve the full ___." | meaning | The interpreter aims to retain the content rather than replace it with a summary.
Clinician: "The patient remains the ___." | decision-maker | Interpretation supports the patient's participation and does not transfer their decision-making role.'''),
scenario(title='A work note without unnecessary disclosure',
    skill='Clarify the purpose and authorized content of a work-related letter.',
    setup='Patient Ellis asks Dr Shaw for a work note. The employer requests a diagnosis, but Ellis wants to discuss what information is actually necessary and authorized. The clinician will follow applicable rules and use supported facts. No work-capacity judgment or legal entitlement is supplied.',
    cast='Ellis | Patient\nDr Shaw | General practitioner',
    dialogue='''Ellis | My employer wants a note and asked for my diagnosis. I am not comfortable sending my whole medical history.
Dr Shaw | Let us clarify the purpose of the letter and what information is necessary under the applicable process.
Ellis | I want them to understand the relevant limitation, but not receive details unrelated to work.
Dr Shaw | We should distinguish [[functional information::Functional information describes relevant abilities or limitations and is different from disclosing an entire diagnostic or personal history.]] from a full clinical history, while checking what this particular process actually requires.
Ellis | Could the letter say I cannot do a particular task even if we have not assessed that task?
Dr Shaw | No. Any statement needs a basis in the actual assessment; I should not invent a restriction to make the letter sound useful.
Ellis | Then we need to discuss the real duties rather than use a generic phrase about all work.
Dr Shaw | Yes. The [[job demands::Job demands are the actual tasks and conditions relevant to assessing work-related function rather than a generic assumption about an occupation.]] provide context, but the clinical assessment and any authorized occupational review remain separate.
Ellis | If the employer asks for more information later, does my request for this note authorize every future disclosure?
Dr Shaw | It does not automatically do that. We need the appropriate permission and applicable rules for the information being shared.
Ellis | I would like to know the recipient and see what the note is intended to communicate.
Dr Shaw | We will clarify the [[disclosure scope::Disclosure scope defines the information, purpose, and recipient covered by the relevant authorization rather than treating one request as unlimited permission.]] rather than treat a request for a note as unlimited permission.
Ellis | Can the note guarantee that the employer will approve my preferred arrangement?
Dr Shaw | No. The letter can communicate supported information; the employer's process and any legal rights need their own appropriate handling.
Ellis | I understand. I do not want an unsupported promise about the employment decision.
Dr Shaw | We should also distinguish an [[occupational recommendation::An occupational recommendation concerns work-related advice based on appropriate assessment and is not a guarantee that an employer will adopt a particular arrangement.]] from the employer's eventual decision.
Ellis | What if the form has a box that does not match what you can establish?
Dr Shaw | We should explain the [[evidence limitation::An evidence limitation identifies what the assessment cannot support and prevents a form's wording from forcing an invented clinical conclusion.]] or seek clarification rather than force an unsupported answer.
Ellis | Then the note can stay factual, limited to its purpose, and shared through the agreed route.
Dr Shaw | Exactly. A clear [[authorized recipient::An authorized recipient is the person or service permitted to receive the specified information through the applicable process.]] and supported content matter more than adding unnecessary medical detail.''',
    transfer_title='The employer asks for an unrelated history',
    transfer_setup='A work-note request asks for unrelated past diagnoses. The patient has not authorized that disclosure. The clinician checks the purpose and applicable requirements before responding.',
    transfer='''Patient: "Those past diagnoses are ___ to the stated purpose." | unrelated | The scenario identifies the requested history as unrelated to the work-note purpose.
Clinician: "Disclosure has not been ___." | authorized | The patient has not authorized sharing the additional historical information.
Patient: "Please clarify the actual ___." | requirements | The appropriate process must establish what information is actually required.
Clinician: "We will not assume unlimited ___." | permission | A request for a work note does not itself authorize every possible disclosure.'''),
scenario(title='Closing an unanswered result call',
    skill='Assign follow-up responsibility without treating an attempted call as completed communication.',
    setup="Dr Wynn and coordinator Jo review a result that still needs the clinician's explanation to the patient. A call went unanswered and no sensitive voicemail was left because the contact permissions require checking. The actual clinical priority and escalation route must be confirmed; no result value or safe delay is supplied.",
    cast='Dr Wynn | General practitioner\nJo | Care coordinator',
    dialogue='''Jo | The call went unanswered, and the result has not yet been explained to the patient. I have recorded the attempt.
Dr Wynn | Thank you. An attempted call is not completed communication. We need the actual priority and follow-up process.
Jo | I did not leave sensitive details because the voicemail permission was not clear in the record.
Dr Wynn | We should verify the [[contact permission::Contact permission specifies what communication is authorized through a particular route and should be checked before sensitive details are left.]] rather than assume that a listed number permits every kind of message.
Jo | The task currently says called patient, which might make another colleague think the discussion already happened.
Dr Wynn | Change the status through the approved record process to reflect an [[unsuccessful contact attempt::An unsuccessful contact attempt records that contact was tried but not achieved, preventing it from being mistaken for a completed clinical explanation.]], without hiding the original history.
Jo | Who should determine how urgently the next attempt or escalation needs to happen?
Dr Wynn | The responsible clinician must confirm the clinical priority using the actual result and circumstances, not an administrative guess.
Jo | I will not infer that it can wait merely because the patient did not answer.
Dr Wynn | Correct. The [[clinical priority::Clinical priority is determined from the actual result and circumstances and cannot be inferred from an unanswered telephone call.]] remains a clinical question requiring the appropriate review.
Jo | Once that is confirmed, we need a named person to carry out the next agreed contact step.
Dr Wynn | Let us assign [[follow-up ownership::Follow-up ownership identifies who must complete the next action so an unanswered contact does not disappear between team members.]] explicitly and record the actual plan and route.
Jo | If that person is away, should the task remain in an individual inbox without review?
Dr Wynn | No. Use the service's actual coverage and escalation arrangements so the responsibility does not depend on an unmonitored inbox.
Jo | We also need to know when the receiving clinician has accepted any escalation.
Dr Wynn | An [[acknowledged escalation::An acknowledged escalation includes confirmation that the relevant person received and accepted the concern rather than merely having a message sent.]] is different from a sent message with no response.
Jo | I will keep the result explanation marked incomplete until the appropriate discussion or documented process is completed.
Dr Wynn | Yes. Record what was actually communicated, by whom, and any unresolved issue according to the clinical process.
Jo | That should prevent another colleague from assuming that the patient knows the result just because we tried calling.
Dr Wynn | Exactly. A [[closed-loop follow-up::Closed-loop follow-up verifies that the relevant communication and responsibility were completed or appropriately escalated, not simply attempted.]] depends on accurate status, assigned responsibility, and the actual clinical response.''',
    transfer_title='A message was sent but not accepted',
    transfer_setup='A coordinator sends an escalation to the appropriate clinician. No acknowledgment has arrived. The task remains open under the actual service process.',
    transfer='''Coordinator: "The escalation was ___." | sent | The coordinator has transmitted the escalation to the appropriate clinician.
Clinician: "Receipt has not been ___." | acknowledged | No acknowledgment has arrived, so acceptance cannot be assumed.
Coordinator: "The task remains ___." | open | The scenario explicitly keeps the task open pending the appropriate process.
Clinician: "We must follow the actual service ___." | process | The response follows the real clinical and operational arrangements rather than an invented waiting rule.'''),
]
