"""Additional original insurance conversations with explicit fictional terms."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The rate stayed; the payroll changed",
        skill="Explain an audited premium by separating exposure, rate, total premium, and balance due.",
        setup="Fictional annual policy: premium = eligible payroll / 100 x $2.40. Estimated payroll $250,000; $6,000 deposit premium fully paid. Audited eligible payroll $300,000. One unchanged classification and rate; no minimum, modifier, tax, fee, or other adjustment. The figures are supplied, not real rating advice.",
        cast="Arjun|Business owner\nMei|Premium-audit specialist",
        dialogue="""Arjun|The audit statement asks for another twelve hundred dollars. I thought our six-thousand-dollar premium was already paid in full. Has the rate changed?
Mei|The [[rate per hundred::The rate is $2.40 for each $100 of eligible payroll and is unchanged; a larger exposure base can increase premium without a rate increase.]] is still two dollars forty. The estimated payroll changed to the audited amount, which changes the calculation.
Arjun|We estimated two hundred fifty thousand and ended at three hundred thousand. I want to see how that becomes an insurance charge.
Mei|The [[exposure base::The exposure base is eligible payroll in this fictional policy; $300,000 replaces the $250,000 estimate without changing the rate or classification.]] is eligible payroll here. Divide three hundred thousand by one hundred, then multiply by two dollars forty.
Arjun|That gives seventy-two hundred dollars for the whole policy period, not seventy-two hundred in addition to what we paid.
Mei|Correct. The six thousand was your [[deposit premium::The deposit premium was calculated from estimated payroll and already paid; it must be credited against the audited total rather than charged again.]]. Subtract it from the audited total to find the remaining amount.
Arjun|Seventy-two hundred minus six thousand leaves twelve hundred. The statement's balance is right under those supplied figures, but the heading confused me.
Mei|I can label it [[additional premium::Additional premium is the $1,200 difference between the $7,200 audited total and $6,000 already paid, not the full audited premium.]] and show the calculation beside it. That distinguishes the adjustment from the complete annual premium.
Arjun|Is this a penalty for reporting a higher payroll, or a charge for extra claims? We are not discussing claim costs here.
Mei|Neither is included in this exercise. This adjustment reconciles the estimated and audited exposure under the stated formula. It does not introduce a penalty or claims charge.
Arjun|Payroll is twenty percent above the estimate, and the total premium is twenty percent higher. I should not call that a twenty-percent rate increase.
Mei|Exactly. The rate is unchanged. The increase comes from the exposure amount, with every other calculation condition held constant in this example.
Arjun|Our payroll system total is not always the same as eligible payroll for insurance. Where do we check what went into the audit figure?
Mei|Use the [[audit worksheet::The audit worksheet records the payroll basis and classification used; payroll-account totals must be reconciled to the eligible exposure under the actual policy rules.]] and supporting records. The supplied three hundred thousand is already eligible payroll; do not substitute another total without reconciling its basis.
Arjun|The worksheet uses one classification. Could I move some wages to another class myself to make the adjustment smaller?
Mei|Any classification question needs the actual operations, applicable rules, records, and authorized review. This arithmetic does not establish eligibility for a different class.
Arjun|If I find a duplicated payroll entry, I should identify that entry and request a correction rather than simply challenge the whole statement.
Mei|Yes. Send a [[reconciliation request::A reconciliation request identifies the disputed audit entry and supporting records; it seeks a supported correction rather than assuming the full audit is invalid.]] through the approved channel, with the specific difference and supporting record. The reviewer can then address the actual issue.
Arjun|For this example, I can explain the same rate, higher eligible payroll, seventy-two-hundred total, six thousand paid, and twelve hundred remaining.
Mei|That is the complete reconciliation. Keep it separate from renewal pricing, claim coverage, and any real dispute deadline, which require their own terms and records.""",
        transfer_title="Credit the amount already paid",
        transfer_setup="Fictional formula: eligible payroll / 100 x $3.00. Estimated payroll $150,000; deposit $4,500 fully paid. Audited eligible payroll $180,000. The rate and classification are unchanged, with no other adjustments.",
        transfer="""Specialist: The audited premium totals ___ dollars.|5,400|One hundred eighty thousand divided by one hundred and multiplied by three gives 5,400 dollars.
