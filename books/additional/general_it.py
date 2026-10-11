"""Additional IT conversations: recovery, offboarding, and certificate renewal."""
from books.supplements import scenario

SCENARIOS = [
scenario(
    title='The backup succeeded; the recovery exercise did not',
    skill='Explain a recovery-test shortfall using distinct time and data-loss measures.',
    setup='A fictional recovery exercise starts at 10 a.m. The latest usable backup represents 2 a.m. data. Service is restored at 1:20 p.m. The approved objectives are a four-hour recovery point objective and a two-hour recovery time objective.',
    cast='Ravi|Systems administrator\nLeah|Service owner',
    dialogue='''
Leah|The backup dashboard is green. Can I mark the recovery exercise successful?
Ravi|Not against both objectives. We restored service, but the [[elapsed time::Elapsed time is the interval actually taken, here from 10 a.m. to 1:20 p.m.]] was three hours and twenty minutes.
Leah|Our target is two hours. Where did the extra time go?
Ravi|Most of it went into restoring the data. I have separate timings for provisioning, restoration, and application checks.
Leah|And how current was the recovered data?
Ravi|The [[recovery point::Recovery point identifies the time represented by recovered data, not when restoration finished.]] was 2 a.m., eight hours before the exercise started.
Leah|So we also missed the four-hour data-loss objective.
Ravi|Yes. The job completed, but the available recovery point was older than the business requirement allows.
Leah|Can we solve that by scheduling more backups?
Ravi|That may help, but first we should check why the later copy wasn't usable. I don't want to prescribe a fix before that review.
Leah|Agreed. What evidence should go in the report?
Ravi|The selected copy, its data timestamp, the [[restore duration::Restore duration is the time spent recovering data, one part of the overall recovery time.]], and the application validation results.
Leah|Were the recovered records actually checked, or did we stop when the service started?
Ravi|We checked the agreed sample and the totals for that backup. The checks passed within that defined scope.
Leah|Then the summary needs both the successful restoration and the missed objectives.
Ravi|I'll show them separately in the [[test record::Test record preserves the conditions, observations, and results of the recovery exercise.]]. No overall green status.
Leah|Who will propose the corrective work?
Ravi|I'll investigate the unusable copy. The storage team will review the duration. We'll bring you options with cost and [[dependencies::Dependencies are prerequisites or other work that the proposed corrective actions rely on.]].
Leah|Good. We'll choose a plan, then schedule another exercise.
Ravi|And define the [[acceptance criteria::Acceptance criteria specify the conditions the next exercise must meet before it can pass.]] before rerunning it, including both objectives and the data checks.
''',
    transfer_title='A weekly status report confuses backup and recovery',
    transfer_setup='A manager wants to report that nightly backups prove the application can recover within two hours. No timed recovery test has established that claim.',
    transfer='''
Manager: Can I describe two-hour recovery as ___?|verified|Verified means supported by completed checks, which this claim currently lacks.
Administrator: Not yet. We have backup-job results, not a timed ___ test.|recovery|Recovery tests whether the service and data can be restored as required.
Manager: I'll label two hours as the agreed ___ instead.|objective|Objective describes a required target rather than an already measured result.
Administrator: Good. The exercise will provide the missing ___ evidence.|performance|Performance evidence shows what the recovery process actually achieved under test conditions.
'''),
scenario(
    title='An employee leaves, but three workflows still use the account',
    skill='Coordinate offboarding while separating identity access from business continuity.',
    setup='An approved offboarding request ends a staff member\'s access at 5 p.m. Friday. A report subscription, a shared mailbox workflow, and a scheduled integration need new owners. Records must follow the organization\'s retention instructions.',
    cast='Tara|IT coordinator\nBen|Department manager',
    dialogue='''
Ben|Can we leave Maya's account active for a week? Her reports still run from it.
Tara|The approved [[cutoff::Cutoff is the specified time after which the departing employee's access must end.]] is Friday at five. Let's transfer the work instead of extending personal access informally.
Ben|I hadn't realized the report subscription belonged to her rather than the team.
Tara|That's one item. There's also the shared mailbox workflow and a scheduled integration. Who can take responsibility for each?
Ben|I can own the reports. Jordan can coordinate the mailbox. I don't know enough about the integration.
Tara|I'll contact its service owner. A named [[service account::Service account means an identity for an automated process rather than a departing employee's personal identity.]] may be appropriate, subject to the approved design and access review.
Ben|Could Jordan simply use Maya's password while we sort this out?
Tara|No. We'll assign authorized access to Jordan's own identity. We need to know who performed each action.
Ben|Understood. Should I ask Maya to delete her old project files before she leaves?
Tara|Don't request deletion. The [[retention policy::Retention policy determines how records are kept and disposed of; departure alone does not authorize deletion.]] and any applicable hold instructions govern those records.
Ben|I'll leave the records intact and identify the business owners.
Tara|Thanks. The access change and the records decision are separate tasks in the checklist.
Ben|How do we know the transferred report still works?
Tara|Run the approved [[validation::Validation checks that the transferred workflow meets its intended requirements under the new ownership.]] with its new owner and delivery list. A changed owner field isn't enough.
Ben|I'll verify the report output. What happens if the integration isn't ready by Friday?
Tara|We escalate that continuity issue to the authorized owner. We don't silently cancel the access cutoff.
Ben|Please put that on the handover so the Friday team sees it.
Tara|I will, with an [[action owner::Action owner identifies the person responsible for carrying out a particular follow-up task.]] and status for each unresolved item.
Ben|Then we have three workflow transfers, one access deadline, and a separate records check.
Tara|Exactly. I'll send the [[handover checklist::Handover checklist records the tasks and confirmations needed to transfer responsibility without omissions.]] for you to confirm today.
''',
    transfer_title='A report arrives after its owner has left',
    transfer_setup='A recurring report still shows the former employee as its owner. The new manager has not verified its recipients or output.',
    transfer='''
Manager: The report arrived, so can we close the ___ task?|transfer|Transfer refers to moving workflow responsibility, which requires more than successful delivery.
IT: First confirm the new owner and the authorized ___ list.|recipient|Recipient identifies who is permitted and expected to receive the report.
Manager: I'll also compare the output with the agreed ___ criteria.|validation|Validation criteria state what the new owner must check before accepting the workflow.
IT: Then record the result before marking the handover ___.|complete|Complete means all agreed handover conditions have been satisfied and recorded.
'''),
scenario(
    title='The certificate renews tonight, but nobody owns the alert',
    skill='Clarify technical ownership and communicate a preventive change.',
    setup='The customer portal\'s TLS certificate expires in six days. Automated renewal failed last night. The infrastructure team manages the renewal service; the application team validates the portal. No customer outage has been reported.',
    cast='Nia|Infrastructure engineer\nSol|Application owner',
    dialogue='''
Sol|I received an expiry warning for the portal. Is the site already down?
Nia|No outage is reported. The current [[certificate::Certificate is the signed digital credential used in the portal's secure connection.]] remains valid for six days, but last night's renewal failed.
Sol|I thought renewal was automatic. Why does this need our team?
Nia|Automation still needs monitoring and an owner when it fails. Infrastructure owns the renewal service; your team checks the application afterward.
Sol|What failed: issuance or installation?
Nia|The log shows issuance didn't complete. We haven't reached installation. I'm checking the approved renewal workflow now.
Sol|Can I tell Support there may be a planned outage?
Nia|Let's first define the [[change window::Change window is the agreed period for planned service work, not a prediction of an outage.]] and expected impact. Don't announce downtime we haven't established.
Sol|Fair. What do you need from us today?
Nia|Confirm the portal endpoints and a tester. We'll document the renewal result and the certificate presented by each endpoint.
Sol|Our health check only confirms that the page responds.
Nia|Then add the approved TLS checks to the [[validation plan::Validation plan specifies the checks needed to establish that the change works as intended.]]. A page response alone won't confirm the intended certificate is in use.
Sol|Should users ignore a browser warning if one appears during the work?
Nia|No. Route any warning through Support. We shouldn't ask users to bypass a security warning to keep working.
Sol|Who gets the next failed-renewal alert?
Nia|The infrastructure [[on-call::On-call identifies the person or team assigned to respond during the relevant period.]] contact, with application ownership listed as the escalation contact.
Sol|I'll verify that contact list. The current alert reached a mailbox nobody checks overnight.
Nia|That explains the notification gap, not necessarily the renewal failure. I'll track the two issues separately.
Sol|Please include both in the [[change record::Change record documents the planned work, responsibilities, checks, and relevant evidence.]] so we don't fix only the certificate.
Nia|Agreed. We'll close it after the renewal, endpoint checks, and a tested alert [[handoff::Handoff transfers the alert and response responsibility to a confirmed receiving owner.]].
''',
    transfer_title='Support receives a certificate-warning screenshot',
    transfer_setup='A user reports a browser warning after the planned renewal. Support must gather evidence and escalate without asking the user to bypass it.',
    transfer='''
User: Should I click past the ___ to reach the portal?|warning|Warning is the browser's security notice, not a routine confirmation to dismiss.
Support: No. Please report the exact portal ___ through our support channel.|address|Address identifies the endpoint involved and helps distinguish different portal routes.
User: I'll include the time and the wording of the ___.|message|Message supplies the observed error text rather than a guessed diagnosis.
Support: I'll escalate it to the named ___ and keep you updated.|owner|Owner is the person responsible for investigating and coordinating the issue.
'''),
]
