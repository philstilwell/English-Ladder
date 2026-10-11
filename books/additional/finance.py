"""Additional treasury, investment-appraisal, and consolidation discussions."""
from books.supplements import scenario

SCENARIOS = [
scenario(
    title='The supplier price is fixed, but the dollar cost is not',
    skill='Explain currency exposure and distinguish a budget rate from a contracted rate.',
    setup='A US business owes a supplier EUR 100,000 in sixty days. Its budget uses USD 1.10 per euro. The team compares that with an illustrative USD 1.15 per euro; neither is a live quote or an executed hedge. Treasury must review any hedging proposal.',
    cast='Maya|Treasury analyst\nJon|Procurement manager',
    dialogue='''
Jon|The supplier agreed a fixed price. Why has Finance increased the dollar forecast?
Maya|The invoice is fixed in euros, not dollars. We still have [[currency exposure::Currency exposure means the domestic-currency cost can change when the exchange rate changes.]] until the payment is covered under the approved arrangements.
Jon|The purchase order is for one hundred thousand euros. What did the budget assume?
Maya|One dollar ten per euro, so one hundred ten thousand dollars before any additional charges.
Jon|And at one dollar fifteen?
Maya|One hundred fifteen thousand. That's a five-thousand-dollar [[sensitivity::Sensitivity shows how a modeled result changes when an input changes, not a prediction that it will occur.]] to the rate change in this example.
Jon|Could I tell the supplier we need a five-thousand-dollar reduction?
Maya|You can discuss commercial options through your process, but the supplier hasn't changed the euro price. The forecast movement is on our currency side.
Jon|I thought Treasury locked the rate when we approved the budget.
Maya|A [[budget rate::Budget rate is an assumption for planning, not evidence that a foreign-exchange transaction was executed.]] isn't a trade confirmation. I'll check whether any approved coverage already applies to this payment.
Jon|Would an expected euro receipt reduce the amount we need to cover?
Maya|Potentially, if the currency, amount, timing, and availability align. We must verify those details before describing a [[natural hedge::Natural hedge means offsetting business cash flows reduce exposure without necessarily using a derivative.]].
Jon|We may receive forty thousand euros, but the customer hasn't confirmed the payment date.
Maya|Then show that receipt separately. Don't reduce the exposure as though the funds are already available on the supplier's due date.
Jon|What will Treasury need for its review?
Maya|The invoice, due date, existing coverage, expected receipts, and any change in the payment plan. We'll compare them with the approved [[hedging policy::Hedging policy defines the organization's permitted objectives, instruments, limits, and approval process.]].
Jon|If a hedge is executed, can I assume the accounting treatment is settled too?
Maya|No. The economic transaction and any hedge-accounting treatment require separate review under the applicable framework.
Jon|I'll send the confirmed payment details and flag the uncertain receipt.
Maya|Thanks. We'll report the proposal separately from an executed trade and retain its [[confirmation::Confirmation is the record of an executed transaction's terms, unlike an unexecuted proposal or indicative rate.]] if a transaction is authorized and completed.
''',
    transfer_title='An indicative rate appears in the payment forecast',
    transfer_setup='An analyst has copied an indicative bank rate into the forecast. No trade has been executed and no binding rate has been confirmed.',
    transfer='''
Manager: Is this the rate we've ___ for payment?|locked in|Locked in implies a binding arrangement, which the scenario has not established.
Analyst: No. It's an ___ rate used for this estimate.|indicative|Indicative describes an illustrative or nonbinding quotation rather than an executed transaction.
Manager: Then retain the foreign-currency amount and the rate ___ beside it.|assumption|Assumption identifies the input used to translate the amount for planning.
Analyst: I will update it when Treasury confirms the actual ___ status.|execution|Execution status distinguishes a proposed trade from one that has actually been completed.
'''),
scenario(
    title='The payback slide leaves out recurring maintenance',
    skill='Challenge an investment-appraisal shortcut and request a complete cash-flow basis.',
    setup='A proposed machine costs $600,000 initially. The sponsor estimates $150,000 of annual cash savings but excludes $30,000 of annual maintenance. Figures are constant illustrative amounts; tax, discounting, working capital, and residual value have not been modeled.',
    cast='Owen|Project sponsor\nLena|Capital-finance analyst',
    dialogue='''
Owen|The machine pays for itself in four years. Can we put that in the approval request?
Lena|Four years uses the gross savings. Where is the recurring maintenance in your [[cash-flow::Cash-flow identifies cash movements, which must include relevant outflows as well as expected savings.]] schedule?
Owen|I left it in the operating budget. It's thirty thousand a year.
Lena|It still affects this investment comparison. With that cost, the simple annual net benefit is one hundred twenty thousand, not one hundred fifty.
Owen|So simple payback becomes five years: six hundred thousand divided by one hundred twenty thousand.
Lena|Under those simplified assumptions, yes. But [[simple payback::Simple payback measures time to recover the initial outlay without discounting and may omit later cash flows.]] isn't a complete measure of value.
Owen|What else do you need before the committee reviews it?
Lena|Installation costs, useful life, ramp-up timing, working-capital effects, and the basis for the savings. We'll also review tax and residual-value assumptions.
Owen|The savings assume the machine operates at full capacity from day one.
Lena|Then add a [[ramp-up::Ramp-up is the period during which activity or output builds toward its expected operating level.]] case. Training and commissioning may delay the benefits, even if the purchase price doesn't change.
Owen|Would discounting make the payback calculation more accurate?
Lena|Discounted payback answers a related question, but we also need the complete present-value analysis required by our process. Don't relabel one metric as another.
Owen|I'll ask Engineering to confirm the installation schedule and expected useful life.
Lena|Good. I'll use the approved [[discount rate::Discount rate converts future cash flows to present values under the chosen investment-appraisal assumptions.]] and show how the result changes under relevant alternative assumptions.
Owen|Could we include the benefit of redeploying staff as a cash saving?
Lena|Only to the extent the cash-flow effect is supported. Freed capacity and reduced payroll aren't automatically the same benefit.
Owen|Then the staffing line needs an owner to validate what actually changes.
Lena|Exactly. Avoid [[double counting::Double counting includes the same economic benefit or cost more than once in the analysis.]] a productivity gain as both lower payroll and extra output without a consistent operating case.
Owen|I'll replace the four-year headline with the revised simple payback and the outstanding assumptions.
Lena|And we'll complete the [[investment appraisal::Investment appraisal evaluates the proposal using relevant costs, benefits, risks, and comparison criteria.]] before recommending approval. The arithmetic correction isn't approval of the project.
''',
    transfer_title='Freed staff time is presented as a payroll reduction',
    transfer_setup='A process change saves ten staff hours a week. The employees remain on the same paid schedules, and no approved staffing change exists.',
    transfer='''
Sponsor: Can I call the ten hours a payroll ___?|saving|Saving would imply a reduction in payroll cash cost, which is not established here.
Analyst: We have freed ___, not a confirmed reduction in pay.|capacity|Capacity is time available for other work even when payroll remains unchanged.
Sponsor: I'll show the operational benefit and identify the cash-flow ___ separately.|effect|Effect identifies the actual change in cash, which needs its own supported basis.
Analyst: Good. Don't count the same benefit twice in the ___ case.|business|Business case combines the proposal's evidence and assumptions for a decision.
'''),
scenario(
    title='Two subsidiaries disagree on an intercompany balance',
    skill='Reconcile counterpart records before explaining consolidation adjustments.',
    setup='Two subsidiaries are within the same consolidation group. Entity A reports a USD 60,000 receivable from Entity B. B reports a USD 55,000 payable to A for the same month-end. The USD 5,000 difference is unexplained. No adjustment has been approved.',
    cast='Rina|Group accountant\nCal|Entity B controller',
    dialogue='''
Rina|A's intercompany receivable is sixty thousand. Your payable is fifty-five. Can we reconcile the difference before the close review?
Cal|I have the invoice list. The totals don't match, but I haven't identified the missing item yet.
Rina|Let's compare by [[counterparty::Counterparty identifies the other entity in the transaction, which must match in both sides of the reconciliation.]] and invoice reference, not just the overall balances.
Cal|Both schedules name Entity A. Are they using the same cutoff?
Rina|That's the first check. A's schedule is month-end; please confirm your extract includes all postings through that date.
Cal|It does, but one invoice arrived after our last review. I'll check whether it was accrued or left out.
Rina|Good. Don't assume a late invoice means the service belongs to the next period. We need the [[cutoff::Cutoff concerns assigning transactions to the appropriate reporting period, not merely the date a document arrived.]] assessment and any existing entry.
Cal|Could Group just eliminate fifty-five thousand and leave the rest until next month?
Rina|We need to explain the [[reconciling difference::Reconciling difference is the unresolved mismatch between records that should agree under the defined basis.]]. An unexplained balance shouldn't disappear inside the consolidation process.
Cal|Understood. And a consolidation adjustment wouldn't automatically change our local ledger, would it?
Rina|Correct. The entity books and group consolidation entries are different records. Any required local correction follows its own approval route.
Cal|The operations manager thinks eliminating the intercompany sale means Group is deleting our revenue.
Rina|It removes internal activity from the [[consolidated::Consolidated statements present the included group as one economic entity rather than simply adding all internal transactions.]] view. It doesn't mean the underlying transaction never occurred in the entity's books.
Cal|I'll explain that distinction. Do you also need the service period on each invoice?
Rina|Yes, and the currency, posted amount, and any related accrual or credit note.
Cal|I'll send a revised [[reconciliation::Reconciliation compares corresponding records and explains or resolves the differences between them.]] showing the exact five-thousand-dollar item if I can trace it.
Rina|If it remains unresolved, keep it visible with an owner and the next check. Don't insert a balancing entry just to make the schedules agree.
Cal|Agreed. I'll bring the supporting records and any proposed correction for review.
Rina|Then Group can assess the appropriate [[elimination::Elimination is a consolidation adjustment removing intragroup balances or transactions under the applicable accounting rules.]] after the underlying difference has been addressed.
Cal|I'll send the status this afternoon, including whether the amount, period, and approval are actually confirmed.
''',
    transfer_title='A group adjustment is mistaken for a local posting',
    transfer_setup='A group accountant has prepared an intercompany elimination in the consolidation file. No local-ledger correction has been authorized.',
    transfer='''
Controller: Does the group adjustment change our local ___ automatically?|ledger|Ledger is the entity's own accounting record, separate from the consolidation file.
Group accountant: No. This entry belongs to the ___ process.|consolidation|Consolidation combines the included entities into the group reporting view.
Controller: Any local correction still needs its own support and ___.|approval|Approval authorizes the local correction; a group-level entry does not supply it automatically.
Group accountant: Exactly. Keep the two records ___ and traceable.|distinct|Distinct means separately identified so each entry's purpose and authority remain clear.
'''),
]
