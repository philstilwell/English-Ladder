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
             note='Occupational context for shipment records, package checks, stock information, and inventory discrepancies. All teaching cases and conversations are original and fictional.', checked='10 October 2026'),
        dict(title='Microsoft Learn. Set Up Unit Sequence Groups.',
             url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/unit-measure-stocking-policies',
             note='Terminology background for product-specific relationships between individual units, boxes, and pallets. The book does not teach Microsoft system setup or prescribe a universal pack size.', checked='10 October 2026'),
        dict(title='Microsoft Learn. Cycle Counting.',
             url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting',
             note='Context for distinguishing physical inventory counts from review of differences. Fictional approval limits and handoffs are not instructions for operating a particular warehouse system.', checked='10 October 2026'),
        dict(title='Occupational Safety and Health Administration. Warehousing: Hazards and Solutions.',
             url='https://www.osha.gov/warehousing/hazards-solutions',
             note='Safety context for separating communication practice from actual site training, equipment use, and handling procedures. The dialogues do not provide operational safety certification.', checked='10 October 2026'),
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
    dialogue='''Nia | Ben, can you check PO 740 with me? It calls for twenty cartons. I've counted twenty-two, and the item labels match.
Ben | So we're two over. I'll log an [[overage::Overage names the two cartons above the order's twenty, not the total quantity received.]], with the product match noted separately. Have we heard from the supplier?
Nia | Not yet. Could these be extras from an earlier shortage? I don't have anything linking them to another order.
Ben | Then we need a [[supplier explanation::The supplier has not explained the extra cartons; a possible earlier shortage is not an established cause.]]. Don't put replacement stock in the note unless that is actually confirmed.
Nia | All right. I'll leave the ordered figure at twenty. I don't want my count to make it look as though we'd ordered twenty-two.
Ben | Keep the [[expected quantity::The expected quantity remains twenty, so the original order can still be compared with the physical count.]] unchanged. The discrepancy would disappear on paper if we quietly increased the order to match the truck.
Nia | My receiving note can say twenty-two physically counted, but that sounds different from accepting twenty-two. Which wording do you need?
Ben | Say [[received count::Received count describes the physical observation of twenty-two cartons, without approving their acceptance or payment.]] and make the unresolved acceptance clear. Use our actual status fields; don't select a status that approves more than you've checked.
Nia | The labels are right, at least. I'll put that beside the count instead of describing the whole delivery as correct.
Ben | Yes, the [[item match::The labels match the ordered product, but that does not resolve whether the additional quantity is accepted.]] tells us which product arrived. It doesn't answer what to do with the two extra cartons.
Nia | Can I amend the order once you've seen the count, or does that still go through the approval process?
Ben | An [[order amendment::Changing the purchase order requires authorization; Ben's review of a count does not itself provide that approval.]] still needs authorization. Neither this call nor the matching labels gives you that authority.
Nia | Understood. I'll flag it to you. I haven't agreed to pay for the extras or made them available for use.
Ben | Good. [[Stock release::Stock release is a separate authorization and is not established by reporting that cartons are physically present.]] remains a separate decision. Keep that separate from the quantity record so the next shift doesn't assume they're cleared.
Nia | For the summary, should I say plus two cartons, rather than simply twenty-two? Both numbers seem useful.
Ben | Include both. The [[quantity variance::The variance is positive two cartons: twenty-two counted minus twenty ordered.]] is plus two, against twenty ordered and twenty-two counted. That makes the comparison clear.
Nia | I'll send that with PO 740 and the label match. The supplier's explanation is still the open question.
Ben | And retain your [[approval limit::Nia can report the discrepancy but cannot approve an order change, payment, or release through this conversation.]] in the handoff. Someone reviewing the note needs to know what has not been authorized.
Nia | Read-back: twenty ordered, twenty-two counted, labels matching, two over. No explanation yet and no approved order change.
Ben | That's enough to start [[reconciliation::Reconciliation compares the order with the count and follows up the difference without erasing the original figures.]]. I'll take the discrepancy for review; don't describe it as resolved before we have the answer.''',
    rehearsal=["Read the two quantities with their labels: twenty ordered and twenty-two counted.","Repeat the two-carton overage and the separate item-label match.","Read the closing handoff without changing the original order or approving payment."],
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
SSCC | Serial Shipping Container Code: an 18-digit GS1 identifier for a logistic unit, such as one pallet. | verify the full SSCC
GTIN | Global Trade Item Number identifying a trade item, not a unique pallet shipment instance. | distinguish the GTIN from the SSCC''',
    precision='BK-14-B is the requested blue-folder item; BK-14-G is the green-folder item observed at A12. The bin sign and stock label conflict. Neither their similarity nor the shared location authorizes substituting the green folders.',
    precision_extra='The mismatch alone does not establish a bad putaway, a wrong sign, or a missing-blue-stock location. Read back both full codes and A12, then request the record check. Do not make an unapproved move or label change to force agreement.',
    phrases='''State the requirement | I need BK-14-B, blue folders.\nName the location | I am checking bin A12.\nRead the sign | The bin sign says BK-14-B.\nRead the stock | The stock label says BK-14-G.\nClarify the differing letter | B as in blue, not G as in green.\nReport the conflict | The sign and the actual stock label disagree.\nAvoid a substitution | Green folders are not the requested item.\nAsk for the record | Can you check the putaway record?\nKeep the cause unknown | I do not yet know why the green folders are here.\nKeep location unknown | We have not established where the blue folders are.\nAvoid a false correction | No bin-sign change has been approved.\nAvoid an unapproved move | I will not move the stock based on a guess.\nPreserve both codes | Please keep BK-14-B and BK-14-G separate in the note.\nConfirm the next owner | I will check the record for A12.\nDistinguish checking and approval | A record check is not permission to substitute.\nClose the clarification | The item mismatch remains open pending verification.''',
    notes='''B as in blue | Clarifies the code suffix using the relevant product color.\nSays versus contains | The sign's wording and the location's physical contents are separate observations.\nAssigned versus observed | A recorded location assignment is not proof of the goods currently present.\nSimilar versus identical | A one-letter difference can identify a different product variant.\nWhy versus where | The cause of the mismatch and the location of the correct stock are separate questions.\nCheck versus change | Looking at a record does not authorize a stock move or label amendment.''',
    d='''Which message is precise? | A12 sign says BK-14-B; stock says BK-14-G. | A12 has the right item because the sign says so. | The two codes mean the same thing. | The blue folders are definitely in the next bin. | The precise message preserves both conflicting identifiers and the relevant location.
