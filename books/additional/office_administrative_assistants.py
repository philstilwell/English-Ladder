"""Original office expense, mailing, and print-production conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Receipts are not the reimbursement",
        skill="Reconcile an expense claim without paying company-funded or personal costs twice.",
        setup="Fictional trip, all amounts in dollars. Hotel receipt $264, already paid directly by the company. Employee paid a $68 meal receipt: $48 eligible business share and $20 excluded personal share under this case's policy. Employee also paid eligible rail fare $42 and received a $50 cash advance. Figures include all applicable charges; no extra tax, fee, or currency conversion. Approval and payment are pending.",
        cast="Mira|Traveler\nBen|Administrative assistant",
        dialogue="""Mira|The receipts total three hundred seventy-four dollars. I took off the fifty-dollar advance and put three hundred twenty-four as the amount the company owes me.
Ben|We need to separate the [[payment method::The hotel was paid directly by the company, while the meal and rail fare were employee-paid; adding all receipts does not give the amount owed to Mira.]] first. The two-hundred-sixty-four-dollar hotel bill was already paid directly by the company, not by you.
Mira|So the hotel receipt belongs with the trip record, but it isn't another two hundred sixty-four dollars to pay into my account.
Ben|Exactly. Keep it as a [[company-paid expense::The hotel remains a documented trip cost but is excluded from employee reimbursement because the company has already paid it directly.]]. Supporting the trip record and reimbursing you are different purposes; the receipt shouldn't disappear.
Mira|I paid the meal bill myself. It's sixty-eight in total, but the worksheet marks twenty as my personal share and forty-eight as eligible.
Ben|Use that supplied [[itemization::Itemization separates the meal receipt's forty-eight-dollar eligible share from its twenty-dollar personal share; the whole sixty-eight is not reimbursable in this case.]]. Forty-eight enters this claim's eligible employee-paid amount. The twenty is excluded under the fictional policy.
Mira|And the forty-two-dollar rail ticket is fully eligible here. That gives me ninety dollars of eligible costs I paid, before the advance.
Ben|Yes. Those are the [[out-of-pocket expenses::The eligible employee-paid amounts are forty-eight for the meal and forty-two for rail, totaling ninety; the company-paid hotel is not added.]] relevant to this calculation: forty-eight plus forty-two. Don't add the meal's personal share back into that subtotal.
Mira|Now I subtract the fifty dollars I already received. That leaves forty, not three hundred twenty-four or ninety.
Ben|Correct. The [[cash advance::The fifty-dollar advance is money already provided for the trip; subtract it once from ninety dollars of eligible employee-paid costs to obtain forty due.]] is applied once. It's not another expense and it doesn't need to be subtracted from every receipt separately.
Mira|Then the amount due to me is forty dollars, assuming this claim is approved. I shouldn't describe it as already paid.
Ben|Right. The calculated [[net reimbursement::Ninety eligible employee-paid dollars less the fifty-dollar advance leaves forty dollars due to the employee, subject to the pending approval and payment.]] is forty. Calculation, approval, and transfer of money are three different stages.
Mira|I still want the approver to see why the meal receipt says sixty-eight when the eligible line says forty-eight. Will that look like a mismatch?
Ben|Not if the split is clear. Retain the total receipt and show forty-eight business plus twenty personal. The two parts reconcile to sixty-eight.
Mira|And I shouldn't enter another tax allowance because these figures already include all the applicable charges supplied in this example.
Ben|Exactly. No extra tax, fee, or exchange adjustment has been specified. Adding one would change the case instead of checking it.
Mira|What if the advance had been a hundred, with the same ninety dollars of eligible employee-paid costs? Would the company still owe me ten?
Ben|The direction would reverse: ten would remain to return under the case's settlement rule. An excess advance isn't another reimbursement due to you.
Mira|I'll submit the hotel as company-paid, retain the meal split, include the rail receipt, and show ninety less fifty equals forty due.
Ben|That gives the approver a traceable reconciliation. Keep the personal exclusion and advance visible, and leave approval and payment marked pending until they're actually confirmed.""",
        transfer_title="Keep the payer and advance visible",
        transfer_setup="Another fictional trip has $120 of eligible employee-paid expenses, plus a separate $15 personal expense excluded by policy. The company directly paid $200 of additional travel costs. The employee received an $80 advance. No other amounts apply; approval is pending.",
        transfer="""Traveler: Eligible employee-paid costs are ___ dollars.|120|The case explicitly supplies one hundred twenty as eligible; the separate personal and company-paid amounts are not added.
Assistant: The advance to subtract once is ___ dollars.|80|Eighty has already been provided to the employee and offsets the eligible employee-paid total.
Traveler: The calculated amount due to me is ___ dollars.|40|One hundred twenty minus eighty equals forty; the personal fifteen and company-paid two hundred do not enter this reimbursement.
Assistant: The approval status is still ___ .|pending|Reconciling the amounts does not establish approval or payment of the claim.""",
        reference=("Microsoft Learn: settling expense reports against cash advances", "https://learn.microsoft.com/en-us/dynamics365/project-operations/expense/cash-advance"),
    ),
    scenario(
        title="Check the people behind the rows",
        skill="Review a personalized mailing by recipient identity, selection rules, and field accuracy.",
        setup="Fictional printed confirmation mailing: six rows, IDs A01, A02, A02, A03, A04, A05. The owner confirms the two A02 rows are an identical duplicate, not separate people. A01-A03 are confirmed; A04 declined; A05 is pending. Send one letter per confirmed person only. A02 and A03 share a postal address but are different people. A01's verified test postal code is 00123. Nothing has been dispatched.",
        cast="Elena|Office assistant\nKai|List owner",
        dialogue="""Elena|The sheet has six rows, so I expected six letters. But A02 appears twice, and two different names have the same postal address.
Kai|Start with the [[recipient identifier::The supplied IDs distinguish people; the owner confirms that the repeated A02 row is an identical duplicate, leaving five distinct people in six rows.]], not the row count. A02 is duplicated; those two rows belong to one person, not two attendees.
Elena|That leaves five distinct people. Should I also combine A02 and A03 because their address matches?
Kai|No. A shared address isn't a [[duplicate record::A02 and A03 are different people sharing an address; only the repeated A02 row is confirmed as an identical duplicate in this case.]] by itself. They're different people and each needs a separate letter if included in the approved mailing.
Elena|The mailing is for confirmed attendees only. A01, A02, and A03 are confirmed; A04 declined and A05 hasn't answered.
Kai|Then the [[recipient filter::The confirmed-only selection includes A01, A02, and A03 once each; declined A04 and pending A05 are excluded from this particular mailing.]] leaves three letters after resolving the duplicate. It doesn't leave five, six, or four with A02 counted twice.
Elena|I'll exclude the declined and pending records from this run. That doesn't mean deleting their records from the office's main list.
Kai|Correct. The [[data source::The underlying contact data remains distinct from the subset selected for this mailing; excluding someone from the current run does not require deleting their source record.]] still contains their statuses. We're selecting a mailing audience, not erasing people or changing their replies.
Elena|The preview shows A01's postal code as 123, but your verified source says 00123. Can I just ignore the missing zeros?
Kai|No. Those [[leading zeros::The verified test code is 00123; dropping its leading zeros changes the identifier, and the prepared text value must retain all five characters.]] belong to the code. Preserve it as text and check the merged result against the source, rather than accepting a shortened identifier.
Elena|Changing the cell format now wouldn't recover characters already lost from an imported number. I'll check the original source value rather than invent padding.
Kai|Good. Also verify the [[merge field::A merge field inserts a particular source value into the template; the name, address, and code must all come from the intended recipient's record.]] mapping. A correct greeting paired with another person's address would still produce the wrong letter.
Elena|I'll compare all three complete previews, not only the template. The shared address makes it particularly important to check the individual names.
Kai|Yes. A template can look right before actual values are inserted. Check each selected record's name, address, code, and confirmed status together.
Elena|The tool offers a duplicate finder based on names. Should its suggestion override your confirmed IDs?
Kai|No. A suggested match needs review against the record meaning. Our known duplicate is A02; matching names or addresses alone doesn't prove identical people.
Elena|So the check is three letters: A01, A02, A03. One A02, no A04 or A05, and no combined household letter.
Kai|That's the required selection. Keep the source correction traceable and confirm the final output count against those three identifiers.
Elena|I'll keep dispatch pending while we review the corrected previews. Generating a file hasn't put anything in the post.
Kai|Exactly. Record the list review and final output separately from dispatch. The result should be three accurate individual confirmations, not simply six copies because there were six rows.""",
        transfer_title="Count selected people, not rows",
        transfer_setup="A new fictional list has B01, B02, B02, B03, B04. The owner confirms identical B02 duplication. B01 and B03 are confirmed, B02 pending, B04 declined. Send one letter per confirmed person only. B01's verified test postal code is 00456; the preview currently shows 456. No dispatch has occurred.",
        transfer="""Assistant: The selected mailing should contain ___ letters.|two|Only confirmed B01 and B03 qualify; the duplicate pending B02 does not add an eligible recipient.
Owner: B02 remains ___, not confirmed.|pending|Its supplied response status stays pending even though the duplicate row must be resolved.
Assistant: B01's code must read ___ in the output.|00456|The verified source contains both leading zeros; the preview's 456 has lost part of the identifier.
Owner: Dispatch is ___ .|unconfirmed|A selected list and corrected preview do not establish that letters have been dispatched.""",
        reference=("Microsoft Support: preparing source fields and postal codes for mail merge", "https://support.microsoft.com/en-au/word/prepare-your-excel-data-source-for-a-word-mail-merge"),
    ),
    scenario(
        title="Pages, sheets, and finished copies",
        skill="Specify a booklet order without confusing page count, paper count, proofs, and approval.",
        setup="Fictional print brief: 20 A4 pages including all covers, printed as folded A3 booklets. Each physical A3 sheet carries two A4 pages per side, four pages across both sides. Need 30 finished booklets plus two separate complete physical proofs. All use the same paper; no extra covers, waste allowance, or spare copies. Full production must await proof approval. Price and delivery date are not supplied.",
        cast="Sam|Office coordinator\nFarah|Print-room lead",
        dialogue="""Sam|I wrote thirty copies of twenty pages, so six hundred sheets. Then I added two sheets for the proofs. Is that the right paper count?
Farah|Not for this [[booklet imposition::Booklet imposition arranges the document pages for folding; this brief puts four finished pages on each physical A3 sheet, not one page per sheet.]]. Six hundred is the number of finished document pages across thirty booklets, not the number of A3 sheets.
Sam|Each A3 sheet has two A4 pages on the front and two on the back. That makes four document pages per physical sheet.
Farah|Right. [[Duplex printing::Duplex means both sides are printed; the supplied two-pages-per-side layout gives four document pages across a physical sheet, not eight.]] uses both sides here. Twenty pages divided by four gives five A3 sheets for each complete booklet.
Sam|Then thirty finished copies require a hundred fifty sheets, before the separate proofs. I shouldn't halve that again just because they're double-sided.
Farah|Correct. The [[sheet count::Thirty finished booklets at five physical sheets each require one hundred fifty A3 sheets; duplex use is already included in the four-pages-per-sheet calculation.]] already includes the two-sided layout. Dividing by two again would count the same paper saving twice.
Sam|The brief includes covers within the twenty pages. So I don't add another cover sheet to every copy.
Farah|Exactly. Also, the [[finished size::The booklet's finished page size is A4 after the A3 sheets are folded; A3 is the input sheet size, not the finished booklet-page size.]] is A4. A3 describes the paper going into this job, not the size of each finished page.
Sam|What about the two proofs? I treated them as two extra pages, but you need two complete assembled booklets for review.
Farah|Yes. Each [[physical proof::A complete physical proof uses all five sheets of the twenty-page booklet; two separate proofs therefore need ten sheets, not two.]] uses five sheets. Two proofs add ten, giving one hundred sixty sheets under this exact brief.
Sam|That's thirty copies for distribution plus two separate proofs, not thirty copies with the proofs taken out of the delivery quantity.
Farah|Right. The [[production quantity::The order requires thirty finished distribution copies in addition to two proofs; the proofs must not reduce the thirty-copy delivery quantity.]] remains thirty. We prepare the proofs first, but the full run waits for approval.
Sam|If I say the file is ready, that doesn't mean you have permission to print all thirty before anyone checks the folded result.
Farah|Correct. A ready file and an approved proof are different statuses. We need to check the assembled page order, orientation, and content before release.
Sam|The file is in normal reading order. Should I manually rearrange its pages to look like the outer and inner print sheets?
Farah|Don't assume that. Confirm the print-room input requirement. Applying booklet arrangement twice can scramble the sequence; the supplied count alone doesn't establish the correct production file.
Sam|And one hundred sixty is an exact-use calculation. It doesn't include test waste, damaged sheets, or an extra stock allowance.
Farah|Yes. Any allowance would need to be stated separately. We haven't supplied one, and we also haven't agreed a price or delivery date.
Sam|I'll revise the brief: twenty pages including covers, A4 finished, A3 duplex booklet layout, thirty distribution copies plus two full proofs.
Farah|Add five sheets per booklet and one hundred sixty for the stated quantities. Keep full production pending proof approval, with price and delivery still to confirm.""",
        transfer_title="Count another booklet order",
        transfer_setup="A fictional 24-page booklet, covers included, uses four finished pages per physical sheet. Need 18 distribution copies plus one separate complete proof. No waste, spare copies, or extra covers. The proof has not been approved.",
        transfer="""Coordinator: Each booklet requires ___ sheets.|six|Twenty-four finished pages divided by four pages per sheet gives six physical sheets.
Print lead: The eighteen distribution copies use ___ sheets.|108|Eighteen multiplied by six equals one hundred eight sheets, before the separate proof.
Coordinator: Including the complete proof, exact usage is ___ sheets.|114|The six-sheet proof is additional to the one hundred eight sheets for distribution, totaling one hundred fourteen.
Print lead: Full production remains ___ .|pending|The brief requires proof approval, which has not occurred; a paper calculation does not release production.""",
        reference=("Adobe: booklet arrangement, duplex sheets, and finished page order", "https://helpx.adobe.com/ca/acrobat/kb/print-booklets-acrobat-reader.html"),
    ),
]
