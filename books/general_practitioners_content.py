"""Original consultation English for general practitioners and family physicians."""
from books.medical_support import medical_unit as unit, source, TEACH_BACK, SCOPE

BOOK = dict(slug='general-practitioners', title='General Practice English',
    cover_label='ENGLISH FOR GENERAL PRACTITIONERS', cover_title='General\nPractice', cover_size=40,
    tagline='Hear the concern. Make the plan clear.',
    audience='For general practitioners, family physicians, and primary-care doctors.',
    roles='general practitioners, family physicians, primary-care doctors, family medicine residents',
    summary='Consultation English for primary-care doctors: histories, uncertain results, treatment expectations, prevention, mental health, and coordinated follow-up.',
    map_intro='Eight consultations move from a shared agenda to accurate histories, medicines, test results, antibiotic expectations, screening, mental health, and referral follow-up.',
    notes_title='Clinical precision. Everyday language.',
    notes_intro='Primary care combines continuity with new concerns. These conversations practice how a doctor listens, explains the limits of evidence, negotiates a plan, and keeps responsibility visible.',
    field_notes=[
        ('Start with the patient agenda', 'Elicit the concern behind the appointment label. Explain how you will prioritize competing needs without treating a new concern as an interruption.', '"Which concern most needs our attention today?"'),
        ('Keep the timeline intact', 'A symptom account has a source, timing, and context. Ask what changed before compressing the history into clinical shorthand.', '"The tiredness began before the medicine was started."'),
        ('Explain uncertainty usefully', 'Name what is established, what remains possible, and the next step. Reassurance should not become an unsupported promise.', '"This result needs context; it does not establish a diagnosis by itself."'),
        ('Close the communication loop', 'A requested test or referral creates follow-up work. Identify who reviews it, how the patient hears back, and how unresolved concerns are escalated.', '"Our team will confirm receipt; that is different from a booked appointment."'),
    ], scope_note=SCOPE,
    sources=[TEACH_BACK,
        source('AAFP. Continuity of Care.', 'https://www.aafp.org/about/policies/continuity-of-care', 'Context for sustained primary-care relationships and coordination across encounters.'),
        source('CDC. Healthy Habits: Antibiotic Do\'s and Don\'ts.', 'https://www.cdc.gov/antibiotic-use/about/index.html', 'Background for antibiotic communication; fictional cases do not establish prescribing rules.'),
        source('AHRQ. Make Referrals Easy: Tool 21.', 'https://www.ahrq.gov/health-literacy/improve/precautions/tool21.html', 'Context for referral communication and follow-up responsibilities.')], units=[])

BOOK['units'].append(unit(
    title='Agreeing on a consultation agenda', scene='Three concerns, one visit',
    skill='Negotiate priorities without dismissing a newly disclosed concern.',
    brief='Dr Shah sees Morgan for a planned long-term-condition review. Morgan also wants to discuss tiredness and a form for work. No clinical urgency assessment has yet been made. Morgan says the tiredness matters most. Dr Shah will first clarify that concern and assess priorities, then explain what can be covered and what requires follow-up. No symptom is declared safe to postpone merely because the appointment was booked for another purpose.',
    cast='Dr Shah | General practitioner\nMorgan | Patient',
    culture=('An agenda is negotiated, not imposed', 'Invite the person to name their concerns before announcing the visit structure. A follow-up arrangement is a specific agreement, not a way to quietly drop an unresolved concern.'),
    a='''What was originally planned? | A long-term-condition review | A work-capacity assessment only | A confirmed emergency discharge | A completed tiredness investigation | The booking is a review; the other concerns emerge during this consultation.
Which concern does Morgan prioritize? | Tiredness | The work form | A medicine already prescribed today | A referral already completed | Morgan explicitly identifies tiredness as the concern that matters most.
What has not yet happened? | Clinical assessment of urgency | Morgan mentioning the form | The visit being booked | Morgan naming a priority | The brief says urgency has not been assessed at this point.''',
    vocabulary='''consultation agenda | Concerns and tasks agreed for a clinical encounter. | agree on the consultation agenda
presenting concern | Problem the patient brings to the current encounter. | elicit the presenting concern
continuity of care | Connected care over time with an ongoing clinical relationship. | maintain continuity of care
comorbidity | Another condition occurring alongside a particular condition. | review relevant comorbidity
multimorbidity | Presence of multiple long-term health conditions in one person. | manage multimorbidity
problem list | Organized record of a patient's identified health problems. | update the problem list
acute concern | A new or recently changing health concern. | assess an acute concern
long-term condition | Health condition requiring ongoing management or follow-up. | review a long-term condition
patient-centered care | Care attentive to the person's needs, priorities, and circumstances. | provide patient-centered care
functional limitation | Restriction affecting a person's usual activities or abilities. | describe a functional limitation
follow-up visit | Later encounter to review progress or unfinished care. | arrange a follow-up visit
priority | Issue judged to require attention before other issues. | establish the clinical priority
shared agenda | Visit priorities agreed through discussion with the patient. | negotiate a shared agenda
visit length | Time allocated or used for an encounter. | explain the visit length
care coordination | Organizing related care across people, services, or settings. | improve care coordination
concern elicitation | Inviting the patient to describe what needs attention. | use open concern elicitation
signposting | Explaining where a conversation is going next. | use clear signposting
safety-netting | Explaining what changes require further help and how to obtain it. | provide specific safety-netting''',
    precision='A booked review does not determine the urgency of a newly raised symptom. Agree on the agenda after appropriate clinical assessment, not before it.',
    precision_extra='A work form, a symptom, and a chronic-condition review are different tasks. Summarize all three so that prioritizing one does not erase the others.',
    phrases='''Open the agenda | What else were you hoping we could cover?
Reflect the priority | The tiredness is the main concern for you today.
Explain sequencing | I will clarify that concern before we agree on the order.
Avoid dismissal | I am not setting it aside because it was not on the booking.
Keep another task visible | The work form is still on our list.
Negotiate follow-up | Let us agree how to handle anything we cannot complete today.
Use a transition | First I will ask about the tiredness; then we will review the plan.
Check priorities | Have I captured the concerns in the right order?''',
    notes='''What else | Invites additional concerns without implying that the patient has used up permission to speak.
Before we agree | Makes the order conditional on clarification and assessment.
Still on our list | Reassures the patient that a deferred task has not been forgotten.''',
    d='''Which response avoids dismissing the symptom? | Let us clarify the tiredness before deciding the agenda. | That was not booked, so it cannot matter today. | The form proves you are well. | A review slot makes tiredness nonurgent. | Clarification must precede assumptions about priority or the symptom's significance.
Which wording preserves the patient's preference? | Morgan identifies tiredness as the main concern. | Morgan refuses all chronic care. | Morgan has only an administrative concern. | Morgan requests a diagnosis already confirmed. | The statement records Morgan's priority without inventing a refusal or diagnosis.
What does follow-up mean here? | An agreed later review of unfinished work | Permission to ignore new symptoms | A guarantee that no assessment is needed | Automatic completion of the form | A follow-up needs a clear purpose and does not replace necessary assessment.
Which signpost is clearest? | First the tiredness history, then we will agree on the remaining plan. | We will get to whatever matters eventually. | Everything is sorted already. | Nothing new can be raised. | Naming the history before the planning step makes the conversational sequence clear.''',
    dialogue='''Dr Shah | We booked a review of your ongoing condition. Before we start, what else were you hoping to discuss?
Morgan | I have been unusually tired, and I brought a work form. The tiredness is my main [[presenting concern::The presenting concern is the problem Morgan brings for assessment today.]].
Dr Shah | Thank you. I will ask about the tiredness before we decide which issues need attention first.
Morgan | I thought the [[consultation agenda::The consultation agenda includes the issues discussed and prioritized for this encounter.]] was fixed because the reminder only mentioned a review.
Dr Shah | The booking helps us prepare, but it does not replace listening to a new concern or assessing it.
Morgan | That helps. I did not want the form to make this look like an entirely administrative [[priority::Priority identifies what needs attention first rather than what happens to be written on a booking.]].
Dr Shah | Let us keep all three items visible. Tell me first when the tiredness began and how it affects you.
Morgan | I am struggling with ordinary tasks. I suppose that is a [[functional limitation::Functional limitation describes difficulty with usual activities rather than a diagnosis by itself.]].
Dr Shah | Exactly. Describe those tasks in your own words; I do not need you to use a clinical label.
Morgan | Can we still review the [[long-term condition::A long-term condition is an ongoing health issue requiring continuing care and review.]] rather than losing that appointment altogether?
Dr Shah | Yes, we will account for it in the plan. First I need enough information to assess today's priorities.
Morgan | I appreciate that [[signposting::Signposting tells the listener which part of the conversation comes next and why.]]. I understand why you are asking about the tiredness now.
Dr Shah | After that assessment, we can agree what to complete today and how to address anything left unfinished.
Morgan | A specific [[follow-up visit::A follow-up visit provides an agreed later encounter for review or unfinished care.]] would help more than being told to call sometime.
Dr Shah | We will make the purpose clear and explain how to obtain help if the situation changes before then.
Morgan | So [[safety-netting::Safety-netting explains changes that require further help and the route for obtaining it.]] is part of the plan, not a promise that nothing will happen.
Dr Shah | Correct. We also need to clarify the form's requirements before promising what I can certify.
Morgan | Then our [[shared agenda::A shared agenda reflects both the patient's concerns and the clinician's assessed priorities.]] begins with the tiredness, while the review and form remain visible.
Dr Shah | That captures your preference. I will assess the concern before we settle the clinical order and next steps.
Morgan | Good. I want [[continuity of care::Continuity of care connects this visit with ongoing review instead of treating every concern as unrelated.]], not three disconnected conversations in which the details get lost.''',
    rehearsal=['Read the corrected agenda exchange. Stress tiredness, review, and work form as three separate concerns.', 'Swap roles. Repeat the signposting lines and the distinction between a proposed agenda and assessed priorities.'],
    transfer_title='Keep a second concern visible', transfer_setup='Patient Lee attends a blood-pressure review and raises a new sleep concern. Dr Chen will clarify the sleep concern before agreeing on priorities. A travel form remains unfinished.',
    transfer='''Dr Chen: "The planned visit is a blood-pressure ___." | review | The planned appointment is the review named in the scenario.
Lee: "I also want to discuss my ___." | sleep | Sleep is the new concern Lee raises during this encounter.
Dr Chen: "I will first ___ that concern." | clarify | Clarification comes before deciding the clinical priorities in this scenario.
Lee: "The travel form remains ___." | unfinished | The form has not been completed or removed from the plan.'''))

