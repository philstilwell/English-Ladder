"""Original radiography communication, with explicit professional scope."""
from books.medical_support import medical_unit as unit, source, TEACH_BACK, SCOPE

BOOK = dict(slug='x-ray-technicians', title='X-Ray and Radiography English',
    cover_label='ENGLISH FOR X-RAY TECHNICIANS', cover_title='X-Ray &\nRadiography', cover_size=38,
    tagline='Verify the request. Guide the patient. Close the handoff.',
    audience='For X-ray technicians, radiologic technologists, and radiographers working within their authorized scope.',
    roles='X-ray technicians, radiologic technologists, radiographers, imaging department staff',
    summary='Practical radiography English for identity checks, positioning, pregnancy screening, pediatric cooperation, portable imaging, image quality, results questions, and near-miss reporting.',
    map_intro='Eight imaging encounters practice verification, stepwise instructions, sensitive questions, child-friendly language, bedside coordination, technical explanations, scope boundaries, and accurate incident reporting.',
    notes_title='A clear instruction is part of a careful examination.',
    notes_intro='Radiography combines technical precision with short, consequential conversations. Patients need understandable instructions, an opportunity to report difficulty, and a clear distinction between acquiring images and interpreting them.',
    field_notes=[
        ('Verify before proceeding', 'An identity, examination, or laterality discrepancy requires the actual verification process. Do not resolve it by guessing from a schedule or silently changing a request.', '"The request says left, but you describe the right side. I need to verify that discrepancy."'),
        ('Make movement negotiable', 'Give one movement instruction at a time and check what the patient can do. Pain, mobility limitations, equipment, and consent may require an adapted approach.', '"Tell me before moving if that position is painful or difficult."'),
        ('Keep interpretation with the authorized clinician', 'Explain image acquisition and the reporting process within your role. A patient asking about a picture deserves a helpful handoff, not an improvised diagnosis.', '"I can explain the examination; the reporting clinician interprets the images."'),
        ('Preserve the record', 'Distinguish a technical limitation, a corrected record, and an incident. Use approved systems and escalation routes without deleting evidence or concealing an error.', '"I have paused and preserved the record while the discrepancy is reviewed."'),
    ], scope_note=SCOPE,
    sources=[TEACH_BACK,
        source('RadiologyInfo. Chest X-ray.', 'https://www.radiologyinfo.org/en/info/chestrad', 'Background for plain radiography, positioning, image acquisition, and interpretation responsibilities.'),
        source('ASRT. Practice Standards for Medical Imaging and Radiation Therapy.', 'https://www.asrt.org/main/standards-and-regulations/professional-practice/practice-standards-online', 'Professional context; actual duties depend on law, competence, authorization, and setting.'),
        source('ASRT. Position Statements.', 'https://www.asrt.org/main/standards-and-regulations/professional-practice/position-statements-online', 'Context for professional responsibilities, patient communication, image integrity, and appropriate escalation.')], units=[])

BOOK['units'].append(unit(
    title='Resolving a request discrepancy', scene='The request says left; the patient says right',
    skill='Pause an examination and verify conflicting information without suggesting an answer.',
    brief='Morgan arrives for a wrist X-ray. The request names the left wrist, but Morgan describes an injury to the right wrist. Radiographer Alex has not acquired any images. Alex verifies identity using the approved identifiers, records the discrepancy, and contacts the requesting team through the department process. This case does not authorize Alex to rewrite the request.',
    cast='Alex | Radiographer\nMorgan | Patient',
    culture=('Ask without leading', 'Invite the patient to state information rather than simply agree with a suggested name or side. Explain the pause as a verification step, not as blame.'),
    a='''Which side appears on the request? | Left | Right | Both | Neither | The written request names the left wrist in the supplied case.
What does Morgan describe? | A right-wrist injury | A left-ankle injury | A completed examination | A diagnosis from the image | Morgan describes the right wrist, which conflicts with the request.
What happens before acquisition? | Verification through the department process | Guessing the intended side | Silently editing the request | Imaging both sides automatically | The discrepancy must be resolved through the authorized process before acquisition.''',
    vocabulary='''laterality | The specified right or left side of an examination. | verify laterality
imaging request | Authorized request describing the intended imaging examination. | review the imaging request
patient identifier | Approved identifying detail used to verify a person's identity. | confirm patient identifiers
examination site | Anatomical location intended for the examination. | verify the examination site
requesting clinician | Clinician who initiated the imaging request. | contact the requesting clinician
clinical indication | Clinical question or reason supporting an examination. | clarify the clinical indication
requisition | Document or electronic order requesting a service. | reconcile the requisition
worklist | Electronic list of scheduled or requested imaging examinations. | review the worklist
accession number | Identifier assigned to a particular imaging examination. | verify the accession number
identity discrepancy | Conflict between identifying details or records. | resolve an identity discrepancy
side marker | Marker identifying anatomical side on a radiographic image. | verify the side marker
pre-examination check | Verification performed before carrying out the examination. | complete the pre-examination check
order clarification | Authorized clarification of an ambiguous or conflicting request. | obtain order clarification
acquisition | Process of obtaining the imaging data. | pause image acquisition
anatomical landmark | Identifiable body feature used to orient an examination. | identify an anatomical landmark
request amendment | Authorized documented change to an examination request. | record a request amendment
verification pause | Temporary stop while relevant information is checked. | explain a verification pause
resolved discrepancy | Conflict clarified through the appropriate documented process. | confirm a resolved discrepancy''',
    precision='The patient account identifies a conflict; it does not independently authorize a different examination. Verification and request amendment are different actions.',
    precision_extra='Use the approved identifiers and local procedure. An accession number identifies an examination, not a substitute for confirming the person.',
    phrases='''Invite the account | Please tell me which wrist was injured.
Identify the conflict | The request names the left side, while you describe the right.
Explain the pause | I need to clarify this before taking the images.
Avoid blame | I am checking the information, not asking you to resolve the paperwork.
Name the contact | I will contact the team that requested the examination.
Avoid leading | Please state your details rather than agreeing with my suggestion.
Keep the boundary | I cannot silently change the request on that basis.
Confirm the resolution | We will proceed once the discrepancy is appropriately resolved.''',
    notes='''While versus therefore | While can contrast two accounts; therefore would wrongly make the patient's account automatic authorization.
Before taking | Makes the verification step precede acquisition, rather than follow an avoidable exposure.
Names versus describes | Separates information in the request from the patient's own account.''',
    d='''Which question avoids leading? | Please tell me which wrist was injured. | It is your left wrist, correct? | You mean left, do you not? | Agree that the request is right. | The open factual question does not suggest the desired side to the patient.
What does an accession number identify? | A particular examination | The patient's preferred language | The reporting diagnosis | The painful side by itself | The accession number identifies the examination record, not every patient or clinical detail.
Which action exceeds the supplied authorization? | Silently changing the request | Explaining the pause | Contacting the requesting team | Recording the conflict | The case does not authorize an undocumented independent change to the requested examination.
Which wording preserves both sources? | The request says left; the patient reports right. | The request must be right. | The patient must be wrong. | Both sides are authorized. | Naming both sources preserves the conflict until the appropriate verification resolves it.''',
    dialogue='''Alex | Before we start, please state the identifying details our department uses and tell me which wrist was injured.
Morgan | My right wrist. The receptionist mentioned the left, so I wondered whether something had been entered incorrectly.
Alex | The [[imaging request::The imaging request is the authorized examination instruction and currently conflicts with the patient's reported side.]] does name the left wrist. I need to clarify that difference before taking any images.
Morgan | Can you just change it to right? That is definitely where I hurt myself yesterday.
Alex | Your account matters, but [[laterality::Laterality means the specified side and must be verified through the appropriate process rather than silently changed.]] needs verification through our process. I cannot silently rewrite the request.
Morgan | Does that mean you think I have given you the wrong information about my injury?
Alex | No. This [[verification pause::A verification pause is a temporary stop to resolve conflicting information before the examination proceeds.]] checks the information from both sources. It is not a criticism of your account.
Morgan | Thank you. Who can clarify what examination was actually intended when the request was made?
Alex | I will contact the [[requesting clinician::The requesting clinician initiated the examination and is an appropriate contact for clarifying its intended scope.]] or the authorized team following our department procedure.
Morgan | I have a number on my appointment message. Would that settle which wrist you should examine?
Alex | The [[accession number::An accession number identifies the examination record but cannot independently resolve the clinical side discrepancy.]] identifies the examination record. It does not resolve the side conflict on its own.
Morgan | I understand. You will still check that the record belongs to me before doing anything else?
Alex | Yes. We use the approved [[patient identifier::A patient identifier is an approved identifying detail used to verify the person rather than infer identity from the appointment alone.]] checks rather than relying only on an appointment number.
Morgan | What will you tell the team when you ask them to look at the request?
Alex | I will state the request's side, your account, and the relevant [[clinical indication::The clinical indication is the reason or question for imaging and helps the authorized team clarify the intended examination.]] without inventing a new reason for imaging.
Morgan | And if they need to change the order, will that change be recorded somewhere?
Alex | Any authorized [[request amendment::A request amendment is a documented authorized change, not an informal substitution made without the required process.]] must follow the proper process so the record remains clear.
Morgan | All right. I would rather have the correct examination than hurry past a mismatch.
Alex | Exactly. [[Acquisition::Acquisition is obtaining the images and is paused here until the relevant discrepancy has been appropriately resolved.]] has not started. I will explain the verified plan once the team responds.
Morgan | So we are waiting for a [[resolved discrepancy::A resolved discrepancy means the conflict has been appropriately clarified and documented before the intended examination proceeds.]], not assuming that either account can simply be ignored.''',
    rehearsal=['Read the corrected exchange, stressing left and right without blaming either source.', 'Swap roles. Repeat the verification and authorization distinction without adding an examination.'],
    transfer_title='An ankle request with a missing side', transfer_setup='An ankle request omits the side. Jo reports a left-ankle injury. No images have been acquired, and the authorized team is being contacted.',
    transfer='''Jo: "My injured ankle is the ___ one." | left | Jo reports a left-ankle injury in the supplied scenario.
Radiographer: "The request currently ___ the side." | omits | The missing laterality is the discrepancy requiring clarification before acquisition.
Jo: "The team will ___ the request." | clarify | The authorized team is being contacted to clarify the incomplete request.
Radiographer: "No images have been ___." | acquired | The scenario explicitly states that acquisition has not yet begun.'''))

