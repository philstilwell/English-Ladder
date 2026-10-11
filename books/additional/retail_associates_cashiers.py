"""Original split-tender, shelf-capacity, and net-weight conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="One sale, two ways to pay",
        skill="Explain a completed split-tender receipt without confusing cash handed over, cash retained, sale value, and gift-card balance.",
        setup="Fictional completed sale: total $42.60, including all charges. The shopper used $15 from a gift card that previously held $20, then handed over $50 cash. The remaining $27.60 was paid in cash and $22.40 change returned. Both payments succeeded. Cashier Inez and supervisor Omar review the receipt; no refund is requested.",
        cast="Inez|Cashier\nOmar|Supervisor",
        dialogue="""Inez|Could you check how I'm explaining this receipt? It shows forty-two sixty for the sale, fifteen on a gift card, and fifty cash tendered.
Omar|That's a [[split tender::Split tender means one sale paid using more than one payment method; it does not create two separate sales.]]: one sale, two payment methods. The fifty-dollar note isn't all money retained for the purchase.
Inez|The customer asked us to use only fifteen from the twenty-dollar gift card. We did that before the cash portion.
Omar|Then the card's [[remaining balance::Twenty dollars on the gift card minus fifteen redeemed leaves a five-dollar remaining balance.]] is five dollars. Don't describe the original twenty as the amount redeemed.
Inez|After applying fifteen, the screen said twenty-seven sixty still due. That is forty-two sixty minus fifteen.
Omar|Right. That was the [[cash portion::The cash portion is the remaining 27.60 paid toward the sale, not the 50.00 note initially handed over.]] of the sale. The customer handed over fifty to cover it.
Inez|So the difference between the note and that remaining amount is twenty-two forty. We returned that at the counter.
Omar|Yes, that's the [[change::Cash tendered of 50.00 minus the 27.60 cash portion produces 22.40 change.]]. It comes from fifty minus twenty-seven sixty, not fifty minus the whole sale.
Inez|If I subtract the whole forty-two sixty from fifty, I get seven forty. That would ignore the fifteen already paid on the gift card.
Omar|Exactly. You'd be collecting that gift-card portion twice. The [[cash retained::The store retains 27.60 in cash after returning change; this plus 15.00 redeemed equals the sale total.]] is twenty-seven sixty, and the gift-card redemption supplies the other fifteen.
Inez|I can explain that as fifty handed over, twenty-two forty handed back, and twenty-seven sixty applied to the purchase.
Omar|Good. Both methods succeeded, so the sale's [[outstanding amount::Both successful payment portions total 42.60, leaving zero outstanding; the five-dollar gift balance is separate.]] is zero. The five left on the gift card isn't an unpaid part of this sale.
Inez|What if the customer sees two payment lines and thinks we've charged forty-two sixty twice?
Omar|Point to the sale total once, then the two portions: fifteen and twenty-seven sixty. Their sum is forty-two sixty, not eighty-five twenty.
Inez|And the fifty-cash entry records what was handed over, rather than a third payment on top of those portions?
Omar|Correct. Read it with the change entry. Don't add the tendered note to the net cash portion when explaining the total.
Inez|Should I call the twenty-two forty a refund? Money did go back to the shopper during the transaction.
Omar|Call it change. No return or refund is requested here; it was excess cash tendered for this same purchase.
Inez|Then my summary is one completed sale, fifteen gift-card value used, twenty-seven sixty cash paid, twenty-two forty change, and five still on the gift card.
Omar|That's clear. Use the receipt and actual confirmed payment results. This example explains the amounts; it doesn't supply buttons or procedures for another checkout system.""",
        transfer_title="Separate the two remaining balances",
        transfer_setup="A completed $68.25 sale has no additional charges. A gift card held $30; $18 was redeemed. The shopper handed over $60 cash for the remaining $50.25, and the correct change was returned. Both portions succeeded.",
        transfer="""Cashier: The cash applied to the sale is $___ .|50.25|The sale total 68.25 minus the 18.00 gift-card redemption leaves 50.25 paid in cash.
