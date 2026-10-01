"""Original Retail Associate and Cashier learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='retail-associates-cashiers',
    title='Retail Associate and Cashier English',
    cover_label='ENGLISH FOR THE SHOP FLOOR AND CHECKOUT',
    cover_title='Retail Associate\nand Cashier',
    cover_size=33,
    tagline='Helpful service. Accurate details.',
    audience='For retail associates, cashiers, collection-desk staff, customer-service colleagues, and shift supervisors.',
    map_intro='Eight retail conversations: identify an advertised item, compare garment labels, explain a quantity offer, correct a duplicate scan, discuss an exchange, clarify collection status, offer accessible checkout assistance, and hand over an unverified till difference.',
    notes_title='Helpful does not mean guessing.',
    notes_intro='A strong retail conversation identifies the exact item, explains the relevant condition, and makes the next step clear. Careful language protects the shopper from a wrong variation or price and helps colleagues distinguish checked facts from unfinished work.',
    field_notes=[
        ('Identify before promising stock', 'Color alone may not identify an advertised product. Confirm the item reference, material, size, and location before making an availability claim or offering an unrequested substitute.', '"You mean the medium cotton shirt C218; I have not checked local stock yet."'),
        ('State the condition with the price', 'A two-item offer does not necessarily give one item half the bundle price. State the qualifying quantity and the complete amount for each option without pressuring the shopper to buy more.', '"One bottle is $3; two qualifying bottles are $5."'),
        ('Separate eligibility from completion', 'Meeting a fictional exchange policy does not establish replacement stock. An order acknowledgment is not a collection notice, and correcting an unpaid basket is not the same as issuing a refund.', '"The exchange conditions are met, but I still need to check the larger size."'),
        ('Keep help and handovers specific', 'Ask which assistance the shopper prefers. At shift change, name unfinished checks and their owner without turning a difference into an accusation or an accepted task into a completed one.', '"The recorded count is $5 below expected; the second check is pending and the cause is unknown."'),
    ],
    scope_note='All stores, shoppers, prices, product references, balances, offers, and policies are fictional. This book teaches workplace English, not legal advice, payment-system operation, accounting investigation, or accessibility certification. Follow actual store procedures, product information, payment-security requirements, applicable consumer and accessibility laws, and emergency arrangements. A fictional exchange policy does not replace statutory rights. Ask before providing personal assistance or handling a shopper\'s belongings or mobility aid.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Retail Sales Workers.',
             url='https://www.bls.gov/ooh/sales/retail-sales-workers.htm',
             note='Occupational context for product assistance, promotions, payment, receipts, and exchange-policy communication. The dialogues are original fictional teaching cases.', checked='1 October 2026'),
        dict(title='Federal Trade Commission. Clothes Captioning: Complying with the Care Labeling Rule.',
             url='https://www.ftc.gov/business-guidance/resources/clothes-captioning-complying-care-labeling-rule',
             note='Background for reading actual garment-care information rather than inventing care claims. The book does not prescribe laundering settings or summarize legal penalties.', checked='1 October 2026'),
        dict(title='Federal Trade Commission. Solving Problems With a Business: Returns, Refunds, and Other Resolutions.',
             url='https://consumer.ftc.gov/articles/solving-problems-business-returns-refunds-and-other-resolutions',
             note='Context for distinguishing requested remedies, purchase records, policies, and factual follow-up. The example exchange conditions are fictional, not universal rights.', checked='1 October 2026'),
        dict(title='US Department of Justice. ADA Update: A Primer for Small Business.',
             url='https://www.ada.gov/resources/title-iii-primer/',
             note='Background for accessible customer service and appropriate assistance. The supplied checkout route is fictional and is not an accessibility-compliance assessment.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Finding the item the shopper actually means',
    scene='Which blue shirt?',
    skill='Use a reference, material, and size to identify a product before making an unverified local-stock claim.',
    brief='Shopper Casey asks associate Hana for the blue shirt in an advertisement. The advertisement contains two blue shirts: linen L214 and cotton C218. Casey wants the cotton version in medium, not the linen version or another size. Local availability has not been checked. Hana confirms C218, blue, medium, and cotton before beginning a stock inquiry. No item has been located, reserved, or sold, and the advertisement does not prove that the requested variation is available at this branch.',
    cast='Casey | Shopper\nHana | Retail associate',
    culture=('Clarification is part of helping', 'A shopper may reasonably remember the image rather than an item number. Narrow the choice with a short concrete question, then read back the product details. Avoid making the shopper repeat the whole story or treating a displayed advertisement as proof of local availability.'),
    a='''Which product does Casey mean? | Cotton C218 | Linen L214 | Either blue shirt | A different unmentioned item | Casey identifies the cotton version, whose reference is C218.
Which size is requested? | Medium | Small | Large | Any available size | Medium is the explicit size preference and should not be substituted without agreement.
What is known about local stock? | It has not been checked | The item is definitely available | The item is definitely sold out | One has already been reserved | The conversation identifies the item before any local availability check has occurred.''',
    vocabulary='''item reference | Identifier used to distinguish a product. | confirm the item reference
stock-keeping unit | Internal identifier for a stocked product variation, often abbreviated SKU. | check the stock-keeping unit
barcode | Machine-readable code used to identify an item or record. | scan the barcode
product variation | Specific version differing in size, color, or another feature. | confirm the product variation
colorway | Color version offered within a product range. | identify the blue colorway
size | Labelled dimension category such as medium. | confirm the requested size
cotton | Textile fiber identified for the requested shirt in this case. | identify the cotton version
linen | Different textile fiber used in the other advertised shirt. | distinguish the linen version
fiber content | Information describing the fibers used in a textile. | check the fiber content
advertised item | Product featured in a promotion or advertisement. | identify the advertised item
product image | Picture of a product, not proof of local stock. | compare the product image
range | Group of related products or variations. | identify the product range
local availability | Whether the exact variation is available at the relevant branch. | check local availability
branch | Particular store location within a retailer. | identify the branch
shop floor | Customer-accessible area where merchandise is displayed. | check the shop floor
stockroom | Storage area for merchandise not on the selling floor. | check the stockroom
display sample | Item shown for viewing, not necessarily available for sale. | distinguish a display sample
stock inquiry | Request to check whether a specific item is available. | make a stock inquiry
stock record | System record of recorded merchandise quantities or status. | consult the stock record
physical check | Verification of the actual item and its location. | request a physical check
reservation | Confirmed arrangement to hold an item under the store process. | distinguish a reservation
substitution | Replacement with a different item or variation requiring agreement. | discuss a substitution
specification | Set of details defining the requested item. | repeat the specification
availability claim | Statement that an item can be supplied, requiring support. | avoid an unsupported availability claim''',
    precision='The exact request is blue cotton C218 in medium. Linen L214 is a different item even though it is also blue. Confirming the product does not establish stock, a reservation, or permission to substitute another variation.',
    precision_extra='A stock-keeping unit, item reference, and barcode may identify different levels of detail in a retailer\'s system. Use the actual system correctly and read back the shopper-facing details; do not assume a familiar-looking code proves the size or local availability.',
    phrases='''Narrow the advertisement | The ad shows two blue shirts; do you mean cotton or linen?\nAsk for the size | Which size are you looking for?\nName the selected reference | The cotton shirt is C218.\nDistinguish the other item | L214 is the linen version.\nRead back the request | Blue cotton C218 in medium; is that right?\nSeparate identification and stock | I have identified the item, but I have not checked local availability yet.\nAvoid an advertisement assumption | The advertisement does not confirm stock at this branch.\nConfirm before searching | I will use that exact reference and size for the stock inquiry.\nKeep alternatives optional | I would ask before offering a different size or material.\nAvoid a reservation claim | Nothing has been reserved yet.\nClarify the location | Are you asking about availability at this branch?\nExplain the next step | The next step is to check the requested variation.\nKeep the record precise | Medium cotton, not medium linen.\nAvoid premature certainty | I cannot confirm available or sold out before the check.\nInvite correction | Please tell me if I have the size or material wrong.\nClose the clarification | The item is confirmed; its stock status is still unknown.''',
    notes='''The blue shirt | A shared color may still leave more than one possible item.\nIn medium | In introduces the requested size rather than a different product name.\nCotton versus linen | The material distinction identifies separate advertised products in this case.\nYet | Not checked yet means unresolved, not unavailable.\nAt this branch | Limits the availability question to a specific store location.\nIdentified versus reserved | Identifying the correct item does not create a hold or confirm stock.''',
    d='''Which read-back is accurate? | Blue cotton C218 in medium. | Blue linen L214 in medium. | Any blue shirt in any size. | Cotton C218 in large without asking. | The correct read-back preserves the requested reference, material, color, and size.
Which stock statement is supported? | Local availability has not been checked yet. | The advertisement guarantees one here. | The medium version is sold out. | A copy is already reserved. | No stock inquiry result exists yet, so both availability and reservation claims are unsupported.
Which next step follows the clarification? | Check the exact requested variation. | Substitute linen without asking. | Promise a medium based on the photo. | Mark the sale complete. | The exact item must be checked before discussing verified local availability.
Which distinction should a colleague receive? | C218 is cotton; L214 is linen. | Both references are interchangeable. | Blue proves the same material. | Medium automatically means local stock. | The two references identify different products despite their shared color.''',
    dialogue='''Casey | I am looking for the blue shirt in this advertisement. I liked the picture, but I did not write down the item number.
Hana | There are two blue shirts in the ad. Let us confirm the [[item reference::Item reference distinguishes the two advertised products, preventing the shared color from being treated as enough identification.]] before I check stock. Do you mean the cotton one or the linen one?
Casey | The cotton one, please. I noticed the other blue shirt too, but it is not the material I came in to find.
Hana | The [[cotton::Cotton identifies the requested material and connects the shopper's choice to C218 rather than the linen item.]] version is C218. The linen version has a different reference, L214, even though the colors look similar in the advertisement.
Casey | C218 sounds like the one. I need a medium, not a small. I would rather wait for the right size than take a different one.
Hana | I will keep the [[size::Size is medium, a specific part of the request that should not be replaced with another available size without agreement.]] specific. You are asking for medium in the blue cotton C218, not whichever blue shirt happens to be on the nearest rack.
Casey | Exactly. Does the advertisement mean you have that version here, or does it only show something from the store's range?
Hana | It shows the [[advertised item::Advertised item means the product featured in the promotion; it does not prove that the requested variation is available at this branch.]], but it does not establish stock at this branch. I have not checked local availability for the medium yet.
Casey | That is useful to know. I do not want to hear that it is available and then discover that the only one is a different size.
Hana | The [[product variation::Product variation combines the relevant details, here the blue cotton C218 in medium, which must stay together in the stock inquiry.]] matters. I will keep the reference, material, color, and size together when I make the inquiry.
Casey | Please do. I am asking about this location today, not whether a different branch might have something similar.
Hana | Understood. The first question is [[local availability::Local availability concerns the exact requested item at this branch, not general availability elsewhere or an unrequested substitute.]] here. If we later discuss another location or an alternative, I will make that distinction explicit.
Casey | Has one been put aside already, or are we still at the stage of finding out whether the right shirt is present?
Hana | No [[reservation::Reservation would be a confirmed hold under the store process; none has been made during this identification conversation.]] has been made. We have identified the request, but no item has yet been located or set aside.
Casey | Good. I prefer that clear answer. Would you read the details back once before checking, just so we do not start with the wrong reference?
Hana | The [[specification::Specification summarizes the shopper's exact choice: blue cotton C218, medium, with local stock still unchecked.]] is blue cotton shirt C218 in medium. L214 is the linen shirt and is not the one you want.
Casey | That is right. If there is only linen or another size, please ask me rather than treating it as an equivalent replacement.
Hana | Any [[substitution::Substitution changes the requested item or variation and needs the shopper's agreement rather than an assumption of equivalence.]] would be a separate choice for you. I will not change the material or size simply to turn an uncertain stock result into a sale.
Casey | Thank you. We have found the right product description, so the remaining question is whether this branch actually has it.
Hana | Yes. The next step is the [[stock inquiry::Stock inquiry checks availability after the exact product is identified; its outcome has not yet established available, sold out, or reserved status.]] for that exact variation. Until it is checked, I will not describe it as available, sold out, or reserved.''',
    transfer_title='Identify a different advertised item',
    transfer_setup='An advertisement shows red wool W310 and red cotton C314 sweaters. The shopper wants red cotton C314 in large. Local stock is unchecked, and no item is reserved.',
    transfer='''Associate: "The requested reference is ___." | C314 | C314 identifies the cotton sweater the shopper selects, not the wool alternative.
Shopper: "The requested size is ___." | large | Large is the explicit size choice in this new scenario.
Associate: "Local stock remains ___." | unchecked | Identifying the product does not supply a verified availability result.
Shopper: "Nothing has been ___." | reserved | No hold has been created merely by clarifying the product request.'''
))


BOOK['units'].append(unit(
    title='Comparing fit, materials, and label information',
    scene='The care label decides the comparison',
    skill='Compare stated garment features and care requirements without inventing comfort, fit, or durability claims.',
    brief='Shopper Luis needs a machine-washable jacket and compares two $60 options with associate Priya. Jacket A is unlined and its label permits machine washing. Jacket B is lined and its label says dry-clean only. No other care details, durability tests, or fit measurements are supplied. A meets the stated washing requirement on the available label information; B does not. Luis asks to look at A next but has not tried it on or purchased it. Priya must not infer washing suitability from the presence or absence of a lining.',
    cast='Luis | Shopper\nPriya | Retail associate',
    culture=('Use evidence instead of confident sales language', 'Words such as comfortable, durable, and easy-care can mean different things to different shoppers. Compare the label facts with the stated need, and distinguish a feature from a tested benefit. A useful recommendation can be conditional without sounding evasive.'),
    a='''Which jacket meets the stated machine-washing requirement? | A, according to its label | B, because it is lined | Both, because they cost the same | Neither, because A is unlined | Jacket A's label permits machine washing, while B's says dry-clean only.
What do the two jackets cost? | $60 each | A $30 and B $60 | $60 for the pair | A $60 and B $90 | The brief prices each jacket at sixty dollars, not both together.
What is unverified? | Fit, comfort, and durability | A's unlined construction | B's dry-clean-only label | The stated equal prices | No fitting, comfort evidence, or durability testing has been supplied.''',
    vocabulary='''garment | Item of clothing. | compare the garments
care label | Label stating how a garment should be cared for. | read the care label
machine-washable | Suitable for machine washing under the actual label instructions. | check the machine-washable claim
dry-clean only | Label instruction restricting cleaning to dry cleaning. | explain the dry-clean-only instruction
hand wash | Care instruction specifying washing by hand. | distinguish a hand-wash instruction
lining | Inner layer of a garment. | identify the lining
lined | Made with an inner lining. | describe the lined jacket
unlined | Made without a separate inner lining. | describe the unlined jacket
outer fabric | Material forming the garment's external surface. | identify the outer fabric
fiber blend | Combination of different fibers in a textile. | read the fiber blend
woven fabric | Textile formed by interlacing sets of yarns. | identify woven fabric
knit fabric | Textile formed through interlocking loops. | distinguish knit fabric
seam | Line where pieces of fabric are joined. | inspect the seam
hem | Finished edge of a garment or fabric section. | identify the hem
cuff | Finished section at the end of a sleeve. | compare cuff styles
fastening | Part used to close or secure the garment. | check the fastening
zipper | Sliding fastening with interlocking elements. | inspect the zipper
fit | How the garment sits on the individual wearer. | check the fit
cut | Overall shaping or silhouette of a garment. | compare the cut
size chart | Guide relating labelled sizes to stated measurements. | consult the size chart
measurement | Quantified dimension used to compare fit. | check the measurement
shrinkage | Reduction in dimensions, not ruled out by an unsupported claim. | avoid a shrinkage guarantee
colorfastness | Ability of a textile to retain color under specified conditions. | check colorfastness information
durability claim | Statement about resistance to wear that needs support. | avoid an unsupported durability claim''',
    precision='The care label, not the lining, answers the washing question. A is unlined and permits machine washing; B is lined and says dry-clean only. Do not extend these two examples into a rule about all lined or unlined jackets.',
    precision_extra='Both prices are $60 each. Equal price does not imply equal care, fit, comfort, or durability. The shopper has asked to inspect A, not confirmed that it fits or completed a purchase. Use actual label details for any further care question.',
    phrases='''Ask about the requirement | Is machine washing a requirement for you?\nRead the first label | Jacket A's label permits machine washing.\nRead the second label | Jacket B's label says dry-clean only.\nCompare construction | A is unlined; B has a lining.\nAvoid an inference | The lining alone does not tell us how to clean it.\nState the equal prices | Both jackets are $60 each.\nConnect fact and need | A meets your stated washing requirement on the label information.\nKeep fit separate | We still need to check how it fits you.\nAvoid a comfort claim | I cannot establish comfort from the price or lining alone.\nAvoid a durability promise | We do not have evidence here that one will last longer.\nOffer inspection | Would you like to look at A more closely?\nUse the full label | We should check the actual instructions for any further care detail.\nAvoid invented settings | No washing temperature has been supplied in this comparison.\nClarify purchase status | Looking at A does not mean you have decided to buy it.\nInvite a practical check | You can compare the fit before making your choice.\nSummarize the evidence | Same price, different care instructions, fit still unverified.''',
    notes='''Each versus together | Sixty dollars each does not mean sixty dollars for both jackets.\nPermits versus recommends | Use the actual wording supplied rather than strengthening or changing the instruction.\nOnly | Dry-clean only excludes treating the garment as machine-washable in this comparison.\nFeature versus benefit | A lining is a construction feature, not automatic proof of comfort or durability.\nMeets the requirement | This applies to the specified washing need, not every possible shopping preference.\nNot tried on | Fit remains unverified until the relevant practical check occurs.''',
    d='''Which recommendation uses the supplied evidence? | A meets your machine-washing requirement according to its label. | All unlined jackets can be machine washed. | B must wash well because it costs the same. | A is guaranteed more comfortable. | The recommendation connects the actual label to the shopper's specific requirement.
Which comparison is unsupported? | B will definitely last longer because it has a lining. | Both jackets cost $60 each. | A is unlined. | B's label says dry-clean only. | A lining alone does not establish comparative durability or wear performance.
Which statement preserves the purchase status? | Luis wants to inspect A but has not tried it on or bought it. | Luis has confirmed A fits perfectly. | Both jackets have been purchased. | Asking about A authorizes payment. | Inspection interest does not establish fit or a completed purchase.
What should resolve a further washing-temperature question? | The actual care-label instructions | A guess based on the price | Assuming all cotton settings apply | Copying instructions from a different jacket | The comparison supplies no temperature, so the actual garment information must be checked.''',
    dialogue='''Luis | I need a jacket I can machine wash. These two are the same price, but I am not sure which one fits that requirement.
Priya | Let us check the [[care label::Care label provides the relevant evidence about cleaning, rather than relying on equal price or visual similarity.]] on each. Jacket A permits machine washing, while jacket B says dry-clean only.
Luis | I noticed B has an inner layer and A does not. Is that the reason one needs different care, or should I not assume that?
Priya | B has a [[lining::Lining is a construction feature, not by itself proof of the garment's care requirements or the reason for them.]], and A is unlined. Those are construction details, but the lining alone does not establish the cleaning requirements or their cause.
Luis | Then A is the one to look at for my washing requirement. I do not want to choose B and assume I can wash it anyway.
Priya | On the information here, A is [[machine-washable::Machine-washable reflects A's supplied label instruction, subject to the actual care details rather than invented settings.]] under its label instructions. That meets the specific care requirement you have stated.
Luis | Does dry-clean only mean something stronger than a suggestion that dry cleaning might give a nicer finish?
Priya | Yes. The word [[only::Only limits the stated method for B; it should not be paraphrased as optional dry cleaning or machine-washing permission.]] is important in B's instruction. I should not describe that label as permission to machine wash the jacket.
Luis | Are they really both sixty dollars? I want to make sure one price is not for a different size or for two items together.
Priya | Both are sixty dollars [[each::Each applies the sixty-dollar price separately to either jacket, not to the pair together.]]. The equal prices do not mean the care instructions or other characteristics are identical.
Luis | That helps. I would like to look at A, although I have not tried either one on yet. I still need to see how it sits on me.
Priya | Of course. The [[fit::Fit concerns how the jacket sits on Luis, which has not been established by its label or price.]] is a separate question. Meeting your washing requirement does not tell us whether this particular jacket fits you as you want.
Luis | Could the lined one be more comfortable, though? I have heard people say that, but I do not know whether it applies to these jackets.
Priya | I cannot make a [[comfort claim::Comfort claim would assert an experience not established by the supplied construction and care facts or by Luis trying the jacket.]] from the lining alone. We can compare the stated features without promising how either will feel to you.
Luis | And I suppose the same applies to saying one will last longer. I do not see any test information here.
Priya | Correct. A [[durability claim::Durability claim needs evidence about wear; neither equal price nor the presence of a lining supplies that evidence here.]] would need support. We have not checked evidence that one of these jackets will last longer than the other.
Luis | Please show me A first, then. I want to inspect it and check the fit, not decide to buy before I have looked properly.
Priya | I can help you with that. We can check the [[size chart::Size chart can provide stated measurements for a fitting comparison, without guaranteeing fit before the shopper assesses the actual garment.]] and the actual garment information rather than treating the washing label as a complete recommendation.
Luis | Good. If I have a question about washing temperature later, I will ask to see the actual instructions instead of guessing.
Priya | That is the right detail to verify. The [[washing temperature::Washing temperature has not been supplied in this comparison; the actual label must answer it rather than an invented general setting.]] has not been confirmed in our discussion, and I will not invent one. For now, A meets the stated care requirement, with fit and purchase still open.''',
    transfer_title='Compare another pair of care labels',
    transfer_setup='Jacket C is lined and permits machine washing. Jacket D is unlined and says dry-clean only. Both are $70 each. The shopper requires machine washing and has tried neither on.',
    transfer='''Associate: "Jacket ___ meets the stated washing requirement." | C | C's actual label permits machine washing despite its lined construction.
Shopper: "Both jackets cost seventy dollars ___." | each | Each states the price of either jacket separately, not the pair.
Associate: "Jacket D says dry-clean ___." | only | Only preserves the restriction in D's supplied care instruction.
Shopper: "The ___ remains unverified." | fit | Neither garment has been tried on, so fit is not established.'''
))


BOOK['units'].append(unit(
    title='Resolving shelf prices and offer conditions',
    scene='One bottle is not half the bundle',
    skill='Explain a quantity condition, distinguish average and single-item prices, and respect the shopper choice.',
    brief='Shopper Nia has one juice bottle with a regular single-bottle price of $3. The shelf offer is two qualifying bottles for $5; single bottles remain $3. Nia expects one bottle to cost $2.50. Associate Ben explains that $2.50 is the average per bottle only when buying the qualifying pair. Two at regular prices would cost $6, so the pair saves $1 against that comparison, but it requires $2 more total spending than one $3 bottle. Nia chooses one bottle at $3. No other charges apply in the exercise.',
    cast='Nia | Shopper\nBen | Retail associate',
    culture=('Explain the offer without pushing the extra purchase', 'A lower average price does not necessarily serve a shopper who needs only one item. State the quantity condition and both complete totals neutrally. Distinguish saving against two regular-price items from spending less than the single item already chosen.'),
    a='''What is the price of one bottle? | $3 | $2.50 | $5 | $6 | The offer leaves the single-bottle price at three dollars.
What qualifies for the $5 offer? | Two qualifying bottles | One bottle alone | Any unrelated item | Half a bottle | The stated promotion requires a qualifying pair, not a single item.
Which choice does Nia make? | One bottle at $3 | Two bottles at $5 | One bottle at $2.50 | Two bottles at $3 | Nia chooses the single bottle after the complete comparison is explained.''',
    vocabulary='''shelf label | Displayed product and price information at the shelf. | check the shelf label
multibuy offer | Promotion requiring purchase of a specified number of items. | explain the multibuy offer
qualifying item | Product that meets the offer's stated conditions. | identify a qualifying item
quantity condition | Required number of items for an offer. | state the quantity condition
single-item price | Price charged when buying one item alone. | confirm the single-item price
regular price | Non-promotional price used as the stated comparison. | compare regular prices
bundle total | Complete price for the grouped qualifying items. | state the bundle total
average price | Total divided by the number of items, not necessarily the one-item selling price. | explain the average price
price per item | Amount per individual item under the specified purchase conditions. | compare the price per item
unit pricing | Price stated per standard quantity such as a liter or kilogram. | distinguish unit pricing
comparison basis | Quantity and conditions used to calculate a saving. | identify the comparison basis
saving | Reduction against the specified comparison amount. | calculate the saving
extra spending | Increase in total outlay compared with another purchase choice. | explain the extra spending
minimum purchase | Smallest quantity or spend needed to qualify. | clarify the minimum purchase
mix-and-match | Offer allowing specified different items to form a qualifying group. | check mix-and-match eligibility
exclusion | Item or condition not covered by an offer. | explain an exclusion
promotion period | Dates during which an offer applies. | check the promotion period
loyalty price | Price available under a stated membership condition. | clarify the loyalty price
coupon | Voucher or code offering a benefit under specified terms. | check a coupon
redemption condition | Requirement for using a coupon or offer. | explain redemption conditions
price query | Shopper question about the amount or conditions charged. | resolve a price query
quantity read-back | Confirmation of the number of items selected. | give a quantity read-back
basket total | Total for the shopper's selected goods. | confirm the basket total
purchase preference | Shopper's choice among clearly explained options. | respect the purchase preference''',
    precision='Two bottles for $5 works out to $2.50 per bottle only within that qualifying purchase. It does not change the stated $3 single-bottle price. One bottle and two bottles are different purchase quantities with different complete totals.',
    precision_extra='The pair saves $1 compared with two bottles at $3 each. It still costs $2 more than buying only one $3 bottle. Always name the comparison basis before saying cheaper or saves money; do not imply a larger basket necessarily lowers total spending.',
    phrases='''Acknowledge the calculation | I see how you arrived at $2.50 by dividing the pair price.\nState the condition | The $5 offer applies to two qualifying bottles.\nConfirm the single price | One bottle on its own remains $3.\nExplain the average | $2.50 is the average per bottle when you buy the pair.\nGive both complete totals | One is $3; two qualifying bottles are $5.\nName the comparison | Two at the regular price would cost $6.\nCalculate the saving | The pair saves $1 compared with that $6 total.\nExplain the extra outlay | It is still $2 more spending than buying one bottle.\nAvoid a false single price | The bundle average is not the one-bottle selling price.\nKeep qualification explicit | We should check that both bottles qualify for the offer.\nAvoid adding conditions | No membership condition is stated in this offer.\nRespect the need | You do not have to buy a second bottle to keep the single-item option.\nAsk for the choice | Would you prefer one at $3 or two at $5?\nConfirm the selection | You have chosen one bottle at $3.\nRead back quantity | The selected quantity is one, not the pair.\nClose the query | The offer is clear, and your single-bottle choice remains unchanged.''',
    notes='''For versus each | Two for $5 gives a group price; $3 each describes the regular single price here.\nAverage versus sale price | Division explains the pair's average but does not create a one-item offer.\nCompared with | This phrase names the baseline for a saving claim.\nQualifying | The offer applies only to products meeting the stated terms.\nMore spending versus better value | A lower per-item price can still require a higher total payment.\nChoice versus pressure | Explain both options without treating the larger purchase as the only sensible one.''',
    d='''Which explanation is accurate? | $2.50 is the pair's average per bottle; one alone is $3. | One bottle must be $2.50 because five divided by two is 2.5. | The offer requires three bottles. | All juice products are automatically included. | The promotion has a quantity condition that division alone does not remove.
What is the saving on the pair against two regular-price bottles? | $1 | $2 | $2.50 | $3 | Two regular-price bottles cost six dollars, so the five-dollar pair saves one.
How much more does the pair cost than buying one bottle? | $2 | $1 | Nothing | $2.50 | The five-dollar total exceeds the three-dollar single purchase by two dollars.
Which response respects the final choice? | One bottle at $3; I will keep that quantity. | I added another bottle because the average is lower. | You must buy two now that I explained the offer. | One bottle is $5 because you declined the pair. | The shopper explicitly selects one, and its stated single price remains three dollars.''',
    dialogue='''Nia | The shelf says two for five dollars, so I expected this one bottle to be two fifty. Why is the single price showing three dollars?
Ben | The offer has a [[quantity condition::Quantity condition requires two qualifying bottles for the five-dollar offer, while one bottle remains at the stated single price.]]. Five dollars applies when you buy two qualifying bottles; one bottle on its own remains three dollars.
Nia | I divided five by two. The arithmetic seemed straightforward, so I thought that was what each bottle would cost even if I only took one.
Ben | That gives the [[average price::Average price is five dollars divided by two within the qualifying pair; it is not a separate one-bottle selling price.]] within the pair. It is two fifty per bottle when the purchase meets the two-bottle condition.
Nia | So the calculation is right, but I used it for a different purchase quantity than the offer actually describes.
Ben | Exactly. The [[single-item price::Single-item price is three dollars for one bottle alone, distinct from the lower average within the two-bottle offer.]] is still three dollars. The pair costs five dollars in total, rather than changing every individual purchase to two fifty.
Nia | Are both bottles supposed to be part of that particular offer? I should not assume another product can make up the pair.
Ben | Correct. They must be [[qualifying items::Qualifying items meet the stated promotion terms; an unrelated product cannot be assumed to count toward the required pair.]]. We would check the actual products against the shelf offer rather than assume any second item qualifies.
Nia | I only need one today. Before I decide, how much does the offer save compared with buying two at the usual price?
Ben | The [[comparison basis::Comparison basis is two bottles at the regular three-dollar price, giving six dollars against which the five-dollar offer saves one.]] is two bottles at three dollars each, which would be six dollars. The five-dollar pair saves one dollar against that total.
Nia | That is different from saying I spend less than I would on the single bottle I already have in my basket.
Ben | Yes. The pair requires two dollars of [[extra spending::Extra spending compares the five-dollar pair with the three-dollar single purchase, showing a two-dollar increase in total outlay.]] compared with your one-bottle purchase. A lower average price does not mean a lower total than buying only one.
Nia | Thank you. I would rather keep the extra two dollars today because I do not need the second bottle.
Ben | That is a clear [[purchase preference::Purchase preference is the shopper's choice based on actual need and total spending, which should not be overridden by the lower bundle average.]]. The single-bottle option remains available at three dollars; there is no need to change your quantity to justify that choice.
Nia | Please keep it to one, then. I mainly wanted to understand the shelf wording, not have another bottle automatically added.
Ben | I will give a [[quantity read-back::Quantity read-back confirms one bottle, preventing the explanation of the pair offer from being mistaken for permission to add another.]]: one bottle only. Explaining the offer does not mean you have accepted the two-bottle purchase.
Nia | Is there a membership condition I have missed as well, or is the issue here simply that I have one bottle instead of two?
Ben | No membership condition is stated in this offer. This [[price query::Price query concerns the difference between the quantity offer and the single-item price, not an invented loyalty requirement.]] is about the required quantity and the difference between an average and a single price.
Nia | That answers it. One at three dollars is what I want, and I understand why dividing the pair price does not change that amount.
Ben | Your [[basket total::Basket total is three dollars for the chosen single bottle under the fictional no-other-charges case, not the five-dollar pair price.]] for this choice is three dollars. The selected quantity stays one, and no second bottle has been added.''',
    transfer_title='Explain a different quantity offer',
    transfer_setup='One qualifying soup can is $4. The offer is three qualifying cans for $10, with no other charges. The shopper selects one can. Three at regular prices would cost $12.',
    transfer='''Associate: "The offer requires ___ qualifying cans." | three | Three is the stated quantity required for the ten-dollar promotion.
Shopper: "My one-can choice costs ___ dollars." | four | The single-can price remains four dollars despite the bundle offer.
Associate: "The bundle saves ___ dollars against three regular-price cans." | two | Twelve dollars minus the ten-dollar bundle total gives a two-dollar saving.
Shopper: "My selected quantity remains ___." | one | The shopper chooses one rather than accepting the larger bundle.'''
))


BOOK['units'].append(unit(
    title='Checking the basket and payment status',
    scene='One mug, two recorded entries',
    skill='Correct a duplicate before payment and distinguish the revised basket total from a refund or completed transaction.',
    brief='Shopper Leo has one mug priced at $8, but cashier Amira has scanned it twice. The checkout record shows two mugs and $16. No other charges apply in the exercise, and payment has not begun. Amira acknowledges the duplicate, corrects the recorded quantity through the store checkout process, and reads back one mug at $8. Leo confirms the correction. No money has been taken, no refund is required for this unstarted payment, and the exchange ends before payment completion.',
    cast='Leo | Shopper\nAmira | Cashier',
    culture=('Make the correction visible in the explanation', 'A shopper should not need to infer that a total changed correctly. Acknowledge the exact error, explain the corrected quantity, and read back the revised total before payment. Avoid calling an unpaid-basket correction a refund, which can make the transaction sound further along than it is.'),
    a='''What is the actual quantity? | One mug | Two mugs | Eight mugs | Sixteen mugs | The shopper has one mug even though two entries were recorded.
What is the corrected total? | $8 | $16 | $24 | $0 | One mug at eight dollars gives eight dollars with no additional charges.
What is the payment status? | Payment has not begun | Payment has been refunded | Payment was declined | Payment is completed | The brief explicitly places the correction before any payment begins.''',
    vocabulary='''checkout | Place or process for recording and paying for purchases. | check the checkout total
point-of-sale system | System recording sales and payments, often abbreviated POS. | use the point-of-sale system
scan | Read an item code into the checkout record. | scan the item
duplicate scan | Recording the same intended item twice by mistake. | correct a duplicate scan
line item | Individual product entry in a transaction record. | review the line item
recorded quantity | Number of units entered in the system. | correct the recorded quantity
physical quantity | Actual number of items the shopper has. | verify the physical quantity
basket correction | Amendment to the selected goods before completion. | make a basket correction
void entry | Cancel an incorrect recorded item under the store process. | void the duplicate entry
quantity adjustment | Change to the number of units recorded. | confirm the quantity adjustment
revised total | Updated amount after a correction. | read back the revised total
amount due | Sum still to be paid. | confirm the amount due
payment status | Stage of the payment, such as unstarted or completed. | check the payment status
tender | Money or payment method offered to pay. | confirm the tender amount
cash payment | Payment made using notes or coins. | process a cash payment
card terminal | Device used for supported card-payment interactions. | identify the card terminal
contactless payment | Payment interaction using supported contactless technology. | distinguish a contactless payment
authorization | Payment-system approval stage, not equivalent to every later settlement step. | check authorization status
declined payment | Payment attempt not approved through the relevant system. | explain a declined payment
receipt | Record of a transaction or completed purchase details. | check the receipt
refund | Return of money already paid. | distinguish a refund from a correction
change | Cash returned when the tendered amount exceeds the amount due. | confirm the change
customer display | Screen showing transaction information to the shopper. | check the customer display
transaction completion | Finalizing the sale through the actual store process. | confirm transaction completion''',
    precision='The original record incorrectly shows two $8 mugs, totaling $16. The corrected record shows one $8 mug. This is a quantity correction before payment, not a refund of money already taken.',
    precision_extra='A displayed total, a started payment, an authorization, and a completed transaction are different states. In this case payment has not begun, so do not invent a decline, reversal, or refund. Follow the actual checkout process for the correction.',
    phrases='''Acknowledge the duplicate | You are right; the mug has been recorded twice.\nState the actual quantity | You have one mug, not two.\nPause before payment | Let us correct the basket before payment begins.\nExplain the record | The current entry shows two at $8, totaling $16.\nName the correction | I will correct the recorded quantity through our checkout process.\nConfirm the revised quantity | The record now shows one mug.\nRead back the amount | The corrected total is $8.\nKeep status clear | Payment has not begun.\nAvoid refund language | No money has been taken, so this is not a refund.\nInvite a check | Please check that the display shows one mug at $8.\nDistinguish the price | The price per mug stays $8; the quantity was wrong.\nAvoid a false discount | This is a correction, not a special discount.\nConfirm the remaining step | Payment is still the next step.\nKeep the explanation short | The duplicate is removed; one mug remains.\nAvoid an invented decline | There has been no payment attempt to decline.\nClose the correction | We have confirmed the corrected basket before proceeding.''',
    notes='''Twice versus two | Scanning the same intended item twice does not mean the shopper has two items.\nQuantity versus price | The unit price is unchanged; the recorded number of mugs is corrected.\nDue versus paid | Eight dollars due is not eight dollars already paid.\nCorrection versus refund | An unstarted payment has no paid amount to return in this scenario.\nNow shows | This describes the updated record, not merely a promise to change it later.\nBefore proceeding | The shopper can verify the correction before the payment step begins.''',
    d='''Which explanation is accurate? | One mug was recorded twice; the corrected total is $8 before payment. | The price of each mug has been reduced to $4. | A $16 payment has already been refunded. | The shopper has two mugs but pays for one. | The correction removes an erroneous quantity while preserving the eight-dollar price.
Which term should not describe this correction? | Refund | Quantity adjustment | Revised total | Duplicate scan correction | Refund means returning paid money, but payment has not begun here.
What should the customer display show after correction? | One mug at $8 | Two mugs at $8 each | A completed payment receipt | A declined-payment message | The revised basket contains one eight-dollar mug before payment begins.
Which statement preserves the final stage? | The basket is corrected; payment is still next. | The sale is already paid and complete. | The bank rejected the payment. | Change has already been returned. | No payment attempt or completion occurs during this correction exchange.''',
    dialogue='''Leo | Could you check the screen before I pay? It shows two mugs, but I only have one here on the counter.
Amira | You are right. There is a [[duplicate scan::Duplicate scan means the same intended mug has been entered twice, not that the shopper selected two physical mugs.]]. The mug has been recorded twice, and we should correct that before starting payment.
Leo | I thought it might have scanned while you were moving it, but I mainly want to make sure the quantity matches what I am buying.
Amira | The [[physical quantity::Physical quantity is one mug, which the checkout record must match rather than leaving the two-entry mistake in place.]] is one mug. The recorded quantity is two, so the issue is the number entered rather than the price of the mug.
Leo | The shelf price was eight dollars. That part still looks right, but the total is sixteen because the entry appears twice.
Amira | Exactly. The [[line item::Line item is the transaction entry showing the mug and its quantity; the duplicate produces the incorrect sixteen-dollar total.]] needs correction. Two at eight dollars gives sixteen, while your one mug should total eight dollars here.
Leo | Please correct it before I use the payment terminal. I have not started paying yet, and I would prefer to check the amount first.
Amira | The [[payment status::Payment status is unstarted, so the cashier must not describe this as a completed charge, decline, or refund.]] is still unstarted. I will make the quantity correction through our checkout process before we move to the payment step.
Leo | Does that mean you are changing the price, or just removing the extra recorded mug? I want to understand what will remain on the screen.
Amira | It is a [[quantity adjustment::Quantity adjustment changes the recorded number from two mugs to one while leaving the eight-dollar item price unchanged.]]. The price per mug stays eight dollars; we are removing the extra recorded unit rather than applying a discount.
Leo | All right. I can see the quantity has changed to one now. Could you confirm the total as well so I know the correction is complete?
Amira | The [[revised total::Revised total is eight dollars after the duplicate quantity is corrected, with no additional charges in the supplied case.]] is eight dollars for one mug. There are no other charges on this purchase, and the basket now matches the item on the counter.
Leo | Thank you. Someone once called a correction like this a refund, which made me wonder whether I had already been charged without realizing it.
Amira | This is not a [[refund::Refund would return money already paid; no money has been taken because the payment has not begun.]]. No money has been taken here, so we are correcting the unpaid basket rather than returning a payment.
Leo | That is clear. The difference matters, because I have not presented payment and would not expect a completed transaction yet.
Amira | Correct. The [[amount due::Amount due is the eight dollars still to be paid, distinct from money already received or returned.]] is eight dollars. It is still to be paid, and I will not describe the sale as paid or completed.
Leo | The screen is showing one mug and eight dollars, which is what I expected. I am satisfied that the basket itself is right now.
Amira | Thank you for checking the [[customer display::Customer display lets Leo verify the corrected quantity and total before the next payment step.]]. Reading back both the quantity and the amount helps confirm that the record and your purchase agree.
Leo | We can move to payment next, then. I appreciate you explaining the correction instead of just changing the number without saying what happened.
Amira | We have confirmed one mug at eight dollars. [[Transaction completion::Transaction completion has not yet occurred; the corrected basket is ready for the separate payment and completion steps.]] is still ahead of us, after the payment step, so the correction has not been confused with a refund or an already finished sale.''',
    transfer_title='Correct a different duplicate scan',
    transfer_setup='One bowl costs $12, but two were recorded for $24. The shopper has one bowl. Payment has not begun and no other charges apply. The quantity is corrected to one.',
    transfer='''Cashier: "The actual quantity is ___ bowl." | one | Only one physical bowl is being purchased in this scenario.
Shopper: "The corrected total is ___ dollars." | twelve | One bowl at twelve dollars gives the revised twelve-dollar total.
Cashier: "Payment has not ___." | begun | The correction occurs before any payment attempt starts.
Shopper: "This is a correction, not a ___." | refund | No money has been paid, so there is no paid amount to return.'''
))


BOOK['units'].append(unit(
    title='Discussing returns and exchanges at the counter',
    scene='Eligible does not mean in stock',
    skill='Apply supplied exchange conditions while separating eligibility from replacement availability and completed processing.',
    brief='Shopper Morgan wants a larger size of a shirt bought ten days ago. The shirt is unused, its tags remain attached, and Morgan has the receipt. In this fictional store, those conditions permit an exchange within thirty days. Associate Ellis confirms that the supplied conditions are met, then explains that stock of the larger size has not been checked. Morgan wants the same shirt in the larger size, not a different color or an automatic refund. The exchange remains unfinished pending the stock check and actual store process.',
    cast='Morgan | Shopper\nEllis | Customer-service associate',
    culture=('Explain the policy without making it universal', 'A clear answer can confirm what the supplied store policy allows while admitting that the desired replacement has not yet been located. Do not use eligibility as a promise of immediate stock, and do not substitute a refund or another variation for the shopper\'s stated request.'),
    a='''Which supplied policy conditions are met? | Unused shirt, attached tags, receipt, and purchase within thirty days | Used shirt without proof of purchase | Purchase outside the stated window | Only the request for a larger size | The brief confirms all four conditions of this fictional exchange policy.
What does Morgan want? | The same shirt in a larger size | An automatic refund | A different color without discussion | A second identical size | The requested remedy is a larger-size exchange for the same shirt.
What remains unknown? | Larger-size availability | Whether a receipt is present | Whether ten days is within thirty | Whether the shirt is unused | The replacement stock has not been checked despite the policy conditions being met.''',
    vocabulary='''return | Bringing an item back for a requested resolution. | discuss a return
exchange | Replacing a purchased item with another agreed item. | request an exchange
refund | Return of money already paid. | distinguish an exchange from a refund
store credit | Value issued for use with the retailer under stated terms. | clarify store-credit terms
proof of purchase | Record supporting where and when the item was bought. | check proof of purchase
receipt | Transaction record supplied as purchase evidence. | review the receipt
purchase date | Date on which the original sale occurred. | confirm the purchase date
exchange window | Time period during which the stated exchange policy applies. | check the exchange window
eligibility | Whether the stated conditions for a process are met. | confirm exchange eligibility
unused condition | Item state in which it has not been used. | confirm unused condition
attached tags | Original tags still connected to the item. | check attached tags
original packaging | Packaging supplied with the original product. | identify original packaging
replacement size | Different size requested in the exchange. | check the replacement size
same-style exchange | Exchange retaining the same product style while changing a variation. | request a same-style exchange
price difference | Difference between original and replacement prices, if established. | clarify any price difference
policy condition | Requirement stated in the relevant store policy. | explain a policy condition
exception request | Request for a departure from a stated policy, requiring the relevant authority. | refer an exception request
manager review | Review by a person with the relevant decision authority. | arrange manager review
statutory rights | Rights established by applicable law, distinct from a fictional store policy. | distinguish statutory rights
replacement stock | Inventory of the desired alternative item. | check replacement stock
availability check | Verification that the exact replacement can be supplied. | complete the availability check
exchange processing | Store steps needed to carry out an agreed exchange. | complete exchange processing
requested remedy | Outcome the shopper asks the store to provide. | confirm the requested remedy
pending exchange | Exchange not yet completed. | record the pending exchange''',
    precision='Ten days is within the fictional thirty-day exchange window, and the unused condition, attached tags, and receipt are present. Eligibility is established on these supplied facts, but availability of the larger size is still unknown.',
    precision_extra='An exchange, refund, and store credit are different outcomes. The shopper requests the same shirt in a larger size. Do not promise an unverified replacement, invent a price difference, or present the fictional policy as a statement of universal consumer rights.',
    phrases='''Clarify the requested outcome | Would you like the same shirt in a larger size?\nCheck the date | The receipt shows the purchase was ten days ago.\nState the local window | This store's stated exchange window is thirty days.\nConfirm the condition | The shirt is unused and the tags are attached.\nIdentify the evidence | You have the receipt as proof of purchase.\nConfirm eligibility | The supplied conditions for this exchange are met.\nSeparate stock from policy | I still need to check the larger size.\nAvoid a readiness promise | Eligibility does not mean the replacement is already available.\nKeep the variation exact | Same shirt and color, larger size.\nAvoid changing the remedy | I will not turn your exchange request into a refund without discussion.\nKeep alternatives optional | We can discuss alternatives only if you want to.\nAvoid invented charges | No price difference has been established here.\nName the pending step | The replacement-stock check is still outstanding.\nKeep the status accurate | The exchange has not been completed yet.\nLimit the policy claim | I am explaining this store's stated policy for this case.\nClose with the next action | I will check the exact larger-size replacement next.''',
    notes='''Within | Ten days falls inside the stated thirty-day window.\nEligible versus available | Policy conditions can be met while replacement stock remains unknown.\nSame versus similar | The same shirt is more specific than an unrequested similar product.\nExchange versus refund | Replacing an item and returning money are different remedies.\nPresent versus processed | Having a receipt does not mean an exchange has already been completed.\nLocal policy | The exercise policy is a supplied condition, not a replacement for applicable rights.''',
    d='''Which explanation is accurate? | You meet the stated exchange conditions; I still need to check the larger size. | Meeting the policy guarantees the replacement is here. | Ten days is outside thirty days. | A receipt automatically completes the exchange. | Eligibility is supported while replacement availability and processing remain unfinished.
Which outcome has the shopper requested? | Same-shirt exchange to a larger size | Immediate store credit instead | Refund without further discussion | Different material selected by staff | Morgan wants a particular replacement rather than any available remedy.
Which claim is unsupported? | Every store must use this exact thirty-day policy. | The receipt is present. | The tags remain attached. | The larger size is unchecked. | The stated policy is fictional and does not establish universal legal requirements.
What should be checked next? | Stock of the exact larger-size replacement | Whether ten is greater than thirty | An unrelated color chosen without asking | A refund already described as complete | Replacement availability is the unresolved practical step after the supplied conditions are confirmed.''',
    dialogue='''Morgan | I bought this shirt ten days ago, and I would like a larger size. It has not been used, and I have kept the tags attached.
Ellis | I can help check the [[exchange::Exchange is the requested replacement of the purchased shirt with a larger size, not an automatic refund or store credit.]] request. Do you want the same shirt and color, with only the size changed?
Morgan | Yes, exactly the same shirt. I do not want another color substituted just because it might be easier to find.
Ellis | I will keep the [[replacement size::Replacement size is the specific larger variation Morgan requests, while the shirt style and color remain unchanged.]] separate from the other details. The request is the same shirt and color in the larger size.
Morgan | Here is the receipt. I was not sure whether ten days was still inside the period for an exchange at this store.
Ellis | Our stated [[exchange window::Exchange window is thirty days in this fictional store, and the ten-day-old purchase falls within it.]] is thirty days for an unused shirt with attached tags and a receipt. Ten days falls within that period.
Morgan | The shirt is unused, and the tags are still on it. Is there another condition in the policy you have just described that I am missing?
Ellis | On these facts, the [[eligibility::Eligibility means the stated unused-condition, tags, receipt, and time-window requirements are met, not that replacement stock is confirmed.]] conditions are met. That answers the policy question, but I still need to check the larger-size stock.
Morgan | So I qualify for the exchange, but you are not yet saying that the replacement is definitely here today.
Ellis | Correct. [[Replacement stock::Replacement stock is the inventory of the exact larger-size shirt, which has not yet been checked.]] has not been checked. I do not want the policy confirmation to sound like a promise that we have located your size.
Morgan | Thank you. I would prefer that distinction now rather than expect to walk out with it before anyone has looked.
Ellis | The [[availability check::Availability check is the next verification of the exact requested variation, separate from confirming the exchange policy conditions.]] is the next step. We will use the same shirt and color in the larger size, rather than check only for something similar.
Morgan | If it is not available, I would want to hear the options before making another choice. Please do not automatically refund it.
Ellis | I will preserve your [[requested remedy::Requested remedy is the larger-size exchange; an unavailable replacement would require another discussion rather than automatic substitution of a refund.]]. You have asked for an exchange, and any different outcome should be discussed with you instead of assumed.
Morgan | Good. I have had refund and exchange used as though they meant the same thing, which can be confusing at the counter.
Ellis | A [[refund::Refund returns money already paid, whereas Morgan's exchange request seeks a replacement item.]] returns money, while an exchange replaces the item with an agreed alternative. They are different outcomes, even when both begin with bringing an item back.
Morgan | That makes sense. Does having the receipt here mean the exchange itself is already processed, or is it simply the evidence for the original purchase?
Ellis | It is [[proof of purchase::Proof of purchase supports the original transaction and date; presenting it does not itself complete an exchange.]]. The receipt supports the original transaction and date, but the replacement and exchange processing are not complete.
Morgan | Then please check the larger size next. The same shirt is still my first choice, and I understand we do not have a stock answer yet.
Ellis | I will do that. The status is a [[pending exchange::Pending exchange means the conditions are met but the stock check and actual exchange steps remain unfinished.]]: the stated conditions are met, the requested replacement is clear, and stock and processing remain to be confirmed.''',
    transfer_title='Separate another eligibility and stock question',
    transfer_setup='A fictional store permits unused, tagged shirts to be exchanged with a receipt within twenty-one days. A shopper bought a shirt seven days ago, meets those conditions, and requests the same shirt in small. Replacement stock is unchecked.',
    transfer='''Associate: "Seven days is ___ the stated window." | within | Seven days falls inside the twenty-one-day period supplied for this store.
Shopper: "The replacement size requested is ___." | small | Small is the specific variation requested in this new case.
Associate: "Replacement stock remains ___." | unchecked | Meeting exchange conditions does not establish the replacement's availability.
Shopper: "The requested remedy is an ___." | exchange | The shopper seeks a replacement shirt rather than an automatic refund.'''
))


BOOK['units'].append(unit(
    title='Explaining local stock and collection status',
    scene='An order message is not a pickup notice',
    skill='Distinguish order acknowledgment from collection readiness and give a reliable update commitment without promising an outcome.',
    brief='Shopper Ravi shows collection-desk associate Jules a message acknowledging order R61. It is not a ready-for-collection notification. One item is still being located, and the complete order is not confirmed ready. Collection colleague Noor will update Ravi at 3:00 even if the issue is unresolved. No substitute size, color, or product has been agreed. Jules must keep the order reference, current status, next contact owner, and update time clear without turning 3:00 into a collection promise.',
    cast='Ravi | Shopper\nJules | Collection-desk associate',
    culture=('An update is still useful when the outcome is uncertain', 'A shopper may read a positive-sounding automated message as permission to travel to the store. Explain what the message actually confirms, acknowledge the inconvenience, and state who will update them and when. Do not make the uncertainty disappear by offering a guessed ready time.'),
    a='''What does the message confirm? | Acknowledgment of order R61 | The complete order is ready to collect | A substitute has been accepted | Collection has already occurred | The supplied message acknowledges the order but is not a collection-ready notice.
What remains unfinished? | One item is still being located | Every item has been collected | The shopper has accepted another color | A refund is already processed | The order is not confirmed ready because one item is still being located.
What is promised for 3:00? | An update from Noor, even if unresolved | Guaranteed collection readiness | Automatic replacement with another size | A completed refund | The commitment concerns communication at three, not a guaranteed stock outcome.''',
    vocabulary='''order acknowledgment | Message confirming that an order has been received or recorded. | read the order acknowledgment
order reference | Identifier used to locate the specific order. | confirm the order reference
collection notice | Message stating that the order can be collected under the stated process. | distinguish a collection notice
pickup | Common US term for collecting an order. | explain pickup status
ready for collection | Status indicating the relevant preparation and checks are complete. | confirm ready-for-collection status
order line | Individual item entry within an order. | check the outstanding order line
item location | Place where a requested unit is being found or verified. | confirm the item location
picking | Selecting the ordered goods from stock under the store process. | check picking status
packing | Preparing selected goods for handover or dispatch. | distinguish packing from picking
fulfillment | Process of preparing and supplying the order. | explain fulfillment status
partial order | Order for which only some items are available or prepared. | describe a partial order
complete order | All items included in the order together. | verify the complete order
collection desk | Store point handling order pickup. | contact the collection desk
collection colleague | Staff member responsible for the relevant pickup update. | name the collection colleague
status update | Communication about the latest verified position. | give a status update
update deadline | Time by which an update will be provided. | confirm the update deadline
readiness estimate | Provisional expectation of when collection may be possible. | distinguish a readiness estimate
readiness promise | Commitment that the order will be available by a stated time. | avoid an unsupported readiness promise
unresolved item | Item whose location or status remains unsettled. | track the unresolved item
variation match | Confirmation that size, color, and other details match the order. | check the variation match
substitution consent | Shopper agreement to a different item or variation. | obtain substitution consent
contact owner | Person responsible for the next communication. | identify the contact owner
collection record | Record of order preparation and handover status. | update the collection record
handover completion | Actual transfer of the order to the shopper. | confirm handover completion''',
    precision='Order R61 is acknowledged but not confirmed ready. One item is still being located. Noor will update the shopper at 3:00 even if unresolved; that is an update commitment, not a promise that collection will be possible then.',
    precision_extra='A different size, color, or product is not automatically an acceptable way to complete the order. No substitution is agreed. Keep preparation, readiness, and actual handover distinct so a message does not imply a stage that has not occurred.',
    phrases='''Identify the order | Let us check order R61.\nExplain the message | This is an order acknowledgment, not a collection notice.\nState the current position | One item is still being located.\nAvoid a readiness claim | The complete order is not confirmed ready yet.\nAcknowledge the inconvenience | I understand why you expected the message to mean you could collect it.\nName the update owner | Noor is the collection colleague handling the next update.\nGive the contact time | Noor will update you at 3:00.\nKeep the commitment precise | The update will happen even if the issue is still unresolved.\nSeparate time and outcome | Three o'clock is the update time, not a guaranteed collection time.\nPreserve the ordered variation | We will keep the requested size and color in the check.\nAvoid an unrequested substitute | No alternative item has been agreed.\nAsk before a change | Any proposed substitution needs your agreement.\nDo not invent a cause | I do not have a confirmed reason the item has not been located.\nRead back the next step | Noor will provide the next status update at 3:00.\nKeep handover status accurate | The order has not been collected.\nClose with the known facts | Acknowledged order, one unresolved item, next update at three.''',
    notes='''Acknowledged versus ready | Recording an order does not establish that every item is prepared for collection.\nAt three versus by three | Here at three identifies the promised contact time, not an order-completion deadline.\nEven if | This keeps the communication commitment valid when the outcome remains uncertain.\nComplete order | Readiness of some items does not establish readiness of the whole order.\nSubstitute | A different variation requires discussion instead of silent acceptance on the shopper's behalf.\nLocated versus handed over | Finding an item is a different stage from transferring the order to the shopper.''',
    d='''Which explanation is accurate? | The message acknowledges R61; one item is still being located. | Every acknowledged order is ready. | The shopper accepted a substitute by showing the message. | The order has already been collected. | The message and current location work do not establish complete readiness.
What does even if unresolved add? | The update still occurs without a final stock answer. | The order must be ready by then. | A substitute will be selected automatically. | The shopper loses the right to ask questions. | The phrase preserves the communication commitment despite an uncertain outcome.
Which statement wrongly turns an update into a promise? | Your complete order will definitely be ready at 3:00. | Noor will update you at 3:00. | One item is still being located. | No substitute has been agreed. | Readiness at three is not supported by the promised status update.
What needs separate agreement? | A proposed different size, color, or product | Reading the order reference aloud in the conversation | Stating that readiness is unconfirmed | Naming the update time | The shopper has not authorized any substitution for the ordered variation.''',
    dialogue='''Ravi | I received this message about order R61, so I came to collect it. It says you have my order, but the desk cannot find everything yet.
Jules | Let me clarify the [[order acknowledgment::Order acknowledgment records receipt of R61, but it does not state that the complete order is ready for collection.]]. This message confirms the order was received; it is not the notice saying the complete order is ready to collect.
Ravi | I see the difference now, although the wording sounded positive enough that I thought I could come in. What is the current position?
Jules | One [[order line::Order line identifies the individual item still being located, explaining why complete-order readiness has not been confirmed.]] is still being located. I cannot confirm the complete order is ready while that item remains unresolved.
Ravi | Does that mean you know it is sold out, or simply that someone has not located the correct item yet?
Jules | The confirmed fact is the unfinished [[item location::Item location remains unresolved; that does not by itself establish sold-out status or a particular cause.]] check. I should not turn that into a sold-out claim or invent a reason that has not been verified.
Ravi | Thank you. Can someone tell me when I will hear more? I do not want to keep coming back to the desk for the same answer.
Jules | Noor is the [[contact owner::Contact owner identifies Noor as responsible for the next communication, giving the shopper a specific person rather than an anonymous promise.]] for the next update. Noor will update you at three o'clock, including if the item is still unresolved.
Ravi | So I will hear from Noor at three even if there is not a final answer. That would at least let me plan what to do next.
Jules | Yes. The [[status update::Status update communicates the latest verified position at three, even if the order cannot yet be confirmed ready.]] is the commitment. You should not have to infer from silence whether the check is still continuing.
Ravi | I want to be careful about the time. Are you promising the order will be ready at three, or only that I will get an update then?
Jules | Three is the [[update deadline::Update deadline concerns the promised communication, not a guaranteed completion or collection time for the order.]], not a guaranteed collection time. We have not established when the complete order will be ready.
Ravi | Understood. Please do not replace the missing item with another size or color just to make the order look complete.
Jules | No [[substitution consent::Substitution consent has not been given, so a different size, color, or product cannot be assumed acceptable.]] has been given. Any proposed alternative needs a separate discussion with you rather than being treated as an automatic solution.
Ravi | The exact version matters because the item is a gift. I would rather receive a clear update than collect the wrong variation.
Jules | We will keep the [[variation match::Variation match means checking the ordered size, color, and product rather than using a similar-looking alternative to close the order.]] in the check. Finding something similar is not the same as confirming the item you ordered.
Ravi | Could you repeat the reference and the next step? I want to make sure this update is attached to my order, not another one.
Jules | The [[order reference::Order reference is R61, connecting the unresolved item and Noor's three-o'clock update to this specific shopper's order.]] is R61. One item is still being located, and Noor will update you at three even if that remains unresolved.
Ravi | That is clear. I have not collected the order, and I should wait for an actual collection notification rather than rely on the acknowledgment.
Jules | Correct. [[Handover completion::Handover completion has not occurred; the shopper has an acknowledged order and a promised update, not a completed collection.]] has not happened. The current record should preserve the unconfirmed readiness and the next update, without describing the order as already collected.''',
    transfer_title='Keep another update commitment precise',
    transfer_setup='Order P74 is acknowledged but not ready for collection because one item is still being located. Jo will update the shopper at 4:30 even if unresolved. No substitution is agreed.',
    transfer='''Associate: "The order reference is ___." | P74 | P74 connects the message and unresolved item to the correct order.
Shopper: "The next update is at ___." | 4:30 | Four thirty is the promised communication time, not a readiness guarantee.
Associate: "The update owner is ___." | Jo | Jo is explicitly responsible for the next status communication.
Shopper: "No substitution has been ___." | agreed | An unresolved item does not authorize a different variation without agreement.'''
))


BOOK['units'].append(unit(
    title='Managing queues and offering practical assistance',
    scene='A checkout route that works',
    skill='Ask what assistance is preferred, offer an available checkout route, and respect individual choices and position in line.',
    brief='Shopper Sam uses a mobility aid and says the current checkout is too narrow. Associate Lina knows that accessible checkout lane four is open, reached by the clear main aisle to the left. Sam prefers spoken directions, keeps personal belongings and the mobility aid under their own control, and accepts the move to lane four. Lina will ask colleague Noor to preserve the current place in line during the move; that request is not yet confirmed. No diagnosis, physical assistance, or handling of belongings is requested.',
    cast='Sam | Shopper\nLina | Retail associate',
    culture=('Ask rather than take over', 'Address the shopper directly and ask what help would be useful. A mobility aid is not an invitation to touch it or a reason to make assumptions about the person. Give practical information and respect the requested form of assistance without demanding a personal explanation.'),
    a='''What problem does Sam identify? | The current checkout is too narrow | The shopper forgot a payment card | The store is closed | Every checkout is inaccessible | Sam identifies the width of the current checkout, not a store-wide finding.
Which available route is offered? | Main aisle to the left toward open lane four | A closed lane with no clear route | Moving the mobility aid without asking | An unverified staff-only shortcut | The brief supplies an open accessible checkout and a clear main-aisle route.
What help does Sam prefer? | Spoken directions, with belongings and aid left under personal control | Unrequested physical guidance | Staff taking the mobility aid | A medical assessment | The shopper chooses directions and does not authorize handling personal belongings or the aid.''',
    vocabulary='''queue | Line of shoppers waiting for service. | manage the queue
place in line | Shopper's position in the service order. | preserve a place in line
checkout lane | Specific path and counter used for payment. | identify the checkout lane
accessible checkout | Checkout identified as accessible in the supplied store scenario. | offer the accessible checkout
main aisle | Principal route through the selling area. | describe the main aisle
clear route | Route free of the stated obstruction in the scenario. | identify a clear route
narrow passage | Space the shopper reports as too restricted for access. | acknowledge a narrow passage
mobility aid | Device a person uses to support movement. | respect the mobility aid
walker | Walking aid providing support through a frame. | identify a walker when relevant
wheelchair | Mobility device used for seated movement. | respect wheelchair users' choices
personal belongings | Items owned or carried by the shopper. | ask before handling belongings
preferred assistance | Help the shopper says would be useful. | ask about preferred assistance
spoken directions | Verbal explanation of where to go. | offer spoken directions
physical guidance | Hands-on assistance, not authorized by a general offer to help. | ask before physical guidance
permission | Agreement to a specific action. | obtain permission before handling items
independent movement | Shopper moving under their own control. | respect independent movement
direct address | Speaking to the shopper rather than only a companion. | use direct address
companion | Person accompanying the shopper, not automatically their spokesperson. | avoid addressing only the companion
route confirmation | Check that the proposed path is understood and suitable for the request. | give a route confirmation
colleague coordination | Communication to arrange the next service step with another worker. | coordinate with a colleague
open lane | Checkout currently available for use. | identify the open lane
queue transfer | Move between lines while managing the service order. | arrange a queue transfer
assistance boundary | Limit on what help the shopper has authorized. | respect the assistance boundary
pending request | Asked-for action not yet confirmed or completed. | distinguish a pending request''',
    precision='Lane four is open and reached by the supplied main-aisle route. Sam chooses spoken directions and retains control of belongings and the mobility aid. Lina will ask Noor to preserve the place in line, but that coordination is not yet confirmed.',
    precision_extra='Do not turn a helpful offer into unrequested touching or a medical inquiry. Ask about the practical assistance needed for this route. The fictional description identifies an available checkout; it does not certify real-world accessibility or replace applicable requirements.',
    phrases='''Acknowledge the barrier | I understand that this checkout is too narrow for you.\nAsk about preferred help | What help would you prefer?\nOffer the available lane | The accessible checkout at lane four is open.\nDescribe the route | The clear main aisle to the left leads to lane four.\nCheck the preference | Would spoken directions be helpful?\nRespect belongings | I will not handle your belongings without your permission.\nRespect the mobility aid | I will leave your mobility aid under your control.\nAvoid a personal inquiry | We can focus on the checkout route and the help you want.\nAddress the shopper | Let me check the next step with you directly.\nPreserve service order | I will ask Noor to preserve your place during the move.\nKeep coordination accurate | That request still needs confirmation.\nAvoid an unverified promise | I have not yet confirmed the queue arrangement with Noor.\nConfirm the accepted help | You prefer directions, without physical assistance.\nInvite a route question | Is there any part of the route you would like clarified?\nKeep the choice with the shopper | Please tell me if you prefer a different form of help.\nClose the arrangement | Lane four is available; I will coordinate the place-in-line request.''',
    notes='''Would you like | Offers a choice without assuming that assistance is needed or wanted.\nDirectly | Speaking to the shopper preserves agency even when a companion is present.\nPermission scope | Accepting directions does not authorize touching a bag or mobility aid.\nToo narrow | This reports the shopper's practical barrier without requiring a diagnosis.\nWill ask versus confirmed | A promised coordination step is not proof that the colleague has accepted it.\nPreserve versus restart | Preserving the place means addressing continuity rather than automatically sending the shopper to the back.''',
    d='''Which opening respects the shopper's choice? | What help would you prefer with the route to lane four? | I will move your aid now. | Tell me your diagnosis before I help. | Your companion should decide for you. | The question asks about practical preferences without assuming permission or demanding personal medical details.
Which action is authorized? | Giving spoken directions | Taking the mobility aid without asking | Carrying the bag despite refusal | Providing hands-on guidance automatically | Sam accepts directions and retains control of belongings and the mobility aid.
Which statement accurately describes the queue arrangement? | Lina will ask Noor to preserve the place; confirmation is pending. | Noor has already confirmed the move. | Sam must automatically restart at the back. | The request is completed because Lina thought of it. | The brief distinguishes the planned colleague request from an accepted arrangement.
Which route information is supplied? | Clear main aisle to the left, toward open lane four | An unverified back-room shortcut | A closed lane at the far exit | A measured legal clearance for every passage | The scenario provides a specific usable route, not a certification or invented shortcut.''',
    dialogue='''Sam | This checkout is too narrow for me to get through comfortably with my mobility aid. Is there another lane I can use?
Lina | Yes. The [[accessible checkout::Accessible checkout is the available lane four identified in this scenario, offering a practical alternative to the reported narrow lane.]] at lane four is open. Before I offer help, what would you prefer?
Sam | Directions would be enough. I can move myself, and I would like to keep my bag and mobility aid with me.
Lina | I will give [[spoken directions::Spoken directions are the form of assistance Sam chooses, without authorizing physical guidance or handling personal items.]] and leave your belongings and aid under your control. I will not assume you want me to carry or move anything.
Sam | Thank you. Where is lane four from here? I cannot see the lane number clearly past the people standing in this line.
Lina | The [[main aisle::Main aisle is the clear route to the left supplied in the scenario, leading toward open lane four.]] to your left leads toward lane four. That is the clear route available, rather than trying to continue through this narrow checkout.
Sam | That sounds workable. I am also concerned about losing my place, because I have already been waiting here for some time.
Lina | I will ask Noor to preserve your [[place in line::Place in line is Sam's existing service position, which Lina will ask the colleague to preserve during the move.]] during the move. I do not want to treat the change of lane as a reason to ignore the time you have already waited.
Sam | Has Noor agreed to that already, or is it something you still need to arrange? I would like to know the current position.
Lina | The [[colleague coordination::Colleague coordination is still pending; Lina has proposed asking Noor but has not received confirmation.]] still needs confirmation. I will ask Noor, but I should not tell you the arrangement has already been accepted.
Sam | I appreciate that distinction. Please ask, and keep the directions as the help I have chosen. I do not need someone to move the aid.
Lina | Understood. Your [[assistance boundary::Assistance boundary limits help to the requested directions and coordination, excluding unrequested handling of the mobility aid or belongings.]] is clear. Directions are welcome; touching the mobility aid or taking your bag has not been authorized.
Sam | Exactly. Sometimes people begin helping before asking, and then I have to stop them while also trying to navigate the space.
Lina | I will seek [[permission::Permission must apply to a specific proposed action; a general offer of help does not authorize touching or carrying.]] before any different kind of help. Your answer about directions should not be treated as agreement to every possible action.
Sam | Good. I am happy to move to lane four using the route you described once the place-in-line request has been checked.
Lina | Let me give a [[route confirmation::Route confirmation repeats the left-hand main aisle and lane-four destination so the shopper can verify the proposed path.]]: use the clear main aisle to the left, toward the open lane four. I will also follow up with Noor about the queue.
Sam | That is clear. There is no need to ask my companion to decide; I can explain what assistance works for me.
Lina | Of course. I will use [[direct address::Direct address means speaking to Sam about Sam's preferences, rather than treating a companion as the automatic decision-maker.]] and keep discussing the arrangement with you. The practical route and your preference are what we need to clarify.
Sam | Thank you. Directions, no handling of my belongings or aid, and a request to preserve my place are the help I am asking for.
Lina | That is accurate. The [[pending request::Pending request is Noor's place-in-line coordination, which remains to be confirmed rather than reported as already complete.]] is the queue arrangement with Noor. Lane four is open, your preferred assistance is clear, and I will not describe the coordination as complete until it is confirmed.''',
    transfer_title='Offer another agreed form of help',
    transfer_setup='A shopper says lane two is too narrow. Open lane six is reached through the clear aisle to the right. The shopper wants spoken directions only. A request to preserve the place in line is awaiting a colleague response.',
    transfer='''Associate: "The open alternative is lane ___." | six | Lane six is the available checkout stated in this new scenario.
Shopper: "The clear aisle is to the ___." | right | Right identifies the supplied direction to the alternative lane.
Associate: "The preferred help is spoken ___." | directions | The shopper requests verbal route information rather than physical assistance.
Shopper: "The place-in-line request is still ___." | pending | The colleague has not yet responded, so the arrangement is unconfirmed.'''
))


BOOK['units'].append(unit(
    title='Handing over a till and an unfinished query',
    scene='Five dollars below the expected count',
    skill='Report an unverified cash difference neutrally and transfer ownership of two unfinished checks without inventing a cause.',
    brief='At shift change, cashier Tessa reports an expected drawer balance of $180 and a recorded count of $175. A second check has not occurred, so the recorded difference is $5 below expected with no cause established. A separate price query for item P32 is also open. Incoming supervisor Arun accepts responsibility for both the second balance check and the P32 price query. Neither task is completed during the handover. Tessa must not accuse a colleague, describe a proven loss, or imply that Arun accepting the checks resolves them.',
    cast='Tessa | Outgoing cashier\nArun | Incoming supervisor',
    culture=('Neutral detail is stronger than suspicion', 'A precise handover names the expected figure, the recorded count, the unchecked difference, and the person taking the next action. It should not speculate about a colleague or combine unrelated open matters into an invented explanation. Separate ownership from completion.'),
    a='''What is the recorded difference? | $5 below expected | $5 above expected | $175 below expected | No difference | The recorded count of $175 is five dollars below the expected $180.
What verification is pending? | A second balance check | A completed investigation | A confirmed theft finding | An approved correction to P32 | The brief states that the second check has not yet occurred.
What does Arun accept? | Both unfinished checks, not their completed outcomes | A proven-loss finding | Only a resolved price query | Responsibility for an admitted cause | Arun takes the next actions without confirming a cause or completing either task.''',
    vocabulary='''till | Register or cash-handling point used for sales. | hand over the till
cash drawer | Compartment holding cash at the checkout. | check the cash drawer
expected balance | Amount the relevant record indicates should be present. | state the expected balance
recorded count | Amount entered after the initial cash count. | report the recorded count
cash difference | Difference between expected and recorded amounts before cause is established. | report the cash difference
variance | Difference between a reference figure and an actual or recorded figure. | quantify the variance
overage | Amount recorded above the expected balance. | distinguish an overage
shortfall | Amount recorded below a specified expected balance. | describe a recorded shortfall
recount | Another count to verify the initial result. | request a recount
second check | Independent or repeated verification under the store process. | complete the second check
reconciliation | Comparison of related records and amounts to explain differences. | begin reconciliation
opening float | Cash amount assigned at the start for normal checkout operations. | verify the opening float
cash drop | Recorded movement of cash out of a till under store procedures. | check the cash-drop record
cash movement | Transfer of cash that should be reflected in relevant records. | review cash movements
denomination | Face-value category of notes or coins. | check the denomination totals
count sheet | Record used to document counted amounts. | review the count sheet
transaction log | Record of sales and related checkout actions. | consult the transaction log
unverified discrepancy | Difference not yet confirmed or explained through the required checks. | record an unverified discrepancy
established cause | Explanation supported by completed verification. | distinguish an established cause
proven loss | Confirmed loss, not established by the initial difference alone. | avoid claiming a proven loss
open price query | Unresolved question about an item's price. | hand over the open price query
incoming supervisor | Supervisor taking over responsibility for the next shift. | brief the incoming supervisor
action owner | Person assigned the next check or follow-up. | name the action owner
handover status | Current state of each item at transfer. | confirm the handover status''',
    precision='The arithmetic is $180 expected minus $175 recorded, giving $5 below expected. The second check is pending and the cause is unknown. This is a recorded discrepancy, not proof of theft, a specific error, or a confirmed loss.',
    precision_extra='The P32 price query is a separate unfinished item. No evidence links it to the drawer difference. Arun accepts both follow-ups, but acceptance does not complete the recount or resolve the price question. Record both statuses explicitly.',
    phrases='''State the expected figure | The expected drawer balance is $180.\nState the recorded figure | The recorded count is $175.\nQuantify the difference | That is $5 below expected.\nMark the verification stage | The second check has not occurred yet.\nAvoid a cause claim | The cause is not established.\nKeep the language neutral | I am reporting a discrepancy, not accusing anyone.\nAvoid a proven-loss statement | The initial difference does not establish a confirmed loss.\nSeparate the other item | There is also an open price query for P32.\nAvoid an invented link | I have no verified connection between the two issues.\nAssign both checks | Can you take the balance check and the P32 follow-up?\nConfirm ownership | I accept responsibility for both follow-ups.\nKeep completion separate | Neither check is completed by this handover.\nAsk for a read-back | Please repeat the figures and the two pending actions.\nPreserve the initial record | Keep the recorded count distinct from any later verified result.\nName the current status | Recount pending; price query open; cause unknown.\nClose the handover | The next owner is clear, while both outcomes remain unresolved.''',
    notes='''Below versus above | The direction of the difference matters as much as the five-dollar amount.\nRecorded versus verified | A written initial count can still await the required second check.\nUnknown versus suspicious | Unknown cause is a factual limit, not evidence against a person.\nAlso | This introduces a separate item without claiming it caused the first issue.\nAccept versus complete | Taking responsibility for a task does not mean it has been performed.\nInitial versus final | Preserve the original count while documenting any later checked result accurately.''',
    d='''Which handover is accurate? | Expected $180, recorded $175, second check pending, cause unknown. | Five dollars has definitely been stolen. | The drawer is five dollars over. | The second check proved the initial count correct. | The correct statement includes both figures, the verification stage, and the limit on causal claims.
What is known about P32? | Its price query is still open. | It caused the drawer difference. | It has been resolved and closed. | The shopper admitted a pricing error. | The price query remains unfinished, with no established connection to the balance difference.
Which statement wrongly treats ownership as completion? | Arun accepted both checks, so both issues are resolved. | Arun is the next action owner. | The second check remains pending. | No cause is established. | Accepting follow-up responsibility does not perform the checks or supply their outcomes.
Which calculation matches the facts? | $180 minus $175 equals $5 below expected. | $175 minus $180 means $5 above expected. | $180 plus $175 equals the loss. | The $175 count is itself the discrepancy. | The expected balance exceeds the recorded count by five dollars, with verification still pending.''',
    dialogue='''Tessa | Before I finish, I need to hand over the drawer figures and one unfinished price question. Neither issue has had its follow-up check yet.
Arun | Start with the [[expected balance::Expected balance is the reference amount of 180 dollars, which must be distinguished from the recorded physical count.]]. I want the reference figure and the actual recorded count separately before we describe the difference.
Tessa | The expected balance is one hundred eighty dollars. The count entered on the sheet is one hundred seventy-five dollars, and it has not been checked again.
Arun | Then the [[recorded count::Recorded count is the initial 175-dollar figure, still awaiting a second check rather than a final verified outcome.]] is one hundred seventy-five. We should preserve that as the initial entry while the required second check remains outstanding.
Tessa | That makes it five dollars below expected. I do not know whether another check or a record review will explain the difference.
Arun | We can report the [[variance::Variance is the five-dollar difference between expected and recorded amounts; it does not establish the cause.]] as five dollars below expected, with no established cause. The arithmetic is clear even though the explanation is not.
Tessa | I have not accused anyone or described it as stolen. I only want the next person to know exactly what needs verification.
Arun | That is appropriate. This is an [[unverified discrepancy::Unverified discrepancy identifies the initial difference while acknowledging that the second check and causal review have not occurred.]], not a finding about a person. We should not turn an incomplete check into an allegation.
Tessa | The other matter is the price query for item P32. That question is still open, and I have no evidence connecting it to the drawer figures.
Arun | I will keep the [[open price query::Open price query is the separate unresolved P32 issue; no evidence links it to the drawer discrepancy.]] separate. An unfinished question about P32 does not automatically explain the cash difference just because both appear in the handover.
Tessa | Can you take responsibility for the second balance check and the price follow-up? I do not want either item to be left without an owner.
Arun | Yes. I will be the [[action owner::Action owner is Arun, who accepts both next checks without claiming either is already completed.]] for both. I accept the second balance check and the P32 follow-up, while keeping their outcomes unresolved for now.
Tessa | Thank you. Please make sure the record still says the second check has not occurred. Your accepting it should not make that status disappear.
Arun | The [[second check::Second check is the pending verification of the drawer count, not an action completed merely by accepting responsibility.]] remains pending. The handover assigns the work; it does not count as performing it or confirming the first result.
Tessa | Exactly. I also want to avoid writing loss confirmed when all we currently have is the initial difference between those two figures.
Arun | A [[proven loss::Proven loss would require a supported finding beyond the initial recorded difference; the current handover does not establish it.]] has not been established. The accurate statement is a recorded five-dollar difference with verification pending and the cause unknown.
Tessa | Could you read back both tasks and the figures before I leave? That will help us catch a reversed number or a missing follow-up.
Arun | Expected one hundred eighty, recorded one hundred seventy-five, five below expected. The [[handover status::Handover status preserves the pending recount, open P32 query, unknown cause, and Arun's accepted ownership without claiming resolution.]] is second check pending and P32 price query open, with me responsible for both follow-ups.
Tessa | That is correct. There is no established cause and no confirmed connection between the price question and the drawer difference.
Arun | I will keep the [[reconciliation::Reconciliation compares relevant amounts and records to explain a difference; it is subsequent work, not a conclusion already reached in this handover.]] work separate from assumptions. Both actions have an owner now, but neither outcome is complete or proved by this conversation.''',
    transfer_title='Report a different recorded difference',
    transfer_setup='Expected drawer balance is $240 and the recorded count is $245. A second check is pending and the cause is unknown. Price query Q18 is open. Supervisor Jo accepts both follow-ups.',
    transfer='''Cashier: "The recorded count is five dollars ___ expected." | above | Two hundred forty-five exceeds the expected two hundred forty by five dollars.
Supervisor: "The second check is ___." | pending | The check has not occurred merely because follow-up responsibility is accepted.
Cashier: "The open price query is ___." | Q18 | Q18 identifies the separate unresolved price matter in this handover.
Supervisor: "The cause remains ___." | unknown | The initial arithmetic does not establish why the difference exists.'''
))
