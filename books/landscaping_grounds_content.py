"""Original Landscaping and Grounds learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='landscaping-grounds',
    title='Landscaping and Grounds English',
    cover_label='ENGLISH FOR GROUNDS WORK AND CUSTOMER VISITS',
    cover_title='Landscaping\nand Grounds',
    cover_size=37,
    tagline='Clear requests. Careful promises.',
    audience='For grounds workers, landscaping crews, site leads, maintenance coordinators, and customer-facing office staff.',
    map_intro='Eight grounds-work conversations: clarify a booking, respect an unconfirmed property limit, identify a requested plant, explain a weather pause, report standing water, query mulch discrepancies, address missed cleanup, and hand over an unfinished bed review.',
    notes_title='Name the work before promising the result.',
    notes_intro='A useful grounds-work conversation identifies the exact area, plant, material, or condition under discussion. It separates the agreed job from a new request, a visible observation from a diagnosis, and a proposed visit from a confirmed booking.',
    field_notes=[
        ('Keep the booked scope visible', 'A request made while the crew is present does not automatically change the work order. Name what is included, what is excluded, and who can review a separate request.', '"Today includes front-lawn mowing and path leaf clearance; the rear hedge needs a separate review."'),
        ('Clarify the plant and the location', 'The tall one or over there can point to more than one plant or area. Confirm the exact subject and location before a qualified person assesses the requested work.', '"You mean the rosemary beside the left flower bed, not the specimen magnolia."'),
        ('Report what you observed', 'A wet area does not establish a broken pipe, and a material label does not prove it matches the approved sample. State the observation, location, time, and unanswered question.', '"At 09:15 I saw standing water beside the east bed near zone 3; the cause is unknown."'),
        ('Separate an update from a booking', 'A weather pause, suggested day, requested callback, and confirmed visit are different stages. Preserve the customer deadline and identify who owns the next communication.', '"Thursday is suggested, not booked; I will request a scheduling update by Wednesday noon."'),
    ],
    scope_note='All sites, customers, plants, materials, times, work orders, and decisions in the cases are fictional. This book teaches workplace English, not horticultural diagnosis, pruning technique, equipment operation, chemical application, land surveying, or legal boundary advice. Follow actual site controls, training, work orders, local requirements, and qualified-lead decisions. The dialogues do not authorize entering disputed land, pruning a plant, changing irrigation, applying products, substituting materials, or resuming paused work.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Grounds Maintenance Workers.',
             url='https://www.bls.gov/ooh/building-and-grounds-cleaning/grounds-maintenance-workers.htm',
             note='Occupational context for landscape maintenance, grounds tasks, and supervised crew work. The scenarios are original fictional conversations, not work instructions.', checked='10 October 2026'),
        dict(title='Occupational Safety and Health Administration. Landscape and Horticultural Services: Hazards and Solutions.',
             url='https://www.osha.gov/landscaping/hazards/',
             note='Context for respecting site conditions, training, and task-specific safety boundaries. No tool-operation or chemical-application procedure is taught here.', checked='10 October 2026'),
        dict(title='University of Minnesota Extension. Pruning Trees and Shrubs.',
             url='https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/pruning-trees-and-shrubs',
             note='Background for distinguishing plant identity, appearance goals, and qualified pruning decisions. Regional timing advice and cutting procedures are not reproduced as learner instructions.', checked='10 October 2026'),
        dict(title='US Environmental Protection Agency. WaterSense: Sprinkler Spruce-Up.',
             url='https://www.epa.gov/watersense/sprinkler-spruce-up',
             note='Terminology context for irrigation components and observed pooling that warrants review. The book does not diagnose a leak or direct system testing or repair.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Confirming the booked grounds work',
    scene='A hedge request during a lawn visit',
    skill='Explain the current work order, acknowledge an additional request, and refer it without inventing a price or appointment.',
    brief='At Oak Court, worker Asha explains the booked work to resident Ben. Today includes front-lawn mowing and path leaf clearance. Ben asks the crew to shape the rear hedge as well. Hedge work is excluded from this booking. The office can review a separate request, but no price, date, or approval is confirmed. Asha must preserve the existing work scope while passing on the hedge request accurately, without implying that a quick favor is automatically covered.',
    cast='Ben | Resident\nAsha | Grounds worker',
    culture=('Acknowledge the request before explaining the limit', 'A resident may see the crew on site and assume an additional task is easy to include. Explain the current work order in concrete terms, then identify the separate review route. A clear boundary can remain helpful without criticizing the resident for asking.'),
    a='''What is included today? | Front-lawn mowing and path leaf clearance | Rear-hedge shaping only | Every outdoor task at Oak Court | Tree removal and irrigation repair | The booking names front-lawn mowing and path leaf clearance as the included work.
Which task does Ben add? | Rear-hedge shaping | Front-lawn mowing already listed | Path leaf clearance already listed | A confirmed tree removal | Ben requests shaping of the rear hedge beyond the current booking.
What can Asha offer? | Office review of a separate request, with no confirmed price or date | Immediate free hedge work | A guaranteed appointment tomorrow | Approval of any extra task | The office can review the additional request, but its terms and timing are not confirmed.''',
    vocabulary='''work order | Record specifying the tasks assigned for a particular job. | check the work order
booked scope | Work included in the agreed booking. | confirm the booked scope
grounds maintenance | Upkeep of outdoor areas and landscape features. | discuss grounds maintenance
front lawn | Grassed area at the front of the property. | identify the front lawn
mowing | Cutting grass as part of the specified lawn task. | confirm the mowing task
path | Defined walking route through an outdoor area. | identify the path
leaf clearance | Removal of fallen leaves from the specified area. | confirm path leaf clearance
rear hedge | Row of shrubs at the back of the site. | identify the rear hedge
hedge shaping | Work intended to change or maintain a hedge's form. | request hedge shaping
included task | Activity explicitly covered by the booking. | name the included tasks
excluded task | Activity outside the current agreed work. | explain the excluded task
additional request | New work requested beyond the existing arrangement. | record an additional request
separate quotation | Price proposal for work outside the current booking. | request a separate quotation
site visit | Attendance at a location for defined work or assessment. | confirm the site visit
crew | Group of workers assigned to the job. | brief the crew
grounds lead | Person supervising or assessing grounds work. | consult the grounds lead
office review | Assessment of a request by the coordinating office. | refer for office review
scope change | Amendment to the agreed work content. | seek approval for a scope change
task authorization | Permission to carry out the specified work. | confirm task authorization
service date | Day on which agreed work is scheduled. | confirm the service date
price estimate | Provisional cost figure for specified work. | distinguish a price estimate
confirmed booking | Arrangement explicitly agreed and entered through the actual process. | verify a confirmed booking
request handoff | Transfer of a new request to the responsible person. | complete a request handoff
completion claim | Statement that assigned work has been finished. | avoid an unsupported completion claim''',
    precision='The current booking includes front-lawn mowing and path leaf clearance, not rear-hedge shaping. Referring Ben to the office preserves the additional request but does not approve it, price it, or book it for another day.',
    precision_extra='A task can be outside the booking even when the crew is already on site. Do not infer that it is free, quick, technically appropriate, or authorized. The conversation clarifies scope; it does not establish that the booked tasks have been completed.',
    phrases='''Acknowledge the request | I understand you would like the rear hedge shaped as well.\nName the booking | Let me confirm today's work order.\nState the first task | Front-lawn mowing is included.\nState the second task | Path leaf clearance is included too.\nName the exclusion | Rear-hedge work is outside this booking.\nKeep the request specific | You are asking for the rear hedge, not the front lawn.\nExplain the review route | The office can review a separate request.\nAvoid a price promise | I do not have a confirmed price for that work.\nAvoid a date promise | No service date is confirmed for the hedge.\nAvoid an informal addition | I cannot add it as a quick favor to today's scope.\nAsk permission to relay | Would you like me to pass the hedge request to the office?\nSeparate review and approval | A review request is not task authorization.\nPreserve the existing work | Today's listed tasks remain mowing and path leaf clearance.\nAvoid a universal refusal | I am explaining this booking, not ruling out future hedge work.\nKeep completion separate | Confirming the scope does not mean the work is finished.\nClose with the next step | I will refer the rear-hedge request with price and timing still open.''',
    notes='''As well | Adds a new request and does not prove it belongs to the original booking.\nIncluded versus excluded | Describes the current agreed scope, not all services the business offers.\nSeparate | Keeps the new hedge request distinct from the existing lawn visit.\nCan review | Offers assessment without promising acceptance or availability.\nNo confirmed date | Avoids turning a possible future service into a scheduled visit.\nQuick favor | Informal wording that can obscure authority, cost, and task suitability.''',
    d='''Which scope explanation matches the booking? | Today covers front-lawn mowing and path leaf clearance, not the rear hedge. | All grounds work is included because the crew is present. | The rear hedge is automatically included if it looks quick. | Only the hedge is booked today. | The work order includes the two named front-area tasks and excludes hedge work.
Which next-step statement is accurate? | I can pass the separate hedge request to the office for review. | I have booked the hedge for tomorrow. | The extra work is free. | Your question authorizes the crew to begin. | Referring the request is available, while approval, cost, and timing remain open.
Which statement overpromises? | The hedge will definitely be shaped today at no charge. | No price is confirmed. | The office can review the request. | The existing scope has not changed. | Neither same-day service nor a free price is supplied or authorized.
What should remain in the handoff? | Rear-hedge shaping requested; separate review needed; price and date unknown. | All outdoor tasks approved and completed. | Hedge task silently added to the mowing order. | A guessed quotation and appointment. | The handoff must preserve the actual request and the unresolved approval, price, and timing.''',
    dialogue='''Ben | Could you shape the rear hedge while you're here? I'd assumed the grounds visit covered that as well as the lawn.
Asha | I can pass that request on. Today's [[work order::Work order specifies today's front-lawn mowing and path leaf clearance, rather than every grounds task.]] lists front-lawn mowing and path leaf clearance; the hedge isn't included.
Ben | Oh, I thought it was a general garden visit. You're saying the lawn and the path are the actual tasks on the booking?
Asha | That's the [[booked scope::Booked scope limits the current visit to the agreed tasks; sharing a property does not add hedge work.]], yes. Being at Oak Court doesn't mean the crew has approval for every outdoor job.
Ben | Please tell the office it's the hedge at the back. I'm not asking for shaping around the front lawn.
Asha | I'll specify [[rear hedge::Rear hedge identifies the exact subject of the additional request and keeps it separate from the front-lawn task.]] shaping, so the location doesn't get confused with the mowing area. The office can review it separately.
Ben | Would that mean an extra bill? I don't want a request for information to be taken as agreement to a price.
Asha | No [[separate quotation::Separate quotation would provide a price for the additional work; none has been given or accepted here.]] is confirmed. Asking for a review doesn't commit you to a charge, and I don't have a price to offer.
Ben | All right. Could it happen later this week, or do they need to check the schedule before you can say?
Asha | The [[service date::Service date for the hedge remains unconfirmed and must not be presented as an appointment this week.]] still needs checking. I can relay your request, but I can't confirm a hedge appointment for this week.
Ben | Please don't tell the other residents it's booked yet. They'll expect someone to turn up if they hear a definite day.
Asha | [[Office review::Office review assesses the new request and is separate from approval or an entered booking.]] is the next step. I'll keep it described as a request until there is an actual arrangement.
Ben | What if I only want a quick tidy? Is that different from asking for the hedge to be shaped?
Asha | The wording doesn't replace [[task authorization::Task authorization is still needed for the actual hedge work; changing the informal description does not add approval.]]. We need the actual work assessed and agreed; I can't add it as a quick favor.
Ben | Then leave it as rear-hedge shaping. I'd rather the office knows what I'm asking for than gets an unclear note.
Asha | I'll make that [[request handoff::Request handoff transfers the accurately described hedge request while leaving approval, price, and date unresolved.]] with the location and requested work. Today's mowing and leaf-clearance tasks stay as they are.
Ben | Can you repeat the two tasks before I speak to the residents? I don't want to say the hedge was missed.
Asha | Mowing is the [[included task::Included task identifies front-lawn mowing, alongside path leaf clearance, as work actually named for today's visit.]] for the front lawn; path leaf clearance is also listed. The rear hedge was not part of today's booking.
Ben | Thanks. Please refer the hedge separately. I'll wait for the office to discuss the price and a possible day.
Asha | Yes. No [[scope change::No scope change is approved; the separate hedge request is only being passed for review.]] has been approved in this conversation. I'll send the request with both price and timing still open.''',
    rehearsal=["Read the included tasks: front-lawn mowing and path leaf clearance.","Repeat Ben's rear-hedge shaping request and the separate office-review route.","Read the price and date answers without adding a quotation or appointment."],
    transfer_title='Refer another additional task',
    transfer_setup='Elm Court has booked front-lawn mowing and driveway leaf clearance. A resident requests side-hedge shaping. It is excluded from the current booking; the office can review it, with no price or date confirmed.',
    transfer='''Worker: "The booked lawn task is ___." | mowing | Mowing is the included lawn task in the existing work order.
Resident: "The additional request concerns the ___." | side hedge | Side hedge is the subject of the separate shaping request.
Worker: "The next step is office ___." | review | Review is the available process for assessing the additional task.
Resident: "The price and date are still ___." | unconfirmed | No quotation or service appointment has been established for the extra work.''',
))


BOOK['units'].append(unit(
    title='Clarifying access and property limits',
    scene='The plan stops at the fence',
    skill='Separate a work-plan limit from an unverified ownership claim and refer an access request without deciding a legal boundary.',
    brief='At Elm View, customer Rosa asks grounds worker Kai to clear a strip beyond the rear fence. Rosa says the strip is probably part of the property, but ownership is unconfirmed. The current work plan ends at the fence. Kai can report the additional request and uncertainty to the office but cannot determine the property boundary, extend the work area, or assume permission to enter. No ownership conclusion, clearance work beyond the fence, or revised plan is established.',
    cast='Rosa | Customer\nKai | Grounds worker',
    culture=('A work limit is not a legal boundary finding', 'A fence can be a clear reference for the booked work without proving ownership of the land beside it. Repeat the customer request respectfully, preserve uncertain wording such as probably, and refer the issue instead of deciding property rights during a maintenance visit.'),
    a='''Where does the current work plan end? | At the rear fence | Beyond the fence to an unknown point | At every area Rosa can see | At a newly approved boundary | The supplied work plan ends at the rear fence and has not been extended.
What is known about the strip's ownership? | It is unconfirmed | Rosa's ownership has been legally established | The neighbor definitely owns it | The worker has completed a survey | Rosa says probably, which does not establish who owns the strip.
What can Kai do? | Flag the request and uncertainty to the office | Decide the legal boundary | Enter and clear the strip automatically | Change the plan without review | Kai can refer the issue but has no authority to determine ownership or expand the work area.''',
    vocabulary='''work-plan limit | Endpoint of the area covered by the current assigned work. | confirm the work-plan limit
rear fence | Fence at the back of the site used as a location reference. | identify the rear fence
boundary | Line separating areas or property interests, requiring appropriate verification. | avoid deciding the boundary
property line | Legally relevant limit of a property, not established here. | request property-line clarification
ownership claim | Statement that land belongs to someone. | qualify the ownership claim
unconfirmed ownership | Ownership not established by the available information. | report unconfirmed ownership
land strip | Narrow area of ground. | identify the land strip
beyond the fence | On the far side of the named fence. | clarify beyond the fence
within the plan | Inside the assigned scope or area. | stay within the plan
adjacent land | Land next to the current site or work area. | distinguish adjacent land
access permission | Authorization to enter a specific area. | verify access permission
entry request | Request to go into an area for work. | refer an entry request
clearance request | Request to remove vegetation or debris from a specified area. | define the clearance request
site plan | Document or drawing identifying site areas and planned work. | consult the site plan
survey | Professional measurement or assessment of land boundaries or features. | distinguish a survey from a visual guess
fence alignment | Position of the fence relative to the surrounding site. | describe the fence alignment
assumption | Belief accepted without adequate verification. | avoid an ownership assumption
qualified statement | Wording that preserves uncertainty or a stated limit. | retain a qualified statement
scope extension | Proposed expansion of the assigned work area or tasks. | request a scope extension
authorized area | Area for which relevant work permission is established. | confirm the authorized area
boundary clarification | Process of resolving uncertainty about the relevant property limit. | seek boundary clarification
office referral | Transfer of a question to the coordinating office. | make an office referral
site restriction | Limit governing access or work at the location. | respect the site restriction
revised plan | Updated work arrangement after the appropriate review and approval. | await a revised plan''',
    precision='The work-plan limit is the rear fence. That fact does not prove the legal property line or ownership of the strip beyond it. Rosa says probably; the uncertainty must remain explicit in the office referral.',
    precision_extra='Access permission, property ownership, and the booked work area are separate questions. The dialogue supplies no legal determination or permission to enter and clear beyond the fence. Refer the request through the actual process before any proposed scope extension.',
    phrases='''Identify the requested area | You mean the strip beyond the rear fence?\nConfirm the task | You would like that strip cleared.\nState the current limit | Our work plan ends at the fence.\nPreserve uncertainty | You said it is probably yours; ownership is not confirmed.\nSeparate plan and title | The work-plan limit does not determine the property line.\nAvoid a legal conclusion | I cannot decide who owns that strip.\nAvoid an access assumption | I cannot assume permission to enter beyond the fence.\nOffer referral | I can flag the request to the office.\nKeep the issue specific | The question concerns the strip beyond the rear fence.\nAvoid a visual shortcut | The fence position alone does not settle ownership here.\nName the required review | The office needs to review the request and the access question.\nPreserve the existing plan | No extension of the work area is approved.\nAvoid claiming a survey | We have not established the boundary through this conversation.\nAttribute the statement | The customer believes the strip may belong to the property.\nKeep the outcome open | No revised plan is confirmed yet.\nClose with the next step | I will pass on the clearance request with ownership and permission still unresolved.''',
    notes='''Probably | Signals uncertainty and must not be rewritten as definite ownership.\nBeyond versus within | Distinguishes the requested strip from the current planned area.\nEnds at | Defines the work-plan limit without establishing a legal property line.\nBelieves | Attributes the claim rather than endorsing it as verified fact.\nPermission versus ownership | These are related but separate questions requiring the appropriate process.\nReferred versus approved | Passing a request to the office does not extend the work area.''',
    d='''Which report preserves the uncertainty? | Rosa believes the strip may be theirs; ownership is unconfirmed. | Rosa definitely owns the strip because she said probably. | The neighbor definitely owns it because it is beyond the fence. | Kai has established the legal boundary. | The correct report attributes Rosa's belief while retaining the lack of confirmation.
What does the rear fence establish in this scenario? | The endpoint of the current work plan. | The definitive legal property line. | Permission to work on both sides. | An automatically revised clearance area. | The fence is the supplied work-plan reference, not a legal ownership determination.
Which action is within Kai's stated role? | Refer the request and access uncertainty to the office. | Perform a boundary survey without qualification. | Clear beyond the fence while ownership is unknown. | Treat the extra strip as already authorized. | Kai can flag the issue but cannot decide ownership or extend the plan.
Which statement wrongly combines separate questions? | If the customer believes it is theirs, entry and clearance are automatically approved. | Work scope and ownership both need clarification. | The current plan ends at the fence. | No revised plan is confirmed. | An uncertain ownership belief establishes neither access permission nor authorization for additional work.''',
    dialogue='''Rosa | Could you clear the strip beyond the rear fence? I think it's probably ours, but I'm not certain.
Kai | You mean the [[land strip::Land strip identifies the narrow area beyond the rear fence, separate from the current planned work area.]] beyond the fence, not the ground on this side? I want to make sure I pass on the correct area.
Rosa | Yes, that narrow strip on the far side. The fence looks as though it's inside the edge, but I haven't confirmed it.
Kai | Thank you for clarifying. The current [[work-plan limit::Work-plan limit is the rear fence, which defines assigned work without deciding the legal property boundary.]] is the rear fence. That tells me where this job ends, but it does not establish the legal boundary.
Rosa | I'd hoped you could include it while the crew was here. Does asking now change the work area?
Kai | It creates an [[additional request::Additional request records Rosa's proposed extra work but does not itself extend the approved area.]] to refer, not an approved extension. I cannot decide the ownership question or assume permission to enter beyond the fence.
Rosa | Please keep probably in the note. I don't want it recorded as though I've established ownership.
Kai | I will keep the [[qualified statement::Qualified statement preserves probably or may, rather than changing an uncertain ownership belief into a verified fact.]] accurate: you believe the strip may belong to the property, but ownership has not been confirmed.
Rosa | Does the fence position help? The planting continues past it, but that may not tell us much.
Kai | The [[fence alignment::Fence alignment is an observed location feature and does not establish ownership or the property's legal limit in this case.]] alone does not settle ownership here. A planting pattern is not enough for me to make a property-line determination either.
Rosa | All right. I'd rather check than ask you to clear land that turns out not to be ours.
Kai | I can make an [[office referral::Office referral passes the precise clearance request and unresolved access question to the coordinating office for review.]]. I will identify the strip, the clearance request, and the uncertainty about ownership and access.
Rosa | Please refer it. I'm asking about clearance, not saying you've agreed to do it today.
Kai | Correct. No [[scope extension::Scope extension would expand the work area beyond the fence, which has not been approved.]] has been approved. The current plan still ends at the fence while the additional request is reviewed.
Rosa | If I find any ownership information, should I send it to the office for their review?
Kai | Yes. The relevant [[boundary clarification::Boundary clarification requires the appropriate review process, not an on-site ownership decision by the grounds worker.]] and access review need the proper process. This conversation is not a survey or a legal decision about the strip.
Rosa | Could you read back the exact area? I don't mean everything behind the property.
Kai | You request clearance of the strip [[beyond the fence::Beyond the fence precisely locates the additional area outside the current work-plan limit.]]. Ownership is unconfirmed, and no permission or extension of the current work area has been established here.
Rosa | That's the request. Please keep the uncertainty in the referral, and I'll wait for the office.
Kai | I will pass it on. A [[revised plan::Revised plan remains unconfirmed; referring the request has not approved entry or clearance beyond the fence.]] is not confirmed yet. The existing work limit remains the fence, with the extra request and its uncertainties clearly recorded.''',
    rehearsal=["Read the fence as the work-plan limit, not a verified property line.","Repeat Rosa's probably or may wording when attributing her ownership belief.","Read the office referral without treating it as permission to enter the strip."],
    transfer_title='Refer another uncertain area request',
    transfer_setup='A work plan ends at a side gate. A customer asks for clearance beyond it and says the area may belong to the property. Ownership and access are unconfirmed; the worker can refer the request to the office.',
    transfer='''Worker: "The current plan ends at the side ___." | gate | The side gate is the stated endpoint of the existing work plan.
Customer: "The area ___ belong to the property." | may | May preserves the customer's uncertain ownership statement rather than asserting a fact.
Worker: "Ownership remains ___." | unconfirmed | No evidence in the scenario establishes who owns the requested area.
Customer: "The next step is office ___." | review | The request can be reviewed, but entry and clearance are not yet authorized.''',
))

BOOK['units'].append(unit(
    title='Clarifying appearance and plant requests',
    scene='Which plant needs attention?',
    skill='Resolve an ambiguous plant reference, describe the requested appearance, and preserve the qualified lead review.',
    brief='At the entrance to Maple House, customer Nina asks worker Tomas to tidy the tall one. Two plants stand nearby: rosemary beside the left flower bed and a specimen magnolia. Nina means the rosemary, not the magnolia. She wants a neater appearance but has not specified a suitable pruning method or extent. A qualified lead must assess whether and how any pruning fits the job. Identifying the plant does not authorize the worker to cut it.',
    cast='Nina | Customer\nTomas | Grounds worker',
    culture=('A description is not a technical instruction', 'Customers often describe the visual result they want rather than a horticultural method. Repeat the plant and location, clarify the appearance goal, and pass the request to the qualified lead without turning casual words into an agreed cutting instruction.'),
    a='''Which plant does Nina mean? | The rosemary beside the left flower bed | The specimen magnolia | Both plants without distinction | An unidentified tree at the rear | Nina clarifies that the rosemary, not the magnolia, is the requested plant.
What result does she request? | A neater appearance | A confirmed removal | A diagnosed disease treatment | A specified cutting depth | Nina describes an appearance goal without specifying a suitable method or extent.
What remains necessary? | Qualified lead review of whether and how pruning fits the job | Immediate cutting because the plant is identified | Approval inferred from a pointing gesture | A promise that any method will work | Plant identification resolves the reference but does not establish authorization or appropriate pruning.''',
    vocabulary='''plant identification | Establishing which plant a person is referring to. | confirm plant identification
rosemary | Named plant in the customer's request. | identify the rosemary
specimen plant | Individual plant grown as a distinct feature. | identify the specimen plant
magnolia | Named plant excluded from this particular request. | distinguish the magnolia
flower bed | Defined area containing ornamental plants. | locate the left flower bed
entrance planting | Plants positioned near the property entrance. | describe the entrance planting
appearance goal | Visual result the customer wants. | clarify the appearance goal
tidy up | Informal request to make something look neater. | clarify what tidy up means
pruning | Selective removal of plant parts for a defined purpose. | refer a pruning request
plant form | Overall shape and structure of a plant. | describe the plant form
growth habit | Characteristic way a plant grows. | assess the growth habit
canopy | Above-ground spread of a woody plant's branches and foliage. | describe the canopy
foliage | Leaves collectively. | refer to the foliage
branch | Woody growth extending from a stem or trunk. | identify the branch
stem | Supporting axis bearing a plant's leaves or growth. | identify the stem
plant health | Condition of the living plant. | assess plant health
qualified assessment | Review by someone with the relevant competence. | request a qualified assessment
pruning extent | Amount and reach of proposed pruning. | clarify the pruning extent
proposed method | Suggested way to carry out a task. | review the proposed method
reference point | Fixed feature used to clarify a location. | use a reference point
cultivar | Named cultivated selection within a plant group, such as lavender Hidcote. | confirm the cultivar name
customer preference | Result favored by the customer. | record the customer preference
botanical name | Scientific plant name identifying genus and species, with cultivar where relevant. | read the full botanical name
cutting authorization | Permission to perform specified cutting work. | confirm cutting authorization''',
    precision='The rosemary is identified, while the magnolia is excluded from this request. Nina wants a neater appearance. Neither that preference nor the clearer plant reference determines a suitable pruning method, pruning extent, or permission to start cutting.',
    precision_extra='Tidy up is useful as the beginning of a conversation, but it is not a precise work instruction. The lead must assess the request and its fit with the job. Avoid converting an informal appearance goal into removal, treatment, or immediate pruning.',
    phrases='''Clarify the reference | Which plant do you mean by the tall one?\nOffer the two candidates | Do you mean the rosemary or the specimen magnolia?\nUse the location | Is it the rosemary beside the left flower bed?\nConfirm the exclusion | You are not asking us to work on the magnolia.\nClarify the result | What would you like to look neater?\nPreserve the wording | I will record a neater appearance as your goal.\nAvoid an invented diagnosis | I have not assessed the plant's health.\nSeparate identification and permission | We have identified the plant, but pruning is not yet authorized.\nRefer the method | The qualified lead needs to assess how to approach it.\nRefer the extent | The amount of pruning is still to be assessed.\nCheck the job fit | The lead also needs to check whether it fits this job.\nAvoid promising removal | I am not recording a removal request.\nRead back the request | Rosemary beside the left flower bed, with a neater appearance requested.\nKeep the other plant separate | The magnolia is outside this request.\nExplain the next step | I will pass the specific request to the lead.\nClose without approval | No cutting decision has been made in this conversation.''',
    notes='''The tall one | An ambiguous reference when more than one plant could fit the description.\nBeside | Gives a location relative to a visible reference point.\nNot the magnolia | Explicitly excludes the other candidate from the request.\nNeater | Describes an appearance preference without specifying a method.\nWhether and how | Preserves both job suitability and the appropriate approach for review.\nIdentified versus authorized | Knowing the subject does not establish permission to perform the task.''',
    d='''Which clarification resolves the ambiguity? | Do you mean the rosemary beside the left flower bed, not the magnolia? | Do you mean both entrance plants need the same work? | Do you want the magnolia beside the left bed tidied? | Do you mean the rosemary should be removed? | The question identifies the intended plant and explicitly distinguishes the nearby alternative.
Which record preserves Nina's request? | Rosemary beside the left flower bed; neater appearance requested; lead review needed. | Magnolia removal approved. | Both plants diagnosed as unhealthy. | Immediate heavy pruning authorized. | The record preserves the plant, appearance goal, and unresolved qualified assessment.
Which statement goes beyond the facts? | The rosemary definitely needs a specific amount cut off today. | The customer means the rosemary. | The magnolia is excluded. | The pruning method remains to be assessed. | Neither a suitable amount nor same-day cutting permission has been established.
What can Tomas confirm now? | The plant and the requested visual goal | The best pruning method | The plant's health diagnosis | That pruning is included and approved | Tomas can clarify the reference and preference while leaving technical and scope decisions open.''',
    dialogue='''Nina | Could you tidy the tall one by the entrance? I mean the one beside that bed; it looks a bit untidy.
Tomas | For [[plant identification::Plant identification establishes the intended subject before the worker records or refers any pruning request.]], do you mean the rosemary beside the left flower bed, or the specimen magnolia? Both are near the entrance.
Nina | The rosemary, please. Not the magnolia. I can see why the tall one wasn't a very useful description with both here.
Tomas | I'll use the left bed as the [[reference point::Reference point uses the left flower bed to distinguish the rosemary from the nearby magnolia.]] and name the rosemary in the note. That should keep the two plants separate.
Nina | I don't know the gardening term for what I want. Neater is probably the best way I can describe it.
Tomas | I can record that [[appearance goal::Appearance goal records the visual result Nina wants without inventing a pruning method or amount.]] without choosing a cutting method. The lead needs to assess what is suitable for this plant and this job.
Nina | That's fine. I don't want someone to take off a large amount just because I said tidy it up.
Tomas | The [[pruning extent::Pruning extent concerns how much work would be appropriate; Nina has not specified or authorized that amount.]] hasn't been decided. We've identified the plant, but not how much, if anything, should be removed.
Nina | And please don't put removal in the note. I want to keep the rosemary; I'm asking about how it looks.
Tomas | I'll preserve that [[customer preference::Customer preference is for a neater appearance, not plant removal or a particular technical treatment.]]. Neater appearance, not removal, and no request to work on the magnolia.
Nina | Does the lead also need to check whether this is part of our booking? I wasn't sure if I could add it while you're here.
Tomas | Yes, [[Scope fit::Scope fit asks whether the requested pruning belongs to the agreed job; the conversation has not settled that question.]] still needs review. An appearance request doesn't automatically add pruning to the work order.
Nina | Could the lead explain what they're proposing before anything is cut? I'd like to know what the result would mean.
Tomas | The [[proposed method::Proposed method remains a matter for qualified assessment rather than a cutting instruction supplied by the customer.]] needs that assessment first. I'm not recommending a technique or promising a particular result from this conversation.
Nina | Please read the location back for me. The entrance has several plants, and I don't want the wrong one included.
Tomas | Rosemary beside the [[left-hand bed::Left-hand bed preserves Nina's specific location and helps the lead identify the correct plant at the entrance.]] at the entrance; neater appearance requested; magnolia excluded. The qualified lead reviews suitability and whether it belongs to this job.
Nina | Yes, that's the one. I'm agreeing that you've understood my request, not agreeing to an amount of cutting today.
Tomas | [[Cutting authorization::Cutting authorization has not been granted merely by clarifying the plant and describing a preferred appearance.]] isn't established by that clarification. I'll keep the request separate from any later decision to proceed.
Nina | Thank you. Send that to the lead, please. I'll wait to hear the assessment rather than choose a pruning amount myself.
Tomas | I'll refer it for a [[qualified assessment::Qualified assessment is the next step for the request; no pruning result, method, or completion is promised.]], with the plant and your appearance goal clear. No pruning has been agreed or reported complete.''',
    rehearsal=["Read rosemary beside the left flower bed, then explicitly exclude the magnolia.","Repeat neater appearance without replacing it with a pruning amount or removal.","Read the lead-review lines, keeping plant identification separate from cutting authorization."],
    transfer_title='Read back the plant request',
    transfer_setup='Complete this exchange using the clarified plant, the excluded plant, the appearance goal, and the unresolved review. Do not add a pruning amount or approval.',
    transfer='''Worker: "You mean the ___ beside the left flower bed." | rosemary | Rosemary is the plant Nina explicitly identifies beside the left bed.
Customer: "The ___ is not part of my request." | magnolia | Nina excludes the nearby magnolia from the appearance request.
Worker: "Your goal is a ___ appearance." | neater | Neater preserves the customer preference without prescribing a pruning method.
Customer: "The qualified lead still needs to ___ it." | assess | Assessment remains necessary before any method, extent, or authorization is established.''',
))

BOOK['units'].append(unit(
    title='Explaining a weather-related change',
    scene='A suggested day is not a booking',
    skill='Explain a work pause, preserve the customer deadline, and distinguish a requested update from a confirmed return visit.',
    brief='At Cedar Court, lead Imani has paused planned outdoor work because of site conditions after rain. Customer Joel has an event on Friday. The office has suggested Thursday as a possible return day, but crew availability is unconfirmed. Imani can relay the event and request a scheduling update by Wednesday noon. Neither the Thursday visit nor completion before the event is promised. The customer needs an accurate status and a clear next communication point.',
    cast='Joel | Customer\nImani | Grounds lead',
    culture=('Give useful certainty at the right level', 'When a customer faces a deadline, a possible day can easily sound like a promise. State the known pause, the suggested day, the unresolved availability, and the requested update separately. Acknowledge the event without guaranteeing work that is not scheduled.'),
    a='''Why is the work paused? | Site conditions after rain | A confirmed cancellation of all future service | A completed job | A customer refusal to pay | The lead has paused the planned work because of the site conditions after rain.
What is the status of Thursday? | Suggested, with crew availability unconfirmed | A confirmed return visit | A guaranteed completion date | A date the customer has rejected | Thursday is only an office suggestion because crew availability has not been confirmed.
What communication can Imani request? | A scheduling update by Wednesday noon | Guaranteed completion before Friday | Automatic work resumption now | A confirmed Thursday appointment | Imani can request the update while preserving the unresolved visit and completion dates.''',
    vocabulary='''weather pause | Temporary stop associated with weather-related conditions. | explain a weather pause
site conditions | Physical circumstances at the work location. | assess site conditions
rainfall | Rain received at a location. | refer to recent rainfall
ground condition | State of the surface or soil at the site. | review the ground condition
waterlogged | Saturated with water beyond normal drainage. | describe a waterlogged area
planned work | Tasks intended for the scheduled visit. | identify the planned work
resumption | Starting work again after a pause. | confirm authorization for resumption
tentative date | Proposed day that is not yet confirmed. | state a tentative date
crew availability | Whether the required workers are available. | confirm crew availability
scheduling update | New information about arrangements for work. | request a scheduling update
return visit | Later attendance to continue or review work. | discuss a return visit
event deadline | Time constraint created by a planned event. | relay the event deadline
completion date | Day on which work is expected or agreed to finish. | avoid an unsupported completion date
weather dependency | Reliance on suitable weather-related circumstances. | explain a weather dependency
provisional suggestion | Idea offered before arrangements are confirmed. | label a provisional suggestion
customer constraint | Limitation affecting what the customer needs. | record a customer constraint
office coordinator | Person arranging visits and communication. | contact the office coordinator
confirmation status | Whether an arrangement is agreed or remains open. | state the confirmation status
update target | Requested time for the next communication. | specify the update target
service interruption | Break in planned service delivery. | explain a service interruption
revised schedule | Changed arrangement for when work occurs. | confirm a revised schedule
outstanding check | Matter still requiring verification. | name the outstanding check
deadline pressure | Urgency arising from a time limit. | acknowledge deadline pressure
work status | Current stage of the assigned work. | report the work status''',
    precision='Thursday is a suggested return day, not a confirmed booking. Wednesday noon is the requested scheduling-update time, not a work-completion deadline. Friday is the customer event. Keep these three time references separate when summarizing the conversation.',
    precision_extra='The lead has paused work because of site conditions after rain. The book does not prescribe when those conditions become suitable. Neither customer urgency nor a calendar suggestion authorizes resumption or establishes that the work will be complete before the event.',
    phrases='''State the pause | The planned outdoor work is paused because of the site conditions after rain.\nAcknowledge the impact | I understand the Friday event makes the timing important.\nState the suggestion | The office has suggested Thursday.\nPreserve uncertainty | Crew availability has not been confirmed.\nCorrect an assumption | Thursday is a possibility, not a booked return visit.\nSeparate the deadline | Friday is your event date, not a completion promise from us.\nRelay the constraint | I will pass the Friday event detail to the office.\nRequest the update | I will request a scheduling update by Wednesday noon.\nDistinguish the two times | Wednesday noon concerns the update, not the work itself.\nAvoid a guarantee | I cannot guarantee completion before the event.\nKeep the pause intact | The suggestion does not authorize work to resume now.\nName the unresolved check | Availability still needs to be checked.\nAvoid inventing a cause | I am reporting the site conditions, not diagnosing a drainage fault.\nRepeat the current status | Work is paused and no return date is confirmed.\nPreserve customer planning | Please do not treat Thursday as a confirmed arrangement yet.\nClose with the handoff | I will relay your event deadline and the requested update time.''',
    notes='''Paused | Describes the present work status without claiming permanent cancellation.\nSuggested | Marks a proposed date rather than an agreed appointment.\nBy Wednesday noon | Gives the requested communication deadline, not a service deadline.\nBefore Friday | Refers to the desired timing relative to the customer event.\nUnconfirmed | Leaves availability open without implying that it is definitely unavailable.\nRequest versus promise | Asking for an update does not prove the office has accepted that deadline.''',
    d='''Which explanation preserves all three dates? | Thursday is suggested; an update is requested by Wednesday noon; the event is Friday. | Work is guaranteed Wednesday and the event is Thursday. | Friday is the confirmed return day. | Wednesday noon is the guaranteed completion time. | The explanation assigns each date its actual role without converting suggestions into promises.
Which statement should be corrected? | Thursday is definitely booked and everything will be finished before Friday. | Crew availability remains unconfirmed. | Work has been paused. | The customer has a Friday event. | Neither the Thursday booking nor completion before the event is confirmed.
What should Imani send the office? | The Friday event detail and a request for a scheduling update by Wednesday noon | A report that the customer accepted completed work | An invented resumption authorization | A confirmed Thursday appointment | These are the customer constraint and communication request actually supported by the case.
What does unconfirmed availability mean? | The crew arrangement still needs verification | The crew is definitely free | The crew is definitely unavailable | The work is already complete | Unconfirmed preserves the open check rather than asserting availability or unavailability.''',
    dialogue='''Joel | I heard Thursday mentioned. We've got an event on Friday; can I tell the organizer the work will be finished?
Imani | Not yet. The current [[work status::Work status is paused because of site conditions after rain; the conversation does not establish completion or resumption.]] is paused because of the site conditions after rain. I understand why you need a reliable answer before your event.
Joel | Thursday sounded definite when I heard it. Is a crew assigned, or was it only a possible day?
Imani | It is a [[tentative date::Tentative date describes Thursday as a suggestion rather than a confirmed return visit or guaranteed completion date.]]. The office suggested Thursday, but crew availability has not been confirmed. Please do not treat that suggestion as a booked visit.
Joel | I'm not asking you to ignore the site conditions. I just need to know what arrangements I can rely on.
Imani | I will relay that [[customer constraint::Customer constraint is the Friday event, which affects planning but does not authorize resuming work or promise completion.]] clearly. Friday is your event date; it is not a completion commitment that we have made, and I should keep those separate.
Joel | Can we ask for an update before Wednesday lunchtime? Friday morning would be too late for my planning.
Imani | I can request a [[scheduling update::Scheduling update is the information Imani can request by Wednesday noon; it is not the work itself.]] by Wednesday noon. That is a request for the next communication, not a promise that the work will happen then.
Joel | So Wednesday noon is the update request, and Thursday is still only the possible return day.
Imani | Exactly. The [[confirmation status::Confirmation status keeps Thursday open because the office has not established crew availability or a confirmed return arrangement.]] of Thursday remains open. The office still needs to check availability before a return arrangement can be confirmed.
Joel | Please include the Friday event in the message. That's why I need the scheduling answer.
Imani | Yes. I will include your [[event deadline::Event deadline records Friday as the customer's planning constraint without treating it as an agreed service deadline.]] and the requested Wednesday-noon update together. The message will say the timing matters for your event, without guaranteeing a result.
Joel | Has the pause actually been lifted, or is Thursday just a calendar suggestion at this stage?
Imani | The suggestion does not establish [[resumption::Resumption means restarting paused work; a proposed date alone does not authorize it or establish suitable conditions.]]. The pause remains the current status, and I will not present a calendar suggestion as permission to restart the work.
Joel | I'd prefer an honest unresolved update to a date that sounds certain and then falls through.
Imani | I will make the [[outstanding check::Outstanding check is crew availability, which remains unresolved and must not be silently treated as confirmed.]] explicit. Crew availability is unconfirmed, and no return date or completion date has been agreed in this conversation.
Joel | Please request Wednesday noon and flag Friday. I won't tell the organizer Thursday is booked.
Imani | I will pass both details to the [[office coordinator::Office coordinator is the scheduling contact who receives the event constraint and the requested communication time.]]. Requesting the update does not mean the office has already accepted the deadline, so I will describe it accurately.
Joel | Thanks. Work paused, Thursday suggested, update requested by Wednesday noon, event Friday. I'll keep those separate.
Imani | That is the correct summary of the [[service interruption::Service interruption refers to the paused planned work, with a suggested return day and an unresolved scheduling arrangement.]]. I will relay it without adding a booking or a promise that everything will be finished before your event.''',
    rehearsal=["Read the three time references: Wednesday-noon update, suggested Thursday, Friday event.","Repeat requested and suggested with emphasis; neither means confirmed.","Read the current pause without implying the calendar suggestion authorizes resumption."],
    transfer_title='Separate three time references',
    transfer_setup='Complete the customer update. Keep the pause, the suggested Thursday visit, the requested Wednesday-noon update, and the Friday event in their correct roles.',
    transfer='''Lead: "The work remains ___ because of the site conditions." | paused | Paused is the stated work status after rain affected the site.
Customer: "Thursday is ___, not confirmed." | suggested | Thursday was proposed by the office, but crew availability remains unconfirmed.
Lead: "I will request an update by Wednesday ___." | noon | Noon completes the requested Wednesday communication time, not a work deadline.
Customer: "My event is on ___." | Friday | Friday is the event date and does not establish a completion guarantee.''',
))

BOOK['units'].append(unit(
    title='Reporting site observations without diagnosis',
    scene='Standing water beside the east bed',
    skill='Report a visible condition with its location and time, and respond to a suspected cause without presenting it as confirmed.',
    brief='At 09:15, worker Leila sees standing water beside the east bed near irrigation zone 3 at Birch Court. Customer Evan asks whether a pipe is broken. The cause is unknown, and no irrigation-system check has occurred. Leila can report the observation and refer it to grounds lead Marco, who can arrange review. She must not turn the location near a zone into proof that the zone, a pipe, or another component has failed.',
    cast='Evan | Customer\nLeila | Grounds worker',
    culture=('Answer the concern without adopting the diagnosis', 'A customer may offer a possible explanation in the form of a question. Acknowledge the concern, then separate what you saw from what has not been checked. Specific location and time details make the referral useful without requiring a guessed technical answer.'),
    a='''What did Leila observe? | Standing water beside the east bed at 09:15 | A confirmed broken pipe | A completed irrigation repair | A failed controller diagnosis | The observation is standing water at the stated place and time, not a confirmed fault.
What has not occurred? | An irrigation-system check | A customer question | A visible water observation | Identification of the east bed | The case explicitly says no system check has occurred.
Who can arrange review? | Grounds lead Marco | A worker who has already diagnosed the pipe | A confirmed repair crew arriving now | The customer through an already booked repair | Marco is the lead who can arrange review, but no repair appointment is confirmed.''',
    vocabulary='''standing water | Water collected on a surface rather than visibly draining away. | report standing water
pooling | Accumulation of water in a particular area. | describe observed pooling
irrigation | Artificial supply of water to plants or land. | discuss the irrigation system
irrigation zone | Defined area or circuit served as part of an irrigation system. | identify irrigation zone 3
sprinkler head | Outlet that distributes irrigation water. | identify a sprinkler head
irrigation line | Pipe or tubing carrying water within an irrigation system. | refer to an irrigation line
valve | Component controlling flow through a line. | identify a valve
controller | Device managing system operation settings or timing. | refer to the controller
drainage | Movement or removal of water from an area. | describe a drainage concern
runoff | Water flowing over a surface. | report visible runoff
saturation | Condition of material holding a high amount of water. | describe visible saturation
east bed | Planting area on the east side of the identified site. | locate the east bed
observation time | When the reported condition was seen. | include the observation time
visible condition | State that can be directly seen. | report the visible condition
suspected cause | Possible explanation that has not been established. | distinguish a suspected cause
confirmed fault | Problem established through appropriate checking. | avoid claiming a confirmed fault
system check | Examination of the relevant system. | request a system check
leak | Escape of water from a system or container. | refer a possible leak concern
pipework | Pipes collectively within a system. | refer to the pipework
inspection request | Request for examination of a condition or system. | pass an inspection request
precipitation rate | Irrigation application depth per unit of time, commonly millimeters or inches per hour. | compare precipitation rates
review owner | Person responsible for arranging or carrying out a review. | name the review owner
diagnosis | Identification of the cause or nature of a problem. | distinguish observation from diagnosis
distribution uniformity | Measure of how evenly irrigation is applied across sampled positions. | assess distribution uniformity''',
    precision='Standing water is an observation. A broken pipe is a possible explanation raised by Evan, not a finding. Near zone 3 identifies the location; it does not prove that zone 3 or any particular irrigation component is faulty.',
    precision_extra='The useful report includes what was seen, where, when, and what has not been checked. Marco can arrange review. Do not add a leak diagnosis, repair plan, visit time, or claim that someone has already tested the system.',
    phrases='''Name the observation | I saw standing water beside the east bed.\nGive the time | I noticed it at 09:15.\nLocate the area | It is near irrigation zone 3.\nAcknowledge the concern | I understand why you are asking about a pipe.\nSeparate possibility from finding | A broken pipe has not been confirmed.\nState the limit | I do not know the cause.\nKeep the check status clear | No irrigation-system check has taken place.\nAvoid a location inference | Being near zone 3 does not identify the faulty component.\nRefer the observation | I will report what I saw to Marco.\nName the review route | The grounds lead can arrange a review.\nPreserve the customer question | I will include your question about a possible pipe problem.\nAvoid a repair promise | No repair or visit time is confirmed.\nDistinguish reporting and testing | Passing the report does not mean the system has been tested.\nUse neutral wording | Standing water observed; cause unknown.\nRead back the details | East bed, near zone 3, observed at 09:15.\nClose with the next step | Marco can review the report and arrange the appropriate follow-up.''',
    notes='''Observed | Claims only that the worker saw the condition.\nNear | Locates the observation without establishing a causal connection.\nCould be | Introduces a possibility and should not be repeated later as a confirmed cause.\nNo check yet | Preserves the actual evidence limit at the time of the conversation.\nArrange review | Describes a next step, not a completed inspection or repair.\nCause unknown | Gives a precise limit rather than a vague reassurance.''',
    d='''Which report is supported? | Standing water beside the east bed near zone 3 at 09:15; cause unknown. | Zone 3 has a confirmed broken pipe. | The controller failed at 09:15. | Marco has completed a repair. | Only the visible water, location, time, and unknown cause are established.
How should Leila answer the pipe question? | I cannot confirm that; no system check has occurred. | Yes, because the patch is beside the irrigation zone. | No, because recent rain already explains the water. | The repair is already booked. | The response preserves uncertainty without asserting or excluding an untested cause.
Which detail must not be silently changed? | Near zone 3 must not become a confirmed fault in zone 3. | The east bed remains the location. | The observation time remains 09:15. | Marco remains the grounds lead. | A location reference does not establish that the nearby system zone caused the water.
Which next step is accurate? | Refer the observation to Marco, who can arrange review. | Announce that the system passed inspection. | Promise a same-day repair. | Tell the customer the pipe has been replaced. | The lead can arrange review, while inspection findings and repair arrangements remain unknown.''',
    dialogue='''Evan | There's water beside the east bed. Could a pipe be broken? I'm worried it might be more than a wet patch.
Leila | I noticed the [[standing water::Standing water names the visible condition without identifying the cause or proving a pipe failure.]] at nine fifteen. I can report exactly where it is, but I haven't established what caused it.
Evan | Is that near zone 3 on the irrigation plan? I remember seeing that number beside this part of the garden.
Leila | Yes, near [[irrigation zone::Irrigation zone identifies the nearby numbered area; proximity does not establish that the zone is faulty.]] 3. That gives us a location reference; it doesn't prove that the zone or a particular component caused the water.
Evan | Has anyone checked the system? I don't want to tell the office it's a pipe problem if they've already found something else.
Leila | No [[system check::System check has not occurred, so no test result or confirmed cause can be included in the report.]] has happened yet. I'll include that in the report so it isn't mistaken for an inspection result.
Evan | Please include the time you saw it. The patch may look different by the time someone comes to review it.
Leila | I'll record the [[observation time::Observation time is 09:15, when Leila saw the water; it is not a failure time or inspection appointment.]] as zero nine fifteen, with the east bed and nearby zone number. It isn't a confirmed fault-start time.
Evan | I'm asking about a pipe, not saying I know one's broken. That was just the first explanation that occurred to me.
Leila | I'll keep it as a [[suspected cause::Suspected cause preserves Evan's pipe question as a possibility rather than a diagnosis or established finding.]] raised in your question. The observation itself is standing water, with the cause still unknown.
Evan | Who should get the report? I'd like someone to take the next step rather than have it passed around without an owner.
Leila | Marco, the grounds lead, is the [[review owner::Review owner identifies Marco as the person who can arrange review of the reported condition.]] for this referral. He can arrange the appropriate review of what you've raised.
Evan | So we're asking for it to be checked. That doesn't mean there's already a repair crew booked to come here?
Leila | Correct. We're reporting a [[visible condition::Visible condition is the water Leila observed; reporting it does not establish a repair booking or technical conclusion.]] and requesting review. No repair or attendance time has been confirmed.
Evan | Could the note actually say cause unknown? I don't want a message about a possible leak shortened to leak confirmed.
Leila | Yes. I won't record a [[confirmed fault::Confirmed fault would claim a problem had been established through checking; no such finding exists in the case.]]. I'll retain cause unknown and no system check, alongside what I actually saw.
Evan | Read the location back once, please. There are several beds, and I want the lead sent the right information.
Leila | The [[site location::Site location is beside the east bed near zone 3, which distinguishes this observation from other planting beds.]] is beside the east bed, near zone 3, observed at zero nine fifteen. Your question concerns a possible pipe problem.
Evan | That's right. Please pass it to Marco with the time and the fact that nothing has been checked yet.
Leila | I'll send that [[inspection request::Inspection request asks for review of the observation; it does not mean an inspection or repair has already happened.]]. Marco can arrange review, and any later finding must come from the actual check, not our guess about the cause.''',
    rehearsal=["Read standing water, east bed, near zone 3, and 09:15.","Repeat the possible-pipe question as a question, not a confirmed diagnosis.","Read Marco's role and leave inspection findings and visit timing unresolved."],
    transfer_title='Pass on an observation accurately',
    transfer_setup='Complete the report to Marco. Keep the visible condition, time, location, and unknown cause distinct. Do not turn the customer question into a diagnosis.',
    transfer='''Worker: "I observed standing ___ beside the east bed." | water | Water is the visible condition reported, not a confirmed damaged component.
Worker: "The observation time was ___." | 09:15 | This is when Leila saw the condition, not when a fault began.
Worker: "The area is near zone ___." | 3 | Zone 3 is the location reference, not proof of a faulty zone.
Worker: "The cause is ___; no system check has occurred." | unknown | No examination has established the cause of the standing water.''',
))

BOOK['units'].append(unit(
    title='Checking materials and requested quantities',
    scene='Six bags and the wrong label',
    skill='Compare a delivery with the requested quantity and approved sample, then refer both discrepancies without approving substitution.',
    brief='At Cedar Lane, a front-bed job lists eight bags of dark mulch. Customer Mira approved a dark sample. Worker Dev counts six delivered bags, whose label says natural brown. The delivered material has not been approved as a substitute. Dev cannot promise that six bags will cover the beds or that the labeled color matches the sample. The office will query the supplier about both the two-bag shortage and the apparent color discrepancy.',
    cast='Mira | Customer\nDev | Grounds worker',
    culture=('Separate two discrepancies instead of averaging them away', 'A delivery can have more than one mismatch. State the count and the description separately, and keep each compared with its correct reference. A customer question about making do does not establish coverage, color acceptance, or authority to substitute the material.'),
    a='''What quantity is listed and what arrived? | Eight bags listed; six delivered; two short | Six listed; eight delivered; two extra | Eight listed and eight delivered | Two listed and six delivered | Subtracting six delivered bags from eight listed bags gives a two-bag shortage.
Which description raises a second question? | Natural brown on the delivered label versus the approved dark sample | A confirmed identical color | No label and no sample | A customer-approved replacement already recorded | The delivered label differs from the requested dark description and approved sample.
What is the next step? | Office query to the supplier about both discrepancies | Automatic acceptance of a substitute | A guarantee that six bags cover the beds | A claim that the customer changed the order | The office will query both quantity and description without assuming substitution or coverage approval.''',
    vocabulary='''mulch | Material placed over a soil surface for a specified landscape purpose. | confirm the mulch specification
bag count | Number of bags counted in a delivery. | verify the bag count
requested quantity | Amount stated in the job or order. | compare the requested quantity
delivered quantity | Amount actually received. | record the delivered quantity
shortfall | Amount by which the delivered total is below the required total. | report a two-bag shortfall
material specification | Stated requirements for a material. | check the material specification
approved sample | Example accepted as a reference for the requested product. | compare the approved sample
color description | Words identifying the intended or labeled color. | check the color description
natural brown | Color description on the delivered bags in this case. | record the natural-brown label
dark mulch | Requested mulch description in the job. | confirm the dark-mulch request
product label | Information attached to or printed on the material packaging. | read the product label
supplier query | Question sent to the business providing the material. | raise a supplier query
quantity discrepancy | Difference between expected and actual amounts. | report a quantity discrepancy
description discrepancy | Difference between the requested and delivered descriptions. | report a description discrepancy
substitute material | Product proposed instead of the specified material. | seek approval for substitute material
substitution approval | Agreement to use an alternative product. | confirm substitution approval
coverage | Area that a quantity of material can cover under relevant conditions. | avoid an unsupported coverage promise
material takeoff | Calculation of required material quantities from dimensions and specifications. | check the material takeoff
delivery record | Document or entry describing a delivery. | check the delivery record
order reference | Identifier connecting a query to the relevant order. | include the order reference
replacement request | Request for an appropriate replacement product. | discuss a replacement request
net area | Area requiring material after stated exclusions have been subtracted. | calculate the net area
acceptance | Agreement that delivered material meets the relevant requirement. | distinguish receipt from acceptance
material match | Agreement between a supplied material and its specified reference. | verify the material match''',
    precision='Eight requested minus six delivered leaves two bags short. Separately, natural brown appears on the delivered label while the job and approved sample specify dark mulch. The quantity calculation does not resolve whether the delivered material matches or is acceptable.',
    precision_extra='The case does not supply bed dimensions, application requirements, or a verified coverage calculation. Do not promise that six bags will be enough. Neither physical delivery nor a customer question about using it establishes approval of substitute material.',
    phrases='''State the order quantity | The job lists eight bags.\nState the delivery count | I have counted six delivered bags.\nCalculate the difference | That leaves a two-bag shortfall.\nName the requested material | The specified material is dark mulch.\nRead the delivered description | The delivered label says natural brown.\nUse the sample reference | Your approved sample was dark.\nKeep the issues separate | We have a quantity question and a material-description question.\nAvoid a match claim | I cannot confirm that this matches the approved sample.\nAvoid a coverage claim | I cannot promise that six bags will cover the beds.\nPreserve approval status | No substitution has been approved.\nRefer both discrepancies | The office will query the supplier about both points.\nAvoid changing the order | I am not recording six bags as the requested quantity.\nAvoid assigning blame | The cause of the discrepancy has not been established.\nKeep timing open | No replacement delivery time is confirmed.\nRead back the comparison | Eight requested, six delivered, and natural brown on the label.\nClose with the review route | The supplier query needs to resolve quantity and material before acceptance is assumed.''',
    notes='''Short by two | Expresses the difference between eight expected and six received.\nLabel says | Reports packaging information without claiming a verified visual or technical match.\nApproved sample | Refers to the customer's accepted reference, not any later substitute.\nEnough | A coverage claim requiring more information than the bag count alone.\nBoth | Keeps quantity and material description in the supplier query.\nDelivered versus accepted | Receiving material does not establish that it satisfies the order.''',
    d='''Which calculation is correct? | Eight requested minus six delivered equals two bags short. | Six minus eight means two bags extra. | Eight requested means eight delivered. | Two short means only two were ordered. | Comparing the expected and received counts shows a shortage of two bags.
Which statement preserves the color issue? | The label says natural brown, while the approved sample was dark. | Natural brown is confirmed identical to the approved sample. | The customer approved any available color. | The label has already been corrected. | The statement compares the actual label with the approved reference without claiming a match.
How should Dev answer whether six bags are enough? | I cannot promise coverage from the information we have. | Six is enough if each bag is spread more thinly. | Six should cover it because the label color is similar. | Six covers three quarters of the area regardless of bag volume. | The case lacks the measurements and application information needed for a coverage promise.
What belongs in the supplier query? | Both the two-bag shortage and the material-description discrepancy | Only a request to approve the delivery automatically | An invented replacement arrival time | A claim that the customer changed the sample | Both unresolved differences need review; neither acceptance nor replacement timing is established.''',
    dialogue='''Mira | We expected eight bags of dark mulch. I'm counting fewer, and these labels say natural brown. Can you check?
Dev | I have checked the [[bag count::Bag count is six delivered bags, which must be compared with the eight bags listed in the job.]] and found six. The job lists eight bags, so the delivery is two bags short before we address the description.
Mira | My approved sample was dark. Does natural brown mean someone changed the specification, or don't we know yet?
Dev | I cannot say that. The [[product label::Product label supplies the delivered description natural brown; it does not explain why that material was delivered.]] says natural brown, and the requested material is dark mulch. No approved change has been established.
Mira | If the color is acceptable, could six bags cover the beds? Or are we short of what the job needs?
Dev | I cannot promise [[coverage::Coverage depends on information not supplied here; six bags cannot be declared sufficient simply because they arrived.]] from the count alone. We need to keep the missing quantity separate from the question of whether this material matches what you approved.
Mira | Please keep eight as the ordered quantity. Six is what arrived, not what I asked for.
Dev | I will preserve the [[requested quantity::Requested quantity remains eight bags; receiving six does not amend the original job requirement.]] as eight. The record will show six delivered and two short, not a revised order for six bags.
Mira | Could you include the actual sample in the query? The color word alone isn't the reference I approved.
Dev | I will refer to the [[approved sample::Approved sample is the dark reference Mira accepted; the delivered label has not been verified against it as a match.]] as well as the job description. I am not confirming a match between that sample and the delivered bags.
Mira | What happens next? I don't want the crew using it on the assumption that it's close enough.
Dev | The office will raise a [[supplier query::Supplier query is the agreed next route for investigating both quantity and material description, without assuming acceptance.]] about both points. The query will include the two-bag shortage and the difference between the label and your approved reference.
Mira | Are we ordering a replacement now, or just asking the supplier to explain the delivery?
Dev | No [[replacement request::Replacement request is not yet confirmed as an order or delivery arrangement; the current step is a supplier query.]] has been confirmed as an order. I also do not have a replacement delivery time to give you now.
Mira | All right. I'm asking about options, not accepting a smaller quantity or a different material.
Dev | I will. [[Substitution approval::Substitution approval has not been given; asking about possibilities does not authorize an alternative material.]] is still absent. Your question about making do will not be recorded as acceptance of a different material or a smaller quantity.
Mira | Can you summarize both issues? I don't want the missing two bags to hide the color question.
Dev | The [[quantity discrepancy::Quantity discrepancy is two bags short, while the material-description discrepancy remains a separate unresolved issue.]] is eight requested against six delivered. Separately, the delivered label says natural brown while your approved sample and the job request are dark.
Mira | Please send both points. We still don't know whether the material matches or whether six bags could cover the beds.
Dev | I will keep [[acceptance::Acceptance of the delivery is not established; the office must resolve the quantity and material questions through the supplier.]] open while the office queries the supplier. The count, the material description, and any proposed resolution will remain separate in the message.''',
    rehearsal=["Read eight requested, six delivered, and two bags short.","Compare natural brown on the label with the approved dark sample.","Read the supplier query with both discrepancies and no coverage or substitution promise."],
    transfer_title='Report two delivery discrepancies',
    transfer_setup='Complete the office handoff. Include the original quantity, the delivered count, the resulting shortage, and the unapproved material description.',
    transfer='''Worker: "The job requires ___ bags of dark mulch." | eight | Eight is the requested quantity and remains unchanged by the delivery.
Worker: "We received ___ bags." | six | Six is the delivered count, not a revised order quantity.
Worker: "We are ___ bags short." | two | Eight requested minus six delivered leaves a shortage of two bags.
Worker: "The label says natural ___; substitution is not approved." | brown | Natural brown is the delivered description, which differs from the dark reference.''',
))

BOOK['units'].append(unit(
    title='Responding to finish and cleanup concerns',
    scene='Clippings beside the front steps',
    skill='Acknowledge a specific missed cleanup, identify the included area, and refer correction without expanding the job.',
    brief='After a front-lawn visit at Rowan Court, customer Hazel says the path cleanup was incomplete. Worker Amir can see clippings beside the front steps, which are within the listed cleanup area. The rear patio is excluded from the booking. The lead can organize the missed front cleanup, but no wider task or exact return time is agreed. Amir must acknowledge the visible concern without denying it, declaring it resolved, or adding the rear patio to the job.',
    cast='Hazel | Customer\nAmir | Grounds worker',
    culture=('Acknowledge the specific problem before discussing scope', 'A customer who reports incomplete work needs evidence that the concern has been heard. Name the visible missed area first. Then separate the correction of an included task from a new request, keeping the explanation calm and specific rather than defensive.'),
    a='''What can Amir see? | Clippings beside the front steps | A fully cleared front path | A confirmed damaged patio | A completed return visit | The worker can see clippings in the front-step area identified by the customer.
Which area is included? | The front steps within the listed cleanup area | The excluded rear patio | Every outdoor surface | An unspecified neighboring property | The front steps fall within the listed cleanup area, while the rear patio is excluded.
What can the lead organize? | The missed front cleanup | An automatically expanded whole-property cleanup | A completed correction already recorded | A guaranteed return at an invented time | The lead can organize correction of the missed included work without adding wider tasks.''',
    vocabulary='''clippings | Small pieces of plant material left after cutting. | report remaining clippings
cleanup area | Location included in the agreed clearing task. | identify the cleanup area
front steps | Steps at the front entrance of the property. | locate the front steps
rear patio | Paved outdoor area at the back of the property. | distinguish the rear patio
missed cleanup | Included clearing work left incomplete. | acknowledge missed cleanup
finish concern | Customer concern about the final condition of work. | record a finish concern
visible residue | Material remaining that can be seen. | describe visible residue
incomplete task | Assigned work that has not been fully carried out. | identify the incomplete task
corrective visit | Later attendance intended to address a problem. | discuss a corrective visit
remedial work | Work intended to correct an identified issue. | arrange remedial work
included area | Location covered by the booking. | confirm the included area
excluded area | Location outside the agreed booking. | explain the excluded area
customer complaint | Expression of dissatisfaction with a service or result. | acknowledge a customer complaint
service recovery | Action to address a problem in delivered service. | discuss service recovery
completion status | Whether the relevant work is finished. | correct the completion status
scope boundary | Limit of the work or area agreed. | preserve the scope boundary
follow-up arrangement | Plan for the next contact or attendance. | confirm a follow-up arrangement
return time | Time of a later attendance. | avoid inventing a return time
cleanup standard | Agreed expectation for the condition after clearing. | refer to the cleanup standard
workmanship | Quality of work performed. | discuss a workmanship concern
correction request | Request to put an identified problem right. | pass a correction request
additional area | Location beyond the existing task area. | identify an additional area
observation record | Note of a condition directly seen. | make an observation record
resolution | Outcome that addresses the reported issue. | verify the resolution''',
    precision='The visible clippings support Hazel regarding the missed front cleanup. They do not establish a wider problem across every area of the property. The front steps are included; the rear patio is excluded. Correcting the included task does not automatically expand the booking.',
    precision_extra='The lead can organize the missed front cleanup, but organization is not completion. No precise return time is supplied. Avoid marking the complaint resolved before the correction is verified, or promising rear-patio work as part of the existing arrangement.',
    phrases='''Acknowledge the concern | I can see the clippings beside the front steps.\nConfirm the included area | Those steps are within the listed cleanup area.\nState the missed work | That part of the cleanup is incomplete.\nAvoid a denial | I will not describe the area as fully cleared.\nRefer correction | The lead can organize the missed front cleanup.\nKeep completion accurate | The correction has not yet been completed.\nAvoid a timing promise | I do not have a confirmed return time.\nSeparate the rear area | The rear patio is outside this booking.\nPreserve the scope | The correction concerns the included front area.\nAcknowledge another request | Rear-patio cleanup would be a separate request.\nAvoid generalizing | I am reporting this visible area, not claiming every task was missed.\nKeep the record specific | Clippings remain beside the front steps.\nExplain the next step | I will pass the correction request to the lead.\nAvoid premature closure | I will not mark the concern resolved now.\nRead back the handoff | Missed front cleanup, within scope, with follow-up still to be arranged.\nClose respectfully | Thank you for showing me the exact area.''',
    notes='''I can see | Acknowledges direct evidence without requiring the customer to repeat the complaint.\nThat part | Limits the finding to the identified incomplete area.\nWithin scope | Connects the correction to the agreed booking.\nSeparate request | Keeps the excluded patio distinct from correction of the front cleanup.\nOrganize versus complete | Arranging a response is not evidence that the work is finished.\nResolved | Should describe an established outcome, not merely receipt of a complaint.''',
    d='''Which opening best acknowledges the evidence? | I can see clippings beside the front steps, within the cleanup area. | Everything was completed because the crew left. | You must be referring to the excluded patio. | There cannot be any clippings. | The opening recognizes the directly visible problem in the included area.
Which scope statement is accurate? | The lead can organize missed front cleanup; the rear patio remains excluded. | A complaint automatically includes the rear patio. | No front cleanup was ever booked. | Every outdoor area is now approved. | Correcting the included task does not change the excluded status of the rear patio.
Which status should not be recorded yet? | Resolved and fully corrected | Missed front cleanup reported | Clippings visible beside the steps | Return time unconfirmed | No completed correction or verified resolution has occurred in the supplied facts.
What belongs in the correction request? | The exact front-step location, visible clippings, included scope, and pending follow-up | An invented all-property cleaning promise | A guaranteed return time not supplied | A statement that the rear patio was damaged | These details preserve the observed problem, its scope, and the unresolved arrangement.''',
    dialogue='''Hazel | The cleanup beside the front steps hasn't been finished. There are still clippings there, and that area was included, wasn't it?
Amir | Yes, it was. I can see the [[clippings::Clippings are the visible remaining material beside the front steps, supporting the report of incomplete cleanup.]] beside the steps. You're right to point out that the included area hasn't been fully cleared.
Hazel | Thank you for looking. I was worried I'd just be told the crew had left, so everything must be complete.
Amir | The [[completion status::Completion status of the identified front cleanup is incomplete; leaving the site does not prove that task was finished.]] needs to match what's here, not simply whether the visit has ended. I'll record this part as incomplete.
Hazel | Can the lead arrange for that bit to be put right? I'm asking for the work we already booked.
Amir | Yes, the lead can organize the [[missed cleanup::Missed cleanup is an included front-area task left incomplete, which the lead can arrange to address.]] at the front. I'll give the exact location rather than a general message about the garden.
Hazel | While they're dealing with it, could they clear the rear patio too? It would help to have both areas done.
Amir | The [[rear patio::Rear patio is excluded from this booking and does not become included through the front-cleanup correction request.]] is outside this booking. I can pass that on as a separate request, but it's not included in the front correction.
Hazel | That's fair. Please don't let the patio question distract from the missed work beside the steps. That's the concern I'm reporting.
Amir | I'll preserve the [[scope boundary::Scope boundary keeps the missed included front cleanup separate from the customer's additional rear-patio request.]]: front cleanup to be corrected, patio request separate. Asking about the patio doesn't cancel the front concern.
Hazel | Do you have a time for someone to return? I can plan around it once it's actually arranged.
Amir | I don't have a confirmed [[return time::Return time is not supplied, so Amir cannot promise an exact attendance time for the correction.]] yet. I'll refer the correction to the lead without promising an appointment that isn't booked.
Hazel | Please mention that you saw the clippings yourself. That may make the note clearer than just saying I complained.
Amir | The [[observation record::Observation record preserves what Amir directly saw, rather than treating the concern as an unsupported general complaint.]] will say clippings beside the front steps, inside the listed cleanup area. That's the part I've directly seen.
Hazel | I'm not saying nothing was done. The issue I'm showing you is this unfinished part of the path cleanup.
Amir | I'll keep the [[correction request::Correction request concerns the specific missed front cleanup; it should not claim that every task or area was defective.]] specific to that area. It won't say the whole visit failed or that the rear patio was included.
Hazel | Thanks. Please don't close the complaint just because we've spoken. I need the missed cleanup dealt with, not only acknowledged.
Amir | [[Resolution::Resolution requires the issue to be addressed; merely passing a message to the lead does not establish that outcome.]] still needs to follow the actual correction. I'll leave it open rather than mark it resolved when I pass on the message.
Hazel | Good. The front steps are the first issue. The patio can be discussed separately, with its own scope and timing.
Amir | I'll ask the lead for the [[follow-up arrangement::Follow-up arrangement is still to be organized for the missed front cleanup; no wider task or exact time is agreed.]] for the missed front cleanup. The exact return time remains unconfirmed until it's arranged.''',
    rehearsal=["Read the visible clippings and the included front-step location.","Repeat the correction request separately from the excluded rear-patio request.","Read the closing follow-up without marking the complaint resolved or inventing a time."],
    transfer_title='Acknowledge and refer the missed area',
    transfer_setup='Complete the exchange about the visible front cleanup problem. Keep the included correction, excluded patio, and unresolved timing separate.',
    transfer='''Worker: "Clippings remain beside the front ___." | steps | The steps are the exact location of the visible missed cleanup.
Customer: "That area was ___ in the booking." | included | The front-step area belongs to the listed cleanup scope.
Worker: "The rear patio remains ___." | excluded | The patio is outside the booking and is not automatically added.
Worker: "The lead can organize correction; the return time is ___." | unconfirmed | No exact return time is supplied, even though the lead can organize correction.''',
))

BOOK['units'].append(unit(
    title='Handing over unfinished grounds work',
    scene='A clear path and an open bed review',
    skill='Separate completed work from a deferred review, preserve a callback request, and identify who owns the next arrangement.',
    brief='At Pine Court, worker Rosa hands the visit over to office coordinator Ava. Front-path leaves are cleared. The lead deferred the rear-bed review; no planting or diagnosis was done there. The customer asks for a callback about the rear bed before Friday. Ava owns scheduling, but no visit date is booked. Rosa must distinguish the completed front-path task, the deferred review, the requested communication deadline, and the unresolved appointment.',
    cast='Rosa | Grounds worker\nAva | Office coordinator',
    culture=('Hand over separate statuses, not a single overall label', 'A visit may contain both completed work and an unresolved request. A short handoff still needs the distinction. Name what is finished, what was deferred, what the customer asked to hear, and who owns the next arrangement without declaring the whole visit complete or incomplete.'),
    a='''Which work is complete? | Front-path leaf clearance | Rear-bed planting | Rear-bed diagnosis | A booked follow-up visit | The case confirms only that the front-path leaves are cleared.
What happened to the rear-bed review? | The lead deferred it; no planting or diagnosis was done | It was completed with a confirmed diagnosis | The crew planted the bed | The customer cancelled all work permanently | The lead deferred the review, leaving both planting and diagnosis unperformed.
What does the customer request? | A callback about the rear bed before Friday | A confirmed visit on Friday | Completed planting before Friday | A report that diagnosis is finished | The requested deadline concerns a callback, not an agreed site visit or completed work.''',
    vocabulary='''handover | Transfer of relevant work information and responsibility. | give a clear handover
completed task | Defined work confirmed as finished. | identify the completed task
deferred review | Assessment postponed rather than completed. | record a deferred review
rear bed | Planting area at the back of the site. | identify the rear bed
leaf removal | Clearing fallen leaves from a specified location. | confirm front-path leaf removal
planting | Placing plants in a prepared location. | distinguish planting from review
callback | Return telephone contact responding to a request. | request a callback
callback deadline | Requested or agreed latest time for a return call. | preserve the callback deadline
scheduling owner | Person responsible for arranging dates or contact. | identify the scheduling owner
unbooked visit | Possible attendance without a confirmed appointment. | describe an unbooked visit
status summary | Concise account of each relevant work stage. | provide a status summary
pending item | Matter not yet resolved or finished. | flag a pending item
lead decision | Direction made by the person supervising the work. | record the lead decision
review outcome | Finding or decision resulting from an assessment. | avoid inventing a review outcome
follow-up contact | Later communication about an unresolved matter. | arrange follow-up contact
site attendance | Presence at the property for a stated purpose. | distinguish site attendance from a callback
completion record | Note identifying work confirmed as finished. | update the completion record
unperformed work | Task that has not been carried out. | identify unperformed work
appointment status | Whether a visit is booked, proposed, or unresolved. | confirm appointment status
customer priority | Matter the customer treats as important. | preserve the customer priority
communication request | Request for information or contact. | pass a communication request
open action | Next step not yet completed. | assign an open action
ownership transfer | Passing responsibility for a defined follow-up. | confirm ownership transfer
closeout | Final review or closure of a job or issue. | avoid premature closeout''',
    precision='Front-path leaf clearance is complete. The rear-bed review was deferred by the lead, with no planting or diagnosis performed. Before Friday applies to the requested callback. It is not a booked visit date or a promise to complete work on the bed.',
    precision_extra='Ava owns scheduling, but that ownership does not mean an appointment already exists. The handoff should preserve the customer request and the pending arrangement. Avoid changing deferred into diagnosed, callback into site attendance, or front-path completion into whole-job closeout.',
    phrases='''Open with the completed item | The front-path leaves are cleared.\nName the pending area | The rear-bed review remains outstanding.\nExplain the decision | The lead deferred that review.\nState what was not done | No planting or diagnosis was carried out there.\nPreserve the customer request | The customer wants a callback about the rear bed.\nGive the requested deadline | The callback is requested before Friday.\nDistinguish contact and attendance | That is a request for a call, not a booked visit.\nName the owner | Ava owns the scheduling follow-up.\nState appointment status | No visit date is booked.\nAvoid inventing an outcome | There is no review finding to report.\nSeparate the two areas | The front path is complete; the rear bed is a pending item.\nKeep the request specific | The callback concerns the deferred rear-bed review.\nAvoid a planting promise | No planting commitment was made during this visit.\nRead back the action | Scheduling to follow up on the requested callback before Friday.\nPreserve the unresolved detail | The date of any site attendance remains open.\nClose the handoff | Please keep the completed task and the pending review as separate entries.''',
    notes='''Cleared | A completion statement limited to the front-path leaves.\nDeferred | Postponed; it does not mean inspected, diagnosed, or permanently cancelled.\nBefore Friday | The requested callback deadline, not necessarily Friday itself.\nCallback versus visit | Communication and physical attendance are different commitments.\nOwns scheduling | Identifies responsibility without establishing an appointment.\nSeparate entries | Prevents one completed task from obscuring an unresolved item.''',
    d='''Which handoff preserves the two work statuses? | Front-path leaves cleared; rear-bed review deferred; no planting or diagnosis. | All grounds work finished and diagnosed. | Nothing was completed anywhere. | Rear bed planted but path untouched. | The handoff distinguishes the completed front task from the unperformed rear review.
What does before Friday refer to? | The requested callback | A confirmed site visit | Completed planting | A finished diagnosis | The customer requested communication before Friday, not an appointment or work-completion promise.
Which appointment statement is supported? | Ava owns scheduling, but no visit date is booked. | Ava has already booked Friday. | The crew will definitely return tomorrow. | Scheduling ownership proves a visit is confirmed. | Responsibility for scheduling does not establish that an appointment has been made.
Which closure would misstate the case? | Entire visit closed with all follow-up complete | Front-path leaf clearance complete | Rear-bed review remains pending | Callback request passed to Ava | A pending review and callback request remain, so all follow-up cannot be declared complete.''',
    dialogue='''Rosa | Ava, Pine Court handover: the front-path leaves are cleared. The rear-bed review needs to stay open.
Ava | Let me separate the entries. The [[completed task::Completed task is front-path leaf clearance only; it does not include rear-bed assessment, planting, or diagnosis.]] is front-path leaf clearance. What is the current status of the rear-bed item, and what does the customer need from us?
Rosa | The lead deferred the rear review. No planting or diagnosis was done there; I've no finding to pass on.
Ava | I will record a [[deferred review::Deferred review means the assessment was postponed, not completed with a finding or converted into planting work.]], not a completed inspection. I will also state that no planting or diagnosis took place in that area.
Rosa | The customer wants a callback about the rear bed before Friday. Please keep that timing with the request.
Ava | I have the [[callback deadline::Callback deadline is the customer's request for contact before Friday; it is not a confirmed work or visit deadline.]] as before Friday. Does the customer already have a booked visit, or is the request only for contact about the next step?
Rosa | No visit is booked. They want a call about the next step, not a confirmed attendance on Friday.
Ava | Then the [[appointment status::Appointment status remains unbooked; the callback request cannot be treated as confirmation of physical attendance.]] remains unbooked. I will not put Friday down as a confirmed attendance date just because it appears in the callback request.
Rosa | Please don't let the cleared path close the rear-bed item. They have different statuses.
Ava | I will keep a separate [[pending item::Pending item is the rear-bed review and its follow-up, which must remain visible alongside the completed front task.]] for the rear bed. The cleared front path can be recorded accurately without closing the unresolved review.
Rosa | You'll take the scheduling follow-up, correct? I want the next reader to know who owns it.
Ava | Yes, I am the [[scheduling owner::Scheduling owner identifies Ava's responsibility for arrangements; it does not imply that she has already booked a date.]]. That identifies responsibility, but it does not mean a date has already been arranged or a visit has been confirmed.
Rosa | Please keep deferred as the lead's decision. It wasn't a diagnosis that planting or treatment was needed.
Ava | I will not invent a [[review outcome::Review outcome is absent because the rear-bed assessment was deferred and no diagnosis was performed.]]. The note will describe the deferral and the absence of planting or diagnosis, rather than supply a reasoned finding we do not have.
Rosa | Could you read the timing back? Before Friday means the callback request, not completed bed work.
Ava | The [[communication request::Communication request is a callback about the rear bed before Friday, distinct from a booked visit or completed grounds work.]] is a callback about the rear bed before Friday. There is no promise of planting, diagnosis, or completed work by that time.
Rosa | That's right. Any later visit still needs arranging; we've only passed the request for contact.
Ava | I will retain that as an [[open action::Open action is the unresolved scheduling follow-up on the callback request; it is not evidence that contact has already happened.]]. The record will name me as the owner and will not say the callback has already happened.
Rosa | Thanks. The path can be marked complete without making the unfinished rear review disappear.
Ava | Agreed. I will avoid premature [[closeout::Closeout of all work would be inaccurate because the rear-bed review and requested follow-up remain unresolved.]]. The handover will retain the completed front task, deferred rear review, requested callback deadline, and unbooked visit status as separate facts.''',
    rehearsal=["Read front path complete and rear-bed review deferred as two separate entries.","Repeat before Friday as the requested callback timing, not a booked visit.","Read Ava's scheduling ownership while leaving the actual appointment unbooked."],
    transfer_title='Hand over four distinct facts',
    transfer_setup='Complete the office handoff. Preserve the finished front task, deferred rear review, requested callback timing, and absence of a booked visit.',
    transfer='''Worker: "The front-path leaves are ___." | cleared | Cleared confirms the completed front-path task, not all work at the site.
Coordinator: "The rear-bed review was ___ by the lead." | deferred | Deferred means postponed; no planting or diagnosis was performed there.
Worker: "The customer requests a callback before ___." | Friday | Friday belongs to the requested callback deadline, not a booked attendance date.
Coordinator: "I own scheduling, but no visit is ___." | booked | Scheduling responsibility exists, while the actual visit date remains unconfirmed.''',
))
