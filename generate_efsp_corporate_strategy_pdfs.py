from __future__ import annotations

import html
from pathlib import Path

from reportlab.platypus import PageBreak, Paragraph, Spacer

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
                "Focus: high-level professional English for corporate strategy workplaces, including strategic diagnosis, where-to-play and how-to-win choices, tradeoffs, industry structure, competitive advantage, portfolio strategy, resource allocation, growth strategy, M&A logic, uncertainty, scenarios, operating model, OKRs, executive narratives, and board-level dialogue.",
                "Designed for advanced ESL learners who work in corporate strategy, business strategy, CEO office, transformation, corporate development, strategic finance, internal consulting, product strategy, commercial strategy, or strategy-adjacent leadership roles.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: corporate strategy English is the language of consequential choice. Learners need to frame ambiguous problems, make tradeoffs explicit, connect analysis to decisions, challenge attractive but incoherent ideas, and communicate uncertainty without sounding weak. This course teaches professional communication and judgment, not a single best strategy framework.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use corporate strategy terminology accurately in executive discussions, strategy reviews, portfolio meetings, market-entry debates, M&A screening, scenario planning, transformation governance, and board preparation.",
    "Translate vague strategic goals into diagnosis, strategic choices, hypotheses, evidence requirements, tradeoffs, resource implications, risks, and decision rights.",
    "Discuss industry structure, competitive advantage, customer value, profit pools, business models, portfolio roles, resource allocation, strategic options, and execution governance in precise professional English.",
    "Push back on weak strategy: generic ambition, activity lists, spreadsheet-only business cases, pet projects, unsupported synergy claims, no-choice roadmaps, vanity KPIs, and politically protected investments.",
    "Participate in realistic strategy dialogues: CEO problem framing, where-to-play debate, Five Forces analysis, portfolio review, resource allocation, market entry, M&A synergy challenge, scenario planning, board-story revision, and KPI alignment.",
    "Write clear strategy outputs: issue trees, strategy memos, market-attractiveness summaries, investment theses, portfolio recommendations, scenario implications, executive decision notes, and board-ready storylines.",
]


