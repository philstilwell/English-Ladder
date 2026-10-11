"""Original client-facing financial-advice communication practice."""
from books.authoring import unit

BOOK = dict(
    slug='financial-advice', title='Financial Advice English',
    cover_label='Advisers / client conversations / informed decisions',
    cover_title='Financial\nAdvice', cover_size=32,
    tagline='Make goals concrete. Explain choices clearly. Keep trust grounded in facts.',
    audience='For financial advisers, planners, client-service colleagues, and supervised advice teams.',
    map_intro='Guide a client conversation from discovery through explanation, documentation, and follow-through.',
    notes_title='Reassurance is not a guarantee.',
    notes_intro='Clients bring goals, incomplete information, uncertainty, and sometimes strong emotion. Effective advice English makes room for those concerns while keeping costs, risks, assumptions, and authority clear. These fictional cases practice communication, not recommendations for real portfolios.',
    field_notes=[
        ('Ask for the missing fact', 'Translate a broad goal into the amount, date, priority, and constraints needed for analysis. Explain why the information matters instead of treating a questionnaire as the conversation.', '"Which spending estimate and retirement date should the first illustration use?"'),
        ('Name the relationship', 'Clients need to know the service, professional capacity, fee basis, and limits that apply. A title alone does not explain what the firm will do or how it is paid.', '"Let us use the current relationship summary and agreement to check the service and charges."'),
        ('Preserve client agency', 'Explain relevant alternatives and check understanding without pressuring the client or confusing a question with an instruction. Family involvement does not itself confer account authority.', '"We can compare the options before you decide; no change is authorized by this discussion."'),
        ('Make uncertainty specific', 'Identify which result is historical, which is modeled, and which information is missing. A useful qualification tells the client what changes the conclusion and what happens next.', '"This chart uses a constant return assumption; actual returns and spending can differ."')],
    scope_note='Fictional English-language practice, not personalized financial, investment, insurance, tax, or legal advice. US terminology is used where identified; professional duties and account rules vary. Actual recommendations require current documents, client facts, applicable rules, and qualified review. No product or transaction is endorsed.',
    sources=[
        dict(title='Investor.gov. Customer and client relationship summaries (Form CRS).', url='https://www.investor.gov/CRS', note='Background for discussing services, fees, conflicts, and professional capacity in US retail relationships. Actual obligations depend on the applicable relationship and rules.', checked='10 October 2026'),
        dict(title='Investor.gov. How Fees and Expenses Affect Your Investment Portfolio.', url='https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated', note='Background for distinguishing fee layers and their effect. All fee examples in this book are invented teaching facts, not a firm quotation.', checked='10 October 2026'),
        dict(title='Internal Revenue Service. Retirement plan and IRA required minimum distributions FAQs.', url='https://www.irs.gov/retirement-plans/retirement-plan-and-ira-required-minimum-distributions-faqs', note='Background for US distribution terminology. Eligibility, deadlines, tax treatment, and exceptions need current individualized verification; the book does not prescribe them.', checked='10 October 2026'),
        dict(title='FINRA, SEC, and NASAA. Why You Should Consider Adding a Trusted Contact to Your Account.', url='https://www.finra.org/investors/insights/trusted-contact', note='Background for distinguishing a trusted contact from someone authorized to transact or decide for an account holder.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Advisor English: Discovery, Scope, Trust, and Boundaries', scene='Turning a retirement wish into usable planning facts',
    skill='Clarify an imprecise client goal and explain the information needed before an individualized recommendation.',
    brief='Leah tells adviser Sam, "I want to retire comfortably." She has not supplied a target date, spending estimate, or current asset and liability summary. The introductory meeting covers discovery and the proposed planning service; no engagement scope or investment recommendation has been finalized. Leah asks whether a single savings target can be supplied immediately. Sam can explain the process and request information through the approved secure channel, but cannot responsibly fill the missing facts with assumptions presented as her circumstances.',
    cast='Leah | Prospective client\nSam | Financial adviser',
    culture=('Make discovery collaborative, not interrogative', 'A client may not yet have exact numbers. Explain which estimate is needed first, distinguish a provisional input from a verified fact, and acknowledge the goal in the client\'s own words. A warm response can still be clear that a reliable recommendation requires more information.'),
    a='''Which key facts are missing? | Retirement date, spending estimate, and current financial summary | A guaranteed investment product | A completed tax return prepared by Sam | A confirmed trading instruction | The briefing identifies the date, spending, and asset-liability information as missing inputs for the planning discussion.
What is the current meeting's purpose? | Discovery and explanation of the proposed planning service | Execution of an approved portfolio change | Confirmation of guaranteed retirement income | Acceptance of a final savings target | The meeting is introductory and no engagement scope or recommendation has been finalized.
How should any provisional number be described? | As an assumption to check, not a verified client fact | As Leah's confirmed financial position | As guaranteed investment performance | As automatic permission to trade | The case requires keeping estimates and missing information distinct from verified circumstances and client authority.''',
    vocabulary='''discovery meeting | An initial discussion to understand a client's circumstances and aims. | conduct a discovery meeting
fact-find | Structured collection of information relevant to planning or advice. | complete the client fact-find
planning scope | The agreed topics and services included in a planning assignment. | define the planning scope
engagement agreement | Terms describing the professional relationship and services. | review the engagement agreement
financial goal | A desired outcome expressed with relevant amount, timing, and priority. | clarify a financial goal
target retirement date | The date or period the client aims to stop or reduce work. | confirm the target retirement date
spending estimate | An approximation of expected outgoings on a stated basis. | build a spending estimate
essential spending | Costs the client treats as necessary for basic or committed needs. | identify essential spending
discretionary spending | Outgoings the client has greater ability to adjust. | distinguish discretionary spending
household cash flow | Money received and paid by a household over a period. | review household cash flow
asset summary | An account of owned resources and their relevant characteristics. | prepare an asset summary
liability summary | An account of debts and other obligations. | update the liability summary
net worth | Assets less liabilities on a defined valuation basis. | estimate household net worth
pension statement | A record of pension information issued by a plan or provider. | obtain a current pension statement
income source | An identified origin of household receipts. | verify each income source
dependant | A person relying on the client for financial support in context. | identify financial dependants
emergency reserve | Resources intended for unexpected needs, with access and amount requiring context. | discuss the emergency reserve
time horizon | The period before or over which money is expected to be needed. | distinguish planning time horizons
constraint | A condition limiting available choices. | document a planning constraint
priority | Relative importance assigned to a goal or need. | confirm the client's priority
planning assumption | A provisional input used to explore possible outcomes. | label a planning assumption
information gap | Missing data relevant to the assessment. | identify an information gap
secure channel | An approved protected route for exchanging sensitive information. | use the secure document channel
scope limitation | A boundary on what the engagement or analysis covers. | explain a scope limitation''',
    precision='Comfortably is a useful expression of a goal, not a defined spending amount. A date and spending estimate need a basis: today\'s money or future amounts, household or individual, before or after tax. Do not silently choose those meanings for the client.',
    precision_extra='Discovery is not automatically a finalized engagement or a recommendation. Estimates can support an initial illustration when clearly labeled, but the adviser should not present invented assets, income, priorities, or authority as confirmed client facts.',
    phrases='''Acknowledge the aim | You want retirement to feel financially secure and manageable.
Make it concrete | What timing should we use for your target retirement date?
Clarify spending | Does that estimate cover the household or only your own spending?
Check the basis | Are these amounts in today's money or projected future amounts?
Separate priorities | Which costs are essential, and which could change?
Request the record | Please provide current asset, liability, and pension information through the secure channel.
Limit the estimate | An initial illustration would use assumptions that we need to verify.
Close the meeting | We will confirm the information and service scope before a personalized recommendation.
Avoid a promise | I cannot give a reliable single target from the goal alone.
Clarify services | The proposed scope does not automatically include tax or legal advice.
Preserve agency | Reviewing the information does not authorize an investment change.
Explain a request | The dates and spending basis affect how we interpret the target.
Identify uncertainty | We can record a provisional range without treating it as confirmed spending.
Confirm the household | Who relies on the income included in this plan?
Summarize accurately | The goal is clear; the amount, timing, and current position remain incomplete.
Check understanding | Does this summary distinguish your confirmed facts from our open questions?''',
    notes='''Comfortable and sufficient | These words need the client's meaning; they do not specify a universal amount.
Today's money | This phrase identifies purchasing-power basis and should not be confused with a future nominal amount.
Could versus can confirm | Could introduces a possible illustration; can confirm claims that a fact is established.
Scope wording | Included, excluded, and referred for specialist advice describe service boundaries plainly.
Estimated versus verified | Keep the status next to the number instead of relying on a general caveat elsewhere.
Client-centered summary | Use the client's stated goal without adding an investment preference they have not expressed.''',
    d='''Which response best develops the vague goal? | Let us clarify the retirement date, spending basis, and current financial position. | Everyone needs exactly the same retirement amount. | A comfortable retirement is guaranteed if you sign today. | Your missing asset total must be zero. | The response seeks the case's missing inputs without inventing facts or promising an outcome.
Which question clarifies the scope and purchasing-power basis of a spending estimate? | Is the amount for the household and expressed in today's money? | Which adviser will attend the next review meeting? | Which investments currently pay distributions into the account? | Which provider issued the most recent pension statement? | Household coverage and today's-money versus future-money amounts define the estimate's meaning. The provider, income sources and meeting arrangements answer different planning questions.
Which statement correctly limits an initial illustration? | It uses labeled assumptions that still need verification. | It proves the final recommended target. | It confirms every unknown asset value. | It authorizes purchases in the account. | A preliminary illustration explores assumptions; it does not establish missing facts or trading authority.
Which route fits the sensitive document request? | The firm's approved secure channel | A public discussion board | An unverified message recipient | A shared link open to anyone | The briefing specifies a secure approved route for personal financial information rather than unrestricted disclosure.''',
    dialogue='''Leah | I want to retire comfortably, but I do not know what number to aim for. Can you give me a savings target before we finish today?
Sam | We can clarify the goal first. A useful [[target::A target needs relevant timing and spending context; an unsupported single number would not represent Leah's circumstances.]] depends on when you expect to retire, your spending needs, and the resources already available.
Leah | I might stop full-time work in several years, although part-time work could remain an option. I have not chosen an exact date.
Sam | Let us record that as an open [[time horizon::The time horizon identifies when resources are needed; Leah has not yet confirmed the timing or future work pattern.]], not a fixed retirement date. We can examine alternatives without treating either one as your confirmed instruction.
Leah | I can provide recent household bills. Travel and future healthcare costs are less certain, so my first spending estimate would be incomplete.
Sam | Separate [[essential spending::Essential spending covers costs treated as necessary or committed, helping distinguish them from more adjustable preferences.]] from the more adjustable items. We can mark uncertain amounts clearly rather than filling the gaps with figures that look precise but lack support.
Leah | Should the estimate describe what those things cost now, or what they might cost in the year I stop working? Those numbers could be quite different.
Sam | Exactly. Identify whether it is in [[today's money::Today's money expresses current purchasing power; it is different from an unqualified future nominal spending figure.]] or future amounts. We also need to know whether it covers your household and whether taxes are included in the estimate.
Leah | I have account statements in several places, plus a pension statement and a mortgage. I do not have a single page showing my current position.
Sam | An [[asset summary::An asset summary brings owned resources together; it supports planning but should not omit debts or be confused with net worth.]] will help, alongside the liabilities and income sources. Use current statements where available and label anything still estimated or missing.
Leah | I would rather not email the details to an unverified address. How should I send the documents?
Sam | Use our approved [[secure channel::A secure channel is the firm's protected document route; it reduces inappropriate exposure of sensitive client information.]]. I will explain how to verify and access it through our established contact route, without asking you to post private information publicly.
Leah | Will the planning service also decide the legal and tax questions connected to retirement? I do not want to assume those are included just because they affect the plan.
Sam | We need to agree the [[planning scope::Planning scope defines the services included; related tax or legal questions are not automatically covered by the proposed engagement.]]. I will explain our services and boundaries, including where a qualified tax or legal professional's separate input may be needed.
Leah | Once you have the documents, could you show a preliminary illustration even if a few spending amounts are still approximate? Seeing the assumptions might help me check them.
Sam | Yes, where appropriate, with each [[planning assumption::A planning assumption is a provisional input, not a verified fact or promised outcome; labeling it supports meaningful review.]] visible. An illustration can organize the discussion, but it must not disguise an uncertain input as a fact or guarantee the result.
Leah | I sometimes help a family member with bills. The amount varies. How should we include that without pretending it is a fixed monthly expense?
Sam | Include that [[commitment::The commitment is a potential household support need; recording its uncertainty prevents it from being silently excluded from planning.]] with its uncertainty and importance to you. We should understand your priorities rather than assume every optional-looking payment is something you would comfortably stop.
Leah | I will bring the records and work out what I spend now. Please leave the investments as they are while we clarify the plan.
Sam | Correct. We will review the information and proposed [[engagement agreement::The engagement agreement records the relationship and services; reviewing discovery information does not itself finalize scope or authorize investments.]] before finalizing the scope and an individualized recommendation. Today's goal is a clear starting point, not an unsupported answer.''',
    transfer_title='A goal without a currency',
    transfer_setup='A client says they need "forty thousand a year" but has not identified the currency, household scope, or whether the amount is before or after tax. No target has been approved.',
    transfer='''Adviser: "First, which ___ does the amount use?" | currency | The same number means different monetary amounts in different currencies, so the unit must be identified.
Client: "I also need to clarify whether it covers the whole ___." | household | Household scope distinguishes one person's spending from the combined needs of several people.
Adviser: "Please specify whether the figure is before or after ___." | tax | Tax basis affects how an income requirement relates to spendable money and must not be assumed.
Client: "Until then, treat it as an incomplete planning ___." | input | The unqualified amount is not sufficient to establish a reliable target or an approved recommendation.''',
    rehearsal=["Read Leah and Sam's corrected discovery exchange. Keep the retirement date, spending basis and current financial summary as missing facts, not invented estimates.","Switch roles. Stress the requests for household scope and today's-money amounts, and the separate need to agree the planning service.","Read the corrected transfer twice. Preserve all three missing qualifiers: currency, household coverage and before- or after-tax basis."]))

BOOK['units'].append(unit(
    title='Standards of Conduct, Best Interest, Disclosures, and Conflicts', scene='What the advisory fee includes, and what it does not',
    skill='Explain compensation, additional costs, and conflicts using current disclosures and a bounded illustration.',
    brief='Client Rosa asks adviser Evan how the firm is paid. The fictional advisory agreement charges 1% per year on the defined billable asset value, billed quarterly under its stated calculation method. For a simple illustration only, assume a constant $500,000 billable balance for a full year. Product expenses and certain third-party charges are additional, not included in that 1%. Evan has the current agreement and relationship disclosures. No assurance that conflicts are absent or that a fee depends on positive returns is supported.',
    cast='Rosa | Client\nEvan | Adviser',
    culture=('Explain the incentive as well as the price', 'A client asking about compensation is testing how the relationship works, not necessarily accusing the adviser of bad faith. Give the fee basis, services, excluded costs, and relevant incentives plainly. Disclosure informs the conversation; it is not a reason to avoid explaining a conflict.'),
    a='''What is the annual advisory-fee illustration on the stated constant balance? | $5,000 | $500 | $50,000 | $1,000 | One percent of $500,000 is $5,000 for the full year under the explicitly simplified constant-balance illustration.
Which costs are included in the 1% according to the case? | The defined advisory fee, not all product and third-party charges | Every possible investment cost | All taxes and legal fees | Only costs when returns are positive | The briefing says product expenses and certain third-party charges are additional, so the fee is not an all-cost figure.
What documents should guide Evan's explanation? | The current agreement and relationship disclosures | An assumed universal industry fee | A previous firm's brochure | An invented no-conflict guarantee | The case supplies current documents, which define this fictional relationship more reliably than assumptions about other arrangements.''',
    vocabulary='''advisory capacity | Acting in the role of an investment adviser under the relevant relationship. | clarify advisory capacity
brokerage capacity | Acting in a brokerage role for the relevant service or transaction. | identify brokerage capacity
dual registrant | A firm registered for both brokerage and investment-advisory activities in the US context. | explain a dual registrant's roles
standard of conduct | The professional or legal duties applying in the relevant circumstances. | explain the applicable standard of conduct
fiduciary duty | Duties of loyalty and care arising in a legally defined relationship. | clarify the scope of fiduciary duty
best interest | A conduct requirement or objective whose precise duties depend on applicable rules. | discuss the best-interest obligation
Form CRS | A US retail relationship summary for covered brokerage and advisory firms. | review the current Form CRS
disclosure | Information provided about material terms, risks, costs, or conflicts. | explain the relevant disclosure
compensation | Payment or other benefit received for services or activity. | describe the compensation arrangement
asset-based fee | A charge calculated using a defined measure of assets. | explain the asset-based fee
billable assets | Assets included in the contractual fee calculation. | identify billable assets
billing period | The interval for which charges are calculated or collected. | confirm the billing period
fee schedule | A statement of charges and how they are determined. | consult the current fee schedule
commission | Transaction-related compensation under the relevant arrangement. | disclose the commission structure
markup | An amount added to a transaction price under the relevant dealing arrangement. | explain a transaction markup
expense ratio | A fund's annual operating expenses relative to its specified asset measure. | identify the fund expense ratio
custody fee | A charge for specified account or asset-holding services. | check applicable custody fees
third-party charge | A cost imposed by another provider rather than the quoted service fee. | identify third-party charges
wrap fee | A bundled charge covering specified services and transactions, not necessarily every cost. | review wrap-fee exclusions
conflict of interest | An interest or incentive that may affect judgment or conduct. | disclose a relevant conflict of interest
incentive | A potential reward or pressure influencing a choice. | explain the financial incentive
referral payment | Compensation for directing business to another party. | disclose a referral payment
conflict mitigation | Steps intended to reduce the effect or risk of a conflict. | explain conflict-mitigation measures
informed decision | A choice made with adequate understanding of relevant information. | support an informed decision''',
    precision='The $5,000 figure illustrates 1% of a constant $500,000 billable balance for a full year. Actual quarterly bills follow the agreement\'s valuation, timing, and adjustment method. Do not present this simple illustration as a verified invoice or an all-in cost.',
    precision_extra='An asset-based advisory fee is not inherently payable only when returns are positive. Disclosure of a conflict does not mean the conflict disappears or that every legal obligation is satisfied. The service, professional capacity, applicable rules, and actual incentives need accurate explanation.',
    phrases='''Name the arrangement | This advisory service uses the fee basis in the current agreement.
State the rate | The stated annual advisory rate is 1% of defined billable assets.
Bound the illustration | At a constant $500,000 for a full year, that illustrates $5,000.
Explain billing | Actual quarterly bills follow the agreement's calculation method.
Identify exclusions | Product expenses and certain third-party charges are additional.
Avoid a false condition | The fee is not described as payable only after a positive return.
Explain incentives | An asset-based fee creates an incentive related to the assets under advice.
Close with the documents | Let us review the services, costs, and conflicts together.
Clarify capacity | Which role and service are we discussing for this account?
Define the base | Not every quoted account value necessarily equals billable assets.
Separate layers | The adviser charge and product expenses are different cost components.
Reject an absolute | I cannot describe the relationship as conflict-free merely because disclosures exist.
Explain mitigation | The documents describe how relevant conflicts are addressed.
Invite a precise question | Which charge or exclusion would you like me to locate in the agreement?
Preserve uncertainty | I will verify that additional charge before quoting an amount.
Confirm understanding | The 1% is the advisory rate, not a promise that all costs are included.''',
    notes='''Per year versus per quarter | A rate quoted annually can be billed quarterly; do not imply that the annual percentage is charged four times.
On versus of | A fee on assets identifies its base; one percent of the stated balance calculates the simple illustration.
Included and additional | These words define cost boundaries and should appear near the headline fee.
Conflict language | Describe the actual incentive and response, not only a reassuring claim of independence.
Conditional quotations | A fee example tied to a constant balance is not a bill when the actual valuation method differs.
Relationship precision | A firm may offer different services; the applicable role should be clear for the specific discussion.''',
    d='''Which explanation keeps the fee illustration bounded? | One percent of a constant $500,000 illustrates $5,000 annually; actual billing follows the agreement. | Every quarterly invoice is definitely $5,000. | The fee is exactly $500 per year for every account. | The example proves all costs are included. | The correct wording preserves the assumed balance, annual period, and distinction between an example and actual contractual billing.
Which response accurately addresses additional costs? | Product expenses and certain third-party charges are separate from the advisory fee. | No other cost can ever apply. | Taxes are automatically covered by the 1%. | Every product has a zero expense ratio. | The case explicitly excludes these additional layers from the quoted advisory rate.
Which statement avoids overstating disclosure's effect? | Disclosures explain relevant conflicts; they do not make the incentives vanish. | Signing a disclosure removes every conflict. | A disclosed incentive can never matter. | Disclosure means no further duties apply. | Explaining a conflict does not eliminate the underlying incentive or replace other applicable obligations.
Which question clarifies the fee base? | Which assets and valuation method determine the billable amount? | How often will the adviser send a performance report? | What investment return would be needed to cover the fee? | Which date will the next invoice be delivered? | The base is the contractual asset measure used to calculate the charge. Report frequency, a break-even return and invoice delivery timing do not identify that measure.''',
    dialogue='''Rosa | I understand that advice has a cost, but I am not clear how you are paid. Does the one-percent figure apply only when my account makes a profit?
Evan | It is an [[asset-based fee::An asset-based fee uses a defined asset value, not necessarily investment gains; the case does not make payment conditional on positive returns.]] under this agreement, not a share of positive returns. Let us look at the calculation and the services it covers.
Rosa | If the relevant balance stayed at five hundred thousand dollars for a year, what would that percentage mean in dollars before any other charges?
Evan | On that simple assumption, the annual [[illustration::The illustration uses a constant balance and full-year period; it explains the rate without pretending to be an actual invoice.]] is five thousand dollars. Actual invoices follow the agreement's valuation, timing, and adjustment method rather than this simplified example alone.
Rosa | Does quarterly billing mean the annual percentage is charged four times? I want to check that I understand the difference.
Evan | No. One percent is the annual rate, not the rate charged each quarter. The quarterly [[billing period::The billing period identifies when charges are calculated or collected; quarterly billing does not make a quoted annual rate a quarterly rate.]] tells us the billing schedule. Actual amounts follow the agreement's calculation method.
Rosa | Does the one percent include the costs inside the investments, or could those reduce my account separately even though they do not appear as the adviser fee?
Evan | Our agreement lists [[product expenses::Product expenses are a separate cost layer in this case; the advisory rate does not automatically include costs within investments.]] and certain third-party charges as additional. I will distinguish those from our advisory fee instead of calling the rate an all-in cost.
Rosa | Is every asset on the account statement included in the amount used to calculate your charge?
Evan | We need the definition of [[billable assets::Billable assets are those included by the agreement's fee method; the headline account value should not be assumed identical.]] in the agreement. The visible account total alone does not establish the contractual fee base or which exclusions apply.
Rosa | If I keep more money with your firm, you earn more. How do you handle that incentive when you advise me about moving money elsewhere?
Evan | That is a relevant [[conflict of interest::The asset-related incentive may affect judgment; naming it explains a potential conflict rather than denying its existence.]] to explain. We should discuss the actual incentive and how it is addressed, using the current disclosures rather than simply claiming there are no conflicts.
Rosa | Does receiving the disclosure mean the conflict disappears or that I have agreed to every recommendation? I would still expect an explanation of the reasons for a proposed action.
Evan | No, it does not remove the conflict or approve a recommendation. A [[disclosure::Disclosure communicates relevant information; it does not remove incentives or turn receipt into agreement with every recommendation.]] informs you; it does not erase the incentive or replace other applicable obligations. We still need to explain recommendations within the relevant relationship and rules.
Rosa | I have seen firms offering brokerage and advisory services. Should I know which role applies before comparing charges or expectations about ongoing monitoring?
Evan | Yes. Clarify the professional [[capacity::Capacity identifies the role in which the professional acts; services, compensation, and duties must be understood in that context.]] and the service involved. A firm's general title is not enough to describe the role, agreement, or duties for a particular account.
Rosa | Where can I find a concise summary pointing me to the relevant services, costs, and conflicts before reading the detailed provisions?
Evan | The current [[relationship summary::The relationship summary outlines services, fees, conflicts, and related information for covered US retail relationships; detailed terms still matter.]] is a starting point, alongside the agreement and fuller disclosures. We can locate the relevant sections together and verify any charge I cannot confirm immediately.
Rosa | So I could pay the advisory fee in a year when the account loses money, and there may be separate investment costs. Please show me both.
Evan | That captures the important distinctions. The purpose is an [[informed decision::An informed decision requires understanding relevant terms and incentives, not merely receiving a document or accepting a reassuring fee label.]], with the services, calculation basis, exclusions, and incentives clear before you decide how to proceed.''',
    transfer_title='A quoted bundle has exclusions',
    transfer_setup='A fictional fee bundle includes advisory services and specified transaction charges. The current disclosure excludes fund expenses and certain custody charges. A client asks whether bundle means every cost is included.',
    transfer='''Adviser: "The bundle covers the ___ services, not every possible cost." | specified | The agreement defines what is bundled; the label alone does not expand coverage.
Client: "Please show the fund expenses and custody ___ separately." | charges | These are identified excluded cost layers that should remain distinct from the bundle.
Adviser: "The current disclosure lists those ___." | exclusions | Exclusions describe costs outside the stated bundle, correcting the assumption that every cost is included.
Client: "Then the bundle is not an all-cost ___." | guarantee | The facts expressly leave additional costs, so a promise that all costs are covered would mislead.''',
    rehearsal=["Read the corrected fee exchange. State 1% per year and the $5,000 constant-balance illustration; do not describe either as a quarterly rate or verified invoice.","Switch roles. Stress the distinction between additional product costs, the advisory charge and an incentive disclosed but not erased.","Read the corrected bundle transfer twice. Keep specified included services and the separately listed exclusions audible."]))

BOOK['units'].append(unit(
    title='Goals, Risk Profile, Asset Allocation, and IPS Language', scene='Comfortable with risk, but buying a home next year',
    skill='Distinguish willingness to take risk from capacity for loss and the timing of a specific goal.',
    brief='Client Theo says he is comfortable with investment risk, but expects to need $60,000 for a home purchase in twelve months. The purchase date has limited flexibility. Adviser Nia has not yet verified the household reserves, other assets, or funding alternatives. No allocation or trade is approved. For discussion only, Nia uses a hypothetical 20% decline on the $60,000 amount, which would leave $48,000 before any other effects. This is a stress example, not a forecast.',
    cast='Theo | Client\nNia | Adviser',
    culture=('A risk label is not the whole client profile', 'A client can be willing to experience market fluctuations while having little flexibility about a near-term payment. Ask about the specific goal, timing, and consequences of a loss without challenging the client\'s confidence or treating a questionnaire label as a complete recommendation.'),
    a='''What is the stated near-term need? | $60,000 for a home purchase in twelve months | Guaranteed retirement income next week | A confirmed $48,000 purchase price | Unlimited funds with no date | The briefing specifies the home-purchase amount and twelve-month timing, with limited flexibility.
What does the 20% decline represent? | A hypothetical stress example, not a forecast | A guaranteed market decline | Theo's actual recorded loss | An approved trading instruction | Nia uses a stated hypothetical to clarify consequences, not to predict markets or report an actual result.
Which facts still require verification? | Reserves, other assets, and funding alternatives | Whether Theo expressed willingness to take risk | Whether the purchase need is $60,000 | The arithmetic of the stated 20% example | The adviser has not verified the wider financial resources that affect capacity and planning flexibility.''',
    vocabulary='''risk profile | A combined account of risk attitudes, needs, capacity, and relevant circumstances. | update the risk profile
risk tolerance | Willingness to accept uncertainty or loss in pursuit of an objective. | assess stated risk tolerance
risk capacity | Financial ability to withstand adverse outcomes without undermining needs. | distinguish risk capacity from tolerance
required return | A modeled return needed to meet a goal under specified assumptions. | examine the required-return assumption
investment objective | The intended purpose or outcome of an investment approach. | clarify the investment objective
liquidity need | A requirement to access funds at a particular time or under certain conditions. | identify near-term liquidity needs
capital preservation | An objective of protecting the amount invested, subject to actual risks. | discuss the capital-preservation objective
investment horizon | The period over which an investment is intended to support a goal. | match the investment horizon to the goal
goal flexibility | Ability to change the amount, timing, or priority of an objective. | assess goal flexibility
funding gap | A difference between resources available and an amount required. | quantify the funding gap
stress scenario | An adverse hypothetical used to examine consequences. | explain a stress scenario
loss threshold | A specified loss level relevant to review or client concerns. | clarify the loss threshold
asset class | A category of investments with shared broad characteristics. | compare asset-class exposures
strategic allocation | A longer-term target distribution among investment categories. | review the strategic allocation
tactical allocation | A shorter-term allocation adjustment within a defined approach. | distinguish tactical from strategic allocation
diversification | Spreading exposures to reduce some concentration risks, not all losses. | explain diversification limits
correlation | A measure of how variables move together in the measured setting. | assess changing correlations
concentration | A large or dependent exposure to a particular source of risk. | identify portfolio concentration
investment constraint | A restriction affecting investment choices or implementation. | document an investment constraint
IPS | Investment policy statement, recording agreed objectives and investment guidelines. | review the IPS
target weight | An intended proportion of a portfolio assigned to an exposure. | specify the target weight
allocation range | Permitted or intended bounds around an allocation under a stated policy. | define an allocation range
rebalancing trigger | A condition prompting review or action to restore the intended allocation. | agree a rebalancing trigger
suitability assessment | Evaluation of a proposed approach against relevant client facts and rules. | support the suitability assessment''',
    precision='Risk tolerance describes willingness; capacity concerns the financial consequences a client can withstand. The $60,000 home goal has a short horizon and limited timing flexibility. That need cannot be erased by labeling Theo generally comfortable with risk.',
    precision_extra='A 20% decline from $60,000 leaves $48,000 and a $12,000 gap to the stated goal. This arithmetic illustrates consequences, not the probability of loss or a recommended investment. Diversification can reduce some risks but does not guarantee capital preservation.',
    phrases='''Acknowledge willingness | You are comfortable with fluctuations; let us check the consequences for this goal.
Separate the goal | The home-purchase money has a different horizon from long-term savings.
Clarify timing | How flexible is the twelve-month purchase date?
Test capacity | What resources would cover a shortfall without disrupting essential needs?
Label the example | This is a hypothetical decline, not a prediction.
Quantify the effect | A 20% decline would leave $48,000 of the $60,000 amount.
Preserve missing facts | The reserves and alternative funding sources are not yet verified.
Close with the profile | We will document the goal and constraints before recommending an allocation.
Avoid a shortcut | A questionnaire label does not settle the allocation for every goal.
Distinguish concepts | Willingness to accept risk is different from financial capacity for loss.
Clarify a need | Is the $60,000 required in full at the purchase date?
Keep agency | No trade is authorized by this discussion.
Explain diversification | It may reduce concentration risk, but it cannot guarantee against loss.
Document the guideline | The investment policy should reflect the agreed objectives and limits.
Check a change | Has the goal's timing or flexibility changed since the last review?
Confirm the summary | This goal needs its own assessment within the wider household plan.''',
    notes='''Willing versus able | Willing describes preference; able concerns resources and consequences. Neither alone completes the assessment.
Would under a scenario | Conditional wording identifies the effect of a hypothetical without claiming it will occur.
For this goal | This qualifier prevents a conclusion about one need from automatically covering the whole household portfolio.
Not yet verified | Use this phrase for missing evidence without implying that the resources do not exist.
Can reduce versus prevents | Diversification may reduce certain risks; prevents loss would make an unsupported guarantee.
Before recommending | This sequence keeps information gathering distinct from a completed allocation decision.''',
    d='''Which statement distinguishes tolerance and capacity? | A client may accept fluctuations emotionally but lack resources to absorb a near-term loss. | A client's positive risk questionnaire establishes enough funds for every goal. | A larger current balance establishes willingness to accept any decline. | A longer retirement horizon removes the separate home-purchase constraint. | Willingness and financial resilience are different. Theo's near-term home goal remains relevant despite a risk label, account size or another goal's longer horizon.
What is the gap after the stated stress decline? | $12,000 | $48,000 | $60,000 | $1,200 | Twenty percent of $60,000 is $12,000, leaving $48,000 against a $60,000 need.
Which description correctly limits the example? | A hypothetical consequence used to discuss flexibility | A guaranteed twelve-month market result | Proof of an actual account loss | An instruction to sell every asset | The case expressly uses a stress illustration, not a prediction, observed loss, or trading authorization.
Which next step fits the incomplete information? | Verify resources and record the goal's constraints before recommending. | Apply the same allocation to all goals immediately. | Assume unknown reserves are unlimited. | Treat a risk label as an approved trade. | The missing household information and goal limits need review before a suitable recommendation can be developed.''',
    dialogue='''Theo | I put comfortable with risk on the questionnaire. I do not want that answer ignored just because I also plan to buy a home next year.
Nia | Your stated [[risk tolerance::Risk tolerance describes willingness to accept uncertainty; acknowledging it does not settle the separate consequences for a near-term goal.]] matters. We also need to understand what a loss would mean for the specific sixty-thousand-dollar payment and its timing.
Theo | The purchase date is not very flexible. I could consider a different property, but I cannot assume the seller would wait for my investments to recover.
Nia | That limited [[goal flexibility::Goal flexibility concerns changing timing, amount, or priority; limited flexibility affects how a loss would interfere with the purchase.]] is important. The home money has a different purpose and horizon from funds you might leave invested for much longer.
Theo | I can accept seeing a statement fluctuate. The harder question is whether I could still complete the purchase if the value were lower when payment is due.
Nia | Exactly. That concerns [[risk capacity::Risk capacity concerns the financial ability to withstand a loss without undermining needs, distinct from emotional comfort with fluctuations.]], not just comfort. We need to verify your reserves and other funding options rather than assume you could replace a shortfall.
Theo | I have not gathered those records yet. Some savings are already intended for household emergencies, and I do not want to count them twice without discussing that purpose.
Nia | We will separate each [[liquidity need::A liquidity need identifies when funds must be accessible; emergency reserves and a home payment should not silently be treated as interchangeable.]] and any restrictions. An asset total alone does not tell us which money is available for this particular purchase.
Theo | Could you show the effect of a decline in dollars? A risk category is less useful to me than seeing how the home-payment amount might change.
Nia | Use this [[stress scenario::A stress scenario is an adverse hypothetical for examining consequences; it does not forecast the market or assign a probability.]] only as an illustration: a twenty-percent decline on sixty thousand would leave forty-eight thousand, before any other effects.
Theo | A twelve-thousand-dollar gap could delay the house purchase. I ticked comfortable with risk, but I had not connected that answer to losing part of the deposit.
Nia | Correct. The [[funding gap::The funding gap is the $12,000 difference between the stated $60,000 need and the hypothetical $48,000 remaining amount.]] makes the consequence concrete. It does not prove that decline will happen or determine which investment, if any, is appropriate.
Theo | Does diversification solve that problem? I have heard it described as protection, but I do not want to assume it guarantees the amount at the purchase date.
Nia | [[Diversification::Diversification spreads exposures and can reduce some concentration risks, but it does not guarantee against loss at the required date.]] has limits. It may reduce concentration risks, yet it cannot promise that the full amount will be available regardless of market conditions.
Theo | Then the questionnaire answer should remain in the record, alongside the short deadline and the fact that my other resources have not been verified.
Nia | Yes. The [[risk profile::The risk profile combines willingness, capacity, goals, and constraints; preserving all of them avoids reducing the client to one label.]] needs those dimensions together. We should neither ignore your willingness nor let it override the goal's practical constraints.
Theo | How would the agreed approach be recorded after we complete the review? I would like the purpose and boundaries clear enough to revisit if my plans change.
Nia | The [[IPS::The investment policy statement records agreed objectives and guidelines; it can provide a reference when goals or circumstances change.]] can document the relevant objectives and guidelines. Its scope and detail should match the service and decisions actually agreed with you.
Theo | I will confirm the purchase amount and which savings are already reserved. Please do not move anything until we have reviewed those figures together.
Nia | Correct. Those [[investment constraints::Investment constraints are limits affecting the choices; documenting them precedes, rather than substitutes for, a reviewed recommendation and client decision.]] will inform a reviewed recommendation. The next step is to verify the facts and explain the options, not infer a trade from your questionnaire.''',
    transfer_title='One household, two timelines',
    transfer_setup='A client needs $8,000 for tuition on a fixed date in six months and has a separate, more flexible retirement goal twenty years away. Other resources are unverified. No allocation has been recommended.',
    transfer='''Adviser: "The goals have different investment ___." | horizons | Six months and twenty years are distinct periods before or over which funds are needed.
Client: "The tuition has less timing ___." | flexibility | The case fixes the tuition date and describes retirement timing as more flexible, so the two goals have different timing constraints.
Adviser: "We must verify other resources before assessing loss ___." | capacity | Financial ability to absorb a loss depends on resources and consequences, not only willingness.
Client: "So my questionnaire result alone does not settle the ___." | allocation | A general label does not establish the investment distribution appropriate for both distinct goals.''',
    rehearsal=["Read the corrected risk conversation. Contrast Theo's willingness with the consequences for $60,000 needed in twelve months; stress that the 20% decline is hypothetical.","Switch roles. Keep the $48,000 remaining amount and $12,000 gap distinct, with household reserves still unverified.","Read the corrected transfer. Preserve the fixed tuition date and the more flexible twenty-year retirement goal without choosing an allocation."]))

BOOK['units'].append(unit(
    title='Retirement Planning, Income, Tax-Aware Conversations, and RMDs', scene='A smooth retirement chart mistaken for a promise',
    skill='Explain retirement-model assumptions and distinguish projected income from guarantees and withdrawal requirements.',
    brief='Client Elena sees a retirement chart with a fixed 5% annual return assumption and projected withdrawals of $3,000 per month. The illustration uses nominal amounts and excludes taxes and fees. It does not model varying annual returns. Adviser Malik must correct Elena\'s impression that the chart promises that income. Her account types and personal tax circumstances are not yet verified, and no required-minimum-distribution calculation has been completed. No retirement date or withdrawal instruction is approved.',
    cast='Elena | Client\nMalik | Retirement adviser',
    culture=('Correct the impression without dismissing the relief', 'A client may feel reassured by a smooth upward chart. Acknowledge that response, then explain precisely what the line represents and leaves out. Replace a vague disclaimer with the assumptions and missing checks that could change the result.'),
    a='''What is the 5% figure? | A fixed annual model assumption | A guaranteed account return | Elena's verified historical return | A required tax rate | The chart uses 5% as an input, not a promise, historical measurement, or established tax rate.
What does this illustration exclude? | Taxes and fees, with no varying-return sequence modeled | Every nominal amount | The monthly withdrawal illustration | The fixed return assumption | The briefing identifies taxes, fees, and changing annual returns as limitations that affect interpretation.
What has been approved? | No retirement date or withdrawal instruction | A guaranteed $3,000 monthly payment | A completed RMD amount | A final personalized tax result | The illustration has not produced an approved retirement decision, withdrawal instruction, or individualized distribution calculation.''',
    vocabulary='''retirement illustration | A modeled account of possible retirement outcomes under assumptions. | explain the retirement illustration
deterministic model | A model producing outcomes from a fixed set of inputs. | identify deterministic-model limits
stochastic model | A model using variable inputs or simulated paths under a defined method. | explain a stochastic model
Monte Carlo simulation | Repeated modeled trials using specified assumptions about uncertain inputs. | qualify Monte Carlo results
projection | An estimate of future outcomes based on stated premises. | distinguish a projection from a promise
nominal amount | An amount expressed in money units without adjusting for inflation. | label nominal amounts
real return | Return adjusted for inflation under the stated calculation basis. | distinguish real from nominal return
inflation assumption | A modeled rate of change in prices or purchasing costs. | review the inflation assumption
purchasing power | The goods or services an amount of money can buy. | discuss purchasing-power changes
withdrawal rate | Withdrawals relative to a specified account value and period. | define the withdrawal-rate basis
sequence risk | Risk from the order of returns when cash flows occur. | illustrate sequence-of-returns risk
longevity risk | Risk of financial resources not lasting through the relevant lifetime. | assess longevity risk
planning horizon | The span over which a plan models needs and resources. | extend the planning horizon
income floor | Resources intended to cover essential income needs under stated conditions. | assess the proposed income floor
pension benefit | A payment or entitlement under a pension arrangement's terms. | verify the pension-benefit estimate
Social Security estimate | A projected US public retirement benefit based on specified records and assumptions. | review the Social Security estimate
tax-deferred account | An account in which certain taxes are deferred under applicable rules. | identify tax-deferred accounts
Roth account | A US account type with specific contribution and distribution tax rules. | verify the Roth account type
RMD | Required minimum distribution under applicable retirement-account rules. | verify the RMD requirement
distribution | Money or assets paid out from an account or arrangement. | document the distribution request
withholding | An amount retained from a payment toward a tax obligation. | clarify tax withholding
tax basis | The tax-recognized amount relevant to determining taxable treatment. | verify the tax basis
marginal tax rate | The rate applying to an additional amount of taxable income under the relevant system. | distinguish the marginal tax rate
survivor benefit | A benefit potentially payable after another person's death under specified terms. | review survivor-benefit conditions''',
    precision='The projected $3,000 withdrawal is not a guaranteed payment. The model uses fixed 5% returns, nominal amounts, and no taxes or fees. A smooth line can hide variability and purchasing-power changes that matter to the client\'s interpretation.',
    precision_extra='A required minimum distribution is a rule-based withdrawal requirement, not a recommended spending amount or evidence that a withdrawal is sustainable. Account type, ownership, beneficiary status, age-related rules, and other facts can affect the analysis. Verify current rules and qualified tax advice for actual decisions.',
    phrases='''Acknowledge the reaction | I understand why the chart looked reassuring.
Correct the meaning | The line shows a modeled outcome, not promised income.
Name the assumption | It assumes a fixed 5% annual return rather than varying yearly results.
Identify exclusions | This version excludes taxes and fees.
Clarify purchasing power | The $3,000 is a nominal amount, not a guarantee of constant purchasing power.
Explain sequence | The order of returns can matter when withdrawals occur.
Separate tax questions | We need the account details before discussing the applicable distribution rules.
Close with revision | We will review the assumptions before using the chart to support a retirement decision.
Avoid a date promise | The illustration does not approve a retirement date.
Define a simulation | A simulation explores modeled paths; its percentages depend on its assumptions.
Distinguish a requirement | A required distribution is not automatically the amount you should spend.
Preserve a missing fact | Your account types and tax circumstances remain unverified.
Limit withholding | Withholding is not necessarily the final tax liability.
Check the period | What lifetime and spending horizon does this illustration cover?
Clarify benefits | Is that pension amount an estimate or a confirmed benefit under its terms?
Confirm understanding | The next step is to improve the model, not to execute a withdrawal.''',
    notes='''Assumes versus earns | The model assumes 5%; the account has not thereby earned or been promised 5%.
Nominal versus real | Nominal amounts omit an inflation adjustment; real measures account for purchasing-power effects under the stated method.
Could support | This phrase indicates conditional modeled support, not a guaranteed entitlement to a payment.
Required versus recommended | Required describes a rule; recommended describes advice based on circumstances. They are not interchangeable.
Probability language | A simulation percentage is conditional on the model, not a certainty about a person's life.
Not yet calculated | Identify unfinished tax or distribution work explicitly instead of substituting a generic rate or age rule.''',
    d='''Which sentence accurately describes the chart? | It projects withdrawals using a fixed return assumption and omits taxes and fees. | It guarantees $3,000 of real monthly income. | It proves the client can retire immediately. | It supplies a completed personal tax calculation. | The correct statement preserves the model inputs and exclusions instead of turning an illustration into a promise.
Which question tests purchasing-power interpretation? | Are the amounts nominal, and how is inflation reflected? | Can we ignore all price changes? | Does a smooth line mean prices never rise? | Is every future dollar identical in purchasing power? | Nominal amounts need an inflation interpretation before the client treats them as constant real spending capacity.
Which distinction is correct? | A required distribution is not automatically a sustainable spending recommendation. | Every RMD is a guarantee of lifetime income. | Withdrawal rules are identical for all account types. | An unverified tax rate can replace account review. | A rule-based minimum and a personalized sustainable spending assessment serve different purposes.
What does sequence risk concern? | The order of investment returns when withdrawals or other cash flows occur | The average size of yearly price changes without regard to their order | The risk of outliving the plan's modeled resource horizon | The decline in purchasing power caused by rising prices | Sequence risk concerns return order interacting with cash flows. Volatility, longevity and inflation are related planning considerations, but answer different questions.''',
    dialogue='''Elena | I felt relieved when I saw three thousand dollars a month on the chart. Can I treat that as the amount I'll receive after I retire?
Malik | Not as promised income. This is a [[projection::A projection is a modeled estimate based on premises; it is not a contractual promise of monthly income.]] using assumptions. Let's look at what it includes before you use it to decide when to leave work.
Elena | The line is so smooth that I thought the investments produced the same amount every year. Is that something the account is designed to do?
Malik | The smoothness comes from the fixed five-percent [[return assumption::The return assumption is an input to the chart; a constant modeled rate does not establish constant actual investment performance.]]. This version doesn't vary annual results. The investments themselves have not promised a constant rate.
Elena | Then I need to know what is missing from the spending figure. Is the three thousand already after the charges and tax I would pay?
Malik | No. This version excludes both taxes and [[fees::Fees are costs omitted from this version; their absence limits how the projected withdrawal relates to money available to the client.]]. We need those reviewed before describing what you could actually spend; the displayed withdrawal is not that completed calculation.
Elena | And in ten years, would that amount buy what it buys today? My main concern is covering bills, not seeing the same number each month.
Malik | The chart uses [[nominal amounts::Nominal amounts are money figures without an inflation adjustment; they do not assure constant purchasing power over time.]]. It hasn't established constant purchasing power. We'll make the inflation treatment explicit so the figures answer your spending question.
Elena | If markets fall early on, while I'm taking money out, could that be worse than the same poor years arriving much later in retirement?
Malik | Yes, that's [[sequence risk::Sequence risk concerns return order when cash flows occur; withdrawals can make early losses matter differently from later losses.]]. The order matters when money is being withdrawn. A single steady rate doesn't show how those different paths affect the remaining assets.
Elena | Another report gave a percentage chance of success. Would switching to that sort of chart turn this into something I could rely on as guaranteed?
Malik | No. A [[Monte Carlo simulation::Monte Carlo simulation explores repeated modeled paths; its results depend on assumptions and do not remove uncertainty about actual outcomes.]] explores many modeled paths. Its success percentage still depends on its inputs and definition of success; it isn't a personal guarantee.
Elena | Can we check that definition? Covering my bills for ten years is different from covering them throughout retirement. I don't want the chart to hide that difference.
Malik | We'll check the [[planning horizon::The planning horizon sets how long needs and resources are modeled; changing it can materially alter the apparent outcome.]] and spending definition together. A shorter modeled period can look easier without answering how long you actually need the money.
Elena | A friend mentioned the minimum amount retirement accounts require you to take out. Is that the amount you're recommending I spend, or a separate calculation?
Malik | An [[RMD::An RMD is a withdrawal requirement under applicable retirement-account rules, not automatically a sustainable or recommended spending amount.]] is a rule-based distribution requirement, not a recommended spending budget. We haven't calculated yours; we still need your account records and the applicable rules.
Elena | I have several accounts and haven't sent their details. I'd rather get that right than assume they all follow the same withdrawal and tax treatment.
Malik | We'll verify each [[account type::Account type and personal circumstances affect distribution and tax analysis; the missing records prevent a reliable individualized conclusion.]] and your circumstances. We'll also distinguish any withholding from final tax, instead of treating a deducted amount as a completed tax assessment.
Elena | Please include less favorable cases when we meet again. I'll bring the records. I'm not asking you to start withdrawals or setting a retirement date today.
Malik | Understood. We'll review the [[assumptions::Assumptions determine the modeled outcome; reviewing them and the exclusions is necessary before relying on the illustration for a decision.]], omitted costs and account details first. I'll record those next steps and that no withdrawal instruction has been given.''',
    transfer_title='Withholding is not the final tax bill',
    transfer_setup='A client sees $1,000 withheld from a fictional distribution and asks whether that settles the final tax amount. The full tax circumstances have not been reviewed. The adviser is not giving a completed tax calculation.',
    transfer='''Adviser: "The $1,000 is ___ from the payment." | withholding | Withholding is an amount retained toward tax, not necessarily the final amount owed.
Client: "It does not automatically equal my final tax ___." | liability | The final obligation depends on the applicable tax calculation and circumstances, which remain unreviewed.
Adviser: "That question requires your full circumstances and qualified ___." | review | A reliable individualized tax conclusion needs the relevant facts and appropriate professional assessment.
Client: "Please keep the distribution and tax-estimate ___ separate." | figures | The payment amount, withheld amount, and estimated final tax answer different questions and must not be merged.''',
    rehearsal=["Read the corrected retirement exchange. Stress the fixed 5% assumption, nominal $3,000 withdrawals and omitted taxes and fees; none is a promised payment.","Switch roles. Keep the variable-return and lifetime questions separate from the uncompleted account-rule calculation.","Read the corrected transfer twice. Distinguish $1,000 withheld from the final tax liability, which has not been calculated."]))

BOOK['units'].append(unit(
    title='Portfolio Reviews, Volatility, Rebalancing, and Behavioral Coaching', scene='A lower account balance is not all market loss',
    skill='Acknowledge concern, reconcile an account-value change, and separate explanation from a trading recommendation.',
    brief='Client Victor sees his account fall from $100,000 to $85,000 during the statement period. The supplied statement bridge lists a $10,000 withdrawal, $1,000 in fees, and a $4,000 negative investment change. No contributions are listed. Adviser June has verified that these amounts reconcile, but has not reviewed the performance-return method, cash-flow dates, or whether the current allocation differs from the agreed policy. Victor asks whether everything should be sold. No transaction instruction has been confirmed.',
    cast='Victor | Client\nJune | Adviser',
    culture=('Acknowledge the concern before correcting the arithmetic', 'A technically correct answer can sound dismissive when a client is worried. Name the concern, separate the components clearly, and avoid predicting a recovery. Do not treat a distressed question as a completed instruction or tell the client that emotion makes the question illegitimate.'),
    a='''Which amounts explain the $15,000 decline in account value? | $10,000 withdrawal, $1,000 fees, and $4,000 negative investment change | $15,000 of market loss only | $10,000 of fees and $5,000 contribution | A guaranteed $15,000 future recovery | The three stated components total the decline from $100,000 to $85,000 without treating the withdrawal as market performance.
What is not yet verified? | The performance-return method and allocation-policy comparison | The beginning balance | The withdrawal amount | Whether the listed amounts reconcile | The briefing distinguishes the verified dollar bridge from the unfinished return-method and allocation review.
What does Victor's question currently establish? | A concern and a request for discussion, not a confirmed transaction instruction | A completed sale of every asset | A signed revised investment policy | A guaranteed market recovery plan | The case expressly says no transaction instruction has been confirmed, despite the question about selling.''',
    vocabulary='''account value | The stated monetary value of holdings and cash at a specified time. | reconcile the change in account value
opening balance | The value at the start of the reporting interval. | verify the opening balance
closing balance | The value at the end of the reporting interval. | confirm the closing balance
contribution | Money or assets added to an account. | identify external contributions
withdrawal | Money or assets removed from an account. | separate withdrawals from investment results
net cash flow | Contributions less withdrawals on a defined basis. | reconcile net cash flows
investment change | A stated change attributable to investment results under the report's method. | verify the investment-change component
performance return | An investment-result measure calculated using a stated methodology. | confirm the performance-return method
statement reconciliation | Explanation linking statement totals and component movements. | complete the statement reconciliation
fee deduction | A charge removed from the account or its value. | identify fee deductions
market movement | Changes in market prices or valuations over a period. | separate market movement from withdrawals
unrealized loss | A decline in value of a position not yet disposed of on the stated basis. | distinguish unrealized from realized loss
realized loss | A loss recognized on disposal under the stated reporting basis. | explain a realized loss
cost basis | The recorded acquisition or tax basis used for a specified purpose. | verify the cost basis
allocation drift | Movement away from an intended portfolio distribution. | assess allocation drift
rebalancing | Adjusting exposures toward a specified target or policy. | review a rebalancing proposal
threshold | A defined level that prompts review or action. | check the rebalancing threshold
turnover | The extent of trading or replacement of holdings over a period. | assess portfolio turnover
transaction cost | A cost associated with buying, selling, or transferring an investment. | estimate transaction costs
tax consequence | A tax effect dependent on the transaction and applicable circumstances. | assess possible tax consequences
loss aversion | A tendency to experience losses more strongly than comparable gains. | discuss loss aversion without labeling the client
recency bias | A tendency to overweight recent experience when judging the future. | recognize possible recency bias
behavioral coaching | Support for understanding decisions and reactions without removing client agency. | provide respectful behavioral coaching
review cadence | The agreed frequency or triggers for reassessing a plan or account. | confirm the review cadence''',
    precision='The account-value decline is $15,000, but the supplied bridge attributes $10,000 to a withdrawal, $1,000 to fees, and $4,000 to investment change. The withdrawal is not a market loss. The investment change still matters and should not be minimized.',
    precision_extra='A dollar change is not automatically a properly calculated return percentage. Cash-flow timing and the reporting method matter. Rebalancing is a policy-based allocation action, not simply another name for selling after a decline. Costs, taxes, client facts, and authority require review.',
    phrases='''Acknowledge concern | I can see why the lower balance concerns you.
Separate the components | The decline includes a withdrawal, fees, and investment change.
State the arithmetic | Those three amounts reconcile the account from $100,000 to $85,000.
Avoid dismissal | The investment decline still deserves explanation.
Limit the percentage | I need the cash-flow timing and method before quoting a performance rate.
Avoid a recovery promise | I cannot promise when or whether a market recovery will occur.
Clarify the request | Are you asking to discuss selling, or giving an instruction that needs confirmation?
Close with a review | We will review the allocation and relevant consequences before any recommendation.
Preserve agency | Your concern is legitimate, and the decision remains yours within the service process.
Distinguish rebalancing | Rebalancing should be tied to the agreed allocation policy.
Check drift | How far has the current allocation moved from the target?
Keep costs visible | Any proposed trades need review of costs and tax consequences.
Name a missing check | The dollar bridge is complete; the return calculation remains unchecked.
Summarize the change | Not all of the lower balance represents investment loss.
Avoid a label | Let us examine the concern rather than describe you as an irrational investor.
Confirm follow-through | The next review will separate performance, cash flows, and the allocation question.''',
    notes='''Balance versus return | Account value includes flows and charges; performance return uses a defined method to evaluate investment results.
Still matters | This phrase acknowledges a genuine loss while correcting an exaggerated interpretation of the total decline.
Question versus instruction | Clarify intent and follow the authorization process instead of inferring a trade from a worried question.
May versus will recover | May identifies uncertainty; will recover promises an outcome that the case does not establish.
Policy-based verbs | Review, compare, propose, approve, and execute are separate stages of a rebalancing process.
Nonjudgmental wording | Describe the concern and evidence without diagnosing the client's behavior from one conversation.''',
    d='''Which response combines empathy and accurate explanation? | The lower balance is concerning; let us separate the withdrawal, fees, and investment change. | You lost $15,000 in the market and should panic. | Nothing important happened because some money was withdrawn. | Your concern proves you cannot make decisions. | The response acknowledges the concern while preserving all three components without exaggerating or dismissing investment loss.
Which calculation matches the supplied bridge? | $100,000 minus $10,000 minus $1,000 minus $4,000 equals $85,000. | $100,000 minus $15,000 in market losses equals the verified return. | $85,000 plus $10,000 equals the full opening value. | The withdrawal cancels every fee. | The arithmetic reconciles the balances using the specifically supplied withdrawal, fee, and investment-change components.
What remains necessary before quoting a performance percentage? | Verify cash-flow timing and the return-calculation method | Divide the $15,000 account decline by the opening balance | Divide the $4,000 investment change by the opening balance without checking dates | Use the closing balance as the denominator because it is more recent | The dollar bridge does not establish a return method or how to handle the withdrawal date. Each proposed shortcut chooses a numerator or denominator without resolving those inputs.
Which next step respects the unconfirmed instruction? | Clarify Victor's intent and complete the required review and authorization. | Sell every holding immediately from the question alone. | Promise a recovery to avoid further discussion. | Ignore the concern until the next annual meeting. | The case contains a question, not a confirmed instruction; clarification and the applicable process preserve client agency and accuracy.''',
    dialogue='''Victor | My account was one hundred thousand and now it's eighty-five thousand. Did the investments lose fifteen thousand? Should I just sell everything before it gets worse?
June | I can see why that [[closing balance::The closing balance is the end value; its decline needs explanation but is not automatically all investment loss.]] is upsetting. Let's separate the statement's movements first, then clarify what you want to discuss about the investments.
Victor | I did take ten thousand out. But please don't tell me there's nothing to worry about just because some of the decline was my own payment.
June | I won't. The [[withdrawal::A withdrawal removes money from the account; separating it prevents the client's own cash removal from being counted as market loss.]] explains ten thousand; fees explain one thousand; negative investment change is four thousand. That investment result still deserves a proper explanation.
Victor | So those three figures add to fifteen thousand, but it would be wrong to call all fifteen thousand a loss on the investments themselves?
June | Yes. That dollar [[reconciliation::Reconciliation connects the opening balance to the closing balance through the reported components without merging different causes.]] is checked: one hundred thousand less ten thousand, one thousand and four thousand gives eighty-five thousand. It separates the components without dismissing the decline.
Victor | Could you just call the investment part minus four percent? Four thousand divided by the starting hundred thousand seems straightforward enough for me to follow.
June | I need to check the [[performance-return method::The performance-return method determines how cash-flow timing is handled; a simple division may not match the appropriate reported return.]] and the withdrawal dates first. That shortcut may not reflect when money was invested during the period, so I won't label it the verified return.
Victor | All right. But I need the rest of this money. Can you tell me when the investments will get back to where they were?
June | I can't promise a recovery date. [[Market movement::Market movement is uncertain; the known statement change does not establish the timing or existence of a future recovery.]] is uncertain. We can review when you need the money and the exposure, without inventing a timetable for recovery.
Victor | When I said sell everything, I meant should we discuss that option. Please don't place any trades on the strength of that question.
June | Understood: no [[transaction instruction::A transaction instruction authorizes a specified action through the relevant process; Victor has clarified that he is currently asking about options.]] is confirmed. I'll record that we're discussing options, and keep any later decision separate from what you've asked me today.
Victor | You mentioned rebalancing at our last meeting. Would that answer a different question from selling because I'm worried by this month's statement?
June | It would. [[Rebalancing::Rebalancing adjusts exposures toward the intended policy or target; it is not simply an immediate sale in response to a decline.]] compares exposures with our agreed policy and adjusts toward its targets when appropriate. It isn't simply a name for selling after a fall.
Victor | Have you done that comparison yet? The total balance alone doesn't tell me which part of the account is above or below its intended share.
June | The [[allocation drift::Allocation drift measures departure from the intended distribution; the case has not yet completed that comparison.]] check is still pending. I'll compare the current holdings with the policy before we discuss whether a change is warranted and why.
Victor | Before I decide on any change, show me its costs and possible tax effects too. I don't want an apparent solution to create another problem.
June | We'll include [[transaction costs::Transaction costs are expenses of implementing trades; they matter alongside possible taxes and the purpose of a proposed change.]], possible taxes and your circumstances in the comparison. I'll explain the purpose of each proposal rather than treat more trading as progress by itself.
Victor | Please send the checked performance explanation and those options. For now, I need to understand the statement and the choices, not make a rushed trade.
June | I'll record those [[review steps::Review steps identify the unfinished performance and allocation work, keeping the response concrete without implying an approved transaction.]] and your request. The dollar movement is reconciled; the performance method and allocation comparison still need checking, and no trade is authorized.''',
    transfer_title='A deposit masks a negative investment result',
    transfer_setup='An account opens at $50,000 and receives a $10,000 contribution. The statement shows a $2,000 negative investment change and no other movements, giving a $58,000 closing value.',
    transfer='''Adviser: "The higher balance includes a $10,000 ___." | contribution | Added client money increases account value independently of the investment result.
Client: "The investment component is still a $2,000 ___." | decline | The supplied investment change is negative even though the closing account value exceeds the opening value.
Adviser: "The three amounts reconcile to the $58,000 closing ___." | balance | Fifty thousand plus ten thousand minus two thousand equals the stated closing account value.
Client: "A larger account value does not by itself prove a positive ___." | return | Contributions can raise value despite negative investment results, so value growth alone does not establish performance return.''',
    rehearsal=["Read the corrected statement conversation. Reconcile $100,000 to $85,000 using the $10,000 withdrawal, $1,000 fees and $4,000 investment decline.","Switch roles. Acknowledge the loss without calling the entire balance change market performance or treating the question as a sell order.","Read the corrected transfer. Keep the $10,000 contribution separate from the $2,000 investment decline within the $58,000 balance."]))

BOOK['units'].append(unit(
    title='Products, Account Types, Rollovers, Annuities, Insurance, and Alternatives', scene='Comparing accounts without the missing cost columns',
    skill='Compare options on consistent criteria and explain product and transfer limitations without recommending prematurely.',
    brief='Client Hana compares two fictional account services. Option A has a $120 annual account fee and on-request support; Option B has a $240 annual account fee and scheduled quarterly reviews. The short summary omits exit charges and product-level expenses. A full schedule, now available to adviser Louis, lists a $75 transfer-out charge for A and no transfer-out charge for B. Product expenses, the existing account type, and any tax effects still need review. Neither option is recommended or approved.',
    cast='Hana | Client\nLouis | Adviser',
    culture=('Compare the whole service, not one attractive number', 'A cheaper headline fee and a more frequent review service answer different questions. Put relevant costs, access conditions, service differences, and client needs on the same comparison. An incomplete summary is a reason to obtain the terms, not to invent missing values.'),
    a='''Which service difference is stated? | A offers on-request support; B offers quarterly reviews | Both promise identical monitoring | A guarantees higher returns | B includes unlimited legal advice | The case distinguishes support arrangements, not return guarantees or unlisted professional services.
What transfer-out charges does the full schedule show? | A: $75; B: none | A: none; B: $75 | Both: $240 | Neither charge is available | The complete schedule supplies the missing transfer-out terms, while other cost and tax questions remain open.
What remains unreviewed? | Product expenses, existing account type, and tax effects | The annual account fees | The stated support arrangements | The supplied transfer-out charges | The briefing separates known account-service facts from outstanding product and transfer-related review.''',
    vocabulary='''account wrapper | The legal or tax account structure holding investments, depending on context. | distinguish the account wrapper from the investment
taxable account | An account whose investment income or gains may be currently taxable under relevant rules. | identify a taxable account
IRA | Individual retirement arrangement, a US retirement-account category with specific rules. | verify the IRA type
employer-sponsored plan | A retirement arrangement offered through an employer under its governing terms. | review employer-plan features
rollover | A movement of eligible retirement assets subject to applicable rules and conditions. | evaluate a proposed rollover
direct transfer | Movement between providers or accounts through a specified direct process. | confirm the direct-transfer procedure
in-kind transfer | Movement of holdings without selling them in the transfer process, where supported. | check in-kind transfer eligibility
liquidation | Sale or conversion of holdings into cash. | explain liquidation consequences
transfer-out charge | A fee charged for moving an account or assets away from a provider. | identify the transfer-out charge
exit charge | A cost triggered by leaving a product or arrangement under its terms. | disclose an applicable exit charge
surrender charge | A product charge for specified early withdrawals or termination. | review the surrender-charge schedule
liquidity restriction | A condition limiting access to invested funds. | explain liquidity restrictions
lockup | A period during which withdrawal or transfer is restricted under the terms. | confirm the lockup period
redemption window | A specified period or opportunity for requesting withdrawal from a product. | identify the redemption window
annuity | An insurance contract with specified accumulation or payment features. | review the annuity contract
fixed annuity | An annuity with contract-defined fixed features, subject to its terms and issuer obligations. | explain fixed-annuity conditions
variable annuity | An annuity whose value or benefits depend partly on selected investments and contract terms. | explain variable-annuity risks
indexed annuity | An annuity with certain credited returns linked to an index formula under contract terms. | examine the indexed-annuity formula
rider | An optional contract feature with specific terms and possible additional cost. | review the rider charge
insurer credit risk | Risk that an insurer cannot meet its contractual obligations. | explain insurer credit risk
cash value | A policy or contract value accessible under specified terms and adjustments. | distinguish cash value from a benefit amount
prospectus | A formal document describing a securities offering or product and its material features. | read the current prospectus
product comparison | A side-by-side assessment using consistent, relevant criteria. | complete the product comparison
service level | The scope and frequency of support supplied under an agreement. | compare the service levels''',
    precision='Option A has a lower annual account fee, but the comparison also needs its $75 transfer-out charge and on-request service. Option B has a higher annual fee and quarterly reviews. No conclusion about overall suitability follows from one fee alone.',
    precision_extra='An account wrapper and the investments inside it are different. A move may involve transfer, liquidation, rollover rules, access restrictions, costs, or tax effects. An annuity label also does not establish universal guarantees, immediate access, or identical product terms.',
    phrases='''State the known fees | A charges $120 annually; B charges $240 annually.
Restore a missing column | The full schedule lists a $75 transfer-out charge for A.
Compare service | A offers support on request; B provides quarterly reviews.
Preserve the gap | Product expenses are not yet included in this comparison.
Separate the wrapper | The account type and the investments held inside it need separate review.
Avoid a shortcut | A lower annual account fee does not by itself settle the choice.
Check the move | Would this involve an in-kind transfer, a sale, or a retirement rollover?
Close with the terms | We will complete the comparison before discussing a recommendation.
Clarify access | Which restrictions or exit charges apply if you need the funds?
Check coverage | Does the quoted fee include the optional feature?
Limit a guarantee | Any contractual guarantee depends on its terms and the responsible issuer.
Ask about exclusions | Which services are outside the account agreement?
Clarify the label | An index-linked crediting formula is not the same as owning the index.
Check tax review | The tax effects depend on the actual account and transaction.
Preserve an alternative | Remaining in the existing arrangement also needs a fair comparison where relevant.
Confirm authority | Reviewing the options does not authorize a transfer or sale.''',
    notes='''Lower versus cheaper overall | A lower fee component does not establish the total cost across the expected use period.
Included versus omitted | An omitted charge is unknown in the summary, not necessarily zero.
Transfer versus sale | Moving assets and selling assets are different actions; confirm which process the proposal involves.
Guarantee qualifiers | Identify who owes what, under which conditions; do not broaden a limited contractual promise.
Like-for-like columns | Compare the same cost types, periods, service expectations, and access conditions.
Account versus product | An account holds investments; its tax structure is not itself a description of the holdings' risk.''',
    d='''Which comparison includes the supplied material differences? | A: $120 annual fee, $75 transfer-out, on-request support; B: $240 annual fee, no transfer-out charge, quarterly reviews. | A has no costs because its annual fee is lower. | Both accounts have identical service and exit terms. | B guarantees better returns because it costs more. | The complete comparison preserves each known fee and service difference without inferring returns or overall suitability.
What should an omitted product-expense figure be labeled? | Not yet reviewed, rather than assumed zero | Zero by definition | Included in every account fee automatically | Irrelevant to any comparison | The briefing leaves product expenses unreviewed, so a missing entry cannot truthfully be treated as no cost.
Which question most directly clarifies transfer mechanics and possible consequences? | Will the holdings move in kind or be sold, and what rules and costs apply? | Will the receiving firm use the same monthly statement layout? | Will the new adviser offer reviews on the same weekday? | Will the account retain the same nickname in the online portal? | Moving securities without selling differs from liquidation and can affect eligibility, costs and taxes. Administrative appearance and scheduling do not identify the transaction mechanics.
Which statement properly limits a product guarantee? | Its scope and conditions depend on the contract and responsible issuer. | Every annuity permits immediate free withdrawal. | A guarantee removes every kind of risk. | An optional rider has no cost because it is optional. | Product terms and issuer obligations determine the promise; the label alone does not eliminate costs, restrictions, or risk.''',
    dialogue='''Hana | Option A has the lower annual fee. The summary makes it look like the obvious choice, but I cannot find anything about leaving the account later.
Louis | The full schedule lists a seventy-five-dollar [[transfer-out charge::The transfer-out charge is an additional cost for leaving A; omission from the summary did not mean it was zero.]] for A and none for B. We should restore that missing information.
Hana | A is one hundred twenty dollars a year and B is two hundred forty. Does the higher charge buy a different service, or are they otherwise the same?
Louis | The [[service level::Service level identifies the support supplied; A offers on-request help while B includes scheduled quarterly reviews.]] differs: A offers on-request support and B schedules quarterly reviews. Whether that matters depends on your needs, not just the fee.
Hana | Then I should not call A cheapest overall from the annual fee alone. What other amounts have not yet been included in the comparison?
Louis | [[Product expenses::Product expenses are a separate investment-cost layer; the case has not reviewed them for either account option.]] remain unreviewed. The account fee is only one layer, so mark that gap rather than insert zero to make the table look complete.
Hana | My existing account is a retirement account, but I have not supplied the exact type. Could moving it differ from moving an ordinary taxable account?
Louis | Yes. Verify the [[account wrapper::The account wrapper defines the legal or tax structure, which affects transfer rules separately from the investments held.]] and transaction first. We should not describe tax effects before identifying the actual accounts and applicable rules.
Hana | I also want to know whether the investments move as they are or must be sold. A transfer sounds simple, but those are different actions.
Louis | An [[in-kind transfer::An in-kind transfer moves eligible holdings without selling them in that process; availability depends on the assets and receiving arrangement.]] may preserve eligible holdings; another route may require sales. Confirm the supported process rather than assuming every holding can move unchanged.
Hana | Would I have to sell what I already hold? I thought this was mainly a change of provider, not a sale that might create other costs.
Louis | Correct. [[Liquidation::Liquidation sells holdings or converts them to cash, potentially creating costs and tax effects beyond a change of provider.]] can involve costs and tax effects. Those need appropriate review before we explain what the move would mean for you.
Hana | Another brochure calls an annuity guaranteed. Does that mean I could withdraw the whole amount whenever I want, or is access a separate question?
Louis | Read access terms separately. A [[surrender charge::A surrender charge may apply to early withdrawals or termination; a guarantee label does not establish unrestricted free access.]] or other condition may apply. The contract must identify what is promised, by whom, and under which circumstances.
Hana | It mentions an optional income feature. Should I assume that is included in the base charge because it appears on the same page?
Louis | No. A [[rider::A rider is an optional contract feature with separate terms and possible cost; proximity to a quote does not establish inclusion.]] may have an additional cost and different conditions. Inclusion needs verification, not an inference from the brochure's layout.
Hana | I am not asking you to choose now. I want the account comparison completed and the separate product questions identified clearly before discussing a recommendation.
Louis | That is a useful [[product comparison::A product comparison uses consistent criteria and verified terms; an incomplete fee table is not a sufficient recommendation.]] request. We can organize costs, services, access, and risks while marking questions requiring more information or specialist review.
Hana | Include staying where I am as one option. I would like to see what I would actually gain or give up before agreeing to move.
Louis | Agreed. Review alternatives without presuming a [[rollover::A rollover moves eligible retirement assets under applicable rules; changing providers does not by itself establish that it is appropriate.]] or other move is appropriate. No transfer or sale is authorized by today's discussion of the documents.''',
    transfer_title='A free exit does not mean no costs',
    transfer_setup='A product has no stated exit charge, but ongoing expenses and possible transaction costs remain unreviewed. A client asks whether "no exit charge" means the product is cost-free.',
    transfer='''Adviser: "No exit charge describes one cost ___." | category | The absence of one type of charge does not establish that every other cost is zero.
Client: "We still need the ongoing ___." | expenses | The case expressly leaves recurring expenses unreviewed, so they remain part of the comparison.
Adviser: "Possible transaction costs also require ___." | verification | Those costs are unknown and need checking before a complete cost claim can be made.
Client: "Then cost-free would be an unsupported ___." | conclusion | The known exit term does not support a conclusion that all charges and expenses are absent.''',
    rehearsal=["Read the corrected comparison. State A's $120 annual and $75 transfer-out fees beside B's $240 annual and zero transfer-out fees, preserving their different services.","Switch roles. Stress that product expenses, account type and tax effects remain unreviewed; do not choose either option.","Read the corrected transfer twice. Keep no exit charge distinct from no ongoing or transaction costs."]))

BOOK['units'].append(unit(
    title='Family, Estate, Beneficiaries, Elder Risk, and Difficult Client Moments', scene='Reviewing beneficiaries after a family loss',
    skill='Explain an account-update process compassionately while distinguishing beneficiary status, trusted contact, and legal authority.',
    brief='After her spouse dies, client Carla asks service colleague Devin how to review beneficiary details. Her daughter is listed as a trusted contact but has no verified transaction authority. Carla wants to remain the decision-maker and asks whether naming her daughter as trusted contact already made her a beneficiary. Devin can explain the firm\'s identity-verified review and update process. Account documents and legal questions have not been reviewed by the assigned specialists. No beneficiary change has been submitted or confirmed.',
    cast='Carla | Client\nDevin | Client-service colleague',
    culture=('Respect grief and preserve the client\'s voice', 'A bereaved client may need a slower pace and a clear sequence. Address the client directly, ask before involving family, and do not infer incapacity from age, grief, or a companion\'s presence. Practical help should preserve privacy and the distinction between administrative support and legal advice.'),
    a='''What role does the daughter currently have in the stated record? | Trusted contact, without verified transaction authority | Confirmed account owner | Automatically the primary beneficiary | Authorized decision-maker for every account | The record identifies a trusted contact, which does not itself confer ownership, beneficiary status, or transaction authority.
What does Carla want preserved? | Her role as decision-maker | An automatic transfer to her daughter | A completed legal opinion from Devin | A change submitted without her confirmation | The briefing expressly states Carla wants to remain the decision-maker while receiving help with the review process.
What is the current change status? | No beneficiary change is submitted or confirmed | The daughter has already inherited | Every account record has been updated | A specialist has approved all legal effects | The request concerns reviewing details; it is not evidence of a submitted, accepted, or effective change.''',
    vocabulary='''beneficiary | A person or entity designated to receive a benefit under relevant terms. | review the named beneficiary
beneficiary designation | A recorded instruction naming benefit recipients under an account or contract. | verify the beneficiary designation
primary beneficiary | A first-priority designated recipient under the relevant terms. | confirm the primary beneficiary
contingent beneficiary | A designated recipient if specified conditions affecting primary recipients apply. | review contingent-beneficiary details
account owner | The person or entity holding ownership rights under the account arrangement. | verify the account owner
joint ownership | Ownership shared under a specified legal form. | clarify the joint-ownership form
estate | A person's property and obligations in the relevant legal context, often after death. | refer estate questions to qualified counsel
will | A legal document directing specified matters after death under applicable law. | review the will with legal counsel
trust | A legal arrangement in which property is held and administered under defined duties and terms. | identify the trust arrangement
trustee | A person or entity administering trust property under the governing duties. | verify the trustee's authority
executor | A person authorized to administer an estate under applicable law and process. | verify executor documentation
power of attorney | An instrument granting specified authority to another person under applicable law. | review the power-of-attorney scope
authorized representative | A person with verified permission or legal authority for a defined role. | confirm the authorized representative
trusted contact | A person the firm may contact in limited circumstances, not automatically authorized to transact. | update trusted-contact information
consent | Permission for a specified action or information use, within applicable requirements. | obtain appropriate client consent
identity verification | Confirmation of a person's identity through the approved process. | complete identity verification
privacy preference | A stated choice about communication or information sharing within applicable limits. | record privacy preferences
capacity concern | A specific concern about decision-making ability requiring appropriate assessment. | escalate a capacity concern respectfully
undue influence | Improper pressure affecting another person's decision under the relevant legal context. | report a concern about undue influence
financial exploitation | Improper use of another person's money or resources under applicable definitions. | escalate suspected financial exploitation
safeguarding | Measures intended to protect a person from harm while respecting rights. | follow the safeguarding process
bereavement | The experience or period following the death of someone close. | offer sensitive bereavement support
case note | A factual record of an interaction and relevant actions. | make an accurate case note
effective change | A change that has taken effect under the applicable process and terms. | confirm an effective change''',
    precision='A trusted-contact designation does not itself make someone a beneficiary or authorize account decisions. Beneficiary, owner, representative, and trusted contact are different roles. Verify the current record and the specific authority rather than relying on a family relationship.',
    precision_extra='A request to review details is not a completed change. Legal effects involving death, divorce, estate documents, ownership, or beneficiary designations depend on the account and applicable law. Explain the service process and route legal questions to qualified review without predicting the result.',
    phrases='''Acknowledge the loss | I am sorry for your loss; we can take this one step at a time.
Preserve the client role | I will address the review and decisions with you.
Clarify the contact | Being your trusted contact does not itself authorize your daughter to transact.
Separate designations | Trusted contact and beneficiary are different account roles.
Start the process | We can verify your identity and review the current account records.
Avoid a status claim | No beneficiary change has been submitted or confirmed yet.
Limit the role | I can explain the update process, but legal effects need qualified review.
Close with confirmation | We will distinguish the request, submission, and confirmed update.
Ask about involvement | Would you like your daughter involved, and what may we discuss with her?
Preserve privacy | We need the appropriate permission before sharing account information.
Verify authority | A family relationship alone does not establish account authority.
Check the record | Let us confirm what each account currently lists.
Avoid a legal shortcut | We should not assume the will changes every beneficiary designation.
State a concern neutrally | I will record the specific observation and follow the safeguarding process.
Respect pacing | We can review the next step without rushing a decision.
Confirm control | This conversation does not transfer control of your account.''',
    notes='''Listed as | Name the role: listed as a trusted contact is not listed as an owner or beneficiary.
Request versus effect | Requested, submitted, accepted, and effective describe different stages that need separate confirmation.
May contact versus may transact | Permission for limited contact does not create authority to move money or decide investments.
Respectful concern | State observed behavior or pressure without diagnosing incapacity from age or grief.
Consent scope | Permission for one conversation does not automatically authorize all future disclosure or transactions.
Legal boundaries | "Needs legal review" identifies the right next assessment rather than offering a guessed estate-law conclusion.''',
    d='''Which explanation accurately separates the daughter's roles? | Trusted-contact status does not itself make her a beneficiary or transaction agent. | Trusted contacts automatically inherit every account. | Family membership gives unrestricted account access. | A trusted contact can sign every instruction without verification. | The trusted-contact role allows limited contact under the relevant arrangements, not automatic beneficiary status or decision authority.
Which response respects Carla's requested control over the review? | Address Carla directly and ask what family involvement she wants and permits. | Copy her daughter on the full account review because she is the trusted contact. | Accept her daughter's confirmation as the beneficiary instruction to reduce Carla's workload. | Send account figures to the daughter first so she can explain them to Carla. | Carla wants to remain the decision-maker. Helpful family involvement still requires appropriate permission and verified authority; trusted-contact status alone does not authorize these disclosures or decisions.
Which status update is supported? | The review is requested; no change is submitted or confirmed. | Every beneficiary has already changed. | The daughter now owns the assets. | The legal effects are fully approved. | The case describes a request for review, not a completed administrative or legal change.
Which issue should Devin route for qualified review? | How the account designation interacts with estate documents and applicable law | Where to find the approved update form | Whether identity verification is required by the process | How to check a submission's administrative status | The interaction of account terms and estate law exceeds a service explanation and requires the assigned qualified assessment.''',
    dialogue='''Carla | Since my spouse died, I have been trying to review the paperwork. My daughter is a trusted contact; does that mean she is already the beneficiary?
Devin | I am sorry for your loss. A [[trusted contact::A trusted contact may be contacted in limited circumstances; that designation does not itself name a beneficiary or authorize transactions.]] has a different role. We can check each account's beneficiary record without assuming the contact designation changes it.
Carla | I want her to help me organize things, but I still want to make the decisions. I do not want the account treated as hers.
Devin | You remain the person we address for your decisions. We will verify any [[authority::Authority must be established for the particular action; a family relationship or contact listing does not confer control of the account.]] separately rather than infer it from her family relationship or her presence.
Carla | Where do we begin? There may be more than one account, and I do not know whether each one has the same information on file.
Devin | Begin with the approved [[identity verification::Identity verification establishes the person requesting access through the approved process before current account details are reviewed.]] process, then review the relevant records. We should confirm what each account lists instead of assuming all designations are identical.
Carla | Once we have the record, I can see whether I want to request an update. Asking today does not itself change the names, correct?
Devin | Correct. Reviewing a [[beneficiary designation::A beneficiary designation records benefit recipients under the relevant terms; inspecting it is not the same as changing it.]] is different from submitting a change. No update has been submitted or confirmed through this conversation.
Carla | My daughter may join the next call. I would like her help, but there are some financial details I prefer to discuss privately with you.
Devin | We can record your [[privacy preferences::Privacy preferences identify the client's communication choices; family involvement does not automatically permit unrestricted information sharing.]] and obtain the appropriate permissions. We will clarify what may be shared rather than assume joining one call grants unrestricted access.
Carla | My will names my daughter too. I assumed that settled everything. Do I still need to check each account's beneficiary record separately?
Devin | That interaction needs [[legal review::Legal review assesses the interaction of account terms, estate documents, and applicable law; a service colleague should not assume a universal outcome.]]. I can explain our record-update process, but I should not guess the legal effect of the will or other documents.
Carla | If my daughter were given a power of attorney later, would that be the same thing as being a trusted contact now?
Devin | No. A [[power of attorney::A power of attorney can grant specified legal authority subject to its terms and law; it is distinct from trusted-contact status.]] is a separate instrument with defined authority and requirements. Its validity, scope, and treatment would need verification under the applicable process.
Carla | I appreciate that. I may need more time with the forms because there is a lot to manage, but I do not want needing time mistaken for being unable to decide.
Devin | We can work at a reasonable pace. A [[capacity concern::A capacity concern requires specific observations and appropriate assessment; needing time or grieving does not by itself establish incapacity.]] should not be inferred from grief or a slower review. Your questions and preferences should remain central.
Carla | Suppose someone pressures me to make a change I do not want. I would want a way to tell the firm without having to discuss everything in front of them.
Devin | We can explain the firm's [[safeguarding::Safeguarding provides a process for concerns about harm or pressure while respecting the client's rights and role.]] and reporting routes. A specific concern should be handled through the appropriate process, with information shared only as permitted or required.
Carla | First help me see what is currently recorded. I want to speak with the legal specialist before requesting changes; there is already a lot to manage.
Devin | I will make that clear in the [[case note::A case note records the client's actual request and limits; it must not convert a review inquiry into a beneficiary-change instruction.]]. We will distinguish review, any later instruction, submission, and confirmation so you know what has and has not happened.''',
    transfer_title='A relative asks for the balance',
    transfer_setup='A caller says they are the account holder\'s son and asks for the balance. His identity and authority to receive account information are unverified. No disclosure permission is established.',
    transfer='''Colleague: "A family relationship does not establish disclosure ___." | authority | Being a relative does not by itself verify permission or legal power to receive private account information.
Caller: "You need to complete the appropriate identity and permission ___." | checks | The case leaves identity and authorization unverified, so the approved checks must precede disclosure.
Colleague: "Until then, I cannot share the account ___." | balance | The balance is private account information and no basis for disclosing it to this caller is established.
Caller: "Please explain the approved verification ___." | process | A service colleague can explain the route for establishing permission without revealing the protected information.''',
    rehearsal=["Read Carla and Devin's corrected exchange. Keep Carla as decision-maker and her daughter as trusted contact without assumed beneficiary or transaction authority.","Switch roles. Distinguish a requested review from a submitted or effective change; retain the specific permission needed for family involvement.","Read the corrected caller transfer. Explain verification while withholding the balance until identity and disclosure authority are established."]))

BOOK['units'].append(unit(
    title='Practice Management, Documentation, Complaints, Marketing, and Supervision', scene='An acknowledgment that never answered the complaint',
    skill='Restate a specific complaint, explain investigation status, and commit only to an authorized next step.',
    brief='Client Dana complained that two $300 entries appeared with similar fee descriptions. The firm sent an acknowledgment and ticket number but did not answer why the two entries were posted. Liam, the service lead, has the complaint and statement references but no completed review of the entries. The assigned complaints team will assess the issue. A status update is scheduled for Friday, not a guaranteed final decision. No duplicate-charge finding or refund has been approved.',
    cast='Dana | Client\nLiam | Service lead',
    culture=('An apology needs a concrete response', 'A polite acknowledgment can frustrate a client if it replaces the answer they requested. State the specific concern, the current evidence, the responsible team, and the next update. Do not promise a refund or final date merely to end an uncomfortable conversation.'),
    a='''What question remains unanswered? | Why two similarly described $300 entries were posted | Whether a ticket number was issued | Whether the acknowledgment arrived | Whether Dana ever raised a concern | The firm acknowledged receipt but has not explained the two entries that prompted the complaint.
What is scheduled for Friday? | A status update | A guaranteed refund | A final legal ruling | Automatic closure regardless of findings | Friday is an update point only; the case expressly does not guarantee a final decision then.
What conclusion has been approved? | Neither a duplicate-charge finding nor a refund | A confirmed duplicate and full refund | A finding that Dana is mistaken | A closed complaint with no remaining issue | The entry review is incomplete, so neither the cause nor the remedy has been approved.''',
    vocabulary='''complaint | An expression of dissatisfaction requiring handling under the applicable process. | record a client complaint
acknowledgment | Confirmation that a message or concern has been received. | send an acknowledgment
substantive response | A reply addressing the actual issue rather than only confirming receipt. | provide a substantive response
complaint owner | The person or team responsible for progressing the complaint. | identify the complaint owner
case reference | An identifier used to track an issue and related records. | quote the case reference
investigation status | The current stage of evidence review and assessment. | explain the investigation status
service failure | A shortcoming in the service provided, where established. | assess a reported service failure
resolution | An outcome addressing a matter under the applicable process. | explain the complaint resolution
remedy | An action intended to address an established problem under relevant authority. | consider an authorized remedy
refund | Repayment of an amount charged or paid under the applicable decision. | confirm an approved refund
escalation | Referral to a responsible authority for further attention. | route a complaint escalation
response deadline | A time by which a specified reply is required or planned. | distinguish update and response deadlines
record retention | Keeping records for the period and purpose required by applicable arrangements. | follow record-retention requirements
correspondence log | A record of communications and their dates or status. | update the correspondence log
supervisory review | Oversight assessment by an authorized reviewer. | obtain supervisory review
approval workflow | A defined process for obtaining required authorization. | follow the approval workflow
advertisement | A promotional communication under the relevant rules and context. | review an advertisement before use
testimonial | A statement about experience with a provider under applicable definitions. | assess a proposed testimonial
endorsement | A statement of support or recommendation under applicable definitions. | review an endorsement disclosure
hypothetical performance | Results not representing the actual performance experience described for a real portfolio. | qualify hypothetical performance
cherry-picking | Selecting favorable information while omitting relevant unfavorable context. | avoid cherry-picking results
substantiation | Evidence supporting a factual or promotional claim. | retain claim substantiation
misleading omission | Missing information that materially distorts the message in context. | correct a misleading omission
version control | Management of document versions and their approval status. | maintain approved-version control''',
    precision='An acknowledgment establishes receipt, not investigation completion or resolution. Similar fee labels are a reason to examine the entries, not proof that the second charge is a duplicate. The Friday commitment is a status update, not a guaranteed refund or final decision.',
    precision_extra='Complaint handling, records, response requirements, and marketing communications follow applicable law and firm procedures. A useful service message preserves the client\'s specific concern and actual status. It should neither erase the complaint nor invent a conclusion to make the record look closed.',
    phrases='''Acknowledge the gap | Our earlier message confirmed receipt but did not answer your question.
Restate the concern | You want to know why two $300 entries have similar fee descriptions.
State the evidence | We have the statement references, but the entry review is incomplete.
Name the owner | The assigned complaints team is responsible for the assessment.
Limit the commitment | Friday is the scheduled status update, not a promised final decision.
Avoid a premature remedy | No refund decision has been approved yet.
Preserve the record | I will keep your original concern and the correspondence linked to the case.
Close with substance | The next update will say what has been checked and what remains open.
Avoid a finding | Similar descriptions do not yet establish a duplicate charge.
Take responsibility | I will make sure the unanswered question is explicit in the handoff.
Check accuracy | Does this restatement capture the issue you want addressed?
Confirm delivery | Which approved communication route should we use for the update?
Avoid forced closure | An acknowledgment alone is not a reason to mark the complaint resolved.
Preserve an escalation | I will explain the applicable escalation route without implying an outcome.
Limit a marketing claim | A favorable comment cannot be published without the required review and permissions.
Keep the version | Use only the currently approved communication, with its qualifications intact.''',
    notes='''Received versus resolved | These status words mark different stages; changing one to the other without evidence misstates progress.
Why questions | Answer the specific explanation request rather than replacing it with an unrelated reassurance.
Update versus decision | State whether a date concerns progress reporting or an actual completed determination.
No decision yet | This phrase communicates status without promising either approval or rejection.
Apology precision | Acknowledge the communication shortcoming without inventing a concluded cause for the underlying charge.
Record fidelity | Preserve the client's concern and corrections rather than rewriting the history to match a preferred outcome.''',
    d='''Which opening addresses the actual communication failure? | Our acknowledgment did not explain the two entries; that question remains open. | We sent a ticket number, so the issue is resolved. | Similar labels prove a refund is due. | A polite greeting is the same as an investigation. | The correct opening names the unanswered question and distinguishes receipt from a substantive response.
Which Friday promise is supported? | We will provide the scheduled status update. | Your refund is guaranteed Friday. | The final finding will certainly be complete Friday. | Every record will be deleted Friday. | The case authorizes a progress update, not a guaranteed remedy, final determination, or record deletion.
Which statement matches the evidence on the charges? | The similar descriptions need review; a duplicate is not established. | The second entry is definitely fraudulent. | Two identical amounts can never be legitimate. | The complaint proves the exact cause. | Similar descriptions and amounts justify checking but do not by themselves determine the underlying transactions.
Which handoff best preserves the complaint? | Include the two entry references, unanswered fee question, pending review, owner and Friday update. | Record a request for another statement without the disputed entries. | Record the ticket number and mark the communication task complete. | Record an expected $300 refund as the planned Friday outcome. | The handoff must carry the substantive issue, evidence and real status to the complaints team. A statement request or ticket alone loses the question; an expected refund invents a decision.''',
    dialogue='''Dana | Your email gave me a ticket number, but it did not answer my question. Why are there two three-hundred-dollar entries with almost the same fee description?
Liam | You are right that the [[acknowledgment::An acknowledgment confirms receipt; it does not explain the entries or establish that the complaint has been resolved.]] did not answer that question. I will make the unresolved issue explicit rather than treating the earlier email as a completed response.
Dana | I need an explanation of the entries, not another message saying the firm values me. Was one charged incorrectly?
Liam | That requires a [[substantive response::A substantive response addresses the actual complaint and evidence, rather than offering another receipt confirmation or general reassurance.]]. We have the statement references, but the review of the entries is incomplete, so I cannot responsibly give you an unverified explanation.
Dana | The similar labels look like a duplicate to me. Can you confirm that now, or do you still need to inspect the transaction and fee records?
Liam | The [[duplicate-charge finding::A duplicate-charge finding would conclude that an amount was improperly repeated; similar descriptions alone do not establish that result.]] is not established yet. We need the underlying records to identify each entry and assess whether either was charged incorrectly.
Dana | Who is responsible? I have spoken to several people, and I do not want the question passed around without an owner.
Liam | The assigned complaints team is the [[complaint owner::The complaint owner is responsible for progressing the assessment; naming that role makes the handoff accountable rather than vague.]]. I will link your original concern, the statement references, and this conversation so the team receives the specific unresolved question.
Dana | The email mentioned Friday. Does that mean you will tell me the final answer then, or only that someone is still looking at it?
Liam | Friday is the scheduled [[status update::A status update reports progress and open work; the case does not authorize promising a final decision on that date.]], not a guaranteed final decision. It should identify what has been checked, what remains open, and the next authorized step.
Dana | If the review confirms an error, I would expect the firm to explain how it will put things right. Can you promise the refund today?
Liam | No [[refund::A refund is a repayment requiring the applicable decision; the incomplete review does not support promising one now.]] has been approved. I can ensure that your requested remedy is recorded, but I should not promise an outcome before the assessment and required approval.
Dana | Please do not remove the earlier messages. They show that I asked this question before and that the response did not address it.
Liam | We will preserve the [[correspondence log::The correspondence log retains communications and their sequence, helping the review trace the original concern and the response gap.]] under the applicable record process. Your original concern and the fact that it remains unanswered should stay visible in the file.
Dana | I also want to know how to escalate if the next response is another acknowledgment. I am not withdrawing my complaint by agreeing to wait for Friday.
Liam | I will explain the relevant [[escalation::Escalation routes the concern for further attention through the applicable process; accepting an update date does not withdraw the complaint.]] route. Waiting for a scheduled update does not, by itself, mean you consider the matter resolved or waive your concern.
Dana | Could you read back the issue you are sending to the reviewer? The two entries are my main concern, not just the unhelpful email.
Liam | You seek an explanation and review of two similarly described three-hundred-dollar entries, with any appropriate remedy assessed. That will be in the [[handoff::The handoff preserves the substantive fee question and requested assessment, rather than reducing the complaint to general dissatisfaction with service tone.]], alongside the communication shortcoming.
Dana | Yes, that is the question. Please use our usual contact route and update me when promised, even if you are still waiting for the final answer.
Liam | I will record that request. The case stays open pending the proper [[resolution::Resolution requires an outcome addressing the complaint through the applicable process; sending another email alone does not complete it.]], and the next message will distinguish verified findings, unfinished work, and any decision actually approved.''',
    transfer_title='A client comment is not an approved advertisement',
    transfer_setup='A client sends a favorable private email. A colleague proposes quoting it in a public advertisement. Required permission, disclosure, and supervisory checks have not been completed.',
    transfer='''Colleague: "The private comment is not yet approved for public ___." | use | A favorable private message does not itself authorize publication in a promotional communication.
Supervisor: "Verify the required permission and any relevant ___." | disclosures | Publication may require permission and material information under the applicable rules and process.
Colleague: "The proposed advertisement still needs supervisory ___." | review | The case expressly leaves the required oversight assessment incomplete.
Supervisor: "Keep the draft separate from the approved ___." | version | Version control prevents an unreviewed promotional draft from being mistaken for an authorized communication.''',
    rehearsal=["Read Dana and Liam's corrected complaint conversation. Name the two $300 entries and the unanswered question; similar descriptions do not establish duplication.","Switch roles. Commit to Friday's status update without promising a final decision or refund. Keep the complaint open for assessment.","Read the corrected advertisement transfer twice. Preserve permission, disclosure and supervisory checks before any proposed public use."]))
