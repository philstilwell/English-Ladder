"""Twenty-four original short general-practice conversations."""
from books.general_practitioners_content import BOOK
from books.medical_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], """
A second concern before the door closes | A patient adds an issue while the agenda is being agreed. | Patient | GP
I came about my shoulder, but there is another issue I nearly forgot to mention.
Please tell me what it is before we agree on the priorities for today.
I also need a form signed, although the shoulder is what worries me.
Let us separate the clinical concern from the form and check what each requires.
Does mentioning the form mean we will have no time for the shoulder?
No. We need to understand the priorities rather than assume the paperwork comes first.
I would prefer to discuss the pain before deciding how to handle the document.
That preference helps. I will explain what can be addressed and any follow-up needed.
So we are agreeing on an agenda, not promising that everything is completed today.
Exactly. We will make the next steps clear rather than leave the unfinished item unmentioned.

The referral letter has a different priority | A clinician checks the patient's reason for attending. | GP | Patient
The referral mentions tiredness, but I want to hear what matters most to you today.
The tiredness is important, but I mainly want to understand the recent test message.
Thank you. The referral gives background; it does not replace your account of this visit.
I worried that asking about the message would seem unrelated to the appointment.
It belongs on the agenda. Let us identify the questions before choosing the sequence.
I want to know what the result means and who is responsible for the next step.
We can review the actual result and distinguish its interpretation from the follow-up arrangements.
Please tell me if something requires a separate discussion rather than leaving it vague.
I will. An agreed follow-up should name the issue and the responsible service.
That makes the visit feel organized without pretending the referral captured every concern.

A routine review with an access barrier | A patient explains why an earlier appointment was missed. | Patient | GP
I missed the previous review because my shift changed, not because I thought it was unnecessary.
Thank you for explaining. I will record the access difficulty rather than assume refusal.
I can attend some mornings, but I cannot promise availability at the same time every week.
Let us clarify the actual scheduling options and what follow-up is clinically required.
Does that mean you can guarantee an appointment outside all my work hours?
I cannot guarantee a slot before checking, but we can identify the practical constraint.
I would appreciate knowing whom to contact if the offered time is impossible.
We will confirm the appropriate contact and the actual arrangements for the next review.
So a missed appointment does not tell you what I believe about the care.
Correct. The reason needs clarification, and the next plan needs to be workable.
""")
LESSONS['module-2'] = short_lesson(BOOK['units'][1], """
Dizzy does not yet describe the sensation | A clinician clarifies an ambiguous symptom word. | GP | Patient
When you say dizzy, what does that feel like in your own words?
Sometimes it feels as though the room moves, but sometimes I mean that I feel faint.
Those are different descriptions, so let us keep the episodes separate while we clarify them.
I thought I needed one medical word before I could explain the problem properly.
Your description is useful. We should not force different experiences into one label.
Do you want to know how long each episode lasts or how often it happens?
Both, but one question at a time: how long is different from how often.
I can describe a recent episode, although I have not timed every occurrence.
Please distinguish what you remember from anything you measured rather than guessing a precise number.
Then the history can stay accurate even when I cannot give perfect timing.

An onset date is corrected | A patient corrects the timeline before it enters the record. | Patient | GP
I said the cough began on Monday, but that was when I first called the clinic.
Thank you for correcting it. When do you recall the symptom actually beginning?
I noticed it over the weekend, although I cannot identify an exact hour.
I will record the approximate onset separately from the date of the call.
Does changing my answer make the history less trustworthy than leaving the first date?
No. A clear correction improves the account; keeping a known error would be less useful.
I also want to distinguish the first mild symptom from when it became more noticeable.
That distinction matters. Onset and worsening are different points in the timeline.
Please read the summary back so I can check that those points remain separate.
I will, and we will preserve the uncertainty instead of inventing an exact time.

A symptom changes with context | A clinician asks about circumstances without assuming a cause. | GP | Patient
You mentioned that the discomfort is more noticeable at work. What changes in that setting?
I stand longer there, but I do not know whether standing is actually the cause.
That is a useful distinction: association with a setting does not prove the explanation.
I was concerned that you might write occupational injury before assessing what happened.
I will document your account and investigate the relevant context without assigning an unsupported cause.
At home I sometimes notice it too, so work is not the only setting.
Let us include that detail rather than describe the symptom as occurring exclusively at work.
Would a description of the activity be more useful than guessing which diagnosis fits?
Yes. Explain what you were doing, what you felt, and how the episode changed.
Then we can keep the history specific without treating my theory as a confirmed finding.
""")
LESSONS['module-3'] = short_lesson(BOOK['units'][2], """
An allergy label needs clarification | The medicine record contains an imprecise reaction entry. | Patient | GP
My record says allergy, but I remember nausea rather than a rash or breathing problem.
Let us clarify what happened and when, without changing the label casually.
Does that mean you are saying it definitely was not an allergy?
No. Your description needs appropriate clinical review before the record is amended.
I can explain the symptoms, but I do not remember the exact product name.
We should preserve that uncertainty and check the available records rather than guess.
I also took another medicine at the time, which might matter to the review.
Please include that context, while keeping an association separate from a proven cause.
So we will document the actual reaction history and ask the responsible team to review it.
Exactly. A precise account is more useful than either retaining or removing a label without assessment.

A supplement is missing from the list | A patient asks whether a nonprescription product belongs in reconciliation. | GP | Patient
Is there anything you take that does not appear on this list, including supplements?
I use a herbal product, but I did not think it counted as medicine.
It belongs in the review. Please bring the actual product information rather than a guessed name.
I assumed natural meant it could not affect anything prescribed by the clinic.
That assumption is not reliable; the actual ingredients and clinical context need checking.
I cannot remember the amount, and the packaging is at home.
Then we will record that it remains unverified rather than invent a dose.
Should the list distinguish what I currently take from something I stopped months ago?
Yes. Current use, past use, and an unverified product are different statuses.
I can see why a complete list means more than copying the prescription screen.

Cost changed what was actually taken | A clinician clarifies a gap between prescription and use. | Patient | GP
The prescription list says I take it regularly, but cost has made that difficult.
Thank you for saying so. A prescription record is not proof of actual use.
I was afraid the note would simply say noncompliant without explaining the problem.
We should describe the access barrier and what happened, not substitute a judgment.
I do not want to change the medicine on my own to make it last longer.
Any change needs the responsible clinical review, not an improvised adjustment.
Could someone help check the actual assistance or coverage options available to me?
We can identify the appropriate support route without promising approval before it is verified.
Please also make sure the record distinguishes the intended plan from what I could obtain.
That distinction belongs in reconciliation and in the discussion of the next safe clinical plan.
""")
LESSONS['module-4'] = short_lesson(BOOK['units'][3], """
The portal flag is not the whole result | A patient asks about a result marked outside range. | Patient | GP
The portal highlighted one result in red, and I assumed that meant a serious diagnosis.
The flag indicates a comparison with a reference range; interpretation needs the actual context.
Does being outside the range always mean the same thing for every test?
No. The test, degree of difference, history, and other findings can matter.
I would like you to explain this result rather than reassure me from the color alone.
That is appropriate. We should discuss what the result can and cannot establish.
I also noticed an earlier value, but I do not know whether the tests are comparable.
We need to check that before describing a meaningful change.
So the display helps me notice the result, but it does not explain the diagnosis.
Exactly. We will use the actual report and clinical assessment rather than the portal's color.

A repeat request needs a purpose | A patient asks why another sample is proposed. | GP | Patient
The team has requested another sample, and I want to explain the actual reason clearly.
I thought a repeat meant the first result must have been wrong.
Not necessarily. We need to distinguish checking a finding from declaring the first result invalid.
Could you tell me what question the repeat is intended to answer?
Yes. The explanation should connect the actual request to the clinical question.
I do not want to assume that repeating the test guarantees a normal result.
It cannot guarantee that. The possible findings and next discussion still require review.
Who will explain the result once the new sample has been processed?
We should identify the responsible clinician and the actual contact arrangements.
That gives me a purpose and a follow-up route without predicting the result.

A comparison uses a different laboratory | A clinician checks whether two reported values can be compared directly. | Patient | GP
These two results look different, but they came from different laboratories several months apart.
We should check the units, methods, reference information, and clinical context before interpreting the difference.
I nearly subtracted the numbers and described the answer as a definite deterioration.
That arithmetic alone would not establish what the change means clinically.
One report also uses an abbreviation that is absent from the other.
Let us clarify the actual test names rather than assume the labels are interchangeable.
Would the dates and any relevant circumstances around sampling belong in the discussion?
Yes. A comparison needs more than two isolated numbers placed beside each other.
So we can acknowledge the apparent difference without declaring a diagnosis from it.
Correct. We will explain the reviewed comparison and preserve any important limitation.
""")
LESSONS['module-5'] = short_lesson(BOOK['units'][4], """
A previous improvement is not proof of cause | A patient links an antibiotic to recovery in an earlier illness. | Patient | GP
I improved after antibiotics last time, so I assumed they caused the recovery.
Improvement afterward describes the sequence, but it does not by itself prove the cause.
Are you saying that my memory of getting better is wrong?
No. The improvement can be real while its explanation still needs careful interpretation.
I want to understand today's recommendation rather than repeat last year's decision automatically.
That is the right question: today's assessment and indication determine the recommendation.
Could you explain the reasoning without making me feel foolish for asking?
Certainly. We should discuss the actual findings, expected benefit, and possible harms.
I also need the follow-up advice that belongs to today's clinical plan.
We will explain that plan and its contact route without assuming every similar symptom has the same cause.

A prescription request from a colleague | Two clinicians clarify the basis of an antibiotic request. | Clinician | GP
The patient asked whether we could repeat the antibiotic from a previous encounter.
What is the current assessment and indication, rather than the earlier prescription alone?
The request is documented, but the clinical decision has not yet been made.
Then please keep patient request separate from clinician recommendation in the record.
I should not write antibiotic required simply because the patient asked for one.
Correct. That wording would convert a request into a conclusion unsupported by the assessment.
Would you like the previous reaction history included in the review as well?
Yes, with its source and certainty clear, alongside the actual current findings.
I will send the verified information and identify what is still unknown.
Then the responsible clinician can explain the decision using evidence, not a copied instruction.

Understanding a no-antibiotic recommendation | A patient checks the explanation of an assessed recommendation. | GP | Patient
After the actual assessment, my recommendation is not to use an antibiotic for this episode.
I would like to understand that recommendation, not just hear that the answer is no.
Let us discuss the assessed reason and what benefit an antibiotic would or would not offer here.
Does the recommendation mean that my symptoms are imaginary or unimportant?
No. Taking your symptoms seriously and recommending an antibiotic are not the same thing.
I also want to know what the actual care plan says if the situation changes.
We will review the relevant follow-up instructions and the appropriate contact route.
Please check that I have understood the plan rather than assuming my nod means agreement.
Tell me how you understand the recommendation, and I will clarify anything I explained poorly.
Then I can distinguish the treatment decision from whether my concern has been heard.
""")
LESSONS['module-6'] = short_lesson(BOOK['units'][5], """
An invitation is not a diagnosis | A patient receives a screening invitation. | Patient | GP
The screening invitation worried me because I thought the service had already found something wrong.
An invitation offers a screening discussion; it is not a diagnosis or an abnormal result.
Then the first question is what this particular screening test is intended to detect?
Yes, along with its possible benefits, limitations, and the choices available to you.
I would like to know what could happen after either a positive or negative result.
Those pathways belong in the explanation, using the actual screening program.
Does accepting the invitation mean I have agreed to every possible later procedure?
No. Later decisions may require their own information and appropriate consent discussion.
I appreciate separating the invitation, the test, and any later diagnostic assessment.
That sequence helps you make an informed choice without assuming the result in advance.

A false alarm and overdiagnosis differ | A clinician explains two different screening limitations. | GP | Patient
You asked whether a false-positive result and overdiagnosis mean the same thing.
I assumed both meant that the test found something that was not really there.
A false positive is not confirmed as the condition being assessed.
So overdiagnosis must refer to a different problem than an unconfirmed alarm?
Yes. It concerns detecting a real condition that would not have caused relevant harm.
That sounds different because the finding may be real even when detection does not help.
Exactly. The terms describe different limitations and should not be used interchangeably.
Can we discuss their relevance to the actual screening option rather than every test together?
We should use the particular program's evidence and explain the uncertainty honestly.
Then I can compare the possible benefits and harms using the correct meanings.

Declining today is not refusing all future care | A patient postpones a screening choice. | Patient | GP
I do not want to decide on screening today, but I am not refusing every future discussion.
I will record that accurately rather than describe your choice as a blanket refusal.
I need the information in a form I can understand before making a decision.
We can review the actual option, its limitations, and any relevant timing considerations.
Could you also explain whether the invitation is screening or follow-up for an existing concern?
That distinction matters, and we should verify which process this invitation belongs to.
I do not want a postponement recorded as though the test was already completed.
It should not be. Offered, accepted, declined, and completed are different statuses.
Once the actual information is clear, we can discuss the next step appropriately.
Yes. The record should reflect the decision actually made, not one inferred from silence.
""")
LESSONS['module-7'] = short_lesson(BOOK['units'][6], """
A direct safety question | A clinician explains why a sensitive question is being asked. | GP | Patient
I would like to ask directly whether you have had thoughts of ending your life.
I appreciate the clear wording, although it is difficult for me to answer.
Take the space you need within the actual assessment. The question is not a judgment.
Will an honest answer automatically be reduced to a label without hearing the context?
Your account needs proper assessment, including relevant details and the actual safety response.
I also want to understand the limits of privacy before sharing more.
We should explain the applicable confidentiality and safety duties rather than promise absolute secrecy.
I do not want to be reassured or classified from one sentence alone.
That would not be sufficient. The clinical assessment and appropriate support remain essential.
Clear questions and an explanation of the process make it easier to describe what is happening.

Low mood and a diagnosis are different | A patient asks how symptom language relates to assessment. | Patient | GP
I have described low mood, but I do not know whether that establishes a diagnosis.
A symptom report contributes to assessment; it does not replace the full clinical evaluation.
I was worried that using the wrong word would make you misunderstand the seriousness.
Please describe your experience, its course, and its effect rather than choosing a label for me.
Some days are different from others, so a single word feels incomplete.
That variation belongs in the account, with uncertainty preserved where you are unsure.
Could we distinguish what I experience from what someone else has noticed?
Yes. Both can be useful, but each source should remain identifiable.
I would also like to know the actual next step after this discussion.
We will explain the appropriate assessment and support plan without diagnosing from vocabulary alone.

A warm handoff needs acknowledgment | Two clinicians coordinate the next support contact. | GP | Receiving clinician
The patient has agreed to this referral, and I am confirming the receiving contact.
I can acknowledge the referral information, but we should clarify the actual next appointment arrangement.
The patient should not assume that sending the request means a visit is already booked.
Agreed. Receipt, acceptance, and appointment confirmation need to remain separate.
I will include the relevant concerns and actual safety arrangements without unnecessary personal detail.
Please preserve what is reported, what was assessed, and what remains unresolved.
Who will explain the next step to the patient and check any access difficulty?
Let us assign that responsibility explicitly rather than leave it between the two services.
I will document the accepted handoff and the outstanding scheduling information.
That closes the communication loop without pretending the whole care pathway is already complete.
""")
LESSONS['module-8'] = short_lesson(BOOK['units'][7], """
The referral went to the wrong service | A coordinator identifies a routing problem. | Coordinator | GP
The receiving service says this referral belongs elsewhere and has not accepted the patient.
We need to verify the correct route rather than mark the referral as completed.
The original request was sent successfully, but that did not establish acceptance.
Exactly. Sent, received, accepted, and booked are different stages in the process.
Who should review the clinical priority while the routing issue is resolved?
The responsible clinician must use the actual case, not infer urgency from administrative delay.
I will keep the task open and record which service responded.
Please also identify who will contact the patient with the corrected arrangements.
We should not leave the patient believing an appointment is already on its way.
Agreed. Accurate status and named responsibility matter as much as transmitting the document.

The patient has heard nothing | A patient asks about an unconfirmed referral. | Patient | GP
I was told a referral would be sent, but I have not heard about an appointment.
Let us check the actual status rather than assume that no news means it was accepted.
I do not know whether it was sent, received, or reviewed by the service.
Those are separate stages, and we should explain which one is confirmed.
Could you tell me who is responsible for checking with the receiving team?
We will identify that person and the actual follow-up route.
I also need to know which clinical instructions apply while the appointment is unresolved.
Those must come from your actual care plan, not a guessed waiting period.
Thank you. I want a clear next contact rather than another vague instruction to wait.
We will confirm the arrangement and keep any unresolved step visible.

A specialist response needs patient explanation | A clinician receives advice that has not reached the patient. | Specialist | GP
I have sent the reviewed recommendation, but I have not discussed it directly with the patient.
Thank you. We should not treat the letter's arrival as completed patient communication.
Please distinguish the recommendation from any decision that still needs an informed discussion.
I will review the actual advice and explain the relevant next step with the patient.
There is also a question that the available information did not resolve.
We will preserve that limitation rather than present the response as a complete answer.
Can you confirm who owns the follow-up after the explanation?
I will clarify responsibility under our actual clinical process and acknowledge any further referral.
Then the recommendation will not remain an unread attachment with an assumed outcome.
Correct. Receipt, interpretation, patient discussion, and agreed action each need their own accurate status.
""")
