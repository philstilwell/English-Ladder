"""Original obstetric conversations centered on evidence, consent, and continuity."""
from books.medical_support import medical_unit as unit, source, SCOPE

BOOK = dict(slug='obstetricians', title='Obstetrics English', cover_label='ENGLISH FOR OBSTETRICIANS',
    cover_title='Obstetrics', cover_size=42, tagline='Explain the uncertainty. Respect the choice. Coordinate care.',
    audience='For obstetricians, obstetric trainees, and physicians coordinating pregnancy and postpartum care.',
    roles='obstetricians, obstetrics residents, maternal-fetal medicine physicians, maternity-care physicians',
    summary='Obstetric English for pregnancy histories, prenatal screening, urgent maternal concerns, gestational diabetes discussions, birth preferences, labor handoffs, postpartum care, and pregnancy loss.',
    map_intro='Eight maternity encounters practice sensitive history, probability language, urgent escalation, nonjudgmental explanations, renewed consent, source-aware handoffs, postpartum follow-up, and difficult news.',
    notes_title='The plan can change; the person remains central.',
    notes_intro='Obstetric communication moves between routine planning and consequential uncertainty. Explain what is known, what a test can establish, who has a decision to make, and how the patient remains involved as circumstances change.',
    field_notes=[
        ('Do not assume the history', 'Ask respectfully about prior pregnancies, losses, dates, language needs, and support people. A companion is not automatically a decision-maker or an authorized recipient.', '"How would you like us to refer to your previous pregnancy, and who may join this discussion?"'),
        ('Name what a result can establish', 'Screening, diagnostic testing, imaging, and clinical assessment answer different questions. Keep probabilities distinct from confirmed findings.', '"This screening result changes the estimated chance; it does not itself establish the diagnosis."'),
        ('Revisit consent when the situation changes', 'Explain the new concern and relevant options using the actual clinical assessment. Prior preferences matter but do not remove the need for an appropriate current discussion.', '"The circumstances have changed. Let me explain the recommendation and hear your questions."'),
        ('Carry care beyond delivery', 'Postpartum concerns deserve specific communication and appropriate assessment. Do not normalize a concerning change simply because the baby has been born.', '"Please tell the receiving team that you recently gave birth and describe the current symptoms."'),
    ], scope_note=SCOPE,
    sources=[
        source('ACOG. Prenatal Genetic Screening Tests.', 'https://www.acog.org/womens-health/faqs/prenatal-genetic-screening-tests', 'Background for distinguishing screening probabilities from diagnostic conclusions and discussing testing choices.'),
        source('ACOG. Gestational Diabetes.', 'https://www.acog.org/womens-health/faqs/gestational-diabetes', 'Terminology and communication context; no diagnostic cutoffs or treatment instructions are supplied.'),
        source('CDC Hear Her. Urgent Maternal Warning Signs.', 'https://www.cdc.gov/hearher/maternal-warning-signs/index.html', 'Supports prompt attention to urgent concerns during pregnancy and after birth; the language tasks never determine that symptoms can wait.'),
        source('ACOG. Early Pregnancy Loss.', 'https://www.acog.org/womens-health/faqs/early-pregnancy-loss', 'Context for compassionate discussion of confirmed loss, uncertainty, and individualized options without prescribing management.')], units=[])

BOOK['units'].append(unit(
    title='Taking a sensitive pregnancy history', scene='Dates, previous experiences, and preferred words',
    skill='Clarify dating information and previous pregnancy experiences without making assumptions.',
    brief='At an initial visit, Avery is unsure of the last menstrual period and mentions a previous pregnancy loss. Dr Stone asks permission to discuss the history, records uncertain dates as uncertain, and asks which support person Avery wants involved. No estimated due date, gestational age, or pregnancy outcome is calculated in the case.',
    cast='Avery | Pregnant patient\nDr Stone | Obstetrician',
    culture=('Use the person\'s words', 'A previous loss may carry a meaning not captured by a count. Ask respectfully, avoid assumptions about family structure, and separate necessary history from curiosity.'),
    a='''Which date is uncertain? | The last menstrual period | A confirmed delivery date | A booked procedure | A completed diagnostic test | Avery is unsure of the last menstrual period in the supplied history.
What previous experience is mentioned? | Pregnancy loss | A confirmed current complication | A completed current birth | A known due date | Avery mentions a previous loss without supplying a detailed obstetric history.
What is not calculated? | Gestational age or due date | A privacy preference | The need to clarify dates | Permission to discuss history | The case supplies no data or instruction for calculating gestational age or a due date.''',
    vocabulary='''gravidity | Number of pregnancies, counted under the relevant clinical convention. | document gravidity
parity | Birth history summarized using the applicable clinical convention. | clarify parity
gestational age | Duration of pregnancy expressed using the relevant dating method. | explain gestational age
estimated due date | Estimated date used for pregnancy planning and dating. | verify the estimated due date
last menstrual period | Reported starting date of the most recent menstrual period. | clarify the last menstrual period
dating ultrasound | Ultrasound used to inform pregnancy dating in context. | discuss a dating ultrasound
menstrual regularity | Pattern of how consistently menstrual cycles occur. | ask about menstrual regularity
obstetric history | Account of previous pregnancies and their relevant outcomes. | obtain an obstetric history
prior pregnancy loss | Loss in an earlier pregnancy. | acknowledge a prior pregnancy loss
live birth | Birth showing signs of life under the relevant definition. | document a live birth
preterm birth | Birth before the relevant full-term threshold. | review a preterm-birth history
ectopic pregnancy | Pregnancy implanted outside the usual uterine cavity location. | clarify an ectopic-pregnancy history
prenatal record | Record of pregnancy-related care before birth. | review the prenatal record
support person | Person the patient chooses to provide support. | identify the chosen support person
preferred terminology | Words the person wishes used for sensitive experiences. | ask about preferred terminology
trauma-informed approach | Approach attentive to safety, choice, and prior distressing experiences. | use a trauma-informed approach
dating uncertainty | Unresolved information affecting pregnancy dating. | document dating uncertainty
history clarification | Follow-up questions resolving ambiguous historical information. | request history clarification''',
    precision='An uncertain menstrual date must not become a precise due date by assumption. A history abbreviation does not replace clarification of what actually occurred.',
    precision_extra='Counting conventions and terminology differ. Confirm the actual record and local convention; do not calculate a pregnancy outcome or dating estimate from this exercise.',
    phrases='''Ask permission | May we discuss your previous pregnancy experiences?
Allow uncertainty | It is fine to say that you do not remember the exact date.
Keep the record honest | I will record the date as uncertain.
Ask about words | Is there a term you would prefer us to use?
Include support by choice | Who would you like involved in this conversation?
Explain relevance | I will explain why I am asking each sensitive question.
Avoid assumptions | I will not infer the outcome from an abbreviation alone.
Summarize respectfully | Let me check that I have understood your history correctly.''',
    notes='''Estimated versus guaranteed | An estimated due date is a planning estimate, not a promise of the birth date.
Unsure versus approximate | Unsure identifies uncertainty; an approximate date still requires a basis in the person's account.
Chosen support person | Identifies the patient's preference without assigning decision authority to a companion.''',
    d='''Which entry preserves the history? | Last menstrual period uncertain. | Exact date invented from memory. | Due date guaranteed. | Previous loss omitted for convenience. | The entry accurately retains uncertainty rather than manufacturing precision.
Which opening is respectful? | May we discuss your previous pregnancy experiences? | Your companion must answer everything. | We do not need your preferred words. | Every loss means the same thing. | Asking permission creates space for a sensitive history without assuming the person's experience.
What should an abbreviation not replace? | Clarification of the actual history | A font choice | A waiting-room number | A generic slogan | Clinical shorthand may use different conventions and cannot replace the relevant facts.
Which role is not automatic for a companion? | Authorized decision-maker | Chosen support person when requested | Someone who may attend with permission | A person whose presence can be discussed | Accompanying a patient does not by itself establish decision-making or information-sharing authority.''',
    dialogue='''Dr Stone | Before we discuss dates, may I ask about previous pregnancy experiences and how you would like us to refer to them?
Avery | Yes. I had a pregnancy loss, and I would prefer that wording rather than moving straight to a number.
Dr Stone | I will respect that [[preferred terminology::Preferred terminology records the person's chosen words for a sensitive experience rather than imposing a label without checking its meaning.]]. The history matters, but the experience is more than an abbreviation.
Avery | I am also unsure of the exact date of my last period. I do not want to give a false answer.
Dr Stone | We can record the [[last menstrual period::The last menstrual period is a reported dating detail and should remain uncertain when the patient cannot supply a reliable date.]] as uncertain rather than turn a guess into a precise date.
Avery | Does that mean the date on my calendar is not automatically the date we should use for planning?
Dr Stone | Correct. [[Dating uncertainty::Dating uncertainty identifies unresolved information affecting pregnancy dating and should remain visible while the appropriate assessment is arranged.]] needs to remain visible while we review the relevant information.
Avery | A previous form used letters and numbers that I did not understand. Could those be checked with me?
Dr Stone | Yes. Your [[obstetric history::Obstetric history describes prior pregnancies and relevant outcomes and should be clarified rather than inferred solely from unfamiliar shorthand.]] should reflect what actually happened, not an assumption based only on shorthand.
Avery | One word was gravidity. Does that refer to every pregnancy rather than just births?
Dr Stone | [[Gravidity::Gravidity counts pregnancies under the relevant convention and differs from a summary of birth history.]] concerns the number of pregnancies under the relevant convention; we will clarify the details respectfully.
Avery | And parity is a different summary, so I should not assume the two numbers mean the same thing?
Dr Stone | Yes. [[Parity::Parity summarizes birth history using the applicable clinical convention and is not interchangeable with gravidity.]] uses the applicable birth-history convention. The underlying facts still need to be clear.
Avery | I would like my partner involved later, but I want this first part of the conversation to remain between us.
Dr Stone | We can discuss the appropriate privacy arrangements and when your chosen [[support person::A support person is someone the patient chooses for support and is not automatically entitled to every disclosure or decision.]] joins the conversation.
Avery | Will a scan necessarily give a guaranteed day on which the baby will be born?
Dr Stone | No. An [[estimated due date::An estimated due date is a planning and dating estimate rather than a guarantee of the actual day of birth.]] is an estimate, and its basis should be explained.
Avery | I appreciate knowing what is uncertain instead of feeling that I must remember every detail perfectly.
Dr Stone | A [[trauma-informed approach::A trauma-informed approach attends to safety, choice, and prior distress without forcing unnecessary disclosure or ignoring the person's preferences.]] includes explaining the purpose of questions and allowing appropriate choice and pauses.
Avery | Then we can complete the [[history clarification::History clarification resolves ambiguous information through respectful follow-up rather than replacing missing details with assumptions.]] with uncertain dates marked honestly and the previous loss described in my words.''',
    rehearsal=['Read the corrected history discussion. Preserve uncertain dates and the preferred terminology.', 'Swap roles. Explain the difference between history terms without calculating a due date.'],
    transfer_title='A record uses unfamiliar shorthand', transfer_setup='An outside record contains an unfamiliar pregnancy-history abbreviation. The patient has not confirmed its meaning. The clinician requests clarification before adopting it.',
    transfer='''Patient: "I do not recognize that ___." | abbreviation | The outside record contains shorthand the patient does not recognize.
Clinician: "Its meaning is not yet ___." | confirmed | The patient has not confirmed what the abbreviation represents.
Patient: "We need to clarify the actual ___." | history | The underlying pregnancy history matters more than assuming the shorthand is accurate.
Clinician: "I will not adopt it by ___." | assumption | The clinician requests clarification rather than treating the unverified entry as established.'''))

