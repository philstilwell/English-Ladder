"""Twenty-four original short oncology conversations."""
from books.oncologists_content import BOOK
from books.medical_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], """
A diagnosis before the staging discussion | A patient separates what is confirmed from what is pending. | Patient | Oncologist
I heard the word malignant, but I could not take in the rest of the explanation.
The tissue assessment confirms cancer. We can pause before discussing what is still being investigated.
Does that confirmation also tell you exactly where it has spread?
No. Diagnosis and staging answer different questions, and the stage is not established here.
I would like the confirmed finding repeated in plain language before hearing more terminology.
Of course. We should not soften the meaning so much that the finding becomes unclear.
Could my chosen support person join the next part with my permission?
Yes. We can confirm what you want shared and whom you want present.
Then I can separate the diagnosis from questions that the further assessment still needs to answer.
That distinction will remain clear in the summary and the next discussion.

The pathology wording is unfamiliar | A clinician explains the role of a report without inventing its details. | Oncologist | Patient
Which part of the pathology report would you like explained before we move on?
I recognize the diagnosis line, but the descriptive terms make me think every word predicts my future.
The report describes the tissue findings; not every term is a prognosis.
Could we distinguish the type of tumor from how the overall situation is staged?
Yes. Those concepts should be explained separately using the actual report and other assessment.
I also want to know which questions the tissue sample cannot answer by itself.
That limitation matters, and we should not imply that one sample settles every clinical question.
Please avoid giving a survival estimate simply because I ask what the words mean.
We will distinguish terminology, established findings, and any appropriate individualized prognosis discussion.
Then the report can become understandable without turning each unfamiliar word into a prediction.

Permission to include a relative | A patient clarifies who may hear difficult news. | Patient | Oncologist
My brother came with me, but I want to hear the diagnosis privately first.
We can arrange that and discuss what you would like shared afterward.
He usually handles appointments, so people sometimes assume he should answer every question.
Helping with appointments does not automatically make him the recipient of every clinical detail.
I may want him present when we discuss the next investigation.
We can revisit your preference and confirm the appropriate permission for that discussion.
I also want the record to show that I am making my own decisions.
The actual decision-making arrangements should be clear rather than inferred from who accompanies you.
Thank you. Support is helpful, but I do not want my voice replaced.
We can include the support you choose while keeping the explanation and questions directed to you.
""")
LESSONS['module-2'] = short_lesson(BOOK['units'][1], """
Grade is not stage | A patient confuses two classification terms. | Patient | Oncologist
The report gives a grade, so I assumed that number was also my stage.
Grade and stage describe different features and should not be treated as interchangeable.
Can you explain the distinction without assigning a stage before the remaining assessment?
Grade concerns features of the tumor cells or tissue; stage concerns the extent of disease.
Then a grade alone cannot tell me where disease is present in the body.
Correct. The actual staging process uses the relevant clinical and investigation findings.
I do not want a number copied from one category into the other.
We should name each category and preserve what remains unestablished.
Could the summary state clearly that the stage is still pending?
Yes. A clear record should not turn an available grade into an invented stage.

An imaging finding needs correlation | Two clinicians discuss a finding that may affect staging. | Radiologist | Oncologist
There is a finding that needs correlation before its significance is described as established.
Thank you. I will not automatically label it metastatic disease in the patient summary.
Please retain the report's uncertainty and the actual recommendation for further review.
We need to explain what is seen separately from what it may mean.
An earlier comparison study may be useful, if the relevant images can be obtained.
I will clarify whether those images are available rather than assume the comparison is complete.
The current report should not be shortened to a definitive stage without the required assessment.
Agreed. The staging discussion must use the actual combined evidence.
Please let the patient know which question remains unresolved and who will address it.
We will provide a concrete next step without promising the conclusion of the review.

A stage question is not a prognosis timetable | A patient asks what classification can predict. | Patient | Oncologist
If you eventually establish the stage, will that tell me exactly how long I will live?
Stage provides important information, but it is not an individual timetable.
I want honest information without having a population statistic presented as my guaranteed outcome.
That distinction matters. Any prognosis discussion needs the actual diagnosis, context, and uncertainty explained.
Would treatment response and other individual factors also belong in that discussion?
Yes, where relevant, rather than reducing the whole situation to one classification.
I am not asking you to avoid the subject, only to describe what the information supports.
We can discuss it directly while making the limits of prediction clear.
Could we first confirm which findings are established and which tests remain outstanding?
We should. Prognostic language must not rest on a stage that has not yet been established.
""")
LESSONS['module-3'] = short_lesson(BOOK['units'][2], """
A biomarker is not a treatment guarantee | A patient asks about an identified alteration. | Patient | Oncologist
The report names an alteration. Does that guarantee a targeted treatment will work for me?
No. A biomarker may inform options, but it does not guarantee response or availability.
I also want to know whether the finding is established and clinically relevant.
We should review the actual test, interpretation, and evidence for this disease context.
Could the same alteration have different implications in different kinds of cancer?
The clinical context matters; a familiar term is not a universal treatment instruction.
Then we need to distinguish a possible option from an agreed treatment plan.
Exactly, including eligibility, access, benefits, harms, and the actual clinical assessment.
Please do not let an encouraging headline replace that individualized explanation.
We will explain what the result supports and what remains uncertain before discussing a decision.

Tumor testing and inherited risk | A patient asks whether a tumor result proves a family risk. | Patient | Oncologist
The tumor test found a change, and I assumed that means my children inherited it.
A tumor finding does not automatically establish an inherited variant in your family.
Could you distinguish a somatic change from a germline finding?
A somatic change is acquired in cells; a germline finding concerns inherited genetic material.
Does that mean the tumor report alone cannot settle whether relatives need testing?
Correct. The appropriate assessment and counseling determine what further discussion is relevant.
I would like to know what information is confirmed rather than alarm everyone from an assumption.
We should explain the actual result and the limits of what it establishes.
Who can help us understand any genuine inherited-risk question that remains?
The appropriate genetics service can provide counseling through the actual referral process.

A variant remains uncertain | Two clinicians clarify how an uncertain variant should be described. | Oncologist | Genetics clinician
The report lists a variant of uncertain significance, and the patient thinks it proves a harmful mutation.
We should explain that its clinical significance is not established by that label.
I will avoid presenting the variant as a confirmed explanation for the disease.
That is important. The uncertainty should remain visible in the patient discussion and record.
Does the wording itself authorize a treatment change or family testing plan?
No. The actual clinical and genetics assessment must determine what action, if any, is appropriate.
The patient would benefit from a clear explanation of why uncertain does not mean harmless either.
Agreed. Neither pathogenic nor benign should be asserted without the supporting interpretation.
I will identify the appropriate contact for questions about the report and any later update.
That keeps the result understandable without forcing a conclusion the evidence does not support.
""")
LESSONS['module-4'] = short_lesson(BOOK['units'][3], """
Control is not cure | A patient checks the stated treatment intent. | Patient | Oncologist
You described the aim as disease control. I heard that as a promise of cure.
Those are different aims, and I need to correct that misunderstanding clearly.
Please explain the actual intent without using a more comforting word that changes its meaning.
The relevant plan aims to control the disease; we should discuss what that means in your situation.
Does an aim describe what is hoped for rather than guarantee what will happen?
Yes. Treatment intent and the eventual outcome must remain distinct.
I would like the expected benefits and burdens explained against that stated aim.
That belongs in the informed discussion, using the actual options and evidence.
Then I can compare choices without believing a cure has been promised.
Exactly. Clear language about intent helps you understand the decision rather than merely agree to terminology.

Caregiving responsibilities affect the discussion | A patient explains a practical priority. | Oncologist | Patient
What responsibilities or priorities should we include when discussing the actual treatment options?
I care for my partner, and frequent appointments could affect both of us.
That practical burden belongs in the discussion rather than being dismissed as unrelated.
I do not want it recorded as though I have already refused treatment.
A concern about feasibility is not the same as an informed decision to decline.
Could we clarify the actual visit requirements before deciding what support is needed?
Yes. We should verify the proposed schedule and available services rather than guess.
I would also like someone to help explore support without promising assistance is guaranteed.
We can identify the appropriate service and distinguish an application from confirmed help.
That would let me discuss the clinical options with the practical facts in view.

Consent after a clearer explanation | A patient requests clarification before agreeing to a plan. | Patient | Oncologist
I signed that I received information, but I still do not understand the treatment goal.
Let us clarify it. A signature should not replace a meaningful discussion.
I need to distinguish reducing symptoms from reducing the chance of recurrence.
Those are different purposes, and the actual recommendation should identify its intended aim.
Could you explain which aim applies here rather than list every possible benefit?
Yes, using the real plan and its relevant evidence and limitations.
I would then like to explain it back so you can check your wording was clear.
That helps us check understanding without treating you as the problem.
Understanding the explanation does not necessarily mean I have agreed to start immediately.
Correct. Comprehension, questions, and the actual decision should be distinguished and documented accurately.
""")
LESSONS['module-5'] = short_lesson(BOOK['units'][4], """
A symptom report during an active response | A nurse transfers an urgent treatment-related concern. | Nurse | Oncologist
The patient reports fever and shaking after treatment, and the urgent clinical pathway is already active.
Please lead with those symptoms and the action taken, then identify the verified information.
I have not assigned a cause or inserted laboratory values that are not available.
Good. A concerning report should not become a confirmed diagnosis without assessment.
The patient also corrected the time symptoms began, and I have recorded that change.
Please preserve the corrected timing and its source in the handoff.
Should I wait until every field is complete before confirming the receiving team?
No. The actual urgent response must not wait for a perfectly polished report.
I will confirm acceptance and pass new verified information through the active route.
That keeps urgency, uncertainty, and responsibility clear while the clinical assessment continues.

New symptoms are not automatically progression | A patient asks what a new symptom means. | Patient | Oncologist
I have a new symptom during treatment. Does that automatically mean the cancer is progressing?
No. The cause requires the actual clinical assessment; the timing alone does not establish progression.
I also wondered whether every symptom during treatment must be caused by the medicine.
That is another assumption we should avoid. Report the symptom and follow the actual care instructions.
I can describe when it began and how it changed without choosing the cause myself.
Those details are useful, with anything measured distinguished from what you noticed.
I do not want uncertainty about the cause to be mistaken for permission to ignore it.
It should not be. The appropriate clinical response depends on the actual situation.
Please confirm the real contact route rather than give a general instruction to wait.
We will use your actual care plan and assessment, not a guessed rule from terminology.

An urgent message is not a routine inbox item | Two staff members clarify the communication route. | Coordinator | Nurse
This message describes an urgent concern, but it arrived in the routine appointment inbox.
We need to follow the actual escalation process rather than leave it for ordinary scheduling.
I will not decide that it can wait because the patient used the wrong channel.
Correct. The clinical concern needs the appropriate assessment and response.
The message has been forwarded, but I have not received acknowledgment from the clinical team.
Then we must distinguish sent from accepted and continue the actual service process.
I will record the source, time, and actions without adding an unconfirmed diagnosis.
Please also identify who is responsible for confirming the receiving team.
A forwarded message alone is not a completed clinical handoff.
Exactly. The communication loop must support the real response rather than merely move the message elsewhere.
""")
LESSONS['module-6'] = short_lesson(BOOK['units'][5], """
Smaller is not automatically a response category | A patient reads a scan comparison. | Patient | Oncologist
The report says a measured lesion is smaller. Can I call that a partial response?
A response category requires the relevant criteria and complete assessment, not one phrase alone.
I am glad about the change, but I do not want to overstate what it means.
We can acknowledge the finding while explaining what the overall review establishes.
Does a smaller measurement also guarantee that every area of disease has improved?
No. The actual comparison and other relevant findings must be reviewed.
Could differences in technique or the comparison study affect how a change is interpreted?
They can matter, which is why the report and clinical context belong together.
Then the measurement, response category, and treatment decision remain separate questions.
Exactly. We will explain the actual conclusion without turning a favorable detail into a guarantee.

Stable disease still needs explanation | A patient asks about a response term. | Oncologist | Patient
You asked what stable disease means in the reviewed assessment.
I heard stable and thought it meant nothing clinically important had happened.
The term needs the actual criteria and context; it is not a judgment that the treatment was pointless.
Could we distinguish a response category from how I feel day to day?
Yes. Symptoms, function, imaging, and the relevant assessment may describe different aspects of care.
I would like to know what the category supports and what it does not decide by itself.
We should explain that before discussing the actual next treatment decision.
Does the word stable guarantee that the situation cannot change before the next review?
No. It describes the assessed state, not a promise about every future event.
That helps me understand the term without treating it as either failure or permanent reassurance.

A comparison report lacks the earlier images | Two clinicians discuss an incomplete comparison. | Radiologist | Oncologist
The earlier written report is available, but I do not yet have the actual comparison images.
Then we should not describe the image-to-image comparison as complete.
I can state the limitation and explain what additional material would support the review.
Please keep that limitation visible rather than shortening the report to a definite response category.
The patient may ask whether the delay itself means an unfavorable finding.
We should explain that missing comparison material is not a clinical outcome.
Once the images arrive, the appropriate review can address the actual comparison question.
Agreed. We should identify who follows up the missing material and communicates the reviewed result.
A requested comparison is not the same as a completed one.
That distinction belongs in both the clinical record and the patient explanation.
""")
LESSONS['module-7'] = short_lesson(BOOK['units'][6], """
A trial invitation is not enrollment | A patient asks about joining a study. | Patient | Oncologist
I received an invitation to discuss a trial. Does that mean I am already enrolled?
No. An invitation, eligibility review, consent, and enrollment are different steps.
I want to understand the study before anyone assumes I have agreed to participate.
The relevant information and questions belong before the actual consent decision.
Does being invited guarantee that I meet every eligibility criterion?
It does not. The study team must review the actual criteria and your circumstances.
I also want to know what happens to ordinary care if I decide not to join.
That should be explained clearly using the actual study and care arrangements.
Then a discussion can help me decide without making the decision for me.
Exactly. Participation should not be inferred from accepting information or attending a meeting.

Randomization is not a personalized recommendation | A research clinician explains allocation. | Research clinician | Patient
You asked whether randomization means the team chooses the arm it thinks will work best for you.
That was my assumption, because I thought every assignment was individually selected.
Randomization allocates according to the study method rather than that kind of personal choice.
Could you explain the actual allocation process and what I would know about it?
Yes. We need to use the real protocol, including any masking and relevant alternatives.
Does joining guarantee that the experimental approach will be better than the comparison?
No. The study addresses uncertainty, and benefit cannot be promised in advance.
I would like those limits explained before I decide whether participation fits my priorities.
That is part of the informed discussion, alongside risks, burdens, and your questions.
Then I can distinguish research allocation from a clinician's individualized recommendation.

Withdrawing needs an actual explanation | A participant asks about leaving a study. | Patient | Research clinician
If I choose to leave the study, does everything connected with it disappear immediately?
We should explain withdrawal using the actual protocol and applicable rules, not a blanket promise.
I want to understand the difference between stopping study treatment and later follow-up.
Those may involve different arrangements, which need to be explained clearly.
What about information already collected before I withdraw?
Its handling depends on the actual consent documents and relevant requirements.
I do not want someone to discourage my question by saying that joining is irreversible.
Your questions and voluntary participation matter; we should explain the available choices accurately.
Could we review the relevant document together before I decide what to request?
Yes. We will distinguish the decisions and consequences without inventing a universal withdrawal rule.
""")
LESSONS['module-8'] = short_lesson(BOOK['units'][7], """
Palliative care alongside active treatment | A patient asks whether support means treatment is ending. | Patient | Oncologist
The palliative-care referral frightened me because I assumed it meant every cancer treatment was stopping.
Palliative care can address symptoms and support alongside disease-directed care; the referral does not automatically stop treatment.
I would like the actual purpose of this referral explained for my situation.
We should identify the symptoms, practical needs, and questions the team can help address.
Does it automatically mean that I have entered hospice care?
No. Those terms and services are not interchangeable, and the actual arrangements need explanation.
I also do not want a resuscitation decision inferred from accepting symptom support.
That would be a separate discussion under the actual clinical and legal process.
Then I can consider the support without agreeing to decisions that were never discussed.
Exactly. Clear distinctions let you understand what the referral does and does not mean.

A family request differs from the patient's wish | A clinician clarifies whose preference is being expressed. | Relative | Oncologist
I think the patient should avoid hearing difficult details because they might lose hope.
I hear your concern, but we need to understand the patient's own information preferences.
Can you assume that I know best because I attend most appointments?
Your support is important, but attendance does not automatically determine what the patient wants disclosed.
How can we discuss this without making the patient feel abandoned by the family?
We can ask respectfully about preferred information, support, and the appropriate decision-making arrangements.
I do not want my worry recorded as though it were the patient's stated choice.
That distinction matters. We should attribute your concern to you rather than merge the accounts.
Then the conversation can include the family without replacing the patient's voice.
Yes. We will follow the actual preferences, capacity assessment, and applicable responsibilities.

Symptom priorities change over time | A patient revisits the focus of supportive care. | Patient | Palliative clinician
At our last visit, pain was my main concern. Today fatigue is affecting me more.
Thank you for updating the priority. The earlier note should not freeze the agenda.
I want the team to understand the impact on ordinary tasks, not just hear a symptom label.
Please describe what has become harder and how the pattern has changed.
Does changing the priority mean the earlier pain concern no longer matters?
Not necessarily. We can distinguish improvement, persistence, and a new leading concern.
I would like the actual care options explained after the appropriate assessment.
That discussion should use your current situation rather than an unchanged template.
Could we confirm who coordinates the follow-up with the oncology team?
Yes. Shared care needs clear responsibility and communication, not an assumption that another service has everything.
""")
