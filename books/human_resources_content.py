"""Original human-resources conversations with bounded language practice."""
from books.authoring import unit

BOOK = dict(
    slug='human-resources', title='Human Resources English',
    cover_label='Hiring / performance / employee relations / change',
    cover_title='Human Resources', cover_size=32,
    tagline='Be clear about expectations. Be careful with people.',
    audience='For HR partners, recruiters, people managers, and employee-relations teams.',
    map_intro='Eight people-management conversations connecting fair questions, clear expectations, and accurate records.',
    notes_title='Clear language is part of fair treatment.',
    notes_intro='Human resources conversations often carry two responsibilities at once: responding to a person and keeping the record accurate. A concern is not yet a finding. A salary midpoint is not an individual promise. A manager can acknowledge uncertainty without sounding indifferent. These fictional cases practice the words that make those distinctions understandable while keeping next steps specific.',
    field_notes=[
        ('Describe the work, not a personality', 'Replace vague judgments with a task, an observable behavior, and the relevant expectation. Ask for the missing context before assigning a motive.', '"The last two reports omitted the summary; I have not established why."'),
        ('Name the status of the information', 'Distinguish what someone reported, what a document shows, what has been verified, and what the authorized process has decided. Each supports a different statement.', '"The note records an allegation, not a finding."'),
        ('Make a limited promise useful', 'Commit to the next contact or review you can deliver. Do not replace uncertainty with an unsupported outcome, secrecy guarantee, or employment assurance.', '"I will update you on Friday even if the review remains open."'),
        ('Use the actual policy and jurisdiction', 'These exercises supply fictional policy terms where needed. Real eligibility, process, privacy, representation, and employment obligations depend on the relevant facts and applicable rules.', '"That is the policy range; your individual placement requires a separate explanation."')],
    scope_note='Original fictional language practice, not legal, employment, benefits, medical, or investigation advice. People, policies, figures, and outcomes are invented. Real decisions require current local law, applicable agreements, authorized procedures, and qualified advice. US and UK sources provide identified background, not a universal HR procedure.',
    sources=[
        dict(title='US Office of Personnel Management. Structured Interviews.', url='https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews/', note='Background on job-related competencies, consistent questions, and common rating standards. The selection exercise and candidates are fictional.', checked='30 September 2026'),
        dict(title='US Equal Employment Opportunity Commission. Prohibited Employment Policies/Practices.', url='https://www.eeoc.gov/prohibited-employment-policiespractices', note='US background on discrimination and retaliation. This book does not determine whether any fictional or real act meets a legal test.', checked='30 September 2026'),
        dict(title='US Equal Employment Opportunity Commission. Disability Discrimination and Reasonable Accommodation: Medical Inquiries, Leave and Telework.', url='https://www.eeoc.gov/disability-discrimination-and-reasonable-accommodation-medical-inquiries-leave-and-telework', note='US background on individualized accommodation discussions and information handling. No request in this book is legally adjudicated.', checked='30 September 2026'),
        dict(title='Acas. Carrying Out an Investigation.', url='https://www.acas.org.uk/investigations-for-discipline-and-grievance-step-by-step/step-3-carrying-out-an-investigation', note='UK background on fair fact gathering and objective evidence review. Local procedures and rights must be checked separately.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Recruiting, Screening, and Candidate Experience',
    scene='What does good fit actually mean?',
    skill='Turn vague hiring preferences into observable, job-related criteria and a consistent candidate conversation.',
    brief='Recruiter Lina and hiring manager Marcus are preparing interviews for a client-operations coordinator. Marcus asks for good cultural fit but has not defined it. The role requires timely client follow-up and escalation of conflicting deadlines. The draft scorecard rewards confidence and shared interests without describing evidence. No applicant has been scored. Lina must clarify the competencies, interview questions, rating basis, and candidate updates before the panel starts making comparisons.',
    cast='Lina | Recruiter\nMarcus | Hiring manager',
    culture=('Translate an impression into evidence', 'A fluent, sociable applicant can create a strong first impression without demonstrating the required work. Ask what the person needs to do, what evidence would demonstrate it, and how every applicant will have a fair opportunity to provide that evidence.'),
    a='''Which tasks are actually required? | Client follow-up and escalation of conflicting deadlines | Sharing the manager's hobbies | Speaking at the fastest pace | Agreeing with every panel member | The brief identifies two work requirements, not a preferred personality or social background.
What is wrong with the draft scorecard? | It uses impressions without observable evidence criteria. | It already contains all completed candidate scores. | It prohibits asking about previous work. | It measures only the two specified competencies. | Confidence and shared interests do not explain how candidates will demonstrate the required tasks.
What is the current selection status? | No applicant has been scored. | The preferred applicant has been selected. | Every candidate has failed the interview. | An offer has been accepted. | The brief explicitly places this discussion before the panel scores applicants.''',
    vocabulary='''job requisition | An internal request to fill an approved or proposed position. | open a job requisition
role profile | A description of a position's purpose and required work. | clarify the role profile
essential criterion | A requirement necessary for the particular role. | define essential criteria
desirable criterion | A useful attribute that is not a minimum requirement. | distinguish desirable criteria
job-related competency | A demonstrable capability connected to the work. | assess job-related competencies
behavioral evidence | Specific actions showing how someone handled a situation. | request behavioral evidence
structured interview | An interview using consistent questions and evaluation standards. | conduct a structured interview
behavioral question | A question asking about an actual past action or experience. | ask a behavioral question
situational question | A question asking how someone would address a supplied scenario. | use a situational question
scoring rubric | Stated standards used to assign assessment ratings. | apply the scoring rubric
rating anchor | A description illustrating a particular score level. | define rating anchors
interview panel | The group responsible for interviewing or assessing candidates. | brief the interview panel
candidate pipeline | Applicants at different stages of the recruitment process. | review the candidate pipeline
screening call | An initial conversation checking relevant requirements and interest. | arrange a screening call
shortlist | Candidates selected for a further assessment stage. | develop a shortlist
selection rationale | The evidence-based explanation for a selection decision. | document the selection rationale
affinity bias | Favoring someone because of perceived similarity to oneself. | challenge affinity bias
halo effect | Allowing one favorable impression to dominate unrelated judgments. | check for the halo effect
calibration | Aligning assessors' use of the stated rating standards. | hold a calibration discussion
work sample | A job-related task used to observe relevant performance. | evaluate a work sample
candidate experience | How applicants experience the recruitment process and communication. | improve the candidate experience
reasonable adjustment | A change intended to reduce a relevant barrier, under applicable rules. | discuss a reasonable adjustment
offer approval | Internal authorization for the terms of a proposed job offer. | obtain offer approval
time to fill | Elapsed time between defined vacancy and hiring milestones. | state the time-to-fill basis''',
    precision='Good cultural fit is too vague to score consistently. Define the actual behavior: following up on commitments and raising deadline conflicts. A shared interest, accent, or outgoing manner does not itself establish either competency.',
    precision_extra='Consistent questions and common criteria support comparison; identical treatment does not mean ignoring legitimate access needs. Follow the applicable adjustment process. A recruitment metric also needs defined start and end events before its duration is comparable.',
    phrases='''Clarify the preference | What specific work behavior do you mean by good fit?
Return to the role | The role requires client follow-up and timely escalation.
Separate the criteria | Which requirements are essential and which are desirable?
Ask for evidence | Tell us about a time you handled two conflicting deadlines.
Follow the action | What did you do, and what happened next?
Avoid social scoring | Shared hobbies are not evidence of this competency.
Define a rating | What would distinguish a strong answer from an adequate one?
Keep comparison consistent | Use the same core questions and rating standards.
Challenge an impression | Confidence alone does not tell us whether the commitments were met.
Calibrate the panel | Let us compare the evidence against the agreed anchors.
Keep access open | Explain the assessment and the route for requesting an adjustment.
Record the rationale | Link the score to the candidate's actual example.
Separate stages | A shortlist decision is not an approved offer.
Respect the candidate | Tell applicants when they can expect the next update.
Avoid an invented promise | We have not made a selection decision yet.
Close the preparation | Confirm the criteria before the panel starts scoring.''',
    notes='''Fit | Ask fit for which task and on what evidence.
Confident | Describes presentation, not necessarily competence.
Essential | A genuine minimum requirement, not merely a preference.
Consistent | Common assessment standards with appropriate access arrangements.
Selected | Identify the stage; shortlisted and hired are different.
Fast | A shorter process does not prove a better selection decision.''',
    d='''Which interview question best targets the stated work? | Describe a deadline conflict, your escalation, and the outcome. | Which sports does our manager enjoy? | Would you describe yourself as universally confident? | Do you share the panel's favorite interests? | A concrete example can reveal the required escalation behavior and its result.
A panelist says, "I liked their energy, so I scored follow-up highly." What is the best response? | Which example shows how they followed through on a client commitment? | Good energy proves every competency. | Replace the score with the panelist's favorite number. | Ignore all evidence because interviews are subjective. | The question redirects an impression toward evidence relevant to the competency being scored.
What belongs in a selection rationale? | Relevant evidence linked to the agreed criteria | A guess about the candidate's private life | A record of shared hobbies as proof of competence | The assumption that fluency guarantees reliability | A defensible explanation connects the observed response to the stated assessment standard.
Which candidate update is supported before selection? | We are completing interviews and will update you on the stated date. | You have the job because the interview felt positive. | All offer terms are approved. | No further communication is needed. | A process update can be promised without falsely announcing a hiring outcome.''',
    dialogue='''Marcus | I want someone who will fit the team. The current draft says confident, approachable, and easy to work with, which sounds reasonable to me.
Lina | Those impressions need a [[job-related competency::The competency must connect the preference to required work rather than social similarity.]]. For this coordinator, the actual requirements are client follow-up and escalation when deadlines conflict.
Marcus | I see the difference. Someone might be pleasant in an interview but still leave a client waiting or conceal a delivery problem until it becomes urgent.
Lina | Exactly. Let us start with the [[role profile::The role profile defines the position's work before candidate preferences become assessment criteria.]] and describe the actions we need. Then the panel can look for evidence rather than a familiar personality.
Marcus | Could we ask candidates to describe a time when two clients needed something at once? I would want to hear how they handled the competing commitments.
Lina | That is a useful [[behavioral question::A behavioral question asks for an actual past example, here involving conflicting client commitments.]]. Follow it with what they did, who they contacted, and the result, using the same core prompts across candidates.
Marcus | We should probably decide what a strong response sounds like before hearing the first person. Otherwise the most polished answer may set our standard.
Lina | We need a [[scoring rubric::A scoring rubric supplies the common standards for judging responses before the panel scores candidates.]] with clear evidence levels. Strong delivery should not compensate for an example that never explains how the deadline conflict was handled.
Marcus | One panelist likes people who share the team's interests. I understand the impulse, but that does not show whether someone can manage client commitments.
Lina | That is where [[affinity bias::Affinity bias favors perceived similarity, such as shared interests, rather than evidence of relevant capability.]] can enter. Bring the discussion back to the required work without turning the panel review into an argument about who seems friendly.
Marcus | After each interview, should we compare scores immediately? I want disagreements about evidence to surface before the final shortlist discussion.
Lina | Use the agreed [[rating anchors::Rating anchors describe score levels so assessors can explain why particular evidence earns a rating.]] when comparing judgments. Ask which part of the example supports the score, not merely whether everyone liked the candidate.
Marcus | Some candidates will have questions about the assessment format. We should explain it early enough for them to raise any access needs.
Lina | Yes. A [[structured interview::A structured interview uses common questions and standards while allowing appropriate access arrangements.]] does not mean refusing an appropriate adjustment. Explain the process and route requests through the relevant procedure without making assumptions about the person.
Marcus | We also need to tell candidates when they will hear from us. A long silence can make a well-organized interview feel careless.
Lina | That affects the [[candidate experience::Candidate experience includes the clarity and reliability of recruitment communication, not just the interview itself.]]. Set a realistic update date and keep it even if the decision is still pending; an update need not be an offer.
Marcus | For the final discussion, I want notes showing why someone progressed. "Good fit" on its own will not help us explain the comparison later.
Lina | Record the [[selection rationale::The selection rationale links the decision to relevant evidence and agreed criteria rather than a vague impression.]] against the criteria. Distinguish the candidate's actual example from our interpretation, and do not add details they never supplied.
Marcus | Agreed. We will revise the criteria, brief the panel, and complete the interviews. No one should imply an offer is ready merely because a candidate was shortlisted.
Lina | Correct. [[Offer approval::Offer approval is authorization for proposed employment terms, separate from shortlisting or a positive interview.]] is a separate stage. Today we are making the assessment clearer, not deciding a winner before we have compared the relevant evidence.''',
    transfer_title='A score needs an example',
    transfer_setup='A panelist awards a high teamwork score because an applicant shares a hobby. The interview notes contain no teamwork example. No hiring decision is approved.',
    transfer='''Recruiter: "A shared hobby is not job-related ___." | evidence | The hobby does not demonstrate the teamwork behavior the panel needs to assess.
Manager: "We need an example against the agreed ___." | criterion | The assessment must refer to the stated teamwork requirement rather than personal similarity.
Recruiter: "The score needs a supported ___." | rationale | A rating needs an explanation connected to actual relevant evidence.
Manager: "No offer has been ___." | approved | The supplied facts explicitly leave the hiring decision without approval.'''))

BOOK['units'].append(unit(
    title='Onboarding and Role Clarity',
    scene='The laptop is ready; the role is not',
    skill='Clarify first-month priorities, success criteria, support, and decision authority without confusing access with readiness.',
    brief='New coordinator Evan has working accounts and equipment on day three, but no agreed first-month priorities. Manager Nora brings a proposed plan: review five sample cases by day ten, process live cases under supervision by day twenty, and hold a readiness review on day thirty. Sample-case checks cover required fields and the escalation route. Independent case ownership requires Nora\'s sign-off. The onboarding checklist currently says complete because the equipment and account tasks are finished.',
    cast='Evan | New coordinator\nNora | Line manager',
    culture=('Questions can show ownership', 'A new starter may hesitate to ask which task comes first or who can approve a decision. Clear questions reduce rework. Managers can make expectations usable by naming the deliverable, standard, support person, and review point instead of asking someone simply to be proactive.'),
    a='''What is already complete? | Equipment and account setup | All role-specific learning | Independent case approval | The day-thirty readiness review | The checklist covers setup tasks, not the employee's full readiness for independent work.
What is proposed for day ten? | Review five sample cases | Take unrestricted ownership of every live case | Complete the day-thirty review early | Approve another employee's work | The proposed first milestone is five sample cases checked against the stated requirements.
What must precede independent case ownership? | Nora's sign-off | Having a working laptop alone | Reaching day three automatically | Assuming every account permission is decision authority | The brief explicitly requires the manager's sign-off before independent ownership.''',
    vocabulary='''onboarding | The process of helping a new employee enter and become effective in a role. | plan the onboarding
preboarding | Preparation completed before the employee's first working day. | coordinate preboarding
orientation | An introduction to the organization, people, and basic arrangements. | attend orientation
access provisioning | Creation of the required system accounts and permissions. | confirm access provisioning
role clarity | A shared understanding of responsibilities and expected outcomes. | establish role clarity
first-month plan | A sequence of priorities and reviews for the initial month. | agree a first-month plan
deliverable | A defined piece of work to be produced. | specify the deliverable
success criterion | A stated basis for judging whether work meets expectations. | agree success criteria
milestone | A meaningful point used to track progress. | set a learning milestone
ramp-up period | The time needed to reach the expected level of contribution. | support the ramp-up period
shadowing | Observing an experienced colleague carrying out work. | arrange job shadowing
supervised practice | Performing a task with appropriate oversight and support. | schedule supervised practice
buddy | A colleague assigned to help with everyday orientation and questions. | assign an onboarding buddy
line manager | The person with direct managerial responsibility for an employee. | confirm the line manager
stakeholder map | A guide to people affected by or involved in the role's work. | review the stakeholder map
decision authority | Permission to make specified decisions. | clarify decision authority
escalation route | The path for referring an issue beyond one's role or authority. | identify the escalation route
dependency | Something that must be available or completed for another task to proceed. | flag a dependency
check-in | A scheduled conversation about progress, needs, or concerns. | hold a weekly check-in
feedback loop | A process of using responses to improve subsequent work. | create a feedback loop
readiness review | An assessment of preparedness for a defined responsibility. | conduct a readiness review
sign-off | Explicit confirmation or approval by the authorized person. | obtain manager sign-off
independent ownership | Responsibility for carrying out defined work without routine supervision. | confirm independent ownership
onboarding completion | Completion of a defined onboarding scope, not automatically all role learning. | qualify onboarding completion''',
    precision='A completed equipment checklist establishes access, not competence or decision authority. Day thirty is a review point, not an automatic promise of independent ownership. The scope and approval condition must stay visible in the plan.',
    precision_extra='Five sample cases is a quantity; required fields and the escalation route are assessment criteria. A useful milestone combines the work, date, review basis, and support. Avoid describing someone as fully trained solely because a date has arrived.',
    phrases='''Distinguish setup | My accounts work, but the role priorities are not yet clear.
Ask for sequence | Which deliverable should I complete first?
Name the first milestone | Review five sample cases by day ten.
Define the check | We will check the required fields and the escalation route.
Separate practice stages | Live cases come next, with supervision.
Clarify the reviewer | Nora will review the sample cases with you.
Ask about authority | Which decisions can I make, and which should I refer?
Keep support visible | Bring unresolved cases to the named supervisor.
Qualify the date | Day thirty is a readiness review, not automatic authorization.
Confirm the condition | Independent ownership requires manager sign-off.
Raise a dependency | I need the sample-case access before I can complete that milestone.
Avoid vague effort | Let us define what ready looks like for this responsibility.
Set a check-in | We will review progress and questions at the scheduled meeting.
Correct the checklist | Mark system setup complete, with role learning still in progress.
Read back the plan | Samples first, supervised cases next, then a readiness review.
Close the agreement | Record the milestones, support, and sign-off requirement together.''',
    notes='''Ready | Ready for which responsibility and under what supervision?
Complete | Name the scope before using this status.
Access | A system permission is not necessarily authority to decide.
By | Gives a deadline; it does not guarantee approval on that date.
Own | Clarify responsibility and limits, not merely enthusiasm.
Review | An assessment point whose outcome is not predetermined.''',
    d='''Which checklist status is accurate on day three? | System setup complete; role learning not yet complete | Fully competent in every task | Independent ownership approved | All onboarding goals achieved | The completed tasks concern equipment and accounts, while role expectations remain to be agreed.
Which milestone is most usable? | Review five sample cases by day ten against fields and escalation criteria. | Be more proactive as soon as possible. | Learn everything quickly without asking questions. | Become fully ready whenever it feels appropriate. | The stated milestone supplies a quantity, date, and concrete basis for review.
What does the day-thirty meeting establish in advance? | A planned readiness assessment, not a guaranteed outcome | Automatic sign-off for independent work | Proof that supervision is already unnecessary | Permission to bypass unresolved questions | A scheduled review does not determine what the assessment will find.
How should Evan raise missing sample access? | I need access to the sample cases to meet the day-ten milestone. | The laptop works, so no dependency can exist. | I will mark the cases complete without opening them. | The milestone is irrelevant because accounts exist. | This statement connects a specific missing resource to the agreed work and date.''',
    dialogue='''Evan | My accounts and laptop are working, but the checklist says onboarding is complete. I still do not know which work matters most this month.
Nora | The checklist only confirms [[access provisioning::Access provisioning establishes working accounts and permissions, not readiness for the whole role.]]. We need to separate that setup from your learning plan and the responsibilities you will take on.
Evan | That would help. I have several training links and messages from colleagues, but no clear order or definition of what I should produce first.
Nora | Let us agree a [[first-month plan::The first-month plan puts the proposed learning tasks and review points into a clear sequence.]]. Start with five sample cases by day ten, then supervised live work by day twenty.
Evan | What will you check in the samples? I can count five completed files, but that would not tell me whether I handled them correctly.
Nora | We need explicit [[success criteria::Success criteria specify required fields and the escalation route, not just the number of completed cases.]]. I will check the required fields and whether you identified the correct escalation route for each case.
Evan | I also need to know what to do when a sample contains an unclear request. Should I choose an answer or bring the uncertainty to you?
Nora | Use the stated [[escalation route::The escalation route identifies where Evan should refer uncertainty beyond the scope of his current responsibility.]]. We are checking that you recognize the boundary, not rewarding guesses that happen to look decisive.
Evan | After the samples, I would like to see how a colleague handles live cases. The examples alone may not show the pace of the real queue.
Nora | We can arrange [[shadowing::Shadowing means observing an experienced colleague at work before or alongside practice.]] before your supervised cases. I will identify the colleague so you know who to ask about everyday workflow.
Evan | Will that colleague approve my work, or will you? I do not want friendly advice to become an approval I was never actually given.
Nora | I retain the defined [[decision authority::Decision authority distinguishes who can approve work from a colleague who provides informal guidance.]]. The colleague supports learning; the designated supervisor handles the live-case checks under the plan.
Evan | The day-thirty date sounds like a target for working independently. Should I tell other teams they can send cases directly to me from then?
Nora | Not yet. It is a [[readiness review::The readiness review assesses preparedness on day thirty without guaranteeing independent ownership then.]], not an automatic change in responsibility. We will assess the evidence and identify any remaining support you need.
Evan | Understood. I should describe the date as a review point and avoid promising independent handling before the approval is actually in place.
Nora | Correct. My [[sign-off::Sign-off is the explicit manager approval required before Evan takes independent ownership.]] is required for independent ownership. Account permissions alone do not change that condition, even if a system technically lets you open a case.
Evan | One practical point: the sample-case folder is not visible yet. I can access the general system, but that particular resource still needs to be added.
Nora | That is a [[dependency::The missing sample folder is a resource needed to complete the first milestone.]] for the first milestone. I will arrange the access and check progress with you rather than treating the existing setup tick as proof everything is available.
Evan | Let me confirm: five samples, then supervised live cases, then a readiness review. We will record the criteria and approval condition with those dates.
Nora | Yes. That gives us [[role clarity::Role clarity makes the responsibilities, sequence, support, and authority understandable to both parties.]]. I will correct the checklist to say system setup complete and role learning in progress, so other teams see the same boundaries.''',
    transfer_title='A date is not a sign-off',
    transfer_setup='A new employee completes account setup on Monday. Three sample cases are due Friday. Independent processing requires a supervisor review that has not yet occurred.',
    transfer='''Employee: "Account setup is ___." | complete | Monday's finished setup supports that status only for the accounts.
Manager: "The next milestone is three ___ cases." | sample | The briefing identifies three sample cases as the next defined task.
Employee: "Independent processing still requires a ___." | review | The supplied condition requires a supervisor assessment before independent processing.
Manager: "That approval is not yet ___." | confirmed | The required review has not occurred, so approval cannot be reported as confirmed.'''))

BOOK['units'].append(unit(
    title='Performance Feedback and Documentation',
    scene='Two missing summaries, not a personality verdict',
    skill='Give specific performance feedback, invite factual context, and record an observable improvement standard.',
    brief='Manager Priya and analyst Daniel review two weekly reports, dated September 11 and 18. Both omitted the summary section required by the agreed template, and Priya had to request it separately. A draft note calls Daniel careless and unmotivated. No explanation for the omissions has been established. Priya wants the next report, due September 25, to include the summary. This is a feedback meeting; no formal warning or disciplinary decision has been made.',
    cast='Priya | Team manager\nDaniel | Analyst',
    culture=('Direct feedback can remain respectful', 'Name the work and its effect without assigning a character flaw. Invite the employee to explain the sequence and barriers. A clear expectation is easier to act on than a softened hint, while a specific record is fairer than an unsupported judgment about motivation.'),
    a='''What was missing from the two reports? | The agreed summary section | Every data table | A signed disciplinary warning | All supporting calculations | The brief identifies one omitted section in each report, not wholesale failure of the work.
What does the draft note wrongly assume? | A motive and personality judgment not established by the facts | That the reports have dates | That a summary was required | That the manager requested the missing sections | Careless and unmotivated go beyond the observed omissions and imply unsupported explanations.
What is the current meeting status? | Feedback without a formal disciplinary decision | A completed dismissal | A confirmed final warning | A completed appeal outcome | The brief explicitly states that no formal warning or disciplinary decision has been made.''',
    vocabulary='''performance expectation | The standard of work or behavior required for a role. | clarify performance expectations
observable behavior | An action that can be specifically described or evidenced. | describe observable behavior
performance gap | A difference between expected and observed performance. | identify a performance gap
feedback conversation | A discussion of work, its effects, and improvement. | hold a feedback conversation
specific example | A concrete instance supporting the feedback. | give a specific example
impact statement | An explanation of the effect of the observed work or behavior. | make an impact statement
employee response | The employee's account, explanation, or comment. | record the employee response
barrier | A factor that may prevent the expected work. | explore a work barrier
attribution | An explanation assigning an outcome to a cause or person. | check the attribution
recency bias | Overweighting the most recent events when judging a longer period. | avoid recency bias
performance standard | A defined level or feature of acceptable work. | apply the performance standard
measurable objective | A target whose achievement can be checked against stated criteria. | agree a measurable objective
improvement action | A specified step intended to address a performance gap. | confirm the improvement action
support commitment | Assistance the manager or organization agrees to provide. | record the support commitment
review date | The planned date for checking progress or an outcome. | set a review date
contemporaneous note | A record made at or near the time of the event. | keep a contemporaneous note
factual record | Documentation distinguishing evidence from interpretation. | maintain a factual record
acknowledgment of receipt | Confirmation that a document was received, not necessarily agreed with. | obtain acknowledgment of receipt
informal coaching | Developmental guidance outside a stated formal disciplinary stage. | provide informal coaching
formal warning | A notice issued under an applicable formal employment process. | distinguish a formal warning
performance improvement plan | A structured plan specifying improvements, support, and review arrangements. | review the performance improvement plan
calibration meeting | A discussion aligning performance ratings with common standards. | prepare for a calibration meeting
right of response | An opportunity to answer a concern under the relevant process. | provide a right of response
follow-up evidence | Later information used to assess whether the agreed change occurred. | review follow-up evidence''',
    precision='The observed fact is that two dated reports lacked a required section. That supports feedback about completeness, not a conclusion that Daniel is unmotivated. An employee explanation is a reported account until the relevant facts are checked.',
    precision_extra='Receipt of a note does not necessarily mean agreement with its contents. Label the actual meeting stage accurately. A measurable next step names the report, required section, due date, and review method without silently converting coaching into a formal warning.',
    phrases='''Open with the work | I want to discuss the September 11 and 18 reports.
Name the gap | Both reports omitted the agreed summary section.
State the impact | I had to request the summary separately before completing my review.
Invite context | Please walk me through how you prepared those reports.
Avoid a motive claim | I have not established why the section was missing.
Separate the account | You explained that you used an older template.
Verify the document | Let us compare that file with the agreed version.
Keep the standard clear | The September 25 report needs the summary section.
Offer specific support | I will send the current template and confirm the required section.
Define the check | We will review completeness against that template.
Correct the label | The note should describe the omissions, not call you unmotivated.
Preserve disagreement | We can record your response without pretending we agree on every point.
Clarify the stage | This meeting is feedback, not a formal warning.
Distinguish receipt | Acknowledging receipt does not necessarily mean agreeing with the note.
Close the next step | Confirm the report date, required section, and review arrangement.
Assess the follow-up | Judge the next submission against the agreed standard.''',
    notes='''Always | Usually overstates a pattern when only two examples are supplied.
Careless | A judgment that should not replace a description of the work.
Explained | Attributes an account without automatically verifying it.
Agreed | Specify agreement on the standard, facts, or action.
Received | Does not by itself mean accepted as accurate.
Improved | Identify the evidence and comparison supporting the claim.''',
    d='''Which opening is most precise? | The September 11 and 18 reports omitted the required summary. | You never care about your work. | Your personality is the problem. | Every report you have ever written is wrong. | Two dated examples support a specific completeness concern, not a universal character judgment.
Daniel says he used an older template. What should the note say before verification? | Daniel said he used an older template; the file will be checked. | The manager has proven every omission was a system fault. | Daniel admitted having no motivation. | No explanation was offered. | Attribution preserves the employee's account while keeping its verification status clear.
Which objective is measurable? | Include the required summary in the September 25 report and check it against the agreed template. | Care much more from now on. | Become a better person immediately. | Never have another difficulty of any kind. | The objective identifies the work, required feature, date, and review basis.
What does a receipt acknowledgment alone establish? | The note was received | Every statement in it is agreed | A formal warning was issued | The employee waived every possible concern | Receipt is a communication fact and should not be treated as agreement or a disciplinary outcome.''',
    dialogue='''Priya | I want to discuss the reports dated September eleventh and eighteenth. Both arrived without the summary section required by the template we agreed to use.
Daniel | I understand the [[performance gap::The performance gap is the missing required summary, not a judgment about Daniel's character.]]. I included the tables, but not the summary. Could we check which template I actually used before deciding why that happened?
Priya | Yes. The missing section meant I had to come back to you before finishing my review. I want to explain that effect without guessing at your motivation.
Daniel | That [[impact statement::The impact statement explains the extra request and delayed review caused by the omission.]] helps me understand the consequence. I thought the tables were the full submission because the file I opened did not include the summary heading.
Priya | Please show me the file and walk me through how you prepared the reports. I want to distinguish a document problem from any other possible explanation.
Daniel | I will provide it as part of my [[employee response::The employee response is Daniel's explanation, which the manager can record and check.]]. My account is that I used an older version, but we should compare the documents before treating that as verified.
Priya | Agreed. The draft note says careless and unmotivated. Those words do not describe what we have established, so I will replace them with the dated omissions.
Daniel | A [[factual record::A factual record separates the observed omissions from unsupported motive judgments and unverified explanations.]] would be more accurate. Please keep my explanation in the note too, including that the version question still needs checking.
Priya | I will. For the next submission, the expectation is unchanged: the September twenty-fifth report must contain the summary section as well as the supporting tables.
Daniel | That gives us a clear [[performance standard::The performance standard specifies the summary and supporting tables required in the next report.]]. I would like the current template so I can check the exact section before I submit.
Priya | I will send the agreed file today and confirm which heading to use. We can also check whether another shared folder still contains the outdated version.
Daniel | Please record that [[support commitment::The support commitment is the manager's specific promise to provide and clarify the current template.]]. It addresses the document issue without removing my responsibility to make sure the required section is present.
Priya | Exactly. We will review the next report against that template. The action should be specific enough that neither of us has to infer what improvement means.
Daniel | Then the [[measurable objective::The measurable objective is a complete September 25 report checked against the specified template.]] is to include the summary in the next dated report, not simply to sound more committed in this meeting.
Priya | Correct. I also want the record to show the stage accurately. This is a feedback discussion; I have not issued a formal warning or made a disciplinary decision.
Daniel | Thank you for distinguishing [[informal coaching::Informal coaching describes the stated feedback stage rather than inventing a formal disciplinary outcome.]] from a formal process. I can acknowledge the concern while still asking for my explanation to be recorded accurately.
Priya | I will send the revised note for you to read. Please identify any factual errors, and confirm receipt so I know the record reached you.
Daniel | I can provide [[acknowledgment of receipt::Acknowledgment of receipt confirms the note arrived without automatically agreeing to every statement.]]. That should not be described as agreement with every sentence if there is still a point we need to correct.
Priya | Understood. We will retain the actual response and check the next submission. The evidence of improvement will be what the report contains, not a promise alone.
Daniel | That makes the [[follow-up evidence::Follow-up evidence is the next report assessed against the agreed completeness standard.]] clear. I will use the confirmed template, include the summary, and raise any remaining version conflict before the due date.''',
    transfer_title='Record the event, not a motive',
    transfer_setup='Two timesheets lacked project codes. The employee says the code list was unavailable; this has not been verified. The next timesheet must include the codes by Friday.',
    transfer='''Manager: "Two timesheets omitted the project ___." | codes | The observable issue is the missing codes in two specified records.
Employee: "My explanation is that the list was ___." | unavailable | The supplied employee account identifies unavailable information as the reported barrier.
Manager: "That explanation still needs to be ___." | verified | The briefing explicitly says the reported cause has not yet been checked.
Employee: "The corrected next timesheet is due ___." | Friday | The stated next deadline is Friday, not an unspecified future improvement date.'''))

BOOK['units'].append(unit(
    title='Employee Relations and Investigations',
    scene='Receive the concern without deciding the case',
    skill='Listen empathetically, attribute accounts accurately, and explain process limits without promising secrecy or a finding.',
    brief='Employee Tomas tells HR adviser Imani that colleague Reed excluded him from two project meetings and made a dismissive comment on September 15. Tomas recalls the words but has not supplied the invitations or messages. He thinks another colleague may have heard the comment; that has not been checked. Imani is receiving the first account, not deciding whether misconduct occurred. Tomas asks whether the conversation can remain entirely secret and whether Reed will be disciplined.',
    cast='Tomas | Employee raising a concern\nImani | HR adviser',
    culture=('Empathy is not a verdict', 'Thank someone for raising a concern and explain what you can do next. Taking the account seriously does not require declaring it proven. Equally, an incomplete record is not a reason to dismiss the person. Be candid about appropriate information sharing and avoid guarantees about another employee.'),
    a='''What evidence is available at the start? | Tomas's initial account | A completed investigation finding | Confirmed witness testimony from everyone present | Verified invitations and message records | The brief supplies one account while documents and possible witness information remain unchecked.
What is Imani's role in this conversation? | Receive and clarify the concern | Announce Reed's discipline | Decide a legal claim immediately | Guarantee that no one else will ever know | This is an intake conversation, not a completed investigation or outcome meeting.
What is known about the possible witness? | Tomas thinks someone may have heard the comment. | The colleague has already confirmed every word. | The colleague has denied being present. | The colleague issued a disciplinary decision. | Possible witness knowledge is reported but has not been established by a direct account.''',
    vocabulary='''employee relations | Work addressing the employment relationship and workplace concerns. | manage employee-relations concerns
intake | The initial receipt and clarification of a concern. | conduct an intake conversation
allegation | A claim about conduct that requires appropriate assessment. | record an allegation
complainant | A person raising a complaint under a defined process. | contact the complainant
respondent | A person responding to an allegation under the relevant process. | hear the respondent's account
firsthand account | Information from someone who directly experienced or observed an event. | distinguish a firsthand account
reported account | Information attributed to the person who supplied it. | attribute a reported account
corroboration | Independent information supporting an account. | seek corroboration
contemporaneous record | A document or note created at or near the event. | preserve contemporaneous records
chronology | Events arranged in time order. | establish the chronology
witness | Someone who may have relevant knowledge about an event. | identify a possible witness
neutral question | A question that does not assume the desired answer or conclusion. | ask a neutral question
leading question | A question suggesting the answer or assuming a contested fact. | avoid leading questions
scope of inquiry | The issues and boundaries to be examined. | define the scope of inquiry
impartiality | An approach not favoring a person or predetermined conclusion. | maintain impartiality
conflict of interest | A connection or interest that could compromise fair handling. | disclose a conflict of interest
confidentiality | Appropriate protection and restricted handling of information. | explain confidentiality limits
need-to-know basis | Sharing information with people who require it for a legitimate purpose. | share on a need-to-know basis
retaliation concern | A concern about adverse treatment connected to protected conduct or reporting. | raise a retaliation concern
interim measure | A temporary arrangement pending review, not itself a finding. | explain an interim measure
evidence preservation | Keeping relevant original information available and intact. | arrange evidence preservation
finding | A conclusion reached through the applicable assessment process. | distinguish a finding from an allegation
substantiated | Supported under the relevant process and evidential standard. | explain a substantiated finding
case update | Information about the progress or status of a concern. | provide a case update''',
    precision='Write Tomas reported that he was excluded, not Reed deliberately excluded Tomas as an established finding. Record exact words only when they are actually supplied, and label uncertain recollection. A possible witness is not yet corroboration.',
    precision_extra='Appropriate confidentiality is different from absolute secrecy. Explain the actual sharing limits and process without imposing a blanket gag rule or restricting protected reporting. An interim arrangement or an intake note does not prove guilt or determine discipline.',
    phrases='''Acknowledge the concern | Thank you for bringing this to me.
Invite the sequence | Please describe what happened and when.
Clarify direct knowledge | Which parts did you personally see or hear?
Separate recollection | Are those the exact words you remember, or a summary?
Request the record | Please identify the relevant invitations and messages.
Attribute the account | I will record this as your account of the events.
Keep the witness status open | We have not yet heard from the possible witness.
Avoid prejudgment | I cannot determine the outcome from this conversation alone.
Explain information handling | I will handle the information carefully and explain appropriate sharing.
Avoid an absolute promise | I cannot promise that no one else will need to know.
Clarify the next step | The concern will go through the applicable review process.
Keep reporting available | Please raise any further concern, including possible retaliation.
Preserve the original | Keep the relevant messages in their original form.
Distinguish a temporary measure | A temporary arrangement is not itself a finding.
Set a realistic update | I will contact you on Friday with the current process status.
Check the note | Please tell me if my summary misstates what you reported.''',
    notes='''Reported | Identifies the source without deciding the truth of the claim.
Alleged | Describes a claim under review, not an insult or a dismissal.
Confirmed | Requires adequate verification, not repetition of one account.
Confidential | Does not mean that relevant people can never receive information.
Unsubstantiated | Does not automatically mean deliberately false.
Resolved | Clarify whether the process ended, an action occurred, or the person feels satisfied.''',
    d='''Which intake note is most accurate? | Tomas reported exclusion from two meetings; invitations have not yet been reviewed. | Reed is guilty because Tomas spoke first. | No concern exists because documents are missing. | Every colleague confirmed deliberate exclusion. | The note attributes the report and preserves the missing-evidence status without prejudging the case.
Which question avoids assuming misconduct? | What happened at the September 15 meeting, and who was present? | Why was Reed deliberately humiliating you again? | Which punishment should we announce today? | How can we prove the conclusion we already reached? | A neutral question seeks the event and participants rather than embedding a contested conclusion.
What is the best response to a request for total secrecy? | Explain careful handling and the limits of necessary, appropriate sharing. | Promise that no person can ever learn anything. | Publish the account to the whole team. | Require silence about every concern in every setting. | Honest limits allow appropriate review without making a promise the adviser may be unable to keep.
What does a temporary separation arrangement establish by itself? | A temporary process measure, not a finding of guilt | That every allegation is proven | That the respondent has admitted the conduct | That no review is needed | An interim measure manages the situation while the assessment remains separate.''',
    dialogue='''Tomas | I was left out of two project meetings, and Reed made a dismissive comment on September fifteenth. I am worried that bringing this up will make things worse.
Imani | Thank you for telling me. This [[intake::Intake is the initial receipt and clarification of the concern, not a decision about its outcome.]] is for understanding your account and explaining next steps, not announcing a conclusion.
Tomas | I can describe the comment, although I would like a moment to remember the exact words. I do not have the invitations open right now.
Imani | We can build a [[chronology::A chronology places the meetings and comment in time order so the account can be examined accurately.]] first. Please separate what you remember clearly from anything you are unsure about, and identify the meetings as specifically as you can.
Tomas | The comment was said directly to me. The reason I think I was excluded from the meetings is that I heard about them afterward from someone else.
Imani | That distinction matters. The comment is part of your [[firsthand account::A firsthand account concerns what Tomas directly heard, unlike his inference about why invitations were missing.]], while the meeting information has another source. I will not combine them as though you directly observed everything.
Tomas | I think a colleague nearby may have heard the comment, but I have not asked them. I do not want to tell you they confirmed something they have not confirmed.
Imani | I will identify them as a possible [[witness::The colleague is only a possible witness because their presence and knowledge have not yet been checked.]]. We have not heard their account, so the note should not present their involvement as independent confirmation.
Tomas | Can you keep this entirely secret? I am uneasy about Reed hearing a different version of what I said before I have checked the summary.
Imani | I will explain the limits of [[confidentiality::Confidentiality involves careful information handling, not a guarantee that no appropriate person will need access.]]. I will handle the information carefully, but others may need to know to address the concern.
Tomas | I understand the distinction, though it still feels difficult. I would like to know how information is shared and whom I can contact if something changes.
Imani | Appropriate sharing should be on a [[need-to-know basis::A need-to-know basis limits sharing to legitimate process needs rather than general workplace circulation.]]. I will explain the process and contact route without restricting protected reporting rights.
Tomas | Will Reed be disciplined? Part of me wants a clear answer now, but I realize you have only heard from me.
Imani | We have an [[allegation::An allegation is a claim requiring assessment; the intake does not establish a disciplinary outcome.]], not a finding. The relevant review needs to examine the information fairly, and I cannot promise a particular outcome from this conversation.
Tomas | I can provide the messages and identify the invitations I expected. Some details may support my interpretation, while others may show something I did not know.
Imani | Preserve the originals for [[evidence preservation::Evidence preservation keeps relevant original messages and records available without changing them to fit an account.]]. We need the actual records, including context, rather than edited extracts that accidentally leave out information relevant to the concern.
Tomas | My biggest worry is what happens after I raise this. If my assignments suddenly change, I would want someone to examine that rather than assume it is unrelated.
Imani | Please report any [[retaliation concern::A retaliation concern should be raised and assessed, not dismissed or automatically treated as a proven legal violation.]] through the available route. We should record the facts and assess the concern, not pre-decide either that retaliation occurred or that it could not occur.
Tomas | Before we finish, could you read back the main points? I want the note to distinguish my recollection, what I inferred, and what still needs checking.
Imani | Yes, and I will give you a [[case update::A case update reports process status without promising that the review will be finished or a particular result reached.]] on Friday. That is a commitment to communicate the status, not a promise that the review or an outcome will be complete then.''',
    transfer_title='A report is not yet corroboration',
    transfer_setup='An employee reports a comment and names a possible witness. The witness has not been contacted. HR has promised a Tuesday status update, not an outcome.',
    transfer='''Adviser: "The note records the employee's ___." | account | The note attributes the information to the person who supplied it.
Manager: "The possible witness has not yet been ___." | contacted | The briefing says the witness has not been approached for information.
Adviser: "The review has not produced a ___." | finding | The current record contains a report, not an assessed conclusion.
Manager: "Tuesday is the promised status ___." | update | The promised event is communication about progress, not a guaranteed outcome.'''))

BOOK['units'].append(unit(
    title='Compensation, Benefits, and Equity',
    scene='The midpoint is not an automatic salary',
    skill='Explain pay-range calculations and policy criteria while keeping fairness concerns and individual decisions open.',
    brief='Employee Alex earns a USD 72,000 annual base salary in a role with a published USD 60,000-100,000 range. Alex assumes the USD 80,000 midpoint is what everyone should receive. HR partner Maya has a fictional policy stating that placement depends on role level, relevant experience, and an internal-equity review; midpoint placement is not automatic. A separate 5% target bonus is conditional, not guaranteed. No individual pay-review outcome or discrimination finding is supplied.',
    cast='Alex | Employee\nMaya | HR partner',
    culture=('Explain without shutting down the concern', 'A correct calculation does not settle whether an individual pay decision is fair. Explain the range and the review process, then address the actual question. Avoid using policy language as a way to dismiss a concern, promise a raise, or discourage legitimate discussion of pay.'),
    a='''What is the range midpoint? | USD 80,000 | USD 72,000 | USD 60,000 | USD 100,000 | The midpoint is the average of the 60,000 minimum and 100,000 maximum.
What does the fictional policy say about midpoint placement? | It is not automatic. | Everyone must immediately receive it. | It equals the guaranteed bonus. | It replaces the individual review. | The supplied policy lists placement criteria and expressly rejects an automatic midpoint entitlement.
What is the status of the 5% target bonus? | Conditional, not guaranteed | Already paid | Included in the stated base salary | A confirmed salary increase | The brief distinguishes the target bonus from base pay and says its payment is conditional.''',
    vocabulary='''base salary | Fixed contractual salary before separate variable payments and benefits. | state the annual base salary
salary range | The stated minimum-to-maximum pay interval for a defined role or level. | publish a salary range
range minimum | The lower bound of the defined pay range. | identify the range minimum
range maximum | The upper bound of the defined pay range. | identify the range maximum
midpoint | The central value of the defined range. | calculate the midpoint
compa-ratio | Base salary divided by the relevant range midpoint. | calculate the compa-ratio
range penetration | The share of the minimum-to-maximum interval reached by the salary. | calculate range penetration
pay grade | A category grouping roles within a compensation structure. | confirm the pay grade
job level | A defined category of responsibility and scope. | verify the job level
job evaluation | Assessment of a role's relative requirements or value within a structure. | conduct a job evaluation
market benchmark | External pay information used for a defined comparison. | review the market benchmark
internal equity | Consistency and fairness of pay relationships within an organization. | review internal equity
pay compression | A narrowing of pay differences between roles or experience levels. | examine pay compression
pay disparity | A difference in compensation requiring a defined comparison and context. | investigate a pay disparity
pay transparency | Openness about pay information, ranges, or decision processes. | explain pay transparency
merit increase | A pay increase linked to performance under the applicable policy. | review a merit increase
promotion increase | A pay change associated with moving to a higher-level role. | distinguish a promotion increase
market adjustment | A pay change intended to address relevant external market positioning. | assess a market adjustment
variable pay | Compensation dependent on specified results or conditions. | distinguish variable pay
target bonus | A reference bonus amount subject to the plan's actual conditions. | explain the target bonus
total cash compensation | Base pay plus the relevant cash incentive payments. | define total cash compensation
total rewards | The wider package of pay, benefits, and other employment value. | describe total rewards
benefits eligibility | The conditions for participating in a particular benefit. | confirm benefits eligibility
compensation review | A process for examining pay under the relevant criteria. | request a compensation review''',
    precision='The midpoint is (60,000 + 100,000) / 2 = 80,000. Compa-ratio is 72,000 / 80,000 = 90%. Range penetration is (72,000 - 60,000) / (100,000 - 60,000) = 30%. The two percentages answer different questions.',
    precision_extra='Five percent of 72,000 is a 3,600 target bonus, not guaranteed pay. Being inside a range does not by itself establish fair or lawful treatment; being below midpoint does not by itself establish an error. Review the actual criteria and facts.',
    phrases='''Acknowledge the question | I understand why the published midpoint prompted your question.
State the base | Your annual base salary is 72,000 dollars.
Explain the range | The published range runs from 60,000 to 100,000.
Calculate the center | The midpoint is 80,000 dollars.
Separate policy from inference | The policy does not promise midpoint pay to every employee.
Name the criteria | Placement uses role level, relevant experience, and an internal-equity review.
Define the ratio | Your base salary is 90% of the midpoint.
Avoid a percentage mix-up | Thirty percent is range penetration, not the compa-ratio.
Separate the bonus | The 5% target is conditional variable pay.
Quantify the target | At this base salary, the target amount is 3,600 dollars.
Avoid guaranteed totals | A target total is not a promise of the actual payout.
Keep fairness open | These calculations do not settle your individual equity concern.
Invite the specific concern | Which aspect of the placement or comparison would you like reviewed?
Use the proper route | I can explain the compensation-review process and required facts.
Avoid an unsupported outcome | I cannot promise a raise before the review.
Close with accountability | I will confirm the review owner and next update.''',
    notes='''Range | Describes an interval, not each employee's individual entitlement.
Midpoint | A reference value, not necessarily the average actual salary.
Target | An incentive reference, not guaranteed payment.
Equity | Requires relevant comparisons and context, not a single ratio.
Within range | Does not settle all fairness or legal questions.
Review | A process whose individual result remains to be determined.''',
    d='''What is Alex's compa-ratio? | 90% | 30% | 5% | 120% | Dividing the 72,000 base salary by the 80,000 midpoint gives 0.90, or 90%.
What does 30% represent here? | Salary position across the 60,000-100,000 interval | Salary as a share of the midpoint | The guaranteed annual raise | The employee's actual bonus payout | The salary is 12,000 above the minimum across a 40,000 range width, giving 30%.
Which statement handles the fairness question properly? | The range calculation does not replace review of your individual concern. | Inside the range means every possible concern is invalid. | Below midpoint proves discrimination without further facts. | Discussing the range automatically approves a raise. | Numerical position alone neither resolves the concern nor establishes a legal conclusion.
A different salary is 84,000 and its midpoint is 80,000. What is the compa-ratio? | 105% | 95% | 5% | 80% | Dividing 84,000 by 80,000 gives 1.05, or 105% of midpoint.''',
    dialogue='''Alex | The posting shows a range of sixty thousand to one hundred thousand dollars. I earn seventy-two thousand, so why am I not receiving the eighty-thousand midpoint?
Maya | Let us separate your [[base salary::Base salary is the fixed annual pay being compared with the range, excluding the conditional bonus.]] from the range references and the bonus. I also want to understand your individual fairness concern, not just explain the arithmetic.
Alex | I assumed the middle was the normal amount everyone in the role should get. Otherwise I do not understand what publishing the middle means.
Maya | The [[midpoint::The midpoint is the central range reference, 80,000 dollars, not an automatic individual salary under this policy.]] is a reference value. Our supplied policy uses role level, relevant experience, and internal-equity review; it does not automatically place every person at the center.
Alex | Could you show how my salary compares with it? I have seen two different percentages and do not know whether one of them is wrong.
Maya | Your [[compa-ratio::Compa-ratio divides 72,000 base salary by the 80,000 midpoint, producing 90%.]] is ninety percent: seventy-two thousand divided by eighty thousand. That tells us salary relative to midpoint, not how far you are through the full range.
Alex | The other figure is thirty percent. It sounds much lower, which is why I thought someone might have calculated the comparison incorrectly.
Maya | That is [[range penetration::Range penetration measures 12,000 above minimum across a 40,000 range width, producing 30%.]]. You are twelve thousand above the minimum across a forty-thousand interval, so thirty percent answers a different question from the midpoint ratio.
Alex | That explains the numbers, but it does not tell me whether my experience was counted properly. I would like the placement decision examined.
Maya | We can use the [[compensation review::The compensation review examines individual placement under the stated criteria rather than inferring fairness from one ratio.]] process for that question. I will identify the responsible reviewer and the relevant facts rather than treat a position inside the range as the whole answer.
Alex | I also want to understand comparisons with similar work. I am not asking you to dismiss other people's circumstances, but the reasoning should be consistent.
Maya | That is part of [[internal equity::Internal equity concerns consistent and fair pay relationships, requiring relevant comparison rather than an unsupported individual conclusion.]]. Relevant role scope and experience need examination. I cannot announce the result of that assessment before it has happened.
Alex | The compensation statement also lists a five-percent bonus. Should I add that to salary and describe the total as money I will definitely receive?
Maya | No. A [[target bonus::The target bonus is conditional, so the calculated 3,600 amount cannot be treated as guaranteed payment.]] is not a guaranteed payout. Five percent of your current base is thirty-six hundred dollars, but the plan conditions determine any actual payment.
Alex | So seventy-five thousand six hundred would be base plus the target illustration, not a guaranteed cash amount for the year.
Maya | Correct. [[Variable pay::Variable pay depends on specified conditions and must be distinguished from fixed base salary.]] needs its conditions stated. An actual cash total uses actual relevant payments; a target illustration should be labeled as such.
Alex | I would also like to understand where benefits belong. The statement seems to move between salary, bonus, and a much wider package.
Maya | That wider view is [[total rewards::Total rewards includes benefits and other employment value beyond base salary and cash incentives.]]. It can include benefits and other elements, but those should not be presented as though each were an additional dollar of base salary.
Alex | Thank you. Please confirm who will review the placement and when I will hear back. I understand that asking does not itself approve an increase.
Maya | I will confirm that and keep the [[pay disparity::A pay disparity is a difference to examine with relevant facts, not automatically proof of an unlawful decision.]] question open for proper review. Neither a range explanation nor a target bonus replaces an answer to your specific concern.''',
    transfer_title='A ratio and a target',
    transfer_setup='Annual base salary is USD 54,000, the range midpoint is USD 60,000, and the conditional target bonus is 10% of base. No actual payout is confirmed.',
    transfer='''Employee: "My compa-ratio is ___ percent." | ninety | Dividing 54,000 by the 60,000 midpoint gives ninety percent.
HR: "The target bonus is 5,400 ___." | dollars | Ten percent of the 54,000 base produces a 5,400-dollar target amount.
Employee: "That target is not ___." | guaranteed | The briefing describes a conditional incentive, not a guaranteed payout.
HR: "The actual payout remains ___." | unconfirmed | No actual payment has been confirmed in the supplied facts.'''))

BOOK['units'].append(unit(
    title='Policy Communication and Compliance',
    scene='Received is not approved or refused',
    skill='Acknowledge a work-adjustment request promptly and explain an individualized review without collecting unnecessary sensitive information.',
    brief='Manager Sana receives a request from an employee to start at 9:30 rather than 8:30 from October 7 for a health-related reason. HR adviser Ben has not reviewed it. The request gives the desired schedule but does not explain the work barrier or coverage implications. No decision or temporary arrangement is approved. Sana asks whether the request is automatically accepted, or whether the standard-hours policy permits an immediate refusal. Ben must clarify the process and information boundaries.',
    cast='Sana | Department manager\nBen | HR adviser',
    culture=('Be prompt without pretending certainty', 'Acknowledge the request and arrange the appropriate discussion. A standard rule does not answer every individual case, and a request does not itself establish a decision. Ask about relevant work needs through the correct process; avoid making an employee disclose sensitive details in a team forum.'),
    a='''What change has the employee requested? | A 9:30 start instead of 8:30 from October 7 | A confirmed permanent promotion | An approved change for every employee | A completed medical determination | The briefing states a requested schedule change, not a broader employment decision.
What is the current status? | Received but not yet reviewed or decided | Automatically accepted | Formally refused after review | Implemented as a temporary arrangement | HR has not reviewed the request and no arrangement has been approved.
Which information still needs appropriate clarification? | The work barrier and relevant coverage implications | The employee's complete private history for the whole team | A predetermined reason to deny the request | A diagnosis invented by the manager | The brief identifies work-related questions while sensitive information requires appropriate handling.''',
    vocabulary='''accommodation request | A request for a change addressing a relevant workplace barrier under applicable rules. | acknowledge an accommodation request
work adjustment | A change to working arrangements intended to address a stated need. | discuss a work adjustment
interactive process | A discussion to clarify needs and explore an effective arrangement. | engage in the interactive process
essential function | A fundamental duty of the position under the applicable framework. | identify essential functions
functional limitation | A restriction affecting the performance of an activity. | clarify a functional limitation
workplace barrier | A feature of work that creates a relevant difficulty or limitation. | identify a workplace barrier
individualized assessment | A review of the particular person's circumstances and work needs. | conduct an individualized assessment
effective accommodation | An arrangement that addresses the relevant barrier. | assess an effective accommodation
alternative arrangement | Another proposed way of addressing the stated need. | explore an alternative arrangement
modified schedule | A change to the employee's usual work hours or timing. | assess a modified schedule
coverage requirement | A stated need for staffing or task availability at particular times. | clarify coverage requirements
interim arrangement | A temporary measure pending a fuller decision or review. | confirm an interim arrangement
implementation date | The date an authorized arrangement is to begin. | confirm the implementation date
review checkpoint | A planned point for checking progress or effectiveness. | set a review checkpoint
supporting documentation | Relevant information used to assess a request under the proper process. | handle supporting documentation
medical confidentiality | Appropriate protection of medical information. | preserve medical confidentiality
restricted access | Limiting information access to authorized people and purposes. | maintain restricted access
data minimization | Collecting only information needed for the legitimate purpose. | apply data minimization
policy owner | The person or function responsible for a policy's interpretation and upkeep. | consult the policy owner
policy exception | An authorized departure from a general rule, where applicable. | document a policy exception
undue hardship | Under the US disability framework, significant difficulty or expense assessed in context. | assess undue hardship
request status | The current stage of a request, distinct from its outcome. | communicate request status
decision rationale | The supported explanation for an authorized decision. | document the decision rationale
review route | The applicable path for questioning or revisiting a decision. | explain the review route''',
    precision='The requested start date is not an approved implementation date. Acknowledgment confirms receipt, not acceptance or refusal. An individualized process should clarify the relevant barrier and work requirements rather than treating a general schedule rule as the entire decision.',
    precision_extra='Do not request a full medical history in a group email. Any necessary supporting information must follow the appropriate confidential process. The book does not determine eligibility, effectiveness, undue hardship, or what information a real employer may lawfully require.',
    phrases='''Acknowledge promptly | We have received your request and will arrange the appropriate discussion.
State the status | The request has not yet been reviewed or decided.
Clarify the need | What work barrier is the requested schedule intended to address?
Separate dates | October 7 is the requested start date, not a confirmed implementation date.
Use the right channel | Any necessary sensitive information should go through the designated confidential route.
Avoid a blanket refusal | The standard-hours policy does not replace an individual review.
Avoid automatic approval | Receipt of a request is not confirmation of the arrangement.
Identify the work need | We need a clear description of the relevant coverage requirements.
Explore alternatives | An alternative must address the actual barrier, not merely be easier to offer.
Keep authority clear | Confirm who can approve an interim arrangement.
Protect the information | Share only what is appropriate for the person's role in the process.
Limit the manager's question | I need the relevant work information, not a team-wide medical explanation.
Give a realistic checkpoint | I will confirm the next review step and contact date.
Distinguish recommendation | A proposed arrangement is not yet an authorized change.
Explain the outcome properly | Communicate the actual decision and its supported rationale through the proper process.
Keep questions possible | Explain the available review route without discouraging the request.''',
    notes='''Requested | Describes what the employee asks for, not a completed decision.
Reasonable | A framework-dependent assessment, not a casual synonym for convenient.
Effective | Addresses the actual barrier, not merely the appearance of action.
Temporary | Still needs clear scope, authority, and timing.
Medical | Sensitive information, not ordinary team-update content.
Policy | Apply with relevant law and individual facts; do not assume it answers everything.''',
    d='''Which first response is appropriate? | Acknowledge receipt and arrange the relevant discussion without promising the outcome. | Tell the team the employee's health details. | Approve automatically without review. | Refuse automatically because a standard schedule exists. | The response is prompt and useful while preserving the need for an appropriate individual assessment.
How should October 7 be described now? | The requested start date | The approved implementation date | The date of a completed refusal | Proof that review is unnecessary | The employee requested that date, but the relevant decision has not been made.
Which information request respects the stated boundary? | Clarify the work barrier and use the designated route for any necessary sensitive support. | Ask the employee to publish their complete medical history. | Ask coworkers to guess a diagnosis. | Collect unrelated private information just in case. | Relevant work questions and appropriately handled supporting information avoid unnecessary disclosure.
What makes a proposed alternative useful? | It addresses the actual barrier and is assessed through the applicable process. | It uses the word flexible in its title. | It is convenient for the manager regardless of the need. | It bypasses every approval and review question. | An alternative needs relevant effectiveness and proper assessment, not merely attractive wording.''',
    dialogue='''Sana | An employee has asked to start at nine thirty instead of eight thirty from October seventh for a health-related reason. Does receiving the message mean I should approve it?
Ben | No. Acknowledge the [[accommodation request::The accommodation request starts a relevant review; receipt alone does not decide the arrangement.]] promptly and arrange the appropriate discussion. We have not reviewed the individual circumstances or approved an arrangement.
Sana | Our handbook lists the standard hours. I wondered whether I could simply quote that section and say the schedule cannot change.
Ben | The rule does not replace an [[individualized assessment::An individualized assessment considers the particular need and work circumstances rather than applying a blanket answer.]]. We need to understand the relevant need and work requirements, not jump from the existence of standard hours to a final refusal.
Sana | The message gives the preferred schedule, but not the difficulty it is intended to address. I want to ask a useful question without becoming intrusive.
Ben | Ask about the [[workplace barrier::The workplace barrier is the relevant difficulty the requested schedule is intended to address.]] through the appropriate process. We need enough relevant information to understand the request, not a public explanation of the employee's entire health history.
Sana | Would you handle any supporting health information? I do not want the employee to send it to a group mailbox that the whole department can open.
Ben | Yes, we will use the designated route for [[medical confidentiality::Medical confidentiality requires appropriate handling of sensitive information, separate from ordinary team circulation.]]. Any necessary supporting information should reach the authorized people under the applicable procedure, not become a general team update.
Sana | On the work side, some tasks occur early, but I should establish what coverage is actually required rather than assume every task must happen at eight thirty.
Ben | Clarify the [[essential functions::Essential functions are the fundamental duties that help frame the work assessment, not every customary scheduling preference.]] and the actual coverage needs. Separate a real task requirement from a customary schedule before treating them as interchangeable.
Sana | Could a different schedule or another arrangement address the difficulty? I want to leave room for options without promising one before we understand the need.
Ben | That is part of the [[interactive process::The interactive process clarifies needs and explores effective options through discussion, not a predetermined outcome.]]. An alternative has to address the relevant barrier; offering something unrelated does not become effective just because it sounds flexible.
Sana | The employee asked to begin on October seventh. Should I tell payroll or the scheduling team that date is already confirmed?
Ben | Not as an [[implementation date::An implementation date belongs to an authorized arrangement; October 7 remains only the requested date here.]]. It is the requested start date. We should move the review forward promptly and keep the status clear rather than quietly turn the request into an approved instruction.
Sana | What if there is a need for something temporary while the review continues? I should not improvise a promise outside my authority.
Ben | Any [[interim arrangement::An interim arrangement is a temporary measure that still needs appropriate authority and clearly stated terms.]] needs the relevant authorization and clear terms. A temporary label does not remove the need to state what is approved, for whom, and for how long.
Sana | I can acknowledge the message today, explain who will contact the employee, and identify the work information the review needs. I should avoid predicting its result.
Ben | Exactly. Communicate [[request status::Request status names the current process stage, here received and awaiting review, rather than an invented outcome.]] accurately. Also establish a contact point and update time so the employee is not left wondering whether the request has disappeared.
Sana | If a decision is eventually made, we need to explain it clearly and provide the applicable route for questions, rather than send a bare yes or no.
Ben | Include the supported [[decision rationale::The decision rationale explains the authorized outcome based on the review, not an assumption made at intake.]] through the proper process. For now, the accurate message is received, review being arranged, and no decision or temporary schedule confirmed yet.''',
    transfer_title='Keep the requested date separate',
    transfer_setup='An employee requests a schedule change from Monday. HR has acknowledged it, but assessment and approval are pending. No interim arrangement exists.',
    transfer='''Manager: "Monday is the ___ start date." | requested | The employee asked for Monday, but the arrangement has not been authorized.
HR: "The request has been ___." | acknowledged | HR has confirmed receipt without deciding the substance of the request.
Manager: "The assessment is still ___." | pending | The briefing states that the review is not yet complete.
HR: "No interim arrangement is ___." | approved | No temporary arrangement exists under the supplied facts.'''))

BOOK['units'].append(unit(
    title='Conflict Mediation and Manager Coaching',
    scene='Clarify the handoff before assigning blame',
    skill='Coach a manager to separate positions from work needs and define a testable handoff without inventing shared fault or agreement.',
    brief='Manager Ken asks HR coach Daria for help with Rosa and Felix, who each say the other should own the weekly account reconciliation. Their role notes never assigned that recurring task. Ken proposes a two-week trial: Rosa assembles the inputs by Monday noon, Felix checks them by Tuesday 10:00, and Ken approves the result by Tuesday 15:00. The colleagues have not yet discussed or accepted the proposal. No misconduct allegation is supplied.',
    cast='Ken | Team manager\nDaria | HR coach',
    culture=('A shared problem does not prove shared fault', 'A manager can clarify a work arrangement without deciding that both people were equally to blame. Distinguish the missing responsibility from the accusations. A facilitated task discussion may help here; it should not be treated as a substitute for the proper response to serious misconduct or protected complaints.'),
    a='''What underlying gap is established? | The recurring task was never assigned in the role notes. | Both colleagues signed the same clear ownership plan. | A formal investigation proved equal misconduct. | Ken already approved both completed reconciliations. | The brief identifies an undocumented responsibility, not a proven refusal to follow an agreed assignment.
Who would approve the result under Ken's proposal? | Ken | Rosa alone | Felix alone | An unnamed client automatically | The proposed sequence names Ken as the approver by Tuesday 15:00.
What is the status of the two-week trial? | Proposed, not yet discussed or accepted by the colleagues | Already completed successfully | A permanent policy accepted by everyone | A disciplinary sanction already issued | The briefing expressly states that the colleagues have not yet discussed or accepted the proposal.''',
    vocabulary='''task ownership | Responsibility for ensuring a defined task is carried through. | clarify task ownership
role ambiguity | Uncertainty about responsibilities or expectations. | reduce role ambiguity
position | A person's stated demand or preferred outcome in a disagreement. | distinguish a position
underlying interest | The need or concern behind a stated position. | identify underlying interests
facilitated discussion | A conversation guided to clarify issues and possible arrangements. | arrange a facilitated discussion
mediation | A structured process using an impartial third party to help parties seek agreement. | assess whether mediation is appropriate
ground rule | An agreed condition for how a discussion will proceed. | establish ground rules
active listening | Listening that checks meaning before responding. | use active listening
paraphrase | A restatement used to check understanding of another person's meaning. | offer a neutral paraphrase
reframing | Restating a conflict in terms that clarify the issue or shared work need. | use constructive reframing
common ground | A relevant aim or fact the parties share. | identify common ground
boundary | A stated limit on responsibility, conduct, or authority. | clarify the boundary
handoff | Transfer of work or information between responsible people. | define the handoff
handoff criterion | The condition a work item must meet before transfer. | agree handoff criteria
responsibility matrix | A record showing who performs, approves, or supports each task. | update the responsibility matrix
accountable owner | The person answerable for the defined result. | name the accountable owner
consulted party | Someone whose input is sought before a relevant decision or action. | identify consulted parties
escalation trigger | A stated condition requiring an issue to be referred. | define an escalation trigger
working agreement | An explicit arrangement about how people will coordinate work. | record a working agreement
trial period | A limited time for testing an arrangement. | set a trial period
review meeting | A planned discussion assessing the arrangement or progress. | schedule a review meeting
action log | A record of tasks, owners, dates, and status. | maintain an action log
coaching question | A question helping someone examine facts and choose a responsible action. | ask a coaching question
false equivalence | Treating unequal or unestablished conduct as if responsibility were the same. | avoid false equivalence''',
    precision='The missing assignment is established; equal fault is not. Rosa preparing inputs, Felix checking, and Ken approving are three distinct responsibilities. A proposed sequence does not become a working agreement merely because it looks clear on paper.',
    precision_extra='A deadline needs a usable handoff criterion and a route for missing inputs. The trial should have a defined duration and review. Do not claim that both colleagues agreed before hearing and recording their actual responses.',
    phrases='''Start with the known gap | The role notes do not assign the recurring reconciliation.
Avoid a blame shortcut | We have not established that both people failed an agreed duty.
Separate the positions | Each person says the other should own the task.
Ask about the need | What information or authority does each person need to complete their part?
Reframe the issue | We need a reliable weekly handoff, not a contest over who cares more.
State the proposed sequence | Rosa prepares inputs, Felix checks, and Ken approves.
Name the dates | Inputs Monday noon, checks Tuesday 10:00, approval Tuesday 15:00.
Define transfer quality | Specify what complete inputs must contain before they are handed over.
Make a blockage visible | A missing-input problem needs a named escalation route.
Keep the proposal honest | The two-week trial has not yet been accepted.
Check understanding | Ask each colleague to restate their task and the handoff.
Preserve a disagreement | Record any remaining objection instead of writing agreement prematurely.
Assign accountability | Ken remains the named approver in this proposal.
Limit the trial | Review the arrangement after two weekly cycles.
Use the appropriate process | A task discussion does not replace formal handling of a serious complaint.
Close with a record | Document the actual arrangement, owners, deadlines, and review point.''',
    notes='''Both | Do not use it to manufacture equal responsibility.
Help | Too vague unless the task and timing are named.
Own | Clarify doing, checking, approving, or overall accountability.
Agree | Requires actual assent to the stated arrangement.
Trial | A bounded test, not a permanent policy by implication.
Neutral | Fair process does not mean ignoring evidence of unequal conduct.''',
    d='''Which opening avoids an unsupported blame judgment? | The reconciliation task was not assigned; let us clarify the required handoff. | Both people are equally guilty by definition. | One must be lazy because they disagree. | The role notes prove a clear assignment to both. | The opening uses the established documentation gap instead of assuming motive or equal fault.
What must be added to "send the inputs Monday"? | What complete inputs contain and how missing information is escalated | A guess about each colleague's personality | A claim that the trial already succeeded | A permanent punishment for every possible delay | A useful handoff needs a defined content standard and response to missing information.
Which summary preserves the proposal's status? | Ken proposes a two-week trial; the colleagues' responses are still needed. | Everyone has accepted a permanent arrangement. | The trial has passed two successful cycles. | Neither colleague has any right to raise a practical concern. | The supplied facts establish a proposal, not acceptance or evidence of successful operation.
Why is automatic equal blame inappropriate? | The facts do not establish equivalent conduct or a previously assigned duty. | Every disagreement always has exactly equal causes. | Clarifying ownership requires finding both people guilty. | The manager must ignore all evidence to stay neutral. | Fair handling follows the evidence rather than forcing an equal-fault conclusion.''',
    dialogue='''Ken | Rosa and Felix each say the other should handle the weekly reconciliation. I was going to tell them both to stop blaming each other and cooperate.
Daria | First address the [[role ambiguity::Role ambiguity is the missing assignment in the role notes, which must be clarified before assuming a breached duty.]]. The role notes never assigned this recurring task, so cooperation alone will not tell them who must prepare, check, or approve it.
Ken | That is true. Rosa says it belongs with Felix's reporting work, while Felix says Rosa has the client information and should own the whole task.
Daria | Those are their stated [[positions::Positions are the competing claims about ownership; the underlying practical needs may be different.]]. Ask what each needs to do the work reliably, including information, timing, and authority, instead of treating either statement as the complete explanation.
Ken | I can see a shared aim: the account needs to be reconciled on time. We need a workable sequence rather than another conversation about attitude.
Daria | Use that [[common ground::Common ground is the shared need for a reliable, timely reconciliation rather than assumed agreement on responsibility.]] to frame the discussion. It does not prove they agree about ownership, but it gives them a concrete result to organize the work around.
Ken | My proposal is for Rosa to assemble the inputs by Monday noon, Felix to check them by Tuesday ten, and me to approve by Tuesday fifteen hundred.
Daria | Put that in a [[responsibility matrix::A responsibility matrix distinguishes preparing, checking, and approving instead of assigning vague shared ownership.]]. Three named stages are clearer than saying both own it, provided the boundaries and resources are actually workable.
Ken | I also need to define what Rosa sends. Otherwise Felix may receive an incomplete file and the same conflict will reappear at the next stage.
Daria | Agree the [[handoff criterion::The handoff criterion specifies what complete inputs must contain before Felix receives the work.]] for those inputs. A deadline is not enough if the receiver cannot tell whether the transferred work is complete and usable.
Ken | What if information from a client is missing by Monday noon? I do not want the plan to hide a dependency neither colleague controls.
Daria | Define an [[escalation trigger::An escalation trigger makes a missing-input problem visible through a stated referral point instead of silent delay.]] and who receives it. That should expose the missing input early without implying either person can invent the information to satisfy the timetable.
Ken | I want to test this for two weeks and review the results. I should still hear their practical objections before writing that the arrangement is agreed.
Daria | Correct. A [[trial period::A trial period limits the proposed arrangement to two weeks and creates a defined opportunity to assess it.]] is a proposal until the relevant discussion and authorization occur. Record what is actually decided, including any point that remains unresolved.
Ken | I had also planned to ask them both to apologize. But the documentation gap does not show that they were equally responsible for the earlier failures.
Daria | Avoid [[false equivalence::False equivalence would assign equal fault without evidence of equal conduct or an agreed prior responsibility.]]. You can address any supported behavior separately without manufacturing equal blame simply to make the conversation look balanced.
Ken | Would a joint task discussion be appropriate here? There is no misconduct allegation in the information I have given you, just a recurring ownership dispute.
Daria | A [[facilitated discussion::A facilitated discussion can clarify the stated task dispute but is not a substitute for appropriate handling of other serious concerns.]] may help clarify this work arrangement. If a different or serious concern emerges, use the relevant process rather than forcing every issue into an ownership compromise.
Ken | I will ask each person to restate the task, timing, and missing-input route. Then I can record the actual arrangement and review it after two cycles.
Daria | That produces a usable [[working agreement::A working agreement records the actual coordination arrangement, not a proposal falsely described as accepted.]] if the discussion supports it. Keep your approval responsibility explicit, and evaluate the trial against completed handoffs rather than the absence of visible disagreement.''',
    transfer_title='Proposed is not agreed',
    transfer_setup='A manager proposes that Ana prepares a file Monday, Bo checks it Tuesday, and the manager approves it Wednesday. Neither colleague has yet responded.',
    transfer='''HR: "Ana's proposed role is to ___ the file." | prepare | The proposal assigns Ana the preparation stage rather than checking or approval.
Manager: "Bo would ___ it on Tuesday." | check | The stated second stage is Bo's Tuesday check.
HR: "The manager would give ___ on Wednesday." | approval | The proposal reserves the final approval stage for the manager.
Manager: "The colleagues' responses remain ___." | pending | Neither colleague has responded, so their acceptance cannot yet be reported.'''))

BOOK['units'].append(unit(
    title='Restructuring and Sensitive Communication',
    scene='Do not call possible job losses small changes',
    skill='Communicate a restructuring proposal with empathy while separating confirmed facts, possible impacts, and unfinished decisions.',
    brief='HR director Mei and communications lead Owen review a restructuring announcement. Twelve positions are within the proposal\'s review scope, but no final position-elimination count or individual outcome is confirmed. The draft says small changes and no one should worry. A Friday 11:00 staff update is scheduled; it is not a promised decision date. Mei wants a clear message that acknowledges potential employment consequences, explains what remains open, and points employees to an appropriate contact without inventing assurances.',
    cast='Mei | HR director\nOwen | Communications lead',
    culture=('Reassurance should not erase the stakes', 'People may hear an upbeat phrase as evasive when their employment could be affected. Name the proposal and uncertainty plainly, acknowledge the impact, and offer a real contact and update. Avoid implying that an unfinished decision is final or that a genuine risk does not exist.'),
    a='''What does the number twelve describe? | Positions in the proposal's review scope | Confirmed dismissals | The final severance payment | A completed list of affected individuals | The brief defines a review scope, not a final count of eliminated roles or individual outcomes.
What is confirmed for Friday at 11:00? | A staff update | A final decision on every position | Guaranteed confirmation that no jobs are affected | Every employee's departure time | The scheduled event is a communication update, explicitly not a promised decision deadline.
Why is "small changes" unsuitable here? | It minimizes possible employment consequences. | It accurately states a verified small impact. | It gives the final position count. | It identifies the complete consultation process. | The draft minimizes a potentially serious effect that has not yet been determined.''',
    vocabulary='''restructuring | A change to how an organization arranges its work, roles, or reporting. | communicate a restructuring proposal
operating model | The arrangement through which an organization delivers its work. | review the operating model
business rationale | The stated business reason for a proposed change. | explain the business rationale
review scope | The roles, activities, or issues included in an assessment. | define the review scope
role impact | The effect of a change on a position's work or existence. | assess role impact
at-risk position | A position potentially affected, not necessarily finally eliminated. | clarify at-risk positions
position elimination | Removal of a defined role from the organizational structure. | distinguish position elimination
headcount | A count of people under a specified employment definition. | state the headcount basis
redeployment | Moving an employee into another suitable role under the relevant process. | explore redeployment
consultation | A process for seeking and considering relevant views under applicable arrangements. | conduct meaningful consultation
selection criteria | The defined basis for a relevant choice among roles or people. | explain selection criteria
individual notification | Communication to a particular person about their situation. | arrange individual notification
notice period | The applicable interval between employment notice and its effective end. | confirm the notice period
severance | Separation-related pay or arrangements under applicable terms and rules. | explain severance terms
transition support | Assistance during a change in role or employment. | provide transition support
retention risk | The possibility of losing employees the organization seeks to retain. | assess retention risk
manager briefing | Information given to managers so they can communicate accurately. | prepare a manager briefing
talking points | Key statements supporting a consistent conversation. | approve talking points
message cascade | Planned communication through successive organizational levels. | coordinate the message cascade
rumor | Unverified information circulating informally. | address a rumor accurately
confirmed fact | Information established sufficiently for the stated communication. | distinguish confirmed facts
open question | An issue for which a supported answer is not yet available. | record open questions
employee assistance program | A workplace support service whose scope depends on the actual program. | explain the employee assistance program
change fatigue | Strain associated with repeated or prolonged organizational change. | acknowledge change fatigue''',
    precision='Twelve positions in scope does not mean twelve people will leave. Roles, current incumbents, and final employment outcomes are different categories. Friday 11:00 is the next update; it is not evidence that all decisions will be complete then.',
    precision_extra='Do not promise no job losses, guaranteed redeployment, or particular separation terms without authority and supporting facts. Consultation, notification, representation, notice, and benefit obligations vary. A communication exercise cannot establish which legal process applies to a real restructuring.',
    phrases='''Name the proposal | We are reviewing a restructuring proposal that may affect positions.
State the scope | Twelve positions are within the current review scope.
Separate the outcome | That is not a confirmed count of positions to be eliminated.
Avoid false comfort | We should not say no one will be affected when that is not known.
Acknowledge the stakes | I recognize that this uncertainty can be difficult for employees.
Preserve the status | No final individual outcome is confirmed in this briefing.
Explain what is missing | We cannot yet give a supported final count.
Distinguish the event | Friday at 11:00 is the next staff update, not a promised decision date.
Keep the update | We will communicate the current status even if questions remain open.
Prepare managers | Give managers the same confirmed facts and limits.
Handle a rumor | We have not confirmed that claim and should not repeat it as a decision.
Avoid invented benefits | Do not promise a package or redeployment option before its terms are established.
Give a contact | Name the appropriate route for individual questions.
Protect personal information | Use the appropriate individual process for personal employment details.
Invite relevant questions | Record unanswered questions and assign follow-up ownership.
Close with honesty | State what is known, what remains open, and when the next update will occur.''',
    notes='''Small | Can minimize a serious personal consequence even if the organizational scope is limited.
May | Signals possibility, not a hidden confirmation of a final outcome.
In scope | Included in a review, not necessarily selected for elimination.
Consultation | Should not be described as open if the relevant choice is already irreversibly decided.
Support | Name the service and its actual scope; do not imply a guaranteed replacement job.
Update | A communication event that can report continuing uncertainty.''',
    d='''Which announcement accurately states the number? | Twelve positions are under review; final eliminations are not confirmed. | Twelve employees have definitely been dismissed. | No position can possibly be affected. | The number twelve is the guaranteed redeployment total. | Review scope and final outcomes are different categories under the supplied facts.
Which phrase offers empathy without an unsupported guarantee? | I recognize this uncertainty is difficult, and we will provide the next update Friday. | Nobody has any reason to worry because all jobs are safe. | Everyone will receive a guaranteed replacement role. | This is too minor for questions. | The statement acknowledges the stakes and promises a real communication event without inventing job security.
What should managers do with a rumor about a final list? | Distinguish it from confirmed facts and use the authorized question route. | Repeat it as a decision because several people heard it. | Create an unofficial list from guesses. | Promise the opposite without evidence. | Repetition does not verify a rumor, and unsupported counter-assurances are equally unreliable.
If decisions remain open on Friday, what should the update say? | State the current status, unresolved questions, and next contact arrangements. | Pretend the review is complete to avoid discomfort. | Cancel all future communication without explanation. | Announce a random final number. | The promised update can honestly report continuing uncertainty while keeping follow-up concrete.''',
    dialogue='''Owen | The draft announcement calls this small changes and says no one should worry. I was trying to keep the tone calm, but those phrases may go too far.
Mei | They minimize the possible [[role impact::Role impact includes potential changes to positions or employment, which the draft should not trivialize.]]. People may face serious consequences, and we do not yet know the final outcome. Calm language still needs to acknowledge that.
Owen | We know that twelve positions are being examined. Some readers may assume that means twelve people have already been selected to leave.
Mei | Call it the [[review scope::Review scope identifies the twelve positions being assessed, not a final elimination count or individual decision.]]. Twelve positions are within the proposal's assessment, but that is not a confirmed position-elimination count or an individual notification.
Owen | Should the message explain why the organization is considering a change? Otherwise people may hear a threat without any explanation of its purpose.
Mei | Use the approved [[business rationale::The business rationale explains the reason for the proposal but must come from actual approved information.]] when it is available. Do not invent savings, performance problems, or strategic reasons merely to make the announcement sound complete.
Owen | We also need to distinguish a proposal from a final decision. I do not want an unfinished process presented as though employees are hearing the outcome.
Mei | Correct. If [[consultation::Consultation involves seeking and considering views under the applicable process, not disguising a completed choice as open.]] is part of the applicable process, describe it accurately. The message must not suggest a choice is open when it has already been settled, or settled when it remains open.
Owen | Friday at eleven is booked for a staff update. I originally wrote that everyone would know their position then, which is more than we have agreed.
Mei | That is not a [[confirmed fact::The confirmed fact is the scheduled update, not a promise that all individual decisions will be ready.]]. The appointment is an update, not a promised decision date. We must communicate the current status even if the review is unfinished.
Owen | Managers will receive questions before Friday. They need a common basis for answering without filling gaps from their own assumptions or informal conversations.
Mei | Prepare a [[manager briefing::A manager briefing gives leaders the same established facts, uncertainty boundaries, and contact routes.]] with what is known, what remains open, and the contact route. It should help them acknowledge questions without improvising employment assurances.
Owen | There is already a rumor about a final list. Should the announcement deny it outright, even though we have not checked the specific claim?
Mei | Address the [[rumor::A rumor is unverified information and should not become a confirmed decision through repetition or unsupported denial.]] with the actual verified status. We should neither repeat an unconfirmed list nor promise the opposite just to counter it.
Owen | People may also ask about alternative roles or separation arrangements. It would be tempting to promise broad support now and work out the details later.
Mei | Do not promise guaranteed [[redeployment::Redeployment concerns another suitable role under the relevant process and cannot be guaranteed without established options.]] or a particular package. Explain only the support and process that are actually established, with the appropriate route for individual questions.
Owen | We should keep personal employment information out of the broad announcement. A general update should not become an accidental disclosure about a named person.
Mei | Use the appropriate [[individual notification::Individual notification addresses a particular person's situation through the proper process rather than a general announcement.]] process when there is an actual supported message for that person. Do not imply it has happened merely because the staff update is scheduled.
Owen | I will replace small changes with a clear description of the proposal and potential impact. The closing will acknowledge uncertainty and confirm Friday's update.
Mei | Also record each [[open question::Open questions remain visibly unanswered with follow-up ownership instead of being filled by invented assurances.]] with a follow-up owner. Employees deserve a truthful account of what we know and a reliable next contact, even when we cannot yet supply the answer they most want.''',
    transfer_title='Scope is not an outcome',
    transfer_setup='Eight positions are included in a proposal review. Final changes are not decided. A Wednesday 14:00 update is scheduled, with no guaranteed individual outcome then.',
    transfer='''HR: "Eight positions are in the review ___." | scope | The number describes positions included in assessment, not a final elimination count.
Manager: "Final changes are not yet ___." | decided | The supplied facts leave the final outcome open.
HR: "Wednesday at 14:00 is the next ___." | update | The scheduled event is communication about status rather than a guaranteed decision.
Manager: "We cannot promise an individual ___ then." | outcome | No individual decision has been guaranteed for that appointment.'''))
