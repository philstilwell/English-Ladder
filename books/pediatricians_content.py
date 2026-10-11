"""Original pediatric English for child, caregiver, and team communication."""
from books.medical_support import medical_unit as unit, source, SCOPE

BOOK = dict(slug='pediatricians', title='Pediatrics English', cover_label='ENGLISH FOR PEDIATRICIANS',
    cover_title='Pediatrics', cover_size=42, tagline='Hear the child. Include the caregiver. Explain the plan.',
    audience='For pediatricians, pediatric trainees, and physicians coordinating care for children and adolescents.',
    roles='pediatricians, pediatric residents, community pediatricians, adolescent-health physicians',
    summary='Pediatric English for child and caregiver histories, growth, developmental screening, vaccine questions, medicine instructions, adolescent privacy, school plans, and urgent handoffs.',
    map_intro='Eight pediatric encounters practice multiple perspectives, chart explanations, screening uncertainty, respectful disagreement, precise units, confidentiality, school coordination, and time-critical updates.',
    notes_title='One visit can have more than one voice.',
    notes_intro='Pediatric conversations often include a child, caregivers, schools, and several clinicians. Attribute each account, speak directly to the child when appropriate, and make the next step understandable to the people who will carry it out.',
    field_notes=[
        ('Hear the child as well as the caregiver', 'Accounts may differ without either person being dishonest. Ask about setting, timing, and meaning, and preserve who supplied each detail.', '"You notice it at school; your caregiver notices it after dinner. Let us keep both accounts."'),
        ('Translate without turning a chart into a grade', 'Explain what a measurement or screening result represents. Avoid calling a child a failure, a percentile a target, or a screening concern a confirmed diagnosis.', '"The result tells us what needs further assessment, not everything about your child."'),
        ('Verify medicine language', 'Distinguish amount of drug, liquid volume, concentration, and the measuring device. Use the actual verified instructions; this book does not supply doses.', '"Milligrams and milliliters describe different things. We need the actual label and instructions."'),
        ('Explain privacy before promising it', 'Confidentiality, access to records, caregiver authority, and safety duties vary by setting and jurisdiction. Explain the actual limits and communication channels.', '"Let us discuss what is private, who can access the record, and the relevant safety exceptions."'),
    ], scope_note=SCOPE,
    sources=[
        source('AAP HealthyChildren. Understanding Growth Charts.', 'https://www.healthychildren.org/English/health-issues/conditions/Glands-Growth-Disorders/Pages/growth-charts-by-the-numbers.aspx', 'Context for explaining measurements and patterns without treating percentiles as grades.'),
        source('AAP HealthyChildren. Assessing Developmental Delays.', 'https://www.healthychildren.org/English/ages-stages/toddler/Pages/Assessing-Developmental-Delays.aspx', 'Background for distinguishing screening concerns from a diagnostic assessment.'),
        source('AAP HealthyChildren. How to Use Liquid Medicines for Children.', 'https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Using-Liquid-Medicines.aspx', 'Supports precise liquid-measurement language and appropriate measuring tools; no doses are supplied here.'),
        source('AAP HealthyChildren. Information for Teens: Privacy.', 'https://www.healthychildren.org/English/ages-stages/teen/Pages/Information-for-Teens-What-You-Need-to-Know-About-Privacy.aspx', 'Context for adolescent privacy conversations; actual legal and record-access rules must be checked locally.')], units=[])

BOOK['units'].append(unit(
    title='Hearing the child and caregiver', scene='Two accounts of the same week',
    skill='Reconcile different symptom accounts without deciding that one speaker is unreliable.',
    brief='Ten-year-old Leo says stomach discomfort happens before school. His caregiver reports seeing it after dinner. Dr Park asks Leo for his account first, then clarifies each setting and timing. No cause, examination finding, or school-avoidance diagnosis is established. The two accounts may describe different episodes.',
    cast='Dr Park | Pediatrician\nLeo | Child patient',
    culture=('Do not turn a difference into an accusation', 'A child may describe sensations differently from an adult. Distinguish what each person experienced or observed before attempting to reconcile the accounts.'),
    a='''When does Leo report discomfort? | Before school | Only after dinner | Only during examination | Never | Leo describes discomfort before school in the supplied brief.
What does the caregiver observe? | Discomfort after dinner | A proven cause | Every episode at school | A completed diagnosis | The caregiver reports seeing episodes after dinner, not every possible episode.
What is not established? | The cause | Two accounts | Leo's report | A need to clarify timing | The case does not supply a cause, examination finding, or diagnosis.''',
    vocabulary='''presenting concern | Main issue bringing the child or family to the consultation. | clarify the presenting concern
caregiver account | Information supplied by a person caring for the child. | attribute the caregiver account
child account | Information described directly by the child. | invite the child account
symptom onset | Time when a symptom first began. | clarify symptom onset
episode duration | Length of an individual occurrence. | establish episode duration
symptom frequency | How often a symptom occurs. | describe symptom frequency
associated symptom | Additional symptom occurring with the main concern. | ask about associated symptoms
functional impact | Effect on everyday activities and participation. | assess functional impact
school attendance | Pattern of being present at school. | clarify school attendance
sleep pattern | Usual timing and quality of sleep. | describe the sleep pattern
appetite change | Difference from the person's usual desire to eat. | report an appetite change
baseline behavior | Usual behavior used for comparison. | establish baseline behavior
direct observation | Information personally witnessed by the speaker. | distinguish direct observation
recalled event | Event described from memory rather than current observation. | clarify a recalled event
contextual difference | Difference in circumstances surrounding two accounts. | explore contextual differences
developmental language | Wording adapted to the child's communication development. | use developmental language
rapport | Working relationship supporting comfortable and accurate communication. | build rapport
summary check | Confirmation that a summary reflects the speaker's account. | perform a summary check''',
    precision='Before school and after dinner may describe different episodes. Neither phrase proves a cause or a motive.',
    precision_extra='Do not diagnose anxiety, deception, or school avoidance from the timing alone. Preserve the child and caregiver accounts as separate sources.',
    phrases='''Invite the child | Leo, tell me what happens in your own words.
Clarify timing | Is that when it starts or when someone notices it?
Separate episodes | Those may be two different episodes.
Ask about impact | What becomes difficult when it happens?
Avoid accusation | The accounts differ; that does not tell us why.
Keep attribution | Your caregiver notices it after dinner.
Check meaning | What does that word mean when you use it?
Summarize | Tell me which part of my summary needs correcting.''',
    notes='''Reports versus observes | Reports attributes an account; observes specifies something personally witnessed.
Starts versus is noticed | Separates onset from the time another person becomes aware of a symptom.
May describe | Keeps an explanation possible without asserting that it is established.''',
    d='''Which summary preserves the sources? | Leo reports morning episodes; his caregiver notices evening episodes. | Leo must be mistaken. | The caregiver knows every episode. | The timing proves school avoidance. | The summary keeps both accounts visible without assigning cause or credibility.
Which question clarifies duration? | How long does one episode last? | What color is the waiting room? | Who is definitely wrong? | Why are you avoiding school? | Duration concerns the length of one occurrence rather than its frequency or assumed cause.
Which conclusion exceeds the facts? | Leo has a school-avoidance diagnosis. | Leo describes discomfort. | Timing needs clarification. | Two accounts are available. | No diagnosis or motive is established by the supplied symptom timing.
What is a summary check for? | Correcting the clinician's understanding | Testing the child's intelligence | Forcing agreement | Replacing an examination | The check verifies whether the clinician has understood the account accurately.''',
    dialogue='''Dr Park | Leo, I would like to hear your account first. What happens before school when your stomach feels uncomfortable?
Leo | It feels tight while I am getting ready, but I do not know the exact word for it.
Dr Park | That description helps. Your [[child account::The child account is Leo's own description and should be heard directly rather than replaced by an adult's interpretation.]] does not need a medical label before I can listen carefully.
Leo | My caregiver said it happens after dinner. I thought that made my answer sound wrong.
Dr Park | The [[caregiver account::The caregiver account records what the caregiver reports and may concern different episodes or settings from the child's description.]] may describe a different episode. We should clarify both rather than choose a winner.
Leo | Sometimes I do notice it after dinner too, but that was not the time I was thinking about.
Dr Park | Let us separate [[symptom frequency::Symptom frequency means how often the discomfort occurs and differs from the length of any one episode.]] from how long each episode lasts. How often is different from how long.
Leo | I understand. I can remember some mornings, but I have not counted every time it happened.
Dr Park | Then we will preserve that uncertainty. A [[recalled event::A recalled event is described from memory and should not be presented as a complete contemporaneous record.]] is not a complete record of every episode.
Leo | It is difficult to explain because sometimes I carry on doing things even when I notice it.
Dr Park | That is useful when discussing [[functional impact::Functional impact concerns how the symptom affects everyday activities rather than assuming its effect from the label alone.]]. Tell me what becomes harder rather than guessing what I expect.
Leo | I worry that mentioning school will make everyone think I am trying not to go.
Dr Park | The timing alone does not establish that. A [[contextual difference::A contextual difference concerns the circumstances of separate accounts and does not automatically reveal a motive or diagnosis.]] needs exploration, not an accusation about your intentions.
Leo | Could you ask what I mean when I use a word instead of changing it straight away?
Dr Park | Yes. Using suitable [[developmental language::Developmental language adapts the discussion to the child's understanding while preserving the meaning of the child's account.]] means checking your meaning, not replacing it with something you did not say.
Leo | My caregiver sees me holding my stomach at dinner, but cannot see every feeling I have at school.
Dr Park | Exactly. [[Direct observation::Direct observation identifies what a speaker personally witnessed and should be distinguished from symptoms another person experiences privately.]] covers what someone witnesses, not every sensation you experience.
Leo | So you will keep the two timings separate until we understand whether they describe the same pattern?
Dr Park | Yes. We will clarify [[episode duration::Episode duration describes the length of one occurrence and must not be confused with onset or how often symptoms happen.]], timing, and other details without assigning a cause from this conversation alone.
Leo | Then a [[summary check::A summary check invites correction of the clinician's understanding rather than requiring the child to agree with an inaccurate account.]] lets me correct what you heard before it becomes the record.''',
    rehearsal=['Read the corrected conversation. Give each source its own attribution.', 'Swap roles. Contrast how often with how long without inventing a diagnosis.'],
    transfer_title='A different observer', transfer_setup='A teacher reports seeing discomfort at lunchtime. Leo has not yet discussed that episode with the clinician. The cause remains unknown.',
    transfer='''Teacher: "I noticed the discomfort at ___." | lunchtime | The teacher's observation is explicitly located at lunchtime.
Clinician: "That is the teacher's ___." | account | The information comes from the teacher rather than a completed clinical assessment.
Leo: "We have not yet ___ that episode." | discussed | The scenario leaves Leo's account of this particular episode uncollected.
Clinician: "The cause remains ___." | unknown | A new observation does not establish the cause of the discomfort.'''))

