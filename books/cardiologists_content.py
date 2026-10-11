"""Original cardiology consultations and interprofessional communication."""
from books.medical_support import medical_unit as unit, source, SCOPE

BOOK = dict(slug='cardiologists', title='Cardiology English', cover_label='ENGLISH FOR CARDIOLOGISTS',
    cover_title='Cardiology', cover_size=42, tagline='Explain the finding. Clarify the decision.',
    audience='For cardiologists, cardiology fellows, and physicians coordinating cardiovascular care.',
    roles='cardiologists, interventional cardiologists, electrophysiologists, cardiology fellows',
    summary='Cardiology English for urgent handoffs, rhythm monitoring, echocardiography, risk discussions, procedural consent, heart-failure care, and rehabilitation.',
    map_intro='Eight cardiovascular encounters practice urgency, rhythm evidence, imaging explanations, stroke and bleeding tradeoffs, procedure discussions, care plans, risk numbers, and rehabilitation handoffs.',
    notes_title='A precise finding is not the whole decision.',
    notes_intro='Cardiology moves between symptoms, electrical recordings, imaging, and probabilities. Clear language identifies the evidence source, explains what a number measures, and connects the next action to a responsible professional.',
    field_notes=[
        ('Lead urgent handoffs with the concern', 'Give the current concern and action already taken before background detail. Preserve unknowns and confirm acceptance without delaying the actual emergency response.', '"The emergency pathway is active; I am confirming the receiving team."'),
        ('Name the measurement', 'A percentage, rhythm label, or imaging estimate answers a particular question. Do not let patients mistake a measurement for a percentage of life remaining or a complete diagnosis.', '"Ejection fraction describes a pumping measurement, not how much of your heart is alive."'),
        ('Make comparisons comparable', 'Risk numbers need the same outcome, denominator, and time period. Explain absolute change as well as relative change using the supplied figures.', '"That is one fewer event per hundred over the stated period, not a personal guarantee."'),
        ('Keep the plan connected', 'A referral, device transmission, or discharge summary is not proof that follow-up occurred. Name the receiving clinician, outstanding question, and communication route.', '"The rehabilitation referral is sent; the first appointment is not yet confirmed."'),
    ], scope_note=SCOPE,
    sources=[
        source('American Heart Association. Ejection Fraction Heart Failure Measurement.', 'https://www.heart.org/en/health-topics/heart-failure/diagnosing-heart-failure/ejection-fraction-heart-failure-measurement', 'Background for explaining the measurement and why it is only part of a clinical assessment.'),
        source('American Heart Association. Atrial Fibrillation Medications.', 'https://www.heart.org/en/health-topics/atrial-fibrillation/treatment-and-prevention-of-atrial-fibrillation/atrial-fibrillation-medications', 'Context for distinct treatment goals and stroke/bleeding discussions, not a prescribing guide.'),
        source('American Heart Association. Coronary Angiogram.', 'https://www.heart.org/en/health-topics/heart-attack/diagnosing-a-heart-attack/coronary-angiogram', 'Background for explaining diagnostic coronary angiography and related terminology.'),
        source('American Heart Association. Cardiac Rehabilitation for Heart Failure.', 'https://www.heart.org/en/health-topics/heart-failure/treatment-options-for-heart-failure/cardiac-rehab-for-heart-failure', 'Context for medically supervised rehabilitation and practical access questions.')], units=[])

BOOK['units'].append(unit(
    title='Giving an urgent cardiovascular handoff', scene='Concern first, uncertainty intact',
    skill='Communicate a time-critical concern without assigning an unconfirmed diagnosis or delaying emergency care.',
    brief='Dr Vale hands over Chris, who reports chest pressure with breathlessness. The emergency response is already active. The cause, initial test results, and current measurements are not supplied in this exercise. Dr Chen is accepting the clinical handoff. The task is concise communication of reported symptoms, known actions, and unresolved information, not deciding whether chest discomfort is safe to wait.',
    cast='Dr Vale | Referring physician\nDr Chen | Receiving cardiologist',
    culture=('Urgent does not mean speculative', 'Use a clear opening and closed confirmation. Do not increase certainty to sound decisive, and do not postpone an active emergency response until a report sounds polished.'),
    a='''What symptoms are reported? | Chest pressure with breathlessness | A confirmed infarction | A normal examination | No current concern | The case supplies the symptom report without establishing its cause.
What is already active? | The emergency response | A routine appointment next month | A completed discharge | A prescribed medicine from this exercise | The emergency response begins before the communication exercise.
Who accepts the handoff? | Dr Chen | Chris's employer | An unnamed waiting-list clerk | Nobody | Dr Chen is the receiving cardiologist explicitly accepting the report.''',
    vocabulary='''acute coronary syndrome | Group of urgent conditions involving reduced coronary blood flow. | evaluate suspected acute coronary syndrome
myocardial ischemia | Inadequate blood supply to heart muscle relative to its needs. | assess myocardial ischemia
myocardial infarction | Heart-muscle injury and death caused by ischemia under diagnostic criteria. | confirm myocardial infarction
retrosternal | Located behind the breastbone. | describe retrosternal discomfort
exertional symptom | Symptom associated with physical effort. | clarify exertional symptoms
rest symptom | Symptom occurring without physical exertion. | report symptoms at rest
diaphoresis | Marked sweating, described in clinical context. | report associated diaphoresis
dyspnea | Subjective sensation of difficult or uncomfortable breathing. | describe reported dyspnea
troponin | Cardiac-injury biomarker interpreted with timing and clinical context. | interpret a troponin result
serial testing | Repeated testing over a defined clinical sequence. | explain serial testing
hemodynamic status | State of circulation assessed through relevant clinical information. | communicate hemodynamic status
initial assessment | First clinical evaluation in the relevant encounter. | report the initial assessment
prehospital report | Clinical information collected before arrival at the receiving hospital. | relay the prehospital report
emergency activation | Initiation of the relevant emergency-response process. | confirm emergency activation
symptom trajectory | Pattern of symptom change over time. | describe the symptom trajectory
receiving team | Professionals accepting the next stage of care. | identify the receiving team
time-critical concern | Concern requiring prompt action within the relevant clinical process. | communicate a time-critical concern
closed-loop escalation | Urgent communication that includes confirmation of receipt and responsibility. | complete closed-loop escalation''',
    precision='Chest pressure and breathlessness are reported symptoms, not a confirmed infarction. Missing measurements must remain missing; the exercise cannot classify urgency or establish a diagnosis.',
    precision_extra='Emergency activation and information transfer happen together. Do not wait for every detail or a language correction before following the real emergency process.',
    phrases='''Lead with the concern | I am handing over chest pressure with breathlessness.
State the action | The emergency response is already active.
Avoid invention | I do not have a verified measurement to report.
Separate diagnosis | The cause is not established in this handoff.
Request acceptance | Please confirm that your team is receiving the patient and report.
Preserve timing | I will distinguish reported onset from the time of our assessment.
Correct immediately | That detail needs correction before it is repeated.
Close the loop | I have your acknowledgment and the receiving contact.''',
    notes='''Reports | Attributes symptoms to the patient rather than presenting an unverified finding as measured.
Already active | Identifies an emergency action that must not wait for this conversation to finish.
Confirm receiving | Requests acceptance instead of assuming that a sent message completed the transfer.''',
    d='''Which opening is strongest? | Chest pressure with breathlessness; the emergency response is active. | A small issue may need discussion eventually. | A confirmed infarction with invented results. | No concern because no results are shown. | Naming the symptoms and active response communicates the actual concern and action without adding unsupported findings.
Which result must not be invented? | A normal troponin | The reported chest pressure | The accepted handoff | The active emergency response | No troponin result is supplied, so normal cannot be inserted as reassurance.
What completes the communication loop? | Confirmation of the receiving team and responsibility | An unanswered voicemail alone | A guessed diagnosis | A promise that nothing can change | Closed-loop communication requires acknowledgment rather than merely attempted contact.
What should not delay emergency care? | Completing every detail of this language exercise | The actual local emergency pathway | The receiving clinician's assessment | Necessary clinical action | The exercise is for language practice and must never replace or delay the real response.''',
    dialogue='''Dr Vale | I am handing over Chris, who reports chest pressure with breathlessness. The emergency response is already active.
Dr Chen | I am receiving the report. Keep this [[time-critical concern::A time-critical concern requires the active clinical response while the handoff conveys known facts and unresolved information.]] with the clinical team while we clarify the verified information.
Dr Vale | I will separate what Chris reports from what our team has actually observed or measured.
Dr Chen | Good. Report [[dyspnea::Dyspnea is the reported breathing difficulty; the term does not by itself establish a cause or measurement.]] as a symptom, and do not convert it into a diagnosis without the evidence.
Dr Vale | I do not yet have verified current measurements to pass on. I will update you as they become available.
Dr Chen | Then do not describe the [[hemodynamic status::Hemodynamic status requires relevant circulatory assessment and cannot be called normal from missing measurements.]] as normal. Missing information must stay visible while the real assessment continues.
Dr Vale | I also need to distinguish the patient's reported onset from the time someone first contacted the service.
Dr Chen | Yes. The [[prehospital report::The prehospital report contains information collected before hospital arrival and needs accurate source and timing attribution.]] should retain its source and timing rather than be blended with later observations.
Dr Vale | I have not labeled this a confirmed infarction. The symptoms justify concern, but the cause is unestablished here.
Dr Chen | Correct. [[Myocardial infarction::Myocardial infarction is a diagnosis requiring appropriate evidence and is not established by the supplied symptom report alone.]] is not a substitute label for every chest-pressure report.
Dr Vale | Nor should an absent test result be treated as a negative test that rules out the concern.
Dr Chen | Exactly. We are still awaiting the [[troponin::Troponin is interpreted as a cardiac-injury biomarker with timing and context; no value is supplied in this case.]] result. Please include the sampling time when you pass it on.
Dr Vale | I will send any verified update through the active pathway rather than leave a separate routine message.
Dr Chen | Please do. The [[receiving team::The receiving team accepts the next stage of care and needs updates through the active clinical channel.]] needs to know which facts are new and who is responsible for them.
Dr Vale | Shall I wait until every field is complete before confirming transfer of the report?
Dr Chen | No. [[Emergency activation::Emergency activation initiates the relevant urgent response and must not be delayed while a language report is perfected.]] is already underway; do not interrupt necessary care to perfect the wording.
Dr Vale | I will identify the unfinished information explicitly and confirm the contact for further clinical updates.
Dr Chen | That supports [[closed-loop escalation::Closed-loop escalation includes acknowledgment and accepted responsibility, not simply sending information without confirmation.]]. I acknowledge the concern and am accepting this handoff through our clinical process.
Dr Vale | Understood. Reported symptoms, active response, unresolved cause, and no invented measurements or results.
Dr Chen | Correct. Continue communicating the [[symptom trajectory::Symptom trajectory describes how symptoms change over time and should be reported accurately as new information becomes available.]] as verified information becomes available, alongside the real clinical response.''',
    rehearsal=['Read the corrected urgent handoff. Lead with the symptom report and emergency action.', 'Swap roles. Repeat the acceptance and missing-information statements without inserting measurements or a diagnosis.'],
    transfer_title='A corrected onset time', transfer_setup='During an active emergency handoff, the patient clarifies that symptoms began at 09:10, not 09:40. The receiving clinician acknowledges the correction. No cause is established.',
    transfer='''Referrer: "The corrected reported onset is ___." | 09:10 | 09:10 is the corrected onset time; it replaces the original report of 09:40.
Receiver: "The previously reported onset time of ___ has been superseded." | 09:40 | 09:40 was reported first but is now replaced by 09:10. "Previously reported" refers to the order of the reports, not which clock time is earlier.
Referrer: "The emergency response remains ___." | active | Correcting the history does not interrupt the active emergency response.
Receiver: "The cause remains ___." | unestablished | The timing correction does not itself establish a diagnosis.'''))

