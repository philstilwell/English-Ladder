"""Original telecommunications cases for the English Ladder learner book."""
from books.authoring import unit

BOOK = dict(
    slug='telecommunications', title='Telecommunications English',
    cover_label='ENGLISH FOR NETWORK AND SERVICE TEAMS',
    cover_title='Telecommunications', cover_size=30,
    tagline='Keep the service picture clear.\nTurn technical uncertainty into useful updates.',
    audience='For network operations, deployment, provisioning, field service, customer care, and vendor-management professionals.',
    map_intro='Eight service conversations: coordinate an outage bridge, qualify a fiber handover, investigate busy-hour Wi-Fi, clarify an activation request, prepare a useful dispatch, review an emergency-calling notice, handle repeated interruptions, and compare equipment support horizons.',
    notes_title='Name the service, the evidence, and the next step',
    notes_intro='Telecommunications teams work across technical, commercial, and customer-facing boundaries. Precise English keeps a reported symptom from becoming an assumed cause, a target from becoming a promise, and a completed task from becoming an approved service.',
    field_notes=[
        ('Separate service impact from root cause', 'A team can confirm that a service is interrupted before it knows which component caused the interruption. Report each with its own confidence level.', '"We have confirmed the affected area; fault isolation is still in progress."'),
        ('Use identifiers before shorthand', 'An address may contain several circuits, accounts, or services. Confirm the relevant reference and read it back before arranging changes.', '"Which circuit at that address is included in the activation request?"'),
        ('Distinguish readiness from completion', 'Installation, inspection, acceptance, provisioning, and activation are different milestones. Name the milestone that the evidence actually supports.', '"The installation is complete; acceptance remains pending."'),
        ('Make the update commitment useful', 'Give a named owner, a time zone, and the purpose of the next update. Do not turn an update time into a restoration estimate.', '"I will update you at 14:00 Eastern, even if the restoration estimate is still unavailable."'),
    ],
    scope_note='All operators, customers, circuits, incidents, dates, prices, contracts, and local procedures are fictional. This book teaches professional English, not network configuration, field-safety procedures, legal compliance, or emergency-call handling. Use approved operating procedures and qualified personnel. Regulatory examples identify their jurisdiction and are not complete compliance instructions.',
    sources=[
        dict(title='Electronic Code of Federal Regulations. 47 CFR 9.11: E911 service.', url='https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-9/subpart-D/section-9.11', note='Current U.S. interconnected-VoIP emergency-calling requirements inform the notice-review case. Applicability, location obligations, and customer notifications require service-specific review.', checked='1 October 2026'),
        dict(title='Cisco. Wireless Network Solution Guide.', url='https://www.cisco.com/c/en/us/products/collateral/wireless/unified-wireless-network-sg.html', note='Background on wireless local-area networks, coverage, capacity, and performance. The book uses fictional Wi-Fi measurements, not current product specifications.', checked='1 October 2026'),
        dict(title='The Fiber Optic Association. Fiber Optic Cable Plant Installation.', url='https://www.thefoa.org/tech/ref/OSP/install.html', note='Background on installation documentation and testing terminology. The dialogue does not replace technical acceptance specifications or field-safety requirements.', checked='1 October 2026'),
        dict(title='Cisco. End-of-Life Policy.', url='https://www.cisco.com/c/en/us/products/eos-eol-policy.html', note='Background on distinct sales and support milestones. Fictional vendor dates illustrate comparison language; actual support depends on the applicable product notice and terms.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Network Operations and Outage Bridges',
    scene='The next update is not a restoration promise',
    skill='Give a concise incident update that separates verified impact, investigation, and a timed communication commitment.',
    brief='At 09:10, incident O73 interrupts 120 broadband services in the East service area. The number is a count of services, not individual people. Network alarms confirm the interruption, but the cause has not been isolated. No estimated time of restoration has been verified. Network operations lead Arun and customer communications lead Tess join an outage bridge. Their next public update is due at 09:40 Eastern. They need a consistent message without inventing a restoration time or blaming a recent change before evidence connects it to the incident.',
    cast='Arun | Network operations lead\nTess | Customer communications lead',
    culture=('Urgency needs a shared status vocabulary', 'On a busy bridge, short statements help only when everyone understands their status. Use confirmed, investigating, and not yet verified consistently. A direct challenge to an unsupported estimate protects the team from repeating a promise it cannot substantiate.'),
    a='''What is the verified impact? | 120 broadband services in the East area | 120 individual people nationwide | Every service in all areas | One confirmed faulty router | The record counts interrupted broadband services in one specified area, not people or equipment.
What does 09:40 Eastern represent? | The next public update | A verified restoration time | The incident start | The end of customer impact | The team has committed to an update at that time, not to restoration.
What remains unconfirmed? | The root cause and restoration estimate | The incident identifier | The affected service count | The 09:10 start time | Fault isolation is ongoing and no restoration estimate has been verified.''',
    vocabulary='''NOC | Network operations center; the team or facility monitoring network service. | notify the NOC
outage bridge | A coordinated call used to manage an interruption. | join the outage bridge
incident commander | The person coordinating the incident response. | identify the incident commander
service impact | The effect of an incident on a defined service. | confirm service impact
blast radius | Informal term for the extent of an incident's effects. | assess the blast radius
fault isolation | Investigation to locate the source of a fault. | continue fault isolation
alarm correlation | Analysis of related alerts to find a common pattern. | perform alarm correlation
root cause | The underlying cause established through investigation. | verify the root cause
ETR | Estimated time of restoration; a forecast, not automatically a guarantee. | validate the ETR
restoration | Return of the affected service to its required operating state. | confirm service restoration
degradation | Reduced performance without necessarily losing the entire service. | report service degradation
packet loss | Failure of some transmitted data packets to reach their destination. | measure packet loss
latency | Time taken for data to travel through a specified path. | measure latency
jitter | Variation in packet delay over time. | monitor jitter
failover | Transfer to an alternative component or path after a problem. | assess failover status
redundancy | Additional capacity or components intended to improve resilience. | verify redundancy
workaround | A temporary way to reduce impact without resolving the underlying cause. | evaluate a workaround
change freeze | A restriction on changes during a defined period. | observe the change freeze
rollback | Return to a prior configuration or release under an approved process. | request a rollback
escalation path | The defined route for involving additional authority or expertise. | follow the escalation path
status cadence | The agreed frequency of updates. | establish a status cadence
incident timeline | A chronological record of relevant incident events. | maintain the incident timeline
monitoring window | A defined period for observing service behavior. | complete the monitoring window
post-incident review | A structured review of the response and underlying learning. | schedule a post-incident review''',
    precision='An affected-service count is not automatically a count of customers, households, or people. Retain the measurement unit in every update. A shared incident identifier helps different teams discuss the same event without merging unrelated reports.',
    precision_extra='An ETR is an estimate supported by the available evidence. An update time is a communication commitment. If no estimate is verified, state that clearly and still specify when the next information will be provided.',
    phrases='''Open the update | Here is the confirmed service impact.
Bound the area | The interruption is limited to the East service area in our current evidence.
Retain the unit | We have identified 120 affected broadband services.
Separate cause from impact | The interruption is confirmed; the cause is still under investigation.
Reject speculation | The recent change is a lead, not a confirmed cause.
Qualify the estimate | We do not yet have a verified restoration estimate.
Name the next contact | The next public update is at 09:40 Eastern.
Prevent confusion | That is an update time, not a restoration commitment.
Ask for a source | Which monitoring result supports that statement?
Check a workaround | Has the proposed workaround been approved and validated?
Keep the bridge focused | Let us separate current impact from the investigation hypotheses.
Assign an owner | Arun will confirm the technical status before the message goes out.
Record a milestone | Please add that event and its time to the incident timeline.
Avoid premature closure | We need the agreed monitoring evidence before closing the incident.
Keep the message aligned | Customer care and the status page should use the same verified facts.
Close the handover | I will circulate the impact, open questions, owner, and next update time.''',
    notes='''Current evidence | Limits a statement to what has actually been established.
A lead, not | Distinguishes a useful hypothesis from a verified explanation.
Do not yet | Communicates an information gap without implying that no work is happening.
At ... Eastern | Makes the communication time unambiguous across locations.
Before closing | Names a required dependency instead of assuming the incident is resolved.
Same verified facts | Aligns messages without forcing every channel to use identical wording.''',
    d='''Which public line is accurate? | We are investigating an interruption affecting 120 broadband services in the East area. | All East residents have lost every service. | A recent change definitely caused the outage. | Service will be restored at 09:40. | The accurate line preserves the verified service count, area, and investigation status.
A colleague says the recent change caused O73. What is the best response? | What evidence links that change to this incident? | Shall we publish the blame immediately? | Can we omit the incident identifier? | Does a recent change always cause the next outage? | Asking for a specific evidence link tests the claim without dismissing a potentially useful lead.
Which sentence correctly uses ETR? | No ETR has been verified; the next update is at 09:40 Eastern. | The ETR is simply the time we promised to post. | ETR means the incident has ended. | The public-update deadline guarantees restoration. | The sentence explicitly separates a restoration forecast from the communication schedule.
What should the handover preserve? | Impact, open questions, owner, and next update time | Only the most optimistic guess | An unverified component name as root cause | A count of people inferred from services | These items let the next team continue work without losing status or inventing certainty.''',
    dialogue='''Tess | Customer care needs a short statement for O73. People are asking whether the whole network is down and when it will come back.
Arun | Start with the [[service impact::Service impact names the verified effect on broadband service without treating the cause or restoration time as established.]]: 120 broadband services in the East area have been interrupted since 09:10. We have not confirmed an impact outside that area.
Tess | Can I describe that as 120 customers? It sounds more natural in a public notice than a count of services.
Arun | Keep the [[affected-service count::Affected-service count preserves the measured unit; one customer may have several services and a service may serve several people.]]. It does not tell us the number of individual people or accounts. We should not convert the figure without a reliable mapping.
Tess | Someone on the call mentioned a change made earlier this morning. Is that the explanation we should give?
Arun | No. [[Fault isolation::Fault isolation is the ongoing process of locating the fault; a recent change remains a hypothesis until evidence connects it.]] is still in progress. The change is one lead, but timing alone does not establish that it caused the interruption.
Tess | Understood. The status page has a field for the expected restoration time. Should I enter our next update time there?
Arun | Leave the [[ETR::ETR means estimated time of restoration; the team has no verified forecast and must not substitute a communication deadline.]] as unavailable under the page's approved format. Our 09:40 Eastern commitment is to publish an update, not to restore the service.
Tess | I want customers to see that we are actively working on this, even if we cannot give them a finish time.
Arun | We can say the network team is investigating. Set the [[status cadence::Status cadence is the agreed update frequency, giving customers a useful communication expectation without inventing technical progress.]] clearly and provide the next time. That is a concrete commitment we can keep while the technical position develops.
Tess | The bridge is getting crowded. One person is discussing a workaround, while another is repeating the customer reports.
Arun | I will ask the [[incident commander::Incident commander identifies the person coordinating response priorities and keeping the bridge's decisions, owners, and updates aligned.]] to separate those workstreams. A proposed workaround should not enter the customer message as available before it is approved and validated.
Tess | Who will confirm the technical wording before I send it to the status-page team and customer care?
Arun | I will. Put the current facts in the [[incident timeline::Incident timeline records events chronologically, preserving the source and timing of changes in the service picture.]] as well, so later updates can show what changed and when.
Tess | If one monitoring screen turns green, can I immediately say that everyone is back online?
Arun | We need the agreed [[monitoring window::Monitoring window is the defined observation period used to establish stable service rather than relying on a single favorable reading.]] and the relevant service checks. One favorable indicator alone does not demonstrate that every affected service has recovered.
Tess | Then the next message may still say we are investigating, but it will have a named owner and a clear time.
Arun | Yes. If the impact changes, describe the [[restoration::Restoration is the verified return of service; it should be reported from the agreed evidence, not inferred from optimism.]] status precisely. Do not replace an unknown cause with a guess just to make the message feel more complete.
Tess | I will keep the 120-service figure, the East area, the investigation status, and the 09:40 Eastern update commitment together.
Arun | Good. Use that same factual core across channels. After recovery, the [[post-incident review::Post-incident review examines the response and causes after the incident; it is distinct from an immediate service-status update.]] can address the fuller explanation and any follow-up actions.''',
    transfer_title='Separate a second update from a forecast',
    transfer_setup='Incident R16 affects 45 voice services in the North area from 14:05. The next update is at 14:30 Central. The cause and restoration estimate remain unverified.',
    transfer='''Lead: "The incident reference is ___." | R16 | R16 is the identifier supplied for this separate interruption.
Agent: "The verified impact is ___." | 45 voice services | The record counts affected voice services, not individual users or broadband lines.
Lead: "Our next update is at ___." | 14:30 Central | This is the stated communication time and includes its time zone.
Agent: "The restoration estimate remains ___." | unverified | No verified restoration estimate is supplied, so the update time cannot replace it.''',
))


BOOK['units'].append(unit(
    title='Fiber Deployment and Construction Coordination',
    scene='Installed does not mean accepted',
    skill='Describe a construction handover accurately and request the missing acceptance evidence without overstating readiness.',
    brief='Fiber route F24 is physically installed. The contractor has supplied route photographs and an optical time-domain reflectometer trace, but the agreed handover package also requires an insertion-loss report, updated route drawings, and an inspection sign-off. Those three items remain pending. The next team has scheduled service work on the assumption that the route is accepted. Deployment coordinator Hana and construction lead Victor must correct that assumption. No inspection failure has been reported, but neither installation photographs nor a single test trace establish completion of the agreed acceptance process.',
    cast='Hana | Deployment coordinator\nVictor | Construction lead',
    culture=('Milestone words carry operational consequences', 'One team may use done to mean its own physical task has ended, while another hears permission to proceed. Use the named milestone and list the remaining dependencies. Ask for an owner and evidence instead of assigning blame for the misunderstanding.'),
    a='''Which milestone is complete? | Physical installation of route F24 | Inspection sign-off | Full handover acceptance | Service activation | Physical installation is confirmed, while the required acceptance items remain pending.
Which item has been supplied? | An OTDR trace | The insertion-loss report | The updated route drawings | The inspection sign-off | The contractor supplied the trace and photographs, not the three outstanding items.
What can be said about inspection? | Sign-off is pending; no failure is reported. | It has definitely failed. | It is unnecessary because photographs exist. | It has already authorized service. | Pending sign-off establishes neither a successful inspection nor a reported inspection failure.''',
    vocabulary='''fiber route | The path followed by an installed fiber cable system. | identify the fiber route
cable plant | The installed cabling and associated connecting components. | document the cable plant
as-built drawing | A drawing showing the installation as actually constructed. | update the as-built drawing
splice enclosure | A protective housing for joined fiber sections. | identify the splice enclosure
splice schedule | A record of planned or completed fiber connections. | reconcile the splice schedule
fiber strand | An individual optical fiber within a cable. | identify the fiber strand
termination | The prepared end connection of a cable or fiber. | document the termination
patch panel | A panel organizing connections between cables and equipment. | label the patch panel
OTDR | Optical time-domain reflectometer; an instrument locating fiber events from reflected light. | review the OTDR trace
insertion loss | Reduction in optical power through a link or component. | record insertion loss
loss budget | The planned allowance for optical loss across a link. | check the loss budget
acceptance criterion | A stated condition that must be met for acceptance. | confirm the acceptance criteria
test report | A documented account of test methods and results. | submit the test report
inspection sign-off | Recorded approval following the specified inspection. | obtain inspection sign-off
handover package | The agreed documents and evidence supplied at transfer. | complete the handover package
punch list | A recorded list of remaining defects or unfinished items. | close the punch list
snag | A defect or incomplete item requiring attention. | record a snag
demarcation point | The defined boundary between service or ownership responsibilities. | identify the demarcation point
wayleave | Permission to install or maintain infrastructure across another party's land. | check the wayleave
right of way | A legal or designated right to use a route or corridor. | confirm the right of way
duct | A protective conduit through which cable is routed. | identify the duct
pull section | A defined route segment used in cable-installation planning. | document the pull section
reinstatement | Restoration of disturbed surfaces after construction work. | inspect the reinstatement
ready for service | A status indicating the specified service-readiness conditions are met. | verify ready-for-service status''',
    precision='An OTDR trace helps locate and characterize events along a fiber. It is not a substitute for every required measurement. Here the agreed insertion-loss report remains a separate handover requirement, regardless of how convincing the trace appears.',
    precision_extra='Pending means not yet completed or decided. It does not mean failed. Use physically installed, inspection pending, and acceptance pending separately so that a planning team does not infer service readiness from a narrower construction milestone.',
    phrases='''Name the completed task | Physical installation of F24 is complete.
Correct the status | The route has not yet been accepted.
List the supplied evidence | We have photographs and an OTDR trace.
Identify a missing item | The insertion-loss report is still outstanding.
Request the current drawing | Please supply the updated as-built route drawing.
Clarify the inspection | Inspection sign-off is pending; no failure has been reported.
Separate the measurements | The trace does not replace the agreed loss report.
Refer to the agreement | Let us check the handover package against the acceptance criteria.
Ask about ownership | Who is responsible for each outstanding item?
Avoid a date assumption | Do we have confirmed submission dates or only targets?
Qualify downstream planning | The service work depends on acceptance, not just installation.
Correct the schedule note | Please mark the route as installed, acceptance pending.
Check the boundary | Which demarcation point does this report cover?
Keep evidence traceable | The test result needs the route and fiber identifiers.
Escalate the dependency | I will flag the acceptance gap to the scheduling team.
Close the handover | We will confirm readiness after the required evidence is reviewed.''',
    notes='''Has not yet | Describes an incomplete milestone without implying permanent failure.
Still outstanding | Identifies a required item that has not been supplied.
Does not replace | Prevents one type of evidence from standing in for a different requirement.
Against the criteria | Gives the review a defined reference instead of a general impression.
Depends on | Makes the sequence between milestones explicit.
Targets or confirmed dates | Distinguishes planning intentions from reliable commitments.''',
    d='''Which schedule note is supported? | F24 installed; acceptance pending. | F24 accepted and active. | F24 failed inspection. | F24 requires no further documents. | The note states the completed physical work while preserving the unresolved acceptance status.
What should Hana request? | The missing reports, drawings, and inspection sign-off with owners and dates | A more confident version of the same photographs | Immediate activation regardless of acceptance | A statement that OTDR replaces all testing | The request addresses the three actual dependencies and makes follow-up responsibility clear.
Which sentence handles the inspection accurately? | We are awaiting sign-off; no failure has been reported. | Pending always means failed. | A photograph counts as inspector approval. | Installation automatically closes inspection. | The evidence supports pending approval but contains no report of an inspection failure.
What is the best response to the OTDR argument? | The trace is useful, but the agreed insertion-loss report is still required. | The two records always measure exactly the same thing. | A trace automatically accepts every strand. | We can remove the requirement after the fact. | The response recognizes the supplied evidence without replacing a distinct agreed acceptance requirement.''',
    dialogue='''Hana | The service team has F24 on tomorrow's schedule. Their note says the route is complete, so they have treated it as available.
Victor | The [[fiber route::Fiber route identifies the specific installed cable path; completing its physical work does not establish every acceptance milestone.]] is physically installed. That is what the contractor reported, but I have not issued an acceptance notice for the handover.
Hana | We need to correct the schedule before that wording travels further. What evidence has actually arrived?
Victor | We have photographs and an [[OTDR::OTDR identifies the instrument used to produce the supplied trace; that trace does not satisfy every separate handover requirement.]] trace. The agreed package also includes an insertion-loss report, updated route drawings, and inspection sign-off. Those three items are still outstanding.
Hana | The contractor says the trace looks good. Does that make the separate loss report a paperwork formality?
Victor | No. [[Insertion loss::Insertion loss describes optical power reduction through the link; its required report is distinct from the supplied event trace.]] is a separate required result in our agreement. We should not treat one type of evidence as a replacement for another because it looks reassuring.
Hana | The current route drawing is the design version. Does the handover need to show the final installed path?
Victor | Yes, we need the [[as-built drawing::As-built drawing records the actual constructed arrangement rather than simply repeating the planned design.]] for the completed installation. If the route or connections changed, the receiving team needs the actual arrangement, not an assumption that the original plan stayed unchanged.
Hana | Is the inspection delayed because something failed, or do we simply not have a recorded decision yet?
Victor | We are awaiting [[inspection sign-off::Inspection sign-off is the recorded approval still pending; its absence does not establish that the inspection failed.]]. No failure has been reported. I would avoid saying passed or failed until we have the inspection record and its actual outcome.
Hana | Then I should tell the service team that installation is complete but acceptance remains pending.
Victor | Exactly. Ask them to plan against the [[acceptance criteria::Acceptance criteria are the agreed conditions for accepting the route, rather than a general impression that construction looks finished.]], not the contractor's shorthand. We need the outstanding evidence reviewed before anyone turns that status into ready for service.
Hana | Can you send me a list showing who owns each missing item and when it is expected?
Victor | I will update the [[handover package::Handover package brings together the agreed documents and evidence; tracking its missing items makes the transfer dependency explicit.]] tracker with owners and target dates. I will mark a date confirmed only when the responsible person has actually committed to it.
Hana | The test files also need to identify what was measured. There are several fibers and more than one termination point.
Victor | Agreed. Each result needs the route, [[fiber strand::Fiber strand identifies the individual optical fiber tested, preventing a result for one strand from being assumed to cover another.]], and endpoint references. A technically valid result is still unhelpful if the receiving team cannot match it to the connection they will use.
Hana | I will move the schedule note out of the accepted column and explain the dependency to the next team.
Victor | Use [[ready for service::Ready for service is a defined readiness status; it should follow the required evidence and authorization, not physical installation alone.]] only after the required review. That keeps the milestone meaningful and avoids asking the next team to discover the missing records on site.
Hana | I will also keep pending separate from failed. We need to correct the assumption without inventing a construction defect.
Victor | Thank you. Once the evidence is complete, we can confirm the [[demarcation point::Demarcation point defines the responsibility boundary at handover, helping the receiving team understand exactly what is being transferred.]] and the accepted scope together, then notify scheduling with a clear, traceable status.''',
    transfer_title='Check a second handover',
    transfer_setup='Route C18 is installed. Its drawings and loss report are supplied, but inspection sign-off is pending. The agreed local process requires that sign-off before acceptance.',
    transfer='''Coordinator: "The route identifier is ___." | C18 | C18 is the route named in this separate handover record.
Contractor: "The completed milestone is ___." | physical installation | The record confirms installation, not completion of every acceptance requirement.
Coordinator: "The outstanding approval is ___." | inspection sign-off | Drawings and loss results are supplied, leaving the stated inspection approval pending.
Contractor: "The acceptance status remains ___." | pending | The local acceptance condition has not been met while the required sign-off remains outstanding.''',
))

BOOK['units'].append(unit(
    title='Wireless Capacity and Coverage',
    scene='A signal map cannot explain a busy-hour slowdown',
    skill='Compare wireless observations, test a causal claim, and request measurements that distinguish coverage from capacity.',
    brief='A station concourse provides public Wi-Fi. A coverage map shows signal availability across the seating area. During one quiet-period test, a device achieved 80 megabits per second; during one busy-period test, it achieved 5. The tests do not control for client count, device conditions, interference, or backhaul load. Station manager Mei asks wireless engineer Jordan whether adding access points will solve the problem. Jordan must explain why visible signal does not guarantee usable capacity and why two speed readings alone cannot establish the cause or justify a particular equipment change.',
    cast='Mei | Station service manager\nJordan | Wireless engineer',
    culture=('Translate the distinction before the acronym', 'A customer-facing colleague may hear strong signal as good service. Start with the difference between reaching a device and serving its traffic, then introduce the technical measures. Correct an inference without making the person feel foolish for using a coverage map.'),
    a='''What does the coverage map establish here? | Reported signal availability across the seating area | Guaranteed throughput for every user | The cause of the busy-hour slowdown | Sufficient backhaul capacity at all times | The map concerns signal availability and does not establish end-to-end performance or cause.
What were the two observed speeds? | 80 Mbps quiet and 5 Mbps busy | 5 Mbps quiet and 80 Mbps busy | 80 Mbps at both times | Zero Mbps at both times | The brief records those two readings under different, uncontrolled operating conditions.
What is not yet justified? | A claim that extra access points will solve the issue | A request for comparable measurements | Distinguishing coverage from capacity | Recording the test times | The evidence does not isolate the limiting factor or establish the effect of additional access points.''',
    vocabulary='''WLAN | Wireless local-area network, commonly implemented using Wi-Fi. | assess the WLAN
access point | A device connecting wireless clients to a network. | identify the access point
coverage | The area in which a usable radio signal is available under stated conditions. | assess coverage
capacity | The traffic or user demand a system can support under stated conditions. | assess capacity
throughput | The achieved rate of useful data transfer over a measured interval. | measure throughput
bandwidth | A frequency range or, in service discussions, a link's nominal data capacity. | specify the bandwidth
RSSI | Received signal strength indicator; a measure of received radio signal level. | record RSSI
SNR | Signal-to-noise ratio; signal level compared with background noise. | measure SNR
airtime | Time during which a shared wireless channel is occupied. | measure airtime utilization
channel utilization | The proportion of observed time a channel is busy. | compare channel utilization
co-channel interference | Interference or contention involving devices sharing a channel. | assess co-channel interference
adjacent-channel interference | Interference involving transmissions on neighboring channels. | investigate adjacent-channel interference
client density | The concentration of connected or active devices in an area. | measure client density
concurrency | Simultaneous activity by multiple users or processes. | assess peak concurrency
backhaul | The connection carrying traffic onward from an access network. | check backhaul load
bottleneck | A limiting point that constrains overall performance. | locate the bottleneck
contention | Competition among devices for a shared transmission resource. | measure contention
roaming | A client's movement between access points while maintaining connectivity. | assess roaming behavior
sticky client | Informal term for a client that stays attached to a less suitable access point. | investigate a sticky client
site survey | A structured assessment of a wireless environment. | conduct a site survey
heat map | A visual representation of measurements across an area. | interpret the heat map
busy hour | A defined period of high traffic demand. | compare busy-hour results
baseline | A reference measurement used for comparison. | establish a baseline
test condition | A documented circumstance under which a measurement is taken. | control the test conditions''',
    precision='Coverage asks where a signal is available. Capacity asks how much demand the system can support under specified conditions. Throughput is an observed transfer rate. These related terms are not interchangeable, and a coverage map does not guarantee a throughput result.',
    precision_extra='A quiet test and a busy test can reveal a performance difference without identifying its cause. Record device, location, time, client activity, radio conditions, and onward-link load before attributing the change to a particular bottleneck.',
    phrases='''Acknowledge the map | The map is useful for signal availability.
Name its limit | It does not guarantee throughput during peak demand.
State the observations | We observed eighty megabits per second in the quiet test and five in the busy test.
Keep evidence bounded | Those are two readings, not a complete performance profile.
Explain capacity | More simultaneous demand can compete for the same resources.
Avoid a diagnosis | We have not yet isolated the bottleneck.
Request comparable data | Let us repeat the tests under documented conditions.
Ask about devices | Were the device, location, and test method the same?
Check radio conditions | We need signal, noise, and channel-utilization measurements.
Check the onward path | We should compare backhaul load at the same time.
Qualify the proposal | Extra access points are an option to assess, not a confirmed solution.
Prevent oversimplification | A strong signal can coexist with poor throughput.
Separate time periods | The quiet-period result does not represent the busy hour.
Ask for the objective | What service level are we trying to support in this area?
Report the next step | I will bring a comparison of the measurements and likely constraints.
Close without a promise | We can recommend a change after the limiting factor is better established.''',
    notes='''Useful for | Acknowledges what a piece of evidence can establish.
Does not guarantee | Blocks an unsupported inference without dismissing the evidence.
Can coexist | Shows that two apparently conflicting observations may both be true.
At the same time | Makes cross-system measurements more comparable.
An option to assess | Presents a possible intervention without claiming it will work.
After ... established | Connects a recommendation to the evidence needed to justify it.''',
    d='''Which explanation is most accurate? | Signal availability and busy-hour throughput measure different things. | A coverage map guarantees every speed test. | Strong signal rules out all congestion. | One slow test proves the access point is defective. | The explanation distinguishes coverage from achieved performance without inventing a cause.
What should Jordan say about adding access points? | It is an option to assess after identifying the constraint. | It will definitely solve the issue. | It always increases throughput in proportion to device count. | It makes interference impossible. | Additional access points may help in some designs, but the current evidence does not establish that result.
Which comparison is more useful? | Documented tests with radio and backhaul measurements from the same periods | Unlabeled screenshots from different months | A coverage map without traffic observations | Only the fastest quiet-period result | Matched context helps the team distinguish competing explanations for the observed slowdown.
What is supported by the two readings? | Measured throughput differed between the two tests. | Backhaul was certainly the cause. | Every user received exactly five Mbps. | The coverage map was necessarily false. | The readings establish a difference in observed throughput, not a population-wide result or a specific cause.''',
    dialogue='''Mei | The coverage map shows a signal across the concourse, but passengers still complain during the evening rush. Are they connecting incorrectly?
Jordan | Not necessarily. [[Coverage::Coverage concerns signal availability across an area; it does not establish the throughput each connected passenger will receive.]] tells us something about the radio signal, not everything about the service passengers experience when many devices are active.
Mei | Our quiet test reached eighty megabits per second. In the busy test, the same report shows only five.
Jordan | Those are [[throughput::Throughput is the achieved data-transfer rate measured in each test, unlike a signal map or nominal link specification.]] readings under different conditions. They show a performance difference, but we need more context before explaining why that difference occurred.
Mei | I had assumed that a strong signal meant the connection should be fast. What distinction should I use with the station team?
Jordan | Separate signal availability from [[capacity::Capacity describes how much demand the system can support under specified conditions, not merely whether a signal reaches a device.]]. A device may receive a strong signal while competing with many other devices or encountering a limit elsewhere in the path.
Mei | Would buying more access points give each passenger a larger share? The purchasing team wants a simple recommendation.
Jordan | First we need to locate the [[bottleneck::Bottleneck is the limiting point in the service path; identifying it helps determine whether an equipment proposal addresses the actual constraint.]]. Extra access points are not automatically the answer, especially if channel conditions or an onward connection are limiting performance.
Mei | What should we collect that the existing map and two speed tests do not tell us?
Jordan | Start with [[client density::Client density measures the concentration of devices in the area, adding demand context that a signal map alone does not show.]] and activity during the busy period. We also need the test device, location, method, and time recorded so the comparisons mean something.
Mei | The map was produced before the new seating area opened. Could that change the way demand is distributed?
Jordan | It could. We should review [[airtime::Airtime is the shared wireless-channel time consumed by transmissions; high demand can reduce the opportunity available to each active client.]] use across the area, not simply count installed equipment. A changed concentration of active devices may alter how the shared radio resource is used.
Mei | Is interference a definite explanation, or is it another possibility to investigate?
Jordan | It is a possibility. Measurements of signal, noise, and [[channel utilization::Channel utilization measures how busy a wireless channel is, helping assess radio conditions without declaring interference proven in advance.]] can help us distinguish radio conditions from other constraints. We should not name interference as the cause before checking.
Mei | You also mentioned the onward connection. The station team tends to think everything beyond the access point is the same problem.
Jordan | The [[backhaul::Backhaul carries traffic onward from the access network; a constraint there can affect performance even when radio coverage is adequate.]] needs attention too. We should compare its load during the same periods, because a limit there can affect users even where the radio signal is adequate.
Mei | Then the eighty-megabit result is useful, but it does not promise that rate at the busiest time.
Jordan | Correct. It is one [[baseline::Baseline is a reference observation for comparison; a quiet-period result does not automatically represent performance under peak demand.]], with its conditions attached. We need a comparable busy-period picture rather than treating the fastest observation as a guaranteed service level.
Mei | I will tell purchasing that we are gathering evidence before recommending equipment, and explain the distinction to the station team.
Jordan | Good. I will document the [[test conditions::Test conditions record the circumstances behind measurements, making the comparison interpretable and reducing unsupported claims about cause.]] and bring back the measured constraints. Then we can discuss a targeted change and how its effect would be evaluated.''',
    transfer_title='Describe another wireless comparison',
    transfer_setup='A library Wi-Fi test records 60 Mbps at 08:00 and 12 Mbps at 16:00. Signal availability is shown on a map. Client activity and backhaul load have not been measured.',
    transfer='''Manager: "The 08:00 throughput reading was ___." | 60 Mbps | Sixty megabits per second is the early test result stated in the record.
Engineer: "The 16:00 throughput reading was ___." | 12 Mbps | Twelve megabits per second is the later observed result, not a guaranteed rate for all users.
Manager: "The map describes ___." | signal availability | The supplied map concerns coverage rather than measured traffic capacity or cause.
Engineer: "The cause of the difference remains ___." | unconfirmed | Missing demand and backhaul observations prevent the readings alone from establishing the cause.''',
))


BOOK['units'].append(unit(
    title='Provisioning and Service Activation',
    scene='One address, two circuits, no activation date',
    skill='Resolve an incomplete service request through precise identifiers, time references, and a closed-loop read-back.',
    brief='Order A77 asks for activation at 18 Cedar Plaza but omits the circuit reference and requested date. The site has two services: circuit CP-204 for the ground-floor office and CP-205 for the upstairs studio. During the clarification call, customer coordinator Omar confirms CP-205 and requests 7 October, 18:00-20:00 Eastern. Provisioning specialist Lina has not yet checked resources, approvals, or dependencies. The requested window must be recorded as requested, not confirmed. No one has authorized a change to CP-204, and the conversation does not establish that activation will be interruption-free.',
    cast='Omar | Customer service coordinator\nLina | Provisioning specialist',
    culture=('A read-back is a reliability tool', 'Repeating a long identifier can feel formal, but it gives both sides a chance to catch a mismatch. Read back the service, location, date, and time zone together. Use requested and confirmed deliberately so politeness does not turn into accidental acceptance.'),
    a='''Which circuit does Omar request? | CP-205 for the upstairs studio | CP-204 for the ground-floor office | Every circuit at Cedar Plaza | An unidentified replacement circuit | Omar identifies the upstairs studio service as CP-205 during the clarification.
What is the status of the 7 October window? | Requested, not yet confirmed | Approved and guaranteed | Already completed | Rejected as impossible | Lina has not checked the resources, approvals, and dependencies needed to confirm the window.
Which service is outside the stated request? | CP-204 | CP-205 | The upstairs studio service | The service named in A77 after clarification | No change to CP-204 is authorized by the clarified request.''',
    vocabulary='''provisioning | Preparing and configuring resources for a specified service. | coordinate provisioning
activation | Enabling an identified service for use. | schedule activation
service order | A recorded request for a defined service action. | validate the service order
circuit reference | An identifier for a particular telecommunications circuit. | read back the circuit reference
service address | The location associated with the requested service. | verify the service address
service identifier | A unique reference distinguishing a specific service. | confirm the service identifier
order validation | Checking that an order is complete and consistent. | complete order validation
requested date | The date the customer asks for, before confirmation. | record the requested date
committed date | A date formally confirmed under the applicable process. | verify the committed date
activation window | The scheduled period for enabling a service. | confirm the activation window
time zone | The regional time standard used for a schedule. | state the time zone
dependency | A condition or task that must be satisfied before another proceeds. | identify the dependency
resource availability | Whether required people, capacity, or equipment are available. | check resource availability
service profile | The defined configuration or characteristics of a service. | verify the service profile
port assignment | Allocation of a physical or logical connection point. | check the port assignment
CPE | Customer premises equipment used at the customer's location. | verify the CPE details
ONT | Optical network terminal connecting a customer to an optical access network. | identify the ONT
handoff | The point or process where service or responsibility transfers. | confirm the handoff
cutover | A planned transition from one service arrangement to another. | coordinate the cutover
number porting | Transfer of a telephone number between service providers or arrangements. | confirm number-porting dependencies
portability | The ability to retain a telephone number when changing eligible service arrangements. | check portability requirements
acceptance test | A defined check used to determine whether a service meets acceptance requirements. | arrange the acceptance test
order fallout | An order exception that prevents normal processing. | resolve order fallout
read-back | Repetition of key details to confirm shared understanding. | perform a read-back''',
    precision='A service address locates the premises; it does not necessarily identify the circuit. Preserve the exact reference when several services share a site. An order number identifies the request, while the circuit reference identifies what the request concerns.',
    precision_extra='Requested and committed dates are different statuses. Repeating a requested window does not confirm it. A successful clarification supplies missing information; the provisioning team must still complete the relevant checks and communicate the actual scheduling decision.',
    phrases='''Identify the request | I am checking service order A77.
Explain the ambiguity | There are two circuits at that address.
Ask for the exact reference | Which circuit is included in this request?
Confirm the location | CP-205 serves the upstairs studio.
Exclude the other service | CP-204 is outside this request.
Ask for the date | What activation date are you requesting?
Complete the time reference | Please include the time zone with the window.
Read back the request | You are requesting 7 October, 18:00-20:00 Eastern.
Keep status clear | I have recorded that as requested, not confirmed.
Name the checks | We still need to check resources, approvals, and dependencies.
Avoid implied acceptance | This clarification does not yet commit the activation window.
Check the order scope | Is this activation only, or does the order include a cutover?
Avoid a continuity promise | I cannot confirm an interruption-free change from this information.
State the next step | I will return the scheduling decision through the order process.
Request a correction | Please correct any part of that read-back that does not match your request.
Close with a boundary | No action on CP-204 is included in the clarified order.''',
    notes='''Which circuit | Requests an identifier instead of relying on a shared street address.
Included in | Defines the scope of the specific request.
Requesting | Records the customer's preference without promising availability.
As requested, not confirmed | Explicitly separates information capture from acceptance.
Still need to | Names checks that remain open.
Does not yet commit | Prevents a courteous acknowledgment from becoming a scheduling promise.''',
    d='''Which clarification is most useful first? | Which circuit reference at 18 Cedar Plaza is the request for? | Can we activate both circuits to save time? | Should we assume the ground floor? | May we omit the circuit field? | The address is ambiguous because two distinct circuits serve the same premises.
Which read-back is correct? | A77 requests CP-205 on 7 October, 18:00-20:00 Eastern; confirmation is pending. | CP-204 is approved for immediate activation. | Both services are guaranteed for 7 October. | CP-205 was activated during the call. | The read-back preserves the order, circuit, date, time zone, and unconfirmed scheduling status.
What is overpromised? | There will definitely be no interruption. | We need to check dependencies. | The requested circuit is CP-205. | The window is not yet confirmed. | The supplied information does not establish that the activation can occur without interruption.
What should Lina do after clarification? | Complete the relevant checks and return the scheduling decision. | Treat the customer's preferred date as automatically committed. | Change CP-204 because it shares the address. | Delete the time zone from the order. | Clarification completes missing request information but does not replace approval or scheduling checks.''',
    dialogue='''Lina | I am reviewing A77 for 18 Cedar Plaza. The address is present, but I cannot see the circuit reference or the requested activation date.
Omar | Thanks for checking the [[service order::Service order identifies the recorded request; it must be distinguished from the individual circuit that the request will affect.]]. We have a ground-floor office and an upstairs studio there. The request concerns the studio, not the office service.
Lina | There are two references on the site record, CP-204 and CP-205. Which one belongs to the studio request?
Omar | The [[circuit reference::Circuit reference identifies the precise service to act on, preventing the shared address from being treated as sufficient identification.]] is CP-205. CP-204 serves the ground-floor office and should not be included in this activation request.
Lina | I will read that back: CP-205, upstairs studio, at 18 Cedar Plaza. No action on CP-204 is included.
Omar | That [[read-back::Read-back repeats the key details so both people can confirm or correct the same service, location, and scope.]] is correct. The studio team wants the service available for its new schedule, so they are asking for an evening window.
Lina | What date and time should I record, and which time zone are they using?
Omar | The [[requested date::Requested date records the customer's preference before the provider completes the checks needed to confirm a commitment.]] is 7 October. They are asking for 18:00 to 20:00 Eastern, when the studio team can make a contact available.
Lina | I can capture that request, but I have not yet checked the team, capacity, or approvals needed for it.
Omar | Please keep the [[activation window::Activation window is the specified period for enabling the service; in this conversation it remains a request rather than an approved slot.]] marked as requested. I do not want the studio to read an acknowledgment as confirmation that the work is booked.
Lina | Exactly. I also need to check whether the order has any dependencies beyond enabling this service.
Omar | Let me know which [[dependency::Dependency is a prerequisite for the activation, so identifying it matters before the requested date becomes a confirmed schedule.]] needs customer input. I can help gather the information, but I should not assume the order has cleared every internal step.
Lina | The address record alone did not tell us whether this was a new activation, a cutover, or a change to both services.
Omar | The [[order validation::Order validation checks completeness and consistency; it resolves ambiguities rather than allowing staff to infer a broader scope.]] matters, then. Keep the scope limited to the stated studio request and ask before adding any work involving the office.
Lina | Will the studio team expect me to guarantee that there will be no interruption during the change?
Omar | No. We have not established that. The [[service identifier::Service identifier keeps the conversation tied to the exact service while performance or continuity expectations are checked separately.]] tells us what is involved, but it does not by itself tell us the operational effect of the work.
Lina | I will return the scheduling decision through the order process after checking resources and the remaining approvals.
Omar | Once you have a [[committed date::Committed date is a formally confirmed schedule, unlike the requested date that the customer has supplied during this call.]], I will pass that exact status to the studio. Until then, I will describe 7 October as our request.
Lina | One final check: A77, CP-205, upstairs studio, 7 October from 18:00 to 20:00 Eastern, with confirmation pending.
Omar | Correct, including the [[time zone::Time zone removes ambiguity for teams in different locations; Eastern is part of the requested window, not an optional detail.]]. Please keep CP-204 outside the request, and contact me if any part of the order conflicts with that read-back.''',
    transfer_title='Clarify another activation request',
    transfer_setup='Order B62 concerns circuit MS-310 at the west office, not MS-311 at the east office. The customer requests 12 October, 09:00-11:00 Pacific. Scheduling checks are incomplete.',
    transfer='''Specialist: "The requested circuit is ___." | MS-310 | MS-310 identifies the west-office service named in the request.
Coordinator: "The requested date is ___." | 12 October | The customer specifies this date, but the scheduling checks remain incomplete.
Specialist: "The requested time window is ___." | 09:00-11:00 Pacific | The supplied window includes Pacific time, preventing a cross-location scheduling ambiguity.
Coordinator: "The scheduling status is ___." | not yet confirmed | Incomplete scheduling checks mean the requested window is not a committed appointment.''',
))

BOOK['units'].append(unit(
    title='Field Service and Dispatch',
    scene='Turn internet bad into a useful ticket',
    skill='Elicit observable symptoms, document unknowns, and set accurate expectations for a field-service handoff.',
    brief='Ticket J31 says only internet bad. During a clarification call, customer Erin reports that video calls drop on two Wi-Fi laptops between 18:00 and 20:00. Wired performance has not been checked. The service address is verified through the approved process. Dispatcher Paulo must document the reported pattern without diagnosing a failed router or treating untested wired service as faulty. Erin can provide access from 13:00 to 15:00 on Friday, but that availability has not been booked. A visit, if confirmed, would be an investigation appointment rather than a guarantee of repair within the window.',
    cast='Paulo | Service dispatcher\nErin | Customer office coordinator',
    culture=('Use questions that produce observable answers', 'Customers may describe a service as bad because they do not know the technical distinction. Ask what stops working, on which devices, and when. Repeat their report accurately without turning a customer observation into a confirmed technical diagnosis.'),
    a='''What symptom is reported? | Video calls drop on two Wi-Fi laptops between 18:00 and 20:00. | All wired devices fail all day. | The router is proven defective. | Every application on every device is unavailable. | The customer reports a specific application, connection type, device count, and time pattern.
What is unknown? | Wired performance | The ticket number | The reported time range | Whether the two reported devices use Wi-Fi | No wired-performance observation has been supplied during the clarification.
What does Friday 13:00-15:00 represent? | Customer availability, not a booked appointment | A guaranteed repair completion time | A confirmed technician arrival | The time the fault occurs | Erin has offered access availability, but dispatch has not confirmed a booking.''',
    vocabulary='''trouble ticket | A recorded report of a service problem. | update the trouble ticket
symptom | An observable sign of a problem. | describe the symptom
intermittent fault | A problem that appears and disappears rather than remaining constant. | document an intermittent fault
reproducibility | Whether a reported issue can be observed again under stated conditions. | assess reproducibility
affected device | A device on which a problem has been reported or observed. | identify affected devices
wired connection | A network connection using a physical cable. | check wired-connection evidence
wireless connection | A network connection using radio transmission. | identify the wireless connection
dropout | A temporary loss or interruption of a connection or service. | report a dropout
symptom window | The time range in which a problem is observed. | record the symptom window
customer availability | The times a customer can support access or contact. | confirm customer availability
dispatch | Assignment and coordination of field-service work. | request dispatch review
work order | An authorized instruction defining service work to be carried out. | review the work order
appointment window | A scheduled period for the agreed visit or arrival arrangement. | confirm the appointment window
site access | Permission and practical arrangements for entering the premises. | arrange site access
access contact | The person coordinating entry to the location. | identify the access contact
no-access visit | A visit that cannot proceed because required site access is unavailable. | avoid a no-access visit
remote diagnostics | Investigation using approved tools without an on-site visit. | review remote diagnostics
line test | A defined check of a telecommunications line's condition or performance. | review line-test results
fault code | A coded classification or result associated with a reported fault. | verify the fault code
repeat dispatch | A further field visit for a previously reported issue. | review repeat-dispatch history
first-time fix | Resolution during the first relevant service visit. | measure first-time-fix performance
repair authorization | Approval for specified repair work. | confirm repair authorization
customer-reported | Describes information supplied by the customer rather than independently verified. | label customer-reported symptoms
closure note | A record explaining the outcome when a ticket is closed. | complete the closure note''',
    precision='Customer-reported identifies the source of an observation, not a reason to dismiss it. Record the application, devices, connection type, and time pattern. Do not widen two Wi-Fi laptops into every device or turn unknown wired performance into a confirmed fault.',
    precision_extra='Availability is not a booking, and an appointment is not a repair guarantee. Separate the customer access window, the confirmed visit arrangement, the investigation task, and any authorized repair. Avoid promising an outcome before diagnosis and approval.',
    phrases='''Open the clarification | I want to add a clear symptom description to J31.
Ask about the effect | What stops working when the problem happens?
Identify the devices | Which devices have shown the issue?
Identify the connection | Are those devices using Wi-Fi or a cable?
Ask for the pattern | When does the problem usually occur?
Preserve the observation | You report video-call dropouts on two Wi-Fi laptops.
Mark the unknown | Wired performance has not been checked.
Avoid a diagnosis | That pattern does not yet establish a failed router.
Confirm the source | I will label these as customer-reported symptoms.
Ask about access | When can someone provide access to the site?
Separate availability | I have recorded Friday afternoon as your availability.
Avoid a booking assumption | The appointment has not yet been confirmed.
Clarify the purpose | A visit would investigate the reported problem.
Avoid a repair promise | The visit window is not a guaranteed repair deadline.
Protect credentials | Please do not send passwords or one-time security codes in the ticket.
Close the handoff | I will pass on the symptoms, unknowns, access contact, and requested availability.''',
    notes='''What stops working | Invites an observable description rather than an assumed cause.
Which devices | Narrows the scope of the report.
Has not been checked | Preserves an unknown instead of converting it into a negative result.
Customer-reported | Attributes the information accurately.
Would investigate | Describes the purpose of a possible visit without claiming a result.
Not a ... deadline | Separates a scheduled contact from an outcome guarantee.''',
    d='''Which ticket summary preserves the report? | Customer reports video-call drops on two Wi-Fi laptops from 18:00 to 20:00; wired status unknown. | Router failure confirmed on every device all day. | Wired service is definitely faulty. | Friday afternoon is the fault's only occurrence. | The summary retains the observed scope, timing, source, and untested wired condition.
Which question provides useful clarification? | Are the affected laptops using Wi-Fi or a cable? | Can you guess which component has failed? | Will you send all passwords in the ticket? | Can we mark every service unavailable? | Connection type helps describe and investigate the symptom without asking the customer to invent a diagnosis.
Which appointment statement is accurate? | Friday 13:00-15:00 is your availability; booking is not yet confirmed. | The technician is guaranteed to finish repairs by 15:00. | Offering access automatically books the visit. | The appointment proves the cause. | The statement distinguishes offered access from a confirmed visit and avoids guaranteeing repair.
What should remain marked unknown? | Wired performance | Whether two Wi-Fi laptops were reported | The J31 ticket reference | The reported evening time range | The clarification contains no wired test or observation, so its status remains unknown.''',
    dialogue='''Paulo | I have J31 in front of me. It currently says internet bad, and I want the field team to understand what you are actually experiencing.
Erin | The main [[symptom::Symptom describes the observable video-call interruption without assuming which component or network segment caused it.]] is that video calls drop. We reconnect, but the call sometimes drops again. It is disruptive when the evening team meets customers.
Paulo | Which devices have shown that problem? I do not want to assume it affects everything at the site.
Erin | The [[affected devices::Affected devices limits the report to the two laptops, not every device at the premises.]] are two laptops used by that team. Both are on Wi-Fi. I do not have a report about the other devices.
Paulo | Have you observed the same behavior on a wired connection, or is that still unknown?
Erin | [[Wired performance::Wired performance remains untested; no observation establishes either success or failure.]] has not been checked. I would rather leave that unknown than have the ticket suggest we tested something we did not.
Paulo | That is helpful. Is there a time pattern, or does it happen throughout the day?
Erin | The [[symptom window::Symptom window identifies the reported occurrence period, which is separate from the customer's availability for a field visit.]] is usually 18:00 to 20:00. That is when these users are making their calls. I cannot say what happens overnight.
Paulo | I will record those details as reported and keep the router diagnosis open. This pattern alone does not identify a failed component.
Erin | Please mark it [[customer-reported::Customer-reported attributes the observations to Erin rather than presenting them as independently verified findings.]]. I can describe what the staff experienced, but I do not have a technical test result to attach.
Paulo | The service address has been verified through our process. Who can arrange entry if a visit is approved?
Erin | I will be the [[access contact::Access contact names the person coordinating entry so the technician can reach the relevant work area.]]. I can meet the technician and make sure they reach the area where the two laptops are used.
Paulo | What availability should I send to dispatch? I need to distinguish your preferred time from an appointment we have actually booked.
Erin | Our [[customer availability::Customer availability is the offered access period; it does not become an appointment until scheduling is confirmed.]] is Friday from 13:00 to 15:00. The evening users will not be there, but I can provide their symptom notes.
Paulo | I will record that as availability only. The scheduling team must confirm whether a visit can be arranged within that period.
Erin | And a confirmed [[appointment window::Appointment window specifies the visit arrangement, not a deadline guaranteeing fault resolution.]] would mean an investigation visit, not a guarantee that the connection will be repaired by three. Is that right?
Paulo | Correct. The next step depends on the approved diagnostic process and what the investigation finds. I cannot promise a repair result now.
Erin | Then include the evening pattern in the [[work order::Work order carries the task and facts to the field team; the timing helps them prepare.]] if dispatch proceeds. Otherwise the technician may arrive at a time when the symptom is not visible.
Paulo | I will pass on the two laptops, Wi-Fi connection, evening dropouts, unknown wired status, and your access availability. Do not send passwords in the ticket.
Erin | Thank you. That should make the [[dispatch::Dispatch coordinates the visit using the clarified symptoms, access details, and scheduling status.]] more useful. Please send the booking decision separately so our staff do not mistake this clarification call for a confirmed visit.''',
    transfer_title='Prepare a second dispatch summary',
    transfer_setup='Ticket P28 reports voice-call dropouts on one wired desk phone from 10:00 to 11:00. Other phones have not been checked. The customer offers Monday 15:00-17:00 for access; no booking exists.',
    transfer='''Dispatcher: "The affected device is ___." | one wired desk phone | The report identifies one wired phone, not every phone or a wireless laptop.
Customer: "The reported symptom window is ___." | 10:00-11:00 | This is when the dropouts occur, not the offered access period.
Dispatcher: "Other-phone performance is ___." | not checked | No observations for other phones are supplied, so their performance remains unverified.
Customer: "My access availability is ___." | Monday 15:00-17:00 | This is offered availability only; the separate record says no appointment has been booked.''',
))


BOOK['units'].append(unit(
    title='Regulatory and Emergency Services',
    scene='Always works is not an approved notice',
    skill='Challenge an unsupported service claim and coordinate a clear, service-specific customer notice with the responsible reviewers.',
    brief='A U.S. interconnected Voice over Internet Protocol provider is preparing a customer notice. The draft says, "911 always works, even without power or broadband." Product records identify dependence on powered customer equipment and a broadband connection, but the draft has not been reviewed against the current applicable requirements or approved service wording. Communications editor Celia and compliance reviewer Marcus must remove the absolute assurance, obtain verified service-specific limitations, and route the notice for review. The task is not to invent a universal disclaimer or conduct an emergency test call.',
    cast='Celia | Customer communications editor\nMarcus | Compliance reviewer',
    culture=('Plain language can still preserve conditions', 'Removing jargon should make a limitation easier to understand, not make it disappear. Explain the customer consequence, retain the relevant conditions, and ask the accountable team to verify the wording. A confident tone does not justify an absolute service guarantee.'),
    a='''What is wrong with the draft assurance? | It promises availability despite dependencies identified in the product record. | It includes an unnecessary date. | It gives an approved service-specific limitation. | It is already reviewed and authorized. | The absolute assurance conflicts with known equipment and broadband dependencies and lacks the required review.
What should happen next? | Verify the limitations and route revised wording through the responsible review process. | Publish the assurance because it sounds reassuring. | Invent a universal disclaimer for all services. | Call 911 simply to test the draft. | The task requires verified service-specific content and review, not unsupported publication or an emergency test call.
What jurisdiction and service context are stated? | U.S. interconnected VoIP | Every telephone service worldwide | Only private radio systems | A mobile-only service outside the United States | The brief expressly identifies the U.S. interconnected-VoIP context, which limits the regulatory discussion.''',
    vocabulary='''VoIP | Voice over Internet Protocol; voice communication carried over IP networks. | describe the VoIP service
interconnected VoIP | A regulatory service category connecting IP-based voice with the public telephone network. | identify interconnected-VoIP obligations
E911 | Enhanced 911; emergency calling with associated routing and caller information functions. | review E911 requirements
PSAP | Public safety answering point; a facility receiving emergency calls. | identify the relevant PSAP
dispatchable location | Location information sufficient to identify where assistance is needed under applicable rules. | verify dispatchable-location requirements
registered location | Location information supplied or maintained for a service under applicable arrangements. | update the registered location
fixed service | A service associated with a fixed location under the relevant definition. | determine fixed-service requirements
non-fixed service | A service not restricted to a fixed location under the relevant definition. | review non-fixed-service requirements
nomadic use | Use of a service from changing locations. | assess nomadic-use implications
power dependency | Reliance on electrical power for service operation. | disclose the power dependency
broadband dependency | Reliance on a broadband connection for service operation. | explain the broadband dependency
backup power | An alternative power source intended to support operation during a primary-power loss. | verify backup-power capabilities
service limitation | A condition restricting availability, function, or performance. | explain a service limitation
customer notification | Information provided to customers about a relevant service matter. | review the customer notification
affirmative acknowledgment | An active indication that a customer has received or recognized specified information. | record affirmative acknowledgment
prominence | The degree to which important information is noticeable. | assess the notice's prominence
plain-language notice | A notice using understandable wording while preserving necessary facts. | prepare a plain-language notice
absolute assurance | An unconditional promise such as always or never. | remove an absolute assurance
applicability | Whether a requirement covers the specific service or situation. | assess applicability
approved wording | Language authorized through the responsible review process. | use approved wording
version control | Identification and management of changes to a document or record. | maintain version control
compliance review | Assessment against applicable requirements by responsible personnel. | request compliance review
publication hold | A restriction preventing release until specified conditions are met. | maintain the publication hold
review record | Documentation of who reviewed which version and the result. | retain the review record''',
    precision='VoIP describes a technology family; interconnected VoIP is a specific U.S. regulatory category. Emergency-calling obligations and location arrangements depend on the service and applicable rules. Do not turn one product example into a universal statement about all calling services.',
    precision_extra='Backup power is not an unlimited guarantee, and local equipment power is only one possible dependency. State verified limitations in clear, prominent language and obtain the appropriate review. This exercise does not provide a complete customer-notification template.',
    phrases='''Identify the claim | The draft says that 911 always works.
State the conflict | That assurance is not supported by the product record.
Name the dependencies | The service depends on powered equipment and broadband.
Limit the context | We are reviewing a U.S. interconnected-VoIP service.
Ask for current requirements | Which current requirements apply to this specific service?
Request verified wording | Please confirm the service-specific limitations.
Avoid a universal disclaimer | We should not reuse a generic notice without checking applicability.
Keep the consequence clear | The customer needs to understand when calling may be limited or unavailable.
Retain prominence | The limitation should not disappear into fine print.
Separate review from release | A revised draft is not yet approved for publication.
Check the version | Which document version has the reviewer cleared?
Record the decision | Please retain the review outcome with the approved text.
Question the absolute | Can we substantiate always under the stated conditions?
Protect emergency resources | We are not making an emergency call to test this wording.
Assign the review | Product and compliance need to verify the technical facts and applicable language.
Close the release condition | Keep the notice on hold until the responsible review is complete.''',
    notes='''Not supported by | Challenges the evidence behind a claim rather than the writer personally.
This specific service | Prevents an example from becoming a universal regulatory statement.
May be limited or unavailable | Describes a possible service consequence without promising a uniform outcome.
Not yet approved | Distinguishes editing progress from release authorization.
Which version | Makes approval traceable to an exact document.
Until ... complete | States the condition for ending the publication hold.''',
    d='''Which revision approach is appropriate? | Replace the absolute with verified service-specific limitations and obtain review. | Add always in bold type. | Copy a disclaimer from an unrelated service. | Hide the limitation in unreadable text. | The appropriate approach preserves verified facts, relevance, readability, and the required review.
Which statement should be challenged? | Backup power means emergency calling can never fail. | Equipment power is a dependency to verify. | The draft needs service-specific review. | The applicable service category matters. | Backup power alone does not establish an unconditional guarantee across all equipment and network conditions.
What does an approved wording record need? | The exact version and documented review outcome | Only a general statement that someone saw a draft | An unrelated service's old brochure | A claim that legal review is never needed | Version-specific records distinguish actual authorization from an informal or unrelated review.
What does this scenario authorize? | Review of customer-notice language, not an emergency test call | An uncoordinated call to 911 | Publication before review | A universal promise for every VoIP service | The exercise concerns communication review and explicitly excludes using emergency calling as a test.''',
    dialogue='''Celia | The draft is meant to reassure customers. It says 911 always works, even without power or broadband. I am worried that the sentence goes too far.
Marcus | It is an [[absolute assurance::Absolute assurance is an unconditional promise unsupported by the documented equipment and broadband dependencies.]] that our product record does not support. We need to stop that version from being published while we verify the relevant service facts.
Celia | The product notes say the customer equipment requires power and the voice service uses a broadband connection. Neither dependency appears in the draft.
Marcus | Then each [[service limitation::Service limitation identifies a condition affecting availability; customers need that condition to understand the service.]] needs to be explained accurately. Reassurance should come from useful information, not from deleting conditions that may affect whether the service works.
Celia | Can I take a standard paragraph from another provider and replace the product name? That would be quicker than starting again.
Marcus | First check [[applicability::Applicability asks whether the requirement and wording fit this particular service, jurisdiction, and operating arrangement.]]. We are dealing with a U.S. interconnected-VoIP service, and the actual product, location arrangements, and current requirements matter. Another service's paragraph may not fit.
Celia | I want the revised notice to be understandable without asking customers to decode technical language.
Marcus | A [[plain-language notice::Plain-language notice makes the facts understandable while preserving the relevant dependencies and consequences.]] can say what customers need to know about possible limitations. Product staff must verify the facts, and the responsible reviewers must check the resulting wording.
Celia | Should we say that a battery solves the problem? Some equipment has backup-power options.
Marcus | Do not infer a guarantee from [[backup power::Backup power is an alternative power source; its existence alone does not guarantee the entire service path remains available.]]. We need verified capabilities and conditions. Power at one device does not automatically establish that every part of the calling path remains available.
Celia | The marketing layout puts the limitation in a small note after the main reassurance. Is that acceptable for this notice?
Marcus | We need to assess [[prominence::Prominence concerns whether customers notice the limitation; a contradictory headline can undermine the notice.]] as well as wording. A clear sentence loses value if the layout makes it easy to miss or the headline contradicts it.
Celia | I will remove the always statement, list the questions for product, and send the replacement draft through the review process.
Marcus | Keep the [[publication hold::Publication hold prevents the unreviewed notice from being released while technical facts and applicable requirements are checked.]] in place. A better draft is progress, but it is not the same thing as a document cleared for customer release.
Celia | We have two versions circulating. One has the old headline and the other has my changes. That could become confusing.
Marcus | Use [[version control::Version control identifies the reviewed document and prevents an obsolete draft from being mistaken for approved text.]] and retire the old release copy from the active workflow. The review should point to an exact version, not a vague reference to the latest draft.
Celia | I will ask product to verify the limitations and compliance to identify the current requirements, including the relevant customer-notification process.
Marcus | Yes. Retain the [[review record::Review record documents the version, responsible reviewers, and outcome, preserving evidence of what was actually checked and approved.]]. Do not describe our edited paragraph as a complete compliance solution before those checks and any associated process requirements are addressed.
Celia | And we are reviewing language, not asking staff to call emergency services to see what happens.
Marcus | Correct. Once the responsible process is complete, use the [[approved wording::Approved wording is language authorized for the identified service and version after the required review, not merely a plausible draft.]] for this service. Keep the customer consequence clear and do not restore an unsupported promise for a more reassuring tone.''',
    transfer_title='Track a notice through review',
    transfer_setup='Draft N8 says a voice service never fails. Product records identify a power dependency. The local release process requires product and compliance approval. Neither team has approved N8.',
    transfer='''Editor: "The unsupported absolute is ___." | never fails | Never fails promises an unconditional result that the supplied product facts do not establish.
Reviewer: "The identified technical condition is a ___." | power dependency | The product record explicitly identifies dependence on power as a condition to explain.
Editor: "The required reviewers are ___." | product and compliance | Both teams are named in the local release process and neither has approved the draft.
Reviewer: "The release status is ___." | not approved | The stated approvals are absent, so revision work alone cannot authorize release.''',
))

BOOK['units'].append(unit(
    title='Customer Churn and Service Recovery',
    scene='A retention conversation without a false guarantee',
    skill='Acknowledge repeated disruption, offer accountable follow-up, and distinguish service recovery from unsupported retention promises.',
    brief='Business customer Leila reports three broadband interruptions this week and is considering cancellation. The service is currently working, but the incident records do not yet establish a single shared cause. Account specialist Mateo can coordinate a technical review and provide a named update at 16:00 Central the next day. A service-credit request may be reviewed under the actual contract and applicable requirements; no amount is approved. Leila wants a guarantee that the problem will never recur. Mateo must respond honestly and preserve access to the cancellation process rather than making support conditional on staying.',
    cast='Leila | Business customer\nMateo | Account specialist',
    culture=('Acknowledge the cost without promising the impossible', 'A customer may need recognition of operational disruption before hearing the technical explanation. Name the repeated impact, then offer specific ownership and timing. Avoid using a sympathetic tone to smuggle in a promise about cause, compensation, or future reliability.'),
    a='''What has Leila reported? | Three broadband interruptions this week | Three proven failures of the same component | Continuous service loss at the moment | An approved credit amount | Leila reports three interruptions, while the records have not established a shared technical cause.
What can Mateo commit to? | A coordinated review and an update at 16:00 Central the next day | A guarantee that interruption will never recur | An already approved credit | Automatic resolution before the update | Mateo can own the review and communication, but no permanent repair or compensation result is established.
What should happen if Leila wants to cancel? | Provide the applicable cancellation route without withholding support. | Require her to withdraw the request before receiving help. | Claim cancellation is impossible without checking terms. | Promise a credit only if she stops asking questions. | The brief requires preserving access to the actual cancellation process rather than using support as leverage.''',
    vocabulary='''churn | Customer loss over a defined period or the process of leaving a service. | analyze customer churn
retention | Efforts to maintain an ongoing customer relationship. | handle a retention conversation
service recovery | Actions taken to address a poor service experience. | coordinate service recovery
repeat incident | A further incident involving a previously affected customer or service. | review repeat incidents
recurrence | The return of a problem after an earlier occurrence. | investigate recurrence
common cause | A cause shared by multiple events. | establish a common cause
impact statement | A concise account of the customer's operational consequences. | record the impact statement
case owner | The person accountable for coordinating a case. | name the case owner
follow-up commitment | A specific promise about a later action or contact. | record the follow-up commitment
service credit | A contract-related adjustment for eligible service performance issues. | review a service-credit request
goodwill adjustment | A discretionary commercial adjustment offered under applicable authority. | request a goodwill adjustment
eligibility | Whether the conditions for a process or benefit are met. | assess credit eligibility
SLA | Service-level agreement; defined service commitments and associated terms. | review the SLA
availability | The extent to which a service is usable during a defined measurement period. | measure service availability
downtime | Time during which a defined service is unavailable. | reconcile downtime records
exclusion | A circumstance left outside a specified contractual provision. | check the exclusions
remediation plan | A planned set of actions to address an identified problem. | confirm the remediation plan
cancellation request | A customer's request to end a service. | record the cancellation request
notice period | The time required between a notice and its effective action under applicable terms. | verify the notice period
termination charge | A charge that may apply when ending a contract under specified conditions. | check the termination charge
complaint escalation | Referral of a complaint to a further review level. | explain the complaint escalation route
relationship risk | The likelihood or consequence of damage to an ongoing customer relationship. | assess relationship risk
service history | The record of service events and interactions over time. | review the service history
reliability claim | A statement about a service's dependable operation. | substantiate a reliability claim''',
    precision='Three interruptions establish a repeated customer experience, not necessarily one recurring technical fault. Say the records are being compared until a common cause is supported. Service currently working does not erase earlier disruption or establish that recurrence is impossible.',
    precision_extra='A service credit and a goodwill adjustment can follow different rules and approval routes. Record the request accurately without promising eligibility or an amount. Explain the actual cancellation and complaint processes without making support conditional on retention.',
    phrases='''Acknowledge repetition | Three interruptions in one week have disrupted your team.
Recognize the consequence | I understand why you are questioning the service.
Separate present status | The connection is working now, but that does not resolve your concern.
Avoid a common-cause assumption | We have not yet established that all three incidents share one cause.
Decline the guarantee honestly | I cannot promise that an interruption will never happen again.
Offer ownership | I will coordinate the review and remain your contact.
Make the update specific | I will update you tomorrow at 16:00 Central.
Preserve the distinction | That is a progress update, not a guaranteed resolution time.
Capture the credit request | I will submit the service-credit request for review.
Qualify the outcome | Eligibility and any amount remain unconfirmed.
Separate commercial routes | A goodwill adjustment is not the same as an SLA credit.
Respect the customer's choice | I can explain the cancellation route while the review continues.
Avoid a condition | You do not need to withdraw the complaint to receive support.
Ask for evidence | Let us compare the incident times with the service history.
Explain escalation | I will provide the applicable complaint-review route.
Close with accountability | You will receive the review status, open questions, and next actions at the agreed time.''',
    notes='''Working now, but | Acknowledges current recovery without minimizing the prior impact.
Not yet established | Keeps a causal claim open until evidence supports it.
I cannot promise | Gives an honest limit instead of an impossible assurance.
I will coordinate | Offers a concrete action within the speaker's control.
For review | Records a request without granting its outcome.
While ... continues | Allows parallel support and customer-choice processes.''',
    d='''Which response best handles never again? | I cannot guarantee that, but I will coordinate the review and update you tomorrow at 16:00 Central. | I guarantee no future interruption under any conditions. | We cannot help unless you stay. | Three incidents prove one cause, so there is nothing to review. | The response honestly limits the assurance while making a specific, accountable follow-up commitment.
Which credit statement is accurate? | I will submit the request; eligibility and amount remain unconfirmed. | Your full monthly fee is already approved for refund. | Every interruption automatically earns the same credit. | A goodwill adjustment and SLA credit are always identical. | No approved amount or eligibility decision is supplied, so the request must remain under review.
What should the technical summary say? | Three interruptions are reported; a shared cause is not yet established. | The same router caused all three incidents. | Current operation proves the previous reports were false. | Every future interruption is impossible. | The summary distinguishes repeated impact from an unverified common-cause explanation.
How should cancellation be handled? | Explain the applicable route while continuing the review. | Withhold the route until the customer withdraws the complaint. | Invent a notice period to discourage departure. | Make all technical support conditional on retention. | The customer should receive accurate process information without support being used as leverage.''',
    dialogue='''Leila | This is the third interruption this week. Our team has had to rearrange customer calls, and I am considering moving the service elsewhere.
Mateo | I understand the [[service recovery::Service recovery addresses the poor experience through concrete follow-up, not just an attempt to retain the account.]] needs to be more than an apology. Three interruptions have affected your work, even though the connection is operating at the moment.
Leila | The last person said it was fixed. Why should I trust another explanation if the same thing keeps happening?
Mateo | We need to compare the [[service history::Service history supplies the incident and interaction record needed to compare events before claiming they share the same cause.]] before calling it the same technical fault. The repeated impact is clear, but the records do not yet establish one common cause.
Leila | I need someone to own this instead of asking me to repeat the story each time I contact support.
Mateo | I will be the [[case owner::Case owner identifies the person coordinating the review and communication, giving the customer a clear point of accountability.]] for the coordinated review. I will link the three incident records and make sure the technical team sees the times and the effect on your business.
Leila | Can you guarantee that it will never happen again? That is the assurance I need before deciding to stay.
Mateo | I cannot make that [[reliability claim::Reliability claim concerns dependable service; the current evidence cannot support an unconditional no-recurrence guarantee.]]. I can promise a defined review and communication, but it would be misleading to guarantee that no interruption could ever occur.
Leila | Then tell me exactly when I will hear from you and what that contact will contain.
Mateo | My [[follow-up commitment::Follow-up commitment specifies a controlled action and time, not a guaranteed repair deadline.]] is tomorrow at 16:00 Central. I will provide the review status, any verified findings, the questions still open, and the next actions.
Leila | We have lost time dealing with this. I also want the charges reviewed, not just the technical records.
Mateo | I will submit a [[service credit::Service credit is a possible contract-related adjustment that requires review; the conversation does not establish eligibility or an approved amount.]] request under the actual agreement and applicable requirements. I cannot confirm eligibility or an amount before that review has taken place.
Leila | Someone mentioned a goodwill payment. Is that the same thing as a credit under the service agreement?
Mateo | A [[goodwill adjustment::Goodwill adjustment is a discretionary commercial route, which may have different conditions and authority from an SLA-related credit.]] can follow a different approval route. I will keep the requests distinct so that we do not imply one decision automatically resolves the other.
Leila | I still want the cancellation information. I do not want to be told I must stay before anyone investigates.
Mateo | I will provide the applicable [[cancellation request::Cancellation request concerns ending service; access to that process must not depend on withdrawing the complaint.]] process while the review continues. You do not have to withdraw the complaint to receive support, and I will not invent terms to discourage your decision.
Leila | That is clearer. Please do not send a message saying the root cause is confirmed unless the technical team can support it.
Mateo | Agreed. We will describe a [[common cause::Common cause means an explanation shared by the incidents; repeated customer impact alone does not establish that technical relationship.]] only if the evidence connects the events. If the review is still incomplete at the update time, I will say that and explain what remains.
Leila | I will expect your update tomorrow at four Central, with the technical status and the separate credit-review status.
Mateo | Yes, and I will include the [[complaint escalation::Complaint escalation provides a further review route for unresolved concerns, distinct from technical work, compensation review, and cancellation.]] route if you want that review. My update commitment stands whether you decide to retain the service or proceed with cancellation.''',
    transfer_title='State a bounded recovery commitment',
    transfer_setup='Customer Nera reports two interruptions. Agent Sol owns the review and promises an update on Tuesday at 11:00 Mountain. The shared cause and any service credit remain undecided.',
    transfer='''Agent: "The reported number of interruptions is ___." | two | The record supplies two incidents, without establishing that they share a cause.
Customer: "The named review owner is ___." | Sol | Sol is the agent explicitly assigned responsibility for coordinating this review.
Agent: "The next update is ___." | Tuesday at 11:00 Mountain | The commitment specifies a day, time, and time zone for communication.
Customer: "The credit outcome remains ___." | undecided | No eligibility or amount decision has been made for the service-credit request.''',
))


BOOK['units'].append(unit(
    title='Vendor and Equipment Lifecycle',
    scene='The cheaper purchase leaves a two-year support gap',
    skill='Compare procurement options across a common planning horizon and explain the limits of a headline-price comparison.',
    brief='A team plans to operate new network equipment through 31 December 2030. Fictional Model A costs $40,000 and its published last date of support is 31 December 2028. Model B costs $50,000 and support runs through 31 December 2031. The quotations contain no migration, maintenance, training, or disposal estimates. Procurement lead Zara favors A because it saves $10,000 at purchase. Network planner Noah must explain A\'s 24-month support gap during 2029-2030, while making clear that B\'s longer support horizon does not by itself establish the lower total cost or prove every required feature is suitable.',
    cast='Zara | Procurement lead\nNoah | Network lifecycle planner',
    culture=('Compare the decision, not just the price', 'A procurement colleague may be correctly reporting a purchase saving while omitting a later exposure. Acknowledge the saving, then compare both options over the same operating period. Avoid replacing one incomplete argument with an equally unsupported claim that the more expensive option must be better.'),
    a='''What is Model A's purchase-price advantage? | $10,000 | $24,000 | $50,000 | No difference | Fifty thousand minus forty thousand gives a ten-thousand-dollar initial price difference.
How long is A's support gap within the plan? | 24 months during 2029-2030 | 12 months during 2031 | No gap | 60 months during 2026-2030 | Support ends before 2029, while planned operation continues through both 2029 and 2030.
What remains unknown? | The complete total cost of either option | A's quoted purchase price | B's published support end date | The planned operating end date | Migration, maintenance, training, and disposal costs have not been supplied for either option.''',
    vocabulary='''equipment lifecycle | The sequence from acquisition through operation and retirement. | plan the equipment lifecycle
end-of-sale | The milestone after which a product is no longer sold through the specified channel. | check the end-of-sale notice
end-of-life | A vendor-defined lifecycle phase with associated milestone dates. | review the end-of-life announcement
LDOS | Last date of support; the final support milestone specified by the vendor. | verify the LDOS
support horizon | The period through which the applicable support remains available. | compare support horizons
support gap | A period of intended operation beyond available applicable support. | quantify the support gap
planning horizon | The period covered by the decision or operating plan. | align the planning horizon
purchase price | The initial amount paid to acquire an item. | compare purchase prices
TCO | Total cost of ownership across a defined scope and time period. | estimate TCO
maintenance cost | The cost of keeping equipment in its intended operating condition. | estimate maintenance costs
migration cost | The cost of moving from one system or arrangement to another. | scope migration costs
training cost | The cost of preparing staff to use or support a system. | include training costs
disposal cost | The cost of retiring, removing, or disposing of equipment appropriately. | estimate disposal costs
residual value | Estimated value remaining at the end of a defined period. | assess residual value
support entitlement | The specific support rights provided by applicable terms. | verify support entitlement
renewal | Extension or replacement of a contract under agreed terms. | review renewal conditions
security update | A software change addressing security issues. | verify security-update availability
firmware | Software embedded in or closely associated with a device. | review firmware support
spares strategy | A plan for obtaining and holding replacement components. | establish a spares strategy
interoperability | The ability of systems or components to work together as required. | test interoperability
technical fit | How well a product meets the stated technical requirements. | assess technical fit
exit plan | A plan for leaving a system or supplier arrangement. | prepare an exit plan
risk acceptance | An authorized decision to take a defined risk under the organization's process. | document risk acceptance
decision record | Documentation of a choice, its evidence, assumptions, and approval. | maintain the decision record''',
    precision='End-of-sale and last date of support are different milestones. A product may remain supported after sales end, or continue operating after support ends. Continued operation does not demonstrate support entitlement, security-update availability, or an acceptable risk decision.',
    precision_extra='A $10,000 purchase saving is not a $10,000 total-cost saving unless the remaining cost comparison supports it. Use the same planning horizon and scope for both options. A contract renewal should not be assumed to extend a published hardware-support boundary.',
    phrases='''Acknowledge the saving | Model A is ten thousand dollars cheaper to purchase.
Align the horizon | Our operating plan runs through 31 December 2030.
State the support boundary | Model A's last date of support is 31 December 2028.
Quantify the gap | That leaves twenty-four months beyond support within our plan.
Separate milestones | End-of-sale is not the same as last date of support.
Avoid a cost shortcut | Purchase price alone does not establish total cost.
List missing costs | We still need migration, maintenance, training, and disposal estimates.
Qualify the alternative | Model B covers the stated support horizon, but technical fit still needs checking.
Check the actual terms | What support entitlement does this quotation include?
Challenge an assumption | Do we have written confirmation that renewal changes the support boundary?
Avoid an operating inference | Equipment still running is not the same as equipment still supported.
Ask about the transition | What would a supported replacement require before the deadline?
Keep risks visible | The support gap needs a documented response or authorized risk decision.
Separate price from suitability | A higher price does not prove that every requirement is met.
Request a comparable estimate | Please cost both options over the same period.
Close the decision record | Record the dates, costs, missing evidence, and approving owner together.''',
    notes='''Cheaper to purchase | Restricts the saving claim to the known initial cost.
Within our plan | Connects the support gap to the decision's actual time horizon.
Still need | Identifies missing evidence instead of filling it with assumptions.
Does not establish | Blocks a conclusion stronger than the supplied facts.
Written confirmation | Requests traceable evidence for an important contractual claim.
Same period | Makes the cost comparison fair and interpretable.''',
    d='''Which financial claim is supported? | A costs $10,000 less to purchase; total-cost savings are not established. | A has a proven $10,000 lower total cost. | B is automatically the cheapest over its lifetime. | Support dates have no relevance to the plan. | The quotation establishes the initial price difference but omits several lifecycle costs.
Which statement describes the gap correctly? | A is beyond its stated support date for all of 2029 and 2030. | A is supported throughout the plan. | B loses support before the plan ends. | A has only one unsupported month. | A's support ends on 31 December 2028, leaving the next two planned operating years uncovered.
What should be checked before relying on renewal? | The applicable product notice and written support terms | Only whether a purchase order can be raised | Whether the equipment still powers on | A salesperson's vague statement without terms | Renewal cannot simply be assumed to override the specified product support boundary.
What remains necessary for Model B? | Technical-fit and full-cost assessment | No further assessment because it costs more | A claim that support dates prove performance | Automatic purchase without approval | B's longer support horizon addresses one comparison point but does not establish suitability or complete cost.''',
    dialogue='''Zara | Model A is forty thousand dollars and Model B is fifty thousand. I would like to take the saving unless there is a concrete reason not to.
Noah | The [[purchase price::Purchase price is the known initial acquisition cost, so the ten-thousand-dollar advantage is valid at that stage of the comparison.]] difference is real. Before deciding, we should compare the support dates against our plan to operate the equipment through the end of 2030.
Zara | A's notice says support ends on 31 December 2028. The equipment should still be able to run after that, though.
Noah | Running and supported are different. The [[LDOS::LDOS is the last date of support stated by the vendor; continued operation does not extend that support milestone.]] tells us the support boundary, not the date the equipment necessarily stops functioning. Our plan extends two years beyond that boundary for A.
Zara | So you are identifying the whole of 2029 and 2030, rather than a short gap at the end of the project.
Noah | Yes, a twenty-four-month [[support gap::Support gap is the period of intended operation after applicable support ends; here both 2029 and 2030 fall inside the operating plan.]] within the current plan. We need a response to that gap, whether it involves a supported replacement or an authorized risk decision.
Zara | Could we simply renew the support contract in 2028 and keep the same equipment for the remaining two years?
Noah | We need to verify the [[support entitlement::Support entitlement defines the actual rights under the applicable terms, not an assumed consequence of renewal.]]. Do not assume renewal extends a published hardware-support boundary. We need the applicable notice and written terms before relying on that option.
Zara | Model B's support date is 31 December 2031, so it covers the operating period we are discussing.
Noah | Its [[support horizon::Support horizon describes the period of available applicable support; B's stated date extends beyond the end of the current operating plan.]] does cover that period. That is a useful advantage, but it does not prove B meets every technical requirement or has the lowest complete cost.
Zara | I do not want the comparison to become an automatic recommendation for the more expensive product.
Noah | Nor do I. We need [[TCO::TCO means total cost of ownership across a defined scope and period, including relevant costs beyond the initial purchase.]] over the same period for both. The quotations do not yet include migration, maintenance, training, or disposal, so a total-cost conclusion would be premature.
Zara | If A requires replacement before support ends, that transition could use some of the initial saving.
Noah | Exactly, but we must estimate the [[migration cost::Migration cost covers moving to a replacement arrangement; its amount must be estimated, not assumed.]] rather than invent it. The amount, timing, staff effort, and service implications need a scoped comparison.
Zara | We should also check whether both models work with the equipment and management tools we already use.
Noah | That is the [[interoperability::Interoperability asks whether the equipment works with required existing systems; a support date does not establish this.]] assessment. A support date and a price do not answer whether the product fits the required environment or needs additional changes.
Zara | I will ask for comparable cost estimates and confirmation of the support terms. How should I describe the unresolved risk for A?
Noah | State the twenty-four-month gap and the missing [[exit plan::Exit plan describes leaving or replacing the equipment arrangement before unsupported operation becomes necessary.]]. Avoid labeling the saving as a complete business benefit until the transition or risk response is costed and reviewed.
Zara | Then the decision is not simply forty versus fifty thousand. It includes support coverage, technical suitability, and the costs we have not obtained.
Noah | Correct. Put those facts and open assumptions in the [[decision record::Decision record preserves the comparison, evidence, assumptions, and approval so the final choice can be understood and revisited.]]. We can make a defensible recommendation once the comparison is complete, without pretending either price alone settles it.''',
    transfer_title='Compare another support horizon',
    transfer_setup='A plan runs through 31 December 2032. Model C costs $24,000 with support ending 31 December 2031. Model D costs $29,000 with support through 2033. Other lifecycle costs are unknown.',
    transfer='''Buyer: "Model C's initial price advantage is ___." | $5,000 | Twenty-nine thousand minus twenty-four thousand produces a five-thousand-dollar purchase difference.
Planner: "C's support gap within the plan is ___." | 12 months | Support ends before 2032, leaving that full planned operating year beyond the support boundary.
Buyer: "The model covering the stated support horizon is ___." | Model D | Model D remains supported through 2033, which extends beyond the plan ending in 2032.
Planner: "The complete total-cost comparison is ___." | not established | Other lifecycle costs are unknown, so purchase prices do not establish the complete cost comparison.''',
))
