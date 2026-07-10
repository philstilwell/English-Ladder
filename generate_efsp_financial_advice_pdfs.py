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
                "Focus: high-level professional English for financial-advice workplaces, including client discovery, fiduciary and best-interest language, risk profiling, retirement planning, portfolio reviews, product discussions, fees, conflicts, documentation, and realistic advisor-client dialogue.",
                "Designed for advanced ESL learners who already work as financial advisors, investment advisers, planners, client service associates, paraplanners, wealth managers, retirement specialists, or advice-adjacent professionals.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: this is financial-advice English training, not investment, tax, legal, insurance, banking, or retirement advice. Standards and obligations vary by jurisdiction, license, firm, role, account type, and client facts. Learners should practice language, documentation, and professional judgment while relying on qualified supervisory, compliance, legal, tax, and investment guidance for actual recommendations.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use financial-advice terminology accurately in client discovery, planning meetings, risk reviews, recommendation discussions, portfolio reviews, rollover conversations, and compliance documentation.",
    "Ask client-centered discovery questions about goals, time horizon, liquidity needs, risk tolerance, risk capacity, tax status, investment experience, family situation, and constraints.",
    "Explain recommendations with a clear link among client facts, alternatives considered, costs, risks, conflicts, and rationale.",
    "Handle difficult client conversations about volatility, underperformance, concentrated stock, retirement income, fees, tax consequences, beneficiary issues, and family pressure.",
    "Distinguish education, general information, financial advice, investment recommendations, tax/legal referrals, and firm-approved communication.",
    "Write professional outputs: meeting notes, discovery summaries, IPS language, recommendation rationales, portfolio-review comments, risk notes, and client-safe follow-up emails.",
]


