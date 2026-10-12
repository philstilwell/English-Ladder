"""Original international-law communication: parties, forums, treaties, and coordinated advice."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='international-law', title='International Law English',
    balanced_answer_columns=True,
    category='Business & professional services', cover_label='ENGLISH FOR INTERNATIONAL LEGAL PRACTICE',
    cover_title='International Law', cover_size=30,
    tagline='Identify the jurisdiction. Preserve the distinction.',
    audience='For lawyers, international legal advisers, and legal professionals coordinating matters across jurisdictions.',
    roles='international lawyers, cross-border counsel, treaty advisers, international disputes teams',
    summary='International legal English for cross-border intake, governing-law clauses, service abroad, arbitration, enforcement, treaty interpretation, evidence coordination, and settlement discussions.',
    map_intro='Eight matters distinguish the client and mandate, governing law and forum, service and receipt, arbitral seat and hearing venue, awards and enforcement, treaty text and applicability, access and lawful production, and proposals and binding settlements.',
    notes_title='International is a context, not a universal rulebook.',
    notes_intro='Cross-border work requires lawyers to explain which law, institution, entity, and procedure they mean. Clear English keeps a provisional view separate from local advice and preserves uncertainty when documents travel between languages and legal systems.',
    field_notes=[
        ('Name the legal person', 'A group name, brand, parent company, and contracting affiliate may not identify the same legal person. Clarify the client and relevant parties before discussing the substance.', '"Which entity signed, and which entity is asking us to act?"'),
        ('Separate the legal questions', 'Governing law, jurisdiction, venue, arbitral seat, and enforcement concern different questions. A convenient location does not answer all of them.', '"That clause identifies substantive law; the forum clause needs separate review."'),
        ('Keep local advice attributable', 'A coordinating lawyer should identify which jurisdictional issue requires local counsel, what information the opinion assumes, and what remains open.', '"Local counsel has confirmed that point for the stated facts, not for every affiliate."'),
        ('Make the status explicit', 'Received, served, filed, recognized, enforced, proposed, and agreed are not interchangeable. Shortened progress reports can create false legal certainty.', '"The application was filed; the court has not determined it."'),
    ], scope_note=FICTION + 'This is professional English practice, not legal advice, a filing guide, or authority to practice law. Legal meanings, deadlines, privilege, service, privacy, sanctions, and enforceability depend on the actual jurisdiction, instrument, facts, and current law. Use qualified counsel and verified current primary materials for real matters. No exercise establishes a filing deadline, service method, court jurisdiction, treaty obligation, or binding settlement. Protect real client information.',
    sources=[
        source('HCCH. Service Section.', 'https://www.hcch.net/en/instruments/conventions/specialised-sections/service', 'Background on the Service Convention, channels of transmission, status information, and country-specific practical requirements.'),
        source('ICC. 2021 Arbitration Rules.', 'https://iccwbo.org/dispute-resolution/dispute-resolution-services/arbitration/rules-procedure/2021-arbitration-rules/', 'Terminology for arbitration agreements, place, procedure, and language. Actual matters require the applicable version of the rules and law.'),
        source('UNCITRAL. New York Convention.', 'https://uncitral.un.org/en/texts/arbitration/conventions/foreign_arbitral_awards', 'Background for distinguishing an arbitral award from court recognition and enforcement under the relevant framework.'),
        source('United Nations. Vienna Convention on the Law of Treaties.', 'https://legal.un.org/ilc/texts/instruments/english/conventions/1_1_1969.pdf', 'Primary terminology for treaty participation, entry into force, reservations, and interpretation. Fictional provisions are not quotations from the Convention.')], units=[])

BOOK['units'].append(unit(
    title='Defining the client and the cross-border mandate', scene='The parent is not the signatory',
    skill='Clarify legal entities, instructions, and jurisdictional scope before summarizing a cross-border matter.',
    brief='Orion Group contacts coordinating lawyer Leila about a supply dispute. The contract names Orion Components Ltd as signatory, while the email comes from the parent company, Orion Holdings. Contact Theo has not yet confirmed which entity will be the client or who can authorize the engagement. Documents mention operations in two jurisdictions. No representation, conflict clearance, or merits opinion has been established.',
    cast='Theo | Group legal contact\nLeila | Coordinating lawyer',
    culture=('A familiar group name is not enough', 'Corporate shorthand can conceal important distinctions. Clarify the legal entity and authority without implying that the contact has acted improperly.'),
    a='''Which entity is named in the contract? | Orion Components Ltd | Orion Holdings | Orion Group as an identified legal person | Leila's firm | The contract names Orion Components Ltd, while the email comes from the parent.
Which point remains unresolved? | The client entity and engagement authority | The existence of a supply dispute | The parent's email involvement | The subsidiary's contract name | The brief explicitly leaves client identity and authorization for the engagement unconfirmed.
What would overstate the present status? | Our firm has accepted representation | Two jurisdictions are mentioned | Theo is the contact | A contract has been supplied | No accepted representation or conflict clearance is established in the case.''',
    vocabulary='''legal entity | Organization or person recognized as having a distinct legal identity. | identify the legal entity
parent company | Company controlling another company under the relevant relationship. | distinguish the parent company
subsidiary | Company controlled by another company. | identify the contracting subsidiary
affiliate | Entity connected through the relevant ownership or control relationship. | clarify the affiliate relationship
contracting party | Person or entity that is a party to the contract. | identify the contracting party
signatory | Person or entity identified as signing a document in the relevant capacity. | verify the signatory
client identity | Identification of the person or entity for whom counsel acts. | confirm client identity
engagement letter | Document defining the agreed professional engagement. | settle the engagement letter
scope of engagement | Boundaries of the work counsel is engaged to perform. | define the scope of engagement
conflicts check | Review for relevant conflicts before or during representation. | complete a conflicts check
authority to instruct | Power to give instructions for the relevant client or matter. | verify authority to instruct
local counsel | Lawyer advising on the relevant local jurisdiction. | instruct local counsel
coordinating counsel | Lawyer organizing advice or work across the matter. | identify coordinating counsel
jurisdictional nexus | Connection linking a matter to a particular legal jurisdiction. | identify a jurisdictional nexus
private international law | Rules addressing cross-border private-law questions, including applicable law and jurisdiction. | distinguish private international law
public international law | Law concerning states and other subjects of the international legal order. | distinguish public international law
corporate capacity | Legal ability of an entity to act in the relevant context. | verify corporate capacity
instruction record | Traceable account of instructions received and their source. | maintain an instruction record''',
    precision='The parent\'s email does not establish that the parent signed the contract or is the client. Cross-border facts also do not automatically make the dispute one between states.',
    precision_extra='Clarifying intake information is not accepting representation or giving a merits opinion. Actual engagement, conflict, and local-practice requirements must be satisfied.',
    phrases='''Identify the party | Which legal entity signed this agreement?
Clarify the client | Is the proposed client the parent or the contracting subsidiary?
Check authority | Who is authorized to give instructions for that entity?
Limit the mandate | We need to define which jurisdictions and questions the engagement covers.
Coordinate advice | That local-law point needs the appropriate local counsel.
Avoid premature acceptance | We have not yet confirmed the engagement or completed the required checks.
Separate legal fields | A private cross-border contract dispute is not automatically a dispute between states.
Summarize intake | The signatory is identified; client identity and authority remain to be confirmed.''',
    notes='''Act for versus coordinate with | Act for identifies representation; coordinate with can describe communication without creating that relationship.
Group versus entity | Group is often commercial shorthand and may not identify the exact legal person involved.
Subject to | Subject to preserves an unresolved condition such as conflict clearance; omitting it may overstate acceptance.''',
    d='''Which intake question resolves the key distinction? | Which entity is asking us to act, and which signed? | Can the group brand replace every entity name? | Shall we assume the parent is liable? | Have we already won in both jurisdictions? | The question separates client identity from the contracting party without assuming representation or liability.
Which summary is supported? | The subsidiary signed; the proposed client remains unconfirmed | The parent signed and retained us | Every affiliate is already our client | The matter is necessarily a state dispute | The supplied contract and unresolved engagement facts support only the qualified summary.
What should be attributed to local counsel? | Advice on the specified local-law question | Every commercial preference of the group | A universal rule for all countries | Automatic authority to act for all affiliates | Local counsel's advice should remain tied to its jurisdiction, facts, and question.
Which phrase preserves an unresolved condition? | Subject to completion of the required checks | Unconditionally accepted | Representation is already confirmed | No further authority is needed | Subject to makes the condition visible rather than presenting the engagement as complete.''',
    dialogue='''Theo | Orion Group would like your firm to handle the supply dispute. The contract and the parent's email are attached.
Leila | Before discussing the merits, which [[legal entity::A legal entity has a distinct identity, so a group name cannot automatically identify the contracting party or proposed client.]] is asking us to act, and which entity signed the contract?
Theo | The contract names Orion Components Ltd, but I work with Orion Holdings and used the parent company's email.
Leila | Then the [[contracting party::The contracting party named in the supplied agreement is the subsidiary, which must not be silently replaced with the parent company.]] and the email sender are different. We should keep that distinction in the intake record.
Theo | I assumed that using the group name would cover the parent and every affiliate without more detail.
Leila | We need to confirm [[client identity::Client identity identifies whom counsel would represent and is not settled merely by a contact using a corporate group name.]] rather than assume that every connected company would be represented under one engagement.
Theo | I can ask who will authorize the work. My role is to gather the documents, not necessarily to retain counsel.
Leila | That clarifies [[authority to instruct::Authority to instruct concerns who can give instructions for the actual client and must be verified rather than inferred from document coordination.]]. Please identify the authorized person without treating your coordination role as broader permission.
Theo | The documents mention operations in two jurisdictions. Does that mean you will advise on every local issue directly?
Leila | Not necessarily. The [[scope of engagement::Scope of engagement defines the work and jurisdictional questions accepted, rather than assuming unlimited advice across every country mentioned.]] should identify the questions we handle and where appropriately qualified local advice is needed.
Theo | We would value one person coordinating the advice so that separate answers do not contradict each other without explanation.
Leila | We can discuss a [[coordinating counsel::Coordinating counsel organizes the matter across advisers while preserving the source and limits of each jurisdiction-specific opinion.]] role while keeping each local opinion attributable to the relevant lawyer and stated assumptions.
Theo | Should I tell management that your firm has accepted the matter now that we have sent the documents?
Leila | Not yet. We need the actual engagement process and a [[conflicts check::A conflicts check is part of the relevant representation process and cannot be assumed complete because documents have been sent.]], along with the other required information, before confirming representation.
Theo | I will describe this as an intake discussion, not an accepted engagement or a favorable view on the claim.
Leila | Good. The [[engagement letter::The engagement letter records the agreed professional engagement and should identify the client and scope once the required process is completed.]] should eventually reflect the confirmed client and scope rather than leaving those points implied.
Theo | One executive called this public international law because the companies operate in different countries. Is that a useful description?
Leila | Not automatically. [[Private international law::Private international law addresses cross-border private-law questions, so a contract dispute is not automatically a dispute between states.]] questions can arise in a private contract dispute; the international element alone does not make it a state dispute.
Theo | I will return with the exact entity details, the authorized contact, and the questions we need answered in each jurisdiction.
Leila | That will give us an accurate [[instruction record::An instruction record preserves who supplied the information and instructions, helping prevent assumptions about authority or representation from becoming facts.]] and a sound basis for deciding the engagement, without assuming liability or offering a merits opinion prematurely.''',
    rehearsal=['Read the corrected intake and distinguish the group, parent, subsidiary, signatory, and proposed client.', 'Swap roles and give the final intake summary without claiming that representation has been accepted.'],
    transfer_title='A new affiliate joins the email chain', transfer_setup='After intake, another affiliate joins the email chain and asks for advice. The engagement for that affiliate has not been confirmed, and no conflicts outcome is supplied.',
    transfer='''Contact: "A different ___ has joined the discussion." | affiliate | The new sender is another connected entity, not automatically the same client.
Lawyer: "Its representation is not yet ___." | confirmed | Being copied on an email does not establish an accepted engagement.
Contact: "We need to identify its authority to ___." | instruct | The relevant person's power to instruct for that entity needs clarification.
Lawyer: "The required checks remain ___." | outstanding | The scenario supplies no completed checks for the newly involved affiliate.'''))

BOOK['units'].append(unit(
    title='Separating governing law from the dispute forum', scene='The clause answers two different questions',
    skill='Explain contract provisions without collapsing substantive law, court jurisdiction, and hearing location.',
    brief='A fictional supply contract says its substantive law is the law of Jurisdiction A and names courts in Jurisdiction B in a separate dispute clause. Counsel Mina and commercial manager Owen review the wording. Whether the clauses are effective, exclusive, or subject to mandatory rules has not been assessed. Owen assumes the named courts necessarily apply only their own substantive law.',
    cast='Owen | Commercial manager\nMina | Counsel',
    culture=('Separate before simplifying', 'A short explanation can remain accurate if it identifies the distinct question each clause addresses. Avoid replacing several legal concepts with the convenient word location.'),
    a='''Which substantive law does the fictional wording select? | Law of Jurisdiction A | Law of Jurisdiction B automatically | Any law chosen later by a witness | No identified law | The contract expressly identifies Jurisdiction A in its substantive-law wording.
Which courts does the separate clause name? | Courts in Jurisdiction B | Courts in Jurisdiction A only | Every court worldwide | No court | The dispute clause separately names courts in Jurisdiction B.
What remains unassessed? | Effectiveness and scope of the clauses | The wording's two named jurisdictions | Owen's assumption | The existence of separate clauses | The brief leaves effectiveness, exclusivity, and mandatory-rule issues for legal review.''',
    vocabulary='''governing law | Law identified as governing a legal relationship or question. | identify the governing law
substantive law | Law determining rights and obligations rather than only procedure. | distinguish substantive law
procedural law | Rules governing the conduct of legal proceedings. | distinguish procedural law
choice-of-law clause | Contract wording selecting law for specified matters. | review a choice-of-law clause
forum-selection clause | Wording identifying a forum for disputes. | interpret a forum-selection clause
jurisdiction | Legal authority of a court or tribunal over the relevant matter or parties. | assess jurisdiction
venue | Place where proceedings are conducted under the relevant framework. | distinguish venue
exclusive jurisdiction clause | Clause purporting to designate a forum to the exclusion of alternatives. | assess an exclusive jurisdiction clause
non-exclusive jurisdiction clause | Clause identifying a forum without necessarily excluding others. | interpret a non-exclusive jurisdiction clause
mandatory rule | Rule that may apply despite party agreement under the relevant legal framework. | identify a mandatory rule
conflict-of-laws analysis | Assessment of which law or forum rules apply to a cross-border issue. | undertake conflict-of-laws analysis
forum non conveniens | Doctrine allowing a court in applicable systems to decline a forum on specified grounds. | assess forum non conveniens locally
choice of court | Selection of a court or courts for a dispute. | clarify choice of court
dispute-resolution clause | Contract provision addressing how disputes are to be handled. | review the dispute-resolution clause
severability | Treatment of whether one invalid provision affects others under the applicable framework. | consider severability under the actual law
enforceability opinion | Legal assessment of whether specified rights or provisions can be enforced. | qualify an enforceability opinion
contract interpretation | Determination of contractual meaning under the relevant law and context. | explain contract interpretation
local-law qualification | Limitation or condition arising from the relevant local-law analysis. | preserve a local-law qualification''',
    precision='Selecting a court and selecting substantive law address different questions. The fictional wording can be described without concluding that either clause is effective or universally enforceable.',
    precision_extra='Do not infer exclusivity, a procedural deadline, or the effect of mandatory rules from this exercise. Those issues need the actual clause, facts, and qualified jurisdiction-specific review.',
    phrases='''Separate the clauses | This provision selects law; that provision identifies a forum.
State the wording | The contract names A for substantive law and B for courts.
Avoid automatic inference | The court's location does not by itself settle every applicable-law question.
Clarify scope | Which disputes and parties does the clause actually cover?
Preserve review | We have described the wording, not yet given an enforceability opinion.
Check exclusivity | We should not assume exclusive unless the actual wording and law support it.
Flag qualification | That conclusion remains subject to the relevant local-law analysis.
Summarize plainly | Where a dispute is heard and which substantive law applies are distinct questions.''',
    notes='''Names versus establishes | A clause names a forum; whether jurisdiction is legally established requires the relevant analysis.
Applies to | Applies to should identify the issue or category governed, not imply that one clause answers every procedural question.
Subject to review | This preserves the difference between reading the contract and completing the legal opinion.''',
    d='''Which summary accurately separates the clauses? | A is named for substantive law; B is named for courts | B automatically replaces A in every respect | A's courts are necessarily the only forum | The clauses have no possible separate functions | The summary states the supplied wording without deciding its legal effectiveness.
Which question remains open? | Whether the forum clause is effective and exclusive | Whether the text names A | Whether B is mentioned | Whether Owen asked for clarification | Effectiveness and exclusivity require review beyond identifying the named jurisdictions.
What does a local-law qualification do? | Limits the conclusion to the actual analysis and conditions | Removes the need for local advice | Guarantees enforcement everywhere | Replaces the contract wording | A qualification preserves the assumptions and limits of the opinion rather than creating universal certainty.
Which phrase most clearly avoids an overstatement? | The clause names these courts; its effect needs review | These courts are unquestionably exclusive | Every jurisdiction must enforce it | The choice eliminates all mandatory rules | Naming the courts reports the text while leaving the unresolved legal effect explicit.''',
    dialogue='''Owen | The contract names courts in B, so I assumed the law of B governs every question under the agreement.
Mina | Let us separate the [[choice-of-law clause::The choice-of-law clause selects law for specified questions, which is distinct from the contract's separate selection of courts.]] from the provision about courts before drawing that conclusion from the location alone.
Owen | The first provision says the agreement uses the substantive law of A. The next one names courts in B.
Mina | Then [[substantive law::Substantive law concerns rights and obligations, and the supplied contract wording identifies A for that question.]] and the named forum are identified separately in this wording. That is the distinction we need to preserve.
Owen | Does a court's location tell us nothing useful, or does it answer a different part of the legal question?
Mina | It matters, but [[procedural law::Procedural law concerns how proceedings are conducted and must not be treated as identical to the substantive-law choice.]] and other forum issues need their own analysis. One label should not stand in for every issue.
Owen | I also called the courts exclusive in my summary, although I did not check whether the clause used that word.
Mina | We should review the [[forum-selection clause::The forum-selection clause identifies the dispute forum, but its wording and applicable law must be examined before assuming exclusivity.]] before describing its scope or exclusivity. Your summary currently adds a conclusion we have not assessed.
Owen | Could a rule still matter even if the parties chose a different law in their agreement?
Mina | A [[mandatory rule::A mandatory rule may apply despite party agreement under the relevant legal framework, so its effect requires jurisdiction-specific review.]] can require separate attention under the relevant framework. We need local analysis rather than a universal answer from this clause alone.
Owen | Then choosing a court is not quite the same as confirming that the court has authority over every possible dispute.
Mina | Correct. [[Jurisdiction::Jurisdiction concerns the court's legal authority over the relevant matter or parties and is not conclusively established merely by a manager's reading of a clause.]] needs to be assessed for the actual parties and issue, not assumed from an abbreviated contract summary.
Owen | I used venue as another word for governing law in the internal slide. That now seems likely to confuse people.
Mina | [[Venue::Venue concerns the place of proceedings under the relevant framework and should not be used as a synonym for governing substantive law.]] concerns the place of proceedings in the relevant framework. It is not a substitute term for substantive law.
Owen | Could I tell management we have read the wording but have not completed the legal opinion about its effect?
Mina | Yes. An [[enforceability opinion::An enforceability opinion assesses legal effect under the relevant conditions and is different from simply identifying what the contract says.]] is more than identifying the two jurisdictions named in the document.
Owen | We should also carry any assumptions from local counsel into the summary instead of removing them to make the slide shorter.
Mina | Exactly. A [[local-law qualification::A local-law qualification preserves the conditions or limits of the jurisdiction-specific advice and should not be deleted during summarization.]] may be essential to the meaning of the advice, not optional wording around the main answer.
Owen | My corrected explanation is that A is named for substantive law, B for courts, and scope and effect remain under review.
Mina | That preserves the [[contract interpretation::Contract interpretation determines meaning in context under the relevant law, so a careful summary must distinguish the text from unresolved legal conclusions.]] questions without promising a result or treating one location as the answer to everything.''',
    rehearsal=['Read the corrected exchange and separate substantive law, procedure, jurisdiction, and venue.', 'Swap roles and summarize the two fictional clauses while keeping effectiveness and exclusivity unresolved.'],
    transfer_title='Exclusive was added in the summary', transfer_setup='The original clause names a forum, but its exclusivity has not been assessed. An internal summary calls the forum exclusive. Counsel requests correction pending review.',
    transfer='''Counsel: "The clause names a ___." | forum | The wording identifies a forum, which is the only stated textual fact.
Manager: "My summary added the word ___." | exclusive | Exclusive was introduced in the summary without the required assessment.
Counsel: "That conclusion remains under ___." | review | The legal effect and exclusivity have not yet been determined.
Manager: "I will correct the unsupported ___." | characterization | The added characterization must be removed or accurately qualified rather than repeated as settled.'''))

BOOK['units'].append(unit(
    title='Coordinating service abroad and deadline questions', scene='Delivered is not necessarily served',
    skill='Distinguish physical receipt, a service method, and verified legal effect in a cross-border procedural update.',
    brief='Coordinator Ben sends counsel Asha a courier receipt showing delivery of documents to an overseas company\'s office. No assessment of valid service, applicable treaty channels, translation requirements, recipient authority, or response deadline has been completed. Ben has described the defendant as served. Asha requests jurisdiction-specific verification and keeps any actual urgent deadline issue with qualified counsel.',
    cast='Ben | Matter coordinator\nAsha | Counsel',
    culture=('Operational proof and legal effect differ', 'A courier can confirm a delivery event without answering whether service was valid under the applicable law. Report each state precisely and escalate real time limits promptly.'),
    a='''What does the supplied receipt confirm? | A courier delivery event | Valid service under every applicable rule | An established response deadline | The recipient's legal authority | The receipt concerns physical delivery, while the relevant legal effect has not been assessed.
Which summary currently overstates the facts? | The defendant has been served | Documents reached an office | A receipt exists | Counsel needs to review the route | Served implies a legal conclusion that the delivery receipt alone does not establish.
What must be verified before giving a deadline answer? | The applicable rules and actual triggering facts | A guessed standard period | The courier's advertising promise | The coordinator's preferred date | Legal deadlines depend on the actual governing process and verified facts, not a universal guessed interval.''',
    vocabulary='''service of process | Formal delivery or notification of legal documents under the applicable rules. | verify service of process
transmission channel | Route used to send documents under the relevant procedure. | identify a transmission channel
Central Authority | Designated authority with functions under the relevant convention. | verify the designated Central Authority
Convention Contracting Party | State or other eligible party bound in the relevant convention context. | check Convention Contracting Party status
service request | Request seeking service through the relevant procedure. | prepare a service request
certificate of service | Document recording service-related facts under the applicable process. | review a certificate of service
courier receipt | Record of delivery by a courier. | distinguish a courier receipt
authorized recipient | Person permitted to receive documents in the relevant legal capacity. | verify the authorized recipient
translation requirement | Rule requiring documents in a specified language or form. | confirm a translation requirement
certified translation | Translation accompanied by the certification required in the relevant context. | obtain the required certified translation
declaration or objection | State position affecting operation of a convention provision under the relevant framework. | check current declarations or objections
country profile | Official country-specific procedural information. | consult the current country profile
response deadline | Latest time for a required response under the actual rules. | verify the response deadline
triggering event | Event that starts a legal period or obligation under the relevant rule. | establish the triggering event
procedural calendar | Record of verified procedural dates and obligations. | maintain the procedural calendar
proof of transmission | Evidence that documents were sent through a stated route. | retain proof of transmission
defective service | Service that fails to satisfy applicable requirements. | assess alleged defective service
local procedural advice | Jurisdiction-specific advice on process and formalities. | obtain local procedural advice''',
    precision='Delivery, transmission, and valid service are different claims. The receipt cannot establish a universal deadline or show that treaty and local requirements were met.',
    precision_extra='Do not treat the lack of a verified deadline as permission to wait. Real procedural risk must be addressed promptly by qualified counsel using the actual facts and rules.',
    phrases='''Report the event | The courier confirms delivery to the office.
Avoid the legal leap | That receipt alone does not establish valid service.
Check the route | Which transmission channel is applicable to these documents and countries?
Verify the recipient | We need to confirm who received them and in what capacity.
Check current requirements | Let us verify the relevant country information and translation requirements.
Preserve timing uncertainty | The triggering event and response period still need legal verification.
Escalate promptly | The deadline question needs immediate attention from the responsible counsel.
Correct the status | I will replace served with the narrower delivery status until the legal review is complete.''',
    notes='''Delivered versus served | Delivered reports physical receipt; served asserts a procedural status under applicable legal requirements.
From versus by | From can identify the start of a period; by identifies a latest time. Neither supplies the governing legal rule.
Confirmed by whom | The source matters: a courier confirms delivery, while legal effect requires the appropriate assessment.''',
    d='''Which update preserves the receipt's evidential scope? | Courier delivery confirmed; service validity under review | Valid service and deadline confirmed | Every treaty requirement satisfied | The company admitted the claim | The receipt confirms delivery only, so the wider procedural conclusions remain unresolved.
What should the coordinator not calculate by guesswork? | The legal response deadline | The number of attached documents | The courier reference as printed | The date shown on the receipt | A response deadline depends on applicable law and triggering facts, not an assumed standard period.
Which source is appropriate for country-specific requirements? | Current official information and qualified local procedural advice | A forum anecdote about another country | The courier's general delivery policy alone | An old unrelated contract template | The actual route needs current official and qualified jurisdiction-specific verification.
Which action addresses real timing risk? | Escalate promptly to responsible counsel while facts are checked | Wait indefinitely because validity is uncertain | Assume the longest period found online | Tell the client no deadline can exist | Uncertainty requires prompt qualified attention rather than a guessed deadline or permission to delay.''',
    dialogue='''Ben | The courier receipt shows delivery to the overseas office, so I marked the defendant as served in our status report.
Asha | Please separate the [[courier receipt::A courier receipt records a physical delivery event and does not alone establish valid service under the applicable legal requirements.]] from the legal conclusion. We have not yet verified whether that delivery constitutes valid service.
Ben | I thought the signature on the receipt answered the question, but it only identifies someone who accepted the package.
Asha | We need to verify the [[authorized recipient::An authorized recipient must have the relevant legal capacity to receive the documents; a signature on delivery does not by itself establish that capacity.]] and the applicable procedure, rather than assume that any office signature has the same legal effect.
Ben | The matter crosses two countries. Should I simply choose the route the courier normally uses for international deliveries?
Asha | No. The [[transmission channel::A transmission channel is the route applicable under the relevant legal process and cannot be selected solely from ordinary courier logistics.]] needs to be checked against the actual legal framework, documents, countries, and relevant requirements.
Ben | The team mentioned a Hague Convention route but did not identify the countries' current positions or the authority involved.
Asha | Then verify the relevant [[Central Authority::A Central Authority is designated under the relevant convention, and the correct authority and its role must be checked for the actual matter.]] where that channel applies, together with the current official country information and qualified advice.
Ben | I can gather the exact documents and the delivery record without claiming that the formal process is complete.
Asha | Please also check any [[translation requirement::A translation requirement depends on the actual procedure and jurisdiction and must not be assumed satisfied because documents were physically delivered.]] through the proper review. Sending an English copy does not settle that question by itself.
Ben | Management is asking when the company must respond. I was about to use the standard period from another matter.
Asha | Do not guess the [[response deadline::A response deadline depends on the applicable rules and verified triggering facts, not the period used in an unrelated matter.]]. This needs prompt attention from the responsible counsel using the actual rules and facts.
Ben | We also need to know which event starts any relevant period, rather than assuming the courier timestamp controls.
Asha | Exactly. The [[triggering event::A triggering event starts a legal period under the actual rule, and it cannot be assumed from an unreviewed delivery timestamp.]] must be established under the applicable process. Uncertainty is not permission to leave the question unattended.
Ben | Would an official document confirming service answer a different question from our delivery receipt?
Asha | A [[certificate of service::A certificate of service records relevant service facts under its actual process, which must be reviewed rather than equated automatically with a courier receipt.]] has to be reviewed in its actual procedural context; we should not treat different documents as interchangeable proof.
Ben | I will correct the status to delivery confirmed, with legal service validity and timing still being checked.
Asha | Good. Keep the [[procedural calendar::The procedural calendar should distinguish verified obligations from unresolved timing questions and identify the responsible counsel for urgent verification.]] accurate, and make the outstanding deadline question visible to the lawyer responsible for it.
Ben | I will send the facts and unanswered questions today, with no invented deadline or claim that the defendant admitted anything.
Asha | That gives [[local procedural advice::Local procedural advice addresses the jurisdiction-specific requirements and needs accurate facts rather than assumptions already presented as legal conclusions.]] a reliable starting point and prevents an operational update from becoming an unsupported legal conclusion.''',
    rehearsal=['Read the corrected update and distinguish sent, delivered, received, and validly served.', 'Swap roles and route the deadline question promptly without calculating an unsupplied legal period.'],
    transfer_title='Sent is not yet received', transfer_setup='A service request is dispatched through a route selected after legal review. Receipt by the relevant authority has not been confirmed. No service certificate or response deadline is supplied.',
    transfer='''Coordinator: "The request has been ___." | dispatched | Dispatch describes the sender's completed action, not confirmed receipt or completed service.
Counsel: "Authority receipt remains ___." | unconfirmed | The brief explicitly leaves receipt by the relevant authority unconfirmed.
Coordinator: "No service certificate is ___." | available | The case supplies no certificate establishing service-related facts for review.
Counsel: "We must preserve the actual procedural ___." | status | The update should distinguish dispatch, receipt, and service rather than collapse them.'''))

BOOK['units'].append(unit(
    title='Explaining an arbitral seat and hearing arrangements', scene='A remote hearing does not answer the seat question',
    skill='Distinguish the legal seat, hearing venue, procedural rules, and language in an arbitration planning discussion.',
    brief='A fictional arbitration clause identifies City A as the seat and a named institution\'s rules. The parties are considering a remote hearing with some participants joining from City B. Counsel Farah and client representative Emil review logistics. The language of proceedings and any change to the legal seat have not been agreed. No real institutional rule, legal deadline, or court power is determined by this exercise.',
    cast='Emil | Client representative\nFarah | Arbitration counsel',
    culture=('Legal choices and travel choices are separate', 'An efficient meeting plan should not silently change the legal basis of a proceeding. Use the same words consistently in schedules, emails, and instructions.'),
    a='''Which seat does the fictional clause identify? | City A | City B automatically | Every participant's location | No seat at all | The clause expressly identifies City A as the legal seat.
What is being considered for the hearing? | Remote participation with some people in City B | An agreed change of seat to City B | A completed award | A final enforcement order | Only hearing logistics are under discussion; no seat change is agreed.
Which issue remains unresolved? | The language of proceedings | The clause's stated seat | The existence of institutional rules | The possibility of remote participation | The case explicitly says that the language has not yet been agreed.''',
    vocabulary='''arbitration agreement | Agreement to resolve defined disputes through arbitration. | examine the arbitration agreement
arbitral seat | Legal place of arbitration with significance under the applicable framework. | identify the arbitral seat
hearing venue | Physical or arranged location for a hearing. | distinguish the hearing venue
arbitral tribunal | Arbitrator or panel deciding the dispute under the relevant authority. | address the arbitral tribunal
arbitral institution | Organization administering arbitration under its applicable framework. | identify the arbitral institution
institutional rules | Procedural rules associated with the administering institution. | verify the institutional rules
ad hoc arbitration | Arbitration not administered by an institution in the same way as institutional proceedings. | distinguish ad hoc arbitration
procedural order | Tribunal direction organizing aspects of the proceeding. | review a procedural order
terms of reference | Document defining aspects of an arbitration where required by the applicable process. | clarify the terms of reference
language of proceedings | Language or languages used under the agreed or determined procedure. | confirm the language of proceedings
remote hearing | Hearing with participants joining through remote communication technology. | organize a remote hearing
hearing protocol | Agreed or directed arrangements for conducting a hearing. | confirm the hearing protocol
tribunal constitution | Process of establishing the arbitral tribunal. | track tribunal constitution
arbitrator appointment | Selection or designation of an arbitrator under the relevant process. | confirm an arbitrator appointment
challenge to an arbitrator | Objection to an arbitrator under the applicable standards and process. | distinguish an arbitrator challenge
procedural timetable | Schedule governing steps in the proceeding. | maintain the procedural timetable
interim measure | Temporary relief or protection under the applicable authority. | discuss an interim measure
jurisdictional objection | Challenge to the authority of the tribunal or court to hear the matter. | preserve a jurisdictional objection''',
    precision='The legal seat and hearing arrangements are distinct. Remote participation from City B does not, on these facts, establish an agreed change to the stated seat in City A.',
    precision_extra='The actual agreement, applicable rules and law, tribunal directions, and party arrangements determine legal effect. Do not infer a real procedural power or deadline from this fictional planning conversation.',
    phrases='''Identify the legal choice | The clause names City A as the seat.
Separate logistics | The hearing arrangement is a different question from the legal seat.
Avoid silent change | We should not describe a seat change that nobody has agreed.
Verify the rules | Which version of the applicable rules governs this matter?
Clarify language | The language of proceedings still needs confirmation.
Plan participation | The protocol should address who joins, from where, and under what arrangements.
Preserve authority | That request needs the appropriate tribunal or procedural decision.
Summarize status | The seat is stated; hearing logistics and language remain under discussion.''',
    notes='''Seat versus venue | Seat is a legal concept; venue usually describes hearing location. Keep their roles distinct in this context.
Proposed versus directed | Proposed identifies a request; directed identifies a procedural instruction by the relevant authority.
From City B | A participant's connection location does not by itself establish a change of legal seat.''',
    d='''Which summary matches the case? | Seat A; remote logistics involving B under discussion | Seat B automatically because a participant is there | No legal seat whenever a hearing is remote | Every participant creates a new seat | The case states the seat in A and separately discusses remote hearing arrangements.
Which question needs confirmation? | The language and hearing protocol | Whether any clause exists | Whether A is named | Whether some people may connect remotely | The unresolved procedural arrangements include language and the actual hearing protocol.
Which statement preserves the request's status? | We propose this arrangement for the appropriate decision | The tribunal has already directed it | All objections are waived | The seat change is final | A proposal must not be presented as a tribunal direction or agreed change.
What should be checked before relying on an institutional procedure? | The applicable rule version and actual directions | The institution's logo alone | Another matter's old timetable | A participant's travel preference | Procedure depends on the actual applicable framework, not branding or unrelated logistics.''',
    dialogue='''Emil | Several participants will join from City B, so I changed the planning slide to say the arbitration is seated there.
Farah | Please restore the [[arbitral seat::The arbitral seat is the legal place identified by the agreement and relevant framework, not automatically the location of remote participants.]] stated in the clause. City A remains the stated seat; our hearing discussion has not agreed a change.
Emil | I had treated seat and the location of the people speaking as two expressions for the same thing.
Farah | The [[hearing venue::The hearing venue concerns where the hearing is conducted or arranged and must be distinguished from the arbitration's legal seat.]] and the legal seat answer different questions. Logistics should not silently rewrite the legal description of the proceeding.
Emil | If the hearing is remote, we still need a clear arrangement rather than saying there is no location or procedure at all.
Farah | Yes. A [[remote hearing::A remote hearing uses communication technology for participation and does not eliminate the need for applicable procedure or a clearly identified legal seat.]] needs an appropriate protocol, while the actual agreement, rules, and directions continue to matter.
Emil | The contract names an institution, but the file contains rules from two different years. Which should the team cite?
Farah | We must verify the applicable [[institutional rules::Institutional rules must be identified in the version applicable to the matter rather than selected from whichever copy is easiest to find.]] rather than choose the newest or most convenient file without checking the governing framework.
Emil | I will flag that question. We also have not agreed which language will be used for submissions and the hearing.
Farah | Then the [[language of proceedings::The language of proceedings is an actual procedural matter requiring agreement or determination under the relevant framework, not an assumption based on participants' locations.]] should remain an open item instead of being assumed from where participants connect.
Emil | Can our scheduling email itself decide those points, or does it need to be treated as a proposal?
Farah | Treat it as a proposal for the appropriate process. A [[procedural order::A procedural order is a direction under the tribunal's authority and should not be confused with a party's scheduling suggestion.]] is different from an internal email suggesting an arrangement.
Emil | The technical team wants to know who is allowed in each remote room and how documents will be displayed.
Farah | Those belong in the [[hearing protocol::The hearing protocol sets the actual arrangements for conducting the hearing, including participation and document handling as appropriately agreed or directed.]], subject to the actual decisions and safeguards required for this proceeding.
Emil | I will not tell them that a convenient technical setting resolves every legal issue about participation.
Farah | Correct. The [[arbitral tribunal::The arbitral tribunal exercises the authority available under the relevant agreement, rules, and law, which is distinct from technical coordination of a call.]] and applicable framework determine the procedural questions within their proper scope.
Emil | We should keep a separate list of proposed dates and dates that have actually been fixed.
Farah | That will protect the [[procedural timetable::The procedural timetable records actual procedural dates and should distinguish binding or fixed steps from proposed scheduling options.]] from becoming a mixture of binding directions and unapproved planning preferences.
Emil | My revised slide will show seat A, proposed remote arrangements involving B, and language still to be confirmed.
Farah | That accurately describes the [[arbitration agreement::The arbitration agreement provides the relevant agreed framework, whose stated terms must not be altered merely by a shortened logistical summary.]] and the open planning issues without claiming that a logistical proposal has changed the legal seat.''',
    rehearsal=['Read the corrected exchange and contrast seat, venue, remote participation, and language.', 'Swap roles and report the planning status without turning a proposal into a procedural order.'],
    transfer_title='A draft timetable was circulated as final', transfer_setup='Counsel proposes a hearing date in a draft email. No tribunal direction or party agreement fixing the date is supplied. The internal calendar marks it confirmed.',
    transfer='''Counsel: "The date was only ___." | proposed | The draft email offered a date but did not establish a final arrangement.
Coordinator: "Our calendar incorrectly marked it ___." | confirmed | Confirmed overstates the status because no fixing agreement or direction is supplied.
Counsel: "The actual procedural decision remains ___." | pending | The scenario leaves the relevant agreement or direction unresolved.
Coordinator: "I will correct the timetable ___." | status | The correction must preserve the distinction between a proposal and a fixed date.'''))

BOOK['units'].append(unit(
    title='Explaining recognition, enforcement, and recovery', scene='An award is not money in the account',
    skill='Distinguish a favorable arbitral award from recognition, enforcement proceedings, and actual collection.',
    brief='A fictional company has received a favorable arbitral award. Client representative Marta asks counsel David to report the award amount as cash recovered. No voluntary payment, recognition order, enforcement step, verified asset location, or collection has occurred in the supplied case. Counsel discusses the questions requiring jurisdiction-specific review without predicting the result.',
    cast='Marta | Client representative\nDavid | Counsel',
    culture=('A legal success and a commercial result may be different stages', 'Acknowledge the award while explaining what remains. Avoid making the client feel that an important result was meaningless simply because further work is required.'),
    a='''What has actually occurred? | A favorable arbitral award was received | Cash was collected | Every court recognized the award | Assets were seized | The case supplies the award but none of the later recovery steps.
Which financial report would overstate the facts? | Cash recovered equals the award amount | An award has been received | Further legal review is needed | Payment has not yet occurred | The award amount is not cash received when no payment or collection has occurred.
Which issue needs verification? | Asset location and the relevant enforcement framework | Whether an award exists | Whether Marta asked a question | Whether payment is absent | No asset location or jurisdiction-specific enforcement position has been established.''',
    vocabulary='''arbitral award | Decision issued by an arbitral tribunal under the relevant process. | review an arbitral award
award creditor | Party entitled to relief under the award. | identify the award creditor
award debtor | Party against whom the award grants relief. | identify the award debtor
recognition | Legal acceptance of an award's status or effect under the relevant framework. | seek recognition
enforcement | Use of legal mechanisms to give effect to an obligation or decision. | pursue enforcement
execution against assets | Legal measures directed at assets under the applicable enforcement process. | assess execution against assets
voluntary compliance | Performance without compulsory enforcement measures. | request voluntary compliance
asset tracing | Investigation to identify relevant assets. | distinguish asset tracing from recovery
asset location | Jurisdiction or place in which assets are situated. | verify asset location
grounds for refusal | Recognized bases for declining relief under the applicable framework. | assess grounds for refusal
public policy exception | Rule allowing specified relief to be refused on relevant public-policy grounds. | examine the public policy exception
arbitrability | Whether a dispute can be resolved by arbitration under the applicable law. | assess arbitrability
set-aside proceeding | Proceeding seeking annulment of an award under the relevant law. | distinguish a set-aside proceeding
stay of enforcement | Suspension of enforcement under the relevant authority. | assess a stay of enforcement
sovereign immunity | Protection of a state or relevant entity from specified proceedings or measures under applicable rules. | assess sovereign immunity
certified award copy | Copy of an award meeting the applicable certification requirements. | obtain a certified award copy
enforcement forum | Court or jurisdiction in which enforcement relief is sought. | identify the enforcement forum
recovery estimate | Qualified estimate of what may actually be collected. | qualify a recovery estimate''',
    precision='The award establishes the result stated in that decision, not payment received. Recognition, enforcement, execution, and actual recovery are distinct stages and may raise different legal and practical questions.',
    precision_extra='The New York Convention is relevant to many foreign or non-domestic awards, but applicability, requirements, defenses, assets, and local procedure must be checked. No universal outcome or deadline is supplied here.',
    phrases='''Acknowledge the result | The favorable award is an important result.
Separate recovery | We have not yet received payment or collected funds.
Name the next question | We need to assess the relevant enforcement forum and assets.
Avoid a guarantee | Recognition and collection should not be presented as automatic.
Distinguish proceedings | A challenge to the award and an enforcement application are not the same proceeding.
Qualify the estimate | Any recovery estimate depends on verified legal and asset information.
Check documents | We need the copies and translations required by the actual forum.
Report accurately | The status is award received, with recovery steps still under review.''',
    notes='''Awarded versus recovered | Awarded identifies relief in the decision; recovered identifies an actual collection outcome.
May refuse | May refuse describes a legally available possibility under specified grounds, not a prediction that refusal will occur.
Available assets | Available should not be used for assets that have merely been rumored or not assessed for the actual enforcement process.''',
    d='''Which update is supported? | Award received; no payment collected | Award amount already in the bank | Enforcement guaranteed everywhere | Assets verified and seized | This update separates the supplied decision from recovery stages that have not occurred.
What does asset tracing establish when successful? | Information about relevant assets, not necessarily recovery | Automatic transfer of funds | Elimination of every defense | A universal enforcement forum | Identifying assets is distinct from obtaining and executing the legal measures needed for recovery.
Which legal questions should not be collapsed? | Set-aside and enforcement proceedings | Award and arbitral award | Payment and payment received | Client and client representative | Challenges to the award and requests to enforce it can involve different proceedings and authorities.
Which phrase preserves the uncertainty appropriately? | Recovery depends on verified legal and asset information | Recovery is guaranteed by the award alone | No local review is needed | Every named asset can immediately be seized | This statement identifies the relevant unresolved conditions rather than promising collection.''',
    dialogue='''Marta | We have a favorable award. Can I report the full amount as recovered cash in the management update?
David | The [[arbitral award::An arbitral award states the tribunal's decision, but receiving it does not mean that payment or collection has occurred.]] is an important result, but it is not the same as money received. No payment has occurred yet.
Marta | I do not want to understate the result, but I also should not make the cash position look better than it is.
David | Exactly. We can report the award and separately discuss [[voluntary compliance::Voluntary compliance means performing the obligation without compulsory enforcement, and no such payment is established in this case.]], any enforcement steps, and the actual amount collected.
Marta | The debtor has operations abroad. Does that mean we can enforce the award in any country where its name appears?
David | We need to verify the relevant [[enforcement forum::The enforcement forum is the court or jurisdiction where relief is sought, which requires analysis rather than assumption from a company's international presence.]] and legal framework rather than treating every business location as an available recovery route.
Marta | We also have a list of possible assets, but some entries are old and may belong to other group entities.
David | Then [[asset tracing::Asset tracing investigates relevant assets and ownership; a preliminary list is not proof that the award debtor owns recoverable assets.]] and ownership verification matter. A group connection does not establish that an asset belongs to this award debtor.
Marta | I keep hearing recognition and enforcement used together. Should I understand them as identical words?
David | [[Recognition::Recognition concerns legal acceptance of the award's status or effect under the applicable framework and is distinct from actual collection.]] concerns the award's legal effect under the relevant framework; enforcing and collecting involve further questions and mechanisms.
Marta | Could the other side resist the application even after the tribunal has issued its decision?
David | The applicable framework may provide [[grounds for refusal::Grounds for refusal are specified bases under the relevant framework and need actual legal assessment rather than an assumption that recognition is automatic.]]. We need to assess the actual position, not promise that every court must grant every request.
Marta | A colleague mentioned a possible challenge where the award was made. Would that be the same proceeding as our recovery application?
David | A [[set-aside proceeding::A set-aside proceeding seeks annulment under the relevant law and is not simply another name for an application to enforce the award elsewhere.]] is a different question from enforcement elsewhere, although the actual relationship between proceedings needs legal review.
Marta | Even with the appropriate court relief, obtaining money from assets could still require additional steps.
David | Yes. [[Execution against assets::Execution against assets uses the applicable legal measures to give effect to the decision and is distinct from merely identifying an asset or receiving an award.]] follows the applicable process; identifying an asset does not mean we already have a right to take it.
Marta | I will not describe a rumored asset as funds available for immediate recovery in the board paper.
David | That would overstate the [[recovery estimate::A recovery estimate must reflect verified legal and asset information and cannot equate the award amount with guaranteed cash collection.]]. Any estimate should identify the assumptions, limits, and current evidence behind it.
Marta | My update will say favorable award received, no payment yet, and jurisdiction-specific recovery work under review.
David | That accurately separates the [[award creditor::The award creditor is the party entitled to relief under the award, a status that does not itself prove money has been collected.]] status from the commercial outcome while recognizing the significance of the decision.''',
    rehearsal=['Read the corrected exchange and distinguish awarded, recognized, enforced, and recovered.', 'Swap roles and give the management update without presenting the award amount as cash received.'],
    transfer_title='An asset list is not a recovery', transfer_setup='An investigation identifies a possible asset linked to a group company. Ownership by the award debtor and the legal recovery route remain unverified. No funds have been collected.',
    transfer='''Investigator: "We identified a ___ asset." | possible | The asset is a lead, not a verified recovery source.
Counsel: "The debtor's ownership remains ___." | unverified | The group connection does not establish ownership by the relevant award debtor.
Investigator: "No funds have been ___." | collected | The investigation has not produced an actual receipt of money.
Counsel: "The legal recovery route needs ___." | assessment | The applicable enforcement process must be assessed before a recovery conclusion is made.'''))

BOOK['units'].append(unit(
    title='Reading treaty text without overstating applicability', scene='A signature does not answer every status question',
    skill='Distinguish treaty wording, participation status, temporal scope, and interpretation in a concise legal briefing.',
    brief='Adviser Lina and colleague Marcus review a fictional treaty provision and a status table. The table shows State R signed, while State S is listed as a party for which the treaty is in force. Further details about State R\'s consent, reservations, and the relevant date have not been verified. Marcus drafts a note saying the same obligations unquestionably apply to both states. They revise the briefing to identify the unresolved legal questions.',
    cast='Marcus | Legal colleague\nLina | Treaty adviser',
    culture=('Status tables are evidence, not decoration', 'A legal brief should state the relevant date and basis for participation. Do not erase distinctions among signature, consent to be bound, and entry into force to make a summary shorter.'),
    a='''What is established for State S in the fictional table? | Party status with the treaty in force | Signature only | No relationship to the treaty | A reservation identical to State R | The table explicitly identifies S as a party for which the treaty is in force.
What has not been verified for State R? | The relevant consent and applicability details | That a signature is listed | That a status table exists | That the briefing concerns a treaty | R's additional consent, reservations, and timing details remain unverified in the case.
Which briefing claim is too strong? | The same obligations unquestionably apply to both | The status entries differ | The relevant date matters | Further verification is needed | The supplied differing status entries do not support identical unquestionable obligations.''',
    vocabulary='''treaty | International agreement governed by international law in the relevant legal context. | identify the treaty instrument
signature | Formal act whose legal effect depends on the treaty and relevant circumstances. | verify the effect of signature
ratification | International act establishing consent to be bound where that procedure applies. | distinguish ratification
accession | Act by which a state establishes consent to be bound through the applicable accession process. | verify accession
consent to be bound | Legally relevant expression of agreement to treaty obligations under the applicable rules. | establish consent to be bound
entry into force | Point at which a treaty becomes operative under its terms and relevant conditions. | verify entry into force
state party | State bound in the relevant treaty relationship for which the instrument is in force. | confirm state-party status
reservation | Statement seeking to exclude or modify the legal effect of specified treaty provisions for the reserving state. | assess a reservation
interpretative declaration | Statement explaining a state's understanding of an instrument, whose legal character needs assessment. | examine an interpretative declaration
depositary | Entity entrusted with specified treaty-administration functions. | consult depositary information
authentic text | Treaty text having authoritative status under the instrument's arrangements. | identify the authentic text
ordinary meaning | Meaning of terms considered under the applicable interpretative framework. | examine ordinary meaning in context
object and purpose | Treaty aims relevant to its interpretation under the applicable framework. | address object and purpose
contextual interpretation | Reading a provision with its relevant surrounding text and legal context. | use contextual interpretation
travaux preparatoires | Preparatory work relevant under applicable interpretative rules. | assess travaux preparatoires
temporal scope | Period or events to which an instrument or obligation applies. | clarify temporal scope
territorial application | Geographical scope of an instrument's application. | verify territorial application
subsequent practice | Later conduct potentially relevant to interpretation under applicable rules. | assess subsequent practice''',
    precision='Signature, consent to be bound, and entry into force must be assessed under the actual treaty and rules. Do not assert that signature always has no binding effect or that it always establishes every obligation.',
    precision_extra='The example uses a fictional provision and status table. Actual treaty analysis requires the relevant instrument, current depositary information, applicable dates, and jurisdiction-specific legal expertise where needed.',
    phrases='''State the source | The table lists a signature for R and party status for S.
Preserve the question | We have not yet verified the effect of R's signature under this instrument.
Check timing | What is the relevant entry-into-force date for this state and issue?
Read in context | The isolated sentence needs its context and the applicable interpretative framework.
Check authoritative wording | Which language versions are authentic under the treaty?
Identify qualifications | We need to check relevant reservations and declarations.
Avoid universality | Different participation entries do not support identical obligations without further analysis.
Summarize carefully | The text is identified; applicability to R remains under review.''',
    notes='''Signed versus in force | These describe different status information; the legal effect depends on the actual treaty and circumstances.
Shall versus may | These modal verbs often signal different normative functions, but the provision still needs its full context and applicable interpretation.
As of | As of attaches a status statement to a date and prevents historical information from sounding timeless.''',
    d='''Which revised briefing best fits the evidence? | S is listed as a party; R's relevant status needs further verification | Signature always means all obligations apply | Signature can never have legal effect | Both states necessarily have identical reservations | This statement reports the table while leaving the unresolved effect of R's status open.
Why identify authentic texts? | Authoritative language versions matter to interpretation | Any online translation automatically controls | A convenient summary replaces the instrument | English always overrides every other language | The actual authentic versions must be identified instead of assuming a translation's authority.
What does as of add to a status statement? | The date to which the statement relates | A guarantee the status can never change | A new reservation | Automatic territorial application | As of makes the time reference explicit rather than presenting status as timeless.
Which interpretative shortcut should be avoided? | Reading one sentence without its context | Identifying the instrument | Checking the relevant date | Reviewing depositary information | Context and the applicable interpretative framework are needed beyond an isolated sentence.''',
    dialogue='''Marcus | The table lists both states, so I drafted that the treaty's obligations unquestionably apply to R and S in the same way.
Lina | Their entries differ. We need to separate [[signature::Signature has the legal effect provided by the actual treaty and circumstances and cannot automatically be equated with identical full obligations for every listed state.]] from the other status information before making that statement.
Marcus | R is listed as having signed, while S is listed as a party for which the treaty is already in force.
Lina | Then we must verify the relevant [[consent to be bound::Consent to be bound is the legally relevant agreement to treaty obligations under the applicable procedure, which has not been fully established for R here.]] and timing for R rather than treating two different table entries as equivalent.
Marcus | I should not replace that with the opposite claim that signatures never have any legal effect, should I?
Lina | Correct. The instrument and circumstances matter. [[Ratification::Ratification is one relevant international act expressing consent where applicable, but the actual treaty determines which procedures matter.]] may be relevant, but we should not impose one universal procedure on every treaty.
Marcus | We also need a date for the briefing, not just a statement that the instrument is in force somewhere.
Lina | Yes. [[Entry into force::Entry into force must be checked for the relevant treaty relationship and date rather than inferred from a general statement that the treaty exists.]] needs to be checked for the relevant state and question at the relevant time.
Marcus | The file contains a declaration attached to one state's entry. Can I omit it because the main text is clearer?
Lina | No. We need to assess whether a [[reservation::A reservation seeks to exclude or modify specified legal effects and must be assessed rather than omitted from an applicability analysis.]] or another relevant statement affects the analysis, including its actual legal character and effect.
Marcus | Where should I verify the status rather than rely on an undated summary copied into our internal notes?
Lina | Use the relevant [[depositary::The depositary performs specified treaty-administration functions, making its relevant status information an important source to verify.]] information and other appropriate primary materials, with the date and source clearly recorded.
Marcus | The provision is available in several languages, but the working English translation in our file is not labeled authoritative.
Lina | Then identify the [[authentic text::An authentic text has authoritative status under the treaty's arrangements and must be distinguished from a convenient working translation.]] arrangements before treating that translation as controlling wording.
Marcus | I also quoted one sentence without the preceding definition, which may have made the obligation sound broader.
Lina | That is why [[contextual interpretation::Contextual interpretation reads the provision with relevant surrounding text and the applicable legal framework rather than isolating a convenient sentence.]] matters. We should read the term within the actual instrument and applicable interpretative framework.
Marcus | Could we state the treaty's purpose without using that purpose to erase limits that appear in the actual wording?
Lina | Yes. [[Object and purpose::Object and purpose are relevant to treaty interpretation under the applicable framework but do not justify ignoring the actual text and context.]] belongs in the analysis, not as a slogan replacing the text or the status questions.
Marcus | My revised note will distinguish S's listed position from R's unresolved status and identify the date and source for each.
Lina | Good. Keep [[temporal scope::Temporal scope identifies the period or events to which the obligation applies and prevents an undated status statement from answering a time-specific question.]] explicit too, so a careful status statement does not quietly become an answer about every past or future event.''',
    rehearsal=['Read the corrected briefing and distinguish signature, consent, party status, and entry into force.', 'Swap roles and report only the two fictional table entries, retaining the unresolved applicability questions.'],
    transfer_title='An undated table was reused', transfer_setup='A colleague reuses a historical treaty-status table for a current briefing. The relevant current status and date have not been verified. No conclusion about changed status is supplied.',
    transfer='''Colleague: "The table is ___." | historical | The source describes an earlier status rather than a verified current position.
Adviser: "Current status remains ___." | unverified | The case supplies no check establishing the current relevant treaty status.
Colleague: "We need the relevant source and ___." | date | A traceable status statement must identify its source and time reference.
Adviser: "We cannot assume the status is either unchanged or ___." | changed | Without verification, neither continuity nor a change can be asserted as established.'''))

BOOK['units'].append(unit(
    title='Coordinating cross-border document production', scene='Access is not authority to export',
    skill='Explain preservation, review, disclosure, and transfer as separate steps while coordinating conflicting legal requirements.',
    brief='US litigation counsel requests records held by a European affiliate. IT contact Dana can technically export the files. Coordinating lawyer Samir has not yet completed the review of privilege, personal data, applicable transfer requirements, or the production scope. A preservation instruction is already in place. No legal basis, disclosure permission, or deadline is established by this fictional case; real timing questions require prompt qualified review.',
    cast='Dana | IT records contact\nSamir | Coordinating lawyer',
    culture=('Technical capability is one fact, not the legal answer', 'An IT colleague can help preserve and identify information without being asked to make a cross-border legal decision. Explain the separate review stages in practical language.'),
    a='''What can Dana do technically? | Export the files | Decide every privilege issue | Establish a lawful transfer basis alone | Guarantee production is complete | Dana's technical access does not supply the unresolved legal permissions.
What instruction is already in place? | Preservation | Unrestricted overseas production | Public disclosure | Destruction after export | The case identifies preservation as the established instruction, not disclosure or deletion.
Which review remains unfinished? | Privilege, personal data, transfer requirements, and scope | Whether the files can technically be exported | Whether counsel requested records | Whether an affiliate holds records | The stated legal reviews remain incomplete and must not be presumed resolved.''',
    vocabulary='''document production | Disclosure of documents under the relevant proceeding or legal process. | define document production scope
preservation hold | Instruction to retain relevant information under the applicable process. | maintain a preservation hold
custodian | Person or source responsible for potentially relevant records. | identify a record custodian
collection scope | Boundaries of information gathered for review. | define the collection scope
review set | Documents selected for a specified review stage. | assemble the review set
responsiveness | Relevance of a document to the actual request or production criteria. | assess responsiveness
legal privilege | Protection for specified communications or material under applicable law. | assess legal privilege locally
privilege log | Record identifying withheld material as required by the relevant procedure. | prepare the required privilege log
redaction | Removal or obscuring of specified information in a disclosed copy. | verify a redaction
personal data | Information concerning an identified or identifiable person under the applicable definition. | identify personal data
cross-border transfer | Movement or disclosure of information across relevant legal borders. | assess a cross-border transfer
transfer mechanism | Arrangement relied on under the applicable data-transfer rules. | verify the transfer mechanism
lawful basis | Legal justification required for the relevant processing or action. | assess the lawful basis
data controller | Entity determining purposes and means of processing under the applicable data-protection framework. | identify the data controller
blocking statute | Law restricting specified information disclosure or cooperation in the relevant context. | assess a blocking statute
protective order | Order limiting use or disclosure of material under the relevant court process. | examine a protective order
chain of custody | Traceable handling history of evidence or records. | preserve the chain of custody
production protocol | Agreed or directed specifications for document production. | confirm the production protocol''',
    precision='Preserving files, collecting them for review, and producing them abroad are distinct actions. Technical access and a foreign request do not by themselves settle all relevant disclosure and transfer requirements.',
    precision_extra='Neither this exercise nor a generic privacy label resolves the actual conflict of obligations. Qualified counsel must address current law, court directions, preservation, and real timing promptly; do not destroy records or improvise a transfer.',
    phrases='''Separate capability | The export is technically possible; legal authorization is a separate question.
Preserve first principles | The preservation instruction remains in place while review proceeds.
Define the request | Which custodians, dates, and document categories are actually requested?
Identify the stages | Collection for review is not the same as external production.
Clarify privilege | We need the applicable privilege analysis, not a label added to every file.
Check transfer | The cross-border disclosure requirements need the appropriate review.
Escalate competing duties | Counsel must reconcile the actual obligations and timing.
Report readiness accurately | The files are accessible, but production is not yet authorized.''',
    notes='''Can versus may | Can can describe technical ability; may can describe permission. State which meaning is intended.
Preserve versus produce | Preserving retains information; producing discloses it through a legal process. One instruction does not imply the other.
All relevant | Relevant requires a defined request and review criteria, not an unbounded export of everything accessible.''',
    d='''Which statement accurately separates the stages? | Preservation remains active; disclosure review is incomplete | Export capability proves lawful production | A foreign request resolves every data rule | Privilege labels eliminate the need for review | This statement preserves the existing instruction and the unfinished legal work.
What should Dana not decide from technical access? | Whether every file may be disclosed abroad | Whether a file can be located | Whether an export function exists | Which system stores the records | Disclosure permission requires the relevant legal review, not merely system access.
Which action would conflict with the stated instruction? | Deleting preserved records to reduce the review set | Identifying custodians | Clarifying the request | Maintaining the preservation hold | The preservation instruction remains active and must not be undermined by deletion.
Which summary is most useful for counsel? | Files accessible; scope, privilege, and transfer questions unresolved | Everything is ready because export works | No records exist because review is unfinished | The IT team has decided all legal issues | This summary identifies both the technical fact and the specific unresolved legal questions.''',
    dialogue='''Dana | The US team requested the affiliate's records, and I can export the folders this afternoon. Does that mean we are ready?
Samir | Technically accessible is not the same as authorized [[document production::Document production is disclosure under the relevant legal process, and technical export capability does not establish permission to disclose all files.]]. We still need to resolve scope, privilege, personal-data, and transfer questions.
Dana | The preservation instruction is already active. I will not delete anything just because it might be outside the eventual production.
Samir | Correct. The [[preservation hold::A preservation hold retains relevant information under the actual process and remains distinct from a later decision about disclosure.]] remains in place while the appropriate review determines what is collected and disclosed.
Dana | Which information will help you define the request without asking me to decide the legal relevance of every file?
Samir | Start with the actual [[custodian::A custodian identifies a person or source associated with potentially relevant records, helping counsel define and review the requested information.]] and system information, dates, and document categories requested. We will clarify the review criteria with counsel.
Dana | I can identify the folders and access permissions. That does not mean every file in them responds to the request.
Samir | Exactly. [[Responsiveness::Responsiveness concerns whether a document meets the actual request or production criteria and cannot be inferred from its folder location alone.]] needs review against the defined request, rather than assuming that everything in one folder belongs in the production.
Dana | Some files are labeled confidential or privileged. Should I exclude all of them automatically based on the label?
Samir | No. [[Legal privilege::Legal privilege depends on the applicable law and actual material, so a file label cannot replace the required jurisdiction-specific assessment.]] requires the applicable analysis. A label is a fact to review, not a complete legal determination.
Dana | We also have personnel information in some attachments, and the receiving team is outside the country where the records are held.
Samir | Then [[personal data::Personal data in the records raises relevant information-handling questions that must be assessed alongside the actual production obligations.]] and cross-border requirements need to be assessed alongside the actual litigation obligations and directions.
Dana | Does the request from overseas counsel automatically provide the transfer permission, or is that another issue for the review?
Samir | It is another issue. The appropriate [[transfer mechanism::A transfer mechanism must be assessed under the applicable rules and is not automatically supplied by a foreign request or technical ability to export.]] and other relevant requirements cannot simply be inferred from the existence of the request.
Dana | If a reviewed copy needs information removed, I should keep the original preserved and follow the actual production instructions.
Samir | Yes. A [[redaction::A redaction removes or obscures specified information in a disclosed copy and should follow the actual reviewed production instructions while originals are preserved appropriately.]] must follow the verified instructions and be checked, not improvised by anyone trying to shorten the file.
Dana | I will also record how the files were handled so that the review team can trace the material it receives.
Samir | That preserves the [[chain of custody::Chain of custody records handling history so the identity and integrity of evidence can be traced through the actual collection and review process.]]. Traceability matters alongside the legal scope and the safeguards for the actual information exchange.
Dana | My update will say the files are accessible, preservation continues, and external production is not yet authorized.
Samir | Good. We will clarify the [[production protocol::The production protocol specifies the actual agreed or directed production requirements and should not be replaced by a convenient unreviewed export format.]] and address real timing promptly with responsible counsel, without asking IT to resolve competing legal duties alone.''',
    rehearsal=['Read the corrected exchange and distinguish technical access, preservation, review, and production.', 'Swap roles and give the readiness update without authorizing an export or resolving a legal conflict yourself.'],
    transfer_title='The export file is ready, but review is not', transfer_setup='IT has prepared a review copy under the preservation process. Privilege and transfer review remain incomplete. No external production has been authorized.',
    transfer='''IT: "The review copy is technically ___." | ready | The technical preparation is complete, which is narrower than production authorization.
Counsel: "The legal review remains ___." | incomplete | Privilege and transfer questions have not yet been resolved in the case.
IT: "External production is not ___." | authorized | No permission for external production is supplied by the brief.
Counsel: "The preservation instruction stays in ___." | place | The existing preservation process continues while the remaining review is completed.'''))

BOOK['units'].append(unit(
    title='Negotiating settlement language across legal systems', scene='A commercial proposal is not a signed settlement',
    skill='Separate negotiating positions, authority, drafting status, and legal effect in a cross-border settlement update.',
    brief='Company representative Nadiya and counsel Felix discuss a proposed settlement of a cross-border commercial dispute. The business teams have discussed a payment figure, but release scope, governing documents, approval authority, and execution remain unresolved. No final legal-effect opinion or binding settlement is established. An email uses without prejudice and subject to contract; counsel explains that their effect must be assessed in the actual jurisdiction and context.',
    cast='Nadiya | Company representative\nFelix | Counsel',
    culture=('Agreement on one point is not agreement on every point', 'Recognize commercial progress while stating the unresolved terms. Do not assume that familiar English negotiation labels have identical effects across legal systems.'),
    a='''Which point has been discussed commercially? | A payment figure | Every release provision | Final execution | Complete approval authority | The brief establishes discussion of a figure, not a completed settlement package.
Which issue remains unresolved? | Release scope and execution | Whether a dispute exists | Whether emails were exchanged | Whether a figure was discussed | The case explicitly leaves release terms, authority, documents, and execution unresolved.
What must be checked about the email labels? | Their actual jurisdictional and contextual effect | Whether English labels work identically everywhere | Whether labels remove all need for advice | Whether the subject line alone guarantees confidentiality | Their legal effect depends on the relevant law and context rather than the words alone.''',
    vocabulary='''settlement proposal | Offer or suggested terms for resolving a dispute. | clarify a settlement proposal
agreement in principle | Preliminary understanding whose legal effect depends on its actual terms and context. | qualify an agreement in principle
subject to contract | Negotiation label whose effect depends on the applicable law and circumstances. | assess subject-to-contract wording
without prejudice | Label associated with settlement communications whose protection depends on applicable rules and context. | assess without-prejudice protection
settlement authority | Power to approve or enter the relevant settlement. | verify settlement authority
release | Provision giving up specified claims or rights under its terms. | define the release scope
waiver | Relinquishment of a right or requirement under the applicable circumstances. | distinguish a waiver
reservation of rights | Statement seeking to preserve specified rights. | preserve a reservation of rights
no-admission clause | Wording stating that settlement does not constitute a specified admission. | review a no-admission clause
confidentiality clause | Provision governing specified information disclosure. | negotiate a confidentiality clause
non-disparagement clause | Provision restricting specified negative statements under its actual terms. | review a non-disparagement clause
payment condition | Condition governing when or how a payment is due under the agreement. | clarify a payment condition
execution | Formal signing or completion of a document in the relevant context. | confirm execution status
counterpart | Separately signed copy forming part of an agreement under the relevant arrangements. | check counterpart execution
conditions precedent | Specified conditions required before an obligation or transaction proceeds under its terms. | identify conditions precedent
entire agreement clause | Provision addressing the relationship between the written agreement and prior communications. | review an entire agreement clause
term sheet | Summary of proposed or agreed principal terms with context-dependent legal effect. | qualify the term sheet's status
settlement implementation | Carrying out the actual obligations in the settlement. | plan settlement implementation''',
    precision='A discussed payment figure does not establish that every term, approval, and execution step is complete. Do not rely on without prejudice, subject to contract, or agreement in principle as universal legal-effect switches.',
    precision_extra='The actual wording and conduct may have legal consequences requiring qualified advice. This exercise does not determine whether negotiations are binding, protected, or enforceable in a real jurisdiction.',
    phrases='''Recognize progress | There is commercial progress on the figure, with other terms still open.
Separate authority | Who can approve the settlement for the actual entity?
Define release | Which claims, parties, and periods would the release cover?
Qualify the label | That phrase needs assessment under the applicable law and context.
Track drafting | This is the current proposal, not a confirmed executed document.
Avoid admission | Let us distinguish the proposed payment from any admission of liability.
Preserve conditions | The payment trigger and outstanding approvals must remain visible.
Report accurately | We have a negotiating position, with legal effect and final terms still under review.''',
    notes='''Discussed versus agreed | Discussed reports negotiation; agreed should identify the precise point and actual status supported by the record.
In principle | In principle signals a preliminary character in ordinary speech, but legal effect still needs the actual contextual analysis.
Executed versus performed | Executed can refer to signing a document; performed refers to carrying out obligations. Clarify which meaning is intended.''',
    d='''Which status report best fits the facts? | A figure was discussed; release, authority, and execution remain open | The entire dispute is conclusively settled | Every affiliate released every claim | Payment has been received | This report preserves commercial progress and the explicitly unresolved legal terms.
Which question clarifies release scope? | Which claims and parties would this wording cover? | Which font looks final? | Who suggested the round number? | Can we omit every definition? | A release needs its actual claims, parties, and other scope limits identified.
Which assumption about without prejudice should be avoided? | The label guarantees identical protection in every jurisdiction | Its effect needs legal review | Context can matter | The actual communication must be examined | A familiar label does not create universal protection regardless of applicable law or context.
Which distinction matters after signing? | Execution of the document and performance of its obligations | Signature and handwriting | Payment and a payment figure | Counsel and a lawyer | Signing and carrying out the settlement obligations are distinct stages that should be reported separately.''',
    dialogue='''Nadiya | The business teams discussed a payment figure, and I would like to tell the board that the dispute is settled.
Felix | We can report progress, but the [[settlement proposal::A settlement proposal states suggested terms and should not be treated as a completed binding resolution when key matters remain unresolved.]] still leaves the release, approvals, documents, and execution unresolved.
Nadiya | They called it an agreement in principle. I thought that phrase supplied a clear legal answer about the whole negotiation.
Felix | [[Agreement in principle::Agreement in principle describes a preliminary understanding in ordinary use, while its actual legal effect depends on the terms, conduct, and applicable law.]] needs its actual terms and context examined. It should not become a shortcut around the unresolved legal questions.
Nadiya | The parent approved the discussion, but I do not know who can bind the subsidiary involved in the claim.
Felix | Then verify [[settlement authority::Settlement authority identifies who can approve or enter the agreement for the relevant legal person and is not established by a different entity's informal approval.]] for the actual entity. Group-level support and power to bind the relevant company may be different.
Nadiya | The proposed release says all claims, but nobody has clarified which parties or periods that phrase is intended to cover.
Felix | The [[release::A release gives up specified claims or rights under its terms, so its parties, claims, and other scope limits require careful definition.]] needs a defined scope. A broad phrase can conceal a major disagreement rather than resolve it.
Nadiya | One email says without prejudice. Can I assume that makes every statement protected in every country involved?
Felix | No. [[Without prejudice::Without prejudice is a legal-context label whose protection depends on the relevant rules and circumstances, not a universal guarantee created by typing the words.]] needs assessment under the applicable law and context. The label is not a universal protection switch.
Nadiya | Another draft says subject to contract. We should check its actual effect rather than rely on familiar wording alone.
Felix | Exactly. [[Subject to contract::Subject to contract must be assessed in the actual legal context and cannot by itself answer every question about the parties' words and conduct.]] is part of the material counsel reviews, not a substitute for that review.
Nadiya | We also want the proposal to avoid suggesting that payment is an admission of the allegations.
Felix | Then the intended [[no-admission clause::A no-admission clause addresses specified admissions in its actual wording and should be reviewed rather than assumed from the payment proposal alone.]] needs careful drafting and review alongside the rest of the agreement, rather than being assumed from the figure.
Nadiya | Even if signatures are arranged, we still need to know when payment becomes due and what approvals come first.
Felix | Yes. The [[payment condition::A payment condition defines the actual trigger or terms for payment and must remain distinct from a figure merely discussed in negotiations.]] and any relevant prerequisites must be explicit in the actual document.
Nadiya | I have been using executed to mean both signed and completely carried out, which could confuse the status report.
Felix | Clarify [[execution::Execution in this document context concerns formal signing or completion, which should not be confused with later performance of the settlement obligations.]] as the signing stage here, and report performance separately when the actual obligations are carried out.
Nadiya | My revised update will identify the commercial discussion and the open terms, without declaring the legal result settled.
Felix | That gives the board an accurate picture and leaves [[settlement implementation::Settlement implementation concerns carrying out the actual obligations after their status and terms are established, not assuming performance from a negotiating proposal.]] to be planned against the verified final position, not an optimistic summary.''',
    rehearsal=['Read the corrected negotiation update and distinguish a discussed figure, authority, execution, and performance.', 'Swap roles and give the board update while preserving the unresolved terms and jurisdictional qualifications.'],
    transfer_title='Signed does not mean paid', transfer_setup='A settlement document has been signed. The payment date under its actual terms is in the future, and no payment has been received. Counsel does not assess any other legal issue in this update.',
    transfer='''Counsel: "The document has been ___." | signed | Signing is the completed step explicitly established by the brief.
Client: "The payment date is still in the ___." | future | The actual payment date has not yet arrived in this scenario.
Counsel: "No payment has been ___." | received | The case explicitly distinguishes signing from actual receipt of funds.
Client: "Signing and performance are separate ___." | stages | Executing the document and carrying out its obligations are different status events.'''))
