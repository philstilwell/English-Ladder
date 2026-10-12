"""Original university teaching and faculty-work communication."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='university-professors', title='University Professors English', category='Education & public service',
    balanced_answer_columns=True,
    cover_label='ENGLISH FOR UNIVERSITY TEACHING', cover_title='University Professors', cover_size=27,
    tagline='Teach clearly. Challenge ideas. Support progress.',
    audience='For university professors, lecturers, instructors, and faculty members teaching and advising in English.',
    roles='university professors, lecturers, teaching faculty, course coordinators',
    summary='English for university teaching, seminar facilitation, assessment feedback, office hours, teaching-team coordination, accessibility, academic integrity, and curriculum decisions.',
    map_intro='Eight situations follow the work of a teaching professor: clarifying expectations, guiding a seminar, explaining feedback, helping in office hours, coordinating graders, implementing access arrangements, discussing integrity concerns, and making curriculum decisions.',
    notes_title='Make the intellectual demand clear.',
    notes_intro='Students can meet a demanding standard more readily when a professor names the task, explains the evidence, and distinguishes support from a promise about grades. Faculty conversations also require precise language about authority, process, and academic judgment.',
    field_notes=[
        ('Challenge the claim', 'A seminar can welcome disagreement while requiring accurate representation of evidence. Distinguish criticism of an argument from a judgment about its speaker.', '"Which part of the evidence supports that conclusion?"'),
        ('Name the criterion', 'Specific feedback connects a feature of the submitted work to the published criterion and a manageable next step.', '"The paragraph summarizes the article but does not yet compare its explanation with the second source."'),
        ('Make support usable', 'A referral should identify the relevant service and next step without diagnosing a student, promising an exception, or disclosing private information.', '"Let us identify the appropriate contact and what they need to arrange this."'),
        ('Separate recommendation from decision', 'Faculty proposals, committee votes, approvals, and implementation can be different stages. State the actual institutional process.', '"The committee recommended the change; final approval is still pending."')],
    scope_note=FICTION + 'Professional English practice, not institutional policy, legal advice, disability assessment, academic-integrity adjudication, or a grading system for real students. All course rules and committee procedures supplied in cases are fictional local rules, not universal university requirements. Use your institution\'s current policies, privacy and accessibility processes, authorized support services, and emergency procedures. Keep real student records confidential.',
    sources=[
        source('Cornell Center for Teaching Innovation. Assessing student learning.', 'https://teaching.cornell.edu/teaching-resources/assessing-student-learning', 'Background on formative and summative assessment; the exercises use original fictional course examples.'),
        source('Cornell Center for Teaching Innovation. Using rubrics.', 'https://teaching.cornell.edu/teaching-resources/assessing-student-learning/using-rubrics', 'Supports explicit criteria and feedback linked to demonstrated work rather than vague judgments.'),
        source('Cornell Center for Teaching Innovation. AI and academic integrity.', 'https://teaching.cornell.edu/generative-artificial-intelligence/ai-academic-integrity', 'Supports clearly communicated, assignment-specific expectations and the actual institutional process.'),
        source('US Department of Education. Academic adjustments for postsecondary students.', 'https://www.ed.gov/laws-and-policy/civil-rights-laws/disability-discrimination/disability-discrimination-key-issues/disability-discrimination-academic-adjustments-postsecondary-students', 'US accessibility context; actual arrangements require the institution\'s qualified process and individual circumstances.')], units=[])

BOOK['units'].append(unit(
    title='Making assignment expectations explicit', scene='Compare does not mean summarize twice',
    skill='Explain the required intellectual task, evidence, and submission details without expanding the assignment.',
    brief='Professor Chen assigns a 600-word comparison of two supplied articles. Students must identify one shared question, explain one difference in the authors\' reasoning, and support that comparison with a passage from each article. Outside sources are not required. A formative outline is due Friday; the graded submission is due the following Tuesday. Student Maya has planned two separate summaries.',
    cast='Maya | Student\nProfessor Chen | Course instructor',
    culture=('Do not make the hidden task a test', 'Advanced students may understand the vocabulary but misread what a comparison requires. Clarifying the task maintains the academic standard.'),
    a='''What is the central task? | Compare the reasoning in two supplied articles | Summarize each article without connecting them | Conduct an original survey | Add as many outside sources as possible | The assignment requires a shared question and a supported difference in reasoning.
Which submission is formative? | The Friday outline | The Tuesday graded submission | Both articles | An unsupplied oral examination | The brief explicitly labels Friday's outline as formative and Tuesday's submission as graded.
Which evidence is required? | A supporting passage from each supplied article | Only the student's opinion | Five outside articles | A new dataset collected by the student | The stated task requires support from both supplied texts, not new research.''',
    vocabulary='''learning outcome | Stated capability students should demonstrate through learning. | align the learning outcome
assignment brief | Instructions defining a particular assessed or practice task. | clarify the assignment brief
comparison | Analysis identifying meaningful similarities or differences. | develop a focused comparison
summary | Condensed account of the main content of a source. | distinguish summary from analysis
analytical claim | Statement offering an interpretation supported by reasoning and evidence. | formulate an analytical claim
textual evidence | Passage or feature of a text supporting an interpretation. | select textual evidence
assessment criterion | Standard used to judge a feature of student work. | explain the assessment criterion
formative assessment | Practice assessment used to support learning and improvement. | provide formative assessment
summative assessment | Assessment used to evaluate learning at a defined stage. | distinguish summative assessment
submission window | Period during which work can be submitted under stated rules. | confirm the submission window
word limit | Stated maximum or target length under the task rules. | apply the word limit
required reading | Material students are expected to read for the course. | identify the required reading
optional resource | Material available but not required for the stated task. | label an optional resource
scaffolding | Structured support helping students build toward a task. | provide appropriate scaffolding
prerequisite knowledge | Prior understanding needed for the learning task. | check prerequisite knowledge
task alignment | Connection between the activity and intended learning. | check task alignment
submission format | Required form or file type for delivering work. | specify the submission format
clarification announcement | Shared message resolving an instruction question. | post a clarification announcement''',
    precision='Two summaries do not necessarily compare reasoning. The supplied task requires a connection between the articles and evidence from both.',
    precision_extra='Formative describes the learning purpose here, not a universal rule that every formative task carries no marks. Follow the actual assignment instructions.',
    phrases='''Name the task | The goal is to compare their reasoning, not summarize them separately.
Locate the evidence | Which passage supports the difference you have identified?
Clarify the requirement | Use one passage from each of the two supplied articles.
Limit the scope | Outside sources are not required for this assignment.
Separate stages | Friday is the outline; Tuesday is the graded submission.
Explain the standard | I will assess how well the evidence supports the comparison.
Check understanding | Tell me which part connects the two authors.
Share the clarification | I will post the same clarification for everyone in the course.''',
    notes='''Compare versus describe | Compare requires a relationship between items; describe can address each item independently.
Required versus optional | Required is part of the task; optional offers an additional resource without silently adding a condition.
By Friday versus on Friday | By identifies a latest point; on identifies a day. Use the actual published time when needed.''',
    d='''Which plan best matches the brief? | A shared question, one reasoning difference, and evidence from both texts | Two unrelated summaries with no comparison | A new survey replacing both texts | Five outside sources without using the supplied articles | This plan contains the exact intellectual components and evidence requested.
Which clarification preserves scope? | Outside sources are not required | Add outside sources to receive any credit | Replace the articles with a personal example | Ignore the stated word limit | The brief does not require additional research or authorize replacing the texts.
What should the instructor assess in the central comparison? | How the cited passages support the stated reasoning difference | Whether the student agrees with the professor | Whether the paper uses the longest words | Whether the student added an unsupplied survey | The task concerns evidence-based comparison, not agreement, decorative complexity, or additional research.
Which announcement prevents unequal access to clarification? | Share the clarified requirement with the whole course | Tell only the student who asked | Add a hidden new criterion after submission | Change the deadline in a private conversation only | A shared clarification makes the same task information available to all students.''',
    dialogue='''Maya | I have planned three hundred words on each article. Is that enough to meet the requirement to compare them?
Professor Chen | Two summaries may not yet give us a [[comparison::A comparison explicitly relates the two texts, whereas separate summaries can leave their relationship unexplained.]]. What shared question do the authors address, and where does their reasoning differ?
Maya | Both ask why commuters change routes, but one emphasizes travel time while the other emphasizes reliable arrival.
Professor Chen | That gives you a focused [[analytical claim::An analytical claim offers a reasoned interpretation that the student can support with evidence from the two articles.]]. Now show the passages that support that difference rather than adding a general opinion about transport.
Maya | I marked a paragraph on average journey time in the first article and one on variation in the second.
Professor Chen | Those may provide the [[textual evidence::Textual evidence links the proposed interpretation to specific passages rather than leaving the comparison unsupported.]]. Explain how each passage supports your comparison instead of placing two quotations side by side without analysis.
Maya | I was about to search for five more articles because the task sounded too short to count as university work.
Professor Chen | The [[assignment brief::The assignment brief defines the actual required task and should not be expanded through assumptions about how much additional research looks impressive.]] asks you to work closely with the two supplied texts. Outside sources are not required here.
Maya | Then the challenge is the quality of the connection, not the number of sources I can add to the bibliography.
Professor Chen | Exactly. The relevant [[assessment criterion::The assessment criterion concerns the demonstrated quality of the evidence-based comparison rather than the quantity of extra sources.]] is how clearly your evidence supports the reasoning difference you identify.
Maya | I also see two dates. Is Friday the final deadline, or do we submit something different on Tuesday?
Professor Chen | Friday is the [[formative assessment::The formative assessment is the outline used to support improvement before the later graded submission in this fictional assignment.]] stage: an outline that lets us address the comparison before the graded submission on Tuesday.
Maya | I can use the outline feedback to check whether I have actually connected the articles rather than simply shortened each one.
Professor Chen | Yes. That is the purpose of the [[scaffolding::Scaffolding provides structured support for building the required skill before the more complete task.]], while the final work still needs to demonstrate your own understanding of the texts.
Maya | Does the six-hundred-word requirement mean I should give equal space to every paragraph of each article?
Professor Chen | No. The [[word limit::The word limit constrains the length but does not require equal coverage of every source paragraph or replace the task's analytical focus.]] makes selection important. Keep the shared question, the difference, and the evidence central.
Maya | I will organize the outline around that contrast and use the two passages to explain why the distinction matters.
Professor Chen | That matches the [[learning outcome::The learning outcome is the capability to demonstrate, here an evidence-based comparison rather than disconnected recall.]] for this assignment: making a supported comparison rather than recalling each article separately.
Maya | Other students may have read compare the same way I did. Could the course page include this clarification?
Professor Chen | I will post a [[clarification announcement::A clarification announcement shares the same resolved instructions with the course rather than giving a private advantage to one student.]] so everyone has the same instructions, without adding a new requirement or changing the published submission details.''',
    rehearsal=['Read the corrected exchange and stress compare, support, required, and formative.', 'Swap roles and repeat the three-part task and the two submission stages exactly as supplied.'],
    transfer_title='Optional reading became a requirement', transfer_setup='A course page labels an additional article optional. The assignment requires only the two supplied core articles. A student assumes the extra article is necessary for credit.',
    transfer='''Student: "The extra article is labeled ___." | optional | The page explicitly identifies the article as an additional resource, not a requirement.
Professor: "The assignment requires the two ___ articles." | core | The supplied task names the two core texts as the required materials.
Student: "I should focus on the stated assessment ___." | criteria | The student should follow the actual standards rather than invent an extra condition.
Professor: "I will share that ___ with the class." | clarification | A shared clarification gives everyone the same accurate assignment information.'''))

BOOK['units'].append(unit(
    title='Leading a rigorous and inclusive seminar', scene='Challenge the causal claim, not the speaker',
    skill='Guide disagreement, test an inference, and make room for a reasoned response.',
    brief='In a seminar, student Leo says a campus survey proves that using the library causes higher grades because frequent library users report higher grades. The survey records an association and supplies no causal design. Professor Okafor asks Leo to distinguish the observation from the inference and acknowledge prior preparation as a possible alternative explanation. No participant has established the actual cause.',
    cast='Leo | Seminar participant\nProfessor Okafor | Seminar leader',
    culture=('Disagreement is not a personal verdict', 'A seminar can challenge an argument firmly while treating its speaker with respect. Invite revision of the claim rather than humiliating the student.'),
    a='''What does the supplied survey establish? | An association in the reported data | A proven causal effect of library use | That prior preparation is the actual cause | That grades cause every library visit | The case supplies association without a design establishing the causal direction or mechanism.
Which alternative explanation is raised? | Prior preparation | Confirmed cheating by every participant | A measured library intervention | A randomized assignment process | Prior preparation is supplied as a possible alternative, not an established cause.
What should the professor challenge? | The unsupported causal inference | The student's right to speak | The student's nationality | Every observation in the survey as fabricated | The central issue is the leap from association to causation, not the student's identity or participation.''',
    vocabulary='''seminar | Academic session centered on discussion and analysis. | facilitate a seminar
discussion norm | Shared expectation governing participation. | establish discussion norms
turn-taking | Management of who speaks and when. | support equitable turn-taking
wait time | Pause allowing participants time to formulate a response. | allow wait time
probing question | Question that examines reasoning or assumptions. | ask a probing question
follow-up question | Question extending or clarifying a previous contribution. | pose a follow-up question
revoicing | Restating a contribution to check or clarify its meaning. | use revoicing
evidence-based disagreement | Challenge tied to evidence and reasoning. | model evidence-based disagreement
causal claim | Assertion that one factor produces an effect. | qualify a causal claim
association | Observed relationship that does not alone establish causation. | distinguish association from causation
alternative explanation | Different account that could explain an observation. | test an alternative explanation
confounding variable | Factor affecting interpretation of a relationship between variables. | identify a possible confounding variable
inference | Conclusion drawn from evidence or premises. | examine the inference
counterexample | Example challenging a general statement. | introduce a counterexample
scope condition | Circumstance limiting the application of an argument. | state the scope condition
qualified conclusion | Conclusion that retains relevant limits or uncertainty. | offer a qualified conclusion
discussion synthesis | Summary linking contributions and unresolved questions. | provide a discussion synthesis
participation balance | Distribution of opportunities to contribute. | monitor participation balance''',
    precision='The survey reports a relationship. It does not establish that library use causes higher grades, nor that the proposed alternative explanation is the true cause.',
    precision_extra='Respectful disagreement can be intellectually demanding. A revised, qualified conclusion is not the same as abandoning every useful observation.',
    phrases='''Challenge the inference | What lets us move from association to causation here?
Invite a revision | Can you restate that conclusion with the evidence limit included?
Offer an alternative | Could prior preparation affect both study habits and grades?
Protect the speaker | We are examining the claim, not judging the person making it.
Check meaning | Are you saying the survey shows a relationship or establishes a cause?
Make space | Let us give others a moment before taking the next response.
Return to evidence | Which part of the data supports that stronger wording?
Synthesize | We agree on the association; the causal explanation remains open.''',
    notes='''Shows versus proves | Shows can describe a finding; proves makes a stronger claim that needs appropriate support.
May explain versus explains | May explain offers a possibility; explains presents the account more definitively.
I disagree with the inference | This phrase directs disagreement toward the reasoning rather than the speaker's character.''',
    d='''Which revision fits the evidence? | Frequent library use is associated with higher reported grades | Library use has been proven to cause higher grades | Prior preparation is definitely the only cause | The association must be meaningless | The qualified statement preserves the observation without claiming an established causal explanation.
Which question invites rigorous discussion? | What other factor might account for both observations? | Why are you bad at reasoning? | Can we ignore the data because we disagree? | Should only the loudest speaker answer? | This question examines an alternative explanation rather than attacking or excluding participants.
Which statement about prior preparation is supported? | It is a possible alternative explanation | It has been measured as the sole cause | It disproves every survey response | It makes further analysis unnecessary | The brief supplies it as a possibility, not a verified explanation or conclusive refutation.
What should the closing synthesis preserve? | The association and unresolved causal question | A unanimous causal finding that never occurred | The professor's preference as proof | A personal ranking of speakers | The synthesis should accurately retain both the finding and its evidential limit.''',
    dialogue='''Leo | The survey proves that studying in the library improves grades. Frequent users reported higher grades than students who rarely go there.
Professor Okafor | Let us examine that [[causal claim::A causal claim says library use produces the grade difference, which the supplied association alone does not establish.]]. Does the survey establish a cause, or does it report a relationship?
Leo | It reports the relationship. I used proves because the difference seemed strong, but I do not know how students were selected.
Professor Okafor | Then start with [[association::Association describes the observed relationship without claiming that one measured factor caused the other.]]. A strong relationship can be worth discussing without settling the causal explanation.
Leo | Students who were already well prepared might be more likely to use the library and also receive higher grades.
Professor Okafor | That is an [[alternative explanation::An alternative explanation identifies another possible account of the observation without establishing that account as the actual cause.]] to examine. We should not announce it as the answer merely because it is plausible.
Leo | So prior preparation might affect our interpretation of the relationship, but we would need relevant evidence to assess it.
Professor Okafor | Yes. It could be a [[confounding variable::A confounding variable can affect interpretation of the relationship, but its role here remains a possibility requiring evidence.]]. Naming a possibility helps define the question rather than resolving it automatically.
Leo | I can revise my sentence to say that frequent library use is associated with higher reported grades in this survey.
Professor Okafor | That is a [[qualified conclusion::A qualified conclusion preserves the observed finding and its limits instead of replacing uncertainty with a stronger unsupported claim.]]. It keeps the finding while avoiding a causal promise the study design has not supplied.
Leo | I worried that changing my wording would make it sound as though my entire contribution was wrong and should be withdrawn.
Professor Okafor | Revising an [[inference::An inference is a conclusion drawn from evidence, and revising it can improve an argument without discarding the underlying observation.]] is part of rigorous discussion. We are examining the reasoning, not making a judgment about you.
Leo | Another student suggested that grades might influence where people choose to study. That is another direction we could investigate.
Professor Okafor | Good. Let us use that as a [[probing question::A probing question examines the reasoning or assumptions and can open a testable issue without treating it as an established result.]] about direction, rather than treating the first plausible story as settled.
Leo | Could you restate the distinction once more before we invite the next response? I want to be sure I have it.
Professor Okafor | The [[revoicing::Revoicing restates a contribution or distinction to check shared meaning before the discussion moves forward.]] is this: the reported grades differ with library use, but the cause of that difference remains unestablished here.
Leo | That gives others something specific to challenge. They can question the interpretation without dismissing the people who completed the survey.
Professor Okafor | Exactly. Our [[discussion norm::A discussion norm sets expectations for participation, here challenging claims with reasons rather than attacking the people making them.]] is to challenge claims with reasons and make room for a response.
Leo | I will keep the association in my summary and mark the causal explanation as an open question.
Professor Okafor | I will include that in the [[discussion synthesis::The discussion synthesis links what was established and what remains open rather than manufacturing consensus on an unproven causal story.]], then invite another contribution after a short pause so more participants have time to formulate it.''',
    rehearsal=['Read the corrected seminar exchange and stress association, possible, and remains open.', 'Swap roles and state the revised conclusion without selecting an unsupplied causal explanation.'],
    transfer_title='An alternative became the new certainty', transfer_setup='After the seminar, a note says prior preparation definitely caused the grade difference. The discussion identified it only as a possible alternative.',
    transfer='''Student: "Prior preparation was a possible ___." | explanation | The discussion raised a possibility rather than a confirmed causal result.
Professor: "It was not established as the ___." | cause | The supplied evidence does not identify the actual cause of the difference.
Student: "The original survey reported an ___." | association | The survey supports a relationship, not the stronger causal conclusion.
Professor: "Keep the conclusion appropriately ___." | qualified | The revised conclusion must retain the evidence limit stated in the case.'''))

BOOK['units'].append(unit(
    title='Giving precise feedback and correcting a grading error', scene='The total is wrong; the criterion still needs discussion',
    skill='Acknowledge a clerical error while explaining the difference between score correction and academic review.',
    brief='Student Sam receives criterion scores of 6, 7, and 8, but the recorded total is 19 rather than 21. Professor Rivera confirms the arithmetic error. Sam also requests 24 because of the time spent on the paper. The feedback says the second paragraph cites evidence without explaining how it supports the conclusion. A substantive grade change has not been decided.',
    cast='Sam | Student\nProfessor Rivera | Instructor',
    culture=('Own the error without bargaining away the standard', 'A professor can apologize and correct a verifiable mistake while discussing the academic criterion separately. Effort deserves recognition without being substituted for the stated assessment standard.'),
    a='''What is the correct total of the supplied criterion scores? | 21 | 19 | 24 | 18 | Adding the stated scores of six, seven, and eight gives twenty-one.
What remains undecided? | The requested substantive increase to 24 | Whether 6 plus 7 plus 8 equals 21 | Whether a paper was submitted | Whether the student spent time on the paper | The arithmetic correction is clear, but the larger academic score change has not been decided.
What does the feedback identify? | Evidence is cited without explaining its link to the conclusion | No evidence appears anywhere | The student's effort is irrelevant to learning | The paper was never read | The specific concern is the missing explanation connecting cited evidence to the conclusion.''',
    vocabulary='''rubric | Framework describing criteria and performance levels for assessment. | apply the published rubric
criterion score | Score assigned to one assessment dimension. | check the criterion score
recorded total | Total entered in the grade record. | correct the recorded total
clerical error | Administrative or transcription mistake distinct from academic judgment. | acknowledge a clerical error
arithmetic correction | Change fixing an incorrect numerical calculation. | make an arithmetic correction
substantive review | Reassessment of the underlying academic judgment. | request a substantive review
grade appeal | Formal challenge through the institution's stated process. | explain the grade-appeal process
feedback conference | Meeting discussing assessed work and improvement. | hold a feedback conference
evidence link | Explanation connecting evidence to a claim or conclusion. | strengthen the evidence link
performance descriptor | Description of work meeting a rubric level. | apply the performance descriptor
feedforward | Guidance directed toward the next attempt or future work. | provide specific feedforward
revision priority | Improvement selected for attention before other changes. | identify a revision priority
margin comment | Feedback placed beside a particular passage. | clarify a margin comment
holistic judgment | Overall evaluation rather than separate dimension scoring. | distinguish holistic judgment
gradebook | System recording student assessment results. | update the gradebook
review procedure | Stated process for examining an assessment concern. | follow the review procedure
evidence of learning | Work demonstrating the intended knowledge or skill. | identify evidence of learning
professional apology | Clear acknowledgment of an error and responsibility. | offer a professional apology''',
    precision='Correcting 19 to 21 fixes the supplied arithmetic. It does not decide whether any criterion score should change or promise the requested 24.',
    precision_extra='Explain the actual review process without discouraging a legitimate concern or inventing a universal rule about whether a review can change grades.',
    phrases='''Acknowledge the error | You are right; those scores total twenty-one, not nineteen.
Take responsibility | I am sorry for the recording error, and I will correct it.
Separate questions | The arithmetic correction and your request for a higher criterion score are separate.
Point to the work | This passage gives the evidence but does not yet explain the connection.
Recognize effort | I can see the work you put in; the score still needs to follow the stated criteria.
Make feedback usable | Add the missing reasoning link before polishing the wording.
Explain process | Let us use the published review procedure for the substantive concern.
Avoid a promise | Reviewing the concern does not predetermine the outcome.''',
    notes='''Correct versus reconsider | Correct fixes an established error; reconsider reviews a judgment that may or may not change.
Effort versus evidence | Effort concerns work invested; evidence of learning concerns what the submitted work demonstrates under the criteria.
Will correct versus may revise | Will correct commits to fixing the established mistake; may revise leaves an unresolved judgment open.''',
    d='''Which response takes appropriate responsibility? | You are right about the total; I will correct it to 21 | The system must be right because I entered it | I will award 24 to avoid discussing the issue | Your effort automatically changes every criterion score | The supplied arithmetic error is verifiable and should be acknowledged without an unrelated grade promise.
Which feedback is most actionable? | Explain how the quoted evidence supports the paragraph conclusion | Be more academic in every way | Try harder next time | Make the paper sound impressive | This comment identifies the specific missing reasoning step in the supplied work.
Which statement separates the issues? | The total correction does not decide the substantive review | Correcting the total proves every criterion score is wrong | A review guarantees the requested mark | Effort alone resolves the evidence criterion | Arithmetic and academic judgment are different issues in the supplied case.
What should the instructor avoid? | Discouraging the student from using the stated review process | Explaining the relevant criterion | Correcting the gradebook total | Recognizing the student's effort | A legitimate concern should be handled through the actual process rather than suppressed.''',
    dialogue='''Sam | My three scores are six, seven, and eight, but the gradebook total is nineteen. I think something has gone wrong.
Professor Rivera | You are right. The [[recorded total::The recorded total is the entered sum, which is incorrect because the supplied criterion scores add to twenty-one.]] should be twenty-one. I am sorry for that error and will correct the entry.
Sam | Thank you. I also spent several evenings on the paper, so I hoped the mark could be raised to twenty-four.
Professor Rivera | Let us separate the [[arithmetic correction::The arithmetic correction fixes the established sum and does not itself decide whether the underlying academic scores should change.]] from your concern about the academic assessment. They need different explanations.
Sam | The comment on paragraph two says the evidence is not connected to the conclusion, but I included a quotation there.
Professor Rivera | The quotation is present. The [[evidence link::The evidence link explains how the cited material supports the conclusion, which is different from merely including a quotation.]] is the missing step: the paragraph does not explain how that passage supports the conclusion you draw.
Sam | So the issue is not that I failed to cite anything, but that I left the reader to supply the reasoning.
Professor Rivera | Exactly. The [[performance descriptor::The performance descriptor defines the quality expected at the rubric level and keeps the feedback tied to the published standard.]] asks for an explained relationship, not simply the presence of a source.
Sam | I read the short comment as a judgment that the whole paper was poor, which made it difficult to know where to start.
Professor Rivera | I should make that [[margin comment::A margin comment concerns a particular passage and should identify its specific issue rather than imply an unsupported judgment about the entire work.]] more precise. The concern is this reasoning step, not a dismissal of every part of your work.
Sam | For the next assignment, would improving that connection be more useful than replacing ordinary words with longer academic expressions?
Professor Rivera | Yes. Make the missing explanation your [[revision priority::A revision priority identifies the most important next improvement, here the reasoning link rather than decorative vocabulary changes.]]. Clear reasoning matters more here than making the wording sound complicated.
Sam | I still want to understand whether the criterion score itself was applied consistently with the published rubric.
Professor Rivera | That is a request for [[substantive review::Substantive review examines the underlying academic judgment and remains distinct from correcting an established recording or calculation error.]]. We can follow the stated process without assuming the outcome in advance.
Sam | I appreciate the distinction. I was worried that pointing out the error would be treated as bargaining for points.
Professor Rivera | Raising a specific concern is legitimate. The [[review procedure::The review procedure provides the actual route for examining a grading concern rather than treating the request as improper negotiation.]] gives us a way to examine it against the work and criteria.
Sam | Then the immediate action is to fix the total, while the separate review addresses the criterion question.
Professor Rivera | Correct. I will update the [[gradebook::The gradebook is the record that needs the confirmed total correction, without silently changing unresolved criterion judgments.]] to reflect the arithmetic and keep the substantive request clearly identified.
Sam | For future work, I will explain how each selected passage supports the conclusion rather than leave that relationship implied.
Professor Rivera | That is useful [[feedforward::Feedforward directs feedback toward a concrete improvement in subsequent work without promising a particular future grade.]]. It gives you a specific next step, while the current review proceeds through the proper process.''',
    rehearsal=['Read the corrected exchange and distinguish the confirmed total from the unresolved criterion review.', 'Switch roles and repeat the concrete feedback about the evidence link without adding a promised grade.'],
    transfer_title='A recording correction became a grade promise', transfer_setup='An instructor confirms a missing two-point entry. A student interprets that correction as approval of a separate request for five additional points. The latter request remains unresolved.',
    transfer='''Instructor: "The missing two-point entry is a confirmed ___." | correction | The established recording issue is separate from the unresolved larger request.
Student: "The additional five points remain under ___." | review | The brief does not supply approval of the substantive request.
Instructor: "We will use the published assessment ___." | criteria | The academic concern must be examined against the actual assessment standards.
Student: "The outcome has not been ___." | promised | A review is not an advance guarantee of the requested change.'''))

BOOK['units'].append(unit(
    title='Making office hours a focused learning conversation', scene='More people is not a higher percentage',
    skill='Diagnose a specific misunderstanding through a worked example and check the student can apply the distinction.',
    brief='During a fifteen-minute office-hour meeting, student Noor asks why a chart cannot show that Group B had the higher participation rate merely because more people participated. Group A has 40 participants out of 100 eligible people; Group B has 60 out of 200. Professor Evans uses the supplied figures to distinguish counts from rates. The meeting does not determine a grade or change an assessment deadline.',
    cast='Noor | Student\nProfessor Evans | Instructor',
    culture=('Support does not require doing the task for the student', 'A focused meeting can model one distinction and check understanding without rewriting the student\'s assignment or promising a mark.'),
    a='''Which group has the larger participant count? | Group B, with 60 | Group A, with 40 | Both have 100 participants | The count cannot be identified | Sixty participants in B is a larger count than forty in A.
Which group has the higher participation rate? | A, at 40 percent | B, at 60 percent | B, at 30 percent | Both, at 40 percent | A is forty out of one hundred, while B is sixty out of two hundred, or thirty percent.
What is the meeting intended to resolve? | The difference between a count and a rate | A guaranteed higher grade | A deadline extension already approved | A complete rewrite of the student's assignment | The brief identifies a focused conceptual question, not a grade or deadline decision.''',
    vocabulary='''office hours | Scheduled time for students to consult an instructor. | hold accessible office hours
meeting agenda | Agreed focus for a discussion. | set a focused meeting agenda
diagnostic question | Question identifying the source of a misunderstanding. | ask a diagnostic question
worked example | Example showing the reasoning or steps of a solution. | explain a worked example
think-aloud | Spoken demonstration of the reasoning process. | model a think-aloud
conceptual misunderstanding | Incorrect understanding of an underlying idea. | identify a conceptual misunderstanding
procedural slip | Mistake in carrying out a process despite understanding the concept. | distinguish a procedural slip
numerator | Quantity above the fraction line, representing the counted part here. | identify the numerator
denominator | Quantity below the fraction line, representing the eligible group here. | check the denominator
absolute count | Number of observed items or people without normalization. | report the absolute count
participation rate | Proportion of the eligible group that participated. | calculate the participation rate
normalization | Expressing values relative to a common basis for comparison. | explain normalization
concept check | Short task checking understanding of an idea. | use a concept check
transfer of learning | Application of understanding to a different example. | check transfer of learning
retrieval practice | Recalling knowledge rather than only rereading it. | use retrieval practice
metacognition | Awareness and monitoring of one's own learning or reasoning. | support metacognition
learning bottleneck | Specific difficulty preventing further progress. | identify a learning bottleneck
follow-up appointment | Subsequent meeting for continued support. | arrange a follow-up appointment''',
    precision='Group B has more participants, but Group A has the higher participation rate. The denominator changes the comparison.',
    precision_extra='The supplied numerical example supports a language and reasoning conversation. It does not authorize changing an actual student grade or deadline.',
    phrases='''Focus the meeting | Which step stopped making sense to you?
Distinguish the quantities | Are you comparing the number of participants or the share of eligible people?
Identify the denominator | How many people could have participated in each group?
Model the reasoning | Forty out of one hundred is forty percent.
Invite a check | Explain why sixty participants can still represent a lower rate.
Keep the task bounded | Let us resolve this distinction before adding another topic.
Check transfer | Apply the same distinction to the second supplied group.
Close with a next step | Use counts for headcount and rates for the stated proportional comparison.''',
    notes='''More versus a larger share | More can compare counts; a larger share compares proportions relative to the relevant whole.
Out of versus compared with | Out of identifies a denominator; compared with identifies another quantity or group.
Cannot conclude versus is false | Cannot conclude identifies an evidence limit; it does not always establish that the proposition itself is false.''',
    d='''Which explanation correctly compares the groups? | B has more participants, but A has the higher rate | B has both the larger count and rate | A has sixty participants out of two hundred | The denominators can be ignored | The supplied figures give B sixty participants but thirty percent, versus A forty participants and forty percent.
Which question diagnoses the misunderstanding? | What is the eligible population for each count? | Why did you not work harder? | Can you memorize the larger number? | Would a longer answer sound more academic? | The denominator is the missing basis for the proportional comparison in this case.
Which sentence checks understanding rather than supplying a grade? | Explain why the larger count can have the lower rate | This explanation guarantees full marks | I will rewrite the entire assignment for you | The deadline is automatically extended | Asking for the distinction checks learning without making an unsupplied assessment or policy decision.
What should the final meeting summary contain? | The count-rate distinction and the next practice step | A promise that every chart uses the same denominator | An invented grade change | A conclusion that Group B has fewer participants | The meeting resolves the stated concept and identifies how to apply it accurately.''',
    dialogue='''Noor | I thought Group B performed better because sixty people participated, compared with forty in Group A. The feedback says to check the rate.
Professor Evans | Let us set a short [[meeting agenda::The meeting agenda focuses the available time on the specific count-versus-rate misunderstanding instead of trying to redo the whole assignment.]]: first distinguish the quantities, then use the two groups to check the idea.
Noor | I compared the number of people and did not look at how many people were eligible in each group.
Professor Evans | That identifies the [[learning bottleneck::The learning bottleneck is the specific missing denominator distinction that prevents the student from interpreting the comparison correctly.]]. You are using an absolute count to answer a question about a proportion.
Noor | Group A had one hundred eligible people, while Group B had two hundred, so the groups were not the same size.
Professor Evans | Exactly. The [[denominator::The denominator is the eligible group size in this example, which changes how each participant count becomes a rate.]] tells us the whole against which the participant count is being compared.
Noor | Then forty is the part for Group A, and sixty is the part for Group B.
Professor Evans | Those are the [[numerator::The numerator is the participating part of each fraction, not the full eligible population.]] values. For A, forty out of one hundred gives forty percent.
Noor | For B, sixty out of two hundred gives thirty percent, even though sixty is the larger number of participants.
Professor Evans | Good. That is the [[worked example::The worked example demonstrates the actual calculation and reasoning needed to separate counts from proportions.]]: B has the larger count, while A has the higher participation rate.
Noor | I can see why putting both raw counts on a chart does not by itself answer which group had the higher proportion.
Professor Evans | That is the purpose of [[normalization::Normalization expresses the counts relative to their eligible populations, allowing the stated proportional comparison.]] here. We compare each count with its own eligible population rather than treating the groups as equal in size.
Noor | Would it be accurate to say B had more participants but a lower share of its eligible population?
Professor Evans | Yes. That sentence separates the [[absolute count::The absolute count reports how many participated without dividing by the eligible population.]] from the proportional measure and keeps both facts intact.
Noor | I initially thought the feedback meant sixty was the wrong number, but the number was right and my interpretation was wrong.
Professor Evans | That is a [[conceptual misunderstanding::A conceptual misunderstanding concerns the meaning of the comparison, unlike a simple numerical or transcription slip.]] rather than a transcription error. Understanding the distinction will help with other unequal-size groups.
Noor | Can we check it once more without looking at the completed percentages, using the same supplied figures?
Professor Evans | Certainly. That [[retrieval practice::Retrieval practice asks the student to recall and apply the reasoning rather than only reread the completed explanation.]] will show whether you can reconstruct the reasoning instead of recognizing an answer that is already written.
Noor | A is forty percent and B is thirty percent. I will identify the eligible population whenever I report a participation rate.
Professor Evans | That completes the [[concept check::The concept check verifies the specific understanding developed in the meeting without promising a grade or changing the assignment requirements.]]. Use the distinction in your next practice, and bring any remaining specific question to a follow-up meeting.''',
    rehearsal=['Read the corrected exchange and say all four supplied numbers and both percentages clearly.', 'Switch roles and explain the contrast using more participants but a lower share.'],
    transfer_title='Equal counts, different rates', transfer_setup='Group C has 20 participants out of 50 eligible people. Group D has 20 out of 100. Their counts are equal; their rates are 40 percent and 20 percent.',
    transfer='''Student: "Both groups have the same participant ___." | count | Each group has twenty participants, so the absolute counts are equal.
Professor: "Their eligible populations form different ___." | denominators | Fifty and one hundred are the different totals used in the fractions.
Student: "Group C has the higher participation ___." | rate | Forty percent in C is higher than twenty percent in D.
Professor: "Equal counts do not guarantee equal ___." | proportions | Different denominators can produce different proportions from the same numerator.'''))

BOOK['units'].append(unit(
    title='Calibrating a teaching team before grades are released', scene='Fluent wording is not the missing reasoning',
    skill='Resolve a scoring difference through shared criteria, anchor examples, and a consistent review plan.',
    brief='Professor Malik and teaching assistant Elena use a fictional three-level evidence scale: 0 for no relevant evidence, 1 for relevant evidence without an explained link, and 2 for relevant evidence with an explained link. An anchor response contains a relevant quotation but no explanation of its connection. Elena gave 2 because the prose was fluent; Malik applied 1. Grades have not been released.',
    cast='Elena | Teaching assistant\nProfessor Malik | Course coordinator',
    culture=('Calibrate the judgment, not the person', 'A grading discussion should examine the criterion and submitted work, not rank graders by status. Agree how the same principle will be applied across the batch.'),
    a='''What score matches the supplied evidence scale for the anchor response? | 1 | 0 | 2 | A score cannot be assigned from the supplied facts | Relevant evidence without an explained link matches level one on the fictional scale.
Why did Elena assign 2? | The prose was fluent | The response contained no evidence | The student requested an extension | The grades had already been released | Elena used fluency as the reason for the higher evidence score.
What is the release status? | Grades have not been released | Every student has received a final result | The review is prohibited by policy | A formal appeal has concluded | The brief explicitly states that results remain unreleased.''',
    vocabulary='''teaching assistant | Staff member or student supporting teaching under the relevant role. | brief the teaching assistant
grading calibration | Process of aligning application of assessment standards. | conduct grading calibration
anchor response | Selected example used to illustrate a scoring standard. | discuss an anchor response
scoring guide | Instructions explaining how to assign marks. | apply the scoring guide
inter-rater agreement | Degree of consistency between assessors. | improve inter-rater agreement
double marking | Assessment of work by two markers under the stated process. | use double marking
moderation | Review supporting consistency and appropriateness of assessment. | conduct assessment moderation
borderline response | Work near the boundary between performance levels. | discuss a borderline response
criterion contamination | Influence of an unrelated feature on a criterion judgment. | avoid criterion contamination
batch review | Examination of a group of submissions under a defined process. | organize a batch review
release hold | Temporary pause before results are made available. | maintain the release hold
scoring rationale | Explanation linking a score to the work and standard. | document the scoring rationale
marking consistency | Application of the same relevant standard across work. | check marking consistency
anonymized sample | Example with identifying details removed under the actual process. | use an anonymized sample
adjudication | Resolution of a disputed judgment through the stated authority or process. | route for adjudication
teaching-team briefing | Meeting or message aligning course staff on responsibilities. | hold a teaching-team briefing
assessment dimension | Particular aspect of performance being evaluated. | separate assessment dimensions
release approval | Authorization to make results available. | obtain release approval''',
    precision='The fictional evidence scale assesses the explained link, not general fluency. The anchor response earns 1 under the supplied rule because the link is absent.',
    precision_extra='Calibration should apply the agreed standard consistently. Do not invent a universal moderation policy or quietly change a published criterion after seeing results.',
    phrases='''Return to the scale | Which descriptor matches what the response actually demonstrates?
Separate dimensions | Fluency and evidence use are different dimensions here.
Explain the score | The quotation is relevant, but the link is not explained.
Invite comparison | Let us score the same anchor before reviewing the next sample.
Name the inconsistency | We have applied different standards to the same feature.
Plan the review | We need to check whether the same issue affects other submissions.
Protect privacy | Use the approved anonymized samples for the briefing.
Confirm release | Results remain on hold until the agreed review and approval are complete.''',
    notes='''Consistent versus identical | Consistent applies the same standard; it does not require different work to receive identical scores.
Relevant versus explained | Evidence may be relevant while its connection to the conclusion remains unexplained.
Calibrate versus curve | Calibration aligns judgments with standards; changing a grade distribution is a different action.''',
    d='''Which scoring rationale follows the stated scale? | Relevant quotation present, explanatory link absent: 1 | Fluent prose always earns 2 for evidence | Any quotation automatically earns 2 | Missing explanation means no evidence exists: 0 | The scale distinguishes relevant evidence without explanation from both absent evidence and an explained link.
What is the main inconsistency? | Fluency influenced the evidence score | Both graders ignored every criterion | The anchor had no quotation | The grades were already public | Elena substituted an unrelated dimension for the stated evidence-link requirement.
What should the team check next? | Whether the same interpretation affected other work | Only the student's name | How to conceal the discrepancy | Whether to guarantee everyone a higher mark | A defined review should identify whether the inconsistent standard affected the wider batch.
Which statement preserves authority and status? | Release awaits the agreed review and approval | The teaching assistant may invent a new scale | Calibration automatically changes every mark | A discussion alone is final release approval | Review completion and actual release authorization are distinct steps in the case.''',
    dialogue='''Elena | I gave this response two points because it reads fluently and includes a relevant quotation. Your score is one.
Professor Malik | Let us return to the [[scoring guide::The scoring guide defines the actual evidence levels and prevents unrelated impressions from replacing the stated requirement.]]. What distinguishes level one from level two on this evidence scale?
Elena | Level two requires the response to explain how the evidence supports the conclusion. This response leaves that connection unstated.
Professor Malik | Then our [[anchor response::The anchor response illustrates the criterion boundary, here relevant evidence without the explanation required for the higher level.]] demonstrates level one, even though the prose is fluent.
Elena | I allowed the polished wording to influence my judgment about whether the reasoning was complete.
Professor Malik | That is [[criterion contamination::Criterion contamination occurs when an unrelated feature, here fluency, influences the score for a different assessed dimension.]]. We need to keep the evidence dimension separate from any criterion assessing expression.
Elena | I can explain the one-point score as relevant quotation present, but the explanatory link is absent.
Professor Malik | That gives a clear [[scoring rationale::The scoring rationale connects the assigned score to the actual work and descriptor instead of relying on an overall impression.]] that another grader can inspect and discuss.
Elena | Should we compare a second example where the link is partly implied? That seems more difficult than this clear case.
Professor Malik | Yes. A [[borderline response::A borderline response sits near a descriptor boundary and can help the team clarify consistent application without changing the published scale.]] can expose where we interpret the descriptor differently, without rewriting the published standard.
Elena | We can score it independently first and then compare the passages each of us relied on.
Professor Malik | That supports [[grading calibration::Grading calibration aligns how assessors apply the standard through shared examples and explicit reasoning.]]. The purpose is consistent judgment, not simply having the junior colleague copy a senior score.
Elena | I may have applied the same fluency shortcut to other papers in my batch, so correcting this one example is not enough.
Professor Malik | Then define a [[batch review::A batch review checks the relevant group of submissions for the identified scoring issue rather than fixing only the visible example.]] under our assessment process and identify the work that needs checking.
Elena | The grades are still unreleased. I can keep the results from being published while we complete the agreed check.
Professor Malik | Maintain the [[release hold::The release hold keeps unreviewed results from being made available while the identified assessment issue is addressed.]] and make the reason clear to the teaching team, without exposing student work unnecessarily.
Elena | For the briefing, I will use the approved anonymized examples and show the criterion alongside the relevant passages.
Professor Malik | Good. That should improve [[inter-rater agreement::Inter-rater agreement concerns consistency among assessors applying the same standard, not forcing every student result to be identical.]] by making our interpretation and evidence visible.
Elena | Once the review is complete, I will report what was checked and any changes made through the approved process.
Professor Malik | Then we can seek [[release approval::Release approval is the actual authorization to publish results after the required review, not merely the fact that graders discussed an example.]]. A calibration conversation is a useful step, but it is not the same as completing and authorizing the release.''',
    rehearsal=['Read the corrected exchange and apply the supplied 0-1-2 scale to the anchor response.', 'Switch roles and repeat the review and release sequence without inventing a new grading rule.'],
    transfer_title='The quotation is relevant but unexplained', transfer_setup='Under the same supplied scale, a second response includes relevant evidence but does not explain its link. The team has agreed to apply the criterion consistently.',
    transfer='''Assistant: "The evidence is ___." | relevant | The brief states that the selected evidence relates to the task.
Professor: "The explanatory link is ___." | absent | The response does not explain how its evidence supports the conclusion.
Assistant: "That matches level ___." | one | The supplied scale assigns one to relevant evidence without the explained link.
Professor: "Apply the same ___ across the reviewed work." | standard | Consistency requires the same descriptor rather than a different rule for each student.'''))

BOOK['units'].append(unit(
    title='Implementing an approved access arrangement', scene='The letter says ninety minutes; the platform says sixty',
    skill='Confirm practical accessibility arrangements without demanding unnecessary personal disclosure or making unsupported promises.',
    brief='Student Tessa has an approved arrangement specifying 90 minutes for a quiz whose standard duration is 60 minutes. Professor Ali sees that the learning platform still shows the standard setting. A suitable testing-room booking has not been confirmed. They need prompt coordination with the designated access office and testing staff. Tessa is not being asked to disclose a diagnosis to classmates or justify the approved arrangement again.',
    cast='Tessa | Student\nProfessor Ali | Instructor',
    culture=('Discuss access without making the student defend it', 'Focus on implementing the approved arrangement and resolving practical obstacles. Keep personal information within the appropriate institutional process.'),
    a='''What duration is specified in the approved arrangement? | 90 minutes | 60 minutes | 30 minutes | An unspecified unlimited period | The supplied approval specifies ninety minutes for this quiz.
Which two practical issues remain? | The platform setting and room confirmation | Whether the student may speak in class | A decided grade change and appeal | A requirement to disclose the diagnosis publicly | The platform still shows sixty minutes, and the room booking is unconfirmed.
What should the professor focus on? | Implementing and checking the approved arrangement | Asking classmates to vote on access | Requiring a public medical explanation | Assuming the platform has already updated itself | The case concerns practical implementation, not relitigation or public disclosure of the approval.''',
    vocabulary='''academic adjustment | Change supporting equal access under the relevant institutional and legal process. | implement an academic adjustment
approved accommodation | Arrangement approved through the institution's relevant process. | confirm the approved accommodation
accessibility office | Institutional service coordinating disability-related access arrangements. | coordinate with the accessibility office
implementation detail | Practical setting or action needed to carry out a plan. | confirm implementation details
extended time | Additional time specified for a task under an approved arrangement. | configure approved extended time
testing arrangement | Agreed practical conditions for an assessment. | verify the testing arrangement
accessible format | Presentation usable with the relevant access requirements. | provide an accessible format
assistive technology | Technology supporting access to information or activities. | check assistive-technology compatibility
captioning | Text representation of speech and relevant audio information. | arrange accurate captioning
screen-reader compatibility | Usability of digital content with software that reads its structure and text. | verify screen-reader compatibility
functional barrier | Feature of the environment or task obstructing access. | identify a functional barrier
essential requirement | Core academic or technical requirement under the relevant process. | identify the essential requirement
confidentiality boundary | Limit on sharing personal information. | maintain the confidentiality boundary
implementation confirmation | Verification that an approved arrangement is actually in place. | obtain implementation confirmation
testing coordinator | Person managing assessment logistics under the institutional process. | contact the testing coordinator
access concern | Reported difficulty obtaining or using an arrangement. | address an access concern
effective access | Practical ability to participate through suitable arrangements. | verify effective access
contingency arrangement | Authorized alternative if the planned arrangement cannot operate. | confirm a contingency arrangement''',
    precision='The approved 90-minute arrangement and the platform\'s 60-minute setting conflict. A displayed default does not cancel the approval.',
    precision_extra='Do not require unnecessary diagnostic disclosure or ask the student to negotiate access with classmates. Resolve implementation promptly through the actual institutional process.',
    phrases='''Acknowledge the mismatch | The platform setting does not match the approved ninety minutes.
Focus on implementation | We need to correct the practical arrangement, not ask you to justify the approval again.
Protect privacy | We can discuss the logistics without sharing your diagnosis with the class.
Name the contact | I will coordinate with the access office and testing staff.
Verify the change | I will check the student-facing setting after the update.
Avoid an empty assurance | The room is requested, but I do not yet have confirmation.
Plan for failure | We need an authorized alternative if the booking cannot be completed.
Close the loop | I will confirm the actual arrangements through the agreed private channel.''',
    notes='''Approved versus implemented | Approved records authorization; implemented means the practical arrangement is in place.
Requested versus booked | Requested identifies an application or inquiry; booked indicates confirmed allocation.
Same standard versus same conditions | Maintaining academic requirements does not imply that every student must use identical access arrangements.''',
    d='''Which response addresses the actual problem? | Correct and verify the platform setting through the approved process | Tell the student the default overrides the approval | Require a classroom explanation of the diagnosis | Assume an email request confirms the room | The supplied approval needs practical implementation and verification.
Which status statement is accurate? | The room has been requested but is not confirmed | The room is definitely booked | No testing arrangement is needed | The platform already shows ninety minutes | The brief leaves the room booking unresolved and identifies a conflicting platform setting.
What information should the discussion prioritize? | Necessary implementation details | A public account of the student's diagnosis | Classmate opinions about fairness | An unrelated student's private record | The case requires logistics and appropriate coordination, not unnecessary personal disclosure.
What should happen if the planned room cannot be arranged? | Coordinate an authorized alternative promptly | Leave the student to improvise alone | Cancel the approved arrangement automatically | Promise any room without checking | The actual institutional process should resolve access with a workable authorized contingency.''',
    dialogue='''Tessa | My approved letter specifies ninety minutes for the quiz, but the course platform still shows the standard sixty-minute limit.
Professor Ali | Thank you for flagging it. The [[implementation detail::The implementation detail is the practical platform setting, which must be aligned with the approved arrangement rather than treated as overriding it.]] does not match the approval, and we need to resolve that before relying on the setup.
Tessa | I was worried I would need to explain my diagnosis again to persuade you that the extra time is justified.
Professor Ali | We are discussing the [[approved accommodation::The approved accommodation has already been authorized through the relevant process; this conversation concerns carrying it out rather than requiring a new public justification.]], not asking you to justify it again. Let us focus on the necessary logistics.
Tessa | The testing room was requested last week, but I have not received a booking confirmation from the office.
Professor Ali | Then the [[testing arrangement::The testing arrangement includes the actual practical conditions, including a room whose confirmation remains unresolved here.]] is not yet fully confirmed. I will coordinate with the responsible staff rather than assume the request completed the booking.
Tessa | Which office should we include so that the timing setting and room information do not remain in separate conversations?
Professor Ali | I will contact the [[accessibility office::The accessibility office is the relevant institutional service for coordinating the approved access arrangement and resolving implementation questions.]] and testing coordinator through the appropriate process, using only the information needed to arrange access.
Tessa | I would prefer not to have my personal situation discussed in a general announcement to the class.
Professor Ali | Of course. We should maintain the [[confidentiality boundary::The confidentiality boundary limits personal-information sharing and keeps the logistical discussion within the appropriate private process.]] and use the agreed private channel for your specific arrangements.
Tessa | If the platform limit is changed, can you check what I will actually see rather than only the instructor setting?
Professor Ali | Yes. We need [[implementation confirmation::Implementation confirmation verifies that the arrangement is actually functioning, rather than stopping at a promise or an unchecked setting change.]], including the relevant student-facing view, so an administrative update does not leave the same practical problem.
Tessa | The quiz content itself has not changed, and I understand that the same academic requirements still apply.
Professor Ali | Correct. The [[essential requirement::The essential requirement concerns the academic demand, which remains distinct from the approved conditions used to provide access.]] and the access arrangement are different questions; identical conditions are not the only way to maintain the academic standard.
Tessa | What happens if the requested room cannot be confirmed in time? I do not want to arrive without a workable plan.
Professor Ali | We need a [[contingency arrangement::A contingency arrangement is an authorized workable alternative if the intended setup cannot operate, not an improvised cancellation of the approval.]] agreed through the actual process, and I will raise that promptly rather than leave you to improvise.
Tessa | Thank you. A clear confirmation of the duration, location, and contact would resolve the uncertainty for me.
Professor Ali | That is the aim of [[effective access::Effective access concerns the practical ability to participate, not merely the existence of an approval letter or a request in an inbox.]]: the arrangement has to work in practice, not just exist as an approved document.
Tessa | I will use the private channel if the displayed information still conflicts with the confirmation you send.
Professor Ali | Please do. Any remaining [[access concern::An access concern is a reported practical obstacle that should be addressed through timely coordination rather than dismissed after an administrative assurance.]] needs prompt attention, and I will close the loop when the actual setting and testing arrangements are verified.''',
    rehearsal=['Read the corrected exchange and distinguish approved, requested, implemented, and confirmed.', 'Switch roles and repeat the three confirmation items: duration, location, and contact.'],
    transfer_title='The setting changed but the booking did not', transfer_setup='The platform now correctly shows 90 minutes. The testing-room request remains unconfirmed. The approved arrangement still needs a workable location.',
    transfer='''Instructor: "The platform duration is now ___." | correct | The displayed ninety-minute duration now matches the approved arrangement.
Student: "The room booking remains ___." | unconfirmed | The scenario expressly leaves the testing-room request unresolved.
Instructor: "I will contact the testing ___." | coordinator | The responsible testing contact can address the practical location question.
Student: "Please send the final arrangement ___." | confirmation | The student needs verified logistics, not merely another unconfirmed request.'''))

BOOK['units'].append(unit(
    title='Discussing an academic-integrity concern fairly', scene='A missing source needs a factual explanation',
    skill='State a specific concern, explain the applicable course rule, and separate an inquiry from a finding.',
    brief='A fictional assignment permits AI-assisted brainstorming if disclosed but requires the submitted analysis to be the student\'s own work. Professor Park cannot locate a cited article and finds that its journal details do not match the supplied reference. Student Amir says he used a tool for an outline and believed the suggested reference was real. No integrity finding or penalty has been determined; the actual institutional review process applies.',
    cast='Amir | Student\nProfessor Park | Instructor',
    culture=('Be specific before being conclusive', 'A concern about a reference warrants careful inquiry. State the discrepancy and relevant rule without treating a student\'s accent, fluency, or a tool flag as a verdict.'),
    a='''What does the fictional assignment permit? | Disclosed AI-assisted brainstorming | Undisclosed generated final analysis | Any invented citation if formatted correctly | Automatic delegation of the whole assignment | The supplied rule permits brainstorming with disclosure while requiring the student's own submitted analysis.
What is the concrete concern? | A cited article cannot be located and its details mismatch | The student's accent | A confirmed confession of every allegation | A final penalty already imposed | The brief identifies a specific reference discrepancy, not an identity-based suspicion or determined outcome.
What is the review status? | No finding or penalty has been determined | A violation has been conclusively established | The inquiry has been abandoned | The professor has approved every reference | The case expressly leaves any formal finding and consequence unresolved.''',
    vocabulary='''academic integrity | Honest and responsible participation in academic work. | uphold academic integrity
permitted assistance | Help allowed under the stated assignment rules. | clarify permitted assistance
authorship | Responsibility for producing the submitted work. | explain authorship
attribution | Identification of the source of ideas, wording, or assistance. | provide appropriate attribution
disclosure statement | Account of assistance or tool use required by the task. | review the disclosure statement
source verification | Checking that a cited source exists and supports the use made of it. | complete source verification
fabricated reference | Citation identifying a source that is not genuine as represented. | investigate a potentially fabricated reference
citation discrepancy | Mismatch or problem in reference details. | identify a citation discrepancy
process evidence | Material relevant to how work was developed. | review relevant process evidence
draft sequence | Ordered versions showing development of a document. | preserve the draft sequence
unauthorized collaboration | Cooperation not allowed by the stated task rules. | distinguish unauthorized collaboration
similarity report | Tool output indicating textual matches for review. | interpret a similarity report
allegation | Assertion of a possible violation not itself a finding. | distinguish an allegation from a finding
finding | Determination reached through the relevant review process. | communicate the actual finding
procedural fairness | Appropriate and fair handling under the relevant process. | maintain procedural fairness
opportunity to respond | Chance to address a concern through the stated process. | provide an opportunity to respond
referral for review | Routing a concern to the designated process or authority. | make a referral for review
educational consequence | Learning-related outcome or requirement under the applicable decision. | explain an authorized educational consequence''',
    precision='The source discrepancy is a fact to investigate. It does not establish the complete history of tool use, intent, or a formal violation by itself.',
    precision_extra='Fictional course rules here are not universal AI policies. Use the actual communicated assignment requirements and institutional process; do not invent evidence or presume a penalty.',
    phrases='''State the concern | I could not locate this article, and the journal details do not match.
Invite an account | Please explain where the reference came from.
Clarify the rule | The assignment permits disclosed brainstorming, not generated final analysis.
Separate the issue | A tool suggestion still needs source verification.
Avoid a verdict | This meeting does not predetermine a finding.
Protect fairness | You will have the opportunity to respond through the stated process.
Preserve records | Keep the relevant existing drafts and source information intact.
Explain next steps | I will explain the applicable review route and what happens next.''',
    notes='''Concern versus finding | Concern identifies a matter to examine; finding is an actual determination through the relevant process.
Reported versus admitted | Reported attributes an account; admitted can imply acceptance of wrongdoing and should not replace neutral description without basis.
Permitted with conditions | Permission can depend on disclosure, task stage, or other stated limits; it is not unrestricted permission.''',
    d='''Which opening is most appropriate? | I cannot locate this reference; please explain its source | Your fluent wording proves misconduct | A tool flag settles every question | The penalty is fixed before you respond | This opening states a concrete discrepancy and invites an account without a predetermined verdict.
Which rule summary matches the case? | Brainstorming is allowed with disclosure; final analysis must be the student's own | Every AI use is forbidden in every university course | Any tool-generated final text is allowed if polished | Citation formatting makes invented sources acceptable | This choice preserves the assignment-specific permission and its limits.
What should happen to existing drafts? | Preserve relevant records through the actual review process | Alter them to support a preferred account | Delete inconvenient versions | Present newly invented notes as contemporaneous | Existing records should remain intact rather than be fabricated or manipulated.
Which status language is accurate? | A concern is being reviewed; no finding is determined | A complete violation is already proven | The source has been verified as genuine | The student has no opportunity to respond | The supplied case identifies an inquiry with an unresolved formal outcome.''',
    dialogue='''Amir | Your message says there is a concern about my reference list. I am worried that you have already decided I cheated.
Professor Park | No finding has been made. I want to explain a specific [[citation discrepancy::The citation discrepancy is the mismatched and unlocated source information, not a complete determination of misconduct.]] and hear your account through the appropriate process.
Amir | Which reference is the problem? I used a tool to help outline the topic and thought the suggested article was real.
Professor Park | I could not locate that article, and the journal details do not match. It needs [[source verification::Source verification checks that a reference exists and supports its use, which is required even when a tool suggested it.]] rather than an assumption based on a plausible-looking citation.
Amir | The assignment allowed brainstorming, so I understood that I could ask for possible topics and an outline.
Professor Park | It allowed that [[permitted assistance::Permitted assistance is bounded by the actual assignment rule, here disclosed brainstorming rather than unrestricted generation of the final analysis.]] with disclosure. It also required the submitted analysis to be your own work.
Amir | I included a short note about the outline tool, but I did not explain that the reference came from its suggestion.
Professor Park | We need to examine the actual [[disclosure statement::The disclosure statement records the assistance reported and should be examined against the communicated requirement rather than assumed complete.]] and the relevant facts, not broaden or narrow the rule during this conversation.
Amir | I understand that even if brainstorming was allowed, I still needed to check whether the cited source existed.
Professor Park | Correct. Accurate [[attribution::Attribution identifies sources and assistance honestly, but a citation label does not make an unverified or nonexistent source genuine.]] and source checking remain important. A convincing format does not establish that a reference is genuine.
Amir | I have the drafts and notes I actually used. Should I keep them as they are rather than try to tidy the history?
Professor Park | Yes. Preserve the relevant [[process evidence::Process evidence concerns the actual development record and should be preserved, not retrospectively fabricated or altered to fit an account.]] through the appropriate process. Do not create a different history to make the record look cleaner.
Amir | Will this conversation determine the outcome immediately, or is there a separate university procedure I need to understand?
Professor Park | I will explain the applicable route. A concern or [[allegation::An allegation identifies a possible violation and must remain distinct from a formal finding reached through the relevant process.]] is not itself the final determination.
Amir | I want to respond to the specific source issue and understand what information the process asks me to provide.
Professor Park | You should have the stated [[opportunity to respond::The opportunity to respond allows the student to address the identified concern through the relevant institutional process.]], with clear information about the concern and the actual next steps.
Amir | Thank you. I do not want my explanation summarized as admitting things I have not said or that have not been established.
Professor Park | I will record your account accurately and maintain [[procedural fairness::Procedural fairness requires appropriate handling of the concern and response rather than a predetermined conclusion or distorted account.]] under the institution's process.
Amir | For now, I will preserve the existing materials and respond to the identified question about the source and its use.
Professor Park | That is the next step. Any [[finding::A finding is an actual determination under the relevant process, which has not yet occurred in this fictional case.]] or authorized consequence must be communicated as an actual outcome, not implied in advance by this inquiry.''',
    rehearsal=['Read the corrected exchange and distinguish the permitted brainstorming rule from the source-verification issue.', 'Switch roles and state the concern, response opportunity, and unresolved status without inventing intent or a penalty.'],
    transfer_title='A report was mistaken for a verdict', transfer_setup='A tool report flags a passage for review. The instructor has not checked the source or completed the institutional process. No finding exists.',
    transfer='''Instructor: "The report identifies a passage for ___." | review | A tool flag directs attention to material and does not itself determine misconduct.
Student: "It is not a formal ___." | finding | The case contains no completed institutional determination of a violation.
Instructor: "We need to check the actual ___." | evidence | The underlying facts and sources require assessment through the appropriate process.
Student: "I need the stated opportunity to ___." | respond | The student should address the specific concern through the actual review procedure.'''))

BOOK['units'].append(unit(
    title='Making a faculty curriculum decision traceable', scene='A recommendation is not implementation approval',
    skill='Clarify a proposal, test resource assumptions, and summarize the actual committee decision.',
    brief='A fictional department committee discusses increasing a seminar enrollment cap from 20 to 30. Professor Grant supports access; Professor Silva asks about feedback workload and room capacity. A motion is amended to recommend a one-term pilot only if staffing and a suitable room are confirmed. The committee votes for that recommendation. Under the supplied local process, a separate faculty board must approve implementation; that approval has not occurred.',
    cast='Professor Grant | Committee member\nProfessor Silva | Committee chair',
    culture=('Disagree on conditions without implying opposition to the goal', 'Faculty can share a goal while disagreeing about readiness. State the unresolved resource question and the decision authority rather than labeling colleagues obstructive.'),
    a='''What enrollment change was initially discussed? | From 20 to 30 | From 30 to 20 | From 20 to 60 | No change to enrollment | The supplied proposal increases the seminar cap by ten students.
What did the committee vote for? | A conditional one-term pilot recommendation | Immediate unconditional implementation | Permanent approval by every body | Cancellation of the seminar | The amended motion recommends a pilot subject to staffing and room confirmation.
Which approval remains outstanding? | The separate faculty board approval | The committee vote already reported | A student vote required by the brief | An external accreditation decision already supplied | The fictional local process assigns implementation approval to a board that has not yet approved it.''',
    vocabulary='''curriculum proposal | Suggested change to a program or course structure. | submit a curriculum proposal
enrollment cap | Maximum permitted enrollment under the stated arrangement. | revise the enrollment cap
teaching allocation | Assignment of teaching responsibilities or resources. | confirm the teaching allocation
contact hours | Scheduled instructional time with students. | calculate contact hours
feedback workload | Time and effort required to respond to student work. | assess feedback workload
resource assumption | Premise about available staffing, space, or support. | test a resource assumption
committee motion | Formal proposal presented for a committee decision. | put forward a committee motion
motion amendment | Proposed change to the motion under discussion. | agree a motion amendment
quorum | Required participation for valid business under the applicable rules. | confirm quorum
abstention | Decision not to cast a vote for or against. | record an abstention
meeting minutes | Formal record of discussion and decisions. | approve the meeting minutes
decision authority | Person or body empowered to make the relevant decision. | identify decision authority
conditional recommendation | Recommendation dependent on specified unresolved conditions. | record a conditional recommendation
pilot offering | Limited trial delivery before a broader decision. | plan a pilot offering
implementation approval | Authorization to put a proposal into operation. | obtain implementation approval
course capacity | Ability to deliver a course for the proposed enrollment. | verify course capacity
review checkpoint | Defined stage for evaluating progress or results. | establish a review checkpoint
dissenting view | Position disagreeing with the proposal or majority. | record a dissenting view''',
    precision='The committee recommended a conditional pilot. It did not provide the separate implementation approval required by the supplied local process.',
    precision_extra='Committee rules vary. Quorum, voting, authority, and minute-taking must follow the actual institution; the case supplies only its fictional decision sequence.',
    phrases='''Separate goal from readiness | I support wider access, but the staffing assumption is unresolved.
Make the condition explicit | The pilot depends on confirmed teaching support and a suitable room.
Clarify the motion | Are we recommending a pilot or authorizing immediate implementation?
Identify authority | The faculty board must approve implementation under this process.
Invite precise dissent | Which condition would need to change for you to support the proposal?
Record the amendment | The recommendation is limited to one term.
Preserve status | The committee vote does not complete the board approval.
Summarize next steps | Verify the resources, submit the recommendation, and await the actual decision.''',
    notes='''Recommend versus approve | Recommend proposes a course of action; approve exercises the relevant authority to authorize it.
Subject to versus after | Subject to retains a condition; after identifies sequence but may not clearly state a dependency.
Support the goal versus support this version | Agreement with an objective does not imply agreement with every implementation proposal.''',
    d='''Which minute accurately records the outcome? | Conditional one-term pilot recommended; board approval pending | Thirty places are permanently approved from today | All staffing and rooms are confirmed | The committee rejected wider access entirely | This choice preserves the amended recommendation and the separate outstanding approval.
Which response identifies a resource issue without dismissing the goal? | I support access, but we need to verify feedback capacity | Anyone questioning staffing opposes students | Room availability is irrelevant to implementation | A favorable vote creates staff automatically | This statement separates the shared objective from the practical capacity question.
What must remain visible in the recommendation? | The staffing and room conditions | Only the headline enrollment number | An invented unanimous vote | A claim that the board already approved it | The conditions limit the recommendation and cannot be removed without changing its meaning.
What is the next decision-status distinction? | Submission to the board versus board approval | A committee title versus a course title | A room name versus a page number | A contact list versus an attendance list | Sending the recommendation does not establish that the authorized body has approved implementation.''',
    dialogue='''Professor Grant | I support raising the seminar cap from twenty to thirty. More students want access, and the current limit leaves some out.
Professor Silva | I support that goal too. Before we settle the [[curriculum proposal::The curriculum proposal is the suggested change under discussion, not an already authorized implementation decision.]], we need to examine the teaching and room assumptions.
Professor Grant | My concern is that resource questions will delay the idea indefinitely, even though the demand is already visible.
Professor Silva | Let us make them specific. The [[feedback workload::Feedback workload concerns the actual capacity to respond to additional student work and is a practical condition rather than opposition to access.]] increases with enrollment, and the current staffing plan has not addressed that increase.
Professor Grant | We could recommend a limited trial rather than a permanent change, provided the teaching support is confirmed.
Professor Silva | That would be a [[pilot offering::A pilot offering is a limited trial rather than a permanent change, allowing the proposal to be bounded in duration and scope.]]. We should state the duration and conditions clearly instead of leaving them in informal discussion.
Professor Grant | I propose one term, subject to confirmed staffing and a room suitable for thirty participants.
Professor Silva | That is a [[motion amendment::A motion amendment changes the proposal being decided, here limiting it to a conditional one-term pilot.]] to the original proposal. We need the committee to know exactly which version it is voting on.
Professor Grant | The revised wording still supports increased access, but it does not assume that a larger room and staff already exist.
Professor Silva | Correct. It makes the [[resource assumption::The resource assumption identifies capacity that must be verified rather than treated as created by a favorable vote.]] visible and gives the responsible colleagues concrete information to verify.
Professor Grant | Under our department process, does this committee authorize the pilot once the vote is complete?
Professor Silva | No. The faculty board has [[decision authority::Decision authority identifies the body empowered to authorize implementation under the supplied fictional process.]] for implementation; this committee sends a recommendation under the local process.
Professor Grant | Then the minutes should not say the enrollment increase is approved for next term merely because this vote passes.
Professor Silva | Exactly. The [[meeting minutes::The meeting minutes should preserve the actual motion, conditions, and decision status rather than report an authorization that did not occur.]] need to record the amended wording and distinguish our recommendation from the board's eventual decision.
Professor Grant | The committee has voted for the amended proposal. I will tell colleagues it is a one-term pilot recommendation with conditions.
Professor Silva | Call it a [[conditional recommendation::A conditional recommendation retains the unresolved requirements and must not be shortened into an unconditional commitment.]], and keep staffing and room confirmation in the same sentence as the proposed increase.
Professor Grant | We can submit the recommendation after identifying the responsible contacts for those checks, without announcing a completed launch.
Professor Silva | Yes. [[Implementation approval::Implementation approval is the separate authorization needed before putting the change into operation, which the committee recommendation does not supply.]] remains pending until the faculty board actually makes that decision.
Professor Grant | If the pilot is approved, we should specify when the department evaluates workload and student participation.
Professor Silva | Include a [[review checkpoint::A review checkpoint defines when the trial will be assessed, keeping evaluation separate from an automatic promise of permanent continuation.]] in the proposal, so a limited trial does not quietly become a permanent change without the appropriate review.''',
    rehearsal=['Read the corrected meeting exchange and stress recommend, conditional, and approval pending.', 'Switch roles and deliver the minute entry using the supplied cap, duration, conditions, and decision authority.'],
    transfer_title='Submitted became approved', transfer_setup='The committee recommendation has been sent to the faculty board. The board has not yet decided. Staffing and room confirmation remain conditions of the proposal.',
    transfer='''Chair: "The recommendation has been ___." | submitted | Submission describes sending the proposal, not a completed board decision.
Member: "Implementation approval remains ___." | pending | The board has not yet made the required decision.
Chair: "Keep the resource ___ visible." | conditions | Staffing and room confirmation remain part of the proposed authorization.
Member: "We should not announce a confirmed ___." | launch | The supplied status does not establish authorization to begin implementation.'''))