MODULES = [
    {
        "title": "Module 1. Strategy Role, Problem Framing, and Executive Diagnosis",
        "time": "90 minutes",
        "big_idea": "Corporate strategy work begins before analysis. Learners must frame the real decision, separate symptoms from causes, identify the executive audience, and define what would change if the analysis is persuasive.",
        "objectives": [
            "Distinguish problem statement, symptom, root cause, hypothesis, issue tree, decision question, recommendation, and implementation implication.",
            "Ask executive-level clarification questions without sounding junior or obstructive.",
            "Write a concise diagnosis that names the strategic tension rather than listing every fact.",
        ],
        "concepts": [
            "Diagnosis: a disciplined explanation of what is happening, why it matters, and what tension the organization must resolve.",
            "Decision question: the specific choice leadership needs to make, not just the topic under discussion.",
            "Issue tree: structured breakdown of the problem into mutually useful questions that guide analysis.",
        ],
        "activities": [
            "Problem reframing: learners convert vague mandates into decision questions.",
            "Issue-tree drill: learners build a strategy issue tree under time pressure.",
            "Executive diagnosis practice: learners summarize a messy business situation in three sentences.",
        ],
        "outputs": [
            "Problem statement and decision question.",
            "Issue tree with hypotheses.",
            "Executive diagnosis memo.",
        ],
    },
    {
        "title": "Module 2. Strategic Choices: Ambition, Where to Play, How to Win, and Tradeoffs",
        "time": "90 minutes",
        "big_idea": "A strategy is not a slogan or a project list. It is a set of choices about where the company will compete, how it will win, what capabilities it needs, and what it will not do.",
        "objectives": [
            "Use choice language for ambition, where to play, how to win, capabilities, systems, and management priorities.",
            "Explain tradeoffs without sounding negative or risk-averse.",
            "Identify whether an initiative supports the strategy or merely sounds attractive.",
        ],
        "concepts": [
            "Where to play: the customers, geographies, channels, segments, use cases, or parts of the value chain the company chooses to prioritize.",
            "How to win: the distinctive logic by which the company creates superior value or lower cost compared with alternatives.",
            "Tradeoff: a deliberate choice to deprioritize some opportunities so the chosen strategy can be coherent and resourced.",
        ],
        "activities": [
            "Choice cascade: learners test whether a proposed strategy makes real choices.",
            "Tradeoff rehearsal: learners explain what the company should stop, delay, or reject.",
            "Strategy vs slogan: learners classify statements as ambition, analysis, choice, initiative, or metric.",
        ],
        "outputs": [
            "Strategy choice map.",
            "Tradeoff statement.",
            "Strategic coherence checklist.",
        ],
    },
    {
        "title": "Module 3. Industry Structure, Competitive Dynamics, and Profit Pools",
        "time": "90 minutes",
        "big_idea": "Attractive growth is not always attractive profit. Learners need language for industry structure, Five Forces, profit pools, competitor moves, barriers, substitutes, and shifting value capture.",
        "objectives": [
            "Discuss market attractiveness using Five Forces, profit-pool logic, growth, margin, cyclicality, regulation, and structural change.",
            "Explain why a growing market may still be strategically unattractive.",
            "Distinguish competitor activity from competitive advantage.",
        ],
        "concepts": [
            "Industry structure: the competitive forces that shape how value is created and captured in a market.",
            "Profit pool: where profit accumulates across the value chain, customer segments, geographies, or business models.",
            "Barrier to entry: structural factor that makes it difficult or costly for new competitors to enter and compete effectively.",
        ],
        "activities": [
            "Five Forces readout: learners assess an industry and identify the highest-pressure force.",
            "Profit-pool map: learners locate where economics are strong and weak across a value chain.",
            "Competitor move drill: learners separate noise from moves that change industry structure.",
        ],
        "outputs": [
            "Industry-attractiveness summary.",
            "Profit-pool map narrative.",
            "Competitive implications memo.",
        ],
    },
    {
        "title": "Module 4. Business Models, Unit Economics, Capabilities, and Advantage",
        "time": "90 minutes",
        "big_idea": "Corporate strategy must explain how value is created, captured, defended, and scaled. Learners need to connect customer value, economics, capabilities, activities, and operating model.",
        "objectives": [
            "Use business-model and financial terms such as revenue model, gross margin, contribution margin, CAC, LTV, ROIC, WACC, DCF, NPV, and payback accurately.",
            "Explain strategic advantage in terms of activities, capabilities, cost position, differentiation, switching costs, data, distribution, brand, or scale.",
            "Challenge business cases that assume growth without credible economics or capabilities.",
        ],
        "concepts": [
            "Business model: how the company creates value for customers and captures economic value for itself.",
            "Unit economics: revenue, cost, margin, acquisition cost, retention, and payback at the customer, product, or transaction level.",
            "Capability system: reinforcing skills, processes, assets, data, culture, and operating routines that enable the strategy.",
        ],
        "activities": [
            "Unit-economics challenge: learners identify where a growth plan breaks economically.",
            "Capability gap analysis: learners compare required capabilities with current reality.",
            "Advantage explanation: learners explain why a competitor cannot easily copy a strategy.",
        ],
        "outputs": [
            "Business-model narrative.",
            "Capability gap summary.",
            "Advantage thesis.",
        ],
    },
    {
        "title": "Module 5. Portfolio Strategy, Capital Allocation, and Resource Reallocation",
        "time": "90 minutes",
        "big_idea": "Corporate strategy often fails because resources do not move. Learners need language for portfolio roles, capital allocation, mature cash businesses, growth bets, divestitures, adjacency, opportunity cost, and management politics.",
        "objectives": [
            "Use portfolio terminology accurately: core, adjacency, horizon, business unit, capital allocation, resource reallocation, hurdle rate, divestiture, stranded cost, and opportunity cost.",
            "Discuss investment, hold, harvest, partner, acquire, divest, and exit recommendations.",
            "Push back when every business unit requests equal growth funding despite different economics and strategic roles.",
        ],
        "concepts": [
            "Portfolio role: the job a business or initiative plays in the enterprise, such as cash generation, growth option, strategic control point, or capability platform.",
            "Resource reallocation: shifting capital, talent, management attention, and operating expense toward higher-value strategic choices.",
            "Opportunity cost: value lost when scarce resources remain tied to lower-priority options.",
        ],
        "activities": [
            "Portfolio heat map: learners classify businesses by attractiveness, advantage, cash generation, and strategic fit.",
            "Capital allocation role-play: learners defend a resource shift in front of business-unit leaders.",
            "Divestiture language drill: learners explain exit logic without sounding dismissive of the team.",
        ],
        "outputs": [
            "Portfolio recommendation.",
            "Resource reallocation script.",
            "Investment committee memo.",
        ],
    },
    {
        "title": "Module 6. Growth Strategy, Market Entry, Partnerships, and M&A Logic",
        "time": "90 minutes",
        "big_idea": "Growth strategy requires a clear thesis: where growth will come from, why the company has a right to win, what route to market is credible, and whether to build, buy, partner, or wait.",
        "objectives": [
            "Use terms such as organic growth, inorganic growth, adjacency, market entry, beachhead, build-buy-partner, joint venture, strategic alliance, acquisition thesis, synergy, integration risk, and cannibalization.",
            "Explain why a market may be attractive but still not a good fit.",
            "Challenge unsupported M&A or partnership logic with questions about value creation, integration, control, culture, and downside risk.",
        ],
        "concepts": [
            "Right to play: permission or relevance to compete in a market based on brand, access, capabilities, assets, or customer relationships.",
            "Right to win: credible basis for outperforming alternatives once in the market.",
            "Synergy: incremental value from combining assets, capabilities, customers, channels, cost structures, or technology, net of integration cost and risk.",
        ],
        "activities": [
            "Market-entry screen: learners evaluate attractiveness, fit, economics, and execution difficulty.",
            "Build-buy-partner debate: learners compare routes to market under speed, control, risk, and capability constraints.",
            "Synergy challenge: learners test whether projected synergies are real, timed, owned, and measurable.",
        ],
        "outputs": [
            "Market-entry recommendation.",
            "Build-buy-partner comparison.",
            "M&A thesis and risk note.",
        ],
    },
    {
        "title": "Module 7. Uncertainty, Scenarios, Strategic Options, and Risk Posture",
        "time": "90 minutes",
        "big_idea": "A strong strategist does not pretend the future is certain. Learners need language for scenarios, residual uncertainty, trigger indicators, no-regrets moves, options, big bets, shaping, adapting, and reserving the right to play.",
        "objectives": [
            "Discuss uncertainty without sounding indecisive.",
            "Create scenario implications that change decisions, not decorative future stories.",
            "Recommend strategic moves based on uncertainty level, risk appetite, and trigger indicators.",
        ],
        "concepts": [
            "Residual uncertainty: uncertainty that remains after good analysis has been completed.",
            "No-regrets move: action likely to create value across multiple plausible futures.",
            "Strategic option: limited investment that preserves the ability to scale, pivot, or exit as uncertainty resolves.",
        ],
        "activities": [
            "Scenario cleanup: learners remove scenarios that do not change decisions.",
            "Trigger indicator drill: learners define what the team should monitor and when to revisit the decision.",
            "Options vs big bets: learners recommend the right move under different uncertainty conditions.",
        ],
        "outputs": [
            "Scenario implications table.",
            "Trigger indicator dashboard.",
            "Risk posture recommendation.",
        ],
    },
    {
        "title": "Module 8. Execution Governance, Operating Model, KPIs, and Board Narrative",
        "time": "90 minutes",
        "big_idea": "Strategy becomes real through operating model, decision rights, resource shifts, milestones, KPIs, governance, and narrative discipline. Learners must convert strategy into accountable execution without turning it into a long project inventory.",
        "objectives": [
            "Use execution terms such as operating model, governance, decision rights, initiative, roadmap, milestone, dependency, OKR, KPI, leading indicator, lagging indicator, value driver, and board narrative.",
            "Separate strategic KPIs from activity metrics.",
            "Build an executive or board storyline that names choices, evidence, risk, resource implications, and decisions needed.",
        ],
        "concepts": [
            "Operating model: how structure, roles, processes, governance, capabilities, and incentives support the strategy.",
            "Decision rights: clarity on who recommends, decides, executes, and escalates.",
            "Board narrative: concise strategic story designed for oversight and decision, not a complete working file.",
        ],
        "activities": [
            "KPI cleanup: learners replace activity metrics with strategic value drivers.",
            "Governance role-play: learners clarify owners, decision rights, and escalation paths.",
            "Board deck rewrite: learners turn an analysis-heavy deck into a decision-ready storyline.",
        ],
        "outputs": [
            "Strategic KPI set.",
            "Governance and decision-rights map.",
            "Board-ready executive summary.",
        ],
    },
]


