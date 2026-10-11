"""Twenty-four original short cardiology conversations."""
from books.cardiologists_content import BOOK
from books.medical_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], """
A symptom time and a call time differ | A clinician corrects an urgent handoff while care continues. | Referrer | Cardiologist
The patient clarified that the pressure began before the call, not at the time recorded for contact.
Please preserve the corrected symptom onset separately from the call time while the response continues.
I have not assigned an exact minute because the patient cannot confirm one.
That is appropriate. An approximate report should not become a falsely precise timestamp.
The emergency pathway remains active, and the team has acknowledged the update.
Good. A corrected history should not interrupt the actual urgent clinical process.
I will identify which earlier entry is superseded through the approved record process.
Please also retain the source of the correction rather than present it as a new measured finding.
The handoff will distinguish onset, contact, and the time of the clinical assessment.
That gives the receiving team a usable sequence without inventing evidence.

An absent result is not negative | Two clinicians clarify an unavailable test result. | Cardiologist | Referrer
Do we have an actual verified result, or is the test still pending?
It is pending. The earlier summary said negative, but no result supports that word.
That needs prompt correction. An unavailable result cannot be treated as a negative finding.
I will correct the message and confirm that the receiving team acknowledges the change.
Please keep the current clinical concern and active response visible while the record is clarified.
I will not infer a safe delay from the missing result.
Correct. The actual assessment and urgent process determine the response.
The revised handoff will state pending rather than substitute a reassuring conclusion.
It should also identify the responsible clinician for reviewing the result when available.
Then the correction addresses both the inaccurate word and the unfinished follow-up responsibility.

A concise opening without a guessed diagnosis | A referrer practices the order of an urgent report. | Referrer | Cardiologist
I am handing over current chest pressure with breathlessness, and the emergency response is already active.
That opening gives the concern and action. What verified information is available next?
I can provide the patient account, but I do not have confirmed measurements in this report.
Please state that limitation rather than fill the gap with normal or stable.
Should I begin with the patient's entire remote medical history?
Lead with the current priority, then include the relevant background without delaying care.
I also need to confirm which team is accepting responsibility for the transfer.
Yes. A sent message alone does not establish an accepted handoff.
I will preserve the unresolved cause rather than use a diagnosis to sound decisive.
That is clearer and more accurate while the actual clinical assessment continues.
""")
LESSONS['module-2'] = short_lesson(BOOK['units'][1], """
A symptom diary needs a usable time | A clinician clarifies an ambiguous diary entry. | Patient | Cardiologist
My diary says the episode happened at seven, but I did not write morning or evening.
We need to clarify that before matching the report with the recording.
I thought the device marker would automatically tell you everything about how I felt.
The marker identifies a time; your description adds the sensation and relevant activity.
Could I describe the event without deciding that it was an arrhythmia?
Yes. A symptom account and the interpreted rhythm are different kinds of information.
I remember the activity clearly, but I am less certain about the exact minute.
Keep that uncertainty visible rather than invent a precise time.
Then the diary helps the review without becoming a diagnosis by itself.
Exactly. We compare the actual recording with the best accurate account you can provide.

A marker is not an emergency call | A patient checks the device's role. | Patient | Monitor clinician
If I press the event marker during a concerning symptom, does that contact emergency help?
You must not assume that. The marker's function and the service's actual arrangements need explanation.
I thought someone might be watching every marked event immediately.
The team should explain the real monitoring and review process, including its limits.
Then urgent symptoms need the actual urgent-care route rather than waiting for a routine report.
Correct. Follow the real clinical instructions supplied for your situation.
Could you show me the device-specific instructions rather than use a generic explanation?
Yes. Controls, restrictions, and transmission arrangements can differ between devices.
I also want to know whom to contact if the equipment stops recording.
We will distinguish the technical support route from urgent clinical assessment.

An artifact needs technical review | Two clinicians discuss an uncertain segment of a recording. | Reviewing clinician | Cardiologist
This segment contains signal distortion, and I do not want it described as a confirmed rhythm abnormality.
Please identify the limitation and the relevant recording interval for the actual review.
The patient's diary mentions movement around the same time, but that does not settle the cause.
Agreed. Context can help without replacing assessment of the trace itself.
I will distinguish a possible artifact from an established clinical finding.
That distinction should remain visible when we explain the result to the patient.
Does an uninterpretable segment prove the rhythm was normal during that period?
No. Missing usable information cannot establish either a normal or abnormal rhythm.
We should explain what the recording can support and any important limitation.
Exactly. A clear report does not hide uncertainty behind a confident-sounding label.
""")
LESSONS['module-3'] = short_lesson(BOOK['units'][2], """
A pumping percentage is not living tissue | A patient clarifies an echocardiogram term. | Patient | Cardiologist
I thought the ejection-fraction percentage meant how much of my heart was still alive.
It describes a pumping proportion, not a percentage of living heart muscle.
Could you explain what is being compared in that proportion?
It relates the blood expelled by the ventricle to the relevant volume before contraction.
Then an amount of blood per beat would be a different measurement.
Yes. Stroke volume is an amount, while ejection fraction is a proportion.
Does that one proportion describe every aspect of how the heart works?
No. Filling, valves, structure, symptoms, and other findings also need consideration.
I would like the actual report explained without treating the number as a complete health score.
That is the right distinction: an important measurement, interpreted within the whole assessment.

Preserved does not mean every function is normal | A clinician corrects an overbroad inference. | Cardiologist | Patient
You asked whether preserved ejection fraction excludes every possible heart problem.
I assumed preserved meant the entire heart assessment was normal.
It describes that measurement category, not every aspect of cardiac structure or function.
Does it also rule out heart failure by itself?
No. Heart failure requires the actual clinical assessment and may occur with preserved ejection fraction.
Then the wording should not be shortened to nothing can be wrong.
Correct. We need to discuss what the report establishes and what it does not.
I also want the valve and filling findings explained separately.
Those belong in the full interpretation rather than being absorbed into one percentage.
That helps me understand why a reassuring-sounding label still needs context.

A comparison has an image-quality limitation | Two clinicians discuss a follow-up scan. | Imaging clinician | Cardiologist
The current examination has a relevant image-quality limitation that affects the comparison.
Please keep that visible rather than present the numerical difference as unquestionably meaningful.
The earlier study used a different acquisition context, which also needs review.
Then we should establish comparability before describing a definite change in function.
The report can state the actual measurements and the limitations of interpretation.
That gives the patient a clearer explanation than either ignoring the numbers or overstating them.
Should we explain that a precise-looking value can still have uncertainty?
Yes. Numerical precision on a screen does not eliminate measurement limitations.
I will identify what the comparison supports and what remains unresolved.
We can then discuss the actual clinical implications without manufacturing certainty from two numbers.
""")
LESSONS['module-4'] = short_lesson(BOOK['units'][3], """
A calmer heartbeat and stroke prevention | A patient separates two treatment goals. | Patient | Cardiologist
My heartbeat feels calmer, so I thought the stroke-prevention discussion was no longer relevant.
Symptom or rhythm management and stroke prevention address related but different questions.
Could you explain the goals separately rather than assume I understand why each medicine is discussed?
Yes. We should use your actual clinical plan and explain what each part aims to address.
Feeling better does not automatically establish that every risk has disappeared.
Correct. We must not infer a treatment change from the sensation alone.
I want to discuss the actual benefits and harms before making any decision.
That belongs in an individualized assessment, not a universal rule from a symptom description.
Please also make clear that this conversation is not an instruction to stop anything.
Any medicine decision must come from the responsible clinician and your verified plan.

Bleeding concern is not automatic refusal | A clinician invites a specific concern. | Cardiologist | Patient
What worries you most about the proposed stroke-prevention discussion?
I am concerned about bleeding, but I do not want that recorded as refusing every option.
A concern deserves assessment and explanation; it is not automatically an informed refusal.
I would like the risk described with actual context rather than just the word small.
Where relevant figures are available, we should explain the outcome, timeframe, and uncertainty.
Could my prior history change how the options are considered?
The actual clinical history matters and should be reviewed rather than assumed.
I also need to distinguish a possible adverse effect from a certainty that it will happen.
We will explain both benefits and harms without promising zero risk.
That gives me a basis for questions rather than pressure to agree before understanding.

Rate and rhythm are different aims | A patient asks about two common terms. | Patient | Cardiologist
I hear rate control and rhythm control used as though they mean the same thing.
They describe different aims, even though both may appear in an atrial-fibrillation discussion.
Could you explain the distinction without selecting a treatment for me from the terminology alone?
Rate concerns how fast the heart beats; rhythm concerns the pattern or organization of the rhythm.
Then a change in one does not automatically settle every question about the other.
Correct. The actual assessment determines the relevant strategy and its goals.
I also understand that stroke prevention remains a separate discussion.
Yes. We should avoid presenting symptom control as a substitute for that assessment.
Could the summary identify each goal so I can explain the plan accurately?
It should, using the actual agreed care rather than an invented medicine instruction.
""")
LESSONS['module-5'] = short_lesson(BOOK['units'][4], """
An angiogram is not automatically a stent | A patient asks about procedural scope. | Patient | Cardiologist
I thought agreeing to an angiogram meant a stent would definitely be placed at the same time.
A diagnostic examination and a possible intervention are different parts of the discussion.
Could you explain what is actually proposed and what decisions remain conditional?
Yes. The actual procedure plan, findings, options, and consent arrangements need to be clear.
I do not want a possible next step presented as though it has already been selected.
That is important. We should distinguish what is planned from what might be considered.
Will you explain the relevant benefits, risks, and alternatives using my actual circumstances?
That belongs in the appropriate consent discussion, not a generic promise.
I also want to know whom to ask about preparation instructions that seem inconsistent.
We should verify them with the responsible service rather than ask you to guess.

Contrast questions need the actual history | A clinician clarifies an imprecise reaction report. | Cardiologist | Patient
You mentioned a previous reaction around an imaging procedure. What do you remember happening?
I remember feeling unwell, but I do not know which product was involved.
Let us preserve that uncertainty and review the available record rather than invent a substance.
I was worried that saying allergy would automatically answer every preparation question.
The actual reaction history needs assessment; a label alone may not explain the event.
I can describe the timing and symptoms, but not a confirmed cause.
Those details help, provided we distinguish your account from an established causal conclusion.
Could the procedure team clarify the actual implications for the planned examination?
Yes. The relevant clinicians should review the real history and preparation requirements.
Then I will not be asked to decide which precaution applies from a vague memory.

Understanding is not the same as agreement | A patient checks the consent conversation. | Patient | Cardiologist
I can repeat the explanation, but I still have a question before deciding about the procedure.
Understanding the information does not mean you have already agreed.
I want to compare the actual alternatives, including their relevant limitations.
We should explain those in the context of the recommendation and your circumstances.
A signed information sheet should not close the discussion if something remains unclear.
Correct. The consent process includes meaningful explanation and the appropriate decision.
Could you clarify the difference between the expected benefit and a guaranteed outcome?
An expected benefit is an aim or supported possibility, not a promise of success.
Then we can document what is understood and what decision has actually been made.
Yes. The record should not infer authorization from a nod or a completed form alone.
""")
LESSONS['module-6'] = short_lesson(BOOK['units'][5], """
A home record needs the actual plan | A patient asks how to use monitoring information. | Patient | Cardiologist
I have started a home record, but I do not know which changes the team wants me to report.
The reporting instructions must come from your actual individualized care plan.
I should not borrow a numerical threshold from another patient's leaflet.
Correct. A general example is not automatically the instruction appropriate to you.
Could we review what is recorded, when, and through which contact route?
Yes. The real plan should distinguish routine information from concerns requiring prompt assessment.
I also want to know who reviews the record rather than assume it is constantly watched.
We should explain the actual review arrangements and their limits.
Then recording information will support care without becoming a substitute for the clinical instructions.
Exactly. A usable record needs a clear purpose, verified plan, and responsible contact.

A practical barrier is not a character judgment | A patient explains difficulty following a home-care instruction. | Cardiologist | Patient
Which part of the agreed home plan has been difficult to carry out?
The timing conflicts with my work, and I have not managed it consistently.
Thank you for explaining the barrier rather than letting the record imply everything is straightforward.
I worry that difficulty will be labeled noncompliance without the practical reason.
We should describe what happened and review the actual plan with you.
I do not want to invent my own medicine adjustment to solve the scheduling problem.
Any change needs the appropriate clinical review rather than an improvised substitution.
Could we identify what flexibility, if any, is actually available?
Yes. We should verify the options rather than promise a change before assessment.
That would make the next discussion specific and useful instead of simply repeating the instruction.

Routine messages and urgent concerns differ | A clinician checks the patient's understanding of contact routes. | Cardiologist | Patient
Please explain how you understand the difference between routine follow-up and an urgent concern.
The routine inbox is for the matters specified in my plan, not a guarantee of immediate assessment.
That is important. The actual urgent-care instructions must remain separate.
I should not wait for a routine reply if the real plan says to seek urgent help.
Correct. A submitted message does not establish that a clinician has reviewed it.
Could we check the contact details together rather than rely on an old leaflet?
We should verify the current service information and who responds through each route.
I also need language support for understanding the written plan.
We can arrange the appropriate support and check the explanation again.
Then the plan can be practical rather than merely a document I possess.
""")
LESSONS['module-7'] = short_lesson(BOOK['units'][6], """
The denominator changes the meaning | A clinician checks a fictional numerical comparison. | Cardiologist | Patient
In this fictional example, the same outcome occurs in forty versus thirty people per thousand over five years.
So the absolute difference is ten people per thousand over that period.
Correct. Both groups use the same outcome, denominator, and timeframe.
That is four percent versus three percent, a one-percentage-point absolute reduction.
Yes. The relative reduction is twenty-five percent compared with the original forty.
I can see why saying twenty-five percent alone might sound larger than the absolute change.
Both descriptions can be correct, but they answer different comparison questions.
These are teaching figures, not evidence about a medicine I should take.
Exactly. No personal treatment recommendation follows from the fictional arithmetic.
A clear explanation should state the numbers and their context rather than only the most impressive percentage.

Relative change stays the same while absolute change differs | A patient works through a second fictional comparison. | Patient | Cardiologist
In another fictional example, the outcome changes from twenty to fifteen people per thousand.
The absolute difference is five per thousand, provided the outcome and timeframe match.
That is two percent versus one and a half percent.
Yes, an absolute reduction of half a percentage point.
The relative reduction is still twenty-five percent because five is a quarter of twenty.
Correct. The relative percentage matches the earlier example, but the absolute reduction is smaller.
So an identical relative reduction does not imply an identical number of people affected.
Exactly. The starting frequency matters when explaining what the difference means.
We should not transfer these invented figures to a real person's prognosis.
They are language and arithmetic practice, not a clinical risk estimate.

A percentage needs a named outcome | Two clinicians revise an unclear risk statement. | Clinician | Cardiologist
The draft says risk falls by thirty percent, but it does not name the outcome or period.
That statement is incomplete. We need the actual outcome, baseline frequency, comparison, and timeframe.
It also fails to say whether thirty percent is relative or absolute.
That distinction can change the listener's understanding substantially.
We should not fill the missing numbers from memory merely to make the sentence sound finished.
Correct. Verify the source and explain its uncertainty and relevance to the actual discussion.
If the data are unavailable, the limitation should be stated rather than hidden.
Yes. A precise-looking percentage is not useful when the comparison remains undefined.
The revised explanation will use verified figures and comparable denominators where available.
Then the patient can understand the claim instead of being persuaded by an isolated number.
""")
LESSONS['module-8'] = short_lesson(BOOK['units'][7], """
A rehabilitation referral is not an intake visit | A patient asks whether a program has accepted the referral. | Patient | Cardiologist
You sent a rehabilitation referral, so I assumed my first visit had already been arranged.
Sending the referral does not confirm receipt, acceptance, or an appointment.
Could we check which stage is actually complete rather than leave me waiting without a contact?
Yes. We should identify the receiving service and the route for checking progress.
I also want to know what information the program still needs.
That should be clarified through the actual intake process, not guessed from a generic checklist.
Does the referral itself give me an exercise prescription?
No. The appropriate clinical assessment and program plan determine the actual activity instructions.
Then I should distinguish the referral from clearance or a training schedule.
Exactly. We will explain the verified next step without implying that assessment has already happened.

Transport affects attendance | A rehabilitation coordinator discusses an access barrier. | Coordinator | Patient
The program has contacted you about intake. Is there a practical issue we should know about?
Transport is difficult, and I am worried that missing a visit will look like refusing rehabilitation.
We should record the access barrier accurately rather than assume your intention.
I want to attend, but I need to understand the actual scheduling and travel options.
We can check what is available without promising a service before confirmation.
Could you also clarify which contact handles questions about coverage?
Yes. Coverage questions need the appropriate team and your actual arrangements.
I do not want an estimate presented as a guarantee that every visit is paid for.
We will distinguish the estimate, any authorization, and confirmed coverage.
That helps me plan without turning the practical difficulty into a judgment about my motivation.

Returning to work requires a real assessment | A patient asks whether rehabilitation attendance proves work readiness. | Patient | Cardiologist
If I attend rehabilitation, does that automatically mean I am cleared for every task at work?
No. Participation and work readiness are different questions requiring the actual assessment.
My job includes duties that may differ from what another patient does.
The actual job demands matter, along with your clinical situation and relevant professional review.
Could a letter describe a restriction that has not been assessed just to satisfy a form?
It should not. Any clinical statement needs an appropriate factual basis.
I would like the employer process kept separate from a promise about a medical outcome.
That distinction is important, including what information is authorized for sharing.
Then rehabilitation can support recovery without becoming a universal work-clearance certificate.
Exactly. The record should state what is established and which decision still needs the appropriate review.
""")
