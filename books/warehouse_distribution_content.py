"""Original Warehouse and Distribution learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='warehouse-distribution',
    title='Warehouse and Distribution English',
    cover_label='ENGLISH FOR RECEIVING, STOCK, AND DISPATCH',
    cover_title='Warehouse\nand Distribution',
    cover_size=35,
    tagline='Exact quantities. Clear status.',
    audience='For receiving clerks, pickers, packers, inventory staff, returns teams, and distribution supervisors.',
    map_intro='Eight warehouse conversations: flag an inbound overage, resolve conflicting item labels, confirm each-versus-case quantities, report a short pick, pause a label mismatch, reconcile a dispatch manifest, route a return review, and hand over a verified count difference.',
    notes_title='The item, the unit, and the status.',
    notes_intro='Warehouse English connects physical goods to records without confusing the two. Useful messages identify the exact item and location, state quantities with their units, and make clear whether goods are merely present, available, approved, staged, or actually dispatched.',
    field_notes=[
        ('Keep the unit beside the number', 'Six each and six cases can describe very different quantities. Confirm the product-specific pack size before making a conversion; do not assume that all cartons or cases contain the same number.', '"Six trays are requested; this item has six trays per case, so that is one case."'),
        ('Read the item, not just the location', 'A bin sign can conflict with the label on the stock. Report both identifiers and the location rather than treating a familiar bin as proof that the product is correct.', '"A12 is marked BK-14-B, but the stock label reads BK-14-G."'),
        ('Separate presence from availability', 'Stock shown in reserve may be allocated or otherwise unavailable. Staged cartons may still be missing from dispatch records. Name the uncompleted check before promising a full order or a departure.', '"Four are at the pick face; the twelve shown in reserve still need an availability check."'),
        ('Distinguish a count from permission to change it', 'An agreed recount can establish an observed quantity without establishing the cause of a difference or authorizing an adjustment. Transfer the figures, completed checks, and next owner together.', '"Both counts give eighteen; the system shows twenty. Sam owns the transaction review."'),
    ],
    scope_note='All orders, goods, locations, quantities, workers, times, and decisions are fictional. This book teaches workplace English, not equipment operation, manual handling, warehouse-system configuration, product-safety inspection, or inventory authorization. Follow actual site procedures, training, safety controls, product requirements, and approval limits. The dialogues do not authorize stock movement, relabeling, release for sale, shipment, or record adjustment. Do not enter restricted areas or operate equipment based on a language exercise.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Material Recording Clerks.',
             url='https://www.bls.gov/ooh/office-and-administrative-support/material-recording-clerks.htm',
             note='Occupational context for shipment records, package checks, stock information, and inventory discrepancies. All teaching cases and conversations are original and fictional.', checked='1 October 2026'),
        dict(title='Microsoft Learn. Unit of Measure and Stocking Policies.',
             url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/unit-measure-stocking-policies',
             note='Terminology background for product-specific relationships between individual units, boxes, and pallets. The book does not teach Microsoft system setup or prescribe a universal pack size.', checked='1 October 2026'),
        dict(title='Microsoft Learn. Cycle Counting.',
             url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting',
             note='Context for distinguishing physical inventory counts from review of differences. Fictional approval limits and handoffs are not instructions for operating a particular warehouse system.', checked='1 October 2026'),
        dict(title='Occupational Safety and Health Administration. Warehousing: Hazards and Solutions.',
             url='https://www.osha.gov/warehousing/hazards-solutions',
             note='Safety context for separating communication practice from actual site training, equipment use, and handling procedures. The dialogues do not provide operational safety certification.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Receiving against the expected shipment',
    scene='Two cartons over the order',
    skill='Report an inbound overage with matching item labels while preserving the original order and the limit of your authority.',
    brief='Receiving clerk Nia checks a shipment against purchase order 740, which expects twenty cartons. The physical count is twenty-two cartons, and the item labels match the ordered item. The supplier has not explained the additional two cartons. Nia can flag the overage to inventory coordinator Ben, but neither can treat this conversation as approval to change the order. Matching item labels do not settle quantity acceptance, payment, stock release, or the cause of the difference.',
    cast='Nia | Receiving clerk\nBen | Inventory coordinator',
    culture=('A matching item can still have a quantity exception', 'Positive wording such as the labels match is useful, but it must not conceal an overage. Give the expected and observed counts in one message. Report what needs review without making the record agree by quietly changing the order quantity.'),
    a='''What does purchase order 740 expect? | Twenty cartons | Twenty-two cartons | Two cartons | Twenty individual products | The purchase order specifies twenty cartons, which remains the comparison basis.
What does receiving count? | Twenty-two cartons with matching item labels | Twenty cartons with wrong labels | Two cartons with no labels | Twenty-two verified individual products | Receiving observes twenty-two cartons whose item labels match the ordered item.
What has not been established? | Why two extra cartons arrived or whether an order change is approved | The original expected count | The physical carton count | The matching item labels | The supplier has not explained the extras, and no order amendment is approved.''',
    vocabulary='''purchase order | Buyer document specifying ordered goods and quantities, often PO. | check the purchase order
inbound shipment | Goods arriving at a warehouse or receiving location. | identify the inbound shipment
expected quantity | Amount required by the reference order or record. | state the expected quantity
received count | Number physically counted on arrival, distinct from approval status. | report the received count
overage | Quantity above the expected or ordered amount. | flag an overage
carton | Outer package used as the counting unit here. | count the cartons
item label | Label identifying the goods or product reference. | compare the item label
item match | Correspondence between the observed and ordered product identity. | confirm the item match
quantity exception | Difference requiring review against the stated quantity. | report a quantity exception
supplier | Business providing the ordered goods. | contact the supplier
receiving clerk | Worker checking and recording incoming shipments. | brief the receiving clerk
inventory coordinator | Person coordinating stock records and related checks. | notify the inventory coordinator
order line | Individual entry specifying an item and quantity on an order. | review the order line
packing slip | Supplier document describing the shipment contents. | compare the packing slip
delivery note | Document accompanying delivered goods and their descriptions. | check the delivery note
advance shipping notice | Electronic notice of expected shipment details, often ASN. | compare the advance shipping notice
quantity variance | Difference between expected and observed amounts. | quantify the quantity variance
supplier explanation | Supplier account of why a discrepancy occurred. | await the supplier explanation
order amendment | Authorized change to an existing purchase order. | request an order amendment
approval limit | Boundary of a person's authority to accept or change something. | respect the approval limit
acceptance status | Whether the goods or quantity have been accepted under the process. | clarify acceptance status
stock release | Authorization to make goods available for the relevant use. | distinguish stock release
invoice quantity | Number of units billed by the supplier. | verify the invoice quantity
reconciliation | Comparison of records and actual figures to explain differences. | begin quantity reconciliation''',
    precision='The expected count is twenty cartons and the observed count is twenty-two: an overage of two cartons. Matching item labels support product identity, not approval of the additional quantity or a change to purchase order 740.',
    precision_extra='Physical presence, receipt recording, quantity acceptance, payment, and stock release can be separate stages. Use the actual process and authority limits. Reporting an overage must not erase the original order or invent the reason for the additional cartons.',
    phrases='''Identify the order | I am checking the shipment against purchase order 740.\nState the expectation | The order expects twenty cartons.\nState the count | I have counted twenty-two cartons.\nQuantify the excess | That is an overage of two cartons.\nConfirm the item match | The item labels match the ordered item.\nSeparate item and quantity | Matching labels do not resolve the quantity difference.\nKeep the cause open | The supplier has not explained the additional two.\nAvoid an assumption | I cannot call the extra cartons a free addition.\nFlag the exception | I will report the overage for review.\nPreserve the original figure | Keep twenty as the original ordered quantity.\nState the authority limit | I cannot approve an order change.\nAvoid a false amendment | The order has not been changed to twenty-two.\nDistinguish payment | This count does not approve payment for the extras.\nDistinguish release | The count alone does not authorize stock release.\nRead back both figures | Twenty expected, twenty-two counted, item labels matching.\nClose with the open question | The extra quantity still needs an explanation and a decision.''',
    notes='''Over versus short | Over identifies excess quantity; short identifies a deficit.\nAgainst | Names the order used as the basis of comparison.\nMatching | Can describe product identity without describing quantity approval.\nAdditional | Refers to the two beyond the original twenty.\nCounted versus accepted | Physical observation is different from approval under the receiving process.\nHas not explained | Leaves the cause unknown without accusing the supplier of deliberate action.''',
    d='''Which report includes all checked facts? | PO 740 expects twenty; twenty-two counted; item labels match. | PO 740 now orders twenty-two because they arrived. | Two cartons arrived and all others are missing. | Matching labels prove the supplier intended a free bonus. | The correct report preserves the expected count, observed count, and item-label match.
Which figure describes the variance? | Two cartons over the order. | Two cartons short of the order. | Twenty-two cartons over the order. | No difference because labels match. | Twenty-two observed minus twenty expected gives an excess of two cartons.
Which action exceeds Nia's authority? | Approving the order change to twenty-two. | Flagging the extra quantity. | Stating that labels match. | Asking for a supplier explanation. | The brief explicitly denies authority to approve an order amendment.
Which conclusion does not follow from the labels? | The additional quantity is approved for payment and release. | The observed labels match the ordered item. | Quantity review is still needed. | The original order remains twenty cartons. | Identity information alone establishes neither payment approval nor stock-release permission.''',
    dialogue='''Nia | Ben, I have a quantity exception on purchase order 740. The order expects twenty cartons, but I have counted twenty-two at receiving.
Ben | That is an [[overage::Overage describes the two-carton excess above the twenty cartons expected on purchase order 740.]] of two cartons. Before we ask about the additional quantity, do the item labels match what the order actually names?
Nia | Yes, the labels match the ordered item. The problem is the number of cartons, not a different product reference on the labels.
Ben | Keep that [[item match::Item match concerns product identity; it does not settle whether the additional quantity was ordered or approved.]] in the report, but do not let it hide the quantity exception. We need both facts together.
Nia | Has the supplier explained why there are two extra? I do not want to assume they are free stock or part of an approved change.
Ben | No [[supplier explanation::Supplier explanation is absent, so the reason for the two extra cartons remains unknown.]] has been received. We should not describe the extras as a bonus, replacement stock, or an agreed increase without evidence.
Nia | Then I will flag twenty expected and twenty-two counted. Should the original order stay at twenty while that question is reviewed?
Ben | Yes. The [[expected quantity::Expected quantity remains twenty cartons, preserving the original comparison basis rather than changing it to match arrival.]] is still twenty. Changing the order to fit the arrival would conceal the difference we need to resolve.
Nia | I can report the count, but I cannot approve an order amendment. I want that limit clear before someone treats my entry as approval.
Ben | That [[approval limit::Approval limit prevents the receiving clerk's count from being treated as authority to alter the purchase order.]] matters. This conversation does not authorize you to increase the purchase order or decide what should happen to the additional cartons.
Nia | Good. I also want to avoid saying that we received twenty-two and leaving everyone to infer that we accepted and paid for all twenty-two.
Ben | State the [[received count::Received count here means twenty-two physically counted cartons, not automatic quantity acceptance or payment approval.]] as a physical count, with acceptance unresolved. If a local status label means something more, use the actual receiving process carefully.
Nia | So the report should not suggest that matching labels authorize the extra quantity for use, either. The cartons are here, but that is a separate issue.
Ben | Correct. [[Stock release::Stock release is a separate authorization; matching item labels and physical presence do not supply it.]] is not established by the count alone. We are documenting the discrepancy and routing it for the appropriate decision.
Nia | Let me read back the message: purchase order 740 expects twenty cartons, twenty-two are present, and their item labels match the ordered product.
Ben | Add that the [[quantity variance::Quantity variance is the two-carton excess, whose cause and treatment still require review.]] is two cartons over, with no supplier explanation yet. That gives the next person a precise question to follow up.
Nia | I will include that. No change to the ordered quantity, no claim that the extras are free, and no payment or release approval.
Ben | Exactly. An [[order amendment::Order amendment would require authorization that has not been given; reporting the overage is not that approval.]] has not been approved. We can keep the original order visible while the additional quantity is reviewed.
Nia | That is clear. I will flag the overage to you with both counts and the matching-label detail, rather than just saying the delivery looks fine.
Ben | Thank you. That starts the [[reconciliation::Reconciliation compares the order and physical count to resolve the difference without inventing its cause or outcome.]] with reliable facts. The extra two cartons still need an explanation and an authorized decision.''',
    transfer_title='Flag another inbound overage',
    transfer_setup='Purchase order 851 expects twelve cartons. Receiving counts fifteen with matching item labels. The extra quantity is unexplained, and the clerk cannot approve an order change.',
    transfer='''Clerk: "The order expects ___ cartons." | twelve | Twelve is the unchanged purchase-order quantity used as the reference.
Coordinator: "The physical count is ___ cartons." | fifteen | Fifteen is the actual observed count at receiving in this scenario.
Clerk: "That is an overage of ___ cartons." | three | Fifteen minus twelve gives three cartons above the ordered amount.
Coordinator: "An order amendment is not ___." | approved | No authorized change has been granted by counting or reporting the extra cartons.''',
))


BOOK['units'].append(unit(
    title='Locating and identifying stock',
    scene='The bin sign and stock disagree',
    skill='Read back similar item codes, distinguish location labels from product labels, and request a record check without substituting stock.',
    brief='Picker Luis needs BK-14-B, blue folders, from bin A12. The bin sign names BK-14-B, but the stock in the bin is labelled BK-14-G, green folders. Inventory clerk Mei can check the putaway record. No stock move, bin-sign change, or substitution has been approved. The location mismatch does not prove why the green folders are there or establish where the blue folders are. Luis needs to report both complete codes and the location without picking the wrong color.',
    cast='Luis | Picker\nMei | Inventory clerk',
    culture=('Say the part of the code that differs', 'Similar product codes can sound identical in a noisy warehouse. Repeat the full reference, then clarify the final letter in ordinary words. A confident location instruction should not override conflicting product information, and a discrepancy report should not become an accusation.'),
    a='''Which item is required? | BK-14-B, blue folders | BK-14-G, green folders | Either color of folder | Any stock in A12 | The pick requirement specifically identifies blue folders under BK-14-B.
What is actually labelled on the stock in A12? | BK-14-G, green folders | BK-14-B, blue folders | No item code at all | An approved substitute code | The stock labels identify green folders, conflicting with the bin sign.
What can Mei do next? | Check the putaway record | Approve a substitution automatically | Declare the blue folders lost | Move the green folders without authorization | The brief authorizes a record check, not a move or substitute pick.''',
    vocabulary='''item code | Identifier assigned to a product or variant. | read back the item code
stock-keeping unit | Internal identifier for a stock item or variant, often SKU. | verify the stock-keeping unit
product variant | Version of an item differing in a feature such as color. | distinguish the product variant
bin location | Identified storage position within the warehouse. | confirm the bin location
bin sign | Location display indicating assigned stock information. | compare the bin sign
stock label | Identifier attached to the actual goods or their packaging. | read the stock label
location mismatch | Conflict between assigned location information and observed stock. | report a location mismatch
putaway | Process of placing received goods in an assigned storage location. | check the putaway record
putaway record | Record of where goods were placed after receiving. | review the putaway record
location history | Record of stock movements involving a location. | examine the location history
item master | Central record of product information in the inventory system. | consult the item master
suffix | Final part of a code, here the letter B or G. | clarify the suffix
color variant | Product version distinguished by color. | confirm the color variant
look-alike code | Identifier visually similar to another code. | distinguish look-alike codes
read-back | Repetition of information to verify accuracy. | request a full read-back
substitution | Use of a different item in place of the requested one. | avoid an unapproved substitution
stock move | Transfer of goods between locations. | request approval for a stock move
relabeling | Changing an existing label under the proper process. | distinguish relabeling from checking
assigned location | Storage position shown for an item in the relevant record. | verify the assigned location
observed stock | Goods actually seen at the location. | describe the observed stock
picking error | Selection of an incorrect item or quantity. | prevent a picking error
location correction | Authorized change to inaccurate location information. | request a location correction
verification request | Request to check conflicting facts before proceeding. | raise a verification request
inventory clerk | Worker maintaining and checking stock records. | contact the inventory clerk''',
    precision='BK-14-B is the requested blue-folder item; BK-14-G is the green-folder item observed at A12. The bin sign and stock label conflict. Neither their similarity nor the shared location authorizes substituting the green folders.',
    precision_extra='The mismatch alone does not establish a bad putaway, a wrong sign, or a missing-blue-stock location. Read back both full codes and A12, then request the record check. Do not make an unapproved move or label change to force agreement.',
    phrases='''State the requirement | I need BK-14-B, blue folders.\nName the location | I am checking bin A12.\nRead the sign | The bin sign says BK-14-B.\nRead the stock | The stock label says BK-14-G.\nClarify the differing letter | B as in blue, not G as in green.\nReport the conflict | The sign and the actual stock label disagree.\nAvoid a substitution | Green folders are not the requested item.\nAsk for the record | Can you check the putaway record?\nKeep the cause unknown | I do not yet know why the green folders are here.\nKeep location unknown | We have not established where the blue folders are.\nAvoid a false correction | No bin-sign change has been approved.\nAvoid an unapproved move | I will not move the stock based on a guess.\nPreserve both codes | Please keep BK-14-B and BK-14-G separate in the note.\nConfirm the next owner | I will check the record for A12.\nDistinguish checking and approval | A record check is not permission to substitute.\nClose the clarification | The item mismatch remains open pending verification.''',
    notes='''B as in blue | Clarifies the code suffix using the relevant product color.\nSays versus contains | The sign's wording and the location's physical contents are separate observations.\nAssigned versus observed | A recorded location assignment is not proof of the goods currently present.\nSimilar versus identical | A one-letter difference can identify a different product variant.\nWhy versus where | The cause of the mismatch and the location of the correct stock are separate questions.\nCheck versus change | Looking at a record does not authorize a stock move or label amendment.''',
    d='''Which message is precise? | A12 sign says BK-14-B; stock says BK-14-G. | A12 has the right item because the sign says so. | The two codes mean the same thing. | The blue folders are definitely in the next bin. | The precise message preserves both conflicting identifiers and the relevant location.
Which clarification targets the code difference? | B as in blue, not G as in green. | Just take whichever ends in a letter. | Both begin BK, so they match. | Ignore the suffix when the location agrees. | The final letter distinguishes the requested blue variant from the observed green variant.
Which claim lacks evidence? | A specific worker put the stock away incorrectly. | The bin sign and stock label disagree. | Mei can check the putaway record. | No substitution is approved. | The observed mismatch does not identify a cause or responsible worker.
Which next step matches the authority supplied? | Mei checks the putaway record. | Luis silently substitutes green folders. | Luis changes the bin sign immediately. | Both codes are merged into one item. | The available next step is verification, not an unapproved movement or record change.''',
    dialogue='''Luis | Mei, I have a mismatch at A12. I need BK-14-B, the blue folders, but the stock label in the bin reads BK-14-G.
Mei | Let us separate the [[bin sign::Bin sign identifies the location's displayed assignment, which must be compared with the different stock label.]] from the stock label. What does the sign at A12 say, and what color are the folders you actually see?
Luis | The sign says BK-14-B. The stock is green folders labelled BK-14-G. The last letter differs, although the rest of the code looks alike.
Mei | Then the [[color variant::Color variant distinguishes blue folders from green folders; similarity of the other code characters does not make them interchangeable.]] is different. You need B as in blue, while the stock label has G as in green.
Luis | Correct. I have not picked the green folders as a replacement. I wanted the mismatch checked before treating this bin as the right stock.
Mei | Good. An unapproved [[substitution::Substitution would replace the requested blue folders with green ones, which this location mismatch does not authorize.]] would not resolve the issue. I can check the putaway record to see what information we have for A12.
Luis | Could the sign be wrong, or could the wrong folders have been put there? I do not have evidence to choose between those explanations.
Mei | The [[putaway record::Putaway record may help establish what was placed in A12; it must be checked rather than assumed to prove a cause.]] is a useful next check. We should not assign a cause simply because the sign and the goods disagree.
Luis | Please do not record the blue folders as missing from the whole warehouse. I only know that the stock I see here is green.
Mei | Agreed. This is a [[location mismatch::Location mismatch describes the observed conflict at A12 without establishing warehouse-wide absence or the correct item's location.]] at A12. We have not established where the blue folders are or why the green folders are in this bin.
Luis | I will keep the location in the message. A code alone might send someone to another aisle and leave the same problem here.
Mei | Include a complete [[read-back::Read-back repeats the two full item codes and the bin so the verification request cannot collapse them into one.]]: requested BK-14-B, sign BK-14-B, observed stock BK-14-G, location A12. That gives us the exact conflict.
Luis | That matches. Is there any approval to move the green folders or change the sign while you check the record?
Mei | No [[stock move::Stock move is a separate action requiring authorization; the record-checking conversation does not approve it.]] has been approved, and no sign change has been approved either. A check is not permission to make the records agree by changing something.
Luis | Understood. I will report what is there rather than trying to fix the location from memory. The codes are too similar to guess.
Mei | Yes. The [[suffix::Suffix is the final B or G, the small code difference that identifies different folder colors.]] matters even when the rest of the code is identical. A familiar-looking reference is not enough to confirm the requested variant.
Luis | So you will review the record, and the pick remains unresolved until the correct stock information is verified. No green-folder replacement is agreed.
Mei | Correct. I own the [[verification request::Verification request assigns the record check while leaving the stock identity conflict and pick unresolved.]]. I will check the putaway information without claiming that it has already located the blue folders.
Luis | Let me repeat the essential point: A12 is signed for blue BK-14-B, but its observed stock is green BK-14-G.
Mei | Exactly. Keep the [[observed stock::Observed stock is the green BK-14-G actually seen, distinct from the bin's assigned blue-item description.]] distinct from the assigned location information. No substitution, move, or relabeling is approved by this discussion.''',
    transfer_title='Clarify a different variant mismatch',
    transfer_setup='Bin C08 is signed for BX-20-R, red binders. The stock label reads BX-20-Y, yellow binders. Red is requested. Jo can check the putaway record; no move or substitution is approved.',
    transfer='''Picker: "The requested item is ___." | BX-20-R | BX-20-R identifies the requested red binders, not the yellow variant.
Clerk: "The observed stock label is ___." | BX-20-Y | BX-20-Y is the label on the yellow binders physically present.
Picker: "The conflicting location is ___." | C08 | C08 is the specific bin where the sign and stock disagree.
Clerk: "No substitution is ___." | approved | The mismatch does not authorize replacing red binders with yellow ones.''',
))


BOOK['units'].append(unit(
    title='Picking the right unit and quantity',
    scene='Six each is not six cases',
    skill='Resolve a unit-of-measure misunderstanding, calculate the product-specific case equivalent, and confirm the requested total.',
    brief='Pick ticket S18 requests six each of a storage tray. For this item, one standard case contains six trays. Coworker Omar initially reads the request as six cases, which would contain thirty-six trays. Picker Asha clarifies that the requested six individual trays equal one standard case of this item. The correction does not establish the pack size of any other product, authorize a different quantity, or confirm that picking and dispatch have already been completed.',
    cast='Omar | Warehouse coworker\nAsha | Picker',
    culture=('Correct the unit before debating the number', 'Two coworkers can agree that the number is six and still prepare different quantities. State the unit attached to the order, the units per case for this item, and the resulting total. Make the correction about the shared record rather than the other person being careless.'),
    a='''What does S18 request? | Six individual trays | Six cases of trays | Thirty-six trays | One individual tray | Six each means six individual trays, not six full cases.
What is the stated pack size for this item? | Six trays per standard case | One tray per case | Six cases per tray | Thirty-six trays per case | The briefing defines one standard case as containing six trays for this item.
How many standard cases equal the requested quantity? | One | Six | Thirty-six | Twelve | Six requested trays divided by six trays per case equals one case.''',
    vocabulary='''pick ticket | Record specifying items and quantities to select for an order. | read the pick ticket
unit of measure | Defined basis for expressing a quantity, often UOM. | confirm the unit of measure
each | Counting unit meaning one individual item. | order six each
case | Grouped package containing the stated number of items. | verify the case quantity
case pack | Number of individual items in one standard case. | confirm the case pack
pack size | Quantity contained in a particular packaged unit. | check the pack size
individual unit | One item counted separately from grouped packaging. | count individual units
requested quantity | Amount specified by the order or picking instruction. | preserve the requested quantity
case equivalent | Number of cases corresponding to a stated item quantity. | calculate the case equivalent
conversion factor | Numeric relationship used to convert one unit to another. | verify the conversion factor
per case | For each single case. | state six trays per case
total units | Complete number of individual items represented. | calculate the total units
overpick | Selection of more units than requested. | prevent an overpick
underpick | Selection of fewer units than requested. | identify an underpick
full-case pick | Selection of a complete case under the picking process. | distinguish a full-case pick
each pick | Selection measured in individual units rather than cases. | clarify an each pick
inner pack | Smaller grouped package within a larger case, where used. | distinguish an inner pack
outer case | Larger package containing individual items or inner packs. | identify the outer case
product-specific conversion | Unit relationship that applies to the particular item. | use a product-specific conversion
order unit | Unit in which the order quantity is stated. | confirm the order unit
stocking unit | Unit used to record inventory for the relevant item. | check the stocking unit
quantity read-back | Repetition of both number and unit to verify accuracy. | give a quantity read-back
pick confirmation | Record that the actual required picking work has been completed. | distinguish pick confirmation
quantity correction | Amendment of an incorrect interpretation or recorded quantity. | explain the quantity correction''',
    precision='S18 requests six each, meaning six individual trays. Six trays per case makes that one case equivalent. Six cases would be thirty-six trays: thirty more than requested. The conversion applies only to this stated item and pack size.',
    precision_extra='Equivalent quantities do not by themselves establish a completed pick or authorize a particular handling method. Follow the actual order and picking process. For another item, check its unit definitions and pack size again rather than reusing six per case.',
    phrases='''Name the ticket | Let us check pick ticket S18.\nRead number and unit | It requests six each.\nExpand each | That means six individual trays.\nState the pack size | This item has six trays per standard case.\nCalculate the equivalent | Six divided by six gives one case.\nCorrect the misunderstanding | Six cases would be thirty-six trays.\nQuantify the overpick | That would be thirty trays more than requested.\nPreserve the order | The requested total remains six trays.\nLimit the conversion | This pack size applies to this item.\nAvoid a universal assumption | We must check the pack size for other products separately.\nAsk for a read-back | Please repeat both the number and the unit.\nDistinguish packaging | An outer case is not the same as one individual item.\nConfirm the agreed interpretation | One standard case contains the six requested trays.\nSeparate calculation and completion | We have clarified the quantity, not confirmed the pick.\nAvoid changing the order | The ticket has not been increased to six cases.\nClose the correction | S18 is six trays in total, equivalent to one case for this item.''',
    notes='''Each | Functions as a unit and cannot be silently replaced with cases.\nPer | States a ratio: six trays for one case.\nSix divided by six | Converts requested individual units into the stated case equivalent.\nSix times six | Calculates the mistaken six-case total of thirty-six trays.\nThis item | Limits the conversion and prevents an unsupported rule for other products.\nEquivalent versus completed | Correct arithmetic does not record that any picking work has occurred.''',
    d='''Which read-back is correct? | Six trays total, equivalent to one standard case of this item. | Six cases total, because the ticket says six. | One tray total, because one case is mentioned. | Thirty-six cases, because both numbers are six. | Six each divided by the six-tray case pack gives one case and six trays total.
How many trays would six cases contain? | Thirty-six | Six | Twelve | One | Six cases multiplied by six trays per case gives thirty-six trays.
How many excess trays would the mistaken six-case pick contain? | Thirty | Six | Thirty-six | Five | Thirty-six trays minus the six requested trays gives thirty excess trays.
Which statement wrongly generalizes the pack size? | Every product in the warehouse has six units per case. | This item has six trays per case. | Another item's case pack needs checking. | S18 requests six individual trays. | The supplied conversion applies to this tray item, not every warehouse product.''',
    dialogue='''Omar | I have S18 here. It says six for the storage trays, so I was preparing to treat that as six cases. Can you confirm?
Asha | Let us read the [[unit of measure::Unit of measure determines what six counts; the ticket specifies individual units rather than cases.]] beside the number. The ticket says six each, which means six individual trays rather than six cases.
Omar | I missed the each part. I saw six and assumed the case was the unit. How many trays are in a standard case of this item?
Asha | The [[case pack::Case pack is six trays in one standard case for this particular item.]] is six trays. That is the stated pack size for this tray item, so one case contains six individual units.
Omar | Then the requested six trays equal one case, not six cases. I want to make sure I have the conversion the right way around.
Asha | Yes. The [[case equivalent::Case equivalent is one case, calculated by dividing six requested trays by six trays per case.]] is one: six requested trays divided by six trays per case. The required total stays at six trays.
Omar | If I had used six cases, I would have multiplied six cases by six trays. That would have given thirty-six trays in total.
Asha | Correct. Those [[total units::Total units for six cases would be thirty-six, which exceeds the requested six individual trays.]] would be thirty-six, not six. The number on the ticket cannot be interpreted without its accompanying unit.
Omar | And thirty-six is thirty more than the order asks for. It is a much bigger difference than simply using a different word on the ticket.
Asha | That would be an [[overpick::Overpick means selecting more than requested; the mistaken six-case interpretation would add thirty excess trays.]] of thirty trays. Clarifying the unit now prevents the wrong quantity from being treated as the intended order.
Omar | Does this mean each always corresponds to one sixth of a case in our warehouse, or only for this tray product?
Asha | Only this [[product-specific conversion::Product-specific conversion applies the stated six-tray case pack to this item, not all warehouse products.]] is supplied. Other products can have different pack sizes, so you must check their actual unit relationships separately.
Omar | Understood. I should not carry the six-per-case assumption over to a different tray style or another product just because its packaging looks similar.
Asha | Exactly. Confirm the [[pack size::Pack size is the verified number in the relevant package, which cannot be inferred from similar appearance.]] for the actual item. Similar boxes do not establish identical quantities inside them.
Omar | Let me read it back: S18 requests six individual storage trays. This product has six per case, giving one standard case equivalent.
Asha | That [[quantity read-back::Quantity read-back repeats both the requested six individual trays and the one-case equivalent to prevent renewed ambiguity.]] is correct. Keep both the total and the unit in the message, rather than just saying take one or take six.
Omar | We have clarified the quantity, but we have not said that the picking work or dispatch has already been completed. Is that distinction important here?
Asha | Yes. [[Pick confirmation::Pick confirmation would record completed picking; resolving the arithmetic does not establish that the work has occurred.]] belongs to the actual completion process. Our calculation is not evidence that the goods have been picked, packed, or sent.
Omar | Good. I will correct my interpretation of the ticket without describing it as a new order for six cases.
Asha | Right. The [[requested quantity::Requested quantity remains the original six trays; the correction fixes interpretation rather than increasing the order.]] has not changed. S18 is six trays total, equivalent to one standard case of this particular item.''',
    transfer_title='Convert a different pack size',
    transfer_setup='Pick ticket T29 requests twelve each of a folder. This item has four folders per standard case. A coworker misreads the request as twelve cases. No picking work has yet been confirmed.',
    transfer='''Picker: "The order requests twelve individual ___." | folders | Each refers to individual folders, not full cases of folders.
Coworker: "There are ___ folders per case." | four | Four is the stated product-specific pack size in this new scenario.
Picker: "The correct case equivalent is ___." | three | Twelve requested folders divided by four folders per case equals three cases.
Coworker: "Twelve cases would contain ___ folders." | forty-eight | Twelve cases multiplied by four folders per case would produce forty-eight folders.''',
))


BOOK['units'].append(unit(
    title='Reporting a short pick and replenishment need',
    scene='Reserve stock is not a delivery promise',
    skill='Quantify a pick-face shortfall, distinguish system reserve stock from available stock, and escalate against a stated cutoff.',
    brief='Order D55 requires ten baskets, but picker Elena finds four at pick face B04. The system lists twelve baskets in reserve. Their allocation, availability, and replenishment timing have not been checked. Replenishment clerk Dev can review the situation. The order cutoff is 15:00, but no promise to complete the order by then is supported. Elena must report the six-basket shortfall without declaring a warehouse-wide stockout or assuming the reserve quantity is already available to D55.',
    cast='Elena | Picker\nDev | Replenishment clerk',
    culture=('Give the shortage and the possible source separately', 'Saying we have twelve in reserve can sound like a promise that the order is covered. Pair the system quantity with the checks still needed. A useful escalation includes the required quantity, current pick-face quantity, location, order reference, and cutoff.'),
    a='''How many baskets does D55 require? | Ten | Four | Twelve | Six | Ten is the order requirement against which the pick-face quantity is compared.
What is the shortfall at B04? | Six baskets | Four baskets | Twelve baskets | Two baskets | Ten needed minus four present at the pick face gives six baskets short.
What is known about the twelve in reserve? | They are listed in the system; allocation and availability are unchecked | They are all available for D55 | They have already replenished B04 | They guarantee completion by 15:00 | The system figure alone does not establish allocation, availability, or replenishment timing.''',
    vocabulary='''pick face | Location from which items are normally selected for orders. | check the pick face
reserve stock | Stock recorded in a storage area used to support picking needs. | check reserve stock
replenishment | Supplying stock to a picking location from another source. | request replenishment
short pick | Picking shortfall against the requested quantity. | report a short pick
order requirement | Quantity or specification needed to fulfill an order. | state the order requirement
pick-face quantity | Number of units currently present at the picking location. | confirm the pick-face quantity
shortfall | Amount needed beyond what is currently present. | quantify the shortfall
system quantity | Amount shown in the inventory system. | distinguish system quantity
allocation | Assignment of stock to a particular order or demand. | check stock allocation
reservation | Earmarking of inventory under the actual system process. | verify a stock reservation
available stock | Stock that is actually usable for the relevant demand under the process. | confirm available stock
on-hand balance | Recorded quantity held, not automatically free for a particular order. | examine the on-hand balance
replenishment request | Request to review or supply stock for a picking location. | raise a replenishment request
replenishment task | Assigned work to move stock to the required location. | confirm the replenishment task
release status | Whether stock is authorized for the relevant use. | check release status
stockout | Absence of available stock at the relevant scope. | avoid an unsupported stockout claim
location shortfall | Insufficient quantity at a specified location. | report the location shortfall
order cutoff | Latest stated time relevant to processing the order. | state the order cutoff
fulfillment commitment | Promise to supply the required order under stated conditions. | avoid an unsupported fulfillment commitment
timing estimate | Provisional expectation for when work may be completed. | request a timing estimate
demand | Quantity needed by orders or other requirements. | review competing demand
priority review | Assessment of how a task should be handled relative to others. | request a priority review
availability check | Verification of stock usable for the specific requirement. | complete an availability check
replenishment desk | Team or contact coordinating pick-location stock supply. | contact the replenishment desk''',
    precision='D55 needs ten baskets and B04 has four, so the location is six short. Twelve shown in reserve is a possible source to investigate, not proof that six can be allocated and replenished in time for 15:00.',
    precision_extra='On-hand, reserved, allocated, released, and available may describe different inventory states. Use the actual system definitions. A short pick at one location does not prove a warehouse-wide stockout, and a replenishment request does not prove movement has occurred.',
    phrases='''Identify the demand | D55 needs ten baskets.\nName the location | The pick face is B04.\nState the observed quantity | There are four baskets at B04.\nCalculate the shortfall | We are six short at the pick face.\nState the system figure | The system lists twelve in reserve.\nPreserve the uncertainty | Allocation and availability have not been checked.\nAvoid promising the reserve | I cannot say those twelve are free for D55.\nAsk for review | Can the replenishment desk review the requirement?\nKeep the cutoff visible | The order cutoff is 15:00.\nAvoid a timing promise | We do not yet have a confirmed replenishment time.\nLimit the shortage claim | This is a B04 shortfall, not a confirmed warehouse-wide stockout.\nSeparate request and movement | The request does not mean the stock has moved.\nConfirm the needed amount | Six more baskets would meet the ten-basket requirement.\nPreserve the order reference | Keep the review attached to D55.\nAvoid automatic priority | The cutoff needs review, not an invented priority approval.\nClose with next checks | We need allocation, availability, and timing checked before promising fulfillment.''',
    notes='''Six short | Measures the gap between ten required and four present.\nShown in reserve | Reports a system figure without asserting physical or allocation verification.\nFree for | Informal wording for stock available to the specific order, not merely present.\nAt B04 | Limits the observed shortage to the named pick face.\nBy 15:00 | Is not promised merely because fifteen hundred is the cutoff.\nRequest raised | Indicates a next action, not a completed replenishment.''',
    d='''Which escalation contains the essential facts? | D55 needs ten; B04 has four; twelve shown in reserve are unchecked; cutoff 15:00. | Twelve in reserve guarantees the order. | The warehouse has no baskets anywhere. | B04 has ten because the order requires ten. | The complete message retains the demand, observed quantity, uncertain source, and cutoff.
How many additional baskets are needed at the pick face? | Six | Four | Ten | Twelve | Ten required minus four present leaves a six-basket shortfall.
Which claim is unsupported? | All twelve reserve baskets are available for D55. | Allocation needs checking. | Four baskets are at B04. | The cutoff is 15:00. | The reserve figure has not been checked for allocation or actual availability to this order.
What must happen before a supported completion promise? | Review stock allocation, availability, and replenishment timing. | Repeat the system total confidently. | Assume a request completes movement. | Remove the cutoff from the message. | Quantity in reserve alone does not establish usable stock or arrival at the pick face in time.''',
    dialogue='''Elena | Dev, D55 needs ten baskets, but I have only four at B04. I need to flag the shortfall before the 15:00 cutoff.
Dev | You are six short at the [[pick face::Pick face is B04, where four baskets are present against the order requirement of ten.]]. Does the system show any reserve stock for the same item, and has its availability been checked?
Elena | It lists twelve in reserve, but I have not checked allocation or availability. I do not want to say those twelve are free for this order.
Dev | Keep that distinction. The [[system quantity::System quantity is the twelve shown in reserve, not verified stock available to D55.]] is a possible source for review, not confirmation that the stock can be assigned and brought to B04.
Elena | So the message should say ten required, four at B04, six short, and twelve in reserve still needing checks. Is that enough to start?
Dev | Include the [[order cutoff::Order cutoff is fifteen hundred and must accompany the request without being turned into a completion promise.]] of 15:00 as well. That tells us why timing matters without claiming that replenishment can definitely meet it.
Elena | I will include D55 and the item details. I do not want the desk to replenish a similar basket while the correct order remains short.
Dev | Right. A [[replenishment request::Replenishment request starts review of supplying the correct stock to B04; it is not a completed movement.]] needs the exact demand and location. Raising it does not mean a replenishment task has already been completed.
Elena | Could some of the reserve stock already belong to another order? I have only the displayed total, not the information behind it.
Dev | That is why [[allocation::Allocation identifies stock assigned to particular demand and must be checked before assuming the reserve is free.]] needs checking. Twelve on the screen does not necessarily mean twelve uncommitted baskets for D55.
Elena | Understood. I should not tell packing that ten will definitely be ready, even though twelve sounds more than enough to cover six.
Dev | Correct. We need an [[availability check::Availability check establishes usable stock for the specific order rather than relying only on a reserve balance.]] for this requirement, followed by a realistic timing assessment. The arithmetic alone does not supply those results.
Elena | I also should not call this a warehouse-wide stockout. I have observed a shortage at B04, not checked every possible source.
Dev | Exactly. It is a [[location shortfall::Location shortfall limits the observed problem to B04 and avoids an unsupported claim about all warehouse stock.]] of six baskets. We should not expand that into a claim that no baskets are available anywhere in the warehouse.
Elena | If six more become available at B04, that would make ten and meet the quantity. But we still need the stock and timing confirmed.
Dev | Yes. Any [[timing estimate::Timing estimate remains to be established; neither the reserve quantity nor the cutoff supplies a replenishment completion time.]] must follow the actual review. No confirmed replenishment time has been supplied so far.
Elena | Can you take the review from here? I can give the exact order and location, while leaving the stock assignment and timing as open questions.
Dev | I can review it at the [[replenishment desk::Replenishment desk is the responsible review point, not a guarantee that stock has been allocated or moved.]]. Keep D55, ten required, four at B04, six short, twelve shown in reserve, and the 15:00 cutoff together.
Elena | That is the complete position. I will not tell anyone the reserve has moved or that the order is guaranteed before those checks happen.
Dev | Good. A [[fulfillment commitment::Fulfillment commitment would promise the order outcome, which remains unsupported until stock and timing checks are complete.]] still needs support. We are taking the next review step, with allocation, availability, and replenishment timing still unresolved.''',
    transfer_title='Report a different pick-face gap',
    transfer_setup='Order E66 needs fourteen bins. Pick face C05 has five. The system lists twenty in reserve, but allocation and availability are unchecked. The order cutoff is 16:30.',
    transfer='''Picker: "The pick face is short by ___ bins." | nine | Fourteen required minus five present creates a nine-bin shortfall.
Clerk: "The system lists ___ in reserve." | twenty | Twenty is the displayed reserve balance, not verified available stock.
Picker: "Allocation and availability remain ___." | unchecked | The reserve balance has not been assessed for this specific order.
Clerk: "The order cutoff is ___." | 16:30 | Sixteen thirty is the stated deadline, not a promised replenishment completion.''',
))


BOOK['units'].append(unit(
    title='Packing and label discrepancies',
    scene='The loose label belongs to another carton',
    skill='Interrupt a possible labeling error politely, compare carton and recipient references, and distinguish prevention from a completed error.',
    brief='At packing station 3, packer Rosa has cartons C70 and C71. The screen for C70 names Harbor Shop. A loose label beside C70 names Hillside School and refers to C71. No label has been applied. Quality colleague Arun asks Rosa to pause the label match while both carton references and recipients are checked. The conversation prevents an unverified label application; it does not establish a completed mislabeling, a shipment departure, or permission to relabel either carton from memory.',
    cast='Arun | Quality colleague\nRosa | Packer',
    culture=('Interrupt the action, not the person', 'A short, specific pause request works better than a vague warning or accusation. Name the conflicting carton and recipient details immediately. If the label has not been applied, preserve that fact rather than describing a mistake as already completed.'),
    a='''Who is named on the screen for C70? | Harbor Shop | Hillside School | Both recipients | No recipient | The C70 screen names Harbor Shop as its recipient.
Which carton does the loose Hillside School label reference? | C71 | C70 | Both C70 and C71 | An unknown unlisted carton | The loose label explicitly identifies C71, not the nearby C70.
What is the current labeling status? | No label has been applied | C70 has already been mislabeled | Both cartons have departed | Relabeling has been completed | The issue is caught before application, so completed-error wording is inaccurate.''',
    vocabulary='''packing station | Work area used to prepare goods and packaging for dispatch. | identify the packing station
carton reference | Identifier distinguishing one packed carton from another. | verify the carton reference
shipping label | Label carrying shipment-routing and identification information. | match the shipping label
loose label | Label not yet attached to a package. | check the loose label
recipient | Intended receiving person or organization. | confirm the recipient
screen record | Information displayed in the relevant system view. | compare the screen record
label match | Verification that a label belongs to the intended carton. | pause the label match
label application | Attaching a label to the intended package. | verify before label application
mislabeling | Applying incorrect identifying information to an item or carton. | prevent mislabeling
reference cross-check | Comparison of identifiers across items and records. | complete a reference cross-check
adjacent carton | Nearby carton that may belong to a different shipment. | distinguish the adjacent carton
workstation mix-up | Confusion between materials or records at one work area. | report a workstation mix-up
shipping address | Destination details on the shipment record. | confirm the shipping address
order association | Link between a carton and the relevant order. | verify the order association
tracking number | Identifier used to follow a particular shipment. | check the tracking number
barcode | Machine-readable representation used to identify records or items. | verify the barcode
human-readable text | Printed characters a person can read without decoding equipment. | compare human-readable text
label printout | Printed label output before or after verification. | inspect the label printout
label reprint | Another print of a label under the actual process. | authorize a label reprint
record selection | Choice of the system record currently being viewed or used. | check the record selection
unapplied | Not yet attached to the carton. | keep the label unapplied
verification pause | Temporary pause to resolve a specific uncertainty. | request a verification pause
prevention | Action that stops an error before it occurs. | distinguish prevention from correction
shipment departure | Actual movement of a shipment away from the facility. | confirm shipment departure''',
    precision='C70 corresponds to Harbor Shop on the screen. The loose Hillside School label references C71. Being physically beside C70 does not make it the correct label for C70. No label has yet been applied.',
    precision_extra='The necessary message identifies a potential mismatch and requests verification of both references. Do not describe it as a completed mislabeled shipment or guess a correction from the recipient names alone. Actual label production and application follow the site process.',
    phrases='''Request a precise pause | Please pause before applying that label.\nName the station | This is packing station 3.\nIdentify the screen | The C70 screen names Harbor Shop.\nIdentify the loose label | This label names Hillside School and references C71.\nState the mismatch | The carton reference and the loose label do not match.\nAvoid a proximity assumption | Being beside C70 does not make it the C70 label.\nCheck both cartons | Let us verify C70 and C71 separately.\nPreserve application status | No label has been applied yet.\nAvoid an accusation | I am flagging a possible mismatch before application.\nKeep recipients separate | Harbor Shop and Hillside School are different recipients.\nAsk for the full match | Check the carton reference and recipient together.\nAvoid a memory correction | Do not relabel from memory.\nDistinguish prevention and repair | This is a verification pause, not a completed relabeling.\nKeep departure separate | No shipment departure is established by this check.\nRead back the pairs | C70 with Harbor Shop; the loose C71 label with Hillside School.\nClose with the required check | Both carton-label associations need verification before application.''',
    notes='''Beside versus belongs to | Physical proximity does not establish record association.\nBefore applying | Places the intervention before an error is completed.\nYet | Preserves the fact that no label application has occurred.\nBoth | Calls for checking each reference rather than assuming the other carton is correct.\nPossible mismatch | Flags the risk without accusing someone of a completed mistake.\nRecipient and reference | The name alone is not a substitute for checking the identifier.''',
    d='''Which interruption is most precise? | Please pause: C70 names Harbor Shop, but this loose label names C71 and Hillside School. | You always label everything wrongly. | Something somewhere looks odd. | Apply it now because it is nearby. | The specific pause identifies both conflicting reference-recipient pairs before application.
Which status report is accurate? | No label has been applied; both references need checking. | C70 has already shipped with the wrong label. | Relabeling is complete. | Both recipients have received their cartons. | The discrepancy is detected before application and no shipment outcome is established.
What does the loose label's location prove? | Only that it is beside C70, not that it belongs to C70. | It must be the correct label for C70. | The C70 screen is necessarily wrong. | C71 has already departed. | Physical proximity alone does not establish which record or carton the label belongs to.
Which next step preserves accuracy? | Verify both carton references and recipient associations. | Swap labels from memory. | Merge the two recipients into one record. | Mark both cartons dispatched to clear the station. | The supplied next step is a reference cross-check, not an assumed correction or departure.''',
    dialogue='''Arun | Rosa, please pause before applying that loose label. The screen for C70 says Harbor Shop, but the label beside it says Hillside School.
Rosa | I have not applied it. Let me check the [[carton reference::Carton reference identifies which physical carton is being matched; the screen currently concerns C70.]] rather than assuming the label belongs here just because it is next to C70.
Arun | The loose label references C71. We have two cartons at station 3, so we need to keep the two recipient associations separate.
Rosa | I see it now. The [[loose label::Loose label remains unattached and identifies C71 for Hillside School, not the adjacent carton C70.]] says C71 and Hillside School. The C70 screen names Harbor Shop, which is a different recipient.
Arun | Exactly. I am not saying a carton has already been mislabeled. I am asking us to verify the match before any label is attached.
Rosa | That is a useful [[verification pause::Verification pause stops application while the specific conflict is checked, without claiming a completed labeling error.]]. No label has been applied yet, and I will not describe this as a completed error.
Arun | Please check both C70 and C71. If we only focus on the one nearest us, we could leave the other association unchecked.
Rosa | Agreed. The [[reference cross-check::Reference cross-check compares both carton identifiers and their recipient records rather than assuming one side is correct.]] should include both carton references and recipients. We should not swap anything from memory simply because the names look familiar.
Arun | Good. A label can be printed correctly for one carton and still be wrong for the carton beside it.
Rosa | Yes. Physical proximity does not establish the [[order association::Order association links a carton to its relevant order; being beside another carton does not create that link.]]. The label needs to match the relevant record, not merely the nearest package.
Arun | Could you read the details back before continuing the check? I want to be sure I have not mixed up the two references myself.
Rosa | C70 has Harbor Shop on its [[screen record::Screen record supplies the C70 recipient information, which must stay separate from the C71 label.]]. The loose label says C71 and Hillside School. Nothing has been applied to either carton in this discussion.
Arun | That is what I observed. We have a clear conflict to check, without needing to invent how the label ended up beside the other carton.
Rosa | Correct. A [[workstation mix-up::Workstation mix-up describes the confusing arrangement at the station without establishing who caused it or that goods shipped incorrectly.]] may be what we are preventing, but we have no basis to accuse a particular person or claim anything has shipped.
Arun | I appreciate that. The important thing is to interrupt the uncertain application and preserve the references for the actual verification process.
Rosa | We should distinguish [[prevention::Prevention catches the potential labeling error before application, unlike correcting a completed mislabeling.]] from repair. There is no completed mislabeling or relabeling to report here; there is an unapplied label and a mismatch.
Arun | Exactly. Once both associations are properly checked, any label handling needs to follow the normal process, not a guess based only on names.
Rosa | Yes. [[Label application::Label application is the action that remains to follow proper verification; it has not occurred in this conversation.]] has not happened. I will keep the check separate from any claim that the cartons are ready or have left.
Arun | Then our handoff is station 3, C70 Harbor Shop on the screen, loose C71 Hillside School label, and both references to be verified.
Rosa | That is accurate. No [[shipment departure::Shipment departure is a separate actual event and is not established by a label-match discussion at the packing station.]] is established here. We have paused the match before application and kept both carton-recipient pairs explicit.''',
    transfer_title='Pause another loose-label mismatch',
    transfer_setup='At station 5, the screen for carton D80 names Maple Clinic. A loose label beside it names Meadow Cafe and references D81. No label has been applied.',
    transfer='''Colleague: "The D80 screen names ___." | Maple Clinic | Maple Clinic is the recipient associated with D80 on the screen.
Packer: "The loose label references ___." | D81 | D81 is the different carton identified by the loose label.
Colleague: "Its recipient is ___." | Meadow Cafe | Meadow Cafe belongs to the loose D81 label, not the D80 screen.
Packer: "No label has been ___ yet." | applied | The mismatch is identified before any label attachment occurs.''',
))


BOOK['units'].append(unit(
    title='Staging and dispatch status',
    scene='Three staged, two on the manifest',
    skill='Compare staged goods with a dispatch record and report a cutoff risk without claiming departure or an approved correction.',
    brief='Order L66 has three cartons staged in lane 2. Its dispatch manifest lists only two cartons. The carrier cutoff is 16:00, and the goods have not departed. Staging colleague Imani asks dispatch clerk Noah to investigate the missing carton entry. No cause or specific missing carton identifier has been established. The discrepancy concerns the recorded carton count, not a verified physically missing carton. A review request does not confirm a corrected manifest, carrier acceptance, or departure before cutoff.',
    cast='Imani | Staging colleague\nNoah | Dispatch clerk',
    culture=('Ready-looking goods may still have unfinished records', 'Cartons in a staging lane can look ready to leave, but their physical position does not prove the dispatch record is complete. Name the lane, order, physical count, manifest count, and cutoff. Keep the record discrepancy separate from the actual movement status.'),
    a='''How many L66 cartons are staged in lane 2? | Three | Two | One | Six | Three physical cartons are staged for L66 in the specified lane.
What does the manifest list? | Two cartons | Three cartons | No cartons | Two pallets | The dispatch manifest records two cartons, one fewer than the staged count.
What is the actual departure status? | The goods have not departed | All cartons have departed | Only two cartons have departed | Carrier acceptance is confirmed | The briefing explicitly places all goods before departure, with the record issue unresolved.''',
    vocabulary='''staging | Placing goods in a designated area ahead of a later process. | confirm staging status
staging lane | Designated area for grouped outgoing goods. | identify the staging lane
dispatch manifest | Record listing shipments or units included in a dispatch. | compare the dispatch manifest
staged count | Number physically present in the staging area. | verify the staged count
manifest count | Number recorded on the dispatch manifest. | state the manifest count
carton entry | Individual or counted carton record in the relevant document. | investigate a missing carton entry
record discrepancy | Difference between documented and observed information. | report a record discrepancy
carrier cutoff | Latest stated time for the relevant carrier process. | confirm the carrier cutoff
departure status | Whether goods have actually left the facility. | preserve departure status
carrier acceptance | Carrier's acceptance of goods under the actual process. | verify carrier acceptance
dispatch release | Authorization to proceed with the relevant outgoing shipment process. | await dispatch release
manifest correction | Authorized amendment to an inaccurate dispatch record. | confirm a manifest correction
shipment grouping | Association of cartons or items under one outgoing shipment. | verify shipment grouping
lane assignment | Designation of the staging lane for an order. | check the lane assignment
outbound order | Order being prepared for shipment from the facility. | identify the outbound order
loading status | Whether goods have been loaded, distinct from staging. | check loading status
departure confirmation | Evidence or record confirming goods have left. | obtain departure confirmation
missing entry | Record absent from the document, not necessarily a missing physical item. | investigate the missing entry
dispatch clerk | Worker coordinating outgoing records and shipment information. | contact the dispatch clerk
cutoff risk | Possibility that an unresolved issue affects the stated deadline. | flag the cutoff risk
reconciliation check | Comparison intended to explain and resolve inconsistent figures. | perform a reconciliation check
unverified cause | Explanation not established by the available evidence. | avoid an unverified cause
status distinction | Separation of stages that must not be treated as interchangeable. | preserve the status distinction
pending correction | Record amendment that has not yet been completed. | report a pending correction''',
    precision='Three cartons are staged, but only two are listed. The manifest is one carton below the staged count. That is not evidence that a physical carton is missing, and the specific omitted carton reference has not been identified.',
    precision_extra='Staged, loaded, accepted by a carrier, and departed are separate statuses. The 16:00 cutoff gives urgency but does not prove completion before that time. Report the discrepancy for investigation without inventing an amendment or recording departure prematurely.',
    phrases='''Identify the order and lane | L66 is staged in lane 2.\nState the physical count | There are three cartons in the lane.\nState the document count | The manifest lists two cartons.\nGive the discrepancy | The manifest is one carton below the staged count.\nDistinguish record and goods | We are investigating a missing entry, not a confirmed missing carton.\nKeep the deadline visible | The carrier cutoff is 16:00.\nAsk for investigation | Can dispatch check the missing carton entry?\nKeep departure accurate | The goods have not departed.\nAvoid a completion claim | The manifest has not been corrected yet.\nAvoid an invented identifier | We have not identified which carton reference is omitted.\nKeep the cause open | We do not know why the record differs.\nSeparate staging and loading | Staged does not mean loaded.\nSeparate loading and departure | Loaded would not by itself prove departure.\nAvoid a cutoff guarantee | I cannot promise departure before 16:00 from these facts alone.\nRead back both counts | Three staged, two listed, with departure still pending.\nClose with the next owner | Dispatch will investigate while the current status stays explicit.''',
    notes='''One below | Compares the manifest's two against the physical count of three.\nMissing entry versus missing carton | Absence in a record is not the same as physical absence.\nStaged | Identifies a preparation stage, not a completed carrier handover.\nHas not departed | Preserves the actual movement status explicitly.\nCutoff risk | Signals urgency without making an unsupported delivery commitment.\nWhich carton | Remains a question when only the count mismatch is known.''',
    d='''Which status update is accurate? | L66 has three staged in lane 2, two listed, and no departure yet. | L66 has departed because the cartons are staged. | One physical carton is definitely lost. | The manifest is corrected because someone will check it. | The accurate update separates the physical count, document count, and unfinished departure.
What is the known discrepancy? | One carton fewer on the manifest than in staging. | One carton fewer in staging than on the manifest. | Three cartons missing from the warehouse. | No discrepancy because the order number matches. | Two listed is one below the three physically staged cartons.
Which statement invents an outcome? | The goods will definitely depart before 16:00. | The carrier cutoff is 16:00. | Dispatch can investigate. | No goods have departed. | The deadline and review request do not establish a guaranteed departure outcome.
What should Noah investigate? | The missing carton entry and correct association with L66. | An assumed theft with no supporting facts. | A fabricated carton reference. | A departure already treated as complete. | The supplied issue concerns a count mismatch in the dispatch record for L66.''',
    dialogue='''Imani | Noah, L66 has three cartons staged in lane 2, but the manifest lists only two. The carrier cutoff is 16:00, so I need to flag it.
Noah | I will check the [[dispatch manifest::Dispatch manifest lists two cartons and must be reconciled with the three physically staged for L66.]]. First, are we talking about three cartons physically present, rather than a system quantity you have not verified?
Imani | Yes, three cartons are staged in lane 2. The difference is in the manifest count. The goods have not departed.
Noah | Then the [[staged count::Staged count is the three cartons physically present, distinct from the manifest's recorded two.]] is three and the document count is two. We should not describe that as a physically missing carton.
Imani | Exactly. I want the report to say one missing entry against the staged quantity, not one carton lost somewhere in the warehouse.
Noah | That is the right [[status distinction::Status distinction separates the record mismatch from physical stock absence and from actual departure.]]. A record can be incomplete while all the staged cartons are present. We still need to establish which entry is missing.
Imani | I have not identified a specific omitted carton reference. I only have the order, lane, and the two different counts so far.
Noah | I will investigate the [[missing entry::Missing entry is the document issue; its specific carton identifier has not yet been established.]] without inventing an identifier. The check needs to connect the correct carton records with L66.
Imani | Please keep the carrier cutoff in the message. I do not want the discrepancy passed along as though there were no timing consequence.
Noah | I will flag the [[cutoff risk::Cutoff risk marks possible impact on the sixteen-hundred deadline without guaranteeing departure or acceptance.]] at 16:00. That gives the issue its timing context, but it does not mean I can promise a completed correction or departure by then.
Imani | Understood. The cartons being in the staging lane can make the order look further along than it is. I want that wording kept precise.
Noah | Yes. [[Staging::Staging places goods in a preparation area; it does not confirm loading, carrier acceptance, or departure.]] is not the same as loading or carrier acceptance, and neither of those should be assumed from their position in lane 2.
Imani | Have you corrected the manifest already, or are you accepting the investigation now? I need to know which status to give the next colleague.
Noah | I am taking the investigation. A [[manifest correction::Manifest correction has not occurred merely because Noah accepts the investigation; the document still requires checking.]] is not complete, and I should not tell you that the count has been fixed before the check.
Imani | Thank you. We also do not know why the manifest lists two. I have no evidence of a particular person's mistake or a system failure.
Noah | Keep the [[unverified cause::Unverified cause remains unknown; the observed count difference does not identify an individual or system failure.]] out of the factual conclusion. We can report the discrepancy accurately without assigning blame.
Imani | Let me summarize for the handoff: L66, lane 2, three cartons staged, two on the manifest, cutoff 16:00, no departure.
Noah | That is a clear [[reconciliation check::Reconciliation check compares the actual staged quantity with the manifest and seeks the correct missing association.]] to take forward. I will investigate the omitted entry while keeping those figures and the cutoff in view.
Imani | I will tell the next colleague you own that investigation, not that the order has been released or sent. The current record remains unresolved.
Noah | Correct. No [[departure confirmation::Departure confirmation is absent because the goods have not left; an accepted review task does not change that fact.]] exists here. Three staged, two listed, and the manifest question is still open while I investigate.''',
    transfer_title='Report a different manifest gap',
    transfer_setup='Order M77 has five cartons staged in lane 4. The manifest lists four. The carrier cutoff is 17:00, and nothing has departed. Dispatch will investigate the missing entry.',
    transfer='''Colleague: "There are ___ cartons staged." | five | Five is the observed physical carton count in lane four.
Clerk: "The manifest lists ___ cartons." | four | Four is the document count, one below the staged quantity.
Colleague: "The cutoff is ___." | 17:00 | Seventeen hundred is the deadline to include without guaranteeing departure.
Clerk: "No goods have ___ yet." | departed | The stated physical movement status remains unchanged during the investigation request.''',
))


BOOK['units'].append(unit(
    title='Returns and stock status',
    scene='Unopened-looking is not ready for sale',
    skill='Confirm return identity, qualify an external observation, and refer condition review without releasing the item as saleable.',
    brief='Returns intake worker Theo receives kettle K25, which matches its return reference. The packaging appears unopened, but the required condition review is still pending. Returns checker Mira owns that review. Theo cannot mark the kettle ready for sale. Colleague Hana needs a clear handoff separating reference matching, apparent packaging condition, review status, and release authority. No refund, functional check, product-safety finding, or saleable-stock decision has been completed in this scenario.',
    cast='Theo | Returns intake worker\nHana | Inventory colleague',
    culture=('A careful observation can still be useful', 'Appears unopened reports what the packaging looks like without claiming that the item has never been used or is safe to sell. Confirm the return reference, name the reviewer, and preserve the pending status instead of letting a positive appearance substitute for the required decision.'),
    a='''What has been matched? | Kettle K25 and its return reference | A completed refund and an invoice | A safety certificate and a new sale | A confirmed repair and replacement | The intake check connects the kettle to the correct return reference.
What does the packaging observation establish? | It appears unopened, without completing condition review | The kettle is definitely unused and functional | The item is certified safe for sale | All return checks are complete | Appearance is the stated observation and does not establish the item's internal condition.
Who owns the pending review? | Mira | Theo with automatic sale-release authority | The next customer | No one | Mira is explicitly named as responsible for the condition review.''',
    vocabulary='''return intake | Initial receiving and recording of returned goods. | complete return intake
return reference | Identifier linking goods to a specific return arrangement. | match the return reference
returned item | Product brought back through a return process. | identify the returned item
reference match | Correspondence between the item and the return record. | confirm the reference match
packaging appearance | Visible external state of the packaging. | describe packaging appearance
appears unopened | Looks unopened without proving past use or internal condition. | report appears unopened
condition review | Examination required to assess returned-item condition. | await condition review
returns checker | Person responsible for the relevant return examination. | name the returns checker
pending review | Status indicating the required examination is unfinished. | preserve pending-review status
saleable stock | Inventory approved as suitable for sale under the applicable process. | distinguish saleable stock
ready for sale | Status indicating required sale-release conditions have been met. | verify ready-for-sale status
release authority | Permission to approve an item for a particular use or status. | confirm release authority
functional check | Examination of whether a product operates as required. | distinguish a functional check
product-safety finding | Established conclusion about relevant safety requirements. | avoid an unsupported product-safety finding
unused condition | State of not having been used, requiring appropriate evidence. | verify unused condition
intake observation | Fact or qualified impression recorded during initial receipt. | preserve the intake observation
review owner | Person responsible for completing the pending assessment. | identify the review owner
stock status | System or process classification of inventory condition and availability. | confirm stock status
restocking | Returning goods to the relevant inventory under the actual process. | clarify restocking authorization
disposition | Authorized decision about the next treatment of returned goods. | await the disposition
refund status | Whether a financial return to the customer has been approved or completed. | keep refund status separate
condition evidence | Information supporting a conclusion about item condition. | check condition evidence
review completion | Actual finishing of the required assessment. | confirm review completion
status release | Authorized change from a restricted or pending state. | distinguish status release''',
    precision='K25 matches the return reference, and its packaging appears unopened. Neither fact completes the condition review or proves unused, functional, safe, or saleable condition. Mira owns the review, and Theo cannot mark the kettle ready for sale.',
    precision_extra='Return identity, physical condition, financial remedy, and inventory status answer different questions. Preserve the actual site statuses and approval limits. This exercise does not instruct learners to test electrical goods, inspect product safety, or release a returned item.',
    phrases='''Identify the return | This is kettle K25.\nConfirm the reference | It matches the return reference.\nQualify the observation | The packaging appears unopened.\nAvoid a use-history claim | I cannot confirm that the kettle has never been used.\nState the review status | Condition review is still pending.\nName the owner | Mira owns that review.\nExplain your limit | I cannot mark it ready for sale.\nSeparate identity and condition | A reference match is not a condition approval.\nAvoid a functional claim | No functional check is confirmed here.\nAvoid a safety claim | We have no established product-safety finding from this intake.\nKeep finance separate | This handoff does not confirm a refund.\nPreserve the existing status | Keep the review status pending until the required decision.\nAsk for an accurate handoff | Please include the observation and the named reviewer.\nAvoid a false release | The item has not been approved as saleable stock.\nDistinguish assignment and completion | Mira owning the review does not mean it is finished.\nClose with the next step | The next step is Mira's condition review.''',
    notes='''Appears | Qualifies an observation instead of asserting a fully verified condition.\nUnopened versus unused | Packaging appearance does not establish the complete use history of the item.\nMatches | Answers identity, not functional condition or saleability.\nPending | Indicates the review is unfinished, not automatically failed or passed.\nOwns versus completed | Responsibility for a review is not evidence of its outcome.\nReady for sale | Requires the actual applicable checks and authorization, not a visual impression alone.''',
    d='''Which handoff is accurate? | K25 matches its reference; packaging appears unopened; Mira's review is pending. | K25 is unused and safe because the box looks closed. | K25 is already released for sale. | Mira has completed the review because she owns it. | The statement separates verified identity, qualified observation, and the unfinished review.
Which conclusion overstates the observation? | The kettle is definitely functional and unused. | The packaging appears unopened. | Condition review remains pending. | Theo lacks sale-release authority. | External packaging appearance does not establish function or prior use.
Who has the next defined task? | Mira, to perform the condition review. | Theo, to mark it saleable without review. | Hana, to promise a refund. | A customer, to decide the warehouse stock status. | Mira is the named owner of the required pending assessment.
Which status should not be claimed yet? | Ready for sale. | Matched return reference. | Packaging appears unopened. | Review pending. | Sale-ready status is unsupported because condition review and release approval remain incomplete.''',
    dialogue='''Hana | Theo, what is the status of the returned kettle K25? I need to know whether it can go into saleable stock or still needs review.
Theo | It has a [[reference match::Reference match confirms K25 belongs to the return record; it does not establish condition or saleability.]] with the return record. The packaging appears unopened, but the condition review is still pending.
Hana | The box looks tidy from here. Is appears unopened your observation, or are you confirming that the kettle has never been used?
Theo | It is an [[intake observation::Intake observation reports the packaging appearance and does not verify the item's complete use history.]], not a confirmed history. I cannot say the kettle has never been used based only on how the packaging looks.
Hana | That distinction matters. I do not want a positive-looking box to become an automatic decision that the product is ready for another customer.
Theo | Exactly. [[Condition review::Condition review is the required next assessment, still unfinished despite the matching reference and apparent packaging state.]] has not been completed. We have matched the identity, but that does not tell us the result of the required examination.
Hana | Who is responsible for that review? I want to give the next shift a person and an action rather than simply saying someone should look at it.
Theo | Mira is the [[review owner::Review owner identifies Mira as responsible for the assessment without implying she has already carried it out.]]. She owns the condition review. Assigning that work to her does not mean we already have a decision.
Hana | Understood. Do you have authority to mark it ready for sale while the review is pending, perhaps because the packaging seems untouched?
Theo | No. I do not have that [[release authority::Release authority to mark K25 ready for sale is not held by Theo and is not created by packaging appearance.]]. I cannot turn an intake observation into permission to return the kettle to saleable stock.
Hana | Then the record should not say function tested either. A matched reference is not the same as checking whether the kettle works.
Theo | Correct. No [[functional check::Functional check would examine operation; no such completed check is supplied by this intake conversation.]] is confirmed here. Nor does our conversation establish a product-safety finding or an approved sale-ready condition.
Hana | I will keep financial questions separate too. We have not said that a refund was approved merely because the returned item matches the reference.
Theo | Yes. [[Refund status::Refund status concerns a separate financial process and is not established by matching the returned item.]] is not established by this handoff. Identity, condition, inventory status, and a customer remedy are different questions.
Hana | Let me read the note back: K25 matches its return reference; packaging appears unopened; condition review pending with Mira; no sale release.
Theo | That keeps the [[stock status::Stock status must preserve the pending review and absence of sale release rather than imply immediate availability.]] accurate. It also avoids claiming that the item is either approved or rejected before the review provides its result.
Hana | Good point. Pending does not mean it has failed. It means the required decision has not been made, despite the reassuring appearance.
Theo | Exactly. A [[disposition::Disposition is the authorized decision about the returned item, still to follow the required condition review.]] still needs to follow the actual review process. We should not choose sale, rejection, repair, or another outcome from appearance alone.
Hana | I will pass on the same facts and the named owner. The next person should know what was checked and what remains to be checked.
Theo | Thank you. [[Review completion::Review completion remains absent; the handoff names the owner but does not supply the assessment or its outcome.]] is still pending with Mira. K25 is matched to the return, but it has not been marked ready for sale.''',
    transfer_title='Hand over another pending return review',
    transfer_setup='Returned toaster T36 matches its return reference. Packaging appears unopened, but condition review is pending with Jo. Intake staff cannot release it for sale.',
    transfer='''Intake: "The returned item is ___." | T36 | T36 is the toaster reference supplied for this new return.
Colleague: "The packaging ___ unopened." | appears | Appears qualifies the visual observation without proving internal condition or past use.
Intake: "The review owner is ___." | Jo | Jo is the named person responsible for the pending assessment.
Colleague: "Sale release is not ___." | authorized | Intake staff lack authority to release the item before the required process.''',
))


BOOK['units'].append(unit(
    title='Inventory and shift handoffs',
    scene='The recount agrees, the cause does not',
    skill='Transfer a verified count difference, distinguish completed recount from pending investigation, and preserve adjustment authority.',
    brief='At shift change, inventory clerk Priya hands item T9 in B11 to evening clerk Sam for follow-up. The first cycle count found eighteen units; a completed recount also found eighteen. The system still shows twenty. The two-unit difference has no confirmed cause. Sam can review transaction history, but no stock adjustment is approved. Priya must make clear that recounting is already complete while cause investigation and any adjustment decision remain unfinished.',
    cast='Priya | Outgoing inventory clerk\nSam | Evening inventory clerk',
    culture=('Do not hand over completed work as if it were still missing', 'A useful handoff states what has already been verified as well as what remains open. Repeating the count may not answer a transaction-history question. Preserve both figures and the completed recount without implying that an agreed count gives automatic authority to adjust stock.'),
    a='''What do both physical counts show? | Eighteen units | Twenty units | Two units | Eighteen cases with an unknown pack size | The first count and completed recount both agree on eighteen units.
What does the system show? | Twenty units | Eighteen units after an approved adjustment | Two units | No item record | The system balance remains twenty despite the verified physical count of eighteen.
What is Sam's next task? | Review transaction history | Perform the recount that has not yet occurred | Approve an adjustment automatically | State that theft is proved | The recount is complete, and Sam can review the transaction history for the unexplained difference.''',
    vocabulary='''cycle count | Physical inventory check of selected stock on a recurring basis. | perform a cycle count
recount | Second count to verify a previous quantity. | confirm the recount
verified count | Quantity supported by the completed checking process. | report the verified count
system balance | Quantity currently recorded in the inventory system. | compare the system balance
count variance | Difference between counted and system quantities. | quantify the count variance
two-unit deficit | Count two units below the reference balance. | report a two-unit deficit
transaction history | Record of inventory receipts, issues, transfers, and adjustments. | review transaction history
receipt transaction | Record of stock received into the relevant inventory. | check the receipt transaction
issue transaction | Record of stock taken out for an order or use. | check the issue transaction
transfer transaction | Record of stock moved between locations or inventory categories. | review the transfer transaction
stock adjustment | Authorized change to recorded inventory to correct a difference. | request a stock adjustment
adjustment approval | Permission to make the relevant inventory correction. | await adjustment approval
posting | Recording a transaction in the relevant system. | check transaction posting
unposted movement | Movement not yet reflected in the relevant records. | investigate a possible unposted movement
audit trail | Record allowing changes and actions to be traced. | preserve the audit trail
count sheet | Document recording an inventory count and its context. | retain the count sheet
item-location pair | Specific combination of product and storage position. | confirm the item-location pair
outgoing clerk | Worker transferring responsibility at the end of a shift. | brief the outgoing clerk
incoming clerk | Worker taking responsibility on the next shift. | identify the incoming clerk
completed check | Verification step already performed and recorded. | distinguish a completed check
pending investigation | Further inquiry whose result is not yet established. | hand over the pending investigation
cause finding | Supported conclusion explaining the discrepancy. | avoid an unsupported cause finding
handoff acknowledgment | Confirmation that the next person accepts the stated follow-up. | obtain a handoff acknowledgment
inventory integrity | Reliability of inventory records and their supporting evidence. | protect inventory integrity''',
    precision='Both counts are eighteen, while the system shows twenty: the verified physical quantity is two units below the recorded balance. The recount is complete. The cause is not confirmed, and no adjustment has been approved.',
    precision_extra='Transaction history can help explain a difference, but reviewing it is not the same as finding the cause or posting an adjustment. Preserve the original figures, item-location pair, and supporting record instead of overwriting the system merely to make it agree.',
    phrases='''Name the item and location | This handoff concerns T9 in B11.\nGive the first count | The first count found eighteen units.\nGive the recount result | The completed recount also found eighteen.\nGive the system figure | The system still shows twenty.\nQuantify the difference | The count is two units below the system balance.\nKeep the cause open | No cause has been confirmed.\nName completed work | The recount is complete, not still pending.\nName the next check | Please review the transaction history.\nAccept ownership | I will take the transaction review.\nPreserve the authority limit | No stock adjustment is approved.\nAvoid an invented explanation | An unposted movement is a possibility to check, not a finding.\nAvoid an accusation | The difference does not by itself prove theft.\nPreserve the evidence | Keep both counts and the system figure in the record.\nSeparate acknowledgment and outcome | Taking the handoff does not resolve the variance.\nRequest a read-back | Please repeat the figures and the remaining task.\nClose with the current status | Eighteen verified, twenty recorded, cause unknown, adjustment unapproved.''',
    notes='''Also | Shows the recount agrees with the original eighteen-unit result.\nStill | Indicates the system remains at twenty rather than claiming an adjustment occurred.\nBelow versus above | Gives the direction of the two-unit variance.\nCompleted versus pending | Applies to separate tasks: recount complete, investigation pending.\nPossible versus found | A suggested explanation is not a verified cause.\nWill review | Assigns future work without implying review completion or adjustment approval.''',
    d='''Which handoff is accurate? | T9 in B11: eighteen counted and recounted, twenty recorded, cause unknown. | T9 in B11: recount still missing and theft confirmed. | T9 was adjusted to eighteen without approval. | T9 has two physical units in total. | The accurate message preserves both verified counts, the unchanged balance, and uncertainty about cause.
Which task is already complete? | The recount that also found eighteen. | The cause investigation. | The approved system adjustment. | The transaction-history review by Sam. | The briefing explicitly states that the recount is complete and agrees at eighteen.
What does the count variance establish? | Two fewer physical units than the system balance. | The cause is definitely an unposted issue. | Theft by the outgoing clerk. | Permission for any worker to change the balance. | The two-unit difference is arithmetic evidence, not proof of cause or authority.
Which next statement respects the approval limit? | I will review history; no adjustment is approved yet. | I will change twenty to eighteen because I accepted the handoff. | The recount automatically approves posting. | There is no need to retain the original system figure. | Reviewing records and accepting ownership do not authorize an inventory adjustment.''',
    dialogue='''Priya | Sam, I need to hand over T9 in B11. The first count was eighteen units, and the recount also gave eighteen. The system still shows twenty.
Sam | So the [[recount::Recount is already complete and agrees with the original eighteen-unit result, rather than remaining an unfinished task.]] is complete, not something you are asking me to do for the first time. The difference is still two units against the system.
Priya | Correct. I want that clear because a note saying count issue could make you repeat completed work instead of checking what remains unresolved.
Sam | I will preserve the [[verified count::Verified count is eighteen, supported by both completed physical counts and distinct from the system's twenty.]] of eighteen and the recorded twenty. Has any cause been confirmed, or are we still at the discrepancy stage?
Priya | No cause is confirmed. We know the figures disagree, but we do not yet know whether a transaction, movement, or something else explains it.
Sam | Then [[transaction history::Transaction history is the next record source to review for an explanation; it has not yet supplied a cause.]] is the next review I can take. I will not call a possible unposted movement an established explanation.
Priya | Thank you. No stock adjustment is approved either. The fact that two counts agree should not be mistaken for permission to change the system.
Sam | Understood. [[Adjustment approval::Adjustment approval is still absent; agreement between counts does not give automatic authority to alter inventory records.]] is a separate requirement. I can review the records without claiming that I may simply replace twenty with eighteen.
Priya | Please keep the exact item and location in your notes. The difference belongs to T9 in B11, not every location that holds T9.
Sam | I will preserve the [[item-location pair::Item-location pair ties the verified difference specifically to T9 in B11 rather than all stock of T9.]]. A location-specific count should not become a statement that the entire warehouse has the same discrepancy.
Priya | Good. Also, two below the system balance is not the same as saying we found only two units. We physically counted eighteen.
Sam | Yes. The [[count variance::Count variance is minus two relative to the recorded twenty; it is not the total physical quantity.]] is two units below the reference balance. The count itself remains eighteen units.
Priya | I have no evidence to accuse anyone. I want the handoff neutral enough that the transaction review can follow the records instead of a story.
Sam | That protects the [[audit trail::Audit trail preserves the original figures and checks so the review can trace actual actions rather than an assumed explanation.]]. We should retain both count results and the system figure, rather than overwriting information to make the discrepancy disappear.
Priya | Can you confirm that you are taking the transaction-history review, while keeping the recount listed as complete and the cause as unknown?
Sam | Yes. My [[handoff acknowledgment::Handoff acknowledgment accepts the next review task while preserving the completed recount and unresolved cause.]] covers that review. It does not mean the records have already been checked or the variance has been resolved.
Priya | Please read the current status back once before we finish. That will show whether we agree on both the figures and the unfinished action.
Sam | T9 in B11: eighteen counted and recounted, [[system balance::System balance remains twenty; no authorized posting has changed it to the physical count.]] twenty, two-unit difference, cause unknown, no approved adjustment. I own the transaction-history review.
Priya | That is accurate. We have transferred the next action without losing the completed check or claiming that the record now agrees with the stock.
Sam | Exactly. The [[pending investigation::Pending investigation is the cause-focused transaction review, distinct from the recount already finished.]] remains open. I will review the history, preserve the existing evidence, and keep any adjustment subject to the proper approval.''',
    transfer_title='Hand over another verified count difference',
    transfer_setup='Item U8 in D03 was counted at twenty-seven units, and the completed recount agrees. The system shows thirty. The cause is unknown. Clerk Jo accepts transaction-history review; no adjustment is approved.',
    transfer='''Clerk: "Both counts give ___ units." | twenty-seven | Twenty-seven is the verified physical quantity supported by the completed recount.
Colleague: "The system balance is ___." | thirty | Thirty remains the recorded amount because no adjustment has been approved.
Clerk: "The physical count is ___ units below the system." | three | Thirty recorded minus twenty-seven counted gives a three-unit deficit.
Colleague: "The transaction-history review belongs to ___." | Jo | Jo accepts the pending review without implying its completion or approving an adjustment.''',
))
