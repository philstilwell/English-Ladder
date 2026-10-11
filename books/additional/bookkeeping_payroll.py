"""Original prepayment, bonus true-up, and receivables-aging conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Paid once, expensed over time",
        skill="Explain a prepaid service schedule without confusing cash, cumulative expense, and the current adjustment.",
        setup="Fictional annual support subscription: $1,200 paid July 1 for service July 1 through June 30. The accountant specifies equal monthly recognition over twelve months, with no tax, impairment, cancellation, or other adjustment. July and August expenses of $100 each are already posted. It is September 30; the September adjustment is not posted. Discuss the proposed schedule, not instructions to post or pay.",
        cast="Nia|Bookkeeper\nOmar|Department manager",
        dialogue="""Omar|The support supplier was paid twelve hundred dollars in July. Why does September's draft report show another hundred of expense? Are we paying them twice?
Nia|No. The original payment created a [[prepaid expense::The payment covers future support service; the specified accounting treatment initially carries the unconsumed cost as an asset rather than treating each later expense as a new payment.]]. The monthly recognition uses that already-paid amount; it doesn't send the supplier more money.
Omar|The service runs from July first to next June thirtieth. So the twelve hundred covers twelve months, not just the calendar months remaining this year.
Nia|Correct. Under the supplied [[recognition schedule::The accountant specifies twelve equal monthly amounts across July through June, so $1,200 divided by twelve is $100 per month, not a six-month allocation.]], each month is one hundred dollars. We don't divide it by six just because the payment was made in July.
Omar|By September thirtieth, July, August, and September have passed. That makes three hundred dollars of expense for those three months together.
Nia|Yes, that's the proposed [[cumulative expense::Three months at $100 each produce $300 cumulative expense through September; that is not the amount to add if July and August are already posted.]] through September. But July and August's two hundred dollars are already recorded.
Omar|Then posting another three hundred for September would double-count those earlier two months. The new month adds only one hundred.
Nia|Exactly. The proposed [[current-period adjustment::Only September's $100 remains to be recognized; adding $300 again would repeat the $200 already posted for July and August.]] is one hundred, not three hundred. A cumulative target and the incremental amount needed to reach it are different.
Omar|After that proposed adjustment, nine months remain: October through June. At a hundred a month, the unused service balance would be nine hundred.
Nia|That's the proposed [[carrying amount::After recognizing $300 of the $1,200 cost, the remaining prepaid asset is $900 under the supplied schedule; it is not a bank balance or a refund claim.]] of the prepaid asset. It's not nine hundred dollars sitting in the bank or automatically refundable by the supplier.
Omar|What does the ledger show before September is posted? It should still have one thousand of prepaid service, since only two hundred has moved to expense.
Nia|Right. The September recognition is a [[noncash adjustment::Recognizing the used portion reduces the prepaid asset and increases expense without another cash payment; the original $1,200 cash outflow occurred in July.]]. It would reduce the prepaid balance from one thousand to nine hundred without changing cash.
Omar|So the bank payment stays twelve hundred in July. We shouldn't enter a new supplier invoice or another cash payment every month to explain the expense.
Nia|Correct. The schedule allocates the existing cost. A monthly expense line is not evidence of a monthly invoice or a second payment.
Omar|If the whole contract had been charged to July expense instead, this one-hundred-dollar proposal wouldn't describe the same starting ledger.
Nia|Exactly. The actual starting balance matters. This case explicitly says July and August were posted according to the prepaid schedule; we aren't correcting a different initial treatment.
Omar|Can I report September as complete now that the calculation agrees? The adjustment still hasn't gone through review and posting.
Nia|Keep it proposed. The arithmetic supports the schedule, but doesn't show that the required review or posting has occurred.
Omar|I'll explain twelve hundred paid once, two hundred already expensed, one hundred proposed for September, three hundred cumulative, and nine hundred remaining afterward.
Nia|That readback keeps cash, the ledger before adjustment, and the proposed closing balances distinct. Attach the service dates and schedule so the reviewer can follow the period basis.""",
        transfer_title="Separate cumulative and incremental",
        transfer_setup="Fictional support subscription $2,400 for twelve months starting April 1, recognized equally monthly. April and May expense is already posted at $200 each. June 30 review is pending; June expense is not posted. No other adjustments or new payments apply.",
        transfer="""Manager: Expense through June should total ___ dollars.|600|April, May, and June are three months at $200, totaling $600 cumulatively.
Bookkeeper: Only ___ dollars remains for June recognition.|200|The $400 for April and May is already posted, so the incremental June amount is $200, not $600.
Manager: The proposed prepaid balance after June is ___ dollars.|1800|The original $2,400 less $600 cumulative expense leaves $1,800 of unconsumed service.
Bookkeeper: The June allocation requires ___ additional cash payment.|no|The service was paid in advance; recognizing June's portion is not another supplier payment.""",
        reference=("OpenStax: prepaid expense recognition and noncash period adjustments", "https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries"),
    ),
    scenario(
        title="The bonus changes the regular rate",
        skill="Explain an overtime recalculation without confusing base rate, regular rate, total gross, and the remaining true-up.",
        setup="Fictional US employee covered and nonexempt under the Fair Labor Standards Act (FLSA): one 44-hour workweek at $20/hour, plus an $88 production bonus earned entirely that week and confirmed includable in the regular rate. Use weekly overtime after 40 hours; no other compensation or rules alter this example. Original gross paid $920: $880 straight time plus $40 overtime premium. Bonus and related true-up remain unpaid. This is gross-pay explanation, not tax or case-specific legal advice.",
        cast="Leila|Payroll assistant\nMorgan|Payroll reviewer",
        dialogue="""Leila|The original gross was nine hundred twenty dollars. I added the eighty-eight-dollar bonus and got one thousand eight. Is that the complete corrected amount?
Morgan|Not yet. The confirmed [[nondiscretionary bonus::The supplied production bonus is includable in the regular rate and earned entirely in this workweek, so it changes the overtime calculation as well as adding eighty-eight dollars.]] belongs in this week's regular-rate calculation. Adding it to the old total alone misses the related overtime difference.
Leila|Straight-time earnings are forty-four hours at twenty dollars: eight hundred eighty. Adding the bonus gives nine hundred sixty-eight before the overtime premium.
Morgan|Right. The [[regular rate::The includable straight-time earnings plus bonus are $968; dividing by all forty-four worked hours gives a $22 regular rate, not the $20 base rate.]] is nine hundred sixty-eight divided by forty-four, or twenty-two dollars per hour. That's different from the twenty-dollar base rate.
Leila|I shouldn't divide by forty and exclude the overtime hours from the denominator. All forty-four worked hours belong in that calculation.
Morgan|Correct. And because straight time for all forty-four hours is included already, the extra [[half-time premium::With straight time for every worked hour already included, the additional overtime premium is half of the $22 regular rate, or $11 for each of four overtime hours.]] is eleven dollars for each overtime hour, not another full thirty-three.
Leila|There are four overtime hours. Four times eleven gives forty-four dollars of overtime premium in the corrected calculation.
Morgan|Yes. The corrected [[gross earnings::The $968 straight-time-plus-bonus amount plus $44 overtime premium totals $1,012 gross, before taxes or other deductions.]] are nine hundred sixty-eight plus forty-four, or one thousand twelve, before deductions.
Leila|The old payroll already paid forty dollars of overtime premium. So we don't owe a second full forty-four on top of that.
Morgan|Exactly. The remaining overtime [[true-up::The corrected premium is $44, of which $40 was already paid; the additional overtime amount is $4, separate from the still-unpaid $88 bonus.]] is four dollars. With the unpaid eighty-eight-dollar bonus, the remaining gross payment is ninety-two.
Leila|That reconciles: nine hundred twenty already paid plus ninety-two still due equals one thousand twelve. The bonus and the overtime increase are separate lines.
Morgan|Keep that [[payroll reconciliation::The original $920 gross plus the $88 unpaid bonus and $4 premium difference equals the corrected $1,012 total; neither the full premium nor the original pay is paid twice.]] in the review note. It shows the complete entitlement calculation and the smaller amount remaining, without double counting.
Leila|Would calling the payment discretionary on a spreadsheet remove it from this calculation? The approved facts say it was an includable production bonus.
Morgan|A label alone doesn't change its treatment. Here the classification and earning week are supplied; don't replace them with a more convenient label.
Leila|If the bonus covered several weeks instead, could I put the whole amount into whichever week we happen to process it?
Morgan|That isn't the fact pattern here. The actual earning period and applicable allocation rules would need review; this example puts it entirely in one specified workweek.
Leila|And ninety-two isn't a promise about the net amount deposited. We haven't modeled withholding or any other deductions.
Morgan|Right. Every amount in this reconciliation is gross. Keep the review in the private payroll channel and don't invent a tax rate or net deposit.
Leila|I'll show base rate twenty, regular rate twenty-two, four overtime hours, total gross one thousand twelve, and ninety-two gross remaining including the bonus.
Morgan|That is the corrected explanation under the stated assumptions. It doesn't determine anyone else's classification, bonus treatment, state-law entitlement, or actual payroll outcome.""",
        transfer_title="Recalculate another included bonus",
        transfer_setup="Same simplified US FLSA assumptions: 46 worked hours at $18/hour, plus a confirmed includable $92 bonus earned entirely that week. Original gross already paid $882: $828 straight time plus $54 overtime premium. Six overtime hours; bonus and true-up unpaid. No other pay components, deductions, or rules are modeled.",
        transfer="""Assistant: The regular rate is ___ dollars per hour.|20|Straight time $828 plus bonus $92 equals $920; dividing by forty-six hours gives $20, not the $18 base rate.
Reviewer: The corrected additional half-time premium totals ___ dollars.|60|Half of the $20 regular rate is $10; six overtime hours therefore require $60 premium in total.
Assistant: Corrected total gross is ___ dollars.|980|The $920 straight-time-plus-bonus amount plus $60 premium equals $980 gross.
Reviewer: Beyond the unpaid bonus, the overtime true-up is ___ dollars.|six|The corrected $60 premium less the $54 already paid leaves $6 extra, not another full $60.""",
        reference=("US Department of Labor: Fact Sheet 56C, included bonuses and the regular rate", "https://www.dol.gov/agencies/whd/fact-sheets/56c-bonuses"),
    ),
    scenario(
        title="Age the balance from the due date",
        skill="Explain an aged-receivables report using the correct date basis and outstanding amount.",
        setup="Fictional report: aging date and balance cutoff both October 31. Due-date aging; overdue starts the day after the due date. Buckets: current, 1-30 days, 31-60 days. A: issued September 1, due October 1, $500 invoice with $100 already applied, $400 open. B: issued September 30, due October 30, $300 open. C: issued October 1, due November 15, $200 open. No other items or later receipts.",
        cast="Ava|Receivables clerk\nLuis|Account manager",
        dialogue="""Luis|Invoice A was issued on September first. At October thirty-first, that looks sixty days old, so I've put its five hundred dollars in the thirty-one-to-sixty column.
Ava|This report uses the [[due-date basis::The report ages from the due date, not the issue date; A is due October 1 and is thirty days past due on October 31.]], not issue-date age. A was due October first, so it's thirty days past due, not sixty.
Luis|Then October second is day one overdue, and October thirty-first is day thirty. It belongs in the one-to-thirty bucket.
Ava|Yes. Keep the [[aging date::October 31 is the fixed date against which overdue days are measured; using today's date or the invoice issue date would change the report's meaning.]] visible as October thirty-first. We shouldn't let a later date change the explanation of this saved report.
Luis|What about the amount? A's invoice is five hundred, but a hundred has already been applied before the cutoff.
Ava|Age the [[open balance::A's original $500 invoice less the $100 already applied leaves $400 outstanding; the aging bucket must contain $400, not the full original invoice amount.]] of four hundred. The paid portion doesn't remain outstanding just because the original invoice still shows five hundred.
Luis|Invoice B is due October thirtieth, so on October thirty-first it's one day overdue. Its three hundred goes in the same bucket as A.
Ava|Correct. The [[aging bucket::The stated 1-30-day bucket includes both one and thirty days; A's $400 and B's $300 therefore total $700 in that bucket.]] includes both endpoints. Four hundred plus three hundred gives seven hundred in one-to-thirty days.
Luis|C was issued October first, but it isn't due until November fifteenth. Is its two hundred current even though the invoice is a month old?
Ava|Yes. A [[current balance::C is not yet due at the October 31 aging date, so its $200 is current despite having an October 1 issue date.]] means not overdue under these report definitions. Issue-date age doesn't move that two hundred into an overdue bucket.
Luis|Then the report totals two hundred current, seven hundred one-to-thirty, and zero thirty-one-to-sixty. Total open receivables are nine hundred.
Ava|That's the [[control total::The three open balances are $400, $300, and $200, totaling $900; the bucket amounts must reconcile to that same total without adding the applied $100 again.]] across the three items. It must match the sum of the buckets without adding A's applied hundred back in.
Luis|If we changed the report to age by document date, some buckets would change even if no customer paid another dollar.
Ava|Exactly. A changed basis can move balances between columns. That movement isn't automatically a deterioration in payment behavior or a new cash event.
Luis|And if someone runs the balance cutoff at a later date while keeping October thirty-first for aging, it may include different payment information.
Ava|Yes. That's why this case fixes both dates at October thirty-first. A comparison needs the same date settings or an explicit explanation of the difference.
Luis|Does being thirty days overdue mean A is automatically written off, or that a late fee has already been authorized?
Ava|No. This report classifies the supplied open balance. It doesn't establish a write-off, a fee, a collection action, or a credit-loss conclusion.
Luis|I'll correct A from five hundred at sixty days to four hundred at thirty days, and retain the stated dates beside the totals.
Ava|Good. Read back two hundred current, seven hundred one-to-thirty, zero thirty-one-to-sixty, total nine hundred. That describes the actual report rather than the age of the original paperwork.""",
        transfer_title="Check the bucket boundary",
        transfer_setup="Fictional aging date and balance cutoff November 30; same due-date basis and inclusive buckets. D: due October 30, $260 invoice less $60 already applied. E: due November 30, $150 open, not overdue on its due date. F: due November 15, $90 open. No other entries.",
        transfer="""Clerk: D is ___ days past due.|31|From October 30 to November 30 is thirty-one days; overdue begins October 31, placing D in the 31-60 bucket.
Manager: D's open balance in that bucket is ___ dollars.|200|The $260 invoice less the $60 applied payment leaves $200 outstanding.
Clerk: E's $150 belongs in the ___ bucket.|current|An item due on November 30 is not yet overdue on that same date under the supplied rule.
Manager: Total open receivables are ___ dollars.|440|D $200 plus E $150 plus F $90 equals $440; the already-applied $60 is not added back.""",
        reference=("Microsoft Learn: customer aging dates, balances, and date criteria", "https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-aging"),
    ),
]