BOOK['units'].append(unit(
    title='Explaining prenatal screening choices', scene='A higher chance is not a diagnosis',
    skill='Explain screening uncertainty and voluntary next steps without directing a reproductive decision.',
    brief='Riley receives a higher-chance prenatal screening result and thinks it proves a fetal condition. Dr Noor explains that screening estimates chance rather than establishing a diagnosis. The actual result and available diagnostic options need individualized counseling. No probability value, procedure choice, or pregnancy decision is supplied. Riley wants time to understand the information and include a chosen support person.',
    cast='Riley | Pregnant patient\nDr Noor | Obstetrician',
    culture=('Explain choices without steering personal values', 'Give clear information about the purpose and limits of testing. Do not assume what the patient would do with a result or pressure a reproductive decision.'),
    a='''What does the result describe? | A higher estimated chance | A confirmed diagnosis | A guaranteed outcome | A required pregnancy decision | The case describes screening probability rather than diagnostic confirmation.
What does Riley request? | Time and a chosen support person | A decision made by the clinician alone | Automatic testing without discussion | A guaranteed normal outcome | Riley wants to understand the information with appropriate support.
What is not supplied? | A numerical probability or procedure choice | A screening concern | A need for counseling | Riley's question | The exercise supplies neither an individual probability value nor a selected diagnostic procedure.''',
    vocabulary='''prenatal screening | Testing that estimates the chance of specified conditions before birth. | explain prenatal screening
diagnostic testing | Testing intended to establish or clarify a condition. | discuss diagnostic testing
cell-free DNA screening | Screening using DNA fragments in maternal blood for specified conditions. | explain cell-free DNA screening
screening probability | Estimated chance reported by a screening process. | communicate screening probability
screen-positive result | Screening finding indicating increased chance under the relevant method. | explain a screen-positive result
false-positive result | Positive screening finding not confirmed for the condition assessed. | explain a false-positive result
false-negative result | Negative screening finding despite the condition being present. | explain a false-negative result
positive predictive value | Proportion of positive results that correspond to the condition in context. | discuss positive predictive value
residual risk | Remaining chance after a result or intervention. | explain residual risk
genetic counseling | Specialist discussion of genetic information, options, and implications. | arrange genetic counseling
amniocentesis | Procedure obtaining amniotic fluid for relevant testing. | discuss amniocentesis
chorionic villus sampling | Procedure obtaining placental tissue for relevant testing. | explain chorionic villus sampling
chromosomal condition | Condition involving chromosome number or structure. | discuss a chromosomal condition
test limitation | Boundary on what a test can detect or establish. | explain test limitations
inconclusive result | Result that does not provide a definitive answer to its question. | communicate an inconclusive result
informed refusal | Decision to decline after relevant information is understood. | document informed refusal
voluntary testing | Testing chosen without coercion after appropriate discussion. | support voluntary testing
decision support | Assistance helping a person understand options and relevant values. | offer decision support''',
    precision='A higher-chance screening result is not diagnostic confirmation. A lower-chance result does not guarantee absence of every condition.',
    precision_extra='Explain actual test performance and options in context. Do not supply an invented probability, universal procedure recommendation, or reproductive decision.',
    phrases='''Name the result type | This is a screening result, not a diagnosis.
Explain the limit | It changes the estimated chance but does not settle the question.
Avoid a guarantee | A lower-chance result cannot rule out every condition.
Offer counseling | We can arrange a discussion of the actual result and options.
Ask about information | What would you like explained before considering the next step?
Protect choice | Testing decisions require an informed, voluntary discussion.
Include chosen support | We can include the person you choose with your permission.
Allow a pause | We can pause to make sure the information is clear.''',
    notes='''Chance versus certainty | Keeps a probability estimate distinct from a confirmed finding.
For specified conditions | Prevents one screening method from being described as testing for everything.
May choose versus must | Preserves voluntary decision-making rather than presenting a procedure as automatic.''',
    d='''Which explanation is accurate? | Screening estimates chance; diagnostic testing addresses confirmation. | Every positive screen proves a condition. | A negative screen guarantees every outcome. | Screening replaces all counseling. | Screening and diagnosis answer different questions and cannot be treated as interchangeable.
Which statement overextends the test? | This screens for every possible condition. | We need the actual test's limits. | The result requires context. | Options can be discussed. | A screening method has a defined scope and cannot be described as detecting every condition.
What does positive predictive value concern? | How often a positive result corresponds to the condition in context | The percentage of tests ordered | A guaranteed personal outcome | The price of a test | The measure concerns the meaning of positive results in the relevant population and context.
Which next-step statement respects choice? | Let us discuss the options and your questions. | You must choose my preferred procedure. | Your support person decides automatically. | No explanation is needed. | An informed discussion supports the patient's decision without imposing a reproductive choice.''',
    dialogue='''Riley | The message says higher chance. I read that as proof that the baby has the condition.
Dr Noor | This is [[prenatal screening::Prenatal screening estimates chance; it does not itself establish a diagnosis.]], not diagnostic confirmation. Let us explain what this particular result can and cannot establish.
Riley | Does that mean the result is meaningless, or that I should simply ignore it?
Dr Noor | No. The [[screening probability::Screening probability informs discussion but is not certainty about an individual outcome.]] informs the next discussion, but an estimate is not certainty.
Riley | I would like to understand how a positive result can occur when the condition is not present.
Dr Noor | That is a [[false-positive result::A false-positive result is not confirmed for the condition being assessed.]]. The actual test and your circumstances determine how the result should be interpreted.
Riley | And a lower-chance result would not mean every possible condition has been excluded?
Dr Noor | Correct. [[Residual risk::Residual risk remains after screening; lower chance is not a universal guarantee.]] and the scope of the test still matter.
Riley | Someone mentioned a predictive value, but I did not understand what was being predicted.
Dr Noor | [[Positive predictive value::Positive predictive value describes positive results in context, not a personal guarantee.]] concerns what positive results mean in context. We should use the actual figures, not invent a number.
Riley | What kind of discussion would help me understand the further testing options?
Dr Noor | [[Genetic counseling::Genetic counseling supports understanding of genetic information, testing options, limitations, and implications without imposing a personal reproductive decision.]] can help explain the actual result, options, limitations, and what information you want.
Riley | Are amniocentesis and the placental-sampling procedure simply more screening blood tests?
Dr Noor | No. [[Amniocentesis::Amniocentesis obtains amniotic fluid for relevant testing and is not simply another screening blood draw.]] and chorionic villus sampling are procedures used for relevant diagnostic testing, with their own discussions of benefits and risks.
Riley | I do not want a procedure selected before I understand what question it would answer.
Dr Noor | That is appropriate. [[Decision support::Decision support helps the patient understand options and relevant values rather than choosing a procedure or pregnancy outcome for them.]] should clarify the question and your preferences rather than make the decision for you.
Riley | Could I include my chosen support person when we discuss the information again?
Dr Noor | Yes, with your permission. [[Voluntary testing::Voluntary testing is chosen without coercion after an appropriate informed discussion, not automatically required by a screening result.]] requires a discussion you understand, with support you choose.
Riley | I also want to know what happens if the further result still does not answer everything.
Dr Noor | We should explain the possibility of an [[inconclusive result::An inconclusive result leaves its relevant question unresolved and should be discussed without promising that every test will provide certainty.]] and other limits before you choose the next step.''',
    rehearsal=['Read the corrected screening exchange, emphasizing chance, confirmation, and limits.', 'Swap roles. Explain the options discussion without assigning a probability or choosing a procedure.'],
    transfer_title='A result is inconclusive', transfer_setup='A prenatal test result is described as inconclusive. The clinician arranges review of the actual report and options. No diagnosis is established.',
    transfer='''Patient: "The result is ___." | inconclusive | The result does not provide a definitive answer to its relevant question.
Clinician: "We need to review the actual ___." | report | The actual report is the basis for explaining the unresolved result.
Patient: "A diagnosis is not ___." | established | An inconclusive result does not establish a diagnosis in this case.
Clinician: "We will explain the available ___." | options | The next step is an informed review of options rather than an automatic decision.'''))

