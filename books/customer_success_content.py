"""Original Customer Success learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='customer-success',
    title='Customer Success English',
    cover_label='ENGLISH FOR CUSTOMER PARTNERSHIPS',
    cover_title='Customer\nSuccess',
    cover_size=38,
    tagline='Build adoption. Explain value. Keep trust.',
    audience='For customer success managers, onboarding specialists, implementation teams, account managers, and customer-facing leaders.',
    map_intro='Eight customer conversations: agree a workable launch, interpret adoption, communicate an incident, validate value, plan a renewal, assess expansion, clarify a feature request, and repair a disputed expectation.',
    notes_title='Useful progress. Credible promises.',
    notes_intro='Customer success conversations connect the product to the work a customer needs to accomplish. These cases practice the language of shared ownership, meaningful use, measured outcomes, and honest follow-through when expectations or evidence are incomplete.',
    field_notes=[
        ('Agree the outcome before the activity', 'A completed training session or a high login count can be useful without proving that the customer has achieved the intended result. Name the workflow and the evidence that would demonstrate progress.', '"Which completed task would show that the team can work independently?"'),
        ('Give numbers a clear basis', 'State the period, population, unit, and source. Keep observed results separate from assumptions, and keep time released separate from cash savings.', '"Thirty of eighty eligible users completed the workflow in the last thirty days."'),
        ('Own the communication you can control', 'Acknowledge the impact, give the verified status, and name the next update. Do not fill an uncomfortable silence with an unsupported fix date or feature promise.', '"I will update you at fourteen hundred UTC, even if the investigation is still open."'),
        ('Keep the partnership two-sided', 'Confirm customer and supplier responsibilities without assigning blame. Ask permission to involve additional stakeholders, and set calm boundaries when frustration becomes personal.', '"I want to resolve the issue with you; let us keep the discussion focused on the work."'),
    ],
    scope_note='All accounts, products, people, metrics, policies, dates, and incidents are fictional. This book teaches professional English, not technical, financial, legal, or security advice. Follow actual contracts, approved support guidance, data-handling rules, and authorized escalation procedures. Health-score definitions and renewal processes vary by organization.',
    sources=[
        dict(title='Gainsight. How Gainsight Redesigned the Customer Health Score for One of Its Products (2021).',
             url='https://www.gainsight.com/blog/how-gainsight-redesigned-the-customer-health-score-for-one-of-its-product/',
             note='Background on multidimensional account health. The book uses original fictional metrics, not a reproduction or endorsement of a proprietary scoring framework.', checked='1 October 2026'),
        dict(title='Pendo. The Path to Increasing Product Adoption.',
             url='https://www.pendo.io/resources/the-path-to-product-adoption/',
             note='Background on usage, adoption, and retention terminology. All populations, calculations, and customer outcomes in the exercises are invented.', checked='1 October 2026'),
        dict(title='Atlassian. Incident Communication Best Practices.',
             url='https://www.atlassian.com/incident-management/incident-communication',
             note='Background on communicating verified impact, status, and update timing. The incident and its approved workaround are fictional.', checked='1 October 2026'),
        dict(title='Atlassian. Agile Roadmaps: Build, Share, Use, and Evolve.',
             url='https://www.atlassian.com/agile/product-management/roadmaps',
             note='Background on communicating evolving product plans. Roadmap examples do not determine contractual obligations or promise real product availability.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Onboarding and Implementation Expectations',
    scene='Turn a hoped-for launch into a shared readiness plan',
    skill='Clarify owners, dependencies, and acceptance checks before confirming a customer launch date.',
    brief='Customer lead Omar expects a launch on Friday, 9 October. The export owner and training slot are still unassigned. Customer success manager Lena cannot confirm readiness. The agreed launch conditions are an approved customer export, a successful test import, user acceptance of the main workflow, and completed administrator training. The customer owns data preparation; the supplier owns import mapping and training delivery. No one has yet confirmed that the required people are available. A readiness review is scheduled for Thursday at 15:00 UTC.',
    cast='Omar | Customer implementation lead\nLena | Customer success manager',
    culture=('A shared plan needs explicit owners', 'Customers may interpret a friendly agreement with a target as a promise. State what is agreed, what is still unassigned, and which conditions govern launch. Confirm responsibility without making the customer feel that the supplier is transferring every difficulty to them.'),
    a='''What is the status of the Friday launch? | A target whose readiness conditions are not yet confirmed | A completed acceptance milestone | A confirmed date with all resources assigned | A date canceled by the customer | The target remains conditional because required tasks and people are not yet confirmed.
Who owns preparation of the customer data? | The customer | The supplier training team | Any end user who logs in | The account executive automatically | The brief assigns data preparation to the customer, separately from supplier import mapping.
When is the readiness review? | Thursday at 15:00 UTC | Friday after launch at 15:00 UTC | Thursday at 15:00 in an unspecified local zone | Whenever training happens to finish | The stated review has both a day and an explicit time zone.''',
    vocabulary='''onboarding | The process of preparing a customer to use a service effectively. | coordinate onboarding
implementation | Work to configure, connect, and introduce a solution. | plan the implementation
kickoff | The initial meeting aligning purpose, people, and approach. | run a kickoff
success plan | A shared record of outcomes, actions, ownership, and measures. | agree a success plan
target date | A desired date whose commitment status must be specified. | qualify the target date
go-live | The start of operational use under agreed conditions. | confirm go-live readiness
dependency | A task or condition on which another step relies. | identify dependencies
prerequisite | Something required before a particular activity can proceed. | verify prerequisites
data migration | Moving data between systems with appropriate checks. | coordinate data migration
source export | Data extracted from the originating system. | approve the source export
data mapping | Specifying how source fields correspond to destination fields. | validate data mapping
data owner | The role accountable for the relevant data and its use. | confirm the data owner
test import | A controlled trial of bringing data into the destination. | complete a test import
UAT | User acceptance testing; users checking the solution against agreed needs. | schedule UAT
acceptance criterion | A defined condition used to judge whether work is acceptable. | agree acceptance criteria
administrator | A user with specified management permissions in the service. | train administrators
training slot | A scheduled period with the required trainer and participants. | confirm the training slot
readiness review | A check of whether the conditions for the next stage are met. | hold a readiness review
cutover | The coordinated transition into a new operational arrangement. | plan the cutover
rollback plan | An approved approach for reversing a change if required. | review the rollback plan
hypercare | A defined period of enhanced support after introduction. | define hypercare coverage
handover | Transfer of responsibility with the necessary information. | complete the handover
RACI | Responsible, accountable, consulted, and informed; a role-assignment framework. | clarify the RACI
open dependency | A required preceding task or condition not yet satisfied. | track open dependencies''',
    precision='A target date is not evidence of readiness. The four stated conditions are export approval, a successful test import, workflow acceptance, and administrator training. The Thursday review checks those conditions; holding the meeting alone does not satisfy them.',
    precision_extra='Data preparation and import mapping have different owners. The customer must approve appropriate source data, while the supplier maps the agreed fields. Secure transfer arrangements, access, and any rollback procedures must follow the actual implementation plan.',
    phrases='''Confirm the objective | Which workflow must the team be able to complete on launch day?
Qualify the date | Friday is the target, but readiness is not yet confirmed.
Name a dependency | The test import depends on an approved customer export.
Separate responsibilities | Your team prepares the data; our team maps the agreed fields.
Ask for an owner | Who can own the export and confirm its availability?
Check capacity | Has that person accepted the task and the timing?
Define acceptance | We need users to complete the agreed workflow successfully.
Clarify attendance | Who will attend the administrator training?
Avoid assuming completion | A calendar invitation does not mean the training has happened.
Set a review | Let us review readiness on Thursday at fifteen hundred UTC.
State a conditional sequence | Once the approved export is available, we can assess the import schedule.
Protect the data | Use the agreed secure transfer route and only the required fields.
Check support | What support coverage is agreed for the initial operating period?
Keep gaps visible | The export owner and training slot are still open.
Agree a decision rule | Confirm launch only after the agreed conditions are met.
Close with ownership | I will update the plan with each owner, dependency, and confirmed date.''',
    notes='''Target | Describes the desired date without silently guaranteeing it.
Depends on | Names the preceding condition rather than blaming another team.
Has accepted | Checks actual ownership, not merely a name on a chart.
Once | Makes the sequence conditional on a completed prerequisite.
Still open | Identifies unresolved work without declaring the entire project a failure.
Only after | Makes the readiness condition explicit.''',
    d='''Which launch statement is accurate? | Friday remains a target pending the four agreed readiness conditions. | Friday is confirmed because both teams want it. | The readiness meeting replaces the test import. | Administrator attendance is unnecessary once invitations are sent. | A desired date cannot substitute for the stated acceptance and preparation conditions.
Which ownership statement matches the brief? | Customer preparation and supplier mapping are separate responsibilities. | The supplier owns all customer source-data decisions. | Every end user is automatically the migration owner. | The trainer must approve the export simply because training is required. | The allocation distinguishes source-data preparation from the supplier's mapping work.
What does a training invitation establish? | A proposed or scheduled event, not completed training | Successful administrator practice | User acceptance of the main workflow | Approval of every imported record | An invitation concerns scheduling and does not prove attendance, learning, or acceptance.
What belongs in the Thursday decision? | The actual status of each launch condition and any unresolved dependency | Only the number of meetings already held | A launch confirmation regardless of missing evidence | A new date invented without checking availability | The decision must use readiness evidence and confirmed dependencies rather than activity counts or unsupported dates.''',
    dialogue='''Omar | Our team is expecting to start using the system next Friday. Can you confirm that date so I can send the announcement?
Lena | Friday is still our [[target date::Target date identifies the intended timing, while the required launch conditions remain unverified.]], but I cannot confirm readiness yet. The export owner and administrator training slot are open. I would like us to settle those responsibilities before you announce a firm launch.
Omar | I thought the supplier handled the migration. Are you saying my team needs to do the technical work as well?
Lena | Let us separate [[data preparation::The customer prepares and approves source data; the supplier separately handles the agreed import mapping.]] from our import work. Your team approves the source export. We map the agreed fields and run the import checks. You do not need to guess how our system processes them.
Omar | That distinction helps. I can coordinate the export, but I need our data lead to confirm when an approved file will be available.
Lena | Please name that person as the [[data owner::Naming a data owner identifies accountability, but availability and approval still require confirmation.]] in the plan and check their availability. We also need the agreed secure transfer route; please do not send the full customer database in an ordinary email.
Omar | Once the file is available, could the team start working immediately, or is there another check first?
Lena | We need a successful [[test import::The test import checks the migration before operational use; receiving a file does not establish success.]] before operational use. Then your users need to verify the main workflow against the agreed criteria. A file arriving is progress, but it does not complete those checks.
Omar | I can arrange for two team leads to check the workflow. I will confirm their availability rather than simply put their names in the plan.
Lena | Good. Their [[user acceptance::User acceptance checks the agreed workflow against customer needs, separately from technical import completion.]] needs a clear basis: the agreed task, expected result, and any exceptions. We should know what successful completion means before deciding whether the system is ready.
Omar | The training invitation is not out yet. Our administrator works across two sites, so I need to check which session they can attend.
Lena | I will coordinate the [[training slot::A training slot needs confirmed trainer and participant availability; an invitation alone does not complete training.]] with you. Sending an invitation is not the same as completing administrator training, which is one of our launch conditions.
Omar | I still need to tell the wider team something today. I do not want silence to create a different set of expectations.
Lena | Tell them Friday remains the target, with confirmation following the [[readiness review::The Thursday review assesses the four conditions; scheduling the review does not satisfy them.]] on Thursday at fifteen hundred UTC. That gives them a real decision point without implying that unresolved work is already finished.
Omar | What if the export is late but training is complete? Would we still describe the project as ready?
Lena | No. The export would remain an [[open dependency::An unresolved export still blocks the dependent checks even if administrator training is complete.]]. We must assess the effect on testing and acceptance rather than count one completed task as a substitute for another.
Omar | Please also make clear who supports the team after launch. They should not have to guess which contact to use.
Lena | We will confirm the [[handover::The handover transfers support responsibility and contact details, rather than assuming the project team remains available indefinitely.]] and initial support arrangements. Coverage and contacts need to be explicit, with any enhanced support period defined rather than assumed to continue indefinitely.
Omar | I will confirm the data lead and user testers, check their availability, and send a conditional update to the team.
Lena | I will update the [[success plan::The success plan brings outcomes, owners, dependencies, and evidence together for the readiness decision.]] with the owners, dependencies, and actual status. At Thursday's review, we will decide from the evidence against all four conditions, not from the date alone.''',
    transfer_title='Confirm the conditions for another launch',
    transfer_setup='A Monday launch remains a target. Customer lead Farah owns source-data approval. Supplier lead Ben owns import mapping. Training is complete, but the test import has failed. The readiness review is Friday at 10:00 UTC.',
    transfer='''Customer: "Monday is still a ___." | target | The launch is not confirmed because a required import check has failed.
Supplier: "Source-data approval belongs to ___." | Farah | The brief assigns source-data approval to Farah, not the supplier mapping lead.
Customer: "The incomplete technical condition is the ___." | test import | Training is complete, but the test import has not succeeded.
Supplier: "The readiness review is Friday at ___." | 10:00 UTC | The supplied time and zone identify the scheduled review, not automatic launch approval.''',
))


BOOK['units'].append(unit(
    title='Adoption Metrics and Health Scores',
    scene='The green score hides a workflow gap',
    skill='Explain usage measures with the right population and distinguish access from meaningful adoption.',
    brief='Account C14 has 120 licensed users. In the last 30 days, 100 distinct users logged in. Of the 80 users whose roles require the approval workflow, only 30 completed it at least once. The dashboard health score is green because its current rule emphasizes logins. Customer lead Mei reports that some staff still use email approvals. Customer success manager Daniel must explain the different denominators and investigate the workflow gap without assuming every inactive license is wasted or that the account will certainly cancel.',
    cast='Mei | Customer operations lead\nDaniel | Customer success manager',
    culture=('Challenge the measure without dismissing the team', 'A green dashboard can feel reassuring to one team and disconnected from daily work to another. Acknowledge what the measure genuinely shows, then examine the missing outcome. Ask about role, frequency, access, and obstacles before calling users resistant.'),
    a='''How many licensed users logged in during the period? | 100 of 120 | 30 of 120 | 80 of 100 | 30 of 30 | The brief reports one hundred distinct logins among one hundred twenty licensed users.
Which population is relevant to workflow completion here? | The 80 users whose roles require that workflow | All visitors to the supplier website | Only the 30 people who completed it | The number of email messages sent | The stated eligible group is eighty users, including those who did not complete the workflow.
Why is the dashboard green? | Its current rule emphasizes logins. | Every eligible user completed the workflow. | The customer confirmed all intended outcomes. | Renewal has already been signed. | The score reflects its configured rule, not proof of workflow adoption or renewal.''',
    vocabulary='''adoption | Use of a product or workflow in the intended working context. | assess adoption
licensed user | A person covered by the relevant access entitlement. | count licensed users
active user | A user meeting a defined activity condition within a stated period. | define active users
unique user | A distinct person or identity counted once under the measurement rule. | count unique users
eligible population | The people for whom a particular measure is relevant. | define the eligible population
denominator | The base quantity used in a fraction or rate. | state the denominator
login rate | The share of a defined population that logged in during a period. | calculate the login rate
workflow completion | Finishing the defined sequence of work. | measure workflow completion
breadth of adoption | How widely relevant use extends across users, teams, or functions. | assess adoption breadth
depth of adoption | How extensively intended capabilities are used. | assess adoption depth
frequency | How often a defined action occurs within a period. | measure usage frequency
cohort | A defined group followed or compared on a shared basis. | compare user cohorts
health score | A configured indicator combining selected account signals. | interpret the health score
weighting | The relative influence assigned to a component in a calculation. | review score weighting
leading indicator | A measure used as a possible signal of a later result. | test leading indicators
lagging indicator | A measure of an outcome that has already occurred. | distinguish lagging indicators
engagement | Participation or interaction under a stated definition. | assess stakeholder engagement
sentiment | Expressed attitudes or feelings about the relationship or service. | record customer sentiment
usage telemetry | Recorded data about product interactions. | validate usage telemetry
instrumentation | The setup used to capture events and measurements. | check instrumentation
event definition | The rule specifying what a recorded action represents. | verify event definitions
usage gap | A difference between intended and observed use. | investigate the usage gap
adoption barrier | A condition making intended use difficult or impractical. | identify adoption barriers
vanity metric | A flattering measure with weak relevance to the decision at hand. | question a vanity metric''',
    precision='Login activity is 100 divided by 120, approximately 83.3%. Relevant workflow completion is 30 divided by 80, or 37.5%. Thirty divided by 120 is 25%, but that answers a different question about all licensed users.',
    precision_extra='A user who completed the workflow once has met this period metric, not necessarily established a habit. A green health score is a configured signal. Its accuracy and usefulness depend on definitions, data quality, and relevance to the intended customer outcomes.',
    phrases='''Acknowledge the signal | The login count shows broad access during this period.
Name the gap | It does not show that the approval workflow is being used.
Specify the period | These figures cover the last thirty days.
Specify the population | Eighty users have roles that require this workflow.
State the rate | Thirty of eighty eligible users completed it, which is thirty-seven point five percent.
Distinguish another rate | Thirty out of all one hundred twenty licenses would answer a different question.
Check the event | What exactly triggers a workflow-completed event?
Avoid double counting | Count distinct users, not every repeated login.
Ask about the obstacle | Where do people switch back to email?
Keep the cause open | Low completion does not tell us the reason by itself.
Check role fit | Some licensed users may not need this workflow.
Challenge the score carefully | Green reflects the current scoring rule, not every aspect of account health.
Test relevance | Does this measure connect to the outcome you bought the product for?
Agree a targeted intervention | Let us address the confirmed obstacle before scheduling generic retraining.
Measure again | Use the same population and period definition for the follow-up.
Close with evidence | Record the gap, the confirmed barrier, and the next measurement date.''',
    notes='''Shows | Restricts the claim to what the measure actually establishes.
Does not show | Separates an access event from a completed customer task.
Of eighty | Makes the relevant denominator audible.
By itself | Leaves the cause open pending investigation.
Current rule | Explains a dashboard label without presenting it as an objective verdict.
Same definition | Makes later comparisons more meaningful.''',
    d='''Which statement correctly describes workflow use? | Thirty of eighty eligible users completed it at least once in thirty days. | Eighty-three percent completed it because they logged in. | Every license without a completed approval is unused. | Thirty completions prove a stable daily habit. | The measure counts distinct eligible completers within the stated period, not login activity or habit.
What is the workflow completion percentage? | 37.5% | 25% | 83.3% | 62.5% | Thirty divided by eighty is 0.375, whereas the other bases or complement answer different questions.
What should happen before blaming resistance? | Verify event definitions and ask where the workflow breaks down. | Replace the score with a guaranteed cancellation prediction. | Count every login as a completed approval. | Remove users whose roles do not require approval. | Measurement checks and customer workflow evidence help distinguish technical, role, and process barriers from assumptions.
Which follow-up comparison is sound? | Compare the same defined eligible group and period, noting any population changes. | Compare this month's unique users with next month's raw event count. | Change the denominator silently to make the rate rise. | Treat one extra login as proof of realized business value. | Consistent definitions and explicit population changes are necessary to interpret movement in the rate.''',
    dialogue='''Mei | Your dashboard says our account is healthy, but my supervisors still chase approvals by email. Those two descriptions do not feel consistent.
Daniel | The green [[health score::The health score reflects a configured rule emphasizing logins, not verified achievement of every customer outcome.]] mainly reflects logins at the moment. It tells us something about access, but it does not establish that the approval workflow is replacing email.
Mei | One hundred people logged in. That sounds encouraging, but I do not know how it relates to the work we actually need.
Daniel | It is one hundred distinct users out of one hundred twenty licenses in thirty days. The [[login rate::The login rate uses one hundred distinct users over one hundred twenty licensed users, approximately 83.3%.]] is about eighty-three point three percent. Repeated visits by the same person do not increase that user count.
Mei | Only eighty people have roles that require approvals. The other forty use different parts of the product.
Daniel | Then eighty is the relevant [[denominator::Eighty is the eligible workflow population; using all licenses would answer a different adoption question.]] for this workflow measure. Thirty of those eighty completed it at least once, which is thirty-seven point five percent.
Mei | Someone presented thirty out of one hundred twenty in our internal meeting. Was the arithmetic wrong?
Daniel | The arithmetic gives twenty-five percent, but the [[eligible population::The eligible population contains the users whose roles require this workflow, rather than every licensed person.]] was different. That figure describes completers as a share of all licenses, not completion among the people expected to use approvals.
Mei | Before we act on thirty, I want to know what the system calls a completed approval. Could starting a request count?
Daniel | We should verify the [[event definition::The event definition establishes what the recorded completion means; opening or starting a request may differ.]]. A started request and a completed workflow are different events. We need to confirm that the recorded signal matches the action we are discussing.
Mei | The supervisors say people return to email when they cannot identify the next approver. I do not yet know whether that is configuration or training.
Daniel | That is a useful [[adoption barrier::An adoption barrier is the obstacle to intended use; the reported approver problem still needs investigation.]] to investigate. Let us look at the affected roles and steps before prescribing another general training session or assuming people simply dislike change.
Mei | Could the score include this workflow information? It is more relevant to our purchase than how often someone opens the homepage.
Daniel | We can review the [[weighting::Weighting determines each component's influence; changing it should improve relevance rather than merely change the color.]] and the signals with our team. The purpose is a more useful account picture, not a different color chosen to justify a conclusion we already want.
Mei | I also want to distinguish someone who tried it once from a team that relies on it throughout the month.
Daniel | Exactly. [[Frequency::Frequency describes repeated use within a defined period; one completion does not establish habitual adoption.]] and task context matter alongside the number of users. We should not turn at least once into a claim of regular, independent use.
Mei | Let us begin with the supervisor group that reported the approver problem, then compare the same group after it is addressed.
Daniel | That gives us a defined [[cohort::A cohort supplies a consistent group for follow-up, with membership changes disclosed rather than hidden.]]. We will record membership changes and keep the completion definition consistent, so a rise does not merely reflect a different population.
Mei | Please keep the renewal discussion separate for now. I am describing a workflow problem, not announcing that we intend to leave.
Daniel | Agreed. The [[usage gap::The usage gap is a difference between expected and observed use, not proof of an inevitable cancellation.]] deserves action, but it does not prove cancellation. We will validate the measure, investigate the approver obstacle, and agree what improvement we should check next.''',
    transfer_title='Use the correct adoption denominator',
    transfer_setup='In one month, 45 of 60 licensed users log in. Only 40 users need the scheduling workflow; 20 of those complete it. A dashboard based on logins does not establish scheduling adoption.',
    transfer='''Customer: "The login rate is ___." | 75% | Forty-five divided by sixty is 0.75, using all licensed users as the base.
Manager: "The eligible scheduling population is ___." | 40 | Forty users need the workflow, so they form the relevant completion denominator.
Customer: "The eligible completion rate is ___." | 50% | Twenty divided by forty is one half, not twenty divided by all licenses.
Manager: "A login is not necessarily a ___." | workflow completion | Access and completion are different events and must not be reported as interchangeable outcomes.''',
))


BOOK['units'].append(unit(
    title='Support Escalations and Incident Communication',
    scene='Offer the verified workaround without inventing a fix date',
    skill='Communicate confirmed impact, temporary relief, unresolved questions, and the next update under pressure.',
    brief='Incident I42 prevents scheduled report exports for eight confirmed customer accounts in the EU region. Support has verified an administrator-only manual download workaround for those accounts. It does not restore automated scheduling. Engineering is investigating; neither a permanent-fix date nor the cause is confirmed. An unsent customer message says the issue will be fixed tomorrow. Customer success manager Asha and support lead Leon must correct it. The next customer update is due at 14:00 UTC, even if the investigation has no new result.',
    cast='Asha | Customer success manager\nLeon | Support lead',
    culture=('Certainty is not the only form of reassurance', 'A customer under pressure needs a usable status, not a confident guess. Acknowledge the disruption and give a specific next contact. Explain unfamiliar technical terms in ordinary language, while keeping the approved workaround and its limits intact.'),
    a='''What is the confirmed impact? | Scheduled exports fail for eight confirmed EU-region accounts. | All products are unavailable worldwide. | Every EU account has lost its stored data. | Only administrator logins fail. | The brief limits confirmed impact to scheduled exports for eight identified accounts.
What does the workaround provide? | Administrator manual downloads, without restored scheduling | A permanent correction of the underlying cause | Automated exports for every account globally | Proof that the incident is closed | The verified workaround is a temporary manual route and does not repair automated scheduling.
What is confirmed about timing? | The next update is at 14:00 UTC. | The permanent fix arrives tomorrow. | The root cause will be known by 14:00 UTC. | No message is needed without a new result. | The communication deadline is confirmed, while the investigation outcome and fix date remain unknown.''',
    vocabulary='''incident | An event disrupting or degrading a service under the relevant process. | coordinate an incident
confirmed impact | The effect established by available evidence. | state confirmed impact
affected account | A customer account known to experience the issue. | identify affected accounts
scheduled export | Data output arranged to run automatically at specified times. | restore scheduled exports
workaround | A temporary way to reduce impact without fully correcting the underlying issue. | provide a verified workaround
permanent fix | A correction intended to resolve the underlying defect or cause. | validate a permanent fix
reproduction | Recreating reported behavior under specified conditions. | reproduce the issue
support case | A tracked customer request or problem report. | link the support case
escalation | Routing an issue to a role with appropriate expertise or authority. | escalate the case
severity | A classification of impact under an organization's incident rules. | assess incident severity
priority | The order or urgency assigned to work. | confirm the response priority
incident owner | The person accountable for coordinating the incident response. | identify the incident owner
root cause | The underlying cause established through investigation. | verify the root cause
mitigation | An action reducing impact or risk. | apply an approved mitigation
restoration | Return of a service or capability to the defined working state. | confirm service restoration
status update | A communication of current facts and next actions. | issue a status update
update cadence | The agreed frequency of status communication. | maintain the update cadence
ETA | Estimated time of arrival or completion; its event and uncertainty must be stated. | qualify an ETA
UTC | Coordinated Universal Time, a shared time reference. | specify the time in UTC
known limitation | A confirmed boundary on capability or effectiveness. | disclose known limitations
scope of impact | The services, users, or accounts affected. | verify the scope of impact
customer impact | The effect on a customer's work or operations. | describe customer impact
post-incident review | A later assessment of events, response, and improvements. | schedule a post-incident review
resolution criterion | A condition used to determine whether the incident can be closed. | confirm resolution criteria''',
    precision='Eight confirmed accounts is the known scope, not proof that no others are affected. The manual route provides limited relief to administrators. It does not restore scheduling, establish the root cause, or justify saying the incident has been permanently resolved.',
    precision_extra='The next-update time and the estimated completion time refer to different events. Asha can promise an update at 14:00 UTC without promising a fix then. Claims about data loss, security, or wider impact require their own verified evidence.',
    phrases='''Acknowledge the impact | I understand that the missing reports are interrupting your daily review.
State the known scope | We have confirmed scheduled-export failures in eight EU-region accounts.
Keep the scope qualified | We are still checking whether other accounts are affected.
Explain the workaround | Administrators can use the verified manual download route.
State the limitation | That route does not restore automated scheduling.
Protect the instructions | Use the approved steps for the affected account configuration.
Correct the promise | We do not have a confirmed permanent-fix date.
Separate two events | Fourteen hundred UTC is the next update time, not a fix deadline.
Maintain contact | We will update you then even if the investigation is still open.
Avoid inventing a cause | The cause has not yet been confirmed.
Coordinate the message | Link the customer case to incident I42 so updates stay consistent.
Check the customer need | Which scheduled report is blocking your immediate work?
Avoid unsafe reassurance | I cannot make a data-loss or security claim without verified information.
Escalate new evidence | Send the new account details through the approved support route.
Define closure | Confirm restoration against the incident team's agreed criteria.
Close with a clear status | A workaround is available; investigation continues; the next update is at fourteen hundred UTC.''',
    notes='''Confirmed | Distinguishes verified scope from assumptions about the wider service.
Still checking | Keeps uncertainty visible without implying no investigation is happening.
Does not restore | Makes the temporary route's limitation explicit.
Next update | Promises communication rather than technical completion.
Has not yet | Describes current knowledge without claiming the cause is unknowable.
Approved steps | Avoids improvising technical instructions in a customer conversation.''',
    d='''Which corrected message is accurate? | A verified administrator workaround is available; the fix date remains unconfirmed. | All exports will be permanently repaired tomorrow. | A manual download proves automatic scheduling is restored. | Eight reports mean only eight people are affected. | The brief confirms a bounded workaround but does not confirm restoration or a permanent-fix date.
What should happen at 14:00 UTC if nothing has changed? | Send the promised update and state that the investigation continues. | Wait silently until engineering has a final answer. | Announce closure because the update deadline has arrived. | Replace the unknown date with tomorrow. | The agreed communication commitment applies even when the technical status is unchanged.
Which scope statement avoids overclaiming? | Eight accounts are confirmed affected; wider impact is still being checked. | Exactly eight accounts worldwide can possibly be affected. | Every EU account is confirmed affected. | The entire service has permanently failed. | Confirmed cases define current knowledge rather than establishing a complete global boundary.
Which statement requires additional verified evidence? | No data was lost and no security issue occurred. | The next update is at 14:00 UTC. | Manual download does not restore scheduling. | The permanent-fix date is unconfirmed. | The supplied facts establish neither data-loss status nor security conclusions, so those assurances are unsupported.''',
    dialogue='''Asha | The customer update says the exports will be fixed tomorrow. Before I send it, has engineering confirmed that date?
Leon | No. The [[permanent fix::No permanent-fix date is confirmed; the proposed message incorrectly converts uncertainty into a promise.]] is still under investigation. Please remove tomorrow. We can give the verified workaround and the next update time, but we should not manufacture a completion estimate.
Asha | The customer is missing its morning reports and wants something useful now. What exactly can we offer?
Leon | The approved [[workaround::The workaround allows administrator manual downloads but does not correct automated scheduling or establish permanent resolution.]] lets administrators download the reports manually for the affected configuration. It does not restore scheduled delivery, so we need to explain the manual effort and access requirement.
Asha | I will avoid saying exports are fully restored. Do we know how many accounts are affected?
Leon | The [[confirmed impact::Confirmed impact currently covers scheduled-export failures for eight identified EU-region accounts, not every account or service.]] is scheduled-export failure in eight accounts in the EU region. That is what we have verified so far, not proof that no additional accounts will report the issue.
Asha | One contact has asked whether the underlying report data has disappeared. I do not see an approved statement about that.
Leon | Do not add one without verification. The [[scope of impact::The scope must be verified for each claim; export failure alone establishes neither data loss nor its absence.]] needs evidence for each claim. We should route the question to the incident team instead of inferring data loss, or its absence, from an export symptom.
Asha | I also need to connect our account's ticket with the wider response. They are currently receiving two different messages.
Leon | Link the [[support case::Linking the support case to I42 keeps account-specific reports connected to the coordinated incident response.]] to I42 and use the approved incident status. Preserve their specific business impact, but do not create a separate fix date in the account notes.
Asha | Their finance lead needs a report before an afternoon meeting. Can I ask which report is most urgent without changing the incident severity myself?
Leon | Yes. Record the [[customer impact::Customer impact describes the blocked business work and helps reviewers assess needs without inventing a resolution promise.]] and send it through the response process. The team can assess urgency using the actual facts; a forceful message alone does not define the technical severity.
Asha | We promised another message at fourteen hundred UTC. If engineering has no new finding, should I wait until there is more to say?
Leon | Keep the [[update cadence::The agreed cadence requires the promised update even if the investigation has not produced a new finding.]]. At fourteen hundred UTC, state that investigation continues, confirm any unchanged workaround, and give the next communication point agreed by the response team.
Asha | I want to be clear that fourteen hundred refers to communication. Otherwise the customer may hear it as another completion time.
Leon | Exactly. It is not an [[ETA::ETA concerns estimated completion of a specified event; the update appointment is not a technical fix estimate.]] for a fix. Use the words next update and name UTC, rather than saying we will have it for you by two.
Asha | If someone can download the report manually, should support close the incident or leave it open?
Leon | Follow the agreed [[resolution criteria::Resolution criteria determine closure; successful temporary manual access does not establish restoration of scheduled exports.]]. Temporary relief does not by itself show that scheduling is restored. The incident team needs the defined verification before declaring the affected capability resolved.
Asha | Then my message will acknowledge the disruption, give the approved manual option, explain its limit, and keep the fix date unconfirmed.
Leon | Good. Check that the [[status update::The status update should align verified impact, workaround limits, unknowns, and the confirmed communication time.]] matches those facts and says when we will contact them again. That is a useful commitment we can keep while the technical investigation continues.''',
    transfer_title='Correct another premature fix promise',
    transfer_setup='Incident J18 affects automated invoice downloads for five confirmed accounts. An approved manual route is available to administrators. The fix date is unknown. The next update is 11:30 UTC.',
    transfer='''Manager: "The known affected-account count is ___." | five | Five is the confirmed count, not proof that no further accounts could be affected.
Customer: "The temporary route requires ___." | administrator access | The manual route is restricted to administrators under the supplied workaround conditions.
Manager: "The permanent-fix date remains ___." | unknown | No completion date has been confirmed, despite the available temporary route.
Customer: "The next update is at ___." | 11:30 UTC | The stated time is a communication commitment rather than a promise of technical completion.''',
))


BOOK['units'].append(unit(
    title='QBRs and Business Outcomes',
    scene='Replace the impressive ROI claim with a defensible value story',
    skill='Present measured change, disclose valuation assumptions, and separate released capacity from proven financial return.',
    brief='For a quarterly business review, Kira prepares a slide claiming proven savings and return on investment. Customer finance lead Joel confirms logs showing 40 staff hours for one reporting cycle before implementation and 28 for one cycle afterward. Other process changes occurred too. Kira values the 12-hour difference at an unvalidated $40 per hour and annualizes it over 12 months. The annual subscription costs $3,600; implementation and training costs are not fully recorded. Staffing expenditure has not changed. The slide must distinguish observations, assumptions, attribution, and missing costs.',
    cast='Kira | Customer success manager\nJoel | Customer finance lead',
    culture=('A challenge to the numbers can strengthen the relationship', 'A customer questioning a value slide is not necessarily rejecting the product. Welcome the distinction between useful operational improvement and an unsupported financial claim. Agree which figures the customer validates, which remain assumptions, and what evidence the next review needs.'),
    a='''What change do the time logs show? | A 12-hour difference between the two recorded cycles | A verified 12-hour monthly saving for every future month | A $5,760 reduction in cash expenditure | Proof that the product alone caused all improvement | Forty minus twenty-eight is twelve hours, but the logs cover only the stated cycles.
Which input has not been validated? | The $40 hourly valuation | The logged 40-hour earlier cycle | The logged 28-hour later cycle | The $3,600 annual subscription price | Joel confirms the time logs, while the hourly monetary value remains an assumption.
Why is a proven full ROI claim unsupported? | Attribution and recurring benefits are unverified, and relevant costs are incomplete. | Time differences can never be useful. | Subscription cost is always the only relevant cost. | The customer has confirmed that all benefits are cash savings. | The evidence leaves causal, recurring-benefit, valuation, and cost gaps that prevent the asserted financial conclusion.''',
    vocabulary='''QBR | Quarterly business review; a periodic discussion of outcomes, priorities, and progress. | prepare a QBR
business outcome | A result relevant to the customer's goals or operations. | validate business outcomes
baseline | The defined starting measure for a comparison. | establish a baseline
comparison period | The time window used as the counterpart in an analysis. | align comparison periods
observed change | A measured difference, without automatically establishing its cause. | report observed change
attribution | Assigning an effect to a cause or contributor. | qualify attribution
time saving | A reduction in time required under a stated comparison. | validate time savings
released capacity | Staff time made available for other work. | describe released capacity
cash saving | A reduction in actual expenditure under a defined comparison. | verify cash savings
hourly valuation | The monetary value assigned to an hour for an analysis. | validate the hourly valuation
annualization | Extending a shorter-period amount to an annual estimate using assumptions. | disclose annualization assumptions
benefit estimate | A calculated or proposed value not necessarily realized. | qualify the benefit estimate
ROI | Return on investment; net benefit relative to investment cost on a stated basis. | substantiate ROI
net benefit | Benefits minus included costs under a defined calculation. | calculate net benefit
cost base | The costs included in a comparison or calculation. | define the cost base
implementation cost | Expenditure or resources used to introduce the solution. | capture implementation costs
training cost | The resources or expenditure associated with preparing users. | include training costs
subscription cost | The recurring access charge under the relevant agreement. | confirm subscription costs
validation | Checking a claim or measure against appropriate evidence. | obtain customer validation
value realization | Actual achievement of an intended customer benefit. | track value realization
confounding factor | Another influence that complicates attribution of an observed change. | identify confounding factors
sensitivity analysis | Examining how results change when assumptions vary. | test assumption sensitivity
outcome owner | The person responsible for confirming and tracking the relevant result. | name the outcome owner
value narrative | An explanation connecting evidence to a customer-relevant benefit. | build a credible value narrative''',
    precision='The observed difference is 40 minus 28, or 12 hours. At the assumed $40 per hour, that equals $480 for a cycle. Multiplying by 12 gives $5,760 only if the monthly frequency, repeated difference, and valuation assumptions hold.',
    precision_extra='A common ROI expression is (benefits minus costs) divided by costs, using a defined period and consistent basis. Here neither a complete cost base nor validated recurring monetary benefit is available. Released time is not automatically reduced payroll or cash expenditure.',
    phrases='''Acknowledge the correction | You are right to distinguish the time logs from a proven financial return.
State the observation | The recorded cycle fell from forty staff hours to twenty-eight.
Calculate the difference | That is twelve fewer hours in the compared cycles.
Limit the inference | The comparison does not isolate the product's contribution.
Identify another influence | Other process changes occurred during the same period.
Label the valuation | Forty dollars per hour is an assumption that needs your validation.
State the conditional figure | At that rate, twelve hours would be valued at four hundred eighty dollars.
Qualify annualization | The annual estimate assumes the same benefit in twelve monthly cycles.
Distinguish capacity | The time difference may release capacity without reducing cash expenditure.
Expose missing costs | Implementation and training costs are not fully recorded.
Withdraw the overclaim | We should not call this proven ROI.
Keep the useful result | The operational change is still worth reporting accurately.
Ask for ownership | Who can validate the time measure and the monetary basis?
Agree the next evidence | Compare further cycles using a consistent task definition.
Separate evidence and assumption | Let us label each input before discussing the result.
Close the review | We will report the observed change and a plan to validate value over time.''',
    notes='''Recorded | Grounds the claim in the actual time logs.
Compared cycles | Avoids presenting a limited observation as a permanent monthly result.
At that rate | Makes the monetary figure conditional on the valuation.
Assumes | Identifies an input that has not been demonstrated.
May release | Keeps potential capacity distinct from verified cash savings.
Still worth reporting | Corrects an overclaim without dismissing a useful operational signal.''',
    d='''What follows from the stated hourly assumption? | Twelve hours at $40 would be valued at $480 per cycle. | The customer has already saved $480 in cash. | The product alone caused every hour of improvement. | The annual subscription is $480. | Multiplication produces a conditional value, not proof of cash savings or exclusive causation.
What is required to describe $5,760 responsibly? | State the assumptions of twelve similar monthly cycles and the unvalidated hourly value. | Label it audited annual cash savings. | Treat it as a guaranteed renewal credit. | Omit the period because the number is positive. | Annualization extends a limited observation and therefore needs explicit frequency, recurrence, and valuation assumptions.
Which cost statement is accurate? | The $3,600 subscription is known, but the full cost base is incomplete. | All implementation and training costs are confirmed zero. | Subscription cost can be ignored when calculating ROI. | Missing costs prove the investment lost money. | Incomplete cost records prevent a full return calculation without establishing either a positive or negative result.
Which review conclusion is strongest? | Report the observed operational change and agree a consistent validation plan. | Remove every positive finding because attribution is uncertain. | Keep the proven-ROI headline and hide its assumptions. | Replace missing evidence with a larger hourly rate. | A bounded observation and explicit next evidence preserve useful learning without inventing financial certainty.''',
    dialogue='''Joel | The slide says proven ROI. I recognize the time logs, but I have not approved the financial claim underneath them.
Kira | You are right. The [[observed change::The logs establish a twelve-hour difference between two cycles, not a proven recurring financial return.]] is from forty staff hours to twenty-eight for the two recorded cycles. I have moved too quickly from that difference to a broader claim about return.
Joel | There were other process changes at the same time. We simplified the approval route as well as introducing the product.
Kira | Then [[attribution::Attribution remains uncertain because other process changes could contribute to the observed time difference.]] needs qualification. The comparison does not isolate what the product caused. We can report the change without claiming that every hour came from one feature or supplier.
Joel | The twelve-hour difference is correct. Where did the forty-dollar hourly number come from?
Kira | It is an unvalidated [[hourly valuation::The forty-dollar hourly valuation is an assumption, not a rate already confirmed by the customer.]] in my calculation. At that rate, twelve hours would be worth four hundred eighty dollars for a cycle, but I should not present your approval as already given.
Joel | And the five-thousand-seven-hundred-sixty-dollar annual figure assumes that the same thing happens every month?
Kira | Yes. That [[annualization::Annualization multiplies the conditional cycle value by twelve, assuming similar monthly results rather than demonstrating them.]] assumes twelve monthly cycles with the same difference and the same valuation. We have one before-and-after comparison, not twelve months of validated recurring benefits.
Joel | Nobody's pay has changed, and we have not reduced the team. The time may be useful, but it has not disappeared from our expenditure.
Kira | Then [[released capacity::Released capacity makes time available for other work without necessarily lowering payroll or cash expenditure.]] is the relevant distinction. Staff may use the time for other work. Calling it a cash saving would imply a spending reduction that you have not reported.
Joel | We pay thirty-six hundred annually for the subscription. The implementation effort and training time are not fully in the model yet.
Kira | The [[cost base::The cost base is incomplete because known subscription charges exclude unrecorded implementation and training resources.]] is incomplete. A return calculation needs the relevant benefits and costs on a consistent basis and over a defined period, not only the easiest numbers to find.
Joel | I do not want this to sound as though the product has delivered nothing. Our reporting work is clearly taking less recorded time.
Kira | Agreed. We can build a stronger [[value narrative::A value narrative can report useful operational evidence while clearly separating assumptions and missing financial inputs.]] around what we know. The recorded change is useful; the mistake was presenting an assumed financial interpretation as an established result.
Joel | For the next review, let us measure the same reporting task across more cycles. Otherwise changes in the task itself could distort the comparison.
Kira | We will keep the [[baseline::The baseline must use a consistent task and measurement definition so later comparisons remain interpretable.]] and task definition explicit. We should also record relevant process changes and exceptions rather than quietly treating unlike cycles as equivalent.
Joel | I can validate the finance inputs, while our operations lead confirms the time records and what people actually do with the released hours.
Kira | Naming an [[outcome owner::The outcome owner confirms the relevant result; finance and operations can validate different parts of the evidence.]] for each measure will help. Your finance validation and the operations evidence answer different questions, so neither should be substituted for the other.
Joel | Please revise the slide before the business review. Keep the time difference, but remove the proven-return headline.
Kira | I will describe [[value realization::Value realization concerns benefits actually achieved, which must be separated from the book's conditional financial estimates.]] only where we have evidence. The revised slide will show the observed twelve-hour difference, label the assumptions, identify missing costs, and state the next validation steps.''',
    transfer_title='Explain another conditional value estimate',
    transfer_setup='A team records 30 hours before and 24 hours after a change for one cycle. An unvalidated rate of $35 per hour is used. Staffing expenditure is unchanged, and implementation costs are missing.',
    transfer='''Customer: "The observed time difference is ___." | six hours | Thirty minus twenty-four gives six hours for the compared cycle, not a proven recurring annual benefit.
Manager: "At the assumed rate, the cycle value would be ___." | $210 | Six multiplied by thirty-five equals two hundred ten, conditional on the unvalidated hourly value.
Customer: "Unchanged expenditure means this is not verified ___." | cash savings | Time released does not establish a reduction in actual spending.
Manager: "A full return calculation still lacks ___." | implementation costs | The missing implementation costs make the relevant cost base incomplete.''',
))


BOOK['units'].append(unit(
    title='Renewals and Churn Risk',
    scene='Rebuild the renewal conversation after the main contact leaves',
    skill='Explore changed priorities, verify decision roles, and describe renewal risk without treating it as a verdict.',
    brief='Account R31 has a $60,000 annual recurring subscription scheduled for renewal on 12 November, six weeks away. Its main contact has left. New operations contact Ella has not confirmed current priorities or who owns the renewal decision and budget. Earlier reports focused on reducing a service backlog, but the business is now reorganizing. Customer success manager Rafael has no cancellation notice and no renewal approval. Ella agrees to a discovery meeting on 8 October at 10:00 UTC. Actual notice terms and the purchasing route still need checking.',
    cast='Ella | New customer operations contact\nRafael | Customer success manager',
    culture=('Do not make a new contact inherit old enthusiasm', 'A replacement stakeholder may have different priorities or knowledge from the previous contact. Give a brief factual handover and invite correction. A change in sponsorship is a reason to learn more, not permission to pressure the new person into endorsing an earlier plan.'),
    a='''What is the renewal date? | 12 November | 8 October | The day the former contact left | A new date already approved by Ella | The subscription is scheduled for renewal on 12 November; 8 October is a discovery meeting.
What is known about the decision? | Neither cancellation nor renewal approval has been received. | Ella has approved the renewal. | The former contact's departure cancels the agreement. | Reorganization guarantees an expansion. | The brief leaves the commercial outcome open while identifying information gaps and a stakeholder change.
What is the next agreed customer event? | A discovery meeting on 8 October at 10:00 UTC | Contract signature at 10:00 UTC | Automatic approval of a discount | Completion of every procurement step | The agreed meeting explores the current position and is not itself an approval or signature.''',
    vocabulary='''renewal | Continuation of an agreement or subscription under applicable terms. | coordinate a renewal
renewal date | The date specified for the relevant renewal event. | verify the renewal date
renewal owner | The role coordinating or responsible for the renewal decision process. | identify the renewal owner
budget owner | The person accountable for the relevant funding decision. | confirm the budget owner
stakeholder change | A change in people involved in or influencing the relationship. | track stakeholder changes
executive sponsor | A senior person supporting the initiative within the customer organization. | reestablish executive sponsorship
champion | An internal advocate who actively helps the initiative progress. | verify the champion relationship
reorganization | A change in organizational structure, roles, or responsibilities. | understand reorganization effects
churn risk | The possibility of losing customer business, with its basis specified. | assess churn risk
logo churn | Loss of customer accounts, distinct from the amount of revenue lost. | measure logo churn
revenue churn | Recurring revenue lost under a specified measurement definition. | distinguish revenue churn
contraction | A reduction in business from an existing customer. | identify contraction risk
retention | Continuation of customer business under a stated measure. | improve customer retention
GRR | Gross revenue retention; retained starting recurring revenue excluding expansion on a defined basis. | calculate GRR
NRR | Net revenue retention; retained starting recurring revenue including expansion on a defined basis. | calculate NRR
ARR | Annual recurring revenue, measured under the organization's stated inclusion rules. | verify ARR
risk signal | Evidence that may indicate a potential problem, not a certain outcome. | record a risk signal
save plan | A defined set of actions addressing an evidenced retention risk. | agree a save plan
renewal forecast | An estimate of renewal outcomes based on current evidence. | update the renewal forecast
notice provision | A contract term concerning required notices and their conditions. | review notice provisions
procurement route | The customer's process for reviewing and completing a purchase. | verify the procurement route
value evidence | Information supporting an actual customer benefit. | refresh value evidence
success criterion | A condition used to judge achievement of a desired result. | reconfirm success criteria
renewal plan | A shared sequence of renewal actions, owners, and dates. | maintain the renewal plan''',
    precision='A contact leaving is a risk signal, not a cancellation. An agreed meeting is progress, not renewal approval. The $60,000 recurring amount does not include an invented expansion or establish recognized revenue. Verify dates and notice terms in the actual agreement.',
    precision_extra='For a defined starting cohort, GRR excludes expansion while NRR includes it. If starting recurring revenue is 100, losses are 10, contraction is 5, and expansion is 20, GRR is 85% and NRR is 105%, using the same basis.',
    phrases='''Acknowledge the transition | I understand that responsibilities have changed since our last review.
Avoid inherited assumptions | I do not want to assume the previous priorities are still yours.
Give a factual handover | Earlier discussions focused on reducing the service backlog.
Ask about the present | Which outcomes matter most during the reorganization?
Confirm the date | The recorded renewal date is the twelfth of November.
Separate status from risk | We have neither a cancellation notice nor renewal approval.
Ask about ownership | Who now coordinates the renewal decision?
Check funding separately | Who owns the relevant budget?
Respect the new contact | How would you prefer us to involve the other decision participants?
Verify the process | We need the current purchasing route and required steps.
Check contractual details | Let us verify the actual notice provisions rather than assume them.
Use evidence | Which results can your team validate from the last period?
Avoid premature discounting | We should understand the issue before proposing a commercial change.
Make the next meeting useful | Let us use the eighth of October to confirm priorities and decision roles.
Keep the forecast honest | The outcome remains unconfirmed while those gaps are open.
Close the plan | Record each action, owner, evidence source, and next date.''',
    notes='''Still yours | Invites the new stakeholder to confirm or change earlier priorities.
Recorded | Identifies the current document information without inventing revised terms.
Neither ... nor | Keeps both unsupported conclusions out of the status report.
Now | Recognizes that decision roles may have changed.
Before proposing | Sequences diagnosis ahead of a commercial response.
Unconfirmed | Avoids disguising uncertainty as either retention or loss.''',
    d='''Which internal renewal update is justified? | The contact has changed; priorities and decision roles need confirmation; the outcome is open. | The account is lost because the old contact left. | The renewal is certain because a meeting is booked. | An immediate discount has already solved the risk. | The known stakeholder change supports investigation, not a predetermined commercial outcome.
What should Rafael ask Ella first? | What matters now and who participates in the decision | Why she has already rejected the product | Whether she will approve an unspecified discount today | Why she must preserve the former contact's priorities | Open factual discovery establishes the current context without imposing an unsupported interpretation.
For starting recurring revenue 100, loss 10, contraction 5, and expansion 20, what is GRR? | 85% | 105% | 95% | 115% | Gross retention excludes expansion: one hundred minus ten minus five, divided by one hundred.
Using those same figures, what is NRR? | 105% | 85% | 80% | 120% | Net retention includes expansion: one hundred minus ten minus five plus twenty, divided by one hundred.''',
    dialogue='''Rafael | Thank you for taking over the conversation. The account is due for renewal on the twelfth of November, and I would like to understand what has changed.
Ella | I can discuss operations, but I have only recently inherited this relationship. I do not yet know who is the [[renewal owner::The renewal owner coordinates the decision process; Ella has not confirmed that this responsibility belongs to her.]] across our reorganized teams.
Rafael | That is helpful to know. Our earlier reviews focused on reducing the service backlog, but I do not want to assume that is still the main priority.
Ella | Backlog matters, but we are also combining two service teams. The [[success criteria::Success criteria need reconfirmation because the reorganization may change which customer outcomes matter most.]] may need to change. I need to speak with the new director before confirming what the combined team requires.
Rafael | We can use our meeting on the eighth of October at ten hundred UTC to clarify that. Who else should contribute to the discussion?
Ella | Let me check the roles first. I do not want an invitation to imply that I am the [[budget owner::The budget owner controls the relevant funding decision; an operations role or meeting invitation does not establish that authority.]] or that finance has already approved continuation.
Rafael | Agreed. We can distinguish operational needs, funding, and purchasing steps. I will keep you involved as we establish the right route.
Ella | Please do. The [[stakeholder change::The departure and replacement of the main contact create an information gap, not automatic cancellation or renewal.]] has left some history scattered across people. A brief factual handover would help more than a presentation assuming everyone already supports the old plan.
Rafael | I can summarize the agreed objectives, recorded usage, and the results previously discussed, marking anything that still needs your validation.
Ella | That [[value evidence::Value evidence should show validated customer results, with uncertain or outdated claims clearly identified.]] will be useful. Please separate actual outcomes from estimates. The new director will ask what the team gained, not simply how many meetings the supplier held.
Rafael | Understood. Internally, I have recorded the contact change as something we need to address, not as proof that the account is leaving.
Ella | Good. A [[risk signal::A risk signal indicates a possible retention issue but does not establish the customer's final decision.]] is not a decision from us. We have sent neither a cancellation notice nor an approval to renew.
Rafael | Before we discuss terms, we should also verify the agreement's notice requirements and the current purchasing steps. I do not want to assume how those work.
Ella | I can help locate the right colleagues. The [[procurement route::The procurement route identifies the actual customer purchasing steps, rather than assuming operations can complete them alone.]] may have changed in the reorganization, so last year's contacts are not necessarily the people who can complete this year's process.
Rafael | Someone suggested offering a discount immediately. I would rather first understand whether the issue is fit, budget, process, or simply missing information.
Ella | That makes sense. A [[save plan::A save plan should address an evidenced retention problem; an unexplained discount may miss the actual customer issue.]] built around the wrong problem will not help us decide. There is no confirmed price objection for you to solve today.
Rafael | I will keep the forecast open while we establish those facts. A scheduled discussion should not be reported as a completed renewal.
Ella | Please make the [[renewal forecast::The renewal forecast must reflect current evidence; a booked meeting is not approval or a guaranteed outcome.]] reflect that distinction. We can make progress without pretending the commercial decision has already happened.
Rafael | For the eighth, I will bring the factual history and open questions. You will confirm which roles should attend and what priorities they can speak to.
Ella | Yes. Then we can build a [[renewal plan::The renewal plan records the agreed actions, owners, and dates while preserving unresolved decision questions.]] with the actual decision participants, owners, and dates. Keep the twelfth of November visible, but do not use it to invent approvals we have not given.''',
    transfer_title='Describe another renewal without guessing the outcome',
    transfer_setup='Account T08 renews on 20 December. Its sponsor has moved roles. New contact Hugo agrees to a needs review on 4 November but has not confirmed the budget owner. No renewal or cancellation decision is recorded.',
    transfer='''Manager: "The recorded renewal date is ___." | 20 December | The renewal date differs from the earlier needs-review meeting.
Contact: "The fourth of November is a ___." | needs review | The agreed event explores needs and is not a contract signature or approval.
Manager: "The funding decision role remains ___." | unconfirmed | The new contact has not identified the budget owner.
Contact: "The commercial outcome is still ___." | open | Neither renewal nor cancellation is recorded, so neither conclusion is justified.''',
))


BOOK['units'].append(unit(
    title='Expansion and Upsell Ethics',
    scene='Check the existing capacity before selling more seats',
    skill='Explore additional demand, verify license rights, and align expansion with readiness and customer benefit.',
    brief='Customer administrator Nora asks success manager Sam for 25 additional licenses for a new team. The account already holds 80 named-user licenses: 50 assigned and 30 unassigned. Of the 50 assigned users, 35 have completed onboarding. The new team needs the same proposed workflow, but its requirements and training availability are unconfirmed. Use of existing unassigned seats requires the customer license owner to confirm entitlement and allocation. No additional purchase or allocation has been approved. Sam must assess fit and readiness before presenting a justified commercial option.',
    cast='Nora | Customer administrator\nSam | Customer success manager',
    culture=('A useful commercial conversation can begin with restraint', 'Customers may ask for a product quantity as a shortcut to describing a business need. Clarify the need and existing capacity before assuming the right purchase. Explain remaining work honestly, and do not use an adoption problem merely as a reason to withhold a suitable option.'),
    a='''How many existing seats are unassigned? | 30 | 25 | 15 | 50 | Eighty total licenses minus fifty assigned leaves thirty unassigned seats.
How many assigned users have completed onboarding? | 35 of 50 | 35 of 80 newly added users | 50 of 50 | 25 of 30 | The stated completion count is thirty-five among the fifty currently assigned users.
What must happen before using existing unassigned seats? | The customer license owner must confirm entitlement and allocation. | Sam may silently assign them to any organization. | A new order must always be signed first. | Training completion automatically changes the contract. | The brief makes license-owner confirmation a prerequisite without assuming a new purchase is necessary.''',
    vocabulary='''expansion | Growth in business with an existing customer. | assess an expansion opportunity
upsell | A move to a higher-value quantity, tier, or offering. | justify an upsell
cross-sell | Sale of a different, related offering to an existing customer. | assess cross-sell fit
seat | A unit of user access under specified licensing terms. | count available seats
named-user license | An access entitlement assigned to an identified individual under the agreement. | verify named-user licenses
concurrent-user license | Access measured by simultaneous use under the agreement's rules. | distinguish concurrent-user licensing
assigned seat | A license allocated to a specified user under the relevant rules. | review assigned seats
unassigned seat | A license not currently allocated to a user. | verify unassigned seats
license utilization | Use or allocation of licenses under a stated measurement definition. | define license utilization
entitlement | The access or usage rights granted by the applicable agreement. | confirm entitlement
allocation | Assignment of available resources or access to a purpose or user. | approve license allocation
license owner | The customer role responsible for managing the relevant license rights. | consult the license owner
onboarding completion | Completion of defined preparation steps for a user or group. | verify onboarding completion
readiness gap | A missing condition needed for effective use. | address readiness gaps
incremental demand | Additional need beyond an established baseline. | establish incremental demand
fit assessment | Evaluation of whether an offering meets the relevant needs. | conduct a fit assessment
commercial option | A proposed purchase arrangement with defined scope and terms. | compare commercial options
order form | The document specifying the relevant purchase details and terms. | review the order form
proration | Proportional charging for a partial period under stated rules. | explain proration
co-termination | Aligning the end dates of subscriptions under agreed terms. | discuss co-termination
true-up | Adjustment to align reported or licensed usage with contractual requirements. | review true-up terms
shelfware | Informal term for purchased software that is little used or unused. | investigate shelfware
expansion readiness | Evidence that added scope can be used effectively. | assess expansion readiness
customer benefit | A relevant advantage for the customer, supported by evidence or clearly labeled assumptions. | establish customer benefit''',
    precision='The account has 30 unassigned seats, but availability is not automatically permission to allocate them. If the license owner authorizes 25 of those seats for the new team, 5 would remain unassigned; no additional quantity is assumed necessary from the count alone.',
    precision_extra='Onboarding completion is 35 of 50 assigned users, or 70%. That is not 70% of all 80 licenses, and it does not prove independent workflow use. Named-user rights must not be treated as permission to share one identity among several people.',
    phrases='''Explore the request | What work will the twenty-five new users need to complete?
Check current capacity | The account has thirty unassigned seats.
Qualify availability | We need the license owner to confirm that those seats can be allocated to this team.
Avoid an automatic sale | The request does not yet establish a need for twenty-five additional licenses.
Check the arithmetic | Allocating twenty-five existing seats would leave five unassigned.
Respect the terms | Allocation must follow the actual entitlement and approved process.
State the readiness gap | Fifteen currently assigned users have not completed onboarding.
Avoid a false equivalence | Training completion does not prove regular workflow use.
Ask about resources | Who will own onboarding for the new team?
Assess fit | Let us confirm their workflow and access requirements.
Keep alternatives open | A justified additional purchase remains an option if existing rights do not meet the need.
Separate two decisions | License allocation and readiness for use need separate confirmation.
Avoid pressure | I will not invent an expiry date to accelerate the purchase.
Explain an actual quote | Any proposal will show quantity, term, charges, and approval status.
Avoid credential sharing | Use the approved user-access arrangement rather than shared named-user identities.
Close with next steps | Verify entitlement, confirm the workflow, and agree the onboarding owner before recommending quantity.''',
    notes='''Does not yet | Leaves room for evidence that an additional purchase is genuinely needed.
Would leave | Makes the arithmetic conditional on authorized allocation.
Separate confirmation | Prevents licensing rights from being confused with practical readiness.
Remains an option | Avoids treating responsible assessment as a blanket refusal to sell.
Actual entitlement | Directs the decision to the governing rights, not a dashboard count alone.
Before recommending | Connects the commercial recommendation to established customer need.''',
    d='''Which response best fits the request? | Confirm needs and allocation rights before deciding whether additional licenses are necessary. | Immediately quote 25 new seats without checking existing capacity. | Promise free reassignment before the license owner confirms it. | Refuse every expansion until all users complete every possible feature. | The relevant decision depends on entitlement, customer need, and readiness, not an automatic sale or blanket refusal.
If 25 existing unassigned seats are authorized for the new team, how many remain? | 5 | 15 | 30 | 55 | Thirty unassigned seats minus twenty-five allocated seats leaves five.
What is the stated onboarding completion rate among assigned users? | 70% | 43.75% | 62.5% | 30% | Thirty-five divided by fifty equals seventy percent; dividing by all eighty licenses uses a different denominator.
Which proposal would be transparent? | A justified quantity with term, charges, allocation basis, and approval status | A quantity chosen only to meet the supplier's target | A promise that every unassigned seat may be used anywhere | A shared-login plan presented as named-user compliance | A transparent commercial option explains its basis and terms rather than concealing need, permissions, or status.''',
    dialogue='''Nora | We are adding another team. Could you send an order for twenty-five more licenses so I can get them started?
Sam | I can help assess that, but let us check the existing [[unassigned seats::Thirty unassigned seats exist, but their allocation still depends on the customer's confirmed licensing rights and process.]] first. Your account has eighty licenses, fifty assigned and thirty unassigned. We should understand whether the new team needs additional rights or an allocation of existing capacity.
Nora | They expect to use the same approval workflow. Does having thirty spare seats mean I can assign twenty-five immediately?
Sam | We need the license owner to confirm the [[entitlement::Entitlement defines permitted use under the agreement; a visible unassigned count alone does not establish permission.]] and allocation. The count shows potential capacity, but I should not interpret the agreement or approve a different team's access on your behalf.
Nora | I will involve our license owner. If those seats can be allocated, the remaining number would be five, correct?
Sam | Correct, subject to that approved [[allocation::Authorized allocation of twenty-five from thirty unassigned seats would leave five, without increasing total licenses.]]. Twenty-five taken from thirty leaves five. It would not increase the total from eighty to one hundred five.
Nora | I also see that only thirty-five of our fifty assigned users have finished onboarding. I do not want the new group to repeat the same difficulties.
Sam | That [[onboarding completion::Thirty-five of fifty assigned users completed onboarding, leaving fifteen whose preparation is not complete.]] figure is seventy percent of assigned users. We should identify the unfinished steps and barriers, but we should not assume every person has the same problem or that training alone proves adoption.
Nora | The new team has not confirmed who will attend training. Their manager asked for access before discussing the practical schedule.
Sam | That is a [[readiness gap::Unconfirmed training attendance and ownership are readiness gaps even if enough valid licenses are available.]] separate from license quantity. Who will own their preparation, and when can the relevant users practice the workflow they actually need?
Nora | I can ask the manager. Would you still be willing to quote more seats if our existing rights do not cover that team?
Sam | Certainly. We should establish [[incremental demand::Incremental demand is the additional need beyond usable existing rights, not simply the number of newly interested users.]] after checking the actual rights and requirements. A suitable additional purchase is a valid option; it just needs a customer basis rather than an assumption from the first request.
Nora | Their process may include an extra approval step. We have not confirmed whether the current configuration supports it.
Sam | Then include that in the [[fit assessment::The fit assessment checks the new team's actual workflow and access needs before recommending a purchase or rollout.]]. More seats do not solve a workflow mismatch by themselves. We should check capability and configuration alongside the training plan.
Nora | Some teams have shared access in other systems. I assume that is not something we should improvise here.
Sam | Correct. These are [[named-user licenses::Named-user licenses apply to identified individuals under their terms and must not be treated as shared-login permission.]]. Follow the approved identity and access arrangement; do not use shared credentials as a shortcut around the actual license or security requirements.
Nora | Once we know the right quantity, I will need a clear explanation of the term and any partial-period charge.
Sam | Any [[commercial option::A commercial option should state the justified quantity, term, charges, and status rather than conceal assumptions.]] should show those details, including the applicable charging basis. I will not invent a discount deadline or imply a new order is approved before your purchasing process is complete.
Nora | Then the immediate decision is not buy twenty-five or buy nothing. It is establish what rights and preparation the team needs.
Sam | Exactly. [[Expansion readiness::Expansion readiness combines usable rights, workflow fit, and practical preparation; it is not established by a purchase request alone.]] comes from those facts. Let us confirm the license owner, the workflow requirements, and the onboarding owner, then recommend the quantity and arrangement that actually serve the team.''',
    transfer_title='Assess another request for more licenses',
    transfer_setup='An account has 100 licenses, with 70 assigned and 30 unassigned. A new team needs 20 users. Existing allocation rights need confirmation. Of the 70 assigned users, 49 have completed onboarding.',
    transfer='''Manager: "The unassigned count is ___." | 30 | One hundred total licenses minus seventy assigned leaves thirty unassigned.
Customer: "If twenty existing seats are authorized, ___ remain." | ten | Thirty minus twenty leaves ten, conditional on approved allocation.
Manager: "Onboarding completion among assigned users is ___." | 70% | Forty-nine divided by seventy is seventy percent, using assigned users as the denominator.
Customer: "Before allocation, we must confirm ___." | entitlement | A spare count does not itself establish permitted use for the new team.''',
))


BOOK['units'].append(unit(
    title='Product Feedback and Feature Requests',
    scene='Discover the workflow behind the requested button',
    skill='Turn a proposed feature into a precise problem, usable evidence, and a responsible product-team handoff.',
    brief='Customer operations lead Nia requests a bulk-approval button. Twenty approvers handle about 200 requests weekly; around 40 need individual exception review. Staff report repeated navigation between similar requests. The customer requires a separate authorized decision record for each request. The current product offers a saved filtered view but no confirmed bulk-approval capability. Success manager Teo must clarify the repeated work and pass the need to product manager Arun. Logging the request does not assign delivery priority or a release date. Any interim approach must preserve the decision-record requirement.',
    cast='Nia | Customer operations lead\nTeo | Customer success manager',
    culture=('Respect the proposed solution while exploring the problem', 'A customer may name a feature because it is the clearest way to express frustration. Do not dismiss the idea as merely a request. Ask for the relevant sequence and obstacle, then confirm the problem in words the customer recognizes before discussing alternative approaches.'),
    a='''What problem has the customer reported? | Repeated navigation between similar approval requests | A confirmed inability to sign in | A verified loss of all approval records | A request to remove all authorization | The brief identifies repetitive navigation, while retaining separate authorized decisions remains a requirement.
What record must an interim approach preserve? | A separate authorized decision for each request | Only one anonymous decision per week | No record for routine requests | A single record covering all twenty approvers | The customer explicitly requires an individual authorized decision record for every request.
What does logging the feature request establish? | That the need has been recorded for assessment | A committed delivery date | The highest priority in the product plan | A capability already released to all customers | Recording feedback does not itself determine priority, feasibility, or release timing.''',
    vocabulary='''feature request | A proposal for a product capability or change. | capture a feature request
problem statement | A clear description of the difficulty to be addressed. | refine the problem statement
use case | A specific situation in which a capability would be used. | document the use case
workflow | The sequence of activities used to complete a task. | map the workflow
friction point | A step that creates avoidable difficulty or effort. | identify friction points
bulk action | An operation applied to multiple selected items. | assess bulk-action needs
exception handling | The treatment of cases outside the normal pattern. | preserve exception handling
audit trail | A traceable record of actions and decisions. | preserve the audit trail
authorization | Permission to perform a specified action. | verify authorization
saved view | A reusable display configured with selected criteria. | configure a saved view
filter | A rule selecting which items are shown or processed. | validate the filter
interim approach | A temporary way of working pending a longer-term decision. | assess an interim approach
user story | A concise expression of a user's need and intended value. | refine a user story
acceptance criteria | Conditions used to judge whether a proposed solution meets the need. | define acceptance criteria
reproduction steps | A sequence allowing others to observe reported behavior. | provide reproduction steps
representative example | An example reflecting the relevant real-world pattern. | select representative examples
frequency | How often the relevant situation or action occurs. | quantify task frequency
impact statement | An explanation of how a problem affects the customer's work. | verify the impact statement
product backlog | A maintained collection of potential product work. | review the product backlog
prioritization | Deciding the relative order or importance of work. | explain prioritization
feasibility | Whether a proposed approach can be achieved under relevant constraints. | assess feasibility
roadmap | A communicated plan for product direction and anticipated work. | qualify roadmap information
discovery | Investigation of needs, context, and possible solutions. | support product discovery
feedback loop | A process that returns assessment or outcome information to the source. | close the feedback loop''',
    precision='About 200 requests and 40 exceptions suggest about 160 non-exception requests in that weekly pattern, not 160 automatically approvable records. Routine status does not remove the stated requirement for an authorized decision on each request.',
    precision_extra='A saved filtered view may reduce navigation, but it is not a bulk-approval capability. A logged request, a backlog entry, a roadmap item, and a released feature are different statuses. Confirm the actual status and its limits before communicating availability.',
    phrases='''Respect the idea | I understand why a bulk-approval button sounds useful.
Explore the sequence | Walk me through the repeated steps between two similar requests.
Identify the obstacle | Is the main effort navigation, comparison, or the decision itself?
Quantify frequency | About how many requests follow this pattern each week?
Separate exceptions | Which cases still need individual investigation?
Preserve the requirement | Every request must retain its own authorized decision record.
Check the current option | The saved view may reduce navigation, but it is not bulk approval.
Avoid premature advice | We need to verify the filter and permissions before recommending that approach.
State the problem | Repeated navigation slows review of similar requests.
Define a useful result | Reduce repeated navigation while preserving individual decisions and exception visibility.
Request minimal evidence | An approved, de-identified example of the workflow is enough for the initial assessment.
Explain the handoff | I will send the problem, frequency, impact, constraints, and examples to Arun.
Keep status clear | Recorded for assessment does not mean scheduled for release.
Avoid a roadmap promise | I do not have an approved delivery date to share.
Return the response | I will bring the product team's assessment back to you.
Close accurately | Let us confirm that this summary captures your need before we submit it.''',
    notes='''Sounds useful | Respects the proposed solution without claiming it is the chosen design.
Main effort | Distinguishes navigation from the judgment the user still needs to make.
While preserving | States a constraint that a faster approach must continue to satisfy.
May reduce | Labels the interim option as something to assess, not a proven outcome.
Recorded for assessment | Names a real status without implying implementation.
Captures your need | Checks that the handoff represents the customer accurately.''',
    d='''Which problem statement best represents the case? | Repeated navigation slows similar-request review while individual decisions must remain traceable. | The customer wants every request approved without review. | Forty exceptions prove that the entire product is unusable. | A new button is already approved for release. | The statement captures the reported effort and preserves the explicit decision-record constraint.
Which interim statement is responsible? | A saved view may help navigation, subject to verified filters and permissions. | A saved view automatically approves all visible records. | Routine requests no longer need individual decisions. | Any filter can replace the approval controls. | The known capability is a view, not bulk approval or permission to remove required controls.
What should the product handoff include? | The workflow, frequency, impact, constraints, and representative approved examples | Only the proposed button color | A promised release date invented by the success manager | Unnecessary unredacted customer records sent through any channel | A concrete, appropriately shared problem record supports assessment without unsupported commitments or excessive data.
Which customer update correctly describes backlog status? | The request is recorded for assessment; priority and delivery timing are not confirmed. | Backlog entry guarantees delivery this month. | Logging the request completes acceptance testing. | A roadmap discussion means the feature is already available. | Recorded work remains distinct from prioritization, implementation, testing, and actual release.''',
    dialogue='''Nia | Could you add a bulk-approval button? Our approvers spend too much time opening similar requests one after another.
Teo | I understand the [[feature request::The proposed bulk-approval button is a feature request, not yet an agreed solution or delivery commitment.]]. Before I pass it to product, can we identify which repeated steps are taking the time: finding the next request, comparing details, or making the decision?
Nia | Navigation is the part people complain about most. Twenty approvers handle about two hundred requests a week, and around forty need closer exception review.
Teo | Then the [[problem statement::The reported problem is repeated navigation during review, while exception handling and individual decisions remain necessary.]] should name that repeated navigation. We should also preserve the distinction between similar requests and exceptions rather than assume all two hundred can be handled identically.
Nia | Yes. Even a routine request needs its own authorized decision. We cannot lose the record of who decided what.
Teo | That [[audit trail::The audit trail must retain a separate authorized decision for each request, including routine requests.]] is a required constraint, not an optional detail. About one hundred sixty non-exception requests does not mean one hundred sixty records can be approved without an individual decision.
Nia | We currently move back to the full list after each review. Could the product at least keep the relevant requests together?
Teo | There is a [[saved view::A saved view can organize selected records, but it does not create or confirm a bulk-approval capability.]] that may help navigation. We need to check its filters and permissions for your workflow. It is not a bulk-approval function, and I do not want to describe it as one.
Nia | We can test whether the view helps, provided the exceptions stay visible and nobody gains permission they should not have.
Teo | Those are useful [[acceptance criteria::Acceptance criteria specify what a useful approach must achieve while preserving exception visibility and authorization boundaries.]] for assessing an interim approach. We can check navigation, exception visibility, and the required individual decision record without removing the controls to make the demonstration look faster.
Nia | What does Arun need from us? I do not want my team to produce a long specification before anyone looks at the need.
Teo | A concise [[use case::The use case describes the actual approver task, sequence, and context without requiring the customer to design the product.]] is enough for the initial discussion: who performs the task, the repeated steps, the frequency, and the obstacle. An approved de-identified example will help; we do not need unnecessary customer records.
Nia | Please include the distinction between navigation and decision effort. I do not want the team to hear that we asked to eliminate review.
Teo | I will include that in the [[impact statement::The impact statement explains the navigation burden without falsely claiming that the customer wants approval judgment removed.]]. I will send the workflow, frequency, constraints, and examples to Arun, then confirm that the summary represents what you actually need.
Nia | Once the request is logged, does that mean it is in the next release? I need to explain the status internally.
Teo | No. A [[product backlog::A backlog records potential work; entry does not establish delivery priority or a release commitment.]] entry records potential work. Product still needs to assess the need, alternatives, effort, and wider priorities. I do not have an approved release date to share.
Nia | Could another customer need move ahead of ours even if our request came first?
Teo | Yes. [[Prioritization::Prioritization considers relative value and constraints rather than guaranteeing delivery order from submission date alone.]] considers more than submission order. I can explain the assessment status and the evidence we supplied, but I cannot promise a ranking before that decision is made.
Nia | Then keep us informed when the assessment changes, including if the team proposes a different way to solve the problem.
Teo | I will close the [[feedback loop::Closing the feedback loop returns the assessment to the customer, including alternatives or unchanged status rather than silence.]]. We will test the bounded interim option, preserve your decision requirements, and return the product response without confusing an idea, a plan, and a released capability.''',
    transfer_title='Clarify another requested feature',
    transfer_setup='A customer requests one-click batch closure for service tickets. The reported problem is repeated navigation. Each ticket must retain an authorized closure record. A saved queue view exists, but batch closure has not been confirmed or scheduled.',
    transfer='''Customer: "The reported obstacle is ___." | repeated navigation | The stated problem concerns moving between tickets, not permission to remove closure decisions.
Manager: "Each ticket must retain an ___." | authorized closure record | The required record remains a constraint for any interim or future approach.
Customer: "The existing capability is a ___." | saved queue view | A view organizes tickets but does not establish batch-closure functionality.
Manager: "The release status for batch closure is ___." | not scheduled | No confirmed delivery schedule is supplied, so logging interest cannot become a release promise.''',
))


BOOK['units'].append(unit(
    title='Difficult Customers and Boundary Setting',
    scene='Repair the expectation without promising a date you cannot confirm',
    skill='Acknowledge impact, reconcile disputed records, and set a respectful boundary while keeping support available.',
    brief='Customer lead Beth says an export feature was promised for October and demands confirmation of 31 October. The available 17 September note says the team is targeting late October, subject to testing; it does not record a confirmed release date. Success manager Idris must check any additional evidence rather than deny that other conversations occurred. He can arrange a manager review and provide a status update by 15:00 UTC on Thursday. He cannot approve compensation or promise delivery. Company procedure allows a pause after a clear boundary if personal insults continue, while preserving an appropriate support route.',
    cast='Beth | Customer team lead\nIdris | Customer success manager',
    culture=('Firm dissatisfaction is not automatically abuse', 'A customer can dispute the record, demand accountability, or speak directly without crossing a conduct boundary. Respond to the substance first. If comments become personal, name the behavior calmly and offer a way to continue the work; do not use a boundary to avoid a legitimate complaint.'),
    a='''What does the available 17 September note say? | Late October is a target subject to testing. | The feature is already released. | 31 October is an unconditional confirmed date. | Compensation has been approved. | The note records conditional planning language, not the confirmed date the customer requests.
What can Idris commit to? | A status update by Thursday at 15:00 UTC | Delivery by 31 October | An immediate financial credit | A finding that no other promise could have occurred | Idris controls the stated communication step, while delivery, compensation, and the full history remain unresolved.
What should happen if other evidence exists? | Preserve and review it through the appropriate process. | Ignore it because the available note is enough to settle every issue. | Alter the original note to match the new account. | Treat it as automatic permission for Idris to approve compensation. | Additional records may matter and should be reviewed without changing history or assuming new authority.''',
    vocabulary='''expectation gap | A difference between what someone expected and what is currently understood or available. | address the expectation gap
conditional estimate | A forecast dependent on stated assumptions or events. | explain a conditional estimate
confirmed commitment | An undertaking established through the relevant authorized process. | verify a confirmed commitment
qualification | Wording that limits or conditions a statement. | preserve the qualification
delivery status | The current state of work toward making a capability available. | verify delivery status
disputed record | Information whose meaning, completeness, or accuracy is challenged. | reconcile a disputed record
contemporaneous note | A note made at or near the time of the relevant event. | preserve contemporaneous notes
supporting evidence | Information that helps assess a claim or account. | request supporting evidence
acknowledgment | Recognition of a concern or impact without necessarily accepting every claim. | give a clear acknowledgment
service recovery | Work to address a service problem and rebuild trust. | coordinate service recovery
complaint escalation | Routing a complaint to the appropriate reviewer or authority. | arrange complaint escalation
review owner | The person responsible for coordinating an assessment. | identify the review owner
compensation request | A request for money, credit, or another remedy. | route a compensation request
commercial authority | Permission to make specified business decisions or commitments. | confirm commercial authority
resolution path | The route for assessing and addressing an issue. | explain the resolution path
boundary | A stated limit on conduct or participation. | set a respectful boundary
personal insult | A demeaning remark directed at a person rather than the work or issue. | address personal insults
de-escalation | Communication aimed at reducing tension while addressing the issue. | use de-escalation language
pause | A temporary interruption with its purpose and next route clarified. | explain a call pause
continuity of support | Maintaining an appropriate way to receive assistance. | preserve continuity of support
factual chronology | A time-ordered account of events and evidence. | compile a factual chronology
read-back | Repeating key points so another person can confirm or correct them. | give a closing read-back
follow-through | Completing and communicating agreed actions. | demonstrate follow-through
trust repair | Rebuilding confidence through accurate communication and reliable action. | support trust repair''',
    precision='Targeting late October, subject to testing is conditional wording. It does not establish the requested 31 October commitment in the available note. That distinction does not prove that no other conversation or document exists, or determine any contractual remedy.',
    precision_extra='Acknowledging disruption does not require agreeing to an unverified date or compensation. A conduct boundary addresses behavior, not the legitimacy of the complaint. If a pause is needed under the stated procedure, explain the continuing support route and next contact.',
    phrases='''Acknowledge the effect | I understand that your team planned around an October expectation.
Invite the evidence | Please share the message or meeting record you relied on.
State the available wording | The note says late October, subject to testing.
Keep the record qualified | I have not yet reviewed every relevant communication.
Avoid a blanket denial | I am not saying that no other conversation occurred.
Separate the date | I cannot confirm the thirty-first of October from the information available.
Take ownership of review | I will arrange the manager review and preserve the records you provide.
Set the next update | I will update you by Thursday at fifteen hundred UTC.
Avoid promising the result | That update may report that the review is still pending.
Route the remedy request | I can record your compensation request, but I cannot approve it.
Accept direct criticism | You can challenge our handling of the issue.
Name the conduct boundary | I want to continue helping; please keep comments focused on the issue rather than personal insults.
Explain a possible pause | If the personal insults continue, we will pause this call and use the agreed support route.
Keep support available | The complaint will remain open through that route.
Confirm the read-back | Your concern is the missed expectation, the operational impact, and the requested review.
Close with follow-through | I will send the factual summary, the review owner, and the promised update time.''',
    notes='''Planned around | Acknowledges reliance and impact without deciding an unreviewed legal claim.
Available | Limits the statement to the information currently checked.
Not saying | Corrects an overly broad interpretation without retreating from the verified wording.
May report pending | Prevents the update time from becoming an implied resolution deadline.
Focused on the issue | Defines a behavior boundary while leaving criticism and complaint available.
Remain open | Preserves the route for legitimate review after a pause.''',
    d='''Which response addresses the disputed promise accurately? | The available note is conditional; let us review any other records you relied on. | No other promise could possibly have been made. | An estimate automatically becomes a confirmed release date. | The customer's frustration proves delivery was guaranteed. | The response distinguishes the available wording from the incomplete history without inventing certainty in either direction.
Which statement preserves a useful communication commitment? | I will update you by Thursday at 15:00 UTC, even if review is still pending. | I guarantee the requested feature and compensation by that time. | I will respond only after the customer stops disagreeing. | The meeting time itself confirms a favorable decision. | Idris can commit to communication without promising a delivery or compensation outcome outside his authority.
Which behavior alone does not justify treating the customer as abusive? | Firmly disputing the record and requesting accountability | Repeated personal insults after a clear boundary | Demeaning comments directed at the employee | Continuing personal attacks instead of discussing the issue | Direct criticism and a substantive complaint are not equivalent to personal abuse.
If the stated procedure requires a pause, what should Idris preserve? | A clear support route, complaint record, owner, and next contact | A threat to erase the complaint | An unapproved credit in exchange for silence | A claim that the original concern is now invalid | A conduct pause should not remove appropriate support or prevent review of the underlying concern.''',
    dialogue='''Beth | We planned around an October release. Now I am hearing uncertainty. I need you to confirm the thirty-first so our team knows where it stands.
Idris | I understand the [[expectation gap::The expectation gap concerns the October timing Beth relied on versus the conditional status currently documented.]] and the disruption. I cannot confirm that date, but I want to review exactly what your team was told.
Beth | The discussion was much more definite than that. I do not want you to use one note to dismiss everything we heard.
Idris | I will not. The available note records a [[conditional estimate::The note targets late October subject to testing, which is conditional rather than a confirmed release date.]] for late October, subject to testing. That is different from a confirmed date, but it does not establish that no other conversation or document exists.
Beth | I may have a presentation from the earlier meeting. I will send it through the customer support channel.
Idris | Please do. We will preserve that [[supporting evidence::Additional messages or presentations may clarify the history and should be preserved for review rather than dismissed.]] alongside the note and review the full context. I do not want either of us to rely on a selective quotation or an incomplete sequence.
Beth | We have spent time preparing for this. I also want a credit, not just another explanation of your process.
Idris | I can record the [[compensation request::Idris can route the requested credit for review but does not hold authority to approve compensation.]] and its basis for the authorized reviewer. I cannot approve a credit or promise the result, but your reported impact belongs in the review.
Beth | This is infuriating. Your team has handled it badly, and I want someone senior to take responsibility.
Idris | You can challenge our handling. I will arrange a [[complaint escalation::Complaint escalation sends the substantive concern to an appropriate reviewer; direct criticism is not itself abusive conduct.]] to a manager and identify who owns the review. I remain responsible for making sure you receive the update I promise.
Beth | You are useless if all you can do is repeat that you cannot commit. Why should I keep talking to you?
Idris | I want to continue helping, and I need to set a [[boundary::The boundary addresses personal insults while keeping the customer's underlying complaint and right to challenge the service intact.]] here: please keep comments focused on the issue rather than personal insults. We can discuss the impact, the records, and the review without directing remarks at each other.
Beth | Fine. My concern is that nobody has taken ownership. What will actually happen next, and when will I hear from you?
Idris | I will confirm the [[review owner::The review owner coordinates assessment of the records and request; identifying that person does not predetermine the result.]] and update you by Thursday at fifteen hundred UTC. That update may say the assessment is still pending, but I will not leave you waiting without the promised contact.
Beth | I can accept a status update if you do not present it as the issue being resolved. The date and our preparation costs still need review.
Idris | Agreed. The [[resolution path::The resolution path covers assessment and follow-up; a scheduled status message is not a completed remedy or release commitment.]] remains open. If personal insults resume, our procedure allows a pause with a clear continuing support route, not deletion of the complaint or abandonment of the review.
Beth | Then summarize what you have understood so I can correct anything before the manager sees it.
Idris | Here is the [[read-back::The read-back checks the concern, impact, disputed evidence, and requested review with the customer before the handoff.]]: your team relied on an October expectation, incurred preparation effort, and wants the communication history, delivery status, and credit request reviewed. The available note is conditional, and you may provide another record.
Beth | That captures it. I will send the presentation, and I expect the Thursday update even if the answer is not final.
Idris | You will receive it. [[Trust repair::Trust repair depends on accurate review and reliable follow-through, not an unsupported promise made to end tension.]] starts with follow-through. I will send the summary, confirm the owner, and keep the agreed contact time.''',
    transfer_title='Respond to another disputed delivery expectation',
    transfer_setup='A note describes a November target subject to testing. Customer Dena requests a confirmed 30 November date and a credit. Manager Vik cannot approve either. He can route additional evidence for review and update Dena on Tuesday at 09:00 UTC.',
    transfer='''Manager: "The documented timing is a ___." | conditional target | The testing qualification prevents the available note from establishing an unconditional date.
Customer: "My additional messages should be sent for ___." | review | Further records may clarify the history and should not be dismissed or treated as automatic approval.
Manager: "I cannot approve the requested ___." | credit | Vik lacks compensation authority even though he can record and route the request.
Customer: "The next status update is Tuesday at ___." | 09:00 UTC | The stated appointment is for communication, not a guaranteed delivery or compensation decision.''',
))
