"""Original learner-book content for hospitality and tourism."""
from books.authoring import unit

BOOK = dict(
    slug='hospitality-tourism',
    title='Hospitality and Tourism English',
    cover_label='ENGLISH FOR HOSPITALITY AND TOURISM',
    cover_title='Hospitality\n& Tourism',
    cover_size=34,
    tagline='Welcome warmly. Resolve clearly. Coordinate precisely.',
    audience='For hotel, resort, venue, and tour professionals working with guests and colleagues.',
    map_intro='Eight service conversations: welcome an early arrival, answer a complaint, offer accommodation alternatives, explain room revenue, coordinate a room release, confirm an event schedule, update a disrupted tour, and clarify an individual preference.',
    notes_title='Hospitality without uncertain promises',
    notes_intro='Good service combines warmth with accurate information. Say what is confirmed, explain the available options, and take responsibility for the next communication. Keep internal shorthand out of guest-facing explanations.',
    field_notes=[
        ('Acknowledge before correcting', 'Recognize the inconvenience, then explain the relevant facts. An explanation that starts by blaming the guest can make a solvable problem harder to resolve.', '"I can see why that message suggested the room would be ready. Let me clarify what we can confirm."'),
        ('Promise the action you control', 'A check with another department and a guest update are actions you can own. A repair completion, room release, or tour departure may depend on a separate decision.', '"I will update you at one o\'clock, even if the room is still awaiting release."'),
        ('Translate operational language', 'Terms such as walk, release, and room inventory have specialist meanings. Use them precisely with colleagues and explain the practical outcome to guests.', '"We can arrange the confirmed room at the nearby hotel, with the agreed transfer included."'),
        ('Ask about the individual', 'A preference about timing, beds, conversation, or service frequency belongs to the guest. Nationality does not establish the reason or the preferred response.', '"Would you prefer service after two today, or no service today?"')],
    scope_note='All properties, people, figures, and policies in the cases are fictional. This book teaches workplace language, not legal advice or safety procedures. Follow current local rules, approved service policies, privacy requirements, and operator emergency plans. Do not treat an exercise as operational authorization.',
    sources=[
        dict(title='CoStar / STR. What Is Hotel Benchmarking?', url='https://www.costar.com/products/benchmark/resources/data-insights-blog/what-hotel-benchmarking', note='Background definitions for occupancy, average daily rate, and revenue per available room. The two-day pricing comparison and all figures are original teaching examples.', checked='30 September 2026'),
        dict(title='Google Business Profile Help. Tips to Get More Reviews.', url='https://support.google.com/business/answer/3474122', note='Background on professional public replies, privacy, and the prohibition on incentives to change or remove reviews. The complaint dialogue and property policy are fictional.', checked='30 September 2026'),
        dict(title='National Weather Service. Lightning Safety and Outdoor Sports Activities.', url='https://www.weather.gov/safety/lightning-sports', note='Background on planned weather decisions and designated responsibility for outdoor activities. The tour case supplies a fictional local hold and guest-update process, not a complete safety plan.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Guest Arrival and Front-Desk Escalation',
    scene='An early-arrival request sounded like a promise',
    skill='Acknowledge an expectation gap and give a reliable next step without inventing a room-ready time.',
    brief='Ms Vega arrives at 12:15. Her confirmation says that her early-arrival request has been noted, but she understood this as guaranteed access at noon. Standard check-in begins at 15:00. No room has yet been released, and the front desk has no verified room-ready time. Complimentary luggage storage and use of the lobby seating are available now. Front-desk agent Arun can check with housekeeping and give a personal update at 13:00 even if the status has not changed. He cannot guarantee an earlier room or authorize compensation on his own.',
    cast='Arun | Front-desk agent\nMs Vega | Arriving guest',
    culture=('Service language can create a commitment', 'Noted, requested, and confirmed can sound interchangeable to a tired traveler. Explain their difference without treating the guest as foolish. A calm apology for unclear communication can sit beside an honest limit on what is currently available.'),
    a='''What did the confirmation establish? | The early-arrival request was recorded. | A room was guaranteed at noon. | The guest had canceled her booking. | Compensation had been approved. | The wording recorded the request but did not confirm early access.
What can Arun provide now? | Complimentary luggage storage and lobby seating | A released room | An approved refund | A guaranteed 13:00 room | The brief confirms these two immediate services, not a room or financial remedy.
What does the 13:00 commitment concern? | A personal status update | Guaranteed room entry | Completion of every room inspection | The start of standard check-in | Arun controls the update; no room-ready time has been verified.''',
    vocabulary='''early arrival | Arrival before the standard check-in period. | note an early arrival
early check-in | Access to a room before the usual check-in time. | request early check-in
reservation confirmation | A message documenting a booking and its stated terms. | review the reservation confirmation
special request | A preference or need submitted with a booking. | record a special request
guaranteed access | A confirmed commitment that entry will be available. | distinguish guaranteed access
subject to availability | Dependent on whether the requested service is available. | explain subject to availability
front desk | The guest reception and service point. | contact the front desk
guest relations | The function handling guest experience and concerns. | refer to guest relations
duty manager | The manager responsible during a particular shift. | consult the duty manager
arrival time | The time a guest reaches the property. | confirm the arrival time
check-in window | The stated period when check-in begins or is expected. | clarify the check-in window
room assignment | Allocation of a particular room to a booking. | confirm a room assignment
room-ready time | The time a room is expected or confirmed to be available. | verify the room-ready time
room release | Authorization to make a prepared room available for use. | await room release
luggage storage | A service holding bags before or after room use. | offer luggage storage
claim ticket | A receipt used to identify stored belongings. | issue a claim ticket
complimentary | Supplied without an additional charge. | offer a complimentary service
lobby | The main public reception area. | use the lobby seating
status update | A report on the current position of a request. | provide a status update
expectation gap | A difference between anticipated and actual service. | acknowledge an expectation gap
service recovery | Action to address a disappointing service experience. | coordinate service recovery
authorization limit | The boundary of what an employee may approve. | respect an authorization limit
escalation | Referral to a person with relevant responsibility or authority. | explain the escalation
follow-through | Completion of an action that was promised. | ensure reliable follow-through''',
    precision='The recorded request is not a confirmed noon check-in. The 13:00 update is a communication commitment, not a room-release estimate. Standard check-in begins at 15:00; Arun should not invent a different guaranteed time.',
    precision_extra='Complimentary luggage storage does not imply compensation, a free upgrade, or automatic room access. Describe exactly what is available. If a remedy needs a manager, distinguish requesting approval from obtaining it.',
    phrases='''Acknowledge the impact | I understand that you planned around arriving at noon.
Own unclear wording | I am sorry the confirmation did not make that distinction clear.
Clarify the record | The message records your request for early access.
Separate confirmation | It does not confirm that a room is ready at noon.
State the current position | No room has been released yet.
Avoid an invented estimate | I do not have a verified room-ready time.
Offer immediate help | We can store your luggage at no additional charge.
Offer a place to wait | You are welcome to use the lobby seating.
Take the next action | I will check the status with housekeeping.
Set the update time | I will speak with you again at 13:00.
Preserve the distinction | That is an update time, not a promise of room access.
Explain the normal timing | Standard check-in begins at 15:00.
Avoid passing blame | Let me clarify the wording and the available options.
Respect approval limits | A compensation request needs the duty manager's review.
Check the guest's preference | Would you like us to store your bags now?
Close the loop | I will update you even if the status has not changed.''',
    notes='''Noted | Means recorded; it does not necessarily mean approved.
Ready | Use only when the relevant room status is confirmed.
At no additional charge | Explains complimentary in plain guest-facing language.
By versus at | By sets a latest time; at names the planned moment.
I will check | Commits to an action, not to a favorable result.
Even if | Makes the update commitment independent of a status change.''',
    d='''Which reply handles the misunderstanding best? | I see why you expected noon access; the request was recorded, but no room is released yet. | You should have understood the wording. | Your room will certainly be ready in ten minutes. | Housekeeping always causes this problem. | The correct reply acknowledges the expectation and preserves the verified room status.
Which promise is within Arun's stated control? | I will update you at 13:00 even if we are still waiting. | The room will be ready at 13:00. | I guarantee an upgrade. | I have approved a refund. | The brief authorizes a status update, not a room guarantee or financial remedy.
Which statement accurately explains complimentary storage? | We can hold your luggage without an additional charge. | Your whole stay is now free. | You must accept storage instead of a room. | Storage guarantees immediate room access. | Complimentary describes the storage charge only, not the wider booking terms.
What should Arun do if compensation is requested? | Refer the request for the duty manager's review. | Promise approval before checking. | Delete the booking to remove the dispute. | Say no manager can ever consider it. | Arun lacks personal authority to approve compensation but can seek the appropriate review.''',
    dialogue='''Ms Vega | I asked to arrive at noon, and your email said it was noted. It is already twelve fifteen. I expected to go straight to my room.
Arun | I understand your [[frustration::Frustration acknowledges the effect of the unclear message without claiming that noon access was actually guaranteed.]], and I am sorry the message was unclear. Let me check the room status and explain what we can arrange now.
Ms Vega | I have been traveling since early this morning. I would have planned differently if I had known I might be waiting.
Arun | Your [[early-arrival request::The request was recorded with the booking, but recording it did not establish guaranteed early access.]] is in the booking record. It asked for noon access, but that access was not confirmed. Standard check-in begins at three this afternoon.
Ms Vega | Is there no possibility of a room before three? Should I leave and return later?
Arun | I cannot rule out earlier availability, but I do not have a verified [[room-ready time::The room-ready time remains unknown; the agent must not replace that uncertainty with a guessed promise.]]. No room has been released yet, so I should not give you an estimate as a promise.
Ms Vega | Another hotel promised twenty minutes, and I waited nearly two hours. I would prefer an honest answer to another guess.
Arun | That is reasonable. I can offer [[complimentary::Complimentary means the luggage storage is available without an additional charge, not that the entire stay is free.]] luggage storage now, and you may use the lobby seating. I will also check directly with housekeeping rather than leave your request without a follow-up.
Ms Vega | Please store the bags. I still need to decide whether to get something to eat nearby. How will I know whether anything has changed?
Arun | I will give you a personal [[status update::A status update communicates the current position; it is the action Arun can reliably commit to at thirteen hundred.]] at one o'clock. That update will happen even if we are still waiting. One o'clock is not a confirmed time for entering the room.
Ms Vega | All right. I will stay in the lobby until then. Please do not send me to several departments to ask the same question again.
Arun | You can come back to me at the [[front desk::The front desk is the reception point where Arun remains responsible for communicating the next update.]]. I will coordinate the check with housekeeping and tell you the result, so you do not need to repeat the request elsewhere.
Ms Vega | Please also review that email. It sounded as though my early arrival had been approved.
Arun | I will pass that concern to the [[duty manager::The duty manager is the appropriate person to review the communication concern and any remedy beyond Arun's authority.]]. I can describe the wording you received and the expectation it created, without suggesting that you caused the misunderstanding.
Ms Vega | Would the manager be able to consider some compensation for the inconvenience? I understand that you may not be the person who can decide.
Arun | I can submit that for [[review::Review means the request will be considered; it does not mean compensation has already been authorized.]], but I cannot promise the outcome. For now, the confirmed arrangements are luggage storage, lobby seating, and my update at one o'clock.
Ms Vega | That is clear. I will hand over the bags now, and I will look for you here at one. Please update me even without good news.
Arun | I will. Once the bags are stored, I will give you a [[claim ticket::The claim ticket identifies the stored bags and supports their later retrieval.]] for collecting them. Please keep it with you, and let me know if you need something from the luggage while you wait.
Ms Vega | Thank you. I will wait here until one, then decide about lunch. Please come and find me even if the room is still not ready.
Arun | I will take care of the [[follow-through::Follow-through means carrying out the promised check and update, not merely making a reassuring statement.]]: check with housekeeping, pass on your concern, and find you here at one. I will distinguish an estimate from a confirmed release.''',
    transfer_title='An update is not a release time',
    transfer_setup='At 11:30, no room is released. Free luggage storage is confirmed. The agent commits to an update at 12:00 but has no verified access time.',
    transfer='''Guest: "Is noon a guaranteed time for ___?" | room access | The question concerns entry, which remains unconfirmed despite the scheduled update.
Agent: "No; noon is the time for my ___." | update | The agent controls the noon communication, not the unverified room release.
Guest: "Can you hold my ___ while I wait?" | luggage | Storage of the guest's bags is the immediate confirmed service.
Agent: "Yes, that service is ___." | complimentary | The brief explicitly states that luggage storage is free.''',
    rehearsal=['Read the completed conversation in pairs, keeping the apology warm and direct.', 'Repeat turns 9-12 and 17-20; stress one as the update time, not the room-access time.', 'Switch roles for the transfer, explaining complimentary in a natural guest-facing tone.']))

BOOK['units'].append(unit(
    title='Complaint Handling and Online Reviews',
    scene='A public reply should not become a public argument',
    skill='Acknowledge a complaint, protect booking details, and move investigation to the appropriate private channel.',
    brief='Guest-relations agent Elise reviews a draft reply to a public complaint about late-night noise. The draft accuses the guest of exaggerating and includes the room number, stay dates, and booking reference. The complaint has not yet been checked against the property records. Manager Mateo requires a brief, courteous public acknowledgement and an invitation to contact the property through its published guest-relations channel. The private review will verify relevant records before any remedy is decided. Any approved remedy must be independent of whether the guest edits or removes the review.',
    cast='Elise | Guest-relations agent\nMateo | Guest-services manager',
    culture=('A reply has more than one reader', 'A public response speaks to the reviewer and to future guests. Firmly correcting a verified fact may sometimes be appropriate, but arguing about an unverified account or revealing private details damages trust. Keep investigation and personal booking discussion in the approved private channel.'),
    a='''What is established about the noise complaint? | It has been reported but not yet checked. | It has been disproved. | Every detail has been verified. | A refund has already been approved. | The brief supplies an unverified complaint, not a completed investigation or remedy.
Which information should be removed from the public draft? | Room number, stay dates, and booking reference | A courteous acknowledgement | The published guest-relations channel | A brief invitation to contact the property | These booking details belong in the appropriate private process, not the public reply.
What may an approved remedy depend on here? | The outcome of the service review and applicable policy | Removal of the review | A five-star replacement review | Public praise for the manager | The fictional policy makes remedies independent of whether the guest changes the review.''',
    vocabulary='''public reply | A response visible to other readers of a review. | publish a public reply
reviewer | A person who posts an account or evaluation. | acknowledge the reviewer
guest feedback | Information guests provide about their experience. | respond to guest feedback
noise complaint | A report of unwanted or disruptive sound. | investigate a noise complaint
service lapse | A failure to provide an expected service standard. | verify a service lapse
acknowledgement | Recognition that a concern has been received. | give a courteous acknowledgement
defensive tone | Language focused on protecting oneself from criticism. | remove a defensive tone
personal attack | Criticism directed at the person rather than the issue. | avoid personal attacks
booking reference | An identifier for a particular reservation. | protect the booking reference
stay dates | The dates covered by a guest's visit. | verify stay dates privately
private channel | A communication route not open to public readers. | use the approved private channel
published contact details | Official contact information available to customers. | use published contact details
case record | The controlled account of a complaint and its handling. | update the case record
complaint handler | The person responsible for progressing a concern. | assign a complaint handler
factual check | Verification of a claim against relevant information. | complete a factual check
incident log | A record of reported events and actions. | consult the incident log
service remedy | An action offered to address a service problem. | authorize a service remedy
goodwill gesture | A discretionary offer intended to repair a relationship. | consider a goodwill gesture
conditional offer | An offer dependent on a stated condition. | reject an improper conditional offer
review incentive | A benefit offered to influence a review. | avoid a review incentive
reputational risk | The possibility of damage to public trust. | reduce reputational risk
response template | A reusable structure for a written reply. | adapt a response template
unverified allegation | A claim not yet established through checking. | distinguish an unverified allegation
resolution status | The current position of a complaint outcome. | report the resolution status''',
    precision='An acknowledgement is not a finding that every allegation is correct. Equally, missing verification is not proof that the guest is wrong. The public reply should not announce the result of a review that has not occurred.',
    precision_extra='Do not condition compensation or a goodwill gesture on deleting, revising, or improving a public review. Resolve the service issue under the applicable policy and keep the guest free to describe their experience.',
    phrases='''Recognize the concern | Thank you for raising your concern about the noise.
Acknowledge disappointment | I am sorry to hear that your stay was disappointing.
Avoid a premature finding | We would like to review the details with you.
Protect the booking | Please do not post your booking information publicly.
Offer a private route | Please contact our published guest-relations channel.
Remove the attack | That sentence challenges the guest's character, not the facts.
Describe the current status | The complaint has not yet been checked.
Request relevant evidence | Let us review the incident log and relevant records.
Name responsibility | I will be the contact for the private review.
Keep the reply concise | The public response needs acknowledgement and a next step.
Avoid a premature remedy | No compensation decision has been made.
Keep the remedy separate | Any remedy will not depend on changing the review.
Reject a condition | We cannot offer a benefit in exchange for removing it.
Use neutral wording | The guest reports late-night noise.
Record the outcome | Update the case record after the review is complete.
Close professionally | We welcome the opportunity to follow up directly.''',
    notes='''Reports | Attributes an account without declaring it proved or false.
Sorry to hear | Expresses concern without asserting an unverified cause.
Review the details | Names a process, not a guaranteed result.
Privately | Concerns the channel; still apply the approved access rules.
In exchange for | Signals a condition linking the benefit to the review.
Resolved | Use only when the relevant outcome and status support it.''',
    d='''Which public reply is most appropriate? | We are sorry to hear about the noise concern; please contact our published guest-relations channel so we can review it. | Your room number proves that you are exaggerating. | Delete the review and we will consider helping. | Our investigation proves you are wrong, although we have not checked. | The correct reply acknowledges the concern and offers a private next step without inventing findings.
Which internal note is suitably neutral? | The guest reports late-night noise; verification is pending. | The guest is dishonest. | The noise definitely never happened. | The complaint is resolved because we replied. | It distinguishes the reported experience from the pending factual review.
Which proposal should be rejected? | Offer a credit only if the guest removes the review. | Check the incident log. | Remove booking details from the public response. | Assign a private follow-up contact. | Linking a benefit to review removal improperly conditions service recovery on the review.
What does posting the public reply establish? | The concern has received an acknowledgement and a next step. | The investigation is complete. | A refund is approved. | The guest has accepted a settlement. | A public acknowledgement does not itself establish investigation, remedy, or acceptance.''',
    dialogue='''Elise | Could you check my response to the noise review before I publish it? I was frustrated by the guest's description.
Mateo | Let us start with the [[public reply::A public reply is visible beyond the original reviewer, so its wording must suit the wider audience.]]. It will be read by future guests as well. We need a calm acknowledgement and a useful next step, not an argument.
Elise | I included the room number and stay dates to show that we know the booking. I also said the guest exaggerated what happened that night.
Mateo | Remove the [[booking reference::The booking reference and other reservation details should not be exposed in the public response.]] and the other private details. Knowing the reservation does not justify publishing it. Have we actually checked the complaint against the relevant property records yet?
Elise | No, not yet. I used the original complaint and my colleague's impression of the conversation. That is not enough to establish whether the reported noise occurred.
Mateo | Then describe it as [[guest feedback::Guest feedback identifies the reported experience without pretending that its factual review is already complete.]] awaiting review. Do not call the account false, and do not claim that we have already proved a service failure. Neither conclusion is established.
Elise | Could the reply say that we are sorry to hear the stay was disappointing, then invite the guest to contact our published guest-relations channel?
Mateo | Yes. That provides an [[acknowledgement::An acknowledgement recognizes the concern and does not by itself confirm every allegation or approve a remedy.]] without announcing an investigation result. Keep it brief, and make the next step easy to find. We do not need to reconstruct the stay in public.
Elise | I will take that sentence out. Could you check the new wording after I remove the booking details as well?
Mateo | Exactly. That [[defensive tone::A defensive tone shifts attention from helping with the complaint to protecting the property from criticism.]] makes a factual conversation harder. We can explain relevant verified information later, but first we need a proper review and a clear person responsible.
Elise | I can handle the follow-up. Once the guest contacts us privately, I will confirm the necessary booking information through our approved process and review the available records.
Mateo | Consult the [[incident log::The incident log may contain relevant reports and actions; it is a source to check, not a presumed verdict.]] as part of that work. Record what it supports and what remains uncertain. An absent entry alone should not become a sweeping claim that nothing happened.
Elise | The handover suggests a credit, but only after the review comes down. We cannot use that condition, can we?
Mateo | Do not make that [[conditional offer::The proposed credit is improperly conditional on removing the review rather than on the service-review outcome.]]. Any approved remedy must stand independently of review removal or revision. Our task is to address the service concern, not purchase a different public account.
Elise | Understood. I will not promise compensation in the initial reply either. We still need to check the facts and determine what our policy permits.
Mateo | Correct. A [[service remedy::A service remedy is an authorized response to the service problem, not an outcome already decided by acknowledging the complaint.]] has not been decided. Explain that clearly in the private conversation if asked, and avoid language that suggests approval is automatic or impossible.
Elise | The public version now thanks the guest for raising the noise concern, acknowledges the disappointing experience, and directs them to the published contact route for follow-up.
Mateo | That is suitable. After publishing, create the [[case record::The case record should track responsibility, relevant facts, and actions so the private review does not lose continuity.]] and identify yourself as the contact. Preserve the distinction between the public acknowledgement and the unfinished private investigation.
Elise | I will check the records before reaching a conclusion, then communicate any authorized outcome directly. The guest will remain free to leave the review as it is.
Mateo | Good. Update the [[resolution status::Resolution status records where the complaint actually stands; posting a reply is not the same as resolving it.]] when the review progresses. For now, mark it as awaiting private follow-up, not resolved merely because we have answered online.''',
    transfer_title='Resolve the service issue, not the rating',
    transfer_setup='A guest posts a complaint about a delayed airport pickup. No investigation is complete. The draft reply includes a reservation code and offers a voucher only for deleting the review.',
    transfer='''Manager: "Remove the ___ from the public response." | reservation code | The reservation identifier is private booking information, not necessary public reply content.
Agent: "We can give a courteous ___ now." | acknowledgement | Recognition of the concern is appropriate before the factual review is complete.
Manager: "The complaint still needs a ___." | factual check | The brief states that no investigation has yet been completed.
Agent: "Any approved voucher must be independent of review ___." | deletion | A service remedy must not be conditional on removing the review.''',
    rehearsal=['Read turns 1-8, separating acknowledgment of the concern from a completed investigation.', 'Repeat turns 13-16; make the rejection of a review-removal condition explicit.', 'Switch roles for the transfer and read the corrected public/private boundary aloud.']))

BOOK['units'].append(unit(
    title='Reservations, Overbooking, and Walks',
    scene='The booked room type is unavailable',
    skill='Present verified alternatives, explain differences honestly, and obtain a guest decision before changing the booking.',
    brief='Mr Chen booked one king-bed room for tonight. That room type is unavailable. Duty manager Sofia has two verified alternatives: an on-site twin room with two separate beds at no additional charge, or a king-bed room at the nearby Harbor Hotel. For the off-site option, this property has approved payment of the room-price difference and a transfer; other expenses are not approved. Harbor Hotel has confirmed availability for tonight. Mr Chen has not selected an option. Sofia must explain the bed arrangements and location, check his preference, and complete the chosen arrangement before calling it confirmed.',
    cast='Sofia | Duty manager\nMr Chen | Guest with a king-room booking',
    culture=('A substitute is not automatically equivalent', 'Two available rooms may differ in the feature that matters most to a guest. Describe beds, location, and approved costs plainly. Internal shorthand such as walk should not replace a respectful explanation of the actual accommodation arrangement.'),
    a='''Which alternative preserves the booked bed arrangement? | The king room at Harbor Hotel | The on-site twin room | Either option has one king bed. | Neither option has a confirmed bed type. | Harbor Hotel has the verified king-bed alternative; the on-site room has two separate beds.
What costs are approved for the off-site option? | The room-price difference and transfer | Every expense during the stay | A future holiday | Only an unconfirmed taxi estimate | The brief limits the approved package to the room-price difference and transfer.
Has the guest accepted an alternative? | No; his choice is still required. | Yes; availability means acceptance. | Yes; the manager chose silently. | No; both alternatives are unavailable. | Both alternatives are available, but the guest has not selected one.''',
    vocabulary='''room type | A category of accommodation with specified features. | verify the room type
king room | A room containing a king-size bed. | confirm a king room
twin room | A room with two separate beds. | offer a twin room
bed configuration | The number and arrangement of beds. | explain the bed configuration
overbooking | Accepting more bookings than the available capacity can accommodate. | manage an overbooking
room-type mismatch | A difference between booked and offered accommodation categories. | resolve a room-type mismatch
walk | Industry shorthand for relocating a guest to another property. | arrange a guest walk
relocation | Moving a booking or guest to another property. | explain the relocation
alternative accommodation | A substitute place to stay. | verify alternative accommodation
receiving property | The property accepting a relocated guest. | contact the receiving property
on-site | Located at the same property. | offer an on-site alternative
off-site | Located away from the original property. | arrange an off-site room
availability check | Verification that a room or service can be supplied. | complete an availability check
rate difference | The difference between the two room prices. | cover the rate difference
transfer | Transport between locations. | arrange the approved transfer
incidental expense | An additional cost outside the basic room arrangement. | clarify incidental expenses
approved allowance | A specifically authorized amount or type of support. | state the approved allowance
guest consent | The guest's agreement to the proposed arrangement. | obtain guest consent
booking amendment | A documented change to an existing reservation. | confirm a booking amendment
confirmation number | An identifier for a confirmed booking. | verify the confirmation number
arrival instructions | Directions for reaching or entering the receiving property. | provide arrival instructions
handover contact | The person coordinating the receiving end of an arrangement. | identify the handover contact
service commitment | A specific promise made about the service provided. | document the service commitment
equivalent feature | A characteristic that genuinely matches the original requirement. | check equivalent features''',
    precision='A twin room does not preserve a king-bed configuration. A king room at another hotel preserves that feature but changes location. Neither alternative should be called identical to the original booking.',
    precision_extra='Availability, guest agreement, and completion of the replacement booking are separate stages. Approval to cover a price difference and transfer is not an unlimited promise to pay all incidental expenses.',
    phrases='''State the problem directly | Your booked king-room type is unavailable tonight.
Acknowledge responsibility | I am sorry we cannot provide the room type you reserved.
Introduce choices | I have two verified alternatives to explain.
Describe the on-site option | We have a twin room here with two separate beds.
Clarify the charge | There would be no additional room charge for that option.
Describe the off-site option | Harbor Hotel has confirmed a king room for tonight.
Name the difference | That keeps the bed type but changes the location.
Explain approved costs | We will cover the room-price difference and the transfer.
Bound the offer | Other expenses are not included in the approved arrangement.
Ask what matters | Is the king bed or staying at this property more important?
Avoid assuming agreement | I have not changed your booking without your choice.
Check the selection | Would you like me to arrange the Harbor Hotel option?
Complete the handover | I will confirm the booking and arrival details.
Keep timing accurate | I still need to confirm the transfer arrangements.
Use plain language | We can arrange accommodation at the nearby hotel.
Close with a readback | Let me repeat the room, location, and costs we have agreed.''',
    notes='''Available | Does not mean already booked in this guest's name.
Included | Specify exactly what the package includes.
Equivalent | Avoid when a material feature or location differs.
Walk | Internal jargon; explain relocation plainly to the guest.
Would you like | Requests a choice rather than assuming agreement.
Confirmed | Identify which part of the arrangement is confirmed.''',
    d='''Which description is most accurate? | The twin room is on-site but has two separate beds. | The twin room is identical to a king room. | The king room is on-site. | Both alternatives change only the price. | The correct description preserves the verified difference in bed configuration.
Which statement overpromises? | We will pay every expense you incur. | The approved offer covers the price difference and transfer. | Harbor Hotel has a king room available tonight. | I need your choice before completing the change. | The approval does not extend to every incidental or future expense.
What should happen before changing the booking? | Explain the alternatives and obtain the guest's choice. | Select the cheaper alternative without asking. | Mark both hotels as occupied by the guest. | Announce that every detail is complete. | The guest has not selected an alternative and needs accurate information before agreeing.
Which handover is complete in principle? | Verify the chosen booking, receiving contact, arrival details, and approved transfer. | Send the guest away with only a hotel name. | Treat room availability as a confirmed transfer. | Promise unspecified costs later. | A practical relocation requires coordination of the selected accommodation and its agreed supporting arrangements.''',
    dialogue='''Mr Chen | I reserved a king room; two separate beds do not suit us. The receptionist mentioned a problem. What is available?
Sofia | I am sorry. Your booked [[room type::Room type identifies the accommodation category that cannot be supplied tonight, rather than suggesting the entire reservation never existed.]] is unavailable tonight. I have two verified alternatives, and I want to explain the differences before you choose either one.
Mr Chen | Please start with the option here. We would prefer not to move unless staying means losing the bed arrangement that we specifically booked.
Sofia | The on-site option is a [[twin room::A twin room has two separate beds and therefore does not preserve the guest's booked king-bed arrangement.]] with two separate beds, at no additional charge. It keeps you at this property, but it does not match your king-bed preference.
Mr Chen | That difference matters to us. What is the second option, and have you actually checked that the other hotel can provide the right room tonight?
Sofia | The [[receiving property::The receiving property is Harbor Hotel, which has verified the relevant accommodation for tonight.]] is Harbor Hotel nearby. They have confirmed that a king room is available tonight. That preserves the bed type, although it changes where you will stay.
Mr Chen | Would I have to pay the difference? I do not want to arrive there and discover that this solution costs more than the booking I made.
Sofia | Our approved arrangement covers the [[rate difference::The rate difference is the additional room-price amount the original property has specifically approved paying.]] and the transfer to Harbor Hotel. Other expenses are not included. I will make that scope clear in the arrangements rather than leave you with an open-ended promise.
Mr Chen | The king room sounds better for us. Before you arrange it, please confirm we would not pay extra for the room or the transfer.
Sofia | Yes. I need your [[consent::Consent means the guest agrees to the specific alternative after hearing the differences and approved costs.]] before completing the change. I have not treated the availability check as your acceptance or amended the booking without asking you.
Mr Chen | Then we choose the king room at Harbor Hotel for tonight. Please confirm the actual reservation before we leave with the luggage.
Sofia | I will complete the [[booking amendment::The booking amendment records the guest's selected change; it is distinct from merely identifying an available alternative.]] and coordinate with Harbor Hotel. I will check the room, arrival details, and payment arrangements so the receiving team has the same information.
Mr Chen | A member of staff used the word walk earlier. Does that mean we are expected to walk there with our bags? That would be difficult.
Sofia | No. That is internal shorthand for [[relocation::Relocation means accommodation at another property; the approved transfer means the guest is not simply told to walk there.]]. In your case, the approved offer includes transport. I should have explained the arrangement in ordinary language instead of leaving that term unclear.
Mr Chen | Do you have a transport departure time yet? Should we stay by reception or wait somewhere else?
Sofia | I still need to confirm the [[transfer::The transfer is the transport arrangement, which requires its own confirmation even though the room option is available.]] details. Please remain by reception while I coordinate them. I will not describe a departure time as confirmed until the transport arrangement is verified.
Mr Chen | That is fine. Before we leave, please give us the receiving contact and explain what we should show when we arrive at Harbor Hotel.
Sofia | I will provide the [[arrival instructions::Arrival instructions make the receiving handover practical by explaining where to go and what booking information is needed.]] once the booking is completed. They will identify the receiving contact and booking details, with the agreed room-price and transfer arrangements clearly recorded.
Mr Chen | Could you put those details in writing? I do not want to explain the price and transport agreement again at Harbor Hotel.
Sofia | Certainly. First, a quick [[readback::A readback repeats the agreed details so both parties can correct any misunderstanding before the relocation is carried out.]]: a king room at Harbor Hotel tonight, price difference and transfer covered, other expenses excluded. I will complete the arrangements and confirm them in writing before you leave.''',
    transfer_title='A feature match still needs agreement',
    transfer_setup='A guest booked a king bed. The local room has two singles. A nearby hotel has a verified king room; the approved offer covers its price difference and transport only.',
    transfer='''Agent: "The local option has a different ___." | bed configuration | Two singles differ from the king bed originally booked.
Guest: "The nearby option preserves the ___." | king bed | The verified nearby room contains the requested king bed.
Agent: "Our offer includes the price difference and ___." | transport | These are the two costs explicitly approved in the scenario.
Guest: "Please confirm the details before changing my ___." | booking | A change should follow informed agreement and completed coordination.''',
    rehearsal=['Read turns 1-8, contrasting two separate beds with a king bed without calling them equivalent.', 'Repeat turns 13-20, explaining walk in ordinary language and reading back the included costs.', 'Switch roles for the transfer and emphasize the feature that each option preserves or changes.']))

BOOK['units'].append(unit(
    title='Revenue Management and Pricing',
    scene='A higher room rate did not produce higher room revenue',
    skill='Explain occupancy, average daily rate, and revenue per available room using the correct denominators.',
    brief='Revenue analyst Mina reviews two single-night results with general manager Owen. Each night had 100 available rooms. On Night A, 80 rooms sold and room revenue was $8,000. On Night B, 60 rooms sold and room revenue was $7,200. These figures exclude non-room revenue; no cost figures are supplied. Owen calls the higher average daily rate a complete commercial improvement. Mina needs to distinguish the higher rate among sold rooms from the lower occupancy and lower revenue per available room. The two observations alone do not establish why demand changed.',
    cast='Mina | Revenue analyst\nOwen | General manager',
    culture=('Challenge the measure, not the person', 'A manager may use a familiar headline as shorthand for success. Name the calculation and its boundary before disagreeing with the conclusion. A precise comparison lets the team discuss pricing without turning a useful challenge into a contest over confidence.'),
    a='''What is Night B's average daily rate? | $120 | $72 | $60 | $100 | Room revenue of $7,200 divided by sixty sold rooms equals $120.
What is Night B's revenue per available room? | $72 | $120 | $80 | $7,200 | The denominator is all one hundred available rooms, giving seventy-two dollars.
What cannot be calculated from the supplied figures? | Profit | Occupancy | Average daily rate | Room revenue per available room | Costs are not supplied, so room revenue measures do not establish profit.''',
    vocabulary='''average daily rate (ADR) | Room revenue divided by rooms sold for the period. | calculate average daily rate
occupancy rate | Rooms sold as a percentage of rooms available. | report the occupancy rate
revenue per available room (RevPAR) | Room revenue divided by available room supply. | compare revenue per available room
room revenue | Revenue from selling guest rooms. | distinguish room revenue
rooms sold | The count of paid room units sold in the stated period. | verify rooms sold
rooms available | Room supply available for the stated reporting period. | state rooms available
room night | One room for one night. | measure demand in room nights
non-room revenue | Revenue from services other than room sales. | separate non-room revenue
revenue management | Coordinating price and availability to manage revenue. | review revenue management
rate strategy | The approach used to set and vary selling prices. | evaluate the rate strategy
demand | Customer willingness and ability to purchase accommodation. | assess room demand
booking pace | The speed at which reservations accumulate for a date. | track booking pace
pickup | The change in booked business between reporting points. | report booking pickup
on-the-books | Reservations already recorded for a future period. | review on-the-books revenue
forecast occupancy | The estimated share of rooms expected to sell. | revise forecast occupancy
market segment | A defined customer or business category. | compare market segments
channel mix | The proportions sold through different booking routes. | examine the channel mix
distribution cost | The expense associated with selling through a channel. | include distribution costs
net room revenue | Room revenue after the specified deductions. | define net room revenue
gross operating profit | Operating revenue less the relevant operating expenses. | distinguish gross operating profit
competitive set | A selected group of properties used for comparison. | review the competitive set
rate premium | A price above a stated comparison rate. | explain the rate premium
price elasticity | The responsiveness of demand to price changes. | assess price elasticity
revenue trade-off | A gain in one revenue driver offset by another change. | explain a revenue trade-off''',
    precision='Night A: occupancy 80%, ADR $100, RevPAR $80. Night B: occupancy 60%, ADR $120, RevPAR $72. ADR increased 20%, but RevPAR and total room revenue each decreased 10%. Occupancy fell 20 percentage points.',
    precision_extra='ADR uses rooms sold; RevPAR uses rooms available. The identical supply makes the revenue comparison straightforward here. Neither room metric includes all hotel revenue or costs, and two nights do not isolate the cause of a demand change.',
    phrases='''Clarify the headline | Which measure do we mean by improved?
State the common base | Both nights had 100 available rooms.
Give the first result | Night A sold 80 rooms for $8,000.
Give the second result | Night B sold 60 rooms for $7,200.
Explain ADR | Divide room revenue by rooms sold.
Report the rate change | ADR rose from $100 to $120.
Explain occupancy | Sixty of one hundred rooms sold, or 60%.
Use points correctly | Occupancy fell by 20 percentage points.
Explain RevPAR | Divide room revenue by rooms available.
Report the capacity yield | RevPAR fell from $80 to $72.
State the revenue change | Room revenue decreased by $800, or 10%.
Avoid a profit claim | We do not have the costs needed to calculate profit.
Keep the scope clear | These figures concern rooms, not all hotel revenue.
Avoid causal overreach | This comparison does not isolate the effect of pricing.
Request useful context | Let us examine demand, segments, and channel mix.
Summarize the trade-off | A higher sold-room rate coincided with fewer rooms sold.''',
    notes='''Per sold room | Names the ADR denominator, not total room supply.
Per available room | Includes the whole defined supply in the denominator.
Rose by versus rose to | By gives the change; to gives the resulting value.
Percentage points | Use for subtracting the two occupancy percentages.
Revenue versus profit | Revenue alone does not account for the relevant costs.
Coincided with | Reports a relationship without declaring its cause.''',
    d='''Which summary is accurate? | ADR rose while occupancy, RevPAR, and room revenue fell. | Every room measure improved. | Higher ADR proves higher profit. | RevPAR excludes unsold available rooms. | The supplied calculations show higher sold-room rate but lower volume and capacity-based revenue.
Which calculation gives Night A's RevPAR? | $8,000 divided by 100 | $8,000 divided by 80 | 80 divided by 100 | 100 divided by 80 | RevPAR divides room revenue by available room supply, not sold rooms.
Which occupancy change is correctly stated? | A fall of 20 percentage points | A fall of 20% relative | A rise of 20 percentage points | No change because supply stayed constant | Eighty percent minus sixty percent is twenty points; the relative fall is twenty-five percent.
Which causal claim is justified by these two nights alone? | None; further evidence is needed to isolate a pricing effect. | The higher price caused every lost booking. | Demand changes never affect occupancy. | The lower occupancy proves the property was closed. | The comparison reports outcomes but does not control other influences on demand.''',
    dialogue='''Owen | Our average rate went up on the second night, so I have called it a complete commercial improvement. Is there anything missing from that summary?
Mina | The higher [[ADR::ADR measures average room revenue among sold rooms, so it can rise while overall room revenue falls.]] is real, but it is only one measure. We should look at how many rooms sold and what the available room supply earned as well.
Owen | Start with the room supply. I do not want to mistake a capacity change for performance.
Mina | Both nights had one hundred [[rooms available::Rooms available is the common supply denominator, which stayed at one hundred on both nights.]]. Night A sold eighty rooms for eight thousand dollars. Night B sold sixty rooms for seven thousand two hundred dollars. These are room-only revenue figures.
Owen | So the first average is one hundred dollars per sold room, and the second is one hundred and twenty. That is a twenty-percent increase.
Mina | Correct. Meanwhile, [[occupancy::Occupancy is rooms sold divided by available rooms, giving eighty percent on Night A and sixty percent on Night B.]] moved from eighty percent to sixty percent. That is a fall of twenty percentage points, or twenty-five percent relative to the original eighty-percent level.
Owen | I see the distinction. The higher rate applies to a smaller number of sold rooms. How should we describe the result across all available rooms?
Mina | Use [[RevPAR::RevPAR uses all available rooms as the denominator, producing eighty dollars on Night A and seventy-two on Night B.]]. Eight thousand divided by one hundred is eighty dollars. Seven thousand two hundred divided by one hundred is seventy-two dollars. The capacity-based room revenue measure fell.
Owen | That means an eight-dollar reduction per available room. Relative to eighty dollars, it is ten percent lower, despite the higher average selling rate.
Mina | Yes. Total [[room revenue::Room revenue fell from eight thousand to seven thousand two hundred dollars, the same ten-percent decline with unchanged supply.]] also fell ten percent, from eight thousand to seven thousand two hundred. The unchanged supply means those two percentage changes align in this comparison.
Owen | Could we still say that profit improved because we had fewer rooms to service? Fewer occupied rooms might mean some costs were lower.
Mina | That is possible, but we have no [[cost figures::Cost figures are needed before a revenue comparison can support a conclusion about profit.]] here. We cannot calculate profit or assume how expenses changed. A possible cost effect should remain a question, not become a reported financial result.
Owen | Fair point. What about restaurant and event spending? Those could change the property's total revenue even when the room figures move in the opposite direction.
Mina | They could, but [[non-room revenue::Non-room revenue is outside the supplied room-only figures, so no total-property revenue conclusion is established.]] is not included in this comparison. We should label the scope clearly instead of using the room result as a complete measure of hotel performance.
Owen | Can I say the price increase caused the occupancy fall, or do we need to look at the business mix first?
Mina | We need more evidence. We have not established [[price elasticity::Price elasticity concerns how demand responds to price; two uncontrolled nights do not establish that response.]] or controlled other influences on demand. Let us compare the dates, segments, and booking patterns before attributing the whole decline to price.
Owen | Then the next discussion should look at context rather than force a cause into the headline. Which breakdown would make that review more useful?
Mina | Examine market segments and [[channel mix::Channel mix identifies how sales are distributed across booking routes and can add context to revenue and distribution-cost analysis.]], alongside demand and booking pace. Keep the same period and definitions, and include relevant costs before making a profitability claim.
Owen | I will revise the summary to say that ADR increased while occupancy, RevPAR, and room revenue declined. That is less sweeping and more informative.
Mina | Exactly. It describes the observed [[trade-off::The trade-off is the higher average rate alongside fewer sold rooms, without asserting a proven cause or profit outcome.]] without treating one favorable metric as the whole result. We can then investigate why it happened and whether the strategy should change.''',
    transfer_title='Choose the right denominator',
    transfer_setup='A hotel has 50 available rooms for one night. It sells 40 rooms and receives $6,000 in room revenue. No costs or non-room revenue are supplied.',
    transfer='''Analyst: "Occupancy is ___ percent." | 80 | Forty sold rooms divided by fifty available rooms equals eighty percent.
Manager: "ADR is ___ dollars." | 150 | Six thousand dollars divided by forty sold rooms equals one hundred fifty.
Analyst: "RevPAR is ___ dollars." | 120 | Six thousand dollars divided by fifty available rooms equals one hundred twenty.
Manager: "We cannot calculate ___ from these figures alone." | profit | The case supplies revenue but no relevant cost figures.''',
    rehearsal=['Read turns 3-10, stating whether each calculation uses rooms sold or rooms available.', 'Repeat turns 11-16, separating revenue, profit, and a causal claim about pricing.', 'Switch roles for the transfer and read 80%, $150, and $120 with their units.']))

BOOK['units'].append(unit(
    title='Housekeeping, Maintenance, and Turnover',
    scene='Clean does not yet mean released',
    skill='Read back separate department statuses and keep a room unavailable until the required release is recorded.',
    brief='Room 417 is cleaned and inspected by housekeeping, but its door-lock repair is still open in the maintenance record. The fictional property requires both housekeeping clearance and maintenance clearance before the duty manager releases a room to reception. Neither maintenance clearance nor the final release is recorded for 417. Reception wants to assign it to an arriving guest. Room 419 has both clearances and a recorded release; its room type and the guest-required features have been checked and match. Reception can assign 419 without changing 417 to available or promising when its repair will finish.',
    cast='Leah | Reception supervisor\nMarco | Rooms-division coordinator',
    culture=('Department labels answer different questions', 'Clean, repaired, inspected, and available may belong to separate checks. A colleague who insists on reading each status is protecting the handover, not criticizing another team. State the missing authorization and the ready alternative without blaming an entire department.'),
    a='''What is missing for Room 417? | Maintenance clearance and final release | Housekeeping inspection | A room number | Evidence that the guest arrived | Housekeeping is complete, but the repair remains open and release is unrecorded.
Which room can reception assign on the supplied facts? | Room 419 | Room 417 | Either room because both are clean | Neither room because no room type was checked | Room 419 is released and its required features match the guest's needs.
Who performs the final release in this fictional process? | The duty manager | Any guest | The reservation website | Whoever sees a clean bed first | The brief explicitly assigns final release to the duty manager after both clearances.''',
    vocabulary='''room turnover | Preparing a room between guest stays. | coordinate room turnover
housekeeping clearance | Confirmation that the required housekeeping checks are complete. | record housekeeping clearance
maintenance clearance | Confirmation that the required maintenance conditions are satisfied. | obtain maintenance clearance
work order | A recorded request or instruction for maintenance work. | update a work order
open repair | A repair not yet recorded as completed and cleared. | track an open repair
door-lock fault | A reported problem with a door's locking system. | report a door-lock fault
inspection record | Documentation of a completed check and its result. | verify the inspection record
release authorization | Permission to make the room available for assignment. | verify release authorization
room status | The recorded operational condition of a room. | reconcile room status
property management system (PMS) | Software managing room, reservation, and guest operations. | update the PMS
out of order | A property-defined status taking a room out of use. | confirm an out-of-order status
out of service | A property-defined temporary unavailability status. | check the out-of-service code
vacant clean | A room-status label indicating an unoccupied, cleaned room. | distinguish vacant clean
vacant dirty | A room-status label indicating cleaning is still required. | report vacant dirty
occupied room | A room currently assigned for guest use. | identify an occupied room
room discrepancy | A conflict between room records or observations. | resolve a room discrepancy
engineering department | The hotel team responsible for technical maintenance. | contact the engineering department
defect report | A record describing a fault needing attention. | submit a defect report
readback | Repetition of details to check shared understanding. | request a status readback
handover log | A record used to transfer operational responsibility. | update the handover log
release hold | A restriction preventing a room from being assigned. | maintain the release hold
guest-required feature | A room characteristic needed for the particular booking. | verify guest-required features
return to service | Authorized restoration of availability after required checks. | confirm return to service
status reconciliation | Checking and resolving differences among recorded statuses. | complete status reconciliation''',
    precision='Housekeeping clearance confirms its own checks. It does not close a maintenance work order or supply the duty manager\'s release. For 417, keep all three statuses distinct rather than translating clean into available.',
    precision_extra='Codes such as out of order and out of service vary by property and reporting system. Confirm the local definition instead of assuming a universal meaning. In this case, the explicit release process governs assignment.',
    phrases='''Name the exact room | I am checking the release status for Room 417.
Separate department checks | Housekeeping is cleared, but maintenance is not.
Identify the open item | The door-lock repair remains open.
State the missing authority | The duty manager's final release is not recorded.
Keep the hold clear | Do not assign 417 yet.
Avoid a shortcut | Vacant clean is not the same as released under this process.
Ask for evidence | Please check the clearance and release records.
Avoid an invented deadline | I do not have a confirmed repair completion time.
Offer the ready alternative | Room 419 has both clearances and final release.
Confirm suitability | Its room type and required features match.
Read back the action | Assign 419 and keep 417 unavailable.
Keep records consistent | Update the handover log without changing the repair status.
Use neutral language | The maintenance clearance is still pending.
Name the next owner | The duty manager can release it after the required clearances.
Report the guest outcome | We can accommodate the guest in the released alternative.
Close the handover | Please confirm that reception has the same room status.''',
    notes='''Cleaned versus cleared | A physical task and a recorded authorization may be different stages.
Still open | Describes the record status without assigning blame.
Not yet | Marks a pending condition without promising when it will change.
Released | Must refer to the relevant authorized decision.
Matches | Confirm actual required features, not only a room-category label.
Keep unavailable | Maintains the hold rather than predicting a technical outcome.''',
    d='''Which handover is accurate? | Assign 419; keep 417 on hold until its required clearances and release are recorded. | Assign 417 because the bed is clean. | Close the repair to make the system look consistent. | Promise 417 will be ready in ten minutes. | The released and suitable alternative meets the guest need without bypassing 417's outstanding requirements.
What does the housekeeping inspection prove here? | The housekeeping checks are complete. | The lock repair is finished. | The duty manager has released the room. | The repair will finish before arrival. | A department-specific inspection does not establish another department's clearance or final authorization.
Which statement about room-status codes is safest? | Check the property's definitions and release rules. | Every property uses identical definitions. | Any green screen label overrides an open repair. | Out of service always means cleaned and assignable. | Local status definitions and the stated release process determine their operational meaning.
Which response avoids blaming a team? | Maintenance clearance is pending; I will check the responsible contact. | Engineering never finishes anything. | Housekeeping caused all delays. | Reception should ignore everyone else. | It states the actionable status and next step without an unsupported general accusation.''',
    dialogue='''Leah | Housekeeping says Room 417 is clean. The guest is waiting, so can I assign it now? The desk needs a clear answer before issuing keys.
Marco | Keep the [[release hold::The release hold prevents assignment while the required maintenance clearance and final authorization remain outstanding.]] in place. Housekeeping has completed its inspection, but the door-lock repair remains open. We need the remaining clearance and the duty manager's release.
Leah | The room screen shows vacant clean. I assumed that meant it was available, since the cleaning team had already finished its part.
Marco | That label describes [[housekeeping clearance::Housekeeping clearance covers housekeeping's checks and cannot stand in for maintenance clearance or the final room release.]] here, not every release condition. We must check the separate maintenance and authorization records rather than infer that all teams have completed their work.
Leah | I see an open work order for the lock. Could it simply be an old entry that someone forgot to close after finishing the repair?
Marco | It could need checking, but the [[work order::The work order is the maintenance record requiring verification; its possible staleness is not proof the repair is complete.]] is still open. We cannot turn that possibility into a completed repair. Ask the responsible team for the recorded status.
Leah | The guest is still at the desk. Is 419 released, and does it match the booking? I would rather offer a confirmed alternative now.
Marco | Room 419 has [[maintenance clearance::Maintenance clearance is already recorded for 419, alongside its housekeeping clearance and final release.]], housekeeping clearance, and final release. Its room type and the guest-required features have been checked and match. It is the confirmed alternative available now.
Leah | Good. I will assign 419. I will not change 417 to available simply because we have solved this guest's immediate accommodation problem.
Marco | Exactly. The [[room assignment::The room assignment concerns 419 only; providing that alternative does not change the unresolved status of 417.]] and the unresolved repair are separate matters. The guest can be accommodated while 417 remains unavailable under the current release process.
Leah | What should I say if the guest asks why the originally considered room is not ready? I do not want to share a speculative technical diagnosis.
Marco | Say that it is awaiting the required [[release authorization::Release authorization is the missing operational permission, which can be described without guessing at the technical fault or repair time.]]. Then explain that we have a released room matching the booking. Do not invent a repair deadline or blame a department.
Leah | I will put both statuses in the handover. The next shift needs to see why 417 says clean on one screen but unavailable on the other.
Marco | That calls for [[status reconciliation::Status reconciliation checks what each label means and resolves the records without automatically treating different department statuses as contradictions.]]. The labels may describe different checks rather than contradictory facts. Confirm their definitions and ensure reception sees whether final release has actually occurred.
Leah | For the handover, I will record 419 as the assigned room and 417 as unavailable, with its lock work order still open pending verification.
Marco | Include that in the [[handover log::The handover log transfers the actual room assignment, unresolved item, and responsibility to the next shift.]], together with the contact responsible for checking the maintenance status. Avoid marking the repair complete merely to make two screens display the same word.
Leah | Once the repair is cleared, does reception release 417 directly, or does the duty manager still need to record the final decision?
Marco | The duty manager records [[return to service::Return to service requires the stated final release after both department clearances; reception does not bypass that step.]] after both clearances. That is the process in this property. A maintenance update alone does not remove the final authorization requirement.
Leah | Let me repeat the action: assign 419, keep 417 unavailable, check the maintenance record, and wait for the duty manager's release before assigning 417.
Marco | That [[readback::The readback confirms the room numbers, hold, and release sequence so the two departments act on the same information.]] is correct. Please confirm the same status with the next shift. We have a practical guest solution and a separate outstanding room issue.''',
    transfer_title='A completed task is not a complete release',
    transfer_setup='Room 208 has housekeeping clearance but no maintenance clearance or manager release. Room 210 is fully released and matches the booking. The local process requires both clearances and manager release.',
    transfer='''Reception: "The released alternative is Room ___." | 210 | The brief identifies 210 as released and suitable for the booking.
Coordinator: "Room 208 still lacks ___ clearance." | maintenance | Only housekeeping clearance has been recorded for Room 208.
Reception: "It also needs the manager's final ___." | release | The local process requires a separate final manager authorization.
Coordinator: "Keep 208 ___ until those requirements are met." | unavailable | Assignment must wait for the outstanding clearance and release.''',
    rehearsal=['Read turns 1-8 with the room numbers clearly separated: four-one-seven and four-one-nine.', 'Repeat turns 15-20, distinguishing maintenance clearance from the final release.', 'Switch roles for the transfer, preserving Room 208 on hold and Room 210 as the released alternative.']))

BOOK['units'].append(unit(
    title='Events, Banquets, and Run of Show',
    scene='The soundcheck everyone assumed someone else had booked',
    skill='Turn an assumed event arrangement into a timed, owned, and acknowledged schedule entry.',
    brief='Venue coordinator Ren and event planner Asha compare their schedules. The soundcheck has no confirmed time, room, or owner; each team assumed the other arranged it. They now have a verified slot in Room A from 10:30 to 11:00. Audio lead Vera has accepted responsibility, the required equipment is available, and audience doors open at 11:15. Vera will check the event microphone and playback feed during the slot. Ren will update the controlled run of show and send it to the affected teams; Asha will confirm their acknowledgement. Later changes require coordinated review rather than a silent edit.',
    cast='Ren | Venue coordinator\nAsha | Event planner',
    culture=('Shared awareness is not shared responsibility', 'An event team may all know that a soundcheck is needed while nobody has actually arranged it. Name the owner, location, start, finish, and affected handovers. Asking for a readback can be a practical coordination habit rather than a sign of distrust.'),
    a='''What was missing from the earlier soundcheck arrangement? | Confirmed time, room, and owner | The event's entire audience | Every piece of equipment in the building | Proof that the event had ended | Both teams assumed the other had arranged the task, leaving these details unconfirmed.
How long is the confirmed soundcheck slot? | Thirty minutes | Fifteen minutes | Forty-five minutes | One hour | The slot runs from 10:30 until 11:00, a thirty-minute duration.
What buffer remains before doors open? | Fifteen minutes | Thirty minutes | No time | Forty-five minutes | Soundcheck finishes at 11:00 and doors open at 11:15.''',
    vocabulary='''run of show | The timed sequence of event activities and responsibilities. | update the run of show
soundcheck | A scheduled test of the event's audio setup. | coordinate the soundcheck
audio lead | The person responsible for the audio work. | confirm the audio lead
playback feed | The audio signal from recorded material into the system. | test the playback feed
microphone check | Verification of the required microphone's operation. | complete a microphone check
doors open | The time attendees may enter the event space. | confirm doors-open time
cue | A signal to begin a particular event action. | call the cue
cue sheet | A list of event signals and related actions. | verify the cue sheet
stage manager | The person coordinating actions around the stage. | brief the stage manager
technical rehearsal | A practice session checking technical event elements. | schedule a technical rehearsal
room booking | A confirmed allocation of a space for a time. | verify the room booking
setup window | Time allocated to preparing the event space. | protect the setup window
strike | Removal of event equipment after use. | schedule the strike
load-in | Bringing equipment into the event location. | coordinate the load-in
load-out | Taking equipment out after the event. | confirm the load-out
banquet event order (BEO) | A detailed document specifying an event's service requirements. | reconcile the banquet event order
function sheet | A property document listing an event's operational requirements. | check the function sheet
headcount | The number of people expected or present. | confirm the headcount
room layout | The arrangement of seating, tables, and equipment. | approve the room layout
buffer time | Time reserved between activities for transition or delay. | preserve buffer time
task owner | The person accountable for completing a specified activity. | name the task owner
schedule version | An identified edition of the event timetable. | circulate the schedule version
acknowledgement | Confirmation that a message or instruction has been received. | obtain team acknowledgement
change control | The process for reviewing and communicating alterations. | follow event change control''',
    precision='The soundcheck is 10:30-11:00 in Room A, owned by Vera. Doors open at 11:15, leaving a 15-minute buffer. Moving the soundcheck finish to 11:15 would consume that buffer even if the start remained unchanged.',
    precision_extra='Sending the updated run of show does not establish that every affected team has received and understood it. Record the version, secure acknowledgement, and coordinate changes that affect the audio lead, room, or doors-open handover.',
    phrases='''Expose the assumption | We both assumed the other team had arranged it.
Name the missing details | The schedule lacks a time, room, and owner.
Confirm the slot | Room A is available from 10:30 to 11:00.
Name the owner | Vera has accepted responsibility for the soundcheck.
Specify the scope | She will check the event microphone and playback feed.
Confirm readiness | The required equipment is available.
Protect the next event | Doors open at 11:15.
State the buffer | That leaves fifteen minutes between soundcheck and admission.
Update the shared record | I will revise the controlled run of show.
Identify the current version | Please use the updated schedule version.
Request acknowledgement | Confirm that the affected teams have received the change.
Avoid a silent edit | Any later change needs coordinated review.
Read back the details | Room A, 10:30 to 11:00, with Vera responsible.
Distinguish duration | The soundcheck lasts thirty minutes.
Clarify distribution | Ren will send the schedule; Asha will collect acknowledgements.
Close the gap | The task now has a confirmed time, place, and owner.''',
    notes='''Booked versus assumed | A shared expectation is not a verified arrangement.
From ... to | States the complete time interval, not only its start.
Doors open | Means attendee admission, not the soundcheck start.
Owner | Name a person with accepted responsibility, not merely a department.
Sent versus acknowledged | Delivery action does not establish receipt or understanding.
Buffer | A planned gap; do not silently allocate it to another activity.''',
    d='''Which schedule entry is complete? | Soundcheck: Room A, 10:30-11:00, Vera, microphone and playback feed. | Soundcheck: Room A, 10:30-11:00, technical team, scope to follow. | Soundcheck: Room A, 10:30, Vera, microphone and playback; finish not listed. | Soundcheck: 10:30-11:00, Vera, microphone and playback; room awaiting confirmation. | Only the complete entry preserves all confirmed details: location, interval, named owner, and test scope.
What happens if soundcheck ends at 11:15 with doors unchanged? | The fifteen-minute buffer disappears. | The buffer grows to thirty minutes. | Doors automatically move to noon. | The original schedule remains unaffected. | The revised finish coincides with admission, leaving no transition buffer.
Which statement correctly separates responsibilities? | Ren updates and sends; Asha confirms affected-team acknowledgement. | Nobody owns communication after the edit. | Asha silently edits Vera's task. | Vera alone must guess every team's needs. | The brief assigns preparation and distribution to Ren and acknowledgement follow-up to Asha.
What is the best response to a later timing change? | Review its effects with the relevant teams and issue an acknowledged update. | Change one private copy only. | Assume the buffer will absorb any delay. | Treat an unread email as acceptance. | Changes can affect dependencies and must reach the teams expected to act on them.''',
    dialogue='''Asha | My team expected the venue to arrange the soundcheck. Your schedule just says audio before doors. Do we have a confirmed room and time anywhere?
Ren | No. That [[assumption::The assumption is the unverified belief that another team had arranged the soundcheck; it left essential details unconfirmed.]] was shared without a named owner. We need to replace it with a definite entry, not ask both teams to keep expecting the other to act.
Asha | Agreed. I have checked Room A, and the available slot is ten thirty until eleven. Does that fit the equipment and audio lead?
Ren | Yes. Vera has accepted the [[soundcheck::The soundcheck is the scheduled audio test Vera will conduct in the verified room and time slot.]] responsibility, and the equipment is available. She will test the event microphone and playback feed during that slot.
Asha | Please replace technical team with Vera on the schedule. I want the presenter to know exactly who is meeting them in Room A.
Ren | Vera will be listed as the [[task owner::The task owner is the named person who has accepted responsibility, avoiding an ambiguous department-level assignment.]]. I will also include Room A and both times. A start time alone would not show when the space must be ready for the next activity.
Asha | The audience comes in at eleven fifteen. Finishing at eleven gives us fifteen minutes between the audio work and admission, provided nobody silently extends the test.
Ren | Correct. That is our [[buffer time::Buffer time is the fifteen-minute interval between the eleven o'clock soundcheck finish and eleven-fifteen audience admission.]]. It is not an unallocated extra rehearsal slot. Any change that consumes it needs a review of the handover before doors open.
Asha | A presenter asked whether playback was included. They were worried that the microphone might be checked while the recorded material was left until the session itself.
Ren | The [[playback feed::The playback feed is explicitly included alongside the event microphone in Vera's soundcheck scope.]] is part of Vera's confirmed scope. I will put both items in the entry so the presenter and audio team can see the same expectation.
Asha | Which document should people use? There is an old planning email, my event schedule, and a venue copy with the vague audio note.
Ren | I will update the controlled [[run of show::The run of show is the shared timed event record that should carry the current soundcheck details.]] and send the identified version to the affected teams. The earlier notes should not remain competing sources for the soundcheck arrangement.
Asha | I will ask the affected teams to confirm receipt. Sending the revised version is necessary, but we need to know they have actually seen the change.
Ren | Thank you. Their [[acknowledgement::Acknowledgement confirms that the update reached the relevant teams; sending it alone does not establish that shared awareness.]] closes the communication step. If someone raises a conflict, we should resolve it explicitly rather than interpret silence as acceptance of every detail.
Asha | If Vera later needs more time, should she simply edit the finish in the shared document, or contact us before changing the schedule?
Ren | Follow [[change control::Change control requires reviewing and communicating the effect of a later adjustment rather than silently changing a dependent schedule.]]. A later finish could affect the room handover and audience admission. We need coordinated review and a communicated update before treating a new time as agreed.
Asha | I will flag eleven fifteen to the admission team. They have an older copy with eleven on it, so we need that copy replaced.
Ren | Exactly. [[Doors open::Doors open identifies the audience-admission time, which is eleven fifteen rather than the eleven o'clock technical finish.]] remains eleven fifteen. Keep that separate from setup and testing times, even though all three activities occur in the same room sequence.
Asha | To confirm: Room A, ten thirty to eleven, Vera responsible, microphone and playback checked, then a fifteen-minute buffer before audience admission.
Ren | That [[readback::The readback verifies the agreed location, duration, owner, scope, and dependent admission time before circulation.]] captures it. I will send the revised run of show, and you will collect team acknowledgements. We now have an arrangement instead of a shared assumption.''',
    transfer_title='Protect the handover interval',
    transfer_setup='An event test runs from 09:20 to 09:50 in Hall B. Audio lead Jo owns it. Doors open at 10:00. The coordinator must circulate the updated schedule and receive acknowledgement.',
    transfer='''Planner: "The test lasts ___ minutes." | 30 | The interval from 09:20 to 09:50 is thirty minutes.
Coordinator: "The buffer before doors is ___ minutes." | 10 | Ten minutes separate the 09:50 finish from 10:00 admission.
Planner: "The named task owner is ___." | Jo | The brief explicitly assigns responsibility to audio lead Jo.
Coordinator: "After circulation, collect team ___." | acknowledgement | Sending the schedule alone does not confirm the affected teams received it.''',
    rehearsal=['Read turns 3-8, stressing the start, finish, and separate doors-open time.', 'Repeat turns 11-18, distinguishing the current schedule from superseded copies.', 'Switch roles for the transfer, reading the thirty-minute test and ten-minute buffer as separate intervals.']))

BOOK['units'].append(unit(
    title='Tour Operations and Traveler Safety',
    scene='A weather update is not permission to depart',
    skill='Communicate an active tour hold, identify decision authority, and give an update without promising departure.',
    brief='At 09:10, thunderstorms have triggered the tour operator\'s local departure hold for a coastal excursion. Guests are already inside the hotel\'s designated indoor waiting lounge, away from windows. Tour-desk agent Camila must keep the group there under the current plan; she cannot clear departure. The operator has not confirmed a route, restart, or cancellation. Operations lead Ben is responsible for the operational decision and will send a status update at 09:30. No refund or alternative excursion has been approved. Camila can promise to relay that update, including an unchanged hold, but cannot promise that the group will leave at 09:30.',
    cast='Camila | Tour-desk agent\nMr Ellis | Excursion guest',
    culture=('Reassurance must not weaken the instruction', 'Guests under time pressure may hear an update time as a departure time. State the current hold first, identify the decision-maker, and repeat what guests should do now. A friendly tone should not turn an active safety instruction into an optional suggestion.'),
    a='''What is the current operational status? | Departure is on hold under the operator's plan. | Departure is confirmed for 09:30. | The tour has been canceled. | The coastal route has been cleared. | The operator's hold is active; no restart, route, or cancellation is confirmed.
What should the group do now in this case? | Remain in the designated indoor lounge under the current plan. | Wait outside beside the coach. | Decide by a guest vote to depart. | Treat clearer-looking sky as authorization. | The supplied local plan keeps the group in its designated indoor waiting location.
Who makes the operational decision? | Operations lead Ben | Any guest who has traveled before | Camila acting independently | The person posting the earliest online comment | The brief assigns the decision to Ben and does not give Camila departure-clearance authority.''',
    vocabulary='''excursion | A planned short trip or organized visitor activity. | coordinate a coastal excursion
tour operator | The organization responsible for providing the tour. | contact the tour operator
departure hold | A temporary restriction preventing the tour from leaving. | maintain the departure hold
operational clearance | Authorized permission to proceed under the relevant process. | await operational clearance
operations lead | The person responsible for the operational decision. | consult the operations lead
weather advisory | Information warning of relevant weather conditions. | monitor weather advisories
thunderstorm | A storm involving thunder and lightning. | respond to a thunderstorm
lightning safety plan | A documented procedure for managing lightning-related activity risk. | follow the lightning safety plan
designated shelter | A specifically identified protective location in the local plan. | use the designated shelter
indoor waiting area | An internal location assigned for guests awaiting instructions. | identify the indoor waiting area
route assessment | A review of the conditions affecting a proposed route. | await the route assessment
itinerary | The planned sequence of trip activities and locations. | revise the itinerary
departure clearance | Approval for the group or vehicle to leave. | distinguish departure clearance
restart decision | A determination that a suspended activity may resume. | communicate the restart decision
cancellation notice | A message confirming that a planned service will not operate. | issue a cancellation notice
contingency arrangement | A prepared alternative if the original plan cannot proceed. | verify contingency arrangements
rebooking | Moving a reservation to another service or time. | check rebooking options
refund eligibility | Whether the applicable conditions permit money to be returned. | verify refund eligibility
passenger manifest | A controlled list of people on the tour or transport. | check the passenger manifest
group accountability | Knowing where the members of a group are. | maintain group accountability
meeting point | The specified place where a group is to assemble. | confirm the meeting point
communication chain | The route by which authorized information reaches others. | follow the communication chain
all-clear | An authorized statement that a specified restriction can end. | avoid an assumed all-clear
travel disruption | An interruption to planned transport or activities. | explain the travel disruption''',
    precision='09:30 is the operator\'s status-update time. It is not a confirmed departure, restart, route, or cancellation time. Camila relays the authorized status; she does not replace the operations lead\'s decision with her own forecast.',
    precision_extra='The active local instruction is to remain in the designated indoor lounge. Do not substitute personal experience, guest pressure, or a brief change in appearance for the operator\'s safety process. Financial options require separate confirmation.',
    phrases='''State the hold first | Departure is currently on hold.
Explain the present action | Please remain in the designated indoor lounge.
Name the responsible authority | Our operations lead is reviewing the conditions.
Avoid a route promise | No route has been confirmed.
Give the communication time | The operator will send an update at 09:30.
Separate the meanings | That is an update time, not a departure time.
Keep the instruction active | The hold remains in place until authorized instructions change.
Reject an informal all-clear | I cannot clear departure based on how the sky looks.
Acknowledge the inconvenience | I understand this affects your plans for the day.
Avoid guessing | I do not have a verified restart time.
Keep cancellation distinct | Cancellation has not been confirmed.
Keep money decisions distinct | No refund decision has been approved yet.
Own the communication | I will relay the operator's update to the group.
Preserve an unchanged status | I will update you even if the hold remains.
Clarify a conditional option | Any alternative excursion would need confirmation.
Close with the current instruction | For now, please stay in this designated indoor area.''',
    notes='''On hold | A temporary operational status, not automatically a cancellation.
At 09:30 | Attach the time to update so it is not heard as departure.
Until | States the condition ending an instruction, not an estimated duration.
Not confirmed | Neither approved nor necessarily ruled out.
All-clear | Must come from the authorized process, not casual observation.
Will relay | Commits to communication rather than a favorable operational result.''',
    d='''Which announcement is accurate? | Departure remains on hold; the next operator update is at 09:30. | We will definitely depart at 09:30. | The weather looks better, so everyone should board now. | Every ticket has already been refunded. | The announcement preserves the active hold and correctly labels the scheduled communication.
What should Camila do if guests demand an immediate departure? | Repeat the active instruction and refer the decision through the operator's process. | Let a majority vote override the hold. | Invent clearance to reduce frustration. | Send the group outside while waiting for permission. | Guest pressure does not give the agent authority to override the active operational hold.
Which statement about cancellation is supported? | It has not been confirmed. | It is certain because a hold exists. | It is impossible because tickets were sold. | It was approved at 09:10. | The brief distinguishes the current hold from an undecided cancellation.
Which financial statement fits the facts? | Refund eligibility and any remedy still require confirmation. | Every guest is guaranteed an immediate refund. | No guest can ever receive a refund. | A status update automatically approves compensation. | No refund decision or alternative arrangement has been approved in the case.''',
    dialogue='''Mr Ellis | Somebody mentioned nine thirty. Is that our new departure time? Should we get our bags ready outside?
Camila | No. The [[departure hold::The departure hold is the active restriction on leaving, so guests should not interpret the update time as permission to board.]] remains in place. Please stay in this designated indoor lounge, away from the windows, under the operator's current plan. Nine thirty is the next update.
Mr Ellis | Thank you for making that clear. I am worried about losing the whole day, especially because we booked another activity later this afternoon.
Camila | I understand the [[travel disruption::Travel disruption describes the effect on the guest's plans without implying that a restart or remedy is already confirmed.]]. I will give you verified information as it arrives. At present, no route or restart time has been confirmed, so I cannot promise when the excursion will begin.
Mr Ellis | The sky looks brighter. Could the driver take us out now and avoid the worst part of the coast?
Camila | We need [[operational clearance::Operational clearance must come through the authorized operator process; a change in appearance or an improvised route does not provide it.]], not a judgment based on a brighter patch of sky. Our operations lead, Ben, is responsible for the decision. I cannot clear departure myself.
Mr Ellis | Has the operator canceled it, or are they still deciding? My family heard both versions in the lobby.
Camila | Correct. The [[route assessment::The route assessment concerns whether and how the excursion can operate; no route outcome has yet been confirmed.]] has not produced a confirmed route for us. Cancellation is also unconfirmed. The current status is a hold, with the group remaining in the designated indoor area.
Mr Ellis | Will we hear from you at nine thirty even without a decision, or should we keep asking at the desk?
Camila | I will relay the [[status update::The status update must be passed on even if it only confirms that the existing hold continues.]] to the group even if the hold is unchanged. You should not have to interpret silence or assume that no message means permission to leave.
Mr Ellis | I appreciate that. Would a cancellation mean that we automatically receive our money back, or move to another excursion today?
Camila | I need to verify [[refund eligibility::Refund eligibility depends on the applicable conditions and decision; the case does not establish an approved refund.]] and any available alternatives before promising either outcome. No refund or replacement excursion has been approved. Those arrangements are separate from the immediate departure decision.
Mr Ellis | Please check with us before moving the booking. An afternoon replacement might clash with our other activity, even if it sounds similar.
Camila | Of course. Any [[rebooking::Rebooking changes the reservation and would require a confirmed option and the guest's agreement, not an automatic assumption.]] would need a confirmed option and your agreement. I will explain the actual itinerary and relevant terms if an alternative becomes available, rather than treating it as already arranged.
Mr Ellis | Where should our group wait so that we do not miss the announcement?
Camila | Stay together in this [[indoor waiting area::The designated indoor waiting area is the location specified by the current local plan, keeping guests available for the authorized update.]]. If someone needs assistance, please tell the desk. We will use the operator's communication process and keep the current instruction clear until it changes.
Mr Ellis | I will tell the others that nine thirty means news, not departure. I will also explain that neither cancellation nor a refund has been decided.
Camila | That is accurate. There is no [[all-clear::An all-clear would require authorized instructions ending the restriction; none has been issued merely because an update is scheduled.]] at present. I know waiting is inconvenient, but I should not soften that message into a suggestion that the group may choose to depart.
Mr Ellis | Understood. We will remain here and wait for the operator's message. Please include us even if the next announcement only says the hold continues.
Camila | I will. The [[communication chain::The communication chain carries the operations lead's authorized status through the tour desk to the guests without inventing an intermediate decision.]] is Ben to the desk and then to the group. I will make the current status and next instruction explicit when I relay the update.''',
    transfer_title='Do not turn a message time into a journey time',
    transfer_setup='A local tour hold remains active. The group is in the designated indoor lounge. The operator promises an 11:00 update but has not cleared a route, departure, cancellation, or refund.',
    transfer='''Guest: "Does eleven mean ___?" | departure | The guest is asking about leaving, which has not been authorized.
Agent: "No; eleven is the next ___." | update | The scheduled time refers only to the operator's communication.
Guest: "We should remain in the designated indoor ___." | lounge | The current local plan keeps the group in that location.
Agent: "Correct; the operational ___ remains active." | hold | No authorized decision has ended the restriction on departure.''',
    rehearsal=['Read turns 1-6, putting the current waiting instruction before the explanation.', 'Repeat turns 9-14, making update, departure, cancellation, and rebooking distinct.', 'Switch roles for the transfer and read the unchanged hold without suggesting permission to board.']))

BOOK['units'].append(unit(
    title='Cultural Expectations and Service Style',
    scene='A timing preference is not a nationality-based rule',
    skill='Clarify an individual service preference, limit its scope, and distinguish a request from a confirmed arrangement.',
    brief='Ms Rahman declines morning housekeeping on the first day of a three-night stay. A colleague assumes guests from her country never want housekeeping and proposes canceling routine service for the whole stay. Guest-relations agent Nico checks directly. Ms Rahman wants no routine room entry before 14:00 today and would like service after 14:00 if available. The afternoon team has not yet confirmed a slot. Her preference for later days has not been stated. Nico can record today\'s request and seek confirmation, but cannot promise the time or infer future preferences. Emergency access follows the property\'s separate rules.',
    cast='Nico | Guest-relations agent\nMs Rahman | Staying guest',
    culture=('Ask without making the guest defend a group', 'People differ within every nationality and language community. A neutral question about today\'s service is more useful than an explanation of what people from a country supposedly prefer. Confirm the individual choice, its time period, and whether the requested service is actually available.'),
    a='''What does Ms Rahman want before 14:00 today? | No routine room entry | No service for the entire stay | An immediate room inspection | Automatic cancellation of the booking | Her stated preference concerns routine entry before a specific time today.
What is the status of afternoon service? | Requested but not yet confirmed | Guaranteed at 14:00 | Completed | Refused for every day | The afternoon team has not confirmed a slot, so the request remains pending.
What is known about later days? | No preference has been stated. | Service is permanently declined. | The same time is guaranteed. | Nationality supplies the missing preference. | The brief explicitly limits the stated preference to today, not the entire stay.''',
    vocabulary='''service preference | An individual's stated choice about how service is provided. | clarify a service preference
routine room entry | Entry for ordinary scheduled room service tasks. | limit routine room entry
do-not-disturb request | A request to avoid routine interruption. | record a do-not-disturb request
stayover service | Housekeeping provided while a guest continues a stay. | coordinate stayover service
service window | A period during which a service may be provided. | confirm the service window
afternoon slot | An available time allocation later in the day. | verify an afternoon slot
service frequency | How often a service is provided. | clarify service frequency
opt out | Choose not to receive a specified optional service. | opt out for today
opt in | Choose to receive a specified optional service. | opt in to service
preference note | A record of an explicitly stated service choice. | update the preference note
scope of request | The limits of what a person has asked for. | confirm the scope of request
duration of stay | The total period of the guest's visit. | distinguish the duration of stay
assumed preference | A choice attributed to someone without confirmation. | question an assumed preference
stereotype | A generalized belief applied to an individual because of group membership. | avoid a cultural stereotype
individual variation | Differences among people within the same group. | recognize individual variation
clarifying question | A question resolving a specific ambiguity. | ask a clarifying question
neutral wording | Language that avoids unsupported judgments or assumptions. | use neutral wording
form of address | The name or title used when speaking to someone. | ask the preferred form of address
language preference | The language a person chooses for communication. | check language preference
communication style | A person's preferred manner of interaction. | adapt communication style
personal space | The distance or privacy a person prefers in an interaction. | respect personal space
interruption | An action that breaks someone's current activity or privacy. | avoid an unnecessary interruption
service confirmation | Verification that the requested service has been arranged. | await service confirmation
emergency access | Entry governed by separate urgent-situation procedures. | distinguish emergency access''',
    precision='No routine entry before 14:00 today is narrower than no housekeeping for three nights. A request for service after 14:00 does not establish a start at exactly 14:00, nor guarantee that an afternoon slot exists.',
    precision_extra='Record what the guest actually says, with the relevant day and service scope. Do not add nationality-based explanations or silently extend the preference to future days. Routine privacy requests do not redefine the property\'s separate emergency-access rules.',
    phrases='''Ask about the service | Would you prefer service later today or no service today?
Confirm the time boundary | You would like no routine entry before 14:00 today.
Clarify the requested option | You would like housekeeping after 14:00 if available.
Keep availability honest | I still need to check an afternoon slot.
Avoid an exact-time promise | After 14:00 does not mean a confirmed start at 14:00.
Limit the period | I will record that for today only.
Avoid a group assumption | I will check your preference directly.
Use the guest's words | The note should describe the service and timing you requested.
Check a future preference | We have not yet discussed the later days.
Separate request and confirmation | The request is recorded; the service time is not confirmed.
Offer a clear next step | I will contact the afternoon team and confirm the available option.
Respect the interaction | I do not need a personal explanation for that preference.
Correct the earlier inference | Declining this morning did not mean declining the whole stay.
Keep the record neutral | No routine entry before 14:00 today; later service requested.
Bound the policy | Emergency access follows the property's separate rules.
Close with a readback | Let me repeat the request so I record it accurately.''',
    notes='''Today | Prevents a one-day preference from becoming a whole-stay rule.
After versus at | After sets a lower time boundary; at names a particular time.
If available | Keeps the requested option conditional until checked.
Decline | Specify exactly which service or timing was declined.
Would you prefer | Gives a neutral choice without demanding a cultural explanation.
Recorded versus arranged | A saved preference is not proof that staffing is confirmed.''',
    d='''Which note is accurate? | No routine entry before 14:00 today; later service requested, slot pending. | No housekeeping for this nationality. | Cancel all service for three nights. | Service guaranteed at exactly 14:00. | The correct note preserves the guest's stated scope and the unconfirmed afternoon availability.
Which question avoids stereotyping? | Would you prefer service later today or no service today? | Do people from your country dislike housekeeping? | Your nationality means you never need service, correct? | Why are all your compatriots so private? | The neutral question asks about the individual's service choice rather than a presumed group trait.
What needs confirmation before promising afternoon service? | An available slot from the afternoon team | The guest's nationality | The employee's general impression | A guess based on the empty corridor | The requested time depends on staffing availability that has not yet been checked.
Which statement about future days is supported? | Their service preference remains unstated. | Today automatically controls every later day. | Three nights means exactly three afternoon services are booked. | An individual preference cannot ever change. | The guest has only specified today's preference, so later days cannot be inferred.''',
    dialogue='''Nico | Ms Rahman, may I check your housekeeping request? Would you like service later today, or would you prefer to skip it today?
Ms Rahman | Later, please. I would like some [[privacy::Privacy concerns the guest's request not to be interrupted before two today, not a whole-stay cancellation.]] this morning. Please do not send anyone in before two, but I would still like the room serviced afterward if possible.
Nico | Certainly. I will ask the afternoon team what they can arrange, then come back to you with an available time.
Ms Rahman | Thank you. An [[afternoon slot::An afternoon slot is the requested later housekeeping allocation; the team has not yet confirmed it.]] would work. It does not have to be exactly two. I just do not want another knock before then.
Nico | I also need to correct our earlier note. It says you declined housekeeping for all three nights. Is that what you intended?
Ms Rahman | No, not for the [[whole stay::The whole stay covers all three nights, whereas the guest has only stated today's timing preference.]]. I only declined this morning. Please do not cancel the other days because of that.
Nico | I am sorry; that note went beyond what you asked. I will correct it to today's request only.
Ms Rahman | Someone also said guests from my country usually want no service. That felt like an [[assumption::An assumption substitutes an unverified group-based belief for this particular guest's stated request.]] about me. Please just ask what I need.
Nico | You are right. We should have asked you directly. I will keep the note about the service and timing, not your nationality.
Ms Rahman | Good. My [[preference::The preference is the individual's choice for today, not a permanent choice determined by nationality.]] today is a quiet morning and housekeeping later if you have space. That is all I need the team to know.
Nico | I have entered no routine entry before two today; later housekeeping requested, awaiting the team's reply. Does that describe it correctly?
Ms Rahman | Yes. Could you make sure the [[housekeeping note::The housekeeping note carries the practical request to the team and must not imply cancellation of all service.]] still says I want service later? I do not want the afternoon team to think I refused everything.
Nico | It does. This covers ordinary housekeeping visits; the hotel's separate emergency procedures are unchanged.
Ms Rahman | Understood. I am asking about [[routine service::Routine service means ordinary housekeeping, distinct from entry governed by a separate urgent-situation procedure.]], not emergencies. Please let me know if the afternoon team cannot fit me in.
Nico | I will. I have recorded the request, but I still need their answer before I can say it is arranged.
Ms Rahman | Please send me the [[confirmation::Confirmation establishes the arrangement after availability is checked; entering a request does not provide it.]] once you have it. A recorded request has been mistaken for a booking on another stay.
Nico | Certainly. We can check tomorrow's arrangements separately when you know what you would like.
Ms Rahman | That suits me. I may want a different [[time window::The time window is the period for service; tomorrow's period has not been requested or agreed.]] tomorrow, but I have not decided. Please leave tomorrow's timing open for now.
Nico | To confirm today's request: no routine visit before two, housekeeping afterward if available, and no change requested for the remaining days.
Ms Rahman | Correct. That is a clear, [[factual::Factual describes a note limited to the stated service request, without cultural explanations or invented future preferences.]] note. Thank you for correcting it. I will wait for your message about the afternoon.''',
    transfer_title='A one-day request stays a one-day request',
    transfer_setup='A guest asks for no routine service before 15:00 today and requests later service if available. The team has not confirmed a slot. No preference has been stated for tomorrow.',
    transfer='''Agent: "The no-entry boundary is before ___ today." | 15:00 | The guest supplied fifteen hundred as today's routine-entry boundary.
Guest: "Later service is subject to ___." | availability | The team has not yet confirmed that a suitable later slot exists.
Agent: "Tomorrow's preference remains ___." | unstated | No request has been supplied for the following day.
Guest: "Please record my individual request without a cultural ___." | stereotype | A nationality-based generalization is not evidence of this guest's service preference.''',
    rehearsal=['Read the completed script, giving the guest time to correct the whole-stay assumption.', 'Repeat turns 11-16, distinguishing the recorded request from the service confirmation.', 'Switch roles for the transfer and stress today without applying that timing to tomorrow.']))