BOOK['units'].append(unit(
    title='Taking a precise symptom history', scene='Dizziness means different things',
    skill='Clarify a patient word and reconstruct a timeline without supplying the answer.',
    brief='Ari uses the word dizzy for episodes that began on Tuesday. Ari describes feeling about to faint, not the room spinning. Episodes are reported after standing, and their duration is not yet clear. Dr Cole has not established a cause. The task is to clarify the account and record relevant unknowns, not diagnose from one trigger or assume unmentioned symptoms are absent.',
    cast='Dr Cole | General practitioner\nAri | Patient',
    culture=('Let the description precede the label', 'A familiar word may mean different sensations to different people. Offer neutral clarification and preserve the person\'s wording before using professional shorthand.'),
    a='''When did the episodes begin according to Ari? | Tuesday | Before any date can be named | After a confirmed treatment change | During a completed admission | Tuesday is the onset Ari reports, not a date independently established by testing.
What sensation does Ari describe? | Feeling about to faint | The room definitely spinning | A confirmed seizure | No symptoms at all | The brief distinguishes Ari's near-faint feeling from room-spinning language.
What remains unclear? | Episode duration | Whether Ari used the word dizzy | Whether standing was mentioned | Whether Dr Cole has met Ari | Duration is specifically unresolved and should not be silently filled in.''',
    vocabulary='''onset | Time at which a symptom first began. | establish the reported onset
duration | Length of time a symptom or episode lasts. | clarify episode duration
frequency | How often a symptom or event occurs. | describe symptom frequency
trigger | Event or circumstance associated with starting a symptom. | identify a reported trigger
relieving factor | Circumstance associated with reducing a symptom. | ask about relieving factors
associated symptom | Another symptom occurring alongside the main symptom. | ask about associated symptoms
pertinent negative | Relevant absence established through questioning or assessment. | document a pertinent negative
progression | Change in a symptom or condition over time. | describe symptom progression
episodic | Occurring in separate periods rather than continuously. | describe episodic symptoms
persistent | Continuing rather than resolving between distinct episodes. | report persistent discomfort
location | Place in the body where a symptom is experienced. | specify the symptom location
radiation | Spread of a symptom such as pain to another area. | describe pain radiation
character | Quality of a symptom, such as pressure or burning. | clarify symptom character
severity | Degree or intensity of a symptom or condition. | assess symptom severity
chronology | Order in which events occurred over time. | preserve the chronology
review of systems | Structured questioning about symptoms across body systems. | conduct a focused review of systems
history of present illness | Organized account of the current clinical problem. | summarize the history of present illness
diagnostic uncertainty | Lack of a sufficiently established explanation for the condition. | communicate diagnostic uncertainty''',
    precision='A reported trigger is not a demonstrated cause. Dizziness, vertigo, and feeling faint should not be substituted for one another without clarification.',
    precision_extra='Not asked, not reported, and denied are different. Record an unanswered duration question as unanswered, not as a normal or reassuring duration.',
    phrases='''Clarify a label | What does dizzy feel like for you?
Offer a neutral distinction | Is it spinning, feeling faint, or something different?
Locate the onset | When did you first notice it?
Separate two times | Is that the length of one episode or the time since it began?
Avoid a supplied answer | Describe what happens next in your own words.
Keep a gap visible | We have not yet clarified how long each episode lasts.
Attribute the trigger | You report noticing it after standing.
Summarize carefully | I have the sequence; I have not established the cause.''',
    notes='''Since versus for | Since introduces a starting point; for introduces a duration. Since Tuesday does not tell us how long one episode lasts.
When versus why | A when question asks about timing; it does not establish why the symptom happens.
Not yet clarified | Names missing information without converting it into an absent symptom.''',
    d='''Which sentence distinguishes onset from duration? | Episodes began Tuesday; the length of each is still unclear. | Each episode has lasted continuously since Tuesday. | Tuesday proves a cause. | Duration has been measured already. | Tuesday gives the onset; stating that episode length is unclear preserves the unresolved duration.
Which phrase overstates the evidence? | Standing definitely caused the condition. | Ari reports symptoms after standing. | The cause is not established. | Ari describes feeling faint. | An association in the history does not by itself demonstrate causation.
Which question is least leading? | What happens during an episode? | It is just stress, correct? | You never have any other symptoms, right? | You agree this is harmless, yes? | The open question invites Ari's account without embedding an unsupported conclusion.
What is a pertinent negative? | A relevant absence established by asking or assessing | Any symptom not mentioned spontaneously | A blank record field | A clinician's guess about what is unlikely | An unmentioned symptom cannot be documented as denied without an appropriate question or assessment.''',
    dialogue='''Dr Cole | You used the word dizzy on the appointment request. What does that feel like for you?
Ari | More like I might faint than like the room is spinning. The [[onset::Onset identifies when Ari first noticed the episodes rather than how long each episode lasts.]] was Tuesday.
Dr Cole | Thank you. Did you feel it continuously from Tuesday, or have there been separate episodes?
Ari | Separate episodes. I suppose [[episodic::Episodic means the sensation occurs in separate periods rather than continuously all the time.]] describes it, but I cannot time them accurately yet.
Dr Cole | That is useful to know. How often have you noticed it, and what are you doing when it starts?
Ari | Standing up seems to be a [[trigger::A trigger is a circumstance associated with starting the symptom, not proof of its underlying cause.]], although I have not kept a record of every episode.
Dr Cole | I will record that as your observation. What happens next, and what makes the feeling ease?
Ari | Sitting down seems to help. That is the main [[relieving factor::A relieving factor is something the patient reports as reducing the sensation during an episode.]] I have noticed.
Dr Cole | When you say it lasts a while, do you mean seconds, minutes, or something you cannot estimate?
Ari | I cannot estimate the [[duration::Duration is the length of a single episode, which remains unclear in this history.]]. I do not want to give you a number just to complete the question.
Dr Cole | Please do not guess. I will ask about other symptoms separately rather than treating silence as an answer.
Ari | So an [[associated symptom::An associated symptom occurs alongside the main concern and needs its own accurate history.]] is something else happening during the same episode?
Dr Cole | Yes. I also need to understand any changes and how the episodes affect what you can do.
Ari | The [[frequency::Frequency tells us how often episodes occur, separate from onset, severity, or the length of one episode.]] may be increasing, but I should explain what I actually remember.
Dr Cole | Exactly. Start with Tuesday and describe the later events in order, including anything that is uncertain.
Ari | That will keep the [[chronology::Chronology preserves the order of reported events without rearranging them to fit a presumed explanation.]] straight instead of mixing the first episode with the most recent one.
Dr Cole | I will summarize your account, then assess it. The standing association alone does not establish a diagnosis.
Ari | I understand the [[diagnostic uncertainty::Diagnostic uncertainty means the cause is not established, even though the symptom account is becoming clearer.]]. You are listening to the pattern, not promising an explanation yet.
Dr Cole | Correct. Any relevant absence I record will come from a question or assessment, not from an empty field.
Ari | Then a [[pertinent negative::A pertinent negative is a relevant absence established through questioning or assessment, not through silence.]] is different from something I simply have not mentioned.''',
    rehearsal=['Read Ari\'s corrected symptom history. Contrast onset, duration, and frequency with clear stress.', 'Swap roles. Repeat the neutral clarification question and the summary that preserves diagnostic uncertainty.'],
    transfer_title='Separate the first day from episode length', transfer_setup='Jamie reports intermittent tingling beginning Friday. Individual episodes last about two minutes by Jamie\'s estimate. Dr Park has not established a cause.',
    transfer='''Dr Park: "The reported onset was ___." | Friday | Friday identifies when Jamie says the intermittent tingling first began.
Jamie: "One episode lasts about ___ minutes." | two | Two is Jamie's estimate of a single episode's duration.
Dr Park: "The symptoms are ___." | intermittent | Intermittent describes episodes that occur with intervals between them.
Dr Park: "The cause is not yet ___." | established | The scenario supplies a symptom account but no confirmed explanation.'''))

