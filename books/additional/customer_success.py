"""Original retention, co-termination, and customer-exit conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Growth can hide lost customers",
        skill="Reconcile customer retention and recurring-revenue retention using the same starting cohort.",
        setup="Fictional annual recurring revenue bridge: ten starting accounts, $100,000 starting ARR. Two accounts leave, losing $20,000; remaining accounts contract $10,000 and expand $35,000. Three new accounts add $30,000. No other changes, reactivations, or currency effects occur. Retention measures use the original ten-account cohort; all figures use the same annualized basis.",
        cast="Inez|Customer success director\nMalik|Revenue operations analyst",
        dialogue="""Inez|The total recurring-revenue line is up, but we lost two customers. I want the review to explain both facts rather than use growth as a synonym for retention.
Malik|Start with the [[starting cohort::The starting cohort is the ten accounts present at the beginning, with 100,000 annual recurring revenue; newly acquired accounts are outside this retention population.]]: ten accounts and one hundred thousand in annual recurring revenue. The three new accounts belong in the total revenue bridge, not in the retention numerator.
Inez|Two of those ten left, so eight remain. That makes account retention eighty percent, even though we finish with eleven accounts after adding three new ones.
Malik|Correct. [[Logo retention::Logo retention measures how many starting customer accounts remain; eight of the original ten is 80%, not eleven divided by ten after including new customers.]] counts retained customer accounts. The ending account count tells a different story and does not turn retention into one hundred ten percent.
Inez|Now take out the twenty thousand from the two departures and ten thousand of contraction. That leaves seventy thousand before expansion.
Malik|So [[gross revenue retention::Gross revenue retention excludes expansion: (100,000 minus 20,000 churn minus 10,000 contraction) divided by 100,000 equals 70%.]] is seventy percent. It shows how much starting recurring revenue remains before the existing customers' additional spending is included.
Inez|The remaining accounts expanded by thirty-five thousand. Adding that to seventy gives one hundred five thousand from the original cohort at the end.
Malik|That makes [[net revenue retention::Net revenue retention includes the original cohort's expansion: (100,000 minus 20,000 minus 10,000 plus 35,000) divided by 100,000 equals 105%; new customers are excluded.]] one hundred five percent. The measure can exceed one hundred because expansion within retained accounts can outweigh churn and contraction.
Inez|But it does not mean we retained every customer or every dollar before expansion. The eighty-percent account figure and seventy-percent gross figure still matter.
Malik|Exactly. A strong net number can coexist with losses. We should show the components so an expansion in one account does not make another customer's departure disappear.
Inez|The three new accounts contribute thirty thousand. Where does that sit in the full revenue report without contaminating the retention calculation?
Malik|Show it as [[new-logo revenue::New-logo revenue is the 30,000 annual recurring revenue from three newly acquired accounts; it contributes to ending total ARR but not retention of the original cohort.]]. Add it after the one-hundred-five-thousand cohort result to reach one hundred thirty-five thousand in total ending ARR.
Inez|The overall ARR growth is therefore thirty-five percent on the one-hundred-thousand starting base. It is not a net retention rate of one hundred thirty-five percent.
Malik|Right. Keep the [[revenue bridge::The revenue bridge reconciles starting and ending recurring revenue through separate churn, contraction, expansion, and new-customer movements on a consistent basis.]] labeled: starting amount, churn, contraction, expansion, and new business. That lets people follow the calculation rather than guess what a percentage includes.
Inez|For the two departures, we need the actual reasons and timing. I do not want a generic poor-adoption label unless the account evidence supports it.
Malik|We can attach the documented reasons and identify unknowns. The arithmetic shows what changed; it does not diagnose the cause of every customer decision.
Inez|And the contracted accounts still exist. We must not count their ten-thousand reduction as another lost logo simply because recurring value fell.
Malik|Correct. Logo loss and contraction are different movements. We should reconcile the account-level records to the totals and keep the original cohort fixed for this period.
Inez|I will present eighty-percent logo retention, seventy-percent gross retention, one-hundred-five-percent net retention, and one hundred thirty-five thousand ending ARR as four distinct results.
Malik|That gives the team a useful review. We can celebrate expansion and acquisition while still addressing the two departures and the reduced spending within continuing accounts.""",
        transfer_title="Keep acquisition out of retention",
        transfer_setup="A starting cohort has 20 accounts and $200,000 ARR. Four accounts leave, losing $30,000; contraction is $10,000 and expansion is $20,000. New customers add $50,000. No other changes occur; all amounts use the same annualized basis.",
        transfer="""Director: Retention of the original accounts is ___ percent.|80|Sixteen of twenty original accounts remain, so logo retention is eighty percent; new customers do not enter that count.
Analyst: Retained ARR before expansion is $___ thousand.|160|Two hundred thousand less thirty thousand churn and ten thousand contraction leaves one hundred sixty thousand.
Director: Net revenue retention is ___ percent.|90|Adding twenty thousand expansion gives one hundred eighty thousand from the original two-hundred-thousand cohort, or ninety percent.
Analyst: Including new customers, ending ARR is $___ thousand.|230|The original cohort's one hundred eighty thousand plus fifty thousand of new business totals two hundred thirty thousand.""",
        reference=("Gainsight: recurring-revenue movements, gross retention, and net retention", "https://www.gainsight.com/essential-guide/recurring-revenue/"),
    ),
    scenario(
        title="The part-year seat charge",
        skill="Read back a co-terminated seat addition with an explicit period, discount scope, and separate renewal illustration.",
        setup="Fictional quote: 100 existing seats end 31 December. Add 15 for October-December at $20/seat/month, whole-month billing, 10% discount on this addition only. Existing charges unchanged; no setup fee; tax excluded. Next-year illustration: 115 seats, 12 months, same rate, no discount; renewal unapproved.",
        cast="Suki|Customer administrator\nMarco|Customer success manager",
        dialogue="""Suki|I expected another annual charge for the fifteen seats, but your quote is much smaller. Can you explain the dates before I send it to finance?
Marco|The addition uses [[co-termination::Co-termination aligns the added seats' end date with the existing subscription, here 31 December, rather than creating a new twelve-month term from 1 October.]]. The new seats end on December thirty-first with the existing hundred, so this quote covers October, November, and December only.
Suki|Then it is fifteen seats at twenty dollars for three whole months. That is nine hundred dollars before the quoted discount, not thirty-six hundred for a year.
Marco|Correct. The stipulated [[proration basis::The proration basis in this fictional quote is whole months: 15 seats times 20 dollars times three months equals 900 before discount; other systems or contracts may use different timing rules.]] uses whole months, not days or seconds. That is the rule supplied by this quote.
Suki|The discount is ten percent. Is that ten percent off our entire subscription, or just the new-seat charge on this quote?
Marco|The [[discount scope::The discount scope is limited to the three-month addition; ten percent of 900 is 90, leaving 810 before tax, with existing charges unchanged.]] is the three-month addition only. Ninety dollars comes off nine hundred, leaving eight hundred ten before tax. It does not create a credit against existing seats.
Suki|The account would then have one hundred fifteen seats until December thirty-first. The smaller invoice does not mean the extra seats disappear after one month.
Marco|Exactly. The [[service period::The service period is 1 October through 31 December for all fifteen added seats; the discounted charge does not shorten that stated period or renew it automatically in this exercise.]] covers all three months. The approved quote should show the quantity, unit rate, period, discount, and resulting amount on the same basis.
Suki|Could you also show finance what a full next year would look like if we kept all one hundred fifteen at the same rate?
Marco|Yes, as a [[renewal illustration::The renewal illustration is a conditional comparison, not an approved renewal: 115 seats times 20 dollars times 12 months equals 27,600 before tax with no assumed discount.]]. At twenty dollars per seat per month for twelve months, without a discount, that would be twenty-seven thousand six hundred before tax.
Suki|That is much more than eight hundred ten, but they are different scopes. One is fifteen extra seats for a quarter; the other is all one hundred fifteen for a year.
Marco|Right. We should not present that as a price increase derived by comparing the two totals. Both the seat count and the duration have changed.
Suki|May I carry the ten-percent discount into next year's budget? It would be convenient to use the same assumption for the renewal.
Marco|Not as an agreed term. The current approval covers only this addition. Any [[renewal discount::A renewal discount would require its own applicable approval and terms; the limited discount on the current three-month addition cannot be silently carried into the next twelve-month term.]] is separate. The illustration we just calculated explicitly assumes none.
Suki|And tax is still outside both figures. I should not describe either amount as the final tax-inclusive payment due.
Marco|Correct. Billing can confirm the applicable tax treatment on the actual invoice. The supplied comparison is pre-tax and includes no setup charge.
Suki|I will send finance the approved addition and the clearly labeled renewal illustration separately. The latter should not look like an order we have already accepted.
Marco|That is the right distinction. Check the customer's purchasing route for the addition and leave next year's quantity and terms subject to the renewal decision.
Suki|Let me read it back: fifteen added seats, three months, nine hundred before discount, ninety discount, eight hundred ten before tax, ending December thirty-first.
Marco|Correct. The separate full-year illustration is one hundred fifteen seats at the stated rate, totaling twenty-seven thousand six hundred before tax, without an approved renewal or carried-over discount.""",
        transfer_title="Calculate another co-terminated addition",
        transfer_setup="A fictional quote adds 12 seats for four whole months at $25 per seat per month. A 15% discount applies only to that addition. No setup fee; tax excluded. The added seats end on the existing subscription's end date.",
        transfer="""Customer: Before discount, the addition costs $___.|1,200|Twelve seats times twenty-five dollars times four months equals twelve hundred dollars.
Manager: The discount amount is $___.|180|Fifteen percent of twelve hundred equals one hundred eighty dollars.
Customer: The resulting pre-tax amount is $___.|1,020|Twelve hundred minus one hundred eighty equals one thousand twenty before tax.
Manager: The shared end date is called ___.|co-termination|Co-termination aligns subscription end dates; it does not by itself establish a discount for a later renewal.""",
        reference=("Stripe documentation: proration and discount behavior varies with billing configuration; the exercise supplies its own whole-month terms", "https://docs.stripe.com/billing/subscriptions/prorations"),
    ),
    scenario(
        title="Help a departing customer leave well",
        skill="Confirm export scope, verify receipt, and separate ending access from data deletion without obstructing a customer exit.",
        setup="Fictional exit: access ends 31 October, 18:00 UTC; extensions need approval. An authorized administrator must retrieve and check separate records and attachment exports beforehand. Deletion and backups require specialist confirmation under the applicable agreement. The customer has declined another retention meeting.",
        cast="Dana|Customer operations lead\nEllis|Customer success manager",
        dialogue="""Dana|We have decided to move, and I have declined another renewal meeting. Can we focus this call on getting our records and attachments out before access ends?
Ellis|Yes. The [[offboarding plan::The offboarding plan coordinates the agreed exit, including owners, export checks, access timing, and required follow-up; assistance is not made conditional on another retention discussion.]] should help you complete that transition. I will not make export assistance depend on reopening the commercial decision.
Dana|Our administrator downloaded a records file yesterday. The row count matches the account total, so someone marked the export complete. I do not see the attachments.
Ellis|That is an [[export scope::Export scope defines which data and file types are included; the records file alone is incomplete because attachments require a separate export in this fictional service.]] gap. Records and attachments use separate files here. A matching row count does not establish that every required attachment has been retrieved.
Dana|We need both, and we need to know which attachment belongs to which record. Otherwise the receiving team will have a folder of files it cannot use.
Ellis|Check the [[record identifier::The record identifier links each exported attachment to its related record; preserving and checking that relationship is necessary for a usable handover, not merely a successful download.]] mapping using the approved export guide. Your administrator should test the links and a suitable sample of files, not just confirm that a download finished.
Dana|Our migration provider offered to collect the files. Can I forward my administrator's password so they can do it without waiting for another account?
Ellis|No. Use the [[authorized recipient::An authorized recipient is a person or party cleared to receive the specified data through approved arrangements; credential sharing does not establish that authorization or provide an acceptable transfer route.]] and access arrangements your team has approved. We can coordinate the permitted route without sharing an individual's credentials.
Dana|The cutoff is October thirty-first at eighteen hundred UTC. Does submitting a support ticket automatically keep the account open after that time?
Ellis|No. An [[access extension::An access extension changes the agreed availability period and requires approval; opening a support ticket does not automatically extend the 31 October, 18:00 UTC cutoff.]] requires approval. Raise any likely delay now so we can assess it, but keep the existing cutoff in the plan until it changes formally.
Dana|Once the files are received, I will ask our administrator to confirm the contents and report missing items. We should do that while there is still time to resolve a problem.
Ellis|Agreed. Record the file versions, receipt, and validation results. Receipt alone is not acceptance that the handover is complete, especially if the attachments have not been checked.
Dana|Does access ending also mean every copy of our data disappears instantly from your systems and backups? Our director wants a clear statement for the exit record.
Ellis|I cannot promise that. The [[deletion confirmation::Deletion confirmation must describe the verified scope and status under the applicable agreement and law, including any relevant backup or retention treatment; access ending alone proves none of those actions.]] must come through the authorized process and state what was completed, what remains, and any applicable retention basis.
Dana|Then please keep export, access closure, and deletion as separate items. I do not want a closed support ticket used as evidence for all three.
Ellis|I will. The specialist team will confirm the applicable handling and timing, including backups and any lawful retention requirement. I will not invent a universal deletion period for this conversation.
Dana|We also have an integration that sends records nightly. Our technical owner needs to know when it must stop and how the receiving system will take over.
Ellis|Include that dependency in the exit plan with the technical owners. Confirm the agreed cutoff and replacement process; do not leave an unattended integration sending data into a closed service.
Dana|The next steps are the separate attachment export, relationship checks, authorized receipt, and confirmation of the closure and deletion processes. No further retention pitch is needed.
Ellis|Understood. I will send the plan and owners, keep the stated access deadline visible, and track unresolved items through the agreed support route until the defined handover is complete.""",
        transfer_title="Check another customer exit",
        transfer_setup="An agreed exit requires separate records and attachment exports before 20 June at 16:00 UTC. The records file is received, but attachments are missing. A support ticket is open; no access extension is approved. Deletion status has not been confirmed.",
        transfer="""Customer: The missing export contains ___.|attachments|Receiving the records file does not satisfy the separately required attachment handover.
Manager: Access still ends at ___ UTC on 20 June.|16:00|The stated cutoff remains in force because no extension has been approved.
Customer: Opening a ticket does not approve an access ___.|extension|A support request starts a review; it does not independently change the agreed access period.
Manager: Deletion status remains ___.|unconfirmed|Neither the records receipt nor the future access cutoff establishes that deletion has been completed.""",
        reference=("UK Information Commissioner's Office: end-of-contract processing terms; check applicable law and agreement, with guidance under review", "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/"),
    ),
]