BOOK['units'].append(unit(
    title='Explaining ambulatory rhythm monitoring', scene='A symptom marker is not a diagnosis',
    skill='Explain what a rhythm recording can show and obtain a usable symptom account without promising detection.',
    brief='Ellis describes intermittent palpitations. Dr Mora proposes an ambulatory recording to compare symptoms with heart rhythm. No arrhythmia has been established in this case. Ellis will receive device-specific instructions from the service. A symptom diary and event marker may help interpretation; they do not themselves diagnose the sensation or guarantee that every episode will be captured.',
    cast='Ellis | Patient\nDr Mora | Cardiologist',
    culture=('Explain the purpose before the equipment', 'A patient needs to know what question the monitor addresses, not just how long it is worn. Keep emergency instructions separate from routine recording instructions.'),
    a='''What is the proposed purpose? | Compare symptoms with recorded rhythm | Guarantee every episode is captured | Prove an arrhythmia already exists | Replace all urgent assessment | The proposed recording explores symptom-rhythm relationships without a guaranteed diagnosis.
What is not established? | An arrhythmia | Ellis's symptom report | A proposed recording | The need for instructions | The case supplies palpitations but no confirmed rhythm diagnosis.
Who provides equipment instructions? | The service using the actual device | A guessed universal script | Another patient | The learner inventing settings | Instructions must match the actual device and service, not assumptions in the exercise.''',
    vocabulary='''palpitations | Awareness of the heartbeat as unusual, forceful, fast, or irregular. | describe palpitations
electrocardiogram | Recording of the heart's electrical activity. | interpret an electrocardiogram
arrhythmia | Abnormality of heart rhythm. | investigate a suspected arrhythmia
sinus rhythm | Rhythm originating from the heart's usual sinus-node pacemaker. | identify sinus rhythm
ectopic beat | Beat arising outside the usual initiating site. | describe an ectopic beat
ambulatory monitor | Device recording heart rhythm during everyday activity. | fit an ambulatory monitor
event marker | Device feature marking a time for later review. | use the event marker
symptom diary | Record of symptoms, times, and relevant activity. | keep a symptom diary
recording period | Time during which the device collects data. | confirm the recording period
symptom-rhythm correlation | Relationship between reported symptoms and rhythm at the relevant time. | assess symptom-rhythm correlation
paroxysmal | Occurring in episodes with onset and offset. | describe paroxysmal symptoms
bradycardia | Heart rate slower than expected in the relevant context. | assess bradycardia
tachycardia | Heart rate faster than expected in the relevant context. | assess tachycardia
conduction | Transmission of electrical impulses through the heart. | evaluate cardiac conduction
electrode lead | Electrical recording connection used in acquiring a trace. | check an electrode lead
signal artifact | Distortion in a recording not representing the true underlying signal. | identify signal artifact
signal quality | Adequacy of the recorded signal for interpretation. | assess signal quality
monitor return | Process of returning equipment or transmitting its recorded data. | confirm monitor return''',
    precision='Palpitations are a symptom; arrhythmia is a rhythm finding. A marked event helps locate information but does not itself diagnose it.',
    precision_extra='A routine monitor is not a substitute for the service\'s urgent-care instructions. Do not advise waiting for a recording review when new concerning symptoms require actual assessment.',
    phrases='''Explain the purpose | We want to compare what you feel with the rhythm at that time.
Separate symptom and finding | Palpitations do not name a specific rhythm by themselves.
Limit the promise | The recording may not capture every episode.
Make the diary useful | Include the time, what you felt, and what you were doing.
Clarify the marker | The marker identifies a time for review, not a diagnosis.
Use the actual instructions | The service will explain this device's controls and restrictions.
Separate urgent care | Follow the urgent-care instructions rather than waiting for the monitor report.
Close the process | Let us confirm how the recording reaches the reviewing team.''',
    notes='''At that time | Connects the reported sensation with the corresponding recording interval.
May not capture | Expresses a limitation without implying that the recording is useless.
Rather than waiting | Separates an urgent-care route from routine data collection.''',
    d='''Which distinction is correct? | Palpitations are a symptom; an arrhythmia is a rhythm abnormality. | Every palpitation proves an arrhythmia. | A diary is a diagnosis. | A marker guarantees a dangerous rhythm. | The symptom and the electrical finding require correlation rather than automatic equivalence.
What makes a diary entry useful? | Time, sensation, and activity | Only the patient's opinion of the device color | A diagnosis invented at home | An unrelated appointment number | The relevant details help connect a reported event with the corresponding recorded interval.
Which promise is unsupported? | Every episode will definitely be captured. | The device has specific instructions. | The recording needs interpretation. | A marker identifies an event time. | A finite recording may not capture every intermittent symptom or produce a definitive explanation.
What must remain separate? | Urgent-care instructions and routine monitor review | Symptom time and the corresponding trace | A device and its actual instructions | The report and its reviewing team | Routine recording does not replace appropriate urgent assessment of concerning clinical changes.''',
    dialogue='''Ellis | My heart sometimes feels as though it skips and then thumps. Is that enough to name the rhythm problem?
Dr Mora | Those are [[palpitations::Palpitations describe the awareness of an unusual heartbeat and do not by themselves identify a specific rhythm abnormality.]], a symptom description. We need appropriate evidence before naming a particular rhythm.
Ellis | The episodes come and go. They never seem to happen at the exact moment someone checks me.
Dr Mora | An [[ambulatory monitor::An ambulatory monitor records rhythm during everyday activity and may help investigate symptoms that are intermittent.]] can record during ordinary activity, helping us look for a relationship with the episodes.
Ellis | Does agreeing to the monitor mean you have already diagnosed an arrhythmia from my account?
Dr Mora | No. An [[arrhythmia::An arrhythmia is an abnormal heart rhythm, which has not been established by this symptom account.]] has not been established in this case. The recording is part of investigating the question.
Ellis | What should I record when I notice the feeling, besides pressing whatever button the device has?
Dr Mora | The service will explain the device. A [[symptom diary::A symptom diary records the sensation, timing, and activity so the reviewing clinician can interpret events in context.]] should include the time, what you feel, and what you are doing.
Ellis | And pressing a marker does not mean the device has instantly told me what caused the sensation?
Dr Mora | Correct. The [[event marker::An event marker identifies a time for subsequent review and does not itself diagnose the event.]] identifies a time to review; it is not itself a diagnosis or a promise of real-time assessment.
Ellis | I am worried I will wear it and nothing will happen during the recording period.
Dr Mora | That is a possible limitation. We are seeking [[symptom-rhythm correlation::Symptom-rhythm correlation compares the reported experience with the recorded rhythm at the relevant time.]], and the available recording may not capture every intermittent event.
Ellis | If the trace looks strange while I move, will every unusual line be treated as a heart problem?
Dr Mora | No. [[Signal artifact::Signal artifact is distortion that may arise during recording and must be distinguished from the underlying cardiac signal.]] can affect recordings, so quality and context matter to the interpretation.
Ellis | Then I should follow the actual device instructions rather than borrow instructions from a friend's different monitor.
Dr Mora | Yes. Those instructions help protect [[signal quality::Signal quality concerns whether the recording is adequate for interpretation and depends on the actual equipment and circumstances.]] and explain the controls, restrictions, and reporting process for this device.
Ellis | If I develop a concerning new symptom, I should not assume pressing the marker replaces asking for help.
Dr Mora | Exactly. Follow the actual urgent-care instructions; the [[recording period::The recording period is the data-collection interval and is not a reason to defer necessary urgent clinical assessment.]] is not permission to delay needed clinical assessment.
Ellis | I also want to know how you receive the recording and when the team explains its findings.
Dr Mora | We will confirm the [[monitor return::Monitor return is the equipment or data-return process needed for review and should not be left as an assumed final step.]] process and the service's review arrangements, without promising a result the data may not establish.''',
    rehearsal=['Read the corrected monitoring discussion. Contrast symptom, marker, and interpreted rhythm.', 'Swap roles. Repeat the device-instruction and urgent-care distinctions without inventing equipment settings.'],
    transfer_title='A diary time needs clarification', transfer_setup='A diary says an episode occurred at 7, without morning or evening. The reviewing team asks Ellis to clarify before matching it to the trace. No rhythm conclusion is supplied.',
    transfer='''Reviewer: "The entry gives seven but not morning or ___." | evening | The time is incomplete because its morning-or-evening context is missing.
Ellis: "I need to ___ that detail." | clarify | Clarification is required before assigning the diary entry to a recording interval.
Reviewer: "Then we can match it to the ___." | trace | The purpose is to compare the clarified symptom time with the rhythm recording.
Ellis: "No rhythm conclusion has been ___." | supplied | The scenario provides a data clarification, not a diagnosed rhythm.'''))