BOOK['units'].append(unit(
    title='Adapting positioning instructions', scene='One movement at a time',
    skill='Give sequenced movement instructions and respond to a limitation without coercion.',
    brief='Casey cannot comfortably raise the left shoulder for the planned position. Radiographer Jamie stops the attempted movement and checks the limitation. An adapted examination requires the appropriate departmental approach and, where needed, clinical advice. Casey has not refused all imaging; Casey has said this particular movement hurts. No alternative projection is prescribed by the exercise.',
    cast='Jamie | Radiographer\nCasey | Patient',
    culture=('A limitation is useful information', 'Thank the patient for reporting pain. Avoid interpreting inability as unwillingness, and obtain agreement before offering physical assistance.'),
    a='''What is difficult? | Raising the left shoulder | Stating the name | Hearing all instructions | Attending any imaging | The case identifies one painful shoulder movement, not a general refusal.
What does Jamie do first? | Stops the attempted movement | Forces the position | Labels Casey uncooperative | Invents a new projection | Jamie stops the movement and checks the reported limitation.
What is not supplied? | An authorized alternative projection | Casey's reported pain | A positioning difficulty | A need to adapt communication | The exercise does not prescribe the technical alternative for the examination.''',
    vocabulary='''positioning | Arranging the patient's body for the intended image. | explain the positioning
projection | Image view defined by the direction of the X-ray beam. | clarify the requested projection
range of motion | Extent of movement available at a joint. | assess available range of motion
mobility limitation | Restriction affecting a person's movement. | accommodate a mobility limitation
weight bearing | Supporting body weight through a limb or joint. | clarify weight-bearing ability
transfer assistance | Help moving between surfaces or positions. | arrange transfer assistance
support aid | Equipment used to help maintain a suitable position. | select an approved support aid
upright position | Position with the upper body vertical. | explain an upright position
supine position | Position lying on the back. | describe the supine position
lateral position | Position lying on or oriented toward a side. | clarify the lateral position
rotation | Turning around a body or joint axis. | limit uncomfortable rotation
alignment | Relationship of body parts to the intended imaging geometry. | check patient alignment
immobilization | Restriction of movement using an appropriate method. | explain proposed immobilization
pain-limited movement | Movement restricted by the person's reported pain. | document pain-limited movement
physical assistance | Hands-on support provided with appropriate agreement and competence. | ask before physical assistance
breath-hold instruction | Direction to briefly suspend breathing for an image when appropriate. | rehearse a breath-hold instruction
adapted technique | Modified examination approach appropriate to the clinical and technical situation. | discuss an adapted technique
movement cue | Short instruction directing one specific movement. | give a clear movement cue''',
    precision='Cannot comfortably move is different from refuses imaging. Record the actual limitation and avoid labeling the patient uncooperative.',
    precision_extra='A language exercise cannot determine a safe transfer, immobilization method, or alternative projection. Follow the actual assessment and authorized technique.',
    phrases='''Give one step | Please turn slightly toward me, then stop.
Invite a limit | Tell me before moving if that is painful or difficult.
Stop clearly | Stop there; do not force that movement.
Clarify ability | Which part of that movement is difficult?
Ask before touch | May I help support your arm?
Acknowledge the report | Thank you for telling me about the pain.
Explain adaptation | I will check how we can adapt the examination appropriately.
Rehearse first | We can practice the instruction before acquiring the image.''',
    notes='''Cannot versus will not | Cannot describes a limitation; will not may imply refusal and should not replace the patient's actual account.
Then stop | Breaks a complex instruction into a bounded movement that can be checked.
May I help | Requests agreement before hands-on assistance rather than announcing it as inevitable.''',
    d='''Which record is most accurate? | Casey reports pain when raising the left shoulder. | Casey refuses every examination. | Casey is deliberately difficult. | Casey has normal movement. | The precise report describes the supplied movement limitation without inventing intent or examination findings.
Which instruction respects the limitation? | Stop there; do not force the movement. | Keep going despite the pain. | Ignore your shoulder. | The picture matters more than your report. | Stopping acknowledges the reported difficulty while the appropriate approach is reviewed.
What should precede hands-on help? | Appropriate agreement and assessment | An assumption of permission | A surprise movement | A guessed transfer method | Assistance requires appropriate agreement and competence, not an unexpected physical intervention.
What is a projection? | A view defined by beam direction | The patient's predicted diagnosis | A consent signature | A guaranteed alternative position | Projection names an imaging view and does not itself authorize a technical change.''',
    dialogue='''Jamie | I will explain one movement at a time. Please tell me before moving if a position is painful or difficult.
Casey | Raising this left shoulder hurts. I can turn a little, but I cannot lift the arm that high.
Jamie | Stop there. This is [[pain-limited movement::Pain-limited movement accurately records the reported reason for stopping rather than assuming refusal or poor cooperation.]], and we should not force the position just to follow the first instruction.
Casey | I do want the examination. I am worried you will think I am refusing to cooperate.
Jamie | I will record the actual [[mobility limitation::A mobility limitation describes restricted movement without assigning the patient a negative motive or a blanket refusal.]], not describe you as refusing every part of the examination.
Casey | Thank you. It is easier when I know exactly which movement you are asking me to try.
Jamie | I can give a shorter [[movement cue::A movement cue directs one specific action and allows the patient's response to be checked before another instruction.]] and pause between steps. We can check what is comfortable before proceeding.
Casey | Could you explain what the position is intended to show without asking me to force it?
Jamie | The requested [[projection::A projection is an imaging view defined by beam direction and its intended purpose should be distinguished from an improvised alternative.]] is a particular view. I will check the appropriate approach when that positioning is difficult.
Casey | Would a cushion or some support help, or does that need to be checked as well?
Jamie | Any [[support aid::A support aid helps maintain a position but must be appropriate to the actual examination and the person's needs.]] must be appropriate for this examination.
Casey | I would also like you to ask before moving my arm, because unexpected movement makes me tense.
Jamie | Of course. [[Physical assistance::Physical assistance is hands-on support and requires appropriate agreement, assessment, and competence rather than surprise movement.]] needs your agreement and a suitable assessment. May I help support it while you stay still?
Casey | Yes, supporting it is comfortable. Please do not lift it farther without checking with me first.
Jamie | Understood. I will keep your [[range of motion::Range of motion describes the movement available at the joint and the reported limitation must remain part of the positioning discussion.]] limitation clear when I discuss the examination with the team.
Casey | Does changing the way I sit automatically mean you can take a different view instead?
Jamie | No. An [[adapted technique::An adapted technique is an appropriate modification based on the actual clinical and technical situation, not an automatic substitution.]] must fit the clinical question and our authorized process, rather than be an improvised substitute.
Casey | Once that is settled, could we practice any breathing instruction before the image is taken?
Jamie | Yes, if a [[breath-hold instruction::A breath-hold instruction can be rehearsed when appropriate so the patient understands the sequence before acquisition.]] is appropriate, we can rehearse it and check that the wording is manageable for you.
Casey | Clear [[positioning::Positioning arranges the body for the intended image, and the instructions should respect the person's actual movement ability.]] instructions and a pause give me a chance to tell you what I can actually do.''',
    rehearsal=['Read the corrected exchange with a clear pause after each movement instruction.', 'Swap roles. Contrast a painful movement with refusal, and practice asking before assistance.'],
    transfer_title='A transfer needs assessment', transfer_setup='Drew says standing from the chair is difficult. The radiographer has not assessed transfer assistance and asks the appropriate team for help. Drew has not refused imaging.',
    transfer='''Drew: "Standing from this chair is ___." | difficult | Drew reports a specific difficulty with standing from the chair.
Radiographer: "The transfer needs ___." | assessment | The assistance required has not yet been assessed in this case.
Drew: "I have not ___ the examination." | refused | A movement limitation is not equivalent to refusing imaging.
Radiographer: "I will request appropriate ___." | assistance | The scenario calls for help from the appropriate team rather than an improvised transfer.'''))

