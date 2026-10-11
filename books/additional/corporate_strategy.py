"""Additional strategic discussions with distinct commercial decisions."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='A competitor cuts price, but not on the same offer',
        skill='Challenge a reactive pricing proposal using a like-for-like comparison.',
        setup='A competitor publicly advertises a price 15% below the company\'s current package. Its advertised package excludes implementation and priority support, both included in the company\'s offer. Three prospects mentioned the advertisement; none has yet confirmed a purchasing decision. No pricing response is approved.',
        cast='Bea|Commercial director\nNikhil|Strategy manager',
        dialogue='''Bea|The competitor's new price is fifteen percent lower. Sales wants us to match it before we lose the pipeline.
Nikhil|Before we respond, is that a [[like-for-like comparison::A like-for-like comparison aligns the included services and conditions rather than comparing headline prices alone.]]? Their public page excludes implementation and priority support.
Bea|Those are in our package. Customers may still react to the first number they see.
Nikhil|I agree. We need a clear comparison for the sales team, not a claim that price cannot matter.
Bea|Three prospects raised the advertisement this week. That feels like a warning we should take seriously.
Nikhil|Yes, as a signal. It is not yet evidence of [[customer switching::Customer switching means customers actually move to another provider; mentioning an advertisement does not establish that outcome.]] or three lost deals.
Bea|Would you leave the offer untouched until we have lost someone? That seems slow.
Nikhil|No. We can review recent objections and test how buyers value each service while we compare bounded response options.
Bea|One option is a lower-priced package without priority support, rather than cutting the full package.
Nikhil|Then examine [[cannibalization::Cannibalization occurs when a new offer displaces sales of the company's existing offer rather than generating only additional business.]]. Existing customers might trade down, so not every sale would be incremental.
Bea|Sales also proposed a temporary discount for new accounts. They think it would preserve the current package architecture.
Nikhil|Model the [[price realization::Price realization is the price actually obtained after relevant discounts and concessions, not simply the published list price.]] and what happens at renewal. A temporary discount can shape expectations beyond its stated period.
Bea|Our implementation team is already busy. Adding low-margin accounts could make the higher-value service worse.
Nikhil|That is an important [[capacity constraint::A capacity constraint is a delivery limit that can make an otherwise attractive sales response operationally unworkable.]]. Include delivery demand and customer impact in the comparison, not just signed revenue.
Bea|A trade-association colleague knows their commercial director. Could we ask whether the cut is likely to last?
Nikhil|Do not seek confidential future pricing from a competitor. Use lawful public information and route any proposed competitor contact through legal review.
Bea|For Friday, I need a recommendation that the team can act on, not twenty equally weighted possibilities.
Nikhil|I will compare holding the package, a bounded offer test, and revised packaging against the same [[decision criteria::Decision criteria provide the common basis for comparing options, including contribution, customer value, and delivery feasibility here.]].
Bea|Include the evidence that would change your recommendation. I can arrange structured follow-up with the three prospects.
Nikhil|Good. We will report their actual concerns and decisions, then recommend the smallest justified response rather than assume every headline requires a price match.''',
        transfer_title='Three objections become three supposed lost accounts',
        transfer_setup='Three customers ask about a competitor\'s price. No cancellation or supplier change has been confirmed.',
        transfer='''Commercial lead: These are price objections, not confirmed customer ___.|losses|The customers asked questions; no cancellation or change of supplier is established.
Strategist: Check the package contents before comparing the headline ___.|prices|Differences in included services can make headline prices an incomplete comparison.
Commercial lead: We can test an offer without promising a permanent ___.|reduction|A bounded test does not establish a permanent change in the company's prices.
Strategist: Record the test limits and the evidence needed for a wider ___.|decision|Further action should depend on the defined test evidence and authorized decision process.'''),
    scenario(
        title='Closing a product line does not close its obligations',
        skill='Discuss an orderly business exit while separating avoidable costs from continuing obligations.',
        setup='A product line has low new sales and ongoing customer contracts. A proposal assumes that stopping new orders next month eliminates all its costs immediately. Shared platform costs, customer support obligations, migration options, and contract terms have not been reviewed. The meeting is to frame the exit analysis, not announce a closure.',
        cast='Omar|Portfolio lead\nClare|Operations director',
        dialogue='''Omar|The proposal says we can stop taking new orders next month and remove the entire product cost base.
Clare|Stopping new sales is one decision. Ending service is another. What [[exit obligations::Exit obligations are responsibilities that continue during or after withdrawal, such as contractual support commitments.]] have been included in that estimate?
Omar|None yet. The analyst used the product's allocated costs as the expected saving.
Clare|Then we need to separate costs that actually disappear from those that move elsewhere in the company.
Omar|The shared platform is the biggest allocation. Other products will still use it after this line stops selling.
Clare|That may leave [[stranded costs::Stranded costs remain after the associated activity is reduced or stopped rather than becoming immediate savings.]]. Removing an accounting allocation does not remove the supplier bill.
Omar|Some customers have another eighteen months on their contracts. We need counsel to review the actual commitments.
Clare|And a [[run-off plan::A run-off plan manages existing commitments while new business is reduced or stopped over time.]] for service, staffing, renewals, and communication while those commitments are resolved.
Omar|Could we migrate everyone to the newer product and close the old one sooner?
Clare|Only if it fits their needs and the terms allow the proposed approach. We have not assessed feature gaps, data movement, or customer consent.
Omar|Then migration is an option to evaluate, not a saving we can put in the base case today.
Clare|Correct. Its [[transition costs::Transition costs are the resources needed to move from the current arrangement to the proposed future one.]] may arrive before any operating savings, so show their timing.
Omar|We also need to avoid losing customers who buy several of our products. This is not an isolated revenue stream.
Clare|Map that exposure account by account. A [[cross-sell::Cross-sell involves selling different products to the same customer; exiting one product can affect the broader relationship.]] assumption is not a guarantee that those other relationships remain unaffected.
Omar|Who should speak to the customer teams first? Rumors could get ahead of the analysis.
Clare|Use a small authorized working group now. We need a communication sequence before an external announcement, with no suggestion that closure is already approved.
Omar|For the recommendation, I will compare maintaining the line, stopping new sales with a run-off, and an assessed migration route.
Clare|Use a common time horizon and show [[avoidable costs::Avoidable costs are future costs that the chosen option can actually prevent, unlike allocations or continuing commitments.]], retained obligations, and the main customer risks for each.
Omar|That will probably reduce the headline saving, but it gives the committee a decision it can actually implement.
Clare|And it tells the service team what must continue. An exit decision needs an operating plan, not just a deleted revenue line.''',
        transfer_title='A cost allocation disappears from a spreadsheet',
        transfer_setup='A discontinued service used 20% of a shared software platform. The platform contract continues at the same total price for the remaining services.',
        transfer='''Analyst: Removing the discontinued service's allocation does not reduce the supplier ___.|bill|The supplier's total contractual charge remains unchanged in the supplied facts.
Director: Show that amount as a continuing cost, not an immediate ___.|saving|A saving requires a real reduction in future cost, which is not established here.
Analyst: We can investigate a lower contract tier at the next ___.|renewal|Renewal is a possible opportunity to review terms, not a saving already obtained.
Director: Keep that possibility separate from the committed ___.|baseline|The baseline should preserve the actual continuing arrangement until a change is justified.'''),
    scenario(
        title='A distribution partnership with unclear decision rights',
        skill='Negotiate the operating boundaries of a strategic partnership before endorsing exclusivity.',
        setup='A distributor requests two-year regional exclusivity without a minimum purchase commitment. Data access, brand approvals, performance measures, and exit terms are unresolved. The strategy lead and channel director are preparing negotiation questions; neither may sign.',
        cast='Anya|Strategy lead\nMateo|Channel director',
        dialogue='''Mateo|The distributor can put us in front of customers we cannot reach ourselves. They want a two-year exclusive arrangement.
Anya|What exactly would [[exclusivity::Exclusivity limits the parties' ability to use other routes within a defined scope; its territory, products, and duration must be specified.]] cover: the territory, a product range, a customer segment, or every route to market?
Mateo|Their draft says the whole region, but it does not distinguish existing accounts from new ones.
Anya|Then that is an open commercial term. We should not evaluate the proposal as though our existing direct relationships are unaffected.
Mateo|They have not offered a minimum purchase commitment. They say market development takes time.
Anya|It may. But what [[performance milestones::Performance milestones are defined results or stages used to assess whether the partnership is delivering its intended value.]] would justify retaining exclusive rights over that period?
Mateo|We could discuss qualified account coverage, trained sales staff, and agreed sales measures rather than a single first-month number.
Anya|Yes, with definitions and evidence. We need to distinguish activity from completed business and avoid targets that encourage poor-fit sales.
Mateo|The draft also lets them adapt marketing materials locally. I support that flexibility.
Anya|So do I, within clear [[decision rights::Decision rights specify who can make which decisions, including which local adaptations need brand or legal approval.]]. Who approves product claims, pricing commitments, and use of the brand?
Mateo|That is unresolved. We should map the decisions rather than require head-office approval for every spelling correction.
Anya|Agreed. Keep routine adaptation workable and identify the decisions that could create a material obligation or risk.
Mateo|They want to hold the customer records in their own system. Our service team needs enough information to support buyers.
Anya|Then define [[data access::Data access describes which information each party may use for specified purposes, subject to relevant permissions and protections.]], permitted uses, security responsibilities, and what happens when the partnership ends.
Mateo|If performance falls short, would we simply terminate? That could leave customers without support.
Anya|We need a reviewed [[exit mechanism::An exit mechanism sets out how the relationship may end and how ongoing responsibilities are handled.]], including any cure process, transition, and customer continuity. We cannot improvise that after a dispute.
Mateo|For the next meeting, I will bring their channel coverage and the unanswered commercial questions. What will you bring?
Anya|A comparison with a nonexclusive arrangement and a bounded pilot, including the control we retain and the capabilities each route requires.
Mateo|Then we are not rejecting the partner; we are testing whether the structure supports the strategy.
Anya|Exactly. The [[governance model::The governance model defines how the parties make decisions, review performance, and resolve issues during the relationship.]] is part of the value proposition, not paperwork to finish after signing.''',
        transfer_title='An exclusive right without a defined territory',
        transfer_setup='A draft grants exclusive distribution rights but leaves the territory and existing-account treatment unspecified. No signature is authorized.',
        transfer='''Channel lead: We need the geographic ___ before evaluating the restriction.|scope|The territory determines where the proposed exclusive right would apply.
Strategist: Also clarify whether existing accounts are inside or outside the ___.|arrangement|The treatment of current customers is an unresolved part of the proposed relationship.
Channel lead: I will request revised terms, not communicate an ___.|acceptance|Requesting clarification does not accept the unapproved contractual proposal.
Strategist: Compare the revised proposal with the nonexclusive ___.|alternative|The nonexclusive route provides a relevant alternative for evaluating the proposed restriction.'''),
]