BOOK['units'].append(unit(
    title='Explaining a growth trajectory', scene='A percentile is not a school grade',
    skill='Explain a comparison measure and its limitations without labeling a child by a number.',
    brief='Caregiver Ana sees the 25th percentile on a growth chart and worries that her child has scored only 25 out of 100. Dr Bell explains that a percentile compares a particular measurement with a reference population; it is not a grade or a target. The full growth trajectory, measurement quality, and clinical context still require review. No growth disorder is diagnosed in the case.',
    cast='Ana | Caregiver\nDr Bell | Pediatrician',
    culture=('Find the mistaken comparison first', 'Before giving more numbers, ask what the existing number means to the caregiver. Correct the interpretation without treating the concern as foolish.'),
    a='''What does Ana mistake the percentile for? | A score out of 100 | A date | A medicine volume | A confirmed diagnosis | Ana interprets the percentile as a school-style score rather than a comparison.
What still needs review? | The trajectory and clinical context | Only the chart color | A predetermined target of 100 | Nothing beyond one point | The case requires the pattern, measurement quality, and context to be reviewed.
What is not diagnosed? | A growth disorder | Ana's concern | A chart entry | A misunderstanding | The brief supplies a terminology misunderstanding but no growth-disorder diagnosis.''',
    vocabulary='''growth trajectory | Pattern of growth measurements over time. | review the growth trajectory
percentile | Position of a measurement relative to a reference distribution. | explain a percentile
reference population | Group providing the comparison distribution for a measure. | identify the reference population
serial measurements | Measurements collected at different times for comparison. | review serial measurements
growth velocity | Rate of change in growth over time. | assess growth velocity
weight-for-age | Weight compared with an age-specific reference. | plot weight-for-age
length-for-age | Recumbent length compared with an age-specific reference. | review length-for-age
stature-for-age | Standing height compared with an age-specific reference. | assess stature-for-age
head circumference | Measurement around the head using the appropriate method. | record head circumference
body mass index | Weight relative to squared height, interpreted appropriately for age. | explain body mass index
measurement technique | Method used to obtain a physical measurement. | verify measurement technique
plotting error | Incorrect placement or entry of data on a chart. | check for a plotting error
centile crossing | Movement across reference percentile lines over time. | review centile crossing
growth faltering | Growth pattern raising concern about inadequate progress in context. | assess suspected growth faltering
familial pattern | Pattern related to relevant family characteristics. | consider the familial pattern
nutritional history | Account of intake and related nutrition circumstances. | obtain a nutritional history
corrected age | Age adjusted for prematurity when appropriate to the assessment. | clarify corrected age
longitudinal assessment | Evaluation using information collected across time. | conduct a longitudinal assessment''',
    precision='The 25th percentile is not 25 percent healthy, 25 percent grown, or a target to improve toward 100.',
    precision_extra='A single plotted point cannot establish the whole growth assessment. Chart selection, measurement quality, timing, and context matter.',
    phrases='''Check the interpretation | What did the number suggest to you?
Reject the grade analogy | This is not a score out of 100.
Name the comparison | It compares this measurement with a reference group.
Shift to the pattern | Let us look at the measurements over time.
Check the data | We should verify how this measurement was taken.
Avoid a target | A higher percentile is not automatically a better result.
Limit the conclusion | This point alone does not establish a growth disorder.
Explain the review | The pattern and the child's circumstances belong together.''',
    notes='''Relative to | Identifies a comparison group instead of implying an absolute health score.
Over time | Moves attention from an isolated point to a trajectory.
Not automatically | Rejects a simplistic inference without declaring every measurement unimportant.''',
    d='''Which explanation is accurate? | A percentile locates a measurement within a reference distribution. | It is the percentage of health achieved. | It is the percentage of adult size reached. | Every child should reach the 100th. | A percentile is a comparison position, not a grade, completion percentage, or universal target.
What does growth velocity describe? | Rate of growth over time | The child's running speed | A single measurement's color | The percentage of healthy organs | Growth velocity concerns change over time rather than a single plotted position.
Which check improves interpretation? | Verify measurement technique and prior points. | Ignore all earlier values. | Assume a disorder from one point. | Use a guessed age. | Reliable measurements and their sequence support the actual clinical interpretation.
Which conclusion is unsupported? | This child has a diagnosed growth disorder. | Ana misunderstands the number. | A chart entry exists. | Context requires review. | No growth-disorder diagnosis has been supplied in the case.''',
    dialogue='''Ana | The chart says 25th percentile. I thought that meant my child had scored only 25 out of 100.
Dr Bell | A [[percentile::A percentile is a reference comparison, not a grade for the child.]] is not a school grade. It tells us where a particular measurement sits in a comparison group.
Ana | So it does not mean that my child is only a quarter as healthy as expected?
Dr Bell | Correct. The [[reference population::The reference population supplies the comparison, not a universal growth target.]] provides the comparison; it does not turn a higher number into an automatic goal.
Ana | Then what do you look at when deciding whether the growth pattern needs attention?
Dr Bell | We review the [[growth trajectory::Growth trajectory describes measurements across time rather than one isolated point.]], the quality of the measurements, and the child's wider clinical circumstances.
Ana | I have earlier measurements from another clinic, but I am not sure they used the same method.
Dr Bell | Those [[serial measurements::Serial measurements need timing and comparability checks before interpreting a pattern.]] may help, provided we check their timing, method, and comparability rather than assume everything matches.
Ana | Would a mistake in entering the height make the chart look different even if nothing changed?
Dr Bell | A [[plotting error::A plotting error changes the chart entry, not necessarily the child's growth.]] can affect the display. That is one reason to verify the underlying data.
Ana | I also heard the phrase growth velocity. Is that another word for the percentile?
Dr Bell | No. [[Growth velocity::Growth velocity is the rate of change over time, whereas a percentile describes a measurement's position relative to a reference.]] describes the rate of growth over time, not the comparison position at one visit.
Ana | So two children at the same percentile today might still have different histories?
Dr Bell | Yes. A [[longitudinal assessment::A longitudinal assessment uses information across time rather than treating one shared percentile as a complete account of growth.]] considers the sequence, not merely whether two points happen to share a label.
Ana | Does that mean I should stop paying attention to the measurements altogether?
Dr Bell | Not at all. We check [[measurement technique::Measurement technique is the method used to obtain the value and affects how reliably it can be interpreted.]] and context because the measurements matter; we simply avoid treating them as grades.
Ana | What other information would help explain the pattern when you review it?
Dr Bell | Relevant history can include a [[nutritional history::A nutritional history describes intake and related circumstances and contributes to assessment without being a diagnosis by itself.]] and family information, alongside the actual examination and other clinical details.
Ana | I understand. The number alone does not tell us that a particular disorder is present.
Dr Bell | Exactly. Even [[centile crossing::Centile crossing describes movement across reference lines and requires contextual review rather than an automatic diagnosis from the chart alone.]] needs interpretation. We will explain the reviewed pattern without making a diagnosis from this single point.''',
    rehearsal=['Read the corrected chart explanation, contrasting comparison, rate, and grade.', 'Swap roles. Explain the 25th percentile without setting a numerical growth target.'],
    transfer_title='A copied height needs checking', transfer_setup='A previous height was copied incorrectly into the chart. The original measurement is being verified before the trajectory is interpreted.',
    transfer='''Caregiver: "The copied height may be ___." | incorrect | The scenario identifies a possible error in the copied height.
Clinician: "We are checking the original ___." | measurement | The original measurement is the source being verified.
Caregiver: "The trajectory is not yet ___." | interpreted | Interpretation waits for the relevant data verification in this case.
Clinician: "An entry error is not itself a growth ___." | disorder | A data-entry error does not establish a clinical growth disorder.'''))

