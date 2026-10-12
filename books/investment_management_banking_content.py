"""Combined buy-side investment and investment-banking communication, with explicit role boundaries."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='investment-management-banking', title='Investment Management and Banking English',
    balanced_answer_columns=True,
    category='Business & professional services', cover_label='ENGLISH FOR INVESTMENT PROFESSIONALS',
    cover_title='Investment Management and Banking', cover_size=24,
    tagline='Explain the thesis. Reconcile the numbers. Respect the boundary.',
    audience='For investment analysts, portfolio managers, investment bankers, and transaction teams communicating in English.',
    roles='investment analysts, portfolio managers, investment bankers, capital-markets professionals',
    summary='Advanced English for investment mandates, portfolio risk, performance reporting, investment committees, valuation, transaction diligence, capital raising, and information barriers.',
    map_intro='Lessons 1-4 concern managing investments for a client or fund. Lessons 5-7 concern advising a corporate transaction or capital raise. Lesson 8 addresses information boundaries between roles. Neither role is permission to act for the other.',
    notes_title='The same number can answer different questions.',
    notes_intro='Investment discussions require clear labels for whose interests are represented, which figures are comparable, and what remains an assumption. A portfolio thesis, an issuer valuation, and a bank mandate are not interchangeable recommendations.',
    field_notes=[
        ('Name the role', 'A buy-side team invests for its client or fund. An investment-banking team advises or executes a corporate transaction under its actual mandate. Identify the role before explaining the recommendation.', '"Are we assessing this as a portfolio investment or advising the issuer?"'),
        ('Keep the basis attached', 'A return needs its period, currency, methodology, and fee basis. A valuation needs its assumptions and a distinction between enterprise and equity value.', '"That is the net return for the stated year, not a guaranteed future result."'),
        ('Show the dependency', 'A model output is conditional on its inputs. A signed contract, management forecast, and analyst assumption have different evidential status.', '"The base case uses management\'s retention assumption; that input remains unverified."'),
        ('Protect information boundaries', 'Being in the same organization does not authorize access to every client or transaction detail. Use the actual compliance process for sensitive information.', '"I cannot confirm confidential transaction information; let us route this to compliance."')],
    scope_note=FICTION + 'Professional English practice, not investment, tax, accounting, transaction, or legal advice; no offer, solicitation, trading instruction, suitability determination, or return promise. Figures and securities are invented. Models and transaction bridges are deliberately simplified and exclude items unless expressly supplied. Use current law, qualified professionals, actual client mandates, authorization, and compliance controls for real work. Do not enter client or confidential deal information into language exercises.',
    sources=[
        source('Investor.gov. Asset allocation and diversification.', 'https://www.investor.gov/introduction-investing/getting-started/asset-allocation', 'Background on objectives, time horizon, risk, and diversification; no model allocation is recommended here.'),
        source('CFA Institute. Code and Standards.', 'https://www.cfainstitute.org/standards/professionals/code-ethics-standards', 'Professional communication context, including performance presentation, reasonable basis, confidentiality, and material nonpublic information. The code is not a substitute for applicable law.'),
        source('Aswath Damodaran, NYU Stern. What is debt?', 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/whatisdebt.htm', 'Background for consistent treatment of debt and cash in valuation; the exercise bridge explicitly excludes other adjustments.'),
        source('SEC. Investor Bulletin: Investing in an IPO.', 'https://www.sec.gov/files/ipo-investorbulletin.pdf', 'Background on offering documents, indications of interest, pricing, and selling shareholders. No historical thresholds or filing deadlines from the bulletin are reproduced as current rules.')], units=[])

BOOK['units'].append(unit(
    title='Clarifying an institutional investment mandate', scene='A five-year objective includes a six-month cash need',
    skill='Separate investment objectives, liquidity requirements, and authority before discussing an allocation.',
    brief='Foundation trustee Nora describes a five-year growth objective for a portfolio. The foundation also needs USD 2 million for a committed payment in six months. Trustee willingness to accept market volatility does not remove that cash requirement. Portfolio manager David is clarifying the mandate; no asset allocation, product selection, or trading authorization has been approved.',
    cast='Nora | Foundation trustee\nDavid | Portfolio manager',
    culture=('A confident preference is not the whole mandate', 'Ask about constraints without treating the client\'s willingness to take risk as a complete assessment of financial capacity or liquidity.'),
    a='''Which need has the shorter horizon? | The USD 2 million payment in six months | The five-year growth objective | An unspecified retirement account | A ten-year loan not in the case | The committed payment is due in six months, earlier than the growth horizon.
What does willingness to accept volatility fail to remove? | The committed cash requirement | The existence of the portfolio | The trustee's stated preference | The manager's role | Risk willingness does not cancel the supplied payment obligation and its timing.
What has been authorized? | No allocation or trade has been approved | A complete equity allocation | A specific fund purchase | An unrestricted trading mandate | The brief explicitly leaves allocation, product choice, and trading authorization unapproved.''',
    vocabulary='''investment mandate | Agreed objectives, constraints, and authority for investment management. | define the investment mandate
investment policy statement | Document setting out investment objectives, constraints, and governance. | review the investment policy statement
investment objective | Financial aim the investment strategy is intended to pursue. | clarify the investment objective
time horizon | Period relevant to an investment goal or obligation. | distinguish the time horizon
liquidity requirement | Need for funds to be available at specified times. | identify the liquidity requirement
risk tolerance | Willingness and ability to bear investment risk in the relevant context. | assess risk tolerance
risk capacity | Financial ability to withstand loss or illiquidity. | distinguish risk capacity
return objective | Target outcome subject to risk and assumptions, not a guarantee. | qualify the return objective
capital preservation | Objective of protecting capital under the stated strategy and risks. | discuss capital preservation
spending policy | Rules governing distributions or expenditure from assets. | review the spending policy
investment constraint | Limit affecting permissible investment decisions. | document investment constraints
restricted asset | Holding subject to a relevant legal, contractual, or policy limitation. | identify restricted assets
discretionary authority | Authorized power to make specified decisions without separate approval each time. | confirm discretionary authority
client governing body | Body authorized to make decisions for the institutional client. | identify the client governing body
mandate amendment | Authorized change to the agreed investment instructions. | approve a mandate amendment
cash-flow schedule | Timetable of expected or committed cash movements. | reconcile the cash-flow schedule
liability matching | Relating assets or cash flows to specified obligations. | discuss liability matching
suitability assessment | Evaluation against the relevant client circumstances and applicable requirements. | complete the suitability assessment''',
    precision='A five-year objective does not give every dollar a five-year horizon. The committed six-month payment must remain visible in the mandate discussion.',
    precision_extra='This scenario selects no investment. A return objective is not a guarantee, and an intake conversation does not establish trading authority.',
    phrases='''Separate horizons | The growth objective and the committed payment have different time horizons.
Clarify liquidity | How much must be available, in which currency, and by what date?
Distinguish risk concepts | Willingness to accept volatility is not the same as capacity to miss the payment.
Confirm authority | Which body can approve the mandate and any changes?
Avoid a guarantee | That is an objective, not an assured return.
Record the constraint | The six-month payment needs to remain explicit in the instructions.
Check completeness | We need the full cash-flow schedule before assessing the proposal.
Close the intake | We have clarified requirements, not approved an allocation or trade.''',
    notes='''Need versus prefer | Need identifies an obligation or constraint; prefer identifies a choice that may be negotiable.
Target versus guarantee | A target describes an objective; a guarantee makes a much stronger promise and must not be implied.
Available by versus invested until | Available by identifies a liquidity deadline; invested until can imply a different period or restriction.''',
    d='''Which summary preserves the two horizons? | Five-year growth objective with a separate six-month payment need | All assets can be treated as unavailable for five years | The payment disappears if the trustee accepts volatility | Six months and five years are interchangeable planning periods | The correct summary retains both the long-term objective and the near-term obligation.
What should be clarified before an allocation discussion? | The cash-flow schedule, constraints, and decision authority | Only the most attractive recent return | Which fund has the shortest name | An assumption that all trustee comments authorize trades | Requirements and authority frame the actual mandate rather than a performance headline.
Which statement avoids an unsupported commitment? | The return figure is an objective subject to risk | The objective is guaranteed because it is written down | The payment will be met regardless of the assets chosen | A five-year plan eliminates all loss | An investment objective remains uncertain and does not become guaranteed through documentation.
Which status is accurate? | Mandate clarification is underway; allocation approval is outstanding | The manager can execute any trade immediately | A product has been selected and purchased | The governing body has approved every future change | The case supplies clarification only, with no completed investment authorization.''',
    dialogue='''Nora | The foundation wants growth over five years, and our trustees are comfortable with market volatility. Can we use that as the main instruction?
David | It is part of the [[investment mandate::The investment mandate includes objectives, constraints, and authority, not only a general willingness to accept volatility.]], but we also need the obligations, liquidity needs, and decision authority.
Nora | We have a committed payment of two million US dollars in six months. The rest supports longer-term programs.
David | That is a distinct [[liquidity requirement::The liquidity requirement identifies the funds needed for the committed six-month payment and must remain separate from the longer growth objective.]]. We should not give that obligation the same horizon as the five-year objective.
Nora | I had assumed a five-year plan meant we would not need to discuss any shorter period within the portfolio.
David | Different obligations can create more than one [[time horizon::The time horizon depends on the particular goal or obligation, so not every asset can automatically be treated as five-year money.]]. The plan needs to preserve those differences.
Nora | Our willingness to accept a temporary loss does not mean we can delay the committed payment if markets move against us.
David | Exactly. [[Risk capacity::Risk capacity concerns the financial ability to bear loss or illiquidity and is not settled solely by willingness to tolerate price movements.]] and willingness are related but different questions, especially when a payment cannot simply be postponed.
Nora | I can provide the payment schedule and identify any other distributions the trustees already expect to make.
David | A complete [[cash-flow schedule::The cash-flow schedule identifies the amounts and timing that the manager needs to understand before assessing the mandate and proposed allocation.]] will help us assess the actual constraints rather than relying on a single growth target.
Nora | One trustee suggested writing an eight-percent return into the instruction so the objective would be unambiguous.
David | We can clarify the [[return objective::The return objective is a target to evaluate against risk and constraints, not an assured result created by writing a percentage into the mandate.]], but documenting a target does not make the outcome guaranteed or remove investment risk.
Nora | The board must approve the policy, and our finance committee can recommend changes but cannot authorize them alone.
David | Then identify the [[client governing body::The client governing body identifies who has the relevant authority, preventing a recommendation from being mistaken for approval.]] and the approval route clearly so a committee discussion is not mistaken for a mandate change.
Nora | We also need to define which decisions you may make once the mandate is actually approved.
David | Yes. [[Discretionary authority::Discretionary authority is the specific decision-making power actually granted and must not be inferred from an introductory conversation.]] must be explicit; this conversation is not permission for me to trade immediately.
Nora | The policy document should bring the objective, cash need, restrictions, and governance together in one place.
David | That is the role of the [[investment policy statement::The investment policy statement records the agreed objectives, constraints, and governance, subject to the actual approval process.]], using the actual agreed instructions and keeping unresolved items visible.
Nora | I will return with the complete schedule and board requirements before we review any proposed allocation.
David | Then we can complete the appropriate [[suitability assessment::The suitability assessment evaluates the proposal against actual client circumstances and requirements rather than choosing an investment from incomplete intake information.]] and mandate process. We have clarified the questions, not selected a product, guaranteed a return, or authorized a trade.''',
    rehearsal=['Read the corrected intake and distinguish willingness, capacity, liquidity, and authority.', 'Switch roles and state the two supplied horizons and the exact payment amount without selecting an investment.'],
    transfer_title='A preferred target became an approved instruction', transfer_setup='A trustee suggests a revised return target in an email. The governing board has not approved a mandate amendment.',
    transfer='''Trustee: "The revised target is a ___." | proposal | The email suggests a change but does not establish the required approval.
Manager: "The mandate amendment is not yet ___." | authorized | The board has not approved the change under the supplied governance.
Trustee: "The board remains the decision ___." | authority | The governing board retains the approval role identified in the case.
Manager: "A target is not a return ___." | guarantee | A desired outcome does not become certain through a proposed instruction.'''))

BOOK['units'].append(unit(
    title='Explaining portfolio positioning and concentration', scene='Eight percentage points is not eight percent more',
    skill='Describe active weights, diversification, and risk limits using a consistent basis.',
    brief='Analyst Imani reviews a fictional portfolio with a technology weight of 28 percent against a benchmark weight of 20 percent. The difference is eight percentage points. The portfolio holds 40 securities, but several share exposure to the same technology demand driver. Portfolio manager Owen requests a risk review; no supplied rule establishes that the portfolio is compliant or that a trade must be made.',
    cast='Imani | Investment analyst\nOwen | Portfolio manager',
    culture=('Precision before persuasion', 'A confident positioning explanation should identify the reference point and risk driver. A long holdings list does not by itself establish balanced risk.'),
    a='''What is the technology active weight in percentage points? | Eight percentage points overweight | Eight percent relative overweight | Twenty-eight percentage points overweight | Forty percentage points underweight | Twenty-eight percent minus twenty percent equals eight percentage points.
Why does forty holdings not settle diversification? | Several share the same demand driver | Forty holdings always means no risk | The benchmark has no technology exposure | Every holding is necessarily a different asset class | The case identifies common exposure despite the number of securities.
What decision has been supplied? | A request for risk review | A mandatory trade instruction | A confirmed compliance conclusion | A guarantee against loss | The manager requests analysis without an established rule-based conclusion or trade.''',
    vocabulary='''asset allocation | Distribution of investments across asset categories. | review asset allocation
portfolio weight | Proportion of the portfolio allocated to a holding or category. | calculate the portfolio weight
benchmark weight | Proportion assigned to a category in the reference benchmark. | compare the benchmark weight
active weight | Difference between portfolio and benchmark weights. | explain the active weight
overweight | Allocation above the specified reference weight. | maintain an overweight position
underweight | Allocation below the specified reference weight. | describe an underweight position
percentage point | Unit expressing the arithmetic difference between percentages. | distinguish percentage points
basis point | One hundredth of a percentage point. | report the change in basis points
concentration risk | Risk from exposure clustered in a holding, sector, or common driver. | assess concentration risk
factor exposure | Sensitivity to an identified systematic driver. | examine factor exposure
correlation | Degree and direction of co-movement under a stated measure. | assess correlation
diversification | Distribution of exposure across investments or risk sources. | evaluate diversification
risk budget | Defined amount or allocation of risk under the investment process. | use the risk budget
tracking error | Measure of variability of active returns relative to a benchmark. | interpret tracking error
position limit | Stated maximum exposure to a holding or category. | check the position limit
rebalancing | Adjusting holdings toward specified target weights or constraints. | assess rebalancing
stress scenario | Specified adverse conditions used to examine potential effects. | run a stress scenario
look-through exposure | Underlying exposure identified beyond a fund or wrapper label. | review look-through exposure''',
    precision='28 percent minus 20 percent is eight percentage points, or 800 basis points. The relative increase against 20 percent would be 40 percent, a different measure.',
    precision_extra='Overweight is relative to a named reference. It does not itself establish a breach, a recommendation, or a guarantee of higher return.',
    phrases='''Name the reference | The technology weight is above the benchmark by eight percentage points.
Separate measures | That is a weight difference, not an eight-percent relative increase.
Explain the driver | Several holdings depend on the same technology spending cycle.
Look through the count | Forty securities do not necessarily mean forty independent risk sources.
Check the limit | Which mandate limit applies to this exposure?
Test the thesis | What happens under the specified demand-stress scenario?
Avoid a guarantee | Diversification does not eliminate the possibility of loss.
Define the next step | We need the risk analysis before deciding whether an adjustment is authorized.''',
    notes='''Overweight relative to | Always identify the benchmark or target; overweight without a reference is incomplete.
Percent versus percentage points | A relative percentage change divides by a base; a percentage-point difference subtracts percentages directly.
Could co-move versus will offset | Possible common movement does not establish a guaranteed offset or fixed future correlation.''',
    d='''Which statement labels the weight difference correctly? | Technology is eight percentage points above the benchmark | Technology is eight percent larger relative to the benchmark weight | Technology is twenty percent above the whole portfolio | Technology is eighty basis points overweight | The arithmetic difference is eight percentage points, equivalent to eight hundred basis points.
What should a diversification explanation examine? | Shared underlying risk drivers | Only the number of security names | Only whether the portfolio has a long report | An assumption that every name moves independently | Several holdings can share a driver, so count alone does not establish independent exposure.
What is needed before calling the weight a breach? | The applicable mandate or limit and its measurement basis | Only the fact that it is an overweight | The analyst's preference for a smaller number | A claim that all benchmarks are legal limits | A relative position is not automatically a breach without the actual governing limit.
Which conclusion matches the request? | Review the exposure and authorized options | Execute an unsupplied trade immediately | Promise that diversification prevents every loss | Declare every holding independent | The case calls for analysis and gives no trade authorization or universal risk conclusion.''',
    dialogue='''Imani | Technology is twenty-eight percent of the portfolio and twenty percent of the benchmark, so I described it as eight percent overweight.
Owen | Please say eight [[percentage points::Percentage points express the arithmetic difference between twenty-eight percent and twenty percent, not the relative percentage increase.]] above the benchmark. The reference and unit need to remain clear.
Imani | The relative increase against the twenty-percent benchmark weight would be forty percent, which answers a different question.
Owen | Exactly. For our positioning table, use the [[active weight::Active weight is portfolio weight minus benchmark weight, which is eight percentage points in the supplied example.]] and label it consistently so readers do not confuse the two calculations.
Imani | The portfolio contains forty securities. I had assumed that number was enough to describe it as well diversified.
Owen | Count is not the whole story. Review the [[factor exposure::Factor exposure identifies sensitivity to common underlying drivers, which can be shared by several differently named holdings.]] when several holdings depend on the same technology spending cycle.
Imani | A fall in that demand could affect several names together even though each is a separate company.
Owen | That is the [[concentration risk::Concentration risk can arise from clustered exposure to a common driver rather than only a large single holding.]] we need to explain, rather than treating every security as an independent source of risk.
Imani | Some exposure also sits inside a fund whose label does not make its technology holdings obvious.
Owen | Include the [[look-through exposure::Look-through exposure identifies the underlying holdings or drivers behind a fund wrapper rather than relying only on its label.]] so the discussion reflects the underlying positions, not just the names on the top-level report.
Imani | Should I call the overweight a breach before checking the mandate, since it is above the benchmark?
Owen | No. Verify the actual [[position limit::A position limit is the applicable maximum or constraint, which must be identified before a relative overweight can be called a breach.]] and measurement basis. A benchmark comparison is not automatically the governing limit.
Imani | We can model the supplied demand shock to show where losses cluster and which assumptions drive the result.
Owen | Use a clearly defined [[stress scenario::A stress scenario applies stated adverse assumptions to examine potential effects and should not be presented as a prediction of what must happen.]], and distinguish its hypothetical result from a forecast or a guarantee.
Imani | The team also wants to know whether the active position uses more risk than the committee intended.
Owen | Compare it with the actual [[risk budget::The risk budget is the risk allocation specified by the investment process and must be assessed using the relevant measures and assumptions.]] and explain the measures, rather than assuming weight alone answers every risk question.
Imani | If the analysis supports a change, we can discuss costs, liquidity, and the authority required before adjusting positions.
Owen | Yes. [[Rebalancing::Rebalancing is an actual adjustment toward targets or constraints and should follow the appropriate analysis and authorization rather than be inferred from a review request.]] is a decision, not an automatic consequence of using the word overweight.
Imani | I will report the eight-point active weight, shared drivers, relevant limits, and the results of the specified stress test.
Owen | Good. Explain [[diversification::Diversification distributes exposure but does not eliminate risk or establish that every holding will offset losses in another.]] without promising that holdings will always offset one another or that the portfolio cannot lose value.''',
    rehearsal=['Read the corrected exchange and state the eight-percentage-point difference and its 800-basis-point equivalent.', 'Switch roles and distinguish an overweight, a limit breach, and an authorized rebalance.'],
    transfer_title='The reference weight changed', transfer_setup='A portfolio weight stays at 25 percent. The benchmark weight rises from 20 to 23 percent. The active overweight therefore falls from five to two percentage points without a portfolio trade.',
    transfer='''Analyst: "The portfolio weight remained ___." | unchanged | The case keeps the portfolio weight at twenty-five percent throughout.
Manager: "The benchmark weight ___." | increased | The reference weight rose from twenty to twenty-three percent.
Analyst: "The active overweight is now two percentage ___." | points | Subtracting the twenty-three-percent benchmark from the twenty-five-percent portfolio weight gives two percentage points.
Manager: "That change does not prove a portfolio ___ occurred." | trade | The supplied difference changed through the benchmark, not an executed portfolio transaction.'''))

BOOK['units'].append(unit(
    title='Presenting performance on a comparable basis', scene='Gross outperformance is not the client net result',
    skill='Explain return measures, benchmark comparisons, and limitations without overstating performance.',
    brief='For the same fictional one-year period and reporting currency, a portfolio reports an 8 percent gross return and a 7 percent net return. Its stated benchmark return is 6 percent on the comparable basis supplied. A draft client slide claims two percentage points of net outperformance. The correct arithmetic net excess is one percentage point. The figures do not specify an individual investor\'s cash-flow experience or promise future results.',
    cast='Ravi | Performance analyst\nClaire | Client portfolio manager',
    culture=('Keep the qualification beside the number', 'A client should not need to discover the fee basis or measurement period in a distant footnote after hearing an overstated headline.'),
    a='''What is the stated net portfolio return? | 7 percent | 8 percent | 6 percent | 2 percent | The brief labels seven percent as net and eight percent as gross.
What is the arithmetic net excess over the benchmark? | One percentage point | Two percentage points | Seven percentage points | One percent relative increase | Seven percent minus six percent equals one percentage point on the supplied basis.
What is not established by these figures? | Every individual investor's cash-flow return | The stated one-year period | The stated gross return | The stated benchmark return | The brief provides portfolio measures, not each investor's separate contributions and withdrawals.''',
    vocabulary='''gross return | Return before the specified fee deductions in the stated methodology. | label the gross return
net return | Return after the specified deductions in the stated methodology. | present the net return
excess return | Difference between a return and its stated reference measure. | calculate excess return
total return | Return including the relevant price change and income under the methodology. | compare total returns
annualized return | Return expressed as an equivalent yearly rate under the stated method. | distinguish annualized return
cumulative return | Total change over the complete stated period. | report cumulative return
time-weighted return | Measure designed to reduce the effect of external cash-flow timing on performance. | explain time-weighted return
money-weighted return | Return measure reflecting the amount and timing of cash flows. | distinguish money-weighted return
performance attribution | Analysis assigning performance differences to defined effects. | review performance attribution
allocation effect | Attribution component associated with category-weight choices under the model. | explain the allocation effect
selection effect | Attribution component associated with security selection under the model. | identify the selection effect
interaction effect | Attribution component capturing joint effects under the chosen model. | label the interaction effect
reporting currency | Currency in which performance is expressed. | confirm the reporting currency
measurement period | Time interval covered by the performance calculation. | align the measurement period
composite | Group of portfolios defined for performance reporting under stated criteria. | explain the composite definition
drawdown | Decline from a prior value peak under the stated measure. | report the drawdown
volatility | Measure of return variability over the specified sample. | contextualize volatility
simulated performance | Model-based results rather than an actual live track record. | disclose simulated performance''',
    precision='Net excess is 7 percent minus 6 percent: one percentage point, or 100 basis points. Two points is the gross comparison, not the net comparison.',
    precision_extra='The gross-net difference does not alone specify a contractual fee rate. Methodology, included deductions, timing, and actual cash flows matter.',
    phrases='''Correct the headline | The two-point difference is gross; net excess is one point.
Keep the basis explicit | These are one-year returns in the stated reporting currency.
Align comparisons | We need the same period and a compatible return basis.
Distinguish experiences | Portfolio performance may differ from an investor's cash-flow return.
Explain attribution | This effect is defined by the attribution model, not a free-standing causal proof.
Avoid fee inference | The gross-net difference is not automatically the contractual fee rate.
Label the record | These results are simulated rather than a live account history.
Limit the promise | Past performance does not guarantee the next period's result.''',
    notes='''Net of which costs | Net needs the included deductions to be specified; it does not automatically mean after every tax and expense.
Annual versus annualized | Annual identifies a one-year period; annualized converts a different period into an equivalent yearly measure.
Outperformed by versus returned | Outperformed by gives a relative difference; returned gives the portfolio's own result.''',
    d='''Which slide headline is correct? | Net return 7 percent; benchmark 6 percent; net excess 1 percentage point | Net return 8 percent; net excess 2 points | Net excess equals the full 7 percent portfolio return | The portfolio guarantees 7 percent next year | This headline keeps the supplied net, benchmark, and arithmetic difference correctly labeled.
Which question clarifies net of fees? | Which deductions are included in this measure? | Can every deduction be assumed from the word net? | Does net mean there can be no loss? | Is the gross number always the investor's result? | The scope of deductions must be specified rather than inferred from the label alone.
Why might a client's cash-flow return differ? | The amount and timing of contributions and withdrawals can differ | The portfolio figures automatically describe every personal cash flow | Currency and period never matter | The benchmark changes the client's past deposits | Individual cash-flow experience is a different measurement question from the supplied portfolio figures.
Which presentation preserves fair interpretation? | Keep period, currency, fee basis, and limitations with the figures | Remove the net figure because gross is larger | Label simulated results as live | Use different periods without explanation | Relevant labels and limits let the audience interpret the performance comparison accurately.''',
    dialogue='''Ravi | The draft slide says we beat the benchmark by two percentage points net. I used eight minus six to prepare the headline.
Claire | Eight percent is the [[gross return::Gross return is the supplied eight-percent measure before its specified deductions, not the seven-percent net result.]]. The net figure is seven, so the headline has mixed the fee bases.
Ravi | Then the net comparison is seven minus six, which gives one percentage point rather than two.
Claire | Correct. State the [[excess return::Excess return is the difference from the stated benchmark, here one percentage point on the supplied net basis.]] with its basis so the client can distinguish portfolio return from benchmark-relative performance.
Ravi | I will show gross eight, net seven, and benchmark six together, rather than leave the net number out of the discussion.
Claire | Good. Also preserve the [[measurement period::The measurement period identifies the interval being compared and must match when interpreting the supplied performance figures.]] and [[reporting currency::The reporting currency identifies the currency used for the figures, which must remain consistent in the supplied comparison.]] so the three figures remain comparable.
Ravi | They all cover the same fictional year in the same currency. The methodology note identifies the deductions included in net.
Claire | Keep that note clear. [[Net return::Net return reflects the deductions included in the stated methodology and should not be assumed to include every possible tax or expense.]] does not automatically mean after every tax, expense, or individual investor circumstance.
Ravi | Could the one-point difference between gross and net be described as the contractual management-fee percentage?
Claire | Not from that subtraction alone. We need the actual fee terms and calculation details before making that separate claim.
Ravi | A client also asks why their account experience differs after making a large contribution midway through the year.
Claire | Their [[money-weighted return::Money-weighted return reflects the amount and timing of cash flows, which can differ from the portfolio measure shown in the report.]] can reflect cash-flow timing and size. Do not tell them the published portfolio number must describe every individual experience.
Ravi | We should explain which method the portfolio report uses and how that differs from the client's cash-flow question.
Claire | Yes. If discussing [[time-weighted return::Time-weighted return is designed to reduce the impact of external cash-flow timing and must be distinguished from a cash-flow-sensitive measure.]], explain its purpose rather than treating the method names as interchangeable labels.
Ravi | The attribution table separates category allocation and security selection, but the model definitions are not on the slide.
Claire | The [[performance attribution::Performance attribution decomposes results under a defined model and should retain its methodology rather than be presented as an unrestricted causal explanation.]] discussion needs enough context to show what those effects mean under the chosen method.
Ravi | We also have a separate backtest in the appendix. I will make sure it does not appear to be an additional live account.
Claire | Label [[simulated performance::Simulated performance comes from a model or backtest rather than an actual live record and must be identified accordingly.]] visibly, with its relevant limitations, instead of relying on a small ambiguous caption.
Ravi | The revised summary will report one-point net excess for the year, with the actual method and deductions identified.
Claire | Good. Include the relevant risk context, such as [[drawdown::Drawdown describes a decline from a prior peak and can provide context that a single positive period return does not reveal.]], without implying that past outperformance guarantees the next year's result.''',
    rehearsal=['Read the corrected exchange and distinguish the eight-percent gross, seven-percent net, and six-percent benchmark figures.', 'Switch roles and explain why one percentage point of net excess is not the same as the portfolio returning one percent.'],
    transfer_title='A three-year total was labeled annual', transfer_setup='A table supplies an 18 percent cumulative return over three years. No annualized calculation has been provided. The slide incorrectly calls it an 18 percent annual return.',
    transfer='''Analyst: "The supplied figure is ___." | cumulative | The figure describes the total return over the complete three-year period.
Manager: "It is not an eighteen-percent ___ return." | annual | The brief does not state that eighteen percent was earned in each year.
Analyst: "An annualized figure needs its own ___." | calculation | Converting the full-period result requires the appropriate method rather than relabeling it.
Manager: "Keep the three-year period ___." | explicit | The time interval must remain visible to avoid overstating the result.'''))

BOOK['units'].append(unit(
    title='Defending an investment thesis under committee challenge', scene='A model assumption is not a verified renewal',
    skill='Present a thesis, answer a skeptical question, and identify evidence that could change the decision.',
    brief='Analyst Sofia presents a fictional software-company investment thesis. The base case assumes 10 percent revenue growth; a downside scenario assumes 2 percent. Both depend on stated assumptions, and no scenario probabilities have been assigned. A key customer-retention input comes from management and is not independently verified. Committee chair Malik asks what evidence could invalidate the thesis. No investment approval is supplied.',
    cast='Sofia | Buy-side analyst\nMalik | Investment committee chair',
    culture=('Pushback is part of the analysis', 'A direct committee challenge can test the case without being a personal attack. Answer the assumption or evidence question rather than defend the presenter\'s status.'),
    a='''What growth does the base case assume? | 10 percent | 2 percent | A probability-weighted 6 percent | A guaranteed 12 percent | The brief explicitly assigns ten-percent growth to the base case.
What is the retention input's status? | Management-provided and independently unverified | Confirmed by every customer | A signed renewal for each contract | An audited future result | The input is attributed to management and has not been independently verified.
What cannot be calculated from the supplied scenario information alone? | A probability-weighted expected outcome | The difference between 10 and 2 | Which scenario is called downside | The stated base-case growth assumption | No probabilities are assigned, so a probability-weighted result is not supplied by the two scenarios.''',
    vocabulary='''investment thesis | Reasoned case for an investment under specified assumptions. | articulate the investment thesis
catalyst | Event or development expected to affect an investment case or valuation. | identify a potential catalyst
variant perception | View differing from the market or consensus assessment. | explain the variant perception
base case | Central scenario using the stated assumptions. | defend the base case
upside case | Scenario with specified more favorable assumptions. | distinguish the upside case
downside case | Scenario with specified adverse assumptions. | model the downside case
sensitivity analysis | Examination of how output changes when inputs change. | run sensitivity analysis
scenario analysis | Comparison of internally specified sets of assumptions. | present scenario analysis
probability weight | Assigned likelihood used in a probability-weighted calculation. | justify a probability weight
margin of safety | Buffer between an assessed value and price under a stated approach. | explain the margin of safety
thesis breaker | Evidence or event that would materially undermine the investment case. | define a thesis breaker
valuation range | Interval of estimated values under stated assumptions. | present a valuation range
discounted cash flow | Valuation method discounting projected cash flows under stated assumptions. | review the discounted cash flow
terminal value | Estimated value beyond an explicit forecast period. | test terminal value assumptions
discount rate | Rate used to convert future cash flows to present value. | justify the discount rate
free cash flow | Cash-flow measure defined after the relevant specified expenditures. | define free cash flow
position sizing | Determination of investment exposure within the portfolio process. | review position sizing
decision record | Account of the decision, rationale, conditions, and authority. | maintain a decision record''',
    precision='The base case is a scenario, not a forecast guarantee. A management retention estimate is not the same as independently confirmed customer renewals.',
    precision_extra='Two scenarios without probability weights do not establish a probability-weighted expected return. The exercise supplies no investment approval or trade instruction.',
    phrases='''State the thesis | The case depends on retention and the stated growth assumptions.
Answer the challenge | That input comes from management and remains unverified.
Define falsification | A material deterioration in the specified evidence would challenge the thesis.
Separate outputs | This is the base-case result, not a probability-weighted expectation.
Expose sensitivity | The valuation changes materially when that assumption changes.
Avoid a false buffer | A margin of safety depends on the valuation assumptions being credible.
Clarify authority | Committee discussion is not the same as investment approval.
Close the review | I will return with the evidence, revised sensitivities, and a clear decision request.''',
    notes='''Assumes versus demonstrates | Assumes identifies an input; demonstrates claims support from evidence or analysis.
Would versus will | Would describes a conditional effect; will states a prediction or commitment.
Base case versus expected value | A named central scenario and a probability-weighted calculation are different concepts.''',
    d='''Which response is evidence-conscious? | Management supplied the retention input; we still need verification | The model output proves renewals occurred | A confident presentation makes the input audited | Ten-percent growth is guaranteed because it is the base case | This response preserves source and uncertainty rather than treating an assumption as evidence.
What does a thesis breaker identify? | Evidence that would materially undermine the case | A reason to ignore all contrary information | A guaranteed future loss | The name of the committee presenter | A thesis breaker makes the conditions for reassessing the investment case explicit.
Which label fits the 2-percent scenario? | A downside case under stated assumptions | A certain future result | A weighted average of all outcomes | A trade authorization | The brief identifies a conditional downside scenario, not certainty or approval.
What should the decision record avoid? | Recording discussion as approval when no approval occurred | Naming unresolved evidence | Recording the actual conditions | Identifying the responsible follow-up | The record must preserve the actual authority and decision status supplied.''',
    dialogue='''Sofia | Our base case uses ten-percent revenue growth, supported by the retention profile management described in the presentation.
Malik | State the [[investment thesis::The investment thesis is the reasoned case and its dependencies, not merely a favorable model output or a management statement.]] before the valuation. Which evidence makes that growth assumption credible?
Sofia | The retention input comes from management, and we have not independently verified the underlying customer data.
Malik | Then the [[base case::The base case is a scenario built on specified assumptions and must not be presented as a verified or guaranteed future result.]] needs that qualification. A number inside the model does not become evidence because the spreadsheet calculates cleanly.
Sofia | I also modeled two-percent growth in the downside scenario to show how weaker demand changes the projected cash flows.
Malik | What changes together in that [[downside case::The downside case uses specified adverse assumptions, whose internal consistency and effects need explanation rather than a label alone.]]? We need a coherent scenario, not one lower revenue number with every other assumption left unexplained.
Sofia | I can show the stated cost and cash-flow assumptions separately and identify which inputs came from management or our analysis.
Malik | Good. Use [[sensitivity analysis::Sensitivity analysis shows how outputs respond to changes in inputs, making dependence on uncertain assumptions visible.]] to expose the variables that drive the result rather than hiding uncertainty inside a single valuation.
Sofia | A large share of the estimated value comes from cash flows beyond the explicit forecast period.
Malik | Then the [[terminal value::Terminal value estimates value beyond the explicit forecast and can make the result sensitive to long-run assumptions.]] assumptions deserve attention. A precise-looking output can still depend heavily on uncertain long-term inputs.
Sofia | I have not assigned probabilities to the two scenarios, so I should not call their simple midpoint our expected result.
Malik | Correct. A [[probability weight::A probability weight supplies the likelihood used in a weighted calculation; none has been assigned in the supplied case.]] needs a reasoned basis. Naming two cases does not create a probability-weighted forecast.
Sofia | The proposed investment depends on customer retention remaining consistent with the evidence we are trying to verify.
Malik | Identify a [[thesis breaker::A thesis breaker is evidence or an event that would materially undermine the case and prompt reassessment rather than automatic defense of the original view.]]. What finding would make you change the recommendation rather than explain every adverse result away?
Sofia | If the verified cohort data materially contradict the assumed retention pattern, I would revisit the growth and cash-flow case.
Malik | That is more useful than saying the valuation offers a [[margin of safety::A margin of safety is a buffer under an assessed valuation approach and does not make weak assumptions reliable by itself.]] without explaining whether the inputs supporting that valuation are credible.
Sofia | We should also assess the exposure in the context of the portfolio, not infer the investment size from my confidence alone.
Malik | Yes. [[Position sizing::Position sizing determines exposure under the portfolio's risk and mandate process and is not settled solely by analyst conviction.]] needs the actual risk, liquidity, and mandate considerations, alongside whatever conclusion the committee reaches.
Sofia | I will return with the verified evidence where available, the unresolved limitations, and the revised scenario comparison.
Malik | Record that request in the [[decision record::The decision record must state the actual review outcome and follow-up rather than transform a committee discussion into investment approval.]]. We have asked for further work; we have not authorized an investment or guaranteed any outcome.''',
    rehearsal=['Read the committee exchange and distinguish an assumption, evidence, a scenario, and an approval.', 'Switch roles and state the proposed thesis breaker using the supplied retention issue.'],
    transfer_title='The midpoint was called expected return', transfer_setup='A model has two unweighted scenarios. An analyst takes their arithmetic midpoint and labels it probability-weighted expected return. No likelihoods have been assigned.',
    transfer='''Analyst: "I calculated the arithmetic ___." | midpoint | The calculation averages the two scenario values without supplied likelihoods.
Chair: "No probability weights have been ___." | assigned | The brief explicitly leaves all scenario probabilities unspecified.
Analyst: "The expected-return label is therefore ___." | unsupported | The label implies a weighting basis that the supplied analysis does not establish.
Chair: "Keep the scenario outputs and their assumptions ___." | separate | The scenarios should remain identifiable rather than be combined under an unjustified probability claim.'''))

BOOK['units'].append(unit(
    title='Explaining enterprise value and the equity bridge', scene='The headline value is not the seller proceeds',
    skill='Reconcile a simplified valuation bridge and distinguish model inputs from verified transaction economics.',
    brief='Investment banker Eva explains an illustrative valuation to corporate client Theo. The model uses normalized EBITDA of USD 15 million at an 8-times multiple, implying enterprise value of USD 120 million. It then subtracts debt of USD 30 million and adds eligible cash of USD 10 million, giving equity value of USD 100 million. No other adjustments are included in this simplified bridge. The EBITDA normalization is still under diligence, and seller taxes, fees, and actual proceeds are not calculated.',
    cast='Theo | Corporate client\nEva | Investment banker',
    culture=('Reconcile before defending the headline', 'A client can reasonably confuse a transaction headline with money received. Walk through the bridge with consistent definitions before debating whether the valuation is attractive.'),
    a='''What enterprise value does the illustrative multiple imply? | USD 120 million | USD 100 million | USD 80 million | USD 15 million | Fifteen million of normalized EBITDA multiplied by eight gives one hundred twenty million.
What is the simplified equity value? | USD 100 million | USD 120 million | USD 160 million | USD 80 million | The supplied bridge subtracts thirty million of debt and adds ten million of eligible cash to one hundred twenty million.
Which conclusion is not supplied? | Actual seller proceeds after fees and taxes | The model enterprise value | The stated debt amount | The illustrative multiple | Fees, taxes, and actual seller proceeds are expressly outside the calculation.''',
    vocabulary='''enterprise value | Value measure for the operating business under the stated definition. | distinguish enterprise value
equity value | Value attributable to equity after the relevant bridge adjustments. | reconcile equity value
EBITDA | Earnings before interest, taxes, depreciation, and amortization under the stated calculation. | define EBITDA
normalized EBITDA | EBITDA adjusted for specified items under a stated normalization approach. | review normalized EBITDA
valuation multiple | Ratio applied to a specified financial metric. | select a valuation multiple
EV-to-EBITDA | Enterprise-value multiple of the defined EBITDA measure. | compare EV-to-EBITDA
add-back | Adjustment adding a specified item back to a financial metric. | substantiate an add-back
net debt | Defined debt less eligible cash under the stated calculation. | reconcile net debt
eligible cash | Cash included under the stated valuation or transaction definition. | verify eligible cash
debt-like item | Item treated like debt under a specified transaction definition. | identify debt-like items
cash-free debt-free | Transaction pricing convention requiring the actual terms to define its effect. | clarify cash-free debt-free pricing
equity bridge | Reconciliation from enterprise value to equity value. | prepare the equity bridge
comparable companies | Businesses used as reference points under a defined valuation comparison. | select comparable companies
precedent transactions | Earlier deals used in a valuation comparison. | analyze precedent transactions
diluted share count | Share count reflecting specified potential dilution under the method. | verify the diluted share count
noncontrolling interest | Ownership interest not attributable to the controlling parent under the relevant context. | assess noncontrolling interest
preferred capital | Capital carrying specified preferences under its actual terms. | account for preferred capital
seller proceeds | Amount actually received by sellers after relevant transaction effects. | distinguish seller proceeds''',
    precision='The supplied bridge is 15 x 8 = 120; then 120 - 30 + 10 = 100, all in USD millions. It excludes other adjustments by design.',
    precision_extra='Normalized EBITDA is not automatically cash flow or a verified sustainable earnings figure. Actual transaction definitions, diligence, fees, taxes, and other claims can alter the analysis.',
    phrases='''Label the headline | The one-hundred-twenty-million figure is enterprise value.
Show the bridge | Subtract thirty of debt and add ten of eligible cash.
Name the result | That gives one hundred million of equity value in this simplified example.
Separate proceeds | Equity value is not automatically the sellers' after-tax cash receipt.
Qualify the input | The normalization remains subject to diligence.
Avoid double counting | Do not subtract net debt and then subtract the same gross debt again.
Compare consistently | The multiple and earnings metric need a compatible basis.
Preserve exclusions | This illustration does not include other transaction adjustments.''',
    notes='''Value versus proceeds | Value is the stated valuation measure; proceeds concern the actual amount received after relevant effects.
Reported versus normalized | Reported identifies the source metric; normalized incorporates specified adjustments that need justification.
Gross debt versus net debt | Net debt already reflects the eligible-cash deduction under the chosen definition; combining both carelessly can double count.''',
    d='''Which bridge is correct for the supplied case? | 120 minus 30 plus 10 equals 100 | 120 plus 30 minus 10 equals 140 | 120 minus 30 minus 10 equals 80 | 120 plus 30 plus 10 equals 160 | Debt is subtracted and eligible cash added under the explicitly supplied simplified bridge.
What happens if net debt of 20 is subtracted and debt of 30 is then subtracted again? | The same debt is counted twice | The bridge becomes more conservative and therefore automatically correct | Eligible cash has been added twice | The EBITDA multiple changes to ten | Net debt already incorporates the supplied debt, so another debt deduction duplicates it.
Which input still needs diligence? | The EBITDA normalization | The fact that eight times fifteen equals 120 | The written currency label | The number of speakers | The case specifically identifies normalization as unverified rather than treating the model input as established.
Which client statement is too strong? | The sellers will receive exactly USD 100 million after every cost | The illustration implies enterprise value of 120 million | The simplified equity bridge gives 100 million | Fees and taxes are not calculated here | Actual proceeds are not supplied and cannot be guaranteed from this simplified equity value.''',
    dialogue='''Theo | The presentation says one hundred twenty million dollars. Is that what the shareholders will receive when the transaction closes?
Eva | That headline is [[enterprise value::Enterprise value is the operating-business valuation measure used here, not the amount automatically payable to shareholders after all transaction effects.]] in our illustration. We need to walk from that measure to equity value and then distinguish actual proceeds.
Theo | You arrived at the headline by multiplying fifteen million of normalized EBITDA by eight, correct?
Eva | Yes. Eight is the [[valuation multiple::The valuation multiple is applied to the specified earnings metric, so eight times fifteen million produces the illustrative one-hundred-twenty-million value.]] applied to the stated metric, with both the metric and the comparison basis requiring clear definitions.
Theo | The fifteen-million figure includes adjustments management proposed. I do not want the model to imply they have all been verified.
Eva | It should not. [[Normalized EBITDA::Normalized EBITDA includes specified adjustments whose justification remains subject to diligence, rather than being a verified cash-flow measure by definition.]] remains subject to diligence, and it is not the same thing as cash available to shareholders.
Theo | For the bridge, the example includes thirty million of debt and ten million of cash that is eligible under the stated definition.
Eva | Correct. The [[equity bridge::The equity bridge reconciles enterprise value to equity value using the specified adjustments, here subtracting debt and adding eligible cash.]] subtracts thirty from one hundred twenty and adds ten, giving one hundred million.
Theo | We could also describe the adjustment as subtracting twenty million of net debt, provided we use the same definition.
Eva | Exactly. [[Net debt::Net debt is thirty million of debt less ten million of eligible cash in this example, so subtracting twenty gives the same bridge result.]] is twenty in this simplified case. Do not then subtract the thirty again, because that would double count.
Theo | What makes the cash eligible? I know some transaction definitions distinguish accessible cash from restricted balances.
Eva | The actual terms determine [[eligible cash::Eligible cash is the cash included under the actual definition, so not every balance should automatically be added without review.]]. Here we explicitly supply ten for the exercise, but a real bridge needs the relevant definitions and verification.
Theo | The illustration says no other adjustments. Does that mean real transactions never have additional claims or price mechanisms?
Eva | No. A [[debt-like item::A debt-like item may be treated as debt under the actual transaction definition, but none is included in this deliberately simplified example.]] or other adjustment can matter in the actual terms. The illustration excludes them; it does not declare them irrelevant everywhere.
Theo | Then the one-hundred-million result is equity value under these supplied assumptions, not a complete closing statement.
Eva | Yes. [[Seller proceeds::Seller proceeds concern what sellers actually receive after relevant fees, taxes, and other transaction effects, which this example does not calculate.]] can differ because of costs, taxes, and other actual transaction effects not calculated here.
Theo | I also want the comparison slide to show whether the other deals use the same earnings definition and time period.
Eva | That is essential when using [[precedent transactions::Precedent transactions are comparison deals whose metrics and circumstances need alignment rather than assuming every reported multiple is directly comparable.]]. A similar headline multiple can conceal different metrics, periods, or deal circumstances.
Theo | I will summarize the model as illustrative enterprise value of one hundred twenty and equity value of one hundred, with normalization still under review.
Eva | Good. Keep [[equity value::Equity value is the result attributable to equity under the stated bridge and must remain distinct from both enterprise value and uncalculated net seller receipts.]], the unresolved inputs, and the uncalculated proceeds separate, so the board understands exactly what the numbers do and do not represent.''',
    rehearsal=['Read the corrected discussion and state the full bridge using USD millions.', 'Switch roles and explain why subtracting both net debt and the same gross debt would double count.'],
    transfer_title='Only the eligible cash amount changes', transfer_setup='Keep enterprise value at USD 120 million and debt at USD 30 million. Eligible cash is now USD 6 million. No other adjustments are included, so equity value is USD 96 million.',
    transfer='''Banker: "Enterprise value remains one hundred ___ million." | twenty | The scenario keeps the enterprise value at one hundred twenty million.
Client: "We subtract thirty million of ___." | debt | The debt deduction remains thirty million under the supplied bridge.
Banker: "We add six million of eligible ___." | cash | The eligible cash addition changes to six million in this case.
Client: "The simplified equity value is ninety-___ million." | six | One hundred twenty minus thirty plus six equals ninety-six million.'''))

BOOK['units'].append(unit(
    title='Challenging revenue quality in transaction diligence', scene='Repeat purchases are not necessarily contracted recurring revenue',
    skill='Distinguish reported revenue, customer concentration, and future contract evidence in a diligence update.',
    brief='In a fictional sell-side transaction, management reports USD 100 million of last-twelve-month revenue, including USD 30 million from one customer. A slide calls that customer revenue contracted recurring revenue. The data room contains past invoices but no reviewed renewal contract for the next period. Banker Lena and finance lead Omar must describe the gap without concluding that no contract exists or that all revenue will disappear.',
    cast='Omar | Company finance lead\nLena | Investment banker',
    culture=('A precise challenge need not accuse management', 'Ask which evidence supports the label. Distinguish an unanswered document request from proof that a commercial statement is false.'),
    a='''What share of reported revenue comes from the customer? | 30 percent | 3 percent | 70 percent | 100 percent | Thirty million divided by one hundred million equals thirty percent.
What documents are supplied in the data room? | Past invoices without a reviewed next-period renewal contract | Every signed future renewal | No evidence of any past billing | A legal opinion guaranteeing future revenue | The brief identifies historical invoices but no reviewed renewal contract for the next period.
What conclusion would overstate the gap? | No contract exists and all future revenue will disappear | Contract evidence remains to be reviewed | The customer is material to the revenue mix | The slide label needs support | A missing reviewed document does not prove absence of a contract or a certain revenue loss.''',
    vocabulary='''due diligence | Structured investigation supporting a transaction or decision. | conduct due diligence
quality of earnings | Analysis of the nature and sustainability of reported earnings. | review quality of earnings
data room | Controlled repository of transaction information. | update the data room
diligence request list | Record of information requested for the review. | maintain the diligence request list
last-twelve-month revenue | Revenue for the specified trailing twelve-month period. | reconcile last-twelve-month revenue
customer concentration | Dependence on revenue or business from a limited customer group. | assess customer concentration
contracted recurring revenue | Revenue described as recurring under actual contractual terms and definitions. | substantiate contracted recurring revenue
repeat purchase | Another purchase that does not alone establish a future contractual commitment. | distinguish repeat purchases
annual recurring revenue | Annualized recurring-revenue measure under the stated definition. | define annual recurring revenue
bookings | Value of orders or commitments recorded under a stated commercial definition. | reconcile bookings
backlog | Outstanding business or orders under the stated definition. | analyze backlog
deferred revenue | Accounting liability or balance for consideration before the relevant revenue recognition. | distinguish deferred revenue
net revenue retention | Retained revenue measure including specified expansion and losses from an existing cohort. | define net revenue retention
gross revenue retention | Retained revenue measure excluding specified expansion under the methodology. | compare gross revenue retention
customer cohort | Defined group of customers followed for analysis. | specify the customer cohort
revenue cutoff | Timing boundary for recognizing revenue in the relevant period. | test revenue cutoff
management representation | Statement supplied by management for the relevant purpose. | attribute management representations
diligence red flag | Issue requiring attention or further investigation during diligence. | escalate a diligence red flag''',
    precision='The customer contributes 30 percent of the supplied trailing revenue. Historical invoices establish a different evidential point from a reviewed future contractual commitment.',
    precision_extra='Missing from the reviewed data room does not mean nonexistent. Contract meaning, revenue recognition, and sustainability require appropriate legal, accounting, and commercial review.',
    phrases='''Test the label | What evidence supports calling this revenue contracted and recurring?
Separate periods | These invoices support past billing, not the next period's renewal.
Quantify concentration | This customer represents thirty percent of the supplied trailing revenue.
Avoid an accusation | We have not reviewed the contract; we have not established that no contract exists.
Request specifics | Please identify the agreement, relevant term, and any renewal conditions for review.
Align definitions | Bookings, backlog, and recognized revenue are not interchangeable.
Attribute the statement | That figure is management-provided and remains under diligence.
Report the gap | The document request is open, and the slide label needs qualification.''',
    notes='''Recurring versus repeated | Repeated describes past occurrences; recurring may imply a defined continuing revenue pattern or contract basis that needs support.
Unreviewed versus nonexistent | Unreviewed identifies the state of the investigation; nonexistent makes a factual claim that has not been established here.
Recognized versus collected | Revenue recognition and cash collection are different accounting events and may occur in different periods.''',
    d='''Which update best fits the evidence? | Past invoices reviewed; future contract support remains outstanding | All future revenue is contractually guaranteed | No contract exists anywhere | The customer cannot affect the valuation | This statement separates the verified historical material from the unresolved future-contract question.
Which numerical description is correct? | One customer accounts for 30 percent of trailing revenue | One customer accounts for 30 percentage points of profit | All revenue comes from that customer | The customer contributes 3 percent of revenue | The supplied amounts concern revenue, and thirty divided by one hundred is thirty percent.
What should the banker request? | The actual agreement and renewal terms for appropriate review | A more confident slide heading only | An assumption that invoices guarantee renewal | A legal conclusion from an unrelated customer | The label needs actual contractual and commercial evidence, not stronger presentation language.
Which terms should not be merged without reconciliation? | Bookings, backlog, and recognized revenue | The stated customer name and its exact identifier | Two identical copies of the same invoice | The same supplied currency label | These commercial and accounting measures have different definitions and cannot automatically be substituted.''',
    dialogue='''Omar | The customer has bought from us repeatedly, so the slide describes its thirty million dollars as contracted recurring revenue.
Lena | What supports that [[contracted recurring revenue::Contracted recurring revenue requires support from the actual contractual terms and definition rather than merely a history of purchases.]] label? We have reviewed invoices, but not a renewal agreement for the next period.
Omar | The invoices support the historical revenue. I agree they do not by themselves show the terms of a future commitment.
Lena | Exactly. A [[repeat purchase::A repeat purchase describes another historical transaction and does not alone establish a continuing contractual obligation for the next period.]] and a contractual renewal are different pieces of evidence.
Omar | Our total revenue for the trailing period is one hundred million, with thirty million from this customer.
Lena | That creates material [[customer concentration::Customer concentration concerns reliance on particular customers, here thirty percent of the supplied trailing revenue from one customer.]] to discuss: thirty percent of the supplied revenue comes from this relationship.
Omar | We should identify the period carefully, because the same slide also includes a current-year management forecast.
Lena | Keep [[last-twelve-month revenue::Last-twelve-month revenue is the historical trailing-period measure and must remain separate from a forward management forecast.]] separate from the forecast so the audience does not mistake projected sales for recognized historical revenue.
Omar | The commercial team may have the agreement in another approved location. Its absence from this folder does not prove it does not exist.
Lena | Correct. Update the [[diligence request list::The diligence request list tracks the actual missing information and its review status without turning an outstanding request into proof of nonexistence.]] with the precise document and terms needed for review.
Omar | I will ask for the agreement, any amendments, the relevant term, and the conditions governing renewal or termination.
Lena | Route them through the controlled [[data room::The data room is the authorized repository for transaction documents, supporting traceable access and review rather than uncontrolled sharing.]] and appropriate legal and commercial review, rather than emailing confidential material indiscriminately.
Omar | Another sheet uses bookings to support the same revenue number. We should not treat those figures as identical without checking.
Lena | Yes. [[Bookings::Bookings is a defined measure of orders or commitments and is not automatically the same as revenue recognized in the accounting period.]], backlog, and recognized revenue need their own definitions and reconciliation.
Omar | We also show a retention percentage, but I need to confirm whether it includes expansion from existing customers.
Lena | That matters for [[net revenue retention::Net revenue retention includes specified expansion and losses for a defined existing cohort, so its methodology must be stated rather than assumed.]]. Keep the cohort, period, and treatment of expansion clear before comparing it with another metric.
Omar | I can attribute the current contract description to management while making the evidence gap visible in the diligence update.
Lena | Good. A [[management representation::A management representation is a statement from management whose source should remain explicit while the relevant diligence is incomplete.]] should not become an independently verified fact merely because we repeat it in the transaction materials.
Omar | The revised note will quantify the concentration, distinguish history from forecast, and mark contract support as outstanding.
Lena | That is an appropriate [[diligence red flag::A diligence red flag identifies an issue needing attention and further work, not a final conclusion that the business claim is false or all future revenue will vanish.]] to investigate, without asserting that no agreement exists or predicting that every dollar of future revenue will disappear.''',
    rehearsal=['Read the corrected diligence exchange and distinguish invoices, renewals, bookings, and recognized revenue.', 'Switch roles and report the 30-percent concentration and the exact document gap without alleging an unsupplied outcome.'],
    transfer_title='An annualized month became a historical year', transfer_setup='One month records USD 3 million of revenue. A slide multiplies it by twelve to show a USD 36 million annualized run rate. Actual trailing-twelve-month revenue is separately supplied as USD 30 million.',
    transfer='''Analyst: "Thirty-six million is an annualized run ___." | rate | Multiplying one month by twelve creates an annualized measure, not a historical full-year total.
Banker: "The actual trailing revenue is ___ million." | thirty | The brief separately supplies thirty million as the historical trailing result.
Analyst: "The monthly figure does not establish future ___." | persistence | One month's revenue does not prove that the same level will continue.
Banker: "Keep the historical and annualized measures clearly ___." | labeled | Distinct labels prevent the extrapolation from being presented as realized history.'''))

BOOK['units'].append(unit(
    title='Explaining capital-raising demand and proceeds', scene='A one-and-a-half-times book is not cash received',
    skill='Distinguish indications, allocations, pricing, and issuer proceeds in an offering update.',
    brief='In a fictional offering illustration, the target gross deal size is USD 80 million: USD 60 million of new shares and USD 20 million sold by existing shareholders. Nonbinding indications of interest total USD 120 million on the same provisional pricing basis. No final allocation, pricing, or settlement has occurred. Fees and expenses are excluded from the figures.',
    cast='Mina | Issuer finance director\nJames | Capital-markets banker',
    culture=('A strong update can still preserve contingencies', 'Report demand confidently without treating indications as commitments or total deal size as cash available to the issuer.'),
    a='''What is the gross primary component for the issuer? | USD 60 million | USD 80 million | USD 120 million | USD 20 million | The new-share component is sixty million; the twenty-million secondary component goes to selling holders before costs.
What does the USD 120 million figure describe? | Nonbinding indications on the provisional basis | Settled cash received by the issuer | Final allocated shares already paid for | Guaranteed net proceeds | The case explicitly labels the amount as nonbinding indications rather than settled proceeds.
Which stages are unfinished? | Final allocation, pricing, and settlement | The initial target-size discussion | The identification of primary and secondary components | The arithmetic total of the two components | The brief expressly states that allocation, pricing, and settlement have not occurred.''',
    vocabulary='''issuer | Entity offering the relevant securities. | identify the issuer
underwriter | Financial institution performing the role defined in an offering arrangement. | confirm the underwriter role
bookbuilding | Gathering investor demand information for an offering. | conduct bookbuilding
indication of interest | Expression of potential investor demand under stated conditions. | record an indication of interest
order book | Compilation of demand information under the offering process. | assess the order book
allocation | Assignment of offered securities under the actual process. | confirm the allocation
primary shares | Newly issued shares sold by the company in the offering. | distinguish primary shares
secondary shares | Existing shares sold by current holders in the offering. | identify secondary shares
issuer proceeds | Funds received by the issuing company under the actual offering economics. | reconcile issuer proceeds
offering price | Price at which securities are sold in the offering. | agree the offering price
price range | Stated range used during the relevant offering stage. | update the price range
roadshow | Investor presentation process under applicable offering rules. | prepare the roadshow
prospectus | Offering disclosure document under the applicable securities framework. | review the prospectus
registration statement | Filing containing disclosures for the relevant registered offering process. | identify the registration statement
underwriting agreement | Contract defining the parties' offering obligations. | review the underwriting agreement
firm commitment | Underwriting arrangement with purchase obligations defined by the actual agreement. | distinguish firm-commitment underwriting
best efforts | Arrangement defined by its actual terms without assuming a firm purchase commitment. | clarify best-efforts terms
overallotment option | Option for additional securities under the specified offering arrangement. | explain the overallotment option''',
    precision='The indicative book is 120 divided by 80, or 1.5 times the target on the supplied basis. It is not settled cash. Gross issuer proceeds from new shares are 60, not the total 80.',
    precision_extra='Offering terms, permitted communications, investor eligibility, commitments, pricing authority, and settlement depend on the actual transaction and law. No offering is being recommended or conducted here.',
    phrases='''Label the demand | These are nonbinding indications on the current provisional basis.
Quantify carefully | The indicated book is one and a half times the target size.
Separate proceeds | The secondary component goes to selling shareholders, not the issuer.
Preserve conditions | Demand may change with price and final terms.
Clarify status | Allocation and pricing are not final, and settlement has not occurred.
Define the commitment | We need the actual underwriting agreement, not an assumption from the bank's involvement.
Avoid endorsement language | Regulatory effectiveness is not an endorsement of the investment's merits.
Close the update | We can report indicated demand while keeping funding and execution risk visible.''',
    notes='''Indicated versus committed | Indicated expresses potential demand under its actual terms; committed requires the relevant binding status.
Gross versus net proceeds | Gross precedes the specified costs; net depends on the actual deductions.
Primary versus secondary | Primary sales involve new issuer shares; secondary sales involve existing holders selling their shares in this case.''',
    d='''Which demand statement is accurate? | Indications equal 1.5 times the target on the provisional basis | The issuer has received 120 million in cash | Every indication is a final binding allocation | The target automatically increases to 120 million | One hundred twenty divided by eighty is one and a half, but the indications remain nonbinding.
Which statement separates offering components? | Sixty million is primary and twenty million is secondary before costs | All eighty million goes to the issuer | All proceeds go to existing shareholders | Secondary means a second deposit into the issuer account | The case identifies new-share and existing-holder components with different recipients.
What can the banker not infer from a large book alone? | Final price, allocation, and settled funding | The supplied indicative amount | The stated target size | The arithmetic coverage ratio | Demand indications do not establish the unfinished execution stages or funding outcome.
Which document defines underwriting obligations? | The actual underwriting agreement | A headline saying the book is strong | An unrelated investor's portfolio report | The issuer's preferred press headline | The commitment depends on the actual contract and framework, not the appearance of bank involvement.''',
    dialogue='''Mina | We have one hundred twenty million dollars of interest for an eighty-million-dollar offering. Can we announce that the funding is secured?
James | Not from these [[indications of interest::Indications of interest express potential demand and are nonbinding in this case, so they do not establish secured funding.]]. The demand is nonbinding and uses the current provisional pricing basis.
Mina | We can still describe the indicated book as one and a half times the target, provided those qualifications stay attached.
James | Yes. The [[order book::The order book compiles the stated demand information, which remains distinct from final allocation, binding commitments, or settled cash.]] is a useful demand signal, not a record of cash already received.
Mina | The target consists of sixty million of new shares and twenty million sold by existing shareholders.
James | Then the [[primary shares::Primary shares are newly issued shares sold by the company, accounting for the sixty-million gross issuer component in this illustration.]] generate the issuer component, while the existing-holder sale is separate.
Mina | Some colleagues have described the full eighty million as money available for the company's expansion plan.
James | That ignores the [[secondary shares::Secondary shares are sold by existing holders, so their sale proceeds do not automatically become funds available to the issuer.]]. The twenty-million component goes to the selling shareholders before the relevant costs.
Mina | We also have not deducted fees or expenses, so even the sixty-million issuer figure is gross.
James | Correct. [[Issuer proceeds::Issuer proceeds concern funds received by the company under the actual offering economics and need gross-versus-net and primary-versus-secondary distinctions.]] need both distinctions: who receives the money and which deductions the figure includes.
Mina | Investors may change their demand when they see the final price or terms, even if the initial conversations were encouraging.
James | Exactly. The final [[offering price::The offering price is the actual price set for the securities, which has not yet been finalized in the supplied case.]] and terms are not established merely by the current demand total.
Mina | The team should also avoid telling an interested investor that a specific amount is reserved before the allocation process is complete.
James | Yes. [[Allocation::Allocation assigns the offered securities under the actual process and remains unfinished despite preliminary expressions of interest.]] is a separate stage, and any statement must reflect the actual authority and status.
Mina | Does the bank's involvement mean it is automatically obligated to purchase any securities investors do not take?
James | We need the [[underwriting agreement::The underwriting agreement defines the actual purchase or distribution obligations rather than allowing them to be inferred from bank involvement alone.]]. The role and commitment depend on its terms, not on a general label.
Mina | We will use the reviewed offering materials rather than improvise claims about guaranteed demand or future trading performance.
James | Good. The [[prospectus::The prospectus contains the relevant offering disclosures and should not be replaced by unsupported assurances in informal communications.]] and other authorized communications need to be consistent with the actual facts and applicable rules.
Mina | My update will say indicated demand is 1.5 times the target, with pricing, allocation, and settlement still outstanding.
James | That accurately describes [[bookbuilding::Bookbuilding gathers and evaluates investor demand during the offering process; it is not equivalent to completing the raise or receiving settled proceeds.]] progress while preserving execution uncertainty and the difference between the total deal and the issuer's gross primary proceeds.''',
    rehearsal=['Read the corrected update and distinguish 120 of indications, 80 of total size, and 60 of gross primary proceeds.', 'Switch roles and explain why the 20-million secondary component is not issuer funding.'],
    transfer_title='Interest fell when the terms changed', transfer_setup='After a revised provisional price, nonbinding indications fall from USD 120 million to USD 90 million against the same USD 80 million target. No settlement occurs.',
    transfer='''Banker: "The indicated demand has ___." | decreased | The amount falls from one hundred twenty to ninety million under the revised basis.
Issuer: "The target remains eighty ___." | million | The scenario keeps the target size at eighty million dollars.
Banker: "The indications are still ___." | nonbinding | The revised figure retains the nonbinding status expressly supplied.
Issuer: "This is not confirmation of ___ funding." | settled | No settlement has occurred, so the demand update does not establish received funds.'''))

BOOK['units'].append(unit(
    title='Protecting the boundary between banking and investment teams', scene='A public rumor does not release a private fact',
    skill='Decline an improper information request and route uncertainty through compliance without confirming confidential details.',
    brief='Banking analyst Dev works on confidential transaction material. A colleague in an investment team asks whether a public acquisition rumor is true, hoping to inform a portfolio decision. Dev has not been authorized to share the material or confirm the transaction. Compliance officer Rosa explains the need to preserve information barriers and use the actual escalation process. The case supplies no legal determination that information is public or permission to trade.',
    cast='Dev | Investment-banking analyst\nRosa | Compliance officer',
    culture=('A professional boundary is not personal distrust', 'Decline the information request clearly without accusing the colleague or giving a hint that confirms the confidential fact. Shared employment does not create universal access.'),
    a='''Why is the public rumor insufficient here? | It does not authorize confirmation from confidential material | Every rumor makes all deal information public | It automatically permits a portfolio trade | It cancels the client confidentiality obligation | Speculation in public does not itself release private information or authorize confirmation.
Who requested the information? | A colleague in an investment team | The authorized deal client through its agreed process | A public filing system | A regulator whose request has been verified | The brief identifies an internal investment colleague seeking information for a portfolio decision.
What permission is supplied? | No permission to disclose or trade | Unrestricted internal sharing | Automatic permission to confirm the rumor | A legal determination that all material is public | The case explicitly leaves disclosure and trading permission unestablished.''',
    vocabulary='''material nonpublic information | Nonpublic information meeting the relevant materiality standard. | identify potential material nonpublic information
information barrier | Controls separating access and communication between activities. | maintain the information barrier
need-to-know access | Access limited to a legitimate authorized purpose. | restrict need-to-know access
wall-crossing | Controlled process for bringing someone inside an information boundary under actual rules. | follow the wall-crossing process
restricted list | Controlled list used for specified compliance restrictions. | follow restricted-list controls
watch list | Controlled monitoring list under the firm's actual compliance framework. | protect watch-list confidentiality
preclearance | Required review or authorization before a specified activity. | obtain required preclearance
conflict of interest | Competing interest that may affect duties or judgment. | identify a conflict of interest
client confidentiality | Duty or obligation to protect relevant client information. | preserve client confidentiality
selective disclosure | Sharing information with a limited audience under circumstances needing legal or policy review. | assess selective-disclosure concerns
public dissemination | Distribution making information public under the relevant standard. | verify public dissemination
compliance escalation | Routing an issue to the designated compliance process. | initiate compliance escalation
deal team | Group authorized for the relevant transaction work. | identify the authorized deal team
public-side research | Research using information permitted for the relevant public-side activity. | use public-side research
restricted access log | Record of controlled access to sensitive materials. | maintain the restricted access log
trade restriction | Limit on trading under applicable law or controls. | observe a trade restriction
accidental receipt | Unintended receipt of information or material. | report accidental receipt
record preservation | Keeping relevant records intact under the applicable process. | follow record-preservation requirements''',
    precision='A rumor and an authorized public disclosure are different. Confirming a rumor from private deal knowledge can itself disclose sensitive information.',
    precision_extra='Do not improvise a legal materiality judgment, disclose list status, or assume that consent from a colleague removes restrictions. Follow actual legal and compliance requirements before action.',
    phrases='''Decline without hinting | I cannot confirm or discuss confidential transaction information.
Name the boundary | My access for banking work does not authorize sharing with the investment team.
Route the question | Please use the designated compliance process for that request.
Avoid rumor logic | A public rumor does not make our private information public.
Preserve uncertainty | We need the appropriate review before treating the information as cleared.
Limit distribution | Do not forward the material beyond the authorized recipients.
Report an error | I received this unintentionally and have contacted the appropriate compliance team.
Keep roles distinct | Portfolio analysis must use information permitted for that activity.''',
    notes='''Cannot confirm versus probably true | Cannot confirm maintains the boundary; probably true can leak a substantive hint.
Publicly rumored versus publicly disclosed | A rumor may be public while the underlying verified fact remains nonpublic.
Internal versus authorized | Internal identifies organizational location; authorized identifies permission for the actual access or use.''',
    d='''Which reply maintains the boundary? | I cannot confirm confidential matters; please use compliance | The rumor is basically right, but do not quote me | We work here, so all information is shared | I will send the slide without the client name | This response avoids confirmation or leakage and routes the request appropriately.
What should determine access? | The legitimate authorized purpose and applicable controls | Curiosity about a colleague's deal | Shared employment alone | The possibility of a better portfolio return | Need-to-know access depends on purpose and authority, not mere internal status.
What should happen after accidental receipt of sensitive material? | Report promptly through the actual process and preserve records as directed | Forward it to test whether others think it is important | Trade before anyone classifies it | Delete the history to avoid a record | The appropriate response is controlled escalation and record handling rather than dissemination, trading, or concealment.
Which statement about a rumor is correct? | Public speculation does not itself authorize private confirmation | Any news mention removes every restriction | A colleague can waive client confidentiality informally | A hint is harmless if the full document stays private | A confirmation or hint can disclose information even without forwarding the source document.''',
    dialogue='''Dev | A colleague on the investment team asked whether an acquisition rumor is true. They know I work on confidential transaction material.
Rosa | Do not confirm or hint at the answer. Your [[client confidentiality::Client confidentiality protects the relevant transaction information and is not removed by an internal colleague's interest in a public rumor.]] obligations remain relevant even when the question starts with public speculation.
Dev | I was going to say I could not send the documents but could give a quick verbal sense of whether the story was accurate.
Rosa | That could still cross the [[information barrier::The information barrier governs communication and use, so a verbal hint can breach the boundary even when documents are not forwarded.]]. Protecting the attachment while revealing its substance does not preserve the boundary.
Dev | The colleague argues that we work for the same organization and that the information could improve a portfolio decision.
Rosa | Shared employment does not establish [[need-to-know access::Need-to-know access depends on a legitimate authorized purpose, not merely on being employed by the same organization or wanting a trading advantage.]] for that activity. Banking access and portfolio-research access serve different authorized purposes.
Dev | I should decline without saying anything that confirms whether the rumored transaction is one of our confidential matters.
Rosa | Exactly. Use [[compliance escalation::Compliance escalation routes the uncertainty to the designated review process without letting the employee improvise permission to disclose or use the information.]] for the request rather than decide on your own that an informal answer is harmless.
Dev | Does a newspaper rumor mean the information is now public enough for the team to use without further checking?
Rosa | A rumor is not proof of [[public dissemination::Public dissemination concerns whether the relevant information has actually become public under the applicable standard, which speculation alone does not establish.]] of the verified facts. The actual information and legal or policy position need review.
Dev | We should treat the material as potentially sensitive rather than make our own quick conclusion that it could not matter to investors.
Rosa | Correct. Potential [[material nonpublic information::Material nonpublic information requires the relevant legal assessment; uncertainty is not permission to disclose or trade on confidential transaction knowledge.]] must be handled through the actual controls, not through an improvised materiality judgment.
Dev | If there were a legitimate reason to involve someone from another team, the access process would need to be followed first.
Rosa | Yes. Any [[wall-crossing::Wall-crossing is a controlled process under actual rules, not informal permission created by a colleague asking to hear the information.]] must follow the firm's requirements and applicable law, including the consequences for the person's activities.
Dev | I also should not reveal whether the company appears on a confidential monitoring or restriction list.
Rosa | Correct. A [[restricted list::A restricted list is itself controlled compliance information and its status should not be disclosed casually as an indirect hint about a confidential matter.]] or monitoring status can carry sensitive information; follow the actual handling rules.
Dev | I will tell the colleague I cannot confirm confidential matters and that their question needs the designated compliance route.
Rosa | Good. Their [[public-side research::Public-side research must use information permitted for that activity, not confidential banking knowledge passed informally across the boundary.]] should remain based on information permitted for that role and its applicable restrictions.
Dev | If material is accidentally sent across the boundary, I will report it promptly rather than forward it or erase the history.
Rosa | Follow the actual [[record preservation::Record preservation keeps relevant evidence intact under the appropriate process and avoids concealment after an accidental disclosure or receipt.]] and access instructions. A clear boundary and timely escalation protect the client and both teams without requiring you to make an unauthorized legal decision.''',
    rehearsal=['Read the corrected conversation and practice the refusal without adding a hint about the transaction.', 'Switch roles and distinguish internal employment, authorized access, and public dissemination.'],
    transfer_title='The wrong recipient received a deck', transfer_setup='An employee accidentally receives a confidential transaction deck intended for another team. No permission to use or redistribute it is supplied.',
    transfer='''Employee: "This appears to be an accidental ___." | receipt | The material reached the employee unintentionally and does not establish authorized use.
Compliance: "Do not ___ it beyond the authorized process." | redistribute | The case provides no permission to circulate the confidential deck further.
Employee: "I will report the issue through the designated ___." | channel | The actual compliance route should handle the incident and next steps.
Compliance: "Follow the applicable record-preservation ___." | instructions | Relevant records should be handled under the proper process rather than concealed or altered.'''))
