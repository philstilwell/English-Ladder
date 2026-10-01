"""Original Legal Operations and Compliance learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='legal-operations-compliance',
    title='Legal Operations and Compliance English',
    cover_label='ENGLISH FOR EVIDENCE AND ACCOUNTABILITY',
    cover_title='Legal Operations\nand Compliance',
    cover_size=32,
    tagline='Clarify the request. Preserve the evidence.',
    audience='For legal operations specialists, compliance coordinators, contract administrators, privacy teams, and governance professionals.',
    map_intro='Eight operational conversations: complete contract intake, turn policy into a working control, answer an audit request, record an allegation, triage a privacy request, compare vendor risk, test training understanding, and report action status.',
    notes_title='Precise records. Responsible decisions.',
    notes_intro='Legal operations and compliance teams connect business requests, evidence, specialists, and authorized decisions. These conversations practice clear handoffs and careful distinctions without turning an incomplete record into a legal conclusion or a completed control.',
    field_notes=[
        ('Name the status', 'Received, assigned, reviewed, approved, signed, implemented, and verified describe different events. Use the status supported by the record and identify what must happen next.', '"The plan is approved; implementation evidence is still outstanding."'),
        ('Keep the source attached to the claim', 'Separate a reported observation, an interpretation, a document, and an established finding. Attribution makes a record fairer and more useful for qualified review.', '"The reporter says the invoice was approved early; the motive has not been established."'),
        ('Match evidence to the question', 'A current screenshot cannot automatically prove how a control operated in an earlier period. State the source, period, version, completeness, and any known gap.', '"This image shows the current setting, not the requested January-to-March operation."'),
        ('Coordinate without inventing authority', 'Make the route and next contact clear. Operational urgency does not confer legal, privacy, investigation, or risk-acceptance authority on the person receiving the request.', '"I can coordinate the review; the designated reviewer must decide the exception."'),
    ],
    scope_note='All organizations, people, policies, thresholds, cases, and timelines are fictional. This book teaches professional English, not legal advice or a complete compliance program. Follow current applicable law, actual policies, retention and preservation duties, and qualified legal or privacy guidance. Source jurisdictions differ; no example creates a universal rule, deadline, privilege, or legal conclusion.',
    sources=[
        dict(title='Corporate Legal Operations Consortium. CLOC Core 12.',
             url='https://cloc.org/cloc-core-12/',
             note='Background on legal operations roles and service delivery. The cases are original and do not reproduce the proprietary maturity assessment.', checked='1 October 2026'),
        dict(title='U.S. Department of Justice. Evaluation of Corporate Compliance Programs (September 2024).',
             url='https://www.justice.gov/criminal/criminal-fraud/page/file/937501/dl?inline=',
             note='United States prosecutorial guidance used as background on evidence and effectiveness, not a universal legal checklist or guarantee of compliance.', checked='1 October 2026'),
        dict(title='UK Information Commissioner. A Guide to Subject Access.',
             url='https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/subject-access-requests/a-guide-to-subject-access/',
             note='United Kingdom guidance for terminology and careful request handling. The fictional triage exercise does not specify applicable law or statutory timing.', checked='1 October 2026'),
        dict(title='U.S. Government Accountability Office. Standards for Internal Control: The Green Book (2025).',
             url='https://www.gao.gov/greenbook',
             note='United States federal internal-control background. Fictional private-company controls and closure rules in this book are not universal legal requirements.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Contract Intake and Workflow',
    scene='Urgent is a signal, not a complete instruction',
    skill='Clarify the agreement, owner, decision need, and document status before routing a contract request.',
    brief='Ben submits request L17 with the subject Urgent contract. It lacks an agreement type, business owner, and required decision date. Attached is an unsigned vendor service proposal for a two-month, $40,000 software pilot; an earlier nondisclosure agreement is also attached. Intake coordinator Mina must establish the transaction purpose, correct parties, required documents, personal-data involvement, and actual timing. Receipt is not legal approval. The business has not confirmed who can authorize spending or sign. Mina can coordinate triage but cannot decide contract terms or promise immediate signature.',
    cast='Ben | Business requester\nMina | Legal intake coordinator',
    culture=('Clarification can be helpful under time pressure', 'A requester may hear questions as delay. Explain which missing facts let the team assign the right reviewer and distinguish a business decision deadline from a hoped-for signature. Acknowledge urgency without promising that required review can be skipped.'),
    a='''Which information is missing from intake? | Agreement type, business owner, and required decision date | Every attached document | The fact that a pilot is proposed | The quoted pilot amount | The request lacks routing essentials even though a proposal and earlier nondisclosure agreement are attached.
What does the service proposal describe? | A two-month software pilot for $40,000 | An already signed annual license | A completed legal approval | A nondisclosure agreement with no services | The attachment describes the proposed pilot, while signature and approval remain unconfirmed.
What can Mina do? | Coordinate triage and route the request | Approve legal terms without review | Sign for the business automatically | Convert urgency into spending authority | Mina's role concerns coordination, not the unconfirmed commercial or legal decision authorities.''',
    vocabulary='''intake | Receiving and organizing information needed to handle a request. | complete contract intake
matter | A legal or operational issue tracked as a defined item of work. | open a matter
triage | Assessing a request to determine its route, priority, and next action. | triage the request
business owner | The person accountable for the underlying business need. | identify the business owner
requester | The person submitting a request, not necessarily its decision-maker. | contact the requester
counterparty | The other party to the relevant agreement or transaction. | verify the counterparty
legal entity | An organization or person recognized as capable of relevant legal rights and duties. | confirm the legal entity
agreement type | The category of contract or document being requested. | identify the agreement type
NDA | Nondisclosure agreement; terms governing specified confidential information. | locate the NDA
MSA | Master services agreement; overarching terms for specified service arrangements. | review the MSA
SOW | Statement of work; a document specifying particular work and related terms. | reconcile the SOW
order form | A document setting out a particular purchase and its relevant terms. | verify the order form
contract package | The related documents that together describe the proposed arrangement. | assemble the contract package
unsigned proposal | Proposed terms that have not been signed in the supplied record. | identify an unsigned proposal
signature authority | Permission to execute the relevant agreement on behalf of a party. | verify signature authority
spend approval | Authorization to commit the relevant funds. | obtain spend approval
decision deadline | The time by which a specified decision is needed. | clarify the decision deadline
target signature date | A desired signing date whose commitment status must be clear. | qualify the target signature date
review scope | The issues and documents included in an assessment. | define the review scope
routing rule | A criterion determining where a request is sent. | apply routing rules
CLM | Contract lifecycle management; processes and systems for managing contract stages. | maintain the CLM record
version control | Management of document revisions and their status. | maintain version control
turnaround estimate | An estimate of how long a defined response or task will take. | qualify the turnaround estimate
legal approval | Approval within the defined legal review process, distinct from other authorizations. | record legal approval''',
    precision='The earlier NDA and the proposed services arrangement serve different purposes. Do not assume the NDA approves the pilot, spending, data processing, or signature. Reviewers need the relevant document package and actual parties, not an intake label alone.',
    precision_extra='The required decision date and the target signature date may differ. Acknowledgment means the request was received. Triage, legal review, commercial approval, and execution have separate statuses and authorities; a system entry does not complete all of them.',
    phrases='''Acknowledge the request | I have received L17 and the attached proposal.
Explain the missing facts | To route it correctly, I need the agreement type, business owner, and decision date.
Clarify the transaction | What services will the two-month pilot actually include?
Verify the parties | Which legal entities would enter the agreement?
Separate the documents | The earlier NDA does not replace the service documents.
Identify the owner | Who is accountable for the business need?
Check authority | Who approves the spend, and who is authorized to sign?
Clarify urgency | What decision is needed by what date, and what happens if it is delayed?
Separate two dates | Is that the review deadline or the desired signature date?
Check data involvement | Will the pilot involve personal data or access to customer systems?
Keep status accurate | The proposal is unsigned and has not completed review.
Request the package | Please include the current proposal and all referenced terms.
Avoid a turnaround promise | We need the scope and reviewer availability before confirming timing.
Route specialist questions | I will flag the data-processing details for the appropriate reviewer.
Maintain one record | Keep the current version and status in the intake record.
Close the handoff | I will confirm the route, missing items, and next contact once triage is complete.''',
    notes='''To route it correctly | Explains why the question matters to the requester's progress.
Which entities | Distinguishes legal parties from brands or informal team names.
Does not replace | Separates the roles of related contract documents.
What decision | Makes urgency specific enough to prioritize responsibly.
Has not completed | States review status without declaring the proposal unacceptable.
Once triage is complete | Sets a process boundary without promising the substantive result.''',
    d='''Which acknowledgment is accurate? | L17 is received; routing information and required approvals remain outstanding. | L17 is legally approved because the file uploaded successfully. | The old NDA authorizes the pilot spend. | The requester may sign because the request is urgent. | Receipt and document presence do not establish review, spending approval, or execution authority.
Which question clarifies timing best? | What decision is needed by which date, and how does that differ from desired signature? | Can we assume urgent means signature today? | Can we omit the date until after execution? | Does a short subject line prove the terms are standard? | A specific decision and consequence make prioritization more useful than an undefined urgency label.
What should the reviewer receive? | The current proposal, referenced terms, party details, business purpose, and relevant data information | Only the subject line | An older NDA instead of the current services documents | A rewritten summary concealing unresolved terms | The complete relevant package supports review without substituting an incomplete or misleading description.
Which distinction is necessary? | Requester, business owner, spend approver, and signer may be different roles. | Every requester is automatically the authorized signer. | Legal approval always approves the budget. | A CLM record is equivalent to an executed contract. | These roles and stages can differ, so authority must be established rather than inferred.''',
    dialogue='''Ben | I marked L17 urgent. The supplier is waiting, and the business wants the software pilot moving this week.
Mina | To complete [[intake::Intake gathers the routing information; receiving an attachment does not establish legal or commercial approval.]], I need the agreement type, business owner, and required decision date. Those details help us assign the right reviewer without unnecessary transfers.
Ben | The proposal is for a two-month pilot costing forty thousand dollars. I attached the confidentiality agreement we signed earlier as well.
Mina | Thank you. The [[NDA::The NDA concerns specified confidential information and does not automatically approve the separate pilot services arrangement.]] and the pilot services arrangement have different purposes. We need the current proposal and any referenced service terms, rather than treat the earlier confidentiality document as approval of the whole purchase.
Ben | I submitted it for Nell in operations. She owns the pilot objective, although I do not know who approves the final spend.
Mina | I will record Nell as the [[business owner::Nell owns the business need, while spending and signature authority still require separate confirmation.]] and leave the spend approver unconfirmed. The person who requests work, the person who owns the need, and the person who can authorize it are not necessarily the same.
Ben | The vendor name on the presentation is Orbit, but the proposal uses a longer company name. Does that difference matter at intake?
Mina | We need the actual [[legal entity::The legal entity identifies the proposed contracting party; a brand name may not identify that party accurately.]] for each side. Please preserve the name in the document and have the business confirm the intended parties, rather than replace a formal name with the brand from the slides.
Ben | Nell needs a decision about whether to proceed by the sixth of October at noon UTC. She hopes to sign by the ninth.
Mina | That gives us a specific [[decision deadline::The decision is needed on 6 October at noon UTC, separately from the desired 9 October signature.]] and a separate target signature date. I will record both and the business consequence of delay, but those dates do not establish reviewer availability or approval.
Ben | The pilot will use customer contact details. I am not sure whether the supplier only views them or also stores a copy.
Mina | Include that uncertainty in the [[review scope::The review scope must flag the unresolved data handling so an appropriate specialist can assess the actual arrangement.]]. The data flow and access details may affect which specialists need to review. Please do not answer stored or not stored merely to make the form look complete.
Ben | There are two versions of the proposal in the email chain. The latest changes the support arrangement, but neither is signed.
Mina | Keep clear [[version control::Version control identifies the current proposal and changes; neither unsigned revision should be presented as executed.]]. Identify the current revision and preserve the relevant history so the reviewer sees the changed support terms rather than an outdated attachment.
Ben | Once the legal team reviews it, can I send it for signature, or should I wait for another approval?
Mina | We must verify [[signature authority::Signature authority must be confirmed separately; legal review does not automatically authorize the requester to execute the agreement.]] and the other required approvals. Legal review does not automatically approve the budget or make you the signer. The actual workflow will identify the necessary sequence.
Ben | Can you at least tell the supplier that we will finish today? That would stop the reminder messages.
Mina | I cannot give that [[turnaround estimate::A turnaround estimate needs the relevant scope and reviewer capacity; supplier pressure alone does not justify today's completion promise.]] yet. I can acknowledge receipt and confirm that we are clarifying the route. Once the scope and reviewer availability are known, we can communicate a supported timing expectation.
Ben | I will get Nell's confirmation, the party details, the latest proposal, and the data-handling information into the same record.
Mina | Good. I will complete [[triage::Triage determines the appropriate route, priority, and next action without deciding the contract's substantive legal or commercial terms.]], identify the missing approvals, and confirm the next contact. We can respond to the urgency while keeping receipt, review, approval, and signature as separate statuses.''',
    transfer_title='Clarify another urgent intake request',
    transfer_setup='Request M22 attaches an unsigned services proposal. Dana owns the business need. A review decision is needed on 5 May; signature is desired on 9 May. The spend approver and authorized signer are not yet confirmed.',
    transfer='''Coordinator: "The document status is ___." | unsigned | The proposal has not been executed in the supplied record.
Requester: "The business owner is ___." | Dana | Dana owns the need, which does not automatically establish every approval authority.
Coordinator: "The decision is needed on ___." | 5 May | The review decision date differs from the desired signature date of 9 May.
Requester: "The signer remains ___." | unconfirmed | No authorized signer has been identified, so the requester cannot assume that role.''',
))


BOOK['units'].append(unit(
    title='Policy Implementation and Controls',
    scene='The policy is published, but the check has no owner',
    skill='Translate a policy requirement into an assigned, evidenced process without confusing publication with operation.',
    brief='Fictional company policy H3 requires compliance preapproval before committing to client hospitality costing more than $100 per guest, including all charges. Other restrictions still apply at any amount. H3 was published on 1 September, but the intake check and evidence retention have no assigned operator. A proposed meal costs $960 for eight guests, with no commitment yet made. Policy owner Mara and expense operations lead Dinesh must define who checks the request, who decides, where evidence is kept, and how exceptions are escalated. The event has not been approved.',
    cast='Mara | Compliance policy owner\nDinesh | Expense operations lead',
    culture=('Published does not mean embedded in daily work', 'A team may believe compliance is complete because a document has been distributed. Ask how a real request moves through the process. Distinguish the person maintaining the policy from the person operating the check and the person making the approval decision.'),
    a='''What triggers the stated H3 preapproval requirement? | More than $100 per guest before commitment | Exactly $100 or less in every case | Only events costing more than $1,000 in total | Publication of a new policy regardless of any event | H3 uses a per-guest threshold above one hundred dollars and requires approval before commitment.
What is the proposed cost per guest? | $120 | $100 | $960 | $80 | Nine hundred sixty divided by eight equals one hundred twenty dollars per guest.
What is missing from implementation? | An assigned check operator and evidence-retention arrangements | The existence of any policy | The proposed guest count | Confirmation that the event is already approved | H3 has been published, but the operational ownership and evidence arrangements remain undefined.''',
    vocabulary='''policy | An organization's stated rule or principle for decisions and behavior. | publish a policy
procedure | The defined steps for carrying out a task or requirement. | implement a procedure
control | An action or arrangement designed to address a specified risk or objective. | operate a control
control objective | The intended result of a control. | define the control objective
policy owner | The role responsible for maintaining and interpreting a policy through the authorized process. | identify the policy owner
control operator | The person performing the defined control activity. | assign the control operator
approver | A person authorized to make the relevant approval decision. | verify the approver
preventive control | A control intended to stop an unwanted event before it occurs. | design a preventive control
detective control | A control intended to identify an event or condition after or as it occurs. | operate a detective control
trigger | The condition that requires a defined action. | specify the control trigger
threshold | A boundary used by a rule or decision criterion. | apply the threshold
preapproval | Required approval before the specified action or commitment. | obtain preapproval
commitment | An undertaking or obligation whose relevant meaning depends on the context. | verify commitment status
control evidence | Records supporting whether and how a control was performed. | retain control evidence
evidence repository | The approved location for maintaining supporting records. | use the evidence repository
retention rule | A requirement governing how long and under what conditions records are kept. | follow retention rules
exception | A departure from a defined requirement, subject to the relevant process. | escalate an exception
override | An authorized or unauthorized bypass of a normal control, with status specified. | review control overrides
segregation of duties | Allocation of incompatible responsibilities to different roles where required. | assess segregation of duties
design effectiveness | Whether a control is suitably designed to address its objective. | assess design effectiveness
operating effectiveness | Whether a control works as intended in practice over the relevant scope. | test operating effectiveness
control frequency | How often or upon what events a control is performed. | define control frequency
implementation gap | A difference between a requirement and its practical deployment. | close the implementation gap
issue escalation | Raising an unresolved problem to the appropriate authority. | document issue escalation''',
    precision='The proposed meal is $960 divided by eight, or $120 per guest, so it exceeds the stated H3 threshold. That triggers review; it does not guarantee approval. Costs at or below $100 are not automatically acceptable because other restrictions still apply.',
    precision_extra='A document, a workflow design, and evidence of a completed check are different things. Publication confirms that H3 is available. Operating effectiveness requires evidence of how the relevant checks actually function, not only the existence of a policy file.',
    phrases='''State the gap | The policy is published, but the check has no assigned operator.
Name the objective | The control should prevent commitments that lack required preapproval.
Apply the correct basis | The threshold is per guest, including all charges.
Show the calculation | Nine hundred sixty divided by eight is one hundred twenty.
Separate trigger and decision | That amount requires review; it does not mean the event is approved.
Keep other rules visible | Below-threshold spending may still be subject to other restrictions.
Assign the activity | Who checks the request before a commitment is made?
Separate the decision | Who has authority to approve or reject the request?
Specify the evidence | Retain the request, calculation, decision, reviewer, and timing.
Check timing | The evidence must show that required approval preceded the commitment.
Choose the repository | Store the records in the approved location under the applicable retention rules.
Handle absence | Who covers the check when the usual operator is unavailable?
Avoid bypassing the rule | Do not split one event to disguise the amount.
Route uncertainty | Send an unclear case to the designated policy reviewer.
Test the process | Walk a real request through the steps and verify the retained evidence.
Close accurately | The design can be assigned now; actual operation still needs verification.''',
    notes='''Per guest | Makes the threshold basis explicit instead of substituting the total.
Requires review | Distinguishes the trigger from a favorable decision.
Before | Defines the sequence that makes this a preventive check.
Who covers | Makes continuity part of the operational design.
Actual operation | Focuses on performed work rather than the existence of documentation.
Still needs verification | Prevents a design decision from becoming an unsupported effectiveness claim.''',
    d='''Which status statement is accurate? | H3 is published, but the control is not yet fully assigned or evidenced. | Publication proves every event has been checked. | A policy owner automatically performed all past checks. | The proposed meal is approved because its total is below $1,000. | Publication does not establish operational ownership or completed checks, and H3 uses a per-guest basis.
Which event statement matches the rule? | The $120-per-guest proposal requires preapproval before commitment. | The $960 total may be divided into smaller claims to avoid review. | Eight guests make the threshold irrelevant. | Approval can be assumed because no booking exists yet. | The per-guest cost exceeds the stated threshold, and the absence of commitment preserves the required review sequence.
Which evidence is most useful? | The identified request, calculation, authorized decision, and timestamps showing the sequence | Only a link to the policy | An undated statement that staff generally follow rules | A receipt with no approval record or timing | The linked records allow review of both the decision and whether it occurred before the relevant commitment.
What does a well-written procedure prove by itself? | The designed steps, not that they operated effectively in practice | Every future event will comply | All historical evidence exists | No exception can ever occur | Design documentation explains the intended process, while operation and effectiveness require separate evidence.''',
    dialogue='''Dinesh | We uploaded H3 last month and emailed everyone. The dashboard says the policy rollout is complete. What else is missing?
Mara | Publication is complete, but the [[control operator::The control operator performs the defined check; publishing H3 has not assigned that practical responsibility.]] is not assigned. For the next hospitality request, we need to know who checks the amount, who makes the decision, and where the evidence goes.
Dinesh | The expense team usually sees receipts afterward. This request is for a meal that has not been booked yet.
Mara | H3 requires [[preapproval::Preapproval must occur before commitment under H3; an after-the-event receipt check does not fulfill that timing requirement.]] before commitment when the cost exceeds one hundred dollars per guest. An after-the-event receipt check can identify a problem, but it cannot replace that earlier requirement.
Dinesh | The estimate is nine hundred sixty dollars for eight guests, including all charges. Someone thought the total had to exceed a thousand.
Mara | The [[threshold::H3 uses more than one hundred dollars per guest, not a thousand-dollar total-event threshold.]] is per guest. Nine hundred sixty divided by eight is one hundred twenty, so this proposal triggers compliance review. That calculation does not itself approve the event.
Dinesh | We can check the information on receipt, but my team should not be deciding whether the hospitality is permissible.
Mara | Correct. The [[approver::The approver holds the relevant decision authority, which is distinct from checking intake completeness and arithmetic.]] is the designated compliance reviewer. Your team can perform the intake check and route it, while the reviewer decides under the actual policy and relevant requirements.
Dinesh | What should the intake check record besides the amount? I want the evidence to be useful without collecting unnecessary information.
Mara | The [[control evidence::Control evidence links the request, relevant calculation, authorized decision, reviewer, and timing to the actual event.]] should connect the request, purpose, relevant parties, cost calculation, decision, reviewer, and timing. Use the approved fields and handling rules, and retain what the process actually requires.
Dinesh | Some approvals are currently scattered across personal mailboxes. That will make it difficult to show the complete sequence later.
Mara | We need an approved [[evidence repository::The evidence repository provides an authorized location for the linked records under applicable access and retention rules.]] with the appropriate access and retention rules. A policy link does not show that a specific request was checked before commitment.
Dinesh | What happens if a requester says the booking cannot wait and the usual reviewer is unavailable?
Mara | Define the [[issue escalation::Issue escalation routes urgency to the designated alternative authority; it does not grant the requester permission to bypass the control.]] and cover arrangement. Urgency does not let the requester approve their own exception or split the event into smaller claims to make the threshold disappear.
Dinesh | Should every amount below one hundred dollars be marked approved automatically?
Mara | No. That would misread the [[control trigger::The stated trigger concerns one preapproval requirement; other restrictions can still apply below the amount threshold.]]. The threshold governs this preapproval step, while other restrictions still apply at any amount. The procedure should preserve those checks rather than imply a universal permission.
Dinesh | Once we document these roles and test a sample request, can we say the control has always worked?
Mara | No. We can assess the [[design effectiveness::Design effectiveness concerns whether the proposed control addresses its objective, not proof that it operated throughout past periods.]] of the defined process. A current walkthrough does not prove how earlier requests were handled or fill missing historical evidence.
Dinesh | Then we should separate the completed publication task from the operational work still needed, and assign the expense check explicitly.
Mara | Exactly. [[Operating effectiveness::Operating effectiveness requires evidence that the control actually worked as intended within the relevant scope and period.]] needs evidence from actual operation. Let us record the operator, approver, cover route, and repository, then verify that the next requests follow the intended sequence.''',
    transfer_title='Apply another fictional preapproval rule',
    transfer_setup='Policy J2 requires review before commitment for hospitality above $80 per guest, including all charges. A proposed event costs $540 for six guests. Other restrictions still apply. No approval or booking is recorded.',
    transfer='''Coordinator: "The proposed cost per guest is ___." | $90 | Five hundred forty divided by six equals ninety dollars per guest.
Reviewer: "That exceeds the stated ___." | $80 threshold | Ninety is above eighty, so the stated preapproval trigger applies.
Coordinator: "Approval is required before ___." | commitment | The fictional rule defines a preventive sequence, not only an after-event review.
Reviewer: "The current approval status is ___." | not approved | No approval is recorded, and exceeding the threshold triggers review rather than automatic permission.''',
))


BOOK['units'].append(unit(
    title='Compliance Audits and Evidence',
    scene='A current screenshot does not answer a historical question',
    skill='Respond to an evidence request with the correct period, source, completeness, and limitations.',
    brief='Auditor Talia requests evidence of monthly privileged-access reviews for January through March 2026. Record owner Hugo locates the January and February review packages but has not found March. A colleague suggests sending a screenshot taken on 2 April showing the current access-review setting. The screenshot does not establish whether the three monthly reviews occurred. Hugo must identify the records found, disclose the March evidence gap, and continue the authorized search. He must not backdate a new record or assert that the missing package proves the March review never happened.',
    cast='Talia | Compliance auditor\nHugo | Control record owner',
    culture=('An evidence gap needs a precise answer', 'Audit questions can feel accusatory when teams are busy. Treat the requested period and record type as shared criteria. Acknowledge what is missing without becoming defensive, inventing evidence, or making a broader conclusion than the records support.'),
    a='''Which period did Talia request? | January through March 2026 | Only 2 April 2026 | Every month after April | An unspecified current day | The request concerns three named historical months rather than the current configuration alone.
Which review packages have been found? | January and February | All three requested months | Only March | None of the requested records | The brief states that two packages are located while March remains missing.
What does the April screenshot establish by itself? | The displayed current setting, not completion of all three historical reviews | Proof of every January-to-March review | Proof that March was never reviewed | A replacement original March sign-off | A current setting image does not document whether the requested historical activities actually occurred.''',
    vocabulary='''audit scope | The subjects, boundaries, and period included in an audit. | confirm the audit scope
evidence request | A request for records supporting a specified question or assessment. | clarify the evidence request
PBC list | Prepared-by-client list; an auditor's requested information schedule in relevant practice. | maintain the PBC list
review period | The time interval covered by an assessment. | state the review period
population | The complete defined set of items relevant to a test. | establish the population
sample | Selected items examined from a defined population. | explain the sample
privileged access | Access with elevated permissions under the relevant system rules. | review privileged access
review package | The linked records supporting a particular review. | assemble the review package
source record | The originating record used as evidence. | preserve source records
provenance | Information about the origin and history of an item. | document evidence provenance
timestamp | A recorded date and time for an event. | verify timestamps
metadata | Information describing a record, such as origin, dates, and version. | retain relevant metadata
contemporaneous evidence | Evidence created at or near the event it records. | locate contemporaneous evidence
retrospective account | A later description of an earlier event. | label a retrospective account
completeness | Whether all required or relevant items are included on the stated basis. | assess completeness
reliability | The extent to which information can be depended on for the intended purpose. | assess evidence reliability
relevance | The connection between evidence and the question being assessed. | assess evidence relevance
evidence gap | Missing information needed to support an assessment. | disclose an evidence gap
exception log | A record of identified departures and their handling. | reconcile the exception log
sign-off | A recorded approval or confirmation under the relevant process. | verify reviewer sign-off
reperformance | Independently carrying out a procedure to check its result. | document reperformance
redaction | Removal or obscuring of information for an authorized disclosure purpose. | document necessary redactions
audit trail | A traceable record of actions, changes, and decisions. | preserve the audit trail
management response | Management's factual reply and planned actions concerning an audit matter. | prepare the management response''',
    precision='Two located packages out of three requested months is a statement about evidence availability. It is not automatically a 66.7% control-effectiveness score. The March gap must be disclosed while the underlying activity and available alternative evidence are assessed.',
    precision_extra='A later explanation may help an investigation, but it must be labeled with its actual creation date and source. Do not recreate a missing sign-off as if it were contemporaneous. Authorized redaction should protect information without disguising a material evidence limitation.',
    phrases='''Confirm the scope | You are requesting the monthly reviews for January through March 2026.
State what is available | We have located the January and February packages.
Disclose the gap | We have not yet located the March package.
Limit the conclusion | That gap does not by itself establish whether the review occurred.
Describe the screenshot | This image was taken on the second of April and shows the current setting.
Separate configuration from operation | It does not demonstrate completion of the three monthly reviews.
Identify the source | Each package will show its originating system, reviewer, and relevant dates.
Check completeness | Let us reconcile the requested months against the evidence index.
Preserve the record | We will retain the original files and relevant metadata.
Avoid backdating | Any later explanation will carry its actual creation date.
Handle sensitive content | Use approved access and redaction procedures without concealing relevant gaps.
Continue the search | We will check the authorized repositories and record the search result.
Clarify alternatives | Would these separately identified records help assess the missing period?
Keep the limitation visible | Alternative evidence must be described for what it actually proves.
Agree a follow-up | I will provide the search status and any additional records by the agreed date.
Close accurately | The submission covers two located packages and an explicit March evidence gap.''',
    notes='''Have located | Reports availability, not a conclusion about every control outcome.
Not yet located | Distinguishes a search gap from proof that an event did not occur.
By itself | Restricts the inference available from one fact.
Actual creation date | Prevents a later record from impersonating earlier evidence.
Separately identified | Keeps alternative evidence distinct from the missing original package.
Covers | Defines the scope of the submission rather than implying completeness.''',
    d='''Which submission description is accurate? | January and February packages are available; March remains an identified evidence gap. | All three months are complete because the current setting is enabled. | March definitely failed because the package is not yet found. | A new March sign-off can be dated earlier to complete the file. | The known record availability supports a bounded description, not historical completeness or a fabricated record.
Which question best tests the screenshot's relevance? | Does this current setting image show that the requested historical reviews actually occurred? | Does the image look polished enough to replace the packages? | Can the capture date be removed to make it less confusing? | Will a smaller image prevent questions about March? | Relevance depends on the audit question and period, not presentation or concealed context.
How should a later employee explanation be handled? | Label its source and actual date and assess what it supports. | Treat it automatically as the missing original sign-off. | Backdate it to the month being discussed. | Discard all later information without considering relevance. | A retrospective account can be useful but must retain its identity and evidential limitations.
What does two packages out of three establish? | Current evidence availability for two requested months | A universal 66.7% compliance rating | Proof that every user was correctly authorized | Proof that March access was improper | Record availability alone does not calculate overall control effectiveness or establish the missing month's substantive result.''',
    dialogue='''Talia | The request covers monthly privileged-access reviews for January through March. Can you confirm which records your submission will include?
Hugo | We have located the January and February [[review packages::The located packages cover two requested months; the March package has not yet been found.]]. I have not found March yet, so I will identify that gap rather than describe the quarter as fully documented.
Talia | A colleague sent me an image of the current review setting. When was it captured, and what is it intended to show?
Hugo | The [[timestamp::The screenshot was captured on 2 April, so its current configuration view is not evidence of all earlier review events.]] is the second of April. It shows the setting visible then. It does not establish that each January-to-March review was performed or signed off.
Talia | That distinction matters. I need evidence of operation during the requested months, not only evidence that a review feature is currently enabled.
Hugo | Understood. The [[review period::The review period is January through March 2026, which determines whether the submitted records answer the request.]] remains January through March 2026. I will label the April image separately so it cannot be mistaken for a historical review record.
Talia | What is included in the two packages you have located? We need to understand how they connect to the control activity.
Hugo | Each should identify the [[source record::Source records connect the package to the originating activity and must be checked rather than inferred from a file title.]], relevant user population, reviewer, date, decision, and exceptions. I will verify those contents rather than assume a file titled completed review contains every required element.
Talia | Do you have an index showing the requested months and the status of each item?
Hugo | I am reconciling [[completeness::Completeness is checked against the defined requested items; two located files cannot silently stand for three months.]] against that list. It will show two located packages and one missing package, with any further evidence added under its own source and date.
Talia | Please be careful not to turn the missing March package into an unsupported conclusion about whether the review occurred.
Hugo | I will call it an [[evidence gap::An evidence gap identifies missing support without by itself proving that the underlying March review did not occur.]]. It means we cannot presently support the activity with that package, not that we have established the review never happened.
Talia | Someone may remember conducting it. A later explanation could be relevant, but it needs to remain distinguishable from contemporaneous evidence.
Hugo | Any [[retrospective account::A retrospective account is a later explanation and must retain its actual date and source rather than impersonate an original sign-off.]] will have its actual creation date and author. We will not recreate a sign-off and date it in March merely to make the index look complete.
Talia | Some records contain user details. Follow the approved sharing process, but make clear if any removal limits what I can assess.
Hugo | We will document necessary [[redactions::Authorized redactions protect information while preserving transparency about any effect on the evidence available for assessment.]] and use the authorized access route. We should not conceal a relevant exception or missing field under a general statement that the package was cleaned up.
Talia | What will you do next to locate the missing material or determine what other evidence exists?
Hugo | I will check the authorized repositories and preserve the [[audit trail::The audit trail records the search, sources, changes, and follow-up without altering the original evidence or its history.]] of what we find. Any alternative records will be identified separately, with an explanation of what they show and what they do not.
Talia | Then send the two packages, the index, and the search status by the agreed follow-up date. Keep the March limitation visible.
Hugo | I will make that clear in the [[management response::The management response should state the available evidence, unresolved gap, and next action rather than claim unsupported historical completion.]]. The response will distinguish current configuration, the two located monthly reviews, and the outstanding March evidence question, without backdating records or inventing an effectiveness score.''',
    transfer_title='Describe another incomplete evidence submission',
    transfer_setup='An auditor requests April, May, and June review packages. April and May are located; June is not. A screenshot dated 3 July shows the current setting. The underlying June activity remains unverified.',
    transfer='''Owner: "The requested period is ___." | April through June | The audit concerns three historical months, not only the current July setting.
Auditor: "The missing package is ___." | June | April and May are available, leaving June as the stated gap.
Owner: "The screenshot date is ___." | 3 July | The image's date identifies a later current-state view rather than a June review record.
Auditor: "The gap alone does not prove ___." | nonperformance | A missing package does not by itself establish that the underlying activity never occurred.''',
))


BOOK['units'].append(unit(
    title='Internal Investigations',
    scene='Record the concern without turning suspicion into a finding',
    skill='Attribute reported events, separate inference from observation, and route sensitive concerns for impartial review.',
    brief='Reporter Elena says that on 27 September she saw invoice V19 marked approved while its receiving field was blank. She interprets this as evidence that her manager took a payoff, but she did not see a payment to the manager. The records and transaction context have not been reviewed. Intake coordinator Noah must preserve the allegation and its source without recording the suspected motive as fact. Elena fears adverse shift changes if her manager learns of the report. The fictional process requires restricted handling, preservation referral, and assignment to an appropriate reviewer without a conflict.',
    cast='Elena | Employee making a report\nNoah | Compliance intake coordinator',
    culture=('Neutral wording is not disbelief', 'Attributing a statement protects the usefulness of the record; it does not mean the concern is unimportant. Explain that the review must distinguish what the reporter observed, what they inferred, and what the relevant evidence establishes. Do not demand that a reporter prove the entire case before accepting it.'),
    a='''What does Elena say she observed? | V19 marked approved while the receiving field was blank | A payment made directly to the manager | A completed investigation finding | A confession by the supplier | The reported observation concerns an invoice status and blank field, not a witnessed payoff.
What is the current status of the suspected motive? | An allegation or inference that has not been established | A verified fact because Elena is concerned | A formal finding of misconduct | Proof that the report must be false | The payoff interpretation is not supported by a witnessed payment or completed review in the supplied facts.
What additional concern requires recording? | Elena fears adverse shift changes after reporting. | Elena has approved the transaction. | The manager has already been found guilty. | All records may now be deleted. | The stated fear concerns possible retaliation and must remain distinct from both the transaction allegation and a proven event.''',
    vocabulary='''allegation | A claim that something occurred, not necessarily established as fact. | record an allegation
reported observation | An event or condition a person says they directly perceived. | attribute a reported observation
inference | A conclusion drawn from information rather than directly observed. | distinguish an inference
finding | A conclusion reached through an authorized assessment of evidence. | substantiate a finding
reporter | A person raising a concern through a relevant route. | acknowledge the reporter
subject | The person or matter being examined in an investigation. | identify the investigation subject
witness | A person who may provide relevant observations or information. | identify potential witnesses
corroboration | Additional evidence supporting an account or claim. | seek corroboration
contradictory evidence | Information that conflicts with a claim or interpretation. | assess contradictory evidence
chronology | A time-ordered account of relevant events. | establish a chronology
first-hand account | Information described by someone who directly experienced the event. | distinguish a first-hand account
hearsay | Information received from another person, with legal treatment depending on context. | attribute second-hand information
intake note | The initial record of a reported concern and its source. | prepare a neutral intake note
case handoff | Transfer of the relevant information and responsibility to the next authorized role. | document the case handoff
investigation scope | The defined questions and boundaries of an inquiry. | establish investigation scope
conflict of interest | A competing interest that may impair or appear to impair impartial judgment. | disclose a conflict of interest
independence | Freedom from inappropriate influence in the relevant assessment. | protect reviewer independence
need-to-know access | Access limited to people requiring information for an authorized purpose. | restrict access on a need-to-know basis
confidentiality | Controlled handling of information under applicable duties and limits. | explain confidentiality limits
anonymity | A person's identity being unknown or withheld in a specified context. | distinguish anonymity
retaliation concern | A concern about adverse treatment because of reporting or another protected activity. | record a retaliation concern
preservation | Keeping relevant information from being improperly lost or altered. | refer preservation needs
legal hold | A direction to preserve specified information for a legal matter under applicable requirements. | follow a legal hold
factual attribution | Identifying who said or supplied a statement and its evidential status. | maintain factual attribution''',
    precision='The intake note should say Elena reports seeing an approved status and a blank receiving field. A blank field does not establish that goods were never received, that approval was improper, or that a payoff occurred. Those are separate questions for review.',
    precision_extra='Confidentiality is not a promise that nobody else will learn the information. Explain authorized sharing and limits accurately. Do not promise privilege, a particular result, or absolute protection; record safety or retaliation concerns and follow the relevant escalation process promptly.',
    phrases='''Acknowledge the report | Thank you for raising the concern; I will record what you tell me accurately.
Ask about observation | What did you personally see or hear?
Separate interpretation | Which part is your conclusion about what the event meant?
Attribute the statement | You report seeing V19 marked approved with a blank receiving field.
Avoid a premature finding | The suspected payoff has not been established.
Clarify timing | When did you see the status, and which record was it?
Keep the context open | We need the transaction context before concluding why the field was blank.
Record uncertainty | I will mark that detail as unknown rather than fill it in.
Preserve relevant material | Do not alter or delete relevant records; follow the authorized preservation instructions.
Avoid unauthorized collection | Do not access another person's account or gather material outside your permission.
Explain handling | Information will be shared only through the authorized process with appropriate people.
Avoid absolute secrecy | I cannot promise that no one else will need to know.
Check impartiality | The reviewer must not have a conflict concerning the allegation.
Record a separate concern | I will record your concern about possible shift changes separately.
Avoid promising an outcome | I cannot predict the review result or any disciplinary decision.
Close the handoff | I will route the factual record and the additional concern to the appropriate reviewer.''',
    notes='''You report | Attaches the statement to its source without dismissing it.
Personally | Separates direct experience from information received from others.
Has not been established | Keeps the allegation open without declaring it true or false.
Separately | Prevents a second concern from being lost inside the initial allegation.
Authorized process | Limits handling and evidence collection to appropriate roles and permissions.
Cannot predict | Avoids promising a finding or remedy before the relevant assessment.''',
    d='''Which intake sentence is neutral and useful? | Elena reports seeing V19 approved with a blank receiving field and suspects a payoff. | The manager took a payoff and falsified every invoice. | Elena has no concern because she cannot prove a payment. | A blank receiving field establishes that no goods arrived. | The sentence preserves the reported observation and interpretation while avoiding an unsupported finding.
What should a reviewer do with alternative explanations? | Assess relevant supporting and contradictory evidence under the authorized scope. | Ignore them after the allegation is recorded. | Treat them as proof the reporter lied. | Ask the reporter to investigate secretly. | Fair assessment considers relevant evidence without prejudgment or unauthorized evidence gathering.
Which confidentiality statement is appropriate? | The report will follow restricted authorized handling, but absolute secrecy cannot be promised. | Nobody else will ever see any information. | Every report is automatically legally privileged. | All colleagues may receive the full report to offer opinions. | Controlled handling and clear limits are more accurate than absolute secrecy, automatic privilege, or broad disclosure.
How should the shift concern be handled? | Record it as a separate concern and route it through the appropriate process. | Promise no adverse action can ever occur. | Omit it because no shift change has yet happened. | Ask the implicated manager alone to decide whether the report may continue. | The concern warrants documented routing without a guarantee or a conflicted decision path.''',
    dialogue='''Elena | I saw V19 marked approved on the twenty-seventh of September, but the receiving field was blank. I think my manager is getting a payoff.
Noah | Thank you for raising it. I will separate your [[reported observation::The reported observation concerns the invoice status and blank field; it remains attributed until the relevant evidence is reviewed.]] from your interpretation. You saw the approved status and blank field. Did you personally see any payment to the manager?
Elena | No. The timing looked suspicious to me, but I did not see money change hands or a payment record.
Noah | I will record the payoff as an [[allegation::The payoff is an allegation, not an established fact or something Elena says she directly witnessed.]], not an established fact. You do not need to prove the entire concern before we receive it, but the note must be accurate about what you know.
Elena | I assumed that the blank field meant the goods had not arrived. I did not check with receiving.
Noah | That is an [[inference::A blank field does not itself establish nonreceipt; Elena inferred that meaning without confirming the receiving facts.]] we should identify. A blank field may need explanation, but it does not by itself establish nonreceipt, improper approval, or a payment to your manager.
Elena | A colleague may have seen the same screen. Should I ask them to agree with my account before you take it further?
Noah | No. Possible [[corroboration::Corroboration should come from independently assessed evidence, not from asking another person to align their account.]] should be assessed through the authorized review. You can identify a potential witness, but do not coach an account or ask someone to confirm details they did not observe.
Elena | I remember the date clearly, although I would need to check my notes for the time. I do not want to guess.
Noah | Keep that distinction in the [[chronology::The chronology should preserve known dates and uncertain times rather than inserting a guess as a precise fact.]]. We can record the date you recall and mark the time as unconfirmed. The reviewer can assess relevant records and context rather than rely on invented precision.
Elena | I have my own notes and a message about the invoice. I have not changed them or accessed anyone else's account.
Noah | I will refer the [[preservation::Preservation protects relevant existing material from loss or alteration through the authorized process, not unauthorized collection.]] needs to the appropriate team. Keep relevant material intact and follow their instructions. Do not enter another person's account or collect information outside your permissions.
Elena | Can you guarantee that my manager will never learn that I contacted you? I am worried about how this could affect my work.
Noah | I can explain our [[confidentiality::Confidentiality concerns restricted authorized handling; it is not a guarantee that no other person will need the information.]] process, but I cannot promise absolute secrecy. Information needs controlled handling by the appropriate people, and some details may need to be shared for a fair review.
Elena | The manager is close to someone on the usual review team. I am concerned that the report could go straight back to them.
Noah | We should record the possible [[conflict of interest::A possible conflict must be assessed when assigning the reviewer so the concern is not handled through an inappropriate or compromised route.]]. The assignment needs an appropriate reviewer without a conflict. I will not ask the person implicated in the report to decide whether the concern may be reviewed.
Elena | I have not had my shifts changed yet, but I fear that could happen if the manager thinks I complained.
Noah | I will record that [[retaliation concern::The fear of adverse shift changes is a separate concern, not a statement that a shift change has already occurred.]] separately and route it promptly under the relevant process. Please distinguish any later event from the fear you are describing now, and use the designated contact if something changes.
Elena | I want the invoice reviewed, but I do not want my suspicion written as something I actually witnessed.
Noah | The [[case handoff::The handoff must preserve the observation, interpretation, unknowns, and separate retaliation concern for the authorized reviewer.]] will distinguish your observation, suspected motive, unknown context, and separate concern. We cannot promise a finding or outcome.''',
    transfer_title='Keep another allegation accurately attributed',
    transfer_setup='Rosa says she saw a supplier invoice marked paid before its delivery field was completed. She suspects a personal benefit to the approver but saw no such payment. The transaction context is unreviewed.',
    transfer='''Coordinator: "Rosa's account of the screen is a ___." | reported observation | The screen account is attributed to Rosa and has not yet been independently established.
Reporter: "The suspected personal benefit is an ___." | allegation | Rosa did not witness a personal payment, so the suspected benefit is not a finding.
Coordinator: "The blank field does not prove ___." | nondelivery | Missing field completion does not by itself establish whether goods were delivered.
Reporter: "The transaction context remains ___." | unreviewed | The relevant context has not yet been assessed, so conclusions about propriety remain premature.''',
))


BOOK['units'].append(unit(
    title='Privacy Operations and Data Requests',
    scene='Recognize the request without disclosing the wrong record',
    skill='Clarify identity and requested actions, preserve receipt details, and route timing and disclosure decisions correctly.',
    brief='At 09:00 UTC on 1 October, agent Pia receives a message from an unfamiliar address signed A. Lee: Send me what you hold about me and delete my contact details. The message lacks enough information to match the person securely to an account. Privacy coordinator Wen must log the original wording and receipt time, arrange proportionate identity clarification through the approved route, and distinguish access from deletion. Applicable law, response timing, and any retention constraints need specialist confirmation. Staff must not disclose a guessed account, demand unnecessary documents, or promise automatic deletion.',
    cast='Pia | Customer service agent\nWen | Privacy operations coordinator',
    culture=('A rights request may arrive in ordinary language', 'A person may not know legal terminology or the internal team name. Recognize the substance without requiring polished English or a particular phrase. Explain why a necessary clarification protects the person, and avoid turning internal routing into a needless obstacle.'),
    a='''What two actions does the message request? | Access to information and deletion of contact details | Only a password reset | Only a marketing quote | A confirmed transfer of every account to a third party | The original wording asks both what is held and deletion of contact details, so the actions must be distinguished.
Why is identity clarification needed here? | The unfamiliar address and name do not securely identify the relevant account. | Every request must always include a passport. | Poorly phrased English invalidates all requests. | Staff are entitled to postpone any inconvenient message indefinitely. | The facts create a genuine matching uncertainty, not a universal requirement for a specific document.
What should be preserved at intake? | The original wording and 1 October 09:00 UTC receipt time | Only the date a specialist eventually opens the record | A rewritten deletion-only request | A guessed account number reported as confirmed | Accurate receipt and wording preserve the request history and support appropriate timing and scope assessment.''',
    vocabulary='''data subject | A person to whom personal information relates in relevant data-protection frameworks. | identify the data subject
personal data | Information relating to an identified or identifiable person under applicable law. | identify personal data
SAR | Subject access request; a request to exercise the relevant right of access. | recognize a SAR
DSAR | Data subject access request; another common term for a personal-data access request. | route a DSAR
right of access | A legally defined right to obtain personal information and related information, subject to applicable rules. | assess a right-of-access request
erasure request | A request to delete personal information under the relevant rules. | assess an erasure request
rectification | Correction of inaccurate or incomplete personal information under applicable rules. | route a rectification request
identity verification | Proportionate checking that the person is who they claim to be. | complete identity verification
authorized representative | A person whose authority to act for another has been established. | verify representative authority
request scope | The information or actions covered by a request. | clarify request scope
clarification | Information sought to resolve a relevant uncertainty. | request necessary clarification
proportionality | Matching the extent of an action to its legitimate need and context. | assess proportionality
data minimization | Limiting information use or collection to what is necessary for the relevant purpose. | apply data minimization
receipt timestamp | The recorded date and time the request arrived. | preserve the receipt timestamp
response deadline | The due date determined under the applicable rules and facts. | verify the response deadline
jurisdiction | The legal system or authority relevant to the matter. | confirm the applicable jurisdiction
controller | A role determining processing purposes and means under relevant data-protection law. | identify the controller role
processor | A role processing personal data on behalf of a controller under relevant law. | assess the processor role
search scope | The defined systems, records, and criteria covered by a search. | document the search scope
third-party information | Information relating to someone other than the requester. | review third-party information
exemption | A legally applicable qualification or exception requiring case-specific assessment. | assess an exemption
retention obligation | A duty to keep specified information under applicable requirements. | verify retention obligations
secure disclosure | Providing information through an appropriately protected, authorized method. | arrange secure disclosure
request log | A record of requests, actions, status, and relevant dates. | maintain the request log''',
    precision='The message contains two distinct requested actions. Recognizing an access or deletion request does not establish identity, disclosure scope, or the outcome of a deletion assessment. Preserve the original wording and avoid silently narrowing the request to make processing easier.',
    precision_extra='Identity checks should address the actual uncertainty without collecting unnecessary material. The applicable law and facts govern timing, any permitted pause, retention, and exemptions. Do not treat internal queue transfer or a clarification email as automatic authority to stop tracking the request.',
    phrases='''Recognize the substance | The message asks for access and deletion, even though it uses ordinary language.
Preserve receipt | Record the first of October at zero nine hundred UTC.
Keep the wording | Retain the original message as well as the operational summary.
State the uncertainty | We cannot yet match the sender securely to an account.
Avoid disclosure by guess | Do not confirm or send a guessed account's information.
Ask proportionately | Use the approved route to request only the information needed to resolve identity.
Explain the purpose | The clarification helps us avoid disclosing your information to the wrong person.
Separate the actions | Access and deletion need distinct assessment within the request.
Avoid a false promise | We cannot promise that every record will be deleted automatically.
Check the governing rules | The privacy team needs to confirm applicable law and response timing.
Keep the clock visible | Continue tracking dates unless the authorized assessment establishes a permitted change.
Clarify without coercion | Do not force a narrower request merely to reduce the search.
Protect other people | Any third-party information requires the appropriate review.
Verify authority | If a representative is acting, confirm their authority through the proper process.
Use an appropriate delivery route | Disclosure must follow the approved secure method after the required checks.
Close the handoff | Log the request, the uncertainty, the assigned owner, and the next action.''',
    notes='''Even though | Keeps informal wording from being mistaken for absence of a request.
Cannot yet | Identifies unresolved matching without refusing the underlying request.
Only ... needed | Limits additional collection to the relevant verification purpose.
Distinct assessment | Prevents one requested action from silently replacing the other.
Unless | Keeps timing changes dependent on an authorized, applicable basis.
After the required checks | Protects disclosure without prescribing an invented universal verification method.''',
    d='''Which initial response is appropriate? | Log both requested actions and arrange necessary identity clarification through the approved route. | Send the closest matching account immediately. | Reject the request because it does not say DSAR. | Delete all records before checking identity or retention duties. | The response recognizes the request while addressing the real identity uncertainty and preserving both actions.
Which identity approach is proportionate? | Request only information needed to resolve the actual uncertainty under the approved process. | Always demand a passport, bank statement, and full medical history. | Ask for account passwords by ordinary email. | Skip every check because the sender supplied initials. | Verification should match the actual risk and need rather than impose excessive collection or unsafe shortcuts.
Which timing statement is accurate for this case? | The applicable rules must be confirmed; internal routing alone does not establish a paused deadline. | Every clarification pauses every legal deadline worldwide. | The clock begins only when the busiest team chooses to open the file. | A receipt timestamp is unnecessary if identity is uncertain. | No applicable legal timing rule is supplied, so staff must preserve dates and obtain the correct assessment.
What should staff avoid when clarifying scope? | Silently turning the combined request into deletion only | Preserving the original wording | Recording necessary clarification | Identifying an accountable request owner | Narrowing or changing the requested action without a proper basis misrepresents what the person asked.''',
    dialogue='''Pia | This message came in at zero nine hundred UTC on the first of October. It says send me what you hold about me and delete my contact details.
Wen | Record the [[receipt timestamp::The original receipt timestamp preserves when the request arrived; later routing must not replace that history.]] and keep the original wording. It contains an access request and a deletion request, even though the person has not used our internal terminology or a legal label.
Pia | The address is unfamiliar and the signature is only A. Lee. Several accounts could match that name.
Wen | Then [[identity verification::Identity verification must resolve the genuine matching uncertainty proportionately before information is disclosed to a guessed account holder.]] needs attention through the approved route. Do not choose the nearest account or confirm its details to this sender while the match is uncertain.
Pia | Would asking for a passport settle it? I do not want the request to remain unclear for days.
Wen | Use [[data minimization::Data minimization limits additional collection to what is necessary for the verification purpose rather than demanding documents by default.]]. Request only what is necessary under the approved process to resolve the uncertainty. Formal identification is not automatically the right answer in every case, and unnecessary documents create their own handling risk.
Pia | I can explain that we need enough information to avoid sending somebody else's record. Should I ask the person to choose access or deletion?
Wen | Keep both parts of the [[request scope::The request scope includes access and deletion; neither should be silently removed or forced into a single action.]]. We may need necessary clarification, but we should not make them abandon one action because our queue is easier to manage that way.
Pia | Could we complete the access part and promise that every matching record will then be deleted?
Wen | No. An [[erasure request::An erasure request requires assessment under applicable rules, including relevant retention duties, rather than automatic deletion of every record.]] has its own assessment. Applicable requirements and retention constraints may affect the outcome. We should not promise deletion before the responsible team has reviewed what the request covers.
Pia | I have seen a one-month deadline in training material. Does that automatically apply to every request our global team receives?
Wen | We need to confirm the applicable [[jurisdiction::Jurisdiction and the relevant facts determine which legal rules apply; a remembered training example is not universal timing authority.]] and rules with the privacy team. A remembered example is not a universal rule for every person, organization, or requested action.
Pia | If I send a clarification today, can I simply mark the timer paused while we wait?
Wen | Do not assume that about the [[response deadline::Response timing and any permitted pause require the applicable legal assessment; a clarification message alone does not establish a universal pause.]]. Record the action and continue tracking dates unless the authorized assessment establishes the relevant timing treatment. An internal transfer is not permission to lose the original receipt date.
Pia | The person may ask a family member to respond for them. How would that change the next step?
Wen | We would need to establish an [[authorized representative::A representative's authority must be established through the appropriate process before treating their instructions as the person's own.]] through the proper process. A family relationship alone should not be treated as automatically proving authority to receive another person's information.
Pia | Once identity and scope are clear, the records may include messages involving colleagues or other customers.
Wen | Flag [[third-party information::Information about other people requires the appropriate disclosure assessment; recognizing access rights does not authorize indiscriminate release.]] for the appropriate review. The access request does not mean we can send an unreviewed export containing everybody else's details.
Pia | I will log the combined request, the identity uncertainty, and the referral to the privacy team without making an outcome promise.
Wen | Good. Keep the [[request log::The request log preserves the original request, dates, owner, actions, and unresolved questions so the case remains traceable.]] complete with the owner and next action. Then use the approved verification, assessment, and secure-response process while preserving what the person actually requested.''',
    transfer_title='Triage another combined data request',
    transfer_setup='A message received on 7 March at 14:20 UTC asks for a copy of personal information and correction of an address. The sender cannot yet be securely matched to an account. Applicable timing rules have not been confirmed.',
    transfer='''Agent: "The receipt time is ___." | 14:20 UTC | The original arrival time belongs in the request history even while identity remains uncertain.
Coordinator: "The second requested action is ___." | address correction | The person asks to correct an address, not to delete all information.
Agent: "Before disclosure, the account match requires ___." | identity clarification | The current information does not securely identify the relevant person and account.
Coordinator: "The applicable deadline remains ___." | to be confirmed | No governing timing rule is supplied, so staff must track the request and obtain the appropriate assessment.''',
))


BOOK['units'].append(unit(
    title='Third-Party Risk and Due Diligence',
    scene='Similar services do not necessarily create similar exposure',
    skill='Compare vendor data flows and dependencies, identify missing evidence, and communicate unresolved risk accurately.',
    brief='Two vendors propose workforce reporting services. Vendor A proposes department-level counts; Vendor B requests names, work email addresses, and individual salary records. B also uses separate hosting and support subcontractors, but their locations and access are unconfirmed. Business lead Paolo prefers B because its demonstration looked easier to use. Risk coordinator Imani must clarify the actual service need, data necessity, subcontractor roles, controls, and contractual arrangements. Neither vendor is approved. A smaller stated dataset does not prove A is risk-free, and a completed questionnaire alone does not prove B is suitable.',
    cast='Paolo | Business service owner\nImani | Third-party risk coordinator',
    culture=('Risk questions should connect to the service need', 'A business team may hear due diligence as opposition to its preferred supplier. Explain which exposure each question addresses and what evidence would help. Keep the usability benefit visible while distinguishing commercial preference from an authorized risk decision.'),
    a='''Which proposed dataset is more detailed about individuals? | B's names, work emails, and salary records | A's department-level counts as described | Both are established as identical | Neither contains any described information | B requests person-level identifiers and salary information, while A proposes counts at department level.
What is unknown about B's subcontractors? | Their locations and access | Whether B has mentioned any subcontractors | The fact that the business saw a demonstration | The names of every employee using the service | The brief identifies hosting and support subcontractors but leaves their locations and access unconfirmed.
What is the current approval status? | Neither vendor is approved. | B is approved by the demonstration. | A is automatically approved because it proposes counts. | Both are approved once a questionnaire is submitted. | The scenario explicitly leaves both approvals open pending relevant assessment.''',
    vocabulary='''due diligence | Appropriate investigation before or during a relationship to understand relevant facts and risks. | conduct vendor due diligence
business rationale | The reason a service or relationship is needed. | document the business rationale
data flow | How information is collected, moved, accessed, stored, and used. | map the data flow
data necessity | Whether information is needed for the stated purpose. | assess data necessity
purpose limitation | Restricting use to the relevant permitted purposes under applicable requirements. | define purpose limitations
subcontractor | A party engaged by a supplier to perform part of the work. | identify subcontractors
subprocessor | A further processor engaged in a processing arrangement under relevant data-protection rules. | verify subprocessor roles
fourth party | A downstream provider on which a direct supplier relies. | assess fourth-party dependencies
cross-border transfer | Movement or access to information across relevant national boundaries. | assess cross-border transfers
onward disclosure | Further sharing beyond an initial recipient. | identify onward disclosures
DPA | Data processing agreement or addendum governing specified personal-data processing arrangements. | review the DPA
contractual safeguard | A contract provision intended to address a specified risk or obligation. | assess contractual safeguards
security questionnaire | A structured set of questions about a supplier's security practices. | evaluate questionnaire responses
assurance report | A report providing an assessment within a defined scope, period, and method. | review assurance-report scope
audit right | A contractual or other right to examine specified records or practices. | clarify audit rights
incident notification | Communication about specified incidents under the applicable rules or agreement. | define incident-notification duties
retention period | The length of time information is kept under stated requirements. | verify retention periods
deletion verification | Evidence supporting that specified information was deleted as required. | request deletion verification
inherent risk | Risk considered before the specified controls or responses. | assess inherent risk
residual risk | Risk remaining after the assessed controls or responses. | describe residual risk
risk acceptance | An authorized decision to take a defined risk under the relevant framework. | document risk acceptance
remediation | Work to correct an identified weakness or issue. | track remediation
ongoing monitoring | Continuing review of relevant changes and performance after initial assessment. | plan ongoing monitoring
exit plan | Arrangements for ending the relationship and handling dependencies and data. | assess the exit plan''',
    precision='Department-level counts may reduce some exposure relative to identified salary records, but the actual fields, group sizes, combinations, access, and use still matter. Do not label a dataset anonymous or a vendor risk-free merely because the proposal uses the word aggregate.',
    precision_extra='A questionnaire is one information source, not an approval. Assess the relevant evidence, scope, period, exceptions, and actual service arrangement. Downstream access and locations can affect the assessment; an unconfirmed detail should remain an explicit gap rather than become an assumed safeguard.',
    phrases='''Acknowledge the benefit | The demonstration suggests B may be easier for the team to use.
Clarify the purpose | Which decisions does the reporting service need to support?
Compare the inputs | A proposes department counts; B requests person-level salary and contact data.
Challenge necessity | Which of those individual fields are needed for the agreed purpose?
Map the flow | Where is each field stored, accessed, and sent?
Identify downstream roles | What do the hosting and support subcontractors actually do?
Keep locations open | Their access locations are not yet confirmed.
Avoid a label shortcut | Calling the data aggregate does not by itself establish anonymity.
Assess evidence | The questionnaire is a starting point, not a completed approval.
Check scope | Does the assurance evidence cover the proposed service and current period?
Clarify safeguards | We need the relevant processing, access, retention, and notification arrangements.
Check the end of the relationship | What happens to the data and dependencies when the service ends?
Separate risk states | Assess the initial exposure and the risk remaining after verified controls.
Name the decision authority | Any risk acceptance belongs to the designated authorized role.
Monitor change | Material changes to data use or subcontractors need the agreed review.
Close the recommendation | Record the business benefit, evidence, unresolved gaps, and approval status together.''',
    notes='''Suggests | Recognizes the demonstration without treating it as complete production evidence.
Which fields | Links collection to the actual reporting purpose.
Not yet confirmed | Keeps an unknown location or access right visible.
By itself | Avoids assigning a legal or risk conclusion from one label.
Verified controls | Distinguishes claimed safeguards from assessed evidence.
Together | Prevents a favorable commercial summary from omitting unresolved risk.''',
    d='''Which comparison is justified? | B proposes more person-level data and unresolved downstream access, requiring relevant assessment. | A has zero risk because it uses the word counts. | B is unsuitable solely because it has any subcontractor. | A and B are identical because their demonstrations have similar charts. | Actual data detail and dependencies affect the assessment without proving automatic approval or rejection.
What is a useful question about salary fields? | Are they necessary for the agreed reporting purpose, and who would access them? | Can they be collected simply because the vendor requested them? | Does a colorful dashboard eliminate the need to know? | Can the business hide the fields from the risk team? | The question connects collection and access to purpose rather than assuming every requested field is justified.
How should a questionnaire be treated? | As one source to evaluate alongside relevant supporting evidence and gaps | As a universal certificate of legal compliance | As permission to ignore subcontractor access | As proof every answer has been independently tested | Questionnaire responses require contextual assessment and do not automatically verify controls or confer approval.
Who may accept an identified residual risk? | The designated authorized decision-maker under the actual framework | Anyone who liked the demonstration | The vendor's salesperson on the customer's behalf | The intake system automatically after an upload | Risk acceptance requires defined authority and a recorded basis, not commercial enthusiasm or document receipt.''',
    dialogue='''Paolo | B's demonstration was easier to use. Both vendors produce workforce reports, so I hoped the risk review could be the same for each.
Imani | Let us preserve that usability benefit while checking the [[business rationale::The business rationale defines the needed reporting outcome, which helps assess whether each vendor's proposed inputs are justified.]]. Which decisions do the reports need to support, and what information is actually necessary to make them?
Paolo | We need department-level planning. A proposes counts by department, while B asks for employee names, work emails, and individual salaries.
Imani | That makes [[data necessity::Data necessity asks whether each individual field is required for the stated department-planning purpose rather than merely requested by the vendor.]] an important question. We should ask why each person-level field is needed instead of assuming a more detailed input always produces a more suitable service.
Paolo | B also mentioned a hosting provider and a separate support company. I do not know whether support can see the underlying records.
Imani | We need the [[data flow::The data flow should identify storage, access, movement, and downstream recipients, including the unconfirmed support access.]] and access roles. A diagram should show where the information is stored, who can reach it, and what each downstream provider does with it.
Paolo | The sales team called them standard subcontractors. Does that description settle the question?
Imani | No. We need to identify each [[subcontractor::A subcontractor label does not establish actual activities, access, locations, or the appropriate data-processing role.]] and its actual role. Whether a particular party is a subprocessor under the relevant arrangement needs assessment, not an assumption from a sales label.
Paolo | We have not been told where the hosting and support activities occur. Should I put our own country in the form for now?
Imani | Leave the location unconfirmed and flag possible [[cross-border transfers::Unconfirmed storage or access locations require assessment; staff must not insert an assumed country to complete a form.]] for the appropriate review. An assumed location can distort both the risk assessment and the contractual questions that follow.
Paolo | A's proposal is simpler. Can we mark it low risk without asking anything further because it only mentions department counts?
Imani | Not automatically. Its [[inherent risk::Inherent risk still needs assessment of actual data, context, access, and use; department counts do not establish zero exposure.]] depends on the actual fields, group sizes, combinations, access, and use. Counts can reduce some exposure, but the label aggregate does not establish anonymity or remove every service risk.
Paolo | B has completed our security questions. The business wants that to count as approval so we can place the order.
Imani | The [[security questionnaire::The questionnaire is a source of vendor claims to assess, not independent proof of every control or an approval decision.]] is one source of information. We still need relevant evidence, its scope and date, any exceptions, and the actual arrangements for this service.
Paolo | What should the agreement and operational plan cover beyond the questionnaire answers?
Imani | The appropriate [[contractual safeguards::Contractual safeguards address defined obligations, but their adequacy depends on the actual service, data roles, and applicable requirements.]] and operating arrangements need review: permitted use, access, downstream providers, retention, incident communication, and what happens at exit. A document title alone does not settle those questions.
Paolo | If some uncertainty remains after those checks, can the business record it and decide whether to proceed?
Imani | Any [[risk acceptance::Risk acceptance is an authorized decision about defined remaining exposure, not permission created by an incomplete intake form.]] must follow the actual authority framework. The decision-maker needs the remaining exposure and evidence gaps, not a summary that hides them behind a favorable demonstration.
Paolo | I will request the data-flow details and field rationale, and keep both vendors unapproved until the relevant decision is made.
Imani | Good. Include [[ongoing monitoring::Ongoing monitoring checks material changes after initial assessment, including changes in data use and downstream dependencies.]] in the proposal as well. Data use and subcontractors can change after onboarding, so the relationship needs a defined review process rather than a one-time green label.''',
    transfer_title='Compare another pair of proposed services',
    transfer_setup='Vendor C proposes site-level totals. Vendor D requests named staff records and uses an external support provider whose access is unknown. Neither is approved, and the business purpose needs clarification.',
    transfer='''Coordinator: "The unresolved support issue is ___." | access | The support provider's ability to reach the records has not been established.
Owner: "We must clarify the service's ___." | business purpose | The required purpose helps determine which inputs and service features are actually necessary.
Coordinator: "Neither supplier is currently ___." | approved | The brief leaves both vendor decisions open rather than favoring one automatically.
Owner: "A site-level-total label does not prove ___." | zero risk | Data context, combinations, access, and other service risks still require assessment.''',
))


BOOK['units'].append(unit(
    title='Training, Attestations, and Culture',
    scene='Completion is not the same as understanding',
    skill='Report completion separately from understanding and explain a policy through precise, role-relevant examples.',
    brief='The learning system shows 490 completions among 500 assigned employees, or 98%. Separately, 20 volunteers answer an application question; only eight answer correctly. Fictional policy W4 requires disclosure of outside paid work before it begins, including weekend work. Disclosure is not automatic prohibition, and the review outcome depends on the actual policy process. Employees still ask whether weekend assignments count. Training coordinator Sofia and compliance adviser Ren must report the two measures accurately and improve the explanation. The volunteer group is not established as representative of all 500 employees.',
    cast='Sofia | Compliance training coordinator\nRen | Compliance adviser',
    culture=('Questions can indicate engagement, not defiance', 'People may stay silent if asking for clarification is treated as failure. Welcome questions about a concrete rule and provide accessible explanations. Keep completion reporting honest while testing whether employees can apply the policy in the situations their roles actually encounter.'),
    a='''What does the 98% figure measure? | Recorded course completion among 500 assigned employees | Verified compliant behavior by 98% of all employees | Correct answers by 98% of the volunteer group | Proof that nobody needs further explanation | Four hundred ninety divided by five hundred measures completion, not every aspect of knowledge or conduct.
How many volunteers answered correctly? | Eight of twenty | Twelve of twenty | Four hundred ninety of five hundred | Twenty of twenty | The application check reports eight correct answers in the separate twenty-person volunteer group.
What does W4 require for paid weekend work? | Disclosure before it begins | Automatic prohibition in every case | Disclosure only after payment arrives | No disclosure because it occurs on a weekend | The fictional rule explicitly includes weekend work and requires prior disclosure without establishing automatic rejection.''',
    vocabulary='''LMS | Learning management system; a platform for assigning, delivering, and recording training. | review LMS records
completion rate | The share of an assigned population meeting a defined completion condition. | calculate the completion rate
assigned cohort | The defined group required to complete a learning activity. | verify the assigned cohort
completion criterion | The condition used to mark an activity complete. | define completion criteria
attestation | A recorded statement confirming specified facts or understanding, with its meaning defined. | obtain an attestation
acknowledgment | Confirmation of receipt or awareness under the stated process. | record policy acknowledgment
knowledge check | An assessment of particular knowledge at a stated point. | administer a knowledge check
application question | A question testing use of a rule in a concrete situation. | design an application question
scenario-based assessment | An assessment using realistic situations to test defined decisions. | use scenario-based assessment
learning objective | A specific capability the instruction aims to develop. | define learning objectives
role-based training | Instruction tailored to the tasks and risks of particular roles. | deliver role-based training
job aid | A concise reference supporting a task at the point of work. | provide a job aid
plain language | Wording that the intended audience can understand and use. | explain in plain language
localization | Adaptation of material for a particular language, setting, or audience. | review localization
accessibility | The ability of people with varied needs to access and use the material. | check training accessibility
advice channel | A defined route for obtaining guidance on a question. | identify the advice channel
speak-up culture | A work environment that supports raising questions and concerns. | support a speak-up culture
knowledge gap | Missing or inaccurate understanding of specified information. | identify knowledge gaps
application gap | Difficulty applying a known rule to a real situation. | address application gaps
volunteer sample | A group whose members choose to participate. | qualify a volunteer sample
representativeness | How well a group reflects the population relevant to a conclusion. | assess representativeness
remedial learning | Targeted instruction addressing an identified learning need. | provide remedial learning
follow-up assessment | A later check of a specified learning outcome. | conduct a follow-up assessment
behavior measure | An indicator of what people actually do, distinct from attendance or reported knowledge. | define behavior measures''',
    precision='Completion is 490 divided by 500, or 98%, leaving 10 without recorded completion. The volunteer application result is eight divided by 20, or 40%. Different populations and measures prevent either percentage from replacing the other.',
    precision_extra='W4 requires prior disclosure of outside paid work, including weekends. That does not mean every disclosed activity is prohibited. A training acknowledgment, a correct answer, and actual workplace behavior are different forms of evidence; each claim needs its own basis.',
    phrases='''Name the measure | Ninety-eight percent refers to recorded training completion.
State the denominator | Four hundred ninety of five hundred assigned employees completed it.
Keep the remainder visible | Ten assigned employees lack recorded completion.
Report the separate check | Eight of twenty volunteers answered the application question correctly.
Qualify the sample | We have not established that the volunteers represent the whole workforce.
Avoid the overclaim | We cannot report ninety-eight percent compliant behavior from this measure.
State the rule plainly | Under W4, disclose outside paid work before it begins.
Address the example | Weekend work is included in that disclosure requirement.
Separate disclosure and outcome | Disclosure does not automatically mean the work is prohibited.
Explain the next route | The designated reviewer applies the actual policy process.
Welcome the question | Asking how the rule applies is a useful part of learning.
Focus the instruction | Let us practice the distinction between disclosure timing and approval outcome.
Make help available | Give employees a clear advice channel for uncertain cases.
Check accessibility | Confirm that the wording and format are usable for the intended audience.
Test the specific objective | Use a follow-up scenario to check whether the timing rule is understood.
Close accurately | Report completion, the limited application result, and the targeted follow-up separately.''',
    notes='''Refers to | Defines the claim instead of letting a percentage imply broader success.
Lack recorded completion | Describes the system evidence without assuming a reason for the missing record.
Have not established | Makes the sample limitation explicit.
Before it begins | Places the required disclosure ahead of the activity.
Does not automatically | Separates a procedural requirement from its possible outcomes.
Separately | Prevents completion and effectiveness measures from being merged into a misleading headline.''',
    d='''Which headline is supported? | Training completion is 98%; a separate volunteer check identified an application gap. | Ninety-eight percent of employees behave compliantly in every situation. | Forty percent of all employees understand every policy. | Every non-completer has deliberately refused training. | The evidence supports a completion measure and a limited separate check, not universal behavior or motive claims.
An employee plans paid weekend work. What does W4 require? | Disclosure before the work begins | Waiting until the first payment arrives | No action because weekends are outside normal hours | Automatic resignation from the outside role | The fictional rule covers weekend paid work and specifies prior disclosure, not an automatic prohibition.
What should be said about the 40% application result? | It describes eight correct answers among twenty volunteers, with representativeness unestablished. | It is the verified understanding rate of all five hundred employees. | It replaces the completion denominator. | It proves the training caused misconduct. | A volunteer result has a defined scope and cannot automatically be generalized or treated as a causal finding.
Which follow-up is most relevant? | A clear W4 example, an advice route, and a later check of the same disclosure-timing distinction | Another completion reminder with no explanation of the misunderstood rule | A demand that employees stop asking questions | Reclassification of every volunteer as non-compliant | The response targets the demonstrated application difficulty and supports questions rather than merely increasing an activity count.''',
    dialogue='''Sofia | The learning dashboard shows ninety-eight percent completion. Our summary currently says the workforce is ninety-eight percent compliant.
Ren | That overstates the [[completion rate::The completion rate is 490 of 500 assigned employees, not a verified rate of compliant workplace behavior.]]. Four hundred ninety of five hundred assigned employees completed the course. It does not measure every person's understanding or behavior in the situations covered by the policy.
Sofia | Ten people do not have a completion record. I will check the assignments and any approved exceptions rather than assume they refused.
Ren | Good. Keep the [[assigned cohort::The assigned cohort defines the completion denominator, while missing records and approved exceptions need accurate status handling.]] and completion criteria clear. We should know who was assigned and what the system counts as complete before drawing conclusions from the percentage.
Sofia | The separate application check was less reassuring. Eight of twenty volunteers answered the outside-work question correctly.
Ren | That is forty percent in the [[volunteer sample::The volunteer sample contains twenty self-selected participants and is not established as representative of all assigned employees.]]. It identifies a concern worth addressing, but it does not establish that forty percent of the whole workforce understands the policy or that everyone else has failed.
Sofia | Most questions were about paid weekend assignments. People thought the disclosure rule only concerned work during their normal hours.
Ren | Then the [[application gap::The application gap concerns whether the prior-disclosure rule includes paid weekend work, rather than course attendance alone.]] is specific. W4 requires disclosure of outside paid work before it begins, including weekends. We can explain that plainly without adding a rule that all outside work is prohibited.
Sofia | The course includes an acknowledgment at the end. Could we use that as evidence that everyone accepted the exact meaning of every example?
Ren | An [[acknowledgment::An acknowledgment records the stated confirmation; it does not automatically prove understanding of every example or compliant conduct.]] means what its wording and process establish. It is not automatic evidence of correct application in every situation, especially when the follow-up questions show a particular misunderstanding.
Sofia | I want a short reminder staff can use when a paid assignment is offered. The full policy is difficult to navigate on a phone.
Ren | A [[job aid::A job aid can support the task by stating the disclosure trigger, timing, and advice route without replacing the governing policy.]] can state the trigger, timing, and advice route. It should point to the current policy and avoid simplifying disclosure required into activity forbidden.
Sofia | Some roles rarely face this issue, while others receive outside-work offers regularly. We should not assume one long module fits them equally.
Ren | Use [[role-based training::Role-based training adapts examples to relevant tasks and risks while preserving the actual policy requirement.]] with relevant examples. Keep the rule consistent, but make the situations recognizable to the employees who need to apply it.
Sofia | A few employees hesitate to ask because they think a question will be treated as evidence that they did something wrong.
Ren | We need a credible [[advice channel::The advice channel gives employees a clear route for questions and should not treat a request for guidance as automatic misconduct.]]. Asking before acting can help the policy work. We should not train people to hide uncertainty merely to preserve a clean-looking dashboard.
Sofia | I will review the wording and format as well. Some of the examples rely on expressions that are hard for multilingual teams to interpret.
Ren | Check [[accessibility::Accessibility includes usable wording and format for the audience; a recorded completion does not prove the material was readily understood.]] and localization with the intended audience. Completion in the system does not prove that the language or format made the requirement easy to understand.
Sofia | After the revised example, we can ask another fixed scenario about when disclosure is needed and what disclosure does not automatically mean.
Ren | That [[follow-up assessment::The follow-up assessment checks the specific timing and outcome distinction rather than substituting another attendance count for understanding.]] matches the objective. Report completion, the limited application result, and the targeted next check separately, then assess whether the actual misunderstanding has been reduced.''',
    transfer_title='Report another training result precisely',
    transfer_setup='A course has 285 completions among 300 assigned employees. A separate group of 30 volunteers answers one application question; 18 answer correctly. The group is not established as representative.',
    transfer='''Coordinator: "The completion rate is ___." | 95% | Two hundred eighty-five divided by three hundred equals ninety-five percent.
Adviser: "The number without recorded completion is ___." | fifteen | Three hundred minus two hundred eighty-five leaves fifteen assigned employees.
Coordinator: "The volunteer correct-answer rate is ___." | 60% | Eighteen divided by thirty equals sixty percent for that separate group.
Adviser: "Generalizing that result requires assessing ___." | representativeness | A volunteer result does not automatically describe the entire assigned population.''',
))


BOOK['units'].append(unit(
    title='Governance, Reporting, and Risk Committees',
    scene='An approved plan is not a closed action',
    skill='Report action status, remaining exposure, and requested decisions against explicit closure criteria.',
    brief='On 1 October, committee action G12 appears as complete because its remediation plan was approved on 12 September. Its due date was 30 September. The fictional closure rule requires implementation evidence and independent verification; neither is available. Action owner Owen has requested 15 October as a new due date, but no extension is approved. Risk coordinator Sara must correct the status for the 7 October committee meeting, preserve the history, and identify the decision needed. Approval of a revised date would not itself prove implementation or accept all remaining risk.',
    cast='Owen | Remediation action owner\nSara | Risk committee coordinator',
    culture=('Accurate bad news is usable management information', 'An overdue action can be uncomfortable to report, especially after a visible milestone has been achieved. Credit the approved plan while keeping the unfinished evidence visible. A clear status enables a real decision; a reassuring label can hide the very issue the committee needs to address.'),
    a='''Why was G12 marked complete? | The plan was approved on 12 September. | Implementation and independent verification were both completed. | The committee approved an extension to 15 October. | The due date was removed from the record. | The tracker confused plan approval with the separate closure requirements.
What evidence is needed for closure under the stated rule? | Implementation evidence and independent verification | Only a newly proposed date | Only the approved plan | Only the action owner's preferred status label | The fictional closure rule requires both implementation support and independent verification.
What is the status of 15 October? | Requested but not approved | The original deadline | An already approved extension | The date independent verification was completed | Owen has requested the new date, but no authorized extension is recorded.''',
    vocabulary='''governance | The structures and processes for direction, oversight, and accountability. | support effective governance
committee charter | A document defining a committee's purpose, scope, and authority. | review the committee charter
terms of reference | The agreed purpose, responsibilities, and operating boundaries of a body or task. | confirm terms of reference
quorum | The participation requirement for a body to conduct specified business under its rules. | verify quorum
decision rights | The allocation of authority to make particular decisions. | clarify decision rights
delegated authority | Decision power assigned within specified limits. | verify delegated authority
action owner | The person responsible for delivering a defined action. | identify the action owner
risk owner | The person accountable for managing a specified risk under the framework. | identify the risk owner
closure criterion | A condition required to mark an action closed. | apply closure criteria
implementation evidence | Records showing that the planned change has actually been put into effect. | verify implementation evidence
independent verification | Assessment by an appropriately separate reviewer under the relevant requirements. | obtain independent verification
residual exposure | The risk remaining after the relevant measures are assessed. | describe residual exposure
proposed extension | A requested change to timing that has not yet been approved. | record a proposed extension
approved extension | A timing change authorized through the relevant process. | document an approved extension
overdue action | An action whose applicable due date has passed without completion. | report overdue actions
status date | The date as of which a status report is accurate. | state the status date
risk appetite | The broad amount or type of risk an organization is willing to take under its framework. | define risk appetite
risk tolerance | Specified acceptable boundaries around relevant risk or performance measures. | monitor risk tolerance
KRI | Key risk indicator; a defined measure used to monitor risk conditions. | interpret a KRI
risk register | A record of identified risks, ownership, assessment, and responses. | maintain the risk register
mitigation plan | Proposed actions intended to reduce a specified risk. | approve a mitigation plan
decision log | A record of decisions, authority, reasons, and relevant conditions. | maintain the decision log
exception reporting | Reporting departures from stated criteria or expectations. | provide exception reporting
escalation threshold | A defined condition requiring referral to a higher or different authority. | apply escalation thresholds''',
    precision='As of 1 October, the 30 September due date has passed and no approved extension exists. G12 therefore remains open and overdue under the supplied facts. The 15 October request must remain labeled proposed until the authorized process decides it.',
    precision_extra='Approving a plan, changing a date, verifying implementation, and accepting risk are separate decisions. Do not report a percentage complete without a defined measurement basis. A later approved extension should preserve the original due date and decision history rather than erase the earlier status.',
    phrases='''State the reporting date | This status is as of the first of October.
Credit the completed milestone | The remediation plan was approved on the twelfth of September.
Keep closure separate | Plan approval does not satisfy the closure criteria.
Name the missing evidence | Implementation evidence and independent verification are outstanding.
Correct the label | The action remains open and overdue against the thirtieth of September deadline.
Qualify the new date | The fifteenth of October is requested, not approved.
Preserve history | Keep the original deadline and the reason for each status change.
Ask for the actual decision | The committee needs to consider the extension request through its authority process.
Separate authority | A date change does not automatically accept the remaining risk.
Avoid an unsupported score | We have no defined basis for calling the action ninety percent complete.
Identify ownership | Owen owns delivery of the action; the risk owner addresses the remaining exposure.
State the impact | Explain what remains exposed while the action is unverified.
Define verification | The independent reviewer must assess the required implementation evidence.
Record conditions | Any decision should identify its scope, owner, conditions, and date.
Escalate appropriately | Use the actual escalation threshold and committee mandate.
Close the report | Show the achieved milestone, missing evidence, current deadline, and requested decision together.''',
    notes='''As of | Fixes the date to which the status applies.
Outstanding | Identifies unfinished evidence without pretending a plan is implementation.
Against | States which deadline is used to judge lateness.
Requested, not approved | Distinguishes a proposal from an authorized timing change.
Does not automatically | Prevents one decision from silently conferring broader authority.
Together | Keeps progress and unresolved exposure visible in the same report.''',
    d='''Which 1 October status is accurate? | Open and overdue; plan approved, implementation and verification evidence outstanding. | Complete because the plan was approved. | On time because 15 October has been requested. | Independently verified because the owner attended the meeting. | The original deadline has passed and neither closure evidence nor an approved extension is available.
What would an approved extension establish by itself? | An authorized timing change under its stated conditions | Completed implementation | Automatic acceptance of every legal or operational risk | Independent verification of the control | A timing decision does not substitute for execution, evidence, verification, or separate risk authority.
Which record should be retained if timing changes? | The original deadline, extension decision, authority, reason, and new conditions | Only the newest date with all prior entries deleted | An earlier approval date invented to remove lateness | A complete label without supporting evidence | A traceable decision history explains both the original status and the authorized change.
What should the committee paper request? | The specific extension decision and any separate action needed for remaining exposure | Approval of an undefined statement that everything is fine | Retroactive proof that evidence was already supplied | Closure solely to improve the overdue count | A decision-ready paper identifies the actual request and keeps unresolved evidence and risk questions visible.''',
    dialogue='''Owen | G12 is marked complete in the tracker. The plan was approved on the twelfth of September, so I assumed we could close the action.
Sara | The [[closure criteria::The stated closure criteria require implementation evidence and independent verification, not merely an approved remediation plan.]] require implementation evidence and independent verification. Neither is available yet. We can record the approved plan as a completed milestone without treating the whole action as closed.
Owen | The original date was the thirtieth of September. I requested the fifteenth of October because the implementation work is taking longer.
Sara | That is a [[proposed extension::The requested 15 October date remains proposed because no authorized extension decision has been recorded.]], not an approved one. As of the first of October, the applicable deadline is still the thirtieth of September, so the action is open and overdue.
Owen | I do not want the committee to think no progress has been made. The plan took substantial work and has the necessary approval.
Sara | The [[status date::The status date fixes the report at 1 October, when plan approval exists but the original deadline has passed without closure evidence.]] lets us be precise. We will show the achieved milestone and the outstanding evidence together. Accurate overdue reporting does not erase the work already completed.
Owen | Can I describe it as ninety percent complete? That might communicate that the plan is nearly ready to deliver.
Sara | Not without a defined basis. [[Implementation evidence::Implementation evidence must show the change actually operating or deployed as required; an unsupported completion percentage cannot replace it.]] needs to show the actual change required by the action. A persuasive percentage is not a substitute for the records the closure rule specifies.
Owen | I can provide the deployment records when they are ready. Who then decides whether they meet the requirement?
Sara | The designated reviewer performs [[independent verification::Independent verification requires the appropriately separate reviewer to assess the required evidence rather than accept the owner's completion label.]]. We need that assessment recorded, including any exceptions, rather than assume your submission automatically proves the action can be closed.
Owen | For the seventh of October meeting, I want the committee to approve the revised date. What else should the paper make clear?
Sara | It should explain the remaining [[residual exposure::Residual exposure describes the risk still present while implementation and verification remain unresolved, not an assumed benefit from plan approval.]] and the effect of delay. The risk owner needs that information, alongside your delivery plan, rather than only a request to make the overdue label disappear.
Owen | If the committee agrees to the new date, would that count as accepting the remaining risk until then?
Sara | We must check the [[decision rights::Decision rights determine who may extend timing or accept risk; one approval does not automatically authorize the other.]]. A timing extension and risk acceptance are different decisions. The committee's mandate and any delegated authority determine what it can actually decide.
Owen | I will keep myself listed as the delivery owner, but the business risk owner should speak to the consequences and any interim measures.
Sara | Correct. The [[action owner::The action owner delivers the defined work, while risk ownership and authorized acceptance may belong to different roles.]] and risk owner can have different responsibilities. Naming one person on the tracker does not automatically transfer every decision or accountability to them.
Owen | Once a decision is made, should we replace the old date with the new one so the report looks current?
Sara | Update the current field while preserving the [[decision log::The decision log preserves the original deadline and the authorized change, including its reason, authority, date, and conditions.]]. Retain the original deadline, the request, and any authorized decision with its reasons and conditions. Do not rewrite the history to imply the action was never overdue.
Owen | Then the paper will show plan approved, evidence outstanding, overdue as of the first, and the requested fifteenth-of-October extension.
Sara | Yes. That is useful [[exception reporting::Exception reporting makes the departure from the deadline and closure criteria visible so the committee can make the actual required decision.]]. The committee can assess the actual request and remaining exposure, and we can close G12 only when the required evidence and verification support closure.''',
    transfer_title='Report another action against its closure rule',
    transfer_setup='Action K09 was due on 10 June. As of 12 June, its plan is approved but required implementation evidence and independent verification are missing. A 25 June extension has been requested but not approved.',
    transfer='''Coordinator: "The status date is ___." | 12 June | The report describes the position as of 12 June, after the original due date.
Owner: "The current action status is ___." | open and overdue | The due date has passed, closure evidence is missing, and no extension is approved.
Coordinator: "The twenty-fifth of June is a ___." | proposed extension | A requested date does not become the applicable deadline before authorization.
Owner: "Closure also requires ___." | independent verification | The stated closure rule requires verification as well as implementation evidence, not only plan approval.''',
))