BOOK['units'].append(unit(
    title='Discussing developmental screening', scene='A concern is a reason to assess',
    skill='Explain the difference between surveillance, screening, evaluation, and diagnosis.',
    brief='A developmental questionnaire raises a communication concern for toddler Nia. Her caregiver Ben worries that the form has already diagnosed a lifelong condition. Dr Shah explains the role and limits of screening, asks about abilities across settings and languages, and arranges the actual assessment pathway. No specific diagnosis or referral appointment date is supplied.',
    cast='Ben | Caregiver\nDr Shah | Pediatrician',
    culture=('Use concern without turning it into a label', "Acknowledge the caregiver's uncertainty. Describe the next step concretely and avoid promising either a diagnosis or that the concern will disappear."),
    a='''What raises the concern? | A developmental questionnaire | A confirmed diagnostic evaluation | An employer report | A treatment trial | The questionnaire flags a communication concern without establishing a diagnosis.
What does Ben fear? | That a lifelong diagnosis is already settled | That the form is blank | That no one read it | That an appointment is already complete | Ben interprets the screening concern as a completed diagnosis.
What is not supplied? | A specific diagnosis or appointment date | Nia's name | A communication concern | An assessment pathway | The case does not provide a diagnostic conclusion or confirmed referral appointment.''',
    vocabulary='''developmental surveillance | Ongoing attention to a child's development across encounters. | conduct developmental surveillance
developmental screening | Structured process identifying possible developmental concerns. | explain developmental screening
diagnostic evaluation | Detailed assessment intended to establish or clarify a diagnosis. | arrange a diagnostic evaluation
developmental milestone | Skill commonly emerging within a developmental period. | discuss developmental milestones
expressive language | Ability to communicate ideas using words or other expressive means. | describe expressive language
receptive language | Ability to understand communicated language. | assess receptive language
gross motor skill | Skill involving larger body movements and muscle groups. | review gross motor skills
fine motor skill | Skill involving smaller coordinated movements. | describe fine motor skills
social communication | Communication used in interaction with other people. | explore social communication
adaptive skill | Practical ability used in everyday functioning. | assess adaptive skills
caregiver questionnaire | Structured form completed by someone caring for the child. | review a caregiver questionnaire
screen-positive result | Screening result indicating that further assessment is warranted. | explain a screen-positive result
false-positive screen | Screening concern not confirmed by the relevant further assessment. | explain a possible false-positive screen
early intervention | Support addressing developmental needs early in childhood. | discuss early-intervention services
hearing assessment | Evaluation of hearing relevant to communication and other concerns. | arrange a hearing assessment
multilingual exposure | Experience with more than one language. | describe multilingual exposure
skill regression | Loss of a previously acquired ability. | report skill regression
referral status | Current stage of a referral's receipt and processing. | check referral status''',
    precision='A screen-positive result identifies a need for further assessment; it is not a diagnosis. Multilingual exposure should be described accurately, not used as an automatic explanation for every concern.',
    precision_extra='Referral sent, referral received, and appointment booked are separate states. Do not promise that an assessment has occurred because a form was completed.',
    phrases='''Name the role | This questionnaire identifies concerns that need a closer look.
Separate the conclusion | It does not establish a diagnosis by itself.
Ask across settings | What do you notice at home and in other settings?
Include languages | Tell me which languages Nia hears and uses.
Clarify a change | Is this a skill not yet acquired or one that was lost?
Explain evaluation | The assessment looks at more information than this form.
Name the next step | We will explain the referral and how to check its status.
Avoid a false promise | I cannot promise the assessment's conclusion in advance.''',
    notes='''Not yet acquired versus lost | Distinguishes delayed acquisition from regression without assigning a cause.
Flags versus confirms | Flags identifies a concern; confirms requires the relevant diagnostic evidence.
Received versus booked | Prevents referral administration from being mistaken for a scheduled assessment.''',
    d='''Which statement preserves the distinction? | Screening flags a concern; evaluation investigates it. | Screening proves a lifelong diagnosis. | A questionnaire replaces all assessment. | Every concern is automatically false. | Screening and diagnostic evaluation have different roles and should not be treated as equivalent.
Which question clarifies regression? | Was the skill previously present and then lost? | Is the form printed in blue? | Will the diagnosis definitely disappear? | Can we skip the history? | Regression concerns loss of a previously acquired ability rather than simply a skill not yet acquired.
How should multilingual exposure be handled? | Describe it accurately within the assessment. | Assume it explains every concern. | Ignore all languages but English. | Treat it as a diagnosis. | The child's language experience belongs in the assessment without becoming an automatic causal explanation.
Which referral claim is unsupported? | An appointment is already booked. | A pathway is being arranged. | The status needs checking. | No date is supplied. | The case gives no confirmed appointment date or booking.''',
    dialogue='''Ben | The questionnaire flagged a communication concern. Has it already diagnosed Nia with something that will last her whole life?
Dr Shah | No. [[Developmental screening::Developmental screening flags concerns for assessment; it does not establish diagnosis.]] identifies concerns for a closer look; it does not settle a diagnosis by itself.
Ben | I thought the score meant the assessment had already been completed and the conclusion was final.
Dr Shah | A [[diagnostic evaluation::A diagnostic evaluation examines additional information rather than treating screening as definitive.]] considers more information, including history, observation, and the relevant assessments.
Ben | What kinds of language skills are you asking about? She understands some things she does not say.
Dr Shah | [[Receptive language::Receptive language concerns understanding, whereas expressive language concerns communicating ideas.]] concerns understanding, while expressive language concerns what she communicates. We should distinguish those accounts.
Ben | She hears two languages at home and uses different words with different relatives.
Dr Shah | Please describe that [[multilingual exposure::Multilingual exposure belongs in the history but does not explain every concern.]] accurately. We should not assume it explains every concern or ignore abilities in another language.
Ben | Some questions also asked about pointing and how she interacts with other children.
Dr Shah | Those can relate to [[social communication::Social communication includes interaction and is broader than counting spoken words.]], which is broader than counting spoken words alone.
Ben | If she has never used a particular word, is that the same as losing a skill?
Dr Shah | No. [[Skill regression::Skill regression means loss of a previously acquired ability and differs from a skill that has not yet emerged.]] means an ability was present and then lost. The distinction matters in the history.
Ben | Could hearing be part of the assessment, even if we think she hears some sounds?
Dr Shah | A relevant [[hearing assessment::A hearing assessment evaluates hearing and may contribute to investigating communication concerns rather than being replaced by an informal impression.]] may form part of the actual pathway. An informal impression does not replace the appropriate assessment.
Ben | Does getting support have to mean that every diagnostic question has already been answered?
Dr Shah | We can discuss appropriate [[early intervention::Early intervention addresses developmental needs early in childhood, with actual eligibility and services determined through the relevant local process.]] and the local process while explaining what remains uncertain.
Ben | I would like to know whom to contact if we do not hear about the referral.
Dr Shah | We will explain how to check [[referral status::Referral status identifies the current processing stage and should distinguish a sent referral from receipt or a booked appointment.]], including the difference between sending a request and having a confirmed appointment.
Ben | That gives us a next step without pretending the questionnaire has answered everything.
Dr Shah | Exactly. Ongoing [[developmental surveillance::Developmental surveillance follows development across encounters and complements, rather than replaces, screening and appropriate diagnostic assessment.]] continues alongside the appropriate assessment and communication with your family.''',
    rehearsal=['Read the corrected screening discussion, keeping each assessment stage distinct.', 'Swap roles. Explain the next step without predicting a diagnosis or an appointment date.'],
    transfer_title='Receipt is confirmed, booking is not', transfer_setup='The developmental service confirms receipt of Nia\'s referral. No appointment has been booked. The family has a contact for checking progress.',
    transfer='''Caregiver: "The service has confirmed ___." | receipt | The supplied update confirms that the referral reached the service.
Clinician: "An appointment is not yet ___." | booked | Receipt does not establish that an appointment has been scheduled.
Caregiver: "We have a progress-check ___." | contact | The scenario provides a contact for checking the referral's progress.
Clinician: "The diagnostic conclusion remains ___." | pending | No completed diagnostic assessment or conclusion is supplied in this update.'''))