BOOK['units'].append(unit(
    title='Explaining an echocardiogram', scene='A percentage is not the amount of heart left',
    skill='Translate an imaging measurement into plain English without reducing the whole assessment to one number.',
    brief='Ren reads an echocardiogram report containing a left-ventricular ejection-fraction measurement. No numerical value or heart-failure diagnosis is supplied. Ren thinks the percentage describes how much heart muscle is still alive. Dr Kim explains what the measurement represents and why symptoms, structure, filling, valves, and other findings also matter.',
    cast='Ren | Patient\nDr Kim | Cardiologist',
    culture=('Ask what the number means to the listener', 'A percentage can sound intuitive while being misunderstood. Establish the patient\'s interpretation before adding ranges or categories that may create a second misunderstanding.'),
    a='''What does Ren misunderstand? | The meaning of the ejection-fraction percentage | The appointment date | A prescribed dose | A confirmed valve procedure | Ren thinks the percentage measures remaining living heart muscle, which is not what it describes.
What is not supplied? | A numerical value or heart-failure diagnosis | An echocardiogram report | Ren's question | A clinician explanation | The exercise provides a terminology discussion without an individual value or diagnosis.
What else belongs in interpretation? | Symptoms and other cardiac findings | Only the percentage | The report's font size | A guessed comparison | The brief explicitly places the measurement within a broader clinical and imaging assessment.''',
    vocabulary='''echocardiogram | Ultrasound examination of heart structure and function. | explain an echocardiogram
ejection fraction | Proportion of ventricular blood volume expelled with a contraction. | explain left-ventricular ejection fraction
systole | Phase of the cardiac cycle involving ventricular contraction and ejection. | describe systolic function
diastole | Phase involving ventricular relaxation and filling. | describe diastolic filling
left ventricle | Heart chamber pumping blood into the systemic circulation. | assess the left ventricle
right ventricle | Heart chamber pumping blood toward the lungs. | assess the right ventricle
stroke volume | Amount of blood ejected by a ventricle in one beat. | distinguish stroke volume
preserved ejection fraction | Ejection fraction within the relevant preserved category despite possible other dysfunction. | discuss preserved ejection fraction
reduced ejection fraction | Ejection fraction below the relevant category threshold in context. | explain reduced ejection fraction
valvular regurgitation | Backward flow through a valve that does not close adequately. | assess valvular regurgitation
valvular stenosis | Narrowing that restricts flow through a heart valve. | explain valvular stenosis
wall motion | Movement of heart-muscle segments during the cardiac cycle. | assess regional wall motion
diastolic function | Ventricular relaxation and filling characteristics. | assess diastolic function
structural heart disease | Abnormality of heart anatomy or associated structures. | investigate structural heart disease
ventricular volume | Amount of blood within a ventricle at a specified phase. | measure ventricular volume
pressure estimate | Indirect approximation of pressure from available measurements. | qualify a pressure estimate
image quality | Adequacy of images for the intended interpretation. | describe image quality
comparison study | Earlier examination used to evaluate change. | review a comparison study''',
    precision='Ejection fraction is a pumping proportion, not a percentage of living heart tissue or life expectancy. It is not the whole assessment of cardiac function.',
    precision_extra='Preserved ejection fraction does not, by itself, exclude heart failure. Interpret the actual measurement with the clinical context and other findings; this case supplies no diagnostic category.',
    phrases='''Check the interpretation | What did that percentage suggest to you?
Define the measurement | It describes the proportion of blood pushed out with a contraction.
Correct gently | It is not the percentage of your heart that is still alive.
Name the chamber | This report refers to the left ventricle.
Broaden the picture | Filling, valves, symptoms, and other findings also matter.
Qualify the image | The report should state any important image-quality limitation.
Avoid a single-number diagnosis | We cannot interpret the whole situation from one number alone.
Separate a comparison | A change needs a comparable earlier study and clinical context.''',
    notes='''Proportion versus amount | Ejection fraction is a proportion, whereas stroke volume is an amount per beat.
Not the percentage of | Corrects exactly what the number does not measure.
By itself | Limits the conclusion supported by one measurement without dismissing its usefulness.''',
    d='''What does ejection fraction measure? | A proportion of ventricular blood expelled with contraction | The percentage of living heart tissue | Life expectancy in percent | The percentage of arteries without narrowing | The measurement concerns pumping from a ventricle, not tissue survival or a global health percentage.
Which statement is accurate? | Preserved ejection fraction alone does not exclude heart failure. | A preserved value proves every cardiac function is normal. | The percentage is a prognosis timetable. | A low value identifies every cause. | Heart failure and cardiac function require the full clinical and imaging context.
Which distinction is useful? | Stroke volume is an amount; ejection fraction is a proportion. | Both mean the number of heartbeats. | Both measure the patient's age. | Neither refers to pumping. | The terms describe related but different ways of expressing ventricular ejection.
Which conclusion exceeds this case? | Ren has a specific heart-failure category. | Ren has a report. | The terminology needs explanation. | No numerical value is supplied. | The scenario intentionally supplies neither an individual measurement nor a diagnosis.''',
    dialogue='''Ren | The report gives a percentage. I thought it meant that only that much of my heart is still alive.
Dr Kim | [[Ejection fraction::Ejection fraction is the proportion of ventricular blood expelled with a contraction, not the proportion of living heart tissue.]] does not measure how much heart tissue remains alive. Let me explain what the number represents.
Ren | Please do. I have been thinking of it as a percentage score for the whole heart.
Dr Kim | This measurement concerns the [[left ventricle::The left ventricle is the chamber pumping blood into the body's systemic circulation and is the chamber named in this report.]], the chamber that pumps blood toward the body.
Ren | What is the percentage actually a percentage of, if it is not the amount of working muscle?
Dr Kim | It relates the blood expelled to the [[ventricular volume::Ventricular volume is the blood in the chamber at a specified phase and provides the relevant basis for the pumping proportion.]] before that contraction. It describes a pumping proportion.
Ren | Then a report using an amount of blood per beat would be describing something related but different?
Dr Kim | Yes. [[Stroke volume::Stroke volume is the amount ejected in one beat, which differs from expressing that ejection as a proportion.]] is an amount per beat, while ejection fraction expresses a proportion.
Ren | I also saw systolic and diastolic in the report. Are those two different parts of the heartbeat?
Dr Kim | [[Systole::Systole includes ventricular contraction and ejection and is distinct from the relaxation and filling phase.]] involves contraction and ejection. Diastole involves relaxation and filling; both are relevant to function.
Ren | So the part about filling is not just an extra technical detail that can be ignored?
Dr Kim | Correct. [[Diastolic function::Diastolic function concerns relaxation and filling and can matter even when a pumping proportion appears preserved.]] is part of the assessment, along with structure, valves, symptoms, and other findings.
Ren | If someone has a preserved percentage, does that prove they cannot have heart failure?
Dr Kim | No. [[Preserved ejection fraction::Preserved ejection fraction describes a measurement category and does not by itself exclude heart failure or other dysfunction.]] alone does not exclude it. We need the complete clinical picture, not just that label.
Ren | I understand. The report also discusses a valve, which I assumed the percentage already covered.
Dr Kim | Valve findings are assessed separately. For example, [[valvular regurgitation::Valvular regurgitation means backward flow through a valve and is not synonymous with an ejection-fraction measurement.]] describes backward flow through a valve, not the ejection fraction itself.
Ren | What if part of the scan was hard to see clearly? Should that limitation be explained too?
Dr Kim | Yes. Important [[image quality::Image quality affects what an examination can establish and relevant limitations should remain visible in the interpretation.]] limitations should be stated rather than hidden behind a precise-looking number.
Ren | Then I should ask how this fits the rest of the assessment, not treat it as an isolated score.
Dr Kim | Exactly. Any [[comparison study::A comparison study is an earlier examination used to assess change and must be interpreted for comparability and context.]] also needs context. We will explain the actual findings without inventing a diagnosis from one measurement.''',
    rehearsal=['Read the corrected echo explanation. Contrast proportion, amount, and living tissue.', 'Swap roles. Repeat the preserved-ejection-fraction explanation without assigning Ren a diagnosis.'],
    transfer_title='A comparison needs context', transfer_setup='A report cites an earlier scan, but the cardiologist has not yet reviewed whether the studies are comparable. No meaningful change has been established.',
    transfer='''Patient: "The report refers to an earlier ___." | scan | An earlier examination is mentioned as a potential comparison.
Clinician: "I still need to review whether they are ___." | comparable | Comparability is unresolved and cannot be assumed from the existence of two reports.
Patient: "A meaningful change is not ___." | established | The case supplies no completed interpretation of a change.
Clinician: "We will interpret the findings in ___." | context | The relevant clinical and examination context must accompany the comparison.'''))

