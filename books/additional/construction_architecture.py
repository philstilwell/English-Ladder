"""Additional built-environment coordination and commercial conversations."""

from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="A clash report is not an instruction to move a duct",
        skill="Verify model references and distinguish a coordination issue from an authorized design change.",
        setup="A coordination viewer flags duct D24 against beam B8 at Level 3. The structural model is revision S12; the loaded services file is M07, although M08 has been issued. Its alignment has not been checked. Issue C17 is open. No approved reroute exists, and this model review is not a fabrication or installation instruction.",
        cast="Nadia|BIM coordinator\nLeo|Building-services engineer",
        dialogue="""Nadia|Issue C17 shows D24 passing through B8 at Level 3. Before the team reroutes anything, can we verify which models produced that view?
Leo|Yes. The structural file is S12, but the services file in the [[federated model::The federated model combines discipline models for coordination; its result depends on the versions and alignment loaded.]] is M07. Our issued services revision is M08.
Nadia|Then the screenshot may describe an older arrangement. I will record M07 as the checked version rather than imply the current design was tested.
Leo|Please load M08 through the coordination process and check the [[shared coordinates::Shared coordinates align the discipline models; a misplaced model can create apparent intersections that do not reflect the intended geometry.]] before rerunning the check. We have not verified alignment in this review yet.
Nadia|I will also retain the old result. Replacing the file should not erase the explanation of why C17 was raised.
Leo|Agreed. Attach both model revisions and the check date to the issue. A later reviewer needs to reproduce the same comparison, not guess from the thumbnail.
Nadia|If the intersection remains after those checks, should I mark it as a confirmed site defect?
Leo|No. It would establish a model [[geometric clash::A geometric clash is an intersection of modeled elements; it does not by itself establish an installed defect or the correct remedy.]] under the checked conditions. Whether it represents an actual design conflict or installed condition still needs the relevant review.
Nadia|The meeting note says move the duct down one hundred millimetres. Was that a design instruction or someone's suggestion?
Leo|A suggestion only. We have not checked the implications for ceiling space, supports, access, or other services, and nobody has issued an approved reroute.
Nadia|I will label it proposed in C17. Can you take ownership of evaluating it with the other disciplines?
Leo|Yes. Give me the issue with its [[viewpoint::The viewpoint and element references locate the model issue so the assigned reviewer can inspect the same conflict.]], element identifiers, level, and model revisions. I will coordinate the design review, not authorize installation through a meeting comment.
Nadia|The team uses BIM Collaboration Format for issues. I can attach the saved view and the question to the existing C17 entry.
Leo|That is useful. Keep the responsible reviewer and requested response date there too; the issue record supports coordination but does not replace the design documents.
Nadia|Should the contractor fabricate to the suggested route while your review runs, to protect the lead time?
Leo|This exchange provides no [[fabrication release::Fabrication release requires the applicable authorized information; a proposed model adjustment does not provide it.]]. The contractor needs the actual authorized information under the project process, not my agreement to review an option.
Nadia|If M08 removes the intersection, I will still record what changed and ask for the required verification before closing C17.
Leo|Exactly. Do not close it solely because the red marker disappears. Check the issue against its stated concern and record the relevant review result.
Nadia|Current action: verify M08 and alignment, rerun the coordination check, and send you the reproducible issue record if it remains.
Leo|I accept that review. Keep the [[resolution status::Resolution status records the issue's verified outcome, distinct from an assigned reviewer or a proposed reroute.]] open until the applicable check supports a change, with any resulting design instruction handled separately.""",
        transfer_title="The screenshot uses an older discipline model",
        transfer_setup="Issue C29 links pipe P6 and beam B12 on Level 2. The viewer used services revision M03; M04 is current. Alignment is unverified. Engineer Rosa accepts the design review; no reroute is approved.",
        transfer="""Coordinator: The current services revision to verify is ___.|M04|M04 is the issued current version; the screenshot used older M03.
Engineer: First verify model ___ before interpreting the apparent intersection.|alignment|Unverified alignment can affect where the combined model displays its elements.
Coordinator: The assigned design reviewer is ___.|Rosa|Rosa accepted the review responsibility, not approval of a particular reroute.
Engineer: The proposed reroute is not yet ___.|approved|The supplied case explicitly leaves design authorization unresolved despite the assigned reviewer.""",
        reference=("buildingSMART: BIM Collaboration Format", "https://www.buildingsmart.org/standards/bsi-standards/bim-collaboration-format/"),
    ),
    scenario(
        title="The color sample did not approve a different product",
        skill="Separate an appearance selection from technical substitution review and purchasing authority.",
        setup="The fictional project specifies acoustic panel P200. The architect accepted sample finish B for color only. A supplier proposes P240 in the same color with a shorter quoted lead time. Its acoustic evidence, fire-performance documentation, mounting details, warranty, and substitution approval are unverified. No order for P240 has been authorized.",
        cast="Mina|Procurement coordinator\nElias|Project architect",
        dialogue="""Mina|The supplier can deliver P240 sooner than P200, and the color matches the sample you accepted. Can I place the order today?
Elias|Not on the sample approval alone. That [[review scope::The review scope was color only; it did not establish acceptance of a different panel product or technical properties.]] covered finish B for color. It did not approve P240 as a replacement for the specified panel.
Mina|The sales email calls it equal, but the attachment only shows the finish options. I cannot find the acoustic report.
Elias|Please request a documented [[substitution proposal::A substitution proposal identifies an alternative to the specified product and provides information for the required review.]]. It needs to identify the proposed product and its differences, rather than rely on the word equal.
Mina|I will ask for a side-by-side comparison against the actual project requirements. Should the supplier include mounting details as well as the panel data?
Elias|Yes. Performance and installation information need review together. Matching the face color does not establish whether the proposed system meets the requirements.
Mina|They have sent a fire-performance document bearing the manufacturer's name, but I cannot tell which product or configuration it covers.
Elias|Then its [[applicability::Applicability asks whether the evidence covers the exact proposed product and configuration, not merely the same manufacturer.]] is unverified. Ask for the product and configuration covered; do not treat a familiar logo as evidence for this assembly.
Mina|The supplier says the acoustic rating is close enough. I do not have the test method or the mounting arrangement behind that number.
Elias|We need those details for comparison with the specification. Similar numbers from different tested arrangements are not automatically interchangeable.
Mina|What about the lead time? P200 is quoted at six weeks and P240 at four, but neither production slot is reserved.
Elias|Describe the two-week difference as a [[quoted lead-time saving::The quoted comparison is six weeks versus four; no reserved production slot establishes an actual delivery commitment.]], not a confirmed delivery gain. The technical review and availability still need to be resolved.
Mina|There is also a proposed price reduction. I will show it separately from any change in mounting costs or warranty terms.
Elias|Good. The reviewer needs the full proposed effect, including exclusions. A lower unit price is not proof that the total installed cost will fall.
Mina|The supplier offered to reserve stock if I send a purchase order marked subject to approval. Would that keep the decision open?
Elias|Do not assume that wording avoids a [[commercial commitment::A purchase order may create an obligation; adding a condition does not establish that Mina has authority or no liability.]]. Check the proposed reservation and order terms with the authorized commercial team before committing.
Mina|For the register, I will record finish B accepted for color, P240 substitution under review, and purchasing authorization absent.
Elias|That is accurate. Link the comparison and supporting documents to the substitution entry so the required reviewers can respond to the same proposal.
Mina|When a decision arrives, I will verify exactly which product and configuration it covers before I update the purchasing instruction.
Elias|Yes. Retain the [[decision record::The decision record establishes the authorized outcome and its scope; a prior color selection cannot stand in for it.]] and any conditions. For now, keep the alternative unapproved and the two quoted lead times separate from delivery promises.""",
        transfer_title="A finish selection has a limited scope",
        transfer_setup="Specified product Q10 has an accepted color sample, finish C. Supplier alternative Q12 quotes three weeks rather than Q10's five. Technical evidence and substitution approval are pending, and no production slot or purchase is confirmed.",
        transfer="""Coordinator: The sample acceptance concerns finish ___ only.|C|Finish C is the accepted color; that decision does not approve Q12.
Architect: The proposed alternative is product ___.|Q12|Q12 is the supplier's proposed replacement, not the specified Q10.
Coordinator: The quoted lead-time difference is ___ weeks.|two|Five quoted weeks minus three quoted weeks gives two, not a guaranteed delivery saving.
Architect: Technical acceptance of the substitution remains ___.|pending|The supplied facts contain no completed technical decision or substitution approval.""",
        reference=("AIA: construction scope, substitutions, and payment", "https://learn.aiacontracts.com/6502786-construction-basics-for-owners-contract-sum-owner-financing-and-payment-process/"),
    ),
    scenario(
        title="Cumulative value is not this month's payment",
        skill="Reconcile completed work, eligible stored materials, retainage, and previous certified amounts.",
        setup="Fictional terms: completed work $90,000; separately eligible presently stored materials $10,000; retainage 5% on both; previous certificates $60,000. No other deductions, taxes, or adjustments apply. An unapproved $5,000 change proposal is excluded. This application still requires certification.",
        cast="Priya|Contractor's quantity surveyor\nSam|Contract-administration coordinator",
        dialogue="""Priya|The draft requests one hundred thousand dollars this month. That is the completed-and-stored total, but it looks as though we have missed the earlier certificates.
Sam|Yes. We need a [[cumulative valuation::The valuation is the total eligible completed and stored amount to date, not automatically the amount payable in the current application.]] first, then apply the stated deductions and prior certified amount. Show the two components separately.
Priya|Completed work is ninety thousand. Eligible materials presently stored are ten thousand, separate from the installed work. Together they make one hundred thousand to date.
Sam|Five percent [[retainage::Retainage is the specified withheld portion: five percent of the eligible $100,000 total equals $5,000.]] on both components is five thousand. That leaves ninety-five thousand before we deduct prior certificates.
Priya|Previous certificates total sixty thousand. Ninety-five thousand less sixty thousand leaves thirty-five thousand for this application.
Sam|Correct. Thirty-five thousand is the [[current amount requested::The current request is $95,000 after retainage less $60,000 previously certified, giving $35,000 before certification.]], subject to certification. It is not a payment already made.
Priya|The accounts team has only received fifty thousand against the earlier sixty thousand certified. Should we subtract cash received instead, to include the unpaid ten thousand again?
Sam|No. This calculation subtracts [[previous certificates::The stated calculation deducts prior certified amounts, not cash received; the unpaid balance is tracked separately rather than certified twice.]]. Track that unpaid ten thousand separately; do not request it twice as new work.
Priya|I will reconcile that receivable with accounts. There is also a five-thousand-dollar change proposal in the draft schedule.
Sam|Keep that pending proposal outside this application's supplied basis. Adding it to a spreadsheet would not establish approval.
Priya|The stored-materials line has supporting eligibility records. I have also checked that these materials are not included in the ninety thousand of installed work.
Sam|Good. That avoids [[double counting::Counting the same material as both installed work and presently stored would overstate the eligible cumulative amount.]]. The same value cannot remain in presently stored materials after it has also been included in completed work.
Priya|If those materials are incorporated next period, we need to move their existing value to completed work, not add that value a second time.
Sam|Exactly. Any newly earned installation value is a separate supported item. Reclassifying the same material alone does not create another entitlement to its purchase value.
Priya|Can I assume five percent also applies on the next project? The templates look identical.
Sam|No. Verify that project's contract and applicable requirements. Retainage rates, eligible stored materials, reductions, and other deductions can differ even when the form looks familiar.
Priya|I will attach the line-item reconciliation and distinguish this period's request from the cumulative totals and the earlier unpaid balance.
Sam|Also preserve the [[valuation date::The valuation date identifies the cut-off for work and materials included, supporting comparison with the relevant billing period.]]. Otherwise, an invoice received later could be mistaken for value that belonged in this period.
Priya|The corrected summary is one hundred thousand eligible to date, five thousand retained, sixty thousand previously certified, and thirty-five thousand now requested.
Sam|That reconciles under the supplied terms. Send it through the required review, with the earlier unpaid ten thousand tracked separately and no suggestion that the new amount is already certified.""",
        transfer_title="Subtract certification, not only cash receipts",
        transfer_setup="A fictional application has $70,000 completed and $10,000 separately eligible stored materials to date. Retainage is 5% on both. Previous certificates total $50,000, of which $45,000 is paid. No other adjustments apply. Deduct previous certificates in the new request.",
        transfer="""Surveyor: Total eligible completed and stored value is $___.|80,000|Seventy thousand plus ten thousand gives eighty thousand cumulative eligible value.
Coordinator: The stated retainage is $___.|4,000|Five percent of eighty thousand equals four thousand retained.
Surveyor: The new request, before certification, is $___.|26,000|Eighty thousand less four thousand retainage less fifty thousand previously certified equals twenty-six thousand.
Coordinator: The earlier certified but unpaid balance is $___.|5,000|Fifty thousand certified minus forty-five thousand paid leaves five thousand to track separately.""",
        reference=("AIA: progress-payment calculation and reconciliation", "https://learn.aiacontracts.com/articles/how-to-complete-the-g702-payment-application/"),
    ),
]
