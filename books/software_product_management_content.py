"""Original software product-management conversations and bounded practice."""
from books.authoring import unit

BOOK = dict(
    slug='software-product-management', title='Software Product Management English',
    cover_label='Discovery / priorities / evidence / releases',
    cover_title='Software Product\nManagement', cover_size=28,
    tagline='Clarify the problem. Make the trade-off explicit.',
    audience='For product managers, product owners, product analysts, and cross-functional software teams.',
    map_intro='Eight product conversations moving from user problems and priorities to measurable acceptance, experiments, releases, and decisions.',
    notes_title='A product conversation should move a decision.',
    notes_intro='A feature request is not yet a user problem, a roadmap is not unlimited capacity, and a favorable metric is not the whole outcome. Product managers need language that connects user evidence, business commitments, technical constraints, and a clear next decision. These cases practice that work through concrete requests, numerical examples, disagreements, and handoffs.',
    field_notes=[
        ('Ask what the user was trying to do', 'A requested button names one possible solution. Identify the task, the obstacle, and the evidence before deciding what to build. Similar support tickets may describe different problems.', '"Eight tickets concern finding the action; four concern permission to use it."'),
        ('Say what gives way', 'Prioritization has a consequence when capacity is limited. Explain which criterion is being applied and which work is deferred. Calling every request urgent does not create another delivery slot.', '"We can fit the committed audit work and setup recovery; the refresh moves out."'),
        ('Attach a definition to the metric', 'A conversion rate needs a denominator and time window. A load-time requirement needs a start, an endpoint, and test conditions. Keep those definitions near the numbers.', '"Setup completion is measured within seven days of signup for each mature cohort."'),
        ('Finish with the decision and next check', 'A useful discussion ends with an owner, a boundary, and evidence that would change the position. Separate a recommendation from approval and a progress update from a delivery promise.', '"The launch decision remains open until Support confirms the required migration notes."')],
    scope_note='Original fictional English practice, not a product-management certification, statistical analysis service, software security assessment, or release authorization. All teams, data, dates, and decisions are invented. Actual work must follow the organization\'s responsibilities, research safeguards, engineering controls, experiment methods, and applicable requirements.',
    sources=[
        dict(title='Government Digital Service. Learning About Users and Their Needs.', url='https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs', note='Background on distinguishing user needs from proposed solutions and connecting needs to user stories. The cases are original software-product examples.', checked='30 September 2026'),
        dict(title='Schwaber, K., and Sutherland, J. The Scrum Guide, November 2020.', url='https://scrumguides.org/scrum-guide.html', note='Background for Scrum-specific terms such as Product Goal, Product Backlog, and Definition of Done. The book does not assume every organization uses Scrum.', checked='30 September 2026'),
        dict(title='Microsoft Research. Patterns of Trustworthy Experimentation: During-Experiment Stage.', url='https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/', note='Background on monitoring experiments, early results, and appropriate statistical methods. The fictional fixed-horizon case is not a universal test-duration rule.', checked='30 September 2026'),
        dict(title='Google. API Improvement Proposal 180: Backwards Compatibility.', url='https://google.aip.dev/180', note='Background on interface compatibility and the effects of changes on clients. The API trade-off and estimates in this book are invented.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Product Discovery and Problem Framing',
    scene='One button request, two different problems',
    rehearsal=['Read turns 1-10 in pairs. Stress finding and permission as different barriers.', 'Switch roles for turns 11-20. Pause after the two-day limit and the no-approval statement.', 'Check the Download exchange, then read it with six and four clearly distinguished.'],
    skill='Reframe a requested interface addition using supplied support evidence and agree a focused discovery task.',
    brief='Support lead Morgan asks product manager Li for a new Export button on the home page. Their review finds 12 relevant tickets from the past month: eight users could not find the existing action, while four found it but lacked the required permission. The records do not show how common either problem is among all users. No design change is approved. Morgan and Li agree to separate the two issues and prepare a two-day investigation of navigation and permission messaging before choosing a solution.',
    cast='Morgan | Support lead\nLi | Product manager',
    culture=('Clarification is not rejection', 'A stakeholder may offer a solution because it makes a recurring problem tangible. Acknowledge the problem, then separate the proposed implementation from the evidence. Agree a small next step so the conversation does not feel like an indefinite research delay.'),
    a='''What do eight tickets describe? | Difficulty finding the existing Export action | A confirmed outage of every export | Users finding the action but lacking permission | A completed test of the new button | Eight records concern discoverability, while four describe permission restrictions.
What do the other four describe? | The action was found, but the required permission was missing. | The action did not exist anywhere. | Every user completed the export successfully. | A home-page redesign was approved. | Those four users reached the action but could not use it under their permissions.
What have Morgan and Li agreed to do? | Prepare a two-day investigation of navigation and permission messaging. | Build the new home-page button immediately. | Remove all export permissions. | Claim that every user has the same problem. | The agreement is a bounded investigation before selecting or approving a design change.''',
    vocabulary='''product discovery | Work to understand problems and test potential product directions. | conduct product discovery
problem statement | A concise description of a user problem and its context. | frame the problem statement
solution request | A request for a particular implementation or feature. | unpack the solution request
user need | An outcome a user needs to accomplish. | identify the user need
job to be done | The progress or task a user seeks in a given situation. | clarify the job to be done
user segment | A group of users sharing relevant characteristics or needs. | define the user segment
support evidence | Information from support interactions used to investigate problems. | review support evidence
discoverability | How readily users can find an available function. | improve discoverability
permission | Authorization to perform a defined action. | explain the permission requirement
access barrier | A condition preventing a user from reaching or using a capability. | identify the access barrier
navigation path | The sequence of locations used to reach a function. | trace the navigation path
friction point | A step that makes a user task harder or less reliable. | locate a friction point
usability test | Observation of representative users attempting defined tasks. | run a usability test
task success | Completion of a defined user task under stated conditions. | measure task success
research question | A specific uncertainty the investigation aims to resolve. | define the research question
assumption | An unverified premise guiding a proposal or decision. | test the assumption
hypothesis | A proposed explanation or prediction to evaluate. | state the hypothesis
prototype | A representation used to explore or test a design. | compare prototypes
desirability | Whether a solution addresses something users value. | assess desirability
feasibility | Whether a solution can be built and operated under constraints. | assess feasibility
viability | Whether a solution can support the relevant business needs. | assess viability
opportunity | A problem or possibility that could create product value. | evaluate the opportunity
discovery scope | The defined boundaries of the investigation. | bound the discovery scope
evidence gap | Missing information needed to support a conclusion. | identify the evidence gap''',
    precision='Twelve tickets are support evidence, not a census of all users. Eight describe finding the action, and four describe permission. A new button might help the first group but would not itself give the second group authorization to export.',
    precision_extra='The two-day scope creates a decision point without predetermining a design. The investigation can examine navigation and permission messaging separately. Its purpose is not to remove legitimate access controls or claim that the requested button is already proven necessary.',
    phrases='''Acknowledge the problem | We should address the export friction in these tickets.
Separate request from need | The button is one proposed solution, not the problem itself.
Identify the task | What were users trying to export, and from where?
Split the evidence | Eight tickets concern finding the action; four concern permission.
Name the first issue | The existing action may have a discoverability problem.
Name the second issue | The permission message may need a separate review.
Avoid a false fix | Adding a button would not grant authorization.
Limit the inference | These tickets do not establish prevalence across all users.
Ask a focused question | Can users find the action during the relevant task?
Keep safeguards | We are not proposing to bypass access controls.
Bound the investigation | Let us spend two days examining these two paths.
Request useful detail | Link each ticket to the task and navigation path.
Compare possibilities | A clearer label and a new location are different options.
Preserve decision status | No design change is approved yet.
Agree the handoff | Bring the observed paths and findings to the next review.
Close with purpose | Choose the solution after separating the two problems.''',
    notes='''Request | May contain a solution before the underlying need is clear.
Users | Specify which users and what evidence supports the claim.
Cannot | Distinguish cannot find from is not permitted to use.
Discoverable | A function existing does not mean people can locate it.
Research | Give it a question, scope, and decision point.
Validate | State what evidence would support or challenge the assumption.''',
    d='''Which problem framing fits the tickets? | Users encounter two barriers: finding Export and understanding or obtaining the required permission. | The product has no export capability. | All users require an extra home-page button. | Permission should be removed because navigation is unclear. | The evidence separates discoverability and permission without assuming one implementation solves both.
Which statement overclaims the ticket evidence? | Every user is unable to export. | Twelve relevant tickets were reviewed. | Eight tickets concern finding the existing action. | Four describe a permission restriction after finding it. | The reviewed tickets do not establish the experience or prevalence of the entire user population.
Which discovery task is appropriately focused? | Observe the export path and review permission messaging for the two ticket groups. | Redesign every product screen without a defined question. | Approve the requested button before examining either issue. | Ask Support to stop recording permission concerns. | The task addresses the two identified barriers and can inform a bounded solution decision.
Why is adding a button not a complete answer for the four permission cases? | Finding an action and being authorized to use it are separate conditions. | A visible button always removes authorization requirements. | Permission has no relationship to export use. | The four users never found the action. | Those users already located Export, so another location would not itself grant the missing permission.''',
    dialogue='''Morgan | Can we put an Export button on the home page? Support keeps hearing that people cannot export, and I would like something visible we can point them to.
Li | I want to address that, but let us separate the [[solution request::The solution request names a new button, while the underlying evidence may support more than one kind of problem.]] from the problem. The existing action already exports, so what happened when these users tried to reach it?
Morgan | We reviewed twelve tickets from last month. Eight users could not find the action. Four found it but did not have the required permission.
Li | Then [[discoverability::Discoverability concerns finding the available action, which is the barrier described in eight of the twelve tickets.]] is one issue, not the entire set. We should keep the four permission cases separate instead of treating cannot export as a single diagnosis.
Morgan | So the button might help eight of them, but it would leave the other four stuck. Can we keep those groups separate in the ticket summary?
Li | Right. Their [[permission::Permission is authorization to use the action, distinct from being able to locate it.]] problem needs its own review. We can examine the explanation and request path without suggesting that legitimate access controls should disappear.
Morgan | I can attach the relevant ticket excerpts and task details. We should not just count the phrase cannot export when it can describe different experiences.
Li | That makes the [[support evidence::Support evidence provides concrete reported experiences, but the ticket sample does not establish prevalence among all users.]] more useful. It still does not tell us how common either problem is across all users, so keep that broader claim out of the summary.
Morgan | For the navigation cases, I would like to know where people started and which menu labels they tried. That could explain why the existing location was missed.
Li | Trace the [[navigation path::The navigation path records the sequence users followed and can reveal where they missed the existing action.]] during the actual task. A clearer label, a different location, and an additional button are distinct options rather than interchangeable fixes.
Morgan | How much investigation are we talking about? Support needs a date for an update, even if we cannot promise a fix yet.
Li | Let us set a two-day [[discovery scope::Discovery scope bounds the work to navigation and permission messaging, creating a specific decision point before design selection.]]. We will examine these two paths and bring the findings back before choosing a design change.
Morgan | For the navigation work, the question should be whether people can find the action when they need it, not whether they like our preferred button idea.
Li | That is a better [[research question::The research question tests the user's task and obstacle instead of soliciting approval of a predetermined button solution.]]. We can observe what happens and compare the evidence with the assumption behind the request.
Morgan | The permission review should also check whether the message explains why access is unavailable and what the legitimate next step is. It should not promise access automatically.
Li | Agreed. Keep the [[user need::The user need concerns accomplishing the export task appropriately, rather than mandating a specific interface element.]] separate from a specific control. The product should help users understand the path without disguising an authorization decision as a navigation change.
Morgan | Once we have the observations, we can decide whether to test a revised label, a new location, or another design. We do not have to build every option.
Li | A [[prototype::A prototype can test a proposed design before committing to full implementation, using the findings from the bounded investigation.]] may help compare the relevant direction before implementation. The choice should follow what we learn, not merely the most visible suggestion in the initial request.
Morgan | I will prepare the ticket groups and coordinate the review. Our status will say that we have agreed the investigation, not approved a new home-page feature.
Li | Good. Record the [[problem statement::The problem statement separates the two observed barriers and gives the next design discussion an evidence-based starting point.]] with both barriers and the remaining uncertainty. That gives Support a clear next step and gives the product team a useful basis for choosing a solution.''',
    transfer_title='A visible action can still be restricted',
    transfer_setup='Ten tickets are reviewed. Six users could not find Download. Four found it but lacked permission. No design change is approved, and the records do not represent all users.',
    transfer='''Support: "Six tickets concern ___." | discoverability | Those users could not find the existing action, which is a discoverability problem.
Product: "Four concern ___." | permission | The other users found Download but lacked authorization to use it.
Support: "A design change is not yet ___." | approved | The briefing explicitly leaves design approval absent at this stage.
Product: "These records are a ticket sample, not all ___." | users | The supplied records do not establish the experience of every user.'''))


BOOK['units'].append(unit(
    title='Roadmaps and Prioritization',
    scene='Three urgent requests, two delivery slots',
    rehearsal=['Read turns 1-10. Emphasize two slots and the fixed-commitment rule.', 'Switch roles for turns 11-20. Contrast a review point with a delivery promise.', 'Check the X/Y/Z exchange. Read the selected pair and deferred item aloud in order.'],
    skill='Apply agreed priorities to a capacity conflict, explain the displaced work, and distinguish a review date from a delivery promise.',
    brief='Product owner Nora and commercial sponsor Samir review three features. A improves setup recovery and directly supports the agreed activation goal. B provides audit export needed for a recorded October 31 customer commitment. C refreshes the home page; no fixed commitment or activation evidence is supplied for it. Each feature needs one of two available delivery slots, and splitting them is not feasible this cycle. The agreed rule is to protect fixed commitments first, then the activation goal. Nora proposes B and A, with C reviewed again in two weeks.',
    cast='Nora | Product owner\nSamir | Commercial sponsor',
    culture=('Make the deferred work visible', 'A clear no for this cycle can be more useful than an impossible yes. Explain the shared criterion, the capacity constraint, and the work that would be displaced by a change. Give the deferred request an honest review point without quietly promising the next release.'),
    a='''Which feature addresses the recorded fixed commitment? | B, audit export | A, setup recovery | C, home-page refresh | All three have the same recorded commitment | The briefing identifies B as required for the October 31 customer commitment.
Which pair follows the agreed priority rule? | B and A | A and C | B and C | All three within two slots | B protects the fixed commitment, and A then supports the agreed activation goal.
What does the two-week date mean for C? | A review point, not a promised delivery date | Guaranteed production release | Evidence that C already supports activation | Permission to use a third slot | Nora proposes reviewing C again in two weeks, not delivering or approving it then.''',
    vocabulary='''product roadmap | A communication of intended product direction and priorities over time. | update the product roadmap
product goal | The future product outcome guiding a defined body of work. | align with the product goal
prioritization criterion | A stated basis for ordering competing work. | apply prioritization criteria
capacity constraint | A limit on work the team can undertake in the period. | state the capacity constraint
delivery slot | A defined allocation of capacity for planned work. | allocate a delivery slot
fixed commitment | A recorded obligation treated as non-discretionary in the stated planning rule. | protect a fixed commitment
time-critical work | Work whose value or obligation depends on a specific timing need. | identify time-critical work
opportunity cost | The value of the best displaced alternative. | explain opportunity cost
trade-off | A choice that gains one benefit while giving up another. | make the trade-off explicit
sequencing | Ordering work to respect priorities and dependencies. | agree the sequencing
dependency | An input or condition required for another item to proceed. | identify a dependency
deferred item | Work deliberately moved outside the current period. | record a deferred item
backlog ordering | Arranging planned work by current priority. | revise backlog ordering
sponsor | A stakeholder advocating or accountable for a proposed investment. | brief the sponsor
escalation | Raising a decision beyond the current authority or agreement. | define the escalation route
decision rule | An agreed method for selecting among alternatives. | use the decision rule
decision log | A record of choices, rationale, and relevant context. | maintain the decision log
scope split | Dividing work into independently useful smaller parts. | assess a scope split
confidence level | Stated certainty in an estimate or claim under its defined basis. | qualify the confidence level
effort estimate | An assessment of the work needed to deliver an item. | review the effort estimate
cost of delay | The consequence of postponing work over a stated period. | assess cost of delay
review trigger | A condition prompting reconsideration of a decision. | define the review trigger
planning horizon | The period covered by a planning discussion. | state the planning horizon
forecast | A current estimate of a future result, not necessarily a commitment. | distinguish forecast from commitment''',
    precision='With two slots and three one-slot features, selecting C displaces A or B. Under the supplied rule, B comes first because of the recorded commitment, followed by A because it supports activation. No evidence permits treating all three as simultaneously feasible.',
    precision_extra='A review in two weeks is not a promise to deliver C in two weeks or in the next cycle. New evidence can reopen the priority decision, but it must be evaluated against the same capacity and commitments unless those constraints are explicitly changed.',
    phrases='''State the capacity | We have two slots for three one-slot features.
Name the shared rule | Fixed commitments come first, then the activation goal.
Protect the commitment | B addresses the recorded October 31 commitment.
Connect the outcome | A directly supports setup recovery and activation.
Qualify the third request | C has no supplied fixed commitment or activation evidence.
Make the selection | On this basis, I recommend B and A.
Name the consequence | C moves outside this cycle.
Ask what gives way | Which selected item would C displace?
Check splitting honestly | The team has assessed splitting as infeasible this cycle.
Avoid false capacity | Calling all three urgent does not create another slot.
Invite relevant evidence | What new fact would change C's priority under our rule?
Separate appeal from decision | I can record your objection without pretending the priority changed.
Define reconsideration | We will review C again in two weeks.
Avoid a hidden promise | That review date is not a release commitment.
Record the basis | Put the selected pair and displaced work in the decision log.
Close consistently | Communicate the same scope and timing status to every sponsor.''',
    notes='''Urgent | Ask for the actual timing consequence or obligation.
Priority | Meaningful only when it changes the order or allocation.
Next | Avoid implying the deferred item is automatically next to ship.
Capacity | A constraint to verify, not a number changed by enthusiasm.
Review | A decision checkpoint, not necessarily approval or delivery.
Committed | Distinguish a recorded obligation from an internal preference.''',
    d='''Which response best explains deferring C? | B protects the fixed commitment and A supports activation; C does not fit the two-slot capacity. | C is unimportant because its sponsor disagrees. | C is secretly included without additional capacity. | C will definitely ship at the two-week review. | The explanation applies the supplied rule and states the capacity consequence without personal dismissal or an invented date.
If C is added with no capacity change, what must happen? | A or B must be displaced. | All three still occupy only two slots. | Splitting becomes feasible because the sponsor requests it. | The October 31 commitment is automatically withdrawn. | Each feature requires one slot and the briefing rules out splitting, so another selection must change.
What new information could justify reconsideration? | Relevant evidence changing C's position under the agreed criteria | The same urgent label repeated more loudly | A review date mislabeled as a delivery promise | An assumption that effort estimates no longer matter | A priority decision can change with relevant evidence, not merely repeated preference.
Which statement about the review is accurate? | C will be reconsidered in two weeks without a promised delivery date. | C is guaranteed in production within two weeks. | The review cancels the current pair automatically. | The review proves C has no possible future value. | A reconsideration checkpoint preserves flexibility without creating an unsupported release commitment.''',
    dialogue='''Samir | All three sponsors are calling their feature urgent. My team wants the home-page refresh included because we have already discussed it in several customer conversations.
Nora | We have a [[capacity constraint::The capacity constraint is two available delivery slots for three one-slot features, with no feasible split this cycle.]]. There are two slots, and the team has assessed each feature at one slot. We need to choose rather than announce a scope the team cannot deliver.
Samir | Understood. But I need more than "there is no room" for the sponsor. Can you walk me through the rule we agreed?
Nora | The agreed [[decision rule::The decision rule protects recorded fixed commitments first and then the activation goal, rather than ranking sponsors by forcefulness.]] is fixed commitments first, then the activation goal. It gives us a shared basis instead of comparing the intensity of each sponsor's request.
Samir | The audit export has the October thirty-first customer commitment. That is different from my team's interest in showing a more current home page.
Nora | Yes. B protects that [[fixed commitment::The fixed commitment is the recorded October 31 audit-export obligation that the supplied rule prioritizes.]]. We should not displace it without explicitly addressing the obligation and the required authority, rather than treating it as another optional preference.
Samir | That leaves one slot. Setup recovery directly supports activation, which is the outcome we agreed to improve this cycle. We have not supplied similar evidence for the refresh.
Nora | A therefore aligns with the [[product goal::The product goal is the agreed activation outcome, which setup recovery directly supports in the supplied facts.]]. My recommendation is B and A, with C outside this cycle. That is a relative priority decision, not a claim that C can never matter.
Samir | Could we include a smaller refresh alongside the other two? I want to test that option before telling the sponsor the request has moved out.
Nora | We asked about a [[scope split::A scope split would divide work into useful smaller parts, but the briefing states it is not feasible this cycle.]], and the team says it is not feasible this cycle. We cannot count on a smaller item without a supported estimate and usable scope.
Samir | Then putting C back in would require removing one of the selected features. The trade-off should be stated plainly instead of hidden in an overloaded roadmap.
Nora | Exactly. Explain the [[opportunity cost::Opportunity cost makes the displaced alternative visible when C competes for one of the two available slots.]]. Choosing the refresh means giving up the selected work that would otherwise occupy that slot under our current capacity.
Samir | I can explain that to the sponsor. How can we bring new evidence back if a specific customer consequence becomes clearer?
Nora | Set a [[review trigger::A review trigger identifies new evidence or a condition that would justify reconsidering C under the agreed decision rule.]]. Relevant new evidence can change the decision, but the review must still account for the fixed commitment, activation goal, and available capacity.
Samir | Two weeks is a review, then, not a release date? I need to correct that in my customer-call notes before it becomes an expectation.
Nora | Correct. C is a [[deferred item::A deferred item is outside the current cycle; its review date does not guarantee a future delivery slot.]], and the two-week meeting is a review point. It is not automatic approval for the next cycle or a hidden delivery commitment.
Samir | Please record the rationale for every sponsor. Different informal explanations could make a consistent decision look arbitrary.
Nora | I will update the [[decision log::The decision log preserves the selected pair, shared rationale, capacity constraint, and conditions for reconsideration.]] with B and A, the capacity limit, and the review point for C. Your concern and the relevant evidence request will be recorded too.
Samir | Then I will tell the commercial team that the refresh is deferred under the agreed rule, not canceled forever, and that the next discussion needs evidence rather than another urgency label.
Nora | That keeps the [[product roadmap::The product roadmap communicates the selected direction and priorities without implying that every requested feature is simultaneously committed.]] honest. We can pursue the current goal while leaving a clear route to reconsider the deferred request when the facts change.''',
    transfer_title='Two slots still mean two choices',
    transfer_setup='There are two slots. X protects a fixed commitment; Y supports the agreed activation goal; Z has neither supplied basis. Each needs one slot, and splitting is infeasible. The rule prioritizes commitments, then activation.',
    transfer='''Product: "The first selection is ___." | X | X protects the fixed commitment, which the stated rule ranks first.
Sponsor: "The second selection is ___." | Y | Y supports activation, the next criterion after fixed commitments.
Product: "The deferred item is ___." | Z | Z has neither supplied priority basis and cannot fit alongside both selected items.
Sponsor: "Adding it requires a ___." | trade-off | With unchanged two-slot capacity, adding Z displaces one of the selected features.'''))


BOOK['units'].append(unit(
    title='User Stories and Acceptance Criteria',
    rehearsal=['Read turns 1-10. Stress usable, at least 95, and every run.', 'Switch roles for turns 11-20. Keep criterion passed distinct from story complete.', 'Check the transfer. Read 93 and 95 distinctly, then stress fails in the conclusion.'],
    scene='Quickly needs a clock and a test condition',
    skill='Turn a vague performance request into a checkable criterion and distinguish that criterion from the wider completion standard.',
    brief='Product manager Eva and test lead Omar refine a story saying an authorized editor should open the records page quickly. They agree a fictional acceptance test: 100 navigations with the fixed 1,000-record dataset and test profile N, timed from the navigation click until records and the primary action are usable. At least 95 runs must finish within 2 seconds, and every run within 5 seconds without an error. A trial records 96 within 2 seconds and four more within 4.5 seconds, with no errors. Other completion checks remain open.',
    cast='Eva | Product manager\nOmar | Test lead',
    culture=('Define completion together', 'A product manager can specify the user outcome without prescribing every engineering detail. A test lead can make it measurable without replacing that outcome with a convenient technical proxy. Agree the user state, timing boundaries, test basis, and pass rule in language both can defend.'),
    a='''When does the stated timing end? | When records and the primary action are usable | When the first network request is sent | When a blank loading shell appears | When the tester closes the browser | The criterion ends at usable content and action, not merely the start of technical activity.
Does the trial meet the stated timing and error criterion? | Yes; 96 finish within 2 seconds and all finish within 5 seconds without errors. | No; all 100 had to finish within 2 seconds. | Yes; a blank page appeared quickly. | No; the dataset had to contain 100 records. | The supplied rule requires at least 95 fast runs and all runs within the five-second ceiling, with no errors.
What remains open after this trial? | Other completion checks | The supplied count of 100 navigations | The stated dataset size of 1,000 records | The trial's no-error observation | Passing this criterion does not complete the other checks explicitly left open in the briefing.''',
    vocabulary='''user story | A short description of user, capability, and intended benefit. | refine the user story
acceptance criterion | A checkable condition for accepting a specific item. | define acceptance criteria
Definition of Done | The agreed quality standard for a completed increment in Scrum. | meet the Definition of Done
functional requirement | A required behavior or capability. | specify a functional requirement
nonfunctional requirement | A required quality or constraint, such as performance. | clarify a nonfunctional requirement
precondition | A state that must exist before the test or action. | state the precondition
postcondition | A state expected after the action completes. | verify the postcondition
test fixture | Controlled data and setup used for a repeatable test. | prepare the test fixture
test profile | The defined environment and conditions for a test. | use the agreed test profile
navigation event | The action that initiates movement to a page or view. | timestamp the navigation event
usable state | The condition in which the intended task can actually be performed. | define the usable state
latency | Time between a defined initiating event and response. | measure latency
response-time threshold | A specified boundary for an acceptable duration. | set the response-time threshold
percentile | A position in a distribution defined by a proportion of observations. | report the percentile basis
tail latency | Response times in the slower part of a distribution. | monitor tail latency
timeout | A defined limit after which an operation stops waiting. | specify timeout behavior
error state | A condition showing that the requested operation did not complete as intended. | handle the error state
empty state | The interface shown when no relevant content is available. | design the empty state
edge case | An unusual or limiting situation that requires defined behavior. | cover edge cases
happy path | The intended successful sequence without exceptional conditions. | test the happy path
testability | The ability to evaluate a requirement with a defined check. | improve testability
ambiguity | Wording that allows conflicting interpretations. | remove ambiguity
acceptance test | A test evaluating agreed acceptance conditions. | run the acceptance test
completion evidence | Records supporting a claim that required work is complete. | attach completion evidence''',
    precision='The empirical rule here is at least 95 of 100 runs within 2 seconds, with every run within 5 seconds and no errors. It is not an average-time target. A different percentile calculation convention should not silently replace the agreed count-based test.',
    precision_extra='The trial passes this criterion: 96 exceeds the required 95, and the four slower runs still finish before 5 seconds. The evidence applies to the fixed dataset and profile N. Other environments and the remaining completion requirements are not established by this result.',
    phrases='''Clarify the user state | The story concerns an authorized editor.
Replace the adjective | Quickly needs a measurable timing rule.
Define the start | Start the clock at the navigation click.
Define the finish | Stop when the records and primary action are usable.
Fix the test data | Use the agreed 1,000-record dataset.
Name the environment | Run under test profile N.
State the main threshold | At least 95 of 100 runs must finish within 2 seconds.
Bound the slow runs | Every run must finish within 5 seconds.
Include failure behavior | The test must complete without an error.
Avoid a convenient proxy | A visible loading shell is not a usable records page.
Distinguish statistics | An average does not establish the required run count.
Report the evidence | Ninety-six runs met 2 seconds; all met the ceiling.
Keep the scope | This result applies to the defined test conditions.
Separate completion layers | This acceptance criterion does not replace the Definition of Done.
Preserve open work | The remaining completion checks are still open.
Close the story carefully | Attach the evidence before changing the completion status.''',
    notes='''Quickly | A preference until the measurement and limit are defined.
Loaded | Could mean visual, network, or usable completion; specify it.
Within | Includes the stated boundary unless the agreed rule says otherwise.
Average | Does not describe every run or the slow tail.
Accepted | Specify which criterion or work item was accepted.
Done | Requires the applicable completion standard, not only one passing test.''',
    d='''Which criterion matches the agreed performance rule? | At least 95 of 100 defined navigations usable within 2 seconds, all within 5, without errors | Average navigation time below 2 seconds, with every run below 5 | At least 95 loading shells visible within 2 seconds, with no request errors | All 100 navigations usable within 5 seconds, regardless of the two-second count | The correct criterion preserves usable completion, both count and ceiling requirements, and the no-error condition. An average or a loading shell measures something different.
What if only 94 runs meet 2 seconds, while all finish before 5 seconds without errors? | The stated criterion fails. | It passes because the slow ceiling is met. | It passes because 94 is close to 95. | No conclusion is possible about the supplied count rule. | The rule independently requires at least 95 runs within two seconds, so meeting the ceiling alone is insufficient.
Why time until the primary action is usable? | The user must be able to perform the intended task, not merely see a loading shell. | A visual placeholder always proves the task can be completed. | Network start and task readiness are identical by definition. | The dataset size becomes irrelevant once anything appears. | The defined endpoint connects performance evidence to usable behavior instead of an earlier technical event.
What can Eva say after the actual trial? | This criterion passed under profile N; other completion checks remain open. | Every possible user environment is proven fast. | The whole increment automatically meets all quality requirements. | The four slower runs were errors despite completing within the ceiling. | The evidence supports the stated test result, not untested conditions or all remaining work.''',
    dialogue='''Eva | The story says an authorized editor should open the records page quickly. Engineering asked what quickly means, and I can see that we have left too much room for interpretation.
Omar | Let us define an [[acceptance criterion::An acceptance criterion turns the vague performance request into a specific condition that can be evaluated.]] tied to the task. What event starts the timing, and what must be usable before we say the page has finished loading?
Eva | Start at the navigation click. Finish when the records are available and the primary action works, not when the user sees only a loading shell.
Omar | That defines the [[usable state::The usable state requires the records and primary action to be available, avoiding an earlier but misleading loading milestone.]]. A visible placeholder is not enough because the editor still cannot perform the intended task at that point.
Eva | We should fix the data as well. Let us use the agreed one-thousand-record dataset so a smaller empty page does not stand in for the actual check.
Omar | Use that [[test fixture::The test fixture supplies controlled data and setup, here the fixed one-thousand-record dataset.]] with profile N. The evidence needs its configuration attached so another reviewer can understand what was measured and repeat the check appropriately.
Eva | For the main threshold, I propose that at least ninety-five of one hundred navigations finish within two seconds. We should also define what happens to the slower runs.
Omar | Add a [[response-time threshold::The response-time threshold defines an acceptable duration; the case also sets a separate ceiling for every run.]] of five seconds for every run, with no errors. That prevents a good fast-run count from concealing an unacceptable slow tail.
Eva | The dashboard gives me an average. Could you send the individual run counts as well? Otherwise I cannot check our ninety-five-out-of-a-hundred rule.
Omar | Correct. [[Tail latency::Tail latency concerns the slower responses that can be hidden by an average and are bounded here by the five-second ceiling.]] matters to the experience too. Keep the exact rule in the story rather than replace it with a different summary statistic during reporting.
Eva | The trial produced ninety-six runs within two seconds. The other four finished within four point five seconds, and there were no errors.
Omar | Then this [[acceptance test::The acceptance test passes because the recorded run counts, ceiling, and no-error condition all satisfy the agreed rule.]] passes on the supplied result. Ninety-six meets the minimum, and all one hundred remain within the separate ceiling without an error.
Eva | I can report that clearly, but I should not imply that every device, network, or dataset has been tested. The result belongs to the agreed setup.
Omar | Keep the [[test profile::The test profile identifies the environment and conditions under which the passing result was obtained.]] visible. The conclusion applies to profile N and the defined data, not automatically to every environment a future user might have.
Eva | Can I mark the performance criterion passed and leave the story open? We still have completion checks outstanding, and I do not want to hide them.
Omar | Exactly. The [[Definition of Done::The Definition of Done is the wider agreed quality standard in Scrum, not a substitute label for one story-specific passing criterion.]] is a separate completion standard where the team uses Scrum. One story-specific criterion does not replace the agreed quality requirements for the increment.
Eva | We should preserve the distinction between an ordinary successful path and the other states the product must handle. This test did not define every exceptional situation.
Omar | Yes. The [[happy path::The happy path is the intended successful sequence; covering it does not automatically address all exceptional or empty states.]] is not the entire behavior of the product. Keep the remaining checks visible rather than let one useful test stand for everything.
Eva | I will attach the results, keep the unresolved checks open, and use the exact criterion in the next review. That should end the debate over what quickly means here.
Omar | The [[completion evidence::Completion evidence records what has actually passed and what remains outstanding, supporting an accurate completion decision.]] will then support a precise status. We have a measurable requirement and a passing result within scope, without quietly changing the meaning of done.''',
    transfer_title='A ceiling does not replace the main rule',
    transfer_setup='A test requires at least 95 of 100 runs within 2 seconds and all within 5 seconds without errors. The result is 93 within 2 seconds; the remaining seven finish within 4 seconds without errors.',
    transfer='''Tester: "The fast-run count is ___." | 93 | The result records ninety-three runs within the two-second threshold.
Product: "The required fast-run count is at least ___." | 95 | The acceptance rule requires at least ninety-five runs within two seconds.
Tester: "The overall criterion ___." | fails | The fast-run requirement is missed even though the five-second ceiling and error condition are met.
Product: "The recorded timing unit is ___." | seconds | All thresholds and observed durations in the briefing are expressed in seconds.'''))

BOOK['units'].append(unit(
    title='Metrics, Funnels, and Product Analytics',
    rehearsal=['Read turns 1-10. Keep signup counts and completion rates clearly separated.', 'Switch roles for turns 11-20. Stress possible explanations without making them causes.', 'Check the transfer. Read each rate and the percentage-point decline with its unit.'],
    scene='More signups, fewer completed setups',
    skill='Explain opposing funnel movements using aligned cohorts, counts, rates, and an explicit limit on causal interpretation.',
    brief='Analyst Imani and growth lead Alex compare two fully matured signup cohorts using the same seven-day setup-completion definition. The earlier cohort has 1,000 signups and 600 completions; the later cohort has 1,500 signups and 500 completions. Event counts are verified. A campaign ran during the later period, but other conditions were not controlled, and no causal attribution is established. Alex calls the campaign a complete success. Imani must explain acquisition growth alongside the decline in completed setups and completion rate.',
    cast='Alex | Growth lead\nImani | Product analyst',
    culture=('Report the whole defined outcome', 'Different teams may optimize different stages of a funnel. Acknowledge the stage that improved, then show what happened at the next meaningful outcome. Use aligned time windows and denominators so a discussion about success does not become a contest between selectively chosen metrics.'),
    a='''How did signup count change? | It rose from 1,000 to 1,500, a 50% increase. | It fell from 600 to 500. | It stayed at 1,000. | It rose by 500 percentage points. | Five hundred additional signups divided by the original thousand gives a fifty-percent increase.
How did completed setup count change? | It fell from 600 to 500. | It rose from 1,000 to 1,500. | It remained at 600. | It rose to 1,500 because every signup completed. | The supplied completion counts show one hundred fewer completed setups in the later cohort.
What makes the time windows comparable here? | Both cohorts have completed the same seven-day observation window. | The later cohort is measured only on its first day. | Each cohort uses a different definition of setup. | The campaign name replaces the observation period. | The briefing explicitly says both cohorts are fully matured under the same seven-day definition.''',
    vocabulary='''funnel | A defined sequence of steps toward a product outcome. | analyze the funnel
signup | A recorded account-registration event under the stated definition. | count valid signups
activation | A defined early milestone indicating initial product value. | define activation
setup completion | Completion of the specified initial configuration steps. | measure setup completion
conversion rate | The share of an eligible population completing a defined action. | calculate conversion rate
cohort | A group sharing a defined starting event or characteristic. | compare signup cohorts
observation window | The period during which outcomes are counted. | align the observation window
mature cohort | A cohort whose required observation period has elapsed. | use mature cohorts
event definition | The rules specifying when an analytics event is recorded. | maintain event definitions
instrumentation | The implementation used to collect product events and measurements. | verify instrumentation
event property | A recorded attribute attached to an event. | validate event properties
unique user | A distinct user under the stated identity rule. | count unique users
deduplication | Removing repeated records of the same defined event or entity. | apply deduplication
denominator | The eligible total used to calculate a rate. | verify the denominator
drop-off | Loss of users between defined funnel steps. | locate funnel drop-off
cohort maturity | The extent to which a cohort has completed its observation period. | check cohort maturity
segmentation | Dividing data into relevant user or context groups. | segment by acquisition channel
channel mix | The composition of traffic from different acquisition sources. | examine channel mix
attribution | Assignment of credit for an outcome under a stated method. | qualify campaign attribution
retention | Continued use or return under a defined time and activity rule. | measure retention
leading indicator | A measure expected to precede a later outcome. | validate a leading indicator
lagging indicator | A measure reflecting an outcome after relevant activity occurs. | report a lagging indicator
guardrail metric | A measure used to detect unacceptable side effects. | monitor guardrail metrics
metric contract | An agreed definition of a metric's event, population, and calculation. | document the metric contract''',
    precision='Signups rose 50%, but completed setups fell by 100, about 16.67% relative to 600. Completion rates fell from 60% to about 33.33%, a decline of about 26.67 percentage points. Neither the count nor the rate alone describes the entire funnel.',
    precision_extra='Both seven-day windows are complete, so the later cohort is not simply younger in this case. The numbers are verified, but their causes remain unestablished. Channel mix, product friction, and other explanations need investigation rather than being asserted from the two totals.',
    phrases='''Acknowledge acquisition | Signups increased from 1,000 to 1,500.
State the next outcome | Completed setups fell from 600 to 500.
Give the earlier rate | The earlier completion rate was 60%.
Give the later rate | The later completion rate was approximately 33.33%.
Name the rate difference | That is a decline of approximately 26.67 percentage points.
Keep counts visible | We have 100 fewer completed setups despite more signups.
Confirm timing | Both cohorts have a full seven-day window.
Confirm definitions | The setup-completion definition is unchanged.
Avoid a blanket success label | Acquisition improved, but the downstream outcome worsened.
Separate evidence from cause | The comparison does not isolate the campaign's effect.
Ask about the mix | Did the composition of acquisition channels change?
Locate the friction | Which setup step accounts for the observed drop-off?
Protect the denominator | Use eligible signups from the same cohort.
Avoid immature comparisons | Do not compare a one-day cohort with a complete seven-day cohort.
Define the next analysis | Segment the funnel and check the relevant step-level evidence.
Close the update | Report acquisition, completion count, completion rate, and the causal limitation.''',
    notes='''Success | Specify the objective and stage used to judge it.
Conversion | Needs a starting population, event, and time window.
Users | Define identity and avoid counting repeated events as people.
Drop-off | Locate the step; a total alone does not identify the obstacle.
Attributed | Depends on a method and is not automatically causal proof.
Mature | Describes observation time, not product-market maturity.''',
    d='''Which summary represents both movements? | Signups increased, while completed setups and the setup-completion rate declined. | The campaign was a complete success because signups rose. | Setup completion improved because the denominator was larger. | The later cohort had not completed its observation window. | The supplied counts show acquisition growth together with fewer completions and a lower rate.
What is the later setup-completion rate? | Approximately 33.33% | 50% | 60% | 150% | Five hundred completions divided by fifteen hundred signups equals one third.
What is the approximate rate decline in percentage points? | 26.67 | 16.67 | 50.00 | 100.00 | The earlier sixty-percent rate minus approximately thirty-three point three three percent is about 26.67 points.
Which causal statement is supported? | The campaign's causal effect is not isolated by this comparison. | The campaign definitely caused all setup losses. | A specific product bug is already established as the cause. | Verified counts automatically prove the marketing explanation. | Verified observations do not remove the uncontrolled differences between the two periods.''',
    dialogue='''Alex | Signups increased from one thousand to fifteen hundred during the campaign period. I called that a complete success in the update, but you flagged the setup numbers.
Imani | The [[funnel::The funnel includes the later setup outcome as well as signup, so acquisition alone cannot represent the whole result.]] shows a mixed result. Completed setups fell from six hundred to five hundred, even though more people entered at the signup stage.
Alex | I want to make sure the later group has had enough time. Comparing a new cohort with an older one could make completion look worse simply because users are still setting up.
Imani | Each is a [[mature cohort::A mature cohort has completed the defined observation period; both groups here have a full seven-day window.]] in this comparison. Both have a full seven-day window, and the setup-completion definition is the same in both periods.
Alex | Then the counts describe a real difference in the recorded outcome, not merely an incomplete observation window. We gained five hundred signups but lost one hundred completed setups.
Imani | Correct. Keep the [[denominator::The denominator is each cohort's eligible signup count, which must remain aligned with its own completions.]] with each rate. The earlier rate is six hundred divided by one thousand, while the later is five hundred divided by fifteen hundred.
Alex | That is sixty percent before and about thirty-three point three three percent later. The decline in the rate is larger than the decline in the completion count.
Imani | Yes. The [[conversion rate::The conversion rate is the share of signups completing setup within seven days, not the raw completion count.]] fell by about twenty-six point six seven percentage points. The count and the rate answer related but different questions.
Alex | I have sixteen point six seven percent in my slide. That is the fall in completed setups, not the change in conversion rate. I need separate labels.
Imani | Exactly. State [[setup completion::Setup completion is the defined downstream event whose count and rate both declined in the supplied comparison.]] in both forms when needed: five hundred completions and roughly thirty-three percent of signups. Neither should disappear behind the favorable acquisition headline.
Alex | Could the campaign have attracted people who were less ready to configure the product? That seems plausible, but we have not examined the composition of the new signups.
Imani | Investigate [[channel mix::Channel mix concerns the composition of acquisition sources and is a possible explanation to investigate, not an established cause here.]] and other relevant differences. Plausibility is a reason to analyze, not enough to assign the entire decline to the campaign.
Alex | Can we break setup into steps for the next review? I can see the loss in the total, but not where people got stuck.
Imani | Locate the [[drop-off::Drop-off identifies loss between defined funnel steps; step-level evidence is needed to locate the obstacle.]] using the appropriate step-level evidence. A product problem, a changed audience, and other explanations need different supporting records.
Alex | The event counts have been verified for this comparison. That removes one data-quality concern, but it does not make the business explanation automatic.
Imani | Correct. Verified [[instrumentation::Instrumentation produces the event records; verifying those counts does not establish the causal explanation for their movement.]] supports trust in the observation. It does not show which uncontrolled difference between the periods caused the outcome.
Alex | The next analysis can compare relevant channels and user groups while keeping the seven-day definition fixed. We should not change the metric halfway through to recover a favorable result.
Imani | Use [[segmentation::Segmentation separates relevant groups for analysis while preserving the defined outcome and comparison basis.]] with a clear purpose and consistent definitions. It can reveal where the problem is concentrated without pretending that every descriptive split proves causality.
Alex | I will revise the update to say acquisition improved but the downstream completion outcome worsened. The campaign's overall contribution remains a question for analysis, not a settled success claim.
Imani | That qualifies [[attribution::Attribution assigns credit under a stated method; the uncontrolled cohort comparison does not isolate the campaign's causal contribution.]] appropriately. The team can acknowledge the signup gain and address the completion decline using the same honest account of the evidence.''',
    transfer_title='A bigger entrance, a smaller outcome',
    transfer_setup='Two mature seven-day cohorts use the same definition. The first has 200 signups and 100 setup completions. The second has 400 signups and 80 completions. The cause is not established.',
    transfer='''Analyst: "The earlier completion rate was ___ percent." | 50 | One hundred completions divided by two hundred signups equals fifty percent.
Growth: "The later rate was ___ percent." | 20 | Eighty completions divided by four hundred signups equals twenty percent.
Analyst: "The rate declined by ___ percentage points." | 30 | Fifty percent minus twenty percent equals thirty percentage points.
Growth: "The cause remains ___." | unestablished | The briefing supplies descriptive cohort results but no established causal explanation.'''))


BOOK['units'].append(unit(
    title='Experimentation and A/B Testing',
    rehearsal=['Read turns 1-10. Contrast observed lead with final winner.', 'Switch roles for turns 11-20. Stress that guardrail monitoring continues.', 'Check the transfer. Read 8%, 10%, and 25% with the correct comparison each time.'],
    scene='A day-one lead is not a final winner',
    skill='Discuss interim experiment results without changing the decision rule after seeing favorable data, while preserving guardrail monitoring.',
    brief='Product manager Jules and experimentation analyst Priya review day one of a randomized test. Control A has 100 conversions from 1,000 eligible users; variant B has 120 from 1,000. The pre-agreed fixed-horizon plan requires 14 days and at least 10,000 eligible users per arm before the final analysis. No sequential early-success rule is approved. The safety guardrail pauses an arm if its defined error rate exceeds 3%; current B errors are 1.2%. Data-quality checks are clear so far. Jules wants to announce B as the winner.',
    cast='Jules | Product manager\nPriya | Experimentation analyst',
    culture=('Do not rewrite the finish line after seeing the score', 'Interim data can support monitoring and investigation without establishing a final decision. State the planned analysis method and the difference between an early-success claim and a guardrail response. Waiting for planned evidence must never be confused with ignoring harm or a data-quality failure.'),
    a='''What are the observed conversion rates? | A is 10% and B is 12%. | A is 100% and B is 120%. | A is 1% and B is 1.2%. | Both are 20%. | One hundred and one hundred twenty conversions divided by one thousand users give ten and twelve percent.
Which final-analysis prerequisites remain unmet? | Fourteen days and at least 10,000 users per arm | A day-one screenshot only | A shared denominator of 1,000 | The current absence of a guardrail breach | The case is on day one with one thousand users per arm, below both planned prerequisites.
Does B currently exceed the specified error guardrail? | No; 1.2% is below 3%. | Yes; any nonzero error rate triggers this rule. | Yes; conversion is above 10%. | The guardrail applies only after fourteen days. | The current error rate is below the stated threshold, which still remains active during the test.''',
    vocabulary='''A/B test | A randomized comparison between defined alternatives. | run an A/B test
control arm | The experiment group receiving the reference experience. | define the control arm
treatment arm | The group receiving the changed experience. | monitor the treatment arm
random assignment | Allocation to groups by a defined random process. | verify random assignment
unit of randomization | The entity assigned to an experiment group, such as a user. | define the unit of randomization
eligibility rule | A condition determining which entities enter the test or analysis. | apply eligibility rules
exposure event | The recorded event indicating encounter with the tested experience. | validate the exposure event
primary metric | The main preselected measure for the experiment decision. | specify the primary metric
guardrail | A predefined boundary protecting against unacceptable effects. | monitor the guardrail
fixed-horizon test | A test analyzed under a preplanned endpoint rather than opportunistic stopping. | follow the fixed-horizon plan
sequential testing | A statistical approach designed for valid repeated decision opportunities. | use an approved sequential method
stopping rule | A predefined condition for ending or pausing an experiment. | follow the stopping rule
minimum sample | The smallest planned analysis population on the stated basis. | reach the minimum sample
minimum detectable effect | The effect size a planned test is designed to detect at stated power. | specify the minimum detectable effect
statistical power | The probability of detecting a specified effect under the test assumptions. | assess statistical power
confidence interval | An interval produced by a method with stated coverage properties. | report a confidence interval
p-value | A probability under the null model of results at least as extreme as observed. | interpret the p-value carefully
false positive | An erroneous rejection of a true null hypothesis under the stated test. | control false-positive risk
multiple testing | Conducting more than one statistical comparison or decision opportunity. | account for multiple testing
sample ratio mismatch | A difference from expected group allocation large enough to flag a validity concern. | investigate sample ratio mismatch
novelty effect | A temporary response associated with encountering something new. | assess novelty effects
day-of-week effect | Variation associated with the weekday composition of observations. | examine day-of-week effects
interim result | A result observed before the planned final decision point. | qualify interim results
practical significance | The operational importance of an effect, separate from statistical evidence. | assess practical significance''',
    precision='The observed difference is 2 percentage points, or a 20% relative increase from the 10% control rate. These are descriptive day-one figures. No final significance conclusion is supplied, and the pre-agreed time and sample requirements are not met.',
    precision_extra='A fixed-horizon success decision differs from an active guardrail response. The supplied guardrail is not breached at 1.2%, but it must still be monitored. Valid sequential methods can support different rules; none is approved for early success in this case.',
    phrases='''Give the counts | A has 100 conversions and B has 120, each from 1,000 users.
State the rates | The observed rates are 10% and 12%.
Separate effect expressions | The difference is two percentage points, or 20% relative.
Qualify maturity | This is a day-one result.
Recall the plan | Final analysis requires fourteen days and the planned sample.
Keep both prerequisites | The minimum is 10,000 eligible users per arm.
Reject a premature headline | B is ahead in the observed data, not yet a final winner.
Avoid opportunistic stopping | We have no approved early-success rule.
Preserve monitoring | Continue checking guardrails and data quality throughout.
Apply the actual threshold | The current 1.2% error rate is below the 3% guardrail.
Distinguish decisions | A harm-based pause is different from declaring success.
Ask about validity | Have allocation and event checks identified a problem?
Avoid invented certainty | The counts alone do not supply a final significance conclusion.
Consider representativeness | One day may not reflect the planned weekday mix.
State the next readout | Report the interim figures with the remaining evidence requirements.
Close the decision | Keep the final rollout decision pending the agreed analysis.''',
    notes='''Winner | A decision label that needs the planned evidence and rule.
Lift | Specify absolute percentage points or relative percent.
Peeking | Repeated inspection becomes a statistical issue when it changes decision behavior without an appropriate method.
Guardrail | Remains active during the test, not only at its endpoint.
Significant | Distinguish statistical evidence from practical importance.
Minimum | A requirement to meet, not a target to quietly lower after favorable data.''',
    d='''Which update is justified? | B leads descriptively on day one; the planned final-analysis requirements are unmet. | B is the final winner because 120 exceeds 100. | The 20% relative difference proves every user segment benefits. | The experiment can ignore all guardrails until day fourteen. | The update preserves the observed lead without converting interim counts into a final decision.
What is the relative increase from 10% to 12%? | 20% | 2% | 12% | 120% | The two-point increase divided by the ten-percent control rate equals twenty percent.
What should happen if the defined guardrail is later exceeded? | Follow the pre-agreed pause and investigation rule. | Keep running regardless because the horizon is fixed. | Declare B the winner to avoid recording the problem. | Remove the error metric after seeing it worsen. | The guardrail protects against unacceptable effects throughout the test and is distinct from the success analysis.
Why not stop for success simply because B leads today? | The fixed-horizon plan has no approved early-success method. | A randomized test can never have interim monitoring. | Every day-one difference is necessarily false. | Fourteen days guarantees statistical significance for every sample. | The correct decision follows the approved method; interim monitoring does not authorize opportunistic success stopping.''',
    dialogue='''Jules | B has one hundred twenty conversions and A has one hundred, with one thousand eligible users in each group. Can we announce a winner before the weekly product review?
Priya | Call it an [[interim result::An interim result is observed before the planned endpoint; these day-one counts do not establish the final experiment decision.]]. B is ahead in the day-one data, but the final-analysis requirements in our plan have not been met.
Jules | The observed rates are twelve percent and ten percent. I can describe that as a two-percentage-point difference, or twenty percent relative to the control rate.
Priya | Correct, and keep the [[control arm::The control arm is A, whose ten-percent rate provides the reference for the stated relative increase.]] clear. Those expressions describe the observed difference; neither one supplies a final significance conclusion or a guarantee of rollout benefit.
Jules | The plan calls for fourteen days and at least ten thousand eligible users per arm. We are short of both requirements after the first day.
Priya | This is a [[fixed-horizon test::A fixed-horizon test follows its preplanned endpoint and analysis rules rather than stopping whenever an interim result looks favorable.]]. We should not redefine its success decision because today's numbers look attractive, especially when no alternative early-success method has been approved.
Jules | What if B is still ahead tomorrow and we call it then? I want to avoid waiting unnecessarily, but would that change the analysis?
Priya | That changes the [[stopping rule::The stopping rule determines when a decision is permitted; changing it after repeated favorable looks can invalidate the planned inference.]]. Repeated opportunities to declare success need an appropriate statistical method, not an improvised rule added after seeing the data.
Jules | I understand that success stopping needs discipline. But we should still watch for a poor experience while the test runs, rather than wait until the final day.
Priya | Absolutely. The [[guardrail::The guardrail protects against unacceptable effects during the experiment and remains active before the final success analysis.]] stays active. Our defined error rule pauses an arm above three percent; B is currently at one point two percent, so it has not breached that threshold.
Jules | If that error rate later crosses the threshold, we follow the pause and investigation process. The fixed horizon does not require us to ignore that change.
Priya | Correct. [[Sequential testing::Sequential testing is a method designed for valid repeated decisions; none is approved here for declaring early success.]] could support different success rules if properly planned, but it is not the method approved here. Guardrail monitoring is still part of this plan.
Jules | Who is watching assignment and event quality while it runs? I do not want us discussing a conversion gain that turns out to be a logging problem.
Priya | Yes. Investigate a [[sample ratio mismatch::A sample ratio mismatch can indicate a problem in allocation or data capture, so it must be assessed rather than ignored for a favorable outcome.]] if one is flagged, alongside the relevant event checks. The current checks are clear so far, which is a status rather than a permanent guarantee.
Jules | One day also gives us only a narrow time slice. Different weekday behavior or a temporary reaction to the new experience could affect what we see.
Priya | A [[novelty effect::A novelty effect is a temporary response to the new experience and is one possible reason early behavior may not persist.]] is one possible concern. Do not claim it explains this result, but do not assume the first day's response represents the full planned period either.
Jules | At the final readout, we will still need to understand whether the effect matters enough to justify rollout, not only whether the analysis meets its statistical decision rule.
Priya | Assess [[practical significance::Practical significance concerns whether the effect matters operationally and is distinct from the statistical evidence for a difference.]] alongside the planned statistical evidence and guardrails. A decision needs the relevant magnitude, uncertainty, and consequences rather than a single attractive percentage.
Jules | My update will give the counts and observed lead, note the remaining time and sample requirements, and keep the rollout decision pending while monitoring continues.
Priya | That respects the [[minimum sample::The minimum sample is ten thousand eligible users per arm, an unmet prerequisite that cannot be silently lowered after favorable results.]] and the approved method. We can communicate useful progress without turning the first readout into a conclusion the experiment has not yet earned.''',
    transfer_title='The arithmetic is not the decision rule',
    transfer_setup='On day two of a fixed-horizon test, A converts 40 of 500 users and B converts 50 of 500. The final time and sample requirements are unmet, and no early-success rule is approved.',
    transfer='''Analyst: "A converts ___ percent." | 8 | Forty conversions divided by five hundred users equals eight percent.
Product: "B converts ___ percent." | 10 | Fifty conversions divided by five hundred users equals ten percent.
Analyst: "The relative increase is ___ percent." | 25 | The two-point increase divided by the eight-percent control rate equals twenty-five percent.
Product: "The final winner remains ___." | undecided | The approved final-analysis prerequisites are unmet and no early-success method is approved.'''))

BOOK['units'].append(unit(
    title='Release Readiness and Go-to-Market',
    rehearsal=['Read turns 1-10. Contrast sent with confirmed usable.', 'Switch roles for turns 11-20. Stress review, approval, and announcement as separate events.', 'Check the transfer. Read the four handoff terms clearly without adding an approval.'],
    scene='The software is ready; the support handoff is not',
    skill='Coordinate a release review by naming the missing operational prerequisite, its owner, and the distinction between review and launch approval.',
    brief='Release manager Ana and product marketer Rob prepare a Friday 10 a.m. launch review for a workspace-permissions update. Engineering checks are complete and the rollback rehearsal passed. The local launch checklist also requires migration notes delivered to Support and confirmed usable by its lead. Those notes have not been delivered. Ana can assign delivery for Thursday 3 p.m. and request Support review, but no waiver or launch approval exists. Rob wants to send the customer announcement now.',
    cast='Ana | Release manager\nRob | Product marketer',
    culture=('Treat the handoff as part of readiness', 'Customer-facing teams need the information required to handle the change, not merely proof that engineering finished coding. Name what is missing and how it will be checked. A planned review can stay on the calendar while the launch decision remains conditional.'),
    a='''Which readiness item is missing? | Migration notes delivered to Support and confirmed usable | Engineering checks | A successful rollback rehearsal | A scheduled Friday review | The checklist requirement for Support's migration notes has not been met.
What does Friday 10 a.m. represent? | The planned launch review | An already approved launch | A guaranteed completed migration for all customers | A waiver deadline that automatically removes the checklist item | The briefing identifies a review meeting, not a recorded authorization to launch.
What can Ana do now? | Assign note delivery and request Support review. | Declare a waiver without authority. | Treat an undelivered document as accepted. | Announce approval that does not exist. | Ana can coordinate completion of the missing requirement but cannot invent its fulfillment or launch approval.''',
    vocabulary='''release readiness | The state of meeting requirements for a defined release decision. | assess release readiness
go-to-market | Coordinated work to bring a product or change to its intended audience. | align the go-to-market plan
launch checklist | The required items reviewed before a launch decision. | complete the launch checklist
migration notes | Guidance explaining how users or teams move to a changed version or behavior. | deliver migration notes
release notes | A summary of changes in a defined release. | publish release notes
support enablement | Preparing support staff to assist users of the change. | complete support enablement
known issue | A documented problem with a stated status and impact. | disclose known issues
workaround | A defined alternative route around a known limitation. | document the workaround
rollback | Returning to a prior state under a defined recovery procedure. | rehearse rollback
rollout | Making a change available to a defined population. | stage the rollout
feature flag | A control enabling or disabling a capability for defined conditions or users. | configure a feature flag
go/no-go decision | A formal decision about whether a planned release proceeds. | record the go/no-go decision
launch gate | A required condition before proceeding to a launch stage. | satisfy the launch gate
operational readiness | Preparedness of the people and processes supporting live operation. | verify operational readiness
runbook | Documented instructions for a defined operational process. | update the runbook
escalation path | The route for obtaining higher-level help or authority. | confirm the escalation path
customer announcement | Communication informing customers about a change or availability. | approve the customer announcement
release owner | The role coordinating or accountable for the release under local rules. | identify the release owner
dependency owner | The person accountable for a required input. | name the dependency owner
readiness evidence | Records showing that a required release condition has been met. | attach readiness evidence
acceptance confirmation | A recipient's recorded acknowledgment that an input meets the agreed need. | obtain acceptance confirmation
contingency | A planned response if an expected condition is not met. | agree the contingency
launch hold | A restriction preventing the launch from proceeding. | communicate a launch hold
post-launch monitoring | Observation of defined product and operational signals after release. | plan post-launch monitoring''',
    precision='Engineering completion and a passed rollback rehearsal are positive readiness facts. They do not satisfy the separate Support requirement. The checklist calls for both delivery and confirmation that the notes are usable; a sent attachment alone would not necessarily close it.',
    precision_extra='Thursday 3 p.m. is a proposed delivery deadline for the missing input. Friday 10 a.m. is a review, not automatic approval. The customer announcement must not imply a launch decision before the responsible process has made one.',
    phrases='''Acknowledge completed work | Engineering checks are complete and rollback was rehearsed.
Name the open item | Support has not received the required migration notes.
Quote the actual gate | The notes must be delivered and confirmed usable.
Separate team readiness | Code readiness is not the whole launch checklist.
Assign the input | Name the owner for Thursday's note delivery.
Request recipient review | Ask the Support lead to confirm usability.
Avoid a false handoff | Sent does not automatically mean accepted.
Keep the review | Friday's go/no-go review can remain scheduled.
Qualify the launch | Launch approval is still pending.
Hold the announcement | Do not announce availability before the release decision.
Clarify the content | The notes need the changed permission behavior and support route.
Keep authority clear | No waiver has been approved.
Define the contingency | State what happens if the required confirmation is missing.
Preserve the evidence | Attach Support's confirmation to the readiness record.
Coordinate messages | Give Marketing and Support the same status.
Close the review request | Bring completed evidence and remaining blockers to the decision owner.''',
    notes='''Ready | Specify engineering, operational, commercial, or overall release readiness.
Delivered | A transmission event, not always evidence of recipient acceptance.
Usable | A recipient-facing condition, not a file-exists check.
Scheduled | A planned event, not a completed decision.
Announced | Creates customer expectations and should match actual approval.
Waived | Requires the appropriate authorized exception, not an informal assumption.''',
    d='''Which readiness statement is accurate? | Engineering is ready; the required Support handoff remains incomplete. | The whole launch is approved because rollback passed. | Support's missing notes are complete because someone intends to send them. | Friday's meeting automatically grants permission to announce. | The statement recognizes completed engineering work while preserving the separate open launch condition.
What evidence closes the stated Support item? | Delivery of the notes and the Support lead's usability confirmation | Only a promise that a document will exist | Only a draft stored where Support cannot access it | Only a passed code test unrelated to migration guidance | The checklist explicitly requires both delivery and confirmation that the recipient can use the notes.
Which announcement decision fits the facts? | Keep the customer availability announcement pending the release decision. | Announce approval immediately because the review is scheduled. | Describe the missing notes as waived without authorization. | Promise every customer a completed migration before review. | No launch approval or waiver exists, so the announcement must not represent either as settled.
What should happen if confirmation is still missing at the review? | Present the unresolved gate and follow the authorized go/no-go process. | Mark the gate complete to protect the calendar. | Assume silence from Support means acceptance. | Remove the requirement after the meeting begins. | An unmet requirement must remain visible to the decision process rather than be silently bypassed.''',
    dialogue='''Rob | Engineering says the workspace-permissions update is ready, and the rollback rehearsal passed. I would like to send the customer announcement before Friday's review so the campaign can start.
Ana | The [[launch checklist::The launch checklist includes the Support migration-note requirement as well as engineering and rollback checks.]] still has an open item. Support has not received the migration notes, and the local requirement also calls for its lead to confirm that they are usable.
Rob | I had treated the notes as a follow-up document rather than part of the release decision. The checklist makes that dependency explicit, so we need to close it.
Ana | Yes. [[Support enablement::Support enablement prepares the team to assist customers with the change and is a required part of readiness here.]] is part of this launch. The team needs to explain the changed permissions and route questions, not merely know that a new version exists.
Rob | Can we set Thursday at three as the delivery deadline and ask the Support lead to review the material before the Friday meeting?
Ana | We can assign a [[dependency owner::The dependency owner is responsible for producing the missing input, making the delivery request actionable.]] and that deadline. We should also confirm who performs the recipient review so delivery does not become an unowned handoff.
Rob | I will coordinate with the author and make sure Support can access the current document. A draft in a private folder would not meet the requirement.
Ana | Correct. The [[migration notes::Migration notes explain how to move to or handle the changed behavior, and must actually reach Support in usable form.]] need to reach the people using them. Their content should address the change and support route, not just repeat the marketing headline.
Rob | I can show that we sent a file. Are you saying I also need the Support lead to confirm that it answers the migration questions?
Ana | We need [[acceptance confirmation::Acceptance confirmation records that Support considers the delivered notes usable, not merely that an attachment was transmitted.]]. Sent and accepted are different states here, and the readiness record should preserve both rather than assume silence means the document is sufficient.
Rob | We can keep Friday's ten o'clock meeting scheduled while those actions proceed. But the invitation should not be read as proof that the launch has already been approved.
Ana | Exactly. It is a [[go/no-go decision::The go/no-go decision is the pending authorization point, distinct from scheduling the meeting or completing engineering work.]] review. The decision depends on the required evidence and any open items, not on the fact that everyone has accepted the calendar invitation.
Rob | I will prepare the announcement but keep it unsent. Please flag the release decision; I should not infer it from the meeting invitation.
Ana | Keep the [[customer announcement::The customer announcement must reflect actual availability and approval, so it should not get ahead of the pending release decision.]] aligned with the decision. We can prepare coordinated messages now without telling customers a pending change is already approved or available.
Rob | If the notes arrive late or Support finds gaps, we need an explicit response. Otherwise people may assume the engineering result overrides the unfinished handoff.
Ana | Agree the [[contingency::The contingency states the response if the required delivery or confirmation is missing, preserving the authorized decision process.]] with the release owner. The unresolved gate must be presented honestly; no waiver is recorded, and we should not invent one to preserve a preferred date.
Rob | I will ask the Support lead to identify any missing explanation promptly. The author can then address it and bring the final confirmation to the review.
Ana | Attach that [[readiness evidence::Readiness evidence shows that the actual checklist condition has been met and can be reviewed by the decision owner.]] to the release record. It should show what was delivered and accepted, not merely that an action was assigned to someone.
Rob | Our status can now acknowledge the completed engineering checks while naming the remaining operational work. Marketing, Engineering, and Support will use the same wording.
Ana | That gives an accurate [[operational readiness::Operational readiness includes the people and processes needed to support the live change, not only the software's technical state.]] picture. We can keep preparing for the launch while leaving its approval with the responsible review and the evidence it requires.''',
    transfer_title='A sent file is only half the gate',
    transfer_setup='The checklist requires a migration guide delivered to Support and confirmed usable by its lead. Delivery is recorded, but confirmation is absent. The launch review is tomorrow; no approval is recorded.',
    transfer='''Release: "The guide reached Support, so we can record ___." | delivery | Delivery is the recorded transfer of the guide, not acceptance of its contents.
Support: "You still need my usability ___ before closing that item." | confirmation | The recipient must confirm usability; sending the document does not establish this.
Release: "We will take the open item to the launch ___ tomorrow." | review | Tomorrow is the scheduled review, not a recorded decision or completed handoff.
Marketing: "I will keep the availability announcement unsent until we have launch ___." | approval | Approval is still absent, so Marketing cannot announce an authorized launch yet.'''))


BOOK['units'].append(unit(
    title='Platform, APIs, and Technical Debt',
    rehearsal=['Read turns 1-10. Stress estimated timing and the compatibility requirement.', 'Switch roles for turns 11-20. Pause before ownership, rollback, and expiry conditions.', 'Check the transfer. Read two, eight, and twenty-one with the correct time basis.'],
    scene='A three-day adapter or a ten-day interface',
    skill='Explain a short-term delivery option and its maintenance consequences without hiding compatibility, ownership, or retirement requirements.',
    brief='Product manager Camille and engineering lead Dev assess a customer request due in five working days. A client-specific adapter is estimated at three days including tests and could support a single-client pilot. A shared API change is estimated at ten days including tests. The adapter duplicates an existing transformation and needs named ownership, monitoring, rollback, and an approved 30-day expiry or extension process. Existing clients must retain their current behavior. Neither option is approved, and no engineering capacity beyond the estimates is confirmed.',
    cast='Camille | Product manager\nDev | Engineering lead',
    culture=('Translate debt into an owned consequence', 'Technical debt is not a synonym for bad code or an automatic reason to reject a short-term option. Describe what is duplicated, what must be maintained, and how the temporary path ends. A product decision can then weigh timing and consequences without pretending the shortcut is free.'),
    a='''Which estimate fits inside the requested five-day window? | The three-day adapter estimate | The ten-day shared API estimate | Both estimates equally | Neither can be compared with five days | Three days is within five, while ten exceeds it; feasibility and authorization still require the stated conditions.
What does the adapter duplicate? | An existing transformation | The entire customer company | A completed approval record | A confirmed ten-day capacity allocation | The supplied concern is duplicated transformation logic, creating a maintenance responsibility.
Which constraint applies to existing clients? | Their current behavior must be preserved. | They must all join the pilot automatically. | They can be broken without notice because the request is urgent. | Their behavior is irrelevant to the shared interface. | The briefing explicitly requires existing clients to retain their current behavior.''',
    vocabulary='''platform capability | A shared function supporting multiple products or consumers. | invest in platform capability
API | Application programming interface, a defined way for software components to interact. | define the API contract
API contract | The agreed inputs, outputs, and behavior of an interface. | preserve the API contract
endpoint | An addressable operation or resource in an interface. | document the endpoint
request schema | The defined structure and meaning of incoming data. | validate the request schema
response schema | The defined structure and meaning of returned data. | preserve the response schema
backward compatibility | Continued support for existing consumers under the stated contract. | maintain backward compatibility
breaking change | A change that can invalidate existing consumers' expectations. | identify a breaking change
versioning | Identifying and managing distinct interface or product versions. | plan API versioning
deprecation | Notice that a capability is discouraged and may be retired under a defined plan. | communicate deprecation
migration path | The supported route from an old interface or behavior to a new one. | provide a migration path
adapter | A component translating between interfaces or data forms. | scope the adapter
client-specific logic | Behavior implemented for a particular consumer. | isolate client-specific logic
duplicated logic | The same rule or transformation maintained in multiple places. | track duplicated logic
technical debt | Additional future work caused by expedient or inadequate design or implementation. | make technical debt explicit
maintenance burden | The effort and risk involved in keeping a solution working. | estimate the maintenance burden
ownership | Clear responsibility for a component or decision. | assign ownership
observability | The ability to understand a system through its exposed signals. | provide observability
rollback plan | The defined way to reverse a change if necessary. | test the rollback plan
expiry condition | A rule stating when a temporary option ends unless explicitly extended. | set the expiry condition
retirement plan | The agreed work and timing for removing an old or temporary path. | fund the retirement plan
extension decision | A recorded decision to continue beyond an original limit. | require an extension decision
blast radius | The scope of users or systems affected by a change or failure. | limit the blast radius
service-level objective | A defined target for a service measure, abbreviated SLO. | agree a service-level objective''',
    precision='The three-day estimate fits the five-day request numerically; it is not yet an approved commitment. Its scope is a single-client pilot. The ten-day shared API option exceeds the requested window, so the team must change scope, timing, or the decision rather than hide the difference.',
    precision_extra='A temporary adapter remains a maintained product path until removed. The 30-day limit needs a named owner and an approved expiry or extension process. Interface compatibility includes behavior and expectations, not just keeping an endpoint name unchanged.',
    phrases='''Set out the options | The adapter is estimated at three days; the shared API work at ten.
Qualify the estimate | Both estimates include tests but are not delivery approvals.
Name the short-term scope | The adapter would serve one client's pilot.
Expose the duplication | It repeats an existing transformation.
Translate the debt | Both copies would need to stay consistent until retirement.
Protect existing clients | Their current behavior must remain supported.
Ask about the contract | Would this change alter an existing response or behavior?
Limit exposure | Keep the pilot's blast radius explicit.
Assign maintenance | Who owns the adapter after the first delivery?
Require monitoring | Which signals show that the temporary path is working?
Plan reversal | The pilot needs a tested rollback plan.
Set the limit | The proposed adapter expires after thirty days unless explicitly extended.
Avoid silent permanence | A missed retirement date requires a decision, not an assumption.
Compare honestly | The durable option needs a longer delivery window.
Keep approval visible | Neither approach is approved yet.
Close the proposal | Present timing, scope, compatibility, ownership, and retirement together.''',
    notes='''Quick | Specify what is included and what future work remains.
Temporary | Needs an expiry or retirement decision to have practical meaning.
Debt | Describe its consequence instead of using it as a moral label.
Compatible | Includes behavior, not only unchanged field names.
Shared | A wider consumer base can increase both value and change impact.
Estimate | A planning input, not automatically a staffed commitment.''',
    d='''Which proposal accurately describes the adapter? | A three-day estimated single-client pilot with required ownership, monitoring, rollback, and expiry controls | A permanent shared interface already approved for every client | A cost-free change with no future maintenance | A ten-day implementation guaranteed within five days | The adapter's timing advantage comes with a narrow scope and explicit unresolved operating and retirement requirements.
Why does duplicated transformation logic matter? | Future changes may require both copies to stay consistent. | Duplication automatically proves every request is unsafe. | A temporary label removes maintenance work. | Existing clients no longer depend on their contract. | Maintaining the same transformation in two places creates a concrete consistency and ownership burden.
What is a compatibility question? | Will existing clients receive behavior they can still handle under the current contract? | Does the slide call the work a platform investment? | Can the deadline be renamed to hide the estimate? | Can all older users be assumed to migrate instantly? | Compatibility concerns consumers' actual expectations and supported behavior, not labels or assumed adoption.
What should happen at the 30-day limit? | Follow the approved expiry or explicit extension process. | Let the adapter continue forever without ownership. | Assume that temporary means no monitoring is needed. | Declare the shared API work complete without doing it. | The time limit requires a controlled decision or retirement, not silent continuation or an invented replacement.''',
    dialogue='''Camille | The customer needs a response within five working days. We have a three-day adapter estimate and ten days for shared API work, both including tests. What can we responsibly offer?
Dev | The [[adapter::The adapter is the narrow translation component estimated at three days, potentially serving a single-client pilot rather than the shared product.]] could fit the requested window as a single-client pilot. That is an option to assess, not an approved delivery commitment or a solution for every consumer.
Camille | I want to explain why the quicker path has a cost beyond those three days. The estimate says it repeats a transformation we already maintain elsewhere.
Dev | That creates [[duplicated logic::Duplicated logic means maintaining the same transformation in more than one place, creating future consistency work.]]. If the rule changes, both paths need to stay consistent until the adapter is removed. The customer-specific route cannot become invisible once the pilot starts.
Camille | Then technical debt should be described as that future consistency work and the responsibility to retire the temporary path, not simply as engineers disliking a quick solution.
Dev | Exactly. [[Maintenance burden::Maintenance burden is the ongoing effort and risk of keeping the temporary path correct, monitored, and consistent.]] makes the consequence concrete. We can choose a bounded shortcut deliberately, but we should not present it as having no ongoing owner or cost.
Camille | The shared option also needs to preserve existing clients. We cannot change what they receive merely because the new customer has a different need.
Dev | Review the [[API contract::The API contract includes the supported inputs, outputs, and behavior on which existing consumers depend.]]. Existing behavior must remain supported. Keeping the same endpoint name would not be enough if we changed the meaning of a field or response.
Camille | We should distinguish a new optional capability from a change that older clients cannot handle. That will help me explain the engineering review in product terms.
Dev | A [[breaking change::A breaking change can invalidate existing client expectations even when the visible endpoint or field names remain similar.]] can be behavioral, not just structural. We need to assess the actual consumers and contract rather than promise compatibility from a superficial comparison.
Camille | One client sounds contained, but can another client hit that path accidentally? I need to understand the boundary and how we will detect a problem.
Dev | Define the [[blast radius::Blast radius is the scope of affected consumers and systems, which the single-client pilot must explicitly bound.]] and the relevant monitoring. Narrow scope is useful only if the implementation and controls actually preserve that boundary.
Camille | Who will support it after delivery? I do not want the team to assume the first implementer will maintain it indefinitely without agreed capacity.
Dev | Assign [[ownership::Ownership names responsibility for operating and maintaining the adapter after its initial implementation.]] before approval. The proposal must identify who watches the signals, handles issues, and keeps the temporary transformation consistent with the existing one.
Camille | If we switch it off, what happens to that customer? Can we test the return path before offering the pilot, rather than work it out during an incident?
Dev | Include a tested [[rollback plan::The rollback plan defines how the pilot can be reversed if necessary, rather than assuming temporary code is automatically easy to remove.]]. The decision needs a practical recovery route, not just confidence that the change is small.
Camille | We proposed a thirty-day limit. At that point the adapter should expire or receive an explicit extension under an approved process, not remain by accident.
Dev | Make that [[expiry condition::The expiry condition makes the thirty-day limit actionable through retirement or an explicit authorized extension.]] part of the proposal. Temporary is only useful language if the end condition has an owner and a decision route.
Camille | I will present the options with the timing difference, the single-client limit, compatibility requirements, and ongoing work. Neither will be described as approved until the relevant review is complete.
Dev | Include the [[retirement plan::The retirement plan specifies how the temporary path will be removed or replaced, so its future work is visible in the choice.]] alongside the estimates. Then the team can decide whether the bounded pilot is worthwhile or whether the customer timeline should move for the shared solution.''',
    transfer_title='Temporary needs an ending',
    transfer_setup='A single-client adapter is estimated at two days; shared interface work needs eight. The requested window is four days. The adapter requires an owner and expires after 21 days unless explicitly extended. Neither option is approved.',
    transfer='''Product: "The adapter estimate is ___ days." | 2 | The supplied estimate for the narrow adapter is two days.
Engineering: "The shared option needs ___ days." | 8 | The broader interface work is estimated at eight days.
Product: "The adapter limit is ___ days unless extended." | 21 | The proposed expiry condition is twenty-one days with an explicit extension route.
Engineering: "Both options still need ___." | approval | The briefing states that neither proposal has been approved.'''))

BOOK['units'].append(unit(
    title='Stakeholder Pushback and Executive Narrative',
    rehearsal=['Read turns 1-10. Stress tickets rather than distinct customers.', 'Switch roles for turns 11-20. Keep pilot approval distinct from full rollout.', 'Check the transfer. Read the 25% ticket result and ten-day request without adding a retention claim.'],
    scene='Turn competing opinions into a decision request',
    skill='Present a concise recommendation tied to a shared objective while acknowledging evidence limits, displaced work, and decision authority.',
    brief='Product lead Iris prepares a decision with executive chair Malik. The agreed quarterly objective is to reduce support friction for existing paid teams. Option A is a two-week reliability pilot addressing an error category present in 40 of 100 reviewed support tickets. Those tickets are not 40 distinct customers, and no retention effect is established. Option B is a sales dashboard requested for uncommitted prospects. Capacity allows only one pilot. The agreed criterion favors documented existing-customer friction; the chair makes the decision. Iris recommends A, with B deferred and results reviewed after two weeks.',
    cast='Iris | Product lead\nMalik | Executive decision chair',
    culture=('Recommend clearly without overstating certainty', 'Executives need a decision-ready explanation, not a history of every meeting. Lead with the recommendation, connect it to the shared objective and evidence, state the trade-off, and identify the decision requested. Acknowledge the alternative fairly rather than caricaturing the executive who prefers it.'),
    a='''What is the shared quarterly objective? | Reduce support friction for existing paid teams | Maximize every possible feature count | Guarantee revenue from uncommitted prospects | Prove a retention gain already occurred | The briefing identifies support friction among existing paid teams as the agreed objective.
What does 40 of 100 mean? | Forty reviewed tickets belong to the relevant error category. | Forty distinct customers are proven to have churned. | Forty percent of all customers have the error. | A forty-percent retention improvement is established. | The count concerns reviewed tickets, not distinct customers, population prevalence, or retention effects.
Who makes the supplied decision? | Malik, the executive chair | Iris alone by sending a recommendation | Every prospect automatically | Whoever repeats a preference most often | The case explicitly assigns decision authority to the executive chair.''',
    vocabulary='''executive narrative | A concise explanation connecting evidence, trade-offs, and a decision. | shape the executive narrative
decision request | A specific choice or authorization sought from a decision maker. | state the decision request
shared objective | An agreed outcome used to align competing views. | confirm the shared objective
decision criterion | A defined basis for evaluating alternatives. | agree the decision criterion
recommendation | A proposed course of action supported by reasons. | lead with the recommendation
evidence strength | The degree of support the available information gives a claim. | qualify evidence strength
customer friction | Difficulty users encounter while trying to achieve a task. | reduce customer friction
paid team | A customer organization or group with a paid product relationship. | support existing paid teams
ticket category | A defined grouping of support records by issue type. | analyze the ticket category
distinct customer | A unique customer under the stated identity rule. | count distinct customers
retention effect | A change in continued use attributable to a specified intervention. | evaluate the retention effect
prospect | A potential customer who has not yet made the relevant commitment. | distinguish prospects from customers
uncommitted pipeline | Potential business without the stated binding or accepted commitment. | qualify uncommitted pipeline
pilot scope | The bounded population, work, and duration of a trial. | define the pilot scope
decision owner | The role authorized to make a specified choice. | identify the decision owner
displaced work | Work that does not proceed because another option uses capacity. | name the displaced work
counterargument | A reason offered against a proposed conclusion or action. | address the counterargument
steelman | Presenting the strongest reasonable version of another position. | steelman the alternative
assumption check | Review of a premise on which a proposal depends. | conduct an assumption check
reversibility | The extent to which a decision can be undone at acceptable cost. | assess reversibility
decision boundary | The scope of what a particular approval does and does not authorize. | state the decision boundary
success measure | A defined indicator used to evaluate the intended result. | agree a success measure
follow-up review | A scheduled evaluation of progress or results after a decision. | schedule the follow-up review
decision record | Documentation of the choice, basis, authority, and conditions. | preserve the decision record''',
    precision='Forty of 100 reviewed tickets is 40% of those tickets. It is not 40 distinct customers or 40% of the customer population. The case supplies no causal retention effect. A recommendation can be well supported by problem fit while its future impact remains uncertain.',
    precision_extra='The agreed criterion favors A over B for this one available pilot. That does not prove B has no value or authorize a full rollout. The chair must decide the bounded pilot; the two-week review evaluates results rather than guaranteeing success in advance.',
    phrases='''Lead with the action | I recommend the two-week reliability pilot.
Connect the objective | It directly addresses documented friction for existing paid teams.
State the evidence | The error category appears in 40 of 100 reviewed tickets.
Protect the unit | Those are tickets, not 40 distinct customers.
Limit the outcome claim | We have not established a retention effect.
Represent the alternative | The dashboard could support prospect conversations, but the pipeline is uncommitted.
Apply the shared rule | Our criterion favors documented existing-customer friction.
State the trade-off | Choosing A defers the sales-dashboard pilot.
Name the authority | I am asking the chair to approve this bounded pilot.
Define the boundary | This is not approval for a full rollout.
Invite a relevant challenge | Which assumption would change your view under the agreed objective?
Avoid personal framing | The disagreement concerns priorities, not the competence of either team.
Set the review | Review the pilot evidence after two weeks.
Keep the measure honest | Agree the success measure before interpreting results.
Record the decision | Capture the chosen scope, rationale, and owner.
Close the request | Approve or decline the pilot on the stated basis.''',
    notes='''Recommend | A clear proposal, not an announcement that approval already occurred.
Evidence | State its unit, source, and limits.
Customer | Do not substitute ticket counts for unique organizations.
Pipeline | Potential business is not automatically committed revenue.
Pilot | A bounded trial, not a hidden full rollout.
Review | A point to assess results, not a promise that results will be positive.''',
    d='''Which opening is most decision-ready? | I recommend the two-week reliability pilot because it matches our agreed objective and documented ticket evidence. | We have had many interesting meetings and everyone has opinions. | The dashboard sponsor clearly does not care about customers. | Forty tickets prove forty customers will stay forever. | The opening states the action, duration, objective fit, and evidence without personal attack or unsupported outcomes.
How should Iris describe the alternative? | It could support prospect conversations, but the supplied pipeline is uncommitted. | It has no possible value because it is not selected. | It is already guaranteed revenue. | Its sponsor's preference overrides every shared criterion automatically. | A fair comparison recognizes possible value while preserving the actual commitment status.
What does approval of the requested pilot authorize? | The defined two-week pilot within its agreed scope | An unlimited rollout to every customer | A proven retention improvement | Every deferred feature in addition to the pilot | The request is explicitly bounded to one pilot and does not authorize unrelated work or establish outcomes.
Which statement about the ticket evidence is accurate? | It identifies a documented issue category but does not establish distinct-customer count or retention impact. | It proves exactly forty separate organizations are affected. | It is a census of the entire paid population. | It proves the pilot already solved the problem. | The supplied unit is reviewed tickets, and the broader customer and causal claims are expressly unestablished.''',
    dialogue='''Malik | We keep debating reliability for customers and a dashboard for prospects. What decision are you asking us to make?
Iris | My [[recommendation::The recommendation is a specific proposed action, the two-week reliability pilot, rather than a claim that approval already exists.]] is to approve the two-week reliability pilot. It addresses the documented error category and fits the objective we agreed for existing paid teams.
Malik | State that objective explicitly. The executives have been using different ideas of success, which makes each option sound essential on its own terms.
Iris | The [[shared objective::The shared objective is reducing support friction for existing paid teams, providing the common basis for this decision.]] is to reduce support friction for current paid teams this quarter. Under that objective, the ticket evidence gives A a more direct basis than uncommitted prospect requests.
Malik | What exactly does the evidence show? I heard someone say forty customers are affected, but the briefing refers to forty tickets out of one hundred reviewed.
Iris | It is a [[ticket category::A ticket category groups support records; forty tickets in it do not establish forty distinct customers.]] count, not forty distinct customers. The category appears in forty of the hundred reviewed tickets, and we should preserve that unit when presenting the problem.
Malik | Does that also mean the reliability work will improve retention? That would be useful, but I do not want the recommendation to promise a result we have not measured.
Iris | No [[retention effect::A retention effect would require evidence about continued use and attribution, neither of which is established by the ticket count.]] is established. We are proposing to address documented friction, not claiming the ticket count proves a future reduction in customer loss.
Malik | Sales will challenge that. What is the strongest case for their dashboard? Tell me what we give up, not just what supports your recommendation.
Iris | It could support prospect conversations, but the supplied [[uncommitted pipeline::Uncommitted pipeline represents potential business without the relevant confirmed commitment, limiting the strength of the dashboard's current case.]] is not guaranteed business. That potential matters, yet it is less directly supported under the criterion chosen for this quarter.
Malik | Capacity permits one pilot. If I approve A, the dashboard pilot does not happen at the same time, and that consequence should be visible to the commercial team.
Iris | I will name the [[displaced work::Displaced work is the sales-dashboard pilot that cannot proceed alongside A under the one-pilot capacity limit.]]. B is deferred, not declared worthless. Any later reconsideration should use updated evidence and the available capacity rather than an implied promise that it is already next.
Malik | How broad is the approval you want? I do not want a small pilot decision interpreted as permission to roll out a change across the entire customer base.
Iris | The [[decision boundary::The decision boundary limits the requested authorization to the defined two-week pilot, not an unrestricted rollout.]] is the defined two-week pilot. We should record its scope and responsible owner, with any wider rollout requiring its own evidence and decision.
Malik | We also need to agree what we will examine afterward. Otherwise each team may select whichever number makes its original preference look right.
Iris | Agree the [[success measure::The success measure defines how the pilot will be evaluated before results are interpreted, avoiding a retrospective change of criteria.]] before interpreting the results. It should connect to the friction we are addressing, with the limits of the pilot evidence kept visible.
Malik | Put the result review in for two weeks. Bring the same measures whether the pilot succeeds or disappoints; we need an actual decision at that meeting.
Iris | The [[follow-up review::The follow-up review evaluates the pilot evidence after two weeks without guaranteeing a positive result in advance.]] will show what changed, what remains uncertain, and what decision follows. The review date does not promise a retention result or automatic expansion.
Malik | The request is clear: one bounded pilot, an explicit trade-off, and a defined review. I will decide on that basis and record any conditions.
Iris | I will preserve the [[decision record::The decision record captures the authorized choice, scope, rationale, and conditions so teams do not infer more than was decided.]] with your choice and conditions. That gives both teams the same account of the decision, including what was approved and what was deferred.''',
    transfer_title='Tickets are not customers',
    transfer_setup='A team reviews 80 tickets; 20 concern a specific error. Unique-customer counts and retention effects are unknown. The product lead recommends a ten-day pilot, with final approval assigned to the chair.',
    transfer='''Product: "The error appears in ___ percent of reviewed tickets." | 25 | Twenty tickets divided by eighty reviewed tickets equals twenty-five percent.
Chair: "The unit counted is ___." | tickets | The evidence counts support records, not distinct customers or retained accounts.
Product: "The proposed pilot lasts ___ days." | 10 | The briefing defines the recommended pilot duration as ten days.
Chair: "The recommendation still requires my ___." | approval | The product lead recommends the pilot, while final approval belongs to the chair.'''))
