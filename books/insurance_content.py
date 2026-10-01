"""Original learner-book content for insurance workplaces."""
from books.authoring import unit

BOOK = dict(
    slug='insurance', title='Insurance English',
    cover_label='ENGLISH FOR INSURANCE PROFESSIONALS',
    cover_title='Insurance', cover_size=38,
    tagline='Explain the wording. Establish the facts. Keep the decision clear.',
    audience='For underwriting, claims, brokerage, actuarial, and customer-service teams.',
    map_intro='Eight insurance exchanges: complete an underwriting submission, explain policy documents, request claim information, communicate a pending coverage review, compare renewal terms, record investigation concerns, interpret claim-cost changes, and answer a fee complaint.',
    notes_title='Distinguish information, interpretation, and authority',
    notes_intro='Insurance conversations depend on precise status words. A quote is not necessarily bound cover, a reserve is not a settlement promise, and a reported concern is not an established finding. These cases practice keeping those distinctions understandable.',
    field_notes=[
        ('Ask for the missing fact', 'Identify the exact information needed and its purpose. Do not convert an empty field into a favorable answer, and do not ask a client to guess dates or amounts merely to complete the form.', '"The loss-history field is blank; that does not establish that there were no losses."'),
        ('Read documents together', 'Summaries and declarations help locate information, but the applicable wording, endorsements, conditions, and exclusions matter. Avoid treating a convenient heading as a complete coverage decision.', '"The summary is not the complete policy; we need the applicable endorsement too."'),
        ('Separate estimates from commitments', 'A reserve, quote, review appointment, and payment decision have different meanings. Name the status and the person or process with authority to change it.', '"The review is pending; no coverage decision or payment commitment has been made."'),
        ('Compare like with like', 'Premium changes do not describe every change in protection. Claim counts need exposure context, and average claim costs need a consistent basis. State the assumptions before presenting the comparison.', '"The premium is lower, but the deductible is higher; the terms are not identical."')],
    scope_note='All insurers, policies, claims, people, figures, and local procedures are fictional. This is professional-English practice, not insurance, actuarial, legal, financial, or claims-handling advice. Actual wording, authority, notice requirements, privacy obligations, and complaint rights depend on the policy and applicable jurisdiction. No example binds coverage, determines a real claim, or prescribes an investigation.',
    sources=[
        dict(title='National Association of Insurance Commissioners. Understanding Your Homeowners or Renter\'s Policy.', url='https://content.naic.org/article/consumer-insight-understanding-your-homeowners-or-renters-policy', note='Background for policy sections, endorsements, deductibles, and premiums. All teaching policies are invented; no actual coverage is interpreted.', checked='1 October 2026'),
        dict(title='National Association of Insurance Commissioners. Insurance Fraud.', url='https://content.naic.org/insurance-topics/insurance-fraud', note='Background for suspicion, referral, and findings. The original case teaches objective language, not investigation methods or a legal test.', checked='1 October 2026'),
        dict(title='Actuarial Standards Board. ASOP No. 53: Estimating Future Costs for Prospective Property/Casualty Risk Transfer and Risk Retention.', url='https://www.actuarialstandardsboard.org/asops/estimating-future-costs-prospective-propertycasualty-risk-transfer-risk-retention/', note='Background for estimates, assumptions, and pricing components. The fictional calculations are not actuarial indications for a real portfolio.', checked='1 October 2026'),
        dict(title='National Association of Insurance Commissioners. How to File a Complaint.', url='https://content.naic.org/consumer/how-to-file-complaint', note='Background for complaint records and state-specific routes. The fictional conversation creates no universal deadline, remedy, or restriction on rights.', checked='1 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Underwriting and Risk Selection',
    scene='An incomplete submission cannot establish the risk',
    skill='Request material missing information while preserving the difference between review, quotation, and binding.',
    brief='Broker Lena submits an application for Atlas Services, describing its activity only as maintenance. The application omits operating locations and the requested three-year loss history. Underwriter Theo does not know whether the work is performed at a workshop, at customer premises, or both. No quote, binder, or coverage confirmation has been issued. Lena will obtain the activity breakdown, location details, and loss records, and give Theo a status update Monday at 11:00. Atlas wants cover urgently, but neither the requested start date nor a complete submission automatically establishes acceptance or coverage.',
    cast='Lena | Insurance broker\nTheo | Underwriter',
    culture=('Be specific without sounding obstructive', 'A broker under time pressure may hear more information required as a refusal. Identify the missing fields and why they matter to the review. Offer a concrete next contact while avoiding a promise that complete paperwork will produce a particular underwriting outcome.'),
    a='''Which information is missing? | Operating locations and the requested three-year loss history | The applicant's name | Every description of any activity | An already issued binder | The application names Atlas and says maintenance, but omits the location details and requested loss history.
What does the blank loss-history field establish? | The information is missing. | No losses occurred. | Three claims were paid. | Coverage has already been declined. | A blank field provides no confirmed loss history and cannot be treated as a no-loss declaration.
What is committed for Monday at 11:00? | A submission-status update | Guaranteed coverage inception | An accepted quote | A completed claim settlement | Lena promises a status update, not underwriting acceptance or the start of coverage.''',
    vocabulary='''underwriting | Assessment and selection of risk under an insurer's applicable process. | complete underwriting review
submission | Information supplied for an insurance assessment or quotation. | prepare an underwriting submission
applicant | The person or organization requesting insurance. | identify the applicant
business activity | The operations performed by the applicant. | describe the business activity
risk appetite | The types and characteristics of risk an insurer is prepared to consider. | assess fit with risk appetite
exposure | A condition or measure associated with the possibility of insured loss. | identify the exposure
operating location | A place where the business carries out its activities. | list operating locations
premises | Buildings or land occupied or used for an activity. | describe the premises
off-site work | Work performed away from the business's own location. | disclose off-site work
loss history | A record of prior losses or claims over a stated period. | obtain the loss history
loss run | A report listing claims and related information for a defined account and period. | request a loss run
valuation date | The date at which reported amounts or claim statuses are evaluated. | state the valuation date
risk selection | Deciding which risks to accept under the relevant criteria. | support risk selection
referral | Escalation to a person or level with the required authority. | make an underwriting referral
underwriting authority | The defined power to make specified underwriting decisions. | confirm underwriting authority
quote | Proposed insurance terms subject to their stated conditions and status. | issue a quote
binder | A document or agreement providing temporary insurance as applicable to its terms. | confirm the binder terms
inception date | The date on which insurance begins under the applicable agreement. | verify the inception date
subjectivity | A stated requirement attached to a proposed underwriting arrangement. | identify an underwriting subjectivity
material information | Information relevant under the applicable decision or disclosure framework. | request material information
occupancy | The use of premises relevant to a property-risk assessment. | describe the occupancy
risk engineering | Technical assessment of risk conditions and controls. | request risk engineering input
declination | A decision not to offer the requested insurance. | communicate a declination
submission completeness | Whether the requested submission information has been supplied. | check submission completeness''',
    precision='A complete submission is not the same as an acceptable risk, a quote, or bound insurance. Preserve the stage of the process. The urgency of a requested inception date does not itself create coverage.',
    precision_extra='Loss information needs a defined period and reporting basis. Missing records do not establish no losses. A loss run may show paid amounts, outstanding estimates, and status at a valuation date rather than a final outcome.',
    phrases='''Specify the missing information | We still need the operating locations and three-year loss history.
Clarify the activity | Does maintenance mean workshop work, customer-site work, or both?
Avoid a favorable assumption | A blank loss-history field does not mean no losses.
Name the information period | Please supply the requested three-year records.
Check the reporting basis | Include the loss run's valuation date.
Explain the purpose | These details are needed to assess the risk presented.
Separate the stages | Completing the submission does not guarantee acceptance.
Avoid a coverage promise | No quote, binder, or coverage confirmation has been issued.
Recognize urgency | I understand that the requested start date is important.
Keep the date accurate | A requested inception date is not a confirmed inception date.
Name the follow-up | Lena will obtain the activity and location breakdown.
Give a concrete contact | We will update the submission status Monday at 11:00.
Limit the commitment | That is an update time, not a promise of bound cover.
Check authority | Any decision must follow the applicable underwriting authority.
Preserve uncertainty | We have not established where all the work takes place.
Close the handoff | Send the missing records with their period and source clearly identified.''',
    notes='''Still need | Identifies an outstanding requirement without implying a refusal.
Does this mean | Requests clarification instead of selecting an unsupported interpretation.
No losses versus no records | Different factual statements that must not be substituted.
Requested versus confirmed | Distinguishes a desired date from an established agreement.
Complete versus accepted | Distinguishes information status from the underwriting decision.
Issued | Requires an actual document or decision, not an intention.''',
    d='''Which request is most useful? | Please provide the operating locations, activity breakdown, and three-year loss records. | Send something that makes the business look safe. | Mark no losses because the field is blank. | Choose whichever activity gives the lowest price. | The useful request identifies specific missing facts without encouraging unsupported or misleading answers.
Which statement improperly promises coverage? | Cover begins Monday because that is when the update is due. | No binder has been issued. | The application remains under review. | The start date is requested, not confirmed. | The Monday commitment concerns information and does not establish coverage or underwriting acceptance.
What does supplying all requested records accomplish by itself? | It addresses submission completeness, not automatic acceptance. | It automatically binds every requested risk. | It eliminates every possible exposure. | It forces the insurer to offer the lowest premium. | Information completeness is a review milestone and does not itself determine the underwriting outcome.
Why ask for a loss run's valuation date? | Reported claim amounts and statuses relate to a stated evaluation date. | It always equals the future policy inception date. | It proves every claim is permanently closed. | It replaces the requested three-year history. | The valuation date provides context for the reported claim information rather than a universal final outcome.''',
    dialogue='''Lena | Atlas needs cover quickly. The application says maintenance, but I can see the operating-location fields and three-year loss-history section are incomplete.
Theo | We need a clearer [[business activity::Business activity describes the actual operations; the broad word maintenance does not establish where or how Atlas works.]] description first. Does the work happen in a workshop, at customer premises, or both? We cannot choose one simply because the label sounds familiar.
Lena | I will obtain a breakdown from the client. The blank history field should not be treated as a statement that no losses occurred.
Theo | Correct. Request the [[loss history::Loss history records prior losses over a stated period; an empty application field supplies no such evidence.]] for the specified three years. Missing information is not a favorable answer. We need the actual record and any relevant explanation of its coverage or limitations.
Lena | The client may have records from its previous insurer. I will ask what period they cover and whether the reported amounts are current.
Theo | If a [[loss run::A loss run supplies claim information for an account and period; its evaluation date and contents still need to be understood.]] is available, include its valuation date. Claim amounts and statuses can change. We should know the basis of the record rather than treat every figure as a final settled amount.
Lena | Atlas also has a storage address. I do not yet know whether work is performed there or whether it is only used for supplies.
Theo | Clarify each [[operating location::Operating location identifies where activities occur; a storage address does not by itself establish the work performed there.]] and its use. An address alone does not tell us the occupancy or whether there is off-site work. The activity and location details need to agree.
Lena | Would complete records guarantee acceptance? The client wants a definite answer before planning next week.
Theo | No. [[Submission completeness::Submission completeness concerns whether information is supplied; it is distinct from risk acceptance, quotation, or binding.]] is one stage, not an acceptance decision. The information allows the risk to be reviewed under the applicable criteria and authority. It does not predetermine the outcome.
Lena | I will explain that distinction. The client requested Monday as the start date, but I have no document confirming that insurance begins then.
Theo | Keep the [[inception date::The inception date is established by the applicable insurance agreement, not merely by the applicant's preferred start date.]] described as requested. No quote, binder, or coverage confirmation has been issued. An urgent preference does not become confirmed insurance because we repeat it confidently.
Lena | What if the client's manager asks whether your discussion with me counts as temporary cover while the application is completed?
Theo | Do not present it as a [[binder::A binder provides temporary insurance according to its applicable terms; this information-gathering conversation does not issue one.]]. This exchange requests information and describes review status. It does not create an insurance agreement or authorize you to represent that one has been issued.
Lena | I will update you Monday at eleven, even if a previous insurer has not yet supplied every record. Is that useful?
Theo | Yes. Give the [[submission::The submission is the information package being assessed; its status can be updated even when some records remain outstanding.]] status and identify exactly what remains missing. A useful update can explain an unresolved dependency without disguising it as a completed review or an expected acceptance.
Lena | If the clarified activities require a more senior decision, I would rather know the next review step than make a promise to the client.
Theo | We can explain the relevant [[referral::Referral sends the issue to the required decision level; it does not itself mean the risk is accepted or declined.]] status when applicable. Keep the distinction between a review route and a decision. Neither an escalation nor a request for information is automatically a declination.
Lena | My client update will list the requested facts, Monday's status contact, and the absence of any coverage confirmation. It will avoid a guaranteed outcome.
Theo | Good. Any eventual decision must respect [[underwriting authority::Underwriting authority defines who can make specified decisions; gathering complete information does not transfer that authority to every participant.]] and the applicable process. Clear information helps that decision, but it does not substitute for the required authorization or the actual terms offered.''',
    transfer_title='Complete another submission handoff',
    transfer_setup='The Nova application lacks two operating addresses and the requested two-year loss record. Priya will obtain the information. A status update is due Thursday at 10:00; no binder has been issued.',
    transfer='''Broker: "The number of missing operating addresses is ___." | two | The supplied application lacks two addresses rather than a complete list of unknown size.
Underwriter: "The requested two-year document is the ___." | loss record | The brief identifies a two-year loss record as the other missing submission item.
Broker: "The person obtaining the information is ___." | Priya | Priya is explicitly responsible for obtaining the missing submission information.
Underwriter: "The status update is due ___." | Thursday at 10:00 | Thursday at ten is an information-update commitment, not a confirmed coverage inception.'''))


BOOK['units'].append(unit(
    title='Policy Language and Coverage Interpretation',
    scene='A summary does not contain the whole contract',
    skill='Explain the roles of policy documents without deciding coverage from an isolated heading.',
    brief='Business owner Rosa has a one-page summary showing a property limit of $500,000 and a $2,000 deductible. She assumes that every type of property damage is covered up to that limit. Account specialist Evan has the declarations and base form, but the listed endorsement E17 has not yet been retrieved. The full policy also contains conditions and exclusions that require review. No particular loss is being decided in this exchange. Evan will obtain E17 and walk Rosa through the applicable documents; the limit and deductible alone do not establish whether any specific event is covered.',
    cast='Rosa | Business owner\nEvan | Account specialist',
    culture=('Translate structure before offering interpretation', 'Clients may reasonably expect a short summary to be complete. Explain which document supplies which information and why the applicable forms must be read together. Avoid blaming the client for an inference encouraged by an oversimplified summary.'),
    a='''What does the one-page summary show? | A $500,000 property limit and a $2,000 deductible | Every exclusion in the policy | A final decision about every future loss | The retrieved text of E17 | The summary contains the stated limit and deductible, not the entire set of policy terms.
Which listed document is missing from the current review? | Endorsement E17 | The declarations | The base form | The one-page summary | Evan has not yet retrieved the listed endorsement E17.
What is not established by the two amounts alone? | Coverage for a particular event | The figures printed on the summary | That further document review is needed | That a deductible is shown | Limits and deductibles describe terms but do not by themselves establish coverage for a specific event.''',
    vocabulary='''policy wording | The text establishing the insurance contract's applicable terms. | review the policy wording
declarations | Policy information identifying the insured, period, limits, and other stated particulars. | check the declarations
insuring agreement | The policy section describing the basic insurance promise subject to its terms. | read the insuring agreement
definition | A specified meaning assigned to a term in the policy. | apply the policy definition
condition | A requirement or provision affecting rights and obligations under the policy. | review a policy condition
exclusion | A provision removing specified matters from coverage, subject to the applicable wording. | examine an exclusion
endorsement | A document modifying the policy's terms. | read the applicable endorsement
schedule | A list of items, locations, amounts, or forms attached to a policy. | check the policy schedule
coverage limit | The maximum applicable amount subject to the policy's terms. | identify the coverage limit
sublimit | A separate lower limit applying to a specified part of coverage. | identify a sublimit
aggregate limit | A limit applying to a defined total of claims or losses over a stated basis. | review the aggregate limit
per-occurrence limit | A limit applying to one occurrence as defined by the policy. | check the per-occurrence limit
deductible | The specified amount or share borne by the insured under the applicable terms. | explain the deductible
retention | A portion of risk or cost retained under a defined arrangement. | distinguish a retention
named insured | A person or organization identified as an insured in the policy. | verify the named insured
additional insured | A party given insured status for a defined scope under the applicable terms. | confirm additional insured status
covered property | Property meeting the policy's applicable coverage description. | identify covered property
covered cause of loss | A cause of loss within the applicable coverage wording. | assess a covered cause of loss
policy period | The interval during which the policy applies according to its terms. | confirm the policy period
effective date | The date on which a specified policy or change takes effect. | verify the endorsement's effective date
form number | An identifier for a policy document or wording version. | match the form number
coverage summary | A condensed description that may omit detailed policy provisions. | qualify the coverage summary
interpretation | Explanation of wording in its full relevant context. | support the interpretation
document set | The complete applicable collection of policy forms and amendments. | assemble the document set''',
    precision='An endorsement can add, restrict, or otherwise modify coverage; it is not automatically an extra benefit. Its form, effective date, and actual wording matter. E17 cannot be interpreted before its text is obtained.',
    precision_extra='A limit is not a guarantee that every loss is covered or paid in full. The deductible also does not answer coverage by itself. Definitions, insuring terms, exclusions, conditions, endorsements, and facts must be considered as applicable.',
    phrases='''Recognize the inference | I can see why the short summary gave that impression.
Name the document's role | This is a summary, not the complete policy wording.
State the visible amounts | It shows a $500,000 limit and a $2,000 deductible.
Limit the conclusion | Those amounts do not establish coverage for every event.
Identify the missing form | Endorsement E17 is listed but has not been retrieved.
Avoid guessing the change | We cannot infer E17's effect from its number.
Read the set together | We need the applicable forms and endorsements.
Explain an endorsement | It can modify coverage, including restricting it.
Keep definitions visible | The policy may assign a specific meaning to a familiar word.
Check the applicable period | Confirm the form and effective date.
Avoid a blanket promise | I cannot describe every type of damage as covered.
Distinguish limit and scope | The amount of a limit and the scope of coverage are different questions.
Offer a concrete next step | I will obtain E17 and review the document set with you.
Preserve the actual task | We are clarifying documents, not deciding a particular loss today.
Ask a precise question | Which wording supports the coverage statement in the summary?
Close accurately | We will explain the applicable provisions together rather than rely on one heading.''',
    notes='''Subject to | Connects a statement to qualifications that may materially affect it.
Listed versus retrieved | A document reference is not the document's actual wording.
Can modify | Includes additions and restrictions, not only extra protection.
Every type | An absolute claim unsupported by a summary heading.
Applicable | Restricts the review to the correct forms and period.
Limit versus coverage | The maximum amount and the existence of protection are separate questions.''',
    d='''Which explanation is accurate? | The summary shows amounts but does not contain every applicable term. | A listed limit means every event is covered. | Every endorsement only adds protection. | A form number reveals the complete wording. | The summary is condensed, while the missing endorsement and other policy provisions still require review.
What should Evan do about E17? | Obtain the applicable text and check its form and effective date. | Assume it adds unlimited coverage. | Ignore it because the summary is shorter. | Replace it with wording from an unrelated account. | The actual applicable endorsement must be reviewed rather than guessed from its identifier or another policy.
Which statement confuses amount and scope? | A $500,000 limit proves that any property loss is insured. | The summary shows a $2,000 deductible. | Conditions may affect policy obligations. | No particular loss is being decided today. | The maximum stated amount does not establish that every cause or type of loss falls within coverage.
Why review policy definitions? | Familiar words can have specified meanings in the contract. | They automatically remove every exclusion. | They guarantee the highest limit for every loss. | They replace all endorsements. | Contract definitions can narrow or specify ordinary words and must be read with the applicable provisions.''',
    dialogue='''Rosa | The summary says property cover up to five hundred thousand dollars. I assumed that meant every kind of property damage, after the deductible.
Evan | I can see why. But this [[coverage summary::A coverage summary is condensed and may omit provisions needed to understand the actual scope of protection.]] does not contain every applicable term. The limit and deductible are important, but they do not establish that every event or type of damage is covered.
Rosa | I have the summary and declarations. Are those two documents enough, or should I also have the longer form you mentioned?
Evan | We need the complete applicable [[document set::The document set includes the relevant policy forms and amendments, not merely the convenient summary and declarations.]]. I have the declarations and base form, but endorsement E17 is listed and has not yet been retrieved. We should not skip a listed amendment.
Rosa | I thought an endorsement always added protection. Could it actually reduce coverage or change the meaning of something in the main form?
Evan | An [[endorsement::An endorsement modifies policy terms and can add, restrict, or otherwise change coverage depending on its wording.]] can make different kinds of changes. We need its actual text, applicable form, and effective date. Its number alone does not tell us whether it expands or restricts anything.
Rosa | Then we should not describe E17 to my team until we have it. Where does the policy state the basic coverage promise?
Evan | The [[insuring agreement::The insuring agreement describes the basic promise, but it operates with the policy's other applicable provisions.]] is one starting point, read with the definitions and other provisions. It is not a standalone promise that can be separated from the rest of the applicable wording.
Rosa | Some ordinary words seem straightforward. Why would a definition section matter if everyone already knows what property or occurrence usually means?
Evan | A policy [[definition::A policy definition assigns a specified meaning that may differ from everyday usage and affects interpretation in context.]] may give a familiar word a specific meaning. We need that meaning when reading the relevant provision, rather than assume the everyday meaning settles the coverage question.
Rosa | The deductible is two thousand dollars. Does agreeing to bear that amount make every larger loss eligible for payment?
Evan | No. The [[deductible::A deductible specifies an insured share under the terms; it does not create coverage for an otherwise uncovered event.]] addresses the insured's specified share under the terms. It does not by itself establish that the property, cause, event, and other circumstances fall within coverage.
Rosa | What about the five-hundred-thousand-dollar figure? My colleague has been treating it as a guaranteed payment amount whenever something serious happens.
Evan | A [[coverage limit::A coverage limit is a maximum subject to terms, not a guaranteed payment or proof that every loss is covered.]] is not a guaranteed payment. The applicable scope, facts, and other terms still matter. We should correct that interpretation before it becomes a promise in your internal planning.
Rosa | I would like the explanation to show what is covered and what might be removed or qualified, without burying the important sections.
Evan | We will review each relevant [[exclusion::An exclusion removes specified matters from coverage according to its wording; it must be read in the complete applicable context.]] in context, alongside conditions and endorsements. I will not simply list broad headings and ask you to assume that they describe every possible event.
Rosa | Is the effective date another detail we should check when the endorsement arrives? I do not want to use an unrelated version.
Evan | Yes. Match the [[form number::The form number identifies a document or version, helping confirm that the reviewed wording belongs to the applicable policy set.]] and effective date to the applicable policy. A similar document from another period or account is not a reliable substitute for the actual issued wording.
Rosa | Please obtain E17 and walk me through the set. We are not asking you to decide a specific claim in this conversation.
Evan | Agreed. We will explain the [[policy wording::Policy wording establishes the relevant terms; reviewing it is different from making a coverage decision about an unspecified loss.]] together and correct the summary's overbroad impression. Any particular loss would require its facts and the applicable decision process, not a conclusion from the two amounts alone.''',
    transfer_title='Identify another incomplete document set',
    transfer_setup='A summary shows a $200,000 limit and a $1,500 deductible. The declarations list endorsement R4, which has not been retrieved. No specific claim is under decision.',
    transfer='''Client: "The displayed limit is ___ dollars." | 200,000 | Two hundred thousand is the stated limit, not a guaranteed payment for every loss.
Specialist: "The displayed deductible is ___ dollars." | 1,500 | Fifteen hundred is the deductible shown in the supplied summary.
Client: "The missing endorsement is ___." | R4 | R4 is the listed endorsement whose actual text has not been obtained.
Specialist: "A specific claim is ___ under decision here." | not | The case explicitly concerns documents rather than a particular claim decision.'''))

BOOK['units'].append(unit(
    title='Claims Intake and Reserving',
    scene='Open the file without inventing the loss details',
    skill='Ask for precise missing claim information and distinguish an estimate from a settlement commitment.',
    brief='Intake specialist Mina receives notice of alleged water damage under claim C204. The caller, Ben, has provided contact details and photographs, but the event date is unknown and the repair estimate has not been received. The date the damage was discovered is 6 June; that is not necessarily the date the event occurred. An adjuster has not completed the coverage or amount review. Mina will request the known timeline and supporting documents through the approved channel. An internal reserve, if established under the applicable process, is an estimate for claim accounting and management, not a promise of payment to Ben.',
    cast='Ben | Policyholder\nMina | Claims intake specialist',
    culture=('Let the client say unknown', 'People sometimes guess to satisfy a form or to avoid sounding unhelpful. Ask for what is known, distinguish discovery from occurrence, and record uncertainty accurately. A complete-looking file is less useful than an honest file that identifies the missing evidence.'),
    a='''What date is known? | Discovery on 6 June | The confirmed date the event occurred | The final payment date | The adjuster's coverage-decision date | Six June is the discovery date; the brief explicitly leaves the event date unknown.
What supporting document is missing? | The repair estimate | All photographs | The caller's contact details | A completed payment receipt | Photographs and contact details are supplied, but the repair estimate has not arrived.
What does an internal reserve not establish? | A payment promise to Ben | An internal estimate under the applicable process | A figure that may need review as information changes | A claim-management or accounting measure | A reserve is an internal estimate and does not itself approve coverage or promise settlement payment.''',
    vocabulary='''first notice of loss (FNOL) | The initial report of an event or loss to an insurer. | record first notice of loss
claimant | A person or entity making a claim. | identify the claimant
policyholder | The person or organization holding the policy. | contact the policyholder
claim number | The identifier assigned to a claim file. | quote the claim number
date of loss | The date associated with the event causing the claimed loss, as applicable. | establish the date of loss
discovery date | The date the loss or damage was first noticed. | record the discovery date
notification date | The date the insurer or relevant recipient was notified. | confirm the notification date
claim intake | The initial collection and recording of claim information. | complete claim intake
adjuster | A person responsible for investigating or evaluating claims within their role. | assign an adjuster
supporting documentation | Records relevant to evaluating the claimed event or amount. | request supporting documentation
repair estimate | A projected cost for specified repair work. | obtain a repair estimate
proof of loss | A statement or document describing claimed loss as required by the applicable process. | request the applicable proof of loss
case reserve | An estimate assigned to an individual claim under the reserving process. | review the case reserve
unpaid claim estimate | An estimate of amounts remaining to be paid on relevant claims. | assess an unpaid claim estimate
paid loss | Claim amounts already paid on the stated basis. | report paid loss
incurred loss | A loss measure combining paid amounts and relevant estimates on a specified basis. | define the incurred loss basis
incurred but not reported (IBNR) | An estimate for claims or development not yet reflected in reported information on the stated basis. | explain the IBNR estimate
loss adjustment expense (LAE) | Costs associated with investigating and settling claims under the accounting definition used. | distinguish loss adjustment expense
settlement | An agreement or resolution concerning the claim under applicable terms. | document a settlement
payment authorization | Approval for a specified claim payment. | verify payment authorization
claim chronology | A timeline of reported events and claim-handling steps. | build a claim chronology
information request | A request specifying what additional material is needed. | issue a clear information request
secure submission channel | An approved route for transmitting sensitive claim information. | use the secure submission channel
acknowledgment | Confirmation that a report or communication was received. | send a claim acknowledgment''',
    precision='The event date, discovery date, and notification date can differ. Record the known discovery date as such. Do not move it into the event-date field merely because the latter is empty.',
    precision_extra='Reserving estimates and settlement decisions serve different purposes. A reserve may change as information develops; it is not a contractual coverage determination or an amount the policyholder has been promised.',
    phrases='''Acknowledge receipt | We have opened claim C204 and received your photographs.
Separate the dates | You discovered the damage on 6 June.
Preserve the unknown | The event date has not yet been established.
Avoid a guessed entry | Please do not guess a date to fill the form.
Request a known timeline | Tell us when you first noticed the damage and what records you have.
Identify the missing document | We still need the repair estimate.
Explain the purpose | The adjuster needs these details to evaluate the reported loss.
Protect the channel | Please use the approved submission route for the documents.
Confirm what is already held | We have your contact details and photographs.
Avoid repeated requests | I will check the file before asking you to resend anything.
Keep the claim reference | Include C204 with the supporting material.
State the review stage | Coverage and amount reviews are not complete.
Explain an internal estimate | A reserve is not a promise of payment.
Separate authorization | No payment is authorized by this intake conversation.
Document uncertainty | I will record the date as unknown rather than inferred.
Close the request | We need the known timeline and repair estimate, not an invented event date.''',
    notes='''Discovered on | States when damage was noticed without dating the underlying event.
Not established | Preserves an unresolved fact rather than inserting a guess.
Received versus reviewed | Possession of a document does not establish a completed evaluation.
Estimate versus promise | A projected amount is not necessarily a payment commitment.
Still need | Should identify a specific missing item, not demand everything again.
As applicable | Recognizes that requirements depend on the actual policy and process.''',
    d='''Which entry accurately records 6 June? | Discovery date | Confirmed event date | Final settlement date | Payment-authorization date | Six June is when Ben noticed the damage; the event's actual date remains unknown.
Which follow-up request is best? | Please provide the known timeline and repair estimate through the approved channel, quoting C204. | Guess any event date and resend every document. | Send unrelated personal records to an unverified address. | Confirm coverage yourself before we review the file. | The request names the needed information, appropriate route, and claim reference without inventing facts.
Which statement improperly equates reserve and payment? | The internal reserve is the amount we promise to pay you. | The estimate may change as information develops. | No coverage decision is supplied here. | The amount review is incomplete. | A reserve is an internal estimate, not a settlement agreement or payment authorization.
What should Mina do before asking for photographs again? | Check the file, which already contains photographs. | Assume no documents were ever received. | Delete the existing photographs without review. | Replace the photographs with a guessed repair amount. | The brief confirms photographs are received, so checking the file avoids an unnecessary duplicate request.''',
    dialogue='''Ben | I sent photographs, but I only know the discovery date, not when the event occurred.
Mina | We have your [[first notice of loss::First notice of loss records the initial claim report; receiving it does not establish all event facts or coverage.]] under C204. Please tell me what you know without guessing. The report can accurately identify an unresolved fact rather than present an unsupported date as certain.
Ben | I noticed the damage on the sixth of June. I cannot say whether the underlying event happened that morning or earlier.
Mina | I will record that as the [[discovery date::The discovery date is when damage was noticed; it is not necessarily when the event causing it occurred.]]. The event date remains unknown. Those fields answer different questions, so I will not copy the sixth into the event-date field merely to complete it.
Ben | The earlier request was vague. What remains missing after the photographs I sent?
Mina | We still need the [[repair estimate::The repair estimate is the specific missing cost document; photographs have already been received and should not be requested indiscriminately again.]]. Your contact details and photographs are already in the file. I will make the follow-up specific rather than ask you to resend everything without checking what we hold.
Ben | The repair company has not finished its estimate. I can send it when available, but I cannot provide a reliable amount today.
Mina | Note that status in the [[claim chronology::The claim chronology records the actual sequence and outstanding information without inventing an amount or event date.]]. We need the known timeline and any relevant records, with uncertainties identified. An unavailable estimate should not become a made-up amount simply because the file has a field for it.
Ben | Would sending the estimate mean the claim is accepted? I need to explain the next step.
Mina | The [[adjuster::The adjuster evaluates the claim within the assigned role; receiving an estimate does not itself complete the coverage or amount review.]] still needs to review the claim. Providing a document is not the same as a coverage decision or agreement on the amount. Those reviews are not complete in this case.
Ben | Someone mentioned a reserve in an internal note. Is that the amount the insurer has promised to pay me for the damage?
Mina | A [[case reserve::A case reserve is an individual-claim estimate under the internal process, not a payment promise or coverage determination.]] is an internal estimate under the applicable process, not a settlement promise. It may change as information develops and does not by itself establish coverage or the final amount payable.
Ben | I should not treat an internal estimate as approved payment. There is no settlement agreement.
Mina | Correct. [[Payment authorization::Payment authorization approves a specified payment; an internal estimate or intake conversation does not supply that approval.]] is a separate matter. This intake conversation collects information and explains status. It does not authorize a payment or replace the review of the applicable policy and facts.
Ben | How should I send the repair estimate and timeline? They include some personal contact information and the property reference.
Mina | Use the approved [[secure submission channel::The secure submission channel is the authorized route for sensitive material; the example does not ask for disclosure through an unverified address.]] provided through our verified service process, and include claim C204. Do not send sensitive documents to an unverified address simply because a message appears to mention your claim.
Ben | Please make the request list clear. I will provide the known dates and the repair estimate when it is available, without guessing the event date.
Mina | I will send that [[information request::The information request should specify the missing timeline and estimate, preserving known facts and the unresolved event date.]] and identify what we already hold. This helps you respond to the actual gaps rather than repeat work or infer that every earlier submission has been lost.
Ben | That gives me a practical next step. I understand that receipt of the documents is not confirmation of coverage or the final settlement amount.
Mina | Exactly. Our [[acknowledgment::An acknowledgment confirms receipt, not acceptance of coverage, agreement on the loss amount, or authorization of payment.]] will confirm receipt, while the review status remains separate. Keep the claim reference on future correspondence so the new information can be connected to the correct file and evaluated in context.''',
    transfer_title='Separate the dates in another intake call',
    transfer_setup='For claim C318, damage was discovered on 12 July. The event date remains unknown. Photographs are received; the repair estimate is missing. No payment decision has been made.',
    transfer='''Specialist: "The claim reference is ___." | C318 | C318 is the identifier assigned to the separate claim in this exercise.
Caller: "The discovery date is ___." | 12 July | Twelve July is the known discovery date, not a confirmed event date.
Specialist: "The missing cost document is the ___." | repair estimate | The brief states that photographs are received but the repair estimate is missing.
Caller: "The event date remains ___." | unknown | The case explicitly leaves the event date unknown, so it must not be guessed.'''))


BOOK['units'].append(unit(
    title='Coverage Disputes and Denials',
    scene='Explain an open review without implying a denial',
    skill='Respond to pressure for certainty with an accurate status, specific outstanding issue, and useful follow-up.',
    brief='Policyholder Miles reports equipment damage under claim K91 and asks whether the loss is definitely covered. Claims representative Sana confirms that the review is open. The cause report is outstanding, and the applicable endorsement must be evaluated against the facts. No coverage determination, denial, or payment commitment has been made. Sana will provide a status update Friday at 16:00, whether or not the review is complete. Miles interprets the request for more information as a rejection. Sana must correct that impression without promising acceptance or implying that a pending review suspends any applicable rights or deadlines.',
    cast='Miles | Policyholder\nSana | Claims representative',
    culture=('Acknowledge the need without borrowing certainty', 'A policyholder may need a definite answer to make practical decisions. Acknowledge that pressure, explain the actual unresolved issue, and provide a reliable communication step. Neither reassurance nor defensive language should change the claim status.'),
    a='''What is the claim's current status? | Coverage review remains open. | The claim is definitely covered. | A denial has been issued. | Payment has been authorized. | The brief states that review is open and no determination, denial, or payment commitment has been made.
Which information is outstanding? | The cause report | Every contact detail | A previously issued settlement payment | An already final coverage decision | The cause report is specifically identified as outstanding in the current review.
What is promised for Friday at 16:00? | A status update even if review remains incomplete | A guaranteed acceptance | An automatic denial | A payment transfer | Sana commits to reporting status, not to a particular decision or completed review.''',
    vocabulary='''coverage determination | A decision about whether and how policy coverage applies to a claim. | issue a coverage determination
coverage review | Evaluation of the policy and facts relevant to a claim's coverage. | complete a coverage review
coverage position | The insurer's stated interpretation or decision concerning coverage. | explain the coverage position
denial | A decision refusing a claim or specified part of it on a stated basis. | communicate a denial
partial coverage | Coverage applying to some but not all claimed matters under the decision. | explain partial coverage
reservation of rights | A notice preserving specified coverage rights while a matter is handled, subject to applicable law. | review a reservation of rights
cause report | A report examining how an event or damage occurred. | obtain the cause report
causation | The relationship between an event and the claimed loss. | assess causation
factual basis | The established information supporting a conclusion. | explain the factual basis
policy provision | A specific term or clause in the policy. | cite the policy provision
applicable endorsement | The amendment relevant to the policy, period, and issue under review. | evaluate the applicable endorsement
unresolved issue | A question not yet answered sufficiently for the relevant decision. | identify the unresolved issue
review owner | The person responsible for coordinating the relevant evaluation. | identify the review owner
status update | A communication reporting the current stage and known developments. | provide a status update
decision notice | A communication conveying a specified decision. | distinguish the decision notice
review route | The applicable process for requesting further examination of a decision. | explain the review route
appeal | A request for reconsideration through an available formal process. | identify the applicable appeal process
complaint | An expression of dissatisfaction requiring handling under the relevant process. | record a complaint
rights and remedies | Available entitlements and means of pursuing them under the applicable framework. | explain relevant rights and remedies
notice requirement | A rule or term governing a required communication. | check the notice requirement
time limit | A period within which a specified action must be taken. | verify the applicable time limit
without prejudice | A context-dependent legal expression whose effect requires applicable legal assessment. | seek advice on without-prejudice wording
settlement authority | The defined power to approve a claim resolution or payment arrangement. | confirm settlement authority
written explanation | A documented account of the reasons and supporting basis for a position. | provide a written explanation''',
    precision='Pending is neither accepted nor denied. A request for relevant information is not itself a denial, and a promised update is not a promised outcome. Actual notices must comply with applicable requirements.',
    precision_extra='Do not assume an open review pauses a policyholder deadline or removes a complaint or review right. Such questions require the applicable policy, jurisdiction, and authorized advice; this dialogue creates no legal extension.',
    phrases='''Acknowledge the practical need | I understand that you need clarity for your next decisions.
State the actual status | The coverage review remains open.
Correct the inference | The information request is not a denial.
Avoid the opposite promise | It is not confirmation of coverage either.
Name the missing item | We are waiting for the cause report.
Explain the other task | The endorsement must be evaluated against the facts.
Keep the decision separate | No coverage determination has been made.
Avoid payment language | I cannot promise payment from the current status.
Offer a reliable contact | I will update you Friday at 16:00.
Limit the time commitment | That is an update time, not a guaranteed decision date.
Keep communication active | I will contact you even if the review is incomplete.
Respect other rights | Do not assume this review changes any applicable deadline.
Clarify the request | The missing report is needed to assess the reported cause.
Use plain status words | Open review means the decision has not yet been reached.
Explain an eventual position | A decision should be communicated through the applicable process with its basis.
Close the call | We will separate the outstanding evidence, review status, and next contact.''',
    notes='''Definitely covered | Claims a determination that has not been made here.
Not a denial | Corrects rejection without implying acceptance.
Waiting for | Identifies a specific dependency, not an excuse to stop communicating.
Even if | Keeps the update commitment valid despite an incomplete review.
Any applicable deadline | Avoids inventing a universal time limit or extension.
Decision versus status | A report about progress is not necessarily a coverage ruling.''',
    d='''Which response best matches the facts? | The review is open; the cause report is outstanding; no coverage decision has been made. | You are definitely covered because you reported the loss. | We denied the claim by asking for information. | Friday's update guarantees payment. | The accurate response identifies the actual stage and missing evidence without inventing acceptance, rejection, or payment.
What should Sana do if review is incomplete on Friday? | Provide the promised status update and explain what remains open. | Skip the call because there is no final answer. | Invent a favorable decision. | Say all rights have expired without checking. | The communication commitment remains in force even when the substantive review is unfinished.
Which statement about deadlines is unsupported? | The open review automatically pauses every applicable deadline. | Relevant deadlines require the applicable rules and wording. | This example grants no extension. | Status and legal rights are separate questions. | No supplied policy or legal basis establishes that pending review suspends any deadline.
How should an eventual decision be described? | Through the applicable process with its actual basis and relevant next steps | As a guaranteed result before review | As a vague feeling without reference to facts | As a reason to erase the claim records | A decision needs its actual factual and policy basis and the applicable communication process, not a guessed conclusion.''',
    dialogue='''Miles | I need to know whether K91 is definitely covered. Your request for another report sounds as though the claim has already been rejected.
Sana | The [[coverage review::Coverage review is the ongoing evaluation; its open status does not establish acceptance or denial.]] remains open. No coverage determination or denial has been made. I understand that you need clarity, but I should not describe an unfinished decision as either accepted or rejected.
Miles | What remains missing? The general information request does not explain what prevents a decision.
Sana | The [[cause report::The cause report is the specified outstanding evidence about how the damage occurred; naming it makes the dependency clear.]] is outstanding. The applicable endorsement also needs to be evaluated against the facts. Those are the current review issues, rather than a completed conclusion that your loss is outside coverage.
Miles | Would providing that report guarantee acceptance? I need to decide what to do about the equipment.
Sana | Receiving it would inform the [[factual basis::The factual basis supports evaluation; supplying one document does not predetermine the resulting coverage decision.]], not guarantee a particular outcome. We still need to assess what it establishes alongside the applicable wording. I cannot turn a document request into a promise of acceptance.
Miles | Please confirm directly whether anything has been denied. Is this request a decision notice?
Sana | No [[denial::Denial is a decision refusing all or part of a claim; none has been made in the supplied case.]] has been made here. The information request is not one. At the same time, the absence of a denial is not confirmation that the claim is covered.
Miles | That is clearer. Can you identify who will keep me informed rather than leaving me to call repeatedly for the same status?
Sana | I will coordinate the [[status update::A status update reports progress and outstanding matters; it is not automatically a decision or payment promise.]] Friday at sixteen hundred. I will contact you even if the review is incomplete, explain the actual position, and identify what remains unresolved rather than simply repeat a generic message.
Miles | Should I treat Friday as the date when the claim will be decided? That would at least give me a fixed planning point.
Sana | It is not a guaranteed [[coverage determination::A coverage determination decides application of the policy; the Friday communication commitment does not guarantee that decision.]] date. Friday is our communication commitment. I do not control every outstanding input, so I should not promise that the substantive review will be complete by then.
Miles | Which endorsement provision is relevant? An unidentified clause is hard to understand.
Sana | The eventual explanation must identify the relevant [[policy provision::A policy provision supplies the actual wording basis; an unexplained reference to a clause is not a clear coverage explanation.]] and how it relates to the established facts. I will not guess that relationship before the review or substitute a broad label for the applicable wording.
Miles | Does an open review mean I can ignore any time limits elsewhere in the policy while I wait for your answer?
Sana | Do not assume that. An applicable [[time limit::A time limit remains governed by its actual requirements; this pending review does not establish an automatic suspension or extension.]] needs to be checked under the policy and relevant requirements. This conversation creates no extension and does not remove any rights or obligations that may apply.
Miles | If I disagree with the eventual decision, will the available review routes be explained?
Sana | The applicable [[review route::The review route depends on the actual policy and jurisdiction; the dialogue does not invent a universal appeal process or deadline.]] and complaint options should be communicated as required for the actual decision and jurisdiction. We should not invent a universal procedure or suggest that this current request takes those options away.
Miles | For now, I understand that you need the cause report, the endorsement review is ongoing, and I will receive a status call Friday.
Sana | Correct. No [[payment authorization::Payment authorization permits a specified payment; no such commitment follows from the pending review or promised update.]] has been made or promised through this exchange. I will keep the evidence request, review status, and next contact clear so you are not left to infer a decision from silence.''',
    transfer_title='Correct another pending-review message',
    transfer_setup='Claim M22 awaits an inspection report. No coverage determination has been made. Rehan will provide a status update Tuesday at 14:00, even if the review remains incomplete.',
    transfer='''Representative: "The claim reference is ___." | M22 | M22 is the identifier supplied for this separate pending-review case.
Policyholder: "The missing document is the ___." | inspection report | The inspection report is the specified outstanding evidence in the brief.
Representative: "Your update contact is ___." | Rehan | Rehan is explicitly responsible for providing the status update.
Policyholder: "The update is scheduled for ___." | Tuesday at 14:00 | Tuesday at fourteen hundred is an update appointment, not a guaranteed decision time.'''))

BOOK['units'].append(unit(
    title='Broker and Client Renewal Meetings',
    scene='Lower premium does not mean identical protection',
    skill='Explain a renewal trade-off using a bounded deductible calculation and a complete comparison request.',
    brief='Broker Naomi compares two annual renewal quotes for client Victor. Quote A has a $10,000 premium and a $1,000 per-loss deductible; quote B has a $9,000 premium and a $5,000 per-loss deductible. Their full wording has not been compared, and neither quote is bound. For one arithmetic illustration only, assume a fully covered $8,000 loss, sufficient applicable limits, no coinsurance, no other adjustments, and a deductible subtracted once from the loss. A would leave $1,000 of that loss with Victor; B would leave $5,000. The illustration is not a prediction of future claims or a coverage decision.',
    cast='Victor | Business client\nNaomi | Insurance broker',
    culture=('Explain the trade-off before asking for a choice', 'A client may focus on the most visible price. Acknowledge the premium saving, then quantify the changed deductible under explicit assumptions. Do not hide the trade-off or present a simplified example as proof of which option will be best for the client.'),
    a='''How much lower is B's annual premium? | $1,000 | $4,000 | $5,000 | $9,000 | Ten thousand minus nine thousand gives a one-thousand-dollar annual premium difference.
How much higher is B's per-loss deductible? | $4,000 | $1,000 | $8,000 | $10,000 | Five thousand minus one thousand gives a four-thousand-dollar increase in the stated deductible.
What is not yet established? | That the full coverage wording is otherwise identical | The stated premium amounts | The stated deductible amounts | The arithmetic illustration's loss amount | The full wording has not been compared, so equivalent coverage cannot be asserted.''',
    vocabulary='''renewal | Continuation or replacement of insurance for a further policy period. | review the renewal
renewal quote | Proposed terms for the next policy period. | compare renewal quotes
annual premium | The stated insurance price for a one-year period on the specified basis. | compare the annual premium
per-loss deductible | The deductible applied to each loss under the stated terms. | explain the per-loss deductible
premium saving | A reduction in premium relative to a specified comparison. | quantify the premium saving
retained loss | The part of a loss borne by the insured under the arrangement. | compare retained loss
out-of-pocket amount | Money the client bears directly on the defined basis. | estimate the out-of-pocket amount
coverage comparison | Review of differences in the protection and terms offered. | prepare a coverage comparison
like-for-like basis | A comparison holding relevant terms and assumptions consistent. | compare on a like-for-like basis
coinsurance | A cost-sharing or insurance-to-value provision whose meaning depends on the policy type. | review the coinsurance provision
valuation basis | The method used to determine the value of a covered loss. | compare the valuation basis
replacement cost | A valuation basis concerning replacement under the applicable terms. | review replacement-cost terms
actual cash value | A valuation measure defined by applicable policy terms and law, often reflecting depreciation. | explain actual cash value
depreciation | A reduction in value attributed to age, wear, or other relevant factors. | account for depreciation
sublimit comparison | Review of differences in specified lower coverage limits. | complete a sublimit comparison
coverage gap | An identified absence or interruption of relevant insurance protection. | identify a coverage gap
renewal condition | A stated requirement affecting the proposed renewal. | confirm a renewal condition
quote validity | The period and conditions during which proposed terms remain available. | check quote validity
binding instruction | A request to place coverage under the applicable authority and process. | confirm binding instructions
binding confirmation | Communication confirming placed coverage according to its actual terms. | obtain binding confirmation
effective period | The dates during which the relevant terms apply. | verify the effective period
illustrative loss | A hypothetical loss used to demonstrate a calculation. | label the illustrative loss
total-cost comparison | Comparison including specified premium and loss or other cost components. | state the total-cost comparison basis
risk tolerance | Willingness and capacity to bear uncertainty or loss under a defined context. | discuss risk tolerance''',
    precision='In the $8,000 illustration, A pays $7,000 and B pays $3,000, with Victor bearing $1,000 and $5,000 respectively. These results depend on all stated assumptions and do not decide actual claim coverage.',
    precision_extra='B saves $1,000 in annual premium but retains $4,000 more in this one-loss illustration. Combining premium and retained loss gives $11,000 for A and $14,000 for B in that illustration only, not an expected annual-cost forecast.',
    phrases='''Acknowledge the saving | B's annual premium is $1,000 lower.
Name the changed term | B's per-loss deductible is $4,000 higher.
Reject false equivalence | These are not identical terms for less money.
Keep the review open | We have not yet compared the complete wording.
Set the assumptions | Assume one fully covered $8,000 loss with no other adjustments.
Calculate the first share | Under A, you would retain $1,000 of that loss.
Calculate the second share | Under B, you would retain $5,000 of that loss.
State the insurer amount | The illustrated insurer payments are $7,000 and $3,000.
Limit the example | This is arithmetic practice, not a prediction or coverage decision.
Include the full basis | Premium plus retained loss totals $11,000 under A in this example.
Contrast the example | The same illustrated total is $14,000 under B.
Avoid universal advice | One hypothetical loss does not establish the best option for every future year.
Check other differences | We still need the exclusions, endorsements, limits, and valuation terms.
Preserve quote status | Neither quote is currently bound.
Ask for a documented decision | Confirm the actual terms before giving binding instructions.
Close the comparison | We will show the premium saving and the changed exposure together.''',
    notes='''Lower premium | Describes price, not automatically the scope or value of protection.
Per loss | Matters because application can differ from annual or aggregate arrangements.
Would under these assumptions | Keeps the calculation conditional.
Fully covered | A supplied illustration assumption, not a conclusion about a real claim.
Neither bound | Describes placement status, not merely the existence of a quote.
Expected versus illustrative | A single example does not estimate the distribution of future outcomes.''',
    d='''In the illustration, what would A's insurer payment be? | $7,000 | $8,000 | $1,000 | $3,000 | The assumed fully covered loss of eight thousand minus A's one-thousand deductible gives seven thousand.
In the illustration, what would B's insurer payment be? | $3,000 | $5,000 | $9,000 | $7,000 | Eight thousand minus B's five-thousand deductible gives three thousand under the stated assumptions.
Which premium-plus-retained-loss comparison is correct for this example? | A: $11,000; B: $14,000 | A: $10,000; B: $9,000 with no retained loss | A: $18,000; B: $17,000 | Both: $8,000 | A combines ten thousand premium and one thousand retained loss; B combines nine thousand and five thousand.
Which conclusion is unsupported? | B provides identical coverage and always costs less overall. | B has the lower stated premium. | B has the higher stated deductible. | Neither quote is bound. | The complete wording is unreviewed, and total cost depends on actual losses and terms, not premium alone.''',
    dialogue='''Victor | Quote B is a thousand dollars cheaper annually. Is this simply the same protection for less money, or is there a trade-off?
Naomi | The [[annual premium::Annual premium describes the stated yearly insurance price; a lower figure does not establish identical protection.]] is lower, but B's deductible is five thousand rather than one thousand dollars. We also have not compared the full wording, so we cannot claim equivalent protection.
Victor | The deductible difference is four thousand dollars per loss. Could you show how that would matter using the eight-thousand-dollar example?
Naomi | Yes, as an [[illustrative loss::An illustrative loss is hypothetical and demonstrates arithmetic under explicit assumptions rather than deciding actual coverage.]] only. Assume it is fully covered, limits are sufficient, no coinsurance or other adjustment applies, and the deductible is subtracted once. Those assumptions are essential to the calculation.
Victor | Under A, subtracting one thousand from eight thousand gives a seven-thousand-dollar insurer payment. My share of that loss would be one thousand.
Naomi | Correct. That is your [[retained loss::Retained loss is the loss amount borne by the client; A retains one thousand under the supplied assumptions.]] in this example. Under B, the five-thousand-dollar deductible leaves a three-thousand-dollar insurer payment and five thousand for you to bear.
Victor | So B's premium saving is one thousand, but I retain four thousand more if this particular hypothetical loss occurs. Those are different comparisons.
Naomi | Exactly. Show the [[premium saving::Premium saving compares the insurance price, while the higher retained loss is a separate effect of the changed deductible.]] and deductible effect side by side. Do not describe the saving as a guaranteed reduction in every cost you could face during the policy year.
Victor | If I include annual premium and my share of this one loss, I get eleven thousand for A and fourteen thousand for B.
Naomi | That is the correct [[total-cost comparison::The total-cost comparison includes premium and retained loss for this single hypothetical case, not every possible annual outcome.]] on this narrow basis. It is not an expected annual-cost forecast. Different losses, no losses, or other policy terms could produce different outcomes.
Victor | Could another term affect the calculation even if the main limit shown on both quotes looks the same? We have only compared the headline figures.
Naomi | Yes. The [[valuation basis::Valuation basis affects how loss value is determined under the policy; matching headline limits do not establish identical payment terms.]], exclusions, endorsements, sublimits, and other applicable provisions need review. A matching headline limit does not prove that the full coverage or settlement basis is identical.
Victor | I also noticed the word coinsurance in one document. We excluded it from the example, so we have not explained its actual effect.
Naomi | Correct. [[Coinsurance::Coinsurance has policy-specific cost-sharing or insurance-to-value meanings; this illustration expressly excludes it rather than interpreting an actual provision.]] requires the relevant wording and policy context. We should not transfer a definition from another product or assume the simplified illustration settles how that provision applies.
Victor | The example is useful, but I do not want it presented as a recommendation to choose A regardless of our actual circumstances.
Naomi | It is not. A [[like-for-like basis::A like-for-like basis aligns relevant terms and assumptions before comparison; the full quote wording has not yet been aligned here.]] requires the complete terms, and a decision also needs your actual needs and capacity to bear loss. One hypothetical event cannot decide every possible future year.
Victor | Have either of these terms already been placed? I have not instructed you to proceed with a particular quote.
Naomi | Neither has [[binding confirmation::Binding confirmation records actual placed coverage; receiving or discussing a quote does not establish that it has been bound.]]. We must keep proposed terms separate from actual placement. A discussion of the lower premium or our calculation does not by itself confirm coverage under either quote.
Victor | Please finish the wording comparison and show the premium and deductible differences clearly. Then we can make a documented decision about the proposal.
Naomi | Agreed. We will confirm the [[effective period::The effective period identifies when the actual terms apply; it must be checked with the proposal before placement instructions are acted on.]] and other relevant conditions before acting on binding instructions. The comparison should make the trade-offs visible, not hide them behind the lower annual price.''',
    transfer_title='Compare a second pair of deductibles',
    transfer_setup='For one fully covered $6,000 loss, assume sufficient limits and no other adjustments. Quote C has a $500 per-loss deductible; D has a $2,000 deductible. Deductibles are subtracted once.',
    transfer='''Broker: "Under C, the client retains ___ dollars." | 500 | C's five-hundred-dollar deductible is the retained amount under the supplied assumptions.
Client: "Under C, the insurer pays ___ dollars." | 5,500 | Six thousand minus five hundred gives five thousand five hundred dollars.
Broker: "Under D, the client retains ___ dollars." | 2,000 | D's stated two-thousand-dollar deductible is the client's retained amount in this illustration.
Client: "Under D, the insurer pays ___ dollars." | 4,000 | Six thousand minus two thousand gives four thousand dollars under the same assumptions.'''))


BOOK['units'].append(unit(
    title='Fraud Indicators and SIU Referral',
    scene='Record a discrepancy without labeling the customer',
    skill='Make an objective specialist referral that separates observed records, suspicion, and findings.',
    brief='Claims analyst Iris notices that invoice reference P71 from the same repair vendor appears in files Q2 and Q4. The team has not established whether this reflects a duplicate upload, an administrative error, or another explanation. Neither the vendor nor the customer has been found to have acted dishonestly. A draft internal note calls the customer fraudulent. Review lead Hassan will correct that language and refer the documented discrepancy through the approved Special Investigation Unit (SIU) route. Original records must be preserved, access restricted to authorized recipients, and no unsupported allegation added to customer correspondence.',
    cast='Iris | Claims analyst\nHassan | Review lead',
    culture=('Objective language protects the investigation and the person', 'A forceful label can sound efficient inside a busy team, but it can turn an untested concern into an assumed fact. Describe what is observed, identify alternative explanations that remain open, and let the authorized review establish its findings.'),
    a='''What has actually been observed? | Invoice reference P71 appears in Q2 and Q4 for the same vendor. | The customer has admitted fraud. | The vendor has been convicted. | The invoice has been proved altered. | The supplied evidence establishes a repeated invoice reference, not dishonest intent or an established fraud finding.
What remains unknown? | The explanation for the repeated reference | The two file identifiers | The invoice reference | The existence of the draft accusation | The case leaves open whether duplication, error, or another explanation accounts for the repeated reference.
What should happen to the original records? | Preserve them and restrict access to authorized recipients. | Delete them after making the referral. | Replace them with an accusation. | Share them with unrelated colleagues. | Preserving originals and limiting access protects traceability and confidentiality during the authorized review.''',
    vocabulary='''Special Investigation Unit (SIU) | A specialist function reviewing suspected insurance fraud under the applicable process. | refer to the SIU
fraud indicator | Information that may warrant examination for possible fraud. | document a fraud indicator
suspicion | A concern that has not been established as a finding. | distinguish suspicion from proof
allegation | An assertion of wrongdoing that requires appropriate evaluation. | avoid an unsupported allegation
verified finding | A conclusion established through the relevant evidential review. | record a verified finding
discrepancy | A difference or inconsistency requiring explanation. | describe a discrepancy
duplicate record | A second copy or entry that may repeat existing information. | identify a duplicate record
invoice reference | An identifier assigned to an invoice. | compare the invoice reference
source document | The original or originating record supporting an entry. | preserve the source document
administrative error | A mistake in handling or recording information. | examine a possible administrative error
referral criteria | The conditions for sending a matter to a specialist review. | apply referral criteria
referral summary | A concise account of the concern and supporting evidence. | prepare a referral summary
evidence preservation | Retention of relevant material without improper alteration or destruction. | maintain evidence preservation
access restriction | A limit on who may view or use information. | apply access restrictions
authorized recipient | A person permitted to receive the relevant information. | identify authorized recipients
case note | A record of an event, observation, or action in a case file. | correct a case note
source attribution | Identification of where information or an assertion originated. | include source attribution
chronological record | An account organized by the timing of events or entries. | maintain a chronological record
corroboration | Additional evidence supporting a statement or interpretation. | seek appropriate corroboration
alternative explanation | Another possible account of the observed information. | retain an alternative explanation
investigation status | The current stage of an authorized examination. | report investigation status
need-to-know access | Access limited to those requiring the information for their authorized role. | maintain need-to-know access
neutral wording | Language describing facts without an unsupported judgment. | use neutral wording
review conclusion | The outcome established by the relevant review. | distinguish the review conclusion''',
    precision='A repeated invoice reference may justify a closer look, but it does not establish who caused it or why. A referral is an action taken because a concern requires review; it is not a finding of fraud.',
    precision_extra='Correct the accusatory note through the applicable traceable process rather than erase the record of what was written. Share the evidence only through authorized channels. This exercise provides no investigative tactics or fraud-detection threshold.',
    phrases='''State the observation | Invoice P71 appears in both Q2 and Q4 for the same vendor.
Separate observation and conclusion | We have not established the explanation.
Remove an unsupported label | Do not describe the customer as fraudulent.
Keep alternatives open | A duplicate upload or administrative error remains possible.
Preserve the source | Retain the original documents and their references.
Name the next step | Refer the discrepancy through the approved SIU route.
Limit the meaning | Referral is not a finding of fraud.
Use traceable correction | Correct the case note without concealing its history.
Avoid attributing intent | We do not know who caused the repeated entry or why.
Specify the evidence | Include the two file references and the invoice identifier.
Restrict distribution | Send the material only to authorized recipients.
Keep customer communication accurate | Do not insert an unsupported allegation into correspondence.
Report the stage | The concern is awaiting specialist review.
Avoid automatic denial | This referral does not itself determine coverage or payment.
Preserve role boundaries | Let the authorized reviewers establish the findings.
Close objectively | Record the observed discrepancy, open questions, and referral status.''',
    notes='''Appears in both | Reports a record comparison without explaining its cause.
May warrant review | Indicates a reason to examine, not an established offense.
Fraudulent | An accusatory conclusion unsupported by these facts.
Remains possible | Preserves an alternative without claiming it is the explanation.
Referred versus proven | An action status differs from an evidential conclusion.
Authorized recipients | Limits access by role rather than curiosity or convenience.''',
    d='''Which note is appropriate? | P71 appears in Q2 and Q4; explanation unconfirmed; referred through the approved SIU route. | The customer is fraudulent because two references match. | Delete Q4 to remove the discrepancy. | Every repeated invoice proves intentional deception. | The appropriate note records the observation, unresolved explanation, and actual referral action without an unsupported accusation.
Which statement confuses referral with a finding? | SIU referral proves that fraud occurred. | The cause of the repetition is unconfirmed. | Original records must be preserved. | Access is limited to authorized recipients. | Referral requests specialist examination and does not itself establish wrongdoing.
What should the team do with the accusatory draft note? | Correct it through the traceable process and preserve relevant history. | Conceal that it was ever written. | Copy it into every customer letter. | Treat the accusation as evidence of itself. | A traceable correction fixes the wording without hiding the record or treating an allegation as proof.
Which explanation is established? | None of the proposed explanations is yet established. | A deliberate false claim | A vendor conspiracy | A confirmed duplicate upload | The brief explicitly leaves the reason unknown, including the possibility of an administrative or upload error.''',
    dialogue='''Iris | Invoice P71 appears in both Q2 and Q4 for the same vendor. My draft note calls the customer fraudulent, but that overstates what we know.
Hassan | Replace the label with the [[discrepancy::Discrepancy describes the repeated reference without asserting a cause, dishonest intent, or established fraud.]] itself. We have identified a repeated reference, not established who caused it or why. The note must distinguish the observed records from an accusation about the person.
Iris | A duplicate upload or administrative error could explain it. We have not confirmed either explanation, so neither should be presented as the answer.
Hassan | Keep each [[alternative explanation::An alternative explanation remains a possibility until evaluated; naming one does not establish it as the actual cause.]] open. Neutral language is not a conclusion that nothing is wrong. It is an accurate statement that the explanation still requires authorized review.
Iris | Should I send the files through our specialist referral route? I want the concern examined without implying that I have completed an investigation.
Hassan | Use the approved [[Special Investigation Unit::The Special Investigation Unit is the relevant specialist function; referral requests review rather than declaring the customer guilty.]] route under the applicable criteria. Include the factual observation and references. Referral does not by itself establish fraud, decide coverage, or authorize a particular claim outcome.
Iris | I will include the two file identifiers, the invoice reference, and the vendor name from the records. The documents themselves should remain intact.
Hassan | Preserve each [[source document::A source document supports the record comparison and must remain available rather than being replaced by a paraphrase or accusation.]] and its context. Do not replace an original with a cleaned-up version that hides how the discrepancy appeared. Reviewers need traceable evidence, not just our description.
Iris | What should happen to the accusatory draft already in the internal file? Simply deleting it could conceal the change in our wording.
Hassan | Correct the [[case note::The case note needs a traceable correction so the unsupported accusation is fixed without concealing the record's history.]] through the applicable process. Preserve the relevant history and make the corrected factual statement clear. We should not leave the accusation unqualified or erase the audit trail.
Iris | A colleague wants to circulate this widely as a warning. The facts are still under review.
Hassan | Maintain [[need-to-know access::Need-to-know access limits sensitive information to authorized roles rather than broad circulation for interest or warning.]]. Share only with authorized recipients who need the information for their role. An unresolved concern is not a reason to distribute customer information or an unsupported allegation across unrelated teams.
Iris | I will also check the proposed customer correspondence. It must not repeat the draft label or suggest that specialist referral is proof of wrongdoing.
Hassan | Correct. Avoid an unsupported [[allegation::An allegation asserts wrongdoing; this case supports a documented concern, not a conclusion to repeat as established fact.]]. Customer communication must follow the authorized process and actual status. Our language task is to preserve that distinction, not invent investigative disclosures or claim decisions.
Iris | The referral summary should say what we observed, what remains unknown, and what action we took. It should not claim that fraud has been verified.
Hassan | That separates [[suspicion::Suspicion is an unestablished concern; the documented observation may justify review without becoming proof of fraud.]] from a finding. A strong referral can be precise and useful without sounding accusatory. Its value comes from traceable facts and clear questions, not forceful adjectives.
Iris | When another team asks whether the customer has been cleared or found responsible, I should report only the actual review stage.
Hassan | Yes. State the [[investigation status::Investigation status reports the stage of review, not an outcome that has not yet been established.]] available through the authorized route. Do not invent either an adverse finding or an exoneration simply because someone wants a short binary answer before the review is complete.
Iris | I will correct the note, preserve both records, restrict access, and submit the documented discrepancy. The explanation remains unconfirmed.
Hassan | Good. Any eventual [[review conclusion::The review conclusion must follow the authorized evidential assessment; it cannot be supplied by the initial analyst's label.]] needs its actual basis. Until then, keep observation, possible explanations, referral action, and decision status separate in every record you prepare.''',
    transfer_title='Complete an objective referral',
    transfer_setup='Receipt R88 appears in files H3 and H7. Its explanation is unconfirmed. The matter has been referred for specialist review; no fraud finding exists.',
    transfer='''Analyst: "The repeated receipt reference is ___." | R88 | R88 is the specific repeated receipt identifier supplied in this case.
Reviewer: "It appears in H3 and ___." | H7 | H7 is the second file named in the observed record comparison.
Analyst: "The explanation remains ___." | unconfirmed | The brief does not establish why the receipt appears in both files.
Reviewer: "The matter is referred for specialist ___." | review | Referral requests review and does not constitute a finding of fraud.'''))

BOOK['units'].append(unit(
    title='Actuarial Assumptions and Pricing',
    scene='Frequency and severity changes multiply',
    skill='Explain claim-cost movement using consistent exposure, separate drivers, and a limited pricing conclusion.',
    brief='Actuarial analyst Pavel compares two fully developed fictional annual claim cohorts with the same 1,000 policy-years of exposure and a consistent claim-count and cost basis. Year 1 has 100 claims averaging $2,000 each. Year 2 has 120 claims averaging $2,200 each. The totals are $200,000 and $264,000. The comparison excludes expenses, reinsurance, investment income, and other pricing components. Manager Farah drafts a note saying costs rose 30%, adding the 20% claim-frequency increase to the 10% severity increase. Pavel must correct the combined change to 32% and explain why this historical comparison does not itself establish a 32% premium increase.',
    cast='Farah | Portfolio manager\nPavel | Actuarial analyst',
    culture=('Correct arithmetic while protecting the decision context', 'A manager may compress a technical result into an apparently simple price instruction. Show the calculation in ordinary language, name the exposure basis, and separate historical claim experience from a complete forward-looking price recommendation.'),
    a='''What is held constant between the cohorts? | Exposure at 1,000 policy-years and the stated reporting basis | The claim count | The average cost per claim | The total claim cost | The brief explicitly holds exposure and the counting and cost basis consistent while claims and severity change.
What is Year 2's total claim cost? | $264,000 | $240,000 | $220,000 | $200,000 | One hundred twenty claims multiplied by an average of twenty-two hundred dollars gives two hundred sixty-four thousand.
Why is the combined increase not 30%? | The frequency and severity factors multiply rather than simply add. | The exposure doubled. | There were no claims in Year 1. | Expenses are included in the average. | The combined factor is 1.20 times 1.10, giving 1.32 and therefore a thirty-two-percent increase.''',
    vocabulary='''actuary | A professional analyzing financial consequences of risk using relevant methods and standards. | consult the actuary
claim frequency | The number of claims per defined unit of exposure. | calculate claim frequency
claim severity | The average claim cost on a stated measurement basis. | estimate claim severity
policy-year | An exposure unit equivalent to one policy in force for one year on the defined basis. | measure exposure in policy-years
exposure base | The quantity used to relate losses or claims to the business at risk. | define the exposure base
pure premium | Claim cost per unit of exposure on the stated basis, before other specified components. | calculate pure premium
loss cost | A measure of claim cost on a specified basis, distinct from a complete charged premium. | estimate loss cost
cohort | A group of policies or claims defined for a common analysis. | compare claim cohorts
fully developed claims | Claims whose evaluated costs are treated as complete on the stated analysis basis. | compare fully developed claims
development factor | A factor used to estimate change from reported to a later claim-cost stage. | assess a development factor
trend | An estimated pattern of change in cost or frequency over time. | analyze claim-cost trend
credibility | The weight assigned to information based on its relevance and reliability for estimation. | assess statistical credibility
experience period | The period from which observed claims or exposure are drawn. | define the experience period
prospective period | The future period for which an estimate is intended. | specify the prospective period
rate indication | An actuarial estimate informing a proposed rate level under stated assumptions. | develop a rate indication
expense provision | An allowance for defined expense components in an estimate or price. | include an expense provision
reinsurance cost | The cost associated with transferring specified insurance risk to another insurer. | account for reinsurance cost
loss ratio | Loss amounts divided by the specified premium measure on a stated basis. | define the loss ratio
combined ratio | A measure combining defined loss and expense ratios under the stated convention. | interpret the combined ratio
multiplicative effect | A combined change obtained by multiplying relative factors. | explain the multiplicative effect
percentage-point change | The arithmetic difference between two percentages. | distinguish a percentage-point change
sensitivity test | An evaluation of how results vary with changed assumptions. | conduct a sensitivity test
model assumption | A condition or value adopted in an analytical model. | disclose a model assumption
pricing recommendation | A proposed price decision based on the relevant analysis and constraints. | support a pricing recommendation''',
    precision='Frequency rises from 0.10 to 0.12 claims per policy-year: a 20% relative increase. Severity rises from $2,000 to $2,200: 10%. Their combined factor is 1.20 x 1.10 = 1.32, a 32% increase.',
    precision_extra='Pure premium on the stated claim-cost basis rises from $200 to $264 per policy-year. This is not the charged premium or a complete forward-looking rate indication. Other pricing components and assumptions remain outside the example.',
    phrases='''Define the population | Both cohorts contain 1,000 policy-years of exposure.
State the count change | Claims increased from 100 to 120.
Name the rate | Frequency rose from 0.10 to 0.12 claims per policy-year.
Quantify the relative change | That is a 20% frequency increase.
Define severity | Average claim cost rose from $2,000 to $2,200.
Quantify the second driver | Severity increased by 10%.
Combine the factors | Multiply 1.20 by 1.10 to get 1.32.
Correct the headline | Total claim cost rose 32%, not 30%.
Show the amounts | Costs increased from $200,000 to $264,000.
State the exposure-normalized result | Pure premium rose from $200 to $264 per policy-year.
Keep the basis consistent | The claim-count and cost bases are the same.
Name the exclusions | Expenses, reinsurance, and other pricing components are excluded.
Avoid a price instruction | This does not establish a 32% premium increase.
Separate past and future | Historical experience is an input, not a complete forecast.
Ask for the full analysis | A pricing recommendation needs the relevant prospective assumptions.
Close with the calculation | Show the exposure, frequency, severity, and combined factor together.''',
    notes='''Per policy-year | Supplies the exposure denominator needed for a frequency measure.
Increased by versus increased to | Distinguishes the amount of change from the new level.
Relative increase | Compares the change with the starting value.
Multiply versus add | Combined proportional drivers produce an interaction effect.
On this basis | Limits the claim-cost measure to the supplied definitions and exclusions.
Indication versus instruction | Analysis informs a decision; one historical metric does not dictate it.''',
    d='''What is Year 1's frequency? | 0.10 claims per policy-year | 10 claims per policy-year | $2,000 per claim | 100 policy-years per claim | One hundred claims divided by one thousand policy-years gives 0.10 claims per policy-year.
What is the relative total-cost increase? | 32% | 30% | 20% | 10% | The sixty-four-thousand increase divided by the two-hundred-thousand starting total equals thirty-two percent.
What is Year 2's pure premium on this basis? | $264 per policy-year | $2,200 per policy-year | $120 per policy-year | $1,000 per claim | Dividing the two-hundred-sixty-four-thousand total by one thousand policy-years gives two hundred sixty-four per policy-year.
Which price conclusion is supported? | This historical comparison alone does not determine a premium change. | Every customer must receive exactly a 32% increase. | Expenses are automatically zero because excluded. | Historical averages guarantee future losses. | The analysis excludes other pricing components and prospective assumptions, so it cannot prescribe a complete price change.''',
    dialogue='''Farah | My summary says claim costs rose thirty percent: frequency increased twenty percent and severity ten percent. Is that the correct combined figure?
Pavel | It is thirty-two percent. [[Claim frequency::Claim frequency divides claim count by exposure; with exposure unchanged, the rise from 100 to 120 claims is twenty percent.]] rose from 0.10 to 0.12 per policy-year. Severity also increased, so we multiply the two relative factors rather than simply add their percentage changes.
Farah | Before we show the calculation, confirm that both groups have the same exposure. Otherwise claim counts alone could give a misleading comparison.
Pavel | Each has one thousand [[policy-years::Policy-years provide the common exposure unit; both cohorts use one thousand on the supplied consistent basis.]]. The claim-count and cost bases are also consistent. That lets us compare the supplied frequency figures without attributing an exposure increase to a change in underlying claim frequency.
Farah | Year 1 has a hundred claims at two thousand dollars each. Year 2 has a hundred twenty at twenty-two hundred each.
Pavel | Correct. [[Claim severity::Claim severity is average claim cost; increasing from two thousand to twenty-two hundred dollars is ten percent.]] increases ten percent. Total claim cost therefore moves from two hundred thousand to two hundred sixty-four thousand dollars. The difference is sixty-four thousand, not sixty thousand.
Farah | So the total-cost ratio is 264,000 divided by 200,000, or 1.32. Subtracting one gives the thirty-two-percent relative increase.
Pavel | Exactly. The [[multiplicative effect::The multiplicative effect combines 1.20 and 1.10 as 1.32, including the interaction missed by adding twenty and ten.]] is 1.20 times 1.10. More claims also experience the higher average cost. Adding twenty and ten omits that interaction and understates the combined change.
Farah | Can we express the result per exposure unit as well? The portfolio team is used to seeing the amount per policy-year.
Pavel | On this basis, [[pure premium::Pure premium expresses the stated claim cost per exposure unit, not the full charged insurance premium.]] rises from two hundred to two hundred sixty-four dollars per policy-year. Keep the definition attached: this is the stated claim-cost measure, not the full premium charged to a customer.
Farah | Does that justify telling the pricing team to increase premiums by thirty-two percent? It would be a simple message to put on the slide.
Pavel | It does not establish a complete [[rate indication::A rate indication requires relevant prospective cost analysis; the historical claim-cost change excludes necessary pricing components and assumptions.]]. Expenses, reinsurance, and other pricing components are excluded. We also need the relevant prospective assumptions rather than assume that this historical change dictates the next year's price.
Farah | The case calls both cohorts fully developed. That avoids comparing one mature group with another group whose claims have barely been reported.
Pavel | Yes. [[Fully developed claims::Fully developed claims are treated as complete on the supplied analysis basis, keeping development differences out of this particular comparison.]] are an explicit assumption here. In another dataset, differences in development or reporting maturity would require attention. We must not carry this convenient assumption into a real portfolio without evidence.
Farah | These historical annual groups are not automatically a forecast of the year we are about to price.
Pavel | Name the [[experience period::The experience period identifies when observed data arose; it is separate from the future period a pricing estimate addresses.]] and distinguish it from the prospective period. Historical experience can inform a forecast, but it does not guarantee future frequency, severity, or the mix of business.
Farah | I will also avoid saying expenses are zero. They are outside this comparison, which is very different from proving that they do not exist.
Pavel | Correct. An [[expense provision::An expense provision accounts for defined expenses; excluding it from the exercise does not establish that actual expenses are zero.]] and other relevant components need their own basis in a complete analysis. A clean arithmetic example should not silently become a model with missing costs treated as nonexistent.
Farah | The revised slide will show equal exposure, separate frequency and severity changes, the multiplying factors, and the thirty-two-percent total-cost increase.
Pavel | Good. Keep any [[pricing recommendation::A pricing recommendation requires the broader relevant analysis; the corrected historical arithmetic is an input rather than a final instruction.]] separate until the broader work supports it. This correction improves the evidence presented to the decision-makers without claiming that one historical percentage answers every pricing question.''',
    transfer_title='Combine another pair of claim drivers',
    transfer_setup='Two cohorts have the same exposure. Frequency increases 10% and severity increases 20%. Starting total claim cost is $100,000; all other calculation conditions are held constant.',
    transfer='''Analyst: "The frequency factor is ___." | 1.10 | A ten-percent relative increase corresponds to multiplying the starting frequency by 1.10.
Manager: "The severity factor is ___." | 1.20 | A twenty-percent relative increase corresponds to multiplying starting severity by 1.20.
Analyst: "The combined factor is ___." | 1.32 | Multiplying 1.10 by 1.20 gives 1.32, not an additive factor of 1.30.
Manager: "The resulting claim-cost total is ___ dollars." | 132,000 | One hundred thousand multiplied by 1.32 equals one hundred thirty-two thousand dollars.'''))


BOOK['units'].append(unit(
    title='Compliance, Market Conduct, and Complaints',
    scene='Answer the fee question instead of sending another acknowledgment',
    skill='Restate a complaint accurately, investigate its actual basis, and provide a substantive status without inventing a remedy.',
    brief='Policyholder Elena complains about a $30 charge labeled SF30 on an invoice dated 5 August. Her annual quote shows $1,200, and she asks why this separate charge appears and where it was disclosed. A previous reply merely thanked her for the feedback. Complaint handler Marco has not yet established the fee basis, whether it was properly disclosed, or whether it should be corrected or refunded. Marco will obtain the relevant billing and disclosure records and provide an update Friday at 14:00. The complaint remains open; the update appointment is neither a legal deadline nor a guaranteed refund date.',
    cast='Elena | Policyholder\nMarco | Complaint handler',
    culture=('Acknowledge the exact issue before explaining the process', 'A polite generic reply can feel dismissive when it never names the question. Restate the charge, document, and requested explanation. Recognize the earlier communication failure while keeping any decision about validity, correction, or refund tied to the evidence.'),
    a='''What specific charge is disputed? | $30 labeled SF30 on the 5 August invoice | The entire $1,200 annual quote without a fee question | A confirmed $300 refund | A charge on an unknown document | Elena identifies the amount, code, and invoice date, giving a specific billing question.
What did the earlier reply fail to address? | The fee basis and where it was disclosed | Whether the complaint had any greeting | The policyholder's preferred font | A completed refund transaction | A generic thank-you did not answer why the charge appeared or where it had been disclosed.
What is Marco's commitment? | Obtain relevant records and update Elena Friday at 14:00 | Guarantee a refund by Friday | Declare the fee lawful without review | Close the complaint immediately | Marco promises evidence gathering and a status update, while the fee decision and remedy remain unresolved.''',
    vocabulary='''market conduct | How insurance business is carried out in dealings with customers and the market. | review market conduct
complaint intake | Receipt and recording of a customer's expression of dissatisfaction. | complete complaint intake
complaint register | A record of complaints, issues, actions, and status. | update the complaint register
substantive response | A reply addressing the actual issues raised rather than merely confirming receipt. | provide a substantive response
generic acknowledgment | A nonspecific confirmation that a communication was received. | distinguish a generic acknowledgment
fee basis | The reason and applicable authority or terms supporting a charge. | establish the fee basis
billing code | An identifier used to classify an invoice item. | trace the billing code
invoice line | A separate entry showing a charge or other billing item. | examine the invoice line
disclosure record | Evidence of information provided about terms, charges, or other matters. | retrieve the disclosure record
quote comparison | Review of an invoice or proposal against the quoted terms. | conduct a quote comparison
billing reconciliation | Comparison and explanation of differences between billing records. | complete billing reconciliation
refund | Money returned following an applicable decision or correction. | confirm a refund decision
credit adjustment | A recorded reduction or offset to an account balance. | process a credit adjustment
remedy | An action addressing an established problem under the applicable process. | identify the appropriate remedy
complaint owner | The person responsible for coordinating complaint handling. | assign a complaint owner
response commitment | An undertaking to communicate by a specified point. | meet the response commitment
resolution status | The recorded stage of addressing the complaint's issues. | report resolution status
escalation | Raising an issue to the relevant higher or specialist review level. | arrange complaint escalation
customer outcome | The actual result experienced by the customer. | assess the customer outcome
fair treatment | Handling customers consistently with applicable obligations and relevant circumstances. | support fair treatment
record retention | Keeping records for the applicable purpose and required period. | follow record-retention requirements
regulatory inquiry | A request for information or explanation from the relevant authority. | respond to a regulatory inquiry
complaint rights | Applicable options for raising dissatisfaction or seeking further review. | explain complaint rights
final response | A communication stating the completed position under the applicable complaint process. | distinguish a final response''',
    precision='The SF30 label identifies the invoice item, not the legitimacy or disclosure of the fee. A $1,200 quote and a separate $30 line raise a question that requires the applicable records; they do not settle it.',
    precision_extra='A response commitment is not automatically a regulatory deadline or a refund promise. Keep the complaint open until its actual handling status supports closure, and preserve any applicable further-review or complaint rights.',
    phrases='''Restate the issue | You are asking why SF30 adds $30 and where it was disclosed.
Identify the document | The charge appears on the invoice dated 5 August.
Acknowledge the earlier failure | Our previous reply did not answer that question.
Separate receipt and resolution | Thanking you for feedback did not resolve the issue.
Name the missing evidence | I need the billing basis and disclosure records.
Avoid premature validation | I have not established that the charge is correct.
Avoid the opposite promise | I have not established that a refund is due either.
Check the quote | We will compare the invoice with the $1,200 annual quote.
State ownership | I will coordinate the review of this complaint.
Give the next contact | I will update you Friday at 14:00.
Limit the commitment | That is a response time, not a guaranteed refund date.
Keep the file accurate | The complaint remains open.
Explain an unresolved review | If records are still missing, I will name what remains outstanding.
Offer a substantive reply | The response will address the fee basis and disclosure question.
Preserve rights | We will explain the applicable further-review options.
Close respectfully | You should not have to infer an answer from another generic acknowledgment.''',
    notes='''Why and where | Identify two questions: the charge's basis and its disclosure.
Did not answer | Acknowledges the communication failure without inventing the fee outcome.
Not established | Keeps both validation and refund decisions open.
Compare with | Requests evidence reconciliation rather than assuming either document is decisive alone.
Remains open | Describes complaint status while substantive questions remain unresolved.
Update versus final response | An interim communication can be useful without being the completed position.''',
    d='''Which opening addresses Elena's complaint? | You are asking why SF30 adds $30 and where it was disclosed; our earlier reply did not answer that. | Thank you again for your valuable feedback. | Every fee is valid because it has a code. | Your refund is guaranteed despite our incomplete review. | The opening names both substantive questions and acknowledges the earlier response failure without inventing a decision.
What does SF30 establish by itself? | The billing item identifier | That the fee was properly disclosed | That a refund is definitely due | That the complaint is closed | A billing code identifies an item but does not establish its authority, disclosure, or proper outcome.
What should Marco do if the records remain incomplete on Friday? | Provide the promised update and specify what remains unresolved. | Miss the update without explanation. | Close the complaint because time has passed. | Pretend a refund has been approved. | The response commitment remains valid even if the substantive evidence review is not complete.
Which closing statement is premature? | The complaint is resolved because we sent a generic thank-you. | The fee basis is still under review. | The disclosure record has not yet been established. | Applicable review options need accurate explanation. | An acknowledgment does not resolve the fee and disclosure questions that remain open.''',
    dialogue='''Elena | I asked why the August fifth invoice has a thirty-dollar SF30 charge when my annual quote shows twelve hundred. Your reply did not explain it.
Marco | You need the [[fee basis::Fee basis concerns the reason and applicable terms supporting the charge; the earlier acknowledgment did not establish it.]] and where the charge was disclosed. Our previous reply did not answer either question. I will address those issues specifically instead of sending another general thank-you.
Elena | The code means nothing to me. Is it part of the premium or a separate item?
Marco | SF30 is a [[billing code::A billing code identifies an invoice item; it does not by itself explain the charge's legitimacy, disclosure, or relationship to premium.]]. It identifies the item, but it does not by itself establish why the charge applies. I need to trace the relevant billing and terms records before explaining its basis.
Elena | When was it disclosed? Please do not say it was probably somewhere in the paperwork.
Marco | I will obtain the [[disclosure record::The disclosure record supplies evidence of what information was provided; a guess that it was somewhere in paperwork is insufficient.]] and compare it with the quoted terms and invoice. I have not yet established whether the charge was properly disclosed, so I should not make that assertion.
Elena | Does the difference mean that the fee was definitely wrong? I would like a refund if I was charged something I should not have paid.
Marco | We have not reached a [[refund::A refund returns money following the applicable decision; an unresolved fee question does not establish that outcome.]] decision. I should not promise one before the review, just as I should not claim the charge is correct. The records need to support the actual outcome.
Elena | Who owns the complaint? Is anyone actually reviewing the invoice?
Marco | I will be the [[complaint owner::The complaint owner coordinates the handling and communication; that role does not imply a completed decision about the disputed fee.]] coordinating this review. I will request the billing basis and disclosure evidence and keep the specific charge, quote, and questions connected in the file.
Elena | Can you tell me when I will hear from you? I do not want another week of wondering whether my message has disappeared.
Marco | I will make a [[response commitment::A response commitment promises communication at a stated point; it is not automatically a legal deadline or refund date.]] for Friday at fourteen hundred. If the review remains incomplete, I will still update you and identify the outstanding records rather than leave you without contact.
Elena | If it was an error, should I expect a refund by Friday? What exactly does that appointment mean?
Marco | Friday is an update, not a guaranteed [[remedy::A remedy addresses an established problem under the applicable process; the Friday status appointment does not guarantee its decision or completion.]] date. Any correction or refund must follow the supported decision and applicable process. I cannot promise an outcome or payment timing that has not been established.
Elena | I understand. Please do not close the complaint simply because you have now acknowledged the question more clearly.
Marco | It remains open in the [[complaint register::The complaint register should reflect the unresolved fee and disclosure questions rather than mark a generic acknowledgment as resolution.]]. We should distinguish receipt, investigation, response, and resolution. A polite acknowledgment is useful, but it does not answer the charge question or finish the review.
Elena | The eventual reply needs to say why the charge appears and where it was disclosed, with enough detail for me to check the explanation.
Marco | That requires a [[substantive response::A substantive response addresses the actual questions with a supported explanation, instead of merely confirming receipt or expressing appreciation.]]. We will connect the position to the relevant evidence and explain any remaining issue or applicable next step. Another general expression of appreciation would not meet that need.
Elena | Please also explain what I can do if I still disagree with the result. I do not want to lose that option while waiting.
Marco | We will explain the applicable [[complaint rights::Complaint rights depend on the applicable process and jurisdiction; the pending review must not be presented as removing them.]] and further-review routes accurately. This status conversation does not remove them or invent a universal deadline. For now, the complaint remains open and I will update you Friday.''',
    transfer_title='Replace another generic acknowledgment',
    transfer_setup='A policyholder asks about a $45 charge coded AD45 on a 9 September invoice. Its basis and disclosure remain unconfirmed. Lina will update the policyholder Monday at 15:00; no refund decision exists.',
    transfer='''Handler: "The disputed amount is ___ dollars." | 45 | Forty-five dollars is the specific charge supplied in this separate complaint.
Policyholder: "The invoice code is ___." | AD45 | AD45 identifies the disputed invoice item without establishing whether it is correct.
Handler: "The review contact is ___." | Lina | Lina is explicitly assigned to provide the complaint update.
Policyholder: "The promised update is ___." | Monday at 15:00 | Monday at fifteen hundred is a communication commitment, not a guaranteed refund time.'''))
