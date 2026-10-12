"""Additional conversations on currency exposure, execution status, and financing terms."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Explaining currency exposure without promising a perfect hedge',
    skill='Distinguish asset performance, reporting currency, and the scope of an authorized currency hedge.',
    setup='A fictional fund reports in US dollars and owns assets denominated in another currency. A client asks why a positive local-currency asset return does not automatically produce the same US-dollar return. Portfolio specialist Anika explains currency translation and the limits of hedging. No hedge trade, hedge ratio, or product recommendation has been authorized.',
    cast='Client | Institutional client contact\nAnika | Portfolio specialist',
    reference=('Investor.gov. International investing.', 'https://www.investor.gov/introduction-investing/investing-basics/investment-products/international-investing'),
    dialogue='''Client | The overseas assets rose in their local currency, but our dollar report shows a different result. Is one of the reports wrong?
Anika | Not necessarily. The asset return and the currency translation can affect the dollar result differently, so we need the actual basis.
Client | The report should identify which currency measures the underlying asset and which currency is used for our account summary.
Anika | Exactly. The [[reporting currency::The reporting currency is the currency in which the result is expressed, which can differ from the denomination of the underlying assets.]] changes how the result is expressed; it does not change the historical local-currency price by relabeling it.
Client | A change in the exchange rate can therefore affect what the investment is worth when expressed in dollars.
Anika | That is part of [[currency exposure::Currency exposure is sensitivity to exchange-rate movements, distinct from the underlying asset's local-currency performance.]]. We should not describe a positive local result as a guaranteed positive result in every currency.
Client | Would hedging remove all of the uncertainty and make the overseas investment effectively risk-free?
Anika | No. A [[currency hedge::A currency hedge addresses specified exchange-rate exposure under its actual terms and does not eliminate every investment risk or implementation cost.]] addresses a defined exposure, not every market, credit, liquidity, or implementation risk.
Client | We would need to know how much exposure is covered and whether the covered amount stays aligned as the portfolio changes.
Anika | Yes. The [[hedge ratio::The hedge ratio relates the hedge amount to the defined exposure and needs a stated basis rather than an assumption of complete coverage.]] and its measurement basis matter, along with timing, costs, and the actual instrument.
Client | I should not assume that a target hedge percentage means the actual exposure is perfectly matched at every moment.
Anika | Correct. Changes in asset values or cash flows can affect the relationship, and the operational details need monitoring under the mandate.
Client | There may also be differences between the exposure we want to offset and what the selected instrument actually tracks.
Anika | That can create [[basis risk::Basis risk arises when the hedging instrument and the exposure do not move in a perfectly matching way under the relevant circumstances.]], so the explanation should not promise a perfect offset merely because the word hedge appears.
Client | We should evaluate any proposal against the approved policy rather than treat this explanation as authorization for a trade.
Anika | Exactly. We are clarifying the risk, not choosing an instrument or granting trading authority.
Client | The next report can separate local performance, currency effects, and any actual hedging contribution using the stated methodology.
Anika | That supports a clear [[return decomposition::Return decomposition separates the defined components of performance under a stated method rather than conflating asset movement with currency effects.]] without claiming that a simple label explains every difference.
Client | I will ask for the current authorized policy and the methodology before discussing whether a change is needed.
Anika | Good. That keeps the conversation grounded in the actual mandate and evidence, with no promise of risk-free results or automatic action.''',
    transfer_title='A local gain was described as a dollar guarantee', transfer_setup='An asset gains in its local currency. The dollar effect depends on the actual exchange-rate movement, which is not supplied.',
    transfer='''Client: "The supplied gain is in the ___ currency." | local | The brief identifies the asset's local-currency result, not a dollar result.
Specialist: "The dollar result also depends on the exchange ___." | rate | Currency translation requires the actual exchange-rate movement for the period.
Client: "A positive dollar return is not ___." | established | The missing currency movement prevents a conclusion about the dollar outcome.
Specialist: "Keep the two measurement bases ___." | distinct | Local-currency and dollar returns answer different measurement questions and should remain labeled.'''),
scenario(title='Reconciling a partial fill before replacing an order',
    skill='Describe order status precisely and prevent an unconfirmed cancellation from being treated as completed.',
    setup='A fictional authorized order is for 1,000 shares. Execution records show fills of 300 and 200 shares. A request to cancel the remaining quantity has been sent but not confirmed. Trader Ben and operations analyst Leila reconcile the status before any further authorized action. No settlement date, replacement authorization, or additional fill is supplied.',
    cast='Ben | Trader\nLeila | Operations analyst',
    reference=('Investor.gov. Executing an order.', 'https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/executing-order'),
    dialogue='''Ben | The original order was for one thousand shares. I requested cancellation, so I was about to treat the whole order as inactive.
Leila | The execution record already shows fills of three hundred and two hundred shares. We need to separate those events from the cancellation request.
Ben | That means five hundred shares have executed, with five hundred remaining before any later confirmed event.
Leila | Correct. It is a [[partial fill::A partial fill means only part of the order has executed, here five hundred of the one thousand shares.]], not an unexecuted order that can simply be described as though nothing happened.
Ben | The cancellation message was sent for the remainder, but I do not yet have an acknowledgment that it was completed.
Leila | Then the [[cancellation request::A cancellation request is an instruction awaiting the relevant confirmation and must not be treated as proof that the remaining order is canceled.]] is still distinct from a confirmed cancellation.
Ben | We should verify whether any further execution occurred before assuming the remaining quantity is no longer live.
Leila | Yes. Reconcile the actual [[execution record::The execution record identifies completed fills and is needed to establish the current status rather than relying only on a sent message.]] and the current order status through the approved process.
Ben | I do not want a replacement instruction to duplicate exposure if the original remainder is still capable of filling.
Leila | That is why the [[remaining quantity::The remaining quantity is the unfilled part of the original order, whose live or canceled status still needs confirmation here.]] and its status need to be clear before any further authorized action.
Ben | The update should say five hundred executed and cancellation of the remainder requested, not one thousand canceled.
Leila | Exactly. It should also avoid saying settled when the record only establishes execution.
Ben | The actual transfer of cash and securities is a separate event, and this case does not supply its completion.
Leila | Correct. [[Settlement::Settlement concerns completion of the relevant cash and securities transfer and is distinct from an order being placed or a trade being executed.]] must be reported from its own verified status and applicable process.
Ben | I will preserve the order identifier, fill details, and cancellation message so the team can reconstruct the sequence accurately.
Leila | Keep the [[audit trail::The audit trail preserves the sequence of instructions, executions, and confirmations instead of rewriting the history to match an intended outcome.]] intact and route any discrepancy through the normal controls.
Ben | Once the current status is confirmed, any replacement or further action still needs the appropriate authorization.
Leila | Yes. Reconciling the record does not itself create authority for a new trade.
Ben | My immediate report will contain the supplied fills, the five-hundred-share remainder, and the unconfirmed cancellation status.
Leila | That is precise. It avoids treating an intention as an outcome and helps prevent duplicate exposure without inventing a settlement date or new instruction.''',
    transfer_title='A sent request was marked completed', transfer_setup='An order has 500 shares unfilled. A cancellation request is sent, but no completion acknowledgment is received.',
    transfer='''Trader: "Five hundred shares remain ___." | unfilled | The supplied remainder has not been reported as executed.
Operations: "The cancellation has been ___, not confirmed." | requested | Sending the request does not establish that the cancellation completed.
Trader: "We must verify the current order ___." | status | The live or canceled state must be checked through the actual process.
Operations: "Preserve the full audit ___." | trail | The instruction and confirmation sequence should remain intact and traceable.'''),
scenario(title='Clarifying a floating-rate financing illustration',
    skill='Distinguish the benchmark, spread, illustrative rate, and total financing cost without implying a commitment.',
    setup='A fictional corporate financing proposal quotes a benchmark currently supplied as 4.5 percent plus a spread of 200 basis points. For this arithmetic illustration only, no floor, cap, compounding convention, or other adjustment applies, so the indicated annual rate is 6.5 percent before fees. The proposal is indicative, not a committed facility. Actual reset terms, fees, covenants, conditions, and authority require review.',
    cast='CFO | Corporate finance officer\nBanker | Financing adviser',
    dialogue='''CFO | The proposal says benchmark plus two hundred basis points. Does that mean the company will pay a fixed two-percent rate?
Banker | No. The spread is added to the stated benchmark under this simplified illustration; it is not the whole rate.
CFO | Two hundred basis points means two percentage points, and the supplied benchmark is currently four and a half percent.
Banker | Correct. The [[spread::The spread is the two-percentage-point addition to the benchmark in the supplied illustration, not the complete borrowing rate.]] gives an indicated six-and-a-half-percent rate here, before fees and with the stated exclusions.
CFO | That calculation does not make the benchmark fixed for the full life of any eventual financing.
Banker | Exactly. The [[benchmark rate::The benchmark rate is the reference component, whose future changes and application depend on the actual financing terms.]] and its application depend on the actual terms, including when the rate is determined or reset.
CFO | We need to review those reset provisions rather than assume today's reference figure will apply to every future period.
Banker | Yes. The [[reset convention::The reset convention specifies how and when the floating-rate component is updated and cannot be inferred from a single quoted benchmark value.]] is part of the real terms, not something supplied by this simple addition.
CFO | The draft also lists fees separately, so six and a half percent is not a complete statement of every financing cost.
Banker | Correct. Any [[all-in cost::All-in cost requires the relevant fees and economic terms to be included under a stated method, which the before-fees illustration does not provide.]] comparison needs a defined basis and the actual costs, not just the headline rate.
CFO | I should also check whether the real facility includes floors, caps, or other provisions excluded from this example.
Banker | Yes. The exclusions make the arithmetic clear here; they do not establish that such provisions are absent from every financing arrangement.
CFO | The board sees the bank name and assumes the money is already committed. The document is labeled indicative.
Banker | Then preserve that [[indicative proposal::An indicative proposal presents terms for discussion and must not be reported as a committed facility when no commitment is supplied.]] status. We have not established a binding commitment or satisfaction of the actual conditions.
CFO | The next review should cover the financial terms, covenant definitions, conditions, and the authority needed to proceed.
Banker | Exactly. The relevant [[conditions precedent::Conditions precedent are specified requirements that must be satisfied for the relevant contractual step, and their completion cannot be assumed from a proposal.]] and other terms need proper legal and financial review in the actual transaction.
CFO | I will describe the six-and-a-half-percent figure as illustrative and before fees, using the supplied current benchmark.
Banker | That is accurate. Do not call it a fixed lifetime rate or a verified total cost.
CFO | And I will report the financing as under discussion rather than treat this conversation as authorization to sign or draw funds.
Banker | Good. Clear language separates the arithmetic, the contractual terms, and the commitment status instead of compressing them into one reassuring number.''',
    transfer_title='The benchmark changes but the spread does not', transfer_setup='For the same simplified arithmetic only, the benchmark rises to 5 percent and the spread remains 200 basis points. No other adjustments apply; the illustrated rate is 7 percent before fees.',
    transfer='''CFO: "The spread remains two hundred basis ___." | points | Two hundred basis points remains a two-percentage-point addition in the illustration.
Banker: "The benchmark is now five ___." | percent | The scenario explicitly changes the reference rate to five percent.
CFO: "The illustrated rate is ___ percent." | seven | Five percent plus two percentage points equals seven percent under the stated exclusions.
Banker: "That figure still excludes ___." | fees | The supplied arithmetic remains before fees rather than a complete all-in cost.'''),
]