BOOK['units'].append(unit(
    title='Reconciling medicines without blame', scene='Two lists and an unfamiliar packet',
    skill='Investigate a medication discrepancy while separating actual use from recorded instructions.',
    brief='Robin brings a printed hospital list and a packet bought without a prescription. The clinic list differs from the hospital list. Dr Lin has not verified which instructions are current or whether products share an ingredient. Robin sometimes misses a medicine because of cost. No dose changes are supplied. The conversation must establish actual use, verify the conflicting records, and address the cost barrier without calling Robin noncompliant.',
    cast='Dr Lin | General practitioner\nRobin | Patient',
    culture=('Ask what happens, not whether someone obeys', 'A list records an instruction or history; it does not prove what the person takes. Ask about practical barriers in neutral language.'),
    a='''Which records differ? | The clinic and hospital lists | Two verified identical prescriptions | A completed laboratory report and scan | No records differ | The case explicitly identifies a discrepancy between the two medicine lists.
What barrier does Robin report? | Cost | A proven drug allergy | An instruction to stop every medicine | A completed dose adjustment | Robin reports missed medicine because of cost, not a verified clinical instruction.
What has not been verified? | Whether the products share an ingredient | Whether Robin brought a packet | Whether there is a printed list | Whether the clinic has a record | The case does not establish the contents or overlap of the products.''',
    vocabulary='''medication reconciliation | Comparing medicine information to resolve discrepancies across records and actual use. | perform medication reconciliation
medicine list | Record of medicines and their relevant instructions. | verify the medicine list
over-the-counter product | Product available without a prescription under local rules. | disclose over-the-counter products
active ingredient | Substance responsible for a medicine's intended pharmacological effect. | compare active ingredients
brand name | Commercial name used to market a product. | record the brand name
generic name | Standard nonproprietary name of a medicinal substance. | confirm the generic name
duplicate therapy | Unintended or unnecessary overlap between therapeutic products or treatments. | check for duplicate therapy
adherence | Extent to which actual medicine use matches an agreed plan. | discuss barriers to adherence
adverse reaction | Unwanted harmful response associated with a medicinal product. | describe an adverse reaction
drug allergy | Immune-mediated reaction to a medicine. | clarify a reported drug allergy
intolerance | Difficulty tolerating a medicine that is not necessarily an allergy. | distinguish intolerance from allergy
interaction | Effect of one substance or treatment on another. | assess a possible interaction
dosage form | Physical preparation in which a medicine is supplied. | verify the dosage form
route of administration | Path by which a medicine enters the body. | confirm the route of administration
discontinued medicine | Medicine recorded as no longer intended for use. | verify a discontinued medicine
record discrepancy | Difference between records requiring investigation or clarification. | resolve a record discrepancy
prescriber | Authorized professional issuing a medicine prescription. | contact the original prescriber
medication review | Structured evaluation of medicine use and related needs. | arrange a medication review''',
    precision='Do not treat a different brand name as proof of a different ingredient. Verify products and instructions before resolving the clinical question.',
    precision_extra='An adverse reaction, an intolerance, and an allergy are not interchangeable labels. Preserve the reported reaction and obtain the relevant clinical history.',
    phrases='''Ask about actual use | Walk me through what you actually take.
Normalize disclosure | Please include products bought without a prescription.
Name the discrepancy | These two lists do not match.
Avoid premature correction | I need to verify the current instructions first.
Ask about affordability | Has cost made the agreed plan difficult to follow?
Clarify a reaction | What happened when you took it?
Separate names | Different brand names can still contain the same ingredient.
Agree on verification | We will check the source before finalizing the list.''',
    notes='''Actually take | Distinguishes real use from instructions recorded elsewhere.
What happened | Elicits the reaction instead of confirming an assumed allergy.
Before finalizing | Identifies a verification step that must precede a settled record.''',
    d='''Which question avoids blame? | Has cost made the plan difficult to follow? | Why do you ignore doctors? | Why are you always noncompliant? | You chose to waste the medicine, correct? | Asking about cost explores a practical barrier without assuming motives or misconduct.
Which conclusion is unsupported? | Different brands prove different ingredients. | The lists differ. | The packet needs checking. | Robin reports a cost barrier. | Brand names alone do not establish the active ingredients or possible overlap.
Which distinction matters? | Actual use versus recorded instructions | Packet color versus appointment time only | Guess versus another guess | A prescription versus proof of adherence | Recorded instructions do not establish what a patient actually takes at home.
What should happen before finalizing the list? | Verification of conflicting information | Automatic deletion of the hospital list | An invented dose change | Recording every reaction as an allergy | Verification is needed because neither conflicting record has been established as current.''',
    dialogue='''Dr Lin | Please show me both lists, and include anything you buy yourself or take only occasionally.
Robin | I brought this [[over-the-counter product::An over-the-counter product is bought without a prescription and still belongs in a medicine review.]]. I did not think it belonged with my prescriptions.
Dr Lin | It matters too. First, tell me what you actually take rather than reading only the printed instructions.
Robin | My hospital [[medicine list::A medicine list records products and instructions but does not prove current actual use.]] differs from the clinic version, so I am uncertain which is current.
Dr Lin | We need to verify that difference. I will not silently choose one record because it looks newer.
Robin | Is this what you mean by [[medication reconciliation::Medication reconciliation compares records with actual use and resolves discrepancies rather than merely copying a list.]] rather than simply adding another packet to the computer?
Dr Lin | Yes. We will check the products, instructions, and sources, and establish which questions remain unresolved.
Robin | This packet has a different [[brand name::A brand name is a commercial product name and does not by itself identify a different medicinal ingredient.]]. Does that mean it cannot overlap with another medicine?
Dr Lin | Not necessarily. We need the ingredient information before drawing that conclusion or making a clinical decision.
Robin | Then we should compare the [[active ingredient::The active ingredient is the medicinal substance being compared to investigate possible product overlap.]], not rely on the appearance of the packaging.
Dr Lin | Correct. Also, how manageable has the agreed medicine plan been in everyday life?
Robin | Cost has affected my [[adherence::Adherence describes actual use in relation to the agreed plan and can be affected by practical barriers.]]. Sometimes I cannot afford to collect a medicine.
Dr Lin | Thank you for telling me. That is important information for planning care, not a reason to blame you.
Robin | I also described one medicine as an allergy, but I am unsure whether it was [[intolerance::Intolerance means difficulty tolerating a medicine and is not automatically an immune-mediated allergy.]].
Dr Lin | Tell me exactly what happened and when. We should preserve the reaction details before settling the label.
Robin | I understand. A recorded [[drug allergy::A drug allergy refers to an immune-mediated reaction and needs accurate history rather than an assumed label.]] should not be invented from an incomplete description.
Dr Lin | I will clarify the clinical history and contact the relevant source about the conflicting instructions.
Robin | Please make the [[record discrepancy::A record discrepancy is an unresolved difference between medicine records that needs verification.]] visible until it is resolved, so another person does not assume it was settled.
Dr Lin | Agreed. We have not decided any dose change in this discussion; that requires the appropriate clinical review.
Robin | Then today's [[medication review::The medication review evaluates actual use, product information, barriers, and unresolved clinical questions together.]] will include affordability as well as an accurate list.''',
    rehearsal=['Read the corrected review. Stress actually take, recorded instructions, and verify as distinct ideas.', 'Swap roles. Repeat the affordability question and the reaction-history question without adding blame or a dose change.'],
    transfer_title='Verify an old entry', transfer_setup='Taylor says an outside prescriber stopped one medicine, but the local list still includes it. Dr Noor will verify the instruction. The date is unknown; no new dose has been authorized.',
    transfer='''Taylor: "An outside ___ gave the instruction." | prescriber | The reported instruction comes from the outside prescriber in this case.
Dr Noor: "The local list still ___ the medicine." | includes | The unresolved local entry is explicitly described as still including the medicine.
Taylor: "The instruction date is ___." | unknown | The date has not been supplied and must not be guessed.
Dr Noor: "I will ___ the instruction." | verify | Verification is required before treating the reported instruction as settled.'''))

