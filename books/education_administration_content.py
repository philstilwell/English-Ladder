"""Original learner-book content for education administration."""
from books.authoring import unit

BOOK = dict(
    slug='education-administration',
    title='Education Administration English',
    cover_label='ENGLISH FOR EDUCATION ADMINISTRATION',
    cover_title='Education\nAdministration',
    cover_size=32,
    tagline='Explain the process. Support the learner.',
    audience='For admissions teams, school administrators, program coordinators, and education managers.',
    map_intro='Eight school and program decisions: explain an admissions outcome, align learning and assessment, review support, repair a family message, calibrate grading, limit record access, report review evidence, and compare staffing options.',
    notes_title='Clear language, fair processes',
    notes_intro='An education administrator often connects people who use the same words differently: families, teachers, reviewers, and budget holders. State the relevant rule, the available evidence, and the next authorized step.',
    field_notes=[
        ('Name the actual process', 'Eligibility, selection, enrollment, and placement are different stages. A person can meet entry conditions without receiving a place when capacity is limited.', '"The application met the eligibility criteria; the published allocation process determined the offer."'),
        ('Separate observation from interpretation', 'Describe recorded attendance, submitted work, or a documented action before making a claim about motivation, support, or learning.', '"The record shows three late arrivals; it does not establish the reason."'),
        ('Make the next step usable', 'Specify the responsible person, date, channel, and decision needed. An invitation to talk should not sound like a finding of fault.', '"Please confirm whether Tuesday at 08:45 works, and whether you need an interpreter."'),
        ('Keep claims within the evidence', 'A completed action does not by itself prove improved outcomes. A policy, an implemented practice, and evidence of effectiveness serve different purposes.', '"The action is complete; the outcome review is still scheduled for next month."')],
    scope_note='All institutions, people, figures, deadlines, and local procedures in the scenarios are fictional. Admissions, safeguarding, disability support, privacy, employment, and accreditation requirements vary by institution and jurisdiction. Use the applicable approved process and qualified advice; this book teaches communication, not legal or safeguarding decisions.',
    sources=[
        dict(title='Carnegie Mellon University, Eberly Center. Align Assessments, Objectives, and Instructional Strategies.', url='https://www.cmu.edu/teaching/assessment/basics/alignment.html', note='Background for aligning observable learning outcomes, instruction, and assessment. The source-comparison exercise and rubric cases are original.', checked='30 September 2026'),
        dict(title='Attendance Works. Positive Engagement.', url='https://www.attendanceworks.org/resources/transition-guide/a-district-transitions-planning-guide/positive-engagement/', note='Background for supportive attendance communication and family engagement. The school schedules, targets, and attendance records are fictional.', checked='30 September 2026'),
        dict(title='U.S. Department of Education. School Officials and Legitimate Educational Interest.', url='https://studentprivacy.ed.gov/faq/what-must-educational-agencies-or-institutions-do-ensure-only-school-officials-legitimate', note='A U.S. FERPA reference on access to education records. The book does not assume FERPA applies to every institution or replace local privacy review.', checked='30 September 2026'),
        dict(title='Higher Learning Commission. Updated: HLC\'s Providing Evidence.', url='https://www.hlcommission.org/learning-center/news/updated-hlcs-providing-evidence/', note='Background for relevant, persuasive evidence of existence, use, and effectiveness. The fictional program review does not represent an accreditation decision.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Enrollment, Admissions, and Placement',
    scene='Eligible, but no place available yet',
    skill='Explain an allocation decision without disclosing other applicants or promising a future offer.',
    brief='Admissions officer Leena speaks with guardian Mr. Ortiz about a fictional program with 20 places and 24 eligible applicants. The published process uses a lottery among eligible applicants. His child met the entry criteria but was not selected and is fourth on the waiting list. The local procedure allows a factual-error review requested within five school days of the decision notice. A review is not a second lottery, and no vacancy is confirmed. Leena may explain the family\'s own record and published process, not other applicants\' information.',
    cast='Leena | Admissions officer\nMr. Ortiz | Guardian',
    culture=('Explain the rule without sounding dismissive', 'A family may hear a capacity decision as a judgment about the child. Acknowledge that concern, distinguish eligibility from selection, and give a precise next step. Warmth does not require predicting a waiting-list outcome or discussing another family.'),
    a='''Why was an offer not made? | The eligible applicant was not selected in the capacity-limited lottery. | The child failed the entry criteria. | The application was submitted late. | A factual-error review has already rejected the case. | The brief confirms eligibility but states that the lottery did not select the applicant.
What is the current waiting-list position? | Fourth | First | Twentieth | Twenty-fourth | The child's supplied waiting-list position is fourth, not the total number of applicants.
What does the local review procedure examine? | A claimed factual error in the application decision | A guaranteed new place | Another family's private record | A new lottery requested by any guardian | The fictional procedure provides a factual-error review, not an automatic second allocation.''',
    vocabulary='''admissions | The process of considering applicants for entry. | explain the admissions process
applicant | A person seeking entry to a program. | contact an applicant
eligibility | Meeting the conditions for consideration. | confirm eligibility
entry criteria | The published conditions an applicant must satisfy. | apply entry criteria
selection | Choosing among applicants for available places. | explain the selection process
capacity | The number of places available. | state program capacity
oversubscribed | Having more applicants than available places. | an oversubscribed program
allocation | Assignment of available places under a process. | review place allocation
lottery | A random selection process among an eligible group. | conduct a published lottery
offer | A formal invitation to take an available place. | issue an offer
waiting list | A list of applicants awaiting possible vacancies. | confirm a waiting-list position
vacancy | An available, unfilled place. | confirm a vacancy
decision notice | The communication of an application outcome. | send a decision notice
factual error | An incorrect statement or record of fact. | identify a factual error
review request | A request to examine a decision under a stated process. | submit a review request
review window | The period allowed for requesting review. | explain the review window
school day | A day counted under the institution's school-day definition. | count five school days
supporting document | Material supplied to substantiate a claim. | attach a supporting document
enrollment | Formal registration after the applicable admission steps. | complete enrollment
placement | Assignment to an appropriate class, level, or setting. | discuss class placement
intake | A group admitted during a particular entry period. | plan the next intake
confidential record | Information subject to restricted access or disclosure. | protect confidential records
published procedure | An officially available description of the process. | follow the published procedure
acknowledgment | Confirmation that a message or request was received. | send an acknowledgment''',
    precision='Eligibility means the applicant meets the conditions for consideration. It does not guarantee selection in an oversubscribed program. Selection, acceptance of an offer, enrollment, and class placement should not be treated as interchangeable.',
    precision_extra='The five-school-day window belongs to this fictional institution. Explain the actual deadline from the decision notice in a real case. Fourth on the waiting list is a position, not a probability or a guaranteed waiting time.',
    phrases='''Acknowledge disappointment | "I understand why this outcome is disappointing."
Confirm eligibility | "Your child met the published entry criteria."
Separate selection | "Eligibility did not guarantee a place in this intake."
Explain capacity | "There were 20 places for 24 eligible applicants."
Name the process | "The published procedure used a lottery."
State the current position | "Your child is fourth on the waiting list."
Limit a prediction | "No vacancy is confirmed at present."
Protect another family | "I cannot discuss another applicant's record."
Offer permitted information | "I can explain your child's record and the published process."
Define review scope | "The review examines a claimed factual error."
Avoid a false promise | "A review is not a second lottery."
Specify the window | "The local window is five school days from the notice."
Request evidence | "Please identify the disputed fact and supporting document."
Confirm receipt | "We will acknowledge your review request."
Distinguish later stages | "Enrollment begins only after the relevant offer steps."
Close clearly | "I will send the procedure and confirm the current waiting-list position."''',
    notes='''Eligible | Meets entry conditions; does not necessarily receive an offer.
Selected | Chosen through the applicable allocation process.
Waiting | Does not establish a date when a place will become available.
Review | Has a defined scope, not an unlimited reconsideration.
School days | May differ from calendar or business days.
Cannot disclose | Pair the boundary with information you can provide.''',
    d='''Which response best corrects a misunderstanding about eligibility? | "Your child was eligible; the capacity-limited lottery determined the offer." | "Eligibility means enrollment is guaranteed." | "The child must have failed the criteria." | "A waiting-list place is an offer." | This response separates the confirmed entry conditions from the subsequent allocation decision.
Which request can Leena address within the supplied scope? | Explain the child's own decision record. | Send all selected applicants' files. | Name the families likely to withdraw. | Guarantee a place next week. | The permitted scope includes this family's record but excludes other applicants' information.
Which statement about the review is accurate? | It examines a claimed factual error under the local procedure. | It automatically moves the applicant to first place. | It guarantees a fresh lottery. | It removes the capacity limit. | The stated procedure defines review by factual error and promises no new allocation.
What should Leena say about timing? | "No vacancy is confirmed, so I cannot give an offer date." | "Fourth means four days." | "All waiting-list applicants enter next week." | "The review deadline is also the enrollment date." | Waiting-list position alone supplies neither a confirmed vacancy nor a reliable offer date.''',
    dialogue='''Mr. Ortiz | The letter says my daughter meets the criteria, but she has no place. Did someone decide she was not suitable?
Leena | Her [[eligibility::Eligibility confirms that the child met the entry criteria, even though the later allocation did not produce an offer.]] is confirmed. The program had twenty places and twenty-four eligible applicants. Meeting the entry conditions allowed her into the allocation process, but did not guarantee selection.
Mr. Ortiz | Was this a comparison of ability, or was something missing from my daughter's file?
Leena | The published process used a [[lottery::The lottery, rather than a comparative judgment of merit, was the supplied allocation method among eligible applicants.]] among eligible applicants. I can explain your daughter's record and that process, but I cannot discuss other families' applications or personal information.
Mr. Ortiz | All right, so her application passed that stage. Where is she on the list, and should we keep looking for another place?
Leena | She is fourth on the [[waiting list::The waiting list records the applicant's current position for possible vacancies, not a confirmed future offer.]]. No vacancy is confirmed at present. I understand that makes planning difficult, but I do not want to give you an unsupported date.
Mr. Ortiz | Does fourth mean that four children would have to leave? I do not want to misunderstand the number and make plans the school cannot support.
Leena | It states her current position, not an offer timetable. Any [[vacancy::A vacancy is an actual available place; the supplied case confirms none at present.]] would be handled under the published procedure. I can send that procedure so you can see how the list operates.
Mr. Ortiz | I also noticed a review option. Can I ask for the lottery to be run again because we are disappointed with the result?
Leena | The local review examines a claimed [[factual error::A factual error concerns an incorrect fact or record, which is the stated scope of this review process.]]. It is not a second lottery. If you believe a fact in your daughter's decision record is wrong, identify it and provide supporting material.
Mr. Ortiz | I would like to check the record first. How long do I have to request that review, and where should I find the precise instructions?
Leena | The [[review window::The review window is the locally specified period for requesting review, here five school days from the notice.]] is five school days from the decision notice. I will send the instructions with the record information you are authorized to receive.
Mr. Ortiz | If I identify an incorrect fact, should I send a whole new application, or just explain the issue and attach the relevant evidence?
Leena | Identify the disputed fact and attach the relevant [[supporting document::The supporting document substantiates the particular claimed error rather than reopening every aspect of the application.]]. The review team needs a clear account of the issue. A new application is not what this procedure asks for.
Mr. Ortiz | If I send that document today, what will your reply actually confirm? I do not want to mistake a receipt for a changed decision.
Leena | An [[acknowledgment::An acknowledgment confirms receipt; it does not establish that the review has accepted the claim or changed the outcome.]] confirms receipt, not the outcome. The review team still needs to examine the identified fact. I cannot promise that the result will change.
Mr. Ortiz | Thank you. I had also assumed the placement discussion would happen now, but perhaps that is a different stage from this application review.
Leena | Yes. [[Placement::Placement assigns a learner to a class or setting and is distinct from eligibility and the offer decision.]] concerns the class or setting, rather than whether a place has been offered. We should keep those stages separate while the admissions position remains unchanged.
Mr. Ortiz | Please send the procedure, the permitted record information, and confirmation that she remains fourth. I will check for any factual error before deciding about review.
Leena | I will include the relevant [[decision notice::The decision notice anchors the outcome and review timing, helping the family connect the instructions to the correct case.]] details. Your daughter met the entry criteria; the lottery did not select her; and no vacancy is currently confirmed. Those are the facts we can rely on.''',
    transfer_title='A different list, the same distinction',
    transfer_setup='A fictional course has 12 places and 15 eligible applicants. An applicant not selected by lottery is second on its waiting list. No vacancy is confirmed. Its local review covers factual errors only.',
    transfer='''Officer: "The applicant met the ___." | entry criteria | The brief explicitly confirms eligibility, meaning the entry conditions were met.
Guardian: "The current waiting-list position is ___." | second | The supplied position is second, not a prediction of waiting time.
Officer: "The review concerns a claimed ___." | factual error | The fictional procedure limits review to a disputed fact or record.
Guardian: "A future offer is ___." | not confirmed | No vacancy is confirmed, so a future place cannot be promised.''',
    rehearsal=['Read the completed conversation in pairs; stress eligible, lottery, and fourth.', 'Repeat turns 9-16, distinguishing the review request from its acknowledgment.', 'Switch roles and read the four completed transfer lines, retaining the second waiting-list position.']))

BOOK['units'].append(unit(
    title='Curriculum Planning and Learning Outcomes',
    scene='A topic list is not a learning outcome',
    skill='Align a measurable learning outcome with classroom preparation, assessment evidence, and a shared scoring rule.',
    brief='Curriculum coordinator Pavel and teacher Nia review a draft course before teaching begins. Its topic list includes media literacy, but the proposed quiz asks only for definitions. The agreed intended outcome is to compare two supplied sources and justify which is more reliable using authorship and supporting evidence. The draft lessons currently practice only recalling terms. The team can revise the lessons and assessment before approval. They need source-comparison practice and a task scored on both named criteria, not a claim that remembering definitions demonstrates evaluation.',
    cast='Pavel | Curriculum coordinator\nNia | Teacher',
    culture=('Challenge alignment, not a colleague\'s competence', 'A familiar quiz may be well written but measure the wrong performance. State the intended learner action and show the mismatch. This makes revision a shared design problem, not a personal judgment about a teacher or an argument against all factual knowledge.'),
    a='''What must learners demonstrate in the intended outcome? | Compare two sources and justify reliability using authorship and evidence. | Recite every definition from the glossary. | Choose whichever source is longer. | Express an unsupported preference. | The agreed outcome explicitly requires comparison and justification using two named criteria.
What does the proposed quiz currently assess? | Recall of definitions | A supported comparison of two sources | Implementation of a revised curriculum | Agreement between graders | The supplied quiz asks for definitions rather than the intended comparative judgment.
When can the team make the proposed changes? | Before teaching begins and before draft approval | Only after final grades are published | After secretly changing completed scores | Without updating instruction | The brief places the course in a draft stage before instruction and approval.''',
    vocabulary='''curriculum | The planned learning content and experiences of a program. | review the curriculum
topic | A subject area covered in teaching. | list course topics
learning outcome | An observable performance learners should achieve. | specify a learning outcome
observable verb | An action word that identifies demonstrable performance. | choose an observable verb
alignment | A match among outcomes, teaching, and assessment. | check curriculum alignment
backward design | Planning from intended outcomes to evidence and instruction. | use backward design
assessment | A task or process used to gather evidence of learning. | design an assessment
formative assessment | Evidence used during learning to guide improvement. | use formative assessment
summative assessment | Evidence used to judge achievement at a designated point. | plan summative assessment
assessment criterion | A stated feature used to judge performance. | define assessment criteria
rubric | Descriptions of performance levels against criteria. | apply a shared rubric
descriptor | A statement describing performance at a particular level. | clarify a descriptor
authorship | Information about who produced a source. | evaluate authorship
supporting evidence | Material that supports a source's claims. | examine supporting evidence
source reliability | The extent to which a source merits trust for a purpose. | assess source reliability
justification | Reasons supporting a judgment or choice. | provide a justification
comparison | Examination of similarities and differences. | make a source comparison
recall | Retrieval of previously learned information. | assess factual recall
application | Use of knowledge in a task or context. | demonstrate application
evaluation | A judgment made against stated criteria. | demonstrate evaluation
practice task | An activity preparing learners for a target performance. | sequence practice tasks
exemplar | A sample illustrating expected or particular-quality work. | discuss an exemplar
scaffolding | Structured support that helps learners perform a task. | provide appropriate scaffolding
curriculum map | A view linking program elements, outcomes, and assessment. | update the curriculum map''',
    precision='A topic names what a course covers; an outcome states what learners will do. "Media literacy" is a topic. Comparing two sources and justifying reliability against specified criteria is an observable outcome.',
    precision_extra='Recall can support evaluation, but recalling definitions alone does not demonstrate a supported judgment. Revise both practice and assessment. In this case the course is still a draft, so the changes precede instruction and grading.',
    phrases='''Name the gap | "The topic is clear, but the learner performance is not."
State the intended action | "Learners must compare two supplied sources."
Specify the judgment | "They must justify which source is more reliable."
Name the criteria | "Use authorship and supporting evidence."
Identify the current measure | "The quiz currently measures recall."
Preserve useful knowledge | "Definitions support the task but do not complete it."
Connect instruction | "Lessons need practice in the same kind of comparison."
Choose suitable evidence | "A supported comparison would demonstrate the intended outcome."
Clarify scoring | "The rubric should address both named criteria."
Define a descriptor | "State what adequate use of evidence looks like."
Use an example | "Review an exemplar before independent practice."
Offer bounded support | "Provide the sources and a comparison framework."
Avoid a proxy | "Response length is not the stated criterion."
Locate the revision stage | "We can revise this before teaching begins."
Record the link | "Update the curriculum map with the aligned task."
Confirm the decision | "The outcome, practice, and assessment now require the same performance."''',
    notes='''Know | Often too broad unless a demonstrable performance is specified.
Compare | Requires examining sources in relation to each other.
Justify | Requires reasons, not just a selected answer.
Criteria | The dimensions of judgment, not the topic headings.
Aligned | Instruction and assessment support the intended outcome.
Draft | Changes can be approved before learners are taught and assessed.''',
    d='''Which assessment matches the intended outcome? | Compare the supplied sources using authorship and evidence, then justify the stronger source. | List five definitions from memory. | Copy a paragraph without evaluation. | Rank sources by length alone. | The correct task directly elicits comparison and justification against both required criteria.
Which instructional change is needed? | Add guided source comparisons before the final assessment. | Keep recall-only practice and assess comparison unexpectedly. | Remove all explanation of evidence. | Teach only the scoring total. | Learners need preparation in the performance that the intended assessment will require.
Which proposed scoring feature is unsupported? | Awarding marks only for response length | Assessing use of authorship information | Assessing use of supporting evidence | Assessing the justification for the judgment | Length alone is not one of the agreed criteria and does not establish sound evaluation.
Which statement preserves an appropriate role for definitions? | Definitions can support comparison but are insufficient evidence of the complete outcome. | Definitions and evaluation are identical performances. | Factual knowledge is always irrelevant. | Recalling terms proves both criteria were applied. | Factual knowledge can enable higher-level work without demonstrating that the work occurred.''',
    dialogue='''Pavel | The draft curriculum lists media literacy, and the quiz is ready. Before we approve it, can we state what learners must actually do with the material?
Nia | The intended [[learning outcome::The learning outcome specifies the observable source-comparison performance, rather than merely naming the media-literacy topic.]] is to compare two supplied sources and justify which is more reliable using authorship and supporting evidence. That is more specific than covering the topic.
Pavel | At the moment the quiz asks for definitions of reliability, evidence, and author. Those questions are clear, but do they show the performance we agreed?
Nia | They show [[recall::Recall demonstrates retrieval of definitions, which is useful but does not itself demonstrate comparative evaluation.]], not the complete comparison. A learner could reproduce every definition without applying either criterion to the sources. We need a different final task.
Pavel | I would keep the definitions as a starter quiz. Could we use them to check the vocabulary before students tackle the sources?
Nia | Certainly. The issue is [[alignment::Alignment requires the outcome, instructional practice, and assessment to support the same intended learner performance.]], not whether definitions matter. The outcome, classroom practice, and assessment should reinforce the same performance, with vocabulary serving that performance rather than replacing it.
Pavel | Our lessons practice definitions too. Changing only the final assessment would confront learners with a comparison task they had not practiced.
Nia | Add a guided [[practice task::A practice task prepares learners for the comparison and justification they will later need to demonstrate independently.]] with two sources. We can model how authorship and supporting evidence affect the judgment, then gradually reduce the support before the assessed task.
Pavel | For the final task, I suggest supplying both sources and asking for a choice with reasons under the two named headings. That keeps the evidence focused.
Nia | Yes. Each [[assessment criterion::An assessment criterion identifies a dimension of performance to judge, here authorship or supporting evidence.]] should be visible in the task and the scoring guidance. We should not reward a long response that never evaluates either source.
Pavel | Some teachers suggest one overall mark for sounding persuasive. That seems hard to explain consistently without mentioning the two required criteria.
Nia | A shared [[rubric::The rubric describes performance against the required criteria, providing a clearer basis for consistent scoring than an undefined impression.]] should describe how well the learner uses authorship information and supporting evidence. Persuasive wording alone cannot substitute for an accurate, supported comparison.
Pavel | The draft says sufficient evidence. One teacher expects a quotation; another expects an explanation. We need to settle that before anyone marks it.
Nia | Write a clear [[descriptor::A descriptor explains a performance level so teachers do not rely on different unstated interpretations of quality.]] for each level. It should distinguish naming a feature from explaining why that feature strengthens or weakens a source for this purpose.
Pavel | Could we use a sample response during teaching? Students might understand the distinction more quickly if they could see how a reason connects to a judgment.
Nia | An [[exemplar::An exemplar makes the expected performance visible and supports discussion of how criteria are applied.]] would help. We can identify the evidence supporting its conclusion, rather than asking students to copy its wording or assume there is only one acceptable sentence.
Pavel | This is still a draft, so we can revise before teaching starts. I will check that the lesson sequence, task instructions, and scoring guidance all match.
Nia | Update the [[curriculum map::The curriculum map records the links between outcomes, teaching experiences, and assessment so the revision remains traceable.]] as well. That will show where learners practice the comparison and where they demonstrate it, instead of leaving the revised quiz disconnected from the plan.
Pavel | Our approval summary will say that learners compare two supplied sources, apply both criteria, and justify the stronger source. Definitions remain supporting knowledge, not the final evidence.
Nia | That captures the required [[evaluation::Evaluation is the supported judgment against criteria; it is more than recalling terms or selecting a source without reasons.]]. We will approve the revised design only after the practice and scoring materials are ready, so students receive a coherent learning experience from the start.''',
    transfer_title='Match the task to the outcome',
    transfer_setup='A draft course outcome requires learners to classify four supplied expenses as fixed or variable and explain each classification. The current quiz only asks for the two definitions. Teaching has not begun.',
    transfer='''Coordinator: "The quiz currently tests ___." | recall | Asking for definitions measures retrieval rather than the required classification with reasons.
Teacher: "The revised task must include ___." | classification | The stated outcome requires sorting each supplied expense into a category.
Coordinator: "Each choice also needs an ___." | explanation | The outcome requires reasons for classifications, not only category labels.
Teacher: "We should revise practice and assessment before ___." | teaching begins | The course is still a draft, allowing alignment before students encounter instruction.''',
    rehearsal=['Read turns 1-8 with a pause after recall to make the assessment mismatch clear.', 'Read turns 9-16, stressing authorship, supporting evidence, and descriptor.', 'Switch roles for the transfer; pronounce classification and explanation as two separate requirements.']))


BOOK['units'].append(unit(
    title='Student Support and Intervention',
    scene='A plan on paper is not a delivered intervention',
    skill='Distinguish need, implementation, and outcome when reviewing a student-support plan.',
    brief='Student-support coordinator Mina and attendance lead Theo review a learner who arrived late on four of the last ten school days. An earlier plan proposed ten morning check-ins over two weeks. A recovered log documents only two check-ins; the other eight have no delivery record. The available evidence does not establish whether the full plan was delivered or whether it was ineffective. Mina will coordinate a new ten-day record, confirm the learner\'s and guardian\'s reported barriers, and review a local target of no more than one late arrival. No cause of lateness is established.',
    cast='Mina | Student-support coordinator\nTheo | Attendance lead',
    culture=('Use evidence to support, not label', 'Terms such as unmotivated or uncooperative can turn an incomplete record into a judgment about a learner. State what was observed and what remains unknown. Invite the learner and guardian to clarify barriers while keeping responsibilities and the review date explicit.'),
    a='''What does the attendance record show? | Four late arrivals in ten school days | Four full-day absences | Ten completed check-ins | A confirmed transport problem | The record identifies late arrivals, not absences, completed support, or their cause.
How much check-in delivery is documented? | Two of ten planned check-ins | All ten planned check-ins | None of the ten check-ins | Eight confirmed missed check-ins | Two are documented; missing records for eight do not prove either delivery or non-delivery.
What conclusion is premature? | The fully delivered intervention failed. | The implementation record is incomplete. | The learner had four late arrivals. | A new review needs a clear record. | The evidence does not establish full delivery, so it cannot support that specific failure claim.''',
    vocabulary='''student support | Coordinated assistance addressing a learner's needs. | coordinate student support
intervention | A planned action intended to improve an identified outcome. | implement an intervention
baseline | The starting measure used for comparison. | establish an attendance baseline
attendance record | Documentation of presence, absence, or arrival. | verify the attendance record
late arrival | Arrival after the applicable expected time. | record a late arrival
absence | Nonattendance during a defined period. | distinguish absence from lateness
check-in | A brief planned contact to review needs or progress. | conduct a morning check-in
implementation | Putting a planned action into practice. | document implementation
delivery log | A record of whether and when support occurred. | maintain a delivery log
implementation fidelity | The extent to which delivery matches the intended plan. | review implementation fidelity
frequency | How often an action occurs. | specify contact frequency
duration | How long an action or support period lasts. | state the intervention duration
progress monitoring | Repeated measurement to track change. | use progress monitoring
review point | A scheduled time to evaluate available evidence. | set a review point
barrier | A condition making participation or attendance harder. | explore a reported barrier
learner voice | The learner's own account and perspective. | include learner voice
guardian input | Information provided by a parent or authorized guardian. | seek guardian input
referral | A request to another service or specialist for support. | make an appropriate referral
case coordinator | The person organizing actions in a support case. | assign a case coordinator
support plan | Agreed actions, responsibilities, and review arrangements. | update the support plan
measurable target | A specified outcome that can be checked. | agree a measurable target
documented contact | A communication recorded with relevant details. | confirm documented contact
unverified report | An account not yet corroborated where verification is needed. | label an unverified report
outcome evidence | Information showing the result of an action or period. | review outcome evidence''',
    precision='Two documented check-ins do not establish that only two occurred. The other eight are unverified. This is a delivery-evidence gap, which must not be converted into either confirmed non-delivery or confirmed full implementation.',
    precision_extra='Four late arrivals in ten school days is a baseline count, not a diagnosis of motivation. The new target is local to this scenario. Meeting it would show improvement over this period, not prove the intervention caused the change.',
    phrases='''Start with observation | "The record shows four late arrivals in ten school days."
Keep categories separate | "Late arrivals are not the same as full-day absences."
Name the planned support | "The plan proposed ten morning check-ins."
State documented delivery | "The log records two completed check-ins."
Preserve uncertainty | "Delivery of the other eight is unverified."
Limit an effectiveness claim | "We cannot say the fully delivered plan failed."
Check implementation | "First establish what support actually occurred."
Invite the learner's account | "We need the learner's account of the morning barriers."
Include the guardian | "Confirm what the guardian reports without assuming the cause."
Assign coordination | "Mina will coordinate the new ten-day record."
Specify the target | "The local target is no more than one late arrival."
Set the review period | "Review the next ten school days."
Track both sides | "Record support delivery as well as attendance."
Use a fair comparison | "Compare periods of the same length."
Avoid a causal leap | "Improvement alone would not prove which factor caused it."
Close the plan | "The record must show the action, responsible person, and date."''',
    notes='''Planned | Intended, not necessarily delivered.
Documented | Supported by a record, not every event that may have occurred.
Unverified | Neither confirmed nor disproved.
Barrier | A condition to clarify, not a character judgment.
No more than one | Zero or one meets the numerical target.
Improved | Describes a change; does not by itself identify its cause.''',
    d='''Which sentence accurately summarizes implementation? | "Two check-ins are documented; eight have no delivery record." | "All ten check-ins definitely occurred." | "Exactly eight check-ins definitely did not occur." | "The learner refused eight check-ins." | The available log supports two contacts and leaves the remaining delivery unverified.
Which question is most useful before evaluating effectiveness? | Was the planned support delivered as intended? | Did the written plan include a target? | Can we compare this ten-day count with a twenty-day count without adjustment? | Would a lower target make the plan easier to close? | The missing delivery evidence must be resolved; a written target or an easier closure rule cannot establish implementation.
What should the new record track? | Both check-in delivery and late arrivals during the same ten-day period | Only the existence of a written plan | Only staff impressions of motivation | A target with no observations | Recording delivery and outcomes together makes the implementation and progress review more informative.
If the next period has one late arrival, what is supported? | The local numerical target was met for that ten-day period. | The intervention certainly caused the change. | All future lateness has been eliminated. | The earlier records were complete. | One late arrival meets the stated target but does not prove causation or permanent change.''',
    dialogue='''Theo | We have four late arrivals in ten school days. Someone suggested closing the morning check-in plan as an intervention that failed.
Mina | First separate the [[baseline::The baseline is the starting attendance measure, here four late arrivals in ten school days, not an explanation of their cause.]] from the delivery evidence. Four late arrivals describe the attendance period. They do not show whether the planned support occurred or why the learner arrived late.
Theo | The plan proposed ten contacts over two weeks. The recovered log records only two completed check-ins.
Mina | Then our [[delivery log::The delivery log documents two check-ins while leaving the other eight without evidence of delivery.]] is incomplete. We can confirm two documented contacts, but the other eight are unverified. Missing entries do not prove either that the contacts happened or that they did not.
Theo | I will remove failed intervention from the minutes. Can we check with the staff who covered the other mornings before the review?
Mina | Exactly. We need to establish [[implementation::Implementation concerns whether the planned support was actually put into practice before its effectiveness is assessed.]] before describing a fully delivered intervention as ineffective. Otherwise a gap in delivery or documentation could be mistaken for evidence that the support approach cannot work.
Theo | Colleagues suspect transport, but neither the learner nor the guardian has confirmed a cause.
Mina | Record it as a possible [[barrier::A barrier is a possible obstacle to attendance that needs clarification, not an established cause merely because staff suspect it.]], not a finding. Ask for the learner's account and the guardian's input. We should not replace their experience with a convenient explanation that nobody has verified.
Theo | For the next period, can we state the support frequency and who records each contact? The old document named a general team rather than a coordinator.
Mina | I will act as [[case coordinator::The case coordinator organizes the support actions and record, making responsibility clear rather than leaving it with an undefined group.]]. I will coordinate the new ten-day record and confirm the reported barriers. The record should identify each scheduled contact, its delivery status, and relevant follow-up.
Theo | We also need an outcome we can check. The proposed local target is no more than one late arrival during the next ten school days.
Mina | That is a [[measurable target::A measurable target states a checkable outcome, here zero or one late arrival during a defined ten-day period.]] with a defined period. Zero or one would meet it; two would not. We should keep that distinction clear without treating the count as a judgment of character.
Theo | I will keep late arrivals separate from full-day absences. Combining them would change the measure and mislead the comparison.
Mina | Use the same definitions for [[progress monitoring::Progress monitoring requires repeated, comparable observations so the team can assess change over the planned period.]]. Track the next ten school days, alongside support delivery. A count without the observation period would be difficult to compare fairly with the current record.
Theo | At the review, should we first check whether the planned contacts occurred and then look at attendance? That would keep delivery and outcome from being confused.
Mina | Yes. Review [[implementation fidelity::Implementation fidelity asks how closely actual delivery matched the agreed plan, separately from the learner's observed outcome.]] and the attendance measure separately, then discuss them together. We need to know what was delivered before deciding whether to continue, adjust, or seek additional support.
Theo | Suppose next fortnight we get one late arrival. I would report that against the target and ask what else changed in the mornings.
Mina | Correct. That would be useful [[outcome evidence::Outcome evidence records the observed result but does not alone establish which action caused it.]], not proof that check-ins alone caused the improvement. We can report progress honestly while remaining open to the learner's explanation of what helped.
Theo | I will correct the meeting note: two contacts documented, eight unverified, cause of lateness not established, new ten-day monitoring coordinated by you.
Mina | Add the [[review point::The review point sets when the team will examine the new delivery and attendance evidence rather than leaving the plan open-ended.]] at the end of that period. The next discussion should have a clear delivery record, comparable attendance information, and the learner's and guardian's accounts available.''',
    transfer_title='Separate delivery from results',
    transfer_setup='A support plan schedules six check-ins. Four are documented and two have no record. During the next ten school days, a learner has one late arrival. The local target was no more than one.',
    transfer='''Coordinator: "Documented check-ins total ___." | four | The delivery log confirms four contacts, not all six scheduled contacts.
Teacher: "Delivery of the other two is ___." | unverified | The missing records establish uncertainty, not definite delivery or non-delivery.
Coordinator: "The numerical attendance target was ___." | met | One late arrival is within the stated limit of no more than one.
Teacher: "The result alone does not prove ___." | causation | The observed change does not isolate support from other possible contributing factors.''',
    rehearsal=['Read the completed script; emphasize two documented and eight unverified without implying eight missed contacts.', 'Repeat turns 11-18, distinguishing the target, the observation period, and causation.', 'Switch roles for the transfer and read the answer explanations before repeating the corrected exchange.']))

BOOK['units'].append(unit(
    title='Parent and Guardian Communication',
    scene='Repair a message that sounded accusatory',
    skill='Acknowledge the effect of a message, correct unsupported wording, and arrange a clear, accessible meeting.',
    brief='Administrator Rosa sent an authorized guardian, Ms. Lin, an email saying the family had failed to prioritize punctuality. The verified attendance record shows three late arrivals in the last five school days, but no cause is established. Ms. Lin says the wording was accusatory and reports a bus delay. Rosa must correct the unsupported inference, retain the accurate attendance facts, and offer a meeting on Tuesday at 08:45. An interpreter can be requested; availability and the guardian\'s preferred language still need confirmation. The meeting is to understand barriers and agree support, not announce a predetermined penalty.',
    cast='Rosa | School administrator\nMs. Lin | Authorized guardian',
    culture=('Acknowledge impact before explaining intention', 'Explaining that an email was well intended can sound like refusing to hear a concern. Acknowledge the wording, correct the unsupported inference, and keep the verified facts. Then move to a concrete meeting invitation that the guardian can accept, adjust, or clarify.'),
    a='''Which part of the email is unsupported? | The claim that the family failed to prioritize punctuality | The count of three late arrivals | The five-school-day observation period | The proposed Tuesday meeting time | The attendance facts do not establish the family's priorities or motivation.
How should the bus issue be described now? | A delay reported by the guardian | A verified cause of all late arrivals | Proof that the school made no error | A reason to erase the attendance record | The guardian reports a delay, but the brief does not establish it as a verified cause.
What needs confirmation for language support? | The preferred language and interpreter availability | Another family's language preference | A penalty before the meeting | That translation is never necessary | The brief explicitly leaves both the language preference and interpreter availability unconfirmed.''',
    vocabulary='''guardian | A person with recognized responsibility for a learner. | contact the authorized guardian
family engagement | Two-way involvement of families in education. | strengthen family engagement
tone | The attitude conveyed by wording or delivery. | adjust the tone
accusatory wording | Language implying blame before it is established. | remove accusatory wording
acknowledge | Recognize a concern or fact explicitly. | acknowledge the concern
impact | The effect a message or action has. | acknowledge the impact
intention | The purpose someone meant to achieve. | distinguish intention from impact
inference | A conclusion drawn beyond directly recorded facts. | check an unsupported inference
verified fact | Information confirmed by the relevant evidence. | retain verified facts
reported concern | A concern attributed to the person raising it. | record a reported concern
attribution | Identifying the source of an account or claim. | preserve clear attribution
clarification | An explanation resolving uncertainty or misunderstanding. | offer a clarification
correction | A change that removes an error or unsupported claim. | issue a correction
meeting invitation | A request to attend a scheduled discussion. | send a meeting invitation
agenda | The planned topics or purpose of a meeting. | confirm the agenda
availability | Ability to attend or provide a service at a time. | confirm availability
preferred language | The language a person prefers for communication. | ask the preferred language
interpreter | A person supporting communication between spoken or signed languages. | request an interpreter
translation | Rendering written content into another language. | arrange written translation
communication preference | A preferred channel or way of receiving messages. | confirm communication preferences
two-way communication | An exchange allowing both parties to contribute. | support two-way communication
follow-up summary | A record sent after a discussion. | send a follow-up summary
agreed action | A next step accepted by the relevant participants. | record agreed actions
predetermined outcome | A result fixed before the discussion occurs. | avoid a predetermined outcome''',
    precision='An apology for accusatory wording does not require withdrawing accurate attendance information. Rosa can correct the inference about priorities while retaining the verified count and inviting the guardian to explain the circumstances.',
    precision_extra='Attribute the bus delay to the guardian until its status is clarified. Asking whether an interpreter is wanted is not the same as confirming one is booked. State the preferred language and availability as items to confirm.',
    phrases='''Acknowledge impact | "The wording sounded accusatory, and I understand your concern."
Take responsibility | "I should not have inferred your family's priorities."
Correct the claim | "The attendance record does not establish the reason."
Retain the facts | "It shows three late arrivals in five school days."
Attribute the account | "You have reported a bus delay."
Avoid a premature conclusion | "We have not yet confirmed how that affected each arrival."
Explain the purpose | "The meeting is to understand barriers and agree support."
Offer a specific time | "Would Tuesday at 08:45 work for you?"
Allow an adjustment | "Please let us know if another time is needed."
Ask about language | "Which language would you prefer for the discussion?"
Offer interpretation | "Would you like us to request an interpreter?"
Keep booking status accurate | "I still need to confirm interpreter availability."
Invite the guardian's account | "We would like to hear what happened from your perspective."
Avoid a fixed penalty | "No penalty is being announced in this invitation."
Record the agreement | "We will summarize the actions agreed at the meeting."
Close with confirmation | "I will send the corrected message and confirm the arrangements."''',
    notes='''I intended | Explains purpose but does not erase the effect of the wording.
You reported | Attributes an account without presenting it as independently verified.
The record shows | Introduces facts supported by the specified record.
Would Tuesday work? | An invitation, not confirmation of attendance.
Interpreter requested | Not the same as interpreter booked.
Agree support | Leaves room for genuine two-way discussion.''',
    d='''Which opening best repairs the email? | "I should not have inferred your family's priorities from the attendance record." | "You misunderstood, so the wording needs no change." | "The recorded late arrivals never happened." | "All transport delays are already verified." | The opening takes responsibility for the unsupported inference without denying accurate facts.
Which sentence preserves attribution? | "You have reported a bus delay; we need to understand its effect." | "The bus caused every late arrival, as independently confirmed." | "No guardian has reported a concern." | "The school has proved deliberate lateness." | It identifies the guardian as the source and does not overstate what has been verified.
Which meeting message is accurate? | "Tuesday at 08:45 is proposed; please confirm whether it works." | "Your attendance is already confirmed." | "The interpreter is booked in an unspecified language." | "The meeting will announce a penalty already decided." | The stated time is an offer requiring confirmation, not an established arrangement.
What should the follow-up summary contain? | Actions actually agreed and any arrangements still awaiting confirmation | Assumptions about the family's values | Other students' attendance details | An invented statement of agreement | A useful summary separates genuine agreements from unresolved arrangements and unsupported assumptions.''',
    dialogue='''Ms. Lin | Your email said we failed to prioritize punctuality. It sounded as though the school judged us without asking what happened.
Rosa | I understand why the [[tone::Tone concerns the attitude conveyed by the email, which here implied blame unsupported by the attendance record.]] concerned you. I should not have inferred your family's priorities. The attendance record shows late arrivals, but it does not establish your intentions or the reason.
Ms. Lin | There was a bus delay. I wanted someone to ask about it before deciding we did not care.
Rosa | Thank you for explaining. I will record that as your [[reported concern::A reported concern preserves the guardian's account while avoiding an unsupported claim that the cause has been independently established.]] and make sure it is discussed. We have not yet confirmed how that delay affected each arrival, so I will not present more as established.
Ms. Lin | Please correct that sentence. I am not disputing the three late marks; I am disputing what you said they meant.
Rosa | I am correcting the unsupported [[inference::The inference concerns the family's priorities, a conclusion that does not follow from the attendance count alone.]], not removing accurate attendance information. The verified record shows three late arrivals in the last five school days. Both parts should be stated clearly.
Ms. Lin | That is fair. What is the purpose of the meeting? The original email left me wondering whether a penalty had already been decided.
Rosa | The [[agenda::The agenda is to understand barriers and agree support, not to announce a predetermined penalty.]] is to understand the barriers and agree support. This invitation is not announcing a predetermined penalty. We need to hear your account and discuss practical arrangements together.
Ms. Lin | Tuesday might work. Please give me an exact time so I can arrange the journey and check my work schedule.
Rosa | Would Tuesday at eight forty-five suit your [[availability::Availability concerns whether the guardian can attend the proposed time, which has not yet been confirmed.]]? That is a proposed time, not a confirmed appointment. If it does not work, please tell me so we can discuss another arrangement.
Ms. Lin | I will check and reply. I may also need language support. I can discuss ordinary school matters, but I do not want to miss important details.
Rosa | Please tell me your [[preferred language::The preferred language must be established before an appropriate interpreter request can be arranged.]] and whether you would like an interpreter. I can request one, but I still need to confirm availability before saying the service is booked.
Ms. Lin | Could you also send the meeting purpose in writing? Having it in advance would help me check the facts and prepare the information I need.
Rosa | Yes. I will send a corrected [[meeting invitation::The meeting invitation records the proposed time, purpose, and unresolved arrangements so the guardian can respond accurately.]] stating the attendance facts, the purpose, and the proposed time. It will identify anything still awaiting confirmation, including the language-support arrangement.
Ms. Lin | Could we start with the journey to school? I can explain where the delay happens, and then we can look at what might help.
Rosa | We need [[two-way communication::Two-way communication gives the guardian a genuine opportunity to contribute rather than treating the meeting as a one-sided announcement.]]. Your account matters, alongside the school's records. We can clarify the circumstances and identify actions without assuming that either side already has the whole picture.
Ms. Lin | Afterward, please distinguish agreed actions from open questions. That should help avoid another misunderstanding.
Rosa | I will send a [[follow-up summary::A follow-up summary records actual agreements and unresolved points without inventing consent or completion.]] distinguishing those items. It should name the actions, responsible people, and any dates we actually agree, rather than presenting a suggestion as a settled commitment.
Ms. Lin | Thank you. I will confirm the proposed time and my language preference. I appreciate the correction without losing the discussion about the late arrivals.
Rosa | I will send the [[correction::The correction removes the unsupported claim about priorities while preserving the verified attendance facts and next steps.]] today and confirm the remaining arrangements when available. Our next step is a clear, respectful discussion of the facts and support, not a judgment about your family.''',
    transfer_title='Correct blame without erasing facts',
    transfer_setup='A message wrongly called a guardian uninterested. The verified record shows two missed appointments. The guardian reports a shift change. A new meeting and interpreter request are both awaiting confirmation.',
    transfer='''Administrator: "The claim about your interest was an unsupported ___." | inference | Missed appointments alone do not establish the guardian's interest or motivation.
Guardian: "The shift change is my ___." | reported explanation | The account is attributed to the guardian rather than described as independently verified.
Administrator: "The two missed appointments remain recorded ___." | facts | Correcting the unsupported judgment does not erase the verified appointment record.
Guardian: "The new arrangements are still ___." | awaiting confirmation | Neither the meeting nor interpreter request has yet been confirmed in the brief.''',
    rehearsal=['Read turns 1-6 in pairs, keeping the apology direct and the attendance facts neutral.', 'Repeat turns 9-14 with rising intonation on the proposed appointment and language-support questions.', 'Switch roles for the transfer, stressing the difference between reported explanation and recorded facts.']))


BOOK['units'].append(unit(
    title='Faculty Coordination and Evaluation',
    scene='The same paper, two different rubric readings',
    skill='Resolve scoring disagreements through shared criteria and evidence rather than averaging incompatible judgments.',
    brief='Department lead Erin and teacher Sam compare scores for the same anonymized student paper. The published rubric has three criteria, each scored from zero to four, for a maximum of twelve. Erin awarded ten and Sam seven. For the evidence criterion, the level-three descriptor requires two relevant examples with an explanation of how each supports the claim. The paper supplies both, but Sam reduced that criterion because the response was short. Length is not a criterion. They must calibrate the rubric, review affected work, and explain any corrected scores under the institution\'s process.',
    cast='Erin | Department lead\nSam | Teacher',
    culture=('Make disagreement about the evidence', 'A grading discrepancy can feel like a challenge to professional authority. Put the descriptor and anonymized work side by side. Explain the evidence for a score without treating seniority, generosity, or strictness as a substitute for the agreed standard.'),
    a='''What is the maximum rubric total? | Twelve | Ten | Seven | Four | Three criteria scored up to four each produce a maximum total of twelve.
What caused the identified disagreement? | Sam used response length although it is not a rubric criterion. | The paper lacked both examples. | The rubric had only one criterion. | The two teachers scored different papers. | The brief identifies an unsupported length penalty on the same student paper.
What does the evidence descriptor require? | Two relevant examples and explanation of how each supports the claim | A minimum page count | Three teacher signatures | Agreement with the teacher's preferred conclusion | The supplied level-three descriptor specifies relevant examples with their connection to the claim.''',
    vocabulary='''grading rubric | A scoring framework with criteria and performance descriptions. | apply the grading rubric
criterion | A dimension on which work is judged. | apply the stated criterion
performance level | A defined degree of achievement. | distinguish performance levels
score range | The permitted interval of marks. | confirm the score range
maximum score | The highest available mark. | calculate the maximum score
evidence criterion | A scoring dimension concerning support for a claim. | interpret the evidence criterion
relevant example | An example connected to the point being made. | identify relevant examples
claim | A statement or position supported by reasons. | support a claim
rationale | The reason for a judgment or decision. | explain the scoring rationale
calibration | Developing a shared application of a scoring standard. | run a calibration session
moderation | Reviewing assessment judgments for consistency and fairness. | conduct assessment moderation
anchor paper | A reference sample used to illustrate a scoring level. | use an anchor paper
anonymized work | Work presented without identifiers that reveal the learner. | review anonymized work
inter-rater agreement | The extent to which different scorers agree. | improve inter-rater agreement
scoring discrepancy | A difference between judgments of the same work. | investigate a scoring discrepancy
unsupported penalty | A deduction not justified by the applicable criteria. | remove an unsupported penalty
reassessment | A fresh evaluation of work under the relevant process. | arrange reassessment
affected cohort | The group whose work may be influenced by an issue. | identify the affected cohort
feedback comment | An explanation given to a learner about work. | revise a feedback comment
consistency check | A review of whether a standard is applied uniformly. | perform a consistency check
score adjustment | A change to a recorded mark. | document a score adjustment
audit trail | A record showing changes and their reasons. | preserve an audit trail
professional judgment | Informed evaluation using relevant expertise and standards. | exercise professional judgment
standardization | Establishing shared procedures or interpretations. | support grading standardization''',
    precision='A total of ten versus seven signals disagreement but does not reveal which criterion is wrong. Examine the criterion-level judgments. Averaging the totals to 8.5 would conceal the identified unsupported length penalty rather than resolve it.',
    precision_extra='Calibration seeks shared application of the published rubric, not artificially identical results regardless of evidence. The supplied evidence supports level three on the evidence criterion; the brief does not establish a final corrected total for all criteria.',
    phrases='''Locate the discrepancy | "We scored the same paper differently."
Check the scale | "There are three criteria, each worth up to four."
Read the descriptor | "Level three requires two relevant examples with explanation."
Point to the evidence | "Both examples are connected to the claim."
Identify an extra rule | "Length is not part of this rubric."
Separate impression from standard | "A short answer can still meet the descriptor."
Avoid an easy average | "Averaging totals would not resolve the interpretation."
Use a shared sample | "Let us calibrate against this anonymized paper."
State the rationale | "The score needs a criterion-based explanation."
Limit the conclusion | "We have resolved this criterion, not the entire total."
Review the wider effect | "Check other work affected by the same interpretation."
Keep standards stable | "Apply the published criteria rather than adding a new rule."
Record the change | "Document any adjustment and its reason."
Align feedback | "The comment should explain the criterion actually used."
Explain to learners | "We are reviewing inconsistent application of the rubric."
Close the review | "Confirm corrected scores through the institution's process."''',
    notes='''Strict | Describes a tendency, not a scoring justification.
Consistent | Uses the same standard, not necessarily the same mark.
Three out of four | A criterion score, not the whole-paper total.
Average | Can hide a disagreement instead of resolving it.
Affected | Requires review; does not mean every score must change.
Corrected total | Needs review of all relevant criterion scores.''',
    d='''Which evidence supports level three on the evidence criterion? | Two relevant examples, each explained in relation to the claim | A short answer by itself | A teacher's seniority | The average of the two totals | The paper meets the two explicit elements in the supplied level-three descriptor.
Why is simply averaging ten and seven inadequate? | It leaves the unsupported length penalty and interpretation unresolved. | Averages can never be calculated. | The maximum score is only seven. | All teachers must always give identical scores. | Averaging produces a number without correcting the identified misuse of the scoring standard.
What final total can be inferred now? | No corrected total is established for all three criteria. | Exactly 8.5 is necessarily correct. | Twelve must replace both scores. | Seven must remain because it is lower. | The brief resolves evidence for one criterion but supplies no complete corrected criterion-level total.
Which wider action is appropriate? | Review other work affected by the same length interpretation. | Add a hidden minimum length after grading. | Raise every score without review. | Remove all feedback to prevent questions. | The same unsupported interpretation may affect other work and should be checked under the established process.''',
    dialogue='''Sam | We have ten and seven for the same paper. I was stricter because it was short, but I cannot find a length requirement in the rubric.
Erin | Start with the [[criterion::A criterion identifies the dimension being judged, so the discussion must locate the disagreement rather than compare totals alone.]], not our overall impressions. There are three, each scored from zero to four. Which one did you reduce because of the response length?
Sam | The evidence criterion. The paper has two examples, but I expected more writing before awarding three. Perhaps I added an expectation that was not stated.
Erin | Read the [[descriptor::The descriptor specifies the requirements for a performance level, here two relevant examples and an explanation connecting each to the claim.]]. Level three requires two relevant examples and an explanation of how each supports the claim. It does not specify a page count or minimum response length.
Sam | Looking at the paper, both examples are relevant, and each has a sentence explaining its connection. The response is concise, but those elements are present.
Erin | Then the [[rationale::The rationale must connect the judgment to the supplied descriptor and work, not to an unstated preference for longer answers.]] supports level three on this criterion. Concision does not remove the evidence. We should avoid rewarding additional words merely because they create an impression of greater effort.
Sam | Eight and a half would split the difference. But I would still be marking short answers down tomorrow, so that would not fix this.
Erin | It would preserve the [[scoring discrepancy::The scoring discrepancy arises from incompatible interpretations, which an average would conceal rather than resolve.]] beneath a compromise number. We need a shared interpretation of the published standard, not a numerical agreement that leaves the unsupported length rule in place.
Sam | Let us use this paper in the team meeting without identifying the learner. Teachers can compare the descriptor with the same two examples and explanations.
Erin | That provides an [[anchor paper::An anchor paper is a shared reference sample that helps teachers apply a scoring level consistently.]] for calibration. The aim is consistent use of evidence, not persuading everyone to copy a senior colleague's mark without understanding the reasoning.
Sam | We have settled the evidence criterion. Should I now replace seven with ten, or do we need to check the other two criteria first?
Erin | Review them before any [[score adjustment::A score adjustment must follow a complete relevant review; resolving one criterion does not establish the final total.]]. The brief evidence supports this criterion at three, but it does not establish the correct total across all three. Do not invent the remaining scores.
Sam | I may have applied the same length expectation elsewhere. We should identify affected work rather than assume this is isolated.
Erin | Review the [[affected cohort::The affected cohort consists of work potentially influenced by the same interpretation and needing review, not automatic score increases.]] under the institution's process. Some judgments may remain unchanged after review; others may need correction. We should not apply a blanket increase without examining the work.
Sam | I wrote too short in the margin. I should replace that comment as well; otherwise the student will think we want extra words.
Erin | Each [[feedback comment::A feedback comment should explain performance against the actual criterion so learners are not directed toward an unstated requirement.]] should describe the criterion used and the evidence in the paper. If a score changes, the explanation should make that change understandable to the learner.
Sam | We will need a record of the original score, the reviewed score, and the reason. Otherwise later questions could make the correction difficult to explain.
Erin | Preserve an [[audit trail::An audit trail records what changed and why, supporting transparent review rather than silently replacing marks.]] and follow the authorized correction process. That protects transparency without exposing another student's work or implying that every original judgment was invalid.
Sam | Our message can say that we are reviewing inconsistent use of the rubric. It should not say that a new scoring rule has been introduced.
Erin | Correct. This is [[calibration::Calibration develops a shared application of the existing standard rather than adding an undisclosed new grading rule.]] of the published standard. We will document the interpretation, review affected work, and communicate any verified corrections through the agreed process.''',
    transfer_title='A criterion is not a total',
    transfer_setup='A rubric has two criteria worth five points each. Review confirms four points for the first criterion. The second has not been reviewed. An unstated length penalty may also have affected six other papers.',
    transfer='''Lead: "The maximum total is ___." | ten | Two criteria worth five points each allow a total of ten.
Teacher: "The confirmed first-criterion score is ___." | four | The supplied review establishes four points only for the first criterion.
Lead: "The final corrected total remains ___." | unresolved | The second criterion is not yet reviewed, so the total cannot be inferred.
Teacher: "The six potentially affected papers need ___." | review | Possible use of the same unsupported penalty requires examination, not automatic identical changes.''',
    rehearsal=['Read turns 1-8; pronounce criterion and criteria accurately and stress the two required examples.', 'Repeat turns 11-16, keeping the confirmed criterion score separate from the unconfirmed total.', 'Switch roles for the transfer and read ten and four distinctly.']))

BOOK['units'].append(unit(
    title='Compliance, Records, and Privacy',
    scene='A route-planning task does not need an entire file',
    skill='Clarify purpose, authorized access, and minimum task-relevant records without treating job title as blanket permission.',
    brief='Transport coordinator Dana asks records officer Yusuf for complete student files to update pickup assignments. The task requires student IDs and assigned pickup stops only; counseling notes, disciplinary history, and health information are not needed for this task. The fictional institution requires the records owner to approve the fields, recipients, and access period before release. That approval is pending. Yusuf can prepare a two-field roster for review but cannot release it yet. An old shared folder still grants broad access and must be referred for access review, not assumed safe because it is internal.',
    cast='Dana | Transport coordinator\nYusuf | Records officer',
    culture=('Explain the useful alternative', 'A privacy boundary is easier to understand when paired with a route to completing the work. State the task-relevant fields and the approval still required. Avoid implying that a colleague is untrustworthy merely because the request was broader than necessary.'),
    a='''Which fields are needed for the stated task? | Student IDs and assigned pickup stops | Complete counseling and disciplinary records | Every health note | All records because the recipient is a colleague | The brief limits route-assignment needs to two specified fields.
What is the current release status? | Approval is pending, so no roster may be released yet. | The narrow roster is automatically approved. | The old folder replaces approval. | A job title grants unrestricted access. | The fictional local rule requires approval before release, and that approval is pending.
What should happen to the old broad-access folder? | Refer its access for review. | Assume it is safe because it is internal. | Add more sensitive files immediately. | Delete all institutional records without authorization. | Broad existing access needs review rather than being treated as proof of appropriate authorization.''',
    vocabulary='''education record | Recorded information about a learner maintained in an educational context. | handle education records
record custodian | The role responsible for maintaining specified records. | contact the record custodian
records owner | The accountable authority for a dataset or record collection. | obtain records-owner approval
authorized recipient | A person approved to receive specified information. | verify authorized recipients
legitimate educational interest | A U.S. FERPA access concept tied to relevant professional responsibilities. | assess legitimate educational interest
FERPA | The U.S. Family Educational Rights and Privacy Act. | consult applicable FERPA guidance
purpose limitation | Restricting information use to an authorized purpose. | state the access purpose
data minimization | Limiting data to what is necessary for the purpose. | apply data minimization
field | A defined item of information in a record. | approve the requested fields
roster | A list of people or identifiers with relevant details. | prepare a limited roster
student identifier | A value used to distinguish a student record. | verify the student identifier
pickup assignment | The stop or arrangement assigned for a learner's transport. | update pickup assignments
sensitive information | Information requiring particular care because of potential harm or rules. | restrict sensitive information
counseling note | A record of a counseling interaction or observation. | protect counseling notes
disciplinary record | Documentation of disciplinary matters. | restrict disciplinary records
access scope | The information and actions an authorization permits. | define the access scope
role-based access | Access assigned according to approved responsibilities. | review role-based access
least privilege | Granting only the access needed for the authorized task. | apply least privilege
access period | The time during which access is authorized. | specify the access period
secure channel | An approved means of transmitting protected information. | use a secure channel
redisclosure | Further sharing by a recipient. | control redisclosure
retention schedule | Rules governing how long records are kept. | follow the retention schedule
access review | A check of whether permissions remain appropriate. | request an access review
release authorization | Approval to disclose specified information. | confirm release authorization''',
    precision='Reducing a file to two fields addresses relevance but does not itself authorize release. In this case the records owner must approve fields, recipients, and access period. The approval remains pending even for the limited roster.',
    precision_extra='FERPA is a U.S. law with a defined scope and exceptions, not a global label for all school privacy rules. Follow the applicable law and institutional procedure. Internal access and existing permissions do not by themselves establish that every use is appropriate.',
    phrases='''Clarify the job | "Which information is needed to update pickup assignments?"
Narrow the fields | "The task needs student IDs and assigned pickup stops."
Explain the exclusion | "Counseling and disciplinary records are not needed for this task."
Separate relevance from permission | "A smaller roster still requires release approval."
Name the approval owner | "The records owner must approve the scope."
Identify recipients | "Please confirm who will receive the roster."
Set the time boundary | "The access period also needs approval."
State the current status | "Approval is pending, so I cannot release it yet."
Offer a practical step | "I can prepare the two-field roster for review."
Avoid title-based assumptions | "A job title is not blanket permission for the whole file."
Question inherited access | "Existing folder access needs review."
Keep the channel explicit | "Use the approved secure channel after authorization."
Limit further sharing | "Do not redistribute beyond the approved recipients."
Separate retention | "Access expiry does not replace the retention schedule."
Escalate appropriately | "I will refer the broad folder permissions for access review."
Confirm before release | "We need the approved fields, recipients, and period recorded."''',
    notes='''Internal | Describes location or audience, not automatic authorization.
Needed | Establishes task relevance, not permission on its own.
Prepared | Does not mean released.
Pending | The required decision has not yet been made.
Identifier | Can still be personal information; it is not automatically anonymous.
Expires | Refers to access here, not automatic record destruction.''',
    d='''Which response best supports the transport task? | Prepare the ID-and-stop roster for owner review without releasing it. | Send complete files immediately. | Refuse to identify any permitted path forward. | Upload counseling notes to the old folder. | The limited roster addresses the task while respecting the pending release authorization.
Why is the old folder not sufficient authority? | Existing access may be broader than the approved task requires. | Every internal folder is always illegal. | Student IDs are never information. | A folder name establishes consent. | Current permissions must be reviewed against purpose and authorization rather than assumed appropriate.
What must be approved under this fictional procedure? | Fields, recipients, and access period | Fields and access period, with the entire department assumed to be recipients | Recipients and purpose, with the complete file assumed necessary | A secure channel, with the existing folder permissions treated as release approval | The brief requires approval of all three named elements; a secure channel or a partially defined scope does not replace it.
Which statement about access expiry is accurate? | It does not by itself determine record retention or deletion. | It orders immediate destruction of every source record. | It makes further sharing unrestricted. | It removes the need for authorization. | The period of permitted access and the record-retention schedule address different decisions.''',
    dialogue='''Dana | I need complete student files for the pickup-assignment update. The old shared folder would be convenient, and I already have access to it.
Yusuf | Let us define the [[access scope::Access scope identifies the information and actions actually needed, instead of treating an existing folder as permission for every record.]] for this task. Updating pickup assignments needs student IDs and assigned pickup stops. It does not require counseling notes, disciplinary history, or health information.
Dana | I did not know which fields you could separate. A two-field list would let me complete the assignment check.
Yusuf | I can prepare that [[roster::The roster is the limited list of student IDs and pickup stops that supports the stated task.]] for review. Reducing the information is helpful, but it does not mean I can release it immediately. The required approval is still pending.
Dana | Who decides? I assumed my transport role allowed me to receive anything about students on the routes.
Yusuf | The [[records owner::The records owner is the designated authority for approving the fields, recipients, and access period under the fictional procedure.]] must approve the fields, recipients, and access period. Your role explains the task, but it does not create unrestricted permission to receive every part of a student file.
Dana | I will name the two route planners in the request. If another colleague covers a shift, we will check their access rather than forward the list.
Yusuf | Correct. Each [[authorized recipient::An authorized recipient is approved for the specified information and purpose, rather than included through an indefinite team-wide request.]] must be within the approved scope. We should not expand the audience for hypothetical future work that has not been assessed or authorized.
Dana | The task is a pickup update, not a welfare or discipline review. I will state that purpose in the request.
Yusuf | That supports [[purpose limitation::Purpose limitation keeps use tied to the authorized pickup task instead of allowing unrelated uses of the same information.]]. It also explains why the unrelated notes should be excluded. A narrower request helps us complete the legitimate work without exposing information the task does not need.
Dana | The roster would only show IDs and stops. Does removing the names change whether we need that approval?
Yusuf | No. A [[student identifier::A student identifier can link the roster to a particular learner and is not automatically anonymous merely because it is not a name.]] can still link the information to a learner. Replacing a name with an ID does not automatically remove privacy obligations or the local approval requirement.
Dana | I will include the proposed access period. Once that ends, should the source records be deleted, or does the period refer only to our access?
Yusuf | It concerns access. The [[retention schedule::The retention schedule governs how long records are kept, a different question from how long a recipient may access them.]] determines how records are kept under the applicable rules. Do not turn an access end date into an unauthorized instruction to destroy source records.
Dana | The old folder still contains more information than this task needs. Should I assume someone approved that earlier and continue using it until the new list arrives?
Yusuf | Refer it for an [[access review::An access review checks whether existing permissions remain appropriate; their existence alone is not proof of authorization for this use.]]. Existing permissions may be too broad or outdated. We need that issue examined rather than using it to bypass the pending approval for this request.
Dana | After approval, I can use the approved channel and avoid sending the roster to colleagues who are not included. Is that the right boundary?
Yusuf | Yes, including restrictions on [[redisclosure::Redisclosure is further sharing by a recipient and must remain within the applicable approved conditions.]]. Authorization to receive the list does not automatically authorize further distribution. Keep the approved audience and purpose attached to the information when you use it.
Dana | I will submit the two fields, named recipients, and proposed period. Please prepare the roster for review, but hold release until the decision is recorded.
Yusuf | That is the correct [[release authorization::Release authorization is the required approval still needed before the prepared roster can be disclosed.]] sequence. I will also refer the broad folder permissions for review. We can support the route update without treating convenience as permission for a complete student file.''',
    transfer_title='Preparation is not permission',
    transfer_setup='An examinations team needs student IDs and assigned rooms. Medical notes are not needed. Local policy requires the records owner to approve fields and recipients before release; approval is still pending.',
    transfer='''Officer: "The relevant fields are IDs and ___." | assigned rooms | The stated examination task needs the room assignment, not unrelated records.
Coordinator: "The medical notes should be ___." | excluded | Medical notes are not needed for the narrowly defined task in this scenario.
Officer: "The required approval remains ___." | pending | The brief states that the records owner has not yet approved release.
Coordinator: "A prepared list must not yet be ___." | released | Preparation does not replace the required authorization before disclosure.''',
    rehearsal=['Read turns 1-8, making the two permitted fields and named recipients easy to hear.', 'Repeat turns 11-16, distinguishing removal of names, access expiry, and record retention.', 'Switch roles for the transfer; stress prepared and released as different stages.']))


BOOK['units'].append(unit(
    title='Accreditation and Program Review',
    scene='Three completed actions are not a closed review',
    skill='Report action status, ownership, and evidence without confusing completion with effectiveness or accreditation approval.',
    brief='Quality coordinator Amara and program director Hugh prepare a fictional internal review due on October 15. Its action plan has five actions. Actions 1, 2, and 3 have approved completion evidence. Action 4 is underway, with an assigned owner and an October 10 deadline. Action 5 has no assigned owner and no completion evidence. No outcome evaluation has yet established whether the completed actions improved learning. The team must report three of five actions complete, seek an owner and deadline for Action 5, and avoid presenting the internal review as an accreditation decision.',
    cast='Amara | Quality coordinator\nHugh | Program director',
    culture=('A candid status report supports credible review', 'A review team needs a traceable account, not uniformly positive labels. Name what is complete, what is underway, and what has no owner. Acknowledging a remaining gap is more useful than describing an approved plan as if every action and outcome were already verified.'),
    a='''What share of actions is complete? | Three of five, or 60% | Four of five, or 80% | Five of five, or 100% | One of five, or 20% | Three actions have approved completion evidence out of five total actions.
Which action lacks an owner? | Action 5 | Action 4 | Action 3 | All five actions | The brief identifies Action 5 as unassigned while Action 4 has an owner.
What remains unestablished about the completed actions? | Whether they improved learning outcomes | Whether completion evidence exists for Actions 1-3 | Whether the plan contains five actions | Whether the internal review has a due date | Completion is documented, but the brief states that outcome effectiveness has not been established.''',
    vocabulary='''program review | A structured examination of a program's quality and performance. | conduct a program review
accreditation | External recognition under a specified quality-assurance process. | distinguish accreditation from internal review
self-study | An institution's documented examination of its own performance. | prepare a self-study
review panel | A group examining a program against relevant expectations. | brief the review panel
criterion for review | A standard used to evaluate a program. | address a review criterion
supporting evidence | Material used to substantiate a review claim. | organize supporting evidence
evidence register | An index connecting evidence to claims or requirements. | maintain an evidence register
action plan | A set of improvement actions with responsibilities and timing. | update the action plan
action owner | The person accountable for advancing an assigned action. | assign an action owner
due date | The date by which an item is expected. | confirm the due date
completion evidence | Information showing that an action was carried out. | approve completion evidence
status report | A summary of current progress and unresolved items. | issue a status report
underway | Started but not complete. | report an action as underway
unassigned | Without a designated responsible person. | flag an unassigned action
closure criterion | A condition required before an item is closed. | verify closure criteria
effectiveness | The extent to which an action achieves its intended result. | evaluate effectiveness
outcome measure | An indicator of the result being sought. | select an outcome measure
implementation evidence | Information showing that a practice was put into use. | examine implementation evidence
continuous improvement | Repeated use of evidence to improve practice. | support continuous improvement
follow-up review | A later check of progress or results. | schedule a follow-up review
evidence gap | Missing support for a claim or required conclusion. | identify an evidence gap
accountability | Clear responsibility for actions and explanations. | strengthen accountability
review finding | A conclusion reached through examination of evidence. | distinguish a finding from a proposal
decision authority | The body or role permitted to make a decision. | identify the decision authority''',
    precision='Three completed actions out of five is 60%. Action 4 is underway, not complete, and Action 5 is unassigned. Counting an underway item as completed would inflate the rate to 80% without the required evidence.',
    precision_extra='Completion evidence shows that an action occurred. Effectiveness evidence concerns whether the intended result followed. An internal action-plan update is neither proof of improved learning nor an external accreditation decision.',
    phrases='''State the verified count | "Three of five actions have approved completion evidence."
Translate the proportion | "That is 60% complete."
Separate underway work | "Action 4 is in progress, not closed."
Name the existing deadline | "Its assigned owner is working toward October 10."
Expose the ownership gap | "Action 5 remains unassigned."
Request a decision | "We need an owner and deadline for Action 5."
Keep evidence traceable | "Link each claim to its supporting record."
Avoid status inflation | "Do not count underway work as complete."
Separate action from result | "Completion does not yet establish improved learning."
Name the remaining evaluation | "The outcome review still needs to be carried out."
Protect the review date | "The internal submission is due October 15."
Record unresolved items | "The report should show the gap and proposed next step."
Limit the approval claim | "This update is not an accreditation decision."
Identify authority | "Only the relevant decision body can grant that status."
Use a precise close | "The plan is partly complete, with two actions still open."
Plan follow-up | "Set a follow-up review for unresolved actions and outcomes."''',
    notes='''Complete | Requires the specified completion evidence in this case.
Underway | Started; not a synonym for closed.
Unassigned | No accountable owner has yet been designated.
Evidence | Must support the particular claim being made.
Effective | Concerns results, not merely the existence of a process.
Accredited | A status determined through the applicable external process.''',
    d='''Which headline accurately reports progress? | "Three actions complete; one underway; one unassigned." | "The entire improvement plan is complete." | "Four actions complete because one has started." | "No actions have any evidence." | The correct statement preserves all three status categories supplied in the brief.
What should the director decide about Action 5? | Assign an owner and deadline, without falsely marking it complete. | Declare completion because the review is approaching. | Delete it silently from the denominator. | Transfer accreditation authority to the action owner. | The missing ownership and timing need a decision, while completion remains unsupported.
Which evidence would address effectiveness rather than mere completion? | A suitable evaluation of whether the actions improved the intended outcomes | A copy of the action-plan title page | A statement that the deadline is approaching | An email saying the plan looks professional | Effectiveness concerns the intended result, which requires appropriate outcome evidence rather than presentation or scheduling.
What does the October 15 date represent? | The internal review submission deadline | A guaranteed accreditation award | Proof that every action is effective | The recorded completion date for Action 5 | The brief assigns October 15 to internal submission, not external recognition or outcome proof.''',
    dialogue='''Hugh | The review is due on October fifteenth. I would like a concise progress statement, but the current slide says nearly complete without explaining the remaining work.
Amara | Use the [[status report::The status report should distinguish completed, underway, and unassigned work rather than hide the differences behind a vague label.]] categories. Three actions have approved completion evidence, Action Four is underway, and Action Five is unassigned. That is a clearer account than nearly complete.
Hugh | Someone counted Action Four as complete because work has started. That makes the slide show eighty percent.
Amara | The correct [[completion evidence::Completion evidence is required before an action is counted as finished; having an owner and starting work are insufficient.]] exists for three actions only. Three out of five is sixty percent. Counting the fourth would overstate progress before the action meets its closure requirements.
Hugh | Action Four has an October tenth deadline and an assigned owner. We can report that schedule without saying the work is already finished.
Amara | Yes, describe it as [[underway::Underway means started but not complete, preserving the distinction between progress and verified closure.]]. Keep its owner and deadline visible. A planned date gives readers useful context, but it does not become a completion date simply because it is approaching.
Hugh | The fifth action has no owner at all. I do not want that lost in the notes, because nobody is currently accountable for moving it forward.
Amara | We need an [[action owner::The action owner supplies accountability for progressing the task; assigning one does not itself complete the action.]] and an agreed deadline. The report should request that decision explicitly. Once assigned, the action remains open until the required work and evidence are completed.
Hugh | For the three closed actions, where should we point reviewers? The narrative says they are complete, but the supporting documents are in several different places.
Amara | Link them through the [[evidence register::The evidence register connects each completion claim with its supporting record so reviewers can verify the stated status.]]. Each claim should lead to the relevant approved record. A persuasive summary still needs a traceable basis, not just a confident description.
Hugh | One colleague wants to say these completed actions have improved student learning. The work is real, but I have not seen an outcome evaluation yet.
Amara | Then [[effectiveness::Effectiveness concerns whether intended results were achieved, which has not been established by the supplied completion evidence.]] is not established. We can say the actions were completed, while stating that outcome evaluation remains outstanding. Doing the work and showing its effect are different claims.
Hugh | We can count the revised documents now. Would that belong in the completion column rather than the learning-results column?
Amara | That count describes an output, not the intended [[outcome measure::The outcome measure should address the result sought, rather than substitute a convenient count of revised documents.]]. We need suitable evidence about the learning result. A convenient administrative count should not quietly replace the purpose of the improvement.
Hugh | The internal submission will therefore show sixty percent complete, the October tenth action still underway, and the unassigned action needing a decision.
Amara | Include the remaining [[evidence gap::The evidence gap concerns missing support for outcome effectiveness as well as the unfinished action, and should remain visible.]] about outcomes too. Reviewers need to distinguish an incomplete action from an action completed without an evaluated result. Those require different follow-up work.
Hugh | There is another problem on the cover: accreditation achieved. Can we change that to internal action-plan update before this goes out?
Amara | Remove that claim. The relevant [[decision authority::The decision authority for accreditation is distinct from the team preparing an internal progress report.]] determines accreditation status through its process. Our action-plan update cannot confer an external status or predict the outcome of a future review.
Hugh | I will request an owner and date for Action Five today, keep the existing deadline for Action Four, and make the evidence links explicit.
Amara | Then schedule a [[follow-up review::The follow-up review checks unresolved actions and outcome evidence rather than treating submission of the current report as completion of all work.]]. The October fifteenth submission should honestly show what is verified, what remains open, and which decisions are needed next, without overstating completion or results.''',
    transfer_title='Count only verified completion',
    transfer_setup='A fictional plan has eight actions: five have approved completion evidence, two are underway, and one is unassigned. The internal report is due Friday. No external accreditation decision has been issued.',
    transfer='''Coordinator: "The completed-action count is ___." | five | Only the five actions with approved completion evidence are counted as complete.
Director: "The completion rate is ___ percent." | 62.5 | Five divided by eight equals sixty-two point five percent.
Coordinator: "The action without an owner is ___." | unassigned | Unassigned describes the missing accountability, not completed or underway work.
Director: "External accreditation is ___." | not confirmed | The brief states that no external accreditation decision has been issued.''',
    rehearsal=['Read turns 1-8, stressing sixty percent and the distinction between underway and complete.', 'Repeat turns 11-18, separating outputs, outcomes, and accreditation status.', 'Switch roles for the transfer; read 62.5 percent aloud and check its explanation.']))

BOOK['units'].append(unit(
    title='Budget, Staffing, and Institutional Priorities',
    scene='One more class still leaves four learners waiting',
    skill='Compare staffing options using capacity, full cost, displaced work, and authorization status.',
    brief='Operations manager Kiran and principal Elise consider one extra class for a waiting list of 24 learners. The class cap is 20, so one class would leave four learners waiting. Option A reallocates an existing qualified teacher for four weekly teaching hours, removing four weekly tutoring hours; it has no additional direct staffing charge. Option B uses confirmed available, qualified temporary support at an all-inclusive cost of $4,800 against an uncommitted $5,000 budget, preserving tutoring. Both options meet room and timetable requirements. Funding approval is pending. The stated priority is preserving tutoring while adding capacity.',
    cast='Kiran | Operations manager\nElise | Principal',
    culture=('Show what an option displaces', 'A proposal with no additional charge can still reduce another service. Name that effect without dismissing budget constraints. A recommendation is more useful when it states the priority served, the remaining capacity gap, and the approval still required.'),
    a='''How many learners would remain waiting after one extra class? | Four | Zero | Twenty | Twenty-four | The waiting list has twenty-four learners, while the extra class has only twenty places.
What does Option A displace? | Four weekly tutoring hours | All classroom teaching | The entire waiting list | A confirmed temporary contract | The existing teacher's four teaching hours replace four weekly tutoring hours.
Which option matches the stated priority within the supplied budget? | Option B, subject to funding approval | Option A with no tutoring impact | Neither, because $4,800 exceeds $5,000 | Both automatically approved | Option B preserves tutoring and fits the budget, but approval remains pending.''',
    vocabulary='''staffing allocation | Assignment of personnel time to work. | review staffing allocations
reallocation | Moving an existing resource to another use. | propose a staff reallocation
teaching load | The amount of teaching assigned to a staff member. | assess teaching load
contact hour | An hour of direct teaching or scheduled learner contact. | calculate contact hours
tutoring provision | The organized availability of additional learning support. | preserve tutoring provision
temporary appointment | A staffing arrangement for a limited period. | approve a temporary appointment
qualification requirement | The credential or competence needed for a role. | verify qualification requirements
availability check | Confirmation that a person or resource can be scheduled. | complete an availability check
class cap | The maximum permitted class size in the stated setting. | respect the class cap
additional capacity | Extra places or service volume available. | add teaching capacity
unmet demand | Need or requests not covered by available provision. | quantify unmet demand
waiting-list balance | The number still waiting after an allocation. | calculate the waiting-list balance
direct cost | A charge directly attributable to an option. | compare direct costs
all-inclusive cost | A stated price including all specified costs for the option. | confirm the all-inclusive cost
budget headroom | The amount remaining within an available budget. | calculate budget headroom
uncommitted budget | Funds not yet assigned to another approved use. | verify the uncommitted budget
opportunity cost | The value of the alternative use given up. | explain the opportunity cost
service trade-off | A gain in one service accompanied by a loss elsewhere. | state the service trade-off
staffing business case | A reasoned proposal for a staffing decision. | present a staffing business case
funding approval | Authorization to use funds for a specified purpose. | obtain funding approval
timetable feasibility | Whether a proposal fits the available schedule. | check timetable feasibility
room availability | Whether a suitable teaching space can be used. | confirm room availability
institutional priority | A stated objective guiding organizational choices. | align with institutional priorities
decision condition | A requirement that must hold for a decision to proceed. | state the decision conditions''',
    precision='Option B costs $4,800 against $5,000 available, leaving $200 of budget headroom. The all-inclusive cost and availability are supplied facts. Staying within budget does not itself grant funding approval or authorize a commitment.',
    precision_extra='Option A has no additional direct staffing charge, but removes four weekly tutoring hours. That service trade-off is not a dollar amount given in the brief. Neither option accommodates all 24 waiting learners in a single 20-place class.',
    phrases='''State demand | "There are 24 learners on the waiting list."
State the cap | "The extra class can take 20."
Keep unmet demand visible | "Four learners would still be waiting."
Explain reallocation | "Option A moves four weekly hours from tutoring to teaching."
Avoid a misleading zero | "There is no additional charge, but tutoring capacity falls."
State the temporary cost | "Option B has an all-inclusive cost of $4,800."
Identify available funds | "The uncommitted budget is $5,000."
Calculate headroom | "That leaves $200 within the budget."
Confirm supplied readiness | "Qualifications, availability, room, and timetable are confirmed."
Name the priority | "The stated priority is preserving tutoring while adding places."
Make the recommendation | "Option B best meets that priority on the supplied facts."
Keep approval distinct | "Funding approval is still pending."
Avoid premature commitment | "Do not confirm the appointment before authorization."
Explain opportunity cost | "Reallocation gives up four tutoring hours each week."
Bound the claim | "This adds one class; it does not clear the waiting list."
Close with the decision | "We need approval for Option B and a separate response to the remaining demand."''',
    notes='''No additional charge | Does not mean no effect on other services.
All-inclusive | Use the specified scope; do not assume hidden exclusions without evidence.
Available budget | Not the same as permission to spend.
Qualified and available | Necessary readiness information, not a signed appointment.
Headroom | Budget remaining after the stated cost.
Recommended | A proposed choice, not an already authorized commitment.''',
    d='''What is the budget headroom under Option B? | $200 | $4,800 | $5,000 | $9,800 | Subtracting the all-inclusive cost of four thousand eight hundred from five thousand leaves two hundred.
Which description of Option A is most accurate? | No additional direct charge, but four weekly tutoring hours are displaced. | No cost or service consequence of any kind. | It preserves all tutoring and costs $4,800. | It creates twenty-four places. | The option's financial charge is zero while its supplied service trade-off is real.
Which recommendation is best supported? | Recommend Option B to preserve tutoring, subject to approval, while acknowledging four learners still waiting. | Promise all waiting learners immediate places. | Approve spending solely because it fits the budget. | Describe Option A as identical to Option B. | This recommendation follows the stated priority, budget, approval boundary, and remaining capacity gap.
What is still required before a staffing commitment? | Funding approval | Recalculating twenty-four minus twenty as zero | Assuming a room conflict despite confirmed feasibility | Deleting the tutoring impact | The brief confirms operational readiness but explicitly leaves funding authorization pending.''',
    dialogue='''Elise | Twenty-four learners are waiting. The proposal for one additional class needs to explain staffing and remaining demand clearly.
Kiran | The [[class cap::The class cap limits the new class to twenty learners, so it cannot accommodate the entire twenty-four-person waiting list.]] is twenty. One class adds twenty places and leaves four learners waiting. Neither staffing option changes that limit, so we should not describe either as clearing the list.
Elise | Option A uses an existing qualified teacher for four hours each week. There is no additional direct staffing charge, which makes it look attractive.
Kiran | But the [[reallocation::Reallocation moves existing staff time from tutoring to the new class, creating a service loss as well as extra teaching capacity.]] removes four weekly tutoring hours. The teacher's time is not an unused resource. The proposal needs to show what is displaced, not just the absence of a new invoice.
Elise | Our priority is preserving tutoring while adding places. What is the full cost of temporary support?
Kiran | Its [[all-inclusive cost::The supplied all-inclusive cost is four thousand eight hundred dollars, not an hourly rate or an incomplete estimate.]] is four thousand eight hundred dollars. The person is qualified and available, and both options meet the room and timetable requirements. Those readiness checks are confirmed.
Elise | We have five thousand uncommitted dollars. Please state the remaining amount, rather than saying the cost is approximately within budget.
Kiran | The [[budget headroom::Budget headroom is the two hundred dollars remaining after subtracting the stated cost from the uncommitted budget.]] is two hundred dollars. Five thousand minus four thousand eight hundred leaves that amount. The option fits the supplied budget, although fitting it does not authorize spending.
Elise | Good. Funding approval is still pending. We should not tell the temporary teacher that the appointment is confirmed while the decision is unresolved.
Kiran | Exactly. [[Funding approval::Funding approval is the authorization still needed before a commitment, separate from available funds and operational readiness.]] remains a decision condition. We can recommend the option and describe readiness, but we must keep the appointment unconfirmed until the authorized decision is made.
Elise | Let us keep no additional staffing charge in the comparison, but put the lost tutoring hours right beside it. That is the actual choice.
Kiran | State the [[service trade-off::The service trade-off is the loss of four weekly tutoring hours; the brief does not assign that loss a dollar value.]] in its own terms: four tutoring hours are lost each week. The brief does not price that loss. We should neither ignore it nor invent a dollar equivalent.
Elise | Then Option B meets the tutoring priority more closely, while Option A reduces that service. Both add the same twenty places and fit the practical timetable.
Kiran | That supports the [[staffing business case::The staffing business case connects the recommendation to cost, capacity, feasibility, and the stated institutional priority.]] for Option B. The recommendation follows the supplied priority and facts, not a general claim that temporary staffing is always better than using existing staff.
Elise | Before families hear about an extra class, the message needs to say twenty places, not twenty-four. What happens to the remaining four is still unresolved.
Kiran | Keep that [[unmet demand::Unmet demand is the remaining need not covered by the new class, here four learners still awaiting places.]] visible. The proposal adds capacity without resolving every request. Any further provision would need its own feasible plan and authorization rather than being implied by this decision.
Elise | The final paragraph should ask for the exact approval needed, state the full cost, and make clear that tutoring is preserved under the recommended option.
Kiran | I will connect it to the [[institutional priority::The institutional priority is the supplied objective of preserving tutoring while adding capacity, which justifies the choice between otherwise feasible options.]] and record the two hundred dollars remaining. We should also state the capacity limit so the budget decision is not confused with a promise to all families.
Elise | Please request approval. Do not confirm the appointment or change tutoring while the decision is pending.
Kiran | I will state those [[decision conditions::Decision conditions define what must be authorized before the proposal proceeds, preventing a recommendation from being treated as a completed commitment.]] explicitly. The recommended class can add twenty places and preserve tutoring for four thousand eight hundred dollars, subject to approval, with four learners still waiting.''',
    transfer_title='Budget room does not equal approval',
    transfer_setup='An extra class has 18 places for 22 waiting learners. Qualified temporary support is available for an all-inclusive $3,600 against $4,000 uncommitted. It preserves existing tutoring, but spending approval is pending.',
    transfer='''Manager: "The remaining waiting-list count would be ___." | four | Twenty-two waiting learners minus eighteen new places leaves four without a place.
Principal: "The remaining budget would be ___ dollars." | 400 | Four thousand dollars minus three thousand six hundred leaves four hundred.
Manager: "Existing tutoring would be ___." | preserved | The supplied temporary-support option does not reallocate current tutoring hours.
Principal: "The spending decision remains ___." | pending | Available funds and staffing do not replace the outstanding authorization.''',
    rehearsal=['Read turns 1-8, giving a clear pause before the four learners still waiting and the $200 remaining.', 'Repeat turns 9-14, distinguishing a budget balance from spending authorization.', 'Switch roles for the transfer; read the $400 headroom separately from the four remaining learners.']))
