from __future__ import annotations

import html
from pathlib import Path

from reportlab.platypus import PageBreak, Paragraph, Spacer

from generate_efsp_guarded_activities import add_answer_key, add_cloze_exercise, bounded_activity_instruction, make_dialogue_cloze
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
                "Focus: high-level professional English for real estate workplaces, including agency, representation agreements, buyer and seller consultations, pricing, property descriptions, fair housing, offers, contingencies, inspections, appraisals, financing, disclosures, title, escrow, closings, leasing, commercial basics, and realistic transaction dialogue.",
                "Designed for advanced ESL learners who work as agents, brokers, assistants, transaction coordinators, property managers, leasing staff, commercial real estate staff, relocation specialists, mortgage-adjacent staff, title-adjacent staff, or real-estate business partners.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: real estate English is trust, precision, and risk control under time pressure. Learners need language that is persuasive but not misleading, helpful but not discriminatory, confident but not legally careless. This curriculum teaches professional communication and judgment, not state-specific legal advice.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use real estate terminology accurately in client consultations, listing presentations, buyer tours, offer strategy, negotiation, inspection discussions, appraisal issues, financing updates, transaction coordination, leasing conversations, and closing calls.",
    "Explain agency relationships, representation agreements, compensation, disclosure duties, conflicts of interest, fair housing constraints, referral risk, and transaction timelines in clear professional English.",
    "Translate client emotions and vague requests into useful real estate questions, objective criteria, documentation needs, and next steps.",
    "Push back on unsafe requests: discriminatory preferences, steering pressure, inflated pricing, hidden defects, unsupported claims, unauthorized legal advice, referral-kickback pressure, and risky waiver language.",
    "Participate in realistic real estate dialogues: buyer intake, seller pricing, fair housing questions, multiple offers, repair credits, low appraisal, underwriting delay, dual agency, lead disclosure, leasing, and commercial terms.",
    "Write clear real estate outputs: buyer consultation summaries, showing follow-ups, CMA explanations, offer summaries, repair-request language, transaction updates, disclosure reminders, fair-housing-safe responses, and closing checklists.",
]