BOOK['units'].append(unit(
    title='Explaining an uncertain test result', scene='Outside the range is not the diagnosis',
    skill='Explain a result without equating a laboratory flag with a confirmed condition.',
    brief='Casey sees an out-of-range flag on a blood-test report before speaking with Dr Vega. No numerical value or diagnosis is supplied in this case. Dr Vega will review the result alongside symptoms, previous results, and sample context. A repeat test is being considered, not yet ordered. Casey fears that the flag means a serious diagnosis is certain.',
    cast='Dr Vega | General practitioner\nCasey | Patient',
    culture=('Explain the flag before offering reassurance', 'A patient may encounter technical results before receiving an explanation. Acknowledge the uncertainty and explain the review process without promising that a flagged result is harmless.'),
    a='''What has Casey seen? | An out-of-range flag | A confirmed diagnosis supplied in this case | A completed repeat test | A treatment response | The brief supplies a laboratory flag but no confirmed diagnosis or numerical value.
What is the repeat-test status? | Under consideration | Already performed | Already normal | Definitely unnecessary | A repeat is being considered and has not yet been ordered.
What will Dr Vega use alongside the result? | Symptoms, previous results, and sample context | The flag color alone | A guess from the patient portal | A diagnosis invented for the exercise | Interpretation requires the stated clinical and sample context, not the flag alone.''',
    vocabulary='''laboratory result | Reported outcome of a test on a specimen. | interpret a laboratory result
reference interval | Range used by a laboratory for comparison with a result. | explain the reference interval
out-of-range flag | Indicator that a result lies outside a stated comparison range. | review an out-of-range flag
trend | Pattern of change across comparable observations over time. | examine the result trend
baseline | Earlier or usual state used for comparison. | compare with the baseline
preanalytical variation | Differences arising before a sample is analyzed. | review preanalytical variation
false-negative result | Negative test result when the target condition is actually present. | explain a false-negative result
false-positive result | Positive test result when the target condition is actually absent. | explain a false-positive result
repeat sample | New specimen obtained to repeat an investigation. | request a repeat sample
incidental finding | Finding discovered outside the main purpose of an investigation. | explain an incidental finding
clinical significance | Meaning or importance of a finding for patient care. | assess clinical significance
differential diagnosis | Set of possible explanations being evaluated clinically. | discuss the differential diagnosis
working diagnosis | Provisional explanation guiding assessment or care. | qualify a working diagnosis
confirmatory test | Investigation used to help establish a suspected finding. | discuss a confirmatory test
sensitivity | Ability of a test to identify people with the target condition. | explain test sensitivity
specificity | Ability of a test to identify people without the target condition. | explain test specificity
predictive value | How strongly a result predicts the target condition in its context. | discuss predictive value
pending result | Test outcome that has not yet become available. | track a pending result''',
    precision='Outside a reference interval is not a diagnosis. Normal, negative, and no further action are also different statements, each requiring context.',
    precision_extra='A possible repeat is not an order, and an order is not a completed result. Keep the stage of the investigation explicit.',
    phrases='''Acknowledge the worry | Seeing a flag before an explanation can be unsettling.
Explain the marker | The flag shows how the result compares with the laboratory range.
Limit the conclusion | The flag alone does not establish a diagnosis.
Bring in context | I will compare it with your symptoms and previous results.
State a proposal | A repeat is one option under consideration.
Avoid false reassurance | I cannot call it harmless before reviewing the context.
Clarify status | No repeat has been ordered yet.
Check the meaning | What does the flag mean to you after that explanation?''',
    notes='''Does not establish | Limits a conclusion without claiming that the opposite has been proved.
Under consideration | Describes a proposal rather than a completed clinical action.
Compared with | Introduces the reference used to interpret a result or trend.''',
    d='''Which explanation is accurate? | The flag needs clinical context. | Every flag confirms serious disease. | Every flag is harmless. | The portal color decides treatment. | A laboratory comparison marker cannot replace interpretation in the person's clinical context.
Which statement preserves action status? | A repeat is being considered but has not been ordered. | A repeat was completed. | The repeat was normal. | A repeat has ruled out disease. | The proposed test has not advanced to an order or completed result.
Which reassurance is unsupported? | There is definitely nothing to worry about. | We will review the symptoms. | The flag is not itself a diagnosis. | Previous results may provide context. | The case supplies no basis for guaranteeing that the result has no clinical importance.
What is a working diagnosis? | A provisional explanation | Every abnormal test | An administrative flag | Proof that no further review is needed | A working diagnosis remains provisional and may change as evidence develops.''',
    dialogue='''Casey | The portal highlighted my blood result. I saw the warning before anyone explained what it meant.
Dr Vega | I understand why the [[out-of-range flag::An out-of-range flag compares a result with a stated interval without establishing a diagnosis.]] worried you. Let us separate the marker from its clinical meaning.
Casey | Does outside the range mean that I definitely have the condition I read about online?
Dr Vega | Not by itself. The [[reference interval::A reference interval is a laboratory comparison range, not a stand-alone diagnosis for an individual patient.]] helps comparison, but we must interpret the result in context.
Casey | What context do you need before you can tell me more about this particular result?
Dr Vega | Your symptoms, earlier results, and the sample circumstances help us assess its [[clinical significance::Clinical significance concerns what the finding means for care, beyond whether the laboratory flagged it.]].
Casey | I remember having the same test previously. Will you compare those reports rather than only this one?
Dr Vega | Yes, where they are comparable. A [[trend::A trend is the pattern across comparable results over time rather than one isolated flagged value.]] can add information that one isolated result cannot provide.
Casey | I do not know whether the earlier value was typical for me or just another unusual day.
Dr Vega | We should not assume it is your [[baseline::A baseline is an earlier or usual state used for comparison and must be established appropriately.]] without reviewing the relevant history and circumstances.
Casey | Could something about the sample affect the result, or would that just be an excuse to ignore it?
Dr Vega | Sample context can matter. Reviewing [[preanalytical variation::Preanalytical variation concerns differences arising before analysis, which may be relevant without proving an error occurred.]] does not mean declaring that the laboratory made an error.
Casey | Are you ordering the test again now, or is that only something we might discuss?
Dr Vega | A [[repeat sample::A repeat sample would be a new specimen for another test; here it remains a possibility rather than an order.]] is under consideration. I have not ordered it in this discussion.
Casey | So there is no new result waiting somewhere that I have failed to look at?
Dr Vega | Correct. A [[pending result::A pending result belongs to an investigation whose outcome is not yet available, not to a test merely being considered.]] would be a different situation from considering whether to repeat the test.
Casey | I would rather hear that something is uncertain than be reassured today and surprised tomorrow.
Dr Vega | That is reasonable. A [[working diagnosis::A working diagnosis is a provisional explanation and should be distinguished from a confirmed conclusion.]] must be described as provisional while we evaluate the evidence.
Casey | I understand the difference now: the flag needs review, but it is not the diagnosis itself.
Dr Vega | Exactly. We will explain the plan, including whether a [[confirmatory test::A confirmatory test helps establish a suspected finding when clinically appropriate; none is automatically required by a flag alone.]] is appropriate and who will communicate any subsequent result.''',
    rehearsal=['Read the corrected results discussion. Contrast flag, interpretation, and diagnosis.', 'Swap roles. Repeat the lines distinguishing a possible repeat, an order, and a pending result.'],
    transfer_title='A result still awaiting review', transfer_setup='Sam sees a report in the portal. Dr Ames has received it but has not completed the clinical review. The report is available; its clinical meaning and next action remain to be discussed.',
    transfer='''Sam: "The report is now ___." | available | The portal report exists and can be seen in this scenario.
Dr Ames: "The clinical review is not ___." | completed | Receiving a report does not mean its clinical review has been completed.
Sam: "A visible result is not a confirmed ___." | diagnosis | The scenario provides a report but does not establish a diagnosis.
Dr Ames: "We still need to discuss the next ___." | action | The next clinical action remains unresolved in the supplied facts.'''))