BOOK['units'].append(unit(
    title='Discussing atrial-fibrillation treatment goals', scene='The rhythm question and the stroke question',
    skill='Separate symptom control from stroke prevention while explaining a benefit-and-bleeding discussion.',
    brief='Avery has an established atrial-fibrillation diagnosis and asks why stroke prevention is discussed when the heartbeat feels calmer. Dr Patel will explain that symptom or rhythm management and stroke prevention address related but different questions. No risk score, medicine selection, dose, or instruction to stop treatment is supplied. Avery is worried about bleeding and wants that concern included.',
    cast='Avery | Patient\nDr Patel | Cardiologist',
    culture=('Explain why two goals remain on the agenda', 'Feeling better can be mistaken for proof that every risk has disappeared. Acknowledge the improvement while explaining the separate question and taking bleeding concerns seriously.'),
    a='''What diagnosis is established? | Atrial fibrillation | A new stroke in this case | A bleeding disorder diagnosed here | No rhythm diagnosis | The brief explicitly identifies atrial fibrillation as an established diagnosis.
What does Avery ask about? | Why stroke prevention matters when symptoms feel calmer | A dose already supplied | A confirmed procedure date | A guaranteed risk-free medicine | Avery links improved sensations with a question about continuing risk discussion.
What is absent from the case? | A medicine selection or risk score | Avery's bleeding concern | The diagnosis | A consultation | No individual score, prescription, dose, or stopping instruction may be invented.''',
    vocabulary='''atrial fibrillation | Irregular atrial electrical activity producing an irregular heart rhythm. | explain atrial fibrillation
atrial flutter | Organized rapid atrial rhythm distinct from atrial fibrillation. | distinguish atrial flutter
rate control | Strategy aimed at controlling heart rate. | discuss rate control
rhythm control | Strategy aimed at restoring or maintaining an appropriate rhythm. | discuss rhythm control
anticoagulation | Treatment reducing blood's ability to form clots through coagulation pathways. | review anticoagulation
antiplatelet therapy | Treatment reducing platelet activity in clot formation. | distinguish antiplatelet therapy
stroke risk | Likelihood of stroke in a defined clinical context and period. | assess stroke risk
bleeding risk | Likelihood of bleeding under relevant clinical circumstances. | assess bleeding risk
thromboembolism | Obstruction caused by a clot traveling from another site. | discuss thromboembolism
cardioversion | Intervention intended to restore an appropriate heart rhythm. | explain cardioversion
catheter ablation | Procedure targeting tissue involved in an abnormal rhythm. | discuss catheter ablation
left atrial appendage | Pouch-like structure attached to the left atrium. | explain the left atrial appendage
renal function | How effectively the kidneys perform their relevant functions. | review renal function
drug interaction | Effect of one medicine or substance on another's action. | check for a drug interaction
shared treatment decision | Care choice informed by evidence and the person's priorities. | reach a shared treatment decision
bleeding history | Account of previous bleeding events and related circumstances. | clarify the bleeding history
individual risk estimate | Context-dependent estimate for a person's likelihood of an outcome. | explain an individual risk estimate
anticoagulation review | Clinical reassessment of anticoagulant use and relevant risks. | arrange an anticoagulation review''',
    precision='Feeling fewer palpitations does not, by itself, settle the stroke-prevention decision. Do not derive an instruction to start or stop a medicine from this language exercise.',
    precision_extra='Anticoagulants and antiplatelets are not interchangeable labels. Explain their roles accurately within the individual clinical discussion rather than treating all "blood thinners" as identical.',
    phrases='''Separate the goals | Calming symptoms and preventing stroke are related but different goals.
Acknowledge improvement | It is useful to hear that the heartbeat feels calmer.
Keep assessment individual | We need to assess your stroke and bleeding risks in context.
Invite the concern | What worries you most about bleeding?
Clarify a colloquial term | Blood thinner can refer to medicines with different actions.
Avoid an instruction | This explanation is not a direction to stop your medicine.
Explore the history | Tell me about any previous bleeding and the circumstances.
Agree on review | Let us review the relevant information before settling the plan.''',
    notes='''Related but different | Connects the goals without treating one as a substitute for the other.
By itself | Limits the significance of improved symptoms for a separate risk decision.
Before settling | Keeps the choice open until the required individual review is complete.''',
    d='''Which distinction is correct? | Rhythm or symptom control does not replace the stroke-prevention assessment. | Calmer symptoms prove stroke risk is zero. | Every medicine has the same action. | A procedure automatically settles all future risk decisions. | Treatment goals overlap but require their own relevant clinical assessment.
Which question includes Avery's concern? | What previous bleeding have you experienced, and what worries you? | Why are you being difficult about risk? | Can we ignore bleeding? | You agree there can be no harm? | Asking about previous bleeding and worries elicits relevant history without minimizing the concern.
Which instruction cannot be supplied here? | Stop anticoagulation because the heartbeat feels calmer. | Discuss the goals separately. | Clarify the medicine name. | Review the bleeding history. | The case gives no medication-change instruction or evidence for making one.
Why clarify blood thinner? | The informal phrase can hide different medicine actions. | It always identifies one exact product. | It proves the dose. | It means the blood becomes water. | The phrase is colloquial and does not distinguish anticoagulants from other therapies.''',
    dialogue='''Avery | My heartbeat feels calmer now. Why are we still discussing stroke prevention as though nothing has changed?
Dr Patel | With [[atrial fibrillation::Atrial fibrillation is the established rhythm diagnosis here, and its care includes distinct symptom and stroke-risk questions.]], symptom improvement and stroke prevention are related but different parts of care.
Avery | I assumed that if I felt fewer episodes, the risk question would disappear with the symptoms.
Dr Patel | Feeling better is valuable, but [[stroke risk::Stroke risk requires individual assessment and cannot be assumed absent merely because palpitations feel less noticeable.]] cannot be judged from how noticeable the heartbeat feels alone.
Avery | Please explain the terms rate control and rhythm control. They sound as though they mean exactly the same thing.
Dr Patel | [[Rate control::Rate control aims at controlling heart rate and is distinct from a strategy focused on restoring or maintaining rhythm.]] concerns the heart rate; rhythm control concerns the rhythm itself. Neither phrase alone settles the prevention decision.
Avery | I would like the bleeding concern discussed as carefully as the benefit, not treated as a reason to stop asking.
Dr Patel | We should assess [[bleeding risk::Bleeding risk is a relevant part of the individualized benefit-and-harm discussion and should not be dismissed.]] and your concerns alongside the possible benefit of a proposed option.
Avery | I have called all these medicines blood thinners, but perhaps that hides an important difference.
Dr Patel | Yes. [[Anticoagulation::Anticoagulation acts on coagulation pathways and is not simply another name for every medicine informally called a blood thinner.]] and antiplatelet treatment have different actions. We should use the actual medicine name and purpose.
Avery | I had bleeding in the past, but I am not sure which details are relevant for this discussion.
Dr Patel | Tell me what happened and when. Your [[bleeding history::Bleeding history records previous events and their circumstances and is relevant to an individualized clinical review.]] deserves a careful account rather than an unexplained yes-or-no label.
Avery | Will other medicines and health conditions also affect how you judge the options for me?
Dr Patel | Yes. A [[drug interaction::A drug interaction can change a medicine's effects and belongs in review of the actual medicines and clinical context.]], kidney function, and other relevant factors may need review in the actual assessment.
Avery | Then a general chart online cannot tell me precisely which treatment I should take or at what dose.
Dr Patel | Correct. An [[individual risk estimate::An individual risk estimate depends on the relevant person, outcome, period, and clinical information, not a generic online chart alone.]] needs your full history. We will review that together before discussing what the result means for you.
Avery | I also want to understand what matters most to me in choosing among appropriate options.
Dr Patel | That belongs in a [[shared treatment decision::A shared treatment decision combines clinical evidence with the person's informed priorities rather than ignoring either.]], with accurate information about benefits, harms, and practical demands.
Avery | I understand this explanation does not mean I should stop a medicine because I feel better.
Dr Patel | Exactly. Any change requires the appropriate [[anticoagulation review::An anticoagulation review reassesses the actual treatment and risks; the language exercise supplies no authorization to change a medicine.]] and an individualized plan from your treating team.''',
    rehearsal=['Read the corrected atrial-fibrillation discussion. Contrast symptom control with stroke prevention.', 'Swap roles. Repeat the bleeding-history question and the explicit boundary against inferring a medicine change.'],
    transfer_title='Clarify which medicine is meant', transfer_setup='Nico says blood thinner but cannot recall the product. The clinician will verify its name and purpose before discussing a change. No stop instruction has been given.',
    transfer='''Nico: "I do not recall the product ___." | name | The medicine's identity remains unresolved despite the informal label.
Clinician: "We will verify its name and ___." | purpose | Verification must establish what the actual medicine is intended to do.
Nico: "No stop instruction has been ___." | given | The case provides no instruction to discontinue the medicine.
Clinician: "A change needs individual ___." | review | An individual clinical review is required before deciding on a change.'''))