MODULES = [
    {
        "title": "Module 1. Agency, Representation, Compensation, and Trust",
        "time": "90 minutes",
        "big_idea": "Real estate professionals need language for who they represent, what duties they owe, how compensation works, and what the client is agreeing to before advice becomes transaction-critical.",
        "objectives": [
            "Distinguish client, customer, agency, fiduciary duty, representation agreement, listing agreement, buyer agreement, dual agency, designated agency, and transaction brokerage.",
            "Explain written buyer agreements and compensation language without sounding defensive or evasive.",
            "Clarify when a professional can advise, when they must disclose, and when they should refer to legal, tax, lending, or inspection experts.",
        ],
        "concepts": [
            "Agency: a legal relationship in which a real estate professional acts for a client, subject to state law and brokerage policy.",
            "Representation agreement: a written agreement that defines services, term, compensation, exclusivity, and termination language.",
            "Compensation disclosure: clear language about how brokerage compensation is determined, who may pay it, and what is negotiable.",
        ],
        "activities": [
            "Buyer agreement explanation: learners explain the agreement before a property tour.",
            "Role boundary drill: learners sort questions into real estate advice, lending advice, legal advice, tax advice, and referral-needed categories.",
            "Conflict map: learners identify possible conflicts in dual agency, same-brokerage offers, and referral relationships.",
        ],
        "outputs": [
            "Buyer consultation script.",
            "Agency and compensation explanation.",
            "Role-boundary phrase bank.",
        ],
    },
    {
        "title": "Module 2. Client Intake, Needs Analysis, and Property Search",
        "time": "90 minutes",
        "big_idea": "Good real estate conversations move from emotion to criteria: budget, timeline, location needs, property type, financing readiness, risk tolerance, and decision process.",
        "objectives": [
            "Ask precise intake questions without sounding intrusive or robotic.",
            "Separate must-haves, nice-to-haves, deal breakers, assumptions, and tradeoffs.",
            "Respond to neighborhood, school, safety, and demographic questions with fair-housing-safe language and objective resources.",
        ],
        "concepts": [
            "Needs analysis: a structured conversation that clarifies goals, constraints, decision-makers, financing, timeline, and risk tolerance.",
            "Search criteria: objective filters such as price, bedrooms, commute, property condition, HOA, school district boundaries, zoning, and accessibility features.",
            "Steering risk: directing or discouraging clients toward or away from areas based on protected-class characteristics.",
        ],
        "activities": [
            "Buyer intake role-play: learners turn broad preferences into objective search criteria.",
            "Fair housing response drill: learners answer sensitive neighborhood questions using objective sources.",
            "Tradeoff negotiation: learners explain why a buyer may need to adjust price, condition, location, or timeline.",
        ],
        "outputs": [
            "Client intake checklist.",
            "Fair-housing-safe response set.",
            "Search criteria summary email.",
        ],
    },
    {
        "title": "Module 3. Listings, Property Descriptions, Pricing, and Market Data",
        "time": "90 minutes",
        "big_idea": "Listing and pricing language must be attractive, accurate, objective, and defensible. Learners need to discuss comps, condition, market movement, and seller expectations without overpromising.",
        "objectives": [
            "Use CMA, comp, active, pending, closed, DOM, concessions, list-to-sale ratio, appraisal, and absorption terminology accurately.",
            "Explain pricing strategy to a seller who wants a number above market evidence.",
            "Write property descriptions that highlight property features without discriminatory implications or unsupported claims.",
        ],
        "concepts": [
            "CMA: comparative market analysis using recent relevant sales, active competition, pending activity, condition, location, and adjustments.",
            "Pricing strategy: the logic behind list price, timing, market exposure, competition, and adjustment plan.",
            "Material fact: information that could affect a buyer's decision or property value, subject to state law and disclosure rules.",
        ],
        "activities": [
            "CMA explanation: learners present three comps and explain adjustments.",
            "Overpricing pushback: learners respond when a seller wants to test the market too high.",
            "Listing copy audit: learners remove unsafe demographic language and unsupported claims.",
        ],
        "outputs": [
            "CMA presentation script.",
            "Seller pricing follow-up.",
            "Fair-housing-safe listing description.",
        ],
    },
    {
        "title": "Module 4. Showings, Open Houses, Fair Housing, and Advertising",
        "time": "90 minutes",
        "big_idea": "Showings and advertising create high-risk language moments. Real estate professionals must be warm, informative, and useful without steering, discriminating, or making claims they cannot support.",
        "objectives": [
            "Respond to questions about neighborhood, schools, crime, demographics, religion, families, disability access, and safety with appropriate objective-resource language.",
            "Explain fair housing concepts such as protected class, steering, redlining, blockbusting, reasonable accommodation, and discriminatory advertising.",
            "Handle open-house conversations with represented buyers, unrepresented buyers, and visitors who ask for advice outside the professional's role.",
        ],
        "concepts": [
            "Fair housing: federal, state, and local rules protecting people from discrimination in housing-related activities.",
            "Objective resource: a neutral third-party source such as municipal data, school district maps, crime statistics, public transit maps, flood maps, HOA documents, or inspection reports.",
            "Advertising compliance: property and service advertising should be truthful, clear, and free of preferences or limitations based on protected characteristics.",
        ],
        "activities": [
            "Forbidden question practice: learners answer sensitive buyer questions without shaming the client.",
            "Open-house boundary drill: learners explain who they represent and what they can discuss.",
            "Ad rewrite: learners revise rental or listing ads that imply preferences.",
        ],
        "outputs": [
            "Fair housing response bank.",
            "Open-house disclosure script.",
            "Advertising compliance checklist.",
        ],
    },
    {
        "title": "Module 5. Offers, Counteroffers, Negotiation, and Contingencies",
        "time": "90 minutes",
        "big_idea": "Offer strategy requires precise language around price, financing, earnest money, contingencies, timelines, concessions, appraisal risk, inspection risk, and seller priorities.",
        "objectives": [
            "Use offer terminology accurately: earnest money, contingency, counteroffer, escalation clause, appraisal gap, seller concession, backup offer, possession, and rent-back.",
            "Explain tradeoffs between competitiveness and protection.",
            "Summarize competing offers without exaggeration, unauthorized disclosure, or pressure language.",
        ],
        "concepts": [
            "Contingency: a condition that must be satisfied for the contract to proceed, such as inspection, financing, appraisal, sale of home, or title review.",
            "Earnest money: buyer deposit showing seriousness, subject to contract terms and potential forfeiture risk.",
            "Appraisal gap: difference between contract price and appraised value that may require renegotiation, additional buyer cash, or other contract solutions.",
        ],
        "activities": [
            "Offer strategy workshop: learners build an offer from buyer priorities and market context.",
            "Counteroffer role-play: learners negotiate price, closing date, repairs, and concessions.",
            "Risk explanation: learners explain why waiving protections may make an offer stronger but riskier.",
        ],
        "outputs": [
            "Offer comparison summary.",
            "Negotiation phrase bank.",
            "Buyer risk memo.",
        ],
    },
    {
        "title": "Module 6. Inspections, Repairs, Disclosures, and Due Diligence",
        "time": "90 minutes",
        "big_idea": "After contract, language becomes tense. Learners need to discuss defects, repair requests, seller disclosures, inspection scope, specialist referrals, and deal uncertainty without blame or panic.",
        "objectives": [
            "Discuss inspection findings, material defects, seller disclosure, lead-based paint, property condition, repair requests, credits, and due diligence periods.",
            "Separate factual observation, expert opinion, negotiation strategy, and legal advice.",
            "Write repair-request and disclosure follow-up language that is clear, calm, and documented.",
        ],
        "concepts": [
            "Due diligence: the buyer's period or process for investigating property condition, title, financing, HOA, insurance, zoning, and other risks.",
            "Seller disclosure: information the seller provides about known property conditions, subject to state law and transaction documents.",
            "Lead-based paint disclosure: federal disclosure duties for many pre-1978 homes, including known information, records, pamphlet, and required warning language.",
        ],
        "activities": [
            "Inspection debrief: learners explain serious, moderate, and minor findings.",
            "Repair credit negotiation: learners convert an emotional complaint into a specific request.",
            "Disclosure escalation: learners respond when a client wants to hide or minimize a known issue.",
        ],
        "outputs": [
            "Inspection debrief script.",
            "Repair request email.",
            "Disclosure escalation note.",
        ],
    },
    {
        "title": "Module 7. Financing, Appraisal, Title, Escrow, and Closing",
        "time": "90 minutes",
        "big_idea": "Closings depend on many parties and documents. Learners need language for mortgage status, underwriting conditions, Loan Estimate, Closing Disclosure, title issues, escrow, prorations, walk-through, and closing delays.",
        "objectives": [
            "Explain pre-approval, proof of funds, underwriting, conditional approval, clear to close, appraisal, title search, lien, escrow, prorations, Loan Estimate, Closing Disclosure, and cash to close.",
            "Coordinate updates among buyer, seller, lender, title, escrow, attorney, inspector, and brokerage without overstepping.",
            "Handle closing delays with timelines, owners, dependencies, and next steps.",
        ],
        "concepts": [
            "TRID: integrated mortgage disclosure framework using Loan Estimate and Closing Disclosure forms for many mortgage transactions.",
            "Title issue: a lien, ownership question, easement, judgment, or other matter that may affect transfer or insurability.",
            "Clear to close: lender status indicating underwriting conditions have been satisfied, subject to final checks and closing steps.",
        ],
        "activities": [
            "Closing status update: learners write a concise update with owners and deadlines.",
            "Loan document explanation: learners explain that lender documents must be reviewed with the lender, not replaced by agent advice.",
            "Title problem role-play: learners explain a delay without blaming title, lender, or client.",
        ],
        "outputs": [
            "Closing checklist.",
            "Transaction update template.",
            "Delay communication script.",
        ],
    },
    {
        "title": "Module 8. Leasing, Property Management, Commercial Basics, Ethics, and Crisis Scenarios",
        "time": "90 minutes",
        "big_idea": "Real estate English is broader than residential sales. Learners need enough language for leases, screening, property management, commercial terms, referral boundaries, complaints, and reputational risk.",
        "objectives": [
            "Use leasing and commercial terms such as lease term, security deposit, rent roll, CAM, NNN, NOI, cap rate, LOI, TI allowance, estoppel, and operating expenses.",
            "Discuss tenant screening, reasonable accommodation, habitability, maintenance, rent collection, and lease enforcement with fairness and documentation.",
            "Respond to ethical pressure, referral-kickback risk, public complaints, and transaction breakdowns with documented, policy-aware language.",
        ],
        "concepts": [
            "RESPA referral risk: federal restrictions can apply to fees, kickbacks, or things of value connected to referrals of settlement-service business.",
            "Commercial LOI: nonfinal letter of intent often used to outline major deal terms before lease or purchase documents.",
            "Crisis response: calm, factual, documented communication that protects clients, compliance, and reputation.",
        ],
        "activities": [
            "Leasing screening language: learners explain criteria without discriminatory shortcuts.",
            "Commercial term explanation: learners explain NNN, CAM, NOI, and cap rate in plain English.",
            "Ethics scenario: learners respond when a partner offers a benefit tied to referrals.",
        ],
        "outputs": [
            "Leasing conversation script.",
            "Commercial term mini-glossary.",
            "Ethics escalation email.",
        ],
    },
]