Which clarification targets the code difference? | B as in blue, not G as in green. | B as in blue, not B as in the bin location. | BK-14, with the color suffix omitted. | A12 as the requested product code. | The final letter distinguishes the requested blue variant from the observed green variant.
Which claim lacks evidence? | A specific worker put the stock away incorrectly. | The bin sign and stock label disagree. | Mei can check the putaway record. | No substitution is approved. | The observed mismatch does not identify a cause or responsible worker.
Which next step matches the authority supplied? | Mei checks the putaway record. | Luis silently substitutes green folders. | Luis changes the bin sign immediately. | The stock label is changed to match the bin sign. | The available next step is verification, not an unapproved movement or record change.''',
    dialogue='''Luis | Mei, can you check A12? I need blue folders, BK-14-B, but the stock here says BK-14-G.
Mei | Let us separate the [[bin sign::Bin sign identifies the location's displayed assignment, which must be compared with the different stock label.]] from the stock label. What does the sign at A12 say, and what color are the folders you actually see?
Luis | The sign says B, blue. The stock says G, green. It's just that last letter, but it changes the item.
Mei | Then the [[color variant::Color variant distinguishes blue folders from green folders; similarity of the other code characters does not make them interchangeable.]] is different. You need B as in blue, while the stock label has G as in green.
Luis | I haven't picked the green ones. Can you check how they were put away before we go any further?
Mei | Good. An unapproved [[substitution::Substitution would replace the requested blue folders with green ones, which this location mismatch does not authorize.]] would not resolve the issue. I can check the putaway record to see what information we have for A12.
Luis | Could be the sign or the stock location. I don't know which, and I don't want to blame the last putaway without checking.
Mei | The [[putaway record::Putaway record may help establish what was placed in A12; it must be checked rather than assumed to prove a cause.]] is a useful next check. We should not assign a cause simply because the sign and the goods disagree.
Luis | Please don't mark the blue folders missing everywhere. I've only checked what is in A12.
Mei | Agreed. This is a [[location mismatch::Location mismatch describes the observed conflict at A12 without establishing warehouse-wide absence or the correct item's location.]] at A12. We have not established where the blue folders are or why the green folders are in this bin.
Luis | I'll include A12. Just sending the two codes wouldn't tell you where I found the mismatch.
Mei | Include a complete [[read-back::Read-back repeats the two full item codes and the bin so the verification request cannot collapse them into one.]]: requested BK-14-B, sign BK-14-B, observed stock BK-14-G, location A12. That gives us the exact conflict.
Luis | That's right. Am I authorized to move anything or change the sign while you're checking?
Mei | No [[stock move::Stock move is a separate action requiring authorization; the record-checking conversation does not approve it.]] has been approved, and no sign change has been approved either. A check is not permission to make the records agree by changing something.
Luis | Understood. I'll leave the correction to the proper process and report the labels as they are.
Mei | Yes. The [[suffix::Suffix is the final B or G, the small code difference that identifies different folder colors.]] matters even when the rest of the code is identical. A familiar-looking reference is not enough to confirm the requested variant.
Luis | You'll check the record, then. I still don't have confirmed blue stock for this pick.
Mei | Correct. I own the [[verification request::Verification request assigns the record check while leaving the stock identity conflict and pick unresolved.]]. I will check the putaway information without claiming that it has already located the blue folders.
Luis | Final read-back: A12 sign, BK-14-B blue; actual stock, BK-14-G green. Both codes stay in the note.
Mei | Exactly. Keep the [[observed stock::Observed stock is the green BK-14-G actually seen, distinct from the bin's assigned blue-item description.]] distinct from the assigned location information. No substitution, move, or relabeling is approved by this discussion.''',
    rehearsal=["Read both complete item codes, then stress B as in blue and G as in green.","Repeat the sign, observed stock, and A12 location as three separate facts.","Read Mei's record-check commitment without claiming a substitute or stock move."],
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
    dialogue='''Omar | Asha, can you check this before I confirm the pick? S18 says six, and I was about to read that as six cases.
Asha | Read the [[unit of measure::The unit beside six is each, so the requested quantity is six individual trays rather than six cases.]] beside it. It's six each: six individual trays. The number alone isn't the instruction.
Omar | You're right; I skipped each. What is the pack for this tray? I need the conversion for this item, not the last one I picked.
Asha | Its [[case pack::This particular storage-tray item contains six trays per standard case, as stated in the briefing.]] is six trays. One standard case contains the complete six-tray quantity on S18.
Omar | Then the case count is one. Six trays required, divided by six trays in a case. Have I got that the right way round?
Asha | Yes, the [[case equivalent::Six requested trays divided by six trays per case gives one case equivalent, without changing the requested total.]] is one. Say six trays total as well, so nobody hears one and assumes you mean one tray.
Omar | If I'd taken six cases, I'd have thirty-six trays. I was multiplying the request instead of converting it.
Asha | Those would be the [[total units::Six cases multiplied by six trays per case produces thirty-six individual trays, not the six requested.]] in the mistaken pick. Thirty-six is thirty above what this ticket asks for.
Omar | So the excess would be thirty trays, not five. Five is the difference in cases, using this particular case pack.
Asha | Exactly. An [[overpick::An overpick is a quantity above the request; here the proposed six cases would exceed demand by thirty trays.]] needs its unit stated too. Five extra cases and thirty extra trays describe the same excess here.
Omar | I shouldn't use six per case for the folders on my next ticket, though. Their cartons look similar.
Asha | No. This is a [[product-specific conversion::The six-tray relationship belongs to this item; it does not establish a conversion for folders or other products.]]. The folder pack must come from the folder record, not the appearance of its carton.
Omar | What about another size of tray? Same product family, different item code. I'd check that separately as well.
Asha | Yes, confirm the [[pack size::Pack size is the quantity inside the actual item's package, which can differ between variants and products.]] for the exact item. A different variant may have a different quantity per case.
Omar | Let me try the radio message: S18, six storage trays each, one standard case equivalent. No pick confirmation yet.
Asha | That [[quantity read-back::The read-back preserves the six individual trays and one-case equivalent while keeping picking status explicit.]] is clear. I'd say six individual trays rather than six trays each, which can sound awkward.
Omar | Six individual trays total. Thanks. We've corrected my reading, but I haven't said the stock has been picked or sent.
Asha | Right. [[Pick confirmation::Pick confirmation records actual completed picking; a correct conversion alone does not establish that completion.]] belongs to the actual work record. The calculation cannot stand in for it.
Omar | I'll use the corrected quantity in the proper picking process. I won't change the order to six cases just because that was my first reading.
Asha | Good. The [[requested quantity::S18 still requests six individual trays; the conversation corrects an interpretation rather than amending demand.]] remains six trays. We caught the unit error before calling the pick complete.''',
    rehearsal=["Read six individual trays and one standard case equivalent.","Contrast thirty-six trays with six requested; say thirty excess trays, not five trays.","Read the pick-confirmation exchange without claiming the goods have been picked."],
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
FEFO | First-expire, first-out: prioritizing eligible stock by expiry rather than receipt date. | apply FEFO to eligible batches
availability check | Verification of stock usable for the specific requirement. | complete an availability check
remaining shelf life | Time between the relevant delivery date and expiry, assessed against customer requirements. | check remaining shelf life''',
    precision='D55 needs ten baskets and B04 has four, so the location is six short. Twelve shown in reserve is a possible source to investigate, not proof that six can be allocated and replenished in time for 15:00.',
    precision_extra='On-hand, reserved, allocated, released, and available may describe different inventory states. Use the actual system definitions. A short pick at one location does not prove a warehouse-wide stockout, and a replenishment request does not prove movement has occurred.',
    phrases='''Identify the demand | D55 needs ten baskets.\nName the location | The pick face is B04.\nState the observed quantity | There are four baskets at B04.\nCalculate the shortfall | We are six short at the pick face.\nState the system figure | The system lists twelve in reserve.\nPreserve the uncertainty | Allocation and availability have not been checked.\nAvoid promising the reserve | I cannot say those twelve are free for D55.\nAsk for review | Can the replenishment desk review the requirement?\nKeep the cutoff visible | The order cutoff is 15:00.\nAvoid a timing promise | We do not yet have a confirmed replenishment time.\nLimit the shortage claim | This is a B04 shortfall, not a confirmed warehouse-wide stockout.\nSeparate request and movement | The request does not mean the stock has moved.\nConfirm the needed amount | Six more baskets would meet the ten-basket requirement.\nPreserve the order reference | Keep the review attached to D55.\nAvoid automatic priority | The cutoff needs review, not an invented priority approval.\nClose with next checks | We need allocation, availability, and timing checked before promising fulfillment.''',
    notes='''Six short | Measures the gap between ten required and four present.\nShown in reserve | Reports a system figure without asserting physical or allocation verification.\nFree for | Informal wording for stock available to the specific order, not merely present.\nAt B04 | Limits the observed shortage to the named pick face.\nBy 15:00 | Is not promised merely because fifteen hundred is the cutoff.\nRequest raised | Indicates a next action, not a completed replenishment.''',
    d='''Which escalation contains the essential facts? | D55 needs ten; B04 has four; twelve shown in reserve are unchecked; cutoff 15:00. | Twelve in reserve guarantees the order. | The warehouse has no baskets anywhere. | B04 has ten because the order requires ten. | The complete message retains the demand, observed quantity, uncertain source, and cutoff.
How many additional baskets are needed at the pick face? | Six | Four | Ten | Twelve | Ten required minus four present leaves a six-basket shortfall.
Which claim is unsupported? | All twelve reserve baskets are available for D55. | Allocation needs checking. | Four baskets are at B04. | The cutoff is 15:00. | The reserve figure has not been checked for allocation or actual availability to this order.
What must happen before a supported completion promise? | Review stock allocation, availability, and replenishment timing. | Repeat the system total confidently. | Assume a request completes movement. | Remove the cutoff from the message. | Quantity in reserve alone does not establish usable stock or arrival at the pick face in time.''',
    dialogue='''Elena | Dev, D55 is short at B04: ten baskets needed, four here. The cutoff is fifteen hundred.
Dev | You are six short at the [[pick face::Pick face is B04, where four baskets are present against the order requirement of ten.]]. Does the system show any reserve stock for the same item, and has its availability been checked?
Elena | Twelve shown in reserve, but I haven't checked whether they're allocated. I can't say they're free for us.
Dev | Keep that distinction. The [[system quantity::System quantity is the twelve shown in reserve, not verified stock available to D55.]] is a possible source for review, not confirmation that the stock can be assigned and brought to B04.
Elena | Then I'll report ten needed, four here, six short, twelve in reserve unchecked. What else do you need?
Dev | Include the [[order cutoff::Order cutoff is fifteen hundred and must accompany the request without being turned into a completion promise.]] of 15:00 as well. That tells us why timing matters without claiming that replenishment can definitely meet it.
Elena | I'll include D55 and the exact item, so we don't get a different basket sent to B04.
Dev | Right. A [[replenishment request::Replenishment request starts review of supplying the correct stock to B04; it is not a completed movement.]] needs the exact demand and location. Raising it does not mean a replenishment task has already been completed.
Elena | Could those twelve already be committed? I can see the balance, not the allocation detail.
Dev | That is why [[allocation::Allocation identifies stock assigned to particular demand and must be checked before assuming the reserve is free.]] needs checking. Twelve on the screen does not necessarily mean twelve uncommitted baskets for D55.
Elena | So I can't tell packing we'll have ten in time just because twelve appears on the screen.
Dev | Correct. We need an [[availability check::Availability check establishes usable stock for the specific order rather than relying only on a reserve balance.]] for this requirement, followed by a realistic timing assessment. The arithmetic alone does not supply those results.
Elena | I won't call it a warehouse-wide stockout, either. My count is only for B04.
Dev | Exactly. It is a [[location shortfall::Location shortfall limits the observed problem to B04 and avoids an unsupported claim about all warehouse stock.]] of six baskets. We should not expand that into a claim that no baskets are available anywhere in the warehouse.
Elena | Six more at B04 would cover the quantity. We still need to know if those six can get here in time.
Dev | Yes. Any [[timing estimate::Timing estimate remains to be established; neither the reserve quantity nor the cutoff supplies a replenishment completion time.]] must follow the actual review. No confirmed replenishment time has been supplied so far.
Elena | Can you take the review? I'll keep the order and location together with the unanswered stock and timing questions.
Dev | I can review it at the [[replenishment desk::Replenishment desk is the responsible review point, not a guarantee that stock has been allocated or moved.]]. Keep D55, ten required, four at B04, six short, twelve shown in reserve, and the 15:00 cutoff together.
Elena | Thanks. I'll tell packing you've taken the review, with no confirmed replenishment time or completion promise.
Dev | Good. A [[fulfillment commitment::Fulfillment commitment would promise the order outcome, which remains unsupported until stock and timing checks are complete.]] still needs support. We are taking the next review step, with allocation, availability, and replenishment timing still unresolved.''',
    rehearsal=["Read ten needed, four at B04, six short, and twelve shown in reserve.","Repeat allocation, availability, and timing as three checks still required.","Read the 15:00 cutoff without turning it into a replenishment promise."],
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
    d='''Which interruption is most precise? | Please pause: C70 names Harbor Shop, but this loose label names C71 and Hillside School. | C70 has already been sent to Hillside School. | Please reprint C70 before checking either record. | C71 belongs to Harbor Shop because it is beside C70. | The specific pause identifies both conflicting reference-recipient pairs before application.
Which status report is accurate? | No label has been applied; both references need checking. | C70 has already shipped with the wrong label. | Relabeling is complete. | Both recipients have received their cartons. | The discrepancy is detected before application and no shipment outcome is established.
What does the loose label's location prove? | Only that it is beside C70, not that it belongs to C70. | It must be the correct label for C70. | The C70 screen is necessarily wrong. | C71 has already departed. | Physical proximity alone does not establish which record or carton the label belongs to.
Which next step preserves accuracy? | Verify both carton references and recipient associations. | Swap labels from memory. | Merge the two recipients into one record. | Mark both cartons dispatched to clear the station. | The supplied next step is a reference cross-check, not an assumed correction or departure.''',
    dialogue='''Arun | Rosa, stop a moment before you use that loose label. C70 says Harbor Shop on the screen; the label beside it says Hillside School.
Rosa | I haven't attached it. I'll check the [[carton reference::The carton reference identifies which carton the label belongs to; proximity to C70 is not sufficient.]] first. Does the loose one actually say C70?
Arun | No, it says C71. We're at station 3 with both cartons here. I think we're looking at two different recipient pairs.
Rosa | I see C71 on the [[loose label::The unattached label identifies C71 for Hillside School, separate from the C70 screen record.]], with Hillside School underneath. C70 on the screen is Harbor Shop.
Arun | Thanks for pausing. I caught it before anything went on, so we don't have a mislabeled carton to report at this point.
Rosa | Then it's a [[verification pause::The work pauses before application while the conflicting references are verified, not after a completed labeling error.]], not a relabeling job. I'll keep the current status accurate.
Arun | Can you check both references, not just change the one in your hand? I don't want C71 left with an assumed match.
Rosa | Yes, the [[reference cross-check::Both carton identifiers and their recipient records need comparison; checking one does not validate the other.]] covers C70 and C71. I'll use their records rather than swap labels from memory.
Arun | The print could be perfectly right for C71 and still be wrong for C70. Being next to this carton doesn't make it its label.
Rosa | Exactly. The [[order association::The association links a carton to its relevant order or recipient record, not to whichever label is nearest.]] comes from the matching record. We need more than the names looking familiar.
Arun | Read the two pairs back once, please. I nearly said Hillside for C70 myself because I'd just read the loose label.
Rosa | C70's [[screen record::The screen for C70 names Harbor Shop; that information must remain separate from the loose C71 label.]] names Harbor Shop. The loose C71 label names Hillside School. Neither label has been applied.
Arun | That's what I saw. We don't know why the loose label was there, and there's no need to guess who put it there.
Rosa | I'll report the possible [[workstation mix-up::The arrangement creates a potential mix-up, without proving who caused it or that anything was shipped incorrectly.]] with the exact references. A useful note doesn't need an accusation.
Arun | Right. Please don't write corrected wrong label. That would tell the next person a label was already attached and removed.
Rosa | I'll describe [[prevention::The check prevents a possible error before application; it is not evidence of repairing a completed mislabeling.]] instead: mismatch spotted before application, both references being checked. That's the stage we're at.
Arun | Once the records are verified, label handling follows the normal process. I haven't checked either carton for dispatch readiness.
Rosa | Understood. [[Label application::Application has not happened yet and must follow the verified match and actual packing process.]] and dispatch readiness are separate from identifying the two recipient names.
Arun | I'll leave the handoff as station 3, C70 Harbor Shop on screen, loose C71 Hillside School label, no labels applied.
Rosa | Agreed. We have no [[shipment departure::The label check supplies no evidence of shipment departure, and nothing has been described as dispatched.]] to record here. I'll finish the reference check before reporting any later stage.''',
    rehearsal=["Read C70 with Harbor Shop and C71 with Hillside School.","Repeat the interruption and the statement that no label has been applied.","Read the cross-check request for both references, without swapping labels from memory."],
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
What should Noah investigate? | The missing carton entry and correct association with L66. | The physical location of a carton assumed lost. | The carrier's receipt assumed to cover three cartons. | A replacement shipment assumed necessary. | The supplied issue concerns a count mismatch in the dispatch record for L66.''',
    dialogue='''Imani | Noah, there's a manifest discrepancy on L66. Three cartons in lane 2, but only two listed. Carrier cutoff is sixteen hundred.
Noah | I will check the [[dispatch manifest::Dispatch manifest lists two cartons and must be reconciled with the three physically staged for L66.]]. First, are we talking about three cartons physically present, rather than a system quantity you have not verified?
Imani | Three physically staged, yes. Nothing has departed. I'm comparing what's in lane 2 with the manifest.
Noah | Then the [[staged count::Staged count is the three cartons physically present, distinct from the manifest's recorded two.]] is three and the document count is two. We should not describe that as a physically missing carton.
Imani | Please call it a missing entry, not a lost carton. The third carton is here with the other two.
Noah | That is the right [[status distinction::Status distinction separates the record mismatch from physical stock absence and from actual departure.]]. A record can be incomplete while all the staged cartons are present. We still need to establish which entry is missing.
Imani | I haven't identified which carton reference is omitted yet. I have L66, lane 2, and the count difference.
Noah | I will investigate the [[missing entry::Missing entry is the document issue; its specific carton identifier has not yet been established.]] without inventing an identifier. The check needs to connect the correct carton records with L66.
Imani | Can you flag sixteen hundred with it? Dispatch needs the deadline as well as the discrepancy.
Noah | I will flag the [[cutoff risk::Cutoff risk marks possible impact on the sixteen-hundred deadline without guaranteeing departure or acceptance.]] at 16:00. That gives the issue its timing context, but it does not mean I can promise a completed correction or departure by then.
Imani | The order may look ready because it's staged. I don't want that turned into a departed status.
Noah | Yes. [[Staging::Staging places goods in a preparation area; it does not confirm loading, carrier acceptance, or departure.]] is not the same as loading or carrier acceptance, and neither of those should be assumed from their position in lane 2.
Imani | Have you corrected the record, or are you taking the check now? I need to pass on the right stage.
Noah | I am taking the investigation. A [[manifest correction::Manifest correction has not occurred merely because Noah accepts the investigation; the document still requires checking.]] is not complete, and I should not tell you that the count has been fixed before the check.
Imani | I haven't established what caused the missing entry. It could be several things; I don't have evidence yet.
Noah | Keep the [[unverified cause::Unverified cause remains unknown; the observed count difference does not identify an individual or system failure.]] out of the factual conclusion. We can report the discrepancy accurately without assigning blame.
Imani | Read-back: L66, lane 2, three staged, two listed, cutoff sixteen hundred, nothing departed.
Noah | That is a clear [[reconciliation check::Reconciliation check compares the actual staged quantity with the manifest and seeks the correct missing association.]] to take forward. I will investigate the omitted entry while keeping those figures and the cutoff in view.
Imani | I'll name you for the investigation and keep it open. I won't tell the next shift the order has gone.
Noah | Correct. No [[departure confirmation::Departure confirmation is absent because the goods have not left; an accepted review task does not change that fact.]] exists here. Three staged, two listed, and the manifest question is still open while I investigate.''',
    rehearsal=["Read three physically staged and two on the dispatch manifest.","Repeat lane 2, L66, and the 16:00 cutoff in one handoff.","Contrast a missing entry with a missing physical carton; then read no departure."],
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
    dialogue='''Hana | Theo, is returned kettle K25 cleared for sale, or is the condition review still outstanding?
Theo | It has a [[reference match::Reference match confirms K25 belongs to the return record; it does not establish condition or saleability.]] with the return record. The packaging appears unopened, but the condition review is still pending.
Hana | The box looks untouched. Are you saying it appears unopened, or that you've confirmed the kettle was never used?
Theo | It is an [[intake observation::Intake observation reports the packaging appearance and does not verify the item's complete use history.]], not a confirmed history. I cannot say the kettle has never been used based only on how the packaging looks.
Hana | Then I won't call it ready for sale just because the box looks good. What has actually been completed?
Theo | Exactly. [[Condition review::Condition review is the required next assessment, still unfinished despite the matching reference and apparent packaging state.]] has not been completed. We have matched the identity, but that does not tell us the result of the required examination.
Hana | Who's taking the review? I need a named person for the handover, not just someone to look at it.
Theo | Mira is the [[review owner::Review owner identifies Mira as responsible for the assessment without implying she has already carried it out.]]. She owns the condition review. Assigning that work to her does not mean we already have a decision.
Hana | Can you release it while we're waiting, or is that outside your authority?
Theo | No. I do not have that [[release authority::Release authority to mark K25 ready for sale is not held by Theo and is not created by packaging appearance.]]. I cannot turn an intake observation into permission to return the kettle to saleable stock.
Hana | And we haven't established that it works. Matching the return reference isn't a function test.
Theo | Correct. No [[functional check::Functional check would examine operation; no such completed check is supplied by this intake conversation.]] is confirmed here. Nor does our conversation establish a product-safety finding or an approved sale-ready condition.
Hana | What about the refund? I shouldn't tell customer service it's approved from this warehouse note, should I?
Theo | Yes. [[Refund status::Refund status concerns a separate financial process and is not established by matching the returned item.]] is not established by this handoff. Identity, condition, inventory status, and a customer remedy are different questions.
Hana | I'll read the note back: K25 matched, packaging appears unopened, condition review with Mira, no sale release.
Theo | That keeps the [[stock status::Stock status must preserve the pending review and absence of sale release rather than imply immediate availability.]] accurate. It also avoids claiming that the item is either approved or rejected before the review provides its result.
Hana | So pending isn't the same as rejected, either. We don't have the condition decision yet.
Theo | Exactly. A [[disposition::Disposition is the authorized decision about the returned item, still to follow the required condition review.]] still needs to follow the actual review process. We should not choose sale, rejection, repair, or another outcome from appearance alone.
Hana | I'll pass on exactly that, with Mira as owner. The next shift will know what remains outstanding.
Theo | Thank you. [[Review completion::Review completion remains absent; the handoff names the owner but does not supply the assessment or its outcome.]] is still pending with Mira. K25 is matched to the return, but it has not been marked ready for sale.''',
    rehearsal=["Read appears unopened with emphasis on appears.","Repeat the matched return reference and the condition review pending with Mira.","Read the distinction between pending, rejected, and ready for sale."],
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
posting | Recording a transaction in the relevant system, possibly later than physical movement. | compare movement and posting times
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
    dialogue='''Priya | Sam, I've got one count issue for handover: T9 in B11. Eighteen on the first count, eighteen on the recount, twenty in the system.
Sam | Is the [[recount::The recount has already been completed and agrees at eighteen, so it is not the missing next action.]] finished? I want to be sure I'm taking an investigation, not a request for a second count.
Priya | Finished, and it agreed at eighteen. The note needs both results, otherwise the next shift could think we're still waiting for that check.
Sam | I'll retain the [[verified count::Eighteen is supported by the first count and recount, while the recorded balance remains twenty.]] alongside twenty in the system. Have you established why they differ?
Priya | No. A movement or transaction might explain it, but I haven't checked enough to say that one does.
Sam | I'll take the [[transaction history::The history is the next evidence source to review; it has not yet established a cause for the difference.]] review. We need the actual records before turning a possible explanation into a finding.
Priya | Also, no adjustment is approved. Two matching counts don't mean I had authority to replace the recorded twenty with eighteen.
Sam | Yes, [[Adjustment approval::Approval to change the inventory record remains separate from verifying the physical count or accepting the review.]] is separate. Taking this handoff doesn't give me permission to post a change either.
Priya | Please keep B11 in the note. We haven't counted every location holding T9, so this isn't a total-stock statement.
Sam | I'll keep the [[item-location pair::T9 and B11 together define the count being discussed; the finding does not cover all locations of T9.]] explicit. T9 without B11 could send someone to the wrong balance.
Priya | And say two below the recorded balance, not two remaining. There are eighteen physically here, not two.
Sam | Agreed. The [[count variance::Eighteen counted minus twenty recorded gives a variance of minus two units, not a physical total of two.]] is minus two units; the physical count is eighteen. I'll use both figures with their labels.
Priya | The cause stays unknown for now. I don't have evidence of theft or a particular person making an error.
Sam | That's important for the [[audit trail::Retaining both counts and the original system figure keeps the evidence traceable instead of replacing it with an assumed cause.]]. Keep the original figures and count results so we can trace what happened.
Priya | Can I name you for the transaction review in my handover? I'd like the next person to know who has that follow-up.
Sam | Yes. My [[handoff acknowledgment::Sam accepts responsibility for the history review, not a claim that it is already complete or the discrepancy resolved.]] covers that review. Mark it assigned to me, with the cause still unresolved.
Priya | Thanks. Read the current position back once, please, including the part that's already done and the part you're taking.
Sam | T9, B11: eighteen counted and recounted; [[system balance::The system balance is still twenty because no authorized adjustment has changed the recorded figure.]] twenty; cause unknown; adjustment unapproved. Recount complete, history review with Sam.
Priya | That's it. The physical check is complete, but the reason for the difference and any authorized correction are still outstanding.
Sam | I'll continue the [[pending investigation::The remaining investigation concerns the unexplained difference and transaction history, not a recount already completed.]] from that point. I'll preserve the evidence rather than make the record agree before the explanation is established.''',
    rehearsal=["Read eighteen counted, eighteen recounted, and twenty recorded.","Repeat minus two as the variance, not the physical quantity.","Read Sam's next action while keeping the recount complete and adjustment unapproved."],
    transfer_title='Hand over another verified count difference',
    transfer_setup='Item U8 in D03 was counted at twenty-seven units, and the completed recount agrees. The system shows thirty. The cause is unknown. Clerk Jo accepts transaction-history review; no adjustment is approved.',
    transfer='''Clerk: "Both counts give ___ units." | twenty-seven | Twenty-seven is the verified physical quantity supported by the completed recount.
Colleague: "The system balance is ___." | thirty | Thirty remains the recorded amount because no adjustment has been approved.
Clerk: "The physical count is ___ units below the system." | three | Thirty recorded minus twenty-seven counted gives a three-unit deficit.
Colleague: "The transaction-history review belongs to ___." | Jo | Jo accepts the pending review without implying its completion or approving an adjustment.''',
))
