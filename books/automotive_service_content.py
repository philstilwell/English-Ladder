"""Original Automotive Service English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='automotive-service', title='Automotive Service English',
    cover_label='ENGLISH FOR SERVICE ADVISORS, TECHNICIANS, AND PARTS TEAMS',
    cover_title='Automotive\nService', cover_size=40,
    tagline='Accurate concerns. Clear commitments.',
    audience='For automotive service advisors, technicians, parts staff, and customer-service teams working with vehicle owners and workshop colleagues.',
    map_intro='Eight service conversations follow the customer journey: capture an intermittent concern, clarify drop-off, confirm assessment scope, brief the technician, explain a parts delay, relay a diagnostic finding, read an invoice, and recover a mishandled repeat complaint.',
    notes_title='Make the next handoff more accurate.',
    notes_intro='Good service English keeps the vehicle, symptom, permission, price, and promised contact clear. Practice explaining technical information without guessing at a diagnosis or turning an estimate into a guarantee.',
    field_notes=[
        ('Keep the customer concern intact', 'Record the vehicle, the sound or symptom, its reported location, and when it occurs. A customer description is useful evidence without being a diagnosis. Intermittent does not mean imaginary or constant.', '"The blue hatchback has an occasional rear rattle after overnight parking; cause unknown."'),
        ('Define the commitment', 'Drop-off is not necessarily the start of workshop work. A status call is not a finish promise. Go ahead needs a precise readback of what the customer is authorizing under the stated shop terms.', '"You authorize the $95 assessment only; any repair proposal needs separate approval."'),
        ('Separate clues from conclusions', 'A diagnostic trouble code can guide investigation without proving that a named sensor needs replacement. Relay the technician record and ask for the missing explanation rather than supplying one from assumption.', '"The note records a code, but no confirmed cause or component fault."'),
        ('Repair the conversation as well as the record', 'When a customer reports a repeat concern, correct an unsupported dismissal. Acknowledge the new report, retain the earlier history, and state the next contact without promising coverage or a technical result.', '"I should not have said that was impossible. Nia can call at 15:00 to review your report."'),
    ],
    scope_note='The vehicles, shop terms, charges, records, and events are fictional. This book teaches English, not vehicle diagnosis, repair, testing, driving decisions, or legal advice. Follow actual training, authorization, manufacturer information, shop procedures, and applicable requirements. A code, invoice, or customer description does not establish vehicle safety, readiness, repair necessity, or warranty coverage. The dialogues give no instructions to reproduce symptoms while driving or work on a vehicle.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Automotive Service Technicians and Mechanics.',
             url='https://www.bls.gov/ooh/installation-maintenance-and-repair/automotive-service-technicians-and-mechanics.htm',
             note='Occupational context for customer communication, workshop records, maintenance, and repair roles. Technical procedures are not reproduced.', checked='1 October 2026'),
        dict(title='Federal Trade Commission. Auto Repair Basics.',
             url='https://consumer.ftc.gov/articles/0211-auto-repair-basics',
             note='Background for distinguishing diagnostic charges, estimates, parts, labor, and repair records. The fictional charges are not market prices or universal legal rules.', checked='1 October 2026'),
        dict(title='Bosch Car Service. Car Diagnostics.',
             url='https://ap.boschcarservice.com/in/en/car-services/car-diagnostics/',
             note='Reference for distinguishing fault-code information from confirmed diagnosis and replacement decisions. No testing or repair instructions are supplied.', checked='1 October 2026'),
        dict(title='Federal Trade Commission. Auto Warranties and Auto Service Contracts.',
             url='https://consumer.ftc.gov/articles/auto-warranties-and-auto-service-contracts',
             note='Context for checking actual coverage and terms rather than promising them. The cases offer no warranty determination or jurisdiction-specific advice.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title="Capturing the customer's concern",
    scene='The blue hatchback and an occasional rear rattle',
    skill='Identify the booked vehicle and capture an intermittent customer concern without inventing its frequency, cause, or technical finding.',
    brief='Two household cars are listed on the account, but today Mina has booked the blue hatchback. She reports an occasional rattle from the rear after the car has been parked overnight. She does not know the cause, and no technician assessment has occurred. Advisor Ellis must confirm the vehicle, preserve the reported sound and conditions, and read back the concern. Mina is describing existing observations; she is not asked to drive or perform a test to reproduce the sound.',
    cast='Mina | Customer\nEllis | Service advisor',
    culture=('Capture the description before translating it into workshop shorthand', 'A customer can describe a sound accurately without knowing a component name. Confirm the vehicle and repeat the reported conditions. Keep everyday wording when it carries useful meaning, and avoid leading questions that make a suspected part sound like an established fault.'),
    a='''Which vehicle is booked today? | The blue hatchback | Both household cars | An unspecified workshop loan car | The other car by default | The brief identifies the blue hatchback as the vehicle for this booking.
How does Mina describe the sound? | An occasional rattle from the rear | A constant front-end knock | A verified brake failure | A continuous engine squeal | The report is intermittent and located toward the rear, without a confirmed cause.
What assessment has occurred? | None by a technician yet | A confirmed component diagnosis | A completed repair verification | A finding that the car is fault-free | No technician assessment has taken place at the point of this conversation.''',
    vocabulary='''service advisor | Staff member coordinating customer communication and workshop work. | brief the service advisor
customer concern | Issue described by the vehicle owner or user. | capture the customer concern
vehicle identification | Information establishing which vehicle a record concerns. | confirm vehicle identification
household account | Customer record containing vehicles used by one household. | check the household account
hatchback | Car body style with an upward-opening rear door to the cargo area. | identify the blue hatchback
booking reference | Identifier for a scheduled service appointment. | confirm the booking reference
registration number | Identifier assigned through vehicle registration. | verify the registration number
vehicle identification number | Unique vehicle identifier commonly abbreviated VIN. | confirm the vehicle identification number
make | Manufacturer or brand of a vehicle. | record the make
model | Named vehicle design within a manufacturer's range. | confirm the model
model year | Year designation associated with a vehicle version. | identify the model year
odometer | Instrument recording accumulated vehicle distance. | record the odometer reading
intermittent | Occurring at intervals rather than continuously. | describe an intermittent concern
rattle | Repeated light knocking or vibrating sound. | describe the reported rattle
rear | Part or direction toward the back of the vehicle. | locate the sound at the rear
overnight parking | Period during which a vehicle remains parked through the night. | note overnight parking
reported conditions | Circumstances described as accompanying the concern. | preserve the reported conditions
frequency | How often a symptom is reported to occur. | clarify the reported frequency
onset | Time or circumstance when a symptom begins. | distinguish onset from observation
symptom description | Account of the experienced sound, behavior, or condition. | retain the symptom description
technician assessment | Relevant professional evaluation of the concern. | distinguish a technician assessment
suspected cause | Possible explanation not yet verified. | avoid presenting a suspected cause as fact
job card | Workshop record containing the requested work and relevant details. | prepare the job card
concern readback | Repetition of the customer's account to confirm accuracy. | give a concern readback''',
    precision='The booked vehicle is the blue hatchback, not both cars on the account. The sound is occasional and reported from the rear after overnight parking. Do not change those details to a constant noise or a named failed component.',
    precision_extra='No technician assessment has occurred. The readback should preserve what Mina has already experienced without asking her to reproduce a symptom while driving or inventing details about speed, exact duration, cause, or vehicle safety.',
    phrases='''Confirm the vehicle | Which of the two cars is booked today?
Repeat the selection | I have the blue hatchback for this appointment.
Keep the account separate | I will not attach this concern to the other vehicle.
Ask for the existing description | How have you described the sound you noticed?
Preserve the sound | You report a rattle from the rear.
Preserve frequency | It is occasional, not constant.
Clarify the condition | You have noticed it after the car was parked overnight.
Avoid inventing a cause | You have not identified what causes it.
Keep assessment separate | No technician assessment has taken place yet.
Avoid leading terminology | I will record rattle without naming a failed component.
Keep the record attributed | The customer reports the following concern.
Avoid a false guarantee | This description does not establish whether the vehicle is fault-free.
Distinguish identity fields | A model name and a vehicle identification number are different.
Ask for confirmation | Does that wording accurately describe your experience?
Give the complete readback | Blue hatchback; occasional rear rattle after overnight parking; cause unknown.
Close with the handoff | I will put that concern on the job card for assessment.''',
    notes='''Occasional versus constant | Preserves how often the sound is reported without inventing a frequency.
From the rear | Locates the perceived sound without identifying a particular component.
After overnight parking | Records a circumstance, not necessarily a proven cause.
Customer reports | Separates the account from a technician finding.
Has not taken place yet | Identifies the current assessment stage.
Does that wording ...? | Invites a bounded accuracy check instead of a request to diagnose the vehicle.''',
    d='''Which job-card wording preserves the account? | Customer reports occasional rear rattle after overnight parking in blue hatchback | Technician confirmed rear suspension failure | Both cars have constant engine noise | Customer proved the vehicle is safe | The wording retains vehicle, attribution, sound, frequency, and reported conditions.
Which question is leading? | Which rear component has failed? | Which car is booked today? | Is the sound occasional or constant in your account? | Does this readback match what you noticed? | The question assumes a failed component before any assessment has occurred.
What should Ellis not add? | A precise cause or unreported driving condition | The blue hatchback | The rear location | Overnight parking | The account contains no verified cause or additional driving conditions.
Why should the vehicle be confirmed first? | Two cars are on the account and only one is booked | Color proves the mechanical cause | Both cars must receive the same repair | The booking identifies a failed sensor | Confirming identity prevents the concern from being attached to the wrong household vehicle.''',
    dialogue='''Mina | I have booked in because of a rattle. We have two cars on the account, so I want to make sure the notes go against the right one.
Ellis | Certainly. Let us confirm the [[vehicle identification::Vehicle identification prevents this concern from being recorded against the other household car.]] first. Which of the two cars is booked for today's appointment?
Mina | The blue hatchback. The other car is on the same household account, but today's concern is only about the hatchback.
Ellis | I will keep the [[booking reference::Booking reference connects today's appointment to the selected vehicle rather than both cars.]] with the blue hatchback and make sure the concern is recorded there. How would you describe the sound you have noticed?
Mina | It is a rattle from the rear. It happens occasionally, and I have noticed it after the car has been parked overnight.
Ellis | I will record an [[intermittent::Intermittent preserves Mina's description of an occasional sound rather than a constant one.]] rattle from the rear after overnight parking. In this context, intermittent means occasional rather than continuous; is that consistent with your experience?
Mina | Yes. I do not want the note to say it happens all the time. I cannot give you a fixed number of occurrences either.
Ellis | Then we will preserve the reported [[frequency::Frequency is limited to occasional because Mina has not supplied a count or fixed pattern.]] as occasional, without inventing a count. The technician should receive what you know, not a more definite pattern than you described.
Mina | I also do not know which part makes the sound. I can say rear, but I cannot name a component or explain why it happens.
Ellis | That is enough for the [[symptom description::Symptom description captures the experienced sound and location without requiring a component diagnosis.]]. We can keep rear as the reported location without turning it into a claim that a particular component has failed.
Mina | Good. I have not had a technician assess it yet, so any technical explanation from me would only be a guess.
Ellis | I will make that stage clear. No [[technician assessment::Technician assessment has not occurred, so the concern must remain attributed to the customer.]] has taken place, and the cause is unknown. The record will not present your description as a workshop finding.
Mina | Please keep the overnight detail. That is the condition I have noticed, but I am not saying parking overnight is itself the cause.
Ellis | Agreed. Those are [[reported conditions::Reported conditions preserve the overnight-parking circumstance without treating it as proven causation.]], not an established explanation. I will not add a speed, journey length, or other circumstance that you have not supplied.
Mina | Thank you. I would rather give a clear account of what I have already heard than try to use technical words I am uncertain about.
Ellis | That helps us produce a useful [[job card::Job card is the workshop record that should preserve the precise customer concern for assessment.]]. Ordinary words such as rattle can carry important detail when the vehicle, location, and circumstances are accurately recorded.
Mina | Could you read the final wording back? I want to check that occasional has not become constant and that the other car is not included.
Ellis | Here is the [[concern readback::Concern readback checks the vehicle, intermittent sound, reported conditions, and unknown cause together.]]: customer reports an occasional rear rattle in the blue hatchback after overnight parking. Cause unknown; no technician assessment has occurred.
Mina | That matches my account. It says what I have noticed without naming a faulty part or claiming the technician has already confirmed anything.
Ellis | I will retain that [[customer concern::Customer concern remains the owner's account, distinct from a later diagnosis or vehicle-safety conclusion.]] for the workshop handoff. The next assessment can build on an accurate description instead of starting from an assumed cause.''',
    transfer_title='Read back the booked concern',
    transfer_setup='Complete the intake summary. Preserve the correct car, sound, location, and reported condition.',
    transfer='''Advisor: "The booked vehicle is the blue ___." | hatchback | Hatchback identifies the selected household car for today's booking.
Customer: "I report an occasional ___." | rattle | Rattle is the sound Mina described, not a diagnosis.
Advisor: "You hear it from the ___." | rear | Rear preserves the perceived location without naming a failed component.
Customer: "I have noticed it after ___ parking." | overnight | Overnight is the reported circumstance, not a proven cause of the noise.'''
))


BOOK['units'].append(unit(
    title='Clarifying the appointment and drop-off',
    scene='Eight is intake, ten is an update',
    skill='Correct an appointment misunderstanding with a specific communication promise while keeping workshop start and completion times unconfirmed.',
    brief='Customer Omar has booked an 08:00 drop-off and expects work to start immediately and finish by 09:00. The booking confirms intake only. Advisor Leila can offer a status update by 10:00, not a completion guarantee. Omar prefers a phone call. Leila must explain the distinction, acknowledge the timing expectation, and record the call preference. No technician start slot, repair duration, or collection time has been confirmed.',
    cast='Omar | Customer\nLeila | Service advisor',
    culture=('Replace a mistaken promise with a real one', 'A customer who hears appointment may imagine a dedicated work slot. Explain the actual booking without blaming the customer. A specific update time and preferred contact method create a useful commitment while leaving unconfirmed completion information honest.'),
    a='''What does 08:00 confirm? | Intake at drop-off | Technician work starting immediately | Vehicle completion | A confirmed one-hour repair | The booking confirms drop-off intake, not a workshop start or completion time.
What can Leila promise? | A status update by 10:00 | Completion by 09:00 | Immediate technician attention | A collection slot at 10:00 | The supplied commitment is an update deadline rather than a finished vehicle.
How does Omar prefer to receive the update? | By phone call | Only by email | Through an unconfirmed third party | By assuming silence means completion | The brief explicitly identifies a phone call as the preferred method.''',
    vocabulary='''drop-off | Delivery of a vehicle to the service location. | confirm the drop-off time
intake | Initial process of receiving the vehicle and recording the request. | distinguish intake from workshop work
appointment | Arranged time for the stated service interaction. | clarify what the appointment covers
workshop start | Point when the assigned technical work begins. | confirm the workshop start
technician slot | Scheduled period assigned to a technician for work. | verify the technician slot
completion time | Time when the defined work is expected or confirmed to finish. | distinguish completion time
collection time | Time agreed for the customer to receive the vehicle. | confirm the collection time
status update | Communication reporting the current position of the work. | provide a status update
update deadline | Latest time promised for further information. | meet the update deadline
phone preference | Customer choice to receive communication by telephone. | record the phone preference
contact method | Means used to communicate with the customer. | confirm the contact method
callback number | Number agreed for a return telephone call. | verify the callback number
booking terms | Stated conditions defining what an appointment includes. | clarify the booking terms
timing expectation | Customer understanding of when something will happen. | acknowledge the timing expectation
turnaround | Time between receiving work and returning the completed item. | avoid promising an unverified turnaround
work queue | Ordered or managed set of jobs awaiting attention. | distinguish the work queue
progress report | Account of how far the work has advanced. | give a progress report
estimated finish | Provisional prediction of completion time. | qualify the estimated finish
confirmed finish | Completion time explicitly established through the relevant process. | distinguish a confirmed finish
waiting appointment | Booking specifically arranged for a customer to wait under stated terms. | verify a waiting appointment
transport arrangement | Plan for the customer's travel while the vehicle is at the shop. | discuss a transport arrangement
availability window | Period when a person can be contacted or attend. | record the availability window
schedule clarification | Correction of an ambiguous or mistaken timing understanding. | give a schedule clarification
commitment readback | Repetition of agreed promises and their limits. | give a commitment readback''',
    precision='An 08:00 drop-off is not a confirmed 08:00 technician start. Nothing establishes completion by 09:00. Preserve the booked intake while correcting the unsupported assumptions about work and turnaround.',
    precision_extra='By 10:00 is an update deadline, not a vehicle-ready time. The promised contact is a phone call. Do not relabel the appointment as a waiting service or invent collection, transport, or workshop arrangements.',
    phrases='''Acknowledge the expectation | I understand that you expected the work to start at eight.
Clarify the booking | The 08:00 booking is for drop-off intake.
Separate the work slot | It does not confirm an 08:00 technician start.
Avoid a one-hour promise | Completion by 09:00 has not been confirmed.
Offer a real commitment | I can provide a status update by 10:00.
Name the communication | That is an update, not a finish guarantee.
Confirm the preference | You would prefer a phone call.
Record the method | I will keep phone as the contact method.
Keep collection separate | We still need actual confirmation before giving a collection time.
Avoid inventing a waiting booking | This record does not confirm a waiting appointment.
Use the deadline accurately | By ten means no later than ten for the update.
Preserve the intake time | Your drop-off booking remains at 08:00.
Avoid assuming transport | We have not agreed a separate transport arrangement here.
Give an honest limit | I cannot promise a work duration that has not been established.
Read back the commitments | Drop-off at eight; phone update by ten; finish time unconfirmed.
Close with clarity | I will keep those three points separate in the booking notes.''',
    notes='''For drop-off | Defines the event covered by the appointment.
Does not confirm | Limits the inference without canceling the actual booking.
By versus at | By gives a latest time; at identifies a particular time.
Update, not finish | Prevents a communication promise from becoming a completion guarantee.
Would prefer | Records the customer's chosen communication method.
Remains | Preserves the valid booking while correcting its misinterpretation.''',
    d='''Which statement best corrects Omar's expectation? | Eight is drop-off intake; start and finish are not confirmed | All eight o'clock bookings finish at nine | The update at ten guarantees collection at ten | Drop-off and technician start always mean the same thing | The correction explains the actual appointment while preserving uncertainty about workshop timing.
What does by 10:00 mean here? | The status call will be provided no later than 10:00 | The repair must finish exactly at 10:00 | The car can be collected before 10:00 | No update is needed until the next day | By establishes the latest promised communication time, not completion.
Which detail belongs in the contact notes? | Phone call preferred | Email only despite the request | No contact method needed | Customer can infer completion from silence | The notes should preserve the explicitly stated phone preference.
Which promise exceeds Leila's stated authority? | The car will definitely be ready by 09:00 | I can update you by 10:00 | The booking is for intake | I will note your phone preference | No completion guarantee is supplied, so a nine o'clock promise is unsupported.''',
    dialogue='''Omar | I booked an eight o'clock appointment. I expected you to start at eight and finish by nine, so I planned the rest of my morning around that.
Leila | I understand. I need to clarify that the booking is for [[drop-off::Drop-off identifies delivery of the vehicle, not an immediate start of technical work.]] at 08:00. It does not confirm an eight o'clock technician start or a nine o'clock finish.
Omar | When I heard appointment, I assumed someone would have a work slot reserved for my car at that exact time. What happens at eight?
Leila | Eight is the [[intake::Intake is the booked process of receiving the vehicle and recording the request.]] time for receiving the vehicle and the service request. The technical start and duration have not been confirmed in this booking.
Omar | Thank you for explaining. I would rather correct my plans now than arrive thinking I have a guaranteed one-hour turnaround.
Leila | That is important. We do not have a confirmed [[completion time::Completion time has not been established by the intake booking or the customer's expectation.]], so I should not repeat your nine o'clock expectation as though it were a promise from the workshop.
Omar | What can you commit to, then? I need a definite point at which I will hear from you, even if the work is not finished.
Leila | I can give you a [[status update::Status update is the communication Leila can promise, distinct from completed work.]] by 10:00. That will report the position at that stage; it is not a guarantee that the vehicle will be ready then.
Omar | A call would be best. I may not check email during the morning, and I do not want important information going through the wrong channel.
Leila | I will record that [[phone preference::Phone preference preserves Omar's explicit choice of a telephone call rather than email.]]. The promised update will be by phone, using the agreed contact details in your booking.
Omar | Does by ten mean the call could come earlier, but no later than ten? I want to make sure I understand the deadline correctly.
Leila | Yes. Ten is the [[update deadline::Update deadline is the latest promised time for the call, not an exact repair completion time.]], not a fixed completion appointment. Keeping those separate should make the booking notes and your expectations consistent.
Omar | I will keep the eight o'clock drop-off, then. I am not asking you to relabel this as a waiting appointment without an actual agreement.
Leila | Correct. A [[waiting appointment::Waiting appointment would need its own stated arrangement and cannot be inferred from this intake booking.]] is not confirmed here. We should not add that assumption merely because you initially hoped to stay for an hour.
Omar | Nor should I tell someone to meet me for collection at ten just because that is the update deadline. The call may not confirm completion.
Leila | Exactly. The [[collection time::Collection time needs actual readiness confirmation and is not established by the update deadline.]] remains unconfirmed. A communication promise helps you plan the next decision, but it does not itself establish that the vehicle can be handed back.
Omar | That is clear. Please keep my phone preference in the notes so the person handling the update does not assume an email will be enough.
Leila | I will keep the [[contact method::Contact method records how the promised update should reach Omar.]] alongside the deadline. The handoff should say phone update by 10:00, not simply contact customer when convenient.
Omar | Let me repeat the arrangement: I drop off at eight, you call by ten with status, and there is no confirmed start or finish time yet.
Leila | That [[commitment readback::Commitment readback preserves the actual intake and call promises without inventing workshop timing.]] is accurate. I will record it that way so the next colleague sees what is booked, what is promised, and what still needs confirmation.''',
    transfer_title='Confirm the appointment without a finish promise',
    transfer_setup='Complete the booking readback. Keep intake, communication, and completion distinct.',
    transfer='''Advisor: "Drop-off intake is booked for ___." | 08:00 | Eight o'clock belongs to intake rather than a confirmed technician start.
Customer: "I prefer a ___ call." | phone | Phone is the contact method explicitly requested by the customer.
Advisor: "The status update will be provided by ___." | 10:00 | Ten is the latest promised update time, not the completion deadline.
Customer: "The finish time remains ___." | unconfirmed | No workshop duration or completion time is established by the booking.'''
))


BOOK['units'].append(unit(
    title='Explaining estimates and approval limits',
    scene='Go ahead with the assessment only',
    skill='Resolve ambiguous approval by reading back the exact service, charge, and limit, then separate any later repair decision.',
    brief='A fictional shop offers an assessment for $95 under its stated booking terms. No repair is included. Customer Hana says go ahead, intending only the assessment, while advisor Dev needs to record the authorization accurately. Dev must read back the $95 assessment-only scope and route any later repair proposal for separate approval. No repair price, component replacement, or guaranteed diagnostic outcome is supplied. The terms belong to this fictional booking, not to every repair shop.',
    cast='Hana | Customer\nDev | Service advisor',
    culture=('Confirm the meaning of a short yes', 'A brief go ahead can conceal different assumptions about scope. Read back the service and charge in one sentence, then state what is not included. The aim is a shared record of the actual decision, not pressure to approve an unspecified repair.'),
    a='''What does the $95 cover in this booking? | Assessment only | Assessment plus any needed repair | A guaranteed replacement sensor | All future visits | The stated fictional terms cover assessment and explicitly exclude repair.
What does Hana intend by go ahead? | Permission for the assessment only | Approval of every later repair | Agreement to an unknown repair price | Acceptance of a guaranteed diagnosis | The customer intends the limited assessment described in the brief.
What must happen with a later repair proposal? | It needs separate approval | It is automatically covered by the initial yes | It can proceed without being described | It must be free regardless of scope | The supplied process requires a separate decision on any later repair proposal.''',
    vocabulary='''assessment fee | Charge for the defined evaluation service. | explain the assessment fee
diagnostic time | Time spent investigating a reported vehicle concern. | distinguish diagnostic time
assessment scope | Work included in the agreed evaluation. | confirm the assessment scope
repair scope | Defined corrective work proposed or authorized. | separate the repair scope
authorization | Permission for a specific action or service. | record the authorization
approval limit | Boundary of what the customer has agreed to. | preserve the approval limit
assessment only | Wording excluding repair from the current approval. | state assessment only
repair proposal | Description of suggested corrective work and its relevant terms. | present the repair proposal
separate approval | New permission for work outside the current authorization. | obtain separate approval
written estimate | Document describing expected cost for defined work. | review the written estimate
itemized quote | Price proposal separating relevant components of cost. | provide an itemized quote
parts charge | Cost associated with supplied components. | identify the parts charge
labor charge | Cost associated with the stated work time or labor provision. | distinguish the labor charge
scope readback | Repetition of the exact work covered by permission. | give a scope readback
stated terms | Conditions explicitly supplied for the booking or service. | follow the stated terms
cost commitment | Agreed financial obligation for defined work. | clarify the cost commitment
additional work | Work beyond the already authorized scope. | seek approval for additional work
component replacement | Removal and substitution of a particular vehicle part. | propose component replacement
diagnostic outcome | Result of the assessment, which may include unresolved questions. | avoid guaranteeing a diagnostic outcome
customer consent | Customer agreement to the identified work and terms. | confirm customer consent
approval record | Documentation of the permission actually given. | update the approval record
unpriced repair | Corrective work for which a price has not been supplied. | distinguish an unpriced repair
service inclusion | Item expressly covered in the described service. | confirm service inclusions
decision boundary | Limit between the present agreement and a later required decision. | explain the decision boundary''',
    precision='The fictional booking offers a $95 assessment, with no repair included. Hana intends to approve that service only. The phrase go ahead must not expand into permission for an undefined repair or component replacement.',
    precision_extra='Any later repair proposal requires separate approval under the supplied terms. The assessment fee does not establish a repair price or guarantee a particular diagnostic outcome. Keep the present cost and later decision separate.',
    phrases='''Name the present service | The $95 charge is for the assessment.
State the limit | No repair is included in that amount.
Clarify the short approval | By go ahead, do you mean the assessment only?
Read back the charge | You are authorizing the $95 assessment.
Preserve the scope | I will record assessment only.
Separate later work | Any later repair proposal will need separate approval.
Avoid an automatic extension | Your current yes does not authorize unspecified repairs.
Avoid a false inclusion | The assessment charge is not a repair package.
Keep the outcome open | We have not guaranteed a particular diagnostic result.
Keep the repair price open | No repair price has been supplied yet.
Ask for confirmation | Does that match the permission you intend to give?
Explain the next decision | We will explain any proposed repair before seeking its approval.
Keep components unapproved | No component replacement is authorized by this assessment approval.
Use the actual terms | These are the stated terms for this booking.
Record the agreement | The approval record will show the service, amount, and limit.
Close without pressure | The later repair decision remains separate from today's assessment.''',
    notes='''For the assessment | Attaches the price to one defined service.
Only | Restricts authorization rather than merely emphasizing the service name.
By go ahead, do you mean ...? | Checks the intended meaning of an ambiguous phrase.
Any later | Keeps a future proposal conditional rather than inevitable.
Not included | Identifies a scope boundary without inventing another price.
Separate from | Prevents present consent from silently authorizing later work.''',
    d='''Which readback is most accurate? | You authorize the $95 assessment only; repair needs separate approval | You approve assessment and all repairs | Ninety-five dollars guarantees a complete repair | Go ahead means we may replace any component | The readback includes the stated service, amount, and authorization boundary.
What should Dev avoid promising? | A particular diagnostic result or unpriced repair | The assessment charge stated in the booking | A clear approval record | A separate later repair decision | The brief supplies neither a guaranteed outcome nor a repair price.
What makes the original go ahead ambiguous? | It does not itself state the exact approved scope | It always means refusal | It is a technical vehicle identifier | It establishes every repair cost | A short approval phrase needs the agreed service and limit attached.
Which item belongs in the approval record? | Assessment only, $95, with repair excluded | A guessed replacement part | A promised free repair | Unlimited additional work | The record should preserve the permission actually given under the stated terms.''',
    dialogue='''Hana | I have seen the ninety-five-dollar assessment charge. Go ahead with that, please. I want to know what the concern is before deciding on any repair.
Dev | I will confirm the [[assessment scope::Assessment scope defines the evaluation Hana is approving, separate from corrective work.]] before I record your approval. The $95 is for assessment only under this booking, and no repair is included.
Hana | Yes, that is what I meant. I do not intend go ahead to mean replace parts or carry out whatever repair may later be suggested.
Dev | Then the [[approval limit::Approval limit preserves Hana's permission for assessment without extending it to unspecified repairs.]] is clear: the $95 assessment, not corrective work. I will read that back in the record rather than leave only the words go ahead.
Hana | Thank you. I have had conversations where the price and the service got separated, and it became unclear what my yes applied to.
Dev | We will keep the [[assessment fee::Assessment fee is the stated $95 charge for the defined evaluation service.]] attached to the service. It is not a repair allowance or a promise that a particular replacement is covered by that amount.
Hana | Does paying for the assessment guarantee that you will identify one specific failed part? I do not want the wording to promise a result that is uncertain.
Dev | No particular [[diagnostic outcome::Diagnostic outcome is not guaranteed by the stated assessment fee or authorization.]] is supplied in these terms. The assessment is the authorized service; we have not promised a particular cause or component finding before it occurs.
Hana | If the technician later recommends work, I want the proposed repair explained and priced before I make that next decision.
Dev | Any [[repair proposal::Repair proposal describes later corrective work and must be presented for a distinct customer decision.]] will be a separate matter. Your current assessment approval does not settle its scope, price, or whether you want it carried out.
Hana | That includes component replacement, even if the technician thinks it is likely to be needed? I do not want likelihood treated as my permission.
Dev | Correct. No [[component replacement::Component replacement is corrective work outside the present assessment-only authorization.]] is authorized by this assessment-only agreement. A possible recommendation is not the same as customer approval to do the work.
Hana | Please make the later approval requirement explicit in the notes. I may speak to a different advisor when the findings are available.
Dev | I will state that [[separate approval::Separate approval is required for any later repair outside the current assessment scope.]] is needed for any repair proposal. The next advisor should see the actual boundary rather than infer broader permission from a short yes.
Hana | Could you read back the exact permission I am giving now? I want the amount, the service, and the exclusion in the same statement.
Dev | Here is the [[scope readback::Scope readback repeats the service, price, and exclusion so Hana can confirm the actual agreement.]]: you authorize the $95 assessment only; no repair is included or approved. Any later repair proposal will be explained and routed for separate approval.
Hana | That matches my intention. I agree to the assessment on those stated terms, without approving an unpriced repair or asking for a guaranteed diagnosis.
Dev | I will preserve that [[customer consent::Customer consent applies to the specific assessment and stated terms, not to future unpriced work.]] in the booking record. It identifies what you have agreed to while keeping any later recommendation and decision distinct.
Hana | Good. I am comfortable proceeding with the assessment now that the scope is clear and the next repair decision remains mine to consider separately.
Dev | The [[approval record::Approval record documents the present limited permission so the workshop and later advisor receive the same instruction.]] will show exactly that: $95 assessment only, repair excluded, separate approval required later. That gives the workshop and the next advisor the same clear instruction.''',
    transfer_title='Read back the exact approval',
    transfer_setup='Complete the authorization record using the fictional booking terms. Do not add an unpriced repair.',
    transfer='''Advisor: "The authorized charge is ___ dollars." | 95 | Ninety-five dollars is the stated price of the assessment service.
Customer: "I approve the ___ only." | assessment | Assessment is the specific service Hana intends to authorize.
Advisor: "No ___ is included or approved." | repair | Repair falls outside the current assessment-only agreement and stated charge.
Customer: "Any later proposal needs ___ approval." | separate | Separate approval preserves a distinct decision for any later repair proposal.'''
))


BOOK['units'].append(unit(
    title='Handing the concern to the technician',
    scene='Job 208: keep the concern and contact limits together',
    skill='Deliver a concise internal handoff that preserves the symptom, assessment-only authorization, reproduction status, and customer contact window.',
    brief='Job card 208 records a customer-reported intermittent cabin rattle after overnight parking. The customer has approved assessment only, is unavailable from 12:00 to 14:00, and prefers a phone call after 14:00. Technician Arun has not reproduced the concern. Advisor Rosa hands over these facts without naming a cause, expanding authorization, or treating non-reproduction as proof that nothing is wrong. The agreed contact window must remain visible with the technical request.',
    cast='Rosa | Service advisor\nArun | Technician',
    culture=('Treat contact details as part of a technical handoff', 'A workshop handoff can fail even when the symptom is described accurately if the approval limit or customer availability is lost. Put the job identifier first, separate reported and observed information, then read back permission and contact constraints before ending the exchange.'),
    a='''Which job is being handed over? | Job card 208 | Job card 315 | An unidentified household account | A completed invoice only | The brief identifies 208 as the record for this internal handoff.
What is the authorization? | Assessment only | Unlimited repair | An approved replacement | Any work while the customer is unavailable | The customer has approved only assessment, not unspecified corrective work.
What contact arrangement is supplied? | Phone call after 14:00; unavailable 12:00-14:00 | Call during the unavailable period | Email only before noon | No need to contact the customer | The brief states both the unavailable interval and the preferred later phone contact.''',
    vocabulary='''internal handoff | Transfer of relevant information between colleagues. | give an internal handoff
job identifier | Number or code distinguishing a workshop record. | state the job identifier
cabin | Interior space used by vehicle occupants. | locate the cabin concern
intermittent rattle | Occasional repeated light knocking or vibrating sound. | retain the intermittent rattle description
customer-reported | Attributed to the customer's account rather than a technician finding. | label the concern customer-reported
reproduced concern | Reported condition observed again during relevant assessment. | record whether the concern was reproduced
not reproduced | Wording stating that the reported condition has not been observed during the assessment. | retain not-reproduced status
assessment authorization | Permission for the defined evaluation work. | confirm assessment authorization
repair authorization | Permission for specified corrective work. | distinguish repair authorization
contact window | Period when customer communication is appropriate under the stated arrangement. | preserve the contact window
unavailable interval | Period during which the customer cannot be reached as arranged. | record the unavailable interval
preferred channel | Communication method selected by the customer. | preserve the preferred channel
workshop handover | Exchange passing a job and its relevant context to the workshop. | complete the workshop handover
finding status | Current state of observed or established results. | clarify the finding status
diagnostic hypothesis | Possible explanation requiring relevant investigation. | distinguish a diagnostic hypothesis
confirmed cause | Explanation established by the relevant assessment. | avoid inventing a confirmed cause
noise concern | Customer report about an unwanted vehicle sound. | describe the noise concern
reported trigger | Circumstance the customer associates with the symptom. | preserve the reported trigger
concern history | Record of earlier descriptions or occurrences. | retain the concern history
contact note | Record of communication preferences or restrictions. | include the contact note
authorization boundary | Limit of work for which permission has been given. | state the authorization boundary
handoff readback | Repetition by the receiving person of the essential information. | request a handoff readback
non-reproduction | Absence of the reported symptom during the relevant assessment. | distinguish non-reproduction from resolution
next communication | Following planned exchange with the customer. | plan the next communication''',
    precision='Job 208 concerns a customer-reported cabin rattle after overnight parking. Arun has not reproduced it. Non-reproduction is a limited observation, not proof that the report was mistaken or that a cause has been found.',
    precision_extra='Assessment-only approval remains in force while the customer is unavailable from 12:00 to 14:00. That interval does not permit extra work. The preferred next contact is a phone call after 14:00, not an invented fixed appointment.',
    phrases='''Open with the identifier | This handoff is for job card 208.
State the customer's concern | The customer reports an intermittent cabin rattle.
Preserve the condition | They associate it with overnight parking.
State the assessment limit | You have not reproduced the concern.
Avoid dismissing the account | Not reproduced does not mean the report is false.
Keep cause open | No confirmed cause is supplied.
State the permission | The authorization is for assessment only.
Exclude assumed extra work | No repair authorization is recorded.
Give the unavailable interval | The customer is unavailable from 12:00 to 14:00.
Give the preferred contact | They prefer a phone call after 14:00.
Avoid an exact-time invention | After two is a window, not a confirmed call at exactly two.
Keep permission unchanged | Being unable to reach the customer does not expand the scope.
Keep the channel visible | Please retain phone as the preferred channel.
Request the receiver's check | Can you read back the concern, scope, and contact window?
Keep observations attributed | Separate the customer report from what you have observed.
Close with a complete handoff | Job 208, assessment only, concern not reproduced, phone after 14:00.''',
    notes='''Customer reports | Preserves attribution when the technician has not observed the concern.
Not reproduced | Describes an assessment limit without dismissing an intermittent report.
After versus at | Distinguishes a time window from an exact appointment.
Unavailable from ... to | States both endpoints of the contact restriction.
Does not expand | Keeps permission unchanged despite a communication difficulty.
Concern, scope, contact | Groups three different kinds of essential handoff information.''',
    d='''Which handoff preserves all critical facts? | Job 208: intermittent cabin rattle after overnight parking; assessment only; not reproduced; phone after 14:00 | Job 208: confirmed fault repaired; call at noon | Job 315: unlimited repairs; email whenever convenient | Job 208: no problem exists because no noise was heard | The full handoff retains identifier, concern, condition, permission, status, and contact arrangement.
What does not reproduced mean here? | Arun has not observed the reported concern during assessment | The customer invented the sound | The fault has been repaired | The cause is confirmed | Non-reproduction describes the technician's observation limit, not the truth of the customer's history.
When should the preferred phone contact occur? | After 14:00, outside the stated unavailable interval | Between 12:00 and 14:00 | Exactly 12:00 regardless of availability | Only by email before 14:00 | The supplied preference is a phone call after the unavailable interval ends.
What changes the approval limit during customer unavailability? | Nothing in these facts | The inability to contact them automatically permits repair | The job number authorizes replacement | Non-reproduction grants unlimited work | The assessment-only authorization remains unchanged by the customer's contact restriction.''',
    dialogue='''Rosa | Arun, this is the handoff for job card 208. I want the concern, permission, and contact details together before the next update goes to the customer.
Arun | I have the [[job identifier::Job identifier anchors the handoff to record 208 rather than another workshop job.]] as 208. Please give me the customer's wording first, so I do not replace it with a technical assumption.
Rosa | The customer reports an intermittent cabin rattle after the car has been parked overnight. That is their description, not a confirmed component diagnosis.
Arun | I will retain [[customer-reported::Customer-reported attributes the intermittent rattle to the owner's account rather than a verified technician finding.]] in the record. I have not reproduced the concern, so I cannot add a confirmed cause from my assessment.
Rosa | Thank you. Please do not let not reproduced become no problem exists in the summary. The occasional nature of the report needs to remain visible.
Arun | Agreed. [[Non-reproduction::Non-reproduction is a limited assessment result and does not prove the reported intermittent condition never occurs.]] describes what I have not observed during the assessment. It does not establish that the customer is mistaken or that the concern has been repaired.
Rosa | The permission is limited too. The customer approved assessment only, and there is no repair authorization for additional work on this job.
Arun | I will keep that [[authorization boundary::Authorization boundary limits the approved work to assessment rather than corrective action.]] explicit. Identifying a possible next step would not itself give me permission to carry out an unapproved repair.
Rosa | There is an important availability note: the customer is unavailable from noon to two, and prefers a phone call after two.
Arun | I have the [[unavailable interval::Unavailable interval is the stated 12:00-14:00 period that must remain in the contact notes.]] as 12:00-14:00. I will not suggest an update during that period or let the contact restriction disappear from the handoff.
Rosa | Good. After two is the preferred window, not a promised call at precisely two. Please preserve that wording when the job comes back to the desk.
Arun | Understood. The [[contact window::Contact window begins after 14:00 but is not an exact appointment at 14:00.]] is after 14:00, with no exact time supplied. I will not create a fixed appointment that nobody has agreed.
Rosa | The customer prefers a call rather than an email. That detail is easy to lose if the note only says contact customer later.
Arun | I will retain the [[preferred channel::Preferred channel is a telephone call, which must not be replaced with an assumed email update.]] as phone. The next advisor should see both when contact is appropriate and how the customer wants to receive it.
Rosa | Also, not being able to reach the customer during that interval must not become a reason to proceed beyond the assessment approval.
Arun | Correct. [[Repair authorization::Repair authorization is absent and is not created by difficulty contacting the customer.]] remains absent. The communication constraint does not expand the permitted work or turn an assumed remedy into an approved one.
Rosa | Please read back the complete handoff now, including what you have not reproduced. That will help me check the desk and workshop records agree.
Arun | Job 208: customer-reported intermittent cabin rattle after overnight parking; concern not reproduced; assessment only. Customer unavailable 12:00-14:00; phone preferred after 14:00. No [[confirmed cause::Confirmed cause has not been established, so it must not appear as an assumed diagnosis in the readback.]] is supplied.
Rosa | That matches the record. It preserves the customer's experience, your observation limit, the permission boundary, and the contact arrangement without adding a diagnosis.
Arun | I will carry that [[handoff readback::Handoff readback checks the complete transfer of technical and communication facts between colleagues.]] into the job notes. The next communication can use the same facts rather than reconstructing the customer's request from an incomplete summary.''',
    transfer_title='Pass on the concern, scope, and contact',
    transfer_setup='Complete the internal handoff. Keep the job identifier and contact window attached to the assessment-only scope.',
    transfer='''Advisor: "This is job card ___." | 208 | The handoff concerns record 208, not another service job.
Technician: "The approval covers ___ only." | assessment | Assessment is the stated authorization and does not include repair.
Advisor: "The customer is unavailable from 12:00 to ___." | 14:00 | Fourteen hundred is the end of the supplied unavailable interval.
Technician: "They prefer a ___ call afterward." | phone | Phone preserves the requested contact method after the unavailable period.'''
))


BOOK['units'].append(unit(
    title='Explaining parts and completion delays',
    scene='Tuesday arrival is not Tuesday collection',
    skill='Explain a parts delay by separating supplier estimates, shipment confirmation, workshop scheduling, and a firm update commitment.',
    brief='The part required for job 315 is on back order. The supplier estimates arrival on Tuesday, but shipment is not confirmed. Customer Ben wants to collect the vehicle on Tuesday. Technician scheduling and completion are also unconfirmed. Parts clerk Nia promises a supply-status update on Monday afternoon. She must acknowledge the requested pickup without accepting it, preserve the supplier estimate as provisional, and avoid treating part arrival as a completed repair.',
    cast='Ben | Customer\nNia | Parts clerk',
    culture=('Give the dependency chain in ordinary language', 'A customer may hear a part date as a vehicle-ready date. Separate supply, delivery, workshop work, and collection in a short sequence. Preserve the useful supplier estimate but label it honestly, then give a definite communication commitment that does not depend on a guessed result.'),
    a='''What is the part's current status? | On back order with shipment unconfirmed | Delivered and installed | Confirmed dispatched yesterday | Available for immediate collection with the vehicle | The part is back-ordered, and no shipment confirmation has been supplied.
What does Tuesday represent? | The supplier's estimated arrival | A guaranteed vehicle pickup | A confirmed technician completion | A completed installation date | Tuesday is a provisional supply estimate rather than a workshop or collection commitment.
What does Nia promise? | A supply-status update Monday afternoon | Vehicle ready Tuesday morning | A guaranteed Monday shipment | A free replacement vehicle | Nia commits to an update, not to a supply outcome or completed repair.''',
    vocabulary='''back order | Order for an item not currently available for immediate supply. | confirm back-order status
supplier estimate | Provisional timing or quantity information given by the supplier. | qualify the supplier estimate
estimated arrival | Expected delivery time not necessarily confirmed. | state the estimated arrival
shipment confirmation | Evidence that goods have been dispatched under the stated arrangement. | await shipment confirmation
dispatch | Sending goods from the supplier or distribution point. | distinguish dispatch from arrival
delivery | Transfer of goods to the destination. | confirm delivery
lead time | Time between an order stage and the relevant supply stage. | clarify the lead time
parts availability | Whether the required item can be supplied at the relevant time. | check parts availability
part allocation | Assignment of available stock to a particular order or job. | verify part allocation
order status | Current position of a purchase or supply request. | update the order status
supply-status update | Communication about progress or uncertainty in obtaining an item. | provide a supply-status update
workshop scheduling | Assignment of technical work to available time and staff. | confirm workshop scheduling
installation | Fitting the relevant component as part of authorized work. | distinguish installation from delivery
completion confirmation | Verified statement that the relevant work has finished. | obtain completion confirmation
pickup request | Customer preference for collecting the vehicle at a stated time. | record the pickup request
collection commitment | Agreed promise about when the vehicle can be handed over. | distinguish a collection commitment
dependency | Prior condition on which a later stage relies. | explain the dependency
provisional date | Date subject to confirmation or change. | retain the provisional date
confirmed date | Date established through the relevant process. | distinguish a confirmed date
parts clerk | Staff member coordinating component identification and supply. | contact the parts clerk
delay notice | Communication explaining a change or uncertainty in timing. | give a delay notice
supplier follow-up | Further contact to clarify supply information. | arrange supplier follow-up
progress checkpoint | Agreed point for reviewing and communicating status. | set a progress checkpoint
uncertain completion | Finish status or timing that has not been established. | explain uncertain completion''',
    precision='Tuesday is the supplier estimate for part arrival. Shipment is unconfirmed, and the part is on back order. Keep the estimate provisional rather than changing it to a guaranteed delivery or a booked collection.',
    precision_extra='Even part arrival would not by itself confirm technician scheduling, installation, or completion. Nia promises a Monday-afternoon supply update. Ben requests Tuesday pickup, but that request has not been accepted as a commitment.',
    phrases='''State the current supply position | The part for job 315 is on back order.
Attribute the date | The supplier estimates arrival on Tuesday.
Preserve uncertainty | Shipment has not been confirmed.
Separate dispatch and arrival | A dispatch confirmation would not itself mean the part has arrived.
Acknowledge the request | I understand that you would like Tuesday pickup.
Avoid accepting the date | I cannot confirm Tuesday collection from the current information.
Name the next dependency | Technician scheduling still needs confirmation.
Keep completion separate | Part arrival is not the same as completed work.
Give the firm update | I will update you on supply status Monday afternoon.
Limit the promise | That is a communication commitment, not a guaranteed supply result.
Avoid inventing allocation | We have no confirmed allocation or shipment to report here.
Retain the job reference | Please keep job 315 attached to this parts update.
Distinguish expected and confirmed | Tuesday remains estimated, not confirmed.
Avoid a guaranteed turnaround | The completion time is still unconfirmed.
Read back the chain | Back order, estimated Tuesday arrival, shipment and completion unconfirmed.
Close with the next contact | You will hear from me Monday afternoon about the supply position.''',
    notes='''Supplier estimates | Attributes a provisional date to its actual source.
Would like | Records a customer preference without accepting it as agreed.
Not the same as | Separates supply stages from workshop completion.
Still needs confirmation | Keeps a remaining dependency visible.
Will update | Commits to communication rather than the hoped-for outcome.
Estimated, not confirmed | Preserves the level of certainty attached to the date.''',
    d='''Which statement preserves the supplier information? | Arrival is estimated for Tuesday, with shipment unconfirmed | The part will definitely arrive Tuesday | The part has already been dispatched | Tuesday collection is booked | The estimate is provisional and does not establish shipment or collection.
Why can Nia not promise Tuesday pickup? | Supply, technician scheduling, and completion are not confirmed | The customer has not asked for pickup | Monday afternoon is a repair deadline | Every back order always takes a month | The necessary supply and workshop stages remain unresolved in the brief.
What should Nia promise in this case? | A supply-status update Monday afternoon | Guaranteed installation Tuesday morning | Confirmed shipment Monday morning | A fixed completed-repair outcome | The supplied commitment is a status update at the stated time.
What does Ben's request establish? | His preferred collection date, not an accepted promise | A guaranteed workshop slot | Confirmation that the part is allocated | A completed repair | A requested pickup date must remain distinct from a confirmed collection commitment.''',
    dialogue='''Ben | I am calling about job 315. I heard Tuesday mentioned for the part, and I would like to collect the car on Tuesday if that is the plan.
Nia | The part is on [[back order::Back order is the current supply status; the part is not confirmed as immediately available.]]. The supplier has estimated Tuesday arrival, but shipment is not confirmed, so I cannot describe Tuesday collection as an agreed plan.
Ben | I had understood Tuesday as a firm date rather than an estimate. Has the supplier actually sent the part, or are we still waiting for that confirmation?
Nia | We are still waiting for [[shipment confirmation::Shipment confirmation is absent, so an actual dispatch must not be implied.]]. I should keep the supplier estimate separate from evidence of dispatch rather than let the date sound more definite than it is.
Ben | Thank you. If the part does arrive on Tuesday, does that automatically mean the technician can fit it and finish the vehicle the same day?
Nia | No. [[Workshop scheduling::Workshop scheduling remains unconfirmed and is a separate stage from the supplier's estimated arrival.]] is not confirmed either. Part arrival, the work slot, and completion are distinct stages; the supply estimate does not establish all of them.
Ben | I need the car, but I do not want you to promise a collection time that depends on several things nobody has confirmed yet.
Nia | I understand your [[pickup request::Pickup request records Ben's preference for Tuesday without making it an accepted collection commitment.]] for Tuesday. I will keep it in the notes as your preference, not as a confirmed handover date.
Ben | What definite contact can you offer before then? I would like an update that tells me whether the supply position has changed.
Nia | I will provide a [[supply-status update::Supply-status update is the Monday-afternoon communication Nia actually promises.]] on Monday afternoon. That is my commitment to contact you, even though I cannot promise what the supplier's answer will be.
Ben | So Monday afternoon is not a guarantee that the part will ship by then. It is the point at which you will tell me the current position.
Nia | Exactly. It is a [[progress checkpoint::Progress checkpoint identifies an agreed communication point, not a shipment or completion guarantee.]], not a guaranteed dispatch or arrival. The update should distinguish what is confirmed from what remains estimated at that time.
Ben | I appreciate that. I had almost arranged a Tuesday lift to the shop based only on the part date, which would have been premature.
Nia | A [[collection commitment::Collection commitment requires actual readiness arrangements and is not established by a supplier estimate.]] needs the relevant completion and handover confirmation. We do not yet have that, and I would not want your travel plans built on an unsupported promise.
Ben | Please keep the job number in the update as well. We have had more than one conversation with the shop, and I want the information traceable.
Nia | Certainly. Job 315 will stay attached to the [[order status::Order status records the supply position for the specific job rather than a general parts conversation.]] information. The note will identify the back order, the supplier's Tuesday estimate, and the missing shipment confirmation.
Ben | Can you give me a short version I can explain at home? I want to avoid repeating Tuesday as though the vehicle is definitely ready then.
Nia | The [[estimated arrival::Estimated arrival is the supplier's provisional Tuesday date, not a confirmed delivery or finished vehicle.]] is Tuesday; shipment is unconfirmed. Technician scheduling and completion are also unconfirmed. I will update you about supply on Monday afternoon.
Ben | That is clear. Tuesday remains a preference for pickup, not a booking, and I will wait for actual readiness information before treating collection as settled.
Nia | Correct. We will keep [[completion confirmation::Completion confirmation is the later verified status needed before a collection promise can be made.]] separate from the parts forecast. You have a definite next update, but no invented guarantee about delivery, installation, or pickup.''',
    transfer_title='Separate the supply forecast from collection',
    transfer_setup="Complete the delay update using the actual supplier estimate and Nia's communication commitment.",
    transfer='''Clerk: "The part is on back ___." | order | Back order is the current supply status for the required part.
Customer: "The supplier estimates arrival on ___." | Tuesday | Tuesday is an estimated arrival date, not a confirmed collection appointment.
Clerk: "Shipment has not been ___." | confirmed | Shipment remains unverified despite the supplier's estimated arrival date.
Customer: "The supply update is promised Monday ___." | afternoon | Monday afternoon is the stated communication commitment rather than a guaranteed delivery.'''
))


BOOK['units'].append(unit(
    title='Relaying findings and technical terms',
    scene='A code is a clue, not a replacement order',
    skill='Translate a diagnostic note into accurate customer language while separating recorded information, confirmed cause, and authorized work.',
    brief="Technician Jules has recorded a diagnostic trouble code, abbreviated DTC, on job 416. The note gives no confirmed cause or component fault. Customer Tomas assumes the code proves that a sensor needs replacement. Advisor Ava must explain the limited finding and request a clearer technician explanation. No replacement is approved. Ava has no additional test results and must not invent them or tell Tomas how to diagnose the vehicle.",
    cast='Tomas | Customer\nAva | Service advisor',
    culture=('Explain the technical noun and its evidential limit', 'Using the full term once helps a customer follow the conversation. The more important distinction is what the information establishes. Explain what is recorded, what has not been confirmed, and whose clarification is needed before discussing a replacement decision.'),
    a='''What does the note record? | A diagnostic trouble code | A confirmed sensor failure | A completed replacement | A guarantee of vehicle readiness | The technician note records a code without confirming the cause or component fault.
What has Tomas assumed? | The sensor must need replacement | The advisor has no job number | The invoice has already been paid | No code was recorded | Tomas has treated the code as proof of a specific replacement need.
What should Ava request next? | A clearer technician explanation | Automatic sensor replacement | An invented test result | A promise that the code is harmless | The missing explanation must come from the technician rather than the advisor's guess.''',
    vocabulary='''diagnostic trouble code | Coded diagnostic information; abbreviated DTC. | record a diagnostic trouble code
on-board diagnostics | Vehicle monitoring and reporting systems; abbreviated OBD. | refer to on-board diagnostics
scan tool | Device for accessing supported diagnostic information. | identify the scan-tool record
control module | Electronic unit managing specified vehicle functions. | identify the control module
sensor | Component detecting a condition and supplying a signal. | distinguish a sensor from its circuit
actuator | Component carrying out a commanded physical action. | identify the actuator
circuit | Connected electrical path for a function. | identify the relevant circuit
malfunction indicator lamp | Dashboard warning indicator; abbreviated MIL. | report an illuminated lamp
stored code | Code retained in diagnostic memory. | identify a stored code
pending code | Provisional code status, not a repair diagnosis. | distinguish a pending code
freeze-frame data | Snapshot of operating information for a recorded event. | interpret freeze-frame data
live data | Supported information displayed as conditions are read. | distinguish live data
assessment note | Technician record of the examination and available findings. | read the assessment note
confirmed cause | Explanation supported by the completed relevant assessment. | distinguish a confirmed cause
component fault | Established problem attributed to a particular part. | avoid inventing a component fault
diagnostic evidence | Information relevant to investigating a reported problem. | explain the diagnostic evidence
fault tracing | Investigation intended to locate the source of a problem. | distinguish fault tracing from code reading
replacement decision | Conclusion that a particular item should be replaced. | support a replacement decision
technician clarification | Further explanation supplied by the relevant technician. | request technician clarification
finding | Information established or recorded during an assessment. | relay the limited finding
interpretation | Explanation of what information means in context. | separate a record from its interpretation
repair authorization | Customer permission for a specified repair under the stated terms. | obtain repair authorization
unsupported inference | Conclusion not established by the available information. | correct an unsupported inference
plain-language explanation | Account using accessible words without changing the technical meaning. | provide a plain-language explanation''',
    precision='DTC expands to diagnostic trouble code. It does not expand to a repair instruction. Job 416 contains a code, but the note does not identify a confirmed cause or component fault. Do not invent a code number or sensor type.',
    precision_extra='Ava can relay the recorded finding and request clarification. The vocabulary introduces common diagnostic terms without claiming they all appear in this job. No replacement has been approved, and the conversation does not establish vehicle safety or readiness.',
    phrases='''Expand the abbreviation | DTC stands for diagnostic trouble code.
Identify the source | I am reading the technician note for job 416.
State the finding | The note records a code.
Explain the limit | It does not confirm the cause.
Separate the component | It does not establish that this sensor has failed.
Correct the inference | A code is not automatically a replacement instruction.
Avoid invented detail | I do not have a specific test result to quote.
Preserve the uncertainty | The cause remains unconfirmed in this note.
Identify the missing explanation | We need the technician to explain what the finding supports.
Request clarification | Could you clarify whether a component fault has been established?
Use accessible language | The system recorded information that needs interpretation.
Distinguish authorization | No replacement has been approved.
Avoid a safety conclusion | This note does not give me a vehicle-readiness confirmation.
Check the understanding | Are we agreed that the code alone does not settle the repair?
State the next action | I will request a clearer explanation from Jules.
Close the handoff | I will keep the recorded code separate from any later repair proposal.''',
    notes='''Stands for | Introduces the full form of an abbreviation.
Does not establish | Limits a conclusion without denying that information was recorded.
Automatically | Identifies the mistaken leap from code to replacement.
In this note | Defines the information available to the speaker.
Has been approved | Refers to authorization, not simply a proposed action.
What the finding supports | Requests an evidence-based explanation rather than a more confident guess.''',
    d='''Which explanation is accurate? | A code is recorded, but the cause is not confirmed | The sensor has definitely failed | The code proves the vehicle is ready | No further explanation is needed | The available note records information without establishing a confirmed cause.
Which abbreviation is correctly expanded? | DTC: diagnostic trouble code | DTC: direct technician clearance | DTC: delivery timing confirmation | DTC: defective transmission component | Diagnostic trouble code is the stated full term for DTC.
Which sentence invents evidence? | Jules tested the sensor and proved it faulty | The note contains a code | No replacement is approved | We need Jules to clarify the finding | No sensor-test result or confirmed component fault appears in the supplied facts.
Which handoff respects the approval limit? | Request clarification before any separate repair proposal | Replace the sensor because Tomas mentioned it | Treat a recorded code as permission | Promise a free replacement today | Clarification is needed, and no replacement authorization has been given.''',
    dialogue='''Tomas | I saw the code on the note you sent. Does that mean the sensor is bad and you are ordering a new one?
Ava | I can explain what the note says. It records a [[diagnostic trouble code::Diagnostic trouble code is the recorded information, not proof that a particular sensor needs replacement.]], often shortened to DTC. It does not confirm a cause.
Tomas | I thought those codes told you exactly which part to replace. Otherwise, why would the system identify something connected with a sensor?
Ava | The information can help an investigation, but it is not automatically a [[replacement decision::Replacement decision requires support beyond treating the recorded code as a parts-order instruction.]]. I should not turn that entry into a repair instruction.
Tomas | Has Jules actually tested the sensor? Perhaps there is another result that was left out of the message I received.
Ava | I do not have that result. The [[assessment note::Assessment note is the available technician record, which contains no supplied sensor-test result.]] for job 416 records the code without a confirmed cause or component fault. I cannot add a test that is not recorded.
Tomas | Fair enough. But I need something clearer than a string of letters. What should I understand from the information you do have?
Ava | The [[finding::Finding here is limited to the recorded code, not a completed diagnosis or readiness conclusion.]] is that diagnostic information was recorded. What caused it, and whether a particular part needs replacement, are not established in this note.
Tomas | So it might mention a system or a circuit without proving the sensor itself is defective. Is that the distinction you are making?
Ava | Yes. We need to distinguish the information from a confirmed [[component fault::Component fault would attribute an established problem to a particular part, which this note does not do.]]. I am not diagnosing an alternative cause; I am explaining the limit of what is recorded.
Tomas | Please ask Jules to explain that limit directly. I would rather have a useful explanation than an immediate answer that turns out to be wrong.
Ava | I will request [[technician clarification::Technician clarification asks Jules to explain the available evidence rather than having Ava supply a guess.]]. The question will be what the code and assessment establish, and what remains unconfirmed before any repair proposal.
Tomas | I also want to be clear that asking about the sensor was not permission to replace it. I was trying to understand the note.
Ava | Understood. There is no [[repair authorization::Repair authorization has not been given merely because Tomas asked whether a sensor needs replacement.]] for a replacement. Your question will remain a request for explanation, not an instruction to order or fit a part.
Tomas | And you are not telling me the vehicle is ready just because you have read the code. I have not heard that confirmation either.
Ava | Correct. A [[plain-language explanation::Plain-language explanation makes the note understandable without adding a vehicle-readiness or safety claim.]] must not add a readiness claim. I have no such confirmation to give from the information we are discussing.
Tomas | All right. Could your message to Jules include my original misunderstanding? That might help the explanation address the question I actually have.
Ava | Certainly. I will say the customer understood the code as proof of sensor failure. That is an [[unsupported inference::Unsupported inference identifies the leap from a code to proven sensor failure without dismissing the customer's question.]] we need to correct with a clear account of the evidence.
Tomas | Then we are agreed: code recorded, cause not confirmed, no replacement approved. The next step is a more useful explanation from Jules.
Ava | Exactly. I will request the missing [[interpretation::Interpretation explains the significance and limits of the information without inventing a diagnosis or approval.]] and keep it connected to job 416. Any later repair proposal must remain separate from this clarification.''',
    transfer_title='Relay the finding without upgrading it',
    transfer_setup='Complete the advisor readback. Use the recorded evidence and approval status only.',
    transfer='''Advisor: "DTC means diagnostic trouble ___." | code | Code completes the correct full form of the diagnostic abbreviation.
Customer: "The cause has not been ___." | confirmed | Confirmed is the missing evidential status in the technician note.
Advisor: "I will request technician ___." | clarification | Clarification is the next action needed to explain the limited finding.
Customer: "No replacement has been ___." | approved | Approved distinguishes permission from a customer question about the sensor.'''
))


BOOK['units'].append(unit(
    title='Clarifying the invoice and collection handoff',
    scene='The bill is ready; the vehicle status is not',
    skill='Explain a two-line invoice accurately and separate a financial document from verified collection readiness.',
    brief='The fictional invoice for job 527 totals $180: $70 for parts and $110 for labor. Customer Imani thinks the labor line includes another $70 parts charge. Advisor Leo must explain that the two listed charges add to $180, not $250. The service desk has not yet confirmed vehicle readiness. Issuing an invoice does not itself confirm collection. No additional fees, taxes, payment status, or release arrangements are supplied.',
    cast='Imani | Customer\nLeo | Service advisor',
    culture=('Explain the arithmetic before defending the bill', 'A customer can question a charge without accusing anyone of dishonesty. Identify the two lines and show how they form the stated total. Then address collection separately, so a successful billing explanation does not become an accidental readiness promise.'),
    a='''What is the stated invoice total? | $180 | $250 | $110 | $70 | The supplied invoice contains $70 parts plus $110 labor, totaling $180.
What has Imani misunderstood? | She thinks another $70 parts charge is included in labor | She thinks all parts are free | She has received a confirmed collection time | She has been given a new tax rate | Her concern is an apparent extra parts charge within the labor line.
What remains unconfirmed? | Vehicle readiness | The two listed amounts | The invoice total | The job number | The service desk has not yet supplied vehicle-readiness confirmation.''',
    vocabulary='''invoice | Document listing charges for supplied work or items. | explain the invoice
line item | Separately listed entry on a bill or estimate. | identify each line item
parts charge | Amount billed for the listed vehicle components or materials. | distinguish the parts charge
labor charge | Amount billed for the stated work rather than the parts. | explain the labor charge
invoice total | Combined amount shown as payable on the invoice. | confirm the invoice total
duplicate charge | Amount billed again for the same chargeable item. | investigate a suspected duplicate charge
itemized bill | Bill that separates charges into identifiable entries. | read the itemized bill
billing query | Customer request for clarification about a charge. | resolve a billing query
arithmetic | Calculation of the amounts involved. | check the arithmetic
subtotal | Amount before any separately applicable later additions or deductions. | distinguish a subtotal from the stated total
tax line | Separate entry identifying an applicable tax charge. | avoid inventing a tax line
discount | Reduction from an otherwise stated price. | identify an authorized discount
credit adjustment | Recorded reduction or correction applied to an account. | distinguish a credit adjustment
balance due | Amount still payable after relevant recorded payments or credits. | verify the balance due
payment status | Record of whether and how an amount has been paid. | check payment status
receipt | Record acknowledging a payment or transaction. | distinguish a receipt from an unpaid invoice
invoice date | Date assigned to the issued billing document. | verify the invoice date
job reference | Identifier linking the bill and service record. | match the job reference
collection readiness | Confirmed status for the relevant vehicle handover arrangements. | verify collection readiness
service desk | Team or location coordinating service information and handover. | check with the service desk
handover confirmation | Verified information that the agreed transfer can proceed. | obtain handover confirmation
release arrangements | Agreed details governing the transfer of the vehicle. | confirm release arrangements
billing record | Account of charges and related financial entries. | correct the billing record
readiness check | Request to verify the vehicle's current handover status. | request a readiness check''',
    precision='The arithmetic is $70 + $110 = $180. The labor line is not $110 plus an additional $70 parts charge. The supplied invoice has no third charge. Explain the stated figures without introducing a tax rate, discount, or payment.',
    precision_extra='An invoice and a readiness confirmation serve different purposes. The invoice explains charges; the service desk must confirm collection status. Do not infer that the customer has paid, the vehicle is ready, or a particular release requirement has been met.',
    phrases='''Invite the query | Which line would you like me to explain?
Identify the reference | We are looking at job 527.
Separate the entries | There are two listed charges.
Name the first amount | The parts charge is $70.
Name the second amount | The labor charge is $110.
State the calculation | Seventy plus one hundred ten equals one hundred eighty.
Correct the duplicate assumption | There is no additional $70 parts charge in that labor line.
Acknowledge the confusion | I can see why the layout prompted that question.
Keep to the supplied bill | I will not add a charge that is not listed.
Avoid assuming payment | The invoice alone does not establish payment status.
Separate documents | A bill and a receipt are not the same record.
Switch to collection | Let us check readiness separately from the invoice.
State the missing status | The service desk has not confirmed readiness yet.
Avoid a false invitation | I cannot ask you to collect on the basis of this document alone.
Request the handoff check | Please confirm the collection position for job 527.
Close accurately | The invoice total is clear; collection remains unconfirmed.''',
    notes='''Plus versus included in | Distinguishes adding two lines from imagining another charge inside one line.
There are two | Limits the explanation to the supplied invoice entries.
Prompted that question | Acknowledges confusion without accepting an incorrect calculation.
Alone | Identifies the limit of what a single document establishes.
Yet | States the current absence of confirmation without promising when it will arrive.
Separately from | Keeps financial clarification and collection status distinct.''',
    d='''Which explanation resolves the billing query? | $70 parts plus $110 labor gives the $180 total | $70 parts must be added twice | Labor is another name for parts | The total is $250 before an invented discount | The supplied bill contains two charges whose sum is exactly $180.
Which statement wrongly infers readiness? | The invoice exists, so come and collect now | The desk has not confirmed readiness | We should check collection separately | The bill identifies the charges | Invoice creation does not establish the vehicle's collection status.
What can Leo say about payment? | The supplied facts do not establish payment status | The full amount has definitely been paid | A receipt proves an unpaid balance | The customer owes an invented late fee | No payment or receipt information is included in the supplied facts.
Which request should Leo send? | Confirm collection status for job 527 | Add another $70 to labor | Issue a driving-safety guarantee | Tell the customer the car is ready without checking | The service desk must verify readiness independently of the invoice explanation.''',
    dialogue='''Imani | I have the invoice in front of me. There is seventy for parts and one hundred ten for labor. Does labor include another seventy for the parts?
Leo | No. There are two separate entries on this [[itemized bill::Itemized bill separates the parts and labor entries so their amounts can be explained individually.]]. The parts charge is seventy dollars and the labor charge is one hundred ten dollars.
Imani | Then I should not add seventy again after those two figures? I was getting two hundred fifty, which is why I called.
Leo | Correct. The [[invoice total::Invoice total is $180 because the two stated charges are $70 and $110.]] is one hundred eighty dollars: seventy plus one hundred ten. There is no extra seventy-dollar parts charge inside the labor line.
Imani | That makes more sense. I was reading the two descriptions as though the second one repeated the first charge and then added the work.
Leo | I understand the [[billing query::Billing query names Imani's request to understand the apparent extra charge without assuming an accusation.]]. The layout led you to ask whether parts were being charged twice. Here, the two lines represent parts and labor separately.
Imani | Could you repeat them once more, slowly? I am making a note next to the invoice so I can explain it to my partner.
Leo | Certainly. The [[parts charge::Parts charge is the $70 entry, distinct from the $110 labor entry.]] is seventy dollars. Labor is one hundred ten dollars. Those two figures produce the stated total of one hundred eighty dollars.
Imani | Thank you. Now that the invoice has been issued, should I come down and collect the vehicle? I could arrange a lift this afternoon.
Leo | Please let me check [[collection readiness::Collection readiness has not been confirmed merely because the invoice was issued.]] separately. The service desk has not confirmed it yet, so I should not invite you to collect on the strength of the invoice.
Imani | I assumed a finished bill meant a finished car. Are you saying the billing document and the collection message are separate things?
Leo | Yes. The [[billing record::Billing record explains the charges but is not the missing vehicle-handover confirmation.]] tells us about the charges. It does not, by itself, give the missing handover confirmation or settle when you should travel here.
Imani | All right. I do not want to arrive before that has been checked. Does the invoice at least show that payment has gone through?
Leo | We have not established [[payment status::Payment status is not supplied, so Leo must not infer that the invoice has been paid.]] in this conversation. An invoice is not automatically a receipt, and I will not say a payment has been made without the relevant record.
Imani | That is useful. There are several different questions here: what the charges mean, whether payment is recorded, and whether collection can happen.
Leo | Exactly. We have clarified the arithmetic. The next [[readiness check::Readiness check asks the service desk to verify the unresolved collection position.]] should go to the service desk for job 527, without treating the bill as proof of readiness.
Imani | Please keep that job number in the request. I would rather wait for the correct answer than have the desk check a different vehicle.
Leo | I will match the [[job reference::Job reference connects the collection inquiry and billing conversation to the same service job.]] before requesting confirmation. The figures we discussed remain seventy for parts and one hundred ten for labor, totaling one hundred eighty.
Imani | Good. The extra seventy was my misunderstanding, not another listed charge. I will not take the invoice as an invitation to collect.
Leo | Understood. We still need [[handover confirmation::Handover confirmation is the missing readiness information needed before collection arrangements are treated as settled.]]. I will keep the billing explanation and the collection inquiry clear, so resolving one does not accidentally promise the other.''',
    transfer_title='Explain the bill and preserve the handoff limit',
    transfer_setup='Complete the customer-service exchange using the two charges and the unresolved collection status.',
    transfer='''Advisor: "The parts charge is ___ dollars." | seventy | Seventy is the supplied parts entry, not an additional charge within labor.
Customer: "The labor charge is one hundred ___ dollars." | ten | Ten completes the stated labor amount of one hundred ten dollars.
Advisor: "The two charges total one hundred ___ dollars." | eighty | Eighty completes the correct sum of seventy and one hundred ten dollars.
Customer: "Collection readiness is still ___." | unconfirmed | Unconfirmed preserves the missing service-desk status despite the issued invoice.'''
))

BOOK['units'].append(unit(
    title='Handling a repeat concern and follow-up',
    scene='Correct the dismissal before arranging the callback',
    skill='Acknowledge a repeat report, correct an unsupported dismissal, and arrange a specific review without promising a diagnosis or coverage.',
    brief='Two days after service, customer Farah reports the same intermittent rattle. Advisor Daniel initially said, "That cannot be the same issue." The cause and warranty coverage are unknown. Service lead Nia can call at 15:00 to review the report and next arrangements. Daniel must withdraw the unsupported statement, record what Farah reports, and explain the purpose of the callback. The call is not a repair appointment or a promise of free work.',
    cast='Farah | Customer\nDaniel | Service advisor',
    culture=('Correct your own statement explicitly', 'A calm apology is stronger when it identifies what was wrong. Withdraw the unsupported dismissal without swinging to an equally unsupported promise. Preserve the customer report, distinguish it from a confirmed cause, and make the next contact useful and specific.'),
    a='''What does Farah report? | The same intermittent rattle two days after service | A confirmed new component fault | A written warranty decision | A continuous noise proven unrelated to service | The brief gives a repeat customer report, not a technical conclusion about its cause.
What should Daniel correct? | His claim that it cannot be the same issue | The supplied callback time | Farah's right to describe the sound | An established technician diagnosis | The initial dismissal was unsupported because the cause remains unknown.
What can Nia do at 15:00? | Call to review the report and next arrangements | Complete a guaranteed free repair | Confirm coverage without review | Receive the vehicle at an already booked repair slot | The stated commitment is a review call rather than a repair or coverage guarantee.''',
    vocabulary='''repeat concern | Problem reported again after an earlier visit or intervention. | acknowledge a repeat concern
return complaint | Customer report that brings an unresolved or recurring concern back to the business. | record the return complaint
service history | Record of previous vehicle visits and relevant work. | review the service history
repair record | Account of the specified work performed during a service visit. | consult the repair record
reported recurrence | Customer account that a symptom has happened again. | preserve the reported recurrence
intermittent symptom | Experienced condition that occurs at intervals. | describe an intermittent symptom
same symptom | Similar experienced behavior or sound, without proving the same cause. | distinguish the same symptom from the same cause
underlying cause | Explanation responsible for the reported condition. | avoid assuming the underlying cause
unsupported dismissal | Rejection of a report without adequate evidence. | withdraw an unsupported dismissal
acknowledgment | Clear recognition that the report has been heard and recorded. | give a specific acknowledgment
apology | Statement accepting responsibility for an inappropriate response. | make a direct apology
correction | Explicit replacement of an inaccurate statement. | put the correction on record
service lead | Person responsible for coordinating the relevant service review. | refer the report to the service lead
callback | Return telephone contact arranged for a stated purpose. | confirm the callback
review appointment | Arranged discussion or assessment, defined by its actual scope. | clarify the review appointment
next arrangements | Further practical steps to be agreed after the review. | discuss next arrangements
warranty coverage | Protection that depends on the applicable terms and relevant facts. | check warranty coverage
service contract | Separate agreement describing specified services or protection. | distinguish a service contract from a warranty
coverage determination | Decision about whether stated protection applies. | avoid promising a coverage determination
goodwill offer | Discretionary concession made by a business. | avoid inventing a goodwill offer
no-charge work | Work supplied without a stated customer charge. | distinguish no-charge work from a review call
follow-up record | Account of contacts and steps after the original service. | update the follow-up record
complaint ownership | Responsibility for handling the stated concern or communication. | clarify complaint ownership
communication repair | Correction of a mishandled exchange through acknowledgment and accurate follow-up. | begin communication repair''',
    precision='Farah reports the same rattle, not a proven identical cause. Daniel should correct his statement that the issue cannot be the same. He should not replace that dismissal with a claim that the earlier repair definitely failed.',
    precision_extra='Nia can call at 15:00 to review the report and next arrangements. That is not an appointment for a completed repair. Warranty coverage and cause remain unknown, and Daniel has no authority in the supplied facts to promise no-charge work.',
    phrases='''Acknowledge the return | You are reporting the same intermittent rattle.
Preserve the timing | You noticed it again two days after service.
Own the earlier wording | I said it could not be the same issue.
Withdraw the claim | I should not have made that statement.
Apologize directly | I am sorry I dismissed your report.
State the uncertainty | We have not established the cause.
Keep symptoms and causes separate | A similar sound does not by itself prove an identical cause.
Avoid reversing into certainty | I cannot say the previous work definitely failed either.
Preserve the history | I will keep this report with the earlier service record.
Name the contact | Nia is the service lead handling the review call.
Specify the time | Nia can call at 15:00.
Explain the purpose | The call is to review your report and next arrangements.
Limit the commitment | This is not a confirmed repair appointment.
Keep coverage open | Warranty coverage has not been determined.
Avoid an unauthorized concession | I cannot promise no-charge work from the information available.
Close with a readback | Your report is recorded, my earlier dismissal is corrected, and the review call is at 15:00.''',
    notes='''I should not have | Accepts responsibility for a specific past statement.
Reporting the same | Attributes similarity to the customer's experience.
By itself | Limits what one observation can prove.
Either | Prevents the correction from becoming an opposite unsupported claim.
Can call at | Specifies an available contact commitment rather than repair completion.
Has not been determined | Keeps coverage unresolved without denying that it might apply.''',
    d='''Which apology is most appropriate? | I am sorry I dismissed your report; the cause has not been established | I am sorry you failed to understand our diagnosis | The sound is impossible, but I will call you | I apologize, so the repair will definitely be free | The response owns the unsupported dismissal without inventing a diagnosis or remedy.
Which note preserves the evidence? | Customer reports same intermittent rattle two days after service | Technician proved the original repair failed | New cause confirmed unrelated to earlier work | Warranty claim denied after full review | The note retains timing and attribution without adding an unestablished technical conclusion.
What does 15:00 refer to? | Nia's review call | Completion of a free repair | A confirmed collection slot | The time warranty coverage automatically begins | The brief identifies 15:00 as the time of the service lead's call.
Which statement should be avoided? | Your warranty definitely covers this repair | The cause remains unknown | Nia can review the report | I will correct my earlier statement | Warranty coverage is unknown and cannot be promised from the supplied facts.''',
    dialogue='''Farah | I called because the rattle is back, two days after the service. You told me it could not be the same issue, and that felt dismissive.
Daniel | You are right to challenge that wording. I made an [[unsupported dismissal::Unsupported dismissal describes Daniel's rejection of the report without an established cause.]], and I am sorry. I should not have said the issue could not be the same.
Farah | Thank you for saying that. I cannot name the faulty part. I can only tell you the intermittent sound seems the same to me.
Daniel | I will record that as a [[reported recurrence::Reported recurrence preserves Farah's account without turning it into a confirmed technical diagnosis.]] of the same intermittent rattle, two days after service. We have not established what is causing it.
Farah | I do not expect you to diagnose it over this call. I do expect the earlier visit to remain part of the conversation.
Daniel | It will. I will connect your new report with the [[service history::Service history keeps the earlier visit available during review of the repeat report.]], so the service lead can review the concern with the earlier record rather than treating it as unrelated without evidence.
Farah | Does admitting the earlier statement was wrong mean you now agree the repair failed? I want to know exactly what you are accepting.
Daniel | I am accepting that my response was wrong. The [[underlying cause::Underlying cause remains unknown even after Daniel corrects his inappropriate response.]] has not been established, so I cannot say the previous work definitely failed or that the current concern is definitely unrelated.
Farah | That distinction is fair. What happens next, and who will contact me? I do not want to repeat the whole story to another unidentified person.
Daniel | Nia, our [[service lead::Service lead identifies the named person who can review the report and discuss next arrangements.]], can call at fifteen hundred. The purpose is to review your report and the next arrangements, with the earlier service information available.
Farah | By fifteen hundred, you mean three in the afternoon? And that is a telephone call, not a request to bring the vehicle in then?
Daniel | Yes, three in the afternoon for a [[callback::Callback is the promised telephone review, not a vehicle drop-off or repair appointment.]]. It is not a booked repair slot or a completion promise. Nia will review the report and discuss what can be arranged next.
Farah | I will be available for the call. I also need to ask about the cost, because the service was only two days ago.
Daniel | I understand why you are asking. [[Warranty coverage::Warranty coverage is unresolved and must not be promised or denied without the relevant review.]] has not been determined. I cannot promise that work will be free, or say coverage is excluded, from the information we currently have.
Farah | Please include that question for Nia rather than leaving me to ask it all over again. I am not asking you to invent an answer.
Daniel | I will include it in the [[follow-up record::Follow-up record carries the repeat concern, earlier correction, and coverage question into the next conversation.]]. The record will show your concern, my correction, and the coverage question for review, without recording a decision that has not been made.
Farah | Could you read back the arrangement once? I want to be sure the apology has actually led to a clear next contact.
Daniel | Your [[repeat concern::Repeat concern is the same intermittent rattle reported again two days after the earlier service.]] is recorded with the earlier service history. My dismissal is withdrawn. Nia can call at fifteen hundred to review the report and next arrangements.
Farah | That is what I needed. I will speak with Nia then, and I understand that the call does not itself settle the cause or coverage.
Daniel | Correct. We have started the [[communication repair::Communication repair corrects the mishandled response while keeping diagnosis, coverage, and later arrangements unresolved.]] by correcting the statement and specifying the next contact. I will make sure the handoff reflects those facts accurately.''',
    transfer_title='Recover the conversation accurately',
    transfer_setup='Complete the follow-up readback. Keep the apology, report, contact time, and unresolved coverage distinct.',
    transfer='''Advisor: "I should not have ___ your report." | dismissed | Dismissed identifies the unsupported response that Daniel must explicitly correct.
Customer: "The rattle is still ___." | intermittent | Intermittent preserves the reported pattern instead of changing it to a constant sound.
Advisor: "Nia can call at ___." | 15:00 | 15:00 is the stated review-call time, not a repair completion time.
Customer: "Warranty coverage remains ___." | unknown | Unknown preserves the unresolved coverage position without promising or denying protection.'''
))