BOOK['units'].append(unit(
    title='Escalating an urgent maternal concern', scene='Symptoms first, diagnosis still under review',
    skill='Communicate urgent symptoms and pregnancy context without delaying the actual response.',
    brief='Pregnant patient Jordan reports a severe headache and visual changes. The maternity team has already activated the actual urgent assessment pathway. Dr Ahmed confirms the symptom account and receiving team while care proceeds. No blood-pressure value, laboratory result, gestational week, or diagnosis is supplied. The exercise must not be used to decide that these symptoms can safely wait.',
    cast='Jordan | Pregnant patient\nDr Ahmed | Obstetrician',
    culture=('Do not normalize a serious concern', 'Avoid dismissing a marked change as simply part of pregnancy. Communicate the concern plainly and preserve the distinction between symptoms and a diagnosis under assessment.'),
    a='''Which symptoms are reported? | Severe headache and visual changes | A confirmed laboratory diagnosis | Normal measured blood pressure | No current concern | The supplied report names severe headache and visual changes.
What is already underway? | The urgent assessment pathway | A routine review next month | A completed discharge | A language-only conversation | The actual urgent response is already active and continues during communication.
What is not supplied? | Blood pressure or a diagnosis | Pregnancy context | Jordan's report | A receiving team | No measurements or diagnostic conclusion are provided for the learner to invent.''',
    vocabulary='''maternal warning sign | Symptom or sign requiring prompt attention in pregnancy or after birth. | communicate a maternal warning sign
severe headache | Marked head pain described or assessed in context. | report a severe headache
visual disturbance | Change in vision described by the person or assessment. | clarify a visual disturbance
hypertensive disorder | Condition involving high blood pressure in the relevant clinical context. | assess a hypertensive disorder
preeclampsia | Pregnancy-related hypertensive disorder with relevant diagnostic features. | evaluate suspected preeclampsia
blood-pressure measurement | Verified reading obtained through an appropriate measurement process. | relay a blood-pressure measurement
proteinuria | Protein present in urine, interpreted in the relevant context. | interpret proteinuria
epigastric pain | Pain in the upper central abdominal region. | clarify reported epigastric pain
right-upper-quadrant pain | Pain in the upper right abdominal region. | describe right-upper-quadrant pain
urgent assessment | Prompt clinical evaluation through the appropriate pathway. | arrange urgent assessment
maternity triage | Service assessing pregnancy-related concerns and care needs. | contact maternity triage
symptom progression | How a symptom changes over time. | report symptom progression
clinical observation | Finding obtained through actual clinical assessment. | distinguish clinical observations
escalation pathway | Approved route for raising a concern to the appropriate care team. | activate the escalation pathway
maternal status | Current clinical condition of the pregnant or postpartum patient. | communicate maternal status
fetal assessment | Clinical evaluation of fetal condition using appropriate methods. | coordinate fetal assessment
unconfirmed diagnosis | Diagnostic possibility not yet established by evidence. | preserve an unconfirmed diagnosis
receiving service | Service accepting the relevant clinical concern and care transfer. | confirm the receiving service''',
    precision='The symptoms require the actual urgent clinical process. They do not authorize the learner to diagnose preeclampsia or declare measurements normal.',
    precision_extra='A missing blood-pressure value is unknown, not reassuring. Keep the emergency or urgent response moving while accurate information is transferred.',
    phrases='''Lead with symptoms | You report a severe headache and changes in vision.
State the action | The urgent assessment pathway is already active.
Avoid normalization | I will not dismiss this as simply part of pregnancy.
Preserve unknowns | We do not yet have a verified value to report.
Clarify change | Tell the team how the symptoms have changed.
Keep diagnosis separate | The cause is still being assessed.
Name the receiver | We are confirming the receiving maternity team.
Prevent delay | Do not wait for this conversation to finish before following the urgent process.''',
    notes='''Reports versus confirms | The patient reports symptoms; a diagnosis requires the appropriate clinical assessment.
Already active | States that necessary urgent action precedes completion of the language task.
Unknown versus normal | Absence of a supplied measurement cannot support a normal finding.''',
    d='''Which handoff opening is accurate? | Severe headache and visual changes; urgent assessment is active. | Normal blood pressure without a measurement. | Confirmed preeclampsia without assessment. | Routine discomfort that can wait. | The opening states the supplied symptoms and action without inventing a diagnosis or safe delay.
Which diagnosis is not established? | Preeclampsia | The existence of a symptom report | Pregnancy context | An active pathway | The case supplies no diagnostic evidence establishing preeclampsia.
What does missing blood pressure mean here? | No verified value is supplied. | The value is normal. | The concern is harmless. | Assessment is unnecessary. | An absent measurement is unknown and must not be converted into reassurance.
What takes priority over finishing the dialogue? | The actual urgent response | A polished sentence | Completing every blank | A fictional score | Language practice must not delay the real clinical response to the concern.''',
    dialogue='''Jordan | I have a severe headache and my vision has changed. I am worried that this is not my usual discomfort.
Dr Ahmed | The [[urgent assessment::Urgent assessment is already active and must not wait for this conversation.]] pathway is already active. I will confirm your report while the clinical team continues the response.
Jordan | I was afraid someone would say that headaches are just part of being pregnant.
Dr Ahmed | A [[maternal warning sign::A maternal warning sign needs prompt attention, not dismissal as ordinary pregnancy.]] must not be dismissed that way. We need the actual assessment, not reassurance from an assumption.
Jordan | Should I describe what I mean by the vision change rather than choosing a medical term?
Dr Ahmed | Yes. Describe the [[visual disturbance::Visual disturbance describes the reported change and needs clarification in the patient's words.]] in your own words, including how it has changed.
Jordan | Does mentioning these symptoms mean you have already diagnosed a blood-pressure condition?
Dr Ahmed | No. A [[hypertensive disorder::A hypertensive disorder requires assessment; symptom words alone do not establish it.]] is not established by the symptom words alone.
Jordan | I have not been told a verified blood-pressure number during this conversation.
Dr Ahmed | Please flag that it is not yet available. We need an actual [[blood-pressure measurement::Blood-pressure measurement requires an actual verified reading, not assumed normality.]], not an assumption based on how the patient appears.
Jordan | I also want the next team to know that the symptoms have become more noticeable.
Dr Ahmed | We will communicate that [[symptom progression::Symptom progression describes change over time and should be passed on accurately without converting it into an unsupported diagnostic conclusion.]] and distinguish your report from any measured findings.
Jordan | Someone mentioned preeclampsia as a possible concern. Is possible different from confirmed?
Dr Ahmed | Yes. [[Preeclampsia::Preeclampsia is a pregnancy-related hypertensive disorder requiring relevant diagnostic evidence and remains unconfirmed in this language case.]] is not confirmed here. The team evaluates the actual clinical evidence.
Jordan | I understand. I do not want uncertainty about the cause to mean waiting without action.
Dr Ahmed | It does not. The [[escalation pathway::The escalation pathway moves the concern to the appropriate clinical team and can be active while the precise diagnosis remains uncertain.]] is active while the cause is being assessed.
Jordan | Who is receiving the update, including the fact that I am pregnant?
Dr Ahmed | We are confirming the [[receiving service::The receiving service accepts the clinical concern and transfer and should be explicitly confirmed rather than assumed from a sent message.]] and ensuring the pregnancy context and symptom report are included.
Jordan | Then the symptoms are taken seriously without pretending the cause has already been proven.
Dr Ahmed | Exactly. We preserve the [[unconfirmed diagnosis::An unconfirmed diagnosis is a possibility not yet established; keeping that uncertainty visible does not delay necessary urgent assessment.]] while the real urgent response continues, with new verified information passed to the team.''',
    rehearsal=['Read the corrected urgent exchange, leading with symptoms and the action already active.', 'Swap roles. Preserve diagnostic uncertainty without weakening the need for the actual urgent response.'],
    transfer_title='A new detail arrives during assessment', transfer_setup='During active urgent assessment, Jordan adds that the visual change began before the headache. The team acknowledges the corrected sequence. No diagnosis is established.',
    transfer='''Patient: "The visual change began ___ the headache." | before | The patient clarifies the symptom sequence in the supplied update.
Clinician: "I have acknowledged the corrected ___." | sequence | The update changes the order of symptoms in the history.
Patient: "Assessment remains ___." | active | The actual urgent assessment continues during the clarification.
Clinician: "The diagnosis remains ___." | unconfirmed | The corrected timeline does not independently establish a diagnosis.'''))

