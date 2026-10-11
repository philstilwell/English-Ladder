"""Original availability, service-charge, and accessible-ordering conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The last salmon is spoken for",
        skill="Reconcile remaining portions, communicate an unavailable item, and obtain an actual replacement choice.",
        setup="Fictional dinner service: four salmon portions remain, with three already committed to accepted tickets. Table 18 requests two more. The kitchen allocates the last available portion to one named guest after confirmation; the other chooses mushroom pasta at $21 instead of salmon at $26. There is no reported allergy.",
        cast="Nina|Server\nOmar|Expeditor",
        dialogue="""Nina|Table eighteen wants two salmon. The board says four left, but I can see three salmon on accepted tickets. Is that four before those orders or four still available?
Omar|Four is the physical count, including the three [[committed portions::Three of the four physical portions already belong to accepted tickets, leaving only one for a new order.]]. We have one available for a new order, not four.
Nina|Then I cannot promise both guests salmon. Please hold the table's new request while I explain the shortage and ask who would like the remaining portion.
Omar|Agreed. Once we allocate that last one, salmon goes on the [[86 list::The 86 list identifies items unavailable for further orders; it does not cancel portions already committed to accepted tickets.]]. The existing three tickets still get theirs.
Nina|For the guests, I will say we have one salmon portion left. I will not tell them we have eighty-six salmon or use the shorthand without explaining.
Omar|Good. Tell them what is available and let them choose. Mushroom pasta is available at twenty-one dollars; salmon is twenty-six.
Nina|I have checked with table eighteen. Seat one wants the last salmon. Seat two has chosen the pasta after hearing both prices.
Omar|I have allocated the last salmon to seat one. Record the [[substitution::The substitution replaces seat two's requested salmon with the pasta that the guest actually selected.]] against seat two only, with the guest's confirmed choice.
Nina|That makes forty-seven dollars for those two mains, before any other bill items or applicable charges. It was fifty-two for two salmon.
Omar|Yes, a five-dollar [[price difference::Two salmon would total $52; one $26 salmon plus $21 pasta totals $47, a $5 difference for these mains.]] for these mains. It is not a separate discount on top of the pasta's twenty-one-dollar price.
Nina|I will enter the pasta at its own price, not leave a salmon charge and hope someone remembers to change it later.
Omar|Please read the updated ticket back to me before we proceed. I need the table, seats, dishes, and the fact that only seat two changed.
Nina|Table eighteen: seat one salmon, twenty-six; seat two mushroom pasta, twenty-one. The pasta is the [[replacement choice::Seat two explicitly chose mushroom pasta after the shortage and price were explained; it is not a kitchen-selected substitute.]] the guest has agreed to.
Omar|Confirmed. I have the last salmon allocated. We now have zero available for additional orders, although four portions still physically await preparation.
Nina|I will tell the section team and ask the authorized person to update the ordering system. Should we also check the online menu?
Omar|Yes, verify each relevant ordering channel. Do not assume a handwritten board or one screen changes every listing, especially where items have separate records.
Nina|I will confirm the [[availability update::The availability update must communicate that no further salmon orders can be accepted; existing committed orders remain distinct.]] reached the floor and ordering channels. I will not remove salmon from the tickets already accepted.
Omar|Exactly. If another guest asks, offer the current alternatives and their prices. Do not promise a portion that belongs to one of these tickets.
Nina|Then the final read-back is three earlier salmon, one salmon for table eighteen seat one, and pasta for seat two. No salmon remains to sell.
Omar|That matches. Send the corrected table order through our process, and keep the stock message separate from the guest's individual change.""",
        transfer_title="Count what can still be sold",
        transfer_setup="Six sea-bass portions physically remain; four are committed to accepted tickets. Three new guests request sea bass. Two choose the available portions at $28 each; the third agrees to $24 chicken. Other bill items and charges are outside this comparison.",
        transfer="""Server: There are ___ portions available before the new choices.|two|Six physical portions minus four already committed leaves two available to allocate.
Expeditor: The third guest has agreed to ___ .|chicken|The replacement is explicitly chosen chicken, not a substitute selected without permission.
Server: These three mains total ___ dollars.|80|Two sea-bass mains at $28 plus chicken at $24 equals $80.
Expeditor: After allocation, sea bass is ___ for further orders.|unavailable|All six physical portions are now committed; physical presence does not mean they remain available to sell.""",
        reference=("Toast: menu-item inventory and 86 status", "https://doc.toasttab.com/doc/platformguide/adminMenuItemInventoryOverview.html"),
    ),
    scenario(
        title="Service charge or optional tip?",
        skill="Explain an itemized charge and optional payment choice without making unsupported claims about tax or staff distribution.",
        setup="Fictional US check: food and drinks subtotal $150; disclosed mandatory service charge 18% of that subtotal, $27; separately listed tax $12. Total before any voluntary extra tip is $189. The terminal offers an optional tip. No staff-distribution policy or general tax-rate rule is supplied.",
        cast="Dev|Guest reviewing the check\nAlma|Server",
        dialogue="""Dev|Could you explain these two lines? There is already a service charge on the bill, but the terminal is asking about a tip as well.
Alma|Of course. The [[service charge::The $27 service charge is mandatory under this fictional restaurant's disclosed terms, unlike an additional voluntary tip.]] is the eighteen-percent charge shown in our terms. The extra tip on the terminal is optional.
Dev|Eighteen percent of which amount? I want to check the arithmetic because the tax is listed on a separate line.
Alma|The [[subtotal::The stated $150 food-and-drinks subtotal is the basis for this charge; the example does not apply eighteen percent to the final total.]] for food and drinks is one hundred fifty dollars. Eighteen percent of that is twenty-seven dollars.
Dev|And the twelve dollars below it is tax already included in the total shown? It is not another amount I need to add myself?
Alma|Correct. One hundred fifty plus twenty-seven plus twelve gives the [[amount due::The supplied amounts sum to $189 before a voluntary extra tip; the already listed tax and service charge must not be added again.]] of one hundred eighty-nine, before any extra tip you choose.
Dev|I was worried the screen would add eighteen percent again. Does leaving the tip at zero remove the existing service charge?
Alma|No. Zero on the optional-tip screen means no [[additional gratuity::An additional gratuity is a voluntary extra amount; selecting zero there does not remove the existing mandatory service charge.]]. The existing bill still totals one hundred eighty-nine.
Dev|I would like to pay that total without an extra tip today. I do not want to select a suggested percentage by mistake.
Alma|Certainly. Please use the no-extra-tip choice and check the amount displayed before confirming. I can explain the screen without selecting an amount for you.
Dev|Thank you. Does the service charge go directly to you, or is it shared among the team?
Alma|I would need our manager to explain the actual [[distribution policy::The case supplies no policy explaining how the service charge is distributed; Alma must not invent a staff share.]]. I should not promise where every dollar goes without checking.
Dev|Please do ask. I am not trying to argue with you; I just want to understand what I am paying and what the staff receive.
Alma|I understand. The bill calculation and the distribution question are separate. I can show the first now and get the manager's answer to the second.
Dev|Is this how every restaurant calculates tax on service charges? I have seen different layouts on other bills.
Alma|No general tax rule follows from this check. The twelve dollars is the [[listed tax::The case supplies a $12 tax line, not a universal rate or rule about which charges are taxable.]] in our example. Applicable tax treatment and other restaurants' terms need their own verification.
Dev|All right. The calculation here is clear: one hundred fifty for the order, twenty-seven service charge, twelve tax. I am choosing no extra tip.
Alma|Yes. Please check that the terminal shows one hundred eighty-nine for your selected payment. Agreeing the amount does not itself complete the transaction.
Dev|It shows the amount we discussed. I will confirm it myself, and I would like an itemized receipt afterward.
Alma|Certainly. I will provide the receipt through our payment process and follow up with the manager on your distribution question. I will not treat that question as already answered.""",
        transfer_title="Explain a different check",
        transfer_setup="A fictional check lists an $80 subtotal, a mandatory 15% service charge on that subtotal, and $6 listed tax. The guest chooses no additional tip. No staff-distribution percentage or universal tax rule is supplied.",
        transfer="""Guest: The service charge is ___ dollars.|12|Fifteen percent of the $80 subtotal is $12, not fifteen percent of the final total.
Server: The total before any extra tip is ___ dollars.|98|The $80 subtotal plus $12 service charge plus $6 listed tax equals $98.
Guest: My additional tip choice is ___ .|zero|The guest explicitly chooses no extra tip; that does not cancel the mandatory service charge.
Server: The staff-distribution policy remains ___ .|unspecified|The check's arithmetic gives no evidence of what proportion is paid to staff.""",
        reference=("IRS: voluntary tips and mandatory service charges", "https://www.irs.gov/businesses/small-businesses-self-employed/tip-recordkeeping-and-reporting"),
    ),
    scenario(
        title="Read the menu, keep the choice",
        skill="Offer useful menu access, communicate prices and ingredients precisely, and address the guest directly.",
        setup="Guest Rosa has low vision and asks server Theo to read the two vegetarian mains with prices. The current menu lists mushroom risotto $22 with Parmesan, and chickpea stew $20 with bread. Rosa chooses the stew and asks to keep the bread. No vegan request or allergy is reported.",
        cast="Rosa|Guest choosing a main\nTheo|Server",
        dialogue="""Rosa|Could you read the vegetarian mains to me, including the prices? I cannot read this print comfortably, and the menu on my phone is not opening.
Theo|Certainly. Would you like just that section first, or would another [[format::Format describes how the menu information is presented; Theo asks what works instead of assuming the phone or print is accessible.]] work better for you?
Rosa|Reading that section would be helpful. Please tell me what comes with each dish, not only the names.
Theo|There are two listed options. The mushroom risotto is twenty-two dollars and includes [[Parmesan::Parmesan is the explicitly listed risotto ingredient; omitting it would withhold relevant menu information from Rosa.]]. The chickpea stew is twenty dollars and comes with bread.
Rosa|Could you repeat the stew price? I heard the two dishes, but missed the second amount when someone passed behind me.
Theo|The [[chickpea stew::Chickpea stew is the second listed main, priced at $20 and served with bread.]] is twenty dollars, including bread. The risotto is twenty-two.
Rosa|Thank you. I will have the stew. Please keep the bread; I do not need anything taken off.
Theo|Stew with bread as listed. Is that the [[choice::Rosa explicitly selects the stew with its bread; Theo confirms the guest's own decision rather than choosing for her.]] you would like me to enter?
Rosa|Yes. My friend may order something different, so please keep our choices separate.
Theo|Of course. I will take each order directly. Would you like me to read the drinks section too?
Rosa|Not yet. I will stay with water for now. Thank you for asking rather than working through the whole menu while I am deciding.
Theo|You are welcome. I will [[read back::Read back means repeat the selected order aloud so Rosa can check it without depending on the printed menu.]] your order before sending it: chickpea stew with bread, twenty dollars; water for now.
Rosa|That is correct. Is the twenty dollars the price of the stew, or have you included anything else in that figure?
Theo|It is the menu price for the stew with bread. I have not represented it as the final bill total with every possible charge included.
Rosa|Good. When the check comes, could you read the items and total to me as well? I want to check it myself.
Theo|Certainly. We can review the [[itemized bill::An itemized bill separates the ordered items and listed charges; reading it lets Rosa review the bill herself.]] and total together using a method that works for you.
Rosa|One more thing: my companion does not need to answer for me. I may ask for help reading, but I can make my own order.
Theo|Understood. I will speak directly with you and ask what assistance is useful. I will not treat help with print as permission to make your choices.
Rosa|Thank you. Then I am ready to order the stew with bread. Please let me know if anything in that description has changed.
Theo|I will check any changed detail rather than silently substitute. Your selected order is clear, and I will follow our normal ordering process.""",
        transfer_title="Read the requested section accurately",
        transfer_setup="Guest Jo asks for the two desserts and prices to be read aloud. The menu lists apple crumble $8 with vanilla ice cream, and mango sorbet $7. Jo chooses the sorbet. No allergy or dietary restriction is reported.",
        transfer="""Server: The crumble costs ___ dollars.|8|Eight dollars is the stated crumble price, not the price of the sorbet.
Guest: The crumble comes with vanilla ___ .|ice cream|Vanilla ice cream is a listed accompaniment that should not be omitted from the spoken description.
Server: Your chosen dessert is mango ___ .|sorbet|Jo selects sorbet; assistance with reading does not transfer the choice to the server.
Guest: Its menu price is ___ dollars.|7|The sorbet's stated menu price is $7; the facts do not establish the final bill total.""",
        reference=("US Department of Justice: effective communication, including menu access", "https://www.ada.gov/topics/effective-communication/"),
    ),
]
