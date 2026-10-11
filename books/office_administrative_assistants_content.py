"""Original Office and Administrative Assistant English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='office-administrative-assistants', title='Office and Administrative Assistant English',
    cover_label='ENGLISH FOR OFFICE COORDINATION AND ADMINISTRATIVE SUPPORT',
    cover_title='Office &\nAdministration', cover_size=34,
    tagline='Clear arrangements. Reliable follow-through.',
    audience='For office assistants, reception staff, executive support teams, and administrators coordinating people, records, supplies, and schedules.',
    map_intro='Eight everyday office situations demand precise English: cross-office scheduling, call messages, meeting actions, document corrections, delivery queries, visitor reception, travel comparisons, and deadline negotiations.',
    notes_title='Make the arrangement explicit.',
    notes_intro='Administrative work connects people who hold different pieces of information. A useful message identifies the relevant person or record, separates a request from a promise, and makes the next action easy to understand.',
    field_notes=[
        ('Name the reference', 'A first name, clock time, or filename may not identify the intended person, moment, or document. Confirm the distinguishing detail before sending an invitation, directing a visitor, or circulating a correction.', '"Do you mean 3:00 in your office, which is noon in the other office on this date?"'),
        ('Keep requests and commitments distinct', 'A caller can request a deadline without the recipient agreeing to it. A manager can request an extra task without creating extra time. Preserve the request and ask for the missing confirmation or priority decision.', '"Lena requests a callback before 4:00; availability has not been confirmed."'),
        ('Separate preparation from approval', 'Obtaining quotations is not buying a printer. Comparing fares is not booking travel. A useful action record names the owner, deliverable, and due date without quietly adding spending authority.', '"Sam will obtain two quotes by Thursday; no purchase is approved."'),
        ('Correct the message without expanding authority', 'Replace outdated information clearly and identify the current source. An access problem should go to the document owner rather than prompting an unauthorized wider share. Courteous reception likewise preserves the actual visitor arrangements.', '"Use approved version 3. I will ask the owner to resolve your viewing access."'),
    ],
    scope_note='All organizations, records, prices, schedules, and policies are fictional. Use actual workplace approval, security, privacy, purchasing, and records procedures. The time equivalence is supplied for the fictional meeting date, not a permanent conversion rule. Travel conditions belong only to the quoted options. This book teaches communication, not financial or legal advice, and does not authorize purchases, access changes, payments, or visitor entry.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Secretaries and Administrative Assistants.',
             url='https://www.bls.gov/ooh/office-and-administrative-support/secretaries-and-administrative-assistants.htm',
             note='Occupational context for scheduling, documents, calls, records, and administrative coordination. The teaching cases are original and fictional.', checked='10 October 2026'),
        dict(title='Google Calendar Help. Use Google Calendar in Different Time Zones.',
             url='https://support.google.com/calendar/answer/37064',
             note='Background for distinguishing a meeting instant from local clock displays. The fictional case supplies its own date-specific equivalence.', checked='10 October 2026'),
        dict(title='Microsoft Support. Sharing Files, Folders, and List Items.',
             url='https://support.microsoft.com/en-us/sharepoint/libraries/sharing-files-folders-and-list-items',
             note='Terminology for document links, viewing access, and permissions. The book does not instruct learners to change workplace access rights.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Scheduling across calendars and time zones',
    scene="Three o'clock in whose office?",
    skill='Clarify a missing time reference and read back two equivalent local times before issuing a meeting invitation.',
    brief="Colleague Maya asks assistant Arun to arrange a 3:00 meeting with another office. For the fictional meeting date, 3:00 in Maya's office equals noon at the other office. Both calendars are open at that equivalent time, but the request does not identify whose clock Maya means. Arun must confirm the intended office reference before sending invitations. No meeting duration, location, or recurrence has been specified.",
    cast='Maya | Colleague\nArun | Administrative assistant',
    culture=('A small clarification prevents a large scheduling error', 'A free calendar does not remove ambiguity in a spoken request. Ask whose local time is intended without suggesting that the colleague has made a foolish mistake. Once clarified, name both offices and their equivalent times in the readback.'),
    a='''What is missing from the initial request? | Whose local time 3:00 refers to | Whether both calendars are open at the stated equivalent time | Whether noon and 3:00 can be equivalent here | The assistant's name | The request supplies a clock time but does not identify the intended office reference.
What equivalence is supplied for this date? | 3:00 in Maya's office equals noon at the other office | Both offices show 3:00 simultaneously | Noon in Maya's office equals 3:00 elsewhere | The difference is permanently fixed for all dates | The brief explicitly gives the date-specific relationship between the two local times.
What should happen before invitations are sent? | Confirm the intended time reference | Assume the sender always means the recipient's time | Invent a meeting duration | Treat an open calendar as acceptance | Clarifying the intended office time is necessary before sending the invitation.''',
    vocabulary='''local time | Clock time at the specified location. | confirm local time
time zone | Region using a defined civil-time reference. | identify the time zone
time reference | Location or standard that gives a clock time meaning. | clarify the time reference
equivalent time | Different clock display representing the same moment elsewhere. | read back the equivalent time
calendar availability | Time shown as open or occupied in a calendar. | check calendar availability
meeting request | Proposal to arrange a meeting with specified details. | clarify the meeting request
invitation | Message asking identified people to attend an event. | send the invitation
organizer | Person responsible for arranging the meeting. | identify the organizer
attendee | Person invited to or participating in a meeting. | confirm the attendee list
noon | Twelve o'clock in the middle of the day. | specify noon
date-specific | Valid for the particular date being discussed. | use a date-specific conversion
daylight saving time | Seasonal clock adjustment used in some locations; abbreviated DST. | check daylight saving time
Coordinated Universal Time | International time reference commonly abbreviated UTC. | identify Coordinated Universal Time
offset | Difference between one time reference and another. | verify the relevant offset
calendar entry | Event recorded in a scheduling system. | check the calendar entry
time display | Clock representation shown to a particular user. | compare the time displays
scheduling conflict | Overlap between incompatible calendar commitments. | resolve a scheduling conflict
free slot | Unoccupied period shown in a calendar. | identify a free slot
tentative hold | Provisional reservation not yet a final agreement. | distinguish a tentative hold
acceptance | Response agreeing to the stated invitation. | confirm acceptance
duration | Length of time an event is intended to last. | request the meeting duration
recurrence | Pattern under which an event repeats. | confirm recurrence separately
location field | Part of an invitation identifying where the meeting occurs. | complete the location field
schedule readback | Restatement of the agreed scheduling details. | give a schedule readback''',
    precision="The supplied equivalence is 3:00 in Maya's office and noon in the other office on the fictional date. Do not put 3:00 on both local displays or assume the same difference applies on every date.",
    precision_extra='An open calendar is not proof that an invitation has been accepted. The initial request also supplies no duration, location, or recurrence. Confirm the intended reference first and leave other missing invitation details unresolved until they are provided.',
    phrases='''Clarify the reference | Do you mean 3:00 in your office or the other office?
Explain the equivalence | On this date, your 3:00 is their noon.
Keep the question neutral | I want to make sure both offices receive the same meeting time.
State availability | Both calendars are open at that equivalent time.
Separate availability from intent | The calendars are open, but I still need your intended time.
Avoid duplicate clock labels | The two offices should not both be labeled 3:00.
Read back the location | You mean 3:00 in your office.
Read back the other clock | That will be noon in the other office.
Preserve the date | This conversion is for the meeting date we are discussing.
Avoid a permanent rule | I will not assume the same offset for every date.
Distinguish acceptance | An open slot is not an accepted invitation.
Hold the send | I will confirm the reference before sending.
Identify missing duration | How long should the meeting last?
Identify missing location | We still need the meeting location.
Keep recurrence separate | We have not agreed a repeating schedule.
Close the clarification | I have the intended office time and its equivalent clearly recorded.''',
    notes='''Do you mean ... or ...? | Offers the two relevant interpretations without choosing for the speaker.
On this date | Prevents a supplied time relationship becoming a permanent rule.
Their noon | Names the second office's local display.
Before sending | Places clarification ahead of an externally visible commitment.
Still need | Identifies a remaining detail without undoing what is known.
Should not both | Corrects duplicate local labels for the same meeting instant.''',
    d='''Which clarification is best? | Does 3:00 refer to your office or the other office? | I assume every office uses your clock | An open calendar means the time is obvious | I will send 3:00 to both offices | The question directly resolves the missing location reference for the requested time.
Which entry preserves the clarified meeting without adding missing details? | One meeting: Maya's office 3:00, other office noon; duration pending | One meeting: both offices 3:00 local time; duration pending | One meeting: Maya noon, other office 3:00; duration pending | One meeting: Maya 3:00, other office noon; one hour confirmed | The supplied equivalence names one moment, but neither a duration nor an accepted invitation has been established.
What does calendar availability establish? | The relevant slot is open, not that the intended time is confirmed | Every invitee has accepted | The meeting lasts an hour | Recurrence is weekly | Availability concerns the calendar slot rather than intention, duration, or acceptance.
Which detail must not be invented? | A one-hour meeting duration | The supplied noon equivalent | The missing time reference | The need to clarify before sending | The brief provides no duration from which a one-hour meeting could be established.''',
    dialogue='''Maya | Could you set up three o'clock with the other office? Both calendars look open, so I'd like to get it arranged.
Arun | Before I send anything, which [[time reference::Time reference identifies which office's clock gives the requested three o'clock its intended meaning.]] do you mean: three in your office or three in theirs?
Maya | Three here. I was looking at my own calendar and forgot that the other office would see a different time.
Arun | Thanks. On this date the [[equivalent time::Equivalent time is noon in the other office when Maya's office shows three.]] there is noon. I'll state both offices so we're referring to the same meeting.
Maya | Yes, three here and noon there. Please don't put three next to both office names in the message.
Arun | Agreed. There are two [[local time::Local time refers to each office's own clock display for the same meeting moment.]] displays for one meeting, not two meetings at the same clock time.
Maya | Is that enough to send it? The free slots were what I checked before asking you.
Arun | The [[calendar availability::Calendar availability confirms an open slot but does not supply the missing duration or location.]] helps, but I still need the duration and location. Neither was in the request.
Maya | I'll send those separately. For now, can you keep the intended time without filling in an hour by default?
Arun | Yes. I'll retain the [[meeting request::Meeting request remains a proposal whose details must be confirmed before an invitation is issued.]] as three here and noon there on this date, with those other details outstanding.
Maya | We may need another meeting with them later. Can I just use the same three-hour difference every time?
Arun | I'd check each date. This is a [[date-specific::Date-specific limits the supplied equivalence to the fictional meeting date rather than every future meeting.]] equivalence; it isn't a standing rule for future meetings.
Maya | Understood. Also, seeing a free slot doesn't mean their colleagues have agreed to attend, does it?
Arun | No. [[Acceptance::Acceptance is an attendee's agreement to an invitation, distinct from a calendar appearing open.]] is a separate response. We shouldn't say they've agreed just because their calendars appear open.
Maya | Please keep the eventual message as a request, then. I don't want it to sound as though attendance is already settled.
Arun | The [[invitation::Invitation is the attendance request that should contain confirmed scheduling details without assuming prior acceptance.]] will ask them to attend at the clarified time, and we'll track their responses separately.
Maya | Let me check: three in my office, noon in theirs, on the date we're discussing. Nothing sent yet.
Arun | That's the [[schedule readback::Schedule readback repeats both equivalent office times and preserves that invitations have not yet been sent.]]. I'll keep it while we obtain the duration and location rather than assume either.
Maya | I'll send those next. And this is only one meeting for now, not a weekly series.
Arun | Understood. [[Recurrence::Recurrence describes a repeating schedule, which Maya has not authorized in the current request.]] hasn't been authorized. I'll wait for the remaining details before sending the single meeting request.''',
    rehearsal=["Complete the scheduling dialogue using the word bank.","Read the two office times aloud as one meeting: 3:00 here, noon there, on the supplied date. Then read the unresolved duration and location.","Complete the transfer, check the explained key, and repeat the corrected scheduling readback."],
    transfer_title='Read back one meeting in two local times',
    transfer_setup='Complete the scheduling clarification without adding a duration or treating availability as acceptance.',
    transfer='''Assistant: "Whose local ___ do you mean?" | time | Time is the ambiguous reference that must be attached to an office.
Colleague: "Three in my office equals ___ at the other office." | noon | Noon is the supplied equivalent for the fictional meeting date.
Assistant: "Both calendars are ___ at that time." | open | Open describes availability without establishing that an invitation has been accepted.
Colleague: "Confirm the remaining details before ___." | sending | Sending must follow clarification rather than precede the missing details.'''
))


BOOK['units'].append(unit(
    title='Taking useful calls and passing accurate messages',
    scene='Delivery D18 belongs with facilities',
    skill='Route a caller by purpose, capture the reference and preferred reply route, and relay a requested deadline without guaranteeing it.',
    brief='Caller Lena Park needs the facilities team about delivery D18, not the finance team about an invoice. Facilities extension is 214. Lena requests a callback before 4:00, but team availability is unknown. Assistant Dev must confirm the delivery reference and preferred contact route, read back the message, and preserve the requested deadline as a request. The conversation supplies no payment problem or confirmed callback commitment.',
    cast='Lena | Caller\nDev | Office assistant',
    culture=('Route by the purpose, not by the first familiar word', "A delivery reference can sound like an invoice reference over the phone. Confirm the reason for the call before selecting a team. Taking a message is useful work, but it does not give the assistant control over the recipient's availability."),
    a='''Which team does Lena need? | Facilities | Finance | Payroll | An unidentified invoice department | The call concerns delivery D18 and is explicitly for facilities.
What is the facilities extension? | 214 | 241 | 412 | D18 | The supplied internal telephone extension for facilities is 214.
How should before 4:00 be recorded? | A requested callback deadline | A guaranteed response time | A confirmed payment deadline | A delivery time already agreed | Lena requests the callback, but the team's availability is unknown.''',
    vocabulary='''call routing | Directing a telephone inquiry to the appropriate recipient. | confirm call routing
facilities team | Staff coordinating the relevant building or workplace services. | contact the facilities team
finance team | Staff handling the relevant financial records and processes. | distinguish the finance team
extension | Internal telephone number used within an organization. | confirm the extension
delivery reference | Identifier attached to a particular delivery. | capture the delivery reference
caller identity | Name and relevant identifying details of the person calling. | verify caller identity
purpose of call | Reason the caller needs contact. | clarify the purpose of call
message slip | Written record of a call for another person. | complete the message slip
callback request | Request for someone to return a telephone call. | relay a callback request
requested deadline | Time by which the caller would like a response. | preserve the requested deadline
preferred contact route | Communication method selected by the caller. | confirm the preferred contact route
contact details | Information needed to reach the intended person. | verify contact details
transfer | Connection of an existing call to another line. | distinguish a transfer from a callback
voicemail | Recorded message left when a recipient is unavailable. | identify the voicemail option
recipient availability | Whether the intended person or team can respond. | check recipient availability
message readback | Spoken repetition of a message to confirm its accuracy. | give a message readback
reference correction | Amendment of a misheard identifier. | record a reference correction
department | Organizational team with a defined function. | identify the correct department
misdirected call | Call sent to a recipient who does not handle its purpose. | prevent a misdirected call
response commitment | Agreed promise to reply at a specified time or stage. | distinguish a response commitment
call log | Record of telephone contacts and their relevant details. | update the call log
recipient confirmation | Verification that the intended recipient has received or accepted the message. | obtain recipient confirmation
urgency | Stated need for prompt attention. | explain the urgency
handoff note | Message passed to another person for follow-up. | prepare an accurate handoff note''',
    precision='The reference is delivery D18, and the team is facilities at extension 214. Do not turn the call into an invoice query for finance. A good message retains the name, purpose, reference, contact route, and requested deadline.',
    precision_extra="Before 4:00 is Lena's requested response deadline, not a confirmed team commitment. Confirm the preferred route and relevant contact details without inventing a telephone number. A message being taken does not establish that the recipient can meet the request.",
    phrases='''Clarify the purpose | Is this about the delivery or an invoice?
Identify the team | You need facilities rather than finance.
Ask for the reference | Could you confirm the delivery reference?
Read back the identifier | That is D18, D followed by eighteen.
Name the extension | Facilities is on extension 214.
Confirm the caller | I have your name as Lena Park.
Ask for the route | How would you prefer the team to contact you?
Verify the details | May I check the contact details for that route?
Capture the timing | You are requesting a callback before 4:00.
State the limit | I cannot confirm the team's availability.
Avoid an invented promise | I can relay the request, but I cannot guarantee that time.
Separate transfer and callback | Taking a message is not the same as connecting the call.
Keep the purpose intact | This concerns delivery D18, not an invoice.
Read back the whole message | Lena Park requests facilities to call about D18 before 4:00.
Invite a correction | Is any part of that message inaccurate?
Close honestly | I will pass on the requested deadline with the contact route.''',
    notes='''Rather than | Corrects the department without changing the caller's purpose.
D followed by eighteen | Makes a short reference easier to distinguish over the phone.
Would prefer | Elicits the caller's chosen communication route.
Requesting | Marks the deadline as the caller's wish, not an accepted promise.
Cannot guarantee | Limits the assistant's commitment while preserving a useful action.
Any part ... inaccurate? | Invites a specific correction to the completed readback.''',
    d='''Which message is accurate? | Lena Park requests facilities about delivery D18, callback before 4:00 | Finance guarantees payment of invoice D18 at 4:00 | Facilities has already returned the call | Lena has approved a new delivery charge | The correct message preserves the caller, team, reference, and requested timing.
Which response overpromises? | They will definitely call before four | I will relay your requested deadline | Their availability is not confirmed | Please confirm your preferred contact route | The team's unknown availability cannot support a definite callback promise.
Which information still needs verification before the message is usable? | The actual contact details for Lena's chosen reply route | A new department because facilities cannot handle deliveries | A payment amount for the D18 invoice | A guaranteed four o'clock appointment with finance | A telephone preference alone does not supply a verified callback number; the delivery purpose and facilities route are already established.
Which number should Dev associate with facilities? | Extension 214 | Extension 241 | Delivery 214 | Invoice 412 | The brief supplies 214 specifically as the facilities telephone extension.''',
    dialogue='''Lena | Hello, Lena Park here. I was sent to finance about D18, but I think I need facilities.
Dev | Let me check the [[purpose of call::Purpose of call distinguishes the delivery inquiry from an invoice matter before Dev routes it.]] first. Are you calling about a delivery or an invoice? I want to make sure the message reaches the right team.
Lena | It's delivery D18, not an invoice. I'm trying to reach the facilities team.
Dev | Thank you. I have the [[delivery reference::Delivery reference is D18 and should not be relabeled as an invoice identifier.]] as D18, D followed by eighteen. Facilities is the team you need, and their extension is 214.
Lena | Could they call me before four? That's when I need the delivery question answered.
Dev | I will record a [[callback request::Callback request records Lena's wish for a return call without promising the team's response time.]] before four. I cannot confirm their availability, so I should not promise that they can meet the requested time.
Lena | Please keep before four in the message, even if you can't confirm they'll meet it.
Dev | Certainly. The [[requested deadline::Requested deadline preserves before four as Lena's timing request, distinct from an accepted commitment.]] will stay in the message as before four. How would you prefer the team to contact you when they respond?
Lena | A telephone call, please. I'll confirm the contact number with you.
Dev | I will note the [[preferred contact route::Preferred contact route is a telephone call, as Lena chooses during the exchange.]] as telephone and verify the relevant details with you. I will not substitute email just because it is easier to forward.
Lena | Use Lena Park, not just Lena. Another person here has called about a different delivery.
Dev | Yes. The [[caller identity::Caller identity is Lena Park, keeping this message distinct from other callers and deliveries.]] is Lena Park. I will keep your name, delivery D18, and the contact details together so the handoff is not ambiguous.
Lena | Was the extension two-one-four? I wrote two-four-one and may have reversed the last digits.
Dev | It is [[extension::Extension identifies the internal telephone number 214, which Dev corrects without changing the delivery reference.]] 214, two-one-four. The delivery identifier remains D18. I will keep those two kinds of reference separate in the note.
Lena | Could you read the message back before we finish? I want to check the team and the delivery reference together.
Dev | Here is the [[message readback::Message readback combines the caller, intended team, delivery reference, route, and requested deadline for confirmation.]]: Lena Park requests a telephone callback from facilities about delivery D18 before four. The contact details are to be verified, and team availability is not confirmed.
Lena | That's right. There isn't a finance approval or payment question to add.
Dev | Agreed. The [[handoff note::Handoff note must preserve a facilities delivery inquiry rather than inventing a finance approval request.]] will contain no payment or finance-approval request. Its purpose is to get the delivery question to the appropriate facilities colleagues.
Lena | Thank you. I understand you're passing on a request, not guaranteeing their response.
Dev | Exactly. A [[response commitment::Response commitment would require confirmation from the relevant team, which Dev does not currently have.]] has not yet been established. I will relay the accurate request and keep the distinction clear.''',
    rehearsal=["Complete the call-message dialogue.","Read back Lena Park, delivery D18, facilities extension 214, telephone preference, and requested before-four deadline. Keep request separate from guarantee.","Complete the transfer and check each identifier against the key before rereading the whole message."],
    transfer_title="Pass on the caller's actual request",
    transfer_setup='Complete the message summary. Keep the department, reference, extension, and deadline status accurate.',
    transfer='''Assistant: "Lena needs the ___ team." | facilities | Facilities handles the stated inquiry, not finance or payroll.
Caller: "The delivery reference is ___." | D18 | D18 identifies the delivery discussed in this telephone message.
Assistant: "The team extension is ___." | 214 | 214 is the supplied facilities extension, not the delivery identifier.
Caller: "Before 4:00 is my requested ___." | deadline | Deadline preserves the requested timing without asserting that the team has accepted it.'''
))

BOOK['units'].append(unit(
    title='Preparing meetings and confirming action points',
    scene='Two quotes, not permission to buy',
    skill='Use the final minutes of a meeting to confirm an action owner, deliverable, deadline, and deferred agenda item.',
    brief='Ten minutes remain in an office meeting. The two outstanding agenda items are printer replacement and visitor signage. Chair Farah prioritizes the printer decision. Assistant Sam can obtain two quotations by Thursday, but nobody has approved a purchase. Sam must ask Farah to confirm that action and defer signage to the next meeting. The record must not turn quote gathering into an order or claim that signage has been rejected.',
    cast='Sam | Administrative assistant\nFarah | Meeting chair',
    culture=('Close with actions that survive outside the room', 'People can leave the same meeting remembering different levels of agreement. Repeat the owner, deliverable, and due date before closing. Distinguish a decision to gather information from a purchase decision, and record a deferred item without making it disappear.'),
    a='''Which item does the chair prioritize? | Printer replacement | Visitor signage | A new travel policy | A payment dispute | Farah prioritizes the printer item during the final ten minutes.
What can Sam deliver by Thursday? | Two quotations | An approved printer purchase | Installed visitor signage | A guaranteed supplier discount | The supplied action is to obtain two quotes by Thursday.
What is the status of signage? | To be deferred to the next meeting | Rejected permanently | Already installed | Approved for immediate spending | Deferral moves the item to a later meeting without resolving its substance.''',
    vocabulary='''agenda | Ordered list of topics for a meeting. | work through the agenda
agenda item | Individual topic listed for discussion. | prioritize an agenda item
chair | Person directing the meeting. | ask the chair to confirm
booklet imposition | Arrangement of document pages on print sheets so the folded booklet reads in the correct order. | confirm booklet imposition
priority item | Topic selected for attention before others. | identify the priority item
quotation | Supplier statement of a price and relevant terms. | obtain two quotations
quote gathering | Collecting supplier offers for later comparison. | assign quote gathering
purchase approval | Permission to buy the specified item. | distinguish purchase approval
action point | Agreed task arising from a discussion. | confirm the action point
action owner | Person responsible for completing the stated task. | name the action owner
deliverable | Specific output that a task is meant to produce. | define the deliverable
due date | Date by which a stated task should be completed. | record the due date
minutes | Formal or agreed record of a meeting's proceedings. | correct the minutes
decision log | Record of decisions and their scope. | update the decision log
deferred item | Topic moved to a later discussion. | retain the deferred item
duplex printing | Printing on both sides of a physical sheet. | specify duplex printing
carry forward | Keep an unresolved item for later attention. | carry forward visitor signage
procurement | Process of obtaining goods or services for an organization. | distinguish procurement stages
supplier comparison | Review of relevant differences between supplier offers. | prepare a supplier comparison
budget authority | Permission to commit funds within an identified scope. | confirm budget authority
motion | Formal proposal presented for a meeting's decision where that procedure applies. | distinguish a motion from discussion
consensus | Shared agreement among the relevant participants. | verify consensus
action readback | Spoken summary of the task and its limits. | give an action readback
open item | Matter not yet resolved or completed. | preserve an open item''',
    precision='Sam is the action owner. The deliverable is two quotes, due Thursday. No purchase has been approved. Obtaining prices and terms prepares a later decision; it does not establish supplier selection, an order, or installation.',
    precision_extra='Visitor signage is deferred to the next meeting, not rejected or completed. The final ten minutes should produce a precise action record. Do not invent a quotation deadline earlier than Thursday or a new date for the next meeting.',
    phrases='''Signal the time | We have ten minutes left.
Name the competing items | Printer replacement and visitor signage are still on the agenda.
Ask for direction | Which item should take priority?
Confirm the priority | We will use the remaining time for the printer item.
Offer a bounded action | I can obtain two quotes by Thursday.
Name the owner | Sam will gather the quotations.
Define the output | The deliverable is two supplier quotes.
Keep approval separate | No purchase has been approved.
Avoid an accidental order | Gathering quotes does not authorize me to buy.
Ask for confirmation | Can you confirm that as the action point?
Record the deadline | I will put Thursday in the action record.
Defer transparently | Shall we carry signage forward to the next meeting?
Avoid false rejection | Deferred does not mean rejected.
Preserve the open item | Signage remains on the follow-up agenda.
Read back the outcome | Sam: two quotes by Thursday; purchase not approved.
Close with shared wording | I will circulate the record with those limits clear.''',
    notes='''Can obtain | Offers a specific deliverable within the speaker's stated capacity.
By Thursday | Gives the due date rather than the meeting date.
As the action point | Requests confirmation of the task to be recorded.
Does not authorize | Separates preparation from spending permission.
Carry forward | Keeps an item active for later consideration.
With those limits | Preserves the boundary of what was actually agreed.''',
    d='''Which action record is correct? | Sam to obtain two printer quotes by Thursday; no purchase approved | Sam to buy a printer today | Farah has selected a supplier | Signage installed by Thursday | The record names the owner, deliverable, deadline, and purchase-approval limit.
What does deferred mean here? | Moved to the next meeting | Rejected permanently | Approved for immediate purchase | Removed from all records | Deferral postpones discussion without deciding or deleting the item.
Which question closes the meeting usefully? | Can you confirm two quotes by Thursday as my action? | Should I assume all spending is approved? | May I erase the signage item? | Which supplier did we already order from? | The question verifies the bounded task that Sam can actually carry out.
Which claim exceeds the agreement? | A printer order is authorized | Two quotes are needed | Sam owns the quote action | Signage remains unresolved | The brief explicitly states that no purchase has been approved.''',
    dialogue='''Sam | We've got ten minutes left and two items: printer replacement and visitor signage. Which should take the remaining time?
Farah | Make the printer the [[priority item::Priority item is printer replacement, which Farah selects for the remaining meeting time.]]. Let's agree a useful next step rather than rush through both topics.
Sam | I can get two supplier quotes by Thursday. That will let us compare the offers, but it won't settle which printer to buy.
Farah | That's the [[deliverable::Deliverable is two supplier quotes, not a selected or purchased printer.]] I need: two quotations. We haven't selected a supplier or authorized an order.
Sam | Shall I put my name against that action? I don't want the minutes to leave it as someone to get prices.
Farah | Yes, you're the [[action owner::Action owner is Sam, who has offered to obtain the two quotations.]], Sam. Please record the two-quote task against your name.
Sam | I'll keep Thursday as the deadline, then. I haven't offered tomorrow, even though the replacement is becoming urgent.
Farah | Thursday is the agreed [[due date::Due date is Thursday, the stated deadline for the two-quote deliverable.]]. Don't move it earlier in the minutes without checking whether that's achievable.
Sam | Can I put no order approved on the same line? A short note saying printer quotes can sound like the purchase is already agreed.
Farah | Yes. There is no [[purchase approval::Purchase approval has not been given, so obtaining quotations must not be recorded as permission to buy.]]. We're gathering information for a later decision, not giving you spending authority.
Sam | That leaves signage. Shall I carry it to the next meeting rather than mark it resolved because we've run out of time?
Farah | Record it as a [[deferred item::Deferred item keeps visitor signage for the next meeting without treating it as rejected or completed.]]. It hasn't been rejected or completed; we still need to discuss it.
Sam | I'll include both outcomes in the summary, so signage doesn't disappear when people only read the action list.
Farah | Good. The [[minutes::Minutes should preserve both the confirmed quote action and the unresolved signage item.]] should distinguish the confirmed printer task from the postponed signage discussion.
Sam | Here's the printer line: Sam to obtain two quotes by Thursday; no purchase approved and no supplier selected.
Farah | That's an accurate [[action readback::Action readback confirms Sam, two quotations, Thursday, and the absence of purchase approval together.]]. Keep the approval limit attached so it survives if the action is copied elsewhere.
Sam | For signage, I'll say next meeting. I haven't got a confirmed date for that meeting to add.
Farah | That's enough. It remains an [[open item::Open item identifies signage as unresolved despite its move to the next meeting.]], with the next discussion identified but no invented date.
Sam | Then I have one task with an owner and deadline, and one item carried forward. I'll circulate that wording.
Farah | Please do. The [[decision log::Decision log records what was actually agreed, including the boundary between preparation and spending authority.]] needs to show what we agreed, not turn preparation into a purchase decision.''',
    rehearsal=["Complete the meeting-close dialogue.","Read Sam's action and Farah's confirmation aloud: two quotes by Thursday, no purchase approval. Then read the separate signage deferral.","Complete the transfer and check the key. Repeat the two outcomes without turning either into a spending decision."],
    transfer_title='Close the meeting with a precise action record',
    transfer_setup='Complete the action summary. Preserve the quotation task, deadline, and unresolved signage item.',
    transfer='''Chair: "The action owner is ___." | Sam | Sam is the assistant who offered and accepted the quote-gathering task.
Assistant: "I will obtain two ___." | quotations | Quotations are the deliverable, not an approved printer purchase.
Chair: "The due date is ___." | Thursday | Thursday is the explicitly agreed deadline for obtaining the quotes.
Assistant: "Visitor signage is ___ to the next meeting." | deferred | Deferred postpones discussion without rejecting, approving, or completing the signage item.'''
))


BOOK['units'].append(unit(
    title='Checking document versions and access',
    scene='Correct version, missing permission',
    skill='Correct an outdated document message and request appropriate viewing access without independently widening the audience.',
    brief="Assistant Elena sent version 2 of the visitor guide. Version 3 was approved this morning, and the older guide gives the wrong reception floor. The current guide is in the shared folder, but recipient Kai cannot view it. Elena must identify the correction, direct recipients to approved version 3, and ask the document owner to resolve Kai's viewing access. The correct floor number and the identity of the owner are not supplied; neither should be invented.",
    cast='Kai | Guide recipient\nElena | Administrative assistant',
    culture=('Own the correction and separate the access problem', 'An apology should point clearly to the replacement source. A broken permission is a second issue, not a reason to recirculate the inaccurate attachment or make the folder available to everyone. Describe the access needed and route the request to the owner.'),
    a='''Which version is current? | Version 3, approved this morning | Version 2 because it was emailed | Both versions equally | An invented version 4 | Version 3 is the approved current guide, despite the earlier email.
What is wrong in version 2? | The reception floor | The supplier quantity | A confirmed ticket price | The meeting duration | The brief identifies the reception-floor information as the outdated error.
Who should resolve Kai's access? | The document owner through the appropriate process | Elena by making the folder public | Kai by forwarding the old version | Any recipient by guessing a password | The request belongs with the document owner, not an unauthorized expansion of permissions.''',
    vocabulary='''document version | Identified revision of a file or publication. | check the document version
approved version | Revision accepted for the stated use. | use the approved version
superseded | Replaced by a newer applicable version. | mark the guide as superseded
current guide | Document presently valid for the intended purpose. | link to the current guide
shared folder | Storage location available to users with relevant permissions. | locate the shared folder
document owner | Person responsible for the file and relevant access decisions. | contact the document owner
viewing access | Permission to open and read the content. | request viewing access
editing permission | Authority to modify the content. | distinguish editing permission
access request | Request for an appropriate permission to be granted. | submit an access request
permission scope | Range of people and actions covered by an access setting. | preserve permission scope
mail merge | Creation of personalized documents by combining a template with selected source records. | preview the mail merge
attachment | File included with a message. | replace the outdated attachment
document link | Address pointing to a stored file. | share the current document link
version history | Record of changes or saved revisions. | consult version history
approval date | Date on which the relevant revision was accepted. | verify the approval date
correction notice | Message identifying an error and its replacement. | send a correction notice
merge field | Placeholder that inserts a specified source value into a personalized document. | verify the merge field
access error | Message or condition preventing permitted use of a resource. | report an access error
distribution list | Set of recipients for a message or document. | check the distribution list
unrestricted link | Link that does not limit access to the intended named audience. | avoid an unrestricted link
read-only | Allowing viewing without permission to change content. | request read-only access
source location | Place where the authoritative file is stored. | identify the source location
revision control | Management of document versions and their status. | maintain revision control
replacement message | Updated communication that corrects an earlier one. | issue a replacement message''',
    precision='Version 3 was approved this morning. Version 2 contains the wrong reception floor and should not remain the active guide. The brief does not supply the correct floor number, so the correction must point to the current guide rather than invent directions.',
    precision_extra='Kai needs viewing access, not an assumed right to edit or share with everyone. Elena should ask the document owner to resolve the problem through the appropriate process. A shared folder is not necessarily open to every recipient.',
    phrases='''Own the error | I sent version 2 in my earlier message.
Name the replacement | Version 3 was approved this morning.
Identify the affected detail | The older guide gives the wrong reception floor.
Direct recipients clearly | Please use version 3 in the shared folder.
Avoid guessed directions | I will not quote a floor number I have not verified.
Ask about access | Can you open the current guide?
Acknowledge the obstacle | You are receiving an access error.
Name the needed permission | You need viewing access to the approved guide.
Keep editing separate | Viewing access is not a request for editing rights.
Route the request | I will ask the document owner to resolve the permission.
Avoid widening access | I will not make the folder available to everyone.
Retire the old reference | The earlier attachment is superseded.
Correct the distribution | I will send the correction to the affected recipients.
Preserve the authoritative source | The current file remains in the shared folder.
Keep completion honest | Access has been requested, not confirmed.
Close with two actions | Replace the outdated reference and resolve viewing access.''',
    notes='''Superseded | Marks the older version as replaced rather than still equally valid.
Approved this morning | Specifies why version 3 is current.
Can you open ...? | Checks viewing access without asking for an edit.
Requested, not confirmed | Distinguishes submission from successful resolution.
Affected recipients | Identifies the relevant audience without expanding distribution.
I will not quote | Prevents guessed location information from entering the correction.''',
    d='''Which correction is accurate? | Use approved version 3; version 2 has the wrong reception floor | Use either version because both arrived by email | Reception is on an invented floor | Version 4 has automatically replaced both files | The correction identifies the actual current version and the known error.
What permission does Kai need here? | Viewing access | Ownership of the folder | Permission to edit every file | A public link for anyone | The stated problem concerns opening the guide, not editing or unrestricted sharing.
Which action exceeds Elena's supplied authority? | Making the folder public | Asking the owner for viewing access | Correcting the earlier message | Identifying version 2 as superseded | Independently widening permissions is explicitly outside the supplied task.
What should Elena avoid claiming? | Kai's access is fixed before confirmation | Version 3 was approved this morning | Version 2 gives the wrong floor | The owner should receive the request | A request for access does not prove that access has been granted or tested.''',
    dialogue='''Kai | I've got your emailed visitor guide and a message about a newer one. Which should I use for the people arriving today?
Elena | Use the [[approved version::Approved version is version 3, accepted this morning and replacing the outdated guide Elena sent.]], version 3, approved this morning. I sent version 2 earlier, and its reception-floor information is wrong. I'm sorry for the confusion.
Kai | Can you tell me the correct floor now? I don't want to forward two different sets of directions.
Elena | I need to verify it in the [[current guide::Current guide is the authoritative version 3, which should supply the floor rather than Elena guessing.]]. I won't guess a number; version 3 in the shared folder is the replacement source.
Kai | I tried that link. It says I don't have permission, so I can only open the old attachment.
Elena | Then you need [[viewing access::Viewing access is the permission Kai needs to open the approved guide without requesting editing authority.]] to version 3. I'll ask the document owner to resolve that separately from correcting my earlier message.
Kai | Could you just make the link open to anyone? That might be quicker than waiting for the owner.
Elena | I shouldn't widen the [[permission scope::Permission scope defines who can access the file, and Elena must not expand it independently.]] on my own. I'll request access for you, not open the folder to an unrestricted audience.
Kai | I only need to read it. Please don't ask for editing rights on my behalf.
Elena | I'll make the [[access request::Access request should ask for Kai's viewing permission, not unnecessary editing or public-sharing rights.]] specific: Kai needs to view the approved visitor guide, version 3, and the current link returns an error.
Kai | While that's pending, should I leave the old attachment in the visitor email as a temporary fallback?
Elena | No. It's [[superseded::Superseded means version 2 has been replaced and should not remain the active source of visitor directions.]] and contains a known error. Leaving it as the active guide would keep sending people to the wrong place.
Kai | Please make the correction easy to spot. There are several messages in the thread, and a quiet edit would be missed.
Elena | I'll send a clear [[correction notice::Correction notice explicitly identifies the outdated message and directs recipients to the approved replacement.]] identifying the earlier attachment, the reception-floor error, and version 3 as its replacement.
Kai | Once you've sent the owner the request, can I tell my colleague the link is fixed?
Elena | Not yet. The [[access error::Access error remains unresolved until the appropriate permission is established and access is confirmed.]] remains unresolved until the permission and actual access are confirmed. I'll describe the request as pending.
Kai | So one action corrects the information for everyone who received it, and the other resolves my ability to open the right file.
Elena | Exactly. The [[replacement message::Replacement message corrects the earlier communication while the separate viewing-access request remains visible.]] will correct the reference, while the access request stays visible as a separate follow-up.
Kai | Thank you. I won't forward version 2 or say I can open version 3 until it's working.
Elena | I'll keep the [[document owner::Document owner is the appropriate contact for resolving the requested viewing permission without unauthorized sharing.]] involved and report the confirmed status. The next update won't invent a floor number or claim the access change is complete.''',
    rehearsal=["Complete the version-and-access dialogue.","Read the correction and access request aloud. Name version 3, the outdated reception-floor detail, viewing access, and the document owner.","Complete the transfer and check the key. Keep access requested separate from access confirmed."],
    transfer_title='Correct the guide and request the right access',
    transfer_setup='Complete the document handoff. Identify the current version, the known error, and the appropriate permission route.',
    transfer='''Assistant: "The approved guide is version ___." | 3 | Version 3 was approved this morning and supersedes the earlier attachment.
Recipient: "The older version has the wrong reception ___." | floor | Floor is the specific outdated detail identified in the brief.
Assistant: "You need ___ access to the current guide." | viewing | Viewing allows the required reading without assuming editing or public-sharing rights.
Recipient: "Please ask the document ___ to resolve it." | owner | Owner is the appropriate role for the access request under the supplied instructions.'''
))

BOOK['units'].append(unit(
    title='Querying office supplies and delivery differences',
    scene='Twelve on the note, ten in the shipment',
    skill='Present a documented quantity discrepancy and request the missing supply information without inventing a cause or approving payment.',
    brief='Purchase order P44 is for twelve archive boxes. The delivery note also lists twelve, but assistant Omar has checked the shipment and counted ten. No second package or backorder is documented. Supplier contact Leila must receive a factual query asking about the outstanding two and whether another shipment is planned. Omar has no basis to allege theft, assume a split delivery, or approve payment from the information available.',
    cast='Omar | Office assistant\nLeila | Supplier contact',
    culture=('Use matching references and neutral discrepancy language', 'A clear supplier query separates the order, the document, and the checked physical count. Ask for confirmation of the outstanding quantity and delivery position. An unexplained difference is not proof of dishonesty, and a document alone does not establish receipt.'),
    a='''How many archive boxes were ordered? | Twelve | Ten | Two | Twenty-two | Purchase order P44 explicitly requests twelve archive boxes.
What quantity was physically checked? | Ten boxes | Twelve boxes | Two boxes | An uncounted second package | Omar checked the shipment and found ten rather than the twelve listed.
What is documented about a second shipment? | Nothing is confirmed | It definitely arrives tomorrow | It was received yesterday | It has been canceled by Omar | No second package or backorder is documented in the supplied facts.''',
    vocabulary='''purchase order | Formal order record specifying requested goods or services; abbreviated PO. | quote the purchase order
archive box | Container used to store records or documents. | order archive boxes
ordered quantity | Number of units requested on the order. | verify the ordered quantity
delivery note | Document listing goods associated with a delivery. | compare the delivery note
checked count | Quantity established by the stated physical check. | report the checked count
short delivery | Receipt of fewer units than the order or document specifies. | query a short delivery
quantity discrepancy | Difference between relevant stated or counted quantities. | report a quantity discrepancy
outstanding quantity | Ordered amount not yet accounted for as received. | confirm the outstanding quantity
backorder | Order quantity awaiting later fulfillment. | verify a documented backorder
split shipment | Order delivered in more than one consignment. | confirm a split shipment
second package | Additional parcel distinct from the checked one. | verify a second package
shipment plan | Stated arrangement for dispatching the remaining goods. | request the shipment plan
supplier query | Request to clarify information held by the vendor. | raise a supplier query
order reference | Identifier connecting an inquiry to the correct order. | include the order reference
receipt record | Account of goods actually received. | preserve the receipt record
dispatch record | Information documenting goods sent from the supplier. | check the dispatch record
packing list | List describing the contents assigned to a package or shipment. | compare the packing list
unit count | Number of individual items rather than cartons or sets. | confirm the unit count
fulfillment | Completion of the relevant supply obligation. | distinguish partial fulfillment
partial receipt | Receipt of only part of the ordered amount. | record a partial receipt
payment approval | Authorization to pay the relevant charge. | keep payment approval separate
supplier response | Information returned in answer to the query. | request a supplier response
unverified explanation | Possible cause not established by the evidence. | avoid an unverified explanation
delivery reconciliation | Comparison of order, documents, and received quantities. | complete delivery reconciliation''',
    precision='Twelve were ordered and twelve appear on the delivery note, but ten were checked in the shipment. The difference is two. Do not change the checked count to match the paper or claim that the missing two have already been dispatched.',
    precision_extra='The supplier should confirm the outstanding quantity and whether another shipment is planned. No documented backorder, second package, theft, or payment approval is supplied. Keep the discrepancy open until the relevant evidence resolves it.',
    phrases='''Identify the order | I am calling about purchase order P44.
State the ordered amount | The order is for twelve archive boxes.
State the document amount | The delivery note also lists twelve.
State the checked count | We checked the shipment and counted ten.
Calculate the difference | Two boxes are not accounted for in this receipt.
Use neutral language | There is a quantity discrepancy to resolve.
Ask about outstanding supply | Can you confirm the outstanding two boxes?
Check for another shipment | Is a further shipment planned?
Avoid assuming a backorder | We have no documented backorder.
Avoid inventing a package | No second package is recorded.
Separate document and receipt | The note lists twelve, but our checked receipt is ten.
Request the supporting record | Please check the dispatch information against P44.
Keep the cause open | We have not established why the quantities differ.
Avoid an accusation | I am reporting the count, not alleging theft.
Preserve approval limits | This query does not approve payment.
Close with the requested response | Please confirm the remaining quantity and shipment position.''',
    notes='''Lists versus counted | Separates what a document says from the physical check.
Not accounted for | Describes an unresolved quantity without assigning blame.
Further shipment | Asks about a possibility without claiming it exists.
Against P44 | Anchors the check to the correct order.
No documented | Limits the statement to available records rather than claiming absolute impossibility.
Does not approve | Prevents a query from becoming a financial authorization.''',
    d='''Which statement preserves all three quantities? | P44 orders twelve, the note lists twelve, and the checked shipment contains ten | P44 orders ten and all twelve arrived | The note proves twelve were received | Two additional boxes have definitely shipped | The correct statement keeps the order, delivery document, and physical count distinct.
What is the outstanding difference? | Two boxes | Twelve boxes | Ten boxes | Twenty-two boxes | Twelve ordered minus ten counted leaves two boxes unaccounted for.
Which question is justified? | Is another shipment planned for the outstanding two? | Why did your driver steal two boxes? | Can I record a second delivery as completed? | Which payment have we already approved? | The question seeks missing supply information without inventing a cause or status.
Which record should remain accurate? | The checked receipt of ten | An invented receipt of twelve | A confirmed backorder with no evidence | An automatic payment approval | The receipt record must preserve the actual checked quantity despite the document discrepancy.''',
    dialogue='''Omar | Could you check P44, our archive-box order? The quantity on the paperwork doesn't match what we received.
Leila | Certainly. Please give me the [[ordered quantity::Ordered quantity is twelve archive boxes, the amount specified on purchase order P44.]] first, then the delivery-note figure and your checked count. That will help me keep the three records separate.
Omar | We ordered twelve. The note says twelve too, but I've checked the shipment and counted ten.
Leila | Then the [[quantity discrepancy::Quantity discrepancy is the difference between twelve ordered and documented and ten physically checked.]] is two boxes. I will not treat the delivery-note figure as proof that twelve were physically received at your office.
Omar | There isn't a second package or backorder recorded here. Has something been sent separately?
Leila | Understood. A [[split shipment::Split shipment would mean more than one consignment, but no such arrangement is documented here.]] has not been documented in the information you have. I need to check rather than tell you another package is already on its way.
Omar | Please confirm the outstanding two and whether another shipment is planned. I need both points answered.
Leila | I will check the [[outstanding quantity::Outstanding quantity is the two ordered boxes not yet accounted for in the checked receipt.]] against P44 and ask about the shipment position. At this point, I do not have a confirmed dispatch date to give you.
Omar | Keep archive boxes beside P44, please. We've got several office-supply orders open.
Leila | I will retain the [[order reference::Order reference P44 links the archive-box discrepancy to the correct supply transaction.]] and the archive-box description together. The query is twelve ordered, twelve on the note, ten checked, with two outstanding.
Omar | Should I leave the receiving record at ten while you check? Someone suggested matching it to the delivery note.
Leila | You should preserve the [[checked count::Checked count is ten, and it must not be changed merely to match the delivery paperwork.]] of ten in this query. We need to resolve the mismatch, not make it disappear by replacing the physical count with the document figure.
Omar | I want to report the difference without blaming the driver. We don't know why it happened.
Leila | Agreed. The [[supplier query::Supplier query requests clarification of the missing supply facts without accusing anyone of wrongdoing.]] can ask for confirmation without alleging theft or blaming a particular person. The current evidence does not establish a cause.
Omar | Could you compare the dispatch record with P44? I don't want to assume the missing two were held back.
Leila | I will request the relevant [[dispatch record::Dispatch record may clarify what was sent, but its contents have not yet been confirmed in the conversation.]] check. I will not say the boxes were held back unless the information supports that explanation.
Omar | And this query isn't payment approval or permission to close the discrepancy.
Leila | Understood. [[Payment approval::Payment approval is separate from the supply query and has not been given by Omar.]] is not part of this exchange. The query remains open while the outstanding quantity and any further shipment are being confirmed.
Omar | Please come back with the quantity and shipment position, not just an acknowledgment that you received the query.
Leila | I will make the requested [[supplier response::Supplier response should address both the outstanding two boxes and the unconfirmed further-shipment position.]] specific to those questions. Until then, the record remains ten received against twelve ordered, with two still unaccounted for.''',
    rehearsal=["Complete the supplier-query dialogue.","Read the quantities aloud: twelve ordered, twelve on the note, ten counted, two outstanding. Then ask the supplied further-shipment question.","Complete the transfer, check the key, and reread the factual query without adding a cause or payment approval."],
    transfer_title='State the supply discrepancy without guessing',
    transfer_setup='Complete the supplier query using the documented order and checked receipt.',
    transfer='''Assistant: "The purchase order is ___." | P44 | P44 identifies the archive-box order being queried with the supplier.
Supplier: "The order and delivery note both list ___ boxes." | twelve | Twelve is the documented ordered quantity and delivery-note quantity.
Assistant: "The checked shipment contains ___ boxes." | ten | Ten is the actual checked receipt and must remain distinct from the paperwork.
Supplier: "The outstanding difference is ___ boxes." | two | Two is the difference between twelve ordered and ten physically checked.'''
))


BOOK['units'].append(unit(
    title='Welcoming visitors and checking arrangements',
    scene='Two Jordans, one visitor reference',
    skill='Welcome a visitor, distinguish two possible hosts, and explain the waiting arrangement while preserving the actual access boundary.',
    brief='Visitor Taylor arrives for a 10:00 meeting with Jordan. Two colleagues share that first name: Jordan Chen in facilities and Jordan Patel in sales. Visitor reference V12 names Jordan Chen. Receptionist Nia must check the reference, contact the correct host, and explain that Taylor should wait at reception. Taylor is not cleared to enter other areas alone. No host arrival time or further access permission has been confirmed.',
    cast='Taylor | Visitor\nNia | Receptionist',
    culture=('Warmth and verification belong in the same welcome', 'A friendly reception need not rely on guessing who a visitor means. Explain the small ambiguity, use the appointment reference, and say what happens next. A waiting instruction should sound like a clear arrangement, not a personal suspicion or an invented promise about the host.'),
    a='''Which Jordan is named on V12? | Jordan Chen in facilities | Jordan Patel in sales | Both Jordans jointly | An unnamed finance colleague | The visitor reference explicitly identifies Jordan Chen in facilities.
Where should Taylor wait? | At reception | Alone in the facilities work area | In any available meeting room | At the sales desk without checking | Taylor has not been cleared to enter other areas alone.
What is not confirmed? | When the host will reach reception | The reference V12 | The scheduled 10:00 meeting | The existence of two Jordans | No host arrival time is provided in the supplied information.''',
    vocabulary='''reception | Area where visitors first report and are assisted. | wait at reception
visitor reference | Identifier linking a visitor to an arrangement. | check the visitor reference
host | Person responsible for receiving the visitor. | contact the host
appointment record | Information describing a scheduled visit or meeting. | check the appointment record
surname | Family name used to distinguish people with the same first name. | confirm the surname
facilities | Workplace function associated with relevant building services. | identify the facilities host
sales | Business function associated with selling products or services. | distinguish the sales colleague
scheduled time | Time recorded for the arranged meeting. | confirm the scheduled time
arrival | Visitor's appearance at the location. | acknowledge the arrival
check-in | Initial process for recording or verifying a visitor's arrival. | complete the check-in
waiting area | Designated place where a person remains before being received. | explain the waiting area
host notification | Message informing the host that the visitor has arrived. | send the host notification
access clearance | Confirmed permission to enter a defined area. | verify access clearance
unaccompanied access | Permission to enter or move without an escort. | distinguish unaccompanied access
escort | Authorized person accompanying a visitor where required. | confirm the escort arrangement
visitor badge | Identifier issued under the relevant visitor procedure. | follow the visitor-badge procedure
visitor log | Record of arrivals and relevant visit details. | update the visitor log
restricted area | Space whose entry is limited by the applicable rules. | identify a restricted area
identity match | Agreement between the person or name and the relevant record. | verify the identity match
appointment ambiguity | Uncertainty about which arrangement or host is intended. | resolve appointment ambiguity
reception wait | Period spent at reception pending the next arrangement. | explain the reception wait
host availability | Whether the intended host can presently respond. | check host availability
arrival estimate | Expected arrival time that has not necessarily been confirmed. | qualify an arrival estimate
visitor handoff | Transfer of responsibility for receiving the visitor. | coordinate the visitor handoff''',
    precision='Reference V12 names Jordan Chen in facilities, not Jordan Patel in sales. The first name alone is insufficient because both colleagues are called Jordan. Preserve the reference and full name when contacting the host.',
    precision_extra="The appointment is scheduled for 10:00, but the host's immediate availability has not been confirmed. Taylor should wait at reception and has no clearance to enter other areas alone. Do not invent a two-minute wait, badge requirement, or escort arrival.",
    phrases='''Open warmly | Good morning. Who are you here to see?
Acknowledge the booking | You have a 10:00 meeting with Jordan.
Explain the ambiguity | We have two colleagues called Jordan.
Ask for the reference | May I check your visitor reference?
Read back the identifier | I have V12.
Confirm the full name | That reference names Jordan Chen.
Distinguish the department | Jordan Chen is in facilities, not sales.
State the next action | I will contact your host.
Explain the wait | Please wait here at reception while I contact Jordan.
Keep the tone helpful | I want to make sure you reach the correct person.
Avoid invented timing | I do not yet have a confirmed arrival time for the host.
Keep access explicit | You are not cleared to enter the other areas alone.
Separate appointment and entry | The meeting reference does not give unaccompanied access.
Preserve the record | I will keep V12 with your arrival message.
Check the understanding | Is the host name on that readback correct?
Close with the arrangement | Jordan Chen will be contacted; please remain at reception for the next update.''',
    notes='''We have two | Explains why a clarification is necessary without blaming the visitor.
That reference names | Grounds the identification in a record rather than a guess.
While I contact | Connects the wait with the next action without giving a false duration.
Not yet | States an unresolved fact without denying a possible later arrangement.
Alone | Specifies the unaccompanied-access boundary.
Please remain | Gives a courteous, concrete waiting instruction.''',
    d='''Which host message is accurate? | Taylor is at reception for V12 with Jordan Chen at 10:00 | Taylor is meeting Jordan Patel in sales | Both Jordans must attend | Taylor has entered facilities alone | The message retains the visitor, reference, host, time, and current waiting location.
Which sentence is courteous and accurate? | Please wait at reception while I contact Jordan Chen | Go anywhere while we look for Jordan | Jordan will definitely be here in two minutes | Your appointment means you can enter alone | The instruction states the supplied waiting arrangement without inventing timing or access.
What resolves the first-name ambiguity? | V12 and the full host name | Assuming sales receives every visitor | Choosing the first Jordan in a directory | Treating both names as interchangeable | The appointment reference identifies the specific Jordan intended for this visit.
Which fact must remain separate from the booking? | Permission to enter other areas alone | The scheduled 10:00 meeting | The reference V12 | Jordan Chen's department | A meeting arrangement does not itself establish the supplied unaccompanied-access permission.''',
    dialogue='''Taylor | Good morning, Taylor here for a ten o'clock meeting with Jordan. I've got the confirmation on my phone.
Nia | Welcome. May I check the [[visitor reference::Visitor reference V12 identifies the intended arrangement and resolves which Jordan is the host.]]? We have two colleagues called Jordan, so I want to contact the right person before directing you anywhere.
Taylor | It's V12. I remembered Jordan's first name but not the surname.
Nia | Thank you. The [[appointment record::Appointment record for V12 names Jordan Chen in facilities for the scheduled ten o'clock meeting.]] names Jordan Chen in facilities. The other colleague is Jordan Patel in sales, so we have resolved that ambiguity.
Taylor | Yes, Jordan Chen is right. I might have ended up in sales if you hadn't checked.
Nia | I will send the [[host notification::Host notification tells Jordan Chen that Taylor has arrived and is waiting at reception.]] to Jordan Chen, using V12 and your name. Please wait here at reception while I make contact.
Taylor | Do you know if Jordan's already coming down? The meeting is at ten.
Nia | I have not confirmed [[host availability::Host availability is not established merely because the appointment is scheduled for ten.]] yet. I can contact Jordan, but I do not want to promise an arrival time before I have that information.
Taylor | Could I wait near the facilities office instead, so I'm easier to find?
Nia | Please remain in the [[waiting area::Waiting area is reception, where Taylor should remain pending the next arrangement.]] here for now. You have not been cleared to enter the other areas alone, and I do not want to send you beyond the current arrangement.
Taylor | Understood. I thought the meeting confirmation might be enough to go through.
Nia | Yes. The reference identifies your visit; it does not itself establish [[unaccompanied access::Unaccompanied access is separate from the meeting reference and has not been granted to Taylor.]]. I will keep the next step clear while we contact the correct host.
Taylor | Please tell Jordan I've arrived, rather than just asking whether the meeting's still on.
Nia | Certainly. The [[arrival::Arrival is the fact that Taylor is presently at reception, not merely a future appointment inquiry.]] message will say Taylor is at reception for the ten o'clock meeting, reference V12. It will not describe this as a new booking request.
Taylor | Reception is fine. I don't need a different room; I just need Jordan to know where I am.
Nia | I will keep the [[reception wait::Reception wait is the agreed current arrangement, without inventing another room or host arrival estimate.]] as the arrangement. No alternative room or entry route has been agreed, so I will not add one to the message.
Taylor | Could you repeat the full name and department once? I'd like to use the right surname.
Nia | Jordan Chen in facilities. Confirming the [[surname::Surname Chen distinguishes the intended host from Jordan Patel in sales.]] prevents confusion with Jordan Patel in sales. Your reference is V12, and you are waiting here at reception.
Taylor | Thank you. I'll stay here for the next update.
Nia | You are welcome. I will coordinate the [[visitor handoff::Visitor handoff concerns the next confirmed reception arrangement rather than an assumed right to enter alone.]] once the host response is available. For now, the correct host has been identified and the waiting instruction is clear.''',
    rehearsal=["Complete the reception dialogue.","Read the welcome and waiting exchanges aloud. Keep V12, Jordan Chen in facilities, 10:00, and reception together.","Complete the transfer and check the key. Reread the waiting instruction without inventing a host-arrival time."],
    transfer_title='Welcome the visitor and identify the correct host',
    transfer_setup='Complete the reception readback using the reference and the actual waiting arrangement.',
    transfer='''Receptionist: "The visitor reference is ___." | V12 | V12 identifies Taylor's meeting arrangement with the intended host.
Visitor: "I am meeting Jordan ___." | Chen | Chen distinguishes the facilities host from Jordan Patel in sales.
Receptionist: "Your host works in ___." | facilities | Facilities is the department associated with Jordan Chen in the supplied record.
Visitor: "I will wait at ___." | reception | Reception is the stated waiting location until the next arrangement is confirmed.'''
))

BOOK['units'].append(unit(
    title='Clarifying travel options and booking status',
    scene='A higher fare with a conditional refund',
    skill='Compare two supplied rail quotes, explain the conditional refund amount, and distinguish a comparison from an approved booking.',
    brief="Two fictional rail quotes cover the same trip. Option A costs $70 and is nonrefundable. Option B costs $90 and permits a refund before departure with a $10 deduction. Traveler Mira's meeting is not yet confirmed, and purchasing approval is still required. Assistant Ben must compare the quoted terms accurately without choosing for Mira, promising a full refund, or treating the discussion as authority to book.",
    cast='Mira | Traveler\nBen | Administrative assistant',
    culture=('Explain the condition as carefully as the price', "The word refundable can hide a deadline and a deduction. State the upfront price, the condition, and the resulting amount together. A useful comparison helps an authorized decision without turning the assistant's explanation into a booking or financial recommendation."),
    a='''What is the price difference between the quotes? | $20 | $10 | $80 | $160 | Option B costs $90 and option A costs $70, so the difference is $20.
Under the supplied terms, what refund does B permit before departure? | $80 | $90 | $70 | No refund under any circumstances | The $90 fare less the stated $10 deduction leaves an $80 refund before departure.
What must happen before purchase? | Obtain the required purchasing approval | Treat this discussion as a booking | Assume the meeting is confirmed | Ignore the quoted conditions | Purchasing approval is explicitly still required before the assistant can book.''',
    vocabulary='''rail quote | Stated price and conditions for a proposed train journey. | compare rail quotes
fare | Price charged for the specified travel. | state the fare
nonrefundable | Not permitting a refund under the stated quoted terms. | identify a nonrefundable fare
refundable | Permitting a refund subject to the applicable conditions. | qualify refundable
deduction | Amount subtracted from a payment or refund. | explain the deduction
before departure | Earlier than the stated leaving time. | preserve the before-departure condition
refund amount | Sum returned under the applicable refund terms. | calculate the refund amount
upfront cost | Amount paid at the time of purchase. | compare upfront costs
price difference | Amount by which one price exceeds another. | state the price difference
quoted terms | Conditions included in the supplied offer. | preserve the quoted terms
booking status | Current stage of a travel reservation or purchase. | clarify booking status
purchasing approval | Required permission to commit the organization to a purchase. | obtain purchasing approval
unconfirmed meeting | Meeting whose occurrence or arrangement is not yet settled. | identify the unconfirmed meeting
itinerary | Planned sequence and details of travel. | check the itinerary
cash advance | Money provided before eligible expenses are settled, to be reconciled against the applicable claim. | reconcile the cash advance
cancellation | Withdrawal from an existing booking under its terms. | distinguish cancellation from comparison
refund eligibility | Whether the relevant conditions for a refund are met. | check refund eligibility
fare condition | Restriction or permission attached to a ticket price. | explain the fare condition
expense itemization | Separation of an expense into its component amounts and categories. | check expense itemization
net refund | Amount returned after the stated deduction. | calculate the net refund
travel authorization | Approval for travel within a defined scope. | distinguish travel authorization
reservation | Arrangement holding travel space under specified terms. | verify a reservation
ticket issuance | Creation or provision of the actual travel ticket. | distinguish ticket issuance
conditional comparison | Explanation that preserves the conditions affecting the alternatives. | give a conditional comparison''',
    precision='A costs $70 and is nonrefundable under these quoted terms. B costs $90 and permits a refund before departure less $10, leaving $80. B costs $20 more upfront; the $10 deduction is not the price difference.',
    precision_extra='The $80 refund applies only under the supplied before-departure condition. Do not invent later refund rights, transferability, fees, or legal protections. The meeting is unconfirmed and purchasing approval is still needed; no ticket has been authorized by this comparison.',
    phrases='''Define the comparison | Both quotes cover the same trip.
State option A | A costs $70 and is nonrefundable.
State option B | B costs $90.
Include the condition | B permits a refund before departure.
Include the deduction | The refund is reduced by $10.
Calculate the returned amount | Ninety minus ten leaves an $80 refund.
Compare upfront prices | B costs $20 more upfront.
Avoid a full-refund claim | Refundable does not mean the full $90 comes back.
Keep later terms open | No after-departure refund terms are supplied here.
Preserve meeting status | Your meeting is not confirmed yet.
Keep the choice separate | I can explain the options without choosing for you.
State the approval requirement | Purchasing approval is still required.
Avoid an accidental booking | This comparison is not a ticket purchase.
Distinguish the two amounts | The $20 premium and $10 deduction are different figures.
Request the next decision | Please confirm the authorized choice before any booking.
Close accurately | The prices and conditions are clear; the booking remains unapproved.''',
    notes='''Subject to | Introduces a condition that limits a general statement.
Before departure | Defines when the stated refund permission applies.
Less ten | Expresses the deduction from the ninety-dollar payment.
Upfront | Refers to the initial price rather than a later refund.
Not confirmed yet | Preserves the uncertainty about the travel purpose.
Before any booking | Keeps the approval decision ahead of spending.''',
    d='''Which comparison is complete? | A is $70 nonrefundable; B is $90 with an $80 refund before departure | B is $90 with a guaranteed full refund anytime | A and B both cost $80 | B costs only $10 more than A | The comparison retains both prices and B's conditional refund after the deduction.
What does the $10 represent? | The deduction from B's refund | The difference between the fares | A separate confirmed booking fee | The entire price of option A | The supplied $10 is subtracted from B's $90 refund, not from the price comparison.
Which claim is unsupported? | B is refundable after departure without restrictions | B costs $90 | A costs $70 | Approval is required | The supplied terms establish a before-departure refund only, with no later rule provided.
Which handoff is ready for the approver? | Both quotes with conditions, meeting unconfirmed, no purchase approved | B selected because its refund makes it cheaper to buy | A booked because it has the lower upfront price | B reserved with a full refund guaranteed after departure | A comparison can be passed for decision without selecting a fare, issuing a ticket, or extending the supplied refund terms.''',
    dialogue='''Mira | My meeting isn't confirmed, so please don't book yet. Could you explain the two quotes for the same rail trip?
Ben | Yes. Option A has a [[fare::Fare is the upfront travel price: seventy dollars for A and ninety dollars for B.]] of seventy dollars, and option B is ninety. The important difference is not only the price but also the refund conditions.
Mira | A says nonrefundable. Is that the condition we're using for the seventy-dollar option?
Ben | Correct. A is [[nonrefundable::Nonrefundable describes option A under the supplied quoted terms without inventing additional exceptions.]] under these quoted terms. For B, a refund is permitted before departure, but ten dollars is deducted from the amount returned.
Mira | For B, how much would actually come back? Refundable sounds like ninety, but there's a deduction.
Ben | The [[net refund::Net refund is eighty dollars after subtracting the stated ten-dollar deduction from B's ninety-dollar fare.]] would be eighty dollars: ninety less ten. We should state the condition and the deduction together rather than simply describe B as refundable.
Mira | I nearly treated the ten dollars as the price difference. That's the amount retained from a refund, isn't it?
Ben | Exactly. The [[upfront cost::Upfront cost is the purchase price, separate from the amount retained if a conditional refund occurs.]] is seventy for A or ninety for B. The ten-dollar deduction belongs to B's refund terms; it is not B's purchase price.
Mira | So B costs twenty more to buy, while the refund deduction is ten. Those aren't the same comparison.
Ben | Right. The [[price difference::Price difference is twenty dollars because the quoted fares are ninety and seventy dollars.]] is twenty dollars. Keeping those two figures separate prevents a misleading comparison, especially when you are explaining the options to the approver.
Mira | What happens after departure? Does this quote actually say?
Ben | The supplied condition is [[before departure::Before departure is the stated refund condition, and no after-departure permission is supplied.]]. We have no later refund terms here, so I cannot extend the eighty-dollar calculation to an after-departure cancellation.
Mira | Please keep this as a comparison. Asking about refunds isn't an instruction to buy a ticket.
Ben | I will keep the [[booking status::Booking status remains unapproved because a comparison and questions do not authorize a purchase.]] clear. This is a comparison, not a reservation or ticket purchase, and purchasing approval is still required before any commitment.
Mira | Can you give me a short summary for the approver without saying I've selected one?
Ben | Certainly. The [[conditional comparison::Conditional comparison presents the two prices and B's limited refund without choosing or booking for Mira.]] is A at seventy, nonrefundable; B at ninety, with an eighty-dollar refund before departure after the ten-dollar deduction.
Mira | Add that the meeting's still unconfirmed, please. That's why I'm checking the conditions.
Ben | I will preserve the [[unconfirmed meeting::Unconfirmed meeting describes the unresolved travel purpose without converting it into a recommendation or cancellation.]] status alongside the quotes. The decision-maker should see the actual circumstances, not a message implying that the trip is already settled.
Mira | I'll get the choice and purchasing approval clarified. Nothing should be booked on the strength of this conversation.
Ben | Agreed. [[Purchasing approval::Purchasing approval is the missing authorization required before Ben can turn the comparison into a booking.]] remains outstanding. I will not issue a ticket or record an authorized choice until the required confirmation is available.''',
    rehearsal=["Complete the travel-comparison dialogue.","Read both quotes aloud: A $70 nonrefundable; B $90, refund $80 before departure. Then read the separate approval requirement.","Complete the transfer and check the key. Keep the $20 purchase-price difference separate from the $10 refund deduction."],
    transfer_title='State the price and the refund condition',
    transfer_setup='Complete the comparison using the supplied fares and terms. Do not turn the comparison into a booking.',
    transfer='''Assistant: "Option A costs ___ dollars." | seventy | Seventy is the nonrefundable option's stated upfront price.
Traveler: "Option B costs ___ dollars." | ninety | Ninety is B's purchase price before any later conditional refund.
Assistant: "Before departure, B permits an ___-dollar refund." | eighty | Eighty is ninety minus the stated ten-dollar refund deduction.
Traveler: "Purchasing ___ is still required." | approval | Approval remains necessary because discussing the alternatives does not authorize a ticket purchase.'''
))


BOOK['units'].append(unit(
    title='Prioritizing work and handing over coverage',
    scene='Eighty minutes of work in a sixty-minute window',
    skill='Explain a capacity conflict with concrete timings and ask the manager to select a priority or change a deadline.',
    brief='At 10:00, assistant Rosa has a visitor list due at 10:30 and a room pack due at 11:00. Each requires thirty minutes. Manager Ellis requests a new twenty-minute spreadsheet check by 10:20. No colleague is available to help. Rosa must explain the conflict and ask Ellis to choose priorities or adjust a deadline. The case ends with that decision still needed; Rosa cannot truthfully promise all three original deadlines.',
    cast='Rosa | Administrative assistant\nEllis | Manager',
    culture=('Make the trade-off concrete, not personal', 'Saying that you are busy does not show which commitment will move. State the existing deadlines and task durations, then ask for a priority decision. Respectful pushback gives the manager an accurate choice without silently accepting an impossible schedule or delegating to an unavailable colleague.'),
    a='''What is due at 10:30? | The visitor list | The room pack | The new spreadsheet check | An already completed handover | The visitor list has the earliest of the two original deadlines.
How much work is requested in total? | Eighty minutes | Sixty minutes | Thirty minutes | Twenty minutes | Two thirty-minute tasks plus a twenty-minute check total eighty minutes.
What should Rosa ask Ellis to do? | Choose priorities or adjust a deadline | Assume all three will be on time | Assign the work to an unavailable colleague | Treat the durations as zero | The supplied capacity conflict requires a decision about priorities or timing.''',
    vocabulary='''workload | Amount of work assigned or awaiting completion. | explain the workload
capacity | Available ability or time to carry out work. | state the capacity limit
priority decision | Choice about which task takes precedence. | request a priority decision
deadline | Latest required completion time for a task. | clarify the deadline
task duration | Time needed to perform the stated work. | specify task duration
visitor list | Record of expected visitors for the relevant arrangement. | prepare the visitor list
room pack | Set of materials prepared for use in the meeting room. | assemble the room pack
spreadsheet check | Review of the specified spreadsheet information. | perform the spreadsheet check
competing request | New demand that conflicts with existing commitments. | identify the competing request
time window | Period within which work must be performed. | define the available time window
sequence | Order in which tasks are carried out. | agree the task sequence
trade-off | Consequence of choosing one priority at the expense of another. | explain the trade-off
revised deadline | Newly agreed completion requirement. | obtain a revised deadline
displaced task | Work moved later because another task takes its place. | identify the displaced task
coverage | Availability of another person to handle work during the relevant period. | confirm coverage
delegation | Assignment of a task to someone with the relevant availability and authority. | avoid unsupported delegation
commitment | Promise to complete a defined action under stated conditions. | make a realistic commitment
overcommitment | Acceptance of more work than the available capacity permits. | avoid overcommitment
schedule impact | Effect of a change on task timing. | explain the schedule impact
earliest finish | First possible completion time under the stated sequence and durations. | calculate the earliest finish
existing obligation | Task already required before the new request arrives. | preserve existing obligations
reprioritization | Change to the order or importance of assigned work. | request reprioritization
handover coverage | Confirmed support for taking over specified work. | verify handover coverage
decision readback | Repetition of the chosen priority and its consequences. | prepare a decision readback''',
    precision='At 10:00, the original two tasks already require the full sixty minutes until 11:00. The new check adds twenty minutes and is due at 10:20. Doing it first moves the earliest visitor-list finish to 10:50, beyond its 10:30 deadline.',
    precision_extra='If the sequence is spreadsheet, visitor list, then room pack, the finish times are 10:20, 10:50, and 11:20. These are consequences, not newly approved deadlines. No colleague is available, and Ellis has not yet chosen which commitment should change.',
    phrases='''Acknowledge the request | I understand you need the spreadsheet check by 10:20.
Name the existing work | The visitor list and room pack are already due this morning.
State the first deadline | The visitor list is due at 10:30.
State the second deadline | The room pack is due at 11:00.
Give the durations | Each existing task needs thirty minutes.
Add the new demand | The spreadsheet check adds twenty minutes.
Show the capacity conflict | That is eighty minutes of work between 10:00 and 11:00.
State the immediate consequence | If I do the check first, the visitor list cannot finish before 10:50.
Keep consequences conditional | That sequence would also move the room pack to 11:20.
Avoid imaginary help | No colleague is available to take over a task.
Ask for a decision | Which task should take priority?
Offer the relevant alternative | Can one of the deadlines be adjusted?
Preserve prior commitments | I need to know which existing commitment should move.
Avoid vague assent | I cannot confirm all three original deadlines.
Request explicit agreement | Please confirm the revised priority or deadline.
Close without pretending | The schedule change still needs your decision.''',
    notes='''If I do ... first | Introduces a specific scheduling consequence rather than a refusal.
Cannot finish before | States an earliest completion under the given durations.
Would also | Extends the same conditional sequence to the later task.
Which should move? | Asks for a decision about the affected commitment.
No colleague is available | Removes delegation as an invented solution.
Still needs | Keeps an unresolved decision visible in the handoff.''',
    d='''If Rosa does the check first, when can the visitor list finish at the earliest? | 10:50 | 10:20 | 10:30 | 11:20 | Twenty minutes for the check plus thirty for the list gives a 10:50 finish.
If that sequence continues with the room pack, when does it finish? | 11:20 | 10:50 | 11:00 | 10:20 | The check and two thirty-minute tasks require eighty minutes from 10:00.
Which response is professionally clear? | I need a priority choice or an adjusted deadline because these tasks require eighty minutes | I will somehow meet every original deadline | Another colleague will do it despite being unavailable | The visitor list no longer matters without asking | The response states the capacity conflict and asks the manager for an explicit decision.
What remains unresolved at the end of the case? | Which priority or deadline Ellis will change | The stated task durations | Whether a colleague is available | The original visitor-list deadline | The case supplies the conflict but does not provide Ellis's final priority decision.''',
    dialogue='''Ellis | Could you check this spreadsheet by ten twenty? It needs twenty minutes, and I'd like it ready for the next discussion.
Rosa | Before I accept the [[competing request::Competing request is the new twenty-minute spreadsheet check that conflicts with Rosa's existing commitments.]], can we look at what's already due? It's ten now, and the existing tasks fill the next hour.
Ellis | I knew about the room pack. What's the other deadline?
Rosa | The [[visitor list::Visitor list is due at 10:30 and requires thirty minutes, so it occupies the first available half hour.]] is due at ten thirty and needs thirty minutes. The room pack also takes thirty minutes and is due at eleven.
Ellis | If you start the spreadsheet right away, it finishes at ten twenty. Where does that leave the list?
Rosa | It uses twenty minutes of the [[time window::Time window from 10:00 to 11:00 contains sixty minutes, less than the eighty minutes of requested work.]]. With the list next, its earliest finish becomes ten fifty, not ten thirty.
Ellis | Could you do the list faster to catch up? I'm trying to avoid moving the visitor deadline.
Rosa | The supplied [[task duration::Task duration is thirty minutes for each existing task and cannot be silently reduced to make the schedule fit.]] is thirty minutes. I can't responsibly promise a shorter one without a basis for it.
Ellis | Then the room pack would follow the list and finish at eleven twenty. That's late as well.
Rosa | Yes. That's the [[schedule impact::Schedule impact is a 10:50 list finish followed by an 11:20 room-pack finish if the spreadsheet goes first.]] of spreadsheet, list, then room pack. Those finish times aren't approved deadline changes yet.
Ellis | Could someone else assemble the pack while you work on the check?
Rosa | There's no available [[coverage::Coverage would require another available person, which the supplied situation explicitly lacks.]]. No colleague is free, so a handover won't solve this particular conflict.
Ellis | All three feel urgent, but I see that saying urgent doesn't create another twenty minutes.
Rosa | I need a [[priority decision::Priority decision determines which task takes precedence and which existing commitment must change.]]. Should the spreadsheet come first, and if so, which existing commitment may move?
Ellis | Let me check which deadline has flexibility before answering. I don't want you to drop the list without me realizing.
Rosa | Thank you. Any [[revised deadline::Revised deadline must be explicitly agreed rather than inferred from Rosa's explanation of the conflict.]] needs explicit agreement. Until then, the list is still due at ten thirty and the pack at eleven.
Ellis | Don't treat the new request as fully accepted yet. I still need to choose what changes.
Rosa | Understood. That avoids [[overcommitment::Overcommitment would be promising all three original deadlines despite eighty minutes of work in the available hour.]]: eighty minutes of work can't fit into the available sixty while preserving these original deadlines.
Ellis | Keep the durations and consequences in front of us. I'll use those to make the choice.
Rosa | Once you decide, I'll give a [[decision readback::Decision readback follows an actual priority decision; no revised sequence or deadline is approved yet.]] of the agreed order and any changed deadline. For now, the priority choice is still outstanding.''',
    rehearsal=["Complete the priority-negotiation dialogue.","Read the proposed sequence aloud with finish times 10:20, 10:50, and 11:20. Identify them as consequences, not approved deadlines, using Rosa's supplied wording.","Complete the transfer and check the key. Repeat the final request for the still-missing priority decision."],
    transfer_title='Ask for a realistic priority decision',
    transfer_setup='Complete the workload readback. Keep calculated finish times separate from approved deadline changes.',
    transfer='''Assistant: "The three tasks require ___ minutes in total." | eighty | Eighty combines the two thirty-minute tasks and the new twenty-minute check.
Manager: "The visitor list is originally due at ___." | 10:30 | 10:30 remains the original deadline until a change is explicitly agreed.
Assistant: "If the check comes first, the list finishes no earlier than ___." | 10:50 | 10:50 follows twenty minutes for the check and thirty for the visitor list.
Manager: "A priority ___ is still needed." | decision | Decision remains outstanding because no changed priority or deadline has been approved.'''
))