Supervisor: The change returned is $___ .|9.75|Sixty dollars tendered minus the 50.25 cash portion gives 9.75 change.
Cashier: The gift card still holds $___ .|12|The card began with 30 and only 18 was redeemed, leaving 12.
Supervisor: The amount still due on this completed sale is ___ .|zero|The successful 18.00 and 50.25 portions together pay all 68.25; the gift-card balance is separate.""",
        reference=("Shopify: payment methods and split-payment settings", "https://help.shopify.com/en/manual/sell-in-person/getting-started/setup-payment-method/enable-payments"),
    ),
    scenario(
        title="Facings are not the full count",
        skill="Read a shelf plan, calculate a refill, and distinguish moving stock within a store from receiving additional stock.",
        setup="Fictional shelf plan: SKU B24 has three facings across, four units deep per facing, one unit high. Seven units are on the shelf. The stockroom holds one unopened six-unit case plus five loose units, all available. No other locations, sales, damage, or deliveries occur. Mina and Dev plan to fill the assigned space.",
        cast="Mina|Retail associate\nDev|Department lead",
        dialogue="""Mina|The shelf looks almost full from the front, but the refill sheet says we're short. Am I counting the wrong thing?
Dev|Count the actual units, not just the [[facings::Facings are the three front positions across the shelf; each can hold additional units behind it.]]. This plan assigns three front positions to B24, each holding four units deep, including the front unit.
Mina|I counted seven units altogether, including the ones at the back. There aren't four in every position yet.
Dev|The [[shelf capacity::Three facings multiplied by four units deep and one unit high gives twelve units of assigned shelf capacity.]] is twelve: three across, four deep, one high. Seven on hand there means five more will fill the planned space.
Mina|The stockroom has a sealed case marked six and five loose units. I nearly brought the whole case because it was easier to count.
Dev|The [[replenishment quantity::The refill is twelve minus seven, or five units; bringing six would exceed the assigned shelf quantity by one.]] is five units, not one case. The loose five are enough for this refill.
Mina|That lets us leave the six-unit case unopened. The shelf would then have twelve and the stockroom would have six.
Dev|Yes. The [[case pack::The case pack contains six individual units; one case is not the same quantity as one unit or the five-unit refill.]] is six, but it doesn't set the refill quantity. We fill the assigned space from available stock.
Mina|Would I add five to the store's total stock when I record that move? The shelf number is going up by five.
Dev|No. This is an [[internal transfer::Moving five units from stockroom to shelf changes their location, not the store's total quantity.]] from stockroom to shelf, not a new delivery. Total store stock remains eighteen.
Mina|Before the move that was seven on the shelf plus eleven in the stockroom. Afterwards it's twelve plus six.
Dev|Exactly. Keep the [[location quantities::Location quantities change from seven and eleven to twelve and six, while their combined total stays eighteen.]] separate. A shelf increase can have an equal stockroom decrease.
Mina|What if I just pull the seven existing units forward so each front position looks neat? Would that count as the refill?
Dev|It would improve presentation, but it wouldn't add the missing five units. Fronting the stock and replenishing it are different actions.
Mina|I also see a gap next to B24. Could I spread its three facings over that space to make the area look full?
Dev|Use the current plan rather than taking another product's allocation. Check the SKU and shelf label so B24 doesn't end up behind the wrong price.
Mina|So first I use the plan's three positions, then the actual seven-unit count, then move five matching loose units from the stockroom.
Dev|Yes, following the store's handling and rotation process. The arithmetic alone doesn't authorize changing labels, the layout, or stock condition.
Mina|I'll record the locations accurately after the move, with twelve on the shelf and six in the stockroom if the count matches.
Dev|Good. No extra sale or receipt belongs in that record. We've planned a five-unit move within the same eighteen units.""",
        transfer_title="Refill a different shelf",
        transfer_setup="SKU C18 has two facings, five units deep, one high. Four units are on the shelf and nine available units are in the stockroom. Move only enough to fill the assigned shelf. No other stock movements occur.",
        transfer="""Associate: The assigned shelf capacity is ___ units.|ten|Two facings times five units deep times one high equals ten units.
Lead: Move ___ units from the stockroom.|six|Ten capacity minus four already on the shelf gives a six-unit refill.
Associate: The stockroom will retain ___ units.|three|Nine available units minus the six moved leaves three in the stockroom.
Lead: Total store stock remains ___ units.|thirteen|Four plus nine before the move equals ten plus three afterwards; no stock was received or sold.""",
        reference=("Oracle Retail: facings and shelf capacity", "https://docs.oracle.com/en/industries/retail/ai-foundation-cloud-service/25.1.201.0/aifim/assortment-and-space-optimization.htm"),
    ),
    scenario(
        title="The weight behind the price",
        skill="Explain gross, tare, and net weight with consistent units, without deducting packaging twice.",
        setup="Fictional deli label check: filled container gross weight 0.845 kg; correct container tare 0.035 kg; label net weight 0.810 kg. Product price is $12.00 per kg, with no other charges. The label price is $9.72. Shopper Eva and associate Bao compare the label with the weighing record; the tare is already deducted.",
        cast="Eva|Shopper\nBao|Retail associate",
        dialogue="""Eva|Could you explain this label? I saw eight hundred forty-five grams with the container, but the label says eight hundred ten.
Bao|The larger number is the [[gross weight::Gross weight includes product and container; 0.845 kg is not the product-only weight to charge here.]]. It includes the food and container together. The label charges for the food's weight.
Eva|Then the thirty-five-gram difference is the container? I thought perhaps some of the food had been removed between the two numbers.
Bao|It's the [[tare::Tare is the container weight, 0.035 kg or 35 g, deducted from gross to find net product weight.]]: thirty-five grams for this container. Nothing in this record indicates food was removed.
Eva|So eight hundred forty-five minus thirty-five gives eight hundred ten grams. That's what the label is using?
Bao|Yes, the [[net weight::Net weight is 0.845 minus 0.035, or 0.810 kg, after the correct tare has already been deducted.]] is point eight one zero kilograms, which is eight hundred ten grams.
Eva|The price says twelve dollars a kilogram. I shouldn't multiply twelve by eight hundred ten, because that's a number in grams.
Bao|Right. Match the [[unit price::The supplied unit price is twelve dollars per kilogram, so the multiplier must be kilograms rather than grams.]] to kilograms: twelve times point eight one gives nine dollars seventy-two.
Eva|And if the container had been included, twelve times point eight four five would have come to ten dollars fourteen.
Bao|Yes. The [[difference::10.14 based on gross minus the correct 9.72 based on net is 0.42, the price attributable to the container weight.]] would be forty-two cents. The actual nine-seventy-two label already excludes that container weight.
Eva|Could you take the thirty-five grams off the label weight now, just to make sure I don't pay for the packaging?
Bao|That would deduct it [[twice::Tare has already reduced 0.845 kg to 0.810 kg; subtracting it again would understate the product weight.]]. The label says net, so its eight hundred ten grams is already the product-only amount.
Eva|I see. I was comparing a combined weight on the record with a product-only weight on the label, not two measurements of the same thing.
Bao|Exactly. Keeping gross, tare, and net named makes the difference clear. We shouldn't treat every number on the record as another chargeable weight.
Eva|Does the same thirty-five-gram deduction apply to every container you use, or just the one in this check?
Bao|Just the correct container tare supplied here. Different packaging needs its applicable verified tare; we don't carry a convenient number across every container.
Eva|And this calculation doesn't tell us whether a scale is accurate in general? It only shows how these recorded numbers fit together.
Bao|That's right. Actual scales and their use need the required checks. This record lets us explain the price, not certify the equipment.
Eva|Then the food is eight hundred ten grams at twelve dollars a kilogram, and the total here is nine seventy-two.
Bao|Correct, with no additional charges in this case. The container was accounted for once, and the units and label price agree.""",
        transfer_title="Use the net figure once",
        transfer_setup="Gross weight is 1.260 kg, tare 0.060 kg, and the label already shows net 1.200 kg. The price is $7.50 per kg, with no other charges. A gross-weight calculation would incorrectly give $9.45.",
        transfer="""Associate: The labelled net product weight is ___ grams.|1200|1.200 kilograms equals 1200 grams after subtracting the sixty-gram tare.
Shopper: The correct total is $___ .|9.00|1.200 kg multiplied by 7.50 dollars per kg gives 9.00.
Associate: Charging on gross weight would add $___ incorrectly.|0.45|The incorrect 9.45 exceeds the correct 9.00 by 0.45, attributable to packaging weight.
Shopper: The tare must be deducted ___, not again from the net figure.|once|Net already excludes tare; another deduction would subtract the packaging weight twice.""",
        reference=("NIST: grocery scales, packaging tare, and accurate charges", "https://www.nist.gov/how-do-you-measure-it/how-do-you-know-if-grocery-store-scales-are-accurate"),
    ),
]