BOOK['units'].append(unit(
    title='Responding to an antibiotic request', scene='A recommendation without a dismissal',
    skill='Explain an assessed recommendation while acknowledging the expectation behind a treatment request.',
    brief='After an assessment, Dr Rao has not identified an indication for an antibiotic in this fictional visit. Jules expected one because a previous illness improved after antibiotics. The case does not provide diagnostic findings, a named infection, or medicine instructions. The conversation explains the current recommendation, distinguishes sequence from proof of benefit, and includes an individualized follow-up and safety-net discussion with the actual clinician.',
    cast='Dr Rao | General practitioner\nJules | Patient',
    culture=('Acknowledge the expectation before explaining disagreement', 'The patient may be asking for relief, reassurance, or a way to return to work. Address that need without promising an unnecessary treatment or making the conversation a contest.'),
    a='''What is the supplied recommendation based on? | Dr Rao's assessment in this visit | A universal ban on antibiotics | Jules's employer deciding treatment | A laboratory value invented by the learner | The case states an assessed recommendation without supplying a general prescribing rule.
Why did Jules expect an antibiotic? | A previous illness improved after antibiotics | A new prescription already issued | A confirmed allergy | A completed hospital admission today | Jules connects improvement in an earlier illness with having taken antibiotics.
What is not supplied? | A named diagnosis or medicine instruction | A patient expectation | A clinician recommendation | A previous experience | The dialogue must not invent diagnostic findings or medicine instructions absent from the case.''',
    vocabulary='''antibiotic stewardship | Responsible use of antibiotics to preserve benefit and limit avoidable harm. | support antibiotic stewardship
antibiotic | Medicine used against susceptible bacterial infections. | discuss an antibiotic recommendation
viral illness | Illness caused by a virus. | explain a viral illness
bacterial infection | Infection caused by bacteria. | assess a suspected bacterial infection
self-limiting illness | Illness that can resolve without a treatment directed at its cause. | explain a self-limiting illness
symptom relief | Reduction of an uncomfortable symptom. | discuss symptom relief
antimicrobial resistance | Ability of microbes to withstand medicines intended to act against them. | reduce antimicrobial resistance
treatment indication | Clinical reason supporting use of a particular treatment. | establish a treatment indication
watchful waiting | Planned observation with defined reassessment rather than immediate intervention. | explain watchful waiting
return precautions | Instructions about changes requiring further medical attention. | explain return precautions
therapeutic relationship | Working relationship supporting care between clinician and patient. | maintain the therapeutic relationship
treatment expectation | What a patient anticipates receiving or achieving from treatment. | explore the treatment expectation
expected benefit | Improvement a treatment may produce in a relevant situation. | explain the expected benefit
potential harm | Possible adverse consequence of an action or treatment. | discuss potential harm
reassessment | Further evaluation after time or a change in circumstances. | arrange clinical reassessment
examination finding | Observation established through a clinical examination. | explain an examination finding
diagnostic threshold | Evidence level used in deciding whether a diagnosis is sufficiently supported. | clarify a diagnostic threshold
contingency plan | Agreed response if the situation develops differently from expected. | agree on a contingency plan''',
    precision='Improvement after a medicine does not, by itself, prove improvement because of the medicine. The current recommendation belongs to this assessed encounter.',
    precision_extra='Not prescribing an antibiotic is not the same as offering no care. Actual symptom advice, reassessment arrangements, and warning signs must come from the treating clinician, not an invented exercise protocol.',
    phrases='''Acknowledge experience | I can see why your previous experience shaped your expectation.
State the recommendation | Based on today's assessment, I am not recommending an antibiotic.
Explain the distinction | Improving afterward does not prove the medicine caused the improvement.
Keep the need visible | Your need for relief still matters.
Invite the concern | What worries you most about this recommendation?
Avoid a contest | Let us focus on what is likely to help in this situation.
Explain ongoing care | We still need an appropriate plan for symptoms and follow-up.
Check the contingency | Let us confirm what changes mean you should seek further help.''',
    notes='''After versus because of | After gives sequence; because of asserts a cause. They are not interchangeable evidence claims.
Based on today's assessment | Locates the recommendation in this encounter rather than presenting an absolute rule.
Still matters | Acknowledges the patient's goal even when the requested treatment is not recommended.''',
    d='''Which sentence explains the recommendation respectfully? | I understand the expectation; today's assessment does not support an antibiotic. | Antibiotics never help anyone. | Your previous experience is imaginary. | I will prescribe one to end the discussion. | Acknowledging the expectation respects experience while retaining the recommendation based on today's assessment.
Which inference is unjustified? | Improvement afterward proves that antibiotics caused it. | Jules expected treatment. | Dr Rao assessed the patient. | The current recommendation differs from the expectation. | Timing alone cannot establish that a medicine caused an earlier recovery.
What does no antibiotic mean here? | That particular treatment is not recommended | No further care is allowed | No reassessment can ever be needed | Every future infection is viral | The recommendation concerns this treatment in this assessed visit, not all care or future illness.
Which closing is most useful? | Confirm the individualized follow-up and warning-sign plan. | Call only if you can prove a diagnosis. | Nothing can change after today. | Ignore all new symptoms. | A clear follow-up and safety-net plan supports care without promising that circumstances cannot change.''',
    dialogue='''Jules | Last time I felt like this, antibiotics helped. I expected to leave with the same treatment today.
Dr Rao | I understand that [[treatment expectation::Treatment expectation describes what Jules anticipated based on a previous experience, not an indication established today.]]. Based on today's assessment, I am not recommending an antibiotic.
Jules | Are you saying the improvement last time was not real? I remember feeling much better afterward.
Dr Rao | The improvement was real to you. But improvement afterward does not establish the medicine's [[expected benefit::Expected benefit concerns what a treatment may actually achieve, which cannot be proved by timing alone.]] in this situation.
Jules | I mainly need to feel better and get back to work. I do not want to be dismissed.
Dr Rao | Your need for [[symptom relief::Symptom relief means reducing discomfort and remains a care goal even when an antibiotic is not indicated.]] matters. Not recommending this medicine is not the same as offering no care.
Jules | Then please explain what separates my request from a clinical reason to prescribe the medicine.
Dr Rao | A [[treatment indication::A treatment indication is a clinical reason supporting a particular treatment, not simply a request or past timing.]] depends on the current assessment and evidence, not only on an earlier prescription.
Jules | Is the concern just about avoiding unnecessary cost, or can an unnecessary medicine cause problems too?
Dr Rao | There can be [[potential harm::Potential harm means possible adverse consequences that belong in a balanced treatment explanation.]], as well as a lack of benefit. We should discuss that honestly without overstating either.
Jules | I have heard people say their bodies become resistant. Is that the right way to describe it?
Dr Rao | [[Antimicrobial resistance::Antimicrobial resistance concerns microbes withstanding medicines, not a person's body becoming resistant to care.]] concerns microbes that withstand medicines. It is not your body becoming resistant to treatment.
Jules | I follow that distinction. I still want to know what happens if the illness does not develop as expected.
Dr Rao | That needs a clear [[contingency plan::A contingency plan describes what to do if the situation changes rather than assuming the initial course will continue.]], including the appropriate route for further help and reassessment.
Jules | Please make that specific to me rather than just saying to come back if I am worried.
Dr Rao | We will discuss individualized [[return precautions::Return precautions identify changes requiring further medical attention and must be provided for the actual clinical situation.]] and check that the instructions and contact route are clear.
Jules | Then a later review would not mean that I had failed to follow today's recommendation?
Dr Rao | Correct. [[Reassessment::Reassessment is a further clinical evaluation when time or changed circumstances makes it appropriate.]] responds to the clinical situation; it is not a judgment about you.
Jules | I can accept a different recommendation when I understand the reasoning and know the next step.
Dr Rao | That is the aim of [[antibiotic stewardship::Antibiotic stewardship supports appropriate use while retaining attention to benefit, harm, and the patient's care needs.]] alongside good care: explain the decision, address your needs, and keep follow-up clear.''',
    rehearsal=['Read the corrected recommendation. Stress after and because of to distinguish sequence from cause.', 'Swap roles. Repeat the acknowledgment, recommendation, and follow-up lines without turning them into a prescribing rule.'],
    transfer_title='Explain a different treatment expectation', transfer_setup='Noor requests a scan because a relative received one. Dr Hale has assessed Noor and does not recommend that scan at this visit. The relative\'s case is not available. Follow-up remains part of care.',
    transfer='''Noor: "My ___ received a scan." | relative | The request is influenced by a relative's experience, not a supplied scan indication.
Dr Hale: "Your assessment does not support that scan ___." | today | The recommendation belongs to today's assessed encounter, not every future situation.
Noor: "The other person's clinical details are ___." | unavailable | The scenario does not supply the relative's history or reasons for imaging.
Dr Hale: "We still need clear ___." | follow-up | Not recommending the requested scan does not remove the need for appropriate follow-up.'''))