BOOK['units'].append(unit(
    title='Discussing coronary angiography consent', scene='A diagnostic test is not automatic treatment',
    skill='Explain a proposed procedure and clarify what has and has not been agreed.',
    brief='Dr Lewis discusses proposed diagnostic coronary angiography with Blair. Blair assumes a stent will definitely be inserted during the same visit. The exercise supplies no coronary anatomy, intervention decision, risk percentage, or preparation instructions. Dr Lewis must explain the diagnostic purpose, address questions, and clarify the actual consent arrangements for any possible intervention rather than treat attendance as agreement.',
    cast='Blair | Patient\nDr Lewis | Cardiologist',
    culture=('Explain before asking for agreement', 'A familiar procedure name may hide different expectations. Ask what the patient thinks will happen, then clarify the intended test and any separately discussed intervention.'),
    a='''What is proposed? | Diagnostic coronary angiography | A stent already selected | Surgery already completed | A guaranteed normal result | The case proposes a diagnostic investigation, not a settled intervention.
What does Blair assume? | A stent will definitely be inserted | No procedure is proposed | A result already exists | The appointment is a rehabilitation session | Blair confuses the proposed diagnostic procedure with an automatic treatment decision.
What is not supplied? | Coronary anatomy or an intervention decision | A patient question | A consent discussion | The diagnostic purpose | The clinician cannot invent anatomical findings or a final intervention plan.''',
    vocabulary='''coronary angiography | Imaging of coronary arteries using an appropriate angiographic technique. | explain coronary angiography
cardiac catheterization | Procedure using a catheter to investigate or treat cardiac conditions. | discuss cardiac catheterization
catheter laboratory | Specialist environment for catheter-based cardiac procedures. | attend the catheter laboratory
vascular access | Route of entry into a blood vessel for a procedure. | explain vascular access
radial access | Vessel access through the radial artery. | discuss radial access
femoral access | Vessel access through the femoral artery. | discuss femoral access
contrast medium | Substance used to improve visibility of structures on imaging. | explain contrast medium
coronary anatomy | Arrangement and features of the coronary arteries. | assess coronary anatomy
coronary narrowing | Reduction in the internal opening of a coronary artery. | evaluate coronary narrowing
percutaneous coronary intervention | Catheter-based procedure used to treat appropriate coronary artery disease. | discuss percutaneous coronary intervention
stent | Device placed to help maintain an opening in a vessel or structure. | explain a coronary stent
diagnostic procedure | Procedure intended to obtain information about a condition. | distinguish a diagnostic procedure
procedural risk | Possible harm associated with a procedure. | discuss procedural risk
sedation | Medicines used to reduce awareness, anxiety, or discomfort to an intended degree. | explain the sedation plan
procedure consent | Agreement to a specified procedure after appropriate discussion. | confirm procedure consent
access-site complication | Problem occurring at the vessel-entry location. | explain access-site complications
postprocedure observation | Monitoring after a procedure under the actual care plan. | explain postprocedure observation
preparation instruction | Direction needed before a procedure for the individual plan. | verify preparation instructions''',
    precision='Diagnostic angiography and coronary intervention are different actions. Possible same-session treatment must be explained within the actual plan and consent process; it is not automatic.',
    precision_extra='Do not supply fasting, medicine-holding, access-site, or sedation instructions from a language exercise. Those require the actual team\'s individualized instructions.',
    phrases='''Check expectations | What have you understood will happen during the visit?
State the diagnostic aim | The proposed test is intended to show the coronary arteries.
Separate treatment | A diagnostic test is not an automatic decision to insert a stent.
Clarify the agreement | We need to discuss exactly what you are consenting to.
Discuss risk accurately | We will explain the risks relevant to the actual procedure and your situation.
Invite alternatives | Please ask about reasonable alternatives and what they would establish.
Verify preparation | Use the instructions from the team doing your procedure.
Keep the decision open | No intervention decision is supplied by this conversation alone.''',
    notes='''Intended to show | States a diagnostic purpose rather than a guaranteed finding.
Exactly what | Requests the scope of agreement instead of relying on a vague procedure label.
Possible versus planned | A possible intervention is not the same as a settled treatment plan.''',
    d='''Which distinction is essential? | Diagnostic angiography does not automatically mean stent insertion. | Every angiogram includes a stent. | Attendance is consent to any procedure. | The anatomy is known before investigation. | The proposed diagnostic purpose and any intervention agreement must be distinguished.
Which instruction would be inappropriate to invent? | A medication-holding schedule | A request to clarify consent | A question about expectations | An explanation that anatomy is not supplied | Preparation and medicine instructions must come from the actual clinical team.
What does informed agreement require here? | A clear discussion of the specified procedure and relevant options | A signature without explanation | An assumption based on appointment attendance | A promise of zero risk | Consent concerns an understood, specified proposal and cannot be replaced by attendance alone.
Which statement preserves the facts? | No intervention decision is established in this case. | A stent is definitely needed. | Every artery is normal. | A risk percentage has been supplied. | The scenario does not provide findings or a decision authorizing intervention.''',
    dialogue='''Blair | I told my family I am coming in to have a stent. Is that the right description of the appointment?
Dr Lewis | We are discussing [[coronary angiography::Coronary angiography examines coronary arteries; it does not automatically include stent treatment.]], a diagnostic investigation. Let us clarify the difference before you make arrangements around an assumption.
Blair | I thought the test and the treatment were simply two names for what always happens together.
Dr Lewis | A [[diagnostic procedure::A diagnostic procedure obtains information and must be distinguished from a separate treatment action or decision.]] gathers information. Treatment may be discussed in relation to findings, but it is not automatic.
Blair | Then the purpose is to understand the arteries, rather than promise that a particular device will be inserted?
Dr Lewis | Yes. It helps assess [[coronary anatomy::Coronary anatomy describes the arteries; this case supplies no anatomical findings.]]. We need to explain how any findings would affect the options before you agree to proceed.
Blair | Please explain the phrase PCI if it comes up. I hear abbreviations and lose track of which action is meant.
Dr Lewis | [[Percutaneous coronary intervention::Percutaneous coronary intervention is catheter-based treatment, distinct from diagnostic imaging alone.]] is a catheter-based treatment approach. We should explain the actual proposal rather than hide it behind initials.
Blair | What would the consent discussion need to cover if treatment during the same visit were a possibility?
Dr Lewis | The [[procedure consent::Procedure consent concerns the specified actions agreed after discussion, including any possible intervention in the actual plan.]] must be clear about the proposed actions, alternatives, relevant risks, and your questions.
Blair | I do not want signing for a test to be treated as agreement to something nobody has explained.
Dr Lewis | That is why we clarify scope. A [[stent::A stent is a device used in some interventions and is not automatically inserted merely because angiography is discussed.]] is not something we should describe as already decided when it has not been.
Blair | I have read different stories about the wrist and groin. Should I choose from those accounts myself?
Dr Lewis | The team will discuss the actual [[vascular access::Vascular access identifies the actual vessel-entry route, not a plan borrowed from another patient.]] plan and its implications with you. Do not infer your plan from another person's experience.
Blair | I also want to ask about the dye and any concerns in my own medical history.
Dr Lewis | We should review those concerns when explaining the [[contrast medium::Contrast medium improves imaging visibility and its relevant risks and preparation need individual clinical review.]] and the procedure's risks in your individual circumstances.
Blair | Should I follow preparation advice I found online while I wait for the written instructions?
Dr Lewis | Follow the team's [[preparation instructions::Preparation instructions must match the real procedure and medicines; the language exercise does not supply a safe substitute.]]. If another source gives different fasting or medicine advice, please contact us to clarify it before making a change.
Blair | I can explain the visit more accurately now: a diagnostic discussion, with any intervention requiring clarity.
Dr Lewis | Good. We will also explain [[postprocedure observation::Postprocedure observation means planned monitoring; it does not establish a guaranteed discharge time.]] and practical arrangements, without promising an outcome or discharge time we have not established.''',
    rehearsal=['Read the corrected procedure discussion. Contrast diagnostic information with an intervention decision.', 'Swap roles. Repeat the consent-scope question and the instruction to use the actual team\'s preparation advice.'],
    transfer_title='A preparation sheet needs clarification', transfer_setup='Morgan receives two different preparation sheets. The procedural team will verify which applies. Morgan has not been told to alter medicines in this scenario.',
    transfer='''Morgan: "The two sheets give different ___." | instructions | The problem is conflicting preparation information rather than a completed clinical decision.
Clinician: "The procedural team will ___ which applies." | verify | Verification by the responsible team is the supplied next step.
Morgan: "No medicine change is ___ here." | authorized | The scenario supplies no authorization to alter a medicine.
Clinician: "The correct plan is not yet ___." | clarified | Conflicting documents leave the relevant instruction unresolved until verification.'''))

