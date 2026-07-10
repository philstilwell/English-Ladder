from __future__ import annotations

import html
from pathlib import Path

from reportlab.platypus import PageBreak, Paragraph, Spacer

from generate_efsp_guarded_activities import add_answer_key, add_cloze_exercise, make_dialogue_cloze
from generate_efsp_culture_pdfs import (
    S,
    box,
    build_pdf,
    bullets,
    h1,
    h2,
    h3,
    lines,
    p,
    rule,
    table,
)


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "pdf" / "efsp"


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def cover(title: str, subtitle: str, audience: str) -> list:
    return [
        Spacer(1, 0.95 * 72),
        p("EFSP Auxiliary ESL Curriculum", "CoverKicker"),
        Paragraph(esc(title), S["CoverTitle"]),
        Paragraph(esc(subtitle), S["CoverSub"]),
        Spacer(1, 0.25 * 72),
        box(
            audience,
            [
                "Focus: high-level professional English for finance workplaces, including financial statements, FP&A, treasury, banking, investment analysis, valuation, risk, audit, controls, compliance, and realistic finance dialogue.",
                "Designed for advanced ESL learners who already work in accounting, FP&A, treasury, banking, investment management, corporate finance, audit, risk, investor relations, or finance-adjacent roles.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: this is finance English training, not investment, tax, accounting, banking, or legal advice. Standards, regulations, products, and disclosure requirements vary by jurisdiction and role. Learners should practice precise language and professional judgment while relying on qualified finance, accounting, legal, tax, and compliance guidance for actual decisions.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use finance terminology accurately in close meetings, forecast reviews, treasury calls, audit discussions, investment committee meetings, credit reviews, board updates, and client conversations.",
    "Explain financial performance using drivers, variances, bridge logic, assumptions, run rate, one-time items, seasonality, mix, timing, and confidence level.",
    "Discuss financial statements, liquidity, working capital, debt, covenants, valuation, investment risk, and controls in concise professional English.",
    "Push back on weak assumptions, aggressive forecasts, unsupported add-backs, misleading performance claims, or risky shortcuts using evidence and audience-appropriate language.",
    "Participate in realistic finance dialogues: budget challenge, cash runway review, covenant monitoring, audit issue escalation, portfolio performance review, M&A diligence, and board-level liquidity update.",
    "Write clear finance outputs: variance commentary, forecast notes, investment summaries, covenant updates, control memos, risk statements, and executive finance briefings.",
]


MODULES = [
    {
        "title": "Module 1. Finance Communication: Drivers, Assumptions, Materiality, Risk",
        "time": "90 minutes",
        "big_idea": "Finance English is decision language. Strong learners do not only state numbers; they explain what changed, why it changed, whether it matters, what is recurring, and what decision follows.",
        "objectives": [
            "Separate result, driver, assumption, estimate, risk, and recommendation.",
            "Use materiality and confidence language without hiding uncertainty.",
            "Convert vague finance questions into answerable analysis tasks.",
        ],
        "concepts": [
            "Driver: an underlying factor that moves a metric, such as price, volume, mix, churn, utilization, rate, or cost inflation.",
            "Materiality: whether a difference, risk, or error matters enough to affect decisions or reporting judgment.",
            "Estimate vs actual: finance work often compares assumptions, forecasts, accruals, and actual results.",
        ],
        "activities": [
            "Number-to-story drill: learners turn a table of results into three business drivers and one recommended action.",
            "Materiality debate: learners decide which variances require executive attention and which can stay in appendix detail.",
            "Assumption challenge: learners rewrite vague statements into testable assumptions with source, owner, and sensitivity.",
        ],
        "outputs": [
            "Finance driver sentence bank.",
            "Assumption and confidence checklist.",
            "Decision-grade variance comment.",
        ],
    },
    {
        "title": "Module 2. Financial Statements, Close, and Accounting Judgments",
        "time": "90 minutes",
        "big_idea": "Financial statement conversations require precise links among income statement, balance sheet, cash flow, notes, accruals, revenue recognition, reserves, and internal controls.",
        "objectives": [
            "Explain the three main financial statements and how they connect.",
            "Use accounting-close terms such as accrual, deferral, reserve, reconciliation, adjusting entry, and cut-off.",
            "Discuss accounting judgment without sounding either casual or alarmist.",
        ],
        "concepts": [
            "Accrual accounting records revenue and expenses when earned or incurred, not only when cash moves.",
            "Working capital connects operations to cash through receivables, inventory, payables, and timing.",
            "Revenue recognition, fair value, impairments, reserves, and contingencies can require judgment and documentation.",
        ],
        "activities": [
            "Statement connection map: learners explain how a sale on credit affects revenue, receivables, cash flow, and working capital.",
            "Close meeting role-play: learners explain why an accrual changed and what evidence supports it.",
            "Judgment memo rewrite: learners convert informal accounting language into audit-ready language.",
        ],
        "outputs": [
            "Financial statement explainer.",
            "Close issue update template.",
            "Accounting judgment phrase bank.",
        ],
    },
    {
        "title": "Module 3. FP&A, Budgeting, Forecasting, and Variance Analysis",
        "time": "90 minutes",
        "big_idea": "FP&A conversations live between accounting truth and business uncertainty. Learners need language for budget vs actuals, forecast risk, bridge analysis, sensitivity, scenarios, guidance, and management action.",
        "objectives": [
            "Explain budget, forecast, outlook, guidance, run rate, bridge, and variance.",
            "Challenge business-owner assumptions respectfully and specifically.",
            "Write variance commentary that identifies driver, magnitude, timing, recurrence, and mitigation.",
        ],
        "concepts": [
            "Variance: the difference between actual result and budget, forecast, prior period, or benchmark.",
            "Bridge: a structured explanation that walks from one number to another through drivers.",
            "Scenario and sensitivity: testing how results change if assumptions move.",
        ],
        "activities": [
            "Forecast review: learners challenge sales, hiring, cost, churn, and margin assumptions.",
            "Bridge building: learners create a revenue bridge from prior quarter to current forecast.",
            "Executive commentary: learners condense a detailed variance file into a CFO-ready paragraph.",
        ],
        "outputs": [
            "Variance commentary template.",
            "Forecast challenge question set.",
            "Scenario explanation script.",
        ],
    },
    {
        "title": "Module 4. Treasury, Cash, Liquidity, Working Capital, and FX",
        "time": "90 minutes",
        "big_idea": "Treasury language connects operations, banking relationships, liquidity risk, funding strategy, covenant compliance, and market exposure. Cash is not the same as profit.",
        "objectives": [
            "Discuss cash runway, liquidity, revolver availability, covenants, DSO, DPO, inventory, and free cash flow.",
            "Explain why EBITDA, net income, and cash flow can move differently.",
            "Use FX, interest-rate, and hedging language in business-facing conversations.",
        ],
        "concepts": [
            "Liquidity: ability to meet obligations when due without unacceptable loss or disruption.",
            "Covenant: a contractual requirement in a financing agreement, often tied to leverage, coverage, reporting, or restricted actions.",
            "Hedge: a position or contract intended to reduce exposure to risk such as FX or interest-rate movements.",
        ],
        "activities": [
            "Cash runway meeting: learners explain burn, collections, payables, financing options, and tradeoffs.",
            "Covenant monitoring drill: learners identify when forecast changes may create compliance risk.",
            "FX exposure role-play: learners explain transaction exposure and hedge cost to a sales leader.",
        ],
        "outputs": [
            "Liquidity update template.",
            "Covenant risk script.",
            "FX exposure explanation.",
        ],
    },
    {
        "title": "Module 5. Markets, Investments, Performance, and Client Communication",
        "time": "90 minutes",
        "big_idea": "Investment conversations require language for return, risk, benchmark, attribution, volatility, liquidity, duration, yield, spread, allocation, fees, and fair performance presentation.",
        "objectives": [
            "Explain market and portfolio performance without overstating causation.",
            "Use fixed income and equity vocabulary in client-safe language.",
            "Discuss underperformance, benchmark deviation, and risk exposure with credibility.",
        ],
        "concepts": [
            "Return vs risk: performance must be understood relative to volatility, drawdown, liquidity, benchmark, and objective.",
            "Duration: a bond portfolio's sensitivity to interest-rate changes, often discussed with yield and spread.",
            "Attribution: analysis that explains which decisions or exposures contributed to performance.",
        ],
        "activities": [
            "Performance review: learners explain a portfolio that underperformed its benchmark but followed its risk mandate.",
            "Market update: learners summarize rate moves, spread widening, equity sector rotation, and liquidity conditions.",
            "Client concern role-play: learners respond to a client who wants to sell after a volatile month.",
        ],
        "outputs": [
            "Performance attribution script.",
            "Market update template.",
            "Client-safe risk explanation.",
        ],
    },
    {
        "title": "Module 6. Banking, Credit, Lending, and Counterparty Risk",
        "time": "90 minutes",
        "big_idea": "Credit conversations are evidence-driven. Learners need language for borrower capacity, leverage, collateral, covenant package, probability of default, loss given default, concentration, and stress case.",
        "objectives": [
            "Use credit terms accurately in underwriting, portfolio review, and borrower conversations.",
            "Explain why a profitable borrower can still be a weak credit.",
            "Discuss downside cases, collateral gaps, and covenant protections without sounding accusatory.",
        ],
        "concepts": [
            "Credit risk: risk that a borrower or counterparty fails to meet obligations.",
            "Debt service coverage: whether cash flow is sufficient to cover required debt payments.",
            "Collateral and guarantees may reduce loss severity but do not remove repayment risk.",
        ],
        "activities": [
            "Credit memo drill: learners summarize borrower strengths, weaknesses, mitigants, and conditions.",
            "Borrower call: learners ask for updated financials and explain covenant concerns professionally.",
            "Stress case debate: learners decide whether lower revenue, margin compression, or rate increases create the binding constraint.",
        ],
        "outputs": [
            "Credit memo paragraph.",
            "Borrower information-request script.",
            "Stress-case language bank.",
        ],
    },
    {
        "title": "Module 7. Controls, Audit, Compliance, Fraud, and Ethics",
        "time": "90 minutes",
        "big_idea": "Finance teams must be precise when discussing control failures, audit evidence, policy exceptions, conflicts of interest, suspicious activity, and performance claims.",
        "objectives": [
            "Differentiate control deficiency, significant deficiency, material weakness, error, fraud, and remediation.",
            "Discuss audit and compliance findings with evidence and professionalism.",
            "Recognize when finance communication must be escalated to legal, compliance, tax, audit, or senior management.",
        ],
        "concepts": [
            "Internal control: a process designed to provide reasonable assurance around reporting, operations, or compliance.",
            "Segregation of duties reduces the chance that one person can both commit and conceal an error or fraud.",
            "Performance information and marketing claims should be fair, accurate, complete, and supported.",
        ],
        "activities": [
            "Control issue escalation: learners explain a reconciliation failure without blame or minimization.",
            "Audit evidence review: learners identify what support is sufficient, missing, or inconsistent.",
            "Ethics scenario sorting: learners classify conflicts, side letters, revenue pressure, selective disclosure, and misleading performance claims.",
        ],
        "outputs": [
            "Control finding response.",
            "Audit evidence request script.",
            "Ethics escalation checklist.",
        ],
    },
    {
        "title": "Module 8. Valuation, M&A, Capital Allocation, and Executive Finance",
        "time": "90 minutes",
        "big_idea": "Senior finance discussions often combine valuation, strategy, risk, capital structure, and narrative. Learners need language for assumptions, valuation methods, diligence findings, synergies, add-backs, WACC, NPV, IRR, and board recommendations.",
        "objectives": [
            "Explain DCF, multiples, WACC, NPV, IRR, accretion/dilution, enterprise value, and equity value at a practical level.",
            "Challenge aggressive M&A assumptions, EBITDA add-backs, synergies, and integration costs.",
            "Present a recommendation that distinguishes financial return, strategic rationale, execution risk, and downside protection.",
        ],
        "concepts": [
            "Valuation is not a single number; it is a range based on assumptions, methods, comparables, and risk.",
            "Adjusted EBITDA can be useful, but add-backs require evidence, consistency, and skepticism.",
            "Capital allocation compares uses of cash such as reinvestment, acquisitions, debt repayment, dividends, and buybacks.",
        ],
        "activities": [
            "Investment committee simulation: learners recommend approve, reject, or defer an acquisition.",
            "Diligence readout: learners explain quality of earnings, working capital peg, customer concentration, and integration risk.",
            "Board update: learners brief liquidity, leverage, valuation range, and next decision points.",
        ],
        "outputs": [
            "Investment committee recommendation.",
            "M&A diligence issue log.",
            "Executive finance briefing script.",
        ],
    },
]


JARGON_GROUPS = [
    (
        "Financial statements and accounting",
        [
            ("Revenue", "Income from delivering goods or services, recognized under applicable accounting rules."),
            ("Gross margin", "Revenue minus cost of goods or services, often expressed as a percentage of revenue."),
            ("Operating income", "Profit from operations before items such as interest and taxes, depending on presentation."),
            ("EBITDA", "Earnings before interest, taxes, depreciation, and amortization; often adjusted but not a cash-flow substitute."),
            ("Accrual", "An accounting estimate recorded before cash payment or receipt occurs."),
            ("Deferred revenue", "Cash received before revenue is recognized."),
            ("Working capital", "Operational assets and liabilities such as receivables, inventory, and payables."),
            ("Free cash flow", "Cash generated after operating needs and capital expenditures, depending on definition used."),
        ],
    ),
    (
        "FP&A and performance management",
        [
            ("Budget", "Approved financial plan for a period."),
            ("Forecast", "Updated estimate of future performance based on current information."),
            ("Run rate", "An annualized or forward-looking estimate based on recent performance, with limitations."),
            ("Variance", "Difference between actual and comparison point such as budget, forecast, or prior period."),
            ("Bridge", "Step-by-step explanation from one financial number to another."),
            ("Sensitivity", "Analysis showing how results change when an assumption changes."),
            ("Scenario", "A coherent case such as base, upside, downside, or stress case."),
            ("Guidance", "Management's communicated expectation for future performance, usually externally sensitive."),
        ],
    ),
    (
        "Treasury, liquidity, and working capital",
        [
            ("Liquidity", "Ability to meet obligations when due without unacceptable loss or disruption."),
            ("Cash runway", "How long available cash is expected to last at current or projected burn."),
            ("Revolver", "A revolving credit facility that can be drawn and repaid within agreed limits."),
            ("Covenant", "A requirement in a financing agreement, often tied to leverage, coverage, or reporting."),
            ("DSO", "Days sales outstanding; a measure of collection speed for receivables."),
            ("DPO", "Days payable outstanding; a measure of payment timing to suppliers."),
            ("Hedge", "A transaction intended to reduce exposure to financial risk."),
            ("FX exposure", "Potential financial impact from movements in foreign exchange rates."),
        ],
    ),
    (
        "Markets and investments",
        [
            ("Return", "Gain or loss on an investment over a period, usually expressed as a percentage."),
            ("Volatility", "Degree of price movement or variability over time."),
            ("Liquidity", "Ability to buy or sell an asset without excessive delay or price impact."),
            ("Yield", "Income return on a bond or investment, expressed as a percentage."),
            ("Duration", "Measure of a bond's sensitivity to interest-rate changes."),
            ("Spread", "Difference between yields or rates, often reflecting credit or liquidity risk."),
            ("Benchmark", "Reference index or target used to evaluate performance."),
            ("Attribution", "Analysis explaining sources of portfolio return or relative performance."),
        ],
    ),
    (
        "Banking and credit",
        [
            ("Credit risk", "Risk that a borrower or counterparty does not meet obligations."),
            ("Leverage", "Use of debt relative to earnings, assets, or equity."),
            ("DSCR", "Debt service coverage ratio; cash flow relative to required debt payments."),
            ("LTV", "Loan-to-value ratio; loan amount relative to collateral value."),
            ("Collateral", "Assets pledged to support repayment or reduce loss severity."),
            ("Probability of default", "Estimated likelihood that a borrower defaults."),
            ("Loss given default", "Estimated loss severity if default occurs."),
            ("Concentration risk", "Exposure to a borrower, sector, geography, customer, or asset type that is too large or correlated."),
        ],
    ),
    (
        "Valuation and corporate finance",
        [
            ("DCF", "Discounted cash flow valuation based on projected cash flows and discount rate."),
            ("WACC", "Weighted average cost of capital; a common discount-rate input."),
            ("NPV", "Net present value; present value of benefits minus costs or investment."),
            ("IRR", "Internal rate of return; discount rate that sets NPV to zero."),
            ("Enterprise value", "Value of the operating business, often before deducting net debt."),
            ("Equity value", "Value attributable to shareholders after net debt and other adjustments."),
            ("Multiple", "Valuation ratio such as EV/EBITDA or price/earnings."),
            ("Accretion/dilution", "Whether a transaction increases or decreases a per-share metric, often EPS.",
            ),
        ],
    ),
    (
        "Controls, audit, and compliance",
        [
            ("Internal control", "Process designed to provide reasonable assurance around reporting, operations, or compliance."),
            ("Control deficiency", "A control design or operating issue that may allow errors or misstatements."),
            ("Material weakness", "A serious control deficiency creating reasonable possibility of material misstatement."),
            ("Reconciliation", "Process of comparing records and resolving differences."),
            ("Segregation of duties", "Dividing responsibilities to reduce error or fraud risk."),
            ("SOX", "Sarbanes-Oxley Act controls and reporting framework for many public companies."),
            ("KYC", "Know your customer processes used in financial institutions and compliance programs."),
            ("AML", "Anti-money laundering controls for detecting and preventing illicit financial activity."),
        ],
    ),
    (
        "Finance verbs and meeting language",
        [
            ("Bridge", "Explain the movement from one number to another through drivers."),
            ("Normalize", "Adjust results to remove unusual or non-recurring effects."),
            ("Stress-test", "Evaluate performance under adverse assumptions."),
            ("Reprice", "Change pricing to reflect cost, risk, demand, or market conditions."),
            ("Reserve", "Record an estimate for expected loss, liability, or adjustment."),
            ("Impair", "Reduce asset value when recoverability or fair value requires it."),
            ("Escalate", "Raise an issue to a higher authority because risk, materiality, or timing requires it."),
            ("Reconcile", "Compare records, identify differences, and resolve them."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. Monthly Close: Revenue Miss or Timing Issue?",
        "setting": "Finance reviews monthly results before sending the executive package.",
        "dialogue": [
            ("Controller", "Revenue is 4 percent below forecast. Is this a real miss or timing?"),
            ("FP&A lead", "Part of it is timing. Two enterprise renewals slipped into next month."),
            ("ESL learner", "Can we separate timing from underlying demand? If the renewals are signed after month-end, revenue recognition may still be next period, but the sales risk is lower than the P&L variance suggests."),
            ("Controller", "What should the commentary say?"),
            ("ESL learner", "Revenue was below forecast primarily due to renewal timing, with no evidence yet of broad demand weakness. We should still flag churn in the SMB segment as a recurring risk."),
        ],
        "notes": [
            "Good finance commentary separates accounting timing from business demand.",
            "A variance explanation should state driver, recurrence, confidence, and risk.",
        ],
    },
    {
        "title": "2. Forecast Review: Aggressive Sales Assumptions",
        "setting": "A business unit submits a forecast that assumes a sharp Q4 recovery.",
        "dialogue": [
            ("Business owner", "The pipeline supports the forecast. We just need the team to execute."),
            ("CFO", "Pipeline is not the same as committed revenue."),
            ("ESL learner", "The upside case is possible, but the base case should reflect conversion rate, sales-cycle length, and historical slippage. What evidence supports a conversion rate above the trailing average?"),
            ("Business owner", "We have a new campaign."),
            ("ESL learner", "Then I would model the campaign as a sensitivity, not the base case, until we see qualified leads converting."),
        ],
        "notes": [
            "Respectful pushback focuses on assumptions and evidence.",
            "Finance language can separate base case, upside case, and sensitivity.",
        ],
    },
    {
        "title": "3. Cash Runway: Profit Is Not Cash",
        "setting": "A startup leadership team reviews runway after slower collections.",
        "dialogue": [
            ("CEO", "We are close to breakeven, so why is cash still tight?"),
            ("Treasury", "Collections slowed, and prepaid annual contracts are lower than planned."),
            ("ESL learner", "The income statement improved, but working capital moved against us. DSO increased, and deferred revenue growth slowed, so cash came in later than revenue recognition suggests."),
            ("CEO", "What levers do we have?"),
            ("ESL learner", "Accelerate collections, pause noncritical hiring, renegotiate payment timing, and prepare a downside cash forecast. I would avoid assuming fundraising closes until terms are signed."),
        ],
        "notes": [
            "Finance learners must explain why net income, EBITDA, and cash can diverge.",
            "Runway updates should include levers and confidence level.",
        ],
    },
    {
        "title": "4. Covenant Monitoring: Early Warning",
        "setting": "Treasury sees leverage approaching a covenant threshold.",
        "dialogue": [
            ("Treasurer", "If Q3 EBITDA lands at the downside case, leverage gets close to the covenant."),
            ("Business unit CFO", "But we will not breach unless Q4 is also weak."),
            ("ESL learner", "True, but we should treat this as an early warning. The lender conversation is easier before a breach than after one."),
            ("Treasurer", "What do we need?"),
            ("ESL learner", "A rolling covenant forecast, downside mitigation plan, and a decision on whether to seek an amendment, add equity cushion, or reduce discretionary spend."),
        ],
        "notes": [
            "Covenant language should be precise: near breach, projected breach, actual breach, waiver, or amendment.",
            "Early communication can preserve credibility with lenders.",
        ],
    },
    {
        "title": "5. Investment Committee: Duration and Spread Risk",
        "setting": "A portfolio manager explains fixed-income underperformance.",
        "dialogue": [
            ("Client", "Why did we underperform if the bond portfolio is conservative?"),
            ("Portfolio manager", "Rates moved higher, and credit spreads widened at the same time."),
            ("ESL learner", "The portfolio stayed within mandate, but duration exposure hurt absolute returns, and spread widening hurt relative performance versus short-duration peers."),
            ("Client", "Should we reduce risk now?"),
            ("ESL learner", "We can shorten duration, improve credit quality, or hold the allocation if your horizon supports it. The tradeoff is lower rate sensitivity versus potential income and reinvestment opportunity."),
        ],
        "notes": [
            "Client communication should explain performance without making hindsight sound easy.",
            "Use mandate, benchmark, horizon, and tradeoff language.",
        ],
    },
    {
        "title": "6. Credit Underwriting: Strong Growth, Weak Coverage",
        "setting": "A bank credit committee reviews a borrower seeking a larger facility.",
        "dialogue": [
            ("Relationship manager", "The borrower is growing fast and wants more capacity."),
            ("Credit officer", "Growth is good, but cash conversion is weak."),
            ("ESL learner", "Revenue growth does not automatically support more debt. DSCR is below our target in the downside case, and customer concentration increases repayment risk."),
            ("Relationship manager", "What structure would make it approvable?"),
            ("ESL learner", "Lower advance rate, tighter reporting, a springing covenant, and a condition that concentration falls before the next increase."),
        ],
        "notes": [
            "Credit language should distinguish growth story from repayment capacity.",
            "Approvals often depend on structure, reporting, and mitigants.",
        ],
    },
    {
        "title": "7. M&A Diligence: EBITDA Add-Back Challenge",
        "setting": "Corporate development reviews seller-adjusted EBITDA.",
        "dialogue": [
            ("Seller advisor", "The adjusted EBITDA add-backs are standard. These costs are non-recurring."),
            ("Buyer finance", "Some of them appear to be ongoing operating costs."),
            ("ESL learner", "We can accept one-time legal settlement costs if documented, but the customer support add-back looks recurring. Removing it lowers EBITDA and increases the purchase multiple."),
            ("Deal lead", "How should we proceed?"),
            ("ESL learner", "Ask for support by add-back, update the valuation range, and consider a working capital adjustment or earnout if the seller's forecast depends on those savings."),
        ],
        "notes": [
            "Diligence language should be skeptical but not hostile.",
            "Adjusted EBITDA affects valuation, leverage, and covenant forecasts.",
        ],
    },
    {
        "title": "8. Pricing and Margin: Discounting Pressure",
        "setting": "Sales wants approval for a large discount to close a strategic customer.",
        "dialogue": [
            ("Sales", "If we approve the discount, we close the logo this quarter."),
            ("Finance", "The discount compresses gross margin and sets a pricing precedent."),
            ("ESL learner", "Can we separate strategic value from unit economics? The deal may be worth doing, but the base price should not become the reference point for renewals or similar customers."),
            ("Sales", "What is the finance recommendation?"),
            ("ESL learner", "Approve only if we include a ramp, minimum volume, limited term, and renewal pricing reset. Otherwise the short-term booking creates long-term margin leakage."),
        ],
        "notes": [
            "Finance pushback should name both revenue upside and margin risk.",
            "Deal approval language often includes conditions, not only yes or no.",
        ],
    },
    {
        "title": "9. Audit Issue: Control Deficiency or Material Weakness?",
        "setting": "An audit team finds repeated manual journal-entry approvals after posting.",
        "dialogue": [
            ("Auditor", "Approvals occurred after posting in several samples."),
            ("Controller", "The entries were correct, so I do not see the issue."),
            ("ESL learner", "Accuracy helps, but the control objective is timely review before posting. A correct entry can still reveal an operating deficiency."),
            ("Controller", "Are you saying it is a material weakness?"),
            ("ESL learner", "Not from this evidence alone. We need to assess frequency, magnitude, compensating controls, and whether a material misstatement could reasonably occur."),
        ],
        "notes": [
            "Control language should separate error outcome from control design or operation.",
            "Do not jump from deficiency to material weakness without analysis.",
        ],
    },
    {
        "title": "10. FX Hedge Debate",
        "setting": "A multinational company faces euro-denominated costs and dollar revenue.",
        "dialogue": [
            ("Operations", "The euro moved against us. Can treasury just lock the rate?"),
            ("Treasury", "We can hedge part of the exposure, but hedging has cost and forecast risk."),
            ("ESL learner", "The exposure is not only today's spot rate. We need forecasted euro costs, timing, confidence, hedge ratio, and whether the hedge qualifies for the accounting treatment we expect."),
            ("Operations", "So what do you recommend?"),
            ("ESL learner", "Start with a layered hedge for the highly probable exposure and review monthly as the forecast changes."),
        ],
        "notes": [
            "Hedging reduces certain risks but can create cost, accounting, and forecast challenges.",
            "Use exposure, hedge ratio, timing, and accounting-treatment language.",
        ],
    },
    {
        "title": "11. Performance Presentation: Fair, Accurate, Complete",
        "setting": "A wealth team prepares a client deck after a strong quarter.",
        "dialogue": [
            ("Advisor", "Let's lead with our best-performing strategy."),
            ("Compliance", "Only if the performance presentation is balanced and not misleading."),
            ("ESL learner", "We should include benchmark, time period, fees basis, relevant risks, and whether the result is representative. A single strong quarter without context may create a misleading impression."),
            ("Advisor", "Can we still use it?"),
            ("ESL learner", "Yes, if we present it fairly, accurately, and completely, and avoid implying that the return is guaranteed or typical without support."),
        ],
        "notes": [
            "Investment performance language carries compliance and ethics risk.",
            "Strong performance still needs context, risk, fees, and representativeness.",
        ],
    },
    {
        "title": "12. Board Update: Liquidity, Leverage, and Capital Allocation",
        "setting": "The CFO briefs the board before approving a buyback and acquisition pipeline.",
        "dialogue": [
            ("Board member", "Can we fund the buyback and still pursue the acquisition?"),
            ("CFO", "It depends on the downside case and debt capacity."),
            ("ESL learner", "Base case supports both, but the downside case tightens liquidity and pushes leverage close to our target ceiling. The decision is not only affordability; it is flexibility if revenue slows or rates stay higher."),
            ("Board member", "What is management's recommendation?"),
            ("ESL learner", "Authorize a smaller buyback tranche now, preserve capacity for diligence, and revisit after Q2 cash conversion and covenant forecast are updated."),
        ],
        "notes": [
            "Board finance updates need recommendation, tradeoff, downside case, and decision trigger.",
            "Capital allocation language connects cash, strategy, risk, and optionality.",
        ],
    },
]


PHRASE_BANK = {
    "Performance and variance": [
        "The variance is driven by volume, not price, and appears recurring.",
        "The result beat forecast, but the quality of the beat is mixed because working capital moved against us.",
        "This is a timing issue for P&L recognition, but it still affects cash this quarter.",
        "The bridge from budget to forecast has three drivers: mix, hiring delay, and FX.",
    ],
    "Assumptions and forecasts": [
        "What evidence supports this conversion rate relative to the trailing average?",
        "I would keep that in the upside case until we see qualified leads converting.",
        "The base case assumes current run rate; the downside case assumes slower collections and margin compression.",
        "The sensitivity shows that a one-point margin change has a larger impact than the volume change.",
    ],
    "Treasury and liquidity": [
        "Cash is tighter because receivables increased and deferred revenue growth slowed.",
        "We are not in breach, but the downside case creates covenant headroom risk.",
        "The revolver provides liquidity, but drawing it changes leverage and lender optics.",
        "A hedge reduces FX exposure, but it does not remove forecast risk.",
    ],
    "Markets and investment communication": [
        "Performance should be evaluated against the mandate, benchmark, time horizon, and risk taken.",
        "Duration exposure hurt returns when rates moved higher.",
        "Spread widening affected credit positions even though fundamentals have not deteriorated equally.",
        "The portfolio underperformed this month, but attribution shows the main drag was sector allocation, not security selection.",
    ],
    "Credit and risk": [
        "Revenue growth is positive, but repayment capacity depends on cash conversion and coverage.",
        "Collateral reduces loss severity; it does not guarantee repayment.",
        "The downside case binds on DSCR before it binds on leverage.",
        "We can recommend approval with structure: lower advance rate, tighter reporting, and a springing covenant.",
    ],
    "Controls and compliance": [
        "A correct entry can still reveal a control operating deficiency.",
        "We need to assess magnitude, frequency, compensating controls, and reasonable possibility of misstatement.",
        "The performance claim needs context, fees basis, benchmark, time period, and risk disclosure.",
        "This issue should be escalated to compliance before the deck is shared externally.",
    ],
    "Valuation and executive recommendations": [
        "Valuation is a range, not a point estimate, and the range is sensitive to margin and terminal-growth assumptions.",
        "The add-back is acceptable only if it is documented, non-recurring, and consistent with the definition in the agreement.",
        "The transaction is strategically attractive, but the integration risk reduces the financial margin of safety.",
        "My recommendation is to approve, defer, or reject based on return, downside protection, and execution risk.",
    ],
}


WORKBOOK_TASKS = [
    "An executive asks, 'Why are we down, and does it matter?' Write a decision-grade response that names comparison point, driver, magnitude, recurrence, confidence, and recommended action.",
    "A monthly result is below forecast, but two customer renewals slipped after month-end. Write close commentary separating accounting timing, demand, revenue recognition, and ongoing churn risk.",
    "A business owner submits an aggressive revenue forecast. Write five assumption-challenge questions and a sentence moving the unsupported upside into sensitivity analysis.",
    "Cash is tightening even though EBITDA improved. Explain the role of DSO, deferred revenue, and working capital to a non-finance executive.",
    "Leverage is approaching a covenant threshold in the downside case. Write a treasury update with headroom, timing, options, and lender-communication considerations.",
    "A portfolio underperformed its benchmark during a volatile month. Write a client-safe performance explanation using attribution, mandate, and risk language.",
    "A borrower is growing quickly but DSCR is weak. Write a credit memo paragraph naming strengths, risks, mitigants, and recommended structure.",
    "An audit sample shows late approvals on journal entries. Write a control finding response that avoids both blame and minimization.",
    "A deal team proposes seller-adjusted EBITDA with multiple add-backs. Write diligence questions and a recommendation on valuation impact.",
]


SOURCES = [
    "SEC Investor.gov glossary and SEC guidance on reading Form 10-K financial statements, MD&A, risk factors, and filings.",
    "FASB Accounting Standards Codification and FASB revenue-recognition and fair-value resources for U.S. GAAP concepts.",
    "Federal Reserve resources on monetary policy, interest rates, liquidity facilities, and policy tools.",
    "FINRA investor education and fixed-income resources for yield, volatility, liquidity, duration, and market terminology.",
    "FDIC supervisory resources on interest-rate risk and banking risk management language.",
    "CFA Institute Code and Standards and GIPS resources for performance presentation, fair representation, and investment communication.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in finance environments: accountants, FP&A analysts, controllers, treasury staff, bankers, credit analysts, investment analysts, portfolio support teams, auditors, risk professionals, compliance staff, investor relations teams, and finance-adjacent business leaders."
        )
    )
    story.append(
        p(
            "The course is not a certification course in accounting, banking, investing, or valuation. It trains professional English for finance work: explaining drivers, challenging assumptions, writing variance commentary, presenting risk, documenting controls, and communicating with executives, clients, auditors, lenders, and business partners."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "Finance teams compress judgment into short phrases: one-time item, recurring margin pressure, covenant headroom, run-rate assumption, working-capital drag, duration exposure, adjusted EBITDA add-back, material weakness, downside case, valuation range, and fair performance presentation. Learners need both the vocabulary and the conversational discipline around it: quantify, caveat, challenge, reconcile, explain tradeoffs, and recommend."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_finance_communication_principles(story: list) -> None:
    story += h1("Finance Communication Principles")
    story.append(h2("Explain the movement, not only the number"))
    story.append(
        p(
            "A finance answer should usually include comparison point, driver, magnitude, timing, recurrence, confidence, and action. 'Revenue missed by 4 percent' is not enough. The useful answer explains whether the miss came from volume, price, mix, churn, timing, FX, accounting treatment, or a one-time event."
        )
    )
    story.append(h2("Make uncertainty useful"))
    story.append(
        bullets(
            [
                "Use 'base case,' 'upside case,' and 'downside case' instead of pretending the forecast is one certain number.",
                "Use 'current evidence suggests' when data is incomplete.",
                "Use 'recurring' and 'non-recurring' carefully; a cost is not non-recurring just because the team dislikes it.",
                "Use 'cash impact' when a P&L improvement does not translate into liquidity.",
                "Use 'decision trigger' to tell leaders when they need to act.",
            ]
        )
    )
    story.append(h2("Turn vague finance requests into answerable work"))
    story.append(
        table(
            [
                ["Vague request", "Stronger finance question"],
                ["Why are we down?", "Which driver explains the variance: price, volume, mix, churn, timing, FX, cost, or accounting treatment?"],
                ["Can we afford it?", "What is the impact on cash, covenant headroom, leverage, liquidity, and downside flexibility?"],
                ["Is the forecast realistic?", "Which assumptions differ from actual trends, and what evidence supports those differences?"],
                ["Is the deal attractive?", "What is the valuation range, return profile, downside case, integration risk, and strategic rationale?"],
            ],
            [2.2 * 72, 4.8 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a realistic sentence, ask one clarification question about it, and explain the business consequence. Because finance terms depend on standards, formulas, contracts, and jurisdiction, learners should ask which definition is being used."
        )
    )
    for title, items in JARGON_GROUPS:
        story.append(h2(title))
        rows = [["Term", "Working meaning"]]
        rows.extend([[term, definition] for term, definition in items])
        story.append(table(rows, [1.55 * 72, 5.45 * 72]))


def add_module_details(story: list) -> None:
    story += h1("Instructor Module Plans")
    for module in MODULES:
        story.append(h2(f"{module['title']} ({module['time']})"))
        story.append(p(module["big_idea"]))
        story.append(h3("Learning objectives"))
        story.append(bullets(module["objectives"]))
        story.append(h3("Core concepts"))
        story.append(bullets(module["concepts"]))
        story.append(h3("Activities"))
        story.append(bullets(module["activities"], numbered=True))
        story.append(h3("Learner outputs"))
        story.append(bullets(module["outputs"]))
        story.append(
            box(
                "Facilitator note",
                [
                    "When learners give a vague finance answer, ask: compared with what, driven by what, recurring or one-time, cash or non-cash, material or immaterial, controllable or external, and what decision should follow?"
                ],
                "blue",
            )
        )


def add_assessment(story: list) -> None:
    story += h1("Assessment and Coaching")
    story.append(h2("Pre-course diagnostic"))
    story.append(
        bullets(
            [
                "Learner explains their finance role in 90 seconds, including metrics owned, audiences served, recurring meetings, and highest-risk communications.",
                "Learner defines twelve finance terms and uses six in realistic workplace sentences.",
                "Learner handles a short role-play: an executive asks why cash is tight even though EBITDA improved.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but uses formulas loosely.", "Uses finance terms accurately in context.", "Defines terms, asks which definition applies, and adapts to audience."],
                ["Driver analysis", "Reports numbers without explaining movement.", "Names drivers, magnitude, timing, and recurrence.", "Links drivers to decision, risk, and next action."],
                ["Forecast judgment", "Accepts or rejects assumptions broadly.", "Challenges assumptions with evidence and scenarios.", "Frames confidence, sensitivity, and decision triggers clearly."],
                ["Risk communication", "Sounds either alarmist or overly reassuring.", "Explains exposure, mitigants, and uncertainty.", "Connects financial risk to business choice and governance path."],
                ["Executive presence", "Gives too much detail or hides uncertainty.", "Summarizes what changed, why, so what, and now what.", "Handles pushback with concise evidence and recommendation."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a finance leadership meeting after a difficult quarter. Revenue missed forecast because of renewal timing and churn, cash tightened because DSO increased, leverage is near covenant sensitivity, sales requests a discount-heavy strategic deal, and the board wants a capital allocation recommendation. The learner must explain drivers, challenge assumptions, present downside risk, propose actions, and write an executive summary."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "Finance English",
        "Instructor guide for high-level ESL learners working in accounting, FP&A, treasury, banking, investments, audit, risk, and corporate finance",
        "Audience: instructors, finance English coaches, corporate learning teams, finance managers, and advanced professional English programs",
    )
    add_course_opening(story)
    add_finance_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-finance-english-instructor-guide.pdf",
        "EFSP Finance English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Finance English",
        "Participant workbook: financial statements, FP&A, treasury, markets, banking, valuation, controls, and finance dialogue practice",
        "Audience: advanced ESL learners working in accounting, FP&A, treasury, banking, investments, audit, risk, corporate finance, and related roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you speak and write more precisely in finance workplaces. The goal is not to sound complicated. The goal is to make numbers useful: what changed, why it changed, whether it matters, what risk remains, and what decision follows."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which finance conversations are hardest for you: close, forecast review, treasury, banking, audit, investment performance, credit, valuation, or board updates?",
                "Which finance terms do you understand when reading but avoid when speaking?",
                "When someone challenges your numbers, do you become too vague, too defensive, too detailed, or too indirect?",
                "What is one recent finance update you wish you had explained more clearly?",
            ]
        )
    )
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("Finance Driver Language")
    story.append(
        table(
            [
                ["Area", "Useful verbs", "Example sentence"],
                ["Accounting", "recognize, accrue, defer, reserve, reconcile", "We accrued the expense because the service was received before month-end."],
                ["FP&A", "bridge, forecast, sensitize, normalize, explain", "The bridge shows margin pressure from mix and discounting."],
                ["Treasury", "fund, hedge, draw, repay, monitor", "The downside case reduces covenant headroom by the fourth quarter."],
                ["Markets", "attribute, rebalance, underperform, widen, tighten", "Spread widening explains most of the relative underperformance."],
                ["Credit", "underwrite, stress-test, mitigate, collateralize", "Growth is strong, but DSCR falls below target in the downside case."],
                ["Corporate finance", "value, discount, allocate, acquire, divest", "The acquisition is attractive only if the synergy assumptions are achievable."],
            ],
            [1.25 * 72, 2.1 * 72, 3.65 * 72],
        )
    )
    story += h1("Practice Pages")
    answer_key: list[dict[str, str]] = []
    for index, module in enumerate(MODULES):
        dialogue = DIALOGUES[index % len(DIALOGUES)]
        story.append(PageBreak())
        story.append(h2(module["title"]))
        story.append(p(module["big_idea"]))
        story.append(h3("What you should be able to do"))
        story.append(bullets(module["objectives"]))
        add_cloze_exercise(story, make_dialogue_cloze(dialogue), answer_key)
    story.append(PageBreak())
    story += h1("Phrase Bank")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-finance-english-participant-workbook.pdf",
        "EFSP Finance English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "Finance Dialogue Lab",
        "Realistic finance-workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners",
        "Audience: instructors, finance English coaches, peer practice groups, corporate learning teams, and finance teams",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: finance speaker, counterpart, observer.",
                "Read the model dialogue once. Then replay it with changed numbers, different risk level, or a different audience.",
                "The observer listens for terminology accuracy, driver logic, assumption challenge, confidence language, risk framing, and decision clarity.",
                "After each role-play, replay the hardest 30 seconds with a more precise finance sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners hide behind numbers. Ask them to explain the driver, source, definition, business implication, and decision. If they use EBITDA, free cash flow, adjusted margin, or run rate, ask which definition applies."
            ],
            "amber",
        )
    )
    answer_key: list[dict[str, str]] = []
    for item in DIALOGUES:
        story.append(PageBreak())
        story.append(Paragraph(esc(item["title"]), S["CardTitle"]))
        story.append(rule())
        story.append(box("Setting", [item["setting"]], "blue"))
        rows = [["Speaker", "Line"]]
        rows.extend([[speaker, line] for speaker, line in item["dialogue"]])
        story.append(table(rows, [1.25 * 72, 5.75 * 72]))
        story.append(h3("Language notes"))
        story.append(bullets(item["notes"]))
        add_cloze_exercise(story, make_dialogue_cloze(item), answer_key, show_context=False)
        story.append(h3("Observer checklist"))
        story.append(
            bullets(
                [
                    "Did the learner explain the financial movement, not only the number?",
                    "Did the learner use finance terminology accurately and define formulas when needed?",
                    "Did the learner identify assumptions, evidence, recurrence, cash impact, and risk?",
                    "Did the learner make a clear recommendation, owner, or next step?",
                ]
            )
        )
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-finance-dialogue-lab.pdf",
        "EFSP Finance Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "Finance Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise finance vocabulary and workplace meeting language",
        "Audience: advanced ESL learners in accounting, FP&A, treasury, banking, investments, audit, risk, corporate finance, and finance-adjacent roles",
    )
    story += h1("How to Use Finance Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it makes the financial issue more precise.",
                "Pair jargon with comparison point, driver, magnitude, timing, recurrence, and source.",
                "Define formulas for mixed audiences; EBITDA, free cash flow, margin, and leverage can have different definitions.",
                "Avoid giving investment, tax, accounting, legal, or banking advice outside your role and approval process.",
            ]
        )
    )
    add_jargon_sections(story)
    story += h1("Common Meeting Moves")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story += h1("Fast Contrast Pairs")
    story.append(
        table(
            [
                ["Do not confuse", "Working contrast"],
                ["Revenue vs cash", "Revenue may be recognized before or after cash is collected, depending on terms and accounting rules."],
                ["Net income vs EBITDA", "Net income includes more expenses and accounting effects; EBITDA excludes interest, taxes, depreciation, and amortization."],
                ["Profit vs liquidity", "A company can be profitable and still lack cash if working capital, debt service, or capex consume cash."],
                ["Budget vs forecast", "Budget is the approved plan; forecast is an updated estimate based on current information."],
                ["One-time vs recurring", "One-time should be unusual or non-recurring; recurring items should stay in the run-rate view."],
                ["Yield vs total return", "Yield is income relative to price or investment; total return includes price changes and income."],
                ["Duration vs maturity", "Maturity is final repayment date; duration estimates interest-rate sensitivity."],
                ["Enterprise value vs equity value", "Enterprise value measures the business; equity value reflects value to shareholders after net debt and adjustments."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-finance-jargon-quick-reference.pdf",
        "EFSP Finance Jargon Field Guide",
        story,
    )


def main() -> None:
    paths = [
        instructor_guide(),
        participant_workbook(),
        dialogue_lab(),
        quick_reference(),
    ]
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