BOOK['units'].append(unit(
    title='Explaining a glucose-testing pathway', scene='The screening result is not the whole story',
    skill='Explain testing stages and respond to self-blame without assigning a diagnosis or diet plan.',
    brief='Morgan has a glucose screening result that requires further review under the local pregnancy-care pathway. Morgan assumes this confirms gestational diabetes and proves a personal failure. Dr Vale explains that the actual testing method and results determine the next step. No numerical cutoff, diagnostic result, meal prescription, or medicine instruction is supplied.',
    cast='Morgan | Pregnant patient\nDr Vale | Obstetrician',
    culture=('Remove blame without making false assurances', 'Acknowledge the worry and explain the process. Avoid moral language about food or implying that every outcome is under the patient\'s control.'),
    a='''What result is available? | A screening result requiring further review | A supplied confirmed diagnosis | A medicine prescription | A completed monitoring plan | The case gives a screening result needing review, not a diagnostic conclusion.
What does Morgan assume? | The result proves personal failure | The result is already explained | No follow-up exists | A dose is supplied | Morgan interprets the result as both a diagnosis and a moral judgment.
What is not supplied? | A diagnostic cutoff or treatment instruction | Morgan's concern | A local pathway | A clinician discussion | The exercise supplies no values or treatment plan for clinical use.''',
    vocabulary='''gestational diabetes | Diabetes first diagnosed in pregnancy under the relevant clinical criteria. | discuss gestational diabetes
glucose screening | Initial testing used in a particular glucose-assessment pathway. | explain glucose screening
glucose tolerance test | Test assessing the body's response to a specified glucose load. | discuss a glucose tolerance test
fasting sample | Sample collected under the required fasting conditions. | clarify fasting-sample instructions
postprandial | Occurring after a meal. | explain postprandial measurements
insulin resistance | Reduced response of body tissues to insulin. | explain insulin resistance
diagnostic threshold | Value or criterion used in the relevant diagnostic process. | verify diagnostic thresholds
testing pathway | Sequence of assessment steps used by the relevant service. | clarify the testing pathway
capillary glucose | Glucose measured from a small peripheral blood sample. | discuss capillary glucose
glucose log | Record of glucose readings with relevant timing and context. | review a glucose log
nutrition consultation | Individualized discussion with an appropriate nutrition professional. | arrange a nutrition consultation
individualized target | Goal selected for a particular person's clinical circumstances. | explain individualized targets
monitoring schedule | Agreed timing of measurements or checks. | confirm the monitoring schedule
meal context | Relevant information about food and timing around a measurement. | document meal context
hypoglycemia | Low blood glucose in the relevant clinical context. | explain hypoglycemia
hyperglycemia | High blood glucose in the relevant clinical context. | discuss hyperglycemia
postpartum testing | Testing undertaken after birth under the appropriate follow-up plan. | arrange postpartum testing
follow-up ownership | Identification of who is responsible for the next care step. | confirm follow-up ownership''',
    precision='A screening result must be interpreted within the actual testing pathway. Do not turn it into a diagnosis or a moral judgment.',
    precision_extra='Testing methods and criteria vary. Verify the actual instructions and results; do not infer a dose, diet, glucose target, or safe action from this exercise.',
    phrases='''Separate the stages | We need to distinguish this screening result from a diagnostic conclusion.
Remove moral judgment | This is a clinical question, not a score for your character.
Use the actual method | The next step depends on the testing pathway used here.
Clarify preparation | We will verify the instructions for the actual test.
Avoid invented targets | Any monitoring target must come from your clinical plan.
Ask about barriers | What might make the agreed follow-up difficult to attend?
Name support | We can discuss an appropriate nutrition consultation if indicated.
Carry follow-up forward | Let us identify who will coordinate the next result discussion.''',
    notes='''Requires review versus confirms | A result needing review does not automatically establish a diagnosis.
Individualized | Signals that a target or plan belongs to the actual person and assessment.
After a meal | Explains postprandial in plain language without supplying a measurement schedule.''',
    d='''Which explanation is appropriate? | The actual pathway determines how this result is assessed. | Every screening result is a diagnosis. | The result proves a moral failure. | One universal cutoff applies without context. | The testing method and relevant criteria determine the clinical interpretation.
What does postprandial mean? | After a meal | Before pregnancy | During sleep only | Before every sample | Postprandial identifies a relationship to a meal rather than a universal testing instruction.
Which item must come from the actual plan? | A monitoring target | Morgan's stated concern | The need to clarify terminology | The meaning of after | Targets depend on the individual clinical plan and are not provided by this exercise.
Which response avoids blame? | This is a clinical question, not a judgment of your character. | You failed the pregnancy. | You should have known every result. | Good people never have abnormal screens. | The response removes moral judgment while preserving the need for appropriate clinical review.''',
    dialogue='''Morgan | My glucose screening result needs follow-up. Does that mean I definitely have gestational diabetes and have done something wrong?
Dr Vale | A [[glucose screening::Glucose screening is an assessment stage, not automatically a completed diagnosis.]] result is not a moral judgment. We need to review the actual method and result.
Morgan | I thought every service used exactly the same test and that the word positive settled everything.
Dr Vale | The [[testing pathway::The testing pathway determines how this screening result leads to further assessment.]] matters. We should explain the process used here rather than assume every test works identically.
Morgan | Someone mentioned a tolerance test. I do not know how that differs from the first test.
Dr Vale | A [[glucose tolerance test::A glucose tolerance test needs the actual procedure and preparation explained.]] assesses the response to a glucose load. We will explain the actual procedure and instructions if it is the next step.
Morgan | Should I decide on my own whether to fast before an appointment?
Dr Vale | No. If a [[fasting sample::Fasting-sample preparation must come from verified instructions rather than a guess.]] is required, the preparation must come from the actual instructions rather than a guess.
Morgan | I also heard a number from a friend. Can I use that to interpret my own result?
Dr Vale | A [[diagnostic threshold::A diagnostic threshold belongs to a particular method and clinical process and cannot be borrowed without checking that it applies.]] belongs to the relevant method and criteria. A number without that context can mislead.
Morgan | If a diagnosis is later established, does that mean every person receives the same monitoring plan?
Dr Vale | No. An [[individualized target::An individualized target is chosen for the person's clinical circumstances and should not be invented from another person's plan.]] and any monitoring instructions come from the actual clinical plan.
Morgan | What does postprandial mean when people discuss the timing of a reading?
Dr Vale | [[Postprandial::Postprandial means after a meal and explains timing terminology without prescribing a universal measurement schedule.]] means after a meal. The precise measurement timing still needs the verified plan.
Morgan | If I keep readings later, would the surrounding information matter as well as the number?
Dr Vale | A [[glucose log::A glucose log records readings with relevant timing and context so they can be interpreted under the actual clinical plan.]] needs the relevant timing and context, not isolated numbers without explanation.
Morgan | I would appreciate support that does not treat food choices as evidence that I am a bad parent.
Dr Vale | An appropriate [[nutrition consultation::A nutrition consultation provides individualized professional discussion rather than moral judgment or a generic diet prescribed by this language case.]] can address practical needs without blame. The actual recommendation depends on the assessment.
Morgan | Then the immediate task is to understand the next test and who will discuss its result with me.
Dr Vale | Exactly. We will confirm [[follow-up ownership::Follow-up ownership identifies the professional or service responsible for the next step so a result does not remain unexplained.]] and the actual arrangements without inventing a diagnosis, target, or treatment today.''',
    rehearsal=['Read the corrected exchange, separating screening, diagnosis, and individualized monitoring.', 'Swap roles. Respond to self-blame without supplying a diet, cutoff, or medicine instruction.'],
    transfer_title='Preparation instructions conflict', transfer_setup='Two appointment messages give conflicting preparation instructions. The clinic asks the testing service to clarify before the patient follows either version.',
    transfer='''Patient: "The messages ___." | conflict | The two appointment messages contain inconsistent instructions for test preparation.
Clinician: "We need the testing service to ___." | clarify | The responsible testing service must resolve the conflicting instructions.
Patient: "I should not choose a version by ___." | guessing | The scenario calls for clarification rather than guessing which version applies.
Clinician: "We will confirm the actual ___." | preparation | The verified preparation for the actual test is the required information.'''))

