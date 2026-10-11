"""Original learner-book content for banking operations."""
from books.authoring import unit

BOOK = dict(
    slug='banking-operations', title='Banking Operations English',
    cover_label='ENGLISH FOR BANKING OPERATIONS TEAMS',
    cover_title='Banking\nOperations', cover_size=36,
    tagline='Trace the transaction. Explain the status. Protect the record.',
    audience='For account services, payments, lending operations, financial-crime, controls, and complaint teams.',
    map_intro='Eight banking exchanges: complete account-opening checks, describe a monitoring alert, reconcile loan-document versions, report payment exceptions, clarify a disputed transaction, investigate a ledger difference, supply control evidence, and explain a fee review.',
    notes_title='Make each status word earn its place',
    notes_intro='Banking records distinguish requests, reviews, authorizations, postings, and settlements. These conversations practice explaining those stages while protecting confidential information and preserving the actual evidence behind a customer or control decision.',
    field_notes=[
        ('Name the unresolved item', 'A pending application or exception needs a specific reason and next step. Identify the missing document or verification without guessing the facts or promising approval.', '"The ownership information requested for this application remains incomplete."'),
        ('Do not turn an alert into an accusation', 'A monitoring alert starts a review; it does not prove wrongdoing. Describe observed activity and its source, preserve uncertainty, and use authorized confidential channels.', '"The activity differs from the recorded profile; its explanation has not been established."'),
        ('Separate review from resolution', 'Examined, corrected, authorized, released, and settled describe different stages. A reviewed queue item may still require action, and a signed control record may still contain an unresolved exception.', '"Thirty items were reviewed; that does not mean thirty were resolved."'),
        ('Answer the actual customer question', 'Explain the relevant transaction, date, amount, and next contact. Distinguish an interim credit or status update from a final outcome without withholding applicable rights or inventing deadlines.', '"I will check the terms applicable on the transaction date, not assume today\'s schedule settles the charge."')],
    scope_note='All banks, customers, accounts, transactions, figures, and local procedures are fictional. This book teaches professional English, not banking, legal, financial, compliance, or investigation advice. Actual obligations depend on the product, jurisdiction, facts, and current requirements. No exercise authorizes an account opening, fund transfer, record alteration, or disclosure of confidential reporting information.',
    sources=[
        dict(title='Financial Crimes Enforcement Network. Customer Due Diligence Rule FAQs.', url='https://www.fincen.gov/resources/statutes-and-regulations/cdd-rule-faqs', note='Background on customer checks, ownership information, and 2026 account-opening relief. The fictional application uses stated local requirements, not a universal collection rule.', checked='1 October 2026'),
        dict(title='Federal Financial Institutions Examination Council. Suspicious Activity Reporting: Overview.', url='https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04', note='Background on alerts, review, reporting, and confidentiality. The manual flags newer interagency guidance; this book prescribes no filing threshold or investigation procedure.', checked='1 October 2026'),
        dict(title='Consumer Financial Protection Bureau. Electronic Fund Transfers FAQs.', url='https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/electronic-fund-transfers-faqs/', note='Background on U.S. consumer electronic-transfer disputes. The fictional conversation distinguishes intake, investigation, provisional credit, and final decisions without inventing universal deadlines.', checked='1 October 2026'),
        dict(title='Office of the Comptroller of the Currency. Comptroller\'s Handbook: Internal Control.', url='https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/internal-control/pub-ch-internal-control.pdf', note='Background on control design, performance, records, and review. The original reconciliation and examination cases are language exercises, not audit conclusions.', checked='1 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Account Opening and KYC',
    scene='Explain the missing ownership information without promising approval',
    skill='Clarify an account-opening requirement, distinguish ownership from signing authority, and give a useful next step.',
    brief='Application A62 is the first business-account application by Northbank Design at this fictional bank. Its authorized-signatory details are supplied, but the ownership information requested for the applicable customer review is incomplete. Applicant representative Ken asks officer Zoya to open the account immediately and finish the review later. Under the stated local process, this application cannot be approved until the required review is complete. Zoya will provide the specific outstanding-information list through the verified secure channel and arrange a review-status update Thursday at 11:00. Neither complete documents nor that update guarantee approval.',
    cast='Ken | Applicant representative\nZoya | Account-opening officer',
    culture=('Explain the requirement without making a universal legal claim', 'A customer may see repeated information requests as unnecessary. Describe the actual gap in this application and the authorized review route. Do not claim every entity or every additional account has identical requirements, and do not confuse signing authority with ownership.'),
    a='''What is missing from A62? | Requested ownership information | All authorized-signatory details | The applicant's business name | A previously approved payment | The brief supplies signatory details but leaves the requested ownership information incomplete.
What does the local process require before approval here? | Completion of the required review | Only the applicant's urgent request | A promise to provide records later | Automatic acceptance after a status call | The stated process makes review completion a prerequisite for this application, without guaranteeing approval afterward.
What does Thursday at 11:00 represent? | A review-status update | Guaranteed account approval | A funds-transfer deadline | Confirmation that ownership is verified | Zoya promises a status update, not account approval or verification of missing information.''',
    vocabulary='''Know Your Customer (KYC) | Processes used to understand and verify relevant customer information. | complete KYC checks
customer due diligence (CDD) | Assessment of customer identity, relationship purpose, and relevant risk under applicable requirements. | conduct customer due diligence
ownership structure | The arrangement of ownership interests in an entity. | document the ownership structure
legal entity | An organization recognized as a distinct person under applicable law. | identify the legal entity
beneficial owner | An individual meeting the applicable ownership or control definition for the review. | identify the beneficial owner
authorized signatory | A person permitted to act or sign for an account under its mandate. | verify the authorized signatory
Customer Identification Program (CIP) | A U.S. bank program for obtaining and verifying required customer identity information. | follow the Customer Identification Program
control person | An individual meeting the applicable responsibility or control criterion. | identify the control person
account mandate | Instructions defining who may operate an account and under what authority. | review the account mandate
identity verification | Checking identity using the applicable evidence and process. | complete identity verification
documentary verification | Verification using specified documents. | perform documentary verification
non-documentary verification | Verification using appropriate methods other than specified identity documents. | assess non-documentary verification
nature and purpose | The intended role and use of the customer relationship. | establish the nature and purpose
expected activity | The anticipated account use relevant to understanding the relationship. | describe expected activity
customer risk profile | The assessed characteristics relevant to the customer's risk context. | maintain the customer risk profile
source of funds | The origin of money involved in a relationship or transaction. | clarify the source of funds
source of wealth | The origin of a person's or entity's overall accumulated wealth. | distinguish source of wealth
onboarding | The process of establishing a new customer relationship. | coordinate customer onboarding
account application | A request to establish an account with supplied supporting information. | review the account application
outstanding requirement | A requested or applicable condition that has not yet been satisfied. | identify an outstanding requirement
verification status | The current stage of checking relevant information. | report verification status
risk-based procedure | A process calibrated to relevant assessed risks and applicable requirements. | apply a risk-based procedure
exception review | Authorized assessment of a proposed departure from a stated process. | request an exception review
approval authority | The defined power to approve a specified action or relationship. | confirm approval authority''',
    precision='An authorized signatory can operate an account under its mandate without necessarily being its beneficial owner. Supplying signatory details does not automatically answer the ownership question requested in this application.',
    precision_extra='Requirements depend on the entity, relationship, applicable rules, and risk-based procedures. Current U.S. relief can affect repeated beneficial-owner identification at additional account openings. This first-account case does not teach a universal repeat-collection rule.',
    phrases='''Identify the application | We are reviewing business-account application A62.
Name the supplied information | We have the authorized-signatory details.
Name the gap | The requested ownership information remains incomplete.
Separate roles | Signing authority and beneficial ownership are different questions.
State the local condition | This application requires the review to be complete before approval.
Recognize urgency | I understand that you want to begin using the account promptly.
Avoid an override promise | I cannot bypass the required review.
Make the request specific | I will provide the outstanding-information list.
Protect the submission | Use the verified secure channel for the requested records.
Avoid unnecessary repetition | We will identify what remains missing rather than request everything again.
Explain the context | Requirements must be assessed for this customer and application.
Keep stages distinct | Complete documents do not automatically mean approved onboarding.
Check authority | Any exception requires the applicable authorized review.
Give the next contact | We will update the review status Thursday at 11:00.
Limit the commitment | That is an update appointment, not an approval guarantee.
Close constructively | Send the specified information so the relevant review can continue.''',
    notes='''For this application | Restricts a statement to the supplied customer and process.
Authorized to sign | Does not necessarily mean an owner of the entity.
Remains incomplete | Describes information status without accusing the customer.
Before approval | Names a prerequisite, not a guarantee that satisfying it ensures acceptance.
Risk-based | Requires relevant assessment, not arbitrary treatment or a universal checklist.
Verified channel | Protects information without inventing an email address or collection route.''',
    d='''Which explanation is accurate? | We have signatory details, but the requested ownership information is incomplete. | A signatory is always the only beneficial owner. | Urgency proves that review is unnecessary. | Every entity has identical ownership requirements. | The accurate statement distinguishes the information supplied from the separate ownership gap without inventing universal rules.
What can Zoya promise? | A specific missing-information list and a Thursday status update | Guaranteed approval after any document upload | Immediate use before required review | An exception without authorized assessment | Zoya can provide the stated communication steps, but the brief gives no authority to guarantee approval or bypass review.
Which statement improperly generalizes the case? | Every additional account always requires identical new ownership collection. | This is the customer's first account application here. | The local process requires the stated review. | Requirements depend on applicable rules and risk-based procedures. | The case does not establish a universal repeat-collection rule, and current U.S. relief can affect additional-account requirements.
What does a completed information package establish by itself? | Information is supplied for review, not automatic approval. | Every identity is already verified. | Every risk is eliminated. | Account use is authorized without a decision. | Submission, verification, and approval are distinct stages, so completed paperwork alone does not establish acceptance.''',
    rehearsal=['Read turns 1-10, distinguishing signatory details from ownership information.', 'Swap roles for turns 11-20; separate document receipt, verification, and approval.', 'Complete the B14 transfer and check the reference, missing document, owner, and update time.'],
    dialogue='''Ken | We supplied the people authorized to sign. Why is A62 still pending? We need to start using the business account this week.
Zoya | The requested [[ownership structure::Ownership structure identifies ownership interests; permission to sign does not establish those interests.]] information is incomplete. We have the signatory details, but those answer a different question. I will identify the precise outstanding items rather than ask you to resend the entire application.
Ken | Our director can sign for the company. Does identifying her also settle the ownership question?
Zoya | An [[authorized signatory::A signatory can act under the mandate without necessarily meeting the applicable ownership definition.]] is not necessarily a beneficial owner. We need the information relevant to each role under this application's review. One person's signing authority does not establish the full ownership position.
Ken | Could you open the account now? We can promise to send the remaining information later.
Zoya | Under this local process, the required [[customer due diligence::The stated local process requires this customer review before approval; the conversation cannot bypass it.]] review must be complete before this application can be approved. I cannot replace that step with a promise that the information will arrive later.
Ken | Please send a specific list. Our records team needs to know which ownership details are missing and which documents you already hold.
Zoya | I will send the [[outstanding requirement::The outstanding requirement identifies a specific gap, allowing a focused request instead of unnecessary duplication.]] list through the verified secure channel. It will distinguish what we hold from what remains needed. That should help your team provide the relevant records without unnecessary duplication.
Ken | Are these requirements identical for every company and every account? A colleague said the rules had changed for some account openings.
Zoya | They depend on the applicable rules and [[risk-based procedure::A risk-based procedure depends on relevant customer circumstances and requirements, not identical rules for every account.]]. Current requirements and relief must be assessed in context. This is your first business-account application here; I should not generalize its requirements to every additional account or entity.
Ken | The upload screen says complete. Does that mean submitted, verified, or approved? Those would mean different things to my team.
Zoya | The [[verification status::Verification status describes the checks; receiving documents does not establish their verification or approval.]] remains separate from document receipt. Supplying information allows the review to continue. It does not establish that every item has been verified or that the application has been approved.
Ken | Uploading does not mean the account is ready. Who can review a possible exception?
Zoya | Any [[exception review::An exception needs authorized review; urgency or a frontline discussion does not approve a departure.]] must follow the applicable authorized process. I cannot approve a bypass in this conversation. If a relevant question needs escalation, I will route it rather than invent an exception.
Ken | The form also asks how we expect to use the account. That is separate from identifying who owns or signs for the company.
Zoya | Yes. The [[nature and purpose::Nature and purpose describes intended account use, distinct from the customer's ownership and signing authority.]] of the relationship helps establish the relevant customer context. Provide the requested factual description; do not choose an answer merely because you think it will make the review faster.
Ken | When will I hear from you? An accurate pending status would still help our planning.
Zoya | We will update the [[account application::An account application is a request; a status update does not establish that it is approved.]] status Thursday at eleven hundred. That is a communication appointment, not an approval guarantee. We will identify any continuing information gap or review step rather than imply a decision we do not have.
Ken | I will use the verified channel, supply the specified ownership records, and keep the distinction between submission and approval clear internally.
Zoya | Thank you. The eventual decision remains with the relevant [[approval authority::Approval authority identifies the permitted decision-maker; completed paperwork does not replace that person's decision.]]. We can make the process understandable and keep the next contact reliable while preserving the required review and the actual account status.''',
    transfer_title='Clarify another account application',
    transfer_setup='Application B14 has signatory details but lacks the requested ownership chart. Hana will coordinate the review. The next status update is Monday at 10:00; approval is not guaranteed.',
    transfer='''Officer: "The application reference is ___." | B14 | B14 is the specific account-application identifier supplied in this case.
Applicant: "The missing document is the ___." | ownership chart | The brief identifies the ownership chart as missing while signatory details are already supplied.
Officer: "The review coordinator is ___." | Hana | Hana is explicitly responsible for coordinating the stated review.
Applicant: "The next status update is ___." | Monday at 10:00 | Monday at ten is an update appointment, not a guaranteed approval time.'''))


BOOK['units'].append(unit(
    title='AML Monitoring and Suspicious Activity',
    scene='An unusual-activity alert is a question, not a verdict',
    skill='Write a neutral internal handoff and preserve confidential reporting boundaries.',
    brief='Monitoring analyst Sam receives alert T82 because recent transfers differ from the activity recorded in a business customer profile. The transaction records are available, but the business purpose and explanation for the change have not been established. A draft note says the customer is laundering money. Reviewer Aisha asks Sam to replace that conclusion with the observed difference and open questions, then follow the authorized Anti-Money Laundering (AML) review route. No reporting decision is supplied in this case. Suspicious Activity Report (SAR) information and its existence or nonexistence must not be disclosed through unauthorized channels.',
    cast='Sam | Monitoring analyst\nAisha | AML reviewer',
    culture=('Separate a system signal from a human conclusion', 'An alert can feel authoritative because a system produced it. Explain the actual observation and the missing context without treating the signal as proof. Keep the handoff factual and avoid using customer nationality, accent, or unfamiliarity as a substitute for relevant evidence.'),
    a='''What does T82 identify? | Activity differing from the recorded customer profile | A proven money-laundering offense | A completed reporting decision | A confirmed harmless explanation | The alert identifies a difference requiring review, while its explanation remains unestablished.
What is wrong with the draft note? | It states wrongdoing as established without the supporting finding. | It identifies an alert reference. | It preserves uncertainty. | It limits access to authorized reviewers. | The supplied facts do not establish money laundering, so the accusatory conclusion overstates the evidence.
What reporting decision is supplied? | None | A confirmed SAR filing | A confirmed decision never to file | Public disclosure to the customer | The case deliberately provides no reporting decision, and the analyst must not invent one.''',
    vocabulary='''Anti-Money Laundering (AML) | Measures addressing the misuse of financial services to conceal or facilitate illicit funds. | conduct an AML review
Bank Secrecy Act (BSA) | A U.S. framework of financial recordkeeping and reporting requirements. | assess applicable BSA requirements
transaction monitoring | Review of financial activity for patterns requiring attention under the applicable process. | perform transaction monitoring
monitoring alert | A signal identifying activity for further review. | investigate a monitoring alert
customer profile | Recorded information about a customer and the relevant relationship context. | compare the customer profile
observed activity | Transactions or conduct actually recorded or identified. | describe observed activity
business purpose | The commercial reason given or established for activity. | clarify the business purpose
unusual activity | Activity differing from an expected or relevant pattern and requiring context. | assess unusual activity
suspicious activity | Activity meeting the relevant concern or reporting assessment under applicable requirements. | evaluate suspicious activity
Suspicious Activity Report (SAR) | A confidential report made under applicable suspicious-activity reporting requirements. | protect SAR confidentiality
alert disposition | The recorded outcome of an alert review. | document the alert disposition
case escalation | Referral of a matter to the appropriate review level. | coordinate case escalation
supporting records | Documents or data relevant to assessing the observed activity. | preserve supporting records
transaction narrative | A clear description of relevant transaction facts and context. | prepare a transaction narrative
source attribution | Identification of where information came from. | retain source attribution
risk indicator | Information potentially relevant to assessing a concern. | evaluate a risk indicator
contextual information | Background needed to interpret the observed facts. | obtain contextual information
corroborating evidence | Additional information supporting or challenging an interpretation. | review corroborating evidence
review rationale | The documented reasoning for an assessment or next step. | explain the review rationale
reporting decision | A determination under the applicable process about required reporting. | distinguish the reporting decision
confidentiality restriction | A limit on access or disclosure of protected information. | observe confidentiality restrictions
authorized channel | An approved route for transmitting relevant information. | use an authorized channel
need-to-know basis | Access limited to those requiring information for an authorized role. | share on a need-to-know basis
neutral description | Factual wording without an unsupported adverse or favorable conclusion. | use a neutral description''',
    precision='An alert is not proof of criminal conduct and does not itself establish a reporting decision. A review can preserve concern without asserting wrongdoing or assuming that the activity has an innocent explanation.',
    precision_extra='SAR confidentiality includes information revealing whether a SAR exists. Do not disclose filing or nonfiling status to customers or unauthorized recipients. Use the applicable authorized channels and current requirements; this exercise teaches no filing threshold.',
    phrases='''Identify the item | We are reviewing monitoring alert T82.
Describe the observation | The transfers differ from the activity recorded in the customer profile.
Name the missing context | The business purpose has not been established.
Remove the unsupported finding | Do not describe money laundering as proven.
Preserve the concern | The difference still requires review.
Avoid premature reassurance | We have not established a harmless explanation either.
Link the evidence | Attach the relevant transaction references through the authorized channel.
Attribute the source | Separate system records from unverified explanations.
Keep the note neutral | Describe the observed activity and open questions.
Use the review route | Escalate through the applicable AML process.
Separate reporting | An alert review is not itself a reporting decision.
Protect confidentiality | Do not disclose SAR information through unauthorized channels.
Restrict distribution | Share the handoff only on a need-to-know basis.
Avoid an irrelevant proxy | An accent or nationality is not evidence of wrongdoing.
Record the rationale | Explain why the matter needs further context.
Close the handoff | Keep facts, uncertainty, review action, and reporting status distinct.''',
    notes='''Differs from | Reports a comparison without supplying its cause.
Has not been established | Preserves an unanswered question.
Proven | Requires evidence beyond the existence of an alert.
Neither conclusion | Avoids both unsupported accusation and unsupported clearance.
Whether a report exists | Information that can itself be confidential.
Relevant evidence | Refers to the activity and context, not a demographic shortcut.''',
    d='''Which internal note fits the case? | T82 identifies transfers differing from the profile; business purpose unestablished; referred for authorized review. | The customer is proven to be laundering money. | The alert is harmless because the customer sounded polite. | A SAR has been filed because an alert exists. | The appropriate note describes the observed difference, missing context, and review action without inventing a finding or report.
What should the reviewer not use as proof? | The customer's accent or nationality | Relevant transaction records | Verified account context | Documented business-purpose evidence | Accent or nationality is not evidence that the observed transactions constitute wrongdoing.
Which disclosure is inappropriate through an unauthorized channel? | Whether a SAR exists for the customer | The assigned internal alert reference to its authorized reviewer | Relevant records sent through the approved review route | A neutral handoff within the permitted team | Information revealing SAR existence or nonexistence is confidential and must not be disclosed through unauthorized channels.
What should the record preserve? | Sources, observed facts, uncertainty, and the review rationale | The alert score alone without the profile comparison | The transaction totals without their dates or sources | The reviewer's preferred explanation without its verification status | The complete record links evidence to the review question instead of substituting a score, partial summary, or assumption.''',
    rehearsal=['Read turns 1-10; replace the accusation with the observed profile difference.', 'Swap roles for turns 11-20, maintaining the confidential-reporting boundary.', 'Complete the U19 transfer and check the alert, unknown purpose, reviewer, and decision status.'],
    dialogue='''Sam | Alert T82 shows transfers that differ from the recorded customer profile. My draft says the customer is laundering money, but the explanation is still unknown.
Aisha | Use a [[neutral description::A neutral description records the observed difference without converting an unresolved concern into a proven offense.]]. The alert identifies a difference requiring review. It does not establish wrongdoing, and our note should not supply a conclusion that the available evidence has not established.
Sam | I can identify the relevant transactions and the profile used for comparison. I cannot yet explain the business reason for the change.
Aisha | State that the [[business purpose::Business purpose is the relevant explanation for the activity; it remains unestablished rather than necessarily absent or illicit.]] has not been established. That is different from saying no legitimate purpose exists. We need context, not an accusation based on an empty explanatory field.
Sam | If I remove the accusation, how do I make clear that the concern still needs review?
Aisha | Preserve the [[unusual activity::Unusual activity differs from the relevant pattern and requires evaluation; it is neither automatic wrongdoing nor automatic clearance.]] concern without choosing either outcome. Neutral wording can be precise about why review is needed while leaving the explanation open. It does not require us to pretend the difference is irrelevant.
Sam | The transaction records and profile are available. Any explanation we receive later should be distinguished from what the system already records.
Aisha | Maintain [[source attribution::Source attribution distinguishes records from statements or assumptions, allowing reviewers to assess each item's basis.]] for each item. Separate recorded transactions, customer information, and unverified explanations. Otherwise, a later reader may mistake an assertion or assumption for a fact established by the original records.
Sam | I will send the factual handoff to the authorized AML reviewer. Does the existence of an alert itself mean a report has been filed?
Aisha | No. A [[reporting decision::A reporting decision follows the applicable assessment process; the existence of a monitoring alert does not establish one.]] is separate from an alert. No reporting decision is recorded in this handoff. Do not infer filing or nonfiling status from the presence of T82 or from this review conversation.
Sam | An unrelated colleague asked whether a SAR exists. Bank employment alone does not authorize that disclosure.
Aisha | Correct. Observe the [[confidentiality restriction::The confidentiality restriction protects SAR information, including existence or nonexistence, from unauthorized disclosure.]] on SAR information, including whether a report exists. Employment alone does not create permission. Use the applicable authorized process for any request involving protected reporting information.
Sam | The customer-facing team may still need help with an ordinary service question. We should not put reporting information into a general customer note.
Aisha | Keep protected information in the appropriate [[authorized channel::An authorized channel limits information to the permitted review route rather than a broadly visible service note.]]. Customer communication must follow its authorized process without revealing confidential reporting information. Do not use a convenient shared field as a shortcut around access restrictions.
Sam | The handoff should say why we need another review. I can name the profile difference and the missing business-purpose explanation.
Aisha | Document the [[review rationale::The review rationale explains the evidence-based reason for further assessment without substituting a label for analysis.]]. Tie it to relevant activity and missing context, not the customer's accent, nationality, or an impression of their personality. Those are not substitutes for evidence of wrongdoing.
Sam | I will list the alert, records, profile comparison, sources, and unresolved explanation, without asserting a criminal finding.
Aisha | That supports [[case escalation::Case escalation routes the concern to the proper review level; it is an action rather than an established adverse finding.]] through the approved process. Make clear what you observed and what assessment is still needed. Referral status must not be presented as an outcome that has already been reached.
Sam | When the authorized review is complete, its actual result can be recorded with the supporting rationale and the appropriate confidentiality controls.
Aisha | Yes. The [[alert disposition::Alert disposition records the actual review outcome; it must not be guessed while assessment remains incomplete.]] must reflect the completed assessment, not a guess made to clear the queue. Keep the evidence, review stage, and any protected reporting information distinct throughout the record.''',
    transfer_title='Complete a neutral alert handoff',
    transfer_setup='Alert U19 identifies activity differing from a recorded profile. Its business purpose is unconfirmed. Noor owns the authorized review. No reporting decision is supplied.',
    transfer='''Analyst: "The alert reference is ___." | U19 | U19 is the specific monitoring-alert identifier supplied in the case.
Reviewer: "The business purpose remains ___." | unconfirmed | The brief does not establish the explanation for the changed activity.
Analyst: "The assigned reviewer is ___." | Noor | Noor is explicitly responsible for the authorized review.
Reviewer: "This alert alone does not establish a reporting ___." | decision | An alert does not establish a reporting decision, and none is supplied here.'''))


BOOK['units'].append(unit(
    title='Loan Operations and Documentation',
    scene='A checked condition points to the wrong agreement version',
    skill='Escalate a document mismatch without silently changing the evidence or authorizing a drawdown.',
    brief='Loan package L73 uses approved agreement version 3. The operations checklist marks condition C4 complete, but the attached supporting certificate refers to agreement version 2. The team has not established whether that certificate satisfies C4 for version 3. Operations officer Ravi and documentation reviewer Mae must correct the status and obtain an authorized assessment. Under the stated local process, the affected drawdown is not authorized while this condition remains unresolved. The mismatch alone does not prove that the entire loan is invalid. Neither participant may edit the certificate reference or mark the condition satisfied merely to meet a requested funding date.',
    cast='Ravi | Loan operations officer\nMae | Documentation reviewer',
    culture=('A precise challenge can protect the working relationship', 'A checked box can be mistaken for an established fact, especially near a funding deadline. Identify the exact reference mismatch and its consequence for the current task. Challenge the evidence politely without accusing the preparer or claiming a wider legal conclusion.'),
    a='''Which agreement version governs this package? | Approved version 3 | Version 2 because it appears on the certificate | Both versions interchangeably until funding | Whichever version was attached most recently | The brief identifies approved version 3; an attachment, upload order, or unassessed similarity cannot change that status.
What does the supporting certificate reference? | Version 2 | Version 3 | Every agreement ever issued | No agreement at all | The certificate references version 2, creating the unresolved mismatch with version 3.
What is the affected drawdown status under the stated process? | Not authorized while C4 remains unresolved | Automatically authorized by the checked box | Already paid in full | Permanently cancelled by this conversation | The local process leaves the affected drawdown unauthorized pending resolution of the specific condition.''',
    vocabulary='''loan facility | An agreed arrangement providing borrowing subject to specified terms. | administer a loan facility
loan agreement | The contract establishing the borrowing terms and obligations. | review the loan agreement
drawdown | Use or disbursement of funds under a loan facility. | authorize a drawdown
condition precedent | A condition that must be satisfied or appropriately waived before a specified action. | verify a condition precedent
supporting certificate | A document certifying specified information relevant to a requirement. | examine a supporting certificate
approved version | The document issue authorized for the relevant purpose. | identify the approved version
document discrepancy | A mismatch between documents or their references. | record a document discrepancy
execution copy | The version prepared or used for formal signing. | confirm the execution copy
executed document | A document signed or otherwise completed as required for its execution. | retain the executed document
amendment | A documented change to an existing agreement. | review an amendment
waiver | An authorized relinquishment or modification of a requirement under applicable terms. | confirm a waiver
consent | Permission given by the relevant party for a specified action. | obtain the required consent
covenant | A contractual undertaking or restriction. | monitor a covenant
security document | A document establishing or recording relevant collateral rights. | verify the security document
collateral | Property or rights supporting repayment under an agreed arrangement. | identify the collateral
guarantor | A party undertaking specified obligations relating to another party's debt. | confirm the guarantor
facility agent | A party coordinating specified administrative functions under a facility agreement. | contact the facility agent
conditions checklist | A record tracking requirements and their evidence or status. | update the conditions checklist
document index | A list linking required documents to their identifiers and locations. | maintain the document index
version control | Management of document issues and their applicable status. | maintain version control
exception log | A record of unresolved departures or discrepancies. | update the exception log
funding request | A request for a loan disbursement under the applicable arrangement. | review the funding request
release authorization | Approval allowing a specified disbursement or action to proceed. | verify release authorization
document retention | Preservation of records under the relevant requirements. | follow document-retention requirements''',
    precision='The certificate mismatch leaves C4 unresolved; it does not automatically invalidate the entire facility. Satisfaction, waiver, and release authorization are different decisions, each requiring its applicable authority and evidence.',
    precision_extra='A requested funding date does not correct a document reference or authorize disbursement. Preserve the original certificate and obtain the required assessment. Do not silently replace version 2 with version 3 in the evidence.',
    phrases='''Name the package | We are reviewing loan package L73.
Identify the approved issue | The package uses agreement version 3.
State the conflicting reference | The certificate refers to version 2.
Locate the affected condition | The mismatch concerns condition C4.
Correct the checklist | C4 should not be marked complete on this evidence alone.
Preserve the document | Do not edit the certificate reference.
Limit the conclusion | This mismatch does not by itself invalidate the whole loan.
Request authorized review | Please assess whether the certificate satisfies C4 for version 3.
Keep funding status explicit | The affected drawdown is not authorized while the condition remains unresolved.
Distinguish a waiver | A request to overlook the issue is not an approved waiver.
Respect the deadline without inventing authority | I understand the requested funding date, but the evidence still needs review.
Link the references | Record the package, condition, and both version identifiers.
Avoid assumed equivalence | Similar wording does not prove that the documents are interchangeable.
Keep the next action clear | Obtain the relevant documentation decision through the authorized route.
Track the exception | Leave the discrepancy visible until its actual resolution is recorded.
Close the handoff | Report the reviewed evidence and authorization status separately.''',
    notes='''Refers to | Reports the actual document reference without deciding its legal effect.
Should not be marked complete | Challenges a status unsupported by the supplied evidence.
By itself | Limits the conclusion that follows from one observed mismatch.
Satisfied versus waived | Meeting a condition differs from an authorized decision to waive it.
Requested funding | A desired disbursement time, not evidence of permission.
Separately | Prevents document review from being mistaken for release authorization.''',
    d='''Which checklist correction is supported? | Mark C4 unresolved pending authorized assessment of the version mismatch. | Change the certificate text without recording it. | Mark every loan condition permanently invalid. | Leave C4 complete because funding is urgent. | The evidence does not yet establish C4 satisfaction for version 3, so the specific condition requires review.
Which statement invents a waiver? | The client wants funding today, so C4 is waived. | The certificate refers to version 2. | The approved agreement is version 3. | An authorized assessment is required. | A requested funding date does not supply the authority or decision needed to waive a condition.
What should happen to the original certificate? | Preserve it with its actual reference and obtain the necessary assessment. | Silently replace its version number. | Delete it so the mismatch cannot be seen. | Treat it as proof of every other condition. | The original is evidence and must remain traceable while the mismatch is assessed.
What does resolving a document question not automatically establish? | A separate release authorization unless the applicable process provides it | The value of identifying correct versions | The need to record the decision | The existence of the original mismatch | Document satisfaction and funding authorization are distinct matters under the stated process and must not be conflated.''',
    rehearsal=['Read turns 1-10, naming L73, C4, and the two different version references.', 'Swap roles for turns 11-20; distinguish satisfaction, waiver, and release authorization.', 'Complete the N26 transfer and verify each document and condition reference.'],
    dialogue='''Ravi | C4 is checked complete in L73, but its certificate refers to agreement version 2. The approved package uses version 3.
Mae | Record the [[document discrepancy::The document discrepancy is the observed mismatch between the certificate and approved agreement, not a conclusion about the entire loan's validity.]]. We have not established whether that certificate satisfies C4 for version 3. A completed checkbox does not remove the conflicting reference or supply the missing assessment.
Ravi | C4 may be unchanged, but I have not checked. Who can assess whether this certificate still satisfies it?
Mae | That needs authorized review of the [[condition precedent::The condition precedent is the requirement relevant to the proposed action; its satisfaction must be assessed against the applicable agreement.]] and supporting evidence. Similar wording is not enough for us to declare satisfaction. Equally, the mismatch alone does not prove that the whole facility is invalid.
Ravi | The team wants funding today. Can I change the certificate's version number to match?
Mae | Preserve the [[supporting certificate::The supporting certificate is evidence with an actual reference; silently changing it would conceal the mismatch instead of resolving it.]] as received. Do not edit its reference to make the checklist look consistent. We need the relevant assessment and any properly issued replacement or other authorized resolution.
Ravi | I will correct the checklist status and note the exact package and condition. The requested funding date will remain a request, not an authorization.
Mae | Keep the [[drawdown::Drawdown is the use or disbursement of facility funds; it remains unauthorized under the stated process while C4 is unresolved.]] status explicit. Under this local process, the affected drawdown is not authorized while C4 remains unresolved. A deadline does not establish permission to release the funds.
Ravi | Someone suggested calling the issue waived because the client agrees to provide another certificate later. That does not sound like an authorized decision.
Mae | It is not an established [[waiver::A waiver requires the applicable authority and decision; a client's promise or operational preference does not establish one.]]. Satisfaction and waiver are different concepts, and each needs its proper basis. We cannot convert the client's proposal into an approved waiver merely by changing the label.
Ravi | I will send the document references to the appropriate reviewer. We should keep both versions available so the question can be assessed accurately.
Mae | Maintain [[version control::Version control preserves which document issue applies and prevents a prior version from being silently treated as the approved one.]]. Identify version 3 as the approved agreement and version 2 as the certificate's reference. That distinction lets the reviewer understand the actual issue instead of guessing which document we meant.
Ravi | I will flag C4 rather than mark the entire facility defective. We have identified one reference mismatch, not reviewed every document.
Mae | Use the [[exception log::The exception log records the specific unresolved discrepancy and its status, not an unsupported conclusion about every loan document.]] to identify C4 and the pending assessment. Keep the scope precise. We have a document-reference question affecting a condition, not evidence that every part of the facility is defective.
Ravi | Once the reviewer decides what is needed, I will link that decision to the evidence. I will not remove the old certificate from the record.
Mae | Update the [[document index::The document index links the condition, relevant records, and decision while preserving the original evidence and its history.]] so the decision and supporting material are traceable. If a replacement is issued, its identity and status need to be clear without erasing the document that prompted the question.
Ravi | Would satisfying or appropriately waiving C4 automatically authorize release of the funds?
Mae | Check the separate [[release authorization::Release authorization permits the disbursement; resolving one document condition does not automatically supply every remaining approval.]] requirements. Resolving this condition does not automatically establish every other required approval. Report the document decision and funding status separately so nobody infers permission from a narrower update.
Ravi | My handoff will show L73, C4, approved version 3, the certificate's version 2 reference, the unresolved status, and the authorized review request.
Mae | Good. Keep the [[funding request::The funding request expresses the desired disbursement; it remains distinct from the evidence review and actual authority to release funds.]] visible as well, but do not let its urgency replace the evidence. The next team needs the actual condition and authorization status, not a reassuring checkbox unsupported by the record.''',
    transfer_title='Identify another document mismatch',
    transfer_setup='Package N26 uses approved agreement version 5. The certificate supporting condition D2 refers to version 4. Satisfaction is unresolved, and the affected drawdown is not authorized under the stated process.',
    transfer='''Officer: "The package reference is ___." | N26 | N26 is the package identifier given for this separate documentation case.
Reviewer: "The approved agreement version is ___." | 5 | Version 5 is the approved agreement, not the older certificate reference.
Officer: "The certificate refers to version ___." | 4 | Version 4 is the actual reference on the supporting certificate.
Reviewer: "The affected condition is ___." | D2 | D2 is the condition whose satisfaction remains unresolved because of the mismatch.'''))


BOOK['units'].append(unit(
    title='Payment Operations and Exceptions',
    scene='Reviewed is not the same as resolved',
    skill='Give a payments-queue handoff with reconciled counts, clear stage labels, and no unsupported settlement claim.',
    brief='At 10:00 local time, a fixed queue snapshot contains 45 payment exceptions. Thirty have been reviewed: 24 are resolved under the queue process, and six await the required authorization. Fifteen have not yet been reviewed. There are no other categories in this snapshot. Supervisor Bea asks analyst Colin whether all items are resolved. Colin must report 24 resolved and 21 still open, while distinguishing the review rate from the resolution rate. A resolved queue exception does not itself confirm that the underlying payment has settled. The team will provide another status snapshot at 11:00; resolution of every item is not promised.',
    cast='Bea | Payments supervisor\nColin | Payments analyst',
    culture=('Give the denominator with the good news', 'A busy manager may hear thirty reviewed as thirty finished. State the full population and the mutually exclusive status groups. Recognize completed review work without letting a positive headline hide items that still need authorization or examination.'),
    a='''How many exceptions are resolved? | 24 | 30 | 45 | 15 | Only twenty-four reviewed items are resolved; the other six reviewed items still await authorization.
How many exceptions remain open? | 21 | 15 | 6 | 30 | Six reviewed but unresolved items plus fifteen unreviewed items give twenty-one open exceptions.
What does 11:00 represent? | The next queue snapshot | Guaranteed settlement of every payment | Automatic authorization for six items | A promise that every exception is resolved | Eleven hundred is the next status report, not a guarantee of resolution, authorization, or settlement.''',
    vocabulary='''payment instruction | A request specifying a transfer of funds. | validate a payment instruction
payment rail | The system or network through which a payment is processed. | identify the payment rail
Automated Clearing House (ACH) | A network supporting specified electronic credit and debit transfers. | process an ACH payment
wire transfer | A funds transfer through the relevant wire-payment system. | track a wire transfer
real-time gross settlement (RTGS) | Settlement of individual transfers in real time under the relevant system. | distinguish RTGS processing
payment exception | An item requiring attention outside the normal processing path. | investigate a payment exception
exception queue | A collection of payment items awaiting specified review or action. | monitor the exception queue
queue snapshot | The queue's recorded status at a particular time. | timestamp the queue snapshot
reviewed item | An item examined under the review process, possibly still unresolved. | count reviewed items
resolved exception | An exception meeting the queue's defined resolution condition. | record a resolved exception
pending authorization | A state awaiting required approval. | identify pending authorization
unreviewed item | An item not yet examined under the stated process. | prioritize unreviewed items
originator | The party initiating the payment under the relevant arrangement. | identify the originator
beneficiary | The intended recipient of a payment. | verify beneficiary details
routing information | Details directing the payment through the relevant institutions or system. | validate routing information
value date | The date used for value or funds treatment under the relevant payment arrangement. | confirm the value date
cut-off time | A deadline for a specified processing cycle or service. | verify the cut-off time
payment release | The authorized sending of a payment to its next processing stage. | confirm payment release
settlement | The discharge of the payment obligation through the relevant system. | verify settlement status
return | A payment sent back under the applicable process. | investigate a payment return
repair | Correction of a payment instruction through authorized procedures. | route a payment repair
duplicate payment | A payment instruction or execution repeating another unintentionally or without the intended basis. | review a possible duplicate payment
resolution rate | The proportion of the defined population meeting the resolution condition. | calculate the resolution rate
review rate | The proportion of the defined population examined under the review process. | calculate the review rate''',
    precision='Thirty reviewed out of 45 is approximately 66.7%; 24 resolved out of 45 is approximately 53.3%. The difference is six reviewed items awaiting authorization. Open items total 21, not just the 15 unreviewed.',
    precision_extra='Resolved describes the queue exception under its stated process. It does not automatically mean released, received, or settled. Different payment rails and states require their actual evidence; this snapshot supplies no settlement confirmation.',
    phrases='''Timestamp the report | This is the queue snapshot at 10:00 local time.
Give the population | There are 45 exceptions in this snapshot.
State completed review | Thirty items have been reviewed.
Separate the resolved group | Twenty-four are resolved under the queue process.
Name the remaining reviewed items | Six reviewed items await authorization.
State the unreviewed group | Fifteen have not yet been reviewed.
Reconcile the open count | Twenty-one exceptions remain open.
Explain the arithmetic | Six awaiting authorization plus fifteen unreviewed equals twenty-one.
Report the review rate | The review rate is approximately 66.7%.
Report the resolution rate | The resolution rate is approximately 53.3%.
Avoid a settlement claim | Queue resolution does not confirm payment settlement.
Keep authority explicit | The six items still require the relevant authorization.
Avoid silent relabeling | Do not count reviewed items as resolved.
Give the next contact | The next snapshot will be provided at 11:00.
Limit the commitment | That is a reporting time, not a promise to resolve every item.
Close the handoff | Keep the counts and stage labels attached to the same timestamp.''',
    notes='''Of the thirty | Makes clear that resolved and awaiting-authorization groups are subsets of reviewed items.
Still open | Includes more than the unreviewed portion of the queue.
At 10:00 | Restricts a count to its snapshot rather than a changing live total.
Approximately | Signals rounding of the stated ratios.
Resolved under the process | Does not silently claim downstream settlement.
Next snapshot | Promises refreshed information, not completed processing.''',
    d='''Which breakdown reconciles to 45? | 24 resolved, six awaiting authorization, fifteen unreviewed | 30 resolved, six awaiting authorization, fifteen unreviewed | 24 resolved and fifteen open, with six omitted | 45 resolved and fifteen unreviewed | The mutually exclusive groups sum to forty-five without double-counting the reviewed subset.
Which rate is approximately 66.7%? | Review rate | Resolution rate | Settlement rate | Return rate | Thirty reviewed divided by forty-five total exceptions gives approximately sixty-six point seven percent.
Which statement improperly strengthens the evidence? | All 24 underlying payments have settled because their exceptions are resolved. | Twenty-four exceptions are resolved. | Six reviewed exceptions remain open. | Fifteen items are unreviewed. | Exception resolution is not evidence of underlying payment settlement, which the snapshot does not confirm.
What must the next report preserve? | A common timestamp, denominator, and distinct stage labels | The highest percentage without its definition | An invented settlement confirmation | A guarantee that authorization will occur by 11:00 | Comparable counts need the same snapshot basis and clear stages rather than mixed timestamps or unsupported outcome claims.''',
    rehearsal=['Read turns 1-10 and reconcile the 24, six, and fifteen status groups.', 'Swap roles for turns 11-20; distinguish resolving an exception from settling a payment.', 'Complete the twenty-item transfer and check the open count and both percentages.'],
    dialogue='''Bea | The report says thirty items reviewed. Can I tell the morning meeting that the exception queue is cleared?
Colin | No. The [[queue snapshot::The queue snapshot fixes the population and status at 10:00, preventing a review count from becoming an all-clear claim.]] contains forty-five items at ten hundred local time. Thirty were reviewed, but only twenty-four are resolved. Six reviewed items still await authorization, and fifteen remain unreviewed.
Bea | I had read thirty reviewed as thirty finished. Show the six awaiting approval separately so the meeting does not repeat that mistake.
Colin | Yes. [[Pending authorization::Pending authorization identifies reviewed items that still require approval and therefore remain unresolved in this queue.]] is an open status here. Those six items cannot be called resolved simply because someone examined them. The review found another step that has not yet been completed.
Bea | How many exceptions are still open in total? I initially thought only the fifteen unreviewed items remained.
Colin | There are twenty-one. Each [[unreviewed item::An unreviewed item is one of the fifteen not examined; open items also include the six reviewed but unresolved cases.]] belongs in the open group, along with the six awaiting authorization. Fifteen plus six gives twenty-one; counting only untouched items would understate the remaining work.
Bea | I want a clear percentage as well as counts. Thirty divided by forty-five is approximately sixty-six point seven percent.
Colin | That is the [[review rate::Review rate measures examined items over the full population, so thirty of forty-five is approximately 66.7%.]]. The resolution rate uses twenty-four, not thirty, as the numerator. Both can be useful, but the label must match the status being counted.
Bea | Twenty-four divided by forty-five gives approximately fifty-three point three percent. We should not substitute the larger review percentage.
Colin | Correct. The [[resolution rate::Resolution rate uses the twenty-four exceptions meeting the defined resolution condition, producing approximately 53.3% of the forty-five-item queue.]] describes the queue's defined resolved state. It does not mean that the same percentage of all payment value has moved, because this snapshot counts items rather than money.
Bea | Do the twenty-four resolved exceptions establish that those payments have reached their final destination? The meeting may ask about customer impact.
Colin | They do not establish [[settlement::Settlement is a downstream payment state requiring its actual evidence; resolving a queue exception does not confirm it.]]. Exception resolution and payment settlement are different states. We need the relevant payment records before making a statement about the underlying transfer's completion or customer receipt.
Bea | The approver expects to act shortly. I will leave those six open until the actual decision, even if it arrives before the meeting.
Colin | Right. A [[resolved exception::A resolved exception has actually met the queue's condition; expected authorization does not satisfy that condition in advance.]] must meet the stated condition, not an expectation. Keep the approval dependency explicit until its actual status changes under the authorized process.
Bea | If we report a processing deadline, we should specify which system and stage it concerns. There is no universal time for every payment.
Colin | Exactly. A [[cut-off time::A cut-off time applies to a specified processing cycle or service; it is not a universal promise about every payment's settlement.]] belongs to a particular service or cycle. This snapshot gives no applicable cut-off or settlement confirmation, so we must not invent one to make the update sound complete.
Bea | Let us provide another snapshot at eleven hundred. That gives the team a clear next contact without promising that all items will disappear.
Colin | Agreed. We can report any verified [[payment release::Payment release is the authorized sending to a next stage; it must be verified separately and not inferred from a reporting appointment.]] information separately if available. Eleven hundred is our next information update, not an authorization event or a guarantee that every open exception will be resolved.
Bea | My headline will say forty-five total, twenty-four resolved, six reviewed awaiting authorization, and fifteen unreviewed, all as of ten hundred.
Colin | That accurately describes the [[exception queue::The exception queue is the defined population requiring attention; its status must preserve all three groups and their common timestamp.]]. The three exclusive groups reconcile to forty-five, and the open count is twenty-one. Keep those counts with the timestamp so readers do not combine this snapshot with a later number.''',
    transfer_title='Reconcile another queue snapshot',
    transfer_setup='A fixed snapshot has 20 exceptions. Twelve are reviewed: nine resolved and three awaiting authorization. Eight are unreviewed. There are no other categories.',
    transfer='''Analyst: "The resolved count is ___." | nine | Nine items are explicitly resolved, not all twelve reviewed items.
Supervisor: "The open count is ___." | eleven | Three awaiting authorization plus eight unreviewed gives eleven open exceptions.
Analyst: "The review rate is ___." | 60% | Twelve reviewed divided by twenty total exceptions equals sixty percent.
Supervisor: "The resolution rate is ___." | 45% | Nine resolved divided by twenty total exceptions equals forty-five percent.'''))


BOOK['units'].append(unit(
    title='Fraud Operations and Customer Escalation',
    scene='Give one accurate explanation of the disputed-transaction process',
    skill='Correct conflicting service messages while separating dispute intake, investigation, temporary credit, and the final outcome.',
    brief='Customer June disputes a $380 debit-card transaction posted on 7 September to her U.S. consumer account. The bank received her notice on 9 September. One agent told her to resolve it with the merchant first; another said a police report was required before an investigation could begin. Specialist Amir must correct those barriers under the applicable electronic-fund-transfer error-resolution process, preserve the original notice date, and identify the information still needed. No final finding or credit decision is supplied. Applicable investigation, provisional-credit, and notice requirements must be checked promptly; a later handoff does not restart the notice date or justify delay.',
    cast='June | Customer\nAmir | Disputes specialist',
    culture=('Repair the process explanation before adding another request', 'A customer who has heard contradictory instructions may distrust even an accurate next step. Acknowledge the conflict, preserve the original report, and explain which information genuinely helps the review. Do not make the customer repeat an unnecessary prerequisite to receive a consistent answer.'),
    a='''What is the original notice date? | 9 September | 7 September | The date Amir happens to read the file | A future date after merchant contact | Nine September is when the bank received the notice; posting and internal handoff dates are different.
Which barriers must Amir correct in this case? | Requiring merchant resolution or a police report before beginning the applicable investigation | Recording the transaction amount | Preserving the original notice | Checking applicable requirements promptly | The supplied U.S. consumer dispute must not be blocked by those stated prerequisites to initiating error resolution.
What outcome has been established? | No final finding or credit decision is supplied. | A guaranteed permanent refund | A confirmed finding that June authorized the transaction | A final denial because she lacks a police report | The brief leaves both the final finding and credit decision unspecified.''',
    vocabulary='''electronic fund transfer (EFT) | A transfer of funds through electronic means within the applicable framework. | identify the electronic fund transfer
Regulation E | A U.S. regulation implementing consumer electronic-fund-transfer protections. | apply the relevant Regulation E process
unauthorized transaction | A transaction the customer did not make or permit, subject to the applicable definition. | report an unauthorized transaction
disputed transaction | A transaction challenged by the customer for a stated reason. | record the disputed transaction
notice of error | A customer's communication identifying an alleged error under the applicable process. | preserve the notice of error
notice date | The date the relevant recipient received the error report. | retain the original notice date
posting date | The date a transaction is recorded to the account. | distinguish the posting date
merchant | The seller or service provider associated with a card transaction. | identify the merchant
investigation | Examination of relevant facts to determine the dispute outcome. | begin the applicable investigation
provisional credit | A temporary account credit while the relevant investigation continues. | explain provisional credit
final credit | A credit made permanent under the completed decision. | distinguish final credit
debit-card dispute | A challenge relating to a debit-card transaction. | handle a debit-card dispute
error resolution | The process for investigating and addressing alleged account errors. | follow error-resolution requirements
written confirmation | A written account confirming a previously reported matter when applicable. | explain written-confirmation requirements
supporting information | Relevant details or records assisting the investigation. | request supporting information
transaction descriptor | The displayed text identifying a transaction or merchant entry. | check the transaction descriptor
case reference | The identifier assigned to the dispute or review. | provide the case reference
handoff | Transfer of responsibility or information between service teams. | document the handoff
interim update | A progress communication before the final decision. | provide an interim update
final finding | The determination reached after the relevant investigation. | explain the final finding
notification requirement | An obligation to communicate specified information under the applicable process. | verify notification requirements
customer authentication | Verification of the customer's identity through the approved process. | complete customer authentication
sensitive credential | Secret information used to access or authorize account activity. | protect sensitive credentials
process correction | An action fixing an inaccurate instruction or handling step. | record the process correction''',
    precision='For this U.S. consumer electronic-transfer dispute, do not require merchant resolution or a police report before initiating the applicable investigation. Preserve the original 9 September notice; an internal handoff does not create a new notice date.',
    precision_extra='Provisional credit is temporary and is distinct from a final finding or permanent credit. Applicable requirements and timing must be checked promptly. This exercise does not create a universal deadline or make provisional credit discretionary when the law requires it.',
    phrases='''Acknowledge the conflict | You received two different process explanations.
Correct the barriers | We should not make those prerequisites to initiating the applicable investigation.
Preserve the notice | The bank received your report on 9 September.
Separate the posting date | The transaction posted on 7 September.
Avoid restarting the clock | This handoff does not change the original notice date.
Identify the amount | The disputed debit-card amount is $380.
Request relevant facts | Please confirm the transaction descriptor and what you dispute.
Avoid repeated intake | I will check what the file already contains.
Keep authentication safe | Use the approved verification process; do not share a PIN or one-time code here.
Explain the review | The investigation will assess the relevant facts.
Separate temporary and final credit | Provisional credit does not establish the final outcome.
Avoid a premature guarantee | No permanent refund decision is supplied in the current record.
Respect applicable requirements | We need to check the investigation and credit requirements promptly.
Explain a real next step | I will identify the missing information and responsible review team.
Correct the record | Document the earlier conflicting instructions and the process correction.
Close clearly | Keep the original notice, investigation status, and credit status separate.''',
    notes='''Received on | Names the actual notice date rather than a later processing date.
Before beginning | Identifies the improper barriers supplied by this case.
Provisional | Temporary pending the relevant investigation and decision.
Not supplied | Prevents an invented credit decision from entering the exercise.
Promptly check | Does not authorize waiting indefinitely for internal convenience.
Do not share | Protects secret credentials while allowing approved identity verification.''',
    d='''Which message corrects the process? | We will preserve your 9 September notice and not require those prerequisites to begin the applicable investigation. | Your notice begins only after a police report. | Merchant refusal automatically ends the bank's role. | The handoff erases your original report date. | The correct message preserves the original notice and removes the improper initiation barriers in this case.
What does provisional credit mean? | Temporary credit distinct from a final decision | A guaranteed permanent refund in every case | Proof that the customer committed fraud | Permission to ignore investigation requirements | Provisional credit is temporary during the applicable investigation and does not itself decide the final outcome.
Which date is the posting date? | 7 September | 9 September | The handoff date | No date is supplied | Seven September is explicitly when the disputed transaction posted to the account.
Which request should Amir avoid? | Asking June to disclose a PIN or one-time code in this conversation | Asking what transaction she disputes | Checking the recorded descriptor | Reviewing information already in the file | Secret access credentials must be protected; approved authentication should not become a request to disclose them here.''',
    rehearsal=['Read turns 1-10, preserving the original notice and correcting the two initiation barriers.', 'Swap roles for turns 11-20; distinguish temporary credit, investigation, and final findings.', 'Complete the May transfer and check the posting, notice, and handoff dates separately.'],
    dialogue='''June | I reported the three-hundred-eighty-dollar debit on September ninth. One agent said to resolve it with the merchant; another demanded a police report.
Amir | Those conflicting instructions need a [[process correction::Process correction removes the inaccurate initiation barriers without deciding the transaction's merits or promising a refund.]]. For this consumer electronic-transfer dispute, we should not require merchant resolution or a police report before beginning the applicable investigation. I will record and correct that explanation.
June | The charge posted on September seventh. Does your involvement today mean my report date changes to today?
Amir | No. We must preserve the original [[notice date::The notice date is September ninth, when the bank received the report; a later handoff does not restart it.]] of September ninth. September seventh is the posting date. An internal transfer between teams does not change when the bank received your notice or justify restarting the process.
June | I can confirm the amount and merchant description. Please check my first report so this does not become a new intake each time.
Amir | I will review the [[transaction descriptor::The transaction descriptor is the displayed identifying text and helps locate the disputed entry without establishing whether it was authorized.]] and your recorded explanation. We need relevant missing information. A familiar merchant name alone does not answer the dispute.
June | I did not make or permit this transaction. Will you record that without assuming the result before the investigation?
Amir | Yes. We will record the alleged [[unauthorized transaction::Unauthorized transaction describes the customer's reported concern subject to the applicable definition and factual investigation.]] and investigate the relevant facts. We must consider your report properly. The file contains no final finding.
June | Another message mentioned temporary credit. Does that mean the bank has already decided to give me the money permanently?
Amir | [[Provisional credit::Provisional credit is temporary during investigation and must not be described as a final permanent refund decision.]] is different from a final credit or finding. We need to check the applicable credit requirements and timing promptly. Required protections are not optional.
June | I understand that the outcome is open, but I need the team to follow the correct timetable rather than leave the case pending indefinitely.
Amir | Agreed. The applicable [[error resolution::Error resolution has requirements for investigation and communication; an open case is not permission to delay indefinitely.]] process governs investigation, credit, and communication requirements. We must check the actual case conditions and original notice date rather than replace them with a convenient internal target.
June | Please explain any written-confirmation requirement clearly. Another vague instruction should not block the investigation.
Amir | Any [[written confirmation::Written confirmation requirements must be explained accurately within the applicable process, not invented as a universal barrier to investigation.]] request must be explained accurately under the applicable process. It should identify what is needed and its significance, without recreating the improper police-report or merchant-resolution prerequisite you were given.
June | Before discussing account details, I will use the bank's verified service route. I will not share a PIN or one-time code in this conversation.
Amir | Correct. [[Customer authentication::Customer authentication uses the approved identity-checking process; it does not justify requesting secret credentials in this conversation.]] must follow the approved process. Protect sensitive credentials and use the verified channel for any relevant documents. This message does not need secret access details.
June | Please include the original notice and corrected advice in the handoff. I do not want to argue about the police report again.
Amir | I will document the [[handoff::The handoff transfers accurate context and responsibility while preserving the original notice, reported facts, and corrected process instructions.]] with those facts and the remaining information needs. The next reviewer should see the amount, posting date, notice date, reported concern, and process correction without having to reconstruct the conversation.
June | Then an update will tell me the actual review and credit status, rather than imply that either temporary credit or a new contact decides the outcome.
Amir | Exactly. An [[interim update::An interim update reports progress without substituting for the final finding or altering applicable investigation and credit obligations.]] should explain the actual status and next step. Keep investigation, provisional credit, and the final decision distinct, and make sure communication follows the applicable requirements rather than another unsupported promise.''',
    transfer_title='Preserve another original notice',
    transfer_setup='A consumer disputes a $240 debit-card transaction posted on 2 May. The bank received notice on 4 May. A later internal handoff occurs on 6 May. No final finding is supplied.',
    transfer='''Specialist: "The disputed amount is ___ dollars." | 240 | Two hundred forty dollars is the transaction amount supplied for this dispute.
Customer: "The posting date was ___." | 2 May | Two May is the transaction posting date, distinct from notice and handoff.
Specialist: "The original notice date remains ___." | 4 May | Four May is when the bank received notice; the later handoff does not replace it.
Customer: "The internal handoff occurred on ___." | 6 May | Six May is the internal transfer date, not a new original notice date.'''))


BOOK['units'].append(unit(
    title='Operational Risk and Controls',
    scene='A sign-off cannot erase an unmatched balance',
    skill='Explain a reconciliation break, correct a misleading control status, and preserve evidence for the next reviewer.',
    brief='The 30 June reconciliation shows a $250,000 general-ledger balance and a $248,750 subledger balance on the same stated basis, leaving a $1,250 difference. The cause is unconfirmed. A control record has been signed as fully reconciled, although the unmatched item remains under investigation. Analyst Tess and controller Omar must correct that description through the traceable review process. The local procedure permits a reviewer to acknowledge a documented open exception, but not to label an unresolved difference fully matched. No journal adjustment or write-off has been approved. A timing difference is only one possible explanation, not an established fact.',
    cast='Tess | Reconciliation analyst\nOmar | Operations controller',
    culture=('Describe the control state instead of defending the signature', 'A signed record can make a colleague reluctant to raise a remaining difference. Separate acknowledgment of work performed from confirmation that all items match. A precise correction protects the record without assuming misconduct by the person who signed it.'),
    a='''What is the unmatched amount? | $1,250 | $250,000 | $248,750 | $2,500 | Two hundred fifty thousand minus two hundred forty-eight thousand seven hundred fifty equals twelve hundred fifty.
What is established about the cause? | It remains unconfirmed. | It is definitely a timing difference. | It is proven fraud. | It is an approved write-off. | The brief explicitly leaves the cause unconfirmed and identifies timing only as a possibility.
What does the local procedure allow? | Acknowledgment of a documented open exception without calling it fully matched | An unsupported fully reconciled label | Automatic write-off of every small difference | A balancing journal without approval | The local process distinguishes review acknowledgment from claiming that an unresolved difference has been matched.''',
    vocabulary='''general ledger (GL) | The main accounting record of balances and entries. | reconcile the general ledger
subledger | A detailed record supporting a general-ledger balance. | compare the subledger
reconciliation | Comparison of records to identify and explain differences. | perform a reconciliation
reconciling item | A difference requiring explanation or resolution between compared records. | investigate a reconciling item
unmatched balance | An amount not yet matched or explained on the comparison basis. | report an unmatched balance
timing difference | A difference arising from when related events are recorded, if established. | substantiate a timing difference
journal entry | An accounting entry recording a transaction or adjustment. | review a journal entry
adjustment | A change to accounting records under the appropriate basis and authority. | authorize an adjustment
write-off | Removal of a recorded amount under the applicable accounting decision. | approve a write-off
supporting schedule | A detailed record explaining a reported balance. | retain the supporting schedule
control sign-off | A recorded review or approval with a specified meaning. | qualify the control sign-off
preparer | The person producing a record or reconciliation. | identify the preparer
reviewer | The person checking the work under the relevant process. | identify the reviewer
segregation of duties | Separation of incompatible responsibilities to reduce risk. | maintain segregation of duties
maker-checker control | A process in which one person prepares and another independently checks the relevant action. | apply a maker-checker control
control exception | A departure or unresolved condition identified in a control process. | document a control exception
exception aging | The length of time an unresolved item has remained open. | monitor exception aging
root-cause analysis | Examination of the underlying reason for a problem. | conduct root-cause analysis
control deficiency | A weakness in control design or operation under the relevant assessment. | assess a control deficiency
operational loss | Loss arising from relevant operational events or failures. | record an operational loss
audit trail | Records allowing an action or decision to be traced. | preserve the audit trail
reperformance | Independently repeating a procedure to evaluate its result. | arrange reperformance
evidence reference | A link or identifier connecting a conclusion to supporting material. | add an evidence reference
resolution owner | The person accountable for coordinating an item's resolution. | assign a resolution owner''',
    precision='The $1,250 difference is established; its cause is not. Calling it a timing difference requires evidence. Neither the amount nor the existence of a signature authorizes an adjustment, write-off, or fully matched conclusion.',
    precision_extra='A reviewer may acknowledge an open exception under this stated local process, but the record must describe that status honestly. Correcting the label is different from resolving the underlying difference, and both need their own evidence.',
    phrases='''State the comparison | The ledger shows $250,000 and the subledger $248,750.
Confirm the basis | Both balances use the same stated comparison basis.
Calculate the difference | The unmatched amount is $1,250.
Preserve the unknown | The cause has not been confirmed.
Avoid a convenient label | Timing is a possible explanation, not an established one.
Correct the control description | Fully reconciled is not supported while this difference remains unexplained.
Recognize permitted acknowledgment | The reviewer can acknowledge a documented open exception.
Separate correction and resolution | Fixing the label does not resolve the balance difference.
Protect the evidence | Preserve the original record and correction history.
Avoid an unsupported entry | No balancing adjustment has been approved.
Keep authority explicit | A write-off requires its applicable basis and authorization.
Name responsibility | Assign the resolution owner and next review step.
Keep the item visible | Record the amount and status in the exception log.
Link the support | Attach the relevant ledger and subledger references.
Distinguish roles | Preparation and independent review are separate responsibilities.
Close accurately | Report the open difference and qualified review status together.''',
    notes='''Fully reconciled | Claims a completed match or explanation that this case lacks.
Acknowledged with exception | Can describe the local permitted review without hiding the difference.
Possible versus confirmed | Separates an explanation to investigate from an established cause.
Balancing entry | Must not be used merely to make unexplained records agree.
Corrected label | Changes the record's description, not the underlying balance.
Same basis | Ensures the subtraction compares like figures.''',
    d='''Which control description is accurate? | Reviewed with an open $1,250 exception; cause under investigation | Fully matched with no unresolved items | Written off because the amount is inconvenient | Proven fraud based only on the difference | The accurate status preserves the reviewed work and the outstanding difference without inventing its cause or resolution.
Which action is unsupported? | Post an unapproved $1,250 adjustment solely to force agreement. | Preserve both balance records. | Correct the misleading status traceably. | Assign a resolution owner. | No adjustment is authorized, and forcing agreement without a basis would conceal rather than explain the difference.
What is needed before calling this a timing difference? | Evidence establishing the timing explanation | The fact that a similar amount cleared last month | A reviewer signature without transaction-level support | A difference small relative to the total balance | Timing is a hypothesis until relevant records establish this difference's cause; precedent, sign-off, and size do not do so.
Which statement distinguishes two tasks correctly? | Correcting the sign-off description does not itself resolve the underlying balance. | Changing the label automatically changes the balances. | Keeping an exception log proves the cause. | A review signature replaces every missing record. | Record correction and substantive reconciliation resolution are separate actions requiring their own basis.''',
    rehearsal=['Read turns 1-10 and state the $1,250 difference without assigning an unconfirmed cause.', 'Swap roles for turns 11-20; separate correction of the sign-off from correction of a balance.', 'Complete the $90,000 comparison and check the amount, direction, and unknown cause.'],
    dialogue='''Tess | The June thirtieth record says fully reconciled, but the ledger shows two hundred fifty thousand and the subledger two hundred forty-eight thousand seven hundred fifty.
Omar | That leaves an [[unmatched balance::The unmatched balance is the established 1,250-dollar difference on the stated common basis, not an explanation of its cause.]] of twelve hundred fifty dollars. We must preserve that difference in the record. The signature does not establish that it has been explained or resolved.
Tess | The analyst thought it might be a posting-date issue. We do not yet have the records needed to confirm that explanation.
Omar | Then do not call it a confirmed [[timing difference::A timing difference needs supporting evidence; it remains only one possible explanation in this case.]]. It is a possibility to investigate. A plausible explanation can guide the next check without becoming the stated cause before the evidence supports it.
Tess | Our procedure lets a reviewer acknowledge work with a documented exception. It does not permit calling every balance matched when one remains unresolved.
Omar | Correct the [[control sign-off::The control sign-off must state its actual meaning, distinguishing acknowledgment with an open exception from a fully matched conclusion.]] accordingly. Reviewed with an open exception is different from fully reconciled. We should describe the permitted review state without using the signature to hide the unfinished item.
Tess | I will preserve the original signed record and document the correction. The status change should not silently remove the earlier wording.
Omar | Maintain the [[audit trail::The audit trail preserves the original and subsequent correction so reviewers can trace what changed and why.]]. Explain why the description changed and retain the supporting references. Correcting a misleading label improves the record, but it does not itself resolve the accounting difference.
Tess | The proposed adjustment would make the report balance, but I cannot find a transaction or approval supporting the twelve-hundred-fifty-dollar entry.
Omar | Do not create a [[journal entry::A journal entry records an accounting event or adjustment; no unsupported balancing entry is authorized merely to force agreement.]] simply to force agreement. Any actual adjustment needs its proper evidence and authority. Otherwise, the apparent match would conceal an unexplained item rather than provide a valid reconciliation.
Tess | Nor can we write it off just because it is smaller than the full account balance. The amount alone does not provide approval.
Omar | Exactly. A [[write-off::A write-off requires the applicable accounting basis and authorization; relative size alone does not establish either.]] requires its applicable basis and authorization. Neither has been established. Keep the difference open while the relevant records are examined, rather than selecting a convenient accounting outcome.
Tess | The note just says investigate. We need a named coordinator and the specific records to obtain before the next review.
Omar | Assign the [[resolution owner::The resolution owner coordinates follow-up on the difference; naming that person does not itself establish its cause or closure.]] through the local process and record the next review step. Ownership, evidence gathering, and resolution are separate facts; an assigned name should not be mistaken for a closed issue.
Tess | We can link the ledger extract and detailed balance schedule. The next reviewer should see the actual amounts without reconstructing them from our conversation.
Omar | Add an [[evidence reference::An evidence reference connects the stated balances and conclusions to the actual records, making the reconciliation reviewable.]] for each. Preserve the common comparison basis as well. If the balances come from different dates or scopes, that would be a different question requiring its own explanation.
Tess | The comparison basis matches. The root cause remains unconfirmed.
Omar | Keep the [[control exception::The control exception is the unresolved condition in the process; recording it honestly does not determine whether or how it will be resolved.]] visible with its amount and status. The control can acknowledge the exception honestly under the stated procedure; it cannot claim that no exception exists.
Tess | The corrected handoff will show the twelve-hundred-fifty-dollar difference, unconfirmed cause, no approved adjustment, and review acknowledgment with the exception still open.
Omar | Good. Preserve [[segregation of duties::Segregation of duties keeps preparation, checking, and approval appropriately distinct rather than letting urgency bypass the required roles.]] as the work proceeds. Independent review and any authorized accounting decision must follow the applicable roles. A cleaner-looking balance is not a substitute for an explained and properly approved outcome.''',
    transfer_title='Describe a second reconciliation break',
    transfer_setup='A same-basis comparison shows a $90,000 ledger balance and an $89,600 subledger balance. The cause is unknown. No adjustment is approved.',
    transfer='''Analyst: "The ledger balance is ___ dollars." | 90,000 | Ninety thousand is the supplied general-ledger amount for this separate comparison.
Reviewer: "The subledger balance is ___ dollars." | 89,600 | Eighty-nine thousand six hundred is the supplied supporting balance.
Analyst: "The unmatched difference is ___ dollars." | 400 | Ninety thousand minus eighty-nine thousand six hundred equals four hundred dollars.
Reviewer: "The cause remains ___." | unknown | The case does not establish a timing, error, or other explanation.'''))

BOOK['units'].append(unit(
    title='Audit and Regulatory Exams',
    scene='A policy describes the control but does not prove it operated',
    skill='Respond to an evidence request with exact scope, honest availability, and traceable period coverage.',
    brief='An examiner requests evidence that control R9 operated during March, including records for 3, 10, 17, 24, and 31 March. Coordinator Liv has policy version 2 ready. She has also retrieved completed records for 10 and 24 March; records for the other three requested dates have not yet been located. The absence of retrieved records does not by itself establish whether the control failed or operated. Control owner Yusuf will help locate the evidence and report retrieval status Wednesday at 13:00. Liv must distinguish policy design from operating evidence and must not recreate historical sign-offs as if they were original.',
    cast='Liv | Examination coordinator\nYusuf | Control owner',
    culture=('A transparent evidence gap is better than a misleading package', 'Teams may feel pressure to answer an examination request with whatever looks complete. Map the request to the exact dates and evidence types. A clear account of what is available and missing helps the reviewer understand the actual record without a fabricated claim of completeness.'),
    a='''How many requested dated records are retrieved? | Two of five | Five of five | Three of five | None | The records for 10 and 24 March are retrieved; three other requested dates remain unlocated.
What does policy version 2 primarily describe? | The control's documented design or requirements | Proof of performance on every requested date | A completed examiner conclusion | A substitute for every historical sign-off | A policy describes intended control arrangements and is distinct from evidence that the control actually operated.
What can be concluded about the three unlocated records? | Their retrieval is incomplete; operation is not established by that fact alone. | The control definitely failed on all three dates. | The control definitely operated correctly. | The records may be invented to finish the package. | Unlocated evidence leaves a gap but does not alone prove either performance or failure.''',
    vocabulary='''regulatory examination | A supervisory review by the relevant regulatory authority. | coordinate a regulatory examination
examination request | A request for records or explanation within an examination. | respond to an examination request
request reference | The identifier linking a request to the response and evidence. | retain the request reference
control design | The planned structure and requirements of a control. | explain control design
operating effectiveness | Whether a control actually functions as intended over the relevant basis. | assess operating effectiveness
population | The full set of items relevant to a defined review. | define the review population
sample selection | The items chosen from the relevant population for examination. | confirm the sample selection
review period | The dates covered by the requested assessment. | identify the review period
dated evidence | A record tied to an identifiable time or event. | provide dated evidence
execution record | Documentation that a specified activity was performed. | retrieve the execution record
reviewer sign-off | A record of the reviewer's check or approval under the process. | verify the reviewer sign-off
evidence inventory | A list of requested, available, and outstanding supporting records. | maintain an evidence inventory
evidence gap | Missing support for a requested fact or conclusion. | disclose an evidence gap
retrieval status | The stage of locating and obtaining records. | report retrieval status
record custodian | The person or function responsible for keeping the relevant records. | contact the record custodian
walkthrough | A guided examination of how a process is designed or carried out. | conduct a process walkthrough
test of control | A procedure assessing relevant control design or operation. | perform a test of control
period coverage | The extent to which evidence represents the required time interval. | assess period coverage
contemporaneous record | A record created at or near the time of the relevant event. | preserve a contemporaneous record
retrospective explanation | A later account describing a past event or missing record. | label a retrospective explanation
evidence mapping | Linking each request item to its supporting record. | complete evidence mapping
response package | The organized material submitted in reply to a request. | assemble the response package
examiner conclusion | The outcome reached by the examiner's assessment. | distinguish the examiner conclusion
management representation | A statement by management about a matter under review. | qualify a management representation''',
    precision='Two retrieved records out of five requested dates is 40% retrieval coverage for that request. It is not a 40% control-effectiveness score, and it does not establish a conclusion about every day in March.',
    precision_extra='A later explanation can be useful if clearly labeled and supported, but it is not an original historical sign-off. Preserve dates, authorship, and the distinction between contemporaneous evidence and a retrospective account.',
    phrases='''Restate the request | The examiner requested R9 evidence for five specified March dates.
Identify the policy | Policy version 2 is available.
Separate design and operation | The policy describes requirements; it does not prove each execution.
State retrieved records | We have the records for 10 and 24 March.
Name the missing dates | Records for 3, 17, and 31 March are not yet located.
Quantify only what is measured | Retrieval coverage is two of five requested records.
Avoid a performance score | That is not a control-effectiveness percentage.
Preserve uncertainty | Missing retrieved evidence does not by itself prove performance or failure.
Map the package | Link each requested date to its actual evidence.
Contact the custodian | Yusuf will help locate the outstanding records.
Protect historical accuracy | Do not create a later sign-off as though it were original.
Label later explanations | Identify any retrospective account by author, date, and basis.
State the next contact | Retrieval status will be updated Wednesday at 13:00.
Limit the commitment | That is an update time, not a guarantee all records will be found.
Keep the conclusion separate | The examiner's assessment is not ours to invent.
Close the response | Submit the available evidence with an accurate inventory of outstanding items.''',
    notes='''Available policy | Describes a document's presence, not actual control performance.
For five dates | Limits the requested sample rather than implying every March day.
Not yet located | Names retrieval status without asserting that the activity never happened.
Forty percent retrieved | Measures record availability for this request, not effectiveness.
Retrospective | A later explanation must not masquerade as a contemporaneous entry.
Examiner conclusion | Belongs to the actual assessment, not a self-awarded status label.''',
    d='''Which package description is accurate? | Policy version 2 plus records for 10 and 24 March; three requested dates outstanding | Complete evidence for every March day | Proof of failure on three dates | Five original sign-offs reconstructed today | The description accurately identifies available material and outstanding requested records without fabricating completeness or performance.
What is the retrieval coverage? | 40% of the five requested dated records | 40% control effectiveness for all March | 60% completed examiner approval | 100% because the policy is available | Two retrieved records divided by five requested dates gives forty percent retrieval coverage only.
Which action would misrepresent the evidence? | Create today's sign-off and present it as an original March record. | Label a later explanation with its actual date. | Preserve the available records. | Identify the three unlocated dates. | A later record must not be presented as contemporaneous evidence that was created in March.
What should Yusuf report Wednesday if records remain missing? | The actual retrieval status and outstanding dates | That all controls passed because the appointment occurred | A guessed examiner conclusion | An invented historical signature | The promise concerns an accurate status update even if the evidence-retrieval work remains incomplete.''',
    rehearsal=['Read turns 1-10 and map each of the five requested dates to its actual status.', 'Swap roles for turns 11-20; distinguish an original record from a later explanation.', 'Complete the April transfer and label its 75% as retrieval coverage, not effectiveness.'],
    dialogue='''Liv | The examiner wants R9 records for March third, tenth, seventeenth, twenty-fourth, and thirty-first. I have policy version 2 ready.
Yusuf | The policy describes [[control design::Control design states how the control should work; the policy alone does not establish operation on the requested dates.]], but the request also needs operating evidence. We must distinguish the intended procedure from records showing what actually happened on each requested date.
Liv | I found records for the tenth and twenty-fourth. The other three are not yet located.
Yusuf | Put that in the [[evidence inventory::The evidence inventory lists available and outstanding records, preserving the two retrieved dates and three remaining gaps.]]. We have two requested dated records, not five. Keep the available records and missing dates visible rather than describing the package as complete because a policy document is attached.
Liv | That gives two out of five, or forty percent retrieval coverage. I should not call it a forty-percent effectiveness result.
Yusuf | Correct. [[Operating effectiveness::Operating effectiveness concerns actual control performance; the percentage of retrieved records is not a score of that performance.]] is a different assessment. Record availability for this request does not establish the control's success rate, and the five selected dates do not automatically represent every day in March.
Liv | Do the missing records prove the control was not performed on those dates? I want to avoid minimizing the gap.
Yusuf | They establish an [[evidence gap::An evidence gap means support is missing; it does not by itself prove either that the control operated or that it failed.]], not the full explanation. We must investigate and report it honestly. Do not assume performance, but do not claim failure solely because the record has not yet been located.
Liv | I will map each requested date to the available file or outstanding status. That should help the examiner see what the response actually contains.
Yusuf | Use [[evidence mapping::Evidence mapping links each requested item to its supporting record or explicit outstanding status, preventing a misleading package-level claim.]] with the relevant references. Check that each file belongs to the requested control and date. A similarly named record from another period is not a substitute merely because it is available.
Liv | Who can help find the outstanding files? I have checked the shared folder but have not established whether another authorized repository holds them.
Yusuf | I will coordinate with the [[record custodian::The record custodian is responsible for relevant records and can assist retrieval without inventing evidence or guaranteeing its existence.]]. We need the actual retention and storage context, not a guess. Any retrieval route must preserve the records and follow the applicable access requirements.
Liv | Someone offered backdated sign-offs. That would make today's entries look like original March evidence.
Yusuf | Do not present a new entry as a [[contemporaneous record::A contemporaneous record was created at or near the event; a new sign-off cannot be represented as original March evidence.]]. A later sign-off cannot be passed off as an original March record. We need accurate creation dates, authorship, and the actual basis of any later account.
Liv | A reviewer might remember performing the check. Could a clearly dated explanation help, even though it is not the original execution record?
Yusuf | A [[retrospective explanation::A retrospective explanation is a later account that must be labeled as such, not substituted deceptively for historical evidence.]] can be evaluated for what it is. Identify its author, date, and supporting basis. Do not imply it has the same origin as the missing historical document or automatically resolves the request.
Liv | At Wednesday's update, I will name any dates still outstanding. I cannot promise the search will recover every record.
Yusuf | Correct. The [[retrieval status::Retrieval status reports what has actually been located; the update appointment does not guarantee that every missing record will be found.]] update will name any remaining gaps. If we cannot locate a record, we must say so clearly and follow the authorized response process rather than manufacture completeness.
Liv | The package will include the policy, two dated records, a mapped list of the three outstanding dates, and any properly labeled later explanation.
Yusuf | Good. Keep the [[examiner conclusion::The examiner conclusion follows the actual supervisory assessment; the team must not invent approval from its own document submission.]] separate from our submission status. Providing a transparent package supports the review, but it does not mean the examiner has accepted the evidence or concluded that the control operated effectively.''',
    transfer_title='Map another evidence request',
    transfer_setup='An examiner requests four April records. Three are retrieved; one remains unlocated. The current policy is available. A retrieval update is due Friday.',
    transfer='''Coordinator: "The number of requested dated records is ___." | four | Four is the requested population for this separate evidence-retrieval task.
Owner: "The number retrieved is ___." | three | Three records are actually available; the fourth remains unlocated.
Coordinator: "Retrieval coverage is ___." | 75% | Three retrieved divided by four requested equals seventy-five percent, not a control-effectiveness score.
Owner: "The next retrieval update is due ___." | Friday | Friday is the status-update commitment, not a guarantee of complete evidence or examiner approval.'''))


BOOK['units'].append(unit(
    title='Customer Complaints and Fair Treatment',
    scene='The current fee schedule may not explain a past charge',
    skill='Investigate a historical fee question using the applicable period, product, transaction, and waiver conditions.',
    brief='Customer Priya asks about a $15 maintenance charge for the June statement cycle. Representative Daniel has a current fee schedule effective 1 August showing a $10 maintenance fee for a particular account product. He has not checked which product Priya held in June, the terms effective for that cycle, or whether any waiver condition applied. He cannot yet establish whether the $15 charge was correct or whether a refund is due. Daniel will obtain the relevant account and historical fee records and update Priya Tuesday at 15:00. The current schedule must not be applied retroactively merely because it is the first document available.',
    cast='Priya | Customer\nDaniel | Customer-service representative',
    culture=('Take the question seriously before defending the charge', 'A representative may reach for the current schedule because it is convenient. Restate the actual charge and period, then check the terms that applied. Acknowledge uncertainty without dismissing the complaint or promising a refund before the relevant records are examined.'),
    a='''What charge is disputed? | A $15 maintenance charge for the June cycle | A confirmed $10 August charge | A $150 transfer fee | An already approved refund | Priya asks about fifteen dollars charged for the June statement cycle.
What is the effective date of Daniel's available schedule? | 1 August | 1 June | Every prior year automatically | No date is supplied | The schedule is explicitly effective from 1 August and is not automatically applicable to June.
What remains unchecked? | June product, applicable historical terms, and waiver eligibility | Only the arithmetic difference between $15 and $10 | Only the amount printed on the August schedule | Only whether June precedes August | The missing evidence concerns the actual account and applicable terms, not arithmetic or the order of months.''',
    vocabulary='''maintenance fee | A recurring account charge under the applicable terms. | review a maintenance fee
fee schedule | A document listing charges and their conditions. | check the fee schedule
effective date | The date from which specified terms apply. | confirm the effective date
statement cycle | The period covered by a periodic account statement. | identify the statement cycle
account product | The specific type or version of account held by a customer. | verify the account product
historical terms | The terms applicable during a past relevant period. | retrieve historical terms
waiver condition | A requirement that, if met under the terms, removes or reduces a charge. | assess a waiver condition
minimum balance | A required balance threshold under a specified measure and period. | check the minimum-balance condition
average daily balance | A balance measure averaging daily balances over a defined period. | calculate average daily balance
qualifying deposit | A deposit meeting the specified conditions for a benefit or waiver. | identify a qualifying deposit
billing period | The interval to which charges are attributed. | confirm the billing period
posting entry | A recorded account transaction or charge. | trace the posting entry
account conversion | A change from one account product or arrangement to another. | review an account conversion
change notice | Communication of altered terms under the applicable process. | retrieve the change notice
fee assessment | The application of a charge under specified rules and facts. | examine the fee assessment
eligibility | Whether conditions for a particular term or benefit are met. | verify waiver eligibility
retroactive application | Applying terms to a period before their stated applicability. | question retroactive application
historical schedule | The charge schedule applicable to a past period. | obtain the historical schedule
service record | Documentation of customer contacts and actions. | update the service record
complaint reference | An identifier linking a complaint to its handling record. | provide a complaint reference
refund decision | A determination about returning a charged amount. | explain the refund decision
account credit | An entry increasing or offsetting the customer's account balance as applicable. | verify an account credit
case resolution | The supported outcome and completion status of a customer case. | document case resolution
further review | Additional examination through the applicable process. | explain further-review options''',
    precision='The current $10 schedule does not prove the June charge should have been $10. Its effective date is 1 August, and its product coverage still needs checking. A $5 difference alone does not establish a refund.',
    precision_extra='A waiver may depend on a specific balance measure, deposit type, or other condition. Do not substitute an end-of-month balance for an average-daily-balance requirement or assume every deposit qualifies. Use the actual applicable terms.',
    phrases='''Restate the charge | You are asking about the $15 maintenance charge for June.
Name the available document | I have a schedule effective from 1 August.
Limit its use | That schedule does not automatically explain the June charge.
Check the product | I need to confirm the account product held during that cycle.
Find the applicable terms | We will retrieve the fee schedule effective for June.
Review the waiver | We also need to check whether a waiver condition applied.
Avoid a premature defense | I have not established that the charge was correct.
Avoid a premature refund | The $5 difference does not by itself establish a refund.
Separate balance measures | The relevant balance measure depends on the actual terms.
Preserve the history | An account conversion may affect which product terms apply.
Check disclosure | Retrieve the relevant change notice if the terms changed.
Make the next step concrete | I will obtain the historical account and fee records.
Give the next contact | I will update you Tuesday at 15:00.
Limit the appointment | That is a review update, not a guaranteed credit date.
Keep the complaint open | The fee question remains unresolved.
Close with accountability | The response will explain the applicable period, product, and basis for the outcome.''',
    notes='''Effective from | Establishes when terms apply, not every earlier period.
For June | Connects the complaint to its actual statement cycle.
Held during | Recognizes that the product may have changed over time.
Whether a waiver applied | Requires evidence of eligibility, not an assumed benefit.
Difference versus error | Two different amounts do not automatically prove a billing mistake.
Update versus credit | A communication appointment does not establish an account adjustment.''',
    d='''Which first reply is accurate? | I will check the June product, historical terms, and waiver conditions before deciding the charge. | Today's $10 schedule proves you are owed $5. | Every $15 fee is automatically correct. | The complaint is invalid because the schedule changed. | The accurate reply identifies the relevant period and facts without using current terms to invent a historical conclusion.
Why does the 1 August date matter? | It limits the current schedule's applicability and does not automatically establish June terms. | It guarantees every June fee was waived. | It proves Priya held the same product in June. | It is irrelevant to every fee question. | Effective dates help identify which terms apply; the current document alone does not establish the earlier cycle's rules.
Which waiver assumption is unsupported? | Any deposit automatically satisfies every qualifying-deposit condition. | The applicable waiver wording needs review. | The account product needs confirmation. | Different balance measures can produce different results. | Qualifying deposits are defined by the actual terms, so not every deposit necessarily satisfies the condition.
What should Tuesday's update do if the review remains incomplete? | Identify the actual outstanding records and review status. | Invent a refund approval to meet the appointment. | Apply the current schedule retroactively without review. | Close the complaint because one response was sent. | The commitment is to communicate the real status, not manufacture an outcome before the evidence is complete.''',
    rehearsal=['Read turns 1-10 and distinguish the June charge from the August schedule.', 'Swap roles for turns 11-20; separate a qualifying deposit from any deposit.', 'Complete the April transfer and check the charge, later schedule, and update date.'],
    dialogue='''Priya | My June statement has a fifteen-dollar maintenance charge. Your current schedule shows ten dollars. Why was I charged more?
Daniel | I need to check the [[historical terms::Historical terms establish what applied in June; the current schedule does not automatically govern that earlier cycle.]]. The schedule I have is effective from August first. It cannot by itself explain June's charge, and I should not assume either that the fee was correct or that it was wrong.
Priya | I also changed accounts earlier in the year. Could the specific product I held in June affect which fee applied?
Daniel | Yes. We must confirm the [[account product::Account product identifies the specific account arrangement held during the relevant period, which can affect applicable charges and conditions.]] for that cycle. The current schedule covers a particular product. I have not established that it matches the account and terms you held when the June fee was assessed.
Priya | The five-dollar difference does not automatically establish a refund. We need the relevant records.
Daniel | Correct. A [[refund decision::A refund decision needs the applicable facts and terms; a numerical difference between schedules does not establish an error or entitlement.]] must follow the actual review. I will not promise a credit merely because two figures differ, and I will not defend the charge without checking its basis.
Priya | I expected the balance waiver. My month-end balance was positive, but which balance measure actually applies?
Daniel | We need the actual [[waiver condition::A waiver condition defines eligibility under the terms; a positive balance at one point does not establish every possible balance requirement.]]. It may use a specific balance measure or another criterion. A positive balance on one day is not automatically evidence that the relevant condition was met throughout its required basis.
Priya | If the terms use an average daily balance, that would be different from the balance on the last day of the statement period.
Daniel | Exactly. [[Average daily balance::Average daily balance averages the defined daily balances over a period; it is not interchangeable with a single closing balance.]] and a closing balance are different measures. We must use the measure required by the applicable June terms rather than choose whichever figure is easiest to locate or seems most favorable.
Priya | I also received a deposit that month. Please check whether it counted for the waiver instead of assuming every deposit qualifies.
Daniel | I will check the [[qualifying deposit::A qualifying deposit meets the actual terms; receiving some deposit does not necessarily satisfy a specified waiver criterion.]] definition if that condition is relevant. The review should connect the actual transaction details to the terms, not infer eligibility or ineligibility from a broad description alone.
Priya | Please check the account-change date and fee notice together. I need to know which terms applied during June.
Daniel | Yes. We will trace any relevant [[account conversion::Account conversion changes the account arrangement and may affect which terms apply; its timing needs evidence rather than assumption.]] and change notice. That history may help establish the correct product and effective period. We should not apply today's information backward simply because it is the first document available.
Priya | Please keep the actual complaint tied to the June cycle. I am not asking you to decide whether August's fee is correct.
Daniel | I will record the [[statement cycle::The statement cycle identifies the period disputed; the June complaint must not be replaced with an unrelated August fee question.]] and fifteen-dollar posting explicitly. The current ten-dollar schedule is a comparison document, not a substitute for the historical account, fee, and waiver evidence needed to answer your question.
Priya | When will you update me, even if older records take longer to retrieve?
Daniel | I will update the [[service record::The service record preserves the complaint and follow-up; an update appointment does not establish a refund or completed review.]] and contact you Tuesday at fifteen hundred. If something remains missing, I will identify it. That is an update appointment, not a guaranteed account-credit date.
Priya | That gives me a clear next step. Please explain the eventual result using the correct product, period, and waiver rules.
Daniel | Agreed. The [[case resolution::Case resolution must reflect a supported outcome addressing the actual historical fee question, not merely the sending of an acknowledgment.]] will need that basis, along with applicable further-review information. For now, the fee question remains open; we have not established whether the charge stands or should be corrected.''',
    transfer_title='Check the relevant fee period',
    transfer_setup='A customer questions a $12 fee for April. The available schedule is effective from 1 July and shows $8. The April product and waiver conditions are unchecked. The next review update is Wednesday.',
    transfer='''Representative: "The disputed April charge is ___ dollars." | 12 | Twelve dollars is the actual fee in the disputed April cycle.
Customer: "The available schedule takes effect on ___." | 1 July | One July is the stated effective date, not proof of the earlier April terms.
Representative: "That schedule shows ___ dollars." | 8 | Eight dollars is the amount on the later schedule, not an established April entitlement.
Customer: "The next review update is ___." | Wednesday | Wednesday is the communication appointment, not a guaranteed fee correction.'''))
