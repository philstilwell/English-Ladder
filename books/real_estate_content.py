"""Original real-estate communication cases for the expanded learner book."""
from books.authoring import unit

BOOK = dict(
    slug='real-estate', title='Real Estate English',
    cover_label='Clients / properties / transactions',
    cover_title='Real Estate', cover_size=36,
    tagline='Clarify the relationship. Explain the property. Keep each next step precise.',
    audience='For agents, brokers, leasing colleagues, property managers, and transaction coordinators.',
    map_intro='Follow eight conversations from the first representation question to property search, negotiation, closing, and ongoing service.',
    notes_title='Useful detail builds client confidence.',
    notes_intro='Property decisions combine money, deadlines, technical reports, and strong personal preferences. Clear English helps clients distinguish a listing claim from a verified fact, an offer from an agreement, and a progress update from permission to proceed.',
    field_notes=[
        ('Name whom you represent', 'Explain the actual professional relationship and its limits before discussing confidential strategy. Do not assume that providing information or arranging access answers the representation question.', '"Let us confirm the brokerage role and applicable agreement before discussing your negotiating limit."'),
        ('Translate preferences into criteria', 'Ask about the property, budget, travel needs, and other objective requirements. Let the client identify priorities rather than selecting neighborhoods through assumptions about who belongs there.', '"Which destination, transport method, and travel time should we use for the search?"'),
        ('Keep the source beside the fact', 'Attribute an observation to the inspection report, a measurement to its source, and a financing update to the lender. Coordination does not turn an agent into a technical diagnostician or final approver.', '"The report recommends specialist evaluation; it does not supply a repair diagnosis or price."'),
        ('Report the exact state', 'Requested, received, reviewed, and cleared are different milestones. A reassuring update names the open item, responsible professional, and next communication without guaranteeing an unfinished result.', '"The appraisal is received; the title questions remain open."')],
    scope_note='Fictional English practice using mainly US real-estate terminology, not legal, lending, valuation, engineering, or safety advice. Agency, advertising, disclosure, lease, and closing requirements vary. Actual transactions require current documents, local rules, authorized instructions, and appropriately qualified professionals.',
    sources=[
        dict(title='National Association of REALTORS. Consumer Guide: Agency and Non-Agency Relationships.', url='https://www.nar.realtor/the-facts/consumer-guide-agency-and-non-agency-relationships', note='Background on representation terminology and state-law variation. No particular relationship or fee arrangement is presumed for the fictional cases.', checked='10 October 2026'),
        dict(title='US Department of Housing and Urban Development. Housing Discrimination Under the Fair Housing Act.', url='https://www.hud.gov/helping-americans/fair-housing-act-overview', note='Background on US federal fair-housing protections. Practical language examples focus on objective property facts and consistent service; local requirements need separate verification.', checked='10 October 2026'),
        dict(title='Consumer Financial Protection Bureau. Closing on your new home.', url='https://www.consumerfinance.gov/owning-a-home/close/', note='Background on documents, professionals, and stages in a US mortgage closing. The teaching cases do not prescribe universal deadlines or approve a transaction.', checked='10 October 2026'),
        dict(title='American Society of Home Inspectors. Standard of Practice.', url='https://www.homeinspector.org/resources/standard-of-practice/', note='Background on inspection scope and recommendations for further evaluation. Actual scope depends on the applicable standard, agreement, and professional qualifications.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Agency, Representation, Compensation, and Trust', scene='Before the buyer shares a negotiating limit',
    skill='Clarify representation, confidentiality, and compensation without assuming an agreement already exists.',
    brief='Prospective buyer Lena asks licensee Ren whether Ren represents both sides of a property transaction. Their relationship has not been established or documented, and the brokerage role for the particular listing still needs confirmation. No fee terms have been agreed. Lena is about to disclose her maximum offer. Ren can explain the questions that must be settled and obtain the applicable documents and broker guidance, but must not promise unrestricted advocacy, a standard commission, or confidentiality beyond the actual relationship and applicable duties.',
    cast='Lena | Prospective buyer\nRen | Real-estate licensee',
    culture=('Clarify the role before inviting trust', 'A friendly conversation may sound like personal representation to a newcomer. Answer that concern directly and identify what needs confirmation. Do not encourage a negotiating disclosure while the professional role is unresolved, or substitute general reassurance for the actual terms and duties.'),
    a='''Which two issues should Ren clarify before discussing Lena's negotiating limit? | Whom the brokerage represents and the duties of that relationship | The seller's asking price and the property's bedroom count | The appraisal date and the lender's document checklist | The viewing schedule and the preferred closing day | Lena is about to share sensitive negotiating information, so representation and its duties are the immediate issue. The other pairs concern useful transaction details but do not resolve whom Ren represents.
What is Lena about to share? | Her maximum offer | A confirmed appraisal value | A final loan approval | The seller's authorized reserve price | The sensitive information identified in the briefing is Lena's negotiating limit.
What should Ren verify before describing the available arrangement? | The brokerage's role, local requirements, and applicable documents | A universal agency rule inferred from the property's price | A standard commission assumed to apply everywhere | A guarantee that one professional can advocate without limits for both parties | Available relationships and their duties depend on actual brokerage circumstances and applicable rules, not those assumptions.''',
    vocabulary='''agency | A legal representation relationship defined by applicable law. | clarify the agency relationship
principal | The person or entity represented by an agent. | identify the principal
fiduciary duty | A duty of loyalty or care arising in a relationship under applicable law. | explain applicable fiduciary duties
buyer representation | Acting for a buyer under an established relationship. | discuss buyer representation
seller representation | Acting for a seller under an established relationship. | confirm seller representation
dual agency | Representation of both sides where permitted and subject to applicable conditions. | review dual-agency restrictions
designated agency | An arrangement assigning different representatives within a brokerage where permitted. | explain designated agency
non-agency relationship | A permitted service relationship without an agency role. | clarify a non-agency relationship
transaction broker | A professional facilitating a transaction under a jurisdiction's non-agency framework. | verify the transaction-broker role
brokerage | The business through which real-estate services are provided. | identify the brokerage
managing broker | The broker responsible for supervision under the relevant structure. | consult the managing broker
representation agreement | A document setting out a representation relationship and terms. | review the representation agreement
listing agreement | An agreement for marketing or representing a property's seller. | examine the listing agreement
exclusivity | A contractual restriction on using other representatives within a stated scope. | clarify the exclusivity term
agreement term | The period during which an agreement operates. | confirm the agreement term
service scope | The work included in the professional engagement. | define the service scope
compensation | Payment for professional services on agreed terms. | negotiate compensation
commission | A form of compensation often linked to a completed transaction. | explain the commission basis
fee obligation | A contractual responsibility to pay a specified fee. | identify the fee obligation
informed consent | Agreement based on relevant information and understanding. | obtain required informed consent
conflict of interest | A competing interest that may affect professional judgment or duties. | disclose a conflict of interest
confidential information | Information subject to protection under applicable duties or terms. | handle confidential information
material fact | A fact important to a transaction or decision in context. | disclose a material fact
termination provision | Terms governing how an agreement may end. | review the termination provision''',
    precision='Providing access or information does not, by itself, explain whom a licensee represents. Ask for the actual relationship and its duties. Labels such as dual agency or transaction broker cannot be assumed available or identical across jurisdictions.',
    precision_extra='Who represents a party and who pays a fee are distinct questions. Compensation terms must be discussed in their actual contractual context. Do not call a fee legally standard, assume another party will pay it, or describe a negotiable term as already accepted.',
    phrases='''Address the question | We should clarify whom the brokerage represents before discussing your strategy.
Pause the disclosure | Please hold your maximum offer until we have clarified the relationship.
Name the missing fact | I need to confirm the brokerage's role for this listing.
Use the documents | Let us review the applicable agreement and disclosures.
Separate compensation | The representation role and fee obligations are distinct questions.
Avoid a universal claim | Available arrangements and duties depend on the applicable rules.
Preserve choice | We can explain the proposed terms before you decide whether to agree.
Close with verification | I will obtain the role information and broker guidance first.
Explain scope | The agreement should identify the services included.
Check the period | What dates and properties does this term cover?
Clarify exclusivity | Let us check what the exclusivity provision actually restricts.
Avoid a fee assumption | No compensation terms have been agreed in this conversation.
Identify the payer | The documents need to explain who owes which payment under what conditions.
Limit assurance | I cannot promise duties beyond the actual relationship and applicable requirements.
Invite a precise question | Which part of the proposed arrangement would you like clarified?
Confirm understanding | Does this explanation distinguish representation from payment?''',
    notes='''Represents versus assists | Assistance describes an action; representation describes a professional legal relationship.
Before | Use before to sequence clarification ahead of a sensitive disclosure.
May be permitted | This phrase preserves jurisdictional variation rather than promising universal availability.
Agreed versus proposed | A discussed fee is not necessarily an accepted contractual obligation.
Scope and term | Scope concerns what is covered; term concerns the duration.
Who pays | Payment source alone should not be used as a complete description of representation duties.''',
    d='''Which response best addresses Lena's immediate concern? | Let us confirm the brokerage role before you share your maximum offer. | Tell me the limit first, and we can define representation later. | A friendly conversation means I represent you exclusively. | Anyone who opens a property represents both parties. | Clarifying the unresolved relationship first protects the discussion from unsupported assumptions about advocacy and confidentiality.
Which fee statement is accurate? | No fee terms are agreed yet; we need to review the actual proposal. | A legally fixed national commission applies to every transaction. | The seller has already agreed to cover every buyer fee. | Discussing compensation means Lena has accepted it. | The case supplies no agreed fee or payer commitment, so only the proposed terms can be reviewed.
Which question separates two issues correctly? | Whom do you represent, and what payment obligations would the agreement create? | Does any fee automatically make you everyone's agent? | Can a payment replace every required disclosure? | Is a showing identical to unrestricted buyer advocacy? | Representation and compensation are related but distinct questions that require their own facts and terms.
Which next step fits Ren's role? | Obtain the applicable documents and managing-broker guidance. | Invent a local rule to avoid delaying the conversation. | Promise that dual agency is always permitted. | Treat the prospective buyer's silence as full consent. | The briefing authorizes explanation and verification rather than unsupported legal claims or assumed agreement.''',
    dialogue='''Lena | Before I tell you the highest price I could offer, can you explain whether you represent me, the seller, or both sides of this property?
Ren | Let us clarify the [[agency::Agency identifies the representation relationship and its duties; the current conversation has not yet established it.]] question first. Our relationship is not established, and I need to confirm the brokerage's role for this particular listing before describing the available arrangement.
Lena | I assumed that because you were answering my questions, you would automatically negotiate only for me. I do not want to misunderstand that.
Ren | Answering questions does not settle the [[buyer representation::Buyer representation requires clarity about the actual relationship; providing information alone does not answer whom the professional represents.]] question. Please hold your negotiating limit until we have explained the role, duties, and relevant documents properly.
Lena | If your office is connected with the seller, would that mean you can simply represent both of us without changing anything?
Ren | We cannot assume that. [[dual agency::Dual agency concerns both-side representation, with availability and conditions depending on applicable law rather than convenience.]] is treated differently across jurisdictions, and any permitted arrangement has conditions and limits that need to be explained before a decision.
Lena | Can someone in your office confirm the arrangement for this listing? I need to know whom I can speak to before discussing my limit.
Ren | I will consult the [[managing broker::The managing broker provides relevant supervisory guidance about the brokerage's role and applicable process.]] and obtain the listing-role information. Then we can discuss the actual options instead of implying that an unresolved relationship already exists.
Lena | When we review the paperwork, I also want to know what work is included. Does the agreement cover the whole search or just this property?
Ren | The [[service scope::Service scope defines the included work or properties; it must be read from the actual proposed terms.]] should answer that, along with any limits. We need to read the proposed terms rather than assume every conversation creates the same package of services.
Lena | And if I wanted to talk to another agent later, would there be a restriction? I have not agreed to anything exclusive today.
Ren | We would review the [[exclusivity::Exclusivity concerns contractual restrictions on using other representatives; none should be assumed accepted in this unresolved discussion.]] provision, if one is proposed, and its exact reach. Your question should be answered before you decide whether those terms suit you.
Lena | I also hear different things about commissions. Is there one standard amount that the law makes everyone pay, regardless of the services?
Ren | Do not assume a fixed universal amount. [[compensation::Compensation is payment for services under agreed terms; the conversation supplies no legally fixed rate or accepted fee.]] needs a clear discussion of the proposed terms. We have not agreed a fee, a payment basis, or who would owe it.
Lena | If another party offers to contribute, does that automatically mean I have no obligation under an agreement I might sign?
Ren | Not automatically. The [[fee obligation::The fee obligation depends on the actual agreement and payment conditions, not an assumed contribution by another party.]] needs to be explained using the actual documents and conditions. A possible contribution and your contractual responsibility are not interchangeable statements.
Lena | I would like time to read the terms, including when the agreement ends and what would happen if I wanted to stop working together.
Ren | We should review the [[termination provision::The termination provision addresses ending the agreement; it differs from simply assuming a conversation can cancel all terms.]] as well as the duration. I can explain the proposal within my role and direct legal-interpretation questions to qualified counsel when needed.
Lena | Please send the proposed terms and confirm your office's role. I will wait to discuss my maximum offer until those questions are answered.
Ren | Correct. Any required [[informed consent::Informed consent depends on relevant information and understanding; silence or an introductory discussion should not be treated as complete agreement.]] must follow a clear explanation of the actual arrangement. Today I will obtain the missing information, not promise unrestricted advocacy before the relationship is settled.''',
    transfer_title='A fee discussion is not an agreement',
    transfer_setup='A prospective seller receives a proposed service package and fee. They ask for a shorter term. The brokerage has not accepted the change, and the proposal is unsigned.',
    transfer='''Seller: "I am requesting a shorter agreement ___." | term | The seller's request concerns duration rather than a completed change to the service package.
Broker: "That is a proposed ___, not an accepted one." | change | The briefing says the brokerage has not accepted the requested alteration.
Seller: "The document remains ___." | unsigned | The supplied facts state that no signature has been added to the proposal.
Broker: "We should confirm the final terms before recording an ___." | agreement | Discussion and a requested revision do not establish acceptance of the final contractual terms.''', rehearsal=["Check the cloze key, then read Lena and Ren's exchange. Pause before Lena's maximum-offer question; stress Ren's words that leave the relationship unresolved.","Switch roles and reread turns 9-20. Keep service scope, exclusivity, compensation, and termination as separate questions; do not invent agreed terms.","Complete the shorter agreement exchange and check its key. Read it with the proposed shorter term still unsigned and unaccepted."]))


BOOK['units'].append(unit(
    title='Client Intake, Needs Analysis, and Property Search', scene='Turning good neighborhood into a usable search',
    skill='Replace vague preferences with client-defined property and travel criteria without assuming affordability or belonging.',
    brief='Buyer Cam asks agent Imani for a "good neighborhood" and a "short commute." Cam identifies a weekday 9 a.m. destination at Central Clinic, public transport, a target journey of no more than 35 minutes door to door, two bedrooms, and a step-free entrance. Cam proposes a $450,000 asking-price search cap, but lender qualification and the total ownership budget remain unverified. Imani must build a search from these criteria, check property claims, and avoid promising a commute time or deciding which community suits Cam.',
    cast='Cam | Buyer\nImani | Buyer\'s agent',
    culture=('Let the client define fit', 'A broad request invites useful questions, not assumptions about the client\'s background. Ask which features and travel needs matter, then supply objective information consistently. Treat accessibility details as specific property facts to verify rather than replace them with a vague label such as suitable for everyone.'),
    a='''What commute basis did Cam specify? | Public transport, door to door, arriving for 9 a.m. on weekdays | Driving time at midnight between neighborhood boundaries | Walking time from the nearest station only | Any transport method with no arrival time | The briefing supplies transport mode, full-journey scope, destination, and weekday arrival time.
What does $450,000 represent here? | A proposed asking-price search cap | Confirmed lender approval | A verified total ownership budget | A guaranteed accepted offer | The amount is a client-defined search filter, while financing qualification and total costs remain unverified.
Which property requirements are stated? | Two bedrooms and a step-free entrance | Three bedrooms and a guaranteed school place | A detached house with no ownership charges | A renovated kitchen and a private garage | The supplied needs are two bedrooms and step-free entry; the other features have not been requested.''',
    vocabulary='''needs analysis | A structured clarification of a client's requirements and priorities. | conduct a needs analysis
search criterion | A condition used to select possible properties. | refine the search criteria
must-have | A requirement the client treats as essential. | identify the must-haves
preference | A desired feature that may be negotiable. | rank property preferences
trade-off | A compromise between competing priorities. | explain a trade-off
search radius | The geographic distance used to limit a property search. | define the search radius
door-to-door journey | Travel including the full route between actual start and destination. | estimate the door-to-door journey
peak-hour travel | Travel during a period of high demand. | check peak-hour travel
walkability | The practical ease of reaching relevant destinations on foot. | assess walkability using specific routes
transport interchange | A point where a traveler changes services or transport modes. | check the transport interchange
step-free access | Access along a route without steps, subject to exact route details. | verify step-free access
clear opening width | The unobstructed width available through an opening. | confirm the clear opening width
floor plan | A drawing showing a property's layout. | review the floor plan
asking-price cap | An upper advertised-price filter for a search. | set an asking-price cap
purchase budget | The amount available or intended for the purchase on a stated basis. | clarify the purchase budget
ownership costs | Ongoing costs associated with holding and using a property. | estimate ownership costs
property tax | A tax assessed on property under applicable rules. | check the property-tax estimate
association dues | Recurring charges imposed by a relevant owners' association. | verify association dues
special assessment | An additional charge for a particular association or public purpose. | ask about special assessments
insurance premium | The price of an insurance policy for a stated period. | obtain an insurance-premium estimate
utility cost | Expense for services such as electricity, gas, or water. | compare utility costs
prequalification | A preliminary lender assessment whose scope and verification vary. | clarify the prequalification basis
preapproval | A lender's conditional preliminary approval subject to its terms. | review preapproval conditions
shortlist | A selected group of options for closer review. | build a property shortlist''',
    precision='A short commute needs a destination, arrival time, mode, and journey boundary. A station-to-station estimate omits walking and waiting. A current route estimate is also not a guarantee of future service or an exact daily travel time.',
    precision_extra='A price filter does not establish financing or total affordability. Recurring taxes, insurance, association charges, utilities, and possible assessments may matter. Keep a listing\'s access description provisional until the exact entrance route and relevant measurements have been checked.',
    phrases='''Clarify the adjective | What specific features would make the area work well for you?
Define the journey | Are we measuring door to door for a weekday 9 a.m. arrival?
Confirm transport | You plan to use public transport rather than drive.
Separate priorities | Which requirements are essential, and which are preferences?
Record the access need | We will use a step-free entrance as a requirement to verify.
Limit the price claim | The search cap is not confirmation of financing or total affordability.
Check the route | We should include walking, waiting, and any interchange.
Close with a shortlist | I will compare properties against your stated criteria.
Preserve client choice | I can supply objective information; you decide which location fits.
Verify the listing | Let us confirm the access route rather than rely on a broad label.
Check extra costs | We still need the taxes, insurance, and association-charge estimates.
Avoid a guarantee | The journey estimate may vary with service and time.
Clarify the source | Is that travel time from the transit provider or the listing description?
Mark an unknown | The lender's qualification decision is not yet verified.
Use the same standard | We will apply the agreed criteria consistently across the search.
Invite correction | Please correct any requirement I have recorded inaccurately.''',
    notes='''Good for whom | Replace an undefined evaluation with the client's objective needs.
No more than | This expression sets a ceiling, not an average or approximate aspiration.
Door to door | Specify both endpoints so the same words produce comparable estimates.
Step-free | This describes a route feature and does not automatically establish every accessibility need.
Cap versus approval | A search limit is an instruction about filtering, not a lender's decision.
Could fit | Use this provisionally while relevant property or cost facts remain unchecked.''',
    d='''Which question best clarifies neighborhood fit? | Which property features and travel needs should guide the search? | Which background should the neighbors have? | Should I select the area based on where people like you usually live? | Can I treat good as a universal rating? | The question seeks the client's practical criteria rather than substituting demographic assumptions or an undefined judgment.
Which journey estimate is comparable with Cam's target? | Door-to-door public transport for the stated weekday arrival time | A station-to-station time with walking excluded | An off-peak drive with no waiting time | A map distance without transport information | The door-to-door public-transport estimate matches the required route, mode, and arrival time. The alternatives omit or change a required condition.
How should an unverified access claim be described? | The listing says step-free entry; we need to verify the actual route. | The property meets every possible access requirement. | Step-free means no measurements are needed. | A floor plan proves that all entrances are usable. | Attribution and verification preserve the distinction between a listing statement and a confirmed property feature.
Which budget statement is accurate? | $450,000 is a search cap; financing and ownership costs remain open. | $450,000 is confirmed borrowing capacity. | An asking price includes every future ownership charge. | A search cap guarantees the seller will accept that amount. | The briefing defines a search filter and explicitly leaves financing and total costs unverified.''',
    dialogue='''Cam | I want a good neighborhood and a short commute, but I realize that may not tell you which properties to send me.
Imani | Let us turn those words into [[search criteria::Search criteria specify the client's practical requirements rather than relying on a universal meaning of good neighborhood.]]. What matters most about the property and your daily journey? I can compare objective details without deciding where you should feel you belong.
Cam | I need to reach Central Clinic by nine on weekdays. I will use public transport, and I want no more than thirty-five minutes from home to the clinic.
Imani | We should measure the [[door-to-door journey::The full journey includes travel between actual endpoints, not merely the time spent on a train or bus.]], including the walk, waiting, and changes. A station-to-station number could look short while leaving out a substantial part of your morning.
Cam | Some listings say ten minutes from the center without explaining how. That would not tell me whether I could reach the clinic at the right time.
Imani | Correct. We need [[peak-hour travel::The relevant travel conditions are weekday morning arrival conditions, not an unrelated quiet-period estimate.]] information for your stated arrival. Even then, a route estimate is not a guarantee that every service will run at exactly the same speed.
Cam | Inside the property, two bedrooms are essential. I also need an entrance without steps, not just a building described as conveniently accessible.
Imani | I will record those as [[must-haves::Must-haves are the client's essential requirements; they should not be silently traded away for other attractive features.]]. We should distinguish them from preferences so a larger kitchen or attractive view does not silently replace something you said is necessary.
Cam | For the entrance, I would want to know which route the description refers to. A rear route may be very different from the main entrance.
Imani | We will verify the [[step-free access::Step-free access must refer to the relevant real route; a general listing label does not establish that route's details.]] and any relevant measurements. A broad listing label is not enough to establish that the actual route meets your needs.
Cam | I suggest looking at homes advertised up to four hundred fifty thousand dollars. I have not yet completed the lender's checks.
Imani | Then that is an [[asking-price cap::The asking-price cap filters advertised properties; it is not confirmed financing capacity or a complete affordability assessment.]], not confirmed borrowing capacity. We can use it for the initial search while keeping the financing question visibly unresolved.
Cam | I also do not want to discover later that a property has large recurring charges. The advertised price would not tell the whole story.
Imani | We should collect the relevant [[ownership costs::Ownership costs extend beyond the purchase price and may affect the client's practical budget.]], including taxes, insurance, and any association charges. Missing amounts should stay marked as unknown rather than be treated as zero.
Cam | If a condominium has regular dues, could there also be a separate charge for a particular building project? I would want that checked.
Imani | Yes, ask about a [[special assessment::A special assessment can be an additional charge for a particular purpose; regular dues alone may not describe every obligation.]] where applicable and review the actual documents. I should not infer the absence of extra obligations just because a listing shows the routine monthly charge.
Cam | I might accept less space for a shorter journey. Can the comparison show both, rather than rank a larger home as automatically better?
Imani | We can present each [[trade-off::A trade-off makes competing priorities explicit while leaving the client to decide which compromise, if any, is acceptable.]] against your requirements. If an option misses a must-have, I will say so rather than call it a perfect match.
Cam | Use those criteria for the first search. Please flag any unverified entrance or travel claim, and I will follow up with the lender about the budget.
Imani | Exactly. The [[shortlist::The shortlist is a group for closer review, not a guarantee that all property, travel, and financial conditions are already verified.]] will show the source and status of each relevant detail. You can then compare the options on the criteria you actually chose.''',
    transfer_title='The walking time left out the stairs',
    transfer_setup='A listing says five minutes to a station, measured from the building entrance. The apartment is upstairs with no lift. The buyer requires a step-free route from the apartment to the platform.',
    transfer='''Agent: "The quoted time starts at the building ___." | entrance | The supplied estimate excludes the route from the upstairs apartment to the building entrance.
Buyer: "My requirement covers the complete ___." | route | The buyer specified the full route from apartment to platform, not just the outdoor segment.
Agent: "The stairs mean this route is not a step-free ___." | match | The upstairs apartment without a lift conflicts with the stated step-free requirement.
Buyer: "Keep that requirement in the search ___." | criteria | Retaining the requirement prevents an attractive partial travel estimate from replacing the buyer's actual need.''', rehearsal=["After checking the cloze key, read Cam's requirements aloud: weekday arrival at nine, public transport, thirty-five minutes door to door, two bedrooms, and step-free entry.","Switch roles for the budget discussion. Stress asking-price cap and unknown costs; neither speaker may turn $450,000 into lender approval.","Complete and check the apartment-to-platform exchange. Read it again with the stairs treated as a known conflict with the required step-free route."]))


BOOK['units'].append(unit(
    title='Listings, Property Descriptions, Pricing, and Market Data', scene='Three sale prices do not make three equal comparables',
    skill='Explain why a pricing comparison needs verified differences rather than a simple unqualified average.',
    brief='A seller\'s 1,800-square-foot home is described as in good condition. Three nearby sales closed within 90 days: A, 1,800 square feet in similar stated condition, sold for $470,000; B, 2,400 square feet, sold for $540,000; C, 1,800 square feet requiring major repairs, sold for $430,000. Their simple average is $480,000. Concessions, measurement sources, and other material differences have not been verified. Seller Rosa wants to call $480,000 a proven value; agent Dev must explain the comparison\'s limits.',
    cast='Rosa | Seller\nDev | Listing agent',
    culture=('Explain the adjustment question without inventing an adjustment', 'A seller may understandably favor the highest nearby sale or a neat average. Show the exact differences that affect comparability. Do not replace an unsupported average with invented dollar adjustments merely to sound analytical; distinguish what is known from what the pricing review still needs.'),
    a='''Which sale matches the stated size and condition most closely? | A | B | C | All three equally | A is 1,800 square feet in similar stated condition; B is larger and C required major repairs.
What is the simple average of the three prices? | $480,000 | $470,000 | $500,000 | $490,000 | The prices total $1,440,000; dividing by three gives $480,000 before any comparability analysis.
What remains unverified? | Concessions, measurement sources, and other material differences | Whether B was 600 square feet larger in the supplied figures | Whether C required major repairs in the supplied description | Whether the three supplied prices have a computable average | The briefing explicitly leaves concessions, measurement sources, and other differences unchecked.''',
    vocabulary='''comparable sale | A completed sale selected for its relevance to a property's pricing analysis. | select comparable sales
comparative market analysis | An agent's comparison of relevant market evidence for a pricing discussion. | prepare a comparative market analysis
subject property | The property being evaluated or discussed. | describe the subject property
sale price | The reported amount paid in a completed transaction. | verify the sale price
list price | The advertised asking amount for a property. | set the list price
price reduction | A decrease in the advertised asking amount. | document a price reduction
days on market | A listing-duration measure under a stated counting method. | compare days on market
absorption rate | A sales-to-inventory measure over a specified period and definition. | define the absorption-rate basis
months of supply | Inventory divided by a defined monthly sales pace. | calculate months of supply
concession | A negotiated benefit or contribution affecting transaction terms. | verify seller concessions
adjustment | A supported modification used to account for a relevant difference. | explain a valuation adjustment
condition | The physical state of a property or component. | compare property condition
renovation | Work altering or improving an existing property. | verify the renovation scope
deferred maintenance | Upkeep that has been postponed and may require attention. | identify deferred maintenance
living area | Space included under a stated residential measurement definition. | verify the living-area basis
lot size | The measured area of the parcel of land. | confirm the lot size
measurement source | The record or method from which a size figure comes. | identify the measurement source
price per square foot | Price divided by area under a specified measurement basis. | compare price per square foot
market exposure | The extent and duration of a property's availability to prospective buyers. | assess market exposure
arm's-length transaction | A transaction between independent parties acting in their own interests. | verify arm's-length conditions
listing status | The current recorded stage of a property listing. | confirm the listing status
pending sale | A transaction under contract but not yet completed under the local usage. | distinguish pending sales from closed sales
valuation date | The date for which a value opinion is expressed. | state the valuation date
pricing range | A proposed interval for pricing discussion based on specified evidence. | support the pricing range''',
    precision='An average can be arithmetically correct and analytically weak. Sale B has 600 more square feet; sale C required major repairs. The comparison needs verified characteristics and transaction terms before an unadjusted mean can be treated as useful pricing evidence.',
    precision_extra='A listing price is an asking amount, not a completed sale or guaranteed appraisal. Price per square foot also depends on the measurement basis and property differences. Avoid converting a rough comparison into a precise value opinion without the necessary evidence and professional scope.',
    phrases='''Validate the arithmetic | The simple average is $480,000.
Challenge the conclusion | That average does not by itself prove this property's value.
Name the size difference | Sale B has 600 more square feet in the supplied figures.
Name the condition difference | Sale C required major repairs.
Choose a starting point | A is the closest on the stated size and condition, subject to verification.
Request transaction detail | We need to check concessions and other material terms.
Avoid invented precision | I cannot assign a defensible adjustment without supporting evidence.
Close with analysis | Let us verify the comparison before setting the pricing recommendation.
Keep the sources | Which record supplied each area measurement?
Distinguish prices | Asking price and closed sale price are different measures.
Check timing | Use the actual closing dates and relevant market conditions.
Limit the range | A pricing range is not a guarantee of an accepted offer.
Describe condition | State the renovation or maintenance facts rather than saying perfect.
Check area basis | Are the square-foot figures measured on a comparable basis?
Keep the outlier visible | Do not hide the larger property's differences inside the average.
Summarize the evidence | We have three relevant records, but they are not interchangeable properties.''',
    notes='''Closest on stated facts | This is narrower than claiming a fully verified best comparable.
Unadjusted | The word tells the reader that differences have not yet been accounted for.
Average versus value | One is a calculation; the other is a supported opinion in a defined context.
Sold for versus listed at | These phrases identify completed transaction amounts versus asking amounts.
Subject to verification | Name what needs checking so the qualification is useful.
Exact number | Numerical precision does not prove that the underlying comparison is valid.''',
    d='''Which price summary preserves the distinction between arithmetic and valuation? | The unadjusted mean is $480,000; comparability still needs review. | The adjusted mean is $480,000 after allowing for repairs and size. | The comparable range centers on $480,000 because all three homes are equivalent. | The mean is $470,000 because A is the closest comparable. | Adding $470,000, $540,000, and $430,000 gives $1,440,000, or $480,000 divided by three. No adjustments have been established, and selecting A does not change the arithmetic mean.
What should happen before assigning an adjustment for B's extra area? | Verify comparable measurements and supporting market evidence. | Multiply by any convenient round number without support. | Assume all square footage has an identical value in every property. | Ignore the extra 600 square feet because the sale is recent. | An adjustment needs a defensible basis rather than an arbitrary figure or an assumption of perfect comparability.
Which wording distinguishes asking from sold prices? | The seller may choose a list price, but the supplied records are closed sale prices. | Every list price is a completed transaction price. | A pending sale always supplies the final recorded price. | A suggested price is the same as lender approval. | Asking amounts, pending terms, and completed transactions describe different states and evidence.
Which summary preserves the condition issue? | C's major repairs may affect comparability and require investigation. | C proves that repair needs have no effect on price. | C's condition must be identical to the subject property. | The repair cost is exactly the difference between C and A. | The known condition difference matters, but the case supplies no isolated repair-cost estimate or causal price adjustment.''',
    dialogue='''Rosa | I added the three sale prices and divided by three: four hundred eighty thousand. Can we use that as my home's value?
Dev | It is a useful starting calculation, not the conclusion of a [[comparative market analysis::A comparative market analysis evaluates relevant differences and terms rather than treating the simple mean as a proven value.]]. We need to compare what actually sold with your house.
Rosa | All three are nearby and closed within ninety days. What makes one more useful than another?
Dev | A is the closer [[comparable sale::A comparable sale needs relevant similarity and verified context; being nearby and recent does not make every property equivalent.]] on the supplied facts: eighteen hundred square feet, with similar condition. B is six hundred square feet larger.
Rosa | And C sold for forty-three thousand less than A?
Dev | Forty thousand less: four hundred thirty versus four hundred seventy thousand. C needed major repairs; your [[subject property::The subject property is Rosa's home; the comparison should be made against its verified characteristics.]] is described as being in good condition.
Rosa | Then could we add forty thousand to C and say that is what the repairs were worth?
Dev | Not from these records alone. That would be an unsupported [[adjustment::An adjustment should account for a difference using evidence; the case supplies no justified dollar amount for area or repairs.]]. Other differences may explain part of the price gap.
Rosa | A neighbor said one seller helped with the buyer's closing costs. I do not know which sale.
Dev | Let us verify that [[concession::A concession can change transaction economics, so the headline sale price may not describe every material term.]] before relying on the headline prices. We need the transaction terms, not just the amounts on a summary.
Rosa | The area figures came from separate listings. One description includes a finished basement, but I cannot tell whether its figure does.
Dev | I will check the [[measurement source::Measurement source identifies the origin and basis of area figures, which must be checked for a meaningful comparison.]] and what each total includes. Otherwise we could compare different categories of space without noticing.
Rosa | Would dividing each price by its area make the comparison fairer?
Dev | [[price per square foot::Price per square foot is a ratio, not a complete valuation method that removes property and measurement differences.]] can help, but it does not correct inconsistent measurements or different conditions. A tidy ratio can still conceal a poor comparison.
Rosa | I still need an asking figure. Buyers will not accept a page of uncertainties instead of a number.
Dev | Agreed. The review should lead to a supported [[list price::The list price is an asking amount chosen for marketing; it is not established by the mean or guaranteed as a sale outcome.]] recommendation. We can show the unadjusted average without labeling it a proven value.
Rosa | Could your recommendation include a range and explain why A gets more attention? I want to follow the reasoning.
Dev | Yes. A [[pricing range::A pricing range supports a marketing discussion; it is not a guarantee of an appraiser's conclusion or buyer's offer.]] lets us explain the evidence and limits. It will not promise what a buyer offers or an appraiser concludes.
Rosa | Keep the three sales, then. Before we choose the asking figure, check the areas, concessions, and other important differences.
Dev | I will also verify each record's [[listing status::Listing status distinguishes completed evidence from active or pending listings, preventing different stages from being mixed without explanation.]]. Closed prices, pending transactions, and active asking prices should not be presented as equivalent evidence.''',
    transfer_title='A pending price is not a closed sale',
    transfer_setup='A property was listed at $520,000 and is now pending. Its final sale price has not been reported. A presentation labels $520,000 as the confirmed closed price.',
    transfer='''Agent: "The $520,000 figure is the ___ price." | list | The supplied number is the advertised amount, not a reported completed-sale amount.
Seller: "The transaction is currently ___." | pending | Pending is the stated status, so completion has not been established.
Agent: "The final sale price remains ___." | unreported | The case explicitly says the final sale price has not been reported.
Seller: "We need to correct that comparison ___." | label | The presentation incorrectly labels an asking price as a confirmed closed-sale price.''', rehearsal=["Check the answers and read the price discussion in pairs. Say $470,000, $540,000, and $430,000 distinctly; correct forty-three thousand to forty thousand.","Switch roles for turns 11-20. Stress unadjusted mean and measurement source. Keep $480,000 as arithmetic, not an appraisal or supported adjustment.","Complete the pending-sale exchange, check the key, and reread it. Keep the $520,000 asking price separate from an unreported completed sale price."]))


BOOK['units'].append(unit(
    title='Showings, Open Houses, Fair Housing, and Advertising', scene='Describe the home, not the preferred household',
    skill='Revise exclusionary listing language and handle showing questions with consistent, property-focused information.',
    brief='A draft listing describes a home as "perfect for couples without children." The verified property facts are two bedrooms, a fenced patio, and a park 0.4 miles away. No bedroom-size measurements or step-free route details have been confirmed. Listing coordinator Fern and open-house host Malik must replace the household preference with factual copy before review. The viewing team is to provide the same property information and apply the same stated booking process to all visitors, while routing access-related requests for appropriate handling.',
    cast='Fern | Listing coordinator\nMalik | Open-house host',
    culture=('A welcoming description need not select the occupants', 'Promotional wording can communicate an exclusion even when its writer intends warmth. Keep the conversation focused on the property and consistent service. An access question deserves precise information and appropriate handling, not assumptions about someone\'s medical history or whether they belong in the home.'),
    a='''Which draft wording creates the central concern? | Perfect for couples without children | Two bedrooms | A fenced patio | A park 0.4 miles away | The household preference describes favored occupants rather than the supplied property features and requires correction.
Which facts are verified in the case? | Two bedrooms, a fenced patio, and the park distance | Step-free access and every doorway width | A particular household's eligibility to buy | Guaranteed school admission and room suitability | Only the room count, patio feature, and park distance are supplied as verified property facts.
What is the required viewing approach? | Consistent property information and booking process, with appropriate handling of access requests | Different availability claims based on perceived household type | A medical-history interview before answering access questions | Automatic refusal of any different viewing-format request | The briefing requires consistent service and routing access-related requests, not invented restrictions or intrusive assumptions.''',
    vocabulary='''fair housing | Equal housing opportunity under applicable nondiscrimination requirements. | follow fair-housing requirements
protected characteristic | A trait covered by an applicable nondiscrimination law. | avoid decisions based on protected characteristics
familial status | A protected housing category concerning children and related circumstances under US federal law. | recognize familial-status concerns
steering | Directing housing choices on a prohibited discriminatory basis. | avoid discriminatory steering
discriminatory preference | Wording or conduct favoring or excluding a protected group. | remove a discriminatory preference
equal service | Consistent access to relevant assistance under applicable requirements. | provide equal service
objective feature | A property characteristic that can be described and checked. | describe objective features
occupancy standard | A rule about permitted occupancy requiring legal and factual context. | verify an occupancy standard
reasonable accommodation | A disability-related change to a rule, policy, practice, or service where required. | route a reasonable-accommodation request
reasonable modification | A disability-related physical change to premises where protected or required. | distinguish a reasonable modification
access request | A request concerning how someone can enter, view, or use a property. | respond to an access request
showing appointment | An arranged property-viewing time. | confirm a showing appointment
open house | A scheduled period when a property is available for visits. | host an open house
visitor register | A record of attendees collected under a stated process. | maintain the visitor register
booking process | The steps used to arrange a visit. | apply a consistent booking process
availability statement | Information about whether and when a property can be viewed or obtained. | verify the availability statement
property amenity | A useful feature or facility associated with a property. | describe property amenities
fenced patio | An outdoor paved area enclosed by fencing. | verify the fenced patio
advertising copy | Written language used to market a property. | review advertising copy
photograph caption | Text explaining what a property image shows. | check the photograph caption
virtual tour | A digital presentation allowing a remote view of a property. | offer the approved virtual tour
disclosure packet | A collected set of required or relevant property disclosures. | provide the disclosure packet
showing feedback | Information returned after a property visit. | record property-focused showing feedback
complaint route | The process for raising and handling a service concern. | explain the complaint route''',
    precision='A property description should not become a statement about the preferred buyer\'s family status. The supplied wording needs correction; replacing it with verified room count, outdoor space, and distance information preserves useful marketing content without choosing the occupants.',
    precision_extra='Consistent service does not mean ignoring an access-related request. Obtain the relevant practical details and route the request under the applicable process. Do not invent a universal occupancy limit, certify an unverified access route, or demand unnecessary medical information as casual conversation.',
    phrases='''Identify the concern | This line expresses a household preference rather than a property feature.
Offer factual copy | The home has two bedrooms, a fenced patio, and a park 0.4 miles away.
Keep the review | The revised advertisement still needs the appropriate review.
Apply consistency | Give every visitor the same relevant property information.
Avoid steering | Let visitors assess the property against their own stated needs.
Verify availability | Do not change the availability story based on who is asking.
Handle access precisely | Which route or viewing arrangement would you like us to check?
Close with ownership | I will send the request to the responsible colleague and track the response.
Avoid a diagnosis | We need the practical access information, not an unnecessary medical history.
Mark unverified details | Bedroom measurements and the step-free route are not yet confirmed.
Check the image | The photograph should not imply a feature we have not verified.
Correct the copies | Replace the wording in every version using the same approved text.
Separate room count | Two bedrooms does not itself establish a universal occupancy rule.
Respect the question | I can confirm the features we know and obtain the missing details.
Record useful feedback | Note the visitor's property questions without guessing personal suitability.
Escalate a concern | Use the complaint route if someone reports inconsistent treatment.''',
    notes='''Property versus occupants | Keep the subject of the advertisement on the home and its verified features.
Perfect for | This phrase may imply a preferred household when followed by personal characteristics.
Same relevant information | Consistency concerns the quality and availability of service, not ignoring individual access needs.
Not yet confirmed | Use this for measurements or access details that have not been checked.
Which arrangement | A practical question focuses on the request instead of demanding unrelated personal details.
Needs review | Identifying a concern is not the same as giving final legal clearance to revised copy.''',
    d='''Which revision best uses the supplied facts? | Two bedrooms, a fenced patio, and a park 0.4 miles away. | Ideal for couples who do not plan to have children. | Suitable only for the household type the seller prefers. | Guaranteed accessible in every respect. | The bedroom, patio, and distance description uses verified property facts instead of a household preference or an unverified access claim.
Which reply handles an access question appropriately? | Tell me which route or arrangement to check, and I will route the request. | We cannot answer unless you disclose your entire medical history. | The photo proves that every route is step-free. | Everyone must use the same arrangement without review. | The reply seeks practical details and appropriate handling without making unsupported assumptions or demanding irrelevant information.
Which revised listing adds no unsupported feature or household preference? | Two bedrooms, a fenced patio, and a park 0.4 miles away. | Two spacious bedrooms, a fenced patio, and verified step-free entry. | Two bedrooms ideal for a child-free household, with a park nearby. | Two bedrooms with confirmed wheelchair-clear doorways and a fenced patio. | Only the bedroom count, patio, and park distance are verified. Spaciousness, doorway clearances, and step-free access need evidence; the child-free description retains the household preference.
Which conduct violates the supplied service approach? | Claiming different availability because of a visitor's perceived household type | Giving visitors the same verified feature sheet | Checking an unverified route | Recording a property-specific question for follow-up | The briefing requires consistent availability information and booking processes rather than demographic assumptions.''',
    dialogue='''Fern | The draft says perfect for couples without children. I think we should revise it before sending the listing for review or printing the open-house sheet.
Malik | Agreed. It expresses a [[discriminatory preference::The wording favors a household without children rather than describing the property, creating a familial-status concern.]] rather than a feature of the home. We can make the description attractive without suggesting which households the seller wants.
Fern | The verified facts are two bedrooms, a fenced patio, and a park four tenths of a mile away. Those give us useful material.
Malik | Let us lead with each [[objective feature::An objective feature describes something about the property that can be checked, rather than a favored type of occupant.]]. We should not replace the old wording with another personal label that communicates the same exclusion in a different way.
Fern | The seller says that phrase was meant as a compliment to the home. How would you explain why we still need to change it?
Malik | Focus on the effect of the [[advertising copy::Advertising copy communicates to potential buyers; the message it conveys matters even if the writer describes a different intention.]]. Readers could understand a preference about who should live there. A factual revision keeps the property appealing while removing that message.
Fern | What about visitors who ask whether the home would suit their family? I can describe the rooms, but I should not make that decision for them.
Malik | Exactly. Avoid [[steering::Steering directs housing choices on an improper discriminatory basis; visitors should assess objective facts against their own needs.]]. Give the relevant facts and let the visitor assess their own needs, rather than guide them according to assumptions about personal background.
Fern | We have the room count but not the bedroom dimensions. I would rather be clear about that than promise that everyone's furniture will fit.
Malik | Put the missing measurements in the [[disclosure packet::The shared property-information packet should preserve what is known and what still needs verification, rather than create unsupported assurances.]] or accompanying status notes for follow-up. The same information should be available to each visitor, not selectively changed from conversation to conversation.
Fern | A visitor may also ask about a step-free route. We have not checked it, and a photograph does not show the complete entrance sequence.
Malik | Treat that as an [[access request::An access request needs practical route or arrangement information; the case does not establish that the route is already suitable.]]. Ask what practical arrangement or feature needs checking and route it properly, without turning a property question into an unnecessary medical-history interview.
Fern | Does consistent treatment mean offering exactly the same viewing arrangement even when someone asks for a disability-related change?
Malik | No. A [[reasonable accommodation::A reasonable-accommodation request concerns a disability-related change to a rule or service and should receive appropriate handling under applicable requirements.]] request needs appropriate handling under the relevant process. Consistency is not a reason to ignore it or decide casually that no adjustment can be made.
Fern | I will give the team the current property sheet and a contact for unresolved access questions. We should also confirm how appointments are recorded.
Malik | Use the same stated [[booking process::The booking process should be applied consistently rather than altered because of assumptions about a visitor's household.]] for visitors, while routing relevant requests. Do not tell one household that no appointments exist when the same slots are offered to another.
Fern | At the end of a viewing, useful comments would concern layout, condition, price questions, or missing documents, not whether I think a person belongs there.
Malik | Right. Record [[showing feedback::Showing feedback should capture property-related observations and questions, not invented judgments about a visitor's personal suitability.]] in those concrete terms. If a visitor raises a concern about treatment, preserve the actual concern instead of dismissing it as a misunderstanding.
Fern | I will change all three versions: website, printed sheet, and host notes. Please check that the team uses the revised copy at the viewing.
Malik | Then send the consistent version through review and keep the [[complaint route::The complaint route gives visitors and staff a defined way to raise concerns about service or treatment.]] clear for the team. We can market the property effectively while providing factual information and respectful service to everyone.''',
    transfer_title='The photo is not a measurement',
    transfer_setup='A prospective visitor asks for the clear doorway width. The listing has a photograph but no measurement. The team can ask the property contact to obtain an accurate measurement.',
    transfer='''Host: "The doorway width is not yet ___." | verified | A photograph does not supply the accurate measurement requested in the case.
Visitor: "Please obtain the actual ___." | measurement | The visitor needs a dimension rather than a general impression from an image.
Host: "I will ask the property ___ to check it." | contact | The briefing identifies the property contact as the route for obtaining the dimension.
Visitor: "Then I can assess it against my access ___." | needs | The verified information lets the visitor evaluate practical fit without the host guessing suitability.''', rehearsal=["Check the key and read the listing-review exchange. Contrast the rejected household preference with the three verified property facts.","Switch roles for the viewing discussion. Keep consistency in information separate from refusing to handle an access-related request.","Complete and check the doorway exchange. Read both roles, retaining the distinction between a photograph, an actual measurement, and the visitor's own access needs."]))


BOOK['units'].append(unit(
    title='Offers, Counteroffers, Negotiation, and Contingencies', scene='A thirty-day offer with an unconfirmed loan timeline',
    skill='Discuss offer timing and protections without turning a proposal or lender estimate into a binding assurance.',
    brief='Buyer Tomas wants to propose a $420,000 purchase, an $8,000 earnest-money deposit, and closing in 30 days. The lender has given only a provisional 35-45-day processing estimate, not final approval. No offer has been submitted or accepted. Agent Elise must explain the timing mismatch and review the proposed financing contingency and deposit terms with the appropriate professionals. The buyer has not authorized removing any protection, and no seller concession or extension has been agreed.',
    cast='Tomas | Buyer\nElise | Buyer\'s agent',
    culture=('Separate a stronger offer from an uninformed promise', 'A buyer may want to appear decisive in a competitive negotiation. Help them distinguish an attractive term from a term they can reasonably support. Keep the client\'s authority central and explain the review needed before changing conditions, rather than treating urgency as permission to remove protections.'),
    a='''What timing mismatch is stated? | A 30-day proposed close versus a provisional 35-45-day lender estimate | A 45-day signed contract versus a 30-day final lender guarantee | A completed closing before the offer was drafted | Two identical confirmed 30-day commitments | The buyer's proposed date is earlier than the lender's provisional range, and neither establishes final financing approval.
What is the current offer status? | Not submitted or accepted | Accepted with every contingency waived | Rejected by the seller | Signed by both parties with an agreed extension | The briefing explicitly says no offer has been submitted or accepted.
What has Tomas not authorized? | Removing any protection | Discussing a proposed price | Asking about the financing timeline | Reviewing the proposed deposit terms | The case permits discussion but contains no instruction to remove protections.''',
    vocabulary='''purchase offer | Proposed terms for buying a property. | prepare a purchase offer
counteroffer | A response proposing different terms instead of accepting the original offer. | review a counteroffer
acceptance | Agreement to an offer under the applicable legal requirements. | confirm valid acceptance
offer expiration | The point when an offer ceases to remain open under its terms. | verify the offer expiration
earnest money | A deposit showing commitment, governed by the contract and applicable rules. | explain earnest-money terms
deposit holder | The authorized person or entity holding a transaction deposit. | identify the deposit holder
contingency | A contractual condition affecting obligations or available rights. | review the contingency
financing contingency | A contract condition addressing financing under specified terms. | explain the financing contingency
inspection contingency | A contract condition addressing inspection and related rights. | review the inspection contingency
appraisal contingency | A contract condition addressing appraised value and related rights. | clarify the appraisal contingency
home-sale contingency | A condition connected to selling another property. | review the home-sale contingency
contingency deadline | The contractual time limit for a condition or related action. | track the contingency deadline
waiver | Giving up a right or condition under applicable requirements. | explain the proposed waiver
amendment | An agreed change to an existing agreement. | document an amendment
addendum | Additional document or terms incorporated into an agreement. | review the addendum
seller credit | A seller contribution toward specified buyer costs under permitted terms. | request a seller credit
possession date | The date the buyer is entitled to take possession under the agreement. | confirm the possession date
closing date | The scheduled or agreed date for completing closing steps. | verify the closing date
extension request | A proposal to move an existing deadline. | submit an extension request
notice requirement | Rules governing how and when a contractual notice must be given. | check the notice requirement
default | Failure to meet a contractual obligation as defined by the agreement and law. | obtain advice about default
remedy | A response or relief available under an agreement or law. | clarify available remedies
authorized instruction | A direction given by someone with the relevant decision-making authority. | record the authorized instruction
negotiating position | The terms and priorities a party is prepared to advance. | clarify the negotiating position''',
    precision='Proposed closing in 30 days is not the same as a lender confirming that financing can be ready then. An estimate of 35-45 days creates a specific issue to resolve. Avoid describing either the proposed date or the provisional estimate as a guarantee.',
    precision_extra='A contingency has exact conditions, deadlines, and notice requirements; its name alone does not explain every protection. Deposit recovery is not automatically assured by calling money earnest money. Actual rights need the contract and qualified advice, especially before waiver or amendment.',
    phrases='''Name the mismatch | The proposed 30-day close is earlier than the lender's provisional range.
Keep status clear | No offer has been submitted or accepted yet.
Check feasibility | Let us ask the lender what supports the current timing estimate.
Preserve authority | I will not remove a protection without your informed instruction and proper review.
Explain the condition | We need to read the financing contingency's exact terms.
Avoid a refund promise | The deposit's treatment depends on the contract and applicable requirements.
Separate request and agreement | Asking for an extension does not mean the seller has agreed.
Close with review | Confirm the timing and terms before authorizing the offer.
State the price | Your proposed purchase price is $420,000.
Clarify the deposit | The proposed earnest-money amount is $8,000.
Check the notice | Who must receive the notice, by what method, and by when?
Separate possession | Closing and possession dates should not be assumed identical.
Record priorities | Which terms are you authorizing us to propose?
Avoid pressure language | Urgency does not remove the need to understand the consequences.
Review a counter | A counteroffer changes the proposed terms and requires a decision.
Confirm the final version | Use the exact version you have reviewed and authorized.''',
    notes='''Propose versus promise | A proposed term is a negotiating position; a promise can create a stronger assurance.
Subject to financing | The phrase is incomplete without the actual contractual condition and required actions.
Requested versus agreed | An extension request does not alter a deadline by itself.
May be refundable | Any statement about deposit return needs the governing terms and facts.
Authorize versus discuss | Exploring an option is not an instruction to submit it.
By when and how | Contractual notices can depend on both timing and delivery requirements.''',
    d='''Which sentence handles the timing accurately? | We need to resolve the gap between the proposed 30 days and the lender's provisional 35-45 days. | The lender has guaranteed 30 days because that is our preferred offer. | A 35-45-day estimate proves final approval. | The seller has already accepted a 45-day extension. | The sentence retains both actual timeframes and their status without inventing approval or agreement.
Which statement about the deposit is appropriate? | We need the exact contract terms before explaining when the deposit could be returned. | All earnest money is automatically refundable under every circumstance. | An $8,000 deposit guarantees financing approval. | Calling the deposit refundable overrides every notice requirement. | The deposit's treatment depends on the agreement, applicable rules, and facts rather than its label or amount alone.
What should Elise do before removing a protection? | Obtain informed client instruction and the necessary review of consequences. | Infer permission from the buyer's wish to be competitive. | Treat an unanswered message as a blanket waiver. | Let the seller's preference replace the buyer's authorization. | The case contains no authorization to remove protections; urgency is not a substitute for an informed decision.
The buyer has requested more time, but no acceptance is supplied. Which update is accurate? | The extension is requested; agreement to change the deadline is unconfirmed. | The extension is provisionally agreed because the request has been delivered. | The deadline is suspended until the seller answers the request. | The lender's later estimate replaces the proposed contractual date. | Delivery of a request proves neither acceptance nor suspension of a deadline. A lender's processing estimate also cannot by itself amend the parties' terms.''',
    dialogue='''Tomas | I want to offer four hundred twenty thousand dollars, with eight thousand in earnest money and a thirty-day close. That should look decisive.
Elise | We can discuss those terms, but the proposed [[closing date::The proposed closing date is earlier than the lender's provisional processing range and is not yet an agreed or assured date.]] conflicts with the lender's current thirty-five-to-forty-five-day estimate. We need to resolve that gap before presenting thirty days as feasible.
Tomas | The lender said the estimate was provisional. I was hoping that a signed contract might make the process move more quickly.
Elise | It may clarify the transaction, but it does not create final approval. The [[financing contingency::The financing contingency has specific contractual conditions and actions; it cannot turn an unconfirmed timeline into guaranteed financing.]] and timing need careful review, rather than assuming the lender will meet a date because we request it.
Tomas | I have not asked you to remove financing protection. I just want to understand how the dates and conditions affect the proposal.
Elise | Understood. Discussing a [[waiver::A waiver gives up a right or condition; discussing competitiveness does not authorize the agent to remove protections.]] is not an instruction to make one. We should explain the consequences and obtain the appropriate review before you decide about any change.
Tomas | What does the eight-thousand-dollar deposit mean for me if the financing does not work out? I have heard that it is always refundable.
Elise | The [[earnest money::Earnest money is governed by the agreement and applicable requirements; the label does not guarantee automatic return.]] terms need to answer that in context. I cannot promise an automatic refund without the contract, the facts, and any required actions being considered.
Tomas | Show me the dates and notice steps as well as the protection itself. I do not want to miss a deadline because I only read the heading.
Elise | Exactly. Read each [[contingency deadline::A contingency deadline governs timely exercise or satisfaction of a condition; its consequences depend on the actual contract.]] together with the required action. The heading alone does not explain how the condition operates or what happens if a step is missed.
Tomas | If the lender later needs more time, could we simply tell the seller that the closing date has moved?
Elise | We could make an [[extension request::An extension request proposes a new deadline; it does not change the existing agreement without the required acceptance.]], but that is not an agreed change. We would need to follow the applicable process and confirm whether the other party accepts it.
Tomas | And if the seller sends back a different price or date, I should not assume that means our original proposal has been accepted.
Elise | Correct. A [[counteroffer::A counteroffer proposes different terms and requires review; it should not be reported as acceptance of the unchanged original offer.]] needs a fresh review of the actual terms and their legal effect. We should identify the differences clearly so you can make an informed decision.
Tomas | I also want to know who would hold the deposit and what instructions I should rely on if the offer moves forward.
Elise | We should identify the authorized [[deposit holder::The deposit holder is the person or entity authorized to hold the funds; the case has not yet established that arrangement.]] and verify instructions through a trusted route. Do not treat unexpected payment details as verified merely because they mention this transaction.
Tomas | The possession date matters as well because I need to arrange a move. I should not book everything just from the proposed closing line.
Elise | Right. The [[possession date::Possession is governed by the agreement and need not be identical to closing or to an unaccepted proposed date.]] must be checked separately in the terms. We should not promise access to the property before the relevant agreement and closing conditions are confirmed.
Tomas | Ask the lender about a realistic date first. Then walk me through the conditions before I authorize the exact offer you will submit.
Elise | I will record your [[authorized instruction::An authorized instruction identifies the buyer's actual decision; it is distinct from this preliminary exploration of options.]] after that review and confirm the exact version before submission. At present we have a proposal to examine, not an accepted contract or a guaranteed timeline.''',
    transfer_title='A request to extend is still pending',
    transfer_setup='An inspection-response deadline in a fictional contract is Friday at 5 p.m. The buyer has asked to move it to Monday. No agreement to the change has been received.',
    transfer='''Agent: "The proposed new deadline is ___." | Monday | Monday is the requested date, not an already accepted contractual change.
Buyer: "The existing stated deadline remains ___ at 5 p.m." | Friday | No accepted change is supplied, so the original stated deadline must not be treated as replaced.
Agent: "We need confirmation of the required ___." | agreement | The request alone does not establish that the other party has accepted the alteration.
Buyer: "Do not describe the extension as ___." | approved | The case supplies no approval, so that label would invent a completed decision.''', rehearsal=["After checking the key, read the offer discussion. Contrast a proposed thirty-day close with the lender's provisional thirty-five-to-forty-five-day range.","Switch roles for the deposit and notice discussion. Keep $8,000, the exact contractual conditions, and the need for authorized instructions unchanged.","Complete the extension exchange and check its key. Read Friday at five as the existing deadline and Monday as the requested, unconfirmed change."]))


BOOK['units'].append(unit(
    title='Inspections, Repairs, Disclosures, and Due Diligence', scene='An inspection finding is not a repair diagnosis',
    skill='Relay a technical finding accurately, arrange further evaluation, and distinguish a repair request from an agreement.',
    brief='A home inspection reports staining on a basement wall and recommends evaluation by a qualified moisture specialist. It does not establish the cause, give a repair design, or estimate a repair cost. The seller\'s disclosure marks prior water intrusion as unknown. Buyer Nina asks agent Omar whether the wall only needs paint and whether the seller must pay. No specialist appointment or repair agreement is confirmed. The contractual inspection-response requirements need review before any decision or deadline assurance.',
    cast='Nina | Buyer\nOmar | Buyer\'s agent',
    culture=('Be useful without borrowing another profession\'s certainty', 'An agent can locate the relevant report passage, coordinate a referral, and track the contractual steps. That is substantive help. Avoid turning a request for reassurance into a technical diagnosis, a guarantee of safety, or a conclusion about another party\'s obligations.'),
    a='''What does the report establish in this case? | Staining was observed and specialist evaluation was recommended | The wall only needs paint | A particular pipe caused the issue | The seller accepted a repair obligation | The report states an observation and recommendation, not a cause, repair specification, or contractual agreement.
How does the seller's disclosure describe prior water intrusion? | Unknown | Confirmed never to have occurred | Fully repaired with a transferable guarantee | Admitted and priced into an agreed credit | Unknown records an unresolved fact; it is not proof of absence, repair, or an agreed concession.
Which next step is supported? | Arrange qualified evaluation and review the contractual response requirements | Promise that paint will solve the issue | Guarantee the seller will pay every cost | Treat a referral as a completed repair | The case needs technical evaluation and contract review before a diagnosis, cost, or obligation can be asserted.''',
    vocabulary='''home inspection | An assessment of a property's condition within a defined professional scope. | arrange a home inspection
inspection scope | The systems, access, and services covered by an inspection. | review the inspection scope
visual observation | A condition identified through what can be seen. | record a visual observation
accessible component | A component available for inspection under the stated access limits. | identify accessible components
inspection limitation | A condition restricting what could be inspected or concluded. | document an inspection limitation
deficiency | An observed shortcoming or condition requiring attention in context. | describe the reported deficiency
further evaluation | Additional assessment by an appropriately qualified professional. | recommend further evaluation
specialist referral | Direction to someone with relevant expertise for a specific issue. | coordinate a specialist referral
moisture intrusion | Entry of water or moisture into a building area. | investigate moisture intrusion
staining | Visible discoloration that may need explanation or evaluation. | document wall staining
root cause | The underlying source of an identified problem. | establish the root cause
repair scope | The work specified to address a condition. | define the repair scope
repair estimate | An approximate price for specified repair work. | obtain a repair estimate
contractor quotation | A contractor's priced proposal for a stated scope and conditions. | review the contractor quotation
permit | Official authorization for work where required. | verify permit requirements
code compliance | Conformity with applicable building requirements. | obtain qualified code-compliance review
reinspection | A subsequent inspection to assess specified work or conditions. | arrange a reinspection
warranty | A defined promise concerning performance, repair, or other coverage. | review warranty exclusions
seller disclosure | Information about a property supplied by the seller under applicable requirements. | review the seller disclosure
disclosure supplement | Additional information added to an earlier disclosure. | request a disclosure supplement
due diligence | The investigation and review undertaken before a transaction decision. | track due-diligence items
repair request | A proposal asking another party to undertake specified work. | submit a repair request
repair agreement | Accepted terms governing specified repair work. | confirm the repair agreement
repair credit | A negotiated financial allowance instead of or toward repair work. | review the proposed repair credit''',
    precision='Observed staining, suspected cause, and confirmed diagnosis are different levels of information. The supplied report recommends a specialist; it does not say paint is sufficient. A seller\'s unknown response is also not a representation that water intrusion never occurred.',
    precision_extra='A referral is not a confirmed appointment, an estimate is not an agreed price for every possible repair, and a repair request is not an accepted obligation. Keep the technical assessment and contractual decision moving together without pretending either is finished.',
    phrases='''Attribute the finding | The report records staining and recommends specialist evaluation.
Limit the diagnosis | It does not establish the cause or a repair design.
Correct the assumption | We cannot conclude that paint alone will resolve it.
Explain unknown | The seller marked that history as unknown, not confirmed absent.
Coordinate expertise | I can help arrange an appropriately qualified specialist.
Keep the cost open | No repair scope or reliable cost has been established.
Separate the request | Asking the seller to act is not the same as an agreement.
Close with tracking | We will track the evaluation and contractual response requirements.
Check the scope | What did the inspection cover, and what was inaccessible?
Request the wording | Let us read the exact report passage together.
Avoid a guarantee | I cannot certify the condition from this description.
Verify the appointment | A referral has been sent; the visit is not yet confirmed.
Clarify the quote | Does this price cover evaluation or the specified repair work?
Check completion | We need appropriate evidence that any agreed work was completed.
Review the deadline | Confirm the contract's dates, notice method, and available options.
Preserve the record | Keep the report, responses, and any agreed changes together.''',
    notes='''Records versus diagnoses | A report can document a visible condition without identifying its cause.
Unknown versus no | Unknown does not establish the negative fact that something never happened.
Recommended versus arranged | A recommendation does not prove that an appointment has been booked.
Estimate for what | A price needs a specified service or repair scope.
Must pay | This asserts an obligation and needs contractual or legal support, not an agent's reassurance.
Resolved | Reserve this for an adequately verified outcome, not a sent message or referral.''',
    d='''Which handover to the specialist preserves exactly what the report establishes? | Basement staining observed; cause and repair scope not established. | Historic water intrusion confirmed; cosmetic repainting provisionally recommended. | Active plumbing leak diagnosed; repair price awaiting a contractor quote. | Seller's prior repair verified; remaining staining needs a warranty review. | The report documents staining and recommends further evaluation. It supplies no cause, repair history, active plumbing diagnosis, or warranty finding.
How should the unknown disclosure response be interpreted? | The relevant history is not established by that answer. | It proves water intrusion never happened. | It confirms all earlier repairs met current code. | It creates an automatic unlimited repair credit. | Unknown does not establish either absence, completed repair, compliance, or a contractual concession.
Which statement about seller payment is appropriate? | We need the actual contract and any negotiated agreement before asserting an obligation. | Every inspection observation automatically requires seller payment. | A specialist referral is proof the seller accepted liability. | A buyer's repair request is already an accepted amendment. | The case supplies no agreement or established obligation, so the contractual question requires review.
Which update correctly distinguishes progress? | The referral is underway; the appointment and repair scope remain unconfirmed. | The repair is completed because the report was received. | The contractor has agreed to every cost because their name was shared. | All response deadlines are extended automatically during evaluation. | The update reports only the actual referral step and leaves unfinished arrangements and terms open.''',
    dialogue='''Nina | The report shows staining on the basement wall. Can we assume it only needs paint, or does the photograph tell you what caused it?
Omar | The [[visual observation::The observation identifies visible staining; it does not establish the underlying cause or the work needed to address it.]] is staining. The report does not establish the cause, and I should not turn a photograph into a diagnosis or tell you that paint will resolve it.
Nina | The inspector recommends a moisture specialist. I was hoping the general inspection would answer every question before I had to contact anyone else.
Omar | We should review the [[inspection scope::Inspection scope identifies what the inspection covers and its limits; a general report need not resolve every specialist question.]] and the exact recommendation. An inspection can identify an issue requiring another professional's assessment without supplying that specialist analysis itself.
Nina | I noticed that the seller marked previous water intrusion as unknown. Is that effectively the same as saying there has never been a problem?
Omar | No. The [[seller disclosure::The seller disclosure records an unknown history here, not a verified statement that water intrusion never occurred.]] leaves that history unresolved. We should preserve the word unknown instead of paraphrasing it as a confident no.
Nina | Who should look at this next, and can you help arrange it? I need to know what to do before the response deadline.
Omar | I can help coordinate a [[specialist referral::A specialist referral connects the buyer with appropriate expertise; it does not itself establish a diagnosis or confirmed appointment.]] and track the response. We will ask about the relevant qualifications, availability, and evaluation scope before describing any visit as confirmed.
Nina | Once the specialist looks at it, I want to understand why the staining occurred, not just receive a general suggestion to cover the mark.
Omar | That is a question about the [[root cause::The root cause is the underlying source of the problem, which the present inspection has not identified.]]. The qualified evaluator can explain their findings and limits. I can help organize the information, but I cannot supply that technical conclusion in advance.
Nina | If work is needed, I would also want the proposal to say exactly what is included. A single unexplained number would not be enough.
Omar | Ask for the [[repair scope::Repair scope defines the actual work being priced; without it, a cost figure may refer to a different or incomplete service.]] and its conditions. Evaluation, repair, permits where required, and follow-up checks may be different items rather than one automatic package.
Nina | Could we ask the seller to handle the work? I do not want your answer to imply that they have already accepted responsibility.
Omar | We can discuss a [[repair request::A repair request proposes work for negotiation; the seller has not yet accepted any repair obligation in the case.]] after the relevant review. A request is not a repair agreement, and the actual contract and applicable rules determine the available process.
Nina | Timing worries me. If arranging the specialist takes longer than expected, does that automatically extend the inspection-response deadline?
Omar | No. We need to track the [[due diligence::Due diligence includes the investigation and contractual review; continuing an evaluation does not itself alter a contractual deadline.]] alongside the contract requirements. Any extension or notice needs the proper process, rather than an assumption that the clock stops during evaluation.
Nina | If the seller eventually agrees to work, how would I know that the agreed scope was actually completed before relying on it?
Omar | The agreement should address suitable completion evidence and any appropriate [[reinspection::A reinspection can assess specified completed work or conditions; it is distinct from merely receiving a contractor's promise.]]. We should not call the matter resolved solely because someone says a contractor has been contacted.
Nina | Please pursue the specialist visit and check the deadline at the same time. I do not want to lose time while we wait for an appointment.
Omar | Exactly. Any proposed [[repair credit::A repair credit is a negotiated allowance; the current report does not establish its amount or the seller's acceptance.]] or work agreement will need its own review and acceptance. I will give you a status update that separates each completed step from what remains open.''',
    transfer_title='The quotation covers evaluation only',
    transfer_setup='A specialist quotes $250 for an assessment visit. The quotation excludes repairs. The visit is not yet booked, and no repair design or price has been supplied.',
    transfer='''Buyer: "The $250 is for the ___." | assessment | The supplied quotation prices an evaluation visit rather than repair work.
Agent: "It excludes ___." | repairs | The quotation expressly excludes repairs, so they must not be described as included.
Buyer: "The appointment still needs ___." | confirmation | The visit has not been booked, so the quotation is not evidence of a confirmed appointment.
Agent: "A repair price will need a defined ___." | scope | A meaningful repair price requires specified work, which has not yet been supplied.''', rehearsal=["Check the key, then read the inspection discussion. Stress observed staining, unknown history, and specialist evaluation without adding a diagnosis.","Switch roles for turns 11-20. Distinguish scope, request, agreement, and completion evidence; preserve the need to check the response deadline.","Complete and check the quotation exchange. Read $250 as assessment only, with repairs excluded and the appointment still unconfirmed."]))


BOOK['units'].append(unit(
    title='Financing, Appraisal, Title, Escrow, and Closing', scene='Appraisal received does not mean clear to close',
    skill='Explain separate closing milestones and route unresolved financial or title questions to the responsible professional.',
    brief='Buyer Aria sees "appraisal received" on the transaction checklist and asks whether everything is ready to close. The title professional is still investigating a recorded prior lien for which a release has not been verified. Final lender approval is not confirmed. A draft settlement calculation shows $25,000 cash to close, but final figures and payment instructions have not been verified. Transaction coordinator Samir must give an accurate update and assign follow-up without declaring the title clear, guaranteeing funding, or treating the draft as final.',
    cast='Aria | Buyer\nSamir | Transaction coordinator',
    culture=('A useful update identifies both progress and the open item', 'A client may hear one completed milestone as confirmation that the whole transaction is finished. Acknowledge the progress, then name the separate unresolved work and its owner. Avoid a vague "everything is fine" that can lead the client to rely on unverified dates or payment instructions.'),
    a='''What does the checklist confirm? | The appraisal has been received | Title has been cleared | Final lender approval has been issued | Payment instructions have been independently verified | The checklist records receipt of the appraisal only; the other milestones remain unresolved.
Who owns the investigation into the recorded prior lien? | The title professional | The lender's appraiser | The transaction coordinator | The loan underwriter | The title professional investigates the recorded claim. The appraiser addresses value, the coordinator tracks updates, and the underwriter assesses the loan; those roles do not replace this assigned title investigation.
What is the status of the $25,000 figure? | A draft cash-to-close calculation | A verified final payment instruction | The full purchase price | A guarantee of the final mortgage balance | The amount is explicitly a draft settlement calculation, not a confirmed instruction or other transaction value.''',
    vocabulary='''appraisal | A professional opinion of value for a specified purpose and date. | review the appraisal
appraised value | The value opinion stated in an appraisal. | distinguish appraised value from purchase price
underwriting | A lender's assessment of risk and loan requirements. | track underwriting conditions
conditional approval | Approval subject to specified outstanding conditions. | review conditional approval
clear to close | A lender status indicating closing readiness under its process and conditions. | confirm clear-to-close status
loan commitment | A lender's stated commitment subject to its documented terms. | review the loan commitment
rate lock | An agreement to hold specified loan pricing for a defined period and conditions. | verify the rate-lock terms
loan-to-value ratio | Loan amount divided by the applicable property value basis. | confirm the loan-to-value basis
debt-to-income ratio | Debt payments divided by qualifying income under a lender's method. | explain the debt-to-income basis
title search | Examination of records relevant to property ownership and interests. | complete the title search
lien | A legal claim or charge against property securing an obligation. | investigate a recorded lien
lien release | A document or action releasing a lien under applicable requirements. | verify the lien release
encumbrance | A right, claim, or restriction affecting property. | identify an encumbrance
easement | A right to use another's land for a specified purpose. | review the recorded easement
title commitment | A statement of terms and requirements for issuing title insurance. | review the title commitment
title exception | A matter excluded from specified title-insurance coverage. | explain a title exception
owner's title insurance | Coverage protecting the owner's interest subject to policy terms. | review owner's title-insurance coverage
lender's title insurance | Coverage protecting the lender's interest subject to policy terms. | distinguish lender's title insurance
escrow | Holding money or documents pending conditions, or a mortgage account for certain ongoing costs. | clarify which escrow is meant
settlement statement | A document itemizing transaction funds and charges in the applicable closing process. | reconcile the settlement statement
Closing Disclosure | A US form detailing terms and costs for covered mortgage transactions. | review the Closing Disclosure
cash to close | The amount due from the buyer at closing under the stated calculation. | verify cash to close
disbursement | Release or payment of funds to the appropriate recipients. | confirm authorized disbursement
recording | Entry of a document into the relevant public records. | confirm recording status''',
    precision='Received does not mean reviewed, accepted, or cleared. An appraisal concerns value for its purpose; it does not resolve every title issue or loan condition. Title review, lender approval, final calculations, and closing instructions have distinct owners and statuses.',
    precision_extra='Cash to close differs from the purchase price and can reflect deposits, credits, charges, and loan proceeds. A draft figure is not a verified payment instruction. Closing, funding, recording, and possession also need their actual process and agreement rather than an assumed universal sequence.',
    phrases='''Acknowledge progress | The appraisal has been received.
Name the open item | The recorded lien release has not yet been verified.
Assign the question | The title professional is investigating that record.
Separate approvals | Appraisal receipt does not confirm final lender approval.
Label the number | $25,000 is the current draft cash-to-close figure.
Protect the payment step | Verify final instructions through an established trusted channel.
Avoid a blanket assurance | I cannot yet say that every closing condition is satisfied.
Close with owners | I will obtain the title and lender updates separately.
Clarify the document | Which version of the settlement calculation are you reviewing?
Ask about a difference | Please explain which charges or credits changed.
Check the lender state | Has the lender issued its actual clear-to-close confirmation?
Separate interests | An owner's policy and a lender's policy protect different interests.
Define escrow | Do you mean the transaction holding arrangement or the mortgage cost account?
Avoid a title opinion | I will relay the title professional's explanation, not declare the lien resolved myself.
Keep timing conditional | The schedule depends on the unresolved conditions and applicable requirements.
Confirm completion | We need the responsible party's confirmation of each completed step.''',
    notes='''Received versus cleared | Receipt is a document milestone, not a conclusion about its effect.
Draft versus final | Keep the status next to the amount so a client does not mistake a working figure for an instruction.
Owner and lender | These labels distinguish the interest protected by different title policies.
Escrow in context | The same word can describe transaction holding or ongoing mortgage-related payments.
Cash to close | This amount is not interchangeable with down payment, purchase price, or total borrowing.
Confirmed by whom | Identify the professional responsible for the particular approval or record.''',
    d='''Which closing update is accurate? | The appraisal is received, while title and final lender approval remain open. | The appraisal clears every lien automatically. | The draft cash figure proves the loan is funded. | Everything is complete because one checklist item is marked received. | The statement reports the completed receipt milestone and preserves the two separate unresolved approval issues.
Who should explain the unresolved lien record? | The title professional handling the investigation | The coordinator by guessing from the appraisal | The buyer's neighbor based on a similar transaction | The lender's marketing brochure without checking the record | The briefing assigns the record investigation to the title professional; the coordinator should relay verified information.
Which statement properly limits the $25,000 amount? | It is a draft calculation; final figures and payment instructions need verification. | It is the final amount solely because it appears in a draft. | It replaces the need for any closing documents. | It proves the buyer's deposit was never paid. | The draft status prevents treating the figure as final or drawing unsupported conclusions about other amounts.
Which question distinguishes escrow uses? | Are we discussing transaction funds held pending conditions or the mortgage account for ongoing costs? | Does escrow always mean the same account with identical rules? | Does any escrow balance prove clear title? | Can an escrow label replace verification of payment instructions? | Escrow can name different arrangements, so the context must be identified before explaining its function.''',
    dialogue='''Aria | The checklist says appraisal received. Does that mean everything is ready to close and I can treat the remaining steps as routine?
Samir | It confirms receipt of the [[appraisal::The appraisal is a value-related document; receiving it does not establish that all title and lending conditions are complete.]], which is useful progress. It does not confirm that the lender has accepted every condition or that the separate title questions are resolved.
Aria | What is the title question? I do not want to hear simply that paperwork is pending without knowing which issue needs attention.
Samir | The title professional is investigating a recorded [[lien::The recorded lien is the identified title matter; its presence requires review rather than an unsupported assumption that it is cleared.]] associated with an earlier obligation. We have not verified the document showing that the relevant claim was released.
Aria | Does the fact that the loan may have been paid off mean we can ignore the entry in the records?
Samir | We need the title professional's explanation and verification of the [[lien release::A lien release addresses the recorded claim; an assumption about past payment is not confirmation that the required release is established.]]. I should not declare the record resolved from an assumption about what happened to the old loan.
Aria | We sent the lender everything they requested. What confirmation should I look for now, and who will tell me if something is still missing?
Samir | Final approval is not confirmed. The lender needs to report the current [[underwriting::Underwriting is the lender's assessment process; submitted documents do not themselves prove that its conditions are satisfied.]] status and any outstanding conditions. Sending requested records is not the same as receiving the lender's completed approval.
Aria | Would a clear-to-close message settle every part of the transaction, including title, payment figures, recording, and possession?
Samir | [[clear to close::Clear to close is a lender status within its process; it should not be used as a universal substitute for every transaction confirmation.]] is a lender status that needs its own terms and context. We should still confirm the other professionals' requirements and the contract's separate steps.
Aria | The settlement draft shows twenty-five thousand dollars. Is that what I should transfer now, or is it still a working figure?
Samir | It is draft [[cash to close::Cash to close is the amount due under a settlement calculation; a draft amount is not yet a verified instruction to pay.]], not a verified payment instruction. We need final figures and properly verified instructions before treating either the amount or destination as ready for action.
Aria | I would like to see why that figure differs from my down payment. There may be charges, credits, or deposits that I have not connected.
Samir | We can review the [[settlement statement::The settlement statement itemizes funds and charges, helping distinguish cash due from one component such as the down payment.]] with the closing professional. They can explain the actual components and any changes rather than have us guess which line creates the difference.
Aria | The documents also mention escrow in more than one place. Is the money held for this transaction the same as the account for taxes and insurance?
Samir | Not necessarily. [[escrow::Escrow can refer to transaction holding or a mortgage account for certain ongoing costs; the surrounding document determines the meaning.]] needs context. We should identify which arrangement each document means and ask the responsible professional to explain its purpose and terms.
Aria | Once everything is signed, I should not assume that funds have already been released or that the records office has completed its part.
Samir | Correct. Confirm [[disbursement::Disbursement is the release of funds, a distinct status that should be confirmed rather than inferred from signatures alone.]] and the other required steps through the closing process. Signatures, funding, recording, and possession should not be collapsed into one unsupported assurance.
Aria | Send me one update with a contact for each open item. At the moment I cannot tell which professional I should ask about which delay.
Samir | I will obtain those confirmations and the relevant [[recording::Recording is entry into the public records, with status and timing requiring the appropriate professional's confirmation.]] status when applicable. For now, appraisal received is complete; title, final lender approval, and verified closing instructions are not yet confirmed.''',
    transfer_title='The changed bank details need verification',
    transfer_setup='A buyer receives an unexpected email changing the closing-payment account. The closing professional has not confirmed the change. An established contact number from earlier verified documents is available.',
    transfer='''Buyer: "The account change is currently ___." | unverified | The unexpected message has not been confirmed through the established closing contact.
Coordinator: "Pause the ___ while it is checked." | transfer | No payment should be treated as ready solely on the basis of the unconfirmed account change.
Buyer: "I will use the previously verified contact ___." | number | The supplied trusted number avoids relying on new contact details inside the suspicious message.
Coordinator: "Obtain confirmation from the responsible closing ___." | professional | The closing professional is the appropriate source for verifying the instruction, not the unconfirmed email alone.''', rehearsal=["Check the key and read the closing update. Give appraisal received, lien release unverified, and final lender approval unconfirmed different emphasis.","Switch roles for turns 11-20. Keep $25,000 beside draft, and distinguish transaction escrow from the mortgage account for ongoing costs.","Complete the changed-bank-details exchange and check the answers. Read the pause and verification steps in order, using the previously verified contact number."]))


BOOK['units'].append(unit(
    title='Leasing, Property Management, Commercial Basics, Ethics, and Crisis Scenarios', scene='The leak is logged, but the tenant needs an update',
    skill='Acknowledge a missed response, establish current urgency, and give an owned update without inventing a repair appointment.',
    brief='Tenant Leo reported water under the kitchen sink on Monday and again Wednesday morning. Both reports are logged, but no appointment has been confirmed and no update was sent. Property coordinator Asha now owns the follow-up. The contractor has not yet replied. No immediate danger has been reported, but current conditions need checking. Asha can commit to a status update by 2 p.m., not completion of the repair. Entry arrangements and any rent adjustment require the applicable process; neither has been authorized.',
    cast='Leo | Tenant\nAsha | Property coordinator',
    culture=('A reference number is not a substantive response', 'An upset tenant may be asking for ownership and a reliable next contact, not only an apology. Acknowledge the specific missed update, check the present condition, and explain what is confirmed. A promised status update should remain distinct from an unconfirmed attendance time or remedy.'),
    a='''What has actually been completed? | Both reports have been logged | The contractor has confirmed a visit | The repair has been completed | A rent adjustment has been approved | The briefing confirms logging only; appointment, repair, and financial remedy remain unconfirmed.
What can Asha commit to by 2 p.m.? | A status update | A guaranteed completed repair | An approved rent reduction | An unconditional entry into the home | The authorized commitment is communication of status, not those unresolved operational or financial outcomes.
What needs checking now? | Current conditions and the appropriate response urgency | Whether the already stated Monday report existed | A presumed technical diagnosis by Asha | An automatic right to ignore entry requirements | The case says current conditions need checking, which informs urgency without authorizing diagnosis or bypassing entry rules.''',
    vocabulary='''lease | An agreement granting use of property on specified terms. | review the lease terms
lessor | The party granting the lease interest. | identify the lessor
lessee | The party receiving the lease interest. | identify the lessee
security deposit | Money held under lease and legal terms for specified obligations. | account for the security deposit
rent roll | A schedule of tenants, rents, and related lease information. | update the rent roll
arrears | Amounts due but unpaid after their due date. | verify rent arrears
work order | A recorded instruction or request for maintenance work. | open a work order
service request | A tenant's request for assistance or maintenance. | acknowledge the service request
triage | Initial assessment of urgency and appropriate response. | triage the maintenance report
active leak | Water escaping or entering at the time described. | report an active leak
emergency response | Immediate handling of a situation requiring urgent protective action. | use the emergency-response process
attendance window | A stated period during which a worker is expected to arrive. | confirm the attendance window
entry notice | Information about planned access under applicable lease and legal requirements. | check entry-notice requirements
access arrangement | Agreed or otherwise authorized practical terms for entering the property. | confirm the access arrangement
vendor | A supplier or contractor providing a service. | follow up with the vendor
repair authorization | Approval for specified repair work within the relevant authority. | obtain repair authorization
completion record | Evidence documenting that specified work has been finished. | verify the completion record
service recovery | Action to address a service failure and restore a reliable process. | coordinate service recovery
rent adjustment | A change or credit to rent under an authorized agreement or requirement. | review a requested rent adjustment
renewal option | A contractual right to extend a lease under defined conditions. | review the renewal option
break clause | A provision allowing a lease to end early under stated conditions. | check the break clause
permitted use | The activities allowed in the premises under the lease and applicable rules. | confirm the permitted use
tenant improvement | Work adapting leased premises for the tenant's use. | define tenant-improvement responsibilities
common-area maintenance | Shared-property maintenance costs allocated under specified lease terms. | reconcile common-area maintenance charges''',
    precision='Logged, assigned, scheduled, attended, and completed describe different maintenance stages. Here the reports are logged and Asha owns follow-up, but the contractor has not confirmed attendance. A 2 p.m. status commitment must not be restated as a 2 p.m. repair promise.',
    precision_extra='Entry rules, repair duties, rent remedies, and commercial charge allocations depend on the actual lease and applicable law. Do not assume that a maintenance request authorizes every access arrangement or that a complaint automatically determines a rent adjustment.',
    phrases='''Acknowledge the failure | You reported this twice and did not receive an update.
Take ownership | I am responsible for the follow-up now.
Check the present | Is water still appearing, and has the situation changed?
Assess urgency | Please report any immediate danger through the appropriate emergency route.
Give the real status | The contractor has not yet confirmed an appointment.
Commit to communication | I will update you by 2 p.m. even if the visit time remains unresolved.
Separate the promise | That is a status-update time, not a guaranteed repair completion.
Close with the record | I will record the current facts, owner, and next contact.
Confirm access | We need to follow the applicable entry requirements and arrangements.
Avoid diagnosis | I cannot identify the cause from the message alone.
Track the contractor | I will follow up with the vendor and escalate the unanswered request.
Preserve the history | Both earlier reports should remain linked to the work order.
Clarify a remedy | A rent adjustment requires the appropriate review; it is not approved yet.
Verify completion | We will check what work was done before closing the request.
Check commercial terms | Shared maintenance charges depend on the lease's allocation rules.
Keep the tenant informed | A logged ticket should not replace a meaningful response.''',
    notes='''By 2 p.m. | State what will happen by that time; a communication deadline is not an attendance guarantee.
Still versus again | Still asks whether a condition continues; again asks whether it has recurred.
Assigned versus scheduled | An owner can be assigned even when no visit is booked.
Reported danger | Record the actual information without declaring safety from an incomplete remote description.
Requested credit | A financial request is not approval of a remedy.
Closed ticket | A closed record should reflect the verified workflow state, not simply the sending of a message.''',
    d='''Which response combines empathy with accurate ownership? | You reported this twice without an update; I own the follow-up and will update you by 2 p.m. | The ticket exists, so the service issue is already resolved. | The contractor will certainly finish by 2 p.m. | Every rent remedy is automatically approved after two reports. | The response acknowledges the specific failure and makes the authorized communication commitment without inventing an outcome.
Which status pair accurately describes the maintenance case? | Reports logged; contractor attendance unconfirmed | Reports assigned; contractor attendance provisionally accepted | Visit confirmed; repair completion awaiting evidence | Repair authorized; entry arrangements already agreed | Logging and follow-up ownership are confirmed, but the contractor has not replied. That is not acceptance of a visit, repair authorization, or an access agreement.
What should happen before treating the request as completed? | Verify the actual work and record the resulting status. | Close it after sending a reference number. | Assume silence proves a repair occurred. | Replace both earlier reports with a new blank record. | Completion requires evidence of the relevant work, not merely a communication or an absence of further messages.
Which statement keeps the rent question within scope? | The requested adjustment needs the applicable review and is not approved yet. | Any leak automatically cancels all rent obligations. | A coordinator can promise any credit without authority. | Commercial and residential leases have identical remedy rules everywhere. | The supplied facts establish no authorized adjustment, and actual rights require the relevant lease and law.''',
    dialogue='''Leo | This is my second call about water under the kitchen sink. Monday's report got a reference number. This morning's got another one.
Asha | I can see both [[service requests::Service requests record the tenant's reports; their existence does not mean attendance or repair has been arranged.]]. You should have had an update, and I am taking ownership now. Is water still appearing?
Leo | Yes. I have not reported immediate danger, but I do not know what is causing it. Has anyone agreed to come?
Asha | I will record the [[active leak::An active leak describes the current continuing condition; it affects urgency without establishing the technical cause.]] and reassess urgency through our response process. If immediate danger develops, keep clear and use the appropriate emergency route.
Leo | I need an appointment, not another reference number. Can you tell me when the contractor is coming?
Asha | I cannot confirm an [[attendance window::An attendance window is a confirmed expected arrival period; none has been supplied by the contractor yet.]] yet. The contractor has not replied. I will escalate that unanswered request with the property team now.
Leo | Please do not start the whole process again. Someone needs to know that I reported this two days ago.
Asha | I will link both reports in the [[work order::The work order should preserve the linked reports, current condition, and responsible owner rather than treat the second report as unrelated.]] and preserve the Monday history. The new call will not replace the earlier record.
Leo | When will you call me? Last time I was told someone would be in touch, and nobody was.
Asha | By two this afternoon, even if the appointment is still unresolved. That is part of putting the [[service recovery::Service recovery addresses the missed communication with an owned next step; it does not create a guaranteed repair result.]] into practice, not a repair-completion promise.
Leo | I may be at work when someone becomes available. I have not agreed that anybody can let themselves in.
Asha | Understood. We need to confirm the [[access arrangement::Access arrangements must follow the applicable requirements and practical agreement; the report does not authorize unrestricted entry.]] and follow the relevant entry requirements. I will explain the proposed visit and notice before assuming access.
Leo | What happens if the contractor finds work that needs the owner's approval? I do not want another unexplained delay.
Asha | I will identify who handles the [[repair authorization::Repair authorization defines approval for specified work; contacting a contractor does not automatically approve every possible additional task.]] and track the response. The assessment will establish what work is proposed; I cannot approve an unknown scope now.
Leo | And will this ticket disappear once you send another message? That is what this process has felt like so far.
Asha | A message is not a [[completion record::A completion record supports the actual work status; a phone call or reference number alone is not proof of repair.]]. We need evidence of the actual work and its status, and I will keep the communication complaint on record.
Leo | I also want to ask about a rent credit. Please tell me where that request goes.
Asha | I will route the [[rent adjustment::A rent adjustment requires the applicable authority, agreement, or legal basis; no approval exists in this case.]] request for the applicable review. I can confirm it has been raised, but I cannot promise an amount or approval.
Leo | All right. Call by two, tell me whether anyone has accepted the job, and explain the next step if they have not.
Asha | I will. We will also update the [[triage::Triage assesses urgency and response as conditions develop; it should continue alongside scheduling and communication.]] if conditions change. Today you will hear the confirmed status and who is handling each outstanding item.''',
    transfer_title='Base rent does not include every charge',
    transfer_setup='A commercial lease proposal states $2,000 monthly base rent plus the tenant\'s defined share of common-area maintenance. The maintenance estimate and allocation details have not yet been supplied.',
    transfer='''Tenant: "The $2,000 is the monthly base ___." | rent | The proposal identifies that amount as base rent, not the entire occupancy cost.
Agent: "Common-area maintenance is an additional ___." | charge | The proposal adds a defined share of maintenance rather than including it in the base amount.
Tenant: "We still need the allocation ___." | details | The method for determining the tenant's share is explicitly missing from the supplied information.
Agent: "Do not present $2,000 as the complete monthly ___." | total | An additional, unquantified charge prevents the base rent from being described as the full monthly amount.''', rehearsal=["Check the key, then read the maintenance call. Let Leo sound frustrated while Asha acknowledges both reports and asks about the current water problem.","Switch roles for turns 9-20. Stress update by two, not repair by two; keep contractor attendance, entry, and any rent credit unconfirmed.","Complete and check the commercial-rent exchange. Read $2,000 as base rent, with maintenance allocation details still needed before stating a total."]))
