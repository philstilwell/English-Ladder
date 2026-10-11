"""Original planning, procurement, inventory, and logistics communication cases."""
from books.authoring import unit

BOOK = dict(
    slug='supply-chain-logistics', title='Supply Chain and Logistics English',
    cover_label='Demand / supply / inventory / movement',
    cover_title='Supply Chain\nand Logistics', cover_size=28,
    tagline='Plan the demand. Confirm the movement.',
    audience='For demand planners, buyers, inventory teams, logistics coordinators, and supply-chain leaders.',
    map_intro='Eight conversations that turn forecasts, inventory records, supplier messages, and shipment updates into precise decisions.',
    notes_title='Every commitment needs a clear basis.',
    notes_intro='Supply-chain work connects people who measure different things and promise different outcomes. Sales discusses demand; a supplier confirms an order; a carrier estimates arrival; a warehouse reports stock. None of those statements automatically answers all the others. These cases develop the language for distinguishing estimates, available resources, completed movements, and decisions that still need confirmation.',
    field_notes=[
        ('Name the demand evidence', 'Separate a historical result, a forecast, a sales target, and a confirmed order. An attractive promotion can justify a scenario without becoming booked demand or erasing an earlier forecasting pattern.', '"The uplift is a scenario assumption, not an order on the books."'),
        ('Follow the status of the movement', 'Order acknowledged, ready, collected, departed, arrived, and delivered describe different stages. Ask which event the date refers to and whose confirmation supports it.', '"Is Wednesday the estimated warehouse arrival or the planned departure?"'),
        ('Look below the total', 'A large inventory balance can hide shortages of particular items or stock that is allocated, blocked, or in another location. State which quantity is actually available for the relevant demand.', '"The total is high, but these two items still have no available stock."'),
        ('Make the decision and conditions explicit', 'A meeting should distinguish an approved action from an unresolved assumption. Name the owner, the evidence needed, and the next review without treating the absence of objections as a recorded decision.', '"We have agreed the base plan; the promotion increment remains conditional."')],
    scope_note='Original fictional language practice, not customs, legal, financial, transport-safety, or inventory-policy advice. All figures, shipments, organizations, and negotiations are invented. Use applicable law, governing contracts, current trade rules, authorized decisions, and qualified review. US customs examples are identified; requirements differ by jurisdiction.',
    sources=[
        dict(title='Association for Supply Chain Management. Forecast Bias.', url='https://www.ascm.org/ascm-insights/dont-get-caught-in-the-bias-trap/', note='Background on a forecast tending to be too high or low. The book states its own error-sign convention and uses original numerical cases.', checked='10 October 2026'),
        dict(title='Association for Supply Chain Management. Sales and Operations Planning.', url='https://www.ascm.org/topics/sales-and-operations-planning/', note='Background on cross-functional alignment of demand, supply, and business planning. The meeting decisions and scenarios are fictional.', checked='10 October 2026'),
        dict(title='International Chamber of Commerce. Incoterms 2020.', url='https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/', note='Background on allocating specified delivery obligations, costs, and risks. A trade term does not itself establish that a shipment moved or guarantee arrival.', checked='10 October 2026'),
        dict(title='Electronic Code of Federal Regulations. 19 CFR 141.86.', url='https://www.ecfr.gov/current/title-19/chapter-I/part-141/subpart-F/section-141.86', note='US invoice requirements, including detailed merchandise descriptions. The document exercise does not classify goods, assign duty, or authorize a customs filing.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Demand Planning and Forecast Bias',
    scene='Three optimistic forecasts and a new promotion',
    skill='Explain signed forecast error, distinguish bias from error size, and keep an unconfirmed promotional uplift separate from the baseline.',
    brief='Demand planner Aisha and sales lead Martin review monthly forecasts of 120, 130, and 140 units against verified demand of 100, 110, and 120. For this case, signed error means forecast minus actual demand. Next month\'s baseline is 120 units. Sales proposes a 30-unit promotional uplift but has no order evidence for it. Aisha and Martin must describe the three-month pattern and preserve the promotion as a scenario without treating either historical bias or future uplift as a certainty forever.',
    cast='Aisha | Demand planner\nMartin | Sales lead',
    culture=('Separate optimism from evidence', 'A sales opportunity can deserve attention without being entered as confirmed demand. Acknowledge the opportunity, then ask for the assumption and evidence. Keeping baseline and upside visible lets colleagues discuss the commercial case without rewriting historical results or pretending that a forecast is an order.'),
    a='''What is each month's signed error under the stated convention? | Plus 20 units | Minus 20 units | Zero units | Plus 120 units | Each forecast exceeds its corresponding actual demand by twenty units.
What is the next-month baseline? | 120 units | 150 confirmed orders | 30 units | 390 units | The brief states a baseline of 120 and a separate proposed uplift of thirty.
What supports the promotional uplift as confirmed orders? | No order evidence is supplied. | Three months of overforecasting prove the uplift. | The baseline itself is a signed purchase order. | A proposal automatically becomes booked demand. | The promotion is a proposed scenario, and the case explicitly supplies no supporting order evidence.''',
    vocabulary='''demand forecast | An estimate of future demand for a defined item and period. | prepare a demand forecast
actual demand | The observed demand under the stated measurement definition. | reconcile actual demand
forecast bias | A tendency for forecasts to be systematically too high or too low. | monitor forecast bias
signed error | The forecast difference calculated with an explicitly stated direction. | state the signed-error convention
mean error | The average signed forecast error across the defined observations. | calculate mean error
absolute error | The size of a forecast error without its positive or negative sign. | compare absolute errors
mean absolute error | The average absolute error across the defined observations. | report mean absolute error
overforecast | A forecast greater than the corresponding actual demand. | identify an overforecast
underforecast | A forecast below the corresponding actual demand. | investigate an underforecast
baseline forecast | The reference forecast before a separately identified adjustment. | preserve the baseline forecast
promotional uplift | Additional demand expected because of a promotion. | qualify promotional uplift
incremental demand | Demand additional to the specified base rather than displaced from elsewhere. | estimate incremental demand
cannibalization | A gain in one product's demand at the expense of another's. | assess demand cannibalization
seasonality | A recurring demand pattern tied to a calendar or cycle. | account for seasonality
trend | A sustained directional movement in a series over time. | distinguish trend from noise
forecast horizon | The future period covered by a forecast. | define the forecast horizon
forecast lag | The time between making a forecast and the period being forecast. | compare forecasts at the same lag
forecast snapshot | A saved version of the forecast at a specified time. | preserve the forecast snapshot
consensus forecast | A forecast agreed through the relevant cross-functional planning process. | review the consensus forecast
demand signal | Information indicating demand behavior or potential change. | evaluate a demand signal
booked order | An order recorded under the organization's order definition. | distinguish booked orders
scenario assumption | A premise used to construct a possible future case. | document the scenario assumption
forecast override | A deliberate adjustment to a model or baseline forecast. | justify a forecast override
forecast value added | Improvement in a defined forecast measure from a specified planning step. | evaluate forecast value added''',
    precision='With error defined as forecast minus actual, the three errors are +20, +20, and +20 units. Total error is +60 and mean error is +20. Positive means overforecasting under this convention; other systems may reverse the sign.',
    precision_extra='Zero mean signed error does not prove perfect forecasts: +10 and -10 cancel even though both forecasts missed. Mean absolute error would be 10. Next month, 120 plus a proposed 30 is a 150-unit scenario, not 150 confirmed orders.',
    phrases='''State the convention | Here we define signed error as forecast minus actual demand.
Describe the pattern | Each of the three forecasts exceeded actual demand by 20 units.
Name the average | Mean signed error is plus 20 units over these three months.
Limit the conclusion | This pattern does not prove every future forecast will be high.
Separate size and direction | Absolute error measures the miss without its sign.
Keep the reference | The next-month baseline remains 120 units.
Identify the increment | Sales proposes a 30-unit promotional uplift.
Qualify the scenario | That produces a 150-unit scenario, not confirmed demand.
Ask for evidence | What order or response evidence supports the proposed increment?
Avoid historical erasure | A future promotion does not change the earlier forecast errors.
Use a consistent snapshot | Compare the forecast version that existed at the agreed planning point.
Distinguish a target | A sales target is not automatically an unbiased demand estimate.
Check displacement | Is the uplift additional demand or partly shifted from another item?
Record the override | Keep the adjustment, owner, and rationale visible.
Evaluate the contribution | Assess whether the adjustment improves the defined forecast measure.
Close the discussion | Present baseline, upside, and supporting evidence separately.''',
    notes='''Bias | Directional tendency, not a moral judgment about the planner.
Positive | Has meaning only after the error-sign convention is stated.
Actual | Needs a measurement definition; shipments and unconstrained demand may differ.
Uplift | An increment against a specified baseline, not necessarily booked orders.
Consensus | An agreed forecast can still be wrong.
Snapshot | Preserves what was forecast at the time, avoiding hindsight substitution.''',
    d='''A colleague says the promotion cancels the historical overforecast. Which correction is accurate? | The proposed 30-unit increment does not change the three recorded errors of +20. | The total historical error falls from +60 to +30. | Mean historical error falls from +20 to -10. | The 150-unit scenario becomes confirmed demand once the old errors are removed. | Historical errors concern saved forecasts and actual demand for prior periods; a new proposal does not revise them.
Two other errors are +10 and -10. What follows? | Mean error is zero, but mean absolute error is 10. | Both forecasts were perfect. | Mean absolute error is zero. | Bias and error size are always identical. | Signed errors cancel, whereas absolute errors retain the magnitude of each miss.
Which next-month statement is precise? | Baseline 120; proposed uplift 30; upside scenario 150; no order evidence supplied. | Confirmed orders total 150. | Historical overforecasting proves the promotion cannot work. | The promotion eliminates the need to keep a baseline. | The statement separates the reference forecast, proposed increment, scenario total, and missing order evidence.
Why retain the original forecast snapshot? | To evaluate the forecast actually available at the agreed planning point | To replace old forecasts with actual demand before scoring | To ensure every override appears successful | To treat targets as customer orders | A fixed historical version prevents later knowledge from changing the forecast being evaluated.''',
    dialogue='''Martin | Sales expects the promotion to improve demand next month. Before we add the uplift, can we agree what the last three months actually tell us?
Aisha | They show an [[overforecast::Each forecast is twenty units above its corresponding actual demand, so each is an overforecast.]] of twenty units in each month. The forecasts were one hundred twenty, one hundred thirty, and one hundred forty against lower actual demand.
Martin | The dashboard uses a positive error number. I want to make sure everyone reads the direction correctly, because another report seems to use the opposite sign.
Aisha | State the [[signed error::The signed-error convention here is forecast minus actual, making overforecasts positive.]] convention beside it: forecast minus actual. Under this convention, each error is plus twenty; a different system may reverse that sign.
Martin | Let me check: plus sixty units in total, but plus twenty per month on average. Which figure belongs on the monthly performance slide?
Aisha | Correct. The [[mean error::Mean error averages the three signed differences: plus sixty divided by three gives plus twenty units.]] is plus twenty units across these three observations. That describes this period without proving that every future forecast must be too high.
Martin | What if positive and negative errors cancel in a later period? A zero average could look excellent even when individual months still miss by a meaningful amount.
Aisha | Compare [[mean absolute error::Mean absolute error preserves error magnitude, so opposite signed misses do not cancel each other.]] as well. If the errors are plus ten and minus ten, the signed mean is zero but the average absolute miss is ten.
Martin | For next month, the reference forecast is one hundred twenty. Sales proposes another thirty because of the promotion, but we have no supporting orders yet.
Aisha | Keep the [[baseline forecast::The baseline forecast remains the 120-unit reference against which the proposed promotional adjustment is shown.]] visible. We can show the thirty-unit proposal separately so people understand what comes from the reference and what comes from the new commercial assumption.
Martin | That gives a scenario of one hundred fifty. I do not want the planning team to dismiss the opportunity, but we should avoid calling it confirmed demand.
Aisha | Exactly. The [[promotional uplift::The promotional uplift is the proposed thirty-unit increment, not an already confirmed order quantity.]] is an expectation to evaluate. Ask what evidence supports the increment and whether the demand is genuinely additional rather than shifted from another product.
Martin | The campaign could move some existing customers from a related item. If we count all those purchases as new demand, the aggregate plan could be overstated.
Aisha | That would require assessing [[cannibalization::Cannibalization concerns demand transferred from another product, which may not increase total demand by the full uplift.]]. We should distinguish additional demand from redistribution before treating the whole increment as growth in the overall demand plan.
Martin | Sales has a target, but nobody has placed an order for that extra quantity. I will keep those two fields separate in the planning record.
Aisha | Right. A [[booked order::A booked order is recorded order demand, unlike the unsupported promotional expectation in this case.]] has a different status from a forecast or target. We currently have no order evidence for the proposed thirty-unit increase.
Martin | When the next results arrive, let's evaluate the forecast version we actually used. Revising old numbers after seeing demand would make the performance comparison misleading.
Aisha | Preserve the [[forecast snapshot::The forecast snapshot records the version available at the agreed planning point so later information cannot rewrite its score.]] and its planning date. We need a consistent lag and definition if we want to learn whether the adjustment helped.
Martin | I will present one hundred twenty as baseline and one hundred fifty as the promotion scenario, with the evidence gap stated. The historical errors will remain unchanged.
Aisha | Good. Record the proposed [[forecast override::The override is the deliberate adjustment to the baseline, whose rationale and later contribution should remain visible.]] with its owner and rationale. That gives the opportunity a fair assessment without disguising uncertainty or treating the scenario as a customer commitment.''',
    transfer_title='The sign does not measure certainty',
    transfer_setup='A forecast is 80 units and actual demand is 100. Error is defined as forecast minus actual. Next month has a 90-unit baseline and a proposed 15-unit uplift without orders.',
    transfer='''Planner: "The signed error is ___ twenty units." | minus | Eighty minus one hundred equals negative twenty under the stated convention.
Sales: "That is an ___." | underforecast | Forecast demand is below actual demand in the supplied period.
Planner: "The next-month scenario totals one hundred ___ units." | five | The baseline of ninety plus fifteen gives a scenario total of 105.
Sales: "The uplift remains an ___, not booked orders." | assumption | The proposed increment has no supporting order evidence in this case.''',
    rehearsal=["Read the corrected forecast dialogue in pairs. Stress plus twenty, mean, and absolute when comparing the historical errors.","Switch roles. Read turns 9-20, distinguishing the 120-unit baseline, proposed 30-unit uplift, and 150-unit scenario.","Complete and check the transfer. Read 80 minus 100 as minus 20, and keep the 105-unit next-month scenario separate from orders."]))

BOOK['units'].append(unit(
    title='Procurement and Supplier Performance',
    scene='Acknowledged, but not scheduled',
    skill='Request a usable supplier commitment by separating acknowledgment, quantities, shipment timing, arrival timing, and unresolved dependencies.',
    brief='Buyer Keiko and supplier account manager Luis discuss purchase order P46 for 500 units. The supplier has acknowledged receipt but has given no shipping date. The buyer needs warehouse receipt by October 12. Capacity and transit timing are not confirmed. A supplier message promises an update tomorrow at noon, not dispatch tomorrow. Keiko must obtain a clear status and request line-level quantities and dates without treating the acknowledgment or update appointment as a delivery commitment.',
    cast='Keiko | Buyer\nLuis | Supplier account manager',
    culture=('A precise request is easier to answer', 'Instead of asking whether an order is on track, identify the quantity, location, event, and date you need. Separate a request for information from a claim that the supplier has already promised it. This keeps a firm commercial discussion accurate even when the missing date is inconvenient.'),
    a='''What has the supplier confirmed? | Receipt of order P46, not a shipping date | Dispatch of all 500 units | Warehouse receipt on October 12 | Reserved capacity and transit time | The brief supplies acknowledgment only and explicitly leaves timing and capacity unconfirmed.
What does October 12 refer to? | The buyer's required warehouse-receipt date | The supplier's confirmed departure date | The date all units were already delivered | Tomorrow's update appointment | The requested event is receipt at the buyer's warehouse, which differs from dispatch.
What is promised for tomorrow at noon? | An update | Shipment of 500 units | Arrival at the warehouse | A completed supplier audit | The message schedules a status response, not a physical movement of the goods.''',
    vocabulary='''procurement | The process of sourcing and obtaining required goods or services. | coordinate procurement
purchase order | A buyer's order identifying goods, quantities, and relevant terms. | issue a purchase order
order acknowledgment | Confirmation that an order has been received or accepted as stated. | clarify the order acknowledgment
requested date | The date a party asks another party to meet. | distinguish requested and committed dates
committed date | A date a party has explicitly agreed to meet within stated terms. | obtain a committed date
ship date | The date goods leave the specified shipping point. | confirm the ship date
receipt date | The date goods arrive and are received at the stated location. | specify the required receipt date
supplier lead time | The time between defined order and supply events. | verify supplier lead time
transit time | The time spent moving goods between specified points. | confirm transit time
order line | A separate item-and-quantity entry within an order. | review each order line
partial shipment | Delivery of only part of the ordered quantity in one dispatch. | propose a partial shipment
backorder | Ordered demand that cannot yet be fulfilled as required. | track a backorder
allocation | Assignment of limited supply to particular orders or customers. | confirm supply allocation
capacity commitment | A confirmed assignment of production capability for a specified need. | secure a capacity commitment
expediting | Action to accelerate or closely follow a delayed supply activity. | request expediting
minimum order quantity | The smallest quantity a supplier will accept under specified terms. | review the minimum order quantity
request for quotation | A buyer's request for a priced offer against defined requirements. | issue a request for quotation
quotation validity | The period or conditions under which a supplier's offer remains open. | confirm quotation validity
supplier scorecard | A structured summary of supplier performance against defined measures. | review the supplier scorecard
on-time delivery | Delivery within the agreed timing definition and tolerance. | define on-time delivery
on-time in-full | Delivery meeting both the agreed timing and quantity requirements. | measure on-time in-full
service-level agreement | An agreement defining specified service commitments and measures. | review the service-level agreement
commercial escalation | Referral of an unresolved supply issue to the appropriate decision level. | initiate a commercial escalation
status checkpoint | An agreed point for obtaining an updated status. | set a status checkpoint''',
    precision='Order acknowledged does not specify which dates or quantities have been accepted. Ask what the acknowledgment covers. A requested warehouse-receipt date needs a compatible dispatch plan and transit basis; neither is established in this case.',
    precision_extra='Tomorrow at noon is a status checkpoint, not a ship date. A proposed partial shipment must identify quantities, dates, and any remainder. Do not improve a supplier score by replacing the agreed performance basis after an order is late.',
    phrases='''Name the order | This concerns P46 for 500 units.
Clarify acknowledgment | Does your acknowledgment confirm receipt only, or specific quantities and dates?
State the required event | We need warehouse receipt by October 12.
Separate dispatch | A ship date is not the same as a warehouse-receipt date.
Request the commitment | Please confirm the quantity and committed ship date for each line.
Identify missing capacity | Is capacity allocated to this order, or still under review?
Ask about transit | What transit assumption supports the proposed arrival?
Clarify the update | Tomorrow at noon is the response time, not a dispatch commitment.
Keep planning honest | We cannot enter a confirmed receipt date without a supported supply plan.
Explore a partial | A partial shipment may help if quantities and the remainder are explicit.
Preserve the total | Show how the proposed shipments add up to all 500 units.
Ask for the constraint | What prevents you from confirming the date now?
Escalate constructively | Please involve the person who can confirm allocation and timing.
Define the measure | Are we scoring departure or receipt, and against which agreed date?
Avoid an invented promise | I will report the date as unconfirmed until your commitment is clear.
Close the checkpoint | Please send the status tomorrow at noon even if the final date remains open.''',
    notes='''Acknowledged | Can mean received rather than scheduled; ask what is confirmed.
By | Sets a latest time for a specified event; name the event.
Committed | More definite than proposed or estimated, but still governed by the actual agreement.
Partial | Requires a quantity and a plan for what remains.
On time | Needs the agreed date, event, location, and tolerance.
Update | A communication event, not a physical shipment milestone.''',
    d='''Which internal status is accurate now? | P46 acknowledged; ship date, capacity, and transit basis unconfirmed. | P46 confirmed for warehouse receipt October 12. | All 500 units dispatched tomorrow at noon. | The supplier has failed a confirmed date that is not supplied. | The status distinguishes known acknowledgment from the unresolved planning inputs without inventing a promise or breach.
Which request would best clarify the missing commitment? | Please identify the quantity, departure location, committed ship date, and transit basis for warehouse receipt. | Please confirm your acknowledgment number; we will derive arrival from that. | Please repeat October 12 as the requested date without checking production allocation. | Please confirm noon tomorrow as dispatch because it is the next appointment. | Quantity, event, location, timing, and transit assumptions address the actual planning gap; a receipt acknowledgment or response time does not.
The supplier proposes 200 units first and 300 later. What still needs clarification? | Dates, locations, terms, and status for both shipments | Whether 200 plus 300 equals 500 | Whether a partial shipment means all units already arrived | Whether no remainder exists | The quantities reconcile, but a usable plan still needs the timing and conditions of both movements.
How should tomorrow's noon appointment be reported? | Supplier status update due; shipment date still unconfirmed | Guaranteed dispatch at noon | Guaranteed receipt at noon | Automatic order cancellation at noon | The supplied promise concerns communication and must not be relabeled as a shipment event.''',
    dialogue='''Keiko | Thank you for acknowledging P46. We ordered five hundred units and need them at our warehouse by October twelve, but your message does not include a ship date.
Luis | The [[order acknowledgment::The acknowledgment confirms receipt of P46 here, not a shipping or delivery date.]] confirms receipt of the order. It does not yet confirm allocation or dispatch timing, and I do not want you to mistake it for that commitment.
Keiko | Just to be clear, October twelve is our required warehouse receipt date. A shipment leaving your site that day would not meet the request.
Luis | Understood. That is your required [[receipt date::The receipt date concerns arrival and receipt at the buyer's warehouse, distinct from departure from the supplier.]]. We need a compatible dispatch plan and transit basis before I can tell you whether we can support it.
Keiko | Your note also says tomorrow at noon. Our planner read that as the time the order would ship, but I think you meant the next response.
Luis | Correct. It is a [[status checkpoint::The noon checkpoint is a promise to provide information, not a promise that the goods will move then.]]. I will provide an update then; it is not a promise that five hundred units will leave at noon.
Keiko | Please call at noon even if the date is still open. Tell us what is unresolved and who is working on it so we can update production.
Luis | I will. The [[capacity commitment::The capacity commitment is not yet confirmed, so production capability cannot be treated as assigned to P46.]] is still under review. I need the responsible planning team to confirm what capacity can be assigned to this order.
Keiko | When you have that assessment, please identify the quantity and timing for each item line. A single general date could hide different availability across the order.
Luis | I will report each [[order line::An order line identifies a specific item and quantity, allowing different availability to be stated precisely.]] separately where timing differs. The total needs to remain five hundred, with any split clearly linked to the original order quantities.
Keiko | A split could help our operations, but only if it is a real proposal with dates. Two hundred first and three hundred later would not be enough by itself.
Luis | Yes. A [[partial shipment::A partial shipment sends only part of the order and requires a clear plan for both that quantity and the remainder.]] needs quantities, timing, and the remaining balance. I will not describe a possible split as though it has already been approved or dispatched.
Keiko | We also need to know the dispatch location and what the transport estimate includes. Otherwise a proposed departure date may not support the required warehouse arrival.
Luis | The [[transit time::Transit time describes movement between specified points and must be defined before deriving an arrival plan.]] basis must be explicit. We should identify the relevant route and conditions rather than assume a generic number covers every movement and receiving step.
Keiko | Then we can distinguish proposals from commitments. Our internal schedule should use the same status wording.
Luis | Exactly. I will label a [[committed date::A committed date is an explicit agreed commitment, distinct from the buyer's request or an unconfirmed estimate.]] only when the relevant commitment is established. Until then, the requested warehouse date and our unconfirmed supply timing must remain separate.
Keiko | If the planning team cannot resolve allocation, please involve the right decision maker. We need a practical next route without accusing anyone of breaking a date not yet promised.
Luis | I will use the [[commercial escalation::Commercial escalation routes the unresolved allocation and timing question to someone with the appropriate decision authority.]] process if needed. The update will identify the constraint and owner rather than replace the missing date with a vague assurance.
Keiko | For performance reporting later, let's also agree whether we measure dispatch or warehouse receipt. Moving between those definitions would make on-time performance misleading.
Luis | Agreed. [[On-time delivery::On-time delivery needs a defined event, agreed date, location, and tolerance rather than a changing interpretation after the event.]] needs a fixed basis. For now, report P46 as acknowledged with timing unconfirmed, and expect my status response tomorrow at noon.''',
    transfer_title='An update is not a departure',
    transfer_setup='A supplier acknowledges an order for 80 units. Receipt is requested on Friday. The supplier promises a status response on Tuesday but has not confirmed dispatch.',
    transfer='''Buyer: "Friday is our requested receipt ___." | date | Friday refers to arrival at the buyer's location, not confirmed dispatch.
Supplier: "Tuesday is the promised status ___." | response | The supplier has promised information on Tuesday rather than movement of goods.
Buyer: "The ship date remains ___." | unconfirmed | No dispatch commitment is supplied in the scenario.
Supplier: "Acknowledgment alone does not establish ___." | delivery | Receiving the order does not demonstrate that the goods were shipped or received.''',
    rehearsal=["Read turns 1-10, clearly distinguishing warehouse receipt by October 12 from tomorrow's noon status response.","Switch roles for turns 11-20. Stress the requested shipment quantities, departure dates, and unconfirmed transit basis.","Complete and check the transfer. Repeat Tuesday as an update commitment and Friday as requested receipt, without adding a dispatch promise."]))


BOOK['units'].append(unit(
    title='Inventory, Safety Stock, and Service Levels',
    scene='Plenty of inventory, none of these items available',
    skill='Explain item-level availability and service measures without treating a high total balance or safety-stock policy as proof of fulfillment.',
    brief='Inventory planner Elena and distribution manager Omar review a warehouse with a total inventory value of two million dollars. Item A has 40 units on hand, all allocated to existing orders. Item B has 80 units on hand, all blocked by a quality hold. New orders for both items remain unfilled. No available substitute or confirmed replenishment date is supplied. Elena must explain why the headline value does not resolve these shortages and distinguish physical stock from stock available to promise.',
    cast='Elena | Inventory planner\nOmar | Distribution manager',
    culture=('Answer the question at the right level', 'A manager may ask how shortages are possible when inventory is high. Start by separating value, item identity, location, and usability. This turns a seeming contradiction into a concrete allocation and replenishment discussion without implying that all existing stock is useless or every policy has failed.'),
    a='''How many A units are available to the new orders under the supplied facts? | Zero, because all 40 are allocated | Forty, because they are physically present | Eighty, from item B | Two million units | The forty A units are already assigned, and no reallocation is authorized in the brief.
How many B units are currently available under the stated quality status? | Zero, because all 80 are blocked | Eighty, because the total value is high | Forty, because A is allocated | An unknown amount automatically released by demand | The quality hold blocks all eighty B units; demand does not supply release authorization.
Why does the total value not resolve the shortages? | Value aggregates different items and states and does not establish available A or B units. | Dollars can be shipped as either product. | All inventory must be physically absent. | Every stockout proves the warehouse has zero total inventory. | A high aggregate value can coexist with no available stock for specific requested items.''',
    vocabulary='''stock-keeping unit | A distinct inventory item identifier, commonly abbreviated SKU. | analyze each stock-keeping unit
on-hand inventory | The quantity physically recorded at the stated location. | reconcile on-hand inventory
available inventory | Stock usable for the specified demand after relevant restrictions. | confirm available inventory
allocated stock | Stock assigned to particular demand or orders. | review allocated stock
blocked stock | Stock restricted from use under a defined status. | identify blocked stock
quality hold | A restriction pending the required quality review or decision. | respect a quality hold
available to promise | The quantity that can be committed under the defined supply-and-demand rules. | calculate available to promise
inventory position | A defined balance considering on-hand stock, incoming supply, and demand commitments. | state the inventory-position basis
safety stock | Buffer inventory intended to protect against specified uncertainty. | review safety-stock assumptions
cycle stock | Inventory supporting normal demand between replenishments. | distinguish cycle stock
reorder point | The inventory level or position that triggers replenishment under a policy. | review the reorder point
replenishment lead time | The elapsed time from a defined replenishment trigger to usable receipt. | measure replenishment lead time
stockout | Inability to supply an item when required from the relevant inventory. | investigate stockouts
fill rate | The share of defined demand filled under the stated service measure. | define the fill-rate basis
cycle service level | The probability of avoiding a stockout during a defined replenishment cycle. | distinguish cycle service level
backorder | Demand retained for later fulfillment after it cannot be supplied as required. | track backorders
inventory turnover | A period's inventory usage or cost relative to the defined average inventory. | interpret inventory turnover
days of supply | Inventory expressed as coverage of demand at a stated rate. | calculate days of supply
slow-moving stock | Inventory used or sold less frequently than the defined threshold. | identify slow-moving stock
obsolete stock | Inventory no longer suitable or expected to meet its intended demand. | assess obsolete stock
ABC analysis | Grouping items by a selected importance measure, often annual consumption value. | perform ABC analysis
item segmentation | Grouping items by relevant demand, supply, or service characteristics. | refine item segmentation
inventory accuracy | Agreement between recorded and actual inventory under the defined measure. | improve inventory accuracy
reallocation | Authorized reassignment of stock from one demand to another. | assess a reallocation request''',
    precision='Physical presence does not establish free availability. All 40 A units are allocated; all 80 B units are blocked. Neither group is available for the new orders on the supplied facts. A total dollar value cannot be substituted for an item quantity.',
    precision_extra='Safety stock is a buffer against defined uncertainty, not a guarantee against every stockout. Fill rate and cycle service level measure different things. Name the demand unit, time period, location, restrictions, and service definition before comparing percentages.',
    phrases='''Start with the distinction | The value total does not show availability for these two items.
State A's position | All 40 A units are allocated to existing orders.
State B's restriction | All 80 B units remain blocked by the quality hold.
Keep available quantity explicit | Neither item has available stock for these new orders on the current facts.
Avoid an unauthorized release | New demand does not remove the quality restriction.
Avoid double-promising | We cannot promise the same allocated stock to two orders.
Request item-level detail | Show item, location, quantity, allocation, and status.
Clarify incoming supply | A planned receipt is not yet usable on-hand inventory.
Name the service measure | Are we measuring units filled, complete orders, or stockout-free cycles?
Keep the buffer realistic | Safety stock reduces exposure to specified uncertainty; it is not a universal guarantee.
Check policy inputs | Review demand variability and replenishment assumptions for the affected items.
Separate slow stock | High value in another item does not supply a missing unit of A.
Define any reallocation | A priority change needs an authorized allocation decision.
Avoid a premature policy fix | A larger buffer proposal needs an item-specific basis.
State the missing date | No confirmed replenishment date is supplied.
Close the explanation | Report the headline value and the item-level shortage together.''',
    notes='''On hand | Describes recorded physical quantity, not necessarily free usable quantity.
Available | Must specify the demand, location, and restrictions.
Allocated | Assigned already; do not silently promise it again.
Blocked | A controlled restriction, not a suggestion to ignore when demand rises.
Service level | An umbrella phrase; identify the actual measure.
Coverage | Depends on the chosen demand rate and the usable stock basis.''',
    d='''Which management summary is accurate? | Inventory value is high, but A is fully allocated and B fully blocked, leaving no available stock for the new orders. | Two million dollars proves every order can be filled. | A and B have 120 freely available units. | B can be shipped because its units are physically present. | The summary distinguishes the aggregate value from the specific allocation and quality restrictions.
Another item has 60 on hand, 35 allocated, and 10 blocked, with no overlap. What remains free? | 15 units | 25 units | 45 units | 60 units | Subtracting the separate allocated and blocked quantities from sixty leaves fifteen units.
Which claim about safety stock is defensible? | It buffers specified uncertainty but does not guarantee that every item will always be available. | It guarantees no stockouts under all conditions. | It removes the need to measure lead time. | It turns blocked stock into available stock. | A buffer depends on assumptions and cannot override status restrictions or every demand and supply outcome.
A later report shows 95% unit fill rate. Which conclusion needs a separate measure? | Ninety-five percent of replenishment cycles had no stockout. | Five percent of measured demand units were not filled under that report's definition. | The unit measure concerns the share of demand filled. | The reporting definition matters when interpreting the result. | A unit-based fill rate and a stockout-free cycle measure use different denominators; one percentage cannot establish the other.''',
    dialogue='''Omar | We have two million dollars of inventory, yet new orders for A and B are unfilled. The total looks healthy, so I need a clear explanation.
Elena | Start at the [[stock-keeping unit::A stock-keeping unit identifies the particular item, which the aggregate dollar balance does not distinguish.]] level. Value across many items does not establish that the specific products requested are available in the right state and location.
Omar | The record shows forty units of A physically here. Why can those not satisfy the new demand if the items are already in the building?
Elena | They are [[allocated stock::The forty A units are already assigned to existing orders, so they are not free for the new demand.]]. All forty belong to existing orders under the current allocation; promising them again would create two commitments against the same quantity.
Omar | Can we display the allocation beside the forty-unit count? At the moment, the first screen makes those units look available to anyone taking a new order.
Elena | Exactly. [[On-hand inventory::On-hand inventory records physical quantity but does not by itself account for allocation or other use restrictions.]] and available inventory are different views. The same distinction matters for B, although its restriction comes from quality status rather than allocation.
Omar | B has eighty units on hand, but the status is blocked. I assume the new order does not give distribution authority to remove that status.
Elena | Correct. The [[quality hold::The quality hold blocks B from use pending the required decision and is not removed by customer demand.]] remains in force. We cannot treat the eighty units as usable merely because they have value or are physically present.
Omar | So neither item has free stock for the new orders on the current facts. That does not mean the whole warehouse is empty or all our stock is obsolete.
Elena | Right. Our [[available to promise::Available to promise concerns what can be committed under the relevant supply and demand rules, not the gross physical balance.]] assessment must respect allocations and restrictions. We also have no confirmed replenishment date or available substitute in this briefing.
Omar | Should we simply increase safety stock for both items? The repeated shortages suggest a problem, but I do not know whether a larger buffer is the appropriate response.
Elena | Review the [[safety stock::Safety stock is a buffer based on uncertainty assumptions, not an automatic cure for allocations, holds, or every shortage.]] assumptions rather than assume the answer. Demand variation, supply timing, and the reason for unavailable stock need item-specific examination.
Omar | Lead-time assumptions may also matter. A receipt that arrives later than expected could undermine the intended buffer, even if the original quantity calculation looked reasonable.
Elena | Yes. Use the actual [[replenishment lead time::Replenishment lead time includes the defined interval to usable receipt, which can affect inventory-policy assumptions.]] definition, including when stock becomes usable. A shipment in transit is not the same as inventory available at the required location.
Omar | Our service dashboard says ninety-five percent, but the label does not say whether that means units supplied or orders supplied completely. That makes comparisons difficult.
Elena | Define the [[fill rate::Fill rate measures fulfilled demand under a specified unit and timing definition, so the basis must be stated.]] basis explicitly. Units, order lines, and complete orders can produce different percentages, and none should be silently substituted for the others.
Omar | The replenishment report counts cycles with no shortage. Should that have a separate label so our teams stop comparing it directly with the demand-fill figure?
Elena | That is [[cycle service level::Cycle service level concerns avoiding stockouts during replenishment cycles rather than the share of demand units filled.]]. It is not automatically equal to a demand-fill percentage, so a shared label of service level can conceal an important difference.
Omar | I will explain the two-million-dollar total alongside the item-specific restrictions. Any proposal to move A from existing orders will also need a clear priority decision.
Elena | Yes, any [[reallocation::Reallocation changes which demand receives stock and requires an authorized decision rather than a second promise of the same units.]] must be authorized and visible. For now, report A fully allocated, B fully blocked, and replenishment unconfirmed rather than imply the headline value resolves the shortages.''',
    transfer_title='Free quantity has a status basis',
    transfer_setup='An item has 100 units on hand. Sixty are allocated and 25 are blocked, with no overlap. No receipt is confirmed.',
    transfer='''Planner: "The physical on-hand quantity is one ___." | hundred | The physical record contains 100 units before restrictions are deducted.
Manager: "The allocated quantity is ___." | sixty | Sixty units are assigned to existing demand in the supplied facts.
Planner: "The remaining free quantity is ___." | fifteen | 100 minus the separate 60 allocated and 25 blocked units leaves fifteen.
Manager: "Future replenishment remains ___." | unconfirmed | The scenario supplies no confirmed incoming receipt or replenishment date.''',
    rehearsal=["Read the corrected dialogue, contrasting physically present with available for new orders for both A and B.","Switch roles for turns 11-20. Keep fill rate, cycle service level, and an authorized reallocation distinct.","Complete and check the transfer. Say the quantities in order: 100 on hand, 60 allocated, 25 separately blocked, 15 free."]))

BOOK['units'].append(unit(
    title='Warehousing and Fulfillment',
    scene='Shipments and the closing queue',
    skill='Reconcile a changing order queue, distinguish gross completions from net reduction, and avoid unsupported claims about order age or service.',
    brief='Warehouse lead Pavel and customer-operations manager Zoe review a shift that began with 300 open orders. Fifty new orders arrived during the shift, and 220 orders were fully shipped and closed. There were no cancellations, reopenings, or partial closures. The data do not identify which shipped orders came from the opening queue. A report says 80 remain and the oldest orders are cleared. Pavel and Zoe must correct the balance and separate the known throughput from the unsupported age and service claims.',
    cast='Pavel | Warehouse lead\nZoe | Customer-operations manager',
    culture=('Reconcile before celebrating', 'A strong output number deserves recognition, but the closing queue must include new arrivals and other changes. State the arithmetic openly and distinguish volume from customer service. A team can ship many orders while particular older or priority orders still need attention.'),
    a='''How many orders remain open? | 130 | 80 | 220 | 350 | Opening 300 plus 50 arrivals minus 220 completed orders equals 130 open orders.
What is the net reduction from the opening queue total? | 170 orders | 220 orders | 50 orders | 300 orders | The open total falls from 300 to 130, a net reduction of 170 after new arrivals.
What is unknown about the shipped orders? | Which were from the opening queue | Whether 220 were fully closed | Whether 50 new orders arrived | Whether cancellations occurred | The brief explicitly leaves the cohort identity of shipped orders unspecified.''',
    vocabulary='''order backlog | Orders still awaiting the defined fulfillment completion. | reconcile the order backlog
opening balance | The quantity at the start of the reporting period. | state the opening balance
closing balance | The quantity at the end after all relevant movements. | calculate the closing balance
order inflow | New orders entering the queue during a period. | track order inflow
gross completions | Total completed orders before accounting for new arrivals or other queue changes. | report gross completions
net reduction | The decrease in the total balance after additions and removals. | distinguish net reduction
fulfillment cycle | The steps from accepted order through the defined delivery or completion point. | map the fulfillment cycle
order release | Authorization to begin warehouse processing for an order. | schedule order release
wave picking | Grouping orders into planned picking batches or time windows. | organize wave picking
pick face | The location from which items are selected for orders. | replenish the pick face
pick accuracy | The correctness of selected items and quantities under the defined measure. | monitor pick accuracy
short pick | A pick that cannot supply the full requested quantity. | investigate a short pick
packing verification | Checking packed items against order and shipping requirements. | complete packing verification
shipment confirmation | A recorded confirmation of the defined dispatch event. | verify shipment confirmation
partial fulfillment | Completion of only part of an order. | flag partial fulfillment
order aging | The time orders have remained open under the defined starting point. | review order aging
due-date priority | Ranking work by agreed completion or delivery deadlines. | assess due-date priority
cutoff time | The latest time for inclusion in a specified processing or dispatch cycle. | confirm the cutoff time
warehouse management system | Software managing warehouse inventory and operations, abbreviated WMS. | reconcile the warehouse management system
scan event | A recorded identification action at a process step. | trace scan events
exception queue | Work set aside for problems requiring resolution. | review the exception queue
dock capacity | The available capability for loading, unloading, and related dock work. | assess dock capacity
labor capacity | The work volume supported by available personnel under stated conditions. | review labor capacity
order cohort | A defined group of orders, such as those open at the start of a shift. | analyze an order cohort''',
    precision='300 opening orders plus 50 arrivals minus 220 completed orders equals 130 closing orders. Gross completions are 220; the net queue reduction is 170. Ignoring arrivals produces the incorrect balance of 80.',
    precision_extra='The data do not identify which order cohort shipped. You cannot conclude that all oldest orders were cleared or that 220 of the original 300 shipped. A completed shipment count also does not establish on-time delivery or pick accuracy.',
    phrases='''Define the starting queue | We began the shift with 300 open orders.
Include arrivals | Fifty new orders entered during the shift.
State completion precisely | Two hundred twenty orders were fully shipped and closed.
Reconcile the ending queue | The closing balance is 130 open orders.
Separate gross and net | We completed 220 orders, but the queue fell by 170.
Explain the correction | Eighty omits the 50 new arrivals.
Keep the cohort open | We do not know which completed orders came from the opening queue.
Avoid an age claim | The total does not prove the oldest orders were cleared.
Request the age view | Show the remaining orders by age and due date.
Separate service measures | Shipped volume does not by itself establish on-time delivery.
Preserve order units | Do not mix orders, order lines, units, and cartons.
Clarify partials | This report counts only fully closed orders.
Check exceptions | Identify unresolved stock, documentation, or address issues separately.
Reconcile the system | Match the completion events to the warehouse record.
Keep the plan conditional | The next-shift plan needs current capacity and priority information.
Close the report | Present arrivals, completions, ending balance, and remaining exceptions together.''',
    notes='''Shipped | Define the event; it does not necessarily mean delivered to the customer.
Closed | A system status that needs a clear completion rule.
Remaining | Requires additions as well as removals in the calculation.
Oldest | Refers to order age, which a total alone cannot establish.
Throughput | Volume per stated period, not a synonym for service quality.
Cohort | A defined group whose members must be tracked to make group-level claims.''',
    d='''Which closing report is correct? | 300 opening + 50 new - 220 closed = 130 open | 300 - 220 = 80 open, ignoring new orders | 300 + 220 - 50 = 470 open | 220 closed means the opening queue is fully cleared | The correct balance includes both the new arrivals and the completed orders.
Why is net reduction not 220? | Fifty new orders offset part of the 220 completions. | Closing an order always increases the queue. | The 220 shipments were all partial closures. | Cancellations account for the difference. | The case has fifty additions and no other adjustments, leaving a net reduction of 170.
What is the possible number of opening-queue orders still open after this shift? | Between 80 and 130; the exact count needs order identifiers. | Exactly 80, because all 220 completions must belong to the opening queue. | Exactly 130, because none of the 50 new orders can have shipped. | Zero, because gross completions exceed the new arrivals. | At most 50 of the 220 completions can be new, so 170 to 220 can be opening orders. Subtracting that range from 300 leaves 80 to 130; age priority remains unknown.
A later shift starts at 130, receives 40, and fully closes 90, with no other changes. What remains? | 80 open orders | 40 open orders | 90 open orders | 180 open orders | The balance is 130 plus 40 minus 90, leaving eighty open orders.''',
    dialogue='''Zoe | I am about to send customer service the shift report. It says eighty orders remain. Can you check it before I send the update?
Pavel | It omits the [[order inflow::The fifty new orders must be added when calculating the closing queue, not omitted from the balance.]]. Fifty new orders arrived after the opening count of three hundred. We also fully shipped and closed two hundred twenty.
Zoe | Right, I subtracted the shipments but forgot the additions. Three hundred plus fifty, minus two hundred twenty. That leaves one hundred thirty, not eighty.
Pavel | Yes, that is the [[closing balance::The closing balance is 300 opening plus 50 new minus 220 closed, which equals 130 open orders.]]. There were no cancellations or reopenings, so we do not need another adjustment to reconcile these totals.
Zoe | Should I reduce the shipment figure to one hundred seventy as well? That is how much smaller the queue is now.
Pavel | No. Keep two hundred twenty as [[gross completions::Gross completions are the 220 fully closed orders, before the queue effect of new arrivals is included.]]. Those orders really were completed. The extra fifty arrived during the same shift; they do not cancel completed work.
Zoe | Understood. Two hundred twenty completed, fifty added, and the open queue fell by one hundred seventy. I will label each number separately.
Pavel | Call the last figure the [[net reduction::Net reduction is the change in the open balance, 300 minus 130, after accounting for additions.]]. Otherwise the next shift may think one hundred seventy was our total output rather than the change in unfinished work.
Zoe | There is another sentence: all the oldest orders are cleared. The completed total is large, but I cannot find the order identifiers behind that claim.
Pavel | We need the [[order cohort::An order cohort identifies a specific group, and the supplied totals do not show which shipped orders belonged to the opening group.]] detail. We cannot tell from these totals how many completions belonged to the opening queue or which were new arrivals.
Zoe | Then I will remove that sentence. Could you send the remaining order ages and due dates before customer service contacts individual customers?
Pavel | I will pull the [[order aging::Order aging shows how long specific orders remain open, which cannot be inferred from the aggregate queue total.]] report. It can show who is still waiting; the single remaining-order total cannot answer that question.
Zoe | Include the unresolved address and stock issues separately. Customer service needs to know whether an order is ready to process or waiting on somebody else.
Pavel | I will add the [[exception queue::The exception queue groups unresolved problems for the appropriate follow-up rather than treating all remaining orders as identical work.]] and its assigned owners. I will not describe those orders as ready until their blocking issues are resolved.
Zoe | One more point: does fully shipped mean delivered on time? The report heading currently calls these successful deliveries.
Pavel | No. A [[shipment confirmation::Shipment confirmation records the defined dispatch event, not whether a promised arrival or timing requirement was met.]] records dispatch under our definition. We need the agreed dates and the relevant delivery events before claiming on-time arrival.
Zoe | I will change that heading too. We are counting fully closed orders, not cartons, individual units, or customer deliveries.
Pavel | Correct. This count excludes [[partial fulfillment::Partial fulfillment is not counted as a fully closed order in this case, so the completion rule must remain explicit.]]. Shipping one carton from an unfinished order does not make that order one of our two hundred twenty closures.
Zoe | I have corrected eighty to one hundred thirty, kept the completed count, and removed the oldest-cleared and on-time-delivery claims. Please check the underlying events.
Pavel | I will reconcile them against the [[warehouse management system::The warehouse management system provides operational records to reconcile against the stated arrivals and completion events.]]. Customer service will receive the corrected balance and the age and exception details, with any unresolved differences identified.''',
    transfer_title='Count every movement in the queue',
    transfer_setup='A shift starts with 100 open orders, receives 30, and fully closes 80. There are no other changes, and shipped-order ages are not supplied.',
    transfer='''Lead: "The closing balance is ___ orders." | fifty | One hundred plus thirty minus eighty leaves fifty open orders.
Colleague: "Gross completions are ___." | eighty | Eighty orders were fully closed during the shift before accounting for new arrivals.
Lead: "The new-order inflow is ___." | thirty | Thirty new orders entered the queue during the shift.
Colleague: "The oldest-order status is still ___." | unknown | The totals do not identify the ages of the completed or remaining orders.''',
    rehearsal=["Read turns 1-10 and repeat Zoe's corrected balance: 300 plus 50 minus 220 equals 130.","Switch roles for turns 11-20. Stress the phrases that withhold claims about the oldest orders and on-time delivery.","Complete and check the transfer. Say 50 remaining and 80 completed, then read the line leaving order ages unknown."]))


BOOK['units'].append(unit(
    title='Freight, Routing, and Carrier Delays',
    scene='Wednesday is still an estimate',
    skill='Give a useful delay update while separating a carrier estimate, confirmed transport events, appointment timing, and an authorized contingency.',
    brief='Logistics coordinator Nikhil and customer planner Dana review a fictional shipment. The carrier currently estimates warehouse arrival on Wednesday, but departure has not been confirmed. Dana needs the goods for a Wednesday 14:00 production start and asks for a guarantee. An expedited route is only being assessed; its capacity, extra cost, and arrival timing are unconfirmed. Nikhil has arranged a carrier status update for Tuesday at 16:00. He must state what is known without treating that update or the alternative route as a delivery promise.',
    cast='Nikhil | Logistics coordinator\nDana | Customer planner',
    culture=('Be useful without false precision', 'A customer asking for certainty often needs a planning decision. State the latest estimate, the missing milestone, the consequence for the customer, and the next update. Avoid filling the gap with a precise arrival time that no confirmed movement or service commitment supports.'),
    a='''What is the current arrival status? | Estimated Wednesday warehouse arrival, with departure unconfirmed | Guaranteed arrival before Wednesday 14:00 | Confirmed warehouse delivery | A completed departure proving every later milestone | The carrier supplies an estimate, while a key preceding movement has not been confirmed.
What does Tuesday 16:00 represent? | A carrier status update | Guaranteed departure | Guaranteed warehouse arrival | Approved expedited transport | The appointment concerns information, not the physical shipment event.
What is known about the expedited route? | It is being assessed; capacity, cost, and timing are unconfirmed. | It is booked and guaranteed free. | It has already delivered the goods. | It automatically meets Dana's production time. | The alternative remains a proposal with multiple unresolved conditions.''',
    vocabulary='''estimated time of arrival | A forecast arrival time for a specified destination, abbreviated ETA. | qualify the estimated time of arrival
estimated time of departure | A forecast departure time from a specified location, abbreviated ETD. | update the estimated time of departure
actual departure | The confirmed time the shipment left the stated location. | confirm actual departure
actual arrival | The confirmed time the shipment reached the stated point. | record actual arrival
carrier | The organization transporting goods under the relevant arrangement. | request a carrier update
freight forwarder | A party arranging transport and related logistics services. | coordinate with the freight forwarder
consignor | The party sending goods under the transport record. | identify the consignor
consignee | The party named to receive goods under the transport record. | confirm the consignee
bill of lading | A transport document evidencing receipt and carriage terms, with functions varying by type. | review the bill of lading
air waybill | A nonnegotiable document used for air-cargo carriage. | verify the air waybill
transport milestone | A defined event used to track shipment progress. | confirm the transport milestone
tracking exception | A reported departure from the expected shipment process. | investigate a tracking exception
transshipment | Transfer of goods between transport services during a journey. | assess transshipment risk
routing | The planned path and transport connections for a shipment. | review the routing
last mile | The final transport leg to the delivery destination. | coordinate the last mile
delivery appointment | An agreed receiving time slot at the destination. | confirm the delivery appointment
proof of delivery | Evidence documenting the defined delivery event. | obtain proof of delivery
expedited freight | Transport arranged to reduce delivery time under specified conditions. | assess expedited freight
premium freight cost | Additional transport cost for a higher-cost or urgent service. | authorize premium freight cost
capacity booking | A reservation of transport space under the applicable terms. | confirm the capacity booking
demurrage | A charge for specified excess terminal or port use under applicable terms. | review demurrage terms
detention | A charge for specified extended equipment use under applicable terms. | check detention exposure
Incoterms rule | An ICC trade rule allocating specified delivery obligations, costs, and risks. | identify the agreed Incoterms rule
named place | The specific location stated with the relevant trade or delivery term. | specify the named place''',
    precision='An ETA is an estimate for a stated event and place. It is not proof of departure or a guarantee that goods will be usable for a production start. A warehouse appointment and a confirmed arrival are also different events.',
    precision_extra='An expedited option needs capacity, timing, cost, and authorization before it becomes a plan. Incoterms rules allocate specified obligations, costs, and risks; they do not prove physical movement or themselves guarantee an arrival time. Read the actual contract and named place.',
    phrases='''State the latest estimate | The carrier currently estimates warehouse arrival on Wednesday.
Name the missing event | Departure has not yet been confirmed.
Avoid an unsupported guarantee | I cannot confirm arrival before your 14:00 production start from the available information.
Acknowledge the consequence | I understand that the uncertainty affects your production plan.
Clarify the destination | This estimate refers to your warehouse, not merely the destination terminal.
Request a milestone | Please provide the confirmed departure event and its source.
Separate appointment | A receiving slot is not proof that the vehicle will arrive in that slot.
Describe the alternative | We are assessing expedited routing, not reporting a completed booking.
Keep cost visible | Any premium cost needs the appropriate authorization.
Qualify capacity | Space must be confirmed before we rely on the alternative.
Set the communication | The next carrier status update is Tuesday at 16:00.
Preserve update discipline | I will update you then even if the arrival remains uncertain.
Do not relabel | A forecast departure is not actual departure.
Separate trade terms | The agreed trade rule does not itself guarantee Wednesday arrival.
Report changes clearly | State which milestone, estimate, or condition has changed.
Close with the planning basis | Use Wednesday as the current estimate, with the departure dependency explicit.''',
    notes='''Estimated | A forecast based on current information, not a confirmed event.
Actual | A recorded occurrence that needs a clear source and location.
Guaranteed | Requires an actual applicable commitment; do not infer it from an ETA.
Booked | Specify whether capacity is reserved or a request merely submitted.
Arrived | Name the terminal, warehouse, or other location.
Delivered | Identify the contractual or operational event rather than assume every arrival is delivery.''',
    d='''Which customer update is accurate? | Warehouse arrival is estimated Wednesday; departure remains unconfirmed; next update Tuesday 16:00. | Delivery is guaranteed Wednesday before 14:00. | Goods have departed because an ETA exists. | The expedited route is confirmed at no additional cost. | The update preserves the carrier estimate, the missing milestone, and the separate communication commitment.
The system shows ETD Tuesday 10:00 but no departure event. Which wording preserves the distinction? | Departure is estimated for Tuesday 10:00; actual departure is unconfirmed. | The vehicle departed Tuesday 10:00, subject to arrival confirmation. | Departure was confirmed because the system contains a date and time. | Warehouse delivery is booked for Tuesday 10:00, pending unloading. | ETD is an estimated departure time. A populated estimate field is not evidence of completed movement or a receiving appointment.
What is needed before relying on the expedited alternative? | Confirmed capacity, supported timing, cost, and the required authorization | Only a route name in a message | A customer request alone | An Incoterms abbreviation without a booking | The alternative's practical conditions and approval remain unresolved in the brief.
Which statement about an agreed Incoterms rule is accurate? | It allocates specified responsibilities, costs, and risks but does not itself prove arrival or guarantee the ETA. | It always guarantees the next Wednesday delivery. | It automatically replaces a carrier tracking event. | It makes the named place irrelevant. | Trade-rule obligations and physical shipment status are different questions that require different evidence.''',
    dialogue='''Dana | Our production starts Wednesday at fourteen hundred. The carrier estimate says Wednesday, so can you guarantee that the shipment will reach our warehouse before then?
Nikhil | The current [[estimated time of arrival::The ETA is a forecast arrival at the warehouse, not a guarantee of a particular time.]] is Wednesday, but no time before fourteen hundred is confirmed. Departure itself has not been confirmed, which remains an important dependency.
Dana | Please put that in the update to production. They are planning around fourteen hundred, not simply some time on Wednesday.
Nikhil | I will state that [[actual departure::Actual departure requires confirmation that the goods left the stated point, which is missing in this case.]] is still unconfirmed. A planned departure or an arrival estimate does not establish that the goods have already begun that leg.
Dana | Does the Wednesday estimate refer to our warehouse or just the destination terminal? That would make a significant difference to whether the goods can support production.
Nikhil | It refers to the warehouse, but the [[last mile::The last mile is the final transport leg to the warehouse and remains part of the estimated arrival plan.]] remains part of the plan to verify. Arrival at an earlier terminal would not by itself complete that final movement.
Dana | We have a receiving slot available. I want to avoid treating that slot as confirmation that the carrier will reach us on schedule.
Nikhil | Correct. A [[delivery appointment::A delivery appointment reserves or agrees a receiving slot but does not prove the vehicle will arrive then.]] describes the receiving arrangement. It does not turn an uncertain transport estimate into a confirmed arrival event.
Dana | The customer-service note mentions a faster alternative. Is that already arranged, or are you still checking whether it could actually improve this shipment's timing?
Nikhil | We are assessing [[expedited freight::Expedited freight is being considered as a faster option, but its practical conditions are not yet confirmed.]]. Capacity, timing, and cost remain unconfirmed, so it would be misleading to describe the option as a booked recovery plan.
Dana | Please show any extra cost before someone commits us to it. A faster route might help, but we need the actual proposal and the appropriate approval.
Nikhil | Any [[premium freight cost::Premium freight cost is the additional expense of the proposed service and needs the required authorization.]] will be explicit. We should not assume that urgency supplies financial authorization or that a quoted service is already available for this shipment.
Dana | And is there actually space on that faster route? I do not want us to approve extra cost for a connection we cannot secure.
Nikhil | Exactly. We need the [[capacity booking::A capacity booking confirms reserved space under its terms, unlike an unconfirmed routing suggestion.]] and supported timing. I will separate a booking request from an actual confirmation in the update.
Dana | The order also names a trade term. Someone suggested that this term guarantees arrival on the estimated day, but I do not think those are the same issue.
Nikhil | They are not. An [[Incoterms rule::An Incoterms rule allocates specified obligations, costs, and risks; it does not itself guarantee an estimated arrival date.]] allocates specified obligations, costs, and risks. It does not itself prove shipment movement or guarantee that the current estimate will be met.
Dana | What can you promise about the next communication? We need a reliable checkpoint even if the transport timing remains uncertain.
Nikhil | The carrier update is Tuesday at sixteen hundred. I will request the next confirmed [[transport milestone::A transport milestone is a defined shipment event whose confirmation can improve the status assessment.]] and tell you what changed, including if departure or the alternative still remains unresolved.
Dana | That gives us an honest planning basis. We will treat Wednesday as the current estimate, keep the production dependency visible, and wait for the confirmed movement update.
Nikhil | Once delivery occurs, we can obtain [[proof of delivery::Proof of delivery documents the actual defined delivery event, unlike an estimate or appointment.]]. Until then, I will distinguish estimates, bookings, confirmed events, and the next communication rather than combine them into a guarantee.''',
    transfer_title='A scheduled pickup is not a completed pickup',
    transfer_setup='Pickup is scheduled for Monday. Arrival is estimated Thursday. No collection event is confirmed, and the next update is Monday at 15:00.',
    transfer='''Coordinator: "Monday's pickup is ___." | scheduled | A planned pickup date does not establish that collection already occurred.
Customer: "Thursday's arrival remains ___." | estimated | The arrival is a forecast rather than a confirmed or guaranteed event.
Coordinator: "Actual collection is not yet ___." | confirmed | The case supplies no evidence of a completed collection event.
Customer: "Fifteen hundred is the next status ___." | update | The time concerns communication, not guaranteed collection or arrival.''',
    rehearsal=["Read turns 1-10, keeping Wednesday's arrival estimate separate from the customer's Wednesday 14:00 production requirement.","Switch roles for turns 11-20. Stress the unresolved cost, booking, and departure conditions and Tuesday's 16:00 update.","Complete and check the transfer. Contrast scheduled pickup, estimated arrival, and an actual collection not yet confirmed."]))

BOOK['units'].append(unit(
    title='Customs, Trade Compliance, and Documentation',
    scene='The invoice and packing list describe different goods',
    skill='Raise a document discrepancy, request verified product facts, and arrange controlled correction without guessing classification or changing facts to fit a document.',
    brief='Trade coordinator Sofia and exporter contact Chen review a fictional US-bound shipment file. The invoice describes stainless-steel bolts; the packing list describes aluminum brackets. Both show 500 pieces, but matching counts do not establish which description is correct. The broker requests clarification before relying on the file. No verified product specification, classification, or origin determination is supplied. Sofia and Chen must obtain the underlying product facts and corrected authorized documents without simply copying one unverified description over the other.',
    cast='Sofia | Trade coordinator\nChen | Exporter documentation contact',
    culture=('Consistency is necessary but not sufficient', 'Two documents can match and still be wrong. State the discrepancy neutrally, then seek the facts that identify the goods. The goal is an accurate, traceable file, not just matching words that make the broker stop asking questions.'),
    a='''What is the discrepancy? | The invoice describes steel bolts while the packing list describes aluminum brackets. | The piece counts differ. | A classification has been confirmed. | Both descriptions have been verified correct for identical goods. | The document descriptions differ in product and material even though both list five hundred pieces.
What do matching counts establish? | Agreement on the stated count, not verification of the product description | Proof both products are identical | Automatic customs release | A correct tariff classification | The same number does not resolve a conflict over what the goods actually are.
What is missing before an accurate correction? | Verified product facts and the appropriate document correction process | A preferred lower duty rate to copy | Permission to guess the material | Proof that the broker can invent the goods' identity | The file needs underlying evidence and authorized correction rather than selection of a convenient description.''',
    vocabulary='''commercial invoice | A transaction document describing goods, value, parties, and relevant terms. | verify the commercial invoice
packing list | A document describing how goods and quantities are packed. | reconcile the packing list
merchandise description | The factual identification and characteristics of the goods. | provide a precise merchandise description
product specification | Technical information defining a product's characteristics. | obtain the product specification
material composition | The substances or materials making up a product. | confirm material composition
end use | The purpose for which the product is intended or used. | clarify the end use
tariff classification | Assignment of goods to an applicable tariff category under the governing rules. | obtain a classification review
Harmonized System | The international goods-classification framework commonly abbreviated HS. | distinguish Harmonized System codes
HTSUS | The Harmonized Tariff Schedule of the United States. | consult the applicable HTSUS provision
country of origin | The country determined as the goods' origin under applicable rules. | verify country of origin
country of shipment | The country from which goods are dispatched. | distinguish country of shipment
customs value | The value determined under the applicable customs valuation rules. | review customs value
declared quantity | The quantity stated in the relevant customs or shipment record. | verify the declared quantity
unit of measure | The basis used to count or measure goods. | confirm the unit of measure
net weight | The weight of goods excluding the specified packaging. | state net weight
gross weight | The weight including the specified goods and packaging. | distinguish gross weight
importer of record | The party responsible for the import entry under applicable law. | identify the importer of record
customs broker | A qualified intermediary conducting customs business under the relevant authorization. | coordinate with the customs broker
entry documentation | The records supporting the import entry process. | review entry documentation
supporting evidence | Records substantiating the information in a declaration or document. | retain supporting evidence
document discrepancy | A conflict between relevant records or stated facts. | resolve a document discrepancy
corrected invoice | An authorized revised invoice addressing an identified error. | request a corrected invoice
revision history | A record of what changed, when, and why. | preserve revision history
customs release | The customs decision permitting goods to proceed under applicable conditions. | confirm customs release''',
    precision='Five hundred pieces on both documents confirms only agreement in the stated count. Bolts and brackets, and stainless steel and aluminum, are materially different descriptions. Neither document is established as correct by the supplied facts.',
    precision_extra='Do not choose a tariff category, origin, or description to obtain a preferred duty result. Accurate product facts must support the relevant qualified review. Shipment country is not automatically origin, and a corrected file is not itself proof of customs release.',
    phrases='''Name the discrepancy | The invoice says stainless-steel bolts; the packing list says aluminum brackets.
Keep the count separate | Both list 500 pieces, but that does not resolve the product identity.
Avoid choosing by convenience | We cannot assume either description is correct without supporting facts.
Request the specification | Please provide the verified product specification and relevant order details.
Clarify composition | Confirm the actual material rather than copying an unverified label.
Check the packing basis | Reconcile the item identifiers and package contents.
Preserve document authority | Ask the responsible issuer to correct the affected document.
Keep history visible | Retain the original and the reason for the correction.
Separate classification | The product description does not by itself complete a tariff review.
Avoid a duty-driven description | The wording must follow the goods, not a preferred duty outcome.
Distinguish origin | Country of shipment does not automatically establish country of origin.
Coordinate review | Provide the verified facts to the broker and responsible import team.
Do not invent a code | Classification needs the applicable facts and qualified review.
Limit the status | The discrepancy is being resolved; customs release is not confirmed.
Check agreement and truth | The corrected documents must match the verified goods, not merely each other.
Close the handoff | Send the authorized corrections with their supporting references.''',
    notes='''Described as | Attributes wording to a document without endorsing its accuracy.
Verified | Requires a source tied to the actual goods.
Matching | Means consistent with another record, not necessarily factually correct.
Origin | A rules-based determination, not simply the dispatch location.
Corrected | Indicates a documented change; it does not imply customs has accepted the entry.
Released | An actual customs status, separate from a completed internal file.''',
    d='''Which message to the exporter is most appropriate? | Please verify the actual product and material, then arrange authorized corrections supported by those facts. | Copy the invoice onto the packing list because invoices are always correct. | Use whichever description produces lower duty. | Keep both descriptions because the counts match. | The message seeks accurate underlying facts and controlled correction rather than an arbitrary choice between conflicting records.
A colleague changes both descriptions to metal parts without checking the goods. What remains unresolved? | The actual product and material; matching vague wording does not verify them. | Only the number of pieces, because the material is now established. | Only the tariff rate, because any shared wording proves identity. | Nothing about the merchandise, because both documents now agree. | Agreement between documents is not verification against the goods. Replacing conflicting specifics with a vague shared label hides rather than resolves the discrepancy.
Which origin statement is accurate? | Shipment country alone does not determine origin; apply the relevant rules to verified facts. | Origin always equals the loading port's country. | An invoice correction automatically changes origin. | The broker may choose any country with lower duty. | Origin is determined under applicable rules and cannot be inferred solely from dispatch location or convenience.
Which completion statement is supported after an authorized correction but before an agency decision? | The file has been corrected; customs release still needs confirmation. | Customs has released the shipment automatically. | No further review can ever be required. | The corrected invoice proves all classifications worldwide. | Internal document correction and an actual customs release are distinct statuses.''',
    dialogue='''Sofia | The invoice calls these goods stainless-steel bolts, while the packing list says aluminum brackets. The broker has asked us to clarify the file before relying on it.
Chen | That is a [[document discrepancy::The discrepancy is a conflict in product and material descriptions, not merely a formatting difference.]]. Both documents show five hundred pieces, but the matching count does not tell us which product description is accurate.
Sofia | Please check the actual shipment before editing either document. I cannot tell the broker which description is correct from these two conflicting records.
Chen | I will obtain the [[product specification::The product specification can provide verified characteristics of the actual goods to support an accurate correction.]] and reconcile the order and packing records. We need facts linked to this shipment, not a similar product description from another file.
Sofia | Material is one of the conflicts, not just the item name. Steel bolts and aluminum brackets are not two harmless ways of saying the same thing.
Chen | We must confirm [[material composition::Material composition identifies what the goods are made of, resolving the steel-versus-aluminum conflict with evidence.]] from the relevant source. I will not infer it from the document we happen to prefer or from the duty result someone expects.
Sofia | The broker also needs a description that identifies the goods meaningfully. Making both documents say parts would remove the visible conflict while making the file less informative.
Chen | Agreed. The [[merchandise description::The merchandise description should accurately identify the goods rather than hide disagreement behind a vague label.]] must follow the verified goods. A generic replacement would not resolve the underlying uncertainty about product identity and characteristics.
Sofia | Once the facts are established, the responsible issuer should correct whichever document is wrong. We should not silently overwrite an exporter document ourselves.
Chen | I will arrange a [[corrected invoice::A corrected invoice is an authorized revision if the invoice is affected, not an informal alteration by an unrelated recipient.]] if the invoice needs correction, and the corresponding packing-list correction if needed. The verified facts determine which records must change.
Sofia | Please retain the original records and the explanation. The next reviewer needs to understand why the descriptions changed instead of seeing an unexplained replacement.
Chen | We will preserve the [[revision history::Revision history records the original information, authorized change, and reason so the correction remains traceable.]] and supporting references. Consistent documents are useful only if their consistency reflects the actual shipment rather than a convenient edit.
Sofia | We also should not invent a tariff code from this short conversation. We do not yet have the verified characteristics needed for the applicable review.
Chen | Correct. [[Tariff classification::Tariff classification requires the applicable product facts and rules; the conflicting file does not supply a completed determination.]] must follow the relevant facts and rules. A desired duty rate is not a reason to change the product description.
Sofia | The form names the dispatch country. What do we have to support the origin entry? I do not want someone copying the first country they see.
Chen | Yes. [[Country of origin::Country of origin is determined under applicable rules and is not automatically the country from which the shipment departed.]] needs the applicable determination. We should not copy the dispatch country into the origin field merely because it is the only country readily visible.
Sofia | Once the verified information and authorized corrections are ready, I will send them to the broker and responsible import team with the supporting references.
Chen | That gives the [[customs broker::The customs broker receives the verified facts and corrected records for the appropriate customs review rather than being asked to guess product identity.]] a factual basis for the required review. We should answer the clarification request directly rather than imply that matching counts settle the matter.
Sofia | The status update will say the document discrepancy is being resolved. Even a corrected file would not justify telling the warehouse the goods are already released.
Chen | Exactly. [[Customs release::Customs release is a separate actual customs decision, not the automatic result of correcting an internal document file.]] must be confirmed as its own event. Our responsibility here is an accurate, authorized, traceable file, without inventing a classification or a clearance outcome.''',
    transfer_title='Match the goods, not just the words',
    transfer_setup='An invoice says plastic housings and the packing list says steel housings. Both list 40 pieces. Actual material and customs release are unconfirmed.',
    transfer='''Coordinator: "The counts match, but the ___ differs." | material | Plastic and steel are different material descriptions despite the matching quantity.
Exporter: "We need verified product ___." | facts | Underlying evidence is needed before selecting or correcting either description.
Coordinator: "The responsible issuer must authorize any ___." | correction | A document change should follow the appropriate authority and preserve traceability.
Exporter: "A corrected file does not prove customs ___." | release | Document correction is distinct from a confirmed customs release decision.''',
    rehearsal=["Read turns 1-10. Name both conflicting goods descriptions while keeping the matching count of 500 unchanged.","Switch roles for turns 11-20. Emphasize verified facts, authorized correction, and customs release as separate steps.","Complete and check the transfer. Read the material discrepancy and correction request without choosing plastic or steel as the verified fact."]))


BOOK['units'].append(unit(
    title='Supply Risk and Business Continuity',
    scene='A second supplier is not yet a ready backup',
    skill='Compare supply options while separating quoted lead time, reserved capacity, qualification, and shared disruption exposure.',
    brief='Risk planner Ren and sourcing manager Julia compare supplier A, with a quoted two-week lead time, and supplier B, with a quoted four-week lead time. B reports spare capacity, but none is reserved and qualification is incomplete. Both may depend on the same coating site; this is unverified. Current usable stock equals three weeks of the stated demand rate. The team must assess continuity without declaring B immediately usable or treating two supplier names as proof of independent supply.',
    cast='Ren | Risk planner\nJulia | Sourcing manager',
    culture=('Turn backup into a list of conditions', 'A reassuring supplier name is not an operational continuity plan. Ask what must be qualified, reserved, transferred, or verified before the alternative can supply. This makes the resilience discussion concrete without assuming that the faster supplier is always better or the second source removes all common risks.'),
    a='''What is the status of B's capacity? | Reported spare capacity, not reserved for this buyer | A confirmed allocation already producing the order | A guarantee of immediate usable supply | Proof qualification is complete | The supplier reports capacity but no reservation or completed qualification is supplied.
What does the potential shared coating site imply? | A possible common dependency that needs verification | Proven fully independent supply routes | Proof both suppliers have already failed | A guarantee that lead times are identical | A shared dependency could expose both sources to the same disruption, but the fact remains unverified.
What stock coverage is supplied? | Three weeks at the stated demand rate | Four weeks under every demand pattern | An indefinite supply guarantee | Two weeks of reserved B capacity | The brief defines three weeks of usable stock coverage at a specified demand rate.''',
    vocabulary='''single sourcing | Choosing to obtain a requirement from one supplier despite alternatives. | review single-sourcing exposure
sole sourcing | Depending on the only available source for a requirement. | identify sole-source constraints
dual sourcing | Using two sources for a defined supply requirement. | assess a dual-sourcing strategy
source qualification | Evaluation and approval of a source for a specified requirement. | complete source qualification
backup capacity | Potential supply capability intended for contingency use. | verify backup capacity
capacity reservation | A defined commitment setting aside supply capability for a buyer. | negotiate a capacity reservation
quoted lead time | A supplier's stated lead-time estimate or offer under specified conditions. | verify the quoted lead time
activation lead time | Time needed to make a contingency operational after a trigger. | estimate activation lead time
switching cost | The cost of moving a requirement to another source or arrangement. | assess switching cost
tooling transfer | Moving required production tools to another site or source. | plan tooling transfer
subtier supplier | A supplier further upstream than the directly contracted supplier. | map subtier suppliers
common dependency | A resource or facility on which multiple supply options rely. | identify a common dependency
correlated disruption | A disruption capable of affecting multiple sources together. | assess correlated disruption
geographic concentration | Supply dependence clustered in the same area. | reduce geographic concentration
business continuity plan | A plan for maintaining or restoring prioritized operations during disruption. | test the business continuity plan
contingency trigger | A defined condition for activating an alternative action. | set a contingency trigger
time to recover | The period needed to restore the specified supply or operational capability. | estimate time to recover
time to survive | The period operations can continue under a defined disruption scenario. | assess time to survive
recovery objective | A target for restoring a specified capability. | define the recovery objective
buffer coverage | The demand period supported by a stated usable buffer. | calculate buffer coverage
resilience | The ability to prepare for, respond to, and recover from disruption. | strengthen supply resilience
risk register | A record of identified risks, assessments, owners, and actions. | update the risk register
scenario test | An examination of a plan under specified hypothetical conditions. | conduct a scenario test
continuity owner | The person accountable for a defined continuity action or plan. | assign a continuity owner''',
    precision='B has a quoted lead time and reported capacity, not a completed qualification or a reserved production slot. A four-week quote is not necessarily the full time needed to activate the backup. The possible shared coating site remains an open fact to verify.',
    precision_extra='Under a simplified scenario of immediate supply loss, unchanged demand, no receipts, and usable backup only after four weeks, three weeks of stock leaves a one-week gap. This illustration is conditional, not a prediction of actual qualification or recovery time.',
    phrases='''Compare like with like | A quotes two weeks; B quotes four, under their stated conditions.
Separate speed and resilience | A shorter quoted lead time does not answer every continuity question.
Qualify the backup | B is not yet a fully ready alternative.
Check approval | Source qualification remains incomplete.
Reserve the resource | Reported spare capacity is not capacity reserved for us.
Look upstream | Verify whether both suppliers use the same coating site.
Keep the fact open | The common-site dependency is possible, not yet confirmed.
Avoid false independence | Two supplier names do not prove independent disruption exposure.
Name the coverage basis | Current usable stock covers three weeks at the stated demand rate.
Include activation | Tooling, qualification, and allocation may affect when the backup becomes usable.
Test a bounded scenario | State demand, receipts, and activation assumptions before calculating a gap.
Separate target and estimate | A recovery objective is not proof that recovery can occur that quickly.
Define the trigger | Agree which event would activate the contingency review.
Assign the owner | Identify who will verify capacity and qualification status.
Keep action conditional | Do not promise backup supply before the required conditions are met.
Close the risk review | Record dependencies, evidence gaps, owners, and next checkpoints.''',
    notes='''Backup | A role in a plan, not proof of readiness.
Spare | May be available generally without being reserved for this order.
Qualified | Refers to an approved purpose and scope, not every product.
Independent | Requires attention to shared upstream resources and locations.
Coverage | Depends on usable stock and the specified demand rate.
Objective | A target to work toward, distinct from an evidenced recovery estimate.''',
    d='''Which comparison is most useful? | Compare lead-time basis, qualification, reserved capacity, activation needs, and shared dependencies. | Select A solely because two is less than four. | Declare B ready because it reports spare capacity. | Treat two supplier names as proof of no common risk. | Continuity depends on operational readiness and exposure, not only the nominal lead-time comparison.
Stock covers three weeks. In a simplified no-receipts scenario, usable backup starts after four. Which statement is precise? | The conditional gap is one week; unverified activation requirements could change it. | The gap is permanently fixed at one week because the quotation is four weeks. | There is no gap because B reports spare capacity. | The gap is seven weeks because stock coverage and lead time must be added. | Four minus three gives one week only under the stated scenario. A quotation, incomplete qualification, and unreserved capacity do not guarantee usable supply after four weeks.
Why investigate the coating site? | A common upstream dependency could disrupt both sources together. | Shared sites always mean both suppliers are already late. | The same coating site proves every component is identical. | It eliminates the need to qualify B. | Common infrastructure can make apparently separate sources vulnerable to the same event.
What distinguishes a recovery objective from time-to-recover evidence? | The objective is a target; the estimate needs support about actual restoration capability. | A target automatically proves the capability exists. | Both terms mean reserved inventory. | A written objective removes qualification needs. | A desired recovery time and an evidenced estimate are different planning statements.''',
    dialogue='''Julia | Supplier A quotes two weeks and supplier B quotes four. B says it has spare capacity, so the team wants to list it as our ready backup.
Ren | That overstates [[source qualification::Source qualification is incomplete for B, so its approval to supply the required item is not established.]]. B is not yet fully qualified for this requirement, and the capacity report does not establish an allocation to us.
Julia | I will ask whether any capacity is reserved for us. Spare capacity today is not the same as a committed slot when we need it.
Ren | Exactly. A [[capacity reservation::A capacity reservation commits capability to the buyer, unlike a general statement that spare capacity exists.]] needs its own confirmation and terms. Reported availability can change before we need it, so it cannot be treated as a standing commitment.
Julia | The four-week number also may assume everything is ready to begin. If qualification or tooling work is needed first, it may not describe the whole switching period.
Ren | Include the [[activation lead time::Activation lead time covers making the contingency operational, potentially beyond the supplier's quoted production lead time.]]. The time from deciding to switch to receiving usable supply may include steps that are not covered by the supplier's quoted lead time.
Julia | We have another unresolved question: both suppliers may use the same coating site. I do not want to repeat that as fact until it is verified.
Ren | Mark it as a possible [[common dependency::A common dependency is a shared resource that could affect both sources, but the coating-site link remains unverified.]]. If confirmed, a disruption there could affect both suppliers despite their separate names and customer contacts.
Julia | That would change the resilience argument. Two sources could still be useful, but we should not describe their risks as independent without examining the upstream connection.
Ren | Correct. [[Correlated disruption::Correlated disruption can affect multiple sources together when they share an upstream exposure.]] is the concern. We need to understand the shared exposure rather than count suppliers and assume each protects us from every failure of the other.
Julia | Current usable inventory covers three weeks at the stated demand rate. How should that be compared with the four-week quote without creating a false recovery promise?
Ren | Use a clearly bounded [[scenario test::A scenario test states hypothetical conditions explicitly rather than presenting an assumption-based result as a forecast.]]. Assume immediate supply loss, unchanged demand, no incoming receipts, and usable backup after four weeks only for that calculation.
Julia | Under those assumptions, the stock ends after three weeks and the backup starts after four. There is a one-week gap, not complete coverage.
Ren | Yes. The [[buffer coverage::Buffer coverage measures the demand period supported by usable stock, here three weeks under the stated rate.]] is shorter than the assumed wait. But actual activation could differ, especially while qualification and reservation remain incomplete.
Julia | Management wants a shorter recovery time. I will show that as a target, but what can we actually support with the evidence we have?
Ren | Exactly. A [[recovery objective::A recovery objective states a target, whereas an achievable restoration estimate requires supporting evidence.]] expresses what we aim to restore and when. It should not be reported as an evidenced recovery estimate merely because management agreed it was desirable.
Julia | The continuity plan needs a decision point too. Otherwise we may know a backup exists on paper but not know when to begin the required review.
Ren | Define a [[contingency trigger::A contingency trigger identifies the condition that starts the planned alternative action or review.]] and the responsible owner. The trigger should lead to the agreed process, not authorize an unqualified source or an unsupported shipment promise.
Julia | I will revise B from ready backup to candidate pending qualification, reservation, and dependency checks. The comparison will retain A's shorter quote without treating it as the only relevant factor.
Ren | Good. Update the [[risk register::The risk register records the open exposures, evidence gaps, owners, and actions needed for the continuity assessment.]] with those conditions and checkpoints. That gives us a practical continuity discussion instead of reassurance based only on a second supplier name.''',
    transfer_title='A buffer and a delayed backup',
    transfer_setup='Usable stock covers two weeks at unchanged demand. In a simplified scenario with no incoming receipts, usable backup begins after five weeks. Capacity is not reserved.',
    transfer='''Planner: "The assumed supply gap is ___ weeks." | three | Five weeks to usable backup minus two weeks of stock leaves three weeks.
Buyer: "The scenario assumes demand stays ___." | unchanged | The coverage calculation uses the fixed demand condition stated in the briefing.
Planner: "Backup capacity still lacks a ___." | reservation | Reported capability is not the same as supply capacity committed to this buyer.
Buyer: "The calculated gap is conditional, not a ___." | guarantee | The result depends on stated assumptions and does not promise actual recovery timing.''',
    rehearsal=["Read turns 1-10, distinguishing reported spare capacity from a reservation and a possible common site from a verified one.","Switch roles for turns 11-20. Keep the one-week gap conditional on the printed simplified scenario.","Complete and check the transfer. Read five weeks minus two as three, then state the unchanged-demand and unreserved-capacity conditions."]))

BOOK['units'].append(unit(
    title='Executive S&OP Decisions',
    scene='Ten minutes left, one assumption unresolved',
    skill='Summarize a cross-functional planning disagreement as an explicit decision with quantified scenarios, constraints, and recorded ownership.',
    brief='Planning lead Amara and executive chair Victor have ten minutes left in a fictional sales and operations planning meeting. Operations proposes 10,500 units next month; sales proposes 12,000 by adding an unconfirmed 1,500-unit promotion increment. Regular capacity is 11,000. No extra-capacity authorization or shared promotion assumption exists. A note says plan agreed despite the unresolved difference. Amara must clarify the decision request and separate the base case, upside case, capacity gap, and actual decision status.',
    cast='Amara | Planning lead\nVictor | Executive meeting chair',
    culture=('End with a decision, not an atmosphere', 'A constructive meeting can still finish without agreement. Record the actual choice, limits, unresolved conditions, owner, and review point. Do not substitute a positive tone or silence for a decision that affects inventory, capacity, and customer commitments.'),
    a='''What explains the numerical difference between the proposals? | A 1,500-unit unconfirmed promotion increment | A confirmed customer order for 12,000 units | A reduction in regular capacity to zero | A completed decision to add 2,000 units of capacity | Sales adds 1,500 to the 10,500 base proposal, but that increment is not confirmed.
How much does the 12,000-unit scenario exceed regular capacity? | 1,000 units | 500 units | 1,500 units | No amount | The upside proposal of 12,000 exceeds regular capacity of 11,000 by 1,000.
What decision status is supported at the start? | The plan is not yet agreed on the supplied facts. | The 12,000-unit plan is formally authorized. | Extra capacity is already approved. | The promotion assumption is shared and confirmed. | The scenario explicitly leaves the promotion assumption and authorization unresolved.''',
    vocabulary='''sales and operations planning | A cross-functional process aligning demand, supply, and business plans, abbreviated S&OP. | conduct sales and operations planning
demand review | Assessment of the demand outlook and its assumptions. | prepare the demand review
supply review | Assessment of resources and constraints against proposed demand. | complete the supply review
pre-S&OP | The reconciliation stage preparing issues and options for executive review. | resolve issues in pre-S&OP
executive S&OP | The leadership review that makes or confirms the required planning decisions. | chair executive S&OP
aggregate plan | A plan at a combined product-family or other summary level. | review the aggregate plan
base case | The reference scenario used for comparison. | establish the base case
upside case | A scenario with higher demand or a more favorable outcome under stated assumptions. | quantify the upside case
downside case | A scenario with lower demand or another adverse outcome under stated assumptions. | assess the downside case
assumption register | A record of the premises, owners, and status underlying a plan. | maintain the assumption register
unconstrained demand | The estimated demand before limiting it to available supply. | state unconstrained demand
constrained plan | A plan adjusted to the available or authorized resources. | develop a constrained plan
capacity gap | The amount by which required capacity exceeds the defined available capacity. | quantify the capacity gap
regular capacity | Output capability available under the stated normal operating arrangements. | confirm regular capacity
incremental capacity | Additional output capability beyond the defined base arrangements. | assess incremental capacity
decision request | The specific choice or authorization sought from the meeting. | frame the decision request
trade-off | A choice involving competing benefits, costs, or risks. | make the trade-off explicit
financial implication | The effect of a proposed plan on costs, revenue, or other financial measures. | assess financial implications
inventory exposure | The risk or commitment associated with carrying the planned stock. | quantify inventory exposure
demand trigger | A defined demand signal that prompts a specified planning action. | agree a demand trigger
decision rights | The defined authority to make particular choices. | clarify decision rights
decision log | A record of actual decisions, rationale, conditions, and owners. | update the decision log
contingent approval | Approval that takes effect only when specified conditions are met. | define contingent approval
planning handoff | Transfer of the agreed plan and conditions to the teams that execute it. | complete the planning handoff''',
    precision='The sales proposal is 10,500 plus 1,500, or 12,000 units. Regular capacity is 11,000, leaving a 1,000-unit capacity gap for that upside case. The base proposal is 500 below regular capacity. Neither arithmetic result approves a plan.',
    precision_extra='Demand and a constrained production plan are different quantities. A meeting can record a base decision, conditional upside action, or unresolved issue, but only if that is what the authorized participants actually decide. A favorable tone is not a decision record.',
    phrases='''State the disagreement | The proposals differ by an unconfirmed 1,500-unit promotion increment.
Separate the reference | The operations base case is 10,500 units.
Name the upside | The sales scenario is 12,000 units if the promotion increment is used.
State the limit | Regular capacity is 11,000 units.
Quantify the gap | The upside case exceeds regular capacity by 1,000 units.
Avoid an implicit authorization | No additional capacity has been authorized.
Frame the choice | We need a decision on the planning basis and how to handle the unconfirmed increment.
Preserve the forecast | A capacity constraint does not by itself erase possible customer demand.
Ask for the condition | What evidence would trigger a review of the promotion increment?
Clarify authority | Who can authorize the additional capacity and its cost?
Separate cost analysis | The financial effect needs its own supported assessment.
Correct the minutes | The note should not say agreed while the key assumption remains unresolved.
Record the actual outcome | Capture only the decision and conditions the chair confirms.
Name the owner | Assign the promotion evidence review to a specific person.
Define the handoff | Execution teams need one clear approved instruction and visible contingencies.
Close without fiction | If the decision is deferred, record the deferral and next review explicitly.''',
    notes='''Plan | Identify whether it is a forecast, production proposal, or authorized instruction.
Aligned | Agreement needs a stated object and decision, not just a cooperative tone.
Unconstrained | Describes demand before supply limits, not permission to produce without resources.
Contingent | Conditions must be explicit and must not be treated as already satisfied.
Agreed | Report only a confirmed decision.
Deferred | A real decision status when the required choice remains open.''',
    d='''Which summary puts the choice clearly? | Base 10,500; upside 12,000 with unconfirmed promotion; regular capacity 11,000; upside gap 1,000. | Everyone agreed to 12,000 because the meeting was positive. | The capacity gap is 1,500 because that is the promotion increment. | Regular capacity proves demand cannot exceed 11,000. | The summary keeps the demand increment, available capacity, and resulting capacity gap distinct.
What does the 11,000 capacity limit establish? | The stated regular supply limit, not a ceiling on possible customer demand | That all forecasts above 11,000 are false | That extra capacity is already approved | That the promotion must produce exactly 500 units | Supply capability and unconstrained demand are different quantities even when a plan must reconcile them.
What wording matches the outcome at the end of the conversation? | Decision deferred; no extra capacity authorized; Victor arranges the follow-up and Amara collects the open questions. | Base production approved now; the promotion is automatically approved tomorrow. | Twelve thousand units approved, with cost analysis to follow later. | Eleven thousand units approved because that is the regular capacity limit. | The chair explicitly defers the production decision and assigns follow-up. Discussing options and holding a review do not authorize either proposed plan.
What should minutes show if the choice remains unresolved? | Decision deferred, with the unresolved assumption, owner, and next review identified | Plan agreed without conditions | All proposals simultaneously approved | No record because the meeting ended politely | An unresolved decision should remain explicit so execution teams do not act on invented consensus.''',
    dialogue='''Victor | The minutes already say plan agreed. Before I approve that wording, tell me what sales and operations have actually agreed to produce next month.
Amara | Nothing yet. The [[decision log::The decision log should record actual choices, not claim agreement while the planning basis remains unresolved.]] is premature. Operations proposes ten thousand five hundred; sales proposes twelve thousand, including a promotion increment that remains unconfirmed.
Victor | Then remove agreed. Show me the reference and the extra demand separately so we can see which assumption is causing the disagreement.
Amara | The [[base case::The base case is the 10,500-unit operations proposal used as the reference for the promotion scenario.]] is ten thousand five hundred. Sales adds fifteen hundred for the promotion. Regular capacity is eleven thousand, with no additional capacity authorized.
Victor | So the promotion needs fifteen hundred extra units of capacity. Is that the approval request I should send to the operations director?
Amara | Not quite. The [[capacity gap::The 12,000-unit upside exceeds 11,000 regular capacity by 1,000, not by the full 1,500 promotion increment.]] is one thousand. The base case already leaves five hundred units of regular headroom; fifteen hundred is the demand increment.
Victor | Thanks. Could we settle this by changing the demand figure to eleven thousand? That would make the spreadsheet balance without requesting extra resources.
Amara | It would conceal the [[unconstrained demand::Unconstrained demand describes possible demand before supply limits and should not be silently reduced to match capacity.]]. A supply ceiling does not establish how much customers might request. Keep the demand scenario separate from the feasible production instruction.
Victor | All right. What choice needs a decision today, and what still needs evidence? I do not want execution teams choosing their own interpretation.
Amara | The [[decision request::The decision request specifies the planning basis and treatment of the unresolved promotion increment that leadership must decide.]] concerns the planning basis and treatment of the promotion. We also need a supported cost assessment before requesting additional capacity.
Victor | We could use the base and return to the promotion when sales has stronger evidence. I am suggesting an option, not approving it yet.
Amara | Then define the [[demand trigger::A demand trigger identifies the evidence or event that would prompt reconsideration of the promotion increment.]] before recording that option as an instruction. What evidence starts the review, who supplies it, and who makes the subsequent decision?
Victor | Sales can propose the evidence. I also need to verify who may approve the extra resources; I cannot infer that authority from attendance at this meeting.
Amara | I will confirm the [[decision rights::Decision rights identify who can authorize the relevant capacity and cost choices rather than treating any recommendation as approval.]]. A recommendation from this group cannot stand in for an authorization that belongs to somebody else.
Victor | The draft uses the words conditionally approved. Can we leave them while the trigger and authorizing person are still unidentified?
Amara | No. A [[contingent approval::Contingent approval depends on specified conditions and must not be treated as unconditional permission before those conditions are met.]] needs actual approval and explicit conditions. At present we have an option under discussion, not permission to spend or produce the increment.
Victor | Then record the decision as deferred. I will own arranging the follow-up tomorrow morning; you will collect the promotion evidence and capacity-cost questions.
Amara | I accept that follow-up. The [[assumption register::The assumption register preserves the unresolved promotion premise, its owner, and review status rather than burying it in false agreement.]] will show the unresolved promotion premise and those assignments, without claiming that tomorrow's review guarantees approval.
Victor | Read back the outcome: deferred, no extra capacity authorized, evidence collection assigned, and follow-up tomorrow morning. The record must not invent a new production instruction.
Amara | Confirmed. The [[planning handoff::The planning handoff transfers only the actual agreed instruction and conditions to execution teams, not a presumed consensus.]] will report that status and refer teams to the existing authorized instruction. Neither proposal becomes an execution plan simply because we discussed it.''',
    transfer_title='The increment and the gap differ',
    transfer_setup='A base proposal is 800 units. A proposed promotion adds 150, making an upside case of 950. Regular capacity is 900. No decision has been approved.',
    transfer='''Planner: "The upside case is nine hundred ___ units." | fifty | Eight hundred plus one hundred fifty produces an upside case of 950.
Chair: "That exceeds regular ___ by 50." | capacity | The 950-unit scenario is fifty above the stated capacity of 900.
Planner: "The promotion increment remains ___." | proposed | The briefing describes an unapproved proposal rather than confirmed incremental demand.
Chair: "The record must not say the plan is ___." | agreed | No decision has been approved, so agreement cannot be claimed.''',
    rehearsal=["Read turns 1-10. Correct the 1,500-unit demand increment to a 1,000-unit capacity gap, using the 500-unit headroom.","Switch roles for turns 11-20. Contrast an option under discussion with the actual deferral and accepted follow-up.","Complete and check the transfer. State the 950-unit upside and 50-unit gap without calling the unapproved plan agreed."]))