BOOK['units'].append(unit(
    title='Asking sensitive screening questions', scene='A private answer before the examination',
    skill='Explain a pregnancy-screening question respectfully and preserve an uncertain answer.',
    brief='Rowan is asked a pregnancy-screening question under the department protocol and requests privacy from a companion. Rowan is unsure of the answer. Radiographer Taylor offers a private conversation and follows the appropriate review process. The uncertainty is not recorded as a negative answer. The exercise supplies neither an individualized radiation-risk estimate nor a decision to perform or cancel the examination.',
    cast='Taylor | Radiographer\nRowan | Patient',
    culture=('Explain why before asking', 'A personal question can feel intrusive when asked without context or in front of a companion. Offer appropriate privacy without making assumptions about identity, relationships, or reproductive history.'),
    a='''What does Rowan request? | Privacy from a companion | A diagnosis from the image | Automatic cancellation | An invented risk estimate | Rowan specifically asks to answer the screening question privately.
What answer is supplied? | Uncertainty | Confirmed pregnancy | A verified negative result | Refusal of all care | Rowan is unsure, and that uncertainty must remain visible.
What decision is not supplied? | Whether to perform or cancel the examination | A need for review | A privacy request | A screening question | The language case does not determine the clinical examination decision.''',
    vocabulary='''pregnancy screening | Process of checking relevant pregnancy information before an examination. | explain pregnancy screening
possible pregnancy | Pregnancy that has not been confirmed or excluded. | report possible pregnancy
screening uncertainty | Unresolved information from a screening question or process. | preserve screening uncertainty
private conversation | Discussion held away from people not authorized to hear it. | offer a private conversation
sensitive history | Personal information requiring respectful and appropriate handling. | obtain a sensitive history
ionizing radiation | Radiation capable of removing electrons from atoms. | explain ionizing radiation
radiation exposure | Exposure to radiation during an examination or other event. | discuss radiation exposure
justification | Assessment that an examination's expected benefit warrants its use. | review examination justification
optimization | Adjusting imaging practice to achieve its purpose with appropriate exposure. | explain optimization
benefit-risk discussion | Comparison of expected benefit and relevant possible harm. | arrange a benefit-risk discussion
radiologist review | Assessment by a physician specializing in medical imaging. | request radiologist review
examination protocol | Approved approach for a particular imaging examination. | follow the examination protocol
screening response | Recorded answer to a screening question. | document the screening response
exposure history | Account of relevant prior radiation exposure. | clarify the exposure history
reproductive history | Relevant history concerning pregnancy and reproduction. | ask about reproductive history
privacy preference | Person's stated wishes about who hears personal information. | respect a privacy preference
clinical urgency | Degree to which the clinical situation requires prompt action. | communicate clinical urgency
review outcome | Decision or findings following the appropriate assessment. | explain the review outcome''',
    precision='Unsure is not no. Screening information supports the appropriate review; it does not create a universal instruction to cancel or proceed.',
    precision_extra='Risk depends on the actual examination and circumstances. Do not promise zero risk or claim that every X-ray is forbidden during pregnancy.',
    phrases='''Give the reason | This question is part of our examination-screening process.
Offer privacy | Would you prefer to discuss this without your companion present?
Allow uncertainty | It is all right to say that you are unsure.
Record accurately | I will record uncertainty rather than a negative answer.
Avoid a blanket rule | The appropriate team needs to review the actual examination.
Explain the referral | I will arrange the relevant clinical discussion.
Protect the boundary | I cannot give an individualized risk estimate from this information alone.
Return with a plan | We will explain the reviewed plan before proceeding.''',
    notes='''Unsure versus no | Preserves unresolved information instead of forcing a binary answer.
Actual examination | Keeps the discussion specific rather than applying a rule to every imaging procedure.
Would you prefer | Offers a privacy choice without assuming who should be present.''',
    d='''Which entry matches Rowan's response? | Unsure | Negative | Confirmed positive | No screening required | Uncertainty is the supplied answer and must not be silently converted into a negative.
Which statement overpromises? | There is absolutely no risk in every case. | The team will review this examination. | We can speak privately. | I will preserve your answer. | A universal zero-risk statement is not supported by the individualized assessment.
What should guide the next step? | The actual protocol and clinical review | A blanket cancellation rule | The companion's guess | An invented exposure calculation | The relevant examination and clinical circumstances require the appropriate professional process.
Which phrase supports privacy? | We can discuss this without your companion present. | Your companion must answer for you. | Everyone needs to hear this. | I will announce the answer outside. | Offering a private conversation respects the patient's stated preference and sensitive information.''',
    dialogue='''Taylor | I need to ask a question required by our screening process. Would you prefer to discuss it privately?
Rowan | Yes. My companion does not know everything about my situation, and I would rather answer without them here.
Taylor | We can arrange a [[private conversation::A private conversation respects the request to answer without the companion.]]. I will explain why the question matters before asking for personal information.
Rowan | Thank you. I may not be able to give a definite answer about whether I could be pregnant.
Taylor | Please say that clearly. [[Screening uncertainty::Screening uncertainty must remain unresolved rather than being recorded as no.]] is important information; it should not be changed to no.
Rowan | Does being unsure automatically mean that every kind of X-ray has to be canceled?
Taylor | No blanket conclusion follows. The [[examination protocol::The examination protocol governs this procedure, not every imaging situation universally.]] and clinical circumstances guide the appropriate review.
Rowan | I would like someone to explain the possible benefit and risk of this particular examination.
Taylor | I can arrange a [[benefit-risk discussion::A benefit-risk discussion weighs this examination's expected benefit and possible harm.]] with the appropriate professional, without inventing an individual estimate myself.
Rowan | I have heard the word radiation, but I do not know what kind this examination uses.
Taylor | X-rays use [[ionizing radiation::Ionizing radiation describes the radiation type, not a personal risk estimate.]]. The team can explain what that means for the proposed examination and your circumstances.
Rowan | Will my uncertain answer still be visible when the person reviewing the examination reads the record?
Taylor | Yes. The [[screening response::The screening response records what the patient actually answered, including uncertainty, so the review is based on accurate information.]] must reflect what you said, not a more convenient definite answer.
Rowan | Could the reason the examination is needed also matter to that discussion?
Taylor | Yes. [[Justification::Justification considers whether the expected benefit warrants the examination in the actual clinical circumstances.]] concerns whether the expected benefit warrants the examination in its clinical context.
Rowan | And I would like my companion included only after we agree what can be discussed with them.
Taylor | I will respect that [[privacy preference::A privacy preference identifies the patient's wishes about who hears personal information and should be handled within the applicable rules.]] within the applicable rules and explain any relevant limits.
Rowan | Who will tell me what the review means for the next step?
Taylor | We will arrange the appropriate [[radiologist review::Radiologist review is assessment by the imaging physician when required by the relevant process, not a decision supplied by this language exercise.]] or other authorized clinical review, then explain the outcome and next step.
Rowan | That gives me a clear process without pretending the [[review outcome::The review outcome is the decision or findings after assessment and must not be presented as settled before that review occurs.]] has already been decided.''',
    rehearsal=['Read the corrected exchange. Keep unsure distinct from no throughout.', 'Swap roles. Explain privacy and review without supplying a risk estimate or examination decision.'],
    transfer_title='A companion asks for the answer', transfer_setup='A companion asks what Rowan said. Rowan has requested privacy and has not authorized sharing the answer. The clinical review remains pending.',
    transfer='''Companion: "Can you share the screening ___?" | answer | The companion asks for the content of the screening response.
Radiographer: "Sharing has not been ___." | authorized | Rowan has not authorized disclosure of the private answer.
Companion: "The review is still ___?" | pending | The clinical review has not yet reached an outcome.
Radiographer: "I need to respect the requested ___." | privacy | The scenario explicitly requires respecting Rowan's request for privacy.'''))

