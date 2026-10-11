"""Original Bookkeeping and Payroll English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='bookkeeping-payroll', title='Bookkeeping and Payroll English',
    cover_label='ENGLISH FOR BOOKKEEPING, ACCOUNTS, AND PAYROLL TEAMS',
    cover_title='Bookkeeping\n& Payroll', cover_size=39,
    tagline='Explain the figures. Preserve the evidence.',
    audience='For bookkeepers, accounts payable and receivable clerks, payroll assistants, and finance-support staff discussing records, exceptions, and approvals.',
    map_intro='Eight record-based conversations build precise financial English: invoice matching, customer receipts, bank reconciliation, time exceptions, payroll previews, payment approvals, period-close handoffs, and traceable corrections.',
    notes_title='Say what the record establishes.',
    notes_intro='A number can be correct while the explanation around it is wrong. Distinguish a receipt from its allocation, a proposed batch from a released payment, and a duplicate tracker entry from an actual duplicate payment.',
    field_notes=[
        ('Keep the document chain visible', 'Identify the invoice, order, receiving record, and checked quantity separately. An unexplained mismatch calls for supporting evidence. A possible second delivery does not become a documented receipt because it would make the figures agree.', '"A184 and P61 list twelve lamps; R9 records ten. We need support for the remaining two."'),
        ('Separate arithmetic from status', 'A receipt can reduce the overall account position while invoice allocation remains unresolved. A deduction can explain a net-pay difference without its authority being established. State what the calculation shows and what still needs review.', '"Net pay is fifty dollars lower because deductions are fifty higher; the supporting record is pending."'),
        ('Name the exact approval stage', 'Item approval, inclusion in a proposed batch, and release are different states. A reviewer returning at a particular time does not guarantee approval then. Keep excluded items and missing evidence visible in the handoff.', '"Seven invoices have recorded approval; the proposed batch has not been released."'),
        ('Correct claims as well as figures', 'An inaccurate message can outlive a corrected spreadsheet. Identify the specific false claim and replace it with the verified finding. Keep the original record and authorized correction trail according to the actual workplace process.', '"One duplicate tracker entry is confirmed; no duplicate payment or recovery has been established."'),
    ],
    scope_note='All entities, figures, records, deadlines, and approvals are fictional. This is English practice, not accounting, tax, payroll, employment-law, or financial advice. Follow the applicable rules, professional review, privacy safeguards, and organizational controls. The exercises do not authorize posting entries, changing time records, applying deductions, allocating receipts, or releasing payments. Internal review deadlines do not determine employee pay rights. Numerical explanations use only the stated facts.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Bookkeeping, Accounting, and Auditing Clerks.',
             url='https://www.bls.gov/ooh/office-and-administrative-support/bookkeeping-accounting-and-auditing-clerks.htm',
             note='Occupational context for financial records, posting, accuracy checks, and reconciliation. No source examples or statistical forecasts are reproduced.', checked='10 October 2026'),
        dict(title='US Department of Labor. Fact Sheet 21: Recordkeeping.',
             url='https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping',
             note='Background on accurate time and pay records. The fictional cutoff is an internal review time, not a legal pay rule.', checked='10 October 2026'),
        dict(title='OpenStax. Financial Accounting, section 8.6: Bank Reconciliation.',
             url='https://openstax.org/books/principles-financial-accounting/pages/8-6-define-the-purpose-of-a-bank-reconciliation-and-prepare-a-bank-reconciliation-and-its-associated-journal-entries',
             note='Terminology reference for timing differences and reconciliation. The book uses original figures and dialogues, not the source exercises or diagrams.', checked='10 October 2026'),
        dict(title='OpenStax. Financial Accounting, section 4.1: Adjusting Entries.',
             url='https://openstax.org/books/principles-financial-accounting/pages/4-1-explain-the-concepts-and-guidelines-affecting-adjusting-entries',
             note='Background for accounting periods and adjustment terminology. The fictional close item remains subject to accountant review, with no posting instruction.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Matching an invoice to its supporting records',
    scene='A184: two lamps without a receiving record',
    skill='Explain an invoice-matching exception by comparing three records and requesting the missing evidence without assuming a completed delivery.',
    brief='Fictional supplier Alder bills twelve desk lamps on invoice A184. Purchase order P61 lists twelve lamps, but receiving record R9 lists ten. The remaining two may relate to another delivery; no second receiving record is available. Accounts payable clerk Mina asks purchasing colleague Joel to investigate the missing support. No complete match, payment approval, supplier overcharge, or confirmed second delivery has been established.',
    cast='Mina | Accounts payable clerk\nJoel | Purchasing colleague',
    culture=('A matching exception is a question, not an accusation', 'A clear query names the three records and the exact difference. Keep a possible explanation conditional until evidence supports it. This lets the colleague investigate efficiently without changing the receiving record, blaming the supplier, or treating the invoice as approved.'),
    a='''What does invoice A184 bill? | Twelve desk lamps | Ten archive boxes | Two replacement lamps | A confirmed second delivery only | The supplier invoice specifically bills twelve desk lamps.
What does receiving record R9 show? | Ten lamps | Twelve lamps | No delivery at all | An approved payment | R9 records ten received, which differs from the invoice and order quantity.
What is known about the remaining two? | A second delivery is possible but unsupported by another record | They definitely arrived yesterday | They prove Alder overcharged | They have already been paid twice | The possibility of another delivery remains unverified because its receiving record is unavailable.''',
    vocabulary='''accounts payable | Records and processes concerning amounts owed to suppliers; abbreviated AP. | raise an accounts payable query
supplier invoice | Supplier document requesting payment for stated goods or services. | identify the supplier invoice
purchase order | Order document specifying requested items and terms; abbreviated PO. | match the purchase order
receiving record | Evidence recording goods received under the stated process. | check the receiving record
three-way match | Comparison of invoice, order, and receipt information. | investigate a three-way match exception
matching exception | Difference preventing the required records from agreeing. | document the matching exception
invoice quantity | Number of units billed on the invoice. | verify invoice quantity
order quantity | Number of units requested on the purchase order. | compare order quantity
received quantity | Number of units documented as received. | preserve received quantity
supporting document | Record providing evidence for an entry or decision. | request the supporting document
line item | Separately identified entry on a transaction document. | check the line item
unit price | Price stated for one item or unit. | verify the unit price
supplier account | Record grouping transactions for a particular vendor. | identify the supplier account
invoice reference | Identifier for a supplier bill. | quote the invoice reference
order reference | Identifier linking a transaction to the purchase request. | retain the order reference
receipt reference | Identifier for the receiving evidence. | include the receipt reference
quantity variance | Difference between compared unit counts. | explain the quantity variance
partial delivery | Delivery of fewer than all ordered units. | investigate a partial delivery
unmatched balance | Portion not yet supported by the required matching evidence. | explain the unmatched balance
query status | Current state of an unresolved inquiry. | preserve query status
payment hold | Status preventing payment pending the relevant process. | distinguish a payment hold
approval evidence | Record establishing the permission actually given. | obtain approval evidence
overbilling | Billing more than is properly chargeable under the relevant facts. | avoid assuming overbilling
document chain | Linked records supporting a transaction from order to receipt and bill. | preserve the document chain''',
    precision='A184 bills twelve lamps and P61 orders twelve, but R9 supports ten received. The difference is two lamps. The agreement between invoice and order does not remove the mismatch with the receiving record.',
    precision_extra='Another delivery is possible, not confirmed. Request its receiving support if it exists. Do not rewrite R9 to twelve, accuse Alder of overbilling, or describe a complete match or payment approval before the missing evidence is resolved.',
    phrases='''Identify the invoice | I am querying Alder invoice A184.
Name the order | It relates to purchase order P61.
State the billed quantity | The invoice bills twelve desk lamps.
State the order quantity | The purchase order also lists twelve.
State the receipt evidence | Receiving record R9 lists ten.
Describe the difference | Two lamps are not supported by the available receiving record.
Keep a hypothesis conditional | They may relate to another delivery.
Request the missing support | Can you locate a second receiving record?
Avoid claiming a match | The three records do not yet fully agree.
Preserve the original record | I will not change R9 to match the invoice.
Avoid an accusation | This difference does not by itself establish overbilling.
Separate approval | We have not established payment approval.
Request a traceable reply | Please include A184, P61, and R9 in the response.
Limit the statement | Ten are documented as received in the available record.
Keep the query open | The remaining two still need support.
Close with the next action | Please check the delivery evidence and report what is actually documented.''',
    notes='''Also lists | Shows agreement between two documents without implying a complete match.
Not supported by | Identifies an evidence gap rather than asserting the goods never arrived.
May relate to | Keeps a possible explanation conditional.
By itself | Limits the conclusion that can be drawn from one mismatch.
Documented as | Attributes a quantity to its evidence source.
Do not yet fully agree | Keeps the matching exception visible without declaring fraud or final resolution.''',
    d='''Which summary is accurate? | A184 and P61 list twelve; R9 records ten; support for two is missing | All three documents confirm twelve | Alder definitely supplied only ten in total | A second receipt has already been found | The summary preserves the document-specific quantities and the unresolved evidence gap.
Which request moves the query forward? | Please locate any receiving record for the remaining two lamps | Please change R9 to twelve without evidence | Please mark the invoice paid now | Please accuse Alder of intentional overbilling | The missing evidence concerns receipt of the remaining two lamps.
What does may relate to another delivery mean? | It is a possible explanation requiring support | The delivery is confirmed | The supplier has admitted an error | Payment has been approved | May marks a hypothesis rather than an established receiving fact.
Which reference belongs to the receiving record? | R9 | A184 | P61 | An invented second reference | R9 is explicitly the receiving record, while A184 and P61 identify other documents.''',
    dialogue='''Mina | Joel, could you check Alder A184? The invoice and order both say twelve lamps, but the receipt support doesn't cover all twelve.
Joel | Let us walk through the [[document chain::Document chain links invoice A184, order P61, and receiving record R9 so the precise mismatch is visible.]]. Which purchase order and receiving record are you comparing, and what does each document actually show?
Mina | It's order P61 and receiving record R9. P61 and A184 show twelve; R9 shows ten.
Joel | Then we have a [[matching exception::Matching exception arises because the invoice and order show twelve while the receiving record shows ten.]], not a complete match. The invoice agreeing with the order does not establish that all twelve are documented as received.
Mina | Could the other two have come separately? I haven't found another receiving record, so I can't confirm that.
Joel | That is the right distinction. A [[partial delivery::Partial delivery is a possible context for the difference, but a later receipt still needs evidence.]] could explain the first record, but we need evidence before saying the rest arrived separately.
Mina | Please check with receiving and keep A184, P61, and R9 together in the query.
Joel | I will request the missing [[supporting document::Supporting document would provide evidence for any additional receipt rather than relying on an assumed delivery.]], if one exists, and use A184, P61, and R9 in the inquiry. I will not invent a second receipt reference.
Mina | Someone suggested changing R9 to twelve because it would match the order. That would hide the gap.
Joel | Agreed. The [[received quantity::Received quantity documented in R9 is ten and must not be overwritten to force agreement with the other records.]] in R9 should remain ten unless the appropriate evidence and correction process establish something different. The query must preserve what we currently know.
Mina | Does this prove an overcharge? I need to answer a colleague without accusing the supplier on incomplete evidence.
Joel | We should not assert [[overbilling::Overbilling is not established by an unresolved receiving-record gap when another delivery remains possible.]] from this alone. We have a gap in the available receipt evidence, and another delivery remains possible. That is different from proving an improper charge.
Mina | Then I'll say two unsupported by the available record, not definitely undelivered.
Joel | Yes. The [[quantity variance::Quantity variance is two lamps between the billed and ordered twelve and the documented receipt of ten.]] is precise, while the cause remains open. It gives the receiving team a concrete question to investigate without deciding the outcome for them.
Mina | And this isn't a payment approval. We're asking for receiving evidence, not releasing an invoice.
Joel | Understood. We have not established [[approval evidence::Approval evidence is absent from the supplied facts, so the matching inquiry must not be described as payment authorization.]] for payment in this exchange. Locating a document and completing the relevant approval process are not interchangeable statements.
Mina | Please say whether you found the missing record. Handled wouldn't tell me whether the exception is resolved.
Joel | I will report the actual [[query status::Query status should say whether the missing receipt support was found, not merely that someone handled the request.]]. If support is still missing, the reply will say so and retain the two-lamp difference against the same document references.
Mina | I'll leave twelve billed and ordered, ten documented, two requiring support, possible second delivery unconfirmed.
Joel | That captures the [[unmatched balance::Unmatched balance is the two-lamp portion not supported by the available receiving record, not a confirmed debt or loss.]] in quantity terms. I will follow up on the evidence and keep any later conclusion tied to the records that support it.''',
    rehearsal=["Complete the invoice-matching dialogue.","Read the three references and quantities aloud: A184 twelve, P61 twelve, R9 ten. Then read the request for evidence of the remaining two.","Complete the transfer, check the explained key, and reread the query without claiming either overbilling or a complete match."],
    transfer_title='Name the three records and the unresolved difference',
    transfer_setup='Complete the matching query without assuming a second receipt or payment approval.',
    transfer='''Clerk: "The supplier invoice is ___." | A184 | A184 identifies the Alder invoice billing twelve desk lamps.
Colleague: "The purchase order is ___." | P61 | P61 identifies the order for the same twelve lamps.
Clerk: "Receiving record ___ lists ten." | R9 | R9 is the available receiving evidence and supports only ten lamps.
Colleague: "Support for the remaining ___ lamps is missing." | two | Two is the difference between twelve billed and ten documented as received.'''
))


BOOK['units'].append(unit(
    title='Explaining receipts and outstanding customer balances',
    scene='The money arrived; the invoice allocation did not',
    skill='Acknowledge an identified receipt while separating total account arithmetic from unresolved invoice-level allocation.',
    brief="Fictional customer Pine has invoice 410 for $600 and invoice 411 for $400. A $600 receipt is identified as Pine's, but it contains no invoice reference. Both invoices remain open in the ledger pending allocation. Receivables clerk Ava asks customer contact Luis for the missing reference. The two invoices total $1,000 and the identified receipt is $600, leaving a $400 net difference across these stated items; that arithmetic does not establish which invoice is settled.",
    cast='Luis | Customer contact\nAva | Receivables clerk',
    culture=('Acknowledge the money before querying its application', 'A customer may hear open invoice as an accusation of nonpayment. Confirm the receipt that is actually identified, then explain the narrower allocation problem. An amount matching one invoice is a useful clue, not sufficient permission to assign the payment without the required reference.'),
    a='''What is known about the $600 receipt? | It belongs to Pine but lacks an invoice reference | It is definitely allocated to invoice 410 | It belongs to an unknown customer | It proves invoice 411 was paid in full | The customer identity is known, but invoice allocation remains unresolved.
What do the two invoices total? | $1,000 | $600 | $400 | $1,600 | Six hundred plus four hundred gives a thousand dollars of stated invoice amounts.
Which invoice is confirmed settled? | Neither while allocation is pending | Invoice 410 because the amounts match | Invoice 411 because it is smaller | Both automatically | The ledger keeps both invoices open pending the missing allocation information.''',
    vocabulary='''accounts receivable | Records of amounts due from customers; abbreviated AR. | check accounts receivable
customer account | Record grouping transactions for a particular customer. | identify the customer account
cash receipt | Record of money received. | acknowledge the cash receipt
receipt allocation | Assignment of received money to specified account items. | confirm receipt allocation
unallocated receipt | Received amount not yet assigned to particular items. | explain the unallocated receipt
invoice reference | Identifier showing which invoice a payment concerns. | request the invoice reference
remittance advice | Payment information explaining the items a payer intends to settle. | request remittance advice
open invoice | Invoice still shown as unsettled in the relevant ledger. | explain an open invoice
ledger | Organized accounting record of transactions and balances. | check the ledger
settlement | Application or completion that resolves the relevant amount due. | confirm invoice settlement
invoice-level balance | Unsettled amount associated with one particular invoice. | distinguish an invoice-level balance
account-level position | Combined position across the specified customer-account items. | explain the account-level position
net difference | Result after offsetting the stated amounts for comparison. | calculate the net difference
payer identity | Identification of the person or entity sending money. | verify payer identity
aging bucket | Group of outstanding balances classified within a specified age interval and date basis. | reconcile the aging buckets
matching amount | Figure equal to another amount but not necessarily linked to it. | distinguish a matching amount
allocation query | Request to establish where a receipt should be applied. | raise an allocation query
statement of account | Summary of relevant customer transactions and balances. | clarify the statement of account
credit balance | Account position representing an amount in the customer's favor under the relevant records. | verify a credit balance
overdue | Past the applicable due date, when that date is established. | avoid assuming overdue status
unapplied cash | Received funds awaiting application to the relevant items. | identify unapplied cash
days past due | Days elapsed after the applicable due date, measured at the specified aging date. | calculate days past due
allocation instruction | Direction identifying the intended application of a receipt. | record the allocation instruction
collection message | Communication seeking or discussing payment of amounts due. | correct a misleading collection message''',
    precision='Invoices 410 and 411 total $1,000. The identified $600 receipt leaves a $400 net difference across those stated items. Do not call the full $1,000 unpaid without acknowledging the receipt, and do not claim invoice 411 is the confirmed remaining debt.',
    precision_extra='The $600 receipt matches the amount of invoice 410, but its invoice reference is missing. Both invoices remain open pending allocation. Request the intended reference or remittance detail, and do not invent due dates, overdue status, or an authorized application.',
    phrases='''Acknowledge receipt | We have identified your $600 receipt.
Separate the missing detail | The receipt does not include an invoice reference.
Name the invoices | Invoice 410 is $600 and invoice 411 is $400.
Explain the ledger status | Both invoices remain open pending allocation.
Avoid a nonpayment accusation | I am not saying no money was received.
Request the intended application | Which invoice or invoices should this receipt be applied to?
Ask for supporting detail | Could you provide the remittance advice?
Qualify an amount match | The receipt matches 410 in amount, but that does not confirm allocation.
State the total | The two invoice amounts total $1,000.
State the net arithmetic | After the identified $600 receipt, the net difference is $400.
Keep the levels distinct | That is an account-level comparison, not a settled invoice allocation.
Avoid an overdue claim | We have not supplied a due date here.
Preserve the receipt | The allocation query does not erase the money received.
Keep the request focused | We need the intended invoice reference, not another payment.
Avoid unsupported closure | I cannot mark 410 settled from the amount alone.
Close with the next step | Please confirm the allocation so the invoice records can be reviewed accurately.''',
    notes='''Pending allocation | Explains why an invoice remains open despite an identified receipt.
Not saying no money | Corrects the broader misunderstanding before requesting more detail.
Matches in amount | Identifies similarity without claiming transaction linkage.
After the identified receipt | Makes the basis of the net calculation explicit.
Which invoice or invoices | Allows a single or divided application without assuming either.
From the amount alone | Limits what a matching figure establishes.''',
    d='''Which statement is accurate? | $600 was received from Pine, but invoice allocation is pending | Pine has paid nothing | Invoice 410 is definitely settled | Invoice 411 is definitely overdue | The known receipt and unresolved allocation must both remain visible.
What does the $400 net difference establish? | The arithmetic across the stated invoices and receipt | That invoice 411 alone is the confirmed unpaid item | That no receipt exists | That the payment should be refunded | The difference is account-level arithmetic and does not resolve invoice-specific application.
Which request is appropriate? | Please confirm the intended invoice reference or remittance details | Please pay another $600 because the receipt has no reference | Please accept that 410 is closed automatically | Please invent a new due date | The missing information concerns allocation, not whether the money arrived.
Why is a matching amount insufficient here? | The receipt has no invoice reference and allocation remains pending | Equal figures can never relate to the same transaction | Invoice 410 does not exist | Pine's identity is unknown | The known facts explicitly leave application unresolved despite the equal amounts.''',
    dialogue='''Luis | Your message says both invoices are open, but we sent six hundred dollars. Has that payment been missed?
Ava | We've identified Pine's [[cash receipt::Cash receipt confirms six hundred dollars from Pine, even though its invoice application is unresolved.]]. The money isn't missing; the receipt lacks an invoice reference, so its application is unresolved.
Luis | Thank you. Which two invoices are on the message? I need to explain this to our accounts team.
Ava | Invoice 410 is $600 and 411 is $400. Each is still an [[open invoice::Open invoice describes an unsettled ledger item while the identified receipt awaits allocation.]] in the ledger while the receipt awaits allocation.
Luis | Six hundred is exactly the amount of 410. Why not close that one and leave 411 outstanding?
Ava | It's a [[matching amount::Matching amount is a clue, but the missing reference prevents it from proving the intended invoice application.]], but that doesn't confirm your intended application. We still need the reference rather than guessing from the figure.
Luis | What should I ask our team for? Another screenshot of the payment probably wouldn't answer your question.
Ava | Please ask for the [[remittance advice::Remittance advice can identify the invoice or invoices Pine intended the payment to settle.]] or the intended invoice reference. It should say which invoice or invoices the payment was meant to settle.
Luis | Before I go back to them, the overall figures are a thousand in invoices and six hundred received. Is that right?
Ava | Yes. The [[net difference::Net difference is four hundred dollars after comparing the thousand-dollar invoice total with the six-hundred-dollar receipt.]] across these stated items is $400. That acknowledges the receipt without deciding which invoice it settles.
Luis | So the remaining four hundred doesn't itself prove that 411 is the unpaid invoice. The allocation could affect the individual balances.
Ava | Correct. An [[invoice-level balance::Invoice-level balance depends on the actual allocation, which cannot be inferred from the overall four-hundred-dollar difference.]] depends on the actual application. We can't derive that application from the account-level difference alone.
Luis | Please say that in the next message. Otherwise someone may think you're asking us to send the same six hundred again.
Ava | I'll make it an [[allocation query::Allocation query asks where the existing receipt belongs, rather than demanding a second payment.]], not a duplicate payment request. We'll acknowledge the receipt and ask only for the missing application detail.
Luis | Are you also saying anything is overdue? I haven't seen a due date in the information we've discussed.
Ava | We haven't established [[overdue::Overdue requires an applicable due date, which has not been supplied in this case.]] status here. I won't add a deadline or collection claim that the supplied information doesn't support.
Luis | Keep both invoice numbers and the receipt amount together in the request, please. That will help our team identify the right payment.
Ava | The [[customer account::Customer account groups Pine's two invoices and identified receipt while preserving their separate allocation states.]] summary will show 410 at $600, 411 at $400, and Pine's identified $600 receipt awaiting application.
Luis | I'll ask for the intended reference. Then you'll have something firmer than an amount that happens to match.
Ava | Exactly. The missing [[allocation instruction::Allocation instruction identifies the intended application and is the missing information needed for the next review.]] will support the next settlement review. For now, the receipt is acknowledged and both invoice applications remain unresolved.''',
    rehearsal=["Complete the customer-receipt dialogue.","Read the receipt acknowledgment and allocation request aloud. Keep $1,000 invoiced, $600 received, and $400 net difference separate from individual invoice settlement.","Complete the transfer and check the key. Repeat the readback without asking for the same payment again."],
    transfer_title='Acknowledge the receipt and query its application',
    transfer_setup='Complete the customer-account readback. Keep the net calculation separate from invoice settlement.',
    transfer='''Clerk: "The identified receipt is ___ dollars." | 600 | Six hundred dollars has been identified as Pine's receipt, not as a missing payment.
Customer: "The two invoices total ___ dollars." | 1000 | One thousand is the sum of invoice 410 at six hundred and 411 at four hundred.
Clerk: "The net difference across these items is ___ dollars." | 400 | Four hundred is the arithmetic difference, not a confirmed invoice-specific allocation.
Customer: "The receipt still needs ___." | allocation | Allocation remains pending because the receipt has no intended invoice reference.'''
))

BOOK['units'].append(unit(
    title='Qualifying a bank reconciliation difference',
    scene='A July posting helps explain June',
    skill='Describe a plausible timing difference with the correct direction and dates while keeping the broader reconciliation incomplete.',
    brief="A fictional bank reconciliation runs through June 30. The bank balance is $300 lower than the cash ledger. A $300 deposit entered in the ledger on June 30 appears in the bank's July 1 activity. Other reconciliation checks are not complete. Bookkeeper Nia explains the timing evidence to colleague Omar without claiming that every difference has been cleared or that an adjusting entry is automatically needed.",
    cast='Omar | Finance colleague\nNia | Bookkeeper',
    culture=('Explain a plausible cause without declaring the review finished', 'A matching amount and sensible timing can support an explanation while other checks remain open. Name the cutoff, the direction of the difference, and both posting dates. A careful summary can be useful without overstating the completeness of the reconciliation.'),
    a='''Which balance is lower at June 30? | The bank balance by $300 | The cash ledger by $300 | Both are equal | The supplier balance by $600 | The brief explicitly states that the bank balance is three hundred dollars below the ledger.
When does the deposit appear in bank activity? | July 1 | June 1 | June 30 in both records | An unknown year-end date | The deposit is in the June 30 ledger but appears in bank activity on July 1.
What is the status of the broader reconciliation? | Other checks remain incomplete | Fully completed and approved | All differences disproved | An adjusting entry already posted | The supplied facts leave other reconciliation checks unfinished.''',
    vocabulary='''bank reconciliation | Comparison explaining differences between bank and accounting records. | prepare a bank reconciliation
cash ledger | Accounting record containing the relevant cash transactions. | compare the cash ledger
bank balance | Amount reported in the relevant bank record. | identify the bank balance
ledger balance | Amount shown in the corresponding accounting record. | distinguish the ledger balance
reconciliation cutoff | Date through which the comparison is being prepared. | state the reconciliation cutoff
deposit | Money placed into the relevant bank account. | trace the deposit
deposit in transit | Deposit recorded by the business but not yet recorded by the bank at the comparison date. | identify a deposit in transit
timing difference | Mismatch caused by the same item appearing at different times. | explain a timing difference
bank activity | Transactions appearing in the bank's record. | check subsequent bank activity
posting date | Date on which an entry is recorded in a system. | compare posting dates
subsequent activity | Transactions recorded after the period being reviewed. | inspect subsequent activity
reconciling item | Item explaining part of a difference between records. | document a reconciling item
outstanding check | Issued check not yet reflected as cleared in the relevant bank record. | distinguish an outstanding check
bank charge | Fee recorded by the bank for a relevant service. | identify a bank charge
interest credit | Amount added by the bank for earned interest. | distinguish an interest credit
recording error | Incorrect entry of a transaction or amount. | investigate a recording error
adjusted balance | Balance after the relevant reconciliation adjustments are considered. | verify the adjusted balance
unreconciled difference | Portion of a discrepancy not yet fully resolved. | report an unreconciled difference
reconciliation evidence | Records supporting the comparison and explanation. | retain reconciliation evidence
direction of difference | Which figure is higher or lower and by how much. | state the direction of difference
completion claim | Statement that the whole review has been finished. | qualify a completion claim
review status | Current stage of the checking process. | preserve review status
ledger adjustment | Change posted to the accounting record through the relevant process. | distinguish a ledger adjustment
reconciliation sign-off | Confirmation of the completed review by the relevant person. | obtain reconciliation sign-off''',
    precision='At the June 30 cutoff, the bank is $300 lower than the ledger. A $300 deposit recorded in the ledger on June 30 appears at the bank on July 1. That sequence is consistent with a timing difference in the stated direction.',
    precision_extra='The deposit is already recorded in the ledger, so do not propose recording it again merely to explain the timing. Other reconciliation checks are unfinished. The matching amount supports the explanation but does not establish a complete reconciliation or approved adjustment.',
    phrases='''Name the cutoff | This reconciliation is through June 30.
State the direction | The bank balance is $300 lower than the cash ledger.
Identify the ledger entry | The deposit was recorded in the ledger on June 30.
Identify the bank date | It appears in the bank activity on July 1.
Explain the timing | The same deposit appears on opposite sides of the cutoff.
Qualify the explanation | That is consistent with a timing difference.
Use the technical term | It is a deposit-in-transit item at the comparison date.
Avoid reversing the difference | The bank is lower, not higher, at June 30.
Keep the receipt distinct | The ledger already contains the deposit.
Avoid duplicate recording | We should not record the same deposit again merely for timing.
Preserve the open checks | Other reconciliation checks are not complete.
Limit the conclusion | This explains a plausible item, not the whole review.
Request the evidence | Keep both dated records with the reconciliation.
Separate correction and timing | A timing difference is not automatically a recording error.
Avoid premature sign-off | I cannot call the reconciliation complete yet.
Close with a qualified summary | The deposit supports the timing explanation; the remaining checks are still open.''',
    notes='''Through June 30 | Defines the comparison cutoff rather than a later bank date.
Lower than | Preserves the direction of the stated difference.
On July 1 | Gives the subsequent bank appearance of the deposit.
Consistent with | Signals supported interpretation without claiming every check is complete.
Already contains | Explains why blindly adding the same deposit again would be misleading.
Not complete yet | Keeps the broader review state explicit.''',
    d='''Which explanation has the correct direction? | The June 30 ledger includes $300 that appears at the bank July 1 | The bank includes an extra $300 that the ledger lacks | Both records have identical cutoff activity | The deposit proves a $600 loss | The earlier ledger entry is consistent with the bank being lower at the June cutoff.
Why should the deposit not simply be entered again? | It is already recorded in the cash ledger | The bank never recorded it | Every timing difference requires duplicate posting | The ledger has no cash account | The ledger already contains the deposit, so timing alone does not justify recording it again.
Which completion statement is accurate? | The timing item is supported, but other checks remain open | The whole reconciliation is signed off | No further checks are possible | Every difference is necessarily the same deposit | The brief leaves other checks incomplete despite the matching deposit evidence.
Which evidence supports this cutoff explanation? | The June 30 ledger deposit linked to its July 1 bank appearance | The July 1 bank balance without the June cutoff record | A second $300 ledger deposit entered to match the bank | An undated note saying the totals look equal | The two linked dated records explain when the same deposit appears on each side; neither a duplicate posting nor an undated balance claim supplies that evidence.''',
    dialogue='''Omar | The June summary has the bank three hundred below the ledger. Have you found an explanation, or are we still looking for the missing amount?
Nia | There's evidence of a [[timing difference::Timing difference is supported by the deposit appearing in the June 30 ledger and July 1 bank activity.]]. A $300 deposit is in the ledger on June 30 and appears in bank activity on July 1.
Omar | So at the June cutoff the ledger includes it, but the bank doesn't show it until the next day.
Nia | Right. Our [[reconciliation cutoff::Reconciliation cutoff is June 30, so the July 1 bank entry belongs to subsequent activity.]] is June 30. The sequence fits the bank being lower by $300, not higher.
Omar | Is deposit in transit the right wording? I don't want the manager to read missing deposit as money the bank has lost.
Nia | Yes, the dated records support a [[deposit in transit::Deposit in transit describes the deposit recorded in the books but not yet in the bank record at the cutoff.]] at that comparison date. Its appearance on July 1 supports the timing explanation.
Omar | It matches the entire difference. Can I mark the reconciliation complete now?
Nia | Not yet. The [[review status::Review status remains incomplete because other reconciliation checks have not been finished.]] still includes unfinished checks. One matching amount doesn't show that we've reviewed every other transaction.
Omar | Then the update should say we've found supporting evidence, while leaving the rest of the review open.
Nia | Exactly. The [[reconciling item::Reconciling item is the identified deposit timing difference, not proof that the entire review is complete.]] is supported by the two dated records. Keep that progress separate from a claim that all checks are finished.
Omar | Someone suggested adding another three hundred to the ledger so the records agree. Would that be the adjustment?
Nia | No. The [[cash ledger::Cash ledger already includes the June 30 deposit, so timing alone does not justify entering the same deposit again.]] already includes this deposit. Recording it again merely because the bank shows it later would duplicate the same receipt.
Omar | So we first distinguish a timing item from an unrecorded transaction. Not every difference calls for another entry.
Nia | Correct. These facts don't establish a [[ledger adjustment::Ledger adjustment is a separate posting decision and is not automatically required by this timing evidence.]]. We are explaining the existing deposit, not authorizing a duplicate posting.
Omar | What should stay with the reconciliation so another reviewer can verify the explanation?
Nia | Keep the June 30 ledger entry and July 1 [[bank activity::Bank activity on July 1 is the subsequent record supporting the deposit's later bank appearance.]] together, with the amount and their connection visible.
Omar | I'll write bank lower by $300 at June 30, matching deposit in the bank the next day, other checks unfinished.
Nia | That preserves the [[direction of difference::Direction of difference is bank below ledger by three hundred dollars, not the reverse.]] and the review limit. It doesn't hide unfinished work behind the word balanced.
Omar | And I won't say approved. The evidence is progress, but the remaining checks still have to be completed.
Nia | Agreed. [[Reconciliation sign-off::Reconciliation sign-off has not been established while other required checks remain unfinished.]] is outstanding. Keep the supported timing explanation in the working file for the rest of the review.''',
    rehearsal=["Complete the reconciliation dialogue.","Read the cutoff explanation aloud: June 30 ledger, July 1 bank, bank $300 lower at June 30. Then read why a second ledger deposit is not justified.","Complete the transfer and check the key. Retain the unfinished review status in the corrected summary."],
    transfer_title='Explain the cutoff difference precisely',
    transfer_setup='Complete the reconciliation summary using the supplied direction, amount, dates, and review status.',
    transfer='''Bookkeeper: "At June 30, the bank is $300 ___ than the ledger." | lower | Lower preserves the stated direction of the difference at the cutoff.
Colleague: "The deposit is recorded in the ledger on June ___." | 30 | June 30 is the ledger date, before the deposit appears in bank activity.
Bookkeeper: "It appears at the bank on July ___." | 1 | July 1 is the subsequent bank date supporting the timing explanation.
Colleague: "Other reconciliation checks remain ___." | incomplete | Incomplete prevents the supported timing item from becoming a false claim of full reconciliation.'''
))


BOOK['units'].append(unit(
    title='Requesting evidence for time exceptions',
    scene='A missing clock-out is not a known finish time',
    skill='Request evidence for a time-record exception while distinguishing the roster, employee recollection, and confirmed actual work time.',
    brief="Employee Eli's Tuesday timecard has no clock-out entry. The roster shows a 17:00 finish, while Eli recalls finishing at 17:30. Supervisor Hana can review a work log before the internal approval cutoff at 14:00 today. Payroll assistant Dev must request that review and preserve both sources without choosing a finish time. Actual finish time is unconfirmed. The internal cutoff does not authorize an invented entry or determine Eli's pay rights.",
    cast='Dev | Payroll assistant\nHana | Supervisor',
    culture=('Keep the evidence request separate from a judgment about the employee', 'A missing entry is a record problem, not proof of dishonesty or proof that no work occurred. Attribute the roster and recollection clearly. Ask the appropriate reviewer to examine the available log and report the verified status without forcing the record to fit a deadline.'),
    a='''What is missing from Tuesday's timecard? | A clock-out entry | Eli's entire employment record | A confirmed wage rate | The supplied roster finish | The timecard lacks the end-of-work entry, while other information is separately available.
How do the two time sources differ? | Roster says 17:00; Eli recalls 17:30 | Both confirm 17:00 actual finish | Roster says 14:00; Eli recalls noon | Both prove thirty minutes of unauthorized absence | The roster and employee recollection give different times, neither yet confirmed as actual.
What can Hana review before 14:00? | The work log | A final approved payroll already released | A fabricated clock-out | An unrelated supplier invoice | The brief identifies the work log as evidence the supervisor can review before the internal cutoff.''',
    vocabulary='''timecard | Record of employee work-time entries. | check the timecard
clock-out | Entry recording the end of a work period. | query a missing clock-out
clock-in | Entry recording the start of a work period. | verify the clock-in
roster | Planned schedule of assigned work. | distinguish the roster
scheduled finish | End time shown in the planned schedule. | identify the scheduled finish
actual finish | Time work actually ended, established through relevant evidence. | verify the actual finish
employee recollection | Employee's remembered account of events or timing. | record the employee recollection
work log | Record of work activity relevant to the review. | review the work log
time exception | Missing or inconsistent timekeeping information requiring review. | raise a time exception
supervisor review | Check carried out by the relevant supervising person. | request supervisor review
internal cutoff | Organization's stated processing or approval deadline. | meet the internal cutoff
approval status | Current state of the required permission or verification. | report approval status
time correction | Authorized amendment to a time record based on the relevant evidence. | document a time correction
source attribution | Identification of where a statement or figure came from. | preserve source attribution
unverified entry | Record value that has not yet been established. | avoid an unverified entry
exception queue | List of time or payroll issues awaiting review. | maintain the exception queue
pay period | Defined interval covered by the relevant payroll. | identify the pay period
timesheet approval | Confirmation of a time record under the actual process. | distinguish timesheet approval
audit trail | Record showing the history and basis of changes. | preserve the audit trail
scheduled hours | Work time indicated by the roster. | separate scheduled hours
reported hours | Work time described by a person or source. | qualify reported hours
verified hours | Work time established through the relevant review. | distinguish verified hours
review outcome | Finding or unresolved status produced by a check. | record the review outcome
payroll handoff | Transfer of relevant payroll information to the next responsible person. | complete the payroll handoff''',
    precision='The roster gives 17:00, Eli recalls 17:30, and the actual finish remains unconfirmed. Do not convert the scheduled time into verified work time or treat a missing clock-out as proof of no work.',
    precision_extra='Hana can review the work log before the internal 14:00 cutoff. That deadline is for the fictional review process; it is not a rule about pay entitlement. Any correction needs its evidence, reviewer, and actual approval status preserved.',
    phrases='''Identify the exception | Tuesday's timecard is missing a clock-out.
Name the planned time | The roster shows a 17:00 finish.
Attribute the recollection | Eli recalls finishing at 17:30.
State the unresolved fact | The actual finish time is not confirmed.
Request the evidence review | Could you review the work log?
Name the internal deadline | The approval cutoff is 14:00 today.
Avoid defaulting to the roster | I will not treat the scheduled finish as verified actual time.
Avoid defaulting to memory | The recollection needs to remain attributed.
Reject a false inference | A missing entry does not prove no work occurred.
Keep the request neutral | I am asking for verification, not assigning blame.
Preserve both sources | Please keep the roster and Eli's account visible.
Ask for the outcome | Report what the log supports and what remains unresolved.
Keep approval explicit | Has the time correction actually been approved?
Preserve the change history | The correction needs its supporting trail.
Avoid an invented entry | I will not fill the gap just to clear the queue.
Close with the handoff | The work-log review is pending; actual finish remains unconfirmed.''',
    notes='''Shows versus recalls | Distinguishes a planned schedule from an employee's remembered account.
Actual | Refers to what happened, not simply what was scheduled.
Before 14:00 | Defines the internal review window, not a rule about wages.
Supports | Connects a conclusion to evidence.
Remain attributed | Keeps a reported claim attached to its source.
Just to clear | Identifies administrative pressure that does not establish a fact.''',
    d='''Which exception note is accurate? | Missing Tuesday clock-out; roster 17:00; Eli recalls 17:30; actual finish unconfirmed | Eli definitely finished at 17:00 | Eli definitely finished at 17:30 | Eli did no work because the entry is missing | The note preserves the missing entry, both attributed sources, and unresolved actual time.
What should Hana be asked to do? | Review the work log and report the supported finding | Select the earlier time automatically | Enter the later time without review | Treat the internal cutoff as a pay-rights decision | The supplied next step is evidence review by the supervisor.
Which statement about 14:00 is correct? | It is the fictional internal approval cutoff | It establishes the actual Tuesday finish | It proves the employee's pay entitlement | It is the scheduled Tuesday clock-out | The deadline concerns today's review process, not Tuesday's actual work time.
What should accompany an authorized correction? | The evidence and review trail | An erased history of the earlier gap | A guessed finish time | An unrelated supplier approval | A traceable correction retains the basis and status of the change.''',
    dialogue='''Dev | Could you review Eli's missing Tuesday clock-out? The roster and recollection don't agree, and we need the evidence checked before today's internal cutoff.
Hana | Please give me the [[source attribution::Source attribution keeps the roster's 17:00 and Eli's recollection of 17:30 attached to their distinct origins.]] for each time. I want to know what the roster says and what Eli reported before drawing any conclusion about the actual finish.
Dev | The roster says 17:00. Eli recalls 17:30, but the timecard has no end entry.
Hana | Then the [[actual finish::Actual finish is unconfirmed because the available schedule and recollection have not yet been verified against the work evidence.]] is still unconfirmed. We should not select seventeen hundred simply because it was scheduled, or seventeen thirty simply because it was recalled.
Dev | There's a work log available. Can you review it before 14:00 today?
Hana | Yes. I will review the [[work log::Work log is the available evidence Hana can examine before the internal approval cutoff.]] and report what it supports. Please keep the missing clock-out and both reported times visible while that review is pending.
Dev | I'm being asked to clear the queue. Entering the roster time now and checking later would make an assumption look verified.
Hana | Do not treat a [[scheduled finish::Scheduled finish is the roster's planned 17:00 time, not verified evidence of when Eli actually stopped work.]] as verified actual time merely to clear the queue. The deadline does not create evidence that the missing entry currently lacks.
Dev | Please keep the request neutral. A missed clock-out doesn't mean Eli did no work.
Hana | Call it a [[time exception::Time exception describes the missing or inconsistent record without accusing Eli or proving that no work occurred.]] requiring review. We are checking a record gap; we have not established dishonesty, absence, or a confirmed finish time.
Dev | Once you begin checking, can I say 17:30 is approved, or do I need the actual result?
Hana | Wait for the [[review outcome::Review outcome is the finding from examining the evidence, not the fact that Hana has started looking.]]. Starting a check is not approval of a particular time. If the evidence remains inconclusive, that unresolved status must be reported accurately.
Dev | And the 14:00 cutoff is today's internal review deadline, not a rule deciding Eli's entitlement to pay.
Hana | Correct. The [[internal cutoff::Internal cutoff is the organization's fictional review deadline and does not determine employee pay rights.]] defines this processing window. It does not establish the actual hours worked or replace the applicable payroll and employment requirements.
Dev | When there's an authorized correction, the next colleague will need to see why the entry changed.
Hana | Preserve the [[audit trail::Audit trail records the evidence, review, and authorized change rather than hiding the original missing entry.]]. The supporting information and approval status should remain traceable through the actual workplace process, not be replaced by an unexplained number.
Dev | I'll hand over Tuesday clock-out missing, roster 17:00, Eli recalls 17:30, log review pending before 14:00.
Hana | That is an accurate [[payroll handoff::Payroll handoff carries the record gap, source-specific times, pending evidence review, and internal deadline together.]]. Add that actual finish remains unconfirmed, so the next person does not mistake the two candidate times for a completed decision.
Dev | I'll keep the exception visible and the actual finish unconfirmed until the review supplies a supported result.
Hana | Thank you. Keep the [[approval status::Approval status remains unresolved until the relevant review and authorization establish any correction.]] explicit. I will review the available log and report the supported result or remaining uncertainty before the stated internal cutoff.''',
    rehearsal=["Complete the time-exception dialogue.","Read the attributed times aloud: roster 17:00, Eli recalls 17:30, actual finish unconfirmed. Keep today's 14:00 internal review deadline separate.","Complete the transfer and check the key. Repeat the evidence request without selecting an unsupported finish time."],
    transfer_title='Request the time review without selecting a result',
    transfer_setup='Complete the time-exception summary using the distinct sources and the actual review deadline.',
    transfer='''Assistant: "The missing entry is Tuesday's ___." | clock-out | Clock-out is the absent end-of-work entry on the timecard.
Supervisor: "The roster gives ___." | 17:00 | 17:00 is the planned finish, not the verified actual time.
Assistant: "Eli recalls ___." | 17:30 | 17:30 is Eli's attributed recollection and remains subject to evidence review.
Supervisor: "The internal review cutoff is ___ today." | 14:00 | 14:00 is today's processing deadline, not a determination of actual hours or pay rights.'''
))

BOOK['units'].append(unit(
    title='Explaining a payroll preview',
    scene='Same gross pay, fifty dollars less net',
    skill='Explain the arithmetic of two payroll previews while separating a visible deduction from its unverified supporting authority.',
    brief="Preview A shows Morgan's gross pay of $1,200, deductions of $200, and net pay of $1,000. Preview B shows the same $1,200 gross pay, deductions of $250, and net pay of $950. A new $50 deduction line is present, but its supporting record is pending. Payroll assistant Leila must explain the numerical change to Morgan without calling it a salary cut, guessing the deduction's purpose, or declaring it authorized.",
    cast='Morgan | Employee\nLeila | Payroll assistant',
    culture=("Lead with the employee's actual question", 'A lower net figure can look like lower gross pay. Explain the unchanged gross amount and the increased deduction total plainly. Then address the missing support as a separate unresolved question; correct arithmetic does not prove a deduction is valid or approved.'),
    a='''What stays the same in both previews? | Gross pay of $1,200 | Deductions of $200 | Net pay of $1,000 | Every line of the calculation | Both previews show gross pay of twelve hundred dollars.
Why is B's net pay $50 lower arithmetically? | Deductions increase from $200 to $250 | Gross pay falls by $50 | Net pay is unrelated to deductions | A confirmed tax rule changes the salary | The deduction total rises fifty dollars while gross pay stays unchanged.
What remains pending? | Support for the new $50 deduction | The amount of gross pay | The arithmetic difference | An already completed refund | The supporting record for the new deduction line has not yet been supplied.''',
    vocabulary='''payroll preview | Preliminary display of a payroll calculation before final processing. | compare payroll previews
gross pay | Pay amount before the relevant deductions. | state gross pay
deduction | Amount subtracted from pay in the stated calculation. | identify a deduction
net pay | Amount remaining after the stated deductions. | explain net pay
deduction total | Combined amount of the listed deductions. | compare deduction totals
deduction line | Individual entry identifying an amount subtracted. | query a new deduction line
supporting record | Evidence explaining or authorizing the relevant entry. | request the supporting record
pay statement | Document showing the relevant earnings and deductions. | read the pay statement
earnings line | Entry showing a component of pay before deductions. | distinguish an earnings line
pay component | Separately identifiable part of remuneration or its calculation. | identify the pay component
payroll register | Record summarizing payroll details for the relevant run. | check the payroll register
pay run | Particular cycle of payroll calculation and processing. | identify the pay run
preview comparison | Review of differences between preliminary calculations. | prepare a preview comparison
gross-to-net | Relationship between gross pay, deductions, and the resulting net amount. | explain gross-to-net movement
regular rate of pay | Overtime calculation rate including required pay components, not just base pay. | verify the regular rate
nondiscretionary bonus | Bonus that does not meet the applicable discretionary-bonus exclusion criteria. | review a nondiscretionary bonus
deduction authority | Valid basis or approval required for a deduction under applicable rules. | verify deduction authority
payroll query | Request for clarification about a pay record or calculation. | raise a payroll query
withholding | Amount retained from pay under the relevant applicable basis. | distinguish withholding from gross pay
voluntary deduction | Deduction based on an applicable employee election or agreement. | verify a voluntary deduction
statutory deduction | Deduction arising under relevant legal requirements. | distinguish a statutory deduction
correction status | Whether a change has been requested, approved, or processed. | report correction status
final payroll | Completed payroll at the relevant processing stage. | distinguish a preview from final payroll
variance explanation | Account of how and why compared figures differ. | give a variance explanation''',
    precision='Both previews show $1,200 gross. A subtracts $200 to reach $1,000 net; B subtracts $250 to reach $950 net. The $50 net decrease corresponds to the $50 deduction increase, not a stated reduction in gross pay.',
    precision_extra='A visible deduction line is not proof of its authority. The supporting record is pending, and the purpose has not been supplied. Do not label it tax, insurance, or a voluntary choice, and do not promise a refund or final pay outcome.',
    phrases='''Acknowledge the concern | You are asking why preview B shows less net pay.
Start with the unchanged figure | Gross pay remains $1,200 in both previews.
Explain preview A | A shows $200 in deductions and $1,000 net.
Explain preview B | B shows $250 in deductions and $950 net.
State the movement | Deductions rise by $50 and net pay falls by $50.
Identify the new line | Preview B includes a new $50 deduction.
Separate arithmetic and authority | The calculation explains the difference, not whether the line is authorized.
Name the evidence gap | The supporting record is still pending.
Avoid an invented purpose | I cannot identify this as tax or insurance from the information supplied.
Avoid a salary-cut claim | The previews do not show a reduction in gross pay.
Request the support | Please provide the record supporting the new deduction.
Keep the status provisional | We are discussing a preview, not a confirmed final payment.
Avoid a refund promise | No correction or refund has been established yet.
Keep personal details limited | We should use the appropriate private payroll channel.
Summarize precisely | Same gross pay; higher deductions; lower net pay; support pending.
Close with the unresolved question | The new line needs its basis verified before its status can be explained fully.''',
    notes='''Remains | Marks the gross-pay amount as unchanged.
Rise by and fall by | Describe opposite movements of the same fifty-dollar magnitude.
Includes | Establishes that a line appears, not that it is authorized.
Not whether | Separates a mathematical explanation from an approval question.
Still pending | Preserves the unresolved supporting-record status.
Preview, not final | Limits what can be claimed about a future payment.''',
    d='''Which calculation matches preview B? | $1,200 minus $250 equals $950 | $1,200 minus $200 equals $950 | $1,150 minus $250 equals $1,000 | $950 plus $50 equals $1,200 | Preview B retains the twelve-hundred-dollar gross and subtracts two hundred fifty.
Which explanation is accurate? | Net falls because deductions rise, while gross remains unchanged | Gross salary was definitely reduced | The new deduction is definitely insurance | The preview proves a refund has been approved | The supplied arithmetic establishes the movement but not the new line's purpose or authority.
Which reply addresses Morgan's unresolved question? | I will verify the new $50 line's purpose and authority from its supporting record | I have checked that $1,200 minus $250 is $950, so the line needs no review | I will describe the $50 as insurance because that is a common deduction | I will confirm a $50 refund before the line is reviewed | Morgan needs the basis for the new deduction, not only another subtraction; its purpose, authority, and any correction remain unestablished.
Which statement overclaims? | The new line is authorized because it appears in the preview | The line is fifty dollars | The supporting record is pending | Both gross figures are twelve hundred | Appearance in a preliminary calculation does not establish the deduction's valid basis.''',
    dialogue='''Morgan | My preview has dropped from a thousand to nine hundred fifty. Has somebody reduced my salary?
Leila | The [[gross pay::Gross pay remains twelve hundred dollars in both previews, so the supplied figures do not show a gross-pay cut.]] shown hasn't changed: it's $1,200 in both previews. Let's compare the deductions next.
Morgan | Could you take me through A and B in the same order? I want to see where the fifty appears.
Leila | A's [[deduction total::Deduction total is two hundred dollars in A and two hundred fifty in B.]] is $200, leaving $1,000 net. B subtracts $250 from the same gross, leaving $950.
Morgan | So the extra fifty deducted explains the fifty less left over. It isn't a fifty-dollar change to the twelve hundred.
Leila | That's the [[gross-to-net::Gross-to-net explanation connects unchanged gross pay, increased deductions, and the resulting lower net amount.]] movement. The subtraction agrees, but we still need to check the basis of the new line.
Morgan | What is it for? I can't tell whether it's tax, insurance, or something I chose.
Leila | The new $50 [[deduction line::Deduction line is visible in preview B, but its purpose and supporting basis have not been supplied.]] is visible, but its supporting record is pending. I can't identify its purpose from the information here.
Morgan | I assumed anything appearing on a preview had already been checked and approved. Is that not established?
Leila | Not by this [[payroll preview::Payroll preview is a preliminary calculation and does not by itself prove approval of every line.]] alone. It shows a calculation, not proof of the authority behind every line.
Morgan | Please ask about that specific fifty. I'm not disputing twelve hundred minus two hundred fifty; I need to know why the new charge is there.
Leila | Understood. The [[payroll query::Payroll query concerns the basis of the new fifty-dollar deduction, not the subtraction itself.]] will focus on the new line's basis, not simply repeat the subtraction you've already checked.
Morgan | Could the reviewer see that distinction? Otherwise I may get the same numerical explanation without an answer to my concern.
Leila | I'll request the [[supporting record::Supporting record is the missing evidence needed to explain the new deduction's basis and status.]] and clarification of the line's purpose and authority. Those are the unresolved questions.
Morgan | Should I treat nine hundred fifty as my final payment, or is that still not confirmed?
Leila | We aren't confirming [[final payroll::Final payroll has not been established by comparing these preliminary records with unresolved supporting documentation.]] here. With these preliminary records and missing support, I can't promise that amount, a correction, or a refund.
Morgan | Please handle my records through the appropriate payroll contact. I don't want this sent to people who aren't reviewing it.
Leila | Of course. I'll report the [[correction status::Correction status is not yet a completed change or refund; the current action is a private supporting-record query.]] through the appropriate private process. Currently support is pending, with no completed change established.
Morgan | Then the summary is same gross, fifty more deducted, fifty less net, and the reason for that new deduction still needs checking.
Leila | Yes. That's the [[variance explanation::Variance explanation states the numerical movement while retaining the unresolved basis of the new deduction.]] the records support. I'll carry the specific evidence question forward without treating the preview as final approval.''',
    rehearsal=["Complete the payroll-preview dialogue.","Read A and B in the same order: gross, deductions, net. Then read Morgan's question about the new $50 line and Leila's evidence request.","Complete the transfer and check the key. Keep correct subtraction separate from authorization and final payment."],
    transfer_title='Explain the preview without endorsing the deduction',
    transfer_setup='Complete the gross-to-net readback. Preserve the unchanged gross figure and the pending support.',
    transfer='''Assistant: "Gross pay remains ___ dollars." | 1200 | Twelve hundred is unchanged in both payroll previews.
Employee: "Preview B shows ___ dollars in deductions." | 250 | Two hundred fifty is B's deduction total, fifty more than A.
Assistant: "That leaves ___ dollars net in B." | 950 | Nine hundred fifty is twelve hundred less two hundred fifty.
Employee: "The supporting record is still ___." | pending | Pending preserves the unresolved basis of the new deduction rather than declaring it authorized.'''
))


BOOK['units'].append(unit(
    title='Making approval status unambiguous',
    scene='Seven approved items, no released batch',
    skill='Distinguish invoice approval, proposed batch membership, payment release, and an excluded exception in a concise status handoff.',
    brief='A fictional payment set contains eight invoices. Seven have recorded approval. Invoice V22 awaits a receiving document and is excluded from the proposed seven-item batch. The batch itself has not been released, and the approver returns at 15:00. Payment preparer Ben briefs colleague Imani, who must not tell suppliers that all eight invoices are approved or that any payment has already been sent. Return time is not a guaranteed release time.',
    cast='Imani | Finance colleague\nBen | Payment preparer',
    culture=('Use separate verbs for separate control stages', "Approved, included, released, and paid are not interchangeable. A brief update should identify the approved items, the proposed batch, and any excluded exception. Naming the approver's return helps plan follow-up, but it does not promise the outcome of that review."),
    a='''How many invoices have recorded approval? | Seven | Eight | One | None | Seven of the eight invoices have recorded approval in the supplied payment set.
Why is V22 excluded from the proposal? | Its receiving document is missing | It has already been paid twice | The supplier has canceled it | Its amount is confirmed as zero | V22 awaits receiving evidence and is not part of the proposed seven-item batch.
What does 15:00 establish? | The approver's return time | A guaranteed release time | Confirmation all suppliers are paid | Automatic inclusion of V22 | The stated time concerns availability of the approver, not a completed payment decision.''',
    vocabulary='''payment batch | Group of payment items prepared for joint processing. | prepare a payment batch
batch proposal | Suggested set of items for the next payment process. | distinguish the batch proposal
invoice approval | Recorded permission for the specified invoice under the relevant process. | verify invoice approval
recorded approval | Permission evidenced in the available record. | confirm recorded approval
batch release | Authorized step sending the prepared batch into the relevant payment process. | distinguish batch release
payment execution | Carrying out the payment instruction at the relevant stage. | verify payment execution
payment confirmation | Evidence that the specified payment action occurred. | request payment confirmation
excluded item | Entry deliberately left out of the proposed set. | identify the excluded item
receiving evidence | Record supporting receipt of the relevant goods. | obtain receiving evidence
approval dependency | Missing condition required before the next approval stage. | state the approval dependency
approver | Person authorized to give the relevant permission. | contact the approver
return time | Time when a person is expected to be available again. | state the return time
authorization limit | Boundary of what a recorded approval permits. | preserve the authorization limit
batch membership | Items included in the specified group. | confirm batch membership
control stage | Distinct step in checking or authorizing a transaction. | identify the control stage
release status | Whether the relevant batch has actually been released. | report release status
payment status | Current stage of the payment process. | clarify payment status
exception item | Entry requiring separate attention before the process can proceed. | track the exception item
pending evidence | Supporting material not yet available. | identify pending evidence
supplier update | Communication to a vendor about the relevant account position. | qualify a supplier update
remittance notice | Message describing a payment or its intended invoice application. | verify a remittance notice
approval trail | Record of who approved what and at which stage. | retain the approval trail
batch count | Number of entries in a specified payment group. | reconcile the batch count
status readback | Restatement of the stages and unresolved conditions. | give a status readback''',
    precision='There are eight invoices in the original set, seven with recorded approval, and seven in the proposed batch. V22 is excluded pending its receiving document. Do not describe V22 as approved simply because the other seven are approved.',
    precision_extra='The seven-item batch has not been released. The approver returns at 15:00, but that is not a promise of release or supplier receipt of funds. Keep invoice approval, proposed inclusion, release, and payment confirmation separate.',
    phrases='''Identify the original set | We began with eight invoices.
State the approved count | Seven have recorded approval.
Name the exception | V22 is awaiting its receiving document.
State the exclusion | V22 is excluded from the proposed batch.
Confirm the proposed count | The proposal contains seven items.
Keep item and batch stages separate | Invoice approval is not the same as batch release.
State release status | The batch has not been released.
Avoid a payment claim | We have no confirmation that payment has been sent.
Name the availability | The approver returns at 15:00.
Limit the timing inference | That return time does not guarantee release.
Preserve the missing evidence | V22 still needs receiving support.
Correct an overbroad update | It would be inaccurate to say all eight are approved.
Request a stage-specific answer | Are you asking about approval, inclusion, or release?
Keep suppliers informed accurately | I can report the current stage without promising payment.
Read back the whole position | Seven approved, V22 excluded, seven proposed, none confirmed released.
Close with the next review | We will seek the relevant review when the approver is available.''',
    notes='''Have recorded approval | Limits the claim to permission evidenced for the specified items.
Excluded from | Defines batch membership without canceling the invoice.
Has not been released | States the actual batch stage.
Returns at | Describes availability, not an approval outcome.
All eight | Identifies the overgeneralization that the exception makes inaccurate.
Are you asking about ...? | Clarifies which control stage the other person means.''',
    d='''Which status line is accurate? | Seven invoices approved; V22 excluded; proposed batch unreleased | All eight approved and paid | Seven released because they were approved | V22 included without receiving evidence | The correct line preserves item approval, exclusion, proposal, and release status.
What would overstate the meaning of 15:00? | Payments are guaranteed to be sent at 15:00 | The approver returns at 15:00 | Review depends on the relevant process | Release is not yet confirmed | Return time does not guarantee an approval or payment-release outcome.
Which count belongs to the proposed batch? | Seven | Eight | Fifteen | Twenty-two | The proposal excludes V22 and therefore contains the seven other invoices.
What information is still needed for V22? | The receiving document | An invented payment receipt | Proof the other seven were canceled | A new supplier name | V22 is explicitly awaiting evidence of receipt before the exception can be resolved.''',
    dialogue='''Imani | A supplier asked whether the run is approved. There were eight invoices originally; are all eight ready to go?
Ben | No. Seven have [[recorded approval::Recorded approval applies to seven invoices, not all eight in the original payment set.]]. Invoice V22 is still awaiting a receiving document, and it is excluded from the proposed batch.
Imani | Then the proposed batch has seven, not eight. V22 stays outside it.
Ben | Correct. The [[batch membership::Batch membership is seven items because V22 has been excluded from the proposal.]] has changed. Keep V22 visible as an exception, but do not count it among the seven proposed payment items.
Imani | Have those seven been released, or are we only talking about invoice approval?
Ben | The [[release status::Release status remains unreleased even though the seven included invoices have recorded approval.]] is not released. Approval of the seven invoices does not mean the batch itself has passed the release stage or that payment has been sent.
Imani | What receiving document is missing for V22? I need a reason, not just held.
Ben | It is awaiting [[receiving evidence::Receiving evidence is the missing document for V22 and explains its exclusion from the proposed batch.]], specifically the receiving document. That requirement remains open; the invoice has not become approved because the other seven are.
Imani | The approver is back at three. Is that a release time I can give the supplier?
Ben | It is the [[return time::Return time is 15:00 for the approver, not a guaranteed batch-release or payment time.]], fifteen hundred. It tells us when the approver returns, not what the review outcome will be or when any payment will reach a supplier.
Imani | I'll keep 15:00 as the approver's return, with no promised release time.
Ben | Exactly. Preserve the [[control stage::Control stage distinguishes the unreleased proposal from invoice approval and later payment execution.]]. A useful update names where the process stands instead of using approved as a shorthand for every later step.
Imani | Could you read back the status for the team, so we don't use approved to mean several different things?
Ben | Seven invoices have approval; V22 is an [[excluded item::Excluded item identifies V22 as outside the proposed seven-item batch while its receiving document is pending.]] pending its receiving document. The seven-item proposal is not released. The approver returns at fifteen hundred, with no release time guaranteed.
Imani | Does excluded mean canceled? I don't want someone telling V22's supplier the invoice has been rejected permanently.
Ben | No. It remains an [[exception item::Exception item keeps V22 active for follow-up without treating exclusion as cancellation or permanent rejection.]] needing its supporting document. Its absence from this proposal is not a cancellation decision or a statement that the supplier has no valid invoice.
Imani | I'll retain seven approved, seven proposed, V22 excluded, and the batch unreleased.
Ben | Yes. The [[approval trail::Approval trail records the actual permissions without substituting them for uncompleted release or payment stages.]] should show the actual permissions while the release status remains separate. Nobody should infer payment confirmation merely from the existence of item approvals.
Imani | The supplier update will name the stage we actually know, without saying the money has gone.
Ben | Good. A [[supplier update::Supplier update should report the supported process stage without promising that payment has been sent or will arrive at a set time.]] can be specific without overpromising. The next review and any later release must be confirmed through the actual process before we report them as complete.''',
    rehearsal=["Complete the payment-batch dialogue.","Read the full status aloud: eight original invoices, seven approved, V22 excluded, seven proposed, batch unreleased, approver back at 15:00.","Complete the transfer and check the key. Repeat the supplier update without promising release or receipt of funds."],
    transfer_title='Read back approval, exclusion, and release',
    transfer_setup='Complete the payment-status handoff without turning approval into payment confirmation.',
    transfer='''Preparer: "The number of approved invoices is ___." | seven | Seven invoices have recorded approval in the original eight-item set.
Colleague: "The excluded invoice is ___." | V22 | V22 is left out because its receiving document is still missing.
Preparer: "The batch has not been ___." | released | Released names the separate stage that the proposed batch has not completed.
Colleague: "The approver returns at ___." | 15:00 | 15:00 is the return time, not a guaranteed release or supplier-payment time.'''
))

BOOK['units'].append(unit(
    title='Handing over a period-close review',
    scene='Nine checks done, one period question open',
    skill='Hand over an unresolved cutoff question with its amount, dates, review owner, and unapproved posting status intact.',
    brief="The fictional June close has nine of ten checklist items complete. A $240 maintenance invoice is dated July 2 but describes June service. The accountant must review its posting period; no adjusting entry has been approved. Alex takes over the open-item follow-up from Hana at noon. The handoff must distinguish document date from service period and follow-up responsibility from authority to choose or post an accounting entry.",
    cast='Hana | Outgoing bookkeeper\nAlex | Incoming bookkeeper',
    culture=('Transfer responsibility without pretending the decision transferred too', 'A good handoff gives the next person the unresolved question and the evidence needed to pursue it. It does not turn a follow-up owner into an accounting approver. Keep the incomplete checklist item visible even when the other nine tasks are finished.'),
    a='''How many checklist items are complete? | Nine of ten | All ten | One of ten | None | Nine items are complete, with one period-close review still outstanding.
What dates differ on the maintenance item? | Invoice dated July 2; service described as June | Invoice dated June 2; service described as July | Both document and service are confirmed in August | No date or service period is supplied | The document date and stated service period fall in different months.
What does Alex take over at noon? | Follow-up on the open item | Automatic authority to post an adjustment | A fully approved close | Responsibility to erase the exception | Alex takes over follow-up while the accountant's period review and entry approval remain unresolved.''',
    vocabulary='''period close | Process of completing accounting work for a defined reporting interval. | hand over the period close
close checklist | List of required tasks for finishing the reporting period. | update the close checklist
open item | Matter still unresolved or incomplete. | retain the open item
invoice date | Date printed or assigned to the supplier document. | identify the invoice date
service period | Interval during which the invoiced service was provided. | distinguish the service period
posting period | Accounting period to which an entry is assigned. | request posting-period review
cutoff question | Issue about which period should contain a transaction or amount. | raise a cutoff question
maintenance expense | Cost associated with relevant maintenance work. | identify the maintenance expense
accountant review | Evaluation by the relevant accounting professional. | obtain accountant review
adjusting entry | Accounting entry addressing the relevant period-end recognition or measurement. | distinguish an adjusting entry
accrual | Recognition of an amount in the relevant period before the associated cash settlement. | discuss an accrual question
accrued expense | Expense recognized with a related obligation before payment. | identify an accrued-expense review
prepayment | Payment made before the related benefit or service is fully received. | distinguish a prepayment
supporting invoice | Supplier bill retained as evidence for the review. | attach the supporting invoice
posting approval | Permission for the specified accounting entry. | verify posting approval
unposted item | Record or proposed transaction not yet entered in the ledger. | identify an unposted item
journal entry | Record of a transaction using the relevant accounting accounts. | review the journal entry
general ledger | Main accounting record containing account balances and entries. | distinguish the general ledger
follow-up owner | Person responsible for pursuing the next response or action. | name the follow-up owner
handover time | Time responsibility passes to the next person. | confirm the handover time
close status | Current completion stage of the period-end process. | report close status
carrying amount | Amount at which an asset or liability is recorded after relevant recognized adjustments. | reconcile the carrying amount
recognition schedule | Record allocating an amount to accounting periods under the specified treatment. | review the recognition schedule
cutoff evidence | Dates and service information relevant to the period question. | retain cutoff evidence''',
    precision='The invoice amount is $240, its date is July 2, and its description refers to June service. Those are distinct facts. The accountant must review the posting period; the assistant should not choose July solely from the invoice date.',
    precision_extra='Nine of ten checklist items are complete, so the close is not fully finished. Alex takes follow-up ownership at noon, but no adjusting entry has been approved. Follow-up responsibility does not establish authority to decide or post the entry.',
    phrases='''State the close position | Nine of ten checklist items are complete.
Name the open item | The maintenance invoice still needs period review.
Give the amount | The invoice is for $240.
Give the document date | It is dated July 2.
Give the service period | The description refers to June service.
Identify the distinction | The invoice date and service period are not the same fact.
Name the reviewer | The accountant needs to review the posting period.
Preserve approval status | No adjusting entry has been approved.
Avoid an automatic period choice | I will not assign July merely from the invoice date.
Transfer the follow-up | Alex takes over the open-item follow-up at noon.
Separate roles | Owning the follow-up does not mean approving the entry.
Keep the evidence together | Retain the invoice and its June-service description.
Avoid false completion | The close is not ten out of ten yet.
State the dependency | This item remains open pending the accountant's review.
Request a clear result | Please record the reviewed period and actual approval status.
Close with the handoff | Nine complete, one open, Alex following up, no entry approved.''',
    notes='''Dated versus describes | Distinguishes the document's date from the service period it reports.
Still needs | Marks the review as outstanding.
Merely from | Identifies an insufficient basis for a decision.
Takes over at noon | Specifies when follow-up responsibility changes.
Does not mean approving | Separates administrative ownership from accounting authority.
Nine complete, one open | Prevents a high completion count from becoming a claim of full closure.''',
    d='''Which handoff preserves the facts? | $240 invoice dated July 2 for June service; accountant review pending | July date automatically proves July posting | June close fully complete | Alex has approved an adjusting entry | The summary separates amount, document date, service period, and unresolved review.
What does nine of ten complete mean? | One checklist item remains open | All accounting decisions are final | The final item can be ignored | Nine invoices have been paid | The completion count leaves one required checklist item unfinished.
Which responsibility changes at noon? | Alex takes over follow-up | Alex automatically becomes the posting approver | The supplier changes the invoice date | The entry is automatically posted | The brief assigns follow-up ownership rather than authority for an accounting decision.
Which statement is unsupported? | The adjusting entry has already been approved | The invoice is $240 | The description refers to June | The document is dated July 2 | No adjusting entry has been approved in the supplied close status.''',
    dialogue='''Hana | Alex, you're taking over at noon. Nine June-close checks are complete; the maintenance invoice is the one still awaiting review.
Alex | Please give me the [[close status::Close status is nine of ten checklist items complete, not a fully finished June close.]] first, then the invoice details and the decision we are waiting for. I do not want the one open item hidden behind the completed count.
Hana | It's $240, dated July 2, but the description says June service.
Alex | Then we need to distinguish the [[invoice date::Invoice date is July 2, separate from the June service period described on the document.]] from the service period. The printed July date should not make us overlook the fact that the description relates to June.
Hana | The accountant needs to decide the posting period. I haven't treated the July date as an automatic answer.
Alex | I will retain that [[cutoff question::Cutoff question concerns the appropriate posting period for a July-dated invoice describing June service.]] as unresolved. The amount, document date, and service description give the reviewer the facts without our substituting an assumed answer.
Hana | There isn't an approved adjusting entry either. Knowing the amount doesn't mean the entry is ready.
Alex | I will make the [[posting approval::Posting approval has not been given for an adjusting entry, even though the invoice amount is known.]] status explicit. Knowing the amount does not establish that the period treatment or any proposed entry has been approved.
Hana | At noon you're taking over the follow-up, not the accountant's authority to approve the treatment.
Alex | Understood. I become the [[follow-up owner::Follow-up owner is Alex from noon, responsible for pursuing the review rather than approving the accounting entry.]], not the accounting approver. I will pursue the response and preserve the decision with its actual reviewer and approval status.
Hana | Please retain June service beside July 2. A note saying only July invoice would lose the issue.
Alex | I will retain the [[cutoff evidence::Cutoff evidence includes the July 2 document date and June service description needed for the accountant's review.]] together: two hundred forty dollars, July second invoice date, June service. None of those details should disappear in the summary.
Hana | Leave one item open after the handoff. Changing its owner doesn't complete it.
Alex | Correct. The [[open item::Open item remains incomplete after ownership transfers because the accountant's review is still pending.]] stays visible. A change of owner is not a completed review, and nine out of ten must not become ten out of ten just because the handoff is done.
Hana | When the accountant responds, distinguish a period decision, an entry approval, and a request for more evidence.
Alex | I will preserve those distinctions in the [[accountant review::Accountant review must be reported according to its actual outcome, not assumed to include posting approval.]] result. A request for more evidence is not approval, and a period discussion should not be silently expanded into permission to post.
Hana | For now, no adjustment is authorized by this handoff. We just need the actual question and support reviewed.
Alex | Agreed. An [[adjusting entry::Adjusting entry is a possible accounting action requiring the relevant review and approval, not something authorized by this handoff.]] has not been approved, so the handoff should not describe one as ready or already recorded. I will keep that limit attached to the item.
Hana | Readback: nine complete, one open; $240 July 2 invoice for June service; accountant review pending; you follow up from noon.
Alex | That is accurate. The [[handover time::Handover time is noon, when follow-up responsibility passes to Alex without completing or approving the open item.]] changes who pursues the response, not the unresolved accounting status. I will take the follow-up with all those facts intact.''',
    rehearsal=["Complete the period-close handoff.","Read $240, July 2 invoice date, June service, accountant review pending, and Alex taking follow-up at noon. Then read the unapproved-entry status.","Complete the transfer and check the key. Keep nine complete and one open even after the handoff."],
    transfer_title='Hand over the period question without closing it',
    transfer_setup='Complete the close handoff with the amount, service period, review owner, and open status preserved.',
    transfer='''Bookkeeper: "The maintenance invoice is for ___ dollars." | 240 | Two hundred forty is the stated amount of the invoice awaiting period review.
Colleague: "Its description refers to ___ service." | June | June is the service period, despite the July 2 document date.
Bookkeeper: "The ___ must review the posting period." | accountant | Accountant is the required reviewer, not automatically the follow-up owner.
Colleague: "One checklist item remains ___." | open | Open preserves the unfinished review even after Alex takes responsibility for follow-up.'''
))


BOOK['units'].append(unit(
    title='Correcting records while preserving the trail',
    scene='A duplicate entry, not a recovered payment',
    skill='Correct an overstatement by distinguishing a confirmed tracker duplication from unposted ledger changes and unproven cash movements.',
    brief='In fictional tracker version 3, invoice J14 for $180 appears twice because the same file was imported twice. The controller has confirmed one duplicate entry. No ledger correction has been posted. A previous message wrongly said the duplicate payment had been recovered, but no duplicate payment is established. Bookkeeper Rosa must correct the message with controller Ellis and preserve a traceable record of the verified issue and any later authorized change.',
    cast='Rosa | Bookkeeper\nEllis | Controller',
    culture=('Correct the strongest false claim, not just the smallest number', 'Changing a tracker count does not repair a message claiming that money was recovered. Name the earlier statement, withdraw it, and replace it with the verified finding. Preserve the distinction between a file import, a ledger posting, and a cash transaction.'),
    a='''What has the controller confirmed? | One duplicate tracker entry for J14 | Two actual supplier payments | A recovered $180 payment | A completed ledger correction | The verified issue is a duplicate entry caused by importing the same file twice.
What is the current ledger-correction status? | No correction has been posted | A correction is fully posted | A refund automatically changed the ledger | The ledger was deleted | The supplied facts explicitly state that no ledger correction has been posted.
Which earlier claim is wrong? | The duplicate payment had been recovered | J14 is for $180 | Tracker version 3 contains a duplicate | The same file was imported twice | No duplicate payment is established, so the recovery statement is unsupported.''',
    vocabulary='''tracker | Working record used to monitor items or statuses. | identify the tracker
tracker version | Number or label distinguishing a revision of the working record. | specify tracker version
duplicate entry | Repeated record of the same underlying item. | confirm a duplicate entry
duplicate import | Repeated loading of the same source file or data. | identify a duplicate import
source file | Original file from which data were loaded. | preserve the source file
import log | Record of data-loading events and their status. | consult the import log
controller | Person overseeing the relevant accounting controls and reporting. | obtain controller confirmation
verified finding | Conclusion supported by the stated review. | report the verified finding
ledger correction | Authorized change to the accounting record. | distinguish a ledger correction
posted correction | Change actually entered in the ledger through the relevant process. | verify a posted correction
duplicate payment | Actual payment made more than once for the same obligation. | distinguish a duplicate payment
payment recovery | Return or recovery of money previously paid. | verify payment recovery
cash movement | Actual transfer of money into or out of an account. | confirm cash movement
status correction | Amendment of an inaccurate progress or outcome statement. | issue a status correction
retraction | Explicit withdrawal of a previous unsupported claim. | make a precise retraction
correction trail | Record linking the original issue, evidence, and authorized change. | preserve the correction trail
record retention | Keeping information under the applicable requirements and process. | follow record-retention procedures
change authorization | Permission for a specified amendment. | obtain change authorization
transaction reference | Identifier connecting records to the relevant business item. | retain the transaction reference
working total | Sum calculated from a working record rather than a verified final ledger. | qualify a working total
overstatement | Claim or figure that exceeds what the evidence supports. | correct an overstatement
cross-reference | Link between related records or messages. | include a cross-reference
correction owner | Person responsible for carrying out the approved amendment. | identify the correction owner
resolution evidence | Information demonstrating that the specific issue has been resolved. | request resolution evidence''',
    precision='J14 is a $180 invoice shown twice in tracker version 3 because the same file was imported twice. Two displayed entries would total $360, with one extra $180 entry. That tracker arithmetic does not establish two payments, a $180 cash loss, or a recovery.',
    precision_extra='The controller confirmed one duplicate entry, but no ledger correction has been posted. Withdraw the earlier recovery claim explicitly. Preserve the original reference, verified finding, and later authorized correction trail; do not silently erase the history or invent a cash transaction.',
    phrases='''Identify the record | This concerns tracker version 3 and invoice J14.
State the invoice amount | J14 is for $180.
Describe the duplication | The same file was imported twice.
Name the verified finding | The controller confirmed one duplicate entry.
Keep tracker and ledger separate | A tracker duplicate is not automatically a posted ledger duplicate.
State posting status | No ledger correction has been posted.
Separate record and payment | A repeated entry does not prove a repeated payment.
Own the earlier error | My previous message said the duplicate payment had been recovered.
Retract the claim | That recovery statement was unsupported and is withdrawn.
State the evidence limit | No duplicate payment has been established.
Avoid invented cash movement | We have not confirmed any recovered funds.
Preserve the trail | Keep the original record and correction history linked.
Request authorization | Any amendment needs the appropriate approval.
Make the correction visible | I will send an explicit correction to the earlier recipients.
Report only the actual stage | The duplicate entry is confirmed; the ledger correction is not posted.
Close with a precise status | One tracker duplicate, no established duplicate payment, no posted ledger correction.''',
    notes='''Appears twice | Describes the working record without asserting two underlying transactions.
Confirmed one duplicate | Specifies the verified issue and count.
Not automatically | Blocks an unsupported inference between different systems or stages.
Was unsupported and is withdrawn | Corrects the earlier claim explicitly.
No ... established | Limits the evidence without inventing a contrary event.
Keep ... linked | Preserves traceability between the issue and its correction.''',
    d='''Which correction is accurate? | One J14 tracker duplicate is confirmed; no duplicate payment or recovery is established | We recovered a second $180 payment | The ledger is already corrected | Two tracker rows prove two bank transfers | The statement preserves the verified record issue and withdraws the unsupported cash claim.
What does twice $180 establish here? | The duplicate tracker rows sum to $360 | The supplier received $360 | The bank refunded $180 | A final ledger balance is $360 | The calculation concerns two working-record entries, not proven payment or ledger events.
Which action preserves the trail? | Link the explicit correction to the original message and supporting records | Erase every trace of the earlier claim | Invent a refund receipt | Mark the ledger correction posted without evidence | A traceable correction retains the connection between the error, evidence, and authorized amendment.
Which status remains uncompleted? | Ledger correction posting | Controller confirmation of the duplicate | Identification of J14 | Recognition that the file was imported twice | The supplied facts confirm the duplicate but explicitly leave ledger correction unposted.''',
    dialogue='''Rosa | Ellis, my J14 update said a duplicate payment had been recovered. I need to withdraw that: the evidence only establishes a repeated tracker entry.
Ellis | That's right. The [[verified finding::Verified finding is one duplicate J14 entry in tracker version 3, not a recovered payment.]] is one duplicate J14 entry in tracker version 3 because the same file was imported twice.
Rosa | It's a $180 invoice showing twice. I jumped from two rows to two payments, which wasn't justified.
Ellis | A [[duplicate entry::Duplicate entry is a repeated record of J14 and does not prove a second actual payment.]] isn't proof of another payment. The correction needs to address that cash claim, not merely change the number of rows.
Rosa | The two rows sum to $360 in the tracker. That doesn't show $360 leaving the bank.
Ellis | Correct. It's a [[working total::Working total is the sum of the duplicate tracker rows, not a verified cash or ledger balance.]] from the duplicated rows, not a verified bank or ledger balance. The extra $180 displayed isn't an established cash loss.
Rosa | No ledger change has been posted either. I shouldn't say the accounts are fixed because you've identified the import problem.
Ellis | Exactly. A [[posted correction::Posted correction would be an actual ledger change, and none has occurred in the supplied status.]] hasn't occurred. Confirming the issue, authorizing a change, and posting it are different stages.
Rosa | I'll send the same recipients a correction. How do I make sure the recovery claim doesn't remain the headline?
Ellis | Lead with a direct [[retraction::Retraction explicitly withdraws the unsupported claim that a duplicate payment was recovered.]]: the statement that a duplicate payment was recovered was unsupported and is withdrawn. Then state the verified finding.
Rosa | One duplicate J14 entry in version 3, same source file imported twice, and no duplicate payment established.
Ellis | Yes. Don't imply a [[payment recovery::Payment recovery would require evidence that money was returned, which is not established here.]] either. Without evidence of a duplicate payment, we can't report recovered funds as an accomplished result.
Rosa | Should I remove the original message so nobody relies on it later?
Ellis | Preserve the [[correction trail::Correction trail links the original false statement, explicit correction, and evidence rather than silently erasing history.]] through the actual records process. Link the explicit correction to the earlier message so readers can see what replaces the false claim.
Rosa | The source file and import information should remain available too, rather than disappearing during a tracker cleanup.
Ellis | Correct. The [[import log::Import log can support the confirmed repeated file import and should remain connected to the review.]] helps support how the duplication happened. Keep it connected to the review and any authorized amendment.
Rosa | Sending this correction doesn't give me permission to alter the ledger, so I'll keep those actions separate.
Ellis | Yes. [[Change authorization::Change authorization is required for the actual amendment and is not created by correcting a message.]] must cover the specific amendment. A corrected message doesn't approve or post an accounting entry.
Rosa | My final wording will say one confirmed tracker duplicate, no established duplicate payment or recovery, and no ledger correction posted.
Ellis | That's the accurate [[status correction::Status correction replaces the unsupported recovery claim with the verified duplicate-entry finding and unresolved ledger status.]]. Retain J14, version 3, and the supporting record, then report later resolution only when its evidence exists.''',
    rehearsal=["Complete the tracker-correction dialogue.","Read Rosa's retraction and the replacement finding aloud. Distinguish two $180 tracker rows from actual payments or recovered funds.","Complete the transfer and check the key. Repeat the status with no posted ledger correction and the original references retained."],
    transfer_title='Retract the unsupported recovery claim',
    transfer_setup='Complete the corrected status message. Distinguish the tracker, invoice amount, and unproven payment claim.',
    transfer='''Bookkeeper: "The invoice reference is ___." | J14 | J14 identifies the invoice duplicated in tracker version 3.
Controller: "The invoice amount is ___ dollars." | 180 | One hundred eighty is the invoice amount, not a proven recovered payment.
Bookkeeper: "One duplicate tracker ___ is confirmed." | entry | Entry describes the verified repeated record without asserting a duplicate cash payment.
Controller: "No ledger correction has been ___." | posted | Posted is the accounting stage explicitly not completed in the supplied status.'''
))