BOOK['units'].append(unit(
    title='Responding to vaccine questions', scene='A concern deserves a specific answer',
    skill='Elicit the actual concern and explain a recommendation without shaming or claiming zero risk.',
    brief='Caregiver Dana worries about fever after a previous vaccination and asks whether the same thing will happen again. Dr Lin asks what occurred and when, reviews the actual record, and explains that timing alone does not establish causation. The clinician will review the current recommendation and individual history. No vaccine schedule, eligibility decision, or product-specific risk estimate is supplied.',
    cast='Dana | Caregiver\nDr Lin | Pediatrician',
    culture=('Specific questions beat labels', 'Ask what the caregiver observed and fears. Labels such as difficult or anti-science obscure the question and can damage the discussion.'),
    a='''What worries Dana? | Fever after a previous vaccination | A known product recall | A supplied contraindication | A confirmed repeated reaction | Dana asks about fever after a previous vaccination and whether it will recur.
What needs review? | The event history and actual recommendation | Only the caregiver's attitude | A guessed schedule | An automatic exemption | The clinician reviews the individual account and current recommendation rather than assuming an answer.
What is not supplied? | A product-specific risk estimate | A caregiver concern | A previous event | A clinician discussion | No product-specific estimate is available in this language case.''',
    vocabulary='''immunization | Process of developing protection against a disease, commonly through vaccination. | discuss immunization
vaccine recommendation | Current advice about use of a particular vaccine in context. | review the vaccine recommendation
vaccination history | Record of previous vaccine administration. | verify vaccination history
adverse event | Unwanted occurrence after an intervention, not necessarily caused by it. | document an adverse event
adverse reaction | Harmful response attributed to an intervention. | distinguish an adverse reaction
temporal association | Events occurring in a time relationship without proving causation. | explain temporal association
causal relationship | Connection in which one event contributes to producing another. | assess a causal relationship
contraindication | Condition making a particular intervention inappropriate under applicable guidance. | verify a contraindication
precaution | Circumstance requiring additional consideration before an intervention. | review a relevant precaution
expected reaction | Known response discussed in the context of a specific product. | explain an expected reaction
vaccine hesitancy | Uncertainty or reluctance concerning vaccination. | explore vaccine hesitancy
informed choice | Decision made after relevant information and questions are addressed. | support informed choice
disease protection | Reduction in disease risk or consequences through an intervention. | explain disease protection
breakthrough infection | Infection occurring despite relevant vaccination or protection. | discuss breakthrough infection
catch-up schedule | Recommended sequence addressing previously missed vaccine doses. | verify a catch-up schedule
administration record | Documentation of a product given and its relevant details. | check the administration record
safety monitoring | Ongoing observation and review of potential safety issues. | explain safety monitoring
absolute risk | Probability or frequency of an outcome in a defined group and period. | communicate absolute risk''',
    precision='After vaccination describes timing. Caused by vaccination requires a causal assessment. Do not dismiss the event or declare its cause without review.',
    precision_extra='Use current, jurisdiction-appropriate recommendations and the actual clinical history. This exercise supplies no schedule, contraindication decision, or guarantee of no reaction.',
    phrases='''Find the concern | What happened after the previous vaccination?
Clarify timing | How soon afterward did you notice the change?
Acknowledge the experience | I can understand why that experience raised a question.
Separate cause and timing | Happening afterward does not by itself establish the cause.
Review the record | Let us check the actual administration record.
Avoid zero-risk language | I will explain the relevant benefits and possible harms.
Invite a focused question | Which part of the recommendation remains unclear?
Close with understanding | Please tell me how you understand the next step.''',
    notes='''After versus because of | After states sequence; because of assigns a cause.
May recur versus will recur | A possible recurrence is not a prediction that the event is certain.
Current recommendation | Keeps the discussion tied to applicable guidance rather than a remembered universal schedule.''',
    d='''Which wording preserves causation uncertainty? | Fever occurred after vaccination; its cause needs review. | Vaccination definitely caused every later symptom. | Timing proves causation. | Nothing happened because causation is uncertain. | The wording acknowledges the event while keeping the causal question open for review.
Which claim is unsupported? | No reaction can ever occur. | We can review the history. | Your question deserves an answer. | The actual recommendation needs checking. | A universal zero-risk promise cannot be justified by this scenario.
What is an adverse event? | An unwanted occurrence not necessarily caused by the intervention | Proof of a contraindication in every case | A guaranteed harmless response | A completed causal investigation | An event after an intervention and a causally attributed reaction are not automatically identical.
Which question is most useful first? | What happened and when? | Why are you being difficult? | Can you agree without questions? | Who told you to worry? | Specific event and timing details support assessment more effectively than labeling the caregiver.''',
    dialogue='''Dana | My child had a fever after the last vaccination. Does that mean the same thing will happen again?
Dr Lin | Let us first review the [[vaccination history::Vaccination history records prior administrations and supports review of the reported event.]] and what you noticed, including when it started and what happened afterward.
Dana | I appreciate that. I was worried you would think asking about it meant refusing every vaccine.
Dr Lin | Asking a question is not a blanket refusal. Your account helps us review the relevant [[adverse event::An adverse event occurs after intervention without necessarily being caused by it.]] rather than dismiss it.
Dana | The timing seemed very close, so I assumed that was enough to prove the cause.
Dr Lin | A [[temporal association::Temporal association establishes sequence, not proof that one event caused another.]] tells us when things happened. It does not, by itself, settle the cause.
Dana | So you are not saying the fever did not happen, only that its explanation needs review?
Dr Lin | Exactly. A [[causal relationship::A causal relationship needs assessment beyond merely identifying which event happened first.]] is a separate question from whether you observed an event.
Dana | What if something in the medical history means a particular vaccine should not be given?
Dr Lin | We review any relevant [[contraindication::A contraindication requires verification against the actual history and applicable guidance.]] and precautions using the actual history and current guidance.
Dana | I would like to hear the benefit as well as what unwanted effects are possible.
Dr Lin | The [[vaccine recommendation::A vaccine recommendation is current advice for a product and context and should be explained with its relevant benefits, limitations, and risks.]] needs that discussion. I should not replace it with a promise of zero risk.
Dana | Sometimes a percentage is hard to understand without knowing how many children it refers to.
Dr Lin | When relevant figures are available, [[absolute risk::Absolute risk gives the probability or frequency for a defined outcome, group, and period, rather than a context-free percentage.]] needs the outcome, group, and time period made clear.
Dana | I also have a record from another clinic, but I am unsure whether every entry was copied.
Dr Lin | We should verify the [[administration record::An administration record documents what was actually given and should be checked before missing entries are treated as completed or omitted doses.]] rather than assume a copied list is complete.
Dana | Does that mean you will create a catch-up plan just from what I remember today?
Dr Lin | No. Any [[catch-up schedule::A catch-up schedule addresses missed doses under current guidance and requires the actual verified history rather than an improvised sequence.]] requires the verified history and applicable recommendation, not a guessed sequence.
Dana | That helps me ask a more specific question instead of trying to decide everything from one memory.
Dr Lin | Good. An [[informed choice::An informed choice follows relevant information and questions being addressed rather than pressure to agree before the concern is understood.]] depends on clear information and a chance to resolve the questions that matter to you.''',
    rehearsal=['Read the corrected exchange. Distinguish timing from a causal claim.', 'Swap roles. Acknowledge the concern without shaming, prescribing a schedule, or promising zero risk.'],
    transfer_title='An incomplete outside record', transfer_setup='An outside vaccination record contains an unclear entry. The clinic requests clarification before treating it as a confirmed administration.',
    transfer='''Caregiver: "This entry is ___." | unclear | The outside record contains an entry whose meaning is unresolved.
Clinician: "We have requested ___." | clarification | The clinic asks the originating source to clarify the entry.
Caregiver: "Administration is not yet ___." | confirmed | An unclear entry is not proof that the vaccine was administered.
Clinician: "We will use the verified ___." | record | The next decision uses the clarified actual record rather than an assumption.'''))

