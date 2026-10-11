"""Original consulting engagement cases for the English Ladder learner book."""
from books.authoring import unit

BOOK = dict(
    slug='consulting', title='Consulting English',
    cover_label='ENGLISH FOR CLIENT ENGAGEMENTS',
    cover_title='Consulting', cover_size=38,
    tagline='Clarify the question.\nMake the recommendation usable.',
    audience='For consultants, engagement managers, analysts, client-facing specialists, and internal advisory teams.',
    map_intro='Eight client-engagement lessons, from defining the decision and testing hypotheses to managing scope, preparing adoption, and recording the steering committee\'s actual decision.',
    notes_title='A clear point of view. A traceable basis.',
    notes_intro='Consultants need to be concise without disguising uncertainty, helpful without promising unlimited scope, and confident without treating a working hypothesis as a fact. These cases practice the language of real client work, from the first discovery conversation to the final decision.',
    field_notes=[
        ('Ask what the work will decide', 'A requested analysis is often a means, not the business decision itself. Clarify the choice, owner, criteria, and deadline before collecting a large amount of information.', '"What decision should the benchmarking study help you make?"'),
        ('Test the attractive explanation', 'A plausible story can organize analysis, but it must remain open to evidence against it. Separate a proposed explanation from an established finding.', '"Price is a working hypothesis; we have not yet ruled out service or competitor changes."'),
        ('Make the implication visible', 'Executives need to know why a finding matters for their choice. Connect the evidence to a bounded recommendation and an explicit request, without hiding material limitations in supporting pages.', '"The evidence supports a limited pilot, not a full rollout today."'),
        ('Own revisions without inventing agreement', 'A missed constraint deserves a direct acknowledgment and a revised analysis. A positive discussion does not equal approval, and agreement on the problem does not settle the option.', '"We agree on the problem, but the preferred option remains undecided."'),
    ],
    scope_note='All clients, engagements, people, figures, contracts, policies, and decisions are fictional. This is professional English practice, not legal, financial, statistical, or implementation advice. Real decisions require the applicable evidence, contractual terms, approvals, and qualified review. The cited organizations do not endorse this book.',
    sources=[
        dict(title='McKinsey. How to master the seven-step problem-solving process (2019).', url='https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-to-master-the-seven-step-problem-solving-process', note='Background on problem definition, analytical priorities, and synthesis. The cases and language examples are original, not a reproduction of the interview.', checked='1 October 2026'),
        dict(title='Association for Project Management. What is change control?', url='https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/', note='Terminology distinguishing a requested baseline change from an evaluated and authorized change. Fictional engagement terms supply the exercise decisions.', checked='1 October 2026'),
        dict(title='Association for Project Management. What is change management and organisational change?', url='https://www.apm.org.uk/resources/what-is-project-management/what-is-change-management/', note='Background on organizational adoption and sustained change. Training, practice, ownership, and readiness details in the scenarios are invented.', checked='1 October 2026'),
        dict(title='American Society for Quality. What is the Plan-Do-Check-Act cycle?', url='https://asq.org/quality-resources/pdca-cycle', note='Background on small-scale testing and learning before wider change. Pilot thresholds and choices are fictional, not a prescribed professional method.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Client Discovery and Problem Definition',
    scene='The requested study is not the decision',
    skill='Turn a request for benchmarking into an agreed decision question with boundaries, criteria, and an owner.',
    brief='Client sponsor Rita asks consultant Owen for a benchmark of support-center costs. During discovery, she explains that the executive committee must decide by 30 November whether to centralize the North and South support centers or retain them separately. The comparison must address total operating cost, response time, and service continuity, including transition effects. Staffing and customer-impact data are not yet available. Centralization has not been approved. Owen must define the decision and evidence needs before treating a peer cost comparison as a recommendation to close either site.',
    cast='Rita | Client sponsor\nOwen | Engagement lead',
    culture=('Clarification can be a form of service', 'Questioning a requested deliverable can sound obstructive if it is detached from the client objective. Explain how the clarification makes the work more useful, then confirm the decision in the client language. Avoid implying that the sponsor asked a foolish question.'),
    a='''What must the executive committee decide? | Whether to centralize the two centers or retain them separately | Which center has already been approved for closure | Whether benchmarking is forbidden | Which consultant should approve staffing changes | The stated choice is centralization versus separate operation; no closure or staffing decision has been approved.
When is the decision needed? | By 30 November | After an unspecified annual review | Immediately without evidence | Only after both sites close | The brief gives 30 November as the executive committee's decision deadline.
Which criteria belong in the comparison? | Cost, response time, and service continuity, including transition effects | Peer cost alone | Only the presentation length | Only the consultant's preferred operating model | The sponsor explicitly requires three criteria and transition effects, not a cost-only benchmark.''',
    vocabulary='''discovery | Early inquiry to understand the client situation and decision. | conduct client discovery
problem statement | A precise description of the question or issue to address. | refine the problem statement
decision question | The choice that the analysis is intended to support. | define the decision question
client sponsor | The client representative supporting and directing the engagement within their role. | align with the client sponsor
decision owner | The person or body authorized to make the relevant choice. | identify the decision owner
benchmark | A reference used for a defined comparison. | establish a benchmark
peer group | Organizations or units selected for comparison. | define the peer group
comparability | The degree to which a comparison uses sufficiently similar definitions and conditions. | assess comparability
operating model | How an organization arranges people, processes, systems, and responsibilities. | compare operating models
centralization | Concentrating specified activities or authority in a common location or structure. | evaluate centralization
decentralization | Distributing specified activities or authority across units. | assess decentralization
baseline | The defined starting position used for comparison. | establish the baseline
decision criterion | A factor used to evaluate alternatives. | agree decision criteria
constraint | A limit that an option must respect or explicitly address. | surface a constraint
service continuity | Maintaining the required service through an operating change. | assess service continuity
transition cost | A cost associated with moving from one arrangement to another. | estimate transition costs
steady-state cost | Cost after a defined transition has settled. | compare steady-state costs
response time | Elapsed time to provide a specified response. | define response time
stakeholder map | A representation of relevant parties and their interests or roles. | build a stakeholder map
in scope | Included in the agreed work boundaries. | confirm what is in scope
out-of-scope | Excluded from the agreed work boundaries. | identify out-of-scope work
success measure | A defined indicator of whether the intended result has been achieved. | agree success measures
engagement charter | A document summarizing purpose, boundaries, roles, and arrangements. | confirm the engagement charter
decision deadline | The date or time by which a choice is needed. | work to the decision deadline''',
    precision='A benchmark compares selected measures against a reference group. It does not itself decide the operating model. Different service hours, case complexity, or cost definitions can make apparently similar figures misleading unless the comparison is adjusted or qualified.',
    precision_extra='Separate steady-state cost from transition cost and disruption. A centralized model might look attractive after implementation while creating an unacceptable transition problem. The exercise does not establish which option is superior; it establishes the question the engagement must answer.',
    phrases='''Clarify the purpose | What decision should this benchmark help you make?
State the real choice | The choice is centralization or continued separate operation.
Confirm the owner | The executive committee owns that decision.
Confirm the date | The recommendation needs to support the thirtieth-of-November decision.
Keep the option open | Centralization has not been approved.
Identify the criteria | We need to compare cost, response time, and service continuity.
Separate cost types | Show transition costs separately from steady-state costs.
Check comparability | Are the peer figures based on comparable services and definitions?
Name an evidence gap | We do not yet have the staffing and customer-impact data.
Avoid a premature conclusion | A lower peer cost would not by itself justify closing a site.
Set the boundary | This phase evaluates options; it does not authorize implementation.
Ask about constraints | Which service requirements must remain intact during transition?
Reflect the request | The benchmark is one input to the operating-model decision.
Confirm the deliverable | We will produce a decision-focused option comparison.
Check understanding | Is that the choice you need the analysis to support?
Close discovery | Let us record the question, criteria, owner, deadline, and evidence needs.''',
    notes='''Should help | Connects the requested analysis to its intended purpose.
The choice is | States alternatives without selecting one prematurely.
Has not been approved | Prevents exploration becoming an implied commitment.
By itself | Limits what one piece of evidence can establish.
One input | Positions benchmarking within a wider decision.
Let us record | Turns a verbal clarification into a shared reference.''',
    d='''Which problem statement fits the brief? | Should North and South be centralized, given cost, response time, continuity, and transition effects? | How can we justify the already approved closure? | How many slides will impress the committee? | Which peer cost proves centralization is always best? | The appropriate question preserves the actual alternatives and criteria without presuming an approval or result.
Which benchmark caveat matters? | Peer service scope and cost definitions may differ. | Matching company size makes cost definitions unnecessary. | Comparing cost per case removes differences in case complexity. | Using the latest reporting year resolves differences in service hours. | A useful peer comparison requires comparable boundaries and measures. Size, a common ratio, and a shared year do not by themselves align scope, complexity, or service hours.
What does the evidence gap mean? | Staffing and customer-impact information is still needed. | Centralization is necessarily wrong. | Separate operation is necessarily wrong. | The consultant may invent the missing figures. | The gap identifies information required for the comparison without deciding the eventual recommendation.
Which phrase preserves engagement authority? | This phase evaluates options; implementation requires a separate authorized decision. | Discovery automatically authorizes closure. | The consultant replaces the executive committee. | Asking for a benchmark commits the client to centralization. | An analytical engagement supports the client's decision but does not itself authorize implementation.''',
    dialogue='''Rita | The committee keeps asking why our support centers cost so much. Could you give us a peer benchmark before the next decision meeting?
Owen | Before we define the [[peer group::The comparison organizations should fit the decision and relevant service characteristics, not merely be familiar names.]], what decision should the benchmark help you make? That will determine which comparisons are useful and which would simply add more numbers.
Rita | We need to decide whether North and South should become one centralized support operation or continue running separately.
Owen | Then our [[decision question::The actual choice is centralization versus separate operation; benchmarking supports that decision rather than replacing it.]] is about the operating model. The cost benchmark is an input, but we should not let it silently become a recommendation to close either site.
Rita | Agreed. Nothing has been approved. The executive committee needs a recommendation by the thirtieth of November.
Owen | I will record that [[decision deadline::The committee needs the recommendation by 30 November, which guides evidence collection and review timing.]]. We should also confirm who will supply information and when the committee needs material for its own review before that date.
Rita | Cost matters, but we also need acceptable response times and continuity. A cheap arrangement that interrupts service would not solve the problem.
Owen | Those are our [[decision criteria::Cost, response time, and continuity are the agreed comparison factors, including effects during transition.]]. We need definitions for each, so the team does not optimize a cost measure while overlooking the service requirements the committee actually values.
Rita | I can imagine a lower annual cost after centralizing. Getting there is another matter. We have not costed the move or the service disruption.
Owen | Separate [[transition cost::These costs arise during the change and must remain distinct from settled operating costs.]] from the steady-state comparison. We should show temporary effects and ongoing costs distinctly, rather than present a future operating estimate as the whole business case.
Rita | The peer organizations may handle different types of support requests. Some provide fewer service hours than we do.
Owen | That affects [[comparability::Different hours, case types, or cost definitions can distort an apparently simple peer comparison.]]. We need matching definitions or visible qualifications. A lower cost elsewhere does not tell us that either of your centers is inefficient under the same conditions.
Rita | I can arrange access to the current service figures. Staffing and customer-impact information will take longer to obtain.
Owen | Let us establish the [[baseline::The baseline describes current operations; missing staffing and customer information must remain explicit.]] and list those gaps. We can plan the evidence work without filling missing figures with assumptions that look like confirmed client data.
Rita | Should the initial work include a detailed implementation plan, or would that get ahead of the decision?
Owen | We should define what is [[in scope::The agreed analysis includes transition implications but does not automatically include a full implementation plan.]]. The option comparison needs transition implications, but a full implementation plan is a separate level of work that we should not assume is included.
Rita | The committee will make the choice. I can sponsor the engagement and coordinate the inputs, but I cannot approve a closure myself.
Owen | That clarifies the [[decision owner::The executive committee makes the choice; the sponsor coordinates without independently authorizing closure.]]. We can direct the recommendation to the committee and ask you to confirm the factual inputs and engagement arrangements within your role.
Rita | Please summarize the question, boundaries, criteria, and dates so that everyone starts with the same understanding.
Owen | I will put them in the [[engagement charter::The charter records the shared purpose, boundaries, roles, and timing before detailed analysis begins.]]. Then the benchmark serves the actual choice, and the team has a clear basis for deciding what evidence to collect first.''',
    rehearsal=('Read Rita and Owen aloud, then swap roles. Stress the actual choice and the three comparison criteria.', 'Use the answer key to correct all ten gaps. Reread the peer-comparison and transition-cost exchanges without dropping their qualifications.', 'Deliver Owen\'s final engagement summary again, retaining the decision owner, deadline, evidence gaps, and boundary between analysis and implementation.'),
    transfer_title='Clarify a different requested study',
    transfer_setup='A sponsor requests a vendor-price comparison. The actual choice is whether to renew the current provider or run a new competition. The procurement committee decides by 15 January, using total cost, service performance, and transition risk.',
    transfer='''Consultant: "The actual alternatives are renewal or ___." | a new competition | The price comparison supports this stated choice, not an already approved provider change.
Sponsor: "The decision owner is the ___." | procurement committee | The committee holds the stated decision role, while the sponsor supplies engagement direction.
Consultant: "The decision deadline is ___." | 15 January | This date determines when the comparison must support the authorized choice.
Sponsor: "The comparison must include total cost, performance, and ___." | transition risk | Transition risk is an explicit criterion alongside cost and service performance.''',
))


BOOK['units'].append(unit(
    title='Hypotheses and Issue Trees',
    scene='A frequent complaint is not yet the cause of churn',
    skill='Use a working hypothesis to organize analysis while checking alternative explanations, overlapping categories, and evidence that could contradict it.',
    brief='A client lost 60 accounts last quarter. Twenty departing customers volunteered for interviews: 12 mentioned price, 9 mentioned service delays, and 5 mentioned competitor features. Each person could mention more than one issue. Consultant Ada wants to lead with price as the cause of churn; manager Karim asks for a testable hypothesis and a structured inquiry into the alternatives. The interview sample is not established as representative. Timing, customer segments, actual prices paid, and comparable nondeparting accounts have not yet been analyzed. No causal driver has been isolated.',
    cast='Ada | Consultant\nKarim | Engagement manager',
    culture=('Challenge the logic, not the analyst', 'A sharp question about an explanation can improve the work without rejecting the person who proposed it. State which part is useful, then ask what would weaken it. A team that can revise its first answer is more credible than one that protects it from contrary evidence.'),
    a='''How many departing accounts were interviewed? | Twenty of the sixty departing accounts | All sixty accounts | Twenty current nondeparting accounts only | Twenty-six distinct accounts | Twenty customers volunteered for interviews, while sixty accounts departed in total.
Why do the mentions add to more than twenty? | Respondents could mention multiple issues. | The interview count must be fraudulent. | Each mention proves a separate departure. | The percentages use all sixty departures. | Multiple responses permit overlapping categories, so the mention counts need not sum to the number interviewed.
What has the team established about causation? | No causal driver has been isolated. | Price caused every departure. | Service had no effect. | Competitor features cannot matter. | The brief explicitly leaves causal drivers unresolved despite the frequency of particular interview mentions.''',
    vocabulary='''hypothesis | A proposed explanation that can be examined against evidence. | test a hypothesis
issue tree | A structured breakdown of a question into related subquestions. | build an issue tree
hypothesis tree | A breakdown of a proposed explanation into testable supporting claims. | develop a hypothesis tree
workstream | A coordinated part of the engagement's work. | assign a workstream
churn | Customer or account loss, defined over a specified period and population. | analyze account churn
churn driver | A factor contributing to customer departure. | investigate churn drivers
exit interview | A conversation with someone leaving a service or organization. | conduct exit interviews
multi-response question | A question allowing more than one answer category. | interpret a multi-response question
mention count | The number of recorded references to a specified topic. | report mention counts
sample | The observations included in an analysis. | define the sample
sampling bias | Distortion associated with how observations enter a sample. | assess sampling bias
MECE | Mutually exclusive and collectively exhaustive; a structuring aim of avoiding overlap and missing categories. | test a MECE structure
overlap | Inclusion of the same observation in more than one category. | identify category overlap
double counting | Counting the same item more than intended in a total. | prevent double counting
alternative explanation | A different possible account of an observed result. | test alternative explanations
disconfirming evidence | Information that weakens or contradicts a hypothesis. | seek disconfirming evidence
confirmation bias | Favoring information that supports an existing belief. | challenge confirmation bias
causal mechanism | The process through which one factor could produce an effect. | specify the causal mechanism
segmentation | Dividing a population into defined groups for analysis. | use customer segmentation
cohort | A group sharing a defined starting characteristic or period. | compare customer cohorts
price sensitivity | Responsiveness to price changes under specified conditions. | examine price sensitivity
confounder | Another factor that complicates a proposed causal interpretation. | examine potential confounders
triangulation | Comparing different evidence sources or methods. | triangulate the finding
analytical priority | A question selected for attention based on decision relevance and evidence needs. | set analytical priorities''',
    precision='Twelve of twenty interviewees mentioned price: 60% of that interview group. It is not evidence that price caused 60% of all sixty departures. The price, service, and competitor counts overlap because respondents could give more than one answer.',
    precision_extra='MECE is an organizing aim, not a label that makes real-world causes independent. A customer can experience both a price increase and a service failure. Define how observations are coded, and avoid forcing a multi-cause account into a false single-cause total.',
    phrases='''Keep the explanation provisional | Price is a working hypothesis, not an established churn driver.
State the sample | We interviewed twenty of the sixty departing accounts.
Limit the percentage | Twelve of those twenty interviewees mentioned price.
Explain overlap | Respondents could name more than one issue.
Avoid a false total | The categories are not mutually exclusive.
Ask for a mechanism | How would the proposed price effect lead to departure?
Test the alternative | We also need to examine service experience and competitor changes.
Look for contradiction | What evidence would weaken the price hypothesis?
Check timing | Did the price change precede the departure?
Compare carefully | How do otherwise comparable nondeparting accounts differ?
Segment the evidence | Separate the patterns by relevant customer group.
Check actual exposure | Use prices actually paid, not only the published list price.
Avoid a causal shortcut | A frequent complaint does not by itself isolate a cause.
Prioritize the work | Start with questions that could change the client decision.
Revise openly | The new evidence may require us to change the initial explanation.
Close the analysis plan | Assign a test, evidence source, and owner to each priority question.''',
    notes='''Working hypothesis | Gives the team a testable starting point rather than a fixed conclusion.
Those twenty | Keeps the denominator tied to the interview sample.
Could name more than one | Explains why categories overlap.
Would weaken | Actively invites evidence against the preferred explanation.
Actually paid | Distinguishes realized prices from advertised prices.
Could change the decision | Uses relevance rather than analytical convenience to set priorities.''',
    d='''Which finding is supported? | Twelve of twenty volunteer interviewees mentioned price. | Price caused 60% of all departures. | All sixty departing customers answered the interview. | The three categories cover separate people only. | The supported statement retains the sample and what respondents said without converting mentions into causal proof.
Which follow-up best tests rather than protects the hypothesis? | Examine whether comparable accounts with similar price changes stayed. | Recode overlapping complaints so price becomes each respondent's only category. | Compare this quarter's departing accounts with all customers from a different product line. | Ask only the twelve price complainants whether a discount would have helped. | Comparable retained accounts can challenge the explanation. Forced recoding changes the evidence; a different product line may be an unsuitable comparison; questioning only price complainants preserves selection bias.
How should the issue categories be presented? | As overlapping mentions, with the coding method explained | As 26 unique departures from 20 interviews | As mutually exclusive simply because the slide says MECE | As percentages of an unstated population | The multi-response design requires clear overlap disclosure to avoid misleading totals.
What makes an analytical priority useful? | It could change the decision and has an explicit evidence test. | It is the easiest chart to produce. | It confirms the first theory by definition. | It eliminates all uncertainty without data. | Priority should follow decision relevance and a testable inquiry, not convenience or guaranteed agreement.''',
    dialogue='''Ada | Price tops the exit-interview list. My draft says it is driving churn. Before I send that to the client, does the evidence justify the wording?
Karim | Make it a [[hypothesis::Price is an explanation to test, not a cause established by interview frequency.]], not a finding about cause. We have twenty volunteer interviews from sixty departures, and the way people entered that sample could affect what we hear.
Ada | Twelve mentioned price, nine mentioned service delays, and five mentioned competitor features. The total is greater than twenty because people could mention several issues.
Karim | Then disclose the [[overlap::Several topics can describe the same respondent, so their counts can exceed the interview count.]]. Those are topic mentions, not separate groups of departing accounts. A clean-looking chart must not imply that the categories are mutually exclusive when they are not.
Ada | Twelve out of twenty is sixty percent. I should say sixty percent of interviewees mentioned price, not sixty percent of departures were caused by price.
Karim | Exactly. The [[sample::The twenty interviewees are not automatically representative of all sixty departures, and mentions do not establish cause.]] defines that percentage. We have not established representativeness, and mentioning a concern does not isolate its causal effect on the decision to leave.
Ada | How should I organize the next analysis without creating a huge list of every possible reason someone might cancel?
Karim | Build an [[issue tree::The tree organizes decision-relevant subquestions without treating its initial branches as proven explanations.]] around questions that could change the retention decision. Include price exposure, service experience, and competitor developments, while being clear that real causes may interact.
Ada | We sometimes call our trees MECE. That could be misleading if we use the label to suggest that these customer experiences cannot coexist.
Karim | Treat [[MECE::MECE checks structure; the label does not make interacting customer experiences independent or exclusive.]] as a structuring check, not a substitute for understanding the data. Define the coding and identify gaps or overlaps instead of forcing complex departures into artificial single-cause boxes.
Ada | For price, we could check the amounts customers actually paid and whether a change occurred before cancellation.
Karim | That begins to test a [[causal mechanism::This asks how and when price could influence departure, beyond merely recording a repeated complaint.]]. Timing matters, and list prices may differ from actual exposure because of discounts or contract terms. We should not assume every account faced the same change.
Ada | What about accounts that had the same price increase and stayed? I have focused on departures, but that comparison could change the story.
Karim | That could provide [[disconfirming evidence::Comparable retained accounts could weaken the price explanation; comparison quality still needs examination.]]. Check comparability and relevant differences before interpreting it. The aim is to test the explanation, not select the most convenient retained accounts to prove the opposite.
Ada | Service delays may affect some customer groups more than others. A combined result could hide that pattern.
Karim | Use relevant [[segmentation::Defined customer groups can reveal different patterns that a combined result might conceal.]]. But document how groups are defined, and do not repeatedly regroup the data just until a compelling story appears.
Ada | We can compare interview accounts, service records, and actual commercial terms to see where the evidence agrees or conflicts.
Karim | That is useful [[triangulation::Comparing evidence sources can inform the explanation without automatically establishing a causal effect.]]. Keep discrepancies visible. Agreement across sources may strengthen an interpretation, but it does not automatically remove all alternative explanations.
Ada | I will revise the update to state the interview pattern and the tests needed before recommending a price response.
Karim | Good. Set each [[analytical priority::A priority is a decision-relevant test with an evidence source and owner, not merely an easy task.]] with an evidence source and owner. The initial hypothesis should help us learn faster, not make the team resistant to what the next analysis finds.''',
    rehearsal=('Read Ada and Karim aloud, then swap roles. Say the sample size before the sixty-percent figure.', 'Correct the ten gaps from the key. Reread the exchanges on overlapping mentions and evidence against the price hypothesis.', 'Repeat the client-update close using the supplied interview pattern and unresolved tests; keep a frequent complaint distinct from an established cause.'),
    transfer_title='Interpret another overlapping interview sample',
    transfer_setup='Forty customers departed. Ten volunteered for interviews; six mentioned onboarding and five mentioned support. Multiple answers were allowed. The sample has not been shown to represent every departing customer.',
    transfer='''Analyst: "The interview sample contains ___." | ten customers | Ten departing customers were interviewed, not the full population of forty departures.
Manager: "Onboarding was mentioned by ___ of interviewees." | 60% | Six divided by ten equals sixty percent within this interview sample.
Analyst: "The categories contain ___." | overlapping mentions | Multiple answers were allowed, so onboarding and support may describe the same people.
Manager: "The result does not establish a ___." | causal driver | Topic frequency alone neither isolates the cause nor represents all departing customers.''',
))


BOOK['units'].append(unit(
    title='Data Requests and Client Burden',
    scene='Forty requests, but only six are needed first',
    skill='Prioritize a client data request, define the required measures, and agree a feasible delivery sequence without collecting unnecessary personal information.',
    brief='Consultant Mateo sends client lead Leah a 40-item request due Friday. The first analysis actually needs six monthly measures for January through June at the North and South centers: completed cases, paid staff hours, labor cost, vendor cost, reopened cases, and opening backlog. That analysis is needed for a Wednesday workshop. Existing aggregate reports may be sufficient, but definitions and period coverage must be checked. The remaining 34 items have not been prioritized. Leah cannot promise the full request. Mateo must agree owners, feasible dates, and approved transfer arrangements rather than demand raw personal records by default.',
    cast='Mateo | Consultant\nLeah | Client data lead',
    culture=('Client effort is part of the work plan', 'A data request competes with the daily responsibilities of the client team. Explain which decision each priority item supports, accept existing formats when suitable, and negotiate dates with the people doing the work. Labeling every item urgent usually makes genuine priorities harder to recognize.'),
    a='''How many items are required for the first analysis? | Six | All forty | Thirty-four | None | The brief identifies six measures needed first and leaves the remaining thirty-four unprioritized.
Which period is required? | January through June, monthly, for both centers | One total with no period definition | Every year of personal records | Only the latest Friday | The required structure is monthly coverage from January through June for North and South.
What is the timing problem? | A Friday deadline is later than the Wednesday workshop that needs the analysis. | Friday is necessarily too early for every item. | The workshop has already approved all data. | Data definitions no longer matter because of the deadline. | The first analysis must support Wednesday, so its necessary inputs need a feasible earlier arrangement.''',
    vocabulary='''data request list | A documented set of information items requested for an analysis. | prioritize the data request list
DRL | Data request list, with items, owners, definitions, and delivery status. | update the DRL
minimum viable dataset | The smallest adequate set of information for a defined initial analysis. | define the minimum viable dataset
data owner | The person or function responsible for the relevant information. | identify the data owner
extract | A selected set of information taken from a source system. | prepare a data extract
aggregate | Information combined into defined groups rather than individual records. | use monthly aggregates
granularity | The level of detail represented in the data. | agree the required granularity
reporting period | The time interval covered by a measure. | specify the reporting period
data dictionary | Definitions of fields, units, and relevant rules. | request a data dictionary
field definition | The meaning and permitted interpretation of a data item. | confirm field definitions
unit of measure | The scale or quantity in which a value is expressed. | preserve the unit of measure
coverage | The population, locations, or periods included. | check period coverage
completeness | Whether the required information is present. | assess completeness
reconciliation | A comparison used to explain or resolve differences between records. | reconcile source totals
source system | The originating application or record for data. | identify the source system
secure transfer | An approved method for moving information with appropriate protection. | arrange secure transfer
access permission | Authorization to view or use specified information. | confirm access permissions
personal data | Information relating to an identifiable individual under the applicable context. | limit personal data
data minimization | Restricting collection to information necessary for the stated purpose. | apply data minimization
request dependency | A condition that must be met before a requested item can be delivered or used. | identify request dependencies
delivery sequence | The order in which information will be provided. | agree the delivery sequence
staged request | A request divided into prioritized batches. | use a staged request
exception log | A record of missing, changed, or unresolved items. | maintain an exception log
version identifier | A label distinguishing one version of a file or dataset. | record the version identifier''',
    precision='A smaller first request is not a waiver of definitions or quality. Confirm what completed, reopened, and opening mean in the existing reports, along with units, cost scope, and monthly coverage. A timely file with misunderstood fields can produce a misleading comparison.',
    precision_extra='Aggregate reporting may answer the first question without individual records. Verify suitability and approved access rather than requesting personal data for possible future use. Where an item cannot arrive in time, state the effect on the analysis instead of quietly substituting a different measure.',
    phrases='''Acknowledge the burden | The original list did not distinguish what we need first.
Explain the priority | Six measures support the first workshop analysis.
Specify the period | We need monthly figures from January through June for both centers.
Use existing work | Can the existing reports supply those measures?
Check the detail level | Monthly aggregates may be sufficient for this question.
Define the measure | What does completed case mean in this report?
Check cost scope | Do the labor and vendor figures cover the same operating boundary?
Assign an owner | Who can confirm the definition and supply each item?
Negotiate a date | What can realistically be available before Wednesday's workshop?
Stage the remainder | We will prioritize the other thirty-four items separately.
Avoid unnecessary collection | We do not need individual personal records for this first analysis.
Agree the transfer | Use the client-approved channel and access permissions.
Keep gaps visible | Please flag missing periods rather than filling them silently.
Track the version | Record the file version and extraction date.
State an analytical limit | If that measure is unavailable, we will explain the limitation in the workshop.
Close the request | I will circulate the agreed six-item list, owners, dates, and definitions.''',
    notes='''Did not distinguish | Acknowledges a weakness in the request without blaming the client.
Support the analysis | Explains why an item is being requested.
May be sufficient | Leaves suitability open to a definition and coverage check.
Realistically | Invites a feasible commitment rather than a pressured guess.
Separately | Stops unprioritized work inheriting the first deadline.
Rather than silently | Makes an omission visible before it becomes an analytical error.''',
    d='''Which revised request is most useful? | Six defined monthly measures first, with agreed owners and dates; prioritize the rest separately. | Forty equally urgent items with no purpose. | Every personal record just in case. | One unexplained total for both centers combined. | A staged request aligns the immediate analysis with defined information, accountable owners, and feasible delivery.
What should happen if an existing report is available? | Check its definitions, scope, and coverage before accepting it. | Reject it automatically because it is not a new extract. | Accept every column without reading definitions. | Treat its filename as proof of completeness. | Existing reports may reduce effort, but their fields and boundaries must fit the required analysis.
What if a priority item cannot arrive before the workshop? | Agree a realistic plan and state the resulting analytical limit. | Fill it with invented numbers. | Call a different field equivalent without checking. | Hide the missing item from the presentation. | A missing input changes what the analysis can support and should be disclosed rather than concealed.
Which information-handling choice fits the first task? | Use suitable aggregates through approved access and transfer arrangements. | Request names and contact details without a defined need. | Send raw records through any convenient public channel. | Assume every consultant may access every system. | The case calls for the necessary level of detail and authorized handling, not unrestricted collection or access.''',
    dialogue='''Leah | Forty items by Friday is more than my team can commit to during reporting close. Which files actually drive the first piece of analysis?
Mateo | You are right. The [[data request list::The list needs to distinguish the six immediate inputs from later, unprioritized work.]] did not distinguish what we need first. Only six measures support the initial analysis, and I should have separated them from the rest.
Leah | The workshop is Wednesday. A single Friday deadline does not help us understand what you need in time for that meeting.
Mateo | Let us agree a [[delivery sequence::The sequence puts workshop inputs first, with dates negotiated against actual client capacity.]] with feasible dates. We need to know what can arrive before Wednesday and what limitations we will have if something is not available.
Leah | Please name the six measures. We may already have monthly reports that save the teams from producing new files.
Mateo | Our [[minimum viable dataset::The six specified measures supply the initial analysis, rather than every possible future question.]] is completed cases, paid staff hours, labor cost, vendor cost, reopened cases, and opening backlog for January through June at both centers.
Leah | We have monthly summaries, but the two sites may define completed and reopened differently. The report labels do not explain that.
Mateo | We need a [[data dictionary::Definitions prevent different site meanings from being treated as equivalent simply because labels match.]] or equivalent definitions. Confirm what each field means and which period it covers before we compare figures that only appear to describe the same thing.
Leah | Would monthly totals by center be enough? Individual case records would require a different review and take longer to prepare.
Mateo | That [[granularity::Suitable monthly center totals may answer the initial question without requiring individual case records.]] may be sufficient for the first question. Let us verify the report coverage and definitions before asking for more detailed data that we do not currently need.
Leah | There is a catch in labor cost: North includes a shared-service allocation. I need to check South before you compare the two totals.
Mateo | Please flag that for [[reconciliation::The differing cost allocations need examination so unlike operating boundaries are not silently compared.]]. We need the cost scope alongside the numbers. A difference in allocation rules could otherwise look like a difference in operating performance.
Leah | I can identify the relevant owners today. They need to confirm what can be supplied before the workshop, rather than have a date assigned without discussion.
Mateo | Agreed. Each [[data owner::The owner confirms and supplies the information, supporting a realistic commitment and accurate definitions.]] should confirm the definition and feasible delivery date. We will prioritize the other thirty-four items separately once their analytical purpose is clear.
Leah | Our team also needs to know how the files will be shared and which consultants are authorized to see them.
Mateo | We will use the approved [[secure transfer::Files need the approved route and permissions, not any convenient communication channel.]] arrangements and access permissions. We do not need names or contact details for these monthly measures, so they should not be collected for this first analysis.
Leah | If a month is missing, should the team leave a note in the file rather than estimate it?
Mateo | Yes, keep an [[exception log::The log records missing periods and unresolved definitions rather than silently replacing them.]]. Identify the gap and its owner. We will explain its effect on the workshop analysis instead of quietly replacing it with a different period or measure.
Leah | Once the owners confirm the first batch, I will send the agreed files with their extraction dates.
Mateo | Include the [[version identifier::The identifier distinguishes supplied files from revisions, making the analysis and corrections traceable.]] as well. I will circulate the six-item request with definitions, owners, dates, and remaining gaps so both teams know exactly what has been agreed.''',
    rehearsal=('Read Leah and Mateo aloud, then swap roles. Give the six priority measures as a clear list.', 'Check all ten gaps. Reread the period, definition, aggregation, and approved-transfer exchanges using the corrected wording.', 'Repeat the agreed first-batch close with named owners and feasible dates; keep the remaining thirty-four items outside the confirmed first delivery.'),
    transfer_title='Stage another information request',
    transfer_setup='A 25-item request contains four inputs needed for a Monday review. Existing weekly summaries may supply them. The remaining 21 items are for later analysis. Client owners must confirm definitions and realistic delivery dates.',
    transfer='''Consultant: "The first batch contains ___." | four inputs | Four specified inputs support the immediate review, not all twenty-five requested items.
Client: "The first review is on ___." | Monday | Monday is the stated review date that the first delivery sequence must support.
Consultant: "The later group contains ___." | twenty-one items | Subtracting four priority inputs from twenty-five leaves twenty-one items for later prioritization.
Client: "Before using existing summaries, confirm their ___." | definitions | Available files must match the intended measures; their existence alone does not establish suitability.''',
))


BOOK['units'].append(unit(
    title='Slide Storylines and Executive Synthesis',
    scene='Twelve charts need one clear decision request',
    skill='Convert an analytical presentation into a supported recommendation with a specific request, visible limits, and an agreed test.',
    brief='Analyst Jun has twelve charts about a proposed case-routing process but no clear recommendation. Engagement manager Sofia must prepare an executive discussion about a pilot. Walkthroughs suggest a possible benefit, but there is no live operating result. The proposal is a four-week pilot at one center with a $20,000 budget request. Current median handling time is 12 minutes. Proposed success measures are a median of 10 minutes or less and an error rate no higher than 2%, using agreed definitions and eligible-case coverage. The committee is being asked to authorize the pilot, not full rollout.',
    cast='Jun | Analyst\nSofia | Engagement manager',
    culture=('Concise does not mean unqualified', 'A senior audience may interrupt a long tour of the analysis to ask what it should do. Lead with the requested decision, then give the evidence and material limits. Put supporting detail in the appendix, but keep information that changes the decision visible in the main presentation.'),
    a='''What authorization is requested? | A four-week, one-center pilot with a $20,000 budget | Immediate full rollout | An unlimited implementation budget | A guarantee of future savings | The proposal specifies a bounded pilot and budget, not organization-wide implementation.
What evidence exists so far? | Walkthroughs suggesting a possible benefit, with no live operating result | A completed successful live pilot | A verified reduction to ten minutes | A proven zero-error rollout | The brief identifies walkthrough evidence and explicitly states that live operating results are absent.
What are the proposed success measures? | Median handling time at most 10 minutes and error rate at most 2% | Average time below twelve with errors ignored | Any faster case regardless of error rate | A larger chart count | The proposed test combines the stated median-time threshold with an error-rate guardrail under agreed definitions.''',
    vocabulary='''storyline | The logical sequence connecting a presentation's messages. | build the storyline
executive synthesis | A concise integration of findings and implications for a decision. | prepare an executive synthesis
governing message | The central point organizing the supporting argument. | state the governing message
action title | A slide heading expressing its key conclusion or implication. | use an action title
exhibit | A chart, table, or other analytical display. | reference the exhibit
finding | An observation established by the analysis. | state the finding
insight | An interpretation explaining why a finding matters. | develop an insight
implication | A consequence or significance for the decision. | explain the implication
recommendation | A proposed course of action with its supporting basis. | make a recommendation
decision ask | The specific authorization or choice requested from the audience. | clarify the decision ask
supporting evidence | Information used to substantiate a statement. | present supporting evidence
evidence chain | The connection from source information through findings to a conclusion. | check the evidence chain
caveat | A material limitation or condition on a claim. | retain the caveat
main body | The principal part of a presentation, excluding supporting appendices. | keep limits in the main body
appendix | Supporting detail placed after the main material. | move detail to the appendix
pre-read | Material distributed for review before a meeting. | circulate the pre-read
visual hierarchy | The arrangement that signals the relative importance of displayed information. | improve the visual hierarchy
chart annotation | A note explaining a feature or limit of a chart. | add a chart annotation
denominator | The total underlying a proportion or rate. | state the denominator
median | The middle value in ordered observations, or the midpoint of two middle values. | report the median
pilot | A limited test of an approach before a wider decision. | authorize a pilot
guardrail | A defined limit intended to prevent an unacceptable side effect. | set a quality guardrail
success criterion | A specified condition used to judge the result. | agree success criteria
rollout decision | A choice about extending an approach beyond the initial test. | separate the rollout decision''',
    precision='Twelve minutes is the current median, not necessarily the mean. Ten minutes is a proposed threshold, not an achieved result. The 2% error guardrail needs a defined numerator, denominator, and eligible-case population so faster work does not conceal a quality problem.',
    precision_extra='A pilot recommendation can be clear even when the eventual benefit is uncertain. Ask for the limited test, explain why the evidence justifies testing, and identify what the test must show. Do not present authorization to learn as authorization for full rollout.',
    phrases='''Lead with the request | We recommend a four-week pilot at one center.
State the amount | The budget request is twenty thousand dollars.
Limit the authorization | We are not asking for full rollout today.
State the evidence level | Walkthroughs suggest a possible benefit; live results are not yet available.
Explain the implication | That supports a bounded test, not a claim of proven operating improvement.
Name the current measure | The current median handling time is twelve minutes.
Name the proposed threshold | The pilot target is a median of ten minutes or less.
Preserve quality | The error rate must be no higher than two percent under the agreed definition.
Define the measurement | Specify eligible cases, the error numerator, and the denominator before launch.
Improve the heading | Make the slide title state the finding, not just the chart topic.
Connect the argument | What does this exhibit change about the decision?
Keep the caveat visible | The lack of live evidence belongs in the main presentation.
Move supporting detail | Put the calculation detail in the appendix, with a clear reference.
Avoid selective emphasis | Show the quality measure alongside the speed result.
Separate later decisions | A wider rollout requires a subsequent review and authorization.
Close the presentation | Ask the committee to approve the pilot scope, budget, and measurement plan.''',
    notes='''Recommend | States a position without pretending the choice is already authorized.
Not asking for | Limits the immediate decision.
Suggest | Describes preliminary evidence without upgrading it to proof.
Must be no higher | Establishes a proposed upper limit rather than a descriptive average.
Alongside | Prevents one favorable measure from hiding another important result.
Subsequent | Makes the later rollout decision distinct from this pilot approval.''',
    d='''Which opening is decision-focused and accurate? | Approve a four-week, one-center pilot for $20,000 to test the proposed process. | These twelve charts prove full rollout will succeed. | Handling time has already fallen to ten minutes. | We have no request but many interesting graphs. | The accurate opening states the bounded authorization being sought without inventing achieved results.
Which statement belongs in the main presentation? | No live operating result is available yet. | Only the file naming convention | Every calculation row regardless of relevance | A hidden claim that the pilot is already complete | The absence of live evidence materially affects the decision and should not be buried in supporting material.
Which comparison preserves the metric? | Current median 12 minutes; proposed pilot threshold at most 10 minutes | Current mean 12 minutes because median means average in every sense | Guaranteed ten-minute result for every case | Two minutes saved on every individual case | The comparison keeps the stated summary measure and distinguishes current performance from a proposed threshold.
What prevents speed from becoming the only success measure? | Report the defined error-rate guardrail alongside handling time. | Remove error data from the deck. | Treat a faster median as automatic quality improvement. | Count only cases with good outcomes. | The proposed pilot requires both speed and quality measures over the agreed eligible-case population.''',
    dialogue='''Jun | Twelve charts, and I still cannot tell what I want the committee to approve until the last slide. Can we rebuild the opening around the decision?
Sofia | Start with the [[decision ask::The audience needs the specific pilot scope and budget request before the supporting charts.]]. We want authorization for a four-week pilot at one center, with a twenty-thousand-dollar budget. The audience should not have to infer that from the exhibits.
Jun | Should the opening say the new routing process will reduce handling time, or is that stronger than our evidence supports?
Sofia | Keep the [[recommendation::The recommendation proposes a test; walkthroughs do not support a promise of live improvement.]] bounded. Walkthroughs suggest a possible benefit, but there is no live operating result yet. We recommend testing the process, not claiming that the improvement has already happened.
Jun | Then the next page should explain why testing is reasonable and what uncertainty the pilot would address.
Sofia | That gives us a [[storyline::The storyline connects the request, evidence, uncertainty, and test rather than merely arranging charts by topic.]]. Each exhibit should serve that argument. If a chart does not affect the decision or explain the test, it probably does not need equal time in the meeting.
Jun | The current handling-time chart says twelve minutes. I need to label that as the median, not just call it the average.
Sofia | Yes, preserve the [[median::The stated median must not be relabeled as the mean or a value applying to every case.]]. The proposed threshold is ten minutes or less on the same defined measure. Do not make a target sound like an achieved result or a promise about every individual case.
Jun | The error measure is on a separate page. The committee might hear the faster-time target and miss the quality condition.
Sofia | Bring the [[guardrail::The error limit stays visible alongside speed, preventing a one-sided definition of pilot success.]] alongside it. The proposed error rate must be no higher than two percent under the agreed definition. Faster work is not enough if quality deteriorates beyond that limit.
Jun | We should define eligible cases and how errors are counted before launching, rather than adjust the measures after seeing the result.
Sofia | Exactly. State the [[success criteria::The thresholds need agreed measurement rules and eligible-case coverage before results are observed.]] and measurement plan up front. The numerator, denominator, and case coverage need to be clear so the committee knows what a favorable result would actually mean.
Jun | My title just says Routing Analysis. It tells them the topic, but not what the walkthrough found or why we still need a pilot.
Sofia | Use an [[action title::The heading states the supported implication without claiming more than the exhibit establishes.]] that communicates the implication accurately. For example, the evidence supports a limited live test. The heading must not imply proven improvement while the detail says otherwise.
Jun | I can move the detailed walkthrough calculations behind the main story, with a reference for anyone who wants to inspect them.
Sofia | The [[appendix::Supporting calculations can move here; decision-changing evidence limits must remain in the main presentation.]] is appropriate for that detail. But keep the lack of live results and the quality condition in the main presentation, because they change how the recommendation should be understood.
Jun | If the committee approves the pilot, the minutes should not say that it approved the entire new operating model.
Sofia | Correct. A [[rollout decision::Wider implementation needs a separate later authorization; pilot approval does not automatically permit it.]] comes later, after the relevant results and review. We should state that distinction in both the request and the closing summary.
Jun | I will reorder the deck around the request, evidence, proposed test, and decision conditions, with the detailed calculations available separately.
Sofia | That is an [[executive synthesis::Synthesis connects findings to a bounded decision instead of giving every analysis equal emphasis.]]. It is shorter because the argument is organized, not because important uncertainty has been removed.''',
    rehearsal=('Read Jun and Sofia aloud, then swap roles. Put the pilot request before the supporting detail.', 'Check all ten gaps. Reread the median-time target and error ceiling together so neither sounds optional.', 'Give the closing request again with the supplied duration, site, budget, and measurement conditions; do not turn pilot approval into rollout approval.'),
    transfer_title='State another bounded pilot request',
    transfer_setup='A team proposes a three-week trial at two branches with a $12,000 budget. No live results exist. The committee is asked to authorize the trial only; broader rollout requires another decision.',
    transfer='''Presenter: "The proposed duration is ___." | three weeks | Three weeks defines the requested trial period, not a permanent implementation.
Chair: "The trial covers ___." | two branches | The specified two-branch boundary limits the scope of the requested authorization.
Presenter: "The budget request is ___." | $12,000 | Twelve thousand dollars is the amount supplied for this limited trial.
Chair: "Broader rollout requires ___." | another decision | Trial approval does not automatically authorize expansion beyond the stated scope.''',
))


BOOK['units'].append(unit(
    title='Scope Management and Change Requests',
    scene='A second market is a new request, not a free extension',
    skill='Respond constructively to additional work by distinguishing the agreed scope from the proposed change and explaining options without premature commitments.',
    brief='Engagement C18 covers a six-week study of Market A for a fixed $60,000 fee. At the end of week three, client sponsor Helen asks for the same full study of Market B by the original deadline. The current team cannot complete both full studies in the remaining time. Consultant Raj can prepare options: additional resources subject to availability, an extension, a narrower Market B scan, or deferral. Fees and dates for the change are not yet assessed. The signed terms require an agreed written change before extra work begins. Helen has not approved a change.',
    cast='Helen | Client sponsor\nRaj | Engagement manager',
    culture=('A boundary is easier to accept with choices', 'A blunt refusal can miss an important client need, while an unqualified yes can create an impossible commitment. Acknowledge the purpose of the request, explain the current boundary and capacity, and offer options for an authorized decision. Keep assessment separate from approval.'),
    a='''What does the signed engagement currently cover? | A six-week study of Market A for $60,000 | Full studies of both markets for the same fee | An unlimited number of markets | A completed Market B study | Market A is the agreed scope; Market B is an additional request not covered by an approved change.
Can the current team finish both full studies by the original deadline? | No, not under the stated capacity. | Yes, because the request came from the sponsor. | Yes, without changing anything. | Only if the team labels Market B as Market A. | The brief explicitly states that the current team cannot complete both full studies in the remaining time.
What must precede extra work? | An agreed written change under the signed terms | An informal assumption of future approval | A completed invoice after unapproved work | The consultant's unilateral fee decision | The fictional contract requires the written change to be agreed before extra work starts.''',
    vocabulary='''scope baseline | The agreed work boundaries against which changes are assessed. | protect the scope baseline
statement of work | A document specifying the work, outputs, and relevant engagement terms. | review the statement of work
fixed fee | A specified charge for a defined scope under the agreement. | confirm the fixed fee
change request | A proposal to alter agreed work or arrangements. | raise a change request
scope creep | Uncontrolled growth in work beyond the agreed scope. | prevent scope creep
impact assessment | Examination of a proposed change's consequences. | complete an impact assessment
resource capacity | The work a team can perform with its available people and time. | assess resource capacity
resource availability | Whether suitable people or other resources can be assigned when needed. | check resource availability
deliverable | A specified output to be supplied. | define the deliverable
acceptance criterion | A condition used to determine whether an output meets the agreement. | agree acceptance criteria
change authorization | Formal permission for the specified change. | obtain change authorization
commercial terms | Agreed conditions concerning fees and other business arrangements. | confirm commercial terms
schedule extension | An approved increase in the time allowed. | propose a schedule extension
scope trade-off | Exchanging one work element for another under agreed conditions. | explain a scope trade-off
high-level scan | A limited overview rather than a full detailed study. | offer a high-level scan
depth of analysis | The detail and rigor of examination provided. | specify the depth of analysis
assumption log | A record of conditions used in planning or analysis. | update the assumption log
dependency | A condition or task on which another depends. | identify a dependency
rework | Work needed to revise or repeat previous output. | estimate rework
change register | A record of requested changes and their status. | maintain the change register
pending approval | Awaiting the relevant authorized decision. | mark the change pending approval
deferral | Moving a decision or activity to a later time. | propose deferral
out-of-scope request | A request beyond the currently agreed work. | assess an out-of-scope request
written variation | A documented agreed change to specified engagement terms. | execute a written variation''',
    precision='A fixed fee applies to the defined scope, not automatically to any additional request. The $60,000 figure is the existing Market A fee. No price or delivery date has yet been established for Market B, and the exercise supplies no basis for inventing one.',
    precision_extra='A high-level scan is not the same deliverable as a full market study. Specify coverage, evidence depth, exclusions, and acceptance conditions if that option is developed. Calling a narrower product a full study would conceal the trade-off rather than solve it.',
    phrases='''Acknowledge the purpose | I understand why Market B has become important.
State the current agreement | The signed scope covers the six-week Market A study.
Name the additional request | A full Market B study is a change to that scope.
Describe capacity honestly | The current team cannot complete both full studies by the existing deadline.
Offer assessment | We can assess options for resources, timing, and analytical depth.
Avoid an early quote | The revised fee and dates have not yet been assessed.
Check people before promising | Additional resources depend on suitable people being available.
Explain an extension | More time is one option, subject to agreement.
Distinguish a smaller product | A high-level scan would have narrower coverage than a full study.
Offer deferral | We could schedule Market B as a later phase.
Preserve existing commitments | We should show what each option does to Market A.
State the approval condition | The terms require an agreed written change before extra work starts.
Keep status accurate | The request is being assessed, not yet approved.
Define acceptance | Agree what the revised deliverable must contain.
Record the decision | Capture the chosen scope, fee, dates, and responsibilities in the variation.
Close without overpromising | I will return with assessed choices rather than commit to an unsupported deadline.''',
    notes='''Has become important | Acknowledges the new need without accepting the work automatically.
Current team | Makes the capacity statement specific rather than claiming no solution exists.
Have not yet | Identifies an assessment gap, not a refusal to discuss options.
Narrower coverage | States the real difference in the smaller deliverable.
Before extra work | Preserves the agreed approval sequence.
Assessed choices | Promises an evaluation process rather than an unknown result.''',
    d='''Which response is constructive and accurate? | We can assess ways to add Market B, but both full studies do not fit the current capacity and deadline. | Yes, both are included with no changes. | Every new client request must be refused. | We will invent a new fee after finishing. | The response acknowledges the need while making the known capacity limit and assessment step explicit.
Which statement about the scan is appropriate? | Its reduced coverage and depth must be specified. | It is identical to a full study because the title is similar. | It needs no agreed deliverable. | Its limitations should be hidden in the appendix only. | A smaller product is a meaningful option only when its boundaries and expected output are clear.
What is the status of Market B? | Requested and awaiting assessment and written agreement | Approved by the mere act of asking | Already delivered | Included in the original Market A scope | No assessment or agreed written variation exists, so the request remains unapproved additional work.
What should an impact assessment include? | Effects on scope, people, fees, timing, and existing commitments | Only whether the client sounds enthusiastic | A guaranteed date before checking capacity | A change in wording with no work consequences | A decision requires the practical and commercial consequences, including what happens to the original engagement.''',
    dialogue='''Helen | The board now wants Market B as well. Can you cover it to the same depth and keep our six-week presentation date?
Raj | I understand the need. Our [[scope baseline::The baseline covers Market A; adding Market B changes the agreed work boundaries.]] covers Market A at the fixed sixty-thousand-dollar fee. A full second study is additional work, so we need to assess how it would fit.
Helen | We are halfway through the engagement. I had hoped the team could reuse enough of the approach to keep the original date.
Raj | Reuse may help, but the current [[resource capacity::The current team cannot complete both full studies by the original deadline, despite possible method reuse.]] does not support both full studies in the remaining time. I do not want to promise a date that depends on work we have not resourced.
Helen | What options can you bring back? I would prefer choices to a simple statement that the request is outside scope.
Raj | We can prepare an [[impact assessment::The assessment compares effects on people, time, fees, scope, and the original commitments.]]. The options include additional resources if available, an extension, a narrower scan of Market B, or a later phase. Each has different implications.
Helen | If you add people, can you guarantee that the final date stays unchanged?
Raj | Not before checking [[resource availability::Suitable extra staff must be verified before they can support a promised deadline.]]. We need suitable people at the right time, plus any coordination and review capacity. More names on a staffing plan do not automatically remove every dependency.
Helen | We might accept less depth for Market B if it gives us an initial view before the committee meeting.
Raj | Then define a [[high-level scan::The scan is a narrower product with different coverage and evidence depth from a full study.]] explicitly. We should agree the questions, evidence depth, exclusions, and output, rather than describe a smaller product as if it were the full study you originally requested.
Helen | I also need to know whether any of these choices would weaken the work already promised for Market A.
Raj | That is part of the [[scope trade-off::Any reduction or exchange in the original work must be explicit, not silently absorbed.]]. We will show what stays unchanged and what would move or reduce. The original commitments should not quietly disappear because the new request feels more urgent.
Helen | Could you at least get Market B started while I speak with procurement? I do not want us to lose another week waiting for signatures.
Raj | The signed terms require [[change authorization::The agreement requires a written approved change before the additional work starts.]] through an agreed written change before extra work starts. We can assess the request now, but we should not treat pending approval as permission to deliver it.
Helen | Understood. I have requested the change, not approved a revised fee or schedule. Those details still need to come back.
Raj | Correct. The [[commercial terms::The new fee remains unassessed; the existing $60,000 is not a Market B quotation.]] and dates for Market B are not established yet. The existing fee is not an estimate for the extra work, and I will not invent one before the assessment.
Helen | If we choose the narrower scan, the document should say how we will judge whether it has met the agreed brief.
Raj | We will include [[acceptance criteria::These define what the revised output must contain so its narrower scope can be reviewed fairly.]] for that output. A shared definition of completion helps avoid a later disagreement over whether a preliminary overview was supposed to be a full market study.
Helen | Please bring back the options with their effects on Market A, the timing, and the approval needed for the selected route.
Raj | I will record the request in the [[change register::The register tracks the request's status, distinguishing assessed options from an agreed written variation.]] and return with assessed choices. Once the authorized parties agree the written variation, we can plan the added work against the actual approved terms.''',
    rehearsal=('Read Helen and Raj aloud, then swap roles. Practice acknowledging urgency before describing the scope and resource effects.', 'Correct all ten gaps. Reread the narrower-scan option and the exchange about starting before authorization.', 'Repeat the options close with timing, Market A effects, acceptance criteria, and the required approval; keep a requested change distinct from agreed work.'),
    transfer_title='State another unapproved scope addition',
    transfer_setup='A four-week engagement covers Region East for $35,000. In week two, the client requests Region West as well. Extra work requires an agreed written variation. Its fee, staffing, and timing have not been assessed.',
    transfer='''Manager: "The current geographic scope is ___." | Region East | Region East alone is included in the existing engagement.
Client: "The additional requested region is ___." | Region West | Region West is new work rather than part of the stated original scope.
Manager: "The existing fee is ___." | $35,000 | This amount applies to the original engagement, not an invented quote for the addition.
Client: "Extra work requires an agreed ___." | written variation | The supplied terms make written agreement a prerequisite to starting the additional work.''',
))


BOOK['units'].append(unit(
    title='Difficult Client Feedback',
    scene='The recommendation depends on staff the client does not have',
    skill='Acknowledge a missed constraint, restate its effect on the recommendation, and agree a credible correction without becoming defensive or promising an untested solution.',
    brief='Consultant Ronan recommends an eight-week pilot requiring two full-time-equivalent staff throughout. Client operations lead Leila points out that only 0.5 full-time equivalent is available during that period, with no additional hiring approved this quarter. Leila had supplied the limit in a discovery email dated 8 September, which the team missed. The proposed workload has not been redesigned. Ronan must own the oversight, correct the assumption, and assess a smaller scope or different timing. He commits to a revised assessment by Wednesday at 15:00 local time, not to a feasible launch by then.',
    cast='Leila | Client operations lead\nRonan | Consultant',
    culture=('Acknowledge before explaining', 'When feedback identifies a genuine omission, an immediate defense can make the client repeat the problem more forcefully. State what the team missed and its consequence first. Then clarify the constraint and the repair plan without turning the conversation into a search for someone else to blame.'),
    a='''What staffing did the recommendation assume? | Two full-time equivalents for eight weeks | Half a full-time equivalent for one day | Unlimited approved hiring | A completed capacity assessment | The proposed pilot explicitly requires two full-time-equivalent staff throughout the eight-week period.
What staffing is actually available? | 0.5 full-time equivalent during the period | Two full-time equivalents | Four additional hires | An unknown unlimited pool | Leila states the available capacity and the absence of approved additional hiring this quarter.
What is promised for Wednesday at 15:00? | A revised assessment | A guaranteed pilot launch | Approved new hiring | Proof that the original recommendation was feasible | Ronan commits to returning with an assessment, not to solving or authorizing the launch by that time.''',
    vocabulary='''client feedback | Information from the client about the work or its usefulness. | respond to client feedback
staffing constraint | A limit on the people or capacity available. | acknowledge a staffing constraint
FTE | Full-time equivalent; capacity expressed relative to a defined full-time workload. | calculate available FTE
capacity assumption | A planning belief about resources available for the work. | correct the capacity assumption
resourcing model | A representation of people, roles, and effort needed. | revise the resourcing model
workload | The amount of work assigned or required. | assess the workload
feasibility | Whether an option can be carried out under relevant conditions. | reassess feasibility
oversight | A missed fact or step; in other contexts, supervisory responsibility. | acknowledge the oversight
fact check | Verification of a statement against relevant evidence. | complete a fact check
discovery record | Information captured during the initial client inquiry. | review the discovery record
assumption register | A documented list of planning assumptions and their status. | update the assumption register
capacity gap | A difference between required and available resources. | quantify the capacity gap
critical task | Work essential to the intended result or necessary sequence. | identify critical tasks
bottleneck | A point limiting the rate or capacity of a process. | locate the bottleneck
phasing | Dividing work into sequenced stages. | assess phased delivery
scope reduction | A deliberate decrease in included work. | evaluate a scope reduction
de-scoping | Removing work from the agreed or proposed scope through the relevant process. | make de-scoping explicit
schedule constraint | A limit on when work can occur or finish. | clarify schedule constraints
hiring approval | Authorization to recruit or add the relevant staff. | confirm hiring approval
client sign-off | The client's relevant formal acceptance or approval. | obtain client sign-off
revision note | A record of what changed and why. | include a revision note
corrective action | A step addressing an identified problem or error. | agree corrective action
accountability | Responsibility for explaining and addressing one's work or decisions. | demonstrate accountability
follow-through | Completion of agreed next steps. | maintain follow-through''',
    precision='Two FTE required and 0.5 FTE available create a 1.5-FTE capacity gap. The available amount is one quarter of the assumed capacity. This does not automatically prove the pilot will take four times as long: tasks, sequencing, and minimum staffing may prevent simple scaling.',
    precision_extra='An apology does not by itself repair the recommendation. Correct the documented assumption, identify affected tasks and outputs, and assess alternatives with the client. The Wednesday commitment is to provide that assessment; feasibility and authorization remain separate questions.',
    phrases='''Acknowledge the miss | You supplied the staffing limit, and we missed it.
State the consequence | Our recommendation depends on capacity that is not available.
Avoid a defensive qualifier | That omission is ours to correct.
Confirm the constraint | The available capacity is half an FTE for this period.
Respect the hiring limit | No additional hiring is approved this quarter.
Quantify the gap | The proposal assumes one and a half FTE more than is available.
Avoid simple scaling | We cannot assume a quarter of the staff means a four-times-longer schedule.
Review the work | We need to identify which tasks and dependencies are affected.
Offer bounded alternatives | We will assess a smaller scope or different timing.
Keep the goal visible | Which parts of the pilot are essential to the decision it must support?
Avoid a promised solution | I cannot yet say which option will be feasible.
Set the next commitment | I will return with the revised assessment by Wednesday at fifteen hundred local time.
Correct the record | We will update the assumption register and mark the previous version as superseded.
Invite factual verification | Please confirm that we have represented the capacity limit correctly.
Separate review from approval | Reviewing an option does not approve its staffing or launch.
Close with follow-through | The next version will state the constraint, its effects, and the assessed alternatives.''',
    notes='''We missed it | Owns the documented omission directly.
Depends on | Connects the incorrect assumption to the recommendation.
Not available | Identifies a practical limit, not unwillingness to cooperate.
Cannot assume | Rejects an unsupported arithmetic shortcut.
Will assess | Commits to work whose result is not yet known.
Superseded | Makes clear which version should no longer guide decisions.''',
    d='''Which opening best addresses the feedback? | You supplied the limit, and we missed it; the recommendation needs revision. | You should have repeated the email more often. | The slide looks strong, so the constraint is irrelevant. | We can call two FTE half an FTE to resolve it. | The appropriate response owns the documented omission and connects it to the need for substantive correction.
What is the capacity gap? | 1.5 FTE | 0.25 FTE | 2.5 FTE | No gap | Two required FTE minus half an available FTE leaves a gap of one and a half FTE.
Why is multiplying the duration by four not a proven fix? | Task sequencing and minimum staffing may prevent simple proportional scaling. | Arithmetic never matters in staffing. | The client has already approved a longer schedule. | The two measures use no common workload basis. | Capacity ratios describe the gap but do not establish how the actual work can be rescheduled.
Which follow-up statement is accurate? | A revised assessment will be supplied by the agreed time; launch feasibility remains to be established. | The pilot is guaranteed to launch by Wednesday. | Hiring is approved because a revision is underway. | The original version should remain the sole decision basis. | The promised deliverable is the revised assessment, not an untested solution or a separate approval.''',
    dialogue='''Leila | This plan still needs two FTEs for eight weeks. My September eighth email said we have half an FTE. How did that constraint disappear from the recommendation?
Ronan | You did, and we missed that [[staffing constraint::The half-FTE limit was already supplied; the consultant missed it during discovery.]]. Our recommendation depends on capacity you do not have. That omission is ours to correct, rather than something you should have had to raise again.
Leila | I need the team to understand that no extra hiring is approved this quarter. We cannot simply add people because the presentation assumes them.
Ronan | I will correct the [[capacity assumption::The plan must reflect half an available FTE and the absence of approved additional hiring.]] explicitly. The current proposal assumes two FTE, while only half an FTE is available during the period. Additional hiring cannot be treated as an agreed solution.
Leila | That is a large difference. I do not want a cosmetic change to the slide while the same workload remains underneath.
Ronan | The [[capacity gap::Two required FTE minus half available leaves 1.5 FTE; changing slide wording does not remove it.]] is one and a half FTE. We need to examine the work itself, not relabel the resource requirement or imply that the original plan fits.
Leila | One suggestion was to stretch the pilot to four times the duration. That sounds neat on a spreadsheet. Does the work actually divide that way?
Ronan | That does not establish [[feasibility::Actual tasks and constraints need examination; a capacity ratio alone does not prove a workable schedule.]]. Some tasks may need people together or depend on a particular sequence. We cannot infer a workable schedule solely by multiplying the duration.
Leila | What will you check before bringing another option back? The operation still needs a useful answer, but the people limit is real.
Ronan | We will revisit the [[resourcing model::This maps people and effort by task so the proposal can be rebuilt around real capacity.]]. Identify the essential tasks, dependencies, and review effort, then assess what could be reduced, phased, or moved without disguising the effect on the pilot's purpose.
Leila | A smaller pilot might be possible, provided it still tests something meaningful and does not leave the committee with an unusable result.
Ronan | Any [[scope reduction::Removing work changes what the pilot can answer, and that consequence must be explicit.]] needs a clear consequence statement. We should say which question the smaller test can answer and which part of the original ambition would remain untested.
Leila | There may also be a later period with different capacity, but I cannot promise those people now.
Ronan | We can assess that [[phasing::Later stages require confirmed resources; possible future availability is not a staffing commitment.]] option with its conditions visible. We should not replace one unsupported staffing assumption with another about resources that may become available later.
Leila | When can I expect a revised assessment? Please distinguish that from telling the committee we have an approved launch plan.
Ronan | By Wednesday at fifteen hundred local time, I will provide the assessment and a [[revision note::The note explains the corrected assumption and changes; Wednesday's promise is an assessment, not launch.]]. It will state what changed, why it changed, and which feasibility or approval questions remain open.
Leila | I can check whether the next version accurately represents our capacity. That review will not authorize additional staffing.
Ronan | Understood. Your factual review is not automatic [[client sign-off::Checking factual accuracy is not the same as approving staffing or implementation.]] on a new staffing plan or launch. We will identify the actual approval route for whichever option proves supportable.
Leila | Then please make sure the previous version is no longer circulated as the current recommendation.
Ronan | We will mark it superseded and maintain [[follow-through::The repair requires completing the promised revision and version correction, not merely apologizing.]]. The next version will show the real constraint, the consequences for the work, and the assessed alternatives rather than repeat the original unsupported plan.''',
    rehearsal=('Read Leila and Ronan aloud, then swap roles. Make the acknowledgment of the missed email direct and unqualified.', 'Check all ten gaps. Reread the staffing arithmetic and explain why it does not establish a four-times-longer schedule.', 'Repeat the revision commitment with its exact deadline. Say revised assessment, not approved launch plan, and retain the capacity limit.'),
    transfer_title='Correct another capacity assumption',
    transfer_setup='A proposed review requires 1.5 FTE, but the client confirms only 0.5 FTE is available. No extra staffing is approved. The consultant promises a revised assessment on Friday, not a completed review.',
    transfer='''Consultant: "The proposal assumed ___." | 1.5 FTE | One and a half full-time equivalents is the stated requirement in the proposal.
Client: "Confirmed available capacity is ___." | 0.5 FTE | Half a full-time equivalent is available, with no extra staffing approved.
Consultant: "The resulting capacity gap is ___." | 1.0 FTE | Subtracting half an FTE from one and a half leaves one FTE.
Client: "Friday's commitment is a ___." | revised assessment | The consultant promises an assessment, not completion or authorization of the proposed review.''',
))


BOOK['units'].append(unit(
    title='Implementation and Change Management',
    scene='Receiving the launch email is not readiness',
    skill='Explain implementation readiness using training, observed practice, operational cover, and ownership rather than treating communication as adoption.',
    brief='A new approval process is scheduled to launch on Monday for 12 managers. All 12 received the announcement; 10 completed the required training, and 4 of those 10 have demonstrated the required tasks in supervised practice. The agreed launch conditions require every participating manager to complete training and demonstrated practice, with operational cover assigned. Eight managers have no verified practice result, two still need training, and cover has not been assigned. Change lead Imani and client process owner David must assess the gaps and seek an authorized revised launch plan, not label unassessed people incompetent.',
    cast='Imani | Change lead\nDavid | Client process owner',
    culture=('Readiness is not a character judgment', 'People may appear resistant when they lack time, practice, access, or support. Ask which prerequisite is missing before attributing motives. A visible gap can guide support and scheduling; it should not become a public ranking of people whose ability has not been assessed.'),
    a='''How many managers have demonstrated the required tasks? | Four | Twelve | Ten | Eight | Four of the ten trained managers have a verified supervised-practice result.
What remains unknown for eight managers? | Their demonstrated-practice result | Whether they received the announcement | Whether every one is incompetent | Whether all training is complete for all twelve | Eight lack verified practice results; absence of assessment is not proof of inability.
Which launch requirement is entirely unassigned? | Operational cover | The announcement recipient list | The title of the process owner | The four completed demonstrations | The brief explicitly states that operational cover has not yet been assigned.''',
    vocabulary='''change management | Coordinated work helping an organization move to and sustain a different way of operating. | plan change management
implementation readiness | Evidence that the required conditions for starting an approach are met. | assess implementation readiness
go-live | The point when a process or system begins actual operation. | confirm go-live readiness
adoption | Actual use of the intended way of working. | measure process adoption
proficiency | Demonstrated ability to perform the relevant tasks to the required level. | verify proficiency
training completion | Finishing the specified learning activity. | record training completion
supervised practice | Task rehearsal with an appropriate person observing and supporting it. | arrange supervised practice
role-based training | Learning tailored to the tasks and responsibilities of a role. | provide role-based training
job aid | A concise reference supporting task performance. | supply a job aid
dry run | A rehearsal before actual operation. | conduct a dry run
practice environment | A setting where tasks can be rehearsed without unintended live effects. | use a practice environment
protected time | Time explicitly set aside from competing work for a specified activity. | allocate protected time
operational cover | Arrangements maintaining normal work while people undertake another task. | assign operational cover
backfill | Replacement capacity for work someone cannot perform during an assignment or absence. | arrange backfill
process owner | The person accountable for a defined process and its ongoing management. | confirm the process owner
change champion | A person helping colleagues understand and adopt an agreed change. | support change champions
readiness gate | A decision point requiring specified launch conditions to be checked. | apply the readiness gate
support model | Arrangements for helping users and resolving problems. | define the support model
hypercare | A defined period of increased support after launch. | plan hypercare
stabilization | Work to bring a new operation into a reliable ongoing state. | monitor stabilization
reinforcement | Follow-up support that helps maintain a desired practice. | provide reinforcement
usage measure | An indicator of whether and how an approach is being used. | define usage measures
benefit realization | Achievement of intended value after a change, under defined measures. | track benefit realization
business-as-usual | Normal ongoing operations outside a temporary change effort. | maintain business-as-usual service''',
    precision='All 12 received the email, 10 completed training, and 4 demonstrated the tasks. These are different measures, not interchangeable adoption rates. Eight have no verified practice result; that is a readiness evidence gap, not evidence that eight people failed an assessment.',
    precision_extra='Training and demonstrated practice are required for each participating manager, and cover is also required. A smaller launch might be assessable, but it is not automatically authorized. Its scope, support, cover, and approval must be explicit before the original plan is replaced.',
    phrases='''Separate communication from readiness | Everyone received the announcement, but the launch conditions are not met.
State the training position | Ten of the twelve managers completed training.
State the practice position | Four have demonstrated the required tasks.
Describe missing evidence fairly | Eight have no verified practice result; that does not mean eight failed.
Name the remaining training | Two managers still need the required training.
Identify the capacity condition | Operational cover has not yet been assigned.
Ask about support | What protected time and practice support do the remaining managers need?
Keep the gate explicit | Each participant must meet the agreed training and practice conditions.
Avoid a blame label | We should not call a missing assessment resistance.
Define a smaller launch | A staged start would need its own approved scope and cover.
Assign ownership | The process owner needs to confirm the operational arrangements.
Prepare assistance | Name the support contact and escalation route before go-live.
Measure actual use | Track the intended workflow after launch, not just attendance at training.
Keep benefits separate | Process use does not by itself prove that the expected benefit has occurred.
Reinforce the change | Review early issues and provide targeted follow-up support.
Close the readiness review | Present the gaps, owners, support needs, and revised decision to the authorized approver.''',
    notes='''Different measures | Keeps communication, learning, performance, and use distinct.
No verified result | Describes missing evidence without inventing failure.
Still need | Identifies a practical next step rather than a personal deficiency.
Each participant | Applies the agreed condition to the relevant launch population.
Would need | Makes a staged launch conditional on its own arrangements.
After launch | Locates actual-use measurement in operation, not before it starts.''',
    d='''Which readiness statement is accurate? | Four have demonstrated the tasks; eight lack verified practice results. | All twelve are ready because the email arrived. | Eight have failed an assessment. | Training completion proves sustained adoption. | The statement reports the actual practice evidence without confusing missing results with failure or communication with readiness.
Which next step addresses the stated gaps? | Arrange remaining training, supervised practice, and operational cover before seeking the launch decision. | Send the same email and declare the conditions met. | Remove the agreed gate without authorization. | Assume normal duties will cover themselves. | The stated launch conditions require learning, demonstrated practice, and cover, so each outstanding requirement needs an owned action.
What does a usage measure show? | Actual use of the defined workflow | That all users can perform every task independently | That the workflow has caused the expected service improvement | That everyone who attended training has adopted the workflow | Usage concerns observed behavior. It does not alone demonstrate independent proficiency, establish a causal service benefit, or prove that every trainee uses the process.
How should a staged launch be described? | A possible revised plan requiring explicit scope, support, cover, and authorization | Already approved because four people demonstrated tasks | A way to hide the eight missing results | A guarantee that every service remains unaffected | A smaller start is an option for assessment, not automatic permission to bypass the agreed decision process.''',
    dialogue='''David | The dashboard is green for Monday because all twelve managers got the announcement. That tells me the email went out. It does not tell me they can run the process.
Imani | It measures communication, not [[implementation readiness::Launch requires the stated conditions; receiving the announcement establishes only that communication occurred.]]. Ten managers completed training, four demonstrated the required tasks, and operational cover is still unassigned. Those are separate conditions, not details the email resolves.
David | The four who demonstrated the tasks are among the ten trained managers. The other eight do not have a verified practice result.
Imani | Then say exactly that about [[supervised practice::An observed task result supports readiness; eight missing results do not mean eight people failed.]]. We should not describe eight people as having failed when they have not supplied a verified result. Missing evidence and demonstrated inability are different.
David | Two managers still need the training itself. Their teams have been busy, and they have not had time set aside.
Imani | They need [[protected time::Time must be set aside for required learning rather than added silently to full workloads.]] and an agreed route to complete the requirement. Calling them resistant would not address the scheduling barrier or tell us whether they can perform the tasks.
David | Even trained managers need an opportunity to practice. We should not assume that attendance establishes independent performance.
Imani | Correct. [[Training completion::Finishing training is separate from demonstrating the tasks under this agreed readiness plan.]] is one condition. The agreed launch gate also requires demonstrated practice for each participating manager, plus cover for their normal responsibilities.
David | The cover issue worries me. If everyone practices at the same time, the existing approval queue still needs to be handled.
Imani | We need [[operational cover::Normal work needs an assigned arrangement while managers prepare; that requirement remains unresolved.]] rather than hope the queue manages itself. Assign the people and timing explicitly, and check the consequences for ongoing service before confirming a launch arrangement.
David | Would a phased start work? Four have completed the training and practice. Could they begin while we arrange preparation and cover for the other eight?
Imani | A staged start can be assessed at the [[readiness gate::A smaller launch still needs its own scope, cover, support, and authorization.]]. It is not automatically approved. We would need a defined scope, cover, support, and the relevant authorization for that revised plan.
David | I will coordinate those operational arrangements. The change team can support the transition, but somebody in the business must own the process afterward.
Imani | That is the [[process owner::The owner holds ongoing operational responsibility, distinct from the change team's temporary transition support.]] role. The handover should state who handles exceptions, maintains the instructions, and decides when an issue needs escalation after the project team steps back.
David | We also need a clear route for questions during the first days. People should not have to find the consultant who last answered an email.
Imani | Define the [[support model::Named assistance and escalation arrangements prevent reliance on informal personal contacts after launch.]] before go-live. A job aid, named contact, and clear escalation route can make assistance predictable, but they do not replace the required practice or operational cover.
David | Once the process starts, we should check whether managers use the intended workflow, rather than keep reporting training attendance as success.
Imani | Yes, measure [[adoption::Adoption means actual workflow use, not pre-launch training attendance or receipt of a notice.]] in operation. Use the agreed workflow measures and investigate barriers fairly, without assuming every exception means someone is unwilling to change.
David | And if usage improves, we still need to examine whether the change produces the expected service improvement.
Imani | That is [[benefit realization::The intended business result requires evidence beyond training completion or use of the workflow.]]. Keep those measures separate. For now, present the readiness gaps, owners, support needs, and proposed revision to the authorized approver instead of leaving Monday marked ready.''',
    rehearsal=('Read David and Imani aloud, then swap roles. Keep announcement, training, demonstrated practice, and operational use distinct.', 'Check the ten gaps. Reread the four-of-twelve readiness position and the conditions on a phased start.', 'Repeat the ownership and support close, then state the separate need to measure service benefits after adoption.'),
    transfer_title='Separate another set of readiness measures',
    transfer_setup='Eight supervisors receive a process notice. Six complete training, and three of those six demonstrate the required tasks. Five have no verified practice result. A start still requires assigned cover and approval.',
    transfer='''Lead: "The notice reached ___." | eight supervisors | Receipt of the notice establishes communication to eight people, not completion of the readiness conditions.
Owner: "Training is complete for ___." | six supervisors | Six completed the specified learning step, which is separate from demonstrated practice.
Lead: "Verified task demonstrations total ___." | three supervisors | Three trained supervisors have demonstrated the tasks under the supplied facts.
Owner: "The five others have ___, not necessarily failed." | no verified practice result | A missing result describes an evidence gap and does not establish inability.''',
))


BOOK['units'].append(unit(
    title='Steering Committees and Final Readouts',
    scene='Agreement on the problem is not approval of an option',
    skill='Close a divided decision meeting by summarizing trade-offs, distinguishing agreement from authorization, and recording the actual decision and owned follow-ups.',
    brief='A steering committee agrees that service handoffs need improvement but is split between two proposals. Option A is estimated at six weeks and $80,000, with manual reporting and staffing still to be confirmed. Option B is estimated at twelve weeks and $140,000, with automated reporting dependent on an unverified system integration. With two minutes left, chair Marta defers the choice to Friday at 10:00 local time. Consultant Ethan will verify the integration position by Thursday at 12:00; operations lead Nora will confirm Option A staffing by the same time. Neither option nor additional implementation spending is approved.',
    cast='Marta | Steering committee chair\nEthan | Consultant presenting the readout',
    culture=('An accurate close can preserve a difficult discussion', 'A presenter may want to leave a meeting with apparent agreement, especially after extensive work. Do not turn shared concern into a fictional approval. State the unresolved trade-off, the authorized next step, and the decision date so the discussion can advance without rewriting what happened.'),
    a='''What does the committee agree on? | The need to improve service handoffs | Approval of Option A | Approval of Option B | Authorization of both budgets | Agreement concerns the problem, while the option choice and implementation spending remain unapproved.
What did Marta decide at the close? | Defer the option choice to Friday at 10:00 local time | Approve automatic rollout that afternoon | Remove every unresolved dependency | Authorize the consultant to choose privately | The chair explicitly defers the choice to the stated meeting rather than selecting either option.
What must Ethan verify by Thursday at 12:00? | The system integration position for Option B | Staffing for Option A on Nora's behalf | A completed twelve-week implementation | A guaranteed $60,000 saving | Ethan owns the integration follow-up; Nora separately owns Option A staffing confirmation.''',
    vocabulary='''steering committee | A governance group overseeing direction and specified decisions. | brief the steering committee
readout | A presentation of findings, status, or decisions. | deliver the final readout
decision log | A record of choices, authority, conditions, and dates. | maintain the decision log
minutes | The formal record of a meeting's relevant discussion and decisions. | confirm the minutes
consensus | Shared agreement, whose scope should be stated. | establish the scope of consensus
dissent | A stated disagreement with a proposed view or choice. | record material dissent
deferred decision | A choice moved to a later specified point. | document a deferred decision
conditional approval | Authorization that depends on stated conditions. | distinguish conditional approval
endorsement | An expression of support that may differ from formal authorization. | clarify the endorsement
decision authority | The role or body permitted to make the relevant choice. | confirm decision authority
option appraisal | A structured comparison of alternatives. | complete the option appraisal
trade-off | A balance between competing benefits, costs, or conditions. | explain the trade-off
implementation estimate | A projection of time or resources needed to execute an option. | qualify the implementation estimate
integration dependency | A reliance on connecting systems or processes successfully. | verify the integration dependency
manual reporting | Reporting that requires human preparation rather than the proposed automation. | account for manual reporting
automated reporting | Reporting produced through defined automated processes. | assess automated reporting
decision criterion | A factor used to compare and choose between options. | prioritize decision criteria
open item | A question or action not yet resolved. | track open items
action owner | The person responsible for a defined next step. | name the action owner
due time | The specified time by which a follow-up is required. | confirm the due time
decision pack | The material supplied to support a forthcoming choice. | update the decision pack
approval status | Whether and on what terms a proposal has been authorized. | state the approval status
record correction | An amendment making a decision record accurate. | request a record correction
handover | Transfer of relevant responsibility and information. | complete the decision handover''',
    precision='Option B is estimated to cost $60,000 more and take six weeks longer than Option A. Those differences do not establish that either is preferable. Reporting capability, staffing, integration, and the relative importance of the criteria remain material to the decision.',
    precision_extra='Deferral is not conditional approval. Here the committee has authorized neither option nor extra implementation spending. A record saying approved subject to checks would misrepresent the meeting, even though named people have been assigned to resolve the open questions.',
    phrases='''State the shared ground | We agree that the handoff problem needs to be addressed.
Name the unresolved choice | We have not agreed which option to implement.
Compare the estimates | Option B is estimated at sixty thousand dollars more and six weeks longer.
State the capability difference | Option A uses manual reporting; Option B proposes automated reporting.
Keep the dependency visible | The integration required for Option B has not been verified.
Keep staffing provisional | Option A staffing still needs confirmation.
Respect the close | The chair has deferred the choice to Friday at ten hundred local time.
Avoid fictional approval | This is a deferred decision, not an approval subject to checks.
Assign the technical follow-up | Ethan will verify the integration position by Thursday at noon.
Assign the operational follow-up | Nora will confirm Option A staffing by the same deadline.
Keep spending status clear | No additional implementation spending has been approved.
Preserve disagreement | Record the material trade-offs without claiming unanimous support for an option.
Prepare the next discussion | Update the option comparison with the two follow-up results.
Clarify authority | The committee will make the option decision at the agreed meeting.
Read back the record | May I confirm the decision, owners, due times, and approval status?
Close accurately | The problem is agreed, the option is deferred, and the next steps are assigned.''',
    notes='''Shared ground | Separates the agreed problem from the unresolved remedy.
Estimated | Preserves the projected status of cost and schedule figures.
Has not been verified | Keeps a material dependency visible.
Deferred, not approved | Distinguishes two different governance outcomes.
By the same deadline | Aligns follow-ups without merging their owners.
Read back | Gives the chair a chance to correct the record before circulation.''',
    d='''Which minute accurately records the meeting? | The option decision is deferred to Friday at 10:00; neither option nor additional spending is approved. | Both options were approved because the problem was agreed. | Option B was approved subject to integration checks. | The consultant may choose whichever option is easier. | The chair deferred the choice and granted no implementation approval, so the record must preserve that status.
What is Option B's estimated cost premium over A? | $60,000 | $140,000 | $20,000 | No difference | Subtracting the eighty-thousand estimate from one hundred forty thousand gives a sixty-thousand premium.
Who owns Option A staffing confirmation? | Nora | Ethan | Every committee member equally, with no named owner | The system integration vendor by default | The brief assigns the staffing follow-up specifically to operations lead Nora.
Which closing behavior is most useful? | Read back the unresolved choice, follow-up owners, deadlines, and approval status. | Describe silence as unanimous option approval. | Remove dissent from the record to make it simpler. | Present estimated timing as a guaranteed delivery date. | An explicit read-back preserves what was actually decided and makes the next actions accountable.''',
    dialogue='''Marta | Two minutes left. We agree the handoffs need fixing, but we have not agreed on A or B. I need a clean close, not a show of consensus we do not have.
Ethan | Then the scope of [[consensus::Agreement concerns the problem, not a selected option or permission to implement it.]] is the problem, not the solution. I will summarize the trade-off without presenting shared concern as approval of either proposal.
Marta | Please keep the cost, timing, and reporting differences clear. The committee has heard many details and needs the comparison in one place.
Ethan | The [[option appraisal::The comparison must include relevant criteria and unresolved assumptions, not just two prices.]] shows A at an estimated six weeks and eighty thousand dollars with manual reporting. B is estimated at twelve weeks and one hundred forty thousand with automated reporting.
Marta | So B is estimated to cost sixty thousand more and take six weeks longer. Its automation is not yet a confirmed capability.
Ethan | Correct. The [[integration dependency::Option B's automated reporting relies on a system connection that has not been verified.]] remains unverified. We should not describe B as ready simply because automated reporting appears in the proposed design.
Marta | Option A is not fully ready either. Nora still needs to confirm that the required staff can be assigned.
Ethan | That [[open item::Option A staffing remains unresolved alongside the integration uncertainty affecting Option B.]] stays visible in the comparison. The shorter estimate does not establish that the people are available, just as B's design does not establish a working integration.
Marta | We do not have enough resolved information to choose now. I am deferring the option decision to Friday at ten hundred local time.
Ethan | I will record a [[deferred decision::Deferral moves the choice to Friday without approving either option in the meantime.]]. Neither option is approved today, and no additional implementation spending is authorized. That is different from approving one option subject to a final check.
Marta | Please do not write approved subject to confirmation. That would suggest we selected something today. We are deferring the choice, not attaching conditions to an approval.
Ethan | I will make the [[approval status::Both options and additional implementation spending remain unapproved despite the assigned follow-up actions.]] explicit. Assigning evidence-gathering actions does not change the status of the implementation proposals or permit anyone to begin the added work.
Marta | Ethan, please verify the integration position by Thursday at noon. Nora will confirm Option A staffing by the same time.
Ethan | I will list each [[action owner::Ethan owns integration verification; Nora owns staffing confirmation, each with the stated deadline.]] separately. My follow-up is the integration position; Nora's is staffing. Both are due Thursday at twelve hundred local time for the updated decision material.
Marta | The next discussion should make clear what we gain and give up with each option, not just list two prices.
Ethan | We will preserve the [[trade-off::Cost and timing must be weighed with reporting capability and feasibility rather than deciding from one figure.]]. The comparison should connect the cost and timing estimates to reporting capability, staffing, and integration, with any remaining uncertainty stated rather than hidden.
Marta | Some members favor speed, while others value automation more. Record that disagreement without presenting it as personal resistance.
Ethan | The relevant [[dissent::The record preserves substantive disagreements without inventing motives or personal resistance.]] concerns priorities and evidence. We can summarize those differences accurately without claiming unanimity or attributing motives that members did not state.
Marta | Read back the close now, so we can correct anything before the record circulates.
Ethan | The [[decision log::The log records deferral, approval status, owners, and deadlines so later readers do not invent authorization.]] will show the agreed problem, the deferred option choice for Friday at ten, and the Thursday-noon integration and staffing follow-ups. Neither option nor extra implementation spending is approved.''',
    rehearsal=('Read Marta and Ethan aloud, then swap roles. State the two options using the same cost and time units.', 'Check the ten gaps. Reread the decision deferral and the Thursday evidence commitments before the Friday meeting.', 'Deliver the final read-back with decision status, owners, deadlines, and unresolved dependencies. Keep agreement on the problem separate from selection of a solution.'),
    transfer_title='Record another deferred choice accurately',
    transfer_setup='A committee agrees on a problem but defers the option choice to Tuesday at 09:00. Mei must confirm staffing by Monday at 13:00. No option or additional spending is approved.',
    transfer='''Chair: "The option choice is ___." | deferred | The committee has postponed the choice, not conditionally approved a proposal.
Presenter: "The next decision time is ___." | Tuesday at 09:00 | Tuesday at nine is the explicitly stated time for the option decision.
Chair: "The staffing action owner is ___." | Mei | Mei has the named responsibility for the staffing follow-up.
Presenter: "Additional spending is ___." | not approved | Agreement on the problem and assignment of follow-ups do not authorize extra spending.''',
))