BOOK['units'].append(unit(
    title='Discussing preventive screening choices', scene='An invitation is not a diagnosis',
    skill='Compare screening benefits and limitations while preserving a voluntary, informed choice.',
    brief='Dana receives a screening invitation and asks Dr Ellis whether it means a disease is suspected. The invitation is not a diagnostic result. Eligibility and the appropriate options need an individual review; no screening schedule or personal risk calculation is supplied. Dana wants to understand possible benefit, false alarms, and subsequent testing before choosing.',
    cast='Dr Ellis | General practitioner\nDana | Patient',
    culture=('Discuss the tradeoff without steering through fear', 'Explain what a screening test can and cannot establish. A useful discussion includes the person\'s priorities and practical implications, not just a slogan that testing is always better.'),
    a='''What prompted the discussion? | A screening invitation | A confirmed diagnosis | A completed biopsy | A treatment complication | The supplied document is an invitation rather than a result or diagnosis.
What does Dana want explained? | Benefits, false alarms, and subsequent testing | A guaranteed outcome | An invented personal risk score | A diagnosis without assessment | Dana asks about the tradeoffs and next steps before deciding.
What is not supplied? | An individual screening schedule | Dana's questions | The invitation | A request for explanation | The exercise does not establish eligibility, an interval, or an individual clinical recommendation.''',
    vocabulary='''screening | Testing intended to identify possible disease or risk before relevant symptoms prompt diagnosis. | discuss screening options
diagnostic testing | Investigation intended to establish or explain a suspected clinical condition. | distinguish diagnostic testing
average risk | Risk category without specified factors that would place someone in a higher category. | assess average-risk eligibility
shared decision-making | Combining evidence and patient priorities in a care decision. | support shared decision-making
absolute risk | Chance of an outcome over a stated period in a defined group. | explain absolute risk
relative risk | Risk in one group compared with risk in another group. | distinguish relative risk
false alarm | Result suggesting a problem that further investigation does not confirm. | explain a possible false alarm
overdiagnosis | Detection of a condition that would not have caused harm during a person's lifetime. | discuss overdiagnosis
eligibility | Whether a person meets the criteria for an option or service. | review screening eligibility
prevention | Action aimed at reducing disease occurrence or its consequences. | discuss preventive care
asymptomatic | Without the relevant symptoms being considered. | describe an asymptomatic population
positive screen | Screening result indicating that further evaluation may be needed. | explain a positive screen
screening interval | Time between planned screening episodes. | review the screening interval
risk factor | Characteristic associated with a change in likelihood of an outcome. | identify a relevant risk factor
family history | Health information about a person's biological relatives. | update the family history
informed choice | Decision made with adequate understanding of relevant options and consequences. | support an informed choice
decision aid | Resource helping a person compare care options and their tradeoffs. | use a decision aid
follow-up test | Further investigation after an earlier test or finding. | explain a follow-up test''',
    precision='Screening and diagnostic testing serve different purposes. A screening invitation is not evidence that disease has been detected.',
    precision_extra='A risk percentage needs an outcome, time period, and comparison group. Do not invent those details or use a relative change as though it were an absolute chance.',
    phrases='''Explain the invitation | This invites a discussion; it does not announce a diagnosis.
Separate purposes | Screening and testing a symptom are different situations.
Explain an uncertain result | A positive screen may lead to further evaluation.
Name the tradeoff | We should discuss possible benefit as well as false alarms.
Ask about priorities | Which parts of the decision matter most to you?
Clarify a number | Over what time period does that risk apply?
Protect choice | You can ask questions before deciding.
Review eligibility | We need to check which options fit your circumstances.''',
    notes='''May lead to | Describes a possible consequence rather than an inevitable result.
Rather than | Makes the contrast between screening and diagnosis explicit.
Over what period | Requests a missing time horizon needed to interpret a risk statement.''',
    d='''What does the invitation establish? | An opportunity to discuss screening | A diagnosis | A positive result | A guarantee of eligibility for every test | The invitation itself does not establish disease, results, or universal eligibility.
Which explanation of a positive screen is safest? | It may require further evaluation; it is not automatically a diagnosis. | It always proves disease. | It always proves a laboratory mistake. | It never changes care. | Screening results require appropriate interpretation and may lead to diagnostic evaluation.
Which risk statement is incomplete? | The risk is lower, without an outcome or time period. | The invitation is not a result. | Dana has questions about tradeoffs. | Eligibility needs review. | A meaningful risk comparison requires the event, population, and time period being compared.
What supports informed choice? | Explain benefits, limitations, and next steps, then elicit priorities. | Hide false alarms to increase participation. | Treat every question as refusal. | Promise that screening prevents every illness. | An informed choice requires relevant information and attention to the person's priorities.''',
    dialogue='''Dana | This letter invited me for screening. Does that mean someone thinks I already have the disease?
Dr Ellis | An invitation to [[screening::Screening seeks possible disease or risk and an invitation does not itself establish a diagnosis.]] does not announce a diagnosis. Let us review what the invitation offers.
Dana | I do not have the symptom mentioned in an article I read. Is that a contradiction?
Dr Ellis | Not necessarily. Screening often concerns an [[asymptomatic::Asymptomatic means without the relevant symptoms, which is different from proving that no condition is present.]] population; investigating a symptom is a different clinical situation.
Dana | Then the test in this letter is not the same as testing to explain a current complaint?
Dr Ellis | Correct. [[Diagnostic testing::Diagnostic testing seeks to establish or explain a suspected clinical condition rather than merely inviting a screening discussion.]] and screening have different purposes, although one can lead to the other.
Dana | Before deciding, I want to know what a worrying result would mean and what would happen afterward.
Dr Ellis | A [[positive screen::A positive screen indicates a possible concern requiring evaluation and is not automatically a confirmed diagnosis.]] may lead to further evaluation. It does not automatically confirm the condition.
Dana | Could I go through more tests and then discover that the original concern was not confirmed?
Dr Ellis | Yes, a [[false alarm::A false alarm suggests a problem that subsequent investigation does not confirm, one possible limitation to discuss.]] is one limitation to explain alongside the possible benefits and other consequences.
Dana | People also talk about finding conditions that would never have affected them. Is that the same issue?
Dr Ellis | That is [[overdiagnosis::Overdiagnosis is detecting a condition that would not have caused harm during the person's lifetime, distinct from a false alarm.]], which differs from a false alarm. We should explain the distinction without assuming either will happen to you.
Dana | I would like the numbers explained carefully. A headline saying lower risk does not tell me much.
Dr Ellis | We need the event and time period. [[Absolute risk::Absolute risk describes the chance of an outcome over a defined period, rather than only a ratio between groups.]] is not the same thing as a relative comparison.
Dana | And you still need to check whether this particular screening option applies to my circumstances?
Dr Ellis | Yes. We must review [[eligibility::Eligibility means meeting the criteria for the relevant option and is not established solely by reading a general invitation.]] and your history rather than treating a general invitation as the entire assessment.
Dana | I want to compare the options without feeling that asking about limitations means I am refusing care.
Dr Ellis | Questions support [[shared decision-making::Shared decision-making combines relevant evidence with the person's priorities rather than substituting pressure for discussion.]]. Your priorities and the evidence both belong in the discussion.
Dana | That gives me a clearer starting point. I understand this is an invitation, not a diagnosis or a guarantee.
Dr Ellis | Exactly. We can use the relevant information to support an [[informed choice::An informed choice follows an adequate explanation of options and consequences and respects the person's decision.]], then agree on any next step.''',
    rehearsal=['Read the corrected screening exchange. Contrast screening, positive screen, and diagnosis.', 'Swap roles. Repeat the distinction between false alarm and overdiagnosis, preserving the uncertainty.'],
    transfer_title='Clarify a population statistic', transfer_setup='A leaflet gives a risk comparison for a defined study population over five years. Kim asks whether it is a personal prediction. Dr Reed explains that individual interpretation requires clinical context.',
    transfer='''Kim: "The leaflet describes a study ___." | population | The figure concerns a defined study group, not a guaranteed individual outcome.
Dr Reed: "Its time horizon is five ___." | years | Five years is the explicit period attached to the comparison.
Kim: "It is not a guaranteed personal ___." | prediction | A population statistic does not determine exactly what will happen to Kim.
Dr Reed: "Individual interpretation needs clinical ___." | context | The scenario states that personal interpretation requires the relevant clinical circumstances.'''))

