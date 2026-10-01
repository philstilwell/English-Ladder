"""Original project-delivery conversations and fixed-answer practice."""
from books.authoring import unit

BOOK = dict(
    slug='project-management', title='Project Management English',
    cover_label='Scope / schedules / decisions / delivery',
    cover_title='Project Management', cover_size=30,
    tagline='Make the dependency visible. Make the decision clear.',
    audience='For project managers, coordinators, delivery leads, sponsors, and project-office teams.',
    map_intro='Eight delivery conversations that turn requests, dates, risks, and progress claims into precise project communication.',
    notes_title='A useful update enables a decision.',
    notes_intro='Project conversations compress complicated situations into short phrases: nearly done, approved in principle, on track, or just one more feature. Each can hide a different uncertainty. These cases develop the language for unpacking the claim, identifying the consequence, and making the next decision explicit without burying the listener in a task-by-task history.',
    field_notes=[
        ('Give each claim a reference point', 'A delay needs a baseline and a calendar. Completion needs acceptance evidence. A color rating needs defined criteria. State the basis before expecting another person to act on the label.', '"Testing is forecast three working days behind the approved schedule."'),
        ('Separate an option from authorization', 'A useful proposal can still be unapproved. Say who recommends it, who can decide, what changes, and when a decision is needed. Do not turn meeting enthusiasm into permission.', '"The group recommends deferring the feature; approval is still required."'),
        ('Distinguish present problems from uncertainty', 'A confirmed missed commitment is an issue to manage now. Its full consequences may remain uncertain. Keep both the present fact and the future exposure visible.', '"The supplier has confirmed the miss; the replacement delivery date is still unknown."'),
        ('Close the communication loop', 'Name the action, owner, deadline, and evidence needed to close it. A sent message, a scheduled review, or a vendor completion claim is not proof that the receiving team accepted the result.', '"Two acceptance criteria still lack evidence; please confirm their review owner."')],
    scope_note='Original fictional language practice, not a project-management certification, contract interpretation, engineering instruction, or release authorization. All organizations, dates, numbers, and decisions are invented. Actual work must follow the governing agreement, approved project controls, applicable rules, and responsible decision makers.',
    sources=[
        dict(title='Association for Project Management. What Is Change Control?', url='https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/', note='Background on recording, assessing, and deciding proposed baseline changes. The trade-off cases and decisions in this book are original.', checked='30 September 2026'),
        dict(title='Piney, C. Integrated Project Risk and Issue Management. Project Management Institute, 2012.', url='https://www.pmi.org/learning/library/2019/04/07/15/25/integrated-project-risk-issue-management-6303', note='A conference paper discussing risk and issue distinctions, not a claim that every organization uses an identical register or terminology.', checked='30 September 2026'),
        dict(title='UK Government Project Delivery. Government Functional Standard GovS 002: Project Delivery.', url='https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/', note='Background on governance, accountability, and delivery controls in UK government. The book does not impose that framework on every organization.', checked='30 September 2026'),
        dict(title='NASA. Systems Engineering Handbook, Appendix D: Requirements Verification Matrix.', url='https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/', note='Background on linking requirements to identifiable verification evidence. The vendor case is a fictional project discussion, not a NASA acceptance process.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Project Charter and Scope Definition',
    scene='A dashboard is not yet a defined project',
    skill='Clarify the users, decisions, boundaries, and acceptance basis behind a sponsor request before treating a target date as a commitment.',
    brief='Sponsor Greg requests a dashboard in four weeks, but the initial brief does not identify users, decisions, or exclusions. In a planning meeting with project manager Elena, he proposes a first release for operations leads doing weekly queue triage: overdue-item visibility and an export. Automated work allocation would be excluded. Data access and acceptance criteria remain unconfirmed, and no scope baseline is approved. Elena must turn the request into a reviewable definition without promising the four-week target.',
    cast='Greg | Project sponsor\nElena | Project manager',
    culture=('Clarification protects the intended value', 'A sponsor may name a solution before describing the decision it should support. Ask what people will do with the result and what belongs outside the first release. The questions make the request actionable; they do not require the sponsor to design every technical detail.'),
    a='''Who are the proposed first-release users? | Operations leads doing weekly queue triage | Every external customer | Only the finance audit committee | Unspecified public visitors | The meeting proposal identifies operations leads and their weekly triage task.
Which feature is proposed as excluded? | Automated work allocation | Overdue-item visibility | An export | Access to the proposed first-release view | The proposed boundary explicitly excludes automated allocation while retaining visibility and export.
What does four weeks represent now? | A requested target, not a supported delivery commitment | A completed acceptance decision | Proof that data access is available | An approved baseline with all dependencies confirmed | The request precedes confirmed access, acceptance criteria, and an approved scope baseline.''',
    vocabulary='''project charter | A document formally establishing a project and its high-level authority and purpose. | approve the project charter
project sponsor | The person accountable for sponsorship and relevant business decisions. | confirm the project sponsor
business need | The problem or opportunity the work is intended to address. | clarify the business need
business case | The justification for the proposed investment and expected value. | review the business case
project objective | A specific result the project is intended to achieve. | define the project objective
deliverable | A defined output to be produced by the project. | identify the deliverable
outcome | A change or result enabled by using the project's outputs. | distinguish outputs from outcomes
benefit | A measurable improvement of value from the change. | define the expected benefit
scope statement | A description of the work and boundaries included in the project. | refine the scope statement
scope baseline | The approved scope reference used to manage and assess changes. | establish the scope baseline
in scope | Included within the defined project boundary. | confirm what is in scope
out of scope | Excluded from the defined project boundary. | state what is out of scope
assumption | A premise used for planning that needs appropriate validation or monitoring. | record a planning assumption
constraint | A limit within which the project must operate. | identify a constraint
requirement | A defined need or condition the solution must satisfy. | clarify the requirement
acceptance criterion | A condition used to decide whether an output is acceptable. | define acceptance criteria
stakeholder | A person or group affected by or able to affect the project. | identify key stakeholders
end user | A person who will use the delivered capability. | consult the end user
decision use | The decision or action a delivered information product supports. | clarify the decision use
work breakdown structure | A hierarchical division of project work into manageable components, abbreviated WBS. | develop the work breakdown structure
work package | A defined unit of work that can be assigned and managed. | specify a work package
requirements traceability | Links connecting needs, requirements, work, and evidence. | maintain requirements traceability
success measure | A defined indicator used to assess the intended result. | agree a success measure
scope approval | Authorization of the stated project boundaries and work. | obtain scope approval''',
    precision='A dashboard is an output; improved queue decisions would be an intended outcome. The proposed users and exclusions narrow the request, but they do not confirm access, acceptance, or schedule feasibility. Four weeks remains a target until supported and authorized.',
    precision_extra='An export and automated allocation are different capabilities. Listing one does not silently include the other. Acceptance needs a checkable basis, including who accepts the result; a demonstration that looks useful is not automatically formal approval.',
    phrases='''Clarify the need | Which decision should the dashboard help users make?
Name the audience | The proposed first users are operations leads.
Anchor the task | They will use it for weekly queue triage.
Define the output | The first release would show overdue items and provide an export.
State the exclusion | Automated allocation is outside the proposed first release.
Separate value from output | A delivered screen is not itself evidence of better queue decisions.
Qualify the date | Four weeks is the requested target, not yet a delivery commitment.
Identify a dependency | We still need to confirm access to the source data.
Ask for acceptance | What evidence will show that the first release meets the agreed need?
Name the approver | Who is authorized to accept the defined output?
Keep assumptions visible | Record the data-access assumption until it is verified.
Avoid implied additions | A useful future feature is not automatically part of this release.
Define a measurable check | Replace looks good with a checkable acceptance condition.
Preserve the proposal | These are proposed boundaries pending review.
Connect the records | Link the requirements to the scope and acceptance evidence.
Close the definition | Confirm users, decision use, inclusions, exclusions, and approval route.''',
    notes='''Dashboard | Names a product form, not its full purpose or scope.
Need | Distinguish the business problem from a preferred implementation.
Target | An intended date, not automatically an authorized commitment.
First release | Requires explicit limits rather than an implied complete solution.
Accepted | Needs the relevant criteria and decision authority.
Useful | A value judgment that still needs a stated user and task.''',
    d='''Which scope statement best matches the supplied proposal? | Overdue-item visibility and export for weekly operations triage, excluding automated allocation | A complete automated allocation platform for all customers | Any feature suggested during development | A screen with no identified user or decision | This wording identifies the intended users, work purpose, included functions, and explicit exclusion.
What can Elena responsibly say about four weeks? | It is the target; access, acceptance, and feasibility still need confirmation. | It is guaranteed because the sponsor requested it. | It is already an achieved delivery date. | It means every proposed future feature is included. | The missing planning inputs prevent the requested date from becoming a supported commitment.
Which is an outcome rather than merely an output? | Operations leads make better-supported queue-priority decisions. | A dashboard file is delivered. | An export button exists. | A project charter is stored. | An outcome concerns changed use or behavior enabled by the delivered outputs.
Why define who accepts the work? | A useful demonstration does not identify authorized acceptance by itself. | Any observer's applause automatically approves the baseline. | Acceptance is unrelated to the agreed requirements. | The vendor can decide every customer's obligations alone. | Acceptance requires an applicable decision process and authority, not simply a favorable reaction.''',
    dialogue='''Greg | I would like the dashboard in four weeks. The request is short because I thought the team would know what a useful operations dashboard should contain.
Elena | We need to clarify the [[business need::The business need explains the problem the dashboard addresses rather than assuming its form defines its purpose.]]. Which decision should it support, and who will use it? Those answers help us define the first release rather than guess.
Greg | Operations leads would use it for weekly queue triage. They need to see overdue items and take an export into the planning discussion.
Elena | That gives us a specific [[end user::The end user is the operations lead using the proposed dashboard for weekly triage.]] and task. It is more actionable than a dashboard for everyone, because we can connect the requirements to a real workflow.
Greg | I do not need automated work allocation in the first version. That might become useful later, but visibility and an export are the immediate request.
Elena | I will make that [[out of scope::Out of scope identifies automated allocation as excluded from the proposed first release.]] for the proposed first release. A possible future capability should not quietly enter the current delivery commitment.
Greg | Is the dashboard itself the objective, or should we describe what changes once the team uses it? I want the project to do more than add another screen.
Elena | Distinguish the [[deliverable::The deliverable is the dashboard output, distinct from the operational result achieved by using it.]] from the intended outcome. We can deliver a working view, but better queue decisions require the right information and actual use by the leads.
Greg | We should probably define what shows that the view is adequate. Otherwise I might approve a demonstration and discover later that it cannot support the weekly meeting.
Elena | We need an [[acceptance criterion::An acceptance criterion makes adequacy checkable instead of relying on a favorable demonstration impression.]] for each relevant requirement. We also need to identify who can accept the output and what evidence they will review.
Greg | The data team has not confirmed access yet. I had assumed the existing operational records would be available, but that is not the same as having permission.
Elena | Record that [[assumption::The assumption is the unverified planning premise that the source data will be available.]] and its owner. We should establish the access conditions before treating the source as ready for development and testing.
Greg | Then four weeks may still be possible, but I should not tell other departments it is an approved delivery promise simply because I prefer that date.
Elena | Correct. The [[constraint::The requested timing is a planning limit to assess, not evidence that the proposed work is feasible within it.]] needs assessment alongside the work and dependencies. If the date is fixed, we need a supported scope and delivery plan within that limit.
Greg | I am comfortable reviewing a clearer definition first. It should show the user, the two requested capabilities, the exclusion, and the open access question.
Elena | That belongs in the [[scope statement::The scope statement describes the proposed work and boundaries before they become an approved reference.]]. Once the appropriate review and authorization occur, we can distinguish the approved reference from later requests to add features.
Greg | We should keep the requirements connected to the reason for the project. Otherwise an attractive feature may distract us from the weekly triage need.
Elena | Use [[requirements traceability::Requirements traceability connects each requirement and its evidence to the underlying need and agreed work.]] to preserve those connections. The record should show why the work exists, how it is checked, and whether it belongs in this release.
Greg | Good. Please bring the definition and unresolved decisions to the review. I will not announce the date or the wider automation feature as approved today.
Elena | Then we can seek [[scope approval::Scope approval authorizes the defined boundaries; the current discussion prepares that decision rather than pretending it occurred.]] on a clear basis. The immediate result is a reviewable proposal, not a promise built from a product name and a target alone.''',
    transfer_title='An export is not automation',
    transfer_setup='A proposed first release includes a weekly export for operations leads. Automated allocation is excluded. Data access is unconfirmed, and the target date has not been approved.',
    transfer='''Sponsor: "The included capability is a weekly ___." | export | The supplied proposal specifically includes an export for the first release.
Manager: "Automated allocation is ___." | excluded | The proposed boundary explicitly leaves automated allocation outside this release.
Sponsor: "Data access remains ___." | unconfirmed | The briefing does not establish that the source data is available.
Manager: "The target is not an approved ___." | commitment | The requested date has not received approval as a delivery commitment.'''))

BOOK['units'].append(unit(
    title='Schedule, Critical Path, and Dependencies',
    scene='One late task can move the release',
    skill='Explain a schedule impact using dependencies, working days, and remaining durations while keeping recovery options conditional.',
    brief='Planner Luis and delivery lead Anika examine a simplified working-day schedule. Testing was due at the end of day 5 and is now forecast to finish at the end of day 8. Rehearsal takes two working days after testing, followed by a one-day approval task. These finish-to-start links have no lag or buffer, and this chain controls the release milestone. Other work is on schedule. No recovery change is approved; durations and the working calendar are unchanged.',
    cast='Luis | Project planner\nAnika | Delivery lead',
    culture=('Explain the chain, not only the late task', 'A listener may hear that most work is on time and assume the release is safe. Show how the delayed predecessor moves the next necessary step. State the assumptions clearly so a forecast is neither understated nor presented as an unavoidable result if a feasible recovery option later receives approval.'),
    a='''How late is the testing finish forecast? | Three working days | Eight working days | Two calendar months | No delay | The forecast moves from the end of working day 5 to the end of working day 8.
When did the baseline release chain finish? | End of day 8 | End of day 5 | End of day 10 | End of day 11 | Testing ended on day 5, rehearsal used days 6 and 7, and approval used day 8.
What is the forecast release finish with unchanged logic and durations? | End of day 11 | End of day 8 | End of day 9 | End of day 13 | Testing ends on day 8, rehearsal uses days 9 and 10, and approval uses day 11.''',
    vocabulary='''schedule baseline | The approved timing reference used to assess project progress. | compare with the schedule baseline
schedule forecast | The current estimate of future task or milestone timing. | update the schedule forecast
working calendar | The defined days and hours available for scheduled work. | apply the working calendar
working day | A day counted as available work under the stated calendar. | state the delay in working days
activity duration | The time needed to perform a defined scheduled task. | estimate activity duration
remaining duration | The work time still needed to finish an activity. | update remaining duration
predecessor | A task whose timing affects a linked later task. | identify the predecessor
successor | A task whose timing depends on a linked earlier task. | assess the successor
finish-to-start dependency | A link requiring the predecessor to finish before the successor starts. | check a finish-to-start dependency
lag | A specified waiting interval in a dependency link. | define the lag
lead | An allowed overlap relative to a dependency link. | justify a schedule lead
critical path | The controlling task sequence determining the schedule's earliest completion. | analyze the critical path
total float | Time an activity can move without delaying the defined project finish under the schedule model. | assess total float
free float | Time an activity can move without delaying the earliest start of its successor. | distinguish free float
milestone | A defined project event used to track an important point. | confirm the release milestone
slippage | Movement later than the stated planned timing. | report schedule slippage
downstream impact | The effect of a change on subsequent linked work. | trace the downstream impact
resequence | Change the order or logic of planned tasks. | assess whether to resequence work
fast-tracking | Overlapping work that was planned in sequence, with resulting risks. | assess fast-tracking
crashing | Shortening duration by adding resources or cost where feasible. | evaluate schedule crashing
resource leveling | Adjusting timing to resolve resource limits or conflicts. | apply resource leveling
schedule compression | Reducing planned duration through an assessed change. | assess schedule compression
recovery option | A proposed way to regain lost time or restore a milestone. | evaluate a recovery option
forecast variance | The difference between current forecast and the specified baseline. | explain the forecast variance''',
    precision='Baseline: testing through day 5, rehearsal days 6-7, approval day 8. Forecast: testing through day 8, rehearsal days 9-10, approval day 11. The milestone moves three working days, not three days for each downstream task.',
    precision_extra='This conclusion depends on the stated controlling chain, zero buffer, unchanged calendar, and fixed durations. In another project, float or different dependencies could change the result. Extra resources and overlapping tasks are proposals to assess, not automatic recovery.',
    phrases='''Start with the movement | Testing is forecast to finish three working days late.
State the comparison | The baseline finish is day 5; the current forecast is day 8.
Name the blocked step | Rehearsal cannot start until testing finishes.
Explain the sequence | Two days of rehearsal are followed by one day of approval.
Calculate the baseline | The original chain completed at the end of day 8.
Calculate the forecast | With unchanged logic, the chain now completes at the end of day 11.
Qualify the arithmetic | This chain has no buffer and controls the release milestone.
Avoid false averaging | On-time work elsewhere does not cancel this controlling delay.
Keep calendars consistent | These are working days under the same calendar.
Avoid double counting | The three-day delay moves the chain; it is not added separately at every task.
Explore resources carefully | Additional people shorten the task only if the work can use them effectively.
Distinguish overlap | Fast-tracking changes sequencing and may create rework risk.
Keep recovery conditional | No schedule-recovery change has been approved.
Preserve the reference | Update the forecast without silently rewriting the baseline.
Ask for a decision | Compare the feasible recovery options and their consequences.
Close the update | Report the milestone impact, assumptions, owner, and next checkpoint.''',
    notes='''Late | Late against which baseline and calendar?
Critical | Refers to schedule control here, not merely a task that feels important.
Float | Schedule flexibility under a defined model, not unlimited spare time.
Forecast | A current estimate that can change with new evidence.
Recover | Requires a feasible, authorized plan rather than optimism.
Parallel | Independent work does not automatically remove a controlling dependency.''',
    d='''Which statement correctly reports the unchanged forecast? | Release moves from end of day 8 to end of day 11, a three-working-day delay. | Every downstream task adds another three-day delay, making nine. | Other on-time tasks cancel the delay automatically. | Testing finishes on day 8, so release must happen that same day. | The sequential two-day rehearsal and one-day approval preserve the three-day shift in the controlling chain.
What does the on-time status of unrelated work establish? | That work is on schedule, not that this critical chain is unaffected | The delayed predecessor is automatically complete | Three working days disappear from the calendar | The release has already been authorized | Independent progress does not remove the stated dependency that controls the release.
Which proposal is fast-tracking? | Overlap tasks previously planned in sequence, after assessing feasibility and risk | Add any number of people without examining the task | Rename the baseline date without a decision | Treat calendar weekends as working days without a calendar change | Fast-tracking changes sequencing through overlap and can introduce additional risk.
A different task has four days of total float and slips three days with no other changes. What follows? | Its slip can be absorbed without moving the defined project finish. | Every project always slips three days. | The task has gained seven days of float. | Float means the task can be omitted. | The three-day movement is within the stated four-day allowance under that different schedule model.''',
    dialogue='''Anika | Testing is three working days late in the latest forecast, but most other tasks are on schedule. Can I still tell the sponsor the release date is unchanged?
Luis | Not with this [[critical path::The critical path is the stated controlling testing-rehearsal-approval chain, so independent on-time work does not remove its delay.]]. Testing controls rehearsal, and rehearsal controls the approval task. The simplified schedule has no buffer in that chain.
Anika | Walk me through the original dates so I can explain the impact rather than repeat a warning without showing where it comes from.
Luis | The [[schedule baseline::The schedule baseline puts testing at day 5, rehearsal on days 6-7, and approval on day 8.]] had testing finish at the end of day five. Rehearsal used days six and seven, with the approval task on day eight.
Anika | Now testing is forecast to finish at the end of day eight. Rehearsal cannot simply begin earlier because the test result is its required input.
Luis | Correct. That is a [[finish-to-start dependency::A finish-to-start dependency prevents rehearsal from starting until testing has finished under the stated plan.]]. With no lag, rehearsal starts on day nine and takes two working days, followed by approval on day eleven.
Anika | So the release moves three working days, not nine. We do not add the same three-day slip again at each linked task.
Luis | Exactly. The [[downstream impact::The downstream impact is the three-day movement of the subsequent chain, not repeated addition of the same delay.]] carries through the chain once. Testing, rehearsal, and approval shift in sequence while their stated durations remain unchanged.
Anika | I want to make sure I am not mixing working days with calendar days. A weekend might otherwise make the sponsor read the dates differently.
Luis | Use the same [[working calendar::The working calendar defines available workdays and must be consistent across the baseline and forecast calculation.]] for the comparison. Our planning view labels working days directly; the dated schedule still needs its holidays and available work periods applied consistently.
Anika | Could spare time elsewhere protect the release? People often tell me there is slack in another part of the plan.
Luis | Check [[total float::Total float is schedule flexibility before the defined finish moves; this controlling chain is stated to have none.]] on the affected path, not a general impression that other tasks have room. The supplied chain has none, so the unchanged forecast moves.
Anika | What about putting more people on testing? I can present that as an option, but I should not assume the task will automatically finish sooner.
Luis | That would be a [[crashing::Crashing adds resources or cost to shorten duration only where the activity can actually use them effectively.]] proposal if it feasibly shortens duration. We need to assess usable capacity, cost, coordination, and the work remaining before claiming a recovered date.
Anika | Another suggestion is to begin part of rehearsal before testing finishes. That changes the logic and might create rework if the results change.
Luis | That is [[fast-tracking::Fast-tracking overlaps previously sequential work and requires assessment of feasibility and additional risk.]]. It needs a specific feasible overlap and risk assessment, not simply an instruction to do everything at once.
Anika | Until an option is approved, I should report the current date as day eleven and keep the original day-eight commitment visible for comparison.
Luis | Yes. Update the [[schedule forecast::The schedule forecast is the current timing estimate; updating it does not silently authorize a new baseline.]] without silently rewriting the baseline. Otherwise the reporting would hide the very movement the sponsor needs to understand.
Anika | My update will show the three-day impact, the blocked rehearsal, and the recovery options under assessment. I will not call those options a completed recovery.
Luis | That makes the [[forecast variance::Forecast variance is the difference between current forecast and the original reference, here three working days.]] clear. State the assumptions and next review point, so the sponsor can distinguish today's supported forecast from a possible future improvement.''',
    transfer_title='Carry the delay once',
    transfer_setup='In a simplified working-day chain, testing was due day 4 and is now forecast day 6. A one-day review must follow, with no buffer or lag. No recovery is approved.',
    transfer='''Planner: "The original chain finished on day ___." | five | Testing through day four followed by one review day finishes on day five.
Lead: "The forecast finish is now day ___." | seven | Testing through day six followed by one review day finishes on day seven.
Planner: "That is a ___-working-day delay." | two | The finish moves from day five to day seven, a two-day difference.
Lead: "No recovery has been ___." | approved | The briefing explicitly leaves every recovery option without authorization.'''))

BOOK['units'].append(unit(
    title='Risk Register and Issue Escalation',
    scene='The supplier miss is no longer just a possibility',
    skill='Escalate a confirmed delivery problem while separating the known event, uncertain consequences, and unapproved response.',
    brief='Project manager Rina and procurement lead Omar review a supplier commitment for October 12. The supplier has confirmed that date will be missed and gives October 15 only as an earliest possible date, not a new commitment. Testing planned for October 13 needs the delivery. The risk register still describes a possible delay with a 30% likelihood. No replacement source or recovery plan is approved. Rina must update the status, preserve the history, and request a useful escalation.',
    cast='Rina | Project manager\nOmar | Procurement lead',
    culture=('Escalation should explain the need for help', 'A senior audience needs the confirmed problem, the threatened objective, and the decision or support required. A register entry is not a response plan. Avoid keeping an outdated probability merely because the final delivery date and full project impact are not yet known.'),
    a='''What has the supplier confirmed? | The October 12 commitment will be missed. | Delivery is guaranteed on October 15. | Testing has already finished. | A replacement source is approved. | The confirmed fact is the original-date miss, while the later date remains only a possibility.
What does October 15 represent? | The earliest possible date mentioned, not a commitment | The actual receipt date | The approved release date | The date all risk disappears | The briefing explicitly qualifies October 15 as possible rather than committed.
Why is the October 13 test exposed? | It requires the delivery that will miss October 12. | It is unrelated to the supplier item. | It has already passed without the item. | Every testing task always lasts thirty days. | The supplied dependency connects the missed delivery to the planned test start.''',
    vocabulary='''risk | Uncertainty that may affect a project objective positively or negatively. | assess project risk
threat | A potential event or condition with an adverse effect. | identify a delivery threat
opportunity | Uncertainty with a potentially beneficial effect on an objective. | assess an opportunity
risk register | A record of identified risks, assessment, ownership, and responses. | maintain the risk register
issue | A present problem requiring attention or resolution. | log an issue
issue log | A record tracking current problems and their resolution. | update the issue log
risk owner | The person accountable for managing a defined risk. | assign a risk owner
action owner | The person responsible for carrying out a particular response action. | name the action owner
likelihood | The assessed chance of an uncertain event or condition. | reassess likelihood
impact | The consequence for a defined objective if an event occurs. | assess schedule impact
risk exposure | The project's susceptibility to the relevant uncertainty and consequences. | review risk exposure
trigger | A condition or event prompting a defined response. | recognize the trigger
risk response | A planned or implemented action addressing an identified risk. | develop a risk response
mitigation | Action intended to reduce a threat's likelihood or impact. | assess mitigation
contingency plan | A prepared response to be used if specified conditions arise. | activate a contingency plan
fallback plan | An alternative response if the primary response does not work. | prepare a fallback plan
residual risk | Risk remaining after a response has been applied. | monitor residual risk
secondary risk | New risk introduced by a response to another risk. | identify secondary risks
escalation threshold | The point at which an issue or risk must be referred to higher authority. | apply the escalation threshold
escalation brief | A concise statement of the problem, consequence, and help or decision needed. | prepare an escalation brief
decision deadline | The latest time a decision is needed to support the stated plan. | state the decision deadline
contingency reserve | Provision for identified uncertainty within the applicable plan. | clarify contingency-reserve use
response status | Whether a response is proposed, approved, underway, or completed. | report response status
closure evidence | Information showing that the stated closure conditions are met. | require closure evidence''',
    precision='The missed commitment is a present issue once confirmed; the replacement date and final effect may still be uncertain. Update the issue and linked risk records without erasing the history or pretending every downstream consequence is already known.',
    precision_extra='Earliest possible October 15 is not promised October 15. A proposed alternative source is not approved mitigation or completed recovery. Separate event status, impact estimate, response status, and the evidence required to close the issue.',
    phrases='''State the confirmed event | The supplier has confirmed it will miss October 12.
Correct the old wording | Possible delay no longer describes the commitment status.
Preserve uncertainty | The replacement delivery date is not committed.
Qualify the earliest date | October 15 is the earliest possibility mentioned.
Connect the dependency | The October 13 test requires this delivery.
Keep the history | Link the issue to the original risk entry.
Separate consequences | The delivery miss is confirmed; the full milestone impact is still being assessed.
Name the owner | Assign responsibility for obtaining a committed supplier recovery plan.
Make the request actionable | We need a decision on the feasible response options.
Avoid imaginary recovery | No alternative source has been approved.
Distinguish planning from action | A contingency plan must be checked before it is treated as activated.
Watch new exposure | Expediting can introduce cost or quality risks.
Retain residual risk | A response may reduce exposure without removing every uncertainty.
Set the decision time | State when the decision is needed and why.
Define closure | Close only when the agreed evidence supports closure.
Close the escalation | Report the fact, consequence, owner, response status, and next checkpoint.''',
    notes='''Possible | No longer adequate for an event already confirmed.
Earliest | A lower timing bound or possibility, not a promised arrival.
Mitigated | Identify the implemented action and remaining exposure.
Owned | A named person is not evidence that the problem is resolved.
Escalated | Referred for attention, not automatically decided.
Closed | Requires a defined condition and evidence, not a reassuring message.''',
    d='''Which opening is accurate now? | The October 12 miss is confirmed; the replacement date remains uncommitted. | There is only a 30% chance the original commitment will be missed. | October 15 is a guaranteed recovery. | The issue is closed because the supplier replied. | The opening separates the established miss from continuing uncertainty about replacement timing.
How should the original risk record be handled? | Update its status and link it to the current issue while preserving history. | Delete every reference so no one sees the earlier warning. | Keep the old wording unchanged because impact is uncertain. | Mark all project risks closed. | Linked records preserve how the risk developed without leaving an obsolete event status in place.
What should an escalation request include? | The confirmed problem, affected objective, options, decision owner, and needed timing | Only the sentence supplier bad | A completed approval that never occurred | An unsupported guarantee that testing is unaffected | Decision-useful escalation connects the facts and consequences to specific help or authorization.
Which is a secondary risk from using an untested replacement? | New quality or integration uncertainty introduced by the response | The original risk entry's document color | Proof that all risk is eliminated | A guarantee that the replacement is already accepted | A response can create new exposure that must be distinguished from the original supplier problem.''',
    dialogue='''Rina | The supplier has confirmed it will miss October twelfth, but our register still says possible delivery delay with a thirty-percent likelihood. That wording is now misleading.
Omar | We have a current [[issue::An issue is the confirmed commitment problem that now needs action, even though its final consequences remain uncertain.]]. The uncertainty is no longer whether the original commitment will be met; it concerns the replacement timing and the consequences for our work.
Rina | The supplier mentioned October fifteenth as the earliest possible date. I want to make sure nobody turns that into a confirmed recovery in the project update.
Omar | Keep the [[response status::Response status distinguishes a possible recovery date from an approved or completed response.]] explicit. The supplier has not committed to the fifteenth, and we have no approved replacement source or recovery plan.
Rina | Testing is planned for October thirteenth and requires the delivery. That is the immediate dependency we need to show in the escalation.
Omar | State the [[impact::Impact concerns the effect on the planned test and project objectives, which still needs assessment beyond the confirmed miss.]] carefully. The planned test is threatened by the confirmed miss, but we still need a supported assessment of the full milestone consequence.
Rina | Should we remove the original risk entry now? I do not want two records to make it look like two separate supplier problems.
Omar | Update the [[risk register::The risk register should preserve the original risk's history and link it to the current issue.]] and link it to the issue log. Preserve the history and distinguish the event status rather than deleting the warning or duplicating its impact.
Rina | We had identified this supplier miss as a condition requiring escalation. It sounds as though that point has now been reached, regardless of the uncertain new date.
Omar | The [[trigger::The trigger is the confirmed supplier miss that prompts the previously identified escalation response.]] has occurred. An uncertain recovery date is not a reason to postpone acknowledging the event that activates the response.
Rina | I need someone clearly responsible for obtaining the supplier's committed plan. A general instruction to procurement will not tell the sponsor who is following up.
Omar | Name an [[action owner::The action owner is responsible for the specific task of obtaining and reporting the supplier recovery information.]] for that task, with a due time and escalation route. That is separate from pretending the person can guarantee a date the supplier has not committed to.
Rina | There may be a contingency in the procurement plan, but we should check its conditions and availability before saying it has solved the problem.
Omar | Exactly. A [[contingency plan::A contingency plan is a prepared response whose conditions and readiness must be checked before it is treated as active.]] must be usable under the current facts. A named alternative is not automatically available, qualified, authorized, or fast enough for the test.
Rina | If we expedite or switch sources, we may create new costs or quality questions. The escalation should not present every response as an uncomplicated improvement.
Omar | Those are potential [[secondary risks::Secondary risks are new uncertainties introduced by the response, such as quality or integration exposure from switching suppliers.]]. Assess them alongside the remaining exposure from the original delay, and keep the response options comparable on a stated basis.
Rina | I will prepare a short decision request: confirmed miss, affected test, uncommitted replacement date, options under assessment, and the time when support is needed.
Omar | That is a useful [[escalation brief::An escalation brief connects the confirmed problem and consequences to the specific decision or support needed.]]. It gives the decision maker something to act on rather than a long register entry with no clear request.
Rina | When the supplier sends another update, we should not close the issue merely because the wording sounds positive. We need to know what actually changed.
Omar | Require [[closure evidence::Closure evidence demonstrates that the defined issue-resolution conditions are met, not merely that a supplier sent a reassuring message.]]. A committed plan may change the status, but completion and closure depend on the agreed conditions and verified result, not the tone of the reply.''',
    transfer_title='A confirmed miss, an uncertain replacement',
    transfer_setup='A vendor confirms it cannot deliver Tuesday. Thursday is suggested but not committed. A Wednesday test needs the item. No alternative is approved.',
    transfer='''Manager: "Tuesday's miss is ___." | confirmed | The vendor explicitly states it cannot meet the Tuesday commitment.
Buyer: "Thursday remains ___." | uncommitted | The later date is only suggested, with no delivery commitment.
Manager: "The Wednesday test has a delivery ___." | dependency | The test requires the item, linking its timing to the vendor delivery.
Buyer: "No alternative has been ___." | approved | The scenario supplies no authorized substitute or recovery arrangement.'''))

BOOK['units'].append(unit(
    title='Stakeholder Alignment and Governance',
    scene='A recommendation is not an approval',
    skill='Close a governance meeting with a clear decision status, accountable authority, and accurate record of recommendations and actions.',
    brief='Project manager Rae reviews meeting notes with steering-group chair Simon. The group recommended changing a release feature, but the notes say change approved. The project governance plan reserves this change decision to the sponsor; no written delegation or sponsor decision is recorded. The group can recommend and commission analysis. Rae must correct the minutes, identify the approval route, and separate an action to prepare an assessment from authority to implement the feature change.',
    cast='Rae | Project manager\nSimon | Steering-group chair',
    culture=('Ask the authority question before the room empties', 'A meeting can reach a strong recommendation without having the authority to implement it. Clarify what was decided, who can authorize the next step, and what the team may do meanwhile. This prevents a cooperative discussion from becoming an ambiguous instruction passed to delivery teams.'),
    a='''Who holds the stated change authority? | The sponsor | Every meeting attendee independently | The note taker automatically | An unnamed vendor | The governance plan explicitly reserves this change decision to the sponsor.
What did the steering group actually do? | Recommend a change | Record a sponsor approval | Supply a written delegation | Implement the feature change | The brief describes a recommendation and says no sponsor decision or delegation is recorded.
What may the group commission under the supplied remit? | Analysis of the proposal | Unrestricted implementation of the change | A false approval record | A replacement of the sponsor's reserved authority | The group can recommend and request analysis, which is distinct from authorizing implementation.''',
    vocabulary='''governance | The arrangements for project direction, decisions, oversight, and accountability. | clarify project governance
steering group | A group guiding the project within its defined authority. | convene the steering group
terms of reference | The document defining a group's purpose, membership, and remit. | check the terms of reference
remit | The area of responsibility and authority assigned to a person or group. | stay within the remit
change authority | The person or body empowered to authorize a specified change. | identify the change authority
delegated authority | Decision power explicitly assigned by an authorized person or body. | verify delegated authority
approval threshold | A boundary determining the level of authorization required. | apply the approval threshold
decision rights | Defined responsibility for making particular decisions. | confirm decision rights
recommendation | A proposed course of action submitted for consideration. | record a recommendation
endorsement | Expressed support that may not itself constitute formal approval. | distinguish endorsement from approval
authorization | Permission from the appropriate authority to take the stated action. | obtain authorization
quorum | The minimum participation required for a body's valid proceedings under its rules. | confirm a quorum
consensus | Broad agreement among participants on a stated matter. | establish the scope of consensus
dissent | A stated disagreement with a proposal or conclusion. | record material dissent
decision log | A record of actual decisions, authority, conditions, and dates. | maintain the decision log
action log | A record of assigned tasks, owners, deadlines, and status. | update the action log
minutes | The formal record of a meeting's relevant proceedings and outcomes. | correct the minutes
escalation route | The path for referring a matter beyond the current authority. | use the escalation route
stage gate | A defined review point for an authorization or continuation decision. | prepare for a stage gate
assurance review | An examination intended to provide confidence in delivery or controls. | commission an assurance review
accountability | Answerability for a defined decision or result. | assign accountability
RACI | A responsibility model distinguishing responsible, accountable, consulted, and informed roles. | clarify the RACI roles
decision paper | A document presenting the issue, options, consequences, and requested decision. | prepare a decision paper
conditional approval | Authorization limited by explicit conditions. | record conditional approval''',
    precision='Consensus in the steering group does not override the sponsor authority stated in this case. A quorum only answers whether the group can validly conduct its own business; it does not enlarge its remit or create an unrecorded delegation.',
    precision_extra='An action to prepare analysis is not an instruction to implement the change. Minutes should distinguish recommendation, analysis action, approval request, and actual decision. If an approval is conditional, both the conditions and their status must remain visible.',
    phrases='''Check the record | The minutes say approved, but the group made a recommendation.
Name the authority | The governance plan reserves this decision to the sponsor.
Ask about delegation | Is there an explicit delegation covering this change?
Separate agreement | Consensus here does not by itself provide implementation authority.
Clarify the remit | The group can recommend and commission analysis.
Distinguish the action | Preparing the assessment is not approval to implement.
Frame the request | The sponsor needs the options, impacts, and specific decision sought.
Preserve dissent | Record material objections accurately rather than inventing unanimity.
Correct the status | Mark the change as recommended, with approval pending.
Assign the preparation | Name the owner and deadline for the decision paper.
Keep delivery informed | Tell the team exactly what work is authorized meanwhile.
Avoid a silent decision | No objection in the meeting is not a recorded sponsor approval.
Check a condition | State what must happen before a conditional approval takes effect.
Confirm the outcome | Read back the decision, authority, limits, and action owners.
Keep the records distinct | Put decisions in the decision log and tasks in the action log.
Close the route | Send the recommendation through the defined approval route.''',
    notes='''Supported | May mean endorsed, not authorized.
Approved | State by whom, for what, and under which conditions.
Aligned | Clarify whether people agree on the problem, recommendation, or actual action.
Quorate | Valid attendance does not create authority outside the group's remit.
Consulted | Asked for input, not necessarily empowered to approve.
Pending | An open status that must remain visible to implementation teams.''',
    d='''Which correction belongs in the minutes? | Change recommended; sponsor approval pending; analysis commissioned | Sponsor approved despite no recorded decision | Change implemented because the room agreed | All decision rights transferred automatically to the chair | The correction separates the actual recommendation and permitted analysis from missing approval.
What does the group's consensus establish? | Support for a recommendation within its remit | Automatic transfer of the sponsor's authority | Proof of an unrecorded written delegation | Unlimited power to change every baseline | Agreement among participants does not override the authority specified by the governance plan.
Which task can proceed under the supplied facts? | Preparing the commissioned impact analysis | Implementing the proposed feature change as approved | Announcing a sponsor decision that is absent | Erasing the approval requirement from the record | Commissioned analysis is within the group's stated remit, unlike the reserved change approval.
Which record best captures conditional approval if it is later given? | The actual approver, permitted change, explicit conditions, and condition status | Only the word approved without limits | A claim that every possible change is authorized | A recommendation relabeled as approval before the sponsor acts | The conditions define the approval's scope and must not disappear during the handoff.''',
    dialogue='''Simon | The meeting seemed aligned on changing the feature, and the notes say change approved. I assumed that reflected the room, but you have flagged the wording.
Rae | The room made a [[recommendation::A recommendation proposes a course of action; it does not establish the reserved sponsor approval.]]. Our governance plan reserves this decision to the sponsor, and the record contains neither a sponsor decision nor an explicit delegation.
Simon | We had enough members present and everyone supported the proposal. Does that not give the group authority to move the change forward?
Rae | A [[quorum::A quorum satisfies the group's participation rules but does not expand its substantive decision authority.]] lets the group conduct business under its rules. It does not expand the remit or replace a decision explicitly reserved to someone else.
Simon | Then I need to distinguish agreement about what we should recommend from authority to tell the delivery team to build it.
Rae | Exactly. Check the [[terms of reference::Terms of reference define the steering group's remit, here recommendation and analysis rather than reserved change approval.]]. This group can recommend and commission analysis; it cannot treat its own enthusiasm as permission outside the authority the project has assigned.
Simon | There may be a delegation somewhere, but I have not seen one. I should not ask the team to proceed on the assumption that it probably exists.
Rae | Verify [[delegated authority::Delegated authority must be explicitly established; the team cannot infer it from a possible undocumented arrangement.]] before relying on it. Until then, the sponsor remains the stated decision maker for this change, and the implementation status should remain pending.
Simon | We did assign someone to assess the impact. I want that work to proceed, because the sponsor will need a clearer comparison of the options.
Rae | Put that in the [[action log::The action log records the authorized assessment task, its owner, and deadline, not a decision to implement.]]. The task is to prepare analysis with an owner and deadline; it is not an instruction to implement the feature change.
Simon | What should the sponsor receive? Sending the meeting transcript would show the discussion, but might not make the actual choice very clear.
Rae | Prepare a [[decision paper::A decision paper presents the options, consequences, and specific authorization requested from the proper decision maker.]]. Include the options, consequences, recommendation, and specific authorization sought, along with the date when the decision is needed for delivery planning.
Simon | I will correct the minutes to say recommended rather than approved. Should we also explain that the analysis is authorized while implementation is not?
Rae | Yes. Keep [[authorization::Authorization identifies exactly which action is permitted; here analysis can proceed while implementation remains unapproved.]] attached to the specific action. Otherwise the team may hear that work can proceed and assume that means the change itself.
Simon | We should preserve any material objections as well. A short record does not need every comment, but it should not rewrite a qualified view as complete agreement.
Rae | Record material [[dissent::Dissent preserves relevant disagreement instead of falsely presenting the recommendation as unanimous or unqualified.]] accurately. The sponsor needs the substantive concerns, not a smoother account that hides the trade-off the group actually discussed.
Simon | If the sponsor later approves with conditions, the delivery team needs those conditions too. The word approved on its own would still be incomplete.
Rae | A [[conditional approval::Conditional approval permits only the stated action under explicit conditions, whose status must remain visible.]] must state the limits and what must be satisfied. We should not silently treat an unmet condition as though it has already been cleared.
Simon | I will read back the corrected result: recommendation supported, assessment commissioned, sponsor decision pending. Then we will send the paper through the stated route.
Rae | Update the [[decision log::The decision log should reflect actual decisions and their authority, not convert the meeting recommendation into approval.]] accordingly and tell the delivery team the same status. A clear handoff will preserve both useful progress and the actual boundary on implementation.''',
    transfer_title='Authorize analysis, not implementation',
    transfer_setup='A committee may commission analysis but cannot approve a cost change. It recommends an option and requests an assessment. The finance sponsor has not decided.',
    transfer='''Chair: "The committee has made a ___." | recommendation | The committee supports an option without holding the reserved approval authority.
Manager: "The authorized next task is the ___." | assessment | The committee can commission the analysis requested in the briefing.
Chair: "The sponsor's decision is still ___." | pending | The finance sponsor has not made the required decision.
Manager: "Implementation is not yet ___." | authorized | A recommendation and an assessment request do not approve the cost change.'''))

BOOK['units'].append(unit(
    title='Change Requests and Scope Creep',
    scene='Just one more report before launch',
    skill='Respond constructively to a late scope request by comparing explicit options, effort, schedule effects, and approval status.',
    brief='Two weeks before launch, sponsor Nadia asks project manager Chen to add a new report. The current plan uses all 20 remaining person-days. The report is estimated at four person-days including testing. The team has assessed two feasible options: defer an existing four-person-day export feature and retain the launch date, or keep all features and extend the schedule by two working days using the planned team. Both need approval. No overtime, extra staff, or reduced testing is assumed.',
    cast='Nadia | Project sponsor\nChen | Project manager',
    culture=('A constructive boundary includes options', 'A sponsor may hear an immediate no as resistance, but an unqualified yes can conceal a delivery problem. Acknowledge the value, explain the capacity limit, and present the assessed options. The decision is about priorities and consequences, not whether the team is sufficiently willing.'),
    a='''How much effort is estimated for the new report? | Four person-days including testing | Two person-days excluding testing | Zero because the report is requested late | Twenty person-days of confirmed extra capacity | The brief gives a four-person-day estimate and explicitly includes testing.
Which assessed option retains the launch date? | Defer the existing four-person-day export feature | Keep every feature with no other change | Add unapproved overtime automatically | Remove testing from the report | The assessed substitution frees the effort needed for the new report while retaining the date.
What is the status of both options? | They need approval. | Both are already approved simultaneously. | The export has already been removed. | The new launch date is already the baseline. | The briefing states that neither option has yet received authorization.''',
    vocabulary='''change request | A recorded proposal to alter agreed project work or parameters. | raise a change request
change control | The process for assessing and deciding changes to an approved reference. | follow change control
scope creep | Uncontrolled growth in project work without corresponding assessment and authorization. | prevent scope creep
change log | A record of proposed and decided project changes. | update the change log
impact assessment | Analysis of how a proposal affects relevant project dimensions. | complete an impact assessment
effort estimate | The amount of work expected, expressed in person-time or another work unit. | qualify the effort estimate
person-day | One person's defined day of work used as an effort unit. | estimate effort in person-days
elapsed duration | The time passing from an activity's start to finish. | distinguish elapsed duration
capacity limit | The amount of work the stated resources can support. | explain the capacity limit
trade-off | A choice between competing benefits, costs, or constraints. | present the trade-off
scope substitution | Replacing one part of planned work with another under an authorized change. | assess a scope substitution
deferred feature | A capability moved out of the current delivery scope or timing. | identify the deferred feature
incremental cost | Additional cost caused by the proposed change. | assess incremental cost
opportunity cost | Value forgone by choosing one use of resources over another. | explain the opportunity cost
benefit impact | The effect of a change on the value expected from the project. | assess benefit impact
rework | Work repeated or revised because of a change or defect. | estimate rework
test coverage | The extent to which specified requirements or conditions are tested. | preserve required test coverage
release boundary | The defined set of capabilities included in a particular release. | clarify the release boundary
change freeze | A point or period limiting changes under the project's stated rules. | apply the change-freeze rules
baseline revision | An authorized update to the controlled project reference. | record a baseline revision
approval record | Evidence of the actual authorization and its limits. | retain the approval record
implementation instruction | A clear direction specifying the authorized change to perform. | issue an implementation instruction
option comparison | An assessment of alternatives on a consistent basis. | prepare an option comparison
decision latency | Time between needing a decision and receiving it. | account for decision latency''',
    precision='Four person-days is effort; two working days is an assessed schedule extension with the planned team. They are not interchangeable units. The supplied options already include testing and assume no extra staff or overtime.',
    precision_extra='Deferring the export preserves the date but changes the delivered capability and possible benefit. Keeping all features preserves scope but moves timing. Neither is a free addition, and an authorized change is not the same as uncontrolled scope creep.',
    phrases='''Acknowledge the value | I understand why the new report would be useful at launch.
State the current limit | The plan already uses all 20 remaining person-days.
Quantify the addition | The report is estimated at four person-days including testing.
Avoid unit confusion | Effort is four person-days; the assessed extension is two working days.
Present the substitution | We can retain the date by deferring the existing export feature.
Present the timing option | We can keep all features with the assessed two-working-day extension.
Name the lost capability | The substitution means the export is not in this release.
Keep assumptions visible | Neither option assumes extra staff, overtime, or reduced testing.
Protect the decision | We need approval before changing the committed scope or date.
Separate value and capacity | A valuable request still consumes delivery effort.
Compare consequences | Review the timing and benefit effects on the same basis.
Avoid a hidden shortcut | Removing required testing is not one of the assessed options.
Record the request | Put the new report and its impacts in the change record.
Check decision timing | A late decision may require the estimates to be refreshed.
Preserve the baseline | Update the controlled plan only after the actual decision.
Close the choice | Confirm which option is approved and what the team should implement.''',
    notes='''Small | A description that does not replace an effort estimate.
Just | Can conceal additional work when used before a new requirement.
Can | State the conditions under which delivery is feasible.
Swap | Still changes scope and may change expected value.
Estimate | A supported forecast, not an unconditional guarantee.
Approved | Identify the selected option, limits, and implementation date.''',
    d='''Which response is both constructive and accurate? | We can assess the new value through the two stated options, each with a consequence and approval need. | Yes, everything fits unchanged because the sponsor asked. | No change can ever be considered in a project. | Testing can be silently removed to make room. | The response acknowledges the request while preserving capacity, trade-offs, and decision authority.
Why does the four-person-day estimate not mean a four-day extension here? | Effort and elapsed duration differ; the assessed team plan gives two working days. | Person-days are the same as calendar days in every case. | Testing has been excluded without disclosure. | The original plan contains unlimited unused capacity. | The supplied assessment distinguishes total work from elapsed schedule time with the planned resources.
What must the date-preserving option disclose? | The existing export will be deferred from this release. | Every original capability remains unchanged. | The new report needs no testing. | The scope baseline has already been revised. | The option preserves time by changing scope, so the removed capability must remain explicit.
What turns an addition into uncontrolled scope creep? | Implementing extra work without the required assessment and authorization | Recording and approving a supported change | Comparing options before a decision | Updating the baseline after proper approval | Controlled changes can be legitimate; uncontrolled expansion bypasses the project's stated decision process.''',
    dialogue='''Nadia | Could we add one more report before launch? It would be useful for the operations review, and I hope it is a small enough change to fit.
Chen | Let us record the [[change request::A change request captures the proposed new report so its effort, impacts, and approval can be assessed.]]. The current plan already uses all twenty remaining person-days, so the report cannot be treated as an addition with no consequence.
Nadia | I understand it needs work. What does the estimate include? I do not want a build estimate that leaves testing to become a surprise later.
Chen | The [[effort estimate::The effort estimate is four person-days and explicitly includes testing rather than counting only construction.]] is four person-days including testing. The team has assessed two options using the planned people, with no extra staff or overtime assumed.
Nadia | Please explain those options in terms of the launch and what users will receive. That will help me compare the value instead of debating whether four is a big number.
Chen | The first is a [[scope substitution::Scope substitution replaces the existing four-person-day export feature with the new report under an approved change.]]. Defer the existing four-person-day export feature and use that capacity for the new report, retaining the launch date.
Nadia | That preserves the date but removes something people expected. We should make the lost capability visible rather than describe the option as simply fitting the report in.
Chen | Exactly. Assess the [[benefit impact::Benefit impact concerns the value affected when the planned export is deferred, even though the launch date is retained.]] of deferring the export. A date-preserving option still changes the release content and may affect the work users can do.
Nadia | What is the second option if the export remains important enough that we should not remove it from this release?
Chen | Keep all features and accept the assessed [[elapsed duration::Elapsed duration is the schedule time; this option extends it by two working days, distinct from four person-days of effort.]] increase of two working days. That is the team's schedule assessment, not a claim that four person-days always equals two days.
Nadia | Both options include the same testing expectation, correct? I would not want an apparently unchanged date achieved by quietly leaving out required checks.
Chen | Correct. We have not reduced [[test coverage::Test coverage remains within the assessed work; silently dropping required checks is not one of the options.]] to create either option. If someone proposes a different approach, it needs its own assessment rather than being smuggled into the estimate.
Nadia | We should compare the two options together: date retained with export deferred, or all features retained with a later launch. Neither means no trade-off.
Chen | That is the [[option comparison::The option comparison presents both alternatives on a common scope, time, and assumption basis.]]. Include the assumptions and any relevant consequences so the decision is about the actual alternatives, not a more attractive label.
Nadia | I am not choosing an option in this conversation yet. I need to confirm the export's importance with the operations lead before making the decision.
Chen | Then the [[approval record::The approval record must reflect the actual decision; no option has been authorized in this conversation.]] should remain pending. The delivery team should not infer an instruction to remove the export or move the date from our discussion of possibilities.
Nadia | When would you need the decision? If I leave it too long, the plan may change as the team completes work already assigned.
Chen | We must account for [[decision latency::Decision latency is the time taken to receive the needed choice, which can change the feasibility of the assessed options.]]. Confirm a decision checkpoint with the team; if the work has moved on, refresh the assessment rather than reuse an estimate whose assumptions no longer hold.
Nadia | Once the decision is made, we should tell stakeholders exactly what changed. I do not want one audience expecting the original export and another expecting the new report.
Chen | Issue the authorized [[baseline revision::A baseline revision updates the controlled plan after approval and communicates the selected scope and timing.]] and implementation instruction together. That gives the team and stakeholders one supported version of the release instead of several incompatible promises.''',
    transfer_title='A substitution changes scope',
    transfer_setup='A new feature needs three person-days. The assessed date-preserving option removes another three-person-day feature. Both cannot fit under the unchanged plan, and no option is approved.',
    transfer='''Sponsor: "The new feature requires three person-days of ___." | effort | Person-days measure the estimated work, not an automatic number of elapsed days.
Manager: "Keeping the date requires the assessed scope ___." | substitution | The stated option replaces one feature with another to release capacity.
Sponsor: "The original feature would be ___." | deferred | The date-preserving option removes that feature from the current delivery.
Manager: "The option still needs ___." | approval | The briefing says no option is authorized, so implementation cannot be assumed.'''))

BOOK['units'].append(unit(
    title='Status Reporting and Executive Updates',
    scene='Eight tasks finished, one date still threatened',
    skill='Produce a concise executive update that shows material threats, rating criteria, and decision needs without confusing task counts with delivery confidence.',
    brief='Project lead Sofia and sponsor James review a green report. Eight of ten tasks are complete, but the remaining access approval is needed by October 9 for an October 12 rehearsal before the planned October 16 launch. Approval is unconfirmed. The fictional reporting rules require amber when a material threat needs management attention and green only when delivery is on track without such a threat. No effort weights, cost data, approved recovery, or confirmed launch delay are supplied.',
    cast='Sofia | Project lead\nJames | Project sponsor',
    culture=('A color should invite the right conversation', 'Use the agreed reporting rules rather than choosing the color that sounds most reassuring. A material threat can require attention before a date is actually missed. A concise update should identify the dependency, consequence, owner, and needed action, not hide the problem behind a long list of completed work.'),
    a='''What does eight of ten establish? | Eighty percent of the task count is complete. | Eighty percent of all effort is complete. | The launch date is guaranteed. | The final access approval is already granted. | The brief supplies an unweighted task count, not effort weighting or complete delivery evidence.
Why does the access approval matter? | It is needed for the rehearsal that precedes launch. | It is unrelated to remaining work. | It proves all ten tasks are finished. | It replaces every release decision. | The stated chain links access due October 9 to rehearsal and the planned launch.
Which rating matches the supplied rules and facts? | Amber | Green because most task boxes are complete | Automatically red because any uncertainty means failure | No rating because the threat is not yet a confirmed delay | The rules require amber for a material threat needing management attention, which the open dependency creates.''',
    vocabulary='''status report | A periodic account of progress, outlook, problems, and decisions needed. | prepare a status report
status date | The date to which the reported information applies. | state the status date
reporting period | The time interval covered by a report. | define the reporting period
RAG rating | A red-amber-green status classification under stated criteria. | apply the RAG rating
green status | An on-track classification under the project's defined reporting rules. | justify green status
amber status | A warning classification requiring attention under the defined rules. | explain amber status
red status | A serious-problem classification under the defined reporting rules. | explain red status
delivery confidence | An assessment of the likelihood of achieving the intended delivery outcome. | assess delivery confidence
key milestone | A major event used to judge project progress or readiness. | report a key milestone
dependency owner | The person accountable for managing a required external or linked input. | identify the dependency owner
dependency due date | The date a required input must be available for the plan. | confirm the dependency due date
leading indicator | A signal of a possible future result or problem. | monitor a leading indicator
lagging indicator | A measure of an outcome that has already occurred. | distinguish a lagging indicator
exception report | A focused report on a deviation or condition requiring attention. | raise an exception report
percent complete | Completion expressed as a percentage under a specified measurement basis. | define percent complete
task-count completion | The share of listed tasks marked complete without weighting their effort. | qualify task-count completion
weighted progress | Progress calculated using stated effort, value, or other weights. | report weighted progress
earned value | The budgeted value of work actually completed under a defined measurement method. | distinguish earned value
planned value | The budgeted value of work planned by the status date. | compare with planned value
actual cost | Cost incurred for the work under the stated accounting basis. | report actual cost
cost performance index | Earned value divided by actual cost, commonly CPI. | interpret the cost performance index
schedule performance index | Earned value divided by planned value, commonly SPI. | interpret the schedule performance index
confidence qualifier | Wording that states a forecast's uncertainty or conditions. | add a confidence qualifier
executive ask | The specific decision or support requested from senior management. | state the executive ask''',
    precision='Eight of ten means 80% of task count, not necessarily 80% of effort, value, or readiness. Unequal task sizes and a controlling dependency make that distinction important. No earned-value or cost-performance result can be calculated from these counts alone.',
    precision_extra='Under these fictional rules, the open material threat warrants amber even before a confirmed launch delay. That does not prove October 16 is impossible. Report the planned date, uncertainty, dependency deadline, and required attention without inventing either certainty or failure.',
    phrases='''Lead with the exception | The access dependency threatens the planned launch sequence.
State the rating basis | Our rules require amber for a material threat needing management attention.
Keep progress visible | Eight of ten listed tasks are complete.
Qualify the percentage | That is task-count completion, not weighted effort.
Name the missing input | The access approval is still unconfirmed.
Give the needed-by date | We need that approval by October 9.
Connect the milestone | Rehearsal is planned for October 12 before the October 16 launch.
Avoid unsupported certainty | The launch is not yet confirmed delayed, but the threat is material.
Avoid a false green | Completed tasks do not remove the remaining dependency.
Name the owner | Identify who is responsible for obtaining the approval.
State the executive ask | We need help securing a timely decision through the authorized route.
Keep the baseline visible | The planned launch remains October 16 pending further evidence or approval.
Separate data gaps | These task counts do not provide earned-value or cost information.
Set the checkpoint | Confirm when the approval status will next be reviewed.
Report change honestly | Update the outlook when evidence changes, not when a color becomes uncomfortable.
Close in one sequence | Rating, dependency, impact, owner, needed action, next update.''',
    notes='''Green | Apply the actual criteria, not the mood of the meeting.
Complete | Complete under which definition and measurement method?
Eighty percent | State the denominator and any weighting.
Threatened | A material uncertainty, not necessarily a confirmed delay.
On track | Needs a supported outlook for the remaining work.
Escalation | A request for attention or decision, not automatic authorization.''',
    d='''Which executive summary is best supported? | Amber: access due October 9 is unconfirmed; rehearsal and launch are exposed; owner and decision follow-up needed. | Green: 80% of tasks means 80% certainty of launch. | Red: October 16 is definitely impossible on the supplied facts. | All work is complete except tasks that do not matter. | This summary follows the stated criteria and names the material dependency without inventing a final delay.
Why is "80% of the project is done" too broad? | Only unweighted task counts are supplied. | Eight divided by ten is not 80%. | Every task must have identical effort by definition. | The count proves all remaining tasks are optional. | Task-count completion does not establish weighted effort, value, or the importance of remaining work.
What would be needed to calculate CPI? | Earned value and actual cost on a defined basis | Only the number of green tasks | A list of meeting attendees | The planned launch date alone | CPI is earned value divided by actual cost, neither of which the task-count briefing supplies.
Which wording preserves uncertainty accurately? | October 16 remains planned, but the unconfirmed dependency creates a material threat. | October 16 is guaranteed because it is printed in the plan. | October 16 has definitely failed because a threat exists. | No update is needed until after the date is missed. | The wording distinguishes the planned date from confidence in meeting it.''',
    dialogue='''James | The report is green and shows eight of ten tasks complete. That sounds encouraging, but I see the access approval is still open. Does it affect the rehearsal?
Sofia | Yes. Our [[RAG rating::The RAG rating must follow the stated criteria, including material threats, rather than simply count completed tasks.]] should reflect that dependency. The supplied rules require amber when a material threat needs management attention, even before a milestone is confirmed late.
James | Then the eight completed tasks are useful progress, but they do not settle whether the remaining sequence can happen on time.
Sofia | Exactly. That is [[task-count completion::Task-count completion is eight finished tasks out of ten, without weighting their size or importance.]], not eighty percent of all effort or readiness. The remaining tasks may differ in size, and one contains the input needed for rehearsal.
James | Please state the dates in the short update. I need to see the point at which the missing approval affects the rest of the plan.
Sofia | The [[dependency due date::The dependency due date is October 9, when approval is needed to support the planned rehearsal.]] is October ninth. Rehearsal is planned for October twelfth, ahead of the October sixteenth launch, so the approval cannot remain an unrelated footnote.
James | We do not yet know that launch will be late, though. I want the report to show the threat without declaring a final outcome the evidence does not establish.
Sofia | Use a [[confidence qualifier::A confidence qualifier distinguishes the planned date from the uncertainty created by the unresolved dependency.]]: October sixteenth remains planned, but the access dependency is unconfirmed and threatens the sequence. No recovery or revised date has been approved.
James | Who is responsible for obtaining the approval? A clear owner would help me understand where support is needed instead of sending a general chase to everyone.
Sofia | Identify the [[dependency owner::The dependency owner is accountable for managing the required access input and its follow-up.]] and the authorized decision route. The report should say who is following up, what decision is required, and when the next status check will occur.
James | I can help bring the decision to the right forum, but I cannot treat the urgency as permission to bypass the access approval itself.
Sofia | That is the appropriate [[executive ask::The executive ask requests support for a timely authorized decision, not permission to bypass the required control.]]. We need support securing a timely decision through the proper route, not an assurance that an unapproved input can be treated as available.
James | The report also uses the words value delivered beside the eighty-percent figure. We do not have an earned-value calculation here, do we?
Sofia | No. [[Earned value::Earned value measures budgeted completed work under a defined method; unweighted task counts do not provide it.]] needs its defined work and budget basis. The task count supplies neither that measure nor the actual cost needed for a cost-performance calculation.
James | So the update should be shorter but more precise: real progress, the material threat, the needed decision, and the timing. We can remove the unsupported value label.
Sofia | An [[exception report::An exception report focuses attention on the condition needing action while preserving its relevant progress context.]] can make that concise. It should expose the access issue without forcing the sponsor to discover it inside a long list of activities that are already finished.
James | I agree that amber follows our rules. It is not a punishment for the team; it tells us where management attention can still make a difference.
Sofia | Correct. [[Delivery confidence::Delivery confidence concerns the remaining path to the intended outcome, not merely how many historical tasks are complete.]] depends on the remaining work and dependencies, not just historical completion. The rating should change when the relevant evidence changes.
James | Please correct the report and confirm the next checkpoint. Keep the October sixteenth baseline visible while distinguishing it from any later forecast we may need.
Sofia | I will state the [[status date::The status date identifies when the report's facts and outlook apply, making later changes traceable.]] and current approval position, change the rating to amber, and include the owner and decision follow-up. That gives the next audience the same accurate picture.''',
    transfer_title='Counted progress does not remove a blocker',
    transfer_setup='Six of eight tasks are complete. A material dependency remains open. The local rules require amber for that threat, and no final delay is confirmed.',
    transfer='''Lead: "Task-count completion is ___ percent." | seventy-five | Six divided by eight equals seventy-five percent of the listed task count.
Sponsor: "That does not establish weighted ___." | progress | No effort or value weights are supplied for the eight tasks.
Lead: "Under our rules, the rating is ___." | amber | The stated local rules assign amber to the material unresolved dependency.
Sponsor: "A final delay is not yet ___." | confirmed | The briefing identifies a threat without establishing a final delay.'''))

BOOK['units'].append(unit(
    title='Vendor and Cross-Functional Delivery',
    scene='Complete on the vendor side, not yet accepted',
    skill='Resolve a delivery-status disagreement by linking agreed criteria to evidence, distinguishing missing proof from failure, and naming the acceptance authority.',
    brief='Vendor lead Marta says a workflow deliverable is complete. Client acceptance lead Leo can verify four of six agreed criteria, but finds no evidence for C5, audit-log export, or C6, role-based access behavior. The missing evidence does not itself prove those functions fail. No acceptance or waiver is recorded, and Leo cannot waive criteria alone. Contractual payment consequences have not been assessed. Leo and Marta must agree the evidence handoff without adding new scope or treating the delivery claim as acceptance.',
    cast='Leo | Client acceptance lead\nMarta | Vendor delivery lead',
    culture=('Be firm about evidence without escalating the tone', 'A vendor can mean development complete while the client means accepted against the agreed criteria. State the missing evidence and identifiers precisely. This keeps the discussion focused on the original agreement instead of implying new requirements, accusing someone of failure without proof, or approving an incomplete record.'),
    a='''How many criteria currently have verified evidence? | Four of six | All six | Two of six | None | Leo can verify four criteria; C5 and C6 lack evidence in the current record.
What follows from missing evidence for C5 and C6? | Their compliance has not yet been demonstrated in the record. | Both functions are proven defective. | Both criteria are automatically waived. | The client has accepted all work. | Missing proof leaves acceptance unresolved without establishing that the underlying functions fail.
Who may waive the criteria under the supplied facts? | The appropriate authority, which Leo cannot replace alone | Leo automatically because the vendor says complete | Any observer at a demonstration | No authorization is ever relevant | The brief explicitly says Leo cannot waive the criteria alone and records no waiver.''',
    vocabulary='''statement of work | The agreed description of the vendor's work and deliverables, commonly SOW. | refer to the statement of work
deliverable register | A record of promised outputs and their current status. | update the deliverable register
acceptance plan | The arrangement for checking and deciding acceptance of outputs. | confirm the acceptance plan
acceptance authority | The person or body empowered to accept the deliverable. | identify the acceptance authority
acceptance evidence | Information demonstrating whether the agreed criteria are met. | supply acceptance evidence
requirements matrix | A table linking requirements to identifiers, status, or supporting information. | review the requirements matrix
evidence gap | Missing information needed to support a conclusion. | identify an evidence gap
test result | The recorded outcome of a defined test. | review a test result
test environment | The conditions and setup in which a test is performed. | identify the test environment
test data | The inputs used in a defined test. | specify the test data
expected result | The outcome required by the applicable test or criterion. | compare with the expected result
actual result | The outcome observed when the defined test is performed. | record the actual result
defect | A departure from a specified requirement or expected behavior. | log a verified defect
nonconformance | Failure to meet an applicable specified requirement. | document a nonconformance
punch list | A list of remaining items to address before a defined completion point. | maintain a punch list
waiver | An authorized exception to a specified requirement under the governing rules. | request a waiver
conditional acceptance | Acceptance limited by explicit unresolved conditions under the relevant authority. | document conditional acceptance
formal acceptance | Recorded acceptance by the authorized party under the applicable process. | confirm formal acceptance
handover package | The documents, outputs, and evidence transferred to the receiving team. | complete the handover package
completion claim | A party's statement that its work is finished. | verify a completion claim
commercial consequence | An effect on contractual or financial obligations requiring the governing terms. | assess commercial consequences
contract owner | The person responsible for managing the relevant agreement. | consult the contract owner
acceptance record | The documented acceptance decision and its basis or conditions. | retain the acceptance record
evidence handoff | Transfer of identifiable supporting information to the reviewer. | agree the evidence handoff''',
    precision='Four of six criteria have verified evidence. C5 and C6 are unverified in this record, not automatically failed or waived. A vendor completion claim and formal client acceptance are different statuses; neither substitutes for the other.',
    precision_extra='Request evidence against the agreed criteria, including the relevant test context, expected result, and actual result. Do not invent new requirements during acceptance. Payment or contractual remedies need the governing terms and proper authority, not an assumption from a status label.',
    phrases='''Acknowledge the claim | I understand that your team considers development complete.
State the evidence position | We can verify four of the six agreed criteria.
Name the gaps | Evidence for C5 and C6 is missing from the handover package.
Avoid a false failure | Missing evidence does not itself establish a failed function.
Keep scope stable | We are asking for proof against existing criteria, not adding requirements.
Request traceability | Link each result to its criterion identifier and tested version.
Clarify the test context | Identify the environment, inputs, expected result, and actual result.
Separate the statuses | Delivered is not the same as formally accepted.
Keep the authority visible | I cannot waive these criteria on my own.
Avoid implied acceptance | A demonstration invitation is not an acceptance record.
Qualify conditional acceptance | Any conditional acceptance needs proper authority and explicit conditions.
Set the evidence deadline | Confirm when the missing evidence will be available for review.
Avoid premature closure | Keep the two criteria open until the evidence is assessed.
Handle terms correctly | Refer payment consequences to the contract owner and governing agreement.
Confirm the handoff | Name the sender, reviewer, file location, and next checkpoint.
Close with the actual state | Four verified, two awaiting evidence, acceptance not yet recorded.''',
    notes='''Complete | Name whose work stage and which completion definition.
Unverified | Not demonstrated; it does not automatically mean defective.
Failed | Requires evidence against the relevant criterion.
Waived | Requires an actual authorized exception.
Conditional | Keep the condition visible instead of shortening it to accepted.
Paid | A commercial status whose relation to acceptance depends on the agreement.''',
    d='''Which response preserves both accuracy and scope? | Please supply evidence for the existing C5 and C6 criteria; we are not adding new requirements. | Both functions are proven failures because evidence is missing. | Every function is accepted because the vendor is confident. | We can add unrelated requirements without a change discussion. | The response requests the missing proof against the agreed scope without inventing failure or extra work.
What should an evidence package make traceable? | Criterion, tested version, context, and actual result against expectation | Only a slide saying done | The vendor's preferred payment date alone | The number of people who attended a meeting | Identifiable test context and results allow the reviewer to assess the actual agreed criterion.
Which acceptance status is supported now? | No acceptance or waiver is recorded. | Unconditional formal acceptance is complete. | C5 and C6 have been waived by silence. | Leo has unlimited unilateral waiver authority. | The brief explicitly leaves acceptance and waiver absent and limits Leo's authority.
What should be said about payment consequences? | They need assessment against the agreement by the appropriate owner. | Missing evidence automatically cancels every payment in all contracts. | A completion claim proves immediate payment under every agreement. | The project team may invent a new commercial term. | The supplied facts do not establish the contractual payment rules or authorize a commercial conclusion.''',
    dialogue='''Marta | Our team has marked the workflow deliverable complete. I thought that meant we could close the delivery item, but your acceptance sheet still shows two open entries.
Leo | I see the [[completion claim::A completion claim is the vendor's statement of finished work, distinct from the client's acceptance evidence.]]. We can verify four of the six agreed criteria; the handover package has no evidence for C5 or C6.
Marta | Those are audit-log export and role-based access behavior. Are you saying the functions have failed, or that you cannot find the supporting results?
Leo | I am identifying an [[evidence gap::An evidence gap means the supporting information is missing, not that the function has been proven defective.]]. Missing results do not prove the functions fail, but they do prevent us from treating those criteria as demonstrated in the current record.
Marta | That distinction helps. I was concerned the review was adding new scope after the team had finished development and prepared the handover.
Leo | We are referring to the existing [[statement of work::The statement of work and agreed criteria define the original delivery scope, not new requirements invented during acceptance.]] and agreed criteria. The request is for evidence supporting C5 and C6, not additional functionality outside that agreement.
Marta | What would make the package usable for your reviewers? We may have screenshots and test records, but they need to be connected to the right version.
Leo | Use the [[requirements matrix::The requirements matrix connects each criterion identifier with the relevant version, status, and supporting result.]] to identify the criterion, tested version, and result. Reviewers should not have to infer which requirement a screenshot is intended to demonstrate.
Marta | We should include the environment and test inputs too. A result from an unrelated setup may not demonstrate the behavior your agreed test expects.
Leo | Exactly. State the [[actual result::The actual result is the recorded behavior observed in the identified test, to be compared with the expected result.]] alongside the expected result and context. That lets us assess the evidence rather than accept a general statement that the test passed.
Marta | If the evidence takes another day to assemble, could you simply waive those two criteria so the handover record can be closed now?
Leo | I cannot issue a [[waiver::A waiver is an authorized exception; Leo does not have unilateral authority to remove the two criteria.]] on my own. The proper authority would need to decide any exception under the agreement; a missing document does not itself justify pretending the requirement disappeared.
Marta | Could conditional acceptance be considered instead? I am asking about the process, not assuming that it has already been granted.
Leo | Any [[conditional acceptance::Conditional acceptance needs the relevant authority and explicit conditions; it is not established by discussing the option.]] needs the proper decision and clear terms. We have neither that decision nor a waiver recorded, so the current status must remain accurate.
Marta | Understood. I will have our test lead assemble the C5 and C6 evidence and confirm the file location and delivery time for your review.
Leo | That makes the [[evidence handoff::The evidence handoff specifies who sends the missing results, where they are available, and when review can occur.]] actionable. Please confirm the sender, criterion identifiers, tested version, and when the reviewer can access the package, rather than sending another general completion message.
Marta | Our commercial team may ask what this means for invoicing. I should not infer a payment rule from the technical acceptance discussion alone.
Leo | Refer that to the [[contract owner::The contract owner must assess commercial consequences against the governing agreement rather than a generic completion label.]] and the governing terms. I am describing the evidence and acceptance status, not inventing a contractual payment outcome.
Marta | I will update our status to development complete, with client evidence review outstanding for C5 and C6. That should explain why the records currently differ.
Leo | Good. The [[acceptance record::The acceptance record should capture the actual authorized decision after evidence review, not convert delivery status into acceptance.]] can be completed when the applicable review and decision occur. For now: four verified criteria, two awaiting evidence, and no acceptance or exception yet recorded.''',
    transfer_title='Unverified does not mean failed',
    transfer_setup='Five criteria are agreed. Evidence supports four; the fifth has not been reviewed because its result is missing. No waiver or acceptance is recorded.',
    transfer='''Client: "Four criteria have supporting ___." | evidence | The briefing says four of the five criteria have demonstrated support.
Vendor: "The fifth remains ___." | unverified | Its result is missing, so compliance has not yet been demonstrated.
Client: "That does not itself prove a ___." | failure | Missing information is not evidence that the underlying function failed.
Vendor: "No acceptance has been ___." | recorded | The supplied facts explicitly leave the acceptance record absent.'''))

BOOK['units'].append(unit(
    title='Post-Implementation Review',
    scene='Turn communication was poor into a testable action',
    skill='Convert a vague lesson into a specific process change with an owner, deadline, adoption check, and separate effectiveness review.',
    brief='Review facilitator Hana and project-office lead Sanjay examine five scope handoffs from a completed project. Three lack recorded recipient acknowledgment before work began, and two tasks were reworked using an older specification. The notes repeatedly say communication was poor but contain no improvement action. The record does not prove a single cause. Sanjay proposes a revised handoff record by October 10 and a check of the next five handoffs. No pilot result is available yet.',
    cast='Hana | Review facilitator\nSanjay | Project-office lead',
    culture=('A lesson needs somewhere to go', 'A review can sound candid while leaving the next project unchanged. Name the observed process gap and a concrete improvement, then distinguish whether people adopt the new process from whether it improves the outcome. Keep accountability without inventing a single culprit or a causal conclusion the record cannot support.'),
    a='''How many reviewed handoffs lacked recorded acknowledgment before work? | Three of five | All five | Two of ten | None | The briefing identifies three missing acknowledgments among five examined handoffs.
What is established about the rework? | Two tasks used an older specification and were reworked. | All rework was proven to have a single cause. | The pilot eliminated every future error. | No specification version was ever involved. | The record describes two reworked tasks but does not establish a complete causal explanation.
What is the status of the proposed improvement? | Proposed, with no pilot result yet | Already proven effective over many projects | Fully adopted in the next five handoffs | A completed organization-wide policy audit | The briefing supplies a proposed action and review plan, not results.''',
    vocabulary='''post-implementation review | An assessment after delivery of results, process, and lessons. | conduct a post-implementation review
after-action review | A structured discussion of what happened and what to improve. | facilitate an after-action review
lessons log | A record of learning from project experience. | maintain the lessons log
actionable lesson | Learning translated into a specific usable change. | formulate an actionable lesson
contributing factor | A condition that may have helped produce an outcome. | investigate a contributing factor
root-cause hypothesis | A proposed explanation for an underlying cause that needs evidence. | test a root-cause hypothesis
causal claim | A statement that one factor produced an outcome. | qualify a causal claim
blameless review | A learning-focused review that avoids unsupported personal blame without removing accountability. | hold a blameless review
knowledge transfer | Passing usable information or experience to another team. | improve knowledge transfer
improvement backlog | A prioritized list of changes intended to improve future work. | maintain an improvement backlog
corrective action | An action addressing a detected problem or its causes under the stated process. | assign a corrective action
preventive action | An action intended to reduce the chance of a future problem. | define a preventive action
process owner | The person accountable for a defined working process. | identify the process owner
due date | The agreed date by which a task should be completed. | set the due date
adoption check | A check that the intended process is actually being used. | perform an adoption check
effectiveness review | An assessment of whether the change achieves its intended effect. | conduct an effectiveness review
process measure | An indicator of how work is performed. | define a process measure
outcome measure | An indicator of the result produced by the work. | distinguish an outcome measure
baseline value | The reference measurement before the assessed change. | establish the baseline value
comparison window | The defined period or cases used for comparison. | specify the comparison window
sample size | The number of observations in an assessment. | state the sample size
version reference | The identifier of the document or specification used. | confirm the version reference
recipient acknowledgment | Confirmation from the receiving person that the specified handoff was received. | obtain recipient acknowledgment
closure criterion | The condition required to mark an improvement action complete. | define the closure criterion''',
    precision='Two of five handoffs had recorded acknowledgment, a 40% baseline on that process measure. A future four of five would be 80%, an increase of 40 percentage points. It would still miss a five-of-five target and would not alone prove less rework.',
    precision_extra='No pilot result is supplied in the main case. The revised record, its use, and its effectiveness are separate checks. A small before-and-after sample can reveal a process change without establishing that it alone caused an outcome difference.',
    phrases='''Replace the vague label | Three of five handoffs lacked recorded acknowledgment before work began.
State the linked observation | Two tasks were reworked using an older specification.
Limit the causal claim | The record does not establish one exclusive cause.
Name a concrete change | Add the scope identifier, version, owner, and recipient acknowledgment to the handoff record.
Assign the owner | Sanjay will prepare the revised record by October 10.
Define the pilot | Check the next five scope handoffs.
State the process target | Each of the five should have the required record before work starts.
Separate implementation | Publishing the template does not show that teams use it.
Check adoption | Review the actual handoff records, not just training attendance.
Measure the outcome separately | Track version-related rework on a stated comparison basis.
Keep the sample visible | Five cases are a small review sample, not universal proof.
Avoid percentage confusion | Moving from 40% to 80% is a 40-percentage-point increase.
Preserve incomplete status | Four of five would show improvement but miss the five-of-five target.
Plan the effectiveness review | Set who will check whether the change reduces the intended problem.
Close with evidence | Mark the action complete only against its defined closure criterion.
Transfer the learning | Put the tested change where the next project will actually use it.''',
    notes='''Poor | Too broad to identify a repeatable improvement by itself.
Cause | Needs evidence stronger than a nearby event or plausible story.
Published | A document exists; it may not yet be used.
Adopted | People use the process; the desired outcome still needs checking.
Effective | Specify the outcome, evidence, and comparison.
Learned | A recorded lesson becomes useful when it changes relevant future work.''',
    d='''Which action is most specific? | Sanjay revises the handoff record by October 10 and checks required fields in the next five handoffs. | Everyone should communicate better somehow. | All teams should try harder without a review date. | The same vague lesson should be copied into every future report. | The action identifies an owner, deliverable, deadline, and observable follow-up sample.
Why does a published template not prove effectiveness? | Existence, use, and effect are different questions. | Every published document automatically prevents mistakes. | A template makes outcome measurement impossible. | Publication proves a single root cause retrospectively. | The team must examine adoption and outcomes separately from the creation of the document.
A later pilot records acknowledgment in four of five handoffs. What is the process result? | 80%, above the 40% baseline but below the five-of-five target | 40%, exactly the baseline | 100%, because four is close to five | Proof that all future rework is eliminated | Four divided by five is 80%; it improves the observed rate without meeting the full target.
What does a small improved before-and-after result establish by itself? | An observed difference in the measured cases, not proof of an exclusive cause | A universal guarantee for every future project | Proof that no other factor changed | A reason to remove the sample size from reporting | A small comparison can show a change without isolating causality or supporting a universal guarantee.''',
    dialogue='''Hana | The review notes say communication was poor three times, but I cannot find an action that would change the next project. What did the records actually show?
Sanjay | Three of five handoffs lacked recorded [[recipient acknowledgment::Recipient acknowledgment is the receiving person's confirmation, missing before work began in three reviewed cases.]] before work started. We also found two tasks that used an older specification and had to be reworked.
Hana | Those are more useful observations than the broad label. Do they prove that the missing acknowledgment was the sole cause of the rework?
Sanjay | No. That would be an unsupported [[causal claim::A causal claim would assert that the missing acknowledgment produced the rework, which this record does not establish exclusively.]]. The records suggest a process gap to investigate, but they do not exclude other contributing factors.
Hana | Let us define a change that addresses the gap without pretending the analysis is finished. What should the handoff record contain that it does not reliably show now?
Sanjay | Add the scope identifier, [[version reference::The version reference identifies which specification the receiving team is meant to use.]], responsible owner, and recipient acknowledgment before work starts. That makes the transferred instruction identifiable rather than leaving the receiver to infer which document applies.
Hana | Who will produce the revised record, and by when? A lesson saying someone should improve the template may disappear as soon as the project closes.
Sanjay | I will be the [[process owner::The process owner is accountable for the defined handoff process and its proposed improvement, here Sanjay.]] and prepare the revision by October tenth. Record that commitment with the deliverable, not simply assign it to the project office.
Hana | Then we need to find out whether people use it. A new template in a folder can look like completion while the actual handoffs continue unchanged.
Sanjay | Run an [[adoption check::An adoption check examines whether the revised process appears in actual handoff records, not merely whether the template exists.]] on the next five scope handoffs. Check the required fields and acknowledgment before work starts, rather than counting how many people attended a briefing.
Hana | What is the comparison point? We need a clear measure so a later reviewer can tell whether the process changed.
Sanjay | The [[baseline value::The baseline value is two acknowledged handoffs out of five, or 40%, under the defined process measure.]] is two of five with recorded acknowledgment, or forty percent. The pilot target is five of five, with the sample and timing basis stated.
Hana | Suppose the pilot later shows four of five. That would be progress, but the target would still be unmet, and it would not tell us everything about rework.
Sanjay | Correct. The [[process measure::The process measure tracks recorded acknowledgment, which is distinct from an outcome such as less version-related rework.]] would be eighty percent. That is forty percentage points above baseline, not evidence that every intended outcome has been achieved.
Hana | We should measure version-related rework separately. Otherwise the team may comply with the form while still using the wrong specification during the task.
Sanjay | Set an [[effectiveness review::An effectiveness review tests whether the adopted change improves the intended result rather than stopping at procedural compliance.]] with a responsible reviewer and comparison window. Adoption matters, but the intended result needs its own evidence and a clear measurement basis.
Hana | Five cases is also a small sample. We can use it to spot a problem with the process, but not claim a universal result from a short pilot.
Sanjay | State the [[sample size::Sample size is the number of observed handoffs and limits the strength of broader conclusions.]] whenever reporting the result. Keep other possible influences visible instead of treating a before-and-after difference as proof that our change was the only cause.
Hana | That gives us an action, an owner, a deadline, and two different checks: whether the process is used and whether it helps. How should we close it?
Sanjay | Define the [[closure criterion::The closure criterion specifies the evidence required to complete the improvement action, keeping implementation and effectiveness distinct.]] for each stage. We should not mark the entire lesson resolved merely because the template was published; the follow-up records must show what was implemented and what was actually learned.''',
    transfer_title='A better rate, an unmet target',
    transfer_setup='The baseline has recorded acknowledgment in three of six handoffs. A later pilot has five of six, against a six-of-six target. Rework outcomes have not yet been measured.',
    transfer='''Reviewer: "The baseline rate was ___ percent." | fifty | Three acknowledged handoffs divided by six gives a fifty-percent baseline.
Owner: "The pilot has ___ acknowledged handoffs out of six." | five | The supplied pilot result records acknowledgment in five of the six cases.
Reviewer: "The six-of-six target remains ___." | unmet | One pilot handoff still lacks acknowledgment, so the stated target was not achieved.
Owner: "Rework effectiveness is not yet ___." | measured | The briefing explicitly leaves rework outcomes without measurement.'''))
