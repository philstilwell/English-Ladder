"""Original earned-value, sprint-adaptation, and operational-transition scenes."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='Spending less than planned is not necessarily good news',
        skill='Explain earned-value measures without confusing budget performance, cash, and calendar delay.',
        setup='At one reporting date, a fictional project has planned value of $60,000, earned value of $45,000, and actual cost of $50,000, all on the same agreed basis. A sponsor calls the $10,000 difference between planned value and actual cost a saving. The analyst must explain the supported measures. No final-cost or completion-date forecast is supplied.',
        cast='Ines|Project controls analyst\nDrew|Sponsor',
        dialogue='''Drew|We planned sixty thousand dollars and spent fifty thousand. Can I tell the steering group we have saved ten thousand?
Ines|Not from those figures. The [[planned value::Planned value is the budget assigned to work scheduled by the reporting date, not the value of the work actually completed.]] is sixty thousand, but we have not completed all the work scheduled for this point.
Drew|What number shows the work we have actually achieved on the budget basis? I do not want to confuse invoices with progress.
Ines|The [[earned value::Earned value is the budgeted value of work actually performed under the agreed measurement method, here $45,000.]] is forty-five thousand. That is the budgeted value of the completed work, not sales revenue or the cash received.
Drew|Then fifty thousand is the cost of achieving forty-five thousand of budgeted work. That is different from being ten thousand under budget.
Ines|Exactly. The [[cost variance::Cost variance is earned value minus actual cost: $45,000 minus $50,000 gives negative $5,000.]] is negative five thousand: forty-five minus fifty. We have spent more than the earned value of the work achieved.
Drew|The report also asks for the cost index. Could you explain the ratio in language the steering group can follow?
Ines|The [[cost performance index::The cost performance index is earned value divided by actual cost; $45,000 divided by $50,000 equals 0.90.]] is zero point nine. On this basis, each dollar of actual cost has earned ninety cents of budgeted work value.
Drew|And how far behind the planned work are we? I assume that needs the sixty-thousand figure rather than actual cost.
Ines|Yes. The [[schedule variance::The earned-value schedule variance is earned value minus planned value: $45,000 minus $60,000 equals negative $15,000 of budgeted work.]] is negative fifteen thousand in budgeted-work terms. That is not fifteen thousand dollars of cash loss or fifteen days of delay.
Drew|The schedule index would therefore be forty-five divided by sixty, or zero point seven five. Does that mean the finish date is twenty-five percent late?
Ines|No. It describes earned value relative to planned value at this point. The completion date needs the remaining schedule and its dependencies, not that direct conversion.
Drew|Could we use the cost index to produce a final-cost forecast for the board?
Ines|Only with the appropriate remaining-work basis and assumptions. An [[estimate at completion::An estimate at completion forecasts total final cost using a justified method and assumptions; the three supplied current-period measures alone do not provide it.]] is a forecast, not a number we should infer without the necessary inputs.
Drew|I will replace savings with the actual position: less work achieved than scheduled, and a negative cost variance on that achieved work.
Ines|Good. Keep the common reporting date and measurement basis visible so the comparison does not mix this month\'s costs with last month\'s progress.
Drew|What do you need from the delivery team before we discuss recovery? I would rather ask for specific evidence than demand a better index.
Ines|The remaining work, its current estimate, dependencies, and proposed actions. We also need to understand the causes of the variance before assigning a remedy.
Drew|Then the steering group gets the supported measures today and a separately identified forecast review. We will not announce a saving or a new finish date.
Ines|Exactly. These measures identify questions requiring attention; they do not replace the work of explaining the performance and planning what happens next.''',
        transfer_title='A positive cash difference hides a cost overrun',
        transfer_setup='On a consistent basis, planned value is $20,000, earned value is $15,000, and actual cost is $18,000.',
        transfer='''Sponsor: Cost variance compares earned value with actual ___.|cost|The cost variance uses earned value minus actual cost, not planned value minus spending.
Analyst: Fifteen thousand minus eighteen thousand gives a negative three-thousand-dollar ___.|variance|The calculation shows a $3,000 unfavorable cost variance on the work performed.
Sponsor: The schedule comparison uses the twenty-thousand-dollar planned ___.|value|Planned value provides the scheduled-work basis for the earned-value schedule comparison.
Analyst: A monetary schedule variance is not a calendar-day ___.|delay|Earned-value schedule variance measures budgeted work and cannot be read directly as days late.''',
        reference=('National Science Foundation: Earned Value Management Gold Card', 'https://www.nsf.gov/od/ori/evm-gold-card')),
    scenario(
        title='A new request arrives halfway through the sprint',
        skill='Negotiate a delivery plan around a sprint goal without treating selected work as immutable or quality as optional.',
        setup='A Scrum team is halfway through a sprint whose goal is to let support agents find an overdue case and see its owner. An unrelated dashboard color request arrives from a senior stakeholder. The selected work already fills the Developers\' current capacity forecast. The Product Owner and a Developer discuss options; no change has been made.',
        cast='Alexis|Product Owner\nBo|Developer',
        dialogue='''Alexis|A senior stakeholder wants the dashboard colors changed this week. Before I respond, can we look at what that would do to our current plan?
Bo|Yes. Our [[Sprint Goal::The Sprint Goal is the sprint's single objective; here it concerns finding an overdue case and its owner, not an unrelated visual request.]] is overdue-case lookup with the owner visible. The color request does not help us meet that objective.
Alexis|I do not want to add it just because the requester is senior. At the same time, I should not tell them the plan can never change.
Bo|Agreed. The [[Sprint Backlog::The Sprint Backlog is the Developers' current plan for the Sprint Goal and selected work; it can be adapted as more is learned.]] is a plan we adapt as we learn. We need to discuss the impact, not treat it as either untouchable or unlimited.
Alexis|The original selection uses the capacity you forecast. Would the color change displace work needed for the case lookup?
Bo|On our present assessment, yes. It also needs the usual checks. It is not free work simply because the visible change looks small.
Alexis|Could we reduce a nonessential part of the selected work while still meeting the goal? I would like to understand that option before saying no.
Bo|We can examine it together, but we must not compromise the [[Definition of Done::The Definition of Done describes the required quality state of the Increment; dropping required checks to fit extra work would not satisfy it.]]. Removing required checks is not a legitimate way to make room.
Alexis|Understood. I can place the color request in the [[Product Backlog::The Product Backlog is the ordered list of what is needed to improve the product; adding an item there does not promise delivery in the current sprint.]] for ordering and refinement if it does not fit this sprint.
Bo|That lets us assess its value and detail without quietly changing today\'s work. Please tell the stakeholder that recording the request is not a delivery promise.
Alexis|What about the Daily Scrum? Could I use tomorrow\'s meeting to assign the new request to someone with a lighter-looking task list?
Bo|That is not its purpose. The [[Daily Scrum::The Daily Scrum is for the Developers to inspect progress toward the Sprint Goal and adapt their plan, not a manager's task-allocation meeting.]] helps the Developers inspect progress toward the goal and adapt the plan. A short task list does not establish spare capacity.
Alexis|I will bring the value and urgency question to our planning discussion instead. Is there any new information threatening the goal itself?
Bo|The test data is late, and we are arranging an alternative dataset through the approved route. I will make that obstacle visible rather than hide it behind a busy board.
Alexis|Then the immediate priority is resolving that obstacle. When we speak to the stakeholder, I can explain why the lookup outcome remains our focus.
Bo|Yes. And the [[Increment::An Increment must meet the Definition of Done to be usable; a demonstration of unfinished work does not make that work Done.]] we describe as usable must meet our quality definition. A convincing demonstration is not enough if required work is incomplete.
Alexis|I will acknowledge the color request, record it, and explain that delivery this week is not agreed. We can revisit its order with the other product needs.
Bo|I will update the current plan and the data dependency with the Developers. Any scope negotiation needs to preserve the goal, not rewrite it after the fact.
Alexis|That gives us a clear response without claiming Scrum means never changing anything or accepting every urgent-looking request.
Bo|Exactly. We can adapt the work intelligently while keeping the objective and the quality expectation clear.''',
        transfer_title='A demonstration is mistaken for Done work',
        transfer_setup='A feature works in a demonstration, but required checks in the team\'s Definition of Done are incomplete.',
        transfer='''Product Owner: The demonstration does not establish that the item is ___.|Done|The required quality criteria remain incomplete despite the successful demonstration.
Developer: Keep the unfinished checks visible in the current ___.|plan|The Developers' plan should show the actual remaining work instead of hiding it.
Product Owner: Do not drop required quality work to accept an extra ___.|request|Adding scope does not justify lowering the Definition of Done.
Developer: Explain progress against the agreed Sprint ___.|Goal|The Sprint Goal provides the objective for assessing progress and adapting the plan.''',
        reference=('Schwaber and Sutherland: The Scrum Guide', 'https://scrumguides.org/scrum-guide.html')),
    scenario(
        title='The project is finishing, but who supports the service on Monday?',
        skill='Negotiate an operational handover with clear ownership, open defects, and support boundaries.',
        setup='A project plans to hand a new internal service to operations on Friday. Training is complete, but the out-of-hours contact, access to monitoring, and ownership of three open defects are unresolved. A two-week enhanced-support period is proposed, not yet staffed or agreed. The project lead meets the service owner.',
        cast='Nadia|Project lead\nFelix|Service owner',
        dialogue='''Nadia|Training is complete and the project closes on Friday. Are you comfortable taking the service from Monday, including anything that happens outside office hours?
Felix|Not yet. The [[operational acceptance::Operational acceptance establishes that the agreed conditions for taking responsibility are met; completing training does not settle every support requirement.]] checklist still has open items. We have no confirmed out-of-hours contact, and my team cannot access the monitoring view.
Nadia|I saw the training completion note and assumed the handover was ready. Let us go through the remaining conditions instead of relying on that one milestone.
Felix|Start with the [[support model::The support model defines who handles incidents, how they are routed, and when coverage is available for the service.]]. Who receives the first call, who investigates, and who can make a service decision when the project team is unavailable?
Nadia|The proposal names the service desk for first contact and our technical team for escalation, but their coverage has not been confirmed.
Felix|Then the [[escalation matrix::The escalation matrix identifies the roles and routes for unresolved or serious issues; it needs actual owners and coverage rather than unconfirmed names.]] is incomplete. A name on a slide does not establish that someone has accepted the duty or can be reached.
Nadia|I will resolve that with the responsible managers. What do you need on the monitoring side before accepting the service?
Felix|Working access, a usable [[runbook::A runbook gives the approved operational procedures and relevant response information for the service; training attendance alone does not provide that resource.]], and confirmation that the team can find the required information. We should check those with the people who will use them.
Nadia|There are also three open defects. The project report calls them minor, but we should describe their effect and the agreed handling individually.
Felix|Exactly. I need the user impact, current workaround where approved, and [[defect ownership::Defect ownership assigns responsibility for tracking and resolving each defect after transition; an open list without owners leaves the work unassigned.]]. The word minor does not tell my team what to do.
Nadia|Would the proposed two-week hypercare period cover the remaining questions? That was intended to give operations extra support after the transition.
Felix|It could help, but [[hypercare::Hypercare is a defined period of enhanced support after a change; its label does not establish staffing, responsibilities, or completion conditions.]] needs agreed staffing, scope, and exit conditions. At present it is an unstaffed proposal, not confirmed cover.
Nadia|We should not assume project closure automatically closes those defects or ends every responsibility. I will keep the unresolved work in the transition record.
Felix|Thank you. We also need to distinguish service acceptance from any commercial or contractual closeout. My decision should not imply authority over those separate matters.
Nadia|I will bring the contact coverage, monitoring access, defect assignments, and enhanced-support proposal to the readiness review. Is anything else missing from the decision package?
Felix|Include the acceptance criteria and evidence for each. If a condition remains open, state its consequence and who can decide the appropriate response.
Nadia|Then Friday is a planned decision point, not an automatic transfer because the calendar says the project should end.
Felix|Correct. I can commit to reviewing a complete package; I cannot commit to accepting unknown support gaps in advance.
Nadia|I will update the project board with that distinction and arrange the right people for the review, including the proposed support owners.
Felix|That gives us a real handover conversation. Operations needs a service it can support, not only a completed training attendance sheet.''',
        transfer_title='An enhanced-support period has no assigned team',
        transfer_setup='A transition plan promises ten days of enhanced support, but no staff, contact route, or exit conditions have been agreed.',
        transfer='''Service owner: The support period is proposed, not yet ___.|staffed|The plan names a period but does not identify committed people to provide coverage.
Project lead: Confirm responsibilities and the incident contact ___.|route|Operational teams need a known way to obtain help from the responsible support roles.
Service owner: Define the conditions for ending enhanced ___.|support|Exit conditions establish when the additional support can end on an agreed basis.
Project lead: Keep unresolved conditions visible at the acceptance ___.|review|The acceptance review must consider actual gaps rather than infer readiness from a promised period.'''),
]