BOOK['units'].append(unit(
    title='Helping a child cooperate', scene='A rehearsal before the picture',
    skill='Use concrete language, bounded choices, and honest reassurance with a child.',
    brief='Eight-year-old Mina is anxious about a requested chest X-ray. Radiographer Lee explains the equipment and rehearses the relevant instruction before acquisition. Mina worries that the machine will touch her. Her caregiver is available, but any presence or assistance during exposure depends on the department safety process. The exercise does not prescribe restraint or a caregiver position.',
    cast='Lee | Radiographer\nMina | Child patient',
    culture=('Include the child directly', 'Speak to the child rather than only about the child. A choice about explanation or rehearsal is meaningful; do not offer a false choice about a decision that has not been assessed.'),
    a='''What worries Mina? | Whether the machine will touch her | A known diagnosis | A report already issued | A prescribed restraint | Mina asks about the equipment and whether it will touch her.
What happens before acquisition? | Explanation and rehearsal | A promise of no possible discomfort | Unapproved restraint | Automatic caregiver exposure | Lee explains the equipment and rehearses the instruction before acquisition.
What controls caregiver assistance? | The department safety process | A universal rule invented here | The child's guess | The appointment color | Presence or assistance during exposure follows the actual safety process.''',
    vocabulary='''age-appropriate explanation | Explanation adapted to the child's understanding and communication needs. | give an age-appropriate explanation
assent | Child's affirmative agreement appropriate to age and circumstances. | seek meaningful assent
caregiver permission | Authorization from an appropriate caregiver when required. | verify caregiver permission
child-life support | Specialist support helping children cope with healthcare experiences. | request child-life support
demonstration | Showing an action before asking someone to perform it. | offer a demonstration
practice run | Rehearsal before the actual procedure or acquisition. | complete a practice run
bounded choice | Limited genuine choice within the available safe options. | offer a bounded choice
sensory description | Explanation of what someone may see, hear, or feel. | provide a sensory description
distress cue | Sign suggesting anxiety, discomfort, or difficulty coping. | notice a distress cue
coping strategy | Method helping a person manage an uncomfortable experience. | agree on a coping strategy
caregiver presence | Caregiver being with the child during a relevant stage. | clarify caregiver presence
protective arrangement | Appropriate safety setup for people involved in an examination. | confirm protective arrangements
stillness | Absence of movement during the relevant acquisition interval. | explain brief stillness
exposure signal | Cue associated with the actual imaging exposure. | explain the exposure signal
reassurance | Supportive explanation that does not promise an unsupported outcome. | give honest reassurance
stop signal | Agreed cue for communicating a need to pause. | agree on a stop signal
cooperation | Participation supported by understanding and appropriate assistance. | support cooperation
preparation sequence | Ordered explanation and steps before the examination. | simplify the preparation sequence''',
    precision='Assent and caregiver permission are not interchangeable. Requirements depend on age, capacity, law, and setting; involve the child appropriately without inventing a legal rule.',
    precision_extra='Avoid promises such as nothing can hurt or your caregiver can always stand here. Explain the actual equipment and approved arrangements honestly.',
    phrases='''Address the child | Mina, I will explain what happens before we start.
Describe honestly | I can show you which part makes the picture.
Offer a real choice | Would you like me to explain first or demonstrate first?
Rehearse | We can practice that instruction before taking the picture.
Invite a question | Which part worries you most?
Bound the reassurance | I will tell you before we change position.
Explain caregiver arrangements | We need to check where your caregiver can safely be.
Agree on a pause | Let us agree how you can tell me you need a pause.''',
    notes='''First or first | Offers a choice about the order of explanation, not a false choice about clinical authorization.
Before we start | Gives the child a predictable sequence and time for questions.
Can safely be | Makes caregiver placement conditional on the actual safety arrangements.''',
    d='''Which choice is genuine here? | Explanation first or demonstration first | Any unassessed exposure position | A guaranteed normal result | Unlimited movement during acquisition | The available choice concerns preparation order, not technical safety or diagnostic outcomes.
Which reassurance is honest? | I will explain before we change position. | Nothing can ever feel uncomfortable. | Every result will be normal. | Your caregiver can stand anywhere. | Explaining the sequence is a commitment within the speaker's control rather than an unsupported guarantee.
What does a practice run do? | Rehearses an instruction before acquisition | Replaces all permission requirements | Establishes a diagnosis | Guarantees cooperation | Rehearsal supports understanding but does not settle consent, diagnosis, or every response.
Which terms require distinction? | Assent and caregiver permission | Picture and image in plain explanation | Pause and brief stop | Explain and clarify | Child assent and legally required caregiver permission serve different roles in the actual setting.''',
    dialogue='''Lee | Mina, I will explain the equipment before we begin. Which part of having the picture taken worries you most?
Mina | The big machine looks as though it might move toward me. I do not know what it does.
Lee | Let me give a [[sensory description::A sensory description explains what the child may see, hear, or feel rather than relying on technical labels alone.]] of this equipment, then show you the part used for the picture.
Mina | Could you show me first? It is easier when I can see what you mean.
Lee | Yes. That is a useful [[bounded choice::A bounded choice offers a real limited option, here the order of explanation and demonstration, within the available safe process.]]: demonstration first, then we can talk through the instructions.
Mina | Do I have to understand every long word before we can do the examination?
Lee | No. An [[age-appropriate explanation::An age-appropriate explanation adapts the language to the child's understanding without withholding necessary information or speaking only to adults.]] uses words that make sense to you. You can ask me to explain anything again.
Mina | I heard someone say stay still. I am worried that I will forget what to do.
Lee | We can have a [[practice run::A practice run rehearses the instruction before the actual image is acquired so uncertainty can be addressed beforehand.]] before the picture, so you know the sequence rather than guessing during it.
Mina | Will you tell me when the practice finishes and when the real picture begins?
Lee | Yes. I will explain the [[exposure signal::The exposure signal is the cue associated with the actual acquisition and should be distinguished from a rehearsal.]] used here and distinguish practice from the actual picture.
Mina | Can my caregiver stay beside me the whole time? I feel calmer when I can see them.
Lee | We need to check the [[protective arrangement::A protective arrangement is the approved safety setup and determines where another person can appropriately be during the examination.]] before promising where anyone can stand during exposure.
Mina | All right. Could you also tell me before asking me to move into a different position?
Lee | Certainly. A clear [[preparation sequence::A preparation sequence tells the child what comes next and reduces surprise without making promises about every sensation or outcome.]] helps you know what happens next. I will explain before changing the instruction.
Mina | What should I do if I get frightened or do not understand the next step?
Lee | Let us agree on a [[stop signal::A stop signal gives the child a clear way to communicate a need for a pause and should be explained within the actual procedure.]] so you can tell me. We will explain how to use it here.
Mina | I would like to practice with you before the picture. That feels less surprising.
Lee | Your [[assent::Assent is the child's affirmative agreement appropriate to the circumstances and does not replace any legally required caregiver permission.]] matters. We also follow the required permission and safety process with your caregiver.
Mina | I understand. The [[demonstration::A demonstration shows the action before the child is asked to perform it and makes the instruction more concrete.]] first, then a practice, and I can tell you when I need something explained again.''',
    rehearsal=['Read the corrected exchange, using a warm but precise voice for the instructions.', 'Swap roles. Practice the real preparation choice without promising a result or caregiver position.'],
    transfer_title='The instruction was too long', transfer_setup='Noah forgets a three-part instruction during practice. The radiographer breaks it into one step at a time. No image has yet been acquired.',
    transfer='''Noah: "I forgot the three-part ___." | instruction | Noah reports difficulty remembering the instruction during the practice.
Radiographer: "We can use one ___ at a time." | step | The supplied adaptation is a single step at a time.
Noah: "This is still ___." | practice | The scenario states that acquisition has not yet begun.
Radiographer: "No image has been ___." | taken | The rehearsal occurs before the actual image is acquired.'''))