BOOK['units'].append(unit(
    title='Revisiting a birth preference', scene='A changed recommendation needs a new explanation',
    skill='Explain a changed clinical recommendation while preserving the patient as an active decision-maker.',
    brief='During care, the team recommends discussing assisted birth because the clinical circumstances have changed. Patient Quinn had hoped to avoid intervention. Dr Lane explains that the actual assessment, urgency, options, material risks, benefits, and alternatives must be discussed. The exercise supplies no fetal tracing, procedure selection, or instruction to accept or refuse a particular intervention.',
    cast='Quinn | Patient in maternity care\nDr Lane | Obstetrician',
    culture=('Preferences are not a contract for a fixed outcome', 'Acknowledge the original preference without using it against the patient. Explain the changed circumstances clearly and avoid presenting a signature as the whole consent process.'),
    a='''What has changed? | The clinical circumstances and recommendation for discussion | Quinn's legal identity | A supplied procedure choice | A guaranteed outcome | The case describes changed circumstances requiring an appropriate discussion.
What was Quinn's preference? | Avoid intervention if possible | Have no explanation | Let a companion decide automatically | Accept every procedure in advance | Quinn hoped to avoid intervention and wants that preference acknowledged.
What is not supplied? | A procedure selection or fetal tracing | A need for explanation | Quinn's concern | A changed recommendation | The exercise does not provide the clinical evidence or a selected intervention.''',
    vocabulary='''birth preference | Stated wish about care and experience during birth. | acknowledge a birth preference
assisted vaginal birth | Vaginal birth supported by an appropriate instrument under clinical indications. | discuss assisted vaginal birth
cesarean birth | Birth through an operative abdominal and uterine incision. | explain cesarean birth
clinical indication | Reason supporting a proposed intervention in the actual case. | explain the clinical indication
material risk | Risk important to the person's informed decision in context. | discuss material risks
reasonable alternative | Relevant available option to the proposed intervention. | explain reasonable alternatives
informed consent | Authorization following an appropriate discussion and understanding of the proposed care. | obtain informed consent
decision capacity | Ability to make the relevant decision under applicable standards. | assess decision capacity
time sensitivity | Degree to which timing affects the available decision process. | explain time sensitivity
analgesia | Measures intended to relieve pain. | discuss analgesia options
anesthesia | Measures producing loss of sensation for an appropriate procedure. | explain anesthesia arrangements
procedural benefit | Expected advantage of a proposed procedure in context. | explain procedural benefits
change in circumstances | New information or condition altering the relevant assessment. | describe a change in circumstances
consent discussion | Conversation addressing the proposed intervention and relevant choices. | document the consent discussion
patient question | Concern or request for explanation raised by the patient. | invite patient questions
withdrawal of consent | Retraction of previously given authorization in the relevant context. | clarify withdrawal of consent
shared decision-making | Process combining clinical information with the person's informed preferences. | support shared decision-making
communication support | Assistance enabling understandable and accessible discussion. | arrange communication support''',
    precision='A birth preference does not waive future explanation or guarantee an outcome. A consent signature does not replace a meaningful discussion.',
    precision_extra='The actual urgency and assessment determine the available process. This exercise does not select an intervention, interpret fetal monitoring, or supply a legal consent rule.',
    phrases='''Acknowledge the preference | I remember that avoiding intervention was important to you.
Name the change | The circumstances have changed, and I need to explain the recommendation.
Explain the reason | Let us discuss the actual reason for considering this option.
Make time clear | I will explain how time-sensitive the decision is.
Include alternatives | We need to discuss the relevant alternatives and their implications.
Invite a focused question | What needs clarification before you can understand the options?
Check understanding | Please tell me how you understand the recommendation.
Keep the patient involved | Your questions and preferences remain part of this discussion.''',
    notes='''Recommend versus require | A recommendation needs explanation and does not automatically remove the consent process.
Changed circumstances | Identifies why the discussion is being revisited without blaming the earlier preference.
Understand versus agree | Understanding the explanation does not necessarily mean agreeing to the intervention.''',
    d='''Which statement preserves involvement? | Your preferences still matter as we explain the changed recommendation. | Your earlier plan means no further discussion. | A signature answers every question. | Your companion automatically decides. | The patient remains involved even when circumstances require a new clinical discussion.
What is not equivalent to consent? | Understanding the explanation | Appropriate authorization after discussion | A relevant informed decision | Consent under the applicable process | A person can understand a recommendation without agreeing to it.
What should time sensitivity describe? | The actual urgency and available decision process | A tactic to prevent all questions | A guaranteed outcome | A reason to invent a tracing | The timing discussion must reflect the real circumstances rather than pressure or unsupported evidence.
Which clinical action is not authorized here? | Selecting the birth intervention | Asking a clarification question | Acknowledging the preference | Explaining a consent discussion | No procedure or clinical decision is supplied for the learner to select.''',
    dialogue='''Quinn | I had hoped to avoid intervention. Hearing a different recommendation now makes me feel that my earlier wishes no longer matter.
Dr Lane | Your [[birth preference::Birth preferences remain relevant when changed circumstances require a new discussion.]] still matters. I need to explain what has changed and hear your questions.
Quinn | Please start with the reason, not just the name of a procedure I have never heard before.
Dr Lane | We should discuss the actual [[clinical indication::A clinical indication explains the actual reason supporting a proposed intervention.]] and the evidence behind the recommendation.
Quinn | I also need to know whether there is time to ask questions and include my chosen support person.
Dr Lane | I will explain the real [[time sensitivity::Time sensitivity describes real urgency, not a tactic for preventing questions.]] and what communication support is appropriate in these circumstances.
Quinn | If you mention assisted birth, does that mean the choice has already been made for me?
Dr Lane | No. Discussing [[assisted vaginal birth::Assisted vaginal birth names an option; mentioning it does not establish consent.]] does not by itself establish consent or settle the choice.
Quinn | I would like to understand the benefit being sought and the important risks, not only hear that it is recommended.
Dr Lane | The [[procedural benefit::Procedural benefit is an expected advantage, not a guaranteed outcome.]] and material risks belong in the explanation, with the relevant alternatives.
Quinn | Would those alternatives include what happens if I do not choose the proposed option?
Dr Lane | The appropriate [[reasonable alternative::A reasonable alternative is a relevant option requiring explanation in context.]] discussion includes the available choices and their implications in your circumstances.
Quinn | Sometimes I nod because I have heard a sentence, not because I have agreed to everything in it.
Dr Lane | Hearing or understanding is not the same as [[informed consent::Informed consent requires appropriate authorization after a meaningful discussion and is not established merely by a nod or comprehension of words.]]. We need to check the meaning and the decision separately.
Quinn | I also want the pain-relief arrangements explained if a procedure is being considered.
Dr Lane | We should explain the relevant [[analgesia::Analgesia concerns pain relief and should be discussed through the actual clinical arrangements rather than assumed from the procedure name.]] or anesthesia arrangements through the appropriate clinical discussion.
Quinn | Could you summarize the recommendation again in shorter sentences before asking what I understand?
Dr Lane | Yes. That is part of a useful [[consent discussion::A consent discussion addresses the proposed care, relevant information, questions, and authorization rather than treating a signature as the whole process.]], not a delay caused by asking an unreasonable question.
Quinn | Then my original preference is acknowledged, the changed situation is explained, and I can understand the actual options.
Dr Lane | That supports [[shared decision-making::Shared decision-making combines the actual clinical information with the person's informed preferences and questions, including when circumstances change.]] while respecting the real urgency and keeping you involved in the care discussion.''',
    rehearsal=['Read the corrected exchange, distinguishing a recommendation, understanding, and consent.', 'Swap roles. Acknowledge the preference without selecting a procedure or inventing urgency.'],
    transfer_title='A nod was only acknowledgment', transfer_setup='A patient clarifies that a nod meant the explanation was heard, not that consent was given. The clinician acknowledges the distinction and continues the actual consent process.',
    transfer='''Patient: "My nod meant I ___ the explanation." | heard | The patient clarifies that the nod acknowledged hearing the explanation.
Clinician: "It did not establish ___." | consent | Hearing an explanation does not automatically authorize the proposed intervention.
Patient: "I still have a ___." | question | The scenario continues the discussion rather than treating authorization as complete.
Clinician: "We will continue the appropriate ___." | process | The actual consent process continues with the patient's clarification acknowledged.'''))

