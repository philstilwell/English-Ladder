"""Original nonprofit and NGO cases for the English Ladder learner book."""
from books.authoring import unit

BOOK = dict(
    slug='nonprofit-ngo', title='Nonprofit and NGO English',
    cover_label='ENGLISH FOR MISSION-DRIVEN TEAMS',
    cover_title='Nonprofit and NGO', cover_size=34,
    tagline='Make the mission understandable.\nKeep commitments grounded in evidence.',
    audience='For nonprofit and nongovernmental organization staff, program teams, fundraisers, partnership officers, volunteer coordinators, and board members.',
    map_intro='Eight mission-focused conversations: explain a program pathway, check a proposed grant change, interpret evaluation findings, coordinate a changed field visit, receive a safeguarding concern, maintain volunteer boundaries, verify a fundraising claim, and explain available reserves.',
    notes_title='Respectful language. Accountable decisions.',
    notes_intro='Mission-driven work brings together communities, volunteers, partners, funders, and governing boards. These cases practice practical English for explaining evidence, sharing responsibility, maintaining appropriate boundaries, and making commitments that people can rely on.',
    field_notes=[
        ('Describe results at the level measured', 'Participation, learning, behavior, and longer-term outcomes answer different questions. Keep a genuine achievement visible without claiming a change that has not been measured.', '"Two hundred people attended; sustained employment outcomes have not yet been measured."'),
        ('Read the restriction before promising flexibility', 'A useful new activity may still fall outside the purpose or period of a grant. Check the agreement and the authorized change process before committing the funds.', '"The activity fits our mission, but we still need to check whether this award can fund it."'),
        ('Include communities in the coordination loop', 'A partner agreement does not mean that affected people have received, understood, or accepted a changed arrangement. Name who will communicate, confirm, and follow up.', '"The partner can attend on the new date; the community contact has not yet confirmed it."'),
        ('Treat trust as a responsibility', 'A concern, personal story, or contact detail should not become material for a general update. Use the appropriate reporting and information-sharing process, and explain its limits honestly.', '"I will share the concern through the designated process, with the people who need to act."'),
    ],
    scope_note='All organizations, donors, communities, people, grants, statistics, dates, policies, and figures are fictional. This book teaches professional English, not legal, safeguarding, financial, or clinical procedures. Follow the applicable law, award terms, approved policies, and qualified advice. Charity Commission references apply to England and Wales; they are not universal rules for every nonprofit or NGO.',
    sources=[
        dict(title='OECD. Glossary of Key Terms in Evaluation and Results-Based Management, second edition (2023).', url='https://www.oecd.org/en/publications/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_632da462-en-fr-es.html', note='Background terminology for program pathways and evaluation. Definitions and fictional dialogues are original paraphrases, not a reproduction of the glossary.', checked='1 October 2026'),
        dict(title='CHS Alliance, Groupe URD, and Sphere. Core Humanitarian Standard, 2024 edition.', url='https://www.corehumanitarianstandard.org/_files/ugd/e57c40_f8ca250a7bd04282b4f2e4e810daf5fc.pdf', note='Background on accountable communication, coordination, safe reporting, and competent support. The exercises are original cases, not an adaptation of the standard.', checked='1 October 2026'),
        dict(title='Charity Commission. Making grants to charities and other organisations.', url='https://www.gov.uk/guidance/making-grants-to-charities-and-other-organisations', note='England-and-Wales guidance on grant purposes, written terms, and monitoring. The invented award controls the exercise; actual permissions require the relevant review.', checked='1 October 2026'),
        dict(title='Charity Commission. Charity reserves: building resilience (CC19).', url='https://www.gov.uk/government/publications/charity-reserves-building-resilience-cc19/charities-and-reserves', note='England-and-Wales guidance on available reserves and restricted funds. Fictional cash forecasts illustrate communication, not a universal reserve target or spending recommendation.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Mission, Theory of Change, and Program Design',
    scene='Attendance is an achievement, not a lasting outcome',
    skill='Explain the proposed pathway from a program activity to its intended result while distinguishing measured facts from assumptions.',
    brief='The fictional Pathway Project runs employment workshops. Its checked registration records show 200 distinct participants this quarter. The team has not measured employment after the workshops or whether any employment lasts. A donor update calls the attendance figure proof of lasting employment improvement. Program lead Nina and learning officer Joel must correct the claim while retaining the verified participation achievement. Their proposed pathway links workshops to stronger application skills, better job applications, and sustained employment, but those links and the necessary local job opportunities have not been established by the attendance records.',
    cast='Nina | Program lead\nJoel | Learning officer',
    culture=('Protect the achievement without overstating it', 'Staff may hear a challenge to an impact claim as a dismissal of their effort. Acknowledge the verified reach, then explain the additional evidence needed for the stronger claim. A clear program pathway can motivate learning without pretending the hoped-for result has already occurred.'),
    a='''What do the checked records establish? | 200 distinct people participated this quarter. | 200 people gained lasting employment. | Every participant improved application skills. | Local job opportunities increased because of the workshops. | The records substantiate distinct participation, not the unmeasured learning or employment results.
What has not been measured? | Post-workshop employment and its duration | The number of distinct participants | The quarter covered by the attendance record | Whether workshops took place | The brief states that employment after the workshops and its durability have not been measured.
What should happen to the donor claim? | Retain participation and remove the unsupported lasting-employment conclusion. | Remove every mention of the verified achievement. | Treat attendance as proof of every later outcome. | Replace the figure with a larger estimate. | The accurate revision keeps the supported participation result while withdrawing the stronger unmeasured claim.''',
    vocabulary='''mission | The organization's central purpose and intended contribution. | articulate the mission
program design | The planned structure and delivery of an intervention. | refine the program design
theory of change | An explanation of how actions are expected to produce change in a context. | test the theory of change
results chain | A sequence linking resources, actions, and intended results. | map the results chain
input | A resource used to deliver program work. | identify program inputs
activity | Work performed as part of a program. | specify the activities
output | A direct product or service delivered by program activity. | report program outputs
outcome | A change experienced by the people or systems a program seeks to support. | measure outcomes
impact | A broader or longer-term effect, with its meaning defined for the evaluation. | define the intended impact
assumption | A condition or explanation taken as true for planning until tested. | test the assumptions
causal link | A proposed or established relationship in which one factor affects another. | examine a causal link
pathway | The proposed sequence through which change is expected to occur. | explain the pathway
target group | The defined people a program intends to reach. | identify the target group
participant | A person taking part in a program activity. | count participants
reach | The extent of contact or participation within a defined population. | document program reach
needs assessment | A structured examination of priorities, gaps, and existing resources. | conduct a needs assessment
community input | Perspectives and knowledge supplied by the affected community. | incorporate community input
barrier | A factor that obstructs access, participation, or progress. | identify barriers
enabling condition | A circumstance that helps a proposed pathway work. | assess enabling conditions
indicator | A defined measure used to track a relevant condition or result. | select an indicator
baseline | A reference measurement taken before or at the start of a comparison. | establish a baseline
follow-up | Later contact or measurement after an activity. | arrange follow-up
sustained employment | Employment continuing for a defined period under a specified measure. | define sustained employment
learning question | A specific question guiding evidence collection and improvement. | frame a learning question''',
    precision='Two hundred distinct participants is a verified reach figure in this case. It is not an employment count. Keep the achievement, the measurement period, and the unit intact instead of upgrading participation into a result the records do not contain.',
    precision_extra='A theory of change makes the expected pathway and its assumptions explicit. It does not prove the pathway works. Application skills, actual applications, job opportunities, and employment duration need their own definitions and evidence rather than inference from attendance.',
    phrases='''Recognize the achievement | Two hundred distinct participants attended this quarter.
Name the evidence | That figure comes from checked registration records.
Limit the claim | It measures participation, not lasting employment.
Explain the intended pathway | We expect workshops to support stronger application skills.
Keep the link tentative | That is the proposed pathway, not a demonstrated result.
Name the next step | We need evidence of skill use and later employment.
Define the endpoint | What duration will we mean by sustained employment?
Identify an assumption | The pathway assumes relevant job opportunities are available.
Include community knowledge | Participants can help identify barriers that the workshop design misses.
Avoid an impact shortcut | Attendance alone does not establish the longer-term effect.
Preserve the useful result | We can report the reach confidently without overstating the outcome.
Correct the donor wording | Remove proof of lasting employment improvement from this update.
Ask about measurement | Which indicator would show the next step in the pathway?
Separate ambition from evidence | The mission describes what we seek, not what this quarter's records prove.
Plan proportionate follow-up | We should define the purpose and appropriate process before collecting more information.
Close the revision | State what we measured, what we hope to change, and what remains to be tested.''',
    notes='''Distinct participants | Counts people once, as established by the checked records.
Measures ... not | Names the boundary of the evidence.
We expect | Describes an intended mechanism without claiming it has been verified.
What duration | Turns a vague long-term label into a definable measure.
Assumes | Identifies a planning condition needing examination.
Remains to be tested | Keeps the learning task visible rather than presenting a hope as a finding.''',
    d='''Which donor sentence is supported? | Two hundred distinct people attended this quarter; lasting employment outcomes have not yet been measured. | Two hundred people now have lasting jobs because of the project. | Every attendance proves a successful employment outcome. | The project eliminated local unemployment. | The supported sentence preserves the verified reach and explicitly identifies the unmeasured endpoint.
What does the proposed pathway do? | Explains how workshops might lead to skills, applications, and sustained employment. | Certifies that every link has already occurred. | Replaces follow-up evidence with a diagram. | Guarantees jobs despite local labor-market conditions. | A pathway explains the expected mechanism and assumptions, not the actual completion of every step.
Which question makes sustained employment more measurable? | What period and employment definition will the indicator use? | Can we leave lasting undefined so it sounds stronger? | Should we count repeat visits as different jobs? | Can the donor's enthusiasm replace follow-up? | A defined duration and employment measure make the intended endpoint interpretable and testable.
Which factor is an enabling condition rather than a verified workshop result? | Availability of relevant job opportunities | The checked count of 200 participants | The completed registration review | The recorded quarter of participation | Job availability may help the pathway work, but the attendance record does not establish it as an outcome.''',
    dialogue='''Nina | The donor update says two hundred people attended our workshops, proving lasting employment improvement. The participation figure is checked, but the last phrase worries me.
Joel | The [[reach::Reach describes the verified extent of participation; the checked count does not establish later employment or its duration.]] is worth reporting. Two hundred distinct people attended this quarter. That is a real achievement, but the records do not tell us what happened to their employment afterward.
Nina | I do not want the correction to make the workshops sound pointless. The team has put a great deal into delivering them.
Joel | We can acknowledge the [[activity::Activity is the work delivered, such as the workshops, which remains valuable to describe without claiming an unmeasured effect.]] without overstating the evidence. Describe what we delivered and who participated, then distinguish the result we hope the work will support.
Nina | Our idea is that better application skills lead to better applications and eventually to employment that lasts.
Joel | That is a [[theory of change::Theory of change explains the expected route to a result, including assumptions that still need evidence.]]. It makes the expected route understandable, but it does not prove that every link has occurred because people attended a session.
Nina | Then we should show the steps between the workshop and the longer-term aim rather than jump straight from attendance to jobs.
Joel | Yes, the [[results chain::Results chain lays out the connected steps between resources, activities, and intended results rather than skipping intermediate changes.]] helps separate those steps. We need to know whether people developed the intended skills, used them in applications, and later obtained relevant work.
Nina | Some participants have told us that suitable jobs are difficult to find locally. That could affect the route even if their applications improve.
Joel | Job availability is an [[enabling condition::Enabling condition is a circumstance that helps the proposed pathway work; workshop attendance does not establish its presence.]] to examine. We should not imply that the workshop controls every labor-market factor or that a participant is responsible for every barrier they encounter.
Nina | We also use lasting and sustained as if they have an obvious meaning. We have not agreed a period.
Joel | Define [[sustained employment::Sustained employment needs a specified duration and employment measure, not an undefined claim that a job lasts.]] before presenting it as a measured result. A job reported once and employment maintained for a defined period are different pieces of information.
Nina | We could plan a later check, but we should be clear about why we need the information and how it will be handled.
Joel | A proportionate [[follow-up::Follow-up collects information after the activity under an appropriate process, addressing later results absent from registration records.]] can address that gap. Define the purpose, measure, timing, and appropriate participation and information-handling arrangements before collecting extra personal details.
Nina | What should the current update say while that work is still being designed?
Joel | Report participation as the observed result and describe the intended [[outcome::Outcome is the change sought for participants; here later employment has not yet been measured and must remain an intended result.]] as an aim. Remove the phrase proving lasting employment improvement, because it claims evidence that this quarter's attendance record does not contain.
Nina | I will keep the two-hundred-person figure and explain the proposed skills-to-employment pathway separately, with the assumptions visible.
Joel | Include a [[learning question::Learning question directs the next evidence task, such as whether participants use the skills, without presuming the answer.]] about whether participants use the application skills. That gives the team a practical next evidence task instead of treating the diagram as proof.
Nina | The donor can then see both the achievement and the remaining work, without assuming the program has already demonstrated its long-term effect.
Joel | Exactly. Our [[mission::Mission describes the organization's purpose and intended contribution, not a finding established by one quarter of participation records.]] remains ambitious. The reporting becomes more credible when it states what we measured, what we seek to change, and which links still need to be tested.''',
    transfer_title='Keep another participation claim accurate',
    transfer_setup='A mentoring project records 90 distinct participants in April. It has not measured later qualifications. Its proposed pathway links mentoring to study habits and then course completion.',
    transfer='''Lead: "The verified number of distinct participants is ___." | 90 | Ninety distinct participants is the count explicitly supported by the project record.
Officer: "The measurement period is ___." | April | April defines the period covered by this participation figure.
Lead: "The proposed intermediate change is ___." | study habits | The stated pathway links mentoring to study habits before the intended course-completion result.
Officer: "Later qualifications have ___." | not been measured | No qualification follow-up exists, so participation cannot be presented as proof of that outcome.''',
))


BOOK['units'].append(unit(
    title='Grant Proposals and Donor Restrictions',
    scene='Mission fit does not change the grant agreement',
    skill='Request a grant variation by distinguishing organizational purpose, permitted expenditure, and the approval needed before spending.',
    brief='Grant N14 provides $30,000 for after-school reading sessions and approved reading materials. There is $6,000 unspent. Program manager Amir proposes moving $3,000 to a food-outreach activity. Grants officer Leah checks the signed agreement: spending on a different activity requires a written amendment signed by the authorized representatives before commitment. A donor contact has informally called the food idea worthwhile, but no amendment exists. Amir and Leah must prepare a specific variation request without treating unspent money, mission alignment, or informal encouragement as permission to redirect the grant.',
    cast='Amir | Program manager\nLeah | Grants officer',
    culture=('Separate enthusiasm from authorization', 'Donors and staff may support an idea without having approved its funding. Acknowledge the shared aim, then name the award restriction and the actual change process. A clear request makes it easier to respond without forcing a friendly comment into a contractual commitment.'),
    a='''What activity does N14 currently fund? | After-school reading sessions and approved reading materials | Any activity the organization supports | Food outreach without an amendment | All staff travel regardless of purpose | The signed agreement limits this award to the stated reading activities and materials.
What does the proposed $3,000 transfer require? | A written amendment signed by authorized representatives before commitment | Only the fact that $6,000 remains | An informal positive comment from any donor contact | A revised internal spreadsheet after spending | The agreement expressly requires the authorized written amendment before committing to another activity.
What has the donor contact actually done? | Called the idea worthwhile without approving an amendment | Signed the required amendment | Removed all award restrictions | Approved every future food-outreach cost | Informal encouragement is recorded, but the specified amendment and its authorization are absent.''',
    vocabulary='''restricted grant | Funding limited to specified uses or conditions. | review the restricted grant
unrestricted funding | Funding available for the organization's permitted purposes without the stated donor-use restriction. | seek unrestricted funding
award agreement | The document setting the grant's terms and responsibilities. | check the award agreement
permitted expenditure | Spending allowed under the relevant terms. | verify permitted expenditure
purpose restriction | A limit specifying the activity or aim for which funds may be used. | observe the purpose restriction
unspent balance | Award money not yet spent, which may still carry restrictions. | reconcile the unspent balance
budget line | A specific category in an approved budget. | identify the budget line
budget transfer | Movement of an allocation between budget categories or activities. | request a budget transfer
variation request | A request to change an agreed scope, budget, or condition. | submit a variation request
amendment | An authorized change to an existing agreement. | execute an amendment
authorized representative | A person empowered to act for an organization in the relevant matter. | identify authorized representatives
prior approval | Permission obtained before the specified action is taken. | obtain prior approval
commitment | An action creating an obligation or promise to use resources. | avoid an unauthorized commitment
concept note | A concise description of a proposed project or change. | prepare a concept note
funding rationale | The explanation supporting a request for financial support. | clarify the funding rationale
deliverable | A specified output or item promised under an agreement. | revise the deliverables
award period | The time span during which the grant's defined work or costs apply. | check the award period
milestone | A defined stage used to track delivery. | update the milestones
reporting obligation | A requirement to provide specified information to the funder. | meet reporting obligations
donor contact | The person communicating with the organization on the donor's behalf. | confirm the donor contact
delegated authority | Decision power assigned to a person or role within defined limits. | verify delegated authority
mission alignment | Consistency with the organization's overall purpose. | explain mission alignment
funding gap | A shortfall between required and available permitted resources. | identify the funding gap
approval record | Documentation of the decision and its authorized scope. | retain the approval record''',
    precision='Unspent does not mean unrestricted. The $6,000 retains the agreement\'s restrictions, and the proposed transfer is half that balance. The signed N14 terms, not a general view that the new activity is worthwhile, determine the stated approval requirement.',
    precision_extra='A donor contact may communicate enthusiasm without holding the relevant signing authority. Here the process requires an amendment signed by authorized representatives before commitment. An internal budget change or later explanation cannot substitute for that specified approval.',
    phrases='''Acknowledge the need | The food-outreach idea addresses a real program concern.
Identify the restriction | N14 currently funds reading sessions and approved reading materials.
State the balance | Six thousand dollars remains unspent.
Limit the inference | Unspent funds are not automatically available for another activity.
Quantify the request | We propose reallocating three thousand dollars.
Check the agreement | The signed terms require a written amendment before commitment.
Separate encouragement | The donor contact's positive comment is not the required approval.
Confirm authority | Who is authorized to sign the amendment for each organization?
Describe the change | The request should state the new activity, amount, timing, and delivery effect.
Preserve the original promise | Explain how the change would affect the reading-program deliverables.
Avoid premature spending | Do not commit the proposed amount while approval is pending.
Record the status | The variation has been requested, not approved.
Check the full conditions | We also need to review the award period and reporting implications.
Offer another route | We can assess other permitted funding without assuming it is available.
Close the request | Ask for a clear decision on the specified variation.
Retain the evidence | Keep the executed amendment with the award and approval records.''',
    notes='''Currently funds | Identifies the agreement's present scope.
Not automatically | Blocks an inference from unused cash to spending authority.
Before commitment | Sets the required sequence between approval and obligation.
Positive comment ... not approval | Distinguishes relational support from the specified formal act.
Would affect | Describes the proposed consequences while the change remains undecided.
Requested, not approved | Keeps the decision status visible in internal and donor communications.''',
    d='''Which statement about the balance is accurate? | The $6,000 remains subject to N14's terms. | The $6,000 becomes unrestricted at quarter-end automatically. | Any unspent amount can fund food outreach. | Half the balance can always be moved without review. | The existence and size of the unused balance do not remove the agreement's restrictions.
What should the variation request include? | Amount, purpose, timing, and effects on agreed deliverables | Only a statement that the team likes the idea | A claim that approval already exists | A completed purchase followed by a request | A specific proposal gives the authorized parties the information needed to assess the actual change.
Which message overstates the donor contact's response? | The donor approved the amendment by calling the idea worthwhile. | The contact expressed support for the idea. | We still need the authorized signatures. | No executed amendment is on file. | A favorable informal comment does not satisfy the agreement's specified signed-amendment requirement.
What is the supported spending status? | Do not commit the transfer until the required amendment is executed. | Spend first because the purpose is charitable. | Change the ledger after payment to create permission. | Treat mission alignment as delegated signing authority. | The fictional agreement requires the authorized amendment before commitment to a different activity.''',
    dialogue='''Amir | We have six thousand dollars left in N14. Could we use three thousand for the food-outreach activity instead of leaving the money unused?
Leah | First check the [[purpose restriction::The restriction limits N14 to reading work; mission fit alone does not permit food outreach.]]. The signed agreement funds after-school reading sessions and approved reading materials. Food outreach is a different activity, even if it fits our wider mission.
Amir | The donor contact said the idea was worthwhile when I mentioned it last week. I took that as a positive sign.
Leah | It is encouraging, but [[mission alignment::Mission alignment concerns organizational purpose, not permission to redirect this restricted award.]] and informal support do not change the award terms. We need to distinguish liking the proposal from authorizing this grant to pay for it.
Amir | What does the agreement actually require if we want to move part of the remaining balance?
Leah | A [[written amendment::The agreement requires this signed formal change before commitment to the different activity.]] signed by the authorized representatives before commitment to a different activity. We do not have that amendment, so the proposed transfer is not approved.
Amir | I had thought an unspent amount was easier to move because it had not yet been used for the reading sessions.
Leah | The [[unspent balance::The unused money retains its grant restrictions; remaining unspent does not make it general-purpose funding.]] still carries the grant conditions. Six thousand remaining tells us the amount unused, not the purposes for which we may now spend it.
Amir | Then I should prepare a request for three thousand and explain why we want to change the activity.
Leah | Yes, a specific [[variation request::The request seeks an authorized change; submitting it does not itself approve the transfer.]]. Include the amount, proposed work, timing, and the effect on the reading-program commitments, so the donor can assess the actual change rather than a vague idea.
Amir | We would need to explain whether fewer reading sessions or fewer materials would result. I should not leave the original promise untouched on paper.
Leah | Exactly. Show the effect on each relevant [[deliverable::A deliverable is an agreed output; the proposed transfer must explain effects on the reading-program promises.]]. The donor needs a truthful picture of what would change and what would remain, not two incompatible sets of promises.
Amir | Can the contact who encouraged the idea sign the amendment, or does it need someone else?
Leah | We must verify the [[authorized representative::The representative needs the relevant signing power; a familiar donor contact may not hold it.]] for each organization. A familiar contact may help route the request without holding the signing authority needed to approve it.
Amir | The food team wants to reserve supplies today. Would a small deposit be acceptable while we wait?
Leah | Do not create a [[commitment::A deposit may obligate resources, so the required amendment must precede that commitment.]] from this proposed transfer while approval is pending. A deposit can still obligate resources. We should not promise the funds before the specified process is complete.
Amir | I will tell them that the variation is being requested, not that the donor has approved it. We can also check other funding options.
Leah | That is the right status. Any alternative [[permitted expenditure::Another funding source has its own terms, which also need checking before use.]] needs its own review under the relevant source. We should not solve one restricted-funding problem by assuming another pot has no conditions.
Amir | Once the decision arrives, I will update the activity plan and the reporting arrangements to match the approved position.
Leah | Retain the [[approval record::The record documents the authorized terms, distinguishing an executed amendment from encouragement or a pending request.]] and executed amendment with N14. Then the program and finance teams can act on the same documented terms rather than different memories of a conversation.''',
    transfer_title='State another proposed grant variation',
    transfer_setup='Award L8 funds adult-literacy classes. Of $8,000 unspent, the team proposes $2,000 for a transport activity. Its signed terms require a written amendment before commitment. No amendment has been signed.',
    transfer='''Manager: "The existing funded activity is ___." | adult-literacy classes | The award's current purpose is adult literacy, not the proposed transport activity.
Officer: "The unspent balance is ___." | $8,000 | Eight thousand dollars remains unused but still subject to the award's terms.
Manager: "The proposed transfer is ___." | $2,000 | Two thousand dollars is the amount requested for the different activity.
Officer: "The required approval document is a ___." | written amendment | The stated terms require this document before commitment, and no signed amendment exists.''',
))

BOOK['units'].append(unit(
    title='Monitoring, Evaluation, and Learning',
    scene='The scores improved, but the cause is not isolated',
    skill='Report a before-and-after result with the correct population, measurement limits, and a proportionate learning conclusion.',
    brief='A budgeting-skills program enrolls 75 adults. Sixty complete both the initial and final version of the same 100-point knowledge test. Their mean score rises from 40 to 58, an 18-point increase. Fifteen enrollees lack a paired result. There is no comparison group, and practice effects, outside learning, and reasons for missing results have not been examined. Evaluation officer Priya and program manager Dan must report the improvement among paired completers without presenting it as a proven program effect, a result for all 75 enrollees, or evidence that household finances have improved.',
    cast='Priya | Evaluation officer\nDan | Program manager',
    culture=('Learning can begin before causal proof', 'A useful result need not be dismissed because it does not establish causation. Describe the observed change precisely, disclose the missing information, and identify what the team can learn next. Avoid treating methodological limits as either proof of failure or permission to exaggerate success.'),
    a='''Which group has the paired score result? | Sixty people who completed both tests | All seventy-five enrollees | Only fifteen people missing a test | A separate comparison group | Sixty participants supplied both initial and final scores, allowing the paired comparison.
What is the observed mean-score change? | An increase of 18 points, from 40 to 58 | An increase of 58 points | An 18-percentage-point employment gain | No change | Subtracting forty from fifty-eight gives an eighteen-point increase on the stated knowledge test.
What is not established? | A causal effect on household finances | An increase in the paired group's mean test score | Fifteen enrollees lacking paired results | The absence of a comparison group | The study measures knowledge scores and does not establish either program causation or household financial improvement.''',
    vocabulary='''MEL | Monitoring, evaluation, and learning; connected functions for tracking and improving work. | strengthen the MEL approach
monitoring | Routine tracking of defined activities, conditions, or results. | conduct program monitoring
evaluation | Systematic assessment of an intervention and its results or value. | commission an evaluation
learning agenda | A set of priority questions guiding inquiry and adaptation. | define the learning agenda
paired observation | Measurements from the same person or unit at two points. | analyze paired observations
pretest | A measurement taken before the relevant instruction or activity. | administer the pretest
posttest | A measurement taken after the relevant instruction or activity. | review posttest results
mean score | The arithmetic average of scores in a defined group. | calculate the mean score
score point | One unit on a specified scoring scale. | report a score-point change
completer | A participant who finishes the defined measurement or program steps. | identify paired completers
missing data | Information absent from the expected measurement record. | assess missing data
attrition | Loss of participants or observations between stages. | examine attrition
comparison group | A group used to help assess what might occur without the same intervention. | define a comparison group
counterfactual | The unobserved or estimated result without the intervention. | assess the counterfactual
practice effect | Improvement from familiarity with a test rather than the intended learning alone. | examine practice effects
confounding factor | Another influence that complicates interpretation of a relationship. | investigate confounding factors
selection bias | Distortion caused by how people enter or remain in the analyzed group. | assess selection bias
causal attribution | Assignment of an observed change to a specific cause. | support causal attribution
contribution | A role an intervention plays in a result, without necessarily being the only influence. | examine the program's contribution
triangulation | Comparison of different sources or methods to examine a finding. | use triangulation
validity | How well a measure or inference supports its intended interpretation. | assess validity
reliability | Consistency of measurement under relevant conditions. | check reliability
behavioral outcome | A measured change in what people do, rather than only what they know. | measure behavioral outcomes
adaptive management | Adjusting program decisions in response to evidence and learning. | support adaptive management''',
    precision='The mean rose by 18 points on a 100-point test among the same 60 paired completers. That is not an employment percentage or a result for every enrollee. Missing paired results for 15 of 75 mean 20% lack that comparison.',
    precision_extra='A before-and-after improvement can have several explanations. Reusing a test may introduce familiarity, and people who complete both tests may differ from those missing a result. These are issues to examine, not proven explanations or reasons to discard the observed change.',
    phrases='''State the measured group | Sixty participants completed both tests.
State the result | Their mean score increased from forty to fifty-eight.
Use the correct unit | The observed increase is eighteen score points.
Disclose the missing group | Fifteen enrollees lack a paired result.
Avoid broadening the population | We cannot apply the paired result to all seventy-five enrollees.
Name the design limit | There was no comparison group.
Keep alternatives open | Practice effects and outside learning have not been examined.
Avoid causal overstatement | The change alone does not isolate the program's effect.
Keep the result visible | The observed improvement is still useful to report.
Separate knowledge from behavior | A test score does not establish better household financial behavior.
Ask about missingness | Why are the paired results missing for those fifteen people?
Check the measure | Does the test assess the skills the program intends to develop?
Use multiple sources carefully | We can compare test findings with other appropriate evidence.
Plan the next inquiry | The learning agenda should address the key alternative explanations.
Avoid a false choice | We do not have to choose between proven success and no value.
Close the finding | Report the change, analyzed group, missing data, and limits together.''',
    notes='''Their mean | Ties the statistic to the paired-completer group.
Score points | Names the test-scale unit rather than a percentage of employment outcomes.
Lack a paired result | Identifies the missing comparison without inventing its cause.
Have not been examined | Keeps alternative explanations open rather than declaring them proven.
Does not isolate | Limits the causal conclusion while preserving the observation.
Still useful | Recognizes the information value of a bounded finding.''',
    d='''Which finding is accurate? | The mean score among 60 paired completers rose from 40 to 58. | All 75 participants improved their finances by 18%. | The program alone caused an 18-point gain. | The missing 15 participants had no learning. | The accurate statement keeps the observed scores and analyzed group without inventing causation or missing outcomes.
What proportion lacks a paired result? | 20% of enrollees | 15% of enrollees | 80% of enrollees | 25% of enrollees | Fifteen divided by seventy-five equals one fifth, or twenty percent.
How should practice effects be described? | A possible influence that has not yet been examined | A proven explanation for the entire gain | An impossible influence because the test is numerical | Evidence that every score is false | Reusing the same test makes familiarity a relevant possibility, but no analysis has established its contribution.
Which next conclusion is justified? | Investigate missing results and alternative explanations while retaining the bounded finding. | Claim improved household finances from the test alone. | Assume a comparison group would definitely show no effect. | Discard every result because the design has limits. | The evidence supports a precise observation and further inquiry, not an all-or-nothing judgment about success.''',
    dialogue='''Dan | The final knowledge scores look encouraging. Can we say the budgeting program improved everyone's financial skills by eighteen points?
Priya | We need to define the [[paired observations::Paired observations compare the same participants at both times; only sixty enrollees supplied that complete measurement pair.]] first. Sixty people completed both tests. Their average moved from forty to fifty-eight, but fifteen of the seventy-five enrollees do not have a paired result.
Dan | Then the eighteen-point improvement belongs to those sixty people as a group, not automatically to everyone who enrolled.
Priya | Correct. It is a change in the [[mean score::Mean score is the arithmetic average for the defined group; its change does not establish that every individual improved equally.]]. It does not mean that each person gained exactly eighteen points or that the missing participants had the same result.
Dan | Should we call it an eighteen-percent improvement because the test is marked out of one hundred?
Priya | Use eighteen [[score points::Score points identifies the units on the test scale, avoiding confusion with a relative percentage change or another outcome.]]. That is the direct subtraction of forty from fifty-eight on this scale. If we add a relative percentage, it needs its own clear baseline and explanation.
Dan | The missing fifteen are a fifth of enrollment. We need to know why their paired results are absent.
Priya | Yes, examine the [[missing data::Missing data covers the absent paired results; the reasons and possible effects on interpretation remain unknown.]]. We should not assume they learned nothing, or that they improved just as much. Their absence may affect how well the analyzed group represents the full intake.
Dan | We used the same questions before and after. Some of the gain could come from familiarity rather than the teaching alone.
Priya | A [[practice effect::Practice effect is improvement associated with test familiarity; it is a possible influence here, not an established explanation for the whole gain.]] is one possibility to examine. Outside learning is another. We have not tested those explanations, so we should neither ignore them nor claim they account for the entire change.
Dan | There was no other group taking the test without the program. Does that limit what we can say about the cause?
Priya | The absence of a [[comparison group::Comparison group can help examine what might happen without the same intervention; none is available in this design.]] is an important design limit. The before-and-after result alone does not show what would have happened over the same period without this program.
Dan | I want to avoid presenting the data as useless simply because the design cannot answer every question.
Priya | We can report the improvement while limiting [[causal attribution::Causal attribution assigns the change to the program; the available before-and-after observations do not isolate that effect.]]. A bounded observation is useful. It is not the same as proving that the program caused all of the gain.
Dan | And higher knowledge scores do not necessarily mean people changed how they manage household money.
Priya | Exactly. A [[behavioral outcome::Behavioral outcome measures what people do; the knowledge test does not directly establish changes in household financial behavior.]] needs its own measure. We have not demonstrated improved household finances, reduced debt, or sustained behavior from this test result.
Dan | We could examine missingness, review the test, and compare the findings with other appropriate evidence before redesigning the sessions.
Priya | That gives us a focused [[learning agenda::Learning agenda organizes the next questions, including missingness, measurement quality, and plausible alternative explanations.]]. Keep the questions tied to decisions the team needs to make, and use an appropriate process for collecting any further participant information.
Dan | I will revise the report to say the mean rose from forty to fifty-eight among sixty paired completers, with the missing results and design limits alongside.
Priya | Good. That supports [[adaptive management::Adaptive management uses evidence and acknowledged limits to improve decisions, without requiring exaggerated claims of proven success.]]. We can improve the program and its evaluation without turning an encouraging observation into a causal claim that the current design cannot support.''',
    transfer_title='Report another paired-score result',
    transfer_setup='A program enrolls 50 people. Forty complete both tests, with a mean rising from 55 to 67 on a 100-point scale. Ten lack paired data. No comparison group is available.',
    transfer='''Manager: "The paired-completer group contains ___." | 40 people | Forty participants have both measurements and therefore belong in the paired comparison.
Analyst: "The observed mean-score gain is ___." | 12 points | Sixty-seven minus fifty-five equals twelve points on the stated test scale.
Manager: "The number lacking paired data is ___." | 10 people | Ten of the fifty enrollees do not have the complete before-and-after result.
Analyst: "The proportion lacking paired data is ___." | 20% | Ten divided by fifty equals twenty percent, which limits the completeness of the paired analysis.''',
))


BOOK['units'].append(unit(
    title='Field Operations and Partner Coordination',
    scene='A partner changes the visit, but the community has not agreed',
    skill='Coordinate a date change by separating partner availability, community confirmation, transport arrangements, and the final go-ahead.',
    brief='The RiverLink field visit was arranged for 10 October. A partner now requests 12 October and confirms that its own team can attend then. The community contact has not been consulted about the change, and transport remains booked for 10 October. Community liaison Nadia and logistics officer Ben must establish whether the new date works before treating it as agreed. Ben will check transport availability and any change cost by 15:00 local time. Nadia will consult the community contact and update the coordinator by 16:00. Neither has authority to approve additional spending independently.',
    cast='Nadia | Community liaison\nBen | Logistics officer',
    culture=('Coordination includes the people receiving the visit', 'A change agreed between organizations may still inconvenience the community or exclude people who arranged their time around the original visit. Ask whether the revised date works and explain what is pending. Silence or receipt of a message is not automatically agreement.'),
    a='''Who has confirmed availability on 12 October? | The partner's team only | The community contact and every participant | The transport provider | The spending approver | The partner has confirmed its own availability, while community and transport arrangements remain unresolved.
What remains booked for 10 October? | Transport | The revised community meeting | A confirmed visit on 12 October | A new accommodation package | The brief explicitly states that the transport booking still uses the original date.
What may Ben and Nadia approve independently? | Neither may approve additional spending. | Any change cost under the original booking | The community's agreement | Every partner's final attendance | The stated authority limit requires additional spending to follow the relevant approval route.''',
    vocabulary='''field visit | An organized visit to a program location. | coordinate a field visit
community liaison | Communication and relationship work with an affected community. | maintain community liaison
implementing partner | An organization carrying out agreed program work. | coordinate with the implementing partner
availability | Whether a person or resource can be used at a specified time. | confirm availability
proposed date | A date suggested but not necessarily agreed. | circulate the proposed date
confirmed date | A date accepted through the required coordination process. | communicate the confirmed date
itinerary | The planned sequence of places, times, and activities for a visit. | update the itinerary
transport booking | An arrangement reserving transport for stated requirements. | amend the transport booking
rescheduling | Moving an activity to another time or date. | coordinate rescheduling
change fee | A charge associated with altering an arrangement. | verify the change fee
cancellation term | A condition governing cancellation and its consequences. | check cancellation terms
lead time | The time needed between a request and its delivery. | allow sufficient lead time
dependency | A condition another activity relies on. | identify a scheduling dependency
focal point | The designated contact for a particular function or relationship. | contact the focal point
notification | A message informing someone of an event or change. | send a notification
acknowledgment | Confirmation that a message has been received. | request acknowledgment
confirmation | An explicit statement that an arrangement or fact is agreed or established. | obtain confirmation
handover | Transfer of responsibility and relevant information. | complete the handover
action owner | The person responsible for a specified next step. | name the action owner
decision deadline | The time by which an identified decision is needed. | set a decision deadline
contingency | An alternative arrangement for a possible difficulty. | agree a contingency
access requirement | A condition needed for someone to participate or reach a location. | check access requirements
coordination log | A record of arrangements, owners, and current status. | update the coordination log
go-ahead | Authorization to proceed with an agreed action. | obtain the go-ahead''',
    precision='The partner is available on 12 October, but the visit is not yet confirmed for that date. Keep availability, community agreement, transport feasibility, and spending authority separate. A message sent or acknowledged does not establish all four.',
    precision_extra='Ben owes a transport check by 15:00; Nadia owes a coordinator update by 16:00, both local time. Those are information deadlines, not promises that transport will change or the visit will proceed. State any pending dependency in the update.',
    phrases='''Name the original arrangement | The visit and transport were arranged for the tenth.
Identify the proposed change | The partner is asking to move the visit to the twelfth.
Limit the confirmation | Only the partner's team has confirmed that date.
Include the community | We still need to ask whether the revised date works for the community.
Distinguish receipt from agreement | An acknowledgment tells us the message arrived, not that the date is accepted.
Check the booking | Transport is still booked for the original date.
Check feasibility | Can the provider accommodate the proposed change?
Check cost | Please identify any change fee before we request approval.
Respect authority | We cannot approve additional spending ourselves.
Assign the action | I will check transport availability and terms.
Set the update time | I will report the transport position by fifteen hundred local time.
Keep the status provisional | Please label the twelfth as proposed, not confirmed.
Avoid an early cancellation | Do not cancel the original arrangement before the coordinated decision.
Name a dependency | The revised itinerary depends on community confirmation and transport.
Report an unresolved item | Community availability is still pending at this update.
Close the loop | Once the go-ahead is recorded, send the same confirmed details to everyone.''',
    notes='''Only | Limits a confirmation to the party that actually gave it.
Still need | Identifies an outstanding step without blaming anyone.
Acknowledgment | Describes receipt rather than acceptance.
Before approval | Keeps the cost check ahead of an unauthorized commitment.
Proposed, not confirmed | Prevents a tentative arrangement being circulated as final.
Once | Makes the final notification conditional on the recorded decision.''',
    d='''Which status message is accurate? | The partner is available on 12 October; community confirmation and transport checks are pending. | The entire visit is confirmed for 12 October. | The community agreed because an email was sent. | Transport has moved automatically with the partner's calendar. | The accurate message distinguishes the one confirmed availability from the two outstanding coordination tasks.
Which question should Nadia ask? | Does 12 October work for the community, including relevant access arrangements? | Why did you reject a date you have not received? | Can we treat silence as agreement? | Will you pay an unapproved transport charge? | Nadia needs an explicit availability discussion, not an assumption based on silence or an unreceived proposal.
What should Ben report by 15:00? | Transport availability, change terms, and any cost requiring approval | A guaranteed visit regardless of other confirmations | The community's decision on Nadia's behalf | A payment authorization he does not hold | Ben owns the transport check and should report its findings within his stated authority.
Which action closes coordination properly? | Record the go-ahead and circulate consistent confirmed details to all relevant contacts. | Send different dates to different parties. | Leave the original booking unchanged without telling anyone. | Cancel first and ask about community availability afterward. | A recorded decision and consistent notifications align the community, partner, and practical arrangements.''',
    dialogue='''Nadia | The partner has asked to move RiverLink from the tenth to the twelfth. Their team can make the new date, but I have not spoken with the community contact.
Ben | Then the twelfth is still the [[proposed date::Proposed date distinguishes the suggested change from a visit confirmed through all the required coordination steps.]]. The partner's availability does not tell us whether the community can attend or whether the practical arrangements can move with them.
Nadia | Exactly. Some people may have already rearranged their work for the original visit. I need to ask whether the change is workable.
Ben | Please include any relevant [[access requirements::Access requirements identify practical participation needs that a revised date or arrangement may affect.]] in that conversation. A different date could alter who can take part, even if the meeting place remains the same.
Nadia | I will contact the community focal point now. I do not want an email delivery receipt to become our evidence that everyone agreed.
Ben | An [[acknowledgment::Acknowledgment confirms receipt of a message, not acceptance of the date or completion of the coordination process.]] is useful, but it is not the same as acceptance. Record the actual response and any conditions rather than simply marking the communication complete.
Nadia | What is the current transport position? Has the booking moved because the partner changed its calendar?
Ben | No, the [[transport booking::Transport booking remains a separate arrangement for 10 October; the partner's calendar change does not amend it automatically.]] is still for the tenth. I will ask the provider about availability on the twelfth and the terms for changing the reservation.
Nadia | There could be an extra charge. We should know that before telling the partner that the revised arrangements are settled.
Ben | I will check the [[change fee::Change fee is a possible cost of altering the reservation; it needs verification and the relevant spending approval.]] and any other relevant terms. Neither of us can approve additional spending, so I will identify what needs to go to the authorized approver.
Nadia | When can you give the coordinator that information? The partner is waiting for a response, and we need a realistic next update.
Ben | I am the [[action owner::Action owner names the person responsible for the transport check, making the next step traceable rather than leaving it to everyone.]] for transport. I will report availability and terms by fifteen hundred local time, even if the provider has not yet confirmed every detail.
Nadia | I will update the coordinator by sixteen hundred local time after contacting the community. If I have not received a response, I will say that clearly.
Ben | Good. Put those updates in the [[coordination log::Coordination log records the current status, responsible people, and outstanding arrangements so teams work from the same information.]]. The deadline is for an accurate status report, not a promise that the revised visit will definitely be approved by then.
Nadia | Should we cancel the original transport now so that we do not forget it later?
Ben | Not before the coordinated [[go-ahead::Go-ahead is the required authorization to proceed; cancellation should not get ahead of the decision and its dependencies.]]. First establish the consequences and the decision route. Otherwise we could lose the original arrangement without having a workable replacement.
Nadia | Once the community responds and you have the transport position, the coordinator can assess the complete picture rather than two separate assumptions.
Ben | Then we can update the [[itinerary::Itinerary sets out the agreed visit details; it should reflect the recorded decision rather than a provisional calendar change.]] from the recorded decision. Everyone should receive the same date, meeting details, and responsibilities, including any remaining conditions that affect the visit.
Nadia | I will tell the partner that their availability is noted, but community confirmation and transport checks are still pending.
Ben | That keeps each [[dependency::Dependency identifies an outstanding condition, such as community agreement or transport, on which the revised visit relies.]] visible. We can move quickly without describing a one-party preference as a fully agreed field visit.''',
    transfer_title='Coordinate another proposed visit change',
    transfer_setup='A partner proposes moving a visit from 18 to 20 November. Transport remains booked for the eighteenth. Liaison Omar will seek community confirmation; logistics officer Mei will check transport by 14:00 local time.',
    transfer='''Coordinator: "The proposed new date is ___." | 20 November | The twentieth is proposed by the partner, not yet confirmed through the full coordination process.
Mei: "The existing transport date is ___." | 18 November | The transport booking remains on the original date until an authorized change is arranged.
Omar: "My outstanding task is ___." | community confirmation | Omar must establish whether the revised date works for the community rather than assume acceptance.
Mei: "My transport update is due at ___." | 14:00 local time | This is the stated deadline for the transport check, not a guarantee that the visit proceeds.''',
))


BOOK['units'].append(unit(
    title='Safeguarding and Incident Reporting',
    scene='Receive the concern without conducting your own investigation',
    skill='Respond calmly to a concern, distinguish reported information from direct observation, and explain the designated reporting route without promising secrecy.',
    brief='Volunteer Elena tells manager Sam that a participant reported a worker threatening to withdraw support unless the participant did a private favor. Elena did not witness the interaction and does not know whether there is an immediate danger. The fictional organization requires concerns to be passed promptly through its secure safeguarding route, without waiting for proof. Its policy provides an independent alternate contact if the usual lead is implicated or unavailable. Immediate danger requires the relevant emergency route without delay. Sam must listen, clarify immediate safety needs, record the account accurately, and avoid investigating or confronting the worker.',
    cast='Elena | Volunteer reporting a concern\nSam | Receiving manager',
    culture=('Calm does not mean dismissive', 'A measured response can help someone continue reporting without feeling interrogated. Thank them, explain what will happen next, and be honest about information-sharing limits. Do not require certainty, promise a particular outcome, or turn the receiving conversation into a credibility test.'),
    a='''What did Elena directly witness? | She did not witness the reported interaction. | The worker making the alleged threat | A completed investigation | An emergency response | Elena is passing on a participant's account, not claiming to have seen the interaction herself.
Must Sam wait for proof before reporting? | No; the stated policy requires prompt reporting of concerns. | Yes; a concern needs a completed investigation first. | Yes; only a witness can report. | Yes; the worker must first admit the allegation. | The fictional policy requires concerns to enter the designated route without waiting for proof.
What should Sam establish promptly? | Whether there is an immediate safety need requiring the emergency route | Whether the allegation can be publicly announced | How to confront the worker alone | How to guarantee complete secrecy | Immediate safety needs affect the response route, while investigation and publicity are outside this receiving task.''',
    vocabulary='''safeguarding | Organizational work to prevent and respond to harm, abuse, and exploitation. | raise a safeguarding concern
concern | Information suggesting a possible problem that needs appropriate attention. | report a concern
disclosure | A person's communication of information about an experience or event. | receive a disclosure
allegation | A reported claim not yet established through the relevant process. | record an allegation
direct observation | Something a person personally saw or heard. | distinguish direct observation
reported account | Information communicated by another person. | attribute the reported account
immediate danger | A present threat requiring urgent action through the appropriate route. | assess immediate danger
designated lead | The person assigned responsibility for a defined safeguarding function. | contact the designated lead
alternate contact | A specified substitute reporting contact under the policy. | use the alternate contact
reporting route | The approved channel through which a concern is passed. | follow the reporting route
confidentiality | Limits on access to information under the applicable arrangements. | explain confidentiality
need-to-know basis | Sharing information only with those requiring it for the relevant task. | share on a need-to-know basis
secure channel | An approved communication method protecting sensitive information appropriately. | use a secure channel
factual record | An account separating known facts, sources, and uncertainties. | create a factual record
verbatim wording | The exact words used by a speaker. | preserve verbatim wording
inference | A conclusion drawn beyond what was directly stated or observed. | label an inference
retaliation | Harmful treatment in response to a report or other protected action. | report retaliation concerns
power imbalance | Unequal influence or control between people or groups. | recognize a power imbalance
coercion | Pressure or threats used to influence someone's actions. | report possible coercion
professional boundary | A limit defining appropriate conduct in a work relationship. | maintain professional boundaries
support referral | Connection to an appropriate source of assistance. | arrange a support referral
investigation | An authorized process to establish relevant facts. | preserve the investigation process
information minimization | Limiting information to what is necessary for the stated purpose. | apply information minimization
acknowledged receipt | Confirmation that the designated recipient received the concern. | obtain acknowledged receipt''',
    precision='Elena can report exactly what the participant told her while stating that she did not witness the interaction. That distinction does not make the concern unimportant. It preserves the source of the information without declaring the allegation proved or disproved.',
    precision_extra='Confidentiality is not a promise that nobody else will hear the account. Explain the necessary reporting and support process. If immediate danger is identified, follow the relevant emergency route without delaying for an ordinary report or waiting for a particular colleague.',
    phrases='''Welcome the report | Thank you for bringing this concern to me.
Check immediate safety | Is anyone in immediate danger or in need of urgent assistance?
Clarify the source | Did you witness the interaction, or are you describing what you were told?
Preserve the account | Please use the words you remember, without filling in missing details.
Distinguish uncertainty | We do not yet know whether the reported event occurred as described.
Avoid a proof threshold | You do not need to investigate before raising the concern.
Explain sharing | I cannot promise secrecy; I need to use the designated reporting route.
Limit circulation | I will share the necessary information with the people who need to act.
Use the secure route | I will pass this through the approved secure channel promptly.
Check the alternate | If the usual lead is implicated or unavailable, I will use the policy's alternate contact.
Avoid confrontation | Do not approach the worker to test the account yourself.
Keep roles clear | The authorized process will determine the next fact-finding steps.
Record without embellishment | I will separate what you observed from what the participant reported.
Preserve urgent action | Immediate danger requires the relevant emergency route without delay.
Avoid a promised outcome | I cannot predict the outcome, but I can explain the next reporting step.
Close responsibly | I will confirm that the designated recipient has received the concern.''',
    notes='''Thank you | Acknowledges the act of reporting without prejudging the allegation.
Did you witness | Clarifies the source, not whether the person deserves to be heard.
Words you remember | Requests accuracy without demanding invented certainty.
Cannot promise secrecy | Explains an important limit honestly.
Necessary information | Restricts circulation to the relevant purpose.
Authorized process | Keeps investigation responsibility with the designated people.''',
    d='''Which response is appropriate? | Thank you; let us check immediate safety and use the designated route. | Bring proof before anyone will listen. | I promise nobody else will ever hear this. | We should confront the worker immediately ourselves. | The appropriate response acknowledges the concern, addresses urgent safety, and follows the stated reporting process.
Which record preserves the source? | Elena reports that the participant described a threat; Elena did not witness it. | Sam witnessed the worker making a proven threat. | Every detail has already been independently verified. | No concern exists because Elena was not present. | The accurate record attributes the account and separates it from direct observation or an established finding.
What if the usual lead is implicated? | Use the independent alternate contact specified in the policy. | Send the allegation only to the implicated lead. | Abandon the concern because the normal route is unsuitable. | Publish the account to force a response. | The fictional policy explicitly provides an independent alternate route for this conflict.
Which promise should Sam avoid? | Complete secrecy and a guaranteed investigation outcome | Necessary information sharing through the designated route | Prompt reporting under the stated policy | An explanation of the next reporting step | Sam cannot guarantee either that nobody will need the information or what the authorized process will conclude.''',
    dialogue='''Elena | A participant told me that a worker threatened to withdraw support unless they did a private favor. I did not see the interaction, but I am worried.
Sam | Thank you for raising this [[concern::Concern identifies information needing appropriate attention without requiring Elena to prove the allegation before reporting it.]]. Before we discuss the account, do you know whether anyone is in immediate danger or needs urgent assistance now?
Elena | I do not know. The participant did not explain whether the worker is with them now, and I do not want to guess.
Sam | We need to clarify immediate safety through the appropriate process. Any [[immediate danger::Immediate danger requires the relevant emergency route without delay; uncertainty should not be converted into an unsupported assurance of safety.]] requires the relevant emergency route without delay, rather than waiting for our usual contact or an ordinary written report.
Elena | I was unsure whether I could report it because I only heard what the participant said. I cannot confirm what actually happened.
Sam | Your [[reported account::Reported account attributes the information to what the participant told Elena, distinguishing it from Elena's own observation.]] can still be passed on. State who told you what and make clear that you did not witness the interaction. Do not add certainty that you do not have.
Elena | I remember the phrase about losing support, but I cannot reproduce every word. Should I make the statement sound more complete?
Sam | No. Preserve any [[verbatim wording::Verbatim wording means exact remembered words; unclear or missing details must not be invented to make the account sound complete.]] you remember and identify the parts you are paraphrasing or unsure about. A polished reconstruction could accidentally change the meaning of the original account.
Elena | The participant seemed afraid of the worker finding out. Can I tell them that this will remain entirely between us?
Sam | Do not promise secrecy. Explain [[confidentiality::Confidentiality limits access under the relevant process but does not mean a concern can be withheld from everyone who must act.]] honestly: the necessary information must go through the designated process, with appropriate limits on who receives it and for what purpose.
Elena | I was going to ask the worker what happened so that I could give you both sides before making a report.
Sam | Please do not conduct an [[investigation::Investigation belongs to the authorized process; Elena should not confront the worker or collect competing accounts before reporting.]] yourself or confront the worker. Our policy does not require you to establish proof before reporting. The authorized people will decide the appropriate fact-finding steps.
Elena | I can provide the information I have through the designated channel. I should not put the participant's account into the general volunteer chat.
Sam | Correct. I will use the approved [[secure channel::Secure channel is the designated protected reporting method, not a general chat where sensitive information would circulate unnecessarily.]] promptly. The record will separate the participant's reported words, your own observations, and anything that remains unknown.
Elena | What happens if the usual safeguarding lead is unavailable, or if a concern involves that person?
Sam | Our policy specifies an independent [[alternate contact::Alternate contact provides the stated independent reporting route when the usual lead is implicated or unavailable.]] for those situations. We should use that route rather than abandon the report or send it only to someone whose involvement creates a conflict.
Elena | I also want to know what I can say if the participant asks what will happen to the worker.
Sam | Do not predict the outcome. Explain the next [[reporting route::Reporting route describes the approved next step that can be explained now, without guaranteeing an investigative finding or sanction.]] and appropriate support arrangements. We can be clear about the process without promising a finding, a sanction, or information we may not be able to share.
Elena | I will keep the account accurate and avoid discussing it with other volunteers. Please let me know that the concern reaches the right recipient.
Sam | I will obtain [[acknowledged receipt::Acknowledged receipt confirms that the designated recipient received the concern; it does not mean the allegation has been substantiated.]]. That confirms the handover, not the outcome. If new immediate safety information emerges, use the appropriate urgent route rather than waiting for a routine update.''',
    transfer_title='Identify the appropriate reporting steps',
    transfer_setup='Volunteer Hana reports what a participant told her; she did not witness the event. The usual lead is implicated. The fictional policy provides an independent alternate contact and a secure reporting channel. Immediate danger requires the relevant emergency route.',
    transfer='''Manager: "Your information is a ___, not a direct observation." | reported account | Hana describes information from the participant rather than an event she personally witnessed.
Hana: "Because the usual lead is implicated, we use the ___." | independent alternate contact | The stated policy provides this alternative for a concern involving the normal recipient.
Manager: "We send necessary details through the ___." | secure reporting channel | Sensitive information belongs in the designated channel rather than a general conversation.
Hana: "Immediate danger requires the relevant ___." | emergency route | Urgent safety needs must not wait for an ordinary handover or a particular colleague.''',
))


BOOK['units'].append(unit(
    title='Volunteer Management and Training',
    scene='An enthusiastic offer is not a driving authorization',
    skill='Acknowledge a volunteer contribution while maintaining role boundaries, explaining the approval process, and arranging authorized cover.',
    brief='Food-support volunteer Luis is approved for packing and stock counting. A driver becomes unavailable before a delivery, and Luis offers to drive the organization van. Coordinator Grace has no record that Luis has completed the organization-specific driving checks, assessment, or authorization. His ordinary driving experience does not replace those requirements. The fictional policy allows only currently authorized drivers to use the van. Grace must keep Luis within his approved role, contact the transport lead for authorized cover, and explain how he can request assessment for a future driving role without promising approval.',
    cast='Luis | Packing volunteer\nGrace | Volunteer coordinator',
    culture=('Appreciation and boundaries can coexist', 'A volunteer may interpret a refusal as distrust or ingratitude. Recognize the offer and explain the role-based requirement without making the person defend their character. Give an appropriate current task and a clear route to request a broader role later.'),
    a='''Which duties are currently approved for Luis? | Packing and stock counting | Driving the organization van | Assessing other drivers | Authorizing transport cover | The brief defines Luis's approved role as packing and stock counting only.
What does the fictional policy require for van use? | Current driver authorization | General confidence alone | Willingness to help | A busy delivery schedule | The policy restricts van use to currently authorized drivers, regardless of enthusiasm or schedule pressure.
What can Grace offer Luis now? | Continue approved duties and request assessment for a future driving role. | Immediate authorization without checks | A guaranteed assessment result | Permission to substitute his personal experience for the process | Grace can explain the development route while preserving the present authorization boundary.''',
    vocabulary='''role description | A statement of duties, responsibilities, and limits. | review the role description
volunteer agreement | A document setting out the organization's and volunteer's arrangements. | clarify the volunteer agreement
induction | Initial orientation to the organization and relevant work. | complete volunteer induction
onboarding | The process of preparing someone to join an organization or role. | improve volunteer onboarding
scope of role | The activities and responsibilities a role includes. | stay within the scope of role
role boundary | A limit separating authorized duties from other work. | maintain a role boundary
screening | Relevant checks used to assess suitability under the applicable process. | complete role-specific screening
competence | Demonstrated ability to perform a task appropriately. | assess competence
training completion | Finishing a specified training activity. | record training completion
competency assessment | Evaluation of whether someone can perform specified tasks appropriately. | arrange a competency assessment
authorization | Permission from the relevant authority to perform a task. | verify current authorization
supervision | Oversight and support for someone's work. | provide appropriate supervision
refresher training | Further training to maintain or update relevant knowledge and skills. | schedule refresher training
cover | A replacement arrangement when the usual person is unavailable. | arrange authorized cover
roster | A schedule assigning people to duties or shifts. | update the volunteer roster
shift coordinator | The person organizing duties during a particular work period. | contact the shift coordinator
transport lead | The person responsible for coordinating the relevant transport function. | notify the transport lead
task allocation | Assignment of work to people within relevant limits. | confirm task allocation
escalation route | The designated path for an issue needing another level of responsibility. | use the escalation route
availability notice | Information about when someone can or cannot work. | send an availability notice
reasonable adjustment | An appropriate change considered under applicable needs, duties, and policy. | discuss reasonable adjustments
feedback conversation | A discussion about performance, experience, or improvement. | arrange a feedback conversation
role expansion | A proposed increase in someone's authorized responsibilities. | request a role expansion
authorization register | A record showing who holds the relevant permission and its status. | check the authorization register''',
    precision='Experience, training completion, demonstrated competence, and authorization are related but distinct. Luis may have driving experience without holding permission to use this organization van. Finishing a course also need not complete every assessment or approval requirement.',
    precision_extra='An urgent delivery does not expand the authority of Grace or Luis. Grace should explain the limit, contact the transport lead, and keep useful approved work moving. The future assessment route is an opportunity to apply, not a promised authorization.',
    phrases='''Recognize the offer | Thank you for offering to cover the delivery.
State the current role | Your approved duties are packing and stock counting.
Separate experience from permission | Your driving experience does not establish authorization for this van.
Name the policy limit | Only currently authorized drivers may use the organization vehicle.
Avoid a personal judgment | This is a role requirement, not a judgment about your intentions.
Check the record | I need to verify the current authorization register.
Keep the task bounded | Please continue with the approved packing work.
Assign the escalation | I will contact the transport lead for authorized cover.
Avoid a shortcut | We cannot skip the required checks because the delivery is urgent.
Explain the development route | You can request assessment for a future driving role.
Distinguish training and approval | Completing training is not automatically the final authorization.
Avoid a guarantee | I cannot promise the assessment result or approval date.
Check support needs | We can discuss the arrangements needed for the assessment process.
Clarify supervision | Who will provide the required oversight for the approved task?
Keep the roster accurate | Update the roster only after the authorized arrangement is confirmed.
Close respectfully | Your help is valuable, and we need to use it within the agreed role.''',
    notes='''Thank you for offering | Recognizes a contribution before explaining the boundary.
Approved duties | Names the work currently permitted.
Does not establish | Separates one credential from a different permission.
Not a judgment | Prevents a process requirement sounding like a personal accusation.
Can request | Offers a route without promising the outcome.
Only after | Keeps the record aligned with the actual authorization.''',
    d='''Which response respects both Luis and the policy? | Thank you; I will seek authorized cover while you continue the approved packing work. | You seem confident, so the checks no longer matter. | Drive now and complete the records afterward. | A good volunteer would ignore the boundary. | The response acknowledges the offer and keeps both the delivery and Luis's work within the stated role limits.
What does finishing a training course establish by itself? | Completion of that course, not necessarily final authorization | Permission for every organization vehicle | Completion of all possible suitability checks | A guaranteed assessment pass | Training completion documents a learning step but does not automatically satisfy separate assessment and authorization requirements.
Who should Grace contact for replacement transport? | The transport lead | An unrelated donor to waive the policy | Luis alone to approve himself | The community to certify his driving | The brief assigns the authorized-cover route to the transport lead rather than the volunteer or an unrelated party.
Which future-role statement is accurate? | You may request assessment, but approval is not guaranteed. | Asking makes you authorized immediately. | Personal experience replaces every organization-specific check. | The delivery deadline guarantees a pass. | A request starts the specified development process without determining its result.''',
    dialogue='''Luis | I heard that the driver is unavailable. I have driven vans before, so I could take this delivery and keep the schedule moving.
Grace | Thank you for offering. Your current [[scope of role::Luis is approved for packing and stock counting; driving is outside those current duties.]] covers packing and stock counting. I do not have a record that you are authorized to drive our organization vehicle.
Luis | I understand that it is outside my usual tasks, but I have plenty of ordinary driving experience. Is that not enough for a short trip?
Grace | Experience is relevant, but the [[authorization::Authorization is current organizational permission; ordinary driving experience does not replace the required approval.]] is separate. Our policy permits only currently authorized drivers to use the van, even for a short delivery or when the normal driver is unavailable.
Luis | I do not want to make things difficult. The team is waiting, and I thought offering would solve the immediate problem.
Grace | Your offer is helpful. Maintaining this [[role boundary::The boundary limits permitted duties without judging the volunteer's intentions or willingness to help.]] is not a judgment about your intentions. We need to arrange the delivery through the appropriate person while keeping your approved work moving.
Luis | Is there a list you can check, or does the decision depend on who happens to be coordinating the shift?
Grace | We use the [[authorization register::The register establishes current permission rather than relying on an improvised judgment of confidence.]]. I need a current record, not an assumption based on familiarity or confidence. Nothing in your current role record establishes the required driving approval.
Luis | Then who can arrange another driver? I can finish the packing while you find out.
Grace | I will contact the [[transport lead::The transport lead is responsible for arranging authorized cover; Luis cannot approve himself.]] for authorized cover. We may need to revise the delivery arrangement, but urgency does not give either of us permission to bypass the requirement.
Luis | I would like to help with driving in future. Could we make that part of my role instead of having this problem again?
Grace | You can request a [[role expansion::Role expansion requests broader duties but requires the relevant assessment and approval before permission.]]. I can explain the organization-specific checks, assessment, and decision process. I cannot promise that the request will be approved or give you an approval date today.
Luis | If I complete the training, would that mean I can start driving on the next shift?
Grace | Not necessarily. [[Training completion::Finishing training establishes course completion; separate assessment and authorization requirements may still remain.]] is one step. We must also establish which assessment and approval requirements remain, rather than treating a course certificate as permission to undertake every task.
Luis | So the assessment is about demonstrating the required ability, and the final authorization records permission to take on the duty.
Grace | Exactly. The [[competency assessment::The assessment checks demonstrated ability against task requirements, rather than merely recording training attendance.]] checks the relevant task requirements. The process should also explain what support or appropriate adjustments can be discussed, without promising a particular result.
Luis | For today, I will stay with packing and stock counting. Please tell me if there is another task within my current role that would help.
Grace | I will confirm the [[task allocation::Task allocation keeps Luis working within his approved duties while transport cover is arranged.]] for this shift. That lets us use your help effectively while the transport lead handles the replacement arrangement and any necessary schedule change.
Luis | Once another driver is confirmed, I can help the team prepare the correctly labeled packages for collection.
Grace | Good. We will update the [[roster::The roster should record confirmed authorized cover, not an offer from an unapproved driver.]] after the authorized cover is confirmed. We can also arrange a separate conversation about your interest in the driving role, without confusing that future request with today's permission.''',
    transfer_title='Keep another volunteer within an approved role',
    transfer_setup='Maya is approved for reception duties, not home visits. She offers to visit a client alone when a colleague cancels. The coordinator must seek authorized cover and can explain the future role-assessment process, without guaranteeing approval.',
    transfer='''Coordinator: "Your current approved work is ___." | reception duties | The stated role permits reception work, not an unapproved independent home visit.
Maya: "Today's replacement arrangement needs ___." | authorized cover | The canceled visit must be addressed through appropriately authorized staff or volunteers.
Coordinator: "A future expanded role requires the ___." | role-assessment process | A request for broader duties must follow the stated assessment route before permission is assumed.
Maya: "Applying does not mean that approval is ___." | guaranteed | The coordinator can explain the process but cannot promise its eventual outcome.''',
))


BOOK['units'].append(unit(
    title='Advocacy, Public Messaging, and Neutrality',
    scene='An alarming headline changes the meaning of an old survey',
    skill='Challenge an unsupported public claim, preserve the original population and time frame, and distinguish policy advocacy from party endorsement.',
    brief='Fundraiser Maya drafts a headline: one in three local children is hungry tonight. Communications officer Theo traces the number to a fictional 2018 regional survey of 80 self-selected adult respondents. Twenty-seven reported concern about having enough food during the previous month. The survey did not measure current hunger among local children, and its representativeness is unknown. The organization permits evidence-based policy advocacy but has its own nonpartisan rule against endorsing parties. Maya and Theo must remove or accurately qualify the statistic, retain a clear mission-focused request, and avoid unsupported urgency or partisan endorsement.',
    cast='Maya | Fundraiser\nTheo | Communications officer',
    culture=('Urgency does not require distortion', 'A fundraising message can be forceful without changing who was measured or when. Separate the emotional force of the issue from the strength of the evidence. A precise correction can protect the mission and the dignity of the people described, not merely reduce legal or reputational exposure.'),
    a='''Who answered the original survey? | Eighty self-selected adult respondents in the region | All local children | A representative national child sample | Every current service user | The source population is the stated self-selected adult respondent group, not local children.
What did 27 respondents report? | Concern about enough food during the previous month | Verified hunger among children tonight | Current food deprivation across the whole town | A diagnosis made by the organization | The original question concerned respondents' past-month food concerns, not the headline's different population and time frame.
What does the organization's own policy allow? | Evidence-based policy advocacy without party endorsement | Endorsement of any party that supports the mission | Replacement of evidence with an urgent headline | Treating all NGOs as legally identical | The fictional policy distinguishes advocacy about issues from endorsing political parties.''',
    vocabulary='''advocacy | Communication seeking change in policy, practice, or public attention. | support evidence-based advocacy
public messaging | Communication intended for an external audience. | review public messaging
fundraising appeal | A request for financial or other support. | prepare a fundraising appeal
claim substantiation | Evidence supporting what a statement asserts. | check claim substantiation
source attribution | Identifying where information came from. | provide source attribution
survey population | The defined group a survey concerns. | describe the survey population
respondent | A person who provides answers to a survey. | count survey respondents
self-selection | Entry into a sample through people's own decision to participate. | disclose self-selection
representativeness | How well a sample reflects the relevant wider population. | assess representativeness
denominator | The total quantity used as the base of a proportion. | identify the denominator
time frame | The period to which a measurement or claim refers. | preserve the time frame
question wording | The exact phrasing used to collect a survey response. | check question wording
historical finding | A result referring to an earlier period. | label a historical finding
extrapolation | Extending a finding beyond the observations or population measured. | avoid unsupported extrapolation
qualifier | Wording that specifies the limits or conditions of a statement. | add a material qualifier
headline | The prominent title summarizing a message. | revise the headline
call to action | A clear request for what an audience should do next. | state the call to action
nonpartisan | Not supporting or opposing political parties under the relevant meaning or policy. | maintain a nonpartisan position
party endorsement | An expression of support for a political party. | avoid party endorsement
policy position | An organization's stated view on a public issue or proposed measure. | explain the policy position
informed consent | Agreement based on relevant information about the proposed use or action. | obtain informed consent
dignity | Respect for a person's worth and agency. | preserve participant dignity
editorial approval | Authorization of material through the relevant publication process. | obtain editorial approval
correction notice | A statement identifying and correcting published misinformation. | issue a correction notice''',
    precision='Twenty-seven of eighty is 33.75%, roughly one third of those respondents. That arithmetic does not validate the headline. Adults are not children, the region is not necessarily the local area, past-month concern is not measured hunger tonight, and the sample is not established as representative.',
    precision_extra='Naming a source does not repair a claim that changes its meaning. If the historical finding is used, its population, method, date, and actual question need visible context. Removing an unsuitable statistic may produce a clearer appeal than attaching a long footnote to a misleading headline.',
    phrases='''Pause publication | This headline needs an evidence check before release.
Trace the figure | What is the original source for one in three?
Name the population | The survey involved eighty self-selected adult respondents.
Restore the date | The finding comes from a regional survey in two thousand eighteen.
Restore the question | Respondents reported concern about enough food during the previous month.
Reject the population change | That does not establish current hunger among local children.
Keep arithmetic separate | The proportion is roughly one third, but the headline still changes the claim.
Question extrapolation | We do not know whether these respondents represent the wider population.
Avoid attribution as a shield | Adding a source name does not make the revised claim accurate.
Choose a clear correction | Remove the statistic or state the historical finding with its essential limits.
Retain the request | We can make a clear call to action without inventing a current prevalence figure.
Explain advocacy | We can argue for a policy change using appropriately supported evidence.
Maintain the policy boundary | Our nonpartisan rule does not permit endorsing a party.
Respect story ownership | Check informed consent and the intended use before publishing someone's story.
Protect dignity | Describe people as individuals with agency, not as fundraising props.
Close the review | Approve wording that is accurate in the headline as well as the supporting text.''',
    notes='''Original source | Directs the check to the underlying measurement.
That does not establish | Rejects an unsupported inference without denying the issue exists.
Roughly one third | Describes the calculation, not wider representativeness.
Essential limits | Identifies context that changes how a result should be understood.
Without inventing | Keeps the appeal strong while respecting the evidence boundary.
Our rule | Refers to this organization's policy rather than a universal rule for NGOs.''',
    d='''Which statement accurately reflects the source? | In the 2018 regional survey, 27 of 80 self-selected adult respondents reported past-month food concerns. | One in three local children is hungry tonight. | All families in the country lack food. | The survey proves the current cause of child hunger. | The accurate statement preserves the source's date, respondents, quantity, and actual measured concern.
Does adding a citation rescue the original headline? | No; attribution does not correct its changed population and time frame. | Yes; any attributed statement is accurate. | Yes; the date can be hidden. | Yes; respondents and children are interchangeable. | A citation identifies a source but cannot make a claim faithful when its meaning has been altered.
Which advocacy sentence fits the stated nonpartisan rule? | We support the proposed access reform on the evidence, without endorsing a party. | Donate only if you vote for our preferred party. | Our mission automatically exempts us from our own rule. | Every nonprofit worldwide must adopt our exact policy. | The fictional rule allows issue-based advocacy while withholding party endorsement.
What should accompany use of a participant story? | The relevant consent and dignity checks for its intended publication | An assumption that receiving support means agreeing to publicity | A more alarming invented detail | Removal of the participant's agency | Responsible publication requires the relevant consent and respectful representation, not automatic permission derived from service use.''',
    dialogue='''Maya | The appeal headline says one in three local children is hungry tonight. It is powerful, but I need the original source before we send it.
Theo | I traced the [[source attribution::Source attribution identifies the original survey but does not, by itself, make a changed or exaggerated headline accurate.]] to a regional survey from two thousand eighteen. It involved eighty adult respondents, not a survey of local children or a current count of hunger.
Maya | The number came from twenty-seven responses out of eighty. That is roughly one third, so is the calculation at least correct?
Theo | The [[denominator::Denominator is the eighty respondents used to calculate the proportion; it is not the number of local children or all regional adults.]] supports that approximate proportion among respondents. But correct arithmetic cannot fix a change in who was measured, what they were asked, or when the finding applies.
Maya | What did the question actually ask? The draft has been shortened several times, and I am concerned that the meaning changed.
Theo | The [[question wording::Question wording concerned enough food during the previous month, which differs from a measure of children experiencing hunger tonight.]] concerned whether respondents had worried about having enough food during the previous month. It did not establish that children were hungry on a particular night.
Maya | And we cannot turn a finding from two thousand eighteen into a claim about tonight without current evidence.
Theo | Correct. The [[time frame::Time frame limits the finding to the earlier survey and its past-month reference, not a current condition tonight.]] is material to the meaning. We need to restore it if we use the result, rather than place an old date in a footnote under a current-sounding headline.
Maya | Do we know how the eighty people were selected? I do not want to imply that they represent every household in the region.
Theo | They joined through [[self-selection::Self-selection means people chose to respond; representativeness of the wider population has not been established from this sample.]]. We do not know whether they represent the wider population. The result describes those respondents, and the method limits how far we can extend it.
Maya | So adding the source name would not rescue the original headline. It would still make a different claim from the underlying finding.
Theo | Exactly. That would remain unsupported [[extrapolation::Extrapolation extends the respondent finding to a different population or present condition without evidence supporting that extension.]]. Either remove the statistic or state the historical result with its essential limits. A citation is not permission to change the evidence.
Maya | A fully qualified historical finding may be too cumbersome for the headline. I would rather remove it and explain the work clearly.
Theo | We can retain a strong [[call to action::Call to action asks for support clearly without needing an invented or misrepresented current prevalence statistic.]]. State the support being requested and the work it will fund, using verified facts. Urgency should come from the actual need, not a claim we cannot substantiate.
Maya | The appeal also supports an access reform. A colleague thinks our nonpartisan rule means we cannot discuss any policy issue.
Theo | Our [[policy position::Policy position states a view on an issue; the organization's stated rule allows evidence-based advocacy distinct from party endorsement.]] can support an evidence-based reform. This organization's rule separates issue advocacy from endorsing parties; it does not require silence on every public policy question.
Maya | We also have a participant story available. I will check whether the proposed fundraising use is covered, rather than assume service participation gives permission.
Theo | Check [[informed consent::Informed consent concerns the proposed use of the person's story; receiving support does not automatically authorize fundraising publication.]] and the intended use, and preserve the person's dignity. Do not add an alarming detail simply because it might make the appeal more compelling.
Maya | I will remove the unsupported headline, keep a clear request, and send the revised wording through the publication process.
Theo | Then [[editorial approval::Editorial approval should cover the corrected headline and supporting text, ensuring both communicate the verified claim consistently.]] can address the actual message as a whole. The headline, story, policy position, and supporting evidence should tell a consistent account that we can defend.''',
    transfer_title='Keep a survey claim within its evidence',
    transfer_setup='A 2020 survey of 60 self-selected adult service users found 18 reported transport difficulties in the previous month. It did not measure current difficulties among all city residents.',
    transfer='''Editor: "The survey year is ___." | 2020 | The result is historical and cannot be relabeled as a current measurement.
Analyst: "The denominator is ___." | 60 respondents | Sixty adult service users answered, not the entire city population.
Editor: "The proportion reporting difficulties is ___." | 30% | Eighteen divided by sixty equals thirty percent of these respondents.
Analyst: "The question's reference period was the ___." | previous month | The stated survey question concerned the preceding month, not conditions today.''',
))


BOOK['units'].append(unit(
    title='Board Reporting and Sustainability',
    scene='Cash in the account is not all available for the shortfall',
    skill='Explain restricted cash, available funds, a simplified runway calculation, and the board decision needed before using a reserve buffer.',
    brief='Harbor Outreach has $180,000 cash. Of this, $120,000 is restricted to a separate program and cannot fund the operating shortfall in this scenario. The remaining $60,000 is unrestricted and available after other commitments. Net unrestricted cash outflow is assumed to remain $20,000 each month. A proposed $50,000 donation is not confirmed and has no payment date. The board has set its own reserve floor at $20,000. Finance lead Asha and board chair Peter must distinguish three months to cash exhaustion from two months to that floor, then request a decision on options and review triggers.',
    cast='Asha | Finance lead\nPeter | Board chair',
    culture=('Give the board a decision, not a reassuring total', 'A large bank balance can hide a shortage in the funds available for a particular purpose. Present the usable amount, assumptions, timing, and authority clearly. A concise choice with consequences and a review date is more useful than a confident headline that combines incompatible funding categories.'),
    a='''How much is available for this operating shortfall? | $60,000 | $180,000 | $120,000 | $230,000 | The scenario excludes the restricted $120,000 and identifies the remaining $60,000 as available after other commitments.
How long until the stated reserve floor is reached? | Two months under the constant-outflow assumption | Nine months | Three months to the floor | Five months because the donation is confirmed | Sixty thousand less the twenty-thousand floor leaves forty thousand, covering two months at twenty thousand monthly outflow.
How should the proposed donation be treated? | As unconfirmed, without an assumed receipt date | As cash already in the bank | As permission to use restricted funds | As a guaranteed cure for the shortfall | Neither confirmation nor payment timing exists, so the proposal must not be treated as available cash.''',
    vocabulary='''board paper | A document presenting information or a decision for a governing board. | prepare a board paper
restricted fund | Resources limited to specified purposes under the applicable terms. | respect restricted funds
unrestricted fund | Resources not subject to a specified external purpose restriction. | distinguish unrestricted funds
available funds | Resources usable for the stated purpose after relevant restrictions and commitments. | identify available funds
reserve policy | An organization's approach to holding and using a financial buffer. | explain the reserve policy
reserve floor | A defined lower threshold under the organization's policy. | monitor the reserve floor
free reserves | Unrestricted resources available to spend after relevant exclusions. | assess free reserves
cash balance | Money held in the stated accounts at a point in time. | reconcile the cash balance
net cash outflow | Cash paid out minus cash received over a specified period. | forecast net cash outflow
cash runway | The estimated period before defined available cash is exhausted under stated assumptions. | calculate cash runway
liquidity | Ability to meet payments when they fall due. | monitor liquidity
funding gap | A shortfall between available funding and required resources. | explain the funding gap
pledge | A promise or indication of future support, with its status and terms specified. | verify a donor pledge
forecast assumption | A condition used when projecting future figures. | disclose forecast assumptions
sensitivity analysis | Examination of how a result changes when assumptions change. | run a sensitivity analysis
scenario planning | Comparing defined possible future conditions and responses. | use scenario planning
drawdown | Use of an available balance over time. | authorize a reserve drawdown
designated fund | Unrestricted resources earmarked internally, subject to the applicable governance rules. | explain a designated fund
commitment | An obligation or planned use relevant to available resources. | account for existing commitments
cost reduction | A decrease in spending with its timing and consequences specified. | evaluate a cost reduction
service continuity | Ability to maintain the relevant service over time. | protect service continuity
decision authority | The right to approve a specified action. | confirm decision authority
review trigger | A defined event or threshold requiring reconsideration. | set a review trigger
replenishment plan | An approach for rebuilding a used financial buffer. | agree a replenishment plan''',
    precision='The simplified runway is $60,000 divided by $20,000: three months to exhaust available cash if the assumption holds. Reaching the $20,000 reserve floor takes only two months. Nine months incorrectly treats the full $180,000 bank balance as usable for this shortfall.',
    precision_extra='Available cash and accounting reserves are not automatically identical in real organizations. Here the case explicitly states the usable amount after commitments. The board floor is this organization\'s own threshold, not a universal target. Unconfirmed future support should not silently become cash in the base calculation.',
    phrases='''Separate the categories | Of the cash balance, one hundred twenty thousand is restricted to another program.
State the usable amount | Sixty thousand is available for this shortfall after other commitments.
State the assumption | We assume net unrestricted outflow remains twenty thousand a month.
Calculate exhaustion | On that assumption, available cash lasts three months.
Name the earlier threshold | We reach the board's twenty-thousand reserve floor after two months.
Reject the misleading total | Nine months would incorrectly include restricted money.
Keep support provisional | The proposed donation is unconfirmed and has no payment date.
Separate scenarios | Show the donation scenario separately from the base case.
Explain uncertainty | The timing and amount of future receipts could change the projection.
Make the decision explicit | The board needs to choose an authorized response before the threshold is reached.
Describe a cost option | State when the saving begins and which services it affects.
Avoid relabeling | We cannot remove a funding restriction by changing an internal label.
Check authority | Which decision can management take, and which requires the board?
Set the trigger | Review the plan if receipts or outflows depart from the stated assumptions.
Plan recovery | A drawdown proposal should explain how the buffer could be rebuilt.
Close the report | Report the available amount, time to floor, options, and next decision date together.''',
    notes='''For this shortfall | Ties availability to a specific permitted purpose.
After commitments | Prevents the usable figure from overlooking existing obligations.
On that assumption | Makes the forecast conditional rather than certain.
Earlier threshold | Distinguishes policy-floor timing from cash exhaustion.
Separately | Prevents an uncertain donation from being hidden inside the base case.
When and which | Makes a cost option concrete about timing and service consequences.''',
    d='''Which runway statement is accurate? | Three months to exhaustion and two months to the reserve floor under the stated assumption | Nine months to exhaustion using all cash | Three months to the floor and two to exhaustion | Unlimited runway because a donation is proposed | The usable sixty thousand covers three monthly outflows, while only forty thousand can be used before reaching the floor.
Which presentation handles the proposed $50,000 appropriately? | Show it as a separate unconfirmed scenario with uncertain timing. | Add it to today's available cash. | Assume it arrives before the next payment. | Treat its proposed amount as an authorized grant transfer. | Separate scenario reporting preserves uncertainty about both whether the support will arrive and when.
What is wrong with relabeling the restricted $120,000 as operating reserves? | An internal label does not remove the stated restriction. | A board paper automatically changes donor terms. | A large balance cannot be restricted. | Restricted means already spent. | The stated purpose restriction remains in force regardless of the name used in an internal report.
What makes a cost-reduction option decision-ready? | Timing, expected savings, service effects, authority, and a review trigger | A saving amount with no start date or consequences | A promise that every service stays unchanged without evidence | A generic instruction to be more sustainable | The board needs the operational consequences and decision conditions as well as the estimated financial benefit.''',
    dialogue='''Peter | The board summary shows one hundred eighty thousand dollars in cash. At twenty thousand a month, does that mean we have nine months to solve the shortfall?
Asha | Not for this purpose. One hundred twenty thousand is a [[restricted fund::Restricted fund money is limited to the separate program and cannot cover this operating shortfall under the stated facts.]] for a separate program. We cannot include it in the amount available to cover this operating gap.
Peter | Then what amount can we actually use, after accounting for the other obligations already identified?
Asha | The [[available funds::Available funds are the sixty thousand explicitly usable for this shortfall after the stated restrictions and other commitments.]] are sixty thousand dollars. The paper for the board needs to start with that figure, not the total bank balance, so the timing is not falsely reassuring.
Peter | The current projection assumes that the available balance falls by twenty thousand each month. Does that already allow for normal receipts?
Asha | Yes, it is [[net cash outflow::Net cash outflow is payments less receipts over the period; the stated twenty-thousand monthly amount drives this simplified projection.]], not just gross spending. We are assuming it stays at twenty thousand a month. That assumption should remain visible wherever we show the forecast.
Peter | Sixty divided by twenty gives three months. We should distinguish that from the board's twenty-thousand lower threshold.
Asha | Correct. The simplified [[cash runway::Cash runway is three months to exhausting the sixty-thousand available balance, assuming the twenty-thousand monthly net outflow continues.]] to exhaustion is three months. But the board's own reserve floor is reached earlier, after forty thousand has been used, which is two months.
Peter | So the floor is a decision threshold under our policy, not a claim that every organization needs the same amount in reserve.
Asha | Exactly. Our [[reserve policy::Reserve policy establishes this organization's own threshold; the twenty-thousand floor is not a universal requirement for every nonprofit.]] sets that threshold. We should not wait until the third month and then act surprised that we passed the board's floor a month earlier.
Peter | There is also a proposed fifty-thousand donation. Some board members may assume that it already removes the gap.
Asha | The [[pledge::Pledge language must identify the proposed support as unconfirmed with no payment date, rather than treating it as money already available.]] is not confirmed and has no payment date. Show that possible receipt in a separate scenario, not as cash already available in the base calculation.
Peter | We need options that explain more than a number. A reduction could take time to implement or affect services differently.
Asha | A [[cost reduction::Cost reduction needs a start date and service consequences to support a real decision, not only an estimated saving.]] should show when savings begin, the effect on services, and any relevant commitments. An immediate-looking saving is misleading if the outflow changes only after several months.
Peter | Another option may involve using part of the buffer under an approved plan. We would need to explain the authority and recovery path.
Asha | Any proposed [[drawdown::Drawdown uses the relevant available buffer and needs the appropriate authority; it does not permit spending the separate restricted program funds.]] needs the appropriate decision and its conditions. It does not authorize us to relabel the restricted program money or assume that an uncertain donation will restore the balance.
Peter | Let us include a point at which the board revisits the plan if receipts are late or the outflow is higher.
Asha | Set a clear [[review trigger::Review trigger specifies when changed receipts, outflows, or thresholds require reconsideration instead of leaving the response undefined.]], alongside the next decision date. That turns the forecast into a monitored plan rather than a single reassuring number presented without conditions.
Peter | I will ask for a paper showing the available amount, two-month threshold, three-month exhaustion point, and the consequences of each authorized option.
Asha | Include a [[replenishment plan::Replenishment plan explains how a used buffer could be rebuilt, with assumptions identified rather than a guaranteed future donation.]] where a buffer would be used. The board should see what would rebuild it and which assumptions still need confirmation before choosing a response.''',
    transfer_title='Explain another usable buffer',
    transfer_setup='An organization has $150,000 cash: $90,000 restricted to another purpose and $60,000 available after commitments. Net outflow is assumed constant at $15,000 monthly. Its own reserve floor is $30,000. Ignore unconfirmed future donations.',
    transfer='''Chair: "Cash available for this shortfall is ___." | $60,000 | The ninety-thousand restricted amount is excluded, leaving sixty thousand available after commitments.
Officer: "Monthly net outflow is ___." | $15,000 | The scenario states this constant monthly assumption for the simplified projection.
Chair: "Time to exhaust the available cash is ___." | four months | Sixty thousand divided by fifteen thousand gives four months to exhaustion under the assumption.
Officer: "Time to reach the reserve floor is ___." | two months | Sixty thousand less the thirty-thousand floor leaves thirty thousand, covering two monthly outflows.''',
))