BOOK['units'].append(unit(
    title='Coordinating portable imaging', scene='The bedside team stays connected',
    skill='Coordinate equipment, patient movement, and responsibilities before a bedside examination.',
    brief='Radiographer Sam arrives for a portable chest examination. Nurse Priya identifies attached lines and monitoring equipment. Sam asks for the appropriate bedside team to coordinate any movement or equipment management. No line is disconnected, no device setting is changed, and no examination is performed until the actual preparation and safety checks are complete.',
    cast='Sam | Radiographer\nPriya | Bedside nurse',
    culture=('State the dependency directly', 'A polite request can still be explicit: identify the preparation needed and who is authorized to provide it. Do not treat clinical equipment as furniture.'),
    a='''What examination is requested? | A portable chest examination | An independent line adjustment | A device-setting change | A completed diagnosis | The brief specifies a portable chest examination at the bedside.
Who identifies attached equipment? | Priya | A visitor | An absent interpreter | The exercise author | Priya is the bedside nurse identifying lines and monitoring equipment.
What has not happened? | A line disconnection | A preparation discussion | A request for coordination | Arrival at the bedside | The case explicitly states that no line has been disconnected.''',
    vocabulary='''portable radiography | Radiographic imaging performed with mobile equipment at the patient's location. | coordinate portable radiography
bedside examination | Examination performed where the patient is receiving bedside care. | prepare a bedside examination
mobile X-ray unit | Movable equipment used to acquire radiographs outside a fixed room. | position the mobile X-ray unit
detector placement | Positioning the image receptor for the intended examination. | coordinate detector placement
attached line | Tube or connection linked to the patient's care. | identify attached lines
monitoring equipment | Devices used to observe relevant physiological information. | protect monitoring equipment
oxygen delivery device | Equipment providing prescribed oxygen support. | identify the oxygen delivery device
bedside coordination | Joint planning of activity around the patient's immediate care. | request bedside coordination
equipment clearance | Available space for positioning and moving equipment. | check equipment clearance
infection precaution | Measure intended to reduce transmission of infection. | follow infection precautions
isolation status | Applicable infection-control designation for the patient or area. | verify isolation status
cleaning protocol | Approved process for decontaminating equipment or surfaces. | follow the cleaning protocol
patient support | Assistance needed to maintain a suitable and safe position. | arrange patient support
line management | Authorized handling and protection of clinical tubing or connections. | coordinate line management
team readiness | Confirmation that required people and preparations are in place. | confirm team readiness
equipment adjustment | Change to a device's position or settings within authorized practice. | request authorized equipment adjustment
handoff acknowledgment | Confirmation that a transfer of information has been received. | obtain handoff acknowledgment
bedside constraint | Limitation affecting an examination at the patient's location. | communicate bedside constraints''',
    precision='Recognizing an attached line does not authorize disconnecting or adjusting it. Identify the responsible professional and coordinate the actual preparation.',
    precision_extra='Portable does not mean informal. Identity, examination, infection-control, movement, and exposure checks still follow the department process.',
    phrases='''Identify the request | I am here for the requested portable chest examination.
Ask about constraints | What attached equipment affects positioning?
Name the dependency | I need the appropriate team to coordinate movement first.
Protect connections | I will not disconnect that line or change its settings.
Clarify responsibility | Who is authorized to manage this device?
Check preparation | Please confirm when the bedside preparation is complete.
State a limitation | The available space limits where the unit can be positioned.
Close the handoff | Please acknowledge the preparation plan before we proceed.''',
    notes='''Need before | Makes preparation a prerequisite rather than an optional courtesy.
Manage versus move | Clinical equipment may require authorized management, not merely physical relocation.
Please confirm when | Requests a clear readiness signal instead of assuming silence means agreement.''',
    d='''Which request identifies a dependency? | I need authorized line management before movement. | I will remove anything in the way. | Portable imaging needs no checks. | Silence means ready. | The statement names the required preparation and does not assume authority to perform it.
What does portable describe? | Equipment and examination location | Reduced professional responsibility | Permission to alter devices | A diagnostic conclusion | Portable describes how imaging reaches the patient, not a waiver of safeguards.
Which action is unsupported? | Disconnecting an attached line independently | Asking who manages the line | Checking isolation status | Coordinating detector placement | No independent disconnection is authorized in the supplied case.
What confirms readiness? | Explicit acknowledgment from the relevant team | An unanswered request | The radiographer's arrival alone | A clear floor alone | Readiness requires the actual preparations and team acknowledgment, not a single convenient cue.''',
    dialogue='''Sam | I am here for the requested portable chest examination. Before positioning, can we review the bedside constraints together?
Priya | Yes. There are attached lines and monitoring devices, and movement needs coordination with the appropriate bedside staff.
Sam | This [[bedside coordination::Bedside coordination prepares movement and equipment management with the relevant staff.]] is important. I will not treat the connections as objects I can simply move aside.
Priya | Thank you. I can identify them and confirm who is authorized to manage each device.
Sam | Please include the [[oxygen delivery device::An oxygen delivery device requires appropriately authorized handling; it is not furniture.]] in that review. I will not disconnect it or change any setting.
Priya | Understood. We also need to confirm the precautions currently applying to this patient and room.
Sam | I will check the [[isolation status::Isolation status identifies the actual infection-control requirements, not an assumed precaution.]] and follow the required preparation for the equipment and examination.
Priya | Space is limited on the far side of the bed. Does that affect where your unit can go?
Sam | Yes. We need sufficient [[equipment clearance::Equipment clearance means the space required for appropriate positioning and movement.]] without interfering with care or assuming that a device can be relocated.
Priya | I will ask the appropriate colleague to help coordinate the movement and protect the connections.
Sam | That will support [[detector placement::Detector placement may require coordinated patient support and protection of attached equipment.]]. We should agree on the sequence before placing anything or moving the patient.
Priya | The patient also needs support to maintain the position. We have not yet assessed the exact assistance.
Sam | Then [[patient support::Patient support is the assistance required for the position and must be assessed rather than assumed from the imaging request.]] remains an outstanding preparation. I will not describe the bedside as ready yet.
Priya | I will confirm the assistance and line responsibilities through our actual clinical process.
Sam | Please name who will handle [[line management::Line management involves authorized protection and handling of clinical tubing or connections rather than independent adjustment by anyone present.]] so that nobody assumes someone else has accepted that responsibility.
Priya | Agreed. I will give you an explicit update when the required people and preparations are in place.
Sam | That confirms [[team readiness::Team readiness means the required staff and preparations are actually in place, not merely that the radiographer has arrived.]], rather than treating an unanswered request as permission to begin.
Priya | Afterward, the equipment also needs the appropriate cleaning before it leaves the area.
Sam | Yes. I will follow the [[cleaning protocol::The cleaning protocol is the approved decontamination process appropriate to the equipment and infection-control requirements.]] and communicate any unresolved issue through the department process.
Priya | We have a clear [[handoff acknowledgment::Handoff acknowledgment confirms receipt of the preparation plan and responsibilities instead of leaving them as an unconfirmed message.]]: preparation first, explicit readiness, then the examination under the actual safety process.''',
    rehearsal=['Read the corrected bedside exchange, emphasizing the preparation dependencies.', 'Swap roles. Name the responsible team without assigning yourself an unauthorized equipment task.'],
    transfer_title='Readiness is not yet confirmed', transfer_setup='The nurse has requested transfer assistance, but the assisting colleague has not arrived. The radiographer waits for the actual readiness confirmation.',
    transfer='''Nurse: "Transfer assistance has been ___." | requested | A request has been made but is not proof that assistance is present.
Radiographer: "The colleague has not yet ___." | arrived | The scenario explicitly says the assisting colleague has not arrived.
Nurse: "Readiness is not yet ___." | confirmed | The required assistance remains outstanding, so readiness is not established.
Radiographer: "I will wait for the actual ___." | acknowledgment | Explicit confirmation is required before treating the preparation as complete.'''))

