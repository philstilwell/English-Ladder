"""Additional pediatric encounters involving transitions, schools, and feeding history."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Preparing for an adult-care transition',
    skill='Build a verified transition plan without treating a referral as completed transfer.',
    setup='Seventeen-year-old Kai and pediatrician Dr Reed prepare for a future move to adult services. The receiving service has not confirmed an appointment. Kai wants to understand the condition summary, medicine list, contact routes, and changing communication responsibilities. No universal age rule or legal conclusion is supplied.',
    cast='Kai | Adolescent patient\nDr Reed | Pediatrician',
    dialogue='''Kai | I heard that I will move to an adult clinic, but I do not know what I need to understand before that happens.
Dr Reed | Let us prepare a [[transition plan::A transition plan organizes preparation and responsibilities for moving between services rather than treating the referral alone as a completed transfer.]] with clear steps rather than assume that sending a referral completes the change.
Kai | I want to explain my health history myself, but I do not remember every technical term.
Dr Reed | A verified [[condition summary::A condition summary presents the relevant diagnosis and care history in a usable form and must be checked rather than reconstructed from uncertain memory.]] can help you describe the important facts without memorizing the whole record.
Kai | Could we review which medicines are current instead of copying an old list into the new form?
Dr Reed | Yes. We should verify the actual list and instructions with the responsible team before presenting them as current.
Kai | I also want to know whom to contact if the adult clinic has not offered an appointment yet.
Dr Reed | The [[receiving service::The receiving service is the team expected to accept the next stage of care and its actual acceptance and appointment arrangements need confirmation.]] has not confirmed an appointment, so we need a named route for checking progress.
Kai | Does that mean the pediatric team stops answering questions as soon as the referral is sent?
Dr Reed | We need explicit coverage and responsibility arrangements. They should not be assumed from the date a letter was sent.
Kai | Some messages currently go to my caregiver. Will that automatically change on a particular birthday?
Dr Reed | The actual [[communication arrangements::Communication arrangements specify contacts, permissions, and access routes and must be checked under the relevant service and legal rules rather than a universal age assumption.]] and applicable rules need review; we should not invent a universal age rule.
Kai | I would like help learning to ask questions, but I do not want my caregiver excluded without discussion.
Dr Reed | We can discuss the support you want and the appropriate permissions while keeping you involved in your care.
Kai | How do we know whether I am ready to manage a particular task independently?
Dr Reed | A [[readiness discussion::A readiness discussion explores the person's understanding, practical skills, and support needs rather than assuming independence from age alone.]] looks at understanding and practical support needs, not just a birthday or a form.
Kai | Could we check the emergency and routine contact routes separately? I sometimes confuse them.
Dr Reed | Yes. The actual urgent-care instructions remain distinct from routine appointment and prescription questions.
Kai | Then we can confirm each handoff step instead of assuming the new clinic already knows everything.
Dr Reed | A [[confirmed transfer::A confirmed transfer establishes that the receiving service has accepted the relevant care responsibilities, rather than merely receiving a referral request.]] requires accepted responsibility and clear arrangements, not simply a sent letter.''',
    transfer_title='A referral is received but no visit is booked',
    transfer_setup="The adult service confirms receipt of Kai's referral, but no appointment is booked. The teams clarify interim responsibility under their actual process.",
    transfer='''Kai: "The referral has been ___." | received | The adult service confirms receipt of the referral request.
Pediatrician: "A visit is not yet ___." | booked | Receipt does not establish a scheduled appointment in this scenario.
Kai: "Interim responsibility needs to be ___." | clarified | The teams must identify who is responsible before the transfer is complete.
Pediatrician: "The transfer is not simply a sent ___." | letter | A sent referral document alone does not establish a completed care transfer.'''),
scenario(title='A school report with limited sharing permission',
    skill='Clarify the purpose, audience, and authorized scope of a school-related medical report.',
    setup='Caregiver Mina asks Dr Cole for information supporting a school accommodation. The school asks for the entire medical record, but the family has authorized discussion of the relevant functional needs only. The clinician will verify applicable requirements and permissions. No legal entitlement or educational placement decision is supplied.',
    cast='Mina | Caregiver\nDr Cole | Pediatrician',
    dialogue='''Mina | The school wants information for an accommodation, but its form asks for the entire medical record. That feels broader than we discussed.
Dr Cole | Let us clarify the purpose, actual requirements, and authorization before sending information beyond the relevant needs.
Mina | We wanted them to understand the difficulty with a particular school activity, not every past diagnosis.
Dr Cole | The [[functional need::A functional need describes the relevant practical difficulty or support requirement and is distinct from disclosing an entire clinical history.]] should be described using supported facts and the appropriate clinical assessment.
Mina | Does agreeing to a school conversation automatically authorize every teacher to see all the records?
Dr Cole | No. We need to check the [[information-sharing permission::Information-sharing permission defines what may be disclosed, for what purpose, and to whom under the applicable rules and authorization.]] and applicable rules for the actual information and recipients.
Mina | I would like the report to explain the need without guaranteeing an educational decision you do not control.
Dr Cole | That is an important distinction. A clinical report can inform a process without deciding the school's response or legal obligations.
Mina | Could the school ask for clarification if the wording is too general to be useful?
Dr Cole | Yes, through the appropriate [[designated contact::A designated contact is the named person responsible for the relevant communication and helps avoid uncontrolled distribution or contradictory messages.]] and authorized route, rather than distributing sensitive details to everyone.
Mina | We should also involve my child appropriately, because the proposed support affects the school day.
Dr Cole | Agreed. We can explain the discussion in an age-appropriate way and hear the child's perspective.
Mina | If a requested statement has not been assessed, should we include it because the form has a box for it?
Dr Cole | No. An [[unsupported statement::An unsupported statement lacks the relevant evidential basis and should not be added merely because an administrative form requests it.]] should not become part of the report simply to complete a form.
Mina | Then the report can say what is established and what remains outside the current assessment.
Dr Cole | Exactly. The [[report scope::Report scope identifies the subjects and limits covered by the actual assessment and authorization rather than implying a comprehensive opinion on every school issue.]] should remain clear, with relevant limitations stated.
Mina | I would like to know which version was sent and to which person, so we can follow up consistently.
Dr Cole | We can use the approved documentation process to record the recipient, purpose, and relevant version.
Mina | That gives the school useful information without treating a limited request as permission for everything.
Dr Cole | A [[purpose-limited disclosure::A purpose-limited disclosure shares information appropriate to the authorized purpose rather than releasing unrelated history without justification.]] supports that aim while following the actual rules and clinical responsibilities.''',
    transfer_title='A new recipient requests the same report',
    transfer_setup='A staff member not named in the original sharing permission requests the report. The clinician checks authorization before sending it. The report has not been sent to that person.',
    transfer='''Caregiver: "That recipient was not ___." | named | The new staff member was not included in the original permission.
Clinician: "We need to check ___." | authorization | Sharing with the new recipient requires verification under the applicable process.
Caregiver: "The report has not been ___ to them." | sent | The scenario states that no disclosure to the new recipient has occurred.
Clinician: "The original permission was not ___." | unlimited | A limited information-sharing permission does not automatically cover every later recipient.'''),
scenario(title='Reconciling two feeding accounts',
    skill='Clarify amounts, timing, and sources without treating different caregiver accounts as deception.',
    setup="Pediatrician Dr Noor discusses an infant's feeding history with caregiver Alex. Another caregiver describes a different feeding pattern. The accounts cover different times of day and may use different units. No feeding prescription, growth diagnosis, or safe waiting interval is supplied.",
    cast='Alex | Caregiver\nDr Noor | Pediatrician',
    dialogue='''Alex | My partner's feeding account sounds different from mine. I am worried that the difference makes one of us look unreliable.
Dr Noor | Let us clarify the times, units, and what each person observed before deciding that the accounts conflict.
Alex | I usually describe the daytime feeds, while my partner is remembering the night.
Dr Noor | That [[observation window::An observation window is the period covered by a report and must be clarified before two accounts are treated as describing the same events.]] matters. Different periods may produce different but accurate descriptions.
Alex | I also said ounces once and milliliters another time, which may have made the conversation confusing.
Dr Noor | We should identify the [[measurement unit::A measurement unit specifies how an amount is expressed and must be clear before quantities from different reports are compared.]] explicitly rather than compare numbers that represent different quantities.
Alex | Sometimes I describe how much was offered, but my partner reports what seemed to be taken.
Dr Noor | [[Offered volume::Offered volume is the amount made available and is not automatically the amount actually taken during the feed.]] and the amount actually taken are not automatically the same.
Alex | That distinction is useful. We should not present every number as a precise measurement if it was only an estimate.
Dr Noor | Correct. Mark an [[estimated amount::An estimated amount is an approximation and should remain distinguishable from a measured quantity in the feeding history.]] as an estimate, and explain how it was obtained when relevant.
Alex | Would a note about a difficult feed matter even if it does not fit neatly into a volume total?
Dr Noor | Describe the actual difficulty and associated observations. A history is more than adding numbers together.
Alex | I do not want this discussion to become a new feeding plan before you have assessed the actual situation.
Dr Noor | It should not. We are clarifying the account; any clinical recommendation needs the appropriate assessment and current information.
Alex | Could we summarize daytime and nighttime separately and then check the account with both caregivers?
Dr Noor | A [[source-specific summary::A source-specific summary keeps each caregiver's period and observations identifiable rather than blending them into an apparently precise but unsupported total.]] helps preserve who reported each detail.
Alex | If we notice a concerning change, we should follow the actual clinical instructions rather than wait to perfect a diary.
Dr Noor | Yes. Necessary assessment must not be delayed to complete a language task or produce a flawless record.
Alex | Then the different accounts can be clarified without accusing either of us or inventing an average.
Dr Noor | That is [[history reconciliation::History reconciliation aligns accounts by checking sources, timing, units, and uncertainty rather than choosing a winner or manufacturing a combined number.]]: check the sources and meanings before drawing a clinical conclusion.''',
    transfer_title='Offered and taken were confused',
    transfer_setup='One caregiver reports the amount offered, while another reports the amount taken. The units are the same, but the quantities describe different things. No intake total is calculated.',
    transfer='''Caregiver: "My figure describes what was ___." | offered | One report concerns the amount made available during feeding.
Clinician: "The other describes what was ___." | taken | The second report concerns the amount actually taken rather than offered.
Caregiver: "The units are the ___." | same | The scenario states that the units match even though the quantities differ.
Clinician: "No combined total has been ___." | calculated | The exercise does not combine the different quantities into an intake total.'''),
]
