"""Original Housekeeping and Commercial Cleaning learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='housekeeping-commercial-cleaning',
    title='Housekeeping and Commercial Cleaning English',
    cover_label='ENGLISH FOR CLEANING TEAMS',
    cover_title='Housekeeping and\nCommercial Cleaning',
    cover_size=29,
    tagline='Clear tasks. Reliable handovers.',
    audience='For room attendants, commercial cleaners, housekeeping teams, and cleaning supervisors.',
    map_intro='Eight workplace conversations: define an assignment, arrange an occupied-room visit, question an unreadable product label, report a floor hazard, transfer found property, count linen, respond to a quality concern, and hand over room statuses.',
    notes_title='Name the place. Preserve the permission.',
    notes_intro='A useful cleaning message identifies the exact room or surface, what was observed or requested, and what may happen next. Clear English helps a worker be helpful without guessing a product, entering an unapproved space, or reporting unfinished work as complete.',
    field_notes=[
        ('Scope names the work', 'Everything is not a precise assignment. Repeat the listed surfaces and tasks, then send additional requests to the person who can authorize changes.', '"My assignment covers table surfaces and the floor; I will check the extra request with my supervisor."'),
        ('A time is not an entry permission', 'A return window helps coordinate service, but it does not replace actual access requirements. Keep a declined visit, an offered window, and permission to enter separate.', '"I can return between eleven fifteen and eleven thirty; entry still follows our access procedure."'),
        ('Visible details beat a guess', 'Report an unreadable label, the location of water, or the appearance of found property accurately. Do not guess chemical identity, fault cause, contents, or ownership.', '"Water is visible outside washroom B, beside the east stair door; the source is unknown."'),
        ('Done needs a named stage', 'Cleaned, inspected, accessible, and released are different states. Name the next owner and the unfinished step so a handover stays accurate.', '"Room 302 is cleaned and awaits inspection; room 303 was not accessible and has not been cleaned."'),
    ],
    scope_note='All sites, rooms, quantities, guests, and incidents are fictional. This book teaches workplace English, not chemical handling, equipment operation, hazard control, legal advice, or specialist infection prevention. Follow actual training, product labels and safety data sheets, site access rules, privacy and found-property procedures, and emergency arrangements. No example authorizes unsafe access, use of an unidentified product, or release of an unchecked area.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Janitors and Building Cleaners.',
             url='https://www.bls.gov/ooh/building-and-grounds-cleaning/janitors-and-building-cleaners.htm',
             note='Occupational context for task assignments, surface cleaning, supplies, and reporting maintenance needs. Individual duties depend on the actual role and site.', checked='1 October 2026'),
        dict(title='US Bureau of Labor Statistics. Maids and Housekeeping Cleaners.',
             url='https://www.bls.gov/ors/factsheet/maids-and-housekeeping-cleaners.htm',
             note='Occupational context for guest-room cleaning and linen replenishment. No guest-access or property-release rule is inferred from this profile.', checked='1 October 2026'),
        dict(title='Occupational Safety and Health Administration. Hazard Communication.',
             url='https://www.osha.gov/hazcom/',
             note='Background for product identification, labels, safety data sheets, and understandable hazard information. The book supplies no chemical-use instructions.', checked='1 October 2026'),
        dict(title='Centers for Disease Control and Prevention. When and How to Clean and Disinfect a Facility.',
             url='https://www.cdc.gov/hygiene/about/when-and-how-to-clean-and-disinfect-a-facility.html',
             note='Terminology distinguishing cleaning and disinfection in community facilities. This guidance is not a substitute for healthcare or other specialized-site requirements.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Confirming the assignment and its limits',
    scene='What does everything include?',
    skill='Restate a defined cleaning assignment, clarify an extra request, and preserve authorization despite a deadline.',
    brief='Cleaner Maya has a commercial assignment reading conference room: tables and floor. It covers table surfaces and the floor, not high windows or personal equipment. Client Jordan asks for everything before a 3:00 meeting and points to the high windows and laptops on the tables. Supervisor Rosa can clarify and authorize any additional work through the site process. No extra work has been approved, and the deadline does not expand permission. Maya must acknowledge the meeting, name the actual scope, and arrange clarification without promising all requested tasks.',
    cast='Jordan | Client contact\nMaya | Cleaner',
    culture=('A boundary can include a next step', 'A direct request from a client may feel difficult to question. Acknowledge the practical need, state the assigned work plainly, and name who can clarify an addition. Helpful language does not require agreeing to work outside the actual authorization or training.'),
    a='''What is Maya assigned to clean? | Table surfaces and the floor | Every object and high window | Personal laptops only | Anything requested before three | The assignment specifically covers table surfaces and the floor, with stated exclusions.
Who can clarify extra work? | Supervisor Rosa | The deadline itself | Any passerby | The assignment automatically expands | Rosa is identified as the supervisor who can handle changes through the site process.
What does the 3:00 meeting establish? | A stated time constraint, not expanded permission | Approval to clean personal devices | Completion of all tasks | Authorization for high-window work | The meeting time describes urgency but does not change the authorized scope.''',
    vocabulary='''assignment | Work specifically allocated to a worker or team. | confirm the assignment
scope of work | Defined tasks and boundaries of an assignment. | clarify the scope of work
task list | Written list of required work items. | review the task list
table surface | Exposed working area of a table. | clean the table surfaces
floor area | Specified section of floor within the assignment. | identify the floor area
high window | Window area requiring access above ordinary floor-level work. | clarify high-window work
personal equipment | Devices or items belonging to individual users. | exclude personal equipment
client contact | Person communicating requirements for the customer organization. | speak with the client contact
site supervisor | Person overseeing assigned work at the location. | consult the site supervisor
additional work | Work beyond the current assignment. | request additional work
authorization | Actual permission from the relevant responsible person or process. | obtain authorization
work order | Record describing requested or assigned work. | check the work order
service specification | Description of the service and required outcome. | follow the service specification
exclusion | Item or task explicitly outside an assignment. | explain an exclusion
deadline | Time by which a task is requested or required. | clarify the deadline
meeting setup | Arrangement of a room for a meeting. | separate cleaning from meeting setup
surface access | Ability and permission to reach the relevant surface. | confirm surface access
approved change | Change accepted through the required process. | record an approved change
priority | Relative importance or order of assigned tasks. | confirm the priority
capacity | Available time, resources, and ability for the work. | check team capacity
completion estimate | Approximate expected finishing time. | obtain a completion estimate
task boundary | Limit of the work assigned or authorized. | state the task boundary
clarification request | Specific question sent to resolve uncertainty. | raise a clarification request
read-back | Repetition of the understood instruction for confirmation. | give a scope read-back''',
    precision='Before three identifies the requested deadline. It does not mean all tasks are authorized or feasible. Preserve the difference between the current assignment, an additional request, and an approved change.',
    precision_extra='Tables can mean table surfaces rather than every object resting on them. If access is blocked by personal equipment, ask for the actual site arrangement. Do not infer permission to handle devices or belongings from a general cleaning request.',
    phrases='''Acknowledge the timing | I understand the meeting starts at three.
Read the assignment | My task list says table surfaces and the floor.
Clarify everything | Which additional areas do you mean by everything?
Name the exclusion | High windows are not in my current assignment.
Protect personal equipment | Personal devices are outside the stated scope.
Offer the next step | I can ask Rosa to clarify the extra request.
Keep approval distinct | That request has not been approved yet.
Avoid a blanket promise | I cannot confirm all of that from this assignment.
Check the boundary | Does the work order include that surface?
Explain the deadline | The meeting time does not change the permission for the work.
Ask about access | What is the approved arrangement for clearing the table surfaces?
Keep ownership clear | Rosa can confirm whether additional work is authorized.
Summarize the present scope | Table surfaces and floor remain the assigned tasks.
Avoid a guessed estimate | I will not give a completion time I have not checked.
Report the outcome | I will pass on the clarified instruction.
Close the read-back | I understand the request; I am checking the change before agreeing to it.''',
    notes='''Covers | Covers defines included work without implying every nearby task is included.
Outside the scope | This phrase states a task boundary, not a personal unwillingness to help.
Before versus by | Both can identify a deadline; neither supplies permission for extra work.
Request versus approval | A person can request more work before the authorized process accepts it.
Everything | Replace this broad word with specific surfaces and tasks.
Can ask | This commits to seeking clarification, not to receiving a particular answer.''',
    d='''Which response is clearest? | My assignment covers the tables and floor; I will check the extra work with Rosa. | Everything is automatically included. | I will clean personal laptops because they are on a table. | The deadline overrides the task list. | The response preserves scope and gives a practical route for the additional request.
Which statement wrongly treats urgency as permission? | The meeting is at three, so high windows are now authorized. | The meeting starts at three. | Rosa can clarify extra work. | The current task list covers the floor. | A time constraint does not authorize an excluded task or change the assignment.
What should Maya avoid promising? | Completion of every requested extra before three | A clarification request to Rosa | A read-back of the listed tasks | A factual explanation of the exclusion | No approval or feasibility check supports a promise to complete all additional work.
Why clarify tables? | Objects on a table may be outside the assigned surface-cleaning scope. | Tables always include all electronics everywhere. | Personal equipment is never present. | The floor automatically becomes excluded. | Table-surface work does not itself authorize handling personal devices resting on the table.''',
    dialogue='''Jordan | We have a meeting at three, so could you do everything in the conference room? The high windows and the laptops need attention too.
Maya | I understand the timing. My [[assignment::Assignment identifies the work currently allocated: table surfaces and floor, not every requested addition.]] covers the table surfaces and the floor. I need to clarify the extra areas before agreeing to include them.
Jordan | I thought everything in the room came under cleaning. The laptops are sitting on the tables, so would they not be part of that?
Maya | The [[scope of work::Scope of work defines the included tasks and boundaries; table surfaces do not automatically include personal equipment.]] names the surfaces, not the personal equipment on them. I do not have permission from this task list to clean those devices.
Jordan | All right. But the high windows look noticeable from the meeting table. Could you add them because the meeting is important?
Maya | They would be [[additional work::Additional work is outside the current assignment and needs clarification rather than automatic inclusion because of urgency.]]. I can ask Rosa about the request, but I cannot treat the meeting time as approval to take on that task.
Jordan | Who is Rosa in relation to this job? I would like the request to reach someone who can give us a clear answer.
Maya | Rosa is the [[site supervisor::The site supervisor is the identified person who can clarify and authorize changes through the actual site process.]]. She can clarify the authorized work and the arrangements needed for anything beyond my present assignment.
Jordan | Please ask her, then. I do not want you to tell me yes now and later discover the work could not actually be done.
Maya | I will raise a [[clarification request::A clarification request seeks a defined decision about the extra tasks without implying the answer is already yes.]] identifying the high windows and personal equipment. I will also mention the three o'clock meeting as the time constraint.
Jordan | That would help. Meanwhile, what can I tell the meeting organizer is currently included, without promising the extras on your behalf?
Maya | You can say the [[task list::The task list provides the confirmed included work and should not be enlarged in a message to another person.]] covers table surfaces and floor. The extra request is being checked; no change has been approved yet.
Jordan | And if the laptops are in the way of the table surfaces, should I simply assume you will move them aside?
Maya | Please do not assume that. We need the approved [[surface access::Surface access includes the practical and authorized arrangement for reaching the table without assuming permission to handle belongings.]] arrangement for those areas. Cleaning the table does not automatically authorize me to handle personal equipment.
Jordan | Understood. I can wait for the clarification on that. The main thing is to avoid different people giving different instructions at once.
Maya | Yes. Any [[approved change::An approved change is a modification actually accepted through the relevant process, unlike the still-pending request.]] needs to be clear in the work instructions. That helps the team know what is included and what remains outside the task.
Jordan | You have not promised that all the extras will be finished by three, have you? I want to repeat your position accurately.
Maya | Correct. The [[deadline::Deadline names the time requirement but does not establish authorization, resources, or a reliable completion promise.]] is noted, but I have not confirmed extra work or a completion estimate for it. Rosa needs to clarify those points.
Jordan | Thank you. Please pass on the two extra requests and the meeting time. I will describe the current work as tables and floor only.
Maya | That is an accurate [[read-back::Read-back repeats the confirmed scope and pending request, checking that both people share the same understanding.]]. I will take the clarification to Rosa and communicate the actual outcome, without treating the request itself as permission to proceed.''',
    transfer_title='Clarify a different commercial assignment',
    transfer_setup='A work order covers reception counters and the lobby floor. The client adds exterior signs before noon. Supervisor Leon can review changes, but no extra work is approved.',
    transfer='''Cleaner: "The assigned horizontal surfaces are the reception ___." | counters | Counters are the named surfaces included in this work order.
Client: "The additional request concerns the exterior ___." | signs | Exterior signs are the requested addition, not an already included task.
Cleaner: "I will ask ___ to review the request." | Leon | Leon is the supervisor identified for reviewing any proposed change.
Cleaner: "The extra work is not yet ___." | approved | The brief explicitly states that approval has not been given.'''
))

BOOK['units'].append(unit(
    title='Respecting access and occupied spaces',
    scene='Not during the call',
    skill='Acknowledge a declined visit, offer the actual return window, and distinguish an agreed plan from room-entry permission.',
    brief='At 10:00, guest Alex in room 312 declines cleaning because a call is expected to last until 11:00. Attendant Lina can return between 11:15 and 11:30 or offer fresh towels at the door now. Alex chooses the return window and does not request towels at the door. Lina must record that plan accurately without promising exactly 11:00 or treating the end of the call as permission to enter. Actual room-access procedures still apply when the attendant returns. No room entry or cleaning completion occurs in this conversation.',
    cast='Alex | Guest in room 312\nLina | Room attendant',
    culture=('Give control without inventing availability', 'A guest may need privacy without wanting to cancel service entirely. Offer the real options in plain language and repeat the chosen window. Respecting the current refusal is compatible with arranging a later visit; neither requires assuming future entry permission.'),
    a='''Why is cleaning declined at 10:00? | The guest is on a call until about 11:00 | The room has already been released | The attendant has no assigned room | The guest cancels every future visit | The stated reason is the call, not a permanent cancellation of service.
What return window is available? | 11:15-11:30 | Exactly 11:00 | 10:00-10:15 | Any time without checking | Lina's actual available return window begins at eleven fifteen and ends at eleven thirty.
What does Alex choose? | The return window, without towels now | Entry during the call | An exact eleven o'clock appointment | Cancellation of all cleaning | Alex chooses the later offered window and declines the separate towel option.''',
    vocabulary='''occupied room | Room currently in use by a guest or other occupant. | respect an occupied room
room attendant | Worker assigned to guest-room cleaning and related service. | speak with the room attendant
declined service | Offered service the occupant does not accept at that time. | record declined service
return window | Time range in which a worker can come back. | offer a return window
appointment time | Specific agreed time rather than a broad window. | confirm the appointment time
privacy | Freedom from inappropriate intrusion or disclosure. | respect guest privacy
access permission | Authorization to enter or use a particular space. | confirm access permission
entry procedure | Actual required steps and rules for entering a space. | follow the entry procedure
doorstep delivery | Handover of an item at the doorway rather than room entry. | offer doorstep delivery
fresh towels | Clean towels available for guest use. | offer fresh towels
service option | Available choice about the service to be provided. | explain a service option
do-not-disturb notice | Guest instruction or signal requesting no interruption under site rules. | respect a do-not-disturb notice
service request | Guest's stated request for an available service. | record a service request
visit plan | Arrangement for a future visit. | confirm the visit plan
availability | Time or circumstances in which a person or service can be accessed. | clarify availability
time range | Interval with a beginning and end. | repeat the time range
scheduled return | Planned later visit within the agreed arrangement. | record a scheduled return
unoccupied | Not currently occupied, where that status is actually established. | verify unoccupied status
guest preference | Stated service choice or wish of the guest. | record the guest preference
access record | Record of relevant entry or permission information. | update the access record
interruption | Action that disturbs an ongoing activity. | avoid an unnecessary interruption
service deferral | Moving a service to a later available opportunity. | arrange a service deferral
exact-time promise | Commitment to a specific arrival time. | avoid an unsupported exact-time promise
confirmation | Clear agreement about the understood plan. | obtain confirmation''',
    precision='Until eleven describes the guest call. Between eleven fifteen and eleven thirty describes the available return window. Neither means the attendant has promised to arrive exactly when the call ends.',
    precision_extra='A later visit plan does not replace actual access rules. Do not equate silence, an expected end time, or a prior conversation with permission to enter. Keep room status, guest preference, and entry authorization distinct.',
    phrases='''Acknowledge the refusal | Certainly; I will not start service now.
Clarify the timing | Your call is expected to finish at eleven.
Offer the real window | I can return between eleven fifteen and eleven thirty.
Avoid an exact promise | I cannot promise exactly eleven.
Offer the separate option | I can offer fresh towels at the door now.
Keep entry separate | A towel handover does not require us to assume room entry.
Ask for the choice | Which of those options would suit you?
Confirm the return | I have recorded the eleven-fifteen-to-eleven-thirty window.
Preserve the refusal | Cleaning was declined at ten because of your call.
Avoid overgeneralizing | You are postponing this visit, not cancelling every service.
Respect privacy | I understand that you do not want an interruption.
Explain the later check | We will still follow the entry procedure when we return.
Keep towels distinct | No towel delivery is requested now.
Repeat the room | This plan is for room 312.
Check agreement | Have I understood your preference correctly?
Close politely | Thank you; I will record the agreed return plan.''',
    notes='''Between and | Use both endpoints to communicate a real time window.
Until | Until eleven identifies the call's expected duration, not an entry authorization.
Now versus later | Declining now does not necessarily reject all future service.
Can return | State an available option without silently converting it to an exact appointment.
At the door | This specifies a limited handover location, not access to the whole room.
Expected | An expected end time remains different from a completed event.''',
    d='''Which read-back is accurate? | Return between 11:15 and 11:30; no towels requested now. | Enter exactly at 11:00. | Cleaning is permanently cancelled. | Deliver towels and start cleaning during the call. | The read-back preserves the chosen window and declined towel option.
What does the call ending at eleven establish? | Expected availability information, not automatic entry permission | A universal right to enter at eleven | Completed cleaning | A new room number | An expected end time does not replace the actual room-access procedure.
Which offer is within Lina's stated options? | Fresh towels at the door now | Guaranteed arrival at 11:00 | Immediate entry despite refusal | An unpromised late-night visit | Doorstep towels are one of the two explicitly available choices.
Why record the exact window? | To avoid turning a time range into a different appointment | To make permission unnecessary | To prove the room is empty | To claim the service is complete | Recording both endpoints prevents a later worker from assuming an unsupported exact arrival time.''',
    dialogue='''Alex | I cannot have the room cleaned now. I have a call that is expected to run until eleven, and I need some privacy.
Lina | Of course. I will record this as [[declined service::Declined service describes the current ten-o'clock visit, not a cancellation of every future cleaning opportunity.]] for now because of your call. We can discuss a later option without starting anything in the room.
Alex | Thank you. Could you come back as soon as the call ends? Eleven would be convenient if you have that time available.
Lina | My available [[return window::Return window is the actual offered interval, eleven fifteen to eleven thirty, rather than an exact eleven-o'clock appointment.]] is between eleven fifteen and eleven thirty. I cannot promise exactly eleven, but I can offer that later range.
Alex | That should work. I want to hear the other option too, in case I decide I only need towels today.
Lina | I can offer [[fresh towels::Fresh towels are the separate available service option that can be handed over at the door now.]] at the door now. That is separate from the later room-cleaning visit, so you can choose the option you prefer.
Alex | I think I would rather have the cleaning visit later. I do not need the towels brought to the door now as well.
Lina | Understood. Your [[guest preference::Guest preference is the chosen later visit, with no separate towel delivery requested at the present time.]] is a return between eleven fifteen and eleven thirty, without a towel delivery now. I will record those details together.
Alex | Please do. I have had situations where a time range became an exact time when the message reached another member of staff.
Lina | I will keep it as a [[time range::Time range preserves both endpoints and prevents the plan from becoming an unsupported exact arrival promise.]], not an exact appointment. The earliest point offered is eleven fifteen, and the end of the window is eleven thirty.
Alex | And if the call is still going when someone comes back, I do not want them to assume they can enter because we spoke earlier.
Lina | We will still follow the [[entry procedure::Entry procedure remains necessary at the actual visit; this scheduling conversation does not by itself authorize entry.]] when we return. This conversation records a visit plan; it does not replace the required access arrangements.
Alex | Good. The call should finish at eleven, but that is an expectation, not something I can guarantee before it happens.
Lina | I understand. Your expected [[availability::Availability concerns when the guest may be free; it is separate from verified room status or permission to enter.]] helps us plan, but we will not treat the clock reaching eleven as automatic permission to enter the room.
Alex | Thank you for making that distinction. I am not cancelling all cleaning, just asking not to be interrupted during this call.
Lina | I will describe it as a [[service deferral::Service deferral means moving the visit later, accurately reflecting the guest's choice rather than permanent cancellation.]]. You have selected the later window rather than refusing every future visit or requesting immediate cleaning.
Alex | Could you repeat the room number too? I want to make sure this gets attached to the correct room on your list.
Lina | Room three hundred twelve. The [[visit plan::Visit plan links the correct room to the chosen return window and does not report that cleaning has already occurred.]] is a return between eleven fifteen and eleven thirty, with no fresh-towel delivery requested now.
Alex | Yes, that is right. I appreciate the clear options. I will continue my call and expect the later visit within that window.
Lina | Thank you for the [[confirmation::Confirmation establishes agreement on the stated plan, while actual entry permission and completed service remain separate questions.]]. I will record it accurately and respect your privacy now. The later visit will still follow the normal access requirements.''',
    transfer_title='Record another return window',
    transfer_setup='At 9:00, room 420 declines service during a call until 10:00. The offered return window is 10:30-10:45. The guest chooses that window and does not request towels now.',
    transfer='''Attendant: "This plan is for room ___." | 420 | Room 420 is the identifier supplied for the new visit plan.
Guest: "The call is expected to finish at ___." | 10:00 | Ten o'clock is the expected call end, not the promised return.
Attendant: "The return window is ___." | 10:30-10:45 | The offered and chosen window runs from ten thirty to ten forty-five.
Attendant: "Entry still follows the actual ___." | access procedure | Scheduling the visit does not remove the site's entry requirements.'''
))

BOOK['units'].append(unit(
    title='Clarifying product and task information',
    scene='The unreadable label',
    skill='Report uncertain product identity, request understandable information, and resist identification by color or familiarity.',
    brief='Cleaner Farah notices an unreadable label on a bottle on the cleaning cart. Colleague Owen believes it is the usual surface cleaner because of its color, but two products use similar bottles. Farah has not used it. Supervisor Ben can identify the product through the actual site process and provide the relevant information or a clearly identified replacement. No identity, mixing instruction, dilution ratio, protective-equipment selection, or use approval is established here. The task is to ask precise questions and preserve the stopped-use status while the uncertainty is resolved.',
    cast='Farah | Cleaner\nOwen | Colleague',
    culture=('Question the evidence, not the colleague', 'A familiar coworker may offer a confident shortcut in good faith. Explain the specific uncertainty, such as two similar bottles, and request a reliable identification. This keeps the discussion cooperative while making clear that confidence or seniority cannot replace the missing product information.'),
    a='''What is wrong with the bottle? | Its label is unreadable | Its identity is fully verified | It has already been used by Farah | Its instructions are clear | The visible problem is an unreadable label, leaving identity unconfirmed.
Why is color insufficient here? | Two products use similar bottles | Color always identifies every product | Owen has supplied a readable product code | No product information is needed | Similar bottles make appearance an unreliable basis for identifying this product.
What can Ben arrange? | Proper identification and information, or an identified replacement | An invented dilution ratio | Approval based only on memory | A smell test taught by this book | Ben is the named supervisor able to resolve identity through the actual site process.''',
    vocabulary='''product identifier | Name or code used to identify a specific chemical product. | verify the product identifier
unreadable label | Label whose information cannot be reliably read. | report an unreadable label
container | Vessel holding a substance or product. | identify the container
secondary container | Container into which a product has been transferred from another container. | check a secondary container
safety data sheet | Document describing a chemical product's hazards and relevant safety information. | consult the safety data sheet
SDS | Abbreviation for safety data sheet. | obtain the relevant SDS
hazard statement | Standardized wording describing the nature of a chemical hazard. | read the hazard statement
precautionary statement | Wording describing measures to prevent or reduce harmful effects. | understand the precautionary statement
signal word | Label word indicating the relative severity of a hazard. | identify the signal word
pictogram | Graphic symbol communicating a hazard or other defined information. | recognize the pictogram
product information | Relevant identifying, hazard, and use information for a product. | request product information
manufacturer instructions | Directions supplied by the product or equipment manufacturer. | follow manufacturer instructions
surface compatibility | Whether a product is suitable for a particular surface material. | verify surface compatibility
cleaner | Product intended to remove soil or unwanted material from a surface. | identify the cleaner
detergent | Cleaning agent that helps remove soil. | identify the detergent
disinfectant | Product intended to kill or inactivate specified microorganisms when used as directed. | identify the disinfectant
sanitizer | Product used to reduce microorganisms to an applicable specified level. | distinguish a sanitizer
dilution | Reduction in concentration according to the applicable instructions. | verify dilution instructions
concentrate | Product supplied at a strength requiring the specified preparation before use. | identify a concentrate
ready-to-use | Supplied in a form intended for use without additional dilution, as directed. | confirm ready-to-use status
PPE | Personal protective equipment selected for the actual hazards and task. | verify required PPE
ventilation | Supply or movement of air relevant to working conditions. | check ventilation requirements
exposure | Contact with a substance through a relevant route. | report an exposure
identified replacement | Substitute product with its identity and relevant information established. | request an identified replacement''',
    precision='A product identifier must connect the actual container with the relevant information. A similar bottle or familiar color does not establish identity. Do not infer use instructions, surface suitability, or protection requirements from an unverified guess.',
    precision_extra='Cleaning, sanitizing, and disinfecting are different functions. The required product and process depend on the actual task and site. This vocabulary does not authorize a chemical procedure or replace understandable training and current product instructions.',
    phrases='''State the problem | I cannot read this bottle label.
Preserve the status | I have not used the product.
Question the identification | What reliable information identifies this container?
Explain the ambiguity | Two products use similar bottles here.
Reject a color-only guess | The color does not establish which product this is.
Ask for the supervisor | Can Ben verify the identity through the site process?
Request information | I need the relevant product information in a form I can understand.
Ask for the document | Which safety data sheet belongs to this product?
Check the match | The information must match the actual container.
Request a replacement | A clearly identified replacement may resolve the immediate problem.
Avoid a guessed ratio | I will not invent dilution instructions.
Separate compatibility | We also need the product to suit the assigned surface.
Keep the pause visible | The product remains unused while identity is unresolved.
Ask for clarification | Please explain that instruction before I proceed.
Avoid a false approval | We have not confirmed this product for the task.
Close the request | Let us get verified identification and the relevant instructions.''',
    notes='''Looks like | This reports resemblance, not verified identity.
The relevant | The relevant SDS must match the actual product rather than a similar bottle.
Have not used | This clearly states the current status without implying exposure.
Before proceeding | This establishes the sequence of clarification before action.
Understandable | Receiving a document is not the same as understanding the instruction.
Replacement | A replacement needs clear identification; another unknown bottle does not solve the problem.''',
    d='''Which response challenges the shortcut constructively? | Two products look similar; let us ask Ben to verify this one. | You are careless and always wrong. | The color proves it is safe. | I will test it by mixing it with another cleaner. | The response gives the factual reason for doubt and a proper clarification route.
Which document is relevant? | The safety data sheet matching the actual product | Any sheet with a similar logo | An old memory of another product | A cafe recipe | Safety information needs to correspond to the identified product rather than an approximate match.
Which statement is unsupported? | This product is approved for the surface because the bottle looks familiar. | The label is unreadable. | Farah has not used it. | Ben can arrange identification. | Familiar appearance does not establish product identity or suitability for the task.
What should remain clear in the handoff? | Identity unresolved and product unused | Product used successfully | Dilution ratio invented | Every similar bottle is interchangeable | The handoff must preserve the actual uncertainty and stopped-use status supplied.''',
    dialogue='''Farah | I cannot read the label on this bottle. Before I do anything with it, I need to know what product it actually contains.
Owen | It [[looks like::Looks like expresses visual resemblance, which is weaker than verified identity when two products use similar bottles.]] the surface cleaner we usually use. The color is familiar, although I have not checked a readable name or code on this one.
Farah | There are two products in similar bottles here, so the color does not settle it. I have not used this bottle on any surface.
Owen | You are right to separate appearance from the [[product identifier::Product identifier is the reliable name or code needed to connect the container with the correct product information.]]. I cannot give you a verified identity just from recognizing the general bottle style.
Farah | Can Ben help identify it? I would like to give him a precise question instead of asking whether the bottle is probably all right.
Owen | Yes. We can report the [[unreadable label::Unreadable label is the observed problem that prevents reliable identification, rather than an assumed chemical fault.]] and say the product remains unused. He can arrange identification through the actual site process.
Farah | If he identifies it, I also need the relevant instructions. Knowing a name would not tell me every requirement for this particular surface.
Owen | We should request the matching [[product information::Product information must relate to the identified product and task; a name alone does not explain all relevant requirements.]], including the appropriate label and safety information. We should not fill in missing directions from memory.
Farah | I have heard people say SDS. I want to make sure I ask for the correct document rather than just another sheet with a similar name.
Owen | SDS means [[safety data sheet::Safety data sheet expands SDS and identifies the document describing the product's hazards and related safety information.]]. The important point is that it must match the actual product, not merely another container that looks similar.
Farah | Thank you. And if the bottle cannot be identified promptly, could we ask for a different one with clear information instead?
Owen | Ben can arrange an [[identified replacement::An identified replacement offers a product with established identity and information, not a second uncertain container.]] through the site process. That means a product with clear identification and relevant instructions, not another unknown bottle.
Farah | I do not want someone to hear that request as permission to choose any cleaner from the cart and use it in the same way.
Owen | Agreed. [[Surface compatibility::Surface compatibility concerns whether the identified product suits the actual material; products are not interchangeable merely because both clean.]] still matters. We need the appropriate product for the assigned task, with the actual instructions and training requirements followed.
Farah | I also will not guess a mixing amount or a dilution from a previous job. The products and arrangements may be different here.
Owen | Correct. Any [[dilution::Dilution instructions are product-specific requirements that must be verified rather than invented from past experience.]] instruction must come from the applicable information. This conversation has not established a ratio or authorized any preparation step.
Farah | Please include that I have not used it. I want Ben to know this is an identification query, not a report that I already tried it.
Owen | I will preserve that [[unused::Unused states the actual status of this bottle in Farah's task; the message must not invent use or exposure.]] status in the message. We should also keep any exposure or incident report factual if something different ever occurs.
Farah | Good. Once the information is available, I will ask about any part I do not understand before I proceed with the assigned task.
Owen | That is the point of [[clarification::Clarification resolves a specific uncertainty before action; receiving unclear information does not itself establish understanding or permission.]]. Let us ask Ben for reliable identification and understandable instructions, keeping the product unused while this uncertainty remains.''',
    transfer_title='Report another unidentified container',
    transfer_setup='A spray bottle on cart C has an unreadable label. Worker Ana has not used it. Lead Leon can arrange identification or an identified replacement. Product color is not sufficient evidence.',
    transfer='''Worker: "The affected bottle is on cart ___." | C | Cart C is the stated location of the unidentified bottle.
Worker: "The label is ___." | unreadable | Unreadable describes the observed label problem preventing reliable identification.
Colleague: "The lead for this query is ___." | Leon | Leon is the named lead who can arrange the check.
Worker: "The product remains ___." | unused | Ana has not used the bottle, so that status must remain clear.'''
))

BOOK['units'].append(unit(
    title='Reporting faults and unsafe access',
    scene='Outside washroom B',
    skill='Give an exact location and observed condition, preserve uncertainty about the cause, and avoid premature clearance.',
    brief='Cleaner Ravi sees water on the floor outside washroom B, beside the east stair door. Ravi does not know its source and has already reported it under the site safety arrangements. Supervisor Elena asks for a clear follow-up message identifying the location and current status. The affected area has not been declared ready. No leak diagnosis, repair result, completed cleanup, or approved reopening is established. The exchange practices accurate reporting while the actual site controls remain in effect; it does not teach a cleanup method or authorize anyone to enter the affected area.',
    cast='Ravi | Cleaner\nElena | Supervisor',
    culture=('Urgency needs precision', 'A brief hazard message can be both direct and respectful. Lead with the location and observed condition, then state what is unknown and who has been informed. Do not soften a hazard into nothing serious or strengthen a location clue into an unsupported diagnosis.'),
    a='''Where is the water? | Outside washroom B, beside the east stair door | Inside washroom A | On the west stair landing | In an unidentified guest room | The brief supplies both the washroom identifier and the east-door landmark.
What does Ravi know about the source? | It is unknown | A pipe has definitely burst | A guest deliberately spilled it | The roof was repaired | Ravi has observed water but has not established its source.
What is the readiness status? | The affected area has not been declared ready | It is approved for reopening | Cleanup and inspection are complete | It is safe because a report exists | Reporting the condition does not establish completed controls or clearance.''',
    vocabulary='''observed condition | What the worker directly notices at the location. | report the observed condition
exact location | Specific place described with enough detail to identify it. | give the exact location
landmark | Recognizable feature used to locate another place. | name a clear landmark
washroom | Room containing toilet and washing facilities. | identify the washroom
stair door | Door providing access to a stairway. | identify the stair door
corridor | Passage connecting rooms or areas. | locate the corridor
threshold | Floor-level boundary at a doorway. | identify the threshold
stair landing | Level platform between flights or at a stair entrance. | describe the stair landing
visible water | Water that can be directly seen. | report visible water
source | Origin of the observed condition. | investigate the source
leak | Unintended escape of liquid from a system or container. | verify a suspected leak
slip hazard | Condition that may cause a person to slip. | report a slip hazard
trip hazard | Obstacle or condition that may cause a person to trip. | distinguish a trip hazard
affected area | Specific area involved in an incident or condition. | identify the affected area
site controls | Actual measures governing safety and access at a location. | follow site controls
hazard report | Message recording a potentially harmful condition. | submit a hazard report
maintenance referral | Transfer of a fault concern to the relevant maintenance team. | arrange a maintenance referral
fault diagnosis | Determination of the cause or nature of a defect. | avoid an unsupported fault diagnosis
status update | Report of the current state of the matter. | provide a status update
clearance | Required authorization that an area or item may return to the specified use. | await clearance
reopening | Making an area available again after the relevant controls and approval. | confirm reopening
readiness | State of being prepared and authorized for the specified next use. | verify readiness
report acknowledgement | Confirmation that the hazard message was received. | obtain report acknowledgement
follow-up owner | Person responsible for the next check or update. | name the follow-up owner''',
    precision='Outside washroom B and beside the east stair door locate the water. They do not establish that it came from the washroom or stairs. Keep the observed location separate from the unknown source.',
    precision_extra='Reported, assessed, cleaned, repaired, and cleared describe different stages. A received report cannot serve as reopening approval. Actual hazard controls and emergency arrangements take precedence over this language exercise.',
    phrases='''Lead with location | Water is visible outside washroom B.
Add the landmark | It is beside the east stair door.
State uncertainty | I do not know the source.
Avoid a diagnosis | I am not confirming a plumbing fault.
Confirm reporting | I have reported it under the site arrangements.
Preserve the status | The area has not been declared ready.
Ask for acknowledgement | Please confirm you have the correct location.
Correct direction | East stair door, not west.
Keep observations factual | I am reporting what I can see.
Avoid minimizing | I cannot describe it as harmless.
Keep controls active | The actual site controls still apply.
Request the next owner | Who is taking the follow-up?
Separate report and action | Receipt of the report does not mean the work is complete.
Avoid reopening language | I have no clearance to report.
Give a bounded update | The location is confirmed; the source remains unknown.
Close the message | Please keep the current status attached to that location.''',
    notes='''Outside versus inside | This contrast can direct a responder to the correct side of a doorway.
Beside | A landmark locates a condition without identifying its cause.
Visible | This describes direct observation, not a diagnosis or measurement.
Has not been declared | The phrase preserves the absence of authorized readiness.
Still | Use still to carry an unresolved status into the next message.
East versus west | Repeat direction explicitly when a similar landmark exists elsewhere.''',
    d='''Which message is most precise? | Water outside washroom B, beside the east stair door; source unknown. | Water somewhere near the toilets. | The east stair plumbing has definitely failed. | It is nothing serious. | The message supplies the exact location and preserves uncertainty about the source.
Which inference is not supported? | The water definitely comes from a broken pipe. | Water is visible on the floor. | The east stair door is a landmark. | The area is not declared ready. | An observed wet floor does not establish a particular plumbing cause.
What does report acknowledgement mean? | The message was received, not that the area is cleared | Cleanup is complete | Reopening is approved | The source is repaired | Acknowledgement confirms receipt only and must not be confused with operational clearance.
What should a follow-up preserve? | Location, observed condition, unknown source, and current readiness status | An invented cause to sound decisive | An all-clear because the supervisor answered | A promised repair time without checking | These four details maintain an accurate and usable report without unsupported conclusions.''',
    dialogue='''Elena | I have your report about water near the washrooms. Before I pass it on, please give me the exact location and current status.
Ravi | It is [[outside washroom B::Outside washroom B identifies the specific side and room, narrowing the location beyond a general washroom area.]], beside the east stair door. Water is visible on the floor there; I do not know where it came from.
Elena | Thank you. I want to be certain I heard the direction correctly. Is that the east stair door rather than the west one?
Ravi | Yes, the [[east stair door::East stair door is the supplied landmark and direction, preventing confusion with another stair entrance.]]. I am using it as the landmark for the location, not claiming that the water came from the stairway.
Elena | That distinction matters. Has anyone established a source, or is the message still limited to what you observed on the floor?
Ravi | The [[source::Source means the origin of the water, which has not been determined from the visible condition.]] remains unknown to me. I have not diagnosed a pipe, a drain, or any other cause from the location alone.
Elena | Have you already reported the condition through the site arrangements? I do not want this follow-up conversation to replace the required safety response.
Ravi | Yes, I have made the [[hazard report::Hazard report is the communication already made under site arrangements; it does not establish completed response or clearance.]] under those arrangements. The actual site controls still apply while the condition is being addressed.
Elena | Good. Please also state whether the affected area has been declared ready. I need to avoid passing on an accidental all-clear.
Ravi | There is no [[clearance::Clearance is the required authorization to return an area to the specified use; none is established here.]] for me to report. The area has not been declared ready, and my report should not be read as approval to use it.
Elena | Understood. I will keep that status in the message. Could you summarize the observation without adding a probable cause?
Ravi | The [[observed condition::Observed condition is the visible water at the named location, not a theory about how it arrived.]] is water on the floor outside washroom B, beside the east stair door. That is what I can state directly.
Elena | Some people may hear near the washroom and assume a plumbing leak. I will make clear that the source still needs appropriate assessment.
Ravi | Thank you. A [[fault diagnosis::Fault diagnosis requires a determination beyond this observation; the cleaner has not established a plumbing failure.]] has not been made by me. The location helps someone find the condition, but it does not prove what caused it.
Elena | I have the details now. Receiving them is one stage; it does not mean cleanup, repair, or any required inspection has finished.
Ravi | Exactly. Your [[report acknowledgement::Report acknowledgement confirms receipt of the information only, not completion of cleanup, repair, or inspection.]] tells me the message arrived. It should not be turned into a completed-work entry or a statement that the area is ready.
Elena | I will coordinate the follow-up through the site process and keep the responsible people informed. No reopening decision is being made in this exchange.
Ravi | Then I will keep the [[status update::Status update must preserve the current unresolved condition and absence of readiness rather than imply progress not established.]] factual: location confirmed, source unknown, area not declared ready. I will report any new observation through the same arrangements.
Elena | That is clear. Please retain the exact wording of the location when the next worker takes over, especially outside and east.
Ravi | I will. The [[affected area::Affected area identifies the particular location requiring continued attention; it must not be replaced by a vague building-wide statement.]] remains outside washroom B beside the east stair door. I will not replace that precise report with a guessed cause or an all-clear.''',
    transfer_title='Report a different wet-floor location',
    transfer_setup='Water is visible outside washroom D beside the west service door. The source is unknown. A report has been made, but the area has not been declared ready.',
    transfer='''Cleaner: "The water is outside washroom ___." | D | Washroom D is the exact room identifier in the new report.
Supervisor: "The landmark is the ___ service door." | west | West identifies the correct service door rather than another direction.
Cleaner: "The source remains ___." | unknown | The visible condition does not establish where the water originated.
Supervisor: "The area is not declared ___." | ready | Reporting the condition does not provide a readiness declaration or clearance.'''
))

BOOK['units'].append(unit(
    title='Handling found items and privacy questions',
    scene='The closed black case',
    skill='Describe found property without inspecting private contents, record its location, and confirm transfer to the designated receiver.',
    brief='After checkout, attendant Ana finds a closed black glasses case beneath the chair in room 214. The owner is unknown, and Ana does not open the case. Dev is the designated lost-property receiver and can accept it through the site procedure. The handover should record only established details and confirm receipt. A room number does not by itself identify the owner, and the appearance of a glasses case does not confirm what is inside. Any later ownership claim or release requires the actual verification process, not a guess during this conversation.',
    cast='Ana | Room attendant\nDev | Designated lost-property receiver',
    culture=('Careful description protects everyone', 'A found item can prompt curiosity or pressure to identify its owner quickly. Keep the report neutral and limited to the visible details needed for the task. A confirmed transfer is useful progress without inventing ownership or discussing a guest with someone who has no verified role.'),
    a='''Where was the case found? | Beneath the chair in room 214 | Inside the wardrobe in room 214 | Beneath a chair in room 241 | At an unidentified reception desk | Both the room number and the position beneath the chair are supplied.
What is known about the owner? | The owner is unknown | The last registered guest definitely owns it | Dev owns it | Ana has verified a claimant | No ownership verification is supplied, so the room location cannot identify the owner.
Who is the designated receiver? | Dev | Any caller who describes a black case | An unnamed visitor | The next guest automatically | Dev is specifically identified as the receiver under the site found-property process.''',
    vocabulary='''found property | Item discovered whose owner or custody needs appropriate handling. | report found property
lost-property receiver | Designated person who accepts found items under the site process. | contact the lost-property receiver
visible description | Account limited to details observable without inspecting hidden contents. | give a visible description
glasses case | Container designed for spectacles, regardless of its actual contents. | describe the glasses case
closed item | Item whose interior is not exposed or inspected. | preserve the closed item
contents | Items or material inside a container. | avoid guessing the contents
owner | Person with ownership of an item, requiring appropriate verification. | verify the owner
claimant | Person stating that an item belongs to them. | refer a claimant for verification
ownership claim | Statement that a person owns the item. | verify an ownership claim
find location | Place where an item was discovered. | record the find location
checkout | End-of-stay departure process for a guest. | distinguish checkout from ownership
property record | Entry documenting a found item and relevant handling details. | create a property record
item description | Identifying account of the item itself. | record the item description
transfer | Passing an item to the designated next holder. | document the transfer
receipt confirmation | Acknowledgement that the intended receiver has obtained the item. | obtain receipt confirmation
custody | Responsibility for holding an item at a given stage. | confirm custody
custody record | Record of who held or received an item through the process. | maintain the custody record
reference number | Identifier attached to a record or case. | record the reference number
privacy boundary | Limit on access to or disclosure of personal information. | respect the privacy boundary
disclosure | Sharing of information with another person. | avoid unauthorized disclosure
verified recipient | Person whose entitlement to receive the item has been established. | identify the verified recipient
release | Authorized handover to the person entitled to receive the item. | authorize release
site procedure | Required local process for handling the matter. | follow the site procedure
factual correction | Amendment that replaces an inaccurate detail with the verified fact. | make a factual correction''',
    precision='Found after checkout is a timing fact, not proof that the last guest owns the item. Record the room and location accurately while leaving ownership unknown until the actual process verifies it.',
    precision_extra='Glasses case describes the visible container. It does not prove glasses are inside. Keep the item closed in this scenario and transfer it to the designated receiver without turning a description into a search of private contents.',
    phrases='''Open the report | I found a closed black glasses case.
Give the room | It was in room 214.
Give the position | It was beneath the chair.
State timing | I found it after checkout.
Preserve uncertainty | I do not know the owner.
Avoid a contents claim | I have not opened it, so I cannot describe what is inside.
Identify the receiver | Are you the designated lost-property receiver?
Request transfer | I need to hand this over through the site procedure.
Ask for receipt | Please confirm when you have received the item.
Repeat the description | Closed black glasses case, beneath the chair, room 214.
Separate custody and ownership | Receiving it does not identify its owner.
Protect privacy | I cannot share guest details with an unverified caller.
Route a claim | Ownership claims need the actual verification process.
Avoid release by guess | A room number alone is not release authorization.
Correct a number | The room is 214, not 241.
Close the handover | The transfer is recorded; ownership remains unverified.''',
    notes='''Found versus owned | Finding an item in a room does not prove who owns it.
Beneath | This gives a specific position rather than a vague room-level description.
Closed | Include this visible condition without asserting what the item contains.
Received versus released | Staff receipt and return to a verified owner are different handovers.
Unknown | Use unknown where no ownership evidence has been established.
After checkout | This describes when the discovery occurred, not who left the item.''',
    d='''Which description is supported? | Closed black glasses case beneath the chair in room 214 | Prescription glasses belonging to the last guest | An empty case confirmed by opening it | A valuable item with a known owner | The supported description stays within visible details and the stated location.
What does Dev's receipt establish? | Transfer to the designated receiver | Verified ownership by a guest | Authorization for public disclosure | Completed return to the owner | Receipt confirms custody transfer, not ownership verification or final release.
Which statement exceeds the evidence? | It must belong to the last person who stayed in the room. | It was found after checkout. | The case is black and closed. | The owner is unknown. | Room location and checkout timing do not establish the item's owner.
What should happen to a later claim? | Follow the actual ownership-verification and release process | Release immediately based only on room number | Share all guest information with the caller | Open the case out of curiosity | A claim needs the designated process rather than an unsupported assumption or disclosure.''',
    dialogue='''Ana | I have found an item after checkout in room two hundred fourteen. I need to pass it to the designated lost-property receiver.
Dev | I am the [[lost-property receiver::Lost-property receiver identifies Dev's designated role in accepting the item through the site process, not ownership of it.]] for this handover. Please give me the visible description and exact find location before we record the transfer.
Ana | It is a closed black glasses case. I found it beneath the chair, and I have not opened it or inspected anything inside.
Dev | I will record that [[visible description::Visible description is limited to the closed black case and does not claim knowledge of its contents.]] without adding a contents description. A case designed for glasses does not prove what is actually inside it.
Ana | Correct. Please also keep the room number as two hundred fourteen. It could easily be confused with two hundred forty-one if someone writes it quickly.
Dev | I have the [[find location::Find location records room 214 and the position beneath the chair, helping identify the discovery accurately.]] as beneath the chair in room 214. I will read that back before finishing the entry.
Ana | That is right. It was found after checkout, but I do not know who owns it. I do not want to attach a guest name by guessing.
Dev | We will keep [[ownership::Ownership remains unverified; discovery in a room after checkout does not establish who owns the item.]] unverified. The room and timing are useful facts, but they are not a completed identification of the person entitled to receive it.
Ana | Thank you. I can hand the closed case to you through the normal process now. Please confirm when it is actually in your custody.
Dev | I have received the case. That is the [[receipt confirmation::Receipt confirmation establishes that Dev actually received the item, not merely that a transfer was proposed.]] for this transfer. The record should show the real handover rather than an intention to pass it on later.
Ana | Good. I will not describe that as returned to the guest, because we have only moved it to the designated staff receiver.
Dev | Exactly. The [[custody record::Custody record tracks who holds the item; a staff transfer does not mean it has been returned to a verified owner.]] describes this staff handover. Any later return is a separate event with its own verification and recording requirements.
Ana | Suppose someone later says they stayed in that room and asks whether we found anything. I should route that query through the actual process, correct?
Dev | Yes. An [[ownership claim::Ownership claim is a person's assertion, which must be verified through the actual process rather than accepted from a room number alone.]] needs appropriate verification. We should not release an item simply because a caller supplies a room number or sounds confident.
Ana | And I should not discuss another guest's details while trying to help the caller. That would go beyond the information needed for this handover.
Dev | Correct. Keep the [[privacy boundary::Privacy boundary limits unnecessary or unauthorized disclosure of guest information during a found-property query.]] clear and use the designated process. Helpful service does not require giving an unverified caller someone else's personal information.
Ana | Could you repeat the entry once, so I can confirm that the location and the fact that I kept the case closed are both included?
Dev | The [[property record::Property record captures the established item details and handling facts without inventing contents, ownership, or final release.]] says closed black glasses case, found beneath the chair in room 214 after checkout, not opened by you, received by me.
Ana | That matches what happened. The staff transfer is complete, and we still do not have a verified owner or an authorized return to report.
Dev | Agreed. No [[release::Release is the separate authorized return to an entitled recipient; the completed staff receipt does not establish it.]] to a claimant has occurred. We have completed and recorded the custody transfer while leaving the unresolved ownership question accurately open.''',
    transfer_title='Record a different found item',
    transfer_setup='A closed navy pouch is found on the desk in room 318 after checkout. Its owner is unknown. Designated receiver Rosa confirms receiving it unopened.',
    transfer='''Attendant: "The item is a closed navy ___." | pouch | Pouch is the visible container supplied in the new scenario.
Receiver: "The find location is the ___." | desk | The desk is the specific location where the pouch was found.
Attendant: "The room number is ___." | 318 | Room 318 is the recorded room, not an ownership verification.
Receiver: "The owner remains ___." | unknown | Confirmed staff receipt does not establish who owns the item.'''
))

BOOK['units'].append(unit(
    title='Counting linen and replenishing supplies',
    scene='Three bath towels short',
    skill='Report linen counts by item, calculate the exact shortfall, and separate expected delivery from stock on hand.',
    brief='The third-floor cart target is twelve bath towels and eight hand towels. Attendant Noor counts nine bath towels and eight hand towels. A laundry delivery is expected but its arrival and contents are not confirmed. Supply lead Ben needs an item-specific report and a request for three additional bath towels, not a statement that all linen is unavailable. No delivery has been received or counted. The target is a cart-stock requirement, not a claim about the number of occupied rooms or a reason to substitute one towel type for another.',
    cast='Noor | Room attendant\nBen | Supply lead',
    culture=('Specific shortages are easier to solve', 'A broad statement such as we have no linen can cause unnecessary disruption. Name the cart, the towel type, the target, and the counted amount. Keep expected supplies out of the current count until the actual receipt and checks occur.'),
    a='''What is the bath-towel shortfall? | Three | Nine | Twelve | Zero | The target of twelve minus the counted nine leaves three bath towels.
What is the hand-towel status? | Eight counted against a target of eight | All hand towels missing | Three short | Delivery needed to establish the current count | The hand-towel count already matches its specified target.
What is known about the delivery? | It is expected but not confirmed | It has arrived with three bath towels | Its full contents were counted | It guarantees the cart is complete | Neither arrival nor contents are confirmed, so expected stock cannot close the shortfall.''',
    vocabulary='''linen | Textile items used in housekeeping, such as towels and bedding. | count the linen
bath towel | Larger towel intended for drying the body after bathing. | replenish bath towels
hand towel | Smaller towel intended primarily for drying hands. | count hand towels
bath mat | Textile or other item used on the floor near bathing facilities. | identify the bath mat
pillowcase | Cover used over a pillow. | replenish pillowcases
duvet cover | Removable fabric cover for a duvet. | count duvet covers
flat sheet | Unfitted bed sheet without shaped elastic corners. | identify a flat sheet
fitted sheet | Sheet designed to fit around a mattress. | check fitted-sheet stock
linen cart | Mobile storage unit carrying linen supplies. | replenish the linen cart
floor allocation | Supplies assigned to a particular building floor. | check the floor allocation
stock target | Quantity specified as the desired amount on hand. | confirm the stock target
par level | Planned stock level used for replenishment decisions. | compare with par level
physical count | Quantity actually counted at the location. | complete a physical count
stock on hand | Supplies currently present, not merely expected. | report stock on hand
shortfall | Amount by which the current count is below the target. | calculate the shortfall
item type | Category of supply that must remain distinct in the count. | specify the item type
replenishment request | Request to restore the required stock. | submit a replenishment request
laundry delivery | Transfer of linen from the laundry supply process. | check the laundry delivery
expected delivery | Delivery anticipated but not yet confirmed as received. | distinguish an expected delivery
confirmed receipt | Established arrival and acceptance under the relevant process. | record confirmed receipt
delivery contents | Items and quantities actually included in a delivery. | verify delivery contents
count discrepancy | Difference between a recorded or expected amount and a checked count. | report a count discrepancy
substitution | Replacement of one item type with another under the required approval. | avoid an unapproved substitution
stock update | Revised statement of actual inventory after a verified change. | provide a stock update''',
    precision='Bath towels: target twelve, counted nine, short three. Hand towels: target eight, counted eight, no numerical shortfall. Keep item types separate even when giving a combined cart total.',
    precision_extra='Expected delivery is not stock on hand. The delivery may need arrival, contents, and other required checks before the cart record changes. Do not convert an anticipated delivery into a completed replenishment.',
    phrases='''Identify the cart | This is the third-floor linen cart.
State the target | The target is twelve bath towels.
Give the count | I counted nine bath towels.
Calculate the gap | We are three bath towels short.
Report the second item | Hand towels are eight against a target of eight.
Avoid overstatement | The shortage is not across all linen.
Request the exact amount | Please arrange three additional bath towels.
Preserve uncertainty | The laundry delivery is expected but not confirmed.
Keep future stock separate | I have not added expected items to the current count.
Ask about receipt | Has the delivery actually arrived and been checked?
Clarify contents | Do we know what the delivery contains?
Reject a silent substitute | Hand towels are not an assumed replacement for bath towels.
Update after verification | I will revise the count after the actual receipt and checks.
Keep the unit visible | Three bath towels, not three carts or packs.
Name the remaining need | The bath-towel shortfall remains open.
Close the count report | Nine bath towels and eight hand towels are currently counted.''',
    notes='''Against | Nine against twelve compares actual stock with the target.
Short by | Short by three describes the missing amount, not the amount present.
On hand | This means actually available in the stated location.
Expected | Expected is weaker than arrived, received, or counted.
Additional | Three additional bath towels would fill the numerical gap if actually received and accepted.
By item | Separate categories prevent a correct total from hiding the wrong mix.''',
    d='''Which report is best? | Nine of twelve bath towels; eight of eight hand towels; three bath towels short. | We have no linen. | We are twelve towels short. | The expected delivery completes the cart. | The report preserves each item count, target, and exact numerical shortage.
Why not count the expected delivery? | Its arrival and contents are unconfirmed. | Deliveries can never replenish stock. | Hand towels must replace every missing item. | The target has automatically changed. | Anticipation does not establish that the needed items are present and checked.
Which request matches the shortfall? | Three additional bath towels | Twelve additional hand towels | Eight additional bath towels | Three unspecified containers | Three bath towels fill the difference between the target and current count.
What does the cart target establish? | A required stock mix, not the number of occupied rooms | Twelve occupied rooms | Eight guests on the floor | Permission to substitute any linen | The target specifies cart quantities and does not supply occupancy or substitution authority.''',
    dialogue='''Noor | I have counted the third-floor linen cart. The bath towels are below target, but the hand towels match their target.
Ben | Please give me the [[physical count::Physical count is the quantity actually observed on the cart, which must remain separate from expected delivery stock.]] and the target for each type. I want the item-specific figures before arranging replenishment.
Noor | The target is twelve bath towels, and I counted nine. For hand towels, the target is eight and the count is also eight.
Ben | That gives a [[shortfall::Shortfall is the difference between the bath-towel target of twelve and the actual count of nine.]] of three bath towels. The hand towels have no numerical gap against their target, so the two categories need different status messages.
Noor | Exactly. I do not want the handover to say the whole floor has no linen, because that would not describe what I counted.
Ben | We should name the [[linen cart::Linen cart locates this count on the third floor; the report does not establish inventory for the entire building.]] and the two item types. This is the third-floor cart report, not a claim about every cupboard or every floor.
Noor | A laundry delivery is expected, but I have not seen it arrive. I also do not know the quantities or items it will contain.
Ben | Then it remains an [[expected delivery::Expected delivery describes anticipated supply, not confirmed arrival, checked contents, or completed replenishment.]]. We cannot use it to close the bath-towel shortage until the actual supply and relevant checks are established.
Noor | I have kept it out of the current count. I do not want to report twelve just because a delivery may be on the way.
Ben | Correct. [[Stock on hand::Stock on hand is the actual supply present now; future or unconfirmed items must not be included.]] remains nine bath towels and eight hand towels. An expected arrival is useful planning information, but it is not counted stock.
Noor | Please arrange three more bath towels for this cart. I mean individual bath towels, not three packs with an unknown quantity in each.
Ben | I will make the [[replenishment request::Replenishment request specifies three additional bath towels and preserves the individual-item unit needed to fill the gap.]] for three additional bath towels. Keeping the unit explicit prevents us from ordering or recording an unintended quantity.
Noor | Should we describe the hand towels as an alternative? There are eight here, but those eight already match their own target.
Ben | No [[substitution::Substitution would replace one item type with another; the count supplies no approval to use hand towels for the bath-towel shortage.]] has been approved. A hand towel and a bath towel are different stock items, and the present count does not authorize changing the required mix.
Noor | Understood. When the delivery does arrive, I will need to check what it actually includes rather than assume it contains the missing bath towels.
Ben | Yes, verify the [[delivery contents::Delivery contents identify the actual items and quantities supplied; an arrival alone does not prove the required bath towels are included.]] through the normal process. An arrival by itself does not establish that the three needed bath towels are in it.
Noor | Until then, the shortage stays open. I can give another update after the actual receipt and checks, using the resulting count.
Ben | That is when the [[stock update::Stock update should reflect a verified change in actual quantities, not a prediction about an unconfirmed delivery.]] should change the recorded figures. We should preserve the earlier count rather than retroactively pretend the cart was already full.
Noor | My final read-back is third-floor cart: nine bath towels against twelve, eight hand towels against eight, with three bath towels still needed.
Ben | Agreed. The [[stock target::Stock target specifies the required cart mix; it is not evidence about occupied rooms or completed replenishment.]] remains twelve and eight respectively. The delivery is expected, not confirmed, and the request is for three additional bath towels.''',
    transfer_title='Calculate another linen shortfall',
    transfer_setup='The second-floor cart target is ten bath towels and six hand towels. The count is seven bath towels and six hand towels. A delivery is expected but not confirmed.',
    transfer='''Attendant: "The bath-towel target is ___." | ten | Ten is the required bath-towel stock for this cart.
Lead: "The counted bath towels total ___." | seven | Seven is the physical bath-towel count supplied in the scenario.
Attendant: "We need ___ additional bath towels." | three | Ten required minus seven present leaves three bath towels missing.
Lead: "The hand-towel count is ___." | six | Six hand towels are present and match their separate target.'''
))

BOOK['units'].append(unit(
    title='Responding to a quality concern',
    scene='Streaks beside office 8',
    skill='Acknowledge a reported result, identify the exact surface, and arrange a check without inventing the cause or outcome.',
    brief='Client Dana reports streaks on the interior glass panel beside office 8, which was cleaned earlier today. Cleaner Malik has not yet checked the reported area with the client. Dana is available to point out the panel. Lead Rosa can arrange a check and appropriate rework through the site process. The cause is unknown, and no rework or final inspection is complete. Malik needs to acknowledge the concern, locate it precisely, and explain the next step without denying the report, blaming someone, or promising a result and time that have not been verified.',
    cast='Dana | Client contact\nMalik | Cleaner',
    culture=('Acknowledge the result before explaining the process', 'Saying we already cleaned it may sound like a refusal to listen. Recognize the reported concern first, then clarify the surface and arrange the check. An acknowledgement does not require guessing a technical cause or admitting a fault that has not been established.'),
    a='''Which surface is reported? | Interior glass panel beside office 8 | Exterior window above office 8 | Every glass surface in the building | The floor inside office 18 | The brief identifies the interior panel and its location beside office 8.
What is known about the cause? | It is unknown | Wrong product is confirmed | The client caused the streaks | Permanent damage is established | The report identifies a result but does not establish its cause.
What can Dana do now? | Point out the panel | Authorize every chemical procedure | Confirm completed rework | Supply a finished inspection result | Dana is available to identify the relevant panel, while checking and rework remain pending.''',
    vocabulary='''quality concern | Report that a result may not meet the required standard. | acknowledge a quality concern
streak | Visible line or mark remaining across a surface. | report streaks on glass
smear | Spread or blurred mark on a surface. | describe a smear
residue | Material remaining after an activity or substance has been removed. | identify residue
haze | Cloudy appearance that reduces surface clarity. | describe a haze
scratch | Mark or damage caused by abrasion or contact. | distinguish a scratch from residue
interior glass | Glass surface on the inside of a building or assembly. | identify interior glass
glass panel | Defined sheet or section of glass. | locate the glass panel
partition | Structure dividing areas within a space. | identify the partition
frame | Surrounding support or border of a panel. | distinguish the frame from glass
edge | Boundary of a surface or object. | identify the affected edge
finish | Visible or specified final condition of a surface. | assess the finish
inspection | Examination against the relevant requirements. | arrange an inspection
rework | Additional work to correct a result that does not meet requirements. | arrange appropriate rework
verification check | Check that the specified result has actually been achieved. | complete a verification check
reported result | Outcome described by the person raising the concern. | acknowledge the reported result
direct observation | Information obtained by seeing or otherwise directly checking the matter. | distinguish direct observation
cause analysis | Investigation of why a result occurred. | separate cause analysis from acknowledgement
service standard | Required level or condition of the provided service. | check the service standard
client feedback | Information from the client about the service received. | receive client feedback
follow-up arrangement | Agreed method or responsibility for the next action. | confirm a follow-up arrangement
completion claim | Statement that work has been finished. | avoid an unsupported completion claim
resolution | Established outcome that addresses the issue through the actual process. | confirm resolution
update commitment | Promise to provide information about progress, not a guaranteed result. | make an update commitment''',
    precision='Streaks are the reported result. They do not prove the wrong product, permanent damage, or who caused the problem. Acknowledge the report and identify the panel before discussing what the actual check establishes.',
    precision_extra='Cleaned earlier is a past activity, not proof of the present finish. Rework arranged, rework completed, and result verified are different stages. Report the real stage without promising a perfect finish or an unchecked completion time.',
    phrases='''Acknowledge the concern | Thank you for pointing out the streaks.
Recognize the inconvenience | I am sorry the result is not as expected.
Identify the panel | Is it the interior glass beside office 8?
Ask for a precise indication | Could you point out the affected area?
Avoid dismissing the report | The earlier cleaning does not answer your concern about the current result.
Separate the cause | I do not know what caused the marks yet.
Involve the lead | I will ask Rosa to arrange a check.
Explain the next stage | The check will establish what appropriate rework is needed.
Avoid a guessed remedy | I will not choose a method before the relevant assessment.
Keep status accurate | Rework has not been completed yet.
Avoid a time promise | I do not have a checked completion estimate.
Preserve the location | Interior panel beside office 8, not the exterior window.
Acknowledge availability | Thank you for being available to show us the panel.
Promise an update | I will pass on the checked next step.
Separate done and verified | A completion report still needs the required verification.
Close the response | I have the concern and location; Rosa will receive the follow-up request.''',
    notes='''Reported | This attributes the observation accurately when the worker has not yet checked it.
Earlier today | A time reference does not establish the present quality of the result.
Beside | Keep the location relation precise, especially around numbered offices.
Arrange versus complete | Arranging rework does not mean the corrective work has happened.
Yet | The cause is unknown yet; do not fill the gap with blame.
Sorry | An apology for inconvenience need not invent a diagnosis or technical admission.''',
    d='''Which opening is most useful? | Thank you for pointing it out; could you show me the interior panel beside office 8? | We cleaned it, so there cannot be streaks. | You must have touched it. | The glass is permanently damaged. | The response acknowledges the concern and seeks an exact location without a guessed cause.
What does cleaned earlier establish? | A past cleaning activity, not verified current quality | Guaranteed absence of marks | Completed rework after the complaint | A confirmed product error | The earlier activity does not by itself settle the present reported result.
Which next step fits the brief? | Ask Rosa to arrange a check and appropriate rework | Promise a perfect finish in five minutes | Select a chemical method without assessment | Mark the complaint resolved immediately | Rosa is the named lead who can arrange the required check and response.
Which statement falsely closes the issue? | The panel is now verified clear because the client reported it. | Dana can point out the panel. | The cause remains unknown. | The follow-up needs a check. | A report supplies a concern, not evidence of completed correction or verification.''',
    dialogue='''Dana | There are streaks on the glass beside office eight. I know it was cleaned earlier today, but the result still does not look right.
Malik | Thank you for pointing out the [[quality concern::Quality concern acknowledges the reported unsatisfactory result without denying it because cleaning was performed earlier.]]. I am sorry the result is not as expected. Could you show me which panel and area you mean?
Dana | It is the interior panel beside the office, not the outside window. I can point it out when someone comes to check.
Malik | I will keep [[interior glass::Interior glass distinguishes the reported panel from an exterior window, helping the team inspect the correct surface.]] in the description. Beside office eight is the location, and I understand you are available to show the affected part.
Dana | Yes. I am not asking you to guess why it happened. I just want someone to look at the streaks and deal with them appropriately.
Malik | Understood. The [[reported result::Reported result attributes the streaks to the client's observation while the cleaner has not yet completed a direct check.]] is streaking on that panel. I have not yet checked it with you, and I do not know the cause.
Dana | Someone might tell me it has already been cleaned. That would not really answer the concern I am raising about how it looks now.
Malik | I agree. Earlier cleaning is an activity, not a completed [[verification check::Verification check would establish the actual result against requirements; a past cleaning activity does not replace it.]] of the present finish. Your concern still needs the appropriate follow-up.
Dana | Who can arrange that follow-up? I would like to know where the request is going rather than repeat it to several different people.
Malik | Rosa is our lead. I will ask her to arrange an [[inspection::Inspection is the next examination needed to establish the condition and appropriate response, not a completed correction.]] of the identified panel and the appropriate rework through the site process.
Dana | Thank you. Please do not tell her I said the glass was scratched. I said there were streaks, and I do not know more than that.
Malik | I will preserve [[streaks::Streaks is the actual reported description; changing it to scratches would add an unsupported claim of damage.]] as the description. I will not change your report into a claim of permanent damage or a particular product fault.
Dana | That is important. Can you give me a time for the correction, or does the lead need to check the current schedule first?
Malik | I do not have a checked completion estimate. I can make an [[update commitment::Update commitment promises communication of checked progress rather than an unsupported completion time or guaranteed finish.]] to pass on the next step, but I should not invent a finishing time.
Dana | That is reasonable. I would rather receive a realistic update than be told it is fixed before anyone has looked at the panel.
Malik | Yes. [[Rework::Rework is corrective work that may be arranged after the check; it has not already been completed in this exchange.]] needs to be appropriate to the checked condition and actual site requirements. Arranging it is not the same as completing it.
Dana | Please also keep the location precise when you report it. We have several panels nearby, and I do not want the wrong one checked.
Malik | The [[follow-up arrangement::Follow-up arrangement connects the correct panel and concern with Rosa's check, while preserving the client's availability to identify it.]] will name the interior glass panel beside office eight. I will include that you can point out the area with the reported marks.
Dana | Good. I have given you the concern and can help identify it. I am waiting for the check and the appropriate response, not a guess.
Malik | Thank you. I will not report [[resolution::Resolution requires an established outcome addressing the concern; receiving the complaint and arranging a check do not themselves resolve it.]] before the work and required verification are complete. For now, I am passing the accurate concern and location to Rosa.''',
    transfer_title='Respond to another reported finish',
    transfer_setup='A client reports smears on the interior panel beside office 12. Lead Ben can arrange a check. The cause is unknown, and no rework has been completed.',
    transfer='''Cleaner: "The reported marks are ___." | smears | Smears is the client's description and should not become an invented diagnosis.
Client: "The panel is beside office ___." | 12 | Office 12 is the specific location supplied for the concern.
Cleaner: "The lead for the check is ___." | Ben | Ben is the named person who can arrange the follow-up.
Cleaner: "The cause remains ___." | unknown | The report establishes a concern but not its technical cause.'''
))

BOOK['units'].append(unit(
    title='Giving a clear end-of-shift handover',
    scene='Three rooms, different stages',
    skill='Report each room status separately, assign the unfinished steps, and avoid confusing cleaning with inspection or release.',
    brief='At the end of the shift, attendant Tessa hands over rooms 301, 302, and 303 to incoming attendant Arun. Rooms 301 and 302 have been cleaned. Room 302 still awaits inspection by supervisor Rosa. Room 303 was inaccessible and has not been cleaned. Arun can accept the access follow-up for 303; Rosa owns the inspection of 302. The handover does not establish room-release decisions or an inspection result for 301. No new room entry, completed inspection, or completed cleaning of 303 occurs during this conversation.',
    cast='Tessa | Outgoing room attendant\nArun | Incoming room attendant',
    culture=('Precision survives a shift change', 'A short list can carry more useful information than a general all done message. Repeat each room number with its actual stage and the person responsible for the next step. Receiving the list should make ownership clear without upgrading an unfinished status.'),
    a='''Which rooms have been cleaned? | 301 and 302 | All three rooms | Only 303 | No rooms | The brief establishes cleaning of 301 and 302, but not of inaccessible 303.
What remains for 302? | Rosa's inspection | Cleaning confirmed as never started | A guest-release decision already made | Arun's access follow-up for 303 | Room 302 is cleaned and specifically awaits the supervisor's inspection.
What is the status of 303? | Inaccessible and not cleaned; access follow-up can pass to Arun | Cleaned and inspected | Released to a guest | Automatically accessible after handover | Inaccessibility prevented cleaning, and the handover assigns follow-up rather than changing that fact.''',
    vocabulary='''room status | Current recorded state of a guest room. | report room status
cleaned | Cleaning task completed, distinct from later inspection or release. | mark the room cleaned
awaiting inspection | Cleaning completed but the required inspection not yet performed. | retain awaiting-inspection status
inaccessible | Not available for authorized entry or work at the relevant time. | report an inaccessible room
not cleaned | Cleaning has not been carried out. | preserve not-cleaned status
room release | Authorization making a room available for the intended use. | verify room release
inspection owner | Person responsible for the pending inspection. | name the inspection owner
access follow-up | Task of checking and resolving access through the actual procedure. | accept an access follow-up
room-status board | Shared display or record of room stages. | update the room-status board
handover log | Record of transferred work and current status. | maintain the handover log
outgoing shift | Team or work period passing responsibility onward. | brief the outgoing shift
incoming shift | Team or work period taking over responsibility. | brief the incoming shift
outstanding task | Required work that remains unfinished. | identify an outstanding task
task acceptance | Agreement to take responsibility for a task. | confirm task acceptance
completion evidence | Information establishing that work actually occurred. | require completion evidence
status transition | Change from one recorded stage to another after the relevant event. | verify a status transition
inspection result | Actual finding or outcome of the room check. | record the inspection result
release authority | Person or process entitled to authorize the next use. | confirm release authority
access restriction | Condition limiting entry or work in an area. | preserve an access restriction
room identifier | Number or other detail distinguishing the room. | repeat the room identifier
follow-up priority | Relative order or urgency assigned to unfinished tasks. | clarify follow-up priority
exception report | Record of a task or condition outside the expected completed state. | submit an exception report
carryover work | Unfinished work transferred to the next shift. | track carryover work
separate status | Distinct recorded state for each room or task. | preserve separate statuses''',
    precision='Cleaned is not a synonym for inspected or released. Room 302 illustrates the difference: cleaning is complete, but inspection is pending. Room 303 has not been cleaned at all because access was unavailable.',
    precision_extra='The handover supplies only a cleaned status for room 301. Do not invent either a passed inspection or a failed one. A room-release decision must come from the actual authorized process, not from the absence of a problem in a short report.',
    phrases='''Start the room list | I have separate updates for 301, 302, and 303.
State the first fact | Room 301 has been cleaned.
Avoid an invented result | I have no inspection result for 301 to add.
State the second stage | Room 302 is cleaned and awaiting inspection.
Name the inspection owner | Rosa owns the inspection for 302.
State the access issue | Room 303 was inaccessible.
Preserve the consequence | Room 303 has not been cleaned.
Assign follow-up | Can you take the access follow-up for 303?
Accept without overclaiming | I accept the follow-up; access is not resolved yet.
Keep entry separate | The actual access procedure still applies.
Avoid automatic release | This handover does not authorize room release.
Repeat the unfinished work | Inspection for 302 and access follow-up for 303 remain open.
Update by event | Change the status only when the relevant work or decision occurs.
Keep room numbers attached | Please record each stage against the correct room.
Confirm the record | The handover log should match these separate statuses.
Close with ownership | Rosa has the inspection; you have the access follow-up.''',
    notes='''Cleaned versus ready | Ready may imply more than cleaning; name the actual completed stage.
Awaiting | Awaiting inspection explicitly identifies a pending next step.
Was inaccessible | This explains the earlier condition but does not prove present access has changed.
Accepted versus completed | A receiving worker can accept responsibility while work remains unfinished.
No result supplied | Missing information is not evidence of either passing or failing an inspection.
Separate entries | Keep each room number attached to its own state and next owner.''',
    d='''Which summary is accurate? | 301 cleaned; 302 cleaned, inspection pending; 303 inaccessible and not cleaned. | All three rooms ready. | 303 cleaned because Arun accepted it. | 302 inspected because Rosa is responsible. | The summary preserves the distinct completed and unfinished stages for each room.
What does Arun accept? | Access follow-up for 303 | Authority to release every room | A completed inspection result for 302 | Proof 303 is already clean | Arun accepts responsibility for checking access, not completed cleaning or room-release authority.
What can be said about 301's inspection? | No result is supplied in this handover. | It definitely passed. | It definitely failed. | Arun automatically inspected it while listening. | The brief supplies cleaned status only and does not establish any inspection outcome.
When should a status change? | After the relevant actual work or authorized decision | As soon as a new shift arrives | When someone repeats the room number | Before the required inspection to save time | Status records should follow real events and permissions rather than expectations or shift changes.''',
    dialogue='''Tessa | Before I finish, I need to hand over three rooms with different statuses. Please do not combine them into a single all-done entry.
Arun | I am ready to take the [[handover log::Handover log records the separate room states and next tasks, rather than treating the end of a shift as completion.]] details. Give me each room number with what has actually happened and what remains for the next person.
Tessa | Room three hundred one has been cleaned. I have no inspection result or room-release decision to add to that statement.
Arun | I will record [[cleaned::Cleaned is the established stage for room 301; no inspection result or release decision should be added.]] for 301 without inventing another stage. The absence of an inspection result in this message does not mean I can assume one.
Tessa | Room three hundred two has also been cleaned, but it still awaits Rosa's inspection. That unfinished step needs to remain visible.
Arun | So 302 is [[awaiting inspection::Awaiting inspection preserves the pending check after cleaning, distinguishing room 302 from an inspected or released room.]], with cleaning complete. I will keep that distinction on the room-status record instead of shortening it to ready.
Tessa | Exactly. Rosa remains responsible for that inspection. I am not transferring the inspection to you merely because you are receiving this handover.
Arun | Rosa is the [[inspection owner::Inspection owner identifies Rosa's responsibility for room 302; receiving a handover does not automatically transfer that task.]]. I can carry the status forward, but I should not report that she has already completed the check.
Tessa | Room three hundred three was inaccessible, so it has not been cleaned. Can you take the access follow-up through the actual procedure?
Arun | Yes, I accept the [[access follow-up::Access follow-up is the task Arun accepts for room 303; it is not authorization for immediate entry or proof of cleaning.]] for 303. That means I will address the access question through the proper route, not enter just because the shift has changed.
Tessa | Thank you. Please keep not cleaned on the record until the work has really happened. The access issue explains why it was unfinished.
Arun | I will preserve the [[not cleaned::Not cleaned is room 303's actual cleaning state; accepting an access task does not change it.]] status. A planned follow-up is not completion evidence, and I will not upgrade the room based on an intention.
Tessa | Good. If someone asks whether all three rooms can be released, this handover alone does not supply that decision for any of them.
Arun | Understood. [[Room release::Room release is a separate authorized decision, which cannot be inferred from cleaning, task acceptance, or this handover alone.]] belongs to the actual authorized process. I will not substitute our conversation for the required inspection or release decision.
Tessa | Could you repeat the two unfinished tasks and their owners? I want to be sure they remain separate when you update the shared record.
Arun | Rosa has the inspection for 302; I have the access follow-up for 303. That is my [[task acceptance::Task acceptance confirms Arun's responsibility for the access follow-up while leaving the inspection with Rosa and both tasks unfinished.]], not a report that either outstanding task is finished.
Tessa | That is accurate. Room 301 is reported cleaned only. Please do not borrow 302's inspection status and apply it to 301 without information.
Arun | I will keep a [[separate status::Separate status maintains a distinct evidence-based entry for each room instead of copying another room's stage or assuming all are alike.]] for each room. Shared numbering does not make the stages identical, and an unknown result should remain unknown.
Tessa | Thank you. Once the actual follow-up or inspection happens, the person handling it can provide the real outcome for the correct room.
Arun | Yes. Each [[status transition::Status transition should follow the actual task result or authorized decision, not the arrival of a new shift or a repeated promise.]] will follow the relevant event. For now: 301 cleaned, 302 cleaned and awaiting Rosa's inspection, 303 inaccessible and not cleaned, with access follow-up assigned to me.''',
    transfer_title='Hand over another room sequence',
    transfer_setup='Room 410 is cleaned. Room 411 is cleaned and awaits inspection by Ben. Room 412 was inaccessible and is not cleaned. Incoming attendant Jo accepts the access follow-up for 412.',
    transfer='''Outgoing: "The room awaiting inspection is ___." | 411 | Room 411 is cleaned but still requires its identified inspection.
Incoming: "The inspection owner is ___." | Ben | Ben is named as responsible for the pending room inspection.
Outgoing: "The inaccessible, uncleaned room is ___." | 412 | Room 412 has not been cleaned because access was unavailable.
Incoming: "The access follow-up has been accepted by ___." | Jo | Jo accepts the follow-up, which does not establish completed access or cleaning.'''
))
