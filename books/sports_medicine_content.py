"""Original sports-medicine English: history, rehabilitation, evidence, and team communication."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='sports-medicine', title='Sports Medicine English', category='Health & life sciences',
    balanced_answer_columns=True,
    cover_label='ENGLISH FOR SPORTS MEDICINE PROFESSIONALS', cover_title='Sports Medicine', cover_size=33,
    tagline='Describe the movement. Clarify the next step.',
    audience='For sports physicians, physiotherapists, athletic trainers, and rehabilitation professionals working within their authorized roles.',
    roles='sports physicians, physical therapists, physiotherapists, athletic trainers, rehabilitation clinicians',
    summary='Sports medicine English for injury histories, examinations, rehabilitation plans, concussion communication, training load, imaging, return-to-sport decisions, and team confidentiality.',
    map_intro='Eight encounters practice mechanism-of-injury questions, examination explanations, rehabilitation read-backs, concussion communication, training-load comparisons, imaging limits, return criteria, and information sharing.',
    notes_title='Participation is not the same as clearance.',
    notes_intro='Sports medicine conversations connect symptoms and performance with clinical assessment, rehabilitation, and pressure to compete. Accurate English names the activity, evidence, restriction, and responsible decision-maker without turning a hopeful timetable into permission.',
    field_notes=[
        ('Describe before labeling', 'Clarify contact, movement, timing, and symptoms before adopting the athlete\'s informal diagnosis. A pop, a twist, or a feeling of instability is information to assess, not a complete diagnosis.', '"When you say it gave way, what actually happened during the movement?"'),
        ('Separate instruction from progression', 'A current rehabilitation plan does not automatically authorize the next activity. Read back the actual instruction and clarify changes with the responsible clinician.', '"This is the current plan; progression has not been approved in this update."'),
        ('Make the activity specific', 'Training, practice, contact, competition, and performance are not interchangeable. A person may participate in one approved activity without being cleared for every sporting demand.', '"The note allows the specified activity, not unrestricted competition."'),
        ('Protect the athlete\'s voice', 'Performance pressure does not remove privacy, consent, or clinical responsibility. Explain what can be shared, with whom, and for what purpose under the actual rules.', '"We can communicate authorized participation limits without forwarding the full clinical record."'),
    ], scope_note=FICTION + 'This is professional English practice, not medical advice, clinical training, an exercise prescription, or clearance to play. Follow actual emergency procedures, qualified clinical assessment, current evidence, local law, and sport-specific rules. Do not diagnose an injury, calculate a dose, select treatment, or advance rehabilitation from an exercise. Concussion and return-to-sport decisions require the appropriate healthcare professional. Protect athlete information and clarify the authority of each role.',
    sources=[
        source('AAOS OrthoInfo. Sprains, Strains, and Other Soft-Tissue Injuries.', 'https://www.orthoinfo.org/diseases--conditions/sprains-strains-and-other-soft-tissue-injuries/', 'Background for distinguishing tissue terminology and reported injury mechanisms; not a treatment plan.'),
        source('CDC HEADS UP. Returning to Sports.', 'https://www.cdc.gov/heads-up/guidelines/returning-to-sports.html', 'Supports the need for healthcare approval and supervision in concussion return-to-sport communication; the book does not reproduce a progression protocol.'),
        source('AAOS OrthoInfo. Recovery and Rehabilitation.', 'https://www.orthoinfo.org/recovery', 'Context for rehabilitation terminology and the need for instructions appropriate to the actual assessed injury.'),
        source('US Anti-Doping Agency. Therapeutic Use Exemptions.', 'https://www.usada.org/testing/tue/', 'Context for distinguishing an exemption request from approval under the actual anti-doping process.')], units=[])

BOOK['units'].append(unit(
    title='Clarifying an injury mechanism', scene='A twist, not a collision',
    skill='Elicit movement and symptom details without turning an athlete\'s description into an unconfirmed diagnosis.',
    brief='Football player Luca reports left-knee discomfort after planting the left foot and turning during practice. No other player made contact. Luca says the knee gave way but cannot explain whether that meant pain, buckling, or a fall. Dr Arun is taking the history; no examination, scan result, or diagnosis is supplied. The task is accurate history language, not deciding whether the injury is safe to ignore.',
    cast='Dr Arun | Sports physician\nLuca | Athlete',
    culture=('The athlete\'s words need room', 'An everyday phrase such as gave way may have several meanings. Ask for the actual experience before substituting a clinical label.'),
    a='''Which mechanism is reported? | Planting the left foot and turning without contact | A direct collision to the right knee | A fall from height | A confirmed ligament rupture | The brief specifies a left-foot plant and turn without another player's contact.
Which phrase needs clarification? | Gave way | Left foot | During practice | No player contact | Gave way could describe different experiences and has not been clarified in the history.
What is not yet supplied? | A confirmed diagnosis | A reported movement | The side involved | The practice setting | The case contains a symptom history but no examination, imaging, or diagnosis.''',
    vocabulary='''mechanism of injury | Movement or event associated with the reported injury. | clarify the mechanism of injury
non-contact injury | Injury associated with an event without direct contact from another person or object. | describe a non-contact injury
pivot | Turn made around a planted or supporting foot. | describe a pivot
weight-bearing | Supporting body weight through a limb. | clarify weight-bearing ability
joint instability | Sense or finding that a joint does not maintain expected stability. | distinguish reported joint instability
buckling | Sudden giving way during support or movement. | describe an episode of buckling
locking | Reported or assessed inability to move a joint through an expected range. | clarify reported locking
swelling | Enlargement associated with fluid or tissue change. | describe the onset of swelling
effusion | Fluid accumulation within a joint or body space. | assess a joint effusion
ligament | Connective tissue linking bones across a joint. | explain ligament anatomy
tendon | Tissue connecting muscle to bone. | distinguish a tendon from a ligament
meniscus | Fibrocartilage structure in the knee contributing to load distribution and stability. | explain the meniscus
sprain | Injury involving a ligament. | distinguish a sprain
strain | Injury involving muscle or tendon. | distinguish a strain
symptom onset | Time or sequence in which symptoms began. | establish symptom onset
aggravating factor | Activity or circumstance that worsens symptoms. | identify an aggravating factor
relieving factor | Activity or circumstance associated with reduced symptoms. | identify a relieving factor
prior injury | Earlier injury relevant to the current history. | clarify a prior injury''',
    precision='A non-contact pivot describes a mechanism, not a confirmed ligament or meniscal injury. Gave way needs clarification and must not be recorded as an examination finding.',
    precision_extra='Symptoms, assessed function, and structural diagnosis answer different questions. Missing examination and imaging information must not become a normal result or reassurance.',
    phrases='''Locate the event | Which foot was on the ground when you turned?
Clarify contact | Did anyone or anything make contact with you?
Unpack the phrase | When you say it gave way, what did you feel or see?
Separate sequence | Did the discomfort begin before, during, or after the turn?
Ask about function | What happened when you tried to support weight afterward?
Preserve uncertainty | That describes the event; it does not confirm the injured structure.
Check the side | I am confirming that you mean the left knee.
Avoid a shortcut | We should not replace your description with a diagnosis yet.''',
    notes='''Felt versus found | Felt attributes an experience to the athlete; found implies an assessment finding. Keep the source explicit.
During versus after | These words locate onset in the sequence and should not be used interchangeably.
No contact | No contact describes the mechanism and does not mean no injury or no need for assessment.''',
    d='''Which opening question resolves the key ambiguity? | What happened when you say the knee gave way? | Which ligament definitely ruptured? | Why did you keep playing after a diagnosis? | So your examination was normal? | The question clarifies the athlete's own phrase without assuming a diagnosis or examination result.
Which summary preserves the reported mechanism? | Left foot planted; turn without player contact | Right knee struck by another player | Confirmed meniscal tear on imaging | No injury because there was no contact | Only the movement-based summary matches the supplied movement, side, and absence of contact.
Which distinction is anatomically appropriate? | A sprain involves a ligament; a strain involves muscle or tendon | A sprain and strain always name the same tissue | A tendon connects two bones across every joint | A meniscus is a muscle | The terms identify different tissue categories without diagnosing this athlete's injury.
Which claim exceeds the case? | The ligament is definitely torn | The athlete reports discomfort | The event occurred at practice | The left foot was planted | No structural diagnosis is supplied, so a definite tear would add unsupported information.''',
    dialogue='''Dr Arun | Tell me what happened just before the knee discomfort started, including where your foot was on the ground.
Luca | My left foot was planted, and I turned. The [[mechanism of injury::The mechanism of injury describes the event and movement, not a confirmed structural diagnosis.]] was not a tackle; nobody made contact with me.
Dr Arun | I will record that distinction. When you said it gave way, what actually happened during the movement?
Luca | I am not sure whether [[buckling::Buckling describes a giving-way movement and should not be assumed when the athlete has not clarified what occurred.]] is the right word. I felt something unexpected and stopped, but I did not fall.
Dr Arun | We can keep your own description while clarifying it. Did the discomfort begin during the turn or afterward?
Luca | During the [[pivot::A pivot is a turn around a planted or supporting foot, matching the movement described by the athlete.]], as far as I remember. I cannot separate the exact moment any more precisely than that.
Dr Arun | That uncertainty is useful to preserve. What happened when you tried to put weight through the leg afterward?
Luca | I can describe my [[weight-bearing::Weight-bearing concerns supporting body weight through the limb, which is a functional detail rather than a diagnosis.]] experience, but I do not want my answer treated as proof of what structure is injured.
Dr Arun | It will be part of the history, not a substitute for the actual assessment. Did you notice any change in size?
Luca | I noticed some [[swelling::Swelling describes an observed or reported increase in size; it does not by itself identify the injured tissue.]] later, but I cannot say whether it began immediately because I was concentrating on the discomfort.
Dr Arun | We should distinguish that report from what is found on examination. Has anything similar happened before?
Luca | There was a [[prior injury::A prior injury is an earlier event that may be relevant to the current history without automatically being the same current condition.]] to this knee, although I do not have the old records with me today.
Dr Arun | We can clarify those separately. What movement seems to make the current discomfort more noticeable?
Luca | Turning feels like an [[aggravating factor::An aggravating factor is an activity associated with worsening symptoms, not proof of a particular tissue diagnosis.]], but I have not been trying movements just to test the knee myself.
Dr Arun | That account helps. Have you been told a diagnosis, or are the terms you have heard guesses from teammates?
Luca | They mentioned a [[ligament::A ligament links bones across a joint, but mentioning that structure does not establish that it is injured in this case.]] tear and a meniscus problem, but those were suggestions rather than a clinician's findings.
Dr Arun | Then we will not copy them into the record as confirmed. Different structures and symptoms need proper assessment.
Luca | I also mixed up sprain and [[strain::A strain concerns muscle or tendon, while a sprain concerns ligament tissue; neither is confirmed by this history alone.]]. I understand now that the words do not simply mean mild and severe versions of the same injury.
Dr Arun | Exactly. The next clinical assessment uses the actual history and findings; this description does not settle the diagnosis.
Luca | Then my report is a [[non-contact injury::A non-contact injury description identifies the absence of direct contact in the event, not a conclusion that the injury is minor or harmless.]] event with left-knee discomfort and some uncertain details, not a confirmed tear.''',
    rehearsal=['Read the corrected history and stress left, non-contact, and reported.', 'Change roles and clarify gave way without inserting a structural diagnosis.'],
    transfer_title='The side was entered incorrectly', transfer_setup='An athlete clarifies that the right ankle was involved, not the left. No diagnosis is supplied. The clinician follows the actual correction process and retains the source of the clarification.',
    transfer='''Athlete: "The affected ankle was the ___ one." | right | The athlete explicitly corrects the side to the right ankle.
Clinician: "The earlier ___ entry needs correction." | left | The left-side entry is the incorrect earlier information being corrected.
Athlete: "The diagnosis remains ___." | unconfirmed | A corrected side does not itself establish a clinical diagnosis.
Clinician: "I will preserve the correction's ___." | source | The record should identify where the clarification came from under the actual process.'''))

BOOK['units'].append(unit(
    title='Explaining an examination and inviting a pause', scene='Active movement is not passive movement',
    skill='Give clear examination explanations and check consent without converting cooperation into blanket permission.',
    brief='Physiotherapist Elena explains a planned shoulder examination to athlete Mo. She distinguishes movement Mo performs from movement guided by the examiner and explains that Mo can ask to pause. No maneuver, measured angle, diagnosis, or exercise prescription is supplied. Mo initially thinks range of motion means strength. The conversation practices explanation and consent within the actual clinical process.',
    cast='Elena | Physiotherapist\nMo | Athlete',
    culture=('Consent stays active', 'Explain a step before it happens. Agreeing to an appointment does not remove the person\'s ability to ask questions, decline a step, or request a pause.'),
    a='''What does Mo initially confuse? | Movement range and strength | Appointment time and date | Shoulder and ankle | Consent and an imaging result | The case explicitly describes confusion between range of motion and strength.
Which action remains available to Mo? | Ask to pause | Authorize every future procedure automatically | Diagnose the shoulder from the dialogue | Choose an invented maneuver | The explanation makes clear that Mo can request a pause during the actual process.
What is not supplied? | A measured angle | A planned explanation | A patient question | The clinician's role | No measured range, maneuver, or examination finding appears in the case.''',
    vocabulary='''range of motion | Extent of movement available at a joint. | assess range of motion
active movement | Movement performed by the person using their own muscles. | explain active movement
passive movement | Movement guided by another person or an external force. | explain passive movement
resisted movement | Movement or effort made against an applied resistance. | describe resisted movement
flexion | Bending movement that generally decreases a joint angle. | explain shoulder flexion in context
extension | Movement generally increasing a joint angle or moving from flexion. | describe extension
abduction | Movement away from the relevant body midline. | explain abduction
adduction | Movement toward the relevant body midline. | explain adduction
internal rotation | Rotation toward the relevant anatomical midline. | describe internal rotation
external rotation | Rotation away from the relevant anatomical midline. | describe external rotation
palpation | Examination by touch using an appropriate clinical technique. | explain palpation before contact
tenderness | Pain or discomfort elicited by examination pressure. | document assessed tenderness
muscle strength | Capacity to produce force in the relevant assessment. | assess muscle strength
functional task | Activity used to examine a relevant everyday or sporting demand. | clarify a functional task
baseline measurement | Initial measurement used for later comparison. | record a baseline measurement
examination consent | Agreement to an explained examination within the actual consent process. | confirm examination consent
chaperone | Person present in an examination under the relevant policy and preference. | offer a chaperone appropriately
stop signal | Agreed way to request a pause or stop. | establish a stop signal''',
    precision='Range of motion describes movement extent, not muscle strength. Active and passive describe how movement occurs, not whether the athlete is cooperative.',
    precision_extra='This script explains terms, not examination technique. Actual steps, consent, chaperone arrangements, and clinical responses follow the relevant professional process.',
    phrases='''Explain the purpose | This part looks at how the shoulder moves, not only how strong it is.
Distinguish the action | Active means you move it yourself; passive means movement is guided.
Ask before contact | I will explain the next step before any contact.
Invite a pause | Please tell me if you want to pause or stop.
Check meaning | How would you describe that distinction in your own words?
Avoid a label | Passive does not mean you are being unhelpful.
Clarify the measure | A range measurement is not a complete diagnosis.
Keep consent specific | We can discuss this step separately before proceeding.''',
    notes='''Can you versus you must | Can you may invite an action, but the surrounding explanation must make the person's ability to pause or decline clear.
Active/passive | These are movement terms in this context, not character judgments or grammatical voice labels.
Before | Before marks the timing of explanation and permission relative to contact or the next examination step.''',
    d='''Which explanation distinguishes active and passive correctly? | You move it yourself versus movement guided by another | Helpful versus unhelpful behavior | Strong versus weak tissue | Safe versus dangerous diagnosis | The terms describe how movement is produced, not character, strength, or a diagnosis.
Which instruction supports ongoing consent? | Tell me if you want to pause before we continue | You attended, so every step is agreed | Remain silent even if unclear | Questions can only be asked afterward | This statement keeps the person's ability to pause and clarify visible.
Which pair should not be treated as identical? | Range of motion and muscle strength | Left and left | Appointment and scheduled visit | Explanation and explanation | Movement extent and force production are different assessment concepts requiring clear language.
Which claim would invent a finding? | Your range is exactly normal | This step concerns movement | You can ask for a pause | No angle is supplied here | No measurement or finding is provided, so normal would be an unsupported result.''',
    dialogue='''Elena | Before the examination, I would like to explain what we are looking at and how you can ask to pause.
Mo | Thank you. I thought [[range of motion::Range of motion describes how far a joint moves, which differs from the force measured in a strength assessment.]] was another way of saying how strong my shoulder is.
Elena | They are different questions. Movement extent and force production can both be relevant, but one does not replace the other.
Mo | So a [[baseline measurement::A baseline measurement provides an initial comparison point and is not automatically a complete diagnosis or a future clearance decision.]] gives you a starting point rather than a complete diagnosis from one number.
Elena | Exactly. I will also explain whether a movement is one you perform or one that is guided during examination.
Mo | Would [[active movement::Active movement is performed by the person using their own muscles, rather than being guided entirely by another person.]] mean that I move the shoulder myself, using my own muscles?
Elena | Yes. The term describes how the movement happens, not whether you are trying hard enough to please the examiner.
Mo | Then [[passive movement::Passive movement is guided by another person or external force and does not mean the athlete is uncooperative.]] would mean movement is guided, not that I am being unhelpful or refusing to participate.
Elena | Correct. I will explain each step before we do it; I am not asking you to try unfamiliar examination techniques yourself.
Mo | I appreciate that. I would like an explanation before [[palpation::Palpation is examination by touch and should be explained within the actual examination and consent process.]] or any other contact, rather than being surprised halfway through.
Elena | We can do that. Please also tell me if something is unclear or you want to pause before the next step.
Mo | Could we agree on a [[stop signal::A stop signal gives the person a clear way to request a pause or stop during the actual examination process.]] now? Sometimes I hesitate when a clinician seems busy or focused.
Elena | Yes, and you can say stop or ask a question directly. Coming to the appointment does not remove that choice.
Mo | That makes [[examination consent::Examination consent concerns the explained examination and remains specific to the actual process rather than being assumed for every possible step.]] feel specific to what we discuss, rather than permission for every possible procedure.
Elena | Precisely. We can also discuss the relevant chaperone arrangements and your preferences under the service's actual policy.
Mo | I would like to understand when a [[chaperone::A chaperone is a person present during an examination under the relevant policy and preferences, which should be explained rather than assumed.]] is offered and how that works before deciding about the appointment arrangements.
Elena | We will explain it. We should also keep the words movement, strength, and function separate in the summary.
Mo | A [[functional task::A functional task examines an activity relevant to everyday or sporting demands, which is different from one isolated movement measurement.]] would relate to an actual activity, rather than only one isolated angle or force measurement.
Elena | Exactly. The real assessment determines which information is appropriate and what it means in your situation.
Mo | Then [[muscle strength::Muscle strength concerns force production, and distinguishing it from motion and function helps prevent an oversimplified interpretation of the examination.]] is one part of the discussion, not a word I should use for every aspect of the shoulder examination.''',
    rehearsal=['Read the corrected explanation and contrast active, passive, range, and strength.', 'Swap roles and practice asking for a pause before an unexplained step; do not perform examination maneuvers.'],
    transfer_title='The request was to pause, not to finish', transfer_setup='During an examination explanation, an athlete asks to pause for clarification. No measurement has yet been taken and no finding is established.',
    transfer='''Athlete: "I would like to ___ before the next step." | pause | The athlete explicitly requests a pause to clarify the explanation.
Clinician: "Let us clarify the ___ first." | explanation | Clarification is needed before continuing the discussed examination step.
Athlete: "No measurement has been ___." | taken | The case states that no measurement has yet occurred.
Clinician: "There is no established examination ___." | finding | Without an examination result, the dialogue cannot supply an established finding.'''))

BOOK['units'].append(unit(
    title='Reading back a rehabilitation plan', scene='The current plan is not the next progression',
    skill='Clarify exercise-plan language, version changes, and review ownership without inventing treatment details.',
    brief='Athlete Tessa has two rehabilitation documents. The current signed plan specifies supervised rehabilitation and a review before any progression. An older handout uses broader wording about practice. Physiotherapist Omar confirms the current version and the responsible clinician. No exercise name, dosage, resistance, or progression criterion is supplied in this exercise.',
    cast='Tessa | Athlete\nOmar | Physiotherapist',
    culture=('Instructions must survive the journey home', 'Read-back checks whether the explanation was clear. It should not become a test that rewards guessing an unsupplied exercise or dosage.'),
    a='''Which document governs the supplied communication? | The current signed rehabilitation plan | The older broad handout | A teammate's routine | A guessed exercise schedule | The current signed plan is the verified instruction identified in the case.
What must happen before progression? | The stated clinical review | A competition date arriving | Buying new equipment | Completing this English exercise | The supplied plan explicitly requires a review before progression.
Which detail is absent? | Exercise dosage | A current plan | An older handout | The need for review | No exercise, dosage, resistance, or progression criterion is provided here.''',
    vocabulary='''rehabilitation plan | Agreed clinical plan for recovery of relevant function. | clarify the rehabilitation plan
exercise prescription | Authorized specification of exercise within a clinical plan. | verify an exercise prescription
repetition | One complete performance of a specified movement. | distinguish a repetition
set | Group of repetitions performed under a specified plan. | distinguish a set
resistance | Load opposing a movement or effort. | specify the actual resistance
frequency | How often an activity is prescribed or performed. | clarify exercise frequency
duration | Length of time an activity lasts. | distinguish duration from frequency
progression | Planned movement to a different activity or demand under relevant criteria. | authorize a progression
regression | Adjustment to a less demanding activity within a clinical plan. | clarify a regression
supervised session | Session conducted with the specified professional oversight. | confirm a supervised session
home program | Prescribed activities intended for the home setting. | review a home program
load tolerance | Response to a specified amount or type of demand. | assess load tolerance
exercise adherence | Extent to which an agreed exercise plan is followed. | discuss exercise adherence accurately
symptom response | Change in symptoms during or after an activity. | report the symptom response
review criterion | Condition or information used at a clinical review. | clarify a review criterion
prescribing clinician | Professional responsible for the relevant prescribed plan. | identify the prescribing clinician
superseded instruction | Earlier direction replaced by a current one. | identify a superseded instruction
plan version | Identifiable issue of a plan distinguished by date or revision. | confirm the plan version''',
    precision='Sets, repetitions, resistance, frequency, and duration are distinct details. None can be inferred from a generic instruction to do more, and none is supplied here.',
    precision_extra='The current plan requires review before progression. A language read-back confirms understanding; it does not authorize exercise or advancement.',
    phrases='''Check the version | Which dated plan are we reading together?
Separate instructions | That wording belongs to the older handout, not the current plan.
Clarify the unit | Do you mean sets, repetitions, or the length of the session?
Read back | My understanding is supervised rehabilitation, then review before progression.
Identify authority | Which clinician can clarify or change this instruction?
Avoid guessing | I cannot supply a resistance value that is not written here.
Report response | I will describe what happened during and after the specified activity.
Confirm the limit | Completing this conversation does not change the clinical plan.''',
    notes='''Before progression | Before makes the review a prior step rather than a discussion that can be postponed until after advancement.
More | More is incomplete without the relevant quantity or dimension: repetitions, load, frequency, and duration differ.
Current versus older | The date and authority of the plan matter; a familiar older handout is not automatically the governing instruction.''',
    d='''Which read-back matches the plan? | Supervised rehabilitation, with review before progression | Unrestricted practice now | Progress whenever the calendar changes | Copy the older handout because it is shorter | The current plan specifies supervision and a review before progression.
Why is do more an inadequate instruction? | It leaves the dimension of change unclear | It always means double the resistance | It always means add another day | It automatically replaces supervision | More does not identify whether load, frequency, repetitions, or duration should change.
Which action handles the conflicting documents appropriately? | Verify the current version with the responsible clinician | Combine both into a new plan | Choose whichever sounds easier | Treat the older date as stronger authority | The discrepancy needs authorized clarification, not an improvised mixture of instructions.
Which claim exceeds this exercise? | The athlete should use a particular resistance | There are two documents | The current plan requires review | The older wording is broader | No resistance or exercise dosage is supplied, so a specific value would be invented.''',
    dialogue='''Tessa | I have two documents, and the older one makes it sound as though I can return to practice now.
Omar | Let us verify the [[plan version::Plan version identifies which dated and authorized instruction is current when documents contain different wording.]] before combining instructions that were written at different stages of your care.
Tessa | This signed page is the current one. It says supervised rehabilitation and review before any progression.
Omar | Then that is the [[rehabilitation plan::The rehabilitation plan is the current agreed clinical instruction, which must remain distinct from an older generic handout.]] we need to explain, while the older wording is clarified through the appropriate process.
Tessa | I had also written do more in my own notes, but now I cannot remember what more referred to.
Omar | That does not identify [[frequency::Frequency describes how often an activity occurs and cannot be inferred from the ambiguous phrase do more.]], duration, resistance, or repetitions. We should not guess which detail was intended.
Tessa | I sometimes confuse a set with a repetition. I want to understand the words before reading the actual instructions.
Omar | A [[repetition::A repetition is one complete performance of a specified movement, whereas a set groups repetitions under the prescribed plan.]] is one complete performance of a movement; a set is a group of repetitions in the plan.
Tessa | Understanding those terms does not give me permission to add either one when I feel confident, does it?
Omar | Correct. [[Progression::Progression changes the activity or demand under the appropriate clinical criteria and is not authorized by understanding the vocabulary.]] follows the clinical decision and criteria, not simply your understanding of the terms or the competition calendar.
Tessa | The current page also says supervised. I should not turn that into an unsupervised home program myself.
Omar | Exactly. A [[supervised session::A supervised session requires the specified professional oversight and should not be relabeled as an independent home activity.]] is a different arrangement, and any change needs the appropriate clarification and authority.
Tessa | If I notice a change during the activity, what language helps me report it accurately to the clinician?
Omar | Describe the actual [[symptom response::Symptom response describes what happened during or after the specified activity and should be reported without inventing a clinical interpretation.]], including when it occurred, while following your real clinical instructions and contact pathway.
Tessa | I should not decide that discomfort means the plan is definitely working, or that any change proves a new injury.
Omar | Right. The [[prescribing clinician::The prescribing clinician is responsible for the relevant plan and needs accurate information when instructions or responses require review.]] needs the actual information rather than a conclusion added to sound certain.
Tessa | Could we mark which older wording is no longer the instruction so I do not repeat it to my coach?
Omar | We should identify the [[superseded instruction::A superseded instruction is an earlier direction replaced by the verified current plan and should not continue circulating as current guidance.]] through the approved process and ensure the corrected message reaches the relevant people.
Tessa | My read-back is supervised rehabilitation, then the stated review before progression, with no invented numbers or exercises.
Omar | That preserves the [[review criterion::A review criterion belongs to the actual clinical decision process and must not be replaced with a guessed timetable or an invented test.]] and the clinician's authority. I will clarify the missing detail before we treat any progression as agreed.''',
    rehearsal=['Read the corrected exchange and distinguish sets, repetitions, frequency, and duration.', 'Swap roles and read back the current plan without adding an exercise, dose, or progression rule.'],
    transfer_title='More often is not more resistance', transfer_setup='An athlete asks whether more often and greater resistance mean the same thing. No change to the actual rehabilitation plan has been prescribed.',
    transfer='''Athlete: "More often refers to ___." | frequency | Frequency describes how often the specified activity occurs in the plan.
Clinician: "Greater resistance changes the opposing ___." | load | Resistance concerns the load opposing an effort, not how often it occurs.
Athlete: "No plan change has been ___." | prescribed | The case explicitly provides no authorized change to the current plan.
Clinician: "The actual instruction needs appropriate ___." | clarification | Unclear directions should be clarified through the responsible clinical process rather than guessed.'''))

BOOK['units'].append(unit(
    title='Communicating concussion follow-up clearly', scene='Back in class is not back in contact practice',
    skill='Distinguish return-to-learn arrangements from return-to-sport authorization without minimizing symptoms.',
    brief='Student athlete Avery is following an actual clinician-led concussion process. The current school note permits specified classroom adjustments; it does not authorize contact practice or competition. Coach Morgan asks whether attending class means Avery is cleared to play. Athletic trainer Sal explains the difference and identifies the responsible healthcare professional. No symptom score, examination result, or progression step is supplied.',
    cast='Morgan | Coach\nSal | Athletic trainer',
    culture=('A positive step can still have limits', 'Acknowledge progress without making it an all-clear. Coaches need precise participation information, not a reassuring phrase that erases the stated restrictions.'),
    a='''What does the current note address? | Specified classroom adjustments | Unrestricted contact practice | Competition clearance | A complete symptom assessment | The supplied note concerns school arrangements, not sport participation clearance.
Who must handle the clinical authorization question? | The responsible healthcare professional | The coach alone | A teammate | The English exercise | Actual return-to-sport authorization belongs within the appropriate clinical process.
Which inference is unsupported? | Attending class means cleared for contact play | A school note exists | The coach has a question | The process is clinician-led | The classroom arrangement does not establish permission for contact practice or competition.''',
    vocabulary='''concussion | Brain injury requiring appropriate clinical assessment and management. | communicate a concussion concern
return to learn | Process of resuming learning with appropriate supports after concussion. | clarify return-to-learn arrangements
return to sport | Clinically guided process of resuming sporting activity. | clarify return-to-sport status
cognitive exertion | Mental effort associated with learning or other thinking tasks. | discuss cognitive exertion
physical exertion | Bodily effort associated with activity. | distinguish physical exertion
symptom inventory | Structured record of reported symptoms. | review a symptom inventory
headache | Pain experienced in the head. | report a headache accurately
dizziness | Reported sense of altered balance or spatial orientation. | describe dizziness
photophobia | Sensitivity or discomfort associated with light. | explain photophobia
concentration difficulty | Trouble sustaining or directing attention. | describe concentration difficulty
academic adjustment | Temporary change supporting participation in learning. | confirm an academic adjustment
contact practice | Practice involving the relevant sport's physical contact demands. | distinguish contact practice
non-contact activity | Activity without the specified contact demands. | specify non-contact activity
medical clearance | Authorization by the appropriate healthcare professional for a defined activity. | verify medical clearance
staged progression | Stepwise advancement under the applicable clinical process. | follow the authorized staged progression
symptom recurrence | Return of symptoms after improvement or absence. | report symptom recurrence
clinical reassessment | Further evaluation by the appropriate healthcare professional. | arrange clinical reassessment
participation status | Current authorized level and conditions of involvement. | communicate participation status''',
    precision='A return-to-learn note and sport clearance answer different questions. Classroom attendance does not establish readiness for contact practice or competition.',
    precision_extra='No symptom report or score is supplied here, and a single reassuring statement cannot replace the actual clinician-led process. Follow real emergency and concussion procedures for actual concerns.',
    phrases='''Separate the permissions | The school note addresses classroom arrangements, not contact practice.
Specify the activity | Which exact activity are you asking about?
Avoid all-clear | Progress in one setting is not unrestricted clearance.
Identify the decision-maker | The responsible healthcare professional must clarify that authorization.
Preserve the note | Let us use the current written participation information.
Reject calendar pressure | The match date does not replace the clinical process.
Clarify a report | No symptom score or examination finding is supplied in this update.
Confirm receipt | Please read back the participation limit your team has received.''',
    notes='''Back at school | This phrase identifies attendance, not the level of learning demand or permission for sport.
Cleared for | Cleared for needs a specific activity and scope; the word cleared alone invites an overbroad interpretation.
Yet | Not authorized yet describes the present status without promising when authorization will occur.''',
    d='''Which reply corrects the coach's inference? | Classroom arrangements do not authorize contact practice | Attending class always means fit for a match | A quiet morning proves recovery | The calendar supplies medical clearance | Different settings and demands require their actual authorization; attendance alone is insufficient.
What detail should accompany cleared? | The activity and conditions authorized | The team's ranking | The athlete's jersey number | The public's expectation | Clearance must specify its scope rather than imply permission for every activity.
Which wording preserves the evidence limit? | No symptom score is supplied in this update | All symptoms have resolved | The examination is normal | There is no risk of recurrence | The exercise supplies no symptom score or finding, so the other statements invent reassurance.
What does the match date establish? | A scheduling pressure, not clinical authorization | Automatic permission for contact | Completion of every progression stage | A normal assessment | A competition date is an organizational fact and cannot establish clinical clearance.''',
    dialogue='''Morgan | Avery is back in class this week. Can I take that as permission to include them in contact practice?
Sal | No. The note addresses [[return to learn::Return to learn concerns supported learning; it does not authorize sporting contact or competition.]] arrangements, which are different from permission to resume the sport's contact demands.
Morgan | I do not want to ignore progress, but the phrase back at school sounded like a general all-clear.
Sal | We can acknowledge progress while keeping the [[participation status::Participation status describes the current authorized activities and conditions rather than an unrestricted impression of recovery.]] precise. The supplied note permits specified classroom adjustments, not contact practice.
Morgan | Would a shorter practice count as the same kind of adjustment, just with less time on the field?
Sal | That would be a new activity decision. [[Physical exertion::Physical exertion involves bodily demands and cannot be assumed equivalent to the learning arrangements described in a school note.]] and the demands of contact sport need their actual clinical authorization.
Morgan | Then a school arrangement involving reduced concentration demands is not a substitute for a sports decision.
Sal | Correct. [[Cognitive exertion::Cognitive exertion concerns mental effort, distinct from the physical demands of sports practice.]] is part of a different context, although the clinical team coordinates the overall recovery process.
Morgan | Who should answer the specific question about practice if the classroom note is not meant to answer it?
Sal | The responsible healthcare professional should clarify [[medical clearance::Medical clearance must come from the appropriate healthcare professional and specify the activity being authorized.]] through the actual process, with the permitted activity and conditions made explicit.
Morgan | I have not seen a symptom score or an examination report. I should not tell the team they were normal.
Sal | Exactly. A [[symptom inventory::A symptom inventory records reported symptoms; the classroom note supplies no such assessment.]] is not supplied in this update, so we cannot create a reassuring result from its absence.
Morgan | The match is approaching, and people will ask when the athlete can return. I cannot promise a date from this note.
Sal | That is right. The actual [[staged progression::Staged progression follows the applicable clinical process and is not completed merely because a competition date is approaching.]] is not replaced by the team calendar or a confident-sounding prediction.
Morgan | Could I at least say that non-contact activity and contact practice are separate categories when I explain the question?
Sal | Yes, but neither is authorized by this school note. [[Contact practice::Contact practice involves specific physical demands that must not be inferred as permitted from a classroom attendance arrangement.]] has a particular meaning and needs its own decision in the clinical plan.
Morgan | If there is a new concern, we should use the actual clinical route rather than wait for an informal team discussion.
Sal | Correct. Any need for [[clinical reassessment::Clinical reassessment means further professional evaluation under the actual clinical process.]] follows our concussion and emergency procedures. Please use the designated clinical contact, not an informal team discussion.
Morgan | My read-back is classroom adjustments only in this note, with the sport participation question still requiring clarification.
Sal | That is accurate. [[Return to sport::Return to sport is a clinician-guided process whose authorization must be distinguished from the supplied return-to-learn arrangements.]] remains a separate authorization question; we will communicate the actual decision when it is made.''',
    rehearsal=['Read the corrected conversation and distinguish school attendance, contact practice, and clearance.', 'Swap roles and answer the coach\'s question without promising a date or inventing a normal assessment.'],
    transfer_title='The message omitted the activity', transfer_setup='A team message says cleared, but the actual current note authorizes only a specified non-contact activity. It does not authorize competition.',
    transfer='''Clinician: "The authorization is for the specified ___ activity." | non-contact | The current note explicitly limits the authorization to the specified non-contact activity.
Coach: "It does not authorize ___." | competition | Competition is not included in the authorization described in the brief.
Clinician: "The shorter message lost the ___." | scope | The word cleared alone omitted the activity and limits of the authorization.
Coach: "I will send the accurate participation ___." | information | The corrected message should preserve the actual permission rather than broaden it.'''))

BOOK['units'].append(unit(
    title='Comparing training load without false equivalence', scene='The same minutes, a different session',
    skill='Compare activity records while separating duration, intensity, and the limits of monitoring data.',
    brief='Athlete Dani and sports clinician Priya compare two fictional training logs. Both sessions lasted 30 minutes. One was recorded as easy cycling; the other as repeated hard intervals. The logs use a stated perceived-effort scale, but no individualized training recommendation is supplied. Dani calls the sessions the same load because their durations match. Priya clarifies what the records do and do not establish.',
    cast='Dani | Athlete\nPriya | Sports clinician',
    culture=('A number needs its definition', 'Wearable metrics and training jargon can create apparent precision. Clarify what the number measures before comparing it or assigning a clinical meaning.'),
    a='''Which detail is the same in both records? | Duration of 30 minutes | Intensity description | Type of session | A verified clinical effect | Both sessions last thirty minutes, but their recorded demands differ.
What distinguishes the sessions? | Easy cycling versus repeated hard intervals | Different documented injuries | Different prescribed medicines | A guaranteed recovery difference | The logs distinguish session type and effort, without supplying clinical outcomes.
What is not provided by this comparison? | An individualized progression recommendation | Two activity records | A shared duration | Different effort descriptions | The case compares language and records, not a personal training prescription.''',
    vocabulary='''training load | Amount and character of demand imposed by training. | describe training load
external load | Work performed, such as distance or power, measured outside the person's response. | quantify external load
internal load | Person's physiological or perceived response to the work. | describe internal load
training volume | Total amount of training under the stated measure. | compare training volume
intensity | Degree of effort or demand relative to the stated context. | distinguish training intensity
session RPE | Session rating of perceived exertion under a defined scale and method. | record session RPE
perceived exertion | Person's reported sense of effort. | clarify perceived exertion
interval training | Training alternating periods of specified effort and recovery. | describe interval training
steady-state activity | Activity maintained at a relatively consistent demand. | compare steady-state activity
recovery interval | Period between efforts within a training session. | specify the recovery interval
work-to-rest ratio | Relationship between effort and recovery periods. | clarify the work-to-rest ratio
weekly mileage | Distance covered in the stated week. | compare weekly mileage
acute workload | Recent training demand over the defined short period. | define the acute workload window
chronic workload | Training demand over the defined longer period. | define the chronic workload window
fatigue | Experience or state of reduced capacity associated with effort or other factors. | report fatigue in context
recovery status | Current condition relevant to recovery, assessed through appropriate information. | discuss recovery status
wearable metric | Measurement or estimate reported by a wearable device. | interpret a wearable metric
monitoring limitation | Constraint on what a measurement or record can establish. | state a monitoring limitation''',
    precision='Equal minutes do not establish equal intensity or overall demand. A perceived-effort score and a device estimate are different kinds of information, not automatic diagnoses or permission to progress.',
    precision_extra='Define the scale, time window, units, and recording method. Do not use a workload label or ratio from this language exercise as an injury prediction or training prescription.',
    phrases='''Align the measure | Are we comparing time, distance, power, or reported effort?
Preserve the difference | The durations match, but the session demands differ.
Clarify the scale | Which effort scale was used for this entry?
Define the window | What dates are included in the weekly total?
Separate data types | That is a device estimate; this is the athlete's report.
Avoid prediction | This record alone cannot predict an injury or guarantee readiness.
Ask about context | What changed in the session besides the number of minutes?
Summarize precisely | Equal time does not mean an equivalent training session.''',
    notes='''Same | Same needs a named dimension. Same duration is narrower than same load or same effect.
Reported versus recorded by a device | These identify different sources and should not be silently merged into one supposedly objective value.
Over the week | The time window must be explicit when totals or averages are compared.''',
    d='''Which comparison is justified by the logs? | Equal duration but different recorded intensity | Identical overall load | Identical clinical effect | Guaranteed equal recovery time | The logs show matching minutes and different activity demands, not equivalent overall effects.
What does perceived exertion identify? | The person's reported effort | A direct image of tissue damage | A guaranteed readiness score | The device's battery level | Perceived exertion is the person's experience of effort, interpreted using the stated method.
Why clarify the weekly date range? | Totals need matching time windows | Dates establish a diagnosis | Every week has identical activity | Time windows never affect comparisons | Different included dates can make apparently similar weekly totals refer to different periods.
Which statement overreaches? | This wearable number guarantees no injury | The device reports an estimate | The sessions differ in intensity | The durations both equal thirty minutes | A device metric alone cannot guarantee safety or predict the absence of injury.''',
    dialogue='''Dani | Both sessions were thirty minutes, so I entered them as the same training load in my summary.
Priya | They have the same duration, but [[training load::Training load includes the amount and character of the demand, not simply the number of minutes spent exercising.]] is not described completely by the number of minutes alone.
Dani | One session was easy cycling, and the other was repeated hard intervals with recovery periods between them.
Priya | That difference in [[intensity::Intensity describes the degree of effort or demand, which can differ substantially between sessions with equal duration.]] should remain visible instead of disappearing behind a shared duration figure.
Dani | I also used a perceived-effort scale, though I am not sure whether the other athlete used the same one.
Priya | Clarify the scale before comparing [[session RPE::Session RPE is a rating of perceived exertion under a defined method, so the scale and recording approach need to be known.]]. The number needs its definition and recording method attached to it.
Dani | So my report of effort is not automatically the same kind of information as the bike's power reading.
Priya | Correct. The work performed can describe [[external load::External load concerns the work performed, such as measured power or distance, rather than the individual's response to that work.]], while your response to that work is a different part of the account.
Dani | The same bike session might feel harder on another day, but that feeling alone would not tell us why.
Priya | Exactly. [[Internal load::Internal load concerns the person's physiological or perceived response and should be interpreted in context rather than treated as a diagnosis.]] describes the response, not a complete explanation of every factor behind it.
Dani | I wrote intervals without saying how long the recovery periods were. That seems to leave an important detail out.
Priya | The [[work-to-rest ratio::The work-to-rest ratio describes the relationship between effort and recovery periods, helping distinguish sessions that share a broad label.]] helps describe the session, provided we use the actual recorded timings rather than inventing them.
Dani | My weekly total also starts on Sunday, while the team dashboard uses Monday through Sunday.
Priya | Then even [[weekly mileage::Weekly mileage must identify the included dates so distance totals from different recording windows are not compared as identical periods.]] needs a shared date window before you compare those totals meaningfully.
Dani | The watch gives a recovery number, but I should not describe that as a clinician saying I am ready.
Priya | A [[wearable metric::A wearable metric is a device measurement or estimate and does not automatically provide clinical clearance or an individualized training decision.]] is not clinical clearance. Its method and limitations belong in the interpretation.
Dani | I can report the sessions and how I felt without claiming that a ratio predicts an injury.
Priya | Yes. Keep any [[monitoring limitation::A monitoring limitation explains what the available data cannot establish, including a guaranteed injury prediction or safety conclusion.]] explicit rather than using a precise-looking number to support an unsupported prediction.
Dani | My corrected summary is equal duration, different intensity, different activity structure, and clearly identified data sources.
Priya | That is useful. We will assess [[recovery status::Recovery status requires the relevant actual assessment and cannot be settled by matching session durations or relying on one device estimate.]] and any training changes through the clinical process, not by treating those two durations as equivalent sessions.''',
    rehearsal=['Read the corrected comparison and emphasize the dimension attached to same.', 'Swap roles and distinguish recorded work, reported effort, and device estimates without prescribing training.'],
    transfer_title='The weekly totals cover different days', transfer_setup='Two logs both show 20 kilometers. Log A covers Monday to Friday; Log B covers Monday to Sunday. No intensity information is supplied.',
    transfer='''Athlete: "The distance totals are ___." | equal | Both records show twenty kilometers, so the stated distance totals match.
Clinician: "The recording windows are ___." | different | One record ends Friday while the other includes the whole week.
Athlete: "Intensity information is ___." | absent | The brief supplies no intensity data for either activity record.
Clinician: "Equal distance does not establish equivalent ___." | demand | Different time windows and missing intensity prevent an overall equivalence conclusion.'''))

BOOK['units'].append(unit(
    title='Explaining imaging findings in clinical context', scene='An image is not a return-to-play decision',
    skill='Explain the distinction between a structural report, symptoms, function, and a participation decision.',
    brief='Athlete Niko reads a fictional imaging report describing a finding that the reporting clinician says needs clinical correlation. No specific structure, diagnosis, severity, or treatment recommendation is supplied. Dr Bell explains what correlation means and why neither an alarming word nor a reassuring image phrase alone establishes symptoms, function, or sport clearance.',
    cast='Niko | Athlete\nDr Bell | Sports physician',
    culture=('Translate the question the test answered', 'Patients may read a report before discussing it with a clinician. Explain what an imaging finding can describe without making it the whole story or dismissing the concern it raises.'),
    a='''What does the report request? | Clinical correlation | Immediate unrestricted sport | A specific operation | A guaranteed prognosis | The report asks for interpretation alongside the actual clinical information.
Which detail is deliberately not supplied? | A named structural diagnosis | A report phrase | The athlete's question | The physician's explanatory role | The case gives no specific structure, severity, or diagnosis to interpret.
What cannot be concluded from this exercise? | The athlete's sport clearance | That an imaging report exists | That context matters | That Niko wants clarification | Clearance requires the actual assessment and decision, neither of which is supplied here.''',
    vocabulary='''imaging report | Written interpretation of an imaging examination. | review the imaging report
radiograph | Image commonly produced using X-rays. | explain a radiograph
magnetic resonance imaging | Imaging method using magnetic fields and radio waves. | discuss magnetic resonance imaging
diagnostic ultrasound | Imaging using sound waves for the relevant clinical examination. | explain diagnostic ultrasound
structural finding | Feature of anatomy described by examination or imaging. | interpret a structural finding
incidental finding | Finding discovered outside the primary question prompting the examination. | explain an incidental finding
clinical correlation | Interpretation of a finding alongside history, examination, and other relevant information. | seek clinical correlation
clinical significance | Meaning or importance of a finding for the actual clinical situation. | clarify clinical significance
imaging limitation | Constraint on what an examination can show or establish. | state an imaging limitation
report impression | Summarized interpretation section of an imaging report. | explain the report impression
comparison study | Earlier examination used as a reference for the current interpretation. | identify the comparison study
image quality | Technical adequacy of images for the question being assessed. | describe image quality
artifact | Image feature caused by technical or acquisition factors rather than the assumed anatomy. | identify a possible artifact
differential diagnosis | Set of possible explanations evaluated through clinical reasoning. | explain a differential diagnosis
symptom generator | Structure or process considered a possible source of symptoms. | assess a possible symptom generator
functional limitation | Restriction in performing a relevant activity. | describe a functional limitation
prognosis | Expected course or outcome with appropriate uncertainty. | discuss prognosis cautiously
shared interpretation | Explanation bringing the relevant findings and perspectives together. | support shared interpretation''',
    precision='Clinical correlation means the finding must be interpreted with the relevant clinical information. It does not mean the report proves the cause of symptoms, mandates treatment, or authorizes sport.',
    precision_extra='Do not invent a scan result or label a finding harmless from this exercise. An incidental finding is not automatically irrelevant; its actual significance needs appropriate review.',
    phrases='''Explain correlation | We need to connect this finding with the history and examination.
Separate structure and function | The image and your activity limitations answer different questions.
Avoid a leap | That phrase alone does not identify the cause of your symptoms.
Keep limits visible | The examination has limits that the report should describe.
Explain incidental | It was found outside the main question; that does not automatically mean unimportant.
Ask what matters | Which part of the report is most unclear to you?
Preserve uncertainty | We should not turn a possible explanation into a confirmed one.
Separate permission | An imaging phrase is not itself sport clearance.''',
    notes='''Suggests versus confirms | Suggests identifies a supported possibility; confirms asserts a stronger conclusion and needs the relevant evidence.
Incidental | Incidental describes how the finding arose in relation to the original question, not a universal judgment of harmlessness.
Correlate with | Correlate with requests interpretation alongside other information, not simple repetition of the report wording.''',
    d='''Which explanation best fits clinical correlation? | Interpret the finding with the history and examination | Treat the report as complete sport clearance | Ignore the athlete's symptoms | Choose treatment from one isolated word | Clinical correlation explicitly connects the report with relevant clinical information.
Which conclusion does incidental not automatically support? | The finding is harmless and needs no review | The finding was outside the primary question | The context matters | The report needs explanation | Incidental describes discovery context and does not by itself settle clinical importance.
Which pair should remain distinct? | Structural finding and functional limitation | Report and written report | Scan and imaging examination | Question and inquiry | A structural description and an activity limitation answer different questions in the assessment.
Which response handles uncertainty accurately? | This possible explanation needs clinical review | The report guarantees the cause | Every image phrase is a treatment instruction | No image has any clinical value | This response preserves the report's limits without dismissing imaging altogether.''',
    dialogue='''Niko | I read the report before the appointment, and the phrase clinical correlation made me think something had been missed.
Dr Bell | [[Clinical correlation::Clinical correlation means interpreting the finding alongside the history, examination, and other relevant information rather than reading the image in isolation.]] means we interpret the finding alongside the history, examination, and other relevant information, not that the phrase itself proves an error.
Niko | I saw one unfamiliar word and began treating it as the explanation for every symptom I have.
Dr Bell | A [[structural finding::A structural finding describes anatomy and does not automatically establish the cause of every reported symptom.]] is not automatically the cause of every symptom. We need the actual clinical context before making that connection.
Niko | Does the summary at the end carry a different role from the detailed description above it?
Dr Bell | The [[report impression::The report impression summarizes the imaging interpretation, but it remains part of a report that must be read in clinical context.]] summarizes the interpretation, but it still needs to be read with the details and any stated limitations.
Niko | If the report mentions an incidental finding, can I assume it has no importance at all?
Dr Bell | No. An [[incidental finding::An incidental finding was discovered outside the examination's primary question, which does not automatically establish that it is clinically unimportant.]] is outside the primary question that prompted the examination; its actual significance still needs appropriate review.
Niko | I also want to understand why my ability to train is discussed separately from what an image shows.
Dr Bell | A [[functional limitation::A functional limitation concerns an activity the person has difficulty performing, which is distinct from the structural description on an image.]] describes difficulty performing an activity. It is a different kind of information from the structure described in a scan.
Niko | So a reassuring-sounding phrase would not by itself give me permission to return to every sporting demand.
Dr Bell | Correct. A [[shared interpretation::A shared interpretation brings the relevant findings and perspectives together rather than letting one isolated report phrase determine every conclusion.]] brings the relevant information together; neither a reassuring phrase nor an alarming word supplies the entire participation decision.
Niko | The report also mentions limits. I thought any modern scan would answer every possible question about the injury.
Dr Bell | An [[imaging limitation::An imaging limitation identifies what the examination cannot reliably show or establish and belongs in a careful interpretation of the findings.]] tells us what the examination cannot reliably show or establish. Different methods answer different questions.
Niko | Could a technical feature in an image be mistaken for something anatomical if the context is lost?
Dr Bell | That is one reason an [[artifact::An artifact can arise from technical or acquisition factors and should not be assumed to represent the anatomical finding someone expects.]] must be interpreted by the appropriate imaging professional rather than diagnosed from a cropped picture.
Niko | I would like an explanation of the actual report, not a general promise that every uncertain phrase is harmless.
Dr Bell | We can do that while keeping [[clinical significance::Clinical significance concerns what the finding means for the actual person and clinical question, not merely how dramatic the wording sounds.]] separate from how dramatic a term sounds when read without an explanation.
Niko | And any forecast about recovery should state what is known and what remains uncertain in my assessment.
Dr Bell | Exactly. A [[prognosis::A prognosis describes an expected course with appropriate uncertainty and cannot be guaranteed from a single isolated imaging phrase.]] is not a guarantee extracted from one report phrase. It belongs to the actual clinical discussion.''',
    rehearsal=['Read the corrected explanation and distinguish finding, significance, function, and clearance.', 'Change roles and explain clinical correlation without inventing a diagnosis or treatment recommendation.'],
    transfer_title='Suggests became confirms', transfer_setup='A referral summary changed the report phrase suggests a possible explanation to confirms the cause. The original report required clinical correlation; no further assessment is supplied.',
    transfer='''Clinician: "The original report said ___." | suggests | Suggests preserves a possible interpretation rather than asserting confirmation.
Colleague: "The summary incorrectly changed that to ___." | confirms | Confirms increases certainty beyond the original report's stated meaning.
Clinician: "The need for clinical correlation ___." | remains | No additional assessment is supplied to resolve the original requirement for context.
Colleague: "I will correct the overstated ___." | certainty | The correction must restore the original level of certainty instead of repeating an unsupported conclusion.'''))

BOOK['units'].append(unit(
    title='Discussing return-to-sport criteria under pressure', scene='The final is a date, not a criterion',
    skill='Communicate a conditional participation decision while acknowledging competitive pressure and uncertainty.',
    brief='Athlete Imani hopes to play in a final in two weeks. The actual rehabilitation team has not yet authorized competition; a review of the relevant functional and sport-specific criteria is pending. Sports physician Dr Vale explains that the event date is not a clinical criterion. No test score, recovery timetable, or specific clearance standard is supplied. Imani asks how to explain the position to the coach without sounding uncommitted.',
    cast='Imani | Athlete\nDr Vale | Sports physician',
    culture=('Acknowledge the stakes without bargaining away the decision', 'The athlete may fear losing a role or disappointing teammates. Recognize that pressure while keeping authorization tied to the actual assessment and responsible clinician.'),
    a='''What is the current competition status? | Not yet authorized | Unrestricted clearance | Guaranteed selection | Approved because the final is near | The brief explicitly states that competition has not been authorized.
What is pending? | Review of relevant criteria | A known winning result | A supplied normal test score | A promised two-week recovery | The actual review remains pending, with no criteria results provided here.
What does two weeks identify? | Time until the final | Guaranteed recovery duration | A universal clearance standard | A prescribed rehabilitation dose | Two weeks is the event timing and cannot be treated as a clinical recovery guarantee.''',
    vocabulary='''return to participation | Resumption of some sporting involvement under the relevant limits. | distinguish return to participation
return to performance | Regaining the desired level of sporting performance. | distinguish return to performance
competition readiness | Suitability for the relevant competitive demands under actual assessment. | discuss competition readiness
sport-specific demand | Requirement particular to the athlete's sport or role. | identify sport-specific demands
functional testing | Assessment of relevant task performance under the actual clinical process. | explain functional testing
criteria-based decision | Decision linked to specified evidence or conditions rather than time alone. | communicate a criteria-based decision
time-based milestone | Point defined by elapsed time. | distinguish a time-based milestone
psychological readiness | Mental preparedness relevant to returning to activity. | discuss psychological readiness
fear of reinjury | Concern about sustaining injury again. | acknowledge fear of reinjury
confidence in movement | Person's trust in performing a movement or task. | explore confidence in movement
graded exposure | Planned increase in exposure to relevant demands within an appropriate plan. | clarify graded exposure
movement quality | Characteristics of how a task is performed. | assess movement quality
capacity | Ability to meet a specified demand under the relevant assessment. | describe assessed capacity
performance demand | Requirement needed for the intended level of sporting performance. | specify the performance demand
selection pressure | Pressure associated with team or event selection. | acknowledge selection pressure
conditional authorization | Permission dependent on stated conditions. | communicate conditional authorization
decision rationale | Explanation of the basis for a decision. | explain the decision rationale
review outcome | Result of the actual review. | communicate the review outcome''',
    precision='An event date and time since injury are not interchangeable with satisfied criteria. Participation, competition, and performance can describe different demands and permissions.',
    precision_extra='This case supplies no pass score or clearance checklist. It practices conditional language, not a universal return-to-sport standard or an individualized prediction.',
    phrases='''Acknowledge the goal | I understand why this final matters to you.
State the present position | Competition has not yet been authorized.
Separate the calendar | The date tells us when the event happens, not whether the criteria are met.
Explain conditions | The decision depends on the actual review and relevant findings.
Avoid a promise | I cannot turn the two-week interval into a guaranteed recovery time.
Keep roles clear | Team selection and clinical authorization are different decisions.
Support the message | You can state the current limit without apologizing for following the plan.
Close with the next step | We will communicate the actual review outcome and its scope.''',
    notes='''If versus when | If preserves a condition that may not be met; when can imply that authorization is certain to occur.
Ready for what | Ready needs a named demand: limited participation, competition, and prior performance are different targets.
Not yet | Not yet identifies the current status without committing to a future date or result.''',
    d='''Which sentence preserves the condition? | If the actual review supports authorization, the team will communicate its scope | When you are cleared next week, play the final | The final itself proves readiness | Any participation means full performance | If keeps the outcome conditional on the actual review rather than promising clearance.
Which distinction helps answer the coach? | Clinical authorization and team selection | Medical review and a jersey color | Final and any calendar date | Athlete and team member | Selection is an organizational decision, while clinical authorization has its own responsible process.
Which reply acknowledges pressure without promising recovery? | I understand the final matters; the review still determines the decision | You will definitely play because you care | Missing a final means poor commitment | Confidence alone settles readiness | The reply recognizes the athlete's goal while preserving the unresolved clinical decision.
What is not supplied in this exercise? | A universal pass score | A pending review | A competition goal | An event date | No test result or clearance standard is given, so the learner must not invent one.''',
    dialogue='''Imani | The final is in two weeks, and I am worried that saying I am not cleared will sound like a lack of commitment.
Dr Vale | I understand the [[selection pressure::Selection pressure concerns the athlete's role or opportunity in the team and should be acknowledged without changing the clinical decision process.]]. Caring about the team does not require you to describe an authorization that has not been given.
Imani | Can the two weeks become our target, or would that make the date sound more certain than the assessment allows?
Dr Vale | It is a [[time-based milestone::A time-based milestone identifies a point on the calendar and does not establish that clinical or functional criteria have been satisfied.]], not proof that the relevant criteria will be met. I cannot promise recovery by that date.
Imani | Then what is the distinction between returning to some activity and returning to the level I played at before?
Dr Vale | [[Return to participation::Return to participation can involve limited sporting activity under defined conditions and differs from full competition or previous performance.]] may describe limited involvement, while competition and your previous performance can involve different demands.
Imani | I do not want a note about limited activity to be repeated as permission to play an entire match.
Dr Vale | That is why [[conditional authorization::Conditional authorization must preserve its stated limits and conditions rather than becoming an unrestricted permission when summarized.]] needs its conditions and scope attached whenever it is communicated to the team.
Imani | The coach asked whether I passed the functional tests, but I do not have a completed review outcome to report.
Dr Vale | Then say that. [[Functional testing::Functional testing assesses relevant task performance within the actual clinical process, and this scenario supplies no completed results to report.]] is part of the actual process; we should not insert a pass score that has not been supplied.
Imani | I can also feel confident in everyday movement and still feel uncertain about a full-speed change of direction.
Dr Vale | A [[sport-specific demand::A sport-specific demand concerns a task particular to the sport or role and can differ from the demands of everyday movement.]] is not necessarily equivalent to an everyday activity. The real assessment addresses the relevant demands.
Imani | Some of my hesitation is fear of another injury, but I do not want it dismissed as being weak.
Dr Vale | [[Psychological readiness::Psychological readiness concerns mental preparedness for return and should be discussed respectfully rather than used as a character judgment.]] deserves a respectful discussion alongside the other relevant information, not a judgment about your character.
Imani | How can I explain the position in one clear sentence without sounding as though I am negotiating the decision?
Dr Vale | You can say the [[review outcome::The review outcome is the result of the actual assessment process, which remains pending in the supplied case.]] is pending and competition has not yet been authorized. That is factual, not an apology.
Imani | And if the coach chooses another player, that selection decision is separate from the clinical question.
Dr Vale | Correct. We should explain the [[decision rationale::The decision rationale states the basis for the clinical position rather than relying on team pressure or an event date.]] clearly while leaving team selection to the appropriate team process.
Imani | Then the message is that I want to return, but desire and the calendar do not establish permission.
Dr Vale | Exactly. A [[criteria-based decision::A criteria-based decision depends on the relevant actual evidence and conditions rather than elapsed time or competitive pressure alone.]] preserves the actual evidence and responsibility, without promising when the required decision will be made.''',
    rehearsal=['Read the corrected exchange and contrast if with when in the authorization statements.', 'Swap roles and give the one-sentence status update without adding a return date or test result.'],
    transfer_title='A conditional note was shortened', transfer_setup='A clinical note allows only the specified activity under supervision. A team summary changes it to unrestricted training. No wider authorization exists.',
    transfer='''Clinician: "The note requires ___." | supervision | The actual authorization explicitly includes supervision as a condition.
Coach: "The summary incorrectly said ___ training." | unrestricted | Unrestricted broadens the permission beyond the limited activity in the note.
Clinician: "That change removed a ___." | condition | The shorter message omitted a condition that limits the authorization.
Coach: "I will restore the actual ___." | scope | The corrected summary must preserve the activity and conditions actually authorized.'''))

BOOK['units'].append(unit(
    title='Sharing participation information without oversharing', scene='The coach needs the limit, not the whole chart',
    skill='Clarify the recipient, purpose, and authorized scope of a sports-medicine update.',
    brief='Team coordinator Riley requests athlete Casey\'s complete medical chart to plan a practice session. Clinician Dr Shah explains that the team needs the actual authorized participation information, while access to health details follows the relevant consent, law, and institutional policy. Casey\'s permission for a limited participation update is documented; permission for unrestricted chart sharing is not. No diagnosis or specific restriction is supplied in the exercise.',
    cast='Riley | Team coordinator\nDr Shah | Clinician',
    culture=('Role clarity reduces friction', 'A colleague can have a legitimate planning need without being entitled to every clinical detail. Explain the useful information that can be shared through the actual authorized process.'),
    a='''What does the coordinator need for the stated task? | Authorized participation information | Every historical clinical note | A guessed diagnosis | Unrestricted personal records | The task is practice planning, for which the relevant participation information is needed.
What permission is documented? | A limited participation update | Unlimited chart distribution | Public posting of the diagnosis | Permission to add new restrictions | The brief explicitly limits the documented permission to a participation update.
What must govern access to health details? | Relevant consent, law, and institutional policy | The coordinator's curiosity | The match result | A general assumption about teammates | Actual information access depends on the applicable requirements, not a universal team entitlement.''',
    vocabulary='''confidentiality | Obligation to protect information under the applicable professional and legal rules. | maintain confidentiality
authorized disclosure | Sharing permitted under the relevant consent and other applicable requirements. | confirm authorized disclosure
participation restriction | Limit on an activity under the actual authorized plan. | communicate a participation restriction
need-to-know access | Access limited to information relevant to an authorized role and purpose. | apply need-to-know access
clinical record | Recorded information about assessment, care, and relevant health matters. | protect the clinical record
release authorization | Documented permission for specified information sharing under applicable rules. | verify a release authorization
recipient | Person or organization receiving the information. | identify the intended recipient
disclosure purpose | Reason for a particular information exchange. | specify the disclosure purpose
data minimization | Limiting shared information to what is appropriate for the purpose and requirements. | apply data minimization
secure channel | Approved communication route with appropriate protections. | use a secure channel
role-based access | Access permissions linked to an authorized work role. | check role-based access
athlete representation | Support or advocacy arrangement acting for an athlete within defined authority. | clarify athlete representation
team liaison | Contact coordinating communication between the team and relevant services. | identify the team liaison
conflict of interest | Situation in which competing interests may affect professional judgment. | disclose a conflict of interest
professional independence | Ability to exercise appropriate professional judgment without improper pressure. | preserve professional independence
status update | Communication of the current relevant position. | provide an accurate status update
audit trail | Traceable record of actions, access, or changes. | retain an audit trail
information governance | Rules and processes controlling information handling. | follow information governance''',
    precision='A legitimate planning purpose does not automatically authorize access to the whole chart. Share the actual permitted information through the approved route and keep the athlete\'s documented permission and applicable rules in view.',
    precision_extra='Privacy law, consent requirements, safeguarding duties, and institutional roles differ. This language exercise does not establish a universal disclosure rule or invent a clinical restriction.',
    phrases='''Clarify the task | What decision do you need this information to support?
Identify the useful update | The participation information addresses the practice-planning question.
Set the limit | Permission for a limited update is not unrestricted access to the chart.
Check the recipient | Who will receive the message, and will it be forwarded?
Preserve authority | Clinical judgment is separate from pressure to field a player.
Choose the route | We should use the approved communication channel.
Avoid disclosure by habit | Let us verify the authorization rather than copy the full record.
Close constructively | I will clarify what can be shared for this specific purpose.''',
    notes='''Need versus entitlement | A practical need should be clarified; it does not automatically establish permission for all requested information.
Limited to | Limited to marks a boundary that should remain attached when a message is forwarded or summarized.
Can share | Can share depends on the actual authorization and applicable requirements, not merely technical ability to send a file.''',
    d='''Which reply is both useful and appropriately bounded? | Let us confirm the authorized participation update for practice planning | You may have every record because you are on the team | I will invent a restriction so no details are needed | Planning never needs any information | This reply addresses the legitimate task while preserving the actual disclosure limits.
What does documented limited permission not establish? | Unrestricted chart access | A defined update purpose | The need to check scope | The identity of the relevant athlete | Limited permission cannot be expanded into blanket access to all health information.
Which question should precede forwarding? | Is the new recipient and purpose authorized? | Is the file small enough? | Is the team winning? | Would a shorter subject line look better? | Changing the recipient or purpose can change whether the actual disclosure is authorized.
Which distinction protects professional judgment? | Clinical authorization and team selection pressure | A clinician's title and font size | A record and its page count | Practice and a calendar entry | Clinical decisions must retain the appropriate professional authority rather than be dictated by selection pressure.''',
    dialogue='''Riley | Could you send Casey's complete chart? I need to organize tomorrow's practice and do not want to miss anything.
Dr Shah | What decision do you need to make? Clarifying the [[disclosure purpose::Disclosure purpose identifies why information is requested and helps determine which authorized information is relevant to the task.]] will help us identify the relevant information rather than defaulting to the whole record.
Riley | I need the actual participation limits so the practice plan does not contradict the clinical instructions.
Dr Shah | That calls for an authorized [[status update::A status update communicates the current relevant position for the task and need not include every detail in the clinical chart.]]. We should not assume that it requires every historical clinical detail.
Riley | Casey agreed to a limited participation update. Does that permission let me forward the whole chart to the assistants?
Dr Shah | No. We need to preserve the scope of the [[release authorization::Release authorization concerns specified information sharing and cannot be treated as blanket permission for unrestricted chart distribution.]] and the applicable rules, including the actual recipients and purpose.
Riley | Then I should identify who will receive the message instead of using an expanding group chat by habit.
Dr Shah | Correct. Each [[recipient::A recipient is the person or organization receiving information, and their role and authorization matter when the message is shared.]] and the communication route need to fit the relevant authorization and institutional requirements.
Riley | I do not need the diagnostic history simply to understand the participation information that has been authorized.
Dr Shah | That is the point of [[data minimization::Data minimization limits information to what is appropriate for the legitimate purpose and applicable requirements rather than sharing everything available.]]. It keeps the message useful without adding unrelated personal detail.
Riley | Would the ordinary team messaging app be acceptable, or should we check the service's actual requirements first?
Dr Shah | We should use the approved [[secure channel::A secure channel is an authorized communication route with appropriate protections, not merely the most convenient available messaging option.]] rather than assume that convenience establishes an appropriate route for health information.
Riley | The coach is under pressure to field the strongest team. I do not want that to affect how the clinical message is written.
Dr Shah | The clinical decision needs [[professional independence::Professional independence preserves the appropriate clinical judgment rather than allowing team selection pressure to determine the medical position.]]. We can communicate clearly without changing the authorization to satisfy a selection preference.
Riley | And my role as coordinator does not automatically give me every access permission held by the clinical team.
Dr Shah | Exactly. [[Role-based access::Role-based access ties information permissions to authorized work roles and does not grant every team member identical access to health records.]] depends on the actual authorized role, not simply belonging to the same organization.
Riley | I will tell the assistants that the participation update is being clarified, without adding a diagnosis or restriction from this conversation.
Dr Shah | Good. We should also retain the appropriate [[audit trail::An audit trail records relevant access, sharing, or changes so the handling of information can be traced under the actual process.]] of what was shared, with whom, and under which approved process.
Riley | Then we can support practice planning while respecting Casey's permission and the actual information-handling rules.
Dr Shah | Yes. [[Confidentiality::Confidentiality protects information under the relevant professional and legal requirements while allowing appropriately authorized communication for legitimate purposes.]] and useful coordination are compatible when the purpose, authority, and scope remain clear.''',
    rehearsal=['Read the corrected exchange and identify purpose, recipient, scope, and channel.', 'Swap roles and provide a bounded response to the chart request without inventing a diagnosis or restriction.'],
    transfer_title='A new recipient was added', transfer_setup='A participation update was authorized for the team liaison. Before forwarding it to an external sponsor, the coordinator checks the actual authorization; no sponsor disclosure has been approved.',
    transfer='''Coordinator: "The authorized recipient is the team ___." | liaison | The permission in the brief names the team liaison, not every outside party.
Clinician: "The sponsor is a different ___." | recipient | Adding an external sponsor changes who would receive the health-related information.
Coordinator: "Sponsor disclosure has not been ___." | approved | The case explicitly states that no sponsor disclosure has been approved.
Clinician: "We must check the actual authorization ___." | scope | The authorization's limits must be checked before information is shared more broadly.'''))