BOOK['units'].append(unit(
    title='Opening a mental-health conversation', scene='Make a direct question feel safe',
    skill='Ask sensitively about mood and safety while explaining confidentiality limits and a warm handoff.',
    brief='Chris reports low mood and poor sleep affecting work. Dr Wells will ask about safety directly rather than infer it from appearance. No risk assessment has been completed and no risk level is supplied. A behavioral-health colleague is available for an introduction if appropriate and agreed. Dr Wells must explain relevant confidentiality limits accurately rather than promise absolute secrecy.',
    cast='Dr Wells | General practitioner\nChris | Patient',
    culture=('Direct can also be compassionate', 'A clear safety question need not be abrupt. Explain why you are asking, listen without judgment, and avoid making disclosure sound like a test the patient can fail.'),
    a='''What impact does Chris report? | Mood and sleep difficulties affecting work | A completed diagnosis in this case | A known low risk level | A refusal of all help | The case describes reported difficulties and their effect, not a completed diagnosis.
What remains incomplete? | The risk assessment | The appointment booking | Chris mentioning sleep | The colleague's availability | No risk assessment or risk level has been established in the brief.
What must not be promised? | Absolute secrecy | Respectful listening | An explanation of next steps | Attention to the reported difficulties | Confidentiality has limits that depend on the actual situation and applicable requirements.''',
    vocabulary='''low mood | Persistent or recurrent feelings of sadness or reduced emotional well-being. | explore low mood
anhedonia | Reduced ability to experience interest or pleasure. | ask about anhedonia
sleep disturbance | Disruption of the usual pattern or quality of sleep. | describe sleep disturbance
stressor | Circumstance placing psychological or practical demands on a person. | identify a current stressor
protective factor | Circumstance or resource that may reduce vulnerability to harm. | explore protective factors
risk assessment | Clinical evaluation of relevant risks and protective circumstances. | complete a risk assessment
suicidal thoughts | Thoughts about ending one's own life. | ask directly about suicidal thoughts
psychosocial history | Account of psychological and social circumstances relevant to care. | take a psychosocial history
nonjudgmental language | Wording that explores experience without assigning blame or moral fault. | use nonjudgmental language
behavioral health | Care addressing mental health, behavior, and related well-being. | coordinate behavioral-health care
warm handoff | Supported introduction to another care professional with relevant context. | arrange a warm handoff
confidentiality limit | Circumstance in which privacy cannot be guaranteed under applicable duties. | explain confidentiality limits
crisis response | Immediate professional response to an urgent safety concern. | activate the appropriate crisis response
distress | Significant emotional suffering or discomfort. | acknowledge distress
daily functioning | Ability to manage ordinary work, self-care, and other activities. | assess daily functioning
support network | People or services available to provide help. | identify a support network
consent to share | Agreement to disclose specified information in an appropriate context. | clarify consent to share
therapeutic alliance | Collaborative relationship supporting care and agreed goals. | strengthen the therapeutic alliance''',
    precision='A calm appearance does not establish low risk. Ask and assess directly; do not let an English exercise stand in for an actual safety evaluation.',
    precision_extra='A warm handoff is more than passing along a telephone number. Explain the introduction and information sharing, following actual consent and safety requirements.',
    phrases='''Open sensitively | How have things been emotionally as well as physically?
Ask directly | Have you had thoughts about ending your life?
Explain the question | I ask directly because your safety matters.
Avoid an assumption | I cannot judge that from how you look today.
Explain privacy limits | I will explain when I may need to involve others for safety.
Offer an introduction | We can discuss an introduction to our behavioral-health colleague.
Clarify information sharing | Let us agree what information is shared, within the applicable duties.
Keep the person involved | I will explain the next steps as clearly as I can.''',
    notes='''Have you had | The present perfect invites experience over a relevant period rather than assuming a current answer.
May need to | Explains a possible duty without promising secrecy or announcing a decision already made.
From how you look | Identifies an inadequate basis for a risk conclusion.''',
    d='''Which safety question is direct and neutral? | Have you had thoughts about ending your life? | You would never do anything foolish, would you? | You look fine, so there is no risk. | Can we skip this uncomfortable topic? | The direct question invites an honest answer without shame or an assumed conclusion.
Which privacy statement is inappropriate? | I promise absolute secrecy in every circumstance. | We should discuss confidentiality limits. | I will explain relevant information sharing. | Your questions about privacy matter. | Absolute secrecy may conflict with applicable safety and legal duties.
What does a warm handoff add? | A supported introduction with relevant context | A guaranteed cure | A completed risk assessment by definition | An automatic disclosure of everything | A warm handoff connects care while preserving appropriate consent and information boundaries.
Which inference must be avoided? | A calm appearance proves low risk. | Chris reports poor sleep. | Work is affected. | Assessment is still needed. | Appearance alone cannot establish a person's safety or replace a risk assessment.''',
    dialogue='''Dr Wells | You mentioned poor sleep and difficulty at work. How have things been emotionally as well as physically?
Chris | My [[low mood::Low mood describes Chris's reported emotional difficulty without itself establishing a specific diagnosis.]] has been harder to manage than I expected, but I struggle to explain it.
Dr Wells | We can take it one part at a time. What has changed in your usual activities or interests?
Chris | I stopped enjoying things I normally like. I saw the word [[anhedonia::Anhedonia refers to reduced interest or pleasure, which can be explored without diagnosing from the word alone.]], but I was unsure how to say it.
Dr Wells | Your own description is enough. I also need to ask directly about your safety rather than make assumptions.
Chris | I was worried that my [[daily functioning::Daily functioning concerns ordinary activities such as work and self-care, not just how someone appears in a consultation.]] would look normal because I managed to come to this appointment.
Dr Wells | Coming here does not tell me everything. Have you had thoughts about ending your life?
Chris | That is difficult to discuss. Will talking about [[suicidal thoughts::Suicidal thoughts concern ending one's life and require direct, sensitive clinical assessment rather than assumptions.]] mean that everything I say is automatically shared with everyone?
Dr Wells | No. I will explain privacy and its limits, including when safety duties may require involving other people.
Chris | Please explain those [[confidentiality limits::Confidentiality limits are circumstances where applicable duties prevent a promise of absolute secrecy.]] before assuming I understand them. I want to answer honestly.
Dr Wells | Of course. We will discuss the relevant rules and your situation, and I will explain the next steps.
Chris | I appreciate the [[nonjudgmental language::Nonjudgmental language explores the person's experience without assigning blame or shaming a disclosure.]]. I was afraid this would become a lecture about coping better.
Dr Wells | My aim is to understand what is happening and assess safety, including difficulties and sources of support.
Chris | My sister has been helpful. I would like her considered as part of my [[support network::A support network consists of people or services that can help, while their involvement still needs appropriate discussion.]].
Dr Wells | We can discuss that. Our behavioral-health colleague is also available, depending on the assessed needs and agreed plan.
Chris | Could you introduce us? A [[warm handoff::A warm handoff provides a supported introduction with context rather than leaving the patient with only a contact number.]] would be easier than repeating everything to a stranger without preparation.
Dr Wells | We can discuss the introduction and what information is appropriate to share, subject to the relevant duties.
Chris | Then my [[consent to share::Consent to share concerns permission for specified information, within the applicable safety and legal requirements.]] is something we clarify rather than assume from my attendance here.
Dr Wells | Yes. We must also complete the safety assessment and respond appropriately to anything urgent that it reveals.
Chris | I understand that the [[risk assessment::The risk assessment is still required and cannot be replaced by a calm appearance or a promised referral.]] has not already been completed just because I have started talking.''',
    rehearsal=['Read the corrected safety conversation calmly, with a pause before and after the direct question.', 'Swap roles. Repeat the privacy explanation without adding an absolute promise or an invented risk level.'],
    transfer_title='Introduce support without over-sharing', transfer_setup='Rae agrees to an introduction to counselor Jo. The relevant information to share will be clarified. Dr Moss has not completed the safety assessment; no risk level is supplied.',
    transfer='''Rae: "I agree to meet counselor ___." | Jo | Jo is the counselor named for the supported introduction.
Dr Moss: "We will clarify the information to ___." | share | Agreement to an introduction does not by itself settle every disclosure detail.
Rae: "The safety assessment is not ___." | complete | The scenario explicitly states that the safety assessment remains unfinished.
Dr Moss: "No risk level has been ___." | established | The supplied facts do not support assigning a clinical risk category.'''))