BOOK['units'].append(unit(
    title='Checking liquid-medicine instructions', scene='The label, the units, and the tool',
    skill='Distinguish drug amount from liquid volume and check the actual instructions without calculating a dose.',
    brief='Caregiver Omar sees mg on a prescription and mL on a measuring device and assumes they are interchangeable. Dr Cole explains the difference between drug amount, liquid volume, and concentration. The actual bottle, prescription, and appropriate measuring tool must be checked with the prescribing or dispensing team. No numerical dose, concentration, interval, or instruction to administer medicine is provided here.',
    cast='Omar | Caregiver\nDr Cole | Pediatrician',
    culture=('Teach-back checks the explanation', 'Invite the caregiver to show how the verified instructions would be followed. Correct a misunderstanding without treating it as evidence of carelessness.'),
    a='''Which units does Omar confuse? | mg and mL | cm and meters | Hours and dates | Degrees and percentiles | Omar treats milligrams and milliliters as interchangeable even though they measure different quantities.
What must be checked? | The actual bottle, prescription, and measuring tool | A remembered spoonful | A guessed concentration | Another child's instructions | The case requires the actual verified product and instructions rather than a substitute.
What is deliberately not supplied? | A numerical dose | A unit misunderstanding | A need to verify instructions | A caregiver question | No dose or administration instruction is supplied for the learner to use clinically.''',
    vocabulary='''milligram | Unit of mass used to express an amount of drug. | distinguish milligrams
milliliter | Unit of liquid volume, abbreviated mL. | measure in milliliters
concentration | Amount of drug contained in a stated volume or quantity. | verify the concentration
dose amount | Quantity of drug prescribed for an administration. | confirm the dose amount
dose volume | Volume of a liquid corresponding to a verified dose. | verify the dose volume
oral syringe | Measuring device designed for administering liquid medicine by mouth. | select the appropriate oral syringe
calibration mark | Mark indicating a measured quantity on a device. | read the calibration marks
prescription label | Written instructions attached to a dispensed medicine. | check the prescription label
active ingredient | Substance responsible for the medicine's intended pharmacological action. | identify the active ingredient
duplicate ingredient | Same active substance present in more than one product. | check for duplicate ingredients
administration interval | Time between prescribed administrations. | confirm the administration interval
as-needed instruction | Direction describing use when specified conditions apply. | clarify an as-needed instruction
maximum daily amount | Highest permitted amount over the specified daily period. | verify the maximum daily amount
measuring device | Tool used to determine the required quantity. | match the measuring device
dispensing pharmacy | Pharmacy supplying the prescribed product. | contact the dispensing pharmacy
label discrepancy | Conflict between the label and another instruction or record. | resolve a label discrepancy
caregiver demonstration | Caregiver showing how an instruction is understood. | invite a caregiver demonstration
medication reconciliation | Process of verifying and aligning the actual medicine list. | complete medication reconciliation''',
    precision='Milligrams measure drug mass; milliliters measure liquid volume. The relationship depends on the actual concentration, which must not be guessed.',
    precision_extra='Use the prescribed, verified instructions and appropriate device. Household spoons are not reliable measuring tools. This exercise does not authorize dose calculation or administration.',
    phrases='''Separate the units | Milligrams and milliliters measure different things.
Name the missing link | The actual concentration connects amount and volume.
Use the real product | We need to check this bottle and its current label.
Avoid substitution | Do not assume another bottle has the same concentration.
Resolve a conflict | Let us clarify the conflicting instructions with the responsible team.
Check the tool | The measuring device needs to match the verified instructions.
Invite demonstration | Show me how you understand the verified instruction.
Own the explanation | Let me explain the units more clearly.''',
    notes='''Amount versus volume | Keeps the quantity of drug distinct from the volume of liquid containing it.
This bottle | Anchors the check to the actual product rather than a remembered label.
Show me | Checks practical understanding of verified instructions, not mental arithmetic from an incomplete scenario.''',
    d='''Which statement is correct? | mg measures mass; mL measures volume. | mg and mL always mean the same quantity. | A spoonful fixes every dose. | Concentration never matters. | The units describe different quantities, linked by the actual product concentration.
What must not be guessed? | The concentration | The need for clarification | Omar's stated confusion | The existence of a measuring device | A guessed concentration can make an amount-to-volume interpretation unsafe and is not supplied here.
Which tool is inappropriate for precise measurement? | An ordinary kitchen spoon | An appropriate verified oral syringe | The pharmacist-specified calibrated device | A suitable labeled measuring tool | Household spoons vary and are not reliable substitutes for the appropriate medicine-measuring device.
What is the purpose of demonstration? | Check understanding of verified instructions | Test the caregiver's intelligence | Invent a dose | Replace the actual prescription | A demonstration checks how the explanation was understood using the real verified instructions.''',
    dialogue='''Omar | The prescription says mg, but the measuring device says mL. I thought they meant the same amount.
Dr Cole | A [[milligram::A milligram measures drug mass; a milliliter measures liquid volume.]] measures an amount of drug by mass. A milliliter measures liquid volume.
Omar | Then I cannot just copy the same number from one unit onto the other?
Dr Cole | Correct. The actual [[concentration::Concentration links drug amount and volume and must be verified.]] links drug amount and liquid volume. We must not guess it.
Omar | I have an older bottle at home. Could I use its instructions if the name looks similar?
Dr Cole | We need this product's current [[prescription label::The current prescription label cannot be replaced by another bottle's remembered instructions.]] and verified instructions, not a remembered label from a different bottle.
Omar | I also need to know which measuring tool to use. A kitchen spoon seems easier.
Dr Cole | A kitchen spoon is not a reliable measure. The appropriate [[oral syringe::An oral syringe must suit the actual verified liquid-medicine instruction.]] or other specified device should match the verified instructions.
Omar | Some of the small lines on the device are difficult for me to distinguish.
Dr Cole | We should check the [[calibration mark::Calibration marks indicate measured quantities and must be readable and appropriate to the intended measurement.]] spacing and whether the device is suitable, rather than asking you to estimate between unclear lines.
Omar | If the label and another instruction disagree, which one should I guess is current?
Dr Cole | Do not guess. A [[label discrepancy::A label discrepancy is a conflict between instructions that needs clarification with the responsible prescribing or dispensing team.]] needs clarification with the responsible prescribing or dispensing team.
Omar | Would the pharmacy be able to check the product it actually supplied?
Dr Cole | Yes, the [[dispensing pharmacy::The dispensing pharmacy supplied the product and is an appropriate contact for verifying its label, concentration, and measuring device.]] is an appropriate contact for verifying the dispensed product and its instructions.
Omar | I use another over-the-counter product sometimes. Should that be part of the review too?
Dr Cole | Yes. Reviewing the [[active ingredient::The active ingredient is the pharmacologically active substance and should be checked across products rather than relying only on brand names.]] helps identify possible duplication; similar or different brand names do not settle that question.
Omar | Once everything is verified, can I show you how I understand the instruction?
Dr Cole | A [[caregiver demonstration::A caregiver demonstration shows how verified instructions are understood and allows the explanation or equipment to be corrected before use.]] is useful. It checks our explanation and the tool, not your intelligence.
Omar | I can now distinguish the amount of drug from the liquid that contains it.
Dr Cole | Exactly. The [[dose volume::Dose volume is the liquid quantity corresponding to a verified dose and concentration; it is not supplied or calculated in this exercise.]] must match the verified instructions. Let us check the bottle, prescription, and measuring device together before confirming what to give.''',
    rehearsal=['Read the corrected exchange. Say milligrams and milliliters in full at first mention.', 'Swap roles. Practice resolving the instruction conflict without inventing a dose or concentration.'],
    transfer_title='Two products may share an ingredient', transfer_setup='A caregiver brings two products with different brand names. Their active ingredients have not yet been checked. The clinician asks the responsible team to review them.',
    transfer='''Caregiver: "The brand names are ___." | different | The products have different brand names in the supplied scenario.
Clinician: "The active ingredients remain ___." | unchecked | Different brands do not establish whether their active ingredients differ.
Caregiver: "We should not assume there is no ___." | duplication | The ingredients must be reviewed before excluding duplication.
Clinician: "The responsible team will ___ them." | review | The next step is the actual product review, not a guessed administration plan.'''))

