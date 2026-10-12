"""Twenty-four separate sports-medicine exchanges for interactive lessons."""
from books.sports_medicine_content import BOOK
from books.specialist_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], '''
A pop is a report, not a diagnosis | An athlete clarifies an injury description. | Athlete | Sports physician
I heard a pop and immediately assumed that a ligament had torn.
The sound is useful information, but it does not identify the injured structure by itself.
I can describe the movement and what happened afterward without naming the diagnosis.
Please do. Which foot was planted, and was there any direct contact at the time?
The right foot was planted, and nobody touched me during the turn.
I will preserve that side and mechanism rather than copy the teammate's suggested label.
The discomfort began during the turn, but I cannot identify the exact instant of the sound.
That uncertainty belongs in the history instead of being replaced by a precise sequence you cannot confirm.
I would like the examination to answer the clinical question rather than my guess becoming the starting diagnosis.
Exactly. Your account informs the assessment; it does not need to arrive with a diagnosis attached.

Gave way needs a description | A clinician unpacks a familiar but ambiguous phrase. | Clinician | Athlete
When you say the ankle gave way, do you mean it moved unexpectedly or that pain made you stop?
Pain made me stop. I did not see it buckle, and I did not fall.
That distinction matters because those descriptions would not mean the same thing in the record.
I used gave way because everyone on the team says it, not because I knew the clinical meaning.
Your wording is a useful starting point. We can clarify it without treating it as wrong.
Should I also describe what I was doing before the discomfort began?
Yes. The activity, timing, side, and any contact help make the history specific.
I can explain those details, but I do not have an examination result yet.
Then we will not describe the joint as stable or unstable based only on this conversation.
That leaves the actual finding for the assessment instead of increasing certainty as the story is retold.

The old injury was on the other side | An athlete corrects a history summary. | Athlete | Clinician
The previous injury in my record was on the left, but today's problem is on the right.
Thank you for correcting that. I will keep the past history separate from the current side.
The first summary seemed to combine them because the sport and movement sounded similar.
Similar circumstances do not make them the same event or the same diagnosis.
I do not have the old imaging report with me, so I cannot confirm its exact wording.
We can request the relevant record through the appropriate route rather than reconstructing it from memory.
Meanwhile, I can describe today's movement and symptoms as accurately as possible.
That will give us a usable current history without copying an old conclusion into it.
Please make sure the corrected side reaches the people who received the earlier summary.
I will follow the correction process and confirm that the relevant team receives the updated information.
''')
LESSONS['module-2'] = short_lesson(BOOK['units'][1], '''
Range is not force | A clinician clarifies an examination term before beginning. | Athlete | Physiotherapist
When you mentioned range, I thought you were asking how much force I could produce.
Range describes how far the joint moves; strength concerns force in the relevant assessment.
Then one number cannot stand in for both of those questions.
Correct. We should explain which aspect is being assessed before discussing a result.
I would also like to know whether I move myself or you guide the movement.
I will explain that before the actual step and confirm that you are comfortable proceeding.
If I am unsure about the wording, can we pause without it being recorded as refusing treatment?
Yes. Asking for clarification is part of a useful examination conversation, not a character judgment.
I would rather understand the instruction than guess what movement you want.
That is appropriate. We will use the actual clinical process and avoid filling gaps through assumptions.

Permission for one step is not permission for everything | An athlete asks about examination consent. | Athlete | Clinician
I agreed to the appointment, but I would still like each examination step explained before it happens.
Of course. Attending does not remove your ability to ask questions, pause, or decline a step.
I sometimes stay quiet because I assume a clinician's schedule leaves no room for questions.
Please tell me when something is unclear. A brief clarification is important to the actual consent process.
Could we also discuss the service's chaperone arrangements before deciding how to proceed?
Yes. I will explain the relevant policy and available arrangements rather than assume your preference.
I do not need a technical lecture, but I want to know the purpose of the next step.
That is a useful request: purpose first, then the explanation relevant to the examination.
If I ask to pause, I want that to mean pause rather than end the whole appointment.
We can clarify that at the time and agree on what happens next without assuming your intention.

A comparison needs the same measurement context | Two clinicians review an examination note. | Physiotherapist | Sports physician
The new range figure differs from the earlier one, but the notes describe different measurement conditions.
Then we should clarify the methods before calling the difference a definite improvement or deterioration.
One entry is an estimate, while the later note identifies an actual measured value.
That distinction should remain visible rather than presenting both numbers as equally precise.
The athlete has asked whether the change means they can compete again.
A measurement comparison is not automatically a complete participation decision; we need the actual review.
I will include the method, source, and conditions in the summary for that review.
Please also separate the athlete's reported experience from the observed examination findings.
Then the receiving clinician can see which information is comparable and where uncertainty remains.
Exactly. Clear measurement language supports the decision without pretending one number settles every question.
''')
LESSONS['module-3'] = short_lesson(BOOK['units'][2], '''
Sets and repetitions were reversed | An athlete asks for clarification of an existing plan. | Athlete | Physiotherapist
I think I reversed sets and repetitions when I repeated the instruction at home.
Let us read the actual current plan together instead of guessing which number belongs where.
A repetition is one complete movement, and a set groups the repetitions under the plan.
Correct. The prescribed quantities still need to come from the verified instruction.
I should not multiply or change them simply because the total seems inconvenient.
Any change needs the appropriate clinical clarification, not an adjustment invented during this conversation.
The older handout also uses different wording, which is part of why I became unsure.
We will identify the governing version and correct the conflicting message through the proper process.
Could I read the clarified instruction back before leaving so we can catch another reversal?
Yes. Read-back checks the explanation and does not require you to invent missing details.

More resistance was only a question | An athlete distinguishes a proposed change from approval. | Athlete | Clinician
At the last session I asked about greater resistance, but I do not think we actually agreed to it.
Then the record must distinguish your question from a prescribed change to the plan.
My own note simply says increase, which now seems too vague to rely on.
We should clarify the exact instruction with the responsible clinician before treating that word as approval.
I can explain what I asked and what I remember hearing without filling the missing part myself.
That is helpful. A question, a proposal, and an authorized change are different stages.
The review appointment is still pending, so the calendar does not resolve the instruction either.
Correct. The current verified plan remains the reference while the ambiguity is addressed appropriately.
I will avoid telling my coach that progression is approved when all I did was ask about it.
That preserves the actual status and prevents the request from becoming a false instruction through repetition.

A home plan was confused with a supervised session | Two clinicians check a handoff. | Receiving clinician | Referring clinician
The handoff says home program, but the attached current plan specifies supervised rehabilitation.
Thank you for spotting that. The attachment is the verified current instruction; the summary needs correction.
I will not combine them into a new arrangement while the discrepancy is being resolved.
Agreed. The supervision requirement must remain visible when the updated message is sent.
Does the athlete already have the shortened summary that uses home program?
Yes, so we need to correct the communication with the athlete as well as the internal record.
Who will own that contact and confirm that the revised instruction was received?
I will, using our actual process and retaining the correction history.
Then the handoff is not complete merely because the attachment was accurate.
Exactly. The person following the plan also needs the verified message, not only a corrected file in our system.
''')
LESSONS['module-4'] = short_lesson(BOOK['units'][3], '''
The school note has a limited purpose | A coach clarifies a return-to-learn update. | Coach | Athletic trainer
The athlete attended class today, and I wondered whether that means unrestricted practice is now allowed.
No. The school arrangement does not itself authorize a different activity with different demands.
The note mentions classroom adjustments, but I had shortened that to back to normal.
That summary loses important limits and should be corrected before the team relies on it.
I will state the actual school arrangement without adding a sport participation decision.
Please also direct the specific practice question to the responsible healthcare professional.
The approaching match explains why people are asking, but it does not supply the answer.
Exactly. Competitive pressure does not replace the actual clinician-led concussion process.
When a new authorization is communicated, we should preserve its activity and conditions.
That will prevent the same confusion from returning when someone uses the word cleared without its scope.

A symptom report should retain its source | Two clinicians discuss an update received through a coach. | Clinician | Athletic trainer
The coach says the athlete felt better yesterday, but I have not received a direct current report.
Then we should attribute the message to the coach and preserve when it was reported.
I should not turn that into a verified statement that every symptom has resolved today.
Correct. Source, timing, and the actual clinical assessment remain important.
The update also contains no symptom inventory or examination results for us to review.
Missing results must not be presented as normal findings or as clearance for a new activity.
I will use the appropriate clinical contact route to clarify the current position.
Please keep the actual concussion and emergency procedures separate from this routine communication update.
The team needs to know what is authorized, not infer it from a secondhand reassuring phrase.
Exactly. We can acknowledge the report without increasing its certainty or widening the participation permission.

A request to advance is not approval | An athlete checks the status of a return-to-sport question. | Athlete | Clinician
I asked whether I could move to the next activity, but the team recorded that progression was approved.
We need to correct that distinction. Asking a question does not mean authorization has been given.
I do not want the coach planning around permission that was never actually communicated.
We will use the clinical process to clarify the current activity and correct the inaccurate message.
Should I describe the request as pending while the responsible professional reviews it?
Yes, without predicting the outcome or naming a date that has not been agreed.
The school adjustments remain a separate part of the overall plan.
Correct. They should not be treated as automatic authorization for contact practice or competition.
I will read back the actual participation information when the review outcome is communicated.
That will help preserve the scope and conditions instead of letting a short summary broaden them.
''')
LESSONS['module-5'] = short_lesson(BOOK['units'][4], '''
Minutes match but the effort does not | An athlete reviews two training records. | Athlete | Clinician
I described the sessions as identical because both lasted the same number of minutes.
The duration matches, but one record describes easy activity and the other hard intervals.
Then same duration is a narrower claim than same overall training demand.
Exactly. Name the dimension you are comparing instead of letting same cover every aspect.
I also need the recovery periods to describe the interval session accurately.
Yes. The broad session label does not replace its actual structure or recorded details.
My effort rating is a personal report, while the equipment records a different measure.
Those sources should remain identifiable rather than being merged into one unexplained number.
I will revise the summary without turning the comparison into an injury prediction.
That makes it useful for the actual review while respecting what the records cannot establish.

The effort scales differ | Two colleagues compare athlete logs. | Coach | Sports clinician
Both athletes entered a seven, so I assumed they reported exactly the same level of effort.
Were they using the same scale, anchors, and recording method for that number?
One used the team's current scale, while the other copied a different app's format.
Then the matching numeral does not guarantee an equivalent reported rating.
We should preserve the original entries and clarify the method before comparing them.
Correct. Do not silently convert the figures using an assumption nobody has checked.
The logs also describe different sports, which adds another context difference.
That matters too. A comparison needs its purpose and relevant conditions made explicit.
I will explain the limitation instead of claiming the numbers establish equal readiness.
Good. The ratings can inform a review without becoming a stand-alone clinical authorization.

The device estimate changed after an update | An athlete asks about a wearable dashboard. | Athlete | Clinician
My device's recovery estimate changed after a software update, although my activity record was unchanged.
We should clarify what the device measures and whether its method or presentation changed.
I had been treating the number as if it were a clinician's clearance decision.
It is a device estimate, not a replacement for the actual clinical process.
Could the trend still be worth discussing if I describe the update and other context?
Yes, provided the source and limitations stay visible rather than being hidden by the graph.
I should also report my actual experience instead of relying on the dashboard alone.
That provides a more complete account without assuming the device explains every change.
Then the summary can say the displayed estimate changed, not that my injury definitely changed.
Exactly. Keep the observation separate from the clinical interpretation it does not establish by itself.
''')
LESSONS['module-6'] = short_lesson(BOOK['units'][5], '''
Possible became definite in the handoff | Two clinicians correct an imaging summary. | Receiving clinician | Referrer
The report describes a possible explanation, but the summary presents it as the confirmed cause.
That is stronger than the source supports. I will correct the certainty in the summary.
Please retain the request for clinical correlation rather than dropping it to shorten the message.
Agreed. The actual history and examination still need to be connected with the imaging finding.
The athlete has already received the shorter version and is worried it means treatment is settled.
Then the correction needs to reach the athlete, not only the internal referral record.
We should also distinguish the structural description from the participation decision.
Yes. Neither a report phrase nor a summary should quietly become clearance for sport.
I will acknowledge the corrected message and identify what remains unresolved for the review.
That closes the communication loop without pretending the correction itself supplies a new clinical finding.

Incidental does not mean automatically irrelevant | An athlete asks about an unfamiliar report word. | Athlete | Sports physician
I read incidental and assumed I could ignore that part of the report entirely.
It means the finding was outside the main question prompting the examination, not automatically unimportant.
Then I need an explanation of its actual significance rather than a dictionary shortcut.
Exactly. The relevant professional should interpret it in the context of the actual report and assessment.
I also should not assume that an unfamiliar word means the worst possible outcome.
Correct. The emotional effect of a term is not the same as its clinical meaning.
Could we identify which questions the image answered and which questions remain open?
That is a useful way to organize the discussion and keep the limitations visible.
I would like the explanation linked to my actual situation rather than a generic promise.
We can do that without converting this single phrase into a diagnosis, treatment decision, or sport authorization.

The screenshot omitted the limitation | An athlete shares only part of an imaging report. | Athlete | Clinician
I sent the coach a screenshot of the conclusion, but it did not include the report's limitation.
That can change how the conclusion is understood, especially when the cropped text looks more certain.
The report also referred to an earlier comparison study that was not visible in the image.
Then the relevant context should be restored through the appropriate communication process.
I do not want to forward the entire chart just to correct the screenshot.
We should clarify what information can be shared and with whom under the actual authorization.
The coach mainly needs the verified participation information, not an independent interpretation of the image.
Exactly. A cropped report should not become an informal route to a sport-clearance decision.
I will correct the message and direct the clinical question to the responsible professional.
That preserves both the report's meaning and the proper limits of the information exchange.
''')
LESSONS['module-7'] = short_lesson(BOOK['units'][6], '''
The calendar does not supply the criterion | An athlete asks about a competition deadline. | Athlete | Sports physician
The tournament entry closes Friday, so I need a definite answer about playing before then.
I understand the practical pressure, but that deadline does not establish the clinical criteria.
Could you explain the present status without promising a result that is still pending?
Competition is not yet authorized, and the actual review must determine what can be permitted.
I can tell the coach that clearly even though it may affect selection.
Yes. Clinical authorization and team selection are related concerns but separate decisions.
I do not want a hopeful target date repeated as a guaranteed recovery date.
Then label it as a goal or scheduling question, not an established outcome.
When the review is complete, I would like the permitted activity and conditions stated explicitly.
That will give the team usable information without relying on the single ambiguous word cleared.

Everyday confidence differs from sporting confidence | An athlete discusses fear of reinjury. | Athlete | Clinician
I feel comfortable walking around, but a full-speed sporting movement still makes me hesitate.
Those demands differ, and your concern deserves a specific discussion rather than a character judgment.
I worried that mentioning fear would make the team think I lacked commitment.
Psychological readiness can be discussed respectfully alongside the other relevant assessment information.
It should not be treated as proof that a structure is injured again, should it?
No. A feeling and a structural diagnosis are different kinds of information.
I can describe the movement that concerns me without trying to test it on my own.
That will help the responsible team understand the question within your actual clinical plan.
The goal is a clear account of readiness, not a performance of confidence for the appointment.
Exactly. Accurate communication is more useful than hiding uncertainty to satisfy an expected answer.

Limited practice was reported as full performance | Two team staff correct a participation message. | Coordinator | Clinician
The update says the athlete has returned to performance, but the note only allows specified limited participation.
That summary overstates both the permission and what has been established about performance.
I will restore the actual activity and conditions rather than use a broad celebratory phrase.
Please also identify who received the inaccurate version so the correction reaches the right people.
The distinction is not just stylistic; it affects what the coach may expect in practice.
Correct. Different demands and permissions should not collapse into a single return label.
No competition authorization or previous-performance level is established by this note.
Then neither should appear in the corrected team message as an assumed fact.
I will confirm receipt and keep the review status visible in the next update.
That makes the information useful without increasing certainty as it moves between roles.
''')
LESSONS['module-8'] = short_lesson(BOOK['units'][7], '''
The planning question needs a narrower update | A coordinator explains why a record was requested. | Clinician | Coordinator
Before sharing information, what decision are you trying to make with the complete chart?
I need to arrange practice around the athlete's authorized participation limits.
Then let us clarify the permitted participation update rather than assume the entire chart is necessary.
That would answer the task without giving me unrelated historical details.
We still need to verify the recipient, purpose, and actual authorization under our applicable process.
I will identify the staff who need the information instead of forwarding it to a broad group.
Please also use the approved route for the update, not whichever app happens to be open.
Understood. Technical ability to send a file does not establish permission to disclose it.
Exactly. A useful message can remain limited and accurate at the same time.
I will wait for the verified scope rather than invent a diagnosis or restriction to fill the gap.

A sponsor is a new recipient | A team liaison checks a proposed forwarding request. | Team liaison | Clinician
The sponsor asked for the health update we received, but the athlete's authorization named only our liaison role.
Then you should not assume the same authorization covers an external sponsor and a different purpose.
I can explain that we need to check the actual permissions before sharing anything further.
Yes, without disclosing the contents merely to justify why you are not forwarding them.
The sponsor's interest in availability does not automatically create access to clinical details.
Correct. A legitimate business question and a permitted health-information disclosure are not identical.
Could an authorized public availability statement be handled through the actual communications process?
That question should go through the responsible process with the athlete's rights and applicable rules respected.
I will keep the existing limited update within its approved recipient group for now.
That preserves the boundary while the appropriate people clarify whether any different communication is authorized.

Correcting the message without spreading the record | A coordinator discovers an outdated participation update. | Coordinator | Clinician
An assistant is still using the old participation message, although the current authorized update is different.
We need to correct the operational information through the approved channel and identify who received the old version.
I do not need to attach the full clinical record to prove that the update changed.
Correct. Share the actual authorized information relevant to the task, not unrelated details.
The new message should show its status and source clearly so the older one is not mistaken for current guidance.
Please also retain the relevant correction history under the information-handling process.
I will confirm that the people planning practice have received the current update.
That confirmation matters; a sent correction is not always a received and understood correction.
The athlete's privacy and the team's practical planning both depend on getting this right.
Exactly. Clear scope and closed communication make those responsibilities compatible rather than competing by default.
''')
