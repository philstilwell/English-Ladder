"""Original corporate-strategy communication and decision cases."""
from books.authoring import unit

BOOK = dict(
    slug='corporate-strategy', title='Corporate Strategy English',
    cover_label='Choices / resources / executive decisions',
    cover_title='Corporate\nStrategy', cover_size=32,
    tagline='Frame the decision. Expose the trade-off. Make the recommendation precise.',
    audience='For strategy teams, business-unit leaders, analysts, and executive-office colleagues.',
    map_intro='Practice eight decision conversations that connect ambition, evidence, economics, uncertainty, and accountable execution.',
    notes_title='A strong recommendation shows its logic.',
    notes_intro='Strategy English is not a collection of impressive labels. It is language for making choices explicit: what problem matters, why an option could work, what it consumes, and what would change the recommendation. These fictional cases give the meeting a specific decision and a visible evidence boundary.',
    field_notes=[
        ('Separate the objective from the option', 'Entering a market is one possible action; it is not automatically the business outcome the sponsor needs. Confirm the measure and horizon before treating an attractive solution as the assignment.', '"Is the priority revenue growth, operating profit, or a particular market position?"'),
        ('State the forgone alternative', 'A resource request becomes clearer when it names the next-best use of the same money and people. Funding a priority should not conceal the work that must stop, shrink, or wait.', '"Both proposals need the same team; which work would be displaced?"'),
        ('Distinguish potential from captured value', 'A large market, a synergy estimate, and a rising revenue line describe different things. Each needs a bridge to the company\'s actual access, delivery costs, and implementation capacity.', '"The savings are a hypothesis until the timing, cost, and integration dependencies are tested."'),
        ('Ask for the decision you need', 'A board presentation should connect its evidence to an explicit request with limits and follow-up. A pilot decision is not approval of an unlimited rollout.', '"Approve the bounded pilot, with the stated spending cap and review gate."')],
    scope_note='Original fictional language practice, not investment, legal, accounting, valuation, or transaction advice. Figures are teaching assumptions, not forecasts. Actual strategic decisions require verified company facts, appropriate analysis, authorized governance, and qualified review where needed.',
    sources=[
        dict(title='Harvard Business School, Institute for Strategy and Competitiveness. The Five Forces.', url='https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-five-forces.aspx', note='Background on industry structure and competitive forces. The invented market case is not an analysis of a real industry.', checked='30 September 2026'),
        dict(title='US Small Business Administration. Break-even point.', url='https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point', note='Background for basic price, variable-cost, contribution, and break-even terminology. The exercises state their own simplified cost assumptions.', checked='30 September 2026'),
        dict(title='UK Government Office for Science. The Futures Toolkit.', url='https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts/the-futures-toolkit-html', note='Background on exploring plausible futures rather than treating scenarios as predictions. The corporate conversations and scenario facts are original.', checked='30 September 2026'),
        dict(title='HM Treasury. The Green Book (2026).', url='https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026', note='Public-sector appraisal reference for comparing options, costs, benefits, and uncertainty. It is not presented as a binding corporate-strategy standard or a private investment rule.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Strategy Role, Problem Framing, and Executive Diagnosis', scene='Growth is an ambition, not yet a clear assignment',
    skill='Clarify an executive mandate before selecting a growth option or commissioning broad analysis.',
    brief='Executive sponsor Daniel asks strategy lead Rina for a growth strategy. Last year the business reported $20 million revenue and $2 million operating profit. The sponsor has not chosen whether the primary objective is revenue growth, operating-profit improvement, or entry into a new market. No target, horizon, or spending limit has been agreed. A workshop is scheduled for Monday. Rina must establish the decision question and missing inputs rather than assume that an acquisition or a 20% revenue target has already been authorized.',
    cast='Daniel | Executive sponsor\nRina | Strategy lead',
    culture=('Clarifying the assignment is part of senior judgment', 'A question about the objective need not sound resistant. Explain how different definitions of success would change the options and evidence required. Keep the request focused enough for the sponsor to answer, rather than returning a long list of questions with no decision structure.'),
    a='''What is the primary unresolved issue? | Which outcome the growth strategy should prioritize | Whether an acquisition has already closed | Whether the company has no revenue | Which approved market-entry plan is being implemented | The sponsor has not chosen the main objective, so the analysis cannot assume a specific outcome or solution.
What do the supplied figures describe? | Last year's revenue and operating profit | Next year's approved targets | A confirmed acquisition price and integration cost | The new market's total spending | The figures are historical business results, not targets, market estimates, or transaction terms.
Which action is not authorized by the brief? | Treating an acquisition and 20% revenue target as approved | Asking the sponsor to define success | Identifying the missing horizon | Preparing a focused decision question | The case explicitly says no such target or acquisition has been authorized.''',
    vocabulary='''strategic mandate | The authorized purpose and boundaries of a strategy assignment. | clarify the strategic mandate
problem statement | A precise description of the issue to be addressed. | sharpen the problem statement
decision question | The choice the analysis is intended to support. | frame the decision question
executive sponsor | The senior person accountable for backing and directing an initiative. | confirm the executive sponsor
objective | The outcome an effort is intended to achieve. | define the strategic objective
target | A specified desired level of performance or outcome. | set a measurable target
baseline | The starting reference against which a change is assessed. | establish the baseline
time horizon | The period over which a decision or outcome is evaluated. | agree the time horizon
scope boundary | A limit on what the assignment includes. | document the scope boundary
constraint | A condition restricting feasible choices. | identify binding constraints
diagnosis | An evidence-based explanation of the central problem or challenge. | develop the strategic diagnosis
symptom | An observed sign that may have more than one underlying cause. | distinguish a symptom from a cause
hypothesis | A proposition requiring testing against evidence. | test the working hypothesis
issue tree | A structured breakdown of a problem into questions. | build an issue tree
driver analysis | Examination of factors contributing to an observed result. | conduct driver analysis
evidence gap | Missing information needed to support a conclusion. | identify an evidence gap
assumption register | A record of premises, evidence status, and owners. | maintain the assumption register
fact base | The verified information supporting an analysis. | build the fact base
stakeholder map | A description of relevant parties and their interests or roles. | prepare a stakeholder map
alignment | Shared understanding of the relevant goal or decision. | confirm alignment on the objective
decision rights | The authority to make or approve specified choices. | clarify decision rights
success criterion | A condition used to determine whether the effort meets its goal. | agree success criteria
strategic option | A distinct possible course of action. | develop strategic options
recommendation | A proposed course of action supported by reasoning. | present a qualified recommendation''',
    precision='Revenue and operating profit are different measures. The historical figures imply a 10% operating margin on the stated basis, but do not tell the team which outcome to prioritize. A growth label should not silently become a revenue target, acquisition mandate, or permission to spend.',
    precision_extra='Diagnosis asks what explains the challenge; an option proposes what to do about it. Starting with an acquisition can lock the analysis into one answer before the decision question is settled. A clear mandate preserves the ability to compare genuinely different courses of action.',
    phrases='''Clarify the request | Which outcome should the growth strategy prioritize?
Use the baseline | Last year revenue was $20 million and operating profit was $2 million.
Separate the measures | Revenue growth and profit improvement can point to different choices.
Ask for the horizon | Over what period should we evaluate the result?
Name the boundary | We have not yet agreed a spending limit or scope.
Avoid a premature solution | Acquisition is an option to assess, not the mandate itself.
Request authority | Who will approve the objective and the final recommendation?
Close with a decision | Let us confirm the mandate before Monday's options discussion.
Test the diagnosis | What evidence explains the gap between current performance and the desired outcome?
Mark an assumption | I will label that premise as unverified until its owner confirms it.
Keep a hypothesis open | We should test the cause before designing the response.
Limit the analysis | Which questions would actually change the decision?
Distinguish a target | A 20% revenue figure has not been approved as the goal.
Preserve alternatives | The initial option set should not assume one route is inevitable.
Summarize the gap | We have a historical baseline, but no agreed target or horizon.
Check understanding | Does this question capture the choice you need the team to support?''',
    notes='''Growth in what | A useful follow-up names the metric rather than accepting the broad label.
Objective versus route | Profit improvement is an outcome; acquisition is a possible means.
Last year versus next year | Temporal labels prevent a historical result from becoming an implied forecast.
Could versus should | Could identifies an option; should introduces a recommendation that needs a rationale.
Authorized | Use this only for an actual decision, not a promising idea raised in discussion.
Decision-focused question | Ask for the missing input that changes the analysis, not for detail with no clear purpose.''',
    d='''Which clarification should come first? | Is the priority revenue, operating profit, or a defined market-entry outcome? | Which acquisition should we announce before the workshop? | How can we describe every possible initiative as approved? | Should the historical revenue be relabeled as a target? | Different objectives change the option set and evidence needed, so the primary outcome must be clarified.
What operating margin follows from the supplied historical figures? | 10% | 20% | 2% | 100% | Operating profit of $2 million divided by revenue of $20 million equals 10%.
Which sentence correctly labels an acquisition? | It is one option to assess after clarifying the mandate. | It is the only possible meaning of growth strategy. | It is authorized because the sponsor used the word growth. | It is the same thing as a profit objective. | An acquisition is a possible course of action, not a goal or automatic authorization.
Which summary best prepares the next discussion? | We need an objective, target, horizon, boundaries, and decision owner. | We already have all success criteria because last year's revenue is known. | The workshop date establishes unlimited spending authority. | The analyst can invent the target to avoid another question. | The listed inputs resolve the assignment's actual ambiguities without silently making the sponsor's decisions.''',
    dialogue='''Daniel | I want a growth strategy ready for discussion on Monday. The business needs a stronger direction, and I would like the team to move quickly.
Rina | I can focus the work, but first we need the [[strategic mandate::The mandate defines the assignment's purpose and boundaries; the broad request has not yet selected the desired outcome.]]. Does growth mean increasing revenue, improving operating profit, or establishing a position in a new market?
Daniel | Those are all attractive, but I have not ranked them. Last year we had twenty million dollars in revenue and two million in operating profit.
Rina | That gives us a historical [[baseline::The baseline is the prior result used for comparison, not an approved future target or permission to pursue a particular option.]]. It does not yet tell us which change matters most, or what trade-offs you would accept to achieve it.
Daniel | I see the distinction. A plan that adds revenue at a lower margin might look good under one measure and weak under another.
Rina | Exactly. The [[objective::The objective specifies the intended outcome and helps determine which options and trade-offs the analysis should compare.]] changes the comparison. We should not choose the measure after seeing which option produces the most attractive number.
Daniel | What else would you need before asking the team to analyze possible routes? I do not want a clarification process that becomes its own large project.
Rina | A defined [[time horizon::The time horizon sets the period for assessing the result; short-term improvement and long-term market building may require different options.]], a target, and the important constraints. A focused one-year improvement and a longer market-building effort could require very different evidence and commitments.
Daniel | We have not agreed a spending limit. I also mentioned acquisition in a previous conversation, but I did not approve a transaction.
Rina | I will treat acquisition as a [[strategic option::A strategic option is a possible route for assessment; mentioning it does not authorize a transaction or define the outcome.]], not the assignment itself. Otherwise we risk evaluating only how to acquire something instead of whether that route addresses the actual problem.
Daniel | Some people say weak sales execution is the reason growth has slowed. Others say the offer no longer fits what customers need.
Rina | Those are competing explanations. We need a [[diagnosis::Diagnosis seeks an evidence-based explanation of the challenge; the two suggested causes have not yet been established.]] supported by evidence, rather than selecting whichever explanation makes an existing project appear necessary.
Daniel | Can you break that investigation into a few questions for the workshop? I want people to see what information could change the recommendation.
Rina | I can use an [[issue tree::An issue tree organizes the key analytical questions so evidence gathering remains connected to the decision.]] to separate customer demand, the offer, and execution questions. It should structure the work, not become a diagram that pretends we already know the answer.
Daniel | We will also need to distinguish facts from assumptions. Several figures in early presentations came from estimates that nobody formally checked.
Rina | I will keep an [[assumption register::An assumption register records premises and their verification status so estimates do not become silent facts in later presentations.]] with the source and owner of each material premise. That lets us identify which uncertainty could change the choice before refining the numbers.
Daniel | I should confirm the outcome and limits, then the team can compare routes. Who else needs a decision role should be explicit as well.
Rina | Yes. Clear [[decision rights::Decision rights identify who can approve the objective, commitments, and recommendation rather than leaving authority implicit.]] will prevent a workshop preference from being reported as authorization. We can name the sponsor decisions separately from the analytical work assigned to the team.
Daniel | Prepare a short mandate summary for me to confirm before Monday. Do not put a twenty-percent revenue target in it as if I have already agreed.
Rina | I will mark the open [[success criteria::Success criteria define how the effort will be judged; the case has not yet agreed a target, horizon, or priority measure.]] and frame the decision for confirmation. The workshop can then compare options against the same objective instead of debating several different meanings of growth.''',
    transfer_title='A market-entry label hides the outcome',
    transfer_setup='A sponsor proposes opening an overseas office but has not stated the intended business outcome or budget. The team has no authority to sign a lease.',
    transfer='''Analyst: "An overseas office is a possible ___." | option | Opening an office is a course of action, not the business outcome it is intended to produce.
Sponsor: "We first need to define the ___." | objective | The intended business outcome remains unstated, so it must be clarified before evaluating the option.
Analyst: "The spending limit remains ___." | unagreed | The briefing supplies no agreed budget, so a spending amount must not be invented.
Sponsor: "This discussion does not authorize a ___." | lease | The team expressly lacks authority to sign a lease for the proposed office.'''))


BOOK['units'].append(unit(
    title='Strategic Choices: Ambition, Where to Play, How to Win, and Tradeoffs', scene='Two priorities competing for the same specialist team',
    skill='Make a strategic trade-off explicit when two attractive initiatives cannot both fit the available capacity.',
    brief='For the next quarter, a service business has 160 specialist-weeks available after existing commitments. Improving the core service requires 120 specialist-weeks; entering an adjacent segment requires 100. Both need the same specialists. A draft strategy says to deliver both in full next quarter without explaining the 60-week shortfall. No additional hiring, outsourcing, or reduced scope has been approved. Strategy manager Sana and business-unit head Victor must compare choices and sequencing without treating ambition as extra capacity.',
    cast='Sana | Strategy manager\nVictor | Business-unit head',
    culture=('Make the conflict visible before asking for a choice', 'A leader may call two initiatives priorities because both have merit. Respect that ambition while showing the shared resource they consume. A useful challenge quantifies the conflict, names the alternatives, and distinguishes an authorized commitment from a proposal for more capacity.'),
    a='''How much capacity do both full initiatives require? | 220 specialist-weeks | 160 specialist-weeks | 120 specialist-weeks | 100 specialist-weeks | The two requirements are 120 and 100 specialist-weeks, totaling 220.
What is the shortfall against available capacity? | 60 specialist-weeks | 40 specialist-weeks | 20 specialist-weeks | 320 specialist-weeks | Required capacity of 220 minus available capacity of 160 leaves a 60-week gap.
Which assumption is unsupported? | Extra staffing or reduced scope has already been approved. | Both initiatives use the same specialists. | The available capacity is after existing commitments. | Full delivery of both exceeds current capacity. | The briefing explicitly says hiring, outsourcing, and scope reductions have not been approved.''',
    vocabulary='''strategic ambition | The overall level or direction of desired achievement. | articulate the strategic ambition
where to play | The markets, customers, or activities selected for competition. | define where to play
how to win | The proposed basis for succeeding in the chosen arena. | explain how to win
trade-off | A choice that sacrifices one benefit to obtain another. | make the trade-off explicit
opportunity cost | The value of the next-best alternative forgone. | assess opportunity cost
capacity constraint | A limit imposed by the amount of usable resources. | quantify the capacity constraint
resource envelope | The total resources available within defined boundaries. | work within the resource envelope
core business | The established activities central to the company's current operation. | strengthen the core business
adjacency | A related market or activity beyond the current core. | evaluate an adjacency
strategic focus | Concentration on a selected set of choices and priorities. | maintain strategic focus
differentiation | A relevant distinction that gives customers a reason to choose an offering. | substantiate differentiation
cost advantage | A relative cost position that can support competitive performance. | test the cost advantage
competitive positioning | The chosen place and proposition relative to alternatives. | clarify competitive positioning
activity system | A set of mutually supporting activities that deliver a strategy. | align the activity system
strategic fit | Compatibility among choices, capabilities, and the intended direction. | assess strategic fit
operational effectiveness | Performing activities well relative to their required standard or alternatives. | improve operational effectiveness
cannibalization | New activity taking demand or resources from an existing offering. | estimate cannibalization
sequencing | Ordering initiatives over time according to priorities and dependencies. | agree the sequencing
phased rollout | Introduction through defined stages rather than all at once. | propose a phased rollout
minimum viable scope | The smallest scope sufficient for the specified purpose or learning goal. | define minimum viable scope
deprioritization | A decision to give an activity less priority or delay it. | document deprioritization
stop-doing list | An explicit set of activities to discontinue or suspend. | maintain a stop-doing list
resource bottleneck | A resource whose limited availability restricts overall progress. | identify the resource bottleneck
commitment | An agreed allocation or obligation rather than a tentative proposal. | distinguish a commitment from an option''',
    precision='The resource gap is 60 specialist-weeks, not 60 people and not automatically a cash budget of any particular size. Available capacity already excludes existing commitments. Do not count the same specialist time twice or treat an unapproved recruitment idea as immediately usable capacity.',
    precision_extra='Doing both may be feasible only with a changed sequence, scope, or resource plan. Those are options to evaluate, not facts that repair the current plan. The strategic choice also needs the relative value and evidence for each route, not just the fact that one requires fewer weeks.',
    phrases='''Respect the ambition | Both initiatives may have value, but the current plan does not fit.
Show the arithmetic | The two initiatives require 220 specialist-weeks against 160 available.
Name the gap | We are short by 60 specialist-weeks.
Identify the shared resource | Both proposals depend on the same specialist team.
Request the choice | Which outcome takes priority if we cannot deliver both in full?
Offer alternatives | We can compare sequencing, reduced scope, or a properly approved capacity plan.
Avoid invented resources | No extra hiring or outsourcing has been approved.
Close with a commitment | The final plan must name what happens now and what waits.
Test the arena | Which segment are we choosing to serve first?
Explain the advantage | Why would customers choose us in that segment?
Preserve the distinction | Operational improvement and a new market position are not identical choices.
Name the sacrifice | Funding this route means delaying or reducing another use of the team.
Check the ramp | New staff would need realistic onboarding and availability assumptions.
Limit a pilot | A smaller scope should answer a defined question.
Record the non-choice | The strategy should state what we are not committing to this quarter.
Confirm the units | These figures are specialist-weeks, not headcount.''',
    notes='''Both are priorities | The statement does not resolve an actual competition for shared resources.
Now versus later | Sequencing can change timing without pretending that every initiative fits today.
Requires versus has | Separate the resource demand from the capacity already available.
Could add capacity | This introduces a proposal and its dependencies, not an existing resource.
Foregone alternative | Name the specific next-best use when explaining opportunity cost.
Full scope | Keep this qualifier when a smaller pilot might fit but the original commitments do not.''',
    d='''Which statement reports the constraint precisely? | Full delivery needs 220 specialist-weeks, exceeding current capacity by 60. | Full delivery fits because each initiative alone is below 160. | The shortage is 60 permanent employees. | Existing commitments can be ignored because the numbers are strategic. | Combined demand, not each separate request, must be compared with the available specialist-weeks.
Which proposal is correctly described as an option? | Evaluate a phased approach without claiming it is already approved. | Report unapproved outsourcing as existing capacity. | Promise both full launches and omit the shared team. | Count each specialist twice because the initiatives have different sponsors. | A phased approach is a possible plan to assess, while the other options conceal or invent capacity.
Which question addresses how to win? | Why would the chosen customers prefer our offering to alternatives? | Which font makes the strategy look more confident? | How can we avoid mentioning the competing use of staff? | Can the target segment itself prove an advantage? | How to win concerns the reason the company can succeed in the chosen arena, not merely naming the arena.
Which conclusion follows from the resource data alone? | Both full initiatives cannot fit the stated capacity without a change. | The lower-resource initiative is necessarily the better strategy. | The adjacent market is guaranteed to be unprofitable. | The core initiative has no opportunity cost. | Capacity establishes feasibility limits but does not alone rank the options' value or prove their profitability.''',
    dialogue='''Victor | I want the core-service improvement and the adjacent-segment launch in next quarter's strategy. They both matter, and choosing only one feels too cautious.
Sana | Both may be worthwhile, but we need to show the [[capacity constraint::The capacity constraint is the limited 160 specialist-weeks shared by both initiatives, not a judgment that either lacks value.]]. The team has one hundred sixty specialist-weeks available after existing commitments, while the two proposals together require two hundred twenty.
Victor | So the gap is sixty specialist-weeks. Each initiative looked manageable when I reviewed its request separately, but they draw on the same people.
Sana | Exactly. The shared [[resource bottleneck::The resource bottleneck arises because both initiatives need the same limited specialist team; separate sponsorship does not create separate capacity.]] does not disappear because the proposals have different sponsors. The current wording promises more full-scope work than the available team can deliver.
Victor | Could we simply mark both as top priorities and ask the team to find efficiencies? That would avoid delaying either objective at this stage.
Sana | A priority label does not expand our [[resource envelope::The resource envelope is the bounded amount actually available; efficiency hopes do not establish additional usable resources.]] by sixty weeks. We can investigate efficiency changes, but they need evidence before we use them to support a delivery commitment.
Victor | Then we need to explain what each route would achieve. Improving our core service and entering a new segment are not the same strategic choice.
Sana | Right. The [[where to play::Where to play identifies the arena selected for competition, such as the current core or the adjacent segment.]] question identifies the customers and arena. We also need the reason we could succeed there, rather than treat entry itself as evidence of an advantage.
Victor | For the adjacent segment, the proposal mostly describes its size. It says less about why customers would choose our service over the alternatives.
Sana | That leaves [[how to win::How to win concerns the proposed basis of success with the selected customers, which market size alone does not establish.]] unresolved. The comparison needs the offer, capabilities, and evidence of customer preference, not just the appeal of a larger addressable audience.
Victor | If we commit the team to the core improvement first, the adjacent launch would wait. That delay has a cost even if no extra cash is spent.
Sana | Yes, identify the [[opportunity cost::Opportunity cost is the value of the next-best alternative forgone, including the delayed use of scarce specialist time.]]. We should explain the forgone alternative in the decision, rather than present staff allocation as free because the salaries are already budgeted.
Victor | Could we do part of one initiative first, then use what we learn before committing the rest? I do not want a smaller project that proves nothing.
Sana | A [[minimum viable scope::Minimum viable scope must be sufficient for the specified purpose or learning question; merely shrinking work does not make a useful pilot.]] needs a defined purpose. We can assess a bounded pilot, but should not quietly describe that smaller effort as delivering the original full launch.
Victor | Hiring is another possibility, although we have no approval and new specialists would need time before they could contribute fully.
Sana | Then compare it with [[sequencing::Sequencing orders initiatives over time and can address shared-resource conflicts without assuming immediate new staffing.]], including realistic onboarding and funding conditions. Neither a hiring idea nor a later phase should be reported as already available next-quarter capacity.
Victor | The final recommendation should say which activities we commit to now and which we delay or reduce. Otherwise the same conflict will return during execution.
Sana | Include a specific [[stop-doing list::A stop-doing list makes discontinued or suspended work explicit, preventing new priorities from simply accumulating on top of existing demand.]] where relevant, with consequences. We need a feasible set of activities, not a longer list of priorities with the same limited resources.
Victor | I will bring the relative value and customer evidence into the decision. The capacity calculation tells us that the current combination cannot stand unchanged.
Sana | And the approved [[commitment::A commitment is the chosen, authorized plan with resources and limits; it differs from the unapproved alternatives discussed in the meeting.]] should reflect that choice. We can keep the ambition while making the timing, scope, and resource trade-off explicit enough for the team to execute.''',
    transfer_title='Two pilots still share one team',
    transfer_setup='A team has 90 analyst-days available. Pilot A needs 55 days and Pilot B needs 50. No additional capacity or scope reduction has been approved.',
    transfer='''Lead: "The combined requirement is ___ analyst-days." | 105 | Adding the two pilot requirements gives 55 plus 50, or 105 analyst-days.
Analyst: "That exceeds available capacity by ___ days." | 15 | The shortfall is 105 required minus 90 available, which equals 15 analyst-days.
Lead: "We need an explicit resource or sequencing ___." | choice | The current full-scope combination cannot fit without changing resources, timing, or scope through a decision.
Analyst: "Neither proposal creates extra ___ by itself." | capacity | A proposed initiative adds demand, not usable analyst time or approval for additional resources.'''))


BOOK['units'].append(unit(
    title='Industry Structure, Competitive Dynamics, and Profit Pools', scene='A large industry is not the company\'s available market',
    skill='Narrow a market-size claim and distinguish addressable spending, assumed capture, and available profit.',
    brief='A presentation labels $10 billion of annual industry spending as the company\'s immediate opportunity. The company can serve only a segment estimated at $400 million, of which $120 million lies in its current service geography. A separate model assumes a 10% share of that $120 million, implying $12 million annual revenue, but the share assumption has not been validated. No segment profit data or customer-switching evidence are supplied. Strategy analyst Kai and commercial director Yara must rebuild the claim without turning an estimate into a forecast.',
    cast='Kai | Strategy analyst\nYara | Commercial director',
    culture=('A smaller denominator can make a stronger argument', 'Narrowing a market estimate is not necessarily pessimism. It can show that the team understands whom the company can actually serve. Explain each filter and the evidence still needed for capture, instead of presenting a large industry total as a sales opportunity already within reach.'),
    a='''Which figure describes the segment within the current service geography? | $120 million | $10 billion | $400 million | $12 million of confirmed sales | The case narrows total industry spending to the relevant segment and then to the current geography.
What revenue does the 10% share assumption imply? | $12 million annually | $120 million annually | $40 million annually | $1 billion annually | Ten percent of the stated $120 million geographic segment estimate is $12 million.
What is not supplied? | Segment profit data and customer-switching evidence | A stated geographic spending estimate | A numerical share assumption | The total-industry spending figure | The briefing explicitly leaves profitability and switching evidence unavailable, although the market-size and share inputs are supplied.''',
    vocabulary='''market boundary | The definition of customers, products, and geography included in an analysis. | specify the market boundary
total addressable market | Total demand within a clearly defined offering and market boundary. | define the total addressable market
serviceable available market | The portion of defined demand the business can serve with its offering and reach. | estimate the serviceable available market
serviceable obtainable market | The portion of serviceable demand realistically targeted for capture under stated assumptions. | support the serviceable obtainable market
top-down estimate | An estimate derived by narrowing a larger aggregate. | qualify a top-down estimate
bottom-up estimate | An estimate built from smaller units such as accounts, usage, and prices. | construct a bottom-up estimate
capture assumption | An assumed share of available demand won by the company. | test the capture assumption
market share | A company's sales or volume relative to a defined market total. | state the market-share denominator
industry structure | The configuration of participants and forces shaping competition. | analyze industry structure
profit pool | The total profits available in a defined set of activities or segments. | map the profit pool
value chain | The linked activities that create and deliver an offering. | analyze the value chain
value capture | The portion of created value retained by a participant. | explain value capture
buyer power | Customers' ability to influence prices or terms. | assess buyer power
supplier power | Input providers' ability to influence prices or terms. | assess supplier power
rivalry | Competition among existing participants. | evaluate competitive rivalry
substitute | An alternative way to meet the same underlying need. | identify substitutes
barrier to entry | A condition making entry more difficult or costly. | evaluate barriers to entry
switching cost | The cost or difficulty of changing providers or approaches. | investigate switching costs
concentration | The degree to which activity is held by a few participants. | measure customer concentration
price elasticity | Responsiveness of demand to price changes on a stated basis. | estimate price elasticity
channel access | The ability to reach customers through relevant distribution routes. | secure channel access
regulatory barrier | An applicable rule or authorization requirement affecting participation. | verify regulatory barriers
market segmentation | Division of demand into relevant customer or usage groups. | refine market segmentation
competitive response | A rival's possible or observed reaction to a company's move. | assess competitive responses''',
    precision='TAM means total addressable market; SAM, serviceable available market; SOM, serviceable obtainable market. Define each boundary. Industry spending is not automatically the TAM for a narrow offer, and an assumed share is not demonstrated demand.',
    precision_extra='Revenue spending and a profit pool are different quantities. Capturing 10% of $120 million would imply $12 million revenue under the supplied simplified assumption, not $12 million profit. It also needs a time basis, customer evidence, capacity, and a defensible path to winning demand.',
    phrases='''Challenge the boundary | The $10 billion figure includes demand we cannot currently serve.
Apply the filters | The relevant segment is $400 million, with $120 million in our geography.
Name the assumption | Ten percent capture is a modeling input, not a validated result.
Show the arithmetic | That assumption implies $12 million annual revenue.
Separate profit | Market spending does not establish the profit available to us.
Request customer evidence | What would make accounts switch from their current approach?
Check the route | We need evidence of access, buying behavior, and delivery capacity.
Close with definitions | Show the market boundary, filters, and capture assumptions together.
Distinguish competition | A substitute may solve the same need in a different way.
Check leverage | Which buyers or suppliers can influence the terms?
Avoid a share promise | The model does not guarantee that we will win those sales.
Use a second method | A bottom-up estimate can test the top-down calculation.
Clarify the unit | Are we measuring revenue, volume, accounts, or profit?
Keep geography visible | The current service area limits the relevant opportunity.
Test reaction | How might existing competitors respond to entry?
Preserve uncertainty | We have a bounded estimate, with capture still to validate.''',
    notes='''Of which | This phrase identifies a subset and prevents adding nested market figures together.
Available versus obtainable | Ability to serve a market is different from evidence that the company can win it.
Assuming | Keep the condition attached to the result it generates.
Revenue versus profit | Revenue does not subtract the relevant costs or establish retained value.
Same need | A substitute need not be a direct product copy to compete for customer spending.
Current reach | This qualifier distinguishes present service ability from a future expansion option.''',
    d='''Which market statement is accurate? | Current reach covers an estimated $120 million segment; capture is unvalidated. | The company has immediate access to all $10 billion of industry spending. | The three nested market figures should be added together. | A 10% share input proves $12 million of signed orders. | The accurate statement retains the geographic filter and the uncertain capture assumption without adding nested totals.
What does $12 million represent in the model? | Annual revenue implied by the assumed share | Verified annual profit | An approved acquisition budget | Revenue already under contract | The figure is calculated from assumed capture of annual spending, not an established result or profit measure.
Which evidence would most directly test capture? | Account-level need, switching behavior, route to market, and realistic delivery capacity | The industry total alone repeated in a larger font | A competitor's unrelated employee count | A share percentage chosen only to fit the target | Capture requires evidence about winning and serving demand, not just a large total or a desired answer.
Which distinction is correct? | A profit pool concerns profits, while the supplied market figures concern spending. | Every dollar of spending is profit available to one entrant. | Customer power cannot affect terms in a growing industry. | A substitute must have exactly the same product design. | Revenue spending and available profits are distinct; the case supplies no cost or profitability evidence to equate them.''',
    dialogue='''Yara | The opening slide says we have a ten-billion-dollar immediate opportunity. It sounds compelling, but that number is total industry spending, not just our service.
Kai | We need to define the [[market boundary::The market boundary specifies included customers, products, and geography; total industry spending exceeds the current service scope.]] before labeling the opportunity. The company can serve one segment, estimated at four hundred million, rather than every category included in that total.
Yara | People often call the largest number TAM. Would that be a harmless shorthand if we explain the smaller segment later in the presentation?
Kai | Not if the [[total addressable market::Total addressable market must match the offering; a broader industry total may include irrelevant demand.]] label makes the whole industry look relevant to our offering. The definition should match the actual demand we are describing, not simply the largest available figure.
Yara | Within the segment, only one hundred twenty million is in our current service geography. We would need a separate expansion plan for the rest.
Kai | That geographic filter narrows the [[serviceable available market::The serviceable available market reflects demand the business can serve within its defined offering and reach.]] under our current reach. We should show the filter explicitly, rather than let readers assume we can serve the entire segment immediately.
Yara | The revenue model takes ten percent of that one hundred twenty million. That produces twelve million a year, but the percentage was selected as an initial assumption.
Kai | Then call it a [[capture assumption::The capture assumption is a model input requiring validation; its resulting revenue is not a forecast established by customer evidence.]]. The arithmetic is twelve million annual revenue, conditional on that share, not evidence that the accounts are already willing to buy.
Yara | I also do not see margin information. A large amount of spending could leave limited profit after the activities required to serve it.
Kai | Correct. We have not established the [[profit pool::A profit pool measures profits in a defined set of activities; spending totals alone do not provide that amount.]]. We need to understand costs and where value is retained, instead of relabeling every revenue dollar as profit available to us.
Yara | Some segments have a few large customers that negotiate hard. Our market-size estimate does not tell us what terms those customers would accept.
Kai | That is a [[buyer power::Buyer power concerns customers' influence over prices and terms; a spending estimate does not establish the entrant's negotiating position.]] question. The competitive analysis needs to examine the relevant relationships and alternatives, not assume that market growth removes negotiating pressure.
Yara | The account team also says customers may find it difficult to change providers. We should test that rather than assume interest means easy conversion.
Kai | Yes, investigate [[switching costs::Switching costs are burdens of changing providers that can prevent interest from becoming actual adoption.]]. Migration effort, disruption, and contractual conditions may matter, but the current evidence has not quantified them for this segment.
Yara | A customer might also solve the problem internally. That option would not appear on a list of companies selling the same service as ours.
Kai | It can still be a [[substitute::A substitute meets the underlying need in another way, such as an internal approach, rather than copying the same commercial service.]]. Our analysis should cover alternatives to buying the service, not only organizations whose product description resembles our own.
Yara | Before entering, we also need to know whether distribution access, permissions, or capabilities limit participation. None of that is answered by the share calculation.
Kai | Those are possible [[barriers to entry::Barriers to entry concern conditions that make participation difficult; their existence and magnitude require investigation rather than assumption.]]. We should identify and verify the relevant ones, then reflect them in the entry options rather than leave them outside the model.
Yara | I will revise the slide to show industry context, the segment, our geography, and the unvalidated share input. The twelve-million result stays conditional.
Kai | I will add a [[bottom-up estimate::A bottom-up estimate builds from accounts, usage, and pricing to test the aggregate calculation and its capture assumptions.]] using potential accounts and realistic usage assumptions. That will give us a more useful test of the opportunity than repeating a large industry total.''',
    transfer_title='Nested market figures are not additive',
    transfer_setup='A report estimates a $900 million category, including a $200 million target segment. Of that segment, $80 million is in the current region. The figures describe nested groups.',
    transfer='''Analyst: "The current-region estimate is ___ million dollars." | eighty | The supplied regional subset is $80 million, not the whole category or segment.
Director: "It is a ___ of the target segment." | subset | The regional amount lies within the $200 million segment rather than outside it.
Analyst: "Adding the nested figures would double-count ___." | spending | The same underlying spending appears in the larger and smaller groups, so their sum is not a distinct total.
Director: "Keep the boundary and geography ___." | explicit | Stating the definitions prevents a broad category from being mistaken for the company's current reachable demand.'''))


BOOK['units'].append(unit(
    title='Business Models, Unit Economics, Capabilities, and Advantage', scene='More orders, more negative contribution',
    skill='Explain a growing service\'s economics and challenge an unsupported claim that scale alone will solve the loss.',
    brief='A new service charges $100 per completed job and incurs $115 in variable delivery costs per job. Monthly completed jobs increased from 1,000 to 1,500, with price and variable cost per job unchanged. Fixed costs, acquisition costs, and taxes are excluded from these figures. A slide calls rising revenue proof of a sound business model. Business lead Mei and finance partner Hugo must explain the negative contribution and identify what would need to change before higher volume could support profitability.',
    cast='Mei | Business lead\nHugo | Finance partner',
    culture=('Protect the learning without defending the mistaken conclusion', 'Revenue growth can show interest while exposing a delivery problem. Acknowledge what the growth demonstrates, then show the cost bridge. This lets the team investigate pricing, service design, and capabilities without equating a challenge to the economics with opposition to innovation.'),
    a='''What is contribution per job before the excluded costs? | Negative $15 | Positive $15 | Positive $100 | Negative $115 | Revenue of $100 less variable delivery cost of $115 gives negative $15 per completed job.
What is monthly contribution at 1,500 jobs? | Negative $22,500 | Positive $150,000 | Negative $15,000 | Positive $22,500 | The 1,500 jobs each contribute negative $15, totaling negative $22,500 before excluded costs.
What stayed unchanged as volume rose? | Price and variable delivery cost per job | Total monthly revenue | Total monthly contribution | The number of completed jobs | The briefing fixes unit price and unit variable cost while volume changes from 1,000 to 1,500.''',
    vocabulary='''business model | The logic by which a business creates, delivers, and captures value. | test the business model
unit economics | Revenue and cost relationships for a defined unit of activity. | analyze unit economics
revenue model | The way an offering generates income from customers. | clarify the revenue model
monetization | Converting an offering or usage into revenue. | evaluate the monetization approach
variable cost | A cost that changes with the relevant level of activity. | identify variable delivery costs
fixed cost | A cost treated as unchanged within a stated activity range and period. | define the fixed-cost base
contribution | Revenue less the specified variable costs, before other excluded costs. | calculate unit contribution
contribution margin ratio | Contribution divided by revenue on a stated basis. | calculate the contribution margin ratio
gross margin | Revenue less cost of goods or services sold, expressed as an amount or ratio. | define the gross-margin basis
operating leverage | Sensitivity of operating profit to revenue changes given the cost structure. | assess operating leverage
break-even volume | The volume at which revenue covers the included costs under stated assumptions. | calculate break-even volume
cost to serve | Costs associated with delivering and supporting an offering for a customer. | analyze cost to serve
customer acquisition cost | The cost of acquiring a customer under a defined cost and customer basis. | verify customer acquisition cost
customer lifetime value | Estimated value generated over a customer relationship under a stated model. | qualify customer lifetime value
payback period | Time required to recover an investment or acquisition cost on a defined basis. | estimate the payback period
retention | Continued customer participation or spending under a stated measure. | measure customer retention
churn | Customer or revenue loss over a defined period and base. | distinguish customer churn from revenue churn
cohort economics | Revenue and costs tracked for a group with shared entry characteristics. | compare cohort economics
scalability | Ability to grow activity without proportionate deterioration in performance or economics. | test scalability
economies of scale | Cost advantages associated with increased scale under relevant conditions. | substantiate economies of scale
learning curve | Changes in performance or cost associated with accumulated experience. | estimate the learning curve
capability gap | A missing ability required to deliver the intended strategy. | close a capability gap
defensibility | The extent to which an advantage can resist imitation or erosion. | test defensibility
willingness to pay | The amount customers are prepared to pay under relevant conditions. | assess willingness to pay''',
    precision='The service loses $15 of contribution per job on the stated revenue and variable-cost basis. At 1,000 jobs the contribution is negative $15,000; at 1,500 it is negative $22,500. Fixed and acquisition costs are excluded, so these are not complete operating-profit figures.',
    precision_extra='Spreading fixed costs across more units does not repair a negative contribution per unit if price and variable costs remain unchanged. A credible scale argument must explain the mechanism that improves pricing, variable delivery cost, or the service model rather than relying on volume alone.',
    phrases='''Acknowledge demand | More completed jobs show higher volume, not automatically a sound model.
Define the unit | We are measuring one completed job.
Show the bridge | Each $100 of job revenue carries $115 of variable delivery cost.
Name the result | Contribution is negative $15 per job before the excluded costs.
Challenge the scale claim | More volume at unchanged unit economics increases the negative contribution.
Request the mechanism | Which specific change would improve price or variable cost?
Keep the exclusions | Fixed costs, acquisition costs, and taxes are not included here.
Close with evidence | Test the proposed economics before treating scale as the solution.
Separate metrics | Revenue growth and profitability answer different questions.
Check the cost base | Does the delivery figure include every relevant variable item?
Avoid relabeling | This contribution figure is not complete operating profit.
Test pricing | We need evidence of willingness to pay before assuming a higher price.
Examine delivery | Which capability or process change could reduce cost to serve?
Use cohorts | Compare customers on a consistent cost and time basis.
Qualify the forecast | A lower future unit cost remains an assumption until supported.
Preserve the option | We can investigate the model without declaring it proven or impossible.''',
    notes='''Per job versus total | Keep the unit result separate from the aggregate effect of a volume change.
Before excluded costs | This phrase limits what the stated result includes.
At unchanged economics | The condition is essential to the conclusion about higher volume.
Could improve | A potential cost mechanism is not a demonstrated operating improvement.
Contribution versus profit | Contribution subtracts specified variable costs, not every expense.
Proof of | This phrase requires stronger evidence than one favorable revenue trend.''',
    d='''Which statement correctly combines growth and economics? | Revenue rose, but unchanged negative contribution per job made total contribution more negative. | Revenue growth proves all fixed costs are covered. | Higher volume automatically turns negative unit contribution positive. | The excluded acquisition costs must be zero. | More jobs increase revenue and also multiply the negative $15 unit contribution under the supplied unchanged assumptions.
What happened to revenue between the two volumes? | It rose from $100,000 to $150,000 monthly. | It fell from $150,000 to $100,000 monthly. | It stayed at $115,000 monthly. | It became identical to operating profit. | Multiplying the $100 job price by 1,000 and 1,500 jobs gives the two revenue totals.
Which evidence would support a better scale argument? | A verified mechanism reducing variable cost per job or improving realized price | The same unit loss repeated over more jobs | A larger target market with no delivery changes | Reclassifying variable costs as nonexistent | Improving the actual unit revenue-cost relationship, not just the volume label, is needed to address the negative contribution.
Which metric is not fully determined by the supplied figures? | Operating profit | Revenue per job | Variable delivery cost per job | Contribution per job | Fixed and acquisition costs are excluded, so the supplied contribution calculation does not determine complete operating profit.''',
    dialogue='''Mei | Completed jobs rose from one thousand to fifteen hundred this month. The slide says that revenue growth proves the new service has a sound business model.
Hugo | It shows higher volume, but we need the [[unit economics::Unit economics compares revenue and costs for the defined job; higher volume alone does not establish a viable relationship.]]. Each completed job brings in one hundred dollars and incurs one hundred fifteen dollars of variable delivery cost.
Mei | Then the service gives up fifteen dollars on each job before we include fixed costs. I do not want to hide that behind the revenue line.
Hugo | Correct. The [[contribution::Contribution is revenue less the stated variable costs, giving negative $15 per job before excluded expenses.]] is negative fifteen dollars per job. It was negative fifteen thousand for one thousand jobs and is negative twenty-two thousand five hundred for fifteen hundred.
Mei | Revenue still increased from one hundred thousand to one hundred fifty thousand. We should explain both changes rather than make either one disappear.
Hugo | Yes. Higher demand and the [[cost to serve::Cost to serve concerns delivery and support economics; the supplied variable cost currently exceeds the price of each job.]] are separate parts of the story. More completed work can reveal customer interest while increasing the amount lost on the current delivery basis.
Mei | Someone suggested that scale spreads fixed costs, so we should keep growing until the arithmetic fixes itself. Does that address the actual problem?
Hugo | Not while [[variable cost::Variable cost rises with each job; spreading fixed costs cannot repair negative unit contribution.]] per job remains above price. Spreading fixed expenses over more jobs cannot reverse the negative contribution generated by every additional job in this model.
Mei | So we cannot calculate a positive break-even volume by dividing a fixed-cost number by a contribution that remains negative.
Hugo | Exactly. A useful [[break-even volume::Unchanged negative contribution cannot cover positive fixed costs, so no positive break-even volume exists on this basis.]] requires an economically meaningful model. We need a change in price, variable delivery cost, or the service itself before volume can cover the additional included costs.
Mei | The operations team believes repeated work could reduce delivery time. That might matter, but their estimate has not been tested yet.
Hugo | Then describe the proposed [[learning curve::A learning curve is a hypothesis about improvement with experience; an untested estimate should not be treated as an achieved cost reduction.]] and the evidence needed. We should identify the mechanism and measurement, not simply assume that every service becomes cheaper as volume rises.
Mei | A higher price is another possibility, although the current demand was observed at one hundred dollars. We cannot assume it would remain unchanged.
Hugo | We need evidence of [[willingness to pay::Willingness to pay must be tested at the new price; existing-price demand does not establish acceptance.]] at the revised offer. A pricing scenario should show its assumptions about volume and retention instead of lifting revenue with no behavioral consequence.
Mei | We also left customer acquisition costs out of these figures. Even an improved delivery contribution would not automatically mean the whole customer relationship is profitable.
Hugo | Correct. Include the relevant [[customer acquisition cost::Customer acquisition cost is excluded here; complete relationship profitability requires this and other relevant costs.]] and other omitted items in the fuller analysis. Keep the current calculation clearly labeled so it is not mistaken for complete operating profit.
Mei | Some customers may use the service repeatedly, while others use it once. An overall average could hide very different patterns.
Hugo | That is where [[cohort economics::Cohort economics follows comparable customer groups over time and can reveal differences hidden by an aggregate average.]] can help. We need consistent definitions and enough follow-up to compare groups, rather than calling all customers equally valuable from one month's total.
Mei | I will revise the slide: demand increased, but current contribution remains negative. We need to test the pricing and delivery changes before expanding on the same basis.
Hugo | That is a sound test of [[scalability::Scalability concerns how growth affects economics and performance; it is not established merely by a higher number of completed jobs.]]. The service may have options worth exploring, but growth alone has not proved that the business model creates a sustainable positive return.''',
    transfer_title='A positive contribution, with stated fixed costs',
    transfer_setup='A simplified service charges $120 per job, has $90 variable cost per job, and $15,000 monthly fixed costs. Assume constant unit economics and no other costs for this exercise.',
    transfer='''Analyst: "Contribution per job is ___ dollars." | thirty | The unit contribution is $120 revenue minus $90 variable cost, which equals $30.
Lead: "The included fixed cost is ___ dollars monthly." | fifteen thousand | The case explicitly supplies $15,000 of monthly fixed costs for the simplified calculation.
Analyst: "Break-even volume is ___ jobs." | five hundred | Dividing the $15,000 fixed cost by $30 contribution per job gives 500 jobs.
Lead: "That answer depends on the stated ___." | assumptions | Constant unit economics and the exclusion of other costs define the limited exercise, not a universal business forecast.'''))


BOOK['units'].append(unit(
    title='Portfolio Strategy, Capital Allocation, and Resource Reallocation', scene='A budget choice with no stop-doing consequences',
    skill='Compare competing investment requests on a consistent basis and expose displaced work and sunk-cost reasoning.',
    brief='Two divisions each request $2 million from a $3 million investment envelope. Alpha projects $700,000 annual gross savings and Beta $900,000, but implementation timing, ongoing costs, and benefit validation are incomplete. Each proposal currently assumes full funding; neither identifies the work that would stop or wait. Alpha has already spent $400,000 on a completed feasibility study that cannot be recovered. Portfolio lead Ivo and finance director Grace must frame the allocation decision without treating gross savings as net value or past spending as automatic justification.',
    cast='Ivo | Portfolio lead\nGrace | Finance director',
    culture=('A disciplined comparison is not a contest between sponsors', 'Division leaders may defend their projects with different metrics or emotional appeals to prior effort. Put the proposals on a shared basis and make the opportunity cost visible. Challenge the comparison method without implying that a team\'s past work was pointless or that one favorable headline decides the allocation.'),
    a='''What funding gap exists if both full requests are accepted? | $1 million | $2 million | $3 million | $4 million | Two $2 million requests total $4 million against a $3 million envelope, leaving a $1 million gap.
What do the $700,000 and $900,000 figures represent? | Projected annual gross savings with incomplete validation | Verified annual net cash flows after every cost | Guaranteed shareholder returns | Amounts already saved in the current year | The briefing labels them projected gross savings and leaves timing, costs, and validation incomplete.
How should the completed $400,000 study be treated in the forward choice? | As an unrecoverable past cost, not automatic justification to continue | As cash still available to fund either proposal | As proof Alpha must receive full funding | As a future incremental cost identical to the new request | The study cost cannot be recovered, so it does not itself establish the best use of resources from now onward.''',
    vocabulary='''portfolio strategy | The approach to managing a set of businesses or investments together. | review the portfolio strategy
capital allocation | Distribution of financial resources among competing uses. | defend the capital allocation
investment envelope | The total authorized resources available for a set of investments. | respect the investment envelope
capital rationing | Selection among investments when available funding is limited. | account for capital rationing
resource reallocation | Moving resources from one use to another. | plan resource reallocation
investment case | The rationale, economics, risks, and implementation plan for a proposed investment. | strengthen the investment case
incremental cash flow | Cash flow that changes because an option is chosen. | estimate incremental cash flows
sunk cost | An incurred cost that cannot be recovered or changed by the current decision. | separate sunk costs
avoidable cost | A cost that can be prevented by choosing a particular course of action. | identify avoidable costs
committed cost | A cost arising from an existing commitment that may not be easily changed. | review committed costs
benefit realization | Actual achievement and verification of intended benefits. | track benefit realization
gross benefit | A benefit before the relevant offsetting costs are deducted. | qualify gross benefits
net benefit | Benefits less the included costs under a specified basis. | calculate net benefits
net present value | Discounted future net cash flows less the relevant initial investment. | compare net present values
internal rate of return | A discount rate at which the modeled net present value is zero. | qualify the internal rate of return
hurdle rate | A required return threshold used to evaluate an investment. | apply the hurdle rate
weighted average cost of capital | A weighted measure of the required returns on a company's financing sources. | justify the cost-of-capital assumption
return on invested capital | Operating return relative to invested capital on a defined accounting basis. | define return on invested capital
capital intensity | The amount of capital required relative to output, sales, or another stated base. | assess capital intensity
divestment | Disposal of a business, investment, or asset. | evaluate a divestment
harvest strategy | A strategy emphasizing cash extraction with limited further investment. | assess a harvest strategy
stage-gated funding | Funding released in stages after specified reviews. | propose stage-gated funding
benefit owner | The person accountable for delivering and verifying a benefit. | assign the benefit owner
dependency map | A record of relationships that affect delivery or benefits across initiatives. | build a dependency map''',
    precision='The full requests total $4 million, so they cannot both fit a $3 million envelope unchanged. A $1.5 million allocation to each is not automatically a feasible compromise because both current scopes assume $2 million. Reduced funding needs a revised delivery and benefit case.',
    precision_extra='Projected gross savings do not establish net value without costs, timing, and evidence. The completed unrecoverable study is a sunk cost. It can contain useful information, but the money already spent does not, by itself, justify another dollar of investment.',
    phrases='''State the limit | Full funding for both requests exceeds the envelope by $1 million.
Check comparability | Are the benefits measured over the same period and cost basis?
Distinguish the figure | These are projected gross savings, not validated net cash flows.
Request the consequence | What work would stop, shrink, or wait if this proposal is funded?
Separate the past | The feasibility study is unrecoverable past spending.
Use the learning | We should use the study's evidence without treating its cost as a reason to continue.
Test partial funding | A smaller allocation needs a revised scope and benefit case.
Close with a shared basis | Compare forward costs, benefits, risks, timing, and displaced alternatives.
Name the owner | Who is accountable for realizing each saving?
Check overlap | Do both proposals claim the same benefit?
Explain the timing | When would the cash costs and benefits actually occur?
Keep a gate meaningful | Further funding should depend on the stated evidence and review.
Avoid an automatic ranking | The larger gross-saving figure does not settle the allocation.
Record the alternative | Show the best competing use of the limited funds.
Check commitments | Which future costs remain avoidable, and which are already committed?
Limit the model | A return estimate is only as reliable as its assumptions and scope.''',
    notes='''Gross versus net | State which costs have been subtracted before comparing benefit figures.
Already spent | This describes the past; it does not determine the value of a new commitment.
Could be saved | A projected saving needs a mechanism, timing, and accountable owner.
Full funding versus partial | A reduced allocation may change the scope rather than simply scale benefits proportionally.
From now onward | This phrase focuses a decision on consequences that the current choice can still affect.
Shared basis | Comparable timeframes and definitions matter more than matching slide formats.''',
    d='''Which conclusion follows from the budget arithmetic? | Both full scopes cannot be funded within the current envelope. | Both fit because each separately costs less than $3 million. | The completed study increases the envelope to $3.4 million. | Partial funding guarantees both original benefit forecasts. | Combined requests exceed the available funding, while neither past spending nor an untested split creates extra capacity.
Why does Beta's $900,000 headline not settle the decision? | It is gross and unvalidated, with timing and ongoing costs incomplete. | A higher numerical estimate is always less attractive. | No investment can ever be compared using financial information. | Alpha's past expenditure automatically outranks all future benefits. | The proposals need comparable forward economics and evidence rather than a ranking based on one incomplete gross figure.
How should Alpha's study be used? | Use its evidence, but do not treat its unrecoverable cost as automatic justification. | Count the full study cost as new cash available. | Fund Alpha solely to avoid admitting the study was completed. | Exclude all study findings because the cost is sunk. | A sunk expenditure should not drive the forward choice, while the information it produced may remain relevant.
What must accompany a partial-funding option? | A revised scope, delivery plan, and benefit estimate | An assumption that every benefit remains unchanged | A larger font on the original request | No explanation because equal division is inherently optimal | Both proposals assume full funding, so a smaller allocation requires a new feasible case rather than an unsupported proportional split.''',
    dialogue='''Ivo | Both divisions want two million dollars, but we have three million to allocate. The presentation recommends funding both without explaining the missing million.
Grace | Then the [[investment envelope::The investment envelope is the $3 million total available; separate requests must be evaluated together against that limit.]] is not reflected in the recommendation. We need a feasible choice, a changed scope, or a properly authorized increase, not two full commitments against insufficient funds.
Ivo | Beta projects nine hundred thousand in annual savings and Alpha seven hundred thousand. Would ranking those two figures be an adequate first answer?
Grace | They are [[gross benefits::Gross benefits are stated before relevant offsetting costs; the incomplete timing and validation prevent treating them as net value.]], not complete net value. We still need implementation timing, ongoing costs, and evidence supporting the savings before making that comparison decisive.
Ivo | Alpha's sponsor says we have already spent four hundred thousand on the feasibility study, so not proceeding would waste what the team has done.
Grace | That amount is a [[sunk cost::The sunk cost cannot be recovered and does not automatically justify new spending.]]. We should use the study's information, but the unrecoverable spending does not establish that Alpha is the best use of the next dollar.
Ivo | We should distinguish that from a future cost we could avoid by choosing another option. Otherwise every past and future amount gets mixed together.
Grace | Exactly. The comparison needs [[incremental cash flows::Incremental cash flows are the future cash consequences changed by the decision, unlike the unrecoverable completed-study expenditure.]] for each option, with clear timing and a consistent basis. Existing commitments and costs we can still avoid require separate treatment.
Ivo | Neither division says what would stop if it receives the money. Their proposals read as though the rest of the portfolio can continue unchanged.
Grace | Require an explicit [[resource reallocation::Resource reallocation moves limited resources between uses and should identify the work displaced by the funded proposal.]] plan. Financial funding may also depend on shared staff, so the displaced work should be visible rather than discovered after approval.
Ivo | Could we divide the envelope equally and give each division one and a half million? That would look fair and stay within the limit.
Grace | It would fit the cash ceiling, but each [[investment case::The investment case must match its funding; reduced allocations require revised scope and benefit estimates.]] assumes two million. A smaller allocation needs a revised scope and benefit estimate, not an automatic claim that both original plans remain deliverable.
Ivo | We also need someone responsible for turning the savings into actual results. A forecast can remain on the slide long after the activity changes.
Grace | Name a [[benefit owner::A benefit owner is accountable for achieving and verifying the claimed result, not just submitting an attractive forecast.]] for each material saving, with the baseline and verification method. That makes the post-decision review about realized outcomes rather than repeated promises.
Ivo | Some benefits may depend on the same system change. If both divisions include those savings in full, the combined case could double-count them.
Grace | Build a [[dependency map::A dependency map exposes shared prerequisites and overlapping benefits, helping prevent the same saving from being counted twice.]] and identify overlaps. We should not add benefits that rely on the same limited resource or represent the same underlying saving without checking the relationship.
Ivo | If the initial evidence is promising but incomplete, we could fund a defined stage and review the result before releasing the rest.
Grace | That is [[stage-gated funding::Stage-gated funding requires evidence reviews and real authority to change the next commitment.]], provided the gate has real criteria and authority. It should not become a full commitment disguised as a sequence of automatic approvals.
Ivo | The revised recommendation will compare feasible scopes, forward costs, benefit timing, risks, and the alternatives displaced. We will keep the study's useful findings without treating its cost as a mandate.
Grace | Good. The final [[capital allocation::Capital allocation distributes limited funds among competing uses based on the full comparison.]] should explain why the chosen use of funds is preferable on that shared basis. A larger gross number or a completed study cannot substitute for the decision logic.''',
    transfer_title='A sunk fee and a new decision',
    transfer_setup='A completed, nonrefundable study cost $30,000. A new pilot would require another $70,000. The study contains useful evidence, but no pilot approval has been given.',
    transfer='''Analyst: "The completed study fee is a ___ cost." | sunk | The $30,000 has already been spent and cannot be recovered through the present decision.
Sponsor: "The pilot is a new ___." | commitment | The additional $70,000 is a forward decision, not something already authorized by the study purchase.
Analyst: "We should use the study's ___." | evidence | Useful information remains relevant even when the spending that produced it is unrecoverable.
Sponsor: "Past spending does not supply pilot ___." | approval | The briefing explicitly says no pilot approval exists, and completing a study does not create it.'''))


BOOK['units'].append(unit(
    title='Growth Strategy, Market Entry, Partnerships, and M&A Logic', scene='A savings headline without an integration plan',
    skill='Qualify an acquisition rationale and distinguish recurring potential from timed, net cash benefits.',
    brief='A proposed acquisition case claims $4 million in annual procurement savings once fully implemented. The estimate assumes combined buying volumes and revised supplier contracts. No supplier has confirmed the proposed terms, and no integration plan or cost-to-achieve estimate exists. The purchase price is outside this meeting. Strategy lead Elena and integration director Marcus must identify the evidence needed before presenting the savings as dependable. The executive committee has authorized analysis only, not a bid. Building internally and forming a partnership remain alternatives.',
    cast='Elena | Strategy lead\nMarcus | Integration director',
    culture=('Challenge the bridge, not the ambition', 'A useful challenge identifies the missing steps between an attractive strategic idea and a result. Ask about timing, delivery responsibility, dependencies, and costs without suggesting that uncertainty makes the proposal worthless. A credible case can contain potential value and still require substantial further work.'),
    a='''What does the $4 million figure describe? | Potential annual procurement savings after full implementation | Confirmed first-year net cash savings | The approved purchase price | A binding supplier discount | The estimate describes potential annual savings at full implementation, with terms and delivery assumptions still unverified.
What has the committee authorized? | Analysis of the proposal | Submission of a binding bid | Immediate integration spending of any amount | Signing revised supplier contracts | The briefing explicitly limits authorization to analysis and says no bid has been approved.
Which information is missing? | An integration plan and cost-to-achieve estimate | The existence of an acquisition proposal | The category of proposed savings | Whether alternatives remain available | The case names procurement savings and available alternatives but supplies neither implementation planning nor delivery costs.''',
    vocabulary='''acquisition rationale | The explanation of why buying a business may create value. | test the acquisition rationale
strategic fit | The relationship between an option and the company's objectives and capabilities. | assess strategic fit
build-buy-partner | A comparison of internal development, acquisition, and collaboration routes. | compare build-buy-partner options
organic growth | Expansion generated within the business rather than by acquisition. | pursue organic growth
inorganic growth | Expansion through acquisitions or similar external combinations. | evaluate inorganic growth
market-entry mode | The arrangement used to enter a market. | select a market-entry mode
partnership model | The agreed structure for collaborating with another organization. | define the partnership model
deal thesis | The central value-creation argument for a transaction. | challenge the deal thesis
synergy | An additional benefit expected from combining activities or businesses. | validate the synergy estimate
run-rate savings | The recurring savings level expected once changes are fully operating. | distinguish run-rate savings from first-year cash
gross savings | Savings before specified implementation or offsetting costs. | state gross savings separately
cost to achieve | Spending required to deliver a proposed benefit. | estimate the cost to achieve
integration roadmap | A sequenced plan for combining selected activities. | develop the integration roadmap
integration dependency | A prerequisite affecting the delivery of combined operations. | identify integration dependencies
commercial diligence | Investigation of market and customer assumptions behind a proposal. | commission commercial diligence
supplier renegotiation | Discussion intended to change existing supplier terms. | test supplier renegotiation assumptions
revenue dissynergy | Lost revenue associated with the disruption or combination. | assess potential revenue dissynergies
customer retention | The maintenance of existing customer relationships or revenue. | protect customer retention
standalone case | Expected performance without the proposed combination. | establish the standalone case
incremental value | Additional value relative to the chosen comparison case. | estimate incremental value
double-counting | Including the same underlying benefit or cost more than once. | eliminate double-counting
execution risk | The possibility that implementation does not deliver the plan. | assess execution risk
bid authority | Permission to submit an offer within specified limits. | confirm bid authority
integration owner | The person accountable for a defined integration activity. | appoint an integration owner''',
    precision='Annual run-rate savings are not automatically cash received during the first year. A change introduced halfway through a year has a different time profile from one operating throughout it. The proposal also needs implementation costs and offsetting effects before anyone labels the benefit net.',
    precision_extra='Compare the combination with a defined alternative, including standalone performance. Keep standalone improvements separate from acquisition-specific benefits. Counting the same procurement improvement in both categories exaggerates the transaction\'s incremental value.',
    phrases='''Qualify the headline | The $4 million is an unverified annual run-rate estimate.
Ask about timing | When would each saving begin, and when would it reach full effect?
Separate cash from potential | That is not yet a first-year cash-flow forecast.
Request implementation costs | We need the cost to achieve before describing a net benefit.
Test the mechanism | Which supplier terms must change for the savings to occur?
Keep alternatives open | We should compare building, buying, and partnering on the same basis.
Mark authority | The committee authorized analysis, not a bid.
Name an owner | Who is accountable for validating and delivering this saving?
Define the comparison | What would improve in the standalone business anyway?
Prevent duplication | Let us remove benefits already counted in the existing improvement plan.
Expose a dependency | This saving depends on successful supplier renegotiation.
Protect the commercial base | Could integration disrupt the customers we need to retain?
Qualify strategic fit | Strategic fit supports the rationale but does not establish the price.
Ask for a bridge | Show the steps from gross potential to timed net cash flows.
Separate decisions | A positive diligence finding does not itself confer transaction authority.
Summarize the next gate | Return with verified assumptions, delivery costs, timing, and accountable owners.''',
    notes='''Run rate | Name the fully operating period; do not use the phrase as a synonym for cash already earned.
Net of what | Specify which costs and offsets have been deducted.
Synergy versus standalone | Only an additional combination benefit belongs in the acquisition-specific claim.
Potential | This word signals an opportunity, not confirmation that the result will occur.
Buy versus bid | Discussing acquisition as an option does not authorize an offer.
Cost to achieve | This may occur before the saving and changes the cash-flow profile.''',
    d='''Which statement preserves the evidence boundary? | Supplier terms still need validation before the savings can be treated as dependable. | Combined volume guarantees every supplier will accept the requested terms. | A savings estimate is itself a signed commercial agreement. | The committee has already approved the acquisition. | The proposed terms have not been confirmed, and the committee authorized analysis only.
Why is $4 million not yet a net first-year benefit? | Implementation timing, delivery costs, and offsets have not been established. | Annual figures can never be used in strategy. | Procurement savings must always equal the purchase price. | Supplier contracts have no effect on costs. | The annual run-rate estimate lacks the information required to derive timed net cash benefits.
Which comparison helps identify incremental value? | Compare the combination with a defined standalone case and other feasible routes. | Compare the acquisition with a business assumed to have no future performance. | Count existing improvement savings again as entirely new synergies. | Exclude alternatives because an acquisition has been mentioned. | A defined comparison separates acquisition-specific benefits from improvements available without the transaction.
What should happen before a bid is submitted? | Obtain the required bid authority through the applicable decision process. | Treat permission to analyze as unlimited bidding authority. | Ask an analyst to infer permission from the headline saving. | Replace approval with a positive meeting tone. | The explicit authorization covers analysis, not submission of an offer or any transaction commitment.''',
    dialogue='''Elena | The acquisition slide says four million dollars in annual procurement savings. That is the largest quantified benefit, so it will attract attention at the committee.
Marcus | Label it as [[run-rate savings::Run-rate savings describe the recurring level after full implementation, not a confirmed amount realized in the first year.]] at full implementation. We have not established when supplier changes would take effect, so the headline is not a first-year cash forecast.
Elena | The estimate assumes we combine purchasing volumes and obtain better terms. Nobody has confirmed those terms with the suppliers or checked the contract restrictions.
Marcus | Then [[supplier renegotiation::Supplier renegotiation could improve terms, but no supplier has confirmed the assumed discounts.]] is an unverified dependency. Combined volume creates a discussion opportunity, but it does not prove that every requested discount is available.
Elena | The sponsor wants one net benefit number. We have the potential saving, but no implementation estimate, transition schedule, or analysis of costs that continue.
Marcus | We first need the [[cost to achieve::Cost to achieve identifies spending required to deliver savings and is missing from the proposed net-benefit calculation.]]. A gross saving cannot become net simply because we give it a more reassuring heading on the summary slide.
Elena | There is also an existing procurement project in the standalone business. Some improvements might happen without the acquisition, and the proposals use similar descriptions.
Marcus | Establish the [[standalone case::The standalone case shows performance without the acquisition, allowing the team to identify which improvements are genuinely incremental.]] before adding transaction benefits. Otherwise the same improvement can appear once in the operating plan and again as value supposedly created by the deal.
Elena | We should ask whether internal development or a partnership could achieve the strategic objective. The acquisition should not win by being the only route with a slide.
Marcus | A [[build-buy-partner::Build-buy-partner compares internal development, acquisition, and collaboration as alternative routes to the objective.]] comparison would help. Use comparable scope and timing, and show differences in control, capability, resource needs, and uncertainty rather than reducing everything to one headline.
Elena | The commercial team also worries that changing service arrangements during integration could unsettle customers. That would offset some of the expected improvement.
Marcus | Include potential [[revenue dissynergies::Revenue dissynergies are losses associated with the combination or disruption and may offset some expected acquisition benefits.]] instead of assuming the revenue base remains untouched. We need evidence about customer exposure, not a made-up percentage inserted to make the model look balanced.
Elena | None of this says the acquisition is a bad idea. It says we have not yet shown how the proposed value would actually be delivered.
Marcus | Correct. An [[integration roadmap::An integration roadmap connects proposed benefits with sequenced activities, dependencies, owners, and timing needed for delivery.]] should connect each saving to actions, dependencies, timing, and an accountable person. It gives the committee something more useful than an unsupported total.
Elena | Who should be responsible for the procurement estimate? The analyst can document the calculation, but the analyst will not negotiate or implement the new arrangements.
Marcus | Assign an [[integration owner::An integration owner is accountable for delivering a defined activity; preparing the analysis alone does not create delivery responsibility.]] with the relevant operational authority. Keep independent challenge in the review, while making responsibility for validation and implementation explicit.
Elena | The executive committee has authorized analysis only. Some colleagues are treating that as a signal that we can submit an offer once the slide improves.
Marcus | That is not [[bid authority::Bid authority is explicit permission to submit an offer; authorization to analyze does not provide that permission.]]. The next submission should request the appropriate decision and state its limits, rather than infer transaction permission from interest in the opportunity.
Elena | I will revise the recommendation to show the strategic logic, alternative routes, standalone comparison, and evidence still required. The purchase price remains outside this meeting.
Marcus | Good. Keep the [[deal thesis::The deal thesis explains value creation; it remains provisional until material assumptions are tested.]] provisional until its assumptions withstand scrutiny. The strongest version makes uncertainty visible and identifies what must be verified before the next commitment.''',
    transfer_title='Annual potential is not first-year cash',
    transfer_setup='A fictional saving of $120,000 per year begins on July 1 and accrues evenly. A one-time implementation payment is $40,000. Ignore taxes, discounting, and other costs; use six months of savings.',
    transfer='''Analyst: "The annual run-rate saving is ___." | $120,000 | The fully operating annual rate is given directly and does not change because implementation begins midyear.
Reviewer: "Six months produces gross savings of ___." | $60,000 | Half of the stated annual rate is realized during the six-month period under the exercise assumptions.
Analyst: "The implementation payment is a ___." | cost to achieve | The payment is required to implement the saving, so it must be included in the specified net calculation.
Reviewer: "The first-year net cash benefit on this basis is ___." | $20,000 | Subtract the $40,000 implementation payment from $60,000 gross savings, using only the stated assumptions.'''))


BOOK['units'].append(unit(
    title='Uncertainty, Scenarios, Strategic Options, and Risk Posture', scene='A plausible downside is not a prediction',
    skill='Describe conditional outcomes and connect observable signposts to proportionate, authorized responses.',
    brief='A planning team models next year using two illustrative cases. The base case assumes 10,000 units at $200 each. A downside case assumes 8,000 units at $180 each. No probabilities have been assigned, and neither case is an approved forecast. A proposed expansion can begin with a reversible $50,000 test or proceed to a $500,000 commitment. Neither route is approved. Strategist Noor and operations lead Leo must distinguish scenarios from predictions and propose measurable review triggers without implying that uncertainty has disappeared.',
    cast='Noor | Strategist\nLeo | Operations lead',
    culture=('Speak conditionally without sounding evasive', 'Use a clear if-clause, name the assumption, and state what follows on that basis. Conditional language is stronger when it points to evidence and a response. Avoid both false certainty and vague warnings that leave colleagues unsure what to monitor or who should act.'),
    a='''What is the status of the two cases? | Illustrative scenarios without assigned probabilities | Two approved forecasts with equal probabilities | Confirmed sales orders for next year | Actual results from last year | The brief explicitly calls the cases illustrative and supplies neither probabilities nor forecast approval.
Which comparison is supported by the brief? | The test is reversible and requires a smaller initial commitment. | The test guarantees the expansion will succeed. | The larger commitment has already been authorized. | The downside case proves demand will fall. | The supplied facts establish reversibility and spending amounts, not success, approval, or prediction.
What should the team clarify before acting on a review trigger? | The measure, threshold, response, and decision authority | Which scenario title sounds most optimistic | How to turn an unassigned probability into certainty | Whether a trigger can replace all judgment | A useful trigger connects observable evidence with an explicit response and authorized decision process.''',
    vocabulary='''scenario | A coherent description of a possible future under stated assumptions. | construct a plausible scenario
base case | A reference set of assumptions used for comparison. | label the base-case assumptions
downside case | A set of assumptions producing a less favorable outcome. | stress the downside case
forecast | An estimate of expected future results using a stated method. | update the approved forecast
prediction | A statement about what is expected to happen. | avoid an unsupported prediction
probability | A quantified expression of likelihood on a stated basis. | justify the assigned probability
plausibility | The degree to which an outcome is reasonably conceivable. | test scenario plausibility
uncertainty | Lack of sufficient knowledge about outcomes or relevant conditions. | acknowledge material uncertainty
sensitivity analysis | Examination of how changing inputs affects a result. | run sensitivity analysis
stress test | Analysis of performance under specified adverse conditions. | define the stress-test assumptions
signpost | An observable development relevant to an uncertain future. | monitor early signposts
leading indicator | A measure that may provide an early signal of later performance. | validate a leading indicator
lagging indicator | A measure reflecting results after relevant activity has occurred. | review lagging indicators
trigger | A defined condition prompting a specified review or response. | set a review trigger
threshold | The level at which a stated condition is met. | agree the threshold
contingency plan | A prepared response to a specified possible development. | activate a contingency plan
reversible decision | A choice that can be changed with limited exit consequences. | favor a reversible decision where appropriate
irreversible commitment | A commitment difficult or costly to undo. | defer an irreversible commitment
option value | The value of preserving a future choice under uncertainty. | preserve option value
staged commitment | An allocation made in steps subject to specified reviews. | design a staged commitment
risk appetite | The types and amount of risk an organization is willing to pursue or retain. | clarify risk appetite
risk tolerance | The acceptable variation or limits around a defined exposure or objective. | specify risk tolerance
robust option | A choice that performs acceptably across the scenarios examined. | compare robust options
decision gate | A defined review point before a further commitment. | establish a decision gate''',
    precision='A base case is not automatically the most likely outcome, and two scenarios do not automatically have a 50% probability each. If no probabilities have been established, report the cases without inventing them. Plausibility describes what could happen; probability makes a different, quantified claim.',
    precision_extra='A signpost is something to monitor; a trigger is a specified condition tied to a response. For example, a demand measure can be monitored weekly, while a defined decline over an agreed period triggers a review. A review trigger need not automatically authorize cancellation or spending.',
    phrases='''State the condition | If volume and price follow these assumptions, revenue would be $1.44 million.
Separate a forecast | These are planning scenarios, not approved forecasts.
Avoid invented likelihood | We have not assigned probabilities to either case.
Name the reference | The base case is our comparison point, not a guarantee.
Test resilience | Which option remains workable across both scenarios?
Preserve flexibility | The smaller test preserves a later decision on full expansion.
Define monitoring | Which observable signposts would challenge the current assumption?
Specify the trigger | Let us agree the measure, threshold, and review period.
Keep authority explicit | Meeting the threshold triggers a review, not automatic spending.
Request sensitivity | Show how the result changes when price and volume move separately.
Describe the downside | This case tests adverse conditions without predicting that they will occur.
Limit the claim | Reversibility reduces some commitment risk; it does not guarantee success.
Set the next gate | The pilot evidence must be reviewed before any larger commitment.
Name the response | What action would the decision owner consider if the trigger is met?
Clarify exposure | How much can we commit before the next evidence review?
Summarize uncertainty | The decision depends on assumptions that remain open to revision.''',
    notes='''Would versus will | Would fits a conditional model result; will can overstate certainty.
Base does not mean certain | Explain why the reference assumptions were selected.
Equal number of cases | Two cases do not establish equal likelihood.
Trigger versus authority | An alert or review condition is not necessarily permission to act.
Risk language | Define appetite, tolerance, and limits consistently with the organization's own governance.
Reversible | Explain the actual exit costs and constraints before using this label in a real proposal.''',
    d='''What revenue follows from the downside assumptions? | $1.44 million | $1.6 million | $2 million | $3.44 million | Multiply 8,000 units by $180; the result is conditional revenue, not profit or a prediction.
Which statement avoids inventing probability? | No probability has been assigned to either scenario. | Each scenario has a 50% chance because there are two. | The base case is certain because it is listed first. | The downside case is impossible because it is less attractive. | The number and order of scenarios do not establish likelihood, and the brief explicitly supplies none.
Which trigger is operationally clearer? | Review expansion if the agreed demand measure stays below its threshold for the specified period. | React when the market feels uncomfortable. | Spend more whenever someone mentions uncertainty. | Treat every weekly fluctuation as proof of the downside case. | A defined measure, threshold, and period provide a repeatable review condition without turning noise into certainty.
What does the $50,000 test preserve? | A later choice about the larger commitment, subject to evidence and approval | A guarantee of future demand | Automatic approval for the $500,000 expansion | Proof that all possible risks have been removed | The reversible test preserves flexibility but does not establish success or authorize subsequent spending.''',
    dialogue='''Leo | The workshop has a base case and a downside case. The sponsor wants us to say which one will happen so the expansion decision feels clearer.
Noor | We should not turn a [[scenario::A scenario describes a possible future under assumptions; it does not by itself predict which future will occur.]] into a prediction. Neither case has an assigned probability, and neither has been approved as our forecast for next year.
Leo | The base case assumes ten thousand units at two hundred dollars. People keep calling it the expected outcome because it appears first in the presentation.
Noor | It is a [[base case::The base case is the reference assumption set, not automatically the most likely outcome or an approved forecast.]] for comparison. That produces two million dollars of revenue on the stated assumptions, but the heading does not establish that those assumptions are most likely.
Leo | The other case has eight thousand units at one hundred eighty dollars. It changes both demand and price, which makes the revenue reduction more pronounced.
Noor | Yes. The [[downside case::The downside case combines lower volume and price, conditionally producing $1.44 million revenue.]] produces one point four four million dollars. We should explain both changes rather than describing the entire difference as a volume effect.
Leo | Could we assign each case a fifty-percent chance? There are only two cases on the slide, and the committee may ask for an average.
Noor | Not without a basis for the [[probabilities::Probabilities require a justified likelihood assessment; presenting two cases does not establish equal chances or an expected-value calculation.]]. Two selected cases do not establish equal likelihood or exhaust every possible future. An unsupported average would add precision without adding evidence.
Leo | We could also vary the inputs separately. That would show how much of the result depends on price and how much depends on volume.
Noor | That is useful [[sensitivity analysis::Sensitivity analysis changes inputs to show how results respond, helping distinguish the effects of price and volume.]]. Keep the assumptions visible and use it to identify which uncertainties could change the decision, rather than create a large table without a purpose.
Leo | For expansion, we can run a reversible fifty-thousand-dollar test or commit five hundred thousand immediately. Neither proposal has approval at this point.
Noor | The smaller stage may preserve [[option value::Option value preserves a later choice while gathering evidence; it does not guarantee success.]] while we learn. We still need to explain what the test can establish, its limits, and whether its evidence would genuinely inform the larger decision.
Leo | We should monitor customer inquiries and confirmed demand during the test. Those measures could help us see whether the market assumptions are holding.
Noor | Define those [[signposts::Signposts are observable developments relevant to the assumptions; monitoring them does not automatically establish a decision threshold or response.]] carefully. An inquiry and a confirmed order are not interchangeable, and a measure is useful only if its relationship to the decision is clear.
Leo | Then we need a rule for when the evidence deserves another review. I do not want every small weekly fluctuation to restart the whole discussion.
Noor | Set a [[trigger::A trigger links a defined condition to a specified response, here a review.]] using an agreed measure, threshold, and period. Specify whether it calls for review, a pause, or another authorized response rather than leaving its meaning implicit.
Leo | The sponsor must define acceptable exposure before that review. Otherwise the team could keep spending while describing every step as learning.
Noor | Document the [[risk limits::Risk limits constrain exposure during the evidence-gathering stage and prevent learning language from disguising an open-ended spending commitment.]] and decision authority. A staged approach needs an actual boundary; calling something a pilot does not make an open-ended commitment small or reversible.
Leo | I will present the cases as conditional, show the sensitivity, and request a bounded test with clear monitoring. The full expansion will remain a separate decision.
Noor | Add the next [[decision gate::A decision gate requires a defined review before further commitment; pilot approval must not silently become authorization for full expansion.]] and the evidence required there. That gives the committee a practical way to act under uncertainty without pretending that we know the future.''',
    transfer_title='A trigger calls for review',
    transfer_setup='The agreed rule calls for a review if confirmed weekly orders remain below 80 for three consecutive weeks. The last three totals are 76, 79, and 78. The rule grants no automatic cancellation authority.',
    transfer='''Analyst: "All three totals are below the ___." | threshold | Each supplied weekly total is less than 80, the level specified in the review rule.
Lead: "The agreed review ___ has been met." | trigger | Three consecutive weeks below the threshold satisfy the complete condition, not just one part of it.
Analyst: "We should now arrange the ___." | review | The stated response is a review; the exercise supplies no different automatic action.
Lead: "Cancellation would still require ___." | authority | Meeting the review condition does not confer the cancellation authority expressly excluded by the briefing.'''))


BOOK['units'].append(unit(
    title='Execution Governance, Operating Model, KPIs, and Board Narrative', scene='Twelve metrics, but what is the board being asked to approve?',
    skill='Turn a dense status presentation into a bounded decision request with owners, measures, and review conditions.',
    brief='A team asks the board to approve a twelve-week pilot at two sites with a $150,000 spending cap. The proposed goal is to reduce median processing time from the measured six-day baseline to four days, while keeping the error rate at or below 2%. The operations director would own delivery and finance would verify spending. The draft contains twelve metrics but no explicit approval request. No full rollout is authorized. A final review must assess the pilot evidence before the board considers further investment.',
    cast='Amara | Chief of staff\nTom | Operations director',
    culture=('Put the decision before the dashboard', 'Senior listeners should not have to infer whether a presentation requests approval, reports progress, or seeks advice. State the requested decision early, then use a small number of relevant measures to support it. Keep delivery accountability distinct from independent verification and from authority to approve the next stage.'),
    a='''What decision is requested? | Approval of a two-site, twelve-week pilot capped at $150,000 | Approval of an unlimited company-wide rollout | Confirmation that the pilot has already met its target | Permission to remove the error-rate limit | The brief defines a bounded pilot request and expressly excludes full-rollout authorization.
Which measure is a quality guardrail? | Keeping the error rate at or below 2% | Spending the entire cap as quickly as possible | Increasing the number of presentation slides | Reporting twelve metrics regardless of relevance | The error limit protects quality while the team attempts to improve processing speed.
Who would own delivery? | The operations director | Finance solely because it checks spending | Every board member individually | Nobody until after rollout | The briefing assigns operational delivery to the operations director and financial verification to finance.''',
    vocabulary='''execution governance | The arrangements for directing, reviewing, and authorizing implementation. | establish execution governance
operating model | The configuration of roles, processes, systems, and interactions used to deliver work. | define the operating model
board narrative | The decision-focused explanation connecting evidence, choices, and the requested action. | sharpen the board narrative
decision request | The explicit action a decision-making body is asked to authorize. | state the decision request
pilot scope | The boundaries of a limited test. | protect the pilot scope
spending cap | The maximum authorized expenditure for a defined purpose. | enforce the spending cap
delivery owner | The person accountable for implementing the agreed work. | name the delivery owner
accountability | Answerability for a defined result or responsibility. | assign clear accountability
decision authority | Permission to approve a defined action or commitment. | identify decision authority
key performance indicator | A selected measure used to assess important performance. | choose relevant key performance indicators
outcome metric | A measure of the result the initiative is intended to change. | define the outcome metric
guardrail metric | A measure that limits unacceptable side effects or deterioration. | monitor the guardrail metric
metric definition | The specified calculation, data scope, and interpretation of a measure. | document the metric definition
median | The middle value when observations are ordered, or the mean of the two middle values for an even count. | report median processing time
measurement window | The period included in a performance calculation. | agree the measurement window
data owner | The person responsible for the quality and availability of specified data. | confirm the data owner
reporting cadence | The agreed frequency of updates or reviews. | set the reporting cadence
variance | A difference from a stated plan, baseline, or target. | explain material variance
exception report | A focused update on deviations requiring attention. | issue an exception report
escalation route | The path for raising an issue to the appropriate authority. | clarify the escalation route
stage review | A formal assessment before deciding on a subsequent phase. | conduct the stage review
rollout criteria | Conditions required before considering wider implementation. | agree rollout criteria
decision record | Documentation of the choice made, its scope, and its conditions. | maintain the decision record
benefit verification | Checking whether claimed improvements occurred on a defined basis. | require benefit verification''',
    precision='A target is the result sought; a guardrail limits what must not deteriorate while pursuing it. Four-day median processing time does not compensate for an error rate above the stated 2% limit. The pilot must be assessed on both measures, with consistent definitions and a stated measurement period.',
    precision_extra='A spending cap is a ceiling, not an instruction to spend the full amount. Pilot approval also has a scope and duration. Reaching the end of twelve weeks does not automatically authorize additional sites, more spending, or a rollout; those require the specified subsequent decision.',
    phrases='''Open with the request | We request approval for a twelve-week pilot at two sites.
State the ceiling | Total pilot spending must not exceed $150,000.
Name the outcome | The target is a four-day median processing time.
Preserve the baseline | The measured baseline is six days on the stated definition.
Protect quality | The error rate must remain at or below 2%.
Assign delivery | The operations director will own implementation.
Separate verification | Finance will verify spending against the approved cap.
Define the next decision | Wider rollout would require a separate board decision.
Reduce dashboard clutter | Retain measures that show results, guardrails, or material exceptions.
Specify measurement | Use the same case population and calculation when comparing periods.
Clarify reporting | Agree who reports each measure and at what frequency.
Escalate an exception | A threatened cap or guardrail breach must reach the named decision owner.
Document authority | Record the scope and conditions of the approval explicitly.
Avoid premature success | The pilot is not successful merely because it launched on time.
Prepare the review | Present the evidence, limitations, and options at the final review.
Close with boundaries | This request does not authorize extra sites or an automatic extension.''',
    notes='''Approve versus note | Approval authorizes a specified action; noting a report does not necessarily do so.
Cap versus budget target | A ceiling should not create pressure to spend unnecessarily.
Median versus mean | Name the statistic and keep it consistent across comparisons.
Faster and acceptable | Assess the speed target together with the quality limit.
Owner versus verifier | Delivery and independent checking are different responsibilities.
Pilot versus rollout | A small test needs a separate scope and decision from wider implementation.''',
    d='''Which opening makes the decision clearest? | Approve a twelve-week, two-site pilot with spending capped at $150,000. | Here are twelve metrics and a general update. | Approve whatever scope the team later finds convenient. | Note that all future rollout decisions are already implied. | The correct opening states the requested action and its three explicit limits without expanding authorization.
A pilot reaches four days but has a 2.5% error rate. What is accurate? | It meets the speed target but breaches the stated quality guardrail. | It meets both conditions because speed improved. | The error rate can be ignored after launch. | The board must approve rollout automatically. | Four days meets the speed target, but 2.5% exceeds the maximum permitted error rate of 2%.
What follows from spending only $135,000 within the approved scope? | The team is below the cap; it need not spend the remaining $15,000. | The remaining $15,000 must be spent to prove success. | The unused amount automatically authorizes another site. | The quality guardrail no longer applies. | A cap is a maximum rather than a required spending target or permission to expand scope.
What must precede a wider rollout? | Review the pilot evidence and obtain the separate required decision. | Let the twelve-week end date authorize it automatically. | Treat a launch announcement as board approval. | Replace the final review with an unrelated metric count. | The brief requires a final evidence review before the board considers further investment.''',
    dialogue='''Amara | The board pack has twelve metrics but no clear decision. Are we reporting progress, requesting advice, or asking for permission to start?
Tom | We need a clear [[decision request::The decision request explicitly states what the board is being asked to authorize.]]. We are asking for approval of a twelve-week pilot at two sites, with a maximum total spend of one hundred fifty thousand dollars.
Amara | Put that on the first substantive slide. The directors should know the requested action before they interpret a dashboard or listen to the operating detail.
Tom | I will state the [[pilot scope::Pilot scope defines the limited sites, duration, and activities being tested; it must not imply permission for wider implementation.]] explicitly. We are not requesting a company-wide rollout, an automatic extension, or permission to add locations as the team finds new opportunities.
Amara | The current processing baseline is six days. We need to show what would count as meaningful improvement and how the number will be calculated.
Tom | The [[outcome metric::The outcome metric tracks the intended improvement: median processing time moving from six days to the four-day target.]] is median processing time, with a four-day target. We will preserve the calculation and case definitions so the comparison does not improve simply because its basis changes.
Amara | Speed alone could create the wrong incentive. A faster process would not be a success if the team introduced more errors while rushing work through.
Tom | The error rate is our [[guardrail metric::The guardrail metric protects quality while speed improves; the case sets a maximum error rate of 2%.]]. It must stay at or below two percent. The review needs both results, not a headline that highlights speed and hides quality.
Amara | Who will be accountable for implementation? The draft names several functions, but that can leave everyone assuming someone else is responsible for the final result.
Tom | I will be the [[delivery owner::The delivery owner is accountable for implementing the pilot; naming several supporting functions does not replace a clear accountable person.]]. The supporting teams will have defined responsibilities, while finance separately verifies spending rather than becoming responsible for operational delivery.
Amara | We should also clarify the financial boundary. Some people hear a budget number as a target they are expected to use up before the period ends.
Tom | It is a [[spending cap::The spending cap limits expenditure; unused funds do not require spending or authorize expansion.]], not a spending obligation. Being below it does not authorize extra sites, and reaching it does not justify further spending without the necessary decision.
Amara | The board will need timely information if the pilot is moving outside its limits. Waiting until week twelve could make the review too late to help.
Tom | We should agree a [[reporting cadence::Reporting cadence sets the frequency of updates so the relevant decision-makers receive evidence in time to oversee the pilot.]] and an exception route before launch. Routine updates can be brief, but threatened breaches need attention from the person authorized to respond.
Amara | We do not need twelve measures in the main presentation. Some describe activity without showing whether the result is acceptable.
Tom | We can retain supporting detail and focus the main [[board narrative::The board narrative connects the requested decision with relevant evidence, limits, and accountability.]] on the request, outcome, quality limit, spending, and material exceptions. That preserves useful evidence without making directors assemble the recommendation themselves.
Amara | At the end, we need to assess the evidence and its limitations. Two sites may teach us something important without proving the model will work everywhere.
Tom | The final [[stage review::The stage review assesses evidence before a later commitment; completing the pilot does not itself authorize company-wide rollout.]] should compare results with the agreed criteria and identify remaining uncertainty. Any wider rollout stays a separate decision, even if the pilot looks encouraging.
Amara | I will make the approval wording precise and record its limits. Readers should not have to reconstruct authority from slides.
Tom | A clear [[decision record::The decision record documents approval and its limits, preventing an open-ended interpretation.]] will help. It should distinguish what was approved, what must be monitored, and what remains unapproved, so implementation follows the actual decision rather than an optimistic interpretation.''',
    transfer_title='Faster, but outside the quality limit',
    transfer_setup='At review, median processing time is four days, the error rate is 2.5%, and spending is $135,000. The pilot limits remain four days, at most 2% errors, and at most $150,000 spending.',
    transfer='''Lead: "The processing-time target was ___." | met | The reported median equals the four-day target supplied in the briefing.
Reviewer: "The quality guardrail was ___." | breached | The 2.5% error rate exceeds the stated maximum of 2%, despite the speed improvement.
Lead: "Spending remained below the ___." | cap | The $135,000 total is less than the authorized $150,000 ceiling.
Reviewer: "Rollout still requires a separate ___." | decision | Meeting some pilot measures does not authorize rollout, especially with an unresolved guardrail breach.'''))
