"""Twenty-four university teaching conversations for the course accordions."""
from books.university_professors_content import BOOK
from books.specialist_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], '''
The example is not a template to copy | A student asks about an assignment model. | Student | Professor
The sample response has four paragraphs. Does my submission need exactly the same structure to meet the criterion?
The sample illustrates a supported comparison; its paragraph count is not an additional requirement in this brief.
I should follow the stated task rather than reproduce every surface feature of the example.
Exactly. Identify the shared question, explain the difference in reasoning, and support it with both texts.
Could a different organization work if the connection between the authors remains clear?
Yes, provided it satisfies the published instructions and makes the reasoning easy to follow.
I was treating the model as a hidden rule because I did not want to miss anything.
That is understandable. I will clarify which features illustrate the standard and which are merely one possible presentation.
The important question is whether my evidence supports the comparison, not whether my layout looks identical.
Correct. Use the model to understand the intellectual task rather than as a pattern to reproduce mechanically.

The deadline display lacks a time zone | A student checks online submission information. | Student | Professor
The course page says Tuesday at five, but I am attending remotely from another time zone this week.
Thank you for checking. We should identify the published course time zone rather than leave five ambiguous.
The platform display and the assignment document appear to use different local settings.
I will verify the actual deadline and post one clear version for everyone.
Should I rely on the countdown until the mismatch has been resolved?
Do not assume the displays are equivalent; send the specific discrepancy through the course channel promptly.
I will include the two displayed times without sharing any private information from another student's account.
That will help us identify the issue and communicate the correction consistently.
The announcement should include the date, time, and time zone rather than just repeating Tuesday.
Yes. Clear submission information should not require students to guess which clock the instructor meant.

A learning outcome is not a topic list | Colleagues review an assignment explanation. | Lecturer | Course lead
My introduction lists three topics, but students still ask what they should be able to do with them.
A topic list names content; the learning outcome should identify the capability they will demonstrate.
For this task, they need to compare two explanations using evidence from the supplied readings.
Then say that directly and connect the assessment criterion to the same action.
The reading list remains important, but completing it is not the entire demonstration of learning.
Exactly. Students need to know how the reading supports the task rather than treat reading as the final product.
I can also show where the formative outline lets them practice that comparison.
That makes the sequence visible without adding a long explanation before every activity.
The revised introduction will name the task, evidence, and standard in a few clear sentences.
Good. It will make the academic demand more explicit without lowering it.
''')
LESSONS['module-2'] = short_lesson(BOOK['units'][1], '''
A disagreement needs the original claim | A seminar leader checks a rebuttal. | Student | Professor
I disagree with the author because the article says people never change their routines.
Before we respond, can we check the actual wording of the claim you are challenging?
The passage says routines often persist when the cost of changing them is high.
That is narrower than never change, and the qualification matters to the argument.
I should restate the author's position accurately before presenting a counterexample.
Yes. Otherwise the rebuttal may defeat a stronger claim the author did not actually make.
My example involves a low-cost change, so it may not challenge the stated condition.
That is a useful revision. We can now ask whether the condition itself is adequately supported.
I will separate the author's claim, its scope condition, and my objection.
Then the discussion can be demanding without relying on a misrepresentation of the source.

The quickest response is not the only response | A student discusses seminar participation. | Student | Professor
I often have a point ready just after someone else answers, and then the discussion has already moved on.
Thank you for explaining that. I can build in a short pause before inviting responses.
I do not need an easier question; I need enough time to formulate the connection clearly.
That is an important distinction. Time to respond and the intellectual standard are separate matters.
Could you also invite a follow-up after the first answer rather than immediately summarize it?
Yes. We can make room for extension or disagreement while keeping the discussion focused.
I will try to identify which part of the earlier contribution my comment addresses.
That will help the group connect ideas instead of hearing a sequence of unrelated speeches.
The pause should benefit others who are also organizing their thoughts.
Exactly. Participation should not depend only on who can begin speaking first.

A synthesis should preserve disagreement | A seminar participant checks the closing summary. | Student | Professor
Your summary says we agreed that the policy caused the change, but several of us questioned the causal evidence.
You are right. I compressed the discussion too far and should preserve that unresolved issue.
We agreed that the two events occurred together, not that the policy was established as the cause.
Then the synthesis should distinguish the observed association from the competing explanations.
It could also name what evidence would help evaluate those explanations without choosing one prematurely.
Yes. That makes the next inquiry concrete rather than inventing a consensus that did not occur.
I appreciate being able to correct the summary without reopening every point in the discussion.
A precise correction is useful. The summary belongs to the reasoning we actually developed together.
I will note the agreed observation and the open causal question.
That is the accurate outcome of today's discussion and the starting point for the next reading.
''')
LESSONS['module-3'] = short_lesson(BOOK['units'][2], '''
Vague feedback becomes a usable instruction | A student asks about a comment. | Student | Professor
The comment says develop this, but I cannot tell whether you mean add a source or explain the source already there.
In this paragraph, the missing step is explaining how the existing evidence supports your conclusion.
So adding another quotation would not necessarily address the problem.
Correct. The current passage needs a reasoning link, not simply a larger amount of cited material.
Could you point to the sentence where the connection becomes unclear?
Here, the paragraph moves from the reported observation to a broader conclusion without explaining that move.
I can see the gap now, and I can use the same check in the next paragraph.
That is the intended improvement. I will make the feedback wording more specific.
The task is not to make every paragraph longer, but to make the reasoning visible.
Exactly. Concision and a fully explained argument can work together.

A grade review is not a negotiation over effort | A student discusses a mark. | Student | Professor
I worked longer on this assignment than on the previous one, so I expected the mark to be higher.
I recognize the effort. Let us look at what the submitted work demonstrates against the published criteria.
My concern is that the evidence criterion may have been applied differently from the example we discussed.
That is a specific question we can examine through the stated review process.
I can identify the passage and the descriptor I believe it meets.
Please do. That gives the review a clear basis rather than a request for points without reference to the work.
The review may explain the existing score or identify an error, depending on what it finds.
Yes. We should not promise the outcome before checking the actual assessment.
I will use the process and keep the concern focused on that criterion.
That is a constructive way to raise it while preserving the academic standard.

A correction should reach the student record | An instructor checks a confirmed recording error. | Student | Professor
You confirmed the total should be twenty-one, but the course record still displays nineteen.
Thank you for telling me. I need to check whether the correction was actually saved and published.
The email confirmation was clear, but it did not change what I could see.
Then the action is not complete from your perspective, and I should close that loop.
I do not want this follow-up mistaken for a new request to change the criterion scores.
It is not. We are checking implementation of the arithmetic correction already confirmed.
Please let me know once the displayed record matches the corrected total.
I will verify the entry and send a confirmation through the appropriate private channel.
That will resolve the mismatch between the message and the recorded result.
Exactly. A promised correction needs to become an accurate record, not remain only an email.
''')
LESSONS['module-4'] = short_lesson(BOOK['units'][3], '''
The student needs a starting point, not a rewritten paper | A professor structures office hours. | Student | Professor
I brought the whole assignment because I feel stuck, but I cannot identify which part is causing the problem.
Let us begin with the first step you attempted and where the reasoning stopped making sense.
I selected evidence, but I do not know how to turn it into a comparison.
Then we can work through one supplied example and identify the connection it requires.
You will not need to rewrite the whole assignment for me to understand that step.
Correct. The aim is to make the process visible so you can apply it yourself.
After the example, I can explain the same step using the second passage.
That will let us check understanding rather than only confirm that my explanation sounded familiar.
We can leave the formatting questions until the conceptual problem is clearer.
Yes. A focused meeting can resolve the main obstacle more effectively than touching every issue briefly.

A calculation error differs from a concept error | A professor checks a student's reasoning. | Student | Professor
I wrote forty out of one hundred as four percent, but I knew I needed to divide by the eligible population.
Your setup uses the correct denominator; the numerical conversion is where the error occurred.
That differs from comparing raw counts and ignoring group size altogether.
Exactly. We should identify whether the problem is the concept or the execution of the calculation.
I can repeat the conversion carefully and check whether the result is plausible.
Good. Forty out of one hundred means forty percent, not four percent.
The corrected number does not mean I should change which group belongs in the denominator.
Correct. Keep the sound reasoning and repair the specific numerical slip.
I will label the part and whole before doing the arithmetic again.
That gives you a reliable check without discarding an approach you already understood.

The office-hour plan needs a manageable endpoint | A student and professor agree on a meeting focus. | Student | Professor
We have ten minutes left, and I still have questions about the chart, the reading, and next week's assignment.
Let us finish the chart distinction first, then identify the next question for a follow-up.
I would rather leave with one idea I can apply than several explanations I cannot connect.
That is a sensible goal. Tell me the difference between participant count and participation rate.
Count tells us how many participated; rate compares that number with the eligible population.
Good. Use the two supplied groups to check that distinction once more.
I can do that, and then bring a specific reading question to the next meeting.
Please note the passage and the point that became unclear so we can begin efficiently.
The follow-up is support, not an automatic change to the assignment deadline.
Correct. Any deadline question follows the actual course process and needs its own clear decision.
''')
LESSONS['module-5'] = short_lesson(BOOK['units'][4], '''
The rubric version differs between graders | A course coordinator checks inconsistent results. | Assistant | Professor
My copy gives three levels for evidence, but another grader is using an older four-level guide.
Then we need to establish the approved version before comparing or releasing the results.
The difference may come from an outdated attachment rather than disagreement about the same descriptor.
Good distinction. We should identify which submissions were marked with which version.
I can preserve the records and flag the affected batch without silently changing scores.
Then we can follow the assessment process for reviewing the impact consistently.
The team briefing should include the approved guide and a clear version identifier.
Yes. Everyone needs the same standard, not merely a reminder to grade more carefully.
We should also verify that students received the appropriate published criteria.
Absolutely. The review must account for communicated expectations as well as internal grader instructions.

A polished response can still miss the criterion | Two graders discuss an anchor response. | Assistant | Professor
This response is fluent and confident, so it feels stronger than the less polished example beside it.
Let us separate that impression from the evidence criterion we are scoring.
The fluent response quotes a source but never explains the connection to its conclusion.
Then it does not meet the supplied level requiring an explained link.
The other response uses simpler language but makes that relationship explicit.
Under this criterion, the explained relationship matters more than the surface polish.
We should assess expression separately if the published rubric includes that dimension.
Exactly. Do not let one attractive feature silently replace the standard for another.
I will add the passage-based rationale to the calibration note.
That will help other graders understand the distinction rather than simply copy our numbers.

A sampled problem may affect the batch | A teaching team plans a review. | Assistant | Professor
We found the same scoring shortcut in three sampled papers. Is correcting those three enough?
We need to assess whether the issue affects other work in the relevant batch.
The sample reveals a possible pattern, but it does not identify every affected submission by itself.
Correct. Define the review scope through our assessment process and keep results unreleased where required.
I can identify the grader, rubric version, and criterion involved without exposing student details unnecessarily.
That gives the team a practical way to locate the relevant records.
We should document what was checked and any changes made under the approved process.
Yes, so the final status distinguishes a completed review from a plan to review.
I will not mark the batch cleared merely because the sample discussion is finished.
Good. Calibration is a step toward consistency, not automatic evidence that every result is ready.
''')
LESSONS['module-6'] = short_lesson(BOOK['units'][5], '''
The scanned reading is not readable by the student's tool | A student reports an access barrier. | Student | Professor
The reading opens as a picture of text, and my screen reader cannot read the paragraphs.
Thank you for identifying the barrier. We need an accessible version through the appropriate course support process.
The file looks clear visually, but that does not make its text available to the software.
That distinction is important. I will coordinate the format correction and check the actual result.
Please avoid assuming that a new file name means the accessibility problem is fixed.
Agreed. We need to verify usability rather than only replace the attachment.
I can report whether the corrected version works through the private course channel.
That will help us close the loop without asking you to discuss personal information with the class.
The reading deadline also needs attention if access has been delayed.
I will address the practical timing through the actual course and access procedures rather than leave you to improvise.

The captions omit the key term | A student flags a lecture-media issue. | Student | Professor
The automated captions repeatedly replace the technical term with an unrelated word, which changes the explanation.
Please identify the relevant timestamps so the media team can correct the actual content.
The audio is understandable to some listeners, but the captioned version gives a different concept.
Then the issue is accuracy of access, not merely whether a caption track exists.
I can send the timestamps without adding any private details about another student.
That is helpful. I will coordinate correction through the appropriate support process.
Should the transcript also be checked so the same error does not remain in a second resource?
Yes. We should verify the related materials within the stated correction scope.
I will use the revised resource once the accurate version is confirmed.
And I will communicate the update clearly so students do not continue relying on the incorrect terminology.

A room request still needs confirmation | A professor follows up on assessment logistics. | Student | Professor
The platform now shows my approved duration, but the room information still says requested.
Then the timing setting is resolved, while the location remains an open implementation issue.
I need a confirmed plan before arriving, not just reassurance that someone sent an email.
You are right. I will coordinate with the testing staff and the designated access office promptly.
Please send the actual location and contact through our agreed private channel.
I will, and we need an authorized contingency if the original room cannot be secured.
The approved arrangement should not disappear because one booking is delayed.
Correct. We need to resolve the practical barrier through the institution's process.
I will flag any conflicting information in the final message rather than assume the newest label is correct.
That helps us verify a workable arrangement, not merely a series of administrative requests.
''')
LESSONS['module-7'] = short_lesson(BOOK['units'][6], '''
A similarity percentage needs interpretation | A student asks about a report. | Student | Professor
The report shows a high match percentage. Does that automatically mean a violation has been established?
No. The actual passages, sources, assignment rules, and institutional process need to be examined.
Some matches appear to come from the required question and properly quoted source passages.
Those details matter, and the report is a tool for review rather than a verdict.
I can explain where the cited material appears and how I used it.
You should have the appropriate opportunity to respond to any specific concern.
The conversation should identify the passage in question rather than rely only on one total percentage.
Agreed. A number without context can conceal important distinctions in the underlying material.
I will preserve my existing work and source information for the actual process.
That is appropriate. Neither a high nor a low percentage alone replaces the required assessment of the facts.

Different assignments permit different assistance | A student checks a course rule. | Student | Professor
We used an AI tool during last week's brainstorming exercise. I assumed that permission applied to this individual analysis too.
The assignments have different stated conditions, so we need to check the instructions for this task.
The current brief permits planning support with disclosure but requires the submitted analysis to be my own.
That is the rule supplied here. Permission for one stage does not automatically authorize every use.
I should ask about an unclear tool function before using it rather than infer permission from the earlier exercise.
Yes. A specific question helps us clarify the boundary without inventing a new rule after submission.
Could the clarification also be shared with the rest of the class?
Certainly. Everyone should have access to the same communicated expectations.
I will distinguish brainstorming assistance from generating the final analysis in my planning.
Good. Follow the actual assignment conditions and verify any source or claim you include.

The reference exists but does not support the claim | A professor discusses source use. | Student | Professor
I checked that the article exists, but your comment says it does not support the sentence I attached it to.
Source verification includes both existence and the relevance of the evidence to the claim.
The article discusses a different population, while my sentence makes a broader statement.
Then the issue is how you represented and applied the source, not simply whether the citation is genuine.
I need to identify what the article actually establishes and retain its limits.
Exactly. A real source can still be used in a misleading or unsupported way.
We should discuss the specific passage rather than assume that correct formatting resolves the concern.
Yes. Formatting helps readers locate the source; it does not prove the inference is justified.
I will preserve the original submission and respond through the stated process to the identified concern.
That keeps the factual review clear without prematurely determining intent or an institutional outcome.
''')
LESSONS['module-8'] = short_lesson(BOOK['units'][7], '''
A vote needs the amended wording | A committee member checks the minutes. | Member | Chair
The minutes record approval of the original proposal, but we voted on a one-term pilot with staffing conditions.
Thank you. The record needs the amended wording actually put to the vote.
The difference is substantive because the original version sounded permanent and unconditional.
Agreed. We should not shorten the entry in a way that removes the conditions.
It should also distinguish our recommendation from the separate board approval required for implementation.
Yes. The committee vote did not exercise authority assigned to another body.
I can identify the exact amendment in the meeting record for the minutes review.
Please do, and we will follow the stated process for correcting and approving the minutes.
The corrected entry will help colleagues know what action is authorized and what remains pending.
That is the purpose of an accurate decision record, not merely a polished summary.

A shared goal can have different resource proposals | Faculty colleagues discuss course access. | Professor | Chair
I support more student access, but I disagree with increasing the cap before teaching support is confirmed.
Then state that condition directly so the disagreement is not mistaken for opposition to access itself.
My concern is the ability to give timely feedback to an additional ten students.
That is a concrete resource question we can ask the responsible colleagues to assess.
We could propose a limited pilot if staffing and room capacity are verified.
Yes, provided the duration, conditions, and approval route remain explicit.
I do not want the discussion summarized as faculty are unwilling to teach more students.
Nor should it say everyone supports immediate implementation when that is not the position.
The minutes can record support for the goal and the unresolved capacity issue separately.
That will preserve the actual disagreement and make the next decision more informed.

A pilot does not become permanent by silence | A chair discusses the review point. | Member | Chair
The pilot has run for one term, and the timetable team assumes the larger cap continues automatically.
We need to check the actual authorization and the review condition attached to the pilot.
The approved proposal required a review of feedback workload and participation before any permanent change.
Then the absence of a new objection is not itself the required continuation decision.
I will gather the specified evidence and identify which body has authority for the next step.
Good. The review should address the conditions actually agreed, not add unrelated measures after the fact.
The timetable needs a clear status so staff do not plan around an unsupported assumption.
We can communicate that continuation is under review and identify the responsible decision process.
Once the decision is made, the schedule and course information should reflect the actual outcome.
Exactly. A limited trial needs an explicit close or continuation step, not an indefinite extension by habit.
''')
