"""Original learner-book content for construction and architecture."""
from books.authoring import unit

BOOK = dict(
    slug='construction-architecture',
    title='Construction and Architecture English',
    cover_label='ENGLISH FOR THE BUILT ENVIRONMENT',
    cover_title='Construction\nand Architecture',
    cover_size=30,
    tagline='Clarify the intent. Coordinate the work. Document the decision.',
    audience='For architectural, construction, project coordination, and site-administration teams.',
    map_intro='Eight project exchanges: define a room brief, resolve a document discrepancy, qualify a change proposal, update a critical sequence, clarify a safety instruction, report inspection status, hand over a punch list, and separate a delay record from a claim.',
    notes_title='Make the project meaning explicit',
    notes_intro='Construction language connects drawings, physical work, money, time, and responsibility. A small change from requested to approved can change what a colleague believes they may do. These cases practice the distinctions that keep a conversation tied to its evidence.',
    field_notes=[
        ('Replace adjectives with requirements', 'Flexible and high quality can conceal different expectations. Identify the users, activities, quantities, constraints, and performance the client actually needs before treating a preference as a settled design.', '"Do you need two seating arrangements, or simultaneous activities in separate areas?"'),
        ('Identify the document and its status', 'A sheet number alone may not identify the information used on site. Give its revision, the affected location, and the conflicting requirement; request clarification without assuming one document always takes precedence.', '"Drawing A601 revision C and specification S09 revision B disagree at Room 205."'),
        ('Separate proposals from instructions', 'A request for pricing, an estimated effect, an agreed change, and permission to proceed are different things. Use the project contract and authority arrangements, not an informal expression of enthusiasm, to establish status.', '"The partition is priced as a proposal; no instruction to proceed has been issued."'),
        ('Make evidence transferable', 'An incoming colleague needs more than a percentage or a green status. Connect the item, location, action, responsible person, and supporting record so that the next review can continue without reconstructing the conversation.', '"Items 1 to 3 are verified closed; the other five still need review."')],
    scope_note='All projects, figures, people, and local processes are fictional. This book teaches workplace English, not design, legal, construction, code-compliance, or safety practice. Actual contracts, adopted codes, qualified professionals, and site procedures govern the work. No exercise authorizes construction or occupancy.',
    sources=[
        dict(title='AIA Contract Documents. G716-2004: Request for Information instructions.', url='https://help.aiacontracts.com/hc/en-us/articles/1500009325281-Instructions-G716-2004-Request-for-Information-RFI', note='Terminology background for referenced questions and documented clarification. No AIA form is reproduced; the RFI cases and wording are original.', checked='30 September 2026'),
        dict(title='AIA Contract Documents. G701-2017: Change Order overview.', url='https://learn.aiacontracts.com/aia-document/g701-2017/', note='Background on documenting changes to scope, price, and time. The approval arrangements and figures in this book are fictional, not universal contract rules.', checked='30 September 2026'),
        dict(title='Occupational Safety and Health Administration. Personal Protective Equipment: Construction.', url='https://www.osha.gov/personal-protective-equipment/construction', note='U.S. safety terminology background. The toolbox dialogue is about requesting qualified clarification, not selecting protective equipment or providing a work method.', checked='30 September 2026'),
        dict(title='AIA Contract Documents. G704-2017: Certificate of Substantial Completion instructions.', url='https://help.aiacontracts.com/hc/en-us/articles/1500009322461-instructions-g704-2017-certificate-of-substantial-completion', note='Background on closeout terminology and outstanding work. Contractual substantial completion is not presented as a substitute for local occupancy permission.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Design Intent and Client Requirements',
    scene='What does a flexible meeting room need to do?',
    skill='Turn broad client language into specific functional requirements without claiming design approval.',
    brief='Client representative Amira asks architect Ben for a flexible meeting room. During briefing, she specifies workshops for 12 people at movable tables and presentations for 24 people in rows, at different times. Staff should be able to change the arrangement within 15 minutes. Remote participants must hear questions from anywhere in the room. These are requested performance targets, not verified design capabilities or approved occupant loads. Ben will prepare two layouts and seek audiovisual and code reviews. The room dimensions, storage provision, access requirements, and budget effects have not yet been assessed.',
    cast='Amira | Client representative\nBen | Architect',
    culture=('Clarification is part of professional service', 'A client may expect the designer to infer a complete solution from a familiar adjective. Ask about observable uses before recommending a form. Restating the client request accurately shows attention while leaving feasibility and regulatory review to the appropriate process.'),
    a='''Which use pattern does Amira request? | Two arrangements used at different times | Two groups using the room simultaneously | Twenty-four people at workshop tables | A permanently fixed boardroom arrangement | The brief distinguishes a twelve-person workshop from a separate twenty-four-person presentation.
What does the 15-minute figure describe? | A requested furniture-change target | A verified evacuation time | A guaranteed design capability | A regulatory approval period | Fifteen minutes is the requested changeover target, not a tested or approved performance result.
Which statement about capacity is supported? | The requested numbers still need design and code review. | The room is approved for twenty-four occupants. | All layouts with twenty-four chairs are compliant. | The client can waive access requirements. | Requested user numbers do not establish a compliant layout or an approved occupant load.''',
    vocabulary='''design intent | The purpose and performance an intended design should achieve. | explain the design intent
client brief | A statement of the client's needs, priorities, and constraints. | develop the client brief
functional requirement | A description of what a space or system must enable. | define a functional requirement
space planning | Organizing space for activities, movement, and equipment. | review the space planning
occupant load | The number of occupants determined under applicable code provisions. | verify the occupant load
seating arrangement | The planned position and relationship of seats. | compare seating arrangements
theater-style seating | Rows of seats generally facing a presentation area. | propose theater-style seating
workshop layout | An arrangement supporting collaborative or practical group work. | develop a workshop layout
reconfigurable furniture | Furniture that can be rearranged for different uses. | specify reconfigurable furniture
changeover time | The time needed to change between arrangements or uses. | set a changeover target
circulation | Routes and space for movement within a building. | maintain clear circulation
egress | Movement out of a building or space, particularly for emergency exit. | review egress requirements
accessibility | Usability of spaces and facilities by people with differing abilities. | integrate accessibility requirements
sightline | A line of vision from a viewing position to an object or area. | check presentation sightlines
acoustic performance | How a space handles sound for its intended use. | assess acoustic performance
reverberation | Persistence of sound after the original source stops. | evaluate reverberation
speech intelligibility | How clearly spoken words can be understood. | improve speech intelligibility
audiovisual (AV) system | Equipment for presenting or transmitting sound and images. | coordinate the AV system
microphone coverage | The area from which a microphone system can capture usable sound. | assess microphone coverage
power provision | The planned availability and location of electrical power. | coordinate power provision
storage allowance | Space reserved for items that are not currently in use. | include a storage allowance
adjacency | The relationship between nearby spaces or functions. | test an adjacency requirement
performance target | A desired measurable result that must still be evaluated. | state a performance target
design constraint | A condition limiting the available design choices. | identify a design constraint''',
    precision='Requested capacity is not approved occupant load. A layout drawing must still be assessed against the actual space and applicable requirements. Keep the client wish, proposed solution, and verified result distinct.',
    precision_extra='A room may support two arrangements without supporting both simultaneously. Name the use pattern and changeover target. For remote participation, sound quality needs its own requirement rather than an assumption that a screen solves the problem.',
    phrases='''Clarify a broad adjective | When you say flexible, which activities do you need?
Separate use patterns | Will those activities happen at the same time?
Quantify workshop needs | The workshop arrangement needs twelve places at movable tables.
Quantify presentation needs | The presentation arrangement needs twenty-four seats in rows.
State the changeover target | Staff should be able to change layouts within fifteen minutes.
Qualify the target | That is a requested target, not a tested capability.
Ask about storage | Where will unused furniture be stored?
Specify the listening need | Remote participants need to hear questions throughout the room.
Separate AV functions | Displaying slides does not by itself provide microphone coverage.
Check sightlines | We need to assess views from the proposed seating positions.
Name the review boundary | The layouts still need access and code review.
Avoid a capacity promise | I cannot confirm the approved occupant load from this brief.
Preserve a constraint | We have not yet assessed the budget effect.
Offer a defined next step | I will prepare two layouts for review.
Confirm the brief | The two activities occur at different times.
Close the meeting | I will record these as requirements to be tested.''',
    notes='''Needs versus has | A required capability is not an existing verified capability.
At different times | Excludes simultaneous use from the supplied requirement.
Within | Gives a maximum target duration, not an approximate starting time.
Can versus should | Can may claim ability; should here expresses a requested target.
Throughout | Extends the listening requirement beyond the presenter position.
For review | Keeps a proposed layout distinct from an approved design.''',
    d='''Which brief statement is most precise? | Twelve-person workshops and twenty-four-person presentations at different times | A flexible space for everybody | A room guaranteed to meet every code | Two simultaneous twenty-four-person workshops | The precise statement identifies both user numbers and the separate timing of the activities.
Which claim goes beyond the facts? | The room is already approved for twenty-four occupants. | Two layouts will be prepared. | AV review is needed. | Storage provision remains unassessed. | The client request does not establish an approved occupant load or compliant design.
Which question clarifies the changeover requirement? | Who moves the furniture, and where does unused furniture go? | Which wall finish does the client prefer? | How many remote participants normally join? | Which presentation format is used most often? | Staffing and storage directly affect the fifteen-minute changeover; the other questions address different design needs.
Which response addresses remote participants? | Assess sound capture from the room, not just the display. | Add a screen and assume all questions are audible. | Remove the requirement without asking. | Treat remote listening as an occupant-load calculation. | Hearing questions depends on the audio arrangement, not simply the presence of a screen.''',
    dialogue='''Amira | We need a flexible meeting room. At the moment, every session feels squeezed into the same arrangement, even when the activity changes completely.
Ben | Let's make the [[client brief::The client brief records the intended users, activities, and requirements before a specific solution is confirmed.]] more specific. Are you describing different arrangements at different times, or two groups using separate parts of the room simultaneously?
Amira | Different times. We run workshops for twelve people at movable tables, then presentations for twenty-four people in rows. We do not need both together.
Ben | That gives us two distinct [[seating arrangements::The seating arrangements describe how seats relate to each activity; they do not establish approved occupancy or feasibility.]]. I will draw both, but those numbers remain requested capacities until the layouts and relevant requirements have been reviewed.
Amira | Good. Staff also need to switch between them quickly. I would like the room ready for the next session within fifteen minutes, without specialist assistance.
Ben | I will record that [[changeover time::Changeover time is the duration needed to move between the requested arrangements, here a target of fifteen minutes.]] as a performance target. We still need to assess the furniture, available storage, and who will actually make the change.
Amira | Could we simply leave the spare tables against the wall? That seems easier than creating a separate storage area somewhere else in the building.
Ben | We need to check the [[circulation::Circulation concerns movement through the space; stored furniture must not be assumed to fit without assessing its effect on routes.]] and access implications before choosing that solution. Unused furniture still occupies space, and the room dimensions have not yet been assessed.
Amira | Understood. The presentation layout must also work for people joining remotely. They often hear the presenter but miss questions from people sitting further back.
Ben | That is a [[microphone coverage::Microphone coverage addresses capturing sound from the required locations, rather than merely displaying images or slides.]] requirement, not just a request for a larger screen. I will ask the AV specialist to assess sound capture across the room.
Amira | That is our current problem: a good screen, but remote colleagues cannot hear questions from the back. Please include those seats in the audio review.
Ben | We should also consider [[speech intelligibility::Speech intelligibility describes how clearly the spoken words can be understood, beyond the mere presence of an audio signal.]]. Capturing sound does not guarantee that words are clear. The room's acoustic behavior will need professional assessment alongside the equipment.
Amira | Can I tell our team the new room will hold twenty-four people? They want to start scheduling larger presentations as soon as the design begins.
Ben | Say that twenty-four is the requested presentation capacity. I cannot confirm the [[occupant load::Occupant load requires the applicable code determination; the requested number of seats is not that approval.]] from this brief or authorize use before the required reviews.
Amira | I will tell the team the numbers are still being tested. Please also check whether people at the sides can see the diagrams.
Ben | I will include [[sightlines::Sightlines describe the views from seating positions to the presentation area and must be assessed in the proposed layouts.]] in the layout review. That requirement may affect furniture placement and display location, so we should not fix either independently too early.
Amira | What will you bring back to our next meeting? I need something concrete enough for staff to discuss without assuming the design is already settled.
Ben | Two proposed layouts and an explicit list of [[design constraints::Design constraints are conditions limiting the solution; identifying them prevents unresolved matters from being treated as settled design decisions.]]. I will identify the outstanding dimensional, storage, access, AV, code, and budget reviews beside the requested performance.
Amira | That works. Please preserve the twelve and twenty-four figures, different-time use, and fifteen-minute target, while clearly showing that feasibility remains to be established.
Ben | Agreed. Those will form the recorded [[functional requirements::Functional requirements state what the space is intended to enable, while the design and review process establishes how that can be achieved.]]. The next step is to test them against the actual room and project constraints, not to label them approved capabilities.''',
    rehearsal=['Read the corrected conversation, distinguishing 12 workshop places from 24 presentation seats.', 'Switch roles and repeat turns 5-12; emphasize the 15-minute target, storage, and hearing questions from the whole room.', 'Read the checked transfer twice using 10, 18, and 20. Keep requested capacity distinct from approved occupancy.'],
    transfer_title='A second room brief',
    transfer_setup='A separate client requests workshops for 10 people and presentations for 18, at different times. The desired changeover is 20 minutes. None of the capacities is approved.',
    transfer='''Client: "The workshop needs ___ places." | 10 | Ten is the requested workshop capacity in the supplied brief.
Architect: "The presentation request is ___ seats." | 18 | Eighteen refers to presentation seating, not the workshop arrangement.
Client: "The target changeover is ___ minutes." | 20 | Twenty minutes is the requested duration for changing arrangements.
Architect: "Those capacities remain ___, not approved." | requested | The brief explicitly says no capacity approval has been established.'''))

BOOK['units'].append(unit(
    title='Drawings, Specifications, and RFIs',
    scene='Two documents disagree about the same finish',
    skill='Describe a document discrepancy and request a traceable decision without inventing precedence.',
    brief='Site coordinator Lena finds a finish discrepancy in Room 205. Drawing A601 revision C identifies wall finish F2; specification S09 revision B identifies F3 for the same wall. Both are in the current project issue. Neither document resolves the conflict, and no rule of precedence has been established in the supplied case. Architect Marco will coordinate a formal response. A project hold applies to the affected finish procurement until the discrepancy is resolved through the authorized process. The requested response date is Tuesday at 14:00, not a promised answer or automatic release.',
    cast='Lena | Site coordinator\nMarco | Architect',
    culture=('Challenge the documents, not the person', 'A precise discrepancy report can be direct without accusing the designer of carelessness. Give the location and both references, then state the decision needed. Avoid turning a question into an instruction by writing a preferred answer as though it were already approved.'),
    a='''Where is the discrepancy? | The same wall in Room 205 | Every floor in the building | An unspecified external elevation | A room that has already been closed out | Both references identify different finishes for the same wall in Room 205.
Which finish can Lena select from the supplied facts? | Neither; an authorized clarification is required. | F2 because drawings always win | F3 because specifications always win | Whichever can be delivered first | The case supplies no precedence rule or authorized decision resolving the conflict.
What does Tuesday at 14:00 mean? | The requested response time | Automatic procurement release | A guaranteed architect response | The finish installation completion time | The requested date communicates a need without guaranteeing an answer or lifting the hold.''',
    vocabulary='''request for information (RFI) | A documented request to clarify missing or conflicting project information. | raise an RFI
drawing reference | The identifier used to locate a drawing or detail. | cite the drawing reference
specification | Written requirements describing materials, quality, or execution. | review the specification
revision | A controlled version of a document after changes. | verify the revision
issue status | The purpose or authorization status assigned to a document release. | check the issue status
finish schedule | A listing of finishes assigned to spaces or surfaces. | consult the finish schedule
detail | An enlarged or specific representation of part of a design. | reference the detail
elevation | A drawing showing a vertical face of a building or element. | compare the elevation
section | A drawing showing a cut through a building or element. | review the section
callout | A notation directing the reader to a detail or requirement. | follow the callout
discrepancy | A difference between information that should agree. | document the discrepancy
document precedence | The applicable order of authority when project documents conflict. | establish document precedence
clarification | Information that resolves uncertainty about an existing requirement. | obtain written clarification
design coordination | Aligning design information across documents and disciplines. | coordinate the design response
submittal | Information submitted for the review required by the project process. | track the submittal
shop drawing | A detailed drawing prepared for fabrication or installation. | review the shop drawing
material sample | A physical example submitted to demonstrate a proposed material or finish. | submit a material sample
substitution | A proposed alternative to the specified product or arrangement. | request a substitution
procurement hold | A restriction on purchasing affected items pending a required decision. | maintain the procurement hold
response date | The stated date requested or committed for a reply. | distinguish the response date
RFI log | A register tracking information requests and their status. | update the RFI log
superseded document | A document replaced by a later applicable issue. | identify a superseded document
controlled distribution | A process for providing the correct document versions to recipients. | maintain controlled distribution
traceability | The ability to follow a decision back to its source and record. | preserve decision traceability''',
    precision='Revision letters apply within their own document histories. Revision C of one drawing is not automatically more authoritative than revision B of a different specification. Establish the applicable documents and the authorized resolution.',
    precision_extra='An RFI response is not automatically permission for added cost or time. If the answer changes the work, route its consequences through the applicable contract process. Do not silently convert clarification into a change authorization.',
    phrases='''Locate the issue | The discrepancy concerns the same wall in Room 205.
Cite the drawing | A601 revision C identifies finish F2.
Cite the specification | S09 revision B identifies finish F3.
Confirm document status | Both references are in the current project issue.
Avoid invented precedence | The supplied information does not establish which requirement governs.
Ask a bounded question | Please confirm the required finish for this wall.
Attach supporting material | I will attach the marked location and both references.
Separate a proposal | Our suggested option is not an approved instruction.
State the current hold | Affected finish procurement remains on hold.
Explain the requested date | We request a response by Tuesday at 14:00.
Avoid an implied guarantee | That date is requested, not confirmed.
Track the reply | We will record the formal response in the RFI log.
Check change consequences | Any cost or time effect needs the applicable change process.
Distribute the decision | Please identify the documents that need updating.
Keep unaffected work distinct | This hold applies to the affected finish procurement.
Close with traceability | Link the decision to the RFI and the corrected document issue.''',
    notes='''Identifies | Reports what a document says without endorsing it as controlling.
For the same wall | Establishes that the references genuinely conflict.
Please confirm | Requests a specific decision, not general design advice.
Requested by | Does not mean promised by the receiving person.
Suggested | Marks an option as a proposal rather than authority.
Current versus controlling | A current document may still conflict with another current document.''',
    d='''Which RFI description is strongest? | Room 205 wall: A601 rev C says F2; S09 rev B says F3. Please confirm the required finish. | The drawings are bad; sort them out. | We chose F2 because C is later than B. | Please approve all finishes everywhere. | The specific request identifies the location, conflict, references, and decision required.
What follows from both references being current? | The conflict still requires clarification. | Both finishes must be installed together. | Procurement is automatically released. | One reference can be deleted without review. | Current issue status does not by itself resolve contradictory requirements.
What should happen if the reply adds cost or time? | Use the applicable change-authorization process. | Assume the RFI alone approves every consequence. | Hide the effect in the next invoice. | Treat the requested reply date as budget approval. | Clarification and authorization of changed commercial effects are distinct project decisions.
Which update is supported before a reply arrives? | RFI open; affected finish procurement on hold; response requested Tuesday at 14:00. | Finish approved; answer expected sometime. | All site work stopped permanently. | F3 approved because the specification uses words. | This update preserves the actual open status, limited hold, and requested response time.''',
    dialogue='''Lena | I have a finish discrepancy in Room 205. The drawing and specification identify different finishes for the same wall, and procurement needs a definite answer.
Marco | Give me both [[document references::Document references identify the exact sources of the conflict so the response can address the same location and information.]] and their revisions. I want to check the current issue before anyone assumes an old print is the cause of the difference.
Lena | Drawing A601 revision C says F2. Specification S09 revision B says F3. Both appear in the current project issue, and neither explains the difference.
Marco | Then we need documented [[clarification::Clarification resolves the uncertain requirement; the current documents alone do not establish whether F2 or F3 is correct.]]. Do not treat the letter C as automatically overriding B, because those revisions belong to different documents with separate histories.
Lena | A colleague suggested that specifications always take precedence over drawings. I have not found an applicable rule in the material available for this case.
Marco | We should not invent [[document precedence::Document precedence concerns the applicable authority of conflicting documents, which has not been established in the supplied case.]]. Raise the discrepancy through the project process and identify the decision needed. I will coordinate the formal architectural response.
Lena | I will mark the wall on the drawing and attach the specification extract. Should I include the finish we would prefer because it is available sooner?
Marco | You can label that as a proposal, but not as an approved [[substitution::A substitution is a proposed alternative to the requirement; preference or availability does not establish approval.]]. The immediate question is which finish the design requires. Availability does not resolve the document conflict.
Lena | Understood. The affected finish procurement is currently on hold. I need the response by Tuesday at two in the afternoon to support the purchasing plan.
Marco | Record that as the requested [[response date::The response date is requested here, not a promise by Marco or a condition that automatically releases procurement.]]. I have not committed to that time. If coordination takes longer, we must communicate the status rather than silently release the purchase.
Lena | I will make the subject specific: Room 205 wall finish discrepancy. The question will ask you to confirm the required finish, with both references attached.
Marco | That will make the [[RFI log::The RFI log tracks the request, its references, response, and current status so another person can follow the decision.]] useful to the next person. Include the affected procurement item and current hold, without implying that every activity on site has stopped.
Lena | If your reply changes the finish, can the purchasing team immediately treat any extra cost as approved? They want one message that settles everything.
Marco | No. We must distinguish the design answer from the required [[change authorization::Change authorization addresses permission for altered work and its relevant effects; it is not automatically supplied by an RFI clarification.]]. Any effect on cost or time needs the applicable contract process, even if the technical answer is clear.
Lena | Then I will track the design reply and any commercial approval separately. Who needs the corrected information once the response is issued?
Marco | Use the project's [[controlled distribution::Controlled distribution provides recipients with the applicable document issue and helps prevent use of outdated conflicting information.]] process. Identify what needs updating, communicate the revised issue to affected recipients, and retain a traceable link to the original question and response.
Lena | Please tell us which sheets or extracts the response replaces. The buyer has a saved copy, and I do not want the old finish ordered after clarification.
Marco | Exactly. The goal is [[traceability::Traceability allows the team to follow the final requirement back through the documented decision and affected references.]], not simply an email saying resolved. A later reviewer should be able to find the question, authorized response, and resulting document changes.
Lena | For now, the RFI stays open and the affected procurement stays on hold. Tuesday at fourteen hundred is our requested response time, not a release deadline.
Marco | Correct. Maintain the [[procurement hold::The procurement hold remains in effect for the affected finish until the authorized process resolves the discrepancy and permits the next action.]] until the authorized process resolves the issue. I will coordinate the response and make any remaining uncertainty or separate change requirement explicit.''',
    rehearsal=['Read the corrected dialogue, stating each document identifier, revision, and finish separately.', 'Switch roles for turns 11-20; distinguish the RFI response from cost authorization and the requested date from a promise.', 'Read the checked Room 310 transfer twice, keeping C1 and C4 attached to the correct source.'],
    transfer_title='Locate a different discrepancy',
    transfer_setup='Room 310 has a ceiling conflict: drawing A702 revision D says C1; specification S12 revision B says C4. Neither requirement has been confirmed.',
    transfer='''Coordinator: "The affected room is ___." | 310 | The supplied discrepancy concerns Room 310, not Room 205.
Architect: "The drawing identifies ceiling finish ___." | C1 | C1 is the designation in the supplied drawing reference.
Coordinator: "The specification identifies ___." | C4 | C4 is the conflicting designation in the supplied specification.
Architect: "The required finish remains ___." | unconfirmed | The case explicitly provides no decision resolving the two requirements.'''))


BOOK['units'].append(unit(
    title='Change Orders and Cost Control',
    scene='A price request became an instruction in the minutes',
    skill='Distinguish pricing, approval, and authorization while explaining a proposed change in cost and time.',
    brief='A client asks the project team to price an additional partition. The original contract sum is $100,000; previously approved changes total a net addition of $5,000. Estimator Noor proposes a further $6,200 and an estimated two working days for the partition, subject to review. Neither has been accepted. No instruction to proceed has been issued under this fictional project\'s authorization process. Manager Felix notices that draft minutes say the client approved the work. The client actually requested pricing only. Other contracts may provide different change mechanisms; this case supplies no alternative instruction.',
    cast='Noor | Estimator\nFelix | Project manager',
    culture=('Enthusiasm is not a commercial decision', 'A client saying that an idea looks useful may encourage a team to move quickly. Record the actual request and authority separately from the positive reaction. Accurate minutes protect shared understanding without requiring an accusatory conversation about who misunderstood whom.'),
    a='''What is the current approved contract sum? | $105,000 | $100,000 | $111,200 | $106,200 | The original $100,000 plus the approved $5,000 addition equals $105,000.
What has the client authorized in this case? | Preparation of pricing only | Immediate partition construction | A $6,200 increase in the contract sum | A two-day extension of contract time | The client requested a price, while the proposed cost and time remain unaccepted.
What is the status of the two working days? | An estimated effect subject to review | An approved extension | Two calendar weeks | A completed delay analysis | The estimator supplies a provisional time estimate, not an agreed contract adjustment.''',
    vocabulary='''change order | A formal agreed change under the applicable contract process. | execute a change order
scope change | An alteration to the work or deliverables required. | assess a scope change
proposal request | A request to submit a price or other terms for proposed work. | issue a proposal request
contract sum | The monetary amount established by the construction contract and agreed adjustments. | state the current contract sum
approved adjustment | A change accepted through the applicable approval process. | record an approved adjustment
net addition | The overall increase after relevant additions and deductions. | calculate the net addition
deductive change | A change that reduces the relevant price or scope. | price a deductive change
proposed amount | A figure submitted for consideration rather than accepted. | separate the proposed amount
cost breakdown | An itemized explanation of the elements of a price. | request a cost breakdown
quantity takeoff | Measurement of material or work quantities for estimating. | check the quantity takeoff
labor allowance | An estimated amount assigned to labor in a price. | review the labor allowance
material cost | The cost assigned to materials for the work. | verify material costs
markup | An amount added to an underlying cost according to the pricing basis. | explain the markup
contingency | An allowance for identified uncertainty or potential future cost. | distinguish the contingency
exclusion | An item explicitly not included in a price or scope. | identify a pricing exclusion
pricing assumption | A condition used as the basis of an estimate. | state a pricing assumption
quotation validity | The period during which a quoted offer remains available on its stated terms. | check quotation validity
time impact | The effect of a change or event on the project schedule. | assess the time impact
working day | A day counted as working under the applicable project calendar. | specify working days
authorization to proceed | Permission to begin specified work under the applicable process. | verify authorization to proceed
change register | A record tracking proposed and approved changes. | maintain the change register
pending exposure | A potential cost or obligation that has not been settled. | report pending exposure
commitment | An obligation or undertaking, such as an approved purchase. | distinguish a cost commitment
construction change directive | A contract mechanism directing a change under specified conditions before all terms are agreed. | check a construction change directive''',
    precision='The approved sum is $105,000. Adding the unaccepted $6,200 would produce $111,200 only as a hypothetical revised sum. Show the pending proposal separately so the reader can distinguish agreed value from possible exposure.',
    precision_extra='This fictional project has no instruction to proceed. Do not turn that fact into a universal rule that every contract requires an agreed change order before any changed work. Different contractual mechanisms require their own authority and documentation.',
    phrases='''Correct the minutes | The client requested pricing, not construction.
State the approved value | The current approved contract sum is one hundred five thousand dollars.
Separate the proposal | The additional six thousand two hundred dollars remains proposed.
Explain the conditional total | If accepted, that proposal would bring the sum to one hundred eleven thousand two hundred dollars.
Qualify the duration | The two working days are an estimate subject to review.
Keep time separate | No extension of contract time has been agreed.
Ask for the basis | Please show the quantities and pricing assumptions.
Check what is missing | Which items are excluded from this quotation?
Clarify markup | Please distinguish direct cost from the proposed markup.
Avoid implied authorization | Pricing the partition does not authorize construction.
Name the current boundary | No instruction to proceed has been issued in this case.
Track the status | Record the proposal as pending in the change register.
Preserve the original decision | The previously approved changes remain separate.
Address the deadline | Check quotation validity before relying on this price later.
Route the decision | Submit the proposal through the project's authorized process.
Close the correction | I will circulate corrected minutes identifying the request accurately.''',
    notes='''Would bring | Expresses a conditional total, not the present approved sum.
Net addition | Includes the effect of relevant deductions rather than adding every gross figure.
Subject to review | Preserves an unresolved assessment or decision.
Working days | Requires a calendar basis; it is not automatically elapsed calendar days.
Requested pricing | Specifies the action asked for without expanding it to execution.
No instruction issued | Describes the supplied case, not every possible contract mechanism.''',
    d='''Which cost summary is correct? | Approved $105,000; proposed addition $6,200; hypothetical total $111,200 | Approved $111,200; proposal already included | Approved $100,000; ignore prior changes | Approved $6,200; the original work is canceled | The summary preserves both the existing approved value and the separate unaccepted proposal.
Which minutes correction is appropriate? | Replace approved the partition with requested pricing for the partition. | Delete the meeting because the price is uncertain. | Mark the work complete because the client liked it. | Record the estimate as an instruction from the client. | The corrected wording matches the actual action requested rather than inventing an approval.
What does an estimated two-day effect establish? | A provisional schedule assessment | An agreed contract extension | Permission to miss every milestone | A guarantee that no other task is affected | An estimate remains subject to review and does not itself amend contractual time.
Which statement respects different contracts? | Check the applicable mechanism and actual instruction; none is issued here. | Every changed task always requires the same form first. | A price estimate overrides every contract. | Verbal enthusiasm always commits the owner to the quoted sum. | The case describes one authorization status without imposing a universal rule on other contracts.''',
    dialogue='''Felix | The draft minutes say the client approved the additional partition. I remember a request for pricing, not an instruction to build it. Does your record agree?
Noor | Yes. We received a [[proposal request::A proposal request asks for terms or pricing; it is not the client's acceptance of the proposed work.]]. I prepared a price and provisional time estimate, but neither has been accepted through the project process.
Felix | Let's correct the minutes before the purchasing team relies on them. What is our current approved value, including the changes that were agreed earlier?
Noor | The original hundred thousand plus the approved five-thousand-dollar [[net addition::The net addition is the already approved increase, giving a current contract sum of $105,000 before the new proposal.]] gives us a hundred five thousand. The new partition proposal is separate.
Felix | And the six thousand two hundred for the partition would take that to a hundred eleven thousand two hundred only if it were accepted?
Noor | Correct. That is a conditional total, not the current [[contract sum::The contract sum reflects the original agreement and approved adjustments, not a proposal still awaiting acceptance.]]. I will show the approved value, pending proposal, and hypothetical revised figure on separate lines.
Felix | Before I send the proposal, show me what the six thousand two hundred includes. Are labor, materials, and markup separated?
Noor | I will attach the [[cost breakdown::The cost breakdown itemizes the elements behind the proposed price so the reviewer can examine its basis.]], with quantities, labor and material allowances, markup, assumptions, and exclusions. The total alone does not explain the scope included in the offer.
Felix | The schedule note says two days. That could sound like we have already agreed an extension, especially if someone copies it without the qualification.
Noor | I will say estimated [[time impact::Time impact is the assessed schedule effect; the two-day figure remains an estimate rather than an agreed extension.]] of two working days, subject to review. We have not agreed any extension of contract time or confirmed how the work fits the sequence.
Felix | Please preserve working days as well. The client may read an unqualified two days as elapsed calendar time, which could produce a different expectation.
Noor | Agreed. I will also state the [[pricing assumptions::Pricing assumptions are the conditions underlying the estimate; changing them may alter what the quoted price covers.]]. If the scope or planned execution changes, we need to review whether the quotation still represents the work being requested.
Felix | Can procurement reserve materials now? They want to keep the option available, but a reservation might create an obligation even before installation begins.
Noor | We need to check the proposed [[commitment::A commitment can create an obligation such as a purchase; it must not be assumed permissible merely because the work is still proposed.]] against the authorization process. In this case, no instruction to proceed has been issued, and I cannot authorize a purchase.
Felix | I will tell procurement that we have a pricing request, not an instruction to proceed. Flag any reservation charge before anyone commits us to it.
Noor | Exactly. The [[change register::The change register tracks the proposal separately from approved changes, preserving its pending status for later review.]] should show this item as pending. It should not be merged into the approved total simply because the client sounded enthusiastic.
Felix | We should also check how long the price remains available. The client may defer the decision and return later expecting every figure to remain unchanged.
Noor | I will confirm the [[quotation validity::Quotation validity identifies the period and terms under which the offer remains available, rather than assuming an estimate lasts indefinitely.]] and communicate it with the proposal. We should not invent a validity period or silently treat an expired offer as current.
Felix | I will circulate corrected minutes: pricing requested, six thousand two hundred proposed, two working days estimated, and no accepted cost or time adjustment.
Noor | Add that [[authorization to proceed::Authorization to proceed is permission to start specified work; the supplied case explicitly has no such instruction.]] remains absent under this project's process. That gives the team a clear current status without turning the proposal into a decision.''',
    rehearsal=['Read the corrected conversation with $105,000 approved and $6,200 proposed.', 'Switch roles; stress would in the $111,200 total and estimated in the two-working-day effect.', 'Read the checked transfer twice. Keep $84,000 current and $87,000 conditional on acceptance.'],
    transfer_title='Keep pending money separate',
    transfer_setup='Another contract started at $80,000 and has approved net additions of $4,000. A new $3,000 proposal remains unaccepted. No time adjustment has been agreed.',
    transfer='''Manager: "The current approved sum is $___." | 84,000 | The original eighty thousand plus four thousand approved equals eighty-four thousand.
Estimator: "The pending proposal is $___." | 3,000 | Three thousand is the separate proposal that remains unaccepted.
Manager: "If accepted, the revised sum would be $___." | 87,000 | Adding the pending three thousand to eighty-four thousand gives eighty-seven thousand.
Estimator: "The proposed change remains ___." | unaccepted | The supplied facts explicitly say the new proposal has not been accepted.'''))

BOOK['units'].append(unit(
    title='Schedule, Sequencing, and Critical Path',
    scene='The lookahead still shows a delivery that cannot happen',
    skill='Explain a constrained sequence and distinguish forecast movement from contractual entitlement.',
    brief='A simplified project calendar uses numbered working days. The baseline shows delivery at the end of Day 1, installation on Days 2 and 3, and testing on Day 4. Each task depends on the previous one finishing; no overlap or float is available in this supplied sequence. Delivery is now forecast at the end of Day 3. Installation still needs two full working days, followed by one testing day. Planner Imani and site manager Owen have not verified any recovery option. The lookahead still shows the original dates. This arithmetic is not a contract-extension decision.',
    cast='Imani | Planner\nOwen | Site manager',
    culture=('A changed forecast is information, not disloyalty', 'A team may feel that moving a date admits defeat. Keeping an obsolete plan visible as the current forecast is more misleading. Preserve the baseline for comparison, show the supported forecast, and evaluate recovery options separately from promises.'),
    a='''With the stated dependencies, when can installation occur? | Days 4 and 5 | Days 2 and 3 | Day 3 only | Before delivery is complete | Delivery finishes at the end of Day 3, so two full installation days follow.
When does testing move to? | Day 6 | Day 4 | Day 3 | Day 5 while installation is unfinished | Testing requires completed installation, which now finishes at the end of Day 5.
What has been established about recovery? | No recovery option has been verified. | Overtime definitely restores Day 4. | Testing can be omitted. | The dependency can be ignored. | The brief provides no verified way to shorten or overlap the activities.''',
    vocabulary='''baseline schedule | The agreed reference plan used for comparison with later progress. | retain the baseline schedule
lookahead schedule | A short-term plan of upcoming activities and requirements. | update the lookahead schedule
critical path | A sequence of activities determining the relevant earliest completion under the schedule logic. | review the critical path
predecessor | An activity that must occur before a linked activity under the schedule logic. | identify the predecessor
successor | An activity linked to follow another under the schedule logic. | identify the successor
finish-to-start relationship | A link requiring one activity to finish before the next starts. | model a finish-to-start relationship
activity duration | The time required to perform a scheduled activity. | verify the activity duration
total float | Time an activity can move without delaying the relevant project completion under the schedule model. | assess total float
free float | Time an activity can move without delaying the early start of a successor. | distinguish free float
lead time | The time needed to obtain an item or complete a preparatory process. | confirm the lead time
forecast date | The date currently expected on the basis of available information. | revise the forecast date
data date | The point in time to which schedule progress information is updated. | state the data date
milestone | A significant scheduled event, usually with no duration. | track the testing milestone
constraint | A restriction affecting when or how an activity may occur. | identify a schedule constraint
workfront | An area or package available for a crew to perform work. | release a workfront
sequence | The order in which activities are carried out. | preserve the required sequence
recovery plan | A proposal for regaining lost time or limiting delay. | evaluate a recovery plan
acceleration | Measures intended to complete work sooner than otherwise forecast. | assess acceleration options
resource availability | The availability of labor, equipment, or other required inputs. | verify resource availability
productivity | The output achieved per unit of input or time. | test productivity assumptions
schedule variance | A difference between planned and actual or forecast timing. | explain the schedule variance
critical-path analysis | Evaluation of schedule logic and the activities driving completion. | update the critical-path analysis
extension of time | A contractual adjustment to the allowed completion period when properly established. | distinguish an extension of time
calendar basis | The working and nonworking periods used to count schedule time. | state the calendar basis''',
    precision='The delivery moves from the end of Day 1 to the end of Day 3. With unchanged durations and no overlap, installation moves to Days 4 and 5, and testing to Day 6. The forecast shifts two working days.',
    precision_extra='A schedule forecast describes expected timing under stated assumptions. It does not by itself establish responsibility for delay, entitlement to extra time, or entitlement to payment. Recovery proposals also require evidence, resources, and appropriate approval.',
    phrases='''Identify the reference | The baseline places testing on Day 4.
State the changed input | Delivery is now forecast for the end of Day 3.
Explain the dependency | Installation cannot start until delivery is complete.
Preserve the duration | Installation still requires two full working days.
Calculate the new sequence | Installation moves to Days 4 and 5.
State the resulting forecast | Testing moves to Day 6 under the supplied logic.
Quantify the variance | That is a two-working-day movement from the baseline.
Keep the reference intact | Retain the baseline and show the revised forecast separately.
Correct the short-term plan | The lookahead must reflect the current delivery forecast.
Avoid unsupported recovery | We have not verified an option that restores Day 4.
Check resources | Extra hours are not a recovery plan until their feasibility is assessed.
Protect the dependency | We cannot assume testing overlaps unfinished installation.
Qualify the model | This result follows the simplified sequence supplied here.
Separate contractual questions | The forecast does not itself grant an extension of time.
State the clock basis | These are numbered working days, not calendar dates.
Close with the next update | I will issue the revised lookahead with its assumptions.''',
    notes='''At the end of | Matters because the successor cannot use the same full working day.
Still requires | Keeps the activity duration unchanged despite pressure.
Moves to | Reports a forecast change without assigning legal responsibility.
No float | Removes unused schedule allowance in the supplied model.
Under the supplied logic | Limits the calculation to its stated assumptions.
Restore versus request | A proposed recovery action does not prove the old date can be restored.''',
    d='''Which sequence follows the supplied facts? | Delivery ends Day 3; installation Days 4-5; testing Day 6 | Delivery ends Day 3; installation Day 3; testing Day 4 | Delivery ends Day 3; skip testing | Installation Days 2-3 despite the missing delivery | The finish-to-start links and unchanged durations produce testing on Day 6.
How should the schedule records be handled? | Preserve the baseline and update the current lookahead. | Delete the baseline to hide the movement. | Keep the old forecast because it looks better. | Change the delivery date but leave dependent tasks unchanged. | The baseline supports comparison while the lookahead must represent the supported upcoming sequence.
What is the variance in testing? | Two working days later | Two calendar weeks later | One working day earlier | No movement because the baseline is fixed | Testing moves from Day 4 to Day 6, a difference of two working days.
Which contractual conclusion is supported? | None is established by this calculation alone. | A two-day extension is automatically approved. | The supplier owes every additional cost. | The contractor must accelerate without review. | Forecast arithmetic alone does not determine contractual responsibility, relief, or payment.''',
    dialogue='''Owen | The delivery update says the end of Day 3, but our lookahead still shows installation on Days 2 and 3. The crews are asking which plan applies.
Imani | The [[lookahead schedule::The lookahead schedule is the short-term upcoming plan and must reflect the changed delivery forecast rather than obsolete dates.]] needs correcting. We should keep the baseline for comparison, but it cannot remain our current forecast when a necessary input has moved.
Owen | Walk me through the sequence before I brief them. Delivery originally finished at the end of Day 1, installation took two days, and testing followed.
Imani | Correct. The [[finish-to-start relationship::The finish-to-start relationship requires the preceding activity to finish before its successor begins, so installation follows the completed delivery.]] means installation cannot begin before delivery finishes. With delivery now ending on Day 3, installation uses Days 4 and 5.
Owen | So testing moves to Day 6, provided the installation duration stays at two full working days and there is no other change to the supplied sequence.
Imani | Exactly. The [[activity duration::Activity duration is the time needed for the task; installation remains two full working days in the supplied facts.]] has not shortened. We have no overlap or float available in this model, so the delivery movement passes through to the testing date.
Owen | The installer has been asked to catch up and keep testing on Day 4. Has anyone checked a workable way to do that?
Imani | It is not a verified [[recovery plan::A recovery plan needs a feasible method for regaining time; simply retaining the old target does not demonstrate recovery.]]. We would need to assess the proposed method, resources, productivity, and constraints before making a commitment based on a shorter duration.
Owen | Extra hours are being discussed. I do not know whether the crew, equipment, access arrangements, or necessary supervision would actually be available for them.
Imani | Then [[resource availability::Resource availability concerns whether the people, equipment, and other inputs needed for a recovery proposal can actually be provided.]] remains an open question. We should label acceleration as an option under review, not assume it restores the original testing date without consequences.
Owen | I also want to avoid confusion about days. This example uses numbered working days, not dates on a calendar with a weekend somewhere in the middle.
Imani | State the [[calendar basis::The calendar basis identifies which periods count for scheduling; here all numbered days are working days rather than unqualified calendar days.]] explicitly. Day 6 is two working days later than Day 4. We should not translate that into calendar dates without the project calendar.
Owen | Please keep the original Day 4 alongside the forecast. The client will want to see the movement, not just a replacement date.
Imani | Retain the [[baseline schedule::The baseline schedule remains the reference plan for comparing the original timing with the current forecast.]] and show the forecast beside it. That makes the two-day movement visible instead of hiding it by overwriting the original reference.
Owen | Then the client sees both the original testing point and the expected one. We can explain the dependency rather than present a date with no basis.
Imani | Yes. Describe the [[schedule variance::Schedule variance is the difference between the reference and updated timing, here testing moving from Day 4 to Day 6.]] and its assumptions. If the delivery forecast changes again, or a recovery option becomes verified, update the analysis rather than reuse this result automatically.
Owen | Does this mean we can state that a two-day extension of time has been approved? The project report has a column asking about contractual completion.
Imani | No. An [[extension of time::An extension of time is a contractual adjustment requiring the applicable basis and process, not an automatic consequence of forecast arithmetic.]] is a separate contractual question. This calculation establishes neither entitlement nor responsibility, and it does not approve payment or an adjusted contract completion date.
Owen | I will brief installation on Days 4 and 5 and testing on Day 6 under the supplied assumptions, with recovery still unverified and contractual questions separate.
Imani | I will issue that [[forecast date::The forecast date states the currently expected timing under the available information, while retaining uncertainty and the separate baseline reference.]] in the revised lookahead and retain the baseline comparison. The record will show the changed delivery input and the unchanged activity durations clearly.''',
    rehearsal=['Read the corrected dialogue with delivery ending Day 3, installation Days 4-5, and testing Day 6.', 'Switch roles for turns 11-20. Retain working days and keep a forecast separate from a contractual extension.', 'Read the checked transfer twice using Days 6, 7, and 8 without overlapping the activities.'],
    transfer_title='Follow the dependency chain',
    transfer_setup='Delivery finishes at the end of Day 5. Installation needs two full working days after delivery. Testing takes the following full day. No overlap is available.',
    transfer='''Planner: "Installation begins on Day ___." | 6 | The first full working day after the end of Day 5 is Day 6.
Manager: "Its second day is Day ___." | 7 | Two full installation days are Days 6 and 7.
Planner: "Testing therefore occurs on Day ___." | 8 | Testing follows completed installation, so it occurs on Day 8.
Manager: "The dependency permits no ___." | overlap | The supplied facts expressly rule out overlapping the activities.'''))


BOOK['units'].append(unit(
    title='Site Safety and Toolbox Talks',
    scene='The briefing says use the right protection',
    skill='Request task-specific, approved safety information and confirm understanding without inventing a work method.',
    brief='A crew is due to cut composite panels with a powered tool in Zone B. The briefing card says only use the right protection. It does not identify the approved task method, controls, or equipment requirements. Foreperson Rosa has stopped the affected task under the fictional site process. Safety coordinator Dev will obtain qualified review and the applicable approved briefing before any authorized restart. No one is being asked to select equipment from this book. Similar work performed elsewhere does not establish that the same requirements apply here. The immediate need is a clear escalation and repeat-back.',
    cast='Rosa | Foreperson\nDev | Safety coordinator',
    culture=('Repeat-back checks the message, not intelligence', 'Experienced workers can interpret the same vague phrase differently. Ask someone to restate the task status and next requirement as a check on the briefing itself. Do not ask for a yes merely to complete an attendance record.'),
    a='''What is missing from the card? | The task-specific approved method, controls, and equipment requirements | Only the spelling of Zone B | Proof that everyone has done identical work | Permission to ignore the site process | The generic instruction does not supply the actual approved requirements for this task.
What is the affected task's current status? | Stopped under the local process | Authorized to begin immediately | Completed and inspected | Automatically safe because workers are experienced | Rosa has stopped the affected activity pending the required qualified clarification.
What can experience on another site establish here? | It does not by itself establish the requirements for this task. | It replaces the approved briefing. | It authorizes any worker to restart. | It proves all panel products have identical hazards. | Different materials, tools, and conditions require the applicable task assessment rather than an assumed match.''',
    vocabulary='''toolbox talk | A focused workplace briefing about a task or safety topic. | deliver a toolbox talk
task briefing | Instructions and relevant information for a specific planned activity. | clarify the task briefing
method statement | A document describing the planned method and relevant controls for work. | consult the approved method statement
job hazard analysis (JHA) | A structured review of task steps, hazards, and controls. | review the job hazard analysis
hazard identification | Recognition of conditions or activities that may cause harm. | complete hazard identification
risk assessment | Evaluation of risks and the controls needed to manage them. | review the risk assessment
hierarchy of controls | An ordered approach favoring more effective risk controls over reliance on individual behavior. | apply the hierarchy of controls
engineering control | A physical or technical measure that reduces exposure to a hazard. | verify engineering controls
administrative control | A work-practice or organizational measure intended to reduce risk. | communicate administrative controls
personal protective equipment (PPE) | Equipment worn to help protect a person from specified hazards. | specify task-appropriate PPE
exposure | Contact with or presence in conditions that may cause harm. | assess worker exposure
dust extraction | Equipment or arrangements used to capture dust near its source. | review dust extraction requirements
noise assessment | Evaluation of noise conditions and potential exposure. | obtain a noise assessment
safety data sheet (SDS) | A document communicating information about a chemical product and its hazards. | consult the safety data sheet
equipment guarding | Protective arrangements restricting access to hazardous equipment parts. | verify equipment guarding
isolation | Separation from an energy source or hazard under the applicable process. | follow the isolation procedure
exclusion zone | An area with access restricted for a specified safety reason. | identify the exclusion zone
task competence | The knowledge and ability required to perform a particular task. | verify task competence
site induction | Initial orientation to the requirements of a particular site. | complete the site induction
repeat-back | Restating a message to confirm its accurate receipt and understanding. | request a repeat-back
stop-work instruction | A direction to halt a specified activity under the relevant process. | communicate a stop-work instruction
restart condition | A requirement that must be satisfied before work resumes. | state the restart conditions
briefing record | Documentation of the briefing and relevant participation or acknowledgement. | maintain the briefing record
near miss | An event that could have caused harm but did not produce the relevant loss. | report a near miss''',
    precision='The phrase right protection supplies no usable task requirement. Clarification must address the applicable method and controls, not simply invent a list of items to wear. PPE is not a replacement for the wider control process.',
    precision_extra='A signed attendance record does not demonstrate that each person understood the instruction. Use a repeat-back of the actual task status and next requirement. This dialogue does not supply a technical cutting method or authorize a restart.',
    phrases='''Name the affected activity | The panel-cutting task in Zone B is stopped.
Identify the gap | The card does not specify the approved requirements.
Ask for the applicable document | Which approved method statement covers this task?
Request qualified review | Please obtain the task-specific assessment and controls.
Avoid equipment guessing | I will not select protective equipment from a generic phrase.
Broaden the control question | We need the full control arrangement, not PPE alone.
Distinguish similar work | Experience elsewhere does not confirm the requirements here.
State the restart boundary | The required clarification and authorization are still pending.
Check the message | Please repeat the task status and next requirement.
Correct a misunderstanding | Attending the talk does not mean the task is released.
Preserve responsibility | Dev will coordinate the qualified review.
Avoid an implied shortcut | Schedule pressure does not complete the missing assessment.
Record the current status | The briefing remains incomplete for this task.
Confirm the location | This concern applies to the planned activity in Zone B.
Make the next briefing specific | Identify the task, approved controls, and responsible supervisor.
Close the loop | Communicate an authorized status change explicitly before resuming.''',
    notes='''Right | Too vague unless the actual task requirement is identified.
Covers this task | Tests applicability, not merely the existence of a document.
Still pending | Keeps an unresolved condition visible during handover.
Repeat | Requests the message back, not a new safety plan from the learner.
Attendance versus understanding | A record of presence is not proof of comprehension.
Authorized status change | Prevents silence or movement on site from being mistaken for release.''',
    d='''Which clarification is most useful? | Which approved method and controls apply to cutting these panels in Zone B? | Can everyone just be careful? | Which equipment looks most protective? | Can the crew copy an unrelated site's briefing? | The question identifies the task and asks for applicable approved requirements rather than a guess.
Which statement about controls is accurate? | PPE requirements belong within the applicable wider control arrangement. | Wearing any PPE replaces every other control. | A briefing card proves all hazards are eliminated. | A worker's confidence establishes the exposure level. | Protective equipment does not replace assessing and applying the relevant task controls.
Which repeat-back matches the facts? | The task is stopped; qualified clarification and restart authorization are pending. | The task can restart because Dev received the message. | The card is complete because everyone signed it. | No review is needed for experienced staff. | Receipt or attendance does not satisfy the missing clarification and authorization requirements.
What should Rosa avoid? | Inventing equipment requirements to complete the card | Identifying the affected task | Asking who owns the review | Reporting the current stopped status | The case requires qualified task-specific clarification, not improvised protective-equipment selection.''',
    dialogue='''Rosa | I have stopped the panel-cutting task in Zone B. The briefing card says use the right protection, but it does not identify what that means here.
Dev | That [[task briefing::The task briefing needs applicable requirements; the generic phrase does not identify the method or controls.]] is incomplete. I will obtain the qualified review and applicable approved information before we consider any authorized restart under the local process.
Rosa | The crew has cut panels before, and one worker says we should simply use the same arrangement as at the previous site. I cannot verify the match.
Dev | Previous experience does not establish this [[risk assessment::The risk assessment addresses this task's conditions and controls; experience elsewhere does not establish its findings.]]. Materials, equipment, and working conditions can differ. We need the requirements applicable to this task, not a remembered instruction from somewhere else.
Rosa | I will keep the affected task stopped. Should my clarification request ask only which protective equipment the workers need, or is that still too narrow?
Dev | Ask for the full approved method and controls. [[Personal protective equipment::Personal protective equipment protects against specified hazards but does not replace the wider task-control arrangement.]] is not the entire control arrangement. We should not reduce the question to a list of items to wear.
Rosa | Then I will identify the composite panels, powered tool, location, and missing task-specific information, and ask which approved document covers the proposed work.
Dev | Yes. The applicable [[method statement::The method statement describes the planned method and controls; a similar title does not establish task applicability.]] and assessment need qualified review. Do not infer technical requirements from this conversation or from an unrelated document with a similar title.
Rosa | Several people have already signed the attendance sheet. I need to tell them the task is still stopped; that signature has not resolved the missing requirements.
Dev | A [[briefing record::A briefing record documents participation or the briefing; attendance alone establishes neither understanding nor authorization.]] cannot replace clear instructions. We need to check understanding of the current status, and later of the actual approved requirements, without treating a signature as technical approval.
Rosa | I can ask the crew to repeat the status and next step. That seems more useful than asking whether everybody understands and receiving a quick yes.
Dev | Use a [[repeat-back::A repeat-back checks the listener's understanding of the task status and next requirement, beyond a vague acknowledgement.]]. Explain that you are checking the message, not testing anyone's intelligence. The required response now is that the task remains stopped pending clarification and authorization.
Rosa | Can I put you down as the review contact? I will tell the other supervisors who is obtaining the task-specific clarification.
Dev | That gives the [[stop-work instruction::The stop-work instruction identifies the halted activity and remains effective while clarification and authorization are pending.]] a clear follow-up owner. My receiving the concern does not release the task; any change in its status must be communicated through the local process.
Rosa | The installation team is waiting for these panels. They will want an estimate, but we do not yet know how long obtaining the missing information will take.
Dev | We can report that uncertainty without weakening the [[restart conditions::Restart conditions must be satisfied before resumption; schedule pressure or uncertain timing does not remove them.]]. Schedule pressure does not complete the assessment. I will provide an update when we have verified information, rather than invent a release time.
Rosa | The approved briefing should distinguish physical controls, working arrangements, and personal protection, so staff understand their different purposes.
Dev | The [[hierarchy of controls::The hierarchy of controls orders risk-control approaches; it does not treat PPE as the sole or preferred answer.]] helps frame that distinction. Qualified personnel must establish the actual measures; this exchange is about obtaining and communicating those requirements accurately.
Rosa | My immediate message is clear: Zone B panel cutting is stopped, the generic instruction is insufficient, and you are coordinating the task-specific review.
Dev | Correct. The next [[toolbox talk::The toolbox talk communicates the established task requirements; attendance does not replace the required restart authorization.]] needs that approved information and a check of understanding. We will not treat attendance, experience, or my acknowledgement as permission to resume.''',
    rehearsal=['Read turns 1-10 with the answers, naming Zone B and the incomplete task briefing.', 'Switch roles for turns 11-20; repeat the current stopped status without inventing a cutting method or equipment list.', 'Read the checked Zone D transfer twice, retaining Sana as review owner and no authorized restart.'],
    transfer_title='Repeat the current task status',
    transfer_setup='A separate lifting task in Zone D is stopped. The applicable approved briefing is missing. Coordinator Sana owns the review. No restart has been authorized.',
    transfer='''Foreperson: "The affected location is Zone ___." | D | Zone D is the location supplied for this separate task.
Coordinator: "The task is currently ___." | stopped | The brief explicitly states that the lifting task is stopped.
Foreperson: "The named review owner is ___." | Sana | Sana is the coordinator assigned to obtain the missing review.
Coordinator: "A restart remains ___." | unauthorized | The supplied facts explicitly say no restart has been authorized.'''))

BOOK['units'].append(unit(
    title='Permitting, Inspections, and Code Issues',
    scene='A progress email overstates the inspection result',
    skill='Report inspection findings and outstanding conditions without expanding a limited status into full approval.',
    brief='An inspection record for Area C lists four items. Items 1 and 2 are recorded closed by the relevant authority; Items 3 and 4 remain open. Contractor photographs have been submitted for the latter two, but no acceptance of those corrections is recorded. No occupancy permission has been issued for Area C in the supplied case. Coordinator Talia finds a progress email saying fully approved. Architect Marcus will help correct the statement and coordinate the outstanding evidence. The local jurisdiction and adopted code requirements must be checked by qualified personnel; no code interpretation is supplied here.',
    cast='Talia | Project coordinator\nMarcus | Architect',
    culture=('Approval needs an object and an authority', 'Approved can refer to a product, a drawing, an inspection item, or permission to use a space. Ask what was approved, by whom, and in which record. This is not excessive formality when a broader interpretation could lead someone to act beyond the actual decision.'),
    a='''How many inspection items are recorded closed? | Two | Four | None | Three | The supplied record closes Items 1 and 2 while Items 3 and 4 remain open.
What do the photographs establish about Items 3 and 4? | Evidence was submitted, but acceptance is not recorded. | Both items are accepted as closed. | Occupancy permission is issued. | The authority has waived every requirement. | Submission of photographs is not the same as recorded acceptance of the corrections.
Which occupancy statement is supported? | No permission is issued in the supplied case. | Full use is automatically authorized. | The architect's progress email grants occupancy. | Half the inspection items allow half the area to be occupied. | The brief explicitly states that no occupancy permission has been issued for Area C.''',
    vocabulary='''authority having jurisdiction (AHJ) | The relevant authority responsible for interpreting or enforcing applicable requirements. | identify the authority having jurisdiction
adopted code | A code given effect by the relevant jurisdiction, including applicable amendments. | verify the adopted code
local amendment | A jurisdiction-specific change to a model code or requirement. | check local amendments
permit | An authorization issued under the applicable regulatory process for specified work or use. | verify the permit scope
plan review | Examination of proposed documents against relevant requirements. | respond to plan-review comments
inspection record | Documentation of an inspection and its findings or status. | consult the inspection record
inspection finding | A recorded observation or result from an inspection. | address an inspection finding
outstanding item | A matter that has not yet been resolved or accepted as complete. | track an outstanding item
correction notice | A notice identifying work or information that needs correction. | respond to a correction notice
resubmittal | Information submitted again after revision or additional work. | prepare a resubmittal
reinspection | A further inspection following earlier findings or changes. | request a reinspection
acceptance record | Documentation that the relevant reviewer has accepted a specified item. | obtain an acceptance record
conditional approval | Approval that remains subject to stated conditions. | preserve conditional approval terms
approval scope | The specific work, area, or matter covered by an approval. | state the approval scope
occupancy permission | Authorization to use or occupy an area under the applicable jurisdictional process. | verify occupancy permission
certificate of occupancy (CO) | A jurisdictional document concerning authorized occupancy under its applicable requirements. | check the certificate of occupancy
temporary occupancy | Occupancy permitted for a limited scope or period under applicable conditions. | verify temporary occupancy conditions
code compliance | Conformity with the applicable adopted requirements. | demonstrate code compliance
supporting evidence | Material submitted to substantiate a response or claim. | attach supporting evidence
inspection status | The recorded position of the relevant inspection process or items. | report inspection status
permit closeout | Completion of the applicable steps for closing a permit record. | coordinate permit closeout
design professional | A suitably qualified professional responsible for relevant design services. | consult the design professional
jurisdiction | The authority or geographic area governing applicable rules. | identify the jurisdiction
public-use restriction | A limitation on use by occupants or the public under applicable requirements. | communicate a public-use restriction''',
    precision='Two closed items out of four is 50% of this item count. It is not proof that the area is half compliant, half approved for use, or 50% complete by cost. Items differ in importance and regulatory effect.',
    precision_extra='Photographs are supporting evidence, not the reviewer decision. Keep submitted, accepted, closed, and permitted for occupancy separate. Contractual completion language also does not replace the relevant jurisdictional permission to use an area.',
    phrases='''Correct the broad claim | Fully approved is not supported by this inspection record.
Report the closed items | Items 1 and 2 are recorded closed.
Preserve the open items | Items 3 and 4 remain open.
Describe the evidence | Photographs have been submitted for the two outstanding items.
Avoid overstating submission | Acceptance of those corrections is not recorded.
Name the authority | Please identify the authority responsible for this decision.
Limit the statement | This update concerns the four listed inspection items.
Separate occupancy | No occupancy permission is issued in the supplied case.
Ask for the record | Which document supports the approval claim?
Check local requirements | The adopted code and local amendments need qualified review.
Coordinate the next step | Confirm the required evidence and any reinspection process.
Avoid assumed timing | A request for review does not confirm an inspection appointment.
Keep conditions visible | Any approval must be reported with its actual scope and conditions.
Correct all recipients | Send the revised status to everyone who received the original claim.
Preserve evidence links | Link each item to its submission and acceptance record.
Close accurately | I will update the status only when the relevant decision is documented.''',
    notes='''Fully | Expands a claim to the whole relevant scope and needs corresponding evidence.
Submitted | Describes delivery of evidence, not acceptance.
Recorded closed | Connects the status to the authority's documented decision.
No permission issued | Does not imply that permission is impossible later.
For Area C | Limits the location and avoids claims about the whole project.
Subject to conditions | Conditions must remain visible, not disappear from a short summary.''',
    d='''Which progress statement is accurate? | Two items closed; two open with photographs submitted; no occupancy permission issued. | Area C fully approved because photographs were sent. | All work rejected because two items remain open. | Half the area may be occupied because half the items are closed. | The statement distinguishes recorded closure, submitted evidence, and the separate occupancy status.
What can 2 out of 4 measure here? | Fifty percent of the listed item count | Fifty percent of legal occupancy permission | Fifty percent of total construction value | Fifty percent of every code requirement | The numerator and denominator describe listed items, not area, cost, or regulatory permission.
Which evidence would support changing an item's status? | The relevant documented acceptance or closure decision | A photograph sent but not reviewed | A colleague's optimistic summary | The number of people copied on the email | Status should reflect the relevant decision rather than merely evidence delivery or confidence.
Which question makes approved precise? | What was approved, by whom, and in which record? | When was the progress email sent to the client? | How many photographs were attached to the submission? | Who expects the remaining work to finish this week? | Scope, authority, and the decision record establish approval; email timing, attachment counts, and forecasts do not.''',
    dialogue='''Talia | The progress email says Area C is fully approved. I am looking at four inspection items, and only the first two are recorded closed.
Marcus | Then the [[inspection status::Inspection status must match the record; two open items cannot become full approval through a broad summary.]] is overstated. Please identify the record and send a correction to the original recipients before someone treats that sentence as permission to use the area.
Talia | Items 3 and 4 have contractor photographs attached. The team may have assumed that submitting those photographs meant the corrections were accepted by the reviewer.
Marcus | The photographs are [[supporting evidence::Supporting evidence may substantiate a correction; its submission is not the authority's acceptance or closure decision.]], not an acceptance decision. We need to preserve submitted and accepted as different statuses until the relevant review is documented.
Talia | I will say Items 1 and 2 are closed, Items 3 and 4 remain open, and photographs have been submitted for review of the outstanding corrections.
Marcus | Add the [[approval scope::Approval scope limits the decision to its actual subject; closing specific items does not approve the whole area.]]. We are reporting these four listed items, not claiming that every requirement for the area or the whole project has been satisfied.
Talia | The dashboard says fifty percent approved because two of four items are closed. Should the label say listed items closed instead?
Marcus | Call it fifty percent of the listed item count closed. [[Code compliance::Code compliance concerns applicable requirements; counting closed items does not measure a percentage of legal compliance or usable area.]] cannot be reduced to that arithmetic, because the items may differ in significance and effect.
Talia | We also have no occupancy permission for Area C in this case. Should that be a separate line, rather than something readers have to infer from the open items?
Marcus | Yes. State [[occupancy permission::Occupancy permission is a separate jurisdictional authorization, which the supplied facts say has not been issued.]] not issued. Do not imply that closing half the items permits use of half the area, or that our architectural coordination supplies the missing authority.
Talia | The client asks whether a temporary arrangement might be possible. I can pass on the question, but cannot promise any exception or partial use.
Marcus | Correct. The [[authority having jurisdiction::The authority having jurisdiction is responsible for the relevant regulatory decision; the project team cannot assume that authority.]] and qualified project professionals must address that under actual local requirements. This record gives us no basis for offering permission or predicting the outcome.
Talia | I will ask whether the photographs are sufficient or another visit is required. At present, I have requested a follow-up but have no appointment.
Marcus | Keep a requested [[reinspection::Reinspection is a further inspection; a request establishes neither a confirmed appointment nor a successful result.]] separate from a booked visit and a completed decision. Otherwise, the next update could repeat the same mistake using a different status word.
Talia | For each open item, I will link the photographs, date of submission, outstanding response, and responsible coordinator. That should make the next follow-up easier.
Marcus | Include the eventual [[acceptance record::The acceptance record documents the reviewer's decision, providing the basis for marking the specified item accepted or closed.]] when it exists. Do not mark the item closed just because its folder contains more documents than it did yesterday.
Talia | The client also has a contractual completion discussion next week. I want to avoid suggesting that such a project milestone automatically resolves the regulatory position.
Marcus | Keep those processes distinct. [[Permit closeout::Permit closeout concerns the regulatory record and steps; a contractual milestone does not replace that jurisdictional process.]] and occupancy requirements depend on the relevant jurisdiction. We should report their actual documented statuses alongside, not underneath, a broad completion label.
Talia | My correction will preserve all four item numbers, the two closures, the two pending reviews, and the absence of occupancy permission for the specified area.
Marcus | Good. Any later [[conditional approval::Conditional approval remains limited by its conditions; a shortened summary must preserve them and the actual scope.]] must retain its conditions in the summary. We will update the record when the relevant decision arrives, not when somebody hopes it will.''',
    rehearsal=['Read the corrected conversation with Items 1-2 closed and Items 3-4 open.', 'Switch roles for turns 9-20; keep occupancy permission, a reinspection request, and a recorded acceptance distinct.', 'Read the checked Area F transfer twice. Four closures do not establish permission to occupy.'],
    transfer_title='Separate evidence from acceptance',
    transfer_setup='Area F has six inspection items: four recorded closed and two open. Revised information has been submitted for the open items. No occupancy permission is issued.',
    transfer='''Coordinator: "The number recorded closed is ___." | four | Four of the six listed items have documented closure.
Architect: "The number still open is ___." | two | The remaining two items are explicitly identified as open.
Coordinator: "The revised information has been ___." | submitted | The brief establishes submission, not acceptance of the revised information.
Architect: "Occupancy permission remains ___." | unissued | The supplied case explicitly says no occupancy permission is issued.'''))


BOOK['units'].append(unit(
    title='Quality, Punch List, and Closeout',
    scene='A handover needs item-level evidence',
    skill='Transfer a closeout list with accurate status, ownership, and records rather than a misleading completion percentage.',
    brief='A fictional closeout register for Level 2 contains eight punch-list items. Items 1 to 3 are completed and verified closed, with acceptance records linked. Items 4 to 8 are reported corrected by the trade contractors but still await review; they remain open under this project process. Outgoing coordinator Jules hands over to Meera. Meera accepts coordination of the five open reviews and will provide a status update at 16:00 Friday. No review outcome is guaranteed by that time. This eight-item list is not the full contract closeout package or proof of substantial completion.',
    cast='Jules | Outgoing closeout coordinator\nMeera | Incoming closeout coordinator',
    culture=('Completed has several possible meanings', 'A trade contractor may use done to mean physical work has been performed. A coordinator may need verified acceptance before closing the record. Name both stages explicitly so a handover does not turn a report of correction into an unsupported sign-off.'),
    a='''How many items are verified closed? | Three | Eight | Five | None | Only Items 1 to 3 have both completion and linked acceptance records.
What is the status of Items 4 to 8? | Reported corrected but still open pending review | Accepted as closed | Removed from scope | Proved defective after review | Trade reports of correction do not satisfy the fictional process's review requirement.
What does Friday at 16:00 represent? | Meera's status-update commitment | Guaranteed closure of all five items | The start of every warranty | Automatic substantial completion | Meera commits to reporting the status, not to achieving a particular review outcome.''',
    vocabulary='''punch list | A list of incomplete or corrective items tracked toward completion. | update the punch list
snagging | Identifying and recording incomplete or defective work, common in some regional usage. | carry out snagging
closeout register | A record tracking the items and evidence required for project closeout. | maintain the closeout register
deficiency | Work or information that does not meet a relevant requirement. | record a deficiency
rectification | Work performed to correct an identified problem. | report rectification
trade contractor | A contractor responsible for a particular trade or work package. | coordinate with the trade contractor
reported complete | Described as finished by a reporting party but not necessarily verified. | distinguish reported complete
verified closed | Confirmed complete under the relevant closure process. | mark an item verified closed
verification evidence | Information supporting a check of the claimed correction or completion. | link verification evidence
acceptance criteria | Conditions used to determine whether an item meets the required standard. | apply acceptance criteria
rework | Work repeated or altered because the original result is unacceptable. | track rework
workmanship | The quality of execution of construction work. | assess workmanship
tolerance | The permitted variation from a specified dimension or performance. | verify the specified tolerance
mock-up | A sample construction or assembly used for review or testing. | compare with the approved mock-up
commissioning | A process for verifying and documenting that systems perform as required. | coordinate commissioning records
operation and maintenance manual | Information supporting operation, maintenance, and care of installed work or systems. | provide operation and maintenance manuals
record drawing | A drawing documenting relevant information about completed construction. | update record drawings
asset register | A structured inventory of assets and their relevant details. | populate the asset register
warranty | A stated undertaking concerning defects, performance, or remedy under applicable terms. | check warranty terms
defects liability period | A contract-defined period with specified obligations concerning defects. | verify the defects liability period
substantial completion | A contract-defined stage relating to readiness for the intended use. | determine substantial completion
final completion | The completion stage defined by the applicable contract requirements. | verify final completion
handover package | The collection of information and records transferred to the receiving party. | assemble the handover package
sign-off | Recorded acceptance or approval by the relevant authorized person. | obtain the required sign-off''',
    precision='Three verified closures out of eight equal 37.5% of this list by count. That does not measure the total project by value, effort, safety significance, or readiness for use. Five reported corrections remain awaiting review.',
    precision_extra='Punch-list closure, commissioning, manuals, record drawings, warranties, and contractual completion may involve different records and authorities. This small list does not replace the full closeout package or establish any warranty start date.',
    phrases='''State the list scope | This register covers eight Level 2 punch-list items.
Report verified closure | Items 1 to 3 are verified closed.
Qualify trade reports | Items 4 to 8 are reported corrected but await review.
Preserve the open status | Those five items remain open under our process.
Link the evidence | Each closed item links to its acceptance record.
Name the receiving owner | Meera has accepted coordination of the five reviews.
Separate ownership and completion | Accepting the handover does not close the items.
State the next commitment | I will provide a status update at 16:00 Friday.
Avoid guaranteeing results | That is an update time, not a promise of closure.
Qualify the percentage | Three of eight items is 37.5 percent by count.
Limit the metric | That percentage does not describe the whole project.
Check the criterion | What evidence is required before this item can be closed?
Keep documents traceable | Preserve the item number, location, record, and review history.
Distinguish the package | The punch list is only part of the closeout information.
Avoid assumed warranty terms | Check the contract and relevant warranty documents.
Close the handover | Please confirm receipt of the linked records and open-item responsibilities.''',
    notes='''Reported corrected | Attributes the claim without presenting it as verified acceptance.
Verified closed | Requires the specified closure basis, not an empty action column.
By count | Limits the percentage to the number of items.
Accepted coordination | Means ownership of follow-up, not acceptance of the physical work.
At 16:00 | Specifies the communication time, not the completion of every review.
Part of | Prevents one register from being mistaken for the entire closeout package.''',
    d='''Which handover summary is correct? | Three verified closed; five reported corrected and awaiting review | Eight closed because trades say done | Five closed and three awaiting correction | All items unreviewed with no records | The summary preserves the distinction between accepted closure and unverified correction reports.
What is the verified closure rate by item count? | 37.5% | 62.5% | 80% | 100% | Three divided by eight equals 0.375, or 37.5 percent.
What does Meera's acceptance establish? | Ownership of coordinating the outstanding reviews | Acceptance of all physical corrections | A warranty start date | Final completion of the whole project | Meera accepts the coordination task, not every technical or contractual decision.
Which statement about the closeout package is supported? | This list alone does not establish full contractual closeout. | Closing one punch item closes every permit. | All warranties begin when an email is sent. | Record drawings replace every inspection decision. | The eight-item register is explicitly only part of the broader closeout information.''',
    dialogue='''Jules | I want to hand over the eight-item Level 2 list properly. The summary saying almost done is too vague.
Meera | Let's use the [[closeout register::The closeout register records item-level status and evidence, separating verified closure from outstanding review.]] rather than that summary. Which items have completed the required review, and which are only reported corrected by the trade contractors?
Jules | Items 1 to 3 are completed and verified closed. Their acceptance records are linked. Items 4 to 8 have trade reports of correction but still await review.
Meera | Then those five remain open. [[Reported complete::Reported complete attributes a claim to the reporting party; it does not establish required verification or acceptance.]] and verified closed are different stages. I do not want the handover to erase that distinction just because the physical work may be finished.
Jules | The trades uploaded photographs for all five pending items and asked me to close the rows. The reviewer has not responded yet.
Meera | An attachment may be [[verification evidence::Verification evidence supports review of the work; an uploaded file does not itself supply an acceptance decision.]], but it is not the review result. We must check the applicable criterion and obtain the required decision before changing the closure status.
Jules | I preserved the item numbers, locations, earlier comments, and links to the latest submissions, so the reviewer can follow the history.
Meera | That will help us apply the [[acceptance criteria::Acceptance criteria determine whether a correction meets requirements, not merely whether someone has attempted the work.]]. Please make sure the receiving reviewer can find the original issue as well as the contractor's description of the correction.
Jules | The dashboard requests a completion percentage. Three divided by eight gives thirty-seven point five percent, but I hesitate to call the project thirty-seven point five percent complete.
Meera | You are right. It is the [[punch list::The punch list is the eight-item register counted here; its closure rate does not measure overall project completion.]] closure rate by count only. Items can differ greatly in effort, importance, and cost, and this list does not represent the whole project.
Jules | Can you accept coordination of the remaining five reviews? I want a named person rather than a note saying the project team will follow up.
Meera | Yes, I accept that responsibility. It is not [[sign-off::Sign-off is recorded acceptance or approval; accepting responsibility for review coordination is a different action.]] on the corrections themselves. I will coordinate the reviews and provide a status update at sixteen hundred on Friday.
Jules | I will record the update commitment. If responses are still outstanding on Friday, the report needs to say so.
Meera | Exactly. If a [[deficiency::A deficiency fails a relevant requirement and may still need correction despite a trade's report of completion.]] remains, the update must preserve it and identify the next responsible action. We should not close an item to make the promised report look better.
Jules | Manuals and record drawings are in the separate closeout folder. I will include the link; this list does not track their review.
Meera | Link them in the [[handover package::The handover package includes the relevant records; this punch list alone does not cover all closeout information.]]. A list of visible corrections is only one part of closeout. We must not imply that its completion settles every document or system obligation.
Jules | The client has asked whether this handover starts the warranties. I have not checked the relevant contract provisions or individual warranty terms.
Meera | Do not infer a [[warranty::A warranty has applicable terms; handing over this register does not establish its start date or coverage.]] start date from our coordination email. That needs the actual documents and authorized review, just as contractual completion status needs its own basis.
Jules | I will leave the record as three verified closures and five open reviews, with you as coordinator and Friday at sixteen hundred as the next status update.
Meera | I confirm that handover. It does not establish [[substantial completion::Substantial completion is contract-defined; accepting this register or counting closed items does not establish that stage.]] or final completion of the project. I will preserve the links and report the actual review outcomes as they become available.''',
    rehearsal=['Read the corrected conversation, distinguishing three verified closures from five reported corrections.', 'Switch roles; describe 37.5 percent as an item-count rate and Friday 16:00 as an update commitment.', 'Read the checked transfer twice, with Arun accepting four reviews rather than approving the corrections.'],
    transfer_title='Hand over a smaller register',
    transfer_setup='A six-item register has two verified closures and four reported corrections awaiting review. Coordinator Arun accepts follow-up and commits to an update at 11:00 Monday.',
    transfer='''Outgoing coordinator: "The number verified closed is ___." | two | Two is the supplied count of items with verified closure.
Arun: "I will coordinate the ___ outstanding reviews." | four | Four reported corrections still require review under the supplied status.
Outgoing coordinator: "The next update is at ___ Monday." | 11:00 | Eleven on Monday is the stated update time, not guaranteed closure.
Arun: "My acceptance concerns ___, not sign-off." | coordination | Arun accepts follow-up responsibility without accepting the physical work.'''))

BOOK['units'].append(unit(
    title='Claims, Disputes, and Documentation',
    scene='The delay is recorded; entitlement is not established',
    skill='Describe a delay and supporting records without presenting an unreviewed claim as a proven right.',
    brief='Delivery records show that a project item arrived at the end of working Day 11 rather than the planned end of Day 6, a five-working-day difference. Commercial coordinator Saira has $2,400 of reported extra labor costs, but the time records and causal link have not been reconciled. The impact on project completion, any concurrent delay, contract notice requirements, and entitlement to payment or time have not been reviewed. Project manager Theo finds a draft saying the delay automatically entitles us to compensation. They must prepare a factual internal summary for the authorized contract team, not make a legal determination.',
    cast='Saira | Commercial coordinator\nTheo | Project manager',
    culture=('A careful claim can still be firm', 'Separating facts from an unreviewed entitlement does not surrender a position. It makes the request intelligible and prevents a confident phrase from outrunning the records. Legal effect depends on the actual contract and jurisdiction, not on the forcefulness of the writer.'),
    a='''What delivery variance is documented? | Five working days | Five calendar weeks | Eleven working days late | No difference from plan | The arrival moved from the end of Day 6 to the end of Day 11.
What is the status of the $2,400? | Reported extra labor cost requiring reconciliation | Accepted compensation | A verified measure of every project loss | A contractual penalty already imposed | The cost is reported, but its records and causal connection have not been reconciled.
What is not yet established? | Entitlement to payment or time | The actual delivery day | The planned delivery day | The existence of a draft claim statement | Contractual entitlement and the effect on project completion remain unreviewed in the supplied facts.''',
    vocabulary='''claim | A request or assertion seeking a contractual or legal remedy or entitlement. | substantiate a claim
entitlement | A right to a remedy or benefit under the applicable basis. | assess entitlement
causation | The connection between an event and a claimed consequence. | establish causation
quantum | The amount of a claimed or assessed monetary remedy. | assess quantum
contemporaneous record | A record made at or near the time of the relevant event. | preserve contemporaneous records
chronology | An ordered account of events and their dates or times. | prepare a chronology
delay event | An occurrence alleged or shown to affect progress or timing. | document a delay event
concurrent delay | Overlapping delay effects considered under the applicable contract and analysis. | assess concurrent delay
disruption | Interference with the planned manner or efficiency of performing work. | distinguish disruption from delay
prolongation | An extension of the time spent on a project or activity. | assess prolongation effects
mitigation | Reasonable measures to limit adverse effects under the relevant circumstances. | document mitigation measures
notice provision | A contract term governing notification of specified matters. | review the notice provisions
time bar | A limitation linked to meeting a deadline under the applicable legal or contractual rules. | obtain advice on a time bar
reservation of rights | A statement intended to preserve a position, whose effect depends on the circumstances. | seek review of a reservation of rights
substantiation | Evidence and reasoning supporting an assertion or amount. | provide claim substantiation
cost reconciliation | Checking reported costs against supporting records and the relevant basis. | complete cost reconciliation
labor allocation | Assignment of labor time or cost to particular activities. | verify labor allocation
daily report | A record of the day's work, conditions, events, and resources. | consult the daily report
delivery docket | A record accompanying or confirming a delivery. | retain the delivery docket
correspondence register | An organized record of project communications. | update the correspondence register
liability | Legal responsibility determined under the applicable rules and facts. | distinguish alleged liability
disputed amount | A monetary figure whose validity or payment remains contested. | identify the disputed amount
settlement authority | Authority to agree a resolution on behalf of a party. | verify settlement authority
dispute resolution | The process for addressing disagreements under the applicable arrangement. | follow the dispute-resolution process''',
    precision='A five-day delivery variance is not automatically a five-day delay to project completion. The schedule logic, available time, actual effects, and other events require analysis. An event record and a contractual entitlement answer different questions.',
    precision_extra='The reported $2,400 is not yet a reconciled claim amount or an accepted payment. Do not treat the words reservation of rights or without prejudice as universal protection. Obtain authorized contract and legal review for actual notices and positions.',
    phrases='''State the event | Delivery occurred at the end of working Day 11.
Give the reference | The plan showed the end of working Day 6.
Quantify the difference | The recorded delivery variance is five working days.
Avoid a completion inference | The effect on project completion has not been assessed.
Separate the cost status | Extra labor of two thousand four hundred dollars is reported but unreconciled.
Ask for the records | Link the labor entries to the relevant work and dates.
Distinguish causation | We still need to establish which costs arose from this event.
Keep entitlement open | Entitlement to time or payment remains under review.
Correct the draft | Remove automatically entitled from the unreviewed summary.
Route contractual questions | The authorized team must review the contract and notice requirements.
Preserve chronology | Keep the planned date, actual date, and supporting delivery record together.
Avoid retrospective certainty | Do not rewrite an earlier observation as a later proven conclusion.
Address other events | Check whether other delays affected the same period.
Record mitigation accurately | Describe verified steps taken without inventing their effect.
Respect authority | I am not authorized to settle this dispute.
Close with a factual request | Please review the event, claimed effect, records, and applicable contractual basis.''',
    notes='''Reported | Attributes a cost figure without claiming verification.
Arising from | Makes a causal assertion that requires support.
Automatically entitled | Overstates an unreviewed contractual position.
Variance versus delay to completion | A moved delivery date does not establish the whole project's movement.
Under review | Identifies an unresolved assessment, not a rejected claim.
Preserve | Means retain the original evidence and traceable updates, not alter it to strengthen a position.''',
    d='''Which internal summary is supported? | Delivery five working days later than planned; completion impact and entitlement unreviewed | Five-day extension and $2,400 compensation approved | Supplier liable for all losses automatically | No records exist because entitlement is uncertain | The summary states the known event while preserving the unresolved schedule and contractual questions.
Which treatment of $2,400 is appropriate? | Label it reported and reconcile the labor records and causal basis. | Call it accepted payment because it appears in a spreadsheet. | Multiply it by five without a cost basis. | Delete supporting records once the total is typed. | The supplied amount needs reconciliation and a supported connection to the event before stronger claims.
Which distinction is essential? | The event, its consequences, and entitlement are separate questions. | A late delivery proves every claimed consequence. | A chronology replaces the contract. | Confident wording creates settlement authority. | Evidence of an event does not alone establish its effects or the right to a remedy.
Who should assess actual notice requirements? | The authorized contract team with appropriate legal review | Any worker choosing the strongest phrase | The PDF's fictional characters as legal advisers | A supplier who has not seen the contract | Actual notice obligations depend on the contract and jurisdiction and require appropriate authorized review.''',
    dialogue='''Theo | The draft says the delay automatically entitles us to compensation. Before that goes anywhere, let's separate the event from the contractual conclusion.
Saira | The [[chronology::The chronology records event order and timing, here the planned and actual delivery dates, without determining entitlement.]] is straightforward: planned arrival at the end of working Day 6, actual arrival at the end of Day 11. The delivery records support that difference.
Theo | So we can state a five-working-day delivery variance. We cannot yet state that project completion moved five days, because that effect has not been assessed.
Saira | Correct. We need the schedule analysis and any [[concurrent delay::Concurrent delay concerns overlapping delay effects; the possible effects of other events remain unreviewed here.]] review. The arrival dates alone do not show how every activity or the project completion point was affected.
Theo | The draft treats the two thousand four hundred dollars in extra labor as an established loss caused entirely by the late delivery. Is that supported?
Saira | It is reported cost, not completed [[cost reconciliation::Cost reconciliation checks reported costs against their supporting records and basis; the $2,400 remains unreconciled.]]. I need to match the time entries to activities and dates, check for duplication, and establish what the figure actually includes.
Theo | Even if the arithmetic matches the records, we still need to explain why those costs resulted from this event rather than another activity.
Saira | Yes. That is the [[causation::Causation connects the delivery event to the claimed consequence; correct arithmetic alone does not establish that connection.]] question. A correctly added spreadsheet does not prove the cause of every entry. We need a supported link, not simply costs occurring in the same week.
Theo | Please retain the original daily reports and delivery records. Do not rewrite the factual account to sound more decisive after our discussion.
Saira | I will preserve the [[contemporaneous records::Contemporaneous records were made near the event; retain them and distinguish later analysis instead of rewriting the evidence.]] and keep later analysis separate. Any correction needs a traceable explanation; it should not erase what was actually recorded at the time.
Theo | The site team says they sent an email. Please include it for contract review; we have not checked whether it meets the notice requirements.
Saira | Nor am I. The [[notice provisions::Notice provisions govern contractual notification requirements; a generic email cannot be assumed to satisfy the actual terms.]] require authorized review of the actual contract and applicable rules. This internal summary should flag the question, not invent a deadline or prescribe a legal form.
Theo | I want the contract team to assess the possible claim, not read this as us dropping it. How do we label the unresolved right to a remedy?
Saira | State that [[entitlement::Entitlement is the right to a remedy; identifying it as unreviewed neither proves it nor necessarily abandons it.]] remains under review and request assessment of the event, effects, and contractual basis. Accurate qualifications make the request clearer; they do not decide the ultimate position.
Theo | Even if a remedy exists, the reported figure may not be the recoverable amount. We need to distinguish the right to payment from its value.
Saira | Exactly. [[Quantum::Quantum concerns the monetary amount, separate from whether the claimant has a right to a remedy.]] needs its own substantiation. The two thousand four hundred remains reported and unreconciled, and we should not label it agreed compensation or an accepted liability.
Theo | The internal package will include the chronology, delivery records, labor entries, unresolved schedule effects, and questions for authorized reviewers.
Saira | Include verified [[mitigation::Mitigation concerns limiting adverse effects; report actual steps without inventing their success or legal consequences.]] steps where the records support them. Do not assume that discussing a recovery option proves it was implemented or that it prevented a particular amount of loss.
Theo | I will remove the automatic-entitlement statement and circulate the factual summary internally. I will not offer a settlement or communicate a final legal conclusion.
Saira | Good. [[Settlement authority::Settlement authority permits agreeing a resolution for a party; preparing records does not confer that power.]] is separate from preparing records. We can make the event and unresolved questions precise while leaving contractual decisions with the people authorized to make them.''',
    rehearsal=['Read the corrected exchange, keeping the five-working-day delivery variance separate from completion impact.', 'Switch roles for turns 11-20; distinguish reported $2,400, causation, entitlement, and settlement authority.', 'Read the checked transfer twice with three working days and $900 reported, without presenting either as an agreed remedy.'],
    transfer_title='Keep the three questions separate',
    transfer_setup='A delivery planned for the end of working Day 4 arrives at the end of Day 7. Reported additional labor is $900. Completion impact, cost reconciliation, and entitlement are unreviewed.',
    transfer='''Coordinator: "The delivery variance is ___ working days." | three | Day 7 minus Day 4 is a difference of three working days.
Manager: "The reported labor amount is $___." | 900 | Nine hundred dollars is the supplied reported additional labor amount.
Coordinator: "The effect on project completion remains ___." | unassessed | The brief says the completion impact has not been reviewed.
Manager: "The right to a remedy is the ___ question." | entitlement | Entitlement concerns the right to a remedy, separate from timing and amount.'''))
