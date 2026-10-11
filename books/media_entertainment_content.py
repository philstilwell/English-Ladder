"""Original media and entertainment cases for the English Ladder learner book."""
from books.authoring import unit

BOOK = dict(
    slug='media-entertainment', title='Media and Entertainment English',
    cover_label='ENGLISH FOR CREATIVE AND PRODUCTION TEAMS',
    cover_title='Media and\nEntertainment', cover_size=32,
    tagline='Make the brief specific.\nKeep the story, rights, and delivery aligned.',
    audience='For producers, editors, creative teams, talent coordinators, distribution staff, and communications professionals.',
    map_intro='Eight production conversations: clarify a creative direction, repair a shooting schedule, check music rights, coordinate talent approval, compare distribution offers, explain audience results, respond to a sponsor change, and prepare a factual public statement.',
    notes_title='Be specific without flattening the creative idea',
    notes_intro='Creative work needs room for interpretation, but production commitments need precise language. These cases practice translating taste, deadlines, permissions, performance, and public claims into decisions that colleagues can act on.',
    field_notes=[
        ('Turn an adjective into an observable choice', 'Premium, energetic, and cinematic can suggest different things to different colleagues. Ask about audience, references, pace, framing, sound, and deliverables.', '"Which part of that reference do you want us to follow: the pacing or the lighting?"'),
        ('Separate a proposal from a cleared commitment', 'A schedule, music cue, talent appearance, or distribution deal may still depend on an approval. Name the actual dependency instead of saying everything is locked.', '"The edit is ready for review; the music use is not yet cleared."'),
        ('Compare the complete deal', 'Fees, territories, duration, exclusivity, platforms, and deliverables work together. A higher headline fee alone does not establish the better distribution outcome.', '"The larger fee also restricts more rights for a longer period."'),
        ('Preserve the boundary between fact and explanation', 'An incident can be confirmed before its cause is known. Public language should identify what is verified and what remains under review.', '"Filming paused at 09:20; the cause has not yet been confirmed."'),
    ],
    scope_note='All productions, clients, performers, incidents, figures, and contract terms are fictional. This book teaches professional English, not legal advice or production-safety procedures. Rights, labor conditions, disclosures, and approvals depend on the actual agreements, uses, jurisdiction, and current requirements. No exercise authorizes publication, unsafe work, or use of uncleared material.',
    sources=[
        dict(title='U.S. Copyright Office. Musical Works, Sound Recordings & Copyright.', url='https://www.copyright.gov/engage/docs/recording.pdf', note='Background on the distinction between a musical composition and a particular sound recording. The fictional clearance case does not decide legal ownership.', checked='1 October 2026'),
        dict(title='U.S. Copyright Office. Copyright and the Music Marketplace, synchronization-rights discussion.', url='https://www.copyright.gov/docs/musiclicensingstudy/copyright-and-the-music-marketplace.pdf', note='Background terminology for audiovisual music permissions. The book does not rely on historical prices, market shares, or licensing terms as current facts.', checked='1 October 2026'),
        dict(title='Federal Trade Commission. Endorsement Guides: What People Are Asking.', url='https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking', note='Background on truthful endorsements and clear sponsorship disclosures. The sponsor dialogue uses invented requests and does not prescribe a universal disclosure formula.', checked='1 October 2026'),
        dict(title='The Associated Press. News Values and Principles: Telling the Story.', url='https://www.ap.org/about/news-values-and-principles/telling-the-story/', note='Background on verification, attribution, and visible corrections. The production-incident conversation is original, not an AP transcript or policy statement.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Creative Briefs and Development Notes',
    scene='What does premium and energetic actually mean?',
    skill='Clarify creative adjectives through audience, references, observable choices, and delivery requirements.',
    brief='Client Sora asks director Ellis for a video that feels premium and energetic. The request contains no target audience, reference examples, duration, aspect ratio, or release channel. In the meeting, Sora confirms adult first-time buyers, a 30-second main film for the brand website, and a 16:9 frame. She wants deliberate product close-ups and energetic editing, not flashing transitions. A shorter, 15-second vertical social cutdown is only a possible later request. Ellis must document the agreed direction without treating that possible extra version as included or fully priced.',
    cast='Sora | Client brand lead\nEllis | Creative director',
    culture=('Clarification is part of creative work', 'A direct request for examples can sound like resistance if it is detached from the client\'s aim. Acknowledge the desired impression, then offer a concrete distinction. Confirm the chosen interpretation so that later feedback has a shared reference point.'),
    a='''Who is the confirmed audience? | Adult first-time buyers | Existing trade distributors only | Children under ten | Every possible viewer equally | Sora explicitly identifies adult first-time buyers as the target audience in the meeting.
Which deliverable is confirmed? | A 30-second 16:9 film for the brand website | A 90-second cinema trailer | A completed vertical social cutdown | A series of six television spots | The confirmed duration, frame, and channel belong to the main website film only.
What remains only a possible later request? | A vertical social cutdown | Product close-ups | Energetic editing | The 16:9 main frame | The vertical version is not yet included, approved, or fully priced.''',
    vocabulary='''creative brief | A document setting the communication task and production requirements. | clarify the creative brief
target audience | The intended group of viewers. | define the target audience
single-minded proposition | The main message the communication should convey. | sharpen the single-minded proposition
creative territory | A distinct direction for developing an idea. | explore a creative territory
treatment | A written or visual account of the proposed creative approach. | develop a treatment
mood board | A collection of visual references expressing a direction. | review a mood board
reference film | An existing film used to explain a specific creative quality. | select a reference film
storyboard | A sequence of images planning the shots or story. | approve the storyboard
animatic | A timed sequence of storyboard images, often with sound. | review an animatic
shot list | A list of planned shots for production. | prepare the shot list
close-up | A shot framing a subject or detail tightly. | capture a product close-up
pacing | The perceived rhythm and speed of an edit or sequence. | adjust the pacing
transition | The change from one shot or scene to another. | simplify the transition
visual hierarchy | The ordering of visual elements by importance. | establish visual hierarchy
tone of voice | The characteristic style of the spoken or written message. | define the tone of voice
call to action | The action the audience is asked to take. | clarify the call to action
deliverable | A specified item or version to be supplied. | confirm the deliverables
aspect ratio | The proportional relationship between frame width and height. | specify the aspect ratio
running time | The duration of a film or version. | confirm the running time
cutdown | A shorter version adapted from a longer piece. | scope a cutdown
safe area | A defined frame area protecting essential content from cropping or overlays. | check the safe area
supers | Text placed over the moving image. | review the supers
brand lockup | An approved arrangement of brand marks and related elements. | use the approved brand lockup
creative sign-off | Approval of a specified creative version or direction. | record creative sign-off''',
    precision='Energetic can refer to pacing, movement, music, or transitions. Here it means energetic editing, not flashing transitions. A reference is useful only when the team states which feature is being borrowed as inspiration.',
    precision_extra='A 16:9 main film does not automatically include a vertical adaptation. Reframing can affect shots, text, and approvals. Record a possible cutdown as a separate scope question until its requirements and authorization are established.',
    phrases='''Acknowledge the direction | I understand that you want it to feel premium and energetic.
Request a concrete distinction | Do you mean faster pacing, more camera movement, or both?
Identify the viewer | Who needs to understand the product after watching?
Confirm the audience | We are addressing adult first-time buyers.
Pin down the duration | Is thirty seconds the confirmed main running time?
Name the delivery channel | The main film is for the brand website.
Specify the frame | The confirmed aspect ratio is sixteen by nine.
Limit the reference | Let us use the close-ups as a reference, not copy the entire film.
Translate the adjective | We will use deliberate product close-ups and an energetic edit.
Record the exclusion | Flashing transitions are not part of this direction.
Separate possible scope | The vertical cutdown remains a possible later request.
Ask about the message | What is the one product point the viewer must retain?
Check the action | What should the viewer do after the final frame?
Confirm the review stage | The treatment will come back for creative sign-off.
Avoid an unpriced commitment | I have not included a vertical version in this scope.
Close with a read-back | I will circulate the audience, style, format, and outstanding questions.''',
    notes='''Do you mean | Offers interpretations without pretending the adjective is already precise.
Confirmed | Distinguishes the current agreement from an idea still under discussion.
As a reference | Uses an example to explain a quality, not authorize copying.
Not part of | Makes an exclusion explicit and easy to verify.
Remains a possible | Prevents a tentative request from becoming an agreed deliverable.
The one ... point | Narrows the message so the team can prioritize the edit.''',
    d='''Which question best clarifies energetic? | Do you mean faster pacing, camera movement, or flashing transitions? | Can we use premium as the final acceptance criterion without examples? | Should we increase every shot's duration to match the reference exactly? | Can we add a vertical deliverable to demonstrate energy? | The correct question offers observable creative dimensions relevant to the ambiguous adjective.
Which read-back preserves the agreement? | Thirty seconds, 16:9, website, adult first-time buyers; vertical cutdown unconfirmed. | Thirty seconds in every format at the same price. | Vertical social film only, with flashing transitions. | Every audience and every release channel are approved. | The accurate read-back retains the confirmed requirements and leaves the possible extra version unresolved.
What is a useful reference-film instruction? | Identify the particular pacing or framing feature to discuss. | Copy the entire reference without checking rights. | Treat every element as approved automatically. | Use the reference instead of specifying an audience. | A named feature makes the reference actionable without replacing the brief or authorizing copying.
Which statement overcommits scope? | The vertical adaptation is included even though it is only a possible request. | We will scope the vertical version separately. | The website film has a 16:9 frame. | The treatment needs creative sign-off. | The possible later cutdown has not been included or fully priced in the stated scope.''',
    rehearsal=['Read turns 1-10; turn the two style adjectives into observable production choices.', 'Swap roles for turns 11-20; distinguish the main film from the shorter optional version.', 'Complete the transfer and read back audience, duration, frame, and unconfirmed scope.'],
    dialogue='''Sora | The last film looked polished, but it took too long to get going. Can this one feel premium without losing that first burst of energy?
Ellis | That helps. Let us sharpen the [[creative brief::Creative brief turns the desired impression into a shared communication task with specific production requirements.]] before we choose a style. Who should the film speak to, and what should they understand about the product by the end?
Sora | Adult first-time buyers. They will see it on our brand website, and they should quickly understand what the product is for.
Ellis | Then the [[target audience::Target audience identifies the intended adult first-time buyers, guiding explanation and creative choices rather than assuming existing product knowledge.]] needs a clear introduction. We should not rely on the product knowledge that an existing customer might already bring.
Sora | I like deliberate close shots of the product. I do not want the film to look cheap just because the edit is energetic.
Ellis | We can use a [[close-up::Close-up is a tight shot of the product or a detail, matching the client's specific visual preference.]] to show important details and let the edit supply momentum. Faster does not have to mean flashing transitions or constant camera movement.
Sora | Exactly. No flashing transitions. The rhythm should be lively, but the product should remain easy to inspect.
Ellis | That makes [[pacing::Pacing describes the perceived rhythm and speed; energetic editing can supply it without the excluded flashing transitions.]] the main tool for energy. Do you have a reference where the rhythm feels right, even if the subject is different?
Sora | I can send one. I want the team to discuss the editing, not reproduce its entire visual style.
Ellis | Good. We will label it as a [[reference film::Reference film provides an example of a named quality; it does not authorize copying or adopt every creative element.]] for rhythm only. That avoids turning one useful example into an instruction to imitate every shot, color, or music choice.
Sora | The main film needs to be thirty seconds. It will appear in the normal wide player on the website.
Ellis | I will record a thirty-second [[running time::Running time specifies the duration of the main film, which the client confirms as thirty seconds.]] and a sixteen-by-nine frame. Those requirements help us judge how much explanation and product detail the edit can carry.
Sora | We may want a shorter, fifteen-second vertical version for social later. Please do not include it as confirmed scope yet.
Ellis | Then the [[cutdown::Cutdown is a shorter adapted version; the possible vertical version remains a separate scope question rather than an included deliverable.]] stays outside the confirmed scope for now. Vertical reframing may affect the shots and text, so I will not describe it as automatically included.
Sora | Please show us the approach before you organize a shoot.
Ellis | I will prepare a [[treatment::Treatment presents the proposed creative approach for review before the production team commits to executing it.]] with the audience, visual direction, pacing references, and main format. It will also show the questions we still need to settle.
Sora | We should agree what viewers are meant to do after watching. The final message needs some work.
Ellis | Yes, the [[call to action::Call to action identifies the requested viewer response; it remains a message decision rather than an assumed element.]] is still open. I will flag it instead of filling the end frame with a message that no one has approved.
Sora | So the confirmed direction is deliberate product detail, an energetic edit, no flashing transitions, and a thirty-second website film.
Ellis | Correct. We will seek [[creative sign-off::Creative sign-off approves a specified direction or version; this review should preserve the agreed requirements and outstanding decisions.]] on that treatment. The optional vertical version and final action message will remain clearly separate until they are decided.''',
    transfer_title='Read back a second creative brief',
    transfer_setup='A client confirms a 45-second film for returning subscribers, in a 1:1 frame, for an email-linked campaign page. A six-second teaser is only a possible later request.',
    transfer='''Director: "The confirmed running time is ___." | 45 seconds | Forty-five seconds is the duration explicitly agreed for the main film.
Client: "The target audience is ___." | returning subscribers | The briefing names returning subscribers rather than first-time buyers as the intended viewers.
Director: "The confirmed aspect ratio is ___." | 1:1 | One to one is the square frame specified for this main version.
Client: "The unconfirmed later version is a ___." | six-second teaser | The teaser remains a possible later request and must not be treated as included scope.''',
))

BOOK['units'].append(unit(
    title='Production Planning and Budget',
    scene='The location move does not fit the call sheet',
    skill='Explain a scheduling dependency, quantify the immediate gap, and separate a revised estimate from spending approval.',
    brief='A revised shoot plan ends work at Location A at 12:00 and starts filming at Location B at 12:30. The company move takes 35 minutes, followed by 45 minutes of setup; these tasks cannot overlap in this plan. The earliest filming start is therefore 13:20, before any extra delay. The approved budget is $25,000. New transport costs $750 and added equipment costs $250; possible overtime remains unpriced. Producer Leena and first assistant director Grant must revise the plan without cutting required breaks or treating the new costs as approved.',
    cast='Leena | Producer\nGrant | First assistant director',
    culture=('A precise no can preserve the shoot', 'Production teams may feel pressure to accept an optimistic schedule to keep a client happy. State the dependency and arithmetic, then offer a planning decision. Avoid making the crew absorb an impossible promise through skipped safeguards or undocumented overtime.'),
    a='''What is the earliest filming start at B on the stated assumptions? | 13:20 | 12:30 | 12:35 | 12:45 | Thirty-five minutes of movement plus forty-five minutes of setup after noon gives thirteen twenty.
How much known additional cost has been identified? | $1,000 | $750 | $250 | $26,000 | Transport of $750 plus equipment of $250 totals $1,000 in identified additions.
Which cost remains unpriced? | Possible overtime | The $750 transport | The $250 equipment | The original $25,000 budget | The briefing explicitly leaves possible overtime unpriced rather than assuming it costs nothing.''',
    vocabulary='''call sheet | The daily production document listing timing, locations, and key information. | revise the call sheet
company move | Relocation of the production unit between locations. | schedule the company move
setup | Preparation of a location, equipment, and scene for filming. | allow setup time
first assistant director (first AD) | The role coordinating on-set scheduling and execution. | consult the first AD
line producer | The role managing practical production resources and costs. | brief the line producer
shooting schedule | The planned sequence and timing of filming work. | update the shooting schedule
stripboard | A visual scheduling arrangement of scenes or production work. | revise the stripboard
call time | The time a person or department is required to report. | confirm the call time
wrap time | The time filming or a person's scheduled work ends. | estimate the wrap time
turnaround | The interval between one work period's end and the next call. | protect required turnaround
meal break | A scheduled break for eating under applicable conditions. | preserve the meal break
overtime | Work beyond the relevant agreed or regulated hours. | estimate overtime exposure
contingency | A planned reserve for specified uncertainties. | review the contingency
cost report | A record of production spending, commitments, and forecasts. | update the cost report
committed cost | An amount already obligated under a relevant agreement. | record committed costs
actual cost | An amount incurred and recorded on the stated basis. | reconcile actual costs
forecast cost | An estimate of expected cost at a defined point or completion. | revise forecast costs
change order | A document recording an authorized change to agreed work. | obtain a change order
location permit | Required permission to use a location under applicable rules. | verify the location permit
location release | An agreement concerning filming or use of a location. | check the location release
technical scout | A site visit assessing practical production requirements. | arrange a technical scout
load-in | Bringing equipment into a production location. | coordinate load-in
strike | Dismantling and removing a set or equipment. | schedule the strike
critical dependency | A required condition or preceding task affecting the plan. | identify the critical dependency''',
    precision='The 35-minute move and 45-minute setup are consecutive in this plan: 80 minutes after 12:00 gives 13:20. The 12:30 filming slot is short by 50 minutes, even without additional delay.',
    precision_extra='The known additions bring the cost estimate to at least $26,000 before unpriced overtime and any other verified changes. This is not a new approved budget. Do not use an estimate to imply permission to spend.',
    phrases='''Name the conflict | The twelve-thirty filming slot does not fit the location move.
Show the dependency | Setup begins only after the thirty-five-minute move.
Do the arithmetic | Thirty-five plus forty-five gives eighty minutes.
State the earliest start | The earliest filming start is thirteen twenty on these assumptions.
Quantify the shortfall | The current slot is fifty minutes too early.
Preserve the qualifications | That excludes any additional delay.
Separate the known costs | Transport adds $750 and equipment adds $250.
State the estimate | Known costs bring the estimate to at least $26,000.
Keep uncertainty visible | Possible overtime has not yet been priced.
Protect authorization | The approved budget remains $25,000 until the change is authorized.
Request a decision | We need an approved schedule and cost revision.
Avoid unsafe compression | Required breaks and safeguards cannot become our hidden buffer.
Offer a planning route | We can review the scene order with the first AD.
Check the location terms | Confirm access and permit conditions before changing the timing.
Update connected records | The call sheet and cost report must reflect the same decision.
Close with ownership | I will circulate the revised option for approval, not label it approved.''',
    notes='''Only after | Shows a task dependency, not just a preferred order.
Earliest | Gives a lower timing bound under stated assumptions.
At least | Marks a cost floor while specified costs remain unpriced.
Until ... authorized | Preserves the current approval boundary.
Hidden buffer | Names unplanned time taken from other obligations or safeguards.
For approval | Identifies a proposed revision rather than a completed authorization.''',
    d='''Which timing statement is accurate? | Filming can start no earlier than 13:20 under the stated plan. | The 35-minute move fits inside the 30-minute gap. | Setup can be ignored because the camera is already hired. | The 12:30 start is confirmed by the old call sheet. | Consecutive movement and setup require eighty minutes after noon, making thirteen twenty the earliest stated start.
Which cost statement is supported? | Known additions total $1,000; overtime remains unpriced. | All added costs are exactly $1,000 with no uncertainty. | The approved budget automatically becomes $26,000. | Transport is free because it is required. | The two priced additions total one thousand dollars, while possible overtime is explicitly unresolved.
Which wording distinguishes estimate and authority? | The revised estimate needs approval before it becomes an authorized budget change. | An estimate is the same as permission to spend. | The client deadline approves every extra cost. | Missing prices should be entered as approved zero costs. | Estimating the cost does not supply the separate authorization required for changing the budget.
Which response preserves the stated safeguards? | Revise scene order and timing while preserving required breaks and conditions. | Remove required breaks to recover the fifty minutes. | Hide the location move from the crew. | Mark overtime paid before it is priced or approved. | A schedule revision must address the real dependency without relying on skipped safeguards or invented approvals.''',
    rehearsal=['Read turns 1-10; give the move, setup, and earliest filming times in sequence.', 'Swap roles for turns 11-20; distinguish known additions from unpriced overtime.', 'Complete the transfer without overlapping the two consecutive tasks.'],
    dialogue='''Leena | Can you sanity-check the second-location plan? We wrap at A at noon, but the client has put the first interview at B at twelve thirty.
Grant | That [[shooting schedule::Shooting schedule sets the planned filming sequence and times; the proposed slot conflicts with the stated move and setup.]] does not fit the tasks. The move takes thirty-five minutes, and setup at B takes another forty-five. Those steps cannot overlap in this plan.
Leena | So the thirty-minute gap is not enough even for the move alone.
Grant | Correct. The [[company move::Company move is the thirty-five-minute relocation between sites, preceding the separate forty-five-minute setup in this plan.]] finishes at twelve thirty-five at the earliest. Then we still need setup. We should show the full dependency instead of compressing it into a travel note.
Leena | That makes the earliest filming start thirteen twenty, before any extra delay.
Grant | Yes. The [[setup::Setup requires forty-five additional minutes after arrival, producing the thirteen-twenty earliest filming time.]] cannot disappear because the client prefers the earlier slot. We need to revise the scene order or timing with the people responsible for the work.
Leena | I will ask about moving the interview. Meanwhile, should we flag the timing conflict before anyone distributes that call sheet?
Grant | Revise the [[call sheet::Call sheet communicates the operational day's timing and locations; it must reflect the authorized workable plan.]] once the plan is agreed, and flag the current conflict clearly in the meantime. The crew should not receive an impossible time as though it were settled.
Leena | The transport quote adds seven hundred fifty dollars, and the extra equipment adds two hundred fifty.
Grant | Record those in the [[cost report::Cost report tracks spending, commitments, and forecasts; the two known additions need visibility without implying approval.]]. They total one thousand dollars. The timing change may also affect overtime, but we have not priced that exposure yet.
Leena | The current approved budget is twenty-five thousand. Can I say the revised budget is twenty-six thousand?
Grant | Call that a [[forecast cost::Forecast cost is an estimate; twenty-six thousand includes the known additions but excludes still-unpriced overtime.]] floor, not an approved budget. Known additions bring us to at least twenty-six thousand, and the possible overtime remains an open amount.
Leena | We also need to know whether Location B permits the later filming and exit times.
Grant | Check the [[location permit::Location permit contains applicable permission conditions; a scheduling proposal does not establish permission for changed hours.]] and the relevant access agreement. Moving the interview may solve one conflict while creating another, so we should confirm the actual conditions.
Leena | Someone suggested using the crew's break to recover the lost time. I do not want that assumed in the plan.
Grant | Agreed. The [[meal break::Meal break is a required or agreed rest period under the applicable conditions, not an unapproved scheduling buffer.]] and other required safeguards stay protected. We must solve the schedule within the relevant working conditions, not hide the gap in time the crew is entitled to.
Leena | I will present a revised timing option with the known costs and the overtime question.
Grant | Route the proposed [[change order::Change order records an authorized alteration to agreed work; the proposed timing and cost revision still needs that decision.]] through the approval process. A client request explains why the change is being assessed, but it does not make every consequence approved.
Leena | Once a decision is made, both the crew schedule and the financial record should reflect it.
Grant | Exactly. Keep the [[critical dependency::Critical dependency identifies the required move-then-setup sequence that must remain visible in any revised production plan.]] visible: move first, setup next, filming after that. Then the team can make a real production decision instead of inheriting an optimistic thirty-minute gap.''',
    transfer_title='Calculate a second location move',
    transfer_setup='Filming at Site C ends at 10:00. A 25-minute move is followed by 35 minutes of setup, with no overlap. New transport costs $400 and equipment $150; both need approval.',
    transfer='''Producer: "The total move-and-setup time is ___ minutes." | 60 | Twenty-five minutes of movement plus thirty-five minutes of setup totals sixty minutes.
First AD: "The earliest filming start is ___." | 11:00 | Sixty consecutive minutes after ten o'clock gives an earliest start of eleven.
Producer: "The known additional cost is ___ dollars." | 550 | Four hundred dollars of transport plus one hundred fifty of equipment totals five hundred fifty.
First AD: "Those additional costs still need ___." | approval | The briefing expressly states that the priced additions have not yet been authorized.''',
))

BOOK['units'].append(unit(
    title='Rights, Clearances, and Licensing',
    scene='A music receipt is not the release clearance',
    skill='Compare intended music use with documented permission and explain a publication hold precisely.',
    brief='Editor Ada has placed track M17 in a campaign video. A receipt is in the folder, but the available license document describes only organic use on the brand website in the United States from 1 June to 31 August. The planned campaign also includes paid social in the United States and Canada through 30 November. Clearance coordinator Ben has not verified the necessary composition and recording permissions for that expanded use. Under this production\'s release process, the video stays on hold until the required scope is confirmed or an appropriately cleared replacement is used.',
    cast='Ada | Editor\nBen | Clearance coordinator',
    culture=('Separate creative preference from permission', 'A track can become emotionally attached to an edit, making a clearance objection feel like a creative rejection. Explain the missing permission dimensions and the available review routes. A temporary track is a production choice, not evidence of public-use rights.'),
    a='''Which use is described in the available document? | Organic brand-website use in the United States, 1 June to 31 August | Worldwide paid advertising forever | Paid social in Canada through November | Any use merely because a receipt exists | The available document states a limited channel, territory, and term that do not match the whole planned campaign.
Which planned use extends beyond that description? | Paid social in Canada through 30 November | Organic brand-website use in the United States during June | The stated August website use | The documented United States territory alone | Paid social, Canada, and the later end date exceed the available document's stated scope.
What is the local publication status? | On hold pending confirmed rights or an appropriately cleared replacement | Cleared because the editor likes the track | Cleared because there is a payment receipt | Automatically cleared if the track is shortened | The release process requires confirmed scope or a cleared replacement rather than assumptions based on payment or duration.''',
    vocabulary='''clearance | Confirmation of permissions required for a particular use. | complete music clearance
license scope | The boundaries of a granted permission. | verify the license scope
musical composition | The underlying music and any lyrics. | identify the musical composition
sound recording | A particular recorded performance or production of sound. | identify the sound recording
synchronization license | Permission concerning music used in timed relation to visuals. | review the synchronization license
master-use permission | Permission to use a particular sound recording. | confirm master-use permission
rights holder | The party controlling a relevant legal right. | identify the rights holder
music publisher | An entity administering relevant rights in musical works. | contact the music publisher
record label | A company involved in recorded music and potentially controlling recording rights. | verify the record label's authority
chain of title | Records showing ownership or transfer of relevant rights. | examine the chain of title
territory | The geographical area covered by permission. | confirm the licensed territory
license term | The period during which the permitted use is authorized. | check the license term
paid media | Placement or distribution supported by advertising spend. | clear paid-media use
organic use | Distribution without paid amplification in the specified context. | confirm organic-use rights
usage restriction | A condition limiting how material may be used. | identify usage restrictions
cue sheet | A record of music used in a production and relevant details. | prepare a cue sheet
temporary track | Music used provisionally while the final choice or clearance is pending. | replace the temporary track
library music | Music offered through a catalog under applicable licensing terms. | review library-music terms
royalty-free | A licensing description whose actual payment and use terms must be checked. | verify royalty-free terms
public domain | A status in which relevant copyright protection does not apply in the jurisdiction concerned. | assess public-domain status
release hold | A block on publication pending a required condition. | maintain the release hold
clearance log | A record of rights requests, documents, decisions, and gaps. | update the clearance log
rights extension | An agreed expansion of the period or scope of permission. | request a rights extension
replacement cue | A substitute music selection for a production. | assess a replacement cue''',
    precision='The composition and the specific recording are distinct rights subjects. A single provider may administer both, but the team must verify its authority and the actual grant. Do not assume a receipt establishes every required permission.',
    precision_extra='The planned channel, territory, and end date exceed the available description. Shortening the extract or calling it royalty-free does not establish the needed scope. A cue sheet records usage; it is not itself a substitute for permission.',
    phrases='''Identify the asset | We are reviewing music track M17.
Separate payment and permission | The receipt does not establish the complete license scope.
Read the actual document | The document describes organic website use in the United States.
State the documented term | The listed term runs from 1 June to 31 August.
Compare the plan | The campaign also includes paid social and Canada through November.
Name the gaps | Channel, territory, and term all need confirmation.
Distinguish rights subjects | We need the relevant composition and recording permissions checked.
Verify authority | Confirm that the licensor controls the rights it claims to grant.
Protect publication | The video remains on hold under our release process.
Avoid a duration shortcut | A shorter extract does not automatically solve the clearance issue.
Offer a viable route | We can seek the expanded rights or assess a cleared replacement.
Keep an alternative conditional | The replacement also needs its intended uses verified.
Record the evidence | Link the license and scope decision in the clearance log.
Distinguish a usage record | A cue sheet documents the music; it does not grant the rights.
Separate edit and release | The creative edit can be ready while public release remains blocked.
Close with a clear condition | Release follows confirmed scope, not an assumed meaning of royalty-free.''',
    notes='''Describes | Reports what the available document says without inventing a broader grant.
Also includes | Identifies the planned uses missing from the narrower document.
Need confirmation | Names an unresolved permission question, not proof of infringement.
Remains on hold | States the local release status until the specified condition changes.
Controls the rights | Checks the licensor's authority rather than relying on a familiar brand.
Can be ready while | Separates creative completion from legal or operational release readiness.''',
    d='''Which sentence best identifies the mismatch? | The plan extends the documented channel, territory, and term. | The receipt proves worldwide perpetual advertising rights. | Canada is automatically included in United States-only wording. | Paid social is always the same as organic website use. | The planned paid social, Canadian territory, and November end date exceed the described grant.
What must be distinguished when checking this recorded track? | The underlying composition and the particular recording | A cue-sheet entry and an export setting, as the two rights grants | The invoice amount and track length, as proof of complete permission | The platform upload license and the editor's subscription, without checking the rights holders | The musical work and its recorded performance can involve distinct permissions and controlling parties.
Which item is not itself a rights grant? | A cue sheet listing the music used | A verified license covering the actual use | An authorized extension with the relevant scope | Permission from the appropriate rights controller | A cue sheet records use and details, but listing the track does not itself grant permission.
Which next action respects the release process? | Seek the expanded permissions or verify a replacement before release. | Publish first and ask only if challenged. | Shorten the extract and assume it is cleared. | Relabel the file royalty-free without reading terms. | The stated process requires actual clearance of the intended use rather than a labeling or duration shortcut.''',
    rehearsal=['Read turns 1-10; name the channel, territory, and term gaps in the proposed use.', 'Swap roles for turns 11-20; separate composition, recording, and usage documentation.', 'Complete the transfer while keeping documented permission separate from proposed use.'],
    dialogue='''Ada | M17 finally makes the edit work. I found the receipt, but can you check clearance before I mark the export ready for release?
Ben | The payment record does not establish the full [[license scope::License scope defines permitted uses; a receipt alone does not show the required channel, territory, term, and rights coverage.]]. The document we have describes organic brand-website use in the United States from June first through August thirty-first.
Ada | Our campaign includes paid social as well. Does that fall within the website permission?
Ben | We have not confirmed [[paid media::Paid media involves purchased advertising placement or amplification, which is additional to the organic website use described in the document.]] coverage. We need the actual grant checked against that plan. I cannot turn organic website wording into paid social permission just because the same video is involved.
Ada | We also planned to run the campaign in Canada. The music file itself does not mention countries.
Ben | The relevant [[territory::Territory specifies the geographic permission boundary; the document names the United States, while the plan also includes Canada.]] is in the license, not inferred from the file. The document names the United States only, so Canada needs to be addressed in the rights review.
Ada | And our paid campaign continues through the end of November.
Ben | That also exceeds the documented [[license term::License term is the authorized period; the available August end date does not establish permission through November.]]. We have an August end date in the available document and a November end date in the plan. Those dates need an explicit resolution.
Ada | The provider said it was library music. Should we contact the composer or the performer?
Ben | First verify who controls the relevant [[musical composition::Musical composition is the underlying work, distinct from the specific sound recording used in the edit.]] and recording rights. One provider may administer both, but we need evidence of authority and scope rather than guess from the track label.
Ada | So permission for the song does not automatically tell us whether this exact recording is covered.
Ben | Correct. Check the applicable [[master-use permission::Master-use permission concerns the particular recording, so composition permission alone cannot be assumed to cover that recording.]] as well. We should map the intended audiovisual use to the permissions actually granted by the authorized parties.
Ada | The campaign team wants to keep the date. Would using a shorter extract change the clearance question, or would we still need the wider grant?
Ben | A shorter extract does not establish clearance. The [[release hold::Release hold blocks publication under this production's process while the intended-use permissions remain unconfirmed.]] stays in place under our process until the necessary scope is confirmed or an appropriately cleared replacement is used.
Ada | I can identify another cue, but I assume we must check that one too.
Ben | Yes. A [[replacement cue::Replacement cue is an alternative selection; it still needs permissions matching the actual planned use before release.]] is an alternative, not a shortcut around the review. Give the rights team the channels, countries, dates, and versions so it can assess the actual use.
Ada | I will keep the creative export separate from the publication approval and include the relevant documents.
Ben | Put the decision and remaining gaps in the [[clearance log::Clearance log preserves documents, scope decisions, and unresolved questions so the release team can trace the actual permission basis.]]. That helps the next reviewer see why the edit can be finished while release is still pending.
Ada | We also need to prepare the music usage record for delivery.
Ben | Prepare the [[cue sheet::Cue sheet records music use and details; it supports documentation but is not itself the permission to use the music.]], but keep its purpose clear. It records the cue used; it does not replace the rights grant or turn the unresolved campaign scope into an approval.''',
    transfer_title='Identify a second music-use gap',
    transfer_setup='A document for cue C8 covers organic website use in France through 30 September. The proposed use adds paid social in Germany through 31 December. Expanded permission is unconfirmed.',
    transfer='''Editor: "The documented territory is ___." | France | France is the territory explicitly described in the available document.
Coordinator: "The new territory needing review is ___." | Germany | Germany is added by the proposed use and is not established by the French territory description.
Editor: "The documented end date is ___." | 30 September | Thirty September is the available permission's end date, not the proposed later date.
Coordinator: "The proposed end date is ___." | 31 December | Thirty-one December is the intended campaign end, which needs rights review beyond the documented term.''',
))

BOOK['units'].append(unit(
    title='Talent, Contracts, and Approvals',
    scene='A delivery target arrives before the review window ends',
    skill='Coordinate version-specific talent approval and explain a schedule conflict without assuming silence means consent.',
    brief='For campaign F29, the fictional talent agreement allows 48 elapsed hours after confirmed receipt of the complete review package. The package includes the main film and vertical version. It is received Monday at 10:00, so the full window ends Wednesday at 10:00; all times use the same time zone. The delivery calendar targets Tuesday at 17:00. Approval may arrive earlier, but none has yet been received and silence is not deemed approval under the stated terms. Coordinator Mina must agree submission ownership and a realistic delivery message with producer Joel.',
    cast='Mina | Talent coordinator\nJoel | Producer',
    culture=('Treat approval as a documented event', 'Creative teams often use casual phrases such as they seemed happy or we should be fine. Those impressions do not establish approval of a particular version. State who received what, when the review began, and what decision is still outstanding.'),
    a='''When does the full review window end? | Wednesday at 10:00 | Tuesday at 10:00 | Tuesday at 17:00 | Monday at 17:00 | Forty-eight elapsed hours after Monday at ten ends Wednesday at ten in the same time zone.
What must the complete package include here? | The main film and vertical version | Only a thumbnail | Only the main film | A verbal summary without files | The fictional terms explicitly require both versions in the complete review package.
What does silence mean under these terms? | It is not deemed approval. | Automatic approval at Tuesday's target | Approval of every future version | Permission to remove the review requirement | The briefing expressly states that silence is not deemed approval under this agreement.''',
    vocabulary='''talent agreement | A contract governing a performer's engagement and relevant uses. | review the talent agreement
approval right | A contractual right to review and approve specified material. | respect the approval right
review window | The time allowed for a specified assessment. | calculate the review window
complete submission | Delivery of all materials required to start the stated review. | confirm a complete submission
receipt confirmation | Evidence that the relevant recipient received the materials. | obtain receipt confirmation
elapsed hours | Continuous hours passing from a stated starting point. | count elapsed hours
business days | Working days as defined by the relevant agreement or process. | define business days
deemed approval | Approval treated as occurring under a specified contractual condition. | check deemed-approval wording
version identifier | A label distinguishing one specific file or revision. | preserve the version identifier
approval tracker | A record of submissions, recipients, deadlines, and decisions. | maintain an approval tracker
consolidated notes | Feedback combined into a coordinated set. | request consolidated notes
revision round | A defined cycle of feedback and changes. | schedule a revision round
final cut | A specified completed edit, subject to the actual approval arrangement. | identify the final cut
picture lock | The stage at which picture editing is fixed for subsequent work. | confirm picture lock
talent representative | A person authorized to act for a performer in relevant matters. | contact the talent representative
usage buyout | A negotiated payment arrangement for specified usage rights. | define the usage buyout
residual | A payment for qualifying further use under applicable terms. | check residual obligations
exclusivity clause | A term restricting specified competing engagements or uses. | review the exclusivity clause
likeness | A person's recognizable image or representation. | confirm likeness rights
voice usage | The permitted use of a person's recorded or synthesized voice. | define voice usage
digital replica | A digital representation of a person's likeness or voice. | assess digital-replica terms
reshoot | Filming material again after the original shoot. | scope a reshoot
pickup shot | Additional footage captured to complete or supplement an edit. | plan a pickup shot
approval record | Evidence of the actual decision on specified material. | retain the approval record''',
    precision='Forty-eight elapsed hours is not the same as two business days unless the agreement makes them equivalent. This case expressly uses elapsed hours and one time zone. The full window ends Wednesday at 10:00.',
    precision_extra='A Tuesday target does not shorten the agreed review window. Earlier approval is possible, not guaranteed. A changed version may require further review under the actual terms; approval of one file should not be generalized to every export.',
    phrases='''Locate the governing term | The agreement allows forty-eight elapsed hours.
Confirm the start event | The complete package was received Monday at 10:00.
List the required versions | The package contains the main film and vertical version.
Calculate the window | The full review period ends Wednesday at 10:00.
Identify the conflict | Tuesday's delivery target comes before that window ends.
Keep an early response conditional | Approval may arrive earlier, but it has not arrived yet.
Avoid assumed consent | Silence is not deemed approval under these terms.
Name the submission owner | Mina will coordinate the package and receipt confirmation.
Track the actual file | Record the version identifier with every approval.
Request a faster review | Can the representative agree to an accelerated review?
Preserve the answer boundary | A request for acceleration is not acceptance of it.
Coordinate feedback | Please return one consolidated set of notes where the process permits.
Separate creative and contractual status | Picture lock does not itself establish talent approval.
Check a changed export | Confirm whether this revision requires a new review.
Keep the client message accurate | We are awaiting the specified approval before final delivery.
Close the record | Retain the decision, version, recipient, and timestamp together.''',
    notes='''After confirmed receipt | Identifies the event that starts the clock.
Elapsed | Means continuous passing hours under the stated terms.
Comes before | Shows the calendar conflict without assuming no early response is possible.
May ... but | Preserves a possibility while stating that it is not yet an event.
Under these terms | Limits the rule to the fictional agreement, not every talent contract.
Not acceptance | Separates asking for a change from securing it.''',
    d='''Which client update is accurate? | Approval is pending; the full window ends Wednesday at 10:00, after Tuesday's target. | Tuesday's target automatically shortens the review. | The representative's silence approves the files. | Approval of a thumbnail covers every export. | The actual window and pending decision must remain visible despite the earlier delivery target.
Which calculation follows the stated terms? | Monday 10:00 plus 48 elapsed hours equals Wednesday 10:00. | Monday 10:00 plus 48 hours equals Tuesday 10:00. | Forty-eight elapsed hours always means two local business days. | The clock starts whenever the editor opens the project. | The case defines continuous elapsed hours starting from confirmed complete-package receipt.
Which action is supported? | Ask whether an accelerated review can be agreed without assuming acceptance. | Announce an accelerated window before anyone agrees. | Remove the vertical version from the recorded package after receipt. | Treat any positive informal comment as final approval. | An acceleration request is legitimate, but the requested change requires an actual agreement or decision.
What should the approval record identify? | The particular version, decision, recipient, and timestamp | Only the production's nickname | A guessed approval based on the deadline | Every future edit regardless of changes | Version-specific evidence prevents approval of one submission from being applied indiscriminately to another.''',
    rehearsal=['Read turns 1-10; calculate the elapsed-hour window from complete receipt.', 'Swap roles for turns 11-20; request acceleration without reporting it as agreed.', 'Complete the transfer and distinguish the client target from the review deadline.'],
    dialogue='''Joel | The client wants F29 Tuesday at five. I see Monday\'s submission in the tracker, but no decision. How much of the review window is still left?
Mina | Approval is still pending. The [[talent agreement::Talent agreement supplies the actual review terms; the delivery target does not replace those terms or establish approval.]] allows forty-eight elapsed hours after confirmed receipt of the complete package. We received confirmation for Monday at ten, but no approval decision.
Joel | Was that package complete, including the vertical version?
Mina | Yes. The [[complete submission::Complete submission includes both the main film and vertical version, satisfying the stated package requirement for starting this review.]] contained the main film and vertical version. I will keep the file identifiers with the receipt so we know exactly what the representative is reviewing.
Joel | Forty-eight hours takes us to Wednesday at ten, using the same time zone.
Mina | Correct. Those are [[elapsed hours::Elapsed hours run continuously from Monday at ten to Wednesday at ten under the fictional agreement.]], not an assumed business-day calculation. The calendar needs to show that full window, even though our preferred delivery time is earlier.
Joel | They might answer on Tuesday. I do not want to tell the client that Wednesday is certain if an earlier response is possible.
Mina | Agreed. The [[review window::Review window is the allowed assessment period; it does not prevent an earlier response, but no early approval is guaranteed.]] ends Wednesday, but approval could arrive sooner. We should communicate the dependency without pretending either the early response or a delay is already decided.
Joel | Could we treat no response by Tuesday afternoon as consent?
Mina | No. The stated terms do not provide [[deemed approval::Deemed approval would arise only under specified terms; this agreement expressly does not treat silence as approval.]]. A deadline on our internal calendar does not create that mechanism. Silence cannot be turned into a positive decision here.
Joel | Then please ask whether the representative can accommodate an accelerated review.
Mina | I will contact the [[talent representative::Talent representative is the appropriate contact for the review request; asking for acceleration does not establish its acceptance.]]. I will distinguish our request from their answer and record any agreed change. Until then, the original window remains the planning basis.
Joel | If we receive notes, I would like one coordinated list instead of conflicting messages from several people.
Mina | I can request [[consolidated notes::Consolidated notes combine feedback into a coordinated set, helping the team plan a revision without inventing approval.]] where the process permits. We will still preserve who gave the feedback and what it concerns, rather than merge away a substantive disagreement.
Joel | The editor says picture is locked. Does that make the remaining review only a formality?
Mina | No. [[Picture lock::Picture lock fixes the picture-editing stage for subsequent work; it does not itself satisfy the separate talent approval requirement.]] describes an editing stage. It does not cancel the approval right. If a requested change affects the edit, we must assess it under the actual agreement and schedule.
Joel | Can you own the submission and follow-up? I need one place to check which files were received and whether the decision covers them.
Mina | I will own the [[approval tracker::Approval tracker records submissions, versions, recipients, timing, and decisions so responsibility remains clear throughout the process.]]. If a file changes, I will check whether it needs a new review and keep that separate from any decision on the previous version.
Joel | I will tell the client approval is pending, the full window ends Wednesday at ten, and we have requested an earlier response.
Mina | That is accurate. Once we have an [[approval record::Approval record documents the actual decision on identified material; it replaces speculation based on deadlines or informal impressions.]], we can update the delivery status. Until then, a requested acceleration and a locked edit must not be reported as completed approval.''',
    transfer_title='Track a second review window',
    transfer_setup='A fictional agreement allows 24 elapsed hours after complete receipt, with no deemed approval. The package is received Thursday at 14:00 in the same time zone used for all deadlines. The client target is Friday at 09:00; approval is pending.',
    transfer='''Coordinator: "Receipt was confirmed on ___." | Thursday at 14:00 | Thursday at fourteen hundred is the stated event that starts the review clock.
Producer: "The full window ends on ___." | Friday at 14:00 | Twenty-four elapsed hours after Thursday at fourteen hundred ends Friday at fourteen hundred.
Coordinator: "The earlier client target is ___." | Friday at 09:00 | Friday at nine is the desired delivery target, not the end of the agreed review window.
Producer: "Silence is not deemed ___." | approval | The supplied terms expressly exclude treating silence as an approval decision.''',
))

BOOK['units'].append(unit(
    title='Distribution and Windowing',
    scene='The larger fee also sells a broader restriction',
    skill='Compare distribution offers across fee, rights, territory, term, and exclusivity without inventing net value.',
    brief='For documentary North Line, Offer A proposes a flat $30,000 fee for exclusive worldwide video-on-demand rights for 24 months. Offer B proposes a flat $22,000 fee for nonexclusive advertising-supported video-on-demand rights in the United States for six months. Both proposed terms would begin on the same date, but neither deal is signed. Delivery costs, taxes, and other deductions are not supplied; available underlying rights still require verification. Sales lead Priya and producer Mason must compare the offers without choosing solely by fee or assuming both can be accepted unchanged.',
    cast='Priya | Distribution sales lead\nMason | Producer',
    culture=('Describe the restriction as part of the price', 'A headline fee can dominate a fast sales conversation. Put the rights granted beside the money received. Questions about exclusivity are not necessarily resistance to a deal; they identify which future choices the offer would remove.'),
    a='''Which offer has the larger headline fee? | A, at $30,000 | B, at $22,000 | Both are $30,000 | Neither specifies a fee | Offer A explicitly states thirty thousand dollars, exceeding B's twenty-two thousand.
Which offer is narrower in stated territory and duration? | B: United States, six months | A: worldwide, 24 months | Both are worldwide forever | Neither specifies a duration | Offer B is limited to the United States and six months under the supplied terms.
Can both be accepted unchanged without examining overlap? | No; A's exclusive rights overlap B's proposed use. | Yes; different fees prevent overlap. | Yes; B's nonexclusivity overrides A automatically. | Yes; unsigned proposals have already granted both rights. | A's worldwide exclusive video-on-demand scope includes the United States advertising-supported use proposed by B.''',
    vocabulary='''distribution window | A defined period or sequence for particular release rights. | plan a distribution window
territorial rights | Rights limited to specified geographic areas. | define territorial rights
exclusive license | Permission reserving the specified licensed use to the licensee under its terms. | negotiate an exclusive license
nonexclusive license | Permission that does not itself reserve the use to one licensee. | offer a nonexclusive license
video on demand (VOD) | Content available for viewing at a user's chosen time. | license VOD rights
advertising-supported VOD (AVOD) | On-demand viewing funded through advertising under the service model. | compare AVOD offers
subscription VOD (SVOD) | On-demand viewing under a subscription service model. | define SVOD rights
transactional VOD (TVOD) | On-demand viewing paid for per rental or purchase. | negotiate TVOD terms
free ad-supported streaming TV (FAST) | Scheduled streaming channels available without subscription and supported by ads. | evaluate FAST distribution
holdback | A contractual restriction delaying another release or use. | review the holdback
carve-out | An explicit exception to a broader rights restriction. | negotiate a carve-out
rights reversion | Return or expiration of granted rights under the agreement. | confirm rights reversion
license fee | Payment for the specified permission. | compare license fees
minimum guarantee | A contractually specified minimum payment, often linked to later accounting. | review the minimum guarantee
revenue share | An agreed division of defined income. | calculate revenue share
recoupment | Recovery of specified amounts from defined revenues. | examine recoupment terms
distribution fee | An amount charged for distribution services under the agreement. | verify the distribution fee
delivery specification | Technical and material requirements for supplied content. | check delivery specifications
localization | Adapting content for a language or market. | price localization
caption file | A file carrying timed text for accessible or translated presentation. | deliver the caption file
geoblocking | Restricting access based on geographic location. | verify geoblocking requirements
avails | Information about the rights and periods available for licensing. | update the avails
rights grid | A table mapping rights by territory, medium, and period. | maintain the rights grid
net receipts | Income remaining after the deductions defined by the agreement. | define net receipts''',
    precision='The $8,000 fee difference does not establish an $8,000 difference in profit or overall value. A grants broader and longer exclusive rights. Costs, deductions, existing commitments, and future opportunities require their own review.',
    precision_extra='Nonexclusive means B would not itself demand exclusivity; it does not override exclusivity granted to A. Because both proposed terms start together, A overlaps B. Any carve-out would require an actual negotiated agreement.',
    phrases='''Start with the headline | Offer A pays $30,000 and Offer B pays $22,000.
Add the missing context | The larger fee comes with broader exclusive rights.
State A's duration | A proposes twenty-four months.
State B's duration | B proposes six months.
Name the territorial difference | A is worldwide; B is United States only.
Separate the media scopes | A covers VOD broadly, while B specifies AVOD.
Preserve proposal status | Neither offer is signed.
Identify the overlap | A's exclusive scope overlaps B's proposed use.
Reject an automatic combination | We cannot simply accept both unchanged.
Explore a negotiated route | We could ask whether A will agree to an AVOD carve-out.
Keep the request conditional | A requested carve-out is not a granted exception.
Verify available rights | Check the underlying rights and existing commitments first.
Avoid a net-value claim | We do not yet have the delivery costs or deductions.
Make definitions explicit | Net receipts depend on the actual agreement.
Record the comparison | Put fee, term, territory, media, and exclusivity on one rights grid.
Close without premature selection | The fee comparison is clear; the full commercial decision is still open.''',
    notes='''Comes with | Connects the payment to the restriction received in exchange.
Proposes | Marks an offer as unsigned rather than already effective.
Broadly ... while | Contrasts a wider category with a narrower specified use.
Cannot simply | Challenges an unsupported shortcut without excluding negotiation.
Will agree to | Identifies the other party's required consent.
Depend on | Prevents a contract term from being treated as having one universal definition.''',
    d='''Which comparison captures the main trade-off? | A pays more for broader, longer exclusive rights; B pays less for narrower, shorter nonexclusive rights. | A is automatically more profitable because its fee is larger. | B grants worldwide exclusive rights for 24 months. | Both offers grant identical rights. | The complete comparison includes scope, duration, and exclusivity alongside the headline fee.
Why does B's nonexclusive wording not solve the conflict? | It does not override the exclusivity A would receive in the overlapping scope. | Nonexclusive always means no rights are granted. | B's smaller fee legally cancels A. | Only territories matter, never media or time. | A separate nonexclusive grant cannot by itself defeat an overlapping exclusive commitment to another party.
Which statement is unsupported? | Net receipts are exactly $30,000 under A. | A's headline fee is $30,000. | B's term is six months. | Neither proposal is signed. | The missing deductions and delivery costs prevent treating the headline fee as established net receipts.
Which next step is a proposal rather than an agreement? | Ask A to consider a defined AVOD carve-out. | State that A has already accepted the carve-out. | Mark both deals signed without signatures. | Publish a worldwide availability claim without checking underlying rights. | Asking for a carve-out starts a negotiation but does not establish acceptance or available rights.''',
    rehearsal=['Read turns 1-10; compare fee, territory, term, medium, and exclusivity.', 'Swap roles for turns 11-20; distinguish a requested carve-out from an agreed one.', 'Complete the transfer without labeling either headline fee as net income.'],
    dialogue='''Mason | A is eight thousand higher. Before I recommend it, what would we be giving up that is not obvious from the fee column?
Priya | The [[license fee::License fee is the payment for defined permission; the larger amount must be read beside the rights requested.]] is larger, but the rights package is different. A wants worldwide exclusive VOD rights for twenty-four months. B wants United States AVOD rights for six months, nonexclusively.
Mason | So B leaves more future options open, at least under its own proposed restriction.
Priya | Yes, but we still need the [[rights grid::Rights grid maps medium, territory, period, and exclusivity, making both the proposed grants and existing limitations visible.]] and underlying permissions checked. We should not promise that every unmentioned right is freely available when we have not verified existing commitments.
Mason | Could we take both fees? B is nonexclusive, so it sounds compatible with another service.
Priya | B's [[nonexclusive license::Nonexclusive license does not demand sole use for B, but it cannot override exclusive rights granted separately to A.]] does not cancel A's exclusivity. Both offers begin on the same date, and A's worldwide VOD scope includes the United States use that B wants.
Mason | Then accepting A unchanged would conflict with the proposed B grant.
Priya | Correct. An [[exclusive license::Exclusive license reserves its specified use under the agreement, creating the overlap problem with B's proposed simultaneous grant.]] has to be assessed across medium, territory, and time. We cannot avoid the overlap simply by putting the proposals on different lines in a spreadsheet.
Mason | Could we ask A to leave advertising-supported viewing out of its exclusivity?
Priya | We could negotiate a [[carve-out::Carve-out is an explicit exception to a broader restriction; it would need A's actual agreement rather than an internal assumption.]]. That is a possible negotiating route, not a term already granted. The exact AVOD scope and any other restrictions would need clear wording.
Mason | I also want to know when we could offer the film elsewhere after A's period.
Priya | Check [[rights reversion::Rights reversion concerns when granted rights return or expire under the actual agreement, which must be verified rather than assumed.]] and any holdbacks in the actual draft. A headline twenty-four-month term does not tell us every end-of-term obligation or permitted next release.
Mason | The summary labels the thirty thousand net income, but delivery and localization are still unpriced. Can we fix that label before it reaches the producer?
Priya | Then it should not label that [[net receipts::Net receipts require the agreement's defined deductions and relevant costs; the headline fee alone does not establish that amount.]]. We only have the flat headline fee here. Delivery costs, taxes, and other deductions are not supplied, so the net comparison is incomplete.
Mason | B specifically wants advertising-supported on-demand rights. Does that automatically include scheduled free streaming channels?
Priya | Do not assume so. [[Advertising-supported VOD::Advertising-supported VOD refers to on-demand viewing funded by advertising and should not be silently expanded to every ad-supported distribution format.]] names its stated service model. A scheduled FAST channel is a different format that needs its own rights description in the agreement.
Mason | We should ask each buyer for its technical package before estimating delivery effort.
Priya | Yes. The [[delivery specification::Delivery specification defines required materials and technical formats, allowing the team to assess work rather than assume equal delivery burdens.]] may include versions, captions, and localization. Those requirements affect cost and readiness even when the headline fee is fixed.
Mason | I will keep both offers unsigned in the comparison and show their actual restrictions, not just the money.
Priya | Good. Then we can assess the [[distribution window::Distribution window organizes the period and sequence of permitted releases, connecting the deal to future exploitation choices.]] and negotiate from a complete picture. A's higher fee is established; its overall superiority is not established by that number alone.''',
    transfer_title='Compare another pair of offers',
    transfer_setup='Offer C pays $12,000 for exclusive UK SVOD rights for 12 months. Offer D pays $9,000 for nonexclusive French AVOD rights for three months. Neither is signed; no cost figures are supplied.',
    transfer='''Producer: "C's headline fee is ___ dollars." | 12,000 | Twelve thousand dollars is the proposed fee, not an established net-income figure.
Sales lead: "D's territory is ___." | France | France is the stated geographic scope of the second offer.
Producer: "C's proposed term is ___ months." | 12 | Twelve months is the duration of the UK SVOD proposal.
Sales lead: "D's proposed term is ___ months." | three | Three months is the duration of the French AVOD proposal, distinct from C's longer term.''',
))

BOOK['units'].append(unit(
    title='Audience Metrics and Performance',
    scene='More completed plays, but a lower completion rate',
    skill='Give a balanced performance readout using distinct counts, rates, and campaign objectives.',
    brief='Two comparable reporting periods cover the same 30-second video on one platform. Period A records 1,000 eligible starts, 800 complete plays, and estimated reach of 900 accounts. Period B records 2,000 eligible starts, 1,200 complete plays, and estimated reach of 1,500 accounts. A complete play reaches the end; completion rate is complete plays divided by eligible starts. Reach and starts are different measures. Spend and business-outcome data are not supplied. Analyst Felix and account director Dana must replace an unqualified success claim with a precise account of the gains and decline.',
    cast='Dana | Account director\nFelix | Audience analyst',
    culture=('Do not make the meeting choose one flattering number', 'A client may want a simple success story while an analyst sees mixed evidence. Lead with the relevant gains and the important limitation in the same sentence. This avoids both selective praise and an equally selective claim that everything failed.'),
    a='''What is Period B's completion rate? | 60% | 80% | 75% | 120% | Twelve hundred complete plays divided by two thousand eligible starts equals sixty percent.
What happened to complete-play count? | It rose from 800 to 1,200. | It fell from 1,200 to 800. | It stayed at 800. | It became identical to estimated reach. | The briefing supplies eight hundred complete plays in A and twelve hundred in B.
What is not supplied? | Spend and business-outcome data | Both eligible-start counts | Both complete-play counts | The video's duration | The record explicitly leaves spending and business outcomes outside the available figures.''',
    vocabulary='''reach | The estimated or measured distinct audience under a stated method. | report estimated reach
impression | A recorded presentation of content under the platform's definition. | count impressions
eligible start | A video start included under the report's specified rules. | define eligible starts
complete play | A playback reaching the specified end point. | count complete plays
completion rate | Complete plays divided by the defined eligible-start base. | calculate completion rate
view threshold | The condition a platform uses to count a view. | check the view threshold
watch time | The total time spent viewing content under the specified method. | analyze watch time
average view duration | Viewing time divided by the relevant view count. | compare average view duration
retention curve | A display of audience continuation across a video's timeline. | inspect the retention curve
drop-off | Loss of viewers at a stage or time in playback. | locate the drop-off
frequency | Average exposures per reached audience member on the stated basis. | monitor exposure frequency
unique viewer | A distinct viewer estimated or counted under the measurement method. | estimate unique viewers
repeat play | An additional playback rather than necessarily a new viewer. | distinguish repeat plays
engagement | A defined audience interaction such as a reaction, comment, or share. | define engagement
engagement rate | Defined interactions divided by a specified audience or exposure base. | specify the engagement-rate denominator
click-through rate (CTR) | Clicks divided by the defined impression base. | calculate click-through rate
cost per thousand (CPM) | Cost for one thousand impressions on the stated basis. | compare CPM
cost per view (CPV) | Cost divided by the relevant counted views. | define cost per view
cost per completed view | Cost divided by completed views under the specified rules. | calculate cost per completed view
brand lift | A measured change in a brand-related outcome under a study design. | assess brand lift
attribution window | The time interval used to connect an outcome to an exposure or action. | specify the attribution window
measurement methodology | The rules and process used to produce a metric. | document measurement methodology
benchmark | A defined reference used to interpret performance. | choose a relevant benchmark
business outcome | A commercial result beyond the media exposure itself. | measure business outcomes''',
    precision='Complete plays increased by 400, or 50%, while completion rate fell from 80% to 60%, a decline of 20 percentage points. A larger audience can produce more completions even when a smaller share finishes.',
    precision_extra='Estimated reach is a distinct-account measure here, while starts count eligible playback events. Do not divide completions by reach and label it this report\'s completion rate. Without spend or business outcomes, cost efficiency and commercial impact remain unestablished.',
    phrases='''Lead with both results | Complete plays increased, while completion rate declined.
State the count gain | Completions rose from eight hundred to twelve hundred.
State the rate change | The rate fell from eighty to sixty percent.
Use the correct unit | That is a decline of twenty percentage points.
Show the denominator | The later period had two thousand eligible starts.
Keep reach separate | Estimated reach rose from nine hundred to fifteen hundred accounts.
Avoid a viewer claim | Twelve hundred complete plays does not necessarily mean twelve hundred different people.
Name the measurement rule | Here, a completion means playback reached the end.
Request a useful diagnostic | Let us inspect where viewers drop off.
Preserve objective differences | A reach goal and a completion-rate goal are not the same target.
Limit the commercial conclusion | These figures do not establish sales impact.
Name the missing cost | Spend is not included in this report.
Avoid a platform shortcut | Confirm the view threshold before comparing another service.
Make the summary balanced | We reached more accounts and recorded more completions, but fewer starts finished proportionally.
Ask for the right benchmark | Which agreed objective should the result be compared against?
Close with an evidence gap | Cost efficiency and business outcomes still need separate data.''',
    notes='''While | Connects simultaneous gains and a decline without hiding either.
Percentage points | Describes an absolute difference between percentage rates.
Estimated reach | Preserves the measurement qualification attached to the audience count.
Does not necessarily | Blocks a false equivalence between events and distinct people.
Here | Limits the completion definition to the stated report.
Still need | Makes the remaining evidence requirement explicit.''',
    d='''Which summary is accurate? | Complete plays rose 50%, but completion rate fell 20 percentage points. | Completion rate rose because completion count rose. | Reach and complete plays are identical measures. | Every measure proves an unqualified success. | Complete plays rose from 800 to 1,200, while the rate fell from 80% to 60%.
Which denominator produces the stated Period B completion rate? | 2,000 eligible starts | 1,500 reached accounts | 1,200 complete plays | 900 reached accounts from Period A | This report explicitly divides complete plays by eligible starts, not by reach.
Which claim requires additional evidence? | Cost per completed view improved. | Period B had more complete plays. | Period A's completion rate was 80%. | Estimated reach increased. | Cost per completed view requires spend data, which the briefing does not supply.
Which diagnostic addresses retention? | Inspect the playback retention curve for drop-off points. | Replace the denominator with whichever count gives the best rate. | Treat every repeated play as a new person. | Infer sales from reach alone. | A retention curve shows how viewing continues across the timeline and can locate drop-off patterns.''',
    rehearsal=['Read turns 1-10; report the completion count and rate together.', 'Swap roles for turns 11-20; name what cost and sales claims still require.', 'Complete the transfer using eligible starts rather than reached accounts.'],
    dialogue='''Dana | I have led with the larger reach and more finished plays. Before I send the success summary, is there anything in the retention figures I should bring forward?
Felix | We should qualify that. The [[complete play::Complete play is a playback reaching the end; its count rose from eight hundred to twelve hundred.]] count rose from eight hundred to twelve hundred, but the proportion of eligible starts that finished fell. Both results belong in the summary.
Dana | The later period had twice as many starts, so the larger completion count does not mean the same rate.
Felix | Exactly. The [[completion rate::Completion rate divides complete plays by eligible starts, giving eighty percent before and sixty percent afterward.]] moved from eighty percent to sixty percent. Two thousand starts produced twelve hundred completions, while the earlier thousand starts produced eight hundred.
Dana | That is twenty percentage points lower. The complete-play count itself is fifty percent higher.
Felix | Correct. Keep the [[eligible start::Eligible start is the defined playback-event base for this rate; changing that base would change the measure.]] denominator visible. If we quietly switch to reached accounts, we are no longer calculating the completion rate defined in this report.
Dana | Reach rose from nine hundred to fifteen hundred accounts. Can I call those fifteen hundred viewers?
Felix | Preserve the report's [[reach::Reach is estimated distinct accounts here; it should not be silently relabeled as verified individual human viewers.]] definition: estimated accounts. We should not strengthen an account estimate into a verified people count. That qualification matters when the client compares audience numbers.
Dana | And twelve hundred finished plays may include someone watching more than once.
Felix | Yes. A [[repeat play::Repeat play is another playback event and does not necessarily add a new distinct audience member.]] can add another completion without adding a distinct account. Event counts and audience counts are useful, but they answer different questions.
Dana | What should we examine to understand the lower proportion finishing?
Felix | Inspect the [[retention curve::Retention curve shows continuation through the video timeline and can reveal where viewing falls away.]]. It can show where playback drops off. We should not invent the cause from the aggregate rate, but we can identify a useful place to investigate.
Dana | The video is thirty seconds in both periods, so we are not comparing different lengths.
Felix | Good. Preserve that and the [[measurement methodology::Measurement methodology defines how the metrics were produced, supporting comparable interpretation across periods rather than assumed equivalence.]] in the readout. If we later compare another platform, we must check its view and completion definitions before treating the figures as equivalent.
Dana | The client will ask what each completed view cost. Have we received the spend figures, or is that still a gap in the report?
Felix | We cannot calculate [[cost per completed view::Cost per completed view needs spend as well as completions; the provided data contains no spending figure.]] without spend. More completions alone do not establish better cost efficiency. The answer should identify the missing cost data rather than assume it improved.
Dana | They may also want to know whether the campaign increased sales.
Felix | That [[business outcome::Business outcome concerns a commercial result beyond exposure; the audience figures alone do not establish sales impact.]] needs separate evidence and an appropriate attribution approach. Neither the reach increase nor the completion change proves a sales effect.
Dana | I will report more reached accounts and more complete plays, alongside the lower completion rate and the missing cost and sales data.
Felix | Then compare those results with the agreed [[benchmark::Benchmark is the defined reference or objective for judging performance; different goals may lead to different interpretations of the mixed results.]]. A reach objective and a retention objective may receive different answers. We can be positive about the gains without claiming every objective was met.''',
    transfer_title='Explain another mixed audience result',
    transfer_setup='Period C has 500 eligible starts and 350 complete plays. Period D has 800 eligible starts and 480 complete plays. Use completions divided by starts.',
    transfer='''Director: "C's completion rate is ___." | 70% | Three hundred fifty completions divided by five hundred starts equals seventy percent.
Analyst: "D's completion rate is ___." | 60% | Four hundred eighty completions divided by eight hundred starts equals sixty percent.
Director: "The completion count rose by ___." | 130 | Four hundred eighty minus three hundred fifty equals one hundred thirty additional complete plays.
Analyst: "The rate fell by ___." | ten percentage points | Seventy percent minus sixty percent is an absolute ten-percentage-point decline.''',
))

BOOK['units'].append(unit(
    title='Sponsorship, Brand Safety, and Integration',
    scene='One extra mention changes more than the running time',
    skill='Respond to a sponsor change by separating scope, factual claims, disclosure, and approval.',
    brief='A sponsor has approved one ten-second product mention in a program. It now requests a second fifteen-second mention and proposes the line, "This product works for everyone." No evidence supporting that universal claim is supplied. The sponsor also asks to keep the sponsorship disclosure only in the video description. Account lead Carmen and producer Noel must review the added scope, editorial fit, truthful wording, and clear in-video disclosure for the endorsement. The extra mention, revised script, cost, and timing are not yet approved; the original mention alone does not approve the new request.',
    cast='Carmen | Sponsorship account lead\nNoel | Producer',
    culture=('Separate the client relationship from the content decision', 'An extra sponsor line can sound too small to challenge. Explain its concrete effects on time, editorial flow, claims, and approval. A constructive response offers a review path without allowing the commercial relationship to substitute for truthful, clearly identified content.'),
    a='''What is already approved? | One ten-second product mention | Two mentions totaling twenty-five seconds | The universal product claim | A description-only disclosure for this endorsement | The briefing approves only the original ten-second mention, leaving the new request unresolved.
What is wrong with the proposed universal claim? | No supporting evidence is supplied. | It is automatically true because the sponsor proposed it. | It is a verified customer testimonial. | It has already passed a completed claims review. | The supplied facts do not support the assertion that the product works for everyone.
Where should the endorsement disclosure be addressed in this case? | Clearly in the video, not only in its description | Only behind an optional link | Only in a file name | Nowhere because the sponsor paid | The scenario requires clear in-video disclosure; a description-only approach can be missed by viewers.''',
    vocabulary='''sponsorship | Commercial support linked to agreed exposure or association. | disclose the sponsorship
brand integration | Incorporation of a brand or product into content. | review the brand integration
product placement | Display or inclusion of a product within content. | agree product placement
host-read | A promotional message delivered by the program's host. | approve the host-read
endorsement | A message audiences are likely to understand as another party's opinion or experience. | review the endorsement
material connection | A relationship that may affect how an audience evaluates an endorsement. | disclose a material connection
disclosure | Information making a relevant commercial relationship clear. | provide a clear disclosure
clear and conspicuous | Readily noticeable and understandable in the relevant context. | make the disclosure clear and conspicuous
substantiation | Evidence supporting a factual claim. | require claim substantiation
objective claim | A factual assertion capable of being assessed against evidence. | verify an objective claim
universal claim | An assertion extending to every member of a stated group. | challenge a universal claim
testimonial | A statement describing a person's experience or view. | verify a testimonial
editorial fit | Compatibility with the content's purpose, tone, and audience. | assess editorial fit
brand safety | Avoiding specified harmful or unsuitable brand associations. | review brand-safety conditions
brand suitability | Compatibility with a particular brand's preferences and context. | define brand suitability
integration plan | The agreed arrangement for incorporating sponsored material. | revise the integration plan
sponsor deliverable | A specified item or exposure owed under the sponsorship agreement. | confirm sponsor deliverables
category exclusivity | A restriction on competing sponsors within a defined category. | check category exclusivity
makegood | Replacement value or exposure offered for a missed agreed delivery. | negotiate a makegood
approval chain | The sequence of authorized content or commercial reviews. | confirm the approval chain
script revision | A change to the wording of a production script. | submit the script revision
scope change | A change to the work or output originally agreed. | document the scope change
commercial break | A designated interval containing advertising. | schedule the commercial break
audience trust | The audience's confidence in the content's honesty and reliability. | protect audience trust''',
    precision='The new request adds fifteen seconds of mention time, bringing proposed mention time to twenty-five seconds. That arithmetic does not establish the final program length, cost, editorial acceptability, or approval of the new wording.',
    precision_extra='An endorsement disclosure must be clear in the actual viewing experience. A description-only disclosure may be missed. Disclosure also does not make an unsupported product claim true; claim review and relationship disclosure are separate tasks.',
    phrases='''Acknowledge the request | The sponsor wants a second fifteen-second mention.
State the existing agreement | The current plan approves one ten-second mention.
Quantify the change | The proposed mentions would total twenty-five seconds.
Keep the scope visible | This is an additional deliverable, not an already approved adjustment.
Separate the reviews | Timing, cost, editorial fit, claims, and disclosure all need review.
Challenge the wording | What evidence supports the claim that it works for everyone?
Avoid a universal promise | We cannot present that line as established without support.
Protect truthful experience | Do not script a personal experience the host has not actually had.
Keep disclosure in the content | The endorsement needs a clear disclosure in the video itself.
Reject an inadequate shortcut | A description-only disclosure can be missed.
Preserve review status | The revised script has not been approved.
Check the impact | Which content would the extra fifteen seconds displace?
Confirm the decision-makers | Route the revision through the agreed approval chain.
Keep the price conditional | We need to price the added work before promising it.
Separate clarity and persuasion | A visible sponsorship disclosure does not excuse an unsupported claim.
Close with a bounded offer | I can submit a revised proposal, but I cannot confirm the new integration today.''',
    notes='''Would total | Calculates the proposed combined mention time without treating it as approved.
Already approved | Distinguishes existing scope from a new request.
What evidence supports | Challenges the factual basis rather than the sponsor's personality.
In the video itself | Locates disclosure where the endorsement is encountered.
Can be missed | Explains why an available disclosure may still be inadequate.
Has not actually had | Preserves the truth of a host's claimed personal experience.''',
    d='''Which statement describes the time change accurately? | The proposed mentions total twenty-five seconds, fifteen more than approved. | The whole program must now be exactly twenty-five seconds long. | No time is added because the sponsor requested it. | The original ten-second mention automatically includes every later request. | Ten plus fifteen equals twenty-five seconds of mentions, not the entire program or an approved revision.
What does a clear disclosure not accomplish by itself? | It does not substantiate the universal product claim. | It identifies a relevant commercial relationship. | It helps viewers recognize sponsorship. | It can make the paid nature of content clearer. | Disclosure addresses the relationship, while a factual product claim still needs its own supporting evidence.
Which response respects both the relationship and the review? | We can assess the extra mention, but the wording, disclosure, cost, and timing need approval. | We will publish the sponsor's line unchanged without evidence. | We will hide the disclosure in the description to preserve the edit. | The host will claim an experience regardless of whether it occurred. | The bounded response offers a path forward without inventing approval or accepting an unsupported claim.
Which disclosure approach fits the stated video endorsement? | A clear disclosure within the video, reviewed in context | A clear description disclosure without an in-video disclosure | An in-video label made too brief to read so it does not interrupt the edit | A platform sponsorship setting assumed sufficient without checking the viewing experience | Viewers need to encounter an understandable disclosure with the endorsement, not merely in internal or easily missed material.''',
    rehearsal=['Read turns 1-10; separate the new scope request from the existing approval.', 'Swap roles for turns 11-20; distinguish clear disclosure from claim substantiation.', 'Complete the transfer and retain the difference between approved and proposed duration.'],
    dialogue='''Carmen | The sponsor wants another fifteen seconds after the agreed mention. They are calling it a small adjustment. Can we work out the actual impact before I answer?
Noel | Our [[integration plan::Integration plan defines the original sponsored arrangement; it currently includes one ten-second mention, not the proposed additional segment.]] includes one ten-second mention. The request would bring mention time to twenty-five seconds, so we need to assess what changes in the edit and the agreement.
Carmen | They describe it as a small adjustment, but I can see it may displace something.
Noel | It is a [[scope change::Scope change adds work or output beyond the existing agreement; the extra mention cannot be treated as already approved.]]. Let us review timing, cost, and editorial fit before promising it. The fact that the original mention is approved does not authorize the second one.
Carmen | Their suggested line is that the product works for everyone. They have not sent any evidence.
Noel | That [[universal claim::Universal claim extends the assertion to everyone, a breadth not supported by any evidence supplied in this scenario.]] cannot be presented as established on this record. We need supporting evidence and an appropriate claims review, not simply a more confident delivery by the host.
Carmen | Could the host say it is what they personally experienced instead?
Noel | Only if the [[testimonial::Testimonial represents an actual person's experience or view; changing the grammar must not invent an experience the host did not have.]] is truthful. We should not manufacture personal experience to make an unsupported general statement sound acceptable. The wording needs to reflect what can genuinely be said.
Carmen | The sponsor also asked to keep the sponsorship note in the description so that it does not interrupt the program.
Noel | The [[disclosure::Disclosure identifies the relevant commercial relationship; it needs to be clear in the video endorsement rather than solely in the description.]] needs to work in the video itself. Viewers may never open the description. We should assess how they actually encounter the endorsement, not just whether a note exists somewhere.
Carmen | We can explain that a readable disclosure belongs in the viewing experience, not in an optional extra page.
Noel | Yes, it must be [[clear and conspicuous::Clear and conspicuous means readily noticeable and understandable in context, not hidden, fleeting, or dependent on opening a description.]] in context. The final approach needs review with the actual video. A barely visible label or a platform setting should not be assumed sufficient on its own.
Carmen | If we fix the disclosure, the words works for everyone still need evidence, correct? I do not want the sponsor to think that one fix clears both issues.
Noel | Correct. [[Substantiation::Substantiation is the evidence supporting a factual claim; disclosing sponsorship does not supply that evidence.]] and disclosure address different questions. We need truthful content and a clear commercial relationship, not a choice between them.
Carmen | The extra segment may also feel repetitive after the host has already mentioned the product.
Noel | That is an [[editorial fit::Editorial fit assesses how the extra mention works with the program's purpose, tone, and audience rather than only its paid duration.]] question. We can evaluate placement and repetition, but the commercial request should not silently overrule the program's purpose or the audience's experience.
Carmen | I will send the sponsor a proposal showing the added work, the revised wording route, and the disclosure requirement.
Noel | Route it through the [[approval chain::Approval chain identifies the authorized reviews needed for the new script and commercial arrangement before commitment.]]. We still need the relevant decisions on the script, cost, timing, and integration. A proposal sent for review is not permission to publish.
Carmen | I can keep the response constructive: we will assess the request, but we cannot confirm the new segment today.
Noel | Exactly. That protects [[audience trust::Audience trust depends on truthful, identifiable commercial content; careful review supports both the production and the sponsor relationship.]] and gives the sponsor a usable next step. We can work toward an effective integration without disguising paid content or making a claim the evidence does not support.''',
    transfer_title='Clarify another integration request',
    transfer_setup='An approved plan contains one eight-second mention. A sponsor requests another twelve-second mention. The additional work and a new factual claim are unapproved; no supporting evidence is supplied.',
    transfer='''Account lead: "The approved mention is ___ seconds." | eight | Eight seconds is the existing approved mention, not the requested addition.
Producer: "The requested addition is ___ seconds." | twelve | Twelve seconds is the duration of the new, still-unapproved request.
Account lead: "The proposed mention time would total ___ seconds." | twenty | Eight approved seconds plus twelve requested seconds totals twenty proposed seconds.
Producer: "The new factual claim still needs ___." | substantiation | The briefing supplies no supporting evidence, so the claim requires substantiation rather than confident repetition.''',
))

BOOK['units'].append(unit(
    title='Crisis Response and Public Statements',
    scene='Confirm the production pause, not an unverified cause',
    skill='Prepare a concise holding statement that separates verified facts, open questions, and the next update.',
    brief='Filming at Studio C paused at 09:20 following a technical interruption. That pause and time are verified. The cause remains under investigation, injury reports are unverified, and no restart time is confirmed. A draft statement blames a contractor and says nobody was hurt; neither claim is supported. Communications manager Farah and executive producer Luis must remove those claims. They can state the verified pause, say the situation is being assessed, and commit to an update at 11:00. Only the designated spokesperson may release the approved statement under the local process.',
    cast='Farah | Communications manager\nLuis | Executive producer',
    culture=('Precision is not indifference', 'A careful holding statement can acknowledge concern without asserting a cause, injury status, or restart time that has not been verified. Avoid defensive certainty. Clear limits and a reliable next update are more credible than a complete-sounding explanation assembled from rumor.'),
    a='''Which fact is verified? | Filming at Studio C paused at 09:20. | A contractor caused the incident. | Nobody was hurt. | Filming will restart at 11:00. | The brief verifies the pause, location, and time while leaving cause, injury status, and restart unresolved.
Which claims must be removed from the draft? | Contractor blame and the unsupported no-injury claim | The verified pause time | The commitment to an 11:00 update | The fact that assessment is ongoing | Neither contractor responsibility nor absence of injury is supported by the supplied facts.
What does 11:00 represent? | The next public update | Guaranteed production restart | A confirmed medical finding | The time the cause becomes certain | Eleven o'clock is the communication commitment, not a guarantee of operational or investigative completion.''',
    vocabulary='''holding statement | A brief initial statement using verified information while further facts are checked. | prepare a holding statement
verified fact | Information confirmed through an adequate evidential basis. | separate verified facts
unverified report | Information received but not yet confirmed. | label an unverified report
source attribution | Identifying where information came from. | preserve source attribution
corroboration | Supporting confirmation from additional relevant evidence. | seek corroboration
incident timeline | A chronological record of relevant events. | establish the incident timeline
designated spokesperson | The person authorized to speak publicly for the organization. | brief the designated spokesperson
media inquiry | A request for information from a journalist or outlet. | log a media inquiry
public statement | An authorized communication intended for a public audience. | approve the public statement
on the record | Information provided for attributable publication under agreed ground rules. | clarify on-the-record terms
off the record | A source-use arrangement requiring explicit mutual understanding. | agree off-the-record terms
embargo | An agreed restriction on publication until a stated time or condition. | confirm the embargo
correction | A visible acknowledgment and repair of an error. | issue a correction
clarification | Additional explanation making an earlier statement clearer. | provide a clarification
speculation | An explanation or claim not established by the available evidence. | avoid speculation
causal claim | A statement asserting why an event occurred. | verify a causal claim
welfare update | Information about affected people's condition or support, within verified and authorized limits. | verify a welfare update
privacy boundary | A limit on sharing personal information. | respect privacy boundaries
operational pause | A temporary stop in activity. | confirm the operational pause
restart authorization | Permission to resume activity under the relevant process. | verify restart authorization
stakeholder briefing | An update to people with a relevant interest or responsibility. | coordinate a stakeholder briefing
message consistency | Agreement among communications on the verified facts and status. | maintain message consistency
approval version | The specific statement text cleared for release. | identify the approval version
update cadence | The planned rhythm or schedule of further communications. | establish an update cadence''',
    precision='Not confirmed is not the same as false, and unverified injury reports do not establish either injury or no injury. State the verification boundary instead of choosing the more reassuring conclusion.',
    precision_extra='An 11:00 update is not an 11:00 restart. If later evidence changes a published fact, correct it visibly through the authorized process. Calling a factual correction a clarification must not hide the original error.',
    phrases='''Lead with the verified event | Filming at Studio C paused at 09:20.
Describe the known context | The pause followed a technical interruption.
Limit the explanation | The cause has not yet been confirmed.
Remove unsupported blame | We do not have a verified basis for naming a responsible party.
Keep welfare information accurate | Injury reports have not yet been verified.
Avoid an unsupported reassurance | We cannot state that nobody was hurt on this record.
State the ongoing action | The situation is being assessed.
Commit to the next contact | We will provide an update at 11:00.
Separate time promises | That is an update time, not a confirmed restart.
Protect personal information | Release only verified and authorized personal details.
Name the release route | The designated spokesperson will issue the approved statement.
Preserve the evidence | Keep source and timestamp information with each factual claim.
Align internal messages | Brief the team on the same verified facts and open questions.
Handle a media question | I cannot confirm that explanation; we will update the verified position.
Correct an actual error | If published information is wrong, acknowledge and correct it visibly.
Close the draft review | Remove the unsupported claims and retain the factual pause and update commitment.''',
    notes='''Followed | Gives sequence or context without necessarily proving the underlying cause.
Not yet confirmed | States an evidential limit rather than denying the event or explanation.
On this record | Limits the conclusion to the available support.
Will provide an update | Commits to communication rather than a guaranteed resolution.
Verified and authorized | Requires both factual support and permission for disclosure.
Acknowledge and correct | Prevents a silent rewrite from concealing a published factual error.''',
    d='''Which holding statement fits the facts? | Filming at Studio C paused at 09:20 following a technical interruption. We are assessing the situation and will update at 11:00. | Contractor error caused the pause and nobody was hurt. | Filming restarts at 11:00 without further assessment. | Unverified reports prove the incident did not occur. | The supported statement uses the verified pause and timing while avoiding unsupported cause, injury, or restart claims.
What does unverified injury information justify saying? | Injury reports have not yet been verified. | Nobody was injured. | Every reported injury is confirmed. | Injury information is irrelevant to any later update. | Lack of verification supports only the stated uncertainty, not either a positive or negative injury finding.
Who may release the statement under the local process? | The designated spokesperson, using the approved version | The executive producer using the unsupported earlier draft | A department lead treating internal circulation as public approval | The communications writer before the text has completed review | The briefing assigns public release to the designated spokesperson and the approved text.
If a published factual claim proves wrong, what is appropriate? | Acknowledge and correct the error visibly through the authorized process. | Silently change it and deny any earlier error. | Keep repeating it to preserve consistency. | Call every factual error merely a stylistic preference. | Accurate correction must repair the record transparently rather than hide a substantive published error.''',
    rehearsal=['Read turns 1-10; keep verified events separate from cause and welfare reports.', 'Swap roles for turns 11-20; distinguish the update appointment from permission to restart.', 'Complete the transfer and read back the event time, update time, and spokesperson.'],
    dialogue='''Luis | Who supplied the contractor-error and no-injury lines? They are in the draft, but I cannot trace either one to a confirmed source.
Farah | Then neither belongs in the [[holding statement::Holding statement provides a brief verified update while open questions are checked; it must not invent a complete explanation.]]. We have confirmed that filming at Studio C paused at nine twenty following a technical interruption. The cause and injury reports are still being checked.
Luis | We should acknowledge concern without presenting the draft's explanation as fact.
Farah | Exactly. Separate each [[verified fact::Verified fact has adequate confirmation; here the pause, location, and time are established while other claims remain unresolved.]] from the open questions. We can say the situation is being assessed and that we will provide an update at eleven.
Luis | Someone on the crew says the contractor was working near the equipment. Does that justify naming them?
Farah | That is not enough for a [[causal claim::Causal claim explains why an event occurred; proximity to equipment does not establish responsibility for the interruption.]]. Being nearby does not establish responsibility. We need an adequate verified basis before asserting a cause or naming a party as responsible.
Luis | I have also seen social posts about injuries. We cannot confirm them yet.
Farah | Treat each as an [[unverified report::Unverified report is information not yet confirmed; it does not establish either an injury finding or the absence of injuries.]]. That does not mean the report is false, and it does not justify saying nobody was hurt. We must preserve the actual verification status.
Luis | We can ask the appropriate people for confirmed information without releasing private details in the meantime.
Farah | Yes. A [[welfare update::Welfare update concerns affected people and must use verified information within the relevant authorization and privacy limits.]] needs both accuracy and the proper disclosure basis. Concern for people should not become a reason to circulate names or conditions we are not authorized to share.
Luis | Please make the eleven-o'clock line explicitly an update. I do not want crews or reporters reading it as a restart time.
Farah | Then distinguish it from [[restart authorization::Restart authorization permits resuming activity; the scheduled public update does not supply that permission or a restart time.]]. Eleven is the next communication time. We do not have a confirmed restart time, and the statement must not imply one.
Luis | Who should send the public version? Several department leads are receiving media questions.
Farah | The [[designated spokesperson::Designated spokesperson is the person authorized under this local process to release the approved public statement.]] will issue the approved text. We should brief the department leads on the same facts and route inquiries through the agreed process rather than improvise separate explanations.
Luis | Let us also keep track of when each fact was confirmed and by whom.
Farah | Maintain the [[incident timeline::Incident timeline orders relevant events and their support, helping the team distinguish verified times from rumors and later interpretations.]] with source information. That will help us update accurately as evidence develops and avoid confusing the time of a report with the time of the event.
Luis | If something we publish later proves wrong, we should not just quietly replace the text.
Farah | Correct. Issue a visible [[correction::Correction acknowledges and repairs a factual error; a silent replacement would conceal the earlier incorrect public claim.]] through the authorized process. A clarification can explain wording, but it should not be used to disguise a substantive error in what we said.
Luis | I will remove the blame and no-injury sentence. The remaining statement will give the pause, ongoing assessment, and eleven-o'clock update.
Farah | I will identify that [[approval version::Approval version is the specific text cleared for release, preventing an obsolete or unsupported draft from becoming the public statement.]] for review and release. The public should receive the verified position, not the most reassuring draft. We can be clear, humane, and precise while questions remain open.''',
    transfer_title='Prepare a second factual update',
    transfer_setup='Recording at Studio D paused at 15:10. The cause and restart time are unconfirmed. The next approved status update is 16:00, to be delivered by spokesperson Rina.',
    transfer='''Producer: "The confirmed pause time is ___." | 15:10 | Fifteen ten is the verified event time, distinct from the later communication appointment.
Communications lead: "The cause remains ___." | unconfirmed | The briefing supplies no established cause, so an explanation must not be invented.
Producer: "The next status update is at ___." | 16:00 | Sixteen hundred is the planned update, not a promised restart.
Communications lead: "The designated spokesperson is ___." | Rina | Rina is the named person responsible for delivering the approved update.''',
))
