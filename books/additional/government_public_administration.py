"""Original public-administration cases with explicit fictional local rules."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The amendment passed; the proposal did not",
        skill="Report the exact motion, voting basis, and outcome without confusing an amendment with the main decision.",
        setup="Fictional committee rules: seven members; quorum four; five present throughout. Adoption requires more than half of votes cast, excluding abstentions. An amendment changes a proposed pilot from six months to three. Its vote is 3 yes, 1 no, 1 abstention. The subsequent main motion as amended receives 2 yes, 2 no, 1 abstention. These stipulated rules are not universal public-body law.",
        cast="Nora|Committee clerk\nFelix|Committee chair",
        dialogue="""Nora|Before you sign the minutes, we need to separate the two votes. The draft says the three-month pilot was approved, but that is not what the record shows.
Felix|We had a [[quorum::Quorum is the minimum presence required to conduct the business; five members were present, exceeding the fictional committee's requirement of four.]] throughout: five present against a requirement of four. The problem is the recorded outcome, not attendance.
Nora|Agreed. First, the committee voted on changing six months to three. Three voted yes, one no, and one abstained.
Felix|That [[amendment::The amendment changed the proposed pilot's duration from six months to three; adopting that change did not adopt the pilot itself.]] passed. But I then put the revised main motion to the committee, and the votes were different.
Nora|Two yes, two no, and one abstention. I have the roll-call record alongside the exact revised wording, so we can verify both separately.
Felix|Under our stated rule, the [[majority::A majority here means more than half of votes actually cast; the fictional rule excludes abstentions, so three affirmative votes are needed when four votes are cast.]] is based on votes cast, not all seven members or all five present. Four votes were cast on each question.
Nora|So the amendment's three to one is enough. The main motion's two to two is not more than half. The pilot was not approved.
Felix|Correct. Record the [[abstention::An abstention records that a present member did not vote; under these supplied rules it is excluded from votes cast rather than counted as a no.]] accurately, but do not turn it into a third no. We still need the record to distinguish a tie from a two-to-three defeat.
Nora|The member who moved the pilot has asked whether the approved change leaves us with a three-month pilot automatically.
Felix|No. The change became part of the [[main motion as amended::The main motion as amended is the substantive proposal with the adopted change incorporated; it still needed its own successful vote, which it did not receive.]]. Its later defeat means the committee did not authorize that revised proposal.
Nora|I will correct the summary to show amendment adopted, then main motion as amended lost. I will not collapse the votes into one result.
Felix|Please retain the exact wording too. A reader should be able to tell that three months replaced six months, not that a separate three-month extension was authorized.
Nora|The draft currently labels the result unanimous. That is wrong even for the amendment, because one member voted against it.
Felix|Remove that. The [[roll-call vote::A roll-call vote identifies individual members' recorded responses; it supports verification of the totals and preserves the distinction among yes, no, and abstention.]] gives us the actual responses. There is no need for a broader label that contradicts them.
Nora|For the public summary, I can say the committee amended the proposal but did not approve the pilot. That is shorter without changing the result.
Felix|That works. Keep the detailed voting record in the minutes according to our process. Plain language should clarify the outcome, not erase the separate decisions.
Nora|I will also remove the instruction to schedule the pilot. It appears to have been generated from the incorrect approval summary.
Felix|Good catch. Notify the program team of the corrected result before it relies on that instruction. The defeated motion does not authorize implementation.
Nora|I will circulate the corrected draft through the minutes-approval process and retain the revision history, rather than silently replacing an approved record.
Felix|Thank you. The final check is straightforward: five present, four voting each time, amendment three to one, main motion two to two, and no pilot approval.""",
        transfer_title="Use the stated voting basis",
        transfer_setup="A separate fictional board has six members present and a quorum requirement of five. A motion receives 3 yes, 2 no, and 1 abstention. Its rule requires more than half of votes cast, excluding abstentions.",
        transfer="""Clerk: The quorum requirement is ___ members.|five|The supplied requirement is five, which is met by the six members present.
Chair: The number of votes actually cast is ___.|5|Three yes plus two no makes five votes; the abstention is excluded under this stated rule.
Clerk: The number of affirmative votes is ___.|3|The motion received three yes votes, which is more than half of the five votes cast.
Chair: Under this rule, the motion is ___.|adopted|Three of five votes is a majority, so the stated adoption requirement is satisfied.""",
        reference=("Official Robert's Rules: majority, abstentions, and amendments; check governing law first", "https://robertsrules.com/frequently-asked-questions/"),
    ),
    scenario(
        title="Unspent does not mean uncommitted",
        skill="Reconcile available budget, outstanding commitments, and a final invoice without counting reserved funds twice.",
        setup="Fictional budget report: appropriation $120,000; expenditure $62,000; separate outstanding encumbrances $38,000. An included order with $15,000 reserved is fully completed for a final accepted $12,000 invoice. The unused $3,000 is formally released and the order closed. No other changes apply. These figures use the stipulated reporting basis, not a universal accounting treatment.",
        cast="Ravi|Department manager\nElena|Budget analyst",
        dialogue="""Ravi|The report shows sixty-two thousand spent from a hundred twenty thousand. I was about to tell the team we have fifty-eight thousand left for new orders.
Elena|That ignores the [[encumbrances::Encumbrances reserve budget for outstanding commitments under this report's basis; the 38,000 is not included in the 62,000 expenditure and is not freely available for new orders.]]. Thirty-eight thousand is reserved for orders, leaving twenty thousand available before the final invoice.
Ravi|Let me put the authorized budget, expenditure, and outstanding commitments side by side. We need all three for this check.
Elena|Yes. From the [[appropriation::The appropriation is the stipulated 120,000 spending authority in this example; it is distinct from both money already spent and the department's bank balance.]] of a hundred twenty thousand, subtract sixty-two thousand spent and thirty-eight thousand reserved, once each.
Ravi|One order has finished. We reserved fifteen thousand; the accepted final invoice is twelve. Does that free the entire fifteen?
Elena|No. The [[final invoice::The final invoice is the accepted 12,000 charge for the completed order; recording it uses twelve thousand of the amount previously reserved.]] uses twelve thousand of that reservation. Only the remaining three thousand becomes available when the unused amount is formally released.
Ravi|The whole order is complete, with no remaining delivery or charge. We have that confirmation in the record.
Elena|That confirmation matters. Under the stated [[budgetary basis::The budgetary basis defines how this report treats expenditure and outstanding reservations; using the same stipulated basis prevents double counting or mixing it with cash or financial-statement measures.]], expenditure rises to seventy-four thousand and outstanding encumbrances fall to twenty-three thousand.
Ravi|That is sixty-two plus twelve, and thirty-eight less fifteen. Then a hundred twenty less seventy-four less twenty-three gives twenty-three thousand available.
Elena|Exactly. The [[unencumbered balance::The unencumbered balance is the amount available after recorded expenditure and remaining reservations on this report's basis: 120,000 minus 74,000 minus 23,000 equals 23,000.]] increases by three thousand, not fifteen. The invoice replaced part of an existing reservation rather than creating a completely separate commitment.
Ravi|Someone has already entered the twelve-thousand invoice in a local worksheet while leaving all thirty-eight thousand encumbered. That would understate what remains.
Elena|It would count the same twelve thousand as both expenditure and an outstanding reservation. Reconcile the worksheet to the controlled report and the completed order record.
Ravi|I will also avoid calling the released three thousand a cash refund. No supplier has paid anything back in these facts.
Elena|Right. A [[release of encumbrance::A release of encumbrance removes budget reserved for an obligation no longer outstanding; it does not itself describe a cash receipt or supplier refund.]] changes budget availability. A cash receipt would need its own transaction and evidence.
Ravi|Could we transfer the twenty-three thousand to a different program because the report now shows it available?
Elena|Not from this calculation alone. Available within this budget does not establish transfer authority. Any transfer or new commitment still follows the applicable budget and purchasing controls.
Ravi|Then I will show the revised balance and separately identify the proposed use. The arithmetic should not make the approval decision for us.
Elena|That is the right separation. Keep the appropriation, expenditure, remaining commitments, and calculation date visible so another reviewer can reproduce the result.
Ravi|My revised update is seventy-four thousand spent, twenty-three thousand still reserved, twenty-three thousand available, with the completed order formally closed.
Elena|Those figures reconcile to a hundred twenty thousand. Attach the final-invoice and release references so the next report does not restore the old reservation by mistake.""",
        transfer_title="Close a fully completed order",
        transfer_setup="Fictional report: $90,000 appropriation, $40,000 expenditure, and $35,000 separate outstanding encumbrances. An included $10,000 order is completed for a final $8,000. Its unused $2,000 is released and the order closed; no other changes occur.",
        transfer="""Manager: Before the final invoice, available budget is $___ thousand.|15|Ninety minus forty minus thirty-five equals fifteen thousand available before the order closes.
Analyst: Revised expenditure is $___ thousand.|48|The final eight-thousand invoice increases recorded expenditure from forty to forty-eight thousand.
Manager: Remaining encumbrances are $___ thousand.|25|The entire ten-thousand reservation for the completed order leaves the outstanding thirty-five-thousand balance.
Analyst: Revised available budget is $___ thousand.|17|Ninety minus forty-eight minus twenty-five equals seventeen thousand, a two-thousand increase from the released unused reservation.""",
        reference=("Government Finance Officers Association: budget monitoring and outstanding commitments", "https://www.gfoa.org/materials/budget-monitoring"),
    ),
    scenario(
        title="A notice residents can act on",
        skill="Replace administrative jargon with clear instructions while preserving the exact document choices, deadline, and submission route.",
        setup="Fictional allotment-renewal notice R18: the signed renewal form must arrive with ONE of three listed address documents: a current utility bill, tenancy agreement, or council letter. Both items must be received by 24 October at 17:00 local time, through the renewal portal or Service Desk. A postmark is insufficient. A reference number confirms receipt only. The proposed shorter notice wrongly says send all documents by 24 October.",
        cast="Mae|Public-service editor\nOmar|Renewals officer",
        dialogue="""Mae|The shorter version is easier to read, but it changes what residents have to do. Send all documents is not equivalent to one document from this list.
Omar|The [[supporting evidence::Supporting evidence is one of the three accepted address documents in this fictional process; the notice must not turn an alternative list into a requirement to supply all three.]] is a single accepted address document. We also need the signed renewal form, so there are two required items in the submission.
Mae|Then let us separate the instruction from the choices. Submit your signed renewal form and one of the following address documents. The list can sit immediately below.
Omar|Keep [[one of::One of expresses an alternative choice among the listed documents; it prevents the three acceptable options from becoming three cumulative requirements.]] prominent. A utility bill, tenancy agreement, or council letter is acceptable under the stated process. We should not add documents that the policy does not list.
Mae|The deadline sentence also lost the time. Someone reading by twenty-four October might reasonably assume they have until midnight.
Omar|Write [[received by::Received by makes arrival the deadline condition; merely sending or postmarking the submission before the cutoff does not satisfy this fictional process.]] twenty-four October at 17:00 local time. Both the form and the selected document must arrive by that cutoff.
Mae|I will put that near the action, not in a footer. Do we still accept both the renewal portal and the Service Desk?
Omar|Yes. Those are the two stated [[submission routes::Submission routes identify the authorized ways to provide the material: the renewal portal or Service Desk; simplifying the notice must not remove an available route.]]. Do not replace them with online only just because the portal link is convenient to print.
Mae|I also want the sentence to name who receives the material. Your renewal form must be submitted hides the action and makes the next step less immediate.
Omar|Use [[active voice::Active voice makes the actor and action explicit, as in Submit your signed renewal form; it improves clarity without altering what the process requires.]]. We can speak directly to the resident while keeping the required documents and deadline exact.
Mae|Below the portal link, the draft says a reference number means renewal approved. That is not supported by the intake process.
Omar|Change it to [[receipt confirmation::Receipt confirmation shows that a submission arrived and provides its reference; it does not establish completeness, eligibility, or approval of the renewal.]]. The team still checks the application. The reference is useful for an inquiry, but it is not an approval notice.
Mae|Could we test the new version with the service team by asking them to identify the two required items, deadline, and available routes?
Omar|Yes. Give them the notice rather than explaining it first. If they select all three address documents, the wording or layout still needs work.
Mae|I will also ask them whether a twenty-fourth-of-October postmark is enough. The correct answer under these instructions is no; arrival is what matters.
Omar|And ask what the reference number establishes. Those checks cover the errors residents would actually encounter, rather than whether colleagues merely like the shorter text.
Mae|The revised version will use a short document list, a separate deadline line, and labeled submission routes. The contact details will remain with the notice.
Omar|Keep R18 visible too. Staff need to identify the version a resident received if an older copy is still circulating.
Mae|I will send the revised wording for process-owner approval before publication. Clearer wording is still a change that must match the current requirements.
Omar|Agreed. The final check is signed form plus one accepted address document, received by the exact cutoff, through either stated route, with receipt distinguished from approval.""",
        transfer_title="Check a second notice",
        transfer_setup="Fictional notice S20 requires a signed application plus ONE of a current lease or accepted council letter. Both must be received by 6 November at 16:00 local time. The reference confirms receipt, not approval.",
        transfer="""Editor: The applicant chooses ___ of the two address documents.|one|The notice gives two alternative address documents, not a requirement to submit both.
Officer: The chosen document accompanies the signed ___.|application|The application is required in addition to one accepted address document.
Editor: Both items must arrive by ___ local time on 6 November.|16:00|The exact supplied cutoff is 16:00, not midnight or merely a posting date.
Officer: The reference number confirms ___.|receipt|The scenario explicitly limits the reference to receipt and does not make it an approval.""",
        reference=("Digital.gov: writing for understanding", "https://digital.gov/guides/plain-language/writing"),
    ),
]