BOOK['units'].append(unit(
    title='Checking a heart-failure home plan', scene='Teach-back checks the explanation',
    skill='Check understanding of an individualized plan without treating a printed sheet as proof of comprehension.',
    brief='Dr Evans reviews an individualized heart-failure plan with Lee. The actual plan includes symptom monitoring, a verified medicine list, contact routes, and follow-up. No weight threshold, fluid limit, or dose adjustment is supplied here. Lee has received the sheet but is unclear which number is for routine questions and which route is for urgent concerns. The clinician must clarify the distinction and use teach-back without blame.',
    cast='Dr Evans | Cardiologist\nLee | Patient',
    culture=('Ask the patient to explain the plan, not perform obedience', 'Teach-back evaluates the clarity of the explanation. A misunderstanding is an opportunity to explain differently, not evidence of poor intelligence or unwillingness.'),
    a='''What has Lee received? | A written individualized plan | A supplied dose-adjustment rule | A universal fluid limit | A completed follow-up visit | The sheet exists, but this exercise supplies no clinical thresholds or dosing rules.
What is unclear? | Routine versus urgent contact routes | Whether Lee has a plan | Whether Dr Evans is reviewing it | Whether follow-up exists | Lee needs the two communication routes distinguished explicitly.
What does teach-back check? | The clarity of the explanation received | The patient's moral character | Whether questions should be prohibited | A diagnosis without assessment | Teach-back reveals how the explanation was understood and supports clarification.''',
    vocabulary='''heart failure | Clinical syndrome in which cardiac dysfunction causes symptoms and signs in context. | explain heart failure
congestion | Fluid accumulation associated with relevant circulatory dysfunction. | assess congestion
edema | Swelling caused by fluid in tissues. | describe peripheral edema
orthopnea | Breathlessness occurring when lying flat. | ask about orthopnea
paroxysmal nocturnal dyspnea | Episodes of breathlessness waking a person from sleep. | clarify nocturnal dyspnea
exercise tolerance | Ability to perform physical activity without limiting symptoms. | describe exercise tolerance
daily weight record | Log of body-weight measurements under an agreed monitoring plan. | review a daily weight record
fluid balance | Relationship between fluid intake, output, and retention. | assess fluid balance
fluid restriction | Individual instruction limiting fluid intake when clinically indicated. | clarify a prescribed fluid restriction
sodium intake | Amount of sodium consumed through food and drink. | discuss sodium intake
diuretic | Medicine increasing urine production. | explain a prescribed diuretic
guideline-directed therapy | Treatment consistent with applicable evidence-based recommendations and individual circumstances. | review guideline-directed therapy
decompensation | Worsening of a condition beyond its compensated state. | assess suspected decompensation
action plan | Individualized instructions about monitoring and responding to changes. | review the action plan
contact pathway | Defined route for reaching the appropriate care service. | distinguish contact pathways
self-monitoring | Person's observation or recording of agreed health information. | explain self-monitoring
follow-up interval | Planned time between reviews in the individual's care. | confirm the follow-up interval
care-plan discrepancy | Difference between versions or understandings of the intended care plan. | resolve a care-plan discrepancy''',
    precision='A written action plan does not prove understanding. Clarify the actual instructions; the lesson must not become a universal weight, fluid, or medicine-adjustment protocol.',
    precision_extra='Routine messaging and urgent care are different routes. Their actual use must be explained for the patient\'s setting rather than inferred from a worksheet.',
    phrases='''Check the explanation | I want to check that I explained the two routes clearly.
Invite teach-back | Using your plan, tell me which route you would use for each listed situation.
Remove blame | That tells me I need to explain the distinction differently.
Keep it individual | The thresholds and instructions must be the ones agreed for you.
Separate routes | A routine message is not the same as urgent clinical contact.
Verify the list | Let us confirm which medicine list is current.
Resolve a mismatch | These two versions need checking before you rely on them.
Close with clarity | Please show me where the next review and contact details are recorded.''',
    notes='''I explained | Places responsibility for clear communication on the explanation rather than blaming the listener.
Using your plan | Supports teach-back with the actual written information rather than testing unsupported memory.
The ones agreed for you | Prevents individualized thresholds from being treated as universal instructions.''',
    d='''Which teach-back request is best? | Using your plan, explain which contact route applies to each listed situation. | You understand everything, yes? | Prove you memorized the whole sheet. | Stop asking because it is printed. | Explaining the appropriate contacts reveals understanding of the plan instead of merely obtaining a yes-or-no answer.
Which response avoids blame? | I need to explain that distinction differently. | You are bad at following instructions. | The sheet cannot be unclear. | Your question proves you do not care. | Teach-back should prompt clearer explanation rather than criticism of the patient.
What must not be invented? | A universal dose-adjustment threshold | A request to verify the plan | A distinction between contact routes | A next review question | The exercise supplies no numerical or medicine-change instructions to generalize.
What does receipt of the sheet establish? | That Lee has the sheet, not that every instruction is understood | Complete comprehension | Completed follow-up | An unchanged condition forever | Possession of a document is different from understanding or completion of care.''',
    dialogue='''Dr Evans | You have the written plan. Before you leave, let us check how clearly I explained its different parts.
Lee | I have read the [[action plan::An action plan provides individualized monitoring and response instructions, but receiving it does not prove complete understanding.]], but the contact numbers still confuse me.
Dr Evans | Thank you for saying so. Tell me which part is unclear, and we can work through that distinction.
Lee | I cannot tell which [[contact pathway::A contact pathway identifies the appropriate route to a service; routine questions and urgent concerns use different actual arrangements.]] is for ordinary questions and which is for something requiring urgent help.
Dr Evans | We need to make that explicit using your actual instructions. A routine message is not the urgent-care route.
Lee | I also want to understand what I am observing, not just copy numbers into a [[daily weight record::A daily weight record is an agreed monitoring log and does not itself supply a universal threshold for action.]].
Dr Evans | We will explain the monitoring purpose and the instructions agreed for you. This discussion does not supply a universal threshold.
Lee | Good. I have seen different advice about a [[fluid restriction::A fluid restriction is an individual clinical instruction when indicated, not a rule that can be borrowed from another person's plan.]], and I did not know whether it applied to everyone.
Dr Evans | It does not automatically apply in the same way to everyone. Use the individualized instructions from your treating team.
Lee | The medicine sheet also needs checking. I do not want to assume an old [[diuretic::A diuretic is a medicine that increases urine production; its actual instructions need verification rather than guesswork.]] instruction remains current.
Dr Evans | Exactly. We will verify the current list rather than let two different versions sit beside each other unexplained.
Lee | That sounds like a [[care-plan discrepancy::A care-plan discrepancy is a difference between versions or understandings that requires verification before reliance.]] we should resolve before I use the sheet at home.
Dr Evans | Yes. Now, using the corrected plan, explain how you would choose the contact route for each situation it lists.
Lee | I can use the written information for that [[self-monitoring::Self-monitoring means observing or recording agreed information and should be linked to the actual individualized response plan.]] plan rather than guessing which changes matter.
Dr Evans | Correct. This [[teach-back::Teach-back checks how clearly the explanation was understood and should prompt clarification rather than blame.]] checks my explanation. A misunderstanding tells me to explain differently, not to blame you.
Lee | I appreciate that. Some symptoms, such as breathlessness when lying flat, are hard to describe with the usual shorthand.
Dr Evans | We can use plain words. [[Orthopnea::Orthopnea is breathlessness when lying flat; explaining the term does not replace assessment of the person's actual symptoms.]] is the clinical term for that symptom, but your own description remains important.
Lee | I also need to know when the next review is and who answers questions before it.
Dr Evans | We will confirm the [[follow-up interval::The follow-up interval is the individually planned time between reviews and must not be guessed from a generic worksheet.]] and the relevant contact details in the actual plan.
Lee | Then I can describe the monitoring, medicines, and contact routes separately instead of treating the page as one long instruction.''',
    rehearsal=['Read the corrected plan review. Give a clear pause between routine questions and urgent concerns.', 'Swap roles. Repeat the teach-back request and the non-blaming clarification without adding clinical thresholds.'],
    transfer_title='Two versions of a plan', transfer_setup='Kai has an old medicine list and a newly printed plan. Their instructions differ. Nurse Jo will obtain clinician verification. No adjustment is authorized by this exercise.',
    transfer='''Kai: "The instructions on the two versions ___." | differ | The discrepancy concerns conflicting instructions rather than a confirmed current plan.
Jo: "We need clinician ___." | verification | The responsible clinical review must establish which instructions apply.
Kai: "This exercise authorizes no medicine ___." | adjustment | No medicine change may be inferred from the language-practice scenario.
Jo: "The current plan remains to be ___." | clarified | The supplied next step is resolving the discrepancy before relying on a version.'''))

