"""Post-close cross-border integration English: continuity, people, systems, and value."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='cross-border-ma-integration', title='Cross-Border M&A Integration English',
    balanced_answer_columns=True,
    category='Business & professional services', cover_label='ENGLISH FOR POST-ACQUISITION INTEGRATION',
    cover_title='Cross-Border M&A Integration', cover_size=26,
    tagline='Keep the business running while the organizations come together.',
    audience='For integration consultants, workstream leaders, and international managers coordinating the post-acquisition integration of US businesses.',
    roles='M&A integration consultants, integration managers, workstream leads, post-acquisition specialists',
    summary='Practical post-acquisition English for Day 1 continuity, decision rights, workplace norms, HR differences, IT cutovers, customer communications, synergy tracking, and operational handover.',
    map_intro='Eight post-close situations follow an international integration team working with a US business. The focus is operating the combined organization, not negotiating the acquisition price or treating national cultures as fixed personalities.',
    notes_title='Ownership changes faster than operating habits.',
    notes_intro='After closing, consultants need to coordinate decisions without assuming that legal ownership instantly merges systems, contracts, policies, or trust. Clear English makes dependencies and authority visible while keeping customers and employees informed.',
    field_notes=[
        ('Separate closing from integration', 'A completed acquisition does not mean every system, process, or contract has moved. Day 1 continuity and the target operating model are different milestones.', '"The transaction has closed; payroll is continuing on the existing approved process."'),
        ('Ask about local practice', 'Teams may differ in how they challenge proposals, seek agreement, or escalate problems. Describe the observed practice rather than explaining it through nationality.', '"Does silence here mean agreement, or do we need an explicit decision?"'),
        ('Keep authority specific', 'A sponsor endorsement, consultant recommendation, and authorized operational decision can be different steps. Name the actual decision owner and required reviews.', '"The sponsor supports the objective; the process change still needs the stated approval."'),
        ('Report value on a defined basis', 'An annualized saving, an in-period result, and a forecast are different measures. Agree a baseline and avoid counting the same benefit in two workstreams.', '"That is the run rate; the realized quarterly amount is reported separately."')],
    scope_note=FICTION + 'Professional English practice, not legal, employment, tax, accounting, cybersecurity, or transaction advice. All decision matrices, service arrangements, dates, and approval rules in the cases are fictional. Actual integration must follow the transaction documents, current law, employment and privacy requirements, customer obligations, authorized controls, and qualified local advice. No exercise authorizes a policy change, access grant, payment change, system cutover, or workforce decision. Organizational differences are not claims about every person from a country.',
    sources=[
        source('Deloitte. Integrated asset management and integration management office functions.', 'https://www.deloitte.com/us/en/services/consulting/content/integrated-asset-management.html', 'First-party practice context for Day 1 readiness, workstream coordination, transition services, and synergy tracking; the cases and figures are original.'),
        source('US Department of Labor. Fact Sheet 17A.', 'https://www.dol.gov/agencies/whd/fact-sheets/17a-overtime', 'Supports the distinction between a job title and actual exemption requirements. No salary threshold or classification determination is taught here.'),
        source('NIST. Cybersecurity Framework 2.0.', 'https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20', 'Risk-governance and authorized-access context, not a prescriptive technical cutover procedure.'),
        source('FBI. Business email compromise.', 'https://www.fbi.gov/how-we-can-help-you/common-frauds-and-scams/business-email-compromise', 'Supports independent verification of payment changes rather than relying on an apparent acquisition-related email alone.')], units=[])

BOOK['units'].append(unit(
    title='Protecting Day 1 business continuity', scene='The deal closed; the payroll process did not move overnight',
    skill='Separate legal closing, immediate operating needs, and later integration milestones.',
    brief='An overseas buyer completed the acquisition of a fictional US business on Friday. On Monday, employees must be able to enter the site, receive support, and follow the existing approved payroll process. The shared HR platform is not ready, and no immediate payroll migration is authorized. Integration consultant Aya and US operations lead Marcus prioritize continuity and identify the later migration work separately.',
    cast='Aya | Integration consultant\nMarcus | US operations lead',
    culture=('Continuity is a deliberate first-day result', 'A familiar process continuing after closing is not necessarily resistance. Ask which changes are required now and which depend on later readiness.'),
    a='''What has been completed? | Legal acquisition closing | Full HR-platform integration | An authorized payroll migration | Every future operating-model change | The transaction closed Friday, while the shared platform remains unready.
Which process continues under the supplied plan? | The existing approved payroll process | An unapproved new payroll platform | A temporary employee-funded payroll workaround | No payroll process at all | The brief explicitly retains the existing approved payroll process for continuity.
What should be separated from Monday continuity? | The later platform migration | Site access and support availability | The fact of the completed closing | Employee questions about immediate operations | The migration is later work with readiness and authorization still outstanding.''',
    vocabulary='''legal close | Completion of the transaction under its actual closing requirements. | confirm legal close
Day 1 readiness | Preparedness for required operations immediately after closing. | assess Day 1 readiness
business continuity | Ability to sustain required operations through change or disruption. | protect business continuity
integration management office | Team coordinating integration governance and workstreams. | establish the integration management office
workstream | Defined area of coordinated integration work. | lead the HR workstream
critical service | Service whose interruption materially affects required operations. | identify critical services
minimum operating requirement | Condition needed for the specified operation to function. | define minimum operating requirements
transition service agreement | Contract for specified temporary support during a transition. | review the transition service agreement
standalone capability | Ability to perform a function without the temporary support being replaced. | establish standalone capability
interim operating model | Temporary arrangement used during transition. | document the interim operating model
target operating model | Intended future arrangement of roles, processes, and systems. | define the target operating model
readiness checkpoint | Defined review of whether prerequisites are met. | hold a readiness checkpoint
dependency | Requirement or preceding activity on which another task relies. | map the dependency
continuity owner | Person accountable for keeping a specified operation functioning. | name the continuity owner
hypercare | Time-limited heightened support after a transition. | plan hypercare coverage
service desk | Contact function handling user support requests. | brief the service desk
critical-path item | Task whose timing can constrain the overall sequence. | identify a critical-path item
Day 100 milestone | Stated later integration target, not a universal legal deadline. | review the Day 100 milestone''',
    precision='Legal close and completed integration are different. The supplied Monday plan preserves the existing payroll process; it does not authorize immediate migration.',
    precision_extra='Day 1 and Day 100 are planning labels whose actual scope depends on the deal and operating plan. They do not create universal deadlines or permissions.',
    phrases='''Separate milestones | Closing is complete; platform integration is not.
Prioritize continuity | Which services must work when employees arrive on Monday?
Preserve the current plan | Payroll remains on the existing approved process.
Identify dependency | Migration depends on readiness checks and the required authorization.
Name responsibility | Who owns continuity if the new platform is delayed?
Explain the interim state | This is the temporary operating arrangement, not the final design.
Keep support visible | Employees need one clear support route for the transition.
Report accurately | We are ready for the stated Day 1 scope, not every future integration change.''',
    notes='''Closed versus integrated | Closed refers to the completed transaction; integrated refers to the actual operational work.
Continue versus freeze forever | Continue preserves the current approved process now without promising it will never change.
Ready for what | Ready needs a defined scope; one functioning service does not establish readiness for every migration.''',
    d='''Which Monday message is supported? | Payroll continues under the existing approved process | Every employee moves to the new platform immediately | All policies changed automatically at closing | Integration is complete because ownership changed | The brief explicitly retains the current payroll process while the new platform is unready.
Which question identifies continuity responsibility? | Who owns payroll operation during the transition? | Which logo should be larger? | Can we assume the buyer handles every detail? | Does legal close erase the need for support? | A named operational owner is needed rather than an assumption from corporate ownership.
What should a readiness statement include? | The specific services and scope checked | Only a green color without definition | A promise that every future change is complete | A claim that no dependency can delay work | Readiness has meaning only in relation to stated requirements and evidence.
Which action is not authorized by the case? | Migrating payroll immediately | Keeping the support route clear | Recording the platform dependency | Identifying the continuity owner | The brief expressly says no immediate payroll migration is authorized.''',
    dialogue='''Aya | The acquisition closed on Friday. Headquarters would like Monday's message to say that everyone is now fully integrated.
Marcus | We should separate [[legal close::Legal close confirms the completed transaction but does not establish that operational systems and processes have been integrated.]] from the operating changes. Ownership changed, but the shared HR platform is not ready.
Aya | Then the first question is what must function when employees arrive, rather than how many new processes we can announce.
Marcus | Exactly. [[Day 1 readiness::Day 1 readiness concerns the specified immediate operating requirements rather than completion of the entire future integration plan.]] means site access, support, and the approved payroll process work within the agreed immediate scope.
Aya | Payroll currently runs through the existing approved process. No one has authorized moving it to the new platform this week.
Marcus | Keep that [[business continuity::Business continuity preserves required operations through the transition instead of making an unready migration a symbolic sign of progress.]] message explicit. Employees should not infer a pay-process change from a new ownership announcement.
Aya | Some colleagues may see the old process continuing as a sign that the local team is resisting the acquisition.
Marcus | It is our [[interim operating model::The interim operating model is the deliberate temporary arrangement used while later integration prerequisites remain unresolved.]], not a statement that the organization will never change. Explain its purpose and limits.
Aya | The later migration still matters, but we need to identify the testing, data, access, and approval work before scheduling it.
Marcus | Put those items in the [[dependency::A dependency identifies a prerequisite for the later migration and prevents the task from being scheduled as though readiness already exists.]] map so the schedule reflects what actually has to happen first.
Aya | Who should coordinate those items across HR, IT, finance, and the local business without taking over every operational decision?
Marcus | The [[integration management office::The integration management office coordinates workstreams and governance but does not automatically replace every functional decision owner.]] can coordinate the workstreams while the actual functional owners retain their defined responsibilities.
Aya | We also need a named person responsible if employees cannot access the payroll support channel on Monday.
Marcus | Assign a [[continuity owner::The continuity owner is the named person responsible for sustaining the specified service during transition, not an assumed responsibility of the buyer in general.]] and an escalation route rather than leave responsibility attached only to a department name.
Aya | The service desk needs a clear briefing on what changes now, what stays the same, and where to route unanswered questions.
Marcus | Yes. The [[service desk::The service desk provides the user support route and needs accurate transition information rather than an overbroad claim that every system has changed.]] should not tell employees to use a platform that has not been released or supported.
Aya | Before the later migration, we can review the actual evidence that the required tests and authorizations are complete.
Marcus | That is the purpose of a [[readiness checkpoint::A readiness checkpoint reviews the stated prerequisites and evidence before the relevant transition rather than substituting a calendar date for readiness.]]. A target date should not substitute for verified readiness.
Aya | I will revise the message: the transaction has closed, immediate operations continue under the stated plan, and migration work remains scheduled for review.
Marcus | Good. The [[target operating model::The target operating model describes the intended future arrangement, which must remain distinct from the current interim state and completed Day 1 scope.]] can remain our destination without being announced as a completed fact on the first working day.''',
    rehearsal=['Read the corrected exchange and distinguish closed, ready for Day 1, interim, and fully integrated.', 'Switch roles and deliver the Monday message without announcing an unauthorized payroll change.'],
    transfer_title='The logo changed before the support route', transfer_setup='The employee portal has new branding, but the approved support process remains unchanged. The shared support platform has not launched.',
    transfer='''Employee: "The branding has ___." | changed | The portal appearance has changed, but that does not establish a new operating process.
Consultant: "The approved support route remains ___." | unchanged | The brief explicitly retains the existing support process.
Employee: "The shared platform has not ___." | launched | The new platform is not yet in operation in the supplied case.
Consultant: "Use the current approved ___." | process | Employees should follow the actual operating arrangement rather than infer a change from branding.'''))

BOOK['units'].append(unit(
    title='Clarifying integration decision rights', scene='Sponsor support is not process-change authorization',
    skill='Separate coordination, consultation, and approval when a workstream decision crosses functions.',
    brief='A global sponsor supports standardizing customer credit terms. The fictional integration decision matrix requires finance ownership, local legal consultation, and steering-committee approval before the US process changes. Consultant Leo coordinates the proposal but cannot approve it. The sales workstream asks to implement immediately because the sponsor liked the concept. None of the required decision steps has been completed.',
    cast='Leo | Integration consultant\nPriya | Sales workstream lead',
    culture=('Ask who decides without sounding territorial', 'Decision clarity prevents duplicate instructions and premature implementation. A consultant can keep momentum while respecting the actual approval route.'),
    a='''What did the sponsor provide? | Support for the standardization concept | Completed steering approval | Local legal review | Authorization from every process owner | The brief identifies conceptual support, not the required completed decision steps.
Who coordinates but cannot approve the change? | Leo | The steering committee under the supplied matrix | The authorized finance owner | The local legal reviewer | Leo's stated role is coordination, without process-change approval authority.
Which sequence is required before implementation here? | Finance ownership, local legal consultation, and steering approval | Sales preference alone | Sponsor enthusiasm alone | A new slide title | The fictional decision matrix explicitly requires these roles and approval steps.''',
    vocabulary='''decision rights | Defined authority over specified decisions. | clarify decision rights
governance charter | Document defining the program's governance arrangements. | review the governance charter
steering committee | Body directing specified program decisions under its mandate. | seek steering-committee approval
executive sponsor | Senior supporter accountable for the initiative under the defined role. | brief the executive sponsor
process owner | Person accountable for a defined operational process. | confirm the process owner
RACI matrix | Responsibility map distinguishing responsible, accountable, consulted, and informed roles. | use the RACI matrix
accountable role | Role answerable for the specified outcome under the actual matrix. | identify the accountable role
consulted stakeholder | Person whose input is sought under the stated process. | involve consulted stakeholders
informed stakeholder | Person kept updated without necessarily making the decision. | notify informed stakeholders
approval gate | Point requiring the specified authorization before proceeding. | complete the approval gate
escalation path | Route for raising unresolved issues to the appropriate authority. | use the escalation path
decision log | Record of decisions, rationale, authority, and conditions. | update the decision log
issue log | Record of current problems needing resolution. | maintain the issue log
RAID log | Program record of risks, assumptions, issues, and dependencies under the stated convention. | reconcile the RAID log
change request | Formal proposal to alter an agreed scope, process, or plan. | submit a change request
delegated authority | Decision power specifically granted to another role. | verify delegated authority
cross-functional dependency | Requirement linking work across functional teams. | resolve cross-functional dependencies
decision latency | Time between raising a decision need and resolving it. | reduce decision latency''',
    precision='The sponsor supports the objective. Under the supplied matrix, finance ownership, local legal consultation, and steering approval are still required before implementation.',
    precision_extra='A RACI or similar matrix describes the actual chosen governance arrangement. Acronyms and role labels do not create legal or operational authority by themselves.',
    phrases='''Separate support and approval | The sponsor supports the concept; the process change is not yet authorized.
Name the owner | Finance owns this process under the agreed matrix.
Invite the right review | Local legal input is required before the decision.
Define your role | I can coordinate the proposal, but I cannot approve it.
Keep momentum | Let us name the decision owner and the information needed.
Use the escalation route | If the decision is delayed, we escalate through the stated path.
Record the condition | The decision log must retain any conditions attached to approval.
Prevent duplicate instructions | We need one authorized instruction for the affected teams.''',
    notes='''Consulted versus approving | Consultation provides input; approval exercises the specified decision authority.
Supports versus authorizes | Supports expresses endorsement; authorizes permits the relevant action within the actual role.
Responsible for coordinating | Coordination can move work forward without conferring authority to make every underlying decision.''',
    d='''Which response preserves momentum and governance? | Coordinate the required reviews and decision request | Implement because the sponsor smiled at the slide | Let each workstream choose its own terms | Record approval before anyone decides | This choice advances the proposal while respecting the supplied approval route.
Which statement accurately describes Leo's role? | He coordinates the proposal without approving it | He may override the decision matrix | He replaces local legal counsel | He alone changes customer contracts | The case explicitly gives Leo coordination responsibility but not approval authority.
What belongs in a decision log? | Actual decision, authority, rationale, and conditions | Only a positive color | A proposed outcome labeled complete | An unsupported claim that silence means consent | A decision record needs the actual outcome and its limits rather than shorthand that invents authorization.
What should happen if a required decision is delayed? | Use the stated escalation path | Treat delay as automatic approval | Bypass every reviewer | Ask employees to infer a policy | Delay should be addressed through the agreed governance, not converted into permission.''',
    dialogue='''Priya | The sponsor liked our standard credit-terms proposal. Sales wants to start using it in the US business tomorrow.
Leo | We need to distinguish support from [[decision rights::Decision rights identify who can authorize the actual process change, which is not established solely by a sponsor's favorable reaction.]]. The agreed matrix still requires finance ownership, local legal input, and steering approval.
Priya | The sponsor is senior, so I assumed the positive reaction replaced the remaining steps.
Leo | The [[executive sponsor::The executive sponsor supports the initiative under the defined role but does not automatically override every specific approval route in the supplied governance.]] supports the objective, but we have not received an instruction changing the stated approval route.
Priya | Finance needs to assess collection risk and how the proposed terms affect the current customer process.
Leo | Yes. Finance is the [[process owner::The process owner has the defined accountability for the affected operation and must be involved rather than bypassed by a workstream preference.]] under this matrix, rather than merely a team we inform after implementation.
Priya | Local legal counsel also needs to check the actual customer arrangements before we assume the global wording can be used unchanged.
Leo | That is the required [[consulted stakeholder::A consulted stakeholder supplies the specified input before the decision, which is distinct from merely receiving a notice afterward.]] role here. Consultation is not optional simply because the desired outcome is familiar.
Priya | What can you decide as the integration consultant, and what needs to stay with the functional and steering roles?
Leo | I can coordinate the [[change request::The change request records the proposed alteration for review and decision; preparing it does not itself approve the change.]], assemble the dependencies, and track the decision. I cannot approve this process change myself.
Priya | We need a clear request with the proposed scope, affected customers, risks, and the question the committee must answer.
Leo | That will make the [[approval gate::The approval gate requires the stated authorization before implementation and should receive a specific decision-ready proposal.]] more useful than sending a general slide and hoping everyone interprets the next step the same way.
Priya | If a reviewer does not respond quickly, sales still needs a way to raise the timing risk.
Leo | Use the agreed [[escalation path::The escalation path raises a delayed issue to the appropriate authority without converting silence into approval or bypassing the process.]]. We can escalate the delay without treating silence as consent.
Priya | The sales and finance leads should not send conflicting instructions to the US team while the decision remains open.
Leo | Correct. The [[cross-functional dependency::The cross-functional dependency links sales implementation with finance and legal review, so separate unilateral instructions could create an inconsistent process.]] needs one coordinated status and an eventual authorized instruction.
Priya | Once the committee decides, we should record exactly what was approved and any conditions, rather than only marking the slide green.
Leo | Put that in the [[decision log::The decision log preserves the actual decision, authority, and conditions instead of replacing them with a color or an anticipated outcome.]], along with the owner responsible for communicating and implementing the authorized change.
Priya | I will tell sales that the concept is supported and the required review and approval are still outstanding.
Leo | Good. That reduces confusion about [[delegated authority::Delegated authority is the specific power actually granted, which must not be inferred from coordinating a proposal or receiving an encouraging response.]] while keeping the proposal moving through the people who can properly decide it.''',
    rehearsal=['Read the corrected exchange and distinguish supports, consults, coordinates, and approves.', 'Switch roles and state the supplied decision sequence without inventing delegated authority.'],
    transfer_title='Consultation was recorded as approval', transfer_setup='Local legal counsel provides comments on a proposal. The steering committee has not decided. A status slide incorrectly says approved.',
    transfer='''Lead: "Legal has provided ___." | comments | The supplied event is consultation input, not the steering decision.
Consultant: "Steering approval remains ___." | outstanding | The required decision has not yet occurred in the case.
Lead: "The status label overstated the ___." | authority | It treated a consulted role's input as the approval assigned elsewhere.
Consultant: "Correct the decision ___." | record | The record should preserve the actual input and unresolved approval status.'''))

BOOK['units'].append(unit(
    title='Turning blunt disagreement into a workable decision', scene='That timeline will not work is a request to test the plan',
    skill='Respond to direct challenge, identify the underlying constraint, and establish a shared discussion norm.',
    brief='In the acquired US team, operations lead Jordan says the proposed Tuesday supplier cutover will not work because quality approval is still outstanding. Integration consultant Lina initially hears the direct objection as rejection of headquarters. Their previous organizations used different meeting habits. The actual issue is an uncompleted approval, not established hostility. They need explicit agreement and a clear boundary against personal attacks.',
    cast='Jordan | US operations lead\nLina | Integration consultant',
    culture=('Interpret the specific exchange, not a nationality', 'Some teams test a proposal aloud; others expect concerns to be resolved before a meeting. Ask what the speaker means and what evidence supports the objection. Directness does not excuse personal abuse.'),
    a='''What concrete constraint does Jordan identify? | Quality approval is outstanding | Headquarters has no legal ownership | The supplier has already failed every test | The local team refuses every change | The brief identifies an uncompleted quality approval as the reason the Tuesday plan is challenged.
What is not established by the direct objection? | Hostile intent toward headquarters | A challenge to the timeline | An unresolved approval | A difference in meeting habits | The case explicitly does not establish hostility from the direct wording.
What should the team make explicit? | The concern, decision status, and discussion boundary | A rule that silence always means approval | A national stereotype about every employee | Permission to attack colleagues personally | The task requires a shared understanding of the issue and respectful challenge, not assumptions about silence or identity.''',
    vocabulary='''working norm | Agreed way a team conducts recurring work. | establish working norms
challenge protocol | Agreed method for questioning proposals or assumptions. | define a challenge protocol
constructive dissent | Reasoned disagreement intended to improve a decision. | invite constructive dissent
psychological safety | Ability to raise questions or concerns without inappropriate interpersonal punishment. | support psychological safety
face-saving language | Wording that preserves dignity while addressing a difficult point. | use face-saving language
intent clarification | Question checking what a speaker means or aims to do. | seek intent clarification
impact statement | Description of how an action or message affects the work. | make an impact statement
decision norm | Shared expectation for how agreement and decisions are established. | clarify the decision norm
explicit agreement | Clearly stated acceptance rather than inferred assent. | obtain explicit agreement
tacit assumption | Unspoken premise influencing interpretation or action. | surface a tacit assumption
local constraint | Requirement or limitation affecting the local operation. | identify a local constraint
integration friction | Difficulty arising as organizations combine practices and expectations. | address integration friction
shared vocabulary | Agreed meanings for recurring terms across teams. | establish a shared vocabulary
pre-read | Material circulated before a meeting for preparation. | circulate a focused pre-read
disagreement boundary | Limit separating legitimate challenge from personal attack or misconduct. | state the disagreement boundary
repair statement | Wording correcting a misunderstanding or relational impact. | offer a repair statement
alignment check | Explicit test of whether participants share the same understanding. | conduct an alignment check
meeting closeout | Final confirmation of decisions, open issues, and actions. | complete the meeting closeout''',
    precision='Jordan challenges the Tuesday cutover because quality approval is outstanding. That does not establish opposition to the acquisition or personal hostility.',
    precision_extra='Do not excuse harassment or personal attacks as culture. Clarify meaning, require evidence, and maintain the actual workplace conduct standards.',
    phrases='''Invite the constraint | Which part of the Tuesday plan will fail, and why?
Clarify intent | Are you challenging the date or the overall integration goal?
Respond firmly | We can challenge the proposal without attacking the people who prepared it.
Preserve dignity | I may have read your direct wording differently than you intended.
Name the blocker | Quality approval is still outstanding.
Separate support and readiness | We support the goal, but this dependency is unresolved.
Check agreement | Please state whether you agree with the next step or have a remaining objection.
Close precisely | We have agreed to resolve the approval issue, not to proceed Tuesday regardless.''',
    notes='''Will not work versus will not cooperate | The first can challenge feasibility; the second states refusal. Do not substitute one meaning without checking.
Silence versus consent | Silence may have several meanings. Use the actual decision process and seek explicit agreement where needed.
Direct versus disrespectful | Direct language can be task-focused; personal attacks or discriminatory conduct are a different issue.''',
    d='''Which response best clarifies the objection? | Is the issue the Tuesday date or the integration goal? | Why does your whole country resist change? | Your objection proves disloyalty | We should proceed because the wording was blunt | This response checks the meaning without stereotyping or ignoring the stated constraint.
Which sentence protects the discussion boundary? | Challenge the plan with evidence, not the people | Every insult is acceptable if it is direct | Local staff may never disagree publicly | Headquarters proposals cannot be questioned | Task-focused challenge can be firm while personal attacks remain outside the agreed conduct boundary.
What should replace inferred consent? | A clear statement of agreement or remaining objection | A guess based on who stayed quiet | A national assumption about politeness | A positive slide color with no decision | Explicit responses make the actual agreement visible rather than relying on ambiguous silence.
Which closeout matches the facts? | Resolve quality approval before deciding the cutover | Proceed Tuesday regardless of approval | Cancel the acquisition because of one objection | Record unanimous readiness despite the blocker | The actual unresolved approval must remain part of the cutover decision.''',
    dialogue='''Jordan | That Tuesday cutover will not work. We still do not have quality approval, and the schedule treats it as complete.
Lina | I want to check your meaning. Is this [[constructive dissent::Constructive dissent challenges the feasibility or reasoning of a proposal to improve the decision, rather than automatically rejecting the integration goal.]] about the date, or are you objecting to the integration goal itself?
Jordan | The date is the problem. I support the change, but the local quality team has not approved the supplier transition.
Lina | Then the [[local constraint::The local constraint is the outstanding quality approval that limits the proposed cutover, not a general unwillingness to cooperate.]] needs to be visible. I initially heard the direct wording as a rejection of headquarters.
Jordan | In our previous meetings, we tested proposals aloud. A strong objection to a plan was not meant as an attack on its author.
Lina | Our earlier [[working norm::A working norm describes a team's actual meeting practice and should not be generalized into a fixed national personality.]] was to resolve most objections before the meeting, so the same wording landed differently for me.
Jordan | We can adapt without making people hide a real blocker. I would rather explain the approval gap than let the schedule fail.
Lina | Agreed. Let us use a [[challenge protocol::A challenge protocol sets a practical way to state the concern, evidence, and decision needed while preserving room for firm disagreement.]]: name the issue, explain the evidence, and identify what decision or action is needed.
Jordan | That would also help distinguish a specific objection from a vague statement that everything about the integration is wrong.
Lina | Yes, and we need a [[disagreement boundary::The disagreement boundary permits evidence-based challenge while excluding personal attacks or other inappropriate conduct.]]. Challenge the proposal firmly, but do not attack the people or make assumptions about their competence or nationality.
Jordan | I can restate my point: the Tuesday plan depends on quality approval, which is still outstanding, so readiness is not established.
Lina | Thank you. My [[repair statement::A repair statement corrects a misunderstanding and acknowledges its impact without requiring either person to abandon the substantive issue.]] is that I read your intent too broadly. The constraint is legitimate, and we should address it directly.
Jordan | Some colleagues stayed silent after the first discussion. We should not assume that means they accepted the date.
Lina | Correct. We need [[explicit agreement::Explicit agreement makes the actual acceptance or remaining objection clear instead of inferring consent from silence.]] on the next action and the eventual decision, using the actual approval process.
Jordan | A short note before the next meeting could identify the pending approval, its owner, and the evidence needed to resolve it.
Lina | That [[pre-read::A pre-read gives participants the relevant information before the meeting and can reduce misunderstandings about the proposal and unresolved conditions.]] will help both teams prepare without requiring concerns to disappear before they can be discussed.
Jordan | We also use ready differently. Sales means the supplier is willing, while quality means the required approval is complete.
Lina | Then build a [[shared vocabulary::A shared vocabulary gives recurring status terms agreed meanings so different functions do not report incompatible states under the same word.]] around those statuses. A willing supplier and an approved transition are not the same thing.
Jordan | Our next step is to resolve the quality question and then decide the cutover through the proper authority.
Lina | I will record that in the [[meeting closeout::The meeting closeout confirms actual decisions and open issues, here resolving the approval gap rather than authorizing an unconditional Tuesday cutover.]]. We have aligned on the action, not agreed to proceed Tuesday regardless of readiness.''',
    rehearsal=['Read the corrected exchange and practice the intent clarification without adding a national stereotype.', 'Switch roles and state the blocker, evidence, owner question, and next decision using the supplied facts.'],
    transfer_title='Silence was recorded as approval', transfer_setup='A meeting ends without an explicit decision. Two participants remain silent. The required approval has not been given.',
    transfer='''Consultant: "Silence does not establish ___." | approval | The case supplies no explicit decision or required authorization.
Lead: "We need an explicit alignment ___." | check | A direct check can establish the participants' actual positions and unresolved concerns.
Consultant: "Any remaining objection should be ___." | stated | The team needs clear concerns rather than an assumption based on silence.
Lead: "The decision remains ___." | open | The required approval has not occurred in the supplied situation.'''))

BOOK['units'].append(unit(
    title='Handling HR differences without inventing assurances', scene='A new title does not determine overtime status',
    skill='Explain a proposed HR change while preserving local review, current instructions, and employee trust.',
    brief='The integration team proposes changing a US role title from operations coordinator to operations manager. A headquarters spreadsheet assumes the new title makes the role exempt from overtime. HR lead Denise has not completed the required review of actual duties, compensation, and applicable federal and state requirements. Consultant Ken must correct the assumption. No payroll-classification or benefits change has been approved, and the existing approved time-recording process remains in place.',
    cast='Ken | Integration consultant\nDenise | US HR lead',
    culture=('Consistent principles do not require identical local rules', 'Global titles and templates can aid coordination, but local employment requirements and actual role duties still matter. Give employees verified information instead of broad promises about future changes.'),
    a='''What change is proposed? | A role-title change | A completed legal exemption determination | An approved benefits reduction | A confirmed payroll reclassification | The brief identifies a proposed title change and leaves classification review incomplete.
Why is the spreadsheet assumption unsupported? | A job title alone does not determine exemption | Every manager title is automatically exempt | All salaried jobs are automatically exempt everywhere | Local requirements disappear after acquisition | The actual duties, compensation, and applicable requirements need review rather than a conclusion from the title.
What process currently remains in place? | Existing approved time recording | Automatic deletion of time records | An unapproved global payroll setting | No recording until review ends | The brief explicitly retains the current approved time-recording process.''',
    vocabulary='''job architecture | Framework organizing roles, levels, and titles. | align job architecture
role mapping | Comparison of jobs across organizational structures. | complete role mapping
job title | Label identifying a role without determining every legal status. | harmonize job titles
actual duties | Work genuinely performed in the role. | review actual duties
exempt classification | Status under specified legal pay requirements after the relevant assessment. | assess exempt classification
nonexempt classification | Status subject to the relevant applicable pay protections and requirements. | verify nonexempt classification
salary basis | Method of compensation relevant under certain legal tests. | review the salary basis
overtime eligibility | Entitlement under the actual applicable pay requirements. | assess overtime eligibility
timekeeping | Recording work time under the applicable process. | maintain accurate timekeeping
policy harmonization | Coordinating policies while respecting relevant differences and requirements. | plan policy harmonization
local-law review | Qualified assessment of requirements in the relevant jurisdiction. | obtain local-law review
benefits enrollment | Process of selecting or joining employee benefit arrangements. | coordinate benefits enrollment
paid time off | Leave entitlement or policy under the actual applicable terms. | clarify paid-time-off arrangements
employee communication | Message explaining relevant workplace information. | approve employee communications
retention concern | Risk that employees may leave or disengage during transition. | address retention concerns
consultation requirement | Obligation to seek input under the relevant law or process. | verify consultation requirements
personnel data | Information relating to employees and their employment. | protect personnel data
approved change notice | Authorized communication of an actual workplace change. | issue an approved change notice''',
    precision='A manager title does not by itself establish exempt status. The actual requirements and role facts need qualified review; no classification change is authorized here.',
    precision_extra='Do not infer a universal rule from one federal fact sheet. State and local requirements, actual duties, compensation, agreements, and institutional processes may matter. No threshold or employee classification is decided in this exercise.',
    phrases='''Challenge the assumption | The title change does not establish overtime status.
Request the facts | We need the actual duties and compensation information for the review.
Protect current instructions | Continue the existing approved time-recording process.
Separate workstreams | Title alignment and payroll classification are different decisions.
Avoid an unsupported promise | No change is approved at present; I cannot promise that nothing will ever change.
Route legal questions | The applicable requirements need qualified local review.
Limit data access | Share personnel information only through the authorized process.
Close the loop | Employees should receive an approved notice when an actual decision is made.''',
    notes='''Proposed versus effective | Proposed describes a possible change; effective identifies a change actually in force under the relevant process.
Title versus classification | A title is an organizational label; classification concerns the actual legal and policy assessment.
No change approved versus no change ever | The first reports current status; the second promises an unknown future outcome.''',
    d='''Which correction should be made to the spreadsheet? | Title mapping does not establish exempt status | Every operations manager must be exempt | Salary alone settles every case | Acquisition automatically replaces local requirements | The spreadsheet should separate the proposed title from the unresolved legal classification.
Which employee message is accurate? | No classification change is approved; follow current time recording | Stop recording time immediately | Your benefits can never change | The new title removes every overtime entitlement | The case retains the current approved process and supplies no authorized classification change.
What should HR examine? | Actual role facts and applicable requirements | Only the preferred global title | Only whether the spreadsheet cell is green | A rule from an unrelated country without review | Classification depends on the relevant facts and legal requirements rather than a naming preference.
How should personnel records be shared? | Through the authorized access and privacy process | With everyone on the integration mailing list | In an unrestricted public folder | As proof that ownership cancels privacy duties | Employee information still requires appropriate authority, controls, and applicable privacy handling.''',
    dialogue='''Ken | The global role map changes operations coordinator to operations manager. The spreadsheet automatically labels the new title exempt.
Denise | That assumption needs correction. A [[job title::A job title is an organizational label and does not by itself establish exemption from applicable overtime requirements.]] does not determine the applicable overtime classification.
Ken | The title mapping was intended to align levels across the group, not to complete a legal assessment of each US role.
Denise | Then keep [[job architecture::Job architecture organizes roles and levels but must remain distinct from the legal assessment of pay classification.]] separate from payroll classification in both the spreadsheet and the employee explanation.
Ken | What information does the proper review need before anyone changes the employee record or payroll setting?
Denise | We need the [[actual duties::Actual duties describe the work genuinely performed and are relevant to the qualified classification assessment rather than relying only on a title or generic template.]], compensation information, and applicable requirements, assessed through the authorized HR and legal process.
Ken | Being paid a salary also should not be treated as a universal shortcut to an exemption conclusion.
Denise | Correct. The [[salary basis::Salary basis is one potentially relevant compensation concept under applicable tests and does not replace the full requirements for a particular exemption.]] and other requirements must be reviewed in the actual context rather than assumed from one label.
Ken | I will remove the automatic conclusion and mark the classification field as awaiting the required review.
Denise | Good. No [[exempt classification::Exempt classification is a legal status requiring the applicable assessment, which has not been completed or approved in the supplied case.]] change has been approved here, and the title proposal should not be used as authorization to make one.
Ken | Employees have asked whether they should stop using the current time-recording process once the new organization chart appears.
Denise | Tell them to continue the approved [[timekeeping::Timekeeping remains on the existing approved process in the case and should not be stopped based on an unapproved title or classification assumption.]] process. A proposed chart does not cancel current instructions.
Ken | We also have different leave and benefits arrangements across the two organizations. The global template does not resolve those differences.
Denise | [[Policy harmonization::Policy harmonization coordinates workplace arrangements while retaining the local requirements and actual review needed for each proposed change.]] needs its own review, including relevant local requirements and any consultation or approval obligations.
Ken | The local-law questions should go to the qualified advisers rather than be answered from a general headquarters presentation.
Denise | Exactly. [[Local-law review::Local-law review assesses the actual jurisdiction-specific requirements and cannot be replaced by a global title convention or general presentation.]] is necessary before we make claims about what is required or permitted for these employees.
Ken | Some employees want reassurance that nothing about their work or benefits will ever change. I do not have authority to promise that.
Denise | Give an accurate [[employee communication::Employee communication should state verified current status and the actual process rather than promise an unknown future or announce an unapproved change.]]: no change is approved at present, and actual decisions will be communicated through the authorized process.
Ken | I will also make sure the role records and compensation details are shared only with the people authorized for the review.
Denise | Protect the [[personnel data::Personnel data requires appropriate access and privacy handling even after acquisition; common ownership does not imply unrestricted distribution.]]. The integration need does not justify sending sensitive employee information to every person on the program mailing list.''',
    rehearsal=['Read the corrected exchange and distinguish title alignment, legal classification, and payroll implementation.', 'Switch roles and give the current employee message without promising permanent unchanged terms.'],
    transfer_title='The organization chart was mistaken for a payroll instruction', transfer_setup='A proposed organization chart uses new titles. No payroll classification change is approved, and current timekeeping instructions remain effective.',
    transfer='''Employee: "The chart shows a proposed ___." | title | The chart changes the organizational label without deciding payroll classification.
HR: "The classification review remains ___." | incomplete | The scenario supplies no completed classification assessment or approval.
Employee: "I should continue the approved timekeeping ___." | process | The current approved recording instructions remain in effect.
HR: "An actual change needs the required ___." | authorization | A proposed chart does not itself authorize a payroll or classification change.'''))

BOOK['units'].append(unit(
    title='Running a cross-functional IT cutover conversation', scene='Successful login does not prove invoice posting works',
    skill='Explain a hidden system dependency and distinguish technical readiness from a go-live decision.',
    brief='The integration team has tested employee login to the new identity platform successfully. A scheduled invoice-posting job still uses a legacy service account and has not passed an end-to-end test on the new setup. IT lead Fatima and integration consultant Eric review the planned retirement of the legacy identity service. No go-live approval is supplied, and broad shared-administrator access is not an approved workaround.',
    cast='Eric | Integration consultant\nFatima | IT integration lead',
    culture=('Translate the dependency into business impact', 'A nontechnical sponsor needs to understand which business process could fail, not merely hear that an interface remains amber. Preserve the security controls while explaining the decision.'),
    a='''Which test has passed? | Employee login to the new identity platform | End-to-end invoice posting on the new setup | Complete retirement of every legacy account | Approval of shared-administrator access | The brief identifies a successful login test but leaves the invoice job unverified.
What dependency remains? | The invoice job uses a legacy service account | Every user lacks a new login | The acquired business has no invoices | The new platform is already retired | The scheduled job still depends on a legacy service identity.
Which action is not approved? | Broad shared-administrator access as a workaround | Explaining the dependency | Performing authorized readiness review | Identifying business impact | The case explicitly excludes broad shared-administrator access as an approved workaround.''',
    vocabulary='''cutover | Controlled transition from one operating setup to another. | plan the cutover
system migration | Transfer of applications, data, or operations to a different setup. | sequence the system migration
identity provider | Service managing authentication identity under the actual architecture. | verify identity-provider dependencies
single sign-on | Authentication arrangement allowing access across approved services. | test single sign-on
service account | Identity used by an application or automated process. | review service-account access
access entitlement | Permission assigned to a user or system identity. | validate access entitlements
least privilege | Limiting access to what is needed for the authorized task. | maintain least privilege
user acceptance testing | Business-user verification against agreed acceptance requirements. | complete user acceptance testing
end-to-end test | Test covering the relevant full process across connected components. | run an end-to-end test
reconciliation | Comparison confirming agreement between relevant records or outputs. | perform transaction reconciliation
cutover window | Planned period for the controlled transition. | confirm the cutover window
rollback plan | Approved method for returning to a prior workable state if needed. | validate the rollback plan
go/no-go decision | Explicit authorization to proceed or not proceed at a defined point. | make the go/no-go decision
change freeze | Defined restriction on changes during a sensitive period. | observe the change freeze
legacy dependency | Reliance on a component of the earlier setup. | identify the legacy dependency
interface mapping | Definition of how information moves between connected systems. | verify interface mapping
data integrity | Accuracy and consistency of data under the relevant process. | protect data integrity
segregation of duties | Separation of incompatible responsibilities under the control framework. | preserve segregation of duties''',
    precision='A passed employee-login test does not establish that the invoice job works. The legacy service-account dependency must be resolved and tested within the authorized plan.',
    precision_extra='This is a communication scenario, not a technical migration procedure. No access change, control bypass, legacy retirement, or go-live action is authorized by the exercise.',
    phrases='''Translate the risk | Employees can sign in, but invoice posting still depends on the old service.
Limit the status | Login testing passed; end-to-end business testing has not.
Name the dependency | The scheduled job still uses a legacy service account.
Preserve controls | We need an authorized fix, not broad shared-administrator access.
Define acceptance | Which business outputs must reconcile before signoff?
Clarify fallback | Who owns the approved rollback decision and process?
Separate date and permission | A scheduled window is not go-live authorization.
Close the decision | Report the unresolved dependency before the go/no-go review.''',
    notes='''Login works versus process works | Authentication success verifies one component, not every downstream business transaction.
Scheduled versus authorized | A calendar slot reserves time; authorization permits the actual change under the process.
Retire versus disable temporarily | These describe different operational actions whose scope and controls must be explicit.''',
    d='''Which sponsor update is accurate? | Login passed; invoice posting remains dependent on the legacy account | All systems are integrated | The scheduled window proves readiness | Shared administrator access has been approved | The supplied tests establish only login success while a business-process dependency remains.
What should an acceptance check include here? | The invoice job's end-to-end result and reconciliation | Only whether the new logo appears | Only an employee's successful password entry | A green slide with no transaction evidence | The relevant business workflow must be tested beyond authentication and its outputs checked.
Which response preserves control? | Resolve access through the authorized least-privilege process | Share one unrestricted administrator account | Remove every approval because the schedule is tight | Hide the dependency until after retirement | A legitimate fix needs appropriate access and review rather than a control bypass.
What is the status of the go-live decision? | Not supplied as approved | Automatically approved by the calendar | Completed by the login test alone | Delegated to every employee | The case provides no authorization to proceed with the cutover or legacy retirement.''',
    dialogue='''Eric | Employee login passed on the new platform. Can we tell the sponsor that the old identity service is ready to retire?
Fatima | Not yet. That [[single sign-on::Single sign-on testing verifies the stated authentication flow but does not establish that every automated business process works.]] test covers employee access, not every automated job using the existing environment.
Eric | The finance workstream mentioned that invoice posting runs on a schedule rather than through a person signing in.
Fatima | Correct. It still uses a legacy [[service account::A service account is the identity used by the automated invoice job, whose dependency remains distinct from successful employee login.]], and that dependency has not been resolved in the new setup.
Eric | If we retire the old identity service before addressing it, the business impact could be failed invoice posting.
Fatima | That is the [[legacy dependency::The legacy dependency is the job's reliance on the earlier identity setup, which must be addressed before assuming retirement is safe.]] the sponsor needs to understand in operational terms.
Eric | We need to test the actual invoice process from its start through the expected output, not just repeat the login test.
Fatima | Yes. The [[end-to-end test::An end-to-end test covers the full relevant workflow across connected components, including the automated posting process.]] must use the agreed requirements and authorized test arrangements.
Eric | Finance also needs to verify that the resulting records match the expected transactions and totals.
Fatima | Include that [[reconciliation::Reconciliation compares expected and resulting records or totals to establish whether the business process produced the required output.]] in the acceptance evidence. A job reporting success does not by itself prove that every output is correct.
Eric | Someone suggested sharing a broad administrator account until the integration team has more time to solve the issue.
Fatima | That is not approved. Maintain [[least privilege::Least privilege limits access to the authorized task and is not satisfied by broadly sharing an unrestricted administrator identity.]] and use the actual access-review process for an appropriate solution.
Eric | The cutover window is already in the calendar, but the remaining tests and approvals have not been completed.
Fatima | Then the [[go/no-go decision::The go/no-go decision is the explicit authorization based on readiness and controls, not a permission created by a calendar booking.]] remains separate from the scheduled window. We must report the unresolved facts before that review.
Eric | We should also know what happens if the approved transition starts and the business checks fail.
Fatima | The [[rollback plan::The rollback plan defines the authorized return to a workable prior state, including the relevant ownership and conditions.]] needs its actual owner, conditions, and verified feasibility rather than a vague promise to undo everything.
Eric | I will align the IT and finance updates so one does not say complete while the other still reports an untested process.
Fatima | Good. [[User acceptance testing::User acceptance testing verifies business requirements through the relevant users and process, complementing technical component tests rather than being replaced by them.]] should reflect the business outcome, not just a successful technical component.
Eric | The sponsor update will state that login passed, invoice posting remains dependent on the old service, and the decision is pending.
Fatima | That makes [[data integrity::Data integrity concerns the accuracy and consistency of the resulting information and must remain a cutover requirement alongside availability and access controls.]] and continuity visible without bypassing controls, inventing approval, or treating the new platform's appearance as evidence that the migration is complete.''',
    rehearsal=['Read the corrected exchange and explain the service-account dependency in ordinary business language.', 'Switch roles and state the unresolved test, control requirement, and go/no-go status.'],
    transfer_title='A successful job produced mismatched totals', transfer_setup='A test job reports success, but finance finds that its output total does not match the expected test transactions. No acceptance signoff has been given.',
    transfer='''IT: "The job reported ___." | success | The technical status message reports completion, not verified correctness of every output.
Finance: "The totals do not ___." | reconcile | The actual output and expected transactions differ in the supplied test.
IT: "Business acceptance is not yet ___." | confirmed | The unresolved mismatch prevents claiming the supplied acceptance signoff is complete.
Finance: "Record the discrepancy before the go/no-go ___." | decision | The readiness decision needs the actual unresolved test evidence.'''))

BOOK['units'].append(unit(
    title='Keeping customer communications and payment changes controlled', scene='New ownership does not rewrite every invoice instruction',
    skill='Explain continuity to a customer while separating branding, contracting identity, and verified payment instructions.',
    brief='After the acquisition, customer contact Morgan receives a new logo announcement and a separate email asking for payment to a new bank account. Under the supplied approved transition plan, the existing US subsidiary remains the invoicing entity and payment instructions have not been changed. Account lead Sofia and integration consultant Daniel must verify the unexpected email through established channels and avoid sending unapproved new instructions.',
    cast='Sofia | Account lead\nDaniel | Integration consultant',
    culture=('Reassurance needs specific facts', 'Customers want to know whom they are dealing with, where to obtain support, and whether anything changes in the current process. A general welcome message should not imply unapproved contractual or payment changes.'),
    a='''Which entity remains the invoicing entity under the supplied plan? | The existing US subsidiary | The overseas parent automatically | A new unnamed company | The integration consultant | The approved transition plan retains the existing US subsidiary for invoicing.
What is the approved payment-instruction status? | No change has been approved | The new email is automatically valid | Every invoice must use a new account | The customer must choose between accounts | The brief states that payment instructions have not changed under the approved plan.
How should the unexpected email be treated? | As an unverified request needing established-channel verification | As proof that acquisition requires new bank details | As harmless because it contains the logo | As a completed authorized change | A separate unexpected account-change request requires verification rather than trust based on branding.''',
    vocabulary='''customer continuity | Maintenance of customer service and obligations during transition. | protect customer continuity
contracting entity | Legal person entering the relevant customer agreement. | identify the contracting entity
invoicing entity | Entity issuing the invoice under the actual arrangement. | confirm the invoicing entity
brand transition | Change in external name or visual presentation. | coordinate the brand transition
contract assignment | Transfer of contractual rights under the applicable terms and law. | review contract-assignment requirements
novation | Substitution of a contractual party or obligation under the applicable agreement and law. | obtain novation advice
customer consent | Customer agreement where required for a specified change. | verify customer-consent requirements
remittance instruction | Direction for making a payment. | verify remittance instructions
vendor master | Customer or company record containing supplier details. | control vendor-master changes
independent verification | Check using a trusted source separate from the unverified request. | perform independent verification
business email compromise | Fraud involving deceptive business communications or compromised accounts. | recognize business-email-compromise risk
callback control | Verification through an independently established contact route. | use the callback control
service-level commitment | Stated obligation concerning the level of service. | preserve service-level commitments
account handoff | Transfer of customer relationship responsibilities. | coordinate the account handoff
customer-facing notice | Communication intended for customers. | approve customer-facing notices
authorized signatory | Person with the relevant power to sign or authorize an action. | verify the authorized signatory
commercial continuity plan | Approved arrangement for maintaining customer-facing operations. | follow the commercial continuity plan
payment redirection | Change to the destination or process for a payment. | investigate payment redirection''',
    precision='The supplied plan retains the US invoicing entity and existing payment instructions. A new logo and an unexpected email do not authorize a bank-account change.',
    precision_extra='Real contract transfers, customer consents, tax invoices, and payment changes require their actual legal and control processes. The example does not establish universal acquisition consequences.',
    phrases='''Separate identity and branding | The logo changed; the approved invoicing entity has not.
State continuity | Continue using the existing approved payment instructions.
Challenge the request | That account-change email has not been verified.
Use a trusted route | Confirm through contact details already independently established.
Avoid email-loop verification | Do not rely only on the phone number inside the unverified message.
Clarify contract status | Ownership change alone does not answer the contract-transfer question.
Keep notices consistent | Customer-facing messages need the approved facts and review.
Close the handoff | Confirm the account owner, support route, and any actually authorized changes.''',
    notes='''Acquired by versus replaced by | Acquired by describes ownership; replaced by describes substitution and should not be assumed for the contracting entity.
Verified through versus replied to | Verification requires a reliable independent basis; replying to the same unverified sender is not equivalent.
No approved change versus no possible change | The first reports the current plan; the second makes an unsupported claim about every future arrangement.''',
    d='''Which customer statement matches the approved plan? | The existing US entity and payment instructions remain in use | The parent automatically replaces every contract party | The new logo validates the new bank account | The customer should pay whichever email arrived latest | The approved transition plan explicitly retains the existing entity and payment process.
Which verification route is appropriate? | Independently established trusted contact details | Only the number in the unexpected email | A reply asking the same sender to confirm itself | The appearance of the company logo | Independent verification avoids relying on information supplied by the unverified request itself.
What must be reviewed separately from branding? | Actual contract and invoicing-entity changes | Whether the logo file opens | The color of a presentation title | The alphabetical order of contacts | Branding does not determine the legal or operational status of the customer arrangements.
What should the team avoid? | Sending unapproved replacement payment instructions | Preserving the unexpected message through the reporting process | Explaining the current approved plan | Coordinating with the authorized account owner | A new instruction must not be improvised while the actual request is unverified.''',
    dialogue='''Sofia | A customer received our new logo announcement and then an email asking them to pay a different bank account. They assume both are part of integration.
Daniel | Separate the [[brand transition::The brand transition changes presentation and does not itself authorize a new payment destination or legal entity.]] from the payment request. The approved plan has not changed the remittance instructions.
Sofia | The customer also asks whether the overseas parent now replaces the US subsidiary on every invoice.
Daniel | Under the approved plan, the [[invoicing entity::The invoicing entity remains the existing US subsidiary in this case and should not be replaced merely because ownership or branding changed.]] remains the existing US subsidiary. We should not infer a substitution from the acquisition announcement.
Sofia | Their contract names that subsidiary too, but any actual transfer question needs the appropriate legal review.
Daniel | Correct. The [[contracting entity::The contracting entity is the legal party to the agreement, which must be distinguished from a brand or parent company.]] and its obligations should be described from the actual records, not a simplified group label.
Sofia | For the bank-account email, we should verify through the contact route already established in the relationship.
Daniel | Yes. Use [[independent verification::Independent verification checks the request through a trusted source separate from the unverified message rather than allowing the sender to authenticate itself.]] rather than relying on a new phone number printed in that same email.
Sofia | I will not send a replacement account number or ask the customer to choose between the two sets of instructions.
Daniel | Good. [[Payment redirection::Payment redirection changes where funds are sent and requires the actual authorization and control process, not an improvised response to conflicting emails.]] needs the actual controlled process and verified authorization.
Sofia | The logo and correct account-manager name make the email look convincing, but those details do not establish that it is genuine.
Daniel | That is why [[business email compromise::Business email compromise can involve convincing business details, so a familiar logo or name does not prove a payment-change request is authentic.]] is relevant during a transition. A plausible integration story should not bypass the controls.
Sofia | The customer may also need to update its supplier record, but we should give only approved entity information.
Daniel | Exactly. Any [[vendor master::The vendor master contains supplier particulars, and changes to it should use verified approved information rather than assumptions from a new brand announcement.]] change should follow the customer's and our actual verification requirements.
Sofia | Our immediate response can explain that the existing approved payment instructions remain in place while the unexpected request is checked.
Daniel | That protects [[customer continuity::Customer continuity maintains the verified service and payment process while the team resolves the unexpected request through the proper controls.]] without pretending that every integration question is already resolved.
Sofia | I will coordinate the account response with finance and the authorized security or fraud-reporting contact, preserving the message as required.
Daniel | Also align the [[customer-facing notice::The customer-facing notice must use approved facts so separate teams do not send contradictory statements about identity, payment, or service.]] so customers do not receive conflicting instructions from sales, finance, and the integration team.
Sofia | The account owner and support route remain clear, and any future approved change will use the actual notice and verification process.
Daniel | Record that in the [[commercial continuity plan::The commercial continuity plan states the approved customer-facing arrangement and should distinguish current continuity from future changes requiring separate authorization.]]. New ownership is not a reason to improvise a contract transfer or a bank-account change.''',
    rehearsal=['Read the corrected exchange and distinguish brand, contracting entity, invoicing entity, and payment destination.', 'Switch roles and give the customer the current approved status without supplying new payment details.'],
    transfer_title='A reply was treated as independent verification', transfer_setup='A team replies to an unexpected bank-account-change email, and the same sender says it is genuine. No independently verified contact has confirmed the request.',
    transfer='''Lead: "The reply came from the same ___." | sender | The confirmation repeats the unverified source rather than adding an independent basis.
Consultant: "That is not independent ___." | verification | The request has not been checked through a trusted separate channel.
Lead: "We need an established trusted ___." | contact | The verification should use a previously reliable independent contact route.
Consultant: "The payment change remains ___." | unverified | The supplied reply does not establish authorization or authenticity of the new instructions.'''))

BOOK['units'].append(unit(
    title='Reporting integration synergies without double counting', scene='Annual run rate is not money already realized',
    skill='Reconcile annualized savings, realized results, and integration costs on a defined reporting basis.',
    brief='A fictional procurement change saves USD 50,000 per month for three completed months against the agreed baseline. Gross realized savings are USD 150,000. A one-time integration cost of USD 90,000 belongs to the same reporting period and defined cash basis, giving USD 60,000 net realized benefit. Annualizing the monthly saving gives a USD 600,000 run rate, not a realized full-year result. IT and procurement both list the same saving in their workstream reports.',
    cast='Nina | Integration finance lead\nOscar | Procurement lead',
    culture=('Make a defensible result visible', 'A smaller, correctly labeled realized benefit is more useful than an inflated headline. Shared contributions can be acknowledged without booking the same saving twice.'),
    a='''What is the gross realized saving for the three months? | USD 150,000 | USD 600,000 | USD 60,000 | USD 90,000 | Three months at fifty thousand per month gives one hundred fifty thousand realized gross savings.
What is the net realized benefit on the supplied basis? | USD 60,000 | USD 150,000 | USD 600,000 | USD 510,000 | Subtracting the ninety-thousand integration cost from one hundred fifty thousand gives sixty thousand.
Why must the two workstream reports be reconciled? | They list the same saving | Each has a different verified benefit | The saving has no owner | Monthly and annual units are always identical | The same underlying saving appears in both reports and must not be counted twice.''',
    vocabulary='''synergy | Benefit attributed to combining businesses under a defined analysis. | substantiate the synergy
baseline | Agreed reference against which a change is measured. | establish the savings baseline
gross saving | Benefit before the specified related costs. | report the gross saving
net benefit | Benefit after the specified costs on the defined basis. | reconcile the net benefit
run-rate saving | Annualized or other normalized saving based on a stated current rate. | distinguish run-rate savings
in-period realization | Benefit actually achieved within the stated reporting period. | verify in-period realization
one-time integration cost | Nonrecurring transition cost under the stated classification. | track one-time integration costs
benefit owner | Person accountable for delivering and substantiating a benefit. | name the benefit owner
realization date | Date from which a benefit is treated as achieved under the methodology. | verify the realization date
benefit register | Record of benefits, owners, assumptions, and status. | update the benefit register
cost avoidance | Prevention of a prospective cost rather than necessarily reducing an existing expense. | distinguish cost avoidance
headcount saving | Defined labor-cost reduction subject to actual staffing and cost effects. | validate headcount savings
procurement saving | Reduction attributed to purchasing changes on a specified basis. | verify procurement savings
revenue synergy | Additional revenue attributed to integration under a defined analysis. | assess revenue synergies
dis-synergy | Adverse cost or revenue effect associated with integration. | identify dis-synergies
double counting | Recording the same underlying benefit more than once. | prevent double counting
finance validation | Review of figures and methodology by the designated finance role. | obtain finance validation
benefit bridge | Reconciliation from baseline and gross effects to the reported benefit. | prepare the benefit bridge''',
    precision='50,000 x 3 = 150,000 gross realized; 150,000 - 90,000 = 60,000 net realized. 50,000 x 12 = 600,000 annualized run rate, not a completed-year saving.',
    precision_extra='All figures use the supplied reporting period and cash basis. Real accounting recognition, attribution, timing, and future sustainability require the actual methodology and review.',
    phrases='''Label the measure | Six hundred thousand is the annualized run rate.
State realization | The completed three-month gross saving is one hundred fifty thousand.
Include the cost | The same-period integration cost reduces net realized benefit to sixty thousand.
Prevent duplication | IT and procurement contributed to one saving, not two separate benefits.
Check the baseline | Which agreed reference supports this calculation?
Separate future and past | The run rate assumes the monthly level continues.
Name accountability | One benefit owner should coordinate the supporting evidence.
Report the bridge | Show baseline, gross realization, included costs, and net result together.''',
    notes='''Annualized versus realized | Annualized projects a rate over a year; realized identifies benefit achieved in the stated period.
Avoided versus saved | Avoided can refer to a cost that did not arise; saved needs the actual baseline and measurement to be clear.
Contributed to versus owns the total | Several workstreams can contribute to one benefit without each recording the full amount as separate value.''',
    d='''Which headline is accurate? | 600,000 annualized run rate; 60,000 net realized in the stated period | 600,000 already realized in three months | 150,000 net after the 90,000 cost | 1.2 million because two workstreams reported the saving | This statement distinguishes the normalized rate from the actual net period result.
What is the double-counting correction? | Record the underlying benefit once while acknowledging both teams | Add both reports because both teams worked on it | Remove the cost so the numbers match | Call the same saving a second revenue synergy | Shared contributions do not create two separate economic benefits.
Which item is needed to interpret savings? | The agreed baseline and reporting basis | Only a larger headline figure | A promise that all future months are identical | A count of how many teams attended meetings | The baseline and basis determine what the reported change actually measures.
What does the annual run rate assume? | Continuation of the stated monthly rate for annualization | That twelve months have already elapsed | That no future risk can change the saving | That integration costs never exist | Annualization extends the current rate arithmetically and does not prove a realized or guaranteed future year.''',
    dialogue='''Oscar | The procurement change saves fifty thousand dollars a month, so I reported six hundred thousand as realized integration savings.
Nina | That is the annualized [[run-rate saving::Run-rate saving extends the stated monthly rate over a year and must not be reported as benefit already realized in only three months.]], not the completed-period result. We have three months of actual savings in the supplied record.
Oscar | Three times fifty thousand gives one hundred fifty thousand of gross savings for those completed months.
Nina | Correct. That is the [[in-period realization::In-period realization identifies the benefit actually achieved during the three completed months, not the annualized extrapolation.]] before the related cost included in this reporting basis.
Oscar | The one-time implementation expense was ninety thousand in the same period, and the report uses the stated cash basis.
Nina | Then include the [[one-time integration cost::The one-time integration cost is the ninety-thousand expense assigned to the same period and basis, which must be included in the supplied net calculation.]] rather than letting the headline imply the change was free to deliver.
Oscar | The net realized benefit is therefore sixty thousand, even though the monthly saving could continue beyond this quarter.
Nina | Exactly. The [[net benefit::Net benefit subtracts the specified ninety-thousand cost from one hundred fifty thousand of gross realization, yielding sixty thousand here.]] and the annual run rate are useful but different measures.
Oscar | I also noticed that IT listed the same vendor reduction in its workstream total because it helped remove duplicate licenses.
Nina | We need to prevent [[double counting::Double counting would record the same underlying vendor saving twice merely because two workstreams contributed to it.]]. Acknowledging both teams does not create two separate economic benefits.
Oscar | We can assign one shared record to the saving and show IT and procurement as contributors.
Nina | Put that in the [[benefit register::The benefit register records the unique underlying benefit, its contributors, owner, assumptions, and reporting status.]], with a single accountable owner for assembling and validating the evidence.
Oscar | We should also identify the reference cost we compared against, so the saving is not based on an unexplained estimate.
Nina | Yes. The agreed [[baseline::The baseline is the reference against which the reduction is measured and must be stated to make the saving interpretable.]] and any adjustments need to be traceable rather than reconstructed after the result is announced.
Oscar | If a planned future expense never occurs, should we record that in the same way as this reduction in an existing cost?
Nina | Not automatically. [[Cost avoidance::Cost avoidance concerns preventing a prospective expense and may differ from reducing an existing baseline cost, so the methodology must distinguish them.]] needs its own definition and evidence under the reporting methodology.
Oscar | I will show the monthly rate, actual months, gross amount, included cost, and net result in the steering pack.
Nina | That creates a clear [[benefit bridge::The benefit bridge reconciles the stated basis and gross effects to the net result rather than presenting unrelated figures as interchangeable.]], with the six-hundred-thousand annualization labeled separately.
Oscar | The revised headline will acknowledge the ongoing opportunity without saying that a full year's saving has already been achieved.
Nina | Good. Complete the required [[finance validation::Finance validation checks the figures, attribution, and methodology before the result is treated as an approved benefit report.]] and retain the evidence, so the report is credible rather than merely larger.''',
    rehearsal=['Read the corrected exchange and state the gross, cost, net, and annualized figures with their periods.', 'Switch roles and explain how two teams can contribute without creating two separately counted savings.'],
    transfer_title='A forecast entered the realized column', transfer_setup='A future supplier change is forecast to save USD 20,000 monthly after approval. Approval and implementation have not occurred, and no saving has been realized.',
    transfer='''Lead: "The amount is currently a ___." | forecast | The figure concerns a future proposed change, not an achieved result.
Finance: "The required approval remains ___." | outstanding | The scenario says the change has not yet been approved.
Lead: "No benefit has been ___." | realized | No implementation or actual saving has occurred in the supplied case.
Finance: "Keep it out of the realized-benefit ___." | total | A future forecast should not be counted as an already achieved benefit.'''))

BOOK['units'].append(unit(
    title='Handing over to business-as-usual owners', scene='An assigned issue is not a resolved issue',
    skill='Confirm acceptance evidence, ongoing support, and residual-risk ownership before closing integration work.',
    brief='The fictional handover plan requires five consecutive stable operating days before service acceptance. The new process has completed two stable days. A reporting defect remains open but has an identified finance owner. Sponsor Morgan wants the integration workstream closed immediately. Consultant Arjun explains the unmet acceptance condition and prepares the operational ownership, support, and open-item records without claiming that assignment means resolution.',
    cast='Morgan | Integration sponsor\nArjun | Integration consultant',
    culture=('A clear handover protects both teams', 'An integration team should not disappear behind a green status. The receiving operation needs evidence, workable support, and explicit ownership of remaining work.'),
    a='''How many stable days are required by this fictional plan? | Five consecutive days | Two days | Any single successful login | An unspecified month | The supplied acceptance criterion requires five consecutive stable operating days.
What is the reporting defect's status? | Open with a named finance owner | Resolved because someone owns it | Deleted from the record | Accepted as proof that every process is stable | Assigning an owner does not establish that the defect has been fixed.
Why is immediate acceptance unsupported? | Only two of the required five stable days are complete | The transaction never closed | Every support contact is forbidden | The process has no owner at all | The stated acceptance condition remains unmet after only two stable days.''',
    vocabulary='''business as usual | Ongoing operational work after the temporary integration phase. | transition to business as usual
acceptance criteria | Conditions that must be met for the stated acceptance decision. | verify acceptance criteria
service acceptance | Formal acceptance of an operational service under the actual process. | obtain service acceptance
operational signoff | Authorized confirmation of operational readiness or acceptance. | secure operational signoff
knowledge transfer | Handover of information and practical capability to another team. | complete knowledge transfer
runbook | Operational instructions and responsibilities for recurring tasks or incidents. | validate the runbook
standard operating procedure | Approved instructions for a defined recurring process. | update the standard operating procedure
open risk | Identified unresolved uncertainty or exposure. | retain an open risk
defect backlog | Record of unresolved defects and their status. | maintain the defect backlog
incident owner | Person responsible for handling a specified operational incident. | name the incident owner
support coverage | Availability and scope of assistance during stated periods. | confirm support coverage
monitoring cadence | Frequency of reviewing operational indicators or issues. | agree the monitoring cadence
escalation contact | Named route for raising an issue requiring further authority or support. | verify the escalation contact
operating budget | Resources allocated for ongoing operations. | confirm the operating budget
ownership transfer | Explicit handover of responsibility to the receiving role. | document ownership transfer
transition exit | Completion of the defined temporary transition arrangement. | approve transition exit
closure report | Record of completed scope, outstanding matters, and closure authority. | prepare the closure report
post-integration review | Evaluation of integration results and remaining lessons after the transition. | schedule a post-integration review''',
    precision='Two stable days do not satisfy the supplied five-consecutive-day criterion. An open defect remains open when an owner is assigned.',
    precision_extra='Actual acceptance, exception authority, and closure processes depend on the program. Do not silently waive criteria or transfer risk without the required agreement and records.',
    phrases='''Check the criterion | We have completed two stable days against a five-day requirement.
Separate assignment and resolution | Finance owns the defect, but the defect is still open.
Confirm the receiver | Who accepts the ongoing operational responsibility?
Make support usable | The receiving team needs the runbook and actual escalation contacts.
Preserve the record | Open items must remain visible after the project label changes.
Clarify authority | Any exception needs the stated approval; it cannot be implied by a target date.
Avoid a false close | We can prepare the handover without declaring acceptance complete.
Close deliberately | Record completed scope, remaining obligations, and the authorized closure decision.''',
    notes='''Assigned versus resolved | Assigned names responsibility; resolved claims the underlying issue has been addressed.
Prepared versus accepted | Prepared describes readiness of the handover materials; accepted describes the actual receiving decision.
Consecutive versus total | Consecutive requires an uninterrupted sequence; five scattered stable days may not meet that stated condition.''',
    d='''Which status report is accurate? | Two stable days complete; acceptance condition unmet | Five stable days complete because the sponsor wants closure | The defect is resolved because finance owns it | Every open item disappears at handover | This choice preserves the actual operating evidence and the unmet criterion.
What should happen to the defect at handover? | Retain its status, owner, next action, and review route | Remove it because the project is ending | Mark it closed without evidence | Transfer it to an unnamed department | An unresolved item needs traceable ownership and follow-up rather than disappearance from the record.
What should knowledge transfer establish? | The receiving team's practical ability to operate the process | Only that a file was emailed | Only a new organization chart | A promise that no incident can occur | Knowledge transfer should support actual operational capability, not just document transmission.
What is required for an exception to the criterion? | The actual specified exception authority and process | An implied waiver from schedule pressure | A green status color | The consultant's wish to finish | A stated condition cannot be silently waived without the relevant authorization.''',
    dialogue='''Morgan | The process has worked for two days, and finance owns the remaining reporting issue. Can we close the workstream today?
Arjun | The [[acceptance criteria::The acceptance criteria require five consecutive stable days in this fictional plan, so two days do not establish completion.]] specify five consecutive stable days. We have completed two, not the required five.
Morgan | I do not want the integration team to remain indefinitely just because one minor report still needs attention.
Arjun | We can plan the handover, but [[service acceptance::Service acceptance is the actual authorized acceptance of the operation under the stated conditions, not a synonym for preparing to hand over.]] and closure need their actual evidence and authority.
Morgan | The finance lead has accepted responsibility for the report. Does that at least mean we can mark the defect closed?
Arjun | No. The [[defect backlog::The defect backlog records unresolved problems, and assigning an owner does not establish that the underlying defect has been fixed.]] should show it as open with an owner, next action, and review route.
Morgan | The receiving team also needs to know how the new process works and whom to contact when something fails.
Arjun | That is [[knowledge transfer::Knowledge transfer builds the receiving team's practical understanding and capability, rather than merely sending a document or naming a department.]], not just a document email. We need to check that the operational team can use the material.
Morgan | We have a draft procedure, but the escalation contact still points to a consultant who leaves next week.
Arjun | Then the [[runbook::The runbook must contain usable operational instructions and current responsibilities, not an escalation route that disappears after transition.]] needs a workable ongoing contact before we describe the support arrangement as complete.
Morgan | We should confirm the hours and scope of support instead of assuming the receiving team provides the same transition coverage.
Arjun | Yes. [[Support coverage::Support coverage defines when and how assistance is available, which must be agreed rather than inherited by assumption from the temporary project team.]] and the operating resources need explicit agreement.
Morgan | Could we say the handover is prepared while leaving acceptance pending until the stated conditions are met?
Arjun | That is accurate. [[Ownership transfer::Ownership transfer is an explicit handover of responsibility to the receiving role and should not be inferred solely from preparing documents.]] still needs the receiving role's actual acceptance and the required record.
Morgan | If leadership wants an exception to the five-day condition, it should be a visible decision through the specified authority.
Arjun | Correct. Do not hide an [[open risk::An open risk remains an unresolved exposure and must be recorded even when an authorized decision accepts or transfers responsibility for it.]] by changing the status label. Any exception needs its actual approval and conditions.
Morgan | I will tell the sponsor group that handover preparation is progressing, but the operating evidence does not yet meet the criterion.
Arjun | Include that distinction in the [[closure report::The closure report records completed scope, remaining obligations, and actual closure authority rather than implying that preparation equals completion.]], along with the reporting defect and the named operational responsibilities.
Morgan | After acceptance, we should review whether the integration achieved its intended service and value outcomes, not just whether the project ended.
Arjun | Schedule the [[post-integration review::The post-integration review evaluates outcomes after transition and remains distinct from administrative closure of the workstream.]]. That keeps attention on the ongoing business result without declaring unfinished work complete today.''',
    rehearsal=['Read the corrected exchange and distinguish assigned, prepared, accepted, and resolved.', 'Switch roles and give the handover status using the two completed days, five-day criterion, and open reporting defect.'],
    transfer_title='A file transfer was called knowledge transfer', transfer_setup='The consultant emails the runbook. The receiving team has not reviewed it, confirmed the contacts, or accepted responsibility.',
    transfer='''Consultant: "The document has been ___." | sent | Email delivery is the completed action supplied in the scenario.
Operator: "Our practical review is still ___." | pending | The receiving team has not yet checked the material or contacts.
Consultant: "Responsibility has not been formally ___." | accepted | No receiving-team acceptance is supplied by the document email alone.
Operator: "We need a usable handover, not only a file ___." | transfer | Moving a file does not establish operational understanding or ownership.'''))
