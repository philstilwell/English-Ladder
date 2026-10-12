"""Three additional international-law scenarios with primary reference links."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Explaining the jurisdiction question in an interstate dispute',
    skill='Separate an allegation on the merits from the basis for an international court to hear a contentious case.',
    setup='State adviser Amel briefs colleague Rowan about a fictional dispute between two states. Rowan assumes that describing an international-law allegation automatically establishes the International Court of Justice\'s jurisdiction. No particular consent instrument, declaration, reservation, or jurisdictional determination is supplied. They identify the questions that require legal review before reporting a jurisdictional conclusion.',
    cast='Rowan | Legal colleague\nAmel | State legal adviser',
    reference=('ICJ. Basis of the Court\'s jurisdiction.', 'https://www.icj-cij.org/index.php/basis-of-jurisdiction'),
    dialogue='''Rowan | The allegation concerns international law, so I assumed the Court can hear the dispute without a separate jurisdictional question.
Amel | We need to separate the substance of the allegation from the legal basis for the Court to hear this contentious case.
Rowan | Both parties are states, but that fact alone does not identify the relevant consent basis, does it?
Amel | Correct. [[Consent-based jurisdiction::Consent-based jurisdiction requires the relevant basis of state consent to be identified; an allegation concerning international law does not itself supply that basis.]] needs its actual basis examined rather than being inferred from the subject matter alone.
Rowan | I can gather any agreement, treaty provision, or declaration the team proposes to rely on.
Amel | Please also identify its scope and qualifications. A reference to an instrument is not a conclusion that it covers every dispute.
Rowan | Then a question about the court's authority should remain separate from whether the alleged conduct breached an obligation.
Amel | Yes. The [[merits::The merits concern the substantive dispute, which is distinct from the preliminary question of the Court's authority to hear the case.]] and jurisdiction address different questions, even when some facts matter to both parts of the analysis.
Rowan | The briefing currently says the respondent must lose because our jurisdiction paragraph sounds strong.
Amel | That conflates two conclusions. We have not established either the jurisdictional position or the merits from the limited information here.
Rowan | Would a consent instrument's subject-matter limits need to stay visible in the summary?
Amel | Certainly. [[Jurisdictional scope::Jurisdictional scope identifies which disputes or issues the asserted consent basis covers and must not be broadened by a shortened summary.]] cannot be broadened simply because the full qualification is inconvenient in a short briefing.
Rowan | We should also check any relevant dates or reservations rather than assume the same position throughout history.
Amel | Exactly. A [[reservation to consent::A reservation to consent can qualify the asserted jurisdictional basis and requires analysis of its actual wording and applicable effect.]] or another relevant qualification may affect the actual analysis and must be reviewed in context.
Rowan | I will distinguish the materials we have found from a legal conclusion that the Court has already accepted the case.
Amel | Good. A proposed [[jurisdictional basis::A jurisdictional basis is the legal foundation asserted for the Court's authority and must be distinguished from a determination accepting that foundation.]] is not the same as a judicial determination that it is sufficient.
Rowan | The note can identify the open questions and the legal work needed before anyone announces a jurisdictional result.
Amel | That is more useful than an overconfident headline that later advisers must unwind.
Rowan | My revised summary will say the allegation and possible consent materials are being reviewed, with no determination reported.
Amel | Then the [[procedural posture::Procedural posture describes the actual stage and status of a matter, preventing a proposed legal position from being reported as an established court outcome.]] remains accurate, and the reader can distinguish our analysis from an outcome that has not occurred.''',
    transfer_title='A possible basis became a court determination', transfer_setup='A briefing identifies a possible treaty-based jurisdictional argument. No court determination is supplied. An executive summary mistakenly says jurisdiction has been confirmed.',
    transfer='''Adviser: "The briefing identifies a possible ___." | argument | The briefing presents a possible legal position rather than an established outcome.
Colleague: "No court determination is ___." | supplied | The case contains no judicial decision confirming the asserted jurisdictional basis.
Adviser: "The summary overstated the ___." | status | It changed an argument under review into a purported confirmed result.
Colleague: "I will restore the distinction between argument and ___." | determination | A party's legal argument and a court's decision are different procedural facts.'''),
scenario(title='Explaining what an Apostille does and does not certify',
    skill='Distinguish authentication of a public document\'s origin from a guarantee of its substantive truth or acceptance for every purpose.',
    setup='Client contact Jo asks legal coordinator Mira whether an Apostille proves every statement in a public document is true and guarantees that the receiving body must accept it for the intended transaction. No particular document, country pair, or receiving-body requirement is supplied. Mira explains the limited authentication function and identifies the actual applicability and use questions for verification.',
    cast='Jo | Client contact\nMira | Legal coordinator',
    reference=('HCCH. The ABCs of Apostilles.', 'https://www.hcch.net/en/publications-and-studies/details4/?pid=4967'),
    dialogue='''Jo | The document has an Apostille. Can I tell the receiving body that this proves every statement inside it is true?
Mira | No. We need to distinguish authentication of the document's origin from a guarantee of the substantive information it contains.
Jo | I thought the certificate was a broad endorsement of the document and the transaction it will be used for.
Mira | An [[Apostille::An Apostille authenticates specified origin-related features of a public document under the applicable Convention process, not the substantive truth of every statement.]] concerns the relevant signature, capacity, and seal or stamp under the applicable process, not the truth of every underlying statement.
Jo | Then I should not describe the certificate as an independent legal opinion on the transaction either.
Mira | Correct. [[Authentication::Authentication addresses specified origin-related features and must not be confused with an opinion on the underlying transaction's legal effect.]] and the legal effect of the underlying document answer different questions.
Jo | We still need to know whether the Convention applies to the actual document and the relevant countries.
Mira | Yes. The [[applicability check::An applicability check examines the actual document and country relationship rather than assuming every public document and destination uses the same process.]] must use current official information and the actual document circumstances.
Jo | Who verifies the certificate if the receiving body has a question about it?
Mira | The relevant [[Competent Authority::The Competent Authority is the designated body with the relevant Apostille function, and its identity should be verified through official information.]] and official verification arrangements should be identified. We should not invent a verification result ourselves.
Jo | The recipient may also have a specific requirement for the document's purpose, date, or translation.
Mira | Those [[receiving-body requirements::Receiving-body requirements concern the actual intended use and may raise questions distinct from authenticating the origin of the public document.]] need to be clarified separately rather than assumed satisfied by the certificate alone.
Jo | So a certificate can address one formality without deciding whether the document meets every substantive requirement for the application.
Mira | Exactly. We should explain the completed authentication step and the remaining use questions without calling the whole transaction approved.
Jo | I will keep the actual document and certificate together when asking for the appropriate review.
Mira | Good. That preserves the [[document linkage::Document linkage keeps the certificate associated with the relevant public document so the reviewer can identify what the authentication concerns.]] and avoids discussing a certificate detached from the material it concerns.
Jo | I also should not claim that a general website description has verified our particular country pair or document category.
Mira | Correct. We need the actual facts and current official information for that conclusion.
Jo | My summary will say the certificate addresses origin-related authentication, while the intended use still needs its relevant checks.
Mira | That is precise. It avoids turning a limited certificate into a guarantee of substantive truth, legal validity, or universal acceptance.''',
    transfer_title='The certificate was treated as proof of the contents', transfer_setup='A summary says an Apostille proves the underlying document\'s statements are true. The actual question concerns the certificate\'s limited authentication function, not a verified substantive conclusion.',
    transfer='''Coordinator: "The certificate concerns specified origin-related ___." | authentication | The authentication function concerns the relevant signature, capacity, and seal or stamp.
Client: "It does not guarantee the contents are ___." | true | Authentication does not independently establish the substantive truth of every statement.
Coordinator: "The intended use needs its own relevant ___." | checks | The receiving purpose may raise requirements separate from the authentication formality.
Client: "I will correct the overbroad ___." | summary | The summary must describe the certificate's actual scope without adding a universal guarantee.'''),
scenario(title='Reconciling a bilingual contract discrepancy',
    skill='Explain a material translation difference without silently choosing a controlling version or amending the parties\' agreement.',
    setup='Translator Eli and counsel Sana compare two versions of a fictional contract. One says a party may provide a report; the other describes reporting as mandatory. The governing-language provision and parties\' intended obligation have not been verified. They preserve both texts and route the discrepancy for legal and client review rather than silently rewriting either version.',
    cast='Eli | Legal translator\nSana | Counsel',
    dialogue='''Eli | I found a difference that changes the obligation: one version says may provide, while the other makes the report mandatory.
Sana | That is not just a stylistic preference. Please identify the exact clauses and keep both source versions intact.
Eli | I can explain the language difference, but I cannot decide by myself which obligation the parties intended to accept.
Sana | Correct. The [[modal discrepancy::A modal discrepancy changes the force of wording such as permission and obligation, so it can be legally material rather than merely stylistic.]] needs legal and client review before either version is silently corrected.
Eli | The file also contains a working translation, and I do not know whether it was ever approved for signing.
Sana | Then preserve the [[version status::Version status identifies whether a document is a draft, working translation, approved text, or signed version and must remain visible during reconciliation.]] of each document so we do not compare an unsigned draft as though it were the executed agreement.
Eli | Would a governing-language clause answer which text controls if there is a conflict?
Sana | We need to verify the actual [[governing-language provision::A governing-language provision may address which language version prevails, but its actual wording and legal effect must be reviewed rather than assumed.]] and its effect. We cannot assume one exists or that English necessarily prevails.
Eli | I will quote the two short passages and describe the difference as discretion versus a mandatory duty.
Sana | That is a useful [[translation query::A translation query identifies a specific language issue for clarification without deciding the legal effect or amending the agreement on the translator's own authority.]], provided it does not present your proposed wording as a legal amendment already agreed by the parties.
Eli | I can suggest alternative wording after the intended meaning is clarified, with the change tracked for review.
Sana | Yes. We need the appropriate authority and review process, not a quiet replacement that loses the original discrepancy.
Eli | The business team wants the documents aligned today, but speed does not establish the missing instruction.
Sana | A [[tracked revision::A tracked revision makes a proposed wording change visible for review and does not itself prove that the parties authorized or accepted the change.]] helps reviewers see what changed; it does not supply the consent or legal conclusion by itself.
Eli | We should also check whether the same modal difference appears in related definitions or reporting provisions.
Sana | That is a sensible consistency question, but keep the search scope and findings separate from a claim that every issue is resolved.
Eli | My note will identify the clauses, versions, linguistic difference, and the unanswered question for counsel and the client.
Sana | Then the [[reconciliation record::A reconciliation record preserves the discrepancy, review, and authorized resolution rather than hiding a material difference through untracked editing.]] can preserve the original problem and the authorized resolution when it is actually reached.
Eli | Until then, neither version should be rewritten merely because one sounds more natural to me in English.
Sana | Exactly. Linguistic fluency supports the review; it does not replace the legal and contractual authority needed to settle the meaning.''',
    transfer_title='May became must', transfer_setup='A translation changes may submit to must submit. No instruction authorizing a stronger obligation is supplied. Counsel requests a query rather than an unapproved amendment.',
    transfer='''Translator: "The original uses ___." | may | May expresses permission or discretion in the wording supplied for this comparison.
Counsel: "The translation strengthened it to ___." | must | Must introduces a mandatory force not authorized by the supplied instruction.
Translator: "The discrepancy needs a translation ___." | query | The issue should be raised for clarification rather than silently decided.
Counsel: "No stronger obligation has been ___." | authorized | The case supplies no approval to replace the original wording with a stronger duty.'''),
]