BOOK['units'].append(unit(
    title='Explaining absolute and relative risk', scene='Twenty-five percent of what?',
    skill='Translate a relative change into comparable absolute frequencies without turning group data into a personal guarantee.',
    brief='For arithmetic practice only, a fictional comparison describes 40 events among 1,000 people without an intervention and 30 among 1,000 with it over the same five-year period. These are not real treatment estimates or a recommendation. Dr Ali explains the ten-event difference, the one-percentage-point absolute reduction, and the 25 percent relative reduction to Robin. No individual risk estimate is supplied.',
    cast='Robin | Patient in a fictional numerical exercise\nDr Ali | Cardiologist',
    culture=('Keep the denominator visible', 'A large relative percentage can be heard as a large personal probability change. Use the same group size and time period when comparing figures, then explain the limits of individual prediction.'),
    a='''How many events occur in the fictional comparison group? | 40 per 1,000 | 30 per 100 | 25 per 100 | 10 per 10 | The supplied comparison group has forty events among one thousand people over five years.
How many events occur in the intervention group? | 30 per 1,000 | 40 per 100 | 1 per 1,000 | 25 per 1,000 | The intervention group has thirty events among the same denominator of one thousand.
What is the common time period? | Five years | One day | Ten years | An unspecified lifetime | Both fictional figures refer to the same five-year period for a valid comparison.''',
    vocabulary='''absolute risk | Probability of a defined outcome over a stated time in a specified group. | communicate absolute risk
relative risk | Ratio of risk in one group to risk in a comparison group. | calculate relative risk
absolute risk reduction | Difference between comparison and intervention risks. | explain absolute risk reduction
relative risk reduction | Absolute reduction divided by the comparison risk. | explain relative risk reduction
percentage point | Unit for the arithmetic difference between two percentages. | distinguish percentage points
denominator | Total number underlying a proportion or rate. | state the denominator
natural frequency | Count expressed out of a stated group size. | use natural frequencies
time horizon | Period over which an outcome probability is described. | specify the time horizon
comparison group | Group providing a reference for evaluating another group. | identify the comparison group
intervention group | Group receiving the approach being evaluated. | describe the intervention group
event rate | Frequency of specified events in a defined group or observation period. | compare event rates
baseline risk | Risk before or without the evaluated change in the relevant comparison. | explain baseline risk
confidence interval | Range expressing statistical uncertainty around an estimate under its assumptions. | interpret a confidence interval
number needed to treat | Reciprocal of absolute risk reduction for a defined outcome and period. | qualify number needed to treat
population estimate | Estimate describing a defined group rather than a guaranteed individual outcome. | interpret a population estimate
risk communication | Explanation of probabilities, uncertainty, and possible consequences. | improve risk communication
benefit framing | Way of presenting a possible favorable outcome or reduction in harm. | balance benefit framing
uncertainty range | Range communicating limits of an estimate's precision or applicability. | explain the uncertainty range''',
    precision='Forty per 1,000 is 4 percent; thirty per 1,000 is 3 percent. The difference is one percentage point, equivalent to a 25 percent relative reduction from 4 percent.',
    precision_extra='The figures are invented for language and arithmetic practice. They are not a treatment effect, a personal risk prediction, or evidence for choosing an intervention. Do not invent a confidence interval.',
    phrases='''State the denominator | Both figures are out of one thousand people.
Keep time consistent | Both cover the same five-year period.
Use natural frequencies | The comparison is forty events versus thirty.
Explain the difference | That is ten fewer events per thousand.
Name the absolute change | The absolute reduction is one percentage point.
Name the relative change | Ten is one quarter of forty, so the relative reduction is twenty-five percent.
Limit the meaning | These fictional group figures do not predict your individual outcome.
Keep uncertainty honest | No confidence interval has been supplied.''',
    notes='''Percent versus percentage point | A change from four percent to three percent is one percentage point, not twenty-five percentage points.
Out of | Introduces the denominator in an accessible natural-frequency comparison.
Over five years | Keeps the same observation period attached to both figures.''',
    d='''What is the absolute difference? | 10 fewer events per 1,000 | 250 fewer events per 1,000 | 25 percentage points | 40 fewer events per 100 | Subtracting thirty from forty gives ten fewer events among one thousand people.
What is the absolute percentage-point reduction? | One percentage point | Twenty-five percentage points | Ten percentage points | Seventy-five percentage points | Four percent minus three percent equals one percentage point.
What is the relative reduction? | 25 percent | 1 percent | 75 percent | 10 percent | The reduction of ten divided by the comparison count of forty is one quarter, or twenty-five percent.
Which conclusion must be avoided? | These figures guarantee Robin's personal outcome. | The denominators match. | The time periods match. | The figures are fictional. | Fictional group data cannot establish a personal risk or guarantee an individual result.''',
    dialogue='''Robin | A twenty-five percent reduction sounds large. Does it mean twenty-five fewer people out of every hundred?
Dr Ali | Not in this example. We need the [[denominator::The denominator is the group size underlying each figure; both fictional groups contain one thousand people.]] and the original risk before interpreting a relative percentage.
Robin | Please use the counts first. I follow those more easily than a headline percentage on its own.
Dr Ali | The [[natural frequencies::Natural frequencies express the counts out of a common group size, here forty versus thirty events per thousand.]] are forty events per thousand without the intervention and thirty per thousand with it.
Robin | Are those counted over the same period, or is one an annual number and the other a lifetime number?
Dr Ali | The [[time horizon::The time horizon is the period over which the event figures apply; both use the same five years.]] is five years for both. We must keep that period attached to the comparison.
Robin | Then the difference is ten events per thousand, rather than two hundred and fifty per thousand.
Dr Ali | Correct. The [[absolute risk reduction::Absolute risk reduction is the difference between the two group risks, here ten per thousand or one percentage point.]] is ten per thousand, which is one percentage point.
Robin | I want to get the wording right: four percent compared with three percent is one percentage point apart.
Dr Ali | Exactly. A [[percentage point::A percentage point measures the difference between percentage values; four percent minus three percent equals one point.]] is the unit for subtracting percentages, not the same as a relative percent change.
Robin | Where does twenty-five percent come from if the absolute difference is only one percentage point?
Dr Ali | The [[relative risk reduction::Relative risk reduction compares the decrease with the original comparison risk; ten divided by forty equals twenty-five percent.]] is ten divided by forty. The reduction is one quarter of the comparison count.
Robin | So the relative risk itself is thirty divided by forty, or three quarters of the comparison risk?
Dr Ali | Yes. [[Relative risk::Relative risk is the intervention risk divided by the comparison risk, here thirty over forty or 0.75.]] is 0.75 in this fictional example; the relative reduction is 0.25, or twenty-five percent.
Robin | Could someone use only the larger-sounding relative reduction to make the option appear more impressive?
Dr Ali | That is why [[benefit framing::Benefit framing is how a favorable effect is presented; balanced explanation includes absolute as well as relative figures.]] matters. Presenting the absolute figures too helps keep the size of the comparison clear.
Robin | I also understand that these made-up numbers cannot tell me what will happen to me personally.
Dr Ali | Correct. A [[population estimate::A population estimate describes a group and does not guarantee the outcome for an individual person.]] would still need careful interpretation. These made-up figures only illustrate the arithmetic; they are not a prediction for you.
Robin | And we should not add a precision range unless the source actually supplies one and explains it.
Dr Ali | Exactly. No [[confidence interval::A confidence interval expresses statistical uncertainty under defined assumptions and cannot be invented when no interval is supplied.]] is supplied here. We should keep that limitation explicit rather than manufacture certainty.''',
    rehearsal=['Read the corrected numerical explanation. Stress per thousand, over five years, and percentage point.', 'Swap roles. Say the absolute and relative differences using only the fictional figures supplied.'],
    transfer_title='A second fictional comparison', transfer_setup='For arithmetic practice only, fictional five-year event counts are 20 per 1,000 in one group and 15 per 1,000 in another. No treatment recommendation is implied.',
    transfer='''Clinician: "The absolute difference is ___ per thousand." | five | Twenty minus fifteen gives five events per thousand in this fictional comparison.
Patient: "That is ___ percentage points." | 0.5 | Five divided by one thousand is half of one percent, or 0.5 percentage points.
Clinician: "The relative reduction is ___ percent." | twenty-five | Five divided by the comparison count of twenty equals twenty-five percent.
Patient: "These numbers remain ___." | fictional | The figures are invented for practice and do not support a clinical recommendation.'''))

