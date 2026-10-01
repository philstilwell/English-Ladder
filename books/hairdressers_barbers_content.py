"""Original Hairdressing and Barbering learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='hairdressers-barbers',
    title='Hairdressing and Barbering English',
    cover_label='ENGLISH FOR SALONS AND BARBERSHOPS',
    cover_title='Hairdressing\nand Barbering',
    cover_size=36,
    tagline='Clear choices. Confident consultations.',
    audience='For hairdressers, barbers, salon assistants, receptionists, and salon team leads.',
    map_intro='Eight salon conversations: interpret a reference photo, compare shape and upkeep, discuss a color goal, reschedule a delayed appointment, pause for discomfort, explain optional services, review a result concern, and hand over future preferences.',
    notes_title='Agree on the feature, not just the name.',
    notes_intro='A useful consultation turns broad words and reference pictures into a shared understanding of length, shape, time, price, and permission. Clear language also leaves room to pause, assess suitability, or review a result without promising what has not been established.',
    field_notes=[
        ('A photo contains several choices', 'The client may want the outline but not the length or fringe. Ask which features matter and confirm the agreed plan before treating the whole picture as an instruction.', '"The reference is chin-length, but our agreed outline is collarbone-length, with no fringe requested."'),
        ('Appearance and technique differ', 'Explain the supplied visible contrast before using a style label. A photo does not establish which method is suitable for the client or how long daily styling will take.', '"Photo A keeps visible hair over the sides; photo B exposes skin in its shortest area."'),
        ('Assessment comes before assurance', 'A color goal, Friday deadline, or product name does not establish suitability, service duration, or cost. Record the relevant history and explain what remains to be assessed.', '"Today is a consultation; the previous home-color product is still unknown."'),
        ('A preference is not every permission', 'A retained length or no-spray request can be passed to reception. A future-service request is not a booking, and service consent is not permission for promotional photography.', '"The consultation is requested but not booked, and no promotional-photo consent is recorded."'),
    ],
    scope_note='All salons, clients, prices, photographs described in words, and incidents are fictional. This book teaches workplace English, not cutting, chemical services, medical assessment, product testing, or legal requirements. Follow actual professional training, local rules, product instructions, consultation and consent procedures, and emergency arrangements. No example authorizes an unassessed chemical service, continuing through discomfort, or using a client image without the relevant permission.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Barbers, Hairstylists, and Cosmetologists.',
             url='https://www.bls.gov/ooh/personal-care-and-service/barbers-hairstylists-and-cosmetologists.htm',
             note='Occupational context for consultations, service records, styling, payment, and client communication. The original cases are not transcripts of real appointments.', checked='1 October 2026'),
        dict(title='US Food and Drug Administration. Cosmetics Safety Q&A: Hair Dyes.',
             url='https://www.fda.gov/cosmetics/resources-consumers-cosmetics/cosmetics-safety-qa-hair-dyes',
             note='Background for the importance of current warnings, instructions, and required checks. This book gives no dye formulas, testing steps, or treatment advice.', checked='1 October 2026'),
        dict(title='Wella. Hair Levels and Tones.',
             url='https://www.wella.com/international/wella-magazine/want-achieve-your-dream-shade-hair-levels-and-tones-can-help',
             note='Manufacturer terminology distinguishing lightness or darkness from warm or cool tonal character. No brand numbering system or product recommendation is taught.', checked='1 October 2026'),
        dict(title='Occupational Safety and Health Administration. Hair Salons.',
             url='https://www.osha.gov/hair-salons',
             note='Background for checking actual salon-product information and hazards rather than relying on a familiar product name or marketing claim.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Turning a reference photo into a clear request',
    scene='Keep the ponytail length',
    skill='Separate a reference image into chosen and unchosen features, then confirm the agreed length before cutting.',
    brief='Client Alex shows stylist Ren a photograph of a chin-length bob with a straight fringe. Alex likes the outline but wants enough length for a low ponytail. No cut has started. Through clarification, they agree to discuss a collarbone-length outline rather than copying the chin-length endpoint. Alex confirms that no fringe is requested. Ren must keep the visual reference, practical length requirement, and agreed plan distinct. The conversation does not guarantee that every strand will tie back or authorize other changes not specifically agreed.',
    cast='Alex | Client\nRen | Stylist',
    culture=('A picture starts the conversation', 'A client may expect a photograph to explain a preference but may not want every feature copied. Ask which part appeals to them, then point out any conflict with a practical requirement. Confirm the plan in ordinary length words before relying on technical style names.'),
    a='''What practical feature matters to Alex? | Enough retained length for a low ponytail | Copying every feature of the photo | A new straight fringe | A guaranteed chin-length cut today | Alex wants to retain practical length rather than copy the photograph exactly.
Which endpoint is agreed for the outline discussion? | Collarbone length | Chin length copied automatically | Ear length | An unspecified amount removed | The clarification establishes collarbone length instead of the reference's chin-length endpoint.
What is the fringe status? | No fringe is requested | The photo automatically authorizes it | It has already been cut | It is mandatory for every bob | Alex explicitly confirms that the fringe in the reference is not requested.''',
    vocabulary='''consultation | Discussion to establish preferences, suitability, and the proposed service. | conduct a consultation
reference photo | Image used to communicate an idea, not automatically a complete instruction. | discuss the reference photo
bob | Short-to-medium haircut family with a defined outline, varying in length and shape. | clarify the bob outline
outline | Outer visible shape or boundary of the haircut. | confirm the outline
perimeter | Outer edge defining the haircut's overall length and shape. | discuss the perimeter
chin length | Length described relative to the chin. | distinguish chin length
collarbone length | Length described relative to the collarbone. | confirm collarbone length
retained length | Hair length kept rather than removed. | preserve retained length
low ponytail | Hair gathered and secured low at the back of the head. | retain low-ponytail length
fringe | Front hair shaped to fall over or around the forehead; also called bangs. | clarify the fringe
bangs | Common US term for a fringe. | explain bangs
straight fringe | Fringe with a visually straight outline across the front. | identify the straight fringe
face-framing | Hair shaped around the face as a distinct design feature. | discuss face-framing
front length | Length retained in the hair toward the face. | protect front length
side length | Length of hair at the sides of the head. | compare side length
back length | Length of hair at the back of the head. | confirm back length
parting | Line or division where hair is separated; also called a part. | identify the parting
blunt outline | Perimeter with a visually solid, even edge. | describe a blunt outline
layers | Hair lengths arranged at different levels within a haircut. | discuss layers
trim | Removal of a limited amount, which still needs an agreed length. | clarify the trim
length removal | Amount of hair to be cut off. | confirm length removal
visual feature | Specific visible aspect of the reference or proposed result. | identify a visual feature
agreed plan | Service details explicitly confirmed with the client. | repeat the agreed plan
consent | Permission for the specified action, not every possible variation. | confirm service consent''',
    precision='The photo has a chin-length endpoint and a straight fringe. Alex chooses neither automatically. The agreed outline discussion is collarbone-length, with no fringe requested and retained ponytail length as the practical requirement.',
    precision_extra='A trim, a bob, and enough to tie back can mean different things to different people. Use an agreed visible length reference and check the actual hair before making a promise about how every section will behave.',
    phrases='''Open the reference | Which features of this photograph do you like?
Separate length and shape | Do you want the outline, the length, or both?
Identify the visible endpoint | The photograph shows a chin-length bob.
Ask about daily use | Do you need to be able to tie it back?
Name the requirement | Keeping enough length for a low ponytail matters to you.
Propose the longer outline | Shall we discuss a collarbone-length outline instead?
Keep the fringe separate | The photo has a straight fringe; is that part of your request?
Record the exclusion | No fringe is requested.
Confirm before cutting | Let us agree on the length before any cut begins.
Avoid copying everything | The photo is a reference, not permission for every feature.
Clarify front length | How much front length do you want retained?
Check the outline | Is this the shape you mean?
Avoid an absolute promise | I cannot promise every strand will tie back from the photo alone.
Invite correction | Please stop me if I have misunderstood the priority.
Read back the plan | Collarbone-length outline, retained ponytail length, no fringe.
Close the consultation point | That is the agreed direction, with no cut started yet.''',
    notes='''Reference versus instruction | A reference suggests features; the client must confirm which ones are intended.
At versus off | Length at the collarbone describes the endpoint; an amount off describes removal.
Fringe and bangs | These regional terms can refer to the same front feature.
Enough for | This expresses a practical requirement that needs checking against the actual hair.
Instead | Instead marks the agreed longer endpoint replacing the photo's shorter one.
No cut started | Clarification occurs before the irreversible action, leaving room to correct the plan.''',
    d='''Which read-back preserves the agreement? | Collarbone-length outline, retain ponytail length, no fringe | Chin-length with the photo's fringe | Remove all front length automatically | Copy everything because a photo was shown | The read-back includes the chosen length, practical requirement, and explicit fringe exclusion.
Which feature needs separate consent? | The straight fringe shown in the photo | The fact that the photo exists | The word collarbone | Alex's stated wish to keep length | A visible feature is not automatically requested merely because it appears in the reference.
What does trim fail to specify on its own? | The agreed amount or endpoint of length removal | That hair exists | Whether the client is speaking | The salon's name | Trim is imprecise unless the amount or resulting length is clarified.
Which promise is unsupported? | Every strand will definitely fit into a ponytail based only on this photo. | No cut has started. | The reference shows a chin-length bob. | No fringe is requested. | The reference does not establish how all of Alex's actual hair sections will tie back.''',
    dialogue='''Alex | I brought this picture because I like the bob shape. I do need to keep enough length for a low ponytail, though.
Ren | Let us separate the features in the [[reference photo::Reference photo provides an idea to discuss, rather than automatic permission to copy every visible feature.]]. Which part appeals to you most: the outline, the chin-length endpoint, or the front fringe?
Alex | Mainly the outline. I had not really thought about how short the chin length would feel when I tried to tie it back.
Ren | Then your [[retained length::Retained length names the hair Alex wants to keep for practical use, which can conflict with copying the shorter photograph.]] requirement is important. We should not copy the shorter endpoint simply because it appears in the picture you brought.
Alex | Exactly. I like a defined shape, but tying it back for work matters more than matching the photograph strand for strand.
Ren | We can discuss a [[collarbone-length::Collarbone-length is the longer outline direction agreed for discussion, replacing the reference's chin-length endpoint.]] outline instead. That gives us a different length reference to agree on, rather than assuming the chin-length version is your instruction.
Alex | That sounds closer to what I want. Please keep the ponytail requirement in the plan when we discuss the front and sides too.
Ren | I will. A [[low ponytail::Low ponytail is the practical styling requirement Alex wants preserved while the outline and individual sections are discussed.]] is your stated priority, and we need to check the actual lengths rather than make a promise from this photograph alone.
Alex | There is one thing in the picture I definitely do not want: the straight hair across the forehead. I do not want that added.
Ren | That is the [[fringe::Fringe names the front feature in the photograph, also called bangs, which Alex explicitly does not request.]], also called bangs. I will record no fringe requested, so the photograph does not accidentally become permission to add one.
Alex | Thank you. I have heard both words and was not sure whether they always meant something different. Now I know which feature we are discussing.
Ren | Yes. We are identifying the [[visual feature::Visual feature means a particular visible aspect of the style; naming it helps confirm whether the client wants it.]] rather than relying on the label alone. Your choice here is to leave that feature out of the request.
Alex | Could you also explain outline? I understand the general idea, but I want to be certain it is not another word for shortening everything equally.
Ren | The [[outline::Outline describes the haircut's outer shape, not an automatic instruction to remove the same amount from every section.]] is the outer visible shape of the haircut. We can discuss that shape separately from the amount removed in each area.
Alex | That helps. I want a clear shape at the longer length we mentioned, with enough retained length for the practical way I wear it.
Ren | Let me repeat the [[agreed plan::Agreed plan summarizes the confirmed direction: collarbone-length outline, retained ponytail length, and no fringe requested.]]: collarbone-length outline, keeping your ponytail requirement central, and no fringe requested. Have I understood the priorities correctly?
Alex | Yes. I am glad we checked before starting. I would not want the shorter length or the fringe copied simply because they were in the image.
Ren | That is why we confirm [[consent::Consent applies to the specified agreed action, not every feature present in a reference image.]] for the specific plan. A photograph can contain several choices, and they do not all become part of your service automatically.
Alex | Please keep discussing any other change with me before doing it. I would rather ask another question now than discover a misunderstanding afterward.
Ren | Certainly. No cut has started, and we will clarify any further [[length removal::Length removal is the amount to be cut off, which requires agreement rather than an assumption based on the style name.]] before proceeding. We have the outline direction and your priorities, without adding an unrequested fringe or promising every strand will tie back.''',
    transfer_title='Confirm another reference-photo request',
    transfer_setup='A client shows an ear-length reference but agrees to a shoulder-length outline. The client wants front length retained and explicitly declines bangs. No cut has started.',
    transfer='''Stylist: "The agreed outline is ___." | shoulder-length | Shoulder length is the confirmed direction, not the reference's shorter endpoint.
Client: "Please retain the ___ length." | front | Front length is the specific feature the client wants preserved.
Stylist: "No ___ are requested." | bangs | Bangs are explicitly declined despite any appearance in the reference.
Client: "The cut has not yet ___." | started | The brief places the clarification before any cutting begins.'''
))


BOOK['units'].append(unit(
    title='Describing shape, texture, and everyday styling',
    scene='Less bulk, not bare sides',
    skill='Compare visible features, clarify an everyday styling limit, and distinguish a style label from an agreed result.',
    brief='Client Morgan wants less fullness at the neckline but no exposed skin at the sides. Barber Dev has two reference photographs. Photo A, labelled low taper, shows visible hair covering the sides. Photo B, labelled skin fade, shows exposed skin at the shortest area of the sides. Morgan spends five minutes styling each morning. Dev compares only these supplied appearances. No cutting method, exact length, or guaranteed maintenance time has been agreed. Morgan prefers the covered-side appearance of A, while keeping the neckline concern separate.',
    cast='Morgan | Client\nDev | Barber',
    culture=('Compare what both people can see', 'Style names can vary between shops, images, and clients. Anchor the comparison in visible features rather than insisting that one label settles the request. A daily time limit expresses a preference; it does not prove a proposed style will meet it.'),
    a='''What does Morgan want at the neckline? | Less fullness | More exposed skin at the sides | An agreed cutting technique | A guaranteed daily result | Morgan asks for reduced neckline fullness while separately declining exposed sides.
Which supplied photo shows covered sides? | Photo A | Photo B | Both show bare sides | Neither has been described | Photo A is described as retaining visible hair over the sides.
How much daily styling time does Morgan report? | Five minutes | Twenty minutes | No time limit is mentioned | Forty minutes | The brief states five minutes as Morgan's current morning styling allowance.''',
    vocabulary='''fullness | Visual amount of hair or volume in an area. | reduce neckline fullness
bulk | Perceived density or weight in a section of hair. | clarify unwanted bulk
neckline | Lower outline of the hair at the back of the neck. | discuss the neckline
nape | Back portion of the neck near the lower hairline. | identify the nape
taper | Gradual change in hair length; the intended appearance still needs clarification. | discuss a taper
low taper | Style label suggesting a low-positioned transition, interpreted with a reference. | clarify the low taper
fade | Gradual transition between shorter and longer hair lengths. | compare fade references
skin fade | Fade whose shortest area exposes skin in the supplied reference. | identify the skin fade
transition | Visible change from one length or appearance to another. | describe the transition
blend | Visual merging of different hair lengths or areas. | discuss the blend
exposed skin | Skin visible where the supplied reference has very short hair. | avoid exposed skin
coverage | Visible hair remaining over an area. | retain side coverage
sideburn | Hair extending down in front of the ear. | clarify sideburn length
crown | Area toward the upper back of the head. | identify the crown
hairline | Boundary where hair growth meets visible skin. | describe the hairline
natural texture | Hair's own visible or tactile pattern and behavior. | discuss natural texture
density | Amount of hair growing within an area. | assess hair density
strand thickness | Thickness of an individual hair, distinct from overall density. | distinguish strand thickness
growth pattern | Direction or arrangement in which hair naturally grows. | discuss the growth pattern
cowlick | Area where growth direction makes hair stand or turn differently. | identify a cowlick
finish | Final styled appearance following the service. | compare the finish
styling routine | Usual steps and time used to arrange hair. | describe the styling routine
upkeep | Ongoing effort or appointments needed to maintain an appearance. | discuss upkeep
visual comparison | Comparison of observable features rather than assumptions about technique. | make a visual comparison''',
    precision='Photo A and photo B are defined by their supplied appearances. A keeps visible hair over the sides; B exposes skin at the shortest area. Morgan chooses the covered-side appearance, not every feature associated with the label.',
    precision_extra='Hair density concerns the amount of hair in an area; strand thickness concerns individual hairs. Neither a photo nor a style name establishes Morgan\'s actual hair characteristics, suitable cutting method, or guaranteed daily maintenance time.',
    phrases='''Name the priority | You want less fullness at the neckline.\nKeep the exclusion clear | You do not want exposed skin at the sides.\nCompare the references | Photo A keeps visible hair over the sides.\nDescribe the contrast | Photo B exposes skin in its shortest area.\nCheck the label | When you say taper, is this the appearance you mean?\nSeparate the areas | Let us discuss the neckline separately from the sides.\nAsk about routine | How much time do you usually spend styling it?\nRecord the time limit | You have about five minutes each morning.\nAvoid a guarantee | I cannot promise that routine from the photograph alone.\nClarify coverage | Is keeping the sides covered the important feature?\nAvoid technical assumptions | We have not agreed on a cutting method yet.\nAsk for a visible comparison | Which of these side appearances is closer to your preference?\nClarify bulk | Where does the fullness bother you most?\nCheck the natural pattern | We still need to assess how your hair grows.\nRead back the appearance | Less neckline fullness, with visible hair covering the sides.\nConfirm the boundary | Choosing A does not mean copying every detail.''',
    notes='''Less versus none | Less fullness does not mean removing all hair from an area.\nAt versus on | At the neckline identifies a boundary; on the sides identifies a broader area.\nCovered versus exposed | These describe the visible difference relevant to this client's preference.\nLabel versus reference | A style label helps discussion but does not replace an agreed visual description.\nTime budget | Five minutes states available effort, not a verified styling outcome.\nSeparate priorities | Neckline fullness and side coverage can be discussed without treating them as one decision.''',
    d='''Which comparison is supported? | A shows covered sides; B shows exposed skin at the shortest area. | Every low taper looks identical. | B guarantees five-minute styling. | A authorizes every cutting method. | Only the supplied visible difference is established by the two photographs.
Which clarification best follows less bulk? | Where does the fullness bother you most? | Why do you want all the sides shaved? | Shall I assume no hair remains? | Is your appointment tomorrow? | The location question clarifies the requested change without inventing removal or exposure.
What remains unagreed? | The cutting method and exact length | Morgan's five-minute routine | The dislike of exposed sides | Photo A's described coverage | The brief explicitly leaves the method and exact length unagreed.
Which summary preserves both preferences? | Reduce neckline fullness while retaining visible side coverage. | Expose the sides because the neckline is bulky. | Copy B because both images are short. | Promise no upkeep after choosing A. | The correct summary keeps the desired reduction and the coverage boundary distinct.''',
    dialogue='''Morgan | The back feels too full around my collar, but I do not want bare sides. I have had that misunderstood before.
Dev | Let us separate the [[neckline::Neckline identifies the lower boundary at the back where Morgan wants less fullness, separate from the side-coverage preference.]] from the sides. We can compare the visible features in these two pictures before assuming a style name explains everything.
Morgan | The first picture looks closer. The second one is much shorter at the sides than I would feel comfortable wearing.
Dev | In photo A, labelled low taper, there is visible [[coverage::Coverage means hair remains visibly over the sides, which matches Morgan's stated preference in this comparison.]] over the sides. Photo B has exposed skin in its shortest side area.
Morgan | Then A is the direction I mean. I do not want the shortest area from B added just because I ask for less fullness.
Dev | Understood. [[Exposed skin::Exposed skin is the feature Morgan declines; reducing fullness at the neckline does not authorize adding it at the sides.]] is not part of your request. The neckline concern does not override that boundary, and choosing A does not select every detail.
Morgan | Is taper the word I should use next time? I thought it meant what I wanted, but another person understood it differently.
Dev | It can help, but a [[visual comparison::Visual comparison anchors the discussion in observable features rather than assuming a style label has one identical interpretation everywhere.]] is clearer here. Pointing out covered sides and the area of unwanted fullness gives us more precise information than the label alone.
Morgan | That makes sense. The fullness bothers me where the hair meets my collar, rather than across the whole back of my head.
Dev | I will record the unwanted [[bulk::Bulk refers to perceived fullness or weight in an area, here specifically near the collar rather than across the entire head.]] in that location. We still need to agree on the exact length and assess the actual hair before choosing a method.
Morgan | I also have only five minutes in the morning. I cannot spend a long time trying to reproduce a photograph every day.
Dev | Your [[styling routine::Styling routine describes the time and effort Morgan normally uses, which informs consultation without guaranteeing a particular result.]] is an important part of the discussion. Five minutes is your available time, not something I can guarantee from a reference image.
Morgan | Please do not assume I use a dryer or several products. I would rather explain my routine before we settle the final plan.
Dev | Certainly. We can discuss [[upkeep::Upkeep covers ongoing effort needed to maintain an appearance; it remains a discussion rather than an established five-minute guarantee.]] alongside appearance. The photograph does not show the person's daily routine, products, or how their hair naturally behaves.
Morgan | So the photo helps us compare the sides, but it does not tell you exactly how my hair will sit after the appointment.
Dev | Correct. Your [[growth pattern::Growth pattern is the direction or arrangement of natural hair growth, which must be assessed on the client rather than inferred from another person's photo.]] and other hair characteristics still matter. We have not established those details by looking at someone else's hairstyle.
Morgan | Let me check the main point: I prefer A's covered sides, and I want less fullness at the neckline near my collar.
Dev | Yes. That is the agreed [[appearance::Appearance describes the visible direction being discussed, without claiming an exact length or technical cutting method has already been agreed.]] for discussion. It does not yet specify an exact length or technique, and it does not include the exposed side area in B.
Morgan | Good. I would like those details checked with me before anything starts, especially if a proposed change would affect how covered the sides look.
Dev | We will confirm the remaining details before proceeding. Your five-minute [[time budget::Time budget records Morgan's available styling time, not a promise that the proposed appearance will always take exactly five minutes.]] stays in the consultation, alongside the neckline priority and the clear preference for visible hair over the sides.''',
    transfer_title='Compare another pair of references',
    transfer_setup='Photo C shows hair covering the sides. Photo D shows exposed skin at the shortest side area. The client chooses C, dislikes fullness at the nape, and has ten minutes for daily styling. No method is agreed.',
    transfer='''Barber: "The client prefers photo ___." | C | C is the reference with the covered-side appearance the client chooses.
Client: "The unwanted fullness is at the ___." | nape | Nape identifies the specific location of the fullness concern.
Barber: "The daily time budget is ___ minutes." | ten | Ten minutes is the reported allowance, not a guaranteed styling duration.
Client: "No cutting ___ has been agreed." | method | The brief leaves the technical method open despite the appearance preference.'''
))


BOOK['units'].append(unit(
    title='Discussing color without promising a photograph',
    scene='A cool tone by Friday?',
    skill='Clarify a color goal and previous-product uncertainty while explaining what a consultation has not yet established.',
    brief='Client Priya wants the cool color tone in a photograph before Friday. Colorist Ellis is conducting a consultation only today. Priya used a home-color product previously but cannot identify it. Suitability, service duration, and cost have not been assessed, and no color appointment is booked. Ellis distinguishes the desired tonal character from the lightness or darkness of the reference. The conversation records the unknown product and the deadline without promising a formula, exact photographic match, or completion by Friday.',
    cast='Priya | Client\nEllis | Colorist',
    culture=('Translate the goal without selling certainty', 'A client may use brighter, lighter, warmer, and fresher interchangeably. Clarify the visible quality they mean before using technical language. A deadline can guide planning, but it cannot replace assessment of the service, product history, time, and cost.'),
    a='''What is booked today? | A consultation only | A completed color service | A guaranteed Friday transformation | A confirmed product test | Today's booking is explicitly a consultation, not a color-service appointment.
Which history detail remains unknown? | The previous home-color product | Whether Priya brought a photo | The requested Friday deadline | The preference for a cool tone | Priya cannot identify the earlier product, so its identity remains unknown.
Which claim is unsupported? | The photographed result will be completed by Friday. | The client wants a cool tone. | Cost has not been assessed. | No color appointment is booked. | Neither suitability nor time has been established to support that deadline promise.''',
    vocabulary='''color consultation | Discussion and assessment before a possible color service. | book a color consultation
color goal | Desired color appearance, subject to assessment. | clarify the color goal
level | Relative lightness or darkness of hair color. | discuss the color level
tone | Color character such as warm or cool, distinct from lightness. | clarify the tone
cool tone | Tonal family associated with cooler color character. | identify a cool tone
warm tone | Tonal family associated with warmer color character. | describe a warm tone
ash | Salon term for a cool tonal direction; naming systems vary. | discuss an ash tone
golden | Term describing a warm gold tonal character. | identify golden tones
base color | Main underlying or overall color being discussed. | clarify the base color
regrowth | Hair grown since a previous color service. | discuss visible regrowth
color history | Record of previous coloring products and services. | review color history
home color | Hair-color product applied outside the salon setting. | identify previous home color
product identity | Exact name and identifying information of a product. | confirm product identity
permanent color | Product category designed for lasting color change. | distinguish permanent color
demi-permanent color | Color category distinct from permanent and temporary products; details vary. | clarify demi-permanent color
semi-permanent color | Color category generally intended to fade over washes; details vary. | discuss semi-permanent color
temporary color | Product category intended for short-lived color effects. | identify temporary color
lightener | Product category used to lighten hair, requiring professional assessment. | discuss a lightener service
toner | Product or service used to adjust tonal character. | clarify a toner service
highlights | Selected areas made visibly lighter than surrounding hair. | discuss highlights
balayage | Term associated with hand-painted color placement. | clarify balayage expectations
color correction | Service addressing an unwanted or uneven color result. | assess color correction
suitability | Whether a proposed service is appropriate after assessment. | assess service suitability
service estimate | Provisional statement of expected time or cost. | provide a service estimate''',
    precision='Level describes lightness or darkness; tone describes color character. A cool reference tone does not identify a suitable product, establish a formula, or show that the same result can be achieved on Priya\'s hair by Friday.',
    precision_extra='Unknown is a useful, accurate history entry. Do not relabel an unidentified home product as temporary or harmless. Product names, instructions, warnings, professional assessment, and relevant checks must be handled through actual salon procedures.',
    phrases='''Clarify the attraction | Is it the cool tone or the lighter level that you like?\nExplain level | Level describes how light or dark the color is.\nExplain tone | Tone describes the color character, such as warm or cool.\nSet today's scope | Today is a consultation only.\nAsk about history | Which home-color product did you use?\nRecord uncertainty | The previous product is not yet identified.\nAvoid guessing a category | I cannot assume it was temporary color.\nAcknowledge the deadline | I understand you would prefer it before Friday.\nSeparate goal and promise | The photo shows your goal, not a confirmed result.\nName the pending assessment | Suitability has not yet been assessed.\nKeep time provisional | We have not established the service duration.\nKeep price provisional | We have not assessed the cost yet.\nClarify booking status | No color appointment is booked.\nAvoid a formula promise | We have not selected a product or formula.\nConfirm the next discussion | We need the relevant history before confirming the service plan.\nSummarize accurately | Cool-tone goal, unknown previous product, consultation only.''',
    notes='''By versus before | Both express deadline expectations; neither confirms the salon can meet them.\nLighter versus cooler | Lighter concerns level, while cooler concerns tonal character.\nNot yet | This marks an unfinished assessment rather than a permanent refusal.\nUnknown versus none | Unknown previous product does not mean no previous coloring occurred.\nGoal versus result | A desired appearance is not evidence of an achievable exact match.\nEstimate versus quote | An estimate is provisional; use the salon's actual terms for confirmed prices.''',
    d='''Which explanation distinguishes level and tone? | Level is lightness or darkness; tone is color character. | Both mean appointment length. | Tone means the product price. | Level guarantees suitability. | The correct explanation separates two different dimensions of color description.
Which history entry is accurate? | Previous home-color product not identified. | No previous color used. | Temporary product confirmed. | Permanent product confirmed. | The client reports prior use but cannot identify the product or category.
Which response handles the deadline accurately? | I understand Friday matters; we have not assessed whether that is achievable. | Friday is guaranteed because you have a photo. | All color goals take the same time. | Consultation means treatment starts today. | The response acknowledges the preference without replacing the pending assessment with a promise.
Which status should reception receive? | Consultation only; no color appointment booked. | Friday color service confirmed. | Exact formula selected and approved. | Price accepted and paid. | The supplied facts establish only the consultation and an unbooked future service.''',
    dialogue='''Priya | I love the cool color in this picture. I have an event on Friday, and I was hoping I could have it done before then.
Ellis | I understand the timing. Today is a [[color consultation::Color consultation identifies today's booked discussion and assessment, not an appointment to perform the requested color service.]], so we will clarify the goal and the relevant history before confirming what service might be appropriate.
Priya | Is cool the right word? I like that it does not look golden. I am less certain about whether I want it lighter.
Ellis | That helps. [[Tone::Tone describes the warm or cool character Priya likes, rather than the separate question of how light the color is.]] describes that color character. We can discuss the cool quality separately from how light or dark you want the overall result.
Priya | Then I should not just say I want the same color and expect you to understand every part of the photograph.
Ellis | Exactly. The [[level::Level refers to relative lightness or darkness, which remains a separate preference to clarify alongside the cool tone.]] is the lightness or darkness. The picture gives us a starting point, but those two preferences still need their own discussion.
Priya | I used a color from a shop at home a while ago. I do not remember the name or what type it was.
Ellis | I will record the previous [[home color::Home color identifies the reported earlier product use without inventing its exact brand, category, or effects.]] as unidentified. We should not assume it was temporary, or say there was no previous color, simply because the name is missing.
Priya | I may have the packaging somewhere. Would the exact name be more useful than my memory of the color on the box?
Ellis | Yes, accurate [[product identity::Product identity means the actual identifying information, which is more useful than guessing the category from a remembered package color.]] is useful for the assessment. For now, the honest record is that you used a product but cannot identify it.
Priya | Does that mean you cannot tell me today that I will leave on Friday looking exactly like the photograph?
Ellis | Correct. [[Suitability::Suitability is whether the proposed service is appropriate after assessment; it has not been established by the reference or deadline.]] has not been assessed, and the photograph does not establish how your hair will respond. I cannot promise that exact result or deadline.
Priya | I appreciate knowing that before I plan around it. I also need to understand how much time I would have to set aside.
Ellis | We have not established the [[service duration::Service duration is the time needed for the proposed service, which remains unassessed rather than guaranteed to fit before Friday.]] yet. It depends on the plan after assessment, so I do not want you to treat a guessed length of appointment as confirmed.
Priya | And the price? I have seen very different prices for color services, and I do not know which description applies to my request.
Ellis | The [[cost::Cost has not been assessed because the service plan is not established; no quoted total is available from the supplied facts.]] has not been assessed either. We need to clarify the proposed service before discussing a meaningful amount, rather than selecting a price from the photograph alone.
Priya | That is clear. Please keep the cool-tone preference in the notes, but do not book a service on the assumption that I have accepted it.
Ellis | I will record your [[color goal::Color goal captures the desired cool-tone appearance without turning it into a selected formula, accepted price, or booked service.]] and the unknown product history. No product or formula has been selected, and no color appointment is booked.
Priya | Good. Friday is my preference, but I understand it is not a commitment from the salon. We still need to discuss the actual plan.
Ellis | Exactly. The [[booking status::Booking status distinguishes today's consultation from a future color appointment, which remains unbooked despite the client's preferred deadline.]] remains consultation only. We will keep the deadline, tonal preference, product uncertainty, and pending time and cost assessment separate in the record.''',
    transfer_title='Keep another color request provisional',
    transfer_setup='A client requests a warmer tone for a future event. The previous product is unidentified. Today is consultation only, and neither duration nor price is assessed. No future service is booked.',
    transfer='''Colorist: "The requested tonal direction is ___." | warmer | Warmer describes the desired color character in this new request.
Client: "My previous product remains ___." | unidentified | The product was used but its identity is still unknown.
Colorist: "Today is a ___ only." | consultation | The appointment covers discussion rather than an approved color service.
Reception: "No future service is ___." | booked | A desired result and event do not create a confirmed appointment.'''
))


BOOK['units'].append(unit(
    title='Booking time and handling appointment changes',
    scene='The appointment no longer fits',
    skill='Explain a delay, calculate the earliest ordinary finish, and offer a reschedule without promising a shortened service.',
    brief='Receptionist Hana tells client Luis that the 2:00 haircut appointment is running twenty minutes late. The usual service duration is forty minutes, while Luis must leave by 2:45. A 2:20 start would ordinarily finish at 3:00, so the appointment no longer fits the departure requirement. A 10:00 appointment tomorrow is available. This fictional salon waives the change fee when its own delay causes this rescheduling. Luis chooses tomorrow at 10:00, and Hana confirms the replacement appointment without keeping today as an active second booking.',
    cast='Luis | Client\nHana | Receptionist',
    culture=('An apology needs useful information', 'A brief apology works best with a specific delay, its effect on the client, and a workable option. Do not pressure someone to accept a rushed service because they have already arrived. Explain the relevant local fee rule without presenting it as universal.'),
    a='''What is the revised start based on the stated delay? | 2:20 | 2:00 | 2:45 | 3:20 | Twenty minutes after the original 2:00 appointment gives a 2:20 start.
When would the ordinary forty-minute service finish? | 3:00 | 2:40 | 2:45 | 3:20 | Adding forty minutes to 2:20 gives an ordinary finish of 3:00.
Which replacement does Luis choose? | Tomorrow at 10:00 | Today at 2:45 | Both appointments remain active | An unspecified later day | The client chooses the available 10:00 appointment tomorrow as the replacement.''',
    vocabulary='''appointment slot | Specific time reserved for a service. | confirm the appointment slot
scheduled start | Originally planned beginning time. | state the scheduled start
delay | Difference between the planned and later expected start. | explain the delay
revised start | Updated beginning time following a change. | confirm the revised start
service duration | Amount of time normally allocated to the service. | state the service duration
estimated finish | Expected ending time based on available information. | calculate the estimated finish
departure deadline | Latest time the client must leave. | respect the departure deadline
time conflict | Incompatibility between two timing requirements. | identify the time conflict
availability | Whether a slot can currently be offered. | check tomorrow's availability
reschedule | Move an appointment to a different time. | reschedule the haircut
replacement booking | New appointment taking the place of the original. | confirm the replacement booking
cancellation | Removal of an appointment from the schedule. | record the cancellation
change fee | Charge associated with altering a booking under a stated policy. | explain the change fee
fee waiver | Decision not to charge an otherwise applicable fee. | apply the fee waiver
salon-caused delay | Delay originating from the salon's schedule or operations. | acknowledge the salon-caused delay
late arrival | Client reaching the appointment after its scheduled start. | distinguish a late arrival
no-show | Failure to attend without the required notice under a local policy. | clarify the no-show category
notice period | Required advance time for a change under a specified policy. | explain the notice period
confirmation message | Written or spoken statement of agreed booking details. | send a confirmation message
booking record | Stored appointment details and status. | update the booking record
duplicate booking | Two appointments unintentionally active for the same intended service. | avoid a duplicate booking
waitlist | List of clients seeking a slot if one becomes available. | explain the waitlist
service allocation | Time assigned to carry out the planned service. | preserve the service allocation
calendar date | Specific day identified by date, not only a relative term. | confirm the calendar date''',
    precision='The delay changes the start, not the service duration. A 2:20 start plus forty minutes gives 3:00, fifteen minutes after the client must leave. Do not imply the ordinary service can simply fit into twenty-five minutes.',
    precision_extra='This salon waives the change fee because its delay caused the rescheduling. That is a supplied local policy, not a claim about every salon. Confirm the actual date and replacement status when making a real booking.',
    phrases='''Acknowledge the delay | I am sorry; your appointment is running twenty minutes late.\nState the revised start | The revised start is 2:20.\nAsk about the limit | What time do you need to leave?\nState the ordinary duration | We normally allow forty minutes for this service.\nExplain the arithmetic | A 2:20 start would ordinarily finish at 3:00.\nName the conflict | That would be after your 2:45 departure deadline.\nAvoid a rushed promise | I cannot promise a shortened service to make it fit.\nOffer a concrete alternative | We have 10:00 tomorrow available.\nExplain the local policy | We waive the change fee when our delay causes this rescheduling.\nInvite the choice | Would you like the appointment moved to that slot?\nConfirm acceptance | You would like tomorrow at 10:00 instead.\nReplace the original | I will make this the replacement for today's appointment.\nAvoid a duplicate | Today's slot will not remain as a second active booking.\nRead back details | Let us confirm the date, time, and service together.\nDocument the reason | I will record the salon-caused delay.\nClose with a check | Please check that the confirmation shows the agreed replacement.''',
    notes='''Running late | This describes schedule delay without necessarily blaming the client.\nAt versus by | At 2:20 gives a start; by 2:45 gives a latest departure.\nDuration versus delay | Forty minutes is service time; twenty minutes is the delay.\nInstead | Tomorrow's slot replaces today's rather than adding a second service.\nWaive versus refund | Waiving a fee means not charging it; refunding returns money already paid.\nRelative dates | Tomorrow is clear in conversation but a real confirmation should identify the actual date.''',
    d='''Which explanation is accurate? | Starting at 2:20 would ordinarily finish at 3:00, after your departure deadline. | Twenty minutes late means the service lasts twenty minutes. | A 2:20 start guarantees a 2:45 finish. | Forty minutes after 2:20 is 2:40. | The calculation preserves the ordinary duration and shows the fifteen-minute conflict.
Why is the change fee waived here? | The salon's delay causes the rescheduling under its stated policy. | Every salon is legally required to waive every fee. | Luis arrived late. | All tomorrow appointments are free. | The brief gives a specific local policy and a salon-caused delay.
Which booking record is correct after acceptance? | Tomorrow 10:00 replaces today's appointment. | Both slots remain active without discussion. | Today is marked completed. | Tomorrow remains unconfirmed despite the read-back. | The accepted option is a replacement, not a second active appointment.
Which response should be avoided? | We will definitely compress the forty-minute service into twenty-five minutes. | I am sorry about the delay. | Tomorrow at 10:00 is available. | The ordinary finish would be 3:00. | No shortened service has been promised or established as feasible.''',
    dialogue='''Luis | I am here for my two o'clock haircut. Before I sit down, I should mention that I have to leave by quarter to three.
Hana | I am sorry, but we have a twenty-minute [[delay::Delay is the difference between the original 2:00 start and the revised 2:20 start, not the length of the haircut itself.]] today. I want to explain the timing clearly so you can decide whether another appointment would work better.
Luis | Thank you for telling me. Does that mean I would start at twenty past two, or is that when the haircut would be finished?
Hana | Twenty past two is the [[revised start::Revised start identifies 2:20 as the updated beginning, while the ordinary forty-minute service still has to follow.]]. We normally allow forty minutes for this service, so it would not be finished at that point.
Luis | Then I think we have a problem. I cannot move the time I need to leave, and I do not want to be watching the clock throughout.
Hana | I understand. With the usual [[service duration::Service duration is forty minutes; adding it to the revised 2:20 start produces a 3:00 ordinary finish.]], the ordinary finish would be three o'clock. That is fifteen minutes after you need to leave.
Luis | Could it be made shorter, or would that mean promising something the stylist has not actually agreed to do? I would rather know now.
Hana | I cannot promise a shortened service to meet your [[departure deadline::Departure deadline is Luis's fixed latest leaving time of 2:45, which the ordinary revised schedule cannot meet.]]. The straightforward alternative is to move the appointment to a time that allows the normal service allocation.
Luis | What do you have tomorrow? If there is a morning appointment, that would probably be easier than trying to make today work.
Hana | There is [[availability::Availability means the 10:00 slot tomorrow can currently be offered; it becomes the replacement only after Luis chooses and confirms it.]] at ten tomorrow morning. We can discuss moving your haircut to that slot rather than keeping you waiting for a service that conflicts with your schedule.
Luis | Ten works for me. Would I have to pay a change fee even though the appointment is moving because the salon is behind?
Hana | Under our stated policy, we apply a [[fee waiver::Fee waiver means the salon does not charge the change fee in this salon-caused rescheduling; it is not a refund or universal rule.]] when our delay causes this rescheduling. You will not be charged that change fee for moving this appointment.
Luis | All right, please move it to ten tomorrow. I would prefer that to rushing today or being late for my next commitment.
Hana | I will confirm the [[replacement booking::Replacement booking means tomorrow's accepted appointment takes the place of today's slot rather than adding another active haircut booking.]] for tomorrow at ten. Today's appointment will no longer remain as an active second booking for the same service.
Luis | Good. I sometimes get two reminders after an appointment changes, and then I am unsure which one I am supposed to attend.
Hana | I will check the [[booking record::Booking record holds the active appointment and change reason; updating it helps avoid conflicting reminders or duplicate active slots.]] when making the change. The record should show the agreed replacement and the salon-caused reason for rescheduling.
Luis | Could we read the details back before I go? I want to be certain I have heard the time correctly and that it is still the haircut.
Hana | Yes. The [[confirmation message::Confirmation message should state the actual date, 10:00 time, and haircut service so the client can verify the replacement details.]] should show the actual date for tomorrow, ten o'clock, and the haircut service. We will check those details together.
Luis | That is what I want. Thank you for explaining the finish time instead of just asking me to wait another twenty minutes.
Hana | You are welcome, and I am sorry for the disruption. We have avoided a [[duplicate booking::Duplicate booking would leave two unintended active appointments; the accepted tomorrow slot replaces today's delayed appointment.]] and agreed on the new slot, with the change fee waived under our policy for this delay.''',
    transfer_title='Calculate a different scheduling conflict',
    transfer_setup='A 1:00 appointment is delayed to 1:15. Its usual duration is forty-five minutes. The client must leave at 1:50 and accepts a 9:30 replacement tomorrow. The salon waives the change fee for its own delay.',
    transfer='''Reception: "The ordinary finish would be ___." | 2:00 | Forty-five minutes after 1:15 gives an ordinary finish of 2:00.
Client: "That is ___ minutes after my departure deadline." | ten | The ordinary 2:00 finish is ten minutes later than 1:50.
Reception: "Tomorrow's replacement is at ___." | 9:30 | The client accepts the specific 9:30 alternative supplied in the brief.
Reception: "The change fee is ___." | waived | The stated policy removes this fee because the salon caused the delay.'''
))


BOOK['units'].append(unit(
    title='Checking comfort and pausing clearly',
    scene='Pause before the wash',
    skill='Acknowledge discomfort, clarify the client description, and arrange a check without diagnosing or prescribing a position.',
    brief='Before a wash begins, client Sam tells salon assistant Imani that the neck support feels uncomfortable. Water has not started. Sam describes pressure at the back of the neck where it meets the support. Imani pauses preparation and asks lead stylist Noor to review the comfort concern through the salon process. Sam agrees to that check but does not agree to resume the wash yet. No cause, injury, medical condition, or appropriate body position is established by this conversation.',
    cast='Sam | Client\nImani | Salon assistant',
    culture=('A pause is a service response', 'Some clients minimize discomfort because they do not want to interrupt the appointment. Respond plainly and respectfully when they speak up. Agreement to a comfort check is not the same as agreement to restart; ask about the specific next step.'),
    a='''What has not started? | The water and wash | The client's description | The preparation pause | The request for a comfort check | The brief places the concern before water begins and before the wash starts.
Where does Sam describe pressure? | At the back of the neck against the support | Inside the ear | Across the forehead | Only at the wrist | Sam identifies the contact area at the back of the neck.
What does Sam agree to? | A comfort check, not restarting the wash | Immediate restart without a check | A medical diagnosis | A prescribed new body position | Consent is limited to the check; the wash remains paused.''',
    vocabulary='''wash station | Area equipped for washing a client's hair. | identify the wash station
basin | Bowl at the wash station. | refer to the basin
neck support | Surface or fitting supporting the neck at the basin. | check the neck support
contact point | Place where the body touches a support or surface. | identify the contact point
pressure | Sensation of force against an area, described by the client. | describe the pressure
discomfort | Unpleasant sensation that the client reports. | acknowledge discomfort
comfort check | Review of the client's comfort before proceeding. | arrange a comfort check
preparation | Work done before the wash itself starts. | pause preparation
pause | Temporary stop pending clarification or a check. | keep the wash paused
resume | Begin again after a pause with the required agreement. | confirm before resuming
consent to continue | Agreement to proceed with a specific next action. | ask for consent to continue
client report | The client's own account of a sensation or concern. | preserve the client report
location | Specific area where the sensation is felt. | clarify the location
onset | When a sensation began, without diagnosing its cause. | ask about onset
intensity | How strong a sensation feels to the client. | clarify reported intensity
persistent | Continuing rather than stopping immediately. | describe persistent discomfort
intermittent | Occurring at intervals rather than continuously. | describe intermittent pressure
sensitivity | Reported discomfort or response to contact, without a diagnosis. | record reported sensitivity
scalp | Skin covering the head beneath the hair. | distinguish scalp from neck
support adjustment | Change to a support, subject to appropriate assessment. | request a support adjustment review
positioning | How the client is placed, not a prescription made by this exercise. | refer a positioning concern
lead stylist | Senior salon colleague handling the relevant service concern. | contact the lead stylist
reassurance | Supportive communication that should not become an unsupported safety guarantee. | offer measured reassurance
agreed next step | Specific action the client and staff have confirmed. | state the agreed next step''',
    precision='Sam reports pressure where the neck meets the support. That description is not a diagnosis. The water has not started, preparation is paused, and Noor is asked to review the concern before any decision to continue.',
    precision_extra='Keep permission specific: yes to a comfort check does not mean yes to the wash. Do not prescribe a new position, dismiss the sensation as normal, or promise that changing the support will resolve an unknown cause.',
    phrases='''Acknowledge promptly | Thank you for telling me; we will pause here.\nConfirm the service state | The water has not started.\nAsk for location | Where are you feeling the pressure?\nUse the client's description | You feel pressure where your neck meets the support.\nAvoid a diagnosis | I cannot determine the cause from that description.\nKeep the pause explicit | Preparation remains paused while we check.\nAsk permission for review | Would you like me to ask Noor to review the comfort concern?\nName the next person | Noor is the lead stylist handling this check.\nSeparate consent | Agreeing to the check does not mean restarting the wash.\nAvoid minimization | I will not assume the discomfort is something you should tolerate.\nPreserve the report | I will pass on your description in your own terms.\nAvoid prescribing movement | I will not tell you to change position without the appropriate check.\nCheck understanding | Is the pressure at that contact point what you want me to report?\nAvoid a guarantee | We have not established what will resolve it.\nConfirm the boundary | We have not agreed to resume yet.\nClose the immediate exchange | The next step is the comfort check, with the wash still paused.''',
    notes='''Feels versus is | Feels uncomfortable reports experience; is injured asserts a condition not established here.\nPause versus cancel | A pause stops the current action without automatically ending every future service.\nBefore | Before water starts fixes the sequence and prevents an inaccurate incident account.\nPermission scope | Permission for review applies to review, not every later action.\nClient wording | Specific reported pressure is more accurate than an invented medical label.\nNo minimization | Polite reassurance should not pressure a client to continue through discomfort.''',
    d='''Which report is factual? | Sam describes pressure at the back of the neck against the support. | Sam has a diagnosed neck injury. | The wash caused the condition. | The support adjustment will certainly cure it. | The correct statement preserves the client's reported sensation without assigning cause or diagnosis.
Which action is agreed? | Ask Noor for a comfort check while the wash stays paused. | Restart water because Sam agreed to speak. | Prescribe a particular neck angle. | Treat the concern as resolved without review. | The client consents to review only, with no agreement to restart.
Which reassurance overreaches? | This is definitely harmless, so we can carry on. | Thank you for telling me. | We will pause preparation. | I will report the pressure you described. | Harmlessness is not established, and the client has not agreed to continue.
Which chronology is accurate? | Discomfort was reported before water started. | Discomfort followed a completed wash. | Water had been running for ten minutes. | The appointment had ended before the report. | The supplied sequence places the concern before water or washing begins.''',
    dialogue='''Sam | Before you start the water, can we stop for a moment? The support under my neck feels uncomfortable, and I do not want to ignore it.
Imani | Of course. I will [[pause::Pause means stopping preparation now, not continuing while the client waits for someone to review the concern.]] preparation here. Thank you for telling me before the water starts; we can clarify the concern without beginning the wash.
Sam | It is pressure at the back of my neck, right where it rests against the support. I am not sure how else to describe it.
Imani | That description is useful. The [[contact point::Contact point identifies where the neck touches the support, preserving the client's location description without inventing a cause.]] between your neck and the support is where you feel the pressure, rather than somewhere else on your head. Is that correct?
Sam | Yes, that is the spot. I do not know whether it is the support itself or how I am positioned, and I do not want to guess.
Imani | We do not need to guess the cause. I can arrange a [[comfort check::Comfort check is the agreed review of the reported concern before any decision about resuming the wash.]] with Noor, our lead stylist, while keeping the wash paused.
Sam | Please do. I do not want to hold everyone up, but I would feel better having it checked before anything continues.
Imani | You are not agreeing to [[resume::Resume means begin the wash again; consent to a comfort check does not automatically authorize that separate step.]] by asking for the check. We will keep those decisions separate rather than treating your agreement to speak with Noor as permission to restart.
Sam | Thank you. I was worried that saying yes to the check might mean the water would start while we were still discussing it.
Imani | No. The [[water::Water has not started, and the service remains paused during the requested comfort review.]] has not started, and preparation remains paused. The immediate next step is to pass your concern to Noor, not begin washing.
Sam | Could you say exactly where I feel it? If you just say I am uncomfortable, Noor may not understand what I was trying to explain.
Imani | I will preserve your [[client report::Client report means Sam's account of pressure at the back of the neck against the support, rather than a staff diagnosis.]]: pressure at the back of your neck where it meets the support. I will not add a diagnosis or a cause you have not stated.
Sam | That is right. I do not want it described as an injury when I have not said that and no one has assessed it.
Imani | Agreed. [[Discomfort::Discomfort is the reported unpleasant sensation; it does not by itself establish injury, cause, or a medical condition.]] is what you have reported. I cannot determine the cause from this conversation or promise that one adjustment will resolve it.
Sam | Should I move, or is it better to wait until Noor comes over? I do not want to make another assumption about the position.
Imani | I will ask the [[lead stylist::Lead stylist identifies Noor as the colleague handling the salon comfort review, not as someone whose assessment has already occurred.]] to review that concern through our salon process. I will not prescribe a position or tell you to tolerate the pressure without the appropriate check.
Sam | All right. Please make sure the message says that I have agreed to the check but have not agreed to continue the wash yet.
Imani | I will state that [[consent::Consent is limited to the comfort check, with separate agreement still needed before restarting the wash.]] clearly. You agree to Noor reviewing the comfort concern, and we have not agreed to restart the water or the wash.
Sam | Yes, that is exactly what I mean. I appreciate being able to explain it without feeling that I have to keep the appointment moving.
Imani | The [[agreed next step::Agreed next step is the comfort review while preparation remains paused, not a promised adjustment or resumed service.]] is the comfort check, with your description passed on accurately. We will keep the pause in place while that concern is reviewed.''',
    transfer_title='Report discomfort without adding a diagnosis',
    transfer_setup='Before water starts, a client reports pressure behind the neck against the support. Preparation is paused. The client agrees to a comfort review with lead stylist Jo but has not agreed to resume.',
    transfer='''Assistant: "The reported sensation is ___." | pressure | Pressure is the client's description, not an inferred injury or diagnosis.
Client: "The water has not ___." | started | The concern occurs before water begins, preserving the correct chronology.
Assistant: "The agreed next step is a comfort ___." | review | Review is the action accepted by the client in this scenario.
Client: "I have not agreed to ___." | resume | Agreement to review does not authorize restarting the paused wash.'''
))


BOOK['units'].append(unit(
    title='Explaining services, prices, and product choices',
    scene='What does forty-five include?',
    skill='Explain an optional service, compare complete totals, and confirm a client choice before adding anything.',
    brief='Client Aisha believes the advertised $45 haircut includes a finish. Stylist Ben explains that this fictional menu lists the haircut at $45 and an optional finish at $15, with no other charges in the exercise. Neither service has begun. The complete choices are $45 for the haircut only or $60 for both services. Aisha asks whether buying a styling product is required; Ben confirms it is not part of either quoted service choice. Aisha chooses the haircut only, with no finish or retail product added.',
    cast='Aisha | Client\nBen | Stylist',
    culture=('Make the optional part genuinely optional', 'Clients may assume a familiar service name includes the same elements everywhere. Explain the specific menu without implying they should have known. State the full comparison before seeking a choice, and do not let a product recommendation become an unrequested purchase.'),
    a='''What is the haircut-only total? | $45 | $15 | $60 | $75 | The supplied menu sets the haircut alone at forty-five dollars.
What is the complete combined total? | $60 | $45 | $15 | $90 | The forty-five-dollar haircut plus the fifteen-dollar optional finish totals sixty dollars.
What does Aisha choose? | Haircut only, with no finish or product added | Haircut and finish | A retail product instead of a haircut | Both services without a price discussion | The final choice explicitly excludes the optional finish and retail product.''',
    vocabulary='''service menu | List describing available services and their prices. | explain the service menu
base service | Main service before optional additions. | identify the base service
optional finish | Separately offered final styling service in this menu. | explain the optional finish
add-on | Additional item or service requiring agreement. | confirm an add-on
inclusive price | Price covering the specified listed elements. | clarify the inclusive price
combined total | Sum payable for the selected services together. | state the combined total
itemized price | Price shown separately for each component. | provide an itemized price
service inclusion | Element covered by a particular service description. | clarify service inclusions
service exclusion | Element not covered by the quoted service. | explain service exclusions
retail product | Product sold for the client to take away. | discuss a retail product
product recommendation | Suggested product, not an automatic purchase. | separate a recommendation from a sale
styling cream | Product category used to help shape or manage a style. | describe a styling cream
mousse | Foam-format styling product. | identify a mousse
gel | Gel-format product used for styling or hold. | describe a gel
pomade | Styling-product category often associated with shape, control, or sheen. | clarify a pomade preference
finishing spray | Spray product used as a finishing step, subject to client preference. | discuss finishing spray
hold | Degree of styling control claimed for a product. | compare hold descriptions
shine | Degree of visible sheen in a finish. | describe the shine
matte finish | Low-shine appearance in a product or style description. | clarify a matte finish
product claim | Statement made about a product's characteristics or effects. | check a product claim
purchase decision | Client's choice whether to buy an item. | confirm the purchase decision
service authorization | Permission to carry out the specified service. | confirm service authorization
price misunderstanding | Difference between what the client expected and what the menu includes. | resolve a price misunderstanding
charge confirmation | Read-back of the agreed amount and what it covers. | give a charge confirmation''',
    precision='The finish is optional and costs $15 in addition to the $45 haircut. Both services total $60; the haircut-only choice remains $45. There are no other charges in this fictional comparison, and no retail product is included.',
    precision_extra='A recommendation is not a purchase decision. Product words such as hold, matte, and shine describe features to discuss; they do not establish suitability for every person or permission to add a product to the bill.',
    phrases='''Acknowledge the expectation | I understand you thought the finish was included.\nRefer to the specific menu | On this menu, the haircut is $45.\nIdentify the optional element | The finish is an optional $15 addition.\nState the combined total | Both services together would be $60.\nPreserve the base choice | The haircut-only option remains $45.\nClarify the comparison | Those are the complete totals for these two choices.\nAsk before adding | Would you like the finish added, or the haircut only?\nSeparate recommendation and sale | A product recommendation does not add it to your purchase.\nConfirm no purchase requirement | Neither service choice requires a retail-product purchase here.\nExplain a product word | Matte describes a lower-shine appearance.\nAvoid universal claims | We need to check the actual product information and your preference.\nConfirm the decision | You have chosen the haircut only.\nRecord the exclusions | No finish or retail product will be added.\nResolve without blame | Let us make the inclusions clear before we begin.\nRead back the charge | The agreed service is the haircut at $45.\nKeep later changes explicit | We would confirm any later addition before proceeding.''',
    notes='''Includes versus costs extra | Includes places an element inside the price; costs extra marks a separate charge.\nOptional | The client can decline without losing the stated base-service choice.\nTogether versus each | Together gives the combined total; each would imply separate equal amounts.\nWould be | This expresses the price of an option before it is chosen.\nRecommendation versus authorization | Suggesting a product does not authorize sale or application.\nNo other charges | This is a supplied fictional fact, not a rule for every real salon price.''',
    d='''Which comparison is complete? | Haircut only $45; haircut plus finish $60. | Finish $15, with no base price mentioned. | Both services $45 because the client assumed so. | Haircut only $60 and finish extra. | The correct comparison gives both complete totals using the supplied menu.
Which question preserves a real choice? | Would you like the $60 combined option or the $45 haircut only? | You want the finish, do you not? | Shall I add the product because I mentioned it? | Can we discuss the price after finishing? | The question presents both priced options before any service begins.
What does matte describe here? | A lower-shine appearance | A guaranteed allergy-free product | A mandatory purchase | A fixed haircut length | Matte concerns appearance, not safety guarantees, purchase requirements, or haircut length.
Which final read-back matches Aisha's decision? | Haircut at $45, with no finish or retail product added. | Both services at $60, plus an unpriced product. | Finish only at $15. | Haircut and finish at $45. | The correct read-back preserves the selected base service and explicit exclusions.''',
    dialogue='''Aisha | I thought the forty-five-dollar haircut included the finish. Before we start, can you explain what that price actually covers?
Ben | Of course. On this [[service menu::Service menu is the specific list governing this fictional price comparison; the client should not be expected to infer its inclusions from other salons.]], the haircut is forty-five dollars, and the finish is listed separately as an optional fifteen-dollar addition.
Aisha | So if I have both, the final amount is not forty-five. I would like the complete number rather than just the extra amount.
Ben | The [[combined total::Combined total adds the forty-five-dollar haircut and fifteen-dollar finish, giving sixty dollars with no other charges in the exercise.]] for both services is sixty dollars. The haircut-only option is forty-five dollars, and those are the complete totals for these two choices.
Aisha | Thank you. I do not want to agree to the haircut and then discover that the finish was treated as something I had already accepted.
Ben | The [[optional finish::Optional finish is a separate service the client may accept or decline; it is not automatically authorized by choosing the haircut.]] is your choice. Neither service has begun, and I will confirm what you want before adding anything to the agreed plan.
Aisha | Can I just have the haircut today? I am keeping to a budget, and I would rather understand the basic option clearly.
Ben | Yes. The [[base service::Base service is the haircut alone at forty-five dollars, which remains available without the optional finish.]] here is the haircut at forty-five dollars. Declining the finish does not remove that option or turn it into the sixty-dollar combined service.
Aisha | I also heard someone mention a styling product. Do I have to buy one to have the haircut-only option at that price?
Ben | No. A [[retail product::Retail product is a separate take-home purchase, not a required component of either quoted service choice in this scenario.]] is not part of either quoted service choice, and neither requires a product purchase here. Discussing one does not mean adding it to your bill.
Aisha | That is helpful. Sometimes a recommendation sounds like a requirement, especially when I do not know the difference between the product names.
Ben | We can keep the [[product recommendation::Product recommendation is a suggestion to discuss, not the client's authorization to buy or a condition of receiving the stated service.]] separate from the service decision. You can ask about a feature without agreeing to buy anything.
Aisha | For example, what does matte mean? I have seen it on products, but I am not sure whether it describes strength or something else.
Ben | A [[matte finish::Matte finish describes a lower-shine appearance, not the degree of hold or a guarantee that a product suits every client.]] describes a lower-shine appearance. Hold is a different feature, and the actual product information matters when comparing what a particular item claims.
Aisha | So I can ask those questions now and still decide not to buy a product. I do not want anything automatically added today.
Ben | Exactly. The [[purchase decision::Purchase decision belongs to the client and remains separate from asking questions or hearing a recommendation.]] is separate from the discussion. I will not add a product simply because we have talked about its description.
Aisha | Then please keep today to the haircut only, at forty-five dollars. No optional finish and no retail product for me.
Ben | I will record that [[service authorization::Service authorization is limited to the haircut the client selects; it excludes the optional finish and any retail purchase.]]: haircut only at forty-five dollars, with no finish or retail product added. We have clarified the choice before either service begins.
Aisha | Yes, that is correct. I am glad we checked, because I would have felt awkward questioning the price after the service was finished.
Ben | Let me give the final [[charge confirmation::Charge confirmation repeats the agreed forty-five-dollar haircut and exclusions, resolving the original misunderstanding before work starts.]]: forty-five dollars for the haircut. Any later addition would need its own clear discussion and agreement; nothing extra has been selected today.''',
    transfer_title='Compare another optional service',
    transfer_setup='A fictional menu lists a haircut at $50 and an optional finish at $20, with no other charges. The client chooses the haircut only and declines a retail product. Nothing has begun.',
    transfer='''Stylist: "Both services would total ___ dollars." | seventy | Fifty plus twenty gives the combined total of seventy dollars.
Client: "My haircut-only choice is ___ dollars." | fifty | The selected base service retains its fifty-dollar price without the finish.
Stylist: "The finish is ___." | optional | The client can decline the separately priced finish in this menu.
Client: "No retail product is ___." | selected | The client explicitly declines a product rather than authorizing an extra sale.'''
))


BOOK['units'].append(unit(
    title='Responding to a concern about the result',
    scene='The left side looks longer',
    skill='Acknowledge a specific result concern, separate appearance from confirmed findings, and arrange review before promising a remedy.',
    brief='At checkout, client Mei says the left side of the haircut looks longer. Receptionist Rafael hears that the earlier consultation promised an even outline. The current appearance has not been reviewed together with stylist Jo. Rafael pauses checkout and offers a mirror review with Jo. Mei accepts the review. No cause has been established, and neither a correction nor a refund has been approved. The conversation must not turn a reported concern into a confirmed cutting error, a promise to remove more hair, or an automatic payment resolution.',
    cast='Mei | Client\nRafael | Receptionist',
    culture=('Acknowledge without deciding the finding', 'You can take a concern seriously without declaring either that the client is mistaken or that the stylist made an error. Repeat the observable concern, arrange a specific review, and keep the client informed about what has and has not been agreed.'),
    a='''What does Mei report? | The left side looks longer | The right side has already been corrected | A refund has been approved | The stylist has confirmed the cause | The concern is a reported visual difference that has not yet been reviewed.
What was the earlier agreed expectation? | An even outline | A deliberately uneven outline | A shorter left side only | No discussion of the outline | The consultation reportedly promised an even outline, making that expectation relevant to review.
What is accepted now? | A mirror review with Jo | Immediate removal of more hair | An approved refund | A confirmed fault diagnosis | Mei accepts the review while correction and payment decisions remain unapproved.''',
    vocabulary='''result concern | Client's question or dissatisfaction about the service outcome. | acknowledge a result concern
even outline | Outer edge intended to look balanced in length. | review the even outline
apparent difference | Difference that seems visible before assessment confirms details. | describe the apparent difference
left side | Client's left-hand side, clarified from the client's perspective. | identify the left side
right side | Client's right-hand side, distinguished from a mirror image. | compare the right side
mirror review | Joint examination of the appearance using a mirror. | arrange a mirror review
hand mirror | Portable mirror used to show another view. | offer a hand mirror
viewing angle | Direction from which the result is being seen. | clarify the viewing angle
client perspective | The client's view or orientation, important for side references. | confirm the client perspective
reported expectation | What the client says was agreed earlier. | record the reported expectation
consultation note | Record of preferences and agreed service details. | check the consultation note
assessment finding | Conclusion reached through the relevant review. | distinguish an assessment finding
cause | Reason for the apparent difference, not yet established. | avoid inventing a cause
correction | Additional work intended to address a confirmed concern. | discuss a proposed correction
remedy | Proposed response to a service concern. | clarify the proposed remedy
rework consent | Permission for specifically described additional service work. | confirm rework consent
refund request | Client's request for money to be returned. | record a refund request
refund approval | Authorized decision to return money under the relevant process. | distinguish refund approval
checkout pause | Temporary stop in the payment process while a concern is addressed. | confirm the checkout pause
service record | Record of what was discussed and performed. | review the service record
acknowledgment | Clear recognition that the concern has been heard. | give a specific acknowledgment
defensive response | Reply focused on resisting criticism rather than addressing the concern. | avoid a defensive response
premature conclusion | Finding stated before the evidence or review supports it. | avoid a premature conclusion
resolution status | Current stage of handling the concern. | state the resolution status''',
    precision='Mei reports that the left side looks longer; no joint review has confirmed a cause or cutting error. The earlier expectation was an even outline. Acknowledging both facts does not authorize removing more hair.',
    precision_extra='Keep the next step distinct from the outcome. A mirror review is accepted, checkout is paused, and no correction or refund is approved. Further work requires a specific explanation and the relevant agreement, not an assumption that review implies consent.',
    phrases='''Acknowledge specifically | I hear that the left side looks longer to you.\nRecognize the expectation | You were expecting an even outline.\nPause the transaction | Let us pause checkout while we address the concern.\nAvoid dismissal | I will not assume it is just your imagination.\nAvoid a finding too soon | We have not reviewed the appearance together yet.\nOffer a concrete next step | Would you like a mirror review with Jo?\nClarify orientation | Do you mean your left side as you are sitting here?\nPreserve the wording | I will pass on that it looks longer, not that a cause is confirmed.\nSeparate review and correction | Agreeing to review does not authorize more cutting.\nAvoid a remedy promise | No correction has been approved yet.\nKeep payment status accurate | No refund has been approved.\nInvite the relevant explanation | Jo can review the concern against the agreed outline.\nCheck the record | We can refer to the consultation note during the review.\nConfirm the accepted step | You would like the mirror review first.\nKeep the client involved | Any proposed further work should be explained before agreement.\nClose without premature resolution | The review is the next step; the concern is not yet resolved.''',
    notes='''Looks versus is | Looks longer reports perception; is longer asserts a confirmed comparison.\nYour left | Clarifies orientation when a mirror or another person's viewpoint could confuse sides.\nReview versus redo | Review examines the issue; redo implies additional service work.\nAcknowledge versus admit | Acknowledging a concern does not automatically establish a fault finding.\nRequest versus approval | A requested refund and an authorized refund have different statuses.\nFirst | First sequences review before any proposed remedy rather than guaranteeing a later outcome.''',
    d='''Which opening is most useful? | I hear that the left side looks longer and that you expected an even outline. | It cannot be uneven because our stylist is experienced. | The stylist definitely cut it incorrectly. | I will remove more hair immediately. | The response acknowledges the specific concern and expectation without deciding cause or remedy.
Which statement confuses review with consent? | Agreeing to the mirror review means we can cut more without asking. | Checkout is paused. | Jo will review the concern. | No refund is approved yet. | Consent to examine the result does not authorize additional cutting.
Which handover is accurate? | Client reports a longer-looking left side; joint review pending. | Cutting error confirmed and fixed. | Client approved a refund. | Client withdrew the concern. | The handover preserves the reported appearance and unfinished review status.
Which next step has been accepted? | Mirror review with Jo before deciding a remedy | Automatic refund before review | Immediate correction of both sides | Closing the complaint as resolved | The brief confirms review only and leaves both correction and refund unapproved.''',
    dialogue='''Mei | Before I pay, could someone look at the left side? It looks longer than the right, and we agreed on an even outline.
Rafael | Thank you for telling me. I hear the [[result concern::Result concern is Mei's reported longer-looking left side, which should be acknowledged without immediately deciding whether a cutting error occurred.]], and I understand that an even outline was the expectation discussed before the service.
Mei | Yes. I am not trying to be difficult, but I do not want to leave and then feel I should have said something while I was here.
Rafael | Let us put a [[checkout pause::Checkout pause means temporarily stopping the payment process to address the concern, not approving a refund or declaring the service resolved.]] in place while we address it. I can ask Jo, your stylist, to review the appearance with you.
Mei | That would help. I want to show the exact part I mean rather than have the message passed on simply as a complaint about the haircut.
Rafael | We can arrange a [[mirror review::Mirror review is the specific accepted next step for examining the visible concern with Jo before any remedy is decided.]] so you can point it out directly. Would you like that review with Jo before we discuss any possible next action?
Mei | Yes, please. I am pointing to my left side as I sit here. I know the mirror can make the direction confusing.
Rafael | Thank you for clarifying the [[client perspective::Client perspective fixes left and right relative to Mei, avoiding confusion caused by the receptionist's viewpoint or the mirror.]]. I will say your left side, rather than relying on which side appears on my left when I face you.
Mei | I also want Jo to know that the outline was supposed to look even. That was the part we discussed during the consultation.
Rafael | I will include that [[reported expectation::Reported expectation is the even outline Mei says was agreed, which is relevant to review without proving the current cause or finding.]]. The concern should be reviewed against what was agreed, not treated as a new request for an unrelated style.
Mei | Do you think it actually is longer, or could it be the way I am looking at it? I do not want anyone guessing.
Rafael | We have not established an [[assessment finding::Assessment finding would follow the relevant review; the conversation currently contains a reported appearance rather than a confirmed cause.]] yet. I can acknowledge what you see without deciding the cause before you and Jo review it together.
Mei | That is fair. Please do not promise to cut more off before Jo has explained what is being proposed. I might not want that.
Rafael | Absolutely. Your agreement to review is not [[rework consent::Rework consent would authorize specifically described additional work; accepting a mirror review alone does not give that permission.]]. Any proposed further work should be explained and agreed separately before anything is done.
Mei | And if I ask about a refund afterward, would that already have been approved by pausing checkout, or is that a separate discussion?
Rafael | That is separate. No [[refund approval::Refund approval is an authorized payment decision, which has not occurred simply because checkout is paused or a review is accepted.]] has been given, and I do not want to imply that it has. Right now, the accepted next step is the mirror review.
Mei | Good. Please keep the message factual: it looks longer to me, I expected an even outline, and I want to review it with Jo first.
Rafael | I will record the [[apparent difference::Apparent difference describes how the result looks to Mei without changing the report into a confirmed cutting error or diagnosis of cause.]] in those terms. I will not say the cause is known, a correction is agreed, or the matter is already resolved.
Mei | Thank you. That gives us a clear way to look at it without anyone becoming defensive or making decisions before I understand them.
Rafael | The current [[resolution status::Resolution status is review accepted and pending, checkout paused, with no correction or refund approved and no final outcome established.]] is review pending, with checkout paused. We will keep you involved in any proposal that follows rather than treating the review itself as the remedy.''',
    transfer_title='Keep a second result concern factual',
    transfer_setup='A client says the right side looks fuller than expected. An even outline was agreed. A mirror review with stylist Kai is accepted. Checkout is paused; neither further cutting nor a refund is approved.',
    transfer='''Reception: "The reported concern is the ___ side." | right | The client identifies the right side in this new scenario.
Client: "We agreed on an ___ outline." | even | Even outline is the earlier expectation relevant to the review.
Reception: "The accepted next step is a mirror ___." | review | Review is accepted, while a particular remedy has not been authorized.
Reception: "No refund is ___." | approved | Pausing checkout and reviewing the concern do not establish refund approval.'''
))


BOOK['units'].append(unit(
    title='Passing preferences to the next appointment',
    scene='Requested is not booked',
    skill='Hand over confirmed preferences, an unbooked consultation request, and photography permission as separate facts.',
    brief='Stylist Sora is handing client details to receptionist Jordan. The client requested a future color consultation but has not booked it or accepted a date. Confirmed preferences from today are retained front length and no finishing spray. No agreement to promotional photographs is recorded. Sora and Jordan must preserve those distinctions when updating the record: a preference is not a booking, a request is not an accepted appointment, and participation in a salon service does not establish permission to use an image for promotion.',
    cast='Sora | Stylist\nJordan | Receptionist',
    culture=('Pass on statuses, not convenient assumptions', 'A quick handover can accidentally turn interest into a booking or silence into agreement. Label each item according to what the client actually said. Read back the pending request and confirmed preferences separately so the next colleague does not have to reconstruct the conversation.'),
    a='''What future service is requested? | A color consultation, not yet booked | A completed color treatment | A confirmed appointment date | A promotional photograph session | The client requested a consultation but has not selected or accepted an appointment.
Which preferences are confirmed? | Retained front length and no finishing spray | Shorter front length and extra spray | Any future color formula | Unlimited promotional photography | The brief confirms only the two stated service preferences.
What is the photography status? | No promotional-photo agreement is recorded | Consent is implied by visiting | Permission covers every future use | The client approved a campaign | No explicit agreement has been recorded, so permission must not be assumed.''',
    vocabulary='''client profile | Record of relevant client information and preferences. | update the client profile
preference note | Recorded choice about how the client wants a service handled. | preserve a preference note
front-length retention | Keeping the specified hair length toward the face. | confirm front-length retention
no-spray preference | Request not to use finishing spray. | record the no-spray preference
consultation request | Expression of interest in a consultation, not a confirmed appointment. | record the consultation request
pending booking | Appointment arrangement that is not yet confirmed. | distinguish a pending booking
accepted date | Appointment date the client has explicitly agreed to. | confirm the accepted date
follow-up contact | Later communication about an unresolved request. | arrange follow-up contact
handover | Transfer of relevant information and responsibility between colleagues. | give an accurate handover
read-back | Repetition of key details to confirm understanding. | perform a read-back
record amendment | Correction or update to an existing entry. | make a record amendment
service consent | Permission for a particular salon service. | distinguish service consent
image permission | Agreement concerning taking or using a person's image. | check image permission
promotional use | Use of material to advertise or market the salon. | clarify promotional use
portfolio image | Image displayed to demonstrate work, subject to appropriate permission. | discuss a portfolio image
publication channel | Place where content may be shared, such as a website. | specify a publication channel
permission scope | Exact action or use covered by an agreement. | confirm permission scope
recorded agreement | Agreement documented in the relevant record. | check the recorded agreement
unconfirmed assumption | Belief not supported by what the client has agreed. | remove an unconfirmed assumption
factual handover | Handover limited to accurate, relevant information. | provide a factual handover
open request | Request still awaiting a decision or arrangement. | track the open request
next contact owner | Person responsible for the next communication. | identify the next contact owner
status label | Word identifying whether an item is requested, pending, or confirmed. | use a precise status label
current record | Latest accurate version of the client information. | verify the current record''',
    precision='The color consultation is requested but unbooked. Retained front length and no finishing spray are confirmed preferences. No promotional-photo agreement is recorded. These three statuses should not be compressed into a vague statement that the client agreed to everything.',
    precision_extra='Permission is purpose-specific. Do not infer promotional-image use from a completed service, a positive comment, or an unrecorded assumption. Use the actual salon process and applicable requirements for any later request involving taking or publishing images.',
    phrases='''Open the handover | I have two confirmed preferences and one unbooked request.\nState the first preference | Please retain the front length.\nState the second preference | The client does not want finishing spray.\nName the requested service | The client requested a future color consultation.\nKeep the status clear | The consultation is requested but not booked.\nAvoid inventing a date | No appointment date has been accepted.\nDistinguish service and image permission | Service consent does not establish promotional-photo permission.\nState the record accurately | No promotional-photo agreement is recorded.\nPrevent an assumption | Please do not mark that request as confirmed.\nAsk for a read-back | Can you repeat the confirmed preferences and pending request?\nCorrect a status | That should say requested, not booked.\nAssign the next contact | Who will handle the next booking discussion?\nKeep follow-up limited | Follow-up will address availability, not assume acceptance.\nKeep the details separate | The no-spray preference is not a color-service decision.\nConfirm the record | The profile should preserve these exact distinctions.\nClose the handover | Two preferences confirmed; consultation unbooked; photo agreement absent.''',
    notes='''Requested versus booked | Interest or a request does not establish an accepted appointment.\nRetain versus remove | Retain means keep the specified length rather than shorten it.\nNo spray | This is a product-use preference, not permission for every other product.\nRecorded versus assumed | A documented agreement differs from a colleague's inference.\nPurpose-specific permission | Agreement to a service does not automatically cover promotional use of an image.\nRead-back | Repeating the status words catches errors that a general acknowledgment may miss.''',
    d='''Which handover is accurate? | Retain front length; no spray; color consultation requested but unbooked. | Color treatment booked and product choices unrestricted. | Consultation completed and date accepted. | Spray approved unless the client objects again. | The correct handover preserves both confirmed preferences and the unbooked request.
What does no promotional-photo agreement recorded mean? | Do not treat promotional use as authorized. | Permission is automatic after a paid service. | A colleague can assume unlimited publication. | The client approved every channel. | Absence of a recorded agreement does not supply permission for promotional use.
Which label should replace an inaccurate booked entry? | Requested, not booked | Completed | Paid in full | Automatically renewed | Requested reflects the client's interest without inventing an accepted date.
Which read-back catches a meaningful error? | No date accepted; the consultation remains unbooked. | Everything is fine. | I remember the client. | We always do it this way. | The specific read-back verifies the unresolved booking status rather than offering a vague acknowledgment.''',
    dialogue='''Sora | Before you take over at reception, I want to pass on two confirmed preferences and one request that still needs a booking discussion.
Jordan | Go ahead. I will keep the [[preference notes::Preference notes hold the client's confirmed front-length and no-spray choices, separate from the future consultation request.]] separate from the appointment status so an interest in a service does not accidentally become a confirmed booking.
Sora | The client wants the front length retained and does not want finishing spray. Those are the two preferences confirmed during today's conversation.
Jordan | I have [[front-length retention::Front-length retention means keeping the specified front length, not shortening it or treating the preference as a complete future haircut instruction.]] as the first preference. I will record it directly rather than summarizing it as a general request for a different haircut.
Sora | Thank you. Please keep the no-spray point equally clear. I do not want it lost inside a broad note that says the client likes a natural look.
Jordan | Agreed. The [[no-spray preference::No-spray preference explicitly records that finishing spray is not wanted; a vague description of appearance could omit that product-use boundary.]] will be its own entry. A description of the desired look would not communicate that product-use choice as precisely.
Sora | The other point is a future color consultation. The client asked about arranging one, but we did not choose or agree on a date.
Jordan | Then that is a [[consultation request::Consultation request records interest in arranging the future discussion, not an accepted appointment or authorization for a color treatment.]], not a confirmed appointment. I will not mark a color service as booked merely because the client raised the idea.
Sora | Correct. It is a consultation request specifically, not an agreement to have color applied. The next conversation should address available appointments.
Jordan | I will leave the [[booking status::Booking status remains unbooked because no date has been accepted, even though the client has expressed a clear request.]] as unbooked. A later discussion can confirm a date, but the current record should not claim that has already happened.
Sora | There is also a photography point. No agreement to promotional photographs is recorded, so please do not tell anyone that permission was given today.
Jordan | Understood. [[Service consent::Service consent concerns the salon service and does not automatically grant permission to take or use photographs for promotion.]] does not establish permission for promotional images. I will keep that distinction rather than assuming the visit itself covered photography.
Sora | Exactly. A positive comment about the appointment would not change that. Any later image request needs its own clear conversation through the salon process.
Jordan | The [[permission scope::Permission scope is the specific use covered by an agreement; no promotional-photo agreement is present in the current record.]] matters. We cannot turn an absent agreement into permission for a website, portfolio, or another promotional channel.
Sora | Could you read back the main points now? There are only a few, but the difference between requested and booked is easy to lose.
Jordan | My [[read-back::Read-back repeats the exact preferences and statuses so Sora can catch any changed meaning before the handover ends.]] is: retain front length, no finishing spray, future color consultation requested but unbooked, and no promotional-photo agreement recorded.
Sora | That is correct. Please use those status words in the record, and keep the booking discussion separate from the product preference.
Jordan | I will make the [[record amendment::Record amendment is the accurate update preserving the confirmed preferences and unbooked request, not a change to what the client has authorized.]] accordingly. The no-spray preference does not select a color service, and the color request does not change the retained-length preference.
Sora | Good. Reception can handle the next discussion about availability, but please confirm the date with the client instead of treating an offered slot as accepted.
Jordan | Reception will be the [[next contact owner::Next contact owner identifies who will handle the later availability discussion while leaving acceptance and booking still pending.]]. We will discuss availability and seek confirmation, with the current record accurately showing two preferences, an unbooked request, and no photo agreement.''',
    transfer_title='Read back a new client handover',
    transfer_setup='The client confirms retained side length and no finishing spray. A future styling consultation is requested but unbooked. Reception will handle the next availability discussion. No promotional-image agreement is recorded.',
    transfer='''Stylist: "Please retain the ___ length." | side | The confirmed retained-length preference concerns the sides in this new case.
Reception: "The consultation is requested but ___." | unbooked | No accepted appointment has been established by the request alone.
Stylist: "The next availability discussion belongs to ___." | reception | Reception is explicitly assigned the next contact in the supplied handover.
Reception: "No promotional-image agreement is ___." | recorded | The record contains no agreement authorizing promotional image use.'''
))
