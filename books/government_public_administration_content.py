"""Original public-administration cases for the English Ladder learner book."""
from books.authoring import unit

BOOK = dict(
    slug='government-public-administration', title='Government and Public Administration English',
    cover_label='ENGLISH FOR PUBLIC SERVICE PROFESSIONALS',
    cover_title='Government and\nPublic Administration', cover_size=30,
    tagline='Explain the process clearly.\nMake public decisions understandable.',
    audience='For program officers, public-service staff, procurement teams, grant administrators, records staff, and interagency coordinators.',
    map_intro='Eight public-service conversations: distinguish a proposal from current guidance, manage a public meeting, explain a procurement evaluation, reconcile a grant report, assign an interagency handoff, repair a resident referral, review a records response, and connect spending to measurable outcomes.',
    notes_title='Clear service without unsupported promises',
    notes_intro='Public administration combines procedural accuracy with accessible explanations. These conversations practice explaining what a document means, what an office can do, who owns the next step, and what the evidence actually establishes.',
    field_notes=[
        ('Name the document and its status', 'A proposal, current guidance, application receipt, and formal decision do different jobs. Identify the relevant version and status before explaining its consequence.', '"That document is a proposal; the current application guidance has not changed."'),
        ('Explain the boundary and the route forward', 'A resident needs more than a statement that an issue belongs elsewhere. Name the responsible office, explain the referral, and confirm how the handoff will be tracked.', '"The permit team decides that issue; I will confirm that it has received your referral."'),
        ('Keep judgments traceable to evidence', 'A procurement conclusion, grant total, or performance claim should point to a defined criterion and supporting record. A confident label does not replace the reasoning.', '"Which published criterion does that strength address?"'),
        ('Respect participation and privacy together', 'Fair access to a process does not mean publishing every personal detail. Use the announced participation arrangements and the applicable information-handling rules.', '"We can record the issue without reading your personal details into the meeting record."'),
    ],
    scope_note='All programs, residents, offices, applications, figures, meetings, and local procedures are fictional. This is professional-English instruction, not legal advice or authority to decide eligibility, award contracts, release records, or spend funds. U.S. federal references support selected terminology; their rules do not automatically govern every local, state, tribal, or international office.',
    sources=[
        dict(title='Office of the Federal Register. A Guide to the Rulemaking Process.', url='https://uploads.federalregister.gov/uploads/2013/09/The-Rulemaking-Process.pdf', note='Background on proposals, public comments, and final rules. Fictional program conditions are not actual eligibility rules or a universal account of rulemaking.', checked='1 October 2026'),
        dict(title='Federal Acquisition Regulation 15.304. Evaluation factors and significant subfactors.', url='https://www.acquisition.gov/far/15.304', note='Background on disclosed evaluation factors and their importance in U.S. federal negotiated procurement. The invented scoring example is not a universal selection method.', checked='1 October 2026'),
        dict(title='Electronic Code of Federal Regulations. 2 CFR 200.302: Financial management.', url='https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-D/section-200.302', note='Background on federal-award financial records and source documentation. The fictional reporting categories and figures illustrate reconciliation language, not cost allowability decisions.', checked='1 October 2026'),
        dict(title='FOIA.gov. Frequently Asked Questions.', url='https://www.foia.gov/faq.html', note='Background on U.S. federal records requests, review, exemptions, and partial disclosure. The records dialogue does not determine an exemption or prescribe local-law procedures.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Policy Implementation and Program Rules',
    scene='The proposal has not changed the current application test',
    skill='Explain document status and a current requirement without confusing a preliminary check with a formal eligibility decision.',
    brief='The fictional Brookfield Training Grant currently requires 12 months of residence, plus other conditions. Published guidance G4 explains the current requirements. A separate proposal P2 would reduce the residence period to six months, but it has not been adopted and has no effective date. Resident Amina has lived in the area for nine months and brings P2 to the service desk. Program officer Theo must identify the current residence requirement, explain the proposal accurately, and avoid either promising an award or treating this conversation as a formal denial of an application.',
    cast='Amina | Resident\nTheo | Program information officer',
    culture=('Correct the document, not the person', 'A resident may reasonably assume that a published document describes the current service. Acknowledge why the documents look confusing, then show their status and identifiers. Explain the current process without implying that asking a question is itself an application or a final decision.'),
    a='''Which document explains the current requirements? | Guidance G4 | Proposal P2 | A future decision not yet issued | A resident's summary of P2 | G4 is identified as the published guidance explaining the current program requirements.
What does P2 propose? | Reducing the residence period to six months | Reducing it to nine months immediately | Awarding every submitted application | Removing all other conditions | P2 proposes a six-month residence period, but adoption and an effective date are absent.
What can Theo accurately say about nine months? | It is below the current 12-month residence condition. | It satisfies the current residence condition. | It establishes a complete formal eligibility decision. | It guarantees eligibility once P2 is discussed. | Nine months is shorter than the current residence condition, but the desk conversation is not a formal determination.''',
    vocabulary='''program rule | A requirement governing a defined public program. | explain the program rules
eligibility criterion | A condition used to decide whether an applicant qualifies. | verify an eligibility criterion
current guidance | Published explanatory material reflecting the presently applicable position. | consult current guidance
proposal | A suggested change that has not necessarily been adopted. | distinguish the proposal
draft guidance | Preliminary explanatory material not yet issued as the final version. | identify draft guidance
adoption | Formal acceptance of a proposed measure through the applicable process. | confirm adoption
effective date | The date a measure begins to apply under its terms. | check the effective date
implementation date | The planned or required start of operational delivery. | confirm the implementation date
transition provision | A rule addressing movement from an old arrangement to a new one. | check transition provisions
residence requirement | A condition concerning where or how long a person has lived. | explain the residence requirement
application intake | Receipt and initial handling of an application. | arrange application intake
completeness check | A check that required application information is present. | perform a completeness check
eligibility determination | An authorized decision about qualification under the applicable criteria. | issue an eligibility determination
supporting evidence | Documents or information used to substantiate a claim. | identify supporting evidence
verification | Checking information against appropriate evidence. | complete verification
exception | A defined departure from a general requirement where permitted. | check an authorized exception
discretion | Authorized judgment within the limits of a rule or role. | exercise defined discretion
statutory authority | Power granted by legislation. | identify statutory authority
rulemaking | The process of developing and issuing regulations. | follow the rulemaking process
public comment | Input submitted through an announced public consultation process. | submit public comment
comment deadline | The closing time for input under a specified process. | verify the comment deadline
notice | An official communication about a process, action, or decision. | read the notice
superseded version | A document version replaced by a later applicable version. | identify a superseded version
case-specific advice | Guidance tailored to a person's facts within the provider's authority. | seek case-specific advice''',
    precision='A proposal may be public without being in effect. A publication date does not necessarily establish adoption or applicability. Here G4 describes the current condition, while P2 remains an unadopted proposal with no effective date.',
    precision_extra='A residence condition is one part of eligibility, not the whole decision. Explaining that nine months is below twelve does not itself issue a formal denial. Use the actual intake and decision processes, and do not invent an exception or future entitlement.',
    phrases='''Acknowledge the confusion | I can see why these two documents are easy to confuse.
Identify the current source | G4 explains the requirements that currently apply.
Name the proposal | P2 is a proposed change, not an adopted rule.
State the current condition | The current residence requirement is twelve months.
State the proposed change | The proposal would reduce that period to six months.
Qualify the future | No effective date has been established for P2.
Apply the stated comparison | Nine months is below the current residence requirement.
Keep the decision boundary | This explanation is not a formal eligibility determination.
Avoid a guarantee | I cannot promise an award based on the proposal.
Preserve other criteria | The program also has other conditions to assess.
Ask about the source | Which document and version are you reading?
Explain the process | I can show you the current application and review steps.
Check for authority | We should not invent an exception that the rules do not provide.
Separate participation | A comment on the proposal is not a grant application.
Point to the notice | The official notice explains how to submit comments.
Close with a clear distinction | Use G4 for the current requirements and P2 for the proposed change.''',
    notes='''Currently apply | Identifies the present position rather than a possible future one.
Would reduce | Describes the effect of a proposal without claiming adoption.
No effective date | Prevents readers from inventing when a change begins.
Not a formal | Preserves the boundary between information and an authorized decision.
Also has | Prevents one criterion from being mistaken for the entire test.
A comment ... not an application | Distinguishes two public processes with different purposes.''',
    d='''Which explanation is accurate? | P2 proposes six months; G4 still describes the current twelve-month condition. | P2's publication immediately replaced G4. | Nine months qualifies because it lies between six and twelve. | P2 has already removed the other criteria. | The accurate explanation preserves both document status and the current versus proposed periods.
Which response avoids an unauthorized decision? | Nine months is below the current condition; I can explain the formal review process. | This conversation is your final denial notice. | I approve the award under the future rule. | I will create an exception because the proposal seems likely. | The response explains the stated condition without issuing a decision or inventing authority.
What should Theo check before describing a change as operative? | Its adoption, applicable terms, and effective date | Its publication date and consultation deadline only | Whether the application website links to the proposal | Whether the proposal has completed its comment period | Publication, a website link, or the end of consultation alone does not make the proposal operative; adoption and applicability must be checked.
Which statement keeps the processes distinct? | Commenting on P2 does not itself submit an application for the grant. | Every comment automatically becomes an application. | Asking about G4 waives the right to apply. | Application intake guarantees an award. | Consultation input and a program application have different purposes and must not be conflated.''',
    dialogue='''Amina | This came from your grant page. It says six months of residence, and I have been here nine. Have I been using the wrong application guidance?
Theo | Let us check the [[proposal::Proposal identifies P2 as a suggested change, not an adopted replacement for the current program condition.]] you are holding. This is P2, which suggests a change. G4 is the guidance describing the requirements that currently apply.
Amina | Both files look official. I took the shorter period to mean the rules had changed. Nothing on this printout explains the difference to me.
Theo | I understand the confusion. The [[current guidance::Current guidance is G4, the identified explanation of the presently applicable program requirements.]] still describes a twelve-month residence requirement. P2 would reduce that to six months, but the proposal has not been adopted.
Amina | Does the date at the top of P2 mean the shorter period started then?
Theo | That is the publication date, not an [[effective date::Effective date identifies when a measure applies; P2 has no such date because the proposed change is not adopted.]]. No effective date has been established for this proposal. We should not tell applicants that the six-month condition already applies.
Amina | So my nine months does not meet the condition you are using at the moment?
Theo | It is below the current [[residence requirement::Residence requirement is the stated twelve-month condition; nine months is below it without resolving every other eligibility question.]] of twelve months. That explains this particular condition, but it is not a formal decision on an application or a complete assessment of your circumstances.
Amina | I do not want a question at the desk to be recorded as a final rejection. I am trying to understand the process.
Theo | This is not an [[eligibility determination::Eligibility determination is an authorized qualification decision, which this information conversation does not issue.]]. I can show you the actual application and review steps, including where to obtain case-specific information within the program's process.
Amina | Are there other conditions beyond residence? The proposal headline makes the program sound much simpler.
Theo | Yes. Residence is one [[eligibility criterion::Eligibility criterion is one condition within the program's test; meeting it alone would not establish entitlement to an award.]], not the entire test. The current guidance lists the other requirements, and an award should not be promised from one headline.
Amina | If the proposal is adopted later, should I assume it will apply to every application already on file?
Theo | We would need to read any [[transition provision::Transition provision governs movement between arrangements; future application treatment cannot be invented before the adopted terms are known.]] in the adopted measure. We cannot invent how pending applications would be handled before the actual terms and dates are available.
Amina | I would like to support the change. Is submitting a comment the same as asking to receive the grant?
Theo | No. A [[public comment::Public comment contributes to consultation on the proposal; it is separate from applying for an individual program benefit.]] concerns the proposal. It does not itself submit a grant application. The official notice explains the comment route and the deadline for that process.
Amina | Then I should keep the two documents separate and not rely on the proposed six-month period for the current requirements.
Theo | Exactly. Check the [[adoption::Adoption is formal acceptance through the applicable process; publication of a proposal alone does not establish it.]] status before treating a change as operative. Until then, use G4 for the current program explanation and P2 for the suggested change.
Amina | Thank you. Please show me where the current application steps are, and I will read the proposal notice separately.
Theo | I will. The [[application intake::Application intake is the process of receiving a program application, distinct from giving information or collecting consultation comments.]] information will explain what to submit and how the review proceeds. Today's explanation neither guarantees an award nor substitutes for that formal process.''',
    rehearsal=('Read turns 1-8 in pairs, stressing proposal, current, and publication date.', 'Swap roles for turns 9-20, keeping an eligibility explanation separate from a formal decision.', 'Complete the H3 exchange below and check every answer before reading it aloud.'),
    transfer_title='Distinguish another current condition',
    transfer_setup='Guidance H3 states an eight-month residence condition. Proposal Q1 would reduce it to four months but is not adopted. Resident Jo has six months of residence. No formal application decision has been made.',
    transfer='''Officer: "The current guidance is ___." | H3 | H3 is explicitly identified as the document stating the presently applicable condition.
Resident: "The current residence condition is ___." | eight months | Eight months is current; four months belongs to the unadopted proposal.
Officer: "The proposal's status is ___." | not adopted | Q1 has not been adopted, so its proposed period cannot replace the current condition.
Resident: "A formal application decision has ___." | not been made | The record expressly says that no formal determination has been issued.''',
))

BOOK['units'].append(unit(
    title='Public Meetings and Stakeholder Input',
    scene='Give the next speaker a fair turn',
    skill='Apply an announced participation process consistently while acknowledging disagreement and preserving the public record.',
    brief='A fictional town consultation has announced three minutes per speaker, one initial turn each before second turns, and written submissions accepted until Friday at 17:00 local time. Two speakers have already used their initial turns and ask to speak again while five registered speakers remain unheard. Facilitator Rosa and meeting clerk Ian must continue the queue consistently, regardless of whether a speaker supports or opposes the proposal. The meeting gathers input; it is not an up-or-down public vote. Any accessibility request should be handled through the stated meeting arrangements rather than dismissed as an attempt to gain extra influence.',
    cast='Rosa | Meeting facilitator\nIan | Meeting clerk',
    culture=('Be firm about process and neutral about viewpoint', 'A public disagreement may be strongly expressed without justifying unequal access to the microphone. Refer to the announced turn-taking process, acknowledge the contribution, and explain the next opportunity. Keep procedural decisions separate from agreement with the speaker.'),
    a='''Who should be called next under the announced process? | The next registered speaker who has not had an initial turn | Either repeat speaker before the waiting group | Only a speaker supporting the proposal | Whoever speaks most loudly | Five registered speakers remain unheard, and the announced process gives initial turns before second turns.
What is the written-submission deadline? | Friday at 17:00 local time | Immediately after each speaker's turn | Monday at 09:00 | An unannounced time chosen after the meeting | The brief expressly states the Friday local-time deadline for written input.
What is this meeting's purpose? | To gather input, not decide the proposal by a public vote | To award a contract immediately | To count applause as a binding ballot | To approve every speaker's request | The stated consultation purpose is collecting input rather than holding an up-or-down vote.''',
    vocabulary='''consultation | A process of seeking input before or during decision development. | conduct a consultation
stakeholder | A person or group affected by or interested in an issue. | hear from stakeholders
facilitator | A person guiding a discussion and its agreed process. | support the facilitator
meeting clerk | The person maintaining meeting records and administrative arrangements. | brief the meeting clerk
agenda | The planned sequence of meeting business. | follow the agenda
speaker queue | The ordered list of people waiting to speak. | manage the speaker queue
speaking allocation | The time or opportunity assigned to a speaker. | explain the speaking allocation
initial turn | A person's first opportunity to speak in the relevant round. | complete initial turns
second turn | A later speaking opportunity after an initial contribution. | allow second turns
time limit | The stated maximum duration of an activity or contribution. | apply the time limit
procedural reminder | A statement recalling the process currently being followed. | give a procedural reminder
viewpoint neutrality | Consistent treatment without favoring a position on the issue. | maintain viewpoint neutrality
oral submission | Input delivered by speaking. | record an oral submission
written submission | Input provided in written form. | accept written submissions
submission deadline | The final time for receiving input under the process. | state the submission deadline
meeting record | Documentation of the meeting and its relevant proceedings. | maintain the meeting record
attribution | Identification of the source of a statement. | check attribution
summary | A condensed account preserving the relevant meaning. | verify the summary
clarification | An explanation resolving ambiguity in a statement or process. | request clarification
accessibility arrangement | A measure supporting participation by people with access needs. | coordinate accessibility arrangements
interpretation | Spoken or signed language conversion supporting understanding. | arrange interpretation
accommodation request | A request for an adjustment to support access or participation. | handle an accommodation request
deliberation | Structured examination of issues before a decision. | distinguish input from deliberation
decision authority | The person or body empowered to make the relevant decision. | identify the decision authority''',
    precision='A consultation can collect evidence, experiences, and arguments without being a referendum. Do not describe applause, speaker counts, or the most forceful contribution as a binding vote when the announced process gives decision authority elsewhere.',
    precision_extra='Consistent turn-taking does not mean ignoring accessibility arrangements. Handle access requests through the stated process, and explain any authorized adjustment without judging the speaker\'s viewpoint. Acknowledge a contribution without implying endorsement of its substance.',
    phrases='''Acknowledge the contribution | Thank you; your concern has been recorded.
Recall the process | We announced one initial turn each before second turns.
Name the waiting group | Five registered speakers have not yet been heard.
Move the queue | I will now call the next person awaiting an initial turn.
Apply the time limit | The speaking allocation is three minutes.
Separate viewpoint | The same process applies to support and opposition.
Avoid a personal rebuke | I am applying the turn-taking process, not judging your position.
Offer the stated route | Written submissions remain open until Friday at 17:00 local time.
Clarify the meeting purpose | This consultation gathers input; it is not a public ballot.
Check the record | Does that summary accurately capture the point you made?
Preserve attribution | Please identify that as the speaker's claim, not a verified finding.
Handle access needs | Let us use the announced accessibility arrangements for that request.
Avoid an invented promise | I cannot guarantee a second turn before the remaining initial speakers.
Explain decision authority | The designated body will make the decision through its stated process.
Close the oral session | The meeting record will preserve the contributions received.
Restate the next step | We will explain how the input proceeds to the decision stage.''',
    notes='''Has been recorded | Acknowledges receipt without endorsing the claim.
Before second turns | States the priority rule that controls the next action.
Same process | Makes consistent treatment explicit.
Not judging your position | Separates procedure from agreement or disagreement.
Accurately capture | Checks the meaning of a summary with its source.
Speaker's claim | Preserves attribution instead of presenting an allegation as an official finding.''',
    d='''Which intervention best follows the process? | Thank you; we will hear the remaining initial speakers before returning to second turns. | We will let supporters speak twice before opponents speak once. | The loudest speaker can choose the queue. | All remaining speakers lose their turns because time is tight. | The intervention applies the announced priority without favoring a viewpoint or canceling unheard contributions.
Which record entry is appropriately attributed? | A speaker reported concerns about evening access. | Evening access is proven inadequate because one speaker said so. | The entire community unanimously opposes the proposal. | Every concern is an official finding. | Attribution preserves the reported concern without converting one contribution into verified or universal evidence.
How should an access request be handled? | Through the announced accessibility arrangements | By applying an identical format without checking an adjustment | By counting the request as the person's initial contribution | By postponing all access arrangements until written consultation | Consistent treatment includes the stated access process; identical format, counting the request as a contribution, or delaying support may prevent participation.
Which explanation correctly describes the meeting? | It gathers input for the designated decision process. | Applause determines the binding result. | The two longest speakers decide the outcome. | Every written submission guarantees adoption of its request. | The consultation collects input but does not transfer decision authority to applause or individual submissions.''',
    dialogue='''Rosa | Before I reopen the floor, can you check the queue? The two people asking to come back have both spoken, and I can see others still waiting.
Ian | Five people are waiting for an [[initial turn::Initial turn is the first speaking opportunity, which the announced process gives priority over repeat contributions.]]. The two asking to return have already used theirs. We announced that everyone gets that first opportunity before we move to second turns.
Rosa | I heard their concerns. Now I need to move the meeting on without making it sound as though disagreement costs someone a turn.
Ian | Use a [[procedural reminder::Procedural reminder restates the announced turn-taking rule without criticizing the substance or intensity of a contribution.]]. Thank them, confirm that their points were recorded, and explain that the next registered person who has not spoken will now be called.
Rosa | One supports the proposal and the other opposes it. We need to make clear that this is not about either position.
Ian | That is [[viewpoint neutrality::Viewpoint neutrality applies the participation process consistently to supporters and opponents rather than favoring a position.]]. Apply the same initial-turn rule and the same announced three-minute allocation. The explanation should focus on process, not agreement with their arguments.
Rosa | Could we promise them another opportunity at the end, so they are less frustrated now?
Ian | We can explain the possibility of a [[second turn::Second turn is a later opportunity after initial contributions; it should not be guaranteed before the announced priority is met.]], but not guarantee it before the remaining initial speakers. We also have the written-submission route that was announced at the start.
Rosa | Please remind me of the exact deadline. I do not want to give two different times in the same meeting.
Ian | The [[submission deadline::Submission deadline is Friday at 17:00 local time, the announced cutoff for written input in this fictional meeting.]] is Friday at 17:00 local time. We should repeat the same time and submission instructions so that people can use that route reliably.
Rosa | One resident asked whether the amount of applause will determine the result. We should correct that before the next speaker.
Ian | Yes. This [[consultation::Consultation gathers input for a decision process; applause and speaker counts are not a binding public ballot here.]] gathers input. It is not an up-or-down vote, and applause does not replace the designated decision process or establish what everyone in the town thinks.
Rosa | The clerk's summary says that residents cannot reach the site in the evening. Only one person has made that claim so far.
Ian | Keep the [[attribution::Attribution identifies the speaker as the source, avoiding conversion of an individual report into a verified community-wide finding.]]. Record that a speaker reported an evening-access concern. We can preserve the point without turning it into a verified finding about every resident.
Rosa | Another participant has asked for an adjustment so they can follow and contribute to the discussion. How should I respond?
Ian | Use the announced [[accessibility arrangement::Accessibility arrangement supports participation through the stated process; it should not be dismissed as a viewpoint-based request for influence.]] process. Do not treat the request as an attempt to gain influence. Check the appropriate adjustment and communicate it clearly without disclosing unnecessary personal details.
Rosa | I will call the next initial speaker, restate the allocation, and explain that the written route remains available.
Ian | I will update the [[meeting record::Meeting record preserves the contributions and procedural actions so the later decision process has an accurate account.]] and check that summaries retain their meaning. Recording a concern does not mean the office endorses it, but it should not be lost.
Rosa | Before closing, we also need to say who makes the decision and where people can find the next-stage information.
Ian | Agreed. Name the [[decision authority::Decision authority identifies the body empowered to decide, separating receipt of public input from approval of the proposal.]] and the stated next steps. That gives participants a useful account of how their input moves forward without promising that every requested change will be adopted.''',
    rehearsal=('Read turns 1-10 with a calm, firm procedural reminder.', 'Swap roles for turns 11-20; stress the difference between a reported concern and an official finding.', 'Complete the second meeting exchange and read back its allocation, queue, deadline, and purpose.'),
    transfer_title='Apply another meeting process',
    transfer_setup='A meeting allows two minutes per initial speaker before repeat turns. Three registered people remain unheard. Written input closes Wednesday at 12:00 local time. The session is consultation, not a ballot.',
    transfer='''Chair: "The initial speaking allocation is ___." | two minutes | The announced process assigns two minutes to each initial contribution.
Clerk: "The number of registered people still unheard is ___." | three | Three people remain entitled to the next initial turns under the stated process.
Chair: "Written input closes ___." | Wednesday at 12:00 local time | The deadline includes the day, time, and local-time reference from the announcement.
Clerk: "The session is a ___." | consultation | The session gathers input rather than determining the outcome through a public ballot.''',
))


BOOK['units'].append(unit(
    title='Procurement and Vendor Selection',
    scene='Best value needs a reason, not just a label',
    skill='Connect a procurement recommendation to published criteria, comparable evidence, and an authorized decision process.',
    brief='A fictional office evaluates two service proposals using published maximum scores: technical approach 50, service delivery 30, and price 20. Recorded weighted scores are A: 45, 25, 16, total 86; B: 40, 24, 18, total 82. A costs $120,000 and B costs $110,000. The method permits a documented trade-off, but the draft note only says A is best value. Evaluator Dev and procurement officer Marta must explain the scored differences and the $10,000 premium. A vendor\'s local address is not a published criterion. The award has not been authorized.',
    cast='Dev | Technical evaluator\nMarta | Procurement officer',
    culture=('Challenge the rationale without reopening the rules', 'A request to explain an evaluation is not necessarily an accusation of bias. Link the judgment to the announced criteria and the submitted evidence. Do not quietly introduce a new preference after seeing which supplier it would favor.'),
    a='''What are the recorded totals? | A has 86 and B has 82. | A has 82 and B has 86. | Both have 90. | A has 45 and B has 40 overall. | Adding the three recorded weighted scores produces totals of eighty-six and eighty-two.
What is A's price premium? | $10,000 | $4,000 | $16,000 | $30,000 | A's price of one hundred twenty thousand exceeds B's one hundred ten thousand by ten thousand.
Which consideration is not a published criterion? | The vendor's local address | Technical approach | Service delivery | Price | The brief lists three published factors and expressly excludes local address as a criterion.''',
    vocabulary='''procurement | The process of obtaining goods or services under applicable rules. | manage procurement
solicitation | A formal request inviting offers under stated requirements. | review the solicitation
offeror | A supplier submitting an offer in response to a solicitation. | evaluate the offeror
evaluation factor | A stated dimension used to assess proposals. | apply the evaluation factors
subfactor | A defined component of a broader evaluation factor. | assess the subfactor
relative importance | The stated relationship in significance among evaluation factors. | state relative importance
weighted score | A score already adjusted to reflect the specified scoring importance. | verify the weighted scores
scoring matrix | A structured record of scores against criteria. | reconcile the scoring matrix
technical approach | The proposed method for delivering the required work. | evaluate the technical approach
service-delivery plan | The proposed arrangement for providing the required service. | assess the service-delivery plan
price premium | The amount by which one price exceeds another. | justify the price premium
best value | The most advantageous result under the applicable selection method. | explain the best-value judgment
trade-off | A comparison accepting one disadvantage for a supported benefit. | document the trade-off
strength | An assessed favorable feature under an evaluation criterion. | substantiate a strength
weakness | An assessed unfavorable feature under an evaluation criterion. | document a weakness
deficiency | A material failure to meet a stated requirement under the applicable method. | identify a deficiency
past performance | Evidence of how a supplier performed on relevant previous work. | assess past performance
evaluation narrative | Written reasoning supporting the recorded assessment. | complete the evaluation narrative
source selection | The process of choosing a supplier under the applicable procedure. | support source selection
award authority | The person or body empowered to authorize the contract award. | confirm award authority
conflict of interest | An interest that may improperly influence, or appear to influence, official judgment. | disclose a conflict of interest
recusal | Withdrawal from a matter under the applicable conflict-handling process. | arrange recusal
audit trail | Records allowing a decision or transaction to be traced. | preserve the audit trail
debriefing | A structured explanation of a procurement outcome under applicable procedures. | prepare a debriefing''',
    precision='The scores are already weighted. Do not apply the 50/30/20 maxima a second time. The totals are 86 and 82. A higher score is relevant under this method, but the permitted trade-off still needs a reasoned record of the benefits and premium.',
    precision_extra='Best value is a conclusion under a specified selection method, not a synonym for lowest price or local supplier. Link each claimed strength to a published factor and proposal evidence. An evaluation recommendation is not the same as an authorized award.',
    phrases='''Ask for the rationale | What does best value mean under this selection method?
Return to the criteria | Let us use the published evaluation factors.
Check the arithmetic | The weighted scores total eighty-six for A and eighty-two for B.
Avoid double weighting | These scores have already been weighted.
Name the price difference | A carries a ten-thousand-dollar premium.
Identify the strength | Which submitted feature supports the technical advantage?
Link evidence to judgment | Cite the proposal evidence beside the relevant criterion.
Explain the trade-off | The note must explain why the assessed benefit justifies the premium.
Reject an added preference | Local address is not a published criterion.
Preserve equal treatment | Apply the same evidence standard to both offers.
Clarify the status | This is an evaluation recommendation, not an award.
Check authority | The designated award authority still needs to decide.
Handle a conflict | Any relevant interest should go through the conflict-review process.
Avoid score-only reasoning | The total does not replace the evaluation narrative.
Keep the record reviewable | A reader should be able to trace each conclusion to its evidence.
Close the revision | Revise the rationale without changing the published method.''',
    notes='''Under this method | Limits the conclusion to the actual procurement procedure.
Already weighted | Prevents a second adjustment that would distort the scores.
Supports the advantage | Requests evidence for a comparative judgment.
Justifies the premium | Connects a benefit to the additional cost rather than ignoring price.
Not a published criterion | Identifies an impermissible addition under the stated process.
Recommendation, not an award | Separates the evaluation team's work from final authorization.''',
    d='''Which evaluation note is strongest? | Link A's scored strengths to proposal evidence and explain the $10,000 premium. | State best value without further detail. | Add local address as a deciding factor after scoring. | Ignore price because A has the higher total. | The strongest note connects the comparative benefits, evidence, and cost under the published method.
What should happen to the existing weighted scores? | Check their arithmetic without applying the weights again. | Multiply each one by its factor maximum again. | Replace the price scores with the dollar figures. | Average only the two highest factors. | The scores are already weighted, so a second weighting would distort the recorded method.
Which statement preserves authority? | The evaluation recommends A; the award decision remains pending. | The evaluator's preference alone executes the contract. | A's local address automatically authorizes the award. | A four-point lead removes every approval requirement. | The brief gives the evaluation team a recommendation role while award authorization remains outstanding.
Which challenge is appropriate? | Which published factor and submitted evidence support that claimed strength? | Can we add a factor that favors the supplier we prefer? | Should we remove B's stronger price score? | Can we replace the method with a personal impression? | The challenge tests the rationale within the stated rules instead of changing them to fit a desired result.''',
    dialogue='''Marta | I can check the totals, but I cannot sign this rationale yet. Best value is doing a lot of work in the draft. Show me what sits behind it.
Dev | The [[scoring matrix::Scoring matrix records each proposal's assessment against the stated factors, allowing the totals and differences to be checked.]] gives A forty-five for technical approach, twenty-five for service delivery, and sixteen for price. B has forty, twenty-four, and eighteen respectively.
Marta | That gives eighty-six and eighty-two. Are those raw marks that still need the fifty, thirty, and twenty weighting applied?
Dev | No, each [[weighted score::Weighted score already incorporates the specified importance; applying the weights again would change the method and distort the totals.]] is final for that factor. We should check the addition, but applying the weights again would change the evaluation rather than verify it.
Marta | A is also ten thousand dollars more expensive. The note cannot simply report the higher total and leave that difference unexplained.
Dev | Agreed. The [[price premium::Price premium is the ten-thousand-dollar difference between the two quoted prices, which the trade-off reasoning must address.]] is part of the decision. A costs one hundred twenty thousand, while B costs one hundred ten thousand. Our method permits a documented trade-off.
Marta | Which features support the technical difference? A reader should not have to infer a benefit from the score alone.
Dev | I need to expand the [[evaluation narrative::Evaluation narrative supplies the reasons and evidence behind scores rather than relying on a numerical total alone.]]. Each assessed strength should point to the submitted material and the technical factor it addresses, rather than a general impression that A seems better.
Marta | Someone suggested mentioning that A's office is local. Does the solicitation give us a factor for that?
Dev | No. It is not an [[evaluation factor::Evaluation factor is a published assessment dimension; local address is not one of the stated criteria here.]], so we should not add it now. The published dimensions are technical approach, service delivery, and price, with the stated relative importance.
Marta | We also need to show that B's stronger price result was recognized, not quietly removed because the team prefers A.
Dev | The [[trade-off::Trade-off compares the assessed benefits with the additional cost under the permitted method, retaining both favorable and unfavorable evidence.]] explanation should do that. It must explain why the evidenced benefits of A are judged worth the premium, if that remains the supported recommendation.
Marta | Is a four-point lead sufficient by itself? The summary says highest score therefore award, which skips the trade-off we have just discussed.
Dev | No. [[Best value::Best value is the most advantageous result under the applicable selection method, not a universal consequence of a score or price.]] depends on this selection method and a defensible record. We should not present our scoring example as a rule for every procurement.
Marta | Before circulation, check that any interests affecting an evaluator have gone through the proper disclosure process.
Dev | I will confirm the [[conflict of interest::Conflict of interest concerns an interest that could influence official judgment; it requires the applicable disclosure and review process.]] review status. That belongs in the appropriate record, without turning an unsupported suspicion about a colleague into an allegation in the evaluation note.
Marta | Once the explanation is complete, who actually authorizes the contract award? The draft sounds as though the evaluation team already has.
Dev | The designated [[award authority::Award authority is the empowered decision-maker; the evaluation team's recommendation does not itself authorize or execute an award.]] still needs to decide. I will label the document as our recommendation and remove wording that suggests an award has already been made.
Marta | Good. Keep the published criteria, the verified totals, the evidence, and the premium visible in the revised note.
Dev | I will preserve that [[audit trail::Audit trail links the conclusion to the criteria, evidence, arithmetic, and approvals, allowing later review of the decision.]]. The revision will explain the recommendation under the existing method, not introduce a new preference to make the result easier to defend.''',
    rehearsal=('Read turns 1-8, saying each factor score and total clearly.', 'Swap roles for turns 9-20, stressing published factors and recommendation rather than award.', 'Complete the C-and-D comparison; verify the totals and premium before reading the result aloud.'),
    transfer_title='Explain another scored comparison',
    transfer_setup='Under a stated trade-off method, C has already-weighted scores of 42, 26, and 17. D has 40, 25, and 19. C costs $75,000 and D $70,000. Award approval is pending.',
    transfer='''Evaluator: "C's total weighted score is ___." | 85 | Forty-two plus twenty-six plus seventeen equals eighty-five without applying weights again.
Officer: "D's total weighted score is ___." | 84 | Forty plus twenty-five plus nineteen equals eighty-four under the supplied scoring record.
Evaluator: "C's price premium is ___." | $5,000 | Seventy-five thousand minus seventy thousand gives a five-thousand-dollar premium.
Officer: "The award status is ___." | approval pending | The stated approval has not occurred, so a score comparison does not itself award the contract.''',
))

BOOK['units'].append(unit(
    title='Grants, Compliance, and Reporting',
    scene='The total matches the spreadsheet, not the evidence',
    skill='Reconcile expenditure categories to supporting records and explain an unresolved difference without inventing a balancing entry.',
    brief='Grant G62 reports $48,000 spent in the quarter: personnel $30,000, materials $12,000, and travel $6,000. The reporting instructions request these categories and supporting records. The currently assembled records support personnel $29,000, materials $12,000, and travel $6,000, totaling $47,000. One $1,000 personnel item lacks the requested supporting record. Grant officer Sana and finance coordinator Owen must flag the evidence gap, seek the missing record, and follow the actual correction and submission process. The difference alone does not establish fraud, allowability, or authority to move the amount into another category.',
    cast='Sana | Grant officer\nOwen | Finance coordinator',
    culture=('Use neutral discrepancy language', 'A missing record may lead to several possible explanations. State the amount, category, and evidence gap without accusing a colleague or making the problem disappear. A clear reconciliation lets the responsible reviewer decide what needs correction or further support.'),
    a='''What total do the assembled supporting records substantiate? | $47,000 | $48,000 | $46,000 | $30,000 | Twenty-nine thousand plus twelve thousand plus six thousand equals forty-seven thousand.
Where is the evidence gap? | A $1,000 personnel item | All travel costs | A $12,000 materials item | An unexplained $6,000 surplus | The personnel report exceeds the assembled personnel support by one thousand dollars.
What conclusion is not established by the difference alone? | Fraud or cost allowability | A need to reconcile the report | A personnel documentation gap | A difference between reported and supported totals | The discrepancy identifies missing support but does not determine intent or whether the cost is allowable.''',
    vocabulary='''grant award | Funding provided under specified terms for an approved purpose. | identify the grant award
recipient | The entity receiving an award directly from the awarding body. | identify the recipient
subrecipient | An entity carrying out part of an award under a subaward. | monitor the subrecipient
pass-through entity | An entity providing a subaward from funding it has received. | contact the pass-through entity
award terms | The conditions governing a particular funding award. | review the award terms
reporting period | The time interval covered by a report. | confirm the reporting period
expenditure | An amount spent or recognized as spent under the applicable basis. | report expenditures
budget category | A defined grouping of planned or reported costs. | reconcile budget categories
personnel cost | Cost associated with staff work under the applicable accounting rules. | document personnel costs
source documentation | Original or supporting records substantiating a transaction. | obtain source documentation
supporting schedule | A detailed breakdown supporting a reported figure. | prepare a supporting schedule
general ledger | The main accounting record organizing transactions by account. | reconcile the general ledger
reconciliation | Comparison of records to identify and explain differences. | complete the reconciliation
variance | A difference between compared figures or positions. | explain the variance
unsupported item | An item lacking the evidence required for the stated review. | flag an unsupported item
allowable cost | A cost permitted under the applicable rules and award terms. | assess cost allowability
allocable cost | A cost assignable to an activity under the applicable benefit relationship. | assess cost allocability
cost share | The portion of project costs met from sources specified outside the award funding. | document cost share
indirect cost | A cost supporting multiple activities rather than one readily identified objective. | review indirect costs
obligation | A commitment creating a requirement to pay under the applicable definition. | distinguish obligations from expenditures
unobligated balance | Funds not committed through obligations under the applicable accounting basis. | report the unobligated balance
certification | An authorized attestation about specified information or compliance. | review the certification
corrected report | A revised submission fixing identified reporting errors. | submit a corrected report
closeout | The process of completing award-end administrative and financial requirements. | prepare for closeout''',
    precision='A reported total can add correctly while its supporting evidence remains incomplete. Here the category figures total $48,000, but the assembled support totals $47,000. The discrepancy is specifically a $1,000 personnel item, not a general arithmetic error.',
    precision_extra='Documented does not automatically mean allowable, and unsupported does not automatically mean fraudulent. Obtain the required evidence and follow the actual review process. Do not move a cost between categories merely to make the report appear balanced.',
    phrases='''Identify the award | We are reconciling the quarterly report for G62.
State the reported total | The report shows forty-eight thousand dollars.
State the supported total | The assembled records support forty-seven thousand dollars.
Locate the difference | The one-thousand-dollar gap is in personnel.
Separate arithmetic from evidence | The categories add correctly, but the supporting record is incomplete.
Request the missing record | Please locate the record for that specific personnel item.
Avoid an accusation | The gap does not by itself establish fraud.
Preserve the classification | Do not move the amount into travel just to balance the report.
Check the reporting basis | Are these figures for the same award, period, and accounting basis?
Qualify allowability | Supporting documentation does not alone settle cost allowability.
Keep the gap visible | Mark the item as unresolved in the reconciliation.
Ask about correction | What does the applicable process require before submission?
Avoid false certification | We should not certify completeness while this required support is missing.
Assign the follow-up | Owen will trace the item and return the evidence status.
Retain the record | Keep the original figures and any authorized correction traceable.
Close the review | The final report should match the approved treatment and supporting records.''',
    notes='''Support | Describes what the evidence substantiates, not merely what a spreadsheet states.
In personnel | Locates the discrepancy in a specific category.
Does not by itself | Limits a conclusion to what the evidence actually establishes.
Just to balance | Identifies an improper reason for changing classification.
Same award, period, and basis | Makes the reconciliation compare like with like.
Any authorized correction | Preserves the distinction between finding an issue and deciding its treatment.''',
    d='''Which reconciliation statement is correct? | Reported expenditure is $48,000; assembled support is $47,000, with $1,000 unresolved in personnel. | Both reported and supported expenditure are $48,000. | Travel is short by $1,000. | The report has a $1,000 addition error. | The category sum is correct, but one personnel item lacks its requested supporting record.
What should Owen do first with the specific gap? | Trace the personnel item and seek the missing support. | Add $1,000 to travel without evidence. | Delete the item silently from every record. | Declare fraud before investigating. | Tracing the identified item addresses the actual evidence gap without inventing treatment or intent.
Which statement about allowability is sound? | It requires review under the applicable rules and award terms. | Every ledger entry is automatically allowable. | Missing support proves the cost is forbidden in every program. | A balanced spreadsheet alone establishes allowability. | Evidence and correct arithmetic matter, but cost allowability also depends on the governing requirements.
What should a correction preserve? | A traceable record of the original figure, reason, approval, and revised treatment | Only the final number with no explanation | A different category chosen to hide the gap | An unsupported completeness certification | A documented correction lets reviewers understand what changed, why, and under whose authority.''',
    dialogue='''Sana | I cannot tie G62 to the evidence folder. The report says forty-eight thousand; I can support forty-seven. Can we work through the category totals together?
Owen | The [[supporting schedule::Supporting schedule breaks down the total into categories so the reported amount can be compared with the corresponding evidence.]] shows thirty thousand for personnel, twelve thousand for materials, and six thousand for travel. Those figures add correctly to the reported total.
Sana | The records I have show twenty-nine thousand for personnel. Materials and travel match the schedule. Is there another personnel record somewhere?
Owen | We are missing [[source documentation::Source documentation substantiates the transaction; the requested record for one personnel item is absent from the assembled evidence.]] for one thousand dollars in that category. I need to trace the specific item rather than assume it belongs in the folder.
Sana | Then the issue is not that the spreadsheet added the categories incorrectly. It is that the evidence does not yet support every reported item.
Owen | Correct. The [[reconciliation::Reconciliation compares the report with supporting records and identifies the precise difference rather than concealing it in the total.]] should show forty-eight thousand reported, forty-seven thousand supported, and one thousand unresolved in personnel. That is the clearest description of the current position.
Sana | Someone suggested moving the thousand into travel because that category has room in the budget. That would make the report look less awkward.
Owen | Available budget does not determine the [[budget category::Budget category should reflect the transaction's proper classification, not a convenient place to hide an unsupported amount.]] of an actual transaction. We should not reclassify the item simply to remove the visible gap. The treatment needs evidence and the proper review.
Sana | The draft issue note calls it fraud. All we know so far is that the record is missing. I want the wording to reflect that distinction.
Owen | Call it an [[unsupported item::Unsupported item accurately describes the missing required evidence without asserting fraudulent intent or a final cost decision.]] at this stage. Missing support does not by itself establish intent. We can state exactly what is absent and what we are doing to obtain it.
Sana | If you find the record, does that automatically settle whether the grant can pay for the cost?
Owen | No. [[Allowable cost::Allowable cost depends on the governing rules and award terms; finding a record alone does not decide that status.]] status depends on the applicable rules and award terms as well. The record supports the transaction; the reviewer still needs the relevant basis for charging it to the award.
Sana | Before comparing the figures again, please confirm that we are using the same quarter and the same accounting basis.
Owen | I will check the [[reporting period::Reporting period defines the interval covered by the report; mismatched periods can create misleading differences in a reconciliation.]] and the award reference. We should not reconcile a current-quarter total against a folder containing a different period and then explain the wrong discrepancy.
Sana | The submission includes a completeness certification. I do not want us to sign it while ignoring a required missing record.
Owen | We should flag that before [[certification::Certification is an authorized attestation; an unresolved required evidence gap must not be hidden when completeness is attested.]]. I will return the evidence status and ask what the actual correction and submission process requires, rather than choosing a treatment on my own.
Sana | If a correction is authorized, keep the original report and the reason for the change. We need a clear history.
Owen | Agreed. A [[corrected report::Corrected report records an authorized revision; the original amount, reason, and approval should remain traceable.]] should be traceable to the review decision. Quietly replacing the number would make it harder to understand what happened and whether the issue was actually resolved.
Sana | Please send the specific item reference, the missing evidence, and your follow-up status to me before we finalize the submission.
Owen | I will keep the [[variance::Variance is the one-thousand-dollar difference between reported and supported figures; it remains visible until an evidenced treatment resolves it.]] visible until it is resolved through that process. We can be precise about the gap without either hiding it or claiming more than the evidence shows.''',
    rehearsal=('Read turns 1-8, distinguishing the reported amount from the supported amount.', 'Swap roles for turns 9-20; keep the unresolved item neutral and specific.', 'Complete the K9 reconciliation and check that its difference belongs to materials, not personnel.'),
    transfer_title='Reconcile another grant total',
    transfer_setup='Grant K9 reports personnel $18,000, materials $7,000, and travel $3,000. Assembled support is $18,000, $6,500, and $3,000 respectively. One materials record remains missing.',
    transfer='''Officer: "The reported total is ___." | $28,000 | Eighteen thousand plus seven thousand plus three thousand equals twenty-eight thousand.
Coordinator: "The supported total is ___." | $27,500 | Eighteen thousand plus six thousand five hundred plus three thousand equals twenty-seven thousand five hundred.
Officer: "The unresolved difference is ___." | $500 | The reported total exceeds the assembled support by five hundred dollars.
Coordinator: "The affected category is ___." | materials | Personnel and travel match their support; the five-hundred-dollar difference is in materials.''',
))


BOOK['units'].append(unit(
    title='Interagency Coordination',
    scene='Everyone is involved, but nobody has called the resident',
    skill='Assign distinct responsibilities across agencies and confirm a handoff without implying that the underlying service is approved.',
    brief='Request Q41 concerns accessible transport to a community appointment. The Community Office reviews program eligibility; the Transit Office checks vehicle availability and booking feasibility. Each office assumed the other would contact the resident. During a coordination call, Jon from Community agrees to own the resident update at 15:00 local time. Aisha from Transit will send an availability status to Jon by 14:30. Eligibility and a booking both remain unconfirmed. The authorized initial handoff needs the request reference, pickup zone, and requested time window, not the resident\'s full medical file.',
    cast='Jon | Community Office coordinator\nAisha | Transit Office coordinator',
    culture=('Shared work still needs named actions', 'Saying we are handling it can hide a gap between organizations. Assign one person to each action and repeat the recipient, deadline, and expected result. Keep responsibility for communicating progress distinct from authority to approve eligibility or confirm a booking.'),
    a='''Who owns the resident update? | Jon at 15:00 local time | Aisha at an unspecified time | Both offices without a named lead | The resident's appointment provider | Jon explicitly accepts responsibility for the resident update at the stated local time.
What will Transit provide by 14:30? | An availability status to Jon | A guaranteed completed trip | A Community eligibility decision | The resident's full medical file | Aisha commits to sending a status on availability, not approving eligibility or guaranteeing a booking.
What remains unconfirmed? | Eligibility and the transport booking | The Q41 reference | The named resident-contact owner | The agreed internal update time | The offices have assigned communication tasks, but neither the eligibility decision nor booking is confirmed.''',
    vocabulary='''interagency | Involving two or more public agencies. | coordinate interagency work
lead contact | The named person coordinating communication for a matter. | appoint a lead contact
referring office | The office sending a matter to another responsible team. | identify the referring office
receiving office | The office to which a matter is transferred. | confirm the receiving office
responsibility matrix | A record mapping tasks to their responsible owners. | update the responsibility matrix
action owner | The named person accountable for a specific next action. | assign an action owner
handoff | Transfer of a task, information, or responsibility between teams. | confirm the handoff
acknowledgment of receipt | Confirmation that information has arrived. | request acknowledgment of receipt
acceptance of responsibility | Confirmation that a person or team has taken ownership of a task. | record acceptance of responsibility
service dependency | A prerequisite affecting whether a service can proceed. | identify service dependencies
availability check | A review of whether the needed resource or slot can be supplied. | complete an availability check
booking confirmation | Notice that a specific service arrangement is reserved or agreed. | issue booking confirmation
eligibility review | Assessment against the program's qualification requirements. | complete the eligibility review
request reference | An identifier linking records to the same service request. | quote the request reference
pickup zone | The defined area from which a transport pickup is requested. | confirm the pickup zone
requested window | The time period asked for before scheduling is confirmed. | record the requested window
data-sharing authority | The applicable basis permitting a defined information transfer. | verify data-sharing authority
minimum necessary data | Information limited to what is needed for the stated authorized purpose. | share the minimum necessary data
purpose limitation | Restricting information use to the defined permitted purpose. | observe purpose limitation
secure channel | An approved communication route with appropriate safeguards. | use the secure channel
joint status | A coordinated account of progress across participating teams. | prepare a joint status
escalation contact | The person designated for unresolved or urgent coordination issues. | identify the escalation contact
dependency tracker | A record of prerequisites, owners, and their status. | maintain the dependency tracker
closed-loop handoff | A transfer in which receipt and next responsibility are confirmed. | complete a closed-loop handoff''',
    precision='Receipt means a message arrived. Acceptance of responsibility means someone has agreed to perform the next task. Neither proves that the resident is eligible or that a vehicle is booked. Record these different statuses separately in the shared request record.',
    precision_extra='Share information under the applicable authority and safeguards, limited to the task. Here the authorized initial exchange needs a reference, pickup zone, and requested window. Do not attach a full medical file merely because both teams are public agencies.',
    phrases='''Name the gap | Each office assumed the other would contact the resident.
Assign the lead | Jon will own the resident update.
Set the external time | The resident update is at 15:00 local time.
Set the internal time | Transit will send its status to Jon by 14:30.
Define the task | We are checking availability, not confirming a booking yet.
Keep the eligibility boundary | Community retains the eligibility review.
Separate receipt from ownership | Has the receiving office accepted the task, or only received the message?
Use the reference | Please quote Q41 in both records.
Limit the transfer | The initial handoff needs the pickup zone and requested window.
Avoid excess information | The full medical file is not needed for this exchange.
Check permission and method | Use the authorized data-sharing route and approved channel.
Confirm the recipient | Send the availability status to Jon, not directly to an unassigned inbox.
Handle an incomplete result | Report the open question even if availability is not confirmed by then.
Name escalation | Who should we contact if the internal update is missed?
Read back ownership | Aisha checks availability; Jon updates the resident.
Close the loop | Please confirm receipt and the next action in the request record.''',
    notes='''Own the update | Assigns communication accountability without granting decision authority.
By 14:30 | Gives the internal contribution a deadline before the resident contact.
Not ... yet | Prevents an investigation task from being mistaken for a completed result.
Retains | Keeps an existing responsibility with the correct office.
Only received | Distinguishes message delivery from task ownership.
Even if | Preserves the update commitment when the underlying answer remains incomplete.''',
    d='''Which handoff is complete? | Aisha sends the availability status by 14:30; Jon confirms receipt and updates the resident at 15:00. | Both offices assume someone else will call. | Sending an email alone proves the resident has a booking. | Jon transfers every responsibility without acceptance. | The complete handoff names actions, recipients, timing, and confirmation without claiming service approval.
Which statement preserves the agencies' roles? | Community reviews eligibility; Transit checks availability. | Transit automatically decides Community eligibility. | Community guarantees a vehicle without asking Transit. | Both reviews are complete because the request has a number. | The brief assigns these distinct responsibilities and leaves both substantive outcomes open.
Which information belongs in the authorized initial exchange? | Request reference, pickup zone, and requested window | The full medical file by default | All unrelated case notes | Every resident record held by either office | The defined initial task needs the specified limited information, not unnecessary sensitive records.
What should happen if availability remains unknown at 14:30? | Aisha sends that status and the open question so Jon can give the promised update. | Both offices stay silent until a booking exists. | Jon announces a guaranteed vehicle anyway. | The resident-contact task silently disappears. | A progress update remains useful and due even when the underlying resource decision is incomplete.''',
    dialogue='''Jon | We have a gap on Q41. The resident has heard from neither office. Our note says Transit to contact, but I cannot find an accepted handoff.
Aisha | We thought Community was the [[lead contact::Lead contact identifies who coordinates resident communication, resolving the earlier ambiguity between offices.]]. Let us assign that explicitly now rather than leave another shared note that neither office owns.
Jon | I will update the resident at 15:00 local time. I need your availability position early enough to explain what is still open.
Aisha | I will be the [[action owner::Action owner assigns Aisha the Transit status task, distinct from Jon's resident update.]] for the Transit status and send it to you by 14:30. That gives you a defined input before your contact.
Jon | Is that a booking confirmation, or simply the result of the availability check at that point?
Aisha | It is an [[availability check::Availability check assesses resources; it does not automatically confirm a reservation or a completed journey.]] status. We have not confirmed a vehicle or a booking. I will distinguish available, unavailable, and still under review rather than use the vague word arranged.
Jon | Community still needs to complete its program review. I do not want either team to imply that the transport request itself establishes eligibility.
Aisha | Keep the [[eligibility review::Eligibility review remains Community's task; coordination assignments do not decide whether the resident qualifies.]] with Community. Transit can report its resource position, but that does not replace your office's decision or remove the other service dependencies.
Jon | What do you need in the initial handoff? The file contains personal details that may not be relevant to checking a possible slot.
Aisha | Under the authorized exchange, send the [[request reference::Request reference links the offices' records to Q41 without repeating unnecessary personal information.]], pickup zone, and requested time window. We do not need the full medical file for that initial task.
Jon | I will use the approved channel and keep the information limited to that purpose. Should I send it to your personal work queue?
Aisha | Yes, through the designated [[secure channel::Secure channel is the approved route for this authorized exchange, preserving safeguards while the two offices coordinate.]]. I will confirm that it arrived and that I have accepted the availability task, not just that the message is visible.
Jon | That is where we lost the thread last time. Sent appeared in the record, and everyone read it as taken over. I will separate those statuses.
Aisha | An [[acknowledgment of receipt::Acknowledgment of receipt confirms arrival, not task ownership; acceptance must also be explicit.]] alone would not show ownership. I will record the next action and its deadline so your team can see what I have actually agreed to do.
Jon | If you still cannot confirm availability at 14:30, please tell me that rather than wait until you have a final answer.
Aisha | Agreed. The [[joint status::Joint status combines both offices' progress and open questions without implying completed decisions.]] can explain the open questions. You should be able to give the resident the promised update even if the booking decision is still pending.
Jon | We also need a route if the internal update is missed or a dependency cannot be resolved within the available time.
Aisha | I will identify the [[escalation contact::Escalation contact provides a named route for unresolved coordination issues, preventing another round of unowned messages.]] in the record. That is a coordination route, not a promise to override eligibility requirements or create capacity that does not exist.
Jon | Let me read it back: you send the availability status by 14:30; I own the resident update at 15:00. Eligibility and booking remain unconfirmed.
Aisha | Correct. That is a [[closed-loop handoff::Closed-loop handoff confirms receipt, ownership, and next actions instead of relying on message delivery alone.]]. I will confirm the transfer in Q41 and keep my status separate from any booking confirmation so both offices communicate the same position.''',
    rehearsal=('Read turns 1-8 and give the two update times distinct emphasis.', 'Swap roles for turns 9-20; pause after the named recipient and accepted next action.', 'Complete the R52 handoff below and read back each owner with the correct deadline.'),
    transfer_title='Assign a second interagency update',
    transfer_setup='For R52, Housing checks program eligibility and Mobility checks vehicle availability. Mobility officer Bea sends status to Housing officer Eli by 10:00. Eli contacts the resident at 10:30 local time. No booking is confirmed.',
    transfer='''Coordinator: "The internal status owner is ___." | Bea | Bea is assigned to send Mobility's availability status to Eli.
Officer: "The internal update deadline is ___." | 10:00 | This deadline precedes the resident update and gives Eli the information needed for that contact.
Coordinator: "The resident-contact owner is ___." | Eli | Eli owns communication with the resident, distinct from Bea's availability task.
Officer: "The resident update is at ___." | 10:30 local time | The supplied resident-contact commitment includes the exact time and its local-time reference.''',
))

BOOK['units'].append(unit(
    title='Constituent Services and Escalation',
    scene='A referral that does not send the resident in circles',
    skill='Repair a misdirected service request by explaining jurisdiction, confirming a referral, and preserving a separate complaint route.',
    brief='Resident business owner Tessa has contacted three offices about placing a bench outside her shop. Licensing handles business registration, not permission to use the public sidewalk. Under this fictional town\'s process, Public Works Permit Intake receives the site plan and routes the sidewalk-use application for review. Service officer Ben has not yet confirmed that intake has accepted Tessa\'s referral. Ben can seek confirmation and call her Wednesday at 10:00 local time. That is a follow-up commitment, not a permit decision deadline. Her complaint about repeated redirection should be recorded separately from the permit application.',
    cast='Tessa | Resident business owner\nBen | Constituent service officer',
    culture=('Explain the reason for the referral', 'Another office name can sound like another rejection unless the resident understands its role. Acknowledge the repeated redirection, explain the receiving office\'s function, and confirm the handoff. Avoid promising a permit as compensation for a frustrating service experience.'),
    a='''Which office receives the site plan under this process? | Public Works Permit Intake | Business Licensing | The service officer's personal mailbox as a final decision route | An unspecified fourth office | The brief expressly assigns receipt and routing of sidewalk-use applications to Public Works Permit Intake.
What is Ben's Wednesday 10:00 commitment? | A follow-up call about the referral | Guaranteed permit approval | Completion of all site inspections | Automatic acceptance of the site plan | Ben promises a status call, not an application outcome or completion of every review step.
How should the redirection complaint be recorded? | Separately from the permit application | As proof that the permit must be granted | As withdrawal of the application | Only if Tessa stops asking about the bench | The complaint concerns service handling and should not be confused with the separate permit decision.''',
    vocabulary='''constituent service | Assistance connecting people with public processes or offices. | provide constituent service
jurisdiction | The scope of an office's legal or assigned responsibility. | clarify jurisdiction
service remit | The defined matters an office handles. | explain the service remit
intake office | The unit receiving and initially routing requests or applications. | identify the intake office
referral | Direction or transfer of a matter to a relevant person or office. | make a referral
warm referral | A supported transfer that helps connect the person to the receiving office. | arrange a warm referral
referral acceptance | Confirmation that the receiving office has taken the referred matter. | verify referral acceptance
case summary | A concise account of the issue and relevant history. | prepare a case summary
service history | The record of contacts and actions concerning a service matter. | review the service history
business registration | Recording a business under the applicable registration process. | verify business registration
sidewalk-use permit | Permission under a local process for a specified use of a public sidewalk. | apply for a sidewalk-use permit
site plan | A drawing showing the location and layout relevant to a proposal. | submit a site plan
application receipt | Confirmation that an application has arrived. | confirm application receipt
completeness review | Assessment of whether the required application items are present. | conduct a completeness review
substantive review | Assessment of the application's merits against the relevant requirements. | await substantive review
permit condition | A requirement attached to an issued permission. | explain permit conditions
follow-up call | A later contact to provide status or continue handling a matter. | schedule a follow-up call
response target | A planned time for a defined response. | state the response target
decision deadline | A time by which a decision is due under the applicable process. | verify the decision deadline
service complaint | A complaint about the handling or quality of a public service. | record a service complaint
complaint reference | An identifier for a complaint record. | provide the complaint reference
review route | The process for obtaining further examination of a matter. | explain the review route
case continuity | Preservation of relevant information across contacts or transfers. | maintain case continuity
closure reason | The documented explanation for closing a service record. | record the closure reason''',
    precision='Registration of a business does not automatically authorize use of public space. The fictional town assigns the sidewalk application to Public Works Permit Intake. Explain that role clearly, but do not present the same office structure or permit process as universal.',
    precision_extra='Application receipt, completeness review, substantive review, and permission are different stages. A supported referral can reduce repeated explanation without guaranteeing the result. Keep a service complaint separate so that acknowledging poor handling does not pre-decide the permit.',
    phrases='''Acknowledge the history | You have already been redirected repeatedly.
Take responsibility for clarification | I will confirm the correct intake route before sending you elsewhere.
Explain the first office | Licensing handles business registration.
Explain the receiving office | Public Works Permit Intake receives the sidewalk-use application.
Name the needed item | The stated intake process asks for a site plan.
Avoid implied permission | Business registration does not itself authorize this sidewalk use.
Check the transfer | Has Permit Intake accepted the referral?
Offer continuity | With the appropriate authorization, I will pass on the relevant case summary.
Limit personal information | I will use only the details needed for this referral.
State the follow-up | I will call Wednesday at 10:00 local time.
Define the commitment | That call will report the referral status, not guarantee a permit decision.
Keep the complaint separate | I will record the redirection complaint separately from the application.
Avoid compensation by approval | The service problem does not authorize me to grant the permit.
Explain the next stage | Receipt is followed by the applicable completeness and substantive review.
Provide a reference | I will give you the reference and responsible contact once confirmed.
Close accurately | I will not mark the matter resolved merely because an email was sent.''',
    notes='''Already been redirected | Recognizes the resident's actual service history.
Before sending | Makes verification a prerequisite to another referral.
Does not itself | Limits what one administrative action establishes.
Accepted the referral | Checks ownership rather than only message delivery.
Report ... not guarantee | Defines a realistic follow-up commitment.
Separately from | Keeps the complaint and application processes distinct.''',
    d='''Which explanation gives a useful referral? | Licensing handles registration; Public Works Permit Intake receives the sidewalk application and site plan. | Try another office; they probably know. | Registration automatically permits every sidewalk use. | Your complaint means no application is needed. | The explanation names the responsible function and required intake item without promising permission.
Which follow-up statement is accurate? | I will call Wednesday at 10:00 local time with the referral status. | Your permit will be approved by Wednesday at 10:00. | Receipt means every permit condition is satisfied. | A sent email proves the intake team accepted the case. | Ben can promise a status contact, while acceptance and substantive decisions remain unconfirmed.
What preserves case continuity? | An authorized relevant summary and confirmation of the receiving contact | Requiring the resident to restart without checking the record | Sending unrelated personal files to every office | Closing the case when the first email leaves | A relevant, authorized handoff reduces repetition while retaining ownership and appropriate information limits.
How should the complaint affect the permit decision? | It should be handled separately, without pre-deciding the permit. | It automatically guarantees approval. | It automatically disqualifies the applicant. | It replaces the site plan. | The service complaint concerns handling, not whether the proposed sidewalk use meets permit requirements.''',
    dialogue='''Tessa | I have explained this bench three times. Licensing sent me elsewhere, and I was sent back. Before I join another queue, can someone tell me who actually handles it?
Ben | I am sorry about the repeated redirection. Let us clarify the [[service remit::Service remit identifies what each office handles, explaining the referral rather than merely redirecting the resident.]] before I send you anywhere else. Licensing handles business registration, which is different from permission to use the public sidewalk.
Tessa | My business is registered, so I thought that office could confirm whether the bench is allowed outside the shop.
Ben | A [[sidewalk-use permit::Sidewalk-use permit concerns this town's public-space permission, which business registration alone does not provide.]] follows a different process here. Public Works Permit Intake receives that application and the site plan, then routes it for the relevant review.
Tessa | I have a drawing showing where the bench would go and how much space would remain. Is that the document they need first?
Ben | The stated intake item is a [[site plan::Site plan shows the proposed location and layout for the permit process, rather than proving that the proposal is already approved.]]. I can confirm their submission requirements, but I should not say your drawing is complete or approved before the receiving team checks it.
Tessa | Can you transfer the information I have already given? I do not want to start the story again with a fourth person.
Ben | With the appropriate authorization, I can pass on a relevant [[case summary::Case summary preserves the issue and contact history, reducing unnecessary repetition for the resident.]]. I will include the bench request and previous contacts, using only the details needed for this referral through the approved route.
Tessa | That would help. But is someone at Public Works taking it on, or will I arrive with another email that nobody has picked up?
Ben | [[Referral acceptance::Referral acceptance confirms that the receiving office has taken the matter; a sent message alone does not establish this.]] is not confirmed yet. I will seek that confirmation and identify the responsible contact instead of treating an outgoing email as a completed handoff.
Tessa | When will I hear from you? I need something more specific than soon because I am planning the shop opening.
Ben | I can make a [[follow-up call::Follow-up call is a timed status contact within Ben's control, not a deadline for granting the permit.]] on Wednesday at 10:00 local time. I will tell you whether intake has accepted the referral and what the next step is.
Tessa | Does that mean I will have a permit decision by Wednesday morning, or only information about where the application stands?
Ben | Only the status update. A [[decision deadline::Decision deadline is a separate requirement of the permit process; Ben's call commitment does not create or replace it.]] for the permit has not been established here. Receipt, completeness review, and substantive review are different stages, and I cannot collapse them into that call.
Tessa | I also want the repeated redirection recorded as a complaint. That has cost time even if the permit process still has work to do.
Ben | I will record a separate [[service complaint::Service complaint addresses the handling experience; it should not be treated as an application, an approval, or a reason for refusal.]] about the handling. That does not replace your application or decide whether the bench meets the requirements, but the service concern should be addressed.
Tessa | Please keep both references clear. I do not want the complaint to cause the application to disappear from the system.
Ben | I will maintain [[case continuity::Case continuity preserves relevant history while keeping the complaint and permit application distinguishable.]] while distinguishing the records. When the references and receiving contact are confirmed, I will explain which one to quote for each purpose.
Tessa | Then I will expect your Wednesday call about the referral, and the complaint will follow its own review route.
Ben | Correct. I will not use sent an email as the [[closure reason::Closure reason explains the actual outcome; an unaccepted referral does not establish resolution.]] for a resolved case. The record should show the actual handoff status, the remaining action, and who owns it.''',
    rehearsal=('Read turns 1-10, acknowledging the repeated referral without promising a permit.', 'Swap roles for turns 11-20 and distinguish the application from the service complaint.', 'Complete the banner referral below; read the call commitment without turning it into an approval date.'),
    transfer_title='Repair another referral',
    transfer_setup='For a fictional street-banner application, Events Registration records the event but Road Use Intake receives the banner plan. Officer Hana promises a referral-status call on Thursday at 14:00 local time. No permit decision is promised.',
    transfer='''Resident: "The office receiving the banner plan is ___." | Road Use Intake | The local process assigns banner-plan receipt to Road Use Intake, not Events Registration.
Officer: "The promised follow-up owner is ___." | Hana | Hana is the named officer who commits to the referral-status call.
Resident: "The call is scheduled for ___." | Thursday at 14:00 local time | The stated contact includes the day, time, and local-time reference.
Officer: "The call concerns ___." | referral status | The promise is to report the referral position, not to guarantee a permit decision.''',
))


BOOK['units'].append(unit(
    title='Transparency, Records, and Ethics',
    scene='Found records are not automatically cleared records',
    skill='Explain a federal records-review status without promising full release or using a possible exemption as a blanket refusal.',
    brief='A fictional U.S. federal agency receives request F77 for signed service contracts and their attachments from January through March. Staff locate eight responsive contract files. Two contain personal contact details requiring review; no release or withholding decision has been made. An initial acknowledgment mistakenly promises that every page will be released automatically. Records officer Imani and program liaison Cole must correct the promise, preserve the records, and explain the review process. The presence of potentially protected information does not itself authorize withholding an entire file. Applicable disclosure standards and any partial release must be assessed by the responsible staff.',
    cast='Imani | Records officer\nCole | Program liaison',
    culture=('Transparency needs accurate status language', 'A requester can deserve a clear explanation even when review is unfinished. Distinguish records found from records cleared for release. Do not use privacy as a vague excuse, but do not promise to disclose personal details before the appropriate review.'),
    a='''What has been established? | Eight responsive contract files have been located. | Every page has been cleared for release. | All eight files must be withheld. | No records exist. | The search located eight responsive files, but the release review has not reached a decision.
What needs correction? | The promise of automatic full release | The January-through-March request scope | The number eight without contrary evidence | The need to preserve responsive records | The acknowledgment overpromises disclosure before the required review of potentially protected information.
What follows from personal details appearing in two files? | Those details require review; full-file withholding is not automatic. | Both files are automatically excluded in full. | Every page must be released without review. | The entire request can be treated as nonexistent. | Potentially protected details call for the applicable review, including consideration of releasable portions.''',
    vocabulary='''FOIA | Freedom of Information Act; the U.S. federal records-access law. | process a FOIA request
records request | A request for access to identified or described records. | clarify a records request
request scope | The boundaries of the records sought. | confirm the request scope
responsive record | A record falling within the request's description. | identify responsive records
records custodian | The person or unit responsible for relevant records. | contact the records custodian
search terms | Words or criteria used to locate relevant records. | document the search terms
date range | The start and end period limiting a search or request. | confirm the date range
attachment | A file or document included with another record. | review the attachments
acknowledgment | A response confirming receipt of a request. | issue an acknowledgment
tracking number | A reference used to follow a request's progress. | quote the tracking number
disclosure review | Assessment of what information can or must be released. | conduct disclosure review
exemption | A legal provision potentially permitting or requiring specified information to be withheld. | assess an exemption
foreseeable harm | The expected harm considered under the applicable federal withholding standard. | assess foreseeable harm
redaction | Removal or masking of protected information from a released copy. | apply justified redactions
segregable information | Information that can be separated from protected material for release. | identify segregable information
partial release | Disclosure of releasable portions while other information is withheld under an applicable basis. | prepare a partial release
withholding basis | The legal and factual reason supporting nondisclosure. | document the withholding basis
personal privacy | An individual's interest in protection of personal information. | assess personal-privacy interests
release copy | The version prepared for disclosure after the applicable review. | verify the release copy
records preservation | Keeping records intact under applicable requirements. | maintain records preservation
retention schedule | A rule or policy governing how long records are retained and disposed of. | follow the retention schedule
administrative appeal | A request for agency-level review of an initial decision. | explain the administrative appeal route
public liaison | A designated contact helping requesters understand or resolve process concerns. | contact the public liaison
review status | The current position of an assessment before or after a decision. | explain the review status''',
    precision='Responsive means within the request scope; it does not mean cleared for release. The eight files match the stated contract request. Personal details in two files require review, but their presence alone does not decide the fate of every page.',
    precision_extra='For U.S. federal requests, responsible reviewers assess the applicable disclosure and withholding standards, including partial disclosure where appropriate. Do not use a possible exemption as a blanket refusal or quietly change source records to simplify a release.',
    phrases='''State the search result | We located eight responsive contract files.
Retain the request scope | The request covers signed contracts and attachments from January through March.
Separate stages | Located does not mean cleared for release.
Correct the earlier promise | The acknowledgment should not have promised automatic full disclosure.
Describe the pending review | Two files contain personal details that require review.
Avoid a blanket refusal | Their presence does not automatically justify withholding the entire files.
Ask for the basis | What applicable legal and factual basis supports the proposed withholding?
Check partial disclosure | Which information can be separated and released?
Preserve the source | Keep the original records intact under the applicable requirements.
Distinguish the copy | Any justified redactions belong in the reviewed release copy.
Avoid an invented date | We should provide the actual process status, not an unsupported release deadline.
Keep the reference | Please use F77 in the correction and subsequent updates.
Explain responsibility | The records team will make the disclosure assessment.
Document the reasoning | Retain the review decision and its supporting basis.
Provide the relevant route | The response should explain the applicable review or appeal information.
Close accurately | We can report progress without predicting an unmade disclosure decision.''',
    notes='''Located does not mean | Separates a search result from a disclosure decision.
Should not have promised | Corrects a prior overstatement directly.
Require review | Identifies the next task without pre-deciding the result.
Legal and factual basis | Requests both the applicable provision and the reason it fits.
Can be separated | Focuses on releasable information rather than treating a file as indivisible.
Unmade decision | Prevents a progress message from implying that review has finished.''',
    d='''Which update is accurate? | Eight responsive files were located; disclosure review remains underway. | Eight files were found, so every page is automatically public. | Two personal details justify refusing every record. | The search found nothing because review is incomplete. | The update reports the completed search step while preserving the unresolved disclosure decision.
How should the earlier acknowledgment be handled? | Correct the automatic-release promise and explain the actual review status. | Wait for final review before mentioning the inaccurate promise. | Replace the promise with a full-withholding notice for the two files. | Reissue a receipt notice without acknowledging the earlier assurance. | The requester needs an explicit correction and actual status; silence, premature withholding, or an unexplained replacement leaves the error unresolved.
What is the right response to a proposed full-file withholding? | Ask for the applicable basis and assess whether releasable portions can be separated. | Accept it solely because one page contains contact details. | Assume all personal information must always be published. | Stop preserving the file because release is uncertain. | The responsible assessment must address the basis and possible partial disclosure, not merely the presence of sensitive material.
What should remain intact? | The source records under applicable preservation requirements | Only the final email to the requester | A rewritten original with inconvenient details removed | No records once a possible exemption is noticed | Release preparation does not authorize alteration or destruction of the underlying agency records.''',
    dialogue='''Cole | I need to correct our F77 acknowledgment. We located eight files, but the letter promised every page. Two contain personal contact details that have not been reviewed.
Imani | First separate [[responsive records::Responsive records match the request; locating them does not clear every part for disclosure.]] from records cleared for disclosure. The files match the request, but the release assessment is not finished. That acknowledgment promises more than we can support.
Cole | The request is for signed service contracts and their attachments from January through March. We have not been asked for every email about the projects.
Imani | Keep that [[request scope::Request scope defines the contracts, attachments, and date range, keeping the search boundaries explicit.]] visible in the record. We should not silently broaden or narrow the request, and any genuine ambiguity should be handled through the appropriate clarification process.
Cole | I can flag the affected files for review. I would rather not send a blanket withholding message before anyone has looked at the individual details. Is that right?
Imani | Yes. A possible [[exemption::Exemption requires assessment against the information and legal standard, not automatic full-file withholding.]] needs review against the actual information and applicable standard. Personal details do not automatically settle the treatment of every page in those files.
Cole | Then the team should distinguish the contact details from the rest of the contract material, rather than treating each file as indivisible.
Imani | Yes, assess [[segregable information::Segregable information can be separated from protected material, allowing responsible reviewers to assess release of nonprotected portions.]]. The responsible reviewers must examine what can be released and document any valid withholding basis, including the relevant harm analysis where the law requires it.
Cole | I do not want to alter the originals while preparing the material for review. What should the program team preserve?
Imani | Follow [[records preservation::Records preservation keeps sources intact; disclosure preparation does not authorize changes to the originals.]] requirements and keep the source records intact. Preparation of a disclosure version is not permission to rewrite or delete the originals to make the request easier to handle.
Cole | If the review supports removing particular details, we would work from a separate version for disclosure.
Imani | Correct. Any justified [[redaction::Redaction removes or masks protected information in the release version while leaving the original record preserved.]] belongs in the reviewed release copy, with the required basis and explanation. Do not obscure material simply because it is embarrassing or inconvenient for the office.
Cole | The requester may feel we are changing our position after promising full release. How should I explain the correction?
Imani | Correct the [[acknowledgment::Acknowledgment confirms receipt; its mistaken release promise needs correction, not treatment as a disclosure decision.]] directly. Say that the earlier automatic-release assurance was inaccurate, that eight responsive files were located, and that disclosure review is still underway.
Cole | Should we give a new release date now, so the correction does not sound vague?
Imani | Give the actual [[review status::Review status describes the current assessment and pending steps; it should not be replaced by an unsupported release deadline.]] and any properly established process information. Do not invent a deadline to compensate for the earlier promise. The responsible team should confirm any applicable timing statement.
Cole | We will retain the file references, the decision record, and the explanation of anything ultimately withheld.
Imani | Also check the [[partial release::Partial release discloses releasable portions while applying any justified withholding under the completed assessment.]] position where full disclosure is not possible. The response should reflect the actual review, not a blanket choice between releasing everything and releasing nothing.
Cole | I will route the correction through the records team and keep F77 attached to the search and review history.
Imani | Good. When a decision is issued, provide the applicable [[administrative appeal::Administrative appeal is the agency-level review route for an initial decision, distinct from the present progress update.]] information and relevant contacts. We can be transparent about the process while leaving the substantive disclosure decision with the authorized reviewers.''',
    rehearsal=('Read turns 1-8, distinguishing responsive records from information cleared for release.', 'Swap roles for turns 9-20; make the acknowledgment correction direct and specific.', 'Complete the C44 status exchange below and keep its unresolved decision explicit.'),
    transfer_title='Describe another records-review status',
    transfer_setup='Request C44 covers final inspection reports for April. Six responsive files are found. One contains information requiring review. No release or withholding decision has been made.',
    transfer='''Liaison: "The request reference is ___." | C44 | C44 is the tracking reference supplied for this separate records request.
Officer: "The search found ___." | six responsive files | Six files match the stated request scope, but responsiveness does not establish disclosure clearance.
Liaison: "The requested month is ___." | April | April is the time boundary stated for the final inspection reports.
Officer: "The disclosure decision is ___." | not yet made | The record explicitly leaves release and withholding undecided pending the responsible review.''',
))

BOOK['units'].append(unit(
    title='Performance Metrics and Budget Justification',
    scene='Twenty workshops do not prove the outcome',
    skill='Explain outputs, response rates, and observed outcomes while keeping a budget request separate from a causal success claim.',
    brief='A fictional employment program requests $240,000 for next year after spending $200,000 this year. It delivered 20 workshops and recorded 400 attendances, which include repeat visits. In the previous follow-up cohort, 200 of 250 invited people responded and 80 respondents reported employment at 90 days. In the current cohort, 210 of 300 responded and 105 reported employment. The respondent employment rates are 40% and 50%, while response rates are 80% and 70%. Analyst Faye and budget officer Luis must explain the figures without counting attendances as unique people or claiming the program caused the observed change.',
    cast='Faye | Program analyst\nLuis | Budget officer',
    culture=('A useful challenge improves the public explanation', 'A budget reviewer may ask what changed for residents rather than how busy the team was. Answer with definitions, denominators, and limits. Preserve genuine activity and outcome evidence without treating a request for better measurement as dismissal of the staff\'s work.'),
    a='''What do the 400 attendances count? | Visits, including repeat visits | Exactly 400 unique people | Exactly 400 people gaining employment | Only survey respondents | The attendance count includes repeat visits and therefore is not a unique-person or employment count.
What is the current respondent employment rate? | 50% | 35% | 70% | 40% | One hundred five employed respondents divided by two hundred ten respondents equals fifty percent.
How much does the requested budget exceed current spending? | $40,000, or 20% | $20,000, or 10% | $40,000, or 40% | $240,000, or 120% | The difference is forty thousand, and forty thousand divided by two hundred thousand is twenty percent.''',
    vocabulary='''budget justification | The evidence and reasoning supporting a funding request. | strengthen the budget justification
appropriation | Funding authority granted through the applicable legislative process. | distinguish a request from an appropriation
budget request | A proposal for future funding. | submit a budget request
actual expenditure | The amount spent under the stated accounting basis and period. | report actual expenditure
input | A resource used to deliver an activity or service. | identify program inputs
activity | Work carried out by a program. | describe program activities
output | A direct product or count of services delivered. | measure outputs
outcome | A change or result experienced by the target population. | measure outcomes
impact | A broader or causally attributed effect, depending on the evaluation definition. | assess program impact
attendance | A recorded instance of participation, which may include repeat visits. | count attendances
unique participant | A distinct person counted once within the defined scope. | count unique participants
cohort | A defined group observed over a particular period. | compare cohorts
follow-up survey | A later survey collecting information after a service or event. | conduct a follow-up survey
response rate | The share of invited eligible people who provide a response under the stated definition. | calculate the response rate
respondent | A person who supplies a survey response. | identify respondents
denominator | The quantity by which another quantity is divided to calculate a rate. | state the denominator
percentage point | The unit used for the difference between two percentages. | report percentage-point change
relative change | The difference expressed as a share of the starting value. | distinguish relative change
nonresponse bias | Distortion that may arise when respondents differ systematically from nonrespondents. | assess nonresponse bias
selection effect | A difference arising from how people enter or remain in a measured group. | examine selection effects
attribution | Assignment of an observed result to a particular cause. | support causal attribution
counterfactual | An estimate of what would have happened without the intervention. | define the counterfactual
performance target | A specified intended level of achievement. | set a performance target
measurement plan | A defined approach to collecting and interpreting performance evidence. | develop the measurement plan''',
    precision='The employment rates use respondents as the denominator: 80/200 = 40% and 105/210 = 50%. The change is ten percentage points, or 25% relative to 40%. These are observed respondent outcomes, not established results for every invited person.',
    precision_extra='Response rates fell from 200/250 = 80% to 210/300 = 70%. Different response patterns can affect comparability. The workshop count and attendance total measure activity; neither proves unique reach, employment gains, or the causal effect of the program.',
    phrases='''State the funding request | We are requesting two hundred forty thousand dollars for next year.
Compare with actual spending | This year we spent two hundred thousand dollars.
Quantify the increase | The request is forty thousand dollars higher, a twenty-percent increase.
Name the output | We delivered twenty workshops.
Keep the count accurate | The four hundred attendances include repeat visits.
Avoid a reach claim | We cannot call that four hundred unique participants.
Define the outcome measure | We measured reported employment among respondents at ninety days.
State the current denominator | The current rate is 105 out of 210 respondents.
Compare the rates | The respondent employment rate rose from forty to fifty percent.
Use the correct unit | That is a ten-percentage-point increase.
Separate relative change | Relative to forty percent, the increase is twenty-five percent.
Disclose response coverage | The response rate fell from eighty to seventy percent.
Avoid causal overstatement | These observations do not establish that the program caused the change.
Explain the evidence gap | We need better information about nonrespondents and cohort differences.
Connect money to delivery | The request needs a costed plan, not only a list of past activities.
Close the justification | Show the outputs, observed outcomes, limitations, and proposed measurement plan together.''',
    notes='''Higher ... increase | Compares the proposed amount with the stated spending baseline.
Include repeat visits | Prevents an attendance total from becoming a unique-person claim.
Among respondents | Limits the outcome rate to the people actually measured.
Percentage-point | Describes the subtraction of two percentages.
Relative to | Names the baseline used for a proportional change.
Do not establish ... caused | Separates observed association from causal evidence.''',
    d='''Which headline is supported? | Reported employment among respondents rose from 40% to 50%; response coverage changed. | The program caused a ten-percent improvement for every participant. | Four hundred different residents gained jobs. | The response rate rose to eighty percent this year. | The supported headline keeps the respondent denominator and acknowledges the changed response coverage.
How should the employment-rate difference be stated? | Ten percentage points, equivalent to a 25% relative increase from 40% | Ten percent relative and twenty-five percentage points | Fifty percentage points | A decrease of ten percentage points | Fifty minus forty equals ten points; ten divided by the forty-percent baseline equals twenty-five percent.
Which comparison describes survey response? | Previous 80%; current 70% | Previous 40%; current 50% | Previous 70%; current 80% | Both cohorts had complete response | Two hundred of two hundred fifty is eighty percent; two hundred ten of three hundred is seventy percent.
What does the budget request still need? | A costed delivery and measurement plan with limits stated | Only a larger attendance headline | A claim that the requested amount is already appropriated | An assumption that all nonrespondents found work | Past activity counts and limited outcome observations do not alone establish the future plan or its funding authorization.''',
    dialogue='''Luis | The workshop count tells me what we delivered. Before we ask for two hundred forty thousand next year, show me what we know about the people who attended.
Faye | The workshops are an [[output::Output is a direct count of services delivered; twenty workshops describes activity rather than a demonstrated change in residents' circumstances.]], not the outcome itself. We also recorded four hundred attendances, but that includes repeat visits and should not be presented as four hundred different people.
Luis | Do we have a reliable count of distinct participants, or are those repeat visits still mixed together?
Faye | The supplied total is not a [[unique participant::Unique participant counts each person once; the four-hundred attendance total includes repeat visits and cannot supply that count.]] count. I will not convert it into one. The follow-up survey provides a separate set of observations, with its own defined groups and response coverage.
Luis | Walk me through that measure. I want the numerator and denominator stated before we describe an improvement.
Faye | In the earlier [[cohort::Cohort identifies the group followed in a particular period, making clear that the two survey results concern different groups.]], eighty of two hundred respondents reported employment at ninety days. In the current cohort, one hundred five of two hundred ten respondents reported employment at the same follow-up point.
Luis | That gives forty percent and fifty percent among respondents. It does not tell us the employment rate among everyone invited.
Faye | Correct. The [[denominator::Denominator is the respondent count used in the employment calculation, not the larger invited population or the attendance total.]] is respondents in each case. The note should keep that visible so readers do not assume complete follow-up or an outcome measured for every participant.
Luis | The draft says employment improved by ten percent. That wording could be read differently from the calculation we just made.
Faye | The absolute difference is ten [[percentage points::Percentage points expresses fifty percent minus forty percent; it differs from the relative increase based on the starting rate.]]. Relative to the earlier forty-percent rate, that is a twenty-five-percent increase. I will use the first description and label the relative comparison if we include it.
Luis | How many people were invited to respond in each cohort? Different response patterns could affect the comparison.
Faye | The [[response rate::Response rate divides responses by invitations: 200/250 is 80%, while 210/300 is 70%.]] was two hundred out of two hundred fifty before, and two hundred ten out of three hundred now. That is eighty percent before and seventy percent now.
Luis | So the observed respondent rate improved while survey coverage fell. We should not hide either part of that picture.
Faye | Agreed. [[Nonresponse bias::Nonresponse bias may arise if respondents differ systematically from those not responding; the changed coverage warrants examination rather than assumed representativeness.]] is a question to assess, not a result we can quantify from these figures alone. We need better information about missing responses and differences between the groups.
Luis | The draft says the workshops drove the increase. I see a before-and-after comparison, but no estimate of what would have happened without the program.
Faye | The evidence does not support that [[attribution::Attribution assigns the observed change to the program; these cohort observations alone do not establish causation.]]. We have observed outcomes, but no design here establishing what would have happened without the program or accounting for other influences.
Luis | Then connect the request to a costed future plan as well. This year's actual spending was two hundred thousand, not two hundred forty thousand.
Faye | The [[budget request::Budget request proposes future funding; here it exceeds current spending by forty thousand dollars, or twenty percent.]] is forty thousand higher, a twenty-percent increase. It still needs a delivery plan and explanation of the additional resources, not just a larger activity claim.
Luis | Keep the useful results, but make the limits readable. A careful explanation will help the reviewer understand what the evidence can and cannot support.
Faye | I will present the outputs, respondent outcomes, response rates, and a [[measurement plan::Measurement plan specifies future evidence collection and interpretation, addressing gaps rather than overstating the current findings.]] alongside the costed proposal. That gives the funding discussion a clear basis without claiming a causal success we have not established.''',
    rehearsal=('Read turns 1-10, stressing attendances, respondents, and percentage points.', 'Swap roles for turns 11-20 and read both response rates before discussing the funding request.', 'Complete the second program comparison and verify all four calculations against the supplied figures.'),
    transfer_title='Compare a second program measure',
    transfer_setup='An earlier cohort has 30 employed respondents out of 100 respondents. A later cohort has 48 out of 120. Current spending is $150,000 and the next-year request is $180,000. No causal evaluation is supplied.',
    transfer='''Analyst: "The earlier respondent employment rate is ___." | 30% | Thirty divided by one hundred equals thirty percent among respondents.
Reviewer: "The later respondent employment rate is ___." | 40% | Forty-eight divided by one hundred twenty equals forty percent among respondents.
Analyst: "The increase in those rates is ___." | 10 percentage points | Forty percent minus thirty percent is ten percentage points, not a ten-percent relative change.
Reviewer: "The requested funding increase is ___." | $30,000 | One hundred eighty thousand minus one hundred fifty thousand equals thirty thousand dollars.''',
))