BOOK['units'].append(unit(
    title='Explaining a technical limitation', scene='A repeat is a reviewed decision',
    skill='Describe image quality precisely and distinguish technical review from diagnosis.',
    brief='Radiographer Ari identifies motion affecting a chest image and asks senior radiographer Devon to review technical adequacy. The case does not supply a diagnostic interpretation or authorize an automatic repeat. The team will assess whether the image answers the clinical question and whether any additional acquisition is justified under the actual process.',
    cast='Ari | Radiographer\nDevon | Senior radiographer',
    culture=('Describe the limitation, not the blame', 'Use observable technical language. A patient may move because of pain, breathlessness, anxiety, or an unclear instruction; do not label the person difficult.'),
    a='''What limitation is identified? | Motion affecting the image | A confirmed disease | An incorrect diagnosis | A completed repeat | The supplied technical concern is motion affecting the chest image.
Who reviews technical adequacy? | Devon | The patient's employer | A visitor | An automated language answer | Devon is the senior radiographer reviewing the technical concern.
What is not authorized automatically? | A repeat exposure | A review request | Describing motion | Preserving the image | The case requires assessment rather than an automatic additional acquisition.''',
    vocabulary='''motion artifact | Image distortion caused by movement during acquisition. | identify motion artifact
technical adequacy | Fitness of an image's technical features for its intended purpose. | review technical adequacy
diagnostic adequacy | Whether available images sufficiently address the clinical question. | assess diagnostic adequacy
repeat exposure | Additional radiation exposure to acquire another image. | justify a repeat exposure
collimation | Restriction of the X-ray beam to the intended area. | assess collimation
exposure index | System indicator related to detector exposure under specified conditions. | interpret the exposure index
detector exposure | Radiation reaching the image receptor during acquisition. | review detector exposure
image noise | Unwanted variation affecting the visual signal in an image. | assess image noise
image contrast | Difference in appearance between image regions or structures. | assess image contrast
spatial resolution | Ability to distinguish nearby structures in an image. | describe spatial resolution
anatomical coverage | Extent of the required anatomy included in an image. | check anatomical coverage
positioning error | Departure from the intended patient or anatomical position. | describe a positioning error
exposure factor | Technical parameter affecting an imaging exposure. | review exposure factors
image processing | Computational treatment of acquired image data. | distinguish image processing
reject analysis | Review of rejected images to identify patterns and improvement opportunities. | conduct reject analysis
quality assurance | Organized activities checking and improving process quality. | support quality assurance
technical review | Assessment of relevant acquisition and image-quality features. | request a technical review
additional acquisition | Further collection of image data after an initial acquisition. | assess additional acquisition''',
    precision='A technical limitation is not a diagnosis. Exposure index is not a direct patient-dose reading, and a displayed image should not be judged from brightness alone.',
    precision_extra='Retain images and follow the actual review and repeat process. Do not hide a rejected image or automatically repeat solely because a picture looks imperfect.',
    phrases='''Describe the issue | There is visible motion affecting this image.
Request review | Could you review whether the image answers the clinical question?
Avoid blame | I will document the limitation without labeling the patient.
Avoid automatic repetition | A repeat needs the appropriate assessment and justification.
Separate measures | The exposure index is not a direct patient-dose reading.
Preserve the record | I will retain the image within the approved record.
Clarify the purpose | We need adequate information, not merely a prettier picture.
Support improvement | Let us identify what can improve the next instruction.''',
    notes='''Affecting versus invalidating | A limitation may affect an image without automatically making the entire examination unusable.
Whether | Frames adequacy as a question for review rather than a conclusion already reached.
Additional versus replacement | An additional exposure has consequences; it is not merely an edit to an existing picture.''',
    d='''Which statement is precise? | Motion affects this image and needs review. | The patient ruined the study. | Every imperfect image must be repeated. | Motion proves disease. | Describing the image's motion limitation identifies the review need without blame or an unsupported diagnosis.
What is not a direct patient-dose reading? | Exposure index | A documented patient-dose quantity | An appropriately measured dose metric | A verified dose report | Exposure index concerns detector exposure under specified conditions rather than directly reporting individual patient dose.
Why review before repeating? | To assess adequacy and justify any additional acquisition | To hide the first image | To guarantee a normal diagnosis | To make every image identical | Review connects the additional exposure decision to clinical purpose and appropriate justification.
Which practice preserves integrity? | Retaining the image through the approved process | Deleting evidence of motion | Reusing an old image as new | Changing the record invisibly | Preserving the image and approved record supports review and accurate quality improvement.''',
    dialogue='''Ari | This chest image has visible motion. Could you review its technical adequacy before we decide whether anything further is needed?
Devon | Yes. Describe the limitation specifically, and keep the original image available in the approved record.
Ari | The [[motion artifact::Motion artifact describes movement-related distortion, without assigning blame or a diagnosis.]] affects part of the image. I have not concluded that the whole examination is unusable.
Devon | Good. We need to assess the actual clinical question, not simply aim for a more attractive picture.
Ari | So [[diagnostic adequacy::Diagnostic adequacy concerns the clinical question, not a visually perfect picture.]] is different from making every image look technically perfect.
Devon | Exactly. The relevant professional review determines what information is sufficient and what limitation matters.
Ari | I also checked the [[anatomical coverage::Anatomical coverage identifies whether the required body area is included.]], rather than relying only on the overall brightness of the displayed image.
Devon | That is useful. Display appearance and processing do not independently establish appropriate exposure or adequacy.
Ari | The system shows an [[exposure index::Exposure index concerns detector exposure, not a direct patient-dose measurement.]]. I should not describe that as a direct reading of the patient's dose.
Devon | Correct. Interpret the indicator according to the actual system and context, without substituting it for another quantity.
Ari | Does identifying the motion authorize me to acquire another image immediately?
Devon | No. A [[repeat exposure::A repeat exposure needs appropriate review and justification, not automatic repetition.]] needs appropriate assessment and justification under our process.
Ari | I will also avoid recording the patient as difficult. We have not established why the movement occurred.
Devon | Yes. [[Quality assurance::Quality assurance checks and improves the process and should use accurate observations rather than unsupported judgments about the patient.]] should examine the process, including whether our instructions were clear and manageable.
Ari | If another acquisition is authorized, the instruction may need to be explained or rehearsed differently.
Devon | That belongs in the [[technical review::Technical review assesses acquisition and image-quality features and can identify improvements without turning them into a diagnosis.]], alongside the actual clinical and technical constraints.
Ari | The original image will remain available even if the process classifies it as unsuitable.
Devon | Correct. [[Reject analysis::Reject analysis reviews rejected images for improvement and depends on an accurate retained record rather than concealed evidence.]] depends on an accurate record, not deleting evidence of a problem.
Ari | I will document the limitation and the review outcome before treating an [[additional acquisition::An additional acquisition collects further image data and must be based on the appropriate reviewed decision rather than assumed permission.]] as agreed.
Devon | That keeps [[technical adequacy::Technical adequacy concerns the image's technical fitness for purpose and must be distinguished from a diagnostic interpretation.]], diagnostic interpretation, and the decision about another exposure distinct.''',
    rehearsal=['Read the corrected exchange. Distinguish the limitation from the decision about repeating.', 'Swap roles. Explain exposure index without giving a dose estimate or selecting exposure settings.'],
    transfer_title='A missing area needs review', transfer_setup='A required anatomical area is not fully included. The image is preserved. The appropriate reviewer has not yet decided whether additional acquisition is needed.',
    transfer='''Radiographer: "The anatomical coverage is ___." | incomplete | The required area is not fully included in the supplied image.
Reviewer: "The image must remain ___." | available | The scenario explicitly preserves the image for appropriate review.
Radiographer: "Additional acquisition is not yet ___." | decided | The reviewer has not yet made the additional-acquisition decision.
Reviewer: "We need the appropriate ___." | assessment | The decision requires the actual assessment rather than an automatic repeat.'''))