BOOK['units'].append(unit(
    title='Coordinating rehabilitation and return to activity', scene='Referred is not yet enrolled',
    skill='Explain a rehabilitation referral and negotiate practical follow-up without giving an unsupplied exercise prescription.',
    brief='Dr Reed has referred Sam to cardiac rehabilitation after an assessed cardiac event. The rehabilitation team has received the referral, but no intake appointment is confirmed. Sam wants to return to a physically demanding job and has a transport barrier. Exercise clearance, work restrictions, and an individual program require the actual clinical assessment; none is supplied in this exercise. Coordinator Inez will help clarify access arrangements.',
    cast='Sam | Patient\nDr Reed | Cardiologist',
    culture=('Practical barriers are part of the clinical conversation', 'Attendance can be difficult even when the patient wants support. Ask about transport and work demands before labeling missed access as a lack of motivation.'),
    a='''What is confirmed? | Receipt of the rehabilitation referral | A completed intake | Full work clearance | A prescribed exercise intensity | The receiving team has the referral, but later assessment and booking stages remain unresolved.
What barrier does Sam report? | Transport | A refusal of all rehabilitation | A completed exercise test | A supplied work restriction | Transport is the stated practical obstacle, not a lack of interest.
What requires individual assessment? | Exercise and work guidance | Whether a referral was sent | Inez's name | Sam's expressed wish | The exercise supplies no clearance or program from which to give activity instructions.''',
    vocabulary='''cardiac rehabilitation | Supervised program supporting recovery, risk reduction, and functioning after eligible cardiac conditions. | explain cardiac rehabilitation
rehabilitation intake | Initial assessment and planning encounter for a rehabilitation program. | arrange rehabilitation intake
exercise prescription | Individualized specification of appropriate exercise under clinical assessment. | review an exercise prescription
functional capacity | Ability to perform physical tasks under relevant conditions. | assess functional capacity
graded activity | Activity progressed in steps under an appropriate plan. | discuss graded activity
supervised exercise | Exercise performed with the relevant professional oversight. | arrange supervised exercise
return-to-work assessment | Evaluation of readiness and requirements for resuming work. | request a return-to-work assessment
work restriction | Specified limitation on work activity under an appropriate assessment. | clarify work restrictions
occupational demand | Physical or other requirement of a person's job. | describe occupational demands
secondary prevention | Measures reducing recurrence or complications after established disease. | discuss secondary prevention
risk-factor modification | Changes directed at relevant disease risk factors. | support risk-factor modification
rehabilitation goal | Individual objective for recovery or functioning. | set a rehabilitation goal
attendance barrier | Obstacle to taking part in scheduled care. | identify an attendance barrier
transport arrangement | Plan for travel to and from a service. | confirm transport arrangements
program eligibility | Whether a person meets requirements for a particular service. | verify program eligibility
coverage verification | Checking the applicable financial or insurance arrangements. | obtain coverage verification
intake confirmation | Verification that an initial program appointment is booked. | obtain intake confirmation
care coordinator | Professional organizing connected services and practical arrangements. | contact the care coordinator''',
    precision='A rehabilitation referral is not an exercise prescription or work-clearance certificate. Keep acceptance, intake, assessment, and participation distinct.',
    precision_extra='Do not promise coverage, transport, or a place in a program before verification. Help identify the responsible person and the unresolved practical questions.',
    phrases='''Explain the service | Rehabilitation combines assessed activity, education, and support.
State the stage | The team has received the referral; intake is not yet confirmed.
Ask about access | What would make getting to the sessions difficult?
Describe the job | Tell us what the work requires physically.
Avoid clearance by implication | This referral is not a statement that every work task is safe for you.
Name the coordinator | Inez can help clarify the access arrangements.
Separate coverage | We need to verify the applicable coverage rather than promise it.
Confirm the next step | Let us identify who will confirm the intake and contact you.''',
    notes='''Received versus confirmed | Receipt concerns the referral; confirmed intake concerns a booked appointment.
Requires physically | Elicits actual job demands instead of relying on a job title alone.
Can help clarify | Offers coordination without guaranteeing a service or financial outcome.''',
    d='''Which statement preserves the referral stage? | Received, but intake not yet confirmed. | Sam is already enrolled. | Full work clearance has been issued. | The exercise program is finalized. | The brief confirms receipt only and leaves intake and individual assessment unfinished.
Which question addresses access respectfully? | What makes travel to the sessions difficult? | Why are you unmotivated? | Can we ignore transport? | Why do you refuse all care? | Asking what makes travel difficult explores the stated barrier without inventing a negative attitude.
What must not be inferred from the referral? | A safe exercise intensity or unrestricted work clearance | A need to clarify intake | A transport question | A coordinator's role | Actual exercise and work guidance requires the appropriate individual clinical assessment.
Which promise is unsupported? | Every cost and journey will definitely be covered. | Inez can help clarify arrangements. | Intake is not confirmed. | Coverage needs verification. | The case supplies no verified financial or transport entitlement to guarantee.''',
    dialogue='''Sam | I want to return to work, but the job involves lifting and long periods on my feet.
Dr Reed | Those [[occupational demands::Occupational demands are the actual job tasks relevant to the work assessment.]] need to be described for the assessment rather than inferred from your job title.
Sam | Does the rehabilitation referral mean I have already been cleared to do every part of the job?
Dr Reed | No. A [[return-to-work assessment::A return-to-work assessment evaluates actual readiness; rehabilitation attendance alone does not establish it.]] is a separate clinical question. The referral is not unrestricted clearance.
Sam | Then what is rehabilitation intended to add beyond another appointment about the event itself?
Dr Reed | [[Cardiac rehabilitation::Cardiac rehabilitation is supervised care, not automatic authorization for unrestricted activity.]] can combine assessed activity, education, and support, with a program suited to the relevant clinical circumstances.
Sam | I received a letter saying the referral arrived. I assumed that meant I had a first session booked.
Dr Reed | The team has received it, but [[intake confirmation::Intake confirmation establishes the receiving program's actual appointment, not merely referral receipt.]] has not yet been provided. We need to make that next step clear.
Sam | Getting there may be difficult. I do not have a reliable lift during the hours the service usually operates.
Dr Reed | That [[attendance barrier::An attendance barrier is a practical obstacle, not necessarily refusal of rehabilitation.]] matters. Inez can help clarify transport and access arrangements rather than assume you do not want to attend.
Sam | I also need to know whether the sessions are covered before I commit to costs I cannot manage.
Dr Reed | We need [[coverage verification::Coverage verification checks the actual financial arrangements and prevents an unsupported promise that every cost is covered.]]. I cannot promise a financial outcome without checking the applicable arrangements.
Sam | A friend suggested copying their exercise schedule while I wait. Is that the same as the program I will receive?
Dr Reed | No. An [[exercise prescription::An exercise prescription specifies activity for an individual after appropriate assessment and should not be copied from another person's program.]] needs your own assessment. Ask the rehabilitation team what is appropriate for you rather than copying your friend's schedule.
Sam | I would like the program to help me with the tasks that actually matter at home and work.
Dr Reed | That is a useful [[rehabilitation goal::A rehabilitation goal is an individualized recovery or functioning objective that connects the program with the person's needs.]] to discuss with the team as they assess your circumstances.
Sam | I understand that progress may involve different steps rather than an immediate return to everything.
Dr Reed | Yes. Any [[graded activity::Graded activity progresses in planned steps under an appropriate individual plan rather than an unsupplied universal schedule.]] must follow the agreed clinical plan, with the relevant review and support.
Sam | For now I need the intake date, transport information, and a clear route for my work questions.
Dr Reed | We will identify the [[care coordinator::A care coordinator connects services and practical arrangements while clinical decisions remain with the appropriately responsible professionals.]] and responsible clinicians for those questions, without treating the referral as a completed assessment.''',
    rehearsal=['Read the corrected rehabilitation discussion. Contrast referral receipt, intake, and work assessment.', 'Swap roles. Repeat the transport-barrier question without implying poor motivation or promising coverage.'],
    transfer_title='A job title hides the task', transfer_setup='Rory works in a warehouse and asks about returning to lifting. The clinical team requests the actual task demands before assessing restrictions. No lifting limit is supplied.',
    transfer='''Rory: "My job includes ___." | lifting | Lifting is the actual work activity raised in the scenario.
Clinician: "We need the task ___ before assessing restrictions." | demands | A job title alone does not specify the relevant physical requirements.
Rory: "No lifting limit has been ___." | supplied | The exercise provides no numerical or clinical restriction to infer.
Clinician: "The work guidance needs individual ___." | assessment | The appropriate clinical assessment must precede individualized work guidance.'''))