BOOK['units'].append(unit(
    title='Explaining adolescent confidentiality', scene='Privacy without an impossible promise',
    skill='Explain private discussion, record access, and safety limits before sensitive disclosure.',
    brief='Sixteen-year-old Alex asks Dr Hale whether everything discussed will remain private. Dr Hale explains that confidentiality, consent, caregiver access, portal settings, billing, and safety duties depend on the applicable rules and service. The clinician offers an appropriate private discussion and checks actual access arrangements. The case supplies no jurisdiction-specific legal conclusion.',
    cast='Alex | Adolescent patient\nDr Hale | Pediatrician',
    culture=('Explain limits before collecting the detail', 'Do not promise absolute secrecy and then reveal exceptions later. Make the actual privacy arrangements understandable without discouraging the adolescent from seeking care.'),
    a='''What does Alex ask? | Whether everything will remain private | Whether every record is already deleted | Whether a law has been supplied | Whether billing is always invisible | Alex asks about the limits of privacy before sensitive discussion.
What does Dr Hale check? | Actual access arrangements and applicable rules | A universal rule from memory | Only the room number | Nothing beyond verbal reassurance | Privacy depends on the real service, records, and applicable requirements.
What is not supplied? | A jurisdiction-specific legal conclusion | Alex's age | A privacy question | A clinician explanation | The case does not determine the legal rules for a particular jurisdiction.''',
    vocabulary='''confidentiality | Duty to protect information within applicable rules and limits. | explain confidentiality
private consultation | Discussion held without others present when appropriate. | offer a private consultation
consent capacity | Ability to make the relevant informed decision under applicable standards. | assess consent capacity
minor consent | Rules governing a minor's authorization for particular care. | verify minor-consent rules
guardian authority | Legally recognized decision-making role for a child in context. | clarify guardian authority
proxy access | Another person's permitted access to a patient's information system. | check proxy access
portal visibility | Information viewable through a patient-access system. | verify portal visibility
billing disclosure | Information potentially revealed through payment or insurance processes. | explain possible billing disclosure
safety exception | Circumstance permitting or requiring disclosure for safety under applicable rules. | explain a safety exception
mandatory reporting | Legally required communication of specified concerns to an authority. | clarify mandatory-reporting duties
information sharing | Disclosure of relevant information to another person or service. | discuss information sharing
minimum necessary information | Limited information appropriate to a particular authorized purpose. | identify necessary information
preferred contact method | Communication route the person wishes the service to use. | confirm the preferred contact method
confidential contact | Communication handled through an appropriately private route. | arrange a confidential contact
record-access rule | Requirement governing who can see particular health information. | verify record-access rules
privacy limitation | Boundary on what can be kept private in the actual setting. | explain privacy limitations
safeguarding concern | Concern about safety or welfare requiring appropriate assessment or action. | address a safeguarding concern
supported disclosure | Planned sharing of information with appropriate explanation and support. | arrange supported disclosure''',
    precision='Privacy in the room does not automatically make portal, billing, or later communications private. Check the actual channels.',
    precision_extra='Avoid universal claims about minor consent or caregiver access. Explain the applicable rules, safety obligations, and any limits before promising confidentiality.',
    phrases='''Avoid absolute secrecy | I cannot promise that every circumstance is completely private.
Explain before disclosure | Let us discuss the privacy limits before you share the detail.
Offer private time | We can arrange an appropriate conversation without your caregiver present.
Check access | I need to verify who can see this part of the record.
Discuss channels | Portal messages and billing may have different access arrangements.
Explain safety | I will explain the relevant safety duties in this setting.
Ask about contact | Which contact method is appropriate for us to use?
Support sharing | When sharing is needed, I will explain the process and support you.''',
    notes='''Private versus confidential | Private describes the setting; confidentiality concerns handling information under applicable duties.
May have access | Preserves uncertainty until the actual access arrangements are checked.
Before you share | Places the explanation of limits before sensitive detail is requested.''',
    d='''Which promise is unsafe? | Nothing you say can ever be shared under any circumstances. | We can discuss the actual limits. | I will check portal access. | Let us confirm the contact route. | Absolute secrecy ignores possible legal, safety, and record-access limits.
Which issue is separate from privacy in the room? | Portal and billing visibility | The chair color | The clinician's pen | The appointment font | A private conversation can still generate records or communications with separate access arrangements.
Which legal statement is justified here? | Applicable rules must be verified. | Every minor has identical rights everywhere. | Every caregiver sees every record everywhere. | No safety duty can apply. | The case supplies no jurisdiction and therefore requires checking the actual rules.
What should happen before sensitive disclosure? | Explain relevant privacy limits | Promise secrecy without checking | Ask for every detail first | Ignore contact preferences | Explaining limits first helps the adolescent understand how information may be handled.''',
    dialogue='''Alex | Before I say anything personal, can you promise that everything stays between us and nobody else can see it?
Dr Hale | I can explain [[confidentiality::Confidentiality protects information within applicable limits; it is not absolute secrecy.]], but I should not promise absolute secrecy before discussing the actual limits.
Alex | I would like some time without my caregiver in the room. Is that different from the record being private?
Dr Hale | Yes. A [[private consultation::A private consultation does not automatically make subsequent records or messages private.]] and access to information afterward are separate questions.
Alex | My caregiver sometimes reads messages in the patient portal. Could that affect what I send?
Dr Hale | We need to check [[proxy access::Proxy access allows another person specified access and needs actual verification.]] and the settings for this service rather than assume messages are invisible.
Alex | What about letters or insurance information that arrive at home after an appointment?
Dr Hale | Possible [[billing disclosure::Billing disclosure may reveal information separately from the privacy of the consultation.]] and other communications also need explanation. The contact route matters.
Alex | Does being sixteen mean the rules are automatically the same for every type of care?
Dr Hale | No. [[Minor consent::Minor-consent rules vary by jurisdiction and the particular care involved.]] rules depend on the applicable law and the care involved.
Alex | I also want to understand when you might have to tell someone about a safety concern.
Dr Hale | We should discuss the relevant [[safety exception::A safety exception depends on applicable duties, not a universal secrecy promise.]] and duties before asking you for sensitive detail.
Alex | Would you explain what you needed to share, rather than suddenly telling me afterward?
Dr Hale | I will explain the process and support you as appropriate. [[Mandatory reporting::Mandatory reporting is a legal duty to communicate specified concerns and must be explained according to the actual applicable requirements.]] duties, where they apply, cannot be replaced by a promise of silence.
Alex | I understand. Could we agree on how the service should contact me about ordinary follow-up?
Dr Hale | Yes. Let us confirm your [[preferred contact method::A preferred contact method identifies the desired communication route, which the service must check against its actual privacy and operational arrangements.]] and check what the service can actually provide.
Alex | I would rather know a limitation now than discover it after I have sent a message.
Dr Hale | That is why [[record-access rule::A record-access rule governs who can see particular information and should be verified before assurances are given about portal or record privacy.]] checks belong before an assurance, not after it.
Alex | Once those arrangements are explained, I can ask my question with a clearer understanding of the boundaries.
Dr Hale | Exactly. Where sharing is necessary, [[supported disclosure::Supported disclosure involves explaining and supporting the appropriate sharing process rather than leaving the young person surprised about how information is handled.]] can help us explain the next step while following the actual duties.''',
    rehearsal=['Read the corrected privacy discussion. Distinguish the room, the record, and communication channels.', 'Swap roles. Explain qualified confidentiality without stating a universal law.'],
    transfer_title='A shared phone number', transfer_setup='A teenager says the listed phone is shared with a caregiver. The clinic has not verified a private contact route. No sensitive message has been sent.',
    transfer='''Teenager: "That phone is ___." | shared | The listed phone is shared rather than known to be private.
Clinician: "A private route is not yet ___." | verified | The clinic has not confirmed an appropriate confidential contact route.
Teenager: "No sensitive message has been ___." | sent | The scenario explicitly states that no sensitive message has been sent.
Clinician: "We need to check the contact ___." | arrangements | The actual contact process must be checked before assurances are given.'''))

