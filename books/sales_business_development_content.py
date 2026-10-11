"""Original sales and business development cases for the learner-book series."""
from books.authoring import unit

BOOK = dict(
    slug='sales-business-development', title='Sales and Business Development English',
    cover_label='ENGLISH FOR CUSTOMER CONVERSATIONS',
    cover_title='Sales and Business\nDevelopment', cover_size=31,
    tagline='Understand the need.\nEarn the next step.',
    audience='For sales representatives, account executives, business development teams, sales engineers, channel managers, and commercial leaders.',
    map_intro='Eight commercial conversations: discover a real need, connect capability to an outcome, compare competing offers, handle a discount request, map buying roles, route contract changes, define a partnership proposal, and correct an unsupported forecast.',
    notes_title='Persuasive language. Reliable commitments.',
    notes_intro='Good sales English makes a customer problem and the next decision clear. These conversations practice relevant questions, credible value claims, fair comparisons, bounded negotiation, and accurate internal reporting. A positive response is useful information, but it is not the same as budget, approval, or a signed order.',
    field_notes=[
        ('Make discovery useful to the customer', 'Explain why a question matters and connect the answer to a relevant demonstration or next step. Qualification should clarify mutual fit, not feel like an interrogation or a script that ignores the reply.', '"May I understand the approval workflow so the demonstration focuses on the part that slows your team down?"'),
        ('Separate capability from achieved value', 'A feature may support an outcome, but the customer result depends on workflow, data, adoption, and other conditions. State what is demonstrated, what is estimated, and what still needs testing.', '"The tool can consolidate the inputs; the time saving in your reporting cycle still needs validation."'),
        ('Negotiate within actual authority', 'A request can be discussed without being accepted. Confirm the exact scope, terms, and approval route before promising a discount, contract amendment, or exclusive right.', '"I can submit the fifteen-percent request, but I cannot approve that reduction myself."'),
        ('Record customer evidence, not sales hopes', 'Keep the contact, budget holder, procurement steps, and signature status distinct. A target date entered internally should not become a customer-confirmed commitment in the forecast.', '"The proposed close date is our estimate; procurement has not started and the customer has not confirmed it."'),
    ],
    scope_note='All customers, products, people, quotes, contracts, prices, policies, and timelines are fictional. This book teaches professional English, not legal, financial, procurement, or product advice. Follow the actual evidence, approved claims, commercial authority, and contract-review process. FTC references concern United States advertising guidance; they are not a complete statement of applicable law. No cited organization endorses this book.',
    sources=[
        dict(title='Salesforce. What is a Sales Pipeline? And How Do You Build One? (2025).', url='https://www.salesforce.com/sales/pipeline/', note='Background terminology for qualification, customer progress, and pipeline records. Stage names and approval rules in the exercises are fictional.', checked='1 October 2026'),
        dict(title='MEDDICC. MEDDIC / MEDDPICC sales methodology and process.', url='https://meddicc.com/meddpicc-sales-methodology-and-process', note='Background for commonly heard buying-role and decision-process terms. The book is not framework certification or a reproduction of proprietary training.', checked='1 October 2026'),
        dict(title='Federal Trade Commission. Advertising FAQs: A Guide for Small Business.', url='https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business', note='United States background on substantiated, nonmisleading claims. Fictional value and comparison exercises do not determine legal compliance for real advertising.', checked='1 October 2026'),
        dict(title='Cornell Legal Information Institute. Wex: Contract.', url='https://www.law.cornell.edu/wex/contract', note='Background on agreements and differing legal contexts. Contract dialogue practices routing and authority, not enforceability analysis or advice on accepting clauses.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Discovery and Qualification',
    scene='Make the demonstration relevant before opening the slides',
    skill='Clarify the workflow, problem, and buying steps without turning a demonstration request into a purchase commitment.',
    brief='Prospect Nina requests a demonstration of an approval-workflow product. Her four branch teams handle about 600 purchase requests per month through spreadsheets and email. She says managers spend time chasing status, but waiting time and the cost of the problem have not been measured. Nina coordinates operations and has not identified the budget holder, approved budget, or purchasing process. Sales representative Caleb must agree a focused demonstration objective and useful discovery steps. Product fit, savings, purchase authority, and a close date are not yet established.',
    cast='Nina | Prospect operations coordinator\nCaleb | Sales representative',
    culture=('Ask with a reason, then listen', 'A prospect may want to see the product before answering a long list of commercial questions. Explain which few details will make the demonstration relevant and offer a focused agenda. Avoid making unknown budget information sound like a personal failure or treating curiosity as a commitment to buy.'),
    a='''What current workflow is described? | About 600 monthly purchase requests across four branches using spreadsheets and email | A fully measured automated process | A signed order for the new product | A single branch handling six requests annually | The brief specifies the volume, branch count, and existing tools without establishing product fit.
What is known about the problem? | Managers chase status, but waiting time and cost have not been measured. | Every request waits exactly ten days. | The product has already eliminated the delay. | The customer has approved a savings figure. | Nina reports a practical problem, while its time and financial effects remain unmeasured.
What does the demonstration request establish? | Interest in seeing the product, not purchase approval | Confirmed budget and signing authority | A guaranteed close date | Completion of procurement | A request to see the product is evidence of interest, not the missing commercial approvals.''',
    vocabulary='''discovery call | A conversation to understand a prospect's situation and needs. | conduct a discovery call
qualification | Assessment of whether a sales opportunity has relevant fit and buying conditions. | complete opportunity qualification
prospect | A potential customer being considered or engaged. | understand the prospect
lead | A potential customer contact or indication of interest under the team's definitions. | follow up a lead
use case | A specific situation in which a capability would be used. | define the use case
current-state workflow | The sequence of work as it operates now. | map the current-state workflow
pain point | A practical problem or difficulty relevant to the customer. | clarify the pain point
business impact | The effect of a problem or change on the organization. | quantify business impact
discovery gap | Information still missing from understanding the opportunity. | identify a discovery gap
ICP | Ideal customer profile; characteristics used to describe a suitable target organization. | define the ICP
BANT | Budget, authority, need, and timing; a commonly used qualification checklist. | use BANT questions
budget holder | The person or function controlling the relevant funding. | identify the budget holder
buying process | The customer's steps for evaluating and authorizing a purchase. | clarify the buying process
decision-maker | A person with authority over a relevant purchase decision. | identify the decision-maker
end user | A person who will use the product or service. | involve end users
technical evaluator | A person assessing relevant technical suitability. | engage the technical evaluator
demonstration | A showing of specified product capabilities. | tailor the demonstration
demo objective | The question or capability the demonstration should address. | agree the demo objective
discovery agenda | The planned topics for the initial needs conversation. | agree a discovery agenda
baseline measure | A defined current value used to assess a proposed change. | establish a baseline measure
compelling event | A customer-relevant event creating a genuine reason for timing. | verify the compelling event
next step | A specific agreed action moving the conversation forward. | agree the next step
mutual action plan | A shared sequence of customer and seller actions with owners and dates. | develop a mutual action plan
solution fit | How well a proposed offering meets the relevant need and constraints. | validate solution fit''',
    precision='About 600 requests per month describes volume, not delay or savings. Managers chasing status identifies a problem worth examining, but neither the waiting-time baseline nor the cost is supplied. Do not turn those unknowns into a quantified benefit or a guaranteed product result.',
    precision_extra='Unknown budget is different from confirmed absence of budget. An enthusiastic operations contact is different from a budget holder or authorized signer. Ask how the relevant decisions are made, and record what remains unknown without inventing either approval or rejection.',
    phrases='''Respect the request | We can show the product; first, may I clarify what would make the demonstration useful?
Ask about the workflow | How does a purchase request move through approval today?
Reflect the current process | Four branches handle about six hundred requests a month through spreadsheets and email.
Clarify the problem | Where do managers lose visibility or need to chase an update?
Avoid a leading conclusion | Is the delay in approval, information gathering, or another step?
Ask about measurement | Do you have a measured waiting-time baseline?
Separate report and estimate | The status-chasing problem is reported; its cost is not yet quantified.
Define the demonstration | Let us focus on routing requests and seeing their current status.
Keep fit provisional | We still need to test whether the workflow fits your requirements.
Clarify the role | Which parts of the evaluation do you coordinate?
Ask about authority respectfully | Who controls the relevant budget and approves a purchase?
Avoid assuming no budget | We have not confirmed the budget position yet.
Understand timing | Is there a customer deadline driving the evaluation?
Avoid a close-date promise | A demonstration does not establish a purchase date.
Agree a useful follow-up | After the demonstration, we can review the fit and remaining questions together.
Close discovery | I will summarize the objective, participants, known facts, and open questions.''',
    notes='''May I clarify | Requests cooperation and explains why discovery precedes the demonstration.
About | Preserves the approximate nature of the monthly volume.
Where | Seeks the actual problem location without supplying the answer.
Not yet quantified | Keeps an observed problem distinct from an invented financial result.
Which parts | Clarifies the contact role without challenging personal status.
Open questions | Records uncertainty as work to resolve, not as an assumed refusal.''',
    d='''Which demonstration objective fits the stated need? | Show request routing and status visibility in a relevant workflow. | Prove an unmeasured 80% saving. | Display every feature without reference to the process. | Ask Nina to sign before explaining the product. | Routing and status visibility connect directly to the reported workflow and status-chasing problem.
Which statement about budget is accurate? | The budget position has not yet been confirmed. | No budget exists because Nina did not name it. | The request for a demonstration approves the budget. | The seller can choose the customer's budget holder. | Missing budget information remains unknown rather than proving either available funding or its absence.
Which question clarifies the buying process? | Who evaluates the fit, controls funding, and authorizes the purchase? | Which features should we show in the first ten minutes? | How many requests does each branch process? | Which spreadsheet columns identify the next approver? | All four questions can be useful, but only the first establishes the roles involved in evaluating and authorizing the purchase; the others concern demonstration or workflow discovery.
Which benefit statement is supportable now? | We can examine whether status visibility addresses the problem; savings still need measurement. | The product will save exactly half the team's time. | Six hundred requests means six hundred hours saved. | Every spreadsheet workflow is automatically unsuitable. | The current facts support exploring fit, not a quantified or guaranteed improvement.''',
    dialogue='''Nina | Can you show us the approval workflow? My managers keep chasing requests through email, and I want to see whether your product makes the status clearer.
Caleb | Certainly. May I clarify the [[demo objective::The objective links the demonstration to the customer's workflow question rather than an unfocused tour of features.]] first so we show the part that matters to your team? A little context will help us focus the session.
Nina | Four branches handle about six hundred purchase requests a month. People send spreadsheets around and then chase updates by email.
Caleb | That gives us the [[current-state workflow::The current-state workflow describes how requests move now, providing context for a relevant product demonstration.]]. Where does visibility break down: when a request is submitted, while it is awaiting approval, or when someone needs more information?
Nina | I cannot say which step accounts for most of the delay. I know managers spend time asking for status, but we have not measured the waiting time.
Caleb | Then the [[pain point::The pain point is status chasing; the location and measured size of the delay remain to be established.]] is clear enough to explore, while the size and location of the delay remain open. We should not attach a savings figure before understanding those details.
Nina | We could ask the branch leads for examples of the handoffs. I do not want to send sensitive purchasing records just to arrange a demonstration.
Caleb | Agreed. We can start with an appropriate process description and a [[baseline measure::A baseline measure establishes current performance; request volume alone does not quantify waiting time or savings.]] if one is available. Use the approved information-sharing arrangements, and do not send personal or confidential records that we do not need.
Nina | For the demonstration, I mainly want to see how a manager finds the status and knows whose action is next.
Caleb | That is a focused [[use case::The use case is routing and status visibility in the approval workflow, not every capability the product offers.]]. We can show request routing and status visibility, then ask whether the example reflects your actual requirements instead of walking through every available feature.
Nina | I coordinate the operational evaluation. I have not yet involved the people who would assess the system or approve the purchase.
Caleb | Let us clarify the [[buying process::The buying process identifies evaluation and approval steps that Nina's demonstration request does not establish.]] without assuming your role covers every decision. Who would evaluate technical fit, control funding, and authorize a purchase if the product proves relevant?
Nina | I need to confirm that internally. I do not have an approved budget figure to give you today.
Caleb | That remains a [[discovery gap::A discovery gap is missing information, not proof that funding is either approved or unavailable.]], not proof that there is no budget. We can record the position accurately and agree how to identify the relevant people rather than fill in assumptions.
Nina | Just so we are clear, this is an evaluation. I have not promised anyone we will buy this month, and I do not have a purchase date.
Caleb | Understood. We should not invent a [[compelling event::A compelling event is a genuine customer timing driver, not a seller-created date inferred from interest.]] or treat the demonstration as a closing commitment. We can ask about genuine operational deadlines when you have that information.
Nina | After the demonstration, I would like the branch leads to help identify what fits and what would need further examination.
Caleb | That is how we can evaluate [[solution fit::Solution fit needs assessment against actual requirements; a successful demonstration alone does not establish it.]]. We should capture both useful capabilities and unresolved requirements, including anything that the demonstration does not establish about your environment.
Nina | Please send a short agenda with the workflow focus and the questions we should bring to that follow-up.
Caleb | I will summarize the agreed [[next step::The next step is a focused agenda and follow-up, not an invented purchase approval or close date.]], participants, known facts, and open questions. That will make the demonstration useful without turning your interest into a commitment you have not made.''',
    rehearsal=('Read Nina and Caleb aloud, then swap roles. Ask for context without making the demonstration conditional on immediate budget answers.', 'Check all ten gaps. Reread the measured-baseline and buying-role exchanges without inventing missing information.', 'Repeat the agreed demonstration agenda and follow-up, keeping product interest distinct from a purchase commitment.'),
    transfer_title='Qualify another demonstration request',
    transfer_setup='An operations contact asks to see a scheduling product. Three sites currently coordinate by email. Missed updates are reported, but their frequency, budget, approver, and purchase date are unconfirmed.',
    transfer='''Seller: "The existing coordination tool is ___." | email | The brief identifies email as the current method across the three sites.
Contact: "The reported problem is ___." | missed updates | Missed updates are reported, but their frequency and impact have not been measured.
Seller: "The relevant number of sites is ___." | three | Three sites define the stated operational footprint for this initial discussion.
Contact: "The purchase date is ___." | unconfirmed | A request to see the product does not establish a buying commitment or date.''',
))


BOOK['units'].append(unit(
    title='Value Proposition and Use-Case Fit',
    scene='Connect the feature to the reporting work it might change',
    skill='Connect a capability to a testable benefit, with a baseline and a distinction between capacity and cash savings.',
    brief='Evan spends 24 staff hours preparing each monthly report: 14 consolidating inputs, 8 reviewing them, and 2 formatting the output. Sales representative Sera demonstrates automated consolidation using sample data. Evan proposes testing whether consolidation could fall from 14 to 6 hours while review and formatting remain unchanged. That would reduce total preparation to 16 hours, freeing 8 hours per cycle. No customer-data test has occurred, compatibility is unverified, and no staffing cost reduction is planned. Sera must describe a value hypothesis, not guaranteed savings or a proven return on investment.',
    cast='Evan | Prospect reporting lead\nSera | Sales representative',
    culture=('The customer outcome comes before the feature tour', 'A technically impressive feature may not answer the concern of the person buying it. Ask which work changes, what remains, and how the result will be checked. A credible explanation of limits can be more persuasive than a long list of capabilities detached from the customer workflow.'),
    a='''How is the current 24-hour cycle divided? | 14 hours consolidation, 8 review, and 2 formatting | 24 hours consolidation only | 6 hours review and 18 formatting | 8 hours total preparation | The three supplied work categories sum to twenty-four staff hours per monthly cycle.
What total follows from the proposed test assumption? | 16 hours, if consolidation falls to 6 and the other tasks stay unchanged | 6 hours for the entire report | Zero preparation time | A proven total of 14 hours | Six consolidation hours plus eight review and two formatting hours would total sixteen.
What has actually been demonstrated? | Consolidation with sample data, not verified customer results | A completed customer-data test | A guaranteed eight-hour saving | A planned reduction in staffing cost | The demonstration shows a capability on sample data, while customer fit and benefits remain unverified.''',
    vocabulary='''value proposition | A clear explanation of the relevant benefit an offering is proposed to provide. | tailor the value proposition
feature | A specific capability or characteristic of a product. | demonstrate a feature
feature-to-value link | The explanation connecting a capability to a customer outcome. | explain the feature-to-value link
value hypothesis | A proposed customer benefit to be tested against evidence. | validate the value hypothesis
business outcome | A result meaningful to the customer's operation or goals. | define the business outcome
quantified benefit | A proposed or observed improvement expressed in a defined measure. | substantiate a quantified benefit
business case | An assessment of expected value, costs, conditions, and risks for a decision. | build the business case
proof of value | A bounded evaluation of whether a solution produces a relevant customer benefit. | agree a proof of value
time-to-value | The period before a defined benefit is achieved. | estimate time-to-value
value realization | Actual achievement of the intended benefit. | track value realization
workflow fit | Compatibility between the solution and the customer's actual work. | test workflow fit
manual consolidation | Combining information through human effort rather than the proposed automation. | reduce manual consolidation
data readiness | Whether data meets the conditions needed for the proposed use. | assess data readiness
compatibility | Ability of components or data to work together as required. | verify compatibility
configuration | Settings or arrangements used to adapt a product to the required use. | confirm the configuration
integration | Connection between systems or processes to support the intended workflow. | scope the integration
exception handling | Work to address items that do not follow the normal path. | assess exception handling
representative dataset | Data selected to reflect the relevant real-world conditions for a test. | use a representative dataset
acceptance criterion | A defined condition for judging the agreed test or output. | set acceptance criteria
benefit owner | The person responsible for confirming and tracking a particular benefit. | identify the benefit owner
baseline | The defined current position used for comparison. | confirm the baseline
labor capacity | Staff time or capability available for work. | release labor capacity
cash saving | A reduction in actual cash expenditure under a specified comparison. | distinguish cash savings
assumption | A condition taken as true for a calculation until verified. | disclose the assumptions''',
    precision='Under the proposed assumption, consolidation falls by 8 hours, and total preparation falls from 24 to 16. The total time reduction would be 8 divided by 24, approximately 33.3%. The demonstration has not established that this reduction will occur in the customer workflow.',
    precision_extra='Freed staff time is potential capacity, not automatically lower payroll or cash expenditure. No staffing cost reduction is planned here. A return-on-investment calculation would also need relevant costs, timing, and a justified benefit measure that the brief does not supply.',
    phrases='''Start with the workflow | Which part of preparing the report consumes the most time?
State the baseline | The current cycle takes twenty-four staff hours.
Link the capability | Automated consolidation addresses the fourteen-hour input-combining step.
Keep other work visible | Review and formatting do not disappear in this proposal.
State the hypothesis | We would test whether consolidation can fall to six hours.
Calculate conditionally | If the other tasks stay unchanged, total preparation would be sixteen hours.
Name the potential capacity | That would free eight staff hours per monthly cycle.
Avoid a guaranteed claim | The customer-data test has not yet established that saving.
Separate demonstration and proof | Sample-data performance does not confirm compatibility with your inputs.
Define a useful test | Use an approved representative dataset and agreed success criteria.
Check exceptions | Include the unusual inputs that currently require manual attention.
Assign benefit ownership | Who will verify the before-and-after time measurement?
Distinguish value types | Released capacity is not automatically a cash saving.
Avoid invented return | We cannot state a return on investment without the relevant costs and benefit assumptions.
State the implementation dependency | Configuration and integration requirements still need assessment.
Close the value discussion | Let us agree what to test, how to measure it, and what the result would establish.''',
    notes='''Addresses | Links a feature to a particular work step without claiming every task disappears.
Would test | Marks the benefit as a hypothesis.
If | Makes the calculation conditional on the stated assumptions.
Per monthly cycle | Keeps the time-saving unit explicit.
Not automatically | Separates released time from a reduction in expenditure.
What the result would establish | Defines the claim that a bounded test could legitimately support.''',
    d='''Which value claim is accurate before the customer-data test? | The proposed change could free eight hours per cycle if the stated assumptions hold. | The product has already cut all reporting time by two thirds. | Eight staff hours guarantees eight hours less payroll cost. | The demonstration proves every customer format is compatible. | The conditional claim follows the supplied arithmetic while preserving the unverified customer result.
Why is the proposed total sixteen rather than six hours? | Review and formatting still require ten hours combined. | Consolidation is counted twice. | The baseline was six hours. | The customer has removed all review steps. | The six-hour consolidation assumption must be added to eight review hours and two formatting hours.
What should a relevant proof of value include? | Approved representative inputs, exceptions, measures, and agreed criteria | The clean demonstration file and the seller's processing time alone | Real customer inputs, but no record of time spent correcting exceptions | A satisfaction survey without comparing the defined reporting task | A meaningful test needs representative work and agreed measures. Easy samples, omitted correction time, and satisfaction alone cannot establish the claimed reduction in the customer's full reporting cycle.
Which distinction matters for the business case? | Freed staff capacity does not necessarily reduce cash spending. | Every saved minute immediately reduces the invoice. | Staff time has no possible value. | Product cost is irrelevant to any return calculation. | Capacity can be useful without producing a cash reduction, so the benefit measure must be stated accurately.''',
    dialogue='''Evan | I can see the features. What I cannot yet see is which part of our monthly reporting they would shorten. Can we walk through that?
Sera | Let us connect the [[value proposition::The value proposition should address the customer's reporting outcome, rather than merely list product capabilities.]] to that work. Which steps make up the current preparation time, and which one causes the largest amount of manual effort?
Evan | We spend twenty-four staff hours per cycle: fourteen consolidating inputs, eight reviewing them, and two formatting the output.
Sera | That is a useful [[baseline::The baseline is the current twenty-four-hour cycle, with the three work categories separately defined.]]. Automated consolidation relates to the fourteen-hour step. It does not mean the eight hours of review or two hours of formatting would disappear.
Evan | If consolidation could fall to six hours, the change would be useful. We could use the freed time for more analysis.
Sera | That gives us a [[value hypothesis::The proposed six-hour consolidation result is a benefit hypothesis to test, not an achieved customer outcome.]] to test. With review and formatting unchanged, the total would fall to sixteen hours, freeing eight hours per cycle. We have not yet demonstrated that result with your inputs.
Evan | The example you showed worked quickly, but our files vary by branch and sometimes contain exceptions that require manual correction.
Sera | Then [[workflow fit::Workflow fit depends on the real inputs and exceptions, which a smooth sample demonstration does not establish.]] remains to be checked. Sample-data performance does not establish compatibility with every branch format or remove the exception handling your team currently performs.
Evan | We would need an evaluation that includes those awkward inputs, not only the clean examples that are easy to automate.
Sera | Use an approved [[representative dataset::Representative data should reflect relevant branch formats and exceptions, rather than only easy records selected for a demonstration.]] with appropriate information-handling arrangements. Define which formats and exceptions it covers, so we know what the result can and cannot establish.
Evan | I can help identify the types of input and the current work steps. We should agree how to measure the time rather than rely on impressions.
Sera | Exactly. A bounded [[proof of value::Proof of value tests the proposed customer benefit against agreed measures and scope, rather than assuming demonstration success transfers automatically.]] should specify the task boundary, measures, success criteria, and test responsibilities. Compare equivalent work, including any preparation or corrections that the new process still requires.
Evan | Those eight hours would go into analysis. Nobody's pay or contracted hours would fall, so I do not want a payroll saving in the business case.
Sera | Then describe released [[labor capacity::Labor capacity is staff time available for other work; no payroll or cash reduction is planned here.]], not an automatic cash saving. The benefit may still be valuable, but the business case should name what actually changes instead of implying a payroll reduction.
Evan | Could we call it a third less report-preparation time if the full cycle goes from twenty-four hours to sixteen?
Sera | Approximately, under that [[assumption::The approximate one-third reduction depends on the unverified six-hour consolidation result and unchanged review and formatting work.]]. Eight divided by twenty-four is about thirty-three point three percent. Keep the condition and the full-cycle denominator visible rather than presenting the percentage as an established result.
Evan | We also need to understand what configuration or connections would be required before our team could use this in a real monthly cycle.
Sera | Those [[integration::Integration requirements are implementation dependencies that must be assessed before assuming the demonstrated capability works in the customer environment.]] requirements still need assessment, along with configuration and data readiness. I cannot give a reliable time-to-value or return calculation without the relevant implementation conditions and costs.
Evan | I will be responsible for verifying whether the measured reporting work actually changes. We can review the outcome with the team after the evaluation.
Sera | Good; naming the [[benefit owner::The benefit owner verifies and tracks the actual outcome, keeping responsibility separate from a seller's untested value claim.]] makes the next step clear. Let us agree the test scope, representative inputs, measures, and criteria, then use the result to support a proportionate claim about the value.''',
    rehearsal=('Read Evan and Sera aloud, then swap roles. Give the fourteen, eight, and two hours as separate parts of the current cycle.', 'Check the ten gaps. Reread the conditional sixteen-hour total and eight-hour capacity benefit.', 'Repeat the proposed test close with representative inputs, exceptions, timing measures, and a benefit owner; retain the distinction between capacity and cash.'),
    transfer_title='Explain another conditional time benefit',
    transfer_setup='A task takes 18 hours: 10 combining inputs, 6 reviewing, and 2 formatting. A proposed test targets 4 hours for combining, with the other work unchanged. No test result or staffing cost reduction exists.',
    transfer='''Seller: "The current total is ___." | 18 hours | Ten combining hours plus six review and two formatting hours equals eighteen.
Buyer: "The proposed combining time is ___." | 4 hours | Four hours is the test target, not a result already demonstrated.
Seller: "The conditional new total would be ___." | 12 hours | Four combining hours plus six review and two formatting hours would total twelve.
Buyer: "The potential time released per cycle is ___." | 6 hours | Eighteen minus twelve gives six hours of potential capacity, not an automatic cash saving.''',
))


BOOK['units'].append(unit(
    title='Objection Handling and Competitive Pressure',
    scene='The lower headline price covers a different package',
    skill='Acknowledge a price concern and compare scope, support, and implementation without inventing competitor claims.',
    brief='Daria compares an annual $42,000 offer from Luis with a competitor quote of $32,000. The $42,000 offer includes ten implementation-support hours and an initial response within four support hours. Its support window is Monday to Friday, 09:00-17:00 Eastern time, excluding listed holidays. The competitor excludes implementation support, whose price is unknown, and states next-business-day initial response under its own calendar. Neither quote promises resolution within the response time. Daria sometimes needs overnight help. Luis must compare scope honestly and check coverage rather than claim his package provides round-the-clock support.',
    cast='Daria | Prospective buyer\nLuis | Account executive',
    culture=('An objection is information, not an insult', 'A lower competitor price can reveal a real budget issue, an incomplete comparison, or a different priority. Acknowledge the difference and ask what coverage matters. Avoid treating the buyer as uninformed or asserting that the competitor must be poor quality because its headline price is lower.'),
    a='''What is the headline annual price difference? | $10,000 | $32,000 | $42,000 | No difference | Forty-two thousand minus thirty-two thousand gives a ten-thousand-dollar difference between the quoted headline amounts.
What is unknown in the competitor offer? | The price of implementation support | The stated $32,000 headline price | Whether Luis's offer includes ten support hours | Whether initial response means guaranteed resolution | The competitor excludes implementation support and supplies no price for that additional work.
Does Luis's quote provide round-the-clock support? | No; it specifies a weekday daytime window with holiday exclusions. | Yes; four support hours always means four elapsed hours. | Yes; every annual contract includes overnight service. | It guarantees overnight resolution. | The stated weekday window and exclusions do not establish support at every hour or overnight.''',
    vocabulary='''objection | A concern or reason a buyer raises against a proposal. | clarify the objection
competitive quote | An offer from another supplier being considered. | review the competitive quote
headline price | The prominent quoted amount before examining scope and conditions. | compare headline prices
like-for-like comparison | A comparison using equivalent scope and relevant terms. | make a like-for-like comparison
TCO | Total cost of ownership over a defined period and scope. | assess TCO
scope alignment | Making the included work comparable across offers. | establish scope alignment
implementation support | Assistance with setting up and introducing the offering. | specify implementation support
support tier | A defined level of assistance with stated coverage and conditions. | compare support tiers
SLA | Service-level agreement; specified service commitments and their conditions. | review the SLA
initial response | The first defined acknowledgment or engagement after a support request. | confirm initial-response terms
resolution time | Time to reach a defined completed fix or outcome. | distinguish resolution time
support window | The hours during which the stated support service operates. | check the support window
business hour | An hour counted under a specified working-time calendar. | define business hours
elapsed time | Continuous clock time between two points. | distinguish elapsed time
holiday exclusion | A stated holiday period not included in a service calendar. | check holiday exclusions
severity level | A classification of issue impact under the relevant support rules. | confirm severity levels
subscription fee | A recurring charge for access during a defined term. | compare subscription fees
one-time fee | A charge incurred once for the specified item. | identify one-time fees
recurring charge | A cost that repeats under the agreed schedule. | separate recurring charges
unpriced item | Work or a service without a supplied price. | flag unpriced items
quote validity | The period and conditions under which an offer remains available. | confirm quote validity
cost normalization | Adjusting a comparison to a consistent scope, period, and basis. | perform cost normalization
selection criterion | A factor used by the buyer to evaluate offers. | clarify selection criteria
commercial clarification | A question resolving an ambiguity in the offer's terms or price. | request commercial clarification''',
    precision='Four support hours is not automatically four elapsed hours. The stated calendar counts only covered periods, and the precise counting rules still need checking. Initial response also differs from resolution; neither quote supplies a guaranteed time to fix every issue.',
    precision_extra='The competitor headline is $10,000 lower, which should be acknowledged directly. A complete like-for-like cost comparison is still unavailable because implementation support is unpriced and service terms differ. Do not replace an incomplete comparison with an unsupported claim that either supplier has lower total cost.',
    phrases='''Acknowledge the price difference | Their headline quote is ten thousand dollars lower.
Ask what matters | Which support coverage and implementation help do you actually need?
Compare scope | Our offer includes ten implementation-support hours; theirs excludes that work.
Keep the gap explicit | We do not yet have a price for their implementation support.
Avoid an invented total | We cannot complete the like-for-like cost comparison yet.
Clarify the response term | Four support hours refers to initial response, not guaranteed resolution.
State the calendar | The stated window is weekdays from nine to five Eastern, with listed holiday exclusions.
Distinguish clock time | Support hours are not the same as continuous elapsed hours.
Check overnight needs | Your overnight requirement is not covered by this quoted window.
Avoid overclaiming | I cannot describe this package as round-the-clock support.
Ask for comparable terms | Let us compare the service calendars and what counts as an initial response.
Keep severity visible | Check whether different issue severities have different commitments.
Avoid competitor speculation | We should evaluate the written offer rather than guess at their service quality.
Request a clarification | Please obtain the missing implementation price and coverage details.
Respect the buyer's choice | The preferred offer depends on your requirements and the complete terms.
Close the comparison | We will put the prices, inclusions, exclusions, and unresolved items side by side.''',
    notes='''Headline quote | Acknowledges the supplied price while leaving wider costs open.
Includes / excludes | Makes a scope difference concrete.
Do not yet have | Identifies missing information without inventing a disadvantage.
Initial, not resolution | Separates two service events often confused in conversation.
Not covered | States a limitation of the seller's own offer honestly.
Written offer | Uses verifiable terms rather than a negative story about a competitor.''',
    d='''Which competitive statement is supported? | Their headline is $10,000 lower, but equivalent-scope total cost is not yet established. | Their total cost must be lower in every case. | Their product must be unreliable because it costs less. | Our higher headline guarantees a better customer outcome. | The stated prices establish a headline difference, while scope and unpriced implementation prevent a complete total-cost conclusion.
What does the four-support-hour term establish? | A stated initial-response commitment under the specified service calendar | Resolution within four continuous hours at any time | Round-the-clock staffing | Guaranteed correction of every issue before morning | The term concerns initial response within covered support time, not universal elapsed-time resolution.
How should Luis respond to overnight needs? | Acknowledge that the quoted window does not cover them and check appropriate options. | Describe weekday service as twenty-four-seven. | Ignore the requirement because his offer costs more. | Promise a different package without checking availability or terms. | The honest response identifies the current coverage gap and seeks a verified option instead of misrepresenting the quote.
What would improve the comparison? | A priced equivalent implementation scope and clarified service calendars | Removing the competitor's lower price from the table | Assuming every business day is identical across suppliers | Counting response and resolution as the same event | Comparable scope and clear calendars resolve material differences that headline prices alone cannot address.''',
    dialogue='''Daria | You are ten thousand higher: forty-two thousand against their thirty-two. What would we actually get for the difference, and would it cover our overnight needs?
Luis | Their [[headline price::The headline price is genuinely ten thousand lower; acknowledging it does not settle the equivalent-scope total-cost comparison.]] is lower, and that difference matters. May we compare the included work and support terms against what you need, rather than assume the two packages are identical?
Daria | Your proposal includes ten implementation-support hours. Their quote says implementation is separate, but I do not have the additional price yet.
Luis | Then that is an [[unpriced item::Implementation support has no supplied competitor price, leaving the equivalent-scope cost comparison incomplete.]]. We should keep it visible rather than invent an amount that makes our package look better. We cannot finish the equivalent-scope calculation until the missing price is supplied.
Daria | Your summary says four-hour support; theirs says next-business-day response. Are you promising a fix in four hours, or just the first response?
Luis | No. The term concerns [[initial response::Initial response is the specified first support engagement, not a guaranteed completed fix within the same period.]], not guaranteed resolution. We should correct any summary that leaves that distinction unclear, and check exactly what each offer counts as its first response.
Daria | We sometimes have an issue overnight. Would the four hours start counting from the time we contact support in the middle of the night?
Luis | We need to apply the stated [[support window::The quoted support window is weekdays, 09:00-17:00 Eastern, excluding listed holidays; it is not continuous coverage.]]. This package covers Monday to Friday, nine to five Eastern, excluding listed holidays. It does not provide round-the-clock coverage, and the precise counting rules need checking.
Daria | So four support hours could extend across more than four hours on the clock if some of that time is outside the covered window.
Luis | Correct. [[Elapsed time::Elapsed time runs continuously, unlike hours counted only within a specified support calendar.]] and counted support hours are different. I should not imply that an overnight request is guaranteed a response or a completed fix within four continuous hours.
Daria | The overnight requirement could be more important to us than the faster response during the ordinary working day.
Luis | Then make that a [[selection criterion::The selection criterion should reflect the buyer's actual overnight need rather than favor a faster daytime metric alone.]]. We need to check suitable coverage options and their actual terms. The package in front of us does not meet that requirement simply because its headline response is shorter.
Daria | I do not want the comparison to turn into claims that the competitor is poor quality. We have not evaluated their service yet.
Luis | Agreed. A [[like-for-like comparison::A like-for-like comparison uses equivalent scope and verified terms, without inventing claims about the competing supplier's quality.]] should use the written offers. Different terms do not establish poor reliability or make a lower price evidence of inferior performance.
Daria | We should also check which issues the response commitments apply to and whether the suppliers classify severity in the same way.
Luis | Yes, compare the [[severity levels::Severity levels may affect support commitments; the classifications need checking rather than assuming equal treatment across suppliers.]] and relevant conditions. A shared label does not necessarily mean the same impact threshold or entitlement, so any mismatch belongs in the comparison.
Daria | Once we have the implementation price and the relevant support option, we can compare costs for a consistent period.
Luis | That will support [[cost normalization::Cost normalization puts offers on a consistent scope and time basis, including relevant one-time and recurring charges.]]. Separate one-time and recurring charges, define the period, and check quote validity. Do not call the headline subscription amount the complete ownership cost.
Daria | Please send a table with the known prices, coverage, inclusions, and missing answers. I will ask the competitor for the implementation detail.
Luis | I will record each [[commercial clarification::Commercial clarification resolves a specific missing term or price before the buyer relies on a completed comparison.]] and our own coverage gap. Then you can judge the offers against your requirements with the remaining uncertainty visible, rather than hear an unsupported claim that either total is already lower.''',
    rehearsal=('Read Daria and Luis aloud, then swap roles. Acknowledge the ten-thousand headline difference without inventing the missing implementation price.', 'Check all ten gaps. Reread the initial-response and support-calendar exchanges, emphasizing the overnight coverage gap.', 'Repeat the side-by-side comparison close with known inclusions and unresolved questions rather than an unsupported total-cost winner.'),
    transfer_title='Keep another quote comparison accurate',
    transfer_setup='Offer A costs $28,000 annually and includes onboarding. Offer B costs $22,000 annually but excludes onboarding, whose price is unknown. Both state initial response rather than guaranteed resolution.',
    transfer='''Buyer: "The headline annual difference is ___." | $6,000 | Twenty-eight thousand minus twenty-two thousand gives a six-thousand-dollar headline difference.
Seller: "Offer B has an unpriced ___." | onboarding service | Onboarding is excluded from B and has no supplied additional price.
Buyer: "The support promise concerns ___." | initial response | Both quoted terms describe the first response, not a guaranteed completed fix.
Seller: "Equivalent-scope total cost is ___." | not yet established | The missing onboarding price prevents a complete comparison of equivalent packages.''',
))


BOOK['units'].append(unit(
    title='Pricing, Discounting, and Approval',
    scene='Calculate the request without approving it',
    skill='Calculate the requested discount and explain its approval status, price base, and review process accurately.',
    brief='A quote covers 100 licenses for 12 months at an $80,000 subscription fee plus a separate $4,000 setup fee. Buyer Matt requests a 15% reduction on the subscription only, leaving setup unchanged. That request would reduce subscription by $12,000 to $68,000, making the pre-tax first-year total $72,000. Seller Alina may approve at most 5% under the stated standard terms; 15% requires the commercial director. No exception is approved. Alina promises a status update by Thursday at 16:00 local time. The existing quote remains valid until 31 October, without a fabricated earlier deadline.',
    cast='Matt | Buyer\nAlina | Account executive',
    culture=('A calculation is not a commercial promise', 'Buyers may hear a clearly stated revised number as an offer unless its status is explicit. Name it as the requested or illustrative amount, then explain the approval route. A firm limit can remain helpful when the seller gives a specific next step and a reliable update time.'),
    a='''What is the base for the requested 15% reduction? | The $80,000 subscription fee only | The full $84,000 including setup | Only the $4,000 setup fee | An unspecified future renewal amount | The buyer requests a subscription reduction while leaving the separate setup fee unchanged.
What would the requested pre-tax first-year total be? | $72,000 | $68,000 including setup | $71,400 | $84,000 after a 15% subscription reduction | The reduced subscription would be sixty-eight thousand plus the unchanged four-thousand setup fee.
Can Alina approve the 15% request? | No; it requires the commercial director. | Yes; her limit is 15%. | Yes; calculating it approves it. | Yes; the buyer's request overrides the limit. | Alina's authority is at most five percent under the stated terms, so the larger reduction requires escalation.''',
    vocabulary='''list price | A stated standard price before the relevant discounts. | confirm the list price
price book | A controlled source of product prices and related pricing entries. | use the approved price book
discount base | The amount to which a percentage reduction applies. | identify the discount base
discount amount | The monetary reduction from the specified base. | calculate the discount amount
net price | The price after the specified reductions, with inclusions and taxes clarified. | state the net price
subscription term | The period covered by the access agreement. | confirm the subscription term
setup fee | A charge for defined initial setup work. | separate the setup fee
pre-tax total | The amount before applicable taxes are included. | calculate the pre-tax total
approval threshold | A limit above which a different authorization is required. | check the approval threshold
delegated authority | Decision power assigned to a role within stated limits. | stay within delegated authority
pricing exception | A proposed departure from standard pricing conditions. | request a pricing exception
deal desk | A commercial support function coordinating complex terms and approvals. | consult the deal desk
CPQ | Configure, price, quote; tools or processes for preparing structured commercial offers. | update the CPQ record
approval workflow | The required sequence for reviewing and authorizing a request. | follow the approval workflow
concession | A term or benefit offered during negotiation. | evaluate a concession
give-get | A negotiated exchange of a concession for a specified reciprocal commitment. | document the give-get
payment terms | Conditions governing when and how amounts are paid. | confirm payment terms
prepayment | Payment before the specified service or billing period. | assess a prepayment option
contract term | The duration or another defined condition of an agreement, depending on context. | clarify the contract term
ACV | Annual contract value, calculated under the organization's stated inclusion rules. | define ACV consistently
TCV | Total contract value over the specified term, with included charges defined. | calculate TCV
margin | A profit measure relative to revenue under a specified cost basis. | assess margin impact
quote validity | The period for which the quoted terms remain open under their conditions. | preserve quote validity
approved quote | An offer authorized through the relevant internal process. | issue an approved quote''',
    precision='Fifteen percent of $80,000 is $12,000. The requested subscription becomes $68,000; adding the unchanged $4,000 setup charge gives $72,000 before tax. Applying 15% to the entire $84,000 would use the wrong base for this request.',
    precision_extra='Price reduction and margin reduction are not the same measure. No cost information is supplied, so a profit-margin effect cannot be calculated from the discount alone. The $72,000 figure is the requested scenario, not an approved offer or a tax-inclusive total.',
    phrases='''Confirm the request | You are asking for fifteen percent off the subscription only.
State the base | The discount base is eighty thousand dollars.
Show the amount | Fifteen percent of that base is twelve thousand dollars.
State the conditional price | The requested subscription would be sixty-eight thousand dollars.
Keep setup separate | The four-thousand-dollar setup fee remains unchanged.
State the total accurately | The requested first-year total would be seventy-two thousand before tax.
Limit authority | My approval limit is five percent under these standard terms.
Name the approver | The fifteen-percent exception requires the commercial director.
Keep the status explicit | This is a request under review, not an approved revised quote.
Avoid a guaranteed outcome | I can submit the request, but I cannot promise approval.
Explain other options carefully | A change to term or payment timing would need its own assessment and approval.
Avoid silent stacking | We should not combine concessions without checking the complete package.
Preserve the real deadline | The existing quote is valid until the thirty-first of October.
Reject manufactured urgency | I will not describe an earlier cutoff that is not in the offer.
Commit to communication | I will update you by Thursday at sixteen hundred local time.
Close with the right document | Any approved change will appear in the revised authorized quote.''',
    notes='''Only | Identifies which charge receives the percentage reduction.
Would be | Keeps the arithmetic conditional on the requested concession.
Before tax | Defines what the total excludes.
My limit | States the seller's actual authority.
Under review | Describes process status rather than approval.
Any approved change | Makes the revised offer conditional on authorization.''',
    d='''Which calculation matches the request? | $80,000 minus $12,000, plus $4,000 setup, equals $72,000 before tax. | $84,000 multiplied by 85%, with setup discounted too | $68,000 including a waived setup fee | $80,000 plus a 15% surcharge | The correct calculation applies the reduction only to subscription and retains the separate setup charge.
Which status statement avoids a premature commitment? | The requested total would be $72,000 before tax, subject to the required approval. | Your approved total is $72,000 because I calculated it. | Approval is guaranteed once the request enters the system. | The setup fee has disappeared without agreement. | Conditional wording distinguishes the requested calculation from the actual authority to issue a revised offer.
What is promised for Thursday at 16:00? | A status update | Approval of the exception | A signed customer contract | A guaranteed director decision | Alina commits to communication at that time, not to an outcome outside her authority.
Which deadline should be communicated? | The existing 31 October quote-validity date | An invented earlier cutoff to pressure the buyer | No deadline because the request changes every term automatically | A guaranteed renewal price forever | The supplied quote remains valid through the stated date; no earlier limit has been established.''',
    dialogue='''Matt | Can you take fifteen percent off the subscription? That is the request I can take back internally. Leave the setup fee as it is.
Alina | Let me confirm the [[discount base::The reduction applies to the eighty-thousand subscription, not the separate setup charge or the entire quote.]]. You mean the eighty-thousand-dollar subscription for one hundred licenses over twelve months, with the four-thousand-dollar setup charge unchanged.
Matt | Correct. Please show me what that would mean for the first-year amount, so I can explain the request internally.
Alina | The [[discount amount::Fifteen percent of eighty thousand is twelve thousand, leaving sixty-eight thousand for the subscription.]] would be twelve thousand dollars. That brings the requested subscription to sixty-eight thousand, before adding the unchanged setup fee. I am calculating the request, not approving it.
Matt | So the total for the first year would be seventy-two thousand. Does that number include tax?
Alina | No, it is the [[pre-tax total::The seventy-two-thousand total combines the requested subscription and unchanged setup fee before applicable taxes.]]. It combines sixty-eight thousand in subscription and four thousand in setup. We should keep that scope clear when you share the calculation.
Matt | Can you approve that reduction now, or does somebody else need to decide?
Alina | My [[delegated authority::Alina can approve at most five percent under the stated standard terms, not the requested fifteen percent.]] is limited to five percent under these standard terms. The fifteen-percent request requires the commercial director, so I cannot issue it as an approved offer today.
Matt | Please send it for review. I do not want the team to mistake your calculation for a price we can already accept.
Alina | I will label it as a [[pricing exception::The fifteen-percent request is an unapproved departure requiring the commercial director's decision.]] under review. The amount and requested scope will be explicit, along with the fact that no exception approval has been granted.
Matt | Would a longer term or earlier payment help? I am open to options, but I cannot commit to those changes without our own review.
Alina | We can assess the relevant [[payment terms::Different payment timing changes the commercial package and needs assessment; it does not automatically approve the requested discount.]] or term alternatives. They are separate commercial choices, not automatic ways to secure the same discount. Any proposed exchange needs to be clear and approved on both sides.
Matt | I also do not want several concessions added together without knowing which condition goes with each one.
Alina | Agreed. Any [[give-get::A give-get links a specified concession to a reciprocal commitment, rather than silently combining discounts and changed terms.]] must identify the actual exchange. We should assess the whole package and avoid stacking a discount, a term change, and different payment timing as though each were independently approved.
Matt | I heard the price might expire before Friday, but the quote says October thirty-first. Has something changed, or should I use the written date?
Alina | The stated [[quote validity::The existing quote remains valid until 31 October; no earlier deadline is supported by the supplied terms.]] remains the thirty-first of October. I will not introduce an earlier deadline that is not in the offer or use an unsupported cutoff to rush your decision.
Matt | When will I hear back? I need a reliable update even if the director has not reached a decision.
Alina | I will update you by Thursday at sixteen hundred local time on the [[approval workflow::The workflow routes the request to the authorized decision-maker; the promised update does not guarantee approval by that time.]]. That is a status commitment, not a promise that the exception will be approved by then.
Matt | Once a decision is made, please make sure the document shows exactly which charges, conditions, and dates have changed.
Alina | Any authorized change will appear in the [[approved quote::An approved quote records the actual authorized terms, unlike an illustrative calculation or a request still under review.]]. Until then, the seventy-two-thousand pre-tax amount is the requested scenario, and the existing offer remains subject to its stated terms.''',
    rehearsal=('Read Matt and Alina aloud, then swap roles. State the discount base before calculating the amount.', 'Correct all ten gaps. Reread the seventy-two-thousand pre-tax request, five-percent authority limit, and required exception approval.', 'Repeat the Thursday update commitment and existing quote deadline without promising a director decision or inventing urgency.'),
    transfer_title='Calculate another request without approving it',
    transfer_setup='A quote has a $50,000 subscription and an unchanged $3,000 setup fee. The buyer requests 10% off subscription only. The seller cannot approve that exception; the required decision is pending.',
    transfer='''Seller: "The discount base is ___." | $50,000 | The reduction applies only to the subscription, not the separate setup fee.
Buyer: "The requested discount amount is ___." | $5,000 | Ten percent of fifty thousand equals five thousand dollars.
Seller: "The requested total before tax would be ___." | $48,000 | Forty-five thousand in reduced subscription plus three thousand setup gives forty-eight thousand.
Buyer: "The approval status is ___." | pending | The seller lacks authority to approve the exception, and no required decision has been supplied.''',
))


BOOK['units'].append(unit(
    title='Enterprise Buying Committees',
    scene='A supportive contact is not the whole buying process',
    skill='Map purchase roles, criteria, and sequence while respecting the main contact and separating interest from authorization.',
    brief='Operations manager Devon is enthusiastic about Rosa\'s proposal and can explain the workflow need. He does not control the budget or hold contract-signing authority. The finance director owns budget approval, procurement owns vendor onboarding, and an information-security review is required. The authorized contract signer has not been identified. None of these reviews has started. Rosa must work with Devon to identify owners, criteria, sequence, and realistic access to the other participants. Enthusiasm is not an approved purchase, and a favorable demonstration is not a completed security review.',
    cast='Devon | Prospect operations manager\nRosa | Account executive',
    culture=('Broaden the conversation without bypassing the contact', 'A main contact can feel sidelined when a seller suddenly approaches senior colleagues without context. Explain which decisions require other roles and agree how to involve them. A buying-role map should support a transparent evaluation, not encourage secret pressure or treat people as obstacles to be manipulated.'),
    a='''What can Devon contribute? | The workflow need and operational evaluation context | Independent approval of the budget | Contract signature on behalf of the organization | Completion of security review by enthusiasm | Devon understands the operational need but explicitly lacks budget control and signing authority.
Who owns vendor onboarding? | Procurement | Devon alone | The seller's marketing team | Any end user who attended the demonstration | The brief assigns the vendor-onboarding process to procurement.
Which authority is still unidentified? | The authorized contract signer | The owner of budget approval | The team responsible for vendor onboarding | Whether security review is required | The finance and procurement roles are identified, but contract-signing authority remains unknown.''',
    vocabulary='''buying committee | The people participating in evaluating and authorizing a purchase. | map the buying committee
economic buyer | A person with the relevant overall spending decision authority under the buying arrangement. | identify the economic buyer
champion | An influential internal advocate who actively supports a proposal. | verify the champion's role
coach | A contact who helps explain the organization or process without necessarily having strong influence. | learn from a coach
influencer | A person shaping a decision without necessarily holding approval authority. | understand the influencer
end user | A person expected to use the proposed product or service. | involve end users
procurement | The function managing specified purchasing and supplier processes. | engage procurement
gatekeeper | A role controlling access or a required process step. | understand the gatekeeper's requirements
budget approval | Authorization for the relevant allocation or use of funds. | obtain budget approval
decision criteria | The factors used by the buyer to judge options. | confirm decision criteria
decision process | The steps and roles used to choose an option. | map the decision process
paper process | The administrative and contractual steps leading from a decision to signature. | clarify the paper process
authorized signer | A person empowered to execute the relevant agreement. | identify the authorized signer
stakeholder map | A record of relevant people, roles, concerns, and responsibilities. | maintain the stakeholder map
stakeholder alignment | Shared understanding of the proposal and relevant decision requirements. | build stakeholder alignment
single-threaded | Dependent on one contact or relationship in an account. | identify a single-threaded opportunity
multi-threaded | Engaging multiple relevant roles in an account. | develop a multi-threaded engagement
access path | An agreed way to involve or communicate with a relevant person. | agree an access path
executive sponsor | A senior person supporting an initiative within their role. | confirm the executive sponsor
technical win | Informal sales language for favorable technical evaluation, not necessarily purchase approval. | distinguish a technical win
commercial approval | Authorization of the relevant business or financial terms. | confirm commercial approval
vendor onboarding | Steps needed to establish a supplier in the buyer's systems and processes. | complete vendor onboarding
security review | Assessment of relevant information-security requirements. | coordinate the security review
stakeholder concern | A requirement or issue raised by someone involved in the decision. | address stakeholder concerns''',
    precision='Budget approval, vendor onboarding, security review, and contract signature are different steps. The same person may hold several roles in some organizations, but that cannot be assumed here. Devon supports the operational need and does not hold the stated commercial authorities.',
    precision_extra='Champion, coach, technical win, and paper process are common sales shorthand. Use them carefully in internal discussions and translate them into actual responsibilities with customers. An enthusiastic contact is not necessarily an influential advocate, and a technical preference is not a signed purchase.',
    phrases='''Recognize the support | Your understanding of the workflow will help us make the evaluation relevant.
Clarify the contact role | Which decisions do you own, and which require other colleagues?
Ask about budget | Who approves the relevant funding?
Ask about procurement | What vendor-onboarding steps need to happen?
Keep security distinct | A product demonstration does not complete the required security review.
Identify signature authority | Who is authorized to sign the agreement?
Map the sequence | Which reviews can run together, and which depend on an earlier decision?
Ask about criteria | What does each group need to establish before it can support the purchase?
Avoid assuming a champion | I do not want to infer your internal authority from your interest in the proposal.
Agree access respectfully | How would you prefer us to involve the relevant colleagues?
Preserve the main contact | We can keep you included as we address the other teams' questions.
Distinguish technical preference | A favorable technical evaluation does not by itself approve commercial terms.
Keep progress factual | None of the budget, onboarding, or security reviews has started yet.
Avoid a signature promise | We cannot confirm a signing date before understanding the required steps.
Plan jointly | Let us agree owners and realistic next actions with the relevant teams.
Close the map | I will separate known roles, unconfirmed authority, review status, and next steps.''',
    notes='''Which decisions | Clarifies role boundaries without questioning the contact's value.
Need to establish | Connects each reviewer to a relevant requirement.
How would you prefer | Seeks an agreed introduction rather than bypassing the contact.
Does not by itself | Prevents one favorable review being inflated into complete approval.
Has started | Describes actual process progress rather than intention.
Unconfirmed authority | Keeps a missing role visible until it is verified.''',
    d='''Which internal account note is accurate? | Devon supports the need; budget, procurement, security, and signer steps remain unresolved. | Devon's enthusiasm means the purchase is approved. | The demonstration completed the security review. | The finance director must be the signer because the title sounds senior. | The note distinguishes support from the separate uncompleted reviews and unknown signing authority.
Which question broadens access respectfully? | How can we involve the relevant reviewers while keeping you included? | Could you approve the technical and funding questions so other teams need not attend? | Should we wait for signature before involving procurement? | Can we send every reviewer the same feature deck instead of asking what they need? | An agreed introduction preserves the contact's role while involving the actual owners. Substituting Devon's approval, involving procurement too late, or ignoring different criteria does not resolve the buying process.
What does a technical win establish in this context? | A favorable technical assessment, not necessarily budget or contract approval | A completed signed contract | Automatic onboarding | Guaranteed authority for every end user | Technical preference concerns suitability and does not substitute for separate commercial and contractual decisions.
What should the role map distinguish? | Owners, evaluation criteria, sequence, current status, and unknown authority | Job titles alone | Only people who favor the seller | A presumed signature date without process evidence | A usable map explains responsibilities and remaining steps rather than relying on titles or favorable opinions.''',
    dialogue='''Devon | This looks useful for our workflow. I want to take it forward, but I have not bought something like this before. Who needs to be involved next?
Rosa | Let us map the [[buying committee::The buying committee includes the roles needed to evaluate and authorize the purchase, beyond one supportive contact.]] to identify the reviewers and their decisions. Your support is helpful, but I should not assume that you own every approval.
Devon | I coordinate the operational need, but I do not control the budget. The finance director owns the funding approval.
Rosa | Then we should identify the relevant [[budget approval::Budget approval belongs to the finance director in this scenario, not to Devon because he likes the proposal.]] requirements with that role. We need to know what evidence the director expects and how the funding decision relates to the wider purchase process.
Devon | Procurement handles setting up new vendors. I have not contacted them about this proposal yet.
Rosa | Their [[vendor onboarding::Vendor onboarding is a separate procurement process that has not begun; interest in the proposal does not complete it.]] steps should be visible in the plan. We should ask about the required information and timing rather than assume that a favorable operational review gets a supplier into the system automatically.
Devon | Information security also needs to assess the offering. The demonstration was useful, but it was not that assessment.
Rosa | Correct. A [[security review::Security review is required separately; the demonstration does not establish that the buyer's information-security conditions are satisfied.]] has its own requirements and owner. We can arrange the appropriate information exchange without presenting a successful demonstration as clearance to purchase or deploy.
Devon | I do not know who signs the eventual agreement. It may not be the same person who approves the budget.
Rosa | We need to confirm the [[authorized signer::Signing authority is still unidentified and must not be inferred from budget responsibility or a senior job title.]]. A title or budget role is not enough to infer contract authority. We can leave that field unconfirmed until the relevant person or process establishes it.
Devon | There are more steps than I had considered. Some might be able to run together, while others probably depend on a decision first.
Rosa | That is why the [[decision process::The decision process maps evaluation roles and sequence, including steps that can run together and those with dependencies.]] matters. Ask the owners which activities can proceed together and what each one needs before starting, rather than impose a seller timeline on an unknown process.
Devon | Once the organization decides to buy, there may still be contract and purchasing steps before anyone can sign.
Rosa | Sales teams sometimes call that the [[paper process::The paper process covers administrative and contractual steps toward signature, distinct from merely choosing a preferred solution.]]. With your colleagues, we should name the actual documents, reviews, and authorities. The shorthand should not hide work that remains after a preferred option is selected.
Devon | I can make introductions. Please keep me in the conversation, though; I do not want to hear secondhand that the scope changed in a separate meeting.
Rosa | Let us agree the [[access path::An agreed access path involves the necessary reviewers transparently while keeping the main contact appropriately included.]] with you. We can explain why each colleague is needed, keep you included, and focus the conversations on their requirements rather than ask everyone to attend an unfocused sales meeting.
Devon | Some people will care most about the workflow, while others need cost, security, or supplier information. We should not assume they judge the same thing.
Rosa | Record those [[decision criteria::Different reviewers may assess different requirements, so the criteria need explicit confirmation rather than a single assumed preference.]] explicitly. That helps us address substantive questions and understand disagreement without labeling every person who asks for evidence an obstacle.
Devon | Please send a map showing the known roles and the gaps. I will help identify the right owners and discuss a realistic next meeting.
Rosa | I will update the [[stakeholder map::The map records known roles, unconfirmed authority, review status, and next actions without inventing purchase approval.]]. Budget, onboarding, and security reviews have not started, and the signer is unconfirmed. We can plan next steps without inventing purchase approval or a signing date.''',
    rehearsal=('Read Devon and Rosa aloud, then swap roles. Ask about decisions and responsibilities, not just senior job titles.', 'Check all ten gaps. Reread the funding, procurement, security, and signature distinctions.', 'Repeat the agreed introduction and stakeholder-map close while keeping Devon included and unconfirmed authority visible.'),
    transfer_title='Separate another set of buying roles',
    transfer_setup='A department lead supports a proposal. Finance approves funding, procurement registers suppliers, and a technical team evaluates compatibility. The contract signer remains unknown, and no purchase is approved.',
    transfer='''Seller: "The funding role belongs to ___." | finance | Finance holds the stated funding-approval responsibility, not the supportive department lead.
Lead: "Supplier registration belongs to ___." | procurement | Procurement owns the separate supplier-registration process in this scenario.
Seller: "Compatibility is evaluated by the ___." | technical team | The technical team's role concerns compatibility, not automatic funding or contract approval.
Lead: "The contract signer remains ___." | unknown | No signing authority has been identified, so it must not be inferred from another role.''',
))


BOOK['units'].append(unit(
    title='Negotiation and Contract Redlines',
    scene='A customer redline needs review, not an immediate yes',
    skill='Route the exact proposed contract change for review without accepting it or promising a legal outcome.',
    brief='Buyer Priya returns agreement version 4 with a proposed change to clause 10.2, removing a stated liability cap and requesting uncapped liability. She asks seller Marcus to accept it today. The company requires legal review and authorized commercial approval for this change; Marcus holds neither authority. No response wording has been approved. Marcus must preserve the marked document, clarify the business concern for counsel, and track the review. He promises a status update at 16:00 Eastern today, not acceptance. The effect of the clause depends on the complete agreement and relevant law, which the exercise does not determine.',
    cast='Priya | Buyer coordinating contract comments\nMarcus | Account executive',
    culture=('Keep the commercial relationship moving without acting as counsel', 'A buyer asking for an immediate answer may be trying to meet an internal deadline rather than dismiss the review process. Acknowledge that pressure, identify the exact question, and provide a reliable update. Do not create apparent acceptance to preserve momentum or give an unsupported view of enforceability.'),
    a='''What change has the buyer proposed? | Removing the stated liability cap in clause 10.2 of version 4 | Approving the unchanged contract | Reducing only the subscription price | Confirming that all legal review is complete | The brief identifies the version, clause, and proposed removal of the cap without treating it as agreed.
Can Marcus accept the wording? | No; he lacks the required legal and commercial approval authority. | Yes; receiving a redline approves it. | Yes; the buyer's deadline transfers authority. | Yes; version 4 is automatically final. | The stated company process requires reviews and approvals Marcus does not hold.
What is promised at 16:00 Eastern? | A review-status update | Acceptance of uncapped liability | A guarantee of enforceability | A signed agreement from both parties | Marcus commits to a status communication, not an outcome reserved for the required reviewers and approvers.''',
    vocabulary='''redline | A document showing proposed changes to existing wording. | review the redline
markup | Visible additions, deletions, or comments in a document. | preserve the markup
clean version | A version without visible change marks, whose approval status still needs checking. | reconcile the clean version
version control | Identification and management of document revisions. | maintain version control
contract clause | A defined provision within an agreement. | identify the contract clause
liability cap | A stated limit on specified liability, subject to the wording and applicable law. | review the liability cap
uncapped liability | Liability without the specified contractual cap, subject to the full legal context. | assess proposed uncapped liability
indemnity | An obligation concerning compensation for specified losses under the relevant terms. | review the indemnity
warranty | A contractual assurance with meaning and remedies determined by the relevant terms and law. | clarify the warranty
representation | A statement of fact whose legal effect depends on context and applicable law. | review the representation
governing law | The law identified or determined as applicable to an agreement or issue. | confirm governing law
jurisdiction | The relevant authority or forum's legal power over a matter. | review jurisdiction terms
carve-out | An exception to a stated contractual rule or limitation. | identify a carve-out
consequential loss | A category of loss whose scope depends on applicable law and contract interpretation. | refer consequential-loss wording
third-party claim | A claim made by someone outside the contracting parties. | assess third-party claims
MSA | Master services agreement; overarching terms governing specified services or later orders. | review the MSA
order form | A document setting out the specific purchase and related terms. | reconcile the order form
DPA | Data processing agreement or addendum governing specified processing arrangements. | route the DPA for review
approved fallback | Alternative wording authorized for defined circumstances. | check the approved fallback
escalation | Routing an issue to the appropriate authority or specialist. | escalate the redline
authorized signatory | A person empowered to sign the relevant agreement. | verify the authorized signatory
signature workflow | The agreed steps for approving and executing the contract. | confirm the signature workflow
negotiating position | A proposed stance on terms, distinct from a final agreement. | clarify the negotiating position
acceptance | Assent to proposed terms, with legal effect determined by the relevant circumstances. | avoid unintended acceptance''',
    precision='Receiving a marked agreement means a proposal has arrived; it does not mean the changed clause is accepted. A clean version can also contain unapproved wording. Keep document status, review status, commercial approval, and signature status distinct.',
    precision_extra='The exercise supplies an approval process, not enough information to determine the clause effect or enforceability. Do not treat capped, uncapped, indemnity, or carve-out as self-contained legal conclusions. The full text, related terms, and applicable law require the relevant qualified review.',
    phrases='''Acknowledge receipt | I have received your marked version four.
Identify the change | The proposed change is to clause ten point two.
Confirm the request | You are asking to remove the stated liability cap.
Preserve the status | I am acknowledging the proposal, not accepting the wording.
Explain authority | This change requires legal review and authorized commercial approval.
Avoid an improvised legal answer | I cannot determine the clause's effect or enforceability.
Clarify the concern | What business concern should I include when routing the request to counsel?
Keep the text intact | I will send the full marked agreement, not a paraphrase of the clause alone.
Check related terms | The reviewers need the complete document and relevant cross-references.
Avoid a promised fallback | No alternative wording has been approved for this request yet.
Track the version | Any response should identify the version and changes clearly.
Separate urgency and approval | I understand the deadline, but it does not change the required authority.
Promise communication | I will update you at sixteen hundred Eastern today.
Keep uncertainty honest | That update may report that the review is still pending.
Reconcile before signature | The final clean text must match the authorized negotiated position.
Close without apparent assent | The proposed change remains under review until the required decision is communicated.''',
    notes='''Received | Confirms delivery without stating agreement.
Proposed | Keeps the change distinct from an accepted term.
Not accepting | Removes ambiguity from the acknowledgment.
Business concern | Gives reviewers context without asking the seller to supply legal advice.
Full marked agreement | Preserves exact wording and its surrounding terms.
May report pending | Makes the update promise realistic rather than a hidden promise of approval.''',
    d='''Which acknowledgment preserves the actual status? | I received version 4; clause 10.2 remains under the required review and is not accepted. | Agreed, although I have no authority. | The clean file proves everyone approved it. | The buyer's deadline makes the clause enforceable. | The acknowledgment confirms receipt and preserves the unresolved review without implying legal or commercial assent.
What should Marcus send for review? | The full marked agreement with the exact version and business concern | A memory-based paraphrase with the original deleted | Only an unsigned sentence separated from every cross-reference | A message saying approval already exists | Exact wording and context let the qualified reviewers assess the actual proposal rather than a distorted summary.
What can Marcus responsibly promise today? | A status update at 16:00 Eastern | Automatic approval of the buyer's wording | A favorable legal conclusion | A signature from an unidentified authorized person | The only supported commitment is communication at the stated time, not an unapproved review result.
Which check belongs before signature? | Reconcile the clean text with the authorized negotiated version. | Assume all clean documents are approved. | Delete the change history before reviewers compare it. | Treat an email acknowledgment as the final executed agreement. | The final text must match the authorized position rather than merely look finished.''',
    dialogue='''Priya | We have marked clause ten point two in version four. Our team wants the liability cap removed, and they are asking me for your answer today.
Marcus | I have received the [[redline::The redline contains proposed changes; receiving it does not mean the seller has accepted the wording.]]. I am acknowledging the proposal, not accepting the wording. This change requires legal review and authorized commercial approval, neither of which I can provide myself.
Priya | Our team considers the existing cap too restrictive. Can you tell me whether removing it is legally necessary?
Marcus | I cannot determine the effect of the [[liability cap::The liability cap's effect depends on the full wording and legal context, which Marcus is not authorized to determine.]] or give that legal conclusion. I can make sure the reviewers receive your concern and the exact proposed text rather than an incomplete description.
Priya | We are asking for uncapped liability because the business team is concerned about losses beyond the current amount.
Marcus | I will pass that concern on with the proposed [[uncapped liability::The request removes the specified cap, but its consequences require review of the full agreement and applicable law.]] wording. The reviewers need the complete agreement and related provisions, not a conclusion from me about what the change would mean in every situation.
Priya | Please do not send only a summary saying that we want different risk terms. The exact wording matters to our team.
Marcus | Agreed. I will preserve the [[markup::The markup preserves the actual additions and deletions so reviewers assess the customer's exact proposal.]] and identify version four clearly. A paraphrase could miss an exception, cross-reference, or other wording that changes the question the reviewers need to answer.
Priya | Could you offer your standard alternative now? That might avoid another round of discussion.
Marcus | No [[approved fallback::No alternative wording is authorized for this request, so Marcus must not improvise a supposedly approved substitute.]] has been cleared for this request. I will ask whether an authorized alternative is available, but I should not invent one or suggest that a familiar phrase is automatically permitted.
Priya | I understand the review requirement, but the timing is difficult. Our internal team expects an answer today.
Marcus | I understand. The [[escalation::Escalation routes the urgent request to the proper reviewers without transferring their authority to the salesperson.]] will include that deadline and your business concern. Urgency helps the reviewers prioritize; it does not give me authority to accept terms before the required decision.
Priya | What can you commit to telling us today, even if the substantive answer is not ready?
Marcus | I will update you at sixteen hundred Eastern on the [[negotiating position::The negotiating position remains subject to authorized review; the update may report pending status rather than an accepted term.]] and review status. That may mean confirming that the review is still pending, not promising acceptance or a particular alternative by that time.
Priya | Please put the version number in the reply. We already have several files circulating, and I cannot risk forwarding the wrong wording to our reviewer.
Marcus | We will maintain [[version control::Version control distinguishes the exchanged proposals and authorized text, reducing the risk of reviewing or signing the wrong revision.]]. Each response should show which version it addresses and what changed, so neither team treats an older file as the current negotiated text.
Priya | Our team will need a clean document for signature eventually, but I do not want clean formatting to hide a disagreement.
Marcus | Exactly. A [[clean version::A clean version removes visible change marks but does not itself prove that its wording was reviewed or approved.]] must be reconciled with the authorized position. Removing markup is a formatting step, not evidence that the underlying terms have been approved.
Priya | Please confirm the signing route once the wording is actually agreed through the required process.
Marcus | We will verify the [[authorized signatory::The signatory must hold the relevant execution authority; the account executive's acknowledgment does not establish it.]] and signature workflow then. For now, the proposed clause change remains under review, and my next commitment is the status update at sixteen hundred Eastern.''',
    rehearsal=('Read Priya and Marcus aloud, then swap roles. Acknowledge the urgent deadline without sounding as though the clause has been accepted.', 'Correct all ten gaps. Reread the exact-version, full-markup, and authorized-review exchanges.', 'Repeat the sixteen-hundred Eastern status commitment, keeping the review outcome and eventual signature separate.'),
    transfer_title='Acknowledge another unapproved redline',
    transfer_setup='A buyer returns version 7 with a change to clause 8.3. The account executive cannot accept it and must obtain legal and authorized commercial review. The next status update is due at 11:00 Central.',
    transfer='''Seller: "The received document is ___." | version 7 | The supplied version identifier distinguishes this proposal from other exchanged documents.
Buyer: "The changed provision is ___." | clause 8.3 | Clause 8.3 is the specific provision identified for review.
Seller: "Receipt does not mean ___." | acceptance | Acknowledging the proposal does not authorize or agree to the changed wording.
Buyer: "The promised status update is at ___." | 11:00 Central | This is the stated communication deadline, not a guarantee of approval or signature.''',
))


BOOK['units'].append(unit(
    title='Partnerships and Channel Development',
    scene='Define the partnership before promising exclusivity',
    skill='Define territory, products, duration, contribution, and funding before promising partnership rights.',
    brief='Chen requests exclusivity without defining territory, products, duration, or contribution. Amina cannot grant it. For assessment, the team proposes a six-month nonexclusive scheduling-product pilot in fictional Region North, targeting four qualified opportunities per quarter. Qualification requires a customer need, relevant contact, and agreed next step, not an order. Chen requests $5,000 marketing support; none is approved. All pilot terms require commercial and legal review.',
    cast='Chen | Potential channel partner\nAmina | Channel development manager',
    culture=('Partnership language can hide different expectations', 'Partner may mean joint marketing to one party and exclusive resale rights to another. Name the activities and responsibilities first. Shared ambition does not settle rights, targets, funding, or legal suitability.'),
    a='''What is missing from the initial exclusivity request? | Defined territory, products, duration, and contribution | The fact that Chen is interested | An already approved exclusive contract | A guaranteed customer order | The initial request leaves the scope and contribution undefined, so it is not a complete proposed arrangement.
What pilot is being considered? | A six-month nonexclusive scheduling-product pilot in Region North | Permanent worldwide exclusivity for every product | An already executed reseller agreement | Unlimited marketing funding | The brief specifies a bounded nonexclusive pilot for assessment, while all terms remain unapproved.
What does four qualified opportunities per quarter mean here? | Four opportunities meeting the stated need, contact, and next-step criteria | Four signed orders guaranteed | Four arbitrary names on a mailing list | Four paid implementations | The supplied qualification definition concerns opportunity evidence, not completed purchases or revenue.''',
    vocabulary='''channel partner | An organization helping market, sell, deliver, or support an offering under agreed terms. | develop a channel partner
referral partner | A partner introducing potential customers under the relevant arrangement. | define a referral partnership
reseller | A party selling another organization's offering under agreed rights and terms. | appoint a reseller
distributor | An intermediary supplying products to other sellers or channels under an arrangement. | work with a distributor
VAR | Value-added reseller; a reseller combining an offering with additional services or capabilities. | assess a VAR model
MSP | Managed service provider; a provider operating specified services for customers. | engage an MSP
ISV | Independent software vendor; a company developing and selling its own software. | coordinate an ISV partnership
co-selling | Seller and partner working together on a defined sales opportunity. | agree co-selling roles
partner enablement | Training, resources, and support preparing partners to perform agreed activities. | deliver partner enablement
territory | The defined geographic or account area covered by rights or activity. | define the territory
exclusivity | A restriction or sole right within specified boundaries, subject to agreement and law. | assess exclusivity terms
nonexclusive | Not granting a sole right within the stated arrangement. | propose a nonexclusive pilot
product scope | The offerings included in the arrangement. | specify the product scope
term | The defined duration of an arrangement. | agree the pilot term
performance target | A specified level of contribution or result being sought. | define performance targets
qualified opportunity | A potential sale meeting the organization's explicit qualification conditions. | document qualified opportunities
deal registration | Recording a partner opportunity under the relevant channel process. | confirm deal registration
channel conflict | Overlap or disagreement between sales routes or partners. | manage channel conflict
attribution rule | A rule defining who receives credit for a contribution or result. | agree attribution rules
MDF | Market development funds; resources for specified partner marketing activity under approved terms. | request MDF
sell-in | Sales into a channel intermediary, under the relevant measurement definition. | measure sell-in
sell-through | Sales onward through the channel to the defined customer group. | track sell-through
support handoff | Transfer of responsibility for customer assistance between parties. | define the support handoff
renewal review | Assessment before deciding whether to continue an arrangement. | schedule a renewal review''',
    precision='A qualified opportunity is not a signed order. This pilot proposal uses three explicit conditions: identified need, relevant contact, and agreed next step. Four opportunities per quarter would measure pipeline contribution under that definition, not guaranteed bookings or cash receipts.',
    precision_extra='Nonexclusive describes proposed rights, not approval of the arrangement. Territory, products, duration, targets, support, funding, and review terms still need agreement. The $5,000 request does not authorize spending on behalf of the seller.',
    phrases='''Clarify the activity | Are you proposing referrals, resale, implementation, or a combination?
Define the request | What territory, products, duration, and contribution would the exclusive right cover?
State authority | I cannot grant exclusivity in this conversation.
Offer a bounded assessment | We can assess a six-month nonexclusive pilot.
State product and territory | The proposal covers the scheduling product in Region North.
Keep the status clear | These are proposed terms, not an executed agreement.
Define contribution | The target is four qualified opportunities per quarter.
Define qualification | Each opportunity needs an identified need, relevant contact, and agreed next step.
Avoid a bookings claim | An opportunity target is not a guarantee of signed orders.
Plan enablement | What training and materials would support the agreed activities?
Handle overlapping accounts | We need rules for registration and channel conflict.
Clarify credit | Agree how joint contributions will be attributed.
Separate the funding request | The five-thousand-dollar marketing request is not approved.
Assign support | Define who handles customer questions and when responsibility transfers.
Set the review | Agree how results and continuation will be assessed at the end of the pilot.
Close responsibly | Submit the full proposal for the required commercial and legal review before promising rights or funding.''',
    notes='''Are you proposing | Clarifies the relationship type before discussing rights.
Would cover | Treats exclusivity as a defined proposal rather than a vague privilege.
Can assess | Offers evaluation without granting authority.
Each opportunity | Makes the contribution measure testable.
Not approved | Prevents a funding request becoming implied spending permission.
Full proposal | Keeps rights, obligations, targets, and resources together for review.''',
    d='''Which response handles exclusivity appropriately? | Define the scope and contribution, then route the proposal for the required review without promising the right. | Grant worldwide exclusivity because the partner sounds enthusiastic. | Treat the word partner as a signed agreement. | Approve every product and region without discussion. | Undefined rights need concrete terms and authorized review; enthusiasm alone does not grant exclusivity.
Which item meets the supplied qualification definition? | A prospect with a stated need, relevant contact, and agreed next step | A relevant contact who attended an event but has not identified a need | A company with a known need but no identified contact or next step | A scheduled introduction with no established customer need | All three stated elements are required. Attendance, an inferred need, or a meeting alone leaves part of the supplied qualification definition unmet.
How should the $5,000 be described? | An unapproved marketing-support request | A reimbursement guaranteed before review | Money already paid to the partner | Automatic compensation for every introduction | The brief supplies a request only, without authority to spend, reimburse, or pay it.
What should a pilot agreement clarify beyond lead targets? | Rights, product scope, territory, support roles, attribution, funding, and review | Only a friendly label for the relationship | Guaranteed revenue without customer orders | Permanent exclusivity hidden under a pilot title | A workable proposal needs the complete relationship boundaries and responsibilities, not a target alone.''',
    dialogue='''Chen | We could invest in this partnership, but our directors will ask what protects that investment. Would you consider exclusive rights?
Amina | Let us define the [[exclusivity::Exclusivity needs specified boundaries and authorized review; interest in partnering does not create a sole right.]] you have in mind. We have not identified the territory, products, duration, or contribution, and I cannot grant an exclusive right in this conversation.
Chen | We have experience introducing customers and helping with implementation. I have not decided whether we would also handle the commercial sale.
Amina | Then clarify the [[channel partner::The channel role may involve introductions, resale, or delivery; those activities carry different responsibilities that need agreement.]] activities first. Referrals, resale, and implementation are different roles. The proposal should say which you would perform and where our team would remain responsible.
Chen | A limited pilot could help us understand the relationship before either side makes a longer commitment.
Amina | We can assess a [[nonexclusive::Nonexclusive describes the proposed pilot rights; it does not mean the pilot or its other terms are already approved.]] six-month pilot. That is a proposal for review, not an executed agreement or a promise that every later commercial request will be accepted.
Chen | For the pilot, Region North would match our current contacts. We would focus on the scheduling product rather than the full catalog.
Amina | That makes the [[product scope::The proposed product scope is scheduling only, paired with Region North and the six-month term.]] and territory more concrete. We should record both, so the pilot is not later described as covering every product or a broader geographic area.
Chen | What contribution would you expect us to demonstrate during that period? I would prefer a measure we can understand and document.
Amina | The proposed [[performance target::The proposed target is four qualified opportunities per quarter, not a guaranteed number of purchases.]] is four qualified opportunities per quarter. We need a clear definition so the count reflects meaningful customer engagement rather than a list of names.
Chen | We can identify a customer need, the relevant contact, and an agreed next conversation. That does not mean the customer has decided to buy.
Amina | Correct. A [[qualified opportunity::Qualification here requires need, contact, and an agreed next step; it does not establish an order or revenue.]] meets those three conditions in this proposal. It is not a signed order, and we should not turn the target into a promise of bookings or cash receipts.
Chen | Some prospects may already be talking with your direct sales team. We should avoid approaching them with conflicting offers.
Amina | We need a [[deal registration::Deal registration records partner opportunities under agreed rules so overlapping work and account claims can be handled consistently.]] process and channel-conflict rules. Agree how overlapping accounts are handled and how each party learns the current status before making commitments to a customer.
Chen | Joint opportunities will also need a fair way to recognize who contributed. An introduction and implementation support are not the same activity.
Amina | Define the [[attribution rules::Attribution rules establish credit for the actual contributions, rather than allowing competing assumptions about ownership or compensation.]] explicitly. Credit, customer communication, and any compensation should follow the agreed arrangement rather than a general claim that the account belongs to one side forever.
Chen | We have a five-thousand-dollar launch campaign in mind. Do we need funding approval before booking it, or can we send you the receipts afterward?
Amina | No. The [[MDF::Market development funds are only requested here; the five-thousand amount has not been approved for spending or reimbursement.]] request is not approved. We need the activity, budget, conditions, and authorization assessed before you assume that our company will fund or reimburse it.
Chen | Before launch, we also need to know who supports customers and how we review the partnership at the end of the six months.
Amina | Include the [[support handoff::The support handoff defines who assists customers and when responsibility changes, alongside the pilot's review arrangements.]], enablement, and renewal-review arrangements in the full proposal. Then the required commercial and legal review can assess the actual relationship before anyone promises rights, spending, or ongoing commitments.''',
    rehearsal=('Read Chen and Amina aloud, then swap roles. Clarify referrals, resale, and implementation before discussing exclusive rights.', 'Check all ten gaps. Reread the six-month, Region North, scheduling-product proposal and its four-opportunity quarterly target.', 'Repeat the full-proposal close with support, attribution, marketing funding, and review arrangements. Keep all proposed rights and spending unapproved.'),
    transfer_title='Describe another proposed channel pilot',
    transfer_setup='A proposed pilot is nonexclusive, lasts four months, covers the inventory product in Region West, and targets three qualified opportunities per quarter. No agreement or marketing funding has been approved.',
    transfer='''Manager: "The proposed rights are ___." | nonexclusive | The proposal does not grant a sole selling right in the stated pilot arrangement.
Partner: "The proposed term is ___." | four months | Four months defines the proposed pilot duration, not a permanent appointment.
Manager: "The product scope is the ___." | inventory product | The proposal names one offering rather than the entire catalog.
Partner: "The quarterly opportunity target is ___." | three | Three qualified opportunities is the proposed contribution target, not a guarantee of signed orders.''',
))


BOOK['units'].append(unit(
    title='CRM Hygiene and Pipeline Reviews',
    scene='The forecast date is the seller estimate, not a customer promise',
    skill='Correct stages, dates, amounts, and forecast confidence using customer evidence rather than seller hopes.',
    brief='Opportunity H27 concerns a $120,000 twelve-month subscription plus a separate $20,000 setup fee. Seller Mika records 31 October as the close date, selects Contracting, and puts the deal in Commit. The customer has attended a demonstration and expressed interest, but procurement has not started and no signing date is confirmed. Under this fictional team policy, Contracting requires procurement to have started; Commit requires a customer-confirmed signing window and a documented approval path. Evaluation fits the demonstrated current status. Manager Jonas asks Mika to correct the record and verify buying steps with the customer by Monday at 14:00 Eastern.',
    cast='Mika | Account executive\nJonas | Sales manager',
    culture=('A forecast correction is useful information', 'Sales pressure can make an evidence-based downgrade feel like personal failure. Treat the correction as a way to expose the next customer task and improve planning. Do not punish honesty by demanding an invented date or confuse removal from a commitment category with abandonment of the opportunity.'),
    a='''Who supplied the 31 October close date? | Mika entered it as a seller estimate. | The customer confirmed it as a signing commitment. | Procurement approved it after completing review. | Both parties signed an order with that date. | The date is seller-entered and has no customer-confirmed signing basis.
Why is Contracting unsupported under the stated policy? | Procurement has not started. | The customer never saw a demonstration. | The subscription has no stated amount. | Evaluation automatically means a lost deal. | This team's Contracting condition requires procurement to have begun, which the supplied facts say has not happened.
What is Mika required to do by Monday at 14:00 Eastern? | Verify the buying steps with the customer | Guarantee the signature | Recognize all subscription revenue | Delete the opportunity as lost | The follow-up is to establish the customer process, not to promise an unsupported commercial or accounting outcome.''',
    vocabulary='''CRM | Customer relationship management; systems and practices for maintaining customer and opportunity information. | update the CRM
opportunity | A potential sale tracked under the team's defined criteria. | maintain the opportunity record
stage exit criterion | Evidence required before an opportunity moves beyond a defined sales stage. | verify stage exit criteria
forecast category | A grouping indicating how a deal is treated in the forecast. | review the forecast category
Commit | A team's high-confidence forecast category, whose specific requirements must be defined. | substantiate Commit status
best case | A forecast scenario or category for possible outcomes under the team's rules. | qualify the best-case estimate
pipeline | The set of tracked potential sales and their progress. | review the pipeline
pipeline coverage | Potential pipeline value relative to a defined sales target or other stated basis. | define pipeline coverage
weighted pipeline | Opportunity values adjusted by assigned probabilities under a specified model. | interpret weighted pipeline
close date | The recorded expected or actual completion date, with its status specified. | verify the close date
buyer-confirmed date | A date explicitly confirmed by the relevant customer role for the stated event. | record a buyer-confirmed date
stage age | Time an opportunity has spent in its current stage. | monitor stage age
sales velocity | A defined measure of how quickly sales opportunities generate results. | define sales velocity
slippage | Movement of an expected completion beyond the previously forecast period. | explain forecast slippage
stale opportunity | A deal record lacking current evidence or meaningful progress under the team's criteria. | review stale opportunities
next-step owner | The person responsible for a specified follow-up action. | identify the next-step owner
loss reason | The documented reason an opportunity did not proceed, where known. | record the loss reason
Closed Won | A completed-sale status used according to the organization's defined completion conditions. | verify Closed Won criteria
bookings | Contracted sales value measured under the organization's specified rules. | distinguish bookings
recognized revenue | Revenue recorded under the applicable accounting rules, distinct from forecasts or cash receipts. | separate recognized revenue
audit trail | A record of changes, sources, and decisions over time. | preserve the audit trail
forecast snapshot | A dated record of the forecast at a particular point. | retain a forecast snapshot
mutual action plan | Agreed customer and seller steps, owners, and timing. | validate the mutual action plan
recurring value | Value from repeating charges, with term and measurement rules specified. | define recurring value''',
    precision='The $120,000 subscription and $20,000 setup fee total $140,000 before any unmentioned taxes or adjustments, but they are different charge types. A forecast field must identify what it includes. None of these quoted amounts is automatically a booking, cash receipt, or recognized revenue.',
    precision_extra='Contracting and Commit have explicit fictional requirements in this lesson. Other organizations may define their categories differently. Here the missing procurement start, confirmed signing window, and approval path require correction; they do not prove that the customer will never buy.',
    phrases='''State the evidence | The customer attended the demonstration and expressed interest.
Identify the unsupported date | The thirty-first of October is our estimate, not a confirmed signing date.
Check the stage | Procurement has not started, so Contracting does not meet our stated rule.
Use the supported stage | Evaluation reflects the evidence currently available.
Check the category | Commit requires a confirmed signing window and a documented approval path.
Avoid converting enthusiasm | A positive comment is not a purchase commitment.
Preserve the opportunity | Removing it from Commit does not mean marking it lost.
Clarify the amount | Separate the twelve-month subscription from the one-time setup fee.
Avoid revenue confusion | A quote in the pipeline is not recognized revenue.
Name the missing customer action | We need to verify procurement steps, approvers, and timing.
Assign ownership | Mika owns the customer follow-up.
Set the deadline | Verify the buying steps by Monday at fourteen hundred Eastern.
Label estimates honestly | Any retained internal target must remain clearly marked as unconfirmed.
Keep history | Record why the stage and forecast treatment changed.
Use evidence in the next review | Bring the customer's actual response, including any remaining unknowns.
Close the correction | Update the stage, forecast category, amount basis, next step, owner, and evidence date.''',
    notes='''Our estimate | Attributes the date to the seller rather than the buyer.
Under our rule | Refers to this team's defined category requirements.
Currently available | Leaves room for later evidence without inventing it now.
Does not mean lost | Separates forecast confidence from the opportunity's continued existence.
Amount basis | States which charges and period a field includes.
Actual response | Keeps the follow-up tied to customer evidence rather than internal optimism.''',
    d='''Which correction fits the stated policy? | Move to Evaluation and remove unsupported Commit treatment while keeping the opportunity active. | Keep Contracting because the seller wants a strong month. | Mark Closed Won after a favorable demonstration. | Delete the record as lost without customer evidence. | Evaluation matches the known progress, while the missing approval and timing evidence fails the defined Commit conditions.
Which amount statement is accurate? | The quote has $120,000 subscription plus $20,000 setup; the recorded field must state its basis. | The $120,000 necessarily includes every first-year charge. | All $140,000 is already recognized revenue. | A setup fee is recurring subscription value by definition. | Charge types and field definitions must remain clear, and a quote does not establish completed sales or accounting revenue.
What should happen to an internal target date? | Label it as an unconfirmed estimate and distinguish it from a customer commitment. | Attribute it to the customer without asking. | Treat it as proof procurement has started. | Change the notes to claim a signed order. | An internal planning estimate may be recorded as such, but its source and uncertainty must not be disguised.
Which next update is useful? | Customer-confirmed buying steps and remaining gaps, with the evidence date | A larger probability chosen to satisfy the target | The same unsupported date without new information | A claim that every interested prospect closes immediately | The next review needs actual process evidence rather than a revised number unsupported by customer progress.''',
    dialogue='''Jonas | I see H27 in Commit for October thirty-first, with Contracting as the stage. Walk me through what the customer has actually confirmed.
Mika | The customer liked the demonstration, but I entered the [[close date::The close date is Mika's estimate, not a signing date confirmed by the customer.]] myself. Procurement has not started, and I do not have a confirmed signing window. I was using the month-end date as an internal target.
Jonas | Then we need to separate the customer response from our planning estimate. Which stage reflects what has actually happened?
Mika | Under our [[stage exit criteria::The team requires procurement to have started before Contracting; the known demonstration status fits Evaluation instead.]], Evaluation fits the evidence. Contracting requires procurement to have started, so the current stage is ahead of the customer process rather than a record of completed progress.
Jonas | Commit also has a specific definition. It needs a customer-confirmed signing window and a documented approval path, neither of which we have.
Mika | I will correct the [[forecast category::The forecast category must reflect the stated evidence requirements; positive feedback does not support Commit here.]] and remove the unsupported Commit treatment. The opportunity can remain active while I establish those missing facts; correcting the forecast does not require calling the deal lost.
Jonas | Good. I need a forecast grounded in the buying process, not just a favorable response to the demonstration.
Mika | The [[pipeline::The pipeline can retain a live opportunity without treating it as committed or completed revenue.]] should show the interest and the unresolved buying steps separately. A positive response is useful, but it is not an approved purchase, an executed order, or a completed procurement process.
Jonas | Check the amount as well. The quote has a twelve-month subscription of one hundred twenty thousand and a separate twenty-thousand setup charge.
Mika | I will clarify the [[recurring value::Recurring subscription value is distinct from the one-time setup charge; the forecast field needs a clear inclusion basis.]] and the one-time amount. If a field shows only the subscription, its definition should say so, rather than appear to include every first-year charge.
Jonas | And neither the quoted subscription nor the combined amount should be described as revenue already earned from this opportunity.
Mika | Correct. [[Recognized revenue::Recognized revenue follows applicable accounting rules and is not established by a quote, forecast category, or positive customer comment.]] is separate from a quote or forecast. I should also avoid calling the opportunity a booking or cash receipt before the relevant event and definition support that description.
Jonas | What will you ask the customer next? We need to know the steps and owners rather than request a signature date in isolation.
Mika | I will propose a [[mutual action plan::A mutual action plan requires agreement on actual customer and seller steps, not a timetable imposed by the seller.]] after verifying the procurement process, approval path, and realistic timing. It should reflect their actual decisions and dependencies, not a seller schedule presented as already agreed.
Jonas | Please verify those buying steps by Monday at fourteen hundred Eastern and bring the response to the next review.
Mika | I am the [[next-step owner::Mika owns the customer follow-up by the stated deadline; that action does not guarantee a signed purchase.]]. I will record the response and any unresolved items. The commitment is to verify the process, not to guarantee a customer signature by that time.
Jonas | Please leave a note explaining the correction. I do not want the next reviewer to read this as a customer withdrawal when we are fixing our own forecast.
Mika | I will preserve the [[audit trail::The audit trail records the evidence-based correction and its reason, rather than rewriting history to imply earlier customer confirmation.]]. The stage and category are changing because the previous entries lacked the required evidence, not because the customer has said it will never buy.
Jonas | At the next review, use the new evidence to reassess confidence. Do not change a probability just to preserve the total.
Mika | I will retain the [[forecast snapshot::A forecast snapshot preserves what was estimated at a particular time, including corrections and uncertainty rather than invented certainty.]] with the amount basis, stage, next action, and evidence date. Any internal target will remain unconfirmed, not attributed to the customer.''',
    rehearsal=('Read Jonas and Mika aloud, then swap roles. State which evidence supports Evaluation and which evidence is missing for Commit.', 'Correct all ten gaps. Reread the recurring subscription, setup fee, and recognized-revenue distinctions.', 'Repeat Mika\'s Monday follow-up commitment and correction record without marking the active opportunity lost or attributing the seller\'s date to the customer.'),
    transfer_title='Correct another unsupported forecast',
    transfer_setup='A seller enters 30 November as a close date after an encouraging demonstration. The buyer has not confirmed the date, and required approval steps are unknown. The team needs customer evidence before treating the deal as committed.',
    transfer='''Manager: "The entered date is ___." | 30 November | This is the seller-entered date in the record, not an independently confirmed customer commitment.
Seller: "The customer has attended a ___." | demonstration | The demonstration is the stated progress evidence, not a signed or approved purchase.
Manager: "The date's current status is ___." | unconfirmed | The buyer has not confirmed the date, so it must remain an estimate.
Seller: "Before commitment treatment, we need ___." | customer evidence | The team's requirement is evidence of the buying process and timing, not enthusiasm alone.''',
))
