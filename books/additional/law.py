"""Fictional legal communication; local rules and supervising counsel control."""
from books.supplements import scenario

SCENARIOS = [
scenario(
    title='Negotiating the scope of a document search',
    skill='Narrow a discovery proposal without confusing a search agreement with a production decision.',
    setup='In a fictional US civil case, opposing counsel request messages from twelve employees over five years. The responding team proposes an initial search covering four employees and eighteen months, subject to counsel\'s review of the applicable rules and case orders.',
    cast='Jules|Responding counsel\nMara|Requesting counsel',
    dialogue='''
Mara|Your proposal covers four employees. Our request names twelve. Why exclude the other eight?
Jules|I'm proposing a [[phased search::Phased search divides collection or review into agreed stages instead of treating the initial stage as necessarily complete.]], not a final exclusion. Those four negotiated the agreement and managed the disputed deliveries.
Mara|One of the others approved the pricing changes. Their messages may matter too.
Jules|Which person and which changes? If we can identify that connection, I can take a specific addition back to the team.
Mara|Drew approved the revised pricing in March. The email chain we produced names Drew.
Jules|Please give me the document reference. I'll review adding Drew as a [[custodian::Custodian means a person whose potentially relevant records are identified for preservation or collection.]] for the first phase.
Mara|The eighteen-month period is also narrower than our request.
Jules|It covers negotiation through the last disputed delivery. What issue requires the earlier years?
Mara|We allege that the same pricing representation appeared before this contract.
Jules|Then we should identify the representation and the relevant earlier period. We may need a different [[date range::Date range defines the time span of records included in a particular search.]] for that issue.
Mara|Could you run our keywords across everything and tell us the hit count?
Jules|We'll assess that proposal. A hit count alone won't tell either of us how much responsive material it retrieves.
Mara|Would a sample help test the terms?
Jules|Yes, if we agree how to select and review it. We can use the sample to refine the [[search terms::Search terms are words or expressions used to locate potentially relevant material, not final responsiveness decisions.]].
Mara|I don't want refinement to become a way to omit unfavorable documents.
Jules|Understood. Let's record the scope, the sampling approach, and unresolved issues. Neither side has agreed that the first phase satisfies the entire request.
Mara|And collection doesn't mean the material is cleared for production.
Jules|Correct. [[Responsiveness::Responsiveness concerns whether material falls within a document request; privilege is a separate review question.]] and privilege review still follow the applicable protocol.
Mara|I'll send Drew's reference and the earlier representation today. Please circulate a revised proposal afterward.
Jules|I will. If we can't agree on the remaining scope, we'll identify that [[dispute::Dispute means the specific unresolved disagreement, not an agreement to withhold records unilaterally.]] and follow the required process for this case.
''',
    transfer_title='A search hit is mistaken for a production instruction',
    transfer_setup='A review coordinator receives the search results. Counsel has not completed responsiveness or privilege review and has not authorized production.',
    transfer='''
Coordinator: Should every search ___ go straight into the production set?|hit|Hit means material matched a search expression, not that it is cleared for release.
Counsel: No. Keep the results in the ___ set under our protocol.|review|Review set contains material awaiting the required legal and procedural assessment.
Coordinator: I'll record the search terms and date range in the ___ record.|collection|Collection record preserves how the material was gathered and what scope was used.
Counsel: Good. No production until the required review and ___ are complete.|authorization|Authorization is the explicit approval to release the reviewed material through the proper process.
'''),
scenario(
    title='Preparing a witness to distinguish memory from a document',
    skill='Ask for clarification and state the basis of an answer without guessing.',
    setup='Counsel prepares an employee witness for a fictional civil deposition. A shipping email is dated 14 June, but the witness does not independently remember the shipment date. Counsel will explain the applicable deposition procedure separately; the language practice concerns truthful, precise answers.',
    cast='Asha|Counsel\nRobin|Employee witness',
    dialogue='''
Asha|Let's practice with the shipping email. When did the shipment leave?
Robin|June fourteenth, according to the email. I don't actually remember the date myself.
Asha|That distinction matters. Keep the [[basis::Basis identifies the source supporting an answer, such as personal memory or a document.]] of your answer clear.
Robin|Would it sound evasive to say I don't remember?
Asha|Not if that's true. Don't claim a memory you don't have, and don't deny a memory you do have.
Robin|What if the question assumes I approved the shipment? I only prepared the packing list.
Asha|Explain that difference. You can correct the [[premise::Premise is an assumption contained in a question, here that the witness approved the shipment.]] before answering what you actually know.
Robin|Could I say, "I prepared the list, but I wasn't the person who approved dispatch"?
Asha|Yes, if that's accurate. Now suppose you don't understand what dispatch means in the question.
Robin|I'd ask whether they mean approval to ship or the truck actually leaving.
Asha|Good. Request [[clarification::Clarification resolves an unclear meaning so the witness does not answer a different question.]] rather than silently choose one meaning.
Robin|And if they show me another email that changes what I remember?
Asha|Take time to read the relevant material. Say what it refreshes and what still isn't within your personal recollection.
Robin|I shouldn't agree with their summary just because the document looks familiar.
Asha|Exactly. Review the [[exhibit::Exhibit is the document or other material identified for use in the proceeding.]] you're shown, not the document you assume it is.
Robin|What if I realize my earlier answer was wrong?
Asha|Raise the need for a [[correction::Correction makes an inaccurate answer accurate; it is different from changing truthful evidence to help a side.]] promptly. I'll explain the procedure that applies.
Robin|I'm worried about saying something that hurts the company's case.
Asha|Your job is to answer truthfully, not to choose the most helpful version. Separate what you observed from what someone later told you.
Robin|Then I'll keep [[firsthand knowledge::Firsthand knowledge comes from the witness's own observation or experience, rather than another person's account.]] separate from the email and anything I heard afterward.
''',
    transfer_title='Clarifying an ambiguous question',
    transfer_setup='During another practice exchange, the word approved could mean preparing a document or authorizing shipment. The witness prepared the document but did not authorize shipment.',
    transfer='''
Counsel: Did you approve the shipment ___?|document|Document is the item whose preparation may be confused with shipment authorization.
Witness: Could you clarify whether you mean preparing it or ___ dispatch?|authorizing|Authorizing means giving permission for dispatch, a different act from preparing paperwork.
Counsel: I mean giving permission for the goods to ___.|leave|Leave identifies the physical dispatch decision rather than document preparation.
Witness: No. I prepared the paperwork, but that decision was outside my ___.|role|Role defines the witness's responsibilities and distinguishes them from the decision-maker's authority.
'''),
scenario(
    title='Explaining an invoice that exceeds the estimate',
    skill='Handle a billing question by separating fees, expenses, estimates, and agreed scope.',
    setup='A client questions an invoice for a contract matter: $7,200 in professional fees plus $300 in disbursements. The initial fee estimate was $6,500. The engagement terms and the effect of additional negotiation rounds must be reviewed before counsel responds on the disputed amount.',
    cast='Marin|Client representative\nLeo|Matter partner',
    dialogue='''
Marin|Your estimate was sixty-five hundred. The invoice is seventy-five hundred. What changed?
Leo|The invoice lists seventy-two hundred in fees and three hundred in [[disbursements::Disbursements are expenses paid or incurred in connection with the matter, separate from professional fees.]]. I'll walk through both with you.
Marin|I understood the estimate as the maximum we would pay.
Leo|Then we need to review the engagement wording together. I won't assume we understood [[fee cap::Fee cap means an agreed upper limit on fees, which is not automatically created by every estimate.]] and estimate in the same way.
Marin|The additional negotiation rounds may explain more work, but nobody explained the likely cost to me.
Leo|That's a fair question. I'll check the scope updates and who received them before I tell you what was communicated.
Marin|Please don't just send me a total number of hours. I need to see what those hours covered.
Leo|I'll provide an [[itemized::Itemized means broken down into individual entries so the work and charges can be examined.]] account, with the work described clearly and confidential details handled appropriately.
Marin|What are the three hundred dollars of expenses?
Leo|I'll verify the underlying entries and receipts. The label on the invoice isn't enough to answer which costs were incurred and whether they were agreed.
Marin|Can we pay the undisputed portion while you review the rest?
Leo|Let me confirm the appropriate arrangement with billing and the engagement terms. I'll give you a written response rather than improvise one here.
Marin|We also have another round of negotiations scheduled next week.
Leo|Before that work proceeds, let's confirm the [[scope::Scope defines the work covered by the engagement and the proposed next phase.]] and the spending instructions with the authorized client contact.
Marin|I can request approval, but our finance director has to authorize additional spending.
Leo|I'll send a revised [[budget::Budget is the planned spending amount for the defined work, subject to the agreed terms and approval.]] showing assumptions and what would trigger another discussion.
Marin|And the disputed invoice?
Leo|I'll send the breakdown and my response by Thursday. I'll also identify any agreed adjustment separately, so the record is clear.
Marin|That would help. I want predictable updates, not a surprise at the end.
Leo|Understood. Let's agree a reporting [[cadence::Cadence means the regular frequency of updates, here about work and spending.]] for the next phase and a clear contact for questions.
''',
    transfer_title='A new task arrives outside the reviewed scope',
    transfer_setup='The client asks the contract team to handle a separate employment issue. The existing engagement and fee estimate cover only the contract matter.',
    transfer='''
Client: Can you include the employment issue under the existing ___?|engagement|Engagement is the agreed professional relationship and scope, which may not cover the new issue.
Counsel: We need to review the additional ___ before confirming that.|work|Work identifies the new services requested, rather than treating them as automatically included.
Client: Please provide a separate estimate and identify the required ___.|approval|Approval refers to the authorization needed before the additional work is accepted or begun.
Counsel: I will. The current estimate covers the contract matter ___.|only|Only preserves the stated limit and prevents the original estimate from expanding silently.
'''),
]
