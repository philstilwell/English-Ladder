"""Original finance-team communication cases with explicit calculation bases."""
from books.authoring import unit

BOOK = dict(
    slug='finance', title='Finance English', cover_label='Finance teams / evidence / decisions',
    cover_title='Finance', tagline='Explain the numbers. Preserve the assumptions. Make the next step clear.',
    audience='For accounting, financial planning, treasury, investment, credit, audit, and corporate-finance professionals.',
    map_intro='Move from a headline number to its basis, drivers, uncertainty, and decision.',
    notes_title='A number needs its basis.',
    notes_intro='Finance conversations connect measurements to decisions. The same number can mean different things when its period, currency, comparison, fee treatment, or approval status changes. These fictional cases practice the language that keeps those distinctions visible.',
    field_notes=[
        ('Name the comparison', 'Above budget, up on last year, and ahead of the previous forecast are different claims. State the period and comparison before explaining the movement.', '"Revenue is 5% above this month\'s budget, not 5% above last year."'),
        ('Separate result from estimate', 'An actual result, an updated forecast, and a sensitivity calculation carry different kinds of certainty. Name the status and the important assumptions.', '"The cash balance is forecast on the assumption that the customer pays Friday."'),
        ('Explain the unit', 'Distinguish dollars, percentages, percentage points, and basis points. Identify the denominator when quoting a ratio and do not hide a change in calculation basis.', '"The return difference is one percentage point, before the stated fee adjustment."'),
        ('Match the claim to the review', 'A balanced reconciliation, a reviewed assumption, and an approved decision are separate accomplishments. Report what is complete and what still needs evidence or authorization.', '"The difference is identified; the correcting entry is not yet approved."')],
    scope_note='Fictional English-language practice, not investment, lending, accounting, tax, or legal advice. Definitions are concise teaching descriptions. Actual treatments and decisions require current standards, governing documents, firm policies, and qualified review. No product or transaction is recommended.',
    sources=[
        dict(title='US Securities and Exchange Commission. Beginners\' Guide to Financial Statement.', url='https://www.sec.gov/investor/pubs/begfinstmtguide.htm', note='Background for distinguishing financial statements, profit, cash flow, and explanatory notes. Teaching cases and calculations are original.', checked='10 October 2026'),
        dict(title='Investor.gov. Investing glossary.', url='https://www.investor.gov/introduction-investing/investing-basics/glossary', note='Reference point for investment nomenclature. Simplified definitions in this book do not replace product terms or professional analysis.', checked='10 October 2026'),
        dict(title='Public Company Accounting Oversight Board. AS 2201.', url='https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201', note='Background for US public-company internal-control audit terminology. Its scope is not assumed to cover every organization or jurisdiction.', checked='10 October 2026'),
        dict(title='IFRS Foundation. IFRS 10 Consolidated Financial Statements.', url='https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/', note='Background for presenting a consolidation group as one economic entity. Actual group boundaries, eliminations, and local entries require the applicable accounting framework and review.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Finance Communication: Drivers, Assumptions, Materiality, Risk', scene='Revenue is ahead, but profit is behind',
    skill='Explain opposing financial movements using the same period, comparison, and calculation basis.',
    brief='For the month, budgeted revenue was $1,000,000 and operating costs were $800,000. Actual revenue was $1,050,000 and operating costs were $854,000. The cost increase comprises $30,000 in freight and $24,000 in agency labor. The analyst has verified those categories but has not separated rate and volume effects or assessed recurrence. Lena, the analyst, and Amir, the finance director, are preparing a concise management-review explanation. All figures use the same currency and reporting scope.',
    cast='Lena | Finance analyst\nAmir | Finance director',
    culture=('Answer the apparent contradiction', 'A manager may interrupt with "How can sales be up and profit down?" Treat this as a request to connect the figures, not necessarily a personal challenge. Give the comparison and the offsetting movement first, then separate established categories from causes still being tested.'),
    a='''What is actual operating profit in this case? | $196,000 | $200,000 | $250,000 | $54,000 | Actual revenue of $1,050,000 less operating costs of $854,000 gives operating profit of $196,000.
How much did costs exceed budget? | $54,000 | $50,000 | $4,000 | $24,000 | Subtract budgeted costs of $800,000 from actual costs of $854,000; the category increases also total $54,000.
Which question remains unresolved? | How much of the cost increase reflects rate versus volume | Whether revenue is $1,050,000 | Whether the comparison uses the same month | Whether the two cost categories total $54,000 | The briefing verifies category amounts but explicitly leaves rate, volume, and recurrence analysis incomplete.''',
    vocabulary='''revenue | Income recognized from the business's goods or services under the relevant basis. | report recognized revenue
operating cost | A cost included in the stated measure of operating activity. | analyze operating costs
operating profit | Revenue less the operating costs included in the stated presentation. | explain operating profit
gross profit | Revenue less the specified cost of goods or services sold. | distinguish gross from operating profit
net income | Profit after the expenses and other items in the applicable presentation. | reconcile net income
variance | A difference between a result and its stated comparator. | explain a budget variance
driver | A factor contributing to a financial movement. | isolate the main driver
offset | A movement that counteracts another movement. | quantify the cost offset
favorable | Beneficial against the specified comparison or objective. | label a favorable variance
unfavorable | Adverse against the specified comparison or objective. | explain an unfavorable variance
price effect | The portion of a movement attributed to selling-price changes. | separate the price effect
volume effect | The portion attributed to a change in quantities. | estimate the volume effect
mix effect | The impact of a change in the composition of sales or activity. | analyze the product-mix effect
rate effect | The portion attributed to a change in a cost or other unit rate. | separate rate from volume
recurring | Expected to arise repeatedly under the relevant conditions. | identify recurring costs
one-off | An item described as unusual or nonrecurring, subject to support. | challenge a one-off classification
run rate | A projected pace based on selected current activity. | qualify the implied run rate
materiality | Significance assessed in context, not solely by an arbitrary percentage. | assess quantitative and qualitative materiality
assumption | An input or premise used without treating it as an established outcome. | state the underlying assumption
operating margin | Operating profit divided by revenue on the specified basis. | explain operating-margin movement
percentage point | One unit of difference between percentage values. | report a percentage-point change
basis point | One hundredth of a percentage point. | express a movement in basis points
like-for-like | Compared on a sufficiently consistent scope and basis. | establish a like-for-like comparison
management commentary | Explanation accompanying reported financial information. | sharpen management commentary''',
    precision='Revenue is 5% above budget: $50,000 divided by $1,000,000. Operating profit is 2% below budget: a $4,000 decline from $200,000 to $196,000. The percentages use different denominators and must not be subtracted to explain profit.',
    precision_extra='Freight and agency labor explain where the $54,000 cost increase sits. They do not, by themselves, establish whether higher rates, greater activity, or a temporary issue caused it. A category bridge and a causal explanation are related but different.',
    phrases='''Lead with the contrast | Revenue is above budget, but operating profit is below it.
Name the offset | The $54,000 cost increase more than offsets the $50,000 revenue increase.
State the basis | These figures cover the same month, currency, and reporting scope.
Quantify the result | Operating profit is $196,000, which is $4,000 below budget.
Locate the movement | Freight and agency labor account for the identified cost increase.
Preserve uncertainty | The rate-versus-volume split remains under review.
Avoid extrapolation | We have not established that either increase is recurring.
Close with a check | I will validate the drivers before changing the forward estimate.
Clarify a comparison | Are you asking about budget, last year, or the previous forecast?
Correct a unit | That is a percentage-point change, not a percentage change.
Explain a denominator | The 2% decline is measured against budgeted operating profit.
Challenge a label | What supports calling that item one-off?
Limit causation | The category totals locate the increase but do not yet explain its cause.
Separate margins | A higher revenue total does not guarantee a higher operating margin.
Keep a caveat useful | The open question is recurrence, not whether the recorded increase exists.
Offer a concise account | Sales gained $50,000; operating costs rose by $54,000 against budget.''',
    notes='''Above and below | Attach the comparator: above budget is incomplete if the audience might assume above last year.
More than offset | This phrase means the opposing movement is larger, explaining why the final result changes direction.
Percent versus points | A move from 10% to 12% is two percentage points, or a 20% relative increase.
Account for | The phrase can identify a numerical contribution without establishing an underlying operational cause.
Recurrence language | "May recur" is not the same as "is recurring"; the forecast needs a supported assumption.
On the same basis | Use this only after checking period, currency, scope, and relevant measurement definitions.''',
    d='''Which sentence correctly explains the profit movement? | Costs rose $54,000, exceeding the $50,000 revenue gain by $4,000. | Revenue rose 5%, so profit must rise 5%. | Profit fell because 5 minus 2 equals 3. | Costs fell $54,000 and therefore reduced profit. | The dollar bridge reconciles the $4,000 profit shortfall without mixing percentages with different bases.
Which expression accurately describes the revenue comparison? | Five percent above the month's budget | Five percentage points of revenue earned | Five percent above last year | Five dollars above the prior forecast | The $50,000 increase is 5% of the $1,000,000 monthly budget, not a different period or unit.
Which statement preserves the unresolved cause? | The categories are verified; rate and volume effects are not yet separated. | The entire increase is proven to be wage inflation. | Freight costs are conclusively nonrecurring. | The mix effect explains all agency labor. | Only the categories are established; attributing specific causes would go beyond the stated review.
Which question most directly tests the one-off label? | Which costs relate to the disruption, and will those conditions continue next month? | Which cost center owns the freight account? | Has the invoice been paid by month-end? | Do the two cost categories reconcile to $54,000? | Nonrecurrence depends on the cause and its expected persistence. Ownership, payment and the already verified category total do not settle whether the cost will recur.''',
    dialogue='''Amir | The opening slide says revenue is five percent ahead, yet operating profit is two percent behind. Give me the connection before we list every account in the ledger.
Lena | The [[offset::An offset counteracts another movement; here the cost increase exceeds the revenue gain and reduces profit.]] is operating cost. Revenue gained fifty thousand dollars against budget, while costs rose fifty-four thousand, leaving profit four thousand below plan.
Amir | Good. Make sure ahead means ahead of this month's budget. Someone reading the slide quickly could assume the five percent is a year-on-year growth figure.
Lena | I will name the [[comparator::The comparator is the reference used for the measurement, here the same month's budget rather than last year.]] in the headline. Actual profit is one hundred ninety-six thousand dollars against two hundred thousand budgeted, using the same reporting scope.
Amir | Which accounts explain the extra fifty-four thousand? Start with what you've verified, then tell me which causes still need checking.
Lena | Freight contributes thirty thousand and agency labor twenty-four thousand. Those categories explain the [[variance::Variance is the difference from the stated reference; the two verified category amounts reconcile the total cost increase.]], but I have not yet separated rate and volume effects.
Amir | That distinction matters. More sales could require more activity, and a higher unit rate could also contribute. We should not call the entire increase inflation.
Lena | Agreed. The [[volume effect::The volume effect relates to changed quantities or activity; it must be separated from unit-rate changes before attributing the increase.]] needs the underlying quantity records. I will compare those with the rates rather than infer the cause from the account name.
Amir | A colleague wants both increases labeled one-off because a supplier problem occurred this month. Does that event establish that the full amounts will disappear next month?
Lena | No. The [[one-off::One-off claims nonrecurrence; one unusual event does not establish that all costs in the categories will disappear.]] description needs support. We must identify which costs relate to the event and whether the conditions causing them will continue.
Amir | Then don't call it temporary yet. What carries into next month's forecast, and what are you still asking Operations to confirm?
Lena | I will not roll the full amount into a new [[run rate::A run rate projects a pace from selected activity; untested recurrence makes automatic extrapolation unreliable.]] or remove it automatically. The current actuals are known; the expected future pattern remains an analytical question.
Amir | What about operating margin? Revenue growth alone sounds encouraging, but the profit result suggests we should avoid describing the overall performance as uniformly favorable.
Lena | Yes. [[Operating margin::Operating margin relates operating profit to revenue; it can decline even when the revenue amount increases.]] uses profit divided by revenue. We should distinguish that ratio from the two percent decline in the profit amount against budget.
Amir | In a short update, would you say the problem is immaterial because the profit shortfall is only two percent? I do not want a casual label to close the discussion.
Lena | No. [[Materiality::Materiality depends on context and qualitative factors as well as size; a single percentage does not settle significance.]] requires context, including any decision or reporting implications. The small percentage alone does not establish that the matter can be ignored.
Amir | Give me the final two sentences, with the open question intact. The meeting needs the result and the next analytical step, not every intermediate calculation.
Lena | Revenue is five percent above budget, but higher costs more than offset the gain. We are validating the [[drivers::Drivers explain the contributing factors; rate, volume, and recurrence checks turn category totals into a more useful causal account.]] and recurrence of the freight and agency-labor increases before revising expectations.
Amir | That works. Keep the dollar bridge available for follow-up, and ensure the period and currency remain visible when the slide is copied into the executive pack.
Lena | I will preserve the [[basis::The basis identifies the period, currency, scope, and definitions that make the figures comparable and interpretable.]] and retain the unresolved checks in the commentary. The shortened version will not turn a verified category movement into a verified cause.''',
    transfer_title='Margin up, revenue flat',
    transfer_setup='Revenue is unchanged at $500,000. Operating profit rises from $50,000 to $60,000 because costs fall by $10,000. Both periods use the same scope and accounting basis.',
    transfer='''Analyst: "The dollar gain comes from lower ___, not higher sales." | costs | Unchanged revenue and a $10,000 cost reduction explain the $10,000 increase in operating profit.
Director: "The margin rises from 10% to 12%, a two-percentage-point ___." | increase | The difference between the two margin percentages is two percentage points, not a two percent relative change.
Analyst: "I will keep the revenue ___ unchanged in the comparison." | denominator | Each margin divides profit by the same $500,000 revenue, making the ratio comparison consistent.
Director: "Confirm whether the savings recur before changing the ___." | forecast | A historical cost reduction does not automatically establish the future pattern used in a forecast.''',
    rehearsal=["Read Amir and Lena's corrected exchange. Give the $50,000 revenue gain, $54,000 cost increase and $4,000 profit shortfall without subtracting the two percentages.","Switch roles. Stress the unresolved rate, volume and recurrence checks; do not relabel the whole increase as inflation or one-off.","Read the corrected transfer twice. Keep the 10%-to-12% margin change as two percentage points, with revenue unchanged."]))

BOOK['units'].append(unit(
    title='Financial Statements, Close, and Accounting Judgments', scene='December service, January invoice, January payment',
    skill='Clarify the reporting question and separate service timing, recognition, posting, and cash payment.',
    brief='A supplier performed a December maintenance service. The $12,000 invoice was dated 5 January and paid on 20 January. The approved policy for this fictional case expenses this type of service when received. Before confirming the December entry, accounting must verify completion and check whether an accrual was already posted. Sofia, an accountant, and Chen, the controller, are reviewing the close schedule. No new journal entry has been approved.',
    cast='Sofia | Accountant\nChen | Controller',
    culture=('Clarify which date answers the question', 'A colleague asking "Which month?" may mean the expense period, invoice date, payment month, or posting period. Name the purpose of the schedule before choosing a date. Precision about accounting judgments is more useful than confident repetition of a familiar rule.'),
    a='''In which month did the cash payment occur? | January | December | February | The payment date is unknown | The invoice was paid on 20 January; that cash date is distinct from service delivery and expense recognition.
What checks are required before the December entry is confirmed? | Service completion and whether an accrual already exists | Invoice approval and the bank payment date alone | Supplier identity and the January cash forecast alone | Whether the invoice amount equals the draft journal alone | Completion evidence supports the stated expense policy; checking prior accruals prevents duplication. Payment, identity and matching amounts do not establish both points.
What entry has been approved? | No new journal entry | An automatic second $12,000 expense | A reversal of every December balance | A transfer to share capital | The briefing explicitly leaves the new entry unapproved pending the specified accounting checks.''',
    vocabulary='''income statement | A report of income and expenses over a stated period. | review the income statement
balance sheet | A statement of assets, liabilities, and equity at a stated date. | reconcile a balance-sheet account
cash flow statement | A report of cash movements classified under the relevant framework. | explain the cash flow statement
reporting period | The interval covered by a financial report. | identify the reporting period
period-end close | Procedures used to finalize records for a reporting period. | complete the period-end close
cutoff | Assignment of transactions to the appropriate accounting period. | test transaction cutoff
recognition | Recording an item in financial statements when relevant criteria are met. | assess expense recognition
accrual | Recognition of income or expense before related cash is received or paid. | review the expense accrual
accrued liability | A recorded obligation for an incurred cost not yet settled. | substantiate an accrued liability
accounts payable | Amounts owed to suppliers for goods or services received. | reconcile accounts payable
prepayment | Payment recorded before the related expense is recognized. | release a prepayment to expense
deferred revenue | Amount recorded as a liability before related revenue is recognized. | analyze deferred revenue
journal entry | A recorded set of debits and credits. | approve a journal entry
general ledger | The central record of financial accounts and postings. | inspect the general ledger
subledger | Detailed records supporting a general-ledger account. | reconcile the subledger
posting date | The date used to record an entry in a system. | verify the posting date
reversing entry | An entry that offsets an earlier entry under the relevant process. | check the reversing entry
true-up | An adjustment aligning an estimate with updated support. | calculate the required true-up
supporting schedule | A detailed record explaining a reported balance. | maintain the supporting schedule
account reconciliation | Comparison and explanation of records supporting an account balance. | complete the account reconciliation
accounting estimate | An amount measured using judgment and available information. | document an accounting estimate
accounting policy | The principles and methods used for a class of transactions. | apply the approved accounting policy
capitalization | Recording qualifying expenditure as an asset rather than an immediate expense. | assess capitalization criteria
audit trail | Records that allow a transaction and its approvals to be traced. | preserve the audit trail''',
    precision='Under the expressly stated case policy, December service receipt is relevant to the expense period. January payment belongs to January cash reporting. The invoice date alone does not answer both questions, and an existing accrual must be checked before another expense is posted.',
    precision_extra='A journal can balance mathematically and still be wrong in period, account, amount, or support. Approval of an entry and confirmation of service completion are different controls. Follow the applicable framework and policy for actual transactions, not this fictional example alone.',
    phrases='''Clarify the schedule | Are we showing expense recognition or the cash payment date?
State the sequence | Service was in December; invoicing and payment occurred in January.
Apply the case policy | The stated policy expenses this service when received.
Request support | Please provide evidence that the December service was completed.
Check duplication | Was a December accrual already recorded for this supplier?
Limit approval | The new entry is not approved until the supporting checks are complete.
Separate records | The invoice date and reporting period need not answer the same question.
Close the review | I will reconcile the existing balance before proposing an adjustment.
Trace the amount | Which schedule supports the $12,000 balance?
Check a reversal | Has the earlier accrual reversed, and in which posting period?
Name the adjustment | Is this a new expense or a true-up of an existing estimate?
Preserve evidence | Link the service confirmation and invoice to the journal support.
Avoid a shortcut | Payment timing alone does not determine expense recognition here.
Specify the account | Which ledger account contains the original accrual?
Keep status clear | Prepared for review is not the same as approved for posting.
Confirm the handoff | The remaining checks are completion evidence and the existing accrual.''',
    notes='''Occurred versus posted | A service occurs on operational dates; an entry is posted to accounting records. Do not merge those events.
Already and yet | "Already accrued" tests duplication, while "not yet approved" states the current authorization limit.
Which month for what | Pair every date with its purpose: service month, invoice date, cash date, or reporting period.
Under the policy | This phrase ties the treatment to the stated case rule instead of asserting a universal accounting result.
Before posting | A before-clause makes the required sequence explicit: verify the support before posting an adjustment.
Estimate versus actual | A true-up may reconcile a previous estimate with better information; it is not automatically an additional full expense.''',
    d='''Which question best clarifies the ambiguous month request? | Do you mean the expense period or the payment month? | Do you prefer December because it looks better? | Can we use whichever date is latest? | Should every schedule show January? | The correct question identifies the two distinct reporting purposes before selecting a date.
Which statement follows the case facts? | Cash was paid in January; the expense-period check uses the service facts and policy. | Cash was paid in December because service occurred then. | The invoice date proves no accrual exists. | Payment automatically authorizes a second expense. | It preserves the known cash date and the separate policy-based accounting review.
Which check most directly helps prevent duplicate expense recognition? | Trace the existing accrual and any reversal in the ledger | Confirm that the invoice total includes all services | Match the January payment to the bank statement | Verify the supplier address against its master record | A prior accrual may already recognize the cost. Invoice completeness, payment matching and supplier details can matter, but do not establish whether that expense was already posted.
Which phrase accurately describes the proposed journal? | Prepared for review, not approved for posting | Fully authorized because it balances | Irrelevant because the supplier was paid | Automatically capitalized by the invoice date | The required supporting checks and approval remain incomplete even if a draft journal is mathematically balanced.''',
    dialogue='''Sofia | I'm stuck on the month field in the close schedule. Maintenance was in December, but the twelve-thousand-dollar invoice arrived January fifth and we paid it January twentieth.
Chen | Which schedule are you completing: cash payments or [[expense recognition::Expense recognition records the cost in the relevant reporting period; it is not determined solely by when cash is paid.]]? The invoice date will not answer both questions, so let's fix that heading first.
Sofia | It's the December expense review. Our policy expenses this maintenance when received. Operations says the work finished then; the service confirmation is still on its way.
Chen | Leave the [[cutoff::Cutoff assigns a transaction to the proper accounting period; completion evidence helps apply the stated service-receipt policy.]] check open until that confirmation arrives. We need evidence of December completion, not just the January invoice describing the job.
Sofia | There's also a supplier estimate on the December support schedule. I haven't found its posting reference. Should I prepare another twelve-thousand-dollar expense now?
Chen | Not before you trace the [[accrual::An accrual may already recognize the service cost before payment; checking it prevents recording the same expense twice.]]. We could recognize the same service twice. Find the existing entry and its amount, rather than assuming the schedule proves a posting.
Sofia | The spreadsheet has a prepared date and an approver column. Neither gives me a journal number. I'll search by supplier and document reference next.
Chen | Use the [[general ledger::The general ledger records postings; a supporting estimate does not by itself establish that an entry was posted.]] history as well. A prepared estimate is not necessarily a posted expense; attach the record that establishes what actually went through.
Sofia | If I find it, do you want the January history too? An automatic reversal could explain why the current balance looks different from December's closing schedule.
Chen | Yes, trace any [[reversing entry::A reversing entry offsets an earlier entry; its timing affects how the later invoice should be reconciled.]] and its posting period. Don't assume it ran just because that is the usual setup; we need this transaction's history.
Sofia | I can already confirm the bank payment on January twentieth. I'll keep that on the cash schedule even while the December expense review remains open.
Chen | Keep that [[cash flow::Cash flow concerns actual cash movements; January payment remains distinct from the accounting period of the expense.]] date. We are reconciling the expense treatment, not changing when the money left the bank to make two schedules look alike.
Sofia | And if the December estimate differs from twelve thousand? I'll compare the amounts against the completed service and invoice before proposing the remaining adjustment.
Chen | Bring me the proposed [[true-up::A true-up aligns an estimate with updated evidence; it is not automatically a second full recognition of the cost.]] with that comparison. Don't enter the full invoice amount again simply because the final document differs from the estimate.
Sofia | The draft balances, but I'll leave it unposted. Its status will say service confirmation and prior-posting check pending, with no new entry approved.
Chen | Good. Equal debits and credits don't establish that a [[journal entry::A journal entry can have equal debits and credits while still using an incorrect period, account, amount, or unsupported basis.]] uses the correct account, amount or period. Those checks still need their own evidence.
Sofia | I'll link the invoice, completion record when received, posting reference and any reversal. You'll be able to follow the sequence from the original estimate onward.
Chen | Include the payment reference in that [[audit trail::An audit trail connects the transaction, evidence, entries, and approvals so another reviewer can trace the decision.]] too. It supports settlement in January, while the service and posting records support our separate expense-period review.
Sofia | So my update is: December service, January payment, completion evidence awaited and prior accrual still being traced. I'll bring back the supported treatment for your review.
Chen | That's the [[handoff::The handoff identifies known timing, applicable policy, unfinished checks, and the unapproved entry rather than falsely announcing a completed close.]] I need. Keep the open checks visible, and do not post a new adjustment until the evidence and approval are complete.''',
    transfer_title='A paid subscription covers future service',
    transfer_setup='A company pays $6,000 in December for service covering January through June. In this fictional case, the approved policy records a prepayment and releases $1,000 per service month. The payment is confirmed.',
    transfer='''Accountant: "December payment creates a ___ under the stated policy." | prepayment | The case policy treats the advance payment as an asset before the future service months are expensed.
Controller: "The service period begins in ___." | January | January is the first month covered, despite the earlier December cash payment.
Accountant: "The monthly release is $1,000, supported by the ___." | schedule | The six-month schedule allocates the stated $6,000 according to the expressly supplied case policy.
Controller: "Keep the cash date distinct from expense ___." | recognition | Cash payment and recording the expense have different timing under this case's advance-payment policy.''',
    rehearsal=["Read the corrected exchange with separate emphasis on December service and January payment. Keep the completion evidence and prior accrual checks open.","Switch roles. Read the request for ledger and reversal history; do not replace a prepared estimate with a claim that an entry was posted.","Read the corrected subscription transfer. Keep December cash payment, January service start and $1,000 monthly expense release distinct."]))

BOOK['units'].append(unit(
    title='FP&A, Budgeting, Forecasting, and Variance Analysis', scene='A forecast bridge with an unexplained remainder',
    skill='Present a reconciled forecast update and distinguish quantified drivers from unresolved residuals.',
    brief='The annual spending budget for a service line is $100,000. The latest full-year forecast is $120,000, including actual spending to date and estimated remaining spending. A new supplier fee explains $15,000 of the forecast increase. The remaining $5,000 is not yet attributed. Mei, a financial planning and analysis analyst, is preparing a bridge for Rafael, the business lead. No budget increase or savings action has been approved.',
    cast='Mei | Financial planning and analysis analyst\nRafael | Business lead',
    culture=('A forecast is an estimate, not a permission slip', 'Business discussions often mix an updated estimate with a request to spend more. Report the forecast honestly even when it exceeds the budget, then identify the approval or management action as a separate decision. Do not fill an unexplained residual with a plausible-sounding label.'),
    a='''How far is the full-year forecast above budget? | $20,000 | $15,000 | $5,000 | $120,000 | The $120,000 forecast minus the $100,000 budget gives a $20,000 unfavorable spending variance.
How much remains unattributed? | $5,000 | $20,000 | $15,000 | Nothing | The supplier fee explains $15,000 of the $20,000 increase, leaving $5,000 for investigation.
What does the new forecast authorize? | No budget increase or savings action by itself | Automatic spending approval up to $120,000 | A confirmed $5,000 saving | Removal of the supplier fee | A forecast estimates expected performance; the briefing expressly leaves budget and action approvals incomplete.''',
    vocabulary='''FP&A | Financial planning and analysis, connecting forecasts and business decisions. | prepare an FP&A update
budget | An approved financial plan for a specified period and scope. | retain the approved budget
forecast | An updated estimate of expected performance using stated assumptions. | refresh the full-year forecast
actuals | Recorded results for completed periods on the stated basis. | load the latest actuals
year to date | The elapsed part of a financial or calendar year. | reconcile year-to-date spending
full year | The complete annual period used for planning or reporting. | present the full-year outlook
remaining-year estimate | Expected performance for the uncompleted portion of the year. | update the remaining-year estimate
rolling forecast | A forecast extended regularly over a moving future horizon. | maintain a rolling forecast
reforecast | An updated forecast replacing an earlier estimate. | explain the reforecast changes
baseline | A defined starting reference for comparison or modeling. | lock the comparison baseline
bridge | A reconciliation from one financial amount to another through identified movements. | reconcile the forecast bridge
waterfall | A chart showing sequential contributions from a starting value to an ending value. | label the waterfall clearly
residual | The amount left after identified components are deducted. | investigate the unexplained residual
plug | A balancing amount calculated to make a model reconcile; it needs an explicit basis and label. | avoid an unsupported plug
cost center | An organizational unit used to collect or control costs. | verify the cost-center allocation
cost allocation | Assignment of costs to units or activities using a stated method. | review the allocation basis
commitment | An obligation or planned expenditure with status requiring clarification. | distinguish commitments from actuals
purchase order | An authorized order for specified goods or services. | check the purchase-order amount
phasing | Distribution of an amount across periods. | revise monthly phasing
timing variance | A difference caused by an item occurring in a different period. | isolate a timing variance
structural variance | A difference reflecting an underlying change rather than timing alone. | assess a structural variance
contingency | A provision in a plan for specified uncertainty or risk. | explain the contingency assumption
scenario | A coherent set of assumptions and resulting outcomes. | compare downside and base scenarios
forecast bias | A systematic tendency to overestimate or underestimate outcomes. | examine forecast bias''',
    precision='The bridge is $100,000 budget plus $15,000 identified supplier fee plus $5,000 unexplained increase, giving $120,000 forecast. The last amount is a residual, not a verified operational driver. Label it openly instead of inventing a cause.',
    precision_extra='Actuals to date and estimated remaining spending make up the full-year forecast, but they have different evidential status. Moving spending between months changes phasing; it does not necessarily reduce the full-year total. A forecast update does not amend the approved budget.',
    phrases='''Lead with the outlook | Full-year spending is forecast at $120,000 against a $100,000 budget.
Quantify the bridge | The $20,000 increase includes a verified $15,000 supplier fee.
Name the residual | The remaining $5,000 has not yet been attributed.
Separate actual and estimate | The total combines recorded actuals with a remaining-year estimate.
Avoid a plug | I will keep the residual visible rather than assign an unsupported cause.
Distinguish authority | The updated forecast does not approve additional spending.
Test phasing | Is this a shift between months or a change to the full-year total?
Close the update | The next review will identify the residual's source and any proposed action.
Define the baseline | The comparison remains the approved $100,000 annual budget.
Challenge a saving | What action and evidence support that reduction?
Check commitments | Does the estimate include the open purchase order?
Separate possibility | That is a scenario, not the current approved operating plan.
Prevent double counting | Has the supplier fee already been included in the remaining-year estimate?
Clarify ownership | Which cost-center owner can verify the allocation?
Preserve uncertainty | The bridge reconciles arithmetically, but one driver remains unresolved.
Describe approval | Any budget revision requires a separate decision.''',
    notes='''Forecast to be | This construction describes an estimate; "has spent" describes actual expenditure already incurred.
Explained versus reconciled | A bridge may add up while still containing an unexplained residual. State which sense of complete you mean.
Of that | "Fifteen thousand of that increase" links a component to the total and avoids treating it as an additional amount.
Until verified | Keep a tentative cause explicitly tentative until the relevant records support it.
Timing versus total | "Later this year" changes phasing; "next year" may change the current full-year figure and needs separate review.
Decision language | Estimated, requested, budgeted, and approved describe different financial states.''',
    d='''Which update keeps the residual honest? | The fee explains $15,000; $5,000 remains unattributed. | The supplier fee explains the entire $20,000. | A confirmed efficiency saving offsets the residual. | The remaining $5,000 is definitely inflation. | Only $15,000 has an identified driver, so attributing the balance invents evidence.
Which description fits the $120,000 figure? | Full-year forecast including actuals and estimated remaining spending | Actual cash already paid | A newly approved budget | A guaranteed year-end result | The briefing defines the figure as an estimate combining completed and future periods, not cash or authorization.
Which question distinguishes phasing from a real annual change? | Will the cost still occur within the same full year? | Will the invoice use the same purchase-order number? | Will a different cost center review the payment? | Will the payment be included in the next monthly cash forecast? | Moving a cost within the same year can change monthly timing without reducing its annual amount. The document reference, reviewer and forecast inclusion do not settle that annual effect.
Which sentence preserves budget authority? | The forecast is updated; the approved budget remains $100,000. | The forecast automatically raises the budget. | An unexplained residual authorizes an exception. | Every predicted cost is an approved commitment. | Forecasting expected expenditure and authorizing a budget change are separate processes.''',
    dialogue='''Rafael | The full-year spending outlook is one hundred twenty thousand dollars. Is that a new budget request, or are you telling me the expected result has changed?
Mei | It is the latest [[forecast::A forecast estimates the expected result; it does not itself request or authorize a revised spending limit.]]. The approved budget remains one hundred thousand, and no additional spending approval follows automatically from updating the estimate.
Rafael | Explain the twenty-thousand-dollar increase. The supplier added a fee, but the note mentions only fifteen thousand, not the complete movement.
Mei | The [[bridge::A bridge reconciles a starting amount to an ending amount through components, including any explicitly unresolved balance.]] starts at the budget, adds fifteen thousand for the fee, and shows five thousand still unattributed. It reaches one hundred twenty thousand without hiding that gap.
Rafael | Could the remainder be inflation? That would make a simple explanation for the review meeting, although I have not seen a rate calculation supporting it.
Mei | It could have several causes, but the [[residual::The residual is the amount not explained by identified components; it should not receive a causal label without evidence.]] is not evidence of inflation. I will check the records instead of assigning the most convenient label.
Rafael | Please also confirm whether the supplier fee has been counted twice. The cost-center owner may have included it in the amount submitted for the rest of the year.
Mei | I will compare that submission with the [[remaining-year estimate::The remaining-year estimate covers future spending; checking its contents helps prevent adding the same supplier fee twice.]] and its assumptions. A separate bridge line must explain the change, not duplicate a cost already included in the forecast.
Rafael | The total includes spending already recorded as well as future estimates, correct? I want the meeting pack to distinguish evidence from assumptions rather than treating every dollar alike.
Mei | Correct. We have [[actuals::Actuals are recorded results for elapsed periods, unlike estimates for the remaining period in the full-year forecast.]] for completed periods, then estimated spending for the balance of the year. I will make that composition visible in the supporting schedule.
Rafael | A project manager says moving a payment from October to November saves money in October. Is that enough to reduce the full-year forecast we are discussing?
Mei | Not by itself. That may change [[phasing::Phasing distributes an amount across periods; moving it within the same year does not necessarily reduce the annual total.]], while leaving the annual total unchanged. We need to know whether the cost disappears, shifts, or changes in amount.
Rafael | And please keep the savings target separate. Nobody has confirmed an action that delivers it yet; I don't want it quietly balancing the forecast.
Mei | I will keep an unsupported [[plug::Here the plug would be an unsupported balancing reduction. An unconfirmed savings target cannot be presented as a verified cost saving.]] out of the estimate. Any proposed saving needs an identified action, timing, amount, and appropriate review of whether it belongs in the forecast.
Rafael | When you update the file, can you show exactly what changed? I need to explain the next version without rebuilding the whole bridge.
Mei | Retain the approved budget as the [[baseline::The baseline is the defined comparison reference; retaining it makes successive explanations of the forecast movement traceable.]]. I will document changes to the forecast separately, including any corrected allocation or duplicate discovered in the supporting records.
Rafael | If the fee persists next year, distinguish that ongoing change from a cost arriving a month earlier than expected.
Mei | Yes. A [[structural variance::A structural variance reflects an underlying change rather than a timing shift; recurrence needs evidence before informing the next plan.]] affects the underlying spending pattern. We should test that interpretation rather than infer permanence from one invoice or one forecast update.
Rafael | For now, the message is twenty thousand above budget, fifteen thousand explained, five thousand under review, and no new spending authority. Is anything important missing?
Mei | Add that this is a full-year estimate, not an assured outcome. I will return with the [[attribution::Attribution assigns the movement to supported sources; completing it explains the residual rather than merely making the arithmetic balance.]] of the residual and any proposed management action, keeping the approval decision separate.''',
    transfer_title='A delayed purchase is not a canceled purchase',
    transfer_setup='A $9,000 purchase moves from March to April within the same financial year. Its amount is unchanged, and the approved full-year plan still includes it. No cancellation is authorized.',
    transfer='''Analyst: "The move changes monthly ___, not the annual amount." | phasing | The purchase moves between months in the same year without changing its stated cost.
Manager: "Do not describe the March reduction as a confirmed ___." | saving | The purchase remains in the plan, so lower March spending does not establish an annual saving.
Analyst: "The full-year ___ still includes $9,000." | forecast | The unchanged purchase remains expected within the year and therefore belongs in the full-year estimate.
Manager: "Retain the purchase's approval and timing ___." | record | A traceable record preserves what changed and avoids implying that the purchase was canceled.''',
    rehearsal=["Read Mei and Rafael's corrected bridge: $100,000 budget, $15,000 identified fee and $5,000 unexplained increase, totaling $120,000 forecast.","Switch roles. Stress the difference between a reconciled total and an explained driver, and between forecast and spending authority.","Read the corrected transfer twice. Move the $9,000 purchase from March to April without calling it an annual saving."]))

BOOK['units'].append(unit(
    title='Treasury, Cash, Liquidity, Working Capital, and FX', scene='Friday cash depends on an unconfirmed receipt',
    skill='Explain conditional liquidity, test a delayed-receipt case, and distinguish available funds from unverified facilities.',
    brief='Friday begins with $80,000 of available cash. Scheduled outflows total $100,000. The base forecast includes a $50,000 customer receipt on Friday, but the customer has not confirmed payment. Without that receipt, the calculation shows a $20,000 shortfall; with it, closing cash is $30,000. Inez, the treasury analyst, and Paul, the finance manager, are reviewing the position. A credit facility exists, but its undrawn availability and draw conditions have not been verified. No payment deferral or facility draw is approved.',
    cast='Inez | Treasury analyst\nPaul | Finance manager',
    culture=('State the dependency before the reassuring total', 'A cash number can sound certain even when it depends on an unconfirmed receipt. Attach the condition to the balance itself, then explain the delayed-receipt case and the authorized next checks. A forecast is useful precisely because it reveals dependencies early.'),
    a='''What is forecast closing cash if the receipt arrives as assumed? | $30,000 | $130,000 | $50,000 | $20,000 | Opening cash of $80,000 plus the $50,000 receipt less $100,000 of outflows gives $30,000.
What happens in the stated no-receipt calculation? | A $20,000 shortfall | A $20,000 surplus | A confirmed facility draw | Automatic cancellation of outflows | Without the receipt, $80,000 minus $100,000 is negative $20,000; no mitigation is approved.
What has not been verified about the facility? | Undrawn availability and draw conditions | Whether any facility exists | The opening cash amount | The scheduled outflow total | The briefing confirms existence only, not usable availability or satisfaction of drawing conditions.''',
    vocabulary='''treasury | Management of cash, funding, and related financial risks. | prepare a treasury update
liquidity | Ability to meet obligations when due using accessible resources. | assess the liquidity position
available cash | Cash accessible for the stated purpose under relevant restrictions. | confirm available cash
restricted cash | Cash subject to limits on access or use. | separate restricted cash
cash inflow | A receipt of cash during a period. | verify an expected cash inflow
cash outflow | A payment or other movement of cash out of the entity. | schedule the cash outflows
cash forecast | An estimate of future receipts, payments, and balances. | refresh the short-term cash forecast
cash shortfall | A gap between available cash and the cash needed. | quantify the cash shortfall
cash buffer | Cash retained as protection against uncertainty or needs. | assess the required cash buffer
working capital | Current assets less current liabilities; operational variants require definition. | define the working-capital measure
receivables | Amounts due from customers or other debtors. | monitor overdue receivables
payables | Amounts owed to suppliers or other creditors. | review scheduled payables
DSO | Days sales outstanding, a measure relating receivables to credit sales. | monitor DSO trends
DPO | Days payable outstanding, a measure relating payables to relevant purchases or costs. | state the DPO calculation basis
cash conversion cycle | A measure combining inventory, collection, and payment timing. | analyze the cash conversion cycle
revolving credit facility | Borrowing that may be drawn and repaid within agreed terms and limits. | verify revolver availability
undrawn availability | A facility amount potentially accessible after applicable limits and conditions. | confirm undrawn availability
drawdown | Borrowing an amount under a facility. | obtain drawdown approval
covenant | A requirement in a financing agreement. | test covenant compliance
headroom | Capacity remaining before a defined limit is reached. | quantify covenant headroom
settlement date | The date a transaction is completed through the relevant exchange of funds or assets. | confirm the settlement date
value date | The date assigned for funds' financial effect under the banking arrangement. | check the payment value date
FX exposure | Sensitivity to movements in foreign-exchange rates. | identify the FX exposure
hedge | A position intended to reduce a specified risk, with its own limits and costs. | evaluate a proposed hedge''',
    precision='The $30,000 closing balance is conditional on receiving $50,000 that day. Without it, the stated arithmetic shows a $20,000 funding gap. A customer promise, a payment instruction, a settlement notice, and available funds are different evidence states.',
    precision_extra='An existing credit facility is not the same as verified cash available now. Limits, covenants, conditions, timing, and approval may affect a draw. Foreign-currency exposure also needs a specified currency and amount; a hedge does not eliminate every risk.',
    phrases='''Attach the condition | Closing cash is forecast at $30,000 if the customer pays Friday.
Name the alternative | Without that receipt, the model shows a $20,000 shortfall.
Separate evidence | The expected receipt is in the model, but payment is not confirmed.
Request confirmation | Please verify the payment status and expected settlement date.
Qualify funding | The facility exists; usable availability is still being checked.
Avoid authorization | No drawdown or payment deferral has been approved.
State the dependency | The base case depends on the customer receipt arriving that day.
Close with ownership | I will confirm the receipt status and route the funding options for approval.
Clarify availability | Is that cash accessible, or is any portion restricted?
Check timing | Does the value date support the assumed availability?
Preserve the downside | Keep the delayed-receipt case beside the base case.
Test a limit | How much headroom remains under the agreement's definition?
Separate profit | Accounting profit does not establish cash available for Friday's payments.
Define currency | What currency and amount does the exposure relate to?
Limit a hedge claim | The proposed hedge addresses a specified exposure, not every financial risk.
Report the decision | We need an authorized funding response, not a more optimistic assumption.''',
    notes='''If, not when | Use if for an unconfirmed event; when can imply that the event is assured.
Available versus expected | Expected receipts are forecast inflows, while available cash is accessible at the stated time.
Would versus will | "Would be $30,000 if..." preserves the condition; an unconditional will can overstate certainty.
Shortfall versus loss | A cash shortfall is a funding gap, not automatically an accounting loss.
Draw versus approve | A possible draw, an approved draw, and received proceeds identify different states.
Currency qualifiers | Do not quote an FX amount without identifying the currency and relevant conversion basis.''',
    d='''Which sentence preserves the receipt condition? | Closing cash is forecast at $30,000 if the $50,000 arrives Friday. | Closing cash is guaranteed at $30,000. | A forecast entry proves the customer paid. | A positive base case eliminates the funding gap. | The conditional sentence keeps the unconfirmed receipt attached to the resulting balance.
Which calculation describes the delayed-receipt case? | $80,000 minus $100,000 equals a $20,000 shortfall. | $80,000 plus $100,000 equals available cash. | $50,000 minus $30,000 proves a surplus. | The facility automatically supplies $20,000. | The case removes only the unconfirmed receipt, leaving a negative $20,000 balance before any approved mitigation.
What must be checked before counting the facility as usable funding? | Current availability, draw conditions, timing and authorization | Only the original commitment amount and expiry date | Only the bank relationship and previous successful draws | Only the forecast deficit and last approved budget | The funding must be usable in the required amount and time, subject to current terms and authority. Historical access and headline limits do not establish a permitted draw now.
Which statement separates cash from profit? | Profit does not itself confirm funds available for the scheduled payments. | Every profitable business has unlimited cash. | All receivables are already bank cash. | Restricted cash is always freely usable. | Profit and cash access measure different things; payment timing and restrictions can still create a liquidity gap.''',
    dialogue='''Paul | The forecast shows thirty thousand dollars at Friday close. Can I tell the operating team that all scheduled payments are covered without a funding decision?
Inez | Only with the receipt condition attached. The [[base case::The base case uses the selected planning assumptions, including the unconfirmed customer receipt; it is not a guaranteed outcome.]] includes fifty thousand from the customer, and that payment has not been confirmed.
Paul | Walk me through the cash arithmetic and the alternative. I need to understand the dependency before the team relies on the closing balance.
Inez | We start with eighty thousand and schedule one hundred thousand in outflows. Without the receipt, there is a twenty-thousand-dollar [[shortfall::The shortfall is the gap between the available $80,000 and the $100,000 scheduled outflows when the receipt is excluded.]]; with it, thirty thousand remains.
Paul | They normally pay on time, but I don't have a confirmation for Friday. Can you check when the funds would actually reach us?
Inez | Exactly. I will request the payment status and [[settlement date::The settlement date concerns transaction completion; confirming it is more informative than assuming a forecasted receipt is already available.]]. A planned payment date and completed settlement may not give us the same evidence.
Paul | Could we simply include the credit facility in available cash? The agreement is on file, and the facility was used earlier in the year.
Inez | Not until we verify [[undrawn availability::Undrawn availability depends on current limits and conditions; past use or an existing agreement does not establish usable funds now.]] and the current draw conditions. An existing agreement is not itself a confirmed source of funds for the required time.
Paul | Please check any notice period too. Even an amount we may borrow could be too late for the particular payment schedule we are trying to cover.
Inez | I will assess the proposed [[drawdown::A drawdown is borrowing under a facility; its amount, conditions, timing, and approval must support the proposed funding use.]] timing and authorization with the responsible team. No borrowing action is approved merely because we have identified a possible gap.
Paul | And do not silently move supplier payments to make the forecast positive. Any deferral could affect contractual commitments and operating relationships.
Inez | Agreed. The scheduled [[outflows::Outflows are planned cash payments; changing their dates requires support and authority rather than a cosmetic forecast adjustment.]] remain as stated unless an authorized change is confirmed. I will show possible responses separately from the current case.
Paul | One more check: is all eighty thousand available to use? I don't want restricted funds included in the opening balance.
Inez | The case identifies it as [[available cash::Available cash is accessible for the relevant purpose; restricted funds should not be silently included in a spendable opening balance.]]. In the working file, I will retain the supporting check and keep any restricted balances separately identified.
Paul | The business lead may ask why this matters when the operation is profitable. We should explain that without suggesting the accounting result is wrong.
Inez | Profit and [[liquidity::Liquidity concerns meeting obligations when due; accounting profit does not establish timely access to funds for the scheduled payments.]] answer different questions. Revenue can be recognized before collection, while suppliers and employees still need payment on their scheduled dates.
Paul | Once the facility terms are checked, include the relevant limit calculation. A quoted borrowing ceiling alone may hide conditions affecting how much we can use.
Inez | I will state the applicable [[headroom::Headroom measures remaining capacity against a defined limit; its calculation must follow the actual agreement rather than a guessed ceiling.]] and its definition, with any unverified conditions visible. We should not invent a covenant result to complete the funding table.
Paul | Then the update should lead with the conditional balance and the delayed-receipt gap, followed by the receipt check and the funding decision still required.
Inez | Yes. I will keep the [[dependency::The dependency is the receipt on which the positive closing balance relies; naming it makes the unresolved funding exposure visible.]] attached to the number and route verified options for approval. An optimistic forecast assumption will not substitute for an authorized response.''',
    transfer_title='A receipt slips to Monday',
    transfer_setup='Friday starts with $40,000 and has $55,000 of scheduled outflows. A $25,000 receipt is now confirmed for Monday, not Friday. No alternative funding or payment change is approved.',
    transfer='''Analyst: "Exclude the Monday receipt from Friday's closing ___." | balance | The later receipt cannot be counted as Friday funds under the stated timing.
Manager: "Friday therefore shows a $15,000 cash ___." | shortfall | Available $40,000 less $55,000 of outflows leaves a $15,000 funding gap.
Analyst: "I will present possible funding options without implying ___." | approval | The case leaves all alternatives unapproved, so identifying an option is not authority to execute it.
Manager: "Keep Monday's receipt and its confirmed ___ in the update." | timing | The receipt still matters to the forecast, but its actual Monday timing must remain explicit.''',
    rehearsal=["Read the corrected cash review. Contrast $30,000 closing cash if the receipt arrives with the $20,000 shortfall if it does not.","Switch roles. Keep facility availability and draw conditions unverified, and any draw or payment deferral unapproved.","Read the corrected transfer. Exclude Monday's $25,000 receipt from Friday; preserve the $15,000 funding gap and the need for an authorized response."]))

BOOK['units'].append(unit(
    title='Markets, Investments, Performance, and Client Communication', scene='A six-percent return without the fee label',
    skill='Present a qualified performance comparison and correct misleading return language.',
    brief='A portfolio earned 6% before fees over the stated twelve-month period. Its selected benchmark returned 5% for that period. A draft client slide says "outperformed by 1%" but omits the portfolio fee basis. The net-of-fees return is not supplied, and the reporting team must verify currency and calculation consistency before approving the comparison. Omar, the performance analyst, and Grace, the client-reporting manager, are revising the slide. No claim about future returns is authorized.',
    cast='Omar | Performance analyst\nGrace | Client-reporting manager',
    culture=('A clear headline needs a fair comparison', 'Clients may reasonably read an unlabeled return as the amount they earned after costs. Put important fee and period information near the number, not only in remote explanatory text. Precision about historical performance is part of clear communication, not an obstacle to it.'),
    a='''What does the 6% measure represent? | The portfolio return before fees for the stated period | A verified net-of-fees client return | A guaranteed next-year return | The benchmark return | The briefing identifies 6% as historical portfolio performance before fees, not net performance or a forecast.
What is the arithmetic difference between 6% and 5%? | One percentage point | One percent of 5% | Six percentage points | Five basis points | Subtracting the two return percentages gives one percentage point, equivalent to 100 basis points.
What is missing before the full comparison can be approved? | Net-return information and the required basis checks | The stated twelve-month period | The existence of a selected benchmark | The fact that the portfolio return is before fees | The case supplies period and gross return but leaves net performance and currency and method consistency unverified.''',
    vocabulary='''portfolio | A collection of investments held or managed together. | review portfolio performance
benchmark | A reference used to evaluate investment performance or exposure. | select an appropriate benchmark
gross return | Return before the specified fees or costs are deducted. | label gross return
net return | Return after the specified fees or costs are accounted for. | verify the net-return basis
total return | A measure combining income and price movement under a stated method. | compare total-return measures
price return | Return from price movement excluding specified income effects. | distinguish price return from total return
annualized return | Return expressed as an equivalent annual rate using a specified method. | explain an annualized return
cumulative return | The total return over the stated multi-period interval. | report cumulative return
time-weighted return | A method designed to reduce the effect of external cash-flow timing. | calculate time-weighted return
money-weighted return | A return measure affected by the size and timing of cash flows. | explain money-weighted return
attribution | Analysis allocating performance to defined contributing factors. | review performance attribution
excess return | Return above or below a stated benchmark on a consistent basis. | quantify historical excess return
volatility | Variability of returns or prices over the measured interval. | state the volatility measure
drawdown | A decline from a previous peak in the specified value series. | assess maximum drawdown
tracking error | Variability of returns relative to a benchmark under a defined method. | measure tracking error
asset allocation | Distribution of investment exposure among asset categories. | explain asset-allocation effects
security selection | Choice of individual investments within the relevant universe. | assess security-selection contribution
yield | An income or valuation-based rate whose meaning depends on its defined type. | specify the yield measure
coupon | The contractual interest payment terms of a bond. | distinguish coupon from yield
maturity | The contractual date when a debt's principal is due, subject to its terms. | identify the maturity date
duration | A bond measure related to timing or rate sensitivity, depending on the type. | specify modified duration
credit spread | A yield difference against a reference, reflecting several risk and market factors. | monitor credit-spread movement
unrealized gain | An increase in the value of a position not yet disposed of. | distinguish unrealized from realized gain
realized gain | A gain recognized on disposal under the stated reporting basis. | report realized gains''',
    precision='Six percent minus five percent is one percentage point, or 100 basis points. Saying "1% higher" is ambiguous and can be read as a relative comparison. The arithmetic difference alone does not establish a fair benchmark comparison without consistent methods and scope.',
    precision_extra='Gross and net returns differ by their stated cost treatment; neither label should be guessed. Income reinvestment, currency, cash flows, period, and benchmark selection also affect interpretation. Historical performance does not guarantee a future result.',
    phrases='''Label the result | The portfolio returned 6% before fees over the stated twelve months.
Correct the unit | The arithmetic difference is one percentage point, not simply "1% higher."
State the gap | The net-of-fees figure has not been supplied.
Check comparability | We need consistent period, currency, and calculation bases.
Clarify the benchmark | Which index and return version are used in this comparison?
Preserve context | Keep the fee label beside the portfolio return.
Limit the claim | This reports historical performance, not an expected future return.
Close with review | I will verify the basis before the client version is approved.
Distinguish measures | Is that a price-return index or a total-return index?
Check cash flows | Does the method account for client contributions and withdrawals consistently?
Avoid a shortcut | A higher headline return does not establish lower risk.
Explain attribution | The report separates allocation and selection effects under its stated method.
Name the yield | Do you mean current yield or yield to maturity?
Separate income | The coupon rate is not the same as the investor's total return.
Qualify a result | The comparison remains provisional while the calculation basis is checked.
Correct a promise | We cannot present last year's outperformance as a guarantee.''',
    notes='''By versus to | Rose by 6% describes a change; rose to 6% describes the resulting level. Name the measure.
Points for differences | Use percentage points or basis points when subtracting quoted percentage returns.
Gross and net qualifiers | Keep the qualifier with the number so copying a headline does not change its apparent meaning.
Over the period | This phrase identifies a realized historical measurement, not a prediction about the next interval.
Equivalent comparisons | Same dates alone do not guarantee matching currency, income treatment, or methodology.
Risk language | Outperformance describes a return comparison; it does not establish suitability or the absence of risk.''',
    d='''Which headline preserves the known fee treatment? | Portfolio return: 6% before fees for the stated twelve months | Client return after all fees: 6% | Guaranteed next-year return: 6% | Net return: 6%, because the gross return is known | The correct headline retains the stated historical period and before-fees basis without inventing net performance.
How should the arithmetic gap be expressed? | One percentage point, or 100 basis points | One basis point | One percent of the benchmark | Six percent above every alternative | The subtraction is 6% minus 5%, producing a one-percentage-point difference, not a one-percent relative increase.
Which check goes beyond simply matching dates? | Verify currency, income treatment and calculation method | Verify the two reports display the same twelve-month label | Confirm both figures appear in the same presentation | Check that both percentages use the same decimal places | A common period does not establish compatible currency, reinvestment or return methods. Consistent formatting can improve readability but cannot make different measures comparable.
Which statement avoids a future-performance promise? | The result describes this historical period, not a guaranteed future outcome. | The same excess return will occur next year. | Past outperformance removes market risk. | Six percent is the client's minimum future return. | Historical observations do not establish a guaranteed future return or eliminate investment risk.''',
    dialogue='''Grace | The slide shows six percent for the portfolio and five percent for the benchmark. It says outperformed by one percent, but I cannot see a fee label.
Omar | The portfolio figure is a [[gross return::Gross return is before specified fees or costs; omitting the label could make readers mistake it for their after-fee result.]]. It is before fees, and the reporting file does not supply the net figure for this version.
Grace | Put that qualification beside the number. A client should not have to search the appendix to discover that the headline is not an after-fee result.
Omar | I will also change the difference to one [[percentage point::A percentage point measures the arithmetic difference between quoted percentages; 6% minus 5% equals one point.]]. Saying one percent can suggest a relative calculation rather than the subtraction of six and five.
Grace | Before we call the result outperformance, are the period and measurement bases aligned? The dates match, but that may not settle currency or income treatment.
Omar | I need to verify the selected [[benchmark::The benchmark is the comparison reference; its specific version and measurement basis matter to a fair performance comparison.]] version and calculation method. Matching dates alone does not make every return series directly comparable.
Grace | Please check whether the index includes reinvested income. A price-only series would answer a different question from a series including both price changes and distributions.
Omar | Agreed. We should identify the [[total return::Total return includes income and price movement under its method; it differs from a price-only measure.]] treatment rather than assume it. The portfolio and reference need compatible descriptions before the client comparison is approved.
Grace | The account also had contributions during the period. We should know whether the performance method is intended to isolate investment results from the timing of those flows.
Omar | I will verify whether this is [[time-weighted return::Time-weighted return aims to reduce external cash-flow timing effects; the method must be identified rather than guessed from the percentage.]] and confirm its calculation. I will not substitute a money-weighted figure without explaining the change in method.
Grace | Once the comparison checks out, what explains the difference? The client will want more than a line saying the manager did well.
Omar | The [[attribution::Attribution allocates performance to specified contributing factors, providing an analysis beyond a favorable headline comparison.]] report can help, provided we use its stated method. We should distinguish allocation and security-selection contributions rather than invent a narrative from the headline.
Grace | A sales colleague suggested saying the portfolio delivered higher returns with no added risk. Is the return comparison enough to support that statement?
Omar | No. It does not establish [[volatility::Volatility measures variability; a higher return alone does not establish that variability or other risks were lower.]] or other risk characteristics. We need the relevant risk measures and limitations before making any comparative risk claim.
Grace | The next slide shows a bond coupon. Please avoid presenting that contractual interest rate as though it were the investor's overall gain over the period.
Omar | Yes. The [[coupon::The coupon describes bond interest terms; total investor return can also reflect price movements, fees, and other factors.]] is not the same as total return. The explanation needs to distinguish income terms from the effect of price movement and other factors.
Grace | If the net figure isn't ready for our review, leave it unavailable and flag the missing calculation. Don't carry six percent into that box.
Omar | I will mark [[net return::Net return incorporates the specified fee or cost treatment; the unavailable figure must not be inferred to equal the gross result.]] as unavailable for review and route the missing calculation to its owner. The client version will follow the required approval process.
Grace | Finally, remove the sentence implying that we will beat the benchmark again. We can describe the past result without offering a promise about the next year.
Omar | I will identify the one-percentage-point arithmetic gap as historical [[excess return::Excess return is relative performance against a benchmark on a consistent basis; a historical result is not a future guarantee.]], subject to the basis checks, and preserve the fee, period, and uncertainty labels in the revised slide.''',
    transfer_title='Two years is not one year',
    transfer_setup='A report shows a 12% cumulative return over two years. It has not supplied an annualized calculation. The editor wants a short headline without changing the reported measure.',
    transfer='''Analyst: "The 12% figure is ___ over two years." | cumulative | Cumulative identifies the total change across the stated two-year interval, not a one-year equivalent.
Editor: "Do not relabel it as an ___ rate." | annualized | Annualization requires an appropriate calculation; changing the label alone changes the meaning incorrectly.
Analyst: "The headline must keep the two-year ___." | period | The interval is essential context for interpreting the magnitude of the reported return.
Editor: "Retain the calculation ___ with the supporting report." | basis | The method and assumptions must remain traceable so the headline can be checked against the reported measure.''',
    rehearsal=["Read the corrected performance review. Keep 6% before fees, 5% benchmark and the one-percentage-point difference attached to their labels.","Switch roles. Stress that net performance and comparison checks are unfinished; do not turn the historical result into a promised return.","Read the corrected transfer twice. Preserve the 12% cumulative return over two years without relabeling it as an annualized rate."]))

BOOK['units'].append(unit(
    title='Banking, Credit, Lending, and Counterparty Risk', scene='A credit review needs current borrower information',
    skill='Request specific financial evidence and explain its effect on a credit review without promising approval.',
    brief='A lender will review a fictional borrower file on Thursday. The file contains audited statements for the prior December year-end but lacks the requested management accounts through 30 June. The team needs a balance sheet, income statement, and supporting debt schedule. Ellis, the credit analyst, asks Morgan, the relationship manager, to obtain them by Wednesday at 3 p.m. for internal preparation. The borrower has not confirmed delivery. No lending decision or exception to the information requirement is approved.',
    cast='Ellis | Credit analyst\nMorgan | Relationship manager',
    culture=('Make the request exact and the consequence proportionate', 'A vague request for "latest financials" often produces the wrong period or document set. Specify the records, reporting date, purpose, and requested time. Explain an incomplete review without turning the missing information into an unsupported default finding or an automatic rejection.'),
    a='''Which information is missing? | Management accounts through 30 June and the requested debt support | All prior-year audited statements | A completed Thursday approval | Evidence that every loan is in default | The existing December statements do not replace the requested current interim information and supporting schedule.
What does Wednesday at 3 p.m. represent? | The requested delivery time for internal preparation | A confirmed borrower promise | A contractual loan maturity | A guaranteed approval time | The analyst requests that time, but the borrower has not confirmed delivery and it is not a lending commitment.
What decision has been approved? | Neither lending approval nor an information exception | Automatic approval if any file arrives | Immediate default classification | Removal of all review requirements | The briefing leaves both the credit decision and any exception to the information requirement unapproved.''',
    vocabulary='''borrower | A party receiving or seeking funds with repayment obligations. | assess the borrower's position
lender | A party providing or considering credit. | clarify the lender's requirements
credit file | Records supporting assessment and administration of credit. | complete the credit file
underwriting | Assessment of risk and terms before accepting an exposure. | support the underwriting review
credit committee | A body reviewing or deciding credit matters within its authority. | prepare the credit-committee pack
management accounts | Internally prepared financial information, not necessarily audited. | request current management accounts
audited statements | Financial statements accompanied by an independent audit opinion. | inspect the audited statements
interim period | A reporting interval shorter than a full financial year. | identify the interim reporting period
debt schedule | A listing of borrowings and relevant terms and balances. | reconcile the debt schedule
debt service | Principal and interest payments due under the relevant obligations. | assess scheduled debt service
DSCR | Debt service coverage ratio, comparing a defined cash-flow measure with debt service. | specify the DSCR definition
leverage ratio | A measure of debt relative to a specified earnings, asset, or equity base. | verify the leverage-ratio basis
LTV | Loan-to-value ratio, comparing the loan with defined collateral value. | assess the LTV ratio
collateral | Assets pledged to support an obligation. | verify the collateral description
security interest | A legal interest in assets securing an obligation, subject to applicable law. | review the security-interest documentation
guarantor | A party undertaking a specified obligation if another party fails to perform. | assess the guarantor's capacity
maturity profile | The distribution of debt repayment dates. | review the maturity profile
refinancing risk | Risk that replacement funding is unavailable or unattractive when needed. | assess refinancing risk
counterparty risk | Risk of loss from another contracting party's failure to perform. | monitor counterparty risk
concentration risk | Risk arising from exposures sharing a borrower, sector, or other dependence. | assess customer concentration risk
probability of default | Estimated likelihood of default under a specified model and horizon. | state the probability-of-default horizon
loss given default | Estimated share of exposure lost if default occurs under stated assumptions. | evaluate loss given default
exposure at default | Estimated amount exposed when default occurs under the defined model. | calculate exposure at default
credit exception | A departure from a credit requirement requiring authorized assessment. | seek approval for a credit exception''',
    precision='Audited December statements and unaudited June management accounts cover different periods and assurance levels. Describe each accurately. Receipt of a file does not establish completeness, reconciliation, reliable ratios, or credit approval.',
    precision_extra='Credit ratios require specified definitions and periods. Collateral or a guarantee may affect risk but does not prove repayment. Missing documents may prevent a complete assessment; they do not by themselves establish default, fraud, or a final credit decision.',
    phrases='''Specify the request | Please obtain management accounts through 30 June.
Name the components | We need the balance sheet, income statement, and supporting debt schedule.
Explain the purpose | These records support Thursday's credit review.
State the requested time | We have requested delivery by Wednesday at 3 p.m. for preparation.
Preserve status | The borrower has not yet confirmed that timing.
Avoid a promise | Document delivery does not guarantee approval.
Clarify the limitation | The current file does not support a complete interim assessment.
Close the request | Please confirm what can be supplied and flag any missing component.
Distinguish assurance | These are management accounts, not audited interim statements.
Check the period | Does the income statement cover the six months ending 30 June?
Define the ratio | Which cash-flow and debt-service definitions are used for DSCR?
Check completeness | Does the schedule include all borrowings and upcoming repayments?
Separate decisions | Any exception requires its own authorized review.
Avoid a default claim | The missing information does not itself establish a default.
Trace support | Please reconcile the debt schedule to the reported balances.
Confirm receipt | We received the file; its completeness review is still pending.''',
    notes='''Through and as of | An income statement covers a period through a date; a balance sheet presents a position as of a date.
Requested versus confirmed | A requested delivery time is not a confirmed commitment from the borrower.
Latest is ambiguous | Name the reporting end date and components instead of relying on the word latest.
Subject to review | Attach review status to receipt acknowledgments so arrival is not mistaken for acceptance of the information.
Ratio qualifiers | State which numerator, denominator, period, and adjustments a credit ratio uses.
No automatic inference | Incomplete means information is missing; it does not necessarily mean inaccurate, fraudulent, or in default.''',
    d='''Which request is most precise for this case? | Send the 30 June balance sheet, six-month income statement and debt schedule. | Send June monthly sales and the latest bank balance. | Send December audited accounts and a projected year-end income statement. | Send the six-month income statement without the position or debt records. | The required pack combines a position at 30 June, performance through that date and borrowing support. The alternatives omit components or substitute a different period or measure.
Which statement accurately describes the requested timing? | Delivery is requested for Wednesday at 3 p.m.; the borrower has not confirmed. | Delivery is guaranteed because the meeting is Thursday. | The loan matures Wednesday at 3 p.m. | Approval is automatic if a message arrives before Thursday. | It separates the internal preparation request from a borrower commitment or a credit decision.
Which label preserves assurance status? | Internally prepared management accounts, audit status not established | Audited because a spreadsheet is signed | Guaranteed accurate because the borrower emailed them | Final credit approval documentation | Management accounts do not acquire independent audit assurance merely through preparation, signature, or receipt.
Which response avoids an unsupported credit conclusion? | The file is incomplete for the requested review; no decision is approved. | Missing June accounts prove default. | December statements guarantee repayment. | Collateral removes every lending risk. | The case supports an information gap, not default, assured repayment, or elimination of risk.''',
    dialogue='''Morgan | The borrower sent December's audited statements again. They believe that completes the request because those are the most recent documents signed by their external auditor.
Ellis | We still need the June [[management accounts::Management accounts provide internally prepared interim information; December audited statements do not replace the requested June period.]]. Specify the reporting date and required components rather than repeating latest financials, which they are interpreting differently.
Morgan | I will ask for the balance sheet as of June thirtieth and the income statement for the six months ending then. What support should accompany them?
Ellis | Include the [[debt schedule::The debt schedule details borrowing balances and terms, supporting assessment beyond the headline statement totals.]], with balances and relevant repayment dates. It should reconcile to the accounts so we can understand the obligations rather than rely on a single total.
Morgan | We requested Wednesday at three for preparation before Thursday's meeting. The borrower has not confirmed whether that timing is possible, so I should not promise the pack is complete.
Ellis | Correct. Keep the [[requested deadline::The requested deadline is an internal preparation need communicated to the borrower, not a confirmed commitment or a loan maturity.]] distinct from confirmed delivery. Ask what they can provide and identify any component that will remain missing.
Morgan | If they send a signed spreadsheet, should I describe the June numbers as audited? The finance director's signature may make the document look more formal.
Ellis | No. [[Audited statements::Audited statements have independent audit assurance; a manager's signature on internal accounts does not create that status.]] have a different assurance status. Name the preparer and the actual review status without upgrading it because the file looks official.
Morgan | The team wants a coverage ratio as soon as the file arrives. But the cash-flow figure covers six months and the debt payments cover a year.
Ellis | Specify the [[DSCR::DSCR compares a defined cash-flow measure with debt service; mixing inconsistent periods can make the ratio misleading.]] definition and period before quoting it. A ratio can look precise while comparing mismatched amounts or omitting required adjustments.
Morgan | We should also see which loans come due soon. A reasonable total debt balance may still hide several repayments concentrated in a short period.
Ellis | That is why the [[maturity profile::The maturity profile shows repayment timing, revealing concentrations that a single total debt balance can conceal.]] matters. Check dates and amounts, and identify any refinancing assumption rather than treating replacement borrowing as already available.
Morgan | One colleague says the pledged property makes the missing accounts unimportant. I can explain that security and repayment capacity are separate parts of the assessment.
Ellis | Exactly. [[Collateral::Collateral supports an obligation but does not establish the borrower's cash generation or eliminate valuation and recovery risk.]] does not replace current financial information. Its value, enforceability, and recovery assumptions also require appropriate review.
Morgan | What happens if the June package cannot arrive before the meeting? I need a clear message that does not sound like automatic rejection or a promise to waive requirements.
Ellis | Report the gap and route any proposed [[credit exception::A credit exception is a departure from a requirement requiring authorized review; it cannot be granted informally to meet a meeting date.]] through the authorized process. Neither the meeting date nor the relationship team's preference approves an exception.
Morgan | I will avoid saying the borrower is in default just because a document is missing. Any contractual reporting issue would need its own assessment against the agreement.
Ellis | Correct. This update concerns an incomplete [[credit file::The credit file holds review evidence; missing information limits the assessment without itself proving default or another adverse conclusion.]], not an approved default determination. Separate the known information gap from legal or credit conclusions still requiring review.
Morgan | I'll request all three components with the June date and Wednesday timing. If they can't deliver, I'll tell you what is missing before Thursday's review.
Ellis | Good. On receipt, acknowledge delivery and begin the [[completeness review::A completeness review checks whether the requested information is present and usable; receiving a file does not itself complete underwriting or approve credit.]]. Keep receipt, validation, committee consideration, and lending authorization as separate statuses in the handoff.''',
    transfer_title='A guarantee does not replace a current assessment',
    transfer_setup='A borrower offers a parent guarantee, but the guarantor financial information and guarantee wording are unreviewed. The credit team has not approved the loan or reliance on the guarantee.',
    transfer='''Manager: "The guarantee is offered, but reliance is not ___." | approved | The case explicitly leaves both the loan and reliance on the guarantee without approval.
Analyst: "We need the guarantor's financial information and the actual ___." | wording | Capacity and the scope of the promised obligation require evidence, not merely the label guarantee.
Manager: "Do not describe the offer as eliminating credit ___." | risk | An unreviewed guarantee does not establish that all default, performance, or recovery risks disappear.
Analyst: "I will route the evidence through the authorized ___." | review | The information must be assessed by the assigned process before reliance or lending decisions are made.''',
    rehearsal=["Read the corrected credit request. Name the June balance sheet, six-month income statement and debt schedule, then Wednesday at 3 p.m. as requested timing.","Switch roles. Keep borrower confirmation, completeness review and credit approval separate; no delivery promise or exception is established.","Read the corrected guarantee transfer twice. Preserve the unreviewed wording and guarantor information, with reliance and lending still unapproved."]))

BOOK['units'].append(unit(
    title='Controls, Audit, Compliance, Fraud, and Ethics', scene='Three unmatched entries that happen to net to zero',
    skill='Hand off unresolved reconciliation items with evidence, ownership, and neutral risk language.',
    brief='Yara is preparing a bank reconciliation for Noah to review. Three bank entries remain unmatched to ledger support: a $1,200 receipt, a $700 payment, and a $500 payment. Their net amount is zero, but their individual causes are unknown. Yara has attached the bank references and a list of records already checked. No correcting entries, fraud conclusion, or reconciliation sign-off is approved. Noah will continue the review after Yara leaves.',
    cast='Yara | Reconciliation preparer\nNoah | Reviewer',
    culture=('A clean total is not a completed control', 'A reviewer may ask why a zero difference remains open. Explain that individual transactions still need support and correct treatment. Keep observations separate from allegations, and preserve the work history so the next person can continue without guessing what was checked.'),
    a='''What is the net of the three unmatched bank entries? | Zero | $2,400 | $1,200 | Minus $1,200 | The $1,200 receipt less payments of $700 and $500 nets to zero, but individual support is still missing.
What remains unknown? | The causes of the three unmatched items | Whether the entries total zero | Whether bank references are attached | Who will continue the review | The case identifies the amounts and handoff owner but leaves the individual causes unresolved.
What can Yara accurately report? | Three unresolved items with attached references and checks performed | A signed-off reconciliation | Confirmed fraud | Approved correcting entries | Only the unresolved status and documented work are supported; conclusions and adjustments remain unapproved.''',
    vocabulary='''internal control | A process intended to provide reasonable assurance about specified objectives. | assess an internal control
control objective | The result a control is designed to support. | identify the control objective
control owner | The person accountable for the assigned control's operation. | confirm the control owner
control evidence | Records supporting that a control was performed and what it found. | retain control evidence
preventive control | A control designed to stop an error or unwanted event before it occurs. | evaluate a preventive control
detective control | A control designed to identify an error or unwanted event. | perform a detective control
segregation of duties | Separation of responsibilities to reduce error or misuse risk. | maintain segregation of duties
maker-checker | A process separating preparation from an independent check. | follow the maker-checker procedure
bank reconciliation | Comparison of bank and ledger records with explained differences. | complete a bank reconciliation
reconciling item | A difference identified between records being compared. | resolve a reconciling item
unmatched entry | A transaction lacking an identified counterpart or supporting match. | investigate an unmatched entry
suspense account | An account holding items temporarily pending appropriate classification. | clear supported suspense-account items
aging | Classification of unresolved items or balances by time outstanding. | review the aging of open items
exception log | A record of deviations or unresolved items and their status. | update the exception log
root-cause analysis | Examination of the underlying reason a problem occurred. | document the root-cause analysis
corrective action | A step intended to resolve an identified problem. | approve corrective action
control deficiency | A weakness in a control's design or operation. | assess a potential control deficiency
material weakness | In US AS 2201, a control deficiency with a reasonable possibility that a material misstatement escapes timely prevention or detection. | refer a material-weakness assessment
misstatement | An error or omission in reported financial information under the relevant framework. | assess a possible misstatement
fraud indicator | A sign warranting assessment of possible deliberate wrongdoing. | escalate a fraud indicator
professional skepticism | A questioning approach to evidence and possible misstatement. | apply professional skepticism
sign-off | Recorded confirmation that a specified review or approval is complete. | withhold sign-off pending resolution
remediation | Work to address an identified issue and its causes. | track remediation progress
whistleblowing channel | An authorized or protected route for reporting concerns under applicable arrangements. | identify the reporting channel''',
    precision='The net difference is zero, but a receipt and two payments remain unsupported. Offsetting amounts do not prove that each transaction is valid, recorded, classified, or in the correct period. Do not clear unexplained items solely to obtain a clean total.',
    precision_extra='An unmatched entry is an observation, not a finding of fraud. A control deficiency and a material weakness are also not interchangeable labels. Formal classification depends on the relevant framework, evidence, and qualified assessment.',
    phrases='''State the open work | Three entries remain unmatched despite a zero net difference.
Give the amounts | The receipt is $1,200; the payments are $700 and $500.
Separate arithmetic | The amounts offset, but the individual causes remain unknown.
Preserve evidence | Bank references and the records checked are attached.
Limit a conclusion | No fraud finding or corrective entry has been approved.
Assign continuation | Noah will continue the review after this handoff.
Avoid forced clearance | We should not net unsupported items merely to close the reconciliation.
Close with status | Sign-off remains pending resolution and the required review.
Name a reference | Please use the bank transaction reference, not only the amount.
Describe a check | I checked the ledger export through the stated cutoff.
State a negative finding | I did not find a match in the records reviewed.
Avoid overreach | Not found in this extract does not mean the transaction never occurred.
Request confirmation | Please acknowledge the three open items and next checks.
Check independence | The required reviewer must assess the proposed adjustment.
Preserve history | Keep the original exception and the reason for any later correction.
Escalate evidence | Route any supported concern through the appropriate reporting process.''',
    notes='''Not found versus absent | Limit a search result to the records actually examined; an incomplete search does not prove universal absence.
Despite | "Unmatched despite a zero net difference" highlights why arithmetic completion is not evidential completion.
Observation verbs | Appears, shows, and remains unmatched report evidence without asserting deliberate wrongdoing.
Sign-off scope | Identify which control or review is signed off; approval of one step does not complete every related process.
Cause language | Unknown cause is an explicit status, not an invitation to fill in a plausible explanation.
Handoff precision | Name the owner, references, checks performed, remaining work, and approval state.''',
    d='''Which statement accurately separates total and support? | The entries net to zero, but each remains unmatched. | Zero net difference proves every transaction is valid. | The $1,200 receipt cancels the need to review payments. | A zero total authorizes removal of all three records. | Netting is arithmetic; it does not establish the individual transactions' validity or correct accounting.
Which phrase reports the search result without overclaiming? | No match was found in the ledger extract reviewed. | The transaction never existed anywhere. | The supplier definitely committed fraud. | Every possible record has been checked. | The bounded statement identifies the scope of the actual search instead of making unsupported universal or misconduct claims.
Which action preserves the control? | Retain open items and independently review any supported corrections | Match the receipt to both payments because their total agrees | Close the reconciliation but retain the unexplained items in an informal note | Post a net-zero clearing journal without transaction support | Separate support and independent review are required for the unresolved transactions. A zero net amount or an informal note does not establish valid matching or authorize an entry.
Which classification is supported now? | Unmatched entries with causes unknown | Confirmed material weakness | Proven fraud | Approved misstatement correction | The facts establish unresolved matching issues, not the cause, severity classification, or authorized correction.''',
    dialogue='''Noah | The summary shows zero difference. Before you leave, can I sign this reconciliation, or are the three lines underneath still waiting for support?
Yara | They remain [[unmatched entries::Unmatched entries lack identified support or counterparts; a zero combined amount does not resolve each transaction.]]: a twelve-hundred-dollar receipt and payments of seven hundred and five hundred. They cancel numerically, but I haven't established what caused any of them.
Noah | Keep all three visible. Did you find a customer or supplier reference that connects them, or is the amount the only apparent link so far?
Yara | Only the arithmetic links them. Each [[reconciling item::A reconciling item is an identified difference requiring explanation; offsetting differences still need separate support and treatment.]] still needs its own support. I haven't proposed entries or treated the receipt as a reversal of those payments.
Noah | Show me the last check you completed. I'll take this forward, but I don't want to repeat a search without knowing which records you used.
Yara | The attached [[control evidence::Control evidence records the checks performed and their scope, allowing the reviewer to assess the work rather than rely on an assertion.]] lists the bank references, ledger extract, cutoff and searches. I found no match in those records; I haven't checked every possible later posting.
Noah | That's useful. I'll compare the references with the next relevant records. Where have you kept the open status so it won't disappear from the handoff?
Yara | In the [[exception log::The exception log preserves unresolved items, evidence, and status, preventing an unsuccessful search from becoming an unsupported final conclusion.]], on three separate lines. Each has an amount, bank reference and checks completed; I haven't replaced them with a net-zero summary.
Noah | A manager asked whether unexplained payments mean wrongdoing. What have you told them? I need the concern recorded without presenting suspicion as an established cause.
Yara | There's no [[fraud finding::A fraud finding would assert deliberate wrongdoing; unmatched entries alone establish a review issue, not that conclusion.]]. The entries need investigation. If further evidence raises a concern, we'll use the reporting process rather than speculate in the reconciliation comment.
Noah | Understood. Have any corrections been approved, or has anything been moved to suspense? Tell me now so I use the right starting balances.
Yara | No [[corrective action::Corrective action addresses an identified problem; here neither cause nor authorized correction has been established.]] is approved or posted. I haven't moved the items elsewhere just to clear the list; the original differences are still there for review.
Noah | Then I'll acknowledge the handoff, not certify completion. The amount may balance, but we still need to establish the treatment of each transaction.
Yara | Yes, [[sign-off::Sign-off records completion of a defined review or approval; unresolved support prevents treating this reconciliation as completed.]] remains pending. I'll leave that stated beside the zero net amount so someone reading only the headline doesn't mistake it for a completed reconciliation.
Noah | I'll own the next checks. If I prepare a correcting entry myself, it will need a separate reviewer under our process, not my own approval.
Yara | That keeps [[segregation of duties::Segregation of duties separates responsibilities, here preparation and review, to reduce the risk of unchecked error or misuse.]] intact. The preparer and reviewer roles stay separate even though you are taking over the investigation from me this evening.
Noah | When an item is resolved, retain its original bank reference and the decision behind any adjustment. We need to explain the change, not just show a cleaner list.
Yara | The [[audit trail::The audit trail connects the original exception, investigation, decision, and approval so the resolution can be traced later.]] will include the original exception, later support, proposed treatment and approval. Resolving a line won't erase how it reached that decision.
Noah | Let me read it back: three unmatched items, causes unknown, references and searches attached, no entries approved, and I own the next review. Anything missing?
Yara | That's the current [[status::Status reports the actual stage of work and authority, not the misleading appearance of completion created by a zero total.]]. I'll be available for questions about the searches, but the attached evidence and open-item list are ready for you to continue.''',
    transfer_title='A matching amount is not a matching transaction',
    transfer_setup='Two unrelated payments are each $800. One has full supporting references; the other has no identified invoice. The reviewer has not approved treating them as the same transaction.',
    transfer='''Preparer: "The equal ___ does not establish a common transaction." | amount | Identical dollar values can belong to different transactions and do not prove a valid match.
Reviewer: "Check the payee and transaction ___." | reference | Payee and reference information help identify the specific payment beyond a coincidental amount.
Preparer: "The unsupported item remains ___." | open | The missing invoice and unapproved match leave the item unresolved.
Reviewer: "Do not clear it without sufficient ___." | evidence | Clearing requires support for the actual transaction, not merely an equal value elsewhere.''',
    rehearsal=["Read the corrected handoff. State the $1,200 receipt and $700 and $500 payments separately before giving their zero net amount.","Switch roles. Keep three items open, causes unknown and corrections unapproved. Read Noah's final check-back against Yara's confirmation.","Read the corrected transfer twice. Use payee and reference evidence to distinguish the two $800 payments; do not match them by amount alone."]))

BOOK['units'].append(unit(
    title='Valuation, M&A, Capital Allocation, and Executive Finance', scene='A valuation slide showing only the higher case',
    skill='Present valuation sensitivity and distinguish modeled enterprise value from a transaction price.',
    brief='A fictional discounted-cash-flow model estimates enterprise value at $20 million using 2% terminal growth and $30 million using 4% terminal growth. Other modeled inputs are unchanged, including the 9% discount rate. Both are scenarios, not offers. The presentation currently shows only $30 million. Daniel, a corporate-finance analyst, and Aisha, the chief financial officer, review the slide. The illustrative enterprise-to-equity bridge deducts $3 million of net debt and assumes no other adjustments. No acquisition or financing decision is approved.',
    cast='Daniel | Corporate-finance analyst\nAisha | Chief financial officer',
    culture=('Make sensitivity visible before defending a single number', 'Executives may ask for one decisive figure, but a model-dependent range can be the more accurate answer. Explain what changed between cases and what stayed constant. A valuation output supports a decision; it is not an offer, an approved bid, or proof of a future sale price.'),
    a='''Which input changes between the two stated scenarios? | Terminal growth, from 2% to 4% | Discount rate, from 2% to 9% | Net debt, from $3 million to $30 million | Every forecast input | The briefing holds the other model inputs constant and changes only the terminal-growth assumption.
What does the $30 million figure represent? | Modeled enterprise value in the 4% terminal-growth case | An accepted purchase price | Equity value after debt | A guaranteed future sale value | The figure is a scenario output before the stated equity bridge, not a transaction or guarantee.
What is equity value in the higher case under the stated simplified bridge? | $27 million | $33 million | $30 million | $3 million | The case instructs deduction of $3 million net debt from $30 million enterprise value, with no other adjustments assumed.''',
    vocabulary='''valuation | An estimate of value using specified methods and assumptions. | explain the valuation basis
DCF | Discounted cash flow, estimating value from projected cash flows and a discount rate. | review the DCF assumptions
discount rate | A rate used to convert future cash flows to present value. | test the discount-rate assumption
WACC | Weighted average cost of capital, combining funding costs using defined weights. | assess the WACC input
present value | Today's modeled equivalent of future cash flows under a discount rate. | calculate present value
terminal value | Value assigned beyond an explicit forecast horizon. | test the terminal-value contribution
terminal growth | The assumed growth rate used for the continuing period in a model. | justify the terminal-growth assumption
free cash flow | A cash-flow measure after defined operating and investment needs. | define the free-cash-flow measure
enterprise value | Value attributed to the operating business before the specified financing adjustments. | bridge enterprise value to equity value
equity value | Value attributable to equity holders after relevant adjustments. | reconcile equity value
net debt | Debt less the cash or cash-like items included in the chosen definition. | verify the net-debt definition
valuation multiple | A ratio relating value to a specified financial or operating measure. | compare valuation multiples
comparable companies | Businesses selected as relevant valuation references. | screen comparable companies
precedent transactions | Past deals used as valuation references after comparability review. | analyze precedent transactions
sensitivity analysis | Testing how a result changes when selected inputs change. | present sensitivity analysis
base-case valuation | The value produced by the selected central scenario. | qualify the base-case valuation
NPV | Net present value, discounted net cash flows including the investment on a stated basis. | evaluate project NPV
IRR | Internal rate of return, a rate making the modeled NPV zero where such a rate exists. | compare IRR with the stated hurdle
hurdle rate | A specified minimum return criterion for a decision. | confirm the hurdle rate
capital allocation | Decisions about committing resources among uses. | support capital-allocation decisions
capital expenditure | Spending on assets under the applicable accounting and planning definitions. | forecast capital expenditure
synergy | A benefit expected from combining operations or capabilities. | challenge the synergy estimate
due diligence | Investigation of relevant information before a proposed transaction. | complete financial due diligence
accretion and dilution | Increases or decreases in a specified per-share measure after a transaction. | distinguish EPS accretion from value creation''',
    precision='The $20 million and $30 million values are conditional model outputs. Holding other inputs constant isolates the modeled sensitivity to terminal growth, but does not prove either growth assumption is achievable or that a buyer will pay either amount.',
    precision_extra='Under this deliberately simplified case, $30 million enterprise value less $3 million net debt gives $27 million equity value. Actual transaction bridges can include additional adjustments. A deal that increases earnings per share is not automatically value-creating.',
    phrases='''Present both cases | The model gives $20 million at 2% terminal growth and $30 million at 4%.
Name the constant | The discount rate remains 9% in both scenarios.
State the sensitivity | The output is sensitive to the continuing-growth assumption.
Avoid a price claim | These are modeled values, not offers or agreed transaction prices.
Explain the bridge | The illustrative equity bridge deducts $3 million of net debt.
Limit the simplification | This example assumes no other adjustments.
Separate authority | No acquisition or financing decision has been approved.
Close with evidence | We need support for the assumptions before recommending a decision.
Challenge selection | Why does the slide show only the higher case?
Define the metric | Is that enterprise value or value attributable to equity holders?
Test a driver | Which input change produces the difference between these outputs?
Preserve context | Keep the growth and discount-rate assumptions beside the values.
Qualify synergies | The benefits are modeled assumptions, not realized cash flows.
Compare methods | Do the selected comparable companies have relevant business and risk characteristics?
Separate outcomes | Earnings-per-share accretion is not proof of value creation.
Make uncertainty usable | The range identifies an assumption requiring review, not a guaranteed pricing interval.''',
    notes='''At versus by | Value is $30 million at 4% growth; it does not rise by only 4% merely because that is the input.
Holding constant | Name what stays unchanged when isolating sensitivity to one input.
Modeled versus offered | A modeled value comes from assumptions; an offer comes from a negotiating party.
Before and after | Specify whether the number is before or after net debt and other transaction adjustments.
Range language | A scenario range is not automatically a probability interval or a guaranteed minimum and maximum.
Value creation | A positive movement in one accounting metric does not establish an attractive investment on every relevant basis.''',
    d='''Which revision most accurately presents the valuation? | Show both values with their growth assumptions and the unchanged discount rate. | Show $30 million as a guaranteed selling price. | Hide the $20 million case because it is lower. | Relabel both scenarios as accepted bids. | Both conditional outputs and their differing assumption are needed to avoid selective presentation of the higher modeled value.
Which arithmetic follows the case's simplified equity bridge? | $30 million minus $3 million equals $27 million. | $30 million plus $3 million equals $33 million. | $30 million divided by 4% is equity value. | Net debt has no role because the model uses cash flows. | The explicitly supplied bridge deducts net debt and assumes no other adjustments; it does not add debt or ignore it.
Which statement properly limits the scenario range? | It shows outcomes under stated assumptions, not a guaranteed pricing interval. | It proves every buyer will pay between the two values. | It establishes a 100% probability of a $30 million sale. | It eliminates the need to review growth assumptions. | Model scenarios describe conditional outputs, not market commitments or quantified probabilities unless separately justified.
Which question most directly tests whether a synergy is deliverable? | What evidence, timing, implementation cost and dependencies support the benefit? | Which presentation slide will show the combined earnings? | Which transaction name will appear in the announcement? | Can the model display the benefit as a single annual total? | Deliverability requires support for the benefit and the work and costs needed to obtain it. Naming, presentation and aggregation do not establish that the benefit can be realized.''',
    dialogue='''Aisha | The executive slide shows thirty million dollars. Before we discuss a bid, tell me which value that is and what assumption produces it in the model.
Daniel | It is [[enterprise value::Enterprise value concerns the operating business before the stated financing adjustments; it is not the equity figure or an approved bid.]] under the four-percent terminal-growth case. The two-percent case gives twenty million, but that lower output is missing from the current slide.
Aisha | Show both. Are any other inputs changing, or can the audience attribute the difference to growth alone within this particular comparison?
Daniel | The [[discount rate::The discount rate converts future cash flows to present value; holding it constant isolates the growth comparison.]] remains nine percent, and the other modeled inputs are unchanged. This comparison isolates the model's response to the terminal-growth assumption.
Aisha | Then make that sensitivity explicit. A ten-million-dollar difference should not be presented as extra value we have already created or secured from a buyer.
Daniel | I will describe the [[sensitivity analysis::Sensitivity analysis tests how outputs respond to changed inputs; it does not establish that the more favorable assumption will occur.]] and keep the input labels beside the outputs. Neither result is an offer, and neither guarantees a transaction price.
Aisha | Why four percent? Is there evidence for that continuing growth rate, or have we chosen it because we prefer the thirty-million output?
Daniel | The [[terminal growth::Terminal growth is an assumed continuing-period rate; it needs support rather than selection solely to obtain a preferred valuation.]] input still needs review against the business and model context. The higher scenario is available for analysis, not established as the most likely outcome.
Aisha | The audience may also confuse business value with the amount attributable to shareholders. Show the bridge and identify exactly which adjustments this example includes.
Daniel | The simplified bridge deducts three million of [[net debt::Net debt is the specified debt less included cash measure; the case deducts $3 million when moving from enterprise to equity value.]] and assumes no other adjustments. That gives twenty-seven million in the higher case and seventeen million in the lower one.
Aisha | Keep the simplification visible. Actual deal adjustments may differ, and the slide must not imply that this training calculation settles every component of transaction proceeds.
Daniel | Agreed. I will label the resulting figures [[equity value::Equity value is the amount attributable to equity holders after the specified adjustments, here under an expressly simplified bridge.]] under the stated bridge, not cash proceeds guaranteed to each shareholder or an approved purchase consideration.
Aisha | A team member wants to add synergies to the higher value without changing the cost assumptions. Have the benefits, implementation costs, and timing been assessed?
Daniel | No. The proposed [[synergies::Synergies are expected combination benefits; they are not realized cash flows and require support for costs, timing, and dependencies.]] are not verified. We should not add the benefits while omitting the costs and dependencies needed to achieve them.
Aisha | Then show the costs before adding the benefits. We also need to compare this transaction with the other uses of those funds.
Daniel | The [[capital allocation::Capital allocation compares uses of resources; a high valuation output alone does not establish that a transaction is the best use.]] discussion needs consistent assumptions and relevant alternatives. We should identify what further evidence would support a recommendation instead of treating the model as authorization.
Aisha | One presenter says the transaction would increase earnings per share, so it must create value. That sentence needs a more careful distinction.
Daniel | I will separate [[accretion::Accretion increases a specified per-share metric; it does not by itself establish economic value creation.]] in the stated accounting metric from value creation. The financing structure, price, risk, and cash-flow assumptions still matter to the investment assessment.
Aisha | Revise the slide with both scenarios, the debt bridge, and the assumptions requiring review. No bid or financing commitment should be implied by the presentation.
Daniel | I will preserve that approval boundary and list the outstanding [[due diligence::Due diligence investigates transaction information; unfinished checks limit the recommendation and do not authorize a commitment.]]. The pack will support an informed decision without turning conditional model outputs into promises or approvals.''',
    transfer_title='The higher project return has different assumptions',
    transfer_setup='Project A and Project B have modeled returns based on different forecast periods and cost inclusions. No comparable analysis or investment approval is complete. The presenter wants to rank them by the headline rates.',
    transfer='''Analyst: "The headline rates use different calculation ___." | bases | Different periods and cost inclusions prevent a reliable ranking from the headline rates alone.
Director: "Align the periods and included ___ before comparing." | costs | Consistent cost treatment and time scope are needed to understand the relative modeled outcomes.
Analyst: "The ranking remains ___ until that review." | provisional | The underlying comparison is incomplete, so the ranking cannot be presented as a settled conclusion.
Director: "A model result does not itself provide investment ___." | approval | Analysis informs the decision; it does not replace the authorized investment approval process.''',
    rehearsal=["Read the corrected valuation review. Pair $20 million with 2% growth and $30 million with 4%, holding the 9% discount rate constant.","Switch roles. Give $27 million equity value only under the stated $3 million net-debt deduction and no-other-adjustments assumption.","Read the corrected project transfer. Keep the ranking provisional until periods and included costs are aligned; no investment is approved."]))
