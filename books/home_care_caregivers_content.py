"""Original Home Care and Caregiving learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='home-care-caregivers',
    title='Home Care & Caregiving English',
    cover_label='ENGLISH FOR RESPECTFUL, RELIABLE SUPPORT',
    cover_title='Home Care\nand Caregiving',
    cover_size=36,
    tagline='Listen carefully. Explain clearly. Follow through.',
    audience='For home care workers, personal care assistants, support workers, and caregiving teams.',
    map_intro='Eight conversations connect the care plan with everyday communication: clarify a visit, respect a choice, report a change, route a medicine question, discuss meals, protect privacy, hand over accurately, and explain a delay.',
    notes_title='The person comes before the task.',
    notes_intro='Caregiving English needs warmth and precision together. Speak directly to the person, explain what you can do, and distinguish an observation from an interpretation. Clear limits should come with a useful next step, not an abrupt dismissal.',
    field_notes=[
        ('Ask before helping', 'Explain the proposed support in ordinary language and listen to the response. A task on the plan does not make the person invisible or remove the need to follow the actual consent process.', '"Would you like help now, or would you prefer a few quiet minutes first?"'),
        ('Describe rather than diagnose', 'Keep the person\'s words separate from what you observed. Report changes through the appropriate route without inventing a cause or treating an incomplete description as proof that nothing is wrong.', '"She said she felt more tired; I noticed two pauses during our conversation."'),
        ('Name your role accurately', 'Assignments, training, and local rules determine what a worker can do. The fictional reminder-only assignment in this book does not authorize medication administration or dose advice.', '"I can help you contact the nurse, but I cannot decide a replacement dose."'),
        ('Close the communication loop', 'A sent message is not always an accepted handoff. Identify the unresolved issue, responsible person, next contact, and any urgent route. Record what actually happened, including uncertainty.', '"The coordinator has the transport query; no booking has been confirmed."'),
    ],
    scope_note='People, schedules, care plans, and incidents are fictional. This book teaches workplace English, not clinical care, medication instructions, capacity assessment, or professional certification. Follow the actual care plan, consent and privacy requirements, training, employer procedures, and qualified clinical advice. For urgent or emergency concerns use the appropriate local service and procedure without waiting for a routine callback. The cited England/UK sources do not establish universal rules.',
    sources=[
        dict(title='NICE. Home Care: Delivering Personal Care and Practical Support (NG21).',
             url='https://www.nice.org.uk/guidance/ng21/chapter/recommendations',
             note='England-focused guidance informs person-centered communication, continuity, records, and late-visit terminology. All teaching cases and dialogue language are original.', checked='1 October 2026'),
        dict(title='NICE. Managing Medicines for Adults Receiving Social Care in the Community (NG67).',
             url='https://www.nice.org.uk/guidance/ng67/chapter/Recommendations',
             note='Background on assigned responsibilities and referral of clinical medicine questions. The fictional reminder-only role is not a universal caregiver scope.', checked='1 October 2026'),
        dict(title='Care Quality Commission. Regulation 11: Need for Consent.',
             url='https://www.cqc.org.uk/guidance-regulation/providers/regulations-service-providers-and-managers/health-social-care-act/regulation-11',
             note='England regulatory context for ongoing consent and understandable communication. Local legal requirements and authorized processes govern actual practice.', checked='1 October 2026'),
        dict(title='NHS. When to Call 999.',
             url='https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/',
             note='UK emergency-service context. The book uses local emergency routes rather than applying one country-specific telephone number everywhere.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Confirming the visit and the care plan',
    scene='The appointment is real; the transport is unconfirmed',
    skill='Clarify scheduled support, acknowledge an unmet expectation, and request authorization without promising an unassigned service.',
    brief='Caregiver Maya arrives at 9:00 for a two-hour visit with Mr. Ellis. Her assignment lists breakfast support and light household tasks. He expects her to drive him to a 10:00 appointment, but transport is not listed and she has no authorization to provide it. The coordinator is available by phone. Maya must establish the discrepancy, contact the coordinator with the client involved as appropriate, and continue agreed support within her role. Neither a phone message nor a request for help confirms a transport booking.',
    cast='Mr. Ellis | Client\nMaya | Caregiver',
    culture=('A boundary needs a useful next step', 'An unexpected limit can sound like abandonment. Acknowledge the practical consequence, explain the assignment plainly, and identify who can clarify the arrangement. Avoid blaming the client for expecting something that may have been discussed elsewhere.'),
    a='''When is the scheduled visit due to end? | 11:00 | 10:00 | 12:00 | 9:30 | Two hours from the stated 9:00 arrival ends at 11:00.
What is not authorized in the supplied assignment? | Transport to the appointment | Breakfast support | Light household tasks | Contacting the available coordinator | Transport is absent from the assignment and Maya has no transport authorization.
What should Maya clarify with the coordinator? | The transport expectation and an authorized arrangement | Which personal car she must use without approval | Whether to mark a booking complete immediately | How to conceal the unmet expectation | The coordinator can check the discrepancy and appropriate arrangement without Maya inventing authorization.''',
    vocabulary='''care plan | A record of assessed needs and agreed support arrangements. | follow the care plan
assignment | The particular work allocated to a worker. | confirm the assignment
visit window | The specified period for an expected visit. | confirm the visit window
scheduled duration | The planned length of a visit or service. | check the scheduled duration
care coordinator | The person coordinating relevant care arrangements. | contact the care coordinator
support need | An area in which a person requires assistance. | clarify a support need
ADLs | Activities of daily living, such as dressing or eating. | support ADLs
IADLs | Instrumental activities of daily living, such as shopping or household management. | assist with IADLs
personal care | Support with personal daily activities within an agreed role. | provide personal care
domestic support | Agreed help with household activities. | arrange domestic support
light housekeeping | Limited household tasks within the assigned service. | clarify light housekeeping
appointment | A planned meeting or service at a specified time. | confirm the appointment
transport authorization | Permission for the particular transport arrangement. | obtain transport authorization
escort | A person accompanying someone under an agreed arrangement. | arrange an escort
scope of duties | The tasks permitted within the worker's actual role. | clarify the scope of duties
service discrepancy | A difference between expected and recorded service. | report a service discrepancy
unmet expectation | Something expected that has not been confirmed or provided. | acknowledge an unmet expectation
booking confirmation | Evidence that a particular service reservation is accepted. | obtain booking confirmation
accessible transport | Transport suited to the person's relevant access needs. | request accessible transport
contingency arrangement | A prepared alternative for a possible disruption. | activate a contingency arrangement
contact route | The approved way to reach the appropriate person. | use the contact route
visit record | The factual account of support and events during a visit. | update the visit record
authorized change | A change agreed through the required process. | document an authorized change
read-back | Repeating key information to check that it was understood correctly. | give a read-back''',
    precision='An appointment time is not a transport booking. A transport request is not authorization for the caregiver to drive. Keep the appointment, departure arrangements, transport provider, and booking status distinct when asking the coordinator to resolve the discrepancy.',
    precision_extra='The care plan describes agreed support; the assignment identifies this visit and worker. If the two appear inconsistent, use the approved clarification process. Do not silently expand duties, erase the request, or record an unconfirmed service as arranged.',
    phrases='''Introduce the visit | Good morning, Mr. Ellis. I am here for your nine-to-eleven visit.
Confirm the plan | My assignment lists breakfast support and light household tasks.
Invite clarification | What were you expecting for your appointment this morning?
Acknowledge the impact | I understand that getting there at ten matters to you.
Name the discrepancy | Transport is not listed in the assignment I have.
Explain the boundary | I do not have authorization to drive you.
Offer a next step | I can contact the coordinator now to check the arrangement.
Ask to include the client | Would you like to be part of that conversation?
Report without blame | There is a difference between the expected support and my recorded assignment.
Check the status | Has transport actually been booked, or only requested?
Clarify responsibility | Who is confirming the transport arrangement?
Check access needs | Please confirm any access requirements through the agreed process.
Avoid a false promise | I cannot confirm a driver until the coordinator verifies the booking.
Continue agreed support | While we clarify that, would you like help with breakfast?
Repeat key details | Let me check: the appointment is at ten, and transport is still unconfirmed.
Record the outcome | I will record the request, who was contacted, and the confirmed response.''',
    notes='''My assignment lists | Refers to the available record without accusing another person of being wrong.
I understand that | Recognizes the practical impact before explaining a limit.
Do not have authorization | Describes a specific boundary, not a personal unwillingness to help.
Has actually been booked | Separates a completed arrangement from an earlier request.
While we clarify that | Connects ongoing agreed support with the unresolved issue.
Still unconfirmed | Preserves uncertainty rather than implying that transport cannot be arranged.''',
    d='''Which statement is both helpful and accurate? | Transport is not in my assignment; I can call the coordinator to check it now. | My arrival proves transport is included. | Your appointment must be wrong. | I will drive you before asking anyone. | The first response identifies the boundary and supplies an appropriate immediate clarification route.
Which record would overstate progress? | Transport confirmed, when only a message has been sent | Transport requested; coordinator contacted | Appointment reported for 10:00 | No transport authorization available to Maya | Sending a request does not establish that a provider accepted or confirmed transport.
What does a read-back help establish? | Shared understanding of the appointment and transport status | Automatic permission to drive | A guarantee of arrival time | Clinical suitability for all transport types | Repeating key details checks communication but does not supply missing service authorization.
Which question is most useful? | Who will confirm the arrangement and contact Mr. Ellis? | Can we assume any relative will drive? | Can the transport request be omitted from the record? | Does breakfast support include every possible errand? | Identifying the responsible contact makes the unresolved arrangement actionable without inventing a provider.''',
    dialogue='''Mr. Ellis | Good morning, Maya. My appointment is at ten, so I thought we would have breakfast quickly and then leave in your car.
Maya | Good morning. My [[assignment::The assignment identifies Maya's allocated tasks; it does not include permission to provide transport.]] is for breakfast support and light household tasks from nine until eleven. I do not have transport listed, but I can check that with the coordinator now.
Mr. Ellis | I mentioned the appointment when someone called last week. I understood that the visit would include getting me there, not just making breakfast.
Maya | I understand the [[unmet expectation::The expected transport has not been confirmed in the available assignment, and the impact deserves acknowledgment.]]. We should clarify what was discussed without assuming you misunderstood. Getting to the appointment matters, and I want the coordinator to check the arrangement directly.
Mr. Ellis | Could you take me this once? It is only a short drive, and I do not want to lose the appointment.
Maya | I do not have [[transport authorization::Transport authorization is missing; a short journey or urgent request does not supply it.]]. I can help contact the person who can resolve the request, but I cannot make a private driving arrangement outside my assigned role.
Mr. Ellis | All right. Please explain that the appointment is at ten. I would rather speak to the coordinator with you than repeat everything later.
Maya | Of course. We can give a clear [[read-back::A read-back checks shared understanding of the time and unresolved arrangement without creating a booking.]] of the details together: appointment at ten, visit from nine to eleven, and no confirmed transport information in my assignment.
Mr. Ellis | Does that mean nobody has booked a car? There might be something in the office records that neither of us can see.
Maya | Exactly. The [[booking confirmation::Booking confirmation would establish an accepted reservation; the current absence of information does not prove no booking exists.]] may be elsewhere. I will ask what is actually arranged rather than tell you that nothing exists when I have not checked.
Mr. Ellis | I also need enough time to get to the entrance. Please make sure they do not confuse the appointment time with the pickup time.
Maya | I will explain that distinction to the [[care coordinator::The care coordinator is the available role responsible for clarifying relevant arrangements, not a presumed transport provider.]]. The appointment time and pickup time are separate, and any access arrangements need to be confirmed through the proper process.
Mr. Ellis | What happens to breakfast while we are sorting this out? I have not eaten yet, and I still want the agreed help.
Maya | Breakfast remains part of my [[scope of duties::The scope of duties includes breakfast support while the separate transport request remains unresolved.]]. We can continue that support with your agreement while the office checks the transport, without marking the additional request as settled.
Mr. Ellis | When the coordinator answers, please let me hear exactly what is confirmed. I do not want another message that only says someone is dealing with it.
Maya | We will ask for the responsible person and the [[contact route::The contact route identifies how the responsible person will communicate a confirmed response or further update.]] for the response. If an arrangement changes, we need the actual details, not just an assurance that the request was passed on.
Mr. Ellis | Thank you. I can explain what I was told last week, and you can explain what is on your assignment this morning.
Maya | That will help us report the [[service discrepancy::The service discrepancy is the difference between expected transport and the available assignment, not an established finding of fault.]] fairly. I will keep your account separate from what the current record says, so the coordinator can reconcile them.
Mr. Ellis | Please put the outcome in the notes as well. The next person should not have to start the same conversation from the beginning.
Maya | I will update the [[visit record::The visit record should preserve the request, contacts, and actual outcome without converting pending work into completion.]] with the request, contact, and confirmed response. Until we have that response, I will describe transport as unconfirmed rather than booked.''',
    transfer_title='Clarify a different unassigned errand',
    transfer_setup='A 14:00-15:00 visit includes household support. The client expects a parcel pickup, which is not assigned. The coordinator can clarify it; no pickup has been booked.',
    transfer='''Caregiver: "This visit ends at ___." | 15:00 | The stated one-hour visit runs from 14:00 to 15:00.
Client: "The extra request is a ___." | parcel pickup | The new expectation concerns a parcel, not an appointment journey.
Caregiver: "I will clarify the request with the ___." | coordinator | The coordinator is identified as the appropriate person to clarify the unassigned request.
Caregiver: "The pickup is currently ___." | unconfirmed | No pickup has been booked, so completion or confirmation would overstate the facts.''',
))

BOOK['units'].append(unit(
    title='Consent, choice, and respectful assistance',
    scene='Ten quiet minutes before choosing clothes',
    skill='Offer support without pressure, respect a changed preference, and record the agreed timing without judgment.',
    brief='Caregiver Imani has thirty minutes left in her visit with Ms. Hale. Support with choosing and arranging clothes is included in the plan, but Ms. Hale declines help now and asks for ten quiet minutes before a visitor arrives. There is no immediate safety concern in this scenario. Imani should acknowledge the choice, explain the remaining time, and agree whether to ask again later. A listed task is not permission to override the person. The record should describe what was offered, chosen, and actually provided rather than label the client difficult.',
    cast='Ms. Hale | Client\nImani | Caregiver',
    culture=('Respect does not depend on agreement', 'A worker may feel pressure to complete every listed task. Use an adult-to-adult tone and separate the service schedule from the person\'s choice. A preference that differs from yours is not evidence that the person cannot decide.'),
    a='''What does Ms. Hale request? | Ten quiet minutes before help is discussed again | Immediate help despite her refusal | Cancellation of all future care | A change to her visitor's identity | Her stated preference concerns the timing of this task, not the entire care arrangement.
How much scheduled visit time remains after ten minutes? | Twenty minutes | Ten minutes | Forty minutes | No time | Thirty minutes remaining minus ten quiet minutes leaves twenty scheduled minutes.
Which fact is explicitly supplied? | There is no immediate safety concern in this scenario. | Ms. Hale cannot make decisions. | Her visitor can automatically consent for her. | Clothes must be arranged despite refusal. | The brief excludes an immediate safety concern but does not establish incapacity or substitute consent.''',
    vocabulary='''consent | Agreement to a particular action through the applicable process. | seek consent
withdraw consent | Change an earlier agreement so that the action is no longer agreed. | respect withdrawn consent
decline assistance | Say that offered help is not wanted. | acknowledge declined assistance
preference | A person's stated choice or favored way of doing something. | respect a preference
autonomy | A person's ability and right to direct relevant choices about their life. | support autonomy
dignity | Respect for a person's worth, privacy, and personhood. | preserve dignity
person-centered support | Support organized around the person's needs, choices, and circumstances. | provide person-centered support
supported choice | A decision made with appropriate communication or practical assistance. | enable supported choice
decision-specific | Relating to the particular decision, not every possible choice. | use decision-specific language
capacity | Ability to make a particular decision under the applicable legal framework. | refer a capacity concern
coercion | Pressure or force that undermines free choice. | avoid coercion
assent | An expression of agreement whose legal significance depends on context. | distinguish assent from legal consent
verbal agreement | Agreement expressed in spoken words. | confirm verbal agreement
nonverbal response | Communication through gesture, expression, or other nonspoken behavior. | notice a nonverbal response
communication need | A requirement that helps a person understand or express themselves. | meet a communication need
processing time | Time needed to understand information and formulate a response. | allow processing time
privacy preference | A stated choice about personal space or access to information. | clarify a privacy preference
reoffer | Offer support again without assuming the answer will change. | agree when to reoffer
time remaining | The portion of the scheduled visit not yet used. | explain the time remaining
partial support | Help with only the agreed part of a task. | offer partial support
independence | Doing or directing activities with the appropriate degree of support. | promote independence
judgmental label | A description that criticizes a person rather than reporting events. | avoid judgmental labels
neutral wording | Language that describes facts without an unsupported evaluation. | use neutral wording
agreed pause | A mutually understood break before an activity is discussed or resumed. | respect an agreed pause''',
    precision='Declining one offer now does not automatically cancel every later offer or the whole care plan. Ask about the specific task and timing. Respect the actual response; a convenient schedule does not turn refusal into consent.',
    precision_extra='Do not infer lack of decision-making capacity from disagreement, age, accent, or a choice you dislike. Any genuine concern belongs in the applicable assessment and escalation process, not an improvised judgment used to make the task easier.',
    phrases='''Offer help | Would you like help choosing your clothes?
Accept the answer | That is fine; I will not start now.
Check the preference | Would you prefer a few quiet minutes first?
Explain the schedule | There are thirty minutes left in this visit.
Make timing clear | If we pause for ten minutes, twenty minutes will remain.
Ask about a later offer | Would you like me to ask again after that?
Avoid pressure | You do not need to agree just to complete my task list.
Clarify a smaller task | Would help laying out one item be useful, or would you prefer no help?
Respect privacy | Where would you like me to wait during the pause?
Check a changed choice | Is that still what you would like?
Address the person directly | I would like to hear your preference first.
Avoid a label | I will record the help offered and your response.
Distinguish the scope | You are declining this help now, not necessarily every later offer.
Acknowledge independence | You can choose what you want to wear.
Keep a boundary honest | I cannot promise extra visit time without an authorized change.
Confirm the agreement | We will pause for ten minutes, and I will ask again as agreed.''',
    notes='''Would you like | Makes the offer a genuine choice rather than a disguised instruction.
I will not start | Confirms that the worker heard and will respect the current response.
If we pause | Explains the time consequence without using it as a threat.
Ask again | Requests permission to reoffer rather than announcing repeated pressure.
Your preference first | Keeps the person central even when a visitor or relative is present.
Help offered and your response | Supports factual recording instead of a judgment about personality.''',
    d='''Which record is most accurate? | Clothes support offered; Ms. Hale requested a ten-minute pause and agreed to a later offer. | Client was difficult and wasted ten minutes. | All future clothes support permanently refused. | Consent assumed because the task was listed. | The factual record preserves the specific offer, response, and timing without a judgmental or exaggerated conclusion.
Which reply avoids pressure? | I will pause; would you like me to ask again in ten minutes? | You must agree because I have a checklist. | I will begin quietly so you do not notice. | Your visitor will decide whether your refusal counts. | The reply respects the current choice and seeks agreement about a later offer.
What does refusal alone establish here? | The offered help is not wanted at this moment. | An inability to make any decision | A clinical diagnosis | Permission to use force | The refusal concerns this offer and time, not a diagnosis or global decision-making ability.
Which timing statement is correct? | Twenty scheduled minutes remain after the agreed ten-minute pause. | The pause automatically adds ten minutes to the visit. | No support may be offered again. | Thirty minutes remain after the pause. | The pause uses ten of the thirty remaining minutes and does not automatically extend the visit.''',
    dialogue='''Ms. Hale | Please leave the clothes for now, Imani. My visitor is coming later, but I would like ten quiet minutes before we do anything else.
Imani | Of course. I will respect that [[preference::The preference concerns a quiet pause before clothing support, not a refusal of every service.]] and will not start arranging them. Would you like me to ask again after ten minutes, or would you prefer not to discuss clothes today?
Ms. Hale | Ask me again after the pause. I might just need help finding the blue cardigan, but I want to sit quietly first.
Imani | We can agree on that [[reoffer::A reoffer is a later invitation to accept help, not an assumption that the person will agree.]]. There are thirty minutes left in my visit, so twenty will remain afterward. I want you to know the timing without feeling rushed.
Ms. Hale | I know you have a list to finish. I sometimes feel I should say yes because otherwise the notes will make me sound uncooperative.
Imani | I can use [[neutral wording::Neutral wording reports the offer and response without turning a personal choice into criticism.]] in the record. I will describe what I offered and what you requested, rather than give you a negative label for making a choice.
Ms. Hale | That would help. I still want to choose my own clothes. Having someone here should not mean everything gets decided for me.
Imani | Your [[independence::Independence includes directing the support and choosing clothes, not necessarily completing every movement without help.]] matters. I can help with an agreed part of the task, such as finding the cardigan, without taking over decisions you want to make yourself.
Ms. Hale | Could you wait in the sitting room? I would rather not have someone sorting things behind me while I am trying to relax.
Imani | Yes, that is a clear [[privacy preference::The privacy preference specifies where the worker should wait and excludes continuing the task during the pause.]]. I will not use the pause to start the task anyway. Let me know if you want to change that arrangement.
Ms. Hale | My niece sometimes says I should accept whatever help is offered. She means well, but I want you to ask me directly.
Imani | I will. Your answer to this offer is the relevant [[verbal agreement::Verbal agreement expresses the person's response to the specific offer; a relative's general opinion is not a substitute.]] we are discussing. I will not treat another person's opinion as permission to ignore what you have just said.
Ms. Hale | And if I agree later but then want you to stop, can I say so? Some days I change my mind halfway through.
Imani | Yes. You can [[withdraw consent::Withdrawing consent changes the earlier agreement; the worker must follow the actual consent process rather than rely on an old yes.]]. Tell me if you no longer want the help, and I will respond to that rather than assume an earlier yes lasts regardless of what you say.
Ms. Hale | Thank you. I only need a little time, not a debate about whether my reasons are good enough for everyone else.
Imani | I will allow that [[processing time::Processing time allows the person space to respond and choose without repeated prompts or pressure.]]. A quiet pause can be part of respectful communication. There is no need to repeat the same question every minute while you are deciding.
Ms. Hale | After the ten minutes, I think finding the cardigan will be enough. I can decide about the rest when you ask me.
Imani | That would be [[partial support::Partial support covers only the agreed part of the task, such as finding one garment.]]. We can confirm it then, and I will be honest about the remaining visit time rather than promise an extension that has not been authorized.
Ms. Hale | Good. Let us take the quiet time now, and then you can check with me again before touching the clothes.
Imani | We have an [[agreed pause::The agreed pause is ten minutes with permission to ask again afterward, not permission to begin the task automatically.]] of ten minutes. I will wait in the sitting room, ask again afterward, and record the support you actually choose and receive.''',
    transfer_title='Respond to a request for a shorter pause',
    transfer_setup='There are twenty-five minutes left. The client requests five quiet minutes and agrees to a later offer of help with a coat. No immediate safety concern is supplied.',
    transfer='''Caregiver: "We will pause for ___ minutes." | five | The client requested a five-minute pause before another offer.
Client: "Please ask again about help with my ___." | coat | The specified later offer concerns a coat, not all clothing tasks.
Caregiver: "That leaves ___ scheduled minutes." | twenty | Twenty-five minutes remaining minus a five-minute pause leaves twenty.
Caregiver: "I will record the offer and response using ___." | neutral wording | Factual language records the specific choice without criticizing the person.''',
))

BOOK['units'].append(unit(
    title='Reporting a change without diagnosing',
    scene='A precise report without an invented cause',
    skill='Attribute the client\'s words, describe a change from usual behavior, and seek the appropriate response without diagnosing.',
    brief='During a routine visit, caregiver Luis hears Ms. Chen say, "I feel more tired than yesterday." At 9:20, he notices that she stops twice while describing breakfast, which is unusual during his visits. He contacts nurse Jo through the local reporting procedure. He has no clinical diagnosis and has not measured vital signs. No emergency signs are specified in this fictional brief; that is not proof that the person is safe. Any urgent or emergency concern must follow the local urgent route without waiting for routine reporting.',
    cast='Luis | Caregiver\nJo | Nurse receiving the report',
    culture=('Specific observations travel better than labels', 'Words such as fine, poorly, confused, or not herself may hide the information the next person needs. Give the person\'s own words, the observable event, the time, and the comparison you can genuinely support. Let qualified staff assess the cause.'),
    a='''Which statement comes directly from the client? | I feel more tired than yesterday. | She has a diagnosed infection. | Her vital signs are normal. | She is safe to wait indefinitely. | The brief supplies a direct report of tiredness, not a diagnosis or measured assessment.
What did Luis observe? | Two pauses while Ms. Chen described breakfast at 9:20 | A confirmed cause of tiredness | A complete clinical examination | A measured temperature change | The observed event is the two pauses, with a stated time and context.
What must happen if an urgent concern arises? | Use the appropriate local urgent or emergency route without waiting for routine reporting. | Wait until the end of the shift regardless. | Diagnose the cause first. | Treat the fictional absence of emergency details as proof of safety. | The routine reporting exercise does not replace timely local action for urgent or emergency concerns.''',
    vocabulary='''observation | Something the worker directly notices, distinguished from an interpretation. | report an observation
reported symptom | An experience described by the person, not necessarily measured by the listener. | attribute a reported symptom
direct quotation | The person's actual words presented as their statement. | preserve a direct quotation
onset | When a change or symptom began, if known. | clarify the reported onset
baseline | The usual pattern used for a relevant comparison. | describe the known baseline
change from usual | A difference from the person's previously observed pattern. | report a change from usual
frequency | How often something occurs in the stated period. | record the observed frequency
duration | How long an event lasts, when this is known. | clarify the duration
context | The circumstances in which an event happened. | provide relevant context
objective description | A specific factual account rather than an unsupported conclusion. | use an objective description
subjective report | An experience described from the person's perspective. | attribute a subjective report
clinical assessment | Evaluation by an appropriately qualified professional. | request clinical assessment
diagnosis | Identification of a condition through an appropriate clinical process. | avoid an unsupported diagnosis
vital signs | Clinical measurements such as pulse or temperature, taken within an authorized role. | report measured vital signs
unmeasured | Not measured; different from a normal result. | identify unmeasured information
uncertainty | Something not yet established or known. | state uncertainty
red flag | A sign or concern requiring particular attention under the relevant procedure. | recognize a red flag
escalation | Raising a concern through the appropriate route for action. | make a timely escalation
urgent pathway | The designated process for concerns requiring prompt action. | use the urgent pathway
callback | A return call that may still be pending. | request a callback
SBAR | Situation, background, assessment, recommendation; a structured communication framework used in some services. | use the local SBAR format
read-back confirmation | Repetition of key information followed by a check of accuracy. | request read-back confirmation
contemporaneous note | A record made at or near the time of the event. | make a contemporaneous note
follow-up instruction | Direction about the next action from the appropriate person. | clarify follow-up instructions''',
    precision='Not measured is not the same as normal. No emergency signs specified in a teaching brief is not a real clinical clearance. Report the actual known information and follow the local urgent pathway whenever the circumstances require it.',
    precision_extra='Separate what the person said, what you saw, and what you do not know. If your service uses SBAR, keep the assessment portion within your role: describe the concern and observation rather than invent a diagnosis or a measurement.',
    phrases='''Open the report | I am calling about a change I noticed during this visit.
Identify the source | Ms. Chen told me she feels more tired than yesterday.
Quote accurately | Her exact words were, I feel more tired than yesterday.
Describe the observation | She stopped twice while describing breakfast.
Give the time | I noticed this at nine twenty.
Bound the comparison | That is unusual during my visits with her.
State a limit | I do not know what is causing it.
Avoid a false measurement | I have not measured her vital signs.
Clarify onset | I know when I noticed it, but not when it began.
Request the next step | What should happen next under the care plan and reporting procedure?
Check receipt | Can you confirm that you have received the concern?
Read back an instruction | Let me repeat the instruction to check I understood it.
Correct an inference | I reported tiredness; I did not diagnose the cause.
Keep urgency separate | I will use the urgent route if the concern requires it.
Document the exchange | I will record the observation, time, contact, and instructions received.
Avoid false closure | The report is received; that does not mean a clinical assessment is complete.''',
    notes='''Told me | Attributes an experience to the person rather than presenting it as a measured finding.
While describing breakfast | Supplies context for the observation without inventing its cause.
During my visits | Bounds the baseline to the worker's actual experience.
Have not measured | Keeps missing data distinct from reassuring results.
When I noticed it | Distinguishes observation time from symptom onset.
Received versus assessed | Prevents administrative receipt from being mistaken for clinical evaluation.''',
    d='''Which report is most precise? | At 9:20 she paused twice while describing breakfast and said she felt more tired than yesterday. | She definitely has an infection. | She is fine because no numbers were recorded. | Her mood is bad, so no report is needed. | The precise account combines time, observable behavior, and attributed words without inventing a cause.
How should missing vital signs be described? | Not measured by Luis | Normal | Negative | Clinically cleared | The absence of measurements cannot be converted into normal findings or clinical clearance.
Which time is established? | When Luis noticed the pauses | The exact onset of tiredness | The start of a diagnosed disease | The time of a completed clinical assessment | The brief gives an observation time, while the onset and assessment remain unspecified.
What does receipt of the report establish? | The concern reached the receiving person, not that assessment is complete. | The cause is diagnosed. | No follow-up can be needed. | A routine callback overrides every urgent pathway. | Communication receipt and clinical evaluation are separate stages with different meanings.''',
    dialogue='''Luis | Jo, I am calling through the reporting line about Ms. Chen. I noticed a change during this morning's visit and want to pass on the exact information.
Jo | Start with the [[reported symptom::The reported symptom is Ms. Chen's description of tiredness, which should remain attributed to her.]] in her own words, then tell me what you directly observed. Keeping those two sources separate will make the report easier to assess.
Luis | She said, I feel more tired than yesterday. While she was describing breakfast, she stopped twice. That was at nine twenty this morning.
Jo | Thank you. That gives an [[objective description::The objective description states the two pauses, their context, and the observation time without assigning a cause.]] of the pauses and an attributed account of how she feels. Do you know when the tiredness actually began?
Luis | No. I know when we had the conversation, but I cannot say when she first started feeling tired or whether it changed overnight.
Jo | Then the [[onset::Onset means when the change began; the time the worker noticed it does not automatically establish that.]] is not established. Keep nine twenty as the observation time, rather than enter it as the start of the symptom.
Luis | She does not usually pause like that when we talk during my visits. I have not watched her continuously outside those visits, though.
Jo | That is a useful, bounded [[baseline::The baseline is Luis's usual observation during visits, not a claim about every moment outside them.]]. Describe what is unusual in your experience without implying that you know her behavior throughout the whole day or night.
Luis | I was tempted to write that she must be coming down with something. It would be shorter, but I do not actually know the cause.
Jo | Please do not substitute a [[diagnosis::A diagnosis is a clinical conclusion; Luis's observations do not establish a specific cause of the change.]] for the observations. The report should preserve the tiredness, pauses, timing, and uncertainty so the appropriate professional can assess the concern.
Luis | I also have no temperature, pulse, or other measurements to report. Taking those measurements is not part of what I have done this morning.
Jo | Record those as [[unmeasured::Unmeasured describes missing measurements and must not be translated into normal or reassuring results.]], not normal. A blank measurement field cannot support reassurance, and you should not invent a reading to make the record look complete.
Luis | I understand. If the situation becomes urgent while I am trying to reach someone, I should not wait just because a routine message is already in the system.
Jo | Correct. Use the local [[urgent pathway::The urgent pathway addresses concerns requiring prompt action and is not replaced by a pending routine message.]] when required, including emergency services where appropriate. Routine reporting and urgent response serve different needs; an earlier message does not remove that distinction.
Luis | Can you confirm that you have received this report? I also need the next instructions through our care procedure so I know what to record.
Jo | I have received it. We must distinguish that from a completed [[clinical assessment::Clinical assessment is the relevant professional evaluation, not merely acknowledgment that the report arrived.]]. I will address the next steps through our clinical process; do not describe this call as an assessment outcome.
Luis | When you give the instructions, I will repeat the important details. I would rather check an unclear word than act on what I think I heard.
Jo | That [[read-back confirmation::Read-back confirmation checks whether the instructions were understood accurately before they are recorded or acted upon.]] is helpful. Ask immediately if a direction, responsibility, or timing is unclear, and keep any action within the responsibilities you are authorized to perform.
Luis | My record will include her words, the two pauses, nine twenty, what I do not know, and this contact. It will not say that a cause has been confirmed.
Jo | Good. Make a [[contemporaneous note::A contemporaneous note preserves the actual observation and communication near the event, including limits and instructions received.]] and record the actual instructions and response, not an expected outcome. Continue to use the appropriate local route if the concern changes.''',
    transfer_title='Keep a second observation separate from its cause',
    transfer_setup='At 14:10, a client says, "My usual shoes feel tighter today." The caregiver notices the client trying twice to fasten them. No cause or measurements are established; the local reporting route applies.',
    transfer='''Caregiver: "The observation time is ___." | 14:10 | The supplied time concerns when the caregiver noticed the event.
Receiver: "The client reported that the shoes felt ___." | tighter today | These words preserve the person's stated experience rather than invent a clinical finding.
Caregiver: "I observed ___ attempts to fasten them." | two | Two fastening attempts are the specified direct observation.
Receiver: "The cause remains ___." | unconfirmed | The scenario supplies no assessment establishing the cause of the reported change.''',
))

BOOK['units'].append(unit(
    title='Boundaries around medicines and clinical questions',
    scene='A missed dose needs qualified advice',
    skill='Explain a reminder-only role, acknowledge a medication question, and help obtain qualified advice without recommending a dose.',
    brief='Mr. Ahmed tells caregiver Rosa that he missed a medicine dose and asks whether to take twice as much now. Rosa does not know the medicine, strength, prescribed schedule, or when the missed dose was due. Her fictional assignment permits reminders only, not administering medicines or recommending doses. The care plan names a nurse contact for medication questions. Rosa should explain her role and help seek timely qualified advice through the plan. She must not guess a dose, turn a missed dose into a refusal, or delay an urgent response for routine contact.',
    cast='Mr. Ahmed | Client\nRosa | Caregiver',
    culture=('A helpful limit is more than a refusal', 'People may ask a trusted worker for an immediate answer. Acknowledge the concern, make the professional boundary understandable, and offer the approved route to advice. Avoid either guessing to seem helpful or leaving the person with only a curt disclaimer.'),
    a='''What does Rosa's assignment permit? | Reminders only | Recommending replacement doses | Administering any requested medicine | Changing the prescription | The fictional assignment expressly limits Rosa to reminders and excludes administration and dose recommendations.
What information is missing? | Medicine details and the relevant dose timing | The existence of a nurse contact | The fact that a question was asked | Rosa's reminder-only role | The medicine, strength, schedule, and missed-dose timing are unknown in the brief.
What is the appropriate communication response? | Explain the limit and help contact the qualified advice route in the plan. | Tell him to double every missed dose. | Tell him to skip every missed dose. | Describe the medicine as harmless without knowing it. | Qualified, medicine-specific advice is needed; neither a doubling nor a skipping rule can be invented.''',
    vocabulary='''medication reminder | A prompt within the agreed role to support a person's own medicine routine. | give an authorized medication reminder
administration | Giving or applying medicine under the applicable authorization and competence requirements. | distinguish administration from a reminder
prescriber | A professional authorized to prescribe the relevant medicine. | contact the prescriber
pharmacist | A qualified medicines professional. | seek pharmacist advice
prescription | An authorized instruction for a specified medicine. | check the current prescription
dose | The amount of medicine specified for one administration. | clarify the prescribed dose
strength | The amount of active ingredient per stated unit or quantity. | identify the medicine strength
dosage form | The physical form of a medicine, such as a tablet or liquid. | identify the dosage form
route of administration | How a medicine is taken or applied. | confirm the route of administration
missed dose | A scheduled dose that was not taken at the intended time. | report a missed dose
duplicate dose | An additional dose taken or given when the relevant dose has already been taken or given. | report a possible duplicate dose
dosing interval | The time between doses under the prescribed schedule. | clarify the dosing interval
dispensing label | The pharmacy label identifying the medicine and directions. | refer to the dispensing label
medication list | A record of medicines whose accuracy and currency require confirmation. | verify the medication list
MAR | Medication administration record; a record used for actual medicine administration under local arrangements. | distinguish a MAR from a reminder note
PRN | From pro re nata; medicine prescribed for use when needed under specified directions. | clarify PRN directions
contraindication | A reason a particular treatment may be inappropriate in a given situation. | refer a contraindication question
interaction | An effect arising from combining medicines or other relevant substances. | ask about an interaction
side effect | An effect of a medicine other than its intended main action. | report a suspected side effect
adverse reaction | An unwanted harmful response associated with a medicine. | report a suspected adverse reaction
medication discrepancy | A difference between medicine information or records that needs clarification. | report a medication discrepancy
clinical question | A question requiring relevant professional assessment or advice. | route a clinical question
delegated task | A task formally assigned under the applicable authority and competence arrangements. | clarify a delegated task
out-of-hours contact | The designated advice or response route outside ordinary service hours. | use the out-of-hours contact''',
    precision='Reminding, administering, and recommending a dose are different actions. The fictional role permits only the first. Recognizing a label or medicine name does not supply clinical authority, and another worker may have a different authorized role.',
    precision_extra='Missed, declined, and already taken describe different events. Attribute the client report and check facts through the approved process. Do not record administration that you did not perform or witness, or treat a request for advice as a confirmed medication error.',
    phrases='''Acknowledge the question | I understand you want to know what to do about the missed dose.
State the role | My assignment permits reminders, not dose advice.
Separate the actions | A reminder is different from administering the medicine.
Decline to guess | I cannot safely decide that from the information I have.
Offer useful help | I can help you contact the nurse listed in your care plan.
Preserve the question | You are asking whether to take twice the usual amount.
Identify missing details | The professional will need the medicine details and relevant timing.
Avoid a blanket rule | Different medicines require different advice.
Ask about the contact route | Shall we use the nurse contact in the plan now?
Keep the client involved | You can explain what happened, and I can help communicate the question.
Clarify an unclear direction | Please repeat that instruction so we can check it accurately.
Separate reported facts | You told me the dose was missed; I did not observe when it was due.
Avoid false recording | I will not record a medicine as administered when I did not administer it.
Use the proper backup | If the usual contact is unavailable, we need the approved alternative route.
Keep urgency clear | An urgent concern should not wait for a routine callback.
Record the response | I will document the question, contact, and actual advice received through the required process.''',
    notes='''Permits reminders | Names the specific assignment boundary without claiming every caregiver has the same role.
Cannot decide | Avoids giving an unsupported answer disguised as a suggestion.
Listed in your plan | Directs the person to the actual agreed route rather than an invented service.
Relevant timing | Includes when the dose was due and what actually happened, if known.
Different medicines | Explains why a remembered general rule is inadequate.
Actual advice received | Keeps pending contact separate from a completed professional response.''',
    d='''Which response stays within the supplied role? | I cannot recommend a dose; I can help contact the nurse in your plan. | Take twice as much because yesterday was missed. | Skip it because that is always safer. | I will administer whatever amount you choose. | The response gives a useful qualified route without exceeding the reminder-only assignment.
Which record is inaccurate? | Dose administered by Rosa, when she only helped place a call | Client reports a missed dose | Dose question referred through the plan | Medicine details not yet established | Helping obtain advice is not administration and must not be recorded as such.
What would justify a universal missed-dose rule here? | Nothing in the supplied facts | The client's confidence | The caregiver's familiarity with another medicine | A short visit duration | The medicine and circumstances are unknown, and clinical advice is outside the assigned role.
What if the usual nurse contact is unavailable? | Use the approved alternative or urgent route appropriate to the concern. | Invent a replacement prescription. | Wait indefinitely regardless of urgency. | Use another client's medicine instructions. | The appropriate backup pathway preserves timely access to advice without inventing medicine-specific instructions.''',
    dialogue='''Mr. Ahmed | Rosa, I missed a dose of my medicine. Should I take twice as much now to make up for it? I do not want to get behind.
Rosa | That is a [[clinical question::The dose decision needs qualified, medicine-specific advice rather than a caregiver's guess.]], and I cannot decide the dose. My assignment covers reminders only, but I can help you reach the nurse named in your care plan.
Mr. Ahmed | You usually ask whether I have remembered my medicine. I thought that meant you could tell me how to fix a missed one as well.
Rosa | A [[medication reminder::A medication reminder supports the agreed routine but does not authorize dose changes or administration.]] and advice about changing a dose are different. I can prompt within the agreed plan; I cannot choose a new amount or recommend how to replace a missed dose.
Mr. Ahmed | The medicine is in the other room. I do not remember the exact name, and I have not told you when I was supposed to take it.
Rosa | Those details matter, including the name, [[strength::Strength identifies the amount of active ingredient per unit and is one relevant detail for qualified advice.]], and timing. We should give the professional accurate information, not rely on a tablet's color.
Mr. Ahmed | I read somewhere that people sometimes take the next dose as usual. Could we just follow that advice and avoid bothering the nurse?
Rosa | I cannot turn that into a rule for your [[missed dose::A missed dose requires advice appropriate to the actual medicine and circumstances, which are not established here.]]. The right response depends on the medicine and circumstances, and those have not been established in our conversation.
Mr. Ahmed | All right. The care plan has the number we normally use. I would like help making the call because I sometimes lose track of the question.
Rosa | I can help you reach that contact and explain the question clearly. The [[prescriber::The prescriber is an authorized clinical source; the actual advice route in this plan begins with the named nurse contact.]] or another appropriate medicines professional may need to advise through the agreed route.
Mr. Ahmed | Please say that I am asking about a missed dose, not that I deliberately refused treatment. Those are not the same thing.
Rosa | I will preserve that distinction in the [[medication discrepancy::The medication discrepancy concerns the reported missed dose and relevant records, not an assumed deliberate refusal.]] report if the process requires one. I will describe what you told me without adding a motive or an administration event I did not observe.
Mr. Ahmed | If the nurse tells us something I do not understand, can you ask them to repeat it while I am still on the line?
Rosa | Yes. We can ask about the [[dosing interval::The dosing interval is the time between doses; unclear professional directions should be clarified rather than guessed.]] or any other unclear wording, and repeat the instructions back. Clarifying professional advice is different from making up the advice ourselves.
Mr. Ahmed | And if they do not answer? I do not want to sit here all day with the question still unresolved.
Rosa | We should use the approved [[out-of-hours contact::The out-of-hours contact is one possible designated alternative; the actual plan determines which backup route applies.]] or other backup route when applicable. If there is an urgent or emergency concern, we must follow that route without waiting for a routine callback.
Mr. Ahmed | Please do not mark medicine taken just because we discussed it or tried to call.
Rosa | I will not. [[Administration::Administration is the actual giving or application of medicine under the appropriate role, not discussion or a telephone attempt.]] has not happened through me. My note will describe the reported missed dose, the contact attempt, and any actual response, according to the recording procedure.
Mr. Ahmed | Thank you for explaining the difference. Let us contact the nurse now, with the question and the medicine information ready for them.
Rosa | We will follow the plan and clarify any [[follow-up instruction::A follow-up instruction must come from the appropriate professional and be understood accurately before it is recorded or followed.]] we receive. Until qualified advice is obtained, I will not give you a guessed answer about doubling or replacing the dose.''',
    transfer_title='Route a question about a changed label',
    transfer_setup='A reminder-only worker notices that the client reports different directions on a new dispensing label. The worker has not verified the difference. The plan names the supplying pharmacy as the advice contact.',
    transfer='''Worker: "You are reporting a possible medication ___." | discrepancy | The reported difference between directions requires clarification, not an assumed corrected dose.
Client: "Please help me contact the supplying ___." | pharmacy | The supplied plan specifically names the supplying pharmacy as the advice contact.
Worker: "My assigned support is limited to ___." | reminders | The fictional role allows reminders rather than dose decisions or administration.
Worker: "The reported difference is not yet ___." | verified | The worker has not confirmed the reported difference and should preserve that uncertainty.''',
))

BOOK['units'].append(unit(
    title='Meals, preferences, and unresolved restrictions',
    scene='Offer a choice without guessing about restrictions',
    skill='Acknowledge a food preference, explain an unresolved restriction, and offer an approved alternative without pressure.',
    brief='Caregiver Daniel is supporting Ms. Park with breakfast. Her actual plan lists two approved options, labeled A and B in this teaching case. She dislikes A and asks for food C, which is not listed. Daniel does not know whether C meets the documented restrictions. B is available, and the coordinator can clarify C through the appropriate process. The exercise does not specify ingredients or clinical dietary requirements. Daniel must not guess that C is suitable, pressure Ms. Park to eat A or B, or invent an ingredient substitution.',
    cast='Ms. Park | Client\nDaniel | Caregiver',
    culture=('Food is personal, not merely a task', 'Preferences can involve taste, culture, routine, religion, and comfort. Ask the person rather than infer a preference from a name or background. Explain an unresolved restriction without presenting the person as troublesome or treating the approved alternative as compulsory.'),
    a='''Which option is approved and available besides A? | B | C | Every requested food | No alternative | The brief explicitly states that B is an approved option and is available.
What is known about C? | It is requested but its suitability is unconfirmed. | It is definitely prohibited for every client. | It meets all documented restrictions. | It can be substituted without checking. | C is unlisted and Daniel lacks the information needed to confirm suitability.
What must Daniel avoid? | Guessing suitability or pressuring the client to eat | Acknowledging the preference | Asking the coordinator to clarify | Offering available option B | The scenario requires respect for choice and clarification rather than an invented dietary decision.''',
    vocabulary='''meal support | Agreed assistance with preparing, serving, or managing a meal. | provide meal support
approved option | A choice confirmed within the relevant plan or process. | offer an approved option
dietary restriction | A documented limit on particular foods, ingredients, or intake. | verify a dietary restriction
food preference | A person's stated liking or choice concerning food. | ask about a food preference
allergen | A substance capable of triggering an allergic reaction in a susceptible person. | identify a listed allergen
food allergy | An immune-system reaction to a particular food. | distinguish a food allergy
intolerance | Difficulty tolerating a food, distinct from a food allergy. | clarify a reported intolerance
ingredient list | The listed components of a food product. | check the ingredient list
cross-contact | Unintended transfer of an allergen between foods or surfaces. | report a cross-contact concern
texture modification | A prescribed or assessed change to food consistency. | follow specified texture modifications
dysphagia | Difficulty swallowing; assessment and management require qualified guidance. | refer a dysphagia concern
fluid restriction | A clinically directed limit on fluid intake. | clarify a documented fluid restriction
portion | A specified or served amount of food. | confirm the agreed portion
substitution | Replacement of one food or ingredient with another. | verify a proposed substitution
meal plan | The relevant agreed arrangement for food and meals. | follow the meal plan
preparation method | The way food is prepared, which may affect suitability. | check the preparation method
label verification | Checking relevant product-label information through the required process. | complete label verification
expiry date | A stated product date whose meaning depends on the type of label and local rules. | check the expiry date
storage instruction | Direction about how a food should be kept. | follow storage instructions
food safety | Practices intended to prevent harm from food. | follow food safety procedures
appetite | Desire or willingness to eat. | report a change in appetite
intake record | A record of relevant food or fluid consumed under the care plan. | complete an intake record
suitability | Whether an option meets the person's applicable needs and restrictions. | confirm suitability
nutrition professional | An appropriately qualified professional advising on nutritional needs. | consult a nutrition professional''',
    precision='Dislike, allergy, intolerance, and swallowing difficulty are not interchangeable. Use the actual recorded information and the person\'s words. Recognizing these terms does not authorize a caregiver to diagnose a problem or change a clinically directed restriction.',
    precision_extra='An unlisted food is not automatically forbidden forever, but it is not confirmed suitable in this scenario. The worker can seek clarification and offer B without forcing acceptance. No generic ingredient swap is supplied or authorized by the exercise.',
    phrases='''Acknowledge the preference | I understand that you do not want option A today.
Offer the known alternative | Option B is available and is included in your plan.
Keep the offer voluntary | Would you like B while we clarify your other request?
Name the uncertainty | I cannot yet confirm whether C meets the recorded restrictions.
Avoid a diagnosis | I will not guess why a restriction is in the plan.
Explain the check | We need the relevant details checked before treating C as suitable.
Ask the coordinator | Can you clarify this request through the appropriate process?
Separate two facts | C is not listed; that does not tell us that it is permanently prohibited.
Respect a refusal | I will not pressure you to choose an option you do not want.
Avoid an improvised substitute | I cannot assume a different ingredient solves the problem.
Clarify the full preparation | Does the confirmation cover how the food is prepared as well?
Keep terms distinct | A preference is different from an allergy or a prescribed restriction.
Check the record | I will use the current plan, not an older menu I remember.
Report a change | I will report a relevant change in appetite through the agreed route.
Record actual intake | I will record what was actually eaten, not what was offered.
Close the request accurately | C remains unconfirmed until the appropriate clarification is received.''',
    notes='''Do not want today | Describes the current preference without making it permanent.
Would you like | Offers B without turning availability into an obligation.
Cannot yet confirm | Identifies a knowledge gap, not a universal prohibition.
Relevant details | Leaves clinical interpretation to the appropriately qualified person.
What was actually eaten | Distinguishes intake from preparation, serving, and an offer.
Until clarification | States the unresolved status without promising a favorable answer.''',
    d='''Which offer is appropriate? | B is available and approved; would you like it while we clarify C? | You must eat B because I offered it. | C looks harmless, so no check is needed. | Disliking A proves a food allergy. | The first offer combines a confirmed alternative with choice and an appropriate clarification step.
Which record would be inaccurate? | Ate B, when B was only offered | Declined A today | Requested C; suitability unconfirmed | B available under the plan | An offer does not establish consumption and must not be recorded as intake.
Which statement correctly describes C? | Unlisted and not yet confirmed suitable | Automatically prohibited for life | Confirmed suitable because requested | Approved if one ingredient is removed without advice | The supplied information establishes uncertainty, not a permanent ban or an approved substitution.
Which distinction matters? | Preference, allergy, intolerance, and clinical restriction have different meanings. | Every dislike is an allergy. | Every texture change is a personal preference. | A familiar recipe overrides the current plan. | Accurate terminology prevents a preference or unsupported assumption from replacing the actual documented requirements.''',
    dialogue='''Ms. Park | I do not want option A this morning, Daniel. I had it yesterday and would much rather have the food marked C on my shopping list.
Daniel | I understand your [[food preference::The food preference is Ms. Park's stated choice, not evidence of an allergy or a clinical restriction.]]. Option B is available and listed in your plan, but I need clarification before I can confirm whether C meets the recorded restrictions.
Ms. Park | Nobody said C was banned. Are you telling me that I can never have it?
Daniel | No. I am saying its [[suitability::Suitability remains unconfirmed; the absence of C from the plan does not establish a permanent prohibition.]] is unconfirmed in the information I have. That is different from a permanent prohibition. We can ask the coordinator to clarify the request through the appropriate process.
Ms. Park | Could you simply change one ingredient? People often make a small change to a recipe when someone has a dietary requirement.
Daniel | A [[substitution::A substitution changes the food or ingredient but does not automatically satisfy an unknown restriction.]] might not address the actual restriction. I do not have enough information to choose one safely, and I should not invent an adjustment just because it sounds reasonable.
Ms. Park | I appreciate that explanation. I mainly want something different today, not an argument about whether I am being sensible about breakfast.
Daniel | I hear that. The current [[meal plan::The meal plan identifies A and B as approved options; it does not remove the person's right to express a different preference.]] gives us A and B as approved options, and B is here. Would you like B while the other request is checked, or would you prefer to discuss the choice further?
Ms. Park | Please ask about C first. I might choose B afterward, but I do not want it prepared just because it is easier for the schedule.
Daniel | I will not turn an [[approved option::An approved option may be offered, but its status does not compel the client to accept or consume it.]] into a compulsory meal. I can explain what is available and seek clarification without making the decision on your behalf.
Ms. Park | My relative said the label looked fine. Does that count as confirmation, or do we need someone to check it against my actual plan?
Daniel | The relevant [[label verification::Label verification must address the actual requirements through the proper process; a general reassurance is not equivalent.]] needs to match the actual requirements. A general comment that a label looks fine does not tell us which restrictions were checked or by whom.
Ms. Park | Does preparation matter too? A package might not answer every question about the finished meal.
Daniel | Yes, the [[preparation method::The preparation method can affect whether the final food meets requirements; package information alone may be incomplete.]] may be relevant. I will make sure the request describes the food accurately rather than ask for approval of one ingredient while leaving the finished meal unclear.
Ms. Park | Please do not write that I have no appetite. I am hungry; I just do not want the first option you offered.
Daniel | I will keep [[appetite::Appetite concerns desire to eat; rejecting one option does not by itself establish loss of appetite.]] separate from a preference about a particular food. Your words are clear: you are hungry and are asking about an alternative, not reporting that you do not want any food.
Ms. Park | And if I later choose B, the notes should say what I actually ate. Sometimes an offered meal gets recorded as if it was finished.
Daniel | The [[intake record::The intake record concerns actual consumption under the plan, not a meal that was merely offered or prepared.]] should distinguish offered, served, and consumed according to our process. I will not record a full meal as eaten just because it was available or placed in front of you.
Ms. Park | Let us ask the coordinator what needs checking for C. We can decide about B after the response.
Daniel | I will explain the request and the unresolved [[dietary restriction::The dietary restriction must be understood and applied through the appropriate process rather than guessed from the request.]] question. We will preserve your choice and use the actual response, without claiming that an unconfirmed alternative has already been approved.''',
    transfer_title='Offer an approved alternative while checking a request',
    transfer_setup='Lunch options L and M are approved. The client declines L and requests N, which is unlisted. M is available. No confirmation about N or consumption of M has been recorded.',
    transfer='''Worker: "The available approved alternative is ___." | M | The brief identifies M as both approved and available.
Client: "My requested unlisted option is ___." | N | The request concerns N, while L and M are the approved options.
Worker: "Its suitability is currently ___." | unconfirmed | No relevant confirmation about N has been recorded.
Worker: "Offering M does not establish ___." | consumption | The brief contains no evidence that the client ate the offered alternative.''',
))

BOOK['units'].append(unit(
    title='Privacy and family communication',
    scene='A family claim is not verified permission',
    skill='Respond courteously to an unfamiliar caller, protect visit information, and route the request for appropriate verification.',
    brief='Caregiver Nadia receives a call from an unfamiliar woman who introduces herself as June, the niece of a person she names as a client. June asks what happened during the visit. Nadia cannot access the contact record at that moment and cannot verify identity or permission to receive information. The coordinator can handle the request through the approved process. Nadia should not disclose visit details or confirm a care relationship merely because the caller knows a name. She can explain the process and offer the appropriate route without accusing June of dishonesty.',
    cast='June | Unverified caller claiming to be a niece\nNadia | Caregiver',
    culture=('Warmth and privacy can coexist', 'A genuine relative may feel excluded by a verification step. Explain that it protects personal information and applies without an accusation. Being polite does not require disclosing a small detail to prove goodwill, and being careful need not sound hostile.'),
    a='''What is unverified? | The caller's identity and permission to receive information | That Nadia received a call | The existence of a coordinator route | The fact that the caller asked a question | A claimed family relationship does not establish the caller's identity or disclosure authority.
What is unavailable to Nadia? | The relevant contact record | Any ability to speak politely | The caller's stated name | The fact that a visit question was asked | The brief specifically says the contact record cannot be accessed at that moment.
What is the appropriate next step? | Route the request through the coordinator's approved process without disclosing visit details. | Provide one harmless-sounding care detail first. | Treat knowledge of a name as verification. | Declare all relatives permanently barred from information. | The approved process can establish the relevant facts without premature disclosure or an unsupported blanket prohibition.''',
    vocabulary='''confidentiality | Protection of information from inappropriate access or disclosure. | maintain confidentiality
personal information | Information relating to an identifiable person. | protect personal information
disclosure | Making information available to another person. | authorize a disclosure
identity verification | Establishing that a person is who they claim to be. | complete identity verification
permission to receive information | The relevant basis allowing a particular person to receive specified information. | verify permission to receive information
contact record | The approved record of contact details and relevant permissions. | consult the contact record
authorized contact | A person confirmed for a specified communication role. | verify an authorized contact
claimed relationship | A relationship stated by someone but not yet verified. | record a claimed relationship
next of kin | A family-contact description whose legal effect depends on the situation and jurisdiction. | clarify next-of-kin status
representative authority | The established power to act for another person in a defined matter. | verify representative authority
consent record | A record of the person's relevant consent and its scope. | check the consent record
disclosure scope | The specific information a permitted disclosure may include. | limit disclosure scope
need-to-know basis | Access restricted to what is necessary for the relevant authorized purpose. | share on a need-to-know basis
data minimization | Limiting information collection or disclosure to what is relevant and necessary. | apply data minimization
secure channel | A communication route approved for the relevant information. | use a secure channel
callback verification | Returning contact through an established process rather than trusting an incoming claim alone. | follow callback verification
directory information | Contact information obtained from an approved independent source. | use verified directory information
message taking | Recording a relevant message without confirming private details. | use careful message taking
care relationship | The fact that a person receives a particular care service. | protect the care relationship
privacy concern | A question or issue about appropriate information handling. | escalate a privacy concern
information incident | A possible or actual inappropriate handling of protected information. | report an information incident
record availability | Whether the required information can currently be accessed. | check record availability
verification status | Whether the required identity or authority checks are complete. | state verification status
referral route | The approved path for sending a request to the appropriate team. | explain the referral route''',
    precision='Identity and permission answer different questions: who is calling, and what information may be shared with that person? A family label or knowledge of personal facts is not enough to establish both. Use the actual approved verification process.',
    precision_extra='Do not imply that privacy prevents all family communication. The issue is the unverified request now. A relevant consent record or representative authority may permit defined communication, but its existence and scope must be established rather than assumed.',
    phrases='''Acknowledge the request | I understand you would like an update.
Explain the limit | I cannot discuss personal information before the required checks.
Avoid confirming service | I cannot confirm or discuss care arrangements on this unverified call.
Separate the checks | We need to verify identity and permission to receive information.
Avoid an accusation | This is a privacy step, not an accusation about your relationship.
Name the process | The coordinator can handle the request through our approved process.
Offer the route | I can explain how to contact the office through its published contact details.
Limit message taking | I can pass on the request without discussing personal information.
Keep information minimal | Please do not send unnecessary personal documents to me.
Reject a small disclosure | Even a brief visit detail can be private information.
Avoid a blanket refusal | I am not saying that no family communication is possible.
Clarify authorization | Any disclosure must stay within the verified permission.
Use a trusted contact | The office will use the appropriate verification and callback process.
Keep a record accurate | I will record the caller's stated name and request as unverified.
Report an error | If information was shared incorrectly, I will follow the incident procedure.
Close courteously | Thank you for understanding; the coordinator can address the request through the proper route.''',
    notes='''Before the required checks | Explains the present condition rather than a permanent ban.
Cannot confirm | Recognizes that even the existence of care can be private information.
Identity and permission | Names two separate checks that should not be collapsed.
Stated name | Attributes an unverified claim without calling the speaker dishonest.
Within the permission | Keeps authorization specific instead of treating it as unlimited access.
Published contact details | Offers a route without treating an unknown incoming number as trusted.''',
    d='''Which response is most appropriate? | I can explain the approved request route, but I cannot discuss personal information on this unverified call. | Since you know the name, here is the visit summary. | I can confirm breakfast but nothing else. | No family member can ever receive any information. | The response protects the information while preserving a usable route for legitimate communication.
Which fact would not independently establish disclosure permission? | The caller knowing the person's full name | A verified relevant consent record within its scope | Established representative authority for the matter | Completion of the applicable authorization process | Knowing a name is compatible with many relationships and does not establish permission to receive private information.
How should the caller's relationship be recorded now? | Claimed niece; identity and permission unverified | Confirmed legal representative | Authorized for every future disclosure | Fraudulent caller, without further evidence | The record should preserve the claim and uncertainty without granting authority or inventing dishonesty.
What does unavailable permission information mean here? | Nadia cannot verify the requested disclosure at this moment. | Permission definitely never existed. | Any disclosure becomes acceptable. | An unverified phone number is automatically trustworthy. | An unavailable record leaves verification incomplete rather than proving permission absent or supplying it automatically.''',
    dialogue='''June | Hello, my name is June. I am calling about my aunt. I would like to know how the visit went and whether everything was done.
Nadia | I understand you would like an update. Before discussing [[personal information::Personal information includes visit details and may include the fact of a care relationship, so verification must precede disclosure.]], we need the required checks. I cannot confirm or discuss care arrangements on an unverified call.
June | I am her niece. I know her full name and address, and I have spoken to people at the office before.
Nadia | Thank you for explaining. That is a [[claimed relationship::A claimed relationship is the caller's account; knowing personal details does not independently verify identity or permission.]] I can pass on, but I cannot use those details alone to establish identity and permission to receive information.
June | Are you saying you do not believe me? I am only asking a family question, not trying to get hold of a whole medical file.
Nadia | No accusation is intended. [[Confidentiality::Confidentiality protects personal information even when the request sounds ordinary or comes from a possible relative.]] applies to a short update as well as a large record. The coordinator can handle your request through the approved process.
June | Could you at least say whether breakfast was finished? That seems like a small enough detail, and it would reassure me.
Nadia | It would still be a [[disclosure::A disclosure includes a small visit detail; its limited size does not remove the need for an appropriate basis.]]. I cannot share one private detail as a shortcut around the checks. I can explain the contact route without discussing the person's day.
June | I thought my number was already on the list. Can you look it up and tell me whether the office has made a mistake?
Nadia | I cannot access the [[contact record::The contact record is unavailable, so Nadia cannot confirm either existing permission or an error in the record.]] at this moment. That does not mean permission never existed or that anyone made an error; it means I cannot verify it now.
June | Then I would like the office to check. I do not want this conversation recorded as if you have decided that I am not family.
Nadia | I will record your stated name and request, with the [[verification status::Verification status remains incomplete; recording that fact does not deny the claimed family relationship.]] unconfirmed. I will not label the relationship false simply because the checks are not available during this call.
June | What does the office need to establish besides who I am? If I really am the niece, is that not enough?
Nadia | They also need the relevant [[permission to receive information::Permission to receive information is separate from identity and must cover the particular disclosure being requested.]]. A family relationship and authority to receive particular information are not identical. Any verified permission may also have a defined scope.
June | Should I send you photographs of identification and family documents now? I could put them in a message from this phone.
Nadia | Please do not send unnecessary documents to me. [[Data minimization::Data minimization avoids collecting unnecessary personal material and leaves the required evidence to the approved verification process.]] means using only the information needed through the approved route, not gathering extra sensitive material on an improvised channel.
June | I would prefer a clear next step, then. Can I contact the coordinator through the office number I normally use?
Nadia | Use the office's verified published details and its [[secure channel::A secure channel is the approved route for the relevant information, not any channel suggested during an unverified call.]] for the request. The coordinator can explain the checks and the appropriate response without my disclosing visit information here.
June | All right. Please pass on that I asked for an update and would like the relevant permissions checked, not ignored.
Nadia | I can route that request through the approved [[referral route::The referral route gives the request an appropriate next step while preserving confidentiality until verification is complete.]]. I am not ruling out legitimate family communication; I am keeping this call within what I can verify and share.''',
    transfer_title='Respond to an unverified caller claiming to be a son',
    transfer_setup='An unknown caller claims to be a client\'s son and asks for visit notes. The worker cannot access the authorization record. The privacy coordinator handles verified requests through the approved office route.',
    transfer='''Worker: "The caller describes himself as the client's ___." | son | Son is the claimed relationship, not a verified authorization finding.
Coordinator: "Identity and permission remain ___." | unverified | The necessary record is unavailable and the relevant checks are not complete.
Worker: "The requested information is the ___." | visit notes | The supplied request concerns visit notes, which should not be disclosed prematurely.
Coordinator: "Please use the approved ___." | office route | The brief identifies an approved office process for handling and verifying the request.''',
))

BOOK['units'].append(unit(
    title='A handoff the next person can use',
    scene='Completed support and one unresolved arrangement',
    skill='Separate completed tasks from pending work, name the responsible person, and check that the next worker understands the handoff.',
    brief='At 11:00, caregiver Erin finishes a visit. Breakfast support and laundry are complete. A transport query for tomorrow at 10:00 remains pending with coordinator Dev, who is responsible for arranging transport. Incoming caregiver Mateo starts at 15:00. Erin prepares a factual handoff through the approved record and communication route. She must not mark transport complete or transfer booking responsibility to Mateo merely because he is next on the schedule. The handoff should identify the relevant time, current status, responsible person, and route for any further update.',
    cast='Erin | Outgoing caregiver\nMateo | Incoming caregiver',
    culture=('The next shift does not inherit every decision', 'A handoff transfers relevant information and defined responsibilities, not every unresolved task by default. Give the receiver enough detail to understand the situation, and distinguish who needs awareness from who is authorized and assigned to resolve the issue.'),
    a='''What is complete at 11:00? | Breakfast support and laundry | Tomorrow's transport booking | Every possible care need | Mateo's 15:00 visit | The brief explicitly confirms breakfast support and laundry, while transport remains pending.
Who is arranging transport? | Coordinator Dev | Mateo automatically because he is next | Erin's client without any stated arrangement | Any relative who sees the note | Dev is the identified responsible coordinator, so the incoming worker does not automatically become the booking owner.
When does Mateo start? | 15:00 | 10:00 today | 11:00 tomorrow | 9:00 today | The incoming caregiver's start is 15:00, distinct from tomorrow's 10:00 appointment.''',
    vocabulary='''handoff | Transfer of relevant information and defined responsibilities between workers. | give a clear handoff
handover | Another term for a transfer between workers or shifts. | complete a handover
outgoing worker | The person finishing the relevant assignment or shift. | identify the outgoing worker
incoming worker | The person taking the next relevant assignment or shift. | brief the incoming worker
continuity of care | Consistency and coordination of support across people and time. | support continuity of care
completed task | Work actually finished, not merely planned or assigned. | document a completed task
pending item | An issue or action not yet resolved. | highlight a pending item
action owner | The person assigned responsibility for a particular action. | name the action owner
appointment date | The calendar date associated with the appointment. | confirm the appointment date
appointment time | The time of the appointment, distinct from pickup or shift start. | verify the appointment time
shift start | The time the incoming worker begins the assignment. | distinguish the shift start
status update | New information about the progress or state of an item. | request a status update
acceptance of handoff | Confirmation that relevant information and assigned responsibilities were received and understood. | confirm acceptance of handoff
closed-loop communication | An exchange that checks receipt and understanding rather than assuming them. | use closed-loop communication
care diary | A record of care events and relevant updates under local arrangements. | update the care diary
outstanding query | A question still awaiting an answer. | flag an outstanding query
timestamp | The recorded time associated with an event or entry. | preserve the timestamp
late entry | A later record clearly identified as such under the required process. | label a late entry
amendment | A traceable correction or addition to an existing record. | make a traceable amendment
source attribution | Identifying where information came from. | retain source attribution
responsibility transfer | An explicit reassignment of responsibility, not an assumption based on a message. | confirm responsibility transfer
escalation contact | The designated person or service for raising an unresolved concern. | identify the escalation contact
unresolved status | A state in which the relevant question or action remains open. | preserve unresolved status
completion evidence | Information supporting that the specific action actually occurred. | check completion evidence''',
    precision='Complete the handoff is not the same as complete every outstanding task. Mateo needs to know about the pending transport query, but Dev retains responsibility for arranging it unless an actual authorized reassignment occurs.',
    precision_extra='Use the actual date as well as time in a real record; tomorrow can become ambiguous when a note is read later. Keep appointment time, pickup time, outgoing finish, and incoming start separate. Preserve the original record when adding a later update.',
    phrases='''Open the handoff | This is the handoff for the visit ending at eleven.
State completed support | Breakfast support and laundry are complete.
Highlight the open item | The transport query for tomorrow's ten o'clock appointment is still pending.
Name responsibility | Dev, the coordinator, is arranging transport.
Avoid a false transfer | This note does not assign the booking to you.
Separate the times | Your visit starts at fifteen hundred; the appointment is tomorrow at ten.
Clarify confirmation | No transport booking has been confirmed in the current record.
Attribute the status | This is the status available at eleven.
Identify the update route | Please use the approved coordinator route for an updated status.
Check understanding | Can you repeat the unresolved item and who owns it?
Correct an assumption | A query sent to Dev is not a confirmed car booking.
Preserve history | Add a dated update rather than erase the earlier pending status.
Use a precise record | Include the actual appointment date, not just the word tomorrow.
Report only known facts | I cannot describe unobserved events as completed.
Explain escalation | Use the designated escalation contact if the unresolved issue requires it.
Close the loop | We agree on the completed tasks, pending item, responsible person, and contact route.''',
    notes='''Ending at eleven | Anchors the handoff to a particular visit.
Still pending | Makes unfinished work visible without implying neglect or failure.
Is arranging | Names responsibility without claiming that the arrangement is complete.
Does not assign | Prevents awareness from becoming an accidental transfer of duties.
Status available at | Establishes the time boundary of the information.
Add a dated update | Preserves the historical sequence when information changes.''',
    d='''Which handoff is accurate? | Breakfast and laundry complete; transport pending with Dev for tomorrow at 10:00; Mateo starts at 15:00. | Everything complete, including an unconfirmed booking | Mateo must arrange transport because he receives the note | Appointment today at 15:00 | The accurate version preserves task status, action ownership, and the distinct appointment and shift times.
What should a later confirmation do to the record? | Add a traceable update showing the actual new status and time. | Erase the fact that transport was pending at 11:00. | Pretend the booking existed before confirmation. | Change every appointment time to the confirmation time. | A later update should preserve the original history while adding the newly established information.
Which statement confuses awareness with responsibility? | Mateo read the query, so he automatically owns the booking. | Dev is the named action owner. | Mateo needs the relevant current status. | The handoff should identify the update route. | Receiving information does not itself create an authorized reassignment of the transport action.
Which wording avoids time ambiguity in a real record? | The actual appointment date and time | Tomorrow alone in an undated note | Later, with no reference point | At the usual time without verification | An explicit calendar date and time remain interpretable when the record is read on a later day.''',
    dialogue='''Erin | Mateo, I am finishing at eleven. Breakfast support and laundry are complete. There is one transport question that needs to stay visible in the handoff.
Mateo | Please give me the [[pending item::The pending item is tomorrow's transport query, separate from the two support tasks already completed.]] separately from the completed work. I start at fifteen hundred and need to know the current status before my visit, not assume every item is settled.
Erin | The appointment is tomorrow at ten. Dev, the coordinator, is arranging transport, but I do not have a confirmed booking in the record.
Mateo | So Dev is the [[action owner::The action owner is Dev because the scenario explicitly assigns the transport arrangement to the coordinator.]], and I need awareness of the unresolved query. Receiving your message does not mean I should independently make a second booking.
Erin | Exactly. I do not want two people arranging different cars or each assuming that the other has taken responsibility simply because the note was forwarded.
Mateo | Let us keep any [[responsibility transfer::Responsibility transfer requires an explicit appropriate reassignment, not an inference from forwarding or reading a message.]] explicit. Unless the actual assignment changes through the proper process, the booking remains with Dev and I use the designated route for updates.
Erin | I will record the time of this status as eleven. If a confirmation arrives later, it should not make the earlier note look inaccurate.
Mateo | A clear [[timestamp::The timestamp identifies when the recorded pending status applied and helps distinguish it from later developments.]] will help. The note can accurately show that transport was pending at eleven even if a later entry records a confirmed arrangement.
Erin | I also need to replace tomorrow with the actual appointment date in the record. Someone might read the note after midnight or during a later shift.
Mateo | Yes, include the [[appointment date::The appointment date removes the changing reference of tomorrow when the record is read later.]] and ten o'clock time. My fifteen-hundred start is a separate fact; neither the start nor the appointment time tells us the pickup time.
Erin | There is no pickup time to report yet. I should not copy ten into that field just to avoid leaving something blank.
Mateo | Correct. A [[status update::A status update should report confirmed new information; an empty pickup field must not be filled by copying a different time.]] needs actual information from the appropriate source. Until then, an explicit unconfirmed status is better than a plausible but invented time.
Erin | For the completed tasks, I can report what I actually did. I should not use all needs met as a shortcut for breakfast and laundry.
Mateo | Specific [[completion evidence::Completion evidence supports the particular finished tasks and does not establish that every need or unresolved arrangement is resolved.]] is more useful. List the two completed tasks accurately and keep the transport query separate, rather than make a broad statement the record cannot support.
Erin | If Dev sends a booking confirmation, the person receiving it should add the details using the required process, including the source and time.
Mateo | That preserves [[source attribution::Source attribution identifies who supplied the new information so another worker can understand and verify the update.]]. It also lets the next worker distinguish a coordinator confirmation from a client's expectation or a message that only says the request was sent.
Erin | Can you repeat the important points so I know I have not left the responsibility or timing unclear before I finish this handoff?
Mateo | For [[closed-loop communication::Closed-loop communication checks understanding by repeating the relevant facts and allowing correction instead of assuming a message was understood.]]: breakfast and laundry are complete; transport for tomorrow at ten is pending with Dev; I start at fifteen hundred and use the approved update route.
Erin | That is correct. I will put the same facts in the approved record and identify the designated escalation contact if the unresolved issue needs further attention.
Mateo | Then we can confirm [[acceptance of handoff::Acceptance of handoff acknowledges receipt and understanding of the relevant information, not completion of the pending transport arrangement.]]. I understand the completed support, open query, owner, and contact route. We have handed over the information without falsely closing the transport request.''',
    transfer_title='Separate a service query from a completed task',
    transfer_setup='At 12:00, meal support is complete. An equipment-delivery query for Friday at 14:00 is pending with coordinator Ana. The incoming worker starts at 16:00 and has not been assigned the delivery arrangement.',
    transfer='''Outgoing worker: "The completed task is ___." | meal support | The brief confirms meal support, not the equipment delivery arrangement.
Incoming worker: "The query is pending with ___." | Ana | Ana is the named coordinator responsible for the unresolved query.
Outgoing worker: "The delivery query concerns ___." | Friday at 14:00 | Friday at 14:00 is the relevant delivery time, distinct from the incoming shift.
Incoming worker: "My shift starts at ___." | 16:00 | The supplied incoming start is 16:00 and does not transfer arrangement responsibility.''',
))

BOOK['units'].append(unit(
    title='Delays, complaints, and reliable follow-up',
    scene='A late visit needs a clear update and an active response',
    skill='Acknowledge the effect of a delayed visit, qualify the arrival estimate, and confirm the next update without promising unverified cover.',
    brief='At 8:50, caregiver Hana learns that her planned 9:00 visit to Mr. Reed will be delayed. Dispatch estimates arrival between 9:30 and 9:45 but cannot guarantee it. Mr. Reed planned breakfast support for 9:00. Dispatcher Owen is checking an approved backup arrangement and will update the client by 9:10. Hana calls to explain the delay and report the effect on the planned support. No backup is yet confirmed. Neither a callback promise nor an estimated arrival removes the need for the appropriate prompt response to any urgent concern.',
    cast='Mr. Reed | Client\nHana | Caregiver',
    culture=('An apology needs usable information', 'A frustrated person may be asking for reliability rather than an argument about blame. Name the missed expectation, explain what is known, and identify the person handling the next step. Avoid vague reassurance or making the client organize an unverified substitute.'),
    a='''What is the estimated arrival window? | 9:30-9:45 | Guaranteed at 9:30 | Exactly 9:10 | The original 9:00 time | Dispatch supplies a range and explicitly does not guarantee the arrival.
What is due by 9:10? | A client update from dispatch | Guaranteed completion of breakfast support | A confirmed backup in every case | Automatic cancellation of the visit | The commitment concerns communication, not a guaranteed arrival or completed backup arrangement.
What is the backup status at 8:50? | Being checked, not confirmed | Already present at the home | Permanently unavailable | Assigned automatically to a relative | The brief says dispatch is checking an approved arrangement and has not confirmed cover.''',
    vocabulary='''dispatch | The team coordinating worker schedules, travel, and service responses. | contact dispatch
service delay | A service taking place later than scheduled. | report a service delay
arrival estimate | The current best estimate of when someone will arrive. | qualify the arrival estimate
ETA | Estimated time of arrival; not necessarily a guarantee. | update the ETA
arrival window | The range of times within which arrival is currently expected. | give an arrival window
scheduled start | The planned beginning of the visit. | confirm the scheduled start
backup cover | An alternative authorized worker or arrangement for the service. | confirm backup cover
contingency plan | The agreed process for responding to a disruption. | follow the contingency plan
missed visit | A planned visit that does not occur as arranged, as defined by the service. | report a missed visit
time-sensitive need | A need for which delay may have important consequences. | report a time-sensitive need
service impact | The effect of a disruption on the person's actual support. | explain the service impact
welfare concern | A concern about a person's wellbeing requiring the appropriate response. | escalate a welfare concern
update commitment | A promise to provide information by a stated time. | honor an update commitment
contact attempt | An effort to reach someone, distinct from successful contact. | record a contact attempt
confirmed cover | An alternative arrangement verified as accepted and in place as specified. | distinguish confirmed cover from a request
availability check | An inquiry into whether a suitable alternative can be provided. | complete an availability check
complaint | An expression of dissatisfaction requiring the applicable response. | acknowledge a complaint
acknowledgment | Confirmation that a concern or message was received and understood. | give a clear acknowledgment
service recovery | Actions to address the effects of a service problem. | coordinate service recovery
unverified reassurance | A comforting claim not supported by established facts. | avoid unverified reassurance
revised estimate | An updated forecast based on new information. | communicate a revised estimate
follow-through | Completing an agreed action or communication. | demonstrate follow-through
escalation threshold | The condition requiring a concern to move to a designated response route. | follow the escalation threshold
complaint reference | An identifier for tracking a recorded complaint. | provide the complaint reference''',
    precision='An update by 9:10 is not a promise of arrival by 9:10. A 9:30-9:45 estimate is not a guaranteed 9:30 arrival. State the communication commitment, arrival forecast, and backup status as separate facts.',
    precision_extra='Do not assume a relative is available, authorized, or able to replace planned support. Report the actual service impact through the agreed contingency process. Any urgent welfare concern requires its appropriate response rather than waiting for the next routine update.',
    phrases='''Explain early | I am calling at eight fifty because the nine o'clock visit will be delayed.
Apologize specifically | I am sorry that your planned breakfast support will not start at nine.
Give the range | Dispatch currently estimates arrival between nine thirty and nine forty-five.
Qualify the estimate | That is an estimate, not a guaranteed arrival time.
Name the impact | I understand that you planned breakfast around the nine o'clock visit.
Explain the action | Dispatch is checking an approved backup arrangement.
Keep status honest | The backup has not yet been confirmed.
Name the owner | Owen in dispatch is coordinating the response.
Commit to information | Dispatch will update you by nine ten.
Avoid an unsupported substitute | I will not assume a relative can cover the visit.
Report a relevant concern | I will pass on the effect on your planned support now.
Keep urgent needs separate | An urgent concern should use the appropriate route without waiting for that update.
Acknowledge dissatisfaction | I understand why the uncertainty is frustrating.
Record the complaint | I will pass your complaint through the service's process.
Distinguish contact outcomes | A call attempt is not the same as speaking with you.
Close with the facts | The visit is delayed, cover is unconfirmed, and the next update is due by nine ten.''',
    notes='''Calling at eight fifty | Shows when the information was communicated relative to the scheduled visit.
Currently estimates | Signals that the forecast may change and has a specific source.
Has not yet been confirmed | Avoids implying that an availability check is an accepted arrangement.
By nine ten | Sets the latest promised update time, not an arrival guarantee.
Pass on the effect | Focuses on practical support needs rather than defending the schedule.
Appropriate route | Keeps urgent response separate from routine complaint and update processes.''',
    d='''Which update is accurate at 8:50? | Arrival is estimated at 9:30-9:45; backup is being checked; dispatch will update by 9:10. | Arrival is guaranteed at 9:10. | A backup is confirmed because someone is checking. | No support was expected before 9:45. | The accurate version preserves the estimate, pending backup, and separate communication commitment.
What is wrong with saying a relative will cover? | No relative's availability, suitability, or authorization is established. | Relatives can never help under any care plan. | The client has already agreed to it. | Dispatch has confirmed it in the brief. | The proposed substitute is unsupported; the scenario does not establish who can provide authorized cover.
What should a failed call be recorded as? | A contact attempt, not a completed client update | Client fully informed | Complaint resolved | Visit completed | An attempted call does not establish that the person received and understood the information.
What if an urgent welfare concern becomes apparent? | Use the appropriate urgent response without waiting for the routine 9:10 update. | Wait because an update is already promised. | Treat the ETA as proof that no harm is possible. | Ask the client to diagnose the problem first. | A scheduled communication update does not replace the appropriate timely action for an urgent concern.''',
    dialogue='''Mr. Reed | Hana, I was expecting breakfast support at nine. It is eight fifty now. Are you calling because the visit time is changing again?
Hana | Yes, and I am sorry. Dispatch has reported a [[service delay::The service delay means the planned nine-o'clock start will not be met and needs a clear early explanation.]]. The current arrival estimate is between nine thirty and nine forty-five, rather than the scheduled nine o'clock start.
Mr. Reed | Does that mean you will definitely be here at nine thirty? I need to know whether I can rely on the earliest time in that range.
Hana | No. The [[arrival window::The arrival window is an estimated range, not a guarantee that the earliest time will be achieved.]] is an estimate, not a promise of the earliest time. I do not want to give you certainty that dispatch has not confirmed.
Mr. Reed | I planned my morning around help at nine. A later time is not just a small change to the calendar for me.
Hana | I understand the [[service impact::The service impact concerns the delayed breakfast support, not merely an internal scheduling inconvenience.]] on your breakfast support. I will pass that on now so dispatch responds to the actual need rather than treats this only as a travel update.
Mr. Reed | Is someone else coming instead? The last message I received said the office was looking into alternatives, but I never knew what that meant.
Hana | Owen in [[dispatch::Dispatch is the named team coordinating the delayed visit and checking the appropriate alternative arrangement.]] is checking an approved backup arrangement. It is not confirmed yet. Looking for cover and having someone assigned are different stages, and I will not blur them.
Mr. Reed | Please do not tell me to call my daughter as if she is automatically available. She has work, and nobody has asked her about today.
Hana | I will not assume she can provide [[backup cover::Backup cover needs an appropriate verified arrangement; a relative cannot be treated as available or assigned without confirmation.]]. The office needs to follow the approved contingency process, with the actual arrangements and responsibilities established rather than transferred to your family by assumption.
Mr. Reed | When will I hear something definite? Even if the answer is that they are still checking, I do not want to be left waiting without news.
Hana | Dispatch has made an [[update commitment::The update commitment is to contact the client by nine ten, not to guarantee arrival or confirmed cover by then.]] for nine ten. That is the next communication time, not a promise that the visit or a backup will arrive by nine ten.
Mr. Reed | So I should receive an update by then even if they do not yet have a confirmed replacement. That distinction was not clear to me before.
Hana | Correct. A [[revised estimate::A revised estimate may report new timing, but it must remain qualified unless an actual commitment is confirmed.]] or an honest pending status is more useful than silence. The update should explain what is known, what remains open, and what action is continuing.
Mr. Reed | I want the complaint recorded too. My concern is not that one journey ran late; it is that I cannot plan around uncertain support.
Hana | I will pass that [[complaint::The complaint concerns unreliable support and communication, and should be recorded without reducing it to a travel inconvenience.]] through the service process, including the effect you have described. Recording dissatisfaction does not replace the immediate work to address today's delayed support.
Mr. Reed | And if a more urgent problem comes up before nine ten? I do not want the scheduled callback to become a reason nobody responds.
Hana | An urgent [[welfare concern::A welfare concern requiring urgent action must use the appropriate response route instead of waiting for a routine update.]] needs the appropriate local response without waiting for that callback. The communication timetable must not override the service's urgent or emergency procedure.
Mr. Reed | Please record the original nine o'clock expectation, arrival estimate, unconfirmed backup, and next contact.
Hana | I will record those facts and support the agreed [[follow-through::Follow-through means carrying out the actual promised contact and actions, while preserving their status and avoiding unsupported assurances.]]. The visit is delayed, cover is unconfirmed, Owen is coordinating the response, and dispatch will update you by nine ten.''',
    transfer_title='Keep a later visit estimate separate from its update',
    transfer_setup='At 13:40, a 14:00 visit is delayed. Arrival is estimated between 14:20 and 14:35. Dispatcher Tia is checking approved cover and will update the client by 13:55; cover is not confirmed.',
    transfer='''Worker: "The original scheduled start was ___." | 14:00 | The brief identifies 14:00 as the planned start before the delay.
Client: "The current estimated arrival window is ___." | 14:20-14:35 | The range is the arrival estimate, not a guaranteed start.
Worker: "Tia will provide the next update by ___." | 13:55 | The update commitment is 13:55 and is separate from the later arrival estimate.
Client: "The backup remains ___." | unconfirmed | Tia is checking cover, but the brief does not establish a confirmed arrangement.''',
))