MODULES = [
    {
        "title": "Module 1. Advisor English: Discovery, Scope, Trust, and Boundaries",
        "time": "90 minutes",
        "big_idea": "Financial advice begins before the recommendation. Strong advisor English gathers client facts, clarifies scope, explains the role, and builds trust without promising performance or drifting into tax or legal advice.",
        "objectives": [
            "Conduct a client discovery conversation that is warm, structured, and documented.",
            "Separate client goals, facts, preferences, constraints, and assumptions.",
            "Use role-boundary language for tax, legal, insurance, and estate-planning issues.",
        ],
        "concepts": [
            "Discovery: structured fact-finding about the client's financial life, goals, risk profile, experience, and constraints.",
            "Scope: what the engagement or relationship covers and what requires a referral or separate professional.",
            "Client-safe promise language: advisors can promise process and diligence, not market outcomes.",
        ],
        "activities": [
            "Discovery map: learners organize client facts into goals, balance sheet, income, risk, constraints, relationships, and unknowns.",
            "Scope reset drill: learners respond when a client asks for tax, legal, or guaranteed-return advice.",
            "Trust without promise: learners rewrite overconfident advisor statements into professional language.",
        ],
        "outputs": [
            "Client discovery question bank.",
            "Scope and boundary phrase bank.",
            "Discovery summary template.",
        ],
    },
    {
        "title": "Module 2. Standards of Conduct, Best Interest, Disclosures, and Conflicts",
        "time": "90 minutes",
        "big_idea": "Financial advice language is regulated and trust-sensitive. Learners need practical English for fiduciary duty, best interest, suitability, Form CRS, fees, compensation, conflicts, supervision, and documentation.",
        "objectives": [
            "Explain fiduciary duty, best-interest obligations, suitability, conflicts, and disclosures in client-friendly language.",
            "Discuss fees and compensation clearly without sounding defensive.",
            "Document the rationale for a recommendation in a way a supervisor or regulator could understand later.",
        ],
        "concepts": [
            "Best-interest and suitability language depends on role, firm, product, and relationship; learners must use firm-approved definitions.",
            "Conflict of interest: a financial, business, personal, or compensation factor that could influence advice or appear to influence advice.",
            "Disclosure is not a substitute for good judgment; clients need understandable explanations and documented rationale.",
        ],
        "activities": [
            "Disclosure translation: learners explain Form CRS, fees, and conflicts in plain English.",
            "Conflict spotting: learners identify conflicts in five product and account recommendations.",
            "Rationale writing: learners document why an account type or strategy fits the client's profile.",
        ],
        "outputs": [
            "Fees and conflict explanation script.",
            "Recommendation rationale checklist.",
            "Compliance-aware meeting note.",
        ],
    },
    {
        "title": "Module 3. Goals, Risk Profile, Asset Allocation, and IPS Language",
        "time": "90 minutes",
        "big_idea": "Clients often say they want high returns with low risk. Advisors must translate feelings into a documented risk profile, objective, time horizon, liquidity need, allocation, and review process.",
        "objectives": [
            "Distinguish risk tolerance, risk capacity, time horizon, liquidity needs, and investment objective.",
            "Explain asset allocation, diversification, rebalancing, and portfolio constraints.",
            "Write investment policy language that is understandable and reviewable.",
        ],
        "concepts": [
            "Risk tolerance is emotional willingness; risk capacity is financial ability to absorb loss without derailing goals.",
            "Diversification reduces concentration risk but does not eliminate market risk.",
            "Investment policy statement: a document or framework connecting goals, risk profile, allocation, constraints, and monitoring.",
        ],
        "activities": [
            "Risk mismatch role-play: a client wants aggressive growth but panics during normal volatility.",
            "Allocation explanation: learners explain why the portfolio is not 100 percent cash or 100 percent equities.",
            "IPS rewrite: learners convert jargon-heavy investment policy language into client-ready language.",
        ],
        "outputs": [
            "Risk profile distinction worksheet.",
            "Asset allocation explanation.",
            "Client-friendly IPS paragraph.",
        ],
    },
    {
        "title": "Module 4. Retirement Planning, Income, Tax-Aware Conversations, and RMDs",
        "time": "90 minutes",
        "big_idea": "Retirement advice combines cash flow, uncertainty, tax rules, account types, Social Security timing, healthcare, inflation, longevity, and client emotion. Learners need careful language that avoids false precision.",
        "objectives": [
            "Explain accumulation, decumulation, withdrawal strategy, sequence-of-returns risk, RMDs, and tax diversification.",
            "Discuss Roth vs traditional, taxable vs tax-deferred accounts, and account sequencing without giving unapproved tax advice.",
            "Frame retirement income projections as planning tools, not guarantees.",
        ],
        "concepts": [
            "Sequence-of-returns risk: early retirement losses can have a larger impact when withdrawals are being taken.",
            "RMD: required minimum distribution rules generally require withdrawals from many tax-deferred retirement accounts after a specified age, subject to account and client facts.",
            "Monte Carlo analysis: a planning simulation used to estimate probability of meeting goals under many market paths, not a guarantee.",
        ],
        "activities": [
            "Retirement income meeting: learners explain why the withdrawal rate may need adjustment after market losses.",
            "RMD explanation drill: learners define RMDs and when to refer to tax professionals or custodians.",
            "Tax-aware planning role-play: learners discuss Roth conversion considerations without overstepping.",
        ],
        "outputs": [
            "Retirement income explanation script.",
            "RMD and tax referral language.",
            "Planning projection caveat bank.",
        ],
    },
    {
        "title": "Module 5. Portfolio Reviews, Volatility, Rebalancing, and Behavioral Coaching",
        "time": "90 minutes",
        "big_idea": "Clients rarely need only facts during volatility. They need calm framing, review of goals, explanation of portfolio behavior, and a disciplined process for deciding whether to stay, rebalance, adjust, or revisit the plan.",
        "objectives": [
            "Explain performance, benchmark, attribution, drawdown, volatility, rebalancing, and time horizon in client-safe language.",
            "Respond to fear, regret, loss aversion, recency bias, and pressure to chase recent winners.",
            "Avoid statements that imply certainty about market direction.",
        ],
        "concepts": [
            "Drawdown: decline from a prior high point to a lower value.",
            "Rebalancing: returning the portfolio toward target allocation after market movement or client change.",
            "Behavior gap: the difference between investment returns and investor returns caused by timing and behavior.",
        ],
        "activities": [
            "Volatility call simulation: a client wants to sell after a downturn.",
            "Portfolio review: learners explain why a diversified portfolio lagged a concentrated index.",
            "Behavioral coaching drill: learners validate emotion without validating a harmful action.",
        ],
        "outputs": [
            "Volatility conversation script.",
            "Portfolio review commentary.",
            "Behavioral coaching phrase bank.",
        ],
    },
    {
        "title": "Module 6. Products, Account Types, Rollovers, Annuities, Insurance, and Alternatives",
        "time": "90 minutes",
        "big_idea": "Product conversations are high-risk because clients may focus on benefits and miss costs, restrictions, liquidity, surrender charges, tax effects, and conflicts. Learners need balanced product language.",
        "objectives": [
            "Discuss mutual funds, ETFs, bonds, annuities, life insurance, managed accounts, alternatives, 529 plans, and account types at a practical level.",
            "Explain rollover options, fees, services, investment choices, and conflicts without steering prematurely.",
            "Describe product tradeoffs rather than presenting products as universally good or bad.",
        ],
        "concepts": [
            "Rollover: moving assets from an employer plan to another retirement account; alternatives and consequences should be discussed carefully.",
            "Annuity: a contract that may provide income or guarantees, often with costs, conditions, surrender periods, and insurer risk.",
            "Alternative investment: a nontraditional strategy or asset that may involve liquidity limits, complexity, higher fees, and suitability constraints.",
        ],
        "activities": [
            "Rollover conversation: learners compare leaving assets in plan, rolling to IRA, rolling to new plan, or cashing out.",
            "Annuity tradeoff role-play: learners explain income guarantee, liquidity limits, surrender charges, and fees.",
            "Product recommendation review: learners identify missing facts before a recommendation can be supported.",
        ],
        "outputs": [
            "Product tradeoff table.",
            "Rollover documentation script.",
            "Balanced recommendation language.",
        ],
    },
    {
        "title": "Module 7. Family, Estate, Beneficiaries, Elder Risk, and Difficult Client Moments",
        "time": "90 minutes",
        "big_idea": "Financial advice often becomes personal. Advisors may encounter family conflict, cognitive decline concerns, beneficiary mistakes, sudden wealth, divorce, death, job loss, and possible exploitation.",
        "objectives": [
            "Use sensitive language for beneficiaries, estate documents, trusted contacts, incapacity, elder exploitation, and family conflict.",
            "Know when to refer to estate attorneys, tax advisors, insurance specialists, or supervisors.",
            "Respond to grief, fear, embarrassment, and pressure from relatives while protecting the client relationship.",
        ],
        "concepts": [
            "Beneficiary designation: account-level instruction that may control transfer at death and should be reviewed after life events.",
            "Trusted contact: a person the firm may contact in limited circumstances under firm policy, not a general power over the account.",
            "Financial exploitation: improper use of a person's resources, often requiring escalation under firm policy and applicable rules.",
        ],
        "activities": [
            "Beneficiary review: learners discuss outdated beneficiaries after divorce and remarriage.",
            "Trusted contact conversation: learners explain why the firm asks for one.",
            "Elder-risk scenario: learners respond when a relative pressures an older client to liquidate investments.",
        ],
        "outputs": [
            "Sensitive family-language script.",
            "Beneficiary review checklist.",
            "Elder-risk escalation note.",
        ],
    },
    {
        "title": "Module 8. Practice Management, Documentation, Complaints, Marketing, and Supervision",
        "time": "90 minutes",
        "big_idea": "Professional financial advice depends on process. Good client language must be matched by good records, approved communication, follow-through, complaint handling, privacy practices, and supervisory awareness.",
        "objectives": [
            "Write meeting notes that capture client facts, recommendation rationale, alternatives discussed, costs, risks, conflicts, and follow-up items.",
            "Use compliant language in emails, client presentations, social media, testimonials, and performance discussions.",
            "Recognize when a client concern becomes a complaint or escalation issue.",
        ],
        "concepts": [
            "Contemporaneous documentation: notes recorded near the time of the conversation, before memory or facts drift.",
            "Complaint: a client expression of dissatisfaction that may require firm handling even if the client uses informal language.",
            "Supervision: firm review of recommendations, communications, outside activities, advertising, and client handling.",
        ],
        "activities": [
            "Meeting note repair: learners improve a weak note so it explains the recommendation and client context.",
            "Complaint role-play: learners respond to a client who says they were misled about fees.",
            "Marketing language review: learners remove guarantees, promissory wording, and unsupported claims.",
        ],
        "outputs": [
            "Advisor meeting note template.",
            "Complaint escalation script.",
            "Client communication review checklist.",
        ],
    },
]


