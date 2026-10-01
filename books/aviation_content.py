"""Original learner-book content for aviation workplace communication."""
from books.authoring import unit

BOOK = dict(
    slug='aviation',
    title='Aviation English',
    cover_label='ENGLISH FOR AVIATION OPERATIONS',
    cover_title='Aviation',
    cover_size=36,
    tagline='State the status. Close the loop. Preserve the boundary.',
    audience='For ground operations, maintenance coordination, airport services, and airline support teams.',
    map_intro='Eight aviation workplace exchanges: raise a hazard concern, qualify an operations plan, clarify a maintenance deferral, correct passenger updates, accept a turnaround handover, protect access, report an occurrence, and verify audit evidence.',
    notes_title='Precision matters before confidence',
    notes_intro='Aviation teams need language that separates observation, expectation, and authorization. Speak directly when an action needs to stop, preserve uncertainty when facts are incomplete, and confirm who has accepted the next task.',
    field_notes=[
        ('Name the action and the concern', 'In a safety escalation, indirect hints can conceal the urgency. Use the applicable local procedure, identify the affected activity, and report what you observed without inventing a diagnosis.', '"The task remains stopped under the local process; the reported condition still needs assessment."'),
        ('Attach status to each item', 'A provisional aircraft assignment and an unresolved crew question are not a confirmed operating plan. Keep the time basis and source visible as information changes.', '"Aircraft assignment is provisional; crew confirmation is pending as of 10:10 UTC."'),
        ('Close the communication loop', 'Sending a handover is not the same as someone accepting it. Name the receiving person, confirm the task and current status, and distinguish acceptance from completion.', '"Elin has accepted the catering handover; delivery completion is still pending."'),
        ('Report facts before conclusions', 'A time sequence, a reported sound, and observed damage do not by themselves prove a cause. Preserve the source of each statement and leave causal findings to the appropriate review.', '"I observed the damage at 09:42; I did not witness the contact that caused it."')],
    scope_note='All cases and local processes are fictional. This is a language book, not flight, dispatch, maintenance, security, or emergency training. It does not teach operational radio phraseology or authorize aircraft release. Follow current approved manuals, qualified personnel, and applicable authority requirements.',
    sources=[
        dict(title='Federal Aviation Administration. Safety Management System: Components.', url='https://www.faa.gov/about/initiatives/sms/explained/components', note='Background on safety reporting, communication, responsibility, and assurance. The ground-operation tasks and local stop-work arrangements are original fictional cases.', checked='30 September 2026'),
        dict(title="Federal Aviation Administration. AC 120-125: Development and Use of an Operator's MEL, NEF Program, and CDL.", url='https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_120-125.pdf', note='U.S. terminology background for minimum equipment lists and conditional deferrals. No exercise determines whether an actual defect may be deferred or supplies an operational release checklist.', checked='30 September 2026'),
        dict(title='NASA Aviation Safety Reporting System. ASRS Database Online.', url='https://asrs.arc.nasa.gov/search/database.html', note='Background on aviation reporting and the distinction between submitted accounts and verified findings. These dialogues are original fiction, not adapted ASRS reports or reporting instructions.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Safety Culture and Stop-Work Authority',
    scene='A concern must remain visible under schedule pressure',
    skill='Use a direct stop-work message, describe an observation, and preserve the authorized restart boundary.',
    brief='At 08:40 local time, ramp agent Dana observes an unidentified wet patch beside ground equipment at Stand 6. Dana invokes the fictional site\'s local stop-work process for the affected task and informs supervisor Malik. The equipment team has not assessed the patch or its source. Under this local process, the affected task stays stopped until the designated supervisor completes the required assessment and authorizes restart. Dana is not authorized to handle the substance or repair equipment. A colleague suggests continuing because the turnaround is behind schedule. No injury or equipment fault has been established.',
    cast='Dana | Ramp agent\nMalik | Ground-operations supervisor',
    culture=('Directness can be professional care', 'A clear stop-work statement may sound abrupt to someone accustomed to soft requests. In the supplied case, the action boundary needs to be unmistakable. Explain the observation and use the local escalation route; do not weaken the message to protect a senior colleague from mild discomfort.'),
    a='''What did Dana directly observe? | An unidentified wet patch beside equipment | A proved hydraulic failure | A confirmed injury | A completed repair | The brief establishes a visible condition but not its substance, source, or cause.
What is the affected task's current status? | Stopped under the local process | Automatically restarted | Completed without concern | Cleared because the flight is late | The local stop-work process remains active until the required assessment and authorization.
What does schedule pressure change about restart authority? | Nothing; the required authorization is still needed. | Any colleague can waive it. | A late turnaround proves the patch is harmless. | The reporter must repair the equipment. | A deadline does not replace the fictional site's assessment and restart requirements.''',
    vocabulary='''ramp | The airport area used for aircraft servicing and related ground activity. | report a ramp concern
stand | A designated aircraft parking position. | identify the affected stand
ground support equipment (GSE) | Equipment used to support aircraft ground operations. | identify ground support equipment
hazard | A condition or object with potential to cause harm. | report a potential hazard
safety risk | The assessed likelihood and severity of harm from a hazard. | assess safety risk
stop-work authority | Authority under the relevant process to halt an unsafe or uncertain task. | invoke stop-work authority
affected task | The specific activity subject to the concern or restriction. | identify the affected task
escalation route | The defined path for raising a concern to the responsible people. | follow the escalation route
restart authorization | Permission to resume after the required conditions are satisfied. | obtain restart authorization
safety management system (SMS) | An organized approach to managing safety risks and controls. | support the safety management system
hazard report | A record communicating a potentially harmful condition. | submit a hazard report
risk control | A measure intended to reduce or manage risk. | verify a risk control
safety assurance | Checking whether safety arrangements remain effective. | support safety assurance
safety promotion | Training and communication that support safe working practices. | strengthen safety promotion
just culture | An approach balancing fair reporting, learning, and accountability. | support a just culture
authority gradient | The influence of rank differences on communication. | reduce the authority gradient
schedule pressure | Pressure to meet a planned operating time. | recognize schedule pressure
situational awareness | Understanding the relevant conditions and their implications. | maintain situational awareness
unidentified substance | Material whose identity has not been established. | report an unidentified substance
direct observation | Something personally seen or otherwise perceived. | distinguish direct observation
qualified assessment | Evaluation by personnel with the required competence and authority. | request a qualified assessment
hold point | A stage beyond which activity cannot proceed without a required condition. | respect the hold point
closed-loop communication | Communication in which receipt and understanding are confirmed. | use closed-loop communication
residual risk | Risk remaining after the relevant controls are applied. | assess residual risk''',
    precision='Dana can report a wet patch without naming the substance or declaring an equipment failure. The observation warrants the local process, but it does not establish cause, injury, or the correct technical remedy.',
    precision_extra='The task is already stopped in this fictional case. Do not confuse a later written report with the immediate escalation, or acknowledgement with permission to restart. Only the specified authorized process can change the current task status.',
    phrases='''State the action clearly | The affected task is stopped under our local process.
Locate the observation | I saw a wet patch beside the equipment at Stand 6.
Give the observation time | I observed it at 08:40 local time.
Separate observation and cause | I have not identified the substance or its source.
Request qualified review | The equipment team needs to assess the condition.
Avoid an unsafe assumption | We cannot treat it as harmless because the schedule is tight.
Name the restart boundary | Restart requires the designated supervisor's authorization.
Check understanding | Please confirm that the task remains stopped.
Avoid self-assigned repair | I am not authorized to handle the substance or repair the equipment.
Keep the report factual | No injury or equipment fault has been established.
Respond to pressure | The delay does not remove the assessment requirement.
Acknowledge the report | Thank you for raising the concern promptly.
Name the next responsibility | I will coordinate the required assessment.
Keep acknowledgement separate | I have received the report; that is not restart approval.
Preserve the record | Record the time, location, observation, and action taken.
Close the loop | We will communicate any authorized change in status explicitly.''',
    notes='''Stop versus perhaps pause | Do not soften an active safety instruction into an optional suggestion.
Observed | Identifies firsthand information, not a diagnosis.
Unidentified | Keeps a missing fact visible.
Local time | States the clock basis so later records can be compared.
Acknowledged | Means received, not approved for continuation.
Until authorized | Defines the boundary for resuming, not an estimated delay.''',
    d='''Which message best preserves the facts? | Task stopped: unidentified wet patch observed beside equipment at Stand 6, 08:40 local. | Hydraulic failure confirmed, although nobody assessed it. | Everything is safe because no injury is reported. | Continue unless the schedule improves. | The first message gives the observation, location, time, and actual task status without inventing a cause.
Which response to pressure is appropriate? | The task remains stopped until the required assessment and restart authorization. | We can skip review because we are late. | Quietly resume and complete the report later. | Ask the least experienced worker to test the substance. | The local process requires assessment and authorization regardless of schedule pressure.
What does a supervisor's acknowledgement establish? | The concern has been received. | The equipment is repaired. | Restart has been authorized. | The substance has been identified. | Receipt of the report does not establish the technical findings or restart decision.
Which statement about reporting is accurate? | Record the observation and action without assigning an unverified cause. | Invent a fault category to make the form look complete. | Omit the stop because it affected punctuality. | State that every hazard report guarantees immunity from consequences. | Factual reporting preserves evidence; the case provides no universal immunity or confirmed fault.''',
    dialogue='''Dana | The affected task at Stand 6 is stopped under our local process. I saw a wet patch beside the ground equipment at eight forty local time.
Malik | I have received the [[hazard report::The hazard report communicates the observed potentially harmful condition; receiving it does not establish the cause or authorize restart.]]. Thank you for raising it. Keep the task status clear while I coordinate the required assessment. Have you identified the material or its source?
Dana | No. I observed the patch, but I cannot identify the substance. I have not handled it or attempted a repair outside my role.
Malik | That distinction between [[direct observation::Direct observation is what Dana personally saw, as distinct from an inferred substance, equipment fault, or cause.]] and interpretation matters. We should record what you saw and the action taken, without filling the missing information with a guessed fault.
Dana | A colleague says the turnaround is already behind schedule and suggests continuing while the equipment team checks. I need a clear response to that suggestion.
Malik | [[Schedule pressure::Schedule pressure explains the urgency to finish but does not satisfy the assessment or restart requirements.]] does not remove the hold. Under this process, the affected task remains stopped until the assessment is complete and the designated supervisor authorizes restart.
Dana | I will repeat that boundary without making it personal or guessing about the equipment.
Malik | Refer to the [[restart authorization::Restart authorization is the required decision after assessment, not a choice made informally by a colleague under time pressure.]] requirement. Name the task and current status, then direct questions through the responsible supervisor. You do not need to accuse anyone to keep the instruction firm.
Dana | Should I describe the patch as hydraulic fluid in the written record? It is beside equipment, but nobody has confirmed what it is.
Malik | Use [[unidentified substance::Unidentified substance preserves the missing identification instead of labeling the material as a specific fluid without evidence.]] or simply describe the wet patch. Location beside equipment does not establish its source. The qualified team can supply verified findings through the proper record.
Dana | Understood. I will give the stand, observation time, visible condition, and the fact that I invoked the local stop-work process. No injury is established.
Malik | That supports [[situational awareness::Situational awareness depends on accurate relevant conditions and status, not additional details that have not been established.]] without inventing a diagnosis. It also helps the incoming staff understand what remains unresolved, especially if the handover occurs before the assessment is complete.
Dana | A senior colleague might hear my direct statement as disrespectful. I am more used to phrasing concerns as questions, particularly when someone has more experience.
Malik | The [[authority gradient::The authority gradient is the effect of rank differences on speaking up; it should not conceal the active safety boundary.]] should not hide the concern. You can be courteous and explicit: the task is stopped under the local process, and restart authorization is still required.
Dana | I will use that wording. I will also ask the receiving person to repeat the task status so that a brief acknowledgement is not mistaken for agreement to continue.
Malik | That is [[closed-loop communication::Closed-loop communication confirms receipt and understanding, reducing the risk that a safety message is heard but interpreted incorrectly.]]. Check that they understood the affected task and the restart condition. A quick response such as noted is not always enough to show that shared understanding.
Dana | Once the equipment team has assessed the patch, I will wait for the designated supervisor's decision rather than infer permission from people returning to the area.
Malik | Correct. The [[qualified assessment::A qualified assessment supplies the relevant evaluation, but the separate authorized restart decision must still be communicated.]] informs the decision, but it is not an unspoken release. Any authorized change must be communicated explicitly through the local process.
Dana | For now, the affected task remains stopped. The substance and source are unconfirmed, assessment is pending, and nobody has communicated restart authorization.
Malik | That is the correct [[hold point::The hold point is the boundary that remains in place until the specified assessment and authorization requirements are satisfied.]]. I will coordinate the assessment and keep the relevant teams informed. Do not substitute the turnaround target for the required decision.''',
    transfer_title='Report the condition, not a guessed fault',
    transfer_setup='At Stand 9, a worker observes an unidentified patch at 07:20 local. The affected task is stopped under the local process. Assessment and restart authorization are pending.',
    transfer='''Worker: "The observation was at Stand ___." | 9 | Stand nine is the supplied location of the observed condition.
Supervisor: "The time was ___ local." | 07:20 | The brief gives seven twenty on the local clock.
Worker: "The substance remains ___." | unidentified | No assessment has established the material's identity or source.
Supervisor: "The task remains stopped pending the required restart ___." | authorization | The local process requires an authorized decision before resuming.'''))

BOOK['units'].append(unit(
    title='Operations Control and Dispatch Coordination',
    scene='A provisional plan was labeled confirmed',
    skill='Give a timestamped operations summary that preserves separate aircraft and crew statuses.',
    brief='At 10:10 UTC, a coordination snapshot for fictional Flight EL204 lists fleet aircraft A12 as provisional. Crew control has not confirmed the assigned crew\'s status. The planning target is an 11:00 UTC off-block time, not a cleared departure. Planner Nina finds a draft message calling the aircraft, crew, and departure confirmed. Operations coordinator Joel will seek aircraft confirmation, while crew controller Sara owns the crew-status check. Both will provide their next status at 10:25 UTC. These are two tracked planning items, not an exhaustive release checklist; all other approved operating processes still apply.',
    cast='Nina | Operations planner\nJoel | Operations coordinator',
    culture=('One label cannot describe several dependencies', 'A plan can look complete because every field contains text. Separate the status of each dependency before using an overall label. A colleague who asks for the source and timestamp is checking the meaning of confirmed, not refusing to cooperate with the plan.'),
    a='''What is the aircraft assignment's status at 10:10 UTC? | Provisional | Finally confirmed | Canceled | Irrelevant to planning | The snapshot explicitly labels fleet aircraft A12 as a provisional assignment.
What does 11:00 UTC represent? | A planning target for off-block time | An authorized departure | A completed takeoff | The next crew-status update | The brief labels eleven hundred as a planning target, not an operational clearance.
Who owns the crew-status check? | Sara in crew control | Every passenger | Nina's automated draft | The aircraft's fleet identifier | Sara is the named crew controller responsible for that unresolved planning item.''',
    vocabulary='''operations control center (OCC) | The unit coordinating an airline's operational activity. | contact the operations control center
operational control | Responsibility for decisions about initiating, conducting, or ending a flight under applicable rules. | distinguish operational control
dispatch coordination | Communication among the relevant flight-planning and operating functions. | coordinate with dispatch
aircraft assignment | Allocation of a particular aircraft to an operation. | verify the aircraft assignment
fleet identifier | An internal label identifying an aircraft in the fleet. | confirm the fleet identifier
provisional plan | A proposed arrangement that remains subject to confirmation. | label a provisional plan
crew control | The function coordinating crew assignments and related status. | contact crew control
crew status | The verified position of the relevant crew requirements or assignment. | confirm crew status
crew roster | The schedule of assigned crew duties. | check the crew roster
duty period | A defined period of crew duty under applicable rules. | verify the duty period
qualification | A required credential or demonstrated competence for a role. | verify crew qualifications
positioning | Moving crew or aircraft to a required location. | coordinate crew positioning
off-block time | The time an aircraft leaves its parking position. | distinguish off-block time
estimated off-block time (EOBT) | The estimated time the aircraft will leave its parking position. | update the estimated off-block time
target time | A planning objective rather than proof of completion or clearance. | label the target time
UTC | Coordinated Universal Time, a common aviation time reference. | state times in UTC
timestamp | A recorded time attached to information or an event. | preserve the timestamp
status snapshot | A report of known conditions at a particular time. | issue a status snapshot
dependency | A condition or input on which a later action relies. | track an unresolved dependency
operating restriction | A limitation applying to an operation. | communicate operating restrictions
flight release | The applicable authorized release documentation or decision for an operation. | verify flight release status
contingency aircraft | An alternative aircraft considered if the original plan cannot proceed. | assess a contingency aircraft
confirmation source | The responsible origin of a verified status. | identify the confirmation source
planning assumption | A condition treated as a basis for a plan but not yet established. | expose a planning assumption''',
    precision='Aircraft A12 is provisional, crew status is unconfirmed, and 11:00 UTC is a planning target. Keep all three qualifiers in a short update. Replacing them with confirmed changes the operational meaning of the message.',
    precision_extra='The 10:25 UTC check-in is a time for new status information, not a guarantee that both items will be resolved. Aircraft and crew confirmation are not presented as the complete set of conditions for an actual flight release.',
    phrases='''Give the time basis | This is the status as of 10:10 UTC.
Label the aircraft | A12 remains provisionally assigned.
Label the crew item | Crew confirmation is still pending.
Correct the draft | Confirmed is not supported by this snapshot.
Describe the target | The planning target is 11:00 UTC off-block.
Avoid release language | That target is not a departure clearance.
Name the aircraft owner | Joel is checking the aircraft assignment.
Name the crew owner | Sara in crew control owns the crew-status check.
Give the next check-in | Both owners will update at 10:25 UTC.
Keep resolution uncertain | The next update may still show an unresolved item.
Preserve the source | Please include who confirmed each status.
Avoid a stale message | Replace the earlier draft with the timestamped correction.
Separate dependencies | Aircraft confirmation does not confirm the crew.
Keep other requirements visible | All other approved operating processes still apply.
Ask for a readback | Please repeat the target and the two current statuses.
Close the coordination | We will revise the plan when verified information changes.''',
    notes='''Provisional | A proposed assignment, not a completed commitment.
As of | Limits the statement to the recorded information time.
Target | Names an objective, not clearance or actual movement.
UTC | Keep the time basis explicit; do not silently mix local times.
Pending | Makes an unresolved item visible.
Confirmed by | Identifies the responsible source behind a status claim.''',
    d='''Which short update is accurate? | At 10:10 UTC, A12 is provisional, crew is pending, and 11:00 is the off-block target. | Aircraft, crew, and departure are confirmed. | The aircraft has already taken off. | All release requirements are satisfied because a target exists. | The first update preserves the separate statuses and the planning nature of the time.
What does aircraft confirmation alone establish? | The aircraft assignment's status, not crew confirmation | Every operating requirement | The actual off-block time | That crew-control review is unnecessary | One dependency's confirmation does not automatically resolve the others.
Which phrase should not be used for the 11:00 target? | Cleared departure | Planning target | Proposed off-block time | Subject to the required operating decisions | The case provides a target, not an operational authorization to depart.
What should happen at 10:25 if crew status remains unresolved? | Report it as pending with the current timestamp and owner. | Change it to confirmed to avoid another update. | Delete the item from the message. | Claim every check failed. | An update should accurately preserve the remaining uncertainty rather than force closure.''',
    dialogue='''Nina | The draft says aircraft, crew, and departure confirmed. That does not match the ten-ten UTC snapshot. Can we check each item before the message goes out?
Joel | Yes. The [[aircraft assignment::The aircraft assignment is provisional in the supplied snapshot and must not be described as confirmed.]] for A12 is still provisional. I am checking it, but I have not received the confirmation needed to change that status.
Nina | The crew field names a team, which may be why the draft looked complete. Does a name in that field mean crew control has confirmed the status?
Joel | No. [[Crew control::Crew control is the responsible function for the crew-status check; a populated planning field does not replace its confirmation.]] has not confirmed it. Sara owns that check. We should show the unresolved status rather than infer readiness from an assigned name.
Nina | Then the eleven-hundred time also needs a qualifier. Is it our planned off-block time, or has someone authorized a departure at that time?
Joel | It is a [[target time::A target time is the planning objective, not an authorized departure or an actual off-block event.]] for off-block at eleven hundred UTC. It is not a departure clearance. The draft has combined a planning objective with two unfinished confirmations.
Nina | I will keep all three distinctions visible. A shorter update must not remove information that changes its meaning.
Joel | Include the [[timestamp::The timestamp identifies when the reported statuses were known and helps distinguish the correction from an older draft.]] of ten-ten UTC. These statuses may change, and recipients need to know which snapshot they are reading rather than treating every copied message as current.
Nina | Name who is checking each item, or teams may assume someone else will resolve it and send the update.
Joel | I own the aircraft check; Sara owns [[crew status::Crew status is the separate unresolved item assigned to Sara, not something Joel's aircraft confirmation can settle.]]. Both of us will provide a status at ten twenty-five UTC. That is the next check-in, not a promise that both items will be resolved.
Nina | Suppose you confirm A12 at ten twenty, but Sara is still waiting at ten twenty-five. We should report one confirmed item and one pending item, correct?
Joel | Correct. Each [[dependency::A dependency has its own status; resolving one does not automatically resolve another required planning input.]] retains its own status. Do not upgrade the whole plan to confirmed because one favorable answer arrives, or leave the earlier provisional aircraft label unchanged after verification.
Nina | What should we say about release requirements beyond these two items? I do not want readers to treat our brief planning update as the complete operating checklist.
Joel | State that the applicable [[flight release::Flight release involves the relevant authorized operating process and is not established merely by the two planning items discussed here.]] process and all other required checks still apply. This message tracks aircraft and crew coordination; it does not replace authorized operational decisions or approved manuals.
Nina | I will withdraw the old draft so colleagues do not continue forwarding the unsupported confirmation.
Joel | Identify the [[confirmation source::The confirmation source is the responsible person or record supporting a status change, not the existence of a polished draft.]] for each later update. If someone asks why a status changed, we should be able to point to verified information rather than a wording preference.
Nina | There is one more risk: a local station might read eleven hundred on its own clock. Every time in this exchange should retain the same reference.
Joel | Use [[UTC::UTC supplies the common time basis explicitly required in this snapshot, preventing silent substitution of local clock times.]] throughout. Do not silently translate a number while keeping its original label. The recipient should see the same time basis for the snapshot, target, and next check-in.
Nina | The revised message reads: as of ten-ten UTC, A12 provisional, crew confirmation pending, target off-block eleven hundred UTC, next owner updates at ten twenty-five UTC.
Joel | That is a clear [[status snapshot::The status snapshot summarizes the known position at a stated time without turning assumptions into operational confirmation.]]. Send it as the correction, keep the separate owners visible, and revise it when verified information changes. The overall release boundary remains unchanged.''',
    transfer_title='Keep the planning labels attached',
    transfer_setup='At 12:05 UTC, aircraft B7 is provisional and crew confirmation is pending. Target off-block is 13:00 UTC. The next coordination update is 12:20 UTC; no release is established.',
    transfer='''Planner: "B7 is still ___." | provisional | The aircraft assignment has not received the confirmation needed to change that status.
Coordinator: "Crew confirmation remains ___." | pending | The crew item is explicitly unresolved in the supplied snapshot.
Planner: "Thirteen hundred is the off-block ___." | target | The stated time is a planning objective rather than a release.
Coordinator: "The next update is at ___ UTC." | 12:20 | The supplied coordination check-in time is twelve twenty UTC.'''))

BOOK['units'].append(unit(
    title='Maintenance Deferrals and MEL Language',
    scene='A deferral note is missing its basis and status',
    skill='Request the correct maintenance references and distinguish a proposed deferral from an authorized decision.',
    brief='Coordinator Priya receives a note for fictional defect record D17 reading, "Deferred; okay to operate." It gives no approved operator MEL item reference, document revision, applicable conditions, or authorized decision record. Maintenance controller Tomas confirms that D17 is still under review and that no deferral authorization is recorded. D17 is an internal defect identifier, not an MEL reference. The coordinator must correct the status message, request the relevant controlled records through maintenance control, and preserve the unresolved status. The exercise does not specify an aircraft fault or determine whether any item is eligible for deferral.',
    cast='Priya | Maintenance coordinator\nTomas | Maintenance controller',
    culture=('A familiar label is not supporting evidence', 'Colleagues may use deferred casually to mean that someone intends to review an item later. In maintenance communication, status and authority must remain explicit. Request the actual controlled reference without treating the request for evidence as a personal accusation.'),
    a='''What is the verified status of D17? | Under review with no deferral authorization recorded | Authorized for indefinite operation | Repaired and closed | Approved solely because the note says deferred | Tomas confirms the pending review and absence of a recorded authorization.
What is D17? | An internal defect identifier | A verified MEL item reference | A universal repair interval | An aircraft operating clearance | The brief explicitly distinguishes the internal defect record from an MEL reference.
Can the learner determine deferral eligibility from this case? | No; the fault and applicable technical conditions are not supplied. | Yes; every defect can be deferred. | Yes; any coordinator may approve it. | Yes; a short note replaces the approved documents. | The case teaches clarification language and deliberately does not supply an operational eligibility assessment.''',
    vocabulary='''minimum equipment list (MEL) | An operator-specific approved basis for limited operation with specified inoperative items, subject to conditions. | consult the approved MEL
master minimum equipment list (MMEL) | An aircraft-type baseline used in developing an operator's MEL. | distinguish the MMEL
deferral | Authorized postponement of rectification under applicable conditions. | verify a maintenance deferral
proposed deferral | A suggested postponement not yet established as authorized. | label a proposed deferral
defect record | Documentation identifying a reported equipment problem. | trace the defect record
defect identifier | The internal code assigned to a reported problem. | confirm the defect identifier
item reference | The precise document entry relevant to the matter. | verify the item reference
document revision | An identified version of a controlled document. | check the document revision
applicability | Whether a document or condition governs the particular case. | verify applicability
proviso | A specified condition attached to permission or relief. | read the applicable proviso
operating limitation | A boundary governing permitted operation. | preserve operating limitations
repair interval | The applicable time window for rectification. | verify the repair interval
rectification | Action that corrects the reported defect. | record rectification
inoperative | Not functioning as required for the relevant purpose. | describe an inoperative item
maintenance procedure | A specified technical maintenance action or sequence. | refer to the maintenance procedure
operational procedure | A specified operating action or sequence. | refer to the operational procedure
placard | A required notice or label communicating equipment status. | verify placard requirements
technical log | The controlled record of aircraft defects and maintenance status. | reconcile the technical log
maintenance control | The function coordinating maintenance status and related decisions. | contact maintenance control
authorized sign-off | A recorded decision or certification by an appropriately authorized person. | verify authorized sign-off
airworthiness | The status of conformity and condition required for safe operation under applicable rules. | avoid assuming airworthiness
configuration deviation list (CDL) | Approved conditions for operation with specified external parts missing. | distinguish the CDL
nonessential equipment and furnishings (NEF) | A defined category managed under the applicable approved program. | verify NEF applicability
release statement | A communication of the relevant authorized operational or maintenance release status. | verify the release statement''',
    precision='D17 identifies the internal defect; it does not identify an approved MEL item. An MMEL is not interchangeable with an operator\'s approved MEL. A copied heading or familiar acronym cannot supply missing applicability or authorization.',
    precision_extra='Under review, proposed for deferral, authorized deferral, and repaired describe different statuses. Do not infer an interval, condition, or release from this language exercise. Qualified personnel must apply the actual approved documents and operating requirements.',
    phrases='''Quote the unsupported status | The note says deferred, but the authorization is not recorded.
Identify the case | I am checking defect record D17.
Separate identifiers | D17 is our defect identifier, not the MEL item reference.
Request the source | Please provide the applicable controlled reference.
Check the version | Which approved document revision applies?
Preserve conditions | The status must include the applicable conditions.
Avoid a guessed interval | I cannot infer a repair interval from this note.
Name the pending step | Maintenance control is still reviewing the item.
Correct the distribution | Please replace the unsupported okay-to-operate message.
Keep the role boundary | I am requesting clarification, not authorizing a deferral.
Separate repair | An authorized deferral would not mean the defect is repaired.
Separate document types | The MMEL is not the operator's approved MEL.
Ask for the decision record | Who authorized the status, and where is it recorded?
Keep uncertainty visible | No deferral authorization is recorded at present.
Avoid technical improvisation | Use the actual approved procedures and qualified personnel.
Close the handover | Confirm the corrected status in the relevant controlled record.''',
    notes='''Deferred | Use only with its actual status and applicable authority.
Proposed | Signals a request awaiting the relevant decision.
Reference | Must identify the governing entry, not merely an internal ticket.
Revision | Affects which controlled wording applies.
Okay to operate | Too broad without the actual authorized operational basis.
Rectified | Means corrected, not merely postponed under conditions.''',
    d='''Which correction fits the verified information? | D17 remains under review; no deferral authorization is recorded. | D17 is approved for unlimited operation. | D17 is repaired because someone proposed a deferral. | The aircraft is released solely by this coordination note. | The correction matches Tomas's verified status and removes the unsupported operating claim.
Which pair must not be treated as interchangeable? | Internal defect identifier and approved MEL item reference | A reported code and its exact copied spelling | A stated timestamp and the same timestamp | The name D17 and the exact identifier D17 | The internal record code does not supply the relevant approved document entry.
Which request stays within Priya's coordination role? | Please supply the applicable reference, revision, conditions, and authorized status record. | I approve any deferral without checking. | Use whatever interval sounds familiar. | Ignore maintenance control if the schedule is tight. | Priya can request accurate records but cannot replace the qualified authorization process.
What would an authorized deferral establish, in general? | Conditional postponement under the applicable basis, not completed repair | Permanent freedom from operating rules | Proof that every equipment item works | Permission for any unrelated defect | Deferral and rectification are distinct; any permission remains bounded by the applicable conditions.''',
    dialogue='''Priya | The note for D17 says deferred and okay to operate. I cannot find the supporting reference or decision record. What is the verified status?
Tomas | It is still [[under review::Under review is the verified status, distinct from a deferral that has already received the relevant authorization.]]. No deferral authorization is recorded. Please do not repeat the okay-to-operate statement while I clarify the record through maintenance control.
Priya | I will correct the coordination message. The defect number is clear, but I need to avoid presenting that number as the reference for an approved exception.
Tomas | Exactly. D17 is the [[defect identifier::The defect identifier labels the internal record and does not identify the applicable approved MEL entry.]]. It tracks our reported item. It does not identify an entry in the operator's approved minimum equipment list or establish that one applies.
Priya | The colleague who sent the note may have meant that a deferral was being considered. Should the corrected wording preserve that distinction rather than call it approved?
Tomas | Yes. A [[proposed deferral::A proposed deferral is an option awaiting the relevant review and decision, not evidence that postponement is already authorized.]] is not an authorized decision. We should use the current verified status and request the actual basis, rather than infer approval from informal shorthand.
Priya | What information should I request without implying that I can decide the technical question or complete the maintenance review myself?
Tomas | Request the applicable [[item reference::The item reference identifies the relevant controlled document entry, which must be distinguished from the internal defect number.]], document revision, relevant conditions, and recorded authorized status. Those details come through the qualified process. This message does not replace the actual technical records.
Priya | I found a master list title in an older email. Can I attach that as the operator's MEL reference, or would that create another ambiguity?
Tomas | Do not substitute the [[MMEL::The MMEL is an aircraft-type baseline and is not interchangeable with the specific operator's approved MEL.]] for the operator's approved MEL. The document type, revision, and applicability matter. An older title alone cannot settle which controlled requirements govern this item.
Priya | Understood. I also will not add a repair deadline from memory. Nothing in the note tells me which interval applies or when its clock would begin.
Tomas | Correct. The [[repair interval::The repair interval must come from the applicable approved basis; the coordination note provides no authority to invent it.]] must be verified in the applicable record. A familiar interval from another case is not a safe substitute for the conditions governing this one.
Priya | If a deferral is eventually authorized, our update should still not say repaired. The defect and its treatment would remain different parts of the record.
Tomas | Right. [[Rectification::Rectification means correcting the defect, whereas an authorized deferral permits a bounded postponement under the relevant conditions.]] means the defect has been corrected. Deferral concerns permitted postponement under conditions. Keep that distinction visible to everyone who receives the status.
Priya | Who should the next update come from? I want the receiving team to see a verified source rather than another copied sentence without ownership.
Tomas | Use [[maintenance control::Maintenance control is the responsible coordination source in this case, rather than an unsupported forwarded note.]] as the coordination contact here. We will identify the relevant decision record when available. Do not turn a request for that record into a release statement.
Priya | I will withdraw the unsupported message and replace it with D17 under review, authorization not recorded. The request for the controlled reference will remain open.
Tomas | Include the [[document revision::The document revision identifies the controlled version relevant to the eventual reference and prevents an obsolete copy from being treated as current.]] when the reference is verified. That lets the receiving team distinguish the current basis from an old email or an unrelated record.
Priya | For now, I am communicating the uncertainty and asking for evidence. I am not deciding whether the defect is eligible for deferral or whether the aircraft may operate.
Tomas | Correct. The [[authorized sign-off::Authorized sign-off must come from the appropriate qualified process; Priya's coordination correction does not supply it.]] remains a separate requirement in the actual process. Keep the status accurate, preserve the record, and leave technical eligibility and release decisions to authorized personnel.''',
    transfer_title='A ticket number is not approval',
    transfer_setup='Internal defect Q8 is described as deferred in an email. Maintenance control verifies that review is pending and no authorization is recorded. The approved item reference and revision are missing.',
    transfer='''Coordinator: "Q8 is the internal defect ___." | identifier | The code labels the case rather than an approved document entry.
Controller: "The verified status is under ___." | review | The record has not yet reached an authorized deferral decision.
Coordinator: "The controlled document ___ is still missing." | revision | The scenario supplies no verified version of the applicable document.
Controller: "The email does not establish deferral ___." | authorization | Informal wording cannot replace the absent authorized decision record.'''))

BOOK['units'].append(unit(
    title='Irregular Operations and Passenger Communication',
    scene='Passengers have heard two different departure times',
    skill='Correct conflicting information, separate update and departure times, and offer a verified assistance route.',
    brief='At 14:40 local time, passengers for fictional Flight EL618 have heard an earlier 14:30 departure message and seen 15:00 on a display. The latest verified operations message says the departure estimate is not confirmed; its cause has not been authorized for public explanation. Gate supervisor Lena will provide the next passenger update at 15:10 local, even if no new estimate is available. Agent Omar must correct both unsupported times and keep channels consistent. The service desk can review individual connection and rebooking questions, but no replacement seat, refund, or compensation is guaranteed by the supplied facts.',
    cast='Omar | Gate agent\nMs Bell | Delayed passenger',
    culture=('Consistency is more helpful than repeated optimism', 'Passengers make onward plans from the words and times they hear. Acknowledge conflicting messages directly instead of defending each channel. One reliable status, a named update time, and a practical assistance route give the passenger something usable without a new unsupported promise.'),
    a='''What is the latest verified departure estimate? | No departure estimate is confirmed. | 14:30 local | 15:00 local | 15:10 local | The latest verified operations message explicitly leaves the departure estimate unconfirmed.
What will happen at 15:10 local? | The next passenger status update | Guaranteed departure | Automatic rebooking of every passenger | Guaranteed arrival at the destination | Lena commits to an update even if no new departure estimate exists.
What can the service desk do on the supplied facts? | Review individual connection and rebooking questions | Guarantee a replacement seat immediately | Promise every passenger compensation | Override the operational decision | The service desk can assess options, but no particular seat or financial remedy is established.''',
    vocabulary='''irregular operations (IROPS) | Disruptions affecting the normal airline schedule or service. | manage irregular operations
departure estimate | The current expected departure time, subject to its stated status. | verify a departure estimate
delay announcement | A passenger message explaining a service delay. | issue a delay announcement
flight information display | A screen showing flight and gate information. | correct the flight information display
gate supervisor | The person coordinating the gate team's activity. | contact the gate supervisor
passenger update | A communication of the latest verified passenger-facing status. | schedule a passenger update
onward connection | A later service a traveler plans to take. | review an onward connection
connection risk | The possibility that a traveler will miss a later service. | explain connection risk
rebooking option | A possible alternative reservation subject to confirmation. | check rebooking options
seat availability | Whether a place can be confirmed on the relevant service. | verify seat availability
standby | A waiting status without a confirmed seat on the relevant flight. | distinguish standby status
confirmed reservation | A booking accepted for the specified service under its terms. | verify a confirmed reservation
itinerary change | An alteration to the planned travel sequence. | explain an itinerary change
service desk | The point handling individual travel assistance requests. | direct to the service desk
travel document | A document relevant to a passenger's journey or eligibility. | check required travel documents
baggage routing | The planned handling path for checked bags. | verify baggage routing
assistance request | A request for help with a particular passenger need. | record an assistance request
accessibility assistance | Support enabling a passenger with an access need to use the service. | coordinate accessibility assistance
meal voucher | A document authorizing specified food or drink support. | explain a meal voucher
refund | Money returned under the applicable terms or rules. | verify refund status
compensation | A payment or remedy under the relevant policy or legal basis. | distinguish compensation
authorized explanation | Information approved for the relevant public communication. | use the authorized explanation
channel consistency | Agreement among the current messages provided through different routes. | maintain channel consistency
superseded message | An earlier message replaced by newer verified information. | identify a superseded message''',
    precision='Neither 14:30 nor 15:00 is supported by the latest verified update. The 15:10 time concerns a new communication, not departure. State the local time basis and correct the conflicting channels without inventing a cause.',
    precision_extra='A possible rebooking route is not a confirmed replacement seat. Refunds, compensation, and assistance may follow different terms and requirements. This case establishes a review route only, not the passenger\'s legal entitlement or a particular approved remedy.',
    phrases='''Acknowledge the conflict | You have received two different times, and I am sorry for the confusion.
State the latest position | We do not have a confirmed departure estimate.
Correct the earlier announcement | The earlier 14:30 message is no longer reliable.
Correct the display | The 15:00 display does not reflect a confirmed estimate.
Give the next update | We will update you at 15:10 local time.
Separate update from departure | That time is for information, not a promised departure.
Keep the cause bounded | I do not have an authorized explanation to share yet.
Avoid invented reassurance | I cannot guarantee that you will make the connection.
Offer practical assistance | The service desk can review your individual itinerary.
Separate an option from a seat | A rebooking option still needs confirmation.
Protect private details | Let us discuss your booking details at the service desk.
Ask about a specific need | Do you need assistance while we review the options?
Keep remedies accurate | I cannot confirm a refund or compensation from this update.
Maintain all channels | We are correcting the display and the gate message.
Promise communication | You will receive an update even if the estimate remains unconfirmed.
Close with the usable facts | No confirmed departure estimate; next update at 15:10 local.''',
    notes='''Estimate | A forecast, not an actual departure or a guarantee.
Latest verified | Names the information basis that supersedes earlier conflicting messages.
Update at | Attach the time to communication so its purpose remains clear.
Can review | Offers an assessment, not an automatic favorable result.
Confirmed seat | Different from standby or a proposed itinerary.
Cause unknown to the speaker | Do not fill the gap with a plausible operational story.''',
    d='''Which announcement is accurate? | There is no confirmed departure estimate; the next update is at 15:10 local. | Departure is guaranteed at 15:10. | The display proves that 15:00 is final. | Every connection will be protected automatically. | The first announcement gives the verified uncertainty and the actual communication commitment.
Which response handles an onward connection appropriately? | The service desk can review your itinerary and available options. | I guarantee you will make it. | A possible seat means you are already rebooked. | Your connection does not matter. | The supplied assistance route permits individual review without an unsupported outcome guarantee.
What should happen to the conflicting channels? | Correct them to the latest verified status. | Leave both and ask passengers to choose. | Add a third guessed departure time. | Treat the oldest message as permanently authoritative. | Consistent current information prevents passengers from planning around unsupported older messages.
Which statement about the delay's cause is appropriate? | I do not have an authorized explanation to share yet. | It is definitely the crew, although I have no verified information. | It is definitely maintenance because that sounds plausible. | No explanation will ever be provided. | The brief supplies no authorized public cause and does not justify inventing one.''',
    dialogue='''Ms Bell | We were told fourteen thirty, but the screen says fifteen hundred. It is already fourteen forty. Which time should I use for my connection plans?
Omar | I am sorry for those [[conflicting messages::Conflicting messages describe the two inconsistent times the passenger received; neither is supported by the latest verified status.]]. The latest verified information is that we do not have a confirmed departure estimate. I should not ask you to rely on either displayed time.
Ms Bell | The screen looks official, so I assumed fifteen hundred was firm. Does it need correcting?
Omar | Yes. The [[flight information display::The flight information display is one of the channels that must be corrected to match the latest verified operations message.]] does not currently reflect a confirmed estimate. We are aligning it with the gate message so you do not have to choose between inconsistent sources.
Ms Bell | Does anyone know why the flight is delayed? Other passengers are saying it is a crew problem, but somebody else mentioned maintenance.
Omar | I do not have an [[authorized explanation::An authorized explanation is information cleared for this public update; the case provides none about the cause.]] to share about the cause yet. I will not repeat speculation about crew or maintenance as fact. I can give you the verified current status.
Ms Bell | When will we hear something again? We keep watching the display and asking, but the answers change.
Omar | Our gate supervisor, Lena, will give the next [[passenger update::The passenger update is scheduled for fifteen ten local, even if no new departure estimate has been confirmed.]] at fifteen ten local time. That commitment applies even if there is no new departure estimate, so you will not be left interpreting silence.
Ms Bell | Just to check, fifteen ten is when you will speak to us, not when you now expect the aircraft to leave?
Omar | Correct. It is not a [[departure estimate::A departure estimate concerns expected movement; the fifteen-ten communication time must not be mistaken for one.]]. I cannot promise a departure time at present. We will clearly label any verified estimate if operations supplies one later.
Ms Bell | My onward flight leaves this evening. Can you guarantee that I will still make it, or put me on another service now?
Omar | I cannot guarantee the [[onward connection::The onward connection is the later flight whose feasibility requires an individual itinerary review, not a general promise from the gate update.]] from this information. The service desk can review your itinerary and the available options. A proposed replacement would still need its own confirmation.
Ms Bell | I saw another flight online with seats showing. Does that mean I can go directly to its gate and assume my booking has transferred?
Omar | No. [[Seat availability::Seat availability must be verified for a specific rebooking; a public display does not itself transfer or confirm the passenger's reservation.]] on another service does not mean your reservation has changed. Please use the service desk so the actual booking and any related requirements can be checked.
Ms Bell | I also checked a bag. I do not want to agree to a different itinerary without understanding whether the bag arrangement changes.
Omar | Ask the desk to verify [[baggage routing::Baggage routing is a separate practical detail of the itinerary that should be checked rather than assumed from a proposed seat.]] as part of that review. I cannot promise the bag's route from this gate update, but it is a relevant question for the individual arrangement.
Ms Bell | All right. Can the desk also explain whether any refund or compensation applies? I am not asking you to decide that without the details.
Omar | Yes, ask them to review the applicable basis. This update does not confirm [[compensation::Compensation is a separate policy or legal question; the operational update does not establish an approved payment.]] or a refund. I should distinguish that financial review from the current flight status and possible rebooking options.
Ms Bell | I will take the booking details to the desk. Please make sure the next announcement is clear enough that nobody hears another update time as a departure.
Omar | We will maintain [[channel consistency::Channel consistency means the current display and spoken announcements communicate the same verified status and distinguish updates from departure estimates.]]. The usable facts now are no confirmed departure estimate and a passenger update at fifteen ten local. I am sorry for the earlier confusion.''',
    transfer_title='Correct the time without inventing a new one',
    transfer_setup='At 16:20 local, a display says 16:30 departure, but operations has no confirmed estimate. The gate promises an update at 16:45. The service desk can review individual itineraries.',
    transfer='''Passenger: "Is 16:30 a confirmed ___?" | departure estimate | The display is not supported by a verified estimate in this case.
Agent: "No; our next information ___ is at 16:45." | update | The commitment is to communicate, not to depart at that time.
Passenger: "Where can I review my individual ___?" | itinerary | The service desk can assess the passenger's specific travel sequence and options.
Agent: "Please speak with the service ___." | desk | The brief names the service desk as the individual assistance route.'''))

BOOK['units'].append(unit(
    title='Ground Handling and Turnaround Performance',
    scene='A handover was sent, but nobody accepted it',
    skill='Confirm task ownership and report a catering balance without confusing arrival, receipt, and completion.',
    brief='At 13:20 UTC, a fictional turnaround requires 96 catering packs. The receiving record confirms 80 packs, leaving 16 outstanding. A supplier truck has arrived with a note claiming the remaining 16, but receipt and count are not yet verified. The outgoing ground team sent a handover without obtaining a named receiving person\'s acceptance. Coordinator Hassan contacts incoming lead Elin. She can accept responsibility for verifying the balance and reporting status at 13:35 UTC; acceptance does not itself complete the delivery. The 13:45 UTC off-block target remains a planning target. Other required turnaround and release processes are outside this short coordination case.',
    cast='Hassan | Turnaround coordinator\nElin | Incoming ground-services lead',
    culture=('Ownership needs an answer', 'A sent message can create an illusion that responsibility has transferred. Ask the receiving colleague to confirm the task, current balance, and next report. This check is especially valuable when shifts overlap briefly and everyone is working toward the same time target.'),
    a='''How many packs remain unverified in the receiving balance? | 16 | 80 | 96 | 176 | Ninety-six required packs minus eighty confirmed received leaves sixteen outstanding.
What does the truck's arrival establish? | The truck is present, not that receipt and count are verified. | All packs are received. | Every turnaround task is complete. | The aircraft has departed. | Physical arrival and the supplier's note do not establish verified receipt of the remaining packs.
What does Elin's acceptance establish? | Ownership of the verification and status task | Completed delivery | Final flight release | A guaranteed 13:45 departure | Accepting responsibility names the task owner but does not complete the task or authorize departure.''',
    vocabulary='''turnaround | The ground-service period between an aircraft's arrival and next departure. | coordinate the turnaround
ground handler | A person or organization providing aircraft ground services. | contact the ground handler
service handover | Transfer of a service task and its current information. | complete a service handover
receiving lead | The person accepting responsibility at the receiving end. | name the receiving lead
catering uplift | Food and service supplies provided for a flight. | verify the catering uplift
catering pack | A counted package of catering supplies in the stated case. | reconcile catering packs
required quantity | The amount specified as needed. | confirm the required quantity
confirmed receipt | Recorded verification that specified goods were received. | record confirmed receipt
outstanding balance | The amount still needed after verified receipt. | calculate the outstanding balance
delivery note | A supplier document describing a delivery. | check the delivery note
manifest | A list of the goods or people covered by an operation. | reconcile the manifest
truck arrival | The event of the delivery vehicle reaching the site. | record truck arrival
physical count | A check of the actual quantity present or received. | verify the physical count
short delivery | Receipt of less than the required quantity. | report a short delivery
task acceptance | Explicit agreement to take responsibility for an activity. | confirm task acceptance
task completion | Verified finishing of the specified activity. | distinguish task completion
milestone | A defined event used to track progress. | report a turnaround milestone
critical path | The sequence of dependent activities determining the earliest completion. | identify the critical path
service dependency | A required service relationship affecting later work. | track a service dependency
target off-block time | A planning target for leaving the parking position. | protect the target off-block time
readiness status | The verified position of preparation for the next step. | report readiness status
handover gap | Missing information or acceptance during a transfer. | close the handover gap
exception report | A message identifying a departure from the planned condition. | issue an exception report
delay attribution | Assigning a cause or category to a delay using the applicable evidence. | verify delay attribution''',
    precision='96 required minus 80 confirmed received leaves 16 outstanding. The supplier note claims those 16 are on the truck; it does not prove they have been counted and accepted. Keep the receiving balance unchanged until verification.',
    precision_extra='Elin accepts the verification task and the 13:35 status report, not a promise of completed delivery by then. A catering completion would also not establish completion of every other turnaround or release requirement.',
    phrases='''State the current count | We have 80 confirmed against a requirement of 96.
Calculate the remainder | Sixteen packs remain outstanding.
Separate arrival | The truck is here, but receipt is not verified.
Attribute the claim | The delivery note lists the remaining sixteen.
Identify the handover gap | The earlier message has no named acceptance.
Request ownership | Can you accept the balance-verification task?
Confirm the scope | I will verify receipt and count, then report the result.
Set the report time | Please provide status at 13:35 UTC.
Avoid a completion promise | That is a reporting time, not a guarantee of completion.
Preserve the plan label | 13:45 UTC remains the off-block target.
Keep other requirements separate | Catering status is not the whole turnaround status.
Record acceptance | Elin has accepted responsibility for the check.
Report an exception | Any unverified balance remains open.
Avoid premature blame | We have not established the cause of the handover gap.
Close with a readback | Ninety-six required, eighty received, sixteen pending verification.
Update from evidence | Change the receiving balance only after verified receipt.''',
    notes='''Arrived | Describes vehicle presence, not accepted delivery.
Lists | Attributes a quantity to a document rather than a completed count.
Outstanding | The balance not yet confirmed received.
Accepted the task | Distinguish from accepted the goods.
By 13:35 | In this case, the commitment concerns a status report.
Ready | Specify which service or decision the label covers.''',
    d='''Which handover is accurate? | Elin owns verification of the remaining 16; status due at 13:35 UTC. | Truck arrived, so all 96 are received. | Nobody needs to accept a task already emailed. | The flight is released when Elin answers. | The first message names ownership, quantity, and report time without claiming completion.
Which statement about the delivery note is accurate? | It claims a quantity that still needs receipt verification. | It automatically completes the receiving record. | It proves every pack meets every requirement. | It authorizes the aircraft to depart. | A supplier document is information to check, not a substitute for the receiving process.
If 12 additional packs are later verified received, what remains outstanding? | 4 | 12 | 16 | 28 | Eighty plus twelve is ninety-two, leaving four of the required ninety-six.
Which overall conclusion is unsupported even after catering completion? | All flight-release requirements are satisfied. | The catering balance can be updated from verified receipt. | The catering task has reached its recorded completion. | The coordinator can report the verified catering status. | The case covers catering coordination, not the complete turnaround and operational release process.''',
    dialogue='''Hassan | The outgoing team sent the catering handover, but I cannot find a receiving person's acceptance. Before they leave, can we confirm the task and current balance?
Elin | Yes. Give me the [[required quantity::The required quantity is ninety-six packs, the reference against which confirmed receipt and the outstanding balance are calculated.]] and what has actually been received. I do not want to accept a vague instruction that assumes the delivery is already complete.
Hassan | We require ninety-six packs. The receiving record confirms eighty. A truck is here with a note listing the other sixteen, but that receipt has not been verified.
Elin | Then the [[outstanding balance::The outstanding balance remains sixteen because only eighty of the required ninety-six have confirmed receipt.]] is sixteen. The truck's presence does not change the confirmed count. I will keep that distinction when I speak to the receiving team.
Hassan | Someone marked the task nearly done after seeing the vehicle. We need a status that different teams will interpret consistently.
Elin | We can say [[truck arrival::Truck arrival is a verified milestone of vehicle presence, not proof of the remaining goods' receipt or task completion.]] is confirmed while receipt verification remains open. Those are separate milestones. A supplier's arrival is useful information, but it is not the completed receiving step.
Hassan | The supplier note could help the check, provided we do not treat its stated quantity as an independently confirmed count in our own record.
Elin | Correct. I will compare the [[delivery note::The delivery note states the supplier's claimed quantity, which the receiving process still needs to verify.]] with the receiving information through the approved process. Until that verification is recorded, the current confirmed total remains eighty, not ninety-six.
Hassan | Will you own that verification and the next report? The earlier handover went to a group address without explicit acceptance.
Elin | I accept the [[service handover::The service handover transfers the specified verification and reporting responsibility once Elin explicitly accepts it.]] for checking the remaining sixteen and reporting the result. Please record me as the receiving lead so the next shift knows who has the task.
Hassan | I will record that acceptance now. Our next coordination check is thirteen thirty-five UTC, with thirteen forty-five still the planning target for off-block.
Elin | I will give a [[status report::The status report is the commitment due at thirteen thirty-five; it does not guarantee that delivery will be complete by then.]] at thirteen thirty-five UTC. That is a commitment to report the verified position, not a promise that the remaining delivery will be complete by that time.
Hassan | Exactly. If some packs remain unverified, keep the balance visible. We cannot make the record match the plan merely because the target time is approaching.
Elin | I will update [[confirmed receipt::Confirmed receipt changes only when the receiving process verifies additional packs, not when schedule pressure increases.]] from evidence. If all sixteen are verified, the balance becomes zero. If fewer are verified, I will state the remaining amount rather than mark the task complete.
Hassan | And we should not use catering complete as shorthand for the entire aircraft being ready. Other teams still have their own required checks and responsibilities.
Elin | Agreed. [[Task completion::Task completion concerns this specified catering activity only and does not establish completion of all other turnaround or release requirements.]] here is limited to the catering activity. I will not use it as a flight-release statement or as proof that unrelated ground-service work has finished.
Hassan | We should review why the earlier handover had no acceptance, using the messages instead of immediately blaming a department.
Elin | Yes. The [[handover gap::The handover gap is the missing named acceptance; its existence does not by itself prove who caused it or why.]] is established, but its cause is not. Preserve the messages and review the process. Solving the current ownership problem does not settle the later causal question.
Hassan | Let me read back the current arrangement: ninety-six required, eighty confirmed received, sixteen pending verification, Elin responsible, and a status report at thirteen thirty-five UTC.
Elin | That captures my [[task acceptance::Task acceptance means Elin has taken responsibility for verification and reporting, not that the goods are already accepted or the task finished.]]. Keep thirteen forty-five labeled as the off-block target. I will report the verified catering balance and any remaining exception at the agreed check-in.''',
    transfer_title='A partial receipt leaves a visible balance',
    transfer_setup='A service requires 120 packs. The record confirms 100, then verifies 15 more. Lead Jo accepts responsibility for the remaining check and will report at 14:10 UTC.',
    transfer='''Coordinator: "The confirmed total is now ___." | 115 | One hundred original packs plus fifteen verified additional packs equals one hundred fifteen.
Lead: "The outstanding balance is ___." | 5 | The required one hundred twenty minus one hundred fifteen leaves five.
Coordinator: "The named receiving lead is ___." | Jo | The brief assigns acceptance of the remaining check to Jo.
Lead: "My status report is due at ___ UTC." | 14:10 | Fourteen ten is the agreed reporting time, not a guaranteed completion time.'''))

BOOK['units'].append(unit(
    title='Security and Access Control',
    scene='A meeting invitation is not access authorization',
    skill='Refuse an access shortcut professionally and offer the approved verification route without implying automatic entry.',
    brief='Visitor Mr Vale arrives late for a meeting in a restricted airport work area. He shows an email invitation but has not completed the fictional site\'s visitor verification process. He asks employee Anika to admit him using her access and says the host will approve later. Anika is not authorized to bypass verification or provide an unapproved escort. She can keep him at public reception, contact the host through the approved directory, and refer the request to the access desk. Any permitted entry must follow the site\'s actual authorization and escort requirements. No entry permission is established in this case.',
    cast='Anika | Airport employee\nMr Vale | Visitor',
    culture=('A firm boundary can include practical help', 'Urgency, familiarity, and seniority may make a shortcut sound socially reasonable. A professional refusal can acknowledge the late meeting while preserving the access rule. Offer the approved route without accusing the visitor of criminal intent or promising that verification will succeed.'),
    a='''What does the email invitation establish in this case? | A claimed meeting arrangement, not completed access authorization | Automatic restricted-area entry | Permission to borrow employee access | A completed security check | The visitor still has to complete the site's separate verification and authorization process.
What can Anika do now? | Contact the host through the approved directory and refer to the access desk. | Lend her access to the visitor. | Approve her own exception. | Admit the visitor and verify later. | The brief permits the official verification route but not a bypass or unapproved escort.
Where should the visitor remain under the stated process? | Public reception | Inside the restricted area | Anywhere an employee's access opens | An unverified meeting room beyond the boundary | The case explicitly keeps the visitor at public reception while the request is handled.''',
    vocabulary='''restricted area | A location where entry requires specified authorization. | protect a restricted area
access control | Measures determining who may enter or use a location or resource. | follow access control
access authorization | Permission for a person to enter the specified area. | verify access authorization
visitor verification | The approved process for checking a visitor's identity and purpose. | complete visitor verification
identity check | Confirmation that a person is who they claim to be. | conduct an identity check
visitor badge | A credential issued for an authorized visitor under local rules. | verify a visitor badge
access credential | A token or document used to demonstrate permitted access. | protect an access credential
credential sharing | Allowing another person to use an assigned access credential. | prohibit credential sharing
escort authorization | Permission to accompany a visitor under the site's rules. | verify escort authorization
approved escort | A person permitted to accompany a visitor under the relevant conditions. | arrange an approved escort
host confirmation | Verification of the visit through the responsible host. | request host confirmation
approved directory | A trusted source of official contact information. | use the approved directory
public reception | A visitor-contact location outside the restricted area. | wait at public reception
access desk | The function handling access requests and verification. | contact the access desk
visitor register | The record of visits under the local process. | update the visitor register
access scope | The areas and conditions covered by a permission. | confirm access scope
validity period | The time during which a credential or permission applies. | check the validity period
expired credential | A credential whose permitted period has ended. | identify an expired credential
access exception | A departure from the normal rule requiring the relevant authority. | verify an access exception
challenge procedure | The approved response for checking questionable access. | follow the challenge procedure
security escalation | Referral of an access concern through the security process. | use security escalation
urgency claim | A statement that time pressure requires immediate action. | assess an urgency claim
authorization boundary | The limit of what a person or permission allows. | maintain the authorization boundary
unverified visitor | A person whose required visitor checks are incomplete. | refer an unverified visitor''',
    precision='A meeting invitation and host familiarity do not replace the supplied access process. Anika\'s own credential does not establish permission for the visitor, and her employee status does not establish that she may escort him.',
    precision_extra='Host confirmation, identity verification, permission scope, and any escort conditions are distinct checks within the actual site process. This language case provides no shortcut, complete security procedure, or guarantee that entry will be approved.',
    phrases='''Acknowledge urgency | I understand that your meeting is running late.
State the boundary | I cannot admit you before the required verification.
Separate invitation and access | The invitation does not complete the access process.
Protect personal access | I cannot let you use my credential.
Avoid an unapproved escort | I am not authorized to bypass the escort requirements.
Offer a practical route | I can contact the host through our approved directory.
Name the responsible desk | The access desk will handle the verification request.
Give the current location | Please remain at public reception while we contact them.
Avoid accusing intent | This is an authorization requirement, not a judgment about you.
Keep the outcome open | I cannot promise entry before the checks are complete.
Reject retrospective approval | Approval afterward would not satisfy the current entry requirement.
Check the relevant scope | Any permission must cover the required area.
Respect the actual process | We will follow the site's authorization and escort rules.
Keep the host informed | I can tell the host that you are waiting here.
Do not self-authorize | I cannot grant an exception on my own.
Close helpfully | Let us use the approved route to resolve the request.''',
    notes='''Invited versus authorized | A meeting arrangement does not settle restricted-area entry.
My credential | Belongs to its assigned user and does not transfer the user's rights.
Afterward | Too late to satisfy a prior-entry condition in this case.
Can contact | Offers a step without guaranteeing approval.
Not authorized | States a role boundary without blaming the visitor.
Approved route | Refers to the actual site's process, not an improvised workaround.''',
    d='''Which response is both firm and helpful? | I cannot admit you yet; I can contact your host and the access desk from reception. | Use my access and we will check later. | A senior host makes every check unnecessary. | I will grant an exception because you are late. | The first response preserves the boundary and offers the permitted practical next step.
Which statement is unsupported? | Anika may escort anyone because she works here. | The visitor is still unverified. | The access desk can review the request. | The invitation alone does not complete access authorization. | Employee status does not establish escort authority under the supplied site process.
What should Anika use to contact the host? | The approved directory | Only a number the unverified visitor supplies | A guessed personal account | A public comment unrelated to the visit | The case identifies the approved directory as the trusted contact route.
What does a pending access request mean? | Entry is not yet established as authorized. | Entry is automatically approved. | The visitor has been found guilty of a crime. | Every later request must be refused forever. | Pending authorization is a current process status, not a verdict on intent or a permanent refusal.''',
    dialogue='''Mr Vale | I am late for a meeting inside. Here is the email invitation. Could you let me through with you? The host can confirm everything after I arrive.
Anika | I understand the time pressure, but [[access authorization::Access authorization must be established through the site's process before entry; an invitation and urgency do not provide it.]] has not been established. I cannot admit you before the required verification. I can help contact your host from public reception.
Mr Vale | I have visited before, and the host knows me well. Doesn't that count for something?
Anika | We still need [[visitor verification::Visitor verification is the current required process, which prior visits and familiarity do not replace.]] for this visit. The invitation explains the meeting request, but it does not complete the entry process. I will use the approved route to check it.
Mr Vale | Could I borrow your access? I will return it immediately. You can explain that you were helping me reach the meeting.
Anika | I cannot permit [[credential sharing::Credential sharing would let another person use Anika's assigned access, which the supplied process does not authorize.]]. My access applies to me, not automatically to another person. Please remain here while I contact the host and the access desk.
Mr Vale | Then perhaps you can escort me. You are an employee, and I would stay beside you all the way to the room.
Anika | Employee status does not establish [[escort authorization::Escort authorization is a separate permission; Anika is not authorized to provide an unapproved escort simply because she works there.]]. I cannot bypass the site's escort requirements. If an escort is appropriate, the access desk must arrange it through the actual process.
Mr Vale | I can give you the host's mobile number. It will be faster than searching, and they will certainly tell you to let me in.
Anika | I will contact the host through the [[approved directory::The approved directory is the trusted contact source specified in the case, rather than relying solely on details from an unverified visitor.]]. That is our trusted route. Host confirmation is useful, but any entry must also meet the site's authorization and escort requirements.
Mr Vale | All right. Please make clear that I arrived for a real meeting. I do not want the host to think I simply failed to turn up.
Anika | I can tell them you are waiting at [[public reception::Public reception is the permitted waiting location while the access request is verified.]]. That gives the host an accurate update without implying that you have already been admitted or that the access checks are complete.
Mr Vale | Are you refusing to help, or is there an unfinished step? The meeting may finish before we resolve this.
Anika | It is an [[authorization boundary::The authorization boundary limits what Anika may allow; maintaining it does not mean refusing all assistance or judging the visitor's intent.]], not a judgment about your intentions. I can contact the responsible people, but I cannot promise entry or grant an exception myself.
Mr Vale | Could the host approve it afterward if everyone agrees that the delay was unreasonable? That would avoid losing more of the meeting now.
Anika | A later [[access exception::An access exception requires the relevant authority and cannot be assumed retroactively to justify bypassing the current entry requirement.]] cannot be assumed as permission to bypass the current requirement. Let us ask the access desk what approved arrangements are possible before anyone crosses the boundary.
Mr Vale | Understood. I will wait here. Please ask whether the host can meet me in reception or speak with me while the access request is being handled.
Anika | I can pass on that request. The [[access desk::The access desk is the responsible function handling verification and possible permitted arrangements, not a guaranteed approval service.]] will handle the verification, and the host can respond about meeting arrangements. Neither response should be treated as complete until confirmed.
Mr Vale | Thank you. I will not use another person's access or assume that the invitation has completed the checks. Please let me know the verified next step.
Anika | I will. Any approved entry must have the right [[access scope::Access scope identifies the specific areas and conditions covered by permission, rather than treating any approval as unrestricted entry.]] and satisfy the actual site requirements. For now, you remain here and I will contact the responsible people through the approved route.''',
    transfer_title='Keep invitation and permission separate',
    transfer_setup='A visitor has a meeting invitation but incomplete access verification. Employee Jo cannot share credentials or approve an escort. Jo can contact the host through the approved directory and refer to the access desk.',
    transfer='''Visitor: "My invitation does not itself establish access ___." | authorization | The invitation and the required entry permission are separate in this case.
Employee: "I cannot share my ___." | credential | Jo's assigned access cannot be used as permission for the visitor.
Visitor: "Please contact the host through the approved ___." | directory | The supplied trusted contact route is the approved directory.
Employee: "The access ___ will handle the verification request." | desk | The case assigns the verification request to the access desk.'''))

BOOK['units'].append(unit(
    title='Incident Reporting and Investigation',
    scene='An observed dent became an unsupported cause',
    skill='Separate firsthand observation, another person\'s report, and a causal conclusion in an occurrence record.',
    brief='Ground-services employee Rosa observed a dent in the side panel of baggage cart C4 at 09:42 local time. She did not see an impact. Colleague Ivo reports hearing a bang near the cart at approximately 09:39, but did not see contact either. Relevant camera footage has not been reviewed. A draft report says that a tug driver struck C4 and caused the damage; no supplied evidence establishes that claim. Safety reviewer Daniel helps Rosa correct the draft while preserving the original version and the source of each account. Immediate operational controls follow the separate local process; this exchange does not authorize equipment return to use.',
    cast='Rosa | Ground-services employee\nDaniel | Safety reviewer',
    culture=('Neutral does not mean vague', 'A report can be specific about times, locations, equipment, and observations without assigning premature blame. Avoiding an unsupported causal claim protects the investigation; it does not require deleting useful facts or minimizing the seriousness of reported damage.'),
    a='''What did Rosa directly observe? | A dent in cart C4 at 09:42 local | A tug striking the cart | The exact time damage occurred | A completed camera review | Rosa saw the damage at 09:42 but did not witness the contact or its cause.
What is Ivo's account? | He heard a bang at approximately 09:39 without seeing contact. | He saw a named driver strike C4. | He reviewed the footage. | He verified the exact cause. | The brief attributes a reported sound and approximate time to Ivo, not a witnessed impact.
Which claim should be removed as unsupported? | A tug driver struck C4 and caused the damage. | Rosa observed a dent. | Ivo reported a bang. | Camera footage has not been reviewed. | The supplied observations and reported sound do not establish a particular actor or causal contact.''',
    vocabulary='''occurrence report | A record describing an event or condition relevant to safety. | submit an occurrence report
initial report | The first recorded account before the review is complete. | qualify an initial report
firsthand account | Information from a person's own observation. | preserve a firsthand account
witness statement | An attributed account from someone with relevant observations. | record a witness statement
reported sound | An auditory event described by a person. | attribute a reported sound
observation time | When a person noticed a condition. | state the observation time
event time | When the event itself occurred. | distinguish the event time
approximate time | A time given with limited precision. | label an approximate time
chronology | The sequence of relevant events or observations. | establish the chronology
causal claim | A statement that one event produced another. | test a causal claim
contributing factor | A condition that helped produce or shape an event. | assess contributing factors
root cause | An underlying cause identified through the relevant analysis. | avoid premature root-cause claims
evidence source | The origin of information used in a review. | identify the evidence source
corroboration | Independent support for an account or inference. | seek corroboration
camera footage | Recorded video that may provide relevant evidence. | preserve camera footage
review status | The current stage of an examination of evidence. | state the review status
damage description | Factual wording identifying the observed physical condition. | give a damage description
equipment identifier | The code distinguishing the equipment involved. | verify the equipment identifier
baggage cart | A vehicle or trailer used to carry baggage on the ground. | identify the baggage cart
tug | A vehicle used to move other ground equipment or aircraft under the relevant operation. | identify the reported tug
attribution | Stating who supplied a claim or observation. | preserve source attribution
version history | The record of changes to a document over time. | retain version history
factual amendment | A documented correction or addition to the factual record. | make a factual amendment
causation finding | A supported conclusion about what produced the event. | distinguish a causation finding''',
    precision='09:42 is the time Rosa observed the dent, not a verified impact time. Ivo\'s approximately 09:39 sound is a separate reported observation. A three-minute sequence does not identify the contact, actor, or cause.',
    precision_extra='Footage not yet reviewed must not be described as confirming or disproving the draft. Correct the unsupported claim transparently, preserve the original version, and keep sources separate. The report is not equipment-release authorization.',
    phrases='''Start with firsthand information | I observed a dent on the side panel of cart C4.
State the observation time | I noticed it at 09:42 local time.
Avoid claiming an impact | I did not see contact occur.
Attribute the second account | Ivo reports hearing a bang near the cart.
Preserve time uncertainty | He gives the time as approximately 09:39.
Separate observation and event | That is when I saw the damage, not necessarily when it occurred.
Describe the evidence gap | The camera footage has not been reviewed.
Remove the unsupported cause | The supplied evidence does not identify a tug strike.
Keep the equipment precise | The affected cart identifier is C4.
Preserve the original | Retain the earlier draft in the version history.
Record the correction | Add a dated factual amendment explaining the change.
Avoid personal judgment | We should report actions and evidence, not assumed motives.
Leave investigation open | The cause remains under review.
Avoid false exoneration | Removing the accusation does not establish that no contact occurred.
Keep operational authority separate | This report does not clear the equipment for use.
Close the account | Distinguish what I saw, what I was told, and what remains unknown.''',
    notes='''Observed at | Gives the time of noticing, not necessarily the event time.
Reports hearing | Attributes the account and preserves that it is auditory.
Approximately | Retains limited precision; do not silently turn it into an exact timestamp.
Not reviewed | Says nothing about what the footage will show.
Unsupported | Not established by the current evidence, not necessarily disproved.
Amendment | Correct transparently rather than erase the history.''',
    d='''Which sentence is supported? | Rosa observed a dent on C4 at 09:42 local and did not witness contact. | The tug driver definitely caused the dent at 09:42. | Ivo saw a collision. | The camera confirmed an impact. | The first sentence limits the account to Rosa's direct observation and its known boundary.
How should Ivo's time appear? | Approximately 09:39, attributed to Ivo | Exactly 09:39 as a verified impact time | 09:42 because that is easier to align | Omitted because approximate times are useless | The source supplied an approximate sound time, which should retain both attribution and uncertainty.
What should happen to the original draft? | Preserve it and document the correction in version history. | Delete it without trace. | Keep the accusation unchanged to avoid admitting a correction. | Replace it with a claim that nothing happened. | Transparent amendment preserves the record without retaining the unsupported causal assertion as fact.
What does removing the causal accusation establish? | The record no longer presents an unverified cause as proved. | The named person is proved uninvolved. | The equipment is safe to use. | The footage has been reviewed. | A more accurate record does not itself determine causation, exoneration, or operational release.''',
    dialogue='''Daniel | The draft says a tug driver struck cart C4 and caused the damage. Before we keep that sentence, what did you personally observe?
Rosa | My [[firsthand account::A firsthand account covers Rosa's own observation of the dent, not a contact or cause she did not witness.]] is narrower. I saw a dent on C4's side panel at nine forty-two local time. I did not see any impact or contact.
Daniel | Then nine forty-two is the time you noticed the damage. We should not automatically label it the time the damaging event occurred.
Rosa | Correct. It is the [[observation time::Observation time records when Rosa noticed the dent; the actual time of the damage-producing event remains unverified.]], not a verified event time. I do not know how long the dent had been there when I saw it.
Daniel | The draft also mentions a bang at nine thirty-nine. Did you hear that yourself, or is that information from somebody else's account?
Rosa | That needs [[attribution::Attribution identifies Ivo as the source of the reported sound and prevents it from becoming Rosa's claimed firsthand observation.]]. Ivo told me he heard a bang near the cart at approximately nine thirty-nine. He did not see contact either, so his account does not identify an impact.
Daniel | Keep approximately. Turning a remembered time into an exact timestamp would give readers more precision than the source actually provides.
Rosa | I will preserve the [[approximate time::Approximate time marks the limited precision of Ivo's reported auditory observation rather than asserting an exact impact timestamp.]] and name the source. The revised chronology can show his reported sound and my later observation without treating them as a proven causal sequence.
Daniel | That sequence may be relevant, but it does not identify who caused the dent. Is there any reviewed video or other evidence supporting the tug statement?
Rosa | The [[camera footage::Camera footage exists as potential evidence in the case, but its contents have not been reviewed or established.]] has not been reviewed. I should not describe it as supporting the claim, and I cannot say it rules the claim out either.
Daniel | Exactly. The investigation can examine relevant evidence through the approved process. The initial report should not announce what that later review will conclude.
Rosa | I will remove the unsupported [[causal claim::The causal claim assigns the damage to a tug driver without evidence establishing that contact, actor, or causal link.]] from the factual account. The report will say what was observed and reported, with the cause still under review.
Daniel | Removing the accusation should not erase the fact that damage was observed. Neutral reporting can still be specific about the equipment and its physical condition.
Rosa | I will retain the [[damage description::The damage description is the observed dent on C4's side panel, which remains relevant even when the unsupported cause is removed.]], the C4 identifier, and the observation time. I will avoid substituting a vague phrase such as something happened somewhere on the ramp.
Daniel | What will you do with the earlier version? We need an honest correction process rather than a record that silently changes after people have read it.
Rosa | I will preserve the [[version history::Version history retains the earlier draft and the documented change, rather than silently deleting the unsupported wording.]] and add a dated amendment explaining the correction. That keeps the original wording traceable while making the current factual account accurate.
Daniel | Good. Also keep this reporting conversation separate from the equipment's operational status. A revised report is not permission to put the cart back into use.
Rosa | Understood. Any [[factual amendment::A factual amendment corrects the record; it does not provide operational clearance or replace the site's equipment-control process.]] changes the account, not the separate local controls. Those controls continue under the relevant process, and this exchange does not authorize return to use.
Daniel | Read the current boundary back to me: what is directly observed, what is reported by another person, and what remains unresolved?
Rosa | I saw the dent at nine forty-two. Ivo reports a bang at approximately nine thirty-nine. The footage is unreviewed, and there is no established [[causation finding::A causation finding would require a supported conclusion from the appropriate review, which the supplied observations do not yet provide.]] identifying how the damage occurred.''',
    transfer_title='Keep observation time separate from event time',
    transfer_setup='A worker sees damage on cart K2 at 10:15 local. Pat reports hearing a bang at approximately 10:12 but saw no contact. The video is unreviewed and no cause is established.',
    transfer='''Worker: "My observation time was ___ local." | 10:15 | The worker noticed the damage at ten fifteen, not necessarily when it occurred.
Reviewer: "The earlier sound is attributed to ___." | Pat | Pat supplied the auditory account and its approximate time.
Worker: "The video remains ___." | unreviewed | The case states that its contents have not yet been examined.
Reviewer: "No ___ has been established." | cause | The observations do not identify how or by whom the damage occurred.'''))

BOOK['units'].append(unit(
    title='Regulatory Audits and Readiness',
    scene='Verified records are not the same as total compliance',
    skill='Report evidence coverage accurately, assign outstanding checks, and avoid unsupported compliance claims.',
    brief='An internal aviation audit-preparation list covers current training records for 30 staff. Twenty-seven records have been verified against the stated requirement. Three remain unverified: two assigned to records coordinator Daria and one to team lead Ash. Missing verification does not establish that those staff are untrained or that their records are expired. Quality reviewer Leo needs a factual readiness update by Friday at 15:00 local. The draft says all staff are compliant. Daria and Leo must replace that statement with the verified count, open checks, owners, and deadline. This is preparation evidence for one requirement, not an overall regulatory compliance determination.',
    cast='Daria | Records coordinator\nLeo | Quality reviewer',
    culture=('An honest gap is useful management information', 'Pressure before an audit can encourage complete-sounding summaries. A bounded statement of evidence coverage is more useful than an unsupported claim that everyone complies. Name what has been verified and who will check the remainder without treating an open record question as a finding against a person.'),
    a='''What proportion of the listed records is verified? | 90% | 100% | 10% | 27% | Twenty-seven verified records divided by thirty listed records equals ninety percent.
What do the three unverified records establish? | Verification remains incomplete for those records. | Three staff are proved untrained. | Three records are proved expired. | The entire operation is noncompliant. | An unverified status is an evidence gap, not a confirmed adverse finding.
What is the scope of this review? | Training-record evidence for one stated requirement | Every regulatory obligation | Final external certification | Every employee's entire professional competence | The brief limits the list to one training-record requirement and internal audit preparation.''',
    vocabulary='''audit readiness | The state of preparation to support an audit with relevant evidence. | assess audit readiness
audit scope | The requirements, activities, or period covered by an audit. | define audit scope
audit criterion | A requirement or standard used to assess evidence. | identify the audit criterion
objective evidence | Verifiable information supporting an assessment. | provide objective evidence
training record | Documentation of a person's completed training and relevant status. | verify a training record
currency | Whether a credential or training status remains current under the relevant requirement. | verify training currency
competency | The ability to perform a role to the required standard. | distinguish demonstrated competency
evidence coverage | The share of the defined scope supported by verified evidence. | report evidence coverage
verification backlog | Outstanding records or items awaiting checking. | clear the verification backlog
records owner | The person responsible for maintaining or supplying a record. | identify the records owner
document register | An organized list of controlled documents and their status. | update the document register
controlled copy | A document version managed under the relevant control process. | use the controlled copy
revision status | The current version position of a document. | confirm revision status
retention requirement | A rule governing how long a record must be kept. | check the retention requirement
traceability | The ability to follow evidence to its source and relevant requirement. | maintain evidence traceability
audit trail | The record showing actions, changes, and decisions over time. | preserve the audit trail
open item | A matter not yet resolved or verified. | track an open item
finding | A supported result of evaluating evidence against criteria. | distinguish an audit finding
nonconformity | A demonstrated failure to meet a specified requirement. | document a nonconformity
corrective action | Action addressing the cause of an identified nonconformity. | verify corrective action
closure evidence | Information supporting that an item has been satisfactorily resolved. | review closure evidence
readiness statement | A bounded summary of preparation status. | qualify the readiness statement
sampling limitation | A boundary arising from reviewing only part of a population. | disclose a sampling limitation
compliance determination | An assessment of whether applicable requirements are met. | avoid an unsupported compliance determination''',
    precision='27/30 is 90% verified record coverage. The remaining 3/30 is 10% unverified, not a demonstrated 10% noncompliance rate. One additional verified record would make coverage 28/30, approximately 93.3%, with two checks still open.',
    precision_extra='A current training record is evidence for a specified requirement, not proof of every aspect of competence or all regulatory compliance. Identify the review scope and criterion; do not enlarge the conclusion beyond what was checked.',
    phrases='''State the count | Twenty-seven of thirty records have been verified.
Express the coverage | That is ninety percent of the listed records.
Name the gap | Three records still need verification.
Avoid a personnel judgment | Unverified does not mean the staff member is untrained.
Avoid assuming expiry | We have not established that those records are expired.
Identify the owners | I own two checks, and Ash owns one.
State the deadline | The readiness update is due Friday at 15:00 local.
Correct the claim | All staff compliant exceeds the evidence we have.
Limit the scope | This list concerns one stated training-record requirement.
Request traceable evidence | Please link each verified record to the applicable criterion.
Preserve the audit trail | Record who checked the item and when.
Separate plan and closure | An assigned action is not closure evidence.
Update the remaining count | One additional verification leaves two items open.
Avoid backfilling | Do not create a completion entry without supporting evidence.
Keep the determination distinct | This preparation update is not an overall compliance decision.
Close with specifics | Report the verified count, open checks, owners, and deadline.''',
    notes='''Verified | Supported by the stated check, not merely present in a folder.
Unverified | A current evidence status, not proof of a failed requirement.
Current | Needs the applicable requirement and reference date.
Coverage | Describes how much of the defined list is checked.
Closed | Requires the specified supporting evidence, not just an owner.
All compliant | A broad conclusion requiring evidence beyond this limited list.''',
    d='''Which readiness headline fits the facts? | Twenty-seven of thirty records verified; three checks remain assigned and open. | Every staff member meets every rule. | Three staff are confirmed untrained. | The audit has already granted certification. | The bounded headline gives the verified evidence coverage without inventing broader findings.
If one more record is verified, what is the new coverage? | 28 of 30, approximately 93.3% | 28 of 28, 100% | 27 of 30, 90% | 30 of 30, 100% | The denominator remains thirty and the verified count rises to twenty-eight.
Which statement distinguishes an open item from a finding? | An unverified record needs checking; a nonconformity requires evidence of a failed criterion. | Every missing verification proves a violation. | A named owner automatically closes a finding. | Audit preparation cannot contain uncertainty. | The first statement separates absence of verification from demonstrated failure against a requirement.
What should support closing a record check? | Verified evidence linked to the relevant requirement and recorded review | A confident verbal promise alone | A copied date with no source | The approaching audit deadline | Closure needs traceable verification, not confidence, schedule pressure, or unsupported record entries.''',
    dialogue='''Leo | The draft says all staff are compliant. The preparation list only shows twenty-seven verified training records out of thirty. We need a more accurate headline.
Daria | I will report [[evidence coverage::Evidence coverage describes the verified share of the defined record list, not a percentage of overall regulatory compliance.]] instead. Twenty-seven of thirty is ninety percent verified. Three records remain unverified, and their checks need to stay visible in the update.
Leo | Does unverified mean the staff missed training or their records expired? Neither should be implied without evidence.
Daria | No. The [[open items::Open items are the three unresolved verification checks; they are not established failures by the staff concerned.]] are verification questions. We have not established that those people are untrained or that their records are expired. The missing check is not the same as a negative finding.
Leo | Who owns the remaining work? Saying someone will check later will not help us prepare a reliable update.
Daria | I am the [[records owner::Records owner identifies Daria's responsibility for the two assigned checks, while Ash separately owns the third.]] for two checks, and Ash owns the third. I will keep those assignments explicit rather than place all three under a general team label.
Leo | The update is due Friday at fifteen hundred local. That deadline is for a factual readiness report, including any unresolved items, not for changing the status by assumption.
Daria | Agreed. The [[readiness statement::The readiness statement must accurately describe the evidence available at the deadline, including unresolved checks.]] will give the verified count, remaining checks, owners, and deadline. If a record is still unverified, I will say so rather than force a complete result.
Leo | What evidence are we using to mark a record verified? We should be able to show the requirement checked, not just point to a file with the person's name.
Daria | Each check needs [[traceability::Traceability connects the verified record to its source, review, and applicable requirement rather than relying on a filename alone.]] to the stated requirement and the relevant record. A document in a folder is not enough if its identity, currency, or applicable basis has not been verified.
Leo | If one more record is verified today, how will you update the percentage without changing the population?
Daria | The [[verified count::The verified count becomes twenty-eight while the defined population remains thirty, giving approximately ninety-three point three percent coverage.]] becomes twenty-eight of thirty, about ninety-three point three percent. Two checks remain open. We should not change the denominator to twenty-eight and call the result one hundred percent.
Leo | Exactly. We also need to resist treating this single list as evidence for every regulatory obligation or every aspect of a person's ability to perform the job.
Daria | I will state the [[audit scope::Audit scope limits this preparation evidence to the specified training-record requirement, not every operational or regulatory obligation.]] clearly. This preparation list concerns one training-record requirement. It is not a complete assessment of professional competence or an overall regulatory compliance determination.
Leo | If a check later demonstrates that a requirement was not met, then we can record the supported finding and follow the appropriate action process.
Daria | Yes. A [[nonconformity::A nonconformity requires demonstrated failure against a specified requirement; an unverified record alone does not establish it.]] needs evidence against a criterion. We should not label someone noncompliant because a check is pending, or hide a real finding once the evidence establishes it.
Leo | Preserve who performed each check and when. We need a traceable record, not a spreadsheet that silently turns green.
Daria | I will maintain the [[audit trail::The audit trail records verification actions and changes so the status can be reviewed rather than accepted from an unexplained color label.]]. No unsupported completion entry or copied date should replace the actual evidence. Any correction must remain traceable in the controlled record.
Leo | Then our current message is ninety percent record coverage, three checks open, two with you and one with Ash, update Friday at fifteen hundred local.
Daria | Correct. A future [[closure::Closure requires the relevant verification evidence; assignment of an owner and deadline is only a plan for completing the check.]] will depend on verified evidence, not simply on an assigned owner or an approaching deadline. I will circulate the bounded update and revise it as checks are completed.''',
    transfer_title='Report coverage without declaring universal compliance',
    transfer_setup='A list has 40 training records. Thirty-six are verified and four remain unverified. After one more check succeeds, the denominator stays 40. The list covers one requirement only.',
    transfer='''Reviewer: "Initial verified coverage is ___ percent." | 90 | Thirty-six divided by forty equals ninety percent verified coverage.
Coordinator: "After one more verification, the count is ___." | 37 | One additional verified record raises thirty-six to thirty-seven.
Reviewer: "The number still unverified is ___." | 3 | Forty total records minus thirty-seven verified leaves three unverified.
Coordinator: "This does not establish overall regulatory ___." | compliance | Evidence for one requirement does not determine compliance with every applicable obligation.'''))
