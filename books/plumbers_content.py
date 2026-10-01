"""Original Plumbing Workplace English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='plumbers', title='Plumbing Workplace English',
    cover_label='ENGLISH FOR PLUMBING PROJECTS AND CUSTOMER COMMUNICATION',
    cover_title='Plumbing\nWorkplace', cover_size=40,
    tagline='Precise descriptions. Clear agreements.',
    audience='For plumbers, plumbing service coordinators, and project staff working with customers, suppliers, and other trades.',
    map_intro='Eight practical conversations move from a first service call to a final handover: identify fixtures, compare component descriptions, reconcile drawing references, report moisture, explain access, coordinate interruptions, price changes, and close document gaps.',
    notes_title='Name the fixture. Preserve the detail.',
    notes_intro='Plumbing conversations connect everyday descriptions with technical records. Practice narrowing a report, comparing like quantities, explaining a limitation, and giving a clear next step.',
    field_notes=[
        ('Ask which fixture', 'Sink can mean a bathroom basin, kitchen sink, or utility sink. Repeat the room, unit, and fixture description before summarizing a customer report. Keep the observation separate from a diagnosis.', '"You mean the bathroom basin in Unit 3B, not the utility sink beside it."'),
        ('Compare matching references', 'A nominal pipe designation is not necessarily its measured outside diameter. Drawing dimensions also need a datum and endpoint. Confirm the product series and reference before treating different numbers as an error.', '"The number alone does not establish whether the delivered component matches the order."'),
        ('Separate access from drainage', 'An access panel and a cleanout serve different purposes. Explain the terms in plain language, then keep an unreviewed enclosure change open for coordination rather than approving it conversationally.', '"The removable panel provides access; it is not an extra drain."'),
        ('Commit only to what is agreed', 'Arrival time, interruption time, estimate scope, and follow-up date are different commitments. State which is booked, proposed, included, or still awaiting review.', '"The visit is booked for 09:00; the proposed interruption still needs approval."'),
    ],
    scope_note='The cases, products, and project records are fictional. This book teaches English, not plumbing diagnosis, installation, testing, repair, valve operation, or code compliance. Follow actual training, authorization, manufacturer instructions, site procedures, and applicable requirements. A reported symptom, dry surface, drawing, or handover document does not establish system condition or authorize work. The conversations do not instruct clients to test, dismantle, or operate plumbing equipment.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Plumbers, Pipefitters, and Steamfitters.',
             url='https://www.bls.gov/ooh/construction-and-extraction/plumbers-pipefitters-and-steamfitters.htm',
             note='Occupational context for fixtures, project drawings, estimates, and coordination. No installation or repair procedures are reproduced.', checked='1 October 2026'),
        dict(title='Charlotte Pipe. ChemDrain Technical and Installation Manual.',
             url='https://www.charlottepipe.com/uploads/documents/technical/TM-CD.pdf',
             note='Terminology reference distinguishing nominal size and outside diameter. The book gives no product sizing, compatibility, or installation decisions.', checked='1 October 2026'),
        dict(title='Oatey. Access Panels.',
             url='https://www.oatey.com/products/rough-products/access-panels',
             note='Background for describing access to concealed services. Examples do not specify compliant panel dimensions or approve enclosure changes.', checked='1 October 2026'),
        dict(title='Kohler. Product Support.',
             url='https://www.kohler.com/en/support',
             note='Context for model identification, technical documents, care information, and warranty records. Fictional cases do not reproduce product instructions.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Identifying fixtures and service history',
    scene='Which sink in Unit 3B?',
    skill='Clarify a customer report using fixture, location, and observation time without turning a symptom into a diagnosis.',
    brief='Tenant Mina reports a sink problem in Unit 3B. A bathroom basin and a utility sink stand beside one another. She means the bathroom basin and noticed water on the cabinet base at 07:00. The source of the water has not been established. Service coordinator Ellis needs an accurate description for the plumber, using what Mina has already observed. No earlier repair history is supplied, and no instruction to operate or dismantle equipment is needed.',
    cast='Mina | Tenant\nEllis | Service coordinator',
    culture=('Clarify without making the customer defend a diagnosis', 'Customers may use one everyday name for several fixtures. Offer concrete alternatives, acknowledge the reported condition, and ask about existing observations. A precise service description helps the next person without requiring the customer to identify a failed component.'),
    a='''Which fixture does Mina mean? | The bathroom basin in Unit 3B | The utility sink beside it | A kitchen sink elsewhere | Both fixtures equally | The brief identifies the bathroom basin, not the nearby utility sink.
What does 07:00 identify? | When Mina noticed water | The proven start of a leak | A booked arrival time | The time a repair finished | The supplied time is an observation time, not a verified onset.
What is known about the source? | It has not been established | The basin trap has failed | A supply connection has failed | The utility sink is responsible | Water location alone does not identify its source in this report.''',
    vocabulary='''fixture | Plumbing appliance such as a basin, sink, or toilet. | identify the fixture
bathroom basin | Bowl used for washing hands or face in a bathroom. | specify the bathroom basin
utility sink | Sink intended for cleaning or general utility tasks. | distinguish the utility sink
vanity unit | Bathroom cabinet assembly associated with a basin. | describe the vanity unit
cabinet base | Bottom surface within the cabinet. | report water on the cabinet base
service call | Request or attendance for a reported plumbing issue. | log a service call
tenant report | Account given by the person occupying the premises. | record the tenant report
unit number | Identifier of an individual apartment or premises. | confirm the unit number
fixture location | Position of the particular plumbing appliance. | state the fixture location
observation time | Time when someone noticed a condition. | record the observation time
onset | Point when a condition actually began. | distinguish onset from observation
source | Origin of the reported water or problem. | establish the source
supply connection | Connection associated with water delivery to a fixture. | identify a supply connection
waste connection | Connection associated with carrying used water away. | describe the waste connection
trap | Fitting designed to retain a liquid seal in a drainage system. | identify the basin trap
faucet | Fitting that controls delivery of water at a fixture. | name the faucet
tap | Common alternative term for a faucet. | clarify the tap description
visible moisture | Wetness that can be seen at the reported location. | describe visible moisture
service history | Record of earlier attendance or work. | check the service history
previous repair | Corrective work completed on an earlier occasion. | confirm a previous repair
reported symptom | Condition described by a customer before assessment. | retain the reported symptom
call summary | Concise record of information from the conversation. | read back the call summary
unknown cause | Origin or explanation that is not established. | record an unknown cause
attendance | Visit by the relevant service person. | arrange attendance''',
    precision='Water was noticed on the cabinet base at 07:00. This does not establish when it first appeared or which component caused it. Keep the fixture identity, observed location, and time together.',
    precision_extra='The bathroom basin and utility sink are different fixtures. Familiar terms such as tap and faucet can be clarified without correcting the customer unnecessarily. No previous repair or component failure is established here.',
    phrases='''Offer two concrete choices | Do you mean the bathroom basin or the utility sink?
Confirm the premises | I have the location as Unit 3B.
Separate adjacent fixtures | The utility sink is beside it, but it is not the fixture you mean.
Locate the observation | Where had you already noticed the water?
Preserve the time | You first noticed it at 07:00.
Avoid changing the onset | I will record that as the observation time.
Name the surface | The water was on the cabinet base.
Keep the report attributed | The tenant reports water beneath the bathroom basin.
Keep the cause open | The source has not been established.
Avoid naming a failed part | I cannot identify a failed connection from that description.
Distinguish the routes | A supply connection and a waste connection are different.
Clarify familiar wording | By tap, do you mean the basin faucet?
Record the history limit | No earlier repair history has been supplied.
Avoid inventing reassurance | I cannot say the issue has been resolved.
Read back the details | Bathroom basin, Unit 3B, cabinet base, noticed at 07:00.
Close with the record | I will pass that description to the plumber.''',
    notes='''Do you mean X or Y? | Offers bounded alternatives that resolve an ambiguous noun.
Noticed at | Records an observation without asserting when the problem began.
Reports | Attributes an account to its source.
Beneath versus from | Beneath gives location; from asserts origin.
Has not been established | Leaves a cause open without denying the observation.
No history supplied | Does not mean that no earlier work ever occurred.''',
    d='''Which question best clarifies the fixture? | Do you mean the bathroom basin or the utility sink beside it? | Which connection has failed? | Why did the trap start leaking? | Can you dismantle the cabinet connection? | The alternatives identify the fixture without assuming a failure or requesting work.
Which summary preserves the time accurately? | Water noticed on the cabinet base at 07:00 | Leak began exactly at 07:00 | Repair completed at 07:00 | Plumber booked for 07:00 | Noticed records the tenant's observation rather than onset or scheduling.
Which statement wrongly converts location into cause? | The water must be coming from the trap | Water was seen on the cabinet base | The bathroom basin is the reported fixture | The source needs assessment | The trap is not identified as the source by the supplied facts.
What should accompany the handoff? | Fixture, unit, observed surface, time, and unresolved source | Only the word sink | An invented previous repair | A guaranteed diagnosis | These details preserve the usable report without adding unsupported history or conclusions.''',
    dialogue='''Mina | I need someone to look at the sink in Unit 3B. I found water underneath it this morning, and I am not sure what to call the problem.
Ellis | Let me identify the [[fixture::Fixture names the particular appliance; the room contains two different sinks.]] first. Do you mean the bathroom basin, or the utility sink that stands beside it?
Mina | The bathroom one, where we wash our hands. The utility sink is beside the cabinet, but that is not the sink I am talking about.
Ellis | Thank you. I will put [[bathroom basin::Bathroom basin resolves the two-fixture ambiguity using Mina's explicit clarification.]] in the request and keep Unit 3B attached to it. Where had you already noticed the water?
Mina | On the bottom of the cabinet, below that basin. I noticed it at seven this morning. I do not know when it first appeared.
Ellis | I will record water on the [[cabinet base::Cabinet base identifies the observed surface without asserting where the water originated.]], noticed at 07:00. That describes the location you saw, not yet where the water came from.
Mina | Exactly. I had started to say the pipe was leaking, but I cannot actually tell you which part it came from.
Ellis | Then the [[source::Source concerns origin, which Mina's observation has not established.]] remains unknown. We can give the plumber a useful description without naming a failed part before it has been assessed.
Mina | Does saying I saw it at seven make it sound as though the problem began then? I cannot confirm that.
Ellis | No. I will label seven as the [[observation time::Observation time preserves when Mina noticed water without inventing the onset.]], rather than the start of the problem. That distinction should stay in the call notes.
Mina | Good. I also do not have a record of any earlier work on that basin, so I cannot give you a repair date.
Ellis | I will mark the [[service history::Service history concerns earlier work; none has been supplied, not proven absent.]] as not supplied. That does not mean we know there has never been a repair.
Mina | One other thing: I sometimes call the fitting above the basin a tap. Will the plumber understand that, or should I use another word?
Ellis | Tap is understood in many workplaces; [[faucet::Faucet is the alternative name for the water-delivery fitting, not a diagnosis.]] is another common term. We can clarify the name without suggesting that fitting caused the water.
Mina | That helps. I do not want the request to say the tap has failed simply because I mentioned it in this conversation.
Ellis | It will not. The record will preserve your [[reported symptom::Reported symptom distinguishes Mina's account from a confirmed component failure.]] and the fixture location. It will not identify a failed supply or waste connection.
Mina | Please read the short version back to me before you send it. I want the plumber to come to the correct fixture.
Ellis | Here is the [[call summary::Call summary gathers fixture, location, observation, and uncertainty for the next person.]]: Unit 3B, bathroom basin, water on the cabinet base, noticed at 07:00. Source unestablished; earlier repair history not supplied.
Mina | Yes, that is accurate. It names the right basin and does not make me sound certain about something I have not identified.
Ellis | I will pass that through for [[attendance::Attendance means the service visit being arranged, without promising a diagnosis or time.]]. You have clarified the report; the next assessment must establish the cause rather than assume one from the wording.''',
    transfer_title='Give the plumber the precise report',
    transfer_setup='Complete the handoff using the tenant account. Keep the fixture, observed surface, time, and cause status distinct.',
    transfer='''Coordinator: "The tenant means the bathroom ___ in Unit 3B." | basin | Basin identifies the fixture Mina selected, not the adjacent utility sink.
Plumber: "Water was seen on the cabinet ___." | base | Base names the observed surface without identifying the water source.
Coordinator: "It was noticed at ___." | 07:00 | The time belongs to the observation, not a proven onset.
Plumber: "The source remains ___." | unestablished | The account supplies no assessment establishing which component caused the water.'''
))


BOOK['units'].append(unit(
    title='Clarifying pipe and component specifications',
    scene='A designation is not a measurement',
    skill='Distinguish nominal size from measured outside diameter and request complete product identification before judging a delivery.',
    brief='Buyer Omar compares a nominal pipe designation on an order with a measured outside diameter and assumes the delivery is wrong because the numbers differ. The order names a product series, but the delivery label is incomplete. Supplier coordinator Leila must explain the two kinds of size information and request complete identification. Neither material compatibility nor connection compatibility has been verified. Explaining nominal size does not establish that the delivery is correct.',
    cast='Omar | Buyer\nLeila | Supplier coordinator',
    culture=('Correct the comparison without dismissing the concern', 'A customer can make an invalid comparison and still have a genuine delivery problem. Explain the terminology, then investigate the actual item identity. Avoid moving from the numbers are different to either the goods are wrong or the goods are definitely right.'),
    a='''What is Omar comparing? | A nominal designation and a measured outside diameter | Two verified inside diameters | Two complete product labels | Identical manufacturer part numbers | The comparison uses a size designation and a physical measurement of a different kind.
What information is incomplete? | The delivery label | The fact that an order exists | The buyer's concern | The meaning of outside | The order names a series, but the delivered item's label is incomplete.
What remains unverified? | Product identity and relevant compatibility | That the measured number differs | That the order lists a series | That Omar has a question | The supplied facts do not verify the delivered product or its compatibility.''',
    vocabulary='''nominal size | Conventional size designation that may differ from a measured diameter. | confirm the nominal size
outside diameter | Measurement across the outer surface of a pipe. | compare the outside diameter
inside diameter | Measurement across the internal opening of a pipe. | distinguish inside diameter
wall thickness | Distance between the inner and outer pipe surfaces. | specify the wall thickness
size designation | Standard or commercial name used to identify a size. | read the size designation
measured dimension | Numerical value obtained from an actual measurement. | record the measured dimension
product series | Named family of related products. | identify the product series
part number | Manufacturer identifier for a particular item. | verify the part number
delivery label | Identification attached to supplied goods. | check the delivery label
order line | Individual item entry in a purchase order. | reconcile the order line
material specification | Description of required material characteristics. | confirm the material specification
connection type | Form of interface used to join components. | identify the connection type
fitting | Component used to connect, branch, or change a pipe run. | identify the fitting
coupling | Fitting used to join pipe sections or components. | specify the coupling
adapter | Fitting joining different connection forms or sizes as designed. | identify the adapter
elbow | Fitting that changes the direction of a pipe run. | identify the elbow
tee | Fitting with a branch connection. | specify the tee
reducer | Fitting connecting different nominal pipe sizes. | identify the reducer
product identification | Information establishing which item has been supplied. | complete product identification
compatibility | Suitability of components for use together under relevant conditions. | verify compatibility
substitution | Replacement of a specified product with another. | review a substitution
dimensional table | Manufacturer data listing defined dimensions. | consult the dimensional table
supply discrepancy | Difference between ordered and supplied goods or records. | investigate a supply discrepancy
acceptance status | Whether goods have been accepted through the applicable process. | preserve acceptance status''',
    precision='A nominal designation and an outside diameter are different kinds of information. Different numerical values alone do not establish an incorrect delivery. The relevant product series and manufacturer data must be identified.',
    precision_extra='Correcting the size comparison does not verify the delivered item. The label is incomplete, and material and connection compatibility remain unverified. Do not replace one unsupported conclusion with automatic acceptance.',
    phrases='''Acknowledge the concern | I understand why those two numbers look inconsistent.
Name the comparison | One is a nominal designation; the other is a measured outside diameter.
Explain nominal | Nominal size is a designation, not necessarily that measured diameter.
Retain the measurement | We should keep your measurement in the record.
Ask for identity | We need the complete product identification.
Use the order reference | The order names a particular product series.
Identify the missing record | The delivery label is incomplete.
Avoid premature rejection | The numerical difference alone does not prove the delivery is wrong.
Avoid premature acceptance | That explanation does not confirm the delivery is correct.
Separate compatibility | We still need to verify the material and connection requirements.
Request the right document | Please obtain the full label details through the supplier.
Name the data source | The matching manufacturer table defines the relevant dimensions.
Distinguish fitting types | An adapter and a coupling are not interchangeable descriptions.
Keep substitution separate | We have not approved an alternative product.
State the next step | I will reconcile the item identity with the order.
Give a balanced summary | The size comparison is clarified; the delivery remains unverified.''',
    notes='''Not necessarily | Rejects a universal assumption without asserting that the values always differ.
One ... the other | Contrasts two clearly identified quantities.
Alone | Limits what a single piece of evidence can establish.
Still need to | Keeps a remaining verification step explicit.
Matches the designation | Does not by itself establish material or connection compatibility.
Unverified | Neither accepts nor rejects the product without evidence.''',
    d='''Which response best corrects the comparison? | Nominal size and outside diameter are different; we still need full item identification | Different numbers always prove the wrong item | Nominal always equals measured outside diameter | The explanation proves all supplied goods are suitable | The response corrects terminology while preserving the unresolved product check.
Which information should Leila request next? | Complete label details and product identification | An invented replacement size | Immediate installation approval | Only the color of the packaging | Full identification is needed to reconcile the actual item with the order.
Which conclusion is unsupported? | The material and connection are compatible | The order names a product series | The label is incomplete | The numerical comparison needs clarification | Compatibility has not been verified by the available information.
What does a dimensional table need to match? | The relevant identified product and series | Any pipe with a similar color | A different manufacturer's unrelated item | The buyer's preferred number | Dimensions must be read in the context of the actual identified product.''',
    dialogue='''Omar | I think the pipe delivery is the wrong size. The number on our order does not match the outside measurement I have recorded.
Leila | Are you comparing the order's [[nominal size::Nominal size is the designation on the order, not necessarily the measured outside diameter.]] with an outside measurement? Those can be different kinds of information even when the item is correctly identified.
Omar | Yes, that is the comparison. I assumed the ordered size had to equal the measurement across the outside, so I flagged the delivery.
Leila | The [[outside diameter::Outside diameter names the measured outer dimension Omar is comparing with a designation.]] is a physical dimension. The nominal designation names the size within the relevant system; we should not assume the two numbers must match.
Omar | So should I remove the delivery query and tell the site team the goods are correct? I do not want to hold them unnecessarily.
Leila | Not yet. We have clarified the comparison, not the [[product identification::Product identification remains incomplete because the delivery label does not fully identify the goods.]]. The label is incomplete, so I cannot confirm which exact item arrived.
Omar | The order does name the series we wanted. I can give you that order reference, but the delivery label does not show everything.
Leila | Good. We can use the [[product series::Product series provides the ordered family against which full delivery identification must be checked.]] on the order as a reference. We still need the complete details for the supplied item.
Omar | Would the full manufacturer's item code be more useful than my description of the packaging? I can ask the supplier for that information.
Leila | Yes, the [[part number::Part number identifies a particular manufacturer item more precisely than packaging appearance.]] and full label details will help us reconcile the delivery. Please keep the recorded measurement too; it remains useful information.
Omar | I will keep it. Once the identity is clear, where do we look for the dimensions rather than guessing from the size name?
Leila | The matching manufacturer's [[dimensional table::Dimensional table defines measurements for the identified product rather than an unrelated pipe.]] is the appropriate reference. It must belong to the relevant product, not merely something with a similar description.
Omar | There is also a question from the site about whether the supplied component will join the specified item. Does the nominal designation answer that?
Leila | No. We still need the [[connection type::Connection type concerns the joining interface and cannot be inferred from nominal size alone.]] and relevant requirements. The size name alone does not establish that two components can be used together.
Omar | Understood. I should not describe the delivery as an approved alternative either, even if the supplier says the dimensions look close.
Leila | Correct. A [[substitution::Substitution means replacing a specified product; no such replacement is approved by this discussion.]] needs its own review. We have not verified material or connection compatibility, and we have not accepted another product in place of the order.
Omar | Let me check the message: the different numbers do not prove the goods are wrong, but the incomplete label means we cannot confirm them yet.
Leila | Exactly. Keep the [[acceptance status::Acceptance status must remain unresolved while identification and compatibility checks are incomplete.]] unchanged while I reconcile the details. Neither the numerical difference nor my explanation should be treated as a final product decision.
Omar | I will obtain the full label information and part number from the supplier, then send them with the order reference and recorded measurement.
Leila | Thank you. That gives us a proper basis to investigate the [[supply discrepancy::Supply discrepancy identifies the unresolved delivery question without assuming either rejection or acceptance.]]. We can resolve the actual delivery question without relying on a misleading comparison.''',
    transfer_title='Clarify the comparison, retain the query',
    transfer_setup='Complete the supplier summary. Distinguish the designation from the measurement and preserve the missing identification.',
    transfer='''Buyer: "The order gives a ___ size." | nominal | Nominal identifies a size designation rather than necessarily the measured diameter.
Coordinator: "Your measurement is the ___ diameter." | outside | Outside names the physical dimension Omar compared with the designation.
Buyer: "The delivery ___ is incomplete." | label | The incomplete label prevents full identification of the supplied item.
Coordinator: "Compatibility remains ___." | unverified | Neither material nor connection compatibility has been established by the facts.'''
))


BOOK['units'].append(unit(
    title='Reconciling fixture layouts and dimensions',
    scene='The same 450, two different origins',
    skill='Explain a dimension conflict by naming both reference surfaces and requesting a coordinated detail without inventing an offset.',
    brief='Plumber Nia and cabinet coordinator Ben compare a bathroom layout with a cabinet drawing. The layout places the basin centerline 450 millimeters from the finished wall face. The cabinet drawing uses 450 millimeters from the framing face. Basin B2 is selected, but no coordinated rough-in detail is confirmed. The two references are different; no wall-finish thickness is supplied. They need a design clarification, not an assumed conversion or permission to install.',
    cast='Nia | Plumber\nBen | Cabinet coordinator',
    culture=('Show the difference before proposing a remedy', 'Two drawings may contain the same number and still describe different positions. State the origin and endpoint on each. Cross-trade coordination works better when the question identifies the mismatch without blaming the other drawing or quietly inventing a correction.'),
    a='''What reference does the bathroom layout use? | The finished wall face | The framing face | The cabinet door face | The room center | The layout explicitly measures from the finished wall face to the basin centerline.
Why do the two 450-millimeter dimensions conflict? | They start from different reference surfaces | They use different units | The basin has not been selected | One is a confirmed pipe diameter | Equal numbers do not produce equal positions when their reference surfaces differ.
What is not supplied? | A confirmed coordinated rough-in detail | The selected basin identifier | The layout's stated number | The existence of the cabinet drawing | The brief identifies basin B2 but leaves the coordinated rough-in detail unconfirmed.''',
    vocabulary='''basin centerline | Reference line through the center of the basin. | locate the basin centerline
finished wall face | Exposed wall surface after the finish is applied. | measure from the finished wall face
framing face | Surface of the structural framing used as a reference. | reference the framing face
datum | Defined reference from which a dimension is taken. | identify the datum
dimension origin | Starting reference for a measurement. | confirm the dimension origin
dimension endpoint | Point to which a measurement extends. | identify the dimension endpoint
rough-in | Early provision of services before final fixtures or finishes. | coordinate the rough-in
rough-in detail | Drawing information defining relevant preliminary service positions. | confirm the rough-in detail
fixture schedule | List identifying specified fixtures and relevant information. | consult the fixture schedule
selected model | Product chosen for the project. | verify the selected model
layout drawing | Drawing showing intended arrangement of elements. | review the layout drawing
cabinet drawing | Drawing describing the cabinetry arrangement. | compare the cabinet drawing
wall build-up | Layers forming the wall assembly and its finish. | establish the wall build-up
finish thickness | Dimension occupied by the finishing layer or layers. | confirm the finish thickness
offset | Distance between two defined reference positions. | calculate a verified offset
alignment | Relative positioning along a common reference. | coordinate fixture alignment
interface | Meeting point between related building elements or trades. | resolve the cabinet interface
clearance | Required space between or around components. | verify the relevant clearance
design query | Request to clarify design information. | raise a design query
coordinated detail | Information reconciled across the relevant elements and trades. | issue a coordinated detail
drawing reference | Identifier of the drawing supporting a statement. | cite the drawing reference
assumed conversion | Unverified adjustment between reference systems. | avoid an assumed conversion
installation position | Location authorized for the actual installed item. | confirm the installation position
dimension readback | Spoken repetition of a dimension and its references. | give a dimension readback''',
    precision='Both drawings use 450 millimeters, and both concern the basin centerline. The conflict is the origin: finished wall face versus framing face. The shared number does not remove that difference.',
    precision_extra='Basin B2 is selected, but selection alone does not confirm its coordinated service positions. Without the wall build-up and an approved detail, do not invent an offset or turn a clarification into installation authorization.',
    phrases='''State the layout reference | The layout measures from the finished wall face.
State the other reference | The cabinet drawing measures from the framing face.
Keep the endpoint | Both dimensions run to the basin centerline.
Preserve the number | Both drawings state 450 millimeters.
Identify the conflict | The origins differ even though the numbers match.
Avoid an assumed offset | We do not have the wall-finish thickness.
Separate selection from coordination | Basin B2 is selected; the rough-in detail is not confirmed.
Ask the design question | Which datum should the coordinated detail use?
Keep the issue bounded | We are clarifying the reference, not selecting another basin.
Name the interface | The basin and cabinetry need one coordinated position.
Avoid silent correction | I will not adjust either dimension by assumption.
Request the detail | Please confirm a coordinated rough-in detail.
Retain both records | The query should cite both drawings.
State what is unchanged | The selected basin remains B2.
Avoid premature instruction | This query is not permission to install.
Read back the whole dimension | 450 millimeters to the basin centerline, with the origin unresolved.''',
    notes='''From ... to | Identifies both the origin and endpoint of a dimension.
Even though | Highlights why matching numbers do not settle the conflict.
Selected versus confirmed | Product choice and coordinated installation information are separate.
By assumption | Flags an unsupported calculation or adjustment.
Which datum? | Requests a specific design clarification rather than a vague correction.
Remains | Preserves an established fact while another issue is resolved.''',
    d='''Which summary identifies the actual mismatch? | Both show 450 to the centerline, but one starts at the finished face and one at framing | One drawing uses inches and the other millimeters | The client has selected two basins | The drawings disagree about the centerline endpoint | The mismatch concerns the origin, not the number, units, or endpoint.
Which proposed action is unsupported? | Subtract an assumed finish thickness and release installation | Cite both drawing references in the query | Retain B2 as the selected basin | Ask for a coordinated rough-in detail | No finish thickness or approved adjustment is supplied for such a conversion.
What does selecting B2 establish? | The chosen basin model, not a confirmed coordinated rough-in | Every service position | Approval of the cabinet datum | A verified wall build-up | The selected model does not resolve the differing references or missing detail.
Which question is most precise? | Which reference surface governs the coordinated centerline position? | Can someone fix the drawings somehow? | Why did the cabinet team choose the wrong basin? | May we assume the two positions are identical? | Naming the reference surface targets the actual unresolved design issue.''',
    dialogue='''Nia | Before we pass the bathroom information on, I need to resolve the basin position. Both drawings show 450, but they do not start in the same place.
Ben | I see that. The cabinet drawing starts at the [[framing face::Framing face is the origin on the cabinet drawing, distinct from the finished wall surface.]]. Does the bathroom layout use that same surface, or the completed wall surface?
Nia | It uses the completed surface. The dimension runs from the finished wall face to the centerline of the basin, not to its outside edge.
Ben | Then the [[dimension origin::Dimension origin is the starting reference, which differs between these two dimensions.]] differs, even though the endpoint and the number appear to agree. We should make that explicit in the query.
Nia | Yes. I do not want someone to see two matching numbers and assume we have a coordinated position. The difference could be missed in a short email.
Ben | I will describe the layout as 450 millimeters from the [[finished wall face::Finished wall face preserves the bathroom layout's stated origin rather than substituting framing.]] to the basin centerline, then state the cabinet reference separately.
Nia | Keep the number unchanged in both descriptions. We are asking which reference should govern, not silently replacing one drawing with our own calculation.
Ben | Agreed. We do not have the [[finish thickness::Finish thickness is missing, so an offset between framing and finished faces cannot be invented.]], so I cannot convert one dimension into the other and call the result confirmed.
Nia | The basin choice itself is settled. B2 is the selected model, and I do not want the question to reopen the product selection unnecessarily.
Ben | I will preserve B2 in the [[fixture schedule::Fixture schedule identifies the selected basin; it does not settle the coordinated service positions.]] reference. Product selection and the location of the preliminary service provisions are separate pieces of information.
Nia | Exactly. What we do not have is a confirmed detail showing how the plumbing position and cabinet arrangement work together for that basin.
Ben | Then we should request a [[coordinated detail::Coordinated detail reconciles the plumbing and cabinet information rather than favoring an unverified drawing.]], with the datum clearly stated. The query should attach both drawing references so the designer can see the mismatch.
Nia | Would it help to write that both dimensions end at the basin centerline? Otherwise someone might answer a different question about the edge of the bowl.
Ben | Yes. A complete [[dimension readback::Dimension readback repeats the number, origin, and endpoint so the actual ambiguity remains visible.]] needs the number, origin, and endpoint. Here, the origin is unresolved; the centerline endpoint is already identified.
Nia | Can we also make clear that the question does not release the rough-in work? A copied email can otherwise start to sound like a direction.
Ben | Certainly. The [[rough-in detail::Rough-in detail remains unconfirmed despite the selected basin and matching numerical dimensions.]] is not confirmed. Asking for clarification does not authorize either team to use an assumed installation position.
Nia | Let me hear the short version you will send, including B2 and both surfaces. That should keep the request specific enough to answer.
Ben | Selected basin B2; both drawings show 450 millimeters to its centerline. Layout uses finished wall face; cabinet drawing uses framing face. Please resolve the [[datum::Datum names the governing reference that the designer needs to clarify.]] and confirm the coordinated detail.
Nia | That captures it. No invented wall thickness, no revised basin choice, and no claim that the two positions are already the same.
Ben | I will submit that [[design query::Design query requests clarification without creating an installation instruction or approving an assumed offset.]] and keep the rough-in information unconfirmed until the relevant response is received and accepted through the project process.''',
    transfer_title='Read back both references',
    transfer_setup='Complete the coordination exchange. Keep the shared endpoint and number, but do not erase the different origins.',
    transfer='''Plumber: "The layout starts at the ___ wall face." | finished | Finished wall face is the origin explicitly stated on the bathroom layout.
Coordinator: "The cabinet drawing starts at the ___ face." | framing | Framing face is the different origin used by the cabinet drawing.
Plumber: "Both dimensions end at the basin ___." | centerline | Centerline is the shared endpoint, not the basin edge.
Coordinator: "The coordinated rough-in detail remains ___." | unconfirmed | Basin selection does not establish the missing coordinated rough-in detail.'''
))


BOOK['units'].append(unit(
    title='Describing moisture without diagnosing its source',
    scene='A dry patch is not a diagnosis',
    skill='Report the observed condition with a time limit, acknowledge a customer concern, and avoid unsupported cause or repair claims.',
    brief='Shop owner Rosa asks plumber Arun about a ceiling stain below an upstairs washroom. The visible patch is dry during the visit. No pipework is visible, and the source of the staining has not been established. Rosa asks whether the dry surface proves a leak has stopped. Arun must distinguish the visible condition from a diagnosis, preserve the location in the record, and explain that the source still needs assessment. No completed repair or structural assessment is supplied.',
    cast='Rosa | Shop owner\nArun | Plumber',
    culture=('Give a useful limit, not a vague refusal', 'A customer asking whether a problem has stopped often wants reassurance. Acknowledge that need, state what was actually observed, and explain what the observation cannot establish. Precise limits can remain courteous without sounding dismissive or alarmist.'),
    a='''What was observed during the visit? | The visible ceiling patch was dry | All concealed pipework was sound | A repair had stopped a leak | The upstairs basin was the source | Only the visible patch condition during the visit is established.
What is not visible? | The pipework | The ceiling stain | The shop location | The upstairs washroom's position | The brief explicitly states that no pipework is visible.
What remains unresolved? | The source of the staining | Whether a stain exists | Whether the patch was dry during the visit | Whether Rosa asked a question | The visible surface condition does not establish the origin of the staining.''',
    vocabulary='''ceiling stain | Discoloration on a ceiling surface. | record the ceiling stain
visible patch | Area of surface condition available to observation. | describe the visible patch
surface condition | State of the exposed material at a given time. | report the surface condition
concealed pipework | Pipes hidden from view behind building finishes. | distinguish concealed pipework
washroom | Room containing washing or toilet facilities. | locate the upstairs washroom
moisture source | Origin of water or dampness affecting a location. | investigate the moisture source
dry at the visit | Without observed surface wetness during that attendance. | state dry at the visit
historical staining | Discoloration remaining from an earlier event. | distinguish historical staining
active leak | Water escape occurring at the relevant time. | establish an active leak
intermittent condition | Problem that occurs at intervals rather than continuously. | describe an intermittent condition
recurrence | Return of a previously reported condition. | record a recurrence
observation scope | Extent of what was actually seen or assessed. | define the observation scope
time qualifier | Wording limiting a statement to a specified period. | retain the time qualifier
causal claim | Statement identifying why something happened. | avoid an unsupported causal claim
diagnosis | Determination of the nature or cause of a problem. | distinguish observation from diagnosis
assessment | Relevant examination or evaluation of a condition. | arrange an assessment
inspection limitation | Boundary on what could be examined. | explain the inspection limitation
repair claim | Statement that corrective work has been completed. | verify a repair claim
resolution | Established correction or closure of the reported issue. | avoid premature resolution
qualified statement | Statement with explicit limits on its meaning. | make a qualified statement
evidence | Information supporting a conclusion. | distinguish evidence from assumption
attribution | Identification of who supplied an account. | preserve attribution
client concern | Customer's question or worry about the condition. | acknowledge the client concern
finding summary | Concise account of established observations and limits. | give a finding summary''',
    precision='Dry during the visit describes a surface and a time. It does not prove that no leak exists, that a previous leak has stopped, or that a particular concealed pipe caused the stain.',
    precision_extra='The stain is below a washroom, but that location does not identify its source. Preserve the visible observation, concealed-pipework limit, and unresolved cause. No repair result or structural conclusion follows from this account.',
    phrases='''Acknowledge the concern | I understand why you want to know whether it has stopped.
State the observation | The visible patch is dry during this visit.
Keep the time attached | That statement applies to what is visible now.
Identify the limitation | No pipework is visible from this position.
Avoid a cause claim | The source of the staining has not been established.
Separate location from origin | Below the washroom describes location, not a proven source.
Avoid a repair claim | I have no completed repair to report.
Keep uncertainty specific | We cannot infer that a leak has stopped from this surface alone.
Retain the customer account | I will keep your concern in the record.
Avoid dismissing the stain | The dry surface does not make the stain irrelevant.
Name the next need | The source still needs assessment.
Distinguish symptom and diagnosis | A stain is an observation, not a diagnosis.
Avoid a blanket assurance | I cannot confirm the concealed pipework's condition from this view.
Use a bounded summary | Visible patch dry at the visit; source unresolved.
Correct an overstatement | Please replace leak stopped with patch dry during visit.
Close without invented certainty | I can report the observation, but not a confirmed resolution.''',
    notes='''During this visit | Limits a statement in time rather than generalizing indefinitely.
Visible | Restricts the statement to what could be seen.
Below versus caused by | One describes position; the other assigns cause.
Does not prove | Rejects an inference without asserting the opposite.
Still needs assessment | Identifies a remaining task without predicting its outcome.
Cannot confirm | Marks a specific evidence limit, not disbelief in the customer.''',
    d='''Which statement is best supported? | The visible patch was dry during the visit; source unresolved | The leak has definitely stopped | The upstairs basin caused the stain | The concealed pipework is fault-free | The supported wording preserves both the observation and the unresolved cause.
What is wrong with saying leak stopped? | It infers a change in a leak that has not been established | It uses too few words | It preserves the observation time too carefully | It identifies the patch location | Dry surface condition does not establish an active leak's history or cessation.
Which phrase best communicates the inspection limit? | No pipework was visible from this position | All pipework was inspected | The washroom was proved unrelated | The entire structure was assessed | The phrase states the actual visibility limit without inventing a broader examination.
What should the report avoid? | A repair or structural conclusion unsupported by the visit | The location of the stain | The dry surface observation | The unresolved-source statement | Neither a completed repair nor structural assessment is supplied in the brief.''',
    dialogue='''Rosa | The stain is below the upstairs washroom, but the patch looks dry today. Can I tell the shop manager that the leak has stopped?
Arun | I can confirm the [[surface condition::Surface condition refers to the visible patch, not the state of concealed pipework.]] we can see during this visit. I cannot turn that into confirmation that a leak has stopped.
Rosa | I see the distinction, but I need something more useful than we do not know. What can I accurately put in the manager's update?
Arun | Say the [[visible patch::Visible patch limits the observation to the exposed stained area that Arun can see.]] is dry during the visit. Keep the time in the sentence, and add that the source of the staining has not been established.
Rosa | Does the fact that the washroom is directly above help us name the cause, or does that only describe where we found the stain?
Arun | It describes the location. It does not establish the [[moisture source::Moisture source concerns origin, which the location below a washroom does not prove.]]. No pipework is visible here, so we should not name a concealed component as responsible.
Rosa | I had been going to write that the basin upstairs must have leaked. I will leave that out unless there is an actual finding.
Arun | That is right. It would be a [[causal claim::Causal claim assigns the stain to the basin without evidence establishing that connection.]], not a description of the ceiling. We need to keep those two kinds of statement separate.
Rosa | Could the dry patch at least mean that nothing is happening now? I am trying to explain the situation without making the update sound alarming.
Arun | The [[observation scope::Observation scope confines the statement to the visible surface during the visit.]] is the visible surface during this attendance. It does not establish the condition of hidden pipework or prove that an issue cannot recur.
Rosa | Then it would also be wrong to say you checked all the pipes and found no problem. We have not seen them here.
Arun | Exactly. That would erase the [[inspection limitation::Inspection limitation identifies the concealed pipework that was not visible for assessment.]]. The accurate record should say no pipework was visible, rather than imply that every relevant component was examined.
Rosa | I understand. There is no completed repair for me to mention either, is there? I do not want the manager to assume something was fixed.
Arun | Correct. There is no [[repair claim::Repair claim would assert completed corrective work, which this visit account does not establish.]] to make from these facts. We have an observation and an unresolved source, not a documented correction of the problem.
Rosa | Please help me make the final wording concise. I want it to sound clear, not as though I am avoiding the question.
Arun | Use a [[qualified statement::Qualified statement provides explicit limits while still communicating a useful observation.]]: ceiling stain below the upstairs washroom; visible patch dry during the visit; source not established, with assessment still needed.
Rosa | That gives the location, what was seen, and what remains open. I will not shorten dry during the visit to no leak.
Arun | Good. The [[time qualifier::Time qualifier prevents a visit-specific observation from becoming a general assurance.]] matters. Removing it could make a limited observation sound like a continuing assurance about the whole system.
Rosa | I will send that wording and keep the source question open. Thank you for explaining the difference without dismissing what we have noticed.
Arun | You are welcome. That [[finding summary::Finding summary reports established observations and limits without claiming a diagnosis or resolution.]] is accurate and useful. It records the condition we can describe while leaving the cause for the appropriate assessment.''',
    transfer_title='Correct the manager update',
    transfer_setup='Complete the concise report. Preserve the surface observation and the missing source assessment without implying a repair.',
    transfer='''Owner: "The visible patch was ___ during the visit." | dry | Dry is the observed surface condition during the stated attendance.
Plumber: "No ___ was visible." | pipework | The concealed pipework limits what this observation can establish.
Owner: "The source is not ___." | established | The stain location and dry patch do not identify the source.
Plumber: "The source still needs ___." | assessment | Further assessment is needed, without a promised diagnosis or outcome.'''
))


BOOK['units'].append(unit(
    title='Explaining drainage and access terminology',
    scene='The panel is not an extra drain',
    skill='Explain a technical term in ordinary language and distinguish a design request from an approved change to service access.',
    brief='Client Hana reviews a cabinet drawing with plumbing coordinator Dev. The drawing shows a small removable panel for access to a recorded cleanout. Hana calls it an extra drain and asks for it to be permanently covered. The plumber has not reviewed that enclosure change. The designer needs to coordinate the access detail with the plumbing team. No approved panel dimensions, replacement arrangement, or permission to conceal the cleanout is supplied.',
    cast='Hana | Client\nDev | Plumbing coordinator',
    culture=('Explain function before defending terminology', 'A client may object to something because the label suggests the wrong function. Explain what the component does in everyday language, then describe the actual design question. Correcting a term does not require belittling the client or approving the requested change.'),
    a='''What does the removable panel provide? | Access to the recorded cleanout | A second basin drain | A new water supply | A decorative plumbing fixture | The panel is an access feature, not an additional drainage fixture.
What has Hana requested? | Permanent covering of the panel area | Approval of a completed access review | Replacement of the basin model | A new drain location already accepted | The client requests permanent covering, but no approval is established.
Who needs to coordinate the detail? | The designer with the plumbing team | The client alone without review | Only the furniture delivery driver | No one because the panel is decorative | The supplied next step is design coordination with the plumbing team.''',
    vocabulary='''access panel | Removable or openable cover providing access behind a finish. | retain an access panel
cleanout | Fitting or opening provided for access to drainage piping for maintenance. | identify the recorded cleanout
drain | Opening or pipe carrying used water away. | distinguish the drain
drainage line | Pipe route conveying waste water or discharge. | locate the drainage line
waste outlet | Point through which used water leaves a fixture. | identify the waste outlet
service access | Means of reaching equipment or services for relevant work. | preserve service access
removable cover | Cover designed to be taken off through the proper procedure. | specify a removable cover
permanent enclosure | Construction intended to remain closed rather than provide removable access. | review a permanent enclosure
cabinet elevation | Drawing showing the vertical face of cabinetry. | read the cabinet elevation
access detail | Design information showing how services can be reached. | coordinate the access detail
maintenance | Work to preserve or restore a system's relevant condition. | allow for maintenance
clear opening | Unobstructed space available through an opening. | verify the clear opening
obstruction | Item that blocks a required route or space. | identify an obstruction
concealment | Covering that hides an element from view. | review proposed concealment
finish panel | Panel forming an exposed decorative surface. | coordinate the finish panel
fixed panel | Panel not intended to function as a removable access feature. | distinguish a fixed panel
hinged panel | Panel attached so that it can swing open. | identify a hinged panel
serviceable | Capable of receiving relevant maintenance under the required conditions. | verify a serviceable arrangement
design intent | Purpose or intended result of a design feature. | clarify the design intent
appearance request | Client preference about how something looks. | record the appearance request
enclosure change | Proposed alteration to the surrounding cover or construction. | review the enclosure change
access requirement | Condition that access must satisfy for the actual application. | establish the access requirement
review status | Stage of evaluation or acceptance. | confirm the review status
coordination response | Agreed answer from the relevant design and trade review. | await the coordination response''',
    precision='The access panel is not a second drain. It provides a way to reach the recorded cleanout, which serves drainage-maintenance access. Explaining that function does not specify an acceptable panel size or enclosure arrangement.',
    precision_extra='Hana has requested permanent covering, but the plumber has not reviewed that change. Preserve the appearance preference as a request. Do not treat a small symbol on a drawing as proof that access can be removed.',
    phrases='''Clarify the label | That symbol identifies an access panel, not an extra drain.
Explain the function | It provides access to the recorded cleanout.
Define the second term | A cleanout provides maintenance access to the drainage piping.
Acknowledge the appearance concern | I understand that you want a continuous cabinet finish.
Separate request and approval | I can record that preference, but it is not an approved change.
Name the unreviewed item | The proposed permanent enclosure has not been reviewed by the plumber.
Avoid inventing dimensions | We do not have approved access dimensions here.
Keep function distinct | Hiding a component and preserving access are different questions.
Name the coordinator | The designer needs to coordinate this with the plumbing team.
Ask for the actual detail | Please confirm how the required access will be provided.
Avoid a casual assurance | I cannot confirm that permanent covering is acceptable.
Keep alternatives conditional | Any alternative arrangement needs the relevant review.
Distinguish the panel types | A fixed finish panel is not automatically an access panel.
Record the preference | The client requests a less visible panel arrangement.
Preserve the status | The enclosure change remains unapproved.
Close with the next step | We will seek a coordinated access detail before confirming a change.''',
    notes='''Provides access to | Explains function without giving instructions to open or use the component.
Not an extra drain | Corrects the specific misunderstanding rather than criticizing the speaker.
Would like versus will | Separates preference from a confirmed design commitment.
Has not been reviewed | States the missing evaluation, not an automatic rejection.
Any alternative | Keeps every proposed replacement subject to the relevant requirements.
Before confirming | Makes review a condition of a later commitment.''',
    d='''Which explanation is clearest? | The panel lets the relevant team reach the cleanout; it is not another drain | The panel drains the cabinet | The cleanout is merely decorative | A small panel never needs review | The explanation separates the access cover from the drainage-maintenance feature.
What should Dev do with Hana's preference? | Record it for design coordination without approving concealment | Promise permanent covering immediately | Remove the cleanout from the record | Treat the preference as a completed plumbing review | Recording a preference does not establish an acceptable access arrangement.
Which claim is unsupported? | The drawn panel dimensions are approved and sufficient | The drawing shows a removable panel | The client wants a continuous finish | The plumber has not reviewed the change | No approved dimensions or verified access arrangement are supplied.
What is the appropriate next step? | Coordinate the access detail with the designer and plumbing team | Give the client instructions to dismantle the panel | Approve a fixed cover based on appearance | Assume all removable covers are interchangeable | The case calls for design coordination, not client intervention or assumed equivalence.''',
    dialogue='''Hana | On this cabinet drawing, why is there an extra drain in the front panel? I would prefer a continuous finish across that whole section.
Dev | The marked feature is an [[access panel::Access panel is the cover shown in the cabinet drawing, not another drain.]], rather than an additional drain. It provides access to a recorded plumbing component behind the cabinet finish.
Hana | That makes more sense. The label says cleanout, which is not a word I use. Is that another name for the basin outlet?
Dev | No. A [[cleanout::Cleanout identifies drainage-maintenance access, distinct from the basin's waste outlet.]] provides access to drainage piping for maintenance. The basin outlet and this access feature should not be treated as the same thing.
Hana | I understand the function now. Could we permanently cover the front anyway? I would rather not have a visible break in the cabinet face.
Dev | I can record that [[appearance request::Appearance request preserves Hana's preference without turning it into an approved enclosure change.]], but the plumber has not reviewed the enclosure change. I cannot confirm permanent covering as an acceptable arrangement.
Hana | I am not asking to change the drainage route. I am asking whether the cabinet can look continuous while keeping whatever access is needed.
Dev | That is a clearer design question. The designer needs to coordinate the [[access detail::Access detail determines how required access is provided within the proposed cabinet arrangement.]] with the plumbing team, including how the relevant component can be reached.
Hana | Does the small rectangle on the drawing tell us the opening is already large enough? It looks quite small compared with the cabinet door.
Dev | Not from this information. We do not have an approved [[clear opening::Clear opening is the usable access space, whose approved dimensions are not supplied here.]] or a confirmed replacement arrangement. The symbol alone cannot establish that a particular access solution is sufficient.
Hana | Then I should not tell the cabinet maker to replace the removable part with a fixed decorative panel just because it looks cleaner.
Dev | Correct. A [[fixed panel::Fixed panel does not automatically perform the access function of the removable panel it would replace.]] is not automatically equivalent to the removable feature. We need the access requirements resolved before anyone confirms that change.
Hana | Could the design team consider something less visible without assuming that I have demanded a specific technical solution? I am open to their advice.
Dev | Yes. We can record your preference separately from the [[access requirement::Access requirement concerns the conditions the final arrangement must satisfy, independent of appearance preference.]]. Any alternative still needs review; I am not promising a particular panel type or location.
Hana | Please make the request specific. I do not want the next drawing to remove the access entirely because my first email called it an extra drain.
Dev | I will clarify the [[design intent::Design intent explains the access function that must not be lost through the client's earlier terminology.]] in the note: the feature provides access to a cleanout, and the client asks for a less visible arrangement.
Hana | That accurately describes what I want. Who needs to respond before I can regard the cabinet appearance as settled?
Dev | We need the designer and plumbing team to provide a [[coordination response::Coordination response is the relevant combined review needed before the access arrangement can be confirmed.]]. Until then, the permanent-enclosure proposal remains unapproved and the access question stays open.
Hana | All right. I will describe this as an access-detail review, not a request to delete a drain or an instruction to cover the opening.
Dev | Thank you. That keeps the [[review status::Review status preserves the distinction between a client request and an accepted design change.]] clear while giving the design team an answerable question about appearance and access, without authorizing an unreviewed alteration.''',
    transfer_title='Explain the panel and the pending review',
    transfer_setup='Complete the client exchange. Name the access feature and preserve the approval boundary.',
    transfer='''Client: "The panel is not an extra ___." | drain | The feature provides access rather than acting as an additional drain.
Coordinator: "It provides access to a ___." | cleanout | Cleanout is the recorded drainage-maintenance access feature behind the panel.
Client: "The designer will coordinate the access ___." | detail | The access detail must reconcile the cabinet arrangement with plumbing requirements.
Coordinator: "Permanent covering is not yet ___." | approved | The plumber has not reviewed the proposed enclosure change for acceptance.'''
))


BOOK['units'].append(unit(
    title='Coordinating interruptions and room access',
    scene='Arrival at nine, proposed interruption at ten',
    skill='Correct a notice by separating attendance time, affected area, proposed interruption window, and pending approval.',
    brief='Service coordinator Imani speaks with tenant representative Joel about a plumbing visit booked for 09:00. A water interruption is proposed for 10:00-11:00, pending building-manager approval. The stated affected area is the east washroom only. Joel thinks the whole building will be unavailable from 09:00. Imani must correct both the extent and the timing without presenting the proposed interruption as confirmed. The conversation supplies no instruction to operate valves or begin work.',
    cast='Imani | Service coordinator\nJoel | Tenant representative',
    culture=('Separate the clocks and the commitments', 'A visit, an interruption, and a room-access arrangement can appear in one message but have different times and approval states. Give each its own sentence. Correcting one misunderstanding must not leave another in place or make a proposal sound booked.'),
    a='''What is booked for 09:00? | The plumbing visit | A whole-building shutdown | The end of the interruption | A completed valve operation | The booked time belongs to attendance, not to the proposed interruption.
What is the proposed interruption window? | 10:00-11:00 | 09:00-11:00 | All day | 09:00-10:00 already approved | The proposal is specifically 10:00-11:00 and remains pending approval.
What is the stated affected area? | The east washroom only | The whole building | Every washroom | The west washroom only | The supplied scope is limited to the east washroom.''',
    vocabulary='''attendance time | Time scheduled for the service team to arrive. | confirm the attendance time
interruption window | Defined period proposed or agreed for a service interruption. | state the interruption window
affected area | Location included in the stated impact. | identify the affected area
east washroom | Particular room identified by its east-side location. | specify the east washroom
building manager | Person responsible for relevant building coordination. | seek building-manager approval
tenant representative | Person communicating on behalf of occupants. | brief the tenant representative
proposed interruption | Suggested service pause not yet confirmed. | describe the proposed interruption
approved interruption | Service pause accepted through the relevant approval process. | distinguish an approved interruption
booking confirmation | Record establishing an agreed appointment. | read the booking confirmation
notice wording | Text used to inform affected people. | correct the notice wording
impact scope | Extent of the service or area affected. | define the impact scope
pending approval | Awaiting a required acceptance decision. | retain pending-approval status
start time | Beginning of a defined event or period. | preserve the start time
end time | Finish of a defined event or period. | state the end time
room availability | Whether a room is available under stated conditions. | clarify room availability
access arrangement | Agreed means or conditions for reaching a work area. | coordinate the access arrangement
occupant communication | Information provided to people using the premises. | prepare occupant communication
whole-building claim | Statement that the entire premises is affected. | correct a whole-building claim
confirmed appointment | Visit that has been booked rather than merely suggested. | distinguish the confirmed appointment
operating instruction | Direction to act on equipment or a system. | distinguish an operating instruction
schedule readback | Repetition of times, scope, and status for confirmation. | give a schedule readback
status qualifier | Wording identifying certainty or approval stage. | preserve the status qualifier
notice release | Authorization to issue the relevant communication. | confirm notice release
coordination update | New information about arrangements and outstanding decisions. | provide a coordination update''',
    precision='The visit is booked for 09:00. The interruption is proposed for 10:00-11:00, with building-manager approval pending. Do not move the interruption to the arrival time or call the proposal confirmed.',
    precision_extra='The east washroom is the stated affected area, not the whole building. The corrected wording must preserve both scope and status. This scheduling conversation is not authorization to operate valves or start an interruption.',
    phrases='''Separate the appointment | The visit is booked for 09:00.
State the proposed window | The proposed interruption is 10:00-11:00.
Limit the area | The stated affected area is the east washroom only.
Name the approval | Building-manager approval is still pending.
Correct the first misunderstanding | Arrival at 09:00 does not mean interruption at 09:00.
Correct the second misunderstanding | The proposal does not cover the whole building.
Keep the proposal visible | Please retain proposed in the notice.
Avoid overstating certainty | We cannot describe that window as confirmed yet.
Give separate sentences | Put the visit time and interruption window on separate lines.
Read back both endpoints | The proposed start is 10:00 and the proposed end is 11:00.
Preserve the booked item | The attendance booking remains at 09:00.
Avoid invented access terms | Separate room-access arrangements still need their actual coordination.
Distinguish notice and action | This message is not an operating instruction.
Name the correction | We need to correct timing, area, and approval status.
Keep release separate | The final notice still needs the relevant release process.
Close with a precise update | Visit booked; east-washroom interruption proposed; approval pending.''',
    notes='''Booked versus proposed | Identifies two different levels of commitment.
Only | Restricts the stated impact to the named area.
From ... to | Supplies both endpoints of a time window.
Still pending | Makes the unresolved approval visible after other details are corrected.
Does not mean | Blocks an inference from arrival time to service interruption.
Separate lines | Helps readers avoid combining distinct events into one schedule.''',
    d='''Which notice wording preserves all supplied facts? | Visit 09:00; east-washroom interruption proposed 10:00-11:00, pending approval | Whole building closed from 09:00 | East washroom interruption confirmed from 09:00 | Visit proposed at 11:00, interruption approved | The first wording separates the booked visit from the limited, unapproved interruption.
What is wrong with only changing whole building to east washroom? | Timing and approval status may still be wrong | It removes the correct building name | It changes an approved interruption to a proposal | It supplies too much technical detail | Correcting the area alone does not correct the arrival-time confusion or pending approval.
Which item is already confirmed? | The 09:00 visit booking | The proposed interruption | The whole-building effect | Valve operating permission | The case confirms attendance only, not the proposed service interruption.
What should Joel avoid treating the message as? | Permission to operate valves or start an interruption | A correction of the area | A statement of the proposed window | A clarification of attendance time | Scheduling language does not provide an operational instruction or authorization.''',
    dialogue='''Joel | I was about to tell the tenants the whole building will be unavailable from nine. That is when the plumbing team is booked, correct?
Imani | The [[attendance time::Attendance time belongs to the booked visit and does not establish the start of an interruption.]] is 09:00, yes. But that is not the proposed start of the water interruption, and the proposal does not cover the whole building.
Joel | Thank you for stopping me. I have combined the arrival and the interruption into one message. What are the two times I should keep separate?
Imani | The visit is booked for nine. The proposed [[interruption window::Interruption window identifies the separate proposed service pause from 10:00 to 11:00.]] is 10:00-11:00. Those are separate events, and they also have different approval states.
Joel | Before we get to approval, can you confirm the area named in the proposal? I should correct the whole-building wording as well.
Imani | The stated [[affected area::Affected area is limited to the east washroom, not the entire building.]] is the east washroom only. Please keep that room name attached to the proposed interruption rather than describing every area as unavailable.
Joel | So I can write east washroom unavailable from ten to eleven, with the visit at nine. Does that now accurately capture the arrangement?
Imani | It still needs the [[status qualifier::Status qualifier retains proposed status and prevents the revised notice from implying approval.]]. The interruption is proposed, not confirmed, because building-manager approval is pending. Your revised sentence currently sounds like a firm arrangement.
Joel | I see. Correcting the room and the times is not enough if I drop the fact that someone still has to approve the interruption.
Imani | Exactly. The [[building manager::Building manager is the named approval role whose decision remains pending in the case.]] has not approved that proposal yet. We need both the accurate details and the accurate level of certainty in the communication.
Joel | Would separate lines help? One for the booked visit, then another for the proposed interruption with the room and approval note together?
Imani | Yes. That would improve the [[notice wording::Notice wording should distinguish the booked visit from the proposed, limited interruption.]] and make the distinction easier to scan. Keep 09:00 with attendance and 10:00-11:00 with the proposed east-washroom interruption.
Joel | I will not add a wider room-access arrangement from my own assumptions. That needs its actual coordination rather than a guess based on the visit.
Imani | Correct. We should not invent an [[access arrangement::Access arrangement must come from actual coordination rather than being inferred from the visit booking.]] in this correction. We are clarifying the supplied timing, impact, and approval status, not adding new permissions.
Joel | Let me read it back: visit booked for 09:00. East-washroom water interruption proposed for 10:00-11:00, with building-manager approval still pending.
Imani | That [[schedule readback::Schedule readback preserves both times, the limited area, and the unresolved approval in one accurate summary.]] is accurate. It fixes the earlier whole-building claim without turning the interruption into a confirmed event.
Joel | When that wording is reviewed, it will be a tenant notice, not a direction for anyone to begin the interruption or operate equipment.
Imani | Precisely. It is not an [[operating instruction::Operating instruction would direct equipment action, which this scheduling conversation does not authorize.]]. Actual operations and the release of the final notice must follow their separate relevant processes.
Joel | I will replace the earlier draft with the corrected wording and keep the approval note visible. I will not tell tenants the window is confirmed.
Imani | Thank you. That gives us a clear [[coordination update::Coordination update communicates the corrected arrangements while keeping the outstanding decision explicit.]]: booked visit, limited proposed interruption, and a named approval still outstanding. Those distinctions should remain in any later summary.''',
    transfer_title='Separate the two times',
    transfer_setup='Complete the corrected schedule notice. Preserve the room limit and the proposal status.',
    transfer='''Coordinator: "The visit is booked for ___." | 09:00 | The confirmed booking concerns attendance at nine, not the service interruption.
Representative: "The interruption is proposed for ___." | 10:00-11:00 | The proposed window starts at ten and ends at eleven.
Coordinator: "It concerns the ___ washroom only." | east | East washroom is the stated limited area in the proposal.
Representative: "Building-manager approval remains ___." | pending | Pending preserves the fact that the proposed interruption is not yet approved.'''
))


BOOK['units'].append(unit(
    title='Pricing changes and restoration boundaries',
    scene='A fixture allowance is not a vanity package',
    skill='Explain the limits of an estimate, separate a product allowance from related work, and request a revised scope before confirming terms.',
    brief='Client Ava discusses an estimate with plumbing estimator Luis. The estimate covers replacing basin B1 with the specified model. Ava now wants a wall-hung vanity and assumes the fixture allowance includes cabinet changes and redecoration, neither of which appears in the estimate. Access requirements and the revised plumbing scope have not been assessed. Luis must explain the original coverage, record the change request, and avoid quoting an unsupported extra cost or completion date.',
    cast='Ava | Client\nLuis | Plumbing estimator',
    culture=('Explain the document, not the customer fault', 'A customer may read an allowance as a complete package. Point to what the estimate actually includes, acknowledge the desired change, and distinguish the additional questions. Clear boundaries need not sound defensive or imply that every related cost has already been calculated.'),
    a='''What does the current estimate cover? | Replacing B1 with the specified basin model | A complete wall-hung vanity installation package | Cabinet changes and redecoration | Every possible access repair | The stated estimate concerns replacement of B1 with the specified model.
What is Ava assuming? | The fixture allowance includes cabinet changes and redecoration | The original model has no identifier | A revised assessment is complete | Luis has supplied a new completion date | The brief names these related works as Ava's assumption, not quoted inclusions.
What remains unassessed? | Access requirements and revised plumbing scope | The existence of the original estimate | Ava's request for a wall-hung vanity | The fact that B1 is the original fixture | The changed arrangement still needs assessment before its scope or terms can be confirmed.''',
    vocabulary='''estimate | Stated assessment of expected cost for defined work. | review the estimate
fixture allowance | Amount allocated for a fixture within the stated estimate terms. | clarify the fixture allowance
specified model | Product identified in the agreed or proposed scope. | retain the specified model
basin replacement | Work to replace the identified basin. | define the basin replacement
wall-hung vanity | Vanity assembly supported from a wall rather than standing on the floor. | assess the wall-hung vanity request
cabinet alteration | Change to the cabinetry arrangement or construction. | price cabinet alterations
redecoration | Renewal of decorative finishes. | distinguish redecoration
making good | Restoring affected surfaces after work, within an agreed scope. | define making good
access requirements | Conditions or provisions needed to reach the work. | assess access requirements
revised scope | Updated description of work after a change. | agree the revised scope
scope inclusion | Item expressly covered by the stated work. | identify scope inclusions
scope exclusion | Item expressly left outside the stated work. | check scope exclusions
unlisted work | Work not described in the current estimate. | identify unlisted work
change request | Proposal to alter the existing scope or selection. | record a change request
additional cost | Cost beyond the amount already stated. | assess additional cost
revised quotation | Updated price proposal for a defined changed scope. | prepare a revised quotation
commercial terms | Conditions concerning price, timing, and agreement. | confirm commercial terms
completion date | Date agreed or proposed for finishing defined work. | confirm the completion date
trade coordination | Alignment of work between the relevant specialists. | arrange trade coordination
scope boundary | Limit separating included work from other work. | explain the scope boundary
price assumption | Belief about cost not yet confirmed in the agreement. | correct a price assumption
restoration boundary | Limit of any agreed surface reinstatement. | clarify the restoration boundary
client selection | Product or arrangement chosen by the customer. | record the client selection
approval to proceed | Authorization to carry out the agreed work. | obtain approval to proceed''',
    precision='The estimate covers the specified replacement of B1. The fixture allowance does not establish that cabinet alterations and redecoration are included. Explain the actual document instead of treating an allowance as a complete project package.',
    precision_extra='The wall-hung vanity request changes the arrangement. Access requirements and revised plumbing work remain unassessed. Do not invent the cost, required construction, restoration extent, or completion date before that assessment and agreement.',
    phrases='''State the original coverage | The estimate covers replacement of B1 with the specified model.
Identify the new request | You are now asking for a wall-hung vanity.
Clarify the allowance | The fixture allowance has the scope stated in this estimate.
Name the unlisted work | Cabinet changes and redecoration are not listed here.
Avoid blame | I can see why you read that as a complete package.
Separate the tasks | Product supply, plumbing work, and restoration need distinct scope descriptions.
Keep access open | We have not assessed the access requirements for the new arrangement.
Keep the plumbing scope open | The revised plumbing scope also needs assessment.
Avoid an invented extra | I cannot give you a reliable additional figure yet.
Avoid a date promise | We have not confirmed completion timing for the changed work.
Record the request | I will record the wall-hung vanity as a change request.
Ask for the revised basis | We need a defined scope before confirming the revised price.
Clarify making good | Any making-good work needs its own stated extent.
Preserve the original reference | The current estimate remains our reference for the original replacement.
Keep approval separate | This discussion is not approval to proceed with extra work.
Close with the next stage | We will assess the changed scope and then confirm revised terms.''',
    notes='''Covers | Identifies the actual stated work, not everything associated with the room.
Not listed | Describes a document limit without inventing another contract term.
Now asking for | Marks a change from the original arrangement.
Before confirming | Makes scope definition a condition of a reliable commitment.
Any making good | Avoids assuming all restoration is included or already priced.
Reliable figure | Explains why a price cannot responsibly be supplied before assessment.''',
    d='''Which response best addresses Ava's assumption? | The estimate covers B1 replacement; cabinet changes and redecoration are not listed | All related work is automatically covered by an allowance | The wall-hung vanity has already been installed | No plumbing assessment is needed for any vanity change | The response states the estimate's actual coverage and identifies the unlisted related work.
What must happen before revised terms can be confirmed? | Assess access requirements and define the revised scope | Reuse the original date automatically | Assume all cabinet work is free | Treat the product preference as installation approval | The changed arrangement requires assessment before price and timing can be established.
Which phrase overpromises? | The wall-hung vanity will cost exactly the same and finish on the original date | I will record the change request | Cabinet changes are not listed here | We need to define any making-good work | Neither unchanged cost nor unchanged timing is supported for the unassessed change.
What does making good need in an agreement? | A defined extent of restoration | An assumption that every surface is included | A guessed repair method | No connection to the scope | Restoration boundaries must be stated rather than inferred from a broad phrase.''',
    dialogue='''Ava | I would like to change the basin replacement to a wall-hung vanity. I assumed the fixture allowance covered the cabinet changes and repainting around it.
Luis | The current [[estimate::Estimate refers to the existing cost document for the specified B1 replacement.]] covers replacing B1 with the specified basin model. Cabinet changes and redecoration are not listed, so we need to separate those from the original work.
Ava | I read the allowance as a budget for the whole area, not just the fixture described. Is that where my reading went wrong?
Luis | I can see how that happened. The [[fixture allowance::Fixture allowance has the scope stated in the estimate and does not establish all related work as included.]] must be read with the scope stated in the estimate. It does not establish a complete vanity-and-decoration package here.
Ava | I still prefer the wall-hung arrangement. Can we keep that as my request without assuming I have accepted a new price already?
Luis | Certainly. I will record a [[change request::Change request records the new arrangement without treating it as agreed scope or accepted price.]] for the wall-hung vanity. We then need to assess what changes in the plumbing work and the related arrangements.
Ava | What is missing before you can tell me the difference in cost? I would like to understand why a quick fixture-price comparison is not enough.
Luis | We have not assessed the [[access requirements::Access requirements concern reaching the changed work and remain unassessed in the case.]] or the revised plumbing scope. The product price alone does not tell us what work the new arrangement requires.
Ava | Does that mean you are already saying extra cabinet construction is definitely required, or only that the current estimate does not include those changes?
Luis | Only the second is established here. A [[cabinet alteration::Cabinet alteration is related work not listed in the original estimate, not a predetermined technical requirement.]] is not listed in the current estimate; I am not inventing a construction requirement before the arrangement is assessed.
Ava | That is helpful. I also want any affected surfaces to look finished afterward. I have heard people call that making good.
Luis | Yes, but [[making good::Making good means agreed restoration and needs a defined extent rather than an unlimited assumption.]] needs a clear stated extent. We should not assume it includes every cabinet change or all redecoration without describing and pricing the relevant work.
Ava | Could you give me a firm extra amount now and revise the details later? It would help me decide whether to keep the new idea.
Luis | I cannot give a reliable [[additional cost::Additional cost cannot be fixed reliably while the changed work and access remain unassessed.]] before the scope is assessed. A guessed figure could make the decision look simpler now and create a misunderstanding later.
Ava | Fair enough. Does the original completion date carry over automatically, or should I regard timing as another point to confirm for the change?
Luis | Timing also needs review. The [[completion date::Completion date for the changed work is not established by the original estimate.]] for the changed work is not confirmed. We need to define the work and coordinate it before promising the revised terms.
Ava | Then the next document should show what the plumbing work covers, what happens to the cabinet and finishes, and what is outside the price.
Luis | Exactly. A [[revised quotation::Revised quotation sets out a price proposal for a defined changed scope rather than merely restating the product allowance.]] should make those boundaries clear. The original estimate remains the reference for the specified B1 replacement, not evidence that the new package is included.
Ava | Please proceed with assessing the request, but do not treat this conversation as my approval for unpriced additional installation work.
Luis | Understood. There is no [[approval to proceed::Approval to proceed with extra work has not been given by this assessment request.]] with the extra work. We will assess the changed scope, state the price and timing, and obtain the relevant agreement before treating them as commitments.''',
    transfer_title='State what is and is not priced',
    transfer_setup='Complete the estimate discussion. Preserve the original scope and the need to assess the changed arrangement.',
    transfer='''Estimator: "The estimate covers replacement of ___ with the specified model." | B1 | B1 identifies the fixture in the original stated estimate.
Client: "Cabinet changes and ___ are not listed." | redecoration | Redecoration is one of the related works not listed in the estimate.
Estimator: "The revised scope still needs ___." | assessment | The access requirements and changed plumbing scope have not yet been assessed.
Client: "Price and timing are not yet ___ for the change." | confirmed | Revised terms cannot be treated as agreed while the changed scope remains unassessed.'''
))


BOOK['units'].append(unit(
    title='Handing over plumbing records and follow-up',
    scene='The wrong leaflet and an unbooked visit',
    skill='Acknowledge received records, identify a model mismatch, and separate a promised update from an unconfirmed return appointment.',
    brief='At handover, client Maya receives a pack for basin B1, but the care leaflet belongs to the previous model. Service lead Leo takes responsibility for obtaining the replacement leaflet and promises to call on Monday. A separate cosmetic-trim review requires a return visit, but no date is booked. Maya and Leo must keep the document correction and visit arrangement distinct. Receipt of the pack does not make its mismatched leaflet appropriate for the current model.',
    cast='Maya | Client\nLeo | Service lead',
    culture=('Close the conversation without closing unfinished work', 'A handover can include received documents and open items at the same time. Name each unfinished item, assign an owner, and distinguish a communication date from a visit date. A polite closing should not erase a remaining mismatch or imply everything is complete.'),
    a='''What is wrong with the care leaflet? | It belongs to the previous model | It is confirmed for B1's current model | It books the return visit | It changes the warranty terms | The supplied leaflet does not match the current model in the handover pack.
What does Leo promise for Monday? | A call about follow-up | A confirmed return visit | Completion of every open item | A replacement installation | Monday is the promised communication date, not a booked site visit.
What remains unscheduled? | The return visit for cosmetic-trim review | The Monday call commitment | The fact that the pack was received | The identification of Leo as owner | The cosmetic-trim review needs a return visit, but no date is booked.''',
    vocabulary='''handover pack | Collection of records supplied when work is handed over. | receive the handover pack
care leaflet | Product information describing relevant care instructions. | obtain the correct care leaflet
model mismatch | Difference between the product identified and the document supplied. | record the model mismatch
previous model | Product version or selection used before the current one. | distinguish the previous model
current model | Product now relevant to the installation or record. | identify the current model
replacement document | Correct document supplied in place of an unsuitable one. | request the replacement document
product record | Information identifying the relevant supplied or installed item. | reconcile the product record
document receipt | Acknowledgment that records have been delivered. | confirm document receipt
document correction | Amendment or replacement needed to make records accurate. | track the document correction
care guidance | Instructions relevant to maintaining the specified product. | use model-specific care guidance
cosmetic trim | Finishing piece primarily associated with appearance at an interface. | review the cosmetic trim
return visit | Further attendance at the premises. | arrange the return visit
visit booking | Confirmed appointment for attendance. | distinguish a visit booking
follow-up owner | Person responsible for progressing the open item. | name the follow-up owner
callback | Return phone call to provide information or an update. | commit to a callback
update date | Date promised for further communication. | confirm the update date
outstanding item | Matter not yet completed or resolved. | retain an outstanding item
open-item list | Record of matters still requiring action. | maintain the open-item list
completion claim | Statement that relevant work is finished. | verify a completion claim
closeout | Process of resolving and documenting remaining project matters. | manage closeout
warranty record | Document stating relevant warranty information. | retain the warranty record
service record | Account of attendance and work performed. | update the service record
handover readback | Repetition of received records and outstanding actions. | give a handover readback
status update | Communication reporting progress or current position. | provide a status update''',
    precision='The handover pack was received, but the care leaflet belongs to the previous model. Receiving documents does not verify that every document matches the installed product. Keep the model mismatch open until corrected.',
    precision_extra='Leo owns the leaflet follow-up and promises a Monday call. The separate cosmetic-trim review needs a return visit with no date booked. Monday is not a promised visit, repair completion, or change to warranty terms.',
    phrases='''Acknowledge receipt | You have received the handover pack for B1.
Identify the mismatch | The care leaflet belongs to the previous model.
Keep the document specific | We need the leaflet for the current model.
Avoid applying the wrong guidance | I cannot treat that leaflet as confirmed guidance for this model.
Name the correction | I will obtain the replacement care document.
Accept ownership | I will take responsibility for the leaflet follow-up.
Commit to communication | I will call you on Monday.
Separate the visit | The cosmetic-trim review needs a return visit.
State the booking limit | No return date is booked yet.
Correct the inference | Monday is the callback date, not a site appointment.
Keep both items visible | The leaflet and the trim visit are separate open items.
Avoid claiming completion | I cannot mark either item complete merely because we have discussed it.
Preserve the records | The service and warranty records retain their actual terms.
Read back the handover | Pack received; leaflet mismatch open; Leo to call Monday.
Name the remaining arrangement | The return visit still needs scheduling.
Close with a clear commitment | I will update you without promising an unconfirmed outcome.''',
    notes='''Received versus correct | Document delivery and document accuracy are different facts.
For the current model | Links care information to the actual product.
Will call | Commits to communication, not to completing all outstanding work.
Not yet booked | Describes the appointment status without inventing a date.
Separate open items | Prevents one follow-up action from hiding another.
Without promising | Preserves a useful commitment while limiting unsupported outcomes.''',
    d='''Which handover summary is accurate? | Pack received; wrong-model leaflet pending replacement; Leo calls Monday; trim visit unbooked | All documents verified and all work complete | Return visit confirmed for Monday | Warranty extended automatically until a visit | The summary preserves receipt, document correction, ownership, callback, and unbooked visit.
What would turn the callback into an unsupported promise? | Telling Maya the team will attend on Monday | Confirming Leo will call Monday | Recording the leaflet mismatch | Keeping the trim review on the open-item list | The promise concerns a call; no return appointment has been booked.
Which action best handles the leaflet mismatch? | Obtain the document for the current model | Assume similar products use identical guidance | Treat delivery as verification | Replace the model identifier by guesswork | The correct model-specific document is needed rather than an assumed equivalent.
What is not changed by this conversation? | The actual warranty terms | The need to correct the leaflet | Leo's follow-up ownership | The record of the Monday call | A follow-up conversation does not itself revise the applicable warranty terms.''',
    dialogue='''Maya | I have received the pack for B1, but this care leaflet appears to be for the old basin model. Can we check that before handover is closed?
Leo | Yes. There is a [[model mismatch::Model mismatch identifies the leaflet's previous-model reference rather than denying receipt of the pack.]] in that leaflet. The pack has been delivered, but we should not treat the wrong document as confirmed guidance for the current model.
Maya | I do not want to assume the instructions are identical just because the two basins look similar. I would prefer the actual document for this one.
Leo | That is the right distinction. I will obtain the [[replacement document::Replacement document is the correct model-specific leaflet needed to resolve the mismatch.]] for the current model rather than ask you to rely on an unverified equivalent.
Maya | Who should I contact if the new leaflet has not arrived? It would help to have one named person responsible for that item.
Leo | I will be the [[follow-up owner::Follow-up owner names Leo as the person responsible for progressing the leaflet correction.]] for the leaflet. Please record me against it, and I will call you on Monday with an update.
Maya | Thank you. There is also the cosmetic trim that needs review. Does Monday mean someone will return to look at that as well?
Leo | No. Monday is the [[update date::Update date is the promised communication date, not an appointment for the separate trim review.]]. The cosmetic-trim review needs a return visit, but we do not have a date booked for that attendance.
Maya | I had nearly put Monday into our site calendar as a visit. I will leave it as a call instead and keep the visit separate.
Leo | Please do. A [[callback::Callback means the promised phone communication and does not establish site attendance.]] is not a site appointment. I can commit to the Monday call without pretending the return visit has already been arranged.
Maya | In the handover notes, should I list the leaflet and trim together as one general outstanding item, or give them separate entries?
Leo | Give them separate entries on the [[open-item list::Open-item list should retain the document correction and visit arrangement as distinct unfinished matters.]]. One concerns the correct document; the other concerns a review requiring further attendance. Combining them could hide an unfinished action.
Maya | That makes sense. Receiving the pack is one completed step, but it does not mean the incorrect leaflet has somehow been accepted as right.
Leo | Exactly. [[Document receipt::Document receipt acknowledges delivery without verifying the accuracy or suitability of each enclosed record.]] and document accuracy are different. We can acknowledge delivery while keeping the care-leaflet mismatch open until the proper document is supplied.
Maya | I also do not want the note to say the trim has been corrected merely because we have agreed that someone should review it.
Leo | Agreed. That would be an unsupported [[completion claim::Completion claim would wrongly describe the trim as corrected when only a future review is required.]]. The review remains outstanding, and there is no return date to report yet.
Maya | Will anything about this follow-up change the warranty record, or should I keep the actual terms in the documents separate from these arrangements?
Leo | Keep the [[warranty record::Warranty record retains its actual terms; the callback and open items do not automatically revise them.]] and its actual terms. This conversation assigns follow-up and clarifies scheduling; it does not create a new warranty promise.
Maya | Let me summarize: pack received, care leaflet for the wrong model, Leo owns its replacement and calls Monday. Trim review needs a return visit with no date booked.
Leo | That [[handover readback::Handover readback preserves received records, open corrections, ownership, and the distinction between call and visit.]] is accurate. It lets us finish this discussion with clear responsibilities while keeping the remaining work visible, rather than describing the whole handover as complete.''',
    transfer_title='Keep the call and visit separate',
    transfer_setup='Complete the closing exchange. Identify the model mismatch, named owner, call date, and unbooked return attendance.',
    transfer='''Client: "The leaflet belongs to the ___ model." | previous | Previous identifies why the supplied leaflet does not match the current product.
Lead: "___ owns the replacement-leaflet follow-up." | Leo | Leo explicitly accepts responsibility for obtaining the correct care leaflet.
Client: "The promised call is on ___." | Monday | Monday is the communication commitment rather than the return-visit date.
Lead: "The return visit is not yet ___." | booked | The cosmetic-trim review requires attendance, but no appointment date is confirmed.'''
))