BOOK['units'].append(unit(
    title='Responding to requests for results', scene='Explain the process without interpreting the image',
    skill='Set a helpful professional boundary and give a concrete route for results.',
    brief='After an examination, patient Jules asks radiographer Ren whether a visible mark means cancer. Ren has not issued a diagnostic interpretation. The reporting clinician will interpret the images, and the referring service will explain the result through its actual process. No reporting deadline is supplied. Ren checks how Jules can contact the service rather than promising a result time.',
    cast='Ren | Radiographer\nJules | Patient',
    culture=('A boundary should include a next step', 'A bare I cannot say may feel dismissive. Acknowledge the concern, explain your role, and identify the person or service responsible for interpretation and communication.'),
    a='''What does Jules ask about? | Whether a mark means cancer | A confirmed cancer diagnosis | A signed report | A guaranteed deadline | Jules asks an anxious question but no diagnostic interpretation is supplied.
Who interprets the images? | The reporting clinician | The language learner independently | An employer | The appointment system | The reporting clinician is responsible for the diagnostic interpretation in this case.
What is not supplied? | A reporting deadline | Jules's concern | A referring service | A completed examination | No deadline is given, so Ren must not invent a result time.''',
    vocabulary='''image interpretation | Professional assessment of images for clinical meaning. | arrange image interpretation
reporting clinician | Authorized professional responsible for the imaging interpretation. | identify the reporting clinician
radiology report | Recorded interpretation of an imaging examination. | review the radiology report
preliminary report | Initial interpretation that may be updated after further review. | distinguish a preliminary report
final report | Completed authorized report under the relevant reporting process. | communicate the final report
incidental finding | Finding outside the main reason for the examination. | explain an incidental finding
comparison images | Earlier images used to assess relevant differences. | obtain comparison images
referring service | Clinical service that requested or coordinates the examination. | contact the referring service
result communication | Process of explaining a result to the appropriate recipient. | confirm result communication
report turnaround | Time between the relevant examination stage and report availability. | verify report turnaround
critical result | Finding requiring urgent communication through the relevant clinical pathway. | escalate a critical result
report addendum | Additional or corrected information appended to a report. | review a report addendum
clinical correlation | Interpretation of a finding alongside other clinical information. | explain clinical correlation
patient portal | Secure system allowing a patient to access relevant health information. | explain patient-portal access
result inquiry | Request for information about an examination result. | handle a result inquiry
scope of practice | Duties a professional is trained and authorized to perform. | respect scope of practice
follow-up contact | Named person or service for subsequent communication. | provide a follow-up contact
unverified impression | Initial belief not established by the appropriate interpretation. | avoid an unverified impression''',
    precision='A visible feature is not an established diagnosis. Acquiring the image does not automatically authorize diagnostic interpretation.',
    precision_extra='Report availability and explanation to the patient are separate steps. Do not promise a deadline or assume portal release completes clinical communication.',
    phrases='''Acknowledge the concern | I can hear that the mark is worrying you.
Clarify your role | My role here is to acquire the images.
Name the interpreter | The reporting clinician will interpret the examination.
Avoid speculation | I cannot identify that as a diagnosis from this conversation.
Give a route | Let us confirm how the referring service will explain the result.
Limit timing | I need to verify the reporting arrangements rather than guess.
Separate access and explanation | Seeing a report online is not the same as having it explained.
Offer a concrete contact | I can help identify the appropriate contact for your question.''',
    notes='''Will interpret versus has confirmed | Distinguishes a pending professional process from a completed finding.
Cannot identify as | Sets a precise boundary without dismissing the person's concern.
Verify rather than guess | Avoids turning an uncertain administrative timeframe into a promise.''',
    d='''Which response is most helpful? | I cannot interpret that, but I can confirm the reporting route. | I cannot say; goodbye. | It is definitely harmless. | It must be cancer. | The response combines an accurate professional boundary with a concrete next step.
Which distinction matters? | Report access and clinical explanation | The screen color and the diagnosis | A mark and a confirmed cancer as identical | Arrival and report completion as identical | A patient may access a report before its meaning has been explained in context.
What timing claim is unsupported? | The result will definitely be ready tomorrow. | I will check the arrangements. | No deadline is supplied here. | The service can clarify its process. | The case provides no reporting deadline, so tomorrow would be an invented promise.
What does clinical correlation mean? | Interpreting a finding with other clinical information | Matching the report's colors | Deleting an uncertain image | Guaranteeing a benign finding | Clinical correlation places the image finding within the wider clinical evidence.''',
    dialogue='''Jules | I saw a mark on the screen. Does that mean cancer, or can you tell me it is harmless?
Ren | I can hear that it worries you. My role here is to acquire images, not give their diagnostic interpretation.
Jules | But you see these pictures every day. Surely you have an idea of what that mark means.
Ren | An [[unverified impression::An unverified impression is not a reliable diagnosis or reassurance.]] would not give you a reliable answer. I do not want to mislead you in either direction.
Jules | Then who can answer the question properly, and how will the information get back to me?
Ren | The [[reporting clinician::The reporting clinician interprets images; acquiring them is a different responsibility.]] interprets the examination, and we should confirm how your referring service communicates the result.
Jules | Is a report the same thing as someone discussing what it means for my situation?
Ren | No. [[Result communication::Result communication includes explanation, not merely a report existing in the system.]] includes explaining it in context, not merely creating a document in the system.
Jules | I sometimes see reports on my phone before anyone has spoken to me about them.
Ren | A [[patient portal::Patient-portal access does not establish that the report has been clinically explained.]] can provide access, but seeing the words is not the same as discussing their meaning with the appropriate clinician.
Jules | If it says correlate clinically, does that mean the picture did not work?
Ren | [[Clinical correlation::Clinical correlation interprets imaging alongside the patient's other relevant clinical information.]] means considering the finding with other clinical information. It is not automatically a statement that acquisition failed.
Jules | Could an earlier examination help the person who is preparing the report?
Ren | [[Comparison images::Comparison images are earlier examinations used to assess differences and may provide context for the reporting clinician.]] may provide useful context. The team follows its process for obtaining and reviewing them.
Jules | Can you promise that someone will call tomorrow? Waiting without a contact is the hardest part.
Ren | I need to verify the [[report turnaround::Report turnaround is the actual time to report availability and cannot be invented as a guaranteed deadline in this case.]] arrangements rather than guess. No definite reporting time has been established in this conversation.
Jules | I understand the limit, but I would still appreciate knowing whom to contact with the question.
Ren | Let us identify the [[follow-up contact::A follow-up contact gives the patient a concrete person or service for subsequent communication rather than a vague instruction to wait.]] and the referring service's route for discussing your result.
Jules | That is more useful than a guess. I can ask about the report through that route.
Ren | Yes. Respecting [[scope of practice::Scope of practice defines the duties a professional is authorized and competent to perform, including the boundary around diagnostic interpretation.]] still allows a helpful handoff for your [[result inquiry::A result inquiry is a request about examination findings and deserves an appropriate communication route rather than unsupported speculation.]].''',
    rehearsal=['Read the corrected result discussion, pairing every boundary with a useful next step.', 'Swap roles. Respond to the request for certainty without supplying a diagnosis or a deadline.'],
    transfer_title='An online report has appeared', transfer_setup='Pat can see a report online but has not discussed it with the referring clinician. No interpretation or follow-up decision is supplied.',
    transfer='''Pat: "The report is visible in the ___." | portal | The report is available through the online patient portal.
Radiographer: "Access is not the same as clinical ___." | explanation | Seeing the report does not mean its significance has been discussed.
Pat: "I need the appropriate ___." | contact | The next communication step is identifying the relevant clinician or service.
Radiographer: "No follow-up decision is supplied ___." | here | The exercise provides access information but no clinical follow-up decision.'''))

