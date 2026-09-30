"""Original legal-workplace communication practice, not legal advice."""
from books.authoring import unit

BOOK = dict(
    slug='law', title='Law English', cover_label='Legal teams / clients / professional judgment',
    cover_title='Law', tagline='Precise language for facts, authority, and carefully bounded advice.',
    audience='For internationally trained lawyers, paralegals, legal assistants, and legal-team colleagues.',
    map_intro='Separate fact from conclusion, explain the authority, and preserve the client decision.',
    notes_title='Precision is more than formal vocabulary.',
    notes_intro='Legal English distinguishes what someone alleges, what a record shows, what an authority says, and what a lawyer concludes. These fictional cases practice those distinctions using primarily US workplace terminology; legal systems and professional roles vary.',
    field_notes=[
        ('Attribute the statement', 'Identify whether a point comes from a client, a witness, a document, or the reviewing lawyer. A clear attribution avoids silently converting a report into an established fact.', '"The client reports late delivery; we have not reviewed the signed agreement."'),
        ('Name the authority and its limits', 'A relevant decision is not necessarily controlling. Jurisdiction, court level, facts, procedural posture, and later treatment can affect its use.', '"This decision supports the argument by analogy; its binding effect has not been established."'),
        ('Keep the condition attached', 'A short summary should preserve material qualifications. An estimate, an option, a proposed term, and an authorized instruction are different things.', '"The proposed wording remains subject to client approval and counsel review."'),
        ('Do not promise a result', 'Explain known information, options, uncertainty, and next steps within the assigned role. A reassuring tone must not become a guarantee or imply authority the speaker lacks.', '"I can confirm the review is scheduled, not that the court will accept the position."')],
    scope_note='Fictional language practice, not legal advice or qualification to practice law. Terminology, duties, privilege, deadlines, and procedure depend on jurisdiction and facts. Actual decisions require authorized counsel and current governing sources. Never use real confidential client material in practice.',
    sources=[
        dict(title='United States Courts. Glossary of Legal Terms.', url='https://www.uscourts.gov/glossary', note='Reference for general US federal-court terminology. Definitions here are simplified language explanations, not complete statements of law.', checked='30 September 2026'),
        dict(title='American Bar Association. Model Rule 1.4: Communications.', url='https://www.americanbar.org/content/aba-cms-dotorg/en/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_4_communications/', note='Background for clear client communication. ABA model rules are not automatically the governing rules in a particular jurisdiction.', checked='30 September 2026'),
        dict(title='American Bar Association. Model Rule 1.6: Confidentiality of Information, Comment.', url='https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_6_confidentiality_of_information/comment_on_rule_1_6/', note='Background for distinguishing professional confidentiality from evidentiary privilege. Actual obligations and exceptions require jurisdiction-specific review.', checked='30 September 2026'),
        dict(title='Council of Europe. CEFR mediation resources.', url='https://www.coe.int/en/web/common-european-framework-reference-languages/mediation', note='Background for explaining specialist information, clarifying meaning, and supporting informed interaction.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Legal English Mindset: Facts, Issues, Rules, Risk', scene='A late-delivery email is not the whole contract',
    skill='Distinguish an allegation from a legal conclusion and identify missing evidence.',
    brief='A case note says the supplier breached the contract. The team has an email stating that delivery occurred on 18 May, but has not reviewed the signed agreement or amendments. The client says the promised date was 15 May. Ava, a paralegal, prepared the chronology; Daniel, supervising counsel, reviews the analysis. No legal conclusion about breach or remedy has been approved.',
    cast='Ava | Paralegal\nDaniel | Supervising counsel',
    culture=('Qualify the conclusion without weakening the factual report', 'Legal colleagues may challenge a sentence sharply because one verb changes its status. "Reports," "shows," "suggests," and "establishes" convey different levels and sources of support. Attribute each point and identify what further review is needed.'),
    a='''What does the available email report? | Delivery on 18 May | A signed 15 May contractual deadline | An agreed damages award | A court finding of breach | The email supplies a reported delivery date, not the complete contractual terms or a legal ruling.
Where does the 15 May date currently come from? | The client's account | A reviewed signed agreement | A court judgment | An approved amendment | The briefing attributes the date to the client; the agreement and amendments have not been reviewed.
Which conclusion remains unapproved? | Whether the supplier breached an applicable obligation | Whether an email exists | Whether Ava prepared a chronology | Whether Daniel supervises the analysis | The case has not established the governing obligation or approved a breach or remedy conclusion.''',
    vocabulary='''fact | A circumstance treated as established on the relevant evidence. | distinguish facts from conclusions
allegation | An assertion that has not necessarily been established. | attribute an allegation
issue | A question requiring analysis or determination. | frame the legal issue
rule | A governing proposition whose applicability must be assessed. | identify the applicable rule
application | Analysis connecting a rule to the relevant facts. | explain the application
conclusion | A reasoned determination drawn from the analysis. | qualify the conclusion
evidence | Information offered to support a factual proposition. | assess the supporting evidence
inference | A conclusion drawn from other information. | identify an evidential inference
assumption | A proposition used provisionally without establishing it. | state the working assumption
chronology | An ordered account of events over time. | prepare a sourced chronology
source | The origin of a statement or piece of information. | identify the source
corroboration | Additional support for an account or proposition. | seek independent corroboration
agreement | An arrangement whose terms and legal effect require context. | review the signed agreement
obligation | A requirement imposed by a relevant legal or contractual source. | identify the disputed obligation
breach | Failure to comply with an applicable legal or contractual duty. | assess an alleged breach
remedy | A form of relief potentially available for a legal wrong. | evaluate available remedies
damages | Monetary relief for legally recognized loss or injury. | distinguish damages from a claimed loss
causation | The legally relevant connection between conduct and consequence. | analyze causation
materiality | The significance of a fact or term in its legal context. | assess materiality
qualification | A condition or limit attached to a statement. | preserve a material qualification
reservation | A stated concern or limit on a position. | express a reservation
exposure | Potential adverse legal or financial consequence. | assess potential exposure
preliminary | Initial and subject to further review. | label the analysis preliminary
factual record | The assembled information relevant to the matter. | complete the factual record''',
    precision='The email and client account are sources to assess, not interchangeable proof of the signed terms. Delivery on 18 May does not alone establish breach of a 15 May contractual obligation, particularly when the agreement and amendments remain unreviewed.',
    precision_extra='A claimed loss is not automatically recoverable damages. An available remedy depends on governing law and facts. These cases practice how to preserve that uncertainty, not how to resolve a real dispute.',
    phrases='''Attribute a report | The client reports that 15 May was the promised date.
State the record | The email records delivery on 18 May.
Separate a conclusion | We have not yet established the applicable contractual deadline.
Identify missing material | We need the signed agreement and any relevant amendments.
Qualify the note | The potential breach analysis remains preliminary.
Frame the issue | The question is which delivery obligation governed this shipment.
Avoid a guarantee | We cannot infer an available remedy from the date alone.
Close with a task | I will assemble the documents and identify each source in the chronology.
Distinguish evidence | That supports the delivery date, not necessarily the promised date.
Preserve attribution | Please retain "the client reports" in the shortened summary.
Check an assumption | Are we assuming the email varied the signed terms?
Name an inference | That is an inference from the sequence, not an express statement in the document.
Invite correction | Which part of the chronology conflicts with the source record?
Limit certainty | The record may support that position, subject to the remaining review.
Separate loss and relief | The claimed loss and recoverable damages are different questions.
Confirm review status | Counsel has not approved a final conclusion on breach or remedy.''',
    notes='''Reporting verbs | "The client reports" attributes a claim; "the agreement requires" claims the terms have been established.
May versus does | "May support" marks a possible inference rather than a completed legal determination.
Subject to | Keep "subject to review of the amendments" attached to the conclusion it limits.
Chronological order | Dates establish a sequence, not by themselves the legal effect of the events.
Not necessarily | This phrase rejects an automatic inference without claiming that the inference must be false.
Passive precision | "It is alleged" may hide the source; name who makes the allegation when appropriate and authorized.''',
    d='''Which sentence accurately describes the available record? | The client reports a 15 May promise; the email records delivery on 18 May. | The signed agreement conclusively requires delivery by 15 May. | A court has found the supplier liable. | Damages are automatically the difference between the dates. | The first statement keeps the two sources separate and does not invent reviewed terms or a ruling.
Which word best signals an initial analysis? | preliminary | adjudicated | executed | final | Preliminary indicates work subject to further review; the other words imply different procedural or final states.
Which request targets the missing contractual basis? | Please obtain the signed agreement and relevant amendments. | Please remove all qualifications from the summary. | Please calculate a guaranteed recovery now. | Please treat the client's date as a court finding. | The agreement and amendments can identify the obligation; confident wording cannot supply missing terms.
Which distinction matters before recommending a remedy? | Claimed loss versus legally recoverable damages | Email date versus font size | File name versus office number | Meeting length versus paragraph length | A client's stated loss does not itself establish the amount or availability of a legal remedy.''',
    dialogue='''Ava | I have prepared the chronology. The delivery email says 18 May, and the client says delivery was promised for the fifteenth. My summary currently says the supplier breached.
Daniel | Keep the dates, but revise that [[conclusion::A conclusion about breach requires analysis of the applicable obligation; the two dates alone do not establish it.]]. Have we reviewed the signed agreement and any amendments governing this shipment yet?
Ava | Not yet. The client sent the delivery email and described the earlier promise in our call. I should identify that description as the client's account.
Daniel | Yes. That [[attribution::Attribution identifies who supplied a statement, preventing a reported promise from becoming an independently established contract term.]] matters. The email supports a delivery date, but it does not necessarily establish the contractual date against which performance must be assessed.
Ava | Would alleged breach be acceptable while we request the contract? I want the internal note to make the client's concern visible without presenting the analysis as finished.
Daniel | You can describe the client's [[allegation::An allegation is an asserted position whose truth or legal effect is not yet established by the team.]], then identify the issue for review. Avoid using the label as a substitute for stating what information is missing.
Ava | The issue is which delivery obligation applied to this shipment. We need to know whether the fifteenth was an agreed requirement, a forecast, or something later changed.
Daniel | Exactly. Obtain the agreement and relevant [[amendments::Amendments may change contractual terms; reviewing only an initial agreement could miss the obligation actually applicable to the shipment.]]. Do not assume the first document we receive is the complete statement of the parties' terms.
Ava | I will add source references next to each chronology entry. Some entries come from emails, and others are the client's account of telephone conversations with the supplier.
Daniel | That produces a more useful [[factual record::The factual record assembles information with its sources and limitations; it supports later analysis without erasing differences in evidential support.]]. We can then see which points have documentary support and which may need further corroboration.
Ava | The client also estimates a substantial lost sale because the goods arrived late. Should I put that amount under damages in the summary of the matter?
Daniel | Label it a claimed loss for now. [[Causation::Causation concerns the legally relevant connection between the conduct and the loss; an asserted lost sale does not automatically establish that connection.]], recoverability, and amount require analysis. Calling the figure damages at this stage may imply more has been established than is true.
Ava | Understood. I will not promise a recovery or imply a remedy has been approved. The chronology can report the lost-sale account separately from any legal assessment.
Daniel | Good. Preserve the [[qualification::A qualification states a material limit, here that the terms and consequences remain subject to review.]] when you shorten the note for the team. A concise summary should not become more certain than the underlying record.
Ava | One colleague says the three-day difference makes the answer obvious. How can I respond directly without making this sound like a dispute about who understands the file?
Daniel | Ask which reviewed term supports the proposed [[obligation::The obligation is the duty against which conduct is assessed; requesting its source tests the analysis rather than the colleague's competence.]]. We are testing the basis for the statement, not judging the person who made it.
Ava | I will revise the opening: the client reports a fifteenth-of-May delivery promise; the email records delivery on the eighteenth; contractual terms and potential remedies remain under review.
Daniel | That is appropriately [[preliminary::Preliminary marks an initial analysis that remains open to further documents and review, without concealing the client's concern.]]. Add the document request and its owner so the qualification leads to a concrete next action rather than a vague caveat.
Ava | I will request the signed agreement and amendments today, retain the email reference, and send the updated chronology for your review without adding an unsupported deadline or remedy.
Daniel | Thank you. A defensible [[analysis::Analysis connects the established facts and applicable rules before reaching a conclusion; it is more than putting a legal label on a chronology.]] starts with those distinctions. We can assess the legal position once the relevant terms and evidence are available.''',
    transfer_title='A termination email without the governing clause',
    transfer_setup='A client reports that a supplier ended service early. The team has the termination email but has not reviewed the governing termination clause or amendments. No conclusion on validity is approved.',
    transfer='''Paralegal: "The client ___ that service ended early." | reports | Reports attributes the account without presenting an unreviewed legal conclusion as established.
Counsel: "Obtain the governing termination ___ and any amendments." | clause | The applicable contractual wording is needed before assessing the legal effect of the termination.
Paralegal: "Until that review, the validity assessment remains ___." | preliminary | The relevant terms remain unreviewed, so the assessment cannot accurately be described as final.
Counsel: "Keep that qualification attached to the ___ circulated internally." | summary | A shortened internal account must retain material limits rather than appear more certain than the underlying analysis.'''))

BOOK['units'].append(unit(
    title='Client Intake, Scope, Conflicts, and Confidentiality', scene='An urgent inquiry before the conflicts review is complete',
    skill='Explain intake limits, request necessary identifiers, and avoid implying accepted representation.',
    brief='A prospective client, Mira, has emailed a detailed dispute account and asks whether to send a demand today. The conflicts review is incomplete. Leo is an intake coordinator, not the reviewing lawyer. The firm\'s procedure requires the parties\' names and related entities before the assigned lawyer can decide whether the firm may accept the matter. No acceptance or advice has been authorized. Mira mentions a possible deadline but supplies no document establishing it.',
    cast='Mira | Prospective client\nLeo | Intake coordinator',
    culture=('Be helpful without implying a decision', 'A friendly intake response can be mistaken for agreement to act. Explain the current status, the information needed, and the limits of your role. Do not imply that unaccepted representation means information can be shared freely; duties concerning prospective clients require appropriate review.'),
    a='''What remains incomplete? | The conflicts review | A signed settlement | A court hearing already held | A confirmed demand strategy | The briefing says conflicts review is unfinished and no advice or acceptance has been authorized.
What may Leo accurately describe? | The intake process and information needed for review | The guaranteed outcome of a demand | The final legal deadline | A confirmed acceptance by the firm | Leo coordinates intake and lacks authorization to provide the requested substantive advice or confirm acceptance.
How should the mentioned deadline be treated? | As an unverified urgent point for the assigned reviewer | As automatically extended by intake | As canceled because no document was attached | As a confirmed filing date calculated by Leo | The possible deadline needs prompt qualified review; intake status neither verifies it nor changes it.''',
    vocabulary='''intake | The process of receiving and assessing an initial inquiry. | complete the intake record
prospective client | A person seeking legal representation or advice. | handle a prospective-client inquiry
engagement | An accepted professional assignment with defined scope. | confirm the engagement scope
engagement letter | A document recording terms of a professional assignment. | review the engagement letter
scope of representation | The matters and services covered by an engagement. | define the scope of representation
conflict check | Review for interests or duties that may affect acceptance. | complete a conflict check
conflict of interest | Competing interests or duties relevant to professional judgment. | assess a potential conflict
adverse party | A person or entity with an opposing interest in the matter. | identify the adverse party
related entity | An organization connected to a relevant party. | list related entities
affiliate | An entity connected through ownership or control in context. | identify corporate affiliates
confidentiality | Duties or expectations restricting use and disclosure of information. | protect confidential information
privilege | A legally recognized protection affecting compelled disclosure in defined circumstances. | assess a privilege question
informed consent | Agreement following adequate information and explanation under applicable rules. | refer informed-consent questions to counsel
waiver | Relinquishment or loss of a right or protection, depending on context. | avoid assuming a waiver
screening | A controlled process limiting involvement or access where applicable. | follow an approved screening process
referral | Direction to another appropriate professional or service. | coordinate a permitted referral
retainer | A term used for an engagement or fee arrangement, depending on context. | clarify the retainer terms
fee arrangement | Terms governing charges for professional work. | explain the approved fee arrangement
matter number | An identifier assigned to a legal matter or inquiry. | reference the matter number
identity verification | Confirmation of relevant identifying information. | complete identity verification
authorization | Permission to perform a specified action. | confirm advice authorization
acceptance | Agreement to take on the specified professional work. | confirm acceptance of the matter
non-engagement | A decision or communication that specified work is not being accepted. | route a non-engagement communication for review
urgent inquiry | A request whose timing may require prompt attention. | escalate an urgent inquiry''',
    precision='Receipt of an inquiry is not a reliable basis for assuming accepted representation or advice. Duties involving prospective-client information can arise independently of a signed engagement letter. Applicable rules and facts require counsel review.',
    precision_extra='Confidentiality and privilege are related but distinct concepts. An intake coordinator should not promise that every message is privileged, decide a waiver question, or treat an incomplete conflict check as clearance.',
    phrases='''Acknowledge receipt | I have received your inquiry and noted the urgency.
State the stage | The conflicts review is still in progress.
Limit the role | I can explain intake, but I am not authorized to advise on the demand.
Request identifiers | Please provide the parties' names and relevant related entities through the approved channel.
Avoid implied acceptance | I cannot confirm that the firm has accepted the matter.
Protect the deadline | Do not assume the intake process changes any existing deadline.
Route the concern | I will flag the possible deadline for the assigned lawyer's review.
Close with a status | The next message will confirm the review status, not a guaranteed outcome.
Separate questions | Acceptance, scope, and advice are separate decisions.
Handle sensitive material | We will handle the information under the applicable intake procedure.
Avoid a privilege promise | Questions about legal protection require the reviewing lawyer's assessment.
Check entity names | Is that the contracting entity or a related trading name?
Confirm receipt only | This acknowledgment confirms receipt, not authorization to send a demand.
Clarify scope | Which specific matter are you asking the firm to assess?
Preserve an unknown | The deadline has been mentioned but not established from a reviewed document.
Refer appropriately | I will ask the authorized reviewer how to communicate the next step.''',
    notes='''Cannot confirm | This states the speaker's information or authority limit without making an unsupported legal conclusion about the relationship.
Still in progress | The phrase marks incomplete review, not a likely outcome.
Receipt versus agreement | "Received" should not be replaced by "accepted" when only a message has arrived.
Named roles | "The assigned lawyer will review" is more specific than "someone will get back to you."
Existing deadline | Preserve the distinction between a deadline's existence and the team's incomplete knowledge of it.
May arise | This wording avoids treating a general professional duty as an identical rule in every jurisdiction.''',
    d='''Which acknowledgment avoids implying substantive advice? | We received your inquiry; conflicts review and any acceptance decision remain pending. | We received your inquiry, so send the demand today. | Your email guarantees that the firm represents you. | No signed letter means the information has no protection. | The first confirms receipt and current process status without authorizing action or making a blanket confidentiality claim.
Which question supports the stated conflict process? | What are the names of the opposing party and related entities? | What result would you like us to guarantee? | Which deadline should we ignore? | Can we circulate the full dispute to unrelated recipients? | The process requires party and entity identifiers to assess potential conflicts.
Which claim exceeds Leo's role? | The proposed demand is legally safe to send today. | The assigned reviewer has been notified. | The conflict review is incomplete. | The inquiry has been received. | A substantive legal recommendation is outside the coordinator's stated authority and has not been approved.
What does confidentiality not automatically establish? | That every communication is protected by evidentiary privilege | That information requires appropriate handling | That access should be controlled under the applicable process | That counsel may need to review a disclosure question | Confidentiality duties and privilege protections have different legal bases and conditions.''',
    dialogue='''Mira | I sent the full dispute account this morning. The supplier is pressing me for a response, and I need to know whether I should send a demand today.
Leo | I have received your [[inquiry::An inquiry is a request for assistance; acknowledging it does not itself authorize advice or establish the acceptance decision.]] and noted the urgency. I coordinate intake, but I am not the lawyer reviewing the proposed demand.
Mira | Does that mean the firm is already acting for me? I assumed opening the email would start the engagement immediately.
Leo | I cannot confirm [[acceptance::Acceptance concerns taking on the specified work; receipt of an email is not a sound basis for the coordinator to confirm that decision.]]. The assigned lawyer must review the matter, including the incomplete conflict check, before we can communicate the authorized position.
Mira | What information is missing for that check? I gave the supplier's trading name, but the contract uses a different company name and I am not sure which matters.
Leo | Please provide both through the approved intake route, along with relevant [[related entities::Related entities may be relevant to the conflict review; using only a trading name can leave the actual parties unclear.]]. The reviewer needs to identify the actual parties rather than assume two names refer to the same organization.
Mira | I can send the contract page identifying them. Should I send every document now, or wait for confirmation of what the review needs?
Leo | Follow the requested [[intake::Intake is the controlled process for receiving and assessing an initial matter; it does not require uncontrolled collection or circulation of every document.]] steps. I will ask the assigned lawyer what additional material is needed and explain the approved channel for providing it.
Mira | I also mentioned a possible deadline at the end of the week. I do not have the notice in front of me, so I cannot confirm its wording.
Leo | I will flag that as an [[urgent inquiry::An urgent inquiry needs prompt attention, but urgency does not verify a deadline or authorize the coordinator to advise.]]. Do not assume our intake process changes any existing deadline. The document and timing need qualified review.
Mira | Thank you. I want to be sure that sending sensitive information before acceptance does not mean it can simply be shared with anyone who asks about the dispute.
Leo | We handle it under the applicable procedure. Questions about [[confidentiality::Confidentiality concerns appropriate use and disclosure of information; prospective-client information may require protection even before a final acceptance decision.]] and the duties arising from your contact go to the reviewing lawyer, not to an assumption that no signed letter means no obligations.
Mira | Is every email I send automatically privileged, then? I was thinking of forwarding the whole exchange to a business partner so they can help me decide.
Leo | I cannot make that [[privilege::Privilege has legal conditions distinct from general confidentiality; the coordinator cannot guarantee that every message or onward disclosure is protected.]] assessment or advise on onward disclosure. I will refer the question to the lawyer instead of promising protection that depends on the circumstances.
Mira | I am asking about the supplier dispute, not the employment issue mentioned in one attachment. Should that distinction be recorded?
Leo | Yes. Clarifying the requested [[scope::Scope identifies which matter or services are being considered; mentioning another issue does not automatically include it in an engagement.]] helps the reviewer understand what work you are seeking. It does not mean that either matter has already been accepted.
Mira | I will provide the names and possible deadline document through that route. Please confirm when the materials reach the reviewer.
Leo | I can confirm [[receipt::Receipt establishes that material arrived; it must not be presented as approval of the demand or acceptance of representation.]] and review status. I cannot promise the firm's decision or recommend sending the demand before authorized advice is available.
Mira | That is clear. I will not read your acknowledgment as permission to act or as confirmation that the firm has undertaken the entire dispute.
Leo | Thank you. I will record those distinctions and seek the authorized [[next step::The next step is the reviewed process action to communicate, rather than an invented promise about advice, acceptance, or the dispute's outcome.]]. The update will address the intake status, the urgent timing question, and who is responsible for further communication.''',
    transfer_title='A former client, a new dispute',
    transfer_setup='A former client emails a new supplier dispute. The prior engagement concerned a different matter. The new conflicts and scope reviews are incomplete, and an assistant has no authority to accept it.',
    transfer='''Assistant: "We received your new ___ about the supplier." | inquiry | A prior engagement does not make every new request an accepted matter without the appropriate assessment.
Client: "Does the earlier engagement establish the new ___?" | scope | Scope identifies the work covered; the new supplier dispute is distinct from the earlier assignment.
Assistant: "The new conflicts review and acceptance decision remain ___." | pending | The reviews are incomplete, so acceptance cannot accurately be reported as confirmed.
Client: "Please route the question to the authorized ___." | reviewer | The assistant can coordinate communication while the authorized reviewer makes the relevant assessment.'''))

BOOK['units'].append(unit(
    title='Litigation Lifecycle: Pleadings, Motions, Deadlines, Strategy', scene='Two dates in the task list, neither verified as controlling',
    skill='Escalate a deadline discrepancy and distinguish a calendar entry from verified procedural authority.',
    brief='A litigation task list shows 12 October from an internal planning email and 15 October from a document labeled proposed schedule. The team has not located a signed scheduling order or confirmed the applicable deadline rules. Elise coordinates the file; Karim is supervising litigation counsel. No extension has been confirmed. Counsel must verify the controlling deadline; the team cannot treat the later date as approved merely because it appears in a document.',
    cast='Elise | Litigation coordinator\nKarim | Supervising litigation counsel',
    culture=('Raise the discrepancy early and neutrally', 'A deadline conflict calls for precise escalation, not a guess based on the most convenient date. Identify both sources, mark their status, and ask the responsible lawyer to verify the controlling authority. A reminder in a calendar is not itself an extension or court order.'),
    a='''Where does 15 October currently appear? | A document labeled proposed schedule | A located signed order | A confirmed court extension | An approved final judgment | The later date is in a proposal, not a verified order or extension.
What has not been confirmed? | The controlling deadline and any extension | Whether the task list has two dates | Whether an internal email exists | Whether counsel supervises the matter | The case supplies conflicting sources but no verified controlling date or extension.
Who must verify the deadline? | Karim, supervising counsel | The calendar software by itself | An unrelated client contact | The later-dated document automatically | The briefing assigns verification to supervising counsel, using the relevant authoritative sources.''',
    vocabulary='''pleading | A formal document stating a party's position in litigation. | review the pleading
complaint | A document commencing a civil claim in relevant systems. | identify the filed complaint
answer | A formal response to a complaint under applicable procedure. | prepare an answer for review
motion | A request for a court to make an order or decision. | file a motion when authorized
brief | A written presentation of legal argument in context. | review the supporting brief
hearing | A proceeding before a court or decision-maker. | confirm the hearing details
order | A direction or decision issued by the court. | locate the signed order
scheduling order | A court order setting procedural dates or requirements. | verify the scheduling order
docket | The court's record or list of proceedings and filings. | check the docket record
filing | Submission of a document through the applicable court process. | verify filing status
service | Formal delivery of legal documents under applicable rules. | confirm service details
proof of service | A record supporting that formal delivery occurred. | review proof of service
deadline | The time by which a required action must occur. | verify the controlling deadline
extension | An authorized enlargement of the applicable time period. | confirm an extension
stipulation | An agreement between parties with context-dependent procedural effect. | review a proposed stipulation
proposed order | Draft wording submitted for possible court adoption. | distinguish a proposed order from an issued order
entered order | An order recorded through the court's process. | verify entry of the order
calendar entry | An internal scheduling record or reminder. | reconcile calendar entries
procedural posture | The stage and current status of litigation. | explain the procedural posture
jurisdiction | A court's authority or the relevant legal system in context. | identify the relevant jurisdiction
venue | The proper geographical location or forum for a proceeding. | distinguish venue from jurisdiction
continuance | A postponement of a proceeding under applicable procedure. | confirm a granted continuance
default | A failure to take a required procedural step, with context-specific consequences. | avoid an unsupported default conclusion
case management | Coordination of litigation steps and progress. | update the case-management record''',
    precision='Proposed, requested, agreed, signed, entered, and effective may describe different procedural states. The controlling source and legal effect require counsel review. This fictional exercise supplies no rule for calculating an actual deadline.',
    precision_extra='A filing deadline and service deadline may differ. A calendar entry can accurately record a date without establishing its legal basis. An unconfirmed extension must not silently replace the current verified obligation.',
    phrases='''Flag the discrepancy | The task list contains two dates from different sources.
Identify each source | Twelve October comes from an internal email; fifteen October appears in a proposed schedule.
Preserve document status | The document is marked proposed, not confirmed as entered.
Request authority | Please verify the controlling order and applicable rule.
Avoid assuming an extension | We have not confirmed any extension of time.
Separate record and rule | The calendar entry records a date; it does not establish its authority.
Assign verification | Counsel needs to confirm which deadline governs this task.
Close the escalation | I will keep the discrepancy visible until the verified instruction is recorded.
Clarify the action | Does this date concern filing, service, or a hearing?
Check a version | Is this the latest issued order or a circulated draft?
Avoid convenience-based choice | We should not choose the later date because it gives more time.
Preserve the earlier warning | Do not remove the earlier reminder without verified instructions.
Record provenance | Attach the source and review status to the confirmed calendar instruction.
Report missing material | The signed scheduling order has not yet been located.
Distinguish a request | A requested extension is not a confirmed extension.
Confirm the handoff | Please acknowledge who is verifying the deadline and when the team will be updated.''',
    notes='''Proposed as a modifier | Retain proposed whenever naming a draft schedule; dropping it changes the apparent status.
Which governs | This asks about controlling authority rather than simply asking which date the team prefers.
Has been confirmed | The perfect tense connects an approval or verification event to the present status.
Filing versus service | Name the procedural act; "the document deadline" may combine distinct requirements.
Pending verification | This phrase must lead to an assigned verification task, not an indefinite postponement of attention.
Negative evidence | Not locating an order does not establish that no order exists.''',
    d='''Which update preserves the document status? | The later date appears in a proposed schedule; counsel has not confirmed it controls. | The court approved the later date because it appears in a file. | The internal email automatically overrides every order. | The deadline is extended because the team requested more time. | The first distinguishes a proposed date from a verified controlling deadline.
Which question narrows the procedural task? | Does the date govern filing, service, or the hearing? | Which date is easiest for the team? | Which document has the most attractive layout? | Can the discrepancy be removed from the report? | Different procedural acts can carry different requirements, so identifying the act is essential to accurate communication.
What does an unconfirmed extension request establish? | A request has been made, not that more time is authorized. | Every deadline is automatically suspended. | The later requested date now controls. | No further verification is needed. | Requesting time and obtaining an effective extension are different procedural states.
Which record is most useful after counsel verifies the instruction? | The date, required act, authoritative source, and confirmation owner | Only the later number without a source | A deleted history of the earlier discrepancy | A statement that all future deadlines are settled | A sourced, action-specific instruction makes the verified result usable without hiding its basis.''',
    dialogue='''Elise | I found two dates for the response task: 12 October in the planning email and 15 October in a document called proposed schedule. Which should I put on the calendar?
Karim | Keep both sources visible while I verify the [[deadline::The deadline is the legally applicable time requirement; neither an internal email nor an unverified proposal alone establishes it.]]. Has anyone located an issued scheduling order or confirmed an extension affecting this task?
Elise | Not yet. The later document was circulated by the other team, but our copy does not show that the court signed or entered it. I nearly treated its title as enough.
Karim | Retain the word [[proposed::Proposed identifies draft or requested terms, not a confirmed court direction; removing the modifier would overstate the document's status.]] in every update. We cannot turn a circulated schedule into an effective court direction just by copying its date into our task list.
Elise | I will check the authorized file sources and flag the missing order. Should I also confirm whether the response task means filing the document or serving it?
Karim | Yes. [[Filing::Filing is submission through the court process; it is not necessarily the same act or deadline as formal delivery to another party.]] and service can be different requirements. Identify the procedural act before we try to resolve a date attached to an imprecise task description.
Elise | The email simply says response due. I will preserve that wording rather than silently changing it to a filing instruction.
Karim | Good. We need the relevant rule, order, and [[procedural posture::Procedural posture is the current stage and status of the case, which can affect how a deadline question should be analyzed.]]. I will verify the legal effect; you can gather the sources and their recorded status.
Elise | A colleague favors the later date because its document looks more formal and gives us enough preparation time.
Karim | Appearance and convenience do not establish [[authority::Authority supplies the controlling legal or procedural basis; a document's polished format or convenient date does not provide it.]]. Do not remove the earlier reminder without verified instructions while we resolve the discrepancy promptly.
Elise | I will mark the conflict unresolved and name you as reviewer, so nobody mistakes the later entry for a settled extension.
Karim | Exactly. A requested [[extension::An extension is effective additional time under the applicable process; a request or proposal alone does not confirm that status.]] is not a confirmed one. If the record shows a request, report the request and keep its outcome separate.
Elise | What should I tell the team now? They need to plan work, but I do not want an administrative update to sound like an opinion on which deadline controls.
Karim | Say that two sources conflict and counsel is verifying the [[controlling source::The controlling source is the authority whose legal effect governs the task; identifying it is the unresolved review question.]]. Identify the missing material, the owner, and the urgency without suggesting the uncertainty permits delay.
Elise | Once you confirm the instruction, I will record the required act, date, source reference, and who verified it. Should the earlier conflicting entries remain in the history?
Karim | Preserve the appropriate [[audit trail::An audit trail retains how the discrepancy was resolved, allowing the team to understand the basis of the final calendar instruction.]] under the firm's procedure. Correct the operational instruction clearly, but do not erase the reason we investigated the mismatch.
Elise | I will also check whether any dependent preparation tasks used the later date. A correction could affect review time even if the filing work itself has not started.
Karim | That is useful [[case management::Case management coordinates the work and dependencies around litigation; it supports, but does not replace, counsel's legal verification.]]. Keep those planning consequences separate from the legal determination so the team knows which question each update answers.
Elise | I will gather the records now and send the discrepancy to you with both dates still qualified. The team will receive the verified instruction after your review.
Karim | Thank you. A clear [[handoff::A handoff transfers the sources, unresolved question, and assigned responsibility, preventing an administrative calendar choice from becoming unsupported legal advice.]] makes this safer: known sources, unknown controlling effect, named reviewer, and no assumption that a later date is automatically available.''',
    transfer_title='A hearing postponement has only been requested',
    transfer_setup='A lawyer has requested that a hearing be postponed. The team has a copy of the request but no confirmation that it was granted. An assistant is updating internal reminders.',
    transfer='''Assistant: "The record shows a ___ for postponement, not a granted change." | request | The team has evidence of asking, but no evidence that the court approved the postponement.
Counsel: "Keep the current reminder until the controlling status is ___." | verified | The operational calendar should not assume a requested change has taken effect.
Assistant: "I will identify the source and retain its procedural ___." | status | Describing the document as a request preserves the distinction between proposed and granted relief.
Counsel: "Then route any conflict back to the assigned ___ rather than choosing a convenient date." | reviewer | An authorized reviewer must resolve the legal effect; administrative convenience does not establish it.'''))

BOOK['units'].append(unit(
    title='Discovery, ESI, Privilege Review, and Depositions', scene='An email chain awaiting a privilege decision',
    skill='Describe review status and preserve potentially protected material without making a privilege ruling.',
    brief='Nora is reviewing electronically stored information for a supplier dispute. An email chain discusses commercial terms and includes a lawyer on one message. The chain is in the review set, not the production set. The approved workflow requires uncertain privilege issues to be flagged for Owen, reviewing counsel. A draft production list is due tomorrow, but no release of this chain has been authorized. The team must preserve the original record and explain its current status accurately.',
    cast='Nora | Document reviewer\nOwen | Reviewing counsel',
    culture=('A review flag is not a legal determination', 'Discovery conversations move quickly between operational labels and legal judgments. State whether an item was collected, reviewed, withheld, or produced. A lawyer appearing on an email is a fact to assess, not by itself a complete privilege analysis.'),
    a='''Where is the chain now? | In the review set | Already produced to the opposing party | Deleted from the collection | Filed publicly with the court | The briefing places the chain in review and expressly says it is not in the production set.
Who should decide the uncertain privilege issue under this workflow? | Owen, reviewing counsel | Nora acting without review | The commercial sender alone | Anyone who sees a lawyer's name | The assigned workflow routes uncertain privilege questions to reviewing counsel rather than treating a name as decisive.
What does tomorrow's draft-list deadline authorize? | Preparing an accurate status list, not releasing the chain | Producing every collected document | Deleting uncertain items | Declaring all copied lawyers' emails privileged | A planning deadline does not change the item's unapproved release status or settle its legal classification.''',
    vocabulary='''discovery | A process for obtaining relevant information in litigation under applicable rules. | manage discovery requests
ESI | Electronically stored information, including email and other digital records. | review collected ESI
custodian | A person associated with the control or location of relevant records. | identify a document custodian
collection | Gathering potentially relevant records through an authorized process. | document the collection process
preservation | Maintaining relevant information against inappropriate alteration or loss. | follow preservation instructions
legal hold | Instructions to preserve information for a legal matter. | issue an authorized legal hold
review set | Documents made available for examination and classification. | inspect the review set
production set | Documents selected and prepared for disclosure through an authorized process. | approve the production set
responsiveness | Whether material falls within the scope of a relevant request. | assess responsiveness
relevance | The relationship of information to an issue in the matter. | evaluate relevance
privilege review | Assessment of whether a legal protection applies to information. | escalate a privilege-review question
work product | A protection for specified litigation-preparation material under applicable law. | assess a work-product claim
redaction | Removal or masking of specified content from a disclosure copy. | approve a targeted redaction
privilege log | A record describing withheld material as required by applicable procedure. | prepare a privilege-log entry
metadata | Data describing a file, such as dates, authorship, or system attributes. | preserve relevant metadata
email thread | Related messages in a continuing email exchange. | review the complete email thread
attachment family | A parent document and its associated attachments. | keep an attachment family linked
deduplication | Identification or removal of duplicate copies in a controlled workflow. | document the deduplication method
Bates number | A sequential identifier applied to document pages in legal review or production. | cite the Bates number
clawback | A mechanism for seeking return or protection of inadvertently disclosed material. | review the applicable clawback procedure
deposition | Testimony taken outside trial under applicable procedural rules. | prepare for a deposition
exhibit | Material identified for use in testimony or a proceeding. | mark a deposition exhibit
transcript | A written record of spoken testimony or proceedings. | check the deposition transcript
review protocol | Instructions governing document assessment and escalation. | follow the review protocol''',
    precision='Relevance, responsiveness, and privilege answer different questions. Material may respond to a request yet require protection or redaction. A review flag records an unresolved issue; it does not authorize withholding or production on its own.',
    precision_extra='Collection is not production. Redaction of an approved disclosure copy is not permission to alter the preserved original. Clawback protections depend on the governing arrangements and law; do not assume an accidental disclosure can always be undone.',
    phrases='''Locate the item | The chain remains in the review set.
Flag uncertainty | I have flagged a potential privilege issue for counsel.
Avoid a shortcut | The copied lawyer's name does not resolve the classification.
Preserve context | Please review the full thread and linked attachments.
Separate questions | Responsiveness and privilege require separate assessments.
State the hold | This item has not been authorized for production.
Identify the reference | The review identifier is R-214; no production number is assigned.
Close the loop | I will update the status after counsel records the decision.
Describe preservation | The original record and its relevant metadata remain unchanged.
Qualify a draft | This list identifies pending review, not final withholding decisions.
Request instructions | Does the protocol require a separate entry for each attachment?
Limit a redaction | Which passages are approved for redaction in the disclosure copy?
Check terminology | Are you asking whether it was collected or whether it was produced?
Escalate timing | The review question remains unresolved ahead of the draft-list deadline.
Separate testimony | The witness's recollection and the email record should be identified separately.
Confirm release | Please confirm the authorized production version before release.''',
    notes='''Status verbs | Collected, reviewed, approved, and produced name different stages and must not be used interchangeably.
Potential versus established | A potential privilege issue is a reason for assessment, not a completed legal conclusion.
Still and yet | "Still in review" and "not yet approved" communicate an unfinished state without predicting the outcome.
Original versus copy | Name which version may be changed so a redaction instruction cannot be mistaken for alteration of evidence.
Identifier precision | Distinguish an internal review identifier from a Bates number assigned for a particular production.
Agent clarity | "Counsel approved the redaction" is clearer than "the redaction was approved" when authority matters.''',
    d='''Which status statement is supported? | The chain is flagged for counsel review and has not been produced. | The chain is privileged because a lawyer was copied. | The chain was disclosed when it was collected. | The draft list authorizes production. | The supported statement reports the actual workflow stage without deciding privilege or inventing a release.
Which term refers to data about a file? | metadata | deposition | remedy | pleading | Metadata describes attributes of the file; it is distinct from testimony, relief, and formal case documents.
Which instruction preserves the original? | Apply only approved redactions to the disclosure copy. | Delete the original passages before review. | Replace the preserved thread with a summary. | Remove all attachments to simplify the record. | A controlled disclosure copy can be redacted while the original is preserved under the applicable process.
Which phrase properly limits a review flag? | A potential issue requiring counsel's assessment | A final ruling that no disclosure is required | An automatic waiver of protection | Permission to produce without further approval | A flag identifies uncertainty and its next reviewer, not the legal outcome.''',
    dialogue='''Nora | I found a chain about revised supplier terms. A lawyer appears on one message, so I flagged it instead of moving it into the production list.
Owen | Describe it as a potential issue in [[privilege review::Privilege review is the assessment stage; it does not mean the protection has already been established.]], not a final finding. Where is the chain currently located?
Nora | It is in the review set under R-214. Nothing from this chain has been released, and the original messages remain unchanged in the collection.
Owen | Keep that [[status::Status identifies the document's actual workflow stage, preventing collection or review from being mistaken for completed disclosure.]] explicit. A lawyer's presence may matter, but we need the content, purpose, participants, and applicable legal framework.
Nora | The opening messages concern price changes. A later message asks the lawyer a question, and two attachments appear relevant to the commercial discussion as well.
Owen | Retain the full [[email thread::The complete email thread supplies context for the different messages; a single isolated line may not support accurate classification.]] and identify those attachments. Different parts may require different treatment, but the relationships must remain visible.
Nora | Should I mark the entire family nonresponsive while you assess it? That would remove it from tomorrow's draft list and avoid a premature disclosure decision.
Owen | No. [[Responsiveness::Responsiveness concerns the scope of a request, not whether a legal protection may apply; changing that label would hide a separate question.]] answers a different question. Use the pending-review status in our protocol; do not hide uncertainty with an inaccurate classification.
Nora | Understood. The list will show that the item may respond to the request but awaits your privilege decision. It will not describe the material as finally withheld.
Owen | If a [[redaction::A redaction masks approved content in a disclosure copy; it is not permission to change the preserved original or redact without authorization.]] is appropriate, I will identify the approved passages and version. Do not alter the preserved original to prepare that copy.
Nora | The platform displays creation and modification dates as well as email headers. I will retain those fields with the item rather than copying only visible text.
Owen | That preserves relevant [[metadata::Metadata contains file attributes that may support review context; retaining only visible text can omit important information.]]. Record processing issues separately so we do not mistake a display problem for a missing original message.
Nora | Should I use R-214 or invent a production number for tomorrow's list? No final sequence has been assigned, and I want the reference to remain traceable.
Owen | Use the internal identifier. A [[Bates number::A Bates number identifies pages in a legal document sequence; inventing one could misleadingly imply an assigned production reference.]] should come from the authorized numbering process, not an estimate added to make the list look finished.
Nora | If your decision is to withhold material, I can prepare the required descriptive entry for review without including the substance of any protected advice.
Owen | Follow the applicable [[privilege log::A privilege log describes withheld material according to governing requirements; its contents need review and should not reveal the claimed protected substance.]] requirements and our instructions. Check the description and asserted basis; do not copy them automatically from another matter.
Nora | A colleague suggested producing now and retrieving it later if necessary. I have not acted on that suggestion because the release decision remains unresolved.
Owen | Do not assume a [[clawback::A clawback mechanism may address inadvertent disclosure under applicable arrangements, but it does not justify bypassing the required review.]] eliminates every consequence. Continue the approved review and escalate timing concerns instead of relying on a possible later remedy.
Nora | I will send the full chain, attachment references, current classification, and tomorrow's timing to you. The draft list will show pending counsel review without implying approval.
Owen | That is a useful [[handoff::A handoff transfers the item, context, unresolved question, and responsibility; those details allow counsel to decide without guessing the workflow history.]]. Once I record the decision, update the list and route the correct version through the authorized release process.''',
    transfer_title='An exhibit contains an unreviewed attachment',
    transfer_setup='A deposition preparation folder contains an email and a linked attachment. The email has been reviewed, but the attachment has not. The folder is internal; no exhibit release is authorized.',
    transfer='''Reviewer: "The attachment remains ___, even though the parent email has been checked." | unreviewed | Review of one item does not establish that a linked attachment has received the same assessment.
Counsel: "Keep the document ___ visible so the relationship is not lost." | family | The family connects the parent email with its attachment and preserves useful review context.
Reviewer: "I will flag the pending question before any exhibit ___." | release | The case permits internal preparation, not disclosure of unreviewed material as an exhibit.
Counsel: "Record my decision in the review ___ before updating the preparation set." | history | A recorded decision makes the authorization and sequence traceable rather than relying on an informal assumption.'''))

BOOK['units'].append(unit(
    title='Legal Research, Authority, and Memo Writing', scene='A persuasive decision described as controlling',
    skill='Compare authorities and explain a qualified recommendation without overstating precedent.',
    brief='Jon, an associate, has found a published appellate decision from another jurisdiction supporting a supplier-notice argument. His draft memorandum calls it controlling. Priya, supervising counsel, has asked for the governing forum, relevant statutory text, later treatment, and factual differences to be checked. Those checks are incomplete. The cited case involved written notice; this client used a telephone call. No recommendation has been approved for the client.',
    cast='Jon | Associate\nPriya | Supervising counsel',
    culture=('Strength comes from an accurate limitation', 'A useful research update identifies the best support and the strongest limitation in the same discussion. A confident voice is compatible with a qualified conclusion. Do not make an authority sound binding merely because it supports the preferred outcome.'),
    a='''What is the known source of the decision? | An appellate court in another jurisdiction | The identified controlling court in this matter | An unsigned client email | A final order in this client's case | The briefing locates the decision elsewhere; its controlling effect has not been established.
Which factual difference is already known? | Written notice in the decision versus a telephone call here | Identical written notices in both matters | A final judgment against this client | No notice of any kind in the cited decision | The notice method differs and may affect whether the decision's reasoning can be applied by analogy.
What must happen before the recommendation is approved? | The requested authority and factual checks | Removal of all unfavorable information | Automatic adoption of the supporting case | Replacement of the case citation with an assurance | Counsel requested checks of forum, text, treatment, and differences because the preliminary research does not settle the issue.''',
    vocabulary='''authority | A legal source used to support or govern an analysis. | evaluate the cited authority
binding precedent | A prior decision that a court must follow within applicable limits. | identify binding precedent
persuasive authority | A source that may influence reasoning without controlling the result. | rely on persuasive authority
jurisdiction | A legal territory or scope of a court's authority, depending on context. | confirm the relevant jurisdiction
hierarchy | The ordering of courts or sources that affects their relative authority. | map the court hierarchy
holding | A court's determination of an issue necessary to its decision. | identify the holding
dicta | Judicial observations not necessary to the decision's holding. | distinguish dicta from the holding
ratio decidendi | The legal reasoning necessary to a decision in systems using this term. | identify the ratio decidendi
statutory text | The wording of an enacted law. | examine the statutory text
regulation | A rule issued through an authorized administrative process. | check the applicable regulation
legislative history | Materials concerning the development of legislation. | assess relevant legislative history
secondary source | Commentary explaining or analyzing law rather than establishing it directly. | consult a secondary source
citation | A reference identifying a legal source or passage. | verify the citation
pinpoint citation | A reference to the precise location of supporting material. | add a pinpoint citation
subsequent treatment | How later authorities have addressed a decision. | check subsequent treatment
overruled | Displaced as precedent by an authorized later decision. | check whether the decision was overruled
distinguished | Treated as different in a way that limits an earlier decision's application. | explain why the case was distinguished
analogous | Similar in legally relevant respects. | identify analogous facts
material distinction | A difference that may affect the legal analysis. | address a material distinction
procedural posture | The stage and context in which a court decided an issue. | compare procedural posture
standard of review | The approach a reviewing court applies to a challenged determination. | identify the standard of review
counterargument | A reasoned position against the proposed analysis. | address the strongest counterargument
research memorandum | An organized explanation of a legal question, sources, and analysis. | revise the research memorandum
synthesis | A combined account of principles drawn from multiple sources. | develop a qualified synthesis''',
    precision='A published decision is not automatically binding in another forum. Court hierarchy, jurisdiction, issue, and governing law matter. A database excerpt or summary can locate an issue but should not replace reading the relevant decision and checking its treatment.',
    precision_extra='Distinguishing a decision does not mean it has been overruled. A holding and dicta have different analytical roles. Preserve the actual basis of the court\'s decision rather than using every favorable sentence as though it resolved the present issue.',
    phrases='''Qualify authority | This decision is potentially persuasive; controlling effect is not established.
Identify the forum | We first need to confirm which jurisdiction's law governs this issue.
Locate support | The relevant reasoning appears in the cited passage, not the summary heading.
State a difference | The decision involved written notice; our facts involve a telephone call.
Separate status | The later court distinguished the case rather than overruling it.
Check treatment | I will verify subsequent treatment before relying on the decision.
Frame the recommendation | The argument is available, subject to the governing text and factual distinction.
Close with limits | The memorandum will state both the supporting reasoning and the unresolved checks.
Distinguish reasoning | Is that proposition part of the holding or an observation beyond it?
Avoid a shortcut | Publication alone does not establish binding effect in this forum.
Request precision | Which passage supports that specific proposition?
Compare the stage | The cited decision arose on a different procedural posture.
Preserve an objection | We should address the notice-method distinction rather than omit it.
Explain a secondary source | The commentary helps locate the issue but is not itself the governing enactment.
State an assumption | This section assumes that the identified law governs; that remains to be verified.
Give a bounded update | I have found support for the argument, not a guaranteed outcome.''',
    notes='''Controls versus supports | Controls claims governing effect; supports describes assistance to an argument and requires less sweeping authority.
Although clauses | "Although the reasoning helps, the notice method differs" puts support and limitation in a single clear sentence.
On these facts | This phrase confines a proposition to an identified factual setting instead of announcing a universal rule.
By analogy | Explain the relevant similarity and difference when applying reasoning from a different factual situation.
Negative treatment | Name what a later court did; criticized, distinguished, and overruled are not synonyms.
Citation verbs | "The court held" should introduce a holding, while "the court observed" may signal a less central statement.''',
    d='''Which wording avoids overstating the decision? | It may support the argument by analogy, subject to further checks. | It guarantees success because it was published. | It controls every court that hears a notice dispute. | It eliminates the need to read the statute. | The qualified wording preserves both the potential relevance and the incomplete authority checks.
Which phrase names later courts' handling of a case? | subsequent treatment | client intake | service of process | document collection | Subsequent treatment concerns later legal attention to a decision, including limits or changes to its force.
Which sentence preserves the known factual difference? | The cited case used written notice, whereas our client called. | Both cases involved the same written notice. | Notice method is conclusively irrelevant. | The court ruled on this client's telephone call. | Whereas explicitly contrasts the two known methods without inventing a legal ruling about their significance.
Which action best supports a precise source reference? | Add the page or paragraph supporting the proposition. | Cite only a search-result headline. | Remove the court and year. | Refer vaguely to a well-known case. | A pinpoint citation lets the reader verify the exact passage and assess whether it supports the claimed proposition.''',
    dialogue='''Jon | I found a published appellate decision supporting our notice argument. My draft says it controls, but I have not finished checking the governing forum or later cases.
Priya | Change that label for now. It may be [[persuasive authority::Persuasive authority may influence the analysis without binding the relevant court; the outstanding forum check prevents a stronger conclusion.]], but another jurisdiction's published decision does not automatically govern this matter.
Jon | The favorable paragraph says the notice served its purpose. I relied on that language, although the case involved a letter and our client made a telephone call.
Priya | That difference may be a [[material distinction::A material distinction is a difference that could affect the reasoning; the notice method cannot simply be treated as identical.]]. Identify the actual notice requirement before deciding how closely the facts align.
Jon | I will retrieve the relevant provision and check which law applies. The commentary I consulted discusses practical notice, but it does not reproduce the complete provision.
Priya | Read the [[statutory text::Statutory text supplies the enacted wording; commentary can assist research but does not replace checking the provision itself.]] in its proper context and current form. Identify any applicable definitions or qualifications instead of relying only on the commentary's shorthand.
Jon | Should I keep the favorable paragraph in the memorandum while those checks are open? Removing it entirely would hide an argument that could still help the client.
Priya | Keep it with accurate status. Then establish whether the proposition is the [[holding::The holding resolves an issue necessary to the court's decision; a favorable observation may carry a different analytical role.]] or a broader observation not necessary to the decision.
Jon | The court also discussed an alternative ground. I need to trace which ground supported the result before describing every sentence as a rule we can invoke.
Priya | Exactly. Check the [[procedural posture::Procedural posture identifies the stage and context of the decision, which can limit what the court actually decided.]] too. A decision about whether allegations suffice may not establish the final facts or liability after evidence is tested.
Jon | One later decision cites this case but reaches the opposite outcome. The brief summary says the notice circumstances were different, not that the earlier decision was rejected.
Priya | Describe that as a case potentially being [[distinguished::A distinguished case is treated as different in a legally relevant way; that does not itself mean its precedent was overruled.]], pending your full reading. Do not substitute overruled simply because the outcomes differ.
Jon | I will read the later decision and complete the treatment check. The initial search result is useful for locating it, but not enough to describe its reasoning.
Priya | Good. Record the [[subsequent treatment::Subsequent treatment reports how later authorities handled a decision and helps assess whether reliance remains justified.]] accurately and verify the citation. The reader needs the actual authority, not a compressed label copied without examination.
Jon | For the analysis section, I can explain the functional-notice argument and then address the written-versus-oral difference. That gives the reviewing lawyer both sides of the comparison.
Priya | Include the strongest [[counterargument::A counterargument identifies a reason against the proposed position; including the known notice-method objection prevents a one-sided recommendation.]]. A useful memorandum tests the recommendation, rather than gathering only sentences that favor our preferred result.
Jon | I will also replace the broad citation with the specific paragraph supporting the proposition. That should make it easier to check whether my summary is faithful.
Priya | A [[pinpoint citation::A pinpoint citation identifies the exact supporting location, enabling the reviewer to verify the claim instead of searching an entire decision.]] helps. Keep the quotation brief and make your own reasoning explicit; the passage should support the analysis rather than stand in for it.
Jon | My revised update will say we have a potentially useful analogy, with governing law, treatment, and the notice-method difference still under review. It will not promise a result.
Priya | That is an appropriately bounded [[recommendation::A recommendation should reflect the support and unresolved limits of the analysis; it is not a guarantee that the argument will succeed.]]. Send the revised memorandum with the outstanding checks clearly identified before anything goes to the client.''',
    transfer_title='A summary article is not the regulation',
    transfer_setup='An assistant finds a trade article saying a regulatory exception applies broadly. The team has not checked the current regulation, defined terms, or amendments. Counsel has requested the underlying sources.',
    transfer='''Assistant: "The article is a ___ source, not the governing regulation." | secondary | Commentary explains a rule but does not itself establish the enacted or issued requirements.
Counsel: "Retrieve the current ___ and relevant definitions." | text | The wording and definitions are needed to assess the actual scope rather than rely on a summary.
Assistant: "I will flag the claimed exception as ___ until that review." | unverified | The trade article alone does not establish whether the exception applies to the present facts.
Counsel: "Keep the source references attached to the research ___." | memorandum | The memorandum should allow a reviewer to trace and check the analysis against its underlying sources.'''))

BOOK['units'].append(unit(
    title='Contracts, Redlines, and Negotiation', scene='Changing delivery time without conceding the whole clause',
    skill='Propose a precise amendment, preserve linked terms, and distinguish a negotiating position from acceptance.',
    brief='A draft services agreement requires delivery within ten days after a purchase order. Operations needs fifteen business days after receipt of complete specifications. The draft does not define business day or explain incomplete specifications. Elena, commercial counsel, and Marcus, operations director, are preparing a proposed redline. The customer has not accepted any change, and neither participant has approval to concede remedies or liability limits. Their task is to define the proposed timing change and identify related questions for review.',
    cast='Marcus | Operations director\nElena | Commercial counsel',
    culture=('Negotiate the variable, not an undefined package', 'A conversational "that works" may hide different assumptions about the clock, trigger, or scope of agreement. Restate the exact proposed term and identify what remains unchanged or unresolved. A redline is a proposal until the relevant approvals and agreement are established.'),
    a='''What timing does operations need? | Fifteen business days after complete specifications are received | Ten days after any purchase order | Fifteen calendar days after signature | Unlimited time with no trigger | The briefing specifies both a business-day period and receipt of complete specifications as its proposed starting event.
What has the customer accepted? | No change yet | The complete proposed redline | Removal of all remedies | A new liability cap | The proposed changes are still being prepared and the customer has not accepted them.
What falls outside the participants' current approval? | Conceding remedies or liability limits | Identifying undefined timing terms | Preparing a proposed redline | Explaining the operational requirement | Their authority covers preparation and review, not the stated concessions on remedies or liability.''',
    vocabulary='''redline | A version showing proposed changes to existing wording. | circulate a proposed redline
markup | Edits or comments displayed on a draft document. | reconcile competing markups
operative clause | Wording that establishes a substantive term or obligation. | revise the operative clause
defined term | A word or phrase assigned a specified meaning in a document. | use the defined term consistently
business day | A working day as defined by the relevant agreement or rule. | clarify the business-day definition
trigger event | The occurrence that starts an obligation or time period. | identify the trigger event
condition precedent | An event that must occur before a specified duty or effect arises. | review the proposed condition precedent
covenant | A contractual promise to do or refrain from doing something. | assess the covenant wording
representation | A statement of fact with legal significance in context. | qualify the representation
warranty | A contractual assurance whose effect depends on its terms and governing law. | review the warranty scope
indemnity | An obligation to bear specified losses or liabilities under agreed terms. | negotiate the indemnity provision
limitation of liability | A clause restricting specified liability under defined conditions. | preserve the limitation of liability
liability cap | A stated upper limit on specified liability. | verify the liability cap
carve-out | An exception to a provision's general scope. | define the carve-out narrowly
cure period | Time allowed to remedy a specified failure. | negotiate the cure period
termination right | A contractual ability to end an agreement under stated conditions. | clarify the termination right
notice provision | Terms governing how required notices are given. | follow the notice provision
order of precedence | A rule for resolving conflicts among contract documents. | check the order of precedence
entire agreement clause | A clause addressing which materials comprise the parties' agreement. | review the entire agreement clause
amendment mechanism | The required process for changing an agreement. | follow the amendment mechanism
effective date | The date from which an agreement or change has stated effect. | confirm the effective date
execution copy | A version prepared for signing after the required review. | verify the execution copy
fallback position | An alternative negotiating position available within authority. | confirm the approved fallback position
reservation of rights | A statement intended to preserve identified rights or positions. | review the reservation of rights''',
    precision='Ten days after a purchase order and fifteen business days after complete specifications differ in both duration and trigger. Replacing only the numeral leaves the operational problem unresolved. The relevant calendar and completion standard also need clear drafting.',
    precision_extra='A proposed redline is not an execution copy. A commercial concession on timing does not automatically approve a change to remedies, indemnity, or liability. Authority, agreement, and formal amendment requirements must be checked separately.',
    phrases='''State the requirement | Operations needs fifteen business days after receipt of complete specifications.
Identify both changes | We are proposing a different period and a different starting event.
Clarify the definition | Which calendar does the business-day definition use?
Limit the proposal | This markup addresses delivery timing, not the liability allocation.
Preserve status | The proposed wording remains subject to approval and customer agreement.
Check completeness | We need an objective way to identify the required specifications.
Separate concessions | No change to remedies has been authorized.
Close with a redline | I will circulate the marked clause and list the linked provisions for review.
Avoid ambiguity | Does "received" mean received through the agreed submission channel?
Explain the dependency | We cannot start the production clock without the specified inputs.
Request a fallback | Which alternative timing position has the business approved?
Check interaction | Does the purchase order conflict with the main agreement?
Preserve a limit | Please keep the unresolved calendar definition visible in the comments.
Confirm the version | Is this the approved execution copy or an earlier negotiating draft?
Reject implied acceptance | Preparing the change does not establish customer acceptance.
Make a bounded commitment | I can confirm the proposed wording, not promise that it will be accepted.''',
    notes='''Within versus after | Within sets a deadline relative to a trigger; after names the trigger relationship without necessarily defining the endpoint alone.
Calendar qualification | State calendar or business days when the distinction matters, and check the agreement's definition.
Subject to approval | Attach this phrase to the proposal so internal readiness cannot be mistaken for authorized acceptance.
Without changing | Use this phrase to limit a revision's intended scope, but still inspect linked clauses for unintended effects.
Proposal verbs | Propose and request are different from agree and accept; the verb should match the negotiating stage.
Version language | Draft, redline, clean copy, and execution copy identify document states, not interchangeable file descriptions.''',
    d='''Which proposal captures operations' stated need? | Fifteen business days after receipt of complete specifications | Fifteen days after a purchase order, with no other clarification | Ten business days after a signature | Delivery whenever convenient | The correct proposal preserves both the required duration and the new triggering event.
Which sentence accurately describes authority? | We can propose timing changes, but no remedy concession is approved. | We may waive remedies because timing is difficult. | The customer accepted our internal discussion. | Any marked clause is automatically binding. | The briefing permits preparation of a timing proposal while expressly withholding authority for remedy concessions.
Which phrase identifies competing document priority? | order of precedence | deposition transcript | adverse inference | client intake | An order of precedence addresses conflicts between documents, such as an agreement and a purchase order.
Which status statement is appropriate before customer agreement? | The redline is a proposal subject to approval and agreement. | The execution copy has already been signed. | The original clause has been legally replaced. | The customer has conceded every linked issue. | A draft redline records a proposed change, not acceptance or completion of signing.''',
    dialogue='''Marcus | The draft gives us ten days after the purchase order. Operations needs fifteen business days, and we cannot begin until we have the complete specifications.
Elena | Then the [[redline::A redline shows proposed wording changes, here to both the period and its starting event.]] must change both the period and its starting point. Replacing ten with fifteen would not capture the full operational requirement.
Marcus | Correct. Some orders arrive with missing dimensions. If the clock starts immediately, the team could lose several days waiting for information it needs to perform the work.
Elena | Receipt of complete specifications would be the proposed [[trigger event::The trigger event starts the period; an incomplete purchase order would not satisfy the proposed trigger.]]. We must describe those specifications clearly enough for both parties to identify them.
Marcus | We can list the required inputs in a schedule. I would also like the clause to identify the submission channel, because information sometimes arrives through several contacts.
Elena | That can help, but first confirm the [[defined term::A defined term assigns a specific meaning, allowing the schedule and clause to use one completion standard.]] we will use for complete specifications. The schedule and operative clause should refer to the same standard.
Marcus | The customer operates in a different location. Our team means working days on our production calendar, not every date shown on the customer's office calendar.
Elena | Then the [[business day::Business day needs a relevant definition; the parties cannot assume that different working calendars are identical.]] definition needs express attention. We should not silently assume both parties use the same weekends and holiday calendar.
Marcus | Could we offer a shorter cure period if the customer dislikes the fifteen-day request? That might make the timing change easier for their procurement team to accept.
Elena | We have no approval for that [[concession::A concession gives negotiating ground; changing the cure period could affect remedies beyond the authorized proposal.]]. Keep remedy changes out of this proposal until the authorized decision-maker has assessed the consequences.
Marcus | Understood. I will explain the operational timing need without offering a change to liability. The commercial team can separately decide what alternatives it wants counsel to assess.
Elena | Exactly. Confirm an approved [[fallback position::A fallback position is a negotiating alternative that needs authorization, not an improvised concession.]] before negotiating alternatives. A useful range comes from the business decision, not from language added to make the conversation smoother.
Marcus | The purchase order template also says ten days. Even if we revise the main agreement, that form might continue to carry the old wording into later orders.
Elena | Check the [[order of precedence::The order of precedence addresses conflicting documents; the inconsistent purchase order template still needs review.]] and flag the template. We should resolve the inconsistency rather than rely on a reader to guess which clock applies.
Marcus | I will identify both documents in the review note. For the customer message, can I say we have agreed to fifteen business days internally and ask for confirmation?
Elena | Say we [[propose::Propose identifies suggested wording, not completed approval or customer agreement to a change.]] that wording subject to approval and agreement. Avoid describing internal support as if it completed the contractual change.
Marcus | After approval, we will need a clean version that reflects every accepted change. There are two competing marked files, so the version history needs careful reconciliation.
Elena | Yes. Only the approved [[execution copy::An execution copy is prepared for signing after review; clean appearance alone does not establish approval.]] should go forward for signing. A file without visible markup is not automatically the correct final text.
Marcus | I will send the input list, calendar question, and purchase order conflict with the proposed clause. Remedies and liability will remain outside the authorized change.
Elena | That preserves the proposal's [[scope::Scope defines what the change covers, separating authorized timing revisions from unapproved remedy concessions.]]. We can negotiate clearly once the timing, trigger, and linked definitions are settled for review.''',
    transfer_title='A renewal date changes, but termination language does not',
    transfer_setup='A team is authorized to propose a new renewal date. The notice period and termination rights remain under separate review. The counterparty has not accepted the date change.',
    transfer='''Commercial lead: "Our ___ changes the renewal date only." | proposal | Proposal identifies negotiating status and limits the requested change to the authorized date issue.
Counsel: "Keep the separate notice-period question ___ in the review note." | unresolved | The notice period remains under review and should not appear settled merely because a date is proposed.
Commercial lead: "No change to termination rights is currently ___." | authorized | The facts do not grant authority to concede termination rights as part of the date discussion.
Counsel: "Confirm the accepted wording before preparing the execution ___." | copy | The signing version should reflect approved and accepted wording rather than an unresolved negotiation draft.'''))

BOOK['units'].append(unit(
    title='Corporate, Compliance, Regulatory, and Investigation Language', scene='An interview account is not an investigation finding',
    skill='Attribute evidence, protect the investigation process, and communicate an unresolved allegation neutrally.',
    brief='During an internal interview, an employee tells Ruth, the investigator, that a vendor offered a purchasing manager a personal benefit. The employee did not attend the alleged meeting and says a colleague described it. No transaction records or messages have been reviewed. Ben, the compliance director, must brief a small authorized team. A business manager has asked him to announce that a violation occurred. No finding or disclosure decision has been approved.',
    cast='Ruth | Investigator\nBen | Compliance director',
    culture=('Neutral language protects the inquiry', 'Neutrality is not evasiveness. A report can state a serious allegation clearly while identifying its source and limits. Keep access within the authorized process, avoid promises about absolute secrecy, and do not confuse an interim protective step with a final finding.'),
    a='''What is the employee's knowledge source? | A colleague's account of a meeting the employee did not attend | Personal attendance at the alleged meeting | A reviewed bank transfer | An approved investigation report | The employee relays another person's account, so the report must preserve that source limitation.
What evidence review is already complete? | Neither transaction records nor messages have been reviewed | A full review proving a violation | A regulator's final determination | An independent audit clearing all parties | The briefing expressly says those records remain unreviewed and no finding is approved.
What should Ben communicate to the authorized team? | A reported allegation and the current limits of the inquiry | A confirmed violation | A public accusation approved by counsel | A guarantee that no issue exists | The team needs an accurate status update that does not convert an untested account into an established finding.''',
    vocabulary='''compliance | Adherence to applicable obligations and internal requirements. | assess a compliance concern
internal investigation | An organized inquiry conducted within or for an organization. | scope an internal investigation
alleged misconduct | Conduct reported as potentially improper but not yet established. | describe alleged misconduct neutrally
reporting person | Someone who brings a concern to attention. | protect the reporting person's information
firsthand knowledge | Information gained through direct observation or experience. | distinguish firsthand knowledge
secondhand account | Information received from another person's description. | attribute a secondhand account
interview record | A documented account of an investigative conversation. | verify the interview record
corroborating record | Material that independently supports a reported point. | seek a corroborating record
finding | A conclusion reached through an identified review process. | approve an investigation finding
substantiated | Supported to the relevant standard in the applicable process. | explain a substantiated finding
unsubstantiated | Not established to the relevant standard on the available review. | distinguish unsubstantiated from disproved
exculpatory information | Information tending against responsibility or an allegation. | preserve exculpatory information
document retention | Rules and practices for keeping records. | follow document-retention requirements
access restriction | A limit on who may view or use information. | apply an authorized access restriction
need to know | A purpose-based limit on information access. | restrict access on a need-to-know basis
retaliation | Adverse treatment connected to protected reporting or participation in context. | escalate a retaliation concern
non-retaliation | A policy or obligation against improper adverse treatment for reporting. | explain non-retaliation expectations
remediation | Corrective action addressing an identified issue or weakness. | propose proportionate remediation
interim measure | A temporary step while assessment continues. | explain the purpose of an interim measure
root cause | An underlying factor contributing to a problem. | assess the root cause
control deficiency | A weakness in a process intended to prevent or detect problems. | document a control deficiency
reporting obligation | A duty to provide information to a specified recipient. | assess a reporting obligation
regulatory inquiry | A request or investigation by an oversight authority. | coordinate a regulatory-inquiry response
investigation mandate | The authorized scope and purpose of an inquiry. | confirm the investigation mandate''',
    precision='A secondhand account may identify an important lead, but it is not firsthand observation. A finding requires the appropriate assessment under the applicable process. Unsubstantiated does not necessarily mean false, and an interim measure does not itself establish wrongdoing.',
    precision_extra='Internal confidentiality instructions do not authorize interference with lawful reporting or protected participation. Access, preservation, reporting duties, interview procedures, and legal protections require review under applicable law and policy; do not invent assurances about them.',
    phrases='''Attribute the concern | The employee reports what a colleague described.
State a knowledge limit | The employee did not attend the alleged meeting.
Preserve neutrality | The allegation has not yet been substantiated.
Identify missing evidence | The relevant records and messages remain unreviewed.
Limit distribution | This update is for the specifically authorized review team.
Avoid a guarantee | I cannot promise absolute confidentiality in every circumstance.
Separate action and finding | The interim step does not establish that misconduct occurred.
Close with a review task | We will seek the identified records under the approved investigation process.
Correct overstatement | Please replace "violation confirmed" with the current factual status.
Seek a source | Who directly observed the event described in the account?
Protect completeness | Include information that may support or contradict the allegation.
Preserve records | Follow the approved preservation instruction without altering the originals.
Clarify the mandate | Does the approved scope include this additional transaction?
Flag authority | Any external reporting decision requires the assigned legal review.
Explain status | No final finding or disclosure decision has been approved.
Avoid retaliation | Escalate any concern about adverse treatment through the authorized channel.''',
    notes='''Allegedly | Place this qualifier next to the conduct being reported, not so vaguely that the whole sentence becomes unclear.
Reported speech | "The employee said a colleague described..." preserves the two-stage source chain.
Not established | This phrase limits the finding without implying that the allegation is false.
Status and action | State an interim measure separately from the evidence assessment to avoid suggesting that action proves guilt.
Need to know | Identify the authorized recipients; the phrase alone does not decide who qualifies.
Absolute words | Always, never, and guaranteed can create unsupported promises about confidentiality or outcomes.''',
    d='''Which sentence preserves the source chain? | The employee says a colleague described the alleged offer. | The employee witnessed the offer personally. | The records prove the payment. | The investigation has confirmed a violation. | The employee did not attend, so the report must attribute the information to the colleague's account.
What does unsubstantiated necessarily mean here? | The allegation has not been established under the relevant process. | The reporting person lied. | No inquiry may continue. | All records prove innocence. | Lack of substantiation is not automatically proof of falsity or a judgment about the reporting person's honesty.
Which description avoids treating an interim measure as proof? | The temporary step is precautionary; no finding is approved. | The temporary step proves misconduct. | The temporary step is a final court judgment. | The temporary step eliminates all review duties. | The correct sentence distinguishes a provisional protective action from an evidential or legal conclusion.
Which communication requires additional authorized review? | An external disclosure decision | A neutral update to the authorized review team | Identifying an unreviewed record | Preserving the source of an account | The facts reserve disclosure decisions for approval; internal information gathering does not itself authorize external publication.''',
    dialogue='''Ruth | The employee described a possible personal benefit offered by a vendor. I want the briefing to preserve that the employee heard this from a colleague, not firsthand.
Ben | Then lead with the [[secondhand account::A secondhand account comes through another person's description, not the employee's direct observation of the event.]]. The concern is serious, but the wording must not suggest the employee attended the meeting or saw a payment.
Ruth | No messages or transaction records have been reviewed yet. The interview gives us a lead to follow, and I have recorded the source as the employee described it.
Ben | Say the allegation remains [[unsubstantiated::Unsubstantiated means not established under the relevant process, not that the report is necessarily false.]] at this stage. That status should neither dismiss the concern nor turn it into a finding before the evidence is assessed.
Ruth | The business manager wants an announcement that a violation occurred. I told her no finding has been approved and that the authorized team is still gathering information.
Ben | That is correct. An [[investigation finding::A finding follows the designated assessment process; a manager's desire for certainty cannot replace it.]] must follow the appropriate assessment and approval. We cannot create one simply to make the business update more decisive.
Ruth | I will request the relevant records through the approved process. I also want to identify the colleague who may have direct knowledge of the alleged conversation.
Ben | Good. Seek [[corroborating evidence::Corroborating evidence independently supports an account, allowing the inquiry to test more than the repeated allegation.]], but preserve material that points the other way as well. The inquiry should test the account, not only accumulate support for it.
Ruth | One message may show that the vendor offer concerned a company event rather than a personal benefit. It is only a lead, but it could change the interpretation.
Ben | Include that potential [[exculpatory information::Exculpatory information tends against the allegation; preserving it supports a balanced rather than predetermined inquiry.]] for assessment. Do not resolve its meaning now, and do not leave it out because it complicates the initial theory.
Ruth | For distribution, I have a small list of specifically authorized reviewers. The business manager asked for the interview notes to be sent to the entire department.
Ben | Keep the approved [[access restriction::An access restriction limits distribution; an informal request does not authorize circulation beyond the approved recipients.]]. Route the wider request for review rather than forwarding the notes informally or promising that nobody else will ever see them.
Ruth | The employee asked whether the inquiry would remain completely secret. I explained that information would be handled through the approved process without making an absolute promise.
Ben | That is important. Explain applicable [[non-retaliation::Non-retaliation concerns improper adverse treatment for reporting or participation, not a promise of absolute secrecy.]] expectations through the approved guidance too. Any concern about adverse treatment should reach the designated channel promptly.
Ruth | Operations is considering a temporary change to who approves this vendor's transactions. They want to know whether announcing that step means we have already determined wrongdoing.
Ben | Describe it as an [[interim measure::An interim measure is temporary during review; its existence does not establish that misconduct occurred.]] if that is its approved purpose. State separately that no final finding is authorized; do not let the action imply a conclusion.
Ruth | I will keep the factual chronology, evidence requests, and approval status separate in the update. A potential regulator notification will be listed as a question for legal review.
Ben | Yes. A possible [[reporting obligation::A reporting obligation requires assessment under the applicable framework; the allegation alone does not settle notification duties.]] requires its own assessment. Neither public silence nor immediate disclosure should be assumed correct without that review.
Ruth | The briefing will say what was reported, how the employee learned it, which records remain unchecked, and who owns each next step. It will not name a confirmed violation.
Ben | That fits the current [[investigation mandate::The mandate defines the inquiry's authorized scope; the bounded update supports it without announcing unsupported conclusions.]]. Send it to the approved recipients with the source limitation intact, and escalate any material change through the designated process.''',
    transfer_title='Missing approvals, uncertain intent',
    transfer_setup='A review finds that two invoice approvals were not recorded. The team has not determined why, whether an exception applied, or whether anyone acted deliberately. A manager requests a misconduct label.',
    transfer='''Reviewer: "Missing records do not establish ___." | intent | Missing records do not by themselves prove that a person deliberately acted improperly.
Counsel: "Describe the possible control ___ and required checks." | deficiency | A potential process weakness can be reported without converting it into a concluded misconduct finding.
Reviewer: "The cause and any applicable exception remain under ___." | review | The facts expressly leave those questions unresolved, so the update must not present them as settled.
Counsel: "Separate the temporary step from the final ___." | finding | A provisional action can manage risk while the evidence assessment and conclusion remain incomplete.'''))

BOOK['units'].append(unit(
    title='Advocacy, Settlement, Ethics, and Professional Judgment', scene='Settlement priorities without settlement authority',
    skill='Explain negotiating tradeoffs, distinguish proposals from client instructions, and preserve limits on authority.',
    brief='A dispute team is preparing a settlement discussion. The business contact prioritizes payment within thirty days, while the client decision-maker also wants confidentiality. The opposing side has floated a payment figure but supplied no written terms. Nadia, counsel, and Tomas, the client representative, must prepare the options for the decision-maker. Tomas may collect information but cannot approve a settlement. No release, confidentiality wording, payment schedule, or authority range has been approved.',
    cast='Tomas | Client representative\nNadia | Counsel',
    culture=('Firm advocacy still has boundaries', 'A persuasive presentation makes a position and its reasons clear without manufacturing instructions or promising an outcome. Distinguish what the other side suggested, what the client values, what counsel recommends, and what the authorized decision-maker has actually approved.'),
    a='''Which priority belongs to the business contact? | Payment within thirty days | An unlimited release already accepted | A promise never to report any matter | A final court judgment | The briefing identifies payment timing as that contact's priority, separate from the decision-maker's confidentiality concern.
What can Tomas currently do? | Collect information for the decision-maker | Approve the complete settlement | Accept any floated figure | Sign the release without review | Tomas lacks settlement approval authority, so information gathering must not be represented as acceptance.
Which terms are approved? | None of the listed settlement terms | A complete release and confidentiality clause | The final payment schedule | A binding authority range | The briefing expressly says all listed terms and the authority range remain unapproved.''',
    vocabulary='''advocacy | Reasoned presentation of a position for a client or cause. | present measured advocacy
settlement | An agreement resolving specified claims or disputes. | negotiate settlement terms
settlement authority | Permission to negotiate or agree within specified limits. | confirm settlement authority
offer | A proposal whose legal effect depends on its terms and context. | clarify the offer terms
counteroffer | A response proposing different terms from an earlier offer. | prepare an authorized counteroffer
term sheet | A summary of proposed or agreed principal terms, with effect depending on context. | review the term sheet's status
release | Wording relinquishing specified claims or rights under agreed terms. | define the release scope
mutual release | Releases given by more than one party as specified. | negotiate a mutual release
confidentiality clause | Terms restricting specified use or disclosure of information. | review confidentiality exceptions
non-disparagement | Restrictions on specified adverse statements about a party. | distinguish non-disparagement from confidentiality
no admission | Wording addressing whether agreement acknowledges liability or wrongdoing. | review the no-admission clause
payment schedule | Agreed timing and structure of payments. | confirm the payment schedule
installment | One payment in a series. | specify the installment amount
default provision | Terms addressing failure to meet an agreed obligation. | assess the default provision
enforcement | Steps to secure compliance with an obligation or decision. | assess enforcement options
dismissal | Termination of claims or proceedings through the applicable process. | coordinate the dismissal documentation
with prejudice | A label generally indicating a final bar on bringing the dismissed claim again, subject to law. | review dismissal with prejudice
without prejudice | A context-dependent label concerning rights, proceedings, or negotiations. | clarify the effect of without-prejudice wording
mediation | A facilitated negotiation process using a neutral participant. | prepare for mediation
mediator | A neutral person helping parties seek a negotiated resolution. | clarify the mediator's role
caucus | A separate meeting within a mediation or negotiation process. | request an authorized caucus
impasse | A point at which negotiations are not progressing. | identify the source of an impasse
reservation price | A negotiating limit used internally under specified assumptions. | protect the approved reservation price
informed instruction | A client direction given after adequate explanation of relevant matters. | obtain an informed instruction''',
    precision='A floated payment figure is not a complete account of settlement terms. Payment timing, release scope, confidentiality, and approval authority may change the decision. Do not describe a proposal as accepted when the authorized client decision has not occurred.',
    precision_extra='Labels such as without prejudice, confidential, and no admission do not create identical protections everywhere. Their effect depends on the applicable law and context. A confidentiality proposal must not be used to assume prohibited restrictions on lawful disclosures.',
    phrases='''State the status | The other side floated a figure; written terms are not available.
Separate priorities | Payment timing and confidentiality are distinct negotiating questions.
Confirm authority | Who may authorize a counteroffer, and within what limits?
Limit the response | I can gather information, but I cannot approve the settlement.
Request the package | Please identify the release, payment, and confidentiality terms together.
Explain a tradeoff | An earlier payment may be valuable, but the linked conditions still require review.
Preserve the decision | The final instruction belongs to the authorized client decision-maker.
Close with next steps | We will present the options and seek a clear instruction before responding.
Avoid a guarantee | We can explain the proposal's implications, not promise acceptance.
Check the trigger | From which event would the thirty-day payment period run?
Clarify the release | Which claims and parties would the proposed release cover?
Separate concepts | Non-disparagement and confidentiality do not regulate exactly the same conduct.
Check exceptions | The confidentiality wording needs review for required or protected disclosures.
Report the limit | The current authority does not extend to that concession.
Identify incompleteness | Agreement on a number alone does not settle the remaining terms.
Confirm instructions | Please confirm the approved position and any conditions attached to it.''',
    notes='''Authority versus preference | A preferred outcome does not by itself authorize someone to agree to the terms needed to obtain it.
Float versus offer | Float usually describes a tentative suggestion; clarify its status rather than assuming formal legal effect.
Condition placement | Put a material condition next to the commitment it limits, not at the end of a separate email.
From versus by | A payment due within thirty days from an event differs from a payment due by a fixed date.
Could versus will | Could describes a possible outcome; will may sound like a promise and needs appropriate support.
Approval verbs | Recommend, instruct, approve, and accept identify different actors and stages in a settlement decision.''',
    d='''Which response fits Tomas's authority? | I can collect the terms for the decision-maker but cannot approve them. | I accept on behalf of every client entity. | Any figure discussed is automatically approved. | I can waive the release review to save time. | Tomas's role permits information gathering, not acceptance or waiver of the required review.
Which question makes the timing proposal more precise? | What event starts the thirty-day payment period? | Which font should the number use? | Can all other terms be ignored? | Has the payment already arrived? | Identifying the trigger turns a vague period into a term the parties can evaluate and draft accurately.
Which statement correctly separates two restrictions? | Confidentiality concerns disclosure; non-disparagement concerns specified adverse statements. | They always have identical wording and effect. | Either label automatically overrides every reporting duty. | Neither requires review of its actual wording. | The restrictions concern different conduct, and their scope and enforceability depend on wording and applicable law.
Which description fits the current proposal? | Incomplete terms awaiting review and client instruction | A fully authorized signed settlement | A final judgment requiring payment | An accepted release of every claim | A floated figure and unapproved terms do not establish a complete, authorized settlement.''',
    dialogue='''Tomas | The business contact wants payment within thirty days, and the other side floated a figure. The decision-maker also wants confidentiality, but we have no written terms yet.
Nadia | Then treat the discussion as an incomplete [[proposal::Proposal describes terms still being explored; a floated figure does not establish a complete approved settlement.]]. We need the payment trigger, release scope, and confidentiality wording before presenting the package for a decision.
Tomas | I can ask for those details. I cannot approve a settlement, although the business contact seems to expect me to tell the other side that the number works.
Nadia | Make your [[authority::Authority defines permitted actions; collecting information does not permit Tomas to accept terms for the client.]] clear. You can gather the terms for the decision-maker without accepting a figure or implying that the remaining provisions are routine.
Tomas | For timing, should I ask whether thirty days runs from agreement in principle, signature, or another event? Each version could give the business a different payment date.
Nadia | Yes. The [[payment schedule::The payment schedule specifies timing and structure, requiring a starting event as well as a duration.]] needs a defined trigger and any proposed installments. Do not turn the client's preferred period into a term the other side has already accepted.
Tomas | The business contact says a quick payment matters more than a long dispute. I can report that preference while keeping the confidentiality concern beside it for review.
Nadia | That frames the [[tradeoff::A tradeoff compares benefits and conditions, helping the client decide without choosing on the client's behalf.]] usefully. Explain the linked conditions and uncertainty, rather than presenting speed as a reason to stop reviewing the rest of the agreement.
Tomas | The suggested release sounds broad, but I have not seen the text. I will ask which claims and entities it covers instead of calling it a standard release.
Nadia | Correct. The [[release::A release relinquishes specified claims or rights; its actual scope cannot be inferred from a reassuring label.]] requires careful review. Standard is not a substitute for identifying who gives up what, under which terms, and with what approval.
Tomas | The other side also mentioned confidentiality and non-disparagement in one sentence. I should ask for separate wording because those terms do not describe exactly the same restriction.
Nadia | Yes. Review each [[clause::A clause supplies contractual wording; labels alone do not establish a restriction's reach or exceptions.]] and its exceptions. We must not assume a proposed restriction can prevent required or protected disclosures merely because the document calls itself confidential.
Tomas | If the decision-maker asks whether confidentiality is guaranteed, I will explain that you need to assess the wording and applicable limits before making any recommendation.
Nadia | Good. Our [[advice::Advice explains implications and limits for the client's decision; it cannot promise an unassessed confidentiality result.]] should support an informed choice. Reassurance must not become a promise about legal effect, enforceability, or the other side's future behavior.
Tomas | Suppose the decision-maker authorizes a response with an earlier payment date but a narrower release. I would need the exact approved position before transmitting it.
Nadia | Exactly. Record the [[counteroffer::A counteroffer proposes changed terms; transmitting it requires clear authority for those terms and conditions.]] and any conditions attached to that authority. Do not combine separate suggestions into a new package the client never instructed us to propose.
Tomas | If negotiations stall, I can report which terms remain unresolved instead of saying the whole discussion failed. That should help the decision-maker identify the actual disagreement.
Nadia | Describe the [[impasse::An impasse is stalled negotiation; identifying disputed terms is more precise than declaring every issue irretrievably failed.]] precisely. Payment timing might be workable while release or confidentiality remains open, and the next instruction should reflect those distinctions.
Tomas | I will collect the written terms, identify the competing priorities, and prepare the options for review. No acceptance message will go out based on this conversation.
Nadia | Then we can seek an [[informed instruction::An informed instruction follows adequate explanation, preserving the authorized client's decision rather than presuming it.]]. Keep the proposal, recommendation, and client decision separate so everyone understands the next step and who may take it.''',
    transfer_title='A mediator asks whether the figure is accepted',
    transfer_setup='A representative may relay information in a mediation but has no authority to accept an amount. A mediator asks for confirmation while release wording and payment timing remain unresolved.',
    transfer='''Representative: "I can relay the figure, but acceptance is outside my ___." | authority | The representative's permitted role is communication, not a decision to settle.
Counsel: "The release and payment terms remain ___." | unresolved | The facts leave both terms open, so the figure cannot be described as the complete approved package.
Representative: "We will seek the decision-maker's ___ after explaining those terms." | instruction | The authorized client must give a direction informed by the unresolved conditions, not merely the amount.
Counsel: "Until then, describe the figure as a ___ rather than an accepted agreement." | proposal | Proposal preserves the tentative status and avoids falsely representing that settlement approval has occurred.'''))
