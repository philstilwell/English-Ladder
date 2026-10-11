"""Additional original banking operations conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="One purchase, two transaction stages",
        skill="Reconcile posted and available balances while distinguishing a hold from a second debit.",
        setup="Fictional snapshot: opening posted balance $1,000; a $120 purchase has posted; a separate $80 authorization reduces availability. No other items. In the next snapshot, the matching $80 purchase posts and its hold is fully released at the same time. This sequence does not prescribe real processing times.",
        cast="Rosa|Customer-service officer\nImran|Card-operations analyst",
        dialogue="""Rosa|The customer sees an eighty-dollar card item and thinks it has been charged twice. I have the two account snapshots, but their labels are different.
Imran|Start with the [[posted balance::The posted balance includes completed account entries: $1,000 less the $120 posted purchase equals $880 before the second purchase posts.]]. Before the eighty-dollar purchase posts, it is eight hundred eighty dollars, after the separate one-hundred-twenty-dollar debit.
Rosa|The first snapshot shows eight hundred available. That is eighty less than the posted amount. Where is the difference recorded?
Imran|It is the [[authorization hold::The authorization hold reduces availability by $80 without yet being a posted debit in the first snapshot; it is not an additional completed purchase.]]. It reduces availability, but it has not yet become a posted debit in that first snapshot.
Rosa|So the first calculation is one thousand minus one hundred twenty for posted funds, then minus eighty for availability. That gives eight hundred.
Imran|Correct. In the next snapshot, the purchase posts and the matching hold is released. The [[available balance::The available balance remains $800 when the $80 purchase posts and its matching hold is fully released together, with no other items.]] remains eight hundred under these supplied facts.
Rosa|I had subtracted the posted eighty and then the held eighty again, giving seven hundred twenty. That counts the same purchase twice.
Imran|Exactly. The hold no longer exists in that second snapshot. The posted balance is now eight hundred, and there is no remaining hold to subtract.
Rosa|The activity screen may retain a history line for the old authorization. I need to check its status rather than count every visible line as a debit.
Imran|Use the [[transaction reference::The transaction reference and matching records link the authorization to its corresponding posted purchase; appearance of two history lines alone does not establish two debits.]] and matching records. A history entry and a posted charge can describe stages of the same purchase.
Rosa|Can I tell the customer that any two matching amounts are always one transaction? They might have made two separate eighty-dollar purchases.
Imran|No. Matching amounts alone are insufficient. Confirm the actual linkage and whether both entries posted before explaining a possible duplicate.
Rosa|For this case, the linkage and full hold release are supplied. No duplicate posted debit is shown in the second snapshot.
Imran|That is the supported conclusion. A [[duplicate debit::A duplicate debit would be an unintended second posted deduction; this case supplies one matched purchase and a released hold, not two posted deductions.]] would need a different record pattern and appropriate review, not dismissal based on a familiar amount.
Rosa|What if the final purchase amount differs from the authorization, as it sometimes does when the merchant finalizes the bill?
Imran|Then reconcile the actual posted amount and remaining hold status. The unchanged eight-hundred availability here depends on the amounts matching and release occurring together.
Rosa|I will not promise the same release time on another account. The customer's actual record and the bank's applicable process would need checking.
Imran|Right. The [[hold release::Hold release removes the reserved authorization amount from the availability calculation; its timing and amount must come from the actual records, not this example's sequence.]] is a recorded event, not a deadline this exercise creates. State the snapshot time when explaining the balance.
Rosa|My explanation will say: eight hundred eighty posted and eight hundred available first; then eight hundred posted and available after the matching purchase completes.
Imran|Good. Show the two stages side by side, identify the released hold, and leave any genuinely unmatched or unrecognized transaction to its proper review process.""",
        transfer_title="Do not deduct a released hold again",
        transfer_setup="Opening posted balance $600. A $50 debit posts; a separate $70 hold reduces availability. In the next snapshot, that matching $70 purchase posts and the hold fully releases. No other items.",
        transfer="""Officer: Before the second purchase posts, the posted balance is ___ dollars.|550|The opening six hundred less the first posted fifty-dollar debit gives five hundred fifty.
Analyst: At that stage, the available balance is ___ dollars.|480|The five-hundred-fifty posted balance less the seventy-dollar hold leaves four hundred eighty available.
Officer: When the matching purchase posts, its hold is ___.|released|The case explicitly releases the matched hold when the purchase posts, so it is no longer deducted separately.
Analyst: Subtracting that released hold again would ___ the purchase.|double-count|The posted seventy already reflects the purchase; deducting the released reservation again counts the same amount twice.""",
        reference=("Bank of America: pending and posted account transactions", "https://www.bankofamerica.com/smallbusiness/online-banking/faqs/transaction-reporting/"),
    ),
    scenario(
        title="Quote the currency direction explicitly",
        skill="Read back an exchange quote with currencies, fees, recipient amount, and approval status.",
        setup="Fictional business wire quote: send EUR 10,000; quoted rate USD 1.10 per EUR; separate sender fee USD 25. The quote expires at 14:10 local. For the supplied illustration only, a known EUR 15 intermediary charge is deducted from the sent amount. No other deductions or conversion; no transfer is authorized.",
        cast="Lewis|Payments officer\nMina|Business customer",
        dialogue="""Mina|I need the supplier to receive ten thousand euros. Your quote says one point one zero, but I am unsure which currency that number multiplies.
Lewis|The [[quote direction::The quote is 1.10 US dollars for each euro, so the EUR 10,000 send amount is multiplied by 1.10 to obtain USD 11,000.]] is one dollar ten per euro. Ten thousand euros therefore requires eleven thousand US dollars before the separate sender fee.
Mina|So I multiply the euros by one point one, not divide them. Please keep the currency names beside the rate on the confirmation.
Lewis|I will. The [[conversion amount::The conversion amount is USD 11,000 for the EUR 10,000 send amount; the separate USD 25 sender fee is added afterward.]] is eleven thousand dollars. Adding the twenty-five-dollar sender fee gives a total account debit of eleven thousand twenty-five.
Mina|That twenty-five is in dollars, not euros. It should not be subtracted from the supplier's euro amount as well.
Lewis|Correct. It is the separately charged [[sender fee::The sender fee is USD 25 added to the sender's debit in this case, not deducted again from the EUR 10,000 instructed amount.]]. A different euro charge is deducted along the route under this illustrative quote.
Mina|You have listed fifteen euros as an intermediary charge. That means sending ten thousand does not result in ten thousand arriving under these assumptions.
Lewis|Exactly. The [[intermediary charge::The known EUR 15 intermediary charge is deducted from the EUR 10,000 sent, leaving EUR 9,985 under the stated no-other-deductions assumption.]] leaves nine thousand nine hundred eighty-five euros for the beneficiary in this example.
Mina|Then this quote does not meet the supplier's exact-receipt requirement. I should not approve it just because the send amount matches the invoice.
Lewis|Agreed. We need an available arrangement and explicit terms that address the required receipt amount. Do not assume a charge instruction alone guarantees the net receipt.
Mina|Could you simply increase the send amount by fifteen euros? I would want the revised fees and total before deciding.
Lewis|We would need a revised quote and confirmed charging basis. The supplied numbers explain this quote; they do not establish that every revised instruction has identical deductions.
Mina|The current quote expires at fourteen ten local. If I call back after that, the same rate is not assured.
Lewis|Correct. Check the [[quote validity::Quote validity ends at 14:10 local in the supplied terms; discussing or calculating the quote does not extend its availability.]] before proceeding. I would obtain a current quote rather than reuse the old rate as though it were still available.
Mina|And this conversation has not instructed you to release the money. We have only reconciled what the proposal would debit and deliver.
Lewis|Yes. Actual [[payment authorization::Payment authorization is the approved instruction to proceed under the bank's process; reviewing the quote and its arithmetic does not supply it.]] remains separate. We also need the verified payment details and applicable checks before processing any instruction.
Mina|Please read back the three amounts together: euros sent, dollars debited, and euros received under the supplied deduction.
Lewis|Ten thousand euros sent; eleven thousand twenty-five dollars debited including our separate fee; nine thousand nine hundred eighty-five euros received under the stated assumptions.
Mina|That makes the shortfall clear. Please investigate the exact-receipt options without treating my request for information as permission to send this quote.
Lewis|I will. The next proposal should make the rate direction, charges, recipient amount, validity, and required authorization clear before you make a decision.""",
        transfer_title="Keep sender and recipient currencies separate",
        transfer_setup="Fictional quote: send GBP 2,000 at USD 1.25 per GBP, plus a separate USD 20 sender fee. A known GBP 10 charge is deducted en route. No other deduction or conversion. This is a quote, not authorization.",
        transfer="""Officer: The conversion amount is USD ___.|2,500|Two thousand pounds multiplied by 1.25 dollars per pound gives 2,500 dollars.
Customer: Including the sender fee, my debit would be USD ___.|2,520|The separate twenty-dollar sender fee is added to the 2,500-dollar conversion amount.
Officer: The recipient would receive GBP ___ under these assumptions.|1,990|The stated ten-pound route charge reduces the two-thousand-pound send amount to 1,990 pounds.
Customer: Reviewing this quote does not provide payment ___.|authorization|The case explicitly supplies a quote only, so the calculation is not an approved transfer instruction.""",
        reference=("Wells Fargo: international payments, conversion, and charges", "https://www.wellsfargo.com/biz/online-banking/international/"),
    ),
    scenario(
        title="A mid-period principal change",
        skill="Explain simple loan interest using the stated day-count basis and each actual principal interval.",
        setup="Fictional loan: fixed 6% annual simple rate, Actual/360 basis. Principal is $100,000 for 20 actual days, then $150,000 for 10 actual days. The intervals do not overlap. No fees or compounding; round only the final sum to cents. All dates and approvals are already reconciled for this calculation.",
        cast="Ava|Loan-operations analyst\nNabil|Review officer",
        dialogue="""Ava|The draft interest charge is seven hundred fifty dollars. It applies the closing principal of one hundred fifty thousand to all thirty days.
Nabil|But that [[principal balance::The principal balance was $100,000 for twenty days and $150,000 only for the last ten, so the closing balance cannot be applied to the whole period.]] was only outstanding for ten days. Split the calculation at the balance change instead of using the closing figure throughout.
Ava|The first interval has one hundred thousand outstanding for twenty actual days. At six percent, I multiply one hundred thousand by zero point zero six by twenty.
Nabil|Then divide by three hundred sixty under the supplied [[day-count convention::The Actual/360 convention uses actual elapsed days over a 360-day year denominator; it does not replace every month's actual length with thirty days.]]. That interval contributes three hundred thirty-three dollars and one-third of a dollar before rounding.
Ava|For the remaining ten days, one hundred fifty thousand times six percent times ten divided by three hundred sixty gives two hundred fifty dollars.
Nabil|Correct. Add the two [[accrual intervals::The accrual intervals separate twenty days at $100,000 from ten days at $150,000; summing their interest gives $583.333... before final rounding.]] without overlapping or omitting a day. Together they give five hundred eighty-three dollars and one-third of a dollar.
Ava|Rounded once at the end, the charge is five hundred eighty-three dollars and thirty-three cents. The draft overstates it by one hundred sixty-six dollars and sixty-seven cents.
Nabil|Yes. Preserve [[unrounded interest::Unrounded interest is retained through the interval calculation and summed before rounding, following this exercise's explicit final-rounding rule.]] in the working calculation. Our stipulated rule rounds the total, not each daily amount separately.
Ava|Actual/360 does not mean the principal changed on day thirty or that every month has thirty days. It specifies the denominator and actual-day numerator.
Nabil|Exactly. The supplied intervals happen to total thirty actual days. Another period needs its actual day count and the agreement's convention, not an automatic thirty-day assumption.
Ava|We are using a fixed annual rate here. There is no daily benchmark reset or interest-on-interest calculation hidden in these numbers.
Nabil|Right. This is [[simple interest::Simple interest here accrues on the stated principal at the fixed annual rate without adding accrued interest to principal for compounding.]], with no fees or compounding. Do not label the six percent an all-in annual percentage cost for a different loan.
Ava|If the source records disagreed about when the extra fifty thousand became effective, we would need to resolve that before using these intervals.
Nabil|Yes. The [[value date::The value date establishes when a balance change affects the relevant calculation under the agreement; it must be reconciled rather than inferred from a later screen-posting date.]] and transaction record would matter. Here those facts are already reconciled, so we can concentrate on the interval calculation.
Ava|Would dividing by three hundred sixty-five produce a different answer even with the same balances, rate, and actual days?
Nabil|It would. That is why the denominator belongs in the explanation. We must follow the stated agreement basis, not select whichever calculation looks more familiar.
Ava|I will attach the two principal amounts, twenty and ten days, six-percent annual rate, and the three-hundred-sixty denominator to the correction.
Nabil|Also show the original draft and corrected total. The review record should explain the changed input treatment rather than merely replace one amount with another.
Ava|The final charge in this exercise is five hundred eighty-three dollars and thirty-three cents. The correction concerns the principal intervals, not a reduced rate.
Nabil|Good. Route the corrected calculation through the applicable checking process. Completing the arithmetic does not itself authorize an account posting or amend the loan terms.""",
        transfer_title="Use each principal for its own days",
        transfer_setup="Fictional fixed-rate loan: 4.8% annual simple interest, Actual/360. Principal $50,000 for 15 days, then $80,000 for another 15 days. No overlap, fees, or compounding; round the final sum to cents.",
        transfer="""Analyst: Interest for the first interval is ___ dollars.|100|Fifty thousand times 0.048 times fifteen divided by 360 equals one hundred dollars.
Reviewer: Interest for the second interval is ___ dollars.|160|Eighty thousand times 0.048 times fifteen divided by 360 equals one hundred sixty dollars.
Analyst: The combined interest is ___ dollars.|260|The two non-overlapping intervals contribute one hundred plus one hundred sixty dollars, totaling two hundred sixty.
Reviewer: The annual denominator under these supplied terms is ___.|360|Actual/360 uses the actual days in each interval over the stipulated three-hundred-sixty-day denominator.""",
        reference=("ARRC: simple interest and day-count conventions", "https://www.newyorkfed.org/medialibrary/Microsites/arrc/files/2020/ARRC_SOFR_Bilat_Loan_Conventions.pdf"),
    ),
]