JARGON_GROUPS = [
    (
        "Strategy foundations",
        [
            ("Ambition", "High-level performance or market position the company wants to achieve."),
            ("Diagnosis", "Explanation of the strategic problem, its cause, and why it matters now."),
            ("Strategic choice", "Decision about where to focus, how to win, what to build, and what not to do."),
            ("Tradeoff", "A deliberate decision to deprioritize one attractive option to make another choice coherent."),
            ("Strategic thesis", "Argument for why a course of action should create advantage or value."),
            ("Issue tree", "Structured breakdown of a problem into analyzable questions."),
            ("North Star", "Single guiding objective or metric that aligns strategic direction."),
            ("Activity system", "Reinforcing set of activities that makes a strategy harder to copy."),
        ],
    ),
    (
        "Market and competitive analysis",
        [
            ("TAM", "Total addressable market; full demand opportunity if all relevant customers were served."),
            ("SAM", "Serviceable available market; portion the company can realistically reach with its offer and model."),
            ("SOM", "Serviceable obtainable market; share the company can reasonably capture."),
            ("Profit pool", "Where profit accumulates across segments, value chain positions, or business models."),
            ("Five Forces", "Framework for industry structure: entrants, suppliers, buyers, substitutes, and rivalry."),
            ("Barrier to entry", "Structural obstacle that limits new competitors."),
            ("Substitute", "Different product or service that meets the same underlying need."),
            ("White space", "Underserved market, customer need, or value-chain position where the company may compete."),
        ],
    ),
    (
        "Portfolio and resource allocation",
        [
            ("Core business", "Current business central to revenue, profit, capabilities, or strategic identity."),
            ("Adjacency", "Growth area near the core by customer, channel, capability, geography, or value chain."),
            ("Horizon one", "Current core businesses that deliver most present profit and cash flow."),
            ("Horizon two", "Emerging opportunities that may become significant future businesses."),
            ("Horizon three", "Earlier options, pilots, or ventures that could create future growth."),
            ("Capital allocation", "Decision process for assigning capital to businesses, initiatives, acquisitions, or returns."),
            ("Divestiture", "Sale, exit, or separation of a business, asset, or product line."),
            ("Opportunity cost", "Value sacrificed by keeping scarce resources in a lower-priority use."),
        ],
    ),
    (
        "Growth, M&A, and partnerships",
        [
            ("Organic growth", "Growth generated from existing business activities, customers, products, or channels."),
            ("Inorganic growth", "Growth through acquisition, merger, joint venture, or investment."),
            ("Market entry", "Plan to enter a new geography, segment, category, or value-chain position."),
            ("Build-buy-partner", "Comparison of internal development, acquisition, and partnership routes."),
            ("Right to play", "Credible permission or relevance to compete in a market."),
            ("Right to win", "Credible basis for outperforming alternatives in that market."),
            ("Synergy", "Incremental value from combining businesses, assets, capabilities, customers, or costs."),
            ("PMI", "Post-merger integration; work required to combine and realize value after a deal."),
        ],
    ),
    (
        "Value creation and financial logic",
        [
            ("ROIC", "Return on invested capital; profit relative to capital invested in the business."),
            ("WACC", "Weighted average cost of capital; benchmark return required by capital providers."),
            ("DCF", "Discounted cash flow valuation based on expected future cash flows."),
            ("NPV", "Net present value; value of future cash flows after discounting and subtracting investment."),
            ("EBITDA", "Earnings before interest, taxes, depreciation, and amortization."),
            ("Margin expansion", "Improvement in profitability as a share of revenue."),
            ("Sensitivity", "Analysis showing how results change when key assumptions change."),
            ("Value driver", "Factor that materially affects enterprise value, such as growth, margin, capital intensity, or risk."),
        ],
    ),
    (
        "Uncertainty and risk",
        [
            ("Scenario planning", "Structured analysis of plausible futures and their implications for decisions."),
            ("Residual uncertainty", "Uncertainty remaining after strong analysis has been completed."),
            ("Trigger indicator", "Signal that shows which scenario may be unfolding and when to revisit a decision."),
            ("No-regrets move", "Action likely to create value across multiple plausible futures."),
            ("Strategic option", "Limited investment that preserves future ability to scale, pivot, or exit."),
            ("Big bet", "Large commitment that could create major upside or major loss depending on future conditions."),
            ("Risk appetite", "Amount and type of risk leadership is willing to accept to pursue value."),
            ("Resilience", "Ability of the strategy and organization to absorb shocks and keep creating value."),
        ],
    ),
    (
        "Execution and governance",
        [
            ("Operating model", "How structure, roles, processes, governance, incentives, and capabilities support strategy."),
            ("Decision rights", "Clarity on who recommends, decides, executes, and escalates."),
            ("OKR", "Objectives and key results; goal-setting system linking outcomes to measurable progress."),
            ("KPI", "Key performance indicator tied to a strategic objective or decision."),
            ("Roadmap", "Sequenced plan of initiatives, milestones, dependencies, and owners."),
            ("Governance cadence", "Regular rhythm for decision, review, escalation, and accountability."),
            ("Transformation office", "Team coordinating large-scale strategic change and value delivery."),
            ("Board narrative", "Concise strategy story for oversight, alignment, and decision-making."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. CEO Request: 'We Need a Strategy'",
        "setting": "The CEO asks the strategy team for a strategy, but the request sounds like a list of initiatives.",
        "dialogue": [
            ("CEO", "We need a strategy for next year. Give me the top twenty initiatives."),
            ("Strategy lead", "We can build the initiative list, but first we need the strategic choice behind it."),
            ("ESL learner", "If the output is only a project list, we may miss the real decision. Are we trying to defend the core, enter a new segment, improve margins, or shift resources toward higher-growth businesses?"),
            ("CEO", "All of the above."),
            ("ESL learner", "Then the first decision is prioritization. We should define the few choices that matter most, the tradeoffs they imply, and the resources that must move."),
        ],
        "notes": [
            "Strategy language should separate choices from activities.",
            "A broad CEO request often needs reframing before analysis begins.",
        ],
    },
    {
        "title": "2. Where-to-Play Debate: Enterprise vs Mid-Market",
        "setting": "A leadership team is debating whether to prioritize enterprise customers or mid-market customers.",
        "dialogue": [
            ("CRO", "Enterprise logos create credibility. We should focus there."),
            ("Product head", "Mid-market customers adopt faster and need fewer custom features."),
            ("ESL learner", "The where-to-play choice affects product roadmap, sales motion, implementation cost, pricing, and support model. Enterprise may increase contract value, but mid-market may improve velocity and margins."),
            ("CRO", "Can we do both?"),
            ("ESL learner", "Possibly, but not with the same operating model. If we choose both, we need explicit segmentation and different service levels, not one vague strategy."),
        ],
        "notes": [
            "Where-to-play choices change capabilities and economics.",
            "Doing both can be valid only if the operating model supports it.",
        ],
    },
    {
        "title": "3. Five Forces: Growth Does Not Mean Profit",
        "setting": "A team wants to enter a fast-growing market but has not examined industry structure.",
        "dialogue": [
            ("Business unit GM", "The market is growing 18 percent. We should enter quickly."),
            ("Analyst", "Growth is strong, but supplier power and buyer power are also high."),
            ("ESL learner", "Market growth is attractive, but the profit pool may be weak. If buyers can switch easily, suppliers control key inputs, and substitutes are improving, growth may not translate into returns."),
            ("GM", "So you are saying no?"),
            ("ESL learner", "Not necessarily. I am saying entry needs a clear position, a barrier we can build, and economics that survive competitive pressure."),
        ],
        "notes": [
            "Industry attractiveness requires more than growth rate.",
            "Use Five Forces to discuss value capture, not just competition.",
        ],
    },
    {
        "title": "4. Portfolio Review: Protect the Core or Fund the New Bet",
        "setting": "A mature business funds the company, but a new opportunity needs investment.",
        "dialogue": [
            ("Core BU leader", "Our unit generates the cash. Cutting our budget will damage the business."),
            ("Innovation lead", "Without investment, the new platform will miss the window."),
            ("ESL learner", "The portfolio question is not which team deserves funding. It is what role each business plays. The core must remain healthy, but some resources may need to shift if the new platform is the stronger future value pool."),
            ("Core BU leader", "That sounds like punishing performance."),
            ("ESL learner", "I would frame it as funding enterprise value. We should define the minimum investment to protect the core and the incremental investment needed to test the new platform's thesis."),
        ],
        "notes": [
            "Portfolio language should reduce personal defensiveness.",
            "Resource allocation must connect to enterprise value, not politics.",
        ],
    },
    {
        "title": "5. Resource Allocation: Everyone Wants Flat Growth",
        "setting": "Every business unit requests a similar budget increase despite different performance and market opportunities.",
        "dialogue": [
            ("CFO", "Every BU is asking for 8 percent more. That is not a strategy."),
            ("BU leader", "We all have growth plans."),
            ("ESL learner", "Equal increases may feel fair, but they ignore opportunity cost. We should allocate based on market attractiveness, advantage, capital intensity, confidence in execution, and strategic role."),
            ("BU leader", "My team will see that as a cut."),
            ("ESL learner", "Then we need transparent decision rules. Some units may get growth capital, some may get productivity targets, and some may need option funding rather than full-scale investment."),
        ],
        "notes": [
            "Fairness language can hide strategic inertia.",
            "Decision rules help make resource shifts defensible.",
        ],
    },
    {
        "title": "6. Market Entry: Build, Buy, or Partner",
        "setting": "The company wants to enter an adjacent market but lacks several capabilities.",
        "dialogue": [
            ("Corporate development", "We can acquire a player and accelerate entry."),
            ("Operations", "Integration could distract the organization for two years."),
            ("ESL learner", "The route depends on speed, control, capability gap, integration risk, and economics. Build gives control but may be slow. Buy gives access but may overpay. Partner creates optionality but limits control."),
            ("CEO", "What do you recommend?"),
            ("ESL learner", "Start with a partnership to validate demand and operating requirements, while screening acquisition targets if the thesis proves attractive."),
        ],
        "notes": [
            "Build-buy-partner language should compare route, not just preference.",
            "Options can be a strategy under uncertainty.",
        ],
    },
    {
        "title": "7. M&A Synergy Challenge",
        "setting": "A deal team presents synergy estimates that sound optimistic.",
        "dialogue": [
            ("Deal lead", "The acquisition creates 60 million in annual synergies."),
            ("CFO", "Where exactly do those synergies come from?"),
            ("ESL learner", "We should separate revenue synergies, cost synergies, tax or procurement benefits, and capability synergies. Each needs an owner, timing, one-time cost, and confidence level."),
            ("Deal lead", "The revenue synergies are strategic."),
            ("ESL learner", "Strategic is not enough. Which customers, which products, which channel, what attach rate, and what evidence tells us the combined company can capture it?"),
        ],
        "notes": [
            "Synergy language should move from headline value to source, timing, owner, and evidence.",
            "Revenue synergies usually need especially careful challenge.",
        ],
    },
    {
        "title": "8. Scenario Planning: Regulatory Uncertainty",
        "setting": "A new regulation could change the economics of a business model.",
        "dialogue": [
            ("General counsel", "We do not know how the rule will be finalized."),
            ("Strategy director", "Then we need scenarios."),
            ("ESL learner", "Let's build only scenarios that would change our decision. For each one, we need trigger indicators, financial impact, operational implications, and moves that are no-regrets across scenarios."),
            ("CEO", "What can we do now?"),
            ("ESL learner", "We can reduce exposure in the highest-risk product, invest in compliance capability, and create an option to shift the model if the strict scenario becomes more likely."),
        ],
        "notes": [
            "Scenario planning should guide decisions, not decorate decks.",
            "Use trigger indicators to avoid passive waiting.",
        ],
    },
    {
        "title": "9. Strategy vs Operational Effectiveness",
        "setting": "A cost-reduction program is being presented as the company's strategy.",
        "dialogue": [
            ("COO", "Our strategy is to improve productivity by 12 percent."),
            ("Strategy lead", "That is important, but it may be operational effectiveness rather than strategy."),
            ("ESL learner", "Productivity improvement can support strategy, but it does not answer where we will compete differently or how we will win. We need to connect the cost program to a position: lower-cost leadership, reinvestment in growth, or a more focused operating model."),
            ("COO", "So the cost program is not strategic?"),
            ("ESL learner", "It can be strategic if it enables a choice. By itself, it is an initiative with financial benefit."),
        ],
        "notes": [
            "Operational improvement can be valuable without being the whole strategy.",
            "The learner should avoid sounding dismissive while clarifying the distinction.",
        ],
    },
    {
        "title": "10. KPI Conflict: Activity Metrics vs Strategic Outcomes",
        "setting": "A transformation dashboard shows many green projects, but business results are flat.",
        "dialogue": [
            ("Transformation office", "Ninety percent of initiatives are on track."),
            ("CEO", "Then why is margin not improving?"),
            ("ESL learner", "The dashboard may be tracking activity rather than value. We need to link initiatives to value drivers: price, volume, mix, cost-to-serve, retention, working capital, and capital intensity."),
            ("Transformation office", "The teams like milestone tracking."),
            ("ESL learner", "Milestones are useful, but the executive dashboard should show whether strategic outcomes are moving, not just whether workstreams are busy."),
        ],
        "notes": [
            "Green status can hide weak value delivery.",
            "Strategic KPIs should connect to value drivers.",
        ],
    },
    {
        "title": "11. Board Deck: Too Much Analysis, No Decision",
        "setting": "The strategy team has a 70-page deck but no clear board decision.",
        "dialogue": [
            ("Board chair", "What decision do you need from us?"),
            ("Strategy VP", "We wanted to share the full market analysis."),
            ("ESL learner", "The analysis supports one decision: whether to shift 200 million from legacy expansion to the digital platform over three years. The board needs the strategic logic, downside case, risk controls, and milestones for releasing capital."),
            ("Board chair", "Then lead with that."),
            ("ESL learner", "Agreed. We can move the market detail to appendix and open with the choice, recommendation, and resource implications."),
        ],
        "notes": [
            "Board communication should be decision-led.",
            "Appendix detail should support the recommendation, not bury it.",
        ],
    },
    {
        "title": "12. Sunk Cost: Politically Protected Initiative",
        "setting": "A senior sponsor wants to continue a failing initiative because the company has already invested heavily.",
        "dialogue": [
            ("Sponsor", "We have spent two years on this. We cannot stop now."),
            ("CFO", "The economics have deteriorated."),
            ("ESL learner", "The prior investment is real, but the decision should be based on future value, remaining cost, strategic fit, and alternatives. Continuing only because we already spent money would increase opportunity cost."),
            ("Sponsor", "Stopping will look like failure."),
            ("ESL learner", "We can position the recommendation as disciplined reallocation. The learning still has value, but the next dollar may create more value elsewhere."),
        ],
        "notes": [
            "Sunk-cost language needs tact because identity and politics are involved.",
            "Reallocation framing can protect dignity while changing course.",
        ],
    },
]


PHRASE_BANK = {
    "Problem framing and diagnosis": [
        "What decision will this analysis change?",
        "The issue is not only growth; it is whether the growth creates attractive returns.",
        "I would separate the symptom from the strategic cause.",
        "Before we build the model, we should align on the decision question.",
    ],
    "Strategic choices and tradeoffs": [
        "This is a choice, not just a priority statement.",
        "If we choose this segment, what are we explicitly not serving?",
        "The strategy becomes clearer when the tradeoff is visible.",
        "We can do both only if the operating model supports both.",
    ],
    "Market and competitive analysis": [
        "Market growth is attractive, but we need to test value capture.",
        "Which force puts the most pressure on industry profitability?",
        "The competitor move matters only if it changes economics, access, or customer behavior.",
        "The profit pool is shifting, but not necessarily toward us.",
    ],
    "Portfolio and resource allocation": [
        "Equal funding is not the same as strategic funding.",
        "What role should this business play in the enterprise portfolio?",
        "The resource shift should follow market attractiveness, advantage, and strategic fit.",
        "We should define the minimum investment to protect the core and the option funding for future growth.",
    ],
    "Growth, M&A, and partnerships": [
        "Attractive market does not automatically mean right to win.",
        "Build gives control, buy gives speed, and partner gives optionality.",
        "The synergy case needs source, timing, owner, cost, and confidence level.",
        "The acquisition thesis should explain why we are the best owner of the asset.",
    ],
    "Uncertainty and executive communication": [
        "The future is uncertain, but the decision does not have to be vague.",
        "Which trigger indicators would cause us to revisit the plan?",
        "This is a no-regrets move across the scenarios we tested.",
        "For the board, I would lead with the decision, recommendation, risk, and resource implication.",
    ],
}


WORKBOOK_TASKS = [
    "A CEO asks for a strategy but describes a list of projects. Write a response that reframes the work around a decision question and strategic choices.",
    "Leadership wants to pursue enterprise and mid-market at the same time. Write a tradeoff note that explains operating-model implications.",
    "A fast-growing market has weak profit-pool evidence. Prepare a Five Forces and value-capture summary.",
    "A business case assumes growth but has weak unit economics. Write five challenge questions and a revised recommendation.",
    "Every business unit requests the same budget increase. Draft decision rules for resource allocation and a difficult message to underfunded units.",
    "A corporate development team proposes an acquisition with vague revenue synergies. Write a synergy challenge memo.",
    "Regulatory uncertainty could change a market-entry decision. Create scenario implications, trigger indicators, and no-regrets moves.",
    "A board deck has too much analysis and no clear decision. Rewrite the opening storyline in five sentences.",
]


SOURCES = [
    "Harvard Business School and Institute for Strategy and Competitiveness resources on Michael Porter's strategy, strategic positioning, tradeoffs, activity systems, and Five Forces.",
    "McKinsey three horizons framework for balancing current performance, emerging opportunities, and future growth options.",
    "McKinsey strategy-under-uncertainty materials for residual uncertainty, scenarios, trigger indicators, options, big bets, and no-regrets moves.",
    "McKinsey resource-allocation research for capital allocation, reallocation inertia, and linking resources to strategic goals.",
    "BCG growth-share matrix resources for portfolio management, relative market share, growth, investment, harvest, and divestiture language.",
    "SEC Management's Discussion and Analysis guidance for public-company discipline around management perspective, material information, known trends, uncertainty, and disclosure-oriented strategy language.",
    "The learner's own company strategy process, board calendar, investor materials, financial planning rules, governance model, and approved terminology.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in corporate strategy environments: corporate strategy teams, CEO office, business strategy, corporate development, transformation, strategic finance, internal consulting, product strategy, commercial strategy, and leadership roles that require enterprise-level decisions."
        )
    )
    story.append(
        p(
            "The course is not an MBA survey. It trains professional English for strategy work: diagnosing ambiguous problems, framing choices, challenging assumptions, explaining tradeoffs, defending resource allocation, discussing uncertainty, and turning analysis into executive decisions."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "Corporate strategy teams compress high-stakes judgment into short phrases: where to play, how to win, tradeoff, activity system, profit pool, Five Forces, right to win, adjacency, horizon two, resource reallocation, NPV, ROIC, synergy, scenario, no-regrets move, trigger indicator, operating model, decision rights, and board narrative. Learners need the terms and the dialogue moves around them: clarify the decision, connect evidence to value, name uncertainty, and make choices visible."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_strategy_communication_principles(story: list) -> None:
    story += h1("Corporate Strategy Communication Principles")
    story.append(h2("Lead with the decision"))
    story.append(
        p(
            "Strategy work often produces large amounts of analysis, but executives need to know what choice is being proposed, what evidence supports it, what tradeoffs it implies, what resources must move, and what risks remain. Strong strategy English is decision-led, not data-dumped."
        )
    )
    story.append(h2("Make tradeoffs explicit"))
    story.append(
        bullets(
            [
                "Use 'the strategic choice is' when the team is confusing priority with preference.",
                "Use 'the tradeoff is' when leadership wants to pursue incompatible paths.",
                "Use 'the value pool is shifting' when revenue growth does not guarantee profit capture.",
                "Use 'the right to win is not yet clear' when a market looks attractive but the company lacks advantage.",
                "Use 'the next dollar' when challenging sunk-cost logic.",
            ]
        )
    )
    story.append(h2("Turn vague strategy talk into executive questions"))
    story.append(
        table(
            [
                ["Vague strategy statement", "Stronger executive question"],
                ["We need a growth strategy.", "Which growth source, with what right to win, economics, capability gap, and resource shift?"],
                ["Let's enter the market.", "Is the market attractive, can we capture value, and what route gives us speed, control, and acceptable risk?"],
                ["This is a strategic acquisition.", "What is the acquisition thesis, synergy source, integration risk, and alternative use of capital?"],
                ["All initiatives are green.", "Which strategic outcomes are improving, and which value drivers explain the result?"],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a realistic sentence, ask which evidence or definition applies, and explain the consequence for a decision. Strategy terms are often used loosely; the learner's job is to make them useful."
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
                    "When learners give a generic strategy answer, ask: what is the decision, where will we play, how will we win, what tradeoff is required, what evidence supports the thesis, what resources must move, and what would cause us to change course?"
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
                "Learner explains their strategy role in 90 seconds, including executive audience, planning cycle, analysis tools, decision forums, and hardest stakeholder conversations.",
                "Learner defines twelve strategy terms and uses six in realistic executive sentences.",
                "Learner handles a short role-play: a CEO asks for a growth strategy but refuses to make tradeoffs.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Uses strategy terms as buzzwords.", "Uses terms accurately and defines them in context.", "Clarifies definitions, evidence, and implications for executive decisions."],
                ["Problem framing", "Accepts vague mandates as given.", "Turns ambiguity into decision questions and hypotheses.", "Identifies the real strategic tension and what must change."],
                ["Tradeoff discipline", "Avoids conflict by supporting everything.", "Names choices and resource implications.", "Makes tradeoffs constructive, explicit, and tied to enterprise value."],
                ["Analytical judgment", "Reports data without recommendation.", "Connects analysis to value, risk, and options.", "Challenges weak logic while preserving executive trust."],
                ["Executive communication", "Presents too much detail or caveat.", "Leads with recommendation and key evidence.", "Builds decision-ready narratives for senior leaders and boards."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a corporate strategy review. The company faces slowing core growth, a tempting adjacent market, an acquisition target with questionable synergies, pressure to give every business unit equal funding, and regulatory uncertainty. The learner must frame the strategic choice, assess industry attractiveness, challenge the business case, recommend resource shifts, define scenarios, and write a board-ready decision summary."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "Corporate Strategy English",
        "Instructor guide for high-level ESL learners working in corporate strategy, business strategy, transformation, corporate development, strategic finance, and executive advisory roles",
        "Audience: instructors, corporate strategy English coaches, business-school-adjacent programs, corporate learning teams, and internal strategy trainers",
    )
    add_course_opening(story)
    add_strategy_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-corporate-strategy-english-instructor-guide.pdf",
        "EFSP Corporate Strategy English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Corporate Strategy English",
        "Participant workbook: strategic diagnosis, choices, market analysis, portfolio strategy, growth, M&A, uncertainty, governance, and executive dialogue practice",
        "Audience: advanced ESL learners working in corporate strategy, business strategy, corporate development, transformation, strategic finance, internal consulting, product strategy, commercial strategy, and related roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you sound precise and credible in corporate strategy conversations. The goal is not to use more frameworks. The goal is to connect ambiguity to choices, choices to evidence, evidence to resource allocation, and resource allocation to execution."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which strategy conversations are hardest for you: problem framing, market analysis, portfolio review, M&A challenge, executive pushback, scenario planning, board prep, or KPI governance?",
                "Which strategy terms do you understand when reading but avoid when speaking?",
                "When senior leaders ask for everything, do you become too agreeable, too analytical, too indirect, or too blunt?",
                "What is one recent strategy meeting you wish you had handled more clearly?",
            ]
        )
    )
    story.append(lines(6))
    story += h1("Corporate Strategy Workstream Language")
    story.append(
        table(
            [
                ["Area", "Useful verbs", "Example sentence"],
                ["Framing", "diagnose, clarify, structure, hypothesize, prioritize", "We should align on the decision question before building the model."],
                ["Choices", "choose, focus, trade off, sequence, deprioritize", "The strategy is not clear until the tradeoff is visible."],
                ["Markets", "assess, segment, benchmark, map, pressure-test", "The market is growing, but value capture may be structurally weak."],
                ["Portfolio", "allocate, reallocate, fund, harvest, divest", "Equal funding would preserve inertia rather than shift resources to the strongest thesis."],
                ["Growth", "enter, build, buy, partner, integrate", "The route to market depends on speed, control, capability gap, and risk."],
                ["Execution", "govern, measure, escalate, sequence, operationalize", "The dashboard should show movement in value drivers, not only initiative status."],
            ],
            [1.15 * 72, 2.15 * 72, 3.7 * 72],
        )
    )
    story += h1("Practice Pages")
    for module, task in zip(MODULES, WORKBOOK_TASKS):
        story.append(PageBreak())
        story.append(h2(module["title"]))
        story.append(p(module["big_idea"]))
        story.append(h3("What you should be able to do"))
        story.append(bullets(module["objectives"]))
        story.append(h3("Practice task"))
        story.append(box("Situation", [task], "blue"))
        story.append(h3("Decision, hypothesis, or strategic choice"))
        story.append(lines(4))
        story.append(h3("Evidence, tradeoff, risk, or resource implication"))
        story.append(lines(4))
        story.append(h3("Final strategy response"))
        story.append(lines(4))
    story.append(PageBreak())
    story += h1("Phrase Bank")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story += h1("Personal Action Plan")
    story.append(
        table(
            [
                ["Situation", "Term or phrase I will practice", "Evidence I used it well"],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
            ],
            [2.2 * 72, 2.4 * 72, 2.4 * 72],
        )
    )
    return build_pdf(
        "efsp-corporate-strategy-english-participant-workbook.pdf",
        "EFSP Corporate Strategy English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "Corporate Strategy Dialogue Lab",
        "Realistic corporate-strategy workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners",
        "Audience: instructors, strategy English coaches, corporate strategy teams, internal consulting groups, transformation teams, and peer practice cohorts",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: strategist, executive stakeholder, observer.",
                "Read the model dialogue once. Then replay it with a different market, business unit, acquisition target, uncertainty level, or political constraint.",
                "The observer listens for decision framing, tradeoff language, evidence discipline, value logic, uncertainty clarity, and executive next steps.",
                "After each role-play, replay the hardest 30 seconds with a more precise strategy sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners hide behind frameworks. Ask them to state the decision, recommendation, evidence, tradeoff, resource implication, and what would change their mind."
            ],
            "amber",
        )
    )
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
        story.append(h3("Role-play variation"))
        story.append(lines(4))
        story.append(h3("Observer checklist"))
        story.append(
            bullets(
                [
                    "Did the learner clarify the decision before expanding the analysis?",
                    "Did the learner name a tradeoff, strategic choice, or resource implication?",
                    "Did the learner connect evidence to value creation or value capture?",
                    "Did the learner communicate uncertainty without hiding the recommendation?",
                ]
            )
        )
    return build_pdf(
        "efsp-corporate-strategy-dialogue-lab.pdf",
        "EFSP Corporate Strategy Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "Corporate Strategy Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise corporate strategy vocabulary and executive meeting language",
        "Audience: advanced ESL learners in corporate strategy, business strategy, corporate development, transformation, strategic finance, executive advisory, and related roles",
    )
    story += h1("How to Use Strategy Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it clarifies a decision, tradeoff, value driver, risk, or resource implication.",
                "Pair jargon with plain English for executives outside the strategy team.",
                "Distinguish analysis from recommendation; a framework is useful only if it changes a choice.",
                "Avoid generic ambition, activity lists, overconfident forecasts, and unsupported synergy claims.",
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
                ["Strategy vs plan", "Strategy is a set of choices; plan is the sequenced work to execute them."],
                ["Ambition vs choice", "Ambition says what we want; choice says where we focus and what we will not do."],
                ["Growth vs value creation", "Growth increases scale; value creation improves economic worth after cost, risk, and capital."],
                ["Market size vs profit pool", "Market size shows revenue opportunity; profit pool shows where economics are attractive."],
                ["Initiative vs strategic move", "Initiative is work; strategic move changes position, economics, capability, or options."],
                ["Forecast vs scenario", "Forecast estimates one expected future; scenario explores different plausible futures."],
                ["Synergy vs assumption", "Synergy is incremental value with source, timing, owner, and cost; assumption is an input to test."],
                ["KPI vs activity metric", "KPI informs strategic performance; activity metric tracks work completed."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-corporate-strategy-jargon-quick-reference.pdf",
        "EFSP Corporate Strategy Jargon Field Guide",
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
