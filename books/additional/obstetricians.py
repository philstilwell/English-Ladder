"""Additional obstetric encounters with distinct decisions and communication needs."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='A sensitive consultation with language support',
    skill='Arrange qualified interpretation and private discussion without assigning authority to a companion.',
    setup='Patient Noor asks Dr Ellis for qualified interpretation and private time without a companion before discussing sensitive maternity information. The actual interpreter is arranged through the service. This dialogue concerns preferences, privacy, and preparation; it supplies no clinical decision or jurisdiction-specific rule.',
    cast='Noor | Patient\nDr Ellis | Obstetrician',
    dialogue='''Noor | I would like an interpreter, but I do not want my companion to interpret the personal questions for me.
Dr Ellis | We can arrange [[qualified language support::Qualified language support provides trained interpretation for accurate participation and is distinct from assuming a companion should translate sensitive information.]] through the service and discuss the appropriate privacy arrangements.
Noor | My companion speaks more English, but that does not mean I want every detail shared with them.
Dr Ellis | Correct. Language ability does not create [[disclosure permission::Disclosure permission concerns authorization to share specified information and does not follow automatically from a companion's language ability.]] or decision-making authority.
Noor | Could I have some time alone first, before deciding what I want discussed with the companion present?
Dr Ellis | We can arrange an appropriate private conversation and explain any relevant privacy limits in this setting.
Noor | I would also like the interpreter to use the language variety I understand best.
Dr Ellis | We should confirm your [[language preference::Language preference identifies the language or variety the patient understands best and should be checked rather than inferred from nationality or a companion.]] rather than infer it from your name or country.
Noor | When the interpreter arrives, will you still speak to me directly?
Dr Ellis | Yes. I will address you, use manageable segments, and allow the interpretation to finish before adding another question.
Noor | If I do not understand a medical term, I want to be able to ask without feeling that I am delaying everything.
Dr Ellis | A [[clarification request::A clarification request asks for an unclear message to be explained and supports informed participation rather than being treated as unreasonable delay.]] is useful. We should explain the meaning, not ask you to agree to words you do not understand.
Noor | I may want my companion involved later, once I know what information is being discussed.
Dr Ellis | We can revisit that choice and specify the appropriate sharing rather than assume today's preference is unlimited or permanent.
Noor | Does the interpreter make a decision for me if I cannot express the answer fluently in English?
Dr Ellis | No. The interpreter supports communication. Your [[decision-making role::The patient's decision-making role remains distinct from the interpreter's communication role and must not be transferred merely because language support is needed.]] is not transferred because you need language support.
Noor | Could we check the contact method too? The telephone number in the record is shared.
Dr Ellis | We should verify the actual privacy of that route before sending sensitive information or promising confidentiality.
Noor | That helps me understand what will happen before I discuss the personal details.
Dr Ellis | A clear [[communication agreement::A communication agreement records the relevant preferences and arrangements for language, privacy, support, and contact without replacing the actual clinical consent process.]] can record the relevant preferences while we follow the actual clinical and privacy processes.''',
    transfer_title='The contact number is shared',
    transfer_setup='The listed telephone number is shared with a companion. The patient requests a different contact route, which the service has not yet verified.',
    transfer='''Patient: "The listed number is ___." | shared | The listed telephone is used by the patient and a companion.
Clinician: "You have requested a different ___." | route | The patient asks for another way to receive communication.
Patient: "That route is not yet ___." | verified | The service has not yet confirmed that the requested route is available and appropriate.
Clinician: "We will check before sending sensitive ___." | information | The contact arrangement must be verified before sensitive material is sent.'''),
scenario(title='Discussing postpartum contraception preferences',
    skill='Explore priorities and explain that suitability needs an individualized review without imposing a method.',
    setup='Patient Alex asks Dr Vale about contraception after birth. Alex wants to discuss reversibility, bleeding concerns, feeding, convenience, and future pregnancy preferences. The clinician explains that medical eligibility, timing, and available methods require the actual individual assessment. No method, prescription, or eligibility rule is selected.',
    cast='Alex | Postpartum patient\nDr Vale | Obstetrician',
    dialogue='''Alex | I want to discuss contraception, but I do not want a method selected before you know what matters to me.
Dr Vale | Let us start with your priorities and the actual clinical assessment, not assume one option fits everyone.
Alex | I may want another pregnancy later, but I do not want to decide on an exact date today.
Dr Vale | We can discuss [[reproductive preferences::Reproductive preferences describe the person's wishes about future pregnancy and should be elicited without pressure to commit to a fixed timetable.]] without pressuring you to choose a timetable you have not decided.
Alex | I also want to know whether a method can be stopped if my wishes or circumstances change.
Dr Vale | [[Reversibility::Reversibility concerns whether and how a method's contraceptive effect can be ended and needs explanation for the actual option being discussed.]] is an important comparison, with the actual process and limitations explained for each relevant option.
Alex | Bleeding changes would matter to me because a previous experience was difficult.
Dr Vale | We should include your [[bleeding concern::A bleeding concern identifies an effect important to the patient's choice and should be discussed using the actual method information rather than dismissed.]] in the discussion rather than dismiss it as a minor detail.
Alex | Does feeding my baby automatically mean every method has the same suitability and timing?
Dr Vale | No. [[Medical eligibility::Medical eligibility assesses whether a method is appropriate for the person's actual clinical circumstances and cannot be reduced to a universal rule from one detail.]] and timing require the individual assessment and current applicable guidance.
Alex | I need something practical, but I do not want convenience to be the only factor considered.
Dr Vale | We can compare the actual options across the features that matter to you, including how they are used and accessed.
Alex | If a family member prefers a particular method, does that decide what I should receive?
Dr Vale | Your [[voluntary choice::Voluntary choice belongs to the informed patient and should not be replaced by pressure from family or a clinician's preference.]] remains central. Support from others should not become pressure to accept a method.
Alex | I would like benefits, limitations, and possible effects explained in ordinary language.
Dr Vale | That is appropriate. We should also explain what the method does not address, using its actual information.
Alex | Can we document what I want to discuss without treating it as consent to a procedure?
Dr Vale | Yes. A [[preference discussion::A preference discussion explores priorities and information needs and is not itself consent to a procedure or a prescription.]] is not the same as consent to an intervention or a prescription.
Alex | Then I can compare the relevant options after the clinical assessment instead of agreeing to a method I do not understand.
Dr Vale | Exactly. We will explain the actual choices and next step without inventing an eligibility rule or deciding for you.''',
    transfer_title='A preference is recorded, no method chosen',
    transfer_setup='The patient says reversibility matters and asks about possible bleeding changes. No method has been selected or prescribed.',
    transfer='''Patient: "___ matters to me." | Reversibility | The patient identifies reversibility as an important preference.
Clinician: "You also asked about ___ changes." | bleeding | Possible bleeding changes are the second stated information need.
Patient: "A method has not been ___." | selected | The discussion has not reached a method choice.
Clinician: "Nothing has been ___ in this scenario." | prescribed | No prescription is supplied or authorized by this language exercise.'''),
scenario(title='An uncertain ultrasound finding',
    skill='Explain an unresolved finding and the purpose of specialist review without converting uncertainty into a diagnosis.',
    setup='Patient Rowan receives an ultrasound report recommending specialist review of an uncertain finding. Dr Kim explains that the wording does not establish a diagnosis or guarantee that nothing is wrong. The actual report and clinical context will be reviewed. No finding measurements, prognosis, or procedure choice are supplied.',
    cast='Rowan | Pregnant patient\nDr Kim | Obstetrician',
    dialogue='''Rowan | The ultrasound report recommends another review. Does that mean a serious diagnosis has already been confirmed?
Dr Kim | The wording describes an [[uncertain finding::An uncertain finding is an observation whose significance is not yet established and should not be converted into a confirmed diagnosis.]], not a confirmed diagnosis. We should review the actual report and context carefully.
Rowan | I also do not want to be told that it definitely means nothing when the report asks for more assessment.
Dr Kim | That would be an unsupported guarantee. We need to explain what is known and what remains unresolved.
Rowan | What is the purpose of seeing a specialist rather than simply repeating the same reassurance?
Dr Kim | A [[specialist review::A specialist review examines the relevant finding and context with appropriate expertise and does not itself predetermine the conclusion.]] can clarify the question and appropriate next steps without predetermining the conclusion.
Rowan | Is the report's recommendation the same as an appointment being booked?
Dr Kim | No. We need to distinguish the recommendation, the referral, and an actual confirmed appointment.
Rowan | I would like the specialist to have the original images and not only a sentence copied into a letter.
Dr Kim | The relevant [[source images::Source images are the original examination images needed for review and are distinct from a shortened description copied into another document.]] and report should be available through the authorized transfer process.
Rowan | If a measurement is uncertain, should I compare it with a number I found from another pregnancy?
Dr Kim | A [[measurement limitation::A measurement limitation affects what a particular value can establish and requires the actual examination context rather than an unrelated comparison.]] needs the actual context; an unrelated number may not answer your question.
Rowan | I want to understand what the next assessment might clarify and what it may still leave uncertain.
Dr Kim | We should explain that explicitly, including any relevant options once the actual clinical review identifies them.
Rowan | Could I include my chosen support person when the result is discussed?
Dr Kim | Yes, with the appropriate permission. We can also arrange language support if needed for a clear explanation.
Rowan | Please do not treat my questions as agreement to a particular test before it has been explained.
Dr Kim | Questions support understanding. Any [[further-test decision::A further-test decision requires the actual information and appropriate informed discussion rather than being inferred from a request for clarification.]] needs its own appropriate discussion and authorization.
Rowan | Then we should confirm the referral status and who will explain the specialist's findings afterward.
Dr Kim | Correct. [[Result follow-up::Result follow-up assigns the route and responsibility for explaining the reviewed findings rather than ending the process when a referral is sent.]] should be explicit, with uncertainty preserved until the actual assessment supports a conclusion.''',
    transfer_title='The referral is sent but images are missing',
    transfer_setup='The specialist service has received the referral letter but not the source images. The appointment is not confirmed. The finding remains uncertain.',
    transfer='''Patient: "The source images are ___." | missing | The specialist service has not yet received the original examination images.
Clinician: "The referral letter has been ___." | received | Receipt is confirmed for the letter, not the complete review material.
Patient: "The appointment is not ___." | confirmed | No actual scheduled appointment has been confirmed in the scenario.
Clinician: "The finding remains ___." | uncertain | The incomplete transfer does not establish a diagnostic conclusion.'''),
]