BOOK['units'].append(unit(
    title='Coordinating care with a school', scene='A plan must reach the people who use it',
    skill='Translate a clinician-approved care plan into clear responsibilities and authorized communication.',
    brief='Dr Moss and school nurse Rivera discuss a student with an existing asthma diagnosis. The current clinician-approved action plan must be verified and shared through the authorized process. Rivera reports that the school holds an older version. The exercise supplies no inhaler dose, symptom threshold, or independent permission for staff to change treatment.',
    cast='Dr Moss | Pediatrician\nRivera | School nurse',
    culture=('Sending is not the same as implementation', 'Check the version, recipient, authorization, and practical readiness. A document that exists but has not reached the responsible person does not complete the communication.'),
    a='''What does the school hold? | An older action-plan version | A newly verified version | A new diagnosis | An authorized dose change | Rivera reports an older plan rather than a verified current version.
What must be checked? | The current plan and authorized sharing | Only the student's attendance | A guessed inhaler dose | An informal verbal replacement | The case requires verification and appropriate sharing of the clinician-approved plan.
What is not permitted by the exercise? | Independent treatment changes | Version verification | Acknowledging receipt | Clarifying responsibility | No dose, threshold, or independent authority to alter treatment is supplied.''',
    vocabulary='''asthma action plan | Individualized clinician-approved instructions for managing asthma situations. | verify the asthma action plan
controller medicine | Medicine used to manage ongoing disease control as prescribed. | explain controller medicine
reliever medicine | Medicine prescribed for relief in specified circumstances. | clarify reliever instructions
inhaler technique | Method of using the prescribed inhaler correctly. | review inhaler technique
spacer device | Holding chamber used with a compatible inhaler when prescribed. | check the spacer device
trigger exposure | Contact with a factor associated with symptoms. | describe trigger exposure
exercise-related symptom | Symptom occurring in association with physical activity. | report exercise-related symptoms
school health plan | Documented arrangements for a student's health needs at school. | update the school health plan
medication authorization | Required permission for medicine-related action in a setting. | verify medication authorization
self-carry permission | Authorization for a student to carry their own medicine. | check self-carry permission
emergency action | Required response under the actual urgent-care plan. | confirm emergency actions
plan version | Identified edition of a care document. | verify the plan version
school contact | Named person responsible for relevant school communication. | identify the school contact
care coordination | Organization of care information and responsibilities across participants. | strengthen care coordination
activity accommodation | Appropriate adjustment supporting participation in an activity. | discuss activity accommodations
field-trip arrangement | Health-related preparation for an off-site school activity. | confirm field-trip arrangements
receipt confirmation | Acknowledgment that the intended recipient received a document. | obtain receipt confirmation
implementation readiness | Confirmation that the plan can be carried out by the appropriate people. | check implementation readiness''',
    precision='An older plan must not be treated as the current instruction. The exercise does not supply medicine doses or authorize staff to improvise changes.',
    precision_extra='Sharing authorization, receipt, and readiness are separate checks. Use the actual emergency plan and professional scope, not the language exercise, for care.',
    phrases='''Verify the version | Which dated version does the school currently hold?
Name the mismatch | That differs from the version we are reviewing.
Check authorization | We need the appropriate permission for sharing and administration.
Avoid improvisation | Please do not substitute an unverified dose or instruction.
Confirm receipt | Please acknowledge receipt of the verified plan.
Ask about readiness | Are the responsible people and required arrangements in place?
Cover another setting | Let us check the field-trip arrangements separately.
Close the loop | We need both the current document and confirmed responsibilities.''',
    notes='''Current versus available | A document being available does not establish that it is the current version.
Receipt versus readiness | Receiving a file does not prove staff and equipment are prepared to implement it.
Separate arrangements | Another setting may require its own practical preparation rather than an assumed copy of the classroom process.''',
    d='''Which question addresses version control? | Which dated plan does the school hold? | Which color is the folder? | Can we use any old dose? | Does receipt prove readiness? | The date and version identify whether the school holds the appropriate current plan.
What is not equivalent to implementation? | Sending the document | Confirming authorized responsibilities | Verifying the current plan | Checking actual readiness | A sent file may not have been received or made usable by the responsible people.
Which instruction is unsupported? | Increase the inhaler dose from this exercise. | Verify the plan. | Check authorization. | Confirm receipt. | The exercise provides no dose or authority for an independent treatment change.
Why check a field trip separately? | The practical setting and arrangements may differ. | The diagnosis disappears off-site. | Permission never matters outside school. | An old plan automatically becomes current. | Off-site activities may require different practical preparation within the actual approved care arrangements.''',
    dialogue='''Rivera | The school has an asthma plan, but its date is older than the version the family mentioned this morning.
Dr Moss | Let us verify the [[plan version::Plan version identifies the actual edition; an available copy may be outdated.]] before anyone assumes the instructions are unchanged.
Rivera | I would like the current document through the authorized route, not a partial photograph from another parent.
Dr Moss | Agreed. We need the verified [[asthma action plan::An asthma action plan contains individualized instructions, not an improvised substitute.]] and appropriate permission for sharing it.
Rivera | We also need to know which staff are authorized to assist and what permissions apply.
Dr Moss | Check the actual [[medication authorization::Medication authorization does not follow automatically from possessing the care document.]] and professional responsibilities rather than infer them from the document's presence.
Rivera | The family asked whether the student can carry the inhaler independently at school.
Dr Moss | [[Self-carry permission::Self-carry permission needs the actual authorization process, not an assumed entitlement.]] depends on the applicable arrangements. This discussion does not grant it automatically.
Rivera | Once the verified plan arrives, I will acknowledge that the intended school contact has received it.
Dr Moss | That [[receipt confirmation::Receipt confirmation establishes arrival, not readiness to implement every instruction.]] is useful, but we should separately confirm practical readiness.
Rivera | You mean the people, equipment, and procedures needed to carry out the actual plan?
Dr Moss | Yes. [[Implementation readiness::Implementation readiness requires the actual people and practical arrangements, not just paperwork.]] is more than keeping a file in the school record.
Rivera | There is also a field trip next week, which has a different staffing arrangement.
Dr Moss | Then check the [[field-trip arrangement::A field-trip arrangement addresses the practical health preparation for an off-site activity and should not be assumed identical to the classroom setup.]] through the appropriate process rather than assume the classroom plan transfers unchanged.
Rivera | I will use the child's current signed plan and clarify anything that does not match the instructions we hold.
Dr Moss | Correct. The actual [[emergency action::Emergency action follows the student's real urgent-care plan and applicable procedures, not an invented threshold from a language exercise.]] comes from the verified plan and real clinical process.
Rivera | The student also wants to participate in activities without being treated as a problem.
Dr Moss | Appropriate [[activity accommodation::An activity accommodation supports participation through suitable adjustments and should be coordinated with the actual clinical and school arrangements.]] can be discussed without assuming exclusion or promising unrestricted participation.
Rivera | I will confirm the version, authorization, receipt, and any outstanding practical issue through the designated contact.
Dr Moss | That is effective [[care coordination::Care coordination aligns information and responsibilities across the family, school, and clinical team rather than ending when a document is sent.]]: a usable current plan and clear responsibilities across the family, school, and clinical team.''',
    rehearsal=['Read the corrected school exchange, separating version, permission, receipt, and readiness.', 'Swap roles. Confirm the communication process without adding medicine instructions.'],
    transfer_title='The new file arrived but training is pending', transfer_setup='The school confirms receipt of the verified current plan. The responsible staff still need the required preparation. Implementation readiness is not yet confirmed.',
    transfer='''Nurse: "The current plan has been ___." | received | The school confirms receipt of the verified current document.
Clinician: "Staff preparation remains ___." | pending | The scenario says the required preparation is not yet complete.
Nurse: "Receipt does not prove ___." | readiness | A document's arrival is distinct from practical implementation readiness.
Clinician: "Please confirm the remaining ___." | arrangements | The outstanding staff preparation and practical arrangements require follow-up.'''))