JARGON_GROUPS = [
    (
        "Advisor roles and standards",
        [
            ("Financial advisor", "A broad market term for someone who provides financial guidance; legal meaning depends on registration, license, and services."),
            ("Investment adviser", "A regulated adviser role that may owe fiduciary obligations under applicable law and registration status."),
            ("Broker-dealer", "A regulated firm or representative involved in securities transactions and recommendations."),
            ("Fiduciary duty", "Duty to act in the client's best interest under applicable standards and context."),
            ("Regulation Best Interest", "SEC standard of conduct for broker-dealers when making recommendations to retail customers."),
            ("Suitability", "A standard requiring recommendations to fit a customer's investment profile under applicable rules."),
            ("Form CRS", "Relationship summary designed to help retail investors understand services, fees, conflicts, and disciplinary history."),
            ("Form ADV", "Investment adviser disclosure and registration form, including brochure information for clients."),
        ],
    ),
    (
        "Client profile and discovery",
        [
            ("Investment objective", "What the client is trying to accomplish, such as growth, income, preservation, or liquidity."),
            ("Time horizon", "How long the client expects to invest before needing funds for a goal."),
            ("Risk tolerance", "The client's emotional willingness to accept investment volatility or loss."),
            ("Risk capacity", "The client's financial ability to absorb loss without derailing goals."),
            ("Liquidity need", "Need for accessible cash or investments that can be sold without unacceptable cost or delay."),
            ("Investment experience", "Client's familiarity with products, markets, risks, and prior investing decisions."),
            ("Tax status", "Client tax facts that may affect planning and investment decisions, requiring qualified tax guidance."),
            ("Constraints", "Limits such as income needs, legal restrictions, values preferences, concentration, liquidity, or tax concerns."),
        ],
    ),
    (
        "Planning and retirement",
        [
            ("Financial plan", "A coordinated view of goals, resources, assumptions, risks, and recommended actions."),
            ("Monte Carlo analysis", "Simulation showing possible goal outcomes under many market paths, not a guarantee."),
            ("Retirement income", "Cash flow used to support spending after work income decreases or stops."),
            ("Withdrawal rate", "Percentage of a portfolio withdrawn over a period, often discussed in retirement income planning."),
            ("Sequence risk", "Risk that early losses during withdrawals harm long-term sustainability."),
            ("RMD", "Required minimum distribution from certain retirement accounts under IRS rules, depending on age, account, and facts."),
            ("Roth conversion", "Moving pre-tax retirement assets into Roth status, often creating tax considerations."),
            ("Beneficiary designation", "Account instruction naming who receives assets after death, subject to account and legal rules."),
        ],
    ),
    (
        "Portfolio construction",
        [
            ("Asset allocation", "Division of portfolio among asset categories such as equities, fixed income, cash, and alternatives."),
            ("Diversification", "Spreading exposure across holdings or asset classes to reduce concentration risk."),
            ("Rebalancing", "Adjusting portfolio back toward target allocation after movement or client change."),
            ("IPS", "Investment policy statement connecting objectives, risk, allocation, constraints, and monitoring."),
            ("Benchmark", "Reference index or blend used to evaluate portfolio performance."),
            ("Drawdown", "Decline from a prior high value to a lower value."),
            ("Tax-loss harvesting", "Selling investments at a loss to potentially offset gains, subject to tax rules and constraints."),
            ("Concentrated position", "Large exposure to one security, employer stock, sector, or asset class."),
        ],
    ),
    (
        "Products and accounts",
        [
            ("ETF", "Exchange-traded fund; pooled investment traded on an exchange."),
            ("Mutual fund", "Pooled investment vehicle that issues shares and is typically priced at net asset value."),
            ("Expense ratio", "Annual fund operating costs expressed as a percentage of assets."),
            ("Annuity", "Insurance contract that may provide income or guarantees with costs, restrictions, and conditions."),
            ("Surrender charge", "Fee for withdrawing from certain products during a specified period."),
            ("Managed account", "Account in which investments are managed for the client under an agreed program or mandate."),
            ("529 plan", "Tax-advantaged education savings plan under U.S. rules, subject to program and tax details."),
            ("Alternative investment", "Nontraditional investment that may have complexity, illiquidity, higher fees, or eligibility limits."),
        ],
    ),
    (
        "Fees, compensation, and conflicts",
        [
            ("AUM fee", "Fee based on assets under management."),
            ("Commission", "Transaction-based compensation connected to buying, selling, or placing a product."),
            ("Wrap fee", "Bundled fee covering advisory and certain transaction or platform services, depending on program."),
            ("Load", "Sales charge on certain mutual funds or products."),
            ("Revenue sharing", "Payment arrangement that may create a conflict requiring disclosure and management."),
            ("Conflict of interest", "A factor that could influence or appear to influence advice or recommendations."),
            ("Disclosure", "Communication of relevant facts such as fees, risks, services, conflicts, and limitations."),
            ("Fee-only", "Compensation model often meaning no product commissions, but definitions and use should be checked.",
            ),
        ],
    ),
    (
        "Client behavior and risk language",
        [
            ("Loss aversion", "Tendency to feel losses more strongly than similar gains."),
            ("Recency bias", "Tendency to overweight recent events when making decisions."),
            ("Herding", "Following others' decisions without independent analysis of fit and risk."),
            ("Panic selling", "Selling primarily from fear during stress, often without revisiting goals and plan."),
            ("Chasing performance", "Buying what recently performed well without evaluating risk and fit."),
            ("Behavior gap", "Difference between investment returns and investor returns caused by timing and behavior."),
            ("Client objective", "The goal the plan is designed to support, not necessarily the client's latest emotional reaction."),
            ("Tradeoff", "Choice that improves one objective while accepting cost or risk somewhere else."),
        ],
    ),
    (
        "Documentation and compliance verbs",
        [
            ("Recommend", "Suggest a specific action or strategy based on client facts and standards."),
            ("Disclose", "Communicate relevant information about services, fees, risks, conflicts, or limitations."),
            ("Document", "Record facts, rationale, alternatives, risks, client instructions, and follow-up."),
            ("Escalate", "Raise an issue to compliance, supervision, legal, tax, or specialist support."),
            ("Supervise", "Review and oversee advice, communication, accounts, and advisor activity under firm policy."),
            ("Substantiate", "Support a claim, recommendation, or statement with evidence or approved materials."),
            ("Refer", "Direct the client to another qualified professional for tax, legal, insurance, or specialized advice."),
            ("Update", "Refresh client information, risk profile, beneficiary details, or planning assumptions."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. First Meeting: The Client Wants the Hot Stock",
        "setting": "A new client asks the advisor to buy a popular stock immediately before discovery is complete.",
        "dialogue": [
            ("Client", "I want to put half my account into this stock before it runs higher."),
            ("Advisor", "I hear the urgency. Before I can make or support a recommendation, I need to understand your goals, risk profile, time horizon, liquidity needs, and current holdings."),
            ("ESL learner", "If this is an unsolicited decision, we can discuss process, but I do not want to treat a concentrated position as suitable or in your best interest without the facts."),
            ("Client", "So you are saying no?"),
            ("ESL learner", "I am saying we should slow the decision enough to understand the risk. Concentration can create large gains, but it can also damage the plan if the position moves against you."),
        ],
        "notes": [
            "The learner validates urgency without endorsing the trade.",
            "Use concentration, suitability, best interest, and discovery language carefully.",
        ],
    },
    {
        "title": "2. Explaining Fees and Conflicts",
        "setting": "A prospect compares a fee-based advisory account with a transaction-based brokerage account.",
        "dialogue": [
            ("Prospect", "Which account is cheaper?"),
            ("Advisor", "It depends on services, trading pattern, account size, and how you want advice delivered."),
            ("ESL learner", "A fee-based account may make sense if you want ongoing advice and monitoring. A transaction-based account may cost less if you rarely trade. We should also discuss conflicts: how the firm and advisor are compensated can affect recommendations."),
            ("Prospect", "That sounds like a conflict."),
            ("ESL learner", "It can be, which is why we disclose it and manage it. The important question is which account type fits your needs, not only which fee sounds lower in isolation."),
        ],
        "notes": [
            "Fee language should be clear, balanced, and not defensive.",
            "A lower fee is not automatically the better relationship if services differ.",
        ],
    },
    {
        "title": "3. Risk Profile: Tolerance vs Capacity",
        "setting": "A client scores aggressive on a questionnaire but needs cash in three years for a home purchase.",
        "dialogue": [
            ("Client", "I can handle risk. I want the highest return possible."),
            ("Advisor", "Your answers show high risk tolerance, but your home-purchase goal gives you lower risk capacity for that money."),
            ("ESL learner", "We can separate buckets. Long-term retirement assets may accept more volatility, but the down-payment funds need a shorter time horizon and higher liquidity."),
            ("Client", "So I cannot be aggressive?"),
            ("ESL learner", "You can be aggressive where the goal can tolerate volatility. For the home goal, the risk is not only market loss; it is missing the purchase timeline."),
        ],
        "notes": [
            "Risk tolerance and risk capacity are different and often conflict.",
            "Goal-based buckets can help explain why one client may need multiple allocations.",
        ],
    },
    {
        "title": "4. Market Drawdown: Client Wants to Sell Everything",
        "setting": "A retired client calls after a sharp market decline.",
        "dialogue": [
            ("Client", "I cannot watch this anymore. Sell everything and move to cash."),
            ("Advisor", "I understand why this feels painful. Before we act, let's look at your income plan, cash reserve, allocation, and what selling now would do to recovery potential."),
            ("ESL learner", "Your next twelve months of withdrawals are already set aside in short-term assets. The long-term bucket is down, but selling it now would make the temporary loss permanent."),
            ("Client", "What if the market keeps falling?"),
            ("ESL learner", "That is possible. We can review whether your plan still fits your risk capacity, but I would separate a disciplined adjustment from a panic sale."),
        ],
        "notes": [
            "Behavioral coaching validates emotion and returns to plan.",
            "Avoid predicting the market; focus on goals, liquidity, and process.",
        ],
    },
    {
        "title": "5. Retirement Income: RMD and Withdrawal Strategy",
        "setting": "A client approaching RMD age wants to know how much to withdraw.",
        "dialogue": [
            ("Client", "The custodian sent an RMD estimate. Should I take only that amount?"),
            ("Advisor", "The RMD is a minimum required amount for certain accounts, not necessarily your ideal spending strategy."),
            ("ESL learner", "We should coordinate the RMD with your cash-flow need, taxable income, charitable goals, and other accounts. For tax specifics, we should confirm with your CPA."),
            ("Client", "Can I take it from any account?"),
            ("ESL learner", "That depends on the account type and IRS rules. We can help organize the question and coordinate with the custodian and tax advisor before you act."),
        ],
        "notes": [
            "RMD conversations require careful referral and account-specific language.",
            "Do not turn a minimum distribution rule into a complete retirement-income recommendation.",
        ],
    },
    {
        "title": "6. Rollover Conversation: Four Options, Not One Shortcut",
        "setting": "A client changed jobs and asks whether to roll a 401(k) into an IRA.",
        "dialogue": [
            ("Client", "Should I roll the old 401(k) into an IRA with you?"),
            ("Advisor", "We should compare the options before deciding."),
            ("ESL learner", "The common options are leaving assets in the old plan, rolling to the new employer plan if allowed, rolling to an IRA, or cashing out. We need to compare fees, investment choices, services, creditor protections, tax impact, and your need for advice."),
            ("Client", "Which one do you recommend?"),
            ("ESL learner", "I can make a recommendation after we document the facts and alternatives. Because an IRA rollover may increase advisory fees, we need to be especially clear about the rationale."),
        ],
        "notes": [
            "Rollover language should compare alternatives and conflicts.",
            "Cash-out consequences should be discussed carefully and often with tax guidance.",
        ],
    },
    {
        "title": "7. Annuity Tradeoff: Guarantee vs Liquidity",
        "setting": "A client asks about buying an annuity after seeing an advertisement promising lifetime income.",
        "dialogue": [
            ("Client", "This annuity says I can get guaranteed income for life. Why would I not do it?"),
            ("Advisor", "Income guarantees can be valuable, but the tradeoffs matter."),
            ("ESL learner", "We need to review fees, surrender period, liquidity limits, inflation risk, insurer strength, tax treatment, and whether the benefit fits your income need better than other options."),
            ("Client", "But the guarantee sounds safe."),
            ("ESL learner", "It may reduce one type of risk, longevity risk, but it can introduce other constraints. The right question is which risk you are trying to solve and what flexibility you are willing to give up."),
        ],
        "notes": [
            "Product language should be balanced: benefit, cost, risk, constraint, fit.",
            "Guarantee language must be used carefully and with approved materials.",
        ],
    },
    {
        "title": "8. Concentrated Employer Stock",
        "setting": "A technology executive has most of their net worth in employer stock and resists diversification.",
        "dialogue": [
            ("Client", "This stock made me wealthy. I do not want to sell."),
            ("Advisor", "That history matters, and so does the concentration risk going forward."),
            ("ESL learner", "Your salary, bonus, unvested equity, and portfolio are all tied to the same company. Diversifying does not mean you lack confidence; it means you are protecting the wealth already created."),
            ("Client", "What if I sell and it doubles?"),
            ("ESL learner", "That regret risk is real. We can build a staged diversification plan, use price or time triggers, and coordinate tax strategy with your CPA."),
        ],
        "notes": [
            "Concentrated-stock conversations often involve identity and regret.",
            "A staged plan can address tax, emotion, and risk management.",
        ],
    },
    {
        "title": "9. Tax-Loss Harvesting: Useful but Not Magic",
        "setting": "A client asks whether selling losses means the portfolio did not really lose money.",
        "dialogue": [
            ("Client", "If we harvest losses, does that cancel the market loss?"),
            ("Advisor", "No. The investment loss is real. Tax-loss harvesting may create a tax asset that can help offset gains, subject to rules."),
            ("ESL learner", "We should avoid letting the tax benefit drive the investment decision by itself. We also need to watch wash-sale rules and keep the portfolio aligned with your target allocation."),
            ("Client", "So it helps but does not fix everything."),
            ("ESL learner", "Exactly. It is a tool, not a strategy by itself."),
        ],
        "notes": [
            "Tax-loss harvesting requires careful explanation and tax referral language.",
            "Do not imply tax treatment is guaranteed for a specific client without proper review.",
        ],
    },
    {
        "title": "10. Family Pressure and Trusted Contact",
        "setting": "An older client says a relative wants them to withdraw a large amount urgently.",
        "dialogue": [
            ("Client", "My nephew says I should send him money today for an investment."),
            ("Advisor", "That sounds important. Can we slow down and understand the purpose, amount, and whether anyone is pressuring you?"),
            ("ESL learner", "Your choice is yours, but because this is unusual and urgent, I want to protect you from possible financial exploitation. With your permission, we can involve your trusted contact or another professional you rely on."),
            ("Client", "I do not want to get anyone in trouble."),
            ("ESL learner", "The goal is not to accuse anyone. The goal is to make sure the decision is truly yours and that you understand the risk before assets leave the account."),
        ],
        "notes": [
            "Elder-risk language should be respectful, protective, and firm.",
            "Follow firm policy for trusted contact and escalation.",
        ],
    },
    {
        "title": "11. Client Complaint: 'You Never Told Me About the Fees'",
        "setting": "A client expresses dissatisfaction after seeing advisory fees on a statement.",
        "dialogue": [
            ("Client", "You never told me about these fees."),
            ("Advisor", "I am sorry this feels surprising. I want to understand exactly what you are seeing and review what was disclosed."),
            ("ESL learner", "I also need to treat your concern seriously and follow our firm's process. I will document your concern, provide the fee schedule again, and ask the supervisor to review the account history."),
            ("Client", "Are you saying this is my fault?"),
            ("ESL learner", "No. I am saying we should review the facts carefully and make sure your concern is handled through the proper channel."),
        ],
        "notes": [
            "Complaint language should not argue, blame, or dismiss.",
            "Many firms require escalation when a client expresses dissatisfaction.",
        ],
    },
    {
        "title": "12. Annual Review: Plan Change, Not Product Pitch",
        "setting": "An advisor leads an annual review after the client had a new child and changed jobs.",
        "dialogue": [
            ("Advisor", "Before we look at performance, let's update what changed in your life this year."),
            ("Client", "We had a baby, changed jobs, and may buy a larger home."),
            ("ESL learner", "Those changes affect emergency reserves, insurance needs, beneficiary designations, education planning, risk capacity, and cash-flow assumptions. The portfolio review should come after we update the plan inputs."),
            ("Client", "Does that mean we need new investments?"),
            ("ESL learner", "Maybe, but first we update the facts. Product changes should follow the plan, not lead it."),
        ],
        "notes": [
            "Good annual reviews begin with client facts, not performance slides.",
            "Planning changes may affect investment, insurance, estate, and cash-flow conversations.",
        ],
    },
]


PHRASE_BANK = {
    "Discovery and scope": [
        "Before I recommend a strategy, I need to understand your goals, time horizon, liquidity needs, tax status, and risk profile.",
        "That question touches tax or legal advice, so I can help coordinate the issue, but your CPA or attorney should confirm the answer.",
        "I can explain the tradeoffs, but I do not want to promise an outcome the market or tax rules cannot guarantee.",
        "Let's separate what you want emotionally from what the plan can support financially.",
    ],
    "Best interest, fees, and conflicts": [
        "The recommendation needs to fit your facts, not just sound attractive in general.",
        "This option may create compensation for the firm, so we should discuss the conflict and why the recommendation still fits.",
        "A lower fee is not always the better choice if the services and monitoring are different.",
        "I will document the alternatives we considered, the costs, the risks, and the reason for the recommendation.",
    ],
    "Risk and asset allocation": [
        "Your risk tolerance is high, but your risk capacity for this goal is lower because the money is needed soon.",
        "Diversification does not prevent loss, but it reduces dependence on one security, sector, or outcome.",
        "Rebalancing means we are following the plan, not reacting to headlines.",
        "The portfolio is designed for the goal and time horizon, not for beating every index every quarter.",
    ],
    "Retirement and tax-aware planning": [
        "The projection is a planning tool, not a guarantee.",
        "RMD rules set a minimum withdrawal for certain accounts, but your spending strategy may require a different amount.",
        "A Roth conversion may help long-term tax flexibility, but we need tax analysis before recommending an amount.",
        "Sequence risk matters because early retirement losses can make withdrawals harder to sustain.",
    ],
    "Volatility and behavior": [
        "I understand the desire to stop the pain. Let's review what selling now would do to your plan.",
        "We can make a disciplined adjustment, but I would separate that from a panic sale.",
        "Recent performance is important information, but it should not be the only reason to change strategy.",
        "The question is not whether volatility feels bad; it is whether the plan still fits your goals and risk capacity.",
    ],
    "Products and rollovers": [
        "A rollover decision should compare fees, services, investment choices, protections, tax impact, and your need for advice.",
        "The guarantee solves one risk, but we need to review the cost, liquidity limits, and conditions.",
        "This product may be appropriate for some clients, but we need to test fit before discussing implementation.",
        "Alternatives may add diversification, but they can also add complexity, illiquidity, and higher fees.",
    ],
    "Documentation and escalation": [
        "I will note the client facts, alternatives discussed, recommendation rationale, risks, costs, and follow-up items.",
        "Because you are expressing dissatisfaction, I need to follow our firm's complaint process.",
        "This looks unusual enough that I should involve a supervisor before any transaction occurs.",
        "Let's update your beneficiaries, trusted contact, and planning assumptions before changing the portfolio.",
    ],
}


WORKBOOK_TASKS = [
    "A prospect wants to invest half their account in one popular stock before discovery is complete. Write a response that validates urgency, explains process, and avoids endorsing concentration.",
    "A client asks why your advisory account costs more than a brokerage account. Write a balanced explanation of services, fees, conflicts, and account fit.",
    "A client has high risk tolerance but needs money in three years for a home purchase. Explain risk tolerance vs risk capacity and propose goal-based buckets.",
    "A retiree wants to sell everything after a market decline. Write your first five sentences and a follow-up question set.",
    "A client approaching RMD age asks whether to take only the minimum. Write an explanation with tax-referral language and planning context.",
    "A former employee asks whether to roll a 401(k) into an IRA. Compare the main options and identify the facts needed before a recommendation.",
    "An older client is being pressured by a relative to withdraw a large sum. Write protective, respectful language and an escalation note.",
    "A client says, 'You never told me about the fees.' Write a response that preserves the relationship and follows complaint-handling expectations.",
]


SOURCES = [
    "SEC Regulation Best Interest, Form CRS, Form ADV, and Investor.gov resources for retail investors and financial professionals.",
    "FINRA suitability, Reg BI, account, fee, asset allocation, diversification, and investor education resources.",
    "CFP Board Code of Ethics and Standards of Conduct for fiduciary, financial planning, client information, and professional conduct language.",
    "SEC investor education on asset allocation, diversification, rebalancing, risk tolerance, and investment professional selection.",
    "IRS retirement-plan and IRA required minimum distribution resources for RMD terminology and referral-aware retirement language.",
    "Firm compliance manuals, supervisory procedures, approved communications, and product-specific disclosures, which control actual workplace phrasing.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in financial-advice environments: financial advisors, investment advisers, wealth managers, retirement specialists, client service associates, paraplanners, planning analysts, portfolio-review teams, and advice-adjacent professionals."
        )
    )
    story.append(
        p(
            "The course is not a licensing course and does not train learners to give advice outside their role. It trains professional English for advice work: discovery, trust-building, recommendation rationale, disclosures, difficult client conversations, balanced product language, compliance-aware documentation, and supervised escalation."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "Financial-advice teams compress judgment into short phrases: best interest, suitability, risk capacity, IPS, RMD, rollover, surrender charge, tax-loss harvesting, concentrated position, trusted contact, complaint, Form CRS, and advisory fee. Learners need the vocabulary and the conversational habits around it: clarify, disclose, document, avoid guarantees, refer when needed, and connect every recommendation to client facts."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_advice_communication_principles(story: list) -> None:
    story += h1("Financial Advice Communication Principles")
    story.append(h2("Connect every recommendation to client facts"))
    story.append(
        p(
            "Financial-advice English should make the line visible between client facts and recommendation. A strong learner can say: this is the goal, these are the constraints, these alternatives were considered, these are the costs and risks, this conflict exists or may appear to exist, and this is why the recommendation fits."
        )
    )
    story.append(h2("Avoid promises, shortcuts, and role drift"))
    story.append(
        bullets(
            [
                "Use 'designed to' rather than 'will' when describing investment strategy.",
                "Use 'may' and 'subject to rules' when discussing tax outcomes, RMDs, and product features.",
                "Use 'I can coordinate with your CPA or attorney' when the conversation enters tax or legal advice.",
                "Use 'before I recommend...' when discovery is incomplete.",
                "Use 'I need to document and escalate this' when a client expresses dissatisfaction or possible exploitation appears.",
            ]
        )
    )
    story.append(h2("Turn emotional requests into planning questions"))
    story.append(
        table(
            [
                ["Client says", "Advisor turns it into"],
                ["I want to sell everything.", "Which goal, time horizon, liquidity need, and risk-capacity change would justify moving to cash?"],
                ["I want the hot stock.", "How much concentration risk can the plan tolerate, and what happens if the position falls sharply?"],
                ["This fee is too high.", "Which services, account type, compensation model, and conflict disclosures should we compare?"],
                ["Can I retire now?", "What spending, income, healthcare, taxes, inflation, longevity, and market assumptions need review?"],
            ],
            [2.0 * 72, 5.0 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a realistic sentence, ask a clarification question, and explain the client consequence. Because many terms have regulatory, firm-specific, product-specific, or tax-sensitive meanings, learners should ask which definition applies."
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
                    "When learners jump to a recommendation, ask: what client fact supports it, what alternative was considered, what risk or cost must be disclosed, what conflict exists, what documentation is needed, and whether the learner's role permits the statement."
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
                "Learner explains their financial-advice role in 90 seconds, including client types, services, products, supervised activities, and highest-risk conversations.",
                "Learner defines twelve advice terms and uses six in realistic client-facing sentences.",
                "Learner handles a short role-play: a client wants to liquidate a diversified portfolio during a market downturn.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but uses them loosely.", "Uses advice terms accurately in context.", "Defines terms, asks which standard applies, and adjusts to client and role."],
                ["Discovery", "Asks surface questions and moves quickly to product.", "Gathers goals, risk, time horizon, liquidity, tax, and constraints.", "Builds a client fact pattern that supports supervised advice and documentation."],
                ["Recommendation language", "States what the client should do without rationale.", "Connects recommendation to facts, alternatives, costs, risks, and conflicts.", "Explains fit and tradeoff while avoiding promises and role drift."],
                ["Difficult conversations", "Either validates panic or dismisses emotion.", "Acknowledges emotion and returns to plan, facts, and process.", "Coaches behavior while preserving dignity and compliance boundaries."],
                ["Documentation", "Writes vague notes after meetings.", "Records facts, rationale, alternatives, risks, costs, and follow-up.", "Creates notes usable for supervision, review, and client continuity."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead an annual review with a client who changed jobs, inherited money, holds concentrated employer stock, is worried about market volatility, and asks about rolling over a 401(k), buying an annuity, and helping an adult child. The learner must update client facts, avoid premature recommendations, explain tradeoffs, identify referrals and escalations, and write a compliance-aware follow-up note."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "Financial Advice English",
        "Instructor guide for high-level ESL learners working in wealth management, financial planning, retirement advice, and client-facing advisory roles",
        "Audience: instructors, financial-advice English coaches, wealth-management trainers, client-service teams, and advanced professional English programs",
    )
    add_course_opening(story)
    add_advice_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-financial-advice-english-instructor-guide.pdf",
        "EFSP Financial Advice English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Financial Advice English",
        "Participant workbook: discovery, client-safe recommendations, risk profiling, retirement conversations, products, fees, conflicts, and advice documentation",
        "Audience: advanced ESL learners working in financial advice, wealth management, retirement planning, client service, and advice-adjacent roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you sound precise, calm, and trustworthy in financial-advice conversations. The goal is not to sound like a sales script. The goal is to connect client facts to appropriate next steps while avoiding guarantees, unclear conflicts, and advice outside your role."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which client conversations are hardest for you: discovery, fees, volatility, rollovers, retirement income, product tradeoffs, family conflict, complaints, or documentation?",
                "Which financial-advice terms do you understand when reading but avoid when speaking?",
                "When a client is emotional or urgent, do you become too agreeable, too technical, too vague, or too direct?",
                "What is one recent meeting note or client email you wish you had written more carefully?",
            ]
        )
    )
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("Advice Process Language")
    story.append(
        table(
            [
                ["Stage", "Useful verbs", "Example sentence"],
                ["Discover", "ask, clarify, update, document, confirm", "Before recommending, we need to update your goals and liquidity needs."],
                ["Analyze", "compare, model, stress-test, evaluate, prioritize", "The plan is sensitive to retirement spending and healthcare assumptions."],
                ["Recommend", "explain, disclose, compare, justify, document", "This allocation fits the long-term goal but not the home-purchase funds."],
                ["Implement", "open, transfer, rebalance, coordinate, monitor", "We should coordinate the rollover steps with the custodian and your tax advisor."],
                ["Review", "revisit, rebalance, update, adjust, escalate", "The portfolio review should start with life changes, not only performance."],
                ["Protect", "refer, disclose, supervise, preserve, report", "This concern should be escalated under the firm's complaint process."],
            ],
            [1.15 * 72, 2.15 * 72, 3.7 * 72],
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
        "efsp-financial-advice-english-participant-workbook.pdf",
        "EFSP Financial Advice English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "Financial Advice Dialogue Lab",
        "Realistic advisor-client dialogues, role-play cards, and debrief prompts for advanced ESL learners",
        "Audience: instructors, financial-advice English coaches, wealth-management teams, client-service groups, and peer practice cohorts",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: advisor, client or colleague, observer.",
                "Read the model dialogue once. Then replay it with a different client profile, risk level, or compliance constraint.",
                "The observer listens for discovery, role boundaries, client-safe language, balanced product explanation, disclosure, documentation, and next step.",
                "After each role-play, replay the hardest 30 seconds with a more precise advisor sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners give actual investment, tax, legal, or insurance advice in class. Keep practice focused on language, process, client facts, risk explanation, documentation, referrals, and supervised escalation."
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
                    "Did the learner gather or update client facts before recommending?",
                    "Did the learner explain benefits, risks, costs, alternatives, and conflicts?",
                    "Did the learner avoid guarantees, tax/legal overreach, and unsupported product claims?",
                    "Did the learner document or escalate the next step when appropriate?",
                ]
            )
        )
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-financial-advice-dialogue-lab.pdf",
        "EFSP Financial Advice Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "Financial Advice Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise financial-advice vocabulary and client meeting language",
        "Audience: advanced ESL learners in wealth management, retirement planning, client service, paraplanning, portfolio support, and advisory teams",
    )
    story += h1("How to Use Advice Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it clarifies the client issue or recommendation rationale.",
                "Pair jargon with client facts: goal, time horizon, risk tolerance, risk capacity, liquidity need, tax status, costs, and alternatives.",
                "Define terms in plain English for clients, especially Form CRS, fiduciary, suitability, RMD, rollover, annuity, and tax-loss harvesting.",
                "Avoid guarantees, performance promises, unapproved tax/legal advice, and product claims outside approved materials.",
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
                ["Risk tolerance vs risk capacity", "Tolerance is emotional willingness; capacity is financial ability to absorb loss."],
                ["Education vs recommendation", "Education explains concepts; recommendation suggests a specific action or strategy based on client facts."],
                ["Financial advisor vs investment adviser", "Advisor is a broad market term; investment adviser is a regulated term with specific obligations."],
                ["Best interest vs guarantee", "Best-interest language concerns conduct and fit; it does not guarantee investment results."],
                ["Diversification vs no risk", "Diversification reduces concentration risk; it does not eliminate market loss."],
                ["Rollover vs transfer", "Rollover often involves retirement-account movement and consequences; transfer is broader and context-dependent."],
                ["Annuity income vs liquidity", "Annuities may provide income features but may limit liquidity and include costs or surrender charges."],
                ["Beneficiary vs trusted contact", "A beneficiary may receive assets after death; a trusted contact may be contacted under limited firm-policy circumstances."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-financial-advice-jargon-quick-reference.pdf",
        "EFSP Financial Advice Jargon Field Guide",
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