Owner: Credit the ___ dollars already paid.|4,500|The fully paid deposit is 4,500 dollars and must be credited against the audited total.
Specialist: The additional balance is ___ dollars.|900|The audited total of 5,400 minus the 4,500 deposit leaves nine hundred dollars.
Owner: The changed input is eligible ___, not the rate.|payroll|The rate is held constant, while eligible payroll increases from 150,000 to 180,000 dollars.""",
        reference=("Travelers: premium-audit purpose and exposure reconciliation", "https://www.travelers.com/business-insurance/services/premium-audit"),
    ),
    scenario(
        title="Two payments, one deductible",
        skill="Explain a staged property-claim payment without confusing depreciation, cash value, and net payment.",
        setup="Fictional covered repair: agreed replacement cost $20,000, depreciation $5,000, one $1,000 deductible. Initial payment = replacement cost minus depreciation minus deductible. The full $5,000 is recoverable after stipulated repair conditions are verified. Assume completed eligible repairs cost $20,000, sufficient limits, and no other adjustments.",
        cast="Carla|Policyholder\nOmar|Claims representative",
        dialogue="""Carla|Your estimate says twenty thousand dollars, but the first payment is fourteen thousand. I need to explain the six-thousand-dollar difference to the contractor.
Omar|The agreed [[replacement cost::Replacement cost is the agreed $20,000 repair basis in this exercise, before the stated depreciation holdback and deductible affect the initial payment.]] is twenty thousand. Five thousand is withheld depreciation, and one thousand is your single deductible.
Carla|Then twenty thousand minus five thousand is fifteen thousand. Is that the actual cash value in this supplied calculation?
Omar|Yes. Here [[actual cash value::Actual cash value is defined here as replacement cost less the $5,000 depreciation, giving $15,000 before the separate deductible.]] is fifteen thousand before the deductible. The fourteen thousand is the net initial payment, not that gross valuation.
Carla|I was treating depreciation and the deductible as two amounts that I would permanently lose. The statement calls the depreciation recoverable.
Omar|Under these fictional terms, the [[recoverable depreciation::The full $5,000 depreciation is recoverable in this example after the stipulated repair conditions are verified; this is not a rule for every policy.]] is released after the stipulated repair conditions are verified. It is separate from the deductible you retain.
Carla|Assuming the eligible repairs cost the full twenty thousand and those conditions are satisfied, the later payment would be five thousand.
Omar|Correct. The [[supplemental payment::The supplemental payment is the $5,000 held back in this stipulated case; adding it to $14,000 gives $19,000 total insurer payments.]] would bring insurer payments to nineteen thousand altogether. Your one-thousand-dollar share completes the twenty-thousand repair cost.
Carla|Why is the deductible not subtracted from that second payment too? Someone suggested I should expect only four thousand later.
Omar|Because this example applies one deductible to the loss, not one to every payment. It was already reflected in the fourteen-thousand initial payment.
Carla|So fourteen plus five is nineteen. Subtracting the deductible again would leave me bearing two thousand, contrary to the stated terms.
Omar|Exactly. Check the [[payment ledger::The payment ledger records amounts already issued and deductions already applied, preventing a second deduction or a duplicate payment for the same loss.]] before explaining the remaining amount. Multiple payments do not automatically mean multiple deductibles.
Carla|What if the contractor's final invoice is lower, or the repaired items differ from the agreed scope? Does the same five thousand always follow?
Omar|That would change the supplied facts. The actual wording, eligible expenditure, completed work, and verification would need review before any further amount could be confirmed.
Carla|For our example, the repair conditions are stipulated. For a real file, I would need to provide the required completion evidence through the verified channel.
Omar|Yes. Keep the [[repair documentation::Repair documentation supports checking the policy's stipulated conditions; an estimate alone is not evidence that the required eligible repairs were completed.]] linked to the claim and agreed scope. A contractor's estimate and evidence of completed work serve different purposes.
Carla|Please label the statement clearly: replacement cost, depreciation, cash value before deductible, deductible, initial payment, and possible additional amount.
Omar|I can do that. The labels should let you reconcile the money without suggesting that every figure is a separate charge or an immediate payment.
Carla|And the nineteen thousand is the final insurer total under these assumptions, not nineteen thousand on top of the fourteen already received.
Omar|Correct. Show total entitlement and previous payments separately. That prevents the same confusion on the second statement and keeps the remaining amount understandable.""",
        transfer_title="Separate the total from the next payment",
        transfer_setup="Fictional covered loss: replacement cost $12,000, recoverable depreciation $3,000, one $1,000 deductible. Eligible repairs cost $12,000 and all stipulated recovery conditions are met. No other adjustment applies. The initial payment deducts both depreciation and deductible.",
        transfer="""Representative: The initial net payment is ___ dollars.|8,000|Twelve thousand minus three thousand depreciation minus one thousand deductible equals eight thousand dollars.
Policyholder: The later depreciation payment is ___ dollars.|3,000|The full stipulated three-thousand-dollar holdback is recoverable after the supplied conditions are met.
Representative: Total insurer payments equal ___ dollars.|11,000|Eight thousand initially plus three thousand later equals eleven thousand, leaving the one-thousand deductible with the policyholder.
Policyholder: The deductible is applied ___ in this example.|once|The fictional terms specify one deductible for the loss, so it is not deducted again from the later payment.""",
        reference=("Texas Department of Insurance: replacement cost and cash value", "https://www.tdi.texas.gov/pubs/consumer/cb025.html"),
    ),
    scenario(
        title="The annual limit has a remaining balance",
        skill="Explain per-occurrence and aggregate limits using a consistent payment sequence.",
        setup="Fictional liability policy: $1 million per occurrence, $2 million annual aggregate. Prior covered indemnity payments of $1.6 million reduce that aggregate. A new covered occurrence has agreed damages of $700,000. No deductible, defense-cost erosion, reinstatement, other payments, or other applicable limit. Other insurance is not assessed.",
        cast="Nora|Account manager\nFelix|Claims specialist",
        dialogue="""Nora|The new damages are seven hundred thousand dollars, below the million-dollar limit. The client expects that full amount from this policy.
Felix|That checks the [[per-occurrence limit::The per-occurrence limit is $1 million for this event, but satisfying it does not override the separate remaining annual aggregate.]], but there is also an annual cap. We need the remaining aggregate before stating the available amount.
Nora|The declarations show two million dollars annually. The claims ledger shows one point six million already paid against that same aggregate.
Felix|Then the [[remaining aggregate::The remaining aggregate is $2 million minus $1.6 million already applied, leaving $400,000 available under that cap.]] is four hundred thousand. It is not another two million available afresh for this occurrence.
Nora|The new loss is seven hundred thousand, but the remaining annual amount is only four hundred thousand. Which number constrains this payment?
Felix|The [[aggregate limit::The aggregate limit caps the stated year's combined payments; its remaining $400,000 is lower than both the $700,000 damages and $1 million occurrence limit.]] does. Under these assumptions, this policy pays four hundred thousand, not seven hundred thousand.
Nora|That leaves three hundred thousand of the agreed damages unpaid by this policy. It is not a new deductible, is it?
Felix|No. It is an [[unfunded remainder::The unfunded remainder is $700,000 damages less $400,000 from this policy; it results from the aggregate cap, not a deductible supplied in the case.]] under this policy's calculation. We have not assessed another policy or arrangement that might respond.
Nora|I should say unpaid by this policy, not automatically uninsured everywhere. Otherwise I would be claiming to have reviewed other protection.
Felix|Exactly. Be precise about which policy and limits the calculation covers. A clear limitation is more useful than a broader conclusion we have not established.
Nora|After the four-hundred-thousand payment, the remaining annual aggregate is zero. The one-million occurrence figure still appears on the declarations.
Felix|But that figure does not replenish the aggregate. The supplied annual cap is [[exhausted::Exhausted means no aggregate amount remains after the additional $400,000 payment; the printed occurrence limit does not restore that used annual capacity.]] after this sequence, with no reinstatement provision in the example.
Nora|Could defense costs change this result? Some policies treat them differently, and I do not want to imply one universal arrangement.
Felix|They could under different wording. Here defense-cost erosion is expressly excluded. We must check the actual terms before carrying this calculation into another policy.
Nora|The prior figure is paid indemnity, not simply a list of case reserves. We should keep those categories separate in the ledger.
Felix|Yes. The supplied [[aggregate erosion::Aggregate erosion is the reduction caused by the specified payments under this policy; an internal reserve must not be substituted for those stipulated paid amounts.]] comes from payments charged to this cap. Do not substitute reserves or unrelated payments for that defined amount.
Nora|If I show the timeline, it is two million at the start, four hundred thousand after prior payments, then zero after this occurrence.
Felix|That makes the sequence visible. Label the policy period too, rather than combining payments from unrelated years into one total.
Nora|I will explain the four-hundred-thousand policy payment and three-hundred-thousand remainder, then refer any other-insurance question for its own review.
Felix|Good. The client will see why a loss below the occurrence limit can still exceed the available annual amount, without confusing the shortfall with a deductible.""",
        transfer_title="Apply both stated caps",
        transfer_setup="Fictional policy: $800,000 per occurrence and $1.5 million annual aggregate. Prior payments against that aggregate total $1.3 million. New agreed covered damages are $350,000. No deductible, other erosion, reinstatement, or other applicable limit. Other insurance is not assessed.",
        transfer="""Specialist: Before the new payment, the remaining aggregate is ___ dollars.|200,000|One and a half million minus one point three million leaves two hundred thousand dollars.
Manager: After paying that available amount, this aggregate is ___.|exhausted|The two-hundred-thousand payment uses the entire remaining aggregate under the supplied assumptions.
Specialist: The amount unpaid by this policy is ___ dollars.|150,000|Three hundred fifty thousand damages minus two hundred thousand available leaves one hundred fifty thousand.
Manager: That shortfall is not a ___ under these terms.|deductible|The case supplies no deductible; the shortfall results from the exhausted aggregate limit.""",
        reference=("IRMI: general aggregate limit", "https://www.irmi.com/term/insurance-definitions/general-aggregate-limit"),
    ),
]