BOOK['units'].append(unit(
    title='Giving a labor-ward handoff', scene='Separate the patient report from the monitor interpretation',
    skill='Transfer maternal and fetal information with sources, timing, outstanding tasks, and accepted responsibility.',
    brief='Dr Chen hands over patient Samira to Dr Ellis on the labor ward. Samira reports stronger contractions and asks that explanations precede examinations. The latest maternal observations and fetal-monitoring interpretation must be verified from the current clinical record; no values or trace classification are supplied here. The clinicians confirm outstanding tasks and responsibility without inventing findings.',
    cast='Dr Chen | Outgoing obstetrician\nDr Ellis | Receiving obstetrician',
    culture=('An efficient handoff still includes the patient', 'Include clinically relevant preferences as well as observations. Do not let a short report erase consent needs, source attribution, or unfinished work.'),
    a='''What does Samira report? | Stronger contractions | A verified trace category | A supplied cervical measurement | A completed birth | The case supplies the patient's report of stronger contractions only.
What preference should be handed over? | Explain before examinations | No questions ever | Automatic consent to every procedure | A companion makes every decision | Samira asks for explanations before examinations, which remains relevant to the next team.
What requires verification? | Current observations and monitoring interpretation | Samira's name in the brief | That a handoff occurs | The receiving clinician's role | The actual clinical values and interpretation must come from the current record.''',
    vocabulary='''labor progress | Change in the clinical course of labor over time. | describe labor progress
contraction pattern | Frequency, duration, and character of uterine contractions in context. | report the contraction pattern
cervical dilation | Opening of the cervix assessed during the relevant examination. | document cervical dilation
cervical effacement | Thinning of the cervix in the relevant clinical assessment. | describe cervical effacement
fetal station | Position of the presenting part relative to pelvic landmarks. | report fetal station
membrane status | Whether membranes are intact or ruptured as assessed. | clarify membrane status
rupture time | Reported or established time of membrane rupture. | verify rupture time
presenting part | Fetal part positioned toward the birth canal. | identify the presenting part
fetal heart-rate trace | Recorded fetal heart-rate information for clinical interpretation. | review the fetal heart-rate trace
baseline rate | Reference rate assessed over the relevant monitoring interval. | describe the baseline rate
variability | Fluctuation in fetal heart rate assessed within the monitoring context. | assess variability
deceleration | Decrease in fetal heart rate characterized in clinical context. | describe a deceleration
uterine activity | Pattern of uterine contractions or related activity. | assess uterine activity
maternal observations | Verified clinical measurements or findings concerning the patient. | relay maternal observations
working assessment | Current clinical interpretation subject to relevant review. | state the working assessment
outstanding task | Required action not yet completed. | identify outstanding tasks
handoff acceptance | Explicit acknowledgment of receiving information and responsibility. | confirm handoff acceptance
contingency plan | Agreed response to specified possible changes under the actual care plan. | clarify the contingency plan''',
    precision='Patient-reported contraction strength is not a fetal-monitoring interpretation. Use verified sources and timestamps for clinical findings.',
    precision_extra='The terminology bank is not a tracing algorithm or examination guide. No values, classification, or treatment response may be invented from this exercise.',
    phrases='''Lead with context | I am handing over Samira on the labor ward.
Attribute the report | Samira reports stronger contractions.
Preserve the preference | She asks for an explanation before each examination.
Verify the record | Let us check the current observations and their times.
Separate interpretation | The monitoring interpretation needs the actual reviewed trace.
Name unfinished work | This task remains outstanding.
Confirm responsibility | Please confirm who is taking responsibility for that step.
Close the transfer | I acknowledge the handoff and the unresolved items.''',
    notes='''Reports versus assessed | Separates the patient's experience from a professional measurement or interpretation.
Current and timed | Prevents an earlier finding from being repeated as though it were current.
Accepted versus sent | Makes responsibility explicit rather than treating a transmitted report as a completed handoff.''',
    d='''Which statement is source-aware? | Samira reports stronger contractions. | The trace is normal without review. | Dilation is invented from the report. | All observations are current without checking. | The statement accurately attributes the supplied information to the patient.
What does handoff acceptance add? | Confirmation of received information and responsibility | A new diagnosis by itself | A guarantee of outcome | Permission to ignore preferences | Acceptance closes the communication loop rather than merely recording that a message was sent.
Which finding cannot be invented? | A fetal trace classification | The reported contraction change | The request for explanation | The existence of a receiving clinician | No trace or classification is supplied in the case.
Why include the examination preference? | It remains relevant to communication and consent. | It replaces all clinical assessment. | It guarantees no examination is needed. | It removes the patient's involvement. | The preference guides the next team's explanation and does not disappear during handoff.''',
    dialogue='''Dr Chen | I am handing over Samira. She reports stronger contractions and asks for explanations before examinations; please retain that preference.
Dr Ellis | I acknowledge the report. Let us distinguish the patient account from the current verified observations and clinical interpretation.
Dr Chen | The reported change in the [[contraction pattern::Contraction pattern needs source attribution; patient report is not a measured finding.]] is her account, not a substitute for the actual assessment.
Dr Ellis | Understood. We should verify current findings and their times rather than copy an earlier summary as current.
Dr Chen | Let us review the latest [[maternal observations::Maternal observations require actual clinical findings and the relevant assessment time.]] in the current record together, including when each was taken.
Dr Ellis | Please also identify which assessment belongs to which time, particularly where the situation has changed.
Dr Chen | Any [[cervical dilation::Cervical dilation cannot be inferred from a report of stronger contractions.]] finding needs its actual examination source and time, not an inference from stronger contractions.
Dr Ellis | The same applies to membrane information: reported history and established findings should not be blended.
Dr Chen | Yes. [[Membrane status::Membrane status needs its actual source and current assessment context.]] and any rupture time require accurate attribution.
Dr Ellis | What about the fetal monitoring? I need the actual reviewed interpretation rather than a reassuring shorthand label.
Dr Chen | We need the current [[fetal heart-rate trace::A fetal heart-rate trace requires clinical interpretation, not inference from symptoms.]] and the authorized interpretation. No classification should be guessed from this conversation.
Dr Ellis | Terms such as variability have specific clinical meaning, so a language definition is not an interpretation rule.
Dr Chen | Correct. [[Variability::Variability describes fluctuations in fetal heart rate within the monitoring context and its definition does not provide a clinical interpretation algorithm.]] must be assessed in the real context, not assigned because the word appears in a handoff.
Dr Ellis | Let us identify which tasks are complete and which person is responsible for anything unfinished.
Dr Chen | Each [[outstanding task::An outstanding task is an action not yet completed and needs an explicit owner rather than an assumption that the next team knows.]] should remain visible, including the responsible clinician and relevant communication route.
Dr Ellis | I will confirm responsibility rather than simply say that the message has arrived.
Dr Chen | That gives us [[handoff acceptance::Handoff acceptance confirms receipt of the information and responsibility, making the transfer more than an unacknowledged message.]]. Samira's request for explanation remains part of the plan.
Dr Ellis | We also need any actual contingency arrangements explained, not an improvised response to a trace we have not reviewed.
Dr Chen | Agreed. The [[contingency plan::A contingency plan specifies responses under the actual care plan and cannot be invented from an incomplete language scenario.]] must come from the current clinical assessment and agreed care.
Dr Ellis | I accept the handoff, with the [[working assessment::A working assessment is the current clinical interpretation subject to review and must remain separate from unverified values or assumed conclusions.]], sources, unresolved items, and patient preference clearly distinguished.''',
    rehearsal=['Read the corrected handoff. Attribute the patient report separately from verified clinical findings.', 'Swap roles. Confirm responsibility without inventing a tracing category or examination value.'],
    transfer_title='An earlier observation was copied forward', transfer_setup='A handoff repeats an observation from 10:00 as current at 12:00. The receiving clinician identifies the timestamp error and requests the actual current record.',
    transfer='''Receiver: "That observation was recorded at ___." | 10:00 | The supplied observation belongs to the earlier 10:00 assessment.
Sender: "The handoff is occurring at ___." | 12:00 | The current handoff time is 12:00 in the scenario.
Receiver: "We need the actual ___ record." | current | The earlier value must not be presented as a current finding.
Sender: "I will correct the ___." | timestamp | The immediate communication error concerns the observation's time attribution.'''))

