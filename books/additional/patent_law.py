"""Additional patent conversations: title, renewal verification, and translation."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Separating inventorship from the ownership record',
    skill='Explain a document gap without confusing inventor identity, assignment, recordation, and ownership.',
    setup='IP coordinator Mina and counsel Joel review a fictional US patent file. The inventor list names two people. A database shows a recorded assignment, but the underlying instrument and its scope have not been reviewed. Mina initially treats the database entry as proof that every ownership issue is resolved. No conclusion on title or document validity is supplied.',
    cast='Mina | IP coordinator\nJoel | Counsel',
    reference=('USPTO. MPEP 301: Ownership and assignability.', 'https://www.uspto.gov/web/offices/pac/mpep/s301.html'),
    dialogue='''Mina | The patent lists two inventors, while the assignment database names a company. I thought one of those records must be wrong.
Joel | They address different questions. Inventor identity and ownership can differ, and the actual documents need to be examined.
Mina | The company paid for development, but I should not use that fact alone to decide who invented the claimed subject matter.
Joel | Correct. [[Inventorship::Inventorship identifies the relevant inventors under the applicable legal test and is not settled merely by who funded the work.]] is not a synonym for funding, employment, or present ownership.
Mina | The database also shows a recorded transfer. Does that mean the office has determined the underlying document is legally valid?
Joel | No. [[Recordation::Recordation is the recording step and does not itself establish the validity or ownership effect of the underlying assignment instrument.]] does not supply that substantive conclusion merely because an entry appears in the database.
Mina | We need the instrument itself, including the parties, subject matter, signatures, and any relevant conditions.
Joel | Yes. Review the actual [[assignment::An assignment is the instrument or transaction transferring the relevant interest, whose actual scope and legal effect require review.]] rather than treating a short database entry as the entire transaction.
Mina | The file contains one scanned document, but I do not know whether it covers both inventors or every relevant application.
Joel | Then those are specific open questions. We should not silently extend the document beyond the parties and rights it actually addresses.
Mina | I can assemble the related documents in sequence and mark any missing link instead of declaring the file complete.
Joel | That supports the [[chain of title::The chain of title traces relevant ownership transfers and requires examination of the actual links rather than a single isolated entry.]] review, while keeping the distinction between documents located and ownership conclusions reached.
Mina | One company name also changed after a reorganization. The folder uses both names without explaining the relationship.
Joel | Preserve the records and obtain the relevant [[entity identification::Entity identification establishes which legal person each document concerns and prevents a name change from being mistaken for an unexplained transfer.]] information rather than assuming that similar names identify the same party.
Mina | The business team wants a short status for diligence. I can say the entry was found but the instrument is still being reviewed.
Joel | That is accurate and tells them what remains unresolved without implying a defect that has not been established either.
Mina | We should avoid both extremes: guaranteed clean title and an unsupported assertion that the company owns nothing.
Joel | Exactly. The [[title assessment::The title assessment is the qualified evaluation of ownership and its supporting documents, not an automatic result of a database search.]] must follow the evidence and applicable law.
Mina | I will supply the inventor record, database entry, underlying instrument, and entity documents as separate labeled items.
Joel | Then the review can address the actual questions without confusing invention, transfer, recording, and present ownership in one headline.''',
    transfer_title='Recorded became legally validated', transfer_setup='A status note says a database entry proves an assignment is valid. The instrument has not been reviewed.',
    transfer='''Coordinator: "The database shows ___." | recordation | The database establishes the recorded entry, not every substantive legal conclusion.
Counsel: "The underlying ___ still needs review." | instrument | The actual transfer document must be examined for its relevant effect.
Coordinator: "The note overstated legal ___." | validity | Recording alone does not establish the assignment document's substantive validity.
Counsel: "Keep the ownership conclusion ___." | qualified | The unresolved document review prevents an unqualified ownership assurance.'''),
scenario(title='Verifying a patent-renewal payment request',
    skill='Challenge an official-looking request while keeping genuine maintenance obligations visible.',
    setup='Accounts officer Alex receives a letter headed urgent patent cancellation notice. It names the correct patent but comes from an unfamiliar private sender and requests payment through a link. Patent administrator Suri has not verified the sender or the real maintenance status. They route the request through known official and professional channels without assuming that the patent has no genuine deadline.',
    cast='Alex | Accounts officer\nSuri | Patent administrator',
    reference=('USPTO. Non-USPTO solicitations.', 'https://www.uspto.gov/patents/basics/using-legal-services/scam-prevention/non-uspto-solicitations'),
    dialogue='''Alex | This letter names our patent and says urgent cancellation notice. Should I pay through the link before we lose the rights?
Suri | Do not treat the heading or correct patent number as authentication. We need to verify the sender and the actual obligation.
Alex | The sender is a private organization I do not recognize, but the letter uses formal language and details from the patent record.
Suri | Those details may be public. An official-looking [[solicitation::A solicitation can use public patent details without being an official fee notice, so appearance alone does not establish authority.]] is not proof that the sender is the patent office or our authorized provider.
Alex | I will not use the supplied payment link while the request remains unverified. What information should I send you?
Suri | Preserve the letter and sender details through our approved reporting process, without sharing credentials or making an unverified payment.
Alex | We should separately check whether a genuine maintenance obligation exists, even if this particular request is questionable.
Suri | Exactly. Verify the actual [[maintenance status::Maintenance status concerns the real patent record and obligations, which remain a separate question from whether the received letter is authentic.]] through known official channels and the responsible patent professional.
Alex | The accounts system has a contact from our previous legitimate instruction, rather than the phone number printed in this letter.
Suri | Use an independently verified [[trusted contact::A trusted contact is verified independently of the suspicious request, reducing reliance on contact details supplied by the same unverified sender.]] to confirm the matter under our normal controls.
Alex | I can flag the request as unverified rather than mark it paid or dismiss every possible deadline.
Suri | Good. The [[payment authorization::Payment authorization must follow the actual approved process and cannot be inferred from urgency or an official-looking design.]] needs to come through the established process after the obligation and payee are checked.
Alex | The letter's urgency made me assume that asking questions would itself cause a loss of rights.
Suri | Prompt verification matters, but urgency should not bypass controls or turn an unverified demand into a confirmed obligation.
Alex | Once you have checked, we should record the source used and any real action the responsible professional instructs.
Suri | Maintain that [[verification record::The verification record preserves the source, finding, and authorized next action rather than leaving only a vague assurance that someone checked.]] so accounts and the patent team rely on the same confirmed information.
Alex | If a payment is genuinely required, the team will use the approved route and retain the actual receipt.
Suri | Yes, and the [[payment confirmation::Payment confirmation is evidence of the actual completed payment, not the original request or an internal intention to pay.]] should remain distinct from the request, authorization, and filing or maintenance status.
Alex | I will route the letter now, keep the real timing question visible, and avoid using the unverified link.
Suri | That addresses both risks: an improper payment and a genuine obligation being overlooked while the suspicious request is investigated.''',
    transfer_title='Correct details do not authenticate a sender', transfer_setup='An unfamiliar letter includes the correct patent number but has not been verified. The actual maintenance status also needs checking.',
    transfer='''Accounts: "The patent number is correct, but the sender is ___." | unverified | Correct public details do not establish that the sender is authentic.
Administrator: "Use an independently verified ___." | channel | Verification should not depend on contact details in the unverified request.
Accounts: "The real maintenance obligation needs a separate ___." | check | Sender authenticity and actual patent maintenance status are different questions.
Administrator: "Do not bypass payment ___ because of urgency." | controls | Urgent wording does not replace the established authorization and verification process.'''),
scenario(title='Resolving a material patent-translation query',
    skill='Explain a quantifier discrepancy and preserve version control without silently changing technical scope.',
    setup='Translator Aiko compares a source draft saying at least two channels with a translation saying exactly two channels. The text is being prepared for professional review; no filing has occurred. Patent professional Rosa needs the discrepancy raised explicitly. Aiko can explain the linguistic difference but cannot independently decide the final claim scope or legal filing strategy.',
    cast='Aiko | Patent translator\nRosa | Patent professional',
    dialogue='''Aiko | I found a scope difference in the draft. The source says at least two channels, but the translation says exactly two.
Rosa | Please identify the exact sentence and version. Those expressions are not stylistic alternatives with the same numerical meaning.
Aiko | At least two permits two or more in ordinary numerical language, while exactly two restricts the count to two.
Rosa | That [[quantifier discrepancy::The quantifier discrepancy changes the stated numerical range, so it needs substantive review rather than a silent stylistic correction.]] needs an explicit query before we settle the reviewed text.
Aiko | I can explain the language issue without deciding whether the final patent claim should use the broader or narrower expression.
Rosa | Correct. Preserve the [[source wording::The source wording is the actual expression being translated and must remain available while the intended meaning and legal implications are reviewed.]] and do not quietly rewrite either version to match your preferred interpretation.
Aiko | The engineering drawing shows two channels, but that alone does not tell me which quantifier the drafter intended.
Rosa | Good distinction. A pictured example and the intended wording need to be checked against the relevant disclosure and drafting instructions.
Aiko | I will attach the short source passage, translated passage, and explanation of the difference in ordinary English.
Rosa | That is a useful [[translation query::A translation query identifies a specific discrepancy for authorized resolution without granting the translator authority to choose the legal scope.]]. It lets the technical and patent reviewers answer the actual question.
Aiko | The file name currently says final, although this issue and several terminology questions are still open.
Rosa | Correct the [[version label::The version label should reflect the actual review status rather than imply final approval while material questions remain unresolved.]] so nobody mistakes a working translation for approved filing text.
Aiko | Once the reviewers confirm the intended expression, I can apply the authorized wording and check related occurrences.
Rosa | Use a [[controlled revision::A controlled revision makes the authorized change traceable and preserves the relationship between the approved instruction and revised text.]] that preserves what changed, who approved it, and which passages were checked.
Aiko | We should also check whether the same quantifier appears in the summary or dependent claims, rather than correcting only one line.
Rosa | Yes, but report the actual review coverage instead of claiming that every possible language issue has been eliminated.
Aiko | After the check, I will return both a marked version and a clean version with the same date and identifier.
Rosa | Then the [[terminology check::The terminology check verifies consistent use within its stated scope and complements, rather than replaces, the substantive quantifier review.]] can be reviewed separately from the decision about the numerical wording.
Aiko | The delivery note will say the identified query was resolved under instruction, not that I independently certified patent scope.
Rosa | Exactly. Accurate translation supports the legal process while keeping linguistic explanation, technical intent, and legal authority distinct.''',
    transfer_title='At least became at most', transfer_setup='A source draft says at least three sensors. Its translation says at most three sensors. No instruction authorizes changing the numerical relationship.',
    transfer='''Translator: "At least sets a lower ___." | bound | At least three includes three and larger counts in the supplied numerical comparison.
Reviewer: "At most sets an upper ___." | limit | At most three includes three and smaller counts, changing the relationship.
Translator: "The difference needs an explicit ___." | query | The translator should raise the discrepancy for authorized review rather than choose scope.
Reviewer: "Keep both original versions ___." | traceable | Preserving the versions lets reviewers identify the discrepancy and the authorized resolution.'''),
]