COURSE_OBJECTIVES = [bounded_activity_instruction(item) for item in COURSE_OBJECTIVES]
for _module in MODULES:
    _module["objectives"] = [bounded_activity_instruction(item) for item in _module["objectives"]]
    _module["activities"] = [bounded_activity_instruction(item) for item in _module["activities"]]


JARGON_GROUPS = [
    (
        "Agency, representation, and compensation",
        [
            ("Client", "A person represented by the real estate professional under an agency or representation relationship."),
            ("Customer", "A person receiving limited services or information but not represented as a client, depending on state law."),
            ("Agency disclosure", "Required explanation or document identifying the professional's role and who is represented."),
            ("Fiduciary duty", "Duties such as loyalty, confidentiality, disclosure, obedience, reasonable care, and accounting, depending on law and role."),
            ("Listing agreement", "Contract between seller and brokerage defining listing services, term, price, compensation, and conditions."),
            ("Buyer representation agreement", "Agreement defining buyer services, term, compensation, exclusivity, and other obligations."),
            ("Dual agency", "Representation of both buyer and seller in the same transaction where allowed and properly disclosed."),
            ("Designated agency", "Same brokerage but different designated agents represent different clients, where permitted."),
        ],
    ),
    (
        "Property, market, and valuation",
        [
            ("CMA", "Comparative market analysis using comparable properties and market data to support pricing."),
            ("Comp", "Comparable property used to estimate likely market value."),
            ("List price", "Price at which the property is offered to the market."),
            ("Sale price", "Final contract or closed price, depending on context."),
            ("DOM", "Days on market; how long a property has been publicly listed under local rules."),
            ("Concession", "Seller or landlord contribution to buyer or tenant costs, repairs, or other terms."),
            ("Appraisal", "Independent opinion of value often required by a lender."),
            ("Absorption rate", "Pace at which available inventory is sold or leased in a market segment."),
        ],
    ),
    (
        "Buyer and seller transaction terms",
        [
            ("Pre-approval", "Lender review indicating likely borrowing capacity, subject to underwriting and property review."),
            ("Proof of funds", "Documentation showing funds available for cash purchase or down payment."),
            ("Earnest money", "Deposit showing buyer seriousness, handled according to contract and escrow rules."),
            ("Contingency", "Contract condition that must be satisfied or waived for the transaction to continue."),
            ("Inspection period", "Time allowed for property inspection and related negotiations."),
            ("Appraisal gap", "Difference between contract price and appraised value that can create financing or negotiation issues."),
            ("Escalation clause", "Offer term that may increase price under specified competing-offer conditions."),
            ("Backup offer", "Offer accepted or held in position if the primary contract fails, depending on local practice."),
        ],
    ),
    (
        "Financing, title, escrow, and closing",
        [
            ("Loan Estimate", "Mortgage disclosure showing estimated loan terms, payments, closing costs, and cash to close."),
            ("Closing Disclosure", "Mortgage disclosure showing final or near-final loan terms, costs, and cash to close."),
            ("Underwriting", "Lender review of borrower, property, income, assets, credit, and loan risk."),
            ("Clear to close", "Lender status indicating conditions are substantially satisfied for closing."),
            ("Title search", "Review of public records to confirm ownership and identify liens, easements, or other issues."),
            ("Lien", "Legal claim against property that may need resolution before or during closing."),
            ("Escrow", "Neutral holding and coordination of funds, documents, or closing conditions, depending on state practice."),
            ("Proration", "Allocation of taxes, HOA dues, rent, or other costs between parties by date."),
        ],
    ),
    (
        "Disclosure, fair housing, and risk",
        [
            ("Protected class", "A legally protected characteristic under federal, state, or local fair housing laws."),
            ("Steering", "Directing people toward or away from housing based on protected-class characteristics."),
            ("Redlining", "Denying or limiting housing-related services in areas based on protected characteristics or similar unlawful criteria."),
            ("Blockbusting", "Inducing sales by suggesting protected-class changes will affect property values or neighborhood conditions."),
            ("Reasonable accommodation", "Change in rules or services that may be needed for a person with a disability."),
            ("Material fact", "Fact that could affect a party's decision or property value, subject to applicable law."),
            ("Lead-based paint disclosure", "Federal disclosure requirements for many pre-1978 residential properties."),
            ("RESPA Section 8", "Federal restrictions on kickbacks, unearned fees, and referral payments in covered settlement services."),
        ],
    ),
    (
        "Leasing, property management, and commercial",
        [
            ("Lease term", "Length and conditions of a lease agreement."),
            ("Security deposit", "Funds held to cover certain tenant obligations, subject to state and local rules."),
            ("Screening criteria", "Objective rental applicant criteria such as income, credit, rental history, and occupancy rules."),
            ("Rent roll", "Schedule of rents, tenants, lease dates, and payment status for a property."),
            ("CAM", "Common area maintenance charges in some commercial leases."),
            ("NNN", "Triple net lease structure where tenant may pay taxes, insurance, and maintenance in addition to base rent."),
            ("NOI", "Net operating income; property income after operating expenses but before debt service and some other items."),
            ("Cap rate", "Capitalization rate; NOI divided by property value or price, used as a valuation shorthand."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. Buyer Consultation: Agreement Before Touring",
        "setting": "A buyer wants to see a house immediately but has not discussed representation or compensation.",
        "dialogue": [
            ("Buyer", "Can you show me the house this afternoon? I do not want to sign anything yet."),
            ("Agent", "I understand. Before I tour property with you as your agent, we need a written agreement that explains my services, the term, and how compensation works."),
            ("ESL learner", "This agreement is not meant to pressure you. It defines who I represent, what I can do for you, and what compensation we agree to. We can keep the term narrow if you only want to evaluate this property."),
            ("Buyer", "So I have to pay you?"),
            ("ESL learner", "Compensation is negotiable and may be paid in different ways depending on the offer and transaction. The important point is that we discuss it clearly before we start representation."),
        ],
        "notes": [
            "Explain agreement and compensation calmly before advice becomes transaction-specific.",
            "Use transparent language without implying compensation is fixed or required by law.",
        ],
    },
    {
        "title": "2. Fair Housing Question: 'Is This a Good Neighborhood?'",
        "setting": "A buyer asks for subjective neighborhood advice that could lead to steering.",
        "dialogue": [
            ("Buyer", "Is this a good neighborhood for families like us?"),
            ("Agent", "I can help you compare objective information, but I cannot steer you based on who lives here."),
            ("ESL learner", "Let's define what 'good' means for you: commute time, budget, property condition, parks, school district boundaries, noise, transit, or walkability. I can point you to public resources so you can evaluate the area using your own priorities."),
            ("Buyer", "But would you live here?"),
            ("ESL learner", "I should not substitute my personal preference for your decision. I can give you property facts and objective sources, and you can decide whether the area fits your needs."),
        ],
        "notes": [
            "Do not shame the client; redirect to objective criteria.",
            "Avoid statements that imply preference based on protected-class characteristics.",
        ],
    },
    {
        "title": "3. Listing Presentation: Seller Wants an Unrealistic Price",
        "setting": "A seller wants to list far above the CMA range because a neighbor got a high price last year.",
        "dialogue": [
            ("Seller", "My neighbor sold for more last year. I want to list at that number plus 10 percent."),
            ("Listing agent", "The market has changed since then."),
            ("ESL learner", "We can test a premium only if the evidence supports it. The closest recent comps show lower closed prices, longer DOM, and seller concessions. If we list too high, we may reduce urgency and help competing listings look more attractive."),
            ("Seller", "I do not want to leave money on the table."),
            ("ESL learner", "Neither do I. My recommendation is a price that creates serious buyer activity and gives us leverage. We can also agree now on a review point if showings or feedback are weak."),
        ],
        "notes": [
            "Pricing pushback should protect the relationship and the market logic.",
            "Use data, timing, and adjustment plan instead of arguing over ego.",
        ],
    },
    {
        "title": "4. Multiple Offers: Stronger Terms vs Higher Price",
        "setting": "A buyer wants to win in a competitive situation but does not understand the risk of waiving protections.",
        "dialogue": [
            ("Buyer", "Let's waive everything and offer over asking."),
            ("Agent", "That may strengthen the offer, but it changes your risk."),
            ("ESL learner", "We should compare price, appraisal gap, inspection rights, financing contingency, earnest money, closing date, and seller priorities. A stronger offer is not just a higher price. It is also certainty and clean terms."),
            ("Buyer", "Can we waive inspection?"),
            ("ESL learner", "You can choose that strategy, but I want you to understand the risk. Another option is a shorter inspection period, informational inspection, or cap on repair requests, depending on local practice and your comfort level."),
        ],
        "notes": [
            "Protect the distinction between competitiveness and risk.",
            "Do not make waiver decisions sound routine or harmless.",
        ],
    },
    {
        "title": "5. Inspection Negotiation: Repair Credit",
        "setting": "An inspection found roof and electrical issues. The buyer is angry and wants the seller to fix everything.",
        "dialogue": [
            ("Buyer", "This house has problems. Ask them to fix every item."),
            ("Agent", "We need to separate major issues from normal maintenance."),
            ("ESL learner", "The strongest request will focus on safety, systems, and cost. Instead of sending a long emotional list, we can ask for a licensed electrician to address the panel issue and request a credit toward the roof repair, supported by the inspection report and estimate."),
            ("Buyer", "What if they refuse?"),
            ("ESL learner", "Then we evaluate your contract options, your appetite for repairs, and whether a revised price or credit makes the risk acceptable."),
        ],
        "notes": [
            "Convert anger into specific, document-supported requests.",
            "Separate inspection facts from negotiation strategy.",
        ],
    },
    {
        "title": "6. Low Appraisal: Contract Price Is Higher Than Appraised Value",
        "setting": "The appraisal comes in below contract price and financing is affected.",
        "dialogue": [
            ("Lender", "The appraisal is twenty thousand below contract price."),
            ("Buyer", "Does that mean the deal is dead?"),
            ("ESL learner", "Not automatically. We have several paths: challenge the appraisal if there are factual issues, renegotiate price, increase down payment, use an appraisal-gap clause if one exists, or cancel if the contract allows it."),
            ("Buyer", "What should we do?"),
            ("ESL learner", "First, let's review the appraisal with the lender and compare it to our comps. Then we can choose a negotiation position based on your cash, contract rights, and risk tolerance."),
        ],
        "notes": [
            "Low appraisal language should be calm and options-based.",
            "Do not promise the appraisal can be changed.",
        ],
    },
    {
        "title": "7. Financing Delay: Underwriting Conditions",
        "setting": "Closing is approaching but the lender still needs documentation.",
        "dialogue": [
            ("Seller agent", "Are your buyers clear to close? We need certainty."),
            ("Buyer agent", "The file is still in underwriting."),
            ("ESL learner", "The lender has issued conditional approval and is waiting on two documents from the buyer. We expect an update tomorrow afternoon. I do not want to overpromise, so I will send a written status update by 4 p.m. with any impact on closing."),
            ("Seller agent", "Should we issue a notice?"),
            ("ESL learner", "I understand your concern. Please send any contract notice through the proper channel. Meanwhile, I will keep the timeline, owner, and dependency clear for everyone."),
        ],
        "notes": [
            "Use precise status language: condition, owner, deadline, impact.",
            "Avoid blaming lender or buyer while uncertainty remains.",
        ],
    },
    {
        "title": "8. RESPA Risk: Referral Benefit",
        "setting": "A settlement-service provider offers valuable benefits for referrals.",
        "dialogue": [
            ("Vendor", "If you send us your buyers, we can sponsor your client event and give you premium tickets."),
            ("Agent", "That sounds generous, but we need to be careful."),
            ("ESL learner", "I cannot accept anything of value in exchange for settlement-service referrals. If we discuss marketing or sponsorship, it must be reviewed by the broker and compliance, tied to real services, and not conditioned on referrals."),
            ("Vendor", "Everyone does it."),
            ("ESL learner", "Our policy is to protect clients and avoid referral-kickback risk. I can share your public information with clients if they ask for options, but I cannot trade referrals for benefits."),
        ],
        "notes": [
            "Referral pressure requires direct, documented refusal.",
            "Use broker and compliance review rather than improvising.",
        ],
    },
    {
        "title": "9. Seller Disclosure: Known Water Intrusion",
        "setting": "A seller wants to avoid disclosing a past water problem because it was repaired.",
        "dialogue": [
            ("Seller", "Do we really need to mention the basement leak? It was fixed two years ago."),
            ("Agent", "Known property issues can create disclosure duties."),
            ("ESL learner", "I cannot tell you how to complete the legal disclosure form, but I can tell you not to hide known facts. Let's review the form instructions, gather repair records, and if you are unsure, ask your attorney before we publish or respond to buyers."),
            ("Seller", "I am afraid buyers will panic."),
            ("ESL learner", "Clear disclosure with documentation can reduce surprises later. A hidden issue can create a much larger trust and contract problem."),
        ],
        "notes": [
            "Do not complete legal disclosure decisions for the client.",
            "Encourage truth, documentation, and expert review.",
        ],
    },
    {
        "title": "10. Lead-Based Paint Disclosure",
        "setting": "A pre-1978 home is going under contract and documents are incomplete.",
        "dialogue": [
            ("Transaction coordinator", "The lead disclosure form is missing the buyer acknowledgment."),
            ("Agent", "Can we just send it after signatures?"),
            ("ESL learner", "For pre-1978 housing, the lead disclosure process needs to be handled before the buyer is obligated under the contract. We need the required pamphlet, known information, available records, and signed acknowledgment in the file."),
            ("Agent", "The seller does not know of any lead paint."),
            ("ESL learner", "That may be the seller's disclosure position, but the required disclosure process still matters. Let's correct the file before moving forward."),
        ],
        "notes": [
            "Lead disclosure is a document and timing conversation, not only a knowledge conversation.",
            "Use process language and file discipline.",
        ],
    },
    {
        "title": "11. Dual Agency or Same-Brokerage Conflict",
        "setting": "A buyer wants to make an offer on a listing held by the same brokerage.",
        "dialogue": [
            ("Buyer", "Can you still represent me if your office has the listing?"),
            ("Agent", "It depends on state law, brokerage policy, and the agency structure."),
            ("ESL learner", "We need to disclose the relationship clearly and explain whether this is dual agency, designated agency, or another permitted arrangement. You should understand what advice I can and cannot give before you decide whether to consent."),
            ("Buyer", "Will you tell me what the seller will accept?"),
            ("ESL learner", "I cannot share confidential information from another client or side. My role and limits must be clear before we proceed."),
        ],
        "notes": [
            "Conflict language should be explicit, not casual.",
            "Confidentiality survives pressure from the other side.",
        ],
    },
    {
        "title": "12. Commercial Lease: NNN and TI Allowance",
        "setting": "A small business owner is reviewing a commercial lease proposal.",
        "dialogue": [
            ("Tenant", "The rent looks affordable. It says NNN, CAM, and TI allowance. What does that mean?"),
            ("Commercial agent", "Those terms affect your real occupancy cost."),
            ("ESL learner", "Base rent is only one part. NNN usually means you may pay taxes, insurance, and maintenance in addition to base rent. CAM covers common area maintenance. A TI allowance is landlord contribution toward tenant improvements, but the lease will define conditions and repayment risk."),
            ("Tenant", "So can I sign the LOI?"),
            ("ESL learner", "An LOI can frame the deal, but you should review lease language with legal and financial advisors before committing. Let's compare total occupancy cost, term, options, buildout timeline, and exit risk."),
        ],
        "notes": [
            "Commercial terms need plain-English financial consequences.",
            "Refer legal and tax interpretation to qualified advisors.",
        ],
    },
]


PHRASE_BANK = {
    "Agency and role clarity": [
        "Before I advise you as a client, we need to clarify representation and compensation.",
        "My role is to explain the process and market context; legal interpretation should come from your attorney.",
        "This agreement defines the services, term, compensation, and termination process.",
        "Because the relationship could create a conflict, we need clear disclosure and informed consent before proceeding.",
    ],
    "Fair housing and objective resources": [
        "I cannot steer you based on who lives in an area, but I can help you compare objective criteria.",
        "Let's define what matters to you: commute, schools, budget, property condition, noise, transit, or amenities.",
        "I can direct you to public resources so you can make your own neighborhood assessment.",
        "The safest description focuses on property features, not the type of person who might live there.",
    ],
    "Pricing and market data": [
        "The strongest price recommendation is the one we can defend with relevant comps.",
        "If we list above the evidence, we should agree now on a review point and adjustment plan.",
        "Active listings show competition; closed sales show what buyers actually paid.",
        "A premium price needs premium evidence: condition, location, scarcity, upgrades, or buyer demand.",
    ],
    "Offer and negotiation": [
        "A stronger offer is not only higher price; it is also certainty, timing, and cleaner terms.",
        "Waiving a contingency may make the offer more competitive, but it also changes your risk.",
        "Let's separate what we want, what we can support, and what we are willing to risk.",
        "I recommend we put the request in specific, document-supported terms.",
    ],
    "Transaction coordination": [
        "Here is the current status, the open item, the owner, and the deadline.",
        "I do not want to overpromise; I will confirm in writing once the lender updates us.",
        "This issue may affect closing timing, so I am escalating it now.",
        "Let's keep communication factual and avoid assigning blame before we know the cause.",
    ],
    "Risk and ethics": [
        "I cannot accept anything of value in exchange for referrals.",
        "If we know a material issue, hiding it creates more risk than documenting it.",
        "Let's pause and route this through the broker or compliance before responding.",
        "The client should understand the consequence before signing or waiving that term.",
    ],
}


WORKBOOK_TASKS = [
    "A buyer wants a showing today but does not want to sign a representation agreement. Write a clear explanation of role, services, compensation, and options.",
    "A buyer asks whether an area is safe and good for families. Write a fair-housing-safe response that redirects to objective criteria and resources.",
    "A seller wants to list above the CMA range. Prepare a pricing explanation using comps, market exposure, and an adjustment plan.",
    "A listing description says 'perfect for young families near a church community.' Rewrite it to focus on property features and compliance-safe language.",
    "A buyer wants to waive inspection and appraisal protections to win. Write a risk explanation that does not tell the buyer what to do.",
    "An inspection finds serious issues. Write a repair request or credit request supported by the report and an estimate.",
    "The lender is not ready for closing. Write a transaction update that names status, open conditions, owner, deadline, and possible impact.",
    "A vendor offers event sponsorship in exchange for referrals. Draft a refusal and escalation note to your broker or compliance contact.",
]


SOURCES = [
    "HUD and DOJ fair housing guidance for protected classes, steering, discriminatory advertising, and housing-related discrimination language.",
    "HUD Fair Housing Advertising guidance for property advertising and preference, limitation, or discrimination risk.",
    "CFPB RESPA guidance for settlement-service referral, kickback, and unearned-fee risk language.",
    "CFPB TRID, Loan Estimate, and Closing Disclosure materials for mortgage disclosure and closing-cost language.",
    "EPA lead-based paint real estate disclosure guidance for pre-1978 residential sale and lease disclosure language.",
    "NAR resources on agency, written buyer agreements, compensation disclosure, and the Code of Ethics for industry terminology and professional-practice language.",
    "State law, local MLS rules, brokerage policy, forms, legal counsel, lender instructions, title or escrow instructions, and property-management rules used by the learner's own organization.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in real estate environments: residential agents, brokers, transaction coordinators, assistants, leasing staff, property managers, commercial real estate staff, relocation teams, mortgage-adjacent staff, title-adjacent staff, and real-estate business partners."
        )
    )
    story.append(
        p(
            "The course is not a real estate licensing course and does not replace state law, legal counsel, brokerage supervision, MLS rules, lender guidance, title or escrow instructions, or property-management policy. It trains professional English for real estate work: clarifying relationships, explaining documents, avoiding discriminatory language, negotiating terms, documenting risk, and keeping transactions moving under pressure."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "Real estate teams compress risk into short phrases: agency disclosure, representation agreement, procuring cause, CMA, comp, appraisal gap, escalation clause, inspection contingency, seller concession, material fact, steering, reasonable accommodation, Loan Estimate, Closing Disclosure, clear to close, title defect, escrow, proration, NNN, NOI, and cap rate. Learners need the vocabulary and the habits around it: define roles, document facts, separate advice from referral, explain tradeoffs, and protect fair housing."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_real_estate_communication_principles(story: list) -> None:
    story += h1("Real Estate Communication Principles")
    story.append(h2("Clarify role before giving advice"))
    story.append(
        p(
            "Many real estate misunderstandings begin when clients think the professional represents them, but the professional has not explained the relationship. Strong real estate English starts with role clarity: who is represented, what duties apply, what documents are needed, how compensation is handled, and what questions require a different expert."
        )
    )
    story.append(h2("Use objective criteria under sensitive pressure"))
    story.append(
        bullets(
            [
                "Use 'objective criteria' when redirecting neighborhood, school, safety, or demographic questions.",
                "Use 'market evidence' when a client wants a price unsupported by comps.",
                "Use 'contract options' when a problem occurs after signing, not 'we can definitely cancel' or 'they must fix it.'",
                "Use 'according to the lender/title/escrow update' when reporting outside-party status.",
                "Use 'broker or legal review' when a request could create disclosure, agency, or referral risk.",
            ]
        )
    )
    story.append(h2("Turn risky client requests into professional questions"))
    story.append(
        table(
            [
                ["Risky request", "Stronger real estate response"],
                ["Is this a good neighborhood for us?", "Which objective factors matter most to you, and which public resources would help you evaluate them?"],
                ["Let's list high and see what happens.", "Which comps, condition factors, and showing-feedback triggers support that pricing plan?"],
                ["Can we hide the repair?", "What does the disclosure form require, what records exist, and should we ask counsel before responding?"],
                ["Can you recommend your favorite lender?", "I can share options and objective criteria, but I cannot accept referral benefits or guarantee lender performance."],
            ],
            [2.15 * 72, 4.85 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a realistic sentence, ask which state, brokerage, MLS, contract, or lender definition applies, and explain the transaction consequence. Real estate language varies by jurisdiction and role, so learners must not assume one local definition is universal."
        )
    )
    for title, items in JARGON_GROUPS:
        story.append(h2(title))
        rows = [["Term", "Working meaning"]]
        rows.extend([[term, definition] for term, definition in items])
        story.append(table(rows, [1.6 * 72, 5.4 * 72]))


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
        story.append(bullets([bounded_activity_instruction(activity) for activity in module["activities"]], numbered=True))
        story.append(h3("Learner outputs"))
        story.append(bullets(module["outputs"]))
        story.append(
            box(
                "Facilitator note",
                [
                    "When learners give a quick answer, ask: who is represented, what document controls, what objective source supports this, what risk exists, who must decide, and when should the learner refer to broker, legal, lender, title, escrow, inspection, or tax expertise?"
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
                "Learner explains their real estate role in 90 seconds, including clients, transaction type, documents, stakeholders, and highest-risk conversations.",
                "Learner defines twelve real estate terms and uses six in realistic workplace sentences.",
                "Learner handles a short role-play: a buyer asks for neighborhood advice and then asks to see a property before discussing representation.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but uses them loosely.", "Uses real estate terms accurately in context.", "Defines terms, asks which jurisdiction or document applies, and adjusts by audience."],
                ["Role clarity", "Gives advice before clarifying relationship.", "Explains representation, compensation, and role boundaries.", "Protects trust by documenting role, consent, and referral limits before conflict appears."],
                ["Fair housing language", "Answers sensitive questions subjectively.", "Redirects to objective criteria and public resources.", "Handles pressure calmly while preserving client dignity and compliance."],
                ["Transaction judgment", "Reports updates without owner or deadline.", "Explains status, dependency, risk, and next step.", "Keeps multiple parties aligned without blame or overpromising."],
                ["Risk control", "Misses disclosure, referral, or document issues.", "Flags concerns and escalates to broker or expert.", "Protects clients and brokerage with precise, documented, policy-aware language."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a transaction strategy meeting. A buyer wants to tour without a signed agreement, asks about neighborhood demographics, wants to waive contingencies, then faces a low appraisal and lender delay. The seller side disputes inspection credits and a disclosure issue appears. The learner must clarify representation, protect fair housing, explain offer risk, coordinate lender and title updates, document options, and write a concise client update."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "Real Estate English",
        "Instructor guide for high-level ESL learners working in residential sales, leasing, property management, commercial real estate, transaction coordination, and real-estate-adjacent roles",
        "Audience: instructors, real estate English coaches, brokerage trainers, corporate learning teams, property management trainers, and advanced professional English programs",
    )
    add_course_opening(story)
    add_real_estate_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-real-estate-english-instructor-guide.pdf",
        "EFSP Real Estate English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Real Estate English",
        "Participant workbook: agency, fair housing, pricing, offers, disclosures, inspections, financing, closing, leasing, and transaction dialogue practice",
        "Audience: advanced ESL learners working in real estate, leasing, property management, commercial real estate, transaction coordination, and related roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you sound precise, calm, and trustworthy in real estate conversations. The goal is not to memorize more terms. The goal is to explain role, evidence, risk, options, and next steps in a way clients and colleagues can act on."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which real estate conversations are hardest for you: buyer intake, listing price, fair housing questions, offer strategy, inspections, financing updates, leasing, or conflict?",
                "Which terms do you understand when reading but avoid when speaking?",
                "When a client asks a risky question, do you become too agreeable, too blunt, too vague, or too legalistic?",
                "What is one recent transaction conversation you wish you had handled more clearly?",
            ]
        )
    )
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("Real Estate Workstream Language")
    story.append(
        table(
            [
                ["Area", "Useful verbs", "Example sentence"],
                ["Agency", "represent, disclose, consent, document, refer", "Before we tour, we need to clarify representation and compensation."],
                ["Search", "prioritize, filter, compare, verify, narrow", "Let's turn your preferences into objective search criteria."],
                ["Pricing", "compare, adjust, justify, test, reposition", "The price needs support from relevant comps and current competition."],
                ["Offers", "structure, counter, waive, protect, negotiate", "This term may strengthen the offer, but it increases your risk."],
                ["Transaction", "coordinate, confirm, escalate, update, close", "The open item is lender documentation, and the next update is due tomorrow."],
                ["Risk", "disclose, document, pause, review, comply", "We should route that question to broker or legal review before responding."],
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
        "efsp-real-estate-english-participant-workbook.pdf",
        "EFSP Real Estate English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "Real Estate Dialogue Lab",
        "Realistic real-estate-workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners",
        "Audience: instructors, real estate English coaches, brokerage trainers, property management teams, transaction teams, and peer practice cohorts",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: real estate professional, client or stakeholder, observer.",
                "Read the model dialogue once. Then replay it with a different property type, market condition, jurisdictional rule, contract term, or stakeholder pressure.",
                "The observer listens for role clarity, fair-housing-safe language, document awareness, objective evidence, risk explanation, and next-step control.",
                "After each role-play, replay the hardest 30 seconds with a more precise real estate sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners give confident legal or lending advice. Ask them to separate real estate process language from legal, tax, lending, inspection, title, escrow, and brokerage-policy decisions."
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
                    "Did the learner clarify role, document, source, or decision owner?",
                    "Did the learner avoid discriminatory, misleading, or overpromising language?",
                    "Did the learner explain the tradeoff or risk in plain English?",
                    "Did the learner give a concrete next step and document what should happen next?",
                ]
            )
        )
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-real-estate-dialogue-lab.pdf",
        "EFSP Real Estate Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "Real Estate Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise real estate vocabulary and transaction language",
        "Audience: advanced ESL learners in residential sales, leasing, property management, commercial real estate, transaction coordination, and related roles",
    )
    story += h1("How to Use Real Estate Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it clarifies the role, document, risk, deadline, or decision.",
                "Pair jargon with plain English for clients: define the term and explain what it changes in the transaction.",
                "Ask which state law, contract form, brokerage policy, MLS rule, lender instruction, or title or escrow practice applies.",
                "Avoid neighborhood opinions, legal conclusions, lending promises, undisclosed referral benefits, and unsupported property claims.",
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
                ["Client vs customer", "Client is represented; customer may receive information but not full representation, depending on local rules."],
                ["List price vs value", "List price is strategy; value is supported by market evidence and may differ from appraisal or sale price."],
                ["Active vs closed comp", "Active listings show competition; closed sales show accepted market behavior."],
                ["Pre-qualification vs pre-approval", "Pre-approval usually reflects deeper lender review, but still depends on underwriting and property approval."],
                ["Inspection issue vs repair obligation", "An issue found by inspection does not automatically mean the seller must repair it; the contract controls options."],
                ["Appraisal gap vs cash shortage", "An appraisal gap is valuation difference; cash shortage is buyer ability to cover funds needed to close."],
                ["Referral option vs kickback", "Providing options can be appropriate; receiving value for referrals can create RESPA or policy risk."],
                ["LOI vs lease", "A letter of intent frames commercial terms; the lease creates detailed obligations after review and execution."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-real-estate-jargon-quick-reference.pdf",
        "EFSP Real Estate Jargon Field Guide",
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
