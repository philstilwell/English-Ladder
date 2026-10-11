"""Original Childcare and Early Education learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='childcare-early-education',
    title='Childcare and Early Education English',
    cover_label='ENGLISH FOR EARLY-YEARS TEAMS',
    cover_title='Childcare and\nEarly Education',
    cover_size=32,
    tagline='Warm communication. Clear care.',
    audience='For early-years educators, nursery staff, preschool assistants, and childcare teams working with children and families.',
    map_intro='Eight early-years cases: arrivals, shared play, transitions, peer disagreements, learning observations, inclusive participation, health plans, and collection checks.',
    notes_title='Be specific, warm, and fair.',
    notes_intro='Early-years communication moves between brief child-facing phrases and detailed discussions with families and colleagues. Describe what happened, offer genuine choices, preserve the child perspective, and keep important care arrangements clear.',
    field_notes=[
        ('Describe before interpreting', 'A recorded action and a guessed motive are different. Name what you saw and heard without turning one moment into a fixed label for the child or a comparison unsupported by evidence.', '"Eli sorted four buttons by color and said, These go together."'),
        ('Make a choice real', 'Offer options that are genuinely available within the current plan. A choice between two ways to finish a transition is not permission to keep playing indefinitely. Keep the boundary calm and predictable.', '"You can place the last block or ask for a permitted photograph before story time."'),
        ('Recognize more than one way to join in', 'A child may participate through pointing, gesture, or speech when the activity and plan allow it. Describe the response accurately rather than treating silence as absence or claiming every format supplies identical evidence.', '"Noor selected a picture by pointing; no spoken answer was recorded."'),
        ('Name the responsible next step', 'A health-plan query or unverified collection arrangement needs an appropriate owner and the real center procedure. Respectful communication does not require improvising a safety decision or accusing a person without evidence.', '"Rosa is checking the collection arrangement; authority is not yet verified."'),
    ],
    scope_note='All children, families, centers, and cases are fictional. This book teaches workplace English, not childcare licensing, clinical advice, developmental diagnosis, or safeguarding certification. Follow current local law, supervision requirements, individual plans, and center procedures. Do not delay urgent safeguarding or emergency action for a routine query. Materials and activities require age-appropriate risk assessment. England and US sources provide distinct contexts, not interchangeable legal rules.',
    sources=[
        dict(title='Department for Education. Early Years Foundation Stage Statutory Framework.',
             url='https://www.gov.uk/government/publications/early-years-foundation-stage-framework--2',
             note='England framework updated September 2026. Context for family communication, health information, confidentiality, and collection procedures; not a universal legal code.', checked='10 October 2026'),
        dict(title="NAEYC. Observing, Documenting, and Assessing Children's Development and Learning.",
             url='https://www.naeyc.org/node/3811',
             note='Professional context for responsive observation and appropriate use of assessment evidence. Original cases do not establish developmental diagnoses or rankings.', checked='10 October 2026'),
        dict(title='Office of Head Start. Home Language Support.',
             url='https://headstart.gov/culture-language/article/home-language-support',
             note='Developmental background on supporting home languages alongside English. The fictional participation plan is specific to the child and activity.', checked='10 October 2026'),
        dict(title='Rosanbalm and Murray. Co-Regulation From Birth Through Young Adulthood: A Practice Brief.',
             url='https://fpg.unc.edu/sites/fpg.unc.edu/files/resources/reports-and-policy-briefs/Co-RegulationFromBirthThroughYoungAdulthood.pdf',
             note='Research-to-practice context for supportive relationships, predictable environments, and coaching. The original peer scenarios are language practice, not behavior-treatment protocols.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Arrivals and family partnerships',
    scene='Agreeing on the goodbye',
    skill="Clarify conflicting arrival expectations with a parent while keeping the child's needs and responsible educator visible.",
    brief='It is Mina\'s third morning at the center. Parent Daniel expected to stay for ten minutes, but the arrival note says a brief goodbye. Key educator Rosa is present and can clarify the settling-in plan with Daniel. Mina has a familiar cloth; using it must follow the center arrangements. No fixed departure time or guaranteed emotional response is established. Rosa must acknowledge the difference, avoid blaming Daniel or labeling Mina as difficult, and clarify the plan before giving inconsistent directions.',
    cast='Daniel | Mina\'s parent\nRosa | Key educator',
    culture=('A partnership starts with listening', 'Parents and staff may attach different meanings to a brief goodbye. Acknowledge the expectation without promising an arrangement before it is clarified. The child should hear calm, consistent language rather than adults correcting one another sharply at the door.'),
    a='''What did Daniel expect? | To stay for ten minutes | To leave without speaking to anyone | A guaranteed distress-free arrival | A new collection arrangement | Daniel expected ten minutes, while the arrival note describes a brief goodbye.
Who can clarify the plan? | Rosa, Mina's key educator | Another parent without responsibility | Mina alone | An invented policy unrelated to the center | Rosa is present and identified as the educator who can clarify the settling-in plan.
What is not established? | A fixed departure time and guaranteed emotional response | That it is Mina's third morning | That Mina has a familiar cloth | That the arrival note says brief goodbye | The case supplies conflicting expectations but not a completed agreement or guaranteed reaction.''',
    vocabulary='''settling-in plan | Agreed approach helping a child become familiar with a setting and its people. | clarify the settling-in plan
key educator | Staff member with particular responsibility for supporting a child and family. | speak with the key educator
arrival routine | Usual sequence when a child enters the setting. | establish an arrival routine
family partnership | Working relationship in which families and educators share relevant knowledge. | build a family partnership
handover | Transfer of relevant information and care responsibility between people. | complete the morning handover
brief goodbye | Short departure exchange whose practical meaning needs agreement. | agree on a brief goodbye
familiar object | Known item that may offer continuity or comfort within permitted arrangements. | discuss a familiar object
comfort item | Object associated with reassurance, used under appropriate safety arrangements. | check comfort-item arrangements
separation | Period or event in which a child and familiar caregiver are apart. | support separation
reassurance | Supportive communication intended to reduce uncertainty or concern. | offer realistic reassurance
attachment | Enduring emotional connection with a familiar caregiver or other significant person. | support attachment relationships
responsive care | Care that notices and responds appropriately to the child's cues. | provide responsive care
child cue | Observable signal of a child's interest, need, or emotional state. | notice a child cue
predictability | Quality of an arrangement being understandable and reasonably consistent. | build predictability
consistency | Alignment of actions or messages across people or occasions. | maintain consistency
parent expectation | What a parent believes will happen in the arrangement. | clarify the parent expectation
arrival note | Recorded information about the child's arrival or agreed approach. | review the arrival note
agreed wording | Language adults have decided to use consistently. | use agreed wording
transition support | Help with moving between people, settings, or activities. | provide transition support
emotional response | Feelings or reactions expressed in a situation. | observe the emotional response
individual need | Requirement specific to a particular child rather than an assumed group norm. | respond to individual needs
update arrangement | Agreed method or time for sharing later information. | clarify the update arrangement
contact preference | Preferred communication method where appropriate and authorized. | confirm contact preferences
shared understanding | Agreement about what a plan or message means. | establish shared understanding''',
    precision='Brief is not a universal number of minutes. Here it conflicts with Daniel expecting ten minutes, so the plan needs clarification. Do not convert either source into a finalized agreement before Rosa and Daniel resolve the practical meaning.',
    precision_extra='A familiar cloth may support continuity, but its use depends on actual safety and center arrangements. Do not present a comfort item as automatically suitable for every age, activity, or sleep setting, and do not promise it will prevent distress.',
    phrases='''Acknowledge the expectation | You expected to stay for ten minutes.
Read the note neutrally | The arrival note says a brief goodbye.
Name the difference | Those expectations need to be clarified together.
Identify the responsible adult | I am Mina's key educator, and we can clarify the plan.
Keep the child central | Let us keep our messages to Mina calm and consistent.
Avoid blame | We do not need to decide who is at fault to clarify this.
Reject a guarantee gently | I cannot promise exactly how Mina will respond.
Notice the familiar item | Mina has brought her familiar cloth.
Check the arrangement | Its use needs to follow our center arrangements.
Do not invent a deadline | We have not yet agreed on a departure time here.
Invite useful information | Please tell me what you expected the goodbye to involve.
Preserve the plan | We should record the clarified arrangement through our process.
Keep support concrete | Mina needs to know which adult is receiving her.
Avoid a fixed label | One arrival does not define Mina as a difficult child.
Clarify later contact | Any update arrangement should be agreed rather than assumed.
Close together | Let us confirm the plan and use the same message with Mina.''',
    notes='''You expected | Recognizes the parent's understanding without declaring it the final plan.
The note says | Attributes the other message rather than using it as an accusation.
Together | Frames clarification as cooperation instead of correction of the parent.
Exactly how | Limits promises about the child's feelings.
Not yet agreed | Prevents a possible arrangement from becoming a confirmed instruction.
Same message | Connects adult coordination with the child's experience.''',
    d='''Which opening is most useful? | You expected ten minutes; the note says brief goodbye. Let us clarify the plan together. | You are making Mina difficult by staying. | Ten minutes is mandatory in every center. | A brief goodbye guarantees no tears. | The opening preserves both sources and invites a practical agreement without blame or a false guarantee.
What should be said about the cloth? | Its use follows the center's actual arrangements. | Approval during arrival automatically extends to sleep. | A parent's usual home practice replaces the center's safety checks. | Keeping it nearby confirms Mina will not become upset. | Arrival comfort, sleep safety, and the child's response are separate questions; familiarity does not settle all three.
Why should adults coordinate their wording? | To give Mina a calm, consistent message about the clarified plan | To hide the parent expectation | To avoid ever recording a change | To make the child choose which adult is right | Consistent communication supports a clearer transition without making the child resolve an adult disagreement.
Which statement overreaches? | Mina will definitely be calm as soon as Daniel leaves. | It is Mina's third morning. | Rosa is present. | The departure time is not yet agreed here. | The facts do not establish or guarantee Mina's future emotional response.''',
    dialogue='''Daniel | Rosa, I thought I could stay for ten minutes this morning, but the note says a brief goodbye. I do not want Mina hearing two different instructions.
Rosa | Thank you for raising that. We need to clarify the [[settling-in plan::The settling-in plan is the arrangement being clarified, not a universal rule that automatically resolves the two different expectations.]] together. The note and your expectation do not yet give us one agreed approach.
Daniel | It is only her third morning, and I had prepared her for me staying a little while. I am worried about changing the message at the door.
Rosa | I am her [[key educator::The key educator is Rosa, the present staff member identified to clarify the plan with Daniel and support Mina.]], so let us work through the difference calmly. We should not make Mina choose between what you expected and what the note appears to say.
Daniel | When staff say brief, do they mean a particular number of minutes? I cannot tell whether ten minutes fits that word or contradicts it.
Rosa | A [[brief goodbye::A brief goodbye needs a shared practical meaning here; the word alone does not specify a universal number of minutes.]] needs a clear meaning in our arrangement. I should not treat that word as though we have already agreed on an exact departure time.
Daniel | Yesterday I was told not to rush. This morning the note sounds different. I need to know what to do, and Mina is listening to us.
Rosa | This is about [[family partnership::Family partnership treats Daniel's information as part of the clarification rather than assigning blame for an unresolved arrival arrangement.]], not blame. We can acknowledge what you understood and clarify the plan without labeling your choice as the cause of a reaction we have not observed.
Daniel | She has brought her familiar cloth. It helps her recognize something from home, but I do not know the center arrangements for using it.
Rosa | We should check the [[comfort item::The comfort item is the familiar cloth; its use depends on actual center and safety arrangements, not an automatic permission for every situation.]] arrangements. Its familiarity is useful information, but I will not assume it can be used in every activity or setting.
Daniel | Could you promise that she will be settled after I leave? I know that may be difficult to answer, but it would make leaving easier.
Rosa | I can offer honest support, not a guaranteed [[emotional response::An emotional response cannot be promised in advance; Rosa can support Mina without guaranteeing a specific reaction to separation.]]. We will need to notice how Mina responds and follow the agreed approach rather than promise a particular feeling.
Daniel | Could you be the person she comes to after our goodbye? She knows you now, and I would like to tell her who will be with her.
Rosa | Agreed. A consistent [[arrival routine::The arrival routine is the understandable sequence adults clarify for Mina, not a promise that every morning will feel identical.]] should make the next step understandable. Let us clarify the practical handover and use the same message with her.
Daniel | Will tomorrow's staff see what we agree? I do not want to prepare Mina for one routine and be given a different instruction when we arrive.
Rosa | Yes. We should preserve the [[shared understanding::Shared understanding means the practical agreement is clear to the adults, rather than relying on the unresolved word brief.]] through our process. A clear record will help colleagues continue the arrangement without inventing a new version.
Daniel | And how will I hear how she gets on? I keep checking my phone, but I do not know when I should expect an update.
Rosa | We can clarify the [[update arrangement::An update arrangement specifies actual later communication; it must be agreed rather than assumed or offered as an unsupported timing guarantee.]] as part of the conversation. We should say what contact is genuinely agreed rather than leave you waiting for an assumed promise.
Daniel | Thank you. My main concern is that Mina gets one calm message and that I understand the plan before being told to leave.
Rosa | That is why [[consistency::Consistency aligns the adults' messages after clarification, helping Mina receive one coherent plan without an invented departure deadline.]] matters here. Let us resolve the expectation, confirm the handover, and keep the message to Mina clear and respectful.''',
    rehearsal=["Read Daniel and Rosa's checked dialogue. Contrast expected ten minutes with the note's brief goodbye without blaming the parent.","Switch roles. Repeat the handover and update questions, keeping every unconfirmed arrangement conditional.","Complete the five-minute/immediate-handover transfer, check the key, then read it without inventing a revised agreement."],
    transfer_title='Clarify another arrival mismatch',
    transfer_setup='Parent Ellis expects a five-minute stay. The note says immediate handover. Key educator Noor is present. No revised agreement has been made.',
    transfer='''Ellis: "I expected a ___ stay." | five-minute | The parent expectation is a five-minute stay, not an agreed revision.
Noor: "The note says ___." | immediate handover | Immediate handover is the wording in the existing note.
Ellis: "The key educator available is ___." | Noor | Noor is the present educator identified to clarify the arrangement.
Noor: "The revised agreement is not yet ___." | confirmed | No revised arrangement has been agreed in the supplied facts.''',
))

BOOK['units'].append(unit(
    title='Play-based learning and useful prompts',
    scene='Two bridge ideas',
    skill='Use neutral prompts and comparative language to support shared investigation without choosing a winner for the children.',
    brief='During fictional block play, Eva and Jo each want their bridge design used. Eva wants a wider bridge; Jo wants a taller opening underneath. Educators Maya and Ben discuss language that will invite both explanations and support trying two designs with the available blocks. No winner has been chosen, and no test outcome is supplied. The task is to model useful child-facing phrases inside an adult planning conversation. A prompt should leave room for the child idea without quietly supplying the answer or making the activity a competition.',
    cast='Maya | Early-years educator\nBen | Colleague supporting block play',
    culture=('Curiosity can be precise', 'An educator can give language support without taking ownership of the design. Name width and height clearly, allow both ideas to be expressed, and avoid praise that makes one child the winner before the structures have been explored.'),
    a='''What does Eva want? | A wider bridge | A taller opening as her only stated aim | A chosen winner | A completed adult design | Eva's stated priority is the width of the bridge.
What does Jo want? | A taller opening underneath | Removal of all blocks | A fixed winning score | A guaranteed wider deck | Jo's stated priority is the height of the opening underneath.
What can the educators suggest? | Try two designs using the available blocks. | Declare Eva the winner immediately. | Claim both tests have already succeeded. | Supply unavailable materials as though they are present. | The brief allows two designs with available blocks but supplies no winner or outcome.''',
    vocabulary='''play-based learning | Learning developed through purposeful opportunities for play and exploration. | support play-based learning
child-led idea | Proposal originating with the child rather than prescribed by an adult. | follow a child-led idea
adult scaffolding | Temporary support that helps a learner do more while retaining meaningful participation. | provide adult scaffolding
open prompt | Invitation allowing a range of relevant responses rather than supplying one answer. | use an open prompt
leading question | Question that steers the listener toward an implied preferred answer. | avoid a leading question
wait time | Deliberate pause allowing a child time to process and respond. | allow wait time
sustained shared thinking | Extended joint exploration of an idea or problem through interaction. | support sustained shared thinking
modeling | Demonstrating language or action that can support learning. | use language modeling
recasting | Restating a child's message with an adjusted grammatical form while preserving the intended meaning. | use a gentle recast
expansion | Adding useful language to a child's expressed idea while preserving its meaning. | offer a language expansion
comparative language | Words used to describe relative qualities such as wider or taller. | model comparative language
spatial language | Words describing position, direction, distance, or arrangement. | introduce spatial language
width | Measurement across an object from side to side. | compare bridge width
height | Vertical measurement from a defined lower point to a higher point. | compare opening height
span | Distance bridged between supports. | compare the span
support | Part holding up or stabilizing a structure. | position the supports
stability | Ability of a structure to remain in position under relevant conditions. | explore stability
clearance | Space available between an object and a surrounding or overhead surface. | check the clearance
design intention | What the maker wants a design to do or achieve. | clarify the design intention
prediction | Statement about what someone expects to happen before trying it. | make a prediction
trial | Attempt used to explore how something works. | compare two trials
revision | Change made to a design or idea after further thinking or testing. | revise the design
collaborative play | Play involving coordination or shared activity with others. | support collaborative play
specific feedback | Response naming an observed action or feature rather than general praise alone. | give specific feedback''',
    precision='Wider and taller refer to different dimensions. A bridge can be wide without having a tall opening. Preserve each child design intention before suggesting a comparison, and do not change taller into better or wider into stronger without evidence.',
    precision_extra='An open prompt invites the child idea; a leading question suggests the adult answer. Comparing structures is different from ranking children. Useful feedback names an observed feature, while a prediction remains an expectation until the relevant trial has occurred.',
    phrases='''Invite Eva's idea | Eva, show us what you mean by a wider bridge.
Invite Jo's idea | Jo, show us where you want the taller opening.
Name both priorities | Eva is exploring width, and Jo is exploring opening height.
Avoid a winner | We have two ideas to try, not a winner already chosen.
Offer a feasible trial | We can try two designs with these available blocks.
Model comparison | This opening is taller; this bridge is wider.
Ask without supplying | What do you want this part of the bridge to do?
Allow processing | I will pause so each child has time to respond.
Preserve the idea | I can expand the language without replacing the child's intention.
Separate prediction and result | That is what you expect; now we can see what happens.
Give specific feedback | You moved the supports farther apart.
Use spatial language | The opening is underneath the bridge.
Keep the activity shared | Let us hear both explanations before choosing what to try.
Avoid an unsupported claim | A wider design is not automatically the stronger one.
Invite a revision | You can change the design after seeing what happens.
Close with exploration | We can compare the two designs without ranking the children.''',
    notes='''Show us what you mean | Allows gesture and demonstration alongside words.
Where | Directs attention to the relevant part without prescribing the design.
Two ideas to try | Frames the activity as exploration rather than a contest.
What do you want | Keeps the intention with the child.
Expect versus happens | Separates prediction from observation.
Ranking the children | Distinguishes comparing structures from labeling children's ability.''',
    d='''Which prompt preserves Jo's idea? | Show us where you want the taller opening. | You really mean a wider bridge, do you not? | Eva's idea is better, so copy it. | A tall opening always wins. | The prompt preserves opening height as Jo's priority without supplying a design or ranking.
Which sentence is a leading question? | Wouldn't it be better to use my wider design? | What do you want this part to do? | Show us where the opening would be. | Which feature are you describing? | The question embeds the adult preferred answer instead of inviting the child's own explanation.
Which comparison is factual in principle? | This bridge is wider, while that opening is taller. | The child with the taller design is more intelligent. | The wider bridge is always strongest. | Both designs have already passed every test. | Width and opening height can be described separately without ranking children or inventing results.
What is the proposed next action? | Try two designs using available blocks. | Announce a winner before exploration. | Promise that neither structure can fall. | Require a material that is not available. | The stated opportunity is a feasible comparison, not a guaranteed result or predetermined competition.''',
    dialogue='''Ben | Eva and Jo both want their bridge idea used. Eva wants it wider, while Jo keeps showing me a taller opening underneath. I am tempted to choose one.
Maya | Let us clarify each [[design intention::Design intention identifies what each child wants the structure to achieve, so the two different priorities can be heard before choosing a trial.]] first. We can ask Eva to show the width and Jo to show the opening, without deciding whose idea is better.
Ben | I could say, "Eva, show us what you mean by wider." That lets her point or demonstrate rather than requiring a long explanation.
Maya | Yes. That is an [[open prompt::An open prompt invites Eva's meaning through words or demonstration instead of supplying the adult's preferred design.]]. It supports her idea without putting our answer into her mouth or turning the exchange into a vocabulary test.
Ben | For Jo, I could ask where the opening should be taller. I should not translate his request into another version of Eva's idea.
Maya | Exactly. Use [[spatial language::Spatial language identifies the opening underneath the bridge and helps preserve the location relevant to Jo's proposal.]] such as underneath while keeping the idea his. Height of an opening and width of a bridge are different features.
Ben | I caught myself saying, "Wouldn't a wider bridge be better?" That was really my idea in question form. I need to give Jo's opening a fair hearing too.
Maya | That is a [[leading question::A leading question contains an implied preferred answer, here favoring the wider design before the children's ideas are explored.]]. It could make Jo feel that the decision is already made. We can invite explanations without hinting which child should agree with us.
Ben | We have blocks available for trying two designs. I could suggest that practical option instead of making the children compete for one approved plan.
Maya | A second [[trial::A trial is an attempt to explore a design; proposing two trials does not establish either outcome or a winner.]] gives us something to compare. We should not announce the result in advance or promise that a particular structure will work.
Ben | I keep saying good job, but it does not give them much to work with. What could I say about the supports they are moving?
Maya | Offer [[specific feedback::Specific feedback names an observed action or feature, giving useful language without replacing the child's idea with general praise or ranking.]] such as, "You moved the supports farther apart." That names an action and leaves room for the child to explain what they intended.
Ben | I can also model wider and taller while pointing to the appropriate dimension. I should not use taller as another word for better.
Maya | Right. [[Comparative language::Comparative language describes relative qualities such as width and height, not an automatic judgment that one child or design is better.]] helps describe the structures. It should not quietly become a ranking of the children or an unsupported claim about strength.
Ben | If Eva says, "More space here," I might say, "You want more space across the bridge," while checking that I have kept her meaning.
Maya | That is a useful [[expansion::Expansion adds language to the child's expressed meaning while preserving the intention rather than substituting an adult idea.]]. We are adding language around her idea, not correcting her into a different design or requiring her to repeat our exact sentence.
Ben | I tend to fill the silence. Eva may be about to point when I jump in with another question. I will try leaving that space.
Maya | Allow [[wait time::Wait time leaves room for processing and response; answering immediately for the children would remove that opportunity.]]. Watch their responses, including gestures, and keep the exploration moving at a pace that allows both to participate.
Ben | Then our plan is to hear both intentions, offer two available-block trials, and describe what happens without choosing a winner beforehand.
Maya | Yes. That supports [[collaborative play::Collaborative play involves shared exploration and coordination, which the two-design comparison supports without a predetermined winner.]]. We can compare features, invite a later revision, and keep the children's ideas at the center of the conversation.''',
    rehearsal=["Read Maya and Ben's corrected dialogue. Use your voice to distinguish a wider bridge from a taller opening.","Switch roles. Read the exact child-facing prompts, pausing after each prompt instead of supplying a child's answer.","Complete the tower comparison, check the key, then read it aloud without changing wider, taller, or the two proposed trials."],
    transfer_title='Compare two tower intentions',
    transfer_setup='Ari wants a wider tower base. Bea wants a taller tower. Available blocks allow two trials. No winner or result is established.',
    transfer='''Educator: "Ari wants a ___ base." | wider | Ari's stated intention concerns the width of the base.
Colleague: "Bea wants a ___ tower." | taller | Bea's stated intention concerns the height of the tower.
Educator: "We can offer two ___." | trials | The available blocks allow two exploratory trials of the ideas.
Colleague: "No ___ has been chosen." | winner | The facts do not establish a winner before exploration.''',
))

BOOK['units'].append(unit(
    title='Daily routines and supported transitions',
    scene='Five minutes to story time',
    skill='Offer bounded choices and a predictable next step without turning a transition into an open-ended negotiation.',
    brief='Luca is building when the room will move to story time in five minutes. The current center arrangement allows the structure to remain on the marked shelf. Luca can choose to place the last block or ask the educator for a photograph using the center permitted practice. Educators Nora and Ben discuss how to explain these options. They cannot extend play indefinitely, promise a return time that is not supplied, or use a personal device outside the approved photography arrangements. The choices concern how to finish, not whether story time happens.',
    cast='Nora | Early-years educator\nBen | Colleague coordinating the transition',
    culture=('A boundary and a choice can coexist', 'A genuine choice can help a child finish an activity without removing the next routine. State the shared boundary first, then offer the available options in simple language. Avoid asking a yes-or-no question when no is not an available outcome.'),
    a='''Which timing statement is supplied by the arrangement? | Story time begins in five minutes. | Building resumes immediately after the story. | Luca has five minutes after the group starts story time. | The photograph postpones the group transition. | Five minutes is the warning before story time, not a return promise or an extension triggered by the finishing choice.
What can remain on the marked shelf? | Luca's structure under the current arrangement | Every object permanently | An unapproved personal camera | A guaranteed future activity slot | The current arrangement specifically permits the structure to remain on the marked shelf.
What do the two choices concern? | How Luca finishes before the transition | Whether the room ever moves to story time | A new permanent center rule | Unlimited building time | The last block or permitted photograph supports finishing within the existing boundary.''',
    vocabulary='''transition | Move from one activity, place, or part of the day to another. | support a transition
advance warning | Notice given before an expected change. | give advance warning
transition cue | Signal indicating an approaching or current change of activity. | use a transition cue
visual schedule | Sequence of activities represented through pictures or other visual supports. | refer to the visual schedule
first-then language | Wording that makes a short sequence of actions explicit. | use first-then language
bounded choice | Choice among genuinely available options within a clear limit. | offer a bounded choice
predictable routine | Repeated sequence that helps people anticipate what comes next. | maintain a predictable routine
finishing point | Defined place at which an activity pauses or ends. | identify a finishing point
last step | Final action before moving to the next part of a routine. | name the last step
preserved work | Work kept rather than dismantled or discarded immediately. | protect preserved work
marked shelf | Clearly identified storage or display location. | use the marked shelf
photography permission | Applicable consent and authority for taking or using images. | verify photography permission
approved device | Equipment permitted under the organization's actual arrangements. | use an approved device
image storage | Process and location for keeping photographs or other images. | follow image-storage rules
return expectation | Belief about when a person can resume an activity. | clarify the return expectation
cleanup routine | Agreed process for putting away or arranging materials. | follow the cleanup routine
group movement | Coordinated move of children between places or activities. | support group movement
supervision continuity | Maintaining appropriate adult oversight throughout a change. | preserve supervision continuity
processing time | Time needed to understand and respond to information. | allow processing time
follow-through | Carrying out an agreed action or stated boundary. | provide calm follow-through
negotiable detail | Aspect of a plan that can genuinely be chosen or changed. | identify the negotiable detail
nonnegotiable boundary | Limit that is not offered as a choice in the current arrangement. | state the nonnegotiable boundary
rushed instruction | Direction given too quickly or late for an effective response. | avoid a rushed instruction
consistent cue | Signal used in an aligned way across adults or occasions. | agree on a consistent cue''',
    precision='You can choose the last block or a permitted photograph offers two available ways to finish. Do you want story time? suggests that declining the transition is allowed. Match the grammar of the choice to the actual options.',
    precision_extra='Preserving the structure does not establish when Luca will return to it. A photograph also requires the actual permission, device, storage, and privacy arrangements. Do not treat a useful transition idea as authorization to use a personal phone.',
    phrases='''Give advance notice | Story time begins in five minutes.
Name the boundary | We will move to story time after this finishing step.
Offer the two choices | You can add the last block, or I can take a photo using our center's camera.
Show the storage place | Your structure can stay on the marked shelf.
Keep the choice genuine | Both options are available under our current arrangement.
Avoid an open-ended promise | I cannot promise unlimited building time.
Use a short sequence | First we finish this step; then we move to story time.
Preserve the work | We do not need to dismantle the structure for this transition.
Clarify the photo condition | Any photograph must follow the center's permitted practice.
Avoid a false return time | We have not agreed on when the building will resume.
Allow a response | I will give Luca time to understand the two choices.
Keep adult cues aligned | Let us use the same transition message.
Do not make the child choose safety | Supervision remains our responsibility.
Respect the effort | You have been working on this structure.
Follow through calmly | The finishing choice does not change the move to story time.
Close the sequence | The work stays on the marked shelf, and the group moves to the story.''',
    notes='''In five minutes | Provides a concrete warning tied to the supplied routine.
Last block or photograph | Gives a limited, real choice rather than an indefinite negotiation.
First, then | Makes the action sequence understandable.
Can stay | Refers to the current permission without promising permanent preservation.
Any photograph must | Keeps a useful option inside actual privacy arrangements.
Does not change | Maintains the boundary without withdrawing the finishing choices.''',
    d='''Which child-facing message matches the arrangement? | Story time is in five minutes; choose the last block or a permitted photograph before we move. | Do you want to go to story time at all? | Build for as long as you like. | I guarantee you can return at a specific time not provided here. | The message combines the supplied warning, available finishing choices, and actual transition boundary.
Which statement about the structure is supported? | It can remain on the marked shelf under the current arrangement. | It must be destroyed immediately. | It will remain forever. | It can block any walkway. | The brief permits the marked shelf but does not create unlimited storage or safety permission.
Which photography action is inappropriate? | Use an unapproved personal phone because the picture would help. | Follow the center's permitted practice. | Check the applicable arrangements. | Keep the option conditional on permission. | A transition benefit does not authorize an unapproved device or override image-handling requirements.
What should remain with the adults? | Responsibility for supervision during the transition | A child's duty to supervise the group alone | A promise that every child will feel the same | Permission to abandon the routine without explanation | Giving choices does not transfer supervision responsibility from staff to the child.''',
    dialogue='''Ben | Luca is still building, and story time starts in five minutes. I want to help him finish without telling him the whole structure has to come down.
Nora | Start with [[advance warning::Advance warning tells Luca about the five-minute change before it occurs, supporting preparation rather than a sudden instruction.]]: "Story time begins in five minutes." Then explain that the current arrangement allows his structure to stay on the marked shelf.
Ben | That could help. He has put effort into it, so moving on does not need to sound as though the work is being thrown away.
Nora | Exactly. Name the [[preserved work::Preserved work means the structure can remain under the current arrangement; it does not imply unlimited play or a promised return time.]] and show where it will stay. We can respect the effort while keeping the transition clear.
Ben | I can say, "You can add the last block, or I can take a photo using our center's camera." I will check our photo arrangements first.
Nora | That is a [[bounded choice::A bounded choice offers two genuinely available ways to finish while the move to story time remains fixed.]]. Both options concern how to finish. Neither means the group waits indefinitely or that story time becomes optional.
Ben | I should avoid saying, "Do you want to go to story time?" if I am not actually offering the possibility of staying here instead.
Nora | Right. State the [[nonnegotiable boundary::The nonnegotiable boundary is the move to story time, distinct from Luca's available choice of a finishing action.]] calmly, then offer the finishing choices. The question should not imply an option that disappears as soon as he chooses it.
Ben | I could say, "First the last step, then story time." That gives him a short sequence rather than several instructions in one breath.
Nora | Use that [[first-then language::First-then language makes the sequence explicit: the finishing step precedes the move to the next activity.]] with the actual options. It helps us keep the sequence clear without promising extra building time beyond the arrangement.
Ben | The photo option needs a clear handoff between us. I do not want someone taking out a personal phone while we are moving the children.
Nora | The option still requires [[photography permission::Photography permission and the center's actual arrangements govern the image; a helpful transition idea does not authorize any device or use.]] and the permitted device and storage practice. We should not treat the child-facing choice as permission to bypass those arrangements.
Ben | I will also avoid promising that Luca can return immediately after the story. We have permission to preserve the structure, not a supplied return slot.
Nora | Correct. Keep the [[return expectation::The return expectation must not include an invented time; preserving the structure does not establish when building will resume.]] accurate. We can explain what stays without inventing when the next building opportunity will happen.
Ben | If he is still looking at the tower, I will pause and keep the choices the same. Repeating them faster is not helping him finish.
Nora | Allow [[processing time::Processing time lets Luca understand and respond to the available choices rather than face a changing or rushed instruction.]]. The wording can stay short and consistent, with the same boundary instead of a new offer every few seconds.
Ben | During the move, we still need to keep the group appropriately supervised. Offering Luca a choice does not make him responsible for everyone else.
Nora | Yes. [[Supervision continuity::Supervision continuity keeps appropriate adult oversight in place through the transition; the child does not assume that responsibility.]] stays with us. Coordinate the adults and materials through our actual routine, not through an assumption that the children will manage it.
Ben | Then the message is five minutes, one of the two finishing choices, structure on the marked shelf, and a clear move to story time.
Nora | That gives us a [[consistent cue::A consistent cue aligns the adults' transition message so Luca hears the same sequence and available choices.]]. We can acknowledge his work, follow through calmly, and keep the choice meaningful without changing the agreed boundary.''',
    rehearsal=["Read Nora and Ben's checked exchange. Stress five minutes, last block or photo, and the marked shelf.","Switch roles. Repeat the first-then sentence with a calm boundary and the two printed choices; do not invent a return time.","Complete the drawing-to-music transfer, check the key, then read it with the three-minute warning and named tray unchanged."],
    transfer_title='Offer a different finishing choice',
    transfer_setup='Drawing time ends in three minutes. The current arrangement allows the drawing to stay in the named tray. Ari can add one final line or ask the educator to label the work. The next activity is music.',
    transfer='''Educator: "Music begins in ___ minutes." | three | The scenario gives a three-minute warning before music begins.
Ari: "My drawing can stay in the named ___." | tray | The permitted storage location is the named tray.
Educator: "You can add one final ___." | line | Adding one final line is one of the available finishing choices.
Ari: "Or I can ask you to ___ the work." | label | Asking the educator to label the work is the second supplied choice.''',
))

BOOK['units'].append(unit(
    title='Co-regulation and peer disagreements',
    scene='One large scoop',
    skill='Describe a peer disagreement neutrally and model a concrete turn-taking sequence without assigning an unobserved motive.',
    brief='Two children reach for the same large scoop. Educator Sora saw Ari holding it and then Bea reaching toward it; Sora does not know either child motive. Ari wants to finish one container. Bea wants the large scoop next. A smaller scoop is available. Sora and colleague Leon discuss language for supporting the disagreement. No injury or ongoing danger is stated. Staff must remain responsive to actual safety needs, preserve both requests, and avoid describing either child as selfish, manipulative, or deliberately aggressive based on this observation.',
    cast='Sora | Educator who observed the interaction\nLeon | Colleague supporting the play area',
    culture=('Validate a wish without endorsing every action', 'A child can want an object without being entitled to take it immediately. Name the wish, describe the current use, and support a practical next step. Neutral language is not passive: adults can maintain safety and a clear boundary without claiming to know motives.'),
    a='''What did Sora directly observe? | Ari holding the large scoop, then Bea reaching toward it | Bea deliberately trying to upset Ari | An injury requiring a supplied treatment | A completed agreement between both children | Only the holding and reaching sequence is observed; motives and outcomes are not established.
What does Ari want to finish? | One container | Every container indefinitely | The whole session alone | A timed ten-minute task supplied in the case | Ari's stated finishing point is one container, not an unlimited period.
Which additional resource is available? | A smaller scoop | A second large scoop | An invented timer agreement | A new toy outside the room | The brief provides a smaller scoop, which may be offered without pretending it is identical.''',
    vocabulary='''co-regulation | Supportive interaction in which an adult helps a child manage responses and build regulation skills. | provide co-regulation
self-regulation | Developing ability to manage attention, feelings, and actions toward a goal. | support self-regulation
emotional validation | Acknowledgment of a person's feeling or wish without approving every action. | offer emotional validation
neutral description | Account of observable events without adding blame or guessed motive. | use a neutral description
observed sequence | Order of events actually seen or recorded. | preserve the observed sequence
inferred motive | Assumed reason for an action rather than a directly established fact. | avoid an inferred motive
turn-taking | Sharing access through an understandable sequence of use. | support turn-taking
current use | What a person is doing with an item at the relevant moment. | acknowledge current use
waiting option | Available activity or resource during a wait. | offer a waiting option
alternative resource | Different available item that may meet some of the same needs. | offer an alternative resource
finishing point | Defined end of a current action before a next step. | agree a finishing point
next turn | Opportunity to use something after the current user finishes the agreed step. | clarify the next turn
resource conflict | Disagreement involving access to an object, space, or material. | mediate a resource conflict
peer interaction | Exchange or activity involving children with one another. | observe peer interaction
calm boundary | Clear limit expressed without shaming or escalating the exchange. | state a calm boundary
emotion vocabulary | Words that help describe feelings and their intensity. | model emotion vocabulary
impulse | Immediate urge to act before reflection or regulation. | support impulse management
adult modeling | Showing a response or language pattern through the adult's own behavior. | use adult modeling
repair | Action that helps address a disruption or harm in a relationship or activity. | support an appropriate repair
forced apology | Required apology words without necessarily establishing understanding or repair. | distinguish repair from a forced apology
reciprocity | Mutual responsiveness in an interaction. | encourage reciprocity
perspective-taking | Recognizing that another person may have a different view or intention. | support perspective-taking
conflict resolution | Process of addressing a disagreement and its practical next steps. | support conflict resolution
agreement check | Confirmation that the proposed arrangement has been understood or accepted. | make an agreement check''',
    precision='I saw Ari holding the scoop, then Bea reaching describes a sequence. Bea wanted to upset Ari assigns a motive that is not established. Keep observations and interpretations separate while responding appropriately to any actual safety concern.',
    precision_extra='The smaller scoop is a different resource, not a second copy of the large one. Offer it honestly as a waiting option. A proposed next turn is not a completed agreement until the children have been supported to understand the arrangement.',
    phrases='''Describe what was seen | I saw Ari holding the large scoop and Bea reaching toward it.
Avoid a motive claim | I do not know why Bea reached at that moment.
Acknowledge both wishes | Both children want to use the large scoop.
Name current use | Ari is using the large scoop now.
Name the finishing point | Ari wants to finish one container.
Preserve the next request | Bea wants the large scoop next.
Offer the actual alternative | The smaller scoop is available while waiting.
Do not pretend equivalence | The smaller scoop is an option, not an identical replacement.
Model a short sequence | First Ari finishes this container; then it is Bea's turn.
Keep language neutral | Let us describe the action without labeling either child.
Validate without surrendering | You want the big scoop. Ari is using it now; you can have the next turn.
Check the proposal | We need to help both children understand the next step.
Keep adult support present | I will stay responsive to the interaction.
Avoid an invented time | No exact number of waiting minutes has been agreed.
Separate words and repair | An apology alone does not settle access to the scoop.
Close practically | Name the current turn, the finishing point, and the next turn clearly.''',
    notes='''I saw | Marks firsthand observation rather than interpretation.
At that moment | Avoids turning a single action into a fixed character trait.
Now and next | Makes the resource sequence concrete.
An option, not identical | Preserves the real difference between available resources.
Help both understand | Treats a proposed arrangement as something to support, not an automatic result.
Stay responsive | Keeps adult attention present rather than assuming the conflict is solved by one sentence.''',
    d='''Which account avoids an unsupported motive? | Ari held the large scoop; Bea then reached toward it. | Bea deliberately wanted to upset Ari. | Ari is always selfish. | Both children planned to disrupt the session. | The correct account preserves the observed sequence without adding intention or a fixed label.
Which proposal uses the supplied facts? | Ari finishes one container, then Bea has the next supported turn; the smaller scoop is available meanwhile. | Bea must wait exactly ten minutes. | Ari keeps the scoop for the entire session. | A second large scoop is available. | The proposal uses the stated finishing point, next-turn request, and actual alternative without inventing resources or timing.
What does emotional validation mean here? | Acknowledge wanting the scoop without approving every action used to obtain it. | Allow any action because the wish is strong. | Deny that either child has a preference. | Diagnose the cause of every feeling. | Acknowledging the wish can coexist with boundaries and practical support for access.
What remains necessary after proposing the sequence? | Support understanding and remain responsive to the actual interaction. | Assume every child agreed without checking. | Leave all supervision to the children. | Record a guaranteed permanent resolution. | A proposed sequence does not prove acceptance or remove the need for adult support.''',
    dialogue='''Leon | Sora, what happened with the large scoop? I heard a disagreement, but I did not see how it began and do not want to repeat the wrong story.
Sora | The [[observed sequence::The observed sequence is Ari holding the large scoop followed by Bea reaching toward it; it does not establish a motive.]] was Ari holding it, then Bea reaching toward it. I do not know the motive, and I should keep that uncertainty clear.
Leon | Then describing Bea as deliberately upsetting Ari would add something we did not establish. We can describe the reach without attaching that explanation.
Sora | Yes. That would be an [[inferred motive::An inferred motive is an assumed reason for the behavior, unlike the directly observed holding and reaching.]]. It can affect how colleagues treat the child later, so the record and conversation should not present it as fact.
Leon | What are they asking for now? If Ari has nearly finished something, we may be able to make the next turn clearer than just saying share.
Sora | Ari wants to finish one container. Bea wants the large scoop next. That gives us a possible [[finishing point::The finishing point is one container, a specific stated limit rather than unlimited use or an invented number of minutes.]] and a next-turn request to work with.
Leon | We could say, "Ari is using the large scoop now. Bea wants it next." That names the situation without saying one child is bad for wanting it.
Sora | That is a [[neutral description::A neutral description names current use and the next request without judging the children or claiming to know their intentions.]]. It helps us respond to the actual resource issue while staying attentive to any safety concern.
Leon | I can offer the smaller scoop while Bea waits. I will say it is smaller; telling Bea it is just the same would ignore what she wants.
Sora | Exactly. It is an [[alternative resource::The alternative resource is the smaller scoop, which can be offered honestly without claiming it is an identical replacement.]], not an identical replacement. We can name what is available without denying that Bea specifically wants the larger one.
Leon | How do we acknowledge the wish without suggesting that reaching for whatever you want always gets you immediate access?
Sora | Use [[emotional validation::Emotional validation acknowledges the wish or feeling while allowing adults to maintain a clear boundary and support appropriate access.]] alongside the boundary: "You want the scoop. Ari is finishing this container, and we can help with your turn next."
Leon | That is more useful than simply saying share over and over. It describes what happens now, what ends the current use, and what comes afterward.
Sora | A concrete [[turn-taking::Turn-taking organizes access through an understandable sequence rather than a vague instruction to share or an unlimited possession claim.]] sequence can help. We still need to support both children in understanding it rather than assume one sentence settles everything.
Leon | We should not add a ten-minute wait or an exact timer rule, because neither is part of the arrangement we have described.
Sora | Correct. The [[next turn::The next turn follows the supplied finishing point, not an invented time limit or a guaranteed immediate transfer.]] is linked to finishing that container. Keep the wording aligned with the actual proposal instead of introducing another condition halfway through.
Leon | And if one child remains upset, we stay responsive. A calm adult presence and clear language matter more than demanding the right apology words immediately.
Sora | That is part of [[co-regulation::Co-regulation combines supportive adult interaction and clear structure while the child develops ways to manage the disagreement.]]. We can model calm language and maintain the boundary without treating a forced phrase as proof that the practical conflict is resolved.
Leon | Then we describe the sequence, preserve both requests, offer the smaller scoop honestly, and help the children understand the proposed current and next turns.
Sora | Yes, with an [[agreement check::An agreement check establishes whether the proposed sequence has been understood or accepted rather than assuming completion from an adult announcement.]] and continued attention. We have a supported proposal, not evidence that the children have already agreed or that no further help will be needed.''',
    rehearsal=["Read Sora and Leon's corrected dialogue. Keep what was seen separate from the motive that was not established.","Switch roles. Repeat the child-facing now-and-next lines with one container as the finishing point and the smaller scoop as the alternative.","Complete the red-truck/blue-truck transfer, check the key, then read it without inventing a motive or a waiting time."],
    transfer_title='Describe another resource disagreement',
    transfer_setup='Noor is using the red truck and wants to finish one route. Eli wants it next. A blue truck is available. The educator observed Eli reaching but does not know the motive.',
    transfer='''Educator: "Noor is using the ___ truck." | red | The red truck is the object currently being used.
Colleague: "The finishing point is one ___." | route | Noor's stated finishing point is one route, not unlimited time.
Educator: "A ___ truck is available meanwhile." | blue | The available alternative is a blue truck, not another red one.
Colleague: "The motive for reaching is ___." | unknown | The observation establishes reaching but not the reason for it.''',
))

BOOK['units'].append(unit(
    title='Observation and family progress conversations',
    scene='Celebrate the observation',
    skill='Share a specific learning observation warmly while rejecting unsupported developmental rankings and diagnoses.',
    brief='During a supervised activity today, educator Rosa saw Eli sort four buttons by color and heard Eli say, "These go together." Parent Andre asks whether this proves Eli is ahead of every child of the same age. No comparison data, developmental screening, or broader assessment is supplied. Rosa can describe the action, exact words, context, and date of observation, but cannot turn them into a universal ranking. The button activity is fictional and requires appropriate materials, age suitability, and supervision; it is not a recommendation to give small loose items to every child.',
    cast='Andre | Eli\'s parent\nRosa | Early-years educator',
    culture=('Warmth does not require exaggeration', 'A parent may hear a cautious answer as a refusal to celebrate. Start with the actual achievement and explain why it is worth sharing. Then distinguish the observation from a comparison that has not been made, without sounding as though the child work is unimportant.'),
    a='''What did Rosa observe? | Eli sorting four buttons by color during a supervised activity | Eli outperforming every same-age child | A completed developmental screening | A diagnosis of exceptional ability | The observed action involves four buttons and color sorting, not a comparative assessment.
Which words belong inside quotation marks in Rosa's note? | These go together. | These four buttons are the same color. | I counted four matching buttons. | I can sort all the colors. | Only These go together was heard; the other sentences add wording or skills that Rosa did not record.
What evidence is missing for the parent's claim? | Appropriate comparison data and broader assessment | Any observation at all | The educator's identity | The fact that the activity was supervised | A universal age-peer ranking requires evidence that this single observation does not provide.''',
    vocabulary='''observation record | Account of what was noticed in a defined context. | create an observation record
anecdotal note | Brief factual account of a meaningful event or behavior. | write an anecdotal note
verbatim quotation | Exact words reproduced without changing their wording. | preserve a verbatim quotation
context | Circumstances in which an event or response occurred. | record the context
work sample | Example of a child's work used as one source of information. | collect a work sample
learning story | Narrative account connecting observed learning with its context and meaning. | develop a learning story
classification | Grouping items according to shared features. | observe classification
sorting criterion | Feature used to decide which items belong together. | identify the sorting criterion
attribute | Observable feature such as color, shape, or size. | name an attribute
one-to-one correspondence | Matching one item with one other item or one count word. | observe one-to-one correspondence
cardinality | Understanding that the final count word represents the number in a set. | explore cardinality
fine-motor skill | Coordinated use of small muscles, often in hand and finger activity. | observe fine-motor skills
developmental domain | Area of development such as language, physical, or social development. | distinguish developmental domains
developmental milestone | Skill or behavior associated with development, interpreted with appropriate variation and context. | discuss a developmental milestone
formative assessment | Information used during learning to guide support and next steps. | use formative assessment
summative assessment | Assessment of achievement at a defined endpoint. | distinguish summative assessment
developmental screening | Structured process identifying whether further developmental evaluation may be needed. | distinguish developmental screening
diagnostic assessment | Qualified evaluation used to establish a diagnosis or detailed explanation. | refer for diagnostic assessment
comparison group | Relevant group used as a basis for interpreting comparative results. | identify the comparison group
norm-referenced measure | Assessment interpreted in relation to an appropriate reference population. | interpret a norm-referenced measure
criterion-referenced measure | Assessment interpreted against specified criteria rather than a peer ranking alone. | use a criterion-referenced measure
reliability | Consistency of a measurement or assessment under relevant conditions. | examine reliability
validity | Support for the intended interpretation and use of assessment information. | examine validity
strength-based description | Account that recognizes capabilities without exaggerating or ignoring support needs. | use a strength-based description''',
    precision='Sorting four objects by color does not establish counting to four, cardinality, or every other early mathematics skill. Name the feature actually observed. The number of objects in the activity is not automatically evidence that the child counted them.',
    precision_extra='Observation, screening, and diagnosis serve different purposes. A single successful moment can be worth sharing without establishing a stable ability across settings or a rank among peers. Use the actual evidence and appropriate assessment processes for broader conclusions.',
    phrases='''Share the observation | Today I saw Eli sort four buttons by color.
Preserve the words | Eli said, "These go together."
Name the setting | This happened during the supervised activity.
Celebrate specifically | I wanted to share the way Eli grouped the colors.
Limit the comparison | This observation does not rank Eli against every child of the same age.
Do not minimize | The observation is useful even without a comparative claim.
Separate skills | Sorting by color does not by itself establish counting skill.
Identify the criterion | Color was the feature used to group the buttons.
Avoid a diagnosis | This was not a developmental diagnosis.
Distinguish screening | No developmental screening result is supplied here.
Invite factual family input | We can record relevant examples you have observed at home.
Keep sources separate | A home report and my observation should each retain their source.
Avoid a fixed label | One moment does not define every aspect of Eli's development.
Use a precise record | Include the action, words, context, and observation date.
Explain a broader claim | A wider conclusion needs appropriate additional evidence.
Close warmly | We can celebrate this moment and keep the description accurate.''',
    notes='''Today I saw | Identifies the observer and time rather than presenting a timeless trait.
Said | Introduces exact words when quoted accurately.
By color | Names the observed grouping feature.
Does not rank | Rejects the unsupported comparison without denying the observation.
By itself | Leaves room for broader evidence without pretending it is already present.
Celebrate and accurate | Shows that warmth and evidence limits can coexist.''',
    d='''Which message is both warm and accurate? | Eli grouped four buttons by color and said, "These go together"; I wanted to share that moment. | Eli is definitely ahead of every peer. | The observation means nothing because it is not a test. | Eli has mastered all mathematics. | The message celebrates the specific observed action and quotation without a broader unsupported ranking.
Which skill is not established just by the described sorting? | Counting the four objects accurately | Grouping by color in this activity | Using the quoted words | Participating in the supervised activity | Four objects being present does not prove that Eli counted them or understood cardinality.
What would a precise note include? | Action, exact words where quoted, context, and observation date | Only a label such as genius | A diagnosis with no evaluation | A peer rank invented from one event | These details preserve the evidence so it can be understood in its actual context.
How should a home example be handled? | Keep it attributed to the family and distinct from Rosa's observation. | Record it as something Rosa personally saw. | Treat it as proof of every developmental domain. | Delete the original activity note. | Family information can be useful while its source remains accurately identified.''',
    dialogue='''Andre | Rosa, you mentioned that Eli sorted buttons today. Does that mean he is ahead of every other child his age? He seems very quick with things at home.
Rosa | I can share a specific [[observation record::The observation record describes today's event, not Eli's rank among all same-age children.]]. Today I saw Eli sort four buttons by color during a supervised activity, and I heard, "These go together."
Andre | I am pleased to hear that. I do not want a technical report, but I would like to understand exactly what made you notice the moment.
Rosa | The [[sorting criterion::The sorting criterion was color, the feature Eli used to group the buttons in the observed activity.]] was color. Eli grouped the items on that basis, and the words connected with the action. That is the specific moment I wanted to share.
Andre | He will be pleased you noticed. When I ask how his day went, I usually get one word. This gives me something specific to talk about with him.
Rosa | Exactly. A [[strength-based description::A strength-based description recognizes Eli's observed capability without exaggerating it into an unsupported peer comparison.]] can celebrate what happened without adding a ranking. I do not need to overstate it to say it was worth noticing.
Andre | Four buttons sounds like counting practice too. Did he actually count them aloud, or was he just putting matching colors together?
Rosa | They are separate. [[Classification::Classification groups items by a shared feature; it does not establish counting or understanding quantity.]] by color does not prove he counted them. Four objects were present, but we should not add an unobserved counting action to the note.
Andre | I have also heard people mention a developmental check. Is this note part of a screening, or are you sharing something you noticed during play?
Rosa | [[Developmental screening::Developmental screening identifies possible evaluation needs through a structured process, unlike this single observation.]] has a different purpose and process. This conversation does not supply a screening result, and the observation is not a diagnosis.
Andre | I see. His cousin did something similar later, so I started comparing them. That is probably not enough to say where Eli stands with children his age.
Rosa | Yes. A relevant [[comparison group::A comparison group provides a basis for comparative interpretation, which is absent from the parent's universal ranking claim.]] and appropriate assessment evidence would matter. A single classroom moment does not establish that Eli is ahead of every same-age child.
Andre | Did he really say, "These go together"? I would like to remember his own words. That sounds just like something he would say at home.
Rosa | I will preserve the [[verbatim quotation::A verbatim quotation retains Eli's exact words, not a more elaborate invented statement.]] when quoting him. If I paraphrase elsewhere, I should make that clear rather than put new words into his mouth.
Andre | At home I have seen him put similar objects together too. Is that useful to tell you, even if it is not a formal assessment?
Rosa | Yes, with the [[context::Context preserves each event's setting; the family's home report remains distinct from Rosa's observation.]] and source kept clear. Your home example and my observation can both inform a conversation without being recorded as the same event.
Andre | At home he sometimes loses interest halfway through. Does that mean today's success does not count, or can you see different things on different days?
Rosa | Different [[developmental domains::Developmental domains concern different areas of development; one sorting observation cannot establish performance across them.]] and settings can show different patterns. We should not turn this one observation into a fixed description of all his abilities.
Andre | That makes sense. I can enjoy hearing what he did without needing it to prove a rank. Please keep sharing these specific moments with me.
Rosa | I will. A useful [[anecdotal note::An anecdotal note preserves an event's action, words, and context without claiming a full developmental assessment.]] includes what happened, what was said, and when and where it occurred. We can be enthusiastic and precise at the same time.''',
    rehearsal=["Read Andre and Rosa's checked exchange. Say Eli's exact quotation naturally, without adding counting or a peer rank.","Switch roles. Repeat the explanation distinguishing sorting, counting, and screening while keeping the parent conversation warm.","Complete the shape-sorting transfer, check the key, then read three objects as an activity fact, not proof of counting."],
    transfer_title='Describe a shape-sorting observation',
    transfer_setup='Educator Noor observed Ari sort three large shapes by shape during a supervised activity today. Ari said, "These are the same." No counting action or peer comparison is supplied.',
    transfer='''Noor: "The grouping feature was ___." | shape | The observed grouping criterion is shape rather than color.
Parent: "There were ___ large shapes." | three | Three is the number of objects supplied in the activity.
Noor: "Ari said, These are the ___." | same | Same completes the exact quotation supplied in the brief.
Parent: "No peer ___ is established." | comparison | The observation supplies no evidence for a peer ranking.''',
))

BOOK['units'].append(unit(
    title='Inclusive participation and home languages',
    scene='Pointing is a response',
    skill='Explain an allowed participation choice while distinguishing access, engagement, and evidence of spoken language.',
    brief='A small-group story activity allows picture choices or spoken answers under Noor\'s current inclusion plan. Noor prefers pointing today. Colleague Ben describes that as nonparticipation. Educator Amina must explain that pointing is an allowed response without claiming it supplies the same evidence as a spoken sentence. No reason for Noor\'s preference, diagnosis, or home-language profile is supplied. The team can use inclusive language, record the actual response format, and keep future support connected to the plan rather than requiring speech as an unannounced condition of belonging.',
    cast='Amina | Early-years educator\nBen | Colleague observing the group',
    culture=('Participation is broader than one response format', 'A quiet response may be easy to overlook in a busy group. Identify what the child actually did and whether it fits the activity plan. Respect a permitted communication choice without pretending that pointing and speaking demonstrate exactly the same language skills.'),
    a='''Which response formats does the plan allow? | Picture choices or spoken answers | Spoken sentences only | No response of any kind | Only copying another child | Noor's current plan explicitly allows both picture choices and spoken answers.
What does Noor prefer today? | Pointing | A supplied spoken presentation | A new diagnosis | Leaving the group as an established fact | The stated preference is pointing, not an inferred reason or diagnosis.
What should the team avoid claiming? | That pointing supplies identical evidence to a spoken sentence | That pointing is allowed here | That the actual response format matters | That the plan should guide participation | Different formats can support participation while providing different evidence of expressive spoken language.''',
    vocabulary='''inclusion plan | Agreed support arrangements for meaningful access and participation. | follow the inclusion plan
participation | Taking part in an activity through an appropriate available form. | recognize participation
engagement | Attention or involvement in an activity, described through relevant evidence. | observe engagement
response mode | Way a person answers or communicates in an activity. | record the response mode
picture choice | Selection among images used to express a response. | offer picture choices
pointing response | Indication made by pointing rather than speaking. | acknowledge a pointing response
spoken response | Answer communicated through speech. | record a spoken response
expressive language | Language used to convey meaning to others. | support expressive language
receptive language | Understanding of language received through listening, reading, or other input. | distinguish receptive language
communication access | Opportunity and support needed to receive and convey meaning. | provide communication access
visual support | Image or visual arrangement that helps understanding or expression. | use visual supports
gesture | Movement used to communicate meaning. | notice a gesture
augmentative communication | Methods that support existing speech or communication. | use appropriate augmentative communication
alternative communication | Methods used instead of speech for some or all communication. | support alternative communication
AAC | Augmentative and alternative communication: tools and strategies supporting communication. | follow the AAC plan
home language | Language used in the child's home or family life. | value the home language
dual language learner | Child learning two or more languages, including English alongside a home language. | support a dual language learner
language difference | Variation connected with languages used, distinct from an assumed disorder. | distinguish a language difference
language delay | Language skills developing more slowly than expected, assessed in context rather than inferred from one response or multilingualism. | refer a language-delay concern
multilingual repertoire | Languages and communication resources a person can draw on. | recognize a multilingual repertoire
family language information | Details families share about language use and communication. | gather family language information
access barrier | Feature that prevents or limits meaningful participation. | identify an access barrier
equitable opportunity | Fair access that may require different supports rather than identical treatment. | provide equitable opportunity
evidence limit | Boundary on what an observation supports. | state the evidence limit''',
    precision='A permitted pointing response can be participation without being a spoken sentence. Record what Noor selected and how the response was made. Do not convert pointing into either no participation or evidence of a spoken-language performance that did not occur.',
    precision_extra='Noor choosing to point today does not establish a diagnosis, reluctance, home language, or general language ability. Home-language information should come from appropriate sources and family partnership, not inference from a name or a single classroom response.',
    phrases='''Refer to the plan | Noor's current plan allows picture choices or spoken answers.
Name today's choice | Noor prefers pointing today.
Recognize participation | Pointing is an allowed response in this activity.
State the observation | Noor selected a picture by pointing.
Keep evidence precise | No spoken sentence was recorded in that response.
Avoid an all-or-nothing label | A nonspeaking response is not automatically nonparticipation.
Separate the aims | Access to the story and evidence of spoken language are related but distinct.
Reject a guessed diagnosis | This response alone does not establish a language delay.
Avoid a language assumption | We do not know Noor's home-language profile from this observation.
Keep support planned | Any change in support should follow the appropriate planning process.
Use the available options | We can make both permitted response formats accessible.
Respect today's preference | We should not remove the allowed choice because speech is more noticeable.
Value family information | Family language information should retain its source and context.
Avoid false equivalence | The two response modes do not provide identical evidence.
Name the barrier | Requiring speech without changing the plan would remove an allowed route.
Close accurately | Noor participated by pointing; that is the response we should record.''',
    notes='''Current plan | Anchors the response choice to the actual arrangement.
Today | Limits the statement to the observed preference rather than a permanent trait.
Allowed response | Connects the action to participation criteria.
No spoken sentence | States the evidence limit without denying engagement.
Related but distinct | Prevents access and assessment from being treated as the same question.
From this observation | Blocks unsupported conclusions about language background or diagnosis.''',
    d='''Which note is most accurate? | Noor participated by selecting a picture through pointing; no spoken sentence was recorded. | Noor did not participate because there was no speech. | Noor produced a complete spoken sentence. | Noor has a confirmed language delay. | The note preserves the permitted participation and the actual response mode without inventing speech or diagnosis.
Which action conflicts with the current plan? | Require spoken answers as the only way to count participation. | Offer picture choices. | Accept a pointing response. | Record whether the response was spoken. | The plan allows picture choices, so an unannounced speech-only rule removes a permitted route.
What can be inferred about the home language? | Nothing specific from the supplied pointing preference alone | It must be English | It must be a particular language based on the name Noor | There is no language used at home | The case supplies no home-language profile, and a single response does not establish one.
Which distinction matters? | Participation can be valid while evidence of spoken-language production remains limited. | Every response mode proves identical language skills. | Pointing always proves noncomprehension. | Inclusion means never documenting response differences. | Inclusive access and precise assessment can coexist without false equivalence between response modes.''',
    dialogue='''Ben | Noor did not give a spoken answer in the story group. I was going to mark that as not participating, but you seem to have recorded a response.
Amina | The [[inclusion plan::The inclusion plan explicitly permits picture choices or spoken answers, so speech is not the only allowed participation route.]] allows picture choices or spoken answers. Noor preferred pointing today and selected a picture, which is an allowed response in this activity.
Ben | I saw the pointing, but I was listening for a sentence. I may have treated the response I expected as the only response that counted.
Amina | That confuses [[participation::Participation means taking part through an appropriate available form; here a permitted pointing response can count without spoken language.]] with one particular format. We should recognize the actual response while staying precise about what it demonstrates.
Ben | Does that mean we should describe pointing as exactly the same evidence as a spoken answer? I do not want our notes to lose the difference.
Amina | No. The [[response mode::The response mode records how Noor answered, preserving pointing as distinct from a spoken sentence.]] matters. We can write that Noor selected a picture by pointing and that no spoken sentence was recorded in that response.
Ben | I will change my note from no response to selected a picture by pointing. That is what I saw; I did not hear a sentence.
Amina | Exactly. The [[evidence limit::The evidence limit prevents an allowed pointing response from being treated as proof of spoken-language production that did not occur.]] stays visible. A meaningful contribution does not need to be exaggerated into evidence of a different kind of performance.
Ben | Could the preference mean a language delay, or tell us which language Noor uses at home? I have heard colleagues make those assumptions.
Amina | Neither follows from this moment. A [[language difference::A language difference and a developmental concern require appropriate contextual information; Noor's single pointing preference establishes neither.]] or concern needs appropriate information, not an inference from one pointing response or from the child's name.
Ben | So we should not record a particular home language unless we actually have that information through the proper family and record process.
Amina | Correct. [[Family language information::Family language information comes from appropriate sources and retains its context; it cannot be invented from a response preference or name.]] should be gathered respectfully and attributed accurately. We should not create a language profile to explain an observation we have not investigated.
Ben | If I insist on a spoken sentence before Noor can count as taking part, I would be removing one of the routes the plan currently allows.
Amina | That would create an [[access barrier::An access barrier would arise from excluding the picture-choice route that Noor's plan currently permits for this activity.]]. We can support the activity through its available options rather than change the participation rule without the appropriate process.
Ben | We still need to notice how children use language over time. Recognizing pointing should not mean we stop describing the language we actually hear.
Amina | Agreed. Evidence of [[expressive language::Expressive language concerns conveying meaning; the record must identify the actual form rather than invent a spoken sentence or erase other communication.]] should identify the actual form and context. Precise observation and inclusive participation are compatible, not opposing goals.
Ben | Before the next group, let us put the picture choices where Noor can reach them. They are not much help if they stay behind my chair.
Amina | Yes. The [[visual support::Visual support must be usable within the activity; merely listing picture choices in a plan does not make them practically accessible.]] needs to be accessible through the planned arrangement. We should check the environment rather than interpret a missing opportunity as a child failure.
Ben | I will change my note to describe the pointing response and its limits. I will not label it nonparticipation or infer a diagnosis or home language.
Amina | That supports [[equitable opportunity::Equitable opportunity can involve different supports while preserving accurate evidence about how each child participated.]]. Noor used an allowed option today, and we can keep both the participation and the response difference clear.''',
    rehearsal=["Read Amina and Ben's corrected dialogue. Contrast selected a picture with no spoken sentence, without calling the child unresponsive.","Switch roles. Repeat the exchange about making the picture choices physically accessible under the current plan.","Complete Ari's transfer, check the key, then read the permitted response and unspecified home language as separate facts."],
    transfer_title='Record another permitted response mode',
    transfer_setup="Ari's current story plan permits a spoken answer or a picture selection. Ari selects a picture today. No spoken answer or home-language information is supplied.",
    transfer='''Educator: "The selected response used a ___." | picture | Ari selected a picture under the current permitted arrangement.
Colleague: "A spoken answer was not ___." | recorded | No spoken answer is supplied in this observation.
Educator: "The choice was allowed by the current ___." | plan | The plan permits either the spoken or picture response.
Colleague: "The home-language profile remains ___." | unspecified | No home-language information is supplied by this particular observation.''',
))

BOOK['units'].append(unit(
    title='Health records and factual incident handovers',
    scene='A reported allergy-plan change',
    skill='Receive a parent health-plan update and make an accountable document handoff without inventing a care decision.',
    brief='Theo\'s parent, Morgan, tells educator Rosa that the allergy plan may have changed. The center still holds the earlier plan, and no revised document is available in this conversation. Health coordinator Amira is present and accepts the document query. No food decision, exposure, symptoms, or emergency is part of this case. Rosa must take the report seriously, preserve the difference between a reported change and a verified revision, and connect Morgan with Amira promptly. The exercise does not authorize changing treatment, relaxing controls, or ignoring a reported safety concern.',
    cast='Morgan | Theo\'s parent\nRosa | Early-years educator',
    culture=('Take an update seriously without guessing its content', 'A missing revised document does not make a parent report unimportant. Acknowledge the concern and give it a receiving owner. At the same time, do not invent the revision, alter a treatment instruction, or announce that every relevant staff member has been updated before that happens.'),
    a='''What does Morgan report? | The allergy plan may have changed. | A verified revision has already reached every staff member. | A food exposure occurred in this case. | An emergency treatment decision is supplied. | The report concerns a possible plan change, not a completed revision or an exposure.
Which status is established when Amira accepts the document query? | The question has a named receiving owner. | The revised allergy instructions are confirmed. | The earlier plan has been formally superseded. | Every educator has received the updated instructions. | Amira accepts ownership of the query; verification, version replacement, and staff communication are not yet established.
What remains unavailable? | The revised document | The fact that an earlier plan is held | The parent's report | The name of the receiving coordinator | No revised document is supplied, so its contents cannot be treated as verified.''',
    vocabulary='''allergy action plan | Individualized document specifying management of a known allergy under appropriate guidance. | verify the allergy action plan
healthcare plan | Agreed information and arrangements for a person's relevant health needs. | review the healthcare plan
reported change | Update described by a source but not necessarily verified. | record a reported change
verified revision | Updated version confirmed through the appropriate process. | obtain a verified revision
current version | Document version established as applicable for use. | confirm the current version
superseded version | Earlier document replaced through the appropriate process. | identify a superseded version
document control | Process for managing document versions, approval, access, and changes. | follow document control
health coordinator | Person responsible for coordinating specified health-information processes. | contact the health coordinator
parent report | Information attributed to a child's parent or carer. | preserve the parent report
source document | Original or authoritative record supporting an instruction or fact. | request the source document
care instruction | Direction governing an aspect of care from the appropriate source. | clarify a care instruction
emergency action plan | Defined arrangements for responding to an emergency. | follow the emergency action plan
allergen | Substance capable of triggering an allergic reaction in a susceptible person. | identify the relevant allergen
food intolerance | Adverse food response distinct from an immune-mediated food allergy. | distinguish food intolerance
allergic reaction | Immune response to an allergen that may require appropriate medical action. | recognize an allergic reaction
anaphylaxis | Serious allergic reaction requiring immediate emergency response. | follow anaphylaxis procedures
exposure | Contact with a substance or situation relevant to the concern. | record a reported exposure
cross-contact | Unintended transfer of an allergen from one food or surface to another. | prevent allergen cross-contact
medication authorization | Required permission or authority for medicine-related action under applicable rules. | verify medication authorization
training record | Documentation of completed relevant staff training. | check the training record
staff briefing | Sharing of relevant information with staff through an appropriate process. | document the staff briefing
incident record | Factual account of a relevant event, actions, and outcomes. | complete an incident record
handoff acknowledgment | Confirmation that the receiving person accepted the query or information. | obtain handoff acknowledgment
unresolved query | Question that still requires an appropriate answer or action. | track the unresolved query''',
    precision='May have changed identifies a reported uncertainty. It is neither proof that the earlier plan remains suitable nor permission to invent a replacement. Escalate promptly through the real health process so the responsible people address the discrepancy and any immediate implications.',
    precision_extra='This case has no food decision, exposure, symptoms, or emergency. Do not create one in the record. In actual care, urgent or emergency action must follow the applicable plan and procedures without waiting for a routine document exchange.',
    phrases='''Acknowledge the report | Thank you for telling me the plan may have changed.
State the held record | We still hold the earlier plan.
Name the missing document | The revised document is not available here.
Preserve uncertainty | I will record this as a reported possible change.
Name the receiving owner | Amira has accepted the document query.
Make the next step immediate | Let us connect you with Amira now.
Avoid inventing the revision | I cannot state the new instructions without the appropriate verification.
Do not dismiss the report | The missing document does not mean we should ignore what you have told us.
Keep decisions separate | This conversation does not establish a food or treatment decision.
Protect sensitive information | We should handle the health information through the appropriate private process.
Check actual receipt | Amira's acceptance gives the query an owner.
Avoid false completion | The plan has not been confirmed as revised yet.
Keep staff updates factual | Do not record a staff briefing before it has occurred.
Preserve version history | The document process should show which version is applicable.
Keep emergency priorities | Actual urgent concerns must follow the appropriate emergency or health route.
Close accurately | Possible change reported, earlier plan held, revision unavailable, query accepted by Amira.''',
    notes='''May have changed | Retains the parent's uncertainty without dismissing the report.
Still hold | Describes the available document, not a judgment that it remains suitable.
Has accepted | Identifies a confirmed receiving person.
Now | Keeps a relevant safety-information query from drifting into an unspecified future task.
Not confirmed yet | Prevents a received question from being labeled a completed plan update.
Before it has occurred | Keeps documentation tied to actual communication events.''',
    d='''Which handoff is accurate? | Parent reports a possible plan change; earlier plan held; revision unavailable; Amira accepts the query. | New instructions verified and every staff member trained. | Theo had a reaction during this conversation. | The report can be ignored until next month. | The handoff preserves the report, document gap, and receiving owner without inventing a care event or completion.
What does Amira accepting the query establish? | The document question has a receiving owner. | The revised plan is verified. | A new food decision is authorized. | Every required staff briefing has occurred. | Acceptance assigns the query but does not complete all subsequent verification and communication.
Which statement is unsafe as a general inference? | No revised paper means the reported concern can be ignored. | The possible change needs appropriate follow-up. | The exact revision is not supplied. | Emergency procedures take precedence when applicable. | A missing document does not remove the need to address a reported health concern through the appropriate process.
What should not be added to the incident record for this case? | An invented exposure, symptom, or treatment | The attributed parent report | The fact that Amira accepted the query | The document discrepancy | The case explicitly supplies no exposure, symptoms, or treatment event, so recording one would be false.''',
    dialogue='''Morgan | Rosa, I need to tell you that Theo's allergy plan may have changed. I do not have the revised document with me, but I do not want this overlooked.
Rosa | Thank you for telling me. I will record the [[reported change::The reported change preserves Morgan's information as a possible update, not as a verified revision or an irrelevant comment.]] and connect you with health coordinator Amira, who is here and has accepted the document query.
Morgan | Does the fact that you still have the old document mean staff will simply assume nothing has changed? That is what I am concerned about.
Rosa | We need to address the [[unresolved query::The unresolved query concerns the possible change and missing revision; holding an earlier document does not settle its implications.]] through our actual health process. Holding an earlier plan does not justify ignoring your report or guessing the new instructions.
Morgan | I need to check the new paperwork myself. Please do not take what I am saying as a complete set of replacement instructions.
Rosa | I will preserve that [[parent report::The parent report must retain Morgan's wording and uncertainty rather than become a confirmed new clinical instruction.]] accurately. The record should not turn may have changed into a completed update or a treatment instruction you did not provide.
Morgan | Who will check which version should apply? I need to know this has reached someone responsible, rather than become a general note no one owns.
Rosa | Amira is the [[health coordinator::The health coordinator is the named receiving owner who is present and has accepted this document question.]] receiving the query. Let us connect you with her now so the discrepancy and its practical implications are handled through the appropriate process.
Morgan | I am calling about the paperwork, not to report a reaction today. I do not want anyone to think I have described an incident that did not happen.
Rosa | I will not add an [[incident record::An incident record must contain actual reported or observed events; this conversation does not supply an exposure, reaction, or treatment.]] that invents such an event. The information we have is your possible-plan-change report and the missing revised document.
Morgan | I am worried another member of staff will see a note saying updated and assume you already have the new document. You do not have it yet.
Rosa | That is why [[document control::Document control preserves the status and version of the available plan and the unresolved revision, rather than silently substituting an assumed update.]] matters. The earlier plan is held, the revised document is unavailable here, and the applicable version needs the appropriate confirmation.
Morgan | I can try to get the document through the approved route. Until then, I would rather the team ask Amira than piece together instructions from my memory.
Rosa | Agreed. A [[verified revision::A verified revision requires the appropriate source and process; rewriting from memory would not establish an authorized update.]] cannot be created by guessing. We must use the real source and authorization process, including any required communication to the people who need it.
Morgan | Once I speak with Amira, will she confirm what still needs doing? I do not want to leave believing the plan has been checked if it has not.
Rosa | No. The [[handoff acknowledgment::Handoff acknowledgment confirms Amira accepted the question, not that the revised plan or staff communication is complete.]] confirms ownership. It does not establish a completed verification, new care decision, or finished staff briefing.
Morgan | That distinction helps. Please keep the information private while making sure it reaches the appropriate staff through the actual process.
Rosa | Yes. Any [[staff briefing::A staff briefing must actually occur through the appropriate process before being recorded as completed; it is not implied by the first handoff.]] must be appropriate and recorded accurately. We should not claim that everyone has received new instructions before that has happened.
Morgan | Then my report is taken seriously, but no one is pretending I supplied a complete new plan today. I will speak with Amira now.
Rosa | Correct. The [[allergy action plan::The allergy action plan requires appropriate verification of its applicable instructions; this conversation establishes the query and handoff, not a replacement plan.]] question is with Amira. We will preserve the source, the missing revision, and the actual next actions without inventing a food or treatment decision.''',
    rehearsal=["Read Morgan and Rosa's checked exchange. Stress may have changed, earlier plan, revision unavailable, and Amira.","Switch roles. Repeat the immediate handoff without turning the parent report into new food or treatment instructions.","Complete the care-plan transfer, check the key, then read it without adding symptoms, verification, or a completed staff briefing."],
    transfer_title='Hand off another health-document query',
    transfer_setup='Parent Ellis reports that a care plan may have changed. The earlier document is held, and the revised version is unavailable. Health coordinator Noor accepts the query. No symptoms are reported.',
    transfer='''Educator: "The revised document is ___." | unavailable | The revised version has not been supplied in this scenario.
Parent: "The earlier document is still ___." | held | The center still holds the earlier document, not a verified replacement.
Educator: "The receiving coordinator is ___." | Noor | Noor explicitly accepts this document query as the receiving owner.
Parent: "No ___ were reported in this conversation." | symptoms | The scenario supplies no symptom report and none should be invented.''',
))

BOOK['units'].append(unit(
    title='Collection, confidentiality, and safeguarding communication',
    scene='A collection request to verify',
    skill='Verify a collection request respectfully, protect private information, and distinguish a stated relationship from confirmed authority.',
    brief='An unfamiliar adult, Owen, tells educator Lea that he is Nia\'s uncle and has come instead of the usual collector. Today\'s collection authority has not been verified. Lead educator Rosa is available to check the arrangement, and Nia has not been released. Owen\'s statement does not establish his identity, family relationship, legal status, or authority for today. Lea needs to explain the verification step calmly, maintain the actual supervision arrangements, and avoid disclosing private contact details. The scenario does not supply a completed check or permission to release Nia.',
    cast='Owen | Adult requesting collection\nLea | Early-years educator',
    culture=('A check is not an accusation', 'A calm explanation of the process can protect dignity without weakening the boundary. Unfamiliarity alone is not proof of wrongdoing, and a friendly relationship claim is not verified collection authority. Keep the child supervised and use the actual local checking and escalation arrangements.'),
    a='''What does Owen state? | He is Nia's uncle and has come to collect her. | A verified court order names him. | Rosa has approved the collection. | He has already completed the required checks. | Owen states a relationship and purpose, but neither has been verified in this conversation.
What is Nia's current status? | She has not been released. | She left with Owen. | She is waiting unsupervised outside. | She has authorized her own release. | The brief explicitly says Nia has not been released.
Who is available to check the arrangement? | Lead educator Rosa | An unidentified person tomorrow | Nia acting alone | Owen through his own statement | Rosa is the available lead educator for checking the arrangement.''',
    vocabulary='''collection authority | Permission established through the applicable process for someone to collect a child. | verify collection authority
authorized collector | Person whose permission to collect has been confirmed as applicable. | confirm the authorized collector
relationship claim | Statement about a relationship that may still require verification. | distinguish a relationship claim
identity verification | Process of checking that someone is who they say they are. | complete identity verification
parental responsibility | Legal responsibilities and rights whose meaning depends on the applicable jurisdiction. | clarify parental responsibility
collection arrangement | Agreed details governing a child's collection. | check the collection arrangement
usual collector | Person who ordinarily collects the child. | contact the usual collector appropriately
substitute collector | Person proposed to collect instead of the usual person. | verify a substitute collector
release | Transfer of a child into the care of an appropriately authorized person. | authorize release
supervision | Active oversight appropriate to the child and setting. | maintain supervision
sign-out record | Record of a child's departure and relevant collection details. | complete the sign-out record
visitor check | Applicable process for checking a person entering the setting. | follow the visitor check
access control | Arrangements restricting entry to authorized people or areas. | maintain access control
safeguarding | Actions and arrangements to protect children from harm and promote welfare. | follow safeguarding procedures
designated lead | Named person with responsibility for a specified area or process. | consult the designated lead
escalation route | Defined channel for referring a concern to appropriate responsibility. | use the escalation route
confidential information | Information that requires controlled access and appropriate handling. | protect confidential information
disclosure | Sharing information with another person or organization. | limit unnecessary disclosure
verified contact route | Communication channel confirmed as appropriate for contacting the relevant person. | use a verified contact route
need-to-know basis | Limiting information access to what a person legitimately requires. | share on a need-to-know basis
legal restriction | Applicable legal limit that must be checked through the proper process. | verify a legal restriction
factual record | Account distinguishing observed facts, attributed statements, and unresolved matters. | maintain a factual record
unverified authority | Claimed permission that has not been established through the relevant process. | identify unverified authority
handover confirmation | Evidence that the authorized transfer actually occurred. | record handover confirmation''',
    precision='Identity, relationship, and collection authority are different questions. Knowing who someone is does not automatically establish permission for this collection. A child recognizing an adult is not a substitute for the applicable authorization process. Do not infer legal status from a family title.',
    precision_extra='Confidentiality is controlled sharing, not an unconditional promise of secrecy. Actual safeguarding duties may require information to reach appropriate people. Follow applicable local requirements and urgent procedures; this language scenario supplies neither a legal ruling nor a universal list of acceptable documents.',
    phrases='''Welcome without authorizing | Hello. Let me check the collection arrangement with our lead educator.
Acknowledge the statement | You have told me you are Nia's uncle.
Name the remaining check | Today's collection authority has not been verified yet.
Explain the boundary | We need to complete the applicable check before any release.
Name the available lead | Rosa is available to check the arrangement.
Keep supervision clear | Nia will remain under our supervision while we follow the process.
Avoid an accusation | I am explaining the required check, not accusing you of wrongdoing.
Separate identity and authority | Confirming identity is not the same as confirming permission for today.
Protect contact details | I cannot read private contact details out at the collection point.
Use the proper contact route | We will use the appropriate verified contact route.
Avoid invented legal conclusions | I cannot infer legal authority from a stated family relationship.
Keep the outcome open | The check has not produced a confirmed decision yet.
Limit the record to facts | I will record what was stated and what has actually been checked.
Avoid false release records | No handover has occurred, so we should not record one.
Keep escalation available | Any concern must follow our actual safeguarding and escalation arrangements.
Close calmly | Rosa will check the arrangement; Nia has not been released.''',
    notes='''You have told me | Attributes a relationship claim without certifying it.
Yet | Marks an incomplete check without promising approval.
Before any release | Makes the sequence and boundary clear.
Not the same as | Separates identity, relationship, and authority.
Private contact details | Names information that should not be casually disclosed.
Has not been released | States the actual child status rather than an anticipated outcome.''',
    d='''Which opening is respectful and accurate? | Hello. Let me check today's collection arrangement with Rosa. | Nia recognizes you, so the family relationship is enough. | Please sign out first; Rosa can confirm permission afterward. | Once your identity is checked, today's permission is automatic. | The opening preserves today's authorization check; recognition, identity, and a sign-out entry cannot replace it.
What would confirming identity alone establish? | Who the person is, not necessarily today's collection authority | Permission to collect in every circumstance | A court's decision on parental responsibility | That a handover has already occurred | Identity verification does not by itself establish the separate authorization or legal questions.
Which information should not be casually read aloud to Owen? | Private family contact details | The fact that Rosa is available | The fact that a check is needed | The fact that no release has occurred | The request does not authorize unnecessary disclosure of confidential family contact information.
Which final record fits the supplied facts? | Owen stated he was Nia's uncle; authority unverified; Rosa available; no release. | Owen's legal authority confirmed and Nia released. | Owen committed an offense. | Nia approved the collection and waived all checks. | The factual record preserves the attributed statement and actual status without inventing approval, wrongdoing, or release.''',
    dialogue='''Owen | Hello. I am Nia's uncle. I have come instead of the person who usually collects her, and I would like to take her home.
Lea | Hello. Let me check the [[collection arrangement::The collection arrangement must be checked through the actual process; Owen's stated relationship does not establish today's permission.]] with Rosa, our lead educator. She is available, and we have not verified today's collection authority yet.
Owen | I understand that you have not met me before. Does being unfamiliar mean you have already decided I am not allowed to collect her?
Lea | No. We need to verify the [[collection authority::Collection authority concerns permission for this collection; unfamiliarity is not itself a completed decision or accusation.]]. I am explaining the check, not making an accusation or announcing a decision before the process is complete.
Owen | I have told you I am her uncle. Surely that explains why I am here, even if you have not seen me at collection before.
Lea | I will record that [[relationship claim::The relationship claim is attributed to Owen; it does not independently verify identity, legal status, or permission to collect.]] accurately. A stated family relationship does not, by itself, confirm identity or permission for today's collection.
Owen | I have identification with me. Would showing that be enough, or do you also need to confirm that I am collecting today?
Lea | [[Identity verification::Identity verification establishes who someone is through the appropriate process, not every separate question of collection authorization.]] concerns who you are. The applicable collection permission is a separate question, and we must follow our actual process for both.
Owen | Could you read out the family contact details so I can tell you which person to call? That might make this quicker.
Lea | I cannot disclose [[confidential information::Confidential information must be protected; an unverified collection request does not justify reading private family contacts aloud.]] at the collection point. We will use the appropriate verified contact route and involve Rosa without sharing private details unnecessarily.
Owen | Can Nia wait outside with me while that happens? I am asking because I do not know how long the check will take.
Lea | Nia needs to remain under our [[supervision::Supervision remains with the setting while the collection authority is unverified; waiting outside with Owen would bypass that boundary.]] while we follow the process. We have not authorized a release, and I cannot give a completion time that has not been confirmed.
Owen | I understand Nia needs to stay with you. I do not want this written up as though I tried to take her without asking.
Lea | That is how the [[factual record::The factual record distinguishes Owen's statement, unverified authority, and actual actions without inventing a release or wrongdoing.]] should read. It will distinguish your statement, the unverified authority, and the actions actually taken, rather than infer a legal conclusion.
Owen | Has Rosa actually seen the arrangement yet? I heard her name and thought perhaps she had already agreed that I could collect Nia.
Lea | Correct. Her availability does not make you an [[authorized collector::An authorized collector has applicable permission confirmed through the proper process; the lead educator's availability alone establishes no approval.]] for today. The check still needs to establish the applicable permission, and we should not announce its outcome in advance.
Owen | If there is a question that you cannot resolve at the collection point, who handles it? I would prefer a clear next step.
Lea | Rosa will use the appropriate [[escalation route::The escalation route sends an unresolved concern to the responsible people under the setting's actual procedures, not an invented universal rule.]] if needed. Any actual safeguarding concern must follow our procedures, while we keep the information accurate and the child supervised.
Owen | All right. Please ask Rosa to check. I will wait where you direct me while Nia stays with the staff; tell me what information you need.
Lea | Yes. No [[release::Release means the authorized transfer of the child; none has occurred while today's collection authority remains unverified.]] has occurred. Rosa is available to check, and we will keep the verification, supervision, and record clear while that happens.''',
    rehearsal=["Read Owen and Lea's corrected dialogue. Use a calm tone while keeping the authorization boundary clear.","Switch roles. Repeat the identity-check and confidential-contact exchanges without promising release or alleging wrongdoing.","Complete Mia's transfer, check the key, then read the aunt claim and unverified permission as separate facts."],
    transfer_title='Separate a family claim from collection permission',
    transfer_setup='An unfamiliar adult says she is Mia\'s aunt. Today\'s collection authority is unverified. Lead educator Noor is available to check. Mia has not been released. No legal document is supplied.',
    transfer='''Educator: "The stated relationship is ___." | aunt | The adult claims to be Mia's aunt, but this remains an attributed statement.
Colleague: "Today's collection authority is ___." | unverified | The supplied facts do not establish confirmed authority for this collection.
Educator: "The available lead is ___." | Noor | Noor is explicitly named as available to check the arrangement.
Colleague: "No ___ has occurred." | release | Mia has not been released under the facts supplied here.''',
))