BOOK['units'].append(unit(
    title='Closing the referral loop', scene='Sent does not mean seen',
    skill='Give a referral update that identifies the open question, owner, and next contact.',
    brief='Dr Byrne referred Fin to a specialist for an unresolved clinical question. The receiving office confirms receipt, but has not confirmed an appointment. Practice coordinator Mina is checking the status and will update Fin on Friday. Friday is a status-update commitment, not a clinical waiting instruction or appointment date. New or worsening concerns must use the practice\'s actual clinical route.',
    cast='Dr Byrne | General practitioner\nFin | Patient',
    culture=('Make the stage visible', 'Patients may understand referred to mean booked or accepted for treatment. Name the actual stage and retain responsibility for unresolved care rather than treating the referral as a transfer of every duty.'),
    a='''What has the specialist office confirmed? | Receipt of the referral | A Friday appointment | Completed treatment | A resolved diagnosis | Only receipt is confirmed; the later stages have not been established.
Who is checking the status? | Mina | Fin's employer | A clinician not named in the case | Nobody | Mina is the practice coordinator assigned to check and update the status.
What does Friday mean? | A promised status update | A guaranteed appointment | Permission to wait with worsening symptoms | A completed consultation | Friday refers to communication about progress and is not a clinical waiting instruction.''',
    vocabulary='''referral | Request for another professional or service to assess or assist. | send a specialist referral
consultation question | Specific issue the referring clinician asks the receiving service to address. | state the consultation question
urgency category | Assigned level of time sensitivity under a clinical process. | verify the urgency category
referral receipt | Confirmation that the receiving service has obtained the referral. | confirm referral receipt
appointment confirmation | Verification that a specific appointment has been arranged. | obtain appointment confirmation
closed-loop referral | Referral process tracking receipt, follow-up, and information returned to the referrer. | complete a closed-loop referral
consultant letter | Communication from a specialist summarizing an assessment or advice. | review the consultant letter
awaiting review | Received but not yet evaluated by the relevant reviewer. | mark a referral as awaiting review
missed appointment | Scheduled encounter that did not take place as arranged. | follow up a missed appointment
results ownership | Responsibility for reviewing and acting on investigation results. | clarify results ownership
pending action | Task still requiring completion. | identify a pending action
acknowledgment | Confirmation that a message or request was received. | obtain an acknowledgment
interim care | Care provided while another assessment or transition is pending. | clarify interim care
contact preference | Person's preferred appropriate method of communication. | verify the contact preference
escalation route | Process for raising an unresolved or urgent concern to the right professional. | use the clinical escalation route
care transition | Movement of care between settings, professionals, or stages. | support a care transition
record transfer | Appropriate movement of relevant information between care providers. | verify record transfer
access barrier | Obstacle that makes obtaining a service difficult. | identify an access barrier''',
    precision='Receipt, review, booking, attendance, and a returned clinical report are different stages. Do not report a later stage when only an earlier one is confirmed.',
    precision_extra='A status-update date must never imply that symptoms can safely wait until that date. Keep administrative progress and clinical escalation separate.',
    phrases='''State the confirmed stage | The receiving office has confirmed receipt.
Name the missing step | An appointment has not yet been confirmed.
Identify the owner | Mina is checking the status.
Define the date | Friday is our update date, not your appointment date.
Keep care connected | We need to clarify who handles the outstanding clinical questions.
Separate urgent concerns | New or worsening symptoms use the clinical route, not a routine status message.
Confirm contact | Which approved contact method should we use for the update?
Close the loop | We will track the response and the information returned after consultation.''',
    notes='''Has confirmed versus will check | Separates a completed acknowledgment from a future task.
Not yet | Marks an unfinished stage without implying that it has been refused.
Update date versus appointment date | Prevents an administrative commitment from becoming a false booking promise.''',
    d='''Which update is supported? | Receipt is confirmed; an appointment is not. | Fin will be seen Friday. | Treatment is complete. | The clinical question is resolved. | Only receipt has been verified in the supplied referral history.
Which phrase could dangerously confuse two processes? | Wait until Friday with any new symptoms. | Friday is a status update. | Mina is checking the referral. | Clinical concerns use the clinical route. | A routine administrative update cannot determine how long a new clinical concern can wait.
What makes the next step accountable? | A named owner and a defined update | A vague promise that someone will look | An assumed appointment | A closed record before review | Naming Mina and the update date makes the communication task explicit and trackable.
What remains important after sending a referral? | Following the response and clarifying continuing responsibilities | Assuming all duties disappeared | Declaring attendance complete | Ignoring the consultation question | Sending a request is only one step in a connected referral process.''',
    dialogue='''Fin | I was told the referral had gone through. Does that mean the specialist has booked me in?
Dr Byrne | We have [[referral receipt::Referral receipt confirms that the service obtained the request, not that an appointment has been arranged.]], but an appointment has not yet been confirmed.
Fin | Thank you for separating those. I heard gone through and assumed there was a date somewhere.
Dr Byrne | [[Appointment confirmation::Appointment confirmation establishes a specific booking and is a later stage than merely receiving the referral.]] is a separate step. Mina is checking the status with the receiving office.
Fin | What exactly is the specialist being asked to address? I do not want to arrive without understanding that.
Dr Byrne | We will review the [[consultation question::The consultation question states the unresolved issue the referring clinician asks the specialist to address.]] with you and make sure the relevant records accompany the request.
Fin | I can explain my concern, but I may not remember every detail that is already in your notes.
Dr Byrne | Appropriate [[record transfer::Record transfer sends relevant information through the proper process so the receiving team has the necessary context.]] helps the receiving team. It does not replace listening to your current account.
Fin | Mina mentioned Friday. Is that when the consultation will happen, or when someone will contact me?
Dr Byrne | Friday is a status update. The [[pending action::A pending action is a task still to complete; here it is checking progress, not attending a booked consultation.]] is checking progress, not attending a confirmed appointment.
Fin | Who should deal with questions before the specialist sees me? I do not want to fall between teams.
Dr Byrne | We must clarify [[interim care::Interim care covers appropriate care while another assessment is pending and cannot be assumed to belong to nobody.]] and the outstanding responsibilities rather than assume everything transferred when we sent the request.
Fin | If something changes clinically before Friday, should I wait for Mina's administrative update to mention it?
Dr Byrne | No. Use the actual clinical [[escalation route::The escalation route connects new or worsening clinical concerns to appropriate assessment, separate from routine referral tracking.]] for new or worsening concerns. The update date is not advice to wait.
Fin | I also need calls at a time I can answer privately. Can we agree on how the update reaches me?
Dr Byrne | Yes, we will verify your [[contact preference::Contact preference identifies an appropriate communication method and helps an update reach the patient without avoidable privacy problems.]] and use the practice's approved communication process.
Fin | Once the appointment happens, will the specialist's advice come back here, or do I have to relay everything?
Dr Byrne | We will track the [[consultant letter::A consultant letter communicates the specialist's assessment or advice back to the referring clinician for review.]] and review the responsibilities it identifies, rather than assume attendance alone closes every question.
Fin | That is clearer: receipt now, a status update Friday, and no appointment date promised yet.
Dr Byrne | Exactly. A [[closed-loop referral::A closed-loop referral tracks the request, response, and returned information instead of stopping at the act of sending.]] keeps the stages and responsibilities connected until the relevant follow-up is complete.''',
    rehearsal=['Read the corrected referral update. Stress receipt, appointment, and status update as separate stages.', 'Swap roles. Repeat the distinction between Friday\'s administrative update and the clinical escalation route.'],
    transfer_title='Track a returned specialist report', transfer_setup='A specialist consultation occurred Monday. The report has not arrived. Coordinator Zoe is requesting it and will update the referring team Wednesday. No new treatment instruction is supplied.',
    transfer='''Clinician: "The consultation occurred on ___." | Monday | Monday is the completed attendance date stated in this follow-up case.
Zoe: "The report has not ___." | arrived | Attendance does not mean the consultant's report has reached the referring team.
Clinician: "The update is due ___." | Wednesday | Wednesday is the communication commitment, not a treatment deadline.
Zoe: "No new treatment instruction has been ___." | supplied | The exercise provides no new clinical instruction to infer or act on.'''))
