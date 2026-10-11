"""Original property conversations extending the eight core lessons."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='Two office rents use different area figures',
        skill='Compare commercial lease quotations without mixing area or cost bases.',
        setup='A small business is comparing two office proposals. Office A quotes 1,000 usable square feet, 1,200 rentable square feet, and $30 per rentable square foot per year in base rent. Office B quotes $2,900 monthly base rent but has not supplied comparable area or additional charges. Neither proposal has been accepted.',
        cast='Zara|Business tenant\nPaul|Commercial leasing broker',
        dialogue='''Zara|Office A is thirty dollars a foot. Office B is twenty-nine hundred a month. A looks cheaper, doesn't it?
Paul|We need the same basis first. A charges on [[rentable area::Rentable area is the quoted charging basis, which here is 1,200 square feet rather than the 1,000 usable figure.]], and that rate is annual, not monthly.
Zara|I multiplied thirty by the one thousand square feet shown on the floor plan.
Paul|That is the stated [[usable area::Usable area describes the space available for the occupant's use under the stated measurement basis, distinct from the quoted rentable area.]]. The proposal uses twelve hundred for the rent calculation.
Zara|So thirty times twelve hundred gives thirty-six thousand a year, or three thousand a month.
Paul|Correct, for [[base rent::Base rent is the stated rental charge before any additional amounts that the lease may require.]]. We still need the other charges before comparing the total monthly cost.
Zara|Then B is one hundred less per month on base rent. Why does A have two hundred extra square feet in the calculation?
Paul|The quoted difference reflects an allocation beyond the usable space. We should obtain the measurement basis and explanation, not assume every building calculates it identically.
Zara|Can you confirm whether both proposals include the same services? One says building services; the other lists almost nothing.
Paul|I will request the [[operating expenses::Operating expenses are building-running costs whose allocation and recovery depend on the proposed lease terms.]] and who pays each item, including how any annual reconciliation works.
Zara|I also need two meeting rooms. A's plan has only one, so there may be work before we can move in.
Paul|Ask about the permitted work, approvals, schedule, and any [[tenant improvement allowance::A tenant improvement allowance is a proposed landlord contribution toward eligible fit-out work, subject to its terms.]]. An allowance is not automatically a promise to cover every alteration.
Zara|Could I subtract the entire allowance from first-year rent when comparing the proposals?
Paul|Show it separately. Its payment conditions and eligible uses may differ from a rent reduction, and you may incur costs before reimbursement.
Zara|B also offers a month before rent starts. I would like the comparison to show that benefit.
Paul|Yes, with the actual [[rent commencement::Rent commencement is the date rent begins under the agreement, which may differ from access or lease commencement.]] date and any continuing charges during the concession period.
Zara|It sounds as though we need a schedule, not just one attractive number.
Paul|Exactly: area basis, base rent, additional costs, fit-out contributions, dates, and unresolved terms. I will not mark missing costs as zero.
Zara|Please send that comparison before we authorize an offer. We have not chosen either office yet.
Paul|I will obtain the missing details and arrange the appropriate lease review. Today's arithmetic does not approve the commercial or legal terms.''',
        transfer_title='An annual quotation is read as monthly',
        transfer_setup='An office quotes $24 per rentable square foot annually on 900 rentable square feet. Additional charges are not supplied.',
        transfer='''Tenant: Twenty-four times nine hundred gives $21,600 per ___.|year|The rate is annual, so multiplying by the area produces annual base rent.
Broker: Dividing by twelve gives $1,800 in monthly base ___.|rent|The calculation converts the annual base rental amount into its monthly equivalent.
Tenant: That still excludes any additional ___.|charges|The quotation does not supply the other amounts that may be payable.
Broker: Correct. We cannot describe $1,800 as the total occupancy ___.|cost|Total occupancy cost cannot be established while additional charges remain unknown.'''),
    scenario(
        title='Low monthly dues and an unfinished roof review',
        skill='Explain condominium documents and identify unresolved ownership costs.',
        setup='A condominium listing shows $300 monthly association dues. Meeting minutes mention a roof project under discussion. No final contract, funding decision, or assessment notice has been supplied. A buyer asks whether the low dues prove the building is inexpensive to own.',
        cast='Mei|Buyer\nLuis|Buyer representative',
        dialogue='''Mei|The monthly dues are much lower than the other building's. Is that a reliable reason to choose this one?
Luis|It is one part of the comparison. We should review the [[association budget::The association budget shows planned income and spending; the dues figure alone does not show what is funded.]] and what those dues cover.
Mei|I saw a roof project mentioned in the meeting minutes. Has the association decided how to pay for it?
Luis|Not in the documents we have. The minutes describe a discussion, not a signed project contract or confirmed funding plan.
Mei|Does the association keep money for major repairs, separate from its ordinary bills?
Luis|That is the purpose of [[reserves::Reserves are funds set aside for future needs such as major repairs, distinct from simply quoting the monthly dues.]], where maintained. We need the current financial documents rather than infer the amount.
Mei|The agent sent a reserve study from several years ago. Could that answer the question?
Luis|It gives us a starting point. Check its date, assumptions, updates, and the association's actual funding; a study is not a bank statement.
Mei|If there is not enough set aside, would I automatically receive an extra bill as soon as I buy?
Luis|We cannot say that. A [[special assessment::A special assessment is an additional association charge for a specified need; none has been confirmed in this case.]] is one possible funding mechanism, but no decision is supplied here.
Mei|I want the uncertainty visible in the comparison. I do not want us to treat a missing notice as proof there will never be a charge.
Luis|Agreed. I will request the current minutes, project status, financial records, and any existing assessment notices through the proper channel.
Mei|What about the money owners already owe the association? Would unpaid dues affect the building's finances?
Luis|The [[delinquency::Delinquency refers to overdue payments; the association's report can show whether that is a material issue.]] information may be relevant. We need the actual report, not assumptions about particular residents.
Mei|And the insurance summary is only one page. I cannot tell what the master policy leaves for me to cover.
Luis|Ask the qualified insurance professional about the [[master policy::The master policy is the association's insurance arrangement; its coverage must not be assumed to replace every owner's insurance need.]] and the separate coverage you may need.
Mei|Can we get these documents before my review period expires?
Luis|I will track the request and the applicable [[document-review deadline::The document-review deadline is the relevant contractual or legal time limit; requesting documents does not automatically extend it.]]. We must address timing through the actual contract and local requirements.
Mei|Please show three hundred as confirmed dues, with roof funding and other costs still unresolved.
Luis|That is how I will present it. We will separate the known recurring charge from costs and decisions still requiring review.''',
        transfer_title='A draft project estimate becomes a supposed bill',
        transfer_setup='A building committee has obtained a preliminary elevator estimate. It has not selected a contractor or approved an owner assessment.',
        transfer='''Buyer: The elevator estimate is not yet an approved ___.|assessment|An estimate for work does not establish an additional charge approved for owners.
Representative: Correct. We need the association's actual funding ___.|decision|The missing funding decision determines how the proposed project would be financed.
Buyer: Keep the preliminary figure separate from confirmed recurring ___.|dues|Dues are the recurring association charge, not the preliminary project estimate.
Representative: I will also check the date of the next document ___.|update|An update is needed because the preliminary project and funding information may change.'''),
    scenario(
        title='The final walkthrough reveals a missing appliance',
        skill='Report a condition discrepancy and coordinate a response without promising a remedy.',
        setup='At a final walkthrough, a buyer finds that a refrigerator listed as included in the signed purchase agreement is missing. Moving boxes remain in the garage. Closing is scheduled for tomorrow. No amendment, credit, possession change, or delay has been agreed.',
        cast='Iris|Buyer\nDaniel|Buyer representative',
        dialogue='''Iris|The refrigerator is gone. I remember it being included when we agreed the price.
Daniel|Let us check the signed agreement. Yes, it is listed as included. I will record the [[discrepancy::Discrepancy identifies the difference between the agreement and the property's observed condition.]] with the time and photographs from today's visit.
Iris|Could it simply be in the garage with those boxes? I do not want to accuse the seller before we know.
Daniel|We can ask through the seller's representative. We have confirmed that it is absent from the kitchen, not what happened to it.
Iris|What exactly is the purpose of this walkthrough? Is it another full inspection?
Daniel|This [[final walkthrough::The final walkthrough checks the property's condition and relevant agreed items near closing; it is not automatically a new full technical inspection.]] is for the agreed condition and items near closing. A technical concern may still require a qualified professional.
Iris|The garage also has moving boxes. I am supposed to get the property cleared, according to the agreement.
Daniel|I will record those too and confirm the required [[possession condition::Possession condition refers to the state in which the agreement requires the property to be handed over.]] and timing from the actual terms.
Iris|Can we just deduct the price of a new refrigerator from tomorrow's payment?
Daniel|Not unilaterally. We need a documented resolution through the relevant professionals, including any effect on the closing figures and lender requirements.
Iris|My movers are booked. I need to know quickly whether tomorrow is still realistic.
Daniel|I will contact the seller's representative and closing team now. I can commit to an update this afternoon, not guarantee the result.
Iris|If the seller offers a payment instead of returning it, what would we need?
Daniel|Any proposed [[closing credit::A closing credit is an agreed adjustment in the settlement figures, subject to required documentation and applicable constraints.]] needs proper review, agreement, and treatment in the closing documents.
Iris|And if they say it will be returned after we sign?
Daniel|Do not rely on an informal assurance. We should obtain professional advice on the proposed [[written amendment::A written amendment records an agreed contractual change; a verbal promise does not by itself supply those documented terms.]] and how completion would be verified.
Iris|I would prefer the included refrigerator back, but I have not authorized a new arrangement yet.
Daniel|I will convey that preference without representing it as acceptance of any proposal or waiver of a right.
Iris|Please keep the appliance and the boxes as separate open items. One could be resolved while the other remains.
Daniel|I will maintain that [[punch list::A punch list records specific outstanding items for follow-up; listing an item does not establish that it has been resolved.]] and confirm the response to each before reporting the walkthrough issues closed.''',
        transfer_title='A verbal promise to remove stored furniture',
        transfer_setup='Furniture remains in a garage that the agreement requires to be cleared. The seller verbally promises removal after closing. The buyer has not accepted a changed arrangement.',
        transfer='''Buyer: Record the furniture as an outstanding walkthrough ___.|item|The furniture is a specific unresolved condition found during the walkthrough.
Representative: The verbal promise does not establish an agreed ___.|amendment|The buyer has not agreed to change the existing contractual arrangement.
Buyer: Ask the closing professionals what documentation the proposed change would ___.|require|The professionals must review the needed documentation and effects of any proposed change.
Representative: I will report the response without treating it as your ___.|acceptance|The buyer has not accepted the proposal, so coordination must not imply consent.'''),
]