BOOK['units'].append(unit(
    title='Handing over an urgent change', scene="Different from the infant's usual behavior",
    skill="Lead with a concerning change and preserve the caregiver's account during an active urgent response.",
    brief='Caregiver Mei reports that infant Arlo is much less responsive than usual and is feeding poorly. The actual emergency response is already active; this language exercise must not delay it. Dr Reed receives the account and transfers the relevant information to the clinical team. No diagnosis, measured observations, or safe waiting interval is supplied.',
    cast='Mei | Caregiver\nDr Reed | Pediatrician',
    culture=('Take a change from usual seriously', 'A caregiver can identify an important change without having clinical vocabulary. Ask for concrete observations while the real response proceeds, and do not replace uncertainty with reassurance.'),
    a='''What change does Mei report? | Much less responsiveness and poor feeding | A confirmed diagnosis | Normal measured observations | A safe waiting period | The supplied concern is a marked change in responsiveness with poor feeding.
What is already active? | The emergency response | A routine appointment next month | A completed discharge | A language-only review | The emergency response is active and must not wait for this exercise.
What must remain unknown here? | The diagnosis and measured observations | Mei's report | Arlo's name | The need to preserve the account | No diagnosis or measurements are supplied, so they cannot be invented.''',
    vocabulary='''responsiveness | Degree of response to people or stimulation in context. | describe reduced responsiveness
poor feeding | Feeding less effectively or less than usual as reported or assessed. | report poor feeding
usual pattern | Person's typical behavior used as a comparison. | establish the usual pattern
caregiver concern | Worry expressed by the person caring for the child. | acknowledge caregiver concern
acute change | New or recent difference from the prior state. | communicate an acute change
observed behavior | Action or response personally witnessed by the reporter. | describe observed behavior
last known usual state | Most recent time the person was observed in their usual state. | clarify the last known usual state
measured observation | Value obtained through an actual assessment or measurement. | relay measured observations
work of breathing | Effort involved in breathing as clinically assessed. | assess work of breathing
hydration assessment | Clinical evaluation of fluid status using relevant information. | perform a hydration assessment
urine output | Amount or pattern of urine production over time. | clarify urine output
febrile illness | Illness involving fever in the relevant clinical context. | assess a febrile illness
clinical deterioration | Worsening of a person's clinical condition. | communicate suspected clinical deterioration
urgent escalation | Prompt transfer of a concern through the appropriate clinical route. | initiate urgent escalation
emergency response | Active process for addressing an urgent clinical situation. | confirm the emergency response
receiving clinician | Professional accepting the relevant care information and responsibility. | identify the receiving clinician
handoff priority | Most important information to lead a transfer of care. | state the handoff priority
read-back confirmation | Repetition of key information to verify accurate receipt. | obtain read-back confirmation''',
    precision='Less responsive than usual is the caregiver\'s important report, not a measured consciousness score. Preserve the account while the actual emergency assessment proceeds.',
    precision_extra='The absence of supplied measurements does not make the situation reassuring. Do not use the exercise to choose a diagnosis or a waiting interval.',
    phrases='''Lead with the change | You are reporting a clear change from Arlo's usual behavior.
Confirm action | The emergency response is already active.
Ask concretely | What response did you see when you spoke to Arlo?
Preserve the source | I will pass on exactly what you observed.
Avoid false reassurance | We do not have a diagnosis or verified measurements to explain this yet.
Keep urgency separate | Do not wait to complete this conversation before following the emergency process.
Identify the receiver | I will confirm which clinician is receiving the information.
Check the message | Please repeat the key change so we can confirm accurate receipt.''',
    notes='''Usual versus normal | Usual compares with this infant's baseline; normal would imply a broader clinical assessment.
Reports versus measured | A caregiver report and a measured observation have different sources.
Already active | Keeps the actual emergency process ahead of completing the language task.''',
    d='''Which opening conveys the priority? | Arlo is much less responsive than usual and feeding poorly. | There may be some paperwork. | Everything is normal because no numbers are shown. | A definite diagnosis has been established. | The opening conveys the reported change without inventing measurements or diagnosis.
Which statement is unsupported? | Arlo's measured observations are normal. | Mei reports a change. | Emergency response is active. | The receiving team needs the account. | No measured observations are supplied, so normal cannot be asserted.
What should not delay care? | Completing the language exercise | The actual emergency response | Necessary clinical assessment | Appropriate urgent action | Language practice must never postpone the active clinical response.
What does read-back accomplish? | Checks accurate receipt of key information | Establishes a diagnosis automatically | Replaces clinical examination | Guarantees recovery | Repeating the key information verifies communication, not diagnosis or outcome.''',
    dialogue='''Mei | Arlo is much less responsive than usual and has been feeding poorly. This is very different from the usual pattern.
Dr Reed | I hear the change. The [[emergency response::The emergency response continues without waiting for completion of this discussion.]] is already active, and the clinical team is receiving the concern.
Mei | I do not know the medical word. Arlo does not respond to my voice in the usual way.
Dr Reed | That description of [[responsiveness::Responsiveness is the caregiver's report here, not an invented clinical score.]] is useful. Tell us what you observed rather than trying to choose a diagnosis.
Mei | I can describe what I saw, but I have not measured anything or kept a formal chart.
Dr Reed | We will distinguish your [[observed behavior::Observed behavior identifies what the caregiver witnessed, distinct from clinical measurements.]] report from any measurements the team obtains during assessment.
Mei | The feeding is also different. I do not want that detail to disappear when someone else takes over.
Dr Reed | I will include [[poor feeding::Poor feeding is a reported change, not an established cause.]] in the handoff alongside the reduced responsiveness.
Mei | Should I try to remember the exact time everything changed before the team continues?
Dr Reed | Clarify the [[last known usual state::Last known usual state records the most recent observed baseline without delaying care.]] as accurately as you can, but do not delay the active response to produce a perfect timeline.
Mei | I am certain this is different from yesterday, even if I cannot give an exact minute.
Dr Reed | That [[caregiver concern::Caregiver concern can identify an important change and should be acknowledged without demanding clinical terminology or false precision.]] matters. We will preserve the uncertainty about timing instead of replacing it with a guessed value.
Mei | Will the next clinician hear my words or only a short label that loses the change?
Dr Reed | The [[handoff priority::Handoff priority identifies the most important information to lead the transfer, here the reported change in responsiveness and feeding.]] is the change you described, with its source and what is still unknown.
Mei | I do not want someone to assume that missing numbers mean all the observations are normal.
Dr Reed | They do not. A [[measured observation::A measured observation must come from actual assessment and cannot be called normal when no value or finding has been supplied.]] requires an actual assessment; missing information is not reassurance.
Mei | Who will be responsible for receiving the update as the assessment continues?
Dr Reed | We will identify the [[receiving clinician::The receiving clinician accepts the relevant information and responsibility and should be explicitly identified rather than assumed.]] through the active process and confirm the transfer.
Mei | I can repeat the main change if that helps make sure it was heard correctly.
Dr Reed | A [[read-back confirmation::Read-back confirmation repeats key information to check accurate receipt while the actual clinical response continues.]] helps: reduced responsiveness compared with usual, poor feeding, and the emergency process continuing now.''',
    rehearsal=['Read the corrected handoff, leading with the two reported changes and the active response.', 'Swap roles. Preserve uncertain timing without inventing measurements or a safe waiting interval.'],
    transfer_title='The timeline is corrected during care', transfer_setup='During an active emergency response, the caregiver corrects the last observed usual state from 08:00 to 07:30. The receiving clinician acknowledges the correction. No diagnosis is supplied.',
    transfer='''Caregiver: "The corrected time is ___." | 07:30 | The caregiver explicitly corrects the last observed usual state to 07:30.
Clinician: "The earlier report of ___ is superseded." | 08:00 | The prior time is replaced by the caregiver's corrected account.
Caregiver: "The emergency response remains ___." | active | Correcting the timeline does not interrupt the ongoing emergency response.
Clinician: "The diagnosis remains ___." | unestablished | The timing correction does not establish a clinical diagnosis.'''))