BOOK['units'].append(unit(
    title='Taking postpartum concerns seriously', scene='The birth date belongs in the urgent handoff',
    skill='Communicate recent pregnancy context and urgent symptoms without normalizing them as recovery.',
    brief='Twelve days after giving birth, patient Sloane reports shortness of breath and chest pain. The actual emergency response is already active. Dr Patel confirms the recent birth context and symptoms for the receiving team. No diagnosis or measured observations are supplied. This is language practice during an active response, not a guide for deciding whether postpartum symptoms can wait.',
    cast='Sloane | Postpartum patient\nDr Patel | Obstetrician',
    culture=('Recovery is not an explanation for every symptom', 'Do not dismiss a concern because the patient is tired or recently gave birth. The receiving service needs both current symptoms and relevant recent pregnancy history.'),
    a='''When did Sloane give birth? | Twelve days ago | Twelve years ago | Today | No birth is mentioned | The brief places the birth twelve days before this urgent concern.
Which symptoms are reported? | Shortness of breath and chest pain | A confirmed diagnosis | Normal oxygen measurements | No current symptoms | Sloane reports breathing difficulty and chest pain without an established cause.
What is already active? | The emergency response | A routine annual review | A completed discharge from this event | A language assessment only | The actual emergency response is active and must not be delayed.''',
    vocabulary='''postpartum period | Time after childbirth considered in the relevant care context. | identify the postpartum period
recent birth history | Relevant information about a birth that occurred recently. | communicate recent birth history
postpartum warning sign | Symptom or sign after birth requiring prompt attention. | report a postpartum warning sign
shortness of breath | Subjective difficulty or discomfort with breathing. | describe shortness of breath
chest pain | Pain or discomfort in the chest requiring contextual assessment. | report chest pain
thromboembolism | Obstruction caused by a blood clot traveling through circulation. | assess suspected thromboembolism
postpartum cardiomyopathy | Heart-muscle disorder arising around childbirth in the relevant clinical context. | evaluate postpartum cardiomyopathy
postpartum hemorrhage | Excessive bleeding after birth under the relevant clinical criteria. | assess postpartum hemorrhage
postpartum hypertension | High blood pressure occurring after birth in context. | evaluate postpartum hypertension
perinatal mental health | Mental health during pregnancy and the period around childbirth. | discuss perinatal mental health
intrusive thought | Unwanted thought experienced as distressing or inconsistent with wishes. | clarify an intrusive thought
suicidal thought | Thought involving ending one's own life. | ask directly about suicidal thoughts
functional change | Difference in ability to carry out ordinary activities. | describe functional change
urgent-care route | Actual service or process for prompt clinical attention. | confirm the urgent-care route
postpartum follow-up | Planned review of health and care needs after birth. | coordinate postpartum follow-up
handover context | Relevant background accompanying current clinical information. | preserve handover context
support network | People and services providing practical or emotional help. | identify the support network
continuity of care | Connected care across clinicians, services, and time. | maintain continuity of care''',
    precision='Shortness of breath and chest pain after birth require the actual urgent response. The terminology bank lists possible clinical concepts, not diagnoses established for Sloane.',
    precision_extra='Mental-health concerns also require appropriate assessment. An intrusive thought and an intention to act are not interchangeable; do not infer safety or risk classification from a glossary definition.',
    phrases='''State recent pregnancy | I gave birth twelve days ago.
Lead with the symptoms | I am reporting shortness of breath and chest pain.
Keep the context | Please include the recent birth in the handoff.
Avoid dismissal | We will not assume this is ordinary recovery.
Preserve diagnostic uncertainty | The cause has not yet been established.
Confirm urgent action | The emergency response is already active.
Separate routine follow-up | A scheduled postpartum visit does not replace urgent assessment.
Close the loop | We will confirm that the receiving team has the relevant history.''',
    notes='''After birth | Adds clinically relevant context without asserting that childbirth caused the symptom.
Not ordinary recovery by assumption | Rejects dismissal while leaving the actual diagnosis to assessment.
Routine versus urgent | Keeps a scheduled follow-up distinct from immediate clinical needs.''',
    d='''Which detail belongs near the start of the handoff? | Birth twelve days ago with current chest pain and breathlessness | Only the next routine appointment | An invented normal oxygen value | A diagnosis chosen from the glossary | The current symptoms and recent birth context are the supplied urgent communication priorities.
Which conclusion is unsupported? | The cause is postpartum cardiomyopathy. | The cause needs assessment. | Recent birth is relevant. | Emergency response is active. | The case supplies no diagnostic evidence establishing a particular cause.
What does a routine appointment not replace? | Actual urgent assessment | A calendar reminder | The patient's name | A document title | A future routine review is not a substitute for the active urgent clinical process.
Which mental-health distinction is important? | An intrusive thought is not automatically an intention to act. | Every unwanted thought proves intent. | Every thought is harmless without assessment. | A glossary establishes safety. | Thought content, distress, intention, and actual risk require appropriate assessment rather than automatic equivalence.''',
    dialogue='''Sloane | I gave birth twelve days ago, and now I have shortness of breath and chest pain. The emergency response is active.
Dr Patel | I will make sure the [[recent birth history::Recent birth history provides context that belongs alongside the current symptoms.]] is included with those symptoms as the actual response continues.
Sloane | I worried that saying I was tired after birth would make people think this was ordinary recovery.
Dr Patel | A [[postpartum warning sign::A postpartum warning sign must not be dismissed as ordinary tiredness.]] should not be dismissed because you recently gave birth or feel tired.
Sloane | I can describe how the breathing feels, but I do not know what diagnosis explains it.
Dr Patel | Describe the [[shortness of breath::Shortness of breath is a symptom; the patient need not diagnose its cause.]] in your own words. You do not need to choose a diagnosis before being heard.
Sloane | The chest discomfort is part of the same concern, and I want it passed on too.
Dr Patel | I will include the [[chest pain::Chest pain requires assessment and does not identify its cause by itself.]] clearly rather than reduce the handoff to a general statement that you feel unwell.
Sloane | Does mentioning the postpartum period prove that the birth caused whatever is happening?
Dr Patel | No. The [[postpartum period::The postpartum period identifies the time after childbirth and provides context without independently establishing the cause of a new symptom.]] is relevant context, not proof of a particular cause.
Sloane | I have heard several frightening medical names. Should I tell the team that I definitely have one of them?
Dr Patel | No. For example, [[thromboembolism::Thromboembolism is a clinical condition requiring appropriate assessment and is not established by appearing in a list of possible concerns.]] is not a diagnosis you should assign from a list of terms.
Sloane | And the same is true of the heart condition people sometimes mention around childbirth?
Dr Patel | Yes. [[Postpartum cardiomyopathy::Postpartum cardiomyopathy is a heart-muscle disorder requiring clinical evaluation and is not confirmed by the reported symptoms alone.]] requires the actual clinical evaluation; it has not been established in this conversation.
Sloane | I have a routine follow-up booked, but I understand that does not replace what is happening now.
Dr Patel | Correct. [[Postpartum follow-up::Postpartum follow-up is planned care after birth and does not replace urgent assessment of a new concerning symptom.]] and the active urgent response are different parts of care.
Sloane | Please confirm that the next team knows the timing of the birth, not only the symptoms.
Dr Patel | We will preserve that [[handover context::Handover context includes relevant background such as recent birth and must accompany the current symptom report to the receiving team.]] and confirm receipt through the actual clinical process.
Sloane | I want the teams to stay connected afterward as well, rather than assume another service has everything.
Dr Patel | That is part of [[continuity of care::Continuity of care connects information and responsibility across services and time, including after an urgent episode.]]. The immediate response remains the priority, with appropriate communication between services as care proceeds.''',
    rehearsal=['Read the corrected exchange. Put the birth timing and current symptoms at the start.', 'Swap roles. Distinguish urgent response from routine follow-up without naming a confirmed cause.'],
    transfer_title='Recent pregnancy was missing from the summary', transfer_setup='An urgent handoff lists current symptoms but omits that the patient gave birth twelve days ago. The receiving team acknowledges the added history. The response remains active.',
    transfer='''Sender: "The omitted detail is birth ___ days ago." | twelve | The scenario supplies a birth twelve days before the current concern.
Receiver: "I acknowledge the added ___." | history | The receiving team confirms receipt of the recent birth information.
Sender: "The response remains ___." | active | Adding the missing context does not interrupt the ongoing response.
Receiver: "The cause is not yet ___." | established | The added birth history does not independently establish a diagnosis.'''))

