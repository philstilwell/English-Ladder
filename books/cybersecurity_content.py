"""Original, bounded workplace-English cases for cybersecurity professionals."""
from books.authoring import unit

BOOK = dict(
    slug='cybersecurity', title='Cybersecurity English',
    cover_label='DETECTION / RESPONSE / ACCESS / RISK',
    cover_title='Cybersecurity', cover_size=32,
    tagline='Report the evidence. Explain the exposure.',
    audience='For security analysts, engineers, risk specialists, and cross-functional response teams.',
    map_intro='Eight security conversations connect technical observations with defensible conclusions, authorized action, and clear business decisions.',
    notes_title='Precision matters before certainty arrives.',
    notes_intro='Security teams often speak while the evidence is incomplete. An unusual login is not automatically an intrusion; a containment action is not proof of recovery. These conversations practice the language needed to act promptly while keeping observations, hypotheses, authority, and business consequences distinct.',
    field_notes=[
        ('Name the evidence first', 'Give the source, event time, and observed behavior before the interpretation. Preserve uncertainty without hiding the need to act.', '"The log records a successful sign-in; authorization is not yet verified."'),
        ('Bound a negative finding', 'A search result applies to the sources and period actually checked. Missing records cannot prove that nothing happened.', '"We found no matching event in the available application logs."'),
        ('Separate action from outcome', 'Proposed, approved, completed, and verified describe different states. Identify who can authorize a disruptive response.', '"Isolation is complete; eradication and recovery are not yet confirmed."'),
        ('Translate risk into a decision', 'Connect a specific exposure to a plausible business consequence, then state the requested action and what remains uncertain.', '"The proposal addresses delayed payroll recovery, not every cyber risk."')],
    scope_note='Original fictional English practice, not a security certification, incident-response playbook, legal opinion, or authorization to test systems. Follow the responsible team, approved procedures, evidence-handling rules, and applicable requirements. All organizations, incidents, figures, priorities, and control criteria in the cases are invented.',
    sources=[
        dict(title='NIST. SP 800-61 Revision 3: Incident Response Recommendations and Considerations, April 2025.', url='https://csrc.nist.gov/pubs/sp/800/61/r3/final', note='Background for incident-response vocabulary and the distinction between detection, response, and recovery. The case actions and authority arrangements are fictional.', checked='30 September 2026'),
        dict(title='CISA. Known Exploited Vulnerabilities Catalog.', url='https://www.cisa.gov/known-exploited-vulnerabilities-catalog', note='Background for using observed exploitation as one prioritization input. No invented vulnerability in this book is represented as an actual catalog entry.', checked='30 September 2026'),
        dict(title='OWASP. Threat Modeling Cheat Sheet.', url='https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html', note='Background for system modeling, data flows, trust boundaries, and testable mitigations. The application and review findings are original fictional cases.', checked='30 September 2026'),
        dict(title='NIST. SP 800-53 Revision 5: Security and Privacy Controls for Information Systems and Organizations.', url='https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final', note='Background for access, accountability, assurance, and control vocabulary. The local policies and closure criteria in the exercises are not universal compliance rules.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Security Triage and Alert Investigation',
    scene='A successful login is not verified authorization',
    rehearsal=['Read turns 1-10. Stress observed facts separately from the maintenance hypothesis.', 'Switch roles for turns 11-20. Keep authentication distinct from authorization.', 'Check the transfer. Read the UTC time and the two missing-evidence statements clearly.'],
    skill='Give a concise alert handoff that separates logged events, plausible explanations, and unresolved authorization.',
    brief='Analyst Anika reviews alert S14 with shift lead Luis. The identity log records a successful privileged-account sign-in at 02:14 UTC from an unfamiliar address. A maintenance ticket covers 02:00-03:00 UTC, but its host and account have not been matched to the event. The account owner has not replied. Application logs are missing for 02:10-02:20 UTC. No malicious action is confirmed. The local process requires escalation to Luis now while correlation continues.',
    cast='Anika | Security analyst\nLuis | Shift lead',
    culture=('Ask without accusing', 'A direct question about who authorized an action is a request for evidence, not necessarily an accusation. Use event details and neutral verbs. Neither familiarity with a colleague nor an urgent alert label settles whether a particular action was permitted.'),
    a='''What does the identity log establish? | A successful privileged-account sign-in at 02:14 UTC | A confirmed hostile actor | A verified match to the maintenance ticket | Complete application visibility | The log establishes the sign-in event, not the identity or permission behind it.
What is missing from 02:10-02:20 UTC? | Application logs | Every identity record | The maintenance ticket | The alert identifier | The briefing identifies an application-log gap during the relevant period.
What does the local process require now? | Escalation to Luis while correlation continues | Closure because maintenance was scheduled | Waiting for certainty before informing anyone | Calling the account owner malicious | The stated process requires prompt escalation without first asserting a confirmed cause.''',
    vocabulary='''alert | A notification that a detection condition was met. | triage an alert
event | An observable occurrence recorded by a system. | correlate events
incident | An occurrence assessed as compromising or threatening security. | classify an incident
triage | Initial assessment to decide priority and next handling. | perform security triage
privileged account | An identity with elevated system permissions. | review privileged-account activity
successful sign-in | A recorded completion of an authentication process. | verify a successful sign-in
authentication | Checking evidence that an identity claim is valid. | examine authentication records
authorization | Permission for a particular action or resource. | confirm authorization
source address | A network address associated with an observed connection. | investigate a source address
timestamp | A recorded time associated with an event. | preserve the timestamp
UTC | Coordinated Universal Time, a shared time reference. | report times in UTC
maintenance window | A defined period for planned maintenance work. | confirm the maintenance window
correlation | Relating records to assess whether events are connected. | correlate identity and host logs
log source | A system or service producing event records. | identify the log source
telemetry | System observations collected for monitoring or analysis. | review available telemetry
visibility gap | A period or area lacking needed observation data. | disclose a visibility gap
baseline | A reference pattern used to evaluate current behavior. | compare activity with the baseline
anomaly | A departure from an expected pattern. | investigate an anomaly
false positive | A detection that incorrectly indicates the target condition. | validate a false positive
benign activity | Activity assessed as not harmful in its context. | confirm benign activity
indicator | An observable sign that can support an investigation. | assess an indicator
hypothesis | A proposed explanation awaiting evaluation. | test the maintenance hypothesis
confidence level | A qualified assessment of evidential strength. | state the confidence level
case record | A documented account of observations and handling. | update the case record''',
    precision='A successful authentication does not establish that the account holder intended or authorized the action. A matching time window supports a possible maintenance explanation, not a confirmed match to this event.',
    precision_extra='No malicious action confirmed is not the same as no malicious action occurred. The missing application logs restrict what the team can exclude; keep that limitation in the handoff.',
    phrases='''Lead with the event | "The identity log records a successful sign-in at 02:14 UTC."
Identify the privilege | "The event involves a privileged account."
Separate the conclusion | "Authorization is not yet verified."
Name the plausible explanation | "The timing overlaps planned maintenance."
Limit the match | "We have not matched the host and account."
Identify missing evidence | "Application logs are missing for ten minutes."
Avoid an accusation | "Who can confirm the authorized operator?"
Preserve urgency | "I am escalating while correlation continues."
State uncertainty | "No malicious action is confirmed at this point."
Bound the search | "That conclusion applies only to the sources checked."
Use neutral wording | "The address is unfamiliar, not yet classified as hostile."
Ask for a record | "Please provide the relevant maintenance approval."
Keep time consistent | "Both timestamps are reported in UTC."
Reject premature closure | "The maintenance window alone does not close the alert."
Name the next check | "We will compare the ticket, account, and host."
Close the handoff | "S14 remains under investigation with a documented visibility gap."''',
    notes='''Successful | Describes the sign-in result, not permission or intent.
Unfamiliar | A comparison with known patterns, not proof of hostility.
Confirmed | Use only when the stated conclusion has supporting evidence.
No evidence found | Name the sources, period, and missing observations.
May be | Introduces a possibility without treating it as established.
Escalate | Means involve the required authority, not necessarily declare a breach.''',
    d='''Which handoff best fits S14? | Successful privileged sign-in; authorization unverified; application-log gap; escalated for investigation. | Successful privileged sign-in; authorized maintenance; application-log gap; awaiting closure. | Successful privileged sign-in; authorization unverified; complete application visibility; escalated. | Successful privileged sign-in; authorization unverified; application-log gap; escalation deferred until the owner replies. | The correct summary preserves all four facts. The alternatives invent authorization, erase the visibility gap, or delay the required escalation.
Which record would help test the maintenance explanation? | A ticket matching this host, account, and authorized task | A ticket from a different server at any time | The owner's seniority alone | The alert's red display color | A relevant authorization record must connect to this event rather than merely exist.
Why is the log gap relevant? | It limits what the team can exclude about application activity. | It proves the actor deleted all records. | It changes UTC into local time. | It makes the successful sign-in disappear. | Missing visibility limits negative conclusions without proving why the records are absent.
Which wording avoids premature blame? | The account was used; the operator is not yet verified. | The account owner attacked the system. | The owner must have approved the activity. | Every unfamiliar address is malicious. | Account activity does not by itself identify the person or their intent.''',
    dialogue='''Anika | S14 triggered on a privileged sign-in at two fourteen UTC. The address is unfamiliar. I have the identity record, but not an explanation yet.
Luis | Start with the [[event::The event is the recorded sign-in, distinct from the conclusion that it was malicious.]], then tell me what remains unknown. A successful sign-in matters, but I do not want the handoff to imply confirmed hostile activity.
Anika | There is a maintenance ticket from two to three UTC. The timing overlaps, although I have not matched its host or account to this record.
Luis | Then maintenance is a [[hypothesis::Maintenance is a possible explanation because the timing overlaps, but the relevant match is unverified.]], not a closure reason. We need the actual task, operator, and asset match before describing this particular sign-in as approved work.
Anika | I nearly waited for the owner to reply before calling you. Should I escalate now and keep the maintenance explanation provisional?
Luis | Keep [[triage::Triage is the initial assessment and handling process that continues while the owner response is pending.]] moving. Our process requires escalation now, and your uncertainty belongs in the update. We can investigate without accusing the owner or announcing a confirmed intrusion.
Anika | I also found missing application logs between two ten and two twenty UTC. That interval includes the identity event we are discussing.
Luis | Record the [[visibility gap::The missing application logs create a visibility gap that restricts the conclusions available to investigators.]] explicitly. We cannot use an incomplete application search to say that nothing happened after the sign-in, even if the records we have look ordinary.
Anika | The dashboard says new address. Is that enough to label the source hostile, or should I just report that it is unfamiliar?
Luis | Call it an [[anomaly::An unfamiliar address departs from the expected pattern but does not establish malicious ownership or intent.]]. It deserves investigation, but novelty does not establish who controlled the connection. The maintenance explanation still needs testing, just as the hostile explanation does.
Anika | Understood. I will say that the identity log records success, the source is unfamiliar, and the account holder has not confirmed the activity.
Luis | Separate [[authentication::Authentication concerns the identity check reflected in the successful sign-in, not permission for every subsequent action.]] from permission. The recorded login result does not establish that the operator was entitled to perform the particular task at that time.
Anika | I will request the relevant approval through our internal channel. The ticket number alone is not enough without checking which account and host it covers.
Luis | Exactly. We need [[authorization::Authorization is permission for the specific action, which requires more than a ticket with overlapping times.]] evidence tied to the action. Keep the original event details and identify any later corrections instead of silently rewriting the first report.
Anika | For the next shift, I will list the identity record, maintenance ticket, unanswered owner request, and missing application interval together in S14.
Luis | Put that in the [[case record::The case record preserves the evidence, unanswered questions, and actions for the next analyst.]]. The next analyst should see both the current evidence and the reason this alert remains open, without reconstructing the conversation.
Anika | I will compare the ticket against the host and account, then update the working explanation when that evidence arrives. No malicious action is confirmed.
Luis | Describe your [[confidence level::The confidence level qualifies the current interpretation and should change with evidence rather than with repeated assertion.]] carefully. We have a real observation and unresolved context. Repeating the same possibility does not turn it into stronger evidence.
Anika | My handoff will keep the event time in UTC and state that the missing application records limit our ability to exclude later activity.
Luis | Good. Continue the [[correlation::Correlation connects the identity event to relevant ticket and host records to test the competing explanations.]] and keep me involved under the escalation process. The status is under investigation, with authorization unverified and the visibility limitation clearly recorded.''',
    transfer_title='Overlap is still not a match',
    transfer_setup='Alert T8 records a sign-in at 05:20 UTC. Maintenance was scheduled from 05:00-06:00, but the account match is unverified. Application logs are unavailable. The shift lead has received the escalation.',
    transfer='''Analyst: "The event time is 05:20 ___." | UTC | The briefing explicitly gives the event time in Coordinated Universal Time.
Lead: "The account match remains ___." | unverified | The overlapping maintenance period does not establish the relevant account match.
Analyst: "Application logs are ___." | unavailable | The supplied absence of application logs limits the investigation evidence.
Lead: "The escalation has been ___." | received | The briefing says the shift lead has already received the escalation.'''))

BOOK['units'].append(unit(
    title='Incident Response and Containment',
    scene='Isolation is complete; the investigation is not',
    rehearsal=['Read turns 1-10. Give report, authorization, and completion times as separate events.', 'Switch roles for turns 11-20. Stress that the next update is not a recovery promise.', 'Check the transfer. Read the three times without swapping authorization and execution.'],
    skill='Coordinate a response update with action status, operational impact, evidence preservation, and a defined next report.',
    brief='Incident coordinator Mara briefs service owner Joel about suspected unauthorized activity on billing host B7, first reported at 09:10 UTC. Under the approved playbook, Mara authorized network isolation at 09:18; completion was verified at 09:22. Billing jobs are paused. Investigators are preserving available evidence; cause, data access, and wider scope remain unconfirmed. Restoration requires the response lead and service owner under the local process. The next update is due at 09:45, not a promised restoration time.',
    cast='Mara | Incident coordinator\nJoel | Billing service owner',
    culture=('Be decisive about the action, exact about the result', 'During a response, colleagues need short updates that they can repeat accurately. Separate the completed action from what it has not established. A calm statement of uncertainty is more useful than either dramatic speculation or premature reassurance.'),
    a='''When was isolation completion verified? | 09:22 UTC | 09:10 UTC | 09:18 UTC | 09:45 UTC | The case distinguishes the first report, authorization, completion, and next update.
What is the confirmed operational impact? | Billing jobs are paused. | All customer records were stolen. | Every service is unavailable. | Billing has been fully restored. | The supplied service effect is paused billing jobs, not wider damage.
What does 09:45 represent? | The next update time | A guaranteed restoration time | The proven intrusion start | Automatic closure | The briefing expressly makes 09:45 a communication commitment, not a recovery promise.''',
    vocabulary='''incident response | Coordinated handling of a suspected or confirmed security incident. | coordinate incident response
containment | Action intended to limit incident spread or impact. | verify containment actions
network isolation | Restricting a system's network connections. | confirm network isolation
eradication | Removal of incident causes or persistence as applicable. | verify eradication
recovery | Restoring affected capabilities under the required checks. | authorize recovery
response lead | The person directing the assigned response process. | brief the response lead
service owner | The role responsible for a business or technical service. | involve the service owner
playbook | Agreed guidance for handling a defined situation. | follow the approved playbook
action log | A time-ordered record of response actions. | maintain the action log
evidence preservation | Protecting relevant records and artifacts from loss or alteration. | coordinate evidence preservation
chain of custody | Documentation of evidence handling and transfers. | maintain chain of custody
volatile data | Information that may be lost when system state changes. | preserve volatile data appropriately
affected host | A system within the known impact or investigation scope. | identify the affected host
incident scope | The systems, accounts, and effects covered by an incident assessment. | establish incident scope
lateral movement | Movement from an initial foothold to other systems. | investigate possible lateral movement
persistence | A means of retaining access across changes or restarts. | assess persistence
exfiltration | Unauthorized transfer of data outside the relevant boundary. | investigate possible exfiltration
restoration criterion | A condition required before returning a service. | confirm restoration criteria
business impact | A consequence for organizational operations or objectives. | report business impact
status update | A time-specific summary of the current position. | issue a status update
decision authority | The role permitted to approve a particular action. | confirm decision authority
handover | Transfer of responsibility and relevant information. | complete the response handover
post-incident review | A review of events and improvements after handling an incident. | schedule a post-incident review
root cause | An underlying reason supported by investigation evidence. | establish the root cause''',
    precision='09:18 is the authorization time; 09:22 is verified completion. Saying isolated at 09:18 would merge two different events. Record both so later reviewers can reconstruct what actually happened.',
    precision_extra='Isolation may limit exposure but does not establish the full incident scope, removal of persistence, or readiness to restore. Here, the next update is fixed while the recovery time remains unknown.',
    phrases='''State the current impact | "Billing jobs are paused on B7."
Give the first report | "The activity was first reported at 09:10 UTC."
Separate approval from action | "Isolation was authorized at 09:18."
Confirm execution | "Completion was verified at 09:22."
Name the unknown | "The cause and wider scope remain unconfirmed."
Avoid a false all-clear | "Containment does not establish recovery readiness."
Protect the record | "Evidence preservation is in progress."
Assign the decision | "Restoration requires the response lead and service owner."
Bound the statement | "We have not confirmed unauthorized data access."
Commit to communication | "The next update will be at 09:45."
Correct the date meaning | "That is an update time, not a restoration estimate."
Acknowledge disruption | "I recognize the impact on billing operations."
Keep actions traceable | "Please record the authorization and completion separately."
Avoid an improvised change | "Use the response process before changing system state."
Prepare the handover | "Include completed actions, open questions, and owners."
Close with the current status | "B7 is isolated; investigation and recovery assessment continue."''',
    notes='''Reported at | Not necessarily the time the underlying activity began.
Authorized | Permission was given; execution still needs verification.
Contained | Define what action and scope support this description.
Compromised | Do not replace suspected activity with a stronger conclusion.
Restore | Requires the relevant technical and operational checks.
Next update | A commitment to communicate, not a promise of resolution.''',
    d='''Which timeline is accurate? | Report 09:10; isolation authorized 09:18; completion verified 09:22. | Intrusion proven to begin 09:10; recovery complete 09:18. | Isolation complete 09:18 because authorization was given. | Incident closed 09:22 because a host was isolated. | The correct timeline preserves the distinct states and supplied timestamps.
Which reply addresses pressure to restore now? | Billing is paused; restoration still requires the specified response and service-owner process. | Restore immediately because isolation proves the cause is removed. | Treat the update deadline as automatic permission to reconnect. | Say all systems are clean because one host is isolated. | Operational urgency does not remove the restoration conditions stated in the case.
Which statement about data access is justified? | Unauthorized data access has not been confirmed. | No data was accessed under any circumstances. | All billing data was exfiltrated. | Isolation proves that no earlier transfer occurred. | The case leaves data access unresolved rather than establishing either extreme.
What belongs in the handover? | Actions, timestamps, impact, open questions, and responsible roles | Only a reassuring headline | A root cause selected to end uncertainty | An undocumented restoration promise | These items preserve usable continuity without inventing conclusions or authority.''',
    dialogue='''Joel | Billing is paused, and the team wants a restoration time. We know B7 is isolated. Can I tell them the incident is now over?
Mara | No. The [[containment::Containment aims to limit impact; it does not establish that investigation, eradication, or recovery is complete.]] action is complete, but cause, data access, and wider scope remain unconfirmed. We should be precise about what that completed action means.
Joel | Give me the timeline so I can explain the interruption. I have nine ten in the report and nine eighteen in the response channel.
Mara | The [[action log::The action log records the report, authorization, and verified execution as separate events.]] should show first report at nine ten, isolation authorization at nine eighteen, and verified completion at nine twenty-two, all UTC.
Joel | I put nine eighteen as the isolation time in my update. That was only permission to act. I will change it to nine twenty-two.
Mara | Please also keep the [[business impact::The confirmed business impact is paused billing jobs, not an assumed broader outage or data loss.]] concrete: billing jobs are paused. We have not established that every related service is affected or that customer data left the environment.
Joel | Would restarting B7 help us resume sooner? Someone suggested it in the operations channel, but I do not know what investigators still need.
Mara | Route that request through the response team. [[Evidence preservation::Evidence preservation protects relevant information from loss or alteration while response decisions are coordinated.]] is in progress, and an improvised state change could affect the investigation. We must coordinate recovery and evidence needs.
Joel | I will stop treating restart as a routine operations decision here. Who needs to agree before this service can return under our process?
Mara | The [[decision authority::The local process assigns restoration decisions to the response lead and service owner, not any individual requesting speed.]] includes the response lead and you as service owner. Technical checks and operational consequences need to be assessed together before restoration.
Joel | I can explain the business impact and available operational options. I cannot certify from isolation alone that the underlying problem has been removed.
Mara | Correct. [[Eradication::Eradication concerns removing the incident cause or persistence as applicable and is distinct from isolating a host.]] has not been confirmed. We also cannot infer the absence of earlier unauthorized data access from the fact that connections are restricted now.
Joel | The team has also asked whether other hosts are involved. I only have the report about B7, so I have not named additional systems.
Mara | Keep the [[incident scope::Incident scope covers the systems and effects under investigation; it remains incomplete in this case.]] open in the update. One known host does not prove that there are no others, but uncertainty is not evidence that all systems are affected.
Joel | What can I promise for nine forty-five: an update, or a working service? People will read the time as a restoration deadline unless I spell it out.
Mara | Yes, as a [[status update::The agreed status update commits the team to communicate at 09:45 without promising restoration by then.]]. We will report what changed, what remains unresolved, and the next actions then. That time is not a restoration estimate.
Joel | I will say that plainly. I also need the next shift to understand what was authorized and which checks are still open when they arrive.
Mara | Use the [[handover::The handover transfers the current evidence, decisions, impact, and outstanding work to the incoming team.]] record, including timestamps, owners, and outstanding decisions. They should not have to infer permission from a short chat message or an optimistic headline.
Joel | My message will say B7 is isolated, billing jobs remain paused, and investigation continues. I will reserve any all-clear for the authorized process.
Mara | That is accurate. [[Recovery::Recovery is the controlled restoration of affected capabilities and is not established merely by isolation.]] remains subject to the required checks and joint decision. We will give the next factual update at nine forty-five even if uncertainty remains.''',
    transfer_title='A report time is not a recovery deadline',
    transfer_setup='Host C4 was first reported at 11:00 UTC. Isolation was authorized at 11:05 and verified complete at 11:09. The next update is 11:30. Recovery has not been authorized.',
    transfer='''Coordinator: "Isolation was authorized at ___ UTC." | 11:05 | The briefing assigns 11:05 to authorization rather than to completion.
Owner: "Completion was verified at ___ UTC." | 11:09 | The verified completion occurred four minutes after the recorded authorization.
Coordinator: "Our next update is at ___ UTC." | 11:30 | The supplied time is a communication commitment, not automatic recovery permission.
Owner: "Recovery remains ___." | unauthorized | The briefing explicitly states that recovery has not been authorized.'''))


BOOK['units'].append(unit(
    title='Vulnerability Management',
    scene='The same score, a different repair priority',
    rehearsal=['Read turns 1-10. Stress equal scores, different exposure, and exploitation elsewhere.', 'Switch roles for turns 11-20. Keep available, deployed, and verified distinct.', 'Check the transfer. Read the priority without claiming a confirmed local compromise.'],
    skill='Explain a risk-based remediation order without treating severity scores as complete business-risk assessments.',
    brief='Vulnerability analyst Chen and infrastructure owner Petra review two fictional findings, each with a base severity score of 8.8. A affects an internet-facing production gateway; a validated threat bulletin reports exploitation of that flaw elsewhere. B affects an isolated test server containing synthetic data, with no route from the internet. No local exploitation is confirmed. Their agreed rule prioritizes demonstrated exploitation and external exposure when scores tie. A patch is available for each; testing, change approval, and verification remain required.',
    cast='Chen | Vulnerability analyst\nPetra | Infrastructure owner',
    culture=('Explain the ranking, not just the number', 'Operations teams need a reason to interrupt planned work. Connect the weakness to the affected asset, exposure, and exploitation evidence. A defensible priority is more persuasive than repeating a severity label while ignoring operational change controls.'),
    a='''Which finding comes first under the stated tie-break rule? | A, the exposed production gateway flaw | B, because test systems always come first | Both must have identical handling because scores match | Neither, because local exploitation is unconfirmed | The stated rule favors A because external exposure and demonstrated exploitation are supplied.
What does the threat bulletin establish? | The flaw has been exploited elsewhere. | This organization is definitely compromised. | The patch has passed local tests. | B is reachable from the internet. | Exploitation elsewhere is relevant evidence but does not prove a local incident.
What remains required after selecting A first? | Testing, change approval, and verification | Only updating the priority label | Assuming the available patch is already installed | Closing both findings immediately | Prioritization orders the work without completing the required change and verification steps.''',
    vocabulary='''vulnerability | A weakness that can be exploited to harm security. | assess a vulnerability
CVE | Common Vulnerabilities and Exposures, an identification system. | reference a CVE identifier
CVSS | Common Vulnerability Scoring System, a severity framework. | interpret a CVSS score
base score | A severity score based on intrinsic vulnerability characteristics. | compare base scores
exploit | A means of taking advantage of a vulnerability. | assess exploit availability
exploitation in the wild | Observed real-world use of a vulnerability. | confirm exploitation in the wild
KEV catalog | CISA's list of vulnerabilities known to have been exploited. | check the KEV catalog
internet-facing | Reachable through an internet-exposed service or interface. | inventory internet-facing assets
asset criticality | The importance of an asset to organizational objectives. | assess asset criticality
attack surface | The exposed points through which a system can be targeted. | reduce the attack surface
reachability | Whether a relevant path to an asset or service exists. | verify reachability
affected version | A software version within a vulnerability's stated scope. | confirm the affected version
patch | A software update intended to correct a defect. | validate a patch
remediation | Work to resolve an identified weakness or problem. | prioritize remediation
mitigation | A measure intended to reduce exposure or impact. | verify a mitigation
compensating control | An alternative safeguard addressing a defined control need. | evaluate a compensating control
remediation window | An agreed period for completing corrective work. | agree a remediation window
change approval | Permission to carry out a defined system change. | obtain change approval
regression test | A check that a change has not broken existing behavior. | run regression tests
rescan | A follow-up scan to reassess a finding. | perform a rescan
false finding | A reported weakness not supported after validation. | investigate a false finding
exception expiry | The date or condition ending an approved exception. | track exception expiry
risk acceptance | An authorized decision to retain a specified risk. | document risk acceptance
closure evidence | Records showing that the required completion conditions were met. | attach closure evidence''',
    precision='A base severity score describes vulnerability characteristics, not the complete risk to a particular organization. Exposure, affected assets, observed exploitation, and local controls can justify different priorities for equal scores.',
    precision_extra='A patch being available is not evidence that it has been deployed successfully. Separate selection, testing, authorization, installation, and verification. A missing local incident does not erase the supplied reasons for prompt remediation.',
    phrases='''Acknowledge the tie | "Both findings have a base score of 8.8."
Add the asset context | "A affects the production gateway."
Name the exposure | "That service is internet-facing."
Qualify the threat evidence | "The bulletin confirms exploitation elsewhere."
Preserve local uncertainty | "We have not confirmed local exploitation."
Apply the agreed rule | "Our tie-break rule prioritizes A."
Keep B visible | "B remains in the remediation queue."
Distinguish availability | "The patch is available, not yet deployed."
Keep change controls | "Priority does not replace testing or approval."
Ask about service impact | "What interruption does the approved change require?"
Specify verification | "Attach evidence that the affected condition is resolved."
Avoid an unsupported closure | "An installation message alone does not close the finding."
Bound a mitigation | "State which exposure the temporary control reduces."
Name the exception owner | "Any delay needs the required owner and expiry."
Clarify the decision | "We are selecting the work order, not declaring an incident."
Close with a handoff | "Record A first, B still open, and the remaining change steps."''',
    notes='''Severe | A characteristic assessment, not a complete priority decision.
Exploited elsewhere | Supports urgency without establishing local compromise.
Isolated | Verify the actual network and access boundaries.
Available | Does not mean tested, approved, or installed.
Resolved | Needs evidence against the finding's closure criteria.
Accept | A risk decision requiring the designated authority.''',
    d='''Which explanation is strongest for A first? | Equal scores; A adds external exposure and validated exploitation evidence under the agreed rule. | A has a higher supplied score. | B has no possible risk under any circumstances. | A is already proven to be compromised locally. | The correct explanation uses the actual differentiators without inventing a score or incident.
Which statement about B is accurate? | It is lower in this ordering but still requires handling. | It is permanently exempt because it uses synthetic data. | Its score must be changed to zero. | It is internet-facing because A is. | The tie-break changes priority, not the existence or eventual handling of B.
What distinguishes a patch from a mitigation? | A patch changes software; another control may reduce exposure without correcting that software. | Every mitigation installs a patch. | A patch is only a risk-acceptance signature. | A mitigation proves all vulnerabilities are absent. | The distinction concerns how the weakness or its exposure is addressed.
Which closure message is supported before any deployment? | A is prioritized; deployment and verification are still pending. | A is resolved because a patch exists. | Both findings are closed because a plan exists. | The threat bulletin certifies local recovery. | Available patches and selected priorities do not establish completed remediation.''',
    dialogue='''Petra | Both findings are eight point eight. The operations queue usually sorts by score, so I need a clear reason to move the gateway ahead.
Chen | The [[base score::The base score reflects intrinsic severity characteristics and does not include every relevant local risk factor.]] is the same, but our tie-break rule uses exposure and demonstrated exploitation. A has both of those additional facts in the supplied assessment.
Petra | Let us separate those facts. A is the production gateway reachable externally. B is an isolated test server holding synthetic rather than live customer data.
Chen | Yes. A is [[internet-facing::Internet-facing identifies A's external exposure, which differentiates it from the isolated test system.]], while B has no route from the internet in this case. That changes the immediate exposure even before we discuss the bulletin.
Petra | The bulletin says the gateway flaw has been used against other organizations. Does that mean we should announce an incident in our own environment?
Chen | No. It establishes [[exploitation in the wild::Real-world exploitation elsewhere supports prioritization but does not by itself establish local compromise.]], not local compromise. We should preserve that distinction while using the verified information as a reason to prioritize corrective work.
Petra | Fine, A first. Can we leave B assigned and visible? I do not want lower priority to turn into nobody owning the test-server fix.
Chen | Keep it in the [[remediation::Remediation is the corrective work still required for both findings, even though A comes first.]] queue. The ordering is A first under our agreed rule, not A matters and B never matters. Both need an accountable path.
Petra | A patch is available for each. The gateway update may interrupt production, so we still need the service team involved in timing and checks.
Chen | Obtain the required [[change approval::Change approval authorizes the defined operational change; a security priority does not automatically supply that permission.]]. Prioritizing A does not prove the update is compatible or authorize an unplanned production interruption. We need the relevant testing and operational coordination.
Petra | Then my ticket will say selected first, patch available, testing and approval pending. I will not mark it resolved just because we found an update.
Chen | Good. The [[regression test::A regression test checks that applying the change has not broken existing behavior required by the service.]] should cover the relevant existing service behavior. A security correction still needs evidence that the planned change works in the required environment.
Petra | If we cannot deploy immediately, the service owner may propose a temporary control. I want the wording to make clear what that would actually achieve.
Chen | Describe it as a [[mitigation::A mitigation reduces a defined exposure or impact and need not remove the underlying software weakness.]] with a defined scope and verification. Do not claim that reducing one access path automatically corrects the underlying software or removes every route.
Petra | Any delay would need the owner, rationale, and review conditions required by our process. An informal note saying accepted would be too vague.
Chen | Exactly. Formal [[risk acceptance::Risk acceptance is an authorized decision concerning a specified retained risk, not an informal label that erases the weakness.]] is not something the analyst can invent to clear the queue. It must follow the assigned authority and state what remains exposed.
Petra | After installation, what evidence do you need to close the finding? I can attach the change record, but we still need to verify the affected condition.
Chen | Attach the [[closure evidence::Closure evidence demonstrates that the required completion conditions were actually met after the change.]] to the record. The person reviewing completion should see why the affected condition is considered resolved, not just that someone ran an installer.
Petra | My summary is A first for demonstrated exploitation and external exposure, B still open, and no local exploitation confirmed. The change steps remain required.
Chen | That makes the [[asset criticality::Asset criticality adds the importance of the production gateway to the context of the prioritization discussion.]] and exposure visible alongside severity. We can justify urgency without exaggerating the evidence or treating the score as the whole decision.''',
    transfer_title='A high priority is not completed work',
    transfer_setup='Findings X and Y have equal base scores. X is internet-facing with verified exploitation elsewhere; Y is isolated. The local rule selects X first. Its patch is available, but deployment has not started.',
    transfer='''Analyst: "The first priority is ___." | X | The supplied tie-break rule favors the exposed flaw with demonstrated exploitation.
Owner: "The base scores are ___." | equal | The case explicitly makes the base severity scores the same.
Analyst: "Exploitation is verified ___." | elsewhere | The supplied evidence describes exploitation elsewhere, not a confirmed local incident.
Owner: "Deployment is still ___." | pending | The briefing says deployment has not started despite patch availability.'''))

BOOK['units'].append(unit(
    title='Identity, Access, and Least Privilege',
    scene='Support needs logs, not a shared administrator',
    rehearsal=['Read turns 1-10. Contrast read-only access with administrator rights.', 'Switch roles for turns 11-20. Stress pending approval and the recorded expiry.', 'Check the transfer. Read the three-hour proposal as a request, not an approval.'],
    skill='Negotiate a specific access arrangement using identity, task, permission, duration, approval, and accountability.',
    brief='Vendor coordinator Eva requests a shared administrator account so two technicians can diagnose a service issue. Access reviewer Rashid confirms that the supplied task needs only read access to sanitized diagnostic logs for two hours. Their local policy requires named identities, multifactor authentication, owner approval, and recorded expiry. No approval has been granted. The proposed alternative gives each technician only the required log access. Any later write task needs a separate assessed request; no broader privilege is justified by the present facts.',
    cast='Eva | Vendor coordinator\nRashid | Access reviewer',
    culture=('Offer a workable boundary', 'A useful access challenge connects the restriction to the task and offers a precise alternative. Avoid sounding as though vendor status itself makes someone untrustworthy. Explain which requested permissions are unnecessary and how the legitimate work can proceed through the approved route.'),
    a='''What does the diagnostic task require? | Read access to sanitized logs for two hours | Permanent administrator access | A shared password for all staff | Unrestricted production write access | The briefing supplies a narrow read-only task with a defined two-hour duration.
Which local requirement is explicit? | Named identities with multifactor authentication, approval, and expiry | Anonymous access if the vendor is familiar | No review for short tasks | Automatic approval after a request | These four conditions are stated in the fictional local access policy.
What is the current approval status? | Not granted | Granted by the request alone | Unnecessary because the logs are sanitized | Permanent approval for future tasks | The briefing explicitly says no approval has yet been granted.''',
    vocabulary='''identity and access management | Processes for managing identities and their permissions. | review identity and access management
least privilege | Limiting access to what the authorized task requires. | apply least privilege
named account | An account associated with an identified individual. | provision a named account
shared account | An account used by more than one individual. | review shared-account risk
privileged access | Permission to perform elevated system actions. | control privileged access
read-only access | Permission to view data without changing it. | grant read-only access
entitlement | A specific right or permission assigned to an identity. | review entitlements
role-based access | Permissions assigned through defined job or task roles. | configure role-based access
multifactor authentication | Verification using more than one distinct factor type. | require multifactor authentication
single sign-on | Access to multiple services through a shared sign-in arrangement. | support single sign-on
federation | Trust between identity systems to support identity assertions. | configure identity federation
provisioning | Creating or enabling an identity or its access. | complete access provisioning
deprovisioning | Removing or disabling access that is no longer needed. | verify deprovisioning
access review | Evaluation of whether granted rights remain appropriate. | conduct an access review
time-bound access | Permission with a defined end time or duration. | approve time-bound access
expiry | The point at which a permission or approval ends. | record access expiry
just-in-time access | Access activated only for an approved period of need. | request just-in-time access
standing privilege | Elevated access retained beyond a particular active task. | reduce standing privilege
session record | Information documenting a particular access session. | review session records
accountability | Ability to associate actions with responsible identities. | preserve individual accountability
separation of duties | Dividing sensitive responsibilities to reduce conflicting control. | maintain separation of duties
break-glass access | Controlled emergency access outside the normal route. | govern break-glass access
service account | An identity used by a service or automated process. | manage service-account permissions
sanitized logs | Diagnostic records with restricted details removed or protected. | share sanitized logs''',
    precision='Authentication checks identity; authorization controls permitted actions. Multifactor authentication does not by itself justify administrator rights. Sanitization also does not remove the stated approval, identity, and expiry requirements.',
    precision_extra='A two-hour read-only task supports a bounded proposal, not automatic approval. If the work later changes, reassess the additional permission instead of silently extending the original scope.',
    phrases='''Acknowledge the support need | "We need to enable the diagnostic work."
Clarify the task | "Which action requires administrator rights?"
Use the supplied scope | "The task only needs sanitized diagnostic logs."
Offer narrower access | "Read-only access supports that task."
Preserve identity | "Each technician needs a named account."
State the local condition | "Multifactor authentication is required."
Bound the duration | "The requested access lasts two hours."
Keep approval explicit | "The service owner has not approved it yet."
Protect accountability | "We need to associate actions with each technician."
Avoid standing access | "This request does not justify permanent privilege."
Name expiry | "Record when the access ends."
Separate future work | "A later write task needs a new assessed request."
Avoid a personal judgment | "The restriction follows the task, not a judgment about the vendor."
Ask for evidence | "Please include the task, identities, and duration."
Confirm removal | "Verify that access ends as approved."
Close the proposal | "Submit named, read-only, time-bound access for owner review."''',
    notes='''Need | Link the permission to an actual task.
Shared | Can weaken individual attribution when people use one identity.
Read-only | Still requires appropriate handling and approval.
Temporary | Needs an explicit end, not an informal expectation.
Approved | Distinguish a proposal from a recorded decision.
More access | Requires a reason beyond convenience or a possible future task.''',
    d='''Which proposal best matches the supplied task and policy? | Named read-only log access for two hours, with MFA and owner approval | Shared read-only log access for two hours, with MFA and owner approval | Named administrator access for two hours, with MFA and owner approval | Named read-only log access with MFA and owner approval, without an expiry | The correct proposal preserves individual identity, task-limited permission, authentication, approval, and duration. Each alternative changes one required boundary.
Why does MFA not settle the request? | It strengthens identity verification but does not justify unnecessary permissions. | It guarantees every requested action is appropriate. | It replaces the need for named identities in this policy. | It means the account can never be misused. | Authentication strength and permission scope address different questions in access decisions.
What should happen if a write task emerges? | Submit the additional need for a separate assessment. | Quietly add write access to the original request. | Treat all future tasks as already approved. | Reuse a shared administrator password without a record. | The original facts justify only reading, and the briefing requires a separate request for writes.
Which explanation avoids blaming the vendor? | The task requires log reading, so we are proposing only that access. | Vendors always misuse administrator accounts. | Familiar technicians never need access review. | We are refusing all support without reviewing the task. | The task-based explanation states a legitimate boundary without making a personal accusation.''',
    dialogue='''Eva | Two vendor technicians need to investigate the service issue. They asked for a shared administrator account so either person can begin when available.
Rashid | Let us start with [[least privilege::Least privilege ties the permissions to the actual authorized task rather than to the broadest convenient account.]]. The supplied task needs read access to sanitized diagnostic logs for two hours. Which part requires changing the system or administering it?
Eva | None of the documented diagnostic steps requires a write. They want to inspect the logs and compare the recorded errors with their product knowledge.
Rashid | Then propose [[read-only access::Read-only access matches inspection of the supplied diagnostic logs without adding unsupported write or administrative rights.]]. That supports the described work without granting unrelated administrative rights. We should make the permitted action clear in the request.
Eva | They will take turns during the two hours. Can one account cover both, or do we need two identities even for that short window?
Rashid | Our policy requires a [[named account::A named account associates access with an identified technician, as required by the stated local policy.]] for each technician. A private agreement about sharing does not replace individual attribution or the access conditions we have been asked to enforce.
Eva | I will collect both identities. The vendor also says their ordinary login is secure. Does that satisfy our sign-in requirement for this request?
Rashid | We require [[multifactor authentication::Multifactor authentication is the explicit local sign-in condition and is separate from the task's permission scope.]]. We need to verify that the approved arrangement meets it, not rely on the general adjective secure or treat vendor familiarity as an exemption.
Eva | That gives me the identity and sign-in requirements. For timing, I can specify a two-hour window rather than leaving the access available indefinitely.
Rashid | Make it [[time-bound access::Time-bound access records a limited period of need instead of granting ongoing privilege for a short task.]] with a recorded end. Short work does not justify standing privilege, and the duration should be visible to whoever reviews and implements the request.
Eva | I have submitted the request, but the owner has not signed off. What can I tell the technicians while that decision is pending?
Rashid | Correct. [[Provisioning::Provisioning enables the access, but the case still requires owner approval before that approved arrangement can be implemented.]] follows the required approval. A well-scoped request is ready for review; it does not authorize itself simply because the proposed permissions are narrow.
Eva | If their diagnosis later shows that a configuration change is needed, I will ask them to describe the new action and why it is necessary.
Rashid | That is a new [[entitlement::An entitlement is a particular permission; adding write authority changes the access requested and needs reassessment.]] question. Do not silently add write access to a request justified only by log reading. The additional need must go through its own assessment.
Eva | I can explain that this is about fitting access to work, not suggesting that the technicians intend to misuse anything. We still want their support.
Rashid | Exactly. [[Accountability::Accountability preserves a connection between actions and individual identities rather than making an accusation about intentions.]] also protects legitimate work by showing who did what. Neutral language makes that purpose clearer than a blanket statement that vendors are risky.
Eva | I will put the identities, read-only log scope, multifactor requirement, two-hour duration, and owner decision in the request. What should I say about the end?
Rashid | Record the [[expiry::Expiry specifies when the permission ends, making the temporary access boundary concrete and reviewable.]] and confirm how it will be enforced. The access should not remain active simply because everyone assumes somebody else will remove it later.
Eva | Then I will send the bounded proposal for owner review and avoid promising administrator access. Any changed task will return with a specific justification.
Rashid | Good. Verify [[deprovisioning::Deprovisioning removes or disables access after the approved need ends rather than leaving an unused permission active.]] when the approved window ends. We can enable the diagnostic work while keeping permission, duration, approval, and individual responsibility explicit.''',
    transfer_title='The task sets the boundary',
    transfer_setup='A technician needs to view sanitized logs for three hours. Local policy requires a named identity, MFA, owner approval, and expiry. Approval is still pending; no write task is supplied.',
    transfer='''Coordinator: "The requested permission is ___." | read-only | Viewing the supplied logs does not require writing or administrative permissions.
Reviewer: "The requested duration is ___ hours." | three | The briefing explicitly limits the diagnostic task to three hours.
Coordinator: "The identity must be ___." | named | The stated local policy requires an individually identified account.
Reviewer: "Owner approval remains ___." | pending | The supplied facts say approval has not yet been granted.'''))


BOOK['units'].append(unit(
    title='Threat Modeling and Secure Design',
    scene='A sign-in check does not decide document access',
    rehearsal=['Read turns 1-10. Stress identity and document permission as separate decisions.', 'Switch roles for turns 11-20. Keep design evidence distinct from an implementation test.', 'Check the transfer. Read identity, authorization, and server as different parts of the control.'],
    skill='Trace a data flow, identify a trust boundary, and turn a specific abuse case into a testable design requirement.',
    brief='Architect Noor and security engineer Daniel review a fictional document portal. A signed-in browser sends a document ID to a service, which retrieves a file from storage. The draft checks the user at sign-in but does not specify a server-side check that the user may access the requested document. Customers must see only their own organization-owned documents. The review has no implemented-system test result or confirmed breach. Daniel proposes a per-request authorization check and an approved test using separate fictional tenant accounts.',
    cast='Noor | Application architect\nDaniel | Security engineer',
    culture=('Challenge the assumption, not the designer', 'A useful design challenge names the specific request, boundary, and missing decision. It does not accuse the architect of causing a breach. Distinguish a documented design gap from an observed production defect while making the next requirement concrete.'),
    a='''What does the supplied draft already check? | The user at sign-in | Authorization for every requested document | That every customer owns every file | The outcome of an implemented-system test | The draft describes a sign-in check but lacks the separate per-document authorization decision.
What security requirement is supplied? | Customers may see only their own organization-owned documents. | Every signed-in user may read every document. | Storage may trust every browser-supplied identifier. | A document ID grants access by itself. | The briefing explicitly defines the organization-level document-access boundary.
What is not established? | A confirmed breach or implemented-system test result | The existence of browser requests | The use of document identifiers | The need to restrict documents by organization | The discussion concerns the draft design, not an already proven live exploit.''',
    vocabulary='''threat model | A structured account of relevant threats and responses. | review the threat model
data flow | Movement of information between system elements. | trace the data flow
trust boundary | A point where assumptions about control or trust change. | identify a trust boundary
external entity | An actor or system outside the modeled component. | identify external entities
process | A component that transforms or acts on data. | model the service process
data store | A location where information is retained. | identify data stores
asset | Something of value requiring protection. | identify sensitive assets
entry point | A place where data or interaction enters a system. | review entry points
abuse case | A scenario describing misuse of intended functionality. | define an abuse case
security requirement | A checkable condition protecting a security objective. | specify a security requirement
authentication check | A check of the claimed identity. | perform an authentication check
authorization check | A check of permission for a requested action. | enforce an authorization check
object-level authorization | Permission enforcement for a specific requested object. | verify object-level authorization
tenant | A customer or organization sharing a service. | isolate tenant data
tenant isolation | Separation preventing unauthorized cross-tenant access. | test tenant isolation
server-side enforcement | A decision enforced by the service rather than the client. | require server-side enforcement
untrusted input | Data not accepted as authoritative without validation. | handle untrusted input
document identifier | A value used to refer to a specific document. | validate the document identifier
STRIDE | Spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. | apply STRIDE categories
spoofing | Misrepresenting an identity or source. | assess spoofing threats
tampering | Unauthorized modification of data or system state. | prevent data tampering
information disclosure | Exposure of information to an unauthorized party. | prevent information disclosure
denial of service | Disruption of access to a service or resource. | assess denial-of-service risk
elevation of privilege | Gaining rights beyond the permitted level. | prevent elevation of privilege''',
    precision='Identity and object permission are different decisions. A legitimate user may still request a document belonging to another organization. The design must specify where that permission is enforced, not merely that sign-in exists.',
    precision_extra='This is a design review, not proof of a breach. The proposed test belongs in an approved environment with controlled test accounts and data. A passing identity check alone does not satisfy the document-access requirement.',
    phrases='''Start with the request | "The browser sends a document identifier to the service."
Trace the next step | "The service retrieves the file from storage."
Name the boundary | "The client-provided identifier crosses a trust boundary."
Acknowledge the existing check | "The draft checks identity at sign-in."
Identify the missing decision | "It does not specify permission for this document."
State the protected outcome | "Customers must see only their own organization's documents."
Keep the claim bounded | "We have a design gap, not a confirmed breach."
Make the abuse case concrete | "A signed-in user requests another tenant's document."
Place enforcement | "The permission check belongs on the server for each request."
Reject client trust | "A browser-supplied identifier is not authorization."
Define the denied case | "The service must deny access when the document is outside the user's permitted scope."
Preserve legitimate work | "The allowed same-tenant request must still work."
Use controlled testing | "Use approved test accounts and fictional documents."
Assign the requirement | "Add the access condition to the design and tests."
Separate categories | "This case concerns unauthorized disclosure of document content."
Close the review | "Record the requirement, its owner, and the validation evidence needed."''',
    notes='''Authenticated | Does not mean authorized for every object.
Missing in the draft | Not the same as proven absent in the implementation.
Trust | State which input or claim is being relied upon.
Per request | Check the action each time under the intended rule.
Deny | Specify the condition and observable protected outcome.
Test | Must have approved scope, controlled data, and a clear expected result.''',
    d='''Which requirement closes the identified design gap? | Enforce server-side permission for each requested document. | Require sign-in and then trust every document ID. | Hide the document ID in the page while omitting server checks. | Treat every authenticated user as a storage administrator. | The missing decision concerns permission for the requested object, not only identity or interface presentation.
Which pair best tests the stated boundary? | An authorized same-tenant request and a denied cross-tenant request using controlled data | Two requests by the same owner for the same file only | A page color check and a logo check | A search of live customer documents without approval | The pair checks both intended access and the protected boundary within authorized test scope.
Which statement overclaims the review evidence? | A customer breach has definitely occurred. | The draft lacks a specified document-permission check. | A sign-in check is described. | The design needs a testable access condition. | The briefing explicitly supplies no confirmed breach or implemented-system test result.
Why is a browser-supplied ID not enough? | A value naming an object does not establish permission to access it. | Every identifier is automatically secret forever. | Storage ownership changes when a URL is typed. | Authentication makes object checks unnecessary. | Identifying a document and authorizing access to it are separate functions.''',
    dialogue='''Noor | The diagram lists the browser, service, and storage. We require sign-in before the document page, so I thought the main access question was covered.
Daniel | Let us trace the [[data flow::The data flow shows how the identifier moves from the browser through the service to storage.]]. A browser sends a document identifier, the service processes it, and storage returns content. Where is permission for that particular document checked?
Noor | The draft does not say. It describes checking the user at sign-in, then retrieving the requested file. Our customers should see only their own organization's documents.
Daniel | That leaves an [[authorization check::The authorization check decides permission for the requested document, distinct from verifying identity at sign-in.]] unspecified. We know who signed in, but we still need the service to decide whether that user may access the requested object.
Noor | So the gap is not simply that somebody could be anonymous. It also concerns a legitimate user asking for a document outside their organization.
Daniel | Exactly. That is the [[abuse case::The abuse case describes a signed-in user attempting access outside the intended document boundary.]] we should record. It makes the missing decision concrete without claiming that the implemented system has already leaked anything or that a breach occurred.
Noor | Could we just hide documents from other organizations in the browser? Or does the service need to enforce the same boundary independently?
Daniel | The client crosses a [[trust boundary::The trust boundary separates client-controlled input from the service's responsibility to enforce access decisions.]]. A page convention does not give the server a dependable authorization decision. We need enforcement where the service controls access to the content.
Noor | Then the requirement should say the service checks permission on every request, using the authenticated user's allowed organization scope and the requested document.
Daniel | Yes, that is [[object-level authorization::Object-level authorization applies the permission rule to each specific requested document rather than to sign-in alone.]]. The service must deny access when the document is outside that permitted scope, while keeping the legitimate same-tenant request working.
Noor | I will put both outcomes into the design. Otherwise someone could call the issue fixed by denying every request and breaking the ordinary feature.
Daniel | Good. A useful [[security requirement::A security requirement states a checkable protected outcome while preserving the intended authorized behavior.]] is checkable and preserves intended use. We should identify the denied case and the allowed case instead of saying only make document access secure.
Noor | For validation, we can use two fictional organizations with controlled test accounts and documents in the approved environment. No live customer exploration is needed.
Daniel | That supports a [[tenant isolation::Tenant isolation concerns preventing unauthorized access between customer organizations sharing the service.]] check within an authorized scope. Record which account owns which document, the requested action, and the expected result before interpreting the observed outcome.
Noor | What label goes in the review: confirmed vulnerability or design gap? We have a draft in front of us, not an implementation test.
Daniel | Keep the [[threat model::The threat model records the design-level threat and response without converting an untested design gap into a confirmed breach.]] precise: documented design gap, proposed requirement, validation pending. We should not manufacture certainty, but the lack of a live failure does not erase the gap.
Noor | I will assign the requirement to the service owner and include the browser input, storage ownership, and access-decision location in the revised diagram.
Daniel | Make [[server-side enforcement::Server-side enforcement places the permission decision in the controlled service rather than relying on browser behavior.]] explicit. The next reviewer should not have to guess whether the note describes a user-interface preference or an actual control over returned content.
Noor | The review record will distinguish the existing sign-in check, missing per-document rule, proposed controlled tests, and evidence still needed before we close the action.
Daniel | That is clear. The relevant harm here is [[information disclosure::Information disclosure is unauthorized exposure of document content, the specific harm addressed by this access requirement.]], and the response is a defined access decision. We have moved from a technology list to a reviewable requirement without overstating the evidence.''',
    transfer_title='Identity is not object permission',
    transfer_setup='A design checks identity at sign-in but omits permission checks for individual invoices. Customers may access only their own invoices. No implementation test has run. The proposed control belongs in the service.',
    transfer='''Architect: "The existing check establishes ___." | identity | The supplied design checks the signed-in identity rather than invoice permission.
Security: "Each invoice also needs an ___ check." | authorization | Authorization determines whether the user may access the particular requested invoice.
Architect: "Enforcement belongs on the ___." | server | The proposed control is enforced by the service, not by client convention.
Security: "Implementation validation remains ___." | pending | The briefing says no implementation test has yet been performed.'''))

BOOK['units'].append(unit(
    title='Governance, Risk, and Compliance',
    scene='A written policy does not close the control finding',
    rehearsal=['Read turns 1-10. Contrast three supported cases with two unverified cases.', 'Switch roles for turns 11-20. Stress sample limits and the required owner review.', 'Check the transfer. Read the evidence request without calling the missing case late.'],
    skill='Describe audit evidence, distinguish missing proof from proven failure, and state the actual closure conditions.',
    brief='Control owner Rosa asks auditor Amir to close a leaver-access finding because a new policy was approved. The local control requires access removal within 24 hours of departure. In a five-person sample, three records prove timely removal; two lack removal timestamps. The agreed closure criteria require evidence for all five sampled cases and owner review. That review is not recorded. Amir must distinguish a documentation gap from proof that the two removals were late, while keeping the finding open.',
    cast='Rosa | Control owner\nAmir | Internal auditor',
    culture=('Make the evidence request specific', 'A challenge to closure need not dismiss the work already completed. Acknowledge the approved policy, then name the missing records and review. Avoid both extremes: treating paperwork as operating proof or calling every undocumented action a proven late removal.'),
    a='''How many sampled records prove timely removal? | Three of five | Five of five | Two of five | None, because no policy exists | Three records contain evidence of removal within the stated twenty-four-hour limit.
What do the other two records lack? | Removal timestamps | Employee names in every case | A rule requiring access removal | Proof that a policy was approved | The briefing identifies missing timestamps rather than confirmed late removals.
Can the finding close under the supplied criteria? | No; evidence and owner review are incomplete. | Yes; a written policy replaces all operating evidence. | Yes; three records prove every removal was timely. | No; the briefing proves every removal was late. | The stated closure conditions require all five cases to be evidenced and owner review recorded.''',
    vocabulary='''governance | Arrangements for directing decisions, responsibilities, and oversight. | strengthen security governance
control objective | The outcome a control is intended to achieve. | define the control objective
control design | The planned way a control is meant to work. | assess control design
operating effectiveness | Whether a control works as intended over the assessed scope. | test operating effectiveness
policy | An approved statement of required principles or rules. | approve an access policy
procedure | Defined steps for carrying out a process. | maintain the removal procedure
control owner | The role accountable for a defined control. | identify the control owner
evidence request | A specified request for records supporting an assessment. | issue an evidence request
audit trail | Records allowing actions and decisions to be traced. | preserve the audit trail
sample | A selected subset examined in an assessment. | define the audit sample
population | The full set from which assessment items are selected. | establish the population
sampling limitation | A restriction on what a sample supports about the wider set. | disclose sampling limitations
exception | A departure from a defined requirement or expected condition. | investigate an exception
evidence gap | Missing support needed to substantiate a conclusion. | resolve an evidence gap
finding | A documented assessment issue supported by stated criteria and evidence. | track an audit finding
remediation plan | Agreed work to address an identified finding. | review the remediation plan
closure criterion | A stated condition required to close an action. | satisfy closure criteria
attestation | A formal statement affirming a specified matter. | obtain an owner attestation
independent review | Assessment by a sufficiently separate reviewer. | conduct an independent review
retention period | The required duration for keeping records. | apply the retention period
control frequency | How often a control is intended to operate. | specify control frequency
leaver process | Handling required when a person leaves an organization. | verify the leaver process
access removal | Disabling or withdrawing previously granted permissions. | evidence timely access removal
residual risk | Risk remaining after the relevant controls or treatment. | assess residual risk''',
    precision='Three of five is 60% of the sample with documented timely removal. It is not a demonstrated 60% organization-wide effectiveness rate. The two missing timestamps do not establish whether those removals were timely or late.',
    precision_extra='Policy approval supports the existence of a rule. Operating evidence supports what happened in practice. The supplied closure conditions require all five sampled cases and recorded owner review, so the finding remains open.',
    phrases='''Acknowledge progress | "The new policy has been approved."
Separate design from operation | "That does not yet establish operating effectiveness."
State the criterion | "Access removal is required within 24 hours."
Give the supported count | "Three of five records prove timely removal."
Name the missing evidence | "Two records lack removal timestamps."
Avoid a false failure claim | "We cannot determine timeliness for those two from these records."
Limit the percentage | "Sixty percent of this sample has documented timely removal."
Preserve the closure rule | "The agreed criteria require evidence for all five cases."
Ask for the review | "Please provide the recorded owner review."
Avoid retroactive invention | "Do not create a timestamp as though it were an original record."
Request traceable support | "Use the relevant system evidence and identify its source."
Distinguish assurance | "An assurance statement is not a substitute for the required record."
Keep the status accurate | "The finding remains open pending the missing evidence."
Bound the conclusion | "This sample does not establish the result for the entire population."
Assign the next step | "The control owner will gather the missing records."
Close the discussion | "We will reassess closure against the same agreed criteria."''',
    notes='''Written | Establishes a document exists, not that people followed it.
Timely | Needs both a defined deadline and relevant event evidence.
Undocumented | Does not automatically mean not done.
Sample | State its size and avoid unwarranted population claims.
Closed | A conclusion under stated criteria, not a reward for effort.
Attest | Make clear what is affirmed and what evidence remains required.''',
    d='''Which summary is accurate? | Three timely removals are evidenced; two are unverified; owner review is missing. | All five removals are proven timely because the policy exists. | Two late removals are proven by missing timestamps. | Sixty percent of all employees were removed on time. | The correct summary keeps documented timeliness, missing evidence, and missing review separate.
What is 3 divided by 5 in this case? | 60% of the sample with documented timely removal | 60% organization-wide control effectiveness | A 60% proven late-removal rate | Proof that the two undocumented cases were timely | The calculation applies only to the supplied five-item sample and evidence status.
Which evidence request is appropriately specific? | Provide source records for the two removal times and the owner review. | Please send anything that looks reassuring. | Replace the missing timestamps with estimates presented as original records. | Repeat the policy approval date as proof of all removals. | The request directly addresses the missing closure evidence without inventing historical facts.
Why should the finding remain open? | The agreed evidence and review conditions are not met. | A new policy can never support a control. | Every missing record proves deliberate misconduct. | The auditor dislikes the control owner. | Closure follows the supplied criteria, not personal approval or unsupported accusations.''',
    dialogue='''Rosa | The new leaver policy is approved. It requires removal within twenty-four hours, and I would like the audit action marked closed before the committee meeting.
Amir | Policy approval is useful progress on [[control design::Control design concerns the planned rule and process, which policy approval supports without proving operation.]], but closure also requires evidence that the control operated. Let us compare the supplied records with the criteria we agreed.
Rosa | We selected five leavers. Three records include departure and removal times within the required period. The other two do not include removal timestamps.
Amir | Then [[operating effectiveness::Operating effectiveness concerns actual performance; the incomplete records do not establish it for every sampled case.]] is not established for all five. We should not describe the policy document as if it were evidence of each actual removal.
Rosa | Could I say the control was sixty percent effective? Three out of five is sixty percent, and that seems more concise for the committee.
Amir | Report the [[sample::The sample is the five examined cases, so the percentage must be tied to those records and their evidence status.]] accurately: sixty percent has documented timely removal. That does not establish organization-wide effectiveness, and it does not prove the other two were late.
Rosa | I agree about not calling them late without evidence. The help desk thinks the removals happened, but we do not yet have the original supporting records.
Amir | That is an [[evidence gap::The evidence gap is the absence of timestamps needed to determine timeliness, not proof of a late action.]]. Request the relevant system records and identify their source. A recollection can guide the search, but it should not become an invented historical timestamp.
Rosa | The closure note says evidence for every sampled case and owner review. I have not completed a recorded review because the two records are still missing.
Amir | Those are the [[closure criteria::The closure criteria explicitly require all five cases to be evidenced and owner review recorded.]] we must use. The finding remains open until the missing support and required review are addressed, rather than closing merely because the policy now exists.
Rosa | The committee will ask why it is still open. Can we show the approved policy and three supported cases without implying the remaining work is done?
Amir | Show that in the [[remediation plan::The remediation plan can record completed policy work and the remaining evidence and review tasks without falsely closing the finding.]]. Completed work and an open finding can coexist. A progress update should say what changed and what still prevents the agreed closure.
Rosa | I will assign the record retrieval and keep the committee wording bounded. For the missing cases, I will use timeliness unverified rather than late.
Amir | That preserves the [[audit trail::The audit trail records what the evidence shows and how later conclusions are reached without overwriting the uncertainty.]]. We need a traceable account of the assessment, including any later records or corrections, not a headline that hides unresolved support.
Rosa | Could I sign a statement about our normal process? I can describe what the team does, but I cannot supply those two times yet.
Amir | An [[attestation::An attestation is a formal statement, but it does not replace the source evidence expressly required by these closure criteria.]] may be relevant context, but it does not replace the specific records required here. We should not silently change the closure standard at the end.
Rosa | Understood. I will separate approval of the policy, evidence for three timely removals, two unverified cases, and the owner review still to be recorded.
Amir | Also state the [[sampling limitation::The sampling limitation prevents the five reviewed cases from being presented as proof about every leaver in the organization.]]. We examined five records; we have not established the result for every leaver. The percentage needs both its denominator and its evidence meaning.
Rosa | Then I can give the committee a truthful progress report and a clear remaining action, without claiming that missing documentation proves misconduct or lateness.
Amir | Exactly. The [[control owner::The control owner is responsible for gathering the remaining support and completing the required review in this case.]] can bring the missing evidence for reassessment. We will evaluate closure against the same criteria and record the conclusion the completed support actually justifies.''',
    transfer_title='Missing proof is not a proven delay',
    transfer_setup='A four-case access-removal sample has three documented timely removals and one missing timestamp. Closure requires evidence for all four and an owner review. Neither the missing evidence nor the review is complete.',
    transfer='''Auditor: "For the fourth case, we still need the removal ___." | timestamp | The missing removal timestamp is the source evidence needed to compare the action with the deadline.
Owner: "Without it, I cannot verify that case's ___." | timeliness | Timeliness is unresolved; the missing record does not prove either timely or late removal.
Auditor: "We also need the recorded owner ___." | review | The local closure criteria separately require an owner review that has not been completed.
Owner: "Keep the finding open until the evidence and review meet our conditions for ___." | closure | Closure depends on both outstanding requirements, not merely the existence of the approved policy.'''))


BOOK['units'].append(unit(
    title='Security Awareness and Phishing',
    scene='Report the click, without guessing the consequence',
    rehearsal=['Read turns 1-10. Use a calm tone and distinguish each reported action.', 'Switch roles for turns 11-20. Stress the trusted reporting route without promising an all-clear.', 'Check the transfer. Read the seven-minute interval and pending classification accurately.'],
    skill='Elicit a precise suspicious-message report, encourage prompt disclosure, and avoid requests for secrets or unsupported reassurance.',
    brief='Employee Ben calls security responder Leila about an email claiming to be from Payroll. He clicked its link at 09:32 UTC and reported it at 09:36. He says he entered no credentials, opened no attachment, and approved no sign-in prompt. He worries that reporting will get him blamed. The message has not been classified, and compromise is not established. The local process routes the original message through the approved reporting tool. Leila asks for factual details, not passwords, and tells Ben not to interact further while the response team assesses it.',
    cast='Ben | Employee reporter\nLeila | Security responder',
    culture=('Make accurate reporting easier', 'Thank the person for reporting and ask neutral, concrete questions about actions. Do not promise immunity from every workplace consequence or declare the device safe without evidence. Reassurance should support truthful disclosure and the reporting process, not substitute for assessment.'),
    a='''What did Ben report doing? | Clicking the link without entering credentials, opening an attachment, or approving a prompt | Entering a password and approving every prompt | Downloading an attachment and running it | Confirming that Payroll sent the email | The briefing gives a link click and explicitly excludes the other reported actions.
How long after the click did Ben report it? | Four minutes | Thirty-two minutes | Thirty-six minutes | Four hours | The time from 09:32 to 09:36 UTC is four minutes.
What is the message status? | Not yet classified | Confirmed legitimate payroll communication | A confirmed breach of every account | Proven harmless because no password was entered | The briefing leaves both message classification and compromise unestablished.''',
    vocabulary='''phishing | Deceptive communication intended to induce unsafe disclosure or action. | report suspected phishing
social engineering | Manipulating people to gain information or access. | recognize social-engineering tactics
pretext | A claimed reason used to justify a request. | identify the pretext
impersonation | Pretending to be a trusted person or organization. | assess possible impersonation
display name | The sender label shown by a message interface. | inspect the display name
sender address | The address presented as the origin of a message. | verify the sender address
reply-to address | The destination used when replying to a message. | compare the reply-to address
message header | Technical metadata associated with an email. | preserve message headers
link destination | The address to which a link points. | assess the link destination
attachment | A file included with a message. | report an unexpected attachment
credential | Information or a token used to support authentication. | protect authentication credentials
credential harvesting | Deceptively collecting authentication information. | investigate credential harvesting
MFA prompt | A request for an additional authentication step. | report an unexpected MFA prompt
urgency cue | Language pressuring someone to act quickly. | identify an urgency cue
out-of-band verification | Checking through a separate trusted communication route. | use out-of-band verification
known contact channel | A previously verified way to reach a person or team. | use a known contact channel
reporting tool | An approved mechanism for submitting suspicious content. | use the reporting tool
reporter | A person who raises a concern or observation. | acknowledge the reporter
intake | Initial collection of facts for assessment. | complete security intake
interaction history | A factual account of actions taken with content. | record interaction history
message classification | An assessed category assigned to a message. | confirm message classification
compromise | Loss of the intended security of an account or system. | investigate possible compromise
quarantine | Controlled separation of suspicious content or systems. | verify quarantine status
reporting delay | Time between a relevant event and its report. | measure reporting delay''',
    precision='No credentials entered is important reported information, not proof that no risk exists. Preserve what the employee says as a report until corroborated where needed. Message appearance and a familiar display name do not establish authenticity.',
    precision_extra='The four-minute reporting interval is a fact about this case. Thanking the reporter supports the response, but the responder should not promise an outcome that belongs to another process or declare a clean device without assessment.',
    phrases='''Welcome the report | "Thank you for reporting it promptly."
Ask neutrally | "What did you do after opening the message?"
Locate the event | "What time did you click the link?"
Separate the actions | "Did you enter credentials, open a file, or approve a sign-in prompt?"
Protect secrets | "Do not tell me your password."
Attribute the account | "You report that no credentials were entered."
Avoid premature reassurance | "We have not established whether there was any compromise."
Stop further interaction | "Do not interact with the message further."
Use the approved route | "Submit the original through the reporting tool."
Preserve relevant details | "Keep the message details available for the response team."
Avoid ordinary forwarding | "Use the approved tool, not a wider distribution list."
Verify independently | "Use a known Payroll contact channel for any business confirmation."
Name the pretext | "The message claims that payroll action is urgent."
Keep classification open | "The message is still under assessment."
Support disclosure | "Accurate details help us choose the right response."
Close with a clear next step | "The response team will assess the report and provide instructions."''',
    notes='''Claimed sender | Not yet an authenticated sender.
Clicked | Distinguish from entering credentials or opening a file.
Reported | Attributes the information without overstating verification.
No credentials | A relevant fact, not an all-clear.
Thank you | Encourages reporting without promising immunity or outcomes.
Urgent | A reason to verify, not a reason to bypass the reporting route.''',
    d='''Which opening is most useful? | Thank you for reporting. What actions did you take, and when? | Why would anyone fall for that? | Nothing can happen if you entered no password. | Tell me your password so I can check it. | The useful opening encourages disclosure and gathers facts without blame or secret collection.
Which status accurately reflects the facts? | A suspicious-message report is under assessment; compromise is not established. | Every payroll account has been breached. | The email is safe because its display name says Payroll. | The link click proves all credentials were stolen. | Neither message classification nor compromise has been established in the supplied case.
What should Ben use to submit the original? | The approved reporting tool | A message to every colleague | A reply to the suspicious sender asking permission | Repeated clicks to reproduce the issue on other devices | The briefing specifies the approved reporting tool and says to avoid further interaction.
Which confirmation route avoids trusting the suspicious message? | A previously verified Payroll contact channel | The phone number supplied only in that email | The message's reply-to address without checking | The linked page's assurance that it is genuine | An independent known channel does not rely on contact details supplied by the suspect message.''',
    dialogue='''Ben | I clicked a payroll email and now I am worried it was suspicious. I reported it quickly, but I am concerned that I will be blamed.
Leila | Thank you for [[reporting promptly::Thanking the employee for reporting promptly encourages factual disclosure without blame or promises about employment outcomes.]]. Accurate details help the response. Let us go through what you actually did, without guessing the consequence.
Ben | The email said I needed to confirm payroll information urgently. It showed Payroll as the sender name, so I assumed it came from our team.
Leila | That [[display name::The display name is the visible sender label, which does not by itself establish that the message is genuine.]] is useful context, but it does not verify the sender. Tell me the click time and what appeared next, without interacting with the message again.
Ben | I clicked at nine thirty-two UTC and reported it at nine thirty-six. A page opened. I did not type anything into it.
Leila | I will record the [[interaction history::The interaction history distinguishes the click from later actions such as entering data, opening files, or approving prompts.]]. Did you enter credentials, open an attachment, or approve a sign-in prompt? Those are separate actions, and we need each one described accurately.
Ben | No credentials, no attachment, and no prompt approval. I can give you my password if that helps you check whether the account was affected.
Leila | Please do not share any [[credential::A credential supports authentication and should not be disclosed during this factual intake conversation.]]. We do not need your password in this conversation. We need the account identifier and factual actions through the approved response process.
Ben | I did not enter anything. Can I tell my manager the account is safe, or do you still need to check?
Leila | We have not established [[compromise::Compromise is not confirmed, but the absence of reported credential entry alone does not prove that no risk exists.]], and I cannot give an all-clear from that fact alone. Your report narrows the assessment; it does not replace it.
Ben | Understood. I still have the original email. Should I forward it to everyone in my department so they can recognize it and avoid clicking?
Leila | Use the approved [[reporting tool::The reporting tool is the stated route for submitting the original message without spreading it through an ordinary distribution list.]] for the original. Do not distribute the message more widely or interact further. The response team will assess it and coordinate any necessary communication.
Ben | I will use that route. The message also gives a phone number for Payroll. Should I call that number to ask whether they sent it?
Leila | Use [[out-of-band verification::Out-of-band verification uses a separate trusted route rather than contact details supplied by the suspicious communication.]] through a Payroll channel you already know is genuine. A number supplied only in the suspicious message would rely on the same unverified source.
Ben | I can reach Payroll through our established internal contact. For the security report, I will keep the times and the original message available.
Leila | Good. The [[reporting delay::The reporting delay is four minutes between the supplied click and report times, not a measure of confirmed harm.]] was four minutes in this case. Prompt reporting gives us useful information sooner, but we still need the assessment before describing the outcome.
Ben | I almost left out the click. I felt embarrassed and thought the fact that I had not entered a password was the important part.
Leila | Complete [[intake::Intake gathers the relevant facts needed for assessment; omitting the click would distort the response team's understanding.]] depends on those details. Please keep the account accurate. I can explain our response steps, but I should not make promises about decisions outside my role.
Ben | My manager can hear that I clicked, reported four minutes later, and did not enter credentials, open an attachment, or approve a prompt. Assessment is pending.
Leila | Exactly. [[Message classification::Message classification remains pending until assessment determines the appropriate category; a familiar label does not settle it.]] is still open. Submit the original through the approved tool and follow the response team's instructions. Do not treat either embarrassment or reassurance as evidence.''',
    transfer_title='Report actions separately',
    transfer_setup='An employee clicked a suspicious link at 14:10 UTC and reported it at 14:17. They report no credential entry. Message classification is pending. The approved tool is the required reporting route.',
    transfer='''Responder: "The reporting interval was ___ minutes." | seven | The interval from 14:10 to 14:17 UTC is seven minutes.
Employee: "I report no ___ entry." | credential | The supplied fact concerns credential entry rather than every possible interaction or risk.
Responder: "Message classification is ___." | pending | The briefing explicitly leaves message classification unresolved at this stage.
Employee: "I will use the approved reporting ___." | tool | The local process specifies the approved tool as the reporting route.'''))

BOOK['units'].append(unit(
    title='Executive Risk Briefings',
    scene='A recovery shortfall needs a bounded decision',
    rehearsal=['Read turns 1-10. Stress restoration time, the assumed rate, and deferred records.', 'Switch roles for turns 11-20. Contrast requested funding with demonstrated improvement.', 'Check the transfer. Read the two-hour excess and 300-record illustration with their units.'],
    skill='Connect a measured security gap to a business consequence and a specific investment request without claiming guaranteed risk elimination.',
    brief='Security lead Imani briefs finance sponsor Victor on payroll resilience. A controlled recovery test took six hours against an approved four-hour recovery-time objective. It did not establish data loss, and no live incident is occurring. Payroll normally processes 200 scheduled records per hour. A four-hour interruption would defer 800 records at that assumed rate, not prove lost revenue. Proposal A requests $30,000 for recovery automation and repeat testing. Proposal B requests $20,000 for alert-dashboard improvements. The agreed priority is the evidenced payroll recovery shortfall; Victor must decide on A.',
    cast='Imani | Security lead\nVictor | Finance sponsor',
    culture=('Give the decision before the technical inventory', 'Executive listeners need the measured gap, its operational meaning, the proposed response, and the approval requested. Acknowledge alternatives fairly. Avoid converting a scenario into a forecast or a test result into a claim that a current attack is under way.'),
    a='''How far did the test exceed the recovery-time objective? | Two hours | Four hours | Six hours | Eight hundred hours | Six hours of observed recovery minus the four-hour objective equals two hours.
What does the 800-record illustration mean? | Deferred processing during four hours at the assumed rate | Proven lost revenue of $800 | Confirmed destruction of 800 records | A measured live-incident backlog | Four hours multiplied by two hundred records per hour gives deferred processing, not proven loss.
What decision is requested? | $30,000 for recovery automation and repeat testing | $20,000 for a payroll data-loss payment | A declaration that all cyber risk is eliminated | Approval of an already completed live recovery | The briefing identifies proposal A and its defined funding purpose.''',
    vocabulary='''risk scenario | A defined chain of conditions, event, and consequence. | describe a risk scenario
risk exposure | The potential for loss or harm under stated conditions. | explain risk exposure
business consequence | An effect on operations, obligations, or objectives. | connect to a business consequence
likelihood | An assessment of how probable an event is. | qualify the likelihood estimate
impact estimate | A bounded assessment of potential consequences. | state the impact estimate
uncertainty range | An interval expressing limits on an estimate. | report an uncertainty range
recovery-time objective | The target time for restoring a capability after disruption. | test the recovery-time objective
recovery-point objective | The target limit on data loss measured in time. | distinguish the recovery-point objective
recovery test | A controlled exercise of restoration capabilities. | run a recovery test
resilience | Capacity to withstand disruption and restore required function. | improve operational resilience
processing backlog | Work awaiting processing after capacity or availability is lost. | estimate the processing backlog
deferred processing | Work delayed rather than necessarily lost. | quantify deferred processing
service interruption | A period when a service is unavailable or impaired. | assess service interruption
risk treatment | An action or decision to address a specified risk. | select risk treatment
investment case | Reasons, costs, and expected outcomes supporting expenditure. | present an investment case
decision request | A precise action sought from an authorized decision maker. | frame the decision request
funding envelope | The defined amount available or requested for work. | specify the funding envelope
implementation dependency | A prerequisite for carrying out a proposed change. | identify implementation dependencies
success measure | A defined basis for judging a proposed outcome. | agree success measures
assurance evidence | Support for confidence that an intended capability works. | collect assurance evidence
risk appetite | The amount and type of risk an organization is willing to pursue or retain. | clarify risk appetite
tolerance threshold | A defined boundary for acceptable deviation or exposure. | specify a tolerance threshold
residual exposure | The relevant exposure remaining after a proposed measure. | disclose residual exposure
review trigger | A condition requiring renewed assessment or decision. | define a review trigger''',
    precision='The test exceeded its four-hour objective by two hours, or 50% of that objective. A recovery-time objective concerns restoration time; a recovery-point objective concerns tolerable data loss in time. One does not establish the other.',
    precision_extra='At 200 records per hour, four hours represents 800 scheduled records awaiting processing under the stated assumption. It does not establish lost revenue, permanent loss, or actual incident volume. The proposal still requires validation of its result.',
    phrases='''Lead with the gap | "The test took six hours against a four-hour objective."
State the difference | "That is a two-hour shortfall against the target."
Separate test from incident | "This is a controlled test result, not a live outage."
Translate the operation | "An interruption would delay payroll processing."
Give the assumption | "The illustration assumes 200 scheduled records per hour."
Use the right unit | "Four hours would defer 800 records at that rate."
Reject false loss language | "Deferred records are not automatically lost revenue."
State the request | "I am requesting $30,000 for proposal A."
Name the work | "The scope is recovery automation and repeat testing."
Connect the priority | "A directly addresses the measured recovery shortfall."
Represent the alternative | "B improves alert dashboards but does not directly address this test result."
Avoid a guarantee | "The proposal needs evidence that recovery performance improves."
Define success | "Repeat the agreed test against the four-hour objective."
Disclose remaining risk | "This does not remove every security exposure."
Keep authority explicit | "Funding remains subject to your decision."
Close the briefing | "Approve or decline A on this scope, with results reviewed after testing."''',
    notes='''Objective | A target, not a demonstrated current capability.
Shortfall | Name the direction, amount, and comparison basis.
Would | Marks a conditional consequence, not an observed event.
Records | Not interchangeable with customers, dollars, or lost transactions.
Improvement | Requires evidence after the proposed work.
Approve | Authorizes the stated scope, not every future security initiative.''',
    d='''Which opening is most decision-ready? | A six-hour recovery test missed the four-hour objective; I request $30,000 to automate and retest. | We have many tools and technical concerns. | A live attack has destroyed all payroll data. | The dashboard has attractive features, so all risk is solved. | The strongest opening connects evidence, target, action, and amount without inventing an incident.
Which statement about data loss is supported? | The supplied test does not establish data loss. | Six hours of recovery proves six hours of data loss. | Four-hour RTO guarantees zero data loss. | Eight hundred deferred records were permanently deleted. | Recovery duration and data-loss evidence are distinct, and loss is not established here.
Why does A rank ahead under the stated priority? | It directly addresses the evidenced payroll recovery shortfall. | It costs more, so it must be better. | B can never have any security value. | The test proves every dashboard is useless. | The agreed priority is the measured recovery gap, not price or blanket dismissal of alternatives.
What should follow the proposed automation? | Repeat the agreed recovery test and assess evidence against the objective. | Declare success on purchase alone. | Replace the target with six hours without a decision. | Claim all attacks are now impossible. | A proposed capability improvement needs verification against the defined recovery objective.''',
    dialogue='''Victor | The proposal lists several technical weaknesses. I need to know what decision you want and why this work comes before the dashboard upgrade.
Imani | Our [[recovery test::The recovery test supplies the measured six-hour restoration result, distinct from a live incident or a forecast.]] took six hours against an approved four-hour target. I am requesting thirty thousand dollars for recovery automation and repeat testing to address that measured gap.
Victor | So we missed the target by two hours. Is that a statement about how long payroll data was lost, or how long restoration took?
Imani | It concerns the [[recovery-time objective::The recovery-time objective is the restoration-time target and does not itself measure data loss.]]. We measured restoration time. The test does not establish data loss, and I should not describe the six-hour result as six hours of lost information.
Victor | Then explain the business consequence in operational terms. I want the committee to understand the exposure without hearing an unsupported claim about a current attack.
Imani | A [[service interruption::The service interruption is a conditional disruption used to explain the operational consequence, not an event currently occurring.]] would delay payroll processing. At the stated rate of two hundred scheduled records per hour, a four-hour interruption would defer eight hundred records.
Victor | That is a useful scale. But eight hundred records does not mean eight hundred customers permanently lost, or eight hundred dollars of lost revenue.
Imani | Correct. This is [[deferred processing::Deferred processing means delayed work under the supplied rate assumption, not proven permanent loss or lost revenue.]], not a calculated revenue loss. The rate is an assumption for the illustration, and there is no live incident in this briefing.
Victor | What exactly does the thirty thousand fund? I do not want an approval interpreted as a general authorization for unrelated tooling later in the year.
Imani | The [[funding envelope::The funding envelope is the defined thirty-thousand-dollar request for the stated automation and repeat-testing scope.]] covers proposal A: recovery automation and repeat testing. Any additional scope or funding would need its own decision rather than being implied by this approval.
Victor | The dashboard is ten thousand dollars cheaper. Why not buy that first? Tell me how each option addresses the gap we actually measured.
Imani | It could improve alert visibility, but our agreed [[risk treatment::The proposed risk treatment targets the demonstrated recovery shortfall, which the dashboard alternative does not directly address.]] priority is the evidenced payroll recovery shortfall. A is directly aimed at that gap; B does not directly address this test result.
Victor | How will we know whether the automation works? A purchase receipt will show spending, but it will not show that recovery has become faster.
Imani | The [[success measure::The success measure is recovery performance against the existing four-hour objective in the agreed repeat test.]] is performance in the agreed repeat test against the four-hour objective. We need that evidence before claiming that the restoration capability meets the target.
Victor | If the repeat test meets four hours, what risk remains? I need that limitation in the committee note, not just the improvement headline.
Imani | No. [[Residual exposure::Residual exposure is the risk remaining outside or after this specific improvement, so the proposal is not a complete risk-elimination claim.]] remains, and this work addresses one defined capability. Faster recovery does not establish prevention of every incident or eliminate every consequence of disruption.
Victor | That distinction belongs in the committee note. We have a measured gap, a conditional operational illustration, a bounded proposal, and a validation requirement.
Imani | I will include the [[assurance evidence::Assurance evidence supports the claim that the improved recovery capability actually works after the proposed changes.]] expected from the repeat test and identify any implementation dependencies. The recommendation should show what must be demonstrated, not just what we hope to buy.
Victor | I can now evaluate the request against the agreed priority. Please keep the approval status open until I record the decision on that specific scope.
Imani | Understood. The [[decision request::The decision request asks the authorized sponsor to approve or decline the defined proposal rather than reporting approval as already granted.]] is approval of A for thirty thousand dollars, with results reviewed after testing. I will not describe the funding or the improvement as already secured.''',
    transfer_title='Translate the number without changing its meaning',
    transfer_setup='A recovery test takes five hours against a three-hour objective. At an assumed 100 scheduled records per hour, a three-hour interruption would defer work. No data loss or live incident is established.',
    transfer='''Security: "The test exceeded the objective by ___ hours." | two | Five hours minus the three-hour objective equals a two-hour excess.
Sponsor: "The illustration uses ___ records per hour." | 100 | The briefing supplies an assumed processing rate of one hundred records per hour.
Security: "Three hours would defer ___ records." | 300 | Three hours multiplied by one hundred scheduled records per hour equals three hundred.
Sponsor: "Data loss remains ___." | unestablished | The briefing supplies no evidence establishing data loss from the recovery test.'''))
