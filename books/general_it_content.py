"""Original General IT learner-book cases and language practice."""
from books.authoring import unit

BOOK = dict(
    slug='general-it', title='General IT English', cover_label='Service desk / infrastructure / operations',
    cover_title='General IT', tagline='Clear language for reliable services and accountable decisions.',
    audience='For service-desk staff, systems administrators, infrastructure teams, and technical coordinators.',
    map_intro='Clarify the fault, test the explanation, and communicate the next action precisely.',
    notes_title='Describe the service, not just the server.',
    notes_intro='IT conversations cross technical and business boundaries. A useful message identifies the affected function, the evidence, the operational impact, and the next owner without turning a hypothesis into a confirmed cause.',
    field_notes=[
        ('Translate impact into a specific function', '"The system is down" may mean that one export fails while sign-in and other tasks still work. Clarify the task before choosing the priority.', '"You can sign in, but invoice export fails. Which users and periods have you checked?"'),
        ('Distinguish a clue from a diagnosis', 'A pattern can narrow an investigation without proving its cause. Ask which test supports the proposed explanation.', '"The failure occurs through the VPN; DNS remains one hypothesis, not the established cause."'),
        ('Make status words operational', 'Downloaded, installed, restarted, verified, and complete describe different states. A status update should make the remaining work visible.', '"Installation succeeded on 180 laptops; twelve are offline and eight returned errors."'),
        ('Separate urgency from permission', 'A business deadline can justify prompt escalation but does not itself authorize unrestricted access or an unreviewed production change.', '"I will expedite the reporting-role request; administrator access needs separate justification."')],
    scope_note='Fictional workplace language practice, not instructions for administering real systems or handling live incidents. Follow authorized procedures, access controls, and qualified security review. Use invented accounts and records in practice.',
    sources=[
        dict(title='NIST. SP 800-61 Revision 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management (2025).', url='https://csrc.nist.gov/pubs/sp/800/61/r3/final', note='Background for incident coordination and accountable risk decisions. The fictional cases do not reproduce an operational response procedure.', checked='30 September 2026'),
        dict(title='CISA. Require Multifactor Authentication.', url='https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-multifactor-authentication', note='Background for the distinction between authentication and access permissions. Actual controls depend on the authorized environment.', checked='30 September 2026'),
        dict(title='Kubernetes documentation. Pod Lifecycle.', url='https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/', note='Primary documentation for pod states and readiness terminology. A configured readiness check is not a universal test of user-visible behavior.', checked='30 September 2026'),
        dict(title='Council of Europe. CEFR mediation resources.', url='https://www.coe.int/en/web/common-european-framework-reference-languages/mediation', note='Background for collaborative clarification and explaining technical information across roles.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='IT Service Language, Tickets, and Triage', scene='"The system is down" means the export fails',
    skill='Narrow an ambiguous incident report and agree on an evidence-based update.',
    brief='Ren reports that the finance system is down. Ren can sign in and view invoices, but exporting the current month produces an error. Two colleagues report the same export problem; other users and functions have not been checked. The billing team needs its file by 3 p.m. Asha owns service-desk triage and can escalate the ticket, but cannot promise a repair time.',
    cast='Asha | Service-desk analyst\nRen | Billing coordinator',
    culture=('Clarification is part of taking the problem seriously', 'A user may describe the whole system as down because one blocked function prevents their work. Acknowledge the business impact, then narrow the technical description without arguing about the word down.'),
    a='''Which function is confirmed to fail? | Exporting the current month's invoices | Signing in | Viewing every invoice | Every function for every user | The briefing confirms an export error while sign-in and invoice viewing still work for Ren.
How many people have reported the export issue? | Three | One | Two hundred | Every employee | Ren and two colleagues have reported it; the wider affected population is unknown.
What may Asha promise? | An escalation and a timed update | A repair before 3 p.m. | That no other function is affected | That the billing deadline will be waived | Asha can coordinate triage and escalation, but the briefing gives no confirmed repair time or authority over billing.''',
    vocabulary='''service desk | The contact point coordinating user support. | contact the service desk
ticket | A recorded request or issue for tracking. | update the ticket
triage | Initial assessment of impact, priority, and ownership. | triage an incident
incident | An unplanned disruption or reduction in service. | report a service incident
service request | A request for a routine agreed service. | fulfill a service request
impact | The effect on users or business work. | assess business impact
urgency | How quickly action is needed in the circumstances. | establish the urgency
priority | The relative order or importance assigned to work. | assign a ticket priority
affected user | A person experiencing the reported problem. | identify affected users
scope | The functions, users, or locations included. | establish the incident scope
symptom | An observed sign of a problem. | record the exact symptom
error message | Text identifying or describing an error condition. | capture the error message
reproduce | Make the reported behavior occur again. | reproduce the export failure
workaround | A temporary way to reduce impact without fixing the cause. | verify a workaround
resolution | Restoration or completion according to the agreed criteria. | confirm the resolution
response time | Time until support responds under a defined measure. | distinguish response time from repair time
restoration time | Time until a disrupted service is restored. | estimate restoration time cautiously
escalation | Referral for higher authority or specialist attention. | request a technical escalation
assignment group | The team designated to handle a ticket. | confirm the assignment group
service owner | The role accountable for the service. | notify the service owner
knowledge article | A maintained support reference for a known task or issue. | check the knowledge article
duplicate ticket | Another ticket reporting the same underlying incident. | link a duplicate ticket
status update | A communication of progress and remaining uncertainty. | send a timed status update
closure criterion | A condition required before work is marked closed. | agree on closure criteria''',
    precision='Urgency concerns time pressure; impact concerns consequences and scope. Priority normally reflects an organization\'s agreed assessment, not just the strongest wording in a ticket. A response commitment is not a repair guarantee.',
    precision_extra='A workaround may reduce impact while the cause remains unresolved. Closing a duplicate ticket does not close the underlying incident. State where the authoritative progress record remains available.',
    phrases='''Acknowledge impact | I understand the export is blocking your billing file.
Narrow the function | Which action fails after you sign in?
Check what works | Can you still view the invoices on screen?
Establish scope | Who else has tried the same export and seen the error?
Request evidence | Please send the exact error text through the approved support channel.
Separate deadlines | Your billing deadline is 3 p.m.; the repair time is not yet known.
Offer a commitment | I will escalate the ticket and update you by noon.
Read back the issue | Sign-in and viewing work; the current-month export fails for three reported users.
Check a workaround | Has anyone verified that the alternative produces the required file?
Avoid a promise | I cannot confirm a restoration time before the technical assessment.
Explain escalation | I am asking the application team to investigate this function.
Preserve uncertainty | Other functions and users have not yet been checked.
Link related reports | I will link the reports so the investigation has one shared record.
Confirm the owner | Which team is accepting the next investigation step?
Define closure | We will confirm that the required export works before closing the incident.
Close the update | The next message will include findings, outstanding questions, and the next owner.''',
    notes='''Can versus cannot | Paired statements such as "can sign in but cannot export" describe the boundary of failure.
So far | "Three users so far" preserves the possibility that the scope is wider.
By versus at | "By noon" sets a latest time; "at noon" names a specific time.
Reported versus affected | Three reported users does not prove that only three users are affected.
Will update | A promise to update names a controllable communication action, not an unverified repair outcome.
Present perfect | "Who has tried the export?" asks about attempts relevant to the current investigation.''',
    d='''Which ticket summary is most accurate? | Current-month export fails for three reported users; sign-in and viewing work for Ren. | The entire finance platform is unavailable to every user. | Only Ren is affected and all other functions are verified. | The export has already been restored. | The accurate summary preserves confirmed functions and reported scope without extending the evidence.
Which statement promises communication rather than repair? | I will send a progress update by noon. | The export will be fixed by noon. | Every user will be unblocked by noon. | No technical investigation will be needed. | An update can report incomplete findings; it does not guarantee that service will be restored.
Which question establishes business impact? | What work cannot proceed without that file? | What color is the error window? | When was the user's job title changed? | Which support analyst answered first? | The blocked business task explains the consequences that triage must assess.
What does "three reported users" avoid claiming? | That the affected population is limited to three | That anyone has reported a fault | That the issue has an impact | That a ticket can be escalated | Reported counts identify known reports, not a verified upper limit on all affected users.''',
    dialogue='''Ren | The finance system is down, and billing needs the monthly file by three. I have already tried twice, so this is becoming urgent for us.
Asha | I understand the business [[impact::Impact describes the work disrupted, here preparation of the billing file, rather than merely the technical error.]]. To route this correctly, can you tell me which action fails after you open the application?
Ren | I can sign in and see the invoices. When I choose the current month and export, I get an error instead of the file.
Asha | That narrows the [[scope::Scope identifies the affected function and population; the current evidence points to export rather than complete application unavailability.]]. I will record an export failure, while keeping the billing deadline visible in the ticket.
Ren | Two colleagues have the same problem. We have not checked older periods or asked the other office. Does that mean it is a major outage?
Asha | It means three users have reported this [[symptom::A symptom is the observed failure; its extent and underlying cause still need assessment before classifying the whole incident.]]. I need the agreed impact assessment before assigning a broader classification, but I can escalate now.
Ren | Please do. Would a screenshot help? It shows invoice details, so I do not want to paste it into the general team chat.
Asha | Use the approved support channel and follow its handling rules. The exact [[error message::The error message gives diagnostic wording; it should be recorded without unnecessarily widening access to invoice data.]] and approximate time will help the application team locate the event.
Ren | Someone suggested copying the visible rows manually. I am worried that might omit invoices across multiple pages, and we have not checked the totals.
Asha | Then it is an unverified [[workaround::A workaround reduces impact temporarily; an unverified manual copy may not produce the complete file needed for billing.]], not a solution I can recommend as complete. I will ask the service owner to assess an acceptable alternative.
Ren | Can I tell my manager the technical team will fix it before three? They are asking me for a firm answer about the billing run.
Asha | I cannot promise a [[restoration time::Restoration time concerns when service works again; it is different from a support response or scheduled update.]] before their assessment. I can commit to a progress update by noon, even if the cause remains unknown.
Ren | That is useful. Please make the distinction explicit in the ticket because people sometimes treat an update time as the expected repair time.
Asha | I will. I am sending a technical [[escalation::Escalation brings the application specialists into the investigation; it does not itself establish a repair deadline.]] with the confirmed scope, the error details, and your business deadline as separate fields.
Ren | My colleagues each opened a ticket. Should they close theirs now, or leave them open so the team can see that this is not just me?
Asha | I will link them to the main record as related reports. A [[duplicate ticket::A duplicate ticket may refer to the same underlying incident; linking it preserves evidence without treating it as a separate resolved fault.]] can be managed without suggesting that the underlying export problem is resolved.
Ren | Before we finish, can you read back what you are sending? I want the application team to understand that viewing invoices is not the blocked task.
Asha | Certainly. Sign-in and viewing work for you; current-month export fails for three reported users. Other functions remain unchecked. Billing needs the file by three, and the [[assignment group::The assignment group identifies the team handling the next investigation step rather than the business user awaiting the result.]] is the application support team.
Ren | That captures it. Please include me on the noon update. Once they say it is fixed, I can verify the export and compare the file totals.
Asha | I will record that as the [[closure criterion::A closure criterion states the evidence needed before marking the incident resolved, here a working export with the required file checks.]]. We will distinguish a reported fix from your confirmation that the required task works again.''',
    transfer_title='Printing fails, but document editing still works',
    transfer_setup='A user can edit and save documents but cannot print to one office printer. Another printer has not been tested. The user needs printed copies for a 2 p.m. meeting.',
    transfer='''Analyst: "The confirmed ___ is printing to that device, not document editing." | failure | The user can edit and save; only printing to the named device is confirmed to fail.
User: "I have not verified an alternative ___ yet." | printer | Another printer is untested, so it cannot be presented as a confirmed workaround.
Analyst: "I will report the meeting deadline separately from the unknown ___ time." | restoration | The meeting's deadline does not establish when the printer service will be restored.
User: "Please give me a timed ___ even if the repair is still pending." | update | A progress update is a controllable communication action and can accurately report an unfinished repair.'''))

BOOK['units'].append(unit(
    title='Networks, Connectivity, and Root-Cause Hypotheses', scene='The VPN pattern is a clue, not a DNS diagnosis',
    skill='Challenge premature certainty and agree on comparisons that separate hypotheses.',
    brief='The staff portal works from the office network but fails for four people connected through the virtual private network (VPN). The same portal address is used. Nobody has checked name resolution, routing, or access-policy logs for those requests. Eli says DNS must be the cause. Nia coordinates network investigation. The team has an approved diagnostic process and must not change production settings merely to test a guess.',
    cast='Eli | Support engineer\nNia | Network engineer',
    culture=('Question the inference, not the colleague', 'A confident diagnosis can spread faster than its evidence. Acknowledge the useful pattern and ask what would distinguish competing explanations. "What supports DNS over routing?" preserves the investigation without making disagreement personal.'),
    a='''Which pattern is established? | Office access works; four VPN users report failure. | Every internet connection fails. | DNS returns the wrong address. | A firewall rule has been identified. | The reports establish an access-path difference, but no specific network mechanism has yet been tested.
Which cause is confirmed? | None of the proposed causes | DNS | Routing | An access-policy rule | The briefing explicitly says the relevant checks have not been performed.
What constraint applies to investigation? | Follow the approved process without changing production on a guess. | Disable production controls immediately. | Treat confidence as evidence. | Tell users that every path is healthy. | The case permits approved diagnosis, not speculative production changes or unsupported status claims.''',
    vocabulary='''VPN | Virtual private network; a connection providing a defined private access path. | connect through the VPN
DNS | Domain Name System; the system that resolves names to records. | investigate a DNS hypothesis
name resolution | Translating a name into the records needed for a connection. | verify name resolution
IP address | A numerical network address used by the Internet Protocol. | compare resolved IP addresses
hostname | A name identifying a host or service endpoint. | confirm the hostname
resolver | A service that answers or obtains DNS responses. | identify the configured resolver
cache | Stored data reused to avoid repeating work. | inspect a cached response
TTL | Time to live; a lifetime limit, with meaning depending on context. | check a DNS record's TTL
routing | Selection of paths for network traffic. | review routing evidence
route | A path or forwarding rule for reaching a destination. | inspect the relevant route
gateway | A system providing a path between networks or services. | identify the gateway
subnet | A defined subdivision of an IP network. | compare affected subnets
firewall | A control that permits or blocks network traffic under rules. | review firewall logs
access policy | Rules determining permitted access under stated conditions. | check the access policy
port | A numbered transport endpoint associated with a service. | identify the service port
packet loss | Failure of transmitted network packets to reach their destination. | measure packet loss
round-trip time | Time for a request and return response across a path. | compare round-trip times
timeout | Expiry of a waiting period before a response completes. | record a connection timeout
connection refusal | An explicit rejection of a connection attempt. | distinguish refusal from timeout
TLS | Transport Layer Security; protection for communication in transit. | inspect a TLS handshake error
certificate | A signed digital statement used to bind identity and a public key. | review a certificate warning
proxy | An intermediary handling requests between client and destination. | identify the proxy path
reachability | Whether a destination can be contacted under specified conditions. | test service reachability
diagnostic hypothesis | A proposed explanation that still requires testing. | test a diagnostic hypothesis''',
    precision='A timeout, a refused connection, and a certificate warning are different observations. "The VPN is connected" does not establish that every destination is reachable. Name the source, destination, and observed result.',
    precision_extra='DNS, routing, and access policy are different parts of connectivity. A working office path can narrow the comparison but does not by itself identify which VPN-path component differs. TTL has protocol-specific meanings.',
    phrases='''Acknowledge a pattern | The reports do point to a difference between access paths.
Challenge certainty | What evidence establishes DNS rather than another path issue?
State a hypothesis | Name resolution is one explanation we still need to test.
Request exact wording | Was it a timeout, a refusal, or a certificate warning?
Define a comparison | Compare the same destination from the two approved paths.
Preserve controls | We should not change production settings to test an unverified guess.
Name missing evidence | We have not checked the resolver or policy logs for those requests.
Close the inference | The pattern narrows the investigation; it does not yet establish a cause.
Check the source | Were all four reports from the same VPN profile?
Distinguish layers | A successful name lookup does not prove application access.
Limit an observation | The portal worked for this office test at this time.
Avoid a universal claim | We have not tested every VPN user or destination.
Ask for timestamps | Please include the time and time zone for each failed request.
Assign a test | Who will collect the approved comparison and record the results?
Report a negative result | That check did not support the DNS hypothesis.
Preserve the record | Keep the observed results separate from the proposed explanation.''',
    notes='''Must versus may | "DNS must be the cause" expresses certainty; "DNS may be involved" presents a possibility.
Rather than | Use "what supports DNS rather than routing?" to compare explanations without claiming either is established.
From versus through | "From the office" identifies the source; "through the VPN" identifies a path.
Did not support | A negative check weakens a particular explanation without necessarily proving every alternative.
Which error | Asking for the exact error prevents different symptoms from being collapsed into one label.
At this time | Time qualifications matter because intermittent faults can change between checks.''',
    d='''Which statement preserves the evidence boundary? | The VPN path is associated with the reported failures; the cause is unconfirmed. | DNS has been proven faulty because office access works. | Every network component is broken. | A connected VPN guarantees portal access. | The observed path difference is real, but the specific cause still requires testing.
Which question distinguishes symptoms? | Did the request time out, get refused, or show a certificate warning? | Was the portal's name familiar? | Did all users describe their frustration identically? | Was the ticket created during a meeting? | The three outcomes point to different observations relevant to diagnosis.
What does a successful name lookup establish? | That this lookup returned a result under the tested conditions | That the application must be reachable | That the user's permissions are correct | That no packet can be lost | Name resolution is one step and cannot certify later connectivity or authorization.
Which commitment is appropriate before diagnosis? | I will report the comparison results and remaining hypotheses. | I will fix DNS before confirming it is involved. | I will remove every access control today. | I will certify all VPN traffic as healthy. | A result-based update is achievable without promising an unverified repair or bypassing controls.''',
    dialogue='''Eli | Four VPN users cannot reach the staff portal, while the office test works. This must be DNS. I am ready to put that in the incident update.
Nia | The access-path pattern is useful, but DNS is still a [[hypothesis::A hypothesis is a proposed explanation; the path difference alone does not establish which network component caused it.]]. What result distinguishes name resolution from routing or an access-policy issue?
Eli | We do not have that result yet. The reports all use the same portal address, and everyone says the page will not open after connecting.
Nia | Then ask for the exact [[symptom::The symptom is the observed failure, such as a timeout or warning, not the user's general description that the page will not open.]]. A timeout, a refusal, and a certificate warning should not be recorded as the same observation.
Eli | I can collect the wording and timestamps. Does the fact that their VPN says connected tell us that the connection to the portal is available?
Nia | No. It confirms that connection state, not portal [[reachability::Reachability concerns contacting the particular destination under the tested conditions; VPN connection status alone does not establish it.]]. We need to follow the approved diagnostic process for the destination they actually need.
Eli | Someone suggested changing the resolver for all VPN users and seeing whether the complaints stop. That would be a quick way to test the theory.
Nia | A production change has its own approval requirements. First collect the authorized comparison of [[name resolution::Name resolution maps the portal name to records; comparing results helps assess the DNS hypothesis without assuming it is correct.]] and the relevant path evidence without altering everyone else's settings.
Eli | Understood. I will ask whether all four people use the same VPN profile. If they do, that may help us narrow where to compare the configuration.
Nia | Yes, and include the source network and [[hostname::The hostname identifies the specific named destination; a comparable investigation needs the same target rather than merely the same application description.]]. We want comparable requests, not a working office test against a different address.
Eli | If the lookup gives the same address on both paths, should we remove DNS from the report completely and say it is definitely the firewall?
Nia | No. Record what that check establishes, then review the next evidence. A matching answer does not automatically prove an [[access policy::An access policy governs permission under specified conditions; it is another possible explanation that requires its own evidence.]] caused the failure.
Eli | That makes sense. I should also distinguish the portal being slow from a connection that never completes, because the users may have used the same wording.
Nia | Exactly. Record a [[timeout::A timeout means the waiting period expired; it differs from a completed but slow response or an explicit refusal.]] only if that is the actual result. Do not infer it from a user saying the request took too long.
Eli | Who should collect the approved network checks? I can gather user reports, but I do not have permission to inspect every network device involved.
Nia | I will coordinate the network evidence and name the appropriate owner for each boundary. Include the [[time zone::The time zone makes timestamps comparable across logs and reports; a clock time alone can point investigators to the wrong events.]] so we can match the requests to the correct records.
Eli | I will revise the update: four reports through the VPN, one successful office test, exact errors being collected, and no verified root cause yet.
Nia | Good. The [[comparison::A comparison uses specified, comparable conditions; it can narrow explanations without turning an untested alternative into a finding.]] should show what differs and what remains unchanged. That gives the next team something concrete to investigate.
Eli | And if the checks do not support DNS, I will say that directly instead of defending the first theory. The update will still explain what we learned.
Nia | Exactly. A useful [[diagnosis::A diagnosis is an evidence-based explanation; revising an early theory is part of reaching it rather than a failure of the investigation.]] depends on the evidence, not on keeping the first guess. We can be decisive about the next test while remaining uncertain about the cause.''',
    transfer_title='One browser reports a certificate warning',
    transfer_setup='The same portal opens in an approved office test, while a remote user reports a certificate warning. No certificate or proxy review has occurred. The team must describe the actual warning without telling the user to bypass it.',
    transfer='''Analyst: "The reported symptom is a certificate ___, not a confirmed DNS failure." | warning | The user reported a specific warning; the scenario contains no DNS finding.
Engineer: "Record the hostname and the ___ with its time zone." | timestamp | A timestamp with time zone helps authorized reviewers match the reported event to the appropriate records.
Analyst: "The proxy path is another ___ to investigate." | hypothesis | The proxy has not been reviewed, so its involvement is a proposed explanation rather than a conclusion.
Engineer: "Follow the approved process; do not ask the user to ___ the warning." | bypass | The case authorizes investigation, not circumventing a security warning or changing trust decisions.'''))

BOOK['units'].append(unit(
    title='Identity, Access, and Permissions', scene='A report request does not justify administrator access',
    skill='Clarify the required task and refuse excessive access while offering a legitimate route.',
    brief='A temporary analyst, Jo, needs to download a monthly report. Jo requests administrator access because the current account shows an access-denied message. A reporting role may allow the required download, but its exact permissions have not been verified. Imani handles access requests. The manager can confirm Jo\'s business need; the system owner approves the role. The assignment ends on 30 November.',
    cast='Jo | Temporary analyst\nImani | Identity and access analyst',
    culture=('Offer a route, not just a refusal', 'A user may ask for administrator rights as a shortcut because they do not know which role fits the task. Clarify the action, explain the authority boundary, and name the narrower request and approval needed. Urgency does not establish permission.'),
    a='''What task does Jo need to perform? | Download a monthly report | Change all user accounts | Reconfigure the system | Approve other users' roles | The stated need is a report download, not general administrative control.
Who approves the system role? | The system owner | Jo alone | Any colleague with access | The manager without system review | The manager confirms business need, while the system owner has role-approval authority in this case.
What remains unverified? | Whether the reporting role permits the download | Whether Jo is temporary | The assignment end date | Whether an access request exists | The reporting role is a possible fit, not yet a verified authorization solution.''',
    vocabulary='''identity | The representation of a user or service in a system. | verify the account identity
authentication | Establishing that a claimant controls the required identity evidence. | complete authentication
authorization | Permission to perform an action on a resource. | check authorization
permission | An allowed action or access right. | grant a specific permission
role | A defined collection of access rights or responsibilities. | assign a reporting role
RBAC | Role-based access control; access organized through defined roles. | review an RBAC assignment
least privilege | Access limited to what is needed for the task. | apply least privilege
administrator | A role with broad system-management permissions. | justify administrator access
privileged access | Access allowing sensitive or powerful actions. | review privileged access
entitlement | A specific granted right to use a resource or capability. | review account entitlements
provisioning | Creating or assigning accounts and access. | complete approved provisioning
deprovisioning | Removing accounts or access no longer required. | schedule deprovisioning
access review | A check that granted access remains appropriate. | conduct an access review
access request | A recorded request for specified permissions. | submit a scoped access request
business justification | The work-related reason supporting a request. | document the business justification
approver | The person authorized to approve a request. | identify the correct approver
expiration | The point at which an entitlement or credential ends. | set an access expiration
temporary access | Access granted for a defined limited period. | request temporary access
separation of duties | Dividing incompatible responsibilities to reduce risk. | preserve separation of duties
SSO | Single sign-on; using one authentication session across services. | troubleshoot an SSO session
MFA | Multifactor authentication; use of distinct factor types. | complete MFA verification
service account | An identity used by an application or automated process. | identify the service-account owner
audit log | A record of relevant actions for review. | inspect the access audit log
access denied | A message indicating that an attempted action was not permitted. | report an access-denied message''',
    precision='Authentication establishes identity evidence; authorization governs permitted actions. Being able to sign in does not imply permission to download every report. A role name alone does not prove its actual rights.',
    precision_extra='Business justification explains why access is needed. Approval establishes permission under the stated process. Temporary access needs a defined end or review condition; it should not silently become permanent.',
    phrases='''Clarify the action | Which report do you need, and what action must you perform?
Separate identity and access | You can sign in; the download permission is a different question.
Refuse proportionately | I cannot justify administrator rights from the stated reporting task.
Offer a narrower route | Let us verify whether the reporting role covers that download.
Name the approver | Your manager confirms the need; the system owner approves the role.
Limit duration | The requested access should match the assignment ending on 30 November.
Preserve uncertainty | The role may fit, but its permissions still need checking.
Confirm the request | I will submit the task, resource, duration, and approval route together.
Avoid credential sharing | Please use your own approved account rather than another person's credentials.
Check existing rights | Which entitlement is currently assigned to your account?
Explain least privilege | The request should provide the required action without unrelated control.
Handle urgency | I can flag the deadline without bypassing the approval process.
Check completion | After provisioning, confirm the authorized report action works.
Record an end | Who will verify removal when the assignment finishes?
Distinguish roles | A reporting role and an administrator role serve different purposes.
Close clearly | Approval is pending; the request has been submitted, not granted.''',
    notes='''May versus does | "The role may allow download" signals an unverified fit; "the role allows download" claims a confirmed permission.
Need to versus need rights to | Ask for the required task before adopting the user's proposed permission level.
Not yet granted | This states pending authorization without implying permanent refusal.
Until | "Until 30 November" sets an end boundary; specify local handling of the date in the real request.
Can versus authorized to | Technical capability is not the same as organizational permission.
Role of because | Give the concrete reason: "Administrator access is broader than this task requires."''',
    d='''Which request is best scoped? | Access to download the named monthly report for the assignment period | Permanent administrator access to all systems | Permission to use a colleague's account | Access to every financial record because one export fails | The first request states a resource, action, and duration without adding unrelated permissions.
Which statement distinguishes authentication from authorization? | Signing in does not prove permission to download the report. | Signing in grants every application permission. | A role name proves every entitlement. | MFA approval replaces system-owner approval. | Identity verification and permission to perform a specific action are separate controls.
Who should confirm business need in this case? | Jo's manager | An unrelated account holder | The report download itself | The service account | The briefing assigns business-need confirmation to the manager and role approval to the system owner.
Which status is accurate before approval? | Submitted for review; access has not been granted. | Approved because the request is urgent. | Provisioned because the manager received the message. | Permanent because no removal date was discussed. | Submission starts review; it does not establish approval, provisioning, or permanent entitlement.''',
    dialogue='''Jo | I need administrator access to finish the monthly reporting work. I can sign in, but the download gives me an access-denied message every time.
Imani | Let us identify the required [[permission::A permission authorizes a particular action; the required download does not itself justify broad administrative control.]] first. Which report are you downloading, and do you need to change anything in the system?
Jo | It is the monthly sales summary. I only need to download it and analyze the file. I am not changing accounts or system settings.
Imani | Then administrator rights would be broader than that [[business justification::The business justification states the work-related need, here report analysis, rather than adopting the requested privilege level without examination.]]. There may be a reporting role that provides the specific action.
Jo | I assumed signing in meant I already had access and the download error was just a technical fault. Are those separate parts of the process?
Imani | Yes. [[Authentication::Authentication establishes identity evidence; it does not automatically authorize every action within the application.]] gets you through the identity check. Authorization determines which resources and actions the account is allowed to use afterward.
Jo | Could you assign the reporting role now and let me check whether it works? My manager needs the analysis, and I am only here temporarily.
Imani | The system owner must approve it first. I also need to verify its actual [[entitlements::Entitlements are the specific granted rights attached to the role or account; a helpful role name does not prove the necessary download right.]], because the role name alone does not confirm that download is included.
Jo | My manager can confirm the work is required. Does that approval cover the role too, or does the system owner need a separate request?
Imani | In this process they have different responsibilities. The manager confirms the need, and the system owner is the [[approver::The approver is the person authorized to make this access decision; confirming a business need is not the same decision.]] for the system role.
Jo | That is clear. The assignment ends on 30 November. I do not expect to need the system afterward unless the contract is formally extended.
Imani | I will include an [[expiration::Expiration specifies when the entitlement should end, matching temporary access to the stated assignment rather than leaving it open indefinitely.]] aligned with that assignment and the required review route if it changes.
Jo | While we wait, a colleague offered to download the file using their account. Is that the same as sharing their password so I can do it myself?
Imani | Those are different proposals, and neither should bypass the approved process. Do not share [[credentials::Credentials establish access to an identity; sharing them can obscure who acted and does not authorize the recipient's use.]]. Ask the report owner whether an authorized delivery route is permitted.
Jo | I will do that. Please note the deadline in the request, but I understand that urgency does not automatically make administrator access appropriate.
Imani | Exactly. We can expedite review while preserving [[least privilege::Least privilege limits access to the legitimate task; urgency affects handling speed, not the necessary breadth of permissions.]]. I will submit the report name, required action, duration, and business justification together.
Jo | When the role is approved, should I assume the request is complete as soon as I receive the confirmation message from the system owner?
Imani | Approval and [[provisioning::Provisioning is the actual assignment of the approved access; an approval message does not prove that assignment has already occurred.]] are separate states. After the role is assigned, confirm that the authorized download works with your own account.
Jo | And at the end of November, the access should be removed unless an extension is reviewed. Please include who checks that so it is not forgotten.
Imani | I will record [[deprovisioning::Deprovisioning removes access no longer required; assigning its ownership makes the temporary-access end condition actionable.]] ownership. For now the status is submitted for review, not granted, and we have a legitimate route that matches the work you actually need to do.''',
    transfer_title='A contractor needs read-only dashboard access',
    transfer_setup='A contractor needs to view one project dashboard for two weeks, not edit it. The project manager confirms the need; the dashboard owner approves access. No approval has yet been recorded.',
    transfer='''Analyst: "The requested action is ___, not editing or administration." | viewing | The contractor's stated task is to view one dashboard; additional control is not justified by that task.
Manager: "I can confirm the business need, but the owner provides ___." | approval | The case separates confirmation of need from the owner's authorization decision.
Analyst: "The request will include a two-week ___." | duration | The access period should match the temporary task instead of becoming indefinite.
Manager: "Until review is complete, describe the access as ___." | pending | No approval has been recorded, so granted or active would overstate the current status.'''))

BOOK['units'].append(unit(
    title='Cloud, Infrastructure, and Cost-Aware Operations', scene='The cheaper estimate leaves out backup storage',
    skill='Compare incomplete estimates and qualify a recommendation without inventing missing costs.',
    brief='Two monthly cloud planning estimates cover the same application. Option A is $800 and excludes backup storage. Option B is $1,050 and includes backup storage. Transfer charges and support coverage have not been confirmed for either option. Jordan prepares the comparison; Sal owns infrastructure planning. These are fictional estimates, not provider prices. No purchasing decision has been approved.',
    cast='Jordan | Cloud operations analyst\nSal | Infrastructure planning lead',
    culture=('Comparable totals require comparable scope', 'A low headline figure can be accurate yet unsuitable for a decision when inclusions differ. Identify missing line items without accusing the estimator of deception. Ask for a like-for-like comparison and keep unknown amounts unknown.'),
    a='''Which cost difference is confirmed? | Only Option B includes backup storage. | Option A includes all support. | Transfer charges are zero for both. | Both quotes cover identical items. | The briefing identifies backup inclusion as different and leaves transfer and support unconfirmed.
What is the headline difference? | $250 per month | $1,850 per month | $800 per year | No difference | Subtracting $800 from $1,050 gives $250, but that is not a verified like-for-like saving.
Which conclusion is premature? | Option A is the cheaper complete solution. | Option B's estimate is $1,050. | Option A omits backup storage. | No purchase is approved. | The complete scope and missing charges are unresolved, so the cheaper headline cannot establish the cheaper complete service.''',
    vocabulary='''cloud service | Computing capability delivered through a service model. | compare cloud services
infrastructure | The underlying computing and network resources. | plan infrastructure capacity
instance | A running or configured unit of computing capacity. | size a compute instance
virtual machine | A software-defined computing environment emulating a machine. | provision a virtual machine
region | A provider-defined geographical deployment area. | choose an approved region
availability zone | A provider-defined location grouping within a region. | compare availability-zone designs
object storage | Storage that manages data as objects with metadata. | estimate object-storage usage
block storage | Storage presented as addressable blocks. | size block-storage volumes
snapshot | A point-in-time representation of data or system state. | document a snapshot policy
backup | A retained copy intended to support recovery. | include backup storage
retention period | The length of time data is kept. | confirm the retention period
restore test | A check that retained data can be recovered as required. | schedule a restore test
RPO | Recovery point objective; tolerated data-loss interval. | agree on the RPO
RTO | Recovery time objective; target time to restore service. | agree on the RTO
egress | Data leaving a defined network or service boundary. | estimate egress charges
ingress | Data entering a defined network or service boundary. | identify ingress traffic
consumption | Measured resource use over a period. | forecast resource consumption
reservation | A commitment or capacity allocation under stated terms. | compare reservation terms
on-demand | Resource use without the particular advance commitment being discussed. | estimate on-demand usage
right-sizing | Matching resource allocation to workload needs. | assess right-sizing options
cost allocation | Assignment of expenses to services or owners. | document cost allocation
line item | An individual entry in an estimate or bill. | compare each line item
exclusion | A cost or service left outside the stated scope. | disclose estimate exclusions
total cost | Combined cost under explicitly defined inclusions. | compare like-for-like total cost''',
    precision='The $250 difference compares two headline estimates with different inclusions. It is not a verified saving for equivalent services. RPO describes a data-loss interval; RTO describes a restoration-time target.',
    precision_extra='A snapshot or stored backup does not prove that recovery has been tested. Provider pricing, region terminology, and commitment conditions vary; these fictional amounts teach comparison language, not purchasing advice.',
    phrases='''Identify the mismatch | The estimates do not include the same services.
State the known difference | Option A excludes backup storage; Option B includes it.
Limit the arithmetic | The headline difference is $250, not a confirmed like-for-like saving.
Request a common basis | Can we compare both options against the same workload and retention assumptions?
Keep uncertainty visible | Transfer charges remain unconfirmed for both options.
Ask about coverage | Does support cover the hours and response level we need?
Separate cost and recovery | Including storage does not establish that restoration has been tested.
Bound the recommendation | I cannot recommend the lower total until the missing items are priced.
Check a unit | Is that per month, per stored unit, or per transfer volume?
Expose an assumption | Which usage pattern does this estimate assume?
Ask about commitments | What term or minimum spend is attached to that figure?
Preserve exclusions | Put the excluded items next to the headline total.
Avoid invented numbers | I will mark the amount unknown rather than enter zero.
Clarify an objective | Is that the tolerated data-loss interval or the restoration-time target?
Compare sensitivity | Show how the estimate changes under the agreed higher-use scenario.
Close the comparison | We will reconcile the scope before asking for a purchasing decision.''',
    notes='''Includes versus costs | A quoted amount and its included services must be reported together.
Unknown versus zero | "Not confirmed" is missing information, not a numerical zero.
Per | State the billing unit explicitly: per month, per gigabyte, or per request.
Would save | Conditional savings depend on the assumptions; name those assumptions before using would save.
Same as | "The same retention period as Option B" creates a precise comparison condition.
Not until | "Not until exclusions are priced" sets a clear prerequisite for the recommendation.''',
    d='''Which comparison is defensible now? | A is $250 lower before its missing backup and other unconfirmed costs are resolved. | A saves exactly $250 for equivalent coverage. | B costs $250 more solely because its service is better. | Transfer costs are included because no amount is shown. | The first statement gives the arithmetic while preserving the unequal scope and unknown items.
How should an unconfirmed transfer charge appear? | Unknown, with the required assumption identified | Zero, because nobody has quoted it | Included, because cloud services usually bundle everything | Irrelevant, because the headline is monthly | Missing information must remain explicit; entering zero or included would invent a cost assumption.
Which question concerns RPO? | How much recent data loss can the service tolerate? | How quickly must the service be restored? | How many people attend the review? | Which currency symbol appears first? | RPO concerns the tolerated data-loss interval; restoration time is the different RTO concept.
What does included backup storage fail to establish? | That a successful restore has been tested | That storage is in the quoted scope | That the quote contains a backup line | That the estimate is monthly | Storing a backup and demonstrating recoverability are separate matters.''',
    dialogue='''Jordan | Option A is $800 a month and Option B is $1,050. I was going to recommend A as a $250 monthly saving for the application.
Sal | Before recommending it, compare the [[inclusions::Inclusions identify what the quoted amount covers; unequal included services make headline totals unsuitable as equivalent-service savings.]]. I see backup storage in B, but not in A. Are they priced on the same basis?
Jordan | Not yet. A's estimate explicitly excludes backup storage. I also have not confirmed transfer charges or support coverage for either option, so the comparison is incomplete.
Sal | Then $250 is the [[headline difference::The headline difference is the subtraction of the displayed estimates, not a verified saving after aligning their scope.]], not an established saving. We should keep the arithmetic but qualify what it means.
Jordan | I will request the missing backup amount. Should I put zero against transfer charges until the provider confirms them, so the spreadsheet totals correctly?
Sal | No. Mark them [[unknown::Unknown preserves missing information; zero would falsely assert that the charge has been established as nothing.]] and record the assumed traffic. A working formula should not turn an unanswered pricing question into a free service.
Jordan | Understood. The workload estimate also assumes the current data volume. We expect growth, but the higher-use scenario has not been agreed with the application owner.
Sal | Obtain that assumption before adjusting the figure. Compare [[consumption::Consumption is actual or assumed resource use; estimates are meaningful only when the usage basis is explicit.]] on the same basis for both options rather than quietly giving one a smaller workload.
Jordan | For backups, is matching the storage amount enough? B includes a line for retained copies, but I have not seen evidence of a restore test.
Sal | Storage and recoverability are different. Ask about the agreed [[retention period::The retention period states how long copies are kept; it affects scope and cost but does not prove successful recovery.]], recovery requirements, and the process for checking restoration under the approved plan.
Jordan | The application owner mentioned an RPO and an RTO. I want to make sure I ask the right question rather than using those labels interchangeably.
Sal | The [[RPO::Recovery point objective concerns the tolerated interval of data loss; it is distinct from the time needed to restore the service.]] concerns how much recent data loss is tolerable. RTO concerns the target restoration time. Confirm both with the authorized owner.
Jordan | I will also check whether either price assumes a long commitment. A may be an on-demand estimate, while B may rely on an advance reservation.
Sal | Exactly. Any [[commitment::A commitment can impose term or spending conditions; the displayed monthly equivalent does not fully describe those obligations.]] belongs beside the monthly figure. A lower unit rate can involve obligations that change the decision.
Jordan | What about support? The summary says support available, but it does not specify coverage hours or which incidents receive the quoted response level.
Sal | Treat that as another [[line item::A line item separates a cost or service component so its coverage and assumptions can be compared explicitly.]] needing clarification. Availability is not the same as included coverage that meets this application's needs.
Jordan | Then today's note should say the estimates are provisional, identify the missing components, and postpone the recommendation until the scopes are aligned.
Sal | Yes. We are aiming for [[like-for-like::Like-for-like means comparing equivalent scope and assumptions, rather than selecting between superficially similar but different totals.]] totals and clearly stated differences. We do not need to pretend the two options are identical if meaningful differences remain.
Jordan | I will prepare a table with each inclusion, exclusion, assumption, and unresolved amount. The purchasing request will wait until the owners confirm the comparison.
Sal | Good. That creates an [[audit trail::An audit trail records the assumptions and decisions supporting the estimate, so later reviewers can understand why a recommendation was made.]] for the recommendation. We can explain what changed when the final numbers arrive instead of defending a saving we never actually verified.''',
    transfer_title='An annual software quote excludes migration',
    transfer_setup='Quote A is $12,000 annually without migration support. Quote B is $14,000 with migration support. The required migration scope and any additional charges remain unconfirmed.',
    transfer='''Analyst: "The $2,000 difference compares unequal ___." | scope | The two quotes differ in migration coverage, so their totals do not yet describe equivalent services.
Manager: "List migration as an ___ from A, not an assumed free service." | exclusion | Quote A explicitly leaves migration out; treating it as free would invent an inclusion.
Analyst: "I will keep the additional amount marked ___ until it is confirmed." | unknown | No amount has been established, so unknown is more accurate than zero.
Manager: "Then request a ___ comparison before recommending a purchase." | like-for-like | Aligning the migration scope and other assumptions makes the cost comparison decision-relevant.'''))

BOOK['units'].append(unit(
    title='Endpoints, Servers, Patching, and Configuration Management', scene='Ninety percent installed is not complete',
    skill='Report deployment states accurately and define evidence needed for completion.',
    brief='A patch was assigned to 200 managed laptops. The console reports successful installation on 180, twelve laptops were offline, and eight returned installation errors. Post-installation verification has not been completed on all successful devices. Arun manages endpoints; Casey coordinates the rollout. A manager asks whether the deployment is complete. There is no approved exception for the remaining twenty laptops.',
    cast='Arun | Endpoint administrator\nCasey | Rollout coordinator',
    culture=('Use state labels that preserve remaining work', 'A broad word such as done can hide devices that were offline, failed, or still require verification. Report mutually understandable states and counts. Do not describe a percentage as completion unless the agreed criteria actually permit it.'),
    a='''How many laptops report successful installation? | 180 | 200 | 192 | 188 | The console reports 180 successes; offline devices and installation errors are separate remaining groups.
What is known about the remaining twenty? | Twelve were offline and eight returned errors. | All twenty are approved exceptions. | All twenty passed verification. | All twenty were removed from the inventory. | The briefing gives two unresolved states and explicitly says no exception has been approved.
Why is complete premature? | Not all devices are installed and verified under the stated criteria. | The patch has not been assigned to any device. | Every installation has failed. | The console cannot show counts. | Installation remains unresolved for twenty devices, and verification is not complete for all reported successes.''',
    vocabulary='''endpoint | A user device or other terminal system on a network. | manage an endpoint
managed device | A device enrolled under an organization's management controls. | verify the managed-device inventory
asset inventory | A record of devices and their relevant attributes. | reconcile the asset inventory
patch | A software update intended to correct or change behavior. | deploy an approved patch
patch level | The installed state of relevant software updates. | confirm the patch level
deployment | Distribution and application of a configuration or update. | track deployment progress
installation | Placement and setup of software on a system. | confirm installation status
verification | Checking evidence that the required state has been achieved. | complete post-installation verification
reboot | Restarting a system. | identify a pending reboot
maintenance window | An approved period for planned service work. | schedule a maintenance window
offline | Not currently connected or available to the management system. | identify offline devices
retry | Another attempt after an earlier incomplete or failed action. | schedule an authorized retry
error code | A code identifying a reported error condition. | group installation error codes
compliance state | A device's status against defined requirements. | report the compliance state
configuration baseline | The agreed reference configuration. | compare with the configuration baseline
configuration drift | Difference from the expected configuration over time. | detect configuration drift
exception | An approved departure from a requirement under stated conditions. | document an approved exception
remediation | Work to correct a deficiency or failure. | assign remediation ownership
deployment ring | A defined group receiving a staged rollout. | review a deployment ring
pilot group | A limited group used to test a change before expansion. | validate the pilot group
supersedence | Replacement of an earlier update by another. | check patch supersedence
dependency | A prerequisite needed for another action to succeed. | verify installation dependencies
rollback | Return to an earlier configuration or version. | confirm rollback readiness
completion criterion | A condition defining when work counts as complete. | state the completion criterion''',
    precision='Assigned, downloaded, installed, restarted, and verified are not synonyms. A successful installation report may still require a restart or verification under the approved procedure. Report the actual evidence, not the most optimistic label.',
    precision_extra='An offline device is not automatically an installation failure or an approved exception. An exception requires an authorized decision. Keep the inventory denominator stable unless an approved scope change is recorded.',
    phrases='''Report the counts | Installation succeeded on 180 of 200 managed laptops.
Separate remaining states | Twelve were offline; eight returned installation errors.
Qualify completion | Verification is not yet complete on all reported successes.
Reject an overstatement | I would report progress, not mark the deployment complete.
Preserve the denominator | The planned scope remains 200 devices unless a change is approved.
Distinguish an exception | Offline status is not an approved exception.
Ask for error evidence | Which error codes are shared across the eight failures?
Set the next action | Assign owners for the offline follow-up, errors, and verification.
Check a restart | Does the required state depend on a pending reboot?
Avoid a false category | Keep installation failure separate from devices we could not reach.
Name the criterion | What evidence must every in-scope device provide for completion?
Limit the percentage | Ninety percent installed does not mean the full rollout is verified.
Clarify a retry | A retry is scheduled; its outcome is not yet known.
Record a change | Any removal from scope needs a documented reason and approval.
Track recovery | Keep the approved rollback route available during the rollout.
Close honestly | The next update will show verified devices and each unresolved group.''',
    notes='''Of versus remaining | "180 of 200" reports success against scope; "20 remaining" identifies unresolved work.
Reported versus verified | "Reports successful installation" describes a console state; "verified" names a completed check.
Yet | "Not yet complete" preserves unfinished work without predicting when it will finish.
Separate nouns | Use offline devices and failed installations as separate categories when the evidence distinguishes them.
Unless | "The scope remains 200 unless changed by approval" states the condition for revising the denominator.
Scheduled versus completed | A scheduled retry is a plan, not evidence of a successful installation.''',
    d='''Which status statement is accurate? | 180 installed; twelve offline; eight errors; verification still in progress. | Deployment complete because 90 percent installed. | All twenty unresolved devices are approved exceptions. | All 200 devices have failed verification. | The first statement preserves each known state without inventing completion, exceptions, or verification failures.
What percentage reports successful installation? | 90 percent | 10 percent | 94 percent | 96 percent | Dividing 180 successful reports by 200 in-scope devices gives 90 percent.
Which action would distort the report? | Removing offline devices from scope without an approved change | Listing the error group separately | Recording verification as pending | Naming an owner for follow-up | Unapproved removal changes the denominator to improve appearance rather than reflect the agreed scope.
Which statement describes a plan rather than a result? | A retry is scheduled for the eight errors. | The console records 180 successes. | Twelve devices were offline. | No exception has been approved. | Scheduled identifies intended future work; it does not establish the retry outcome.''',
    dialogue='''Casey | The manager wants to know whether the laptop deployment is complete. The console shows 180 successes out of 200. Can I mark the rollout done?
Arun | Not yet. We need to distinguish [[installation::Installation is the software's reported setup state; it is not automatically the complete verified deployment state.]] from verification. Twelve devices were offline and eight returned errors, so twenty still lack successful installation reports.
Casey | I could say ninety percent complete and list the remaining devices underneath. Would that be clearer than calling the whole deployment finished for the manager?
Arun | Say ninety percent report installed. Our [[completion criterion::The completion criterion defines the evidence required for done; an installation percentage does not replace the required verification.]] also includes verification, and that check has not finished on every reported success.
Casey | What should we call the twelve offline laptops? They may simply belong to people who were away. I do not want to count them as failed installations.
Arun | Keep them in an [[offline::Offline identifies devices unavailable to the management system; it does not assert that an installation was attempted and failed.]] group. They remain in scope, but their status differs from the eight devices that actually returned installation errors.
Casey | Someone suggested excluding the offline devices from the total for now. That would make the progress figure look closer to the target while we contact their owners.
Arun | The [[denominator::The denominator is the total in-scope count; changing it without approval would make the percentage misleading.]] remains 200 unless an approved scope change says otherwise. Being inconvenient to reach is not a reason to remove a device from the report.
Casey | Understood. For the eight errors, do we have enough information to promise a successful retry today, or do we need a separate technical review first?
Arun | Review the [[error codes::Error codes identify reported conditions that may require different responses; the count alone cannot establish that a retry will succeed.]] first. A shared count can hide different causes, and a scheduled retry is not evidence that the installation will complete.
Casey | I will ask for owners and next actions for both groups. What about the successful devices that still need a restart before their new state takes effect?
Arun | Record any pending [[reboot::A reboot is a restart; if required for the approved state, installation alone is not enough to claim verification.]] separately under the approved process. We should not describe a device as verified while a required state transition remains unfinished.
Casey | If a laptop cannot be updated during this window because of a documented application dependency, can the team mark it as an exception in the report?
Arun | Only after the authorized [[exception::An exception is an approved departure with conditions, not a label the team applies simply because a device remains unresolved.]] decision. Record the reason, owner, and review condition; do not convert an unresolved error into an approved departure automatically.
Casey | That helps. The manager's update can show installed, pending verification, offline, and error states, provided we explain whether the groups overlap or form separate totals.
Arun | Exactly. Keep the [[inventory::The inventory identifies the in-scope devices and their attributes; reconciling it prevents missing devices or double-counted groups.]] reconciled so a device moving between states is not counted twice. The report should explain its counting rule.
Casey | I will not announce a restoration or completion time we have not established. Can you supply the verified count and unresolved owners for the afternoon review?
Arun | Yes. I will include the current evidence and [[remediation::Remediation is the work assigned to correct outstanding deficiencies; naming it does not claim that those deficiencies are already corrected.]] status. Where an action depends on a user or another team, I will make that dependency visible.
Casey | Then my message will say installation is progressing, twenty devices lack success reports, verification remains open, and no exception has been approved for those twenty.
Arun | That is accurate. We will close the rollout only when the agreed [[criteria::Criteria are the conditions defining acceptable completion; clear reporting follows those conditions rather than an attractive percentage.]] are met or an authorized scope decision changes them. Clear state labels let the manager decide without being misled by done.''',
    transfer_title='A server update is installed but not verified',
    transfer_setup='An approved server update reports successful installation. A required restart is pending, and the service check has not run. The maintenance owner must receive an accurate status.',
    transfer='''Engineer: "Installation is reported successful, but a ___ is still pending." | reboot | The required restart has not occurred, so the installation status cannot imply the final operational state.
Owner: "Then the service check is still part of ___." | verification | Verification checks that the required state and service behavior have actually been achieved.
Engineer: "I will describe the update as in progress, not ___." | complete | The required restart and service check remain unfinished, so complete would overstate the evidence.
Owner: "Keep the approved recovery route available until the ___ are met." | criteria | The completion conditions, not the installation message alone, determine when the work can be closed.'''))

BOOK['units'].append(unit(
    title='Security Operations, Risk, and Incident Response', scene='An unusual sign-in is not yet a confirmed compromise',
    skill='Escalate a security observation with urgency, accurate scope, and controlled evidence.',
    brief='An alert flags an unusual sign-in for a staff account at 09:12 UTC. The account owner has not confirmed whether the activity was legitimate. No data-access review has occurred. Bea detected the alert; Tomas coordinates the authorized response team. The team has a restricted evidence channel and an on-call contact. Only authorized responders decide containment actions in this fictional organization.',
    cast='Bea | Security monitoring analyst\nTomas | Incident response coordinator',
    culture=('Urgency and uncertainty can coexist', 'You can escalate promptly without labeling an unverified event a breach. State the alert, known facts, unanswered questions, and available evidence. An appropriately qualified report helps responders act; qualification is not a reason to delay notification.'),
    a='''What is confirmed? | An unusual-sign-in alert occurred at 09:12 UTC. | The account is compromised. | Customer data was stolen. | The account owner approved the activity. | The alert and its timestamp are known; legitimacy, compromise, and data impact remain unconfirmed.
Who decides containment under this case's process? | Authorized responders | Any message recipient | The alert's wording alone | The account owner without review | The briefing assigns containment decisions to authorized responders, not to every person seeing the alert.
Where should detailed evidence be placed? | The restricted evidence channel | An unrestricted social feed | A public slide deck | A general customer newsletter | The organization provides a controlled channel for evidence that may contain sensitive account information.''',
    vocabulary='''alert | A signal that a condition may require attention. | triage an alert
event | An observed occurrence in a system. | correlate security events
indicator | A piece of information that may point to relevant activity. | assess an indicator
compromise | Unauthorized access or loss of a system's trusted state. | investigate suspected compromise
breach | A security or privacy violation whose exact meaning depends on context. | avoid an unverified breach claim
false positive | An alert or finding that identifies a condition not actually present. | investigate a possible false positive
sign-in log | A record of authentication attempts or sessions. | preserve the sign-in log
session | A period or context of authenticated interaction. | review the account session
geolocation | An estimate of geographical position from available signals. | qualify a geolocation estimate
anomaly | A departure from an expected pattern. | assess a sign-in anomaly
SOC | Security operations center; a function coordinating monitoring and response. | notify the SOC
on-call | Assigned availability to respond during a defined period. | contact the on-call responder
escalation threshold | A condition requiring referral or higher attention. | apply the escalation threshold
containment | Actions intended to limit an incident's consequences. | assign containment authority
eradication | Removal of identified causes or malicious elements under a response process. | distinguish eradication from containment
recovery | Restoration of services or operations after disruption. | coordinate recovery communication
evidence preservation | Keeping relevant records intact for authorized review. | follow evidence-preservation requirements
chain of custody | A record of evidence handling and transfers. | maintain chain of custody
timeline | An ordered account of events with times. | build an incident timeline
scope assessment | Determination of affected assets, accounts, or data. | conduct a scope assessment
severity | The assessed seriousness of an incident or finding. | review incident severity
notification | Communication to designated recipients under defined rules. | confirm notification ownership
need to know | A principle restricting information to necessary recipients. | share on a need-to-know basis
post-incident review | Examination of an incident and lessons after response. | schedule a post-incident review''',
    precision='An alert is a signal to assess, not automatic proof of compromise. A location estimate is not proof of a person\'s physical location. Preserve the difference between observed evidence, an interpretation, and an authorized classification.',
    precision_extra='Containment limits consequences; eradication addresses identified causes or malicious elements; recovery restores operations. These labels describe distinct concerns, not a universal sequence that replaces local response procedures.',
    phrases='''Lead with the event | An unusual-sign-in alert was recorded at 09:12 UTC.
State the unknown | The account owner has not yet confirmed the activity.
Escalate promptly | I am referring this through the approved response channel now.
Avoid a premature label | We have not established compromise or data exposure.
Protect the record | The complete evidence is in the restricted channel.
Name the authority | The authorized responder will decide containment actions.
Preserve timing | Keep the original timestamp and its time zone in the timeline.
Set the next update | The next update will distinguish confirmed findings from open questions.
Qualify location | The alert reports a location estimate, not verified physical travel.
Check scope | Which accounts and assets have actually been reviewed?
Limit distribution | Share account details only with the designated recipients.
Avoid reassurance without evidence | An unconfirmed alert is not the same as a cleared alert.
Record a handoff | Please confirm who has accepted response ownership.
Separate decisions | Technical response and external notification have different owners.
Preserve evidence | Follow the approved handling process before altering relevant records.
Close accurately | The finding remains under review; no final classification has been made.''',
    notes='''Suspected versus confirmed | These modifiers mark different evidence states and must survive shortened updates.
Has not yet | This describes an unfinished confirmation, not proof that the activity was unauthorized.
Who owns | Ask for a named responsibility rather than assuming that everyone on a message is acting.
According to | "According to the alert" attributes a reported signal without treating it as verified reality.
Scope of no | "No review has occurred" describes missing investigation, not absence of data access.
Urgent but qualified | A direct escalation can include "unconfirmed" without weakening the instruction to review promptly.''',
    d='''Which initial report is accurate? | Unusual-sign-in alert at 09:12 UTC; owner confirmation and scope review pending. | Confirmed account takeover with stolen customer data. | False positive because nobody has confirmed it. | Incident closed because an alert is not proof. | The accurate report supplies the known event and missing checks without prematurely confirming or dismissing the issue.
What does "owner confirmation pending" establish? | Confirmation has not been completed. | The owner denies the activity. | The owner approves the activity. | The account was definitely stolen. | Pending identifies an unfinished check and does not supply either possible outcome.
Which question clarifies response ownership? | Who has accepted the containment decision under the approved process? | Who first heard a rumor about the account? | Who prefers the term breach? | Who can forward the screenshot most widely? | The first question identifies the authorized decision owner rather than amplifying or relabeling the report.
Which statement overclaims scope? | Every account is affected because one alert fired. | One account generated the recorded alert. | The data-access review has not occurred. | A restricted evidence channel is available. | A single account alert cannot establish that every account is affected without further investigation.''',
    dialogue='''Bea | An unusual-sign-in alert fired for a staff account at 09:12 UTC. I have the event record, but the account owner has not confirmed the activity yet.
Tomas | Please escalate through the approved route and place the full record in the [[restricted channel::The restricted channel keeps detailed account evidence available to authorized responders without broadly distributing it.]]. We need prompt review without sending account details to everyone in the project chat.
Bea | Should the subject say confirmed compromise so the on-call responder treats it urgently? I do not want a qualified title to make this seem unimportant.
Tomas | Use suspected activity and the confirmed [[alert::An alert is a signal requiring assessment; it does not alone establish unauthorized access or compromise.]] details. Urgency does not require an unsupported conclusion. The escalation route communicates the need for attention.
Bea | The alert includes a location estimate that differs from the user's usual pattern. I have not checked whether travel or another legitimate explanation could account for it.
Tomas | Keep that [[geolocation::Geolocation is an estimate based on available signals; it is not verified evidence of the person's physical location.]] limitation explicit. Do not report physical travel as fact, and do not dismiss the event merely because a benign explanation is possible.
Bea | I also have not reviewed subsequent data access. I will leave impact unknown rather than saying no data was accessed just because that field is empty.
Tomas | Correct. Missing review is not a negative finding. The responder needs a [[scope assessment::A scope assessment determines what accounts, assets, or data are affected; an unreviewed area cannot be declared unaffected.]] before making claims about affected data or other accounts.
Bea | Who decides whether any containment action is needed? I can preserve the alert, but I am not authorized to make changes to the account in this process.
Tomas | The authorized response team owns [[containment::Containment limits possible consequences and is an operational decision for the role authorized in this case.]]. I will confirm the named responder has accepted the handoff rather than assume that receiving a message means someone is acting.
Bea | I will preserve the original record and use a redacted summary for the wider operational update. The timestamp will remain 09:12 UTC in both places.
Tomas | Good. Consistent timing supports the [[timeline::A timeline orders events using comparable timestamps; inconsistent time zones can lead reviewers to associate the wrong records.]]. Follow the evidence-handling process so the original information remains available and its history is clear.
Bea | If the owner later says the activity was theirs, can I close the alert immediately, or does the response team need to review that confirmation first?
Tomas | Follow the assigned review route. Confirmation is evidence, but the authorized reviewer decides the [[classification::Classification records the assessed type or status of the event; one new statement should be handled through the approved review rather than automatic closure.]] using the whole record and the organization's criteria.
Bea | Understood. The business lead is already asking whether we must notify customers. I do not have enough information to answer that, and no data review is complete.
Tomas | Refer [[notification::Notification decisions concern designated recipients and applicable obligations; they have authorized owners separate from the initial alert reporter.]] decisions to the designated owner. Do not invent a legal threshold, promise no notification, or make a public statement from this initial signal.
Bea | The next update will list the event, accepted response owner, checks in progress, and what remains unknown. I will avoid pasting the full account record into it.
Tomas | Exactly. Use a [[need-to-know::Need-to-know limits detailed information to people who require it for their role, while allowing a suitable broader status summary.]] summary for the audience. Clear communication does not mean every recipient receives every piece of evidence.
Bea | I will send the restricted report now and confirm the on-call handoff. I will not describe the absence of a final conclusion as either proof of safety or proof of compromise.
Tomas | That is the right distinction. Keep the finding [[under review::Under review accurately marks an unresolved assessment; it neither clears the alert nor confirms a breach before the evidence supports either result.]] until the authorized decision is recorded, and preserve the evidence and uncertainty in every shortened update.''',
    transfer_title='A suspicious email is reported but not analyzed',
    transfer_setup='An employee reports a suspicious email. The attachment has not been analyzed, and no interaction has been confirmed. The approved reporting route accepts the original message for authorized review.',
    transfer='''Analyst: "The email is reported suspicious; malicious content is not yet ___." | confirmed | A report identifies a concern, but analysis has not established what the attachment contains.
Coordinator: "Use the approved reporting ___ for the original message." | route | The defined route sends the evidence to authorized reviewers instead of encouraging informal redistribution.
Analyst: "Whether anyone interacted with it remains ___." | unknown | No interaction has been confirmed, which is not evidence that interaction either did or did not occur.
Coordinator: "Keep the wider update limited to the audience's need to ___." | know | The need-to-know principle restricts unnecessary distribution of potentially sensitive incident information.'''))

BOOK['units'].append(unit(
    title='Change, Release, Problem, and Post-Incident Communication', scene='Correct the maintenance date before users act on it',
    skill='Replace an inaccurate notice, acknowledge impact, and confirm the controlling record.',
    brief='A maintenance notice sent to users says Tuesday from 8 to 9 p.m. The approved change record says Thursday from 8 to 9 p.m., local branch time. The work has not begun. One team moved its export schedule in response to the incorrect notice. Mina sent the notice; Owen owns change coordination. A correction must reach the original recipients and clearly replace the earlier message.',
    cast='Mina | Service communications analyst\nOwen | Change coordinator',
    culture=('A correction needs an explicit replacement', 'Sending another message without identifying the error can leave two apparent sources of truth. Acknowledge the mistake, state the approved details, say which message is replaced, and address consequences already caused. Avoid implying that the authorized schedule changed when only the notice was wrong.'),
    a='''Which window is approved? | Thursday, 8 to 9 p.m., local branch time | Tuesday, 8 to 9 p.m. | Thursday, all day | Tuesday, 8 to 9 a.m. | The approved change record specifies Thursday evening in local branch time.
What actually changed? | The notice contained an error; the approved window did not change. | The work moved from an approved Tuesday window. | The maintenance already happened. | All user exports were canceled. | The case distinguishes a mistaken communication from a change to the authorized schedule.
Which consequence is known? | One team moved its export schedule. | Every team lost data. | The server failed on Tuesday. | Nobody acted on the notice. | The briefing identifies one concrete downstream scheduling consequence without establishing wider damage.''',
    vocabulary='''change record | The controlled record describing an authorized change. | consult the approved change record
change owner | The role responsible for a proposed or approved change. | identify the change owner
change approval | Permission to carry out a specified change. | verify change approval
maintenance notice | A communication of planned service work and impact. | correct a maintenance notice
maintenance window | The authorized time period for planned work. | confirm the maintenance window
release | A version or package made available under a process. | coordinate a software release
deployment | Introduction of a release or configuration into an environment. | distinguish release from deployment
rollback plan | An approved route for returning to an earlier state. | review the rollback plan
implementation plan | The defined plan for carrying out a change. | confirm the implementation plan
validation | Checks that a change meets its intended requirements. | record post-change validation
stakeholder | A person or group with an interest in the outcome. | identify affected stakeholders
recipient list | The designated audience for a message. | reconcile the recipient list
correction | A statement replacing inaccurate information. | issue an explicit correction
supersede | Replace an earlier record or statement as controlling. | supersede the earlier notice
source of truth | The agreed authoritative record for a particular fact. | name the source of truth
acknowledgment | Confirmation of receipt or understanding. | request acknowledgment
dependency | Work or a condition another action relies on. | identify a scheduling dependency
change freeze | A defined restriction on changes during a period. | check the change-freeze policy
emergency change | A change handled under an authorized urgent process. | follow the emergency-change route
problem record | A record tracking an underlying cause or recurring issue. | open a problem record
known error | A recognized problem with documented diagnostic context or handling. | document a known error
post-implementation review | Review of a change's outcome after implementation. | conduct a post-implementation review
action owner | The person accountable for an agreed follow-up. | name the action owner
due date | The agreed date by which an action is expected. | confirm the action due date''',
    precision='A mistaken notice is not automatically a changed authorization. "The date has moved" would imply an actual schedule change; "the Tuesday date was incorrect" identifies the communication error. Preserve the exact time zone.',
    precision_extra='Acknowledgment confirms receipt or understanding; it does not approve the change. A corrected notice supersedes the inaccurate communication, while the approved change record remains the authority for the work.',
    phrases='''Own the error | The Tuesday date in my earlier notice was incorrect.
State the approved fact | The approved window is Thursday, 8 to 9 p.m., local branch time.
Replace the old record | This correction supersedes the earlier maintenance notice.
Avoid a false history | The approved window has not changed; the notice was wrong.
Acknowledge impact | I understand your team rescheduled an export based on that message.
Request confirmation | Please confirm that the corrected date has reached the affected team.
Name the authority | The approved change record remains the source of truth.
Close with an owner | I will send the correction and contact the team that already changed its schedule.
Check the audience | Use the original recipient list and any known forwarded recipients.
Preserve the zone | Include local branch time in the subject and body where appropriate.
Distinguish receipt | Acknowledging this correction does not provide change approval.
Check dependencies | Which other scheduled work depended on the incorrect date?
Avoid an assumption | We should not assume a second email has been read.
Record the consequence | Note the export rescheduling as a known impact of the error.
Separate follow-up | Review how the mismatch occurred after the immediate correction is sent.
Make action testable | Assign an owner to verify the notice against the approved record before sending.''',
    notes='''Was incorrect versus changed | The first corrects a statement; the second describes a change in the underlying fact.
Supersedes | This verb states which communication takes precedence when two versions circulate.
Apology with action | "I am sorry for the confusion; here is the corrected window" pairs accountability with useful information.
Local time | Name the relevant location or time zone rather than assuming every recipient reads the same clock.
Please confirm that | This requests confirmation of a specific fact, not a vague reply such as "looks good."
Passive alternatives | "An error was made" hides the responsible action; "I sent the wrong date" is clearer when that responsibility is known.''',
    d='''Which subject line matches the facts? | Correction: Thursday maintenance window; Tuesday date was incorrect | Maintenance moved from approved Tuesday to Thursday | Tuesday maintenance successfully completed | All future maintenance canceled | The first corrects the message without inventing a change to the approved schedule or completed work.
Which sentence identifies the controlling communication? | This correction supersedes the earlier notice. | Here is another note for your information. | Both dates may remain useful. | Please choose whichever message suits your team. | Supersedes explicitly replaces the inaccurate notice and reduces competing interpretations.
What does receipt acknowledgment establish? | That the recipient received or understood the correction | That maintenance has been approved anew | That every forwarded recipient has read it | That the export has already been restored to its old schedule | Receipt or understanding is narrower than approval or completion of downstream actions.
Which follow-up is concrete and accountable? | Name an owner to verify future notices against the approved record. | Ask everyone to be more careful indefinitely. | Assume the error cannot happen twice. | Delete all evidence of the first message. | A named verification action can be performed and checked; vague intentions and deleted history do not create that control.''',
    dialogue='''Mina | I found an error in yesterday's maintenance notice. I wrote Tuesday from eight to nine, but the approved record says Thursday during that same hour.
Owen | We need an explicit [[correction::A correction replaces inaccurate information; another unexplained message could leave both dates appearing valid.]] before more teams act on it. Has any work started, or is this still only a communication mismatch?
Mina | The maintenance has not begun. One team moved its invoice export because of my notice, so there is already a scheduling consequence even without a service interruption.
Owen | Include that known [[impact::Impact includes the team's changed work schedule; the absence of an outage does not mean the mistaken notice had no consequences.]]. We should correct the date and contact that team directly rather than assume the general email will resolve everything.
Mina | Should I title the message maintenance moved to Thursday? That sounds concise, but it could imply Tuesday was once the authorized schedule, which it was not.
Owen | Exactly. Say the Tuesday date was incorrect and state the approved [[maintenance window::The maintenance window is the authorized work period, which remains Thursday from eight to nine in this case.]]. The authorization did not change; our message failed to match it.
Mina | I will include Thursday, eight to nine p.m., local branch time. I also need to say that the new message replaces the earlier notice in case both circulate.
Owen | Use [[supersedes::Supersedes states that the corrected communication replaces the earlier one as the version recipients should use.]]. That makes the relationship explicit. Put the correct date prominently so recipients do not have to compare paragraphs to find it.
Mina | I have the original mailing list. Some managers may have forwarded the message, so the first list may not include everyone who now has the wrong date.
Owen | Reconcile the [[recipient list::The recipient list identifies the message audience; known forwarding may require further communication beyond the original addressees.]] and ask managers to pass on the correction where needed. Do not claim that sending one email proves everyone received the right information.
Mina | For the team that moved the export, I will apologize and ask whether the corrected window conflicts with their revised schedule. I cannot change that schedule on their behalf.
Owen | Good. Identify the [[dependency::A dependency is scheduled work affected by another condition; the export plan may now depend on confirmation of the maintenance timing.]] and let its owner confirm the adjustment. Acknowledge the disruption without promising an action you do not own.
Mina | Do we need fresh change approval because I am issuing a corrected notice, or does the existing approved record remain valid for Thursday's work?
Owen | The approved record remains the [[source of truth::The source of truth is the agreed authoritative record; the communication correction does not itself alter or renew the underlying approval.]] for this case. We are correcting its communication, not requesting a different window or scope.
Mina | I will ask the affected team to confirm receipt of the correction. I want to avoid describing their acknowledgment as approval for the maintenance itself.
Owen | Precisely. [[Acknowledgment::Acknowledgment confirms receipt or understanding, not permission to carry out the change or proof that every resulting action is finished.]] and authorization are different. The team's reply can confirm that they know the right time and identify remaining scheduling conflicts.
Mina | After the urgent correction, we should review how the wrong date entered the notice. I copied an earlier planning note instead of checking the approved record.
Owen | Record a concrete follow-up with an [[action owner::An action owner is accountable for completing the agreed improvement, making follow-up more specific than a general request to be careful.]]: verify the date, scope, and time zone against the approved record before each notice is sent.
Mina | I will send the correction now, contact the export team, and report any unresolved recipient or schedule issue before the end of the afternoon.
Owen | Thank you. Keep the correction and its [[audit trail::The audit trail preserves what was sent, corrected, and confirmed, allowing later review without hiding the original communication error.]]. Clear replacement, accurate timing, and accountable follow-up matter more than making the original mistake disappear.''',
    transfer_title='A release notice lists the wrong version',
    transfer_setup='A notice says version 4.2 will be deployed. The approved record specifies version 4.1. Deployment has not begun, and the approved version has not changed.',
    transfer='''Communicator: "The 4.2 reference was ___; the approved version is 4.1." | incorrect | The error is in the notice; the approved version remains 4.1.
Coordinator: "State that the correction ___ the earlier notice." | supersedes | Supersedes tells readers which communication replaces the inaccurate version.
Communicator: "The approved record remains the source of ___." | truth | The controlled record, not either informal assumption, governs the authorized version.
Coordinator: "Ask recipients to acknowledge the correction, not to provide new ___." | approval | Receipt of a corrected notice is distinct from authorizing a different deployment.'''))

BOOK['units'].append(unit(
    title='Platform, DevOps, Observability, and Kubernetes Conversations', scene='Normal CPU does not prove checkout is healthy',
    skill='Challenge a narrow health claim and coordinate investigation around user-visible evidence.',
    brief='The checkout service\'s dashboard shows normal server CPU usage. Five users report slow checkout during the last half hour. Request-duration and database-wait data have not yet been reviewed. Pat owns the application; Suri coordinates the platform team. The service runs in Kubernetes. There is no confirmed cause or approved production change. Both teams can review approved telemetry and agree on the next investigation owner.',
    cast='Pat | Application engineer\nSuri | Platform engineer',
    culture=('A healthy component is not a healthy journey', 'A dashboard can be correct and incomplete. Normal CPU describes one resource measure, not the entire user transaction. Invite application and platform evidence together instead of using a green panel to dismiss user reports or assign blame.'),
    a='''Which metric has been reviewed? | Server CPU usage | Database wait time | End-to-end checkout duration | Every user's network path | The briefing confirms only the CPU panel; the other evidence has not been reviewed.
What do the five reports establish? | Five users experienced slow checkout in the reported period. | Kubernetes is definitely at fault. | The database has failed. | Every customer is unable to buy. | The reports establish a user-visible symptom, not a cause or the total affected population.
What is authorized now? | Review approved telemetry and coordinate investigation ownership | Make any production change without review | Declare the incident resolved from CPU alone | Ignore the reports until every user complains | The case authorizes evidence review and coordination, not unapproved changes or unsupported resolution.''',
    vocabulary='''platform | Shared technical services supporting applications. | coordinate with the platform team
DevOps | Collaborative practices linking software delivery and operations. | clarify DevOps responsibilities
Kubernetes | A platform for managing containerized workloads and services. | inspect Kubernetes workload status
cluster | A group of machines or resources managed together. | review cluster-level signals
node | A machine participating in a Kubernetes cluster. | inspect node resource usage
pod | A Kubernetes unit containing one or more containers. | check pod readiness
container | An isolated execution environment packaged with application dependencies. | inspect container logs
deployment | A Kubernetes resource managing a desired set of replicated pods. | review the deployment status
service | In Kubernetes, an abstraction exposing a group of endpoints. | inspect the service endpoints
ingress | A resource defining external HTTP or HTTPS routing to services. | review ingress routing
readiness | Whether an instance is ready to receive service traffic. | check readiness status
liveness | Whether a running instance should be considered alive under its check. | distinguish liveness from readiness
replica | A copy of an application instance maintained for a workload. | compare replica behavior
resource request | A declared resource amount used in scheduling decisions. | review resource requests
resource limit | A configured ceiling governing resource use. | inspect resource limits
CPU | Central processing unit; processing capacity measured by the panel. | inspect CPU utilization
observability | Ability to understand system behavior from emitted signals. | improve service observability
metric | A numerical measurement collected over time. | correlate service metrics
log | A recorded event or message from a system. | review application logs
trace | A connected record of a request across components. | follow a distributed trace
span | A timed operation within a distributed trace. | identify a slow span
saturation | The extent to which a resource's capacity is consumed. | investigate resource saturation
database wait | Time spent awaiting a database resource or response. | measure database wait time
user journey | The sequence of actions producing a user-visible outcome. | monitor the checkout user journey''',
    precision='A Kubernetes readiness check reports a configured condition, not universal correctness of every user transaction. CPU utilization is one metric; waiting on another component can produce slow responses without high CPU on the observed server.',
    precision_extra='In Kubernetes, Deployment and Service have specific resource meanings; in general IT discussion the same words have broader uses. Name the resource or user-facing function to avoid talking past another team.',
    phrases='''Validate both observations | The CPU panel is normal, and users are reporting slow checkout.
Challenge the inference | That metric alone does not establish service health.
Ask about the journey | Which part of checkout is slow from the user's perspective?
Request timing | Can we compare request durations during the reported half hour?
Avoid blame | We have not isolated the application or platform as the cause.
Follow the request | Trace the transaction across the components rather than stopping at one panel.
Name missing signals | Database wait and complete request duration remain unchecked.
Assign the next review | Application will review request traces; platform will check the corresponding resource signals.
Clarify a resource | By service, do you mean the user-facing checkout or the Kubernetes Service?
Limit a health check | Readiness passes for its configured test; that is not a full checkout result.
Check the time range | Are both dashboards showing the same interval and time zone?
Separate mitigation | A proposed restart is not yet a diagnosed remedy.
Preserve authorization | Any production change still needs the approved route.
Report measured impact | We have five reports; the full affected population is not yet known.
Coordinate ownership | Who will combine the two teams' findings into the next update?
Close precisely | We will keep the issue open until user-visible behavior is assessed.''',
    notes='''And instead of but | "CPU is normal and checkout is slow" allows two compatible observations without dismissing either.
Does not establish | This challenges the strength of an inference without claiming that the metric itself is wrong.
By service | A clarification question identifies whether a word has a platform-specific or business meaning.
During | Tie evidence to the reported period rather than comparing unrelated dashboard windows.
Not yet | This preserves pending diagnosis and avoids treating an untested remedy as confirmed.
Who will | Assign one accountable coordinator rather than leaving ownership implicit across teams.''',
    d='''Which statement combines the evidence accurately? | CPU is normal on the observed panel; checkout slowness still requires investigation. | CPU is normal, so every user report is false. | Kubernetes caused the slowdown because the service uses it. | The database is confirmed to be the bottleneck. | A normal resource measure can coexist with slow transactions; the cause remains unconfirmed.
Which question resolves ambiguous terminology? | By service, do you mean checkout or the Kubernetes Service resource? | Which team usually wins technical disagreements? | Can we rename every component before reviewing it? | Is a green panel always correct about customers? | The first question separates a user-facing function from a specific platform resource with the same label.
What could a distributed trace help identify? | Which recorded operation contributes to the request delay | Whether every customer is satisfied | Who should be blamed without review | Whether all future requests will be fast | A trace records operations and timing for a request, supporting diagnosis rather than universal or personal conclusions.
Which next step fits the stated authority? | Review approved telemetry and coordinate findings before proposing a production change. | Restart every component immediately without approval. | Close the issue because readiness passes. | Promise a fixed completion time without measurements. | The case permits investigation and coordination, while changes and outcome promises need further evidence and approval.''',
    dialogue='''Pat | Five users reported slow checkout in the last half hour. The platform dashboard shows normal CPU, so one colleague says the service must be healthy.
Suri | The panel can be correct without supporting that conclusion. CPU is one [[metric::A metric measures a specified property; normal CPU does not establish the performance of the complete checkout transaction.]], and we need evidence about the user-visible transaction rather than dismissing the reports.
Pat | I agree. I have not reviewed the request durations yet. The reports say checkout feels slow, but they do not identify whether payment or order confirmation is taking longer.
Suri | Start by clarifying the [[user journey::The user journey names the sequence producing the customer's outcome; a symptom should be located within that sequence.]]. We can then compare request timing during the reported period with the corresponding platform signals.
Pat | When you say the service is ready, do you mean checkout has been tested or that the Kubernetes readiness checks are passing for its pods?
Suri | I mean the configured [[readiness::Readiness reports whether an instance meets its configured traffic-acceptance check; it is not a complete test of every checkout behavior.]] checks pass. That is useful evidence about those checks, not proof that every checkout completes promptly.
Pat | Thanks for separating that. I can review the application trace for a reported transaction if we can match it to a request identifier and time.
Suri | A distributed [[trace::A trace connects recorded operations across components for a request, helping locate where time is spent.]] should help us follow the path. Please preserve the exact interval and time zone so our teams compare the same events.
Pat | If the slow operation is a database call, would normal application CPU be consistent with that? People seem to expect every slowdown to make CPU high.
Suri | It could be consistent with waiting, but we have not checked [[database wait::Database wait is time awaiting database work or resources; it is a plausible source of delay, not yet a finding here.]] yet. Describe that as a hypothesis until the timing evidence actually supports it.
Pat | I will not label the database the bottleneck in the update. I can identify the slowest recorded operation and report what the trace includes and omits.
Suri | Good. Inspect the relevant [[span::A span records a timed operation within the trace; it can show a contribution to delay without proving every unrecorded cause.]], and avoid assuming that an uninstrumented interval contains no work. Missing telemetry is a limitation, not a zero-duration finding.
Pat | Should we restart the pods while the investigation continues? A colleague suggested it because that helped with a different issue last month, but this cause is unknown.
Suri | A restart would be a production [[change::A production change requires the approved decision route; success on a previous unrelated issue does not authorize or establish this remedy.]]. It needs the approved route and a reasoned proposal. We should not turn the previous incident's remedy into this incident's diagnosis.
Pat | Understood. Which platform evidence can your team review while I check the request path? We should avoid assigning both teams the same vague task of checking everything.
Suri | We will examine corresponding resource use, workload status, and relevant [[saturation::Saturation concerns resource capacity being consumed; examining it complements request-path evidence without assuming CPU alone covers every resource.]] signals under our approved access. You can focus on application timing and the exact checkout steps.
Pat | Who will combine the findings for the next update? Separate team messages might sound contradictory if one says resources are normal and another says customers are waiting.
Suri | I will coordinate the [[handoff::A handoff combines the evidence and next responsibility so separate observations are not mistaken for conflicting conclusions.]]. We can report both observations, explain their scope, and identify the next owner without declaring either team at fault.
Pat | Then the issue stays open. We have five reports, not a verified total of affected users, and no confirmed cause or approved remedy at this point.
Suri | Exactly. Better [[observability::Observability is the ability to understand system behavior from its signals; useful interpretation connects those signals to user-visible outcomes.]] means connecting the signals to the user outcome. We will report what the evidence establishes and what still needs investigation, even when the dashboard remains green.''',
    transfer_title='Readiness passes while a search request times out',
    transfer_setup="A search application's readiness check passes, but an authorized test request times out. The check only tests a lightweight endpoint. The search backend has not yet been reviewed.",
    transfer='''Engineer: "The readiness ___ passes for the lightweight endpoint." | check | The passing result belongs to the configured endpoint check, not the full search transaction.
Reviewer: "That does not establish the complete search ___ is healthy." | journey | The complete user journey includes work beyond the lightweight readiness endpoint.
Engineer: "I will inspect the request ___ to locate the recorded delay." | trace | A request trace can connect operations and timings along the path of the failing search.
Reviewer: "Keep the backend explanation as a ___ until the evidence supports it." | hypothesis | The backend has not been reviewed, so its involvement remains a proposed explanation.'''))
