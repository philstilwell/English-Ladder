"""Original Truck and Delivery Driver learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='truck-delivery-drivers',
    title='Truck and Delivery Driver English',
    cover_label='ENGLISH FOR DELIVERY AND DISPATCH',
    cover_title='Truck and\nDelivery Driver',
    cover_size=37,
    tagline='Clear details. Reliable handovers.',
    audience='For truck drivers, delivery drivers, dispatchers, receiving staff, and route coordinators.',
    map_intro='Eight delivery conversations: correct a destination note, reconcile carton counts, update an arrival estimate, describe visible damage, discuss an unavailable recipient, explain service boundaries, match a return, and hand over unfinished route records.',
    notes_title='Keep the delivery story accurate.',
    notes_intro='A clear delivery conversation connects the shipment reference to a checked fact and a specific next action. It distinguishes an estimate from an appointment, an observation from a cause, and a received shipment from a successfully uploaded record.',
    field_notes=[
        ('Confirm the receiving point', 'A correct street address may still lead to the wrong suite or entrance. Repeat the consignee, unit number, and receiving point, and refer conflicting instructions for correction.', '"Suite 4 uses the staffed front desk; the rear annex belongs to suite 6."'),
        ('Give the basis of a discrepancy', 'State the documented count and the physical count together. Distinguish external packaging from uninspected contents, and do not turn a difference into an unsupported finding of loss or fault.', '"The document lists twelve cartons; we count eleven. Contents have not been checked."'),
        ('Separate estimates and commitments', 'An estimated arrival does not extend a receiving cutoff or confirm a later slot. Give a time for the next update without presenting it as a guaranteed delivery time.', '"Arrival is estimated at 11:40; I will update you by 10:40 about the receiving arrangement."'),
        ('Hand over ownership and status', 'Name each unfinished item separately and confirm who will act next. A person accepting a follow-up does not mean that a receipt has uploaded or a refused shipment has been resolved.', '"Jo will check the missing receipt upload and contact customer service about the refusal."'),
    ],
    scope_note='All shipments, people, businesses, times, references, and service arrangements are fictional. This book teaches workplace English, not driving, loading, vehicle operation, cargo securement, legal liability, or regulatory compliance. Calls occur while the driver is safely parked or away from driving duties. Follow applicable road and working-time rules, carrier procedures, site safety requirements, and emergency arrangements. Do not use these dialogues as authorization to move, unload, leave, sign for, or alter the service for a real shipment.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Heavy and Tractor-trailer Truck Drivers.',
             url='https://www.bls.gov/ooh/transportation-and-material-moving/heavy-and-tractor-trailer-truck-drivers.htm',
             note='Occupational context for driver-dispatch communication, delivery records, and reported problems. These original conversations do not provide vehicle-operation instructions.', checked='1 October 2026'),
        dict(title='FedEx. Shipping Terms and Definitions.',
             url='https://www.fedex.com/en-us/shipping/glossary.html',
             note='Terminology reference for shipment parties, transport documents, tracking, and additional services. Fictional service arrangements are not FedEx terms or quotations.', checked='1 October 2026'),
        dict(title='Federal Motor Carrier Safety Administration. Hours of Service.',
             url='https://www.fmcsa.dot.gov/regulations/hours-of-service',
             note='Context for distinguishing a customer request from the rules and constraints governing actual driver availability. No numerical driving-time rule is taught in this book.', checked='1 October 2026'),
        dict(title='Occupational Safety and Health Administration. Trucking Industry: Loading and Unloading.',
             url='https://www.osha.gov/trucking-industry/loading-unloading',
             note='Context for keeping language practice separate from site-specific loading and unloading training. The book does not authorize handling equipment or entering loading areas.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Confirming the delivery destination',
    scene='The right address, the wrong entrance',
    skill='Resolve conflicting location information through specific questions, a complete read-back, and a request to correct the record.',
    brief='Driver Leo is safely parked and calls receiving contact Hana about shipment 418 for Alder Books, 26 Mill Street, suite 4. The route note says rear annex. Hana confirms that the rear annex belongs to suite 6 and that suite 4 receives through its staffed front desk. Leo must report the conflict to dispatch for correction. The shipment has not been handed over, and this call does not itself update the route record or authorize a different delivery destination.',
    cast='Leo | Delivery driver\nHana | Receiving contact',
    culture=('Read back the detail that changes the action', 'A vague confirmation such as yes, this building can conceal a wrong suite or entrance. Ask about the specific receiving point, repeat the corrected details together, and explain who must amend the route note before treating the record as corrected.'),
    a='''Who is the shipment for? | Alder Books in suite 4 | Any business in the building | Alder Books in suite 6 | The rear-annex tenant only | The shipment names Alder Books at suite four, not suite six.
What is wrong with the route note? | The rear annex belongs to suite 6 | The street number is missing | The shipment has already arrived elsewhere | The front desk is unstaffed | Hana identifies the rear annex as belonging to a different suite.
What remains to be done? | Dispatch must correct the conflicting note | Mark the shipment handed over | Change the consignee to suite 6 | Describe the record as already corrected | The call establishes the conflict but does not itself amend the dispatch record.''',
    vocabulary='''consignee | Named party intended to receive a shipment. | confirm the consignee
shipper | Party sending the goods. | identify the shipper
carrier | Business transporting the shipment. | contact the carrier
shipment reference | Identifier used to locate a particular shipment. | quote the shipment reference
delivery address | Stated location to which goods are to be delivered. | verify the delivery address
suite number | Identifier for a separate unit within a building. | read back the suite number
receiving point | Specific place where the intended recipient receives goods. | confirm the receiving point
route note | Written information supplied for a delivery stop. | check the route note
rear annex | Additional part of a building located at the back. | distinguish the rear annex
staffed front desk | Front reception point with personnel present. | identify the staffed front desk
entrance | Access point into a building or site. | clarify the entrance
address line | Separate part of a written address. | preserve the address line
dispatch | Team coordinating vehicles, drivers, and delivery instructions. | notify dispatch
receiving contact | Person contacted about receiving a shipment. | call the receiving contact
location conflict | Inconsistency between two descriptions of a destination. | report a location conflict
read-back | Spoken repetition used to check exact information. | request a complete read-back
destination correction | Amendment to incorrect destination information. | request a destination correction
site instruction | Direction applying at a particular receiving location. | verify the site instruction
delivery record | Recorded information about a delivery and its status. | update the delivery record
handover | Transfer of goods to the appropriate receiving party. | confirm the handover
stop number | Identifier for one location in a planned route sequence. | state the stop number
landmark | Recognizable feature used to describe a location. | clarify a landmark
adjacent unit | Neighboring unit that may have a different occupant. | distinguish an adjacent unit
record amendment | Authorized change to existing recorded information. | confirm the record amendment''',
    precision='The street address is not the dispute. Suite 4 and suite 6 use different receiving points. The shipment remains for Alder Books in suite 4; identifying the front desk does not transfer the shipment to another consignee.',
    precision_extra='Confirmation by a receiving contact and amendment of the route record are separate steps. Leo can accurately report the corrected receiving information while stating that dispatch has not yet corrected the note or completed the delivery.',
    phrases='''Identify the shipment | I am calling about shipment 418 for Alder Books.\nConfirm the street | Is the address 26 Mill Street?\nCheck the unit | The shipment lists suite 4; is that your unit?\nName the conflict | My route note says rear annex.\nDistinguish the annex | The rear annex belongs to suite 6.\nAsk for the receiving point | Where does suite 4 receive deliveries?\nGive the confirmed location | We use the staffed front desk.\nRead back the full detail | Alder Books, suite 4, staffed front desk; correct?\nPreserve the consignee | The recipient has not changed.\nSeparate neighbors | Suite 6 is a different unit.\nRefer the correction | I will ask dispatch to correct the note.\nKeep status accurate | The route record has not been amended yet.\nAvoid claiming handover | The shipment has not been handed over.\nCheck the source | Are you the receiving contact for suite 4?\nExplain the purpose | I want to avoid treating the annex as your receiving point.\nClose the clarification | I have the corrected information to report to dispatch.''',
    notes='''For versus at | For names the intended recipient; at gives the location.\nBelongs to | Connects the annex specifically to suite 6.\nNot yet | Preserves an unfinished record update without implying refusal.\nStaffed | Describes personnel being present, not a general delivery authorization.\nThis building | Too broad when several units use different receiving points.\nCorrected information | Can be known before the official record has been amended.''',
    d='''Which read-back matches the facts? | Alder Books, suite 4, staffed front desk. | Alder Books, suite 6, rear annex. | Any desk at 26 Mill Street. | Suite 4, unattended rear annex. | The read-back preserves the consignee, correct suite, and confirmed receiving point.
Which statement wrongly reports completion? | Dispatch has already corrected the note. | I will report the conflict to dispatch. | The annex belongs to suite 6. | The shipment has not been handed over. | Dispatch correction is still required and has not occurred in this call.
Which question targets the actual ambiguity? | Does the rear annex serve suite 4 or suite 6? | Is Mill Street a street? | Should I change the consignee automatically? | Can every tenant sign for every delivery? | The ambiguity concerns which suite uses the named receiving point.
What should remain unchanged? | The intended consignee, Alder Books | The incorrect rear-annex note | The assumption that all suites share an entrance | A false completed-handover status | Correcting the receiving-point information does not replace the intended consignee.''',
    dialogue='''Leo | Hello, I am parked nearby with shipment 418 for Alder Books. Could I check the receiving entrance before I report a problem with my instructions?
Hana | Certainly. I am the [[receiving contact::Receiving contact identifies Hana's role in confirming where Alder Books accepts its shipment.]] for Alder Books. What does your paperwork say about the address and the entrance?
Leo | It gives 26 Mill Street, suite 4, but the route note says rear annex. I want to make sure those details refer to the same place.
Hana | The street address is right. The [[rear annex::Rear annex is the conflicting location, which belongs to suite six rather than Alder Books.]] belongs to suite 6, not us. Alder Books is in suite 4.
Leo | Thank you. That sounds like an entrance problem rather than a different street address. Where does your team normally receive a delivery for suite 4?
Hana | Our [[receiving point::Receiving point names the specific place for suite four, beyond the shared street address.]] is the staffed front desk. Please do not treat the annex as our receiving area simply because it shares the building.
Leo | Let me repeat that: Alder Books, 26 Mill Street, suite 4, staffed front desk. The rear annex is associated with suite 6. Is that accurate?
Hana | Yes, that [[read-back::Read-back repeats the corrected details so Hana can check the complete destination information.]] is accurate. The suite number matters because the two units do not use the same receiving point.
Leo | I have not handed anything over. I will contact dispatch about the conflict so the next instruction is tied to the right unit.
Hana | That is helpful. The [[consignee::Consignee remains Alder Books; correcting the entrance does not change the intended receiving party.]] is still Alder Books. We are clarifying our receiving location, not asking you to deliver to another business.
Leo | Exactly. I also want the incorrect note corrected, rather than leaving a future driver with the same rear-annex instruction.
Hana | Please ask [[dispatch::Dispatch is the coordinating team that must amend the conflicting route information.]] to make that correction. I can confirm our location, but this phone call does not update your route system.
Leo | Understood. I will say the receiving contact confirms the staffed front desk for suite 4, while the existing note incorrectly points to the annex.
Hana | Yes. Describe it as a [[location conflict::Location conflict captures the disagreement between the route note and the confirmed receiving information.]] so they know exactly what needs checking. The street number itself is not the problem.
Leo | Before I call them, could you confirm once more that suite 6 is separate from Alder Books? I do not want to merge the two units.
Hana | It is an [[adjacent unit::Adjacent unit distinguishes suite six from the intended recipient even though both share the building.]], not our delivery destination. Your shipment remains for suite 4, and our receiving point is the staffed front desk.
Leo | Thank you. I have the details for dispatch now. I will not describe the delivery as completed just because we have clarified the entrance.
Hana | Correct. No [[handover::Handover means transfer of the shipment, which has not occurred during this clarification call.]] has occurred in this conversation. We have resolved which receiving information you need to report.
Leo | I will keep those two things separate: the confirmed receiving details and the route note that still needs to be changed.
Hana | Good. The [[record amendment::Record amendment remains pending; accurate information in a call is not an already updated route record.]] is still pending with dispatch. The corrected location to report is suite 4, staffed front desk.''',
    transfer_title='Correct another entrance conflict',
    transfer_setup='Shipment 529 names Birch Print, suite 2 at 14 Oak Lane. A side-door note belongs to suite 3. The receiving contact confirms suite 2 uses the main reception. Dispatch correction is pending.',
    transfer='''Driver: "The consignee is ___." | Birch Print | Birch Print remains the named receiving party despite the entrance correction.
Receiver: "Suite 2 uses the main ___." | reception | Main reception is the confirmed receiving point for suite two.
Driver: "The side-door note belongs to suite ___." | 3 | Suite three is the different unit associated with the side door.
Receiver: "The record correction is still ___." | pending | Dispatch has not yet amended the conflicting route note.''',
))


BOOK['units'].append(unit(
    title='Checking shipment counts',
    scene='Twelve on paper, eleven at receiving',
    skill='Compare document and physical quantities, distinguish cartons from contents, and report an unresolved shortage without assigning blame.',
    brief='At Finch Office Supplies, driver Priya and receiver Ben compare a bill of lading listing twelve cartons with their physical count of eleven. They agree on eleven present cartons. The contents have not been checked, and dispatch has not located a twelfth carton. The difference is one carton against the listed quantity, not a verified count of missing individual products. They need a factual discrepancy report and a dispatch follow-up, not a guess about where the carton was lost.',
    cast='Priya | Driver\nBen | Receiver',
    culture=('Count together, describe the difference neutrally', 'A receiving discrepancy can create pressure to assign blame immediately. State both figures and their sources, then identify what has not been checked. Agreement about a physical count does not establish the contents or the cause of a shortage.'),
    a='''What does the bill of lading list? | Twelve cartons | Eleven individual products | One carton | Twelve pallets | The document lists twelve cartons as the shipment quantity.
What do Priya and Ben physically count? | Eleven cartons | Twelve cartons | Eleven verified products | One opened carton | Both people agree on eleven present cartons at receiving.
What remains unknown? | Contents and the location of the twelfth carton | The listed carton count | The agreed physical carton count | The difference between twelve and eleven | Contents are unchecked, and dispatch has no location for the twelfth carton.''',
    vocabulary='''bill of lading | Transport document recording shipment details and carriage terms, often BOL. | compare the bill of lading
carton | Individual outer box counted in this shipment. | count the cartons
piece count | Number of stated shipping units, with the unit defined. | verify the piece count
listed quantity | Amount recorded on the relevant document. | state the listed quantity
physical count | Count of units actually observed. | perform a physical count
shortage | Quantity below the expected or documented amount. | report a carton shortage
discrepancy | Difference between records or observations requiring clarification. | document a discrepancy
recount | A further count to check the original figure. | request a recount
shipping unit | Unit used for shipment counting, such as a carton or pallet. | identify the shipping unit
pallet | Platform used to support and move grouped goods. | distinguish pallets from cartons
packing list | Document describing items packed in a shipment. | consult the packing list
line item | Separate entry on a shipment or order document. | compare the line item
contents | Goods inside the outer packaging. | distinguish cartons from contents
item quantity | Number of individual goods rather than outer packages. | check the item quantity
unchecked | Not yet examined or verified. | mark contents as unchecked
short by | Expression stating the amount below an expected quantity. | report short by one carton
overage | Quantity above the expected or documented amount. | report an overage
quantity basis | Unit and reference used for a numerical comparison. | state the quantity basis
receiving tally | Count recorded when goods arrive. | compare the receiving tally
trace request | Request to investigate the location or movement of a shipment. | raise a trace request
unlocated carton | Carton whose current location has not been established. | report the unlocated carton
dispatch follow-up | Further action by the delivery coordination team. | request dispatch follow-up
joint count | Count checked by two parties together. | confirm the joint count
cause attribution | Statement assigning a reason or responsibility for an event. | avoid unsupported cause attribution''',
    precision='Twelve listed cartons minus eleven counted cartons gives a one-carton discrepancy. That calculation says nothing about the number of individual products missing or the contents of the cartons present, because no contents check has occurred.',
    precision_extra='A carton, pallet, and individual item are different counting units. State the unit every time figures could be confused. A shared count improves clarity but does not prove where an unlocated carton went or who caused the discrepancy.',
    phrases='''Name the document | The bill of lading lists twelve cartons.\nState the observation | We have counted eleven cartons here.\nGive the difference | That is one carton short of the listed quantity.\nKeep units explicit | I mean cartons, not individual products.\nConfirm agreement | Do you also have eleven in your count?\nSeparate contents | We have not checked the contents.\nState the location limit | Dispatch has not located the twelfth carton.\nAvoid blame | We do not yet know the cause of the difference.\nPreserve both figures | Please record twelve listed and eleven counted.\nAsk for follow-up | Can dispatch investigate the unlocated carton?\nAvoid inventing a result | I cannot say it is at another depot.\nCorrect a broad claim | Eleven cartons does not mean eleven products.\nKeep the source clear | Twelve comes from the document; eleven comes from our count.\nDistinguish a trace | A trace request is not a confirmed location.\nSummarize the issue | One carton is unaccounted for against the listed quantity.\nClose with the open item | The carton discrepancy remains unresolved.''',
    notes='''Short by one | Gives the size and direction of the difference.\nListed versus counted | Separates a document figure from a physical observation.\nCartons versus contents | Outer packages do not establish the number or condition of goods inside.\nUnlocated versus lost | Lack of a known location is not a completed investigation of loss.\nWe both count | Establishes agreement without establishing the cause.\nAgainst | Introduces the reference amount used for comparison.''',
    d='''Which discrepancy report is accurate? | Twelve cartons listed, eleven counted, contents unchecked. | Twelve products listed, eleven products received. | Eleven cartons prove all contents are complete. | Dispatch lost one carton at the depot. | The accurate report preserves both carton figures and the unchecked contents.
Which calculation matches the count? | One carton below the listed quantity. | One carton above the listed quantity. | Eleven cartons missing. | Twelve cartons missing. | Twelve listed minus eleven counted leaves a one-carton difference.
Which statement exceeds the evidence? | The missing carton is definitely at another depot. | Dispatch has not located the twelfth carton. | Both people count eleven cartons. | The contents have not been checked. | No confirmed location is supplied, so the depot claim is unsupported.
What should a follow-up preserve? | The quantity basis and unresolved location. | An invented count of missing products. | A claim that contents were inspected. | Automatic blame assigned to the driver. | The follow-up must retain carton units and the still-unknown location.''',
    dialogue='''Ben | I have eleven cartons on my receiving tally, but the bill of lading says twelve. Can we make sure we are counting the same thing?
Priya | Yes. The [[listed quantity::Listed quantity is twelve cartons on the document, distinct from the eleven physically counted.]] is twelve cartons. I also count eleven cartons here, so our physical counts agree.
Ben | Then we are one short, not eleven short. I want the report to be clear because someone may read only the first line.
Priya | Exactly. We are [[short by::Short by introduces the amount below the documented count: one carton rather than eleven.]] one carton against the twelve listed. I will keep both numbers in the message rather than reporting the difference alone.
Ben | Should I write that one product is missing? The boxes contain office supplies, but I have not opened them to check what is inside.
Priya | Keep the [[quantity basis::Quantity basis must remain cartons; unchecked contents do not establish how many individual products are missing.]] as cartons. One missing outer box does not tell us how many individual products it contains.
Ben | Right. We have checked the number of boxes, not the contents. I do not want my count to suggest a full product inspection.
Priya | We should state that the [[contents::Contents means the goods inside the cartons, which neither party has inspected here.]] are unchecked. That leaves a clear distinction between what we counted and what still needs verification.
Ben | Have you heard from dispatch about the twelfth carton? I would prefer a confirmed location rather than telling our team it will arrive later.
Priya | Dispatch has no confirmed location for the [[unlocated carton::Unlocated carton states the present information limit without declaring a final loss or a known location.]]. I cannot say it is at another depot or promise a later delivery.
Ben | That is disappointing, but I would rather know. Please do not let the report say everything is complete just because we agree on eleven.
Priya | It will record the [[discrepancy::Discrepancy is the difference between twelve documented cartons and eleven observed cartons, not a completed delivery count.]] explicitly: twelve listed, eleven counted, contents unchecked, and the twelfth carton not located.
Ben | Could the bill of lading itself be wrong? I am asking whether that is one possibility, not saying we know it was written incorrectly.
Priya | That needs checking too. Our [[joint count::Joint count confirms agreement on what is present but does not establish whether the paperwork or movement caused the difference.]] establishes eleven here; it does not tell us whether the document or the shipment movement explains the difference.
Ben | Good. I will avoid writing that the driver lost a carton. We have a shortage against the document, but we have not established responsibility.
Priya | Thank you. Unsupported [[cause attribution::Cause attribution assigns responsibility or a reason, neither of which follows from this count alone.]] would go beyond what either of us observed. A precise count gives dispatch something concrete to investigate.
Ben | What should the next person check first? I want the follow-up attached to this shipment and not confused with an individual-item stock query.
Priya | The [[dispatch follow-up::Dispatch follow-up concerns locating or explaining the unaccounted-for carton, while the existing count stays explicit.]] should use the shipment details and the one-carton difference. It must not invent an item count or a location.
Ben | Let me read the message back: twelve cartons listed, eleven counted, contents unchecked, and dispatch has not located the twelfth. Is that complete?
Priya | Yes. That preserves the [[physical count::Physical count is the eleven cartons observed, which must remain separate from the document's twelve.]] and the limits of our information. The discrepancy remains open until the relevant checks establish more.''',
    transfer_title='Report another count difference',
    transfer_setup='At Cedar Supplies, the document lists nine cartons. Driver and receiver count eight. Contents are unchecked, and the ninth carton has no confirmed location.',
    transfer='''Driver: "The document lists ___ cartons." | nine | Nine is the documented amount against which the actual count is compared.
Receiver: "The physical count is ___ cartons." | eight | Eight is the number of cartons actually counted at receiving.
Driver: "The shipment is short by ___ carton." | one | Nine listed minus eight counted creates a one-carton difference.
Receiver: "The contents remain ___." | unchecked | No inspection of the goods inside the cartons has occurred.''',
))


BOOK['units'].append(unit(
    title='Updating an arrival estimate',
    scene='An estimate after the cutoff',
    skill='Compare an estimated arrival with a receiving deadline and commit to a specific update without promising acceptance.',
    brief='Driver Omar is safely parked and calls dispatcher Mei at 10:20. His current estimated arrival is 11:40, but the receiver stops accepting this delivery at 11:30. No later slot has been confirmed. Mei can contact receiving and update Omar by 10:40, even if the question remains unresolved. The conversation must preserve the ten-minute mismatch, distinguish the update deadline from arrival, and avoid implying that the driver should rush or exceed any applicable driving or working-time limits.',
    cast='Omar | Driver\nMei | Dispatcher',
    culture=('An early warning is useful before there is a solution', 'A dispatcher needs the current estimate, the receiving constraint, and the next contact time. Report a likely mismatch plainly. Do not hide it inside an optimistic phrase such as nearly on time or turn a request for a later slot into an accepted appointment.'),
    a='''When is arrival currently estimated? | 11:40 | 10:20 | 10:40 | 11:30 | The arrival estimate is eleven forty, separate from the call and update times.
How does the estimate compare with the cutoff? | Ten minutes after it | Ten minutes before it | Exactly at it | One hour before it | Eleven forty is ten minutes later than the eleven-thirty receiving cutoff.
What can Mei commit to? | An update by 10:40, even if unresolved | Delivery by 10:40 | Automatic acceptance at 11:40 | A confirmed later slot already booked | Mei can provide a communication update without guaranteeing the receiving decision.''',
    vocabulary='''estimated time of arrival | Provisional expected arrival time, commonly ETA. | update the estimated time of arrival
receiving cutoff | Latest stated time for accepting the delivery. | confirm the receiving cutoff
delivery window | Time range arranged or expected for a delivery. | clarify the delivery window
appointment slot | Specific time allocation that requires confirmation. | request an appointment slot
later slot | Receiving time after the original limit or booking. | ask about a later slot
time mismatch | Difference between an estimate and an applicable timing constraint. | report a time mismatch
status update | Message giving the current position of an issue. | provide a status update
update deadline | Latest time promised for the next communication. | state the update deadline
by | No later than a stated time. | update by 10:40
at | At a particular stated time. | call at 10:20
after | Later than a reference time. | arrive after the cutoff
before | Earlier than a reference time. | contact receiving before arrival
receiving confirmation | Explicit acceptance of the proposed receiving arrangement. | obtain receiving confirmation
provisional | Subject to change rather than guaranteed. | give a provisional estimate
revised estimate | Updated expectation based on current information. | issue a revised estimate
delay notification | Notice that timing may differ from the expected plan. | send a delay notification
schedule constraint | Limit affecting whether a proposed time is workable. | explain a schedule constraint
on duty | Working status relevant to actual driver rules and records. | clarify on-duty status
hours of service | Applicable limits and rest requirements governing covered drivers, often HOS. | follow hours-of-service requirements
driver availability | Whether a driver can lawfully and practically perform the proposed work. | verify driver availability
pending response | Reply that has not yet been received. | record a pending response
rescheduling request | Proposal to change the arranged time, not automatic acceptance. | submit a rescheduling request
confirmed appointment | Receiving arrangement explicitly agreed by the appropriate parties. | distinguish a confirmed appointment
communication commitment | Promise to provide information, distinct from promising an outcome. | keep the communication commitment''',
    precision='At 10:20, the estimate is 11:40 and the cutoff is 11:30: a ten-minute mismatch. By 10:40 is the promised update deadline. None of those facts confirms permission to arrive after the cutoff.',
    precision_extra='A customer timing request does not override safe driving, actual working-time requirements, or carrier procedures. This lesson practices reporting the timing conflict and obtaining a decision; it supplies no instruction to change speed, rest, or duty records.',
    phrases='''State the call time | It is 10:20, and I am parked for this call.\nGive the estimate | My current estimated arrival is 11:40.\nName the cutoff | Receiving has an 11:30 cutoff.\nQuantify the mismatch | That puts the estimate ten minutes after the cutoff.\nAvoid minimizing | We should flag the mismatch now.\nKeep the estimate provisional | 11:40 is an estimate, not a guarantee.\nAsk about confirmation | Has receiving agreed to a later slot?\nState the open status | No later slot is confirmed yet.\nAssign the contact | I will contact receiving about the timing.\nCommit to an update | I will update you by 10:40.\nKeep the commitment even if unresolved | You will hear from me even if their answer is still pending.\nDistinguish the times | 10:40 is the update deadline, not the arrival time.\nReject a false appointment | A request for 11:40 is not a confirmed appointment.\nProtect the factual record | Keep the 11:30 cutoff in the message.\nAvoid pressure to rush | We need a receiving decision, not a promise to make up time.\nClose the handoff | I own the receiving call and the next update.''',
    notes='''By versus at | By gives a latest communication time; at names a particular time.\nEstimated | Marks expected arrival as provisional rather than guaranteed.\nTen minutes after | Quantifies the mismatch without claiming acceptance.\nEven if | Keeps the update commitment valid when the decision is unfinished.\nRequested versus confirmed | A proposed later slot needs an actual accepting response.\nMake up time | Can imply unsafe pressure; clarify the receiving plan instead.''',
    d='''Which update is accurate? | ETA 11:40; cutoff 11:30; later slot unconfirmed. | ETA 10:40; cutoff extended automatically. | Arrival guaranteed by 11:30. | Receiving has accepted 11:40. | The statement retains the estimate, unchanged cutoff, and unconfirmed later arrangement.
What does by 10:40 refer to? | The deadline for Mei's update | Guaranteed delivery completion | A new receiving cutoff | The time Omar must begin driving | Ten forty is a communication deadline, not a movement or delivery instruction.
Which sentence turns a request into a false result? | I will ask, so your 11:40 appointment is confirmed. | I will ask whether a later slot is possible. | Their response is still pending. | I will update you even without a final answer. | Asking receiving does not establish that receiving has accepted a later appointment.
What should Omar do linguistically? | Report the timing conflict without promising to rush. | Promise to beat the estimate by any means. | Omit the cutoff to sound reassuring. | Call the estimate a guarantee. | The useful message states the conflict and avoids unsafe or unsupported timing promises.''',
    dialogue='''Omar | Mei, I am parked and checking in at 10:20. My current estimate is 11:40, which does not fit the receiving time on the route.
Mei | I see the [[receiving cutoff::Receiving cutoff is eleven thirty, the stated acceptance limit that the later estimate does not change.]] is 11:30. Your estimate is ten minutes after that, so we need to contact them before assuming they can receive you.
Omar | Yes. I wanted to flag it now instead of arriving and finding the office unable to accept the shipment. I have no later confirmation.
Mei | I will make a [[rescheduling request::Rescheduling request asks for a different arrangement but is not itself an accepted appointment.]] with receiving. Until they respond, we should keep the original cutoff and the unconfirmed status in the record.
Omar | Please keep 11:40 as an estimate, too. I do not want them to hear it as a guaranteed appointment that I have already accepted.
Mei | Agreed. The [[estimated time of arrival::Estimated time of arrival is the provisional eleven-forty expectation, not a promise or a receiving agreement.]] remains 11:40. I will explain that it falls after their stated cutoff and ask what arrangement they can offer.
Omar | When should I expect to hear back? A clear update time would help even if receiving has not made a decision by then.
Mei | I will update you [[by::By sets ten forty as the latest promised update time, not the delivery time.]] 10:40. That is the latest time for my next message, not a promise that the delivery will be completed then.
Omar | Understood. So if you are still waiting at 10:40, you will tell me that, rather than leaving me to assume the later time is accepted?
Mei | Exactly. You will receive a [[status update::Status update communicates the current position even when the requested receiving decision remains unresolved.]] even if their answer is pending. Silence should not become an unofficial confirmation.
Omar | I appreciate that. The ten-minute difference may sound small, but it still puts the estimate outside the stated receiving limit.
Mei | Correct. The [[time mismatch::Time mismatch is the ten-minute difference between the eleven-forty estimate and the eleven-thirty cutoff.]] needs a decision from receiving. We should not describe it as effectively on time or quietly extend their cutoff ourselves.
Omar | Nor should I promise to make up the difference on the road. I can provide an honest estimate, but I cannot solve their schedule by rushing.
Mei | Right. Actual [[driver availability::Driver availability depends on lawful and practical conditions; a customer's request does not remove those constraints.]] and applicable rules still matter. We need an agreed receiving plan, not an unsupported promise to recover time.
Omar | Have we confirmed any alternative yet, or are you about to make the first contact about a later slot?
Mei | No [[later slot::Later slot remains unconfirmed because receiving has not yet accepted a revised arrangement.]] is confirmed. I am taking the contact action now, and I will keep that distinct from whatever answer they eventually give.
Omar | Please repeat the three times once: the call, the arrival estimate, and your update deadline. That will keep my notes clear.
Mei | Call at 10:20, arrival estimate 11:40, and my [[update deadline::Update deadline is ten forty, distinct from the ten-twenty call and eleven-forty arrival estimate.]] is 10:40. Receiving still has the 11:30 cutoff.
Omar | That matches my notes. I will await your update without treating the proposed later arrival as a booking.
Mei | Good. A [[confirmed appointment::Confirmed appointment requires an actual accepted arrangement; the present conversation establishes only a request and an update commitment.]] still needs receiving approval. I own that contact and will update you by 10:40, even if unresolved.''',
    transfer_title='Separate another estimate and update',
    transfer_setup='A parked driver calls at 13:00. Arrival is estimated at 14:20 and receiving closes for this delivery at 14:00. No later slot is agreed. Dispatcher Jo promises an update by 13:15.',
    transfer='''Driver: "Estimated arrival is ___." | 14:20 | Fourteen twenty is the provisional arrival time, not a confirmed appointment.
Dispatcher: "That is ___ minutes after the cutoff." | twenty | Fourteen twenty follows the fourteen-hundred cutoff by twenty minutes.
Driver: "Your update is due by ___." | 13:15 | Thirteen fifteen is the promised communication deadline in the new scenario.
Dispatcher: "A later slot remains ___." | unconfirmed | Receiving has not agreed to an alternative delivery time.''',
))


BOOK['units'].append(unit(
    title='Describing a delivery exception',
    scene='A crushed corner is not a finding of fault',
    skill='Record visible packaging condition, attribute a customer concern, and resist unsupported conclusions about contents or responsibility.',
    brief='At Grove Studio, receiver Ellis points out a crushed lower corner on one carton. Its contents remain unopened and uninspected. Ellis asks driver Nia to describe it as broken equipment caused by the driver. Nia can accurately report the visible crushed corner and the concern about possible internal damage, but neither internal damage nor its cause is established. The exchange ends with a factual description and a referral for follow-up, not a liability finding, claim approval, or decision about accepting the shipment.',
    cast='Ellis | Receiver\nNia | Driver',
    culture=('Acknowledge the concern without adopting the conclusion', 'A customer may use strong causal language because the visible condition is upsetting. Show that you take the concern seriously while separating what is observable from what is alleged. Factual wording preserves the issue for proper review; it does not dismiss the customer.'),
    a='''What is actually visible? | A crushed lower corner on one carton | Broken equipment inside every carton | A driver dropping the carton | Undamaged internal contents | The observed condition concerns one carton corner, not inspected equipment inside.
What has not been checked? | The contents | The presence of the crushed corner | The receiving business name | The fact that a concern was raised | The carton remains unopened, so its internal contents have not been inspected.
Which result is not established? | Internal damage and its cause | A visible packaging concern | A request for follow-up | The lower-corner location | Neither the condition of the equipment nor responsibility follows from the observed packaging alone.''',
    vocabulary='''delivery exception | Irregularity affecting a delivery; formal status meanings depend on the carrier. | report a delivery exception
external packaging | Outer material surrounding the shipped goods. | describe external packaging
crushed corner | Corner visibly compressed or deformed. | record the crushed corner
visible condition | State that can be directly observed. | report the visible condition
internal damage | Damage to goods inside the package. | distinguish internal damage
unopened carton | Outer box whose contents have not been accessed. | identify the unopened carton
inspection | Examination to establish condition or other facts. | request an inspection
condition notation | Written note describing observed condition. | make a condition notation
delivery receipt | Record associated with receiving a delivery. | review the delivery receipt
damage allegation | Statement claiming damage that requires factual evaluation. | attribute a damage allegation
attributed statement | Report clearly identified as someone else's account. | preserve an attributed statement
causal claim | Statement asserting what produced a result. | qualify a causal claim
fault | Responsibility for an event, not established by appearance alone. | avoid assigning fault
liability | Legal responsibility requiring the appropriate determination. | distinguish liability from observation
claim | Formal request for a remedy through the applicable process. | refer a claim
claim approval | Authorized acceptance of a claim, not merely its reporting. | avoid promising claim approval
concealed damage | Damage not apparent from external observation. | report suspected concealed damage
abrasion | Surface wear or scraping. | describe an abrasion
puncture | Hole made through packaging or material. | identify a puncture
tear | Split or rip in packaging material. | describe a tear
wet patch | Visible damp area without an established source. | note a wet patch
observation | Directly perceived fact rather than an inferred cause. | separate observation from inference
follow-up referral | Routing an issue for further review. | make a follow-up referral
acceptance decision | Decision about receiving the shipment under the actual process. | clarify the acceptance decision''',
    precision='The supported description is one carton with a crushed lower corner, contents unopened and uninspected. The condition warrants reporting, but it does not establish broken equipment, a driver-caused event, claim approval, or liability.',
    precision_extra='A receiver concern can be documented as a concern without being presented as a verified finding. Use precise location and packaging words, and follow the actual carrier process for condition records, inspections, acceptance decisions, and claims.',
    phrases='''Acknowledge the concern | I can see why that corner concerns you.\nName the observation | One carton has a crushed lower corner.\nLimit the description | I am describing the external packaging.\nState the inspection status | The contents have not been inspected.\nAvoid false reassurance | I cannot confirm that the equipment inside is undamaged.\nAvoid an unsupported finding | I cannot confirm that the equipment is broken either.\nSeparate cause | We have not established what caused the condition.\nAttribute the concern | You are concerned that the equipment may be damaged.\nReject an inaccurate note | I cannot record driver-caused damage as an established fact.\nKeep the issue visible | The visible condition should be included in the report.\nOffer a factual summary | Crushed lower corner; contents unopened and uninspected.\nRefer the matter | I will refer the concern for follow-up through the carrier process.\nSeparate reporting and approval | Reporting the issue does not approve a claim.\nAvoid deciding liability | This conversation does not determine responsibility.\nPreserve the location | The lower corner, not the whole carton, is the observed area.\nClose without overclaiming | The condition is reported; the internal condition and cause remain unknown.''',
    notes='''May be | Presents a possibility, not a verified internal condition.\nCaused by | Asserts a causal connection and needs evidence beyond appearance.\nConcerned that | Attributes the worry without converting it into a finding.\nVisible versus concealed | Separates externally observable condition from what may be hidden.\nReported versus approved | Filing or routing a concern does not grant a remedy.\nNeither conclusion | Uninspected means neither damaged nor undamaged is confirmed.''',
    d='''Which condition note matches the evidence? | One carton has a crushed lower corner; contents uninspected. | Driver broke the equipment inside. | Contents inspected and confirmed undamaged. | Every carton is crushed. | Only one external corner is observed, while internal condition remains unchecked.
Which sentence acknowledges concern without asserting damage? | You are concerned that the equipment may be damaged. | The driver definitely broke your equipment. | There cannot be any damage inside. | Your concern is irrelevant because the carton is closed. | The correct wording attributes a possibility while taking the receiver's concern seriously.
What does a follow-up referral establish? | The issue is being routed for review, not approved as a claim. | Legal liability has been decided. | A refund has been authorized. | The shipment must be accepted. | Referral starts or continues review without supplying a remedy or acceptance decision.
Which distinction must remain explicit? | Packaging condition versus uninspected contents. | Carton color versus driver nationality. | Claim approval versus guaranteed replacement today. | Any concern versus proven driver fault. | The observed outer condition does not establish what happened inside the carton.''',
    dialogue='''Ellis | This carton has a crushed corner. Please put broken equipment caused by the driver on the receipt, because I do not want the problem ignored.
Nia | I will not ignore it. I can record the [[visible condition::Visible condition is the crushed lower corner that can actually be observed, rather than uninspected equipment damage.]]: one carton has a crushed lower corner. We have not opened it or inspected the equipment inside.
Ellis | The corner looks bad enough that I am worried about the equipment. I do not want a note that makes it sound as though nothing happened.
Nia | The [[condition notation::Condition notation preserves the observed packaging issue without turning a concern into a finding about cause or contents.]] should clearly describe the corner. Saying the contents are uninspected does not remove or minimize that visible concern.
Ellis | But if you only mention the box, will someone assume I said the equipment was fine? That is not what I mean at all.
Nia | We can state the [[inspection::Inspection has not occurred, so neither damaged nor undamaged contents can be confirmed.]] status explicitly. The contents are unopened and uninspected, so I cannot confirm that they are fine or that they are broken.
Ellis | All right. I am concerned that the equipment may be damaged. Please keep that concern alongside the description of the corner.
Nia | Yes. That is an [[attributed statement::Attributed statement identifies the receiver's concern as a concern rather than a verified internal-damage finding.]]: you are concerned about possible internal damage. It is different from recording confirmed broken equipment as an observed fact.
Ellis | I still think the damage happened during delivery, although I did not see the carton being damaged. Can the note say that is what caused it?
Nia | That would be a [[causal claim::Causal claim asserts how the condition arose, which neither the visible corner nor the receiver's suspicion establishes.]] we have not established. I can report your concern, but I cannot state driver-caused damage as a verified conclusion.
Ellis | So you are not deciding that the carrier has no responsibility either? I do not want careful wording to become an automatic rejection.
Nia | Correct. I am not deciding [[liability::Liability is responsibility for the event; this factual description neither establishes nor rejects it.]] in either direction. I am separating the observation from questions that need the appropriate review.
Ellis | Then let us be specific about the location. It is the lower corner of this carton, not all the cartons in the delivery.
Nia | I will keep that precise: a [[crushed corner::Crushed corner describes the lower-corner deformation on one carton, not a whole-shipment or equipment-damage finding.]] on one carton, at the lower corner, with the contents still unopened and uninspected.
Ellis | What happens to the concern next? I want someone to review it, but I understand you cannot promise a replacement here.
Nia | I will make a [[follow-up referral::Follow-up referral routes the reported issue through the actual carrier process without promising a particular outcome.]] through our carrier process. Reporting the issue does not itself approve a claim or decide how it will be resolved.
Ellis | Please do that. I will keep the difference clear between what we can see and what we do not yet know about the equipment.
Nia | That distinction matters. [[Internal damage::Internal damage concerns the goods inside; their condition remains unknown because the carton has not been inspected.]] remains unverified. The packaging condition is visible, and both facts should remain in the report.
Ellis | We have agreed on a factual description, then. We have not agreed that the driver caused broken equipment or that a claim is approved.
Nia | Exactly. No [[claim approval::Claim approval would require an authorized decision, which this description and referral do not provide.]] or acceptance decision is made by this conversation. We have a clear condition report and a concern to refer.''',
    transfer_title='Describe a different visible condition',
    transfer_setup='At Cedar Studio, one carton has a tear in its upper side panel. Contents are unopened and uninspected. The receiver fears internal damage, but neither damage inside nor its cause is established.',
    transfer='''Driver: "One carton has a ___ in its upper side panel." | tear | Tear is the observed external condition, not a finding about the goods inside.
Receiver: "The contents are still ___." | unopened | The carton has not been opened to examine the internal goods.
Driver: "Internal damage remains ___." | unverified | The concern does not establish damage before an appropriate inspection.
Receiver: "The cause is not ___." | established | The visible tear does not establish how or by whom it was caused.''',
))


BOOK['units'].append(unit(
    title='When the recipient cannot receive',
    scene='The contact answers, but the office is closed',
    skill='Distinguish contact from availability, explain an unconfirmed wait, and refer delivery alternatives without inventing arrangements.',
    brief='At 14:10, driver Sam is safely parked outside the closed receiving office of Marlow Design. Listed contact Lina answers the phone and says she can return at 15:00, fifty minutes later. Sam cannot commit to waiting until then. Dispatch can review redelivery; whether collection from a carrier location is available remains unknown. Nothing authorizes leaving the shipment unattended, marking it received, or promising a new slot. Sam and Lina clarify what dispatch needs to review.',
    cast='Sam | Delivery driver\nLina | Listed receiving contact',
    culture=('An answered call is not a successful delivery', 'A customer may reasonably hope that a return time solves the problem, but driver availability is a separate question. Acknowledge the proposed time, state the current limit clearly, and distinguish a reviewable option from a confirmed arrangement.'),
    a='''What is the situation at 14:10? | The receiving office is closed | Lina is at the receiving desk | The shipment has been received | A new delivery appointment is booked | The driver is outside a closed office, although the listed contact answers the phone.
When can Lina return? | 15:00, fifty minutes later | 14:15, five minutes later | 14:10 immediately | Tomorrow at an agreed time | Fifteen hundred is fifty minutes after the fourteen-ten call.
Which alternative can be reviewed but is not confirmed? | Redelivery through dispatch | Unattended delivery already authorized | Collection definitely available | Waiting until 15:00 already agreed | Dispatch can review redelivery, but no new delivery arrangement has been approved.''',
    vocabulary='''recipient unavailable | Status indicating the intended receiver cannot currently receive. | report recipient unavailable
listed contact | Person named in the delivery contact information. | call the listed contact
receiving office | Office responsible for handling incoming deliveries. | check the receiving office
closed premises | Location not currently open for the relevant service. | report closed premises
arrival timestamp | Recorded time of reaching the location. | state the arrival timestamp
contact attempt | Effort to reach the named recipient or contact. | record a contact attempt
answered call | Telephone contact successfully established. | distinguish an answered call
return time | Time when the contact expects to be back. | confirm the return time
waiting commitment | Agreement to remain until a specified time. | avoid an unconfirmed waiting commitment
redelivery | Another attempt to deliver the shipment. | request redelivery review
collection option | Possible arrangement to pick up goods at another location. | check the collection option
carrier location | Carrier-operated or approved place relevant to a shipment. | verify the carrier location
unattended delivery | Leaving goods without an in-person receiving handover. | clarify unattended-delivery authorization
release authorization | Specific permission to release goods under the applicable process. | verify release authorization
delivery attempt | Visit or action aimed at delivery, not necessarily successful handover. | record the delivery attempt
received status | Record that the shipment has actually been received. | distinguish received status
no response | Contact outcome where no reply is obtained. | avoid an inaccurate no-response note
service availability | Whether the requested service can actually be offered. | confirm service availability
waiting period | Length of time spent or proposed at the stop. | specify the waiting period
dispatch review | Assessment by the team coordinating the delivery. | request dispatch review
new slot | Proposed replacement delivery time. | confirm a new slot
unconfirmed alternative | Possible option not yet agreed or available. | explain an unconfirmed alternative
contact outcome | Result of trying to reach the intended person. | document the contact outcome
follow-up owner | Person responsible for the next action or communication. | identify the follow-up owner''',
    precision='Lina answers at 14:10 but cannot receive until 15:00. That is fifty minutes later, not a confirmed waiting arrangement. Dispatch can review redelivery; collection availability and any replacement slot are still unknown.',
    precision_extra='Closed office, answered call, and uncompleted delivery are compatible facts. Do not record no response when the contact answered, or received when no handover occurred. Actual release, waiting, and redelivery decisions require the carrier process.',
    phrases='''State the present position | I am outside the closed receiving office at 14:10.\nConfirm the contact | Am I speaking with the listed receiving contact?\nAsk about availability | When will someone be available to receive?\nRepeat the return time | You can return at 15:00; is that correct?\nQuantify the wait | That would be fifty minutes from now.\nAvoid an unsupported commitment | I cannot commit to waiting until 15:00.\nAcknowledge the inconvenience | I understand that this disrupts your plans.\nOffer a review | Dispatch can review a redelivery arrangement.\nSeparate review and booking | No new slot is confirmed yet.\nKeep collection uncertain | I do not yet know whether collection is available.\nAvoid an unauthorized release | No unattended release has been authorized.\nPreserve the contact outcome | I reached the listed contact by phone.\nPreserve the delivery status | The shipment has not been received.\nCorrect a false inference | Answering the phone does not mean someone is here to receive.\nName the next action | I will send the current details to dispatch for review.\nSummarize the open position | Return at 15:00; waiting and alternatives remain unconfirmed.''',
    notes='''Can return | Describes the contact's availability, not the driver's waiting agreement.\nUntil | Gives the endpoint of a proposed wait.\nCan review | Offers assessment without promising the outcome.\nNot available versus unknown | Unknown collection availability is not a definite refusal of that option.\nAttempted versus received | A delivery visit does not itself establish a completed handover.\nReached versus present | A person can answer remotely while the receiving office remains closed.''',
    d='''Which record preserves the facts? | Office closed at 14:10; contact answered and can return at 15:00. | No response from the listed contact. | Shipment received at 14:10. | Driver agreed to wait until 15:00. | The correct record distinguishes an answered call from current receiving availability.
Which response correctly addresses waiting? | I cannot commit to waiting until 15:00. | I will definitely wait because you answered. | Your return automatically changes my route. | Waiting is confirmed although I have not checked. | The brief states that the driver cannot promise the fifty-minute wait.
Which collection statement is accurate? | Collection availability has not been confirmed. | You can definitely collect tonight. | Collection is impossible at every carrier location. | Your collection booking is complete. | Unknown availability supports neither a guaranteed collection nor a universal refusal.
What can happen next? | Dispatch can review redelivery without promising a slot yet. | Mark the shipment received to close the stop. | Leave it unattended without authorization. | Promise a new time before dispatch responds. | Review is the available next step, while the final arrangement remains unconfirmed.''',
    dialogue='''Sam | Hello, I am outside Marlow Design at 14:10. The receiving office is closed. Are you the listed contact for this delivery?
Lina | Yes, I am the [[listed contact::Listed contact identifies Lina as the person on the delivery record, although she is not currently at the office.]], but I am away from the office. I can return at 15:00. Could you wait until then?
Sam | That would be fifty minutes from now. I understand you want to receive it today, but I cannot commit to that wait.
Lina | I thought my [[return time::Return time is Lina's fifteen-hundred availability, not an agreement that the driver will remain.]] might solve it. I see that it also depends on whether you can stay. What happens if you cannot?
Sam | Dispatch can review redelivery. I will pass on the closed-office situation and your return time, but I cannot promise a new slot here.
Lina | Would [[redelivery::Redelivery means another delivery attempt, which dispatch may review but has not yet scheduled.]] mean later today, or could it be a different day? I do not want to plan around a time that is only a possibility.
Sam | No replacement time is confirmed. The review needs to establish what can be offered, so I should not describe today or tomorrow as agreed.
Lina | Understood. What about a [[collection option::Collection option would let the customer pick up the shipment elsewhere, but its availability is currently unknown.]] at one of your locations? Could I go there after I get back to the office?
Sam | I do not yet know whether collection is available for this shipment. That also needs checking before you make a trip to a carrier location.
Lina | Then please keep both questions clear. My [[service availability::Service availability concerns what the carrier can actually offer, not what the customer would prefer.]] question is about collection, while the other question is whether another delivery can be arranged.
Sam | I will. Neither option is confirmed. Also, this phone call does not mean the shipment has been received, because no handover has occurred.
Lina | Yes, please do not put [[received status::Received status would falsely imply a completed handover when the office is closed and the contact is remote.]] on the record. I answered the phone, but I am not there to accept the goods.
Sam | Exactly. I should record that I reached you and that the office is closed, not say there was no response from the contact.
Lina | That is the correct [[contact outcome::Contact outcome is an answered call with the recipient unavailable in person, not an unanswered attempt.]]. It matters to me that the notes show we spoke and that I gave you a return time.
Sam | I will include 15:00, with waiting unconfirmed. I also have no authorization to treat this as an unattended delivery.
Lina | Agreed. No [[release authorization::Release authorization has not been supplied, so the call does not authorize leaving the goods unattended.]] has been arranged in this conversation. Please do not read my return time as permission to leave the shipment.
Sam | Let me summarize: office closed at 14:10, listed contact reached, return possible at 15:00, no waiting commitment, and alternatives still need review.
Lina | That is accurate. The [[dispatch review::Dispatch review is the next assessment step, not confirmation of a wait, collection, or replacement delivery time.]] should determine what can actually be offered. I would rather hear a checked arrangement than guess.
Sam | I will send those details to dispatch for that review. I cannot give a confirmed new slot or collection location yet.
Lina | Thank you. Keep each [[unconfirmed alternative::Unconfirmed alternative describes redelivery or collection before its availability and arrangement have been established.]] separate from the facts we know. I can return at 15:00, but we have not agreed on the delivery solution.''',
    transfer_title='Clarify another closed-office call',
    transfer_setup='At 09:20, a driver reaches the contact for a closed office. The contact can return at 10:00. Waiting cannot be promised; dispatch can review redelivery, and collection availability is unknown.',
    transfer='''Driver: "Your return would be ___ minutes from now." | forty | Ten hundred is forty minutes after the nine-twenty call.
Contact: "The phone call was ___." | answered | The driver reached the contact, so no-response wording would be inaccurate.
Driver: "Waiting is not ___." | confirmed | The driver has not agreed to remain until the contact returns.
Contact: "Collection availability is still ___." | unknown | No verified collection option has been supplied in this scenario.''',
))


BOOK['units'].append(unit(
    title='Explaining the booked service boundary',
    scene='Curbside is not upstairs placement',
    skill='Explain the booked service, acknowledge a different need, and route a change request without promising price or timing.',
    brief='Customer Rafael expects a household delivery to be carried upstairs. Driver Amara checks the booking, which specifies curbside delivery and does not include inside service. Amara cannot add upstairs placement. Dispatch can review a possible upgrade or rearrangement, but no availability, price, or timing is known. Rafael asks for that review. The conversation does not authorize an immediate service change, direct the customer to move the goods, or establish that any shipment has been unloaded or accepted.',
    cast='Rafael | Customer\nAmara | Delivery driver',
    culture=('Explain the boundary without blaming the customer', 'A customer may use delivery to mean placement in the room where an item will be used. Name the actual booked service and acknowledge the mismatch. Offer a specific route for review without implying that personal effort or an unapproved payment can change the booking.'),
    a='''What service is booked? | Curbside delivery | Upstairs room placement | Assembly and installation | Inside delivery with unpacking | The booking explicitly says curbside and does not include inside service.
What does Rafael request? | Upstairs placement | A different shipment reference | Cancellation already agreed | Collection from a depot | Rafael wants the household delivery taken upstairs rather than curbside.
What is known about a possible change? | Dispatch can review it; availability, price, and timing are unknown | It is free and immediate | The driver has approved it | A new appointment is booked | The option is a reviewable request, not an authorized or priced upgrade.''',
    vocabulary='''curbside delivery | Service to the agreed curbside point under the actual booking. | confirm curbside delivery
inside delivery | Service bringing goods inside under specified terms. | distinguish inside delivery
upstairs placement | Positioning goods on an upper floor. | request upstairs placement
room-of-choice service | Delivery to a specified room when that service is offered and agreed. | check room-of-choice service
booked service | Service actually recorded in the confirmed booking. | verify the booked service
service scope | Work included and excluded in the agreed arrangement. | explain the service scope
service boundary | Limit of what the current arrangement authorizes. | state the service boundary
upgrade request | Proposal to change to an additional or higher service level. | submit an upgrade request
rearrangement | Change to delivery arrangements requiring confirmation. | discuss a rearrangement
availability check | Verification that a requested service can be supplied. | request an availability check
quotation | Stated price for specified work and conditions. | obtain a quotation
accessorial charge | Additional freight-service charge under applicable terms. | clarify an accessorial charge
price confirmation | Verification of the actual amount for the proposed service. | await price confirmation
timing confirmation | Verification of when an agreed service can occur. | await timing confirmation
authorization | Permission from the appropriate decision-maker for a specific action. | obtain authorization
service amendment | Approved change to the recorded service arrangement. | confirm a service amendment
scope mismatch | Difference between the booked work and the requested work. | explain the scope mismatch
customer expectation | What the customer believes the service will include. | clarify the customer expectation
access requirement | Site or access detail relevant to reviewing the requested service. | confirm access requirements
stair carry | Carrying goods on stairs as a separately defined service where offered. | ask about stair-carry service
assembly | Putting product parts together, distinct from delivery. | distinguish assembly from delivery
installation | Setting up a product for use under the relevant service. | distinguish installation from placement
unloading status | Whether unloading has occurred, separate from discussion of scope. | clarify the unloading status
change acceptance | Customer agreement to a specific confirmed proposal. | obtain change acceptance''',
    precision='Curbside delivery is the booked service in this fictional case; upstairs placement is a different request. No general definition here overrides an actual contract. Review by dispatch does not establish that an upgrade exists or that it is free.',
    precision_extra='Price, availability, timing, and authorization are separate questions. A customer can ask for a review without accepting an unknown charge or an unconfirmed date. This dialogue provides no handling instructions or permission to unload or move the shipment.',
    phrases='''Acknowledge the expectation | I understand you expected the item upstairs.\nName the booking | The booking specifies curbside delivery.\nExplain the exclusion | Inside service is not included in this booking.\nState your authority | I cannot add upstairs placement myself.\nAvoid blame | Let us clarify the difference between the booking and the request.\nOffer a review | Dispatch can review an upgrade or rearrangement.\nKeep availability open | I do not yet know whether that service can be offered.\nKeep price open | No upgrade price has been confirmed.\nKeep timing open | No revised delivery time is confirmed.\nClarify the request | Would you like me to refer the upstairs-placement request?\nSeparate request and approval | Asking for review does not approve the service change.\nAvoid an unapproved payment | I cannot agree to an informal extra charge.\nPreserve the choice | You have not accepted an unknown price.\nAvoid expanding the scope | Placement, assembly, and installation are different services.\nKeep the shipment status separate | We are discussing scope, not confirming unloading.\nClose with the next step | I will send the request to dispatch for a checked response.''',
    notes='''Booked versus expected | Separates the recorded arrangement from the customer's understanding.\nIncluded | States the scope of this booking, not every service offered by the carrier.\nCan review versus can provide | Assessment is possible even when availability remains unknown.\nMyself | Marks the driver's authority limit without claiming no alternative exists.\nUpgrade versus authorization | Naming an option does not make it approved.\nUnknown price | Cannot be treated as accepted merely because the customer requests a review.''',
    d='''Which response explains the boundary accurately? | Curbside is booked; upstairs placement needs separate review. | All deliveries automatically include upstairs placement. | Upstairs placement is already approved. | Curbside also means installation in every contract. | The booking covers curbside service, while the different request remains to be reviewed.
Which price statement is supported? | No upgrade price has been confirmed. | The upgrade is definitely free. | The driver can name an informal price. | Rafael has accepted any amount. | Neither a quotation nor customer acceptance of a price exists.
What does Rafael's review request authorize in the dialogue? | Referring the request to dispatch, not performing the upgrade. | Immediate upstairs placement. | Automatic assembly and installation. | Treating unloading as completed. | The customer asks for an assessment, not an unpriced or unauthorized service change.
Which summary keeps all uncertainties? | Upgrade availability, price, and timing remain unknown. | Only timing is unknown; everything else is approved. | The service has been amended and accepted. | The customer must move the goods upstairs personally. | No checked proposal exists for availability, price, or timing.''',
    dialogue='''Rafael | I need this taken upstairs to my apartment. I thought delivery meant putting it where I can use it, not stopping outside.
Amara | I understand the expectation. The [[booked service::Booked service is the recorded curbside arrangement, which differs from the requested upstairs placement.]] here is curbside delivery. This booking does not include inside service or upstairs placement.
Rafael | That is not what I was expecting. Could you add the upstairs part now? I would rather settle it here than arrange another conversation.
Amara | I cannot make that [[service amendment::Service amendment would change the authorized work; the driver cannot approve it in this conversation.]] myself. Dispatch can review an upgrade or rearrangement, but I do not have an approved change to carry out.
Rafael | Is that a definite no to any upstairs service, or are you saying that this particular booking does not include it?
Amara | I am explaining the [[service scope::Service scope identifies what this booking includes; it does not establish every possible service the carrier offers.]] of this booking. Whether another service can be offered needs checking, so I should not give you a definite yes or no yet.
Rafael | Fair enough. Would an upgrade cost extra? I do not want asking the question to mean I have agreed to an unknown charge.
Amara | No [[quotation::Quotation would specify a checked price; none exists, and a question does not authorize an unknown charge.]] has been provided. You have not accepted an unknown price simply by asking what alternatives might be available.
Rafael | And do you know whether it could happen today? The date matters to me as much as the price.
Amara | I have no [[timing confirmation::Timing confirmation is absent, so today or any replacement date cannot be promised.]] either. Availability, price, and timing all need a checked response before you can assess a specific proposal.
Rafael | Please ask dispatch, then. I want the request to say upstairs placement, not just a vague complaint that I am unhappy.
Amara | I can send an [[upgrade request::Upgrade request names the proposed additional service for review without representing it as approved.]] for upstairs placement. I will explain that curbside is booked and that you want them to review a different arrangement.
Rafael | Thank you. I do not need assembly discussed right now. First I need to understand whether the placement I wanted is possible.
Amara | Understood. [[Assembly::Assembly means putting parts together and is separate from the placement request Rafael wants reviewed.]] is separate from placement, and I will not expand your request into installation or other work you have not asked about.
Rafael | I also do not want an informal arrangement outside the booking. I need to know what the carrier has actually agreed to provide.
Amara | That requires the proper [[authorization::Authorization must cover the specific changed service; an informal understanding with the driver is not supplied here.]] and a confirmed arrangement. I cannot agree to an informal extra charge or treat that as a replacement for the process.
Rafael | So the next step is a review, and I will hear an actual proposal before deciding whether to accept it. Is that the position?
Amara | Yes. Your [[change acceptance::Change acceptance applies to a specific confirmed proposal; none has yet been offered or accepted.]] would concern a specific proposed service, price, and timing. At present those details remain unknown.
Rafael | Please keep that clear in the message. We are discussing an upstairs-service request, not saying that it has been performed.
Amara | I will. The [[scope mismatch::Scope mismatch is the difference between booked curbside delivery and requested upstairs placement, still awaiting review.]] is clear, and I will refer it to dispatch. This conversation does not confirm an upgrade or any completed unloading.''',
    transfer_title='Refer another service-change request',
    transfer_setup='A household booking specifies curbside delivery. The customer requests room-of-choice placement. The driver cannot add it; dispatch can review it, with price and timing still unknown.',
    transfer='''Driver: "The booked service is ___ delivery." | curbside | Curbside is the existing arrangement, not the additional placement requested.
Customer: "I am requesting ___ placement." | room-of-choice | Room-of-choice identifies the specific additional service the customer wants reviewed.
Driver: "The proposed change needs ___ review." | dispatch | Dispatch is the team that can assess the requested change here.
Customer: "The price and timing remain ___." | unknown | No checked proposal supplies either cost or a revised schedule.''',
))


BOOK['units'].append(unit(
    title='Matching a return to its collection',
    scene='Two booked cartons and one extra',
    skill='Match goods to a return reference, isolate an unmatched item, and request clarification without silently expanding the collection.',
    brief='Driver Kai arrives for return collection R62, which lists two printer cartons. Customer Dana presents those two identifiable cartons and a third carton of cables without a matching collection reference. Dispatch can query the extra carton, but no authorization to add it has been received. The two printer cartons remain identifiable under R62. The conversation establishes the mismatch and next query; it does not confirm that any carton has been loaded, collected, rejected permanently, or credited to the customer.',
    cast='Kai | Driver\nDana | Customer',
    culture=('Separate the extra item from the valid reference', 'A customer may reasonably group related equipment together, while the collection record identifies a narrower set. Explain which items match and which item needs clarification. Avoid turning one unmatched carton into a claim that the entire collection is invalid.'),
    a='''What does R62 list? | Two printer cartons | Three cable cartons | One printer and one cable carton | Every item at the customer location | R62 identifies two printer cartons, not an unrestricted collection of related items.
Which item lacks a matching reference? | The third carton of cables | Both identified printer cartons | The R62 document itself | A fourth carton not mentioned | The cable carton is additional and has no matching collection reference.
What is established by the discussion? | The mismatch and a dispatch query, not completed collection | All three cartons have been loaded | The extra carton is permanently rejected | A customer credit has been approved | The conversation clarifies identity and follow-up without supplying a collection or credit outcome.''',
    vocabulary='''return reference | Identifier connecting goods to a particular return arrangement. | confirm the return reference
collection booking | Recorded arrangement for picking up specified goods. | check the collection booking
return authorization | Approval for specified goods to be returned under stated conditions. | verify return authorization
return merchandise authorization | Formal return identifier or process, commonly RMA. | quote the return merchandise authorization
matching reference | Identifier consistent with the relevant record. | locate a matching reference
unmatched item | Item not linked to the stated collection record. | isolate the unmatched item
printer carton | Outer box identified as containing a printer in the return description. | identify the printer carton
cable carton | Outer box presented as containing cables. | distinguish the cable carton
additional carton | Box presented beyond the recorded collection quantity. | query the additional carton
booked quantity | Number of units specified in the collection arrangement. | preserve the booked quantity
presented quantity | Number of units offered by the customer at collection. | compare the presented quantity
collection scope | Items included in the specific pickup arrangement. | clarify the collection scope
reference match | Confirmed correspondence between an item and a record identifier. | establish a reference match
return label | Label linking a package to return-shipping information. | check the return label
serial number | Identifier assigned to a particular individual product. | verify the serial number
item description | Recorded wording identifying the type of goods. | compare the item description
packing description | Account of how goods are grouped or packaged. | confirm the packing description
collection amendment | Approved change to the pickup arrangement. | request a collection amendment
query | Request for clarification, not an approved change. | raise a query
item separation | Keeping matched and unmatched items distinct in the discussion. | maintain item separation
loaded status | Record that goods have been placed on the vehicle. | distinguish loaded status
collected status | Record that a pickup has actually occurred. | verify collected status
credit approval | Authorized financial credit, separate from return collection. | distinguish credit approval
return disposition | Decision about what happens to returned goods under the actual process. | await return disposition''',
    precision='R62 matches two printer cartons. Three cartons are presented, but the cable carton has no matching reference. The extra-item query should not change the original two-carton description or make the two identified cartons disappear from the record.',
    precision_extra='A collection reference, a product serial number, and a return authorization may serve different purposes. Use the actual records required by the carrier and customer process. A reference match alone does not prove loading, pickup, refund, or credit completion.',
    phrases='''Identify the booking | I am here for return collection R62.\nState the booked count | The booking lists two printer cartons.\nConfirm the matched items | These two printer cartons match R62.\nName the additional item | The third carton contains cables according to your description.\nIdentify the missing link | I do not have a matching reference for that carton.\nKeep the sets separate | The original two are identifiable; the cable carton is the open question.\nAsk for clarification | Is there a separate collection reference for the cables?\nAvoid silent expansion | I cannot treat R62 as a three-carton booking without confirmation.\nRefer the query | Dispatch can query the additional carton.\nKeep approval pending | No collection amendment has been authorized yet.\nAvoid permanent rejection | Unmatched does not mean permanently rejected.\nPreserve the item description | Two printer cartons, not three printer cartons.\nDistinguish status | Matching the reference does not mean the goods are already collected.\nAvoid a credit promise | This check does not approve a customer credit.\nRead back the difference | Two booked, three presented, with one unmatched cable carton.\nClose with the exact query | The next question is whether the cable carton has an authorized collection arrangement.''',
    notes='''Additional | Identifies the carton beyond the original two, not a substitute for them.\nMatch | Connects a specific item and record rather than similar-looking goods.\nRelated versus included | Cables may relate to printers without belonging to the same booking.\nQuery versus amendment | Asking about an extra item does not alter the collection record.\nIdentifiable versus collected | A successful match is not a completed pickup.\nReturn versus credit | Moving goods back does not itself establish a financial remedy.''',
    d='''Which read-back is accurate? | R62 lists two printer cartons; the cable carton is unmatched. | R62 lists three printer cartons. | No carton matches any record. | The cable carton has already been added. | The statement preserves the two matches and isolates the additional cable carton.
Which action is available in the conversation? | Ask dispatch to query the extra carton. | Invent a matching reference. | Declare a customer credit approved. | Mark all three cartons collected. | Dispatch can seek clarification, while adding or collecting the extra carton remains unconfirmed.
Which statement goes too far? | The unmatched carton is permanently rejected. | The cable carton lacks a matching reference. | The original two printer cartons remain identifiable. | No amendment is authorized yet. | Missing information now does not establish a permanent rejection decision.
Which status distinction is essential? | Reference matched is not the same as collection completed. | Any return automatically creates a refund. | Related equipment always shares one booking. | A query automatically approves an extra carton. | Identity verification and actual collection are different stages with different evidence.''',
    dialogue='''Kai | I am here for return collection R62. The booking lists two printer cartons, but I can see you have presented three cartons.
Dana | Yes, these are the two printers, and this is a [[cable carton::Cable carton identifies the additional package, which is not one of the two printer cartons on R62.]]. The cables relate to the printers, so I put everything together for the return.
Kai | Thank you for explaining. The two printer cartons match R62. I do not have a matching collection reference for the carton of cables.
Dana | I assumed the same [[return reference::Return reference R62 links the two printer cartons to the booking, not automatically every related accessory.]] covered the related equipment. Are you saying the cable carton needs its own confirmed link to the collection?
Kai | Yes, we need the relevant confirmation. Related equipment is not automatically included in this booking, and I should not silently change two cartons to three.
Dana | Understood. I do not have a [[matching reference::Matching reference is absent for the cables, leaving that carton unlinked to the stated collection arrangement.]] for the third carton with me. Can dispatch check whether there is another arrangement for it?
Kai | Dispatch can query it. I will explain the item and the missing reference without describing an extra carton as already authorized for pickup.
Dana | Please keep the [[booked quantity::Booked quantity remains two printer cartons, despite the customer presenting a third carton.]] at two while that question is checked. I do not want the record to suddenly describe three printers.
Kai | Exactly. I will preserve the descriptions: two printer cartons match R62, and a separate carton described as cables has no matching reference.
Dana | Does that make the whole [[collection booking::Collection booking still identifies the original two cartons; an extra unmatched carton does not erase those matches.]] invalid, or are the two printer cartons still identifiable under R62?
Kai | The original two remain identifiable. The unresolved question is the additional carton, not whether those two correspond to the return record.
Dana | That distinction helps. Please do not describe every item as an [[unmatched item::Unmatched item applies to the cable carton only, not the two printer cartons already linked to R62.]] because I presented one extra box. The two printers are the ones listed.
Kai | I agree. We can isolate the extra-item question and send it to dispatch. We have not received approval to add the cable carton.
Dana | So a [[collection amendment::Collection amendment would be an approved change; raising the query has not supplied that approval.]] is still pending, rather than something that happens automatically when I ask about it?
Kai | Correct. At this point we have a query, not an approved change. I also cannot say that the extra carton is permanently rejected.
Dana | Nor should the record show [[collected status::Collected status requires an actual completed pickup, which this reference-checking conversation does not establish.]] yet. We are clarifying the references here, not confirming that any carton has been taken.
Kai | That is right. Matching a record, loading goods, and completing a pickup are separate stages. This conversation has established the identity issue.
Dana | And I assume this is not [[credit approval::Credit approval is a separate financial decision and does not follow from matching cartons to a return booking.]] either. I will not tell our accounts team that the return check guarantees a credit.
Kai | Correct. Let me read back the position: R62 lists two printer cartons; both are identifiable; the third cable carton needs dispatch clarification.
Dana | That is accurate. The [[collection scope::Collection scope remains the recorded two cartons unless the additional item is properly confirmed and authorized.]] has not been expanded. Please raise the cable-carton query while preserving the original two-item description.''',
    transfer_title='Match another return accurately',
    transfer_setup='Return S73 lists three monitor cartons. The customer presents those three and an extra keyboard carton without a matching reference. Dispatch can query the extra item; no amendment or collection is confirmed.',
    transfer='''Driver: "S73 lists three ___ cartons." | monitor | Monitor cartons are the goods named in the recorded return scope.
Customer: "The extra carton contains a ___." | keyboard | The keyboard carton is the additional item lacking a matching reference.
Driver: "The extra carton remains ___." | unmatched | No record has yet linked the additional carton to the booking.
Customer: "The query does not mean collection is ___." | completed | Reference clarification does not establish that any pickup has occurred.''',
))


BOOK['units'].append(unit(
    title='Closing a route with a clear handoff',
    scene='One missing upload, one refusal',
    skill='Hand over distinct delivery outcomes and unfinished records, attributing a reported reason and assigning each follow-up explicitly.',
    brief='Route 12 is ending. Driver Luis tells evening dispatcher Jo that stop 7 was received by Mei at 16:05, but the receipt has not uploaded. Stop 8 was refused because the customer reported a duplicate order; that reported reason has not been independently verified. Jo accepts responsibility for checking the stop-7 receipt upload and contacting customer service about stop 8. Neither follow-up is completed during this handover, and no refund, replacement delivery, or final route closure is established.',
    cast='Luis | Driver\nJo | Evening dispatcher',
    culture=('Name the outcome, the unfinished record, and the owner', 'End-of-route summaries often compress different problems into everything is done or two failed deliveries. Separate the physical outcome from the record status at each stop. Attribute the stated reason for a refusal and confirm the next person owns the remaining work.'),
    a='''What happened at stop 7? | Mei received the shipment at 16:05, but the receipt upload is missing | Nobody received the shipment | Customer service approved a refund | The customer refused a duplicate order | The physical receipt occurred, while its electronic document upload remains unfinished.
What is the known reason given at stop 8? | The customer reported a duplicate order | A duplicate order was independently proved | The driver delivered to the wrong address | The receipt upload failed at stop 7 | Duplicate order is the customer's stated reason for refusal, not an independently verified finding.
What does Jo accept? | Both unfinished follow-ups | A completed refund | A new delivery appointment | Proof that the route is fully closed | Jo takes ownership of the receipt check and customer-service contact without completing them.''',
    vocabulary='''route handoff | Transfer of route information and unfinished responsibilities. | give a route handoff
route closure | Completion of the required route-ending process. | verify route closure
stop outcome | What actually happened at an individual delivery stop. | state the stop outcome
received by | Phrase naming the person who received goods. | record received by Mei
receipt timestamp | Time associated with the receiving event. | preserve the receipt timestamp
delivery receipt | Record associated with the receiving event. | locate the delivery receipt
proof of delivery | Evidence of delivery under the applicable process, often POD. | check proof of delivery
receipt upload | Transfer of the receipt into the required electronic system. | verify the receipt upload
upload pending | Status indicating the electronic transfer is unfinished. | report upload pending
synchronization | Updating records between devices or systems. | check synchronization status
record completeness | Whether all required information and records are present. | verify record completeness
missing document | Required record not currently available where expected. | follow up a missing document
refused delivery | Delivery the intended receiving party declines to accept. | record a refused delivery
refusal reason | Explanation given for declining a delivery. | attribute the refusal reason
reported duplicate | Alleged repetition of an order, not independently verified here. | record the reported duplicate
customer service | Team handling customer queries and resolution processes. | contact customer service
independent verification | Check separate from the original person's statement. | request independent verification
open item | Task or question still needing action. | list the open items
action owner | Person responsible for the next defined task. | name the action owner
ownership acceptance | Agreement to take responsibility for follow-up. | confirm ownership acceptance
completion status | Whether a task has actually been finished. | preserve completion status
route summary | Concise account of outcomes across a delivery route. | provide a route summary
read-back confirmation | Repetition that checks the accuracy of a handoff. | request read-back confirmation
resolution | Established outcome addressing an open issue. | distinguish referral from resolution''',
    precision='Stop 7 was received by Mei at 16:05; its receipt upload is missing. Stop 8 was refused with a customer-reported duplicate-order reason. These are different outcomes, not two undelivered shipments or two completed follow-ups.',
    precision_extra='Jo accepting responsibility changes who owns the next actions, not whether the actions are finished. A reported duplicate is not an independently confirmed duplicate, and a missing upload is not proof that the physical receiving event never happened.',
    phrases='''Name the route | I am handing over the open items from route 12.\nSeparate the stops | Stop 7 and stop 8 have different issues.\nState the receiving event | Mei received stop 7 at 16:05.\nState the missing record | The receipt has not uploaded.\nAvoid a false delivery failure | The missing upload does not mean the goods were not received.\nGive the second outcome | Stop 8 was refused.\nAttribute the reason | The customer reported a duplicate order.\nPreserve uncertainty | That reason has not been independently verified.\nAssign the first action | Please check the stop-7 receipt upload.\nAssign the second action | Please contact customer service about stop 8.\nAccept ownership | I will take both follow-ups.\nAvoid false completion | Taking ownership does not complete either check.\nAsk for a read-back | Please repeat the two actions and their current status.\nKeep remedies unconfirmed | No refund or replacement delivery is confirmed.\nPreserve the timestamp | Keep 16:05 with the stop-7 receiving record.\nClose the handoff | Jo owns both open items; their outcomes remain pending.''',
    notes='''Received versus uploaded | The physical event and electronic record transfer are separate facts.\nReported | Attributes the duplicate-order explanation to the customer.\nBecause | Can state the customer's reason for refusal without proving the underlying duplicate.\nWill check versus checked | Future action must not be written as completed verification.\nBoth | Applies to the two distinct follow-ups, not two identical delivery outcomes.\nClosed | Requires actual route-closeout conditions, not merely a handoff conversation.''',
    d='''Which stop-7 statement is accurate? | Received by Mei at 16:05; receipt upload pending. | Not received because the receipt is missing. | Received by Jo at 15:06. | Refused because of a verified duplicate. | The statement preserves the receiver, timestamp, and separate unfinished electronic record.
Which stop-8 wording preserves attribution? | The customer reported a duplicate order and refused the delivery. | The carrier definitely created a duplicate order. | A duplicate was independently verified. | Stop 8 was successfully received. | The customer's explanation must remain attributed rather than promoted to a verified cause.
Which handoff wrongly claims completion? | Jo accepted the tasks, so both issues are resolved. | Jo will check the receipt upload. | Customer-service contact is still pending. | No refund is confirmed. | Ownership acceptance assigns future work but does not supply its completed outcome.
Which action pair belongs to Jo? | Check stop-7 receipt upload and contact customer service about stop 8. | Deliver both shipments again automatically. | Approve a refund and delete the receipt time. | Change both stops to undelivered. | The two assigned tasks match the distinct unfinished items in the briefing.''',
    dialogue='''Luis | Jo, before I finish route 12, I need to hand over two open items. They are different issues, so I will take them separately.
Jo | Go ahead. Start with the [[stop outcome::Stop outcome describes what actually happened at each location, before discussing unfinished records or follow-up.]] for stop 7, then tell me what remains unfinished. I do not want to merge it with stop 8.
Luis | Mei received the shipment at stop 7 at 16:05. The receipt has not uploaded, so the electronic record is still incomplete.
Jo | I will check the [[receipt upload::Receipt upload is the unfinished electronic transfer, not an uncompleted physical delivery at stop seven.]]. The receiving event is recorded as Mei at 16:05, and the missing upload is the follow-up issue.
Luis | Correct. Please do not change that to undelivered just because the document is not available in the system yet.
Jo | Understood. [[Record completeness::Record completeness concerns the missing receipt in the system and must not erase the actual receiving event.]] is still in question, but the missing document does not erase your report that Mei received the shipment.
Luis | Stop 8 was refused. The customer said the order was a duplicate, but I have no independent verification of that explanation.
Jo | I will keep the [[refusal reason::Refusal reason is the customer's reported duplicate order, not an independently established ordering error.]] attributed to the customer. The wording should not become a finding that our company created a duplicate.
Luis | Exactly. We need customer service to review that, not an automatic refund or another delivery based only on the refusal note.
Jo | I will contact [[customer service::Customer service is the team Jo will approach about stop eight; that contact has not yet resolved the issue.]] about stop 8. No refund, replacement delivery, or other resolution is confirmed by this handoff.
Luis | Can you take responsibility for both items: the receipt upload at stop 7 and the customer-service contact about stop 8?
Jo | Yes, I am the [[action owner::Action owner names Jo as responsible for both next steps without implying either step is already complete.]] for both follow-ups. I have accepted the tasks; I have not yet checked the upload or made the customer-service contact.
Luis | Thank you. Please keep 16:05 with Mei and stop 7. It should not become the time of the refusal at stop 8.
Jo | I will preserve that [[receipt timestamp::Receipt timestamp belongs to Mei's receiving event at stop seven and must not be reassigned to the refusal.]] exactly. We have no supplied time for the stop-8 refusal, so I will not copy 16:05 onto it.
Luis | Good. Could you read both items back before I leave? I want to be sure the next steps and the unfinished status have transferred clearly.
Jo | Here is the [[read-back confirmation::Read-back confirmation checks the two outcomes, pending tasks, and ownership before the driver leaves.]]: stop 7 received by Mei at 16:05, upload pending; stop 8 refused for a customer-reported duplicate order. I own both follow-ups.
Luis | That matches. The customer's statement is not proof of an actual duplicate, and your acceptance does not mean the work is already done.
Jo | Agreed. [[Independent verification::Independent verification of the alleged duplicate has not occurred, so the customer's reason remains an attributed report.]] of the duplicate is still absent. The receipt check and customer-service contact remain pending.
Luis | Then the handoff is clear, but I should not describe the entire route-closeout process as complete just because we have had this conversation.
Jo | Correct. [[Route closure::Route closure requires the relevant process to be completed; this handoff only transfers the two unfinished actions.]] is not established here. We have transferred the two open items with their facts, uncertainties, and next owner intact.''',
    transfer_title='Hand over another pair of stops',
    transfer_setup='On route 15, stop 3 was received by Noor at 12:25, but its receipt upload is pending. Stop 4 was refused after a customer reported an unwanted order. Dispatcher Ana accepts both follow-ups; neither is complete.',
    transfer='''Driver: "Stop 3 was received by ___ at 12:25." | Noor | Noor is the named receiver for the physically completed receiving event.
Dispatcher: "The receipt upload remains ___." | pending | The physical delivery does not establish completion of the electronic upload.
Driver: "The unwanted-order reason was ___ by the customer." | reported | Reported preserves attribution without claiming independent verification of the customer's explanation.
Dispatcher: "The next action owner is ___." | Ana | Ana accepts both unfinished follow-ups without claiming they are already completed.''',
))
