"""Twenty-four original short radiography conversations."""
from books.x_ray_technicians_content import BOOK
from books.medical_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], """
The appointment number is not the identity check | A patient offers a booking message. | Patient | Radiographer
I have the appointment number on my phone. Is that all you need before the examination?
It helps locate the booking, but we still use the approved patient-identification process.
I thought the examination number automatically established that the record belonged to me.
An examination identifier and verification of the person are different checks.
Please explain what details you need rather than reading them out for me to agree.
We will follow the actual department process and ask you to state the required information.
There is an old address in the record as well, which may need correction.
We should handle that through the approved record process without ignoring the identity checks.
Then the appointment message is useful, but it does not replace the verification.
Exactly. We need the correct person, request, and examination linked accurately before proceeding.

The side is missing from the request | A radiographer contacts the requesting team. | Radiographer | Requesting clinician
The ankle request does not specify laterality, and the patient reports a left-sided injury.
Thank you for identifying the discrepancy before acquisition. The request needs appropriate clarification.
I have preserved the patient's account without changing the order independently.
That is important. Reported symptoms and an authorized amendment are not the same action.
Could you clarify the intended examination through the approved request process?
Yes. We will review the actual clinical indication and document the authorized instruction.
No images have been acquired while the side remains unresolved.
Please keep that status clear so the request is not mistaken for a completed examination.
I will confirm the verified plan with the patient once the clarification is available.
Then the examination can proceed under the actual checks rather than an assumption.

A leading question gets a misleading yes | A radiographer rechecks the patient's account. | Radiographer | Patient
I asked whether it was your left wrist, and you agreed, but you are indicating the right.
I was agreeing that it was my wrist; I did not catch the side you mentioned.
Thank you. Let me ask without suggesting the answer: which wrist was injured?
The right wrist is the one I am describing.
That differs from the request, so we need the appropriate verification before taking images.
I appreciate the pause. I did not intend to confirm the wrong side.
A yes can refer to a different part of a question, which is why clarification matters.
Will you record what I actually said rather than assume the earlier answer settled it?
Yes. We will preserve the corrected account and follow the authorized clarification process.
Then a clearer question can prevent a misunderstanding from becoming the examination plan.
""")
LESSONS['module-2'] = short_lesson(BOOK['units'][1], """
Cannot move is not refusing | A patient explains a positioning limitation. | Patient | Radiographer
I cannot raise the arm that high without pain, but I am not refusing the examination.
Thank you for distinguishing that. Stop the movement while we review the appropriate approach.
I was worried that the record would simply call me uncooperative.
We should document the actual limitation rather than make a judgment about your intention.
Could you explain one movement at a time so I know exactly what is being requested?
Yes. A short instruction and pause let us check what is manageable.
I also want you to ask before offering hands-on support.
We will explain any proposed assistance and obtain the appropriate agreement.
Does this automatically authorize a different projection?
No. Any adapted examination must follow the actual assessment and authorized technical process.

A breathing instruction needs rehearsal | A radiographer checks a patient's understanding before acquisition. | Radiographer | Patient
Before the image, let us practice the breathing instruction that applies to this examination.
I find it difficult when several instructions are given quickly together.
We can separate the steps and make clear when practice ends and acquisition begins.
I should not have to guess whether you mean breathe normally or hold at that moment.
Correct. The actual instruction needs to be clear and appropriate for you.
If I cannot manage it comfortably, should I say so before trying again?
Yes. Tell me about the difficulty so the appropriate approach can be reviewed.
I appreciate practicing without an exposure rather than feeling rushed into the sequence.
The rehearsal checks understanding; it does not replace the actual examination and safety checks.
Then we can proceed only with the verified plan and a clear instruction.

Transfer assistance needs assessment | Two staff members coordinate a patient movement. | Radiographer | Nurse
The patient reports difficulty standing from the chair. We need the appropriate transfer assessment.
I will identify the relevant assistance rather than assume a single person can manage it.
The examination request does not itself tell us which transfer method is suitable.
Agreed. The patient's actual needs and our authorized process determine that.
I will not move the patient unexpectedly while waiting for the assessment.
Please explain the pause and ask about the difficulty without assigning a diagnosis.
Once the assistance is confirmed, we can coordinate the sequence and responsibilities.
Yes, including who provides support and when the patient is ready.
A clear floor alone does not establish that the transfer is safe.
Exactly. Practical preparation includes assessment, appropriate people, equipment, and the patient's understanding.
""")
LESSONS['module-3'] = short_lesson(BOOK['units'][2], """
The answer needs privacy | A patient asks to answer screening questions alone. | Patient | Radiographer
Could we discuss that screening question without my companion in the room?
We can arrange appropriate privacy and explain why the question is being asked.
My companion does not know the information, and I do not want them answering for me.
Their presence does not automatically authorize them to provide or receive every detail.
I may be unsure of the answer even when we speak privately.
Please say that. Uncertainty should not be recorded as a negative response.
Will an uncertain answer automatically cancel every possible imaging examination?
No universal conclusion follows; the actual examination and clinical review determine the process.
I would like the reviewed plan explained before anyone assumes I have agreed to proceed.
We will keep the screening response, review outcome, and appropriate agreement distinct.

Unsure was entered as no | A radiographer corrects a screening record. | Radiographer | Supervisor
The patient said unsure, but the screening field was recorded as no.
That needs correction through the approved process, with the uncertainty preserved.
I have not proceeded on the assumption that pregnancy has been excluded.
Good. A binary field should not force the patient's actual answer into a false category.
The original entry and correction need to remain traceable.
Yes. Follow the record process and the appropriate clinical review for the examination.
Should the team know that the answer changed because of an entry error?
They need the accurate current information and relevant correction history.
I will not describe the correction as a new confirmed pregnancy finding.
Correct. Restoring uncertainty is different from establishing either a positive or negative conclusion.

A risk question needs the actual examination | A patient asks about a blanket radiation claim. | Patient | Radiographer
Someone told me every X-ray has exactly the same risk during pregnancy. Is that accurate?
The actual examination and circumstances matter; a blanket statement is not an individualized assessment.
Can you give me a precise personal estimate from this short conversation?
That requires the appropriate professional review, not an invented number.
I would like the reason for the examination considered along with the possible harm.
That is part of the relevant benefit-and-risk discussion with the authorized team.
Does asking for that explanation mean I have already refused the examination?
No. A request for information is not automatically a decision to decline.
Please record my question and arrange the actual review rather than choosing an answer for me.
We will preserve your concern and explain the verified next step through the department process.
""")
LESSONS['module-4'] = short_lesson(BOOK['units'][3], """
A child chooses the preparation order | A radiographer offers a bounded choice. | Radiographer | Child
Would you like me to explain the picture first or show the equipment first?
Please show me first, because the machine looks different from what I expected.
That is a choice we can make. I will explain each part as we go.
Does choosing the demonstration mean I have already agreed to every movement?
No. We still explain the examination and follow the appropriate permission and safety process.
I want to know when something is practice and when the actual picture happens.
I will make that distinction clear rather than ask you to guess.
Can I tell you when I do not understand a word?
Yes. Questions help me explain the instruction in a way that makes sense.
Then I can choose the preparation order without being surprised by the next step.

The caregiver's place needs checking | A child asks where a caregiver can stand. | Child | Radiographer
Can my caregiver stand right beside me for the whole examination?
We need to check the actual safety arrangements before promising where anyone can stand.
I thought being allowed into the room meant every position was permitted.
Entering the room and being present during exposure can involve different arrangements.
Could you explain where they will be before we start the actual picture?
Yes. We should explain the approved plan so you know what to expect.
If I feel worried, I would like a clear way to tell you.
We can agree on an appropriate pause signal and check that you understand it.
I do not need a promise that nothing can ever feel uncomfortable.
Honest explanation and an agreed process are more useful than a guarantee we cannot make.

A long instruction is broken into steps | A child forgets part of a rehearsal. | Child | Radiographer
I remembered the first movement, but I forgot the rest of the instruction.
That tells me the explanation was too much at once. Let us separate the steps.
Are you going to call me difficult because I did not remember all three?
No. We need an instruction you can understand, not a label about your behavior.
Can we practice one part before adding another?
Yes. This is still preparation, and no image has been acquired.
Please tell me clearly when the practice is finished.
I will explain the sequence and check your understanding before the actual examination.
That gives me time to ask instead of guessing what comes next.
Exactly. A shorter instruction can support cooperation without pressure or surprise.
""")
LESSONS['module-5'] = short_lesson(BOOK['units'][4], """
A line is not something to move aside | A radiographer coordinates bedside equipment. | Radiographer | Nurse
The attached line affects detector placement. Who is authorized to manage it during preparation?
I will identify the appropriate colleague rather than assume you should disconnect it.
Thank you. Recognizing the obstacle does not give me authority to alter the connection.
Correct. The patient's actual equipment and care needs must guide the preparation.
We should agree on the movement sequence before anyone places the detector.
Yes, with the relevant support and line responsibilities explicit.
I will not treat silence as confirmation that the bedside is ready.
I will give an actual readiness update once the required arrangements are in place.
Then the examination can proceed without an informal assumption about equipment management.
That is the purpose of the coordination: clear roles alongside the real clinical checks.

Isolation information needs verification | Two staff members clarify bedside precautions. | Radiographer | Nurse
Before bringing the mobile equipment closer, I need to verify the current precautions for this room.
I will confirm the actual isolation information rather than rely on an older note.
The absence of a sign should not become proof that no precaution applies.
Agreed. We need the current service information and the approved process.
I also need the equipment-cleaning arrangements that apply after this examination.
Those should match the actual equipment and infection-control requirements.
Could we distinguish what has been verified from what someone merely remembers?
Yes. The preparation record should not turn an uncertain recollection into a current instruction.
I will explain any pause to the patient without disclosing unrelated information.
Then the examination can be coordinated with both clear communication and the appropriate precautions.

Readiness is not the same as arrival | A lead technologist checks a portable examination status. | Lead technologist | Radiographer
You have arrived at the bedside. Are the required preparations actually complete?
Not yet. Patient support has been requested, but the assisting colleague has not arrived.
Then the status should remain awaiting preparation, not ready for acquisition.
I will keep that distinction clear and coordinate with the bedside team.
Is the request for assistance enough to assume someone has accepted responsibility?
No. We need the actual acknowledgment and the required people in place.
Please also identify any equipment-clearance issue before moving the mobile unit.
I have noted the available space and will not relocate clinical equipment independently.
Once the actual checks are complete, confirm the readiness through the agreed process.
I will. Arrival, a request, and confirmed readiness are separate stages.
""")
LESSONS['module-6'] = short_lesson(BOOK['units'][5], """
Motion is a description, not blame | A radiographer discusses image quality with a senior colleague. | Radiographer | Senior colleague
There is motion affecting the image, but I do not know why the patient moved.
Then describe the artifact rather than label the patient uncooperative.
The instruction may have been difficult to follow, although that has not been established.
We can review the process without turning a possible explanation into a proven cause.
Does identifying motion automatically mean the image must be repeated?
No. The appropriate review considers whether the clinical question is adequately addressed.
I will preserve the original image and request the actual technical assessment.
Good. An imperfect appearance is not by itself authorization for another exposure.
The record should separate the limitation, review outcome, and any authorized next acquisition.
Exactly. That supports image integrity and useful quality improvement.

An exposure indicator is misunderstood | A trainee asks about a system value. | Trainee | Senior radiographer
The system displays an exposure index. Can I call it the patient's radiation dose?
No. It is a detector-related indicator under the system's specified conditions, not a direct patient-dose reading.
Then its meaning requires the actual equipment information and acquisition context.
Correct. We should not rename one quantity as another because both involve exposure.
Does the displayed image brightness alone tell us whether the exposure was appropriate?
No. Processing and display can affect appearance, so that shortcut is unreliable.
I should review the relevant technical information through the approved process.
Yes, and distinguish the technical assessment from a diagnostic interpretation.
Could we explain the limitation without giving a dose estimate that was never measured?
That is essential. Precise terminology prevents a number from implying more than it establishes.

A rejected image remains part of review | Two staff members discuss record integrity. | Radiographer | Quality lead
The image may be rejected after review. Should it disappear from the record?
Follow the approved retention process; do not hide evidence of the acquisition.
I thought deleting it would make the examination look cleaner.
A cleaner-looking record is not the goal if it removes information needed for review.
Reject analysis depends on an accurate account of what was acquired and why it was unsuitable.
Exactly. We need the actual limitation and decision, not a reconstructed perfect history.
Should the review focus on a particular person before the circumstances are established?
No. Start with verified observations and examine the process rather than assume blame.
I will keep the image and relevant information available through the authorized system.
That supports a traceable record and a meaningful opportunity to improve the work.
""")
LESSONS['module-7'] = short_lesson(BOOK['units'][6], """
A worried patient asks for a diagnosis | A radiographer provides a helpful reporting handoff. | Patient | Radiographer
You looked at the screen for a while. Does that mean you saw something serious?
My work with the images does not establish a diagnosis I can give you in this conversation.
I understand the boundary, but I do not want to leave without knowing the next step.
Let us confirm the reporting process and who will explain the result.
Can you promise that the result will be available tomorrow?
I need to verify the actual arrangements rather than invent a deadline.
I would appreciate a contact for questions about the result status.
We can identify the appropriate referring service or reporting contact under our process.
That is more helpful than either guessing a diagnosis or simply saying nothing.
Exactly. A clear boundary should still include a useful route for your question.

The report is online but unexplained | A patient asks what portal access means. | Patient | Radiographer
I can see a report in the portal, but nobody has explained it to me.
Access to a report and a clinical discussion of its meaning are different steps.
Could you interpret the unfamiliar terms from the image while I am here?
The appropriate reporting or referring clinician needs to explain the actual findings in context.
I do not want to assume that every highlighted phrase is a confirmed diagnosis.
That is a reason to use the proper clinical explanation rather than guess from the wording.
Who should I contact if the report arrived before my follow-up discussion?
Let us confirm the actual contact route through the service.
Then portal release should not be recorded as though the clinical explanation has already happened.
Correct. The communication status should describe what actually occurred.

A preliminary report is not the final version | A coordinator checks which report is being discussed. | Coordinator | Radiographer
The patient refers to a preliminary report, but a later version may be available.
We need to verify the actual report status rather than assume the first copy is final.
Should I describe the later document as a correction before checking its content?
No. A later version and a confirmed correction are not automatically the same thing.
The responsible clinician should explain any relevant change in the actual interpretation.
Yes. We should not interpret the clinical significance from the document timestamp alone.
I will identify the current authorized version and the appropriate contact for explanation.
Please preserve the distinction between record availability and the patient's understanding.
Then the patient can ask about the correct report rather than compare unexplained fragments.
That supports a clear handoff without giving a diagnosis outside the relevant role.
""")
LESSONS['module-8'] = short_lesson(BOOK['units'][7], """
A suspected mismatch is not a proven cause | A radiographer reports a labeling concern. | Radiographer | Supervisor
The image label may not match the verified examination details. I have paused further release.
Thank you. Preserve the record and state exactly what is known.
I have not established how the mismatch arose or whether another service received the information.
Keep those questions open rather than state that no impact occurred.
Should I identify a person as responsible because their name appears in the workflow?
No. The cause requires the appropriate investigation, not an assumption from one visible entry.
I will document the event sequence and the actual containment action.
Please use verified times and distinguish them from estimates or later recollections.
The correction will follow the authorized process with its history retained.
That protects the record while the actual review determines the next steps.

One corrected screen is not every system | A supervisor checks the reach of a correction. | Supervisor | Radiographer
The local record has been corrected through the approved process. Have linked systems been checked?
Not yet. I cannot confirm that every downstream record now matches.
Then full reconciliation remains incomplete, even though the local display looks correct.
I will identify the relevant systems and recipients through the authorized review process.
We should not assume that a local edit automatically updates every earlier message.
Agreed. The actual distribution and correction arrangements need verification.
Please retain the original and the authorized change history.
They remain available through the approved record system for traceability.
I will keep the outstanding reconciliation tasks visible with named responsibility.
That prevents a partial correction from being reported as complete resolution.

A near-miss label needs evidence | Two staff members discuss incident classification. | Radiographer | Safety lead
Can I call this a near miss before we know whether the incorrect information reached anyone?
The classification should follow the actual facts and reporting process.
I wanted to reassure the team that the problem was caught.
You can state the containment action without claiming that no relevant harm or exposure occurred.
The downstream impact is still being reviewed, so I should say unconfirmed.
Yes. Unconfirmed impact is not the same as established absence of impact.
I will report the verified chronology and the questions that remain unresolved.
That gives the review useful information without minimizing or exaggerating the event.
Once the facts are established, the appropriate classification can be recorded.
Exactly. Accurate reporting supports learning better than choosing the most reassuring label first.
""")
