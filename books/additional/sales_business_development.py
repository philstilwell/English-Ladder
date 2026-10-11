"""Original product-sales, tender, and distributor conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The agreement and the release",
        skill="Confirm quantities and delivery commitments without confusing an annual agreement with an immediate shipment.",
        setup="Fictional agreement: 1,200 valves over a year, ordered through releases. Release R31 requests 300 by 20 October. Operations can deliver 240 by that date and 60 by 27 October, subject to customer acceptance of the split. The customer needs all 300 by 24 October. No expedited alternative is confirmed. Agreement terms and dates are invented.",
        cast="Lena|Industrial account manager\nPavel|Customer buyer",
        dialogue="""Pavel|We have an annual agreement for twelve hundred valves. My team expects the three hundred on release R31 by October twentieth. Can you confirm that delivery?
Lena|I checked the [[release order::The release order specifies the 300 units requested now; the annual agreement's 1,200-unit commitment is not itself an instruction to ship all units immediately.]] with operations. They can deliver two hundred forty by the twentieth and the remaining sixty by the twenty-seventh, if you accept that split.
Pavel|That is not the date on our release. We need all three hundred for the work, and the latest usable arrival date is the twenty-fourth.
Lena|Then our proposed [[split delivery::A split delivery supplies one release in separate quantities and arrivals; here the proposed 240 and 60 add to 300, but the second arrival misses the customer's latest usable date.]] does not meet your full requirement. The first batch arrives in time, but the final sixty would be three days too late.
Pavel|I do not want the annual agreement used as evidence that stock was reserved for this exact date. What does the current promise actually cover?
Lena|The [[delivery commitment::The delivery commitment must identify the promised quantity and arrival date; the proposed dates have been checked with operations, but the customer has not accepted this revised split.]] needs quantities and dates against R31. I will not mark the whole release confirmed for the twentieth when operations has not offered that.
Pavel|Can another depot supply the sixty? We might accept a separate shipment if it reaches us by the twenty-fourth and the total is still three hundred.
Lena|I can request an [[expedite review::An expedite review checks whether a faster supply route is feasible, including stock, transport, cost, and authority; requesting it does not establish that the sixty units can arrive earlier.]]. We need actual availability, transit timing, and any extra charge before I offer that route as a solution.
Pavel|Please distinguish dispatch from arrival. A vehicle leaving on the twenty-fourth would not help if the valves arrive the following day.
Lena|Understood. Your [[required-on-site date::The required-on-site date is when the goods must arrive where needed, not when they leave the supplier; the customer's latest usable arrival is 24 October.]] is the twenty-fourth at the latest. I will give operations the delivery address and receiving constraints, not just a date without an event.
Pavel|Our receiving team can handle the first two hundred forty on the twentieth. That is useful, but I am not accepting a late balance by saying so.
Lena|I will record that distinction. Acceptance of one proposed batch does not silently approve the revised date for the balance or change your stated need.
Pavel|The first batch and the balance must use the same approved valve specification. Please do not substitute a similar part to fill the gap without asking.
Lena|Any [[substitution::A substitution would replace the specified item with another; a supply shortage does not authorize a different valve specification without the customer's required technical and commercial approval.]] needs the required approval. I will ask about the specified item first and keep any alternative clearly identified as a separate proposal.
Pavel|How will you update the paperwork if an earlier balance becomes possible? Our planning team will use the confirmation, not this call, to schedule the work.
Lena|The revised confirmation will identify R31, each quantity, its arrival date, and any approved cost change. It should also state which earlier confirmation it replaces.
Pavel|And the annual quantity should not become fifteen hundred because someone adds this release to the twelve-hundred agreement as though it were extra business.
Lena|Correct. These three hundred are ordered against that agreement, leaving nine hundred not yet released on the supplied facts. We must not count the same quantity twice.
Pavel|Please come back with the expedite result. Until then, our need remains three hundred by the twenty-fourth at the latest, with only the first batch workable as proposed.
Lena|I will report the confirmed options and remaining shortfall. I will not promise an earlier balance until the supply and delivery checks support it.""",
        transfer_title="Confirm another release and balance",
        transfer_setup="An annual 900-unit agreement has one 250-unit release. The supplier proposes arrival of 200 on 12 May and 50 on 19 May. The customer needs all units by 16 May. No expedited balance is confirmed.",
        transfer="""Seller: The quantity not yet released under the annual agreement is ___.|650|Nine hundred committed annually minus the single two-hundred-fifty release leaves six hundred fifty not yet released.
Buyer: The quantity arriving in time under the proposal is ___.|200|The first two hundred arrive on 12 May, before the latest required arrival on 16 May.
Seller: The late balance is ___ units.|50|The remaining fifty would arrive on 19 May, three days after the customer's latest usable arrival.
Buyer: A faster balance is still ___.|unconfirmed|The supplied facts contain no verified expedited option, so a request to check it is not a delivery promise.""",
        reference=("Microsoft Learn: sales agreements, commitments, and release orders; system-specific terminology", "https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-agreements"),
    ),
    scenario(
        title="Can we meet the tender requirement?",
        skill="Assess a mandatory tender condition, ask a precise clarification, and make a defensible bid decision.",
        setup="Fictional private tender: mandatory 24/7 staffed support from contract start; automated acknowledgments do not qualify. The seller currently offers weekday staffed support. An uncontracted partner is only a possibility. Questions are due 8 November at 12:00 UTC; bids, 15 November at 12:00 UTC. Alternatives require an express buyer amendment. No such amendment exists.",
        cast="Tomas|Sales lead\nZara|Bid manager",
        dialogue="""Tomas|This tender is a strong fit for the product. The one gap is overnight support. Could we mark that requirement compliant and arrange the partner after we win?
Zara|No. It is a [[mandatory requirement::The mandatory requirement is staffed support at every hour from contract start; the current weekday service and an uncontracted potential partner do not establish compliance.]], not a preference that extra product features can offset. We currently provide weekday staffed support, and the partner arrangement is not agreed.
Tomas|Our system sends automatic acknowledgments overnight. Could those count as support, with an agent picking up the request when the office opens?
Zara|The tender excludes that interpretation. Put the actual position in the [[compliance matrix::The compliance matrix maps each requirement to the proposed response and supporting evidence; it must show this gap rather than convert an automated acknowledgment into staffed service.]]. Acknowledgment is not the staffed service the buyer specified.
Tomas|Then we need to know whether a contracted partner could meet the condition. I do not want to ask for a waiver if the intended delivery model is acceptable.
Zara|Submit a [[clarification question::A clarification question seeks the buyer's interpretation through the specified process; it does not itself change a requirement or authorize a different service model.]] about permitted subcontracted coverage and the evidence required. Keep the question precise enough for the buyer to answer.
Tomas|The bid is due November fifteenth. Can the question wait until we finish the rest of the response next week?
Zara|No. The [[clarification deadline::The clarification deadline is 8 November at 12:00 UTC, one week before the bid deadline; the later submission deadline does not extend the question window.]] is November eighth at twelve UTC. We must work to that separate cutoff, not assume the bid deadline also applies to questions.
Tomas|Suppose the buyer accepts subcontracted coverage. We would still need the partner's actual commitment, prices, staffing, and responsibilities before claiming we meet it.
Zara|Exactly. A permitted model is not a completed arrangement. We need evidence of deliverability from contract start, including ownership of customer incidents and the proposed handoff.
Tomas|Could we include a cheaper weekday-only alternative alongside the base response? It might appeal to someone evaluating total cost.
Zara|Not under the current instructions. An [[amendment::An amendment is an authorized change to the tender requirements or instructions; this tender permits alternatives only through an express buyer amendment, and none exists.]] would need to permit that route. We cannot treat our proposed exception as permission to submit a nonconforming alternative.
Tomas|I will keep the opportunity active while we ask the question and assess the partner. That is different from authorizing the full bid effort today.
Zara|Yes. At the [[bid/no-bid review::The bid/no-bid review decides whether to pursue the tender based on requirements, capability, evidence, cost, and risk; an attractive product fit alone does not resolve a mandatory service gap.]], show what is known, the unresolved condition, and the time needed to resolve it. We need a decision based on deliverability.
Tomas|If the answer arrives verbally through our account contact, should we immediately change the response to compliant?
Zara|Use the tender's authorized clarification route and retain the formal response. Do not rely on an informal reassurance to override written instructions or skip the partner evidence.
Tomas|I will draft the question around subcontracted staffed coverage, not claim we already have it. Operations will assess the service model while commercial checks the cost.
Zara|And I will track the question deadline, buyer response, and any amendment against the matrix. Each entry needs an owner and evidence, not just a green status.
Tomas|If the gap cannot be resolved in time, we should decline rather than promise a service we cannot support. I can explain that commercially without blaming the buyer.
Zara|Agreed. A disciplined no-bid can protect the relationship. If we proceed, the submitted offer must describe a deliverable, compliant service, not an aspiration disguised as one.""",
        transfer_title="Keep the two tender deadlines separate",
        transfer_setup="A fictional tender requires staffed weekend support and excludes automated acknowledgments. Questions close 3 March at 10:00 UTC; bids close 10 March at 10:00 UTC. Weekend staffing is unconfirmed. No amendment permits a weekday-only alternative.",
        transfer="""Sales: Weekend coverage requires ___ support.|staffed|The tender expressly requires people providing support, not only an automated message.
Bid manager: The question deadline is ___ March.|3|Questions close on the third, not on the later bid-submission date.
Sales: The bid deadline is ___ March.|10|The tenth is the submission deadline and does not reopen the earlier question window.
Bid manager: The weekday-only alternative is not currently ___.|permitted|The instructions require an express amendment for an alternative, and none has been issued.""",
        reference=("US Federal Acquisition Regulation 15.203: proposal requirements and evaluation information; this case uses fictional private-tender terms", "https://www.acquisition.gov/far/15.203"),
    ),
    scenario(
        title="Stock is not new demand",
        skill="Reconcile channel shipments, end-customer sales, inventory cover, and a bounded stock-return request.",
        setup="Fictional four-week review: opening distributor stock 40 units, supplier deliveries 240, end-customer sales 160, no other movements. Sales averaged 40 units weekly. The return policy caps authorized returns at 10% of this period's deliveries and requires unopened eligible stock. Of 30 units requested for return, only 20 meet that condition. No return is authorized or completed yet.",
        cast="Grace|Supplier account manager\nYusuf|Distributor buyer",
        dialogue="""Grace|We shipped two hundred forty units this period. Before I ask you to take another batch, can we compare that with what actually moved to customers?
Yusuf|We sold one hundred sixty. Your [[sell-in::Sell-in measures supplier sales into the distribution channel, here the 240 units delivered during the period; it is different from the distributor's sales to end customers.]] was two hundred forty, but that was not our end-customer demand. We also had forty units in stock at the start.
Grace|Then total units available were two hundred eighty. With one hundred sixty sold and no other movements, you should have one hundred twenty left. Does that match the count?
Yusuf|It does. Our [[sell-through::Sell-through here refers to the 160 units sold onward to end customers; the explicitly defined period rate uses those sales divided by opening stock plus receipts.]] report records the customer sales separately. For this review, the period rate uses sales divided by opening stock plus receipts.
Grace|On that definition it is one hundred sixty over two hundred eighty, about fifty-seven point one percent. Using shipments alone as the denominator would give a different measure.
Yusuf|Correct. Keep the [[denominator::The denominator for the specified sell-through rate is 40 opening units plus 240 receipts, or 280; dividing by 240 receipts alone does not follow this review's definition.]] visible. Otherwise the same data might be reported as sixty-six point seven percent and look inconsistent even though nobody changed the sales count.
Grace|You sold forty units a week across these four weeks. At that unchanged rate, the one hundred twenty remaining units represent three weeks of stock.
Yusuf|That is the simple [[weeks of cover::Weeks of cover divides current stock by an assumed weekly sales rate, here 120 divided by 40 equals three; it is a planning indicator, not a guarantee about future demand.]] calculation. It is useful, but the next promotion could change demand. I would not call three weeks a guaranteed exhaustion date.
Grace|You also requested a return of thirty units. The policy caps returns at ten percent of the two hundred forty units delivered in this period, which is twenty-four.
Yusuf|The [[return eligibility::Return eligibility requires unopened qualifying stock as well as staying within the numerical cap; only 20 of the requested 30 units satisfy that condition in this case.]] check found only twenty qualifying unopened units. The other ten in the request do not meet the stated condition.
Grace|Then twenty is the most this request could qualify for, not twenty-four. The cap is a ceiling, not an entitlement that overrides the stock-condition rule.
Yusuf|Yes. And that is still a request. We have not received the [[return authorization::Return authorization is approval to proceed under the return process; eligibility arithmetic alone does not establish an approved return, completed movement, or issued credit.]], shipped anything back, or received a credit. Please keep those stages separate.
Grace|The stock reconciliation therefore remains one hundred twenty at this review. We should not subtract the twenty while the goods are still here and no return has occurred.
Yusuf|Agreed. The requested return can appear separately in the action list. If approved and completed, the inventory movement and credit will need their own records.
Grace|Would a larger promotional order help sell through the current stock? My first thought was to add another hundred units before the period closes.
Yusuf|Not without a demand plan. Adding supplier shipments does not make the existing goods sell faster, and it would increase our stock exposure before the promotion is tested.
Grace|Then let us review the product mix, customer inquiries, and promotion timing before proposing replenishment. I should not solve a supplier target by calling extra stock customer demand.
Yusuf|That would be more useful. The product mix matters because a total of one hundred twenty can hide fast-moving lines and slow-moving lines within it.
Grace|I will record two hundred forty sell-in, one hundred sixty sell-through, one hundred twenty closing stock, and a twenty-unit eligible return request pending authorization.
Yusuf|And keep the rate definition and three-week cover assumption beside them. That gives us a shared basis for the next order without confusing inventory, demand, and a possible return.""",
        transfer_title="Reconcile another channel period",
        transfer_setup="Opening stock is 30 units, deliveries 150, customer sales 120 over four weeks, and no other movements. The return cap is 10% of deliveries. A 20-unit return request contains only 12 eligible unopened units; none has returned yet.",
        transfer="""Buyer: Current closing stock is ___ units.|60|Thirty opening units plus one hundred fifty receipts minus one hundred twenty sales leaves sixty; the pending return is not yet a movement.
Seller: At thirty sales weekly, that is ___ weeks of cover.|two|Sixty units divided by the stipulated thirty-unit weekly rate gives two weeks, subject to unchanged demand.
Buyer: The numerical return cap is ___ units.|15|Ten percent of one hundred fifty delivered units equals fifteen.
Seller: This request has only ___ eligible units before authorization.|12|The twelve qualifying unopened units are below the fifteen-unit cap, so eligibility limits the request to twelve rather than fifteen or twenty.""",
        reference=("Salesforce Trailhead: channel strategy, partner responsibilities, and indirect sales", "https://trailhead.salesforce.com/content/learn/modules/channel-management-and-partner-portal-strategy/develop-your-channel-strategy"),
    ),
]