BOOK['units'].append(unit(
    title='Reporting a labeling near miss', scene='Correct the record without hiding the history',
    skill='Describe a discrepancy factually and request an authorized correction with an audit trail.',
    brief='Radiographer Kim notices that an image label may not match the verified examination details. Kim stops further release and contacts supervisor Noor through the department process. The original record is preserved. The team has not established how the mismatch arose or whether any incorrect information reached another service. This is a communication case, not an instruction for editing clinical images.',
    cast='Kim | Radiographer\nNoor | Supervisor',
    culture=('A correction should remain traceable', 'Report what is known promptly, identify what remains unverified, and preserve the record. Do not turn a suspected mismatch into a proven cause or quietly erase its history.'),
    a='''What does Kim notice? | A possible label mismatch | A proven cause | A confirmed external disclosure | A normal diagnostic report | The case supplies a possible mismatch without establishing cause or downstream impact.
What happens to the original record? | It is preserved | It is secretly deleted | It is replaced without history | It is reused for another patient | Preserving the original record supports the authorized review and correction process.
What remains unestablished? | How the mismatch arose | That Kim contacted Noor | That release was paused | That a concern exists | The cause and any downstream impact have not yet been established.''',
    vocabulary='''label discrepancy | Conflict between an image label and verified examination information. | report a label discrepancy
near miss | Event caught before the relevant potential harm occurs. | report a potential near miss
incident report | Formal record of an event through the applicable reporting system. | submit an incident report
audit trail | Traceable history of actions and changes in a record. | preserve the audit trail
record integrity | Accuracy and trustworthiness of a maintained record. | protect record integrity
data correction | Authorized amendment of inaccurate recorded information. | request a data correction
release hold | Temporary prevention of further distribution pending review. | apply an authorized release hold
downstream recipient | Person or system receiving information later in the workflow. | identify downstream recipients
root cause | Underlying factor established through appropriate investigation. | investigate the root cause
contributing factor | Circumstance that may have influenced an event. | identify contributing factors
event chronology | Ordered account of what happened and when. | document the event chronology
verified detail | Information checked against an appropriate source. | distinguish verified details
unconfirmed impact | Possible consequence not yet established by review. | state unconfirmed impact
notification route | Approved path for informing the relevant people. | follow the notification route
correction authorization | Approval required to amend a relevant record. | obtain correction authorization
preserved original | Original information retained through the approved process. | maintain the preserved original
system reconciliation | Process of aligning related records across relevant systems. | coordinate system reconciliation
learning review | Structured review intended to improve future practice. | support a learning review''',
    precision='A possible mismatch is not an established root cause. A near miss can be confirmed only when the relevant facts support that classification.',
    precision_extra='Follow the real incident, correction, and notification processes. Never conceal evidence, overwrite history informally, or assume that fixing one display corrects every linked system.',
    phrases='''Lead with the discrepancy | The label may not match the verified examination details.
State the containment | Further release is paused through our process.
Preserve uncertainty | The cause and downstream impact are not yet established.
Keep the original | I have preserved the original record.
Request authorization | Please confirm the approved correction route.
Separate action and investigation | The immediate containment does not settle the root cause.
Check linked records | We need to verify which systems and recipients are affected.
Close factually | I will record the confirmed actions and outstanding questions.''',
    notes='''May not match | Describes a suspected discrepancy without pretending the investigation is complete.
Not yet established | Preserves uncertainty about cause and impact without minimizing the event.
Corrected versus concealed | A traceable authorized amendment differs from an invisible alteration.''',
    d='''Which opening is factual? | The label may not match verified details. | I know who caused this without review. | Nothing happened anywhere. | I erased it, so it no longer matters. | The wording reports the observed concern without inventing cause or impact.
What must remain traceable? | The original record and authorized changes | Only the final screenshot | A guessed explanation | An informal memory | An audit trail preserves the history needed to understand and verify a correction.
Which conclusion is premature? | No downstream recipient was affected. | Impact is not established. | The supervisor was contacted. | The original is preserved. | The case explicitly leaves downstream impact unverified, so absence of impact cannot be asserted.
What is system reconciliation for? | Aligning related records across affected systems | Hiding the first version | Replacing investigation with a guess | Automatically changing every record | Reconciliation checks related records so a local correction is not mistaken for complete resolution.''',
    dialogue='''Kim | I have noticed a possible mismatch between the image label and the verified examination details. Further release is paused.
Noor | Thank you for escalating it. Preserve the original record and state exactly what you have verified so far.
Kim | The [[label discrepancy::A label discrepancy is a conflict between the image label and verified examination information and should be described before its cause is assumed.]] is the concern. I have not established how it arose or whether another service received it.
Noor | Good. Keep the event description separate from any assumption about who or what caused it.
Kim | I have applied the authorized [[release hold::A release hold temporarily prevents further distribution while the relevant concern is reviewed through the approved process.]] through our process, rather than making an undocumented change to the image.
Noor | We need the approved correction route and an account of what happened in order.
Kim | I will give an [[event chronology::An event chronology records the sequence and timing of known actions, which helps review without turning guesses into facts.]] using verified times and actions, marking anything I have not confirmed.
Noor | Include the point at which you noticed the issue and the people contacted afterward.
Kim | The [[preserved original::A preserved original retains the initial information through the approved process so the review and any correction remain traceable.]] remains available. I have not deleted it or substituted an earlier image.
Noor | That protects the record while the appropriate people determine the correction and notification requirements.
Kim | Should I call this a near miss now, or wait until the impact is known?
Noor | Use the appropriate classification after review. [[Unconfirmed impact::Unconfirmed impact means possible consequences have not yet been established and cannot be described as definitely absent.]] is not the same as proof that no one received incorrect information.
Kim | We need to identify every relevant [[downstream recipient::A downstream recipient is a later person or system receiving the information and may require appropriate notification or correction.]] through the authorized investigation rather than assume the local screen is the only record.
Noor | Correct. Fixing one display does not prove that all related records are aligned.
Kim | I will request [[correction authorization::Correction authorization is the required approval for amending the relevant record rather than an informal independent alteration.]] and keep the actions visible in the approved system.
Noor | We also need the [[audit trail::An audit trail preserves the history of actions and changes so a correction can be understood and verified later.]], including what was changed, by whom, and through which process.
Kim | Once the immediate issue is contained, the investigation can examine contributing factors without guessing at blame.
Noor | Yes. Establishing a [[root cause::A root cause is an underlying factor supported by investigation, not an assumption made from the first visible discrepancy.]] requires investigation; it is not settled by the first report.
Kim | I will complete the required report and flag the unresolved system and recipient questions.
Noor | That supports [[record integrity::Record integrity is the accuracy and trustworthiness of the maintained record, including traceable corrections and unresolved facts.]] and a useful learning review while the actual correction process continues.''',
    rehearsal=['Read the corrected incident exchange, separating verified actions from unresolved cause and impact.', 'Swap roles. Practice requesting a traceable correction without specifying an unauthorized editing method.'],
    transfer_title='One linked system is still unchecked', transfer_setup='An authorized correction is complete in the local record. A linked system has not yet been checked. The original and change history are retained.',
    transfer='''Reporter: "The local correction is ___." | complete | The supplied facts confirm completion only in the local record.
Supervisor: "The linked system remains ___." | unchecked | The scenario explicitly leaves the linked system unverified.
Reporter: "The original and history are ___." | retained | The record and change history remain available for traceability.
Supervisor: "Full reconciliation is not yet ___." | confirmed | One unchecked linked system prevents claiming that reconciliation is complete.'''))