BOOK['units'].append(unit(
    title='Discussing confirmed pregnancy loss', scene='Clear words and space to respond',
    skill='Give difficult news directly and compassionately, then explain an individualized options discussion.',
    brief='After the appropriate clinical assessment has confirmed an early pregnancy loss, Dr Gray meets patient Eden. Eden asks whether the finding is certain and worries that an ordinary daily activity caused the loss. The cause has not been established. Dr Gray explains the confirmed finding, allows silence, asks about chosen support, and arranges discussion of the actual management options. No procedure, medicine, or follow-up interval is prescribed.',
    cast='Dr Gray | Obstetrician\nEden | Patient',
    culture=('Do not rush toward reassurance', 'Avoid minimizing phrases such as at least it was early or you can try again. State the confirmed finding clearly, allow a response, and ask what support the person wants.'),
    a='''What has been confirmed? | An early pregnancy loss after appropriate assessment | The cause of the loss | A selected management option | A future pregnancy outcome | The finding is confirmed, while cause and management choice remain separate questions.
What worries Eden? | That an ordinary activity caused the loss | That a procedure is already supplied | That no assessment occurred | That the future is guaranteed | Eden expresses self-blame about an ordinary daily activity.
What is not prescribed? | A management option or follow-up interval | Compassionate explanation | Space to respond | A support discussion | The case arranges an individualized discussion rather than prescribing treatment or timing.''',
    vocabulary='''early pregnancy loss | Loss of a pregnancy early in gestation under the relevant definition. | explain early pregnancy loss
miscarriage | Common term for spontaneous pregnancy loss in the relevant clinical context. | discuss a miscarriage
confirmed finding | Conclusion established through the appropriate assessment. | explain a confirmed finding
diagnostic uncertainty | Unresolved question about whether a diagnosis is established. | distinguish diagnostic uncertainty
viability assessment | Clinical assessment of whether a pregnancy is continuing as expected. | review the viability assessment
expectant management | Management involving observation under an appropriate clinical plan. | discuss expectant management
medical management | Management using prescribed medicines under the actual care plan. | explain medical management
surgical management | Management involving an appropriate procedure. | discuss surgical management
management preference | Person's informed preference among relevant care options. | elicit a management preference
retained pregnancy tissue | Pregnancy-related tissue remaining in the uterus in context. | assess retained pregnancy tissue
bleeding history | Account of bleeding timing, amount, and associated concerns. | obtain a bleeding history
follow-up assessment | Subsequent review of clinical status and care needs. | arrange follow-up assessment
bereavement support | Support offered after a significant loss. | offer bereavement support
self-blame | Belief that one is personally responsible for an adverse event. | respond to self-blame
empathetic silence | Deliberate space allowing a person to respond to difficult news. | allow empathetic silence
acknowledgment of loss | Direct recognition of the significance of the person's loss. | offer acknowledgment of loss
support preference | Person's wishes about who or what will support them. | ask about support preferences
care summary | Clear record of the finding, discussion, and agreed next steps. | provide a care summary''',
    precision='Here the loss is confirmed; its cause is not. Do not weaken a confirmed finding with misleading ambiguity or invent a cause to answer self-blame.',
    precision_extra='Management depends on the actual clinical situation and informed discussion. The vocabulary names options without supplying a regimen, procedure choice, or safe waiting period.',
    phrases='''Give clear news | I am sorry. The assessment has confirmed that the pregnancy has ended.
Allow space | We can pause here.
Separate certainty | The finding is confirmed; the cause has not been established.
Respond to blame | Nothing in this assessment establishes that your ordinary activity caused this.
Avoid minimization | I recognize that this is a significant loss for you.
Ask about support | Who would you like with you for the next discussion?
Introduce options gently | When you are ready, I will explain the options relevant to your situation.
Close concretely | We will provide the agreed care plan and the appropriate contact route.''',
    notes='''Confirmed versus suspected | Matches the certainty of the actual finding instead of using vague words to soften difficult news.
Cause versus finding | Explains that certainty about what happened does not establish why it happened.
When you are ready | Makes space within the actual clinical circumstances without promising unlimited delay or prescribing timing.''',
    d='''Which statement matches the case? | The loss is confirmed, but the cause is not established. | Both the loss and cause are guesses. | An ordinary activity definitely caused it. | A future outcome is guaranteed. | The case separates the confirmed clinical finding from the unresolved cause.
Which phrase minimizes the loss? | At least it was early. | I am sorry. | We can pause here. | Who would you like with you? | At least it was early imposes a minimizing comparison rather than acknowledging the person's experience.
What does empathetic silence allow? | Space for the person to respond | Avoidance of every necessary explanation | A substitute for clinical care | A guarantee that distress ends | A pause allows a response without rushing the person toward reassurance or a decision.
Which action is not supplied? | Selecting a management regimen | Explaining relevant options | Asking about support | Providing an agreed summary | The scenario supplies no treatment selection, medicine regimen, or clinical follow-up interval.''',
    dialogue='''Eden | Please tell me clearly what the assessment has established. Is the finding definite, or is there still uncertainty?
Dr Gray | I am sorry. The pregnancy has ended. This is a [[confirmed finding::The finding confirms loss; it does not establish why the loss occurred.]]. We can pause before discussing anything further.
Eden | I keep thinking about carrying groceries yesterday. Did something ordinary I did cause this?
Dr Gray | The assessment does not establish that cause. I hear the [[self-blame::Self-blame needs acknowledgment without inventing evidence that an ordinary activity caused loss.]], but we should not turn an ordinary activity into a proven explanation.
Eden | I do not want someone to tell me it does not matter because it happened early.
Dr Gray | It matters. [[Acknowledgment of loss::Acknowledgment of loss recognizes its significance rather than minimizing the experience.]] means recognizing your experience, not comparing it with someone else's.
Eden | Could we sit quietly for a moment before talking about procedures or what happens next?
Dr Gray | Yes. [[Empathetic silence::Empathetic silence allows a response without rushing toward reassurance or decisions.]] can be part of this conversation. I will stay with you while we pause.
Eden | I would like my sister involved, but only after I have understood the main information myself.
Dr Gray | We will respect that [[support preference::Support preference identifies whom the patient wants involved in the discussion.]] and discuss what you want shared when she joins us.
Eden | When we talk about care, will you explain the options rather than assume I already know the medical words?
Dr Gray | Yes. Where appropriate, [[expectant management::Expectant management involves observation under a clinical plan and is an option term, not an instruction here to wait without assessment.]] is one term we may discuss, with the actual circumstances and safety arrangements explained.
Eden | I have also seen references to medicines and procedures, but I do not know what applies to me.
Dr Gray | [[Medical management::Medical management uses prescribed medicines under the actual clinical plan; the term itself does not specify a regimen or establish suitability.]] and surgical management need their own explanations of suitability, benefits, risks, and alternatives.
Eden | I would like time to understand the choices within whatever the actual clinical situation allows.
Dr Gray | Your [[management preference::A management preference is the person's informed choice among relevant options and should be elicited after the actual clinical information is explained.]] belongs in that discussion. We will explain any real timing considerations rather than assume your decision.
Eden | I may need support after leaving, not just information during this appointment.
Dr Gray | We can discuss [[bereavement support::Bereavement support offers help after a significant loss and should be presented as available support rather than an obligation or a substitute for clinical care.]] and the appropriate clinical contact route, according to what would be helpful to you.
Eden | A clear summary would help me remember what was confirmed and what still needs to be decided.
Dr Gray | We will provide a [[care summary::A care summary records the confirmed finding, relevant discussion, and agreed next steps without presenting unresolved choices as already decided.]] that separates the finding, the unresolved cause, and the next steps actually agreed with you.''',
    rehearsal=['Read the corrected difficult-news conversation. Allow a pause after the confirmed finding.', 'Swap roles. Respond to self-blame without inventing a cause or minimizing the loss.'],
    transfer_title='The support person joins with permission', transfer_setup='Eden authorizes sharing the confirmed finding with her sister. Eden has not selected a management option. The clinician explains those two facts separately.',
    transfer='''Patient: "You may share the confirmed ___." | finding | Eden authorizes sharing the established finding with her sister.
Clinician: "The support person is your ___." | sister | The person joining the discussion is Eden's chosen sister.
Patient: "A management option is not yet ___." | selected | No management choice has been made in the supplied scenario.
Clinician: "I will keep those facts ___." | separate | Permission to share a finding does not establish a treatment decision.'''))
