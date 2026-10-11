"""Original shelf-life, pallet-identity, and count-cutoff conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Oldest is not always first",
        skill="Apply a customer's remaining-shelf-life requirement before comparing eligible batches by expiry date.",
        setup="Fictional eight-case order delivers 12 November 2026 and requires 30 days remaining. Date difference means expiry minus delivery. Available batches: A, 12 cases, received 1 October, expires 30 November; B, 10 cases, received 5 October, expires 31 December; C, 6 cases, received 8 October, expires 15 December. All other eligibility checks pass.",
        cast="Elena|Picker\nDev|Inventory coordinator",
        dialogue="""Elena|Dev, I'm reviewing the eight-case order for November twelfth. Batch A arrived first and expires first. Shouldn't it be first in the proposed pick?
Dev|Check the customer's [[remaining shelf life::Eligibility depends on days left at delivery, not simply whether the batch arrived or expires first.]] requirement before ranking batches. This customer needs thirty days at delivery, calculated as expiry date minus delivery date.
Elena|November thirtieth minus November twelfth is eighteen days. So A is below thirty, even though it won't have expired on the delivery date.
Dev|Right. A is [[ineligible::A has eighteen days remaining, below this customer's thirty-day requirement, although it is not yet expired.]] for this order on that requirement. Don't call it expired or assume it needs writing off.
Elena|B expires December thirty-first, forty-nine days after delivery. C expires December fifteenth, thirty-three days after delivery. Both meet the minimum.
Dev|Then [[FEFO::First-expire, first-out ranks the eligible stock by expiry; C expires before B, even though B was received earlier.]], first-expire, first-out, puts C before B here. C expires sooner, despite having arrived three days after B.
Elena|So receipt order and expiry order aren't interchangeable. FIFO would compare when it came in; FEFO compares when it expires.
Dev|Exactly. Among these [[eligible batches::B and C both meet the customer minimum and all other stated checks; A fails the remaining-life requirement.]], C is first. B arriving earlier doesn't move it ahead of C in this expiry-based proposal.
Elena|C has six cases, but the order needs eight. We use all six from C in the proposed allocation, then need two more.
Dev|Those two come from [[batch B::After using six eligible cases from C, two from B complete the eight-case requirement.]]. Six plus two gives eight, with both batches meeting the thirty-day minimum.
Elena|And B would have eight cases remaining after that allocation. A stays at twelve because none of it is proposed for this order.
Dev|Correct. Keep the [[batch split::The proposed eight-case quantity consists of six C and two B; the batch identities must remain attached to the quantities.]] visible: six C, two B. Writing just eight cases would lose the traceability of the proposal.
Elena|Would you describe A as rejected stock on the handoff? I can see how someone might read ineligible that way.
Dev|No. Say it fails this customer's remaining-life requirement for this delivery date. That does not decide its status for another order or authorize disposal.
Elena|If the delivery date moves, we need to calculate again rather than copy today's eligibility result. Less time could remain.
Dev|Yes. And our case assumes every other eligibility check passes. In an actual order, holds, reservations, product requirements, and customer terms still matter.
Elena|Let me read it back: A eighteen days, B forty-nine, C thirty-three. A fails thirty; C expires before B among the eligible batches.
Dev|That's the comparison. We've separated receipt dates, expiry dates, and the customer minimum instead of calling all three the oldest stock.
Elena|The proposed quantity is six C plus two B. This is a planning read-back, not a claim that anything has been picked or dispatched.
Dev|Agreed. Retain the delivery date and batch quantities with that proposal, then use the actual approval and picking process for any work.""",
        transfer_title="Check a later delivery",
        transfer_setup="Six cases deliver 1 December 2026 with at least 21 days remaining. D expires 20 December and has 8 cases; E expires 10 January 2027 and has 5; F expires 28 December and has 4. All other checks pass. Use expiry minus delivery and earliest eligible expiry first.",
        transfer="""Picker: D has ___ days remaining, below the minimum.|nineteen|20 December minus 1 December is nineteen days, which fails the twenty-one-day requirement.
Coordinator: The first eligible batch by expiry is ___ .|F|F expires on 28 December, before eligible E on 10 January; D is ineligible.
Picker: Allocate ___ cases from F.|four|F has four eligible cases, leaving two of the six-case order still to cover.
Coordinator: Complete the order with ___ cases from E.|two|Six required minus four from F leaves two cases from E, which has forty days remaining.""",
        reference=("Microsoft Learn: shelf life and customer sellable-day requirements", "https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/shelf-life"),
    ),
    scenario(
        title="Two scans, one pallet identity",
        skill="Distinguish a logistic-unit identifier from a trade-item identifier and lot, then report duplicate scan events without inventing receipt status.",
        setup="Fictional receiving check: two physical pallets, P and Q, contain the same trade item and lot. Their complete SSCCs are confirmed distinct; staff say ending 0918 for P and ending 0925 for Q only as spoken shorthand. The scan-event log contains P twice and no Q. Neither receipt posting nor quantity acceptance is confirmed.",
        cast="Luis|Receiving clerk\nMei|Inventory clerk",
        dialogue="""Luis|Mei, I've got two pallets here, P and Q, and two events in the scanner log. At first glance that looks like a complete pair.
Mei|Look at the [[SSCC::The Serial Shipping Container Code identifies a logistic unit; two events with P's same SSCC do not identify two different pallets.]], the Serial Shipping Container Code, in each event. Both events identify P, ending zero nine one eight.
Luis|Then the event count is two, but the log only contains one distinct pallet identity. Q ending zero nine two five isn't represented.
Mei|Exactly. That's a [[duplicate scan::The same pallet identifier appears in both events, so the log repeats P rather than demonstrating a scan of Q.]] of P in the event log. It does not establish what the receipt system posted.
Luis|Both pallets contain the same product and lot. Could I use the product number to show that Q is the second pallet?
Mei|No. A [[GTIN::A Global Trade Item Number identifies the trade item, not a unique physical pallet instance containing that trade item.]], Global Trade Item Number, identifies the trade item. Matching product numbers don't make a missing pallet-identity event appear.
Luis|And the lot tells us which batch the goods came from. Two pallets can hold goods from that same batch.
Mei|Yes. The [[batch or lot::A batch or lot groups relevant product units; it does not uniquely distinguish P from Q when both contain the same lot.]] information matters for traceability, but it doesn't distinguish P from Q in this case.
Luis|On the GS1 reference sheet, I see parentheses around zero zero. Is that part of the eighteen-digit pallet identifier?
Mei|That's the [[Application Identifier::The Application Identifier is a prefix defining the following data; AI 00 is separate from the eighteen digits of the SSCC.]], often called AI. Zero zero says the following data is an SSCC; the SSCC itself has eighteen digits.
Luis|So AI zero zero means SSCC. AI zero one means GTIN, and AI ten means batch or lot. Different fields answer different questions.
Mei|Correct. And compare the [[complete identifier::The last four digits are only shorthand here; verification requires the complete identifier, whose distinctness is supplied in the case.]]. Those four-digit endings are only our spoken shorthand, not enough to validate a label or prove uniqueness.
Luis|The briefing confirms the complete P and Q identifiers are different. I'll preserve both full references in the actual record.
Mei|Good. Say two pallets physically present, P scanned twice, Q absent from this scan-event log. Don't reduce that to two pallets received.
Luis|Should I report a duplicated receipt? Two events might sound like we've added P twice to inventory.
Mei|Not yet. We haven't checked receipt posting. A system might reject or handle repeated scans differently; the event log alone doesn't settle that.
Luis|And Q missing from the log doesn't mean Q is physically missing. It's here; its event is what I haven't found.
Mei|Exactly. Physical presence, scan history, and posted inventory are three different checks. Keep each status attached to its own evidence.
Luis|I'll refer the duplicate event and the absent Q event for verification, with the two complete SSCCs and their product and lot information.
Mei|That gives us the right problem to review. Follow the actual receiving process; don't invent a replacement identifier or manually double the quantity.""",
        transfer_title="Count identities, not beeps",
        transfer_setup="Three physical pallets R, S, and T have different complete SSCCs but the same product and lot. The event log contains R, R, and S. Receipt posting is unchecked. Use the full identifiers for verification, not shortened verbal references.",
        transfer="""Clerk: The event log contains ___ distinct pallet identities.|two|R and S are two distinct identities; the repeated R event does not add a third.
Coordinator: The pallet absent from this event log is ___ .|T|T is physically present but has no event in the supplied log.
Clerk: The repeated pallet identity is ___ .|R|R appears twice in the event log, whereas S appears once.
Coordinator: Posted inventory remains ___ .|unchecked|The event log does not establish whether repeated scans created, changed, or were rejected from a receipt posting.""",
        reference=("GS1: logistic-unit identity, SSCC, and trade-item data", "https://www.gs1.org/standards/gs1-logistic-label-guideline/1-3"),
    ),
    scenario(
        title="Counted when, recorded when?",
        skill="Reconcile a physical count with a time-stamped balance using a verified movement, without double-posting an adjustment.",
        setup="Fictional item W6, location C14: the 09:00 inventory snapshot is 100 units. A verified outbound movement takes 6 units at 09:05 but posts at 09:20. The physical count at 09:15 is 94. No other movements or differences occur through 09:20. Priya and Sam review the completed timeline, not operating instructions.",
        cast="Priya|Inventory clerk\nSam|Inventory reviewer",
        dialogue="""Priya|Sam, the count sheet says ninety-four and the snapshot says one hundred. It looks six short, but the two records aren't from the same time.
Sam|Give me the [[cutoff time::The snapshot is a balance as of 09:00; it must not be compared as though it described the later 09:15 physical position.]] for each. The balance snapshot is nine o'clock, and the physical count is nine fifteen, correct?
Priya|Correct. Six units left C14 at nine oh five. We have the verified movement record, but it didn't post until nine twenty.
Sam|Then [[movement time::The goods physically left at 09:05, before the count; the later posting time does not delay that physical change.]] is nine oh five. That's before the count, even though it is before the system entry as well.
Priya|So the nine o'clock snapshot still describes one hundred at its own point in time. It isn't automatically a bad count just because the later figure differs.
Sam|Right. Roll that balance [[forward::To compare at 09:15, start from the 09:00 balance and subtract the six units that left before the count.]] to nine fifteen: one hundred minus six is ninety-four. That's the comparable expected physical quantity.
Priya|And ninety-four counted minus ninety-four expected gives zero. The apparent six-unit shortage came from comparing different times.
Sam|The reconciled [[variance::At the same 09:15 time basis, both the adjusted reference quantity and the physical count are ninety-four, leaving zero variance.]] is zero on these facts. Don't describe six as unexplained shrinkage when the verified movement accounts for it.
Priya|The physical movement was at nine oh five, the count at nine fifteen, and the entry at nine twenty. I should keep all three timestamps.
Sam|Yes. The [[posting time::09:20 is when the six-unit movement reaches the system; it is not the physical movement time or count time.]] belongs to the record update, not to when the goods left. Replacing one timestamp with another would distort the explanation.
Priya|By nine twenty the movement has posted. Since nothing else changed, the current balance should now be ninety-four too.
Sam|Exactly. A further minus-six [[inventory adjustment::The movement has already reduced the record to ninety-four; an extra minus-six adjustment would wrongly reduce it again to eighty-eight.]] would count the same reduction twice and take it to eighty-eight. The difference isn't a second loss.
Priya|Could we instead compare at nine o'clock by adding the six units back to the later physical count?
Sam|For the reconciliation calculation, yes: ninety-four plus six reconstructs one hundred at nine. Don't alter the actual ninety-four count entry to one hundred.
Priya|That distinction helps. A reconstructed comparison figure isn't a replacement for the observation made at nine fifteen.
Sam|Keep the original count, snapshot, movement evidence, and posting timestamp. They explain why the figures changed without overwriting the history.
Priya|Does an open cycle count always stop all stock movement? Someone might assume that nothing could have left between those two times.
Sam|Don't assume that. Site procedures and system settings differ. This case explicitly supplies a verified movement; real counting controls must be followed, not inferred from this example.
Priya|My handoff is W6 in C14, snapshot one hundred at nine, six out at nine oh five, count ninety-four at nine fifteen, posting at nine twenty.
Sam|And zero unexplained difference after reconciling to the same time. That explains this case; it isn't permission to move stock or post adjustments outside the actual process.""",
        transfer_title="Bring a receipt to the count time",
        transfer_setup="Item X7: 14:00 snapshot 80 units. A verified receipt physically adds 12 at 14:05 and posts at 14:30. The 14:20 physical count is 92. No other movements occur through 14:30. Review after posting.",
        transfer="""Clerk: The balance reconstructed for 14:20 is ___ units.|92|The earlier eighty plus the twelve physically received before counting gives ninety-two.
Reviewer: The unexplained count variance is ___ .|zero|Ninety-two counted matches the ninety-two expected on the same time basis.
Clerk: The receipt posting time is ___ .|14:30|The system posting occurs at 14:30, distinct from physical receipt at 14:05 and counting at 14:20.
Reviewer: Adding another twelve after posting would wrongly show ___ .|104|The posted balance is already ninety-two; another twelve would double-count the same receipt and show one hundred four.""",
        reference=("Microsoft Learn: cycle counts, movements, and difference review", "https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting"),
    ),
]
