"""Original retail and e-commerce cases for the English Ladder learner book."""
from books.authoring import unit

BOOK = dict(
    slug='retail-ecommerce', title='Retail and E-Commerce English',
    cover_label='ENGLISH FOR RETAIL AND DIGITAL COMMERCE TEAMS',
    cover_title='Retail and\nE-Commerce', cover_size=36,
    tagline='Explain the offer. Trace the order.\nMake the numbers meaningful.',
    audience='For merchandising, digital trading, inventory, fulfillment, customer service, and store operations teams.',
    map_intro='Eight commercial conversations: compare ranges, examine a promotion, locate sellable stock, explain a delivery delay, investigate checkout performance, challenge a vendor scorecard, handle a return request, and repair a pickup handoff.',
    notes_title='Connect the commercial claim to the customer experience',
    notes_intro='Retail teams move between units, orders, prices, stock states, and customer promises. These conversations practice making each distinction clear while keeping the next action useful.',
    field_notes=[
        ('Name the measure before the result', 'Revenue, gross profit, units, and conversion answer different questions. State the denominator and comparison period before drawing a conclusion.', '"Units increased, but gross profit fell on the stated cost basis."'),
        ('Locate the stock behind the promise', 'A national total does not establish availability at a pickup store. Check the item, location, inventory state, and fulfillment route.', '"Thirty units are available at the warehouse; this store has none."'),
        ('Make uncertainty useful', 'An honest delivery update combines the latest verified status with a named next step. Do not turn an estimated arrival into a guarantee.', '"The carrier has not confirmed a new arrival time; I will update you at two."'),
        ('Separate authority from empathy', 'Acknowledge the inconvenience without inventing a refund, replacement, or policy exception. Explain available review routes and applicable customer rights.', '"I can submit the exception request, but I cannot approve it myself."'),
    ],
    scope_note='All companies, customers, products, figures, and local procedures are fictional. This book teaches professional English, not legal, accounting, or operational advice. Actual consumer rights, return obligations, marketplace terms, and shipping requirements depend on the transaction and jurisdiction. Store policies do not override applicable rights. Software terminology varies by platform.',
    sources=[
        dict(title='Federal Trade Commission. Business Guide to the Mail, Internet, or Telephone Order Merchandise Rule.', url='https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule', note='Background on shipment promises and delay obligations. Shipment and delivery are distinguished; the fictional carrier-delay case is not a complete legal procedure.', checked='1 October 2026'),
        dict(title='Shopify Help Center. Understanding inventory states.', url='https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states', note='Background on on-hand, available, committed, unavailable, and incoming quantities. The fictional inventory case states its own quantities and location scope.', checked='1 October 2026'),
        dict(title='Google Analytics Help. About ecommerce metrics.', url='https://support.google.com/analytics/answer/13428834?hl=en', note='Background on event-level and item-level measures. The checkout case explicitly defines its own denominator rather than implying a universal platform conversion metric.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Merchandising and Assortment Planning',
    scene='Equal revenue, different stock exposure',
    skill='Compare product ranges using a defined sell-through measure and a balanced buying recommendation.',
    brief='During the same four-week season, Range A sold 80 of its 100 opening units for $12,000. Range B sold 120 of its 200 opening units, also for $12,000. There were no receipts, returns, or stock adjustments. A sold at full price; B required markdowns. For this review, unit sell-through means units sold divided by opening units. Buyer Inez and planner Cal must discuss next season without assuming that equal revenue means equal performance. Product costs and customer-segment evidence are not yet available.',
    cast='Inez | Buyer\nCal | Merchandise planner',
    culture=('Challenge the measure, not the buyer', 'A range can matter for customer choice even when its stock turns slowly. Recognize that commercial purpose, then identify the missing evidence. A precise question about margin or remaining stock is more useful than calling a colleague\'s selection a failure.'),
    a='''What is Range A's sell-through under the stated definition? | 80% | 60% | 40% | 120% | Eighty units sold divided by one hundred opening units equals eighty percent.
How many units remain in Range B? | 80 | 20 | 120 | 200 | Two hundred opening units minus one hundred twenty sold leaves eighty units.
What is not yet established? | Which range has higher gross profit | Both ranges earned $12,000 revenue | Range B used markdowns | Range A sold 80 units | Product costs are missing, so equal revenue does not establish relative gross profit.''',
    vocabulary='''assortment | The selection of products offered to customers. | review the assortment
range | A related group of products offered for sale. | compare product ranges
stock-keeping unit (SKU) | An internal identifier for a specific stocked item or variant. | rationalize the SKU count
sell-through | Units sold as a proportion of a defined stock base. | calculate unit sell-through
opening stock | Inventory held at the start of a period. | establish opening stock
residual stock | Inventory remaining after the measured selling period. | reduce residual stock
markdown | A reduction from an earlier selling price. | take a markdown
full-price sale | A sale at the regular undiscounted price. | protect full-price sales
option count | The number of distinct product choices in a range. | review the option count
assortment breadth | The variety of categories or product choices offered. | broaden the assortment
assortment depth | The variety of options within a product category or line, distinct from units held per option. | adjust assortment depth
size curve | The planned distribution of units across sizes. | revise the size curve
colorway | A particular color version of a product. | add a colorway
core line | A recurring product line central to the offer. | replenish a core line
seasonal line | A line intended for a particular selling season. | exit a seasonal line
range review | A structured assessment of the product selection. | conduct a range review
buying budget | Funds allocated to purchasing merchandise. | protect the buying budget
open-to-buy | A planned merchandise purchasing allowance after commitments. | check open-to-buy
stock turn | A measure of how frequently inventory is sold or replaced. | compare stock turn
weeks of cover | Stock expressed in weeks at a specified sales rate. | assess weeks of cover
gross margin return on inventory | Gross profit relative to average inventory cost. | evaluate inventory return
delist | Remove an item from the active product selection. | propose a delisting
range rationalization | Simplifying the assortment using stated commercial criteria. | support range rationalization
customer segment | A group of customers with relevant shared characteristics. | serve a customer segment''',
    precision='Sell-through definitions differ. This case uses units sold divided by opening units, with no other stock movements. A is 80%; B is 60%. Do not quietly substitute revenue or remaining units as the denominator.',
    precision_extra='Equal sales revenue does not establish equal gross profit or inventory return. Costs, timing, stock investment, and the role of each range matter. A recommendation can identify further analysis without pretending the final buying decision is settled.',
    phrases='''Open the comparison | Both ranges generated $12,000 in the same four weeks.
Define the measure | Here, sell-through uses units sold divided by opening stock.
State the stronger rate | Range A sold through at eighty percent.
State the remaining exposure | Range B still has eighty units on hand.
Acknowledge the commercial role | B may serve a different customer segment.
Separate units and revenue | More units sold does not necessarily mean more revenue.
Identify the price effect | B reached the same revenue with markdowns.
Ask for the missing basis | Can we add product costs before comparing gross profit?
Avoid an automatic decision | This is not enough evidence to delist the whole range.
Narrow the next review | Let us examine B by size and colorway.
Protect a useful distinction | The rate is lower even though unit sales are higher.
Request comparable periods | Keep both ranges on the same four-week basis.
Limit the recommendation | I recommend a more targeted buy, subject to the missing evidence.
Clarify commitment | A proposal is not a released purchase order.
Preserve the customer question | We still need to understand which customers bought B.
Summarize the trade-off | The same revenue came with different stock and price exposure.''',
    notes='''At full price | Describes the transaction price, not automatically a higher profit.
Sold through at | Introduces a rate with an explicitly defined stock base.
Subject to | Makes the recommendation conditional on named evidence.
Even though | Connects a higher unit count with a lower sell-through rate.
By size and colorway | Narrows analysis to commercially useful product variants.
Not enough evidence | Challenges the conclusion without dismissing the data.''',
    d='''Which comparison is accurate? | A sold 80% of opening units; B sold 60%. | A sold fewer units, so its sell-through must be lower. | Both sell-through rates are equal because revenue is equal. | B sold 120%, using A's opening stock. | Each range needs its own opening-unit denominator; revenue does not replace that stock base.
Which claim needs product costs? | A earned more gross profit than B. | B sold 120 units. | A had 20 units remaining. | B required markdowns. | Gross profit subtracts product costs, which the briefing does not supply.
Which recommendation is appropriately limited? | Review B by variant and customer segment before changing the buy. | Delist every B item because one period proves no demand. | Double B solely because it sold more units. | Treat equal revenue as proof of equal inventory return. | Variant and segment evidence supports a more specific decision than the aggregate result alone.
Which wording states a condition? | We can revise the buy once the cost and variant review is complete. | We have already released the order. | Every missing cost is zero. | The review guarantees higher future sales. | Once makes the proposed action depend on completing the specified review.''',
    rehearsal=['Read turns 1-10; contrast units sold, sell-through, and remaining stock.', 'Swap roles for turns 11-20; keep the next buy conditional on the cost and variant review.', 'Complete the transfer and check each range against its own opening stock.'],
    dialogue='''Inez | Both ranges brought in twelve thousand. Can we repeat the buy? B needed more promotional support, but I do not want to cut a range customers still use.
Cal | Before we repeat the buy, look at [[sell-through::Sell-through compares sold units with the defined stock base, revealing a difference that equal revenue hides.]]. A sold eighty of one hundred units; B sold one hundred twenty of two hundred. That gives eighty percent and sixty percent respectively.
Inez | B did sell forty more units. I do not want the team to lose sight of that demand when we review the range.
Cal | Agreed, but B also leaves more [[residual stock::Residual stock is the inventory left after sales; B retains eighty units while A retains twenty.]]. We have eighty units remaining there, compared with twenty in A. Those units still need a commercial plan.
Inez | We reached the same revenue through different prices. A held its regular price, while B required reductions during the season.
Cal | Exactly. The [[markdown::Markdown names the price reduction used to support B's sales, not the sales volume itself.]] helped B move units, but we cannot judge the profit effect properly without product costs. The revenue line alone will not settle that question.
Inez | Should we remove B completely? That would release buying budget, but it might also leave a gap for a customer group we serve.
Cal | I would not recommend an immediate [[delisting::Delisting removes a product from the active range; the evidence does not yet justify removing all of B.]]. First, separate B by size and colorway. An aggregate result can hide strong variants alongside weak ones.
Inez | Some sizes may be carrying the leftovers. We should see whether the original distribution matched what customers actually selected.
Cal | Then review the [[size curve::The size curve describes the unit distribution across sizes, which may explain uneven leftover stock.]]. That may support changing quantities within the range rather than removing every option. We need the variant-level data before deciding.
Inez | I also want to know whether B attracts customers who rarely buy A. Equal revenue does not tell us whether the ranges overlap.
Cal | Yes, include the [[customer segment::Customer segment identifies the group served by a range and helps assess its distinct commercial role.]] evidence. We should not describe B as unnecessary until we understand its role. That is a separate question from this period's lower rate.
Inez | Could we call for a smaller initial order, with more room to react later?
Cal | We can propose that within the [[buying budget::Buying budget names the money allocated to merchandise purchases, constraining the proposed initial order.]], but supplier lead times and minimum quantities still need checking. Flexibility on paper is not always available in the supply arrangement.
Inez | Let us keep the recommendation conditional and show the remaining inventory separately.
Cal | I will add [[gross margin return on inventory::This measure relates gross profit to average inventory cost, requiring cost and investment information absent here.]] once we have the required cost and average-stock information. I will not manufacture it from these sales totals.
Inez | Good. Keep the four-week dates visible so we do not compare a full season with a partial one.
Cal | The [[range review::Range review is the structured assessment bringing together sales, stock, pricing, and the role of the selection.]] will show common dates, both denominators, the price reductions, and the outstanding analysis. That makes the recommendation easier to challenge constructively.
Inez | Hold the repeat order, then. Bring me the size and color breakdown with costs before we decide which options to keep.
Cal | Correct. We can revisit [[assortment depth::Assortment depth concerns the variety of options within a line, such as sizes and colorways; units held per option are stock depth.]] after that review, alongside quantities per option. Equal revenue is the starting observation, not the final buying decision.''',
    transfer_title='Compare a second pair of ranges',
    transfer_setup='Range C sells 45 of 60 opening units. Range D sells 60 of 120 opening units. There are no other stock movements. Use the same unit sell-through definition.',
    transfer='''Buyer: "C has a sell-through rate of ___." | 75% | Forty-five sold units divided by sixty opening units equals seventy-five percent.
Planner: "D has a sell-through rate of ___." | 50% | Sixty sold units divided by one hundred twenty opening units equals fifty percent.
Buyer: "C has ___ units remaining." | 15 | Sixty opening units less forty-five sold leaves fifteen remaining units.
Planner: "D has ___ units remaining." | 60 | One hundred twenty opening units less sixty sold leaves sixty remaining units.''',
))

BOOK['units'].append(unit(
    title='Pricing, Promotions, and Margin',
    scene='A busy promotion with a smaller gross profit',
    skill='Explain price-volume arithmetic and challenge a profit claim without dismissing the promotion goal.',
    brief='In the baseline week, a product sold 100 units at $50 each. During the promotion it sold 120 units at $42.50 each, a 15% price reduction. Product cost remained $30 per unit. These are complete comparable weekly sales with no returns. Taxes, shipping income, operating expenses, and other promotional costs are excluded. Trading manager Hugo says the 20% unit increase proves that profit improved. Finance partner Nia must correct that claim and separate the measured result from other possible campaign objectives.',
    cast='Hugo | Trading manager\nNia | Finance partner',
    culture=('Keep the success criterion explicit', 'A promotional team may emphasize traffic or new customers while finance emphasizes margin. Name the objective being tested. Correcting the arithmetic does not require calling the entire campaign a failure; other benefits need their own evidence.'),
    a='''What was promotion revenue? | $5,100 | $6,000 | $4,250 | $5,000 | One hundred twenty units multiplied by forty-two dollars fifty equals five thousand one hundred dollars.
What was promotion gross profit on the stated basis? | $1,500 | $2,000 | $2,400 | $5,100 | Revenue of $5,100 less product costs of $3,600 leaves $1,500 gross profit.
Which cost is excluded? | Operating expenses | The $30 unit product cost | Cost of all 120 units sold | Cost of baseline units sold | The brief includes unit product cost but explicitly excludes operating expenses.''',
    vocabulary='''selling price | The amount charged per unit before specified adjustments. | set the selling price
unit volume | The number of units sold during a period. | increase unit volume
sales revenue | Income from the measured sales before the stated costs. | calculate sales revenue
cost of goods sold | Product costs attributable to the units sold. | deduct cost of goods sold
gross profit | Sales revenue less cost of goods sold. | protect gross profit
gross margin percentage | Gross profit divided by sales revenue, expressed as a percentage. | calculate gross margin percentage
price reduction | A decrease in the selling price. | apply a price reduction
promotional uplift | An increase against a defined nonpromotional comparison. | measure promotional uplift
baseline | The reference level used for comparison. | establish a baseline
incremental revenue | Additional revenue relative to the defined comparison. | estimate incremental revenue
unit gross profit | Selling price less the stated product cost per unit. | compare unit gross profit
contribution margin | Revenue less the variable costs included in its definition. | define contribution margin
price elasticity | The responsiveness of quantity demanded to price changes. | estimate price elasticity
cannibalization | Sales gained by one offer at another offer's expense. | assess cannibalization
halo effect | A related benefit beyond the promoted product itself. | test for a halo effect
basket value | The monetary value of a customer's purchase basket. | increase basket value
average order value | Revenue divided by the relevant order count. | monitor average order value
discount depth | The size of a price reduction against its reference. | compare discount depth
redemption rate | The proportion using an offer among a defined eligible base. | calculate redemption rate
promotion mechanic | The structure by which an offer operates. | explain the promotion mechanic
funding allowance | A contribution toward promotion costs under agreed terms. | verify a funding allowance
price override | An authorized change from the system's listed selling price. | approve a price override
break-even volume | Units required to meet a specified cost or profit threshold. | calculate break-even volume
margin dilution | A reduction in the relevant profit margin. | quantify margin dilution''',
    precision='Units rose 20%, while price fell 15%. Revenue changes multiplicatively: 1.20 times 0.85 equals 1.02, a 2% increase. Subtracting the two percentages would incorrectly give 5%.',
    precision_extra='Baseline gross profit is $2,000; promotion gross profit is $1,500, down 25%. This is not net profit. Gross margin percentage falls from 40% to approximately 29.4% under the stated cost exclusions.',
    phrases='''Acknowledge volume | The promotion sold twenty percent more units.
Correct the inference | That does not by itself establish higher profit.
State the new price | The promotional price was $42.50.
Keep the cost basis | Product cost stayed at thirty dollars per unit.
Calculate revenue | One hundred twenty times $42.50 gives $5,100.
Separate the measures | Revenue rose two percent; gross profit fell twenty-five percent.
Show the unit effect | Unit gross profit fell from twenty dollars to $12.50.
Name the exclusion | This calculation excludes operating and promotional expenses.
Define the margin | Gross margin percentage uses revenue as its denominator.
Avoid a false shortcut | The price and volume changes must be multiplied.
Recognize another objective | New-customer acquisition would need a separate measure.
Ask about funding | Has any supplier allowance actually been agreed?
Limit the conclusion | These figures do not establish net profitability.
Explain the threshold | At $12.50 per unit, 160 units would match the prior gross profit.
Protect the baseline | Use the same product and comparable periods.
Close the review | Let us report the volume gain and the margin cost together.''',
    notes='''By itself | Restricts what one measure can prove.
From ... to ... | Makes the original and new values explicit.
Excludes | Names costs or revenues outside the calculation.
Approximately | Marks a rounded percentage, not an exact value.
Would match | States a conditional threshold, not an achieved result.
Actually agreed | Distinguishes confirmed funding from hoped-for support.''',
    d='''Which statement correctly combines the price and volume effects? | Revenue rose 2%. | Revenue rose 5%. | Revenue rose 20%. | Revenue fell 15%. | The new quantity factor 1.20 multiplied by price factor 0.85 gives revenue factor 1.02.
What happened to gross profit? | It fell from $2,000 to $1,500. | It increased to $5,100. | It stayed at $2,000. | It increased 20% with units. | Baseline gross profit is 100 times $20; promotion gross profit is 120 times $12.50.
How many promotional units would match baseline gross profit? | 160 | 100 | 120 | 150 | The $2,000 baseline divided by $12.50 unit gross profit requires 160 units.
Which claim goes beyond the supplied evidence? | The campaign acquired profitable new customers. | Product cost remained $30 per unit. | Promotion revenue was $5,100. | Gross profit fell on the stated basis. | No customer-acquisition or customer-profitability evidence is supplied by the weekly sales figures.''',
    rehearsal=['Read turns 1-10; say both revenue and gross profit before assessing the promotion.', 'Swap roles for turns 11-20; distinguish the profit-matching threshold from actual sales.', 'Complete the transfer using price times units, then subtract the stated product costs.'],
    dialogue='''Hugo | Units were up twenty percent. I have called that a profit improvement in the trading note. Can you check the wording before I send it?
Nia | The [[unit volume::Unit volume counts units sold; the twenty-percent increase does not alone establish revenue or profit improvement.]] improved, but the price fell. Let us calculate the money result before choosing that wording. We sold one hundred twenty units at forty-two dollars fifty.
Hugo | That gives five thousand one hundred dollars, compared with five thousand in the normal week.
Nia | Correct. [[Sales revenue::Sales revenue is price multiplied by units here; it rose from five thousand to five thousand one hundred dollars.]] increased two percent. We multiply the quantity and price factors, rather than subtracting fifteen percent from twenty percent and calling the difference five.
Hugo | Revenue is still higher. Why would that not support the profit claim?
Nia | Because [[cost of goods sold::Cost of goods sold includes thirty dollars for each sold unit, rising as unit volume increases.]] also increased with the extra units. At thirty dollars per unit, it was three thousand dollars before and three thousand six hundred during the promotion.
Hugo | So we subtract those product costs from the revenue in each week.
Nia | Yes. That gives [[gross profit::Gross profit subtracts product costs from revenue; the resulting amounts are two thousand and fifteen hundred dollars.]] of two thousand dollars before and fifteen hundred during the promotion. On that measure, the result fell twenty-five percent despite the higher revenue.
Hugo | We should also explain why each sale contributed less before the other costs.
Nia | The [[unit gross profit::Unit gross profit subtracts the thirty-dollar product cost from each selling price, producing twenty dollars and twelve fifty.]] fell from twenty dollars to twelve dollars fifty. We would need one hundred sixty promotional units to match the previous two thousand dollars.
Hugo | We sold only one hundred twenty, so we did not reach that threshold.
Nia | Right. This [[break-even volume::Break-even volume here is explicitly the quantity needed to match prior gross profit, not company-wide net-profit break-even.]] is defined as matching the prior gross profit, not covering every business expense. The definition needs to stay next to the number.
Hugo | Could traffic or new customers still make the promotion worthwhile?
Nia | Possibly, but those goals need evidence beyond this [[baseline::Baseline identifies the reference week against which this promotion is compared, not proof of wider customer benefits.]] comparison. We have no new-customer or repeat-purchase data here. A possible benefit should not be presented as a measured result.
Hugo | The buyer mentioned possible supplier funding. Do we have an agreed amount, or should I leave it out of this result?
Nia | Only if the [[funding allowance::Funding allowance is supplier support under agreed terms; an unconfirmed possibility must not be booked as an established benefit.]] is confirmed and accounted for on the correct basis. At present, these figures contain no agreed supplier contribution. Keep that possibility separate.
Hugo | What percentage should the margin line show?
Nia | The [[gross margin percentage::Gross margin percentage divides gross profit by revenue; fifteen hundred over fifty-one hundred is approximately twenty-nine point four percent.]] is approximately twenty-nine point four percent, down from forty. That is a revenue-based ratio, not the twenty-five-percent change in gross profit dollars.
Hugo | I will report the volume gain and the lower gross profit, then list customer acquisition as an unanswered question.
Nia | Good. Describe the [[margin dilution::Margin dilution names the reduction in the profit margin, allowing a balanced account alongside the higher sales volume.]] clearly without declaring every campaign objective a failure. We can assess the wider decision when the additional evidence is available.''',
    transfer_title='Calculate another promotion result',
    transfer_setup='A product sells 50 units at $80 in the baseline period and 60 units at $70 in the promotion. Product cost is $50 per unit. Exclude all other costs and returns.',
    transfer='''Manager: "Baseline revenue was ___ dollars." | 4,000 | Fifty units multiplied by eighty dollars yields four thousand dollars of revenue.
Analyst: "Promotion revenue was ___ dollars." | 4,200 | Sixty units multiplied by seventy dollars yields four thousand two hundred dollars.
Manager: "Baseline gross profit was ___ dollars." | 1,500 | Fifty units times the thirty-dollar unit gross profit gives fifteen hundred dollars.
Analyst: "Promotion gross profit was ___ dollars." | 1,200 | Sixty units times the twenty-dollar unit gross profit gives twelve hundred dollars.''',
))

BOOK['units'].append(unit(
    title='Inventory, Allocation, and Replenishment',
    scene='The national total cannot promise store pickup',
    skill='Translate inventory states into an accurate location-specific availability message.',
    brief='At 09:00, SKU L42 has 100 units physically on hand at the central warehouse: 60 committed to existing orders, ten held for quality review, and 30 available for new sales. Twenty additional units are incoming and are not included in on-hand stock. Store East has no units. The website incorrectly uses the warehouse total to display pickup availability at Store East. Inventory controller Miro and digital trader Anika must correct the promise and check delivery eligibility before offering a warehouse fulfillment route.',
    cast='Miro | Inventory controller\nAnika | Digital trader',
    culture=('Ask which stock number the team means', 'Merchandising, stores, and digital teams may all say available while referring to different records. Repeat the location and status instead of assuming agreement. This makes a correction collaborative and prevents a national total from becoming an unsupported local promise.'),
    a='''How many warehouse units are available for new sales? | 30 | 100 | 60 | 120 | One hundred on-hand units less sixty committed and ten held leaves thirty available.
How many incoming units are included in the on-hand total? | None | 20 | 30 | 100 | The brief explicitly separates twenty incoming units from the one hundred physically on hand.
What is established for Store East? | It has no units. | It has all 100 warehouse units. | It can offer immediate pickup of 30 units. | Its replenishment has already arrived. | Store East has zero units, so warehouse stock cannot establish local pickup readiness.''',
    vocabulary='''on-hand inventory | Stock physically held at the stated location. | reconcile on-hand inventory
available inventory | Stock eligible for new sales under the stated rules. | confirm available inventory
committed inventory | Stock already allocated to existing demand. | protect committed inventory
unavailable inventory | Held stock not currently eligible for sale. | classify unavailable inventory
incoming inventory | Stock expected but not yet received into the location. | track incoming inventory
quality hold | A restriction pending the applicable product-quality review. | maintain a quality hold
allocation | Assignment of stock to a demand source or destination. | revise the allocation
replenishment | Restocking to support future sales or demand. | schedule replenishment
available to promise | Quantity that can be committed under defined fulfillment rules. | calculate available to promise
stockout | Lack of the required sellable stock at a location. | report a store stockout
location-level availability | Sellable stock information for a particular site. | verify location-level availability
inventory feed | Data supplied to another system about stock quantities or states. | correct the inventory feed
safety stock | Stock held as a buffer against uncertainty. | review safety stock
reorder point | The stock position that triggers replenishment under a policy. | set a reorder point
lead time | Elapsed time between defined order and supply milestones. | verify replenishment lead time
transfer order | A record authorizing movement between inventory locations. | create a transfer order
cycle count | A targeted physical count of selected inventory. | perform a cycle count
inventory adjustment | A recorded change to the system's stock quantity. | authorize an inventory adjustment
overselling | Accepting demand beyond what can be fulfilled as promised. | prevent overselling
backorder | Unfilled demand awaiting stock under the applicable arrangement. | manage a backorder
fulfillment eligibility | Whether an item and location may serve a specified order. | check fulfillment eligibility
stock reservation | Holding specified stock for a defined demand. | confirm a stock reservation
inventory snapshot | Quantities and states captured at a particular time. | timestamp the inventory snapshot
channel allocation | Assignment of inventory to particular sales channels. | review channel allocation''',
    precision='On hand is not the same as available. Here the 100 warehouse units comprise 60 committed, ten held, and 30 available. The 20 incoming units are additional expected stock, not stock already received.',
    precision_extra='Warehouse availability does not establish store pickup or a delivery promise. Check location, item, eligibility, reservation, and timing under the actual process. An inventory snapshot can become stale as orders and stock movements occur.',
    phrases='''Identify the item | We are checking SKU L42.
Timestamp the quantity | This is the inventory position at 09:00.
Separate physical and sellable stock | One hundred units are on hand, but only thirty are available.
Protect existing orders | Sixty units are already committed.
Respect the hold | Ten units remain under quality review.
Keep incoming stock separate | Twenty units are incoming, not yet received.
State the local position | Store East currently has no units.
Correct the promise | The warehouse total must not drive a ready-for-pickup message here.
Check the route | Can this warehouse fulfill this customer's delivery address?
Avoid an assumed reservation | Availability alone does not mean this order has reserved stock.
Request a fresh check | Refresh the quantity before making the offer.
Name the system issue | The feed is using the wrong location and inventory state.
Keep the hold intact | Do not release held units just to cover the website promise.
Limit a transfer claim | A proposed transfer is not a received replenishment.
Coordinate the correction | Update the customer-facing message and the underlying feed.
Close with a verified option | Offer a delivery route only after eligibility is confirmed.''',
    notes='''At 09:00 | Fixes the time scope of a changing quantity.
Already committed | Protects demand that has an existing allocation.
Not yet received | Distinguishes incoming units from physically held stock.
Currently | Signals a present position, not a permanent stockout.
Only after | Makes the offer conditional on the relevant check.
Underlying feed | Names the data source, not merely the visible message.''',
    d='''Which website claim is supported now? | Store East has no stock for pickup. | One hundred units are ready at Store East. | All incoming units are ready for immediate sale. | Held stock is available whenever demand is high. | The local store has no units; the warehouse total does not change that fact.
Which arithmetic matches warehouse availability? | 100 minus 60 minus 10 equals 30. | 100 plus 20 equals 120 available. | 100 minus 10 equals 90 available. | 100 minus 60 equals 40 available. | Both existing commitments and the quality hold must be removed from the on-hand total.
Which step requires a separate check? | Whether the warehouse can fulfill the customer's delivery route | Whether Store East currently has zero units | Whether ten units are held | Whether twenty units are incoming | The brief leaves delivery eligibility unconfirmed despite the warehouse having thirty available units.
Which wording overstates a proposed transfer? | The replenishment has arrived at Store East. | We can review a transfer option. | Store East has no units at this snapshot. | A transfer needs the actual timing confirmed. | A proposed stock movement does not establish physical receipt at the receiving store.''',
    rehearsal=['Read turns 1-10; separate on-hand, committed, held, and incoming quantities.', 'Swap roles for turns 11-20; check delivery eligibility before offering warehouse stock.', 'Complete the transfer without adding incoming units to available stock.'],
    dialogue='''Anika | East is getting pickup requests for L42, but the manager says the shelf is empty. The page shows one hundred units. Can we trace where that number came from?
Miro | Start with the [[inventory snapshot::Inventory snapshot fixes the quantity and status at a particular time; these records describe the position at nine.]] at nine this morning. The hundred units belong to the central warehouse, not Store East. The page is drawing the wrong conclusion from that total.
Anika | Even at the warehouse, can we sell all one hundred to new customers?
Miro | No. That is [[on-hand inventory::On-hand inventory includes all physically held units in this case, including commitments and units on quality hold.]]. Sixty are committed to existing orders, and ten are held for quality review. Only thirty remain available for new sales.
Anika | We also have twenty on the way. Someone added them to the website quantity.
Miro | Keep [[incoming inventory::Incoming inventory is expected stock not yet received; it must not be counted as already held at this warehouse.]] separate. Those twenty have not been received. Adding them to current sellable stock would create a promise we cannot support from this snapshot.
Anika | Could we use the ten held units until the next shipment arrives?
Miro | The [[quality hold::Quality hold restricts the ten units pending review; commercial demand does not itself authorize their release.]] remains in place. We cannot release them merely because the page overpromised. The correction must respect the actual stock states rather than make them fit the message.
Anika | And the sixty already assigned cannot be offered a second time.
Miro | Correct. Protect [[committed inventory::Committed inventory is allocated to existing demand and cannot be treated as unassigned stock for another sale.]]. We should not solve one customer promise by quietly taking stock from another order. The available balance here is thirty, not ninety or one hundred.
Anika | I will remove the Store East pickup claim. Could we offer delivery from the warehouse instead?
Miro | First check [[fulfillment eligibility::Fulfillment eligibility establishes whether this item and warehouse may serve the proposed order and delivery route.]]. Available stock does not prove that this warehouse serves the customer's address or that the order meets the route's conditions.
Anika | If delivery is possible, can I say we have put one aside? I have not created a reservation yet.
Miro | Only after the actual [[stock reservation::Stock reservation assigns stock to a particular demand; a general available balance does not establish that assignment.]] is confirmed. Other orders may arrive after our snapshot. Refresh the quantity before offering a specific commitment.
Anika | That handles this customer. We also need to stop the same error on other product pages.
Miro | Review the [[inventory feed::Inventory feed supplies stock information to the website; its location and state mapping must support the displayed promise.]]. It needs the correct location and state, not just a national physical total. Otherwise the visible correction will be overwritten by the next update.
Anika | The store manager has asked for a warehouse transfer. Can we mark the store replenished?
Miro | Not yet. A [[transfer order::Transfer order records an authorized inter-location movement; it does not prove the receiving store already has the goods.]] is different from receipt. Check approval and timing, then update the store position when the relevant events actually occur.
Anika | I will show no pickup stock at East, check the warehouse delivery route, and raise the feed correction.
Miro | Good. Keep [[location-level availability::Location-level availability ties sellable quantities to a specific site, preventing warehouse inventory from implying local pickup readiness.]] visible in the handoff. That gives stores, digital trading, and customer service one accurate basis for the next conversation.''',
    transfer_title='Read a second inventory snapshot',
    transfer_setup='At Warehouse North, 80 units are on hand: 45 committed, five held, and the rest available. Twelve more are incoming. Store South has zero units.',
    transfer='''Trader: "The available warehouse quantity is ___." | 30 | Eighty on hand minus forty-five committed and five held leaves thirty available.
Controller: "The held quantity is ___." | five | The briefing explicitly identifies five units as held rather than available for sale.
Trader: "The incoming quantity is ___." | twelve | Twelve units are expected separately and are not part of on-hand stock.
Controller: "Store South's current quantity is ___." | zero | The warehouse quantities do not change Store South's explicitly stated zero stock.''',
))

BOOK['units'].append(unit(
    title='Fulfillment, Shipping, and Returns',
    scene='An expired estimate needs an honest next step',
    skill='Acknowledge a missed delivery estimate, distinguish shipment from arrival, and explain a concrete follow-up.',
    brief='Order R81 was physically handed to the carrier on 4 May. The customer was given an estimated arrival date of 6 May. It is now 7 May, and the carrier has not confirmed a new arrival time. Customer Laila needs the item for an event. Agent Tomas can open a carrier inquiry and give a status update at 14:00 today. No replacement dispatch, refund, or revised arrival is authorized in the supplied record. The team must check applicable customer rights and service remedies rather than invent a universal rule.',
    cast='Laila | Customer\nTomas | Customer service agent',
    culture=('Own the communication without inventing control', 'Customers need an accountable seller contact even when a carrier holds the parcel. Avoid blaming another company or offering vague reassurance. State the verified event, the unanswered question, and a follow-up you can actually deliver.'),
    a='''What is confirmed? | The carrier physically received the order on 4 May. | The order arrived on 6 May. | A replacement has shipped. | A refund is approved. | Physical handoff on 4 May is established; delivery and remedies remain unconfirmed.
What does 14:00 today represent? | A status update | Guaranteed delivery | A replacement dispatch time | An automatic refund deadline | The agent promises a communication update, not any unconfirmed shipment or financial outcome.
What is unknown? | The revised arrival time | The order reference | The original estimated date | The date of carrier handoff | The carrier has not confirmed a new arrival time in the supplied record.''',
    vocabulary='''fulfillment | The process of preparing and completing an order's supply. | track order fulfillment
dispatch | Sending goods from the seller's fulfillment operation. | confirm dispatch
carrier handoff | Physical transfer of a parcel to the transport provider. | verify carrier handoff
estimated delivery date | A projected arrival date rather than an unconditional guarantee. | revise an estimated delivery date
tracking event | A recorded milestone in a shipment's movement. | check the latest tracking event
carrier inquiry | A request for the transport provider to investigate a shipment. | open a carrier inquiry
proof of delivery | A record supporting that delivery occurred. | request proof of delivery
delivery exception | An event interrupting the expected delivery process. | investigate a delivery exception
last mile | The final transport stage to the recipient. | coordinate last-mile delivery
delivery window | A stated interval during which arrival is expected or scheduled. | confirm the delivery window
service level | The defined standard or terms of a delivery service. | verify the service level
consignment | Goods sent together under a transport arrangement. | identify the consignment
tracking number | An identifier used to follow a shipment. | provide the tracking number
split shipment | An order sent in separate deliveries. | explain a split shipment
partial fulfillment | Supply of only part of an order. | record partial fulfillment
delivery attempt | An effort to deliver at the specified address. | verify a delivery attempt
return to sender | Routing a parcel back to the sending party. | investigate return to sender
replacement order | An order created to supply a substitute for an earlier item. | authorize a replacement order
refund authorization | Approval to return the relevant payment. | confirm refund authorization
service recovery | Actions addressing a failure in the customer experience. | coordinate service recovery
return authorization | Permission or reference for a return under a process. | issue a return authorization
reverse logistics | Movement and handling of goods back from customers. | manage reverse logistics
return inspection | Examination of returned goods under the applicable process. | complete a return inspection
restocking fee | A charge associated with a return where applicable and lawful. | explain a restocking fee''',
    precision='A shipping label alone does not prove carrier possession. This case does establish physical handoff. Shipment on 4 May still does not establish delivery on 6 May or any revised arrival time.',
    precision_extra='An update promise must not become an arrival promise. Applicable shipment-delay obligations, in-transit remedies, and return rights require the actual transaction and jurisdiction; do not treat every delay as the same legal event.',
    phrases='''Acknowledge the missed estimate | The estimated date has passed, and you still do not have the order.
Recognize the impact | I understand that you need the item for an event.
State the verified milestone | The carrier physically received the parcel on 4 May.
Avoid an unsupported date | I do not have a confirmed revised arrival time.
Take the next action | I can open an inquiry with the carrier now.
Own the follow-up | I will update you today at 14:00.
Separate contact and arrival | That is the update time, not a delivery guarantee.
Check the latest event | I will confirm what the tracking record actually shows.
Avoid blame | I will remain your contact while we investigate.
Limit the remedy claim | No replacement has been authorized in this record.
Check available options | I will review the applicable service remedies and customer rights.
Confirm before promising | I need confirmation before giving a new arrival window.
Avoid false certainty | The absence of a new scan does not prove the parcel is lost.
Keep the order reference | I will record the inquiry against R81.
Provide an honest update | I will contact you even if the carrier has not answered.
Close with accountability | The next message will state the latest position and outstanding action.''',
    notes='''Physically received | Distinguishes possession from a label being generated.
Estimated | Marks the stated arrival as a forecast, without erasing relevant obligations.
I do not have | Identifies the present information gap directly.
Even if | Keeps the communication commitment valid while an answer is pending.
No ... authorized | States the record's limits without deciding all possible remedies.
Remain your contact | Maintains customer-facing ownership across another party's investigation.''',
    d='''Which response is both honest and useful? | The carrier has no confirmed new arrival; I will investigate and update you at 14:00. | It will certainly arrive by 14:00. | The carrier has it, so the seller has no further role. | No scan proves it is permanently lost. | The supported response combines the real uncertainty with an action and a communication commitment.
Which event proves shipment in this case? | Physical carrier handoff on 4 May | Creating a label | An expected arrival on 6 May | Promising an update on 7 May | The briefing establishes actual carrier possession, not merely preparation or an estimated future event.
Which promise is not supported? | A replacement will arrive tomorrow. | An inquiry can be opened. | An update will be given today. | The revised arrival is unconfirmed. | Neither replacement authorization nor a replacement arrival date is supplied.
What should a pending-carrier update do? | State that the reply is pending and identify the continuing action. | Invent a new date to sound decisive. | Say the customer has no rights because the date was estimated. | Avoid contacting the customer until delivery occurs. | An honest update preserves the commitment without fabricating an answer or excluding applicable rights.''',
    rehearsal=['Read turns 1-10; distinguish carrier handoff, estimated arrival, and the update time.', 'Swap roles for turns 11-20; offer a review of real remedies without guessing the outcome.', 'Complete the transfer and identify which date is an update rather than an arrival.'],
    dialogue='''Laila | My order was due yesterday. I need it for an event, and the tracking has stopped changing. Can you tell me whether the carrier actually has it?
Tomas | I am sorry the [[estimated delivery date::Estimated delivery date names the projected arrival that has passed; it is not proof that delivery occurred.]] has passed without the order reaching you. I can see R81, and I will check the actual shipment events rather than repeat the old date.
Laila | Does the record show that you sent it, or only that someone printed a label?
Tomas | It confirms [[carrier handoff::Carrier handoff means the parcel was physically transferred to the transport provider, which is established for 4 May.]] on the fourth of May. That is stronger than a label-created message, but it does not tell us when the parcel will reach your address.
Laila | The delivery was meant to be the sixth. Can you promise tomorrow instead?
Tomas | I cannot confirm a new [[delivery window::Delivery window identifies an expected or scheduled arrival interval; no revised interval is confirmed here.]] yet. The carrier has not supplied one. I would rather give you a verified update than another date that might cause you to make unreliable plans.
Laila | What can you do now? I do not want to be told simply to keep refreshing the website.
Tomas | I can open a [[carrier inquiry::Carrier inquiry is the concrete request for shipment investigation that the agent is authorized to initiate.]] and remain your contact. I will ask for the current location and the latest delivery position, then update you today at fourteen hundred.
Laila | Do you mean the order will arrive by two, or that you will contact me then?
Tomas | I mean I will contact you. The latest [[tracking event::Tracking event is a recorded shipment milestone; checking it supports an update without guaranteeing a future arrival.]] may help explain the delay, but the update appointment is not an arrival promise. I will make that distinction clear in the note.
Laila | Could you send another one now so that I have a backup?
Tomas | A [[replacement order::Replacement order supplies another item, but this record contains no authorization for the agent to promise one.]] has not been authorized. I can review the available remedies under the actual order and service terms, including any applicable customer rights, before confirming an option.
Laila | I would also like to know whether a refund is possible if the item cannot meet my need.
Tomas | I will check that rather than invent a [[refund authorization::Refund authorization is approval for returning payment; the agent must not imply an approval that the record lacks.]]. The answer depends on the relevant facts and rights. I will record your event requirement so the review addresses the problem you actually face.
Laila | The missing scans worry me. Does that mean the parcel is lost?
Tomas | Not by itself. A [[delivery exception::Delivery exception identifies an interruption to the expected process; it requires investigation rather than an invented lost-parcel finding.]] or a delayed update needs investigation. I do not have evidence that establishes loss, and I will not label the shipment delivered without support either.
Laila | Please still call at two if you have not heard back. I need time to arrange something else for the event.
Tomas | I will. The [[service recovery::Service recovery concerns addressing the customer experience after the delay, including accountable follow-up and checking available remedies.]] note will include your concern, the inquiry, and the outstanding answer. You should not have to start the explanation again with another agent.
Laila | Thank you. I need a clear position so I can decide what to do about the event.
Tomas | Understood. We will keep the verified [[dispatch::Dispatch concerns sending the goods; it must remain separate from the still-unconfirmed arrival at the customer's address.]] information separate from arrival and remedy decisions. My next contact is today at two, with the actual position even if some questions remain open.''',
    transfer_title='Give a second delayed-order update',
    transfer_setup='Order V32 was handed to the carrier on 12 June. Its estimated arrival was 14 June. Today is 15 June. A new arrival time is unconfirmed; the agent will update the customer at 16:00.',
    transfer='''Agent: "Carrier handoff occurred on ___." | 12 June | Twelve June is the confirmed physical handoff date, not the estimated arrival.
Customer: "The original estimated arrival was ___." | 14 June | Fourteen June is the supplied estimate that has already passed.
Agent: "The revised arrival time remains ___." | unconfirmed | No new arrival time is established by the facts in this exchange.
Customer: "The next status update is at ___." | 16:00 | Sixteen hundred is the contact commitment and must not become a delivery guarantee.''',
))

BOOK['units'].append(unit(
    title='Conversion, UX, and Digital Analytics',
    scene='A checkout decline with two competing explanations',
    skill='Report a conversion change accurately and distinguish an observed association from a causal claim.',
    brief='Before a checkout redesign, 400 of 1,000 eligible checkout sessions completed a purchase. Afterward, 320 of 1,000 did so. For this report, checkout conversion is completed purchasing sessions divided by eligible checkout sessions; one session counts at most once. A payment-provider outage also occurred in the later period. Event collection and traffic mix have not yet been verified as comparable. Product lead Mara and analyst Dev must explain the decline without claiming that the redesign alone caused it.',
    cast='Mara | Digital product lead\nDev | Commerce analyst',
    culture=('Make a challenge testable', 'A design review can become personal when an unfavorable metric is treated as a verdict on the team. State the measured change, identify competing explanations, and request checks that can distinguish them. Avoid using uncertainty to dismiss a real decline.'),
    a='''What is the later conversion rate? | 32% | 40% | 8% | 20% | Three hundred twenty completed purchasing sessions divided by one thousand eligible sessions equals thirty-two percent.
What is the absolute rate decline? | Eight percentage points | Eight percent relative | Twenty percentage points | Thirty-two percentage points | Forty percent minus thirty-two percent is eight percentage points.
Which causal conclusion is established? | The cause is not isolated by this before-and-after comparison. | The redesign alone caused the decline. | The outage explains every lost purchase. | The decline proves there was no measurement issue. | The outage and unverified comparability prevent this comparison from isolating one cause.''',
    vocabulary='''checkout conversion | Completed purchasing sessions divided by the specified checkout-session base. | measure checkout conversion
conversion funnel | The ordered steps toward a defined customer action. | examine the conversion funnel
checkout abandonment | Failure to complete a purchase after entering checkout. | investigate checkout abandonment
eligible session | A session meeting the stated inclusion criteria. | define eligible sessions
purchase event | A recorded event representing a purchase action. | validate the purchase event
event instrumentation | The implementation of event collection in a digital product. | audit event instrumentation
duplicate event | An event recorded more than once for the same action. | remove duplicate events
deduplication | Identifying and handling repeated records of the same event. | validate deduplication
denominator | The base quantity used in a rate calculation. | keep the denominator consistent
percentage point | One unit of difference between percentage rates. | report a percentage-point change
relative change | A change expressed as a proportion of its initial value. | calculate relative change
traffic mix | The composition of visitors by relevant source or characteristic. | compare traffic mix
device segment | A group of users or sessions using a specified device type. | analyze a device segment
payment failure | An unsuccessful payment attempt under the relevant process. | investigate payment failures
payment gateway | A service connecting a checkout to payment processing. | monitor the payment gateway
provider outage | A disruption to a third-party service. | isolate the provider outage
confounder | A factor that complicates a causal interpretation. | identify a confounder
causal attribution | Assigning an observed outcome to its cause. | qualify causal attribution
controlled experiment | A comparison designed to isolate an intervention's effect. | run a controlled experiment
random assignment | Allocation by chance to comparison groups. | verify random assignment
cohort | A group sharing a defined characteristic or starting event. | define a cohort
user experience (UX) | A person's experience of interacting with a product or service. | assess the user experience
friction | An obstacle making a customer action harder. | reduce checkout friction
rollback | Returning a change to an earlier version. | evaluate a rollback''',
    precision='The conversion rate fell from 40% to 32%: eight percentage points, or a 20% relative decline from the original rate. These are two descriptions of the same change, not interchangeable units.',
    precision_extra='This metric counts sessions completing a purchase, not purchase events or purchased items. A session can contain multiple events. Verify collection, deduplication, eligibility, device mix, and outage exposure before attributing the change.',
    phrases='''State the observed result | Checkout conversion fell from forty to thirty-two percent.
Use the correct absolute unit | That is a decline of eight percentage points.
Give the relative comparison | Relative to the original rate, the decline is twenty percent.
Define the counted outcome | We count a session once if it completes a purchase.
Protect the denominator | Both periods contain one thousand eligible checkout sessions.
Name the competing event | A payment-provider outage overlapped the later period.
Limit causality | This comparison does not isolate the redesign's effect.
Request a measurement check | Has event collection remained consistent across the release?
Separate events and sessions | More purchase events do not necessarily mean more purchasing sessions.
Check composition | Compare traffic and device mix before interpreting the aggregate.
Investigate the outage | Separate affected and unaffected time intervals.
Avoid a new overclaim | That breakdown would be informative, not automatically causal.
Recognize the business problem | Uncertain attribution does not make the decline unimportant.
Define a next analysis | Validate the data, then compare the relevant segments.
Keep a decision conditional | A rollback decision should use the full risk and performance evidence.
Summarize the finding | We have a measured decline and an unresolved explanation.''',
    notes='''Fell from ... to ... | Makes both rates explicit before discussing their difference.
Percentage points | Measures the absolute distance between two percentage rates.
Relative to | Identifies the initial value used for relative change.
Overlapped | Shows co-occurrence without claiming a complete explanation.
Does not isolate | Limits causal inference, not the existence of the observed result.
Not automatically | Prevents a useful diagnostic from becoming an unsupported proof.''',
    d='''Which sentence uses the correct units? | Conversion fell eight percentage points, a twenty-percent relative decline. | Conversion fell eight percent relative and twenty percentage points. | Conversion fell thirty-two percentage points. | Conversion rose because session counts were unchanged. | The absolute difference is eight points; eight divided by the original forty is twenty percent.
Which denominator belongs in this report? | Eligible checkout sessions | Purchased items | All recorded purchase events | Only sessions that purchased | The briefing explicitly defines conversion using the eligible checkout-session base.
Which statement overclaims causality? | The redesign caused the entire decline. | The decline coincided with a provider outage. | Measurement consistency needs checking. | The later rate was thirty-two percent. | A concurrent outage and unverified comparability leave the redesign's isolated effect unresolved.
Which diagnostic is useful but not automatically causal proof? | Compare outage-affected intervals with unaffected intervals while checking their differences. | Assume all missing purchases were outage-related. | Ignore device mix because totals match. | Count duplicate events as separate successful sessions. | Segment comparisons can reveal patterns, but differing populations or timing may still complicate causality.''',
    rehearsal=['Read turns 1-10; say the decline in percentage points and as a relative percentage.', 'Swap roles for turns 11-20; separate purchasing sessions from purchase events.', 'Complete the transfer and check the denominator before explaining the change.'],
    dialogue='''Mara | Checkout is down after the redesign. The release team wants a rollback recommendation this morning. What can we actually conclude from this chart?
Dev | The [[checkout conversion::Checkout conversion uses completed purchasing sessions over eligible checkout sessions, giving forty percent before and thirty-two percent after.]] rate did fall, from forty to thirty-two percent. We should acknowledge that result, but the before-and-after chart alone does not identify the cause.
Mara | I wrote an eight-percent decline in my draft. Is that the clearest description?
Dev | Use eight [[percentage points::Percentage points express the absolute difference between the forty-percent and thirty-two-percent rates.]] for the absolute change. The relative decline is twenty percent because we divide the eight-point difference by the original forty-percent rate.
Mara | Both periods had one thousand checkout sessions. Does that make the comparison fully controlled?
Dev | No. A common [[denominator::Denominator is the rate's base; equal base counts do not guarantee equal populations, conditions, or measurement.]] count does not make the visitors or conditions identical. We still need to verify eligibility, measurement, and the composition of the sessions.
Mara | The payment provider was down during part of the later period. That seems important.
Dev | The [[provider outage::Provider outage names the concurrent service disruption that complicates attributing the whole decline to the redesign.]] is a competing explanation we must investigate. We cannot ignore it, but we also cannot assume it accounts for every missing purchase.
Mara | Can we compare the affected hours with the unaffected hours?
Dev | Yes, while checking [[traffic mix::Traffic mix describes the composition of sessions; differences between intervals can complicate interpreting their conversion rates.]]. Those intervals may attract different visitors. The breakdown can identify patterns, but it is not automatically a controlled estimate of the redesign's effect.
Mara | The developers changed some analytics code during the release. Could that affect the result?
Dev | We should audit [[event instrumentation::Event instrumentation is the collection implementation; a change can alter what is recorded even when behavior is unchanged.]]. Confirm that checkout entry and completion are captured consistently. Otherwise an apparent behavior change may include a measurement change.
Mara | The purchase-event count is higher than the number of purchasing sessions. Is the dashboard necessarily wrong?
Dev | Not necessarily. Check [[deduplication::Deduplication handles repeated records; the session-based definition also requires counting each purchasing session at most once.]] and the metric definition. This report counts each eligible purchasing session at most once, not every purchase event or every item purchased.
Mara | So the same session could produce several recorded events without becoming several successful sessions.
Dev | Exactly. Then examine each relevant [[device segment::Device segment groups sessions by device type, allowing the team to locate patterns hidden by the aggregate rate.]]. A mobile-specific issue would be useful to locate, but we should not invent one before seeing the breakdown.
Mara | We still need to make a release decision. Which checks can we finish first, and what would remain uncertain afterward?
Dev | Agreed. Evaluate a [[rollback::Rollback returns to an earlier version; deciding on it requires the relevant operational risks and evidence, not a fabricated causal certainty.]] alongside the actual risks and diagnostics. My caution concerns the explanation, not whether the decline deserves urgent attention.
Mara | I will report the two rates, the outage, and the checks we are doing before claiming a cause.
Dev | That keeps [[causal attribution::Causal attribution assigns an outcome to a cause; this comparison supports an observed decline but not an isolated redesign effect.]] honest. We have a real reported decline, several testable questions, and a clear next analysis. That is more useful than blaming the release from one chart.''',
    transfer_title='Explain a second conversion comparison',
    transfer_setup='A fixed report counts 300 purchasing sessions out of 600 eligible sessions before a change and 240 out of 600 afterward. One session counts at most once.',
    transfer='''Lead: "The original rate was ___." | 50% | Three hundred purchasing sessions divided by six hundred eligible sessions equals fifty percent.
Analyst: "The later rate was ___." | 40% | Two hundred forty purchasing sessions divided by six hundred eligible sessions equals forty percent.
Lead: "The absolute decline was ___." | ten percentage points | Fifty percent minus forty percent is an absolute ten-percentage-point difference.
Analyst: "The relative decline was ___." | 20% | Ten percentage points divided by the original fifty-percent rate equals a twenty-percent relative decline.''',
))

BOOK['units'].append(unit(
    title='Marketplace and Vendor Management',
    scene='The supplier with more defects has the lower rate',
    skill='Challenge a vendor scorecard by specifying the unit, denominator, period, and comparison limits.',
    brief='A July scorecard shows Vendor K with ten defective units and Vendor M with five. The heading says K has the higher defect rate. Receiving records show 800 units received from K and 200 from M in July. Count each defective unit once, even if it has several faults; all counts refer to these July receipts. Product mix and inspection intensity have not been confirmed as comparable. Vendor manager Rosa and supplier representative Malik must correct the rate comparison before discussing causes or commercial deductions.',
    cast='Rosa | Vendor manager\nMalik | Supplier representative',
    culture=('Make the disputed number reproducible', 'Supplier discussions can become adversarial when a scorecard is treated as unquestionable. Ask for the counted unit and denominator, then do the calculation together. Correcting a ranking does not excuse the underlying defects or establish which party caused them.'),
    a='''What is Vendor K's defective-unit rate? | 1.25% | 10% | 5% | 2.5% | Ten defective units divided by eight hundred received units equals one point two five percent.
What is Vendor M's defective-unit rate? | 2.5% | 1.25% | 5% | 0.625% | Five defective units divided by two hundred received units equals two point five percent.
What remains unverified? | Comparable product mix and inspection intensity | K's July received count | M's July defective-unit count | The stated counting rule | The brief explicitly leaves product mix and inspection intensity unconfirmed as comparable.''',
    vocabulary='''vendor scorecard | A report comparing supplier performance against defined measures. | correct a vendor scorecard
defective-unit rate | Defective units divided by the specified unit population. | calculate the defective-unit rate
defect count | The number of individual faults identified. | distinguish the defect count
received units | Units recorded as received within the defined scope. | confirm received units
inspection intensity | The extent or frequency of examination. | compare inspection intensity
product mix | The composition of products within a measured group. | control for product mix
reporting period | The time interval covered by a measure. | specify the reporting period
purchase order | A buyer's formal order specifying the relevant purchase terms. | reconcile the purchase order
vendor allowance | A supplier-funded amount under agreed commercial terms. | verify a vendor allowance
chargeback | A commercial deduction or charge asserted under applicable terms. | dispute a vendor chargeback
supplier corrective action | An action addressing an established supplier-related problem. | request supplier corrective action
root cause | The underlying reason for a problem, supported by investigation. | establish the root cause
acceptance criterion | A requirement used to determine whether goods meet expectations. | confirm the acceptance criterion
inspection record | Evidence of what was examined and found. | retrieve the inspection record
sample size | The number of units examined in a sample. | state the sample size
lot | A defined group of goods identified for traceability. | trace the affected lot
return to vendor | Sending goods back to the supplying party. | authorize a return to vendor
marketplace listing | A product offer displayed on a marketplace. | update the marketplace listing
seller of record | The party identified as the seller for the transaction. | identify the seller of record
catalog attribute | A structured product detail such as size or material. | correct a catalog attribute
content compliance | Conformity with applicable product-content requirements. | review content compliance
service-level agreement | Terms defining expected service performance and responsibilities. | review the service-level agreement
dispute evidence | Records supporting a challenge to a claim or deduction. | submit dispute evidence
remediation plan | A defined set of actions to address a problem. | agree a remediation plan''',
    precision='A count is not a rate. K has more defective units but a lower defective-unit rate: 10/800 = 1.25%, compared with M at 5/200 = 2.5%. Each defective unit is counted only once.',
    precision_extra='A lower observed rate does not prove better inherent quality when inspection and product mix differ. The scorecard does not itself establish root cause, supplier liability, or the right to a commercial deduction.',
    phrases='''Ask for the base | What received-unit denominator is behind this rate?
State the period | Both figures refer to July receipts.
Clarify the counted object | Count each defective unit once, not every fault separately.
Correct the label | Ten is a count, not a percentage.
Show the calculation | Ten divided by eight hundred gives 1.25%.
Compare accurately | K has the larger count but the lower observed rate.
Keep defects visible | Correcting the ranking does not remove the ten defective units.
Check comparability | Were product mix and inspection intensity comparable?
Request traceable evidence | Please link the findings to the relevant lots and inspection records.
Avoid an unsupported cause | These numbers do not establish how the damage occurred.
Separate commercial authority | A scorecard result does not automatically authorize a deduction.
Check the terms | We need the applicable agreement before deciding any chargeback.
Keep the challenge constructive | I am challenging the rate label, not dismissing the reported defects.
Agree a correction | Let us republish the rates with their denominators.
Define the follow-up | Review the defect evidence and the comparison basis separately.
Close the dispute precisely | The arithmetic is corrected; the cause and commercial outcome remain open.''',
    notes='''Observed rate | Restricts the comparison to recorded data, not inherent supplier quality.
Count each ... once | Defines the unit and prevents double-counting multiple faults.
Behind this rate | Requests the denominator supporting the displayed percentage.
Not dismissing | Preserves the substantive concern while challenging its description.
Automatically | Flags an unsupported leap from a metric to an entitlement.
Remain open | Keeps unresolved questions distinct from the corrected arithmetic.''',
    d='''Which ranking is arithmetically correct? | K has a lower defective-unit rate than M. | K has a higher rate because ten exceeds five. | Both rates are equal because both have defects. | M's rate is five percent regardless of receipts. | K's 1.25% rate is below M's 2.5% rate on the stated received-unit bases.
If one unit has three faults, how is it counted here? | As one defective unit | As three defective units | As three received units | As no defective units | The case explicitly counts each defective unit once regardless of its number of faults.
Which claim still needs investigation? | K has better inherent quality under comparable conditions. | K received 800 units in July. | M had five defective units. | K's observed rate is 1.25%. | Product mix and inspection intensity may differ, so inherent comparative quality is not established.
Which action is not authorized merely by the scorecard? | Deducting a chargeback from the supplier's invoice | Correcting the rate arithmetic | Stating the received-unit counts | Requesting inspection records | Commercial deductions require their applicable terms and basis, not just a performance label.''',
    rehearsal=['Read turns 1-10; challenge the rate using each vendor\'s received-unit denominator.', 'Swap roles for turns 11-20; distinguish a corrected metric from a supported chargeback.', 'Complete the transfer and count each defective unit only once.'],
    dialogue='''Rosa | Your July scorecard is flagged red: ten defective units, compared with M\'s five. Before the review, can we check whether that ranking uses the right base?
Malik | Could we check the [[received units::Received units supply the stated rate denominator; ten and five alone are counts rather than rates.]] behind those figures? I am not disputing the ten reported units, but the heading compares rates while the table only shows counts.
Rosa | The receiving file has eight hundred units from K and two hundred from M.
Malik | Then our [[defective-unit rate::Defective-unit rate divides defective units by received units here, yielding 1.25 percent for K and 2.5 percent for M.]] is one point two five percent, while M's is two point five percent. The larger defect count does not make our rate higher.
Rosa | You are right about the calculation. We should correct that before it goes into the supplier review.
Malik | Please also state the [[reporting period::Reporting period fixes both numerator and denominator to July receipts so the comparison does not mix intervals.]]. I understand these counts all refer to July receipts. A rate could still be misleading if the defects came from a different receipt period.
Rosa | They all relate to July. Some units had several faults; the inspection team counted each affected unit once.
Malik | Good. That distinguishes defective units from [[defect count::Defect count counts individual faults; several faults on one unit must not become several defective units in this metric.]]. We should preserve that rule in the scorecard so next month's calculation does not silently change.
Rosa | Does the lower rate mean K has better quality overall?
Malik | It is a lower observed rate, but we need to compare [[product mix::Product mix describes the goods included; different products can limit a claim about inherent comparative supplier quality.]] and inspection intensity before making that broader claim. I would not use the corrected arithmetic to dismiss the ten units.
Rosa | The inspection details should tell us what failed and how the goods were examined.
Malik | Please share the relevant [[inspection record::Inspection record supplies traceable findings and examination details needed to investigate the reported defective units.]] through the agreed channel. We can review the lot references and acceptance criteria rather than argue over an unexplained total.
Rosa | Operations suspects the packaging caused the damage, but the report has not established that.
Malik | Then packaging is a hypothesis, not a confirmed [[root cause::Root cause is the supported underlying reason; the conversation supplies only an unconfirmed packaging hypothesis.]]. We should examine the evidence and handling history before assigning responsibility. A useful correction depends on identifying the actual problem.
Rosa | Commercial wants to deduct a fee from the next invoice. Which inspection records and contract terms do we need to review with you first?
Malik | Any [[chargeback::Chargeback is a commercial deduction or charge whose basis must follow the applicable agreement, not the scorecard alone.]] needs the applicable terms and evidence. Correcting the rate does not decide that question, and the original heading does not automatically establish a right to deduct.
Rosa | I will separate the metric correction from the quality investigation and the commercial discussion.
Malik | That works. We can agree a [[remediation plan::Remediation plan sets out actions addressing the problem once the evidence supports what needs to change.]] when the findings support the actions. Let us not promise a packaging change merely to close the meeting.
Rosa | I will republish both denominators, the July period, and the corrected percentages. The ten affected units will remain visible.
Malik | Thank you. The revised [[vendor scorecard::Vendor scorecard should present defined measures accurately while leaving unresolved cause and commercial questions visible.]] will then support a fair discussion. We can acknowledge the quality concern while keeping the arithmetic, causal investigation, and contract issues distinct.''',
    transfer_title='Correct a second supplier ranking',
    transfer_setup='For the same month, Vendor P has six defective units among 600 received; Vendor Q has four among 200. Count each defective unit once.',
    transfer='''Manager: "P's defective-unit rate is ___." | 1% | Six divided by six hundred equals one percent on the specified received-unit basis.
Supplier: "Q's defective-unit rate is ___." | 2% | Four divided by two hundred equals two percent on the specified received-unit basis.
Manager: "The larger defective-unit count belongs to ___." | P | P has six defective units compared with Q's four, so its count is larger.
Supplier: "The higher defective-unit rate belongs to ___." | Q | Q's two-percent rate exceeds P's one-percent rate despite Q's smaller defective-unit count.''',
))

BOOK['units'].append(unit(
    title='Customer Service and Escalations',
    scene='A return request beyond the goodwill window',
    skill='Acknowledge a customer request, explain a bounded exception review, and distinguish policy from applicable rights.',
    brief='Customer Owen wants to return an unworn $80 jacket because he changed his mind. His request is on day 35; the retailer states a 30-day change-of-mind return window for this purchase. No fault or misdescription is alleged. Agent Elena cannot approve a goodwill exception but can submit a review to the store manager. No review outcome is supplied. Before treating the policy as decisive, the team must check any applicable customer rights and transaction facts. A fault complaint would require a different assessment, not an automatic rejection under the goodwill window.',
    cast='Owen | Customer\nElena | Service representative',
    culture=('Empathy is not an approval formula', 'An apologetic tone can accidentally sound like a refund commitment. Acknowledge the inconvenience, then state exactly what can happen next. Avoid describing a customer as difficult merely because the requested remedy is outside your authority.'),
    a='''Why does Owen want to return the jacket? | He changed his mind. | The jacket is alleged to be faulty. | The wrong product was delivered. | A recall notice requires its return. | The briefing specifies a change of mind and supplies no fault or misdescription allegation.
What can Elena authorize herself? | Submission of a manager review, not approval of the exception | An immediate $80 refund | A guaranteed exchange | A binding extension of every return window | Elena can submit the request but does not hold the stated exception-approval authority.
How should the 30-day policy be treated? | As a stated policy that does not override applicable rights | As a universal legal limit for every transaction | As irrelevant to any review | As proof the jacket is defective | The policy informs the request, but actual customer rights and transaction facts still require checking.''',
    vocabulary='''change-of-mind return | A return requested because the customer no longer wants the item. | handle a change-of-mind return
return window | The period specified for a return under particular terms. | check the return window
goodwill exception | A discretionary departure from policy where permitted. | request a goodwill exception
exception authority | The defined power to approve a policy departure. | confirm exception authority
proof of purchase | Evidence identifying a purchase and its relevant details. | verify proof of purchase
purchase channel | The route through which the customer bought the item. | identify the purchase channel
item condition | The physical state of a product. | assess item condition
original payment method | The payment route used for the original purchase. | verify the original payment method
store credit | Value available for a future purchase from the retailer. | explain store credit
exchange | Replacing a purchased item with another under relevant terms. | authorize an exchange
refund | Return of an amount paid. | confirm a refund
manager review | Assessment by the person assigned the relevant decision authority. | submit a manager review
fault allegation | A customer's statement that a product has a defect. | record a fault allegation
misdescription | A mismatch between an item and its stated description. | investigate misdescription
applicable rights | Customer protections relevant to the actual transaction. | check applicable rights
statutory remedy | A remedy arising under the relevant law. | distinguish a statutory remedy
policy discretion | Permitted choice within an organization's policy authority. | explain policy discretion
escalation route | The defined path to a higher or specialist review. | offer an escalation route
complaint record | A documented account of a customer's concern and its handling. | maintain a complaint record
case owner | The person responsible for coordinating the case. | identify the case owner
review outcome | The result of an assessment. | communicate the review outcome
reason code | A structured label describing the basis for a transaction or request. | select the correct reason code
resolution option | A possible way to address the customer's concern. | verify resolution options
service handoff | Transfer of relevant context and responsibility to another team member. | complete a service handoff''',
    precision='This is a change-of-mind request on day 35, not an established fault claim. Record the actual reason accurately. The 30-day policy is a fictional retailer rule for this purchase, not a universal statement of consumer law.',
    precision_extra='Submitting a review does not approve a refund, exchange, or store credit. Applicable rights must be checked separately; a retailer cannot replace a required remedy with discretionary goodwill merely by changing the label.',
    phrases='''Acknowledge the request | You would like to return the unworn jacket because you changed your mind.
Identify the timing | This request is on day thirty-five.
State the policy carefully | The stated change-of-mind window for this purchase is thirty days.
Keep rights separate | We also need to check the rights applicable to the actual transaction.
Explain your authority | I can submit the request, but I cannot approve an exception myself.
Offer the real next step | I can refer this to the store manager for review.
Avoid a guaranteed outcome | Submission does not guarantee a refund or exchange.
Request relevant evidence | Please provide the purchase details through our approved process.
Respect the customer's choice | Would you like me to submit that review?
Record the correct reason | I will record this as a change-of-mind request.
Distinguish a new allegation | If you are reporting a fault, I need to record and assess that separately.
Avoid an invented substitute | Store credit has not been approved either.
Reduce repetition | I will include the details you have already supplied.
Name the decision-maker | The manager holds the stated exception authority.
Keep the handoff useful | The record will show the timing, reason, item condition, and requested remedy.
Close honestly | I will communicate the actual review outcome without promising it in advance.''',
    notes='''For this purchase | Limits a policy statement to its actual transaction context.
I can ... but I cannot | Separates a permitted action from an unheld authority.
Would you like | Seeks the customer's choice about the offered review.
Has not been approved | Prevents an alternative remedy from being implied as available.
If you are reporting | Distinguishes a new factual allegation requiring a different assessment.
Without promising | Preserves a clear process commitment while leaving the decision open.''',
    d='''Which sentence stays within Elena's authority? | I can submit a manager review, but I cannot guarantee its outcome. | I can guarantee the manager will approve this. | Store credit is automatically yours because a refund is unavailable. | I have extended the policy for every customer. | Elena can submit the request but cannot approve or promise the review result.
Which record best matches the stated request? | Change of mind; unworn jacket; day 35; $80 purchase | Confirmed product defect; refund approved | Misdescription established; exchange mandatory | Customer withdrew the request | The correct record preserves the actual reason, condition, timing, and amount without inventing an outcome.
Which response to a newly alleged fault is appropriate? | Record the allegation and assess the applicable rights and process separately. | Reject it automatically because the goodwill window ended. | Change the label to avoid an investigation. | Promise a refund before checking any facts. | A fault allegation raises a different assessment and cannot be decided merely from this change-of-mind policy.
Which phrase asks permission without implying approval? | Would you like me to submit the review? | Your refund is being processed. | The manager has accepted the request. | Your exception is guaranteed. | The question offers a specific submission action while leaving the review decision unmade.''',
    rehearsal=['Read turns 1-10; acknowledge the request without promising an exception.', 'Swap roles for turns 11-20; keep a change-of-mind request distinct from a fault report.', 'Complete the transfer and identify who submits the request and who decides it.'],
    dialogue='''Owen | I paid eighty dollars for this jacket and have not worn it. I chose the wrong style. I am five days outside the return window; is a review possible?
Elena | You are asking for a [[change-of-mind return::Change-of-mind return accurately identifies Owen's stated reason, rather than inventing a fault or misdescription.]] on day thirty-five. I understand you would prefer not to keep an unworn item. Let me explain what I can do without promising a decision I cannot make.
Owen | The receipt says thirty days. Is there any way to ask someone to look at it?
Elena | Yes. The stated [[return window::Return window is the retailer's stated thirty-day period for this purchase, not a universal legal limit.]] is thirty days for this purchase. We also need to check the actual transaction and applicable rights rather than treat that policy as a universal legal answer.
Owen | I am not saying there is anything wrong with it. I simply chose the wrong style for myself.
Elena | I will record that accurately. I can request a [[goodwill exception::Goodwill exception is a permitted discretionary departure from policy; requesting it does not establish approval or replace applicable rights.]], but I cannot approve one myself. The store manager can assess the request under the relevant process.
Owen | If you send it to the manager, does that mean I will get the money back?
Elena | No. A [[manager review::Manager review is the assessment step Elena can submit; its result is not supplied or guaranteed.]] is a request for a decision, not the decision itself. I do not want you to hear a refund promise when I am offering a review.
Owen | Would store credit be easier? I would be willing to buy something else here.
Elena | I can include that preference, but [[store credit::Store credit is value for a future purchase; it also requires an actual available or approved basis here.]] has not been approved either. I should not present it as an automatic substitute simply because the original request is outside the stated window.
Owen | All right. What information does the manager need from me?
Elena | We need the relevant [[proof of purchase::Proof of purchase identifies the transaction and its details, supporting the review without requiring a fabricated outcome.]], the item condition, and your requested remedy through the approved process. I will include what you have already told me so you do not have to start again.
Owen | I have the receipt and the jacket with its tags. Please submit the request.
Elena | I will. The manager has the [[exception authority::Exception authority identifies who may approve a policy departure; Elena's submission does not transfer that decision power to her.]] described in our process. I will keep your reason and preferred outcomes clear rather than suggest the jacket is faulty to make the request sound stronger.
Owen | Suppose I later notice a fault. Would the thirty-day window automatically rule that out too?
Elena | A [[fault allegation::Fault allegation is a reported defect requiring its own assessment; it must not be automatically rejected under the goodwill window.]] would need to be recorded and assessed separately under the applicable rights and facts. I cannot decide that hypothetical claim from the change-of-mind policy alone.
Owen | That is clear. For now, it is just the style, and I would like the review.
Elena | The [[complaint record::Complaint record preserves the customer's actual concern, supplied details, and handling without turning a request into an approved remedy.]] will show the eighty-dollar jacket, unworn condition, day thirty-five, and your preference. It will not say a refund or exchange has already been agreed.
Owen | Please include the receipt details in the handoff. I would rather not start again when the manager responds.
Elena | I will preserve that in the [[service handoff::Service handoff transfers accurate context and responsibility, including the distinction between a submitted review and its eventual outcome.]]. The next response should communicate the actual assessment and explain the available next step, not make you reconstruct this conversation.''',
    transfer_title='Keep another review within its authority',
    transfer_setup='A customer requests a change-of-mind return on day 22 under a stated 14-day policy. Agent Noor may submit a review to manager Beth but cannot approve it. No outcome is supplied.',
    transfer='''Noor: "The request is on day ___." | 22 | Twenty-two is the request day stated for this separate transaction.
Customer: "The stated policy window is ___ days." | 14 | Fourteen days is the fictional policy period, not an invented universal legal rule.
Noor: "The manager reviewing the request is ___." | Beth | Beth is the named manager; Noor only submits the review.
Customer: "Submission does not guarantee ___." | approval | A submitted review is not the same as an approved exception or remedy.''',
))

BOOK['units'].append(unit(
    title='Store Operations and Omnichannel Execution',
    scene='Ready online, incomplete on the pickup shelf',
    skill='Give an actionable shift handoff that corrects a false pickup status without hiding the missing item.',
    brief='At 16:00, pickup order P64 shows ready online. It contains three items: a notebook, a pen set, and a mug. Staff have located and staged the notebook and pen set, but cannot find the mug. No substitute has been approved. Outgoing lead Talia must hand the issue to incoming lead Evan, who will contact the customer and update the case at 16:30. The local process requires every ordered item to be verified and staged before the whole order is marked ready. Partial pickup needs the permitted process and the customer\'s agreement.',
    cast='Talia | Outgoing shift lead\nEvan | Incoming shift lead',
    culture=('Handover language must support the next action', 'A cheerful all sorted can conceal an unfinished customer problem. Name the item, the physical status, the system discrepancy, and the next owner. The incoming colleague needs enough detail to act without repeating the search or misleading the customer.'),
    a='''Which item has not been located? | The mug | The notebook | The pen set | All three items | The briefing identifies the mug as missing while the other two items are staged.
What does the local whole-order ready status require? | Every ordered item verified and staged | Any one item scanned | A label printed | A shift handoff completed | The local rule requires all ordered items, not just part of the order, to be verified and staged.
Who owns the next customer contact? | Evan | Talia after she leaves | An unnamed carrier | The customer | Evan is the incoming lead assigned to contact the customer and update the case.''',
    vocabulary='''omnichannel | Coordinated retail activity across store and digital channels. | coordinate omnichannel execution
buy online, pick up in store (BOPIS) | Ordering online for collection at a store. | fulfill a BOPIS order
click and collect | An online order collected from a designated location. | manage click-and-collect orders
order management system (OMS) | Software coordinating order information and fulfillment status. | update the OMS
point of sale (POS) | The system or place where a retail sale is processed. | reconcile POS records
picking | Retrieving the specified items for an order. | complete order picking
pick list | A list of items and quantities to retrieve. | verify the pick list
staging | Placing picked items in the designated holding area. | confirm order staging
pickup shelf | The area holding orders prepared for collection. | check the pickup shelf
ready-for-pickup status | A status indicating the specified readiness conditions are met. | correct ready-for-pickup status
short pick | A pick in which the required quantity cannot be found or supplied. | record a short pick
item-level status | The state recorded for an individual order item. | update item-level status
order-level status | The overall state recorded for the complete order. | correct order-level status
substitution | Supplying a different item in place of the ordered one. | confirm a substitution
customer consent | The customer's agreement to a proposed action. | obtain customer consent
partial pickup | Collection of only part of the ordered items. | arrange partial pickup
pickup notification | A message telling the customer about collection readiness. | correct a pickup notification
collection verification | Checking the required identity or order details at pickup. | complete collection verification
cancellation line | An order item recorded for cancellation under the process. | confirm a cancellation line
refund status | The actual stage of returning the relevant payment. | verify refund status
shift handoff | Transfer of work status and responsibility between shifts. | give a shift handoff
action owner | The person responsible for a specified next action. | name the action owner
discrepancy log | A record of mismatches requiring follow-up. | update the discrepancy log
resolution checkpoint | A scheduled point to review progress on an open issue. | set a resolution checkpoint''',
    precision='Two staged items do not make this three-item order ready under the stated local process. A missing mug is not evidence that it was collected, canceled, or refunded. Keep each status tied to its actual event.',
    precision_extra='Partial pickup and substitution are different options. Neither should be assumed from silence or staff convenience. Use the permitted process, obtain the necessary customer agreement, and preserve the remaining item and payment status.',
    phrases='''Start with the order | This handoff concerns pickup order P64.
State the verified items | The notebook and pen set are located and staged.
Name the gap | The mug has not been found.
Identify the contradiction | The website says ready, but the order is incomplete.
Apply the local rule | Whole-order readiness requires all three items to be verified and staged.
Correct the visible status | We need to correct the ready message through the approved process.
Protect the remaining items | Keep the two staged items identified with this order.
Reject an assumed substitute | No substitute has been approved.
Offer a bounded choice | Check whether partial pickup is permitted and whether the customer agrees.
Assign the next action | Evan will contact the customer.
Set the checkpoint | Update the case at 16:30.
Limit the promise | That is a review time, not a promise that the mug will be found.
Keep money status separate | Do not mark a refund complete unless it has actually reached that status.
Reduce repeated work | Record which locations have already been checked.
Preserve the open item | The mug remains unresolved until its actual disposition is recorded.
Close the handoff | Confirm the owner, customer message, and outstanding item before leaving.''',
    notes='''Located and staged | Describes physical preparation, not simply a system entry.
Has not been found | States the search result without inventing theft or cancellation.
Through the approved process | Makes the correction traceable and properly authorized.
Whether ... and whether ... | Separates process permission from customer agreement.
Not a promise | Keeps a scheduled checkpoint from becoming a guaranteed result.
Actual disposition | Refers to what truly happened to the missing order line.''',
    d='''Which handoff is actionable? | P64: two items staged, mug missing, ready status incorrect; Evan contacts customer and updates at 16:30. | P64 is sorted; the next shift can check later. | All items are ready because the website says so. | The mug must have been collected because it is absent. | The detailed handoff preserves physical facts, the system mismatch, responsibility, and the next checkpoint.
Which substitution claim is supported? | No substitute has been approved. | Any similar mug may be supplied without agreement. | The pen set replaces the mug automatically. | Silence from the customer confirms a substitution. | The briefing explicitly leaves substitution unapproved and does not supply customer consent.
What does 16:30 mean? | A case-update checkpoint | Guaranteed completion of the missing-item search | A confirmed refund completion time | Automatic cancellation of the whole order | Sixteen thirty is the scheduled update, not proof of any particular resolution outcome.
Which record would invent an event? | Marking the missing mug as collected because staff cannot find it | Keeping the mug unresolved | Recording the two staged items | Correcting the unsupported ready message | Failure to locate an item is not evidence that the customer collected it.''',
    rehearsal=['Read turns 1-10; compare the ready message with the three actual item states.', 'Swap roles for turns 11-20; confirm the contact owner and update time.', 'Complete the transfer without turning a review time into a promise of stock.'],
    dialogue='''Talia | Can I hand over P64 before I leave? It says ready online, but I can only account for the notebook and pen set on the pickup shelf.
Evan | Then the [[order-level status::Order-level status describes the whole order; ready is unsupported when one of the three required items is missing.]] does not match the physical position. Which item is missing, and have we confirmed the other two belong to this order?
Talia | The mug has not been found. The notebook and pen set are identified for P64 and are already in the designated holding area.
Evan | Keep that [[staging::Staging places the picked items in the holding area; it confirms preparation of two items, not completion of all three.]] information in the handoff. We should protect those items while we investigate the mug, not return them to general stock without a proper reason.
Talia | The online message may already have encouraged the customer to come in. We need to correct that before they make an unnecessary journey.
Evan | I will address the [[pickup notification::Pickup notification communicates collection readiness; an inaccurate ready message needs correction and direct customer follow-up.]] and contact the customer. Our local process requires all three items to be verified and staged before the entire order is ready.
Talia | Could we tell them to collect the two items while we continue the search?
Evan | We can check whether [[partial pickup::Partial pickup supplies only part of the order and needs the permitted process plus the customer's agreement here.]] is permitted and ask whether that works for them. We should not assume they want two trips or silently treat the missing line as complete.
Talia | There is another mug on display, but it is not the one ordered. Please check with the customer before offering it as a substitute.
Evan | Then there is no approved [[substitution::Substitution provides a different item; the nearby mug cannot replace the ordered one without the necessary approval and agreement.]]. Similar appearance is not enough. The customer may have chosen the specific size or design for a reason.
Talia | I will list the locations already checked so your team does not repeat the same search.
Evan | Good. Record the [[short pick::Short pick identifies the unfulfilled picking quantity, keeping the missing mug visible instead of treating the order as complete.]] against the mug and preserve the actual item details. Do not infer theft, collection, or cancellation simply because we cannot find it.
Talia | You will own the customer contact after the shift change. Shall we set a review at half past four?
Evan | Yes. I am the [[action owner::Action owner identifies Evan as responsible for the next customer contact, preventing the task from being lost between shifts.]], and I will update the case at sixteen thirty. That gives the team a clear next contact without promising the mug will be found by then.
Talia | If the customer asks to cancel the missing item, we should follow the actual cancellation and payment process.
Evan | Correct. Keep [[refund status::Refund status records the actual payment-return stage; a cancellation request or missing item does not itself establish a completed refund.]] separate from the request. We must not tell the customer money has been returned before that is supported by the relevant record.
Talia | I will leave P64 open with two staged items, the missing mug, the incorrect ready message, and the search history.
Evan | Add those points to the [[discrepancy log::Discrepancy log preserves the mismatch between physical items and system status, together with ownership and follow-up information.]]. I will correct the customer-facing position through the approved process and make the offered options explicit when we speak.
Talia | That is everything from my side. Please confirm that you have the order details and the scheduled update.
Evan | Confirmed. The [[resolution checkpoint::Resolution checkpoint is the scheduled progress review at sixteen thirty, not an automatic completion or refund event.]] is sixteen thirty, and the mug remains unresolved. I will carry the customer contact and record the actual next decision instead of allowing the ready label to stand.''',
    transfer_title='Give a second pickup handoff',
    transfer_setup='Order C17 contains four items. Three are staged; a desk lamp is missing. Incoming lead Jun owns the next customer contact and will update the case at 18:00. No substitute is approved.',
    transfer='''Outgoing lead: "The order reference is ___." | C17 | C17 identifies the particular pickup order that needs the handoff.
Jun: "The missing item is the ___." | desk lamp | The desk lamp is the unstaged item, not one of the three already prepared.
Outgoing lead: "The next contact owner is ___." | Jun | Jun is explicitly assigned responsibility for contacting the customer after the handoff.
Jun: "The next case update is at ___." | 18:00 | Eighteen hundred is the update checkpoint, not a guaranteed completion time.''',
))
