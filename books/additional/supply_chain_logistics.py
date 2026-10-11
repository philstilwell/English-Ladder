"""Original receiving, returns, and damage-claim conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='Twelve cartons are posted as twelve individual items',
        skill='Reconcile receiving quantities across packaging levels and correct the transaction trail.',
        setup='A delivery contains twelve cartons of eight items each, all of one product. The warehouse system records twelve individual items. The shipment notice also lists 96 items. The receiving lead and inventory controller must check the physical count and receiving entry without inventing an additional shipment.',
        cast='Tessa|Receiving lead\nArun|Inventory controller',
        dialogue='''Tessa|The delivery is here, but the system shows only twelve items received. I counted twelve cartons, and each is labeled as containing eight.
Arun|Start with the [[unit of measure::The unit of measure identifies whether the recorded quantity means individual items, cartons, or another packaging level.]]. Was the receiving entry made in cartons or individual items?
Tessa|The field says each. The operator entered twelve after counting the cartons, so I think we have mixed the packaging levels.
Arun|Then verify the [[pack quantity::The pack quantity states how many individual items belong in each carton; the conversion must match the actual product and packaging.]] against this product and the delivery. A label is a useful lead, but let us confirm what arrived.
Tessa|All twelve cartons contain eight items. That is ninety-six individual items, and it matches the shipment notice.
Arun|Good. The [[conversion factor::The conversion factor is eight individual items per carton in this case, making twelve cartons equal to ninety-six items.]] is eight here. Do not use the supplier\'s other carton sizes as the basis.
Tessa|Should I add a second receipt for eighty-four items? That would bring the system total to ninety-six.
Arun|Follow the correction process for the original [[goods receipt::The goods receipt records this delivery event; its correction should not falsely create a separate physical shipment.]]. We need the right quantity without inventing a second delivery event.
Tessa|I will link the count sheet and the shipment notice. Do you also need the pallet label?
Arun|Yes, record the relevant [[SSCC::The Serial Shipping Container Code identifies the particular logistic unit, such as a pallet; it is not the product's item count.]], the Serial Shipping Container Code. That connects the logistic unit to its record; it is not a quantity.
Tessa|The pallet carries a different code from the product cartons. I will keep those identifiers in their proper fields.
Arun|Exactly. The product identifier and logistic-unit identifier answer different questions. We must not copy one over the other to make the screen look consistent.
Tessa|Purchasing has already received a shortage alert for eighty-four items. I will tell them we are reconciling the posting, not requesting another shipment.
Arun|Please do. After the authorized correction, verify the [[stock ledger::The stock ledger records inventory movements and balances; it must reconcile with the corrected receiving event and physical quantity.]] and the alert so the error does not trigger unnecessary replenishment.
Tessa|The receiving screen defaults to each. We should also check whether the item setup needs a clearer carton option.
Arun|Agreed, through the master-data process. We should not change a conversion used by other transactions without assessing its effect.
Tessa|For today, I will retain the original entry, the recount, and the correction reference. That gives the next shift a clear explanation.
Arun|And I will verify that the final balance increased by ninety-six items in total for this delivery, not twelve plus another ninety-six.
Tessa|That avoids turning a shortage into an overstatement. I will ask you to confirm the corrected balance before I close the discrepancy.
Arun|Yes. Then purchasing can close the false shortage without changing the supplier\'s actual delivery performance.''',
        transfer_title='A correction creates an extra receipt',
        transfer_setup='A delivery contains five cartons of ten items. Five individual items were posted, and a proposed additional posting of fifty would produce an incorrect total of 55.',
        transfer='''Receiver: The physical delivery contains fifty individual ___.|items|Five cartons multiplied by ten items gives fifty items, not fifty-five.
Controller: Correct the original receiving record through the approved ___.|process|The correction must preserve the transaction trail rather than invent another delivery.
Receiver: Verify the final balance against the physical ___.|count|The recorded total should reconcile to the actual fifty items received.
Controller: Keep the correction linked to the same delivery ___.|event|The discrepancy concerns one receiving event, not a second shipment.''',
        reference=('GS1: Serial Shipping Container Code', 'https://www.gs1.org/standards/id-keys/sscc')),
    scenario(
        title='A return authorization is not a restocking decision',
        skill='Coordinate a customer return while separating authorization, receipt, inspection, and credit.',
        setup='A business customer has approval to return six unused pumps under return authorization R218. Seven pumps arrive, including one with a different serial number and signs of use. The returns coordinator and customer-service lead must reconcile the shipment. No inspection outcome or credit has been approved.',
        cast='Beth|Returns coordinator\nJoel|Customer-service lead',
        dialogue='''Beth|R218 covers six pumps, but receiving found seven. One serial number is outside the approved list, and that unit shows signs of use.
Joel|I will check with the customer. The [[return authorization::The return authorization defines the approved return scope; it does not automatically cover an extra item or establish its condition.]] should remain linked to the six listed units, not silently expand to seven.
Beth|Thank you. We have recorded all seven physically received and kept them out of saleable stock pending review.
Joel|That is the right distinction. The [[receipt record::The receipt record documents what physically arrived, even when that quantity differs from the authorized or expected return.]] must show the actual arrival, even though it does not match the authorization.
Beth|The customer\'s note says unopened, but the seventh pump has marks on its housing. I have not tested it or identified the cause.
Joel|Describe the [[observed condition::Observed condition records what was actually seen, without turning appearance into an unsupported conclusion about use, cause, or performance.]] and attach the appropriate photographs. Please do not label it customer damage before the review.
Beth|Understood. Can I route the six matching serial numbers for inspection while you clarify the extra item?
Joel|Yes, under the returns procedure. Keep the discrepancy separately visible so it does not disappear when the matching units move forward.
Beth|The sales team asks whether return approval means we can put those six straight back into available inventory.
Joel|No. We still need the applicable [[disposition::Disposition is the authorized decision about what happens to the returned goods, such as restocking or another route after the required review.]]. Permission to return goods is not evidence that they meet the criteria for resale.
Beth|I will leave their status pending inspection. Should I also tell finance to issue the customer\'s full credit today?
Joel|Not on my authority. A [[credit note::A credit note records a financial adjustment; it follows the applicable commercial decision rather than automatically arising from physical receipt.]] has its own approval and amount under the agreed terms. I will ask finance what evidence they require.
Beth|The extra unit may have been sent by mistake. We should ask for its order reference rather than assume it belongs to this transaction.
Joel|Agreed. I will request the serial number history and the reason it was included, without promising acceptance or charging a fee we have not agreed.
Beth|Will you also explain that the warehouse receipt is complete but the return case remains open?
Joel|Yes. Our [[case status::The case status describes the whole return's progress; completion of receiving alone does not establish inspection, disposition, and credit completion.]] should show the completed and pending stages separately.
Beth|I can send the receipt count and photographs now. Inspection will provide its own findings when the authorized checks are complete.
Joel|That gives me a useful customer update: seven received, six matched, one under clarification, with inspection and credit decisions pending.
Beth|Please send any customer correction back to this case reference. We need the warehouse and finance teams working from the same record.
Joel|I will. Then we can resolve the physical and financial questions without one team treating another team\'s handover as final approval.''',
        transfer_title='Five returned items do not prove five credit approvals',
        transfer_setup='Five returned units have arrived. Inspection and the commercial credit decision are still pending.',
        transfer='''Coordinator: Receiving is complete, but inspection is still ___.|pending|Physical receipt does not establish the condition assessment needed for later decisions.
Service lead: Do not call the units saleable before the required ___.|disposition|The authorized disposition determines the appropriate route after the required review.
Coordinator: Keep the financial decision separate from warehouse ___.|receipt|The physical receiving event does not automatically approve a credit amount.
Service lead: Tell the customer which stages remain ___.|open|A useful update identifies unresolved stages rather than announcing completion prematurely.'''),
    scenario(
        title='The shipment arrived, but two cartons are crushed',
        skill='Document a delivery exception and request evidence without promising a claim outcome.',
        setup='A parcel delivery contains ten cartons. Two have visibly crushed corners, but their contents have not been inspected. The consignee contacts the shipping coordinator. They must preserve the facts, check the applicable carrier process, and keep replacement and claim decisions separate.',
        cast='Mina|Consignee receiving contact\nEvan|Shipping coordinator',
        dialogue='''Mina|All ten cartons arrived, but two have crushed corners. Our system says delivered, and the purchasing team thinks that means the order is fine.
Evan|Delivered records an event, not the condition of everything inside. Please open a [[delivery exception::A delivery exception records a problem associated with the delivery, keeping the condition concern visible alongside the arrival event.]] in our case system and identify the affected cartons.
Mina|I can send the tracking references and photographs of the outside. The contents have not been inspected yet.
Evan|State that clearly. We have visible [[packaging damage::Packaging damage describes the observed condition of the cartons; it does not automatically establish damage to every item inside.]], but we do not yet know the product condition or whether both cartons contain affected items.
Mina|Should we throw away the damaged cartons once the contents are checked? They are taking up space in receiving.
Evan|Please preserve the relevant [[packaging evidence::Packaging evidence can support a carrier's damage investigation; discarding it prematurely may prevent the requested inspection or documentation.]] and contents while we confirm the carrier\'s requirements and our safe handling arrangements.
Mina|I will keep them identified separately. There is no visible spill, but receiving will follow our procedure if anything hazardous is found.
Evan|Good. Do not improvise handling for an unknown hazard. For the commercial record, describe what was observed without guessing where the damage occurred.
Mina|Purchasing wants me to say the driver caused it. I did not see any impact during unloading, so I cannot support that statement.
Evan|Then do not include it. The [[claim investigation::The claim investigation examines the relevant facts and terms; a damage report alone does not determine responsibility or payment.]] needs observations and records, not an unsupported attribution.
Mina|What documents should I gather now, besides the photographs and tracking numbers?
Evan|The delivery record, item details, quantities, and relevant [[proof of value::Proof of value supports the amount being claimed under the applicable process; a quantity count alone does not establish that amount.]]. I will confirm the carrier-specific requirements and deadlines promptly.
Mina|We need the goods for a job tomorrow. Can you send replacements while the claim is being considered?
Evan|I will check stock and the authorized commercial options. A [[replacement order::A replacement order is a separate fulfillment action whose approval and availability must be checked rather than assumed from a damage report.]] is not automatically approved just because we intend to file a claim.
Mina|Please give us the replacement position even if the carrier has not responded. Those timelines may be quite different.
Evan|Agreed. I will update you on the supply options today and show the carrier case as a separate open item.
Mina|For the record, ten cartons arrived, two have visible packaging damage, and the content inspection is pending. Is that the right starting summary?
Evan|Yes. Add the identifiers and photographs so nobody reads two damaged cartons as ten damaged products or a confirmed total loss.
Mina|I will send that now and keep the affected material identifiable while the responsible team decides the next steps.
Evan|Thank you. We will report the actual findings and decisions as they arrive, without promising reimbursement before the claim has been assessed.''',
        transfer_title='An arrival scan hides an unresolved condition check',
        transfer_setup='A parcel is marked delivered. Its carton is torn, but the item inside has not been inspected and no claim outcome exists.',
        transfer='''Receiver: Delivery is recorded, but product condition is ___.|unconfirmed|An arrival scan does not establish the condition of an uninspected item.
Coordinator: Preserve the relevant carton and photographic ___.|evidence|The packaging and photographs may be required to support the damage investigation.
Receiver: Record what I observed, without assigning ___.|blame|Observation of damage alone does not establish which person or event caused it.
Coordinator: Keep any replacement decision separate from claim ___.|approval|A replacement action and a carrier's claim decision are separate processes.''',
        reference=('UPS: Filing and Supporting a Claim', 'https://www.ups.com/us/en/support/file-a-claim')),
]
